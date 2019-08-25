---
layout: post
title: "Understanding MRI scans"
description: "Handling DICOM planes"
categories: ["DICOM", "3D-Geometry", "MRI", "Sagittal", "Axial", "Coronal"]
location: "Bangalore, India"
---

Magnetic Resonance Imaging (MRI) is imaging technique used by radiologist to take pictures of body. It uses strong magnetic field to generate images of organs of body. In few cases Gadolinium Contrast Medium is injected into the body so that radiologist can take enhanced quality images during MRI.

{% include image.html url="/images/mri_machine.jpeg" caption="" max_width="100px"%}
MRI machine takes multiple images in 3 different planes (sagittal, coronal and transverse plane).

{% include image.html url="/images/plane_description.jpeg" caption="" max_width="100px"%}
The <b>sagittal</b> or lateral plane dives the body into left and right halves and is an x-z plane. Technically, the sagittal or median plane goes right through the middle between the body’s left and right halves. It is called the sagittal plane because it goes through or is parallel to the sagittal suture, the line running along the top of the skull that marks where the left and right halves of the skull grew together.

<div>
  <!--{% include image.html url="/images/cervical_view.jpeg" caption="" max_width="100px"%}
  {% include image.html url="/images/lumbar_view.jpeg" caption="" max_width="100px"%}-->
  <img src="/images/cervical_view.jpeg" width="256" height="256" align="middle"/>
  <img src="/images/lumbar_view.jpeg" width="256" height="256" align="middle"/>
</div>

The coronal or frontal planes divide the body into front and back (also called dorsal and ventral or posterior and anterior) sections and are x-y planes.
<br>
{% include image.html url="/images/coronal_view.jpeg" caption="" max_width="100px"%}


The transverse planes, also known as the axial or horizontal planes, are parallel to the ground and divide the body into top and bottom parts. The top and bottom sections also called the superior and inferior section s or the cranial (head) and caudal (trial) sections). They are x-z planes. Transverse plane is also called as axial plane.
<br>
{% include image.html url="/images/axial_view.jpeg" caption="" max_width="100px"%}

It can be seen that these planes will intersect each other. Depending on the orientation of the plane it can either cut the other plane in 1 line or a trapezium.
The general 2 types of MRI scans are T1 and T2 scans. T here referes to time constant. To understand the difference between T1 and T2 we need to know how MRI works.

## Working of MRI

A strong magnetic field is switched on which aligns proton that are normally randomly oriented withing the region of tissue being examined. This alignment of the nuclei is disturbed by applying Radio Frequency(RF) Energy. The RF energy is for an instant and then the disturbed nuclei starts to come back to original position and during that process they emit RF energy. The emitted energy is then captured and processed accordingly to get the image. By varying the sequence of RF pulses applied & collected, different types of images are created.
Now, the tissues can be characterized by two different relaxation times T1 and T2. <b>T1 (longitudinal relaxation time)</b> is the time constant which determines the rate at which excited protons return to equilibrium. It is a measure of the time taken for spinning protons to realign with the external magnetic field. <b>T2 (transverse relaxation time)</b> is the time constant which determines the rate at which excited protons reach equilibrium or go out of phase with each other. It is a measure of the time taken for spinning protons to lose phase coherence among the nuclei spinning perpendicular to the main field.

## Working with DICOM files

MRI images are generally available in DICOM format and to deal with DICOM images in python a library named <i><a href="https://pydicom.github.io/pydicom/stable/getting_started.html" target="_blank">pydicom</a></i> is available.
To read image we use <i>pydicom.dcmread(filepath)</i> function, to store the image as numpy array use <i>pixel_array</i> on return type of dcmread.
<br>
<br>
Since MRI images are taken for diagnostics purpose so just pixels information is not enough, we need more information like what is the area covered by the image, what is the orientation of each planes in 3 dimensional space. These information is helpful to map the image to 3 dimensional space and thus it makes more sense to diagnose with that information.
PixelSpacing returns distance between each pixels in mm in both x and y direction. ImageOrientationPatient returns direction cosines of the first row and first column (in the direction away from the top left point) with respect to 3 dimensional space and at last ImagePositionPatient returns the x,y and z coordinate (i.e. the position w.r.t. to the origin) of the top left pixel of image.
<br>
<br>
These information is sufficient to get each position w.r.t. to origin of each pixels in image. There are plenty of other features available by pydicom which returns other information (refer to <i><a href="https://pydicom.github.io/pydicom/stable/getting_started.html" target="_blank">pydicom</a></i> documentation). But for this series of post this information will be enough

## Projection of point in MRI plane

How to project a pixel location in image to one of the other plane? Here we will use 3D coordinate geometry to do that.
<br>
<br>
The general idea is to convert that pixel location to (x,y,z) coordinate then use project that coordinate to target plane with direction cosines and point available from ImageOrientationPatient and ImagePositionPatient. Then at last we convert that projected (x,y,z) coordinate to the pixel location.
<br>
<br>
Let’s say we want to find <i>(x,y,z)</i> of pixel <i>(i,j)</i> in dcm file ds. We first find (x,y,z) of pixel (0, j) (call it a)then from that we calculate (x,y,z) of (i,j) (lets call it b).
<br>

```
This is a code block
  a_x = ds.ImagePositionPatient[0] + j*ds.ImageOrientationPatient[0]
  a_y = ds.ImagePositionPatient[1] + j*ds.ImageOrientationPatient[1]

```
<br>
<code>
  a_z = ds.ImagePositionPatient[2] + j*ds.ImageOrientationPatient[2]
</code>
<br>
<code>
  b_x = a_x + i*ds.ImageOrientationPatient[3]
</code>
<br>
<code>
  b_y = a_y + i*ds.ImageOrientationPatient[4]
</code>
<br>
<code>
  b_z = a_z + i*ds.ImageOrientationPatient[5]
</code>

Now we project (b_x, b_y, b_z) to target plane (ds_trgt))direction cosines of rows and column as dc_r and dc_c.
{% include image.html url="/images/point.png" caption="" max_width="100px"%}
<code>
  trgt_x = ds_trgt.ImagePositionPatient[0]
</code>
<br>
<code>
  trgt_y = ds_trgt.ImagePositionPatient[1]
</code>
<br>
<code>
  trgt_z = ds_trgt.ImagePositionPatient[2]
</code>
<br>
<code>
  nrml_vctr = np.cross(dc_r, dc_c)
</code>
<br>
<code>
  t_denom = np.dot(nrml_vctr, nrml_vctr)
</code>
<br>
<code>
  t_num = vctr[0]*(trgt_x —b_x[0]) + vctr[1]*(trgt_y — b_y[1]) + vctr[2]*(trgt_z— b_z[2])
</code>
<br>
<code>
  t= t_num/t_denom
</code>
<br>
<code>
  x = b_x+ t*normal_vector[0]
</code>
<br>
<code>
  y = b_y+ t*normal_vector[1]
</code>
<br>
<code>
  z = b_z+ t*normal_vector[2]
</code>

The (x,y,z) is the projected point in target plane. If you have understood the math then you would know we simply used 3D geometry concepts. We can convert the coordinates to the pixel location using inverse of logic we used to find coordinates from point.
<br>
<b>We use this method because the widely circulated matrix multiplication technique used to find the projected point in DICOM doesn’t work. So I had to come up with this long method.</b>

## Reference
<ol>
  <li><a href="https://insideradiology.com.au/gadolinium-contrast-medium/" target="_blank">https://www.insideradiology.com.au/gadolinium-contrast-medium/</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Magnetic_resonance_imaging" target="_blank">https://en.wikipedia.org/wiki/Magnetic_resonance_imaging</a></li>
  <li><a href="https://www.machinedesign.com/medical/what-s-difference-between-sagittal-coronal-and-transverse-planes" target="_blank">https://www.machinedesign.com/medical/what-s-difference-between-sagittal-coronal-and-transverse-planes</a></li>
  <li><a href="http://casemed.case.edu/clerkships/neurology/web%20neurorad/mri%20basics.htm" target="_blank">http://casemed.case.edu/clerkships/neurology/web%20neurorad/mri%20basics.htm</a></li>
  <li><a href="https://en.wikipedia.org/wiki/DICOM" target="_blank">https://en.wikipedia.org/wiki/DICOM</a></li>
  <li><a href="https://pydicom.github.io/pydicom/stable/getting_started.html" target="_blank">https://pydicom.github.io/pydicom/stable/getting_started.html</a></li>
</ol>

{% include test_disqus.html %}

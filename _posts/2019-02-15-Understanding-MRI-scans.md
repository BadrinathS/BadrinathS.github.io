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
  <img src="/images/cervical_view.jpeg" width="256" height="256" align="center"/>
  <img src="/images/lumbar_view.jpeg" width="256" height="256" align="center"/>
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
Since MRI images are taken for diagnostics purpose so just pixels information is not enough, we need more information like what is the area covered by the image, what is the orientation of each planes in 3 dimensional space. These information is helpful to map the image to 3 dimensional space and thus it makes more sense to diagnose with that information.
PixelSpacing returns distance between each pixels in mm in both x and y direction. ImageOrientationPatient returns direction cosines of the first row and first column (in the direction away from the top left point) with respect to 3 dimensional space and at last ImagePositionPatient returns the x,y and z coordinate (i.e. the position w.r.t. to the origin) of the top left pixel of image.
{% include test_disqus.html %}

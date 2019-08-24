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
  <img src="/images/cervical_view.jpeg"/>
  <img src="/images/lumbar_view.jpeg"/>
</div>

The coronal or frontal planes divide the body into front and back (also called dorsal and ventral or posterior and anterior) sections and are x-y planes.
<br>
{% include image.html url="/images/coronal_view.jpeg" caption="" max_width="100px"%}


The transverse planes, also known as the axial or horizontal planes, are parallel to the ground and divide the body into top and bottom parts. The top and bottom sections also called the superior and inferior section s or the cranial (head) and caudal (trial) sections). They are x-z planes. Transverse plane is also called as axial plane.
<br>
{% include image.html url="/images/axial_view.jpeg" caption="" max_width="100px"%}

It can be seen that these planes will intersect each other. Depending on the orientation of the plane it can either cut the other plane in 1 line or a trapezium.
The general 2 types of MRI scans are T1 and T2 scans. T here referes to time constant. To understand the difference between T1 and T2 we need to know how MRI works.
{% include test_disqus.html %}

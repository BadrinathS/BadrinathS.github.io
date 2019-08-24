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

<div style="display:flex">
     <div style="flex:1;padding-right:5px;">
          <img src="/images/cervical_view.jpeg" width="256" height="256">
     </div>
     <div style="flex:1;padding-left:5px;">
          <img src="/images/lumbar_view.jpeg" width="256" height="256">
     </div>
</div>
.imgContainer{
    float:left;
}

<div class="Sagittal View">
    <div class="imgContainer">
        <img src="/images/cervical_view.jpeg" height="200" width="200"/>
        <p>This is Cervical scan</p>
    </div>
    <div class="imgContainer">
        <img class="middle-img" src="/images/lumbar_view.jpeg"/ height="200" width="200"/>
        <p>This is Lumbar scan</p>
    </div>
</div>

{% include test_disqus.html %}

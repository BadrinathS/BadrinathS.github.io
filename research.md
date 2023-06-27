---
layout: page
permalink: /research/
title: Research
pubs:

    - title:   "Spinal Stenosis Detection in MRI using Modular Coordinate Convolutional Attention Networks"
      author:  "Uddeshya Upadhyay, Badrinath Singhal, Meenakshi Singh"
      conference: "Internation Joint Conference on Neural Networks"
      note:    "Budapest, Hungary"
      year:    "2019"
      url:     "/resume/IJCNN_2019.pdf"
    #  doi:     "http://dx.doi.org"
      image:   "/images/Ijcnn_paper_thumbnail.jpg"
      media:
        - name: "Talk"
          url:  "/resume/IJCNN19_Synapsica_Presentation.pdf"

    - title:   "Performance Analysis of a Novel IT2 FCM Algorithm"
      author:  "Shashank Anil Huddedar, Mayank Kagliwal, Badrinath Singhal and Frank Rhee"
      conference: "World Congress on Computational Intelligence"
      note:    "Rio, Brazil"
      year:    "2018"
      url:     "/resume/IEEE_WCCI2018.pdf"
    #  doi:     "http://dx.doi.org"
      image:   "/images/fuzzy_paper_thumbnail.png"
      media:
        - name: "Talk"
          url:  "/resume/wcci_fuzzy.pdf"

projects:

    - title:   "Measurement of Spinal Canal Diameter for detection of Spinal Stenosis from axial MRI scans."
      about: "Measuring spinal canal diameter in axial image of MRI scan to assist radiologists for diagnosing Spinal Stenosis. Used a network called Co-Unet which is combination of Coordinate Convolution and U-Net to make a two stage architecture. First stage called Attention Network crops out the region contaning spinal canal, second stage called Canal Measurement Network that measures canal diameter. Both the stages uses image segmentation approach which is trained with loss function consisting of MSE and dice loss. Approach was tested on 392 unique axial scans out of which 13 axials have error more than 2mm."
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
      year:    "2019"
    #  url:     "https://drive.google.com/open?id=1e616rdl3sSzC8woABygdQH4rdflWKa6q"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
      media:
        - name: "Github"
          url:  "https://github.com/BadrinathS/Spinal_Canal_Measurement"


    - title:   "Listhesis evaluation from sagittal MRI scans"
      about: "We diagnose Listhesis in MRI scan using the sagittal scan. Vertebrae is detected in sagittal scan using YOLO v3 detector, we further crop out each vertebrae and train a CNN based points regresser to fit 6 points at the border of vertebrae. With the border available we calculate vertebrae slippage with the available 6 points, based on the slippage and combining it with other factors such as spine curvature, disc protusion we diagnose the degree of listhesis (if any) in the patient. When evaluated listhesis and compared with previous works, the 6 points approach showed better results compared to the approach mentioned in previous works. Part of our work is documented and made available."
    #  author:  "Uddeshya Upadhyay, Badrinath Singhal, Meenakshi Singh"
    # conference: "Internation Joint Conference on Neural Networks"
    #  note:    "(presented at Budapest, Hungary)"
      year:    "2019"
    #  url:     "https://drive.google.com/open?id=1N7KBbhoRMZ-RvuL-nfamC2RdM_wrqifM"
    #  doi:     "http://dx.doi.org"
    #  image:   "/images/Ijcnn_paper_thumbnail.jpg"
      media:
        - name: "Github"
          url:  "https://github.com/BadrinathS/Listhesis-evaluation-from-sagittal-MRI-scans"


---

## Publications (peer reviewed)

{% assign thumbnail="left" %}

{% for pub in page.pubs %}
{% if pub.image %}
{% include image.html url=pub.image caption="" height="100px" align=thumbnail %}
{% endif %}
[**{{pub.title}}**]({% if pub.internal %}{{pub.url | prepend: site.baseurl}}{% else %}{{pub.url}}{% endif %})<br />
{{pub.author}}<br />
*{{pub.conference}}*
{% if pub.note %} *({{pub.note}})*
{% endif %} *{{pub.year}}* {% if pub.doi %}[[doi]({{pub.doi}})]{% endif %}
{% if pub.media %}<br />Media: {% for article in pub.media %}[[{{article.name}}]({{article.url}})]{% endfor %}{% endif %}

{% endfor %}

<hr>

## Projects
{% assign thumbnail="left" %}

{% for pub in page.projects %}
{% if pub.image %}
{% include image.html url=pub.image caption="" height="100px" align=thumbnail %}
{% endif %}
[**{{pub.title}}**]({% if pub.internal %}{{pub.url | prepend: site.baseurl}}{% else %}{{pub.url}}{% endif %})<br />
{{pub.about}}<br />
{{pub.journal}}
{% if pub.note %} *({{pub.note}})*
{% endif %} {{pub.year}} {% if pub.doi %}[[doi]({{pub.doi}})]{% endif %}
{% if pub.media %}<br />Code: {% for article in pub.media %}[[{{article.name}}]({{article.url}})]{% endfor %}{% endif %}

{% endfor %}

<!--<ul>
#    <li><b><u>Synapsica Spindle:</u></b><br> This project is for performing diagnosing spinal stenosis </li>
#    <li><b><u>Efficient VLSI Implementation of SVD using CORDIC</u></b></li>
#    <li><b><u>Multi IT2 FCM Algorithm</u></b></li>
#    <li><b><u>Pattern Recognition and Machine Learning (PRML) algorithm implementation</u></b></li>
#    <li><b><u>Autonomous Intelligent Robot</u></b></li>
#    <li><b><u>Image Processing Algorithms implementation</u></b></li>
#</ul>-->

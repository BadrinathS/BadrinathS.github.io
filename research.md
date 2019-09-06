---
layout: page
permalink: /research/
title: Research
pubs:

    - title:   "Spinal Stenosis Detection in MRI using Modular Coordinate Convolutional Attention Networks"
      author:  "Uddeshya Upadhyay, Badrinath Singhal, Meenakshi Singh"
      conference: "Internation Joint Conference on Neural Networks"
      note:    "(presented at Budapest, Hungary)"
      year:    "2019"
      url:     "https://drive.google.com/open?id=1e616rdl3sSzC8woABygdQH4rdflWKa6q"
    #  doi:     "http://dx.doi.org"
      image:   "/images/Ijcnn_paper_thumbnail.jpg"
      media:
        - name: "Talk"
          url:  "https://drive.google.com/open?id=1uSlK-YbxPpXahhAKOOF0B_HHH4uay_i0"

    - title:   "Performance Analysis of a Novel IT2 FCM Algorithm"
      author:  "Shashank Anil Huddedar, Mayank Kagliwal, Badrinath Singhal and Frank Rhee"
      conference: "World Congress on Computational Intelligence"
      note:    "(presented at Rio, Brazil)"
      year:    "2018"
      url:     "https://ieeexplore.ieee.org/document/8491457"
    #  doi:     "http://dx.doi.org"
      image:   "/images/fuzzy_paper_thumbnail.png"
      media:
      #  - name: "IMDB"
      #   url:  "http://www.imdb.com/title/tt0133093/"
      
      
    - title:   "Spondylolisthesis Grading in sagittal MRI scans using convolutional neural networks"
      author:  "Badrinath Singhal, Meenakshi Singh, Vivek Kumaran"
      conference: "Association for the Advancement of Artificial Intelligence"
      note:    "(Submitted)"
      year:    "2019"
    #  url:     "https://drive.google.com/open?id=1e616rdl3sSzC8woABygdQH4rdflWKa6q"
    #  doi:     "http://dx.doi.org"
      image:   "/images/C6_4points.jpg"
    # media:
    #    - name: "Talk"
    #      url:  "https://drive.google.com/open?id=1uSlK-YbxPpXahhAKOOF0B_HHH4uay_i0"

    #- title:   "Paper title in 3-7 words that sound like Clingon"
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
    #  year:    "2014"
    #  url:     "http://publish-more-stuff.org"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
    #  media:
    #    - name: "IMDB"
    #      url:  "http://www.imdb.com/title/tt0133093/"



projects:

    - title:   "Measurement of Spinal Canal Diameter for detection of Spinal Stenosis from axial MRI scans."
      about: "Measuring spinal canal diameter in axial image of MRI scan to assist radiologists for diagnosing Spinal Stenosis. Used a network called Co-Unet which is combination of Coordinate Convolution and U-Net to make a two stage architecture. First stage called Attention Network crops out the region contaning spinal canal, second stage called Canal Measurement Network that measures canal diameter. Both the stages uses image segmentation approach which is trained with loss function consisting of MSE and dice loss. Approach was tested on 392 unique axial scans out of which 13 axials have error more than 2mm."
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
      year:    "2019"
      url:     "https://drive.google.com/open?id=1e616rdl3sSzC8woABygdQH4rdflWKa6q"
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
      url:     "https://drive.google.com/open?id=1N7KBbhoRMZ-RvuL-nfamC2RdM_wrqifM"
    #  doi:     "http://dx.doi.org"
    #  image:   "/images/Ijcnn_paper_thumbnail.jpg"
      media:
        - name: "Github"
          url:  "https://github.com/BadrinathS/Listhesis-evaluation-from-sagittal-MRI-scans"

    - title:   "Efficient VLSI Implementation of SVD using CORDIC"
      about: "In this work, we developed a way to calculate SVD of a nxn matrix which consists of operations that can be implemented on VLSI architecture. CORDIC algorithm was used to implement SVD for 2x2 matrix which was further tested in Verilog. For nxn matrix (n>2) we performed series of operations consisting of rotation, shifting, 2x2 SVD to calculate its SVD. We converted each operations such that every operations can be implementated in VLSI architecture. We further tested the approach in Matlab and Verilog."
    #  author:  "Shashank Anil Huddedar, Mayank Kagliwal, Badrinath Singhal and Frank Rhee"
    #  conference: "World Congress on Computational Intelligence"
    #  note:    "(presented at Rio, Brazil)"
      year:    "2018"
      url:     "https://drive.google.com/file/d/1eJkaH5ya5W21vP_sl2sDE4hzz6AFCm7D/view?usp=sharing"
    #  doi:     "http://dx.doi.org"
    #  image:   "/images/fuzzy_paper_thumbnail.png"
      media:
        - name: "Github"
          url:  "https://github.com/BadrinathS/Efficient-VLSI-Implementation-of-SVD"

    - title:   "Multi IT2 FCM Algorithm"
      about: " Integrated Multi-EIASC Algorithm with IT2 Fuzzy C-Means Clustering Algorithm to give Multi-IT2 Fuzzy C-Means Algorithm. Instead of using the EIASC algorithm over each of the dimensions of pattern sets separately, we used Multi-EIASC algorithm for the complete pattern set which uses ndimensionality of pattern sets as its fundamental property"
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
      year:    "2017"
      url:     "https://ieeexplore.ieee.org/document/8491457"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
      media:
        - name: "Github"
          #url:  "https://github.com/BadrinathS/Multi-IT2-FCM"
    
    
    #- title:   "Pattern Recognition and Machine Learning (PRML) algorithm implementation"
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
    #  year:    "2014"
    #  url:     "http://publish-more-stuff.org"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
    #  media:
    #    - name: "IMDB"
    #      url:  "http://www.imdb.com/title/tt0133093/"
  
  
    - title:   "Autonomous Intelligent Robot"
      about: "Developed a robot based on turtle bot which was capable of mapping the indoor enviornment, locate itself and reach from its current position to goal position avoiding the obstacles in between. We used Robot Operating System (ROS) as a platform to implement the required algorithms, Microsoft Kinect to map the indoor enviornment, DC Servo Motor and Arduino to provide commands to move around. We used RANSAC algorithm to stich the images during mapping purpose and Dijkstra Algorithm for calculating the path to goal position. We further used I2C communication to pass signal to DC Servo Motor "
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
      year:    "2014"
    #  url:     "http://publish-more-stuff.org"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
    #  media:
    #    - name: "IMDB"
    #      url:  "http://www.imdb.com/title/tt0133093/"
    

    #- title:   "Image Processing Algorithms implementation"
    #  author:  "M. McFly, D. Kirk, L. Skywalker, H.J. Potter, I. Jones, H. Houdini"
    #  journal: "Transactions on Black Magic"
    #  note:    "(presented at Oz)"
    #  year:    "2014"
    #  url:     "http://publish-more-stuff.org"
    #  doi:     "http://dx.doi.org"
    #  image:   "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.moviepostershop.com%2Fthe-matrix-movie-poster-1999-#1020518087.jpg&f=1"
    #  media:
    #    - name: "IMDB"
    #      url:  "http://www.imdb.com/title/tt0133093/"


---

## Publications (peer reviewed)

{% assign thumbnail="left" %}

{% for pub in page.pubs %}
{% if pub.image %}
{% include image.html url=pub.image caption="" height="100px" align=thumbnail %}
{% endif %}
[**{{pub.title}}**]({% if pub.internal %}{{pub.url | prepend: site.baseurl}}{% else %}{{pub.url}}{% endif %})<br />
{{pub.author}}<br />
*{{pub.journal}}*
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

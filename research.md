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
      url:     "http://publish-more-stuff.org"
      doi:     "http://dx.doi.org"
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
      doi:     "http://dx.doi.org"
      image:   "/images/fuzzy_paper_thumbnail.png"
      media:
      #  - name: "IMDB"
      #   url:  "http://www.imdb.com/title/tt0133093/"

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

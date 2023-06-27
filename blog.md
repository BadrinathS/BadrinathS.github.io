---
layout: page
title: Blog
permalink: /blog/
---

Sometimes I write something here, its mostly to practise writing or make notes or sometimes for no reason at all. 

<ul class="listing">
<a href="/resume/Counterfactuals_Basics.pdf">2021-08-25: Counteractuals Basics</a>
<br>
<a href="/resume/CT-3DMorphableModels.pdf">2021-07-26: 3D Morphable Models</a>
<br>
<a href="/resume/Spatial_Pyramid_Pooling.pdf">2021-05-22: Spatial Pyramid Pooling</a>
<br>
<a href="/resume/The_Morning_Star.pdf">2021-03-31: The Morning Star</a>
<br>
<a href="/resume/Plastics.pdf">2021-03-23: Plastics</a>
<br>
<a href= "/resume/Initialisation_Strategies.pdf">2021-03-20: Initialisation Strategies</a>
<br>
 <a href= "/resume/Bias_and_Variance.pdf">2021-03-19: Bias and Variance </a>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    <a href="{{ post.url | prepend: site.baseurl }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
 
</ul>

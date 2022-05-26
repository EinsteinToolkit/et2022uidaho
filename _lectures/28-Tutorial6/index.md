---
layout: default
usemathjax: true
title: "Tutorial: Post-processing Cactus simulations with Python"
author: Gabriele Bozzola
institution: University of Arizona
shortinst: UA
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

kuibit is a Python library for quantitative post-processing and visualization of
Cactus simulations. In this tutorial, I will first introduce the package and
present some of its design choices. Then, I will walk through the first steps
for new users, including installation, setup, and running some provided
examples. Next, I will develop a script from scratch for a new analysis and
visualization. In doing this, I will discuss some of the most important aspects
of the library.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

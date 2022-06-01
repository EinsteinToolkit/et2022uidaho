---
layout: default
usemathjax: true
title: "Jhuki: a Python library for ET parameter file preparation"
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

Preparing a new parameter file for Einstein Toolkit simulation can be a nuanced task. In this talk, I'll present Jhuki, a Python library to simplify the process. Jhuki provides abstractions that automatically take care of several low-level details, dramatically reducing errors and improving extensibility and reusability of parameter files. Jhuki is ideally suited for designing parametric studies. The library is open-source and under development.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Tutorial: Writing an Einstein Toolkit thorn"
author: Yosef Zlochower
institution: Rochester Institute of Technology
shortinst: RIT
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

This tutorial covers designing and implementing a new physics thorn within the Einstein Toolkit. The system considered here is the Maxwell equations for electromagnetic waves interacting with dielectrics. Topics will include: adding new Cactus grid variables, writing and scheduling functions that update these variables, adding custom runtime parameters, running the simulations, and simple visualizations of the results.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

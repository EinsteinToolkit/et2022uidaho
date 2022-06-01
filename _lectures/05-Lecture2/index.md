---
layout: default
usemathjax: true
title: "Relativistic Magnetohydrodynamics in Perspective"
author: Matt Duez
institution: Washington State University
shortinst: WSU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Numerical relativists are well aware of the important role of magnetic fields in the transportation of angular momentum and generation of jets in the post-merger state of the compact binaries we like to simulate. The dynamics of magnetized conducting flows can be quite rich, and we are lucky to inherit the insights of decades of non-relativistic work studying the solar and terrestrial dynamos, magnetospheres, magnetic confinement fusion, etc. Relativity doesn't complicate things too badly, and the mathematical machinery at our disposal is actually quite clarifying. I will give a quick exposition for those looking to jump into doing and interpreting MHD simulations of the big interconnected ideas: the frozen-in condition, force-free regions, helicity, and the mean-field treatment of dynamos.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Tutorial: GPUs and the Einstein Toolkit"
author: Lorenzo Ennoggi, Jay Kalinani, and Federico Lopez Armengol
institution: Rochester Institute of Technology and University of Padova 
shortinst: RIT and UNIPD
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

With an increasing demand of extensive parallel computing in numerical
simulations addressing various astrophysical problems, codes which can
efficiently work on GPUs are the need of the hour. In the first part
of this tutorial, we will provide a short introduction on CarpetX, a
new driver for the Einstein Toolkit. Next, we will briefly discuss
features of a new general relativistic (magneto)hydrodynamic code
AsterX, based on CarpetX, which is designed to work on GPUs. AsterX
also takes advantage of the block-structured adaptive mesh refinement
provided by CarpetX through the AMReX framework. The second part of
the tutorial will be a hands-on session during which participants will
work on a few basic examples based on CarpetX, followed by a test
simulation performed with AsterX on a GPU.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

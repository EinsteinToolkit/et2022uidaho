---
layout: default
usemathjax: true
title: "The GRChombo code base"
author: Thomas Helfer
institution: Johns Hopkins University
shortinst: JHU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/9FZb7ys-Wv0
---
{% include base.html %}

{%-capture abstract-%}

GRChombo is an open-source code for numerical relativity simulations first released in 2015. It is developed and maintained by a collaboration of numerical relativists with a wide range of research interests, from early universe cosmology to astrophysics and mathematical general relativity. GRChombo is written entirely in C++14, using hybrid MPI/OpenMP parallelism and vector intrinsics to achieve good performance on the latest architectures. Furthermore, it makes use of the Chombo library for adaptive mesh refinement to allow automatic increasing and decreasing of the grid resolution in regions of arbitrary shape and topology.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Visualizing black hole data with proxys"
author: Maria J. Rodriguez
institution: Utah State University
shortinst: USU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Employing computational methods in general relativity we can study the shadows for the static double black hole system (an exact solution to Einsetin's equations) that may be an informative proxy for a dynamical binary. Whereas the conical singularity between the binary configuration induces a discontinuity of the scattering angle of photons it produces no observable effect on the shadows, whose edges remain everywhere smooth.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

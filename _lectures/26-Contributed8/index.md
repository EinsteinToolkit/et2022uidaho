---
layout: default
usemathjax: true
title: "Contributed talk 9"
author: Chloe Richards
institution: University of Illinois at Urbana-Champaign
shortinst: UIUC
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Despite its success story to describe astrophysical phenomena, Einstein’s General Relativity is not a viable candidate for quantum gravity. Among the most popular extensions of general relativity are quadratic gravity theories. In this talk, we will present first results for black holes with a massive scalar field in dynamical Chern-Simons gravity, in which a dynamical pseudo-scalar field is coupled to the Pontryagin density. We have performed numerical relativity simulations of a single rotating black hole in this theory with a linear coupling of the scalar field.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Tutorial: The Black Hole Pertubation Toolkit"
author: Niels Warburton
institution: University College Dublin
shortinst: UC Dublin
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

The Black Hole Perturbation Toolkit is a collection of software and data relating to black hole perturbation theory. In this tutorial I will show how to use the Teukolsky Mathematica package, and related packages, to calculate waveforms for small mass ratio binaries. I will also show how to compare these waveforms with those from numerical relativity simulations. I will also demonstrate how to rapidly calculate waveforms for eccentric binaries using the python Fast EMRI Waveforms package.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

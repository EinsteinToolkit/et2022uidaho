---
layout: default
usemathjax: true
title: "Contributed talk 6"
author: Siddharth Mahesh
institution: West Virginia University
shortinst: WVU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

We describe new strategies adopted by our research group to improve the development, performance and accuracy of Effective-One-Body (EOB)-based spin-precessing waveform models. We accomplish this by developing EOB models through an intuitive, python-based implementation that meticulously documents the EOB physics and the corresponding code in Jupyter notebooks. We then build on this implementation by using our own python package NRPy+ to boost accuracy and performance of the current state-of-the-art approximant SEOBNRv4P. Strategies to accomplish this include the generation of analytical expressions for derivatives on the right-hand sides of the evolution equations and in the initial conditions, as well as the generation of highly optimized C-code to significantly boost performance. We discuss our progress in accomplishing these goals, and present results comparing our implementation to that in the LIGO Algorithms Library. We will also discuss future strategies to vastly improve performance by adopting elegant physically motivated integration techniques and merger models.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

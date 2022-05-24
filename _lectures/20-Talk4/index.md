---
layout: default
usemathjax: true
title: "The Elliptica initial data solver"
author: Alireza Rashti
institution: Florida Atlantic University
shortinst: FAU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

The gravitational wave detectors' sensitivity and accuracy are increasing. Therefore, we require highly accurate numerical simulations in order to interpret the observations and expand our understanding about the physics of astrophysical compact objects. On the other hand, the accuracy of dynamical evolution goes hand in hand with the accuracy of the initial data. Hence, constructing accurate initial data is an indispensable task for gaining further insight into the physics of gravitational systems. As such, we have developed a new infrastructure, named Elliptica, to make self-consistent, constraint-satisfying, and accurate initial data of various numerical relativity systems, such as, binary neutron stars and black hole neutron star binaries. Elliptica is a multi-domain pseudo-spectral code and uses a Schur complement domain decomposition method to solve elliptic partial differential equations. Here, we present the backbone of Elliptica and a few examples of its usage for black hole neutron star binary systems.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Multi-messenger Signals from Magnetized Binary Neutron Star Mergers"
author: Maria Babiuc Hamilton
institution: Marshall University
shortinst: Marshall University
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Neutron stars are fascinating astronomical objects, with huge magnetic fields and extreme gravity, at the limit of collapsing into a black hole. Binary neutron stars (BNS) can collide producing gravitational waves and amplifying their magnetic field to support “collimated jets” stretching for millions of light-years. The mechanism behind jet formation is yet unknown and numerical simulations can provide insight for understanding  its physics.  We simulate magnetized BNS mergers to understand how the magnetic field gets amplified, aiming to discern the key factors responsible for steering the production of detectable electromagnetic counterparts to the gravitational wave signals. This work addresses also the reproducibility of results by using publicly available, open-source software and documenting the workflow, which will enable researchers and students to regenerate the same findings and produce new results.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "Future of the Einstein Toolkit: CarpetX"
author: Lorenzo Ennoggi, Erik Schnetter
institution: Rochester Institute of Technology, Perimeter Institute
shortinst: RIT, PI
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/6bc8UPvIZGY
---
{% include base.html %}

{%-capture abstract-%}

CarpetX is a new "driver" for the Einstein Toolkit, using the AMReX exascale adaptive mesh refinement framework. I will describe the role of a driver in general, the new features that CarpetX provides, and how they can be used by physics code. These new features include: code that is simpler to write, various dataflow errors that are now automatically detected, improved discretization methods (e.g. conservation, higher order accuracy), and improved performance (e.g. multi-threading, GPUs).

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

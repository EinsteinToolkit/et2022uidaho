---
layout: default
usemathjax: true
title: "The Black Hole Perturbation Toolkit"
author: Barry Wardell
institution: University College Dublin
shortinst: UC Dublin
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/KDRg-Y91JNI
---
{% include base.html %}

{%-capture abstract-%}

The Black Hole Perturbation Toolkit brings together software and data relating to black hole perturbation theory. These can be used to model gravitational radiation from small mass ratio binaries as well as from the ringdown of black holes. The former are key sources for the future space-based gravitational wave detector, LISA. In this talk I will give an overview of the toolkit, including a summary of the tools it provides. 

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

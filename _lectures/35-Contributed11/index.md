---
layout: default
usemathjax: true
title: "BlackHoles@Home Update "
author: Zach Etienne
institution: University of Idaho
shortinst: UIdaho
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

BlackHoles@Home is a new, highly efficient numerical relativity code that fits binary black hole (BBH) simulations on consumer desktops. Its extreme efficiency enables the general public to participate in the creation of enormous and highly accurate BBH gravitational waveform catalogs, for the benefit of gravitational wave science. Over the past year the BlackHoles@Home infrastructure has been rewritten to facilitate simulations of not only the long BBH inspiral, but also its merger—both with improved efficiency and reliability. Further the Einstein Toolkit has been recast as an open-source library, which we leverage for state-of-the-art horizon diagnostics in BlackHoles@Home. An update on the volunteer computing/citizen science project will also be provided.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

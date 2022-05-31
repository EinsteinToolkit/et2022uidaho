---
layout: default
usemathjax: true
title: "An overview of numerical relativity"
author: Manuela Campanelli
institution: Rochester Institute of Technology
shortinst: RIT
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Gravitational-waves observations of several binary compact mergers heralded in a new kind of astronomy, one integrating its findings with those obtained from electromagnetic and/or neutrino observations. Multi-messenger astronomy promises to revolutionize our understanding of the universe by providing dramatically contrasting views of the same objects. To understand this unprecedented wealth of observational evidence, theoretical calculations are required in order to link data with underlying physics. However, these demand the creation of new computational tools that can handle an increasingly wide range of physical treatments, characteristic scales, and levels of complexity. I will present here my perspective on some of the key challenges, and on new exciting developments in the field of numerical relativity and computational astrophysics, keeping an eye on the future of the  Einstein Toolkit.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

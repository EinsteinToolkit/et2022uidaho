---
layout: default
usemathjax: true
title: "The SpEC and SpECTRE codes"
author: Geoffrey Lovelace
institution: California State University
shortinst: Cal State Fullerton
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

In this talk, I will present an overview of the SpEC and SpECTRE numerical-relativity codes developed by the SXS Collaboration, focusing primarily on the application of simulating merging binary black holes.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

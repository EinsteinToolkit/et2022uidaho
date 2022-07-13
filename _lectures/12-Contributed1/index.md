---
layout: default
usemathjax: true
title: "FUKA Initial data codes"
author: Samuel Tootle
institution: Goethe University, Frankfurt, Germany
shortinst: Goethe University
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/uZ0dlQRcl3E
---
{% include base.html %}

{%-capture abstract-%}

FUKA is a collection of publicly available initial data codes based on the KADATH spectral solver library.  The initial public release of the codes was in June 2021 with a short talk given at the ETK summer school 2021. My proposed talk this year will include a brief overview of FUKA for those unaware of the codes as well as discuss the revisions made in the past year to enable access to highly asymmetric spinning binaries and a brief demonstration of the minimal workflow required.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

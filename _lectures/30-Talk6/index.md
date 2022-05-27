---
layout: default
usemathjax: true
title: "The Spritz code"
author: Jay Kalinani
institution: University of Padova
shortinst: UNIPD
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Spritz is a fully general relativistic magnetohydrodynamic code
based on the Einstein Toolkit. In this talk, I will discuss some key
features of Spritz which include the implementation of high-resolution
shock capturing techniques, staggered vector potential formalism,
support for reading composition and temperature dependent EOS,
neutrino emission/re-absorption treatment, higher order methods, as
well as a new conservative-to-primitive (C2P) variable recovery scheme
'RePrimAnd'. I will also discuss the various tests performed to
validate the different implementations in Spritz, and then present the
latest results from the first binary neutron star merger simulations
performed with Spritz and RePrimAnd C2P scheme.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

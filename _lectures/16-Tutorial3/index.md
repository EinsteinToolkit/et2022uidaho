---
layout: default
usemathjax: true
title: "Tutorial: Extreme mass ratio inspirals in the Einstein Toolkit"
author: Samuel Cupp
institution: Louisiana State University
shortinst: LSU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

In binary mergers, the mass ratio plays a significant role in determining the behavior of the evolution. Numerical relativity techniques are strongly limited by this ratio, making the simulation of systems with small mass ratios computationally infeasible. However, the extreme-mass-ratio limit allows for a perturbative approach using the mass ratio. In this tutorial, I introduce and demonstrate the capabilities of the SelfForce-1D code, a code for simulating extreme-mass-ratio inspirals. The SelfForce-1D code implements the first-order perturbation equations for the scalar charge toy model, and code for the full gravitational case is under review for inclusion.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

{% include server_instructions.md %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
usemathjax: true
title: "The CurviGiRaFFE Code"
author: Terrence Pierre Jacques
institution: West Virginia University
shortinst: WVU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

CurviGiRaFFE is an in-development, dynamical-spacetime GRFFE code aimed at studying the magnetospheres of compact object binaries. Unlike its parent codes, IllinoisGRMHD and GiRaFFE, CurviGiRaFFE does not require use of Cartesian AMR grids, instead leveraging NRPy+ to solve the GRFFE equations in dynamical spacetimes on highly efficient bispherical-like coordinate grids. These grids, composed of overlapping spherical-like and Cartesian-like grid patches, exploit near-symmetries in binary compact object spacetimes reducing memory overhead by orders of magnitude over Cartesian AMR. This efficiency gain will enable CurviGiRaFFE to model interacting compact binary magnetospheres on high-end, consumer-grade desktop computers, so the vast parameter space of magnetosphere configurations can be explored with minimal computational expense. I will report on CurviGiRaFFE’s covariant GRFFE formulation and preliminary code test results.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

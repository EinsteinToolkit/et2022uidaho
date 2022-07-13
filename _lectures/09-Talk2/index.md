---
layout: default
usemathjax: true
title: "The SGRID initial data code"
author: Wolfgang Tichy
institution: Florida Atlantic University
shortinst: FAU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/hKAR-QHRjWI
---
{% include base.html %}

{%-capture abstract-%}

We give an introduction to the SGRID code that is intended to solve any 
partial differential equation (PDE). The principal spatial discretization 
used in SGRID is a pseudo-spectral method. Together with a Runge-Kutta time 
integrator it can be used to solve hyperbolic PDEs. In the past we have used 
it to evolve the BSSNOK equations for single excised black holes. However, 
we now mostly use it to solve elliptic PDEs. Currently SGRID's main 
application is to solve the conformal thin sandwich equations to construct 
initial data for binary neutron stars with arbitrary masses and spins. To 
deal with complicated spatial geometries such as excision regions, or 
spheroidal regions comprising the interior of star, the spatial domain is 
split into several patches that are each covered with their own coordinate 
system. In its own coordinates each patch ranges over a region that has the 
shape of a box, but via a coordinate transformation to global Cartesian 
coordinates each patch can be given a different shape. SGRID is OpenMP 
parallelized, by distributing loops over grid points or over patches among a 
desired number of threads. In this talk we explain the purpose and structure 
of SGRID. We also discuss how one uses it and how one can extend it.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

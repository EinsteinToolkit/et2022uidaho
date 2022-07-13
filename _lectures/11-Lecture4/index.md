---
layout: default
usemathjax: true
title: "The SpECTRE initial data solver"
author: Nils Vu
institution: Max Planck Institute for Gravitational Physics
shortinst: MPI
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/FAkVCHTzs-s
---
{% include base.html %}

{%-capture abstract-%}

The new SpECTRE code (currently in development by the SXS collaboration) is designed with parallelization at its core. With discontinuous Galerkin methods and a task-based approach to parallelism we are aiming for large-scale simulations on current and future supercomputers. The initial data solver for the code is based in these same principles. I outline the stack of task-based parallel iterative algorithms for the solution of elliptic equations that we have developed to solve initial data problems effectively on many cores. I show how our multigrid-Schwarz preconditioned Newton-Krylov solver achieves resolution-independent iteration counts, and how we solve for BBH initial data already about ten times faster than SpEC. Finally, I give a glimpse into interdisciplinary applications of our new fast elliptic solver.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

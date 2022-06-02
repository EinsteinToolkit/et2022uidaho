---
layout: default
usemathjax: true
title: "The NRPyElliptic initial data code"
author: Thiago Assumpção
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

To simulate black hole binaries, one must specify initial data that satisfy the Hamiltonian and momentum constraint equations, which are typically posed as elliptic PDEs. The NRPyElliptic code is an elliptic solver based on the hyperbolic relaxation method, whereby elliptic equations are transformed into hyperbolic equations. When evolved forward in (pseudo)time, the hyperbolic system exponentially reaches a steady state that solves the elliptic PDEs. In this talk, I will start with a brief overview of the conformal transverse-traceless (CTT) decomposition used to generate binary black-hole (puncture) initial data. I will then show how to use the NRPy+ framework to implement the Hamiltonian constraint equation in the CTT formalism, and generate highly optimized C code that comprises the backbone of the NRPyElliptic code. As an application, we will generate quasicircular initial data within the newly open-sourced NRPyElliptic Einstein Toolkit thorn. These data can be used to simulate the GW150914 gravitational-wave event.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

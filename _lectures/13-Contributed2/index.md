---
layout: default
usemathjax: true
title: "Quark Matter Conversion in Neutron Star Cores"
author: Prasad Ravichandran
institution: Indian Institute of Science Education and Research, Bhopal, India
shortinst: IISER
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: 
---
{% include base.html %}

{%-capture abstract-%}

In the dense cores of a neutron star, the nuclear matter is prone to undergo conversion to quark matter (phase-transition), which can result in the formation of quark/hybrid stars. A neutron star's central density is most likely to increase during its lifetime due to spin changes and mass accretion, resulting in the appearance of a small quark phase and a density discontinuity at the center. The discontinuity can lead to a shock wave, propagating outward and combusting the hadronic matter to quark matter in the region surpassed by it. Using one-dimensional general relativistic hydrodynamics code (GR1D) we have performed a simulation of such a scenario incorporating combustion equations. The simulation performed reveals the time of conversion to be 30-50 microseconds, which indicates a rapid process. The conversion time doesn't change much with the temperature of matter or the height of the initial discontinuity. We have also calculated the gravitational wave (GW) emission from this process, the GW from a source at 10 megaparsecs has an amplitude of the order 10^-21 and frequency in 150-300 kHz. These signals are unique from other known sources, and observing such signals could confirm the existence of quark stars.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

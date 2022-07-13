---
layout: default
usemathjax: true
title: "Docker containers and the Einstein Toolkit"
author: Matt Anderson
institution: Idaho National Laboratory
shortinst: INL
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/DWPE7WRH7aI
---
{% include base.html %}

{%-capture abstract-%}

Containers in scientific computing can make it much easier to deploy an application to multiple different supercomputing systems without having to rebuild the application. They can also reliably reproduce archival simulations that use codes that are no longer supported or have changed so much that they can't even be compiled against a modern software stack. This talk discusses how to prepare a container where mpirun is used to launch the container for running a simulation at system scale. In this modality, a user simply downloads a prepared container and can run a simulation at scale on any supercomputer without having to build the application for that system. Archival capabilities of this operation modality are also discussed.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

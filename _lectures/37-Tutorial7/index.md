---
layout: default
usemathjax: true
title: "Tutorial: Automatic Generation of Carpet/CarpetX Thorns with NRPy+"
author: Steve Brandt
institution: Louisiana State University
shortinst: LSU
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: https://github.com/stevenrbrandt/carpetx-install/blob/main/notebooks/NRPyWaveToy.ipynb
recording: https://youtu.be/d6VZYiAKvXc
---
{% include base.html %}

{%-capture abstract-%}

Creating a thorn for the Einstein Toolkit has been a
successful collaborative framework for numerical relativity.
For the last twenty-five years, groups from arround the
world have been contributing new physics and infrastructure
thorns.

And while the task of creating a thorn is not extraordinarily
difficult, there is still a non-trivial learning curve that
must be crossed before thorns can be correctly written.

The NRPy+ Python tools for using Sympy and generating physics
code simplified the creation of physics thorns by allowing
thorn authors to work with symbolic differential equations
without worrying about the details of loops and boilerplate
C++ code.

However, NRPy+ is not a Cactus-only tool and does not
automate all of the details of thorn generation.

This tutorial is about an addition to the NRPy+ toolset which
helps the authors of physics thorns cover this last mile.
While the tool is still in its early stages of develpoment,
it is usable and ready for community engagement. This tutorial
will show users how to create a wave equation thorn that will
compile and run both for the Carpet driver and the CarpetX
driver.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

{% include server_instructions.md %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

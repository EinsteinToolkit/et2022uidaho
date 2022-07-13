---
layout: default
usemathjax: true
title: "Tutorial: An Introduction to the Einstein Toolkit"
author: Roland Haas
institution: National Center for Supercomputing Applications 
shortinst: NCSA
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: 
recording: https://youtu.be/GK0VNUvdNm0
---
{% include base.html %}

{%-capture abstract-%}

This course covers the basics of the Einstein Toolkit:

1. A brief history;
2. what the Einstein Toolkit is and can do;
3. How to install the ET (including prerequisites);
4. How to run the ET and create a rudimentary plot of some of the data generated.

All of the above steps are carried out within a Jupyter notebook. This means that there are no hardware requirements for your computer.

Familiarity with the linux command line is required, and some minimal knowledge of Python is helpful.

Note that this course replicates the material available in the online tutorial.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

{% include server_instructions.md %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

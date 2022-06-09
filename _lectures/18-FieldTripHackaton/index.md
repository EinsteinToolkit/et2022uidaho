---
layout: default
usemathjax: true
title: "LIGO Hanford Field Trip / Hackaton"
author: The Scientific Organizing Committee
institution: University of Idaho
shortinst: Multiple institutions
# upload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: https://docs.einsteintoolkit.org/et-docs/ET_hackathon
recording: 
---
{% include base.html %}

{%-capture abstract-%}

Field Trip / Hackaton

## Hackathon

The hackathon uses different [Zoom link]([https://illinois.zoom.us/j/87051071723?pwd=Z2NMOVFHNnhIOWxJdDZ3VHNBSDJ0QT09 Zoom link]) than the main school and workshop. A Zoom account (of any type) is required to join and there will be a waiting room.

A list of proposed Hackathon tasks is available on the [Einstein Toolkit wiki](https://docs.einsteintoolkit.org/et-docs/ET_hackathon) and most topics can be found by searching for [hackathon](https://bitbucket.org/einsteintoolkit/tickets/issues?status=new&status=open&q=hackathon) in the ticket system.

If you intend to join the hackathon, please consider claiming a topic there in advance of the hackathon event.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>

---
layout: default
title: Contributed talks
---

{% for talk in site.data.contributed %}

<h2 id="{{talk.tag}}">{{forloop.index}}. {{ talk.title }}</h2>
<em>{{ talk.name }} ({{ talk.institution }})</em>
{%assign fn = '/contributed/' | append: talk.tag | append: '.pdf'-%}
{%-assign found = site.static_files | where: "path",fn | first-%}
{%-if found-%}
<a href="{{talk.tag}}.pdf">(slides)</a>
{%-endif%}

{{ talk.abstract }}

{% endfor %}

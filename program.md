---
layout: default
title: Scientific Program

# day schedules:
# a list of tags for each lecture
# a brak can be given as "breakX"
# 5 minutes breaks are added at the end of lectures where needed
# if no duration given it is assumed to be 45min for lectures and 20min for a break

start: "8:25"
end: "18:05"
# scheduling granularity. Must be no smaller than shortest scheduled item (eg
# the short break).
granularity: 300
# length of authomatic break between items, 0 to disable
short_break_duration: 300

day1:
  - Welcome:
      duration: 20
  - PlenaryTalk1:
      duration: 40
  - PlenaryTalk2:
      duration: 40
  - break:
      duration: 25
  - Lecture1:
      duration: 40
  - Lecture2:
      duration: 40
  - break:
      duration: 120
  - Tutorial1:
      duration: 105
  - break:
      duration: 30
  - Tutorial2:
      duration: 105

day2:
  - Talk1:
      duration: 40
  - Talk2:
      duration: 40
  - break:
      duration: 30
  - Lecture3:
      duration: 40
  - Lecture4:
      duration: 40
  - Contributed1:
      duration: 10
      nobreak: true
  - Contributed2:
      duration: 10
      nobreak: true
  - Contributed3:
      duration: 10
      nobreak: true
  - Contributed4:
      duration: 10
  - break:
      duration: 95
  - Talk3:
      duration: 40
  - Talk4:
      duration: 40
  - break:
      duration: 30
  - Tutorial3:
      duration: 105

day3:
  - FieldTripHackaton:
      duration: 580

day4:
  - Tutorial4:
      duration: 85
  - break:
      duration: 30
  - Lecture5:
      duration: 40
  - Lecture6:
      duration: 40
  - Contributed5:
      duration: 10
      nobreak: true
  - Contributed6:
      duration: 10
      nobreak: true
  - Contributed7:
      duration: 10
      nobreak: true
  - Contributed8:
      duration: 10
  - break:
      duration: 95
  - Tutorial5:
      duration: 105
  - break:
      duration: 30
  - Tutorial6:
      duration: 105

day5:
  - Talk5:
      duration: 40
  - Talk6:
      duration: 40
  - break:
      duration: 30
  - Lecture7:
      duration: 40
  - Lecture8:
      duration: 40
  - Contributed9:
      duration: 10
      nobreak: true
  - Contributed10:
      duration: 10
      nobreak: true
  - Contributed11:
      duration: 10
  - break:
      duration: 105
  - Tutorial7:
      duration: 105
  - break:
      duration: 30
  - Tutorial8:
      duration: 105

---

{% include base.html %}


<div class="col-xs-12">
<h1>Program</h1>

<!-- one of https://getbootstrap.com/docs/3.4/components/#alerts -->

</div>

<div class="col-xs-6">
<h2>Time zones</h2>

<div class="tzinfo" markdown="1">

|                       |                            Start                             |                            End                             |
|-----------------------|--------------------------------------------------------------|------------------------------------------------------------|
|    US Pacific Time    | {{page.start |                            date: "%I:%M %p"}} | {{page.end |                            date: "%I:%M %p"}} |
|    US Central Time    | {{page.start | date: "%s" | plus:  7200 | date: "%I:%M %p"}} | {{page.end | date: "%s" | plus:  7200 | date: "%I:%M %p"}} |
|    US Eastern Time    | {{page.start | date: "%s" | plus: 10800 | date: "%I:%M %p"}} | {{page.end | date: "%s" | plus: 10800 | date: "%I:%M %p"}} |
| Central European Time | {{page.start | date: "%s" | plus: 32400 | date: "%I:%M %p"}} | {{page.end | date: "%s" | plus: 32400 | date: "%I:%M %p"}} |
| [Other time zones](https://www.timeanddate.com/worldclock/converter.html?iso=20220214T220000&p1=3993&p2=195&p3=33&p4=248&p5=176&p6=64&p7=179) |  |

</div> <!--tzinfo-->
</div>

<div class="col-xs-12" markdown="1">
## Schedule overview

<div class="alert alert-warning" role="alert">
Tentative, subject to change without notice.
</div>

All times US Pacific time.

{% assign starttime = page.start | date: "%s" | plus: 0-%}
{%-assign endtime = page.end | date: "%s" | plus: 0-%}
{%-assign duration = endtime | minus: starttime | plus: page.granularity | minus: 1-%}
{%-assign maxrow = duration | divided_by: page.granularity | minus: 1%}

<table class="schedule">
<tr><th> time </th>
<th> Monday, June 13<sup>th</sup> </th>
<th> Tuesday, June 14<sup>th</sup> </th>
<th> Wednesday, June 15<sup>th</sup> </th>
<th> Thursday, June 16<sup>th</sup> </th>
<th> Friday, June 17<sup>th</sup> </th>
</tr>
{%-for row in (0..maxrow)-%}
  {%-comment-%} create information for row of time in alternating colours {%-endcomment-%}
  {%-assign time = row | times: page.granularity | plus: starttime | date: "%I:%M %p"-%}
  {%-assign half_hour = row | modulo: "6"-%}
  {%-comment-%} ensure final time block is exactly end at the final time but is not longer than 30minutes (6 units of 5 minutes) {%-endcomment-%}
  {%-assign timerows = maxrow | minus: row | plus: 1-%}
  {%-if timerows > 6-%}
    {%-assign timerows = 6-%}
  {%-endif-%}

  <tr>
  {%-comment-%} time column {%-endcomment-%}
  {%-if half_hour == 0 and timerows >= 0-%}
  <td class="time" rowspan={{timerows}} {% cycle "time": "style='background: #EEE'", ""-%}> {{time}}</td>
  {%-endif-%}

  {%-comment-%} program {%-endcomment-%}
  {% include intersect day=page.day1 column="day1" row=row-%}
  {%-include intersect day=page.day2 column="day2" row=row-%}
  {%-include intersect day=page.day3 column="day3" row=row-%}
  {%-include intersect day=page.day4 column="day4" row=row-%}
  {%-include intersect day=page.day5 column="day5" row=row %}
  </tr>
{%-endfor-%}
</table>

</div>

<div class="col-xs-12">
<h2>Per-day schedules</h2>

All times US Pacific time.

<div class="row fix">

<div class="col-sm-6">
<h3>Monday, June 13<sup>th</sup>: TBA</h3>

{% include day_schedule_table.html day=page.day1 %}

</div>

<div class="col-sm-6">
<h3>Tuesday, June 14<sup>th</sup>: TBA</h3>

{% include day_schedule_table.html day=page.day2 %}

</div>

<div class="col-sm-6">
<h3>Wednesday, June 15<sup>th</sup>: Field trip/hackaton</h3>

{% include day_schedule_table.html day=page.day3 %}

</div>

<div class="col-sm-6">
<h3>Thursday, June 16<sup>th</sup>: TBA</h3>

{% include day_schedule_table.html day=page.day4 %}

</div>

<div class="col-sm-6">
<h3>Friday, June 17<sup>th</sup>: TBA</h3>

{% include day_schedule_table.html day=page.day5 %}

</div>

</div> <!-- row -->
</div> <!-- per-day schedule -->


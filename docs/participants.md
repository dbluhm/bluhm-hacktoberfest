---
layout: page
title: Participants
permalink: /participants/
---

Here are all of the participants in the Bluhm Hacktoberfest projects!

{% for participant in site.participants %}
{% assign last_interest = participant.interests | last | prepend: "and " %}
### {{ participant.name }}

{{ participant.name | split: " " | first }}
is interested in {{ participant.interests | pop | push: last_interest | join: ", " }}.
Their favorite color is {{ participant.favorite_color }}
and their favorite food is {{ participant.favorite_food }}.

#### Why are you excited for Hacktoberfest?
> {{ participant.content }}
{% endfor %}

# PandaScore REST API for All Videogames (pandascore.co)

> # Introduction Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home). The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain. - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format ### About this documentation Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg) You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg) ## Events hierarchy The PandaScore API allows you to access data about eSports events by using a certain structure detailed below. **Leagues** Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series. Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._ Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._ **Series** A Serie represents an occurrence of a league event. The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._ Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._ **Tournaments** Tournaments groups all the matches of a serie under "stages" and "groups". The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._ Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._ **Matches** Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match). Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._ Matches of the gr

## Identity

- **Record id**: `dea:platform-service-pandascore-co-fhsmwa`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: pandascore.co; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).

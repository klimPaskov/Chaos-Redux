# Evolution Matrix

| Evolution | Chaos gate | Active eligibility | Base pacing | Active-event change | Pre-fire opening | New content | Containment response | Evolution actor |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| I, virulent strain | 200 | active infection, establishment period, deaths or multi-state failure | 90 to 150 days after eligibility | faster mortality curve, moderately faster spread, higher relapse, cure adaptation milestone | one mainland origin with higher load and shorter incubation | adaptation research, darker UI state, new incident pool | adapt cure, expand hospitals, stronger surveillance | none or origin owner when needed |
| II, overseas spread | 400 | coastal infection, multi-country or multi-region spread, valid port route | 120 to 180 days | port and convoy jumps, islands become targets, maritime restrictions matter | mainland origin remains, one overseas destination can become Threatened after route exists | port inspections, sea-route display, first overseas news | close or inspect ports, screen returning troops, share cure overseas | first overseas destination owner for milestone |
| III, Rat Nations | 600 | connected infection basin, state collapse, large deaths, weak containment | 120 to 210 days | rat emergence pressure, strong breakaway country, no plague removal | stronger basin pressure after spread, no immediate rat at firing | tag pool, brood pulse, rat tree, dominance, anti-rat actions | destroy broods, liberate and quarantine, clear burrows and disease | first Rat Nation |
| IV, Rat King | 800 | several broods or absorbed rival, valid high-dominance candidate, proto-sentience | 90 to 180 days | separate Rat King tag unifies all rat states and units | permission is available, but requires Rat Nations and candidate | deep tree, sentient government, coronation super-event, royal pulse | strike crown, divide network, global cooperation | Rat King |
| V, world-end path | 1000 | Rat King controls large world share, catastrophic deaths, high Dominion and Sentience | 90 to 180 days | unlocks target continent, readiness panel, terminal focus lane | all evolution permissions available, but no skipped chain | continental missions, final focus path, terminal scenario | protect capitals and ports, share cure, destroy royal nodes | Rat King |

## Triggerable scenario override

The manual scenario forces Evolutions I through IV in sequence during one scoped bootstrap. It records only missing evolution rows, uses the first scenario Rat Nation for Evolution III, and uses the Rat King for Evolution IV. It never records Evolution V, never sets world end, and clears the bypass before ordinary evolution checks resume.

## Evolution logging

- each evolution records exactly once per campaign unless the source system explicitly supports a restoration history entry outside the evolution log
- baseline disease phases do not create evolution rows
- actor context is set only when a country owns the milestone
- Evolution III uses the first Rat Nation as actor
- Evolution IV and V use the Rat King
- disabled evolutions do not set recorded flags or unlock later content during ordinary play
- the triggerable scenario explicitly overrides Evolution I through IV enable and pacing gates for its one manual setup, as disclosed in scenario detail text

## Dynamic pacing factors

| Factor | I | II | III | IV | V |
| --- | --- | --- | --- | --- | --- |
| active infected states | strong acceleration | medium | strong | indirect | indirect |
| event deaths | medium | low | strong | medium | very strong |
| Severe Crisis share | strong | medium | very strong | indirect | indirect |
| port infection | low | required and strong | medium | low | medium |
| weapon deployment | strong | strong | strong | medium | medium |
| global cure knowledge | delays | delays | delays through fewer basins | low | delays through human resistance |
| rat state count | none | none | after first emergence only | strong | strong |
| absorbed broods | none | none | none | very strong | strong |
| Rat King Dominion | none | none | none | candidate input | required and strong |
| continent control | none | none | none | none | final scenario requirement |

# Event 19 Possessed General Portrait and Archetype Matrix

The asset package needs 20 fictional one-person leader portraits. All personal names are generated during implementation from matching regional and gender pools. The table defines production slots, not final characters.

## Shared rules

- 10 male-presenting and 10 female-presenting portraits.
- Apparent gender presentation is recorded in the asset manifest.
- Female-presenting portraits use female name pools and female leader metadata where supported.
- Male-presenting portraits use male name pools and must not use female metadata.
- Names should sound plausible for the country and period while allowing unsettling surnames, epithets, or nicknames.
- No portrait receives a generic office title as its personal name.
- Every portrait is 156 by 210, HOI4-style bust or upper torso, fictional, and generated.
- All are static. The claimant UI warning border carries the animation.

## Portrait slots

| Slot | Presentation | Primary archetype | Secondary tendency | Regional pool direction | Visual direction |
| ---: | --- | --- | --- | --- | --- |
| 01 | male | Quartermaster Sovereign | Hollow Marshal | Northern and Western Europe | severe logistics officer, impossible medal ribbon, depot dust |
| 02 | female | Quartermaster Sovereign | Barracks Tribune | Central and Eastern Europe | railway command coat, ledger clasp, unnaturally calm stare |
| 03 | male | Quartermaster Sovereign | Iron Saint | Middle East and North Africa | desert staff uniform, dark supply maps, ritual insignia |
| 04 | female | Quartermaster Sovereign | Field Prophet | South and Southeast Asia | transport officer, mixed regional uniform, wrong-direction shadow |
| 05 | male | Field Prophet | Iron Saint | Eastern Europe and Eurasian steppe | weathered field coat, luminous eyes, old cavalry emblem |
| 06 | female | Field Prophet | Barracks Tribune | South Asia | improvised command dress, prophetic calm, dust and signal flags |
| 07 | male | Field Prophet | Hollow Marshal | East Asia | precise officer dress, blank insignia, distant impossible light |
| 08 | female | Field Prophet | Quartermaster Sovereign | Latin America | regional military coat, strange radio headset, severe expression |
| 09 | male | Barracks Tribune | Quartermaster Sovereign | Western Europe | enlisted-origin commander, crowded barracks background, hard gaze |
| 10 | female | Barracks Tribune | Field Prophet | Eastern Europe | soldier committee leader, battered coat, subtle spectral reflection |
| 11 | male | Barracks Tribune | Iron Saint | Middle East and Central Asia | local militia commander, bandolier and formal staff insignia |
| 12 | female | Barracks Tribune | Hollow Marshal | East and Southeast Asia | disciplined field organizer, muted uniform, impossible shadow line |
| 13 | male | Iron Saint | Field Prophet | Southern Europe and Mediterranean | ceremonial combat coat, severe religious or martial symbols |
| 14 | female | Iron Saint | Quartermaster Sovereign | Central Europe | rigid staff portrait, strange decorations, cold barracks light |
| 15 | male | Iron Saint | Barracks Tribune | Sub-Saharan Africa | regional military attire, scarred command standard, possessed intensity |
| 16 | female | Iron Saint | Hollow Marshal | Middle East and North Africa | austere command dress, unnatural stillness, dark halo-like smoke |
| 17 | male | Hollow Marshal | Quartermaster Sovereign | East Asia | immaculate unknown officer, unmarked decorations, empty backdrop |
| 18 | female | Hollow Marshal | Field Prophet | Northern Europe | severe general coat, pale side light, no verifiable insignia |
| 19 | male | Hollow Marshal | Barracks Tribune | Americas | improvised senior commander, polished boots, unsettling composure |
| 20 | female | Hollow Marshal | Iron Saint | Global fallback pool | adaptable period uniform, strong face, subtle supernatural disturbance |

## Archetype mechanics

| Archetype | Main benefit | Main demand pattern | Revolt character | Best counter |
| --- | --- | --- | --- | --- |
| Quartermaster Sovereign | equipment and supply efficiency | stockpiles, depots, autonomous logistics | seizes rail and depots | secure logistics and replace staff |
| Field Prophet | request prediction and readiness | more formations, political recognition | high-chaos or anomalous host | discredit failed predictions and isolate followers |
| Barracks Tribune | organization and rank-and-file loyalty | formal appointment, soldier protections | broad low-level defection | co-option and alternative soldier representation |
| Iron Saint | discipline and combat resilience | emergency powers, purges, political office | concentrated fanatical revolt | deny district control and split loyal host |
| Hollow Marshal | planning and officer competence | formal command, executive power | coup or elite takeover | verify staff, build counter-command, protect capital |

## Demand-to-effect map

| Demand | Immediate concession benefit | Long-term claimant gain | Refusal risk |
| --- | --- | --- | --- |
| Formal appointment | organization and readiness | recognized influence | resignation, sabotage, or revolt preparation |
| Equipment share | better fill and supply | depot loyalty | seizure or loss of readiness |
| Autonomous district | lower congestion | territorial revolt base | local disobedience |
| Another formation | new claimant-attached lot | more loyal troops | unauthorized draw |
| Political seat | national military bonus | takeover access | cabinet or officer split |
| Emergency powers | strong wartime command | timer toward permanent rule | coup preparation |

## Name-pool handoff

Implementation should provide small pools for the major regional groups used by the country roster. Each pool needs:

- male given names
- female given names
- surnames
- optional patronymics or family-name order rules
- optional military nicknames or epithets
- a fallback that still matches portrait presentation

The pool should draw from existing Chaos Redux regional naming helpers when available rather than create a duplicate system.

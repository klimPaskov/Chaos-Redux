# Event 19 Possessed General Army-Identity and Archetype Matrix

The gameplay package uses 20 fictional male claimant profiles with regional male name pools and male-default leader metadata. Each fixed technical portrait slot visually represents the claimant through a distinct regional army or muster, not through an individual person. The table defines the frozen gameplay/profile binding and final visual production slot.

## Shared rules

- Exactly 20 male claimant gameplay profiles.
- Every profile uses a regional male name pool and male-default leader metadata.
- Names should sound plausible for the country and period while allowing unsettling surnames, epithets, or nicknames.
- No claimant receives a generic office title as his personal name.
- Every fixed `GFX_portrait_*` slot is a static 156 by 210 fictional generated army/muster scene.
- No scene has an individual focal human/person, readable face, officer bust, commander portrait, real national emblem, or copied historical identity.
- Regional identity is carried by terrain, period matériel, logistics, formation geometry, weather, and operational posture.
- The claimant UI warning border carries animation; the army/muster scenes remain static.

## Fixed identity-scene slots

| Slot | Gameplay metadata | Primary archetype | Secondary tendency | Regional pool/runtime direction | Final army/muster visual direction |
| ---: | --- | --- | --- | --- | --- |
| 01 | male | Quartermaster Sovereign | Hollow Marshal | Northern and Western Europe | European railhead logistics muster with diagonal ranks, trains, trucks, depots, and converging supply lanes |
| 02 | male | Quartermaster Sovereign | Barracks Tribune | Central and Eastern Europe | frozen river bridgehead with rectangular battalion block, pontoon works, and layered supply columns |
| 03 | male | Quartermaster Sovereign | Iron Saint | Middle East and North Africa | circular oasis-fort defence with concentric ranks, gun pits, pack supply, and an empty center |
| 04 | male | Quartermaster Sovereign | Field Prophet | South and Southeast Asia and Australasia diaspora-compatible | monsoon port-and-rail muster in a fan of columns radiating from docks, warehouses, and flooded sidings |
| 05 | male | Field Prophet | Iron Saint | Eastern Europe and Eurasian steppe | winter-steppe horse-artillery host in an arrowhead with limbers and cavalry screens |
| 06 | male | Field Prophet | Barracks Tribune | South Asia | monsoon floodplain crossing with serpentine infantry columns, pontoon craft, and pack supply |
| 07 | male | Field Prophet | Hollow Marshal | East Asia | dark snowy forest infiltration with several layered echelons and dispersed supply sledges |
| 08 | male | Field Prophet | Quartermaster Sovereign | Latin America | highland pack-artillery muster in a chevron across terraced slopes and storm light |
| 09 | male | Barracks Tribune | Quartermaster Sovereign | Western Europe and North America | industrial tram-square front with infantry blocks, streetcars, trucks, barricades, and factories |
| 10 | male | Barracks Tribune | Field Prophet | Eastern Europe | winter industrial grid of artillery batteries and infantry ranks distributed through ruined works |
| 11 | male | Barracks Tribune | Iron Saint | Middle East and Central Asia | tiered high-plateau canyon shield formation with pack trains and successive stone breastworks |
| 12 | male | Barracks Tribune | Hollow Marshal | East and Southeast Asia and Australasia diaspora-compatible | amphibious wavefront with landing craft, shallow-water infantry bands, and several advancing lines |
| 13 | male | Iron Saint | Field Prophet | Southern Europe, Mediterranean, and South America | symbol-free coastal-cliff artillery defence in a zigzag with gun terraces and switchback supply paths |
| 14 | male | Iron Saint | Quartermaster Sovereign | Central Europe | machineworks muster in checkerboard infantry and vehicle blocks inside an immense industrial yard |
| 15 | male | Iron Saint | Barracks Tribune | Sub-Saharan Africa | storm-savanna mobile echelon with truck columns, infantry screens, field guns, and rain-darkened grassland |
| 16 | male | Iron Saint | Hollow Marshal | Middle East and North Africa | desert mobile crescent of trucks, mounted scouts, infantry files, and gun teams around an empty center |
| 17 | male | Hollow Marshal | Quartermaster Sovereign | East Asia | blackout industrial-city bicycle host arranged in a strict street grid among factories and power lines |
| 18 | male | Hollow Marshal | Field Prophet | Northern Europe | frozen-fjord ski host in a U-shaped envelopment around icebound supply craft and coastal guns |
| 19 | male | Hollow Marshal | Barracks Tribune | Americas | hurricane river-delta defence with levee infantry, barges, trucks, and guns in a broken zigzag |
| 20 | male | Hollow Marshal | Iron Saint | Australia only | outback salt-lake motor host in a hooked arc with trucks, field guns, dust lanes, and scrub horizon |

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
- surnames
- optional patronymics or family-name order rules
- optional military nicknames or epithets
- no fallback entry. If no unused profile matches the country's region, claimant identity selection fails closed

The pool should draw from existing Chaos Redux regional naming helpers when available rather than create a duplicate system. Profiles 04 and 12 are the documented Asia/Australasia diaspora-compatible identities; profile 20 is Australia-only and must never serve as a global or cross-region substitute. The exact current source/runtime evidence is in `docs/assets/019_infantry_spawn/notes/claimant_portrait_asset_crosswalk_2026_07_16.md`.

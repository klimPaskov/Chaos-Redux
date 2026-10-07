# User requirement traceability

“Covered” means specified in this package, not implemented or engine-verified. Parent additions and technical interpretations are documented in tuning and the parent review.

| User requirement | Design location | Acceptance |
| --- | --- | --- |
| 086, World Claims, Minor Repeatable, To Be Reworked, Chaos 1 | Part 1, tuning, implementation handoff | T60 |
| Formables Low only, no secondary cluster | Part 1, tuning, catalog handoff | T60 |
| Every valid country, not a Germany-only event | Parts 1, 8, engine participant contract | T01, T39 |
| Every foreign state directly bordering owned territory | Part 2, frontier table | T01–T06 |
| No valid land neighbors means no claims in that firing | Parts 1–3, geography contract | T04, T07 |
| Conquest changes next firing's frontier | Parts 1–2, achievement A01 | T02–T03, T09 |
| Current map rather than fixed country paths | Parts 2, 5–6, geography contract | T30–T31, T39 |
| Claimant-specific 25% starting Compliance | Part 4, engine G1 | T14–T19 |
| Another occupier does not inherit the benefit | Part 4, engine G1 | T15 |
| Normal Compliance after initial grant | Part 4, consumed-floor tuning | T16–T18 |
| I 200+, 50%, limited connected second ring | Part 3, tuning | T07, T09, T17 |
| I dynamic greater-state ambitions and rewards | Parts 5–7, 9 | T30–T36 |
| II 400+, 75%, broader ring two, selected ring three | Part 3, tuning | T07–T09, T17 |
| II larger geography and successors | Parts 5–6, 9–10 | T30–T32, T45 |
| III 600+, earned cores, controlled WC target, long control, high Compliance | Parts 3–4, core contract | T20–T26 |
| III no immediate cores on newly conquered territory | Part 4 | T20–T25 |
| IV 800+, 100%, several layers, faster cores | Part 3, tuning | T07, T17, T20–T25 |
| IV new identity, flags and integrated heartland for former minors | Parts 5, 9, 13, country matrix | T30, T36, T56 |
| V 1000+, progressive continent-spanning claims, fast earned cores | Parts 2–4, 10 | T10–T11, T20–T25, T52 |
| V transcontinental, hemisphere and global projects | Part 10, scale table | T52–T53 |
| V never instant all-planet claims | Part 2, frozen network rule | T04, T10–T11, T52 |
| Geographic regions, subcontinents, islands, cultures, seas, mountains and basins | Parts 5–6, geographic registry | T30, T47, research gate |
| Connected conquest and neighboring groups | Parts 5–6, connected resolver | T30–T31 |
| Illustrative greater-country names are not exhaustive | Part 6, dynamic registry and identity grammar | T30, T36, T47 |
| Existing HOI4 and Chaos Redux formables take priority where appropriate | Part 9, provider and country matrices | T34–T35 |
| Multiple countries may claim and contest the same state | Parts 4, 8 | T15, T37 |
| Civil wars, peace, releases, independence and transfers remain supported | Part 8, lifecycle contract | T38–T39, T58–T59 |
| Newly created countries participate | Part 8, participant and epoch rules | T38–T39 |
| A new remote frontier can generate new ambitions | Parts 5–6, 8 | T02, T30 |
| Repeats refresh/expand rather than auto-conquer | Parts 1–3, 10 | T09–T11, T16–T18 |
| Read supplied skills and sources thoroughly before authoring | Source audit and SHA/range manifest | Completed for all 42 supplied plaintext files |
| Fully read every externally referenced required file | Source audit missing-read register | Not completed, explicitly disclosed |
| Use provided subagents | All profiles read, bounded handoffs created | Actual spawning unavailable, independent reviews not run |
| Disclose truncation or simplification | Source audit, parent review, README | Explicit external gaps and engine-compatible interpretation |

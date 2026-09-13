# Event 58 acceptance matrix

This matrix defines the minimum evidence needed before Random Buildings can be treated as implemented. Source inspection, MCP evidence, automated checks, and later user-owned live testing serve different purposes. A source-only pass cannot replace map, probability, UI, or live evidence where those are required.

| ID | Setup | Expected result | Evidence |
| --- | --- | --- | --- |
| `RB-A01` | Calm World, all evolutions enabled | every state attempts exactly one baseline state-building result | event inspection, transaction counters, live sample |
| `RB-A02` | Chaos `200-399` | baseline and Evolution I each attempt once per state | event comparison, counters, evolution log |
| `RB-A03` | Chaos `400-599` | baseline, Evolution I, and one Evolution II package per state | event and map inspection, counters |
| `RB-A04` | Chaos `600+` | all lower layers run and exceptional allocation runs afterward | event inspection, exceptional ledger, evolution log |
| `RB-A05` | Evolution I disabled at `600+` | baseline, Evolution II, and Evolution III run without Evolution I | toggle test, recorded flags |
| `RB-A06` | Evolution II disabled at `600+` | state layers and Evolution III run without province packages | toggle test, map comparison |
| `RB-A07` | Evolution III disabled at `600+` | no exceptional provider is selected or logged | toggle test, exceptional ledger |
| `RB-A08` | first Event 58 firing occurs at `600+` | every enabled successful evolution receives its own first-use log entry | Evolutions tab and History detail |
| `RB-A09` | one evolution has zero valid placements | its recorded flag and Chaos milestone remain unset | source trace, transaction result |
| `RB-A10` | landlocked state | no dockyard, coastal fort, or naval-base result can occur | probability inspect, map sample |
| `RB-A11` | lake-only coastline | naval construction remains invalid unless vanilla treats it as usable naval coast | installed map and engine evidence |
| `RB-A12` | state with no free industrial slot | no civilian factory, military factory, dockyard, refinery, or other slot-consuming entry is placed | capacity trace |
| `RB-A13` | state with capped infrastructure | infrastructure has zero weight and no over-cap mutation occurs | probability and state comparison |
| `RB-A14` | special nonhuman controller | compatible military and transport entries remain available, civilian-only entries are filtered | classifier and provider trace |
| `RB-A15` | concentration-camp provider selected | one real camp instance is placed and initialized once by the camp owner | owner callback ledger, no duplicate registration |
| `RB-A16` | extermination or gulag provider unavailable | it has zero weight and no substitute structure uses its name | provider and localisation inspection |
| `RB-A17` | selected provider fails revalidation or callback-readiness proof | local reroll occurs only after the failed attempt proves that it left no building, facility, owner marker, responsibility record, or other partial mutation | seeded or deterministic test harness |
| `RB-A18` | restricted band empties | fallback moves to safer bands only | probability trace |
| `RB-A19` | ordinary band empties | layer is exhausted and no higher-risk result is forced | probability trace, skip reason |
| `RB-A20` | six valid land-border provinces, two capped | four receive one fort level and the state receives no second package | map comparison |
| `RB-A21` | coastal-fort package | every usable uncapped sea-facing province in the state receives one level | map comparison |
| `RB-A22` | naval-base package with existing port | the existing valid port is upgraded before a new port is considered | map and building comparison |
| `RB-A23` | naval-base package without existing port | one verified suitable coastal province receives one level | map inspection and result target |
| `RB-A24` | railway with valid existing path | one verified path or segment gains one level without illegal jumps | railway graph comparison |
| `RB-A25` | railway requiring unsupported path creation | entry is blocked or invalid, with no infrastructure substitute | blocker report and source trace |
| `RB-A26` | supply-hub package | one valid hub and any required verified connector appear atomically | supply graph comparison |
| `RB-A27` | supply-hub connector fails | neither hub nor partial connector remains | map comparison |
| `RB-A28` | only three exceptional locations exist | no more than three placements occur despite the minimum target | exceptional ledger |
| `RB-A29` | more locations than exceptional cap | final count respects current tier cap | exceptional ledger |
| `RB-A30` | one exceptional state selected | the same state cannot receive another exceptional structure in that firing | location uniqueness proof |
| `RB-A31` | globally unique exceptional structure already exists | later firing cannot create a second instance | provider uniqueness proof |
| `RB-A32` | later repeat firing | current caps and owner validity are reevaluated, with no old candidate cache | event comparison |
| `RB-A33` | every active layer exhausted worldwide | event does not consume weight, cap, timer, fire count, log row, or Chaos | preflight transaction proof |
| `RB-A34` | some states exhausted, some valid | event fires and reports both successes and exhausted states | report and counters |
| `RB-A35` | direct hidden resolver call | no normal event history, repeatable transaction, or achievement credit is allowed | debug test |
| `RB-A36` | force-triggered normal event | gameplay can be tested, but achievements remain disqualified | achievement trace |
| `RB-A37` | two human players | each gets one summary for their transaction-start country and no per-state popup spam | multiplayer test |
| `RB-A38` | player tag switches during transaction | summary and achievement identity remain bound to transaction-start country | multiplayer or tag-switch test |
| `RB-A39` | event selected as cluster member | cluster counts once for pacing and Event 58 still records its own fire state | cluster history and timer evidence |
| `RB-A40` | first baseline, province, and exceptional milestones | direct Event 58 Chaos totals at most `+5` lifetime | Chaos History trace |
| `RB-A41` | military factories added | generic military-buildup Chaos remains owner of that generic source | Chaos source comparison |
| `RB-A42` | camp later causes deaths or condemnation | camp owner logs consequences once and Event 58 does not duplicate them | Deaths and Condemnation trace |
| `RB-A43` | Event 54 grants a technology then Event 58 fires | new tech can affect provider validity without either event marking the other fired | history and provider test |
| `RB-A44` | Event 55 project provider registered | random placement creates only the approved completed structure and no project decision completion | owner callback test |
| `RB-A45` | DLC required by one provider is absent | provider is removed and no placeholder is used | DLC matrix |
| `RB-A46` | report opens after a large world transaction | text remains concise, no raw keys, no clipped values, and no state-list wall | GUI and localisation review |
| `RB-A47` | Event Details opened | premise and evolution previews show no fake history metadata or probability internals | Event Details review |
| `RB-A48` | Event Logs History and Evolutions views | date, event identity, tier, stage, and actorless global presentation are correct | GUI render and live review |
| `RB-A49` | save and reload after each layer | buildings, owner registrations, evolution flags, achievements, and exceptional uniqueness persist | save and reload test |
| `RB-A50` | newly registered future building | provider joins the declared layer without editing the root event chain | integration test |
| `RB-A51` | malformed future provider | it fails closed and appears in debug evidence without breaking other states | registry validation test |
| `RB-A52` | first natural firing with at least ten player states and full baseline coverage | Achievement 1 unlocks once | achievement test |
| `RB-A53` | eight surviving display families under one player country | Achievement 2 unlocks and stale destroyed families do not count | achievement test |
| `RB-A54` | exceptional structure retained for 365 days | Achievement 3 unlocks only after uninterrupted valid retention | timed achievement test |
| `RB-A55` | report and achievement assets installed | all textures use correct paths, dimensions, variants, and readable composition | asset audit |
| `RB-A56` | authoritative workbook updated | Event 58 and Positive Economy rows match in-game wording and CSV exports regenerate | spreadsheet handoff |
| `RB-A57` | final source state | probability compare, event compare, localisation audit, completion audit, and improvement closure have no unresolved accepted gap | final handoffs |

## Live testing boundary

The project debug-playtest skill is explicit-invocation only. The coding agent must prepare the acceptance cases and source evidence, but it must not claim user-owned live HOI4 validation unless that workflow was explicitly authorized and actually run.

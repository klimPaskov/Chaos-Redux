# Fallout Event ID Ledger

## Purpose

This ledger owns suffix allocation inside `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

## Reserved Ash-week orientation tranche

The user approved `FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` on 2026-07-18. This ledger reserves suffixes `62` through `84` with the following exact roles:

| Suffix | Component | Event role | Visibility | Follow-up |
| ---: | --- | --- | --- | --- |
| 62 | national orientation | root | human visible | 64 |
| 63 | national orientation | root | hidden AI | 65 |
| 64 | national orientation | result | human visible | 66 |
| 65 | national orientation | result | hidden AI | 67 |
| 66 | capital condition | root | human visible | 68 |
| 67 | capital condition | root | hidden AI | 69 |
| 68 | capital condition | result | human visible | 70 |
| 69 | capital condition | result | hidden AI | 71 |
| 70 | immediate resource crisis | root | human visible | 72 |
| 71 | immediate resource crisis | root | hidden AI | 73 |
| 72 | immediate resource crisis | result | human visible | 74 |
| 73 | immediate resource crisis | result | hidden AI | 75 |
| 74 | government archetype | root | human visible | 76 |
| 75 | government archetype | root | hidden AI | 77 |
| 76 | government archetype | result | human visible | 78 |
| 77 | government archetype | result | hidden AI | 79 |
| 78 | character or institution | root | human visible | 80 |
| 79 | character or institution | root | hidden AI | 81 |
| 80 | character or institution | result | human visible | 82 |
| 81 | character or institution | result | hidden AI | 83 |
| 82 | orientation | closure | human visible | 84 |
| 83 | orientation | closure | hidden AI | 84 |
| 84 | orientation | cleanup | hidden | none |

The component sequence and delayed-result cadence are fixed:

| Sequence | Component | Delay |
| ---: | --- | ---: |
| 1 | national orientation | 2 days |
| 2 | capital condition | 3 days |
| 3 | immediate resource crisis | 4 days |
| 4 | government archetype | 3 days |
| 5 | character or institution | 2 days |

Every result uses the accepted deterministic bands of 70 or more for success, 45 through 69 for partial success, and below 45 for failure. Human and hidden-AI routes use identical costs, scoring, effects, memory, and cleanup. Save recovery preserves the exact generation, transaction, due-day, mode, and event-token identity so an unissued result can issue once and an issued result cannot issue again. Missing regional, archetype, country-memory, state-target, or curated character or institution registry rows refuse orientation with no generic fallback.

The tranche requires six dedicated report assets for the five components and closure. All six assets and their sprite registrations exist. The dormant transaction substrate and the manually written national pilot at `62` through `65` are blocked and uncounted after completion audit. Dedicated localisation exists for the pilot. The other nineteen blocks, caller, event-log rows, event-detail rows, complete regional and archetype coverage, and registry-backed late components remain absent. No caller may be wired until successor allocation, player continuation, and all required candidate registries are proven. Neither scheduler activation flag may be set by this tranche. The Fallout living-world total remains 0 of 660 until every reserved block is implemented, wired, manually reviewed, logged, detailed, and audited.

The dedicated event file was scanned on 2026-07-15 before this reservation. Suffixes `100` through `126` were unused. This reservation does not count as implemented content. A row becomes countable only after final localisation, gameplay effects, AI behavior, memory or closure, cleanup, asset disposition, and manual audit are complete.

## Reserved living-world pilot tranche

| Suffix | Primary family | Working design anchor | Final localisation keys | Ownership | Event class | Visibility | Caller | Follow-up | Cooldown family | Asset | Batch | Audit status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | global survival and society | The Last Inventory | Pending implementation | all eligible successors | crisis incident | human visible | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | `GFX_report_event_fallout_last_inventory` | living-world foundation 1 | ordinary reservation contract proven, content blocked by orientation, event tuning, and scheduler activation |
| 101 | global survival and society | The Last Inventory AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | none | living-world foundation 1 | ordinary reservation contract proven, content blocked by orientation, event tuning, and scheduler activation |
| 102 | global survival and society | Publish the storehouse ledger | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 103 | global survival and society | Hide shortage and protect household caches | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 104 | global survival and society | Seize disputed reserves | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 105 | global survival and society | First winter ration review | Pending implementation | all eligible successors | callback | human visible | 102, 103, 104, 123, 124, or 125 | 106 | food security | shared family art | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 106 | global survival and society | Inventory chain cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | any terminal inventory transaction | none | food security | none | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 107 | global survival and society | River Intake at Dawn | Pending implementation | all eligible successors | crisis incident | human visible | ordinary receipt through Fallout coordinator | 109, 110, 111, or 121 | water security | `GFX_report_event_fallout_river_intake_at_dawn` | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 108 | global survival and society | River Intake at Dawn AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | unallocated hidden AI companions | water security | none | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 109 | global survival and society | Close the intake | Pending implementation | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 110 | global survival and society | Ration filtered flow | Pending implementation | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 111 | global survival and society | Seize upstream pumps | Pending implementation | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 112 | global survival and society | Water compact or epidemic callback | Pending implementation | all eligible successors | callback | human visible | 109, 110, 111, or 121 | 113 | water security | shared family art | living-world foundation 1 | blocked by tuning, intake registry, and hidden AI companion allocation |
| 113 | global survival and society | Intake chain cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | any terminal intake transaction | none | water security | none | living-world foundation 1 | blocked by tuning and curated intake registry |
| 114 | global survival and society | Rail Crew Twenty-Seven | Pending implementation | all eligible successors | crisis incident | human visible | ordinary receipt through Fallout coordinator | 116, 117, 118, or 122 | transport recovery | `GFX_report_event_fallout_rail_crew_twenty_seven` | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 115 | global survival and society | Rail Crew Twenty-Seven AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | unallocated hidden AI companions | transport recovery | none | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 116 | global survival and society | Protect the repair crews | Pending implementation | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 117 | global survival and society | Use forced labor | Pending implementation | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 118 | global survival and society | Abandon the exposed line | Pending implementation | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 119 | global survival and society | Corridor outcome callback | Pending implementation | all eligible successors | callback | human visible | 116, 117, 118, or 122 | 120 | transport recovery | shared family art | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 120 | global survival and society | Rail chain cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | any terminal rail transaction | none | transport recovery | none | living-world foundation 1 | blocked by tuning, corridor registry, and rail repair proof |
| 121 | global survival and society | Foreign intake testing result | Pending implementation | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | blocked by tuning, foreign-testing registry, and hidden AI companion allocation |
| 122 | global survival and society | Neighbor corridor access result | Pending implementation | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by tuning, corridor registry, rail repair proof, and hidden AI companion allocation |
| 123 | global survival and society | Publish the storehouse ledger AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 124 | global survival and society | Protect household caches AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 125 | global survival and society | Requisition disputed reserves AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |
| 126 | global survival and society | First winter ration review AI callback | Hidden event, no player text | all eligible successors | callback | hidden AI | 102, 103, 104, 123, 124, or 125 | 106 | food security | none | living-world foundation 1 | blocked by orientation, event tuning, and scheduler activation |

## Implemented Air Winter allocation outside the release floor

| Suffix | Primary family | Final event | Ownership | Caller | Follow-up | Asset | Audit status |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 6 | Air Winter Phase 1 regional return | Twenty regional policy results | bound original owner and one exact Phase 1 state branch | 1 through 5 after one of ten regional policies | none | `GFX_report_event_air_winter_phase_1` | implemented with regular targets, exact branch cardinality, ten success and inverse failure pairs, Deaths, timed result modifiers, AI projections, memory, stale handling, and cleanup |
| 13 | Air Winter Phase 2 Desert City and regional fallback | The Frozen Main and the Ward Cisterns for the exact receipt, Ice in the District Pumps for the generic row | exact arid urban state through subtype `desert_city`, otherwise non-city arid or Mediterranean state through subtype `none` | Air Winter candidate dispatcher | 49 after 30 days only for one of three exact-receipt policies | exact receipt uses `GFX_report_event_air_winter_desert_water_convoy`, generic row uses `GFX_report_event_air_winter_phase_2` | implemented with route subtype, ordinary and first-frost persistence, exact and generic interface separation, exact affordability, AI, owner-bound receipt, and cleanup |
| 38 | Air Winter Phase 2 island refugees | Boats Beneath the Shore Lights | eligible engine-island receiver with a live foreign coastal source | Air Winter candidate dispatcher after bounded source selection | 39 after 30 days | `GFX_report_event_air_winter_island_refugee_harbor` | implemented with deferred scheduler commit, balanced migration, AI, memory, cleanup, localisation, and dedicated asset |
| 39 | Air Winter Phase 2 island refugees | Thirty Days at the Island Shore | bound receiver and destination state | 38 after one of three positive transfers | none | `GFX_report_event_air_winter_island_refugee_harbor` | implemented with six exclusive results, Deaths on failures, matching memory, and cleanup |
| 47 | Air Winter Phase 5 ruined major-city salvage | Lamps Beneath the Empty Blocks | eligible Phase 5 state with original major-city category, persistent loss receipt, current building damage, and owner control | Air Winter candidate dispatcher | 48 after 30 days | `GFX_report_event_air_winter_dead_city_salvage` | implemented with three competing authorities, exact affordability, AI, policy memory, owner-control validation, and dedicated asset |
| 48 | Air Winter Phase 5 ruined major-city salvage | What Came Up from the Service Streets | bound original owner and controlled salvage state | 47 after one of three policies | none | `GFX_report_event_air_winter_dead_city_salvage` | implemented with nine exhaustive ordinary results, one narrow mixed-cause altered result, Deaths, concrete equipment, conditional repairable damage, exhausted-site memory, and cleanup |
| 49 | Air Winter Phase 2 Desert City result | Nine water-route results | bound original owner and exact Desert City state | 13 after municipal works, railway tankers, or motor columns | none | `GFX_report_event_air_winter_desert_water_convoy` | implemented with nine exhaustive outcomes, complete pending-owner proof, Deaths, conditional repairable damage, timed supply effects, policy and outcome memory, and cleanup |

These identifiers belong to the Air Winter pilot. They are not Fallout living-world content and do not increase the countable 660-block release-floor total.

The current Air Winter pilot contains 52 event blocks, 191 options, 190 effect-bearing options, and 67 delayed-result schedules. The countable Fallout living-world release-floor total remains 0 of 660 blocks.

Suffixes `6` and `49` are allocated to implemented Air Winter results and are no longer free.

## Collision boundary

The scan found existing Fallout suffixes in the request, transition, manual strike, and rewrite ranges. This ledger does not reuse those identifiers. Suffixes `62` through `84` remain reserved for Ash-week orientation. Suffixes `100` through `126` remain reserved for the living-world pilot even if implementation order changes.

## Pilot gates

The ordinary scheduler remains locked until the Ash-week orientation package has all five required parts: national orientation, capital or main-state condition, immediate resource crisis, government-archetype introduction, and the first character or institution. Completing orientation still does not approve or activate the scheduler.

The three pilot report assets exist and their sprites are registered in `interface/fallout_world_end.gfx`. They remain unattached because the corresponding event roots are not defined. Event counting cannot begin until the gameplay rows, AI resolution, delayed results, callbacks, cleanup, target registries, and event asset references pass manual review.

The typed constants for suffixes `100` through `126` are identity reservations only. Primary ownership is `global survival and society`. Food, water, and transport are cooldown families and do not own release-floor counts.

## Count status

Reserved Ash-week orientation identities: `23`.

Reserved living-world pilot identities: `27`.

Total reserved documentation identities across both tranches: `50`.

Defined Ash-week orientation blocks: `4`, all in the uncounted national-orientation pilot.

Defined living-world pilot blocks: `0`.

Countable manually reviewed Fallout living-world blocks: `0 of 660`.

The release-floor counter must remain unchanged until individual rows pass implementation and audit.

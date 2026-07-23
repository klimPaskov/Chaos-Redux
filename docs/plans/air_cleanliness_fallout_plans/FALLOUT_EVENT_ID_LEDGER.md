# Fallout Event ID Ledger

## Purpose

This ledger owns suffix allocation inside `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

## Current reconciliation

After the Names for the Missing tranche, the living-world pilot contains `163`
defined event blocks across `100` through `126`, `1009` through `1018`, `153`
through `200`, and `204` through `281`. All remain dormant and uncounted, so
the release-floor total is `0 of 660`. Historical count snapshots below are
retained as corrections and are superseded by the later correction sections.

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

The tranche requires six dedicated report assets for the five components and closure. All six assets and their sprite registrations exist. The dormant transaction substrate, the national pilot at `62` through `65`, the capital-condition pilot at `66` through `69`, the exact twelve-memory resource pilot at `70` through `73`, the exact twelve-memory government pilot at `74` through `77`, the character or institution pilot at `78` through `81`, and the authenticated closure and cleanup events at `82` through `84` are blocked and uncounted. Dedicated localisation exists for all visible component routes, and history `9110` supplies the 45 payloads through the shared Event Log detail route. The caller, complete regional and archetype coverage, exact capital repair approval, and registry-backed character installation remain absent. No caller may be wired until successor allocation, player continuation, and all required candidate registries are proven. Neither scheduler activation flag may be set by this tranche. The Fallout living-world total remains 0 of 660 until every reserved block is implemented, wired, manually reviewed, logged, detailed, and audited.

The dedicated event file was scanned on 2026-07-15 before this reservation. Suffixes `100` through `126` were unused. This reservation does not count as implemented content. A row becomes countable only after final localisation, gameplay effects, AI behavior, memory or closure, cleanup, asset disposition, and manual audit are complete.

## Reserved living-world pilot tranche

| Suffix | Primary family | Working design anchor | Final localisation keys | Ownership | Event class | Visibility | Caller | Follow-up | Cooldown family | Asset | Batch | Audit status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | global survival and society | The Last Inventory | Implemented, dormant, uncounted | all eligible successors | crisis incident | human visible | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | `GFX_report_event_fallout_last_inventory` | living-world foundation 1 | exact ordinary receipt gate, three authored choices, deterministic result reservation, dedicated localisation and art. Scheduler activation remains blocked. |
| 101 | global survival and society | The Last Inventory AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | none | living-world foundation 1 | deterministic AI branch selection uses the same result reservation and effect path as human play. Scheduler activation remains blocked. |
| 102 | global survival and society | Publish the storehouse ledger | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, ration-law modifier, survival ledger effects, event-log payload, and callback scheduling are wired. |
| 103 | global survival and society | Hide shortage and protect household caches | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, cache-network modifier, survival ledger effects, event-log payload, and callback scheduling are wired. |
| 104 | global survival and society | Seize disputed reserves | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, requisition authority, Deaths-backed failure losses, event-log payload, and callback scheduling are wired. |
| 105 | global survival and society | First winter ration review | Implemented, dormant, uncounted | all eligible successors | callback | human visible | 102, 103, 104, 123, 124, or 125 | 106 | food security | shared family art | living-world foundation 1 | branch-aware callback text, delayed resolution, ration-law and hunger-mission opening flags, event-log payload, and cleanup preparation are wired. |
| 106 | global survival and society | Inventory chain cleanup | Implemented, dormant, uncounted | all eligible successors | cleanup | hidden | any terminal inventory transaction | none | food security | none | living-world foundation 1 | exact hidden cleanup token releases the resolved delayed row. Scheduler activation remains blocked. |
| 107 | global survival and society | River Intake at Dawn | Implemented, dormant, uncounted | all eligible successors | crisis incident | human visible | ordinary receipt through Fallout coordinator | 109, 110, 111, or 121 | water security | `GFX_report_event_fallout_river_intake_at_dawn` | living-world foundation 1 | four authored choices, typed state intake registry, deterministic outcome bands, state water and Deaths effects, dedicated localisation and art, hidden AI companions, event-log payloads, and cleanup are wired. Scheduler activation remains blocked. |
| 108 | global survival and society | River Intake at Dawn AI resolution | Implemented, dormant, uncounted | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | 1009, 1010, 1011, or 1012 | water security | none | living-world foundation 1 | deterministic AI branch selection uses the same result reservation and effect path as human play. Scheduler activation remains blocked. |
| 109 | global survival and society | Close the intake | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, state closure modifier, water and medicine effects, Deaths-backed failure, event-log payload, and callback scheduling are wired. |
| 110 | global survival and society | Ration filtered flow | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, filter rotation modifier, resource effects, Deaths-backed failure, event-log payload, and callback scheduling are wired. |
| 111 | global survival and society | Seize upstream pumps | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 107 | 112 | water security | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, pump-authority modifier, military readiness effects, upstream dispute memory, Deaths-backed failure, and callback scheduling are wired. |
| 112 | global survival and society | Water compact or epidemic callback | Implemented, dormant, uncounted | all eligible successors | callback | human visible | 109, 110, 111, or 121 | 113 | water security | shared family art | living-world foundation 1 | branch-aware callback text, water compact or epidemic modifiers, state memory, event-log payload, and cleanup preparation are wired. |
| 113 | global survival and society | Intake chain cleanup | Implemented, dormant, uncounted | all eligible successors | cleanup | hidden | any terminal intake transaction | none | water security | none | living-world foundation 1 | exact hidden cleanup tokens release their own resolved rows. Final cleanup clears the state-owned intake receipt after both result and callback rows are released. Scheduler activation remains blocked. |
| 114 | global survival and society | Rail Crew Twenty-Seven | Implemented, dormant, uncounted | all eligible successors | crisis incident | human visible | ordinary receipt through Fallout coordinator | 116, 117, 118, or 122 | transport recovery | `GFX_report_event_fallout_rail_crew_twenty_seven` | living-world foundation 1 | four authored choices, state-owned corridor registry, deterministic result reservation, concrete localisation and dedicated art are wired. Scheduler activation remains blocked. A full bilateral neighbor registry is not yet present. |
| 115 | global survival and society | Rail Crew Twenty-Seven AI resolution | Implemented, dormant, uncounted | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | 1014, 1015, 1016, or 1017 | transport recovery | none | living-world foundation 1 | deterministic AI branch selection uses the same corridor registry, result reservation, effects, memory, and cleanup path as human play. Scheduler activation remains blocked. |
| 116 | global survival and society | Protect the repair crews | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, rail and infrastructure effects, equipment, Deaths-backed failure, event-log payload, and callback scheduling are wired. |
| 117 | global survival and society | Use forced labor | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, labor and atrocity memory, rail and infrastructure effects, equipment, Deaths-backed losses, event-log payload, and callback scheduling are wired. |
| 118 | global survival and society | Abandon the exposed line | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, withdrawal and fragmentation memory, rail and infrastructure effects, Deaths-backed failure, event-log payload, and callback scheduling are wired. |
| 119 | global survival and society | Corridor outcome callback | Implemented, dormant, uncounted | all eligible successors | callback | human visible | 116, 117, 118, or 122 | 120 | transport recovery | shared family art | living-world foundation 1 | branch-aware callback text, delayed resolution, heroic and atrocity memory, route fragmentation, event-log payload, and cleanup preparation are wired. |
| 120 | global survival and society | Rail chain cleanup | Implemented, dormant, uncounted | all eligible successors | cleanup | hidden | any terminal rail transaction | none | transport recovery | none | living-world foundation 1 | exact hidden cleanup tokens release their own result and callback rows, clear the state registry, and preserve save recovery. Scheduler activation remains blocked. |
| 121 | global survival and society | Foreign intake testing result | Implemented, dormant, uncounted, simplified | all eligible successors | delayed result | human visible | 107 | 112 or 1013 | water security | shared family art | living-world foundation 1 | Branch wiring, state effects, recognition and medicine results, hidden AI pairing, event log, and cleanup are wired. A real bilateral foreign partner registry remains pending, so this is not a full diplomacy chain. Scheduler activation remains blocked. |
| 122 | global survival and society | Neighbor corridor access result | Implemented, dormant, uncounted, simplified | all eligible successors | delayed result | human visible | 114 | 119 | transport recovery | shared family art | living-world foundation 1 | delayed receipt authentication, three outcome texts, shared-access effects, equipment, Deaths-backed failure, event-log payload, and callback scheduling are wired. The pilot records a state and country access agreement without a full bilateral partner registry. |
| 1009 | global survival and society | Close the intake AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 107 or 108 | 112 or 1013 | water security | none | living-world foundation 1 | hidden AI delayed result uses the close-intake branch and shared effect path. |
| 1010 | global survival and society | Ration filtered flow AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 107 or 108 | 112 or 1013 | water security | none | living-world foundation 1 | hidden AI delayed result uses the filter branch and shared effect path. |
| 1011 | global survival and society | Seize upstream pumps AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 107 or 108 | 112 or 1013 | water security | none | living-world foundation 1 | hidden AI delayed result uses the pump branch and shared effect path. |
| 1012 | global survival and society | Foreign water testing AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 107 or 108 | 112 or 1013 | water security | none | living-world foundation 1 | hidden AI delayed result uses the foreign-testing branch and shared effect path. |
| 1013 | global survival and society | Water compact or epidemic AI callback | Implemented, dormant, uncounted | all eligible successors | callback | hidden AI | 1009, 1010, 1011, or 1012 | 113 | water security | none | living-world foundation 1 | hidden AI callback uses the same review effects, memory, event-log payload, and cleanup path as human play. |
| 1014 | global survival and society | Protect the repair crews AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 115 | 1018 | transport recovery | none | living-world foundation 1 | hidden AI delayed result uses the protected-crews branch and shared effect, memory, event-log, callback, and cleanup path. |
| 1015 | global survival and society | Use forced labor AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 115 | 1018 | transport recovery | none | living-world foundation 1 | hidden AI delayed result uses the forced-labor branch and shared effect, memory, event-log, callback, and cleanup path. |
| 1016 | global survival and society | Abandon the exposed line AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 115 | 1018 | transport recovery | none | living-world foundation 1 | hidden AI delayed result uses the abandonment branch and shared effect, memory, event-log, callback, and cleanup path. |
| 1017 | global survival and society | Neighbor corridor access AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 115 | 1018 | transport recovery | none | living-world foundation 1 | hidden AI delayed result uses the neighbor-access branch and shared effect, memory, event-log, callback, and cleanup path. |
| 1018 | global survival and society | Corridor outcome AI callback | Implemented, dormant, uncounted | all eligible successors | callback | hidden AI | 1014, 1015, 1016, or 1017 | 120 | transport recovery | none | living-world foundation 1 | hidden AI callback uses the same rail effects, memory, event-log payload, and cleanup path as human play. |
| 123 | global survival and society | Publish the storehouse ledger AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | hidden AI delayed result uses the public branch row and shared effect path. |
| 124 | global survival and society | Protect household caches AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | hidden AI delayed result uses the household branch row and shared effect path. |
| 125 | global survival and society | Requisition disputed reserves AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | hidden AI delayed result uses the requisition branch row and shared Deaths-backed effect path. |
| 126 | global survival and society | First winter ration review AI callback | Implemented, dormant, uncounted | all eligible successors | callback | hidden AI | 102, 103, 104, 123, 124, or 125 | 106 | food security | none | living-world foundation 1 | hidden AI callback uses the same review effects, memory flags, event-log payload, and cleanup path as human play. |
| 153 | global survival and society | The Well Queue | Implemented, dormant, uncounted | all eligible successors | crisis incident | human visible | ordinary receipt through Fallout coordinator | 155, 156, or 157 | water security | `GFX_report_event_fallout_well_queue` | living-world foundation 1 | three authored choices, current state and Air Winter water-source gate, deterministic result reservation, Deaths-backed failure, event-log payload, callback, and authenticated cleanup are wired. Scheduler activation remains blocked. |
| 154 | global survival and society | The Well Queue AI resolution | Implemented, dormant, uncounted | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | 158, 159, or 160 | water security | none | living-world foundation 1 | hidden AI branch selection uses the same result reservation, effects, memory, and cleanup path as human play. Scheduler activation remains blocked. |
| 155 | global survival and society | Public queue result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 153 | 161 | water security | shared family art | living-world foundation 1 | three outcome descriptions, water and recognition effects, failure deaths, event-log payload, and callback scheduling are wired. |
| 156 | global survival and society | Filter room result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 153 | 161 | water security | shared family art | living-world foundation 1 | three outcome descriptions, filter and water effects, failure deaths, event-log payload, and callback scheduling are wired. |
| 157 | global survival and society | Guarded intake result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 153 | 161 | water security | shared family art | living-world foundation 1 | three outcome descriptions, guard and water effects, failure deaths, event-log payload, and callback scheduling are wired. |
| 158 | global survival and society | Public queue AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 154 | 162 | water security | none | living-world foundation 1 | hidden AI delayed result uses the public branch and shared human effect path. |
| 159 | global survival and society | Filter room AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 154 | 162 | water security | none | living-world foundation 1 | hidden AI delayed result uses the filter branch and shared human effect path. |
| 160 | global survival and society | Guarded intake AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 154 | 162 | water security | none | living-world foundation 1 | hidden AI delayed result uses the guard branch and shared human effect path. |
| 161 | global survival and society | Well ledger callback | Implemented, dormant, uncounted | all eligible successors | callback | human visible | 155, 156, or 157 | 163 | water security | shared family art | living-world foundation 1 | branch-aware callback effects, shared cistern or exclusion memory, event-log payload, and cleanup preparation are wired. |
| 162 | global survival and society | Well ledger AI callback | Implemented, dormant, uncounted | all eligible successors | callback | hidden AI | 158, 159, or 160 | 163 | water security | none | living-world foundation 1 | hidden AI callback uses the same callback effects, memory, event-log payload, and cleanup path as human play. |
| 163 | global survival and society | Well Queue cleanup | Implemented, dormant, uncounted | all eligible successors | cleanup | hidden | any terminal Well Queue transaction | none | water security | none | living-world foundation 1 | exact cleanup tokens release the result and callback rows, clear the state-owned registry flag, and preserve save recovery. |
| 164 | global survival and society | The Animal Feed Debate | Implemented, dormant, uncounted | all eligible successors | routine incident | human visible | ordinary receipt through Fallout coordinator | 166, 167, or 168 | food security | `GFX_report_event_fallout_last_inventory` | living-world foundation 1 | three authored policies, current produced Air Winter food-reserve gate, deterministic result reservation, state feed ledger, Deaths-backed failure, event-log payload, callback, and authenticated cleanup are wired. |
| 165 | global survival and society | The Animal Feed Debate AI resolution | Implemented, dormant, uncounted | all eligible successors | hidden AI resolution | hidden | ordinary receipt through Fallout coordinator | 169, 170, or 171 | food security | none | living-world foundation 1 | hidden AI branch selection checks affordability and uses the same result reservation, effects, memory, event-log, and cleanup path as human play. |
| 166 | global survival and society | Kitchen feed result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 164 | 172 | food security | shared family art | living-world foundation 1 | three outcome descriptions, food and recognition effects, failure deaths, feed memory, event-log payload, and callback scheduling are wired. |
| 167 | global survival and society | Breeding reserve result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 164 | 172 | food security | shared family art | living-world foundation 1 | three outcome descriptions, breeding and adaptation effects, failure deaths, feed memory, event-log payload, and callback scheduling are wired. |
| 168 | global survival and society | Regional feed result | Implemented, dormant, uncounted | all eligible successors | delayed result | human visible | 164 | 172 | food security | shared family art | living-world foundation 1 | three outcome descriptions, depot and reclamation effects, failure deaths, feed memory, event-log payload, and callback scheduling are wired. |
| 169 | global survival and society | Kitchen feed AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 165 | 173 | food security | none | living-world foundation 1 | hidden AI delayed result uses the kitchen branch and shared human effect path. |
| 170 | global survival and society | Breeding reserve AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 165 | 173 | food security | none | living-world foundation 1 | hidden AI delayed result uses the breeding branch and shared human effect path. |
| 171 | global survival and society | Regional feed AI result | Implemented, dormant, uncounted | all eligible successors | delayed result | hidden AI | 165 | 173 | food security | none | living-world foundation 1 | hidden AI delayed result uses the regional branch and shared human effect path. |
| 172 | global survival and society | First harvest callback | Implemented, dormant, uncounted | all eligible successors | callback | human visible | 166, 167, or 168 | 174 | food security | shared family art | living-world foundation 1 | branch-neutral callback effects, first-harvest memory, event-log payload, and cleanup preparation are wired. |
| 173 | global survival and society | First harvest AI callback | Implemented, dormant, uncounted | all eligible successors | callback | hidden AI | 169, 170, or 171 | 174 | food security | none | living-world foundation 1 | hidden AI callback uses the same callback effects, memory, event-log payload, and cleanup path as human play. |
| 174 | global survival and society | Animal Feed Debate cleanup | Implemented, dormant, uncounted | all eligible successors | cleanup | hidden | any terminal Animal Feed transaction | none | food security | none | living-world foundation 1 | exact cleanup tokens release the result and callback rows, clear the state-owned feed registry and reserve, and preserve save recovery. |

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

The scan found existing Fallout suffixes in the request, transition, manual strike, and rewrite ranges. This ledger does not reuse those identifiers. Suffixes `62` through `84` remain reserved for Ash-week orientation. Suffixes `100` through `126`, `1009` through `1018`, `153` through `200`, and `204` through `281` remain reserved for the living-world pilot even if implementation order changes.

## Pilot gates

The ordinary scheduler remains locked until the Ash-week orientation package has all five required parts: national orientation, capital or main-state condition, immediate resource crisis, government-archetype introduction, and the first character or institution. Completing orientation still does not approve or activate the scheduler.

The three pilot report assets exist and their sprites are registered in `interface/fallout_world_end.gfx`. The immediate-resource asset is attached to human events `70` and `72`, and the government asset is attached to human events `74` and `76`. The capital asset remains unattached because its exact repair surface is blocked. Event counting cannot begin until the gameplay rows, AI resolution, delayed results, callbacks, cleanup, target registries, and event asset references pass manual review.

The typed constants for suffixes `100` through `126` are identity reservations only. Primary ownership is `global survival and society`. Food, water, and transport are cooldown families and do not own release-floor counts.

## Count status

Reserved Ash-week orientation identities: `23`.

Reserved living-world pilot identities: `38`.

Total reserved documentation identities across both tranches: `50`.

Defined Ash-week orientation blocks: `15`, covering the uncounted national-orientation pilot at `62` through `65`, immediate-resource pilot at `70` through `73`, government-authority pilot at `74` through `77`, and dormant closure and cleanup at `82` through `84`.

Defined living-world pilot blocks: `37`, covering the dormant food-security blocks at `100` through `106`, the River Intake blocks at `107` through `113` and `121`, the Rail Crew Twenty-Seven blocks at `114` through `120` and `122`, the hidden food companions at `123` through `126`, the hidden water companions at `1009` through `1013`, and the hidden rail companions at `1014` through `1018`.

Countable manually reviewed Fallout living-world blocks: `0 of 660`.

The release-floor counter must remain unchanged until individual rows pass implementation and audit.

## Well Queue count correction

The Well Queue reservation adds eleven dormant suffixes, so the authoritative living-world pilot total is 38 identities, 48 defined blocks, and 0 countable blocks. This correction supersedes the earlier pre-153 summary values above.

Well Queue event suffixes `153` through `163` are dormant and uncounted. Their candidate row is `153`, transaction key `710004`, and route `7104`.

The authoritative total reserved documentation identities is `61`, combining
`23` Ash-week identities with `38` living-world identities. The authoritative
defined living-world block count is `48`, including the Well Queue blocks.

The Well Queue row also pays its selected branch cost only after delayed-row
reservation and ordinary-receipt consumption succeed. Its country payment flag
is released by event `163` cleanup.

## Animal Feed count correction

The Animal Feed Debate reservation adds eleven dormant suffixes, so the
authoritative living-world pilot total is `49` identities, `59` defined blocks,
and `0` countable blocks. This correction supersedes the earlier Well Queue
summary values above.

Animal Feed event suffixes `164` through `174` are dormant and uncounted. The
candidate row is `164`, transaction key `710005`, and route `7105`. Its native
state gate requires a current produced Air Winter food reserve, and its branch
payment flag is released by event `174` cleanup only after delayed-row
reservation and ordinary-receipt consumption succeed.

The authoritative total reserved documentation identities is `72`, combining
`23` Ash-week identities with `49` living-world identities. The countable
living-world release-floor total remains `0 of 660`.

## Ash-week capital and character completion correction

The capital condition blocks `66` through `69` and the character or institution
blocks `78` through `81` are now defined in the dedicated Fallout event file.
The authoritative Ash-week defined-block count is therefore `23` of `23`, but
all 23 remain dormant and uncounted until callers, caller-owned event receipts,
accepted runtime Event Log and Event Details delivery, complete regional and
archetype coverage, candidate installation surfaces, manual audits, and the
host-authority gate are complete. The countable
Fallout living-world release-floor total remains `0 of 660`.

## Ash-week orientation event-log correction

The five orientation components now share Fallout memory history `9110` with
45 explicit component, branch, and outcome payloads. The writer is idempotent
per component and transition generation, and it refreshes the shared Event Log
views after a committed row. The history name, detail type, and generic detail
window route are statically wired. The history surface remains dormant and
earns no release-floor credit until the orientation caller, coverage,
activation, audits, and runtime gates are approved.

## Triage Wall count correction

The Triage Wall reservation adds thirteen dormant suffixes, so the authoritative
living-world pilot total is `62` identities and `72` defined blocks. The chain
uses event suffixes `175` through `187`, candidate id `175`, transaction key
`710006`, route `7106`, and history id `9111`.

Its candidate gate requires a produced Air Winter shelter snapshot, current
medicine below the pressure band, affordable policy cost, current state
ownership, and shelter capacity above the reviewed minimum. Four policy lanes
have human and hidden AI result events, followed by a human and hidden AI
doctor callback and authenticated cleanup. The chain remains dormant and
uncounted. The countable Fallout living-world release-floor total remains
`0 of 660`.

## Seed Vault Custody count correction

The Seed Vault Custody reservation adds thirteen dormant suffixes, so the
authoritative living-world pilot total is `75` identities and `85` defined
blocks. The chain uses event suffixes `188` through `200`, candidate id `188`,
transaction key `710007`, route `7107`, and history id `9112`.

Its candidate gate requires an Air Winter seed-memory receipt, a produced
snapshot, current reclamation and adaptation, and an owned state with an exact
current-generation resource row. Four policy lanes have human and hidden AI
result events, followed by a human and hidden AI agronomist callback and
authenticated cleanup. The chain remains dormant and uncounted. The countable
Fallout living-world release-floor total remains `0 of 660`.

## Bad Batch count correction

The Bad Batch reservation adds thirteen dormant suffixes, so the authoritative
living-world pilot total is `88` identities and `98` defined blocks. The chain
uses event suffixes `204` through `216`, candidate id `204`, transaction key
`710008`, route `7108`, and history id `9113`. Its candidate row requires a
generation-bound seed or greenhouse provenance receipt, produced Air Winter
snapshot, state reclamation and adaptation thresholds, and an affordable
branch. Four human and hidden-AI result lanes share one delayed scheduler
transaction, a ninety-day callback, Deaths-backed failure handling, Event Log
payloads, and authenticated cleanup. The chain remains dormant and uncounted.
The countable Fallout living-world release-floor total remains `0 of 660`.

## Filters Fail count correction

The Filters Fail reservation adds thirteen dormant suffixes, so the
authoritative living-world pilot total is `101` identities and `111` defined
blocks. The chain uses event suffixes `217` through `229`, candidate id `217`,
transaction key `710009`, route `7109`, and history id `9114`.

Its candidate gate requires shelter capacity, current Filters pressure, a
produced Air Winter snapshot, and an affordable branch. The chain remains
dormant and uncounted. The countable Fallout living-world release-floor total
remains `0 of 660`.

## Door List count correction

The Door List survival transaction adds thirteen dormant event blocks at
suffixes `230` through `242`. The candidate row is `230`, transaction key
`710010`, route `7110`, and history id `9115`. The chain selects one current
source state with a higher Air Winter exposure and one current shelter-
qualified destination state. It freezes the two-state population ledger,
applies the accepted branch viability and movement bands, records source
losses through the shared exact population contract, and uses a delayed
callback with authenticated cleanup. It remains dormant and uncounted because
the scheduler activation gates, host proof, and runtime state-target proof are
still open. The documented living-world block total is now `124` and the
countable Fallout living-world release-floor total remains `0 of 660`.

## Last Transformer count correction

The Last Transformer power-grid reservation adds thirteen dormant event
blocks at suffixes `243` through `255`. The candidate row is `243`,
transaction key `710011`, route `7111`, and history id `9116`. The chain
selects one current state with a produced Air Winter snapshot, durable Supply
Access, repairable infrastructure, an operational civilian or military
factory, exposure above `20`, reclamation above `15`, and Power below `55`.
Priority is deterministic from infrastructure, industry, airbase, and
dockyard evidence with lowest state id as the tie break. A neighbouring AI
country is selected by Power plus its highest owned-state reclamation, with
lowest country id as the tie break.

The human and hidden-AI lanes share four costed plans, one delayed result at
exactly ten days, branch-specific viability and outcome bands, Deaths-backed
failure handling, one callback at exactly 120 days, Event Log payloads, timed
country modifiers, and authenticated cleanup. It remains dormant and
uncounted because scheduler activation, host proof, and runtime state-target
proof are still open. The documented living-world block total is now `137`
and the countable Fallout living-world release-floor total remains `0 of
660`.

## Fever Dormitory count correction

The Fever Dormitory disease and shelter transaction adds thirteen dormant event
blocks at suffixes `256` through `268`. The candidate row is `256`, transaction
key `710012`, route `7112`, and history id `9117`. It selects the lowest owned
state with a current produced Air Winter shelter receipt, disease pressure in
the crisis band, low Medicine, and an affordable policy.

The four human policies and four hidden-AI result lanes share deterministic
viability, branch costs, delayed results at exactly fourteen days, a callback
at exactly 120 days, Deaths-backed failure, fifteen Event Log payloads, and
authenticated cleanup. Dedicated report art and the shared name, detail, and
Event Details routes are wired. Scheduler activation, host authority,
save-recovery, state-target scope, multiplayer behavior, and runtime Event Log
delivery remain unobserved. The documented living-world block total is now
`150`, while the countable Fallout living-world release-floor total remains
`0 of 660`.

## Names for the Missing count correction

Names for the Missing adds thirteen dormant country-level event blocks at
suffixes `269` through `281`. The candidate row is `269`, transaction key
`710013`, route `7113`, and history id `9118`. It freezes country Deaths,
Recognition, Cohesion, and intelligence exposure, then offers four costed
census and memorial policies with deterministic delayed results, a callback,
Deaths-backed failure, dedicated modifiers, and authenticated cleanup. The
documented living-world block total is now `163`, while the countable Fallout
living-world release-floor total remains `0 of 660`.

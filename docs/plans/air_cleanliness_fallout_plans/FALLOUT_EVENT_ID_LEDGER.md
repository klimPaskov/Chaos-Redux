# Fallout Event ID Ledger

## Purpose

This ledger owns suffix allocation inside `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

The dedicated event file was scanned on 2026-07-15 before this reservation. Suffixes `100` through `122` were unused. This reservation does not count as implemented content. A row becomes countable only after final localisation, gameplay effects, AI behavior, memory or closure, cleanup, asset disposition, and manual audit are complete.

## Reserved living-world pilot tranche

| Suffix | Primary family | Working design anchor | Final localisation keys | Ownership | Event class | Visibility | Caller | Follow-up | Cooldown family | Asset | Batch | Audit status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | global survival and society | The Last Inventory | Pending implementation | all eligible successors | crisis incident | human visible | Fallout coordinator scheduler | 102, 103, or 104 | food security | `GFX_report_event_fallout_last_inventory` | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 101 | global survival and society | The Last Inventory AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | event 100 dispatcher | 102, 103, or 104 | food security | none | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 102 | global survival and society | Publish the storehouse ledger | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 100 or 101 | 105 | food security | shared family art | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 103 | global survival and society | Hide shortage and protect household caches | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 100 or 101 | 105 | food security | shared family art | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 104 | global survival and society | Seize disputed reserves | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 100 or 101 | 105 | food security | shared family art | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 105 | global survival and society | First winter ration review | Pending implementation | all eligible successors | arc callback | human visible or hidden AI | 102, 103, or 104 | 106 | food security | shared family art | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 106 | global survival and society | Inventory arc cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | 105 or recovery reconcile | none | food security | none | living-world foundation 1 | blocked by survival ledger and complete ash-week orientation substrate |
| 107 | global survival and society | River Intake at Dawn | Pending implementation | all eligible successors | crisis incident | human visible | Fallout coordinator scheduler | 109, 110, 111, or 121 | water security | `GFX_report_event_fallout_river_intake_at_dawn` | living-world foundation 1 | blocked by event-specific fourth-choice tuning and curated intake registry |
| 108 | global survival and society | River Intake at Dawn AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | event 107 dispatcher | 109, 110, 111, or 121 | water security | none | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 109 | global survival and society | Close the intake | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 107 or 108 | 112 | water security | shared family art | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 110 | global survival and society | Ration filtered flow | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 107 or 108 | 112 | water security | shared family art | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 111 | global survival and society | Seize upstream pumps | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 107 or 108 | 112 | water security | shared family art | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 112 | global survival and society | Water compact or epidemic callback | Pending implementation | all eligible successors | arc callback | human visible or hidden AI | 109, 110, 111, or 121 | 113 | water security | shared family art | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 113 | global survival and society | Intake arc cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | 112 or recovery reconcile | none | water security | none | living-world foundation 1 | blocked by four-choice tuning and curated intake registry |
| 114 | global survival and society | Rail Crew Twenty-Seven | Pending implementation | all eligible successors | crisis incident | human visible | Fallout coordinator scheduler | 116, 117, 118, or 122 | transport recovery | `GFX_report_event_fallout_rail_crew_twenty_seven` | living-world foundation 1 | blocked by event-specific fourth-choice tuning, curated corridor registry, and proven rail repair surface |
| 115 | global survival and society | Rail Crew Twenty-Seven AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | event 114 dispatcher | 116, 117, 118, or 122 | transport recovery | none | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 116 | global survival and society | Protect the repair crews | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 114 or 115 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 117 | global survival and society | Use forced labor | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 114 or 115 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 118 | global survival and society | Abandon the exposed line | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 114 or 115 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 119 | global survival and society | Corridor outcome callback | Pending implementation | all eligible successors | arc callback | human visible or hidden AI | 116, 117, 118, or 122 | 120 | transport recovery | shared family art | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 120 | global survival and society | Rail arc cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | 119 or recovery reconcile | none | transport recovery | none | living-world foundation 1 | blocked by four-choice tuning, curated corridor registry, and proven rail repair surface |
| 121 | global survival and society | Foreign intake testing result | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 107 or 108 | 112 | water security | shared family art | living-world foundation 1 | blocked by fourth-choice tuning and curated foreign-testing registry |
| 122 | global survival and society | Neighbor corridor access result | Pending implementation | all eligible successors | delayed result | human visible or hidden AI | 114 or 115 | 119 | transport recovery | shared family art | living-world foundation 1 | blocked by fourth-choice tuning, curated bilateral corridor registry, and proven rail repair surface |

## Collision boundary

The scan found existing Fallout suffixes in the request, transition, manual strike, and rewrite ranges. This tranche does not reuse those identifiers. Suffixes `100` through `122` remain reserved for this exact batch even if implementation order changes.

## Pilot gates

The ordinary scheduler remains locked until the ash-week orientation package has all five required parts: national orientation, capital or main-state condition, immediate resource crisis, government-archetype introduction, and the first character or institution.

The three pilot report assets exist and their sprites are registered in `interface/fallout_world_end.gfx`. They remain unattached because the corresponding event roots are not defined. Event counting cannot begin until the gameplay rows, AI resolution, delayed results, callbacks, cleanup, target registries, and event asset references pass manual review.

The typed constants for suffixes `100` through `122` are identity reservations only. Primary ownership is `global survival and society`. Food, water, and transport are cooldown families and do not own release-floor counts.

## Count status

Reserved typed identities in this tranche: `23`.

Defined event blocks in this tranche: `0`.

Countable manually reviewed event blocks in this tranche: `0`.

The release-floor counter must remain unchanged until individual rows pass implementation and audit.

# Fallout Event ID Ledger

## Purpose

This ledger owns suffix allocation inside `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

The dedicated event file was scanned on 2026-07-15 before this reservation. Suffixes `100` through `126` were unused. This reservation does not count as implemented content. A row becomes countable only after final localisation, gameplay effects, AI behavior, memory or closure, cleanup, asset disposition, and manual audit are complete.

## Reserved living-world pilot tranche

| Suffix | Primary family | Working design anchor | Final localisation keys | Ownership | Event class | Visibility | Caller | Follow-up | Cooldown family | Asset | Batch | Audit status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | global survival and society | The Last Inventory | Pending implementation | all eligible successors | crisis incident | human visible | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | `GFX_report_event_fallout_last_inventory` | living-world foundation 1 | ordinary reservation contract proven, content blocked by numerical survival, orientation, and tuning |
| 101 | global survival and society | The Last Inventory AI resolution | Hidden event, no player text | all eligible successors | hidden AI resolution | hidden | future ordinary receipt through Fallout coordinator | 102/123, 103/124, or 104/125 | food security | none | living-world foundation 1 | ordinary reservation contract proven, content blocked by numerical survival, orientation, and tuning |
| 102 | global survival and society | Publish the storehouse ledger | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 103 | global survival and society | Hide shortage and protect household caches | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 104 | global survival and society | Seize disputed reserves | Pending implementation | all eligible successors | delayed result | human visible | 100 or 101 | 105 or 126 | food security | shared family art | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 105 | global survival and society | First winter ration review | Pending implementation | all eligible successors | callback | human visible | 102, 103, 104, 123, 124, or 125 | 106 | food security | shared family art | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 106 | global survival and society | Inventory chain cleanup | Hidden event, no player text | all eligible successors | cleanup | hidden | any terminal inventory transaction | none | food security | none | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
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
| 123 | global survival and society | Publish the storehouse ledger AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 124 | global survival and society | Protect household caches AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 125 | global survival and society | Requisition disputed reserves AI result | Hidden event, no player text | all eligible successors | delayed result | hidden AI | 100 or 101 | 105 or 126 | food security | none | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |
| 126 | global survival and society | First winter ration review AI callback | Hidden event, no player text | all eligible successors | callback | hidden AI | 102, 103, 104, 123, 124, or 125 | 106 | food security | none | living-world foundation 1 | blocked by numerical survival, orientation, and tuning |

## Collision boundary

The scan found existing Fallout suffixes in the request, transition, manual strike, and rewrite ranges. This tranche does not reuse those identifiers. Suffixes `100` through `126` remain reserved for this exact batch even if implementation order changes.

## Pilot gates

The ordinary scheduler remains locked until the ash-week orientation package has all five required parts: national orientation, capital or main-state condition, immediate resource crisis, government-archetype introduction, and the first character or institution.

The three pilot report assets exist and their sprites are registered in `interface/fallout_world_end.gfx`. They remain unattached because the corresponding event roots are not defined. Event counting cannot begin until the gameplay rows, AI resolution, delayed results, callbacks, cleanup, target registries, and event asset references pass manual review.

The typed constants for suffixes `100` through `126` are identity reservations only. Primary ownership is `global survival and society`. Food, water, and transport are cooldown families and do not own release-floor counts.

## Count status

Reserved typed identities in this tranche: `27`.

Defined event blocks in this tranche: `0`.

Countable manually reviewed event blocks in this tranche: `0`.

The release-floor counter must remain unchanged until individual rows pass implementation and audit.

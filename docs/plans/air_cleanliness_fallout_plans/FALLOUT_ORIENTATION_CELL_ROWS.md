# Fallout Ash-week region and archetype cell rows

Disposition: implemented (static review; live delivery and AI choice frequencies are `needs_live_game`). Acceptance basis: the accepted coverage matrix `docs/specs/air_cleanliness_fallout_specs/matrices/fallout_orientation_region_archetype_coverage_matrix.md`, round 2 lead item 3, and agent decision A14 in `agent_decisions_2026-10-04.md`.

## What a cell row is

Every registry country with a `fallout_region_id` and a `fallout_government_archetype` has one of 108 cell rows. `fallout_orientation_refresh_cell_row` loads it once per generation from the `fallout_orientation_cell_*` script constants (key `r<region>_a<archetype>`) into the country variables `fallout_orientation_cell_*`. The row supplies:

- the resource the local measure pays (Fuel or Power) and the AI's preferred resource branch;
- the consolidation benefit (kind and amount) and the AI's preferred government branch;
- the matrix's unavailable branch and the world-state condition that reopens it.

Resource crisis (events 70 to 73) and government archetype (events 74 to 77) now run for every such country. A pilot memory row takes precedence when the country's memory, region and archetype all match it; otherwise the cell row is used. The unavailable branch applies to every row, pilot rows included, because it belongs to the region and archetype cell.

## Enforcement

- `fallout_orientation_resource_branch_<n>_is_locked` and `fallout_orientation_government_branch_<n>_is_locked` are true when the branch is the cell's unavailable branch and its condition does not hold.
- The event option triggers (`fallout_orientation_*_branch_<n>_is_available`), the shared affordability trigger used by the human choice and the hidden AI chooser (`fallout_orientation_branch_is_affordable`), and the begin checks (`fallout_orientation_requested_*_has_affordable_branch`) all exclude a locked branch, so human and hidden AI routes are identical.
- Events 70 and 74 name a closed course and what reopens it through `GetFalloutOrientationResourceLockNotice` and `GetFalloutOrientationGovernmentLockNotice`.
- The step is skipped without a popup only when the country has no region or archetype, when no branch it can pay for remains, or when its capital stays missing past the retry window.

The nine mutant polity cells have no locked branch. The matrix's unavailable branch for them is an exclusion or custody branch, and no such branch exists among the three offered courses.

## Text

Each cell has nine hand-written strings in `localisation/english/fallout_consolidated_l_english.yml` (`fallout_orientation_cell_<family>_<region>_<archetype>`): resource opening, local measure option, resource result, government opening, consolidation, shared compact and rival options, government result, and the closure line. The scripted localisation families in `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt` select the pilot text only when the frozen or resolved identity is the pilot row, then the cell text.

## Cell table

Lock thresholds live in `fallout_orientation_cell_lock_threshold`: Fuel 15, Power 15, Recognition 30, Cohesion 30, capital supply access 25, Filters 15, Clean water 15, Medicine 15, Food 15, Shelter capacity 15, and a capital below Air Winter phase 5.

| Region | Archetype | Local measure pays | AI resource | Consolidation benefit | AI government | Unavailable branch | Reopens when |
| --- | --- | --- | --- | --- | --- | --- | --- |
| north america | continuity government | Fuel | ration | recognition 5 | division | Consolidation | recognition |
| north america | bunker authority | Fuel | tailored | recovery 4 | consolidate | Shared compact | capital below phase 5 |
| north america | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| north america | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food |
| north america | maritime remnant | Fuel | tailored | supply 5 | consolidate | Consolidation | coastal capital |
| north america | quarantine state | Power | ration | recovery 5 | division | Local measure | medicine and water |
| north america | scavenger syndicate | Fuel | tailored | reclamation 5 | consolidate | Local measure | capital industry |
| north america | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | fuel |
| north america | machine protocol | Power | ration | adaptation 4 | division | Consolidation | recognition |
| north america | technate | Power | tailored | supply 5 | division | Local measure | power |
| north america | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| north america | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| europe | continuity government | Power | ration | recognition 5 | division | Consolidation | capital below phase 5 |
| europe | bunker authority | Power | tailored | recovery 4 | division | Shared compact | power |
| europe | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| europe | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food |
| europe | maritime remnant | Fuel | tailored | supply 5 | division | Rival brought in | coastal capital |
| europe | quarantine state | Fuel | ration | recovery 5 | division | Local measure | receiving state |
| europe | scavenger syndicate | Power | tailored | reclamation 5 | consolidate | Local measure | power and recognition |
| europe | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | supply access |
| europe | machine protocol | Power | ration | adaptation 4 | division | Consolidation | cohesion |
| europe | technate | Power | tailored | supply 5 | division | Local measure | power and recognition |
| europe | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| europe | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| eurasian interior | continuity government | Fuel | ration | recognition 5 | division | Consolidation | recognition |
| eurasian interior | bunker authority | Power | tailored | recovery 4 | division | Shared compact | exposure below shelter |
| eurasian interior | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| eurasian interior | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food |
| eurasian interior | maritime remnant | Fuel | tailored | supply 5 | consolidate | Consolidation | coastal capital |
| eurasian interior | quarantine state | Fuel | ration | recovery 5 | division | Consolidation | receiving state |
| eurasian interior | scavenger syndicate | Power | tailored | reclamation 5 | division | Local measure | recognition |
| eurasian interior | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | fuel |
| eurasian interior | machine protocol | Power | ration | adaptation 4 | division | Emergency warrant | single state |
| eurasian interior | technate | Power | tailored | supply 5 | division | Local measure | power |
| eurasian interior | mutant polity | Fuel | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| eurasian interior | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| east asia | continuity government | Power | ration | recognition 5 | division | Consolidation | recognition |
| east asia | bunker authority | Power | tailored | recovery 4 | division | Shared compact | exposure below shelter |
| east asia | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | food |
| east asia | food compact | Fuel | tailored | recovery 5 | division | Local measure | water |
| east asia | maritime remnant | Fuel | tailored | supply 5 | division | Local measure | medicine |
| east asia | quarantine state | Power | ration | recovery 5 | consolidate | Consolidation | receiving state |
| east asia | scavenger syndicate | Power | tailored | reclamation 5 | division | Local measure | power and recognition |
| east asia | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | supply access |
| east asia | machine protocol | Power | ration | adaptation 4 | division | Consolidation | filters |
| east asia | technate | Power | tailored | supply 5 | division | Local measure | power and recognition |
| east asia | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| east asia | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| south asia | continuity government | Power | ration | recognition 5 | division | Local measure | water |
| south asia | bunker authority | Fuel | tailored | recovery 4 | division | Shared compact | water and shelter |
| south asia | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel |
| south asia | food compact | Fuel | tailored | recovery 5 | division | Local measure | water |
| south asia | maritime remnant | Fuel | tailored | supply 5 | division | Local measure | medicine |
| south asia | quarantine state | Fuel | ration | recovery 5 | division | Consolidation | receiving state |
| south asia | scavenger syndicate | Power | tailored | reclamation 5 | consolidate | Local measure | crisis not medicine |
| south asia | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | fuel |
| south asia | machine protocol | Power | ration | adaptation 4 | division | Consolidation | single state |
| south asia | technate | Power | tailored | supply 5 | division | Local measure | power and recognition |
| south asia | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| south asia | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| middle east north africa | continuity government | Fuel | ration | recognition 5 | division | Local measure | supply access |
| middle east north africa | bunker authority | Fuel | tailored | recovery 4 | division | Shared compact | water and fuel |
| middle east north africa | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| middle east north africa | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food or water |
| middle east north africa | maritime remnant | Fuel | tailored | supply 5 | division | Local measure | water and shelter |
| middle east north africa | quarantine state | Power | ration | recovery 5 | division | Shared compact | medicine |
| middle east north africa | scavenger syndicate | Power | tailored | reclamation 5 | consolidate | Local measure | capital industry |
| middle east north africa | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | supply access |
| middle east north africa | machine protocol | Power | ration | adaptation 4 | division | Consolidation | water |
| middle east north africa | technate | Power | tailored | supply 5 | division | Local measure | power and recognition |
| middle east north africa | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| middle east north africa | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| sub saharan africa | continuity government | Power | ration | recognition 5 | division | Consolidation | supply access |
| sub saharan africa | bunker authority | Power | tailored | recovery 4 | division | Local measure | water and shelter |
| sub saharan africa | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| sub saharan africa | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food |
| sub saharan africa | maritime remnant | Fuel | tailored | supply 5 | division | Consolidation | coastal capital |
| sub saharan africa | quarantine state | Fuel | ration | recovery 5 | division | Consolidation | medicine and water |
| sub saharan africa | scavenger syndicate | Power | tailored | reclamation 5 | division | Local measure | water |
| sub saharan africa | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | water |
| sub saharan africa | machine protocol | Power | ration | adaptation 4 | division | Consolidation | single state |
| sub saharan africa | technate | Power | tailored | supply 5 | division | Local measure | power |
| sub saharan africa | mutant polity | Fuel | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| sub saharan africa | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| latin america caribbean | continuity government | Power | ration | recognition 5 | division | Consolidation | capital below phase 5 |
| latin america caribbean | bunker authority | Power | tailored | recovery 4 | division | Shared compact | water and shelter |
| latin america caribbean | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel and supply |
| latin america caribbean | food compact | Fuel | tailored | recovery 5 | division | Local measure | crisis not food |
| latin america caribbean | maritime remnant | Fuel | tailored | supply 5 | division | Shared compact | medicine |
| latin america caribbean | quarantine state | Power | ration | recovery 5 | division | Consolidation | receiving state |
| latin america caribbean | scavenger syndicate | Power | tailored | reclamation 5 | consolidate | Local measure | recognition |
| latin america caribbean | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | supply access |
| latin america caribbean | machine protocol | Power | ration | adaptation 4 | division | Consolidation | single state |
| latin america caribbean | technate | Power | tailored | supply 5 | division | Local measure | power and recognition |
| latin america caribbean | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| latin america caribbean | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |
| oceania remote islands | continuity government | Fuel | ration | recognition 5 | division | Consolidation | supply access |
| oceania remote islands | bunker authority | Fuel | tailored | recovery 4 | division | Shared compact | water and shelter |
| oceania remote islands | warlord command | Fuel | requisition | supply 4 | rival | Emergency warrant | fuel |
| oceania remote islands | food compact | Power | tailored | recovery 5 | division | Local measure | water and shelter |
| oceania remote islands | maritime remnant | Fuel | tailored | supply 5 | consolidate | Local measure | fuel |
| oceania remote islands | quarantine state | Fuel | ration | recovery 5 | consolidate | Consolidation | receiving state |
| oceania remote islands | scavenger syndicate | Power | tailored | reclamation 5 | consolidate | Local measure | recognition |
| oceania remote islands | nomad convoy | Fuel | tailored | adaptation 5 | division | Local measure | fuel |
| oceania remote islands | machine protocol | Power | ration | adaptation 4 | division | Consolidation | single state |
| oceania remote islands | technate | Power | tailored | supply 5 | division | Local measure | power |
| oceania remote islands | mutant polity | Power | tailored | cohesion 5 | division | none (no exclusion branch exists) | none |
| oceania remote islands | religious refuge | Fuel | ration | cohesion 5 | division | Consolidation | recognition |

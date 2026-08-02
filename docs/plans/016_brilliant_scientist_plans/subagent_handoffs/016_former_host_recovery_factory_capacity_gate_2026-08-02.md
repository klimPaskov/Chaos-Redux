# Event 016 Former-Host Recovery Factory-Capacity Gate Handoff

## Status

Patched a narrow recovery-board availability defect.

No commit was created or staged.

No models, model consumers, GUI files, or parent-owned Directorate Institutions files were changed.

## Issue list

### Medium, fixed: recovery actions could consume resources without their advertised factory capacity

`brilliant_scientist_reconstruct_independent_research`, `brilliant_scientist_secure_abandoned_archive`, `brilliant_scientist_offer_amnesty_to_assistants`, and `brilliant_scientist_request_international_inspection` each reserve two or three civilian factories for their full timed duration.

Before this patch, none required that many civilian factories to be available for a new project before the player or AI could pay political power, equipment, or manpower and begin the action.

The four decisions now use `num_of_civilian_factories_available_for_projects` to require the exact central threshold from `brilliant_scientist_recovery_cost`.

No further isolated, safe decision or mission defect was identified in the audited foreign, containment, recovery, and KRG surfaces.

## Changed files and identifiers

| File | Identifiers | Change |
| --- | --- | --- |
| `common/decisions/016_brilliant_scientist_former_host_recovery_decisions.txt` | `brilliant_scientist_reconstruct_independent_research` | Added the three-free-factory availability gate. |
| Same file | `brilliant_scientist_secure_abandoned_archive` | Added the two-free-factory availability gate. |
| Same file | `brilliant_scientist_offer_amnesty_to_assistants` | Added the two-free-factory availability gate. |
| Same file | `brilliant_scientist_request_international_inspection` | Added the three-free-factory availability gate. |

The patch reads the existing global constants `brilliant_scientist_recovery_cost.reconstruct_research_factories`, `secure_archive_factories`, `offer_amnesty_factories`, and `international_inspection_factories`.

The pre-existing file-local constants remain the `civilian_factory_use` modifier values because that modifier field already uses them successfully.

## Before and after behavior

Before, a former host could launch a recovery decision while all civilian factories were unavailable to new projects, then immediately pay the decision's political power, equipment, or manpower costs.

After, the decision remains unavailable until the former host has the same two or three civilian factories free that the action will reserve during its timer.

The actions retain their existing one-time receipts, resource spends, cancellation effects, success effects, and AI weights.

## Decision category lifecycle notes

The former-host recovery category is owned by the former Event 016 host after Kruger's departure.

`brilliant_scientist_former_host_recovery_actor` requires a live former host with its capital and an Event 016 facility still under its control, while excluding the current host, Kruger State, world-end state, and previously closed recovery board.

The board stays open while any action remains unresolved.

Only one recovery action can run at a time through `brilliant_scientist_former_host_recovery_action_is_idle`.

Each action ends in a permanent success or failure receipt, and three successes close the board through `brilliant_scientist_former_host_recovery_refresh` and retire the vacuum lifecycle as appropriate.

All four failures also close the board without granting the same capacity reward through another route.

## Timed decision quality notes

This recovery surface has no HOI4 mission entries.

Its four timed decisions provide the mission-like lifecycle below.

| Action | Owner and category | Region | Requirement | Duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| Reconstruct independent research | Former host, recovery board | Country | Idle board, assistants, recruited cohort, 3 free factories, support equipment, manpower | 150 days | Restores capacity and records one success | Actor or assistant loss calls `brilliant_scientist_fail_recovery_research`; one-time success or failure flags prevent duplication. |
| Secure abandoned archive | Former host, recovery board | Selected owned and controlled Event 016 facility state with supply node | Idle board, 2 free factories, support equipment, trucks | 120 days | Secures the selected archive and records one success | Actor loss or archive-state loss calls `brilliant_scientist_fail_recovery_archive`; secured or lost state flags prevent repeat recovery. |
| Offer amnesty | Former host, recovery board | Country | Idle board, surviving assistants, 2 free factories, support equipment, manpower | 90 days | Adds capacity, lowers grievance, and records infiltration risk | Actor or assistant loss calls `brilliant_scientist_fail_recovery_amnesty`; terminal country flags prevent duplication. |
| Request international inspection | Former host, recovery board | Country | Idle board, foreign access, 3 free factories, support equipment, trucks | 180 days | Adds capacity, lowers exposure, joins the technology-sharing network, and records one success | Actor or foreign-access loss calls `brilliant_scientist_fail_recovery_inspection`; terminal country flags prevent duplication. |

## Cost and requirement clarity

The recovery actions already combine political power with concrete support equipment, manpower, or trucks and timed civilian factory use.

The new gates make the existing factory commitment enforceable before spending begins.

The existing localisation descriptions already explain research factory time, field detachment requirements, or inspection time and equipment.

No localisation change was needed, and the concurrently edited `localisation/english/016_brilliant_scientist_recovery_l_english.yml` file was intentionally not touched.

## AI validity and route-lock notes

All four recovery actions already have `ai_will_do` blocks.

Because the factory condition is in `available`, AI cannot choose an action that lacks the civilian project capacity required by its modifier.

Actor, facility-state, assistant, foreign-access, capital-control, and terminal-world-state checks remain the route locks that prevent invalid former-host targets.

## Localisation and tooltip notes

The existing decision and completion tooltip identifiers are present for all four actions.

No new player-facing key was introduced.

The standard unavailable-decision condition exposes the new capacity requirement without a long raw trigger or a stale bespoke tooltip.

## Cleanup and exploit-risk notes

Each cancellation effect clears its in-progress flag and writes a terminal failure receipt.

Each success clears its in-progress flag, writes a terminal success receipt, and registers recovery progress.

`fire_only_once`, action-idle gating, terminal receipts, and selected-state flags already prevent duplicate capacity, equipment, or progress awards.

The new availability checks remove a resource-sink and AI-invalidity path in which an action could spend its material cost while its factory burden was impossible to meet.

## Validation

Reviewed the offline Decision Modding reference and vanilla `common/decisions/AST.txt`, which uses `num_of_civilian_factories_available_for_projects` to gate civilian-factory-consuming decisions.

Checked the vanilla trigger documentation entry for `num_of_civilian_factories_available_for_projects`.

Ran a focused static mapping over the four patched decision blocks and confirmed that each availability threshold matches its existing `civilian_factory_use` modifier and central recovery constant: reconstruct 3, archive 2, amnesty 2, inspection 3.

The `NOT = { ... < constant:... }` form follows the existing Event 016 cross-domain review trigger pattern and expresses an inclusive exact minimum without unsupported operators.

## Skipped meaningful validation

No live game session was launched because live validation belongs to the user.

No scripted GUI inspection or render was needed because this patch does not change a decision-owned GUI surface.

No localisation validation was run because no localisation was edited and that file has concurrent work by another agent.

## Remaining issues and uncertainty

The patch does not alter recovery rewards, timing, AI weights, or the three-success completion threshold, so their live-session balance remains for the parent and user to assess in the complete Event 016 pass.

The parent is implementing a separate Directorate Institutions conflict and grant-rotation tranche; this recovery-only patch deliberately avoids those files and shared tuning surfaces.

The user deferred all 3D model work, and none was performed here.

No fallback or simplification was used.

## Plan handoff path

This file is the implementation handoff.

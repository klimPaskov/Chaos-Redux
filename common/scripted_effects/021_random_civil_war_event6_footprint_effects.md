# Event 021 Event 006 Native Release Footprint

## Overview

`021_random_civil_war_event6_footprint_effects.txt` and `021_random_civil_war_event6_footprint_triggers.txt` keep the Event 021 front ledger in step with the map when an Event 006 carrier is born from a crisis host.

Native `release = TAG` hands the carrier every state its donor owns that is a core of that carrier, whoever controls it, not only the explicitly assigned anchor.
Event 006 owns the package-to-carrier crosswalk, so `independence_wave_collect_event021_native_release_footprint` and `independence_wave_state_is_event021_native_release_core` live in the Event 006 adapter registry files and are documented in `006_independence_wave_event021_adapter_registry_effects.md`.
This file validates that transfer set, publishes it into the ledger before the map changes, proves it again at the mutation gate, and records what the carrier received.

## Footprint rules

The footprint of a package is every state the donor owns that is a core of the registered static carrier, plus the anchor.
It is empty when the static carrier already exists, because the release then does nothing and only the anchor changes hands.
A package is admitted only when every non-anchor member is owned and controlled by the donor, is not the donor's capital, and is not held by another Event 021 reservation, front anchor, or candidate row.
An unsafe footprint rejects the whole package.
The package is never reduced to its anchor, and the release is never narrowed by stripping cores.

## Helper contracts

`event021_parent_collect_event6_native_footprint` runs in the donor country scope.
Inputs are the temporary `event021_event6_footprint_input_package_id`, the temporary `event021_event6_footprint_check_rows`, and the regular target `event021_event6_footprint_anchor`.
The caller declares `event021_event6_footprint_valid` and the temporary array `independence_wave_event021_footprint_states` before the call.
`event021_event6_footprint_check_rows` is 1 only while candidate rows are being assembled, so a member already held by another row of the same collection blocks the package; the plan and mutation gates pass 0 because the ledger already holds the footprint.

`event021_parent_reserve_event6_native_footprint` runs on the opening host after the anchor is reserved.
It adds every other footprint state to `global.random_civil_war_plan_states`, `global.random_civil_war_reserved_states` and the plan state count, so the host remnant row, the carrier row and the actor's opening region all use the complete set.
An unsafe footprint raises the host flag `random_civil_war_event6_footprint_blocked`, which makes `random_civil_war_opening_plan_valid` false so the transaction rolls back before any ownership change.
`event021_rollback_opening` clears the flag.

`event021_parent_append_dynamic_event6_front_candidate` records the anchor followed by the other footprint states as one row span.
The active review's remnant proof, the dynamic span validation, the frozen scenario rows and the retained-front refresh therefore see the territory that really changes hands.
A package with an unsafe footprint adds no row.
`event021_parent_find_event6_package` applies the same test while choosing a package, so a blocked package is skipped for the next one.

`event021_parent_prove_event6_footprint_in_ledger` runs at the secondary mutation gate in `event021_parent_try_event6_secondary_front`.
It re-reads the footprint from the current map and requires each member to be eligible and to appear in the frozen ledger: the opening plan's row entries, or the reviewing government's active row entries.
The output `event021_event6_footprint_covered` must be 1 before the release runs; otherwise the front is rejected and the pending row is marked rejected.

`event021_parent_publish_event6_release_footprint` runs on the host after the native release and the anchor handover.
It sets `random_civil_war_event6_opening_state_count` and `global.random_civil_war_event6_pending_opening_state_count` to the number of states the carrier actually owns for a dormant birth, or to one for a living reuse.
`event021_parent_record_event6_actor_footprint` then runs on the carrier and writes those owned states into `random_civil_war_opening_core_states`, with `random_civil_war_opening_state_count` set to their number.

## Side effects and limits

The collector and the proof are read-only.
The reserve helper only edits the plan and reservation arrays and one host flag.
No Event 006 fired state, weight, cap, evolution, league enrollment, country package or tree is touched.
The package territory level follows the number of states the carrier receives (one state is the anchor level, two is compact, three or more is extended), and the release helper and the footprint trigger treat a living dynamic country of an original-tag carrier's original tag (AFX, AGX, AJX, ARX, ASX, HBX) as the existing carrier.
Native release behaviour itself is not modelled by the Python fixtures in `.tools/test_event021_native_release_footprint.py`.

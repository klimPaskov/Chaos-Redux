# Event 006 anchor-first allocator correction handoff

Date: 2026-07-15
Owner: primary implementation agent
Status: source implementation and task-specific static audit complete; live HOI4 scenario execution remains pending

## Corrected contract

The previous package publisher flow could attempt compact or extended territory while each candidate was being selected. That made optional territory from an early candidate capable of consuming a later candidate's required anchor, contrary to the accepted all-anchors-first design.

The corrected transaction is:

1. Select and reserve only each package's dormant tag, reservation group, host protection row, and unique anchor.
2. Reach the exact automatic or scenario candidate count.
3. Rehydrate every frozen package row and run one compact pass across the full selection.
4. Rehydrate every frozen package row and run one extended pass across the full selection.
5. Trim optional territory on collisions or host-survival pressure without dropping the anchored country.
6. Lock only after aligned-array, exact-count, unique-anchor, living-tag, ownership, and host-survival validation.
7. Release in one incident, verify target ownership and control after every additional-state transfer, initialize packages only after every transfer proves, and commit only after initialization succeeds.

Ambition territory remains post-release claims, negotiations, missions, wars, and formable requirements. It is not a fourth automatic release footprint.

## Files and identifiers

- `common/script_constants/006_independence_wave_package_constants.txt`
  - `independence_wave_reservation_phase.anchors`
  - `independence_wave_reservation_phase.compact`
  - `independence_wave_reservation_phase.extended`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
  - `independence_wave_begin_package_reservation`
  - `independence_wave_reserve_candidate_anchor`
  - `independence_wave_try_candidate_compact_state`
  - `independence_wave_try_candidate_extended_state`
  - `independence_wave_expand_selected_packages_for_current_phase`
  - `independence_wave_expand_selected_optional_territory`
- `common/scripted_effects/006_independence_wave_execution_effects.txt`
  - `independence_wave_transfer_frozen_states`
  - `independence_wave_execute_standalone_frozen_plan`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
  - all-ranked SCN-008 allocation and bounded Universal Belligerence target cleanup
- `common/scripted_effects/005_006_liberations_collision_effects.txt`
  - Event 005 anchors, Event 006 anchors, Event 005 compact states, Event 006 compact/extended states, shared lock
  - `soviet_collapse_joint_transfer_frozen_states`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`
  - deterministic per-host protected-state selection, preferring the owned and controlled capital
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` through `006_independence_wave_packages_region_14_effects.txt`
  - automatic selectors contain only readiness-approved automatic/high-chaos packages
- `.tools/audit_event6_allocator.py`
  - source audit for counts, publisher shape, selector membership, reservation phases, ordering, transfer proof, host protection, scenario roster, and belligerence cleanup

## Automatic and scenario pools

- 149 exact package reservation publishers remain available to their owning explicit systems.
- 126 bound rows with `ready_automatic`, `ready_high_chaos`, `ready_if_tag_not_living`, or `ready_unique_state_confirmed` verdicts appear in automatic regional selectors.
- 13 overlay-only rows and 7 `formable_or_route_only` rows were removed from automatic weighted draws without deleting their publishers.
- SCN-008 contains the exact 138 bound, selectable package IDs and excludes all overlay-only rows.
- Automatic counts remain exactly 3, 4, 5, 7, and 10; World Collapse remains 10.

## Verification evidence

`python .tools/audit_event6_allocator.py` passed with:

- publishers: 149;
- automatic/high-chaos selectable packages: 126;
- SCN-008 ranked selectable packages: 138;
- order: all anchors, compact, extended, lock;
- joint order: Event 005 anchors, Event 006 anchors, optional territory, lock.

`.tools/audit_hoi4_country_tags.py` also passed the locked Event 006 architecture against 122 Workshop directories plus local mods with zero incompatible tag collisions. The result at this handoff was 102 safe custom X tags, 91 registered vanilla identities, and 13 overlay-only identities.

## Remaining test and readiness work

- Run live injected collision cases for living tags, stale origins, same reservation groups, duplicate anchors, and Event 005/Event 006 intersections.
- Run one-state, capital-preference, N-1 loss, compact-trim, and extended-trim host-survival cases.
- Inject one failed ownership/controller transfer and confirm package initialization and commit do not run.
- Execute automatic bands at 3, 4, 5, 7, and 10 and every SCN-008 intensity/type combination.
- The allocator cannot satisfy the automatic minimum until at least three packages pass their complete content-readiness contract, and World Collapse cannot satisfy ten until ten packages do. Publisher presence is not readiness.
- At least one ready package with compact and extended rows is required to prove scenario territory-intensity differences on the live map.

No runtime success is claimed by this handoff.

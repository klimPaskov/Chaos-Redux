# Event 006 Transaction Architecture Audit

> Resolution, 2026-07-15: the ownership-transaction blockers recorded below are resolved by `006_transaction_architecture_resolution_2026_07_15.md`. This file is retained as the pre-correction audit record; its current-state verdict and line references are historical.

Date: 2026-07-15

Status: implementation-blocking audit. No gameplay files were edited by this audit.

## Verdict

The current Event 006 allocator has a strong mutation-free reservation phase, and the joint Event 005 plus Event 006 planner correctly shares country, state, anchor, host, and protected-remnant ledgers. It does **not** meet synchronized incident semantics as a complete transaction.

Three independent blockers prevent a completion claim:

1. A failure after `liberation_release_begin_execution` does not compensate ownership, controllers, host capitals, cores, or complete package state. Standalone and joint paths discard scope marks that are required for compensation. The scenario path can instead remain stuck in `executing`.
2. Normal automatic cluster availability rejects Event 006 before the joint planner can run. The joint transaction is currently reachable only through force-cluster dispatch or another caller that manually constructs both firing-order rows.
3. The working-tree package registry is fail-closed. All runtime content attestations are disabled, IW-006 and IW-007 readiness is disabled, and the minimum automatic wave requires three accepted packages. Event 006 therefore cancels before mutation in the current snapshot. This masks the rollback defect rather than resolving it.

The minimum safe implementation must add compensating rollback before any post-mutation ledger cleanup, distinguish cluster-member eligibility from independent automatic-trigger eligibility, and keep the package gates closed until at least the current exact wave count is fully attested.

## Required reference basis

This audit used the required offline and installed references:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, especially regular event targets, scoped variables, and arrays
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, especially `release`, `annex_country`, `set_capital`, `set_state_owner_to`, and `set_state_controller_to`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`

The useful vanilla precedents were:

- `common/decisions/YUG.txt`, which checks fixed-tag existence before release and sets capitals only after ownership is proven
- `common/national_focus/yugoslavia.txt`, which carries a released nation through one regular event-target chain
- `events/WTT_Japan.txt`, which checks ownership and control before releasing Korea
- `events/WTT_border_conflict_events.txt`, which preserves regular event targets across an event chain and applies explicit state transfers

The offline effect reference is decisive on rollback feasibility. `release` removes the releasing owner's cores from transferred states. `set_state_owner_to`, `set_state_controller_to`, and `set_capital` provide the compensating effects needed to restore the frozen ledger. Clausewitz does not provide automatic transactions, but it does permit a scripted compensating transaction.

## Current execution ordering

### Standalone Event 006

The current call order is:

1. `chaosx.nr6.1` in `events/006_independence_wave.txt`
2. `independence_wave_prepare_and_execute_standalone_incident`
3. `liberation_release_begin_plan`
4. `liberation_release_enter_allocation_phase`
5. `independence_wave_allocate_automatic_packages`
6. `independence_wave_expand_selected_optional_territory`
7. `independence_wave_execute_standalone_frozen_plan`
8. `liberation_release_lock_plan`
9. `independence_wave_validate_execution_metadata`
10. `liberation_release_prepare_host_capitals_for_execution`
11. `liberation_release_begin_execution`
12. `independence_wave_instantiate_frozen_countries`
13. `independence_wave_transfer_frozen_states`
14. `independence_wave_initialize_frozen_countries`
15. `independence_wave_commit_wave_history`
16. `liberation_release_commit_plan`

The failure branch at `common/scripted_effects/006_independence_wave_execution_effects.txt:538` through `:547` sets `independence_wave_standalone_incident_failed_after_mutation`, changes the phase to `aborted`, clears `liberation_release_plan_valid`, and calls `liberation_release_clear_plan_scope_marks`. It does not restore ownership, controllers, cores, capitals, or all package effects.

### Joint Event 005 plus Event 006

The current joint order is:

1. `event_cluster_prepare_runtime_context` in `common/scripted_effects/chaosx_event_cluster_effects.txt`
2. `liberations_joint_prepare_and_execute_incident`
3. Shared plan begin and allocation phase
4. `SOV = { soviet_collapse_joint_allocate_opening_republics = yes }`
5. `independence_wave_allocate_automatic_packages`
6. Event 005 compact expansion, then Event 006 compact and extended expansion
7. One shared `liberation_release_lock_plan`
8. Event 005 metadata validation, then Event 006 metadata validation
9. Shared host-capital preparation and one `liberation_release_begin_execution`
10. `SOV = { soviet_collapse_initialize_crisis_values = yes }`
11. Instantiate every frozen Event 005 country
12. Instantiate every frozen Event 006 country
13. Transfer every Event 005 state
14. Transfer every Event 006 state
15. Initialize every Event 005 country
16. Initialize and validate every Event 006 country
17. Commit Event 006 durable history
18. Commit the shared plan and set both presentation-pending flags
19. Only after commit, queue the two cluster member events

This ordering correctly makes presentation order irrelevant to ownership. Entry events consume the committed presentation flags and do not execute the release a second time.

The failure branch is not atomic. `liberations_joint_record_failure_after_ownership_mutation` at `common/scripted_effects/005_006_liberations_collision_effects.txt:1213` through `:1218` marks the incident failed, sets the plan to `aborted`, and destroys scope marks. It is called from `:1362` through `:1368`. No compensation occurs.

### Triggerable scenario

`independence_wave_trigger_scenario` calls the same `independence_wave_execute_standalone_frozen_plan`. Its failure cleanup at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1240` through `:1251` is gated to a pre-execution plan. A failure after `liberation_release_execution_started` therefore leaves the mutated world and can leave `global.liberation_plan_phase = executing`, blocking later plans.

## Requirement matrix

| Requirement | Current result | Evidence and qualification |
| --- | --- | --- |
| Reserve every tag and state before release | Meets reservation semantics | Both event contributions publish into `global.liberation_plan_*` arrays before `liberation_release_lock_plan`. No allocator effect changes ownership. |
| Unique anchors | Meets | `liberation_release_add_state_reservation`, duplicate validation, reservation groups, and the exact one-anchor-per-country validation prevent shared anchors. |
| Keep one host state, preferably the capital | Partial | Host loss checks preserve one owned state and a protected-state row. The selector prefers an owned and controlled capital, but it can reserve the mandatory anchor itself and then reject a viable package. It also prefers an uncontrolled core before an owned and controlled non-core state. |
| Trim optional territory before dropping a candidate | Meets | Event 006 records compact and extended failures through `independence_wave_record_optional_state_trim`. Event 005 records optional core failures through `soviet_collapse_joint_record_optional_state_trim`. |
| Reroll living or invalid candidates | Meets planner semantics | Event 006 recomputes all weights after each failure and marks the rejected tag with `independence_wave_last_rejected_plan_id`. Event 005 rebuilds its family pool without rejected or living tags. Exact count remains fail-closed. |
| Execute one synchronized incident | Partial | Reservation, lock, ownership mutation, and initialization occur in one effect chain. Post-mutation failure can leave only part of that incident in the world, so the full atomic semantic is not met. |
| Roll back ownership, capitals, and package state after failed verification | Does not meet | There is no post-execution ownership rollback. Event 006 cleanup is incomplete for package effects. Event 005 has no transaction rollback adapter. |
| Event 005 plus Event 006 collision safety | Meets before mutation, fails after mutation | Both events reserve through one coordinator and Event 006 rerolls against Event 005. A later failure can leave both contributions partially active and can destroy the shared recovery ledger. |
| No world periodic scan | Meets for collision handling | No Event 006, joint collision, or shared coordinator effect adds a collision-specific `on_daily`, `on_weekly`, or `on_monthly` scan. Allocation uses fixed package dispatch and bounded plan arrays. Scoped `every_core_state` and `every_owned_state` calls are limited to selected tags or hosts. The existing automatic-event timer is an all-country `on_daily` framework, but joint logic runs only after that framework selects the Liberations cluster. |

## Minimum blocker set

### P0. Post-mutation failure destroys or strands the recovery ledger

Affected identifiers:

- `independence_wave_prepare_and_execute_standalone_incident`
- `liberations_joint_record_failure_after_ownership_mutation`
- `liberations_joint_prepare_and_execute_incident`
- `independence_wave_trigger_scenario`
- `liberation_release_abort_plan`
- `liberation_release_clear_plan_scope_marks`

The state rows already store `liberation_release_original_owner` and `liberation_release_original_controller`. The host rows already store `global.liberation_plan_host_original_capitals`. The failure paths clear the state variables before using them.

`can_liberation_release_reset_plan` treats `aborted` as resettable. A later `liberation_release_begin_plan` can therefore clear all arrays and remove the last forensic description of a partially mutated incident. The scenario has the opposite failure mode because it can remain in `executing` forever.

Required correction:

- Never call `liberation_release_clear_plan_scope_marks`, `liberation_release_clear_plan_arrays`, or an event contribution clearer until a rollback verification succeeds.
- Make `liberation_release_abort_plan` pre-execution only. If `liberation_release_execution_started` is present, it must route to rollback or refuse to clear anything.
- Introduce `liberation_plan_phase.rolling_back` and `liberation_plan_phase.rollback_failed` in `common/script_constants/chaosx_liberation_release_constants.txt`.
- Keep `rollback_failed` out of `can_liberation_release_reset_plan`.
- A failed rollback must retain every array, state variable, host row, package row, and failure reason. It must not permit another release plan.

### P0. Core changes are not in the shared recovery ledger

`release` removes the original host's core from every transferred state. Event 006 also adds planned target cores before release. The temporary arrays `global.independence_wave_execution_added_plan_cores` and `global.independence_wave_execution_masked_core_states` are cleared after each target and cannot support incident rollback.

Required correction in `liberation_release_add_state_reservation`:

- Store a state flag such as `liberation_release_original_owner_had_core` when the original owner is a core owner.
- Store a state flag such as `liberation_release_target_had_core` when the frozen target already has a core.
- Clear these flags only in verified commit or verified rollback cleanup.
- On rollback, remove the target core only when it was transaction-added.
- On rollback, restore the original owner's core when it existed before release.

State flags are sufficient and avoid another aligned array. They remain plan-scoped because the state already carries `liberation_release_plan_id`.

### P0. Package rollback is incomplete for Event 006 and absent for Event 005

Event 006 calls `independence_wave_cleanup_uncommitted_frozen_country_origins`, which calls `independence_wave_reset_current_generation`. That clears many variables, flags, registries, decisions, missions, and ideas. It does not establish exact reversal of every setup effect such as loaded focus trees, politics, leaders, starting manpower, stockpiles, templates, or spawned units.

Event 005 calls `soviet_collapse_setup_breakaway_country`. That effect changes active-origin state, global and Soviet breakaway arrays and counters, pressure values, manpower, equipment, ideas, templates, divisions, focus-tree state, leaders, and presentation scheduling. It can schedule `chaosx.nr5.47` and emit `chaosx.nr5.95` before the shared plan commits. `soviet_collapse_cleanup_resolved_breakaway_target` is campaign-resolution cleanup, not a transaction inverse.

The smallest safe design is to split package work into reversible prepare and irreversible finalize stages:

1. Release and transfer the exact footprint.
2. Verify the whole ownership footprint before broad package setup.
3. Apply only reversible package preparation.
4. Validate all prepared packages.
5. If validation fails, roll back prepared package state, cores, ownership, controllers, and capitals.
6. Once every failure-producing check has passed, run deterministic durable finalizers and commit without another cancellation branch.

Any package effect that must run before final verification needs an exact inverse and an exact rollback-validation trigger. Delayed events and news cannot be unscheduled, so they must move to the post-verification finalizer or carry a committed plan-ID gate when they fire.

Required event-specific adapters:

- `independence_wave_rollback_uncommitted_frozen_country_origins`
- `independence_wave_validate_rollback_cleanup`
- `soviet_collapse_joint_rollback_uncommitted_frozen_countries`
- `soviet_collapse_joint_validate_rollback_cleanup`

The Event 006 dispatcher also needs package-specific rollback and rollback-validation dispatch for every ID admitted by `has_independence_wave_runtime_package_adapter_for_execution_id`. A generic flag cleaner is not proof that starting forces or identity state were reversed.

The joint initializer also has an avoidable cross-event partial-commit seam. `independence_wave_initialize_frozen_countries` runs immediately after `soviet_collapse_joint_initialize_frozen_countries` without first proving that `soviet_collapse_joint_execution_initialized_count` equals `global.soviet_collapse_joint_plan_selected_count`. Event 006 can therefore begin durable origin commits after an incomplete Event 005 initialization. Gate each Event 006 mutation stage on the exact preceding Event 005 count:

- Event 006 instantiation only after the Event 005 instantiation count is exact.
- Event 006 transfer only after the Event 005 transfer count and failure value are exact.
- Event 006 initialization only after the Event 005 initialized count is exact.

These gates reduce the damage surface but do not replace rollback.

### P0. Normal cluster selection cannot select Event 006

The normal path is:

1. `event_cluster_member_check_availability` at `common/scripted_effects/chaosx_event_cluster_effects.txt:547`
2. `evaluate_random_event_selection_candidate` at `common/scripted_effects/chaosx_settings_effects.txt:4348`
3. `evaluate_random_event_active_pool_candidate` at `common/scripted_effects/chaosx_logic_effects.txt:509`

`evaluate_random_event_active_pool_candidate` unconditionally invalidates `event_id = 6` at line 565. In the Liberations cluster, Event 006 and Event 005 begin as optional members. The automatic trigger member is promoted to required, but the other member still runs the active-pool check. When Event 005 triggers the cluster, Event 006 becomes `skipped_unavailable`. `liberations_joint_cluster_selected_both_members` is false, so `liberations_joint_prepare_and_execute_incident` is not called.

Force-cluster dispatch bypasses availability and can reach the joint path. That is not ordinary event reachability.

Required correction:

- Preserve the distinction between independent automatic-trigger eligibility and cluster-member eligibility.
- Set a temporary cluster-member evaluation context around the generic availability call in `event_cluster_member_check_availability`.
- In `evaluate_random_event_active_pool_candidate`, keep Event 006 excluded as an independent automatic trigger, but exempt that exclusion while the cluster-member context is active and a dedicated Event 006 cluster-member readiness proof passes.
- The readiness proof must remain false while runtime content attestations are closed and must demonstrate capacity for the current exact wave target, not merely one candidate.
- Do not simply delete the Event 006 exclusion. That would turn Event 006 into an independent automatic trigger and would allow repeated cancellation with an undersized pool.

This context-specific change is smaller and safer than changing the top-level event pool. Standalone Event 006 remains available to explicit callers without silently changing its random-event policy.

### P0. The package pool cannot satisfy the exact wave in the current snapshot

Current working-tree gates:

- `has_independence_wave_runtime_package_content_attestation_for_execution_id` is `always = no` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- `is_independence_wave_scenario_package_preflight_ready` is `always = no` in the same file.
- `is_independence_wave_ready_package_iw_006_tag_available` and `is_independence_wave_ready_package_iw_007_tag_available` are `always = no` in `common/scripted_triggers/006_independence_wave_package_triggers.txt`.
- `independence_wave_count.calm_world = 3` in `common/script_constants/006_independence_wave_constants.txt`.

Event 006 therefore has zero executable packages at this snapshot and requires at least three even at the calm-world setting. The transaction path is latent. Re-enabling one or two package attestations still cannot satisfy the minimum exact count.

### P1. Host protection can consume the mandatory anchor

`liberation_release_select_and_reserve_host_state` does not exclude the current mandatory anchor. Event 006 already supplies `liberation_candidate_anchor` before calling it from `independence_wave_begin_package_reservation`. If the fixed anchor is the host's current capital, the coordinator protects that state. `liberation_release_add_country_reservation` then rejects the same state because it is protected. A host with another viable remnant can lose an otherwise valid candidate.

Event 005 selects its protected host state before selecting its random mandatory anchor. A one-core candidate can be rejected even when the host owns a safe non-core remnant.

Required correction:

- Every host-state candidate branch must exclude `event_target:liberation_candidate_anchor`.
- Reorder `soviet_collapse_joint_reserve_current_candidate` to select and freeze its anchor before `liberation_release_select_and_reserve_host_state`.
- An existing protected state equal to a later required anchor must reject that host or select another valid Event 005 anchor. It must never silently protect and release the same state.
- Host-remnant priority should be existing valid protection, owned and controlled capital, owned and controlled core, owned and controlled non-core state, owned uncontrolled core, then any owned state.

### P1. A failed pre-execution capital restore is treated as a successful cancellation

`liberations_joint_cancel_before_ownership_mutation` calls `liberation_release_restore_host_capitals_before_execution`, then clears both contributions and aborts regardless of `liberation_release_capital_restore_failed`. If a restore fails, the original-capital ledger is discarded and the incident is still consumed as an atomic cancellation.

Required correction:

- Verify that `liberation_release_capital_restore_failed` is absent before contribution or shared-ledger cleanup.
- On restore failure, retain the host arrays and scope marks in a non-resettable failure phase.
- Do not report the cancellation as atomic until every host capital matches its original row.

### P2. Non-joint Event 005 release seams should reject shared reservations defensively

Ordinary transactions do not interleave, so these paths do not create the present joint collision. They remain unsafe under nested or later reusable callers:

- The direct Kazakhstan release around `common/scripted_effects/005_soviet_collapse_effects.txt:26221` rechecks only `KAZ = { exists = no }`. Its gate lacks a shared reserved-country and Event 006-origin check.
- `soviet_collapse_release_scope_from_soviet_collapse_owner` proves at least one unreserved core, then uses raw `release`, which can transfer every host-owned target core. A reserved or protected target core would need masking before that release.

Add live reserved-country, active-origin, reserved-state, and protected-state checks to those release seams. This is defense in depth after the P0 transaction work.

## Smallest safe shared patch

The following is the minimum implementation-grade shared patch. It is still incomplete until both event-specific package rollback adapters attest success.

### 1. Extend lifecycle and rollback diagnostics

File: `common/script_constants/chaosx_liberation_release_constants.txt`

Add:

- `liberation_plan_phase.rolling_back`
- `liberation_plan_phase.rollback_failed`
- A small rollback failure enum covering state scope, owner restore, controller restore, core restore, host capital restore, country de-instantiation, Event 005 package cleanup, and Event 006 package cleanup

File: `common/scripted_triggers/chaosx_liberation_release_triggers.txt`

Add:

- `is_liberation_release_plan_rolling_back`
- `liberation_release_rollback_ledger_is_valid`
- `liberation_release_rollback_matches_frozen_ledger`

`liberation_release_rollback_matches_frozen_ledger` must verify, through the frozen arrays only:

- Every reserved state has its original owner and original controller.
- Every original owner core fact and target core fact matches its snapshot.
- Every host owns its protected state.
- Every host capital equals its original-capital row.
- Every transaction-created target is absent after losing its complete exact footprint.
- Event 005 and Event 006 rollback-validation flags are both present when their participant flags were in the plan.

### 2. Add compensating effects without clearing the ledger

File: `common/scripted_effects/chaosx_liberation_release_effects.txt`

Add these shared effects or equivalent narrowly named effects:

- `liberation_release_begin_plan_rollback`
- `liberation_release_restore_reserved_state_core_facts`
- `liberation_release_restore_reserved_state_ownership`
- `liberation_release_restore_host_capitals_after_execution`
- `liberation_release_validate_plan_rollback`
- `liberation_release_finish_verified_plan_rollback`
- `liberation_release_mark_plan_rollback_failed`

Required order:

1. Set phase to `rolling_back` and retain `liberation_release_execution_started`.
2. Roll back Event 006 package preparation while its countries still exist.
3. Roll back Event 005 package preparation while its countries still exist.
4. Restore target and original-owner core facts.
5. Restore each reserved state's owner and controller from its state variables.
6. Restore every original host capital from the aligned host ledger.
7. Verify countries, states, controllers, cores, capitals, and package cleanup.
8. Only on exact success, clear event contributions, scope marks, arrays, and `liberation_release_execution_started`, then set phase to `aborted`.
9. On any mismatch, set phase to `rollback_failed` and preserve the complete ledger.

The ownership restore can safely iterate `global.liberation_plan_states`. This is bounded by the frozen incident and does not scan the world.

### 3. Route every post-mutation failure through the shared rollback

Files and replacements:

- In `common/scripted_effects/006_independence_wave_execution_effects.txt`, replace the post-mutation branch in `independence_wave_prepare_and_execute_standalone_incident` with the Event 006 package rollback adapter followed by shared rollback.
- In `common/scripted_effects/005_006_liberations_collision_effects.txt`, replace `liberations_joint_record_failure_after_ownership_mutation` with `liberations_joint_rollback_after_ownership_mutation`.
- In `common/scripted_effects/006_independence_wave_scenario_effects.txt`, route a post-execution failure through the same Event 006 rollback path. Do not leave the phase executing.
- Guard `liberation_release_abort_plan` so it cannot clear an executing plan.

### 4. Close the package-state gap

Files:

- `common/scripted_effects/006_independence_wave_execution_effects.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- Each Event 006 package effect file admitted by the runtime adapter registry
- `common/scripted_effects/005_006_liberations_collision_effects.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

Implementation constraints:

- Defer news, delayed events, durable history arrays, presentation flags, and other non-cancellable effects until every post-release verification has passed.
- Record exact package deltas if manpower, equipment, units, global counters, Soviet pressure, ideas, leaders, politics, or focus state must be applied before final verification.
- Mark transaction-created divisions at creation or defer their creation. A rollback cannot safely identify them later without a ledger.
- Package rollback validation must prove the cleanup, not merely call a cleanup effect.

### 5. Restore normal joint reachability without changing independent trigger policy

Files:

- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- Package readiness and runtime attestation triggers

Add a temporary cluster-member context around the generic member availability evaluator. Keep the raw Event 006 exclusion for independent random selection, but condition it so Event 006 can pass inside that context when a dedicated readiness trigger proves the exact current capacity. Once that proof is true, ordinary cluster member availability can select both Event 005 and Event 006 and reach the synchronized planner.

## Required verification scenarios

All scenarios must inspect exact frozen rows and event-specific registries. A load-only check is insufficient.

1. Event 006 allocation finds fewer than the exact target. No capital, core, owner, controller, package, history, or presentation state changes.
2. A living target tag has nonzero weight due to a deliberate test injection. The candidate is rejected, marked for the current plan, and the allocator rerolls without reducing the target count.
3. Two candidates request the same anchor. Only one is reserved and the other rerolls.
4. A mandatory anchor is the host capital while the host owns another safe state. The other state is protected and the package remains viable.
5. A host has exactly one owned state. Its candidate is rejected.
6. Optional compact and extended states exceed host capacity. Optional rows are trimmed before the candidate is rejected.
7. Inject failure after the first country release but before all tags instantiate. Every state, controller, core, capital, and target existence fact returns to the pre-plan ledger.
8. Inject failure after all state transfers but before Event 006 package activation. The same exact rollback succeeds.
9. Inject failure after one Event 006 package prepares and before all packages validate. Package state and ownership both roll back.
10. Inject failure after one Event 005 breakaway setup prepares and before joint validation. Soviet globals, global arrays, country package state, ownership, and capitals all roll back. No delayed report survives.
11. Force a rollback mismatch. The phase becomes `rollback_failed`, the ledger remains intact, and a new release plan cannot begin.
12. Fire the ordinary Liberations cluster with Event 005 as trigger after cluster-member Event 006 readiness is enabled. Both firing-order members are present, the joint transaction runs once, and later member events only present committed results. Also prove that Event 006 remains excluded as an independent random trigger.
13. Fire the triggerable scenario and inject a post-release failure. The scenario records failure after successful rollback and does not remain in `executing`.
14. Verify no new `on_daily`, `on_weekly`, or `on_monthly` hook and no `every_country` or `every_state` transaction scan was added.

## Documentation that becomes stale after the correction

These current statements explicitly endorse non-rollbackable ownership and must be revised with the implementation:

- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_joint_event5_event6_collision_implementation_handoff.md`

The earlier handoff states that Clausewitz cannot roll back ownership after the first release. The correct limitation is narrower: Clausewitz has no automatic transaction primitive. The frozen owner, controller, core, and capital ledger can still drive explicit compensating effects.

## Completion status

The synchronized transaction is incomplete. The reservation and pre-mutation collision design is usable, but rollback, ordinary joint reachability, and executable package capacity are unresolved. No simplification or fallback was accepted in this audit.

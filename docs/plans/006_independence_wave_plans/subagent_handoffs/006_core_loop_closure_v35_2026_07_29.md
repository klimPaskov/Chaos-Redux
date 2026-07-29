# Event 006 Core-Loop Closure v35 Handoff

Date: 2026-07-29

Scope: Event 006 automatic and World Collapse allocation, frozen-plan execution, and the Event 005/Event 006 joint transaction boundary.

Ownership: This handoff covers only the allocator and transaction surfaces assigned by the parent; package-specific content, collections, registry files, decisions, localisation, assets, spreadsheets, focus files, and Random Events were not changed.

## Outcome

The source audit found three identical prevalidation inversions that rejected every valid instantiated reserved country before ownership execution.

The checks used `NOT = { event_target:... = { exists = no ... } }`, which makes an existing reserved target fail the outer validation and records `invalid_scope`.

All three checks now require `exists = yes` inside the positive readiness block, so an existing target with the required reservation and metadata passes while an absent target still fails.

## Files changed

- `common/scripted_effects/006_independence_wave_execution_effects.txt` at `independence_wave_validate_execution_metadata` for the ordinary Event 006 country target and the breakaway sponsorship country target.
- `common/scripted_effects/005_006_liberations_collision_effects.txt` at `soviet_collapse_joint_validate_execution_metadata` for the Event 005 side of a joint plan.
- No new helper, script constant, scripted trigger, event target, localisation key, asset, or package publisher was added.

The parent also updated `.tools/audit_event6_allocator.py` with regression assertions for all three positive existence checks; that parent-owned update is visible in the shared workspace and was not authored in this subtask.

## Core helper map and call-site proof

No new helper extraction was needed because the existing coordinator and Event 006 planner already provide the required interfaces.

| Helper | Scope and inputs | Outputs and side effects | Core call sites |
| --- | --- | --- | --- |
| `independence_wave_capture_wave_tuning` | Country/root scope; reads the current chaos band and shared constants. | Publishes count, territory, force, depth, and target-count tuning for the current wave. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:19`; called by standalone and joint wrappers. |
| `independence_wave_begin_plan_contribution` | Country/root scope; requires the shared plan to be in allocation. | Clears Event 006 selected arrays, counters, trim arrays, sponsorship arrays, and contribution flags while preserving the shared plan id. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:61`; automatic allocator and joint dispatcher. |
| `independence_wave_begin_package_reservation` plus `independence_wave_reserve_candidate_anchor` | Country and state scopes; consume package metadata and the candidate country, anchor, and host event targets. | Reserves the host remnant, one anchor, package row, owner, force, and plan metadata; optional state passes are phase-gated. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95` and `:293`; package publishers. |
| `liberation_release_select_and_reserve_host_state` plus `liberation_release_add_country_reservation` | Country scope; consume candidate host, country, anchor, package id, and reservation group. | Selects host protection with capital preference, enforces host-loss capacity, dormant-tag eligibility, unique tags, reserved anchors, and unique reservation groups. | `common/scripted_effects/chaosx_liberation_release_effects.txt:247` and `:444`; Event 006 planner and Event 005 joint reservation. |
| `independence_wave_expand_selected_optional_territory` and its compact/extended helpers | Country/state scopes; operate only after every anchor row is frozen. | Attempts compact then extended states, records trims and rejection reasons, and leaves an exact aligned plan or fails the contribution. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:319`, `:350`, `:382`, and `:445`; standalone and joint wrappers. |
| `independence_wave_validate_execution_metadata` | Root scope after the shared plan is locked; reads frozen country, anchor, host, package, and sponsorship arrays. | Sets `independence_wave_execution_metadata_valid` only when all live target, reservation, adapter, sponsorship, and ownership metadata checks pass. | `common/scripted_effects/006_independence_wave_execution_effects.txt:15`; standalone and joint dispatchers. |
| `independence_wave_prepare_finalizer_frozen_country_origins` and `independence_wave_finalize_frozen_country_origins` | Root/finalizing scope; consume frozen rows after ownership transfer. | Runs setup, activation, final validation, durable origin commit, evolution opening, and pending-row cleanup only after every selected row passes. | `common/scripted_effects/006_independence_wave_execution_effects.txt:420` and `:441`; standalone and joint transaction chains. |
| `liberations_joint_prepare_and_execute_incident` | Root cluster scope; requires both Event 005 and Event 006 contributions. | Orders Event 005 anchors, Event 006 anchors, optional territory, lock, synchronized metadata validation, ownership mutation, finalization, commit, and rollback paths. | `common/scripted_effects/005_006_liberations_collision_effects.txt:1237`. |
| `independence_wave_reset_current_generation` and `independence_wave_clear_plan_contribution` | Country and root scopes; called on failed preparation or failed plan contribution. | Clears generation-local flags, variables, package runtime state, pending rows, reservation arrays, and temporary plan marks without erasing historical ledgers. | `common/scripted_effects/006_independence_wave_effects.txt:383`; `common/scripted_effects/006_independence_wave_package_planner_effects.txt:963`. |

## End-to-end source proof

- Band selection and automatic ladder are centralized in `independence_wave_capture_wave_tuning`, with counts 6, 8, 10, 14, and 20 and World Collapse fixed at 20 in `common/script_constants/006_independence_wave_constants.txt`.
- Automatic allocation recomputes regional weights, chooses a weighted region, rerolls rejected candidates through a bounded loop, and refuses ownership mutation unless the exact target count and aligned arrays are frozen in `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:47` and `:79`.
- Dormant-tag, living-tag, Soviet-origin, prior-plan rejection, anchor availability, and aligned-array checks are explicit in `common/scripted_triggers/006_independence_wave_package_triggers.txt:9`, `:23`, and `:178`.
- Host survival is reserved before country reservation, and the shared selector prefers an existing protected row, an owned and controlled capital, then progressively weaker owned-state candidates in `common/scripted_effects/chaosx_liberation_release_effects.txt:247`.
- Reservation groups and exact package uniqueness are enforced by the shared add-country helper, including the explicitly attested IW-008/IW-010 Rhineland/Saar pair exception at `common/scripted_effects/chaosx_liberation_release_effects.txt:444`.
- Event 005 joint allocation fills its anchor families first at `common/scripted_effects/005_006_liberations_collision_effects.txt:639`, then runs optional compact expansion at `:775`; the joint wrapper calls Event 005 allocation before Event 006 allocation and optional expansion before `liberation_release_lock_plan` at `:1237`.
- Standalone Event 006 locks and validates before preparing host capitals, begins execution only after validation, transfers every frozen state, enters finalization only after ownership matches, and commits only after every country initializes at `common/scripted_effects/006_independence_wave_execution_effects.txt:484` through `:542`.
- Joint execution performs the same lock and both metadata validations before the shared execution barrier at `common/scripted_effects/005_006_liberations_collision_effects.txt:1298` through `:1382`.
- Pre-mutation failures restore capitals, clear the Event 006 contribution, and abort the shared plan; post-barrier failures call compensating rollback, and finalization failures preserve the failure state for the transaction wrapper at `common/scripted_effects/006_independence_wave_execution_effects.txt:647` through `:677` and `common/scripted_effects/005_006_liberations_collision_effects.txt:1207` through `:1229`.
- Previous-wave package, region, and host memory is copied before the shared plan is cleared at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:831`, preventing immediate repeat selection while preserving historical ledgers.
- `events/006_independence_wave.txt:7` is the canonical repeatable entry; its immediate block delegates standalone execution to the frozen planner, while `chaosx.nr6.3` at `:72` consumes a queued crisis request, retries only through the bounded timing ladder, and delegates to the same standalone planner after `can_independence_wave_crisis_release_barrier` passes.
- The generic automatic-event timer calls `select_weighted_random_event_id` and `fire_event_by_temp_id` in `common/on_actions/chaosx_on_actions_system.txt:153` through `:166`, and Event 006 availability is gated through the Liberation cluster capacity trigger rather than a second direct world iteration.

## Constants and tuning plan

No new constants are required for this closure.

The existing shared tuning remains the source of truth for counts, chaos bands, reservation phases, loop increments, rejection reasons, owner enums, retry limits, and World Collapse behavior.

The allocator audit confirms the expected automatic counts, scenario intensity mappings, scenario type mappings, package attestation count, reservation-group compatibility, and Event 005/Event 006 ordering.

## Event-target and cleanup plan

- Regular event targets carry the current candidate country, anchor, former host, sponsorship state, sponsorship sponsor, and execution state through the frozen execution passes.
- The shared coordinator marks every reserved state, host, and country with the current plan id and clears those marks through `liberation_release_abort_plan`, `liberation_release_commit_plan`, or compensating rollback.
- Event 006 generation reset clears only generation-local registries, package runtime mappings, flags, variables, and relationship rows; committed historical generation and former-host ledgers remain intact.
- Crisis queue cleanup clears the queued flag, requester flag, retry variable, cooldown/runtime flags, and success or blocked receipt through the existing Event 006 crisis helpers.

## Migration plan

No duplicated logic was migrated in this subtask.

The existing package publishers continue to call the shared reservation and dispatch helpers, while the corrected validation predicates now admit the already-reserved live targets those publishers create.

## Validation

- `python .tools/audit_event6_allocator.py` passed after the source fixes and the parent-owned three-target regression assertions.
- The audit reports 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 12 attested packages, 11 compatible reservation groups, the IW-008/IW-010 capacity witness, automatic counts 6/8/10/14/20, and the joint order Event 005 anchors then Event 006 anchors then optional territory then lock.
- A read-only `hoi4_event_inspect` scan of `chaosx.nr6.1` completed with status `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, graph revision `867986734b88b7aa4434378e9224f3579a21b441df9901c50b3b42e5629b7e0b`, and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20a65ca26ac069a9a4e5df10507001c95f8bbbe025eace5a2a9b230a325a9ab7/64f77aab950abcc6f8bc3b78eb2a4a8d58f6ec6a6d37b7efcc990d4ea636fff7/event-scan-867986734b88.json`.
- The two touched script files retain balanced Clausewitz braces, and a path-scoped `git diff --check` reported no whitespace errors for these changes.
- No in-game or live-save validation was run because the parent explicitly approved authoritative static and MCP evidence instead.

## Unsupported analysis and remaining blockers

- The Event Chain Viewer intentionally returned a large-workspace partial projection with 7,347 unresolved helper references and 2,020 global `EVENT_OPTION_DANGLING` warnings; it reported zero blocking diagnostics, and those workspace-wide parser limitations are not treated as Event 006 core-loop failures.
- The probability inspector can list adapters, but a direct `random_list` projection against the Event 006 planner returned `PROBABILITY_SURFACE_EMPTY`; the source-level random-list and bounded-loop proof is therefore authoritative for this task.
- No package-specific content was audited or changed, so package roster, character, art, localisation, and downstream decision behavior remain outside this handoff.
- No simplification or fallback was introduced by this patch.

## Parent follow-up

The parent can keep the three regression assertions in `.tools/audit_event6_allocator.py` as a permanent guard against reintroducing the inverted existence predicates.

No commit was created, per the parent instruction.

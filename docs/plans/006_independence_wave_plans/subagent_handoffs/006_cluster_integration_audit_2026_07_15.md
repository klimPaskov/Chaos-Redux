# Event 006 cluster integration audit handoff

Date: 2026-07-15

Scope: ordinary automatic availability, Liberations cluster membership, wave-count bands, and the Event 005/Event 006 joint reservation barrier. This handoff does not certify the broader Event 006 country-package implementation.

## Corrections applied

- `common/script_constants/event_cluster_constants.txt`
  - Changed `event_cluster_member_participation.independence_wave` from `0` to `35`, matching the accepted Low participation direction. The triggering member is still promoted to Required/100 by `prepare_event_cluster_firing`; this value governs Event 006 when Event 005 is the selected Liberations member.
- `common/scripted_effects/chaosx_logic_effects.txt`
  - Updated `evaluate_random_event_active_pool_candidate` to inject the Liberations/Event-006 member-availability context when Event 006 is evaluated directly by the ordinary weighted pool, then restore the prior cluster/member values. Existing nested cluster-member evaluation keeps its caller-provided context.
- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - Clarified that the capacity proof is shared by direct ordinary-pool and cluster-member evaluation. The fail-closed Liberations/member/context guards remain intact.

These gameplay files already contained unrelated uncommitted work. The changes above are intentionally limited to the named identifiers.

## Confirmed integration

- Event 006 is registered only in `global.repeatable_events`, so its system classification is Minor Repeatable.
- Event 006 is included in the default-enabled allowlist through `constant:independence_wave_evolution.event_id`, whose value is `6`.
- `event_belongs_to_cluster` maps Events 005 and 006 to `constant:event_cluster_id.liberations` (`2`), and `load_event_cluster_members` registers both members.
- The tuning constants and both runtime band-capture paths resolve to exactly `3 / 4 / 5 / 7 / 10`; World Collapse remains `10`.
- The automatic path is connected: weighted candidate selection -> `fire_event_by_temp_id` -> `try_fire_event_cluster_for_selected_event`; if the cluster roll does not dispatch, `fire_event_by_temp_id_no_cluster` dynamically fires `chaosx.nr6.1`.
- The joint path is reservation-first. `liberations_joint_prepare_and_execute_incident` begins one shared plan, lets Event 005 allocate first, lets Event 006 reroll against the frozen footprint, expands optional territory, locks and validates the aligned ledger, prepares protected host capitals, and only then calls `liberation_release_begin_execution`. Country/tag, unique-anchor, state, reservation-group, host, and protected-host-state facts are stored in the shared release arrays before either origin is instantiated or any state is transferred.

## Blocking readiness gap

The ordinary-selection context defect is corrected, but Event 006 still cannot become an active automatic candidate with the current fail-closed package registry:

- 149 `independence_wave_reserve_package_iw_*` planner publishers exist.
- `has_independence_wave_runtime_package_adapter_for_execution_id` admits only six execution IDs: IW-001, IW-002, IW-006, IW-007, IW-008, and IW-009.
- `has_independence_wave_runtime_package_content_attestation_for_execution_id` currently admits only independently certified `IW-009` Bavaria.
- Every one of the six capacity-witness readiness wrappers calls `is_independence_wave_runtime_package_preflight_ready`, which requires both the execution adapter and content attestation gates.

Consequently the current readiness-backed witness proves at most one candidate, fewer than even the calm-world target of three. Expanding the witness to 7/10 without first completing and registering package execution/content attestations would invent readiness and weaken the accepted fail-closed contract. Once at least ten genuinely audited execution adapters are registered and attested, the six-row capacity witness must be replaced with a complete disjoint-candidate witness covering those ready adapters (or a shared registry-driven equivalent) while preserving tag, anchor, reservation-group, Event-005 footprint, and host-survival checks.

## Focused validation evidence

- Registry scan: 149 reserve publishers and 149 `can_plan_independence_wave_package_iw_*` triggers are present, but only six execution IDs are admitted and only `IW-009` is content-attested.
- Direct availability evaluation now supplies all four values required by `is_independence_wave_liberations_cluster_member_capacity_available`: context, Liberations cluster ID, Event-006 member ID, and Event ID.
- Joint sequencing inspection confirms plan begin/allocation precedes lock, lock precedes execution, and execution precedes country instantiation/state transfer.
- No commit was created.

## Remaining risks

- Automatic Event 006 firing remains blocked until real package content attestations and sufficient execution adapters exist.
- The cluster member danger row is still Low, while the accepted catalog handoff retains player-facing Member Severity Medium. This audit did not change presentation severity because participation and displayed danger are separate fields.

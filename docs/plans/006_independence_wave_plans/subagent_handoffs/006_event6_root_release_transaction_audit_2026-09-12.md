# Event 006 root-to-release transaction audit

Date: 2026-09-12.
Disposition: implemented narrow allocator contract repair, with release-runtime diagnosis unresolved.
Acceptance basis: the parent explicitly required the exact 3/4/5/7/10 ladder and instructed removal of the proven exhausted-pool count rewrite during this audit.
The current parent direction resolves the older Part 1 shortfall wording for this bounded change, without authorizing any country admission, substitute roster, or other design expansion.

## Outcome and changed files

- `common/scripted_effects/006_independence_wave_effects.txt:3638`: removed the automatic, exhausted, nonempty-pool branch that rewrote `global.independence_wave_plan_target_count` and `global.liberation_plan_expected_country_count` to the selected count.
- `common/scripted_effects/006_independence_wave_effects.md:3`: documented `independence_wave_allocate_automatic_packages`, its callers, exact-count outcome, inputs, side effects, and cancellation ownership.
- `.tools/audit_event6_allocator.py:542`: added regression assertions forbidding those count writers inside the automatic allocator and requiring the existing insufficient-pool outcome.
- This handoff records the audit and evidence boundary.

An incomplete automatic selection retains its original target and expected count, sets `independence_wave_plan_exact_count_failed`, records `liberation_plan_reject_reason.insufficient_pool`, and leaves `independence_wave_plan_contribution_ready` unset.
The existing standalone caller stages diagnostic counts, clears the reserved contribution, and aborts before execution.
No helper, constant, target, roster, package, decision, pressure, queue, cost, debug line, or public surface was added.
No gameplay simplification or fallback was introduced.

## Transaction trace

1. `events/006_independence_wave.txt:12`, `chaosx.nr6.1`, accepts joint presentation only with the pending delivery receipt, joint executed flag, committed phase, joint owner, and positive frozen presentation count.
An orphaned pending marker is cleared before standalone allocation.
2. `independence_wave_prepare_and_execute_standalone_incident` clears the previous standalone outcome, recovers only permitted stale standalone phases, captures chaos tuning, and opens an automatic Event 006-only plan through `liberation_release_begin_plan`.
The six tuning values remain 3, 4, 5, 7, 10, and 10.
3. `independence_wave_allocate_automatic_packages` begins the durable possible-country registry and contribution, reserves admitted anchors until exact completion or exhaustion/attempt limit, then publishes readiness only for an aligned exact plan.
The shared joint caller reserves Event 005 anchors first, adds the Event 006 target to its expected count, and uses the same Event 006 allocator against the occupied reservation footprint.
4. Automatic readiness wrappers resolve each exact carrier through `global.independence_wave_plan_possible_countries` and require package preflight plus an available anchor.
Reservation also requires content attestation, the exact force-package mapping, country/anchor/host targets, and the shared host-survival and collision checks.
No admission writer changed.
5. `independence_wave_validate_execution_metadata` requires locked/aligned metadata and exact selected-versus-target equality, exact adapter and force readiness, dormant reserved carrier preflight, a reserved anchor owned by its former host, and former-host membership in the populated `global.liberation_plan_hosts` ledger.
The earlier stale Event-006-only host-ledger defect is already absent.
6. `independence_wave_release_one_frozen_country` preserves the current dormant-shell path and the absent-carrier `every_possible_country` path.
Ordinary absent countries are released by the former host with `release = PREV`, then the live country target is rebound.
The nine explicit dynamic-carrier branches remain untouched.
The live country row, aligned state-target rows, and per-state target variables are rebound before later transfers.
7. Frozen state transfer checks ownership and control, then applies the frozen capital.
The finalizer runs preparation, activation, full package validation, and origin commitment with matching counters before the shared commit barrier.
Pre-finalizer failures use the existing compensating ledger, while irreversible finalization failures stay explicit failures.
8. `independence_wave_commit_wave_history` freezes report fields and replaces the global latest-actor target.
Only the committed standalone receipt or verified committed joint delivery reaches `chaosx.nr6.2`.
The public report also requires a positive frozen country count.
The durable terminal receipt remains diagnostic-only and does not create a pre-event surface.

The audit did not prove a further source-safe cause of the originally reported zero-country result.
The count-rewrite defect could create an undersized success, so its removal is a contract repair and must not be described as proof that the earlier zero-release symptom is fixed.

## Reference review

Read AGENTS.md, the `chaos-redux-events` and `chaos-redux-subagents` skills, the Event 006 README and relevant Parts 1 and 2, current source-of-truth/resume entries, and the terminal-receipt documentation.
Consulted the required offline core wiki pages, including the Data structures temporary-variable and event-target lifetime sections, Scopes invalid-target semantics, and Event modding event delivery.
Consulted installed vanilla script constants documentation, the Script Constants concept section, `release`, `create_dynamic_country`, `save_event_target_as`, and `has_event_target` documentation.
The installed vanilla `common/decisions/YUG.txt` release sequence supplies a concrete `release = PREV` precedent.
Existing shared dynamic effect and documentation registries were reviewed, and no generic helper extraction was needed.

## Meaningful validation

- The unmodified allocator validator initially passed despite the two forbidden count assignments.
- The added regression assertions failed on both assignments before the gameplay patch, then passed after removal.
- `python .tools/audit_event6_allocator.py` passed after the patch with 32 attested packages, 29 compatible reservation groups, 40 runtime adapters, the exact ladder, and the twenty-package static host-survival witness.
- `python .tools/audit_event6_scenario_matrix.py` passed its 32 scenario cells and eight edge-case receipts, including zero failed-branch report/log dispatches.
- `python .tools/audit_event6_country_api.py` passed with 191 resolved unique carriers, zero missing carriers, and zero duplicates.
- The reviewed diff contains only the bounded allocator branch removal, its regression checks, and helper documentation.

These validators inspect source contracts and existing static receipts, not live allocation or engine execution.

## MCP evidence

Baseline `hoi4.event_inspect` state_flow completed with report `complete = true` at revision `9f6663c1f2469632c37df88cc3895b350f3238b6fc479f37fab5ac3aa3b6da64`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7afb1f3048d774b514d1ebeb096daab7267ad9a64fa9161a4ccd49e9e2dcf432/7f51beaa59d552eb6d3bb9f1444d3f0a036f932b741203a885142703c51e3c8d/event-state_flow-9f6663c1f246.json`.
The root scope render reused that full analysis, with 19,422 indexed helpers, zero skipped sources, 45 selected nodes, and 97,495 omitted nodes.
Its graph hash is `ef9883d41d343370fcfc5d73bcf8612f44ce25cec788c20ebda39853722229f1` and layout hash is `51bd6a2cf69574265b180b80306b25261f1d5cf4f83477458acfacd94b0b7739`.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c74903b4c5db9edc992a3e8199af02412a9cc60bb7b88238d1cf5703097d1d62/c65d49088551d8da079517e84f7a8b194328d7066b2be2cf34adc63a51ecbebf/event-scope-9f6663c1f246-manifest.json`.
The render validation did not pass because the full workspace contains 3,912 blocking event-chain diagnostics.
That aggregate was not attributed to this Event 006 helper, and this handoff does not treat full indexing as execution proof or a clean event audit.

Baseline `hoi4.probability_inspect` on the owning effect source discovered 14 outer random-list candidates with a complete declared pool, 14 required inputs, and zero unresolved discovery entries.
Source hash: `4ea923eb3654271e1214a8edad62fdf10e69343b8474c378a0e37ce6b6653e8b`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd8fe3bae3d9472d8c1281d75ceea086b1d16a4a9bc6f6df54d974f82e54acff/eb80935be31a0ebb4465a108a00bd3128c2b6e1b2722e80271620fdf01f2bc49/probability-inspect-4ea923eb3654.json`.
Discovery is not a balance evaluation or a runtime-pool completeness claim.
The parent was asked to route the same-scenario before/after evidence through its probability auditor, with the unchanged HEAD source available as the baseline.

## Remaining gates

The post-change full `hoi4.event_inspect` state_flow refresh completed with `status = error`, `code = INTERNAL_ERROR`, blocker `Unexpected internal error`, and no artifacts or diagnostics.
The exact request used root `chaosx.nr6.1`, `expandHelpers = true`, `maxDepth = 3`, `maxNodes = 45`, and `refresh = true`.
No post-change event revision or successful before/after event comparison can be claimed from that failed refresh.
The specialist probability compare remains parent-owned and pending.
The original runtime failure remains unresolved because no runtime receipt identifying its failure phase was provided to this audit.
No live game was launched, no logs were requested, and no new diagnostic gameplay code was added.
No commit is made while the required comparison and parent review remain pending.

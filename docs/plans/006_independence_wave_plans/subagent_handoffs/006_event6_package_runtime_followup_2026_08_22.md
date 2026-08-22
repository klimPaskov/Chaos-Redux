# Repo Explorer Handoff

> Superseded for the joint-capacity surface by `abb0a8c83` and `006_event6_joint_capacity_wrapper_2026_08_22.md`. The nine admitted-package wrappers identified below are now installed; the ordinary zero-country path remains intentionally unresolved without a terminal runtime receipt.

## Scope read

- Parent task: audit Event 006 admitted-package runtime completeness and explain the zero-country manual result.
- Explicit constraints: read-only exploration; no gameplay edits; compare the 32 attested IDs with adapters, readiness wrappers, loaders/reservation publishers, dispatch, generic focus validation, and the static witness.
- Files or ids requested: `has_independence_wave_runtime_package_content_attestation_for_execution_id`, all 32 current attested IDs, Event 006 manual root `chaosx.nr6.1`, and the automatic allocator.
- Skills or docs read: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, required offline Paradox wiki pages, and the relevant vanilla effects/triggers/script-concept documentation.

## Primary findings

- The current source boundary is internally closed for the 32 attested IDs: 40 runtime adapters, 32 content attestations, 29 reservation groups, exact regional loaders and reservation publishers, 26 setup/final-validation/cleanup family dispatches, and the common generic-focus/AI barrier. `.tools/audit_event6_allocator.py` passes with 149 publishers, 20 static witness packages, and the 3/4/5/7/10 ladder.
- At the time of this exploration, the Event 005-aware Liberations capacity witness was narrower than the attested set. Commit `abb0a8c83` adds automatic-readiness wrappers and capacity-try calls for the nine missing IDs, so the current source has 32 readiness wrappers, 32 capacity tries, and 32 callers matching the 32 content attestations.
- Ordinary Event 006 allocation does not use the joint-capacity wrapper list. Each regional publisher calls its own `can_plan_independence_wave_package_iw_*` trigger, so the former nine-ID difference was a joint-capacity completeness gap, not proof that the ordinary manual allocator cannot see those packages.
- No unconditional source gate blocks AXX/BAX/BBX. IW-024 AXX requires exact dormant-origin availability, anchor state 82 owned by ROM, and its package runtime proof; IW-027 BAX requires state 184 owned by GRE; IW-028 BBX requires state 185 owned by GRE. Their final package checks also require complete setup, current-generation force package, protected former-host state, and the generic focus contract. These are valid fail-closed world-state conditions, not missing package adapters.
- A zero-country manual result is still possible when every attested candidate is unavailable in the actual world state. Candidate weights start at zero and receive positive weight only inside the content-attestation gate. If all fourteen region totals are zero, the first draw sets `independence_wave_plan_pool_exhausted`; the zero-selected branch marks `insufficient_pool`, never sets contribution-ready, and the execution/report path is skipped. A nonzero partial pool would be committed as a smaller wave, so “161 rows remain unattested” alone does not explain zero.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | Central adapter, attestation, and exact runtime preflight gates. | Adapter OR-list at lines 10-61; 32-ID attestation OR-list at lines 159-201; normal preflight requires dormant carrier, adapter, attestation, origin safety, and exact package/tag proof at lines 207-402. |
| `common/scripted_triggers/006_independence_wave_triggers.txt` | Joint automatic readiness and capacity witness. | The pre-repair exploration found 23 IDs; current source after `abb0a8c83` has 32 matching readiness wrappers, capacity tries, and caller entries. |
| `common/scripted_effects/006_independence_wave_package_allocator_effects.txt` | Explains the zero-country path. | Region totals and zero-pool handling at lines 47-77; allocation loop and exact/partial/zero-selected branches at lines 79-157. The zero-selected branch records `liberation_plan_last_failure = insufficient_pool`. |
| `common/scripted_effects/006_independence_wave_package_planner_effects.txt` | Candidate weight and reservation safety. | Candidate starts at zero and receives base/minimum weight only within the attestation gate at lines 484-700; reservation enters only for an attested anchor-phase candidate at lines 95-150. |
| `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | Shared setup/final/cleanup dispatch. | 26 regional family calls are present in each phase at lines 13-119; final validation enforces `has_independence_wave_generic_focus_contract` or `independence_wave_generic_ai_profile` at lines 73-88. |
| `common/scripted_effects/006_independence_wave_execution_effects.txt` | Manual Event 006 transaction wrapper and release/report boundary. | Root wrapper begins at line 840; allocator runs at lines 864-870; execution only runs after contribution-ready at lines 876-881; committed report flag is set at lines 884-887; receipt snapshot is at line 923. |
| `events/006_independence_wave.txt` | Manual root behavior. | `chaosx.nr6.1` at lines 11-63 calls the standalone wrapper at line 49 and only fires the public report after `independence_wave_standalone_incident_committed` at lines 51-59. |
| `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt` | Safe one-package parity candidate. | IW-045 loader at lines 30-40 binds BSK/state 651/group `rg_651`; reservation publisher at line 189 uses the shared begin/reserve/finish contract. |
| `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt` | IW-045 ordinary allocator gate. | `can_plan_independence_wave_package_iw_045` at lines 24-31 checks open plan, remaining slot, package/group uniqueness, exact BSK tag availability, and anchor 651. |
| `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt` | IW-045 package runtime setup/final validation. | Setup at lines 334-403 assigns the full shared focus framework at line 370 and publishes setup success at lines 399-401; final validation at lines 410-411 requires complete setup and exact runtime readiness. |
| `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt` | IW-024 AXX exact runtime contract. | Exact tag/anchor/ROM proof at lines 14-21; runtime-ready proof at lines 23-38; complete setup contract at lines 190-199. |
| `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt` | IW-027 BAX exact runtime contract. | Exact tag/anchor/GRE proof at lines 14-21; runtime-ready proof at lines 23-38; complete setup contract at lines 190-199. |
| `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt` | IW-028 BBX exact runtime contract. | Exact tag/anchor/GRE proof at lines 14-21; runtime-ready proof at lines 23-38; complete setup contract at lines 190-199. |
| `.tools/audit_event6_allocator.py` | Static source witness, not live engine evidence. | `STATIC_20_WITNESS_IDS` at lines 20-42; validator at lines 231-381; current run passes with 149 publishers, 32 attestations, 29 groups, and 20 witness packages. |

## Existing patterns

The ordinary allocator intentionally derives runtime eligibility from each regional `can_plan_independence_wave_package_iw_*` trigger and then routes the selected package through the exact loader/reservation publisher. The shared dispatcher owns family setup/final-validation/cleanup and rejects a package that lacks the generic focus contract or generic AI profile. This is a coherent fail-closed pattern.

The automatic-readiness wrappers are a separate Event 005-aware capacity witness. They are conservative and do not reserve tags, anchors, hosts, or groups. The completed `abb0a8c83` repair preserves the exact tag, anchor availability, Event 005 collision, former-host, and reservation-group checks for all 32 admitted packages and does not bypass the central attestation gate.

## Vanilla or reference precedents

The offline Paradox wiki Data structures, Triggers, Effects, Scopes, On actions, Event modding, Localisation, Decision modding, Idea modding, and AI modding pages were consulted, together with vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`. They support the documented `random_list`, scoped trigger/effect, temporary-variable, event-target, and collection semantics used by the source. No vanilla precedent is needed to justify widening an Event 006 package admission; the current Chaos Redux package contract is the governing pattern.

## Likely edit order for the parent

1. Treat the zero-country symptom as an unresolved runtime-state result until the terminal receipt distinguishes zero selection from post-mutation rollback. Do not relax the attestation, host-survival, generic-focus, or transaction gates from the symptom alone.
2. The Event 005-aware joint-capacity parity repair is complete in `abb0a8c83` for IW-024/027/028/030/031/038/040/044/045. Do not widen central attestation or admit any adapter-only ID from this handoff.
3. If the intended scope is ordinary manual allocation, first capture the terminal receipt and inspect `selected_count`, `target_count`, `attempt_count`, `last_failure`, `phase`, `instantiated_count`, `transferred_state_count`, and rollback/finalization flags. A new world-scan gate would duplicate the 32 package predicates and is not justified by current source evidence.

## Validation checks

- Run `python .tools/audit_event6_allocator.py` and retain the current static result.
- Recompute the attestation/adapters set difference and verify the nine-ID joint-capacity gap remains explicit.
- For the completed wrapper repair, verify 32 readiness wrappers, 32 capacity-try functions, 32 caller entries, exact tag/anchor/host/group checks, and no changes to the central adapter/attestation OR-lists.
- Re-run focused read-only `hoi4.event_inspect`/`hoi4.event_render` for `chaosx.nr6.1` after any parent gameplay edit. Current results are partial and defer workspace-wide helper/lifecycle projections.

## Risks and blockers

Confirmed limitations:

- The static witness is source/static only and does not simulate current ownership, control, living tags, anchors, host survival, reservation collisions, or rollback.
- Current `hoi4.event_inspect` and `hoi4.event_render` results for `chaosx.nr6.1` are `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with helper/lifecycle expansion deferred. Current event artifacts include `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a61fde1b81f81eda606d419dfb08d42bf40cbffa48102a937e168cacd881bd5/130ffe2f8be5240916fa4b384f217ff79e5830f354cc127c3d2a9be4fe72313b/event-scan-2af1fa63424e.json` and the state artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70b692a2edb32cbd2cb034fe4b9be178528d20997041a44838c6e14764ced82e/26bf0afe83cedd55375acbcb70743a98c539d51d6c25b3015df827a7cc0bce3b/event-state-2af1fa63424e.json`.
- Required detailed probability ownership could not be routed through `chaosx_ai_probability_auditor`; no callable tool with that name is exposed in this runtime. Direct `hoi4.probability_inspect` did run first against the allocator with adapter `custom_weighted_pool`, source `{path:"common/scripted_effects/006_independence_wave_package_allocator_effects.txt"}`, and candidate regions. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `unresolved=14`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e885f11dee8c3c380e945f4f7506f57d4238912f9d4819da63c111a6a9efea5/d69b49b135c1b50a43d66b354733bde84b448ae51cfcf0f88c016a6e50bde0ff/probability-inspect-9cab0bffea71.json`. This is not runtime probability evidence.

The former ordinary risk of adding IW-045 to the joint capacity witness is closed by `abb0a8c83`; its exact joint-order, collision, host, and group checks remain bounded and fail-closed. The ordinary standalone zero-country result still requires a terminal receipt before any allocator change.

## Recommended next action

Do not patch ordinary manual allocation from the zero-country symptom alone. The Event 005-aware wrapper gap is already repaired in `abb0a8c83`; separately obtain the terminal receipt before changing the ordinary allocator. The current source still fails closed and explains the zero-result path when no attested candidate is eligible in the live world state.

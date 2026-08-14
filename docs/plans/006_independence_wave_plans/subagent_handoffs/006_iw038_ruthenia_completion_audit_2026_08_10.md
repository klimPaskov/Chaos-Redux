# IW-038 Ruthenia completion audit — 2026-08-10

## Verdict

**READY / PROMOTED for the IW-038 package tranche.**

IW-038 Ruthenia is complete enough for Event 006 package admission on the current filesystem.
The atomic promotion is now present in the shared runtime adapter, content-attestation list, normal preflight, scenario preflight, Region-04 allocator, and Join Wave probe.
This verdict is limited to IW-038 and does not change the ongoing partial status of Event 006 as a whole.

No gameplay file was edited by this audit.
The only audit-owned change is this handoff.

## Authority reviewed

- Current implementation plan: `docs/plans/006_independence_wave_plans/006_iw038_ruthenia_implementation_plan_current_2026_08_10.md`.
- Package documentation: `docs/events/006_independence_wave/ruthenia_package.md`.
- Core Event 006 specification and registries: `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, and `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md`.
- Current source and all IW-038 country-core, decision, focus, localisation, portrait, flag, and probability handoffs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

## Completion status by surface

| Surface | Status | Current evidence and limits |
| --- | --- | --- |
| Registered identity and map anchor | **Finished** | Vanilla `RUT` is reused without rewriting its ordinary history. `is_independence_wave_exact_package_iw_038_tag_available` requires a dormant RUT origin, vanilla capital binding to state 73, an available state-73 anchor, and a distinct living owner in `common/scripted_triggers/006_independence_wave_package_triggers.txt:166-180`. The package remains bound to REG-04 and RG-73. The country-core handoff preserves the state-73 MCP map receipt; no map rewrite is part of IW-038. |
| Event 005 collision and former-host safety | **Finished at source level** | State 73 continues through shared candidate-anchor and reservation checks, including the Event 005 protection contract. Runtime initialization and final readiness require the frozen actual former host, its protected state, and a distinct live scope in `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:49-80` and `:129-202`. No hardcoded CZE fallback was introduced. |
| Lifecycle adapters and cleanup | **Finished** | `independence_wave_setup_iw_038_ruthenia`, final validation, and generation-safe cleanup are present and dispatched from `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`. Setup initializes ledgers, laws, routes, focus assignment, force mapping, AI profile, and completion receipts; cleanup removes the mission and ten projects, package ideas, Event 006 characters, route cosmetics, variables, flags, and the scoped Voloshyn portrait override. |
| Hidden roster checkpoint event | **Finished with partial MCP graph status** | `chaosx.nr6.350` recruits Brodiy, Mondok, and Klympush idempotently, applies the Event 006-only Voloshyn portrait, and publishes the roster checkpoint only after the four-character roster passes in `events/006_independence_wave.txt:278-318`. Mandatory `hoi4.event_inspect` and `hoi4.event_render` both resolved revision `3691f675a525fe0ba010bb87cad447431bd07ebb9c540ff1378ccf6e7620e7b9` as partial, with no IW-038/package blocker. The selected neighborhood contained two nodes. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0fe82947f9db1c1468a441a58abb74a2321024ec232294ce979e7596e1f4f27/8cf81327503b3a678bbd7a6a2cd26ac4c4da0d3defc66624f4ec0a047e6c26f7/event-trace-3691f675a525.json`. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7052c85c1a8fafc970ece1a551db0fc8d4fefe9db2e2e1f8700be063e2c3721c/55e681c33ba63352211cf65fdfa4e4eccdd7c7cd7f308d44ec5f6694a6006b78/event-neighborhood-3691f675a525.svg`. The global graph's unrelated diagnostics are not package findings. |
| Force package | **Finished at source level** | The package registers exactly five pathways and requires the p38 mountain-frontier profile, military tradition 60, pathway mask 647, no naval inheritance, and no air inheritance. Setup applies the shared dynamic force mapping only after the roster checkpoint; the exact proof is in `has_prepared_independence_wave_iw_038_package_setup`. No custom 3D unit, skeletal animation, custom unit audio, or bespoke unit counter is introduced, so the 3D/audio/counter pipeline is not applicable. |
| Shared focus integration | **Finished** | The full `independence_wave_focus_tree` is deliberately used; no bespoke or additive RUT tree is planned. Exactly five calls exist, each guarded by `original_tag = RUT` and `is_independence_wave_rut_package = yes`, at `common/national_focus/006_independence_wave_focus.txt:115`, `:157`, `:180`, `:1410`, and `:1680`. The final focus audit found one call and one idempotent helper definition for each, with no missing RUT prerequisite, reward, icon, or localisation consumer. Current focus MCP evidence retains only unrelated shared-tree/installed-vanilla diagnostics. |
| Founding mission and ten projects | **Finished** | `common/decisions/006_independence_wave_ruthenia_decisions.txt` contains the activation-backed 600-day founding mission and ten serialized, paid, timed projects. Projects cover depots, border guards, communities, former-host settlement, four mutually exclusive governments, durable sovereignty, and the Carpathian corridor. They have real resource payments, capital/package/crisis cancellation, bounded failure effects, one-shot flags, cleanup, and centralized AI scores. Exact displayed resource amounts are now eligible through `NOT = { ... < constant:... }` gates in `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:30-47`. Durable sovereignty now includes the founding-settlement flag in both visibility and availability. |
| Paid-project timer convention | **Accepted disposition** | The ten paid projects use the established Event 006 KOS/MNT `days_remove` convention: timer expiry is successful completion through `remove_effect`, while cancellation invokes the bounded failure helper. The founding mission alone has an explicit failed timeout. This is a disclosed accepted interpretation of the plan, not an undisclosed fallback. |
| Country politics, ideas, host/network/league/ambition | **Finished at source level** | Four route installers promote the researched leaders, set ruling parties and cosmetics, replace route ideas, and lock further government selection. The two visible ledgers are centralized and clamped. Host settlement uses the frozen host or a gated local fallback; the corridor integrates the shared network, league, and ambition helpers. No Ruthenian formable is admitted, matching the plan. |
| AI and weighted logic | **Finished with disclosed adapter limits** | The root-owned final audit is `006_iw038_ruthenia_probability_final_audit_2026_08_10.md`. It records a complete 11-candidate mission pool, a complete scoped five-hook focus pool, bounded six-scenario mission and focus evaluations, a current/current comparison receipt with zero changes, and rendered analysis artifacts. Typed campaign state remains unavailable to the adapter, so the evaluations are partial and do not prove exact live click probabilities, dominance, starvation, or rank reversal. The AI-strategy adapter reports `PROBABILITY_SURFACE_EMPTY` for strategy declarations. These are disclosed tool limits rather than missing source AI. The authored route/project/focus scores and fail-closed eligibility gates are present. |
| Central admission and allocator | **Finished / promoted** | The current shared dispatch trigger contains IW-038 in the runtime adapter list, content attestation, exact normal preflight, and exact scenario preflight. `common/scripted_effects/006_independence_wave_join_effects.txt:237` includes IW-038 in Join Wave. Region-04 retains IW-038 in its eight-entry random list and now validly computes its weight after the same atomic promotion. Parent-owned promotion validation reports the allocator checks passing at 29/26. |
| Characters and portraits | **Finished in authorized source-placeholder mode** | All four grounded male consumers have a `chaosx_portrait_creator` handoff, attributed source masters, immutable crop evidence, 156x210 runtime DDS files, stable sprites, and current wiring. Mondok is `PASS`; Voloshyn, Brodiy, and Klympush are explicitly `PASS_WITH_CAVEAT`. The user-authorized source-placeholder state is not a fail-closed identity result. No generic face, fictional likeness, or unreported substitute was used. Future user-supplied HOI4-styled replacements remain optional replacement work, not an IW-038 promotion blocker. |
| Flags | **Finished** | Four original native-ImageGen alternate-history flat flag ladders exist for `CIVICX`, `AGRARIANX`, `SOCIALISTX`, and strict-1936 `EMERGENCYX`, with normal/medium/small runtime TGAs, source masters, prompts, manifests, checksums, comparison sheets, and DDS round-trip evidence under `docs/assets/006_independence_wave/iw038_ruthenia_flags_2026_08_10/`. All route cosmetics and localisation families are wired. No sourced image was copied and no generated design is presented as an attested 1936 flag. |
| Localisation | **Finished** | `localisation/english/006_independence_wave_ruthenia_l_english.yml` contains the audited 125 scoped entries, with zero missing or duplicate keys in the final localisation handoff. It covers parties, cosmetics, ideas, category, mission/projects, tooltips, costs, and characters. The package documentation and runtime wording were reconciled with actual mission, corridor, portrait, and cost behavior. |
| Package documentation | **Finished; central authority map follow-up remains** | `docs/events/006_independence_wave/ruthenia_package.md`, the implementation plan, asset manifests, and bounded handoffs exist and agree with current source. `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` does not yet name the IW-038 promotion; the next Event 006 documentation-curator pass should add the package and this audit to the central authority index. This indexing gap does not invalidate the package implementation. |
| Event log, event details, evolutions, catalog | **Not applicable to the hidden checkpoint** | `.350` is a synchronous hidden implementation checkpoint, not a new player-facing Event 006 root, log entry, evolution, or scenario catalog row. IW-038 does not create a separate event-details entry or workbook event. The shared Event 006 catalog remains governed by the event-wide workstream. |
| Dedicated GUI, animation, super-event, achievement | **Not applicable** | IW-038 uses the ordinary decision shell and shared focus tree. It introduces no event-owned scripted GUI, shared-UI change, animated surface, super-event, or achievement, so no `chaosx_event_ui_worker`, GUI MCP, frame-animation, super-event, or achievement handoff is required. |

## Accepted-plan disposition

| Central plan gate | Disposition |
| --- | --- |
| 1. State-73 map, host, and collision checks | **Implemented and evidenced.** |
| 2. Dormant RUT and Event 005 collision compatibility | **Implemented fail-closed in exact tag/anchor and shared reservation gates.** |
| 3. Setup, final-validation, and cleanup adapters | **Implemented and dispatched.** |
| 4. Exact p38 force receipt | **Implemented at source level; live consumer validation remains user-owned.** |
| 5. Full shared focus framework and five hooks | **Implemented and independently audited.** |
| 6. Founding mission, ten paid projects, costs, failure, AI, cleanup, and final text | **Implemented; cost equality and durable-visibility findings were corrected before this verdict.** |
| 7. Roster, portraits, flags, and package documentation | **Implemented; portraits are in explicitly authorized source-placeholder mode.** |
| 8. Former host, network, league, ambition, and route-visible effects | **Implemented at source level.** |
| 9. Normal, scenario/SCN008, and Join Wave admission parity | **Implemented in the current central dispatch and Join Wave source.** |
| 10. Package/focus/decision/localisation/probability/asset/map/docs/completion audits | **Satisfied for promotion with disclosed MCP and user-owned runtime limits.** |

The plan's zero-allocation-weight rule was respected until admission.
The current nonzero Region-04 candidate path is valid because the central attestation and exact preflight branches landed in the same atomic promotion.

## Stale or superseded handoff claims

- `006_iw038_decision_mission_audit_2026_08_10.md` says Ruthenia localisation and package documentation are absent.
Those claims are superseded by `006_iw038_ruthenia_localisation_final_2026_08_10.md`, `localisation/english/006_independence_wave_ruthenia_l_english.yml`, and `docs/events/006_independence_wave/ruthenia_package.md`.
- The same decision audit's exact-resource and durable-sovereignty visibility findings were corrected in current triggers and decisions.
- `006_iw038_ruthenia_country_core_handoff_2026_08_10.md` says central attestation, normal/scenario preflight, and Join Wave admission remain off.
That statement is superseded by the current central dispatch trigger and Join Wave source.
- `006_iw038_ruthenia_focus_tree_final_audit_2026_08_10.md` carries the old missing-localisation claim.
The five-hook conclusion remains current, but the localisation blocker does not.
- `006_iw038_ruthenia_flat_flag_contracts_2026_08_10.md` is the research/prompt contract and correctly says it produced no binaries.
Production is superseded by the generated flag package manifest and GFX handoff under `docs/assets/006_independence_wave/iw038_ruthenia_flags_2026_08_10/`.
- The probability handoff records `constant:independence_wave_ruthenia_ai.corridor_priority` as unused.
That tuning mismatch was resolved after the audit by removing the unused constant; neither the current Ruthenia constants file nor AI-strategy file retains the identifier.

## Remaining limitations and recommended actions

1. Add IW-038 and this promotion audit to `006_source_of_truth_map.md` during the next bounded Event 006 documentation-curator pass.
2. Keep the probability handoff's limits explicit: no exact live selection probability or whole-tree focus race was proven from the untyped MCP fixtures.
3. Preserve the three `PASS_WITH_CAVEAT` portrait rights statements until the user supplies replacements or explicitly revisits jurisdiction review.
4. User-owned live-session validation remains outside agent scope, including Event 005 collision behavior, normal and SCN008 admission, Join Wave selection, p38 force realization, focus completion, decision UI, cleanup, and save/runtime consumers.

No missing mechanic, unapproved fallback, generic identity substitution, custom-UI omission, 3D/audio/counter gap, or unhandled improvement addendum remains that should block IW-038 promotion.

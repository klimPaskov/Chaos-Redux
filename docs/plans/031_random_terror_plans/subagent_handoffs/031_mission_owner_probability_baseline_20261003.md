# Event 31 mission-owner probability baseline

Status: immutable pre-owner-patch source snapshot and 26-scenario fixture deposited. The baseline probability evaluation is partial and unresolved; no mission eligibility or normalized probability claim is made. No gameplay source, AI weight, threshold, or balance target was edited.

## Acceptance and scope

The accepted mission contract is recorded in [031_random_terror_decision_mission_matrix.md](../../../specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md) and [031_random_terror_decision_mission_prompt.md](../../../specs/031_random_terror_specs/031_random_terror_decision_mission_prompt.md). The current source-owner findings and recommended receiver/progress contract are in [031_mission_owner_and_progress_contract_20261003.md](031_mission_owner_and_progress_contract_20261003.md). These were read in full for this bounded read-only baseline.

The eight mission candidates are `random_terror_contain_attack_wave`, `random_terror_protect_transport_network`, `random_terror_break_cross_border_corridor`, `random_terror_prevent_capital_seizure`, `random_terror_retake_lost_state`, `random_terror_restore_civil_authority`, `random_terror_hostage_deadline`, and `random_terror_stop_coordinated_uprising`.

The parent reports that its prepared receiver-keyed receipt patch and family-active locks have not been applied. The parent also reports six direct-ROOT setup paths and the nested-controller receiver for hostage and coordinated uprising. This handoff freezes the current baseline only; it does not authorize or implement a repair.

## Immutable before-source set

Physical byte copies are under `docs/plans/031_random_terror_plans/evidence/mission_owner_before_20261003/`, mirroring each repository-relative source path. The directory was absent before creation. The copies were made before the owner patch and checked byte-identical to their live sources immediately afterward.

| Source path | Bytes | Frozen SHA-256 |
| --- | ---: | --- |
| `common/decisions/031_random_terror_missions.txt` | 23,648 | `B24633FA4996FB2D25C44118C44A01F38B3C1C821DBCADF819FA71591813A71D` |
| `common/decisions/031_random_terror_decisions.txt` | 139,805 | `EC998C5B3355AAA8546EC73F0174F90F65A4665372C415DD2101315B2265F215` |
| `common/scripted_effects/031_random_terror_effects.txt` | 249,473 | `0F673544C04424C84EF7DAFADAE1A01F01B075904A5B8C7F4AE52177704972A2` |
| `common/scripted_triggers/031_random_terror_triggers.txt` | 23,168 | `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060` |
| `common/script_constants/031_random_terror_constants.txt` | 14,212 | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` |

The complete Event 31 decision, effect, trigger, and constant files are frozen because the eight mission definitions call Event 31 helpers and their direct setup, outcome, cleanup, and tuning definitions are in those files. No `mtth:` entry is referenced from the eight mission definitions or their decision AI blocks. This is a bounded source-closure statement for the named Event 31 mission paths, not a claim that every unrelated Event 31 effect or every external campaign state is modeled by the probability adapter.

The effects snapshot includes the current casualty-output repair present at freeze time. Its raw SHA-256 is `0F673544C04424C84EF7DAFADAE1A01F01B075904A5B8C7F4AE52177704972A2`; this differs from the earlier wave comparison's effects hash and is intentionally preserved in this mission baseline. The casualty repair is not an AI weight change.

## Immutable scenario fixture

The saved fixture is [031_mission_owner_probability_scenarios_20261003.json](../evidence/031_mission_owner_probability_scenarios_20261003.json), id `event31_mission_owner_baseline_20261003`, 26 named scenarios, SHA-256 `CFD5FF35E35DE0553DE8CC0F07C282FFD4A4CBA6FF97D4675D0BAA02475FDD94`. The exact same parsed file object was passed to the baseline evaluation. Do not regenerate or edit it for the after comparison.

Scenario IDs are: `mission_ai_neutral_baseline`, `mission_ai_high_pressure_context`, `mission_ai_low_legitimacy_context`, `mission_ai_final_unity_context`, `mission_ai_capital_transport_target_priority`, `mission_ai_retake_armed_state_priority`, `mission_a_b_same_mission_separate_states`, `mission_slot1_cross_family_conflict`, `mission_slot2_cross_family_conflict`, `mission_slot3_cross_family_conflict`, `mission_same_state_distinct_receivers`, `mission_transport_foreign_owned_root_controlled`, `mission_capital_foreign_owned_root_controlled`, `mission_restore_foreign_owned_root_controlled`, `mission_retake_external_claimed_enemy_controlled`, `mission_hostage_state_owner_controller_distinct`, `mission_uprising_actor_owner_controller_distinct`, `mission_completion_owner_local_only`, `mission_cancellation_owner_local_only`, `mission_timeout_owner_local_only`, `mission_recovery_close_owner_local`, `mission_global_defeat_cleanup`, `mission_capture_transfer_invalidation`, `mission_all_eight_success_outcome_criteria`, `mission_all_eight_partial_outcome_criteria`, and `mission_all_eight_failure_outcome_criteria`.

The fixture uses the existing `schemaVersion`/`id`/`scenarios`/`label`/primitive `state` envelope. It names A/B/C receivers and state roles in labels but does not invent unsupported typed scope fields. `scope.any_state`, mission ROOT, candidate-state owner/controller, nested CONTROLLER, receipts, per-family slot ownership, and action-result bindings remain unresolved until the connected route accepts typed bindings. Thus the scenarios are immutable named test intentions, not asserted engine-state bindings.

The fixture covers same mission for A and B on separate states; cross-family conflicts for slots 1, 2, and 3; two receivers on one state; foreign-owned/receiver-controlled transport, capital, and restoration targets; external claimed/core retake; hostage owner/controller separation; uprising actor/owner/controller/receiver separation; completion, cancel, timeout, local recovery cleanup, global defeat cleanup, and capture/transfer invalidation; and accepted success, partial, and failure criteria across all eight missions.

## Probability inspect and baseline evaluation

The read-only `hoi4.probability_inspect` used adapter `mission_ai_will_do`, source `{path:"common/decisions/031_random_terror_missions.txt"}`, the exact eight mission IDs above, and `refresh=true`. It returned `PROBABILITY_SOURCE_INSPECTED`, `status=ok`, `poolComplete=true`, `candidates=8`, `unresolved=0`, `requiredInputPaths=["scope.any_state"]`, and `availableCandidates=0`. This establishes that the adapter found all eight mission definitions in the source file; it does not establish scenario eligibility because state scopes are not bound.

The inspect artifact is [probability-inspect-15070be09547.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe20e6ff0a827c433b2949db1c650f76832493dbab4304acd3dd8a5211f35e88/e5568f8fc7b09dcd86c77d0cfee0d90f4adb81ee66c9e902698caca774736532/probability-inspect-15070be09547.json), 19,966 bytes, SHA-256 `fe20e6ff0a827c433b2949db1c650f76832493dbab4304acd3dd8a5211f35e88`. MCP source revision: `e1a54a8fc0135b42af0c4355012499d6172dface7aedcf8da3b64f0e547d32bb`; MCP source hash: `15070be09547197f477201e0395367a5cc5c5323430e9529d80ea6e0f4f2b0f8`. The same result was separately reported by the parent. No additional inspect request is pending from this auditor.

The baseline `hoi4.probability_evaluate` used the same adapter, source, eight-candidate list, and parsed 26-scenario fixture, with `metrics=["raw_value"]` and outputs JSON/ranking/matrix/unresolved. It returned `PROBABILITY_ANALYZED_PARTIAL`, `analysisId=probability-0b8ba2b6dce3976b64c8b383`, `scenarioHash=11d242f0ff0b036d60c9f59bc21320c8d69fd43cf0728ee266f741f9a5d69edc`, `sourceRevision=e1a54a8fc0135b42af0c4355012499d6172dface7aedcf8da3b64f0e547d32bb`, `sourceHash=15070be09547197f477201e0395367a5cc5c5323430e9529d80ea6e0f4f2b0f8`, `scenarios=26`, `candidates=208`, `eligibleCandidates=0`, `unresolved=18`, and `unresolvedCandidates=208`. The 208 entries are scenario-candidate instances for the eight definitions across 26 scenarios, not 208 distinct missions.

The evaluation artifact is [probability-0b8ba2b6dce3976b64c8b383.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5078537a298d6fae2b5c7a256591d27357a87a7d32c81e52e57502752e5323d1/24fa2a87f7c4ceae73f8384782abd6e3e0fe08174b1c872d0bf549ffae0b16fb/probability-0b8ba2b6dce3976b64c8b383.json), 1,861,076 bytes, SHA-256 `5078537a298d6fae2b5c7a256591d27357a87a7d32c81e52e57502752e5323d1`. Six derived visual artifacts were returned: ranking SVG/PNG, matrix SVG/PNG, and unresolved SVG/PNG. They visualize a partial unresolved analysis and must not be read as valid rankings or eligibility results.

The analyzer emitted two informational `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` diagnostics: the corridor mission's urgent factor at mission source line 243 and the hostage mission's urgent factor at line 544 were inactive in all supplied scenarios. This is fixture coverage feedback, not evidence that either factor is dead or should be tuned. The score result remains unresolved because the required `scope.any_state` inputs and typed country/state bindings were not supplied.

## Exact source-only mission weight inventory

The source sets the mission AI bases in `common/decisions/031_random_terror_missions.txt:11-16`: low 1, medium 3, high 7, urgent 12, high modifier factor 2, and urgent modifier factor 4. These are willingness scores, not click probabilities or normalized selection shares. No numeric weight or threshold was changed or recommended.

The eight current source weight recipes are:

| Mission | Base and source modifiers |
| --- | --- |
| Contain Attack Wave | Base high; urgent factor above the high pressure threshold; high factor for `random_terror_failed_raid_recorded`; high factor at war. |
| Protect Transport Network | Base high; urgent factor when the mission subject is the capital; high factor at war. |
| Break Cross-Border Corridor | Base high; urgent factor for `random_terror_support_disrupted`; high factor at war. |
| Prevent Capital Seizure | Base urgent; urgent factor at war; high factor for major countries. |
| Retake Lost State | Base high; urgent factor when a subject is an armed-insurgency state; high factor at war. |
| Restore Civil Authority | Base high; urgent factor below the low legitimacy threshold; high factor at war. |
| Hostage Deadline | Base urgent; urgent factor while the hostage-crisis country flag is active; high factor at war. |
| Stop Coordinated Uprising | Base urgent; urgent factor at war; high factor above the international-unity threshold. |

The transport-capital subject test (`missions.txt:168-172`) and retake armed-state subject test (`:397-401`) are the two state-receipt consumers the parent identifies for owner-keying. The other mission AI factors are country/global predicates or native war/major conditions. All require a valid mission context before their ranking can be evaluated.

An additional source-scope issue should be reviewed without changing weights: containment mission AI and other decision conditions read `random_terror_failed_raid_recorded` as a country flag (`missions.txt:91`; `decisions.txt:93, 1699, 1711, 1731`), while the frozen Event 31 effects file's visible writers at lines 562 and 2907 use `set_state_flag`. No country-flag writer for that identifier was found in the frozen Event 31 effects file. This is a likely scope mismatch, but the exact runtime writer/consumer binding remains unresolved; it is not a balance target.

## Candidate and external-factor completeness

The inspect pass reports the source candidate-definition pool complete for the eight named mission IDs. Scenario-effective eligibility is incomplete: the only required input path reported is `scope.any_state`, while the inspect result reports zero available candidates and the evaluate result reports zero eligible candidates. The fixture does not provide the state-scope input because no accepted typed ROOT/state schema was returned.

Unresolved external inputs include receiver country identity, country war and major status, actual mission-slot flags, nested hostage/uprising receiver scope, exact state subjects, state owner/controller changes, active family-specific locks, state activity/local-control flags, action progress receipts, timeout/cancellation events, and completion/cleanup receiver identity. The parent inventory's `DECISION_ANALYZED_PARTIAL` result is not permission evidence and does not resolve these bindings.

The parent reports that `hoi4.reference_context` for decisions with limit 2 and targeted reference searches/reads for `set_state_flag`, mission definitions, and `activate_mission` succeeded around 2026-10-03 22:31 local. This is parent-provided reference-route status; this handoff does not claim the child performed those live retrievals or infer their detailed output. The parent reports its decision-inspect inventory scanned 7,943 definitions and returned partial status with artifact SHA-256 `e052a29e3200f276d4d11ba9e2bdaca3acb1c52e1d4fd9111f87bb0a01fd6554`, source revision `7698bf78a4925a337290a538c5aa51006cbb661eba62cef0b48f3c416d7c9c8e`; the parent also reports a separate inspect request failed input validation and its inventory continuation remains unreturned. None of these is treated as scenario permission or state-binding evidence.

The parent reports that reading its inspect artifact failed with `-32603 Artifact provenance manifest is unavailable` and that a 6,000-byte retry was issued. That retry had not returned by this handoff. Its state is unreturned, not cancelled, and no unobserved artifact details are claimed.

## Baseline limits and next required evidence

No `probability_sweep`, `probability_simulate`, `probability_sequence`, or post-patch `probability_compare` was run. There is no complete typed scenario eligibility pool for a rank/sensitivity conclusion; no uncertain distribution, declared cadence/transition model, or owner-patched after source exists for the other routes. The partial evaluate's built-in ranking, matrix, and unresolved visuals do not supply those missing inputs.

After the owner patch, this read-only auditor must compare the frozen before source paths against the real current after paths with the exact same saved 26-scenario fixture and eight mission IDs. The compare must preserve `scope.any_state` and typed ROOT/receiver/target bindings as unresolved unless the connected schema accepts and returns them. Do not compare current source to itself, invent `beforeManifest`/`afterManifest` or typed fields, or call mission AI willingness a selection probability. No balance target is selected here.

No gameplay files were edited, no snapshots or scenarios were overwritten, no game was launched, and no logs were searched. The mission owner can now apply the prepared receiver/receipt and family-lock patch against the immutable before paths and scenario fixture. Full Event 31 mission completion and after-patch comparison remain open.

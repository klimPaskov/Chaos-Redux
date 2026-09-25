# Event 016 Mengele Singularity risky Prototype probability comparison

Date: 2026-09-25
Role: `chaosx_ai_probability_auditor`
Disposition: `implemented` as a read-only comparison handoff. The conditional random-list outcomes are exact for the declared weights; the source-to-weight derivation is source-traced and bounded because the adapter does not execute the enclosing Clausewitz effect sequence.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Scope and accepted context

This post-change audit compares the previous host incident pool with the new provider-owned Mengele Singularity incident pool used by all six risky native Prototype callbacks. It keeps the three baseline scenario IDs and contextual exposure values, while declaring the provider-side raw weights from its own capacity and stage-factor formula.

Accepted context: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md`, and the baseline handoff `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_accident_probability_baseline_2026-09-25.md`. The portfolio plan keeps the six native component IDs and requires Mengele provider receipts to remain separate from Kruger host state. This audit does not select or approve balance targets.

## Audited files and source identity

- `common/scripted_effects/016_mengele_singularity_incident_effects.txt:12-40`: provider dispatcher, gate, private pressure/complement calculation, and two-entry random list.
- `common/special_projects/projects/016_brilliant_scientist_projects.txt`: the six risky reward callbacks branch to `brilliant_scientist_mengele_dispatch_singularity_incident` when the Mengele provider stage is valid; the existing host path remains in the alternate branch.
- `common/script_constants/016_brilliant_scientist_project_constants.txt:16`: `brilliant_scientist_project_board.capacity_prototype = 10`.
- `common/script_constants/016_brilliant_scientist_constants.txt:873`: `brilliant_scientist_accident.prototype_stage_factor = 1.00`; the accident range is 0–100.
- Previous host baseline: `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1496-1505`, pressure and safe-complement entries.

Current local SHA-256 values:

- New provider incident effects: `03A14B2966609C7406826C00708135007424B7DDDA1D2AE44B6899DABC94D84D`.
- Native project callback file: `CD52D36792B2A9A9AC767268F131D0B36F1495D43F2B2AD8C52E5BA328E2AB23`.
- Project constants: `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131`.
- Accident constants: `ADFEE7FE6093933C394C34C8A6A162795D4BDB4575512C476B417C1173B6E4A6`.

Six routed reward tokens:

- `sp_brilliant_scientist_singularity_command_core_reward_false_arming_order_risky`.
- `sp_brilliant_scientist_singularity_power_link_reward_power_cascade_risky`.
- `sp_brilliant_scientist_singularity_containment_lattice_reward_lattice_failure_risky`.
- `sp_brilliant_scientist_singularity_temporal_authenticator_reward_contradictory_authentication_risky`.
- `sp_brilliant_scientist_singularity_delivery_architecture_reward_targeting_breach_risky`.
- `sp_brilliant_scientist_singularity_fail_deadly_governor_reward_unauthorized_activation_risky`.

## MCP inspect, evaluate, and compare

Workspace: `mod_chaos_redux_ea3b2d67c2c0`; adapter: `random_list`; verified game version in the comparison artifact: Operation Postern 1.19.2.0 (d245).

### New-pool inspect

`hoi4.probability_inspect` ran first on `common/scripted_effects/016_mengele_singularity_incident_effects.txt` with refresh enabled.

- Status `PROBABILITY_SOURCE_INSPECTED`; complete pool; two candidates; two required dynamic inputs; zero inspect unresolved findings. Dynamic candidates were not statically available (`availableCandidates: 0`, `candidateExamples: []`).
- `sourceRevision`: `989806ea955a125fc8bb37ba9753ce131c20f837e69a73de47ecf1ccc897e743`.
- `sourceHash`: `adeeffaf7d4216b1097f601dbc5f8175d52ef8ad39a91c086a80fc5ad0099ec3`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bea84415d047ea47634eb5753fbbbd0e1e0766938216d1c900c09e974123f499/49813038b9585b8614b6f3c5abb3c53ffee25c61c740087fcdb4c5ba87e16977/probability-inspect-adeeffaf7d42.json`.

The complete new candidate pool is `common/scripted_effects/016_mengele_singularity_incident_effects.txt:31.entry.1` (incident, weight `var:mengele_event016_singularity_incident_pressure`) and `:31.entry.2` (safe, weight `var:mengele_event016_singularity_incident_complement`).

### Named scenario contract

Scenario set ID remains `016-mengele-singularity-risky-prototype-baseline-2026-09-25`; actor remains the baseline fixture label `GER`. The following three scenario IDs and their host exposure context were preserved:

- `016-SING-RISK-PROTOTYPE-LOW-EXPOSURE`: host exposure 0; baseline host pressure 20; host safe complement 80.
- `016-SING-RISK-PROTOTYPE-MEDIUM-EXPOSURE`: host exposure 50; baseline host pressure 70; host safe complement 30.
- `016-SING-RISK-PROTOTYPE-HIGH-EXPOSURE`: host exposure 100; baseline host pressure 100; host safe complement 0.

Each scenario declares Prototype stage, a clean project, no host or Mengele incident active, no provider recovery active, empty `flags`, and empty `scopes`. Provider-valid and Prototype-stage-valid wrapper gates are assumed true and are source-traced; the random-list adapter does not evaluate those enclosing gates or establish country-specific Mengele eligibility.

The after-side provider formula is `capacity_prototype × prototype_stage_factor = 10 × 1.00`, clamped to the configured 0–100 range, with complement `100 − pressure`. The comparison and evaluation declare provider raw weights 10 and 90 in each scenario. These are effect-derived values supplied to the analyzer; the analyzer proves the conditional random-list result for the declared values but does not execute the preceding `set_temp_variable`, `multiply_temp_variable`, and clamp effects.

### Evaluation evidence for provider weights

`hoi4.probability_evaluate` used the new file, both explicit candidate IDs, the same three scenario IDs, and `var:`-qualified state keys for the two dynamic entries.

- Analysis ID `probability-e7699b84277874bd7e13ba1e`; status `PROBABILITY_ANALYZED`, complete, zero unresolved.
- `sourceRevision`: `df180c445bcaa8949a567c0282daa45a602d759c2ea3b4f75752d8c0ca5b7d31`; same `sourceHash` as inspect.
- `scenarioHash`: `41b5a83c5b760d775e9d6ede202b1a2bca0f069aae3d80579ba5fef2b5a589e6`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1388df26442b0b01200ff4befe6e2326cc67993e3585c169f9cdfb5f7e5605ec/7464eb95f85b974412da23f03d50137e0e7c952ab21d44af4ae907f7dbed411b/probability-e7699b84277874bd7e13ba1e.json`.

The evaluator returned four design warnings: the 0.90 safe outcome reaches the configured dominance threshold in each scenario, and the safe candidate is dominant across all three. These are analyzer diagnostics, not balance targets.

### Same-scenario before/after comparison

The first `hoi4.probability_compare` call used unqualified temporary names in the scenario state and returned `PROBABILITY_ANALYZED_PARTIAL`. It identified `VALUE_UNRESOLVED` for `var:mengele_event016_singularity_incident_pressure` and `var:mengele_event016_singularity_incident_complement` in all three scenarios. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37dc14298bea3e1a6d8e488405883a2df3d0f2675b6807ebaed194efa270ef04/3953cc6259680b4db73bb8936cdc9ed6cfe6393f08c43272715fbee54b08d66d/probability-8f28e1d6fb608cbb0e971b16.json`; scenario hash `f39e16fe9cd662e9fc9b7017cf4cb3cba309c288a761887b8e8a64302f1cffd1`. The binding issue was resolved by declaring the literal `var:`-qualified keys, then rerunning the compare.

Corrected `hoi4.probability_compare` compared the baseline host source `common/scripted_effects/016_brilliant_scientist_project_effects.txt` with the provider source `common/scripted_effects/016_mengele_singularity_incident_effects.txt`, using the same scenario IDs and host context.

- Analysis ID `probability-0b93b8c3696a98f5327e72c9`; status `PROBABILITY_ANALYZED`, complete; three scenarios; zero unresolved; zero comparison regressions; 12 source-candidate changes (the two old entries removed and two provider entries added for each scenario).
- `sourceRevision`: `0da94c5ad071e03202152df1b13f3922df6747d3b2519e6ea3b8be8b9379c578`; provider `sourceHash`: `adeeffaf7d4216b1097f601dbc5f8175d52ef8ad39a91c086a80fc5ad0099ec3`.
- `scenarioHash`: `c37c5272228a98c228109515b045b337d3a39dd6813d106879764c6973b20280`.
- Comparison sub-analyses: before `probability-7302118af9f66a57086af7b8`, after `probability-5e75cd325376c408c2193d48`.
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f878e692a7f73b7652e3fe601c81fdd507ca60c54535f435976161386da7d05c/aad07d143d3f723cbcf145506009a3b0fe55c6bf50968207e107e838ff39b4e9/probability-0b93b8c3696a98f5327e72c9.json`.
- Rendered comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9a085a82d1d0a9a3684f6c49705d3a52d33e70abfed5a88357499cb9384ad7f/cbdc17e811aa872f37318efa04618341f7c2f3c4f059d32eb08f35453f58d759/probability-probability-0b93b8c3696a98f5327e72c9-comparison.svg`.
- Unresolved view SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/bbceac67b42371508e4cf067e634e621490779b59aee42258f41360b2cc2b639/probability-probability-0b93b8c3696a98f5327e72c9-unresolved.svg`.

## Results and interpretation

| Scenario ID | Host baseline: incident / safe | Mengele after: incident / safe | Change in incident probability |
| --- | ---: | ---: | ---: |
| `016-SING-RISK-PROTOTYPE-LOW-EXPOSURE` | 0.20 / 0.80 | 0.10 / 0.90 | −0.10 |
| `016-SING-RISK-PROTOTYPE-MEDIUM-EXPOSURE` | 0.70 / 0.30 | 0.10 / 0.90 | −0.60 |
| `016-SING-RISK-PROTOTYPE-HIGH-EXPOSURE` | 1.00 / 0.00 | 0.10 / 0.90 | −0.90 |

Baseline values are from the prior exact evaluation artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/048868a74f2012a2853299111625e013539991c679f5e6521e97cd699ffe2aca/b7db80f0be5047f9146e59b3eaed9648325b92e3d15e39be2d13eeed6194934e/probability-b7c21734eb9b29b48dd049ff.json`, source revision `e437ad5002ec53a10fbd82cd21eb5254bb861e52f3cd41812f79ea4b45aa9b6b`, source hash `17f32e5028225cb6165d9745bf7934f78f0ca18b57d8024ab60703432f117826`, scenario hash `24296a31416d70abbfb26383979523981b763d84cdefa07aa61daab2f16bfdd6`.

This is a same-context, same-scenario source-derived comparison, not a literal identical-weight comparison. The host inputs are 20/70/100 because the prior path includes host exposure; the Mengele formula does not read that exposure and yields 10 in all three scenarios. Copying 20/70/100 into the provider entry weights would be a different counterfactual and would conceal the source change; no separate identical-weight control was run.

The two candidate pool is complete in each scenario. The outcomes remain safe-leading with no rank reversal or starvation across these three points. The 0.90 safe outcome is dominant under the analyzer's configured threshold; whether 90% is an acceptable target belongs to the parent. These are conditional chances after the risky reward callback runs, not chances of selecting the risky reward, researching/completing a native project, or suffering an incident over a campaign.

## Validity, recurrence, and remaining uncertainty

- All six source callbacks route to the provider dispatcher only when the Mengele provider-stage trigger passes; the dispatcher further checks provider validity, Prototype stage validity, no active private incident, and no active recovery. The conditional pool result assumes those gates pass. The probability adapter marks both random-list entries eligible implicitly and does not prove the outer provider/stage gates.
- The provider helper uses private incident flags and history, so the old host exposure and shared host active-incident flag no longer determine the new conditional draw. The new weight is constant across the three exposure contexts by source formula.
- The compare and evaluate prove exact conditional probabilities for the declared 10/90 raw weights. They do not execute the Clausewitz helper or validate runtime callback scope, trigger truth, effect ordering, recovery, or user/AI choice of the risky option.
- No `hoi4.probability_sweep` was run: the provider formula is constant at Prototype and the requested task was the same-scenario source comparison; no provider-capacity range or tuning target was declared. No simulation was run because no uncertain inputs were declared. No sequence analysis was run because this is a native single random-list draw, not a complete declared cadence/state-transition pool.
- No explicit `hoi4.probability_render` retry was needed; the completed compare returned comparison and unresolved render artifacts. No gameplay or runtime files were changed, and nothing was staged or committed.

## References and handoff

The required offline Paradox wiki pages, vanilla random-list/special-project documentation, and vanilla bouncing-bomb training-accident precedent were reviewed in the preceding baseline audit and are recorded in the baseline handoff. `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md` were followed for this update.

Parent follow-up: retain this corrected comparison with the provider patch review. If provider capacity or Prototype accident factor changes, repeat inspect/evaluate/compare under these same scenario IDs; do not interpret this fixed 10% as a selected or approved balance target.

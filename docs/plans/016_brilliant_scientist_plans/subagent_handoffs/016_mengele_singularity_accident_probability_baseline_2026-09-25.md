# Event 016 Mengele Strategic Singularity risky Prototype incident baseline

Date: 2026-09-25
Role: `chaosx_ai_probability_auditor`
Disposition: `implemented` for this read-only baseline handoff; the provider-specific incident path and its probability remain `unresolved` pending the parent-owned implementation and same-scenario comparison.

## Scope and accepted context

This audit covers the conditional incident draw after a risky Prototype reward option is selected for the six native Strategic Singularity components. It does not estimate whether an AI or player chooses the risky option, whether a project is selected, or the total chance of an incident over a campaign.

Accepted context read: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` and `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md`. The plan preserves the six native component project IDs and their existing weighted project pool, assigns provider-specific output/terminal routing to the parent, and identifies missing Mengele Singularity branches and the shared Fallout path as closure work. The Computation incident clauses in the completion contract are not treated as proof that the same private incident behavior is already implemented for Singularity.

## Audited surfaces and sources

- `common/special_projects/projects/016_brilliant_scientist_projects.txt`: six native components and risky Prototype reward options.
- `common/scripted_effects/016_brilliant_scientist_effects.txt:3695`: `brilliant_scientist_refresh_project_accident_pressure` derives host pressure from `brilliant_scientist_exposure`, stage capacity/factor, host-reaction modifiers, family modifiers, and clamps it.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1496-1505`: `brilliant_scientist_dispatch_project_accident`, active-incident guard, safe complement, and the two-outcome `random_list`.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1611-1629`: family incident dispatch, severe-pressure damage check, and delayed report event `chaosx.nr16.13`.
- The project file hash was `F0393DB1A44EB8409B770FB02C1CA392D806C8B318022763CD3B14ACB975EAAD`.
- The pressure helper file hash was `7DC6686137643177045B8FC278078E3BE349CE113D2520B9ADD8D21B11C4F447`.
- The random-list/effect file hash was `8B670BB2A868AEE0BA1275CC72D87161BAB222D47D2C10A88ADB478F51D7D5D7`.

The six project and risky reward IDs are:

- `sp_brilliant_scientist_singularity_command_core` / `sp_brilliant_scientist_singularity_command_core_reward_false_arming_order_risky`.
- `sp_brilliant_scientist_singularity_power_link` / `sp_brilliant_scientist_singularity_power_link_reward_power_cascade_risky`.
- `sp_brilliant_scientist_singularity_containment_lattice` / `sp_brilliant_scientist_singularity_containment_lattice_reward_lattice_failure_risky`.
- `sp_brilliant_scientist_singularity_temporal_authenticator` / `sp_brilliant_scientist_singularity_temporal_authenticator_reward_contradictory_authentication_risky`.
- `sp_brilliant_scientist_singularity_delivery_architecture` / `sp_brilliant_scientist_singularity_delivery_architecture_reward_targeting_breach_risky`.
- `sp_brilliant_scientist_singularity_fail_deadly_governor` / `sp_brilliant_scientist_singularity_fail_deadly_governor_reward_unauthorized_activation_risky`.

Each risky option sets family `singularity` and requested stage `prototype`, refreshes pressure, then calls the shared incident dispatcher. Each cautious option is the default and grants the low progress increment. Project visibility/availability uses `brilliant_scientist_can_research_singularity_component = yes`; the analyzer did not evaluate that gate or any project-selection `ai_will_do` score.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

1. Required baseline `hoi4.probability_inspect`, adapter `random_list`, source `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, `refresh=true`.
   - Status: `PROBABILITY_SOURCE_INSPECTED`; complete two-candidate pool; two required inputs; no inspect diagnostics or unresolved findings.
   - `sourceRevision`: `8f5ec979e56b59cfe4f3f9b231d65add8cf5f1a53433496281ccef8f641d49ab`.
   - `sourceHash`: `17f32e5028225cb6165d9745bf7934f78f0ca18b57d8024ab60703432f117826`.
   - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46e52a694dfefe77a094a592c6435b8c0fc69fd713b360be4805563ab1e70d99/1f7c952b3ca57f31c69985744d57d63f90610c0608223b0e15c721d698e36a5e/probability-inspect-17f32e502822.json`.
   - Candidate IDs: `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1501.entry.1` (safe complement) and `:1501.entry.2` (incident pressure). Both have the audited source hash above.
   - Adapter note: `hoi4-1.19.2.v1`, engine verified as Operation Postern v1.19.2.0.a729 (d245); `random_list` uses proportional categorical selection. Dynamic entry keys and effect-derived weights remain unresolved unless declared.

2. `hoi4.probability_evaluate`, adapter `random_list`, complete candidate pool, analysis `probability-b7c21734eb9b29b48dd049ff`.
   - Scenario set: `016-mengele-singularity-risky-prototype-baseline-2026-09-25`.
   - `scenarioHash`: `24296a31416d70abbfb26383979523981b763d84cdefa07aa61daab2f16bfdd6`.
   - Evaluation `sourceRevision`: `e437ad5002ec53a10fbd82cd21eb5254bb861e52f3cd41812f79ea4b45aa9b6b`; same `sourceHash` as inspect.
   - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/048868a74f2012a2853299111625e013539991c679f5e6521e97cd699ffe2aca/b7db80f0be5047f9146e59b3eaed9648325b92e3d15e39be2d13eeed6194934e/probability-b7c21734eb9b29b48dd049ff.json`.

3. `hoi4.probability_sweep`, analysis `probability-d4f7b34ca1a463c3b3f38994`, pressure path `brilliant_scientist_accident_pressure`, 101 requested steps, but only the single medium scenario was supplied.
   - Result had `sweepPoints: 1`, no breakpoints or rank reversals; it is one state evaluation, not a meaningful continuous sensitivity sweep.
   - `scenarioHash`: `38ebc067` (full hash is in the artifact); `sourceRevision`: `e437ad5002ec53a10fbd82cd21eb5254bb861e52f3cd41812f79ea4b45aa9b6b`.
   - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4721ddd4019aa81dfcb5c605571fc33e318ea4ae92d8509221ae8c2a2c14401/0a13651761a3c664960161019e0cd0530298039dc5aedc41e0d96192e57e5c56/probability-d4f7b34ca1a463c3b3f38994.json`.

4. `hoi4.probability_sweep`, analysis `probability-084299e799c54558291a5d67`, same pressure path, 101 requested steps, pairwise and rank-reversal detection enabled, with the same three named scenarios as the evaluation.
   - Result had three scenario points, `rankReversals: []`, and no continuous threshold/breakpoint evidence. The analyzer treated the declared low/medium/high inputs as three points rather than a continuous 0–100 range.
   - `scenarioHash`: `24296a31416d70abbfb26383979523981b763d84cdefa07aa61daab2f16bfdd6`; `sourceRevision`: `e437ad5002ec53a10fbd82cd21eb5254bb861e52f3cd41812f79ea4b45aa9b6b`.
   - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/760afd73ddcda53131abb2547cb2d0d0395e9d585de6c50c52991fa35b20f2d7/129b46aca335ed7538114f8de7de62c1d9177f06bde80bed598e9c93508342cb/probability-084299e799c54558291a5d67.json`.

5. Evaluation-generated render artifacts (the explicit `hoi4.probability_render` call was interrupted before returning):
   - Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/663051b18415f567dd85d64a679122dcf47841329610ac30163f9e64a6ddbcda/e7909c93cca4e29fbf72c8095097d3ef3802a650d78628091c1d51865f180450/probability-probability-b7c21734eb9b29b48dd049ff-ranking.svg`.
   - Matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3c042296992d463a74d30c78bfa8824282f06e6c941697ad6872e4b58fe2f44/769e9638b4af314405278b073e02549e9a3b625410a40e937eb14ccf6d515ff2/probability-probability-b7c21734eb9b29b48dd049ff-matrix.svg`.
   - Weight waterfall: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/392fcb49cde3337bc69cf54857a8d750b6480e6567e32c0407c15783ee6869db/ea087f8ae2afd085a7c1f62e0ae43401c2374c8ddb56451e49eeecbc044df2f3/probability-probability-b7c21734eb9b29b48dd049ff-waterfall.svg`.
   - Unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/bf6bd5885755ccbb4cf2239b7c34a07747bbf0efaa6e226d3e23f7904c9d4230/probability-probability-b7c21734eb9b29b48dd049ff-unresolved.svg`.

6. Sweep-generated render artifacts:
   - Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a367553407f732224e398293f27230c8ca7bcf18a8edc4c082c9e1f697e96b68/c9a46983af922a8090247df498f8212c7c13f2890598091f96064a73c58cb3fb/probability-probability-084299e799c54558291a5d67-ranking.svg`.
   - Sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3b0f10a0a94a67803b74b1025cd16938ae6f154716d4193c21d10ab68646c6e/46e9814859400dcc944a4d55f5a5e161e39f313b8d6a0ef423a6f38b216bd08d/probability-probability-084299e799c54558291a5d67-sensitivity.svg`.
   - Threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/627941c7085ea1482a53bc6dfb3366b53e70ccc21256be0ec10b04104b20da59/240dbd0e571b0d63a4f3f2ebb5215bd8f75898b56894c8642606fcfbc00bf9ea/probability-probability-084299e799c54558291a5d67-threshold.svg`.

No `hoi4.probability_compare` was run because this is the requested pre-change baseline and no after-source or candidate balance profile exists; the parent owns the post-change comparison using these same scenario IDs. No simulation was run because no uncertain-input distributions were declared. No sequence analysis was run because this is a native effect random list, not a complete declared custom-pool manifest with cadence, cooldown, transitions, and terminal states.

## Scenario contract and results

All three scenarios use actor `GER` as an explicit fixture label, family `singularity`, stage `prototype`, stage capacity input 20, Prototype factor 1.00, clean/nonsuspended project state, no active incident, and no host reaction/family-specific modifiers. There are no scheduled changes, random seed, or uncertain distributions. The actor label is not a country-specific eligibility audit; the two random-list entries do not branch on country identity.

The complete normalized candidate pool in every scenario is: `safe` with raw weight `brilliant_scientist_accident_safe_weight`, and `incident` with raw weight `brilliant_scientist_accident_pressure`. Both raw weights were explicitly supplied. MCP therefore proves the conditional distribution for these declared weights, while the adapter does not resolve the upstream effect-derived pressure expression.

| Scenario ID | Declared exposure | Declared accident pressure | Safe raw weight → probability | Incident raw weight → probability | Classification |
| --- | ---: | ---: | ---: | ---: | --- |
| `016-SING-RISK-PROTOTYPE-LOW-EXPOSURE` | 0 | 20 | 80 → 0.80 | 20 → 0.20 | Exact conditional distribution for declared weights |
| `016-SING-RISK-PROTOTYPE-MEDIUM-EXPOSURE` | 50 | 70 | 30 → 0.30 | 70 → 0.70 | Exact conditional distribution for declared weights |
| `016-SING-RISK-PROTOTYPE-HIGH-EXPOSURE` | 100 | 100 | 0 → 0 | 100 → 1.00 | Exact conditional distribution for declared weights |

Source trace for these fixture values: Prototype stage pressure is `cost_capacity × prototype_stage_factor`; Prototype factor is 1.00, host pressure starts at `brilliant_scientist_exposure`, host/family modifiers are applied, then pressure is clamped to 0–100 and rounded. The dispatcher sets safe raw weight to `maximum - pressure` and incident raw weight to pressure. The evaluator received these already derived values because the adapter reports that effect-derived weights are unresolved unless declared. The overall exposure-to-outcome relationship is therefore `bounded`, not an MCP-proven end-to-end effect evaluation.

## Findings

- Score and probability semantics: this is a proportional random-list draw conditional on the risky reward effect running. It is not a score race, `ai_will_do` value, click probability, risky-option selection probability, or probability that a project completes.
- Dominance and starvation: at high pressure, MCP emitted `PROBABILITY_DOMINANT_OUTCOME` for incident at 1.00 and `PROBABILITY_STARVED_OUTCOME` for safe at 0. The medium point is incident-leading at 0.70; low is safe-leading at 0.80.
- Rank change: the named points show the leader changing from safe at low to incident at medium/high. The sweep's `rankReversals` output is empty and it supplied no exact crossing threshold; a continuous rank-reversal location remains unresolved.
- Severe outcome: the source checks for pressure at or above `brilliant_scientist_accident.severe_threshold` (75) after beginning the incident and damages the project when met. In the declared high case pressure is 100; medium is 70. This is a source trace, not an MCP evaluation of the downstream event effects.
- Validity: source gates all six native projects through the shared component-research trigger. MCP did not evaluate the trigger, native project availability in an actual Mengele-owned country, DLC behavior, or selection of cautious versus risky reward.
- Repetition and starvation over time: the dispatcher skips the draw while `brilliant_scientist_project_incident_active` is set. This prevents overlapping host incidents but also makes future draws dependent on resolution/cleanup. No cadence, incident recovery horizon, or repeated-trial process was evaluated, so cumulative risk, long-run starvation, and snowball behavior are unresolved.
- Provider-boundary risk: the current refresh helper begins with host `brilliant_scientist_exposure` and writes the shared pressure variable; the dispatcher uses the shared active-incident flag and family incident path. If the native callback is invoked for Mengele, the baseline can inherit host state. The accepted portfolio plan identifies missing Mengele Singularity provider branches; this baseline is not evidence of a provider-private incident ledger.
- Exploit risk: maximum exposure forces the declared conditional draw to incident and, by source trace, crosses the severe damage threshold. Whether a provider can manipulate inherited host exposure or hold/re-enter an active incident depends on provider ownership and recovery code not modeled here; classify exploit/snowball risk as unresolved.

## Recommendations for the parent; no balance target selected

1. Route each of the six risky callbacks through the provider-owned incident state required by the accepted portfolio plan. Compute provider pressure from the declared provider capacity/stage inputs and keep Kruger exposure, incident flag, and incident ledger out of that route.
2. Preserve a complete two-entry pool and safe-complement invariant after the provider pressure calculation, including the 0 and 100 boundaries. Treat any tuning change as a candidate, not as an approved balance target.
3. Model the provider's active-incident guard, damage consequence, report/recovery path, cleanup and re-entry in the scenario contract before making repeated-event or campaign-level probability claims.
4. After implementation, ask this read-only auditor to run `hoi4.probability_compare` against this baseline with the same scenario IDs and candidate pool, then use a valid declared range sweep for thresholds if the adapter supports the required range syntax.

## Skipped analyses, blockers, and uncertainty

- Dedicated `hoi4.probability_render` and `hoi4.event_inspect`/`hoi4.event_render` calls were in a batch that was interrupted by the user after 24.7 seconds; no results returned. This is an interruption blocker, not a reported service timeout. The evaluation and sweep did return generated render artifact URIs listed above. The event report chain around `chaosx.nr16.13` has no structural MCP evidence in this handoff.
- Continuous sweep thresholds remain unresolved: the medium-only request produced one point, and the three-scenario request produced three declared points despite `steps=101`. No new MCP call was made after the interruption.
- The analyzer did not parse effect-derived pressure or prove the refresh helper's full modifier path. Scenario values were declared inputs and source-traced against the current helper.
- No AI project-selection or risky-option choice probability, event MTTH, recovery timing distribution, uncertain-input simulation, or multi-draw sequence was analyzed.
- No comparison was possible before the parent implementation. The required post-change comparison belongs to the parent.
- No gameplay files were edited. Only this documentation handoff is assigned to change; no unrelated changes were staged or committed.

## References reviewed

Before source review, the required offline wiki pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Technology modding. Relevant vanilla documentation reviewed included `documentation/effects_documentation.md`, `triggers_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md`, and the special-project documentation under `common/special_projects/`; the vanilla precedent was `common/special_projects/projects/air_projects.txt` and its bouncing-bomb training-accident reward. The applicable repo guidance read was `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, in addition to `AGENTS.md`.

# Event 016 Native Electronics AI Probability Audit

Date: 2026-10-03.

Disposition: unresolved pending complete probability and structural MCP coverage.

Scope: read-only review of the exact native Electronics/Radar prototype selection AI weight and a source-level expression parity check against a distinct existing paid Electronics prototype candidate.

This is a focused Event 016 AI audit checkpoint and does not certify Event 016 completion or campaign balance.

The parent review records that Electronics selection AI copied the existing policy and that probability certification remains outstanding.

No score target was accepted, no gameplay or asset file was edited, no test was run, no game was launched, and no index or commit operation was performed by this auditor.

## Audited weighted surfaces and source identity

- `mengele_event016_native_select_electronics_radar` in `common/decisions/016_mengele_native_prototype_selection_decisions.txt:32-42` is the target decision; its `ai_will_do` is at line 41.
- `mengele_event016_native_release_electronics_radar` in the same file has `ai_will_do = { base = constant:brilliant_scientist_value.zero }` at line 53.
- `mengele_event016_electronics_prototype` in `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt:14-53` is the comparison reference; its `ai_will_do` is at line 52.
- The paid Electronics decision is a distinct candidate and is not a prior definition of `mengele_event016_native_select_electronics_radar`; the before file contains no same-id native selection weight.
- The native source selector writes source code 4, which the accepted native ownership handoff maps to Electronics family 2, durable index 1, and project `sp_air_radar`.
- The native selection gate is `brilliant_scientist_mengele_can_select_native_electronics_radar` in `common/scripted_triggers/016_mengele_native_prototype_triggers.txt:117-130`.
- Its source requires the private Electronics gate, permits an unheld selection or the exact completed Radar project, and permits either exact completion or both Gotterdammerung and `electronic_mechanical_engineering`.
- `brilliant_scientist_mengele_native_electronics_private_gate` at `common/scripted_triggers/016_mengele_native_prototype_triggers.txt:37-42` requires a valid provider, completed Electronics Theory, incomplete private Electronics Prototype, and an empty Electronics decision receipt.
- `brilliant_scientist_mengele_electronics_prototype_low_factory_margin` at `common/scripted_triggers/016_mengele_remaining_conventional_prototype_decision_triggers.txt:35-37` negates `num_of_civilian_factories_available_for_projects > constant:brilliant_scientist_project_fallback_prototype.electronics_civilian_factories`; the constant value is 2 at `common/script_constants/016_brilliant_scientist_project_constants.txt:96`.
- The selection decision's visible/available wrappers are in `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt`; the parent source review describes the selection, release, receipt, provider, Theory, Prototype, and no-DLC completed-adoption conditions.
- The AI constants are centralized in `common/script_constants/016_brilliant_scientist_project_constants.txt`: `ai_high = 10` at line 76, `preferred_factor = 2` at line 288, and `cautious_factor = 0.50` at line 290.
- The local native decision source SHA-256 is `bbe8c7969a20691e5f5ba6057386732bc55672b5f1a030ec34aba842776c4757`, matching the hash recorded in `016_native_electronics_parent_review_2026-10-03.json`.
- The local comparison reference source SHA-256 is `80b52209c7267f27db004b2f9ccc63023c14be76ecb9d4f2b317a0b4fb13c98f`.
- The working tree HEAD at this audit checkpoint is `91dc29cfff8b5438eee5f3b0c1b12d353cd95e2e`; the parent review checkpoint was `a94db48a41a87065bda3f43c0287a0d02afe7dfa`.

## Source-level score findings

- The new selection expression is copied exactly from the existing Electronics prototype decision: base `constant:brilliant_scientist_project_board.ai_high`, war modifier `constant:brilliant_scientist_project_ai.preferred_factor` when `has_war = yes`, and cautious modifier `constant:brilliant_scientist_project_ai.cautious_factor` when `brilliant_scientist_mengele_electronics_prototype_low_factory_margin = yes`.
- The source constants are therefore 10, 2, and 0.50 respectively, but no numeric scenario trace is certified here because the probability evaluator has not returned.
- The release decision's zero base means the AI will not voluntarily select that decision under this source weight; whether that is intended player-only control or causes an AI lifecycle problem remains unresolved.
- These are decision willingness scores. They are not exact click probabilities, normalized selection chances, event MTTH timing distributions, or observations of live campaign behavior.
- The positive selection score is gated by decision visibility and availability. A score alone does not prove that the actor has the provider, completed Electronics Theory, an unsettled private Prototype, an empty paid receipt, DLC/technology eligibility for fresh selection, or exact-completion eligibility for no-DLC adoption.
- The source expressions establish parity with the existing paid Electronics decision, not that either policy is balanced.

## Scenario contract and completeness

The named contract is `E016_NATIVE_ELECTRONICS_AI_2026_10_03` with scenarios `quiet_ready`, `war_ready`, `low_factory_margin`, `already_selected_researching`, `selected_completed`, `paid_stage_active`, `invalid_provider`, and `no_dlc`.

The raw-score evaluation, comparison, and sweep were submitted against this same scenario-set identifier and these eight scenario ids.

For `quiet_ready`, `war_ready`, and `low_factory_margin`, the submitted state map sets `has_war` and the known low-factory-margin trigger boolean, and uses `candidateOverrides` to assume that the native selection candidate is eligible.

For `already_selected_researching`, `paid_stage_active`, `invalid_provider`, and `no_dlc`, the submitted candidate override assumes that native selection is unavailable; for `selected_completed`, it assumes native selection/adoption is available.

Every `candidateOverrides` value is a declared scoring or eligibility assumption, not a live country-state observation.

No actor tag, factory count, exact provider lifecycle state, Theory flag, private Prototype flag, paid receipt, current project activity, DLC state, technology state, AI-strategy factor, or campaign observation was supplied as a verified fact.

The probability inspection queried only the exact native selection decision id, so its `poolComplete = true` result is scoped to that one-id request and does not establish completeness of the whole conventional-program category or any live selection race.

The release candidate and other category decisions were not included in the raw-score evaluation pool; exact normalized selection probability is therefore out of scope and must not be claimed.

No scheduled state changes, uncertainty distributions, seed, cadence, custom pool, or terminal sequence were declared because this is a point-in-time decision-weight audit; no simulation or sequence analysis was requested or run.

## HOI4 MCP evidence and current route status

- `hoi4.probability_inspect` broad request used adapter `decision_ai_will_do`, source `{path:"common/decisions/016_mengele_native_prototype_selection_decisions.txt"}`, candidate pool `[mengele_event016_electronics_prototype, mengele_event016_native_select_electronics_radar, mengele_event016_native_release_electronics_radar]`, and `refresh:true`; it timed out with `tool call failed ... timed out awaiting tools/call after 600s`.
- The one narrower `hoi4.probability_inspect` request used the same adapter/source and only candidate `mengele_event016_native_select_electronics_radar`; it succeeded with code `PROBABILITY_SOURCE_INSPECTED`.
- The narrow inspect returned adapter id `decision_ai_will_do`, one candidate, `poolComplete:true` for the supplied one-id pool, zero available candidates, no required input paths, no unresolved items, MCP source hash `70a20f218d6f4ab30d7c31871635a3d97aa7c7faca25787d941ecb981f1a1ca4`, and MCP source revision `a6b46cc1cd0421ca58d7074a0e6bf711ef657734f172168da6ba5c38eeb5d050`.
- The inspect artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f85707ed74da0c218e759df07447e6e359c719c388927368f46c928e724c38a6/8514d1e1114615e8e852f665b302514e5ec3df88f7a2e83f86436be0f80727b1/probability-inspect-70a20f218d6f.json` with artifact SHA-256 `f85707ed74da0c218e759df07447e6e359c719c388927368f46c928e724c38a6` and size 17,537 bytes.
- Full-size (`offset=0,length=17535`) and narrower (`offset=0,length=1023`) byte-range reads of that artifact both failed with `Artifact provenance manifest is unavailable`; the returned structured summary is retained above, but artifact detail is inaccessible.
- `hoi4.source_lookup` found `mengele_event016_native_select_electronics_radar` at the current mod path, lines 32-42, source revision `d2d747e3ecc155e24b38b1528acdb1178642fea908c20646a88a52b374002097`.
- `hoi4.source_lookup` found `mengele_event016_electronics_prototype` at the reference path, lines 14-53, source revision `ed509b808d76be83c614110e19bd0b7259dfa74f09f8d01a3ea3be0c4edd6771`.
- `hoi4.source_lookup` found `brilliant_scientist_mengele_can_select_native_electronics_radar` at `common/scripted_triggers/016_mengele_native_prototype_triggers.txt:117-130`, source revision `26319ac8136060d956826f8551bfded9c071274a604576a1ccb01100152d4914`.
- `hoi4.source_lookup` found `brilliant_scientist_mengele_native_electronics_private_gate` at `common/scripted_triggers/016_mengele_native_prototype_triggers.txt:37-42`, source revision `ce162bde6cc9ad95a00fad34f70cbe1de8dd1c375bb316f15a77fa8cdb67668b`.
- `hoi4.source_lookup` found `brilliant_scientist_mengele_electronics_prototype_low_factory_margin` at `common/scripted_triggers/016_mengele_remaining_conventional_prototype_decision_triggers.txt:35-37`, source revision `f7c2d22b27ec7e263d178d80327ca2864119ed01795987abd2e25340fa012454`.
- `hoi4.source_lookup` found `brilliant_scientist_project_fallback_prototype.electronics_civilian_factories = 2` at `common/script_constants/016_brilliant_scientist_project_constants.txt:96`, source revision `4d262ad9d91e8139e2e659a9d6d682d2830000ecbc7066497422f1ad83c4bd54`.
- `hoi4.decision_inspect` without scenarios returned `Input validation error ... Decision inspection requires declared scenarios at scenarios` for both the native and reference ids.
- The eight-scenario structural inspect for the native and reference ids timed out after 600 seconds for both requests.
- One narrower structural retry for the native selection id with only `quiet_ready` and its candidate-eligibility override timed out after 600 seconds; the result was observed by `2026-10-03 15:39:11 UTC`.
- The eight-scenario `hoi4.probability_evaluate` request for the native selection id, current source path, and `raw_value` only timed out after 600 seconds; the result was observed by `2026-10-03 15:36:54 UTC`.
- The narrower three-scenario `hoi4.probability_evaluate` retry started at `2026-10-03 15:37:30 UTC` and timed out after 600 seconds; its result was observed by `2026-10-03 15:52:34 UTC`.
- The eight-scenario `hoi4.probability_compare` request started at `2026-10-03 15:28:46 UTC` with distinct real before and after paths and the three-id union candidate list, then timed out after 600 seconds.
- The eight-scenario `hoi4.probability_sweep` request started at `2026-10-03 15:30:02 UTC` for `ai_will_do.modifier[0].factor` and `ai_will_do.modifier[1].factor`, five steps, pairwise analysis, and rank-reversal detection, then timed out after 600 seconds.
- No evaluation scenario hash, comparison id, rendered evidence, or final/narrow-timeout result exists at this checkpoint.
- `hoi4.probability_render` has not been called because no successful evaluation, comparison, or sweep analysis id has returned.
- `hoi4.decision_inspect` and all required probability routes are exposed in the live tool list; the unresolved issue is tool-call timeout or artifact retrieval, not absent tool exposure.

## Reference evidence

- Offline wiki `Decision modding`, AI section, path `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, source id `151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, lines 357-374, was read through `hoi4.reference_read`.
- That section describes decision `ai_will_do` as an MTTH block with a starting value and ordered `add`/`factor`/`base` modifiers, and says zero by default is never selected by AI.
- `hoi4.reference_search` returned installed-game AI documentation at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\ai_faction_theaters\_documentation.md`, source id `80939d6f9556f322836b9ea7557f2eaa90b3a62ab65bf66ab0e56651e016434a`, revision `673a5237cb31e48d106f56591b360737df08586a4f4e54716b3063f59a429e89`, lines 2-37; its narrow `hoi4.reference_read` is pending.
- A separate installed-doc search for `ai_will_do` returned only unrelated operations documentation and is not used to infer decision-selection behavior.
- The vanilla `documentation/` directory was enumerated; direct `findstr` searches there found no `ai_will_do` or MTTH entry, so no decision-specific installed documentation section has been identified yet.
- The `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-mtth`, and `chaos-redux-event-planning` skills were consulted because this is a decision AI-weight audit with a parent-supplied scenario contract.

## Findings by required risk category

- AI validity: the source has a distinct availability gate and zero-cost instant selection; native fresh selection requires both Gotterdammerung and `electronic_mechanical_engineering`, while exact completed-source adoption is an explicit separate branch according to the parent source review.
- Positive weight on impossible or blocked choices: unresolved until structural scenario inspection completes; the source-level gates are visible, but no accepted engine-model result returned.
- Dominance and starvation: unresolved because the one-id raw-score pool omits the other conventional-program decisions and does not model live eligibility or AI strategy factors.
- Rank reversal: unresolved because both sweep calls timed out, and no rank result may be extrapolated outside the explicitly supplied candidate pool.
- Repetition and exploit risk: unresolved as an AI behavior claim; the parent core source handoff reports matching-selection consumption and exact-source lifecycle guards, but this does not prove live engine repetition behavior.
- Release behavior: the release decision's explicit zero weight means the AI will not choose withdrawal on its own; review whether this player-only behavior is intended if the selection can become stale.
- Snowball or unsafe campaign behavior: no such claim is supportable from this isolated AI score without the complete category pool, campaign state, and runtime observations.

## Per-scenario result classification

The only weight trace available is source-score-only: base `ai_high = 10`, war factor `2`, and low-factory-margin factor `0.50`; the MCP evaluator returned no numeric trace, ranking, or scenario hash.

| Scenario id | Submitted state and eligibility assumption | Candidate/external-factor coverage | Classification |
| --- | --- | --- | --- |
| `quiet_ready` | `has_war = false`, low-margin trigger `false`, native candidate override `true` | One target id only; provider, Theory, private Prototype, receipt, actor, strategies, and live state unverified | Score-only source facts; MCP result unresolved |
| `war_ready` | `has_war = true`, low-margin trigger `false`, native candidate override `true` | One target id only; provider, Theory, private Prototype, receipt, actor, strategies, and live state unverified | Score-only source facts; MCP result unresolved |
| `low_factory_margin` | `has_war = false`, low-margin trigger `true`, native candidate override `true` | One target id only; source threshold is 2 but actual available project factories and actor state are unverified | Score-only source facts; MCP result unresolved |
| `already_selected_researching` | Native candidate override `false` | Selection/project state is an override assumption; other category candidates and strategy inputs are omitted | Unresolved |
| `selected_completed` | Native candidate override `true` | Exact `sp_air_radar` completion and no-DLC adoption are assumptions, not observed project state | Unresolved |
| `paid_stage_active` | Native candidate override `false` | Paid receipt/activity is an eligibility assumption; other category candidates are omitted | Unresolved |
| `invalid_provider` | Native candidate override `false` | Provider validity is an eligibility assumption; lifecycle state is unverified | Unresolved |
| `no_dlc` | Native candidate override `false` | Fresh-selection DLC absence is an eligibility assumption; exact completion and other candidate availability are unverified | Unresolved |

The explicitly requested comparison candidate union is an addition comparison between distinct ids, not a complete live decision race; the full category pool and any normalized probability remain unresolved.

## Recommended follow-up, without source changes

- Do not change the copied Electronics selection score on the current evidence; the submitted full and narrowed evaluation, sweep, and comparison calls returned 600-second timeouts without numeric evidence.
- Keep the before path `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt` and after path `common/decisions/016_mengele_native_prototype_selection_decisions.txt` distinct in the comparison; do not compare the current source to itself.
- If the owner intends autonomous cleanup of an invalid or stale selection, review the zero-weight `mengele_event016_native_release_electronics_radar` policy in `common/decisions/016_mengele_native_prototype_selection_decisions.txt:53`; this audit proposes no replacement value.
- If the comparison rejects the union candidate pool because the old and new decision ids do not coexist in the respective sources, preserve that exact error and classify the numerical delta as unresolved rather than substituting a synthetic candidate or comparing against the current file itself.

## Blockers and remaining uncertainty

- Mandatory probability inspection succeeded only after narrowing to one candidate; its full artifact cannot be read because the provenance manifest is unavailable.
- Required decision structural evidence, raw score traces, sensitivity thresholds, rank reversals, and before/after comparison remain unresolved after the submitted MCP calls timed out.
- The user-supplied scenario labels do not provide verified campaign observations; candidate overrides are assumptions only.
- The full candidate pool, external AI-strategy factors, current country state, provider lifecycle, cost affordability, and runtime decision cadence remain unverified.
- No numerical selection probability, probability-proportional race, starvation certification, dominance certification, or balance certification is made.
- This handoff is a recovery checkpoint and remains unresolved until returned MCP outcomes and rendered evidence, where supported, are appended.

## Recovery update after call outcomes

This section supersedes earlier `pending` wording above where it records a later result.

The `hoi4.probability_compare` request started at `2026-10-03 15:28:46 UTC` with the real before path `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt`, real after path `common/decisions/016_mengele_native_prototype_selection_decisions.txt`, and union ids `mengele_event016_electronics_prototype`, `mengele_event016_native_select_electronics_radar`, and `mengele_event016_native_release_electronics_radar` timed out with `timed out awaiting tools/call after 600s`.

The `hoi4.probability_sweep` request started at `2026-10-03 15:30:02 UTC` for the native selection, eight named scenarios, modifier factor paths `ai_will_do.modifier[0].factor` and `ai_will_do.modifier[1].factor`, five steps, pairwise analysis, and rank-reversal detection timed out with `timed out awaiting tools/call after 600s`.

One narrower three-scenario comparison retry and one narrower three-scenario sweep retry were started at `2026-10-03 15:44:22 UTC`; both retain the real distinct before/after paths or the actual after path and later timed out after 600 seconds.

The broad eight-scenario evaluator and comparison timed out, and all three-scenario evaluation, comparison, and sweep retries also timed out.

The existing paid Electronics prototype is a distinct decision candidate from the newly added native selection; there is no exact pre-existing native-selection weight in the before file, so no same-candidate numeric before/after delta is established.

The compare request uses distinct real source files and never compares the current file to itself; if the adapter cannot handle the old/new id union, the numerical delta remains unresolved.

The source decision and comparison candidate distinction is therefore policy-expression parity evidence only, not an exact before/after weight-change proof.

The native selection source and low-margin source lookups completed with revisions recorded above, and the low-margin threshold constant is confirmed as 2 at `common/script_constants/016_brilliant_scientist_project_constants.txt:96`.

The installed-game `ai_faction_theaters` documentation was read successfully; it describes how likely AI is to create that theater and does not document decision-specific normalization.

The attempted `hoi4.reference_read` for the AI Modding MTTH section returned `REFERENCE_POSITION_OUTSIDE_SECTION` for both the over-wide request and the section-bounded retry.

The decision inspector and probability tools are exposed in this context; their returned timeouts are individual call outcomes and do not establish global tool unavailability.

No sidecar scenario count, unrelated auditor outcome, or other-head result is used as evidence in this handoff.

## Parent correction and latest route status

The parent confirms that the authoritative scenario contract is the eight-scenario `E016_NATIVE_ELECTRONICS_AI_2026_10_03` contract recorded above; evidence from another auditor's four-scenario sidecar is excluded.

The parent reports 6,752 passing current-native/later-storage source cases; this is implementation contract evidence and does not replace probability inspection, evaluation, sensitivity, comparison, or balance evidence.

The source expressions still match the recorded current source hash and the existing paid Electronics reference expression; the latter remains a distinct candidate, so same-candidate numeric delta is unresolved.

The narrower three-scenario `hoi4.probability_evaluate` request timed out after 600 seconds; the result was observed by `2026-10-03 15:52:34 UTC`.

The narrower three-scenario `hoi4.probability_compare` and `hoi4.probability_sweep` calls started at `2026-10-03 15:44:22 UTC` and timed out after 600 seconds; the outcomes were observed by `2026-10-03 15:55:40 UTC`.

A one-candidate `hoi4.probability_inspect` for the distinct existing paid Electronics reference started at `2026-10-03 15:50:24 UTC` and remains pending; it is already submitted, and no further source AI requests are being issued.

The one-candidate probability inspection of the existing paid Electronics reference is the only remaining submitted probability call to inspect.

This focused AI audit remains unresolved and does not certify the broader Event 016 goal or claim that all Event 016 simplifications have been ruled out.

## Final outcomes from the narrowed scenario retries

This section supersedes the prior three-scenario `pending` statements above.

The narrowed three-scenario `hoi4.probability_compare` timed out with `timed out awaiting tools/call after 600s`; the outcome was observed by `2026-10-03 15:55:40 UTC`.

The narrowed three-scenario `hoi4.probability_sweep` timed out with `timed out awaiting tools/call after 600s`; the outcome was observed by `2026-10-03 15:55:40 UTC`.

The `hoi4.reference_read` retry for AI Modding lines 26-37 returned `REFERENCE_POSITION_OUTSIDE_SECTION`; the Decision Modding AI section remains the successful decision-specific wiki reference.

The only still-pending probability request is the already-submitted one-candidate inspection of the distinct existing paid Electronics candidate, started at `2026-10-03 15:50:24 UTC`; it had not returned by `2026-10-03 15:55:40 UTC`.

No further probability or source AI requests are being issued after the already-submitted baseline inspection.

## Final submitted-call outcomes

The one-candidate `hoi4.probability_inspect` for `mengele_event016_electronics_prototype` against `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt`, started at `2026-10-03 15:50:24 UTC`, timed out after 600 seconds; its outcome was observed at `2026-10-03 16:01:18 UTC`.

No probability or structural MCP calls remain pending.

The only successful probability route result is the narrower source inspection for `mengele_event016_native_select_electronics_radar`; all attempted evaluations, sweeps, comparisons, and decision inspections ended in the exact timeouts recorded above.

No evaluation scenario hash, comparison id, rank or modifier trace, rendered analysis URI, or live probability result was returned.

Probability and decision-inspection tools were present in the current context's exposed tool list; these unresolved conclusions follow from the individual 600-second call timeouts and artifact provenance read failure, not a claim of global tool absence.

No `hoi4.probability_render` call was made because no successful evaluation, sweep, or comparison returned an analysis id to render.

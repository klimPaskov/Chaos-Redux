# Event 021 independent TGT probability audit

Date: 2026-09-01

Status: Blocked and incomplete. This handoff records the exact parent MCP evidence available and the interruption blocker. It is not an independent probability-auditor certificate.

## Scope

Audited surface: current Event 021 target-weight family TGT, centered on `common/scripted_effects/021_random_civil_war_effects.txt::event021_random_civil_war_prepare_target`.

Requested scenarios: `TGT-STABLE-ELIGIBLE`, `TGT-WEAK-ELIGIBLE`, and `TGT-INELIGIBLE-ZERO`.

No gameplay, AI, event, focus, decision, mission, localisation, or runtime source was edited. No commit was created.

## Files and instructions reviewed

- `AGENTS.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`.
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_tgt_parent_diagnostic_2026-09-01.md`.
- `common/scripted_effects/021_random_civil_war_effects.txt::event021_random_civil_war_prepare_target`.
- `common/scripted_triggers/021_random_civil_war_triggers.txt::event021_country_can_be_target`.
- `common/script_constants/021_random_civil_war_constants.txt::random_civil_war_target_weight` and `::event021_parent_tuning`.
- Relevant offline Paradox wiki AI, data-structure, trigger, effect, modifier, scope, event, and on-action references, plus the installed vanilla script, trigger, modifier, effect, and concept documentation.

## MCP execution and blocker

Independent MCP calls made: none.

The mandatory first call, `mcp__hoi4_agent_tools__hoi4_probability_inspect`, was not executed because the user interrupted the audit before the first callable HOI4 MCP call. Therefore there is no independent inspect result, MCP source revision, independent source hash, or independent inspect artifact URI.

No independent `mcp__hoi4_agent_tools__hoi4_probability_evaluate` call was executed. Therefore there is no independent analysis id, scenario hash, evaluation artifact URI, or independent raw trace.

The exact required two-call operation was to inspect the `custom_weighted_pool` adapter with the validated Event 021 TGT `customPoolManifest`, then evaluate the same manifest over the three named fixtures. The manifest JSON body is not recorded in the named parent diagnostic, so synthesizing a different manifest after interruption would not satisfy the exact-manifest requirement.

## Parent MCP evidence retained for provenance

The parent diagnostic reports this first call, but it was not made by this independent auditor:

```text
hoi4.probability_inspect
adapter: custom_weighted_pool
customPoolManifest: validated Event 021 TGT manifest
refresh: true
workspaceId: mod_chaos_redux_ea3b2d67c2c0
```

Reported parent result: `PROBABILITY_SOURCE_INSPECTED`, one complete declared candidate, zero unresolved inputs, source hash `8132d1cc046b40c885799b1dcd5d05a6980925bac4202fe1256b131a8f43dab2`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83d072d8ae2a74aea75637659ef3f0ebaf5cf6853a8f482f26333b82964a8952/52ea2288aa8db6656afe73731d8ffcd96ae4172cead12ca968731e15856730ed/probability-inspect-8132d1cc046b.json`.

The parent diagnostic reports this second call, but it was not made by this independent auditor:

```text
hoi4.probability_evaluate
adapter: custom_weighted_pool
customPoolManifest: the same validated Event 021 TGT manifest
scenarioSet: TGT-STABLE-ELIGIBLE, TGT-WEAK-ELIGIBLE, TGT-INELIGIBLE-ZERO
workspaceId: mod_chaos_redux_ea3b2d67c2c0
```

Reported parent result: analysis `probability-75458d26511189833fd24427`, scenario hash `29240122aa242e26156dda7b172370506bbb5823b14d53054c5fd0566feeb8f9`, zero unresolved evidence, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c55b09805cb98885e7b2881831e92bd9dd49b233af6d30b80bc117acbe64b72/44399017e8619eae29d8136e70ddc77f3d389e32b2fb1ccd8c4a9d7fd986f820/probability-75458d26511189833fd24427.json`.

The parent diagnostic does not record the MCP source revision. The current local file hashes observed before the interruption were `7F78C38901B068BC7C2913C11F4E3C3CA6D237AA462ACD37AB2465D01C2D1950` for `common/scripted_effects/021_random_civil_war_effects.txt` and `8506E12120C0E81F69A2DEBAE69B6CC9B7A47EB2E7E87CE778DC6971FB1A9515` for `common/script_constants/021_random_civil_war_constants.txt`. These local hashes are not interchangeable with the parent MCP source hash.

## Target arithmetic and parent-reported fixture results

The current helper initializes `event021_target_weight` to `random_civil_war_target_weight.base`, adds the pressure component multiplied by `pressure_per_point`, applies the conditional authority, route, evidence, fragmentation, occupation, manpower, Event 006, major-stage, nearby-exposure, recent-memory, and subject terms, then clamps to the centralized minimum and maximum and rounds the result.

The relevant current constants are base `10`, pressure multiplier `4`, failing-authority addition `90`, collapsed-authority addition `160`, valid-actor-route addition `80`, evidence-strength multiplier `12`, state-fragmentation addition `45`, occupied addition `70`, weak-manpower addition `35`, Event 006 package addition `45`, major-stage addition `50`, nearby-exposure addition `60`, recent-memory addition `-120`, subject addition `20`, minimum `0`, and maximum `1000`.

The invalid target branch sets the score to the minimum. A reserved target is also forced to the minimum. The helper publishes `random_civil_war_target_pool_candidate` only when the final score is greater than the minimum, so the score and the candidate eligibility gate must remain separate in review.

| Scenario | Parent-reported raw weight | Parent-reported eligibility | Parent-reported conditional probability | Independent classification |
| --- | ---: | --- | ---: | --- |
| `TGT-STABLE-ELIGIBLE` | 122 | true | 1 | Unresolved independently. Parent evidence is exact for its one-candidate declared manifest. |
| `TGT-WEAK-ELIGIBLE` | 916 | true | 1 | Unresolved independently. Parent evidence is exact for its one-candidate declared manifest. |
| `TGT-INELIGIBLE-ZERO` | 0 | false | 0 | Unresolved independently. Parent evidence reports the fail-closed zero. |

## Candidate-pool and external-factor completeness

The parent reports a complete declared custom manifest containing one abstract target candidate and explicit zero-or-one scenario inputs for boolean source branches. That is complete for the parent diagnostic's one-candidate score model.

It is not a complete live country target pool. The three fixture results must not be restated as automatic Event 021 launch probabilities or as campaign-wide target shares. The one-candidate `1` values are conditional shares inside that diagnostic pool and do not establish multi-country dominance, starvation, or target-selection frequency.

The parent reports zero unresolved inputs inside its evaluation. Because this independent auditor did not execute the call, the independent external-factor status is unresolved and the parent declaration remains the only available evidence.

## Findings

- The parent result preserves live weight for the stable eligible fixture and reports a substantially larger live weight for the weak eligible fixture.
- The parent result reports exact zero and ineligibility for the invalid fixture, consistent with the current helper's fail-closed minimum and candidate-flag gate.
- The parent result's dominance warning for eligible fixtures is expected for a one-candidate abstract pool and does not prove a competing-country imbalance.
- No independent evidence exists for starvation, rank reversal, repetition, long-run target timing, cooldown recovery, or campaign-level exploit risk because the requested two-call independent MCP pass did not execute and no sequence manifest was requested.
- These are score and conditional one-candidate pool results, not click probabilities or automatic event probabilities.

## Recommended follow-up, not applied

The owner should rerun the exact validated TGT `customPoolManifest` through an independent `probability_inspect` call followed by one `probability_evaluate` call over the same three scenario ids, then preserve the fresh MCP source revision, source hash, analysis id, scenario hash, artifact URIs, raw traces, and unresolved-input counts in a replacement certificate.

If the exact manifest is needed for reproduction, persist its JSON body alongside the parent diagnostic before the next audit. Do not substitute a reconstructed manifest whose canonical hash differs from `8132d1cc046b40c885799b1dcd5d05a6980925bac4202fe1256b131a8f43dab2`.

No source tuning recommendation is justified by this interrupted independent pass. Any later owner patch to `event021_random_civil_war_prepare_target` or `random_civil_war_target_weight` constants must use the same named fixtures and a post-change probability comparison.

## Skipped analyses and remaining uncertainty

- Independent `hoi4.probability_inspect`: skipped because the user interrupted before the first MCP call.
- Independent `hoi4.probability_evaluate`: skipped because the mandatory inspect call did not execute.
- `probability_sweep`, `probability_compare`, `probability_sequence`, `probability_simulate`, and `probability_render`: not run because the user required immediate termination after the two-call audit and no independent baseline existed.
- MCP source revision for the parent artifact: not present in the named parent diagnostic.
- Exact validated manifest JSON: not present in the named parent diagnostic, so independent canonical-manifest reproduction is unresolved.

This handoff is therefore a blocked read-only record, not a completion claim.

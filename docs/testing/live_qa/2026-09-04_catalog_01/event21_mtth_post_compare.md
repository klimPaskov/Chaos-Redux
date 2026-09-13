# Event 021 MTTH post-patch comparison

Audit date: 2026-09-05.

Audit status: **Source correction confirmed; MCP probability and comparison result unresolved because the installed timing adapter exposes no reusable MTTH surface.**

The owner applied the approved one-token trigger correction in `common/mtth/021_random_civil_war_mtth.txt`. This report records the read-only post-patch inspect, evaluation, and mandatory same-scenario comparison. No gameplay source was edited by this audit, and no game, staging, or commit operation was performed.

## Patch boundary and source identity

The archived pre-patch body is `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_mtth/common/mtth/021_random_civil_war_mtth.txt`.

The current post-patch body is `common/mtth/021_random_civil_war_mtth.txt`.

The archived pre-patch local SHA-256 is `74F9B639A53B2DDB1845DB23BDCF72B5731B2562FA7740455F86480A54CE5623`.

The current post-patch local SHA-256 is `6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F`.

Both files contain 93 lines. A line-by-line comparison found exactly one changed line:

```text
before: any_neighbor_country = { stability > constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold }
after:  any_neighbor_country = { has_stability > constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold }
```

The comparator remains strict `>`, the threshold remains `constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold`, the enclosing scope remains `any_neighbor_country`, and `strong_neighbor_factor` is unchanged. This is a parser-validity correction with no base, factor, threshold, cadence, clamp, or route-tuning change.

## Exact scenario contract reused

The same scenario family, scenario IDs, state values, flags, metrics, and 365-day horizon from the baseline report were reused without alteration.

Scenario family: `event021_mtth_evolution_ii_neighbor_stability_baseline_20260905`.

```json
{
  "schemaVersion": "1.0",
  "id": "event021_mtth_evolution_ii_neighbor_stability_baseline_20260905",
  "scenarios": [
    {
      "id": "EVO2-02-LOW-NEIGHBOR-STABILITY",
      "state": {"neighbor_count": 1, "neighbor_stability": 0.64},
      "flags": []
    },
    {
      "id": "EVO2-02-AT-THRESHOLD",
      "state": {"neighbor_count": 1, "neighbor_stability": 0.65},
      "flags": []
    },
    {
      "id": "EVO2-02-HIGH-NEIGHBOR-STABILITY",
      "state": {"neighbor_count": 1, "neighbor_stability": 0.66},
      "flags": []
    }
  ]
}
```

`flags: []` fixes the five other Evolution II flags false in every fixture: `random_civil_war_land_border_exposure_ready`, `random_civil_war_sponsor_commitment_active`, `random_civil_war_event6_front_active`, `random_civil_war_multifront_active`, and `random_civil_war_settlement_phase`.

The declared external factors are one abstract neighboring country, the indicated stability value, no scheduled state changes, no random seed, and a 365-day horizon. The surface is an MTTH timing helper and has no normalized candidate pool.

The nested neighbor scope remains an adapter limitation. The fixture declares the neighbor state, but MCP does not currently bind it to a reusable `common/mtth` entry, so external-factor completeness is declared but not engine-proven.

## Post-patch MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The mandatory post-patch `hoi4.probability_inspect` call used adapter `event_mean_time_to_happen`, source `{identifier: "random_civil_war_evolution_ii_days", path: "common/mtth/021_random_civil_war_mtth.txt"}`, and `refresh: true`.

Inspect returned status `ok` and code `PROBABILITY_SOURCE_DISCOVERED`.

The inspect result scanned `mod:common/mtth/021_random_civil_war_mtth.txt` and returned `discoveryReason: identifier_not_found`, `candidates: 0`, `availableCandidates: 0`, `requiredInputs: 0`, and `unresolved: 0`.

The post-patch MCP source revision is `075fa4ce3cde0377f0140faa984427e99d66d46f0e8214a46ac6a77c2597d202`.

The post-patch MCP source hash is `c55a108bcbf249ce1d76875506cd0fe4b8c8db79646c426b503ba036d72405b8`.

The post-patch inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aedfe85523609e5706ec63c035f5ac0eb51a9340b13786f0cfdc60ae3f98f2a3/ef8941840f44833687d14a8b3e0775c2c93eb375b90aa5cc32ca23adfe7970a2/probability-inspect-c55a108bcbf2.json` with artifact SHA-256 `aedfe85523609e5706ec63c035f5ac0eb51a9340b13786f0cfdc60ae3f98f2a3`.

The post-patch `hoi4.probability_evaluate` call used the same source identifier, the same scenario family and three IDs, metrics `raw_value`, `effective_mtth_days`, and `cumulative_chance`, outputs `json`, `timing`, and `unresolved`, and `horizonDays: 365`.

Evaluation returned status `error`, code `PROBABILITY_SURFACE_EMPTY`, `filesScanned: []`, no analysis ID, no scenario hash, no source revision, no artifact, and the blocker `No weighted blocks matched this request` with `candidatePool: []` and `availableAdapters: []`.

The post-patch evaluation therefore produces no score, effective MTTH, cumulative chance, timing distribution, or scenario-specific result for any of the three IDs.

## Mandatory same-scenario comparison

The `hoi4.probability_compare` call used adapter `event_mean_time_to_happen`, identifier `random_civil_war_evolution_ii_days`, and the same `common/mtth/021_random_civil_war_mtth.txt` path for both sides.

The before side supplied the complete archived body through `inlineClausewitz` from `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_mtth/common/mtth/021_random_civil_war_mtth.txt`.

The after side supplied the complete current body through `inlineClausewitz` from `common/mtth/021_random_civil_war_mtth.txt`.

The compare reused the exact scenario family and all three IDs above, with `horizonDays: 365` and outputs `json`, `comparison`, `timing`, and `unresolved`.

The exact compare result was:

```text
status: error
code: PROBABILITY_SURFACE_EMPTY
filesScanned: []
artifacts: []
validation.passed: false
blocker.code: PROBABILITY_SURFACE_EMPTY
blocker.message: No weighted blocks matched this request
blocker.details: {"truncated":true}
data: {}
```

No comparison ID, before/after analysis ID, compare artifact, compare scenario hash, or compare source revision was emitted. The empty baseline surface prevents the adapter from attributing a before/after timing result, even though the complete archived and current source bodies were supplied.

The comparison was attempted with genuine before and after bodies. No baseline analysis ID was invented or substituted from the prior empty evaluation.

## Source-only interpretation

The documented `has_stability` trigger is now present at line 69, and the source-level threshold semantics are unchanged: `0.64` and exactly `0.65` do not satisfy strict `> 0.65`, while `0.66` does if a neighbor binds to the nested scope.

With the five route and phase flags false, the conditional source trace remains `135 × 1.25 = 168.75` nominal days when the strong-neighbor condition is false and `135 × 1.25 × 1.25 = 210.9375` nominal days when it is true. These are source traces only, not post-patch MCP timing results.

The parser correction does not alter any source numeric value or modifier branch. No dominance, starvation, repetition, rank-reversal, exploit-risk, or balance conclusion is supported by this post-patch MCP pass.

## Disposition and remaining blocker

The approved syntax correction is ready for the parent’s native launch/parser verification.

The probability audit remains unresolved for effective timing because the installed `event_mean_time_to_happen` adapter does not expose reusable entries in `common/mtth/*.txt` as evaluable weighted blocks before or after the correction.

`hoi4.probability_render` was not called because post-evaluation and compare produced no analysis ID or renderable artifact.

`hoi4.probability_sweep` was not repeated after patch because the baseline and post-patch timing surfaces both returned `PROBABILITY_SURFACE_EMPTY`; no valid continuous surface exists to sweep.

`hoi4.probability_simulate` and `hoi4.probability_sequence` remain inapplicable because no uncertain-input distribution or complete custom pool cadence/state-transition manifest exists.

No simplification or fallback was used.

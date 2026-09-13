# Event 021 MTTH parser baseline

Audit date: 2026-09-05.

Audit status: **MCP timing result unresolved; scoped parser correction recommended.**

This is a read-only baseline for the confirmed invalid trigger in the Evolution II timing helper. No gameplay source, AI value, prerequisite, route gate, localisation, asset, workbook, or runtime file was changed, and no commit was made.

## Audited surface

The exact weighted surface is `random_civil_war_evolution_ii_days` in `common/mtth/021_random_civil_war_mtth.txt`.

The owning source block begins at line 44 and has `base = constant:random_civil_war_evolution_mtth.evolution_ii_base_days` at line 45.

The reported parser defect is line 69:

```text
any_neighbor_country = { stability > constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold }
```

The documented trigger form is:

```text
any_neighbor_country = { has_stability > constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold }
```

The scoped correction preserves the strict `>` comparator, the threshold constant, the `any_neighbor_country` scope, the `strong_neighbor_factor`, and every other modifier. It is a syntax and parser-validity correction only, with no tuning change.

The current MTTH file SHA-256 is `74F9B639A53B2DDB1845DB23BDCF72B5731B2562FA7740455F86480A54CE5623`.

The source constants in `common/script_constants/021_random_civil_war_constants.txt` are `evolution_ii_base_days = 135`, `strong_neighbor_stability_threshold = 0.65`, `strong_neighbor_factor = 1.25`, and `no_exposure_route_factor = 1.25`.

The source has five other Evolution II modifiers: land-border exposure at `0.75`, sponsor commitment at `0.75`, Event 006 front at `0.80`, multi-front pressure at `0.85`, and settlement progress at `1.40`.

With all five route and phase flags absent, the source-wise nominal trace is `135 × 1.25 = 168.75` days when the neighbor condition is false, and `135 × 1.25 × 1.25 = 210.9375` days when at least one neighbor satisfies strict stability greater than `0.65`.

Those values are conditional source traces only. `event021_parent_schedule_evolution_due_date` in `common/scripted_effects/021_random_civil_war_parent_effects.txt` samples the helper and applies the separate configured delay bounds, so no sampled or effective timing distribution is claimed here.

## QA evidence

The fresh launch log is `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_07/logs/error.log`.

The relevant entries are:

```text
[09:57:41][no_game_date][trigger.cpp:700]: Invalid trigger 'stability' in common/mtth/021_random_civil_war_mtth.txt line : 69
[09:57:41][no_game_date][trigger.cpp:568]: Error: "Unknown trigger-type: stability, near line: 69" in file: "common/mtth/021_random_civil_war_mtth.txt" near line: 69
```

The same log contains a separate `stability` error at `common/scripted_effects/021_random_civil_war_parent_effects.txt:5150`. That finding is outside this baseline and was not analyzed or folded into the recommendation.

## Documentation evidence

The offline wiki `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:321-322` documents country-scoped `has_stability` with `<float>/<variable>` values and the example `has_stability > 0.5`.

The offline wiki `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:187-189` documents strict `>` and `<` comparisons.

The vanilla documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:4800-4807` lists `has_stability`, its supported country scope, and a stability comparison example.

The offline wiki `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:28-36` describes MTTH base values and multiplicative factor modifiers. This surface is a timing MTTH, not a normalized candidate-selection pool or click probability.

## Declared scenarios

The scenario family is `event021_mtth_evolution_ii_neighbor_stability_baseline_20260905`.

The exact fixture submitted to MCP was:

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

`flags: []` fixes these source flags false in every fixture: `random_civil_war_land_border_exposure_ready`, `random_civil_war_sponsor_commitment_active`, `random_civil_war_event6_front_active`, `random_civil_war_multifront_active`, and `random_civil_war_settlement_phase`.

The declared external factors are one abstract neighboring country, the indicated stability value, no scheduled state changes, no seed, and a 365-day evaluation horizon.

The MTTH surface has no normalized candidate pool, so candidate-pool completeness is not applicable at the source level. The MCP adapter nevertheless discovered zero candidates, and it cannot currently bind the nested `any_neighbor_country` state. Therefore the external-factor fixture is declared but not engine-complete, and all three effective timing results remain unresolved.

At `0.64`, the strong-neighbor condition is source-wise false; at exactly `0.65`, it is also source-wise false because the comparator is strict; at `0.66`, it is source-wise true if the declared abstract neighbor binds to the nested scope. These are source semantics, not MCP timing results.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The mandatory read-only `hoi4.probability_inspect` call used adapter `event_mean_time_to_happen` and source `{identifier: "random_civil_war_evolution_ii_days", path: "common/mtth/021_random_civil_war_mtth.txt"}` with `refresh: true`.

Inspect status was `ok` with code `PROBABILITY_SOURCE_DISCOVERED`.

The inspect result scanned `mod:common/mtth/021_random_civil_war_mtth.txt` and returned `discoveryReason: identifier_not_found`, `candidates: 0`, `availableCandidates: 0`, `requiredInputs: 0`, and `unresolved: 0`.

The inspect MCP source revision is `bc24926cdf8eb9dfcd4c574215be8d07fc3413137653f1664b9711ec7eb32c01`.

The inspect MCP source hash is `7c2d8c672898d42045a6543526cb81991fb6fe48e8f731b772b930f99119cad2`.

The authoritative inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/115b63b1e68789ea7b885f6a87d2eb1c92257a7cb7a0569376c768bfa3feaef5/8325c99ee50499f27d3e06dd69816c38dbee3aca10a931dc65ef83531919abd8/probability-inspect-7c2d8c672898.json` with artifact SHA-256 `115b63b1e68789ea7b885f6a87d2eb1c92257a7cb7a0569376c768bfa3feaef5`.

The required `hoi4.probability_evaluate` call used the same adapter and source, the exact scenario family above, the three named scenarios, metrics `raw_value`, `effective_mtth_days`, and `cumulative_chance`, outputs `json`, `timing`, and `unresolved`, and `horizonDays: 365`.

Evaluation returned status `error`, code `PROBABILITY_SURFACE_EMPTY`, no files scanned, no analysis id, no scenario hash, no source revision, no artifact, and the blocker message `No weighted blocks matched this request` with `candidatePool: []` and `availableAdapters: []`.

The required `hoi4.probability_sweep` call used the same source and scenario family with `state.neighbor_stability` as the three-step sweep path, with threshold and sensitivity outputs requested.

The sweep returned the same status `error`, code `PROBABILITY_SURFACE_EMPTY`, no analysis id, no scenario hash, no artifact, and the same blocker `No weighted blocks matched this request`.

The initial two inspect attempts used unsupported source shapes and were rejected before analysis: `relativePath` and `entryId` were unrecognized under `source`, and a string source was rejected because an object was required. The corrected `{identifier, path}` source shape produced the successful inspect result above.

## Results and classifications

| Scenario | Declared stability | Source-wise strong-neighbor gate | MCP result | Classification |
| --- | ---: | --- | --- | --- |
| `EVO2-02-LOW-NEIGHBOR-STABILITY` | 0.64 | False | No weighted surface matched | `unresolved` for effective timing; conditional source trace only |
| `EVO2-02-AT-THRESHOLD` | 0.65 | False under strict `>` | No weighted surface matched | `unresolved` for effective timing; conditional source trace only |
| `EVO2-02-HIGH-NEIGHBOR-STABILITY` | 0.66 | True only if nested neighbor binding is accepted | No weighted surface matched | `unresolved` for effective timing; conditional source trace only |

No exact or bounded MCP MTTH, cumulative chance, ranking, timing distribution, dominance, starvation, repetition, or rank-reversal result exists for this entry.

The only confirmed defect is parser validity of the trigger key. There is no evidence in this baseline for changing the base, factor, threshold, cadence, clamp, or any adjacent weighted surface.

## Recommended owner action

At `common/mtth/021_random_civil_war_mtth.txt:69`, replace `stability` with `has_stability` and preserve the existing `> constant:random_civil_war_evolution_mtth.strong_neighbor_stability_threshold` expression.

After the owner applies that syntax-only correction, rerun `hoi4.probability_inspect` and `hoi4.probability_evaluate` with this exact source identifier, scenario-set id, scenario ids, fixed flags, and horizon. Then run the mandatory `hoi4.probability_compare` on the same three scenario ids and preserve its before and after revisions, scenario hash, comparison id, and rendered evidence.

## Skipped analyses and blockers

`hoi4.probability_render` was not called because both inspect/evaluate sensitivity routes produced no analysis id or renderable artifact; the unresolved MCP blocker is preserved verbatim above.

`hoi4.probability_simulate` was not applicable because no uncertain input distribution or complete live timing surface exists, and no seed was declared.

`hoi4.probability_sequence` was not applicable because this is a reusable MTTH entry rather than a complete custom weighted pool with cadence, transitions, recovery, cooldowns, removals, resets, and terminal states.

`hoi4.probability_compare` is intentionally deferred to the parent after the owner-applied correction; no before/after source revision was invented.

Event structural inspect/render was not run because this audit is limited to the reusable MTTH parser surface and does not certify the Event 021 event-chain graph.

The adapter limitation is the remaining blocker: the installed `event_mean_time_to_happen` route does not expose reusable entries in `common/mtth/*.txt` as evaluable weighted blocks. Source review supports the correction and the strict-threshold semantics, but it cannot substitute for the missing MCP timing evidence.

No simplification or fallback was used.

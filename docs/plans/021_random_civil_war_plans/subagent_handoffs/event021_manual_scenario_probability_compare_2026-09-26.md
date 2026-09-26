# Event 021 Manual Scenario Country-Selection Post-Change Comparison

Date: 2026-09-26.

Disposition: `unresolved` for probability delta. The post-edit source inspect is current, but the custom-pool adapter still does not discover a complete candidate pool or represent the required campaign states. `hoi4.probability_compare` was not called because no supported, complete scenario set can be built from the available evidence.

No gameplay source was edited during this pass. This report is separate from the baseline handoff so the baseline record remains intact.

## Before and after source identities

| Side | Exact source path | Raw file SHA-256 | MCP source identity and artifact |
| --- | --- | --- | --- |
| Before | `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_parent_effects_current_worktree_capture_2026-09-26.txt` | `B9D5002AF433C4CBC33D2BE3641B63239D3ABCC0DBDA5E030E09D8DB8D599A3C`, verified from the file. | Baseline source revision `ea4669159bc268bcacb07b26a88c4b151990475a45248e401b6d1d6fd5936617`, source hash `6bd965bf376ee70c602e9fcd4f6d0e805be135d7ce10c2ed493c04566070c513`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cdae552a308846be0508861140f802cde624097fcfd0fb285c40c4598abad31/87eef4d593b895e9670c84cd6053075617b99cfa5bc8d5b7a8b039c4fd3aec49/probability-inspect-6bd965bf376e.json`. |
| After | `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `6D736B9413913F1C232DDDC8302F6F7D7C53143D52A01FA1A53D15DDCE3E15DF`, verified from the file. | Post-edit source revision `18b4807db5579a6dc63c42d11525e6ef3998e5ccbf5d57465c94f13ff02d04d6`, source hash `65cbdeafa54f422789e4491a22b40b80a2fc977a3e9636f65ad980ef7f7b8df0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bb8c34fec2a189564f2a6af83bea99232bde144606d99f04785f8116d7d3cb2/f0138dc3936b26811507e58b04eb8aeda2e8496ffe5f7379b2354a5d6eb0e9b1/probability-inspect-65cbdeafa54f.json`. |

The before and after raw file hashes match the supplied identities. The MCP source hashes and revisions are preserved as separate analyzer identities.

## Post-edit MCP inspect

The required first post-change call was `hoi4.probability_inspect` with adapter `custom_weighted_pool` and source `{ path: "common/scripted_effects/021_random_civil_war_parent_effects.txt" }`.

- Result: `PROBABILITY_SOURCE_INSPECTED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`.
- Adapter data: `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `availableAdapters=[]`, `requiredInputs=0`, and `unresolved=0`.
- `filesScanned`: `mod:common/scripted_effects/021_random_civil_war_parent_effects.txt`.
- Artifact URI and source identity are recorded in the after row above.

The empty discovery result is not a complete empty campaign pool. `poolComplete=false` means the analyzer did not establish the candidate roster. `requiredInputs=0` and `unresolved=0` do not establish that the runtime country scopes, derived Clausewitz variables, or external eligibility gates were represented.

## Source-level change confirmed

The pre-edit capture initializes `event021_parent_scenario_remove_tickets` from `constant:individual_crisis_targeting.load_zero_tickets` and runs four `remove_from_temp_array` calls by selected-country value.

The post-edit draw calls `event021_parent_remove_scenario_target_tickets`. That helper initializes `event021_parent_scenario_ticket_scan_index` from the current `event021_parent_scenario_target_pool^num`, decrements the index before each check, compares the indexed scope with the selected country event target, and removes matching entries by index. This is a descending scan bounded by the current pool size and removes the selected country's remaining ticket entries from the live array before the next draw.

The manual selection base weights, scenario budget shares, and load factors are unchanged in the reviewed selection path. The source change removes the prior conditional residual-ticket/reselection path at source level. This confirms the scripted behavior delta only. It does not establish a numeric selection-probability delta or runtime engine outcome.

## Named scenario coverage

The comparison uses the same five scenario IDs from the baseline handoff. No scenario set was submitted, so none has a scenario hash or evaluated before/after result.

| Scenario ID | Before/after candidate-pool completeness | Required inputs still unavailable | Classification |
| --- | --- | --- | --- |
| `E021-MANUAL-EMPTY-POOL-2026-09-26` | Incomplete on both sides. Adapter discovery did not prove an empty runtime pool. | Complete country enumeration and all eligibility gate values. | Unresolved. |
| `E021-MANUAL-SINGLE-HIGH-LOAD-2026-09-26` | Incomplete on both sides. No actual candidate country or manifest was supplied. | Country tag, major status, scenario type/intensity, derived shared load, eligibility flags, queue/reservation state, controlled states, and route/opening-state validity. | Unresolved. |
| `E021-MANUAL-SEVERAL-UNEVEN-LOAD-2026-09-26` | Incomplete on both sides. The full country roster and ticket multiplicities are unavailable. | Every candidate tag, major status, provider markers and derived load, scenario type/intensity, and all eligibility gates. | Unresolved. |
| `E021-MANUAL-SELECTED-COUNTRY-REMAINS-2026-09-26` | Incomplete on both sides. No complete pre-draw ticket array was represented. | Full candidate array, per-country adjusted tickets, draw budget, and live eligibility values. | Source-level change confirmed. Probability delta unresolved. |
| `E021-MANUAL-EVENT006-PACKAGES-2026-09-26` | The 32-ID package allowlist is source-enumerable, but the available package subset and the weighted country roster are incomplete. | Registry initialization, cursor and reservations, actor readiness, valid anchor ownership/state, scenario type, and country/load/eligibility state. | Unresolved. |

The adapter contract documented for this connected route accepts scenario actors, flat primitive state, flags, and explicitly named scopes. It does not bind typed Clausewitz numeric variables or compound triggers. The five case descriptions and baseline handoff do not provide actual candidate tags, complete country rosters, or exact runtime state. No scenario fixture, country tag, or candidate weight was invented.

The source-complete Event 006 adapter package ID list and the detailed per-scenario input gaps are preserved in the [baseline handoff](event021_manual_scenario_probability_baseline_2026-09-26.md).

## Comparison result and skipped routes

`hoi4.probability_compare` requires a `scenarioSet`. The live tool schema exposes that field as required, while the available evidence cannot populate a complete and honest set for these dynamic pools. The compare call was therefore skipped, not attempted and rejected. There is no comparison ID, compare artifact, scenario hash, numeric delta, or rendered comparison view.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, and `hoi4.probability_sequence` were also not run. Their scenario traces require the same unavailable candidate pool and runtime values. `hoi4.probability_simulate` was not run because no uncertain-input distributions or seed were declared. `hoi4.probability_render` was not run because no analysis ID exists to render.

Result class: `exact` for the supplied and verified file hashes, direct inspect fields, and the source-level removal-loop change. `unresolved` for all before/after probability values, rankings, dominance, starvation, rank reversal, repetition frequency, and numerical delta. No sampled or score-only output was produced. The inspect artifacts are adapter/source discovery evidence and do not certify a probability comparison.

No balance approval or Event 021 completion claim is made. The source change closes the fixed-four residual-ticket mechanism in the reviewed code, while its probability impact remains unmeasured by the MCP adapter.

# Event 021 Manual Scenario Country-Selection Post-Change Comparison

Date: 2026-09-26.

Disposition: `unresolved` for probability delta. The refreshed post-edit inspect still reports an incomplete custom pool. The first compare attempt was rejected because the five scenarios omitted `state`; a follow-up schema-correct probe was accepted but returned partial `random_list` analysis rather than the requested custom pool, with no campaign probability evidence.

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

Repetition and exploit risk: before the change, a selected country with more tickets than the fixed removal count could remain in the pool for a later draw when the budget allowed another draw. The new helper removes every matching ticket from the remaining pool, closing that source-level repeated-selection path. Repetition frequency and downstream duplicate-plan or commit safety remain unmeasured.

## Source weights and modifier trace

The source assigns base tickets by intensity and major status as follows: Low uses minor 4 and major 1, Medium uses 2 and 2, and High uses minor 1 and major 3. The manual draw-budget shares are Low 0.10, Medium 0.25, High 0.50, and Maximum 1.00; Maximum bypasses weighted sampling and copies every eligible country once.

`adjust_individual_crisis_candidate_ticket_weight` passes each base value through `individual_crisis_apply_candidate_ticket_curve`: active load zero multiplies by `load_zero_tickets = 4`, load one by `load_one_tickets = 2`, and load two by `load_two_tickets = 1`; the shared eligibility cap is `active_cap = 3`. These are source values only; MCP produced no per-candidate adjusted tickets, modifier trace, ranking, or probability.

The source uses repeated country scopes as ticket entries and `random_scope_in_array` for the draw, so this is a probability-proportional ticket pool rather than an `ai_will_do` score race, event-option `ai_chance`, or MTTH timing surface. The candidate predicate does not require `is_ai = no`, so eligible AI-controlled normal countries may be in the pool. AI willingness validity is not applicable to this manual selection surface.

The reviewed weighted-surface sources are `common/scripted_effects/021_random_civil_war_parent_effects.txt` (`event021_parent_add_scenario_target_to_weighted_pool`, `event021_parent_remove_scenario_target_tickets`, and `random_civil_war_trigger_manual_scenario`), `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` (`event021_parent_scenario_country_eligible`, type and opening-state preflights, and `event021_parent_event6_dormant_candidate`), `common/scripted_triggers/021_random_civil_war_triggers.txt` (`random_civil_war_is_normal_human_country`), `common/scripted_effects/individual_crisis_targeting_effects.txt` (`adjust_individual_crisis_candidate_ticket_weight` and `individual_crisis_apply_candidate_ticket_curve`), `common/scripted_triggers/individual_crisis_targeting_triggers.txt` (`individual_crisis_load_is_below_cap` and derived provider load), `common/script_constants/021_random_civil_war_constants.txt`, `common/script_constants/individual_crisis_targeting_constants.txt`, and `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` (static Event 006 package allowlist and actor mapping).

## Named scenario coverage

The compare attempt used the same five scenario IDs from the baseline handoff. No scenario hash or evaluated before/after result was produced.

| Scenario ID | Before/after candidate-pool completeness | Required inputs still unavailable | Classification |
| --- | --- | --- | --- |
| `E021-MANUAL-EMPTY-POOL-2026-09-26` | Incomplete on both sides. Adapter discovery did not prove an empty runtime pool. | Complete country enumeration and all eligibility gate values. | Unresolved. |
| `E021-MANUAL-SINGLE-HIGH-LOAD-2026-09-26` | Incomplete on both sides. No actual candidate country or manifest was supplied. | Country tag, major status, scenario type/intensity, derived shared load, eligibility flags, queue/reservation state, controlled states, and route/opening-state validity. | Unresolved. |
| `E021-MANUAL-SEVERAL-UNEVEN-LOAD-2026-09-26` | Incomplete on both sides. The full country roster and ticket multiplicities are unavailable. | Every candidate tag, major status, provider markers and derived load, scenario type/intensity, and all eligibility gates. | Unresolved. |
| `E021-MANUAL-SELECTED-COUNTRY-REMAINS-2026-09-26` | Incomplete on both sides. No complete pre-draw ticket array was represented. | Full candidate array, per-country adjusted tickets, draw budget, and live eligibility values. | Source-level change confirmed. Probability delta unresolved. |
| `E021-MANUAL-EVENT006-PACKAGES-2026-09-26` | The 32-ID package allowlist is source-enumerable, but the available package subset and the weighted country roster are incomplete. | Registry initialization, cursor and reservations, actor readiness, valid anchor ownership/state, scenario type, and country/load/eligibility state. | Unresolved. |

The adapter contract documented for this connected route accepts an actor string, flat primitive state, flags, and explicitly named scopes. It does not bind typed Clausewitz numeric variables or compound triggers. The five case descriptions and baseline handoff do not provide actual candidate tags, complete country rosters, or exact runtime state. No actor roster, country fixture, candidate manifest, or typed Clausewitz state was invented.

The source-complete Event 006 adapter package ID list and the detailed per-scenario input gaps are preserved in the [baseline handoff](event021_manual_scenario_probability_baseline_2026-09-26.md).

## Comparison result and skipped routes

`hoi4.probability_compare` was called with adapter `custom_weighted_pool`, `before.path` set to the exact pre-edit capture, `after.path` set to the exact post-edit source, and scenario set ID `E021-MANUAL-COUNTRY-POOL-2026-09-26` containing the five scenario IDs above. Each scenario record contained only its supplied ID because no supported actor or campaign state was available. The MCP route returned `MCP error -32602` with `Invalid input: expected record, received undefined at scenarioSet.scenarios[0].state` and the same error for scenario indexes 1, 2, 3, and 4.

The route rejected the request before source comparison; the paths were submitted, but their resolution by the comparison analyzer is not evidenced. There is no comparison ID, compare artifact, scenario hash, numeric delta, or rendered comparison view.

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were not run because the same named scenarios cannot be submitted with complete supported campaign states or a complete candidate pool. `hoi4.probability_sequence` was not run because no complete declared ticket pool and state-transition manifest exists. `hoi4.probability_simulate` was not run because no uncertain-input distributions or seed were declared. `hoi4.probability_render` was not run because the rejected comparison produced no analysis ID to render.

Result class: `exact` for the verified file hashes, direct inspect fields, and the source diff showing the removal-loop replacement. `bounded` for the source-level behavior that a selected country is removed from the remaining ticket pool before a later draw. `unresolved` for all before/after probability values, rankings, dominance, starvation, rank reversal, repetition frequency, and numerical delta. No sampled or score-only output was produced. The inspect artifacts are adapter/source discovery evidence and do not certify a probability comparison.

The relevant offline wiki references consulted were the `Data structures`, `Effects`, `Triggers`, `Scopes`, `AI modding`, and `Event modding` pages, with the remaining AGENTS.md core pages opened as instructed. Relevant array semantics were checked in the vanilla `documentation/effects_documentation.md` entries for `random_scope_in_array` and `remove_from_temp_array`, and `documentation/script_concept_documentation.md` for arrays and collections.

Recommended follow-up: the baseline recommendation to remove all selected-country tickets is implemented by `event021_parent_remove_scenario_target_tickets` in `common/scripted_effects/021_random_civil_war_parent_effects.txt`; no additional weight, score, or draw-budget change is supported by this comparison. Keep those values unchanged until a supported MCP scenario representation can provide the complete country roster, type/intensity, derived provider load, eligibility gates, and Event 006 state where applicable, then rerun the same five scenarios through inspect/evaluate/sweep/compare and render the comparison. Do not infer a numeric balance delta from this source diff.

Structural `event_inspect` and `event_render` were not invoked because this handoff is limited to the weighted scripted-effect pool and makes no event-chain topology or rendered-chain claim.

No balance approval or Event 021 completion claim is made. The source change closes the fixed-four residual-ticket mechanism in the reviewed code, while its probability impact remains unmeasured by the MCP adapter.

## Schema-probe comparison follow-up (2026-09-26)

This is a schema probe only, not an Event 021 campaign fixture or probability evidence. `GER` was supplied only to satisfy the actor field; for each of the same five named scenario IDs, the supplied fields were exactly `actor = "GER"`, `state = {}`, `flags = []`, and `scopes = {}`. No game-state values, variables, country roster, candidate manifest, or gameplay flags were added.

The post-edit `hoi4.probability_inspect` was refreshed before comparison with adapter `custom_weighted_pool` and the same source path. It returned `PROBABILITY_SOURCE_INSPECTED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `58e354e104a1b150b402749966091c8dae47392ab825b60bb2866db2cda7e760`, source hash `65cbdeafa54f422789e4491a22b40b80a2fc977a3e9636f65ad980ef7f7b8df0`, `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `availableAdapters=[]`, `requiredInputs=0`, and `unresolved=0`. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/495d85300b9df664000bcece108a46d4b01c92d9db542222f63c51175a65ded7/10601781ef27cb53b9c3641a121df1d9ca0c3c27f1c0031abd2b743fe1da3ef5/probability-inspect-65cbdeafa54f.json`.

`hoi4.probability_compare` was then called once with adapter `custom_weighted_pool`, before path `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_parent_effects_current_worktree_capture_2026-09-26.txt`, after path `common/scripted_effects/021_random_civil_war_parent_effects.txt`, and scenario set ID `E021-MANUAL-COUNTRY-POOL-SCHEMA-PROBE-2026-09-26`. The set contained the same five scenario IDs listed above, each with only the four explicitly requested schema-probe fields.

The compare returned code `PROBABILITY_ANALYZED_PARTIAL`, status `ok`, analysis status `partial`, workspace `mod_chaos_redux_ea3b2d67c2c0`, analysis ID `probability-a852b403c22cf2d819899863`, source revision `58e354e104a1b150b402749966091c8dae47392ab825b60bb2866db2cda7e760`, source hash `65cbdeafa54f422789e4491a22b40b80a2fc977a3e9636f65ad980ef7f7b8df0`, and schema-probe scenario hash `c6a63a129d66a76cb3e3bfcb7cb76c6ea5493781e225d8e33a408994c3dfab73`. Structured data also reports `unresolved=17`, `diagnostics=1`, `comparisonChanges=80`, and `visualResources=4`.

The result adapter was `random_list`, not the requested `custom_weighted_pool`; `filesScanned` was empty. The artifact reports five scenarios and 40 candidates, eight per scenario, but these are entries from two other `random_list` blocks in the same source file: six archetype entries at `event021_parent_select_archetype` around line 1197 and two strange-incident entries around line 7133. They are not the manual country ticket pool.

All 40 returned candidates have `supportLevel=unsupported`, `eligibility=true` from an implicit-true trace, and null raw value, score, rank, and conditional probability. Each has unresolved code `VALUE_UNRESOLVED`; for example, `var:event021_ideological_weight` is unresolved with message `Scenario or source definitions do not resolve numeric expression var:event021_ideological_weight`. The result diagnostic is severity `warning`, code `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`, adapter `random_list`, `candidatesFound=8`, with message `The complete candidate pool is not proven, so normalized probabilities are withheld`.

The compare artifact records `beforeAnalysisId=probability-12b6245947ea27d143ce77dc`, `afterAnalysisId=probability-d2165a762bcaf270ecfc0549`, 40 regression records, and 80 scenario-change records. These are partial random-list adapter outputs and do not establish any Event 021 manual-pool delta. The comparison analysis JSON artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7ee39c29df794046ae0ac3994c0a06228170b1d0e4b689939c729934c2416fb/147dbe11d1443ba33143010de7da96af1265d0405e0a42c2906b2e60065e6833/probability-a852b403c22cf2d819899863.json`.

The compare response supplied these rendered evidence artifacts: comparison SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/663f860913c490416c59a17d1466ebcba7e0603404f7ad388a4ee83a4196e6cb/a2a36f6c0746c26502cb00c7e185bd3e5098b9c8f0d1b98de5aefd8dd65cdb8d/probability-probability-a852b403c22cf2d819899863-comparison.svg`, comparison PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/367ed4a872f677174a40b5d00a428b9a92e251ef4ed02cace78f5eb882848777/8e5941796377cabd6f9c32dceaea706fb224afcbc21b7726e5185ccd69eb769b/probability-probability-a852b403c22cf2d819899863-comparison.png`, unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/253396a45fdac035410a31ac24cb55a29f93b7423f5d4dd7cdf2653fe81053e1/8a2bf26d6583b60d4b68f4f4711ae9f67d4213b4f639a5abbb019a63cbb8f1cb/probability-probability-a852b403c22cf2d819899863-unresolved.svg`, and unresolved PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a950aac06341f7fc1313cc0072f939d42d3cb61ae1fd42df3ebbea6aa3ebb2f/328ee0dc059d03d7ecd2f100eb96867eedabcebcc7fd5e84bd9dad360924fcfe/probability-probability-a852b403c22cf2d819899863-unresolved.png`.

An explicit `hoi4.probability_render` call for analysis ID `probability-a852b403c22cf2d819899863` and the returned scenario hash failed with code `PROBABILITY_ANALYSIS_NOT_CACHED`, status `error`, no artifacts, and blocker message `Render requires an analysis ID produced by this server process`. The comparison response above already supplied its four rendered artifacts; no render retry was made.

The comparison JSON was retrieved as `application/json` with declared total size 223232 bytes, decoded and concatenated in offset order, and parsed successfully. The verified `(offset,length)` reads were `(0,24576)`, `(24576,24576)`, `(49152,24576)`, `(73728,24576)`, `(98304,24576)`, `(122880,24576)`, `(147456,24576)`, `(172032,24576)`, `(196608,24576)`, and `(221184,2048)`; each range's continuation URI pointed to the next listed offset except the final range, which had `continuationUri=null`. Range metadata marked every response `complete=false` even though the final returned range ended at the declared total size, so that transport metadata inconsistency is retained here.

Result classification for this attempt is `unresolved`, not `exact probability`, `sampled`, or usable `score-only` evidence. The schema contract accepted the placeholder records, but the selected adapter did not analyze the requested pool, the candidate pool remained incomplete, and all values and ranks were unresolved. No numeric campaign probability or balance conclusion follows. No further compare attempt was made after this schema-correct probe, and no gameplay file was edited.

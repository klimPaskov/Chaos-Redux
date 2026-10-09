# CBRN technology research-cost probability handoff

Initial audit date: 2026-10-08. Reconciliation date: 2026-10-09. Scope is the native `technology_ai_will_do` surfaces for the 27 researchable IDs frozen by the cost inventory: 25 in `common/technologies/chaosx_technologies.txt` and 2 in `common/technologies/cbrn_regimental_support_technologies.txt`. The owner's cost calibration is present in the frozen after snapshots and current source files. This auditor made no gameplay or index changes and no commit.

## Frozen baseline sources

Byte-for-byte before copies are in `docs/testing/2026-10-08_cbrn_research_cost_probability/before_source/` with explicit `-text` attributes in the evidence directory's `.gitattributes`. The frozen hashes are `d52d48eb5796c120e5bd465dddcd5527a6597f7a60cf68f871c6240d05b1f5c1` for the 32,621-byte main technology file and `45826eb81040942fdc2fe9b32c61fdb9be09f625ce37ae655ac6e761415c6cb4` for the 8,450-byte regimental file. At inspection time both live `common/technologies` files had those same hashes and byte counts.

The exact 25/2 IDs are listed in `baseline_manifest.json` and in each MCP request record in `mcp_baseline.json`. The supplied pools are complete within those source files, as confirmed by the adapter. They are not the complete gamewide set of technologies the AI may research.

## Probability adapter and source coverage

The live schema exposes the correct `technology_ai_will_do` adapter. I first inspected the frozen files under their `docs/testing/.../before_source` paths; those calls returned `PROBABILITY_SOURCE_DISCOVERED` / `no_weighted_surfaces`. The files' raw hashes still matched the live sources, so I reran the same exact candidate pools against the canonical indexed paths `common/technologies/chaosx_technologies.txt` and `common/technologies/cbrn_regimental_support_technologies.txt`. Those calls returned `PROBABILITY_SOURCE_INSPECTED` and discovered all 25 and 2 candidate IDs respectively. The archive-path probe was a source-routing issue, not evidence that the source lacks AI weights.

The successful main inspect has source hash `30d3c88c2119d280a2547bdc3e92240b08a6546a2b77582523f37682d1f6129e`, revision `eab52f4d127afa3d8328bbd8786487495312e52be8aa3b6d88763307bb6fb645`, and artifact [probability-inspect-30d3c88c2119.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65a8d9bdc675a6f7e7bd2a815f8bf9e93821c6a441c400d98c289a0fa7c477a7/bfae41739e895955cad2632812b1e64ef816af3176e98c1d68b11648403fe025/probability-inspect-30d3c88c2119.json). The regimental inspect has source hash `07feed41e7f85ee09a1a1b88615228c66b0f0fdfe16369ea155880a715c7facf`, revision `6e2338d7911e637a18e2a9fcf5e7a319cd45e13634493bab0eb7c0ec6425c56a`, and artifact [probability-inspect-07feed41e7f8.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a35280826a51f247ae48fd7529bf122647c52a9da869854d0febeb6e8d12f13a/a052ea1d4951643f17b2dc4117c08e8962e6c1d4ba0b75165b24ceff3311b40d/probability-inspect-07feed41e7f8.json). Both have zero unresolved source expressions. This does not mean the requested scenario inputs are bound.

For frozen-source provenance, I repeated inspection using each canonical engine path plus its evidence `snapshotPath` and the raw SHA-256 `expectedSourceHash`. The adapter resolved the same 25/2 candidates from the frozen copies. Those snapshot-bound source hashes and revisions are recorded in `mcp_baseline.json`; the analyzer `sourceHash` is a separate fingerprint and is not the raw archive SHA-256.

The main adapter reports required paths `has_doctrine`, `has_tech`, `scope.any_controlled_state`, `scope.any_enemy_country`, `variable.cbrn_military_mask_coverage`, and `variable.cbrn_protection_program_profile`, plus adapter-level `technology.external_factors_complete`. The regimental file reports the first four paths and the same adapter-level external-factor completeness requirement. None of those facts was invented or marked complete.

## Historical scenario fixture record

The 2026-10-08 result summaries record scenario-set ID `CBRN_RESEARCH_COST_BASELINE_2026_10_08` and hash `6af9cf175c3e31a2977acb6971aa71414d2ca9bff98567194e20dad5633fd467`. The retained `scenario_fixture.json` contains six named rows for 1936 basic utility/no advanced project, 1939 normal protection, and 1941 advanced enabled, each with `vanillaDoctrine` and `ChaosWarfare` context labels, but only `state.year` is bound. The doctrine variants and stage descriptions are labels, not asserted game identifiers or prerequisite states. Actor, exact doctrines, prerequisite IDs, project flags, country scopes, the two CBRN variables, full AI modifiers, and `technology.external_factors_complete` remain unbound.

The first evaluate request was rejected with MCP `-32602` because it put unsupported `year` and `analysisContext` keys at scenario root. A later request was accepted, but its complete request body was not retained. On 2026-10-09, replaying the exact on-disk `scenario_fixture.json` `scenarioSet` produced a different live hash, `9014abc855784fcdc7f9cba67f0c7d33afff123b1402db73949c381209e7c004`, across both frozen-before evaluations and both before/after comparisons. The captured request/result packets and the unresolved historical discrepancy are documented in `docs/testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json`.

## Baseline evaluation and classification

For `chaosx_technologies.txt`, `probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`: 150 candidate/scenario rows, 144 eligible, 0 excluded, 113 unresolved items, and 6 unresolved candidates across the six cases. Four informational diagnostics say the `CBRN_PROTECTION_RESEARCH_SHORTAGE_FACTOR` modifier was not active in any supplied case for `advanced_gas_masks`, `basic_gas_masks`, `improved_gas_masks`, and `sealed_assault_protection`. Because the required protection variables were deliberately left unbound, those diagnostics do not prove that the modifier is inactive in a campaign.

For `cbrn_regimental_support_technologies.txt`, the result is also partial: 12 rows, 12 eligible, 0 excluded, 19 unresolved items, and 0 unresolved candidates. The render results produced ranking and unresolved views for both analyses. Their analysis IDs, source revisions, scenario hash, per-run totals, and all JSON/SVG/PNG artifact URIs are recorded in `mcp_baseline.json`.

Classification is partial, source-bounded, score-only `technology_ai_will_do` evidence with unresolved external factors. No normalized research-selection probability is claimed. The full competing vanilla/mod technology pool and global `research_weight_factor` strategy inputs are not covered by the 27-ID source pool, and unknown doctrine, prerequisite, scope, and CBRN-variable bindings may change candidate validity and ordering. No exact ranking conclusion is quoted from the rendered summaries.

## Cost context and implications for AI

The before inventory records cost tokens 0.5, 0.75, and 1.0. The frozen after sources use 0.45454, 0.68181, and 0.90909 for the 50, 75, and 100 base-day targets; those multipliers model 49.99940, 74.99910, and 99.99990 days against installed `BASE_TECH_COST = 110`.

Installed vanilla source lookup found `BASE_TECH_COST = 110` at `game:common/defines/00_defines.lua:710`, revision `ad87327665b93c49b9a5a83e229ef7c092b953ffbc842171a9213508753b097a`. The offline Defines page also lists 110 at line 647, revision `61ae03fd36bcbe2ab6ca1304b013d3f432b88e6592856fffdd2685f792e87fcc`. An older Technology modding footnote cites 100; the installed vanilla definition is the current source for this audit.

The offline Technology modding AI-weighting section, lines 331–354, revision `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee`, explains that research choice combines technology `ai_will_do` with cost, bonuses, and ahead-of-time modifiers. Installed `common/ai_strategy/_documentation.md`, `research_weight_factor` lines 603–612, revision `70f5d755ae7ed4060e49cc64a393d1a0dc5611b3acc8abc6dfb4538781c915a1`, documents an external factor on specific technologies. Therefore preserving explicit AI coefficients does not prove unchanged total AI research preferences: a cost change can affect the engine's research-selection weighting.

## Historical comparison summaries and remaining limits

The 2026-10-08 `mcp_after_compare.json` records `probability_compare` analysis IDs `probability-9ae94a528e7cfd853df646b6` and `probability-b4df5becc67c782bcbf0387e`, both with `comparisonChanges=0` and hash `6af9cf175c3e31a2977acb6971aa71414d2ca9bff98567194e20dad5633fd467`. That remains a historical summary; it is no longer asserted as proof that the currently saved scenario fixture was passed verbatim.

The main technology comparison covered 150 candidate/scenario rows, 144 eligible candidates, 181 unresolved items, and 6 unresolved candidates. It repeats four informational diagnostics that the CBRN protection research-shortage modifier is unsatisfied for `advanced_gas_masks`, `basic_gas_masks`, `improved_gas_masks`, and `sealed_assault_protection` in all six supplied cases. Since the protection variables were intentionally left unbound, these diagnostics do not show that those modifiers are inactive in campaigns.

The regimental comparison covered 12 candidate/scenario rows, all eligible, with 29 unresolved items and 0 unresolved candidates. Exact compare JSON, ranking, comparison, and unresolved artifact URIs for both surfaces are preserved in `mcp_after_compare.json`.

The zero comparison count applies to the adapter-exposed `technology_ai_will_do` score comparison. It does not prove unchanged total AI research preference: research cost itself is an engine input to technology-selection preference, while doctrine, prerequisite, CBRN-variable, global research-strategy and complete gamewide-pool inputs remain unresolved. Do not claim normalized research odds or that the engine's overall research preference is unchanged.

The historical compare calls emitted six source-revision-linked visual resources per analysis. Their later standalone render was stale at the time, so the compare-emitted artifacts are retained as the historical visuals.

The owner source-test receipt [source_test_results.json](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/testing/2026-10-08_cbrn_research_cost_review/source_test_results.json) reports 40 tests, 0 failures, exact AI-block preservation in both files, and only approved research-cost changes. The 5-decimal factors model 49.99940, 74.99910, and 99.99990 days, with a 0.00060/0.00090/0.00010-day shortfall from their targets. Native field precision and calendar rounding remain undocumented by the inspected evidence.

No probabilistic simulation was run because no evidence-backed uncertain-input distribution was provided. A separate deterministic synthetic `probability_sweep` tested mask coverage values 49, 50, and 51 around the source threshold, but the adapter left the numeric AI base/factor constants unresolved and a later render marked the analysis stale; it therefore does not establish a game-level threshold effect or rank reversal. No custom-pool sequence applies.

## 2026-10-09 exact-fixture reconciliation and bounded inputs

The live `probability_inspect` route revalidated both frozen-before sources and both frozen-after snapshots through canonical gameplay paths with `snapshotPath` and raw `expectedSourceHash`. Both file-local candidate pools remain complete within their source files: 25 main candidates and 2 regimental candidates. This does not make either pool complete for all vanilla and mod research options.

The exact saved six-row fixture replay returned hash `9014abc855784fcdc7f9cba67f0c7d33afff123b1402db73949c381209e7c004` for the main and regimental before evaluations and their matched before/after comparisons. The new main comparison covered 150 candidate/scenario rows, 144 eligible candidates, 0 exposed score changes, 181 unresolved items, and 6 unresolved candidates. The regimental comparison covered 12 rows, 12 eligible candidates, 0 exposed score changes, 29 unresolved items, and 0 unresolved candidates. These are partial score comparisons, not native research probabilities.

The previous raw analysis artifact ranges available for the historical run were only the first 12,000 bytes of each JSON artifact. Their metadata reports `6af9...5633fd467`, but the complete artifact bodies and declared artifact digests were not assembled. The skill-maintenance note records a contradictory `6af9...f08a3e6c19cf61` receipt hash that is not reproduced by the retained metadata ranges. Since the original request payload is missing, the cause of the historical mismatch remains unresolved; the new exact-fixture replay is the reproducible current comparison.

A second explicitly synthetic six-row scenario set bound `has_doctrine` as `false` or `chaos_warfare`, one `has_tech` ID per row, CBRN mask coverage 49 or 50, program-profile enum values 0, 1, 4, and 6, date/year, actor, war state, generic scope-presence booleans, and the `cbrn_program_established` flag where declared. It returned main scores for 150 rows with 147 eligible and 3 unresolved candidates, and regimental scores for 12 rows with all 12 eligible. Matched comparisons again reported 0 exposed score changes; the main comparison had 141 unresolved items and the regimental comparison had 21. These fixture bindings are declared synthetic inputs, not campaign observations, and they still omit complete prerequisites, nested enemy-scope contents, active strategy plans, and global research factors.

The `ai_strategy_factor` adapter inspected `common/ai_strategy/cbrn_country_profiles.txt` and found 53 candidates with `poolComplete=false`, and inspected `common/ai_strategy/chemical_warfare_research.txt` and found 43 with `poolComplete=false`. Those sources contain `research_weight_factor` and `research_tech` entries whose active country plans are not bound here. No strategy-factor evaluation was treated as a complete preference model.

The synthetic threshold sweep returned 3 points and 65 unresolved items. A fully byte-range-assembled re-render report, SHA-256 `ed873be8653cc33730ca134b5dd80734ab4096c5fcf8c53f8fe20012647850be`, was marked stale after the workspace revision changed from `c1569d3bc19841aee03dbc44b8b04ef2b1f2a36386dc24db05bb3fe5dd11b824` to `383d914fab28f56579abd68f9b4b168520ec56d4637f0cfa740a06063f5f8b3b`. It reports `raw_value = 1` for all 25 source candidates at 49, 50, and 51, zero local elasticities, and no breakpoints, while its traces show `@CBRN_PROTECTION_RESEARCH_BASE` and factor values unresolved. The exact raw score ordering and any real engine rank reversal therefore remain unresolved.

The CBRN `ai_will_do` source declares bases and factors such as `@CBRN_PROTECTION_RESEARCH_BASE = 0.75`, `@CBRN_PROTECTION_RESEARCH_SHORTAGE_FACTOR = 3`, and `@CBRN_PROTECTION_RESEARCH_PROGRAM_FACTOR = 1.75`, but the probability analyzer does not resolve those numeric tokens in the retained runs. The comparison proves zero change only in the adapter-exposed score values under each matched fixture. It does not establish normalized selection odds, unchanged total AI research preference, starvation, dominance, repetition, or exploit safety after the cost change.

Read exact captured requests and live responses in `docs/testing/2026-10-08_cbrn_research_cost_probability/raw_calls/`. The standalone render attempt for the synthetic comparison returned `PROBABILITY_ANALYSIS_NOT_CACHED`; the sweep render returned `PROBABILITY_ANALYSIS_STALE`. The compare and sweep calls themselves returned their requested comparison, ranking, sensitivity, and unresolved artifacts. The full current reconciliation is `docs/testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json`.

## Recommended follow-up

For exact native research-choice probabilities, supply the full eligible gamewide technology pool and enumerate the active `research_weight_factor` and `research_tech` strategies for each named actor and date, then bind the full prerequisite and scope state without setting `technology.external_factors_complete` by assertion.

For source-local CBRN score coverage, retain the tested 49/50 coverage boundary and add an explicitly synthetic `cbrn_protection_program_profile = 5` case to exercise `cbrn_profile_is_limited_or_minimal` and `@CBRN_PROTECTION_RESEARCH_LIMITED_FACTOR` in `common/scripted_triggers/cbrn_protection_triggers.txt` and `common/technologies/chaosx_technologies.txt`.

Do not tune weights or claim balance from the flat bounded `raw_value = 1` sweep; the analyzer reports the relevant source `@CBRN_PROTECTION_RESEARCH_*` and `@CBRN_REGIMENTAL_AI_*` numeric expressions unresolved.

## Evidence files

- `docs/testing/2026-10-08_cbrn_research_cost_probability/baseline_manifest.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/mcp_baseline.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/mcp_after_compare.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/raw_calls/`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/scenario_plan.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/before_source/`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/after_source/`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/after_source_manifest.json`
- `docs/testing/2026-10-08_cbrn_research_cost_probability/.gitattributes`

# Hospital and utility protection entry probability review

Status: matched source comparison completed with a partial analyzer result; the AI willingness-score body is byte-identical before and after, while target eligibility and payment readiness remain partly unresolved in the adapter.

This is a read-only probability audit of `cbrn_protect_hospitals_and_utilities` in `common/decisions/cbrn_protection_decisions.txt` and its current helper chain in `common/scripted_triggers/cbrn_protection_triggers.txt`, `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt`, and `common/scripted_effects/cbrn_immediate_response_cost_effects.txt`.

The parent-applied patch changes the hospital relevance gate to accept the exact raid-alert flag or positive chemical contamination, retains the target-controller and already-secured checks, and computes ordinary population-based quote values in the caller path rather than depending on the dormant alert-registration price writer.

The accepted design basis is `docs/specs/chaos_warfare_system_specs/specs/07_gas_masks_civil_defence_and_population_protection.md:202-204` for the hospital response’s support-equipment and mask costs and continuing-loss effects, plus `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` for Civil Defence decisions responding to real threat, outbreak, contamination, or response need.

## Source snapshots and weight preservation

The four original source snapshots are exact raw byte copies under `docs/testing/2026-10-09_hospital_entry_probability/` and their raw SHA-256 values are in `source_hash_manifest.json`.

| Source | Before SHA-256 | After SHA-256 | Result |
| --- | --- | --- | --- |
| `common/decisions/cbrn_protection_decisions.txt` | `d263e1803a5dbd2b760f78a4f79a29edfdd910b770b79a78600220327afdc790` | `6265c04b4dc3154c0447b7163e533ce6404d010125a5f943a1109c5dbebe4ab7` | Eligibility gates changed. |
| `common/scripted_triggers/cbrn_protection_triggers.txt` | `5e073ad69e3040b63c232b013304730a899000cf3b26abb2d03ecec99aa425c0` | `ce9e25d8fae7c04da8e449b1b468a4bb65f6b652c6a92eb9cd4ff4266e0c2301` | Response-need helper and caller checks changed. |
| `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt` | `0dd204a84975e084e842b8edfcf8d3a6ccee6c2c58516c2d79ed60ca7faa0571` | `854fb993f2738b084627994790e532ab63e7ef98d971abcad7bf9b3b68b83e29` | Fresh population quote path changed. |
| `common/scripted_effects/cbrn_immediate_response_cost_effects.txt` | `609d9585a0e694e53998d936323f6868f7e269a9a0324b4a055830819f5d8ec7` | `8a8e6b9807aa1bcffba68678a6ade2d968b8891865d796edbbec6064f3b1c456` at initial after capture; parent later recorded `5f6094608702d8a2f6f04b0c8dd13411ba4358337508920f9f4232cdcb8ae053` after a two-line whitespace indentation correction. | Only formatting changed after the first after copy; latest exact copy is `cbrn_immediate_response_cost_effects.txt.after_whitespace`. |

The target decision’s entire `ai_will_do` block was extracted from the before and after decision snapshots and compared byte-for-byte after extraction; both have SHA-256 `db3f915aa72a681481a1ebc55f94f490cc8989ce9e6779b7ee8432acef209a38`.

The preserved score formula uses `constant:cbrn_protection_ai.base_response` (8), the alert-only `alert_factor` (5), `capital_factor` (3), and `high_population_factor` (2 when population is strictly above 2,500); these values and gates were not changed.

The fixture is non-capital ENG/state 16 at population 1,000, so the capital and high-population modifiers are intentionally inactive in all nine scenarios; the MCP returned two informational diagnostics for those inactive factors.

## Matched probability evidence

The baseline inspection used `hoi4.probability_inspect` with adapter `decision_ai_will_do`, source hash `d749c85935f66a5d4683e0a99605a0db16a296ec9aaae23e43e93f9d58ff6a4f`, source revision `6f8181d208d1f6c441d080821e524fa4c060aa291b4c2408511a8e21b510bc11`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1d58b5a83a148743d4a9cc5366f3648a64b341cc45141d1449dd06b7b71cfd6/947c0b62d5e8cdef54fca6f4df024e87e5dcb26fc0f26a6e61b68de49a5cb3ed/probability-inspect-d749c85935f6.json`.

The initial `hoi4.probability_evaluate` analysis used the corrected persisted fixture, the exact `.before` decision snapshot, and only candidate `cbrn_protect_hospitals_and_utilities`; it returned partial analysis `probability-e18ff20a02813e7eb1f18922`, scenario hash `1fbef20cc57ced1ed2ac0928792e2c187022de812ed259a5e8c35fbc8a2ea1df`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a9351eef738e27ebaed988c7a41e15c35d7f9ea5de17b147418aa8086da39a/cb4064ece2334424d1b2decd39e508e7510a42d24117de210d602b4316023c40/probability-e18ff20a02813e7eb1f18922.json`.

Its raw willingness-score traces were: `HP_CLEAN_NO_ALERT` 0 and false; `HP_EXACT_ALERT_NO_CONTAMINATION` 40 and unresolved; `HP_CONTAMINATION_NO_ALERT` 0 and false; `HP_ALERT_AND_CONTAMINATION` 40 and unresolved; `HP_ALREADY_SECURED` 0 and false; `HP_WRONG_CONTROLLER` 0 and false; and each of `HP_PAYMENT_ONE_SHORT`, `HP_PAYMENT_EXACT`, and `HP_PAYMENT_ONE_ABOVE` 40 and unresolved.

The exact nine fixture ids are `HP_CLEAN_NO_ALERT`, `HP_EXACT_ALERT_NO_CONTAMINATION`, `HP_CONTAMINATION_NO_ALERT`, `HP_ALERT_AND_CONTAMINATION`, `HP_ALREADY_SECURED`, `HP_WRONG_CONTROLLER`, `HP_PAYMENT_ONE_SHORT`, `HP_PAYMENT_EXACT`, and `HP_PAYMENT_ONE_ABOVE` in `scenario_set_baseline.json`; its raw SHA-256 is `ff4acac45ff8b59c23a22b899ce0511ba4e798ca4d214152bda388ed6841b7c5`.

The one matched `hoi4.probability_compare` used this same fixture hash and only the actual hospital decision candidate; the request is saved as `after_probability_compare.request.json` and the exact response as `after_probability_compare.response.json`.

The compare returned `PROBABILITY_ANALYZED_PARTIAL` with analysis `probability-d521185f92e8005bac5d6816`, scenario hash `1fbef20cc57ced1ed2ac0928792e2c187022de812ed259a5e8c35fbc8a2ea1df`, `comparisonChanges=0`, nine scenarios, nine candidate-scenario records, zero definitely eligible records, three excluded records, six unresolved candidate records, and seven unresolved items.

The artifact comparison metadata reports `adapterChanged=false`, `assumptionsChanged=false`, an empty `regressions` array, and an empty `scenarioChanges` array; because six records remain unresolved, these fields do not prove exact before/after gate equivalence.

The returned linked JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fbd055d6fba9282b4f7021370129ed1a78256b74c78a6dc9aa4f4fc55bdde1c/fdf2f041ef6f604882fd126e9036cce68c1e7375e34f71933b3a1f4c5bea4c48/probability-d521185f92e8005bac5d6816.json`, SHA-256 `4fbd055d6fba9282b4f7021370129ed1a78256b74c78a6dc9aa4f4fc55bdde1c`, size 542,685 bytes, source revision `d4b83dacfb5906164448448fcc99c56de4f56f50ba34e519b22c2bfe6426fc44`, and adapter-computed source hash `4fe566d7206dabe82ff4a5f21eb739551c37ec03b74bcddfdb8a46ec8e8806af`.

The comparison also returned rendered comparison, waterfall, and unresolved views; their artifact URIs, hashes, sizes, and MIME types are retained in `after_probability_compare.summary.json` and the response file.

## Interpretation and boundaries

This adapter is `decision_ai_will_do` version `hoi4-1.19.2.v1`, with `selectionRule=score_only` and `normalizedProbability=false`; it reports willingness scores, not click odds or the AI’s probability of choosing this button among all competing decisions.

The candidate pool contains only the requested hospital decision; it is a complete scope for this one decision’s score trace, not a complete country-wide decision race, and the adapter does not model that selection race.

The after comparison’s main source binding covers `common/decisions/cbrn_protection_decisions.txt` only: its artifact metadata lists `sourcePaths=["common/decisions/cbrn_protection_decisions.txt"]`; the archived before decision text was supplied inline and the after source used the canonical live path, byte-verified against the after snapshot immediately before comparison.

The helper definitions were therefore resolved from the current shared workspace for both compare sides; the comparison did not inject the four `.before` helper snapshots, and it is not a full old-helper-closure versus new-helper-closure comparison.

The baseline evaluation’s `snapshotPath` and raw expected-source hash froze the primary decision file only; they did not freeze the full scripted-trigger/effect dependency closure.

The exact initial baseline evaluation remains separate evidence from the matched compare; its pre-patch helper definitions were live when evaluated, while the comparison’s before side uses the current post-patch helper closure.

The linked after JSON resource exposed a complete-range metadata marker, but the returned text could not be parsed as a complete JSON document and parsing stopped at character 22,396; the per-scenario after `eligibility` and `rawValue` records were not recovered, so this handoff does not infer them from aggregate counts.

The visible unresolved diagnostics name analyzer gaps around `scope.set_temp_variable`, `scope.if`, and the quote flags `cbrn_hospital_quote_valid`, `cbrn_hospital_pp_affordable`, `cbrn_hospital_support_affordable`, and `cbrn_hospital_masks_affordable` inside the hospital payment helper chain; exact after payment readiness remains unresolved.

The baseline synthetic exact-alert scenarios supplied hypothetical pre-registration quote variables; after the patch the quote is recomputed through the fresh population path, which the probability adapter does not fully execute, so baseline one-short/exact/one-above labels cannot be promoted into post-patch threshold claims.

A parent-reported whitespace-only correction to the ordinary-cost effect source landed after the after source copy was first captured; its latest raw copy and hash are retained, and the parent directed that no second compare was needed because the score helper dependency provenance did not include that effect file.

The offline decision-modelling references consulted for the baseline are `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 357-374 and 531-537, `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` lines 26-37, and the installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` lines 1-46; the earlier reference-read revision receipts were not persisted, so their full revision IDs are unavailable in this evidence packet.

## Balance findings and recommendation

No AI weight or score modifier changed, and this comparison supplies no evidence that would justify changing the existing score constants.

The score formula keeps its alert-only factor; conditionally, an eligible contamination-only state has the base response score without that factor, while an eligible exact-alert state can receive the alert factor, but the after adapter result does not resolve enough payment-gate detail to claim either state is definitely eligible.

No complete ranking, dominance, starvation, rank-reversal, repetition, custom-pool cadence, or campaign-level exploit result is available from a one-candidate score-only adapter and these nine synthetic state fixtures.

`probability_sweep` was not run because no weight or threshold changed and the payment helper is unresolved; simulation and sequence analysis were not run because there is no defensible empirical input distribution or declared custom pool; the comparison’s own rendered artifacts made a separate render call unnecessary.

No game was launched and no game logs were searched or requested.

## Evidence files

`docs/testing/2026-10-09_hospital_entry_probability/scenario_set_baseline.json` is the persisted nine-scenario fixture.

`docs/testing/2026-10-09_hospital_entry_probability/cbrn_protection_decisions.txt.before` and the three other `.before` files preserve the raw pre-patch dependency snapshots.

The four `.after` files preserve the initial parent-applied after copies; the effects source also has `cbrn_immediate_response_cost_effects.txt.after_whitespace` for the parent-reported whitespace-only correction.

`docs/testing/2026-10-09_hospital_entry_probability/baseline_probability_inspect.request.json`, `.response.json`, and `baseline_probability_inspect.artifact_1.json` preserve the baseline source inspection.

`docs/testing/2026-10-09_hospital_entry_probability/baseline_probability_evaluate_retry.request.json`, `.response.json`, and `baseline_probability_evaluate.analysis_artifact.json` preserve the corrected baseline evaluation; the initial rejected request is retained separately and is not treated as evidence.

`docs/testing/2026-10-09_hospital_entry_probability/after_probability_compare.request.json`, `.response.json`, and `.summary.json` preserve the one matched comparison, its exact service response, and scoped summary.

`docs/testing/2026-10-09_hospital_entry_probability/source_hash_manifest.json` records raw hashes, comparison binding, the unchanged target `ai_will_do` block hash, and the helper-closure limitation.

`docs/testing/2026-10-09_hospital_entry_probability/` is the sole testing-evidence write scope for this auditor; this handoff is the sole plan write.

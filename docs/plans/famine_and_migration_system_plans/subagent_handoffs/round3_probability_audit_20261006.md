# Famine reserve-release probability audit

Date: 2026-10-06.
Disposition: unresolved MCP affordability comparison; source review only.
Mode: read-only; no gameplay files, AI weights, staging, or commits changed.
The parent reports that the five round-3 drafts were published in commit `53d3a9e4afff10ed4ffb759b8439b5ddee5751ce` without numeric AI-weight changes.

## Audited surface and source

The weighted surface is decision `famine_release_reserves` under adapter `decision_ai_will_do`, declared in `common/decisions/famine_decisions.txt`.
The relevant score table is `common/script_constants/famine_decision_constants.txt`; target gates are in `common/scripted_triggers/famine_decision_owner_triggers.txt`; the payer affordability tuple is in `common/scripted_triggers/humanitarian_legacy_cost_triggers.txt` and `common/script_constants/humanitarian_legacy_cost_constants.txt`.
The frozen before-source is `docs/plans/famine_and_migration_system_plans/validation_baselines/legacy_cost_affordability_20261003/famine_decisions.txt`, with its paired `famine_decision_constants.txt` and `SOURCE_MANIFEST.md`.
The named controlling status files were read: `docs/plans/famine_and_migration_system_plans/takeover_status_2026-10-06.md` and `docs/plans/famine_and_migration_system_plans/ai_probability_current.md`.
Current decision and constant SHA-256 values are `1E3DB123B405076B7A50DB01774682F40DFCDAA6ADB6BB7D3BE82B8095D40B9C` and `8BEA020D386F397C511A7960CA165F31DE24EC403F7A923A4C618D121D214700`.
Frozen before decision and constant hashes are `52E84B51B6C9FAF5827F3152613870E4EBBD65215EDD35D70E913D18BA01DFAA` and `32E53D81DEDAE55852B3FD2EC4F81889E41E1EEC471D04255F9877B45B20CB4C`.

## MCP route and artifacts

The live tool inventory exposed `hoi4.probability_inspect`, `probability_evaluate`, `probability_sweep`, `probability_compare`, and `probability_render`.
The inspect schema exposed the `decision_ai_will_do` adapter, `source` as an opaque object, and `refresh`; the `symbol` form was rejected by input validation.
Exact failed call: `probability_inspect({adapter:"decision_ai_will_do",source:{symbol:"famine_release_reserves"}})`; MCP returned `-32602`, “Unrecognized key: symbol at source”.
Exact bounded retry: `probability_inspect({adapter:"decision_ai_will_do",source:{path:"common/decisions/famine_decisions.txt"},refresh:false})`; it remained pending through 61 seconds and the cell was terminated.
That retry returned no status, artifact URI, source revision/hash, candidate inventory, scenario hash, or analysis ID.
The probability tools remained exposed, so this is a missing result for this bounded call, not proof of global MCP service failure.
No evaluate, sweep, compare, or render call was submitted because inspect did not return and the required cost labels have no supported machine fixtures in the frozen scenario file.
No compare ID, artifact URI, revision, scenario hash, or rendered evidence exists for this audit.
No exact selection probability is claimed.

The requested `reference_context` call for the decision surface and `reference_search` for decision AI/availability/cost each remained pending for 60 seconds and were terminated without citations.
A `source_lookup` request first rejected `maxDefinitions:5` because the live schema caps it at 3; the corrected `maxDefinitions:1` lookup for `famine_release_reserves` remained pending for 61 seconds and was terminated without an artifact.
Following the repository fallback, I read the relevant local wiki sections and installed documentation directly; the reference MCP route gap remains recorded here.

## Source-only score and eligibility trace

The current `ai_will_do` base is `12`.
Its existing factors are `3` for `FROM = { has_state_flag = famine_food_security_active }`, `2` for `FROM` food pressure above zero, and `0.5` when `ROOT` is at war.
The current source adds stage factors of `1.5` for acute shortage, `2.5` for famine, and `4` for catastrophic famine.
The frozen before-source has the same base and the first three factors, but no stage-specific factors; current constants contain those three additional values.
The decision’s target gate requires a valid state, active food registration, initialized reserves, a visible food problem or positive food pressure, and reserve stock above the minimum grant.
The same reserve target rule is used by `visible`, `available`, `target_trigger`, and `famine_release_reserves_can_start`; start availability also requires ROOT to control FROM, all three fees to be affordable, and no paid receipt already active.
A shockless registered state can qualify through its committed stage; in that path the pressure factor of `2` does not apply.
Supply strain qualifies as a visible food problem, but the decision has no supply-strain-specific AI factor.
The separate war factor lowers the score during war; no analyzer evidence establishes how it ranks against the rising famine-stage factors or other available famine actions.
These constants and conditions are a source-only willingness-score definition, classified `score-only`; they are not an evaluated scenario trace or click probability.

Current fees are 20 political power, 50 support equipment, and 500 fuel.
Current shared helpers express affordability as the negation of each native “less than fee” check, so source semantics allow exact-fee equality and require every tuple component to pass.
The frozen before decision used strict `>` checks for the same three fee constants; offline trigger documentation specifies strict comparison operators.
Thus exact-stock eligibility differs at source level between the frozen before and current source, while one-short stock fails the current composite gate.
This is a source comparison only; the required analyzer comparison did not run.
The current decision deducts the fee inside `complete_effect` after revalidating its start gate; the 21-day decision removal callback is later, and source does not defer the initial fee debit until that callback.
The named “late deficit” case must declare whether stock falls before the click/start revalidation or after the fee has already been paid.

## Named scenario coverage

| Scenario ID | Requested setup | Candidate and external-factor completeness | Classification |
| --- | --- | --- | --- |
| `cost_stock_exact` | Parent-requested `GER`, `FROM` state 64, with each resource exactly at its nominal fee. | No machine fixture or returned scenario binding; stage, pressure, war, stock, state ownership/controller, reserve, and competing decision candidates were not returned. | Unresolved; source gate is inclusive at equality. |
| `cost_stock_one_short` | Parent-requested `GER`, `FROM` state 64, with one fee component below its threshold. | The specific short resource and complete remaining facts are not encoded by the frozen scenario CSV or a returned scenario object. | Unresolved; source composite rejects any deficient component. |
| `cost_stock_late_deficit` | Parent-requested late-deficit case. | The phase of the deficit is unspecified and there is no supported fixture; it matters whether the loss precedes start-gate revalidation or follows fee payment. | Unresolved. |

The frozen manifest explicitly records these three cost names as labels only, not approved machine fixtures.
Its official CSV supplies descriptive cases such as `prob_famine_relief_dense` and `prob_famine_relief_blocked_island`, but not exact country/state/resource bindings.
The complete eligible selection pool is unresolved; the inspect returned no candidates.
The takeover status records 28 non-mission decisions with AI blocks across the broader system, but that count does not identify the eligible GER/state-64 pool.
External strategy factors, dynamic target instances, and the analyzer’s treatment of unavailable choices remain unverified.

## Findings and recommended follow-up

No source-level contradiction was found between the selected-state gate and target filters; affordability is an availability gate rather than a modifier in the `ai_will_do` block.
Because no MCP evaluation resolved those gates, positive score on blocked or unavailable candidates is not certified absent.
Numeric ranking, dominance, starvation, rank reversal, timing, repetition, and exploit safety are unresolved.
The source sets `fire_only_once = no`, `days_remove = 21`, and `days_re_enable = 45`; the shared takeover record documents the zero-consumption fee refund, but no probability sequence or repeated-state run was available to test wasted reactivation or farming behavior.
The score definition has no MTTH timing distribution; it is a decision willingness score.

Do not change the score constants based on this source-only pass.
For completion, the parent needs a supported inspect result, then the same before/current `probability_compare` scenarios for the exact-stock, one-short, and clearly phased late-deficit cases, plus the declared famine relief scenarios where supported.
Bind GER/state 64, all three fee resources, reserve eligibility, committed stage, pressure, war state, relevant decision availability and complete competing candidate pool in the adapter’s accepted schema.
Use the sweep route only after a supported scenario run exists to check stage/war sensitivity and rank reversals; render the comparison or unresolved view only from a returned analysis ID.
A code fix should follow a concrete evaluated defect; this audit selects no numeric balance target and applies no patch.

## Reference and validation boundary

Offline wiki sources read directly: `paradox_wiki\\AI modding - Hearts of Iron 4 Wiki.md`, MTTH blocks section around lines 26–45; `paradox_wiki\\Decision modding - Hearts of Iron 4 Wiki.md`, decision visibility/availability, custom cost, AI, and targeted-decision sections around lines 85–110, 308–366, and 511–582; and `paradox_wiki\\Triggers - Hearts of Iron 4 Wiki.md`, strict comparison and variable/resource trigger sections around lines 65–75, 571–590, 723, and 1516–1537.
Installed documentation read directly: `C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV\\documentation\\triggers_documentation.md`, including `check_variable`, `has_equipment`, `has_fuel`, and `has_political_power`; and `script_concept_documentation.md` for script constants.
The installed documentation search did not surface a decision `ai_will_do` selection model; the offline wiki supplies that model and distinguishes decision score races from event-option probability-proportional sampling.
A vanilla decision precedent was read from `C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV\\common\\decisions\\ITA.txt`; it uses a conditional `ai_will_do` block, but does not validate this custom adapter or famine scenario.
No tests were run for this read-only probability handoff; the takeover status reports the current bounded source tests separately.

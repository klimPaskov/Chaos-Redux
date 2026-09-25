# Timed Mask Reservation Probability Baseline

Date: 2026-09-25.
Status: incomplete and unresolved baseline; read-only except for this handoff.

## Scope and source capture

Audited `cbrn_supply_occupied_population` in `common/decisions/cbrn_protection_decisions.txt` and `cbrn_deploy_protective_aid` in `common/decisions/cbrn_occupation_decisions.txt` as timed missions using the `mission_ai_will_do` adapter.
The parent owns the upcoming selection-time reservation patch and the after-change compare.
No gameplay file was changed by this audit.

| Surface | Pre-edit source hash | Mission inspect revision | Mission inspect artifact |
| --- | --- | --- | --- |
| `cbrn_supply_occupied_population` | `7a6d653dc29282f080a07c459f863f3378ccf08a334a5ec79981122e70399df5` | `c35492c698fb770bb847d26225ca5c99f7ddfad76d88b9760366ffc1366becf5` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eb9296434414cca41286e33d654fdd89cd88960737433519340f9aae6a283d6/2c1caf2727d368100e74be0a18653da6039fd17d3f5d2de67abbd673cca5826a/probability-inspect-7a6d653dc292.json` |
| `cbrn_deploy_protective_aid` | `5786d0c9f0836750d8b5662129942a612dbef0c18cbed2010d0f1284e0c45080` | `630932d99f64b15664020b266b61a609506aee1db827aaaba6c6c5c6e3c209d0` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c282b5c3f420c55a4c6c0badea48c126261686b39dec885064063eb184ef75b8/b83d8b7ce7d24c4aa84912dee93eaed95066dc78ee1046a5ee6ff90c1667b862/probability-inspect-5786d0c9f083.json` |

The local decision-file SHA-256 values matched those two MCP source hashes when the pre-edit sources were captured.
The protection evaluator later reported the same source hash and evaluation revision `8042e0a10c9d265822b4d82b054240a423916e3b9c9ba2d63e9e63cb78e2ee9a`.
The occupation evaluator failed before returning a source revision or scenario hash.

## References consulted

Read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`.
Consulted the offline wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`.
Consulted installed vanilla documentation on script constants, decision effects, triggers, and dynamic mission timeout variables under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.
The adapter inspect artifacts cite `docs/research/probability-adapter-evidence.md` and `fixtures/probability`, but neither path exists in the repository checkout.

## MCP route and results

The `decision_ai_will_do` adapter inspections omitted both requested ids, while the `mission_ai_will_do` inspections found them as timed missions.
This matches the source structure: both ids contain `days_remove` and `ai_will_do`, and the mission adapter describes its score as score-only with no selection probability or time-distribution conversion.

| Tool | Surface | Result | Evidence |
| --- | --- | --- | --- |
| `hoi4.probability_inspect` (`decision_ai_will_do`) | `cbrn_protection_decisions.txt` | 5 other candidates; target id omitted; pool incomplete | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24a8a67a57acad997e134a3788a55baa4b464a868c93d2b312ba11d7b32fbc7e/a461263249b41073d95cd707a0b369058ba8b80b392f565f10a313bd924e1c94/probability-inspect-7a6d653dc292.json` |
| `hoi4.probability_inspect` (`decision_ai_will_do`) | `cbrn_occupation_decisions.txt` | 6 other candidates; target id omitted; pool incomplete | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23cdef11118a6e69cc3eef8f5c6c6fb7cc0a9d7f6c6e1c01287886e884c847f9/bfdd249d89bc270d5045c067a9de0940c2793234878f26633b9282dc3a75301b/probability-inspect-5786d0c9f083.json` |
| `hoi4.probability_inspect` (`mission_ai_will_do`) | Both source files | Found each exact candidate; source candidate pools contain 7 and 3 weighted missions respectively; complete-pool flag false | Mission inspect artifacts above |
| `hoi4.probability_evaluate` (`mission_ai_will_do`) | `cbrn_protection_decisions.txt` | `PROBABILITY_ANALYZED_PARTIAL`; 7 named scenarios; one target candidate per scenario; 6 unresolved items in the tool summary; no diagnostics | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/446d7afa6947364afee6991354d5cac13062b55bf1b10668c124b6ad31ebfceb/6457dd62bd0c3f46aba887b115e5813a7f8412c322d93ff58f947535d0962b73/probability-42f89d4e9276e0f99495a89f.json` |
| `hoi4.probability_evaluate` (`mission_ai_will_do`) | `cbrn_occupation_decisions.txt` | `INTERNAL_ERROR`; exact message `Unexpected internal error`; no artifact, diagnostics, source revision, or scenario hash | No artifact returned |
| `hoi4.probability_render` | Protection evaluation | `PROBABILITY_ANALYSIS_NOT_CACHED`; exact message `Render requires an analysis ID produced by this server process` | No render artifact returned by this call |

The protection evaluator's scenario hash is `95911f2bcb590d731c2626a92f2139e03da670203153ab62c87de9a30588e052` and its analysis id is `probability-42f89d4e9276e0f99495a89f`.
The evaluator response also reported ranking, matrix, and unresolved visual resources, but its returned artifact list was truncated before every URI could be recovered; the complete JSON artifact URI above is retained.
The standalone render call could not reproduce those visual artifacts because the analysis was no longer cached by that server process.

Input-shape discovery produced these resolved MCP errors before the successful inspections: `Unrecognized key: "relativePath" at source`, `expected object, received string at source`, and `Source requires an identifier, path, inline Clausewitz source, or virtual patch at source`.
The accepted source form was `source: { path: "common/decisions/<file>.txt" }`.

## Named scenario fixture

Both evaluations used actor `CXT`, the candidate pool containing only the named mission id, and the following scenario ids: `stock_none`, `stock_exact`, `stock_above`, `target_eligible`, `target_ineligible`, `policy_available`, and `ai_affordability`.
Each scenario used a flat `state` map, `flags` array, and `scopes.FROM = { id: "FROM", state: ... }` record.

| Scenario id | Protection scenario inputs | Protective-aid scenario inputs |
| --- | --- | --- |
| `stock_none` | `has_equipment=false`, `any_controlled_state=true`, factories `2`; flags `cbrn_national_respirator_reserve`; FROM population `500`, raid-alert flag true | `has_equipment=false`, `custom_trigger_tooltip=true`, factories `2`; flag `cbrn_program_established`; FROM population `500`, raid-alert flag true |
| `stock_exact` | Same as `stock_none`, except `has_equipment=true` | Same as `stock_none`, except `has_equipment=true` |
| `stock_above` | Same primitive inputs as `stock_exact` | Same primitive inputs as `stock_exact` |
| `target_eligible` | `has_equipment=true`, `any_controlled_state=true`, factories `2`; reserve flag; FROM population `500`, raid-alert flag true | `has_equipment=true`, `custom_trigger_tooltip=true`, factories `2`; program flag; FROM population `500`, raid-alert flag true |
| `target_ineligible` | `has_equipment=true`, `any_controlled_state=false`, factories `2`; reserve flag; FROM population `0` | `has_equipment=true`, `custom_trigger_tooltip=true`, factories `2`; program flag; FROM population `0` |
| `policy_available` | Same as `target_eligible`, with `cbrn_program_established` also present | Same as `target_eligible` |
| `ai_affordability` | `has_equipment=true`, `any_controlled_state=true`, factories `0`; reserve flag; FROM population `500`, raid-alert flag true | `has_equipment=true`, `custom_trigger_tooltip=true`, factories `1`; program flag; FROM population `500`, raid-alert flag true |

The state map used trigger-name keys only and did not declare variables or compound fixture records.
The `stock_exact` and `stock_above` inputs are identical because the current adapter has no typed inventory-count fixture; they do not represent two different stock quantities.
The scenario set did not declare campaign external factors such as a concrete enemy country, target controller/owner relation, faction relation, or a bound trauma variable.

## Source and score evidence

`cbrn_supply_occupied_population` is a non-targeted 30-day mission with a re-enable cooldown and a base AI score from `constant:cbrn_protection_ai.base_civilian`.
The MCP trace resolved the base to `1` and applied the unconditional `occupied_state_factor` as `0.6`.
The `contaminated_state_factor` value `3` and `high_population_factor` value `2` were present in source, but their `any_controlled_state` conditions remained unresolved, so the final mission score and eligibility are unresolved.
The unresolved eligibility chain includes the `has_equipment` stock test, public chemical emergency, controlled-state distribution-work test, and factory affordability comparator.

`cbrn_deploy_protective_aid` has source AI base `constant:cbrn_occupation_decision_ai.protective_aid = 40`, with conditional own-core, allied-core, and positive-trauma factors of `5`, `2`, and `2` in `common/decisions/cbrn_occupation_decisions.txt` and `common/script_constants/cbrn_occupation_constants.txt`.
The evaluator internal error means none of those factors, target eligibility, score, or AI affordability were evaluated by MCP.
The source gates require an established CBRN program, positive gas-mask stock, at least 2 civilian factories available for projects, and a target state with a foreign controller, population, emergency, an occupied distribution gap, and no active protection or aid project.

## Completeness and classification

Both surfaces are `score_only`; the mission adapter explicitly has `normalizedProbability=false` and `timeDistribution=false`.
No result here is a click probability, normalized selection probability, or completion-time distribution.
The source inspectors found 7 and 3 weighted missions in their respective source files, while the evaluated pool contained only the named candidate, so cross-mission ranking and dominance are not established.
The adapter does not require a complete pool for raw scores, but the incomplete scenario state prevents a final score or eligibility claim.
The only exact protection score trace is the base and unconditional occupied-state factor; all conditional modifiers after that are unresolved.
No starvation, rank reversal, repetition, or positive-weight exploit conclusion is supported by these outputs.

## Recommended follow-up

Keep AI willingness evidence separate from the selection-time inventory reservation and do not tune the two AI weights from this partial baseline.
After the parent patch, rerun `mission_ai_will_do` inspection and same-scenario `probability_compare` for both exact ids, preserving these scenario ids and the pre-edit source hashes.
Treat `stock_exact` and `stock_above` as unresolved until the connected adapter provides a typed count for `gas_mask_equipment`; a boolean `has_equipment` only represents the positive-stock condition.
Treat target eligibility, policy, and AI affordability as unresolved until the adapter can bind the source's compound state/controller/factory gates without invented fixture keys.
Do not claim a changed selection probability from a changed reservation threshold because the mission adapter exposes willingness scores only.

## Skipped analyses and blockers

`hoi4.probability_sweep` was not run because the only scenario evaluation could not bind the inventory, aggregate-state, and factory-comparison inputs needed for a meaningful threshold sweep, and the parent directed this baseline pass to stop after the first evaluation attempt.
`hoi4.probability_compare` is deferred until the parent applies the patch; the occupation-side before artifact is absent because its baseline evaluation returned an internal error.
`hoi4.probability_simulate` and `hoi4.probability_sequence` were not applicable because no uncertain input distribution or complete custom pool with cadence/state transitions was declared.
`hoi4.probability_render` remains unresolved due to the cache error above, despite visual resources being listed in the evaluator response.
The baseline is incomplete for the occupation decision and bounded to exact intermediate protection-score evidence for the other decision.

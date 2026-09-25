# Event 006 REG-04 Karelia/Crimea Focus AI Probability Audit — 2026-09-26

Auditor role: chaosx_ai_probability_auditor.

## Status

**PARTIAL / weighted conclusion unresolved.** This is a read-only audit of the ten new REG-04 shared focuses and their imports in common/national_focus/006_independence_wave_focus.txt. No gameplay source was edited, no numeric AI weights were assigned, and nothing was staged or committed. Event 006 remains **HOLD/PARTIAL**.

The ten focus definitions contain no explicit ai_will_do block. They retain the existing default focus-selection behavior. This audit asserts no numeric base value for that default.

## Audited surface and source identifiers

The audited file is common/national_focus/006_independence_wave_focus.txt. Its focus-tree imports are at lines 79–88; the corresponding root-level definitions are at lines 4720, 4747, 4773, 4806, 4839, 4876, 4903, 4929, 4962, and 4995.

- KAR: independence_wave_kar_register_border_districts, independence_wave_kar_survey_forest_railheads, independence_wave_kar_guarantee_language_appeals, independence_wave_kar_commission_border_ski_guard, independence_wave_kar_publish_border_transit_docket.
- CRI: independence_wave_cri_register_tenure_petitions, independence_wave_cri_chart_peninsula_services, independence_wave_cri_ratify_land_hearings, independence_wave_cri_audit_peninsular_service_rolls, independence_wave_cri_publish_rights_and_transit_docket.

Source review shows per-country REG-04 gates on each group’s availability and branch eligibility, prerequisite chains, mutually exclusive branch choices, and branch-matched paid-receipt gates on the terminal docket choices. Those source facts do not certify live eligibility: compound triggers, state and capital control, bypasses, external focus factors, and AI strategy plans were not resolved by a complete scenario.

## MCP evidence

### Pre-edit baseline recorded in the accepted addendum

The 2026-09-25 baseline for national_focus_ai_will_do records source hash ee1def45cdf9a08de544e6abe30766508c5782827227cfb2df167996b9d79c91, 184 direct candidates, 17 required inputs, and poolComplete=false. The original inspect revision was 98efa694667fda026c12417c237b4f23507e180f235fd3a3cd1f8a9f2a0906a0; an independent auditor inspect reported revision b1970df39eafccca7aa15c72b2709848e6ae06c713903f5ea459e9e61466488d for the same reported source hash. Neither source-only inspect supplied a scenario result.

- Original inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14e3353681aba64fb15614057293529d0dbaf93ceffb83d8e81a4ae8c9b1905e/e91f8a79b5168de1236cde15797ab38553107ef4fc4784e5ea5334365431884a/probability-inspect-ee1def45cdf9.json.
- Independent auditor inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff43317b1b150fea32158e1598972a800700a7264b7b8434002926f37bfeae8e/7f135b8b6b583b7e75c304f1efe3a02cfcaf9bc95210bca7ac6f9623045feafc/probability-inspect-ee1def45cdf9.json.
- Prior scenario IDs: REG04_KAR_CURRENT_SHARED_TREE, REG04_CRI_CURRENT_SHARED_TREE, and REG04_DON_CURRENT_UNADMITTED.
- Prior scenario hash: 325423ccd7d955ef2c6f77355b47368a6febd773048c21af88c0690bdcd8e0f5.

The addendum characterizes those probes as partial because numeric Clausewitz variables and compound triggers could not be bound and imported roots were not certified. The exact saved scenarioSet values and a complete candidate-pool manifest are not present in the accepted addendum or matching plan handoff search results. The prior hash and scenario names alone are not enough to recreate the scenarios.

### Current probability inspect

The first call passed source as a string and was rejected by MCP validation (expected object, received string at source); it performed no analysis. The valid read-only call used source: { path: "common/national_focus/006_independence_wave_focus.txt" }, adapter national_focus_ai_will_do, refresh=true, and workspace mod_chaos_redux_ea3b2d67c2c0.

It returned PROBABILITY_SOURCE_INSPECTED / status=ok, source revision c0a2b187ac66600be61b7a8952b42fb0cb1ba0699baece00c4a815eca236433f, and MCP data.sourceHash 5663f8709a0a793f42571505b934eaa19390803bf151f238bfcb1b731a7eeb25. It reports 184 candidates, 17 required inputs, poolComplete=false, zero available candidates, an empty candidateExamples list, and zero source-unresolved items. The zero available count is a source-only result, not proof that no focus is available in a campaign. The 17 required inputs and incomplete pool prevent a scenario-level conclusion.

The current workspace file’s raw SHA-256 is 4faa5146983f3931008f16ceca21d491cdd3cf27a9e7eaa39fe8d0d54c3ba4e2. The inspect artifact’s candidate provenance records that raw file hash; the separate MCP data.sourceHash and source revision are retained above as returned. The repository HEAD version has raw SHA-256 4486871029b7def6872272dcd78f3f92bc8ee1b01428c9e973a71603834e334e, so it is not the recorded pre-edit source snapshot.

- Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5eeb8862243876f9551bc290ea5bd049b551170ce90d0661b7b6ced747485e6/ed743d321351c1c071b51b3a43e69210f38baacc7b12b3401cdc2c0a/probability-inspect-5663f8709a0a.json (1,048,316 bytes).
- Read evidence: the first 8,000-byte range was read and its metadata reported complete=false. The exact continuation URI is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5eeb8862243876f9551bc290ea5bd049b551170ce90d0661b7b6ced747485e6/ed743d321351c1c071b51b3a43e69210f38baacc7b12b3401cdc2c0a/probability-inspect-5663f8709a0a.json?offset=8000&length=8000. The remainder was not fetched after the user directed the audit to stop further MCP inspection.

The adapter metadata identifies focus selection as an independent-uniform maximum-score race, with evaluation cadence at the next-focus selection. It requires the complete eligible focus pool and declared country scope. It also states that ordered AI strategy plans can override weighted focus selection and that prerequisite-completion multipliers and external focus factors require scenario inputs. This is score-race evidence, not probability-proportional sampling.

### Structural focus inspect and render

This audit’s current hoi4.focus_inspect returned FOCUS_INSPECTED, revision 40333af8c469371944a4bd22129f52ef9dcfab3c4e995bdf3cad650e23565b70, 184 direct nodes, 196 connectors, and layout hash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7. It did not include the root-level imported shared focuses. The user-provided fresh inspect revision 27fae753a2a481e0a45453cae07b4044063d129d5b5da3eef34375164b0d1d38 reports the same 184-node / 196-connector count and the same import omission; these are distinct receipts, not a single revision.

- Current inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/568e077eb7e9c624230cdad11a4f43ab168692ace52055a9265ad6de06737c41/9cd81ccd7504697ab5dac1cad3d573b6567d2ae9da389f6372045af1d0050541/focus-inspect.40333af8c4693719.json.
- The inspect also reported one long connector and a missing localisation reference for the generic continuous focus continuous_restrict_freedom_desc; neither diagnostic evaluates these ten imported choices.

The read-only hoi4.focus_render returned FOCUS_RENDERED for independence_wave_focus_tree, with the same layout hash and a rendered canvas of 21424 × 2440. Because its inspected tree omits the imports, this render is not visual evidence for the ten new shared focuses.

- HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/146ee3f258da5f7644a1b769b4a929f79e0e41e49b0f75de687b67824d820a52/67b97845c81c219be264231dbc7cf404c4414538fbd38c51aa50824083c2cdcb/independence_wave_focus_tree.focus.html.
- SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/f55287b5b743f631277c956beab628372b4108332b0a5ea991c8e28822dde027/independence_wave_focus_tree.focus.svg.
- JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da16003773dfa4e30c69596e44138349524224db4c62f309401ae91b54f4c4dd/533de3029450f0c35584235f271e6b05979647082e29e5cd7d1a9a2b8b7ecb77/independence_wave_focus_tree.focus.json.
- Source map: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39898857c8fc1acd3325fd57b0cd1ee4b924f948e69db0b531cfbafa3d15eb19/86d8ad9d5c7e203df03137b63c4001aa13ee4fbafb9538217bc798d980764d/independence_wave_focus_tree.focus.source-map.json.
- Plan metadata: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdc6cc803e0e37b94fc14fd8caccab7956a1b84c9ba8baa8164d43bb994dd691/42260e6a151d476fb9a145ee37726f61be7d98d63e527fa42f636980c0ad9007/independence_wave_focus_tree.focus.plan.json.

The prior structural baseline recorded in the addendum was revision 150b4ac59bee8157299553f269192bd0b84824c0d44943bc5d051acdf2165137, also 184 nodes and 196 connectors with layout hash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7. Its inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb08f0ddfbc30d82ca5f729736445c9381d548c502195b3e5c97413c1bf7538d/38aaef5cc169dc705ff3f8077a3727ecbeef162ec7b36cb331c89f8b6cfcb039/focus-inspect.150b4ac59bee815.json.

## Scenario coverage and comparison status

| Scenario ID | Exact scenarioSet recoverable? | Candidate pool | External factors and inputs | Valid current result |
| --- | --- | --- | --- | --- |
| REG04_KAR_CURRENT_SHARED_TREE | No. The exact actor/state/flags/scopes values are absent; do not reconstruct them from the ID. | Baseline and current inspections each report 184 direct weighted candidates and poolComplete=false; the ten imported roots are not certified by the adapters. | Incomplete. 17 inputs are reported; numeric variables, compound gates, prerequisite/bypass state, and external/strategy factors are not bound. | None. Prior probe was partial; current inspect only. |
| REG04_CRI_CURRENT_SHARED_TREE | No. The exact actor/state/flags/scopes values are absent; do not reconstruct them from the ID. | Baseline and current inspections each report 184 direct weighted candidates and poolComplete=false; the ten imported roots are not certified by the adapters. | Incomplete. 17 inputs are reported; numeric variables, compound gates, prerequisite/bypass state, and external/strategy factors are not bound. | None. Prior probe was partial; current inspect only. |
| REG04_DON_CURRENT_UNADMITTED | No. The exact actor/state/flags/scopes values are absent; do not reconstruct them from the ID. | Baseline and current inspections each report 184 direct weighted candidates and poolComplete=false; the ten imported roots are not certified by the adapters. | Incomplete. The unadmitted DON state and external factors are not declared in an exact reusable scenario. | None. Prior probe was partial; current inspect only. |

hoi4.probability_compare was not run. Its mandatory same-scenario comparison is blocked because the exact prior scenarioSet is unavailable and the exact pre-edit source exists only as a recorded hash/revision plus inspect artifact, not as a saved source path. The available repository HEAD file is not the pre-edit snapshot. Per the local subagent evidence contract, an inspect artifact, source hash, or revision is not a substitute for the before.path; comparing the current source to itself would be invalid.

hoi4.probability_evaluate was not run because no faithful scenario object and complete candidate pool can be supplied without inventing actor state or eligibility. hoi4.probability_sweep was skipped because no valid scenario inputs or weight paths for threshold/sensitivity/rank-reversal analysis are available; no new numeric weights were introduced. hoi4.probability_simulate was skipped because no uncertain-input distribution and seed were declared. hoi4.probability_sequence is not applicable because this is not a declared custom weighted pool with cadence and state transitions. hoi4.probability_render was not run because no valid analysis ID exists to render. The user then directed that no further MCP inspection be performed.

## Weight and campaign findings

- Exact source finding: none of the ten new shared-focus blocks introduces an explicit numeric ai_will_do value or modifier.
- Base values and modifier traces for those ten focus IDs: not returned by the weighted adapter because the new shared roots are not included in its discovered 184 candidates.
- Rankings, selection probabilities, timing distributions, and normalized chances: none established. No exact probability claim is valid.
- Eligibility and route validity: source text contains package gates, prerequisites, branch exclusions, and paid-receipt gates, but live trigger state, hidden/bypass state, and imported-node resolution remain uncertified.
- Positive weight on impossible/dead/hidden choices: unresolved for the new IDs; no positive numeric weight was added in their source blocks.
- Dominance, starvation, rank reversal, repetition, and exploit/snowball risk: unresolved. There is no scenario-complete pool or comparison result. No weight-driven repetition or snowball finding is supported.
- The 184-candidate count is a discovered weighted-source count, not the complete set of choices in a live next-focus race. The source-only availableCandidates=0 result is not a campaign eligibility result.

## Recommended follow-up, not applied

1. Keep all ten IDs on their existing default focus-selection behavior in common/national_focus/006_independence_wave_focus.txt; this audit provides no evidence for adding or tuning numeric AI weights.
2. Before any route-aware weight patch, make the probability adapter and focus index resolve the ten root-level imported shared focuses, and require the complete available-focus pool plus declared prerequisite, bypass, strategy, and external-factor inputs.
3. Recover the exact pre-edit source snapshot and the exact saved scenarioSet for all three REG-04 scenario IDs. Then rerun inspect, evaluate/sweep where inputs support them, and compare the exact same scenarios before making a weighted conclusion.

## References, skipped scope, and handoff limits

The audit followed chaos-redux-subagents and chaos-redux-focus-trees. It consulted the offline Paradox wiki core pages required by AGENTS.md, including AI modding, AI focuses, and National focus modding, and searched the vanilla documentation markdown for focus, AI-weight, strategy-factor, and prerequisite guidance. The relevant rule is that focus AI is a score race whose high score wins; it must not be described as ai_chance-style probability-proportional sampling.

No event, focus, trigger, helper, strategy, localisation, or other gameplay files were edited. This audit does not certify gameplay reward balance, country-package trigger implementation, or the live focus UI for the ten omitted imports. No full feature-completion claim is made.


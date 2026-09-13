# Event 006 infrastructure gate probability evidence

Date: 2026-09-05

This is a read-only probability handoff for the parser correction in `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`. The parent applied exactly 32 replacements of the bare `infrastructure_level > constant:random_civil_war_value.zero` form with `check_variable = { infrastructure_level > constant:random_civil_war_value.zero }` and preserved the state, owner, controller, population, tag, and dormancy gates.

The retained prepatch snapshot is `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event6_infrastructure17/006_independence_wave_event021_adapter_registry_triggers.txt` with source hash `65852B58C0041753E126D0A2ED165B70A4A2C554925EE4F7DDAB7A148A10AFF0`, 8961 bytes, and 32 target rows. The parent reports postpatch source hash `3DDE81D9845C74FEF57D8D089256A69D682D4A937CE410D19600B34DFADCEFC7`.

## Probability inspection

The mandatory trigger inspection used `hoi4.probability_inspect` on `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`. It returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason: no_weighted_surfaces`, zero candidates, and zero unresolved inputs. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce655f6356ad3c879e40e9d0ae2c9e2181d8721505e7d4160e52742d15da0cc7/d8bc150724619523a3398f2ed16fcf58e8a6ae517505ccbb1620535c70bb56ab/probability-inspect-cffee71e5f70.json`.

The weighted caller inspection used the `random_list` adapter on `common/scripted_effects/021_random_civil_war_parent_effects.txt`. It found two categorical pools and eight entries, including the six Event 021 archetype entries at line 1070 and two unrelated strange-incident entries at line 5194. The adapter reported `completePoolRequired: true` and `MULTIPLE_CATEGORICAL_POOLS` until a single pool is selected. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87137c78a71055332897afea6aec7fd7ce693a7eeca4809de9e3cef3435c8fd2/e4d87ea98afecac79a54a775b1a3cf4e1135c468287840ca3372ad00c8c3e99f/probability-inspect-b3edc2585d8f.json`.

## Declared six-entry baseline

The bounded evaluation used adapter `random_list`, the six entries below, and scenario set `E6_INFRA_PARSER_BASELINE_2026_09_05`.

- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.1`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.2`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.3`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.4`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.5`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070.entry.6`

`E6_INFRA_ZERO_INVALID_ANCHOR` supplied the five non-Event006 route weights as `var:` values of 80 and Event006’s declared route weight as 0. `E6_INFRA_POSITIVE_VALID_ANCHOR` supplied all six declared route weights as 80. The complete evaluation returned analysis `probability-2cff514d3e6a80addbd15a5e`, scenario hash `b68580b42e8da7041124924fd63a1504a4ca0c448e45d5c02665619776a9b778`, 12 candidate rows, zero unresolved rows, and one `PROBABILITY_STARVED_OUTCOME` warning for the Event006 entry in the zero-weight scenario. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/218de9aaf654972cdf79ec807dfdc747dbfeaf96836ce7c90afaeced5c4c5827/363fc4feda7f17a5b188a19dd33365fea77f37f69ee2360b64f87796d30ab9e7/probability-2cff514d3e6a80addbd15a5e.json`.

The baseline ranking and matrix renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7cff284de545eb06bbe5db483c4de92d5b8d3d5addd556fa2f986c818ba7037b/fc2c1c94887fdd6bf35736c82cb1b7a5458ad7e3cd34fa4a8306f41b5ba93258/probability-probability-2cff514d3e6a80addbd15a5e-ranking.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95119e301359798168f4c846436ff63225a85fed0d6f3e67c27ddb57251c3a53/d158a7909b85c930845aff6c8bd7d5e89062f25d51b0dd8f232688d5fe2e929e/probability-probability-2cff514d3e6a80addbd15a5e-matrix.png`.

This result is exact only for the declared six-entry fixture and unresolved for campaign behavior. The fixture supplies route weights directly; it does not supply state infrastructure, the 32 anchor/carrier pairings, owner/controller/population checks, dormancy scope, or the complete actor pool. It therefore does not prove that an infrastructure-zero or infrastructure-positive state propagates to Event006 availability or to the downstream random-list weight.

## Same-scenario before/after comparison

The required `hoi4.probability_compare` used `random_list`, the same six candidates, the same scenario set and IDs, and exact `inlineClausewitz` bodies from the archived prepatch trigger and current postpatch trigger. The path-only attempt correctly found no weighted block in the trigger source; the full inline comparison returned the same result: status `error`, code `PROBABILITY_SURFACE_EMPTY`, no analysis ID, no comparison artifact, no files scanned, and blocker `No weighted blocks matched this request`.

The comparison is an MCP capability boundary, not evidence that the parser correction has no gameplay effect. The trigger is an eligibility gate and is not itself a probability surface, while the downstream weighted caller is in a separate source file. Actual infrastructure/availability propagation and any resulting weighted-target change remain unresolved by MCP.

## Classification and skipped analyses

The trigger inspection and trigger comparison are `unresolved` for probability impact. The six-entry random-list evaluation is `exact` within its declared fixture and `unresolved` for campaign behavior. No live dominance, starvation, repetition, rank-reversal, exploit-risk, or balance conclusion is made for the real actor pool.

`hoi4.probability_sweep` was not run because the changed surface has no evaluable weighted block and no declared infrastructure-to-weight projection or sensitivity range. `hoi4.probability_simulate` was not run because no uncertain input distributions were declared. `hoi4.probability_sequence` was not run because no complete custom-pool cadence, cooldown, recovery, cap, removal, reset, or terminal-state manifest exists. No compare render was emitted because the MCP comparison produced no analysis.

The baseline evaluation emitted source revision `a86d66c20e45e9ef06d323874e204f13df32f14143d9fbdb6fb110ac43a7a289`, while the earlier inspect emitted revision `555481ad2f21d4be52be987ab01f2902c14190ab63af9d79bc87ed5283c566a6`; the caller source hash was `b3edc2585d8faa4fc75ba6b5937cc8ccd234868298f0f61ac9c725d8030abf1e` in the evaluation. This MCP revision discrepancy is retained as metadata uncertainty and does not change the empty trigger comparison result.

The earlier probe using unprefixed variable names was partial with six unresolved inputs and is not evidence; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0765122fe8852787db2002c136cd0ccfcfb78a84b63f347d506631cb73124cc/dbdad8b8914ccc9efcfcdbc4c1a801f510e11f792efb0435a080d25d463f0502/probability-ae06663a873f271021079e8a.json`.

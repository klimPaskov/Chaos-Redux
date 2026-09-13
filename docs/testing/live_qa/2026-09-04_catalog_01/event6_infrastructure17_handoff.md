# Event 006 adapter infrastructure trigger repair

Disposition: parser correction implemented and accepted by parent-owned launch 18, with unresolved MCP probability propagation.
Acceptance basis: the parent authorized only an isolated parser correction of the 32 infrastructure comparisons in the protected Event 006 adapter registry.

## Scope and source proof

The only authorized gameplay file is `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`, lines 10–41, inside `independence_wave_event021_dormant_package_available`.
Each row contained `infrastructure_level > constant:random_civil_war_value.zero` directly in an explicit state scope.
Each comparison is wrapped as `check_variable = { infrastructure_level > constant:random_civil_war_value.zero }`.
The operator remains strictly greater than, the zero constant remains unchanged, and the read remains in the same state scope.

Installed vanilla `documentation/dynamic_variables_documentation.md` defines the state scope at line 1096 and `infrastructure_level` at line 1133.
Installed vanilla `documentation/triggers_documentation.md` lines 2110–2132 documents `check_variable` and its short greater-than form.
Vanilla `common/decisions/MTG_congress.txt` line 400 reads `infrastructure_level` inside `check_variable` in a state scope.
The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` game-variables section and `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` variable-comparison entry support the same access pattern.
The existing `state_population_k` gate is a documented trigger and is outside the repair.

The parent-supplied `logs/launch_16/logs/error.log` records 32 `Invalid trigger 'infrastructure_level'` entries for registry lines 10–41, with accompanying unknown-trigger messages.
The source baseline contains exactly 32 fully matching rows and has SHA-256 `65852B58C0041753E126D0A2ED165B70A4A2C554925EE4F7DDAB7A148A10AFF0`.

Preserved state-to-carrier crosswalk: `121:SCO, 122:WLS, 14:BRI, 34:AFX, 36:AGX, 51:RHI, 52:BAY, 42:AJX, 100:ICE, 165:CAT, 1:COR, 114:ARX, 115:ASX, 84:TRA, 82:AXX, 106:MAC, 184:BAX, 185:BBX, 104:BOS, 105:MNT, 802:KOS, 146:KAR, 73:RUT, 234:KUB, 137:CRI, 249:TAT, 651:BSK, 230:ARM, 231:GEO, 229:AZR, 629:HAW, 378:HBX`.

## Existing helper contract

`common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.md` documents this country-scoped availability predicate.
It returns true when at least one admitted package has its exact owned and controlled populated anchor, sufficient infrastructure, and a dormant reusable carrier.
It has no mutation side effects.
Direct consumers are `event021_parent_event6_dormant_candidate` and `event021_parent_event6_secondary_front_candidate` in `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` at lines 58 and 319.
Those consumers gate Event 021 opening or additional-front admission, so a read-only probability auditor established a source-discovery baseline before the owner applied the patch.

No helper extraction, new constants, tuning change, target lifecycle change, cleanup change, or call-site migration was made.
No localisation, UI, assets, catalog facts, or Event 006 package membership changes are required.

## MCP evidence and validation limits

The linked Event 021 root was inspected with `hoi4.event_inspect`, selector `{ kind: "event", eventId: "chaosx.nr21.1" }`, depth 1, 8 nodes, 12 edges, and helper expansion disabled.
The result was `EVENT_INSPECTED_PARTIAL`, revision `1e7516fb00135d5559a8dfcc786dbeaeac9e3850d4f17dad626bbe811df96bc0`.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52ce303551823996a2854839ebd43b2b581094cade8587fe5504fa29e11c3022/78c589efc6741982d1a48414d6ae8f18f651e0445598fe330f548464a06cf32b/event-trace-1e7516fb0013.json`.

The matching `hoi4.event_render` neighborhood returned `EVENT_RENDERED_PARTIAL` with layout hash `3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbed6186fc40f167265a8e2f737a0cb7033b76ab3c9a02e5f3e787783092569a/8da678354eb31121e9f7dd03cc2057ce693fb467f37e9037671908d42a99e569/event-neighborhood-1e7516fb0013-manifest.json`.
Both event routes reported failed full validation because workspace-wide helper projections and lifecycle passes were deferred.
They provide partial chain evidence and do not prove the adapter's runtime evaluation.
The post-edit `hoi4.event_compare` requested the recorded baseline revision with `refresh = true` and returned `EVENT_REVISION_NOT_CACHED`, with no comparison artifacts.
The exact blocker states that the requested event graph revision is not cached.
No successful event-graph comparison is claimed.

## Backup and exact patch verification

Backup: `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event6_infrastructure17/006_independence_wave_event021_adapter_registry_triggers.txt`.
The source and full-byte backup both matched baseline SHA-256 `65852B58C0041753E126D0A2ED165B70A4A2C554925EE4F7DDAB7A148A10AFF0` immediately before writing.
Post-edit source SHA-256: `3DDE81D9845C74FEF57D8D089256A69D682D4A937CE410D19600B34DFADCEFC7`.
Exactly 32 wrappers were added, and removing only those wrappers recovers the entire original text exactly.
The complete file, both direct consumer contracts, and all 32 state/carrier pairs were reviewed.
No other gameplay source file was edited in this subtask.
The parent reported that launch 18 completed, stopped, and was archived with this source hash stable.
All 32 targeted invalid-infrastructure-trigger records were absent, and the parent identified no new diagnostic family beyond the aggregate count.
This is parser acceptance for the bounded correction, not proof of runtime route eligibility or probability propagation.

## Probability baseline and limitations

The read-only `chaosx_ai_probability_auditor` inspected the availability trigger and its actual random-list caller before the patch.
The trigger inspection returned `PROBABILITY_SOURCE_DISCOVERED` with zero weighted candidates.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce655f6356ad3c879e40e9d0ae2c9e2181d8721505e7d4160e52742d15da0cc7/d8bc150724619523a3398f2ed16fcf58e8a6ae517505ccbb1620535c70bb56ab/probability-inspect-cffee71e5f70.json`.
Caller inspection returned `PROBABILITY_SOURCE_INSPECTED` for a random-list adapter.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87137c78a71055332897afea6aec7fd7ce693a7eeca4809de9e3cef3435c8fd2/e4d87ea98afecac79a54a775b1a3cf4e1135c468287840ca3372ad00c8c3e99f/probability-inspect-b3edc2585d8f.json`.

The auditor evaluated the actual six-entry random list under declared `var:` weights with scenario names `E6_INFRA_ZERO_INVALID_ANCHOR` and `E6_INFRA_POSITIVE_VALID_ANCHOR`.
Analysis ID: `probability-2cff514d3e6a80addbd15a5e`.
Scenario hash: `b68580b42e8da7041124924fd63a1504a4ca0c448e45d5c02665619776a9b778`.
Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/218de9aaf654972cdf79ec807dfdc747dbfeaf96836ce7c90afaeced5c4c5827/363fc4feda7f17a5b188a19dd33365fea77f37f69ee2360b64f87796d30ab9e7/probability-2cff514d3e6a80addbd15a5e.json`.
The first fixture manually declares Event 006's route weight as zero, and the second manually declares equal positive weights for all six routes.
These calculations establish only the result of the declared weight inputs.
They do not demonstrate infrastructure-value evaluation, nested availability propagation, actual runtime weights, or campaign probabilities.
The patch owner therefore treats the infrastructure-dependent probability result as unresolved and makes no balance claim from these fixtures.
The complete actor pool, external modifiers, and runtime cadence are unavailable to this evidence pass.
The required `hoi4.probability_compare` used adapter `random_list`, the same six caller candidates, scenario set `E6_INFRA_PARSER_BASELINE_2026_09_05` with the same two scenario IDs, and exact archived/current trigger bodies through `inlineClausewitz`.
It returned `PROBABILITY_SURFACE_EMPTY` with the blocker `No weighted blocks matched this request`, no analysis ID, and no comparison artifact.
This trigger-source request did not provide a supported nested-gate projection into the separate downstream weighted caller.
The comparison therefore supplies no probability-impact result for the repair.
Full auditor evidence and skipped-analysis reasons are recorded in `docs/testing/live_qa/2026-09-04_catalog_01/event6_infrastructure17_probability.md`.

## Simplifications, omissions, and blockers

No game launch or commit is authorized for this subtask.
Native startup parser acceptance is established by the parent-owned launch 18 evidence.
Infrastructure-dependent probability propagation remains unresolved.
No gameplay simplification or fallback was made.
Skills used: events and subagents, with decisions/missions consulted for the vanilla decision precedent.
No skill changes are required.

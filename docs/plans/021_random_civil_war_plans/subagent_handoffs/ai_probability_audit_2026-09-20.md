# Event 021 Random Civil War — Independent AI Probability Audit

Date: 2026-09-20

Status: incomplete and non-certifying. This handoff records read-only source review and the bounded HOI4 MCP evidence available from the installed `hoi4-agent-tools` 3.0.7 route. It does not claim Event 021 balance, completion, or acceptance.

Scope: automatic Event 021/MTTH, target selection, archetypes, opening severity, Evolution I secondary routes, Evolution II sponsor/relief/no-aid and strange incident, settlement selection, Wars cluster overlap, SCN-018 shares and Maximum admission, Event 021 decision and mission AI scores, and Event 021 AI strategy factors.

No gameplay, AI, event, focus, decision, mission, strategy, localisation, source, or workbook file was modified. The checkout was already dirty and concurrent source/index drift was observed; unrelated work was preserved.

## Evidence classes

`Exact current MCP projection` means the analyzer evaluated the declared complete pool at the recorded MCP source revision and scenario hash. It does not prove that the pool or source revision equals the final local checkout when the local SHA256 differs.

`Bounded` means exact only for the declared subset or projection, with omitted engine state explicitly listed.

`Score-only` means a willingness or AI score trace; it is not a click probability or a normalized selection probability.

`Source-only` means the implementation was read, but the installed probability adapter did not expose a usable candidate pool or timing surface.

`Cached/historical` means the artifact came from an earlier audit revision and is retained only as comparison context, not as current proof.

`Unresolved` means that the route, pool, state, or external factor needed for the requested conclusion was unavailable or failed validation.

## Required references and audit commands

The following were read before auditing: `AGENTS.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-mtth/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-event-planning/SKILL.md`; all 41 files in `docs/specs/021_random_civil_war_specs/`; current Event 021 source and documentation; and the prior Event 021 probability and decision/mission handoffs.

The offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding were read. The relevant vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\` was also read, including script concepts, effects, triggers, modifiers, and dynamic variables.

Read-only repository commands used included:

```powershell
Get-ChildItem -LiteralPath '.\docs\specs\021_random_civil_war_specs' -Recurse -File
Get-Content -Raw -LiteralPath '<required-file>'
rg -n 'ai_will_do|ai_chance|random_list|mtth|ai_strategy|SCN-018|Maximum|event021' '<source-or-doc-path>'
Get-FileHash -Algorithm SHA256 -LiteralPath '<source-file>'
```

The installed package was checked at `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\package.json`; reported version is `3.0.7`. The MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

The probability calls were made through `functions.exec` using the installed `mcp__hoi4_agent_tools__hoi4_probability_*` routes. Each family began with `hoi4.probability_inspect`. The bounded workflow used `probability_evaluate` for named fixtures, `probability_sweep` where a numeric range was accepted, and `probability_render` in the same tool process as an evaluation when a render was required. `probability_compare`, `probability_sequence`, and `probability_simulate` were not substituted with hand calculations.

Representative call shapes were:

```text
hoi4.probability_inspect(workspaceId, source={path, adapter}, refresh=true)
hoi4.probability_evaluate(workspaceId, probabilitySourceSchema, scenarioSet, scenarios, horizonDays, metrics)
hoi4.probability_sweep(workspaceId, probabilitySourceSchema, scenarioSet, path, steps, findRankReversals)
hoi4.probability_render(workspaceId, analysisId, views=[ranking,matrix,sensitivity,threshold,unresolved])
```

The installed route uses `horizonDays`, not `horizon`. Render calls made in a later MCP process returned `PROBABILITY_ANALYSIS_NOT_CACHED`; combined evaluate/render calls succeeded and are the render evidence retained below.

## Revision integrity and source anchors

The local checkout snapshot captured during the audit included these key SHA256 values:

| Local source | Local SHA256 |
| --- | --- |
| `events/021_random_civil_war.txt` | `0480E9EBB1FA78096A081A0B597AE8B1072B149D66C9990C5B32B1433D59685E` |
| `common/mtth/021_random_civil_war_mtth.txt` | `6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F` |
| `common/script_constants/021_random_civil_war_constants.txt` | `37DDEF2A1D2589B8B13F287A3781113AB6551759744A173772A2C1D9439B69AC` |
| `common/scripted_effects/021_random_civil_war_effects.txt` | `C76F3D62A3B4FC22CE8A902AB437F24A301EBF579AAB14E4067ED53561774FBC` |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `4A1BEC7A1873C03BF56057EBA8D6D5CDB82F73FD363207ACE47EBFE10A0A9A81` |
| `common/scripted_effects/021_random_civil_war_decision_effects.txt` | `9710EF99472F49856E0419216DF1D5E494FE6482885922976376F916FA62274B` |
| `common/decisions/021_random_civil_war_decisions.txt` | `327E272A69DCD4B8A40D1488BD4D34F33C3BC56A891D7527BB133B26A258B593` |
| `common/ai_strategy/021_random_civil_war_ai_strategy.txt` | `6ADBB93B2CD17665C4BD967368F08BC953738D81DB7A2069171241F45C309DCA` |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16` |
| `common/scripted_effects/chaosx_settings_effects.txt` | `03698706BA40C213CD1855D6250CE106F6D991A9963073EF8C4B8C23C956039C` |

MCP revisions changed during the audit. For example, the latest parent-effect MCP snapshot was `487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367`, while earlier successful evaluations used `a79b53a3e41881722a351c149511b0d584a44c5499e94b477dd5a8495c7e500b`; the latest decision snapshot was `a3b71dc76ec0f4bf2726a3fc7aec82bba7b488f5114613cc69f908092bdbd93e`; and the event source snapshot was `76551f3aa8c52c488d79804a81a95a0b96781970e40c40da3091b79992f988c6`. The corresponding MCP source hashes also differ from the local hashes above. Therefore a current-MCP result is exact to its recorded MCP revision, but no before/after or local-checkout certification is safe.

Current source anchors reviewed were:

| Weighted surface | Source and identifier |
| --- | --- |
| Automatic timing | `common/mtth/021_random_civil_war_mtth.txt`, Event 021 Evolution I/II/III MTTH entries; automatic enqueue logic in `common/scripted_effects/chaosx_settings_effects.txt` |
| Target score | `common/scripted_effects/021_random_civil_war_effects.txt`, `event021_random_civil_war_prepare_target`; shared candidate/validity helpers in `common/scripted_effects/individual_crisis_targeting_effects.txt` and matching triggers/constants |
| Archetype | `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `event021_parent_select_archetype`, current random-list entries at the observed line 1155 |
| Opening severity | `common/scripted_effects/021_random_civil_war_effects.txt`, `event021_prepare_opening_severity` |
| Evolution I secondary route | `common/scripted_effects/006_independence_wave_effects.txt`, Event006 region random list at observed line 3621 |
| Settlement | `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `event021_parent_select_settlement_terms`, observed line 4591 |
| Strange incident | `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `event021_parent_roll_strange_incident`, observed random-list line 6911 |
| Sponsor/relief/no-aid | `common/decisions/021_random_civil_war_decisions.txt` and `common/scripted_effects/021_random_civil_war_decision_effects.txt` |
| Wars cluster | `common/scripted_effects/chaosx_event_cluster_effects.txt`, `common/script_constants/event_cluster_constants.txt`, Event004/Event007/Event021 cluster registrations |
| SCN-018 | Event 021 parent scenario controller and `docs/specs/021_random_civil_war_specs/` scenario documents for `SCN-018` |
| AI strategy | `common/ai_strategy/021_random_civil_war_ai_strategy.txt`, 12 Event 021 role blocks |

## Surface results

### 1. Automatic event and MTTH timing

Source values are Evolution I base 90 days, Evolution II base 135 days, and Evolution III base 120 days. The source contains named modifiers for authority failure, large country, extra actor, near defeat, settlement progress, no extra actor, border route, sponsor, Event006 independence-front exposure, multifront exposure, strong neighbor, no exposure route, and severe/critical opening. The implementation header states that a stage is sampled once when unlocked, stored as an absolute due date, and processed by a bounded transition queue rather than a periodic world scan.

The required first inspect was:

```text
source: common/mtth/021_random_civil_war_mtth.txt
adapter: event_mean_time_to_happen
code: PROBABILITY_SOURCE_DISCOVERED
sourceRevision: 487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367
sourceHash: c55a108bcbf249ce1d76875506cd0fe4b8c8db79646c426b503ba036d72405b8
candidates: 0
discoveryReason: no_weighted_surfaces
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f961d2f989b8b26dc969b91d26a4c245ebdcad4a900833bd5cc09f558499e5c5/546b2ef3d199bf172ba9d501f5c948caa548996102884f4f7a7ee13df2a68292/probability-inspect-c55a108bcbf2.json
```

The automatic-source inspect on `common/scripted_effects/chaosx_settings_effects.txt` likewise returned `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, candidates 0, source hash `ac44527164587019a8be0f5cc2b11297a5f42e5fdd15e7d5f41e1fe042d58f89`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e14dbcc7aafdbe8d3583c8d9f826bf46497e0eabf44dbf569f8ccb8e87bd7b7/37bbe633b013c172e3b4082a06304f8a19ff58b3e4591404a46223715923e001/probability-inspect-ac4452716458.json`.

Named evaluation fixture `event021_mtth_named_timing_fixtures_2026_09_20` contained `EVO1-01-AUTHORITY-FAILURE`, `EVO2-01-EXPOSED-SPONSOR`, and `EVO3-01-SEVERE`, but returned `PROBABILITY_SURFACE_EMPTY` with no weighted blocks and no available adapters. An initial invalid metric attempt also returned the exact validation error `MCP error -32602: Invalid option: expected one of conditional_probability|raw_value|cumulative_chance|effective_mtth_days at metrics[2]`; retrying with valid metrics did not expose the surface.

Classification: source-only for the MTTH formulas and queue contract; unresolved for exact timing distributions, effective MTTH under named modifiers, and automatic incidence. No sequence or simulation was run because no complete timing/state-transition manifest or declared uncertain input distribution was available.

Recommended fix: expose the three MTTH entries, all modifier values, clamping, due-date sampling, queue cadence, and terminal transitions through a 3.0-compatible timing adapter or provide an accepted complete manifest before claiming timing probabilities.

### 2. Target pool and target score

The source score starts at `base`, adds pressure multiplied by 4, authority-failing and authority-collapsed bonuses, valid actor-route bonus, major-stage bonus, nearby-conflict exposure, recent-memory penalty, subject bonus, player marker bonus, and major-target multiplier. Reserved candidates are forced to the minimum. The score is clamped to the configured minimum and maximum, rounded, and only scores above the minimum become target-pool candidates. The parent projection converts final ticket weights to a capped 1-to-10 ticket count.

Required live-source inspections did not discover a normalized candidate list:

```text
source: common/scripted_effects/021_random_civil_war_effects.txt
adapter: custom_weighted_pool
code: PROBABILITY_SOURCE_INSPECTED
sourceRevision: 487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367
sourceHash: 4a7693932e4f5ef9941fdbb2e1fdca37a1a69a190a2bbcd9a7bca8eb9505f0b5
poolComplete: false
candidates: 0
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f4aed8253ac59bb9c04c5cb08d5ea15d80fa603e9cb2cd1a3586df6777d0143/fbae54c55ce8f5e7286243e7ca97ad331b627f26e2f6cafe4b495bd1a1f0ed46/probability-inspect-4a7693932e4f.json
```

The shared helper inspection was also incomplete: source hash `fe7abecca820a057ef92e0a84a37fccef7341ae423578a1cfa08fcad5be27561`, candidates 0, `poolComplete: false`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7413ab27f48a81b7e9b3194d5200e3ba9f8b9665887fdd7d92e4ac3852dae4b/e673ac43df2aa8fb781b5fad2d0c4aaa08de4543466e22687201d39f877cd6ee/probability-inspect-fe7abecca820.json`. The parent custom-pool inspection likewise returned candidates 0 and `poolComplete: false`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/33114bd52015c62acc0129570cb948e895e5f59bd41b3aa189efdaa635c3f5d4/ae0cb4a14b2e08608a8b2bf132608b3072aaf8d0e013dcf6258ccc7cea5d04a0/probability-inspect-1758b110b57a.json`.

A declared projection manifest `event021_target_ticket_projection_2026_09_20_render` was separately inspected and evaluated as a complete four-candidate categorical pool. Its manifest-only inspect returned `PROBABILITY_SOURCE_INSPECTED`, source revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`, source hash `cd8d988e72d08aa76ecdf4301d57a788acbfcbdad078eefb9724e3d21be0bb88`, candidates 4, unresolved 0, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/824aff4e7de24eb148104b290c231e09f4c500e247b00ba54ec473557ca0eeb1/c8f1c7bf53ceec7e316562c3667316d04f9317738ba8c5807ee1f53166bbf4e3/probability-inspect-b695c8587591.json` for the earlier manifest revision. The fresh render fixture evaluation used scenario set `event021_target_ticket_projection_render_scenarios_2026_09_20`, scenario hash `be2bd813063881e155024997bda17e8bedf40995cbc61aef8827811e83149014`, analysis `probability-25c1427ce78e7ad19f487e1c`, code `PROBABILITY_ANALYZED`, candidates 40 across ten scenarios, unresolved 0, and diagnostics 2.

The projection scenarios were `TGT-01-STABLE`, `TGT-02-AUTHORITY-FAILING`, `TGT-03-AUTHORITY-COLLAPSED-MAJOR`, `TGT-04-RECENT-MEMORY`, `TGT-05-RESERVED-EXCLUDED`, `TGT-06-MAJOR-STAGE`, `TGT-07-NEARBY-EXPOSURE`, `TGT-08-SUBJECT-ACTIVE-LOAD`, `TGT-09-PLAYER-MARKER`, and `TGT-10-ONLY-MAJOR`. In the declared projection, `TGT-10` normalized to major 1.0 and the reserved candidate was ineligible. This is an exact projection result, not a live-country candidate-pool result.

Render artifacts for the projection were:

```text
JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7419620e5348632240a2554486bb21e300de620c3ee8cbeddbf49f7ad60e47f/a30de0c9c674887e13a8dcee188d5b819fd7d451bcf754e44a9840b7c93c6347/probability-25c1427ce78e7ad19f487e1c.json
Ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05475821c47d82ecbbec0457739a50245f4470f9daf0ac27904c6b7014850d88/273a39a2eb4d269a1cc57eb6d39c05924fae598bd8ed2e3dc0430756ee5b0785/probability-probability-25c1427ce78e7ad19f487e1c-ranking.svg
Matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fea0b848f9859360e9c0ab31b68451d0fcf72eef938849b1f7a6198f6f3c1f6b/38f8ef6ba6f27cdafe3e69c018fd527799722a939f55ad0ece8b1f6222458f2f/probability-probability-25c1427ce78e7ad19f487e1c-matrix.svg
```

Classification: bounded exact projection plus source-only live scoring. The complete live country pool, eligibility, target reservation, shared-load state, route validity, and external modifiers were not exposed.

Recommended fix: expose the live country candidate/provider array and all eligibility, reservation, load, route, and modifier inputs, or approve a complete manifest that includes those states. Verify that the rounded 1-to-10 cap does not collapse intended score differences.

### 3. Archetype selection

The current parent random list has six explicit candidates: `event021_parent_select_archetype:entry.1` ideological, `.2` legal, `.3` regional, `.4` command, `.5` Event006, and `.6` same-tag. The preparation effect initializes all six to the minimum and assigns the valid actor-route value of 80 to valid routes, so invalid routes are intended to have zero weight.

Required inspect:

```text
source: common/scripted_effects/021_random_civil_war_parent_effects.txt
adapter: random_list
code: PROBABILITY_SOURCE_INSPECTED
sourceRevision: 487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367
sourceHash: 1758b110b57a6afbaaa0fd45fc955f2ffbce661222236f32f82ac8e4b1edc9c0
poolComplete: true
candidates: 6
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37fbb696318863dfaa98a25659ef87262950912f728f359791fa6c95fabcc006/4f351ff8a4c13b65814f5c95d08cb23a4d471f87a248bd565f64049aa908aae3/probability-inspect-1758b110b57a.json
```

Scenario set `event021_archetype_current_var_fixtures_2026_09_20_rerun` used `ARC-ALL-ROUTES-100-VAR`, `ARC-NO-EVENT006-VAR`, and `ARC-IDEOLOGICAL-ONLY-VAR`, with direct state weights of 100 or 0. The evaluation was `PROBABILITY_ANALYZED`, analysis `probability-075d414cc596046530be2202`, scenario hash `71528b6a4b253c7842c757f57d949bb28a4a60bec82ce831ab219151e64f146b`, candidates 18, unresolved 0, diagnostics 7. The exact declared-pool projections are 1/6 each when all six are 100, 1/5 each for the five remaining entries when Event006 is 0, and 1.0 ideological when it is the only positive entry. The diagnostics identify Event006 starvation when its weight is zero and route starvation under the ideological-only fixture.

Combined current-revision rendering used `event021_archetype_render_fixture_2026_09_20`, scenario `ARC-RENDER-ALL-ROUTES`, analysis `probability-cc251741e808d319b23a6f6e`, source revision `487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367`, source hash `1758b110b57a6afbaaa0fd45fc955f2ffbce661222236f32f82ac8e4b1edc9c0`, scenario hash `29def144a5f7b6ec89e0f66068cadb37488ecc6f3d1219f558ad04b58f859483`, candidates 6, unresolved 0, diagnostics 0. Artifacts:

```text
JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15cf6cdd05f94bc45f0c993b237bee1d71a1ed37f0510537d428b9ddd1b60ba5/e29c1a567d373ece25d1e37b636971ed4b610069f19ae706db62b2e92474d37f/probability-cc251741e808d319b23a6f6e.json
Ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cac0a3c247ae784311f9166587a5750ffe25aa94bb8e814c319e6e53d14a6925/a1de5df777fd5f8c4b6668ee894a9e02f4f23373ce4289a2842d36f77893fd22/probability-probability-cc251741e808d319b23a6f6e-ranking.svg
Matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f34ad0607408c1d5731e5534bb69bb892967e3995ae733a9fc31cc94f52decc2/53204b938d144711cd7a5a6cded403c7c816a7efe03e5a6d17edcecaa63aaef6/probability-probability-cc251741e808d319b23a6f6e-matrix.svg
Unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/ee9a3af95de2d396fce3d0b4c8c10a3003842c0a743834c78f8d11f05ecea5ba/probability-probability-cc251741e808d319b23a6f6e-unresolved.svg
```

Classification: exact current MCP six-entry projection, not exact campaign archetype probability. Live country/route validity and state-derived weight construction remain outside the adapter evidence. No rank reversal was certified.

Recommended fix: keep invalid archetypes at exact zero and test each route with complete actor, topology, Event006 package, and same-tag admission fixtures before tuning positive weights.

### 4. Opening severity

`event021_prepare_opening_severity` is deterministic rather than a normalized weighted race. It assigns limited, serious, severe, or critical from pressure/authority/topology inputs and forces the limited state for a one-state route. No separate probability candidate pool was available.

Classification: source-only and unresolved for severity frequency and downstream timing. No probability inspect/evaluate route was able to prove a distribution. Recommended fix: provide named bounded severity fixtures and expose the deterministic state classification plus any upstream uncertainty; do not describe severity as a random selection without that evidence.

### 5. Evolution I Event006 secondary routes

The Event006 region pool has 14 explicit candidates at the observed random list line 3621: `entry.1` through `entry.14`, each corresponding to `independence_wave_region_01_total_weight` through `independence_wave_region_14_total_weight`.

The first symbolic candidate inspection returned `PROBABILITY_SOURCE_DISCOVERED`, `candidate_pool_not_found`, and `availableCandidates: 14`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e68115e1bc34e6b843db3eb66f1a9318b2688cb9812957d649d5384f1b112b07/bcf88a8d66d6bdfa768062b33207743800f7c60516bb91b3b081f654f4acda98/probability-inspect-ee0c5925279c.json`. The corrected inspect was complete:

```text
code: PROBABILITY_SOURCE_INSPECTED
sourceRevision: a79b53a3e41881722a351c149511b0d584a44c5499e94b477dd5a8495c7e500b
sourceHash: ee0c5925279cecc711fcda9f08635861ad0d676e783786b08ade6b3157d038ec
poolComplete: true
candidates: 14
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3c2ce93a6c3835972c4f0a40d0f9bc5826ed2efb06ab493daeff6531e3ac57d/734934cd9ed8e86c178247cc8cb2ba289438589abfb0f31c136e029ae62cc9a7/probability-inspect-ee0c5925279c.json
```

The corrected evaluation used `event021_event006_render_fixture_2026_09_20` with `EVO1-EVENT006-REGION-01-02-RENDER` and `EVO1-EVENT006-REGION-14-ONLY-RENDER`, source hash `ee0c5925279cecc711fcda9f08635861ad0d676e783786b08ade6b3157d038ec`, scenario hash `f910322dcaa7a6d69cfd04b594adf7fc4f3a4599ef94a744e42a2a9ebcb125db`, analysis `probability-424ac2a0583621d923deb5b7`, code `PROBABILITY_ANALYZED`, candidates 28, unresolved 0, diagnostics 26. With declared weights region 1 = 100 and region 2 = 50, the exact projection is 2/3 and 1/3; with only region 14 positive, region 14 is 1.0. Zero-weight entries were diagnosed as starved. Artifacts:

```text
JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b7cee6b7c04af55999b8b545d9d2038ebe7057f1f16491e4347d71a4ceaa671/475cfa37b14765a00d3b87b0072a0b180086bf261aaef96f56eeec68dd520389/probability-424ac2a0583621d923deb5b7.json
Ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f3c7cd74f6b828e5c2b73a78075b1402feb5a20c0feebc4d41b16b4017b37db/c1635f78fb72e0b34581572b1e4bdfb552ef4646d28a54672eb47d852a278754/probability-probability-424ac2a0583621d923deb5b7-ranking.svg
Matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3ffb8ae687ece7e1bf4a96035a7c54292cc40b880a1dc5c292619fd48014398/1ee0267f1dedac87a82fbf6135c4a7cd92e3ee67530995fde6a8ae140eaf1370/probability-probability-424ac2a0583621d923deb5b7-matrix.svg
Unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/60f13846b7b08191ea15c0722adea9503641a821ae6d90997c4bb45bd4aef66e/probability-probability-424ac2a0583621d923deb5b7-unresolved.svg
```

The attempted sweep accepted `steps: 5` but returned `sweepPoints: 1`, analysis `probability-e350e5bc5ad55e1bd21861fd`, scenario hash `886f24a3c91ddcd0b454ad9926f2b20b779e706e07a76518111672024fa321a6`, so no sensitivity or rank reversal is certified. Its render artifacts were JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62c4c1e2f40e7abcf8714f82408810cb42245953d2fdc4808133b78cc7d243ca/e857de474ab82ef98eb69f5274e8ad6c8f2bd377b0057987cc38e8bdab2c5ba1/probability-e350e5bc5ad55e1bd21861fd.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa9088bbf229ca23fa67d363059e0f667d82c5725df18ceb940cbecc86627cad/1096d623542da6981d62b3a9a3dceaeea28dd181a8e0052ebfcd444bdf30c906/probability-probability-e350e5bc5ad55e1bd21861fd-ranking.svg`, sensitivity `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c580a37b1f8d1652565d09c5d4916cfb64780fe1117555854ef1a506942b912d/7c9d31fda356468b1bac337cfcd089a858d0955a44a906607c1a30b60435e724/probability-probability-e350e5bc5ad55e1bd21861fd-sensitivity.svg`, and threshold `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef9a65cd023e6dfc2bcb4f71837702307b041ee90f65b766b5387d7b841a2199/24629122ce257396b5bc599838385d0be0d09c834bcb523e05f97aa108a63a42/probability-probability-e350e5bc5ad55e1bd21861fd-threshold.svg`.

Classification: bounded exact Event006 region-pool projection. It is not exact Event021 secondary-route probability because Event021 route admission, anchor validity, package completeness, parent topology, cooldown, and cross-route priority were not supplied.

Recommended fix: expose the complete Event021 secondary candidate pool and route/package admission state, then run a sequence with cadence, removal, reset, cooldown, and terminal state declarations.

### 6. Evolution II sponsor, relief, no-aid, and strange incident

The current decision source contains 18 Event 021 decisions, including sponsor support, relief, mediation, commitment end, reconstruction, disarmament, coalition governance, communications, and regional administration. All have base `ai_will_do` score 1, with source modifiers including priority-major 1.5, zero gates, and 0.75 discouragement. Sponsor choices include target validity/viability, neighbor action, resources, opportunistic sponsor, aligned target, rival target, and cooldown/commitment conditions.

The strange-incident inner pool has two explicit candidates at `event021_parent_roll_strange_incident` line 6911: the strange incident entry weighted by `var:event021_parent_strange_incident_weight` and the no-strange entry weighted `.92`. The incident path is gated by Evolution II active state, logs enabled, active country, no recent incident, and a 30-day cooldown; its side effects include authority decrease and pressure increase.

Required inspect:

```text
adapter: random_list
code: PROBABILITY_SOURCE_INSPECTED
sourceRevision: 487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367
sourceHash: 1758b110b57a6afbaaa0fd45fc955f2ffbce661222236f32f82ac8e4b1edc9c0
poolComplete: true
candidates: 2
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a03e75908c97d5db57102f3cf0abc458d43e68b05d1d0790bd108bae230b0b0/b1878eadcd492814cd978a81e356d6ac704117c0e6e6911554011ab4a74dca14/probability-inspect-1758b110b57a.json
```

The current inner-pool evaluation used `event021_strange_incident_current_inner_pool_2026_09_20_rerun`, scenarios `STR-01-BASELINE-EVOL-II-VAR` and `STR-02-LONG-LIVED-HIGH-CHAOS-VAR`, and scenario hash `4ca5c3c6364ce01d88b7de8a55393458c9555ceb31a6bc06f60c296a34cdcf7a`. It returned `PROBABILITY_ANALYZED`, analysis `probability-b154ec67a80e27909a727e40`, candidates 4, unresolved 0, diagnostics 3. The declared conditional inner result is strange incident .08 and no-strange .92; the no-strange entry was dominant in both scenarios.

Fresh combined render used `event021_strange_incident_render_fixture_2026_09_20`, scenario hash `46e7df48cc6086ffc3dc52155b1ccf2525fdf999ed9b8b1c6b296fe40cca164a`, analysis `probability-5d2bbcfecbbafa0f61c1add7`, source revision `487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367`, candidates 4, unresolved 0, diagnostics 3. Render artifacts:

```text
JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60eb0426882d14777379c697ab77bb5fd5544d3dd954e7142b77ce04ddd938bb/434a3baeb98d5357d2dee8f01504a08d83fae5fd532fa1c30e77b3e0d278eae7/probability-5d2bbcfecbbafa0f61c1add7.json
Ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f89e28848dc395733573d8de63be5248988a24b84f8dc98cbb529d0331c2350c/dc57ee3202370b9ff8361ae28db62fc0c82d56e0b53d60727e89625b627f0c9c/probability-probability-5d2bbcfecbbafa0f61c1add7-ranking.svg
Matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/491cc375fbad4e90293921e26f8bd1ae7c130128306d7412117588a4ea3adea5/8526c26481741dfe8e13001fe2b686ec4b84246384d9bc82cf4825b0f5dff917/probability-probability-5d2bbcfecbbafa0f61c1add7-matrix.svg
Unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/7faff5e7193cf308750560e695bcc2a1a0b2966262cdaff93707ac49bb12f4ae/probability-probability-5d2bbcfecbbafa0f61c1add7-unresolved.svg
```

Classification: exact current-MCP conditional inner pool only. Overall strange-incident incidence is unresolved because outer active-side gates, recent-incident memory, cooldown, event logging, repeated-cycle reset, and terminal states are outside the evaluated pool.

Historical sponsor score evidence from `probability_sponsor_postrepair_2026-09-02.md` is cached/historical only. Its three-candidate fixture reported SPN-01 government 1.6875, opposition 0, mediation .75; SPN-02 all 0; SPN-03 government and opposition 1.6875 with mediation .75; SPN-04 mediation 1; and SPN-05 mediation 1.5. Historical scenario hash was `07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3`, sweep hash `08d00630206417d93ffd8dc60285334cb2b4a5d06a1e1fe2e20c2a91316b3155`, analysis `probability-4e1958dacabd56d2217cd407`. These scores are not current normalized sponsor probabilities.

Recommended fix: provide complete typed target scopes, resource states, neighbor-action validity, commitment caps, cooldowns, and cleanup/terminal transitions. Keep the .08/.92 conclusion labelled conditional until the outer cadence is evaluated.

### 7. Settlement selection

`event021_parent_select_settlement_terms` is deterministic precedence, not a normalized random pool. Source precedence is Event006 independence, opposition victory, same-tag leverage/autonomy/coalition/government, partition, merger, negotiated settlement with authority and regional-route conditions, then government victory.

No probability adapter exposed a settlement candidate pool. Classification: source-only and unresolved for settlement frequency, repetition, and post-war state distribution. Recommended fix: expose a complete bounded topology/signatory/post-war state sequence if settlement outcomes are to be treated probabilistically; otherwise document this as a deterministic precedence chain.

### 8. Wars cluster overlap

The Wars cluster source contains Event004 as required tier 0 low primary, Event007 as optional tier 1 medium primary, and Event021 as optional tier 0 medium primary. The cluster id is Wars, cooldown is 120 days, and optional activation uses tier base, severity, eligible count, fatigue, optional participation, multiplicity, and clamping formulas.

Required inspections of `common/scripted_effects/chaosx_event_cluster_effects.txt` with `custom_weighted_pool`, `random_list`, and `direct_random` all returned `PROBABILITY_SOURCE_INSPECTED` but `poolComplete: false`, candidates 0, and no usable normalized surface. Latest source revision was `487433803f314a106d53189018c48695b014675f2a61d66c5943b0c5e308d367`, source hash `afd2c5961b9dd2cdd74269bd379b6b4d5b8c78c75ba3da4886fb0671b751c284`; custom-pool artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b5a6ad33ccf944d2c7e4391c163bafbbfc35af051126daeb8dfde1d65f1dd12/2eb300fb5b62e241aeb766a5fc05365277657ba83eb7199f985cb69a1d77d9dd/probability-inspect-afd2c5961b9d.json`.

Classification: source-only. No overlap probability, activation probability, dominance, or starvation conclusion is certified because the complete live member pool, eligibility, reservations, fatigue, cooldown, and multiplicity state were not provided.

Recommended fix: expose Event004/Event007/Event021 member rows and all cluster-level reservations/fatigue/cooldown inputs, then evaluate named low/medium/high and overlap fixtures using the complete pool.

### 9. SCN-018 scenario shares and Maximum admission

SCN-018 is `The Fracture Cascade`. Source shares are low .10, medium .25, high .50, and Maximum 1.0. Low/medium/high use target ticket weights minor/major of 4/1, 2/2, and 1/3 respectively. Maximum freezes every country passing normal-human, topology, route, capacity, opening-state, terminal-lock, successor-grace, active, target-reservation, and cluster-reservation preflight, then visits each frozen row once; nonhumans are excluded and countries created during the same run cannot join.

No live probability adapter exposed a complete SCN-018 eligible-country pool or a Maximum freeze/visit sequence. The source inspection and review therefore prove the algorithmic admission conditions only. Classification: source-only and unresolved for actual share counts, country admission count, target selection, timing, and Maximum performance. Do not treat .10/.25/.50/1.0 as click probabilities or as realized country shares without a complete eligible-country fixture.

Recommended fix: provide low/medium/high fixtures with counted eligible minor/major candidates and a bounded Maximum sequence containing the frozen snapshot, per-row visit state, terminal state, and same-run-created-country exclusion.

### 10. Event option `ai_chance`

The current event source inspection discovered 11 options: `chaosx.nr21.1.skip`, `chaosx.nr21.2.a` through `.9.a`, `news_event_021_multi_front_war.a`, and `news_event_021_global_fracture.a`. The required option pool was not certified complete because one unresolved presentation/context input remained.

```text
adapter: event_option_ai_chance
code: PROBABILITY_SOURCE_INSPECTED
sourceRevision: 76551f3aa8c52c488d79804a81a95a0b96781970e40c40da3091b79992f988c6
sourceHash: d8275e2107ffde3195eb3d451fc839c7fe0b99ce201d9aeb2321ccd21572b61
poolComplete: false
candidates: 11
unresolved: 1
artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d756657baa43aaa81737247acad4cc750dbb5568de1ac41362cf5757d808a688/457d858728d66c79fad38d8e4c7396bfa6137c5ac45689cdc5b6f8ecea753db8/probability-inspect-d8275e2107ff.json
```

The named fixture `event021_event_option_ai_chance_smoke_2026_09_20` with `EVT-OPTIONS-EMPTY` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-c524f41bf0c465e33b312080`, scenario hash `9bf85ad4f22e4ff17cda052fdc47e5b0900f515024beb3f9bd7a8438e1a90768`, candidates 11, unresolved 1, diagnostics 1. Normalization was withheld. An explicit path attempt returned `PROBABILITY_SOURCE_DISCOVERED`, `candidate_pool_not_found`, and `availableCandidates: 11`, confirming the path naming blocker.

Classification: bounded discovery only; no event-option selection probability. Recommended fix: expose the complete presentation-eligible option pool and typed event context, including all target and branch callbacks, before normalizing `ai_chance`.

### 11. Decision and mission AI scores

The final decision inspect found the complete 18-decision pool with source revision `a3b71dc76ec0f4bf2726a3fc7aec82bba7b488f5114613cc69f908092bdbd93e`, source hash `f6f4996120567f9aef7e32719d1c7a986fcfc751bd5fd35d95ac0500f3d26e74`, `poolComplete: true`, candidates 18, required inputs 12, unresolved 0. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a447db000ad2d232e199766e1b45ddaf303f3b8b0064e1c49ea74ba9d756983/0dd82398e2daf37f465db6ee09601c4f17fe7f8d96c6318739bf94bfcb4867f4/probability-inspect-f6f499612056.json`.

The 18 candidates were `event021_secure_arsenals`, `event021_defend_capital`, `event021_review_loyalty`, `event021_seize_depot`, `event021_open_relief_corridor`, `event021_offer_emergency_settlement`, `event021_reconstruct_administration`, `event021_integrate_formations`, `event021_set_priority_front`, `event021_monitor_border`, `event021_support_government`, `event021_support_opposition`, `event021_offer_mediation`, `event021_end_sponsor_commitment`, `event021_complete_disarmament`, `event021_complete_coalition_governance`, `event021_protect_communications`, and `event021_review_regional_administration`.

The final mission inspect found the complete three-mission pool at the same revision/hash, candidates 3, required inputs 3, unresolved 0. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59c990d63a1d68897316780b4a93c4f07a5d2e74ee680fe1163cd2cb5a07a6dd/2dc34624d8caa41f2460a0d91a8a23b10f86870f52b00d172676ab120c0c294d/probability-inspect-f6f499612056.json`. The missions were `event021_hold_the_capital_mission`, `event021_secure_rail_spine_mission`, and `event021_hold_settlement_terms_mission`.

The current empty-context decision fixture `event021_decision_ai_render_fixture_2026_09_20` / `DEC-EMPTY-CONTEXT-RENDER` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-2bd9f21cb15f44f75c7a76bf`, scenario hash `1271260c7939ab31d04e4819bdda1998d580dfe966e6de3a2ac38f58f9f0eadf`, candidates 18, unresolved 48, diagnostics 16. The current empty-context mission fixture `event021_mission_ai_render_fixture_2026_09_20` / `MIS-EMPTY-CONTEXT-RENDER` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-67134e87c874fbf77eaca8d0`, scenario hash `35c5d6b0c3f90962810e4d0c6302d968482a2f0eff697fb173b04e8de31ced0a`, candidates 3, unresolved 6, diagnostics 4. Decision diagnostics included unsatisfied priority-major/discouragement inputs; mission diagnostics included the capital mission never eligible and priority-major unsatisfied. These are score traces only, not decision click probabilities.

Current render artifacts were:

```text
Decision JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ae8f206a9d462d27e6370e77b23bc04be0bfbb39eb8d017610d33f2b57b78f0/42bede556e4560b0b8530530c70f6af28a6cdfc21973dc40fac21cea35d2c6fd/probability-2bd9f21cb15f44f75c7a76bf.json
Decision ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0f465f4791b002912a947707e4d99ad797499918bd7e95038a9b4f38eb63c0b/cde45ace6824be6dd4d0ccd50475e5776b3e2171993fa978544074183b2b39f5/probability-probability-2bd9f21cb15f44f75c7a76bf-ranking.svg
Decision matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07c746c05c48b3c7d6af49c8d28929ff55934bebb94bc2ffa77cb01e23c80ff4/01c5995fd248dfddcef1f6c1250cb7868a7571f2757e9f3ac1c5b3daef3ddca4/probability-probability-2bd9f21cb15f44f75c7a76bf-matrix.svg
Decision unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/235e5b2303b7a27dfc28c8771b43df6fa6ae452bbaab83511c8f8d8274d8b196/71f6d055255dc1e9b9ed2d5c2b282d91d2167aa9e40786d34283dabe89e9d7fb/probability-probability-2bd9f21cb15f44f75c7a76bf-unresolved.svg
Mission JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e7809fa79e66007ec6433661977f62dddf44f51edc504a29420cbdb614f5f61/f4cd1060196af3fa784a9f9745e179f0ffe93e60a5edf53180af1c71118e7abb/probability-67134e87c874fbf77eaca8d0.json
Mission ranking: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3b253924c7eca3314c68bb679ce04909df5a91d82ae38ad2513d16db98ae7d0/32400b77a15a7c8f26f5326ce88785ceb85576180ac3338f8845de30682458cf/probability-probability-67134e87c874fbf77eaca8d0-ranking.svg
Mission matrix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb2f3516a53afdadb14111e057575bade5e3199e3d219fb0a6488a261ccbff57/ec1ef26a165e66a2de066faddbde403053d61e6016a20fad9fa2ab02e244dfd9/probability-probability-67134e87c874fbf77eaca8d0-matrix.svg
Mission unresolved: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef93c595e5d258148a72acde8a554d824c0b4f69be64fe090674437581180d7b/620327134e30a9fe3e66f01747cb07faacdf5167e9550a7b327c5f88d424fb48/probability-probability-67134e87c874fbf77eaca8d0-unresolved.svg
```

Decision and mission sweep attempts were blocked by the exact 3.0.7 error `PROBABILITY_SWEEP_RANGE_REQUIRED: Every sweep path requires scenario range, numeric alternatives, or numeric state value`, including attempts over `constant:event021_ai.priority_major`, `hidden_trigger`, `has_variable`, `custom_trigger_tooltip`, and the front-state variable. No current sensitivity or rank reversal is certified.

Classification: complete candidate discovery, current score-only partial evaluations, unresolved probability. An `ai_will_do` score race is not a click probability; decision cadence, visibility, availability, target scope, resource state, active-side capacity, and engine selection behavior remain incomplete.

Recommended fix: create typed fixtures for every availability/visibility/target/resource/cooldown path and use a complete decision score race only if the engine adapter explicitly supports the selection cadence. Compare before/after with the same named fixtures after an owner-applied change.

### 12. Event 021 AI strategy factors

The strategy source contains 12 role blocks: `event021_government_consolidator`, `event021_government_hardliner`, `event021_government_negotiator`, `event021_revolutionary_claimant`, `event021_constitutional_claimant`, `event021_independence_actor`, `event021_command_claimant`, `event021_neighbor_containment`, `event021_neutral_mediator`, `event021_opportunistic_sponsor`, `event021_survivalist_successor`, and `event021_global_prevention`.

The required inspect with adapter `ai_strategy_factor` returned `PROBABILITY_SOURCE_DISCOVERED`, `no_weighted_surfaces`, candidates 0, source revision `c69e8afef944896674d69268260908dda8147e209b3e89886c0d1523f6915a47`, source hash `74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ece9158cfe92da5d9010ef9abbd7730165078315865d63072cf719df8a7ab82/43b9ef602c18ccf34bef944408fd62d8c592dfc4557bda48cf8db79831cba556/probability-inspect-74d73084d977.json`.

The named evaluation `event021_ai_strategy_factor_empty_surface_2026_09_20` / `STRAT-ROLE-SURFACE` returned `PROBABILITY_SURFACE_EMPTY`. Strategy factors are source-level plan modifiers, not direct click or selection probabilities. Classification: source-only and unresolved for composition with other AI strategies.

Recommended fix: analyze strategy composition only through a supported AI-strategy adapter that exposes the active strategy pool, factors, decay, expiry, and consumer race. Do not normalize the 12 role blocks as a probability pool.

## Structural event evidence

The required read-only structural event pass used `hoi4.event_inspect` on root `chaosx.nr21.1`, trace mode, both directions, `expandHelpers=true`, `maxDepth=3`, `maxNodes=200`, `maxEdges=400`, and refresh. It returned `EVENT_INSPECTED_PARTIAL`, revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, graph hash `c83030c9d67b704f9c6437d31b7e4f5000463e6431ae40865f5b74e4cb15af21`, events 9745, options 15179, entries 1157, unresolved nodes 8763, terminals 7768, edges 38408, state accesses 30547, and issues 2198. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4bba40cbf960fe654699ca0a851ead4dd607a3ba58f1d7880cf28f70f9014d4/e2c02777d3e5ca68b196b6adffe0dfcf98c648cf5313e805e14468d7c3d33ccc/event-trace-a8fde3e58546.json`.

The structural render returned `EVENT_RENDERED_PARTIAL` with timing manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f44f1bf.../55c873.../event-timing-a8fde3e58546-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b69fb.../f1c635.../event-timing-a8fde3e58546.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a7baff.../c2cb56.../event-timing-a8fde3e58546.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3f970.../880862.../event-timing-a8fde3e58546.png`; the server response reported omitted nodes 42612, selected nodes 0, branch renders 0, and deferred validation. The ellipsized URI components are retained exactly as returned in the MCP transcript but are not safe as clickable artifact identifiers here.

A later bounded `state_flow` inspect with `expandHelpers=false`, depth 4, node cap 200, edge cap 400, and refresh returned the exact blocker `INTERNAL_ERROR: Unexpected internal error` and no artifact. No further retries were made.

## Cross-surface findings

The only exact normalized results in this audit are declared-pool projections: six-route archetype fixtures, the two-entry .08/.92 strange inner pool, the 14-entry Event006 region projection, and the four-entry target-ticket projection. They do not establish campaign-level incidence or timing.

Potential dominance and starvation are proven only inside declared fixtures: one positive archetype dominates when all others are zero; the strange no-incident .92 entry dominates its inner pool; zero-weight Event006 regions are starved; and a single eligible target-ticket class normalizes to 1.0. These are not claims about the live campaign until the omitted eligibility and cadence state is supplied.

No current rank reversal was certified. Event006 sweep accepted `steps: 5` but produced one point. Strange sensitivity also produced one point on the successful retry. Decision and mission sweeps failed the range requirement. No comparison id exists because no safe before/after source pair was available.

No `probability_sequence` was run because the required complete custom pool, cadence, cooldown, recovery, cap, removal, reset, state transitions, and terminal states were not declared for the automatic, target, Evolution, cluster, or SCN-018 surfaces. No `probability_simulate` was run because no uncertain input distribution and seed were explicitly declared. No `probability_compare` was run because the checkout and MCP source revisions drifted and no authorized before/after candidate pair existed; using historical artifacts as a current baseline would be misleading.

The primary exploit-risk questions remain unresolved: whether target rounding creates repeated major-country admission, whether reserved/blocked countries can retain positive tickets, whether sponsor relief can repeat without a commitment cap or cleanup, whether strange incidents can recur after cooldown without a terminal/reset guard, whether cluster optional rows overlap with Event021 active reservations, and whether SCN-018 Maximum admission can change while its frozen snapshot is being visited.

## Recommended fixes without applying them

1. Stabilize or pin the MCP source revision to the checkout before any compare or baseline certification.

2. Expose the live target provider, complete country pool, eligibility gates, reservation state, shared load, route validity, and score modifiers through a 3.0-compatible probability adapter or a complete accepted manifest.

3. Add typed timing fixtures for MTTH modifiers, one-time due-date sampling, queue cadence, clamp behavior, and terminal transitions.

4. Add full Event021 route fixtures for archetype and Evolution I secondary admission, including Event006 package validity and same-tag topology.

5. Add complete decision and mission fixtures with typed scopes, resources, target validity, visibility, availability, cooldown, commitment caps, and cleanup; preserve score-only labeling unless a click-selection adapter exists.

6. Expose the complete Wars cluster member pool and SCN-018 eligible-country snapshot so overlap and Maximum admission can be evaluated as bounded sequences.

7. Re-run the same named scenarios through `probability_compare` after an owner-applied change; do not tune from the historical sponsor artifact or from source-only normalization.

## Blockers and skipped analyses

- Installed route is `hoi4-agent-tools` 3.0.7. Version-gated 3.1 helper expansion and job routes were not requested or used.
- Automatic MTTH and AI strategy adapters returned `PROBABILITY_SURFACE_EMPTY` or `no_weighted_surfaces`.
- Live target and Wars cluster pools were not discovered by the probability adapter.
- Event option pool remained incomplete with one unresolved input.
- Decision and mission evaluation was partial because empty context left 48 and 6 unresolved inputs respectively.
- Sweep ranges were not accepted for decision/mission paths; accepted sweeps returned one point for Event006 and strange-incident sensitivity.
- Target projection sweep rejected the 3.0.7 manifest shape with `MCP error -32602: Invalid input: expected object, received undefined at source; Unrecognized key: "customPoolManifest"`.
- MTTH invalid metric retry produced the exact metric validation error recorded above, and valid metrics still left the surface empty.
- Symbolic Event006 and event-option candidate paths returned `candidate_pool_not_found` with available candidates listed, so no guessed path was substituted.
- Structural Event 021 state-flow inspection ended after the bounded call with `INTERNAL_ERROR: Unexpected internal error`.
- Separate render calls failed with `PROBABILITY_ANALYSIS_NOT_CACHED`; successful render evidence was obtained only by evaluating and rendering in the same MCP process.
- Compare, sequence, and simulation were skipped for the exact completeness reasons stated above.

## Acceptance classification

This handoff is not accepted as a complete balance audit. Current acceptance by surface is: MTTH unresolved/source-only; target unresolved with bounded projection; archetype exact declared-pool projection only; severity source-only; Evolution I bounded Event006 projection; Evolution II sponsor/relief/no-aid score-only partial and strange inner pool exact conditional only; settlement source-only; Wars cluster source-only; SCN-018 source-only; event options incomplete; decisions and missions score-only partial; AI strategy source-only. A parent review and a stable current-revision MCP rerun are still required.

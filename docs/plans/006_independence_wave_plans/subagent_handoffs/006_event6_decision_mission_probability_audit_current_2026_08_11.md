# Event 006 decision and mission probability audit — current worktree — 2026-08-11

## Verdict

**HOLD / UNRESOLVED for current weighted-AI and probability claims.** This was a read-only audit. No gameplay, decision, mission, AI-strategy, trigger, constant, localisation, or runtime file was changed.

The current worktree exposes 44 `common/decisions/006_independence_wave*.txt` files with 642 source-level `ai_will_do` blocks and 39 matching category files. The category files contain no `ai_will_do` or `ai_chance` blocks; they contribute visibility, allowed, target, map, and GUI gates only. This count is a source scan, not an MCP candidate-pool count.

The mandatory current `hoi4.probability_inspect` pass is blocked before source parsing. The installed server returns `ARTIFACT_MANIFEST_INVALID` with the exact message **“Artifact provenance manifest is invalid”** for valid Event 006 sources in workspace `mod_chaos_redux_ea3b2d67c2c0` (an absolute-path retry returned `INTERNAL_ERROR` / **“Unexpected internal error”**). Therefore there is no current MCP source revision, artifact URI, scenario hash, ranking, sensitivity, timing, or normalized selection probability to report. All current probability conclusions are **unresolved**.

## Scope and exact sources

The audit covered the Event 006 decision and mission families requested by the parent:

- Shared allocator and state decisions: `common/decisions/006_independence_wave_decisions.txt` (current local SHA-256 `c4bbd83e7b43ca346da3db9f0ebd30d587c683cae23b575d58b88c28a33a8273`).
- Emergency/crisis mission: `common/decisions/006_independence_wave_crisis_decisions.txt` (current local SHA-256 `2c16cf8ebcaab607c01ee531de3d8feaadb7b7e8f8ba057d14f13ff2203bd19b`).
- SCN-008 navigation/ledger controls: `common/decisions/006_independence_wave_scenario_decisions.txt` (current local SHA-256 `1eb8811dfde8b6a2f447ce0e5d3ca89183224041a2477f6abe7eeb39279a85d6`).
- Regional/package decisions: `common/decisions/006_independence_wave_banat_decisions.txt`, `..._bosnia_decisions.txt`, `..._brittany_decisions.txt`, `..._catalonia_decisions.txt`, `..._epirus_decisions.txt`, `..._ice_decisions.txt`, `..._karelia_crimea_decisions.txt`, `..._kosovo_decisions.txt`, `..._macedonia_decisions.txt`, `..._montenegro_decisions.txt`, `..._ruthenia_decisions.txt`, `..._thrace_decisions.txt`, and `..._transylvania_decisions.txt`.
- Formable/registry families: `common/decisions/006_independence_wave_form01_02_04_decisions.txt`, `..._form03_decisions.txt` (current local SHA-256 `838cec4dcc43f72bbf888248c6640b8f9c427182a143f01872439cbbffd8479a`), `..._form05_decisions.txt`, `..._form08_decisions.txt`, `..._form09_decisions.txt`, `..._form39_decisions.txt`, `..._form48_decisions.txt`, and `..._formable_registry_decisions.txt` (current local SHA-256 `52332cf1e93ae893aa74f8ec6baf3003ff69a6e2e9c73670acda600b0e8d0856`).
- Other regional/overlay sources: `..._evolution_incident_decisions.txt`, `..._iberian_decisions.txt`, `..._iw005_flanders_decisions.txt`, `..._iw022_dalmatia_decisions.txt`, `..._iw025_vojvodina_decisions.txt`, `..._iw035_livonia_decisions.txt`, `..._iw043_iw058_decisions.txt`, `..._iw059_mesopotamia_decisions.txt`, `..._iw085_cyrenaica_decisions.txt`, `..._iw093_iw098_decisions.txt`, `..._iw101_iw102_iw105_cog_overlays_decisions.txt`, `..._iw156_iw196_iw197_iw204_overlays_decisions.txt`, `..._mediterranean_decisions.txt`, `..._pacific_decisions.txt`, `..._rhineland_bavaria_decisions.txt`, `..._rival_bloc_decisions.txt` (current local SHA-256 `5fe28984016393adfeae6263e5f36351ac973b0ad7a7ebb099640cdace3f2001`), `..._saar_decisions.txt`, `..._scotland_wales_decisions.txt`, `..._transcaucasus_decisions.txt` (current local SHA-256 `5a87a4fe579a577f9beb9ffe60a47fe19c6c775a1bf99b9371fcf6c491f7aacc`), and `..._wallonia_frisia_decisions.txt`.
- Category gates: all 39 files matching `common/decisions/categories/006_independence_wave*.txt`.
- AI strategy helpers: all 26 files matching `common/ai_strategy/006_independence_wave*.txt`, including `common/ai_strategy/006_independence_wave_generic.txt`, `..._karelia_crimea.txt`, `..._kosovo.txt`, `..._macedonia.txt`, `..._montenegro.txt`, `..._ruthenia.txt`, and `..._thrace.txt`.
- Shared tuning and helper surfaces: `common/script_constants/006_independence_wave_decision_constants.txt`, `006_independence_wave_crisis_constants.txt`, `006_independence_wave_constants.txt`, `006_independence_wave_focus_constants.txt`, package-specific `006_independence_wave_*_constants.txt`, and `common/scripted_triggers/006_independence_wave_decision_triggers.txt`.
- Design authority: `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` (80 rows), `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` (IW-038 promotion/current-authority entry dated 2026-08-10; status HOLD/PARTIAL).

The full file inventory was enumerated from the two `006_independence_wave*.txt` globs; the ellipses above only abbreviate repeated filename prefixes. No category file was treated as a weighted candidate surface.

Expanded decision-source inventory:

```text
common/decisions/006_independence_wave_banat_decisions.txt
common/decisions/006_independence_wave_bosnia_decisions.txt
common/decisions/006_independence_wave_brittany_decisions.txt
common/decisions/006_independence_wave_catalonia_decisions.txt
common/decisions/006_independence_wave_crisis_decisions.txt
common/decisions/006_independence_wave_decisions.txt
common/decisions/006_independence_wave_epirus_decisions.txt
common/decisions/006_independence_wave_evolution_incident_decisions.txt
common/decisions/006_independence_wave_form01_02_04_decisions.txt
common/decisions/006_independence_wave_form03_decisions.txt
common/decisions/006_independence_wave_form05_decisions.txt
common/decisions/006_independence_wave_form08_decisions.txt
common/decisions/006_independence_wave_form09_decisions.txt
common/decisions/006_independence_wave_form39_decisions.txt
common/decisions/006_independence_wave_form48_decisions.txt
common/decisions/006_independence_wave_formable_registry_decisions.txt
common/decisions/006_independence_wave_iberian_decisions.txt
common/decisions/006_independence_wave_ice_decisions.txt
common/decisions/006_independence_wave_iw005_flanders_decisions.txt
common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt
common/decisions/006_independence_wave_iw025_vojvodina_decisions.txt
common/decisions/006_independence_wave_iw035_livonia_decisions.txt
common/decisions/006_independence_wave_iw043_iw058_decisions.txt
common/decisions/006_independence_wave_iw059_mesopotamia_decisions.txt
common/decisions/006_independence_wave_iw085_cyrenaica_decisions.txt
common/decisions/006_independence_wave_iw093_iw098_decisions.txt
common/decisions/006_independence_wave_iw101_iw102_iw105_cog_overlays_decisions.txt
common/decisions/006_independence_wave_iw156_iw196_iw197_iw204_overlays_decisions.txt
common/decisions/006_independence_wave_karelia_crimea_decisions.txt
common/decisions/006_independence_wave_kosovo_decisions.txt
common/decisions/006_independence_wave_macedonia_decisions.txt
common/decisions/006_independence_wave_mediterranean_decisions.txt
common/decisions/006_independence_wave_montenegro_decisions.txt
common/decisions/006_independence_wave_pacific_decisions.txt
common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt
common/decisions/006_independence_wave_rival_bloc_decisions.txt
common/decisions/006_independence_wave_ruthenia_decisions.txt
common/decisions/006_independence_wave_saar_decisions.txt
common/decisions/006_independence_wave_scenario_decisions.txt
common/decisions/006_independence_wave_scotland_wales_decisions.txt
common/decisions/006_independence_wave_thrace_decisions.txt
common/decisions/006_independence_wave_transcaucasus_decisions.txt
common/decisions/006_independence_wave_transylvania_decisions.txt
common/decisions/006_independence_wave_wallonia_frisia_decisions.txt
```

## Required reference review

Before the audit I read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-decisions-missions`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`. I also consulted the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding, plus the vanilla documentation files `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `script_math_functions.md` under the installed HOI4 `documentation` directory.

The relevant engine distinction is preserved throughout this report: `ai_will_do` is a willingness/score surface; it is not a click probability. A normalized selection probability or timing distribution requires a complete candidate pool, typed eligibility state, external modifiers, cadence, and terminal-state contract.

## Mandatory current MCP pass and exact blocker

The required first call was `hoi4.probability_inspect` before any evaluation. Current calls used `decision_ai_will_do`, `mission_ai_will_do`, and source-only discovery for the shared decisions, crisis decisions, scenario decisions, and package sources. Representative sequential calls returned the manifest blocker; a concurrent package-probe batch also returned internal errors and produced no artifacts. The server returned:

| Call | Current result | Evidence |
| --- | --- | --- |
| `decision_ai_will_do` on `common/decisions/006_independence_wave_decisions.txt` | `ARTIFACT_MANIFEST_INVALID`, status `error` | blocker message `Artifact provenance manifest is invalid`; workspace `mod_chaos_redux_ea3b2d67c2c0`; no artifact/revision |
| `mission_ai_will_do` on the same source | `ARTIFACT_MANIFEST_INVALID`, status `error` | same blocker; no candidate pool or artifact |
| `mission_ai_will_do` on `common/decisions/006_independence_wave_crisis_decisions.txt` | `ARTIFACT_MANIFEST_INVALID`, status `error` | same blocker; no artifact/revision |
| source-only discovery for representative valid current Event 006 paths | `ARTIFACT_MANIFEST_INVALID`, status `error` | same blocker |
| concurrent package source probes | `INTERNAL_ERROR`, status `error` | exact message `Unexpected internal error`; no artifact/revision; not treated as source evidence |
| absolute-path retry | `INTERNAL_ERROR`, status `error` | exact message `Unexpected internal error` |
| diagnostic `hoi4.event_inspect` on `events/006_independence_wave.txt` | `ARTIFACT_MANIFEST_INVALID` | confirms the failure is workspace artifact provenance, not a decision-only adapter result |
| nonexistent probability source probe | `PROBABILITY_SOURCE_NOT_FOUND` | path validation works; the current failure is not a simple path typo |

No current probability artifact URI, source revision, source hash, scenario hash, or rendered evidence path was emitted. The current `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_simulate`, and `probability_sequence` passes were consequently skipped; running them without a successful inspect would violate the inspect-first contract.

## Scenario contract and completeness

The following are the named scenario contracts required for a rerun. Existing historical IDs are listed exactly; IDs prefixed “planned” are not current MCP submissions and therefore have no scenario hash.

| Surface/family | Scenario IDs | Candidate-pool completeness | External-factor completeness | Current classification |
| --- | --- | --- | --- | --- |
| Emergency founding/crisis | `CRISIS_PRESSURE_OPEN`, `CRISIS_REQUESTER_LOST`, `CRISIS_RETRY_EXHAUSTED`, `CRISIS_NO_PRESSURE` | historical crisis inspect saw 1 mission; current pool unresolved | requester, host, pressure, retry, cooldown, and target state absent in current run | unresolved; historical bounded score-only |
| Provisional/recognized shared choices | `E6_SHARED_OPEN_CALM`, `E6_SHARED_HOST_CRISIS`, `E6_SHARED_ROUTE_LOCKED`, `E6_SHARED_NO_VALID_TARGET` | historical shared decision pool 10 and mission pool 54 were incomplete; current source has changed | phase, route, capital, host, ledger, costs, targets, active-project locks absent | unresolved; historical bounded score-only |
| Regional/package projects | `MAC_FOUNDING_CALM`, `MAC_HOST_CRISIS`, `MAC_ROUTE_LOCKED`, `MAC_NO_VALID_TARGET`; `RUT_FOUNDING`, `RUT_PROJECT_READY_PEACE`, `RUT_PROJECT_READY_WAR`, `RUT_HOST_LOSS_FALLBACK`, `RUT_ROUTE_LOCKS`, `RUT_NETWORK_READY` | historical MAC/RUT pools were declared (MAC 1 decision/11 missions; RUT 11 missions) but not complete at runtime | package identity, setup, capital, resource affordability, active project, former-host/war, route/network/league state absent | unresolved; historical bounded score-only |
| Regional/formable | planned `E6_FORMABLE_REGIONAL_OPEN`, `E6_FORMABLE_REGIONAL_LOCKED`, `E6_FORMABLE_REGIONAL_NO_TARGET`, `E6_FORMABLE_REGIONAL_CRISIS` | complete normalized pool must be supplied from the relevant form/registry source, including unavailable candidates | formable prerequisites, state/claim/core validity, transaction lock, cooldown, target control, phase/route state | not submitted; unresolved |
| League | planned `E6_LEAGUE_OPEN`, `E6_LEAGUE_CRISIS`, `E6_LEAGUE_ROUTE_LOCKED`, `E6_LEAGUE_NO_VALID_TARGET` | complete league decision/mission pool required; no current inspect | league route, live phase, member minimum, charter lock, crisis pressure, target and cooldown state absent | not submitted; unresolved |
| High-chaos | planned `E6_HIGH_CHAOS_OPEN`, `E6_HIGH_CHAOS_BLOCKED`, `E6_HIGH_CHAOS_RECOVERY`, `E6_HIGH_CHAOS_TARGET_LOST` | complete high-chaos candidate pool required; no current inspect | chaos tier, route/phase, capital, war, target validity, costs, and cleanup/reset state absent | not submitted; unresolved |
| Package-specific/project weights | source package IDs IW-005, IW-014, IW-022, IW-025, IW-026, IW-029, IW-030, IW-031, IW-033, IW-038, IW-041, IW-043/IW-058, IW-070/IW-072 and form/overlay groups | source scan identifies weighted blocks, but current MCP cannot certify complete pools | package admission, identity, setup, phase, route, capital, ledger, resources, target validity, host/network/league state, cooldown and one-shot flags absent | unresolved; no package probability claim |

No exact, sampled, or bounded current result can be assigned to these scenario contracts while the artifact manifest is invalid. Empty-state historical evaluations are retained below only as historical evidence and must not be treated as current balance proof.

## Source-level score and validity observations (not probability evidence)

The shared decision constants currently define `blocked = 0`, `very_low = 2`, `low = 5`, `standard = 10`, `high = 25`, `urgent = 100`, `modifier_half = 0.5`, `modifier_double = 2`, and `modifier_major = 5`. The shared active-surface caps include one active foundation mission, diplomatic action, security mission, league crisis, border operation, and formable operation. These values are nominal `ai_will_do` scores or gates, not normalized probabilities.

The source-level weighted-block distribution across the 44 current decision files is: generic shared file 64 blocks (`high` 29, `standard` 16, `low` 12, `urgent` 4, `very_low` 3); package files are commonly 12 blocks (`high` 6, `standard` 4, `urgent` 2); Brittany has 15 (`high` 10, `urgent` 3, `standard` 2); form01/02/04 has 18 (`urgent` 9, `high` 7, `low` 2); form03 has 23 (`high` 15, `urgent` 3, `standard` 2, `low` 2, `very_low` 1); form05 has 14 (`high` 7, `urgent` 6, `low` 1); formable registry has 10 (`low` 5, `high` 4, plus one constant-based minimum); KAR/CRI has 22 (`standard` 11, `urgent` 6, `discretionary` 5); Mediterranean has 29; Pacific and Rhineland/Bavaria have 28 each; Transcaucasia has 22 (`form16_willing` 7, `standard` 6, `high` 6, `urgent` 3); and the scenario navigation file has three `base = 0` controls. These counts are useful for source review only.

The package constants show intentionally different nominal priorities (for example, RUT survival `build_army = 86`, infantry `40`, artillery `24`, support `50`, infrastructure `70`, bunker `82`, emergency `build_army = 118`, host restraint `-260`, settled restraint `-430`; MAC uses emergency `118`; other packages range roughly `112–132` for emergency army emphasis). RUT `corridor_priority = 84` is present in constants but is not consumed by its strategy source; this is a source-consistency follow-up, not a proven balance defect.

Source gates are extensive and must be represented in typed fixtures before ranking: package identity and setup flags, phase and route flags, capital control, dynamic cost affordability, no-active-project locks, one-shot completion flags, former-host/war conditions, network-member and live-league-phase conditions, formable prerequisites and transaction locks, and cleanup/reset flags. `common/scripted_triggers/006_independence_wave_decision_triggers.txt` enumerates the active founding, security, formable, and league mission families.

Several positive scores belong to deliberately passive activation-backed missions whose source availability is `always = no` (for example `secure_provisional_capital` and package founding missions). Their positive scores do not prove live clickability, dominance, or starvation. KAR/CRI also contains repeated `factor = 0` fail-closed gates for foundation-ready, ledger, material/manpower/security, and diplomatic floors; whether any gate is over-restrictive is unresolved without typed state.

## Historical MCP receipts (stale source revisions; traceability only)

These artifacts were produced in earlier valid MCP runs and are preserved so the parent can compare after the manifest is repaired. Their source hashes/revisions predate the current worktree (for example, the current shared source hash is `c4bb...`, while the historical shared receipt used `f84a...`). They are **not current evidence**.

### Shared decisions and missions

- Shared decision inspect (`decision_ai_will_do`): 10 candidates, 61 required inputs, `poolComplete=false`, old source hash `f84a0e082f6a8b5c518eb769478676e6b78bc23157a39b0303f9947b729aa583`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b89cde389fbe5258215278312a740c9d59c96bf546cb7c255b5e949fb8d9272e/cc307c272b6c3dd1bec83caf0c1dc33632b7dfcff828b9454fdc4e1a0a5aca8c/probability-inspect-f84a0e082f6a.json`.
- Shared mission inspect (`mission_ai_will_do`): 54 candidates, 38 required inputs, `poolComplete=false`, same old source hash. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6d072cfc356bdb7096c61d56741b8c4cb996969ae7ab73fca8abe3b342b1b80/948e3df8d8651f7f64baf60b5939df7ace35c5f64f5265089efed317138d5a6b/probability-inspect-f84a0e082f6a.json`.
- Shared decision evaluation `probability-9f13e191d036a7047654e3ec`, scenario hash `1df471de297c267f3cc488f1a23f6df8922b8a8a3bfb2af5ccd10a46c2ec6a1a`, 4 scenarios/40 rows/1,990 unresolved/8 diagnostics, classification `partial/bounded score-only`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b79fb0dca7ef1671c8fadac953e452ce0ebd129ef9a958fbcca96e1dacbbb1b/35b5cb5c903a4e7e05b9d1cd3c528c6b334c99642a2f5a8214e4b64f531b7062/probability-9f13e191d036a7047654e3ec.json`. Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80fe9da3b07673f9b8b85e216ff7a20093a3ce352f25972754740c9c9e1f2713/7dc27aecc4f2cf5c58e1a71d85db1373aca3348f6a4119905bd8a6feb94daa85/probability-probability-9f13e191d036a7047654e3ec-ranking.svg`; matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4305271e8306f47b1c6c796cd312f8b351bfbd11520f7dbc5f7af84249b38132/8e864e07170b7a6737d2e4fe54aafdfb8ce69346680ee667fc161b318218e376/probability-probability-9f13e191d036a7047654e3ec-matrix.svg`; unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d28dad62fd282de3f1b6c36db8df83546ab934cd4abdf82790866fbe6296d50/ebecc47fe5bd48517719d5b12e0437354c8107ce7683c332120bf6568aed884c/probability-probability-9f13e191d036a7047654e3ec-unresolved.svg`.
- Shared mission evaluation `probability-8950045661d66cea9adf4cf6`, scenario hash `7285f72c125307881faf9b07e13de472af62cd1c88b77988edf291dddf75e123`, 4 scenarios/216 rows/486 unresolved/20 diagnostics, classification `partial/bounded score-only`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a309127743ffdc6ae38993c92883ef481cd118232adcd5d4df37309c581ebe2/2099e8cf2205809140991606adce63d97bc7de10e20b84b3da45145cd06223f6/probability-8950045661d66cea9adf4cf6.json`. Unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/323f18ddb75b77b583185a291f1fcd0e57b8e3f8569806eec122fa09fb275a64/1bd738c2db0e52e6150d6dba515e04e8170e6099bf22438ae33ba0830dbf49b0/probability-probability-8950045661d66cea9adf4cf6-unresolved.svg`.

### Crisis mission

- Historical crisis mission inspect: one candidate, seven required inputs, `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b01652711ed678f07435e0742b9ecc8c7e675be643fa56784cd05b37cc15850c/f61695a16175aaf98b7d6d2971609db498a37245f38194c1bfcf441451f6babf/probability-inspect-da54a4d80e28.json`.
- Historical evaluation `probability-adfb7e57ec7ba9495504a95e`, scenario hash `3db379f661d07101bb0738e1e9c03f83398b573f5c3bf4836b2d0f3bab062a78`, 4 rows/7 unresolved, classification `partial/bounded score-only`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35dbaef73101b242fdfffd8de397ca6d4704e3cd6e55827a3a930c41a3dd3b8d/678a3182ec2a33a37e03d921167819fc6f299bbb16c584aa0c3bbfde350fe119/probability-adfb7e57ec7ba9495504a95e.json`; ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0840d6e64171c4fd404da9ec5b05548de689afd14a0ff1d7de19c519ac039137/694e7d1374f6fc59d263f269a61b243453c0fa6c114a4f79b551f9d1e085138e/probability-probability-adfb7e57ec7ba9495504a95e-ranking.svg`; unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd4a49c275611c8b777e968b61871d981623784a06461f4a7914eca3e42d91c6/b779943618331adb67c5d5e993216ef6ce790ded60b5ed41887e487ca2ec0178/probability-probability-adfb7e57ec7ba9495504a95e-unresolved.svg`.

### Package examples

- Historical MAC ordinary decision inspect: one candidate, 10 inputs; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1ad65fae9e8c9db7110fa565acd255179fe2f11e84a615b5ca38cb16c6186ed/b9712e77f622559238f7674edaad19c8dd768edd8ed7aab6f0458ce58099755d/probability-inspect-9d4afb013511.json`. MAC mission inspect: 11 candidates, 13 inputs; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2403be674528a7719f4e4f1596c11b30e3f3aa4af8262489c71142c854c793d/b55393c502718f3a760427e217ea6e4eb8937ae361b076e342d8016f098fddae/probability-inspect-9d4afb013511.json`.
- MAC decision evaluation `probability-c4c55d64391410e432b56303`, scenario hash `4ba2163247e1ac8748d1da763f0fcfb9476765663d4cf17c25af8b6950dc4376`, 4 rows/17 unresolved, bounded score-only. MAC mission evaluation `probability-0aed88e4788e810660967a16`, scenario hash `3d8d1bf109cd84ad80e80dcf4f60d55c15f5c7748c7499f2f0f9ddff3de49fdb`, 44 rows/64 unresolved, bounded score-only. The JSON and ranking/unresolved renders are recorded in `006_iw026_macedonia_probability_audit_current_2026_08_06.md`.
- Historical RUT mission evaluation `probability-e2009ec2891aa9559706fa13`, scenario hash `d728411c97a5b7c6bc07922a6bf660ba47697f10fbb1b8b29574fab19390a72a`, source revision `6edf2cfeb997b07ac2f343f2086934e718856cb0e71399b60b343a12eb96568c`, source hash `108598448343f3734ae41acb1c2ab43280748b5755a0c74a50aed4102df8c77`, 66 rows/116 unresolved/11 diagnostics, bounded score-only. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e659ecf25469357dd37bc845f340f91cb66a137f6673c9f9b93320d1afe1dd5f/7c1e8ad42cdb89d930500eddef8c4b62b159c7eefd2f00bdd16053bdc2a846c7/probability-e2009ec2891aa9559706fa13.json`; ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac5ab77703d039ab4c8206fa6f343221aa8bba97a93890dd8e92305351b46fcd/58b9280ae2069067bd57b4a920af5ce0fe711382a9bbb99f6746db3701cdb064/probability-probability-e2009ec2891aa9559706fa13-ranking.svg`; unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df45b35b51a064d52bbc06c5996dfc121b4178b50654bd1876e95f062b84786c/399832e38a02901ffa9c0b32135d009bdb248753c0475ed167c96d418ce5bcc4/probability-probability-e2009ec2891aa9559706fa13-unresolved.svg`.
- The historical RUT same-source compare `probability-51c96259bef4fc3beeb629a0`, same scenario hash, returned `comparisonChanges = 0`; this is a capability receipt only, not a balance comparison. Its comparison artifact is recorded in `006_iw038_ruthenia_probability_final_audit_2026_08_10.md`.
- Historical KAR/CRI inspect recognized two decision candidates and 20 mission candidates, both `poolComplete=false`; its `ai_strategy_factor` adapter returned `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`. This is not current evidence and does not prove the current 22-block source is absent from the adapter.

Historical `probability_sweep` calls for MAC/RUT were blocked by `PROBABILITY_SWEEP_RANGE_REQUIRED`: **“Every sweep path requires a scenario range, numeric alternatives, or numeric state value.”** No threshold, sensitivity, or rank-reversal conclusion was made.

## Risk findings and non-findings

The source review identifies potential review targets but no proven balance defect:

- **Validity:** positive scores on passive `always = no` founding/foundation missions must be separated from live selectable projects; package, phase, route, capital, cost, target, host, network/league, formable, one-shot, and active-project gates are all material.
- **Dominance/starvation:** unresolved. The current pool and typed external modifiers are unavailable, so no candidate can be declared dominant or starved.
- **Rank reversal/sensitivity:** unresolved. No current sweep or numeric alternative was accepted.
- **Repetition/cooldown:** unresolved. Active caps and cleanup flags are visible in source, but cadence, removal, recovery, reset, and terminal-state behavior require a complete sequence contract.
- **Exploit risk:** unresolved. Dynamic costs, target validity, former-host conditions, route locks, one-shot flags, and cleanup need typed evaluation; source presence alone is insufficient.
- **Strategy factors:** the generic and several package strategy sources contain weighted layers, but historical `ai_strategy_factor` calls often returned `PROBABILITY_SURFACE_EMPTY`. Treat that as adapter capability failure, not proof that the layers are unused.
- **SCN-008:** the three navigation decisions have `base = 0` and deterministic previous/next controls; historical `direct_random` and `random_list` probes returned `PROBABILITY_SURFACE_EMPTY`. They are UI/ledger controls, not a probability-proportional scenario-selection pool.

## Recommended owner actions (not applied)

1. Repair or regenerate the workspace artifact provenance manifest for `mod_chaos_redux_ea3b2d67c2c0`, then rerun `hoi4.probability_inspect` with current source paths and record source revisions/artifact URIs.
2. Re-run `decision_ai_will_do` and `mission_ai_will_do` separately for each shared, crisis, formable, league, high-chaos, and admitted package source. Supply the complete candidate pool for every adapter; do not infer a pool from source block counts.
3. Evaluate the named emergency, provisional/recognized, regional/formable, league, high-chaos, MAC, RUT, KOS, MNT, KAR/CRI, and project scenarios with typed package identity, phase/route, capital, target, host, ledger, cost, resource, active-project, cooldown, war, network/league, and cleanup state.
4. Use `probability_sweep` only with explicit numeric state ranges or alternatives; retain any `PROBABILITY_SWEEP_RANGE_REQUIRED` response as unresolved rather than substituting hand calculations.
5. Use `probability_compare` only after preserving a valid pre-change source revision/path and reusing the same complete pools and scenario hashes. A same-source `comparisonChanges=0` receipt is not a balance result.
6. Render ranking, matrix, timing, sensitivity, and unresolved views after successful evaluation. Recheck passive founding missions separately from selectable projects and inspect KAR/CRI zero-factor gates under both floor-satisfied and floor-failed fixtures.
7. Revisit RUT `corridor_priority` if the owner confirms it is intended to affect strategy; this is a source-consistency recommendation, not an applied patch.

## Skipped analyses and remaining uncertainty

- Current `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_simulate`, and `probability_sequence`: skipped because all valid current inspect calls failed with `ARTIFACT_MANIFEST_INVALID` (absolute-path retry `INTERNAL_ERROR`).
- Current exact candidate pools, source revisions, artifact IDs, scenario hashes, modifier traces, rankings, timing distributions, threshold sensitivities, rank reversals, repetition rates, dominance/starvation, and exploit-safety proofs: unresolved.
- Simulation was not appropriate without explicitly declared uncertain inputs and seeds. Sequence analysis was not appropriate without a complete custom pool, cadence, state transitions, recovery/removal rules, and terminal states.
- Historical receipts above are bounded/score-only or capability evidence at older source revisions. They must be rerun after manifest repair before any current balance or completion claim.

## Files changed

Only this read-only audit handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_probability_audit_current_2026_08_11.md`. No gameplay or weighted-source patch was applied.

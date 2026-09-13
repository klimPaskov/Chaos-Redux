# CXT special-project callback popup audit

Date: 2026-09-13.
Mode: read-only source and MCP review, with this report as the only auditor-owned file.
Scope: every installed custom project definition in `common/special_projects/projects/*.txt`, its completion outputs, acquisition/prototype callback families, and narrowly reached report dispatches.
The country owner retains the technology/project inventory, history, facilities, equipment helpers, runtime setup and final wiring.
Root owns the reviewed callback patches and final commit.
No gameplay, history, assets, localisation, skills, weights or probabilities were edited by this auditor.

## Completion status by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Custom project completion callback inventory | Finished source review | All 34 active custom projects in all 9 installed TXT files are listed below. Commented documentation examples are excluded. |
| Completion report suppression | Finished source review of owner patch | D’Rhondan `.40` and Black Plague `.2`/`.6` use the temporary silent-unlock contract. Their mechanics remain available. |
| Original country eligibility | Finished source review of owner patch | The 2 USA and 5 JAP project `allowed` edits preserve the original country clause and add CXT. |
| Clone revolt dispatch | Finished bounded source review | `germany_mengele.24` requires a Germany-only active/restricted program and cannot be queued by dormant CXT completion. Its coup effect remains untouched. |
| Acquisition and prototype reports | Finished callback-location review | Ordinary biological field tests require native facility-state outputs. Event 016 callbacks require the host/provider gates. Zombie acquisition/profile callbacks contain no direct report dispatch. No prototype weights were evaluated or changed. |
| Zombie completion | Finished bounded source review | Existing CXT profile initialization keeps the dormant fixture on the ordinary completion path. Success `.1` is already CXT-guarded. The completion bonus helper carries technology, profile and stockpile outputs independently of that report. Failure `.8` remains mechanically active outside the fixture. |
| Event MCP proof | Partial, completion evidence gap | Six narrow event queries produced partial inspect/render artifacts, but every returned timing render selected zero nodes. Deferred helper/lifecycle analysis was not substituted with a source-only engine claim. |
| Native history popup behavior | Unresolved engine behavior | Vanilla history uses `complete_special_project`, but the installed documentation does not explicitly promise that the native completion notification is suppressed during country-history loading. |
| History grant inventory and runtime synchronization | Parent-owned | This audit checked the silent-flag call contract only. It does not duplicate or certify the country owner’s inventory and equipment/facility work. |
| Assets, event logs, details, evolutions, catalog | Outside this bounded repair | No event identity, visible wording, asset, evolution, category or catalog facts changed in these callback edits. |

## Required references

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents` and `chaos-redux-event-planning`, applying their bounded audit, source-evidence, disposition and MCP rules.
Consulted the eleven required offline core wiki pages, with focused event-effect, delayed-event and scope review.
`paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:34` states that a delayed event aimed at a nonexistent country waits until that country exists.
`paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:33` distinguishes runtime on actions from history effects.
The installed vanilla `documentation/effects_documentation.md:2896` documents country-scope `complete_special_project`, bypassing project-tree progression and skipping facility/scientist effects when their scopes are absent.
The same documentation at `:2943` and `:5053` documents explicit country/news event delay fields.
Installed vanilla `common/special_projects/projects/documentation.md:198` places `country_effects` in country scope with FROM as the project and warns at `:206` that script completion may skip facility-state effects.
Installed prototype-reward and special-project documentation was consulted in parallel.
Vanilla precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ANU - Ainu.txt:52` completes `sp_air_radar` through country history.
This precedent supports the history grant route, while its notification behavior remains unspecified in those sources.

## All installed custom completion outputs

Paths in this table are relative to `common/special_projects/projects/`.
Line numbers identify `project_output`.

| File and line | Project | Country callback/output | Popup conclusion |
| --- | --- | --- | --- |
| `016_brilliant_scientist_projects.txt:97` | `sp_brilliant_scientist_computational_engine` | family computation, `brilliant_scientist_record_new_project_prototype` | Host/provider gated. |
| same `:175` | `sp_brilliant_scientist_advanced_materials` | family materials, same callback | Host/provider gated. |
| same `:256` | `sp_brilliant_scientist_biomedical_acceleration` | family biomedical, same callback | Host/provider gated. |
| same `:337` | `sp_brilliant_scientist_quantum_transit` | family teleportation, same callback | Host/provider gated. |
| same `:406` | `sp_brilliant_scientist_cloning` | family cloning, same callback | Host/provider gated. |
| same `:476` | `sp_brilliant_scientist_autonomous_cognition` | family robotics, same callback | Host/provider gated. |
| same `:546` | `sp_brilliant_scientist_paleogenetics` | family paleogenetics, same callback | Host/provider gated. |
| same `:616` | `sp_brilliant_scientist_xenobiological_synthesis` | family xenobiological synthesis, same callback | Host/provider gated. |
| same `:686` | `sp_brilliant_scientist_alien_arms` | family alien arms, same callback | Host/provider gated. |
| same `:756` | `sp_brilliant_scientist_temporal_mechanics` | family temporal, same callback | Host/provider gated. |
| same `:826` | `sp_brilliant_scientist_singularity_command_core` | component command core, `brilliant_scientist_register_singularity_component` | Host/provider gated. |
| same `:896` | `sp_brilliant_scientist_singularity_power_link` | component power link, same callback | Host/provider gated. |
| same `:966` | `sp_brilliant_scientist_singularity_containment_lattice` | component containment lattice, same callback | Host/provider gated. |
| same `:1036` | `sp_brilliant_scientist_singularity_temporal_authenticator` | component temporal authenticator, same callback | Host/provider gated. |
| same `:1106` | `sp_brilliant_scientist_singularity_delivery_architecture` | component delivery architecture, same callback | Host/provider gated. |
| same `:1176` | `sp_brilliant_scientist_singularity_fail_deadly_governor` | component fail-deadly governor, same callback | Host/provider gated. |
| `016_dhrondan_envoy_project.txt:35` | `sp_dhrondan_envoy_craft` | `dhrondan_complete_envoy_craft` | `.40` owner guard reviewed. |
| `020_black_plague_weaponization_projects.txt:56` | `black_plague_weaponization_program` | `black_plague_weaponization_complete_program` | `.2`/`.6` owner guards reviewed. Facility history flag requires a facility. |
| `biowarfare_main_projects.txt:167` | `zombie_cure_bomb` | `anti_zombie_bomb_available` flag | No explicit report. |
| same `:475` | `anthrax_bomb` | silent delivery tech, CBRN decision unlock, bioweapon flag | No country completion report. |
| same `:713` | `plague_bomb` | same for plague delivery | No country completion report. |
| same `:946` | `tularemia_bomb` | same for tularemia delivery | No country completion report. |
| same `:1184` | `smallpox_bomb` | same for smallpox delivery | No country completion report. |
| `chemical_special_projects.txt:49` | `sp_cw_malodor_bomb_program` | equipment/modules, `cbrn_unlock_malodor_aerosol_modules_after_project` | Helper technologies already use `popup = no`. |
| same `:171` | `sp_cw_aphrodisiac_bomb_program` | equipment/modules, `cbrn_unlock_behavioral_aerosol_modules_after_project` | Helper technologies already use `popup = no`. |
| `chemical_warfare_nerve_projects.txt:43` | `sp_cw_sarin_program` | silent sarin tech, CBRN decision unlock | No explicit report. |
| same `:155` | `sp_cw_soman_program` | silent soman tech, CBRN decision unlock | No explicit report. |
| `japan_ishii_projects.txt:47` | `sp_japan_pingfang_records_office` | `camp_rework_japan_complete_pingfang_records_project` | Flag/value outputs, no report in refresh helper. |
| same `:88` | `sp_japan_kwantung_medical_intelligence` | `camp_rework_japan_complete_kwantung_intelligence_project` | Same conclusion. |
| same `:128` | `sp_japan_occupation_test_ledger` | `camp_rework_japan_complete_occupation_test_ledger_project` | Same conclusion. |
| same `:170` | `sp_japan_epidemic_mapping_bureau` | `camp_rework_japan_complete_epidemic_mapping_project` | Same conclusion. |
| same `:221` | `sp_japan_cherry_blossom_dossier` | `camp_rework_japan_complete_cherry_blossom_dossier_project` | Same conclusion. |
| `mengele_cloning_projects.txt:67` | `sp_mengele_cloning` | `germany_mengele_complete_cloning_project` | Germany-only revolt gate excludes CXT. |
| `zombie_weaponized_projects.txt:73` | `weaponize_the_zombies` | `complete_weaponized_zombie_project_from_project_output` | Existing CXT success guard and deterministic fixture reviewed. |

Supporting helper evidence: `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1294` and `:1396` gate the Event 016 completion callbacks.
`common/scripted_triggers/016_brilliant_scientist_triggers.txt:90` requires the current-host flag and Kruger character.
`common/scripted_triggers/016_mengele_project_stage_triggers.txt:16` requires an existing, authorized Directorate provider.
`common/scripted_effects/camp_repression_major_country_effects.txt:1929` through `:1961` provide the five Japan callbacks, and their `camp_rework_japan_refresh_project_unlocks` at `:1492` dispatches no event.
`common/scripted_effects/cbrn_decision_visibility_effects.txt:15` sets the decision-unlock flag only.
`common/scripted_effects/cbrn_designer_effects.txt:225` and `:252` use silent technologies for the aerosol module outputs.

## Report dispatch contracts and owner patch review

| Report | Recipient and timing | Evidence | Minimal action and final source status |
| --- | --- | --- | --- |
| `chaosx.nr16.40` | Project owner, immediate, no delay | `common/scripted_effects/016_dhrondan_contact_effects.txt:24`, dispatch `:38`. Event `events/016_brilliant_scientist_dhrondan_contact_events.txt:11`, option helper `:21`. | Implemented by root: while silent, invoke `dhrondan_ai_try_authorize_expedition` directly at helper `:35`. Otherwise retain report. Flags and report-option action are preserved. |
| `chaosx_nr20_weaponization.6` | Project owner, immediate defensive completion | `common/scripted_effects/020_black_plague_weaponization_effects.txt:198`, event `events/020_black_plague_weaponization.txt:104`. | Implemented by root: guard only report dispatch while silent. Option is empty. Countermeasure gain, completion flags and cleanup remain. |
| `chaosx_nr20_weaponization.2` | Project owner, immediate offensive completion | Same helper `:218`, event `events/020_black_plague_weaponization.txt:23`. | Implemented by root: guard only report dispatch while silent. Option is empty. Stockpile, delivery tech, condemnation and completion flags remain. |
| `germany_mengele.24` | Project owner, `days = 1` | `common/scripted_effects/germany_mengele_effects.txt:112`. Event `events/germany_mengele.txt:713`, coup option `:726`. | Leave untouched. Revolt-ready trigger `common/scripted_triggers/germany_mengele_triggers.txt:77` requires active/restricted program. Both require Germany scope at `:12`, including `exists = yes` and `original_tag = GER`. CXT cannot satisfy it. |
| `chaosx.weaponized_zombies.1` | Project owner, immediate success completion | `common/scripted_effects/zombie_special_project_effects.txt:2545` completion helper. `events/zombie_weaponized_special_projects.txt:8`, immediate `:15`. | Existing architect patch retained: CXT dispatch guard. `apply_weaponized_zombie_completed_bonuses` at helper `:2355` independently grants silent delivery tech, profile bonuses and initial stockpile. |
| `chaosx.weaponized_zombies.8` | Project owner, immediate exceptional failure | Same completion helper. Event `events/zombie_weaponized_special_projects.txt:335`. | Leave untouched under the ordinary dormant CXT fixture. Failure gate `common/scripted_effects/zombie_special_project_effects.txt:1470` requires demonic/necrotic nature plus extreme mutations. Fixture `:123` initializes neurobiological nature. Suppressing `.8` blindly would skip its wendigo spawn and option losses. |
| `condemnation_sanctions.1` | Project owner, targeted pulse delay from constant | `common/scripted_effects/condemnation_sanctions_effects.txt:349`, reached from plague condemnation helper. Event `events/condemnation_sanctions_events.txt:12`, `hidden = yes` at `:13`. | Preserve the hidden lifecycle scheduler. It is not a visible completion report. Its exact inactive-country scheduling path remains bounded source evidence. |
| `cbrn_bio_safety.1` | Project owner, initial monitor delay from constant | `common/scripted_effects/biological_stockpile_safety_effects.txt:753`, event `events/biological_stockpile_safety_events.txt:16`, `hidden = yes` at `:17`. | Preserve monitor. Completion-country output does not designate an arsenal. Designation/start-monitor calls are in facility-state output, which stateless history completion skips. |

The silent flag is set by `common/scripted_effects/chaosx_test_country_special_project_effects.txt:22` before the complete-all sequence and cleared at `:210`.
The registered-project sequence has the same temporary contract starting at `:239`.
`history/countries/CXT - Chaos Redux Test Country.txt:26` calls the complete-all helper.
This is a temporary CXT-owned grant contract, so ordinary country completion reports retain their original behavior.

Acquisition/prototype review: zombie acquisition starts at `common/special_projects/projects/zombie_weaponized_projects.txt:99` and calls reset/profile helpers without a report.
Zombie field-test choices at `:886` call `conduct_weaponized_zombie_field_test`, whose helper at `common/scripted_effects/zombie_special_project_effects.txt:3694` dispatches `.2`/`.3`/`.4` only for that explicit prototype test transaction.
Ordinary biological field-test callbacks are under `facility_state_effects` at `biowarfare_main_projects.txt:579`, `:817`, `:1050`, `:1290`, calling the helpers at `:590`, `:828`, `:1061`, `:1301`.
`common/scripted_effects/biological_field_test_effects.txt:20` uses the exact supplied facility state and requires existing actor/victim.
Its meta-effect reports map anthrax to `chaosx_bioweapon.2`/`.3`, plague to `.7`/`.8`, tularemia to `.100`/`.101` and smallpox to `.201`/`.202`, with immediate actor recipient.
Those are not country-history completion callbacks.
Black Plague prototype-role callback `common/scripted_effects/020_black_plague_weaponization_effects.txt:31` may reach accident helper `:76`, whose report `.1` at `:105` has an empty option.
It is outside the ordinary complete-all grant because that grant supplies no prototype iteration outputs.
Event 016 risky prototype callbacks may reach incident dispatch, and the native host stage path can queue `chaosx.nr16.13` using `brilliant_scientist_directorate_timing.incident_report_days` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1629`.
Dormant CXT lacks the required host/provider gate, so no additional guard is required for the reviewed history path.
Accident probabilities and option AI scores were not balance-audited by this popup-location review.

## Meaningful validation and MCP limits

Source comparison against HEAD removed only the three reviewed report wrappers and the seven CXT `allowed` additions, then compared all remaining content after whitespace normalization.
Results: Black Plague wrappers count 2, D’Rhondan wrapper count 1, USA allow additions count 2, JAP allow additions count 5, with all other file content preserved in all four files.
This verifies that the report suppression edits retain all existing mechanical outputs and that the country eligibility edits retain the original actor rules.
Read the actual recipient event blocks before recommending suppression, identifying and preserving the D’Rhondan option action and avoiding suppression of the Mengele coup or zombie failure event.

MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Revision for six successful narrow inspect/render requests: `3ac0bcfca142cdb797cca8faf293cfa1085b9019421045d9f385374ad094fc2a`.
Queries used event selectors for `.40`, Black Plague `.2`/`.6`, Mengele `.24`, zombie `.1`/`.8`, maxDepth 1, maxNodes 12, maxEdges 24 for inspect, expandHelpers false, timing renders without HTML.
The initial D’Rhondan inspect used maxNodes 20 and maxEdges 30.
All returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`, `validation.passed = false`, with the exact check message: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
All timing renders reported `selectedNodes = 0`, `omittedNodes = 42579`.
Thus the returned artifacts do not prove that the named event nodes or callback edges were resolved.
No service exposure or nominal OK status is being treated as equivalent to complete engine evidence.

Artifact references below record returned inspect and timing JSON content hashes.
Their full URIs are recorded in the artifact appendix.

| Event | Inspect JSON SHA-256 | Timing JSON SHA-256 |
| --- | --- | --- |
| D’Rhondan `.40` | `e143a594d720064e96809ca1bdf823568371a428b85c96072a6b5f928f674cdb` | `29cf82dfdb99ec4955aa55dd01a95a3ee00a3354e37b3f8fca0c1fbd529f51eb` |
| Black Plague `.2` | `76d68a700d1984cff2b81f6748dfb891958e72612ca895ef15beb3d783708708` | `e6a0a81222a46d4318ef3279460123f53942d14252ac69b24683e80b3ec617b8` |
| Black Plague `.6` | `752f37f5c332774ca700ee3cf9e95630d53dec79c61e3bafc8af9435f2dbf9c6` | `bf6f77d08a06a73f6a2f828e872c4b0a15aaeaf9d6715f55c41519661f5206d5` |
| Mengele `.24` | `69279f84427bcbf2241f45da5fff3576ee014cc3b5719f79a997adce2c9a88e2` | `8313cfa86a3e90823cea994c5e37912c757b74664c1fcd7ada59963a5853ca0f` |
| Zombie `.1` | `cb777d51a0e5f583094f0fe929a44cd0cba4ed345fa40b7250af6f258a542acd` | `f4d79dfc6a1e7c34c3e95727b78230a476f584845289d95d039fa82bf18131b4` |
| Zombie `.8` | `c26bb14304bd920cac05da2beaac9dd8f15709d771b4f7661110e089cf1c9f6c` | `bed78cdb2c559413c99d057606f0ae73190476d90c09281ab246817607f607c5` |

A bounded file render attempt using `sourcePath = mod:events/020_black_plague_weaponization.txt` did not return promptly and was stopped within this task’s narrow-review limit.
An event_compare attempt using the cached revision as `before` and current source as `after`, render false, maxRenderNodes 12, also did not return promptly and was stopped.
No comparison result or artifact was returned and none is claimed.
The parent explicitly directed no more broad MCP retries once this partial route evidence was established.
Initial selector-schema errors were corrected to `{kind: event, eventId: ...}` before the successful requests.
The failed file-selector `path` key was corrected to `sourcePath` for the stopped attempt.

## Dispositions, gaps and next actions

The root-accepted CXT-only temporary silent callback guards are implemented with current file evidence above.
Their acceptance basis is the user’s request for suitable CXT unlocks already completed before activation, and root’s explicit instruction to review the applied silent guards.
No expansion plan, new event, new GUI, asset package or broader event-design change was created by this audit.
No simplification of the reviewed mechanical output was found in the source patches.
The audit’s omissions are explicit: full engine callback/lifecycle projection, a returned MCP comparison, native history-notification behavior and the country owner’s grant inventory/runtime synchronization are not certified here.
These are not hidden as future polish.

Next actions for root: review the country owner’s final history and completion-helper handoff, including clear/set timing of the silent flag and dormant CXT gate assumptions.
Carry the exact partial MCP and native-notification limits into the completion report.
A future project adding a report in its country completion output must join the same grant-only silent contract while keeping mechanical actions independent.
Do not suppress hidden maintenance, revolt or incident events indiscriminately.
No further custom completion-report source patch is recommended under the current bounded fixture and grant sequence.

## Artifact appendix

Initial D’Rhondan inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e143a594d720064e96809ca1bdf823568371a428b85c96072a6b5f928f674cdb/adc13aa138249a2af68842ed0ae5b5d0b77a81c39682fb96dffeb505e3ea0bb3/event-trace-3ac0bcfca142.json`.

Event `chaosx.nr16.40`:

- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed7c56428385781bc0813b5875a6e4034d4674496e1216b489d8ed33e24e8ad9/e1c4423bc70ee89fced78a994188eca3e871d8b533e8940720049c630317defa/event-timing-3ac0bcfca142-manifest.json`, application/json, 42786 bytes, SHA-256 `ed7c56428385781bc0813b5875a6e4034d4674496e1216b489d8ed33e24e8ad9`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29cf82dfdb99ec4955aa55dd01a95a3ee00a3354e37b3f8fca0c1fbd529f51eb/978b35af468ff58055af7cbfc381c7fd425170fdc6b291e8705eee22ff389458/event-timing-3ac0bcfca142.json`, application/json, 40997 bytes, SHA-256 `29cf82dfdb99ec4955aa55dd01a95a3ee00a3354e37b3f8fca0c1fbd529f51eb`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/b1bc549997b84037ebc0b8d489304984419acd5a5ad68c8838756763766ac5b2/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/2bbf78a8f3d2b083ee18dc2c0e98999db741a1410dec9aa119ade561b9debf03/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

Event `chaosx_nr20_weaponization.2`:

- inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76d68a700d1984cff2b81f6748dfb891958e72612ca895ef15beb3d783708708/37ceea2dd1075ed61a0b5d2b0b93026961f2c4dd671d0cac0265828a495c622c/event-trace-3ac0bcfca142.json`, application/json, 1060670 bytes, SHA-256 `76d68a700d1984cff2b81f6748dfb891958e72612ca895ef15beb3d783708708`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d4abb0d40415adddf680af0c63d9089a4c26b91b949e3aec33c092b3f978ea5/8316326b1464a24a20cfd5d77e2d2f0755d02f9c3a85ef3ddc4aa795b55dcb91/event-timing-3ac0bcfca142-manifest.json`, application/json, 42799 bytes, SHA-256 `3d4abb0d40415adddf680af0c63d9089a4c26b91b949e3aec33c092b3f978ea5`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6a0a81222a46d4318ef3279460123f53942d14252ac69b24683e80b3ec617b8/8a5bca6a23df2d95d3de01c7e1b4fa826b146e40bf05cb3249ae3cb20ffe6f31/event-timing-3ac0bcfca142.json`, application/json, 41010 bytes, SHA-256 `e6a0a81222a46d4318ef3279460123f53942d14252ac69b24683e80b3ec617b8`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/401d450672663a452e53c57a8e354f0f67111c64f28ef8b84cf074a9b98048bd/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/37950b970c041a5627c921eaced693a0660393883c6972d5cc387eda9025b5b3/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

Event `chaosx_nr20_weaponization.6`:

- inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/752f37f5c332774ca700ee3cf9e95630d53dec79c61e3bafc8af9435f2dbf9c6/3bf44bcf1d8c16e20d2b9ba8606f05081901a4586e72507c35a04c4cd42fc478/event-trace-3ac0bcfca142.json`, application/json, 1060405 bytes, SHA-256 `752f37f5c332774ca700ee3cf9e95630d53dec79c61e3bafc8af9435f2dbf9c6`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2152cb4e3eacedd41dcaa48669ec307a994b0b25331dcd0320a835ae2c8d365/535b668a51e88ed0be9965c2836797465a7fa46af323cc263cdc9248a4e4d969/event-timing-3ac0bcfca142-manifest.json`, application/json, 42799 bytes, SHA-256 `c2152cb4e3eacedd41dcaa48669ec307a994b0b25331dcd0320a835ae2c8d365`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf6f77d08a06a73f6a2f828e872c4b0a15aaeaf9d6715f55c41519661f5206d5/dbb09b66f62f5c88fbef05a9b983ae8a504275306068ca35e10f6c071cf26a13/event-timing-3ac0bcfca142.json`, application/json, 41010 bytes, SHA-256 `bf6f77d08a06a73f6a2f828e872c4b0a15aaeaf9d6715f55c41519661f5206d5`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/142c0324fb37a7ae0397a0292c96e4f507aae413ed3feb3ebe10673da2e3bf13/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/c39173f6e64f3cc54907001963b49705d9c858623f7533e0fa8fa2eecdd396a4/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

Event `germany_mengele.24`:

- inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69279f84427bcbf2241f45da5fff3576ee014cc3b5719f79a997adce2c9a88e2/9645a56f368ca308ebe3442e65d9bdb5390104ef5350874199020747ca527b17/event-trace-3ac0bcfca142.json`, application/json, 1060427 bytes, SHA-256 `69279f84427bcbf2241f45da5fff3576ee014cc3b5719f79a997adce2c9a88e2`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19fc692f8ecd8b93b4d91121b5a341b5c5e9ce2f8b17e7b8e250c9e5bd9a00b3/d112bc57bfc1731140acadf6a20adf1e2fb237bbc346f69c2fbff78f0b89ab41/event-timing-3ac0bcfca142-manifest.json`, application/json, 42790 bytes, SHA-256 `19fc692f8ecd8b93b4d91121b5a341b5c5e9ce2f8b17e7b8e250c9e5bd9a00b3`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8313cfa86a3e90823cea994c5e37912c757b74664c1fcd7ada59963a5853ca0f/cf78f1b7c57f75bb27484fad2361447e8dc8ce8a7f742f38d0c9bbb985c1f2cf/event-timing-3ac0bcfca142.json`, application/json, 41001 bytes, SHA-256 `8313cfa86a3e90823cea994c5e37912c757b74664c1fcd7ada59963a5853ca0f`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/d669d52825b06cf247f24af5b974673a1feff6709876af89aa00269c6c1728ad/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/a5cc4bf178779552397830fd508ba46991dc726ef7fca3ddfaf5f4dea0b1343a/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

Event `chaosx.weaponized_zombies.1`:

- inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb777d51a0e5f583094f0fe929a44cd0cba4ed345fa40b7250af6f258a542acd/9bfdccb73426235b60448a22fe10c3f735afa38eb65fadb2ea551684cd86cdb0/event-trace-3ac0bcfca142.json`, application/json, 1066825 bytes, SHA-256 `cb777d51a0e5f583094f0fe929a44cd0cba4ed345fa40b7250af6f258a542acd`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/183e24f19341f02271f6799adcbb769597d7b18a2aa4e11e869997223121f9b3/8ca38d5b10908e5c1d0db2632495e6cbd339f534bbb5f4958e74a8de265a337d/event-timing-3ac0bcfca142-manifest.json`, application/json, 42799 bytes, SHA-256 `183e24f19341f02271f6799adcbb769597d7b18a2aa4e11e869997223121f9b3`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4d79dfc6a1e7c34c3e95727b78230a476f584845289d95d039fa82bf18131b4/b69b59bc2107fb9bd4b6846a1be6588c1d24d7b7c89cb9b75f5874c7d64bf771/event-timing-3ac0bcfca142.json`, application/json, 41010 bytes, SHA-256 `f4d79dfc6a1e7c34c3e95727b78230a476f584845289d95d039fa82bf18131b4`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/1d1dc9c89d57162d9a2be0612022be192a3b18cc6b37da7996a38d0bf81abaed/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/715fe43340d88e450b275e33c0ccd0fbcfffdf6ed33772b4150d3af07d1a9634/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

Event `chaosx.weaponized_zombies.8`:

- inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c26bb14304bd920cac05da2beaac9dd8f15709d771b4f7661110e089cf1c9f6c/0d4ac1e7543d8c1ef32c5bf7811b795364acdd8475dce28499a10f7c7fa6d194/event-trace-3ac0bcfca142.json`, application/json, 1062095 bytes, SHA-256 `c26bb14304bd920cac05da2beaac9dd8f15709d771b4f7661110e089cf1c9f6c`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e09f6d7e6433dce0a43e036f367fb5ce81071150bbd114cac7816b538aa3b18/47efbd11c58c2ee6aca33e82faa95b2cef29d320b9a40653f58c4f7906e88fb4/event-timing-3ac0bcfca142-manifest.json`, application/json, 42799 bytes, SHA-256 `4e09f6d7e6433dce0a43e036f367fb5ce81071150bbd114cac7816b538aa3b18`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bed78cdb2c559413c99d057606f0ae73190476d90c09281ab246817607f607c5/a13f6d3c7de85d34e222597ce1dd47d2c03dd98a3568b72e8df29648b11a2e7a/event-timing-3ac0bcfca142.json`, application/json, 41010 bytes, SHA-256 `bed78cdb2c559413c99d057606f0ae73190476d90c09281ab246817607f607c5`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a/6c3fed5e28d7087cf00a200a6f711962425b05d0c27048dc7df686b94c4d943a/event-timing-3ac0bcfca142.svg`, image/svg+xml, 19291 bytes, SHA-256 `01acc3df1cf64aeca1d1e8a5e976aeb9e61bbfccb2f256941e6117717752354a`.
- render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7/cfbcc83984cf570472a411d7ba00dfd5a1c44c79423e5f8b54d40682f53200c9/event-timing-3ac0bcfca142.png`, image/png, 4956 bytes, SHA-256 `79d13e693be8a354509fd9b90b170dafed77d708c2c80c46b7a04e18396784c7`.

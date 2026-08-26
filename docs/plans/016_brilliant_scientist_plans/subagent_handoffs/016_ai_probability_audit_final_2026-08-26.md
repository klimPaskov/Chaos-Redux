# Event 016 final weighted-logic audit

Date: 2026-08-26.

Owner: `chaosx_ai_probability_auditor` subagent, read-only handoff to `/root`.

Status: partial evidence-only audit. No gameplay, AI, event, focus, decision, mission, project, raid, constant, localisation, or runtime source was changed and no commit was made by this audit. No live Hearts of Iron IV completion, normalized campaign probability, or balance certification is claimed.

## Scope and result vocabulary

This handoff covers exactly the requested Event 016 weighted surfaces: the four evolutions, opening/host/referral, Directorate actions, D'Rhondan expeditions, Alien Infantry landing, D'Rhondan rebellion 10/20/40 tiers and the 90-day pulse, the D'Rhondan focus and AI routes, the special-project selector, Event 019 provider selection, Portal raids, and terminal/world-end routes.

`Exact` means the declared candidate pool and direct values were resolved by MCP for the named scenario. `Bounded` means the pool or threshold supports a limited ordering or boundary conclusion but not a campaign rate. `Sampled` would mean a seeded simulation; no sampled result was produced. `Score-only` means an AI willingness or factor trace, not a click probability. `Unresolved` means that a required adapter, candidate, gate, state, cadence, or external factor was unavailable.

## Source, reference, and reproducibility boundary

The repository `AGENTS.md` was read before this audit. The repository skills `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-event-planning/SKILL.md` were read and applied as relevant.

The complete 44-file Event 016 specification package under `docs/specs/016_brilliant_scientist_specs/` was read, including the accepted core, host/Directorate, project, exactly-four-evolution, KRG/focus, world-reaction/AI, super-event/world-end, acceptance, matrices, source ledger, and handoff documents.

The required offline Paradox wiki pages were read: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. The required vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and the script-constants documentation.

The audit includes the repository history through commit `18f7c7d6708bf252708353f3a50b7301162d37ac` (`docs: attest directorate gui and localize dhrondan outcomes`). The shared-worktree HEAD at the time of the final source fingerprint was `3fd004225caf3f10aab2ab052117245ab21143e7`, so current file hashes below are not interchangeable with older MCP artifacts whose source revision is explicitly different. Unrelated pre-existing worktree changes were preserved.

### Current source fingerprints

These SHA-256 values were captured from the current shared worktree for the weighted surfaces. They are source fingerprints only and are not claims that a matching MCP analysis completed at this revision.

| Source surface | Current SHA-256 |
| --- | --- |
| `events/016_brilliant_scientist.txt` | `11985C5077E92D8227311082BD6828562E0B2E1D7447C8886B33ABBAD7274101` |
| `events/016_brilliant_scientist_evolutions.txt` | `742E4855DC4B47074E39F3A310C2C1180C55471A39DA646FC2C8AB0B3A56C907` |
| `events/016_brilliant_scientist_context_events.txt` | `9C2A9B9E2567A26093670CA27B0B60F09EC03EF3352EAAC788F769EA7802481B` |
| `events/016_brilliant_scientist_dhrondan_contact_events.txt` | `095ACBE2888C05F225740BBC7DC2C8015CA18EC14AB69EE23EA9160624496827` |
| `events/016_dhrondan_country_events.txt` | `6A020C97DA4047989A22BA7495085F9FAFFB3DB92E213457A1091CE825B59796` |
| `events/019_infantry_spawn.txt` | `CC4895B29BB870651C591A6BFF610C41E41EDFAE9DA2BEA2F0A63056FF8B1A66` |
| `events/019_infantry_spawn_scenario.txt` | `815178844629ED674803AE07437D645813BEE9E0C4B1E1990FEB9BD5772A23E0` |
| `common/decisions/016_brilliant_scientist_foreign_decisions.txt` | `E7DC774843599C2A3B03705C4CBE77821D71720917EA48486B8961CCAD33D0CF` |
| `common/decisions/016_brilliant_scientist_directorate_project_board.txt` | `23B9CA7D73D8F2CC8CA6207F695BA08C8D4ABED3695BA8C3FB35960D3FBB67FD` |
| `common/decisions/016_brilliant_scientist_evolution_missions.txt` | `D96557575E506AA38A80A600F82E6690E1A19FD0427B3ABD4C36F8E6D220781E` |
| `common/decisions/016_alien_infantry_landing_decisions.txt` | `6DB11ED949357944CFA9D8EFCED2E25D82F9A64C6FF1DF9D9C2BF20B39C80CB5` |
| `common/decisions/016_dhrondan_contact_decisions.txt` | `D991406DA31AB1402D233167A8C1EA7C05F9FEA6809D9E294188760F9ADD5E82` |
| `common/scripted_effects/016_dhrondan_contact_effects.txt` | `3FE4074057CC8E3196C7220C6C50B8522EADEFC35D7ACE1446FC7FC9E6ED4740` |
| `common/scripted_effects/016_brilliant_scientist_context_effects.txt` | `9D8C724223F61E844B655A05E2447AEA7B761537EBC116CC3C5329EA8AE55418` |
| `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` | `CB8320FCE95ACB25C7D2DA12517CA6B072B943873827B8489613F1EEA8F8032C` |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | `475CB9AB9A5F31784E8C9E1997C1CE8E25AF0F9BA75C59A2E046B84A17326213` |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | `350464DF13E8401F1C5ACDBBBE279CA05EF6482D9742B5B39163113D33218A8F` |
| `common/scripted_effects/016_brilliant_scientist_directorate_outcome_effects.txt` | `5550C121939B3189EB50F1A66E5D07387B87136EFB3480884FA0F3E0C7BF0D2F` |
| `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` | `CFCEC7C0DF758F698C8959514C06312FF6F1AFCA1A186497D7BEFFBF45FF1392` |
| `common/scripted_effects/019_infantry_spawn_core_effects.txt` | `80425CA2558816D078F0D5BEE046D1DD04F74646893AC58A54DC9E2FB5AFBB23` |
| `common/scripted_effects/019_infantry_spawn_scenario_effects.txt` | `92765FEB01EAC13692FF82B335DC3E1E09EE4405C90364F1FA9673B555C7D8AE` |
| `common/raids/016_brilliant_scientist_portal_raids.txt` | `6622C192BDE870E7109F52EC4448A3A2E5F8C5C9E05909A68B3F906AD0F17ABF` |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `B1148C8516E6743BE727EE59ABE3BEB03C8CD347342DB8A2C09D4F2DCFA7CDD8` |
| `common/special_projects/projects/016_dhrondan_envoy_project.txt` | `77611ED129EBC20F744AF1B15143CF24EA29892EE04FCC46723AA6D801B1841E` |
| `common/national_focus/016_dhrondan_focus_tree.txt` | `746C49F4232E8C21C2499E638B681347F9E80A41A273600F651731C647026AD8` |
| `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` | `55C8EADC89509FE65528158470122F0B96F205C5DA32F6F46B43D252648F7D13` |
| `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` | `4ADDED732338182899773208440E782B66072082C9582BCA2FA428B390F2101C` |
| `common/script_constants/016_brilliant_scientist_constants.txt` | `97B2B3FD628209383BE88C213872E9078A48706CD573353CBAD294607DE796D7` |
| `common/script_constants/016_brilliant_scientist_evolution_constants.txt` | `D716F3A13C4C2410B7D83F3DCABCABB76A3E6AC40855524AC30A6EBED320BA35` |
| `common/script_constants/016_brilliant_scientist_project_force_constants.txt` | `F7A2328CF14944DD045B6CC0B25DEA3D0E7F364987DB6B1FB75CB017EDD5EA7B` |
| `common/script_constants/019_infantry_spawn_constants.txt` | `E0420F46D0F1BC7D184308E6B496B3B4AA5A883A4FF8EC15E68D04BDEF4463C4` |
| `common/mtth/016_brilliant_scientist_mtth.txt` | `24AA832E7820359AF3F69CB6C0AF5007441E961CC580AF8FC5D46A4216A7C4A2` |

## MCP execution receipt

The probability workspace was `mod_chaos_redux_ea3b2d67c2c0`. The retained successful artifacts report Operation Postern 1.19.2.0 (`d245`) and adapter `hoi4-1.19.2.v1`. Available probability adapters included `event_mean_time_to_happen`, `event_option_ai_chance`, `decision_ai_will_do`, `mission_ai_will_do`, `national_focus_ai_will_do`, `technology_ai_will_do`, `doctrine_ai_will_do`, `direct_random`, `random_list`, `ai_strategy_factor`, and `custom_weighted_pool`. No callable `chaosx_ai_probability_auditor` subagent route was present.

The final fresh broad call began with the required read-only `hoi4.probability_inspect` for `adapter=event_option_ai_chance`, source `events/016_brilliant_scientist.txt`, `refresh=true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. The caller-side bounded result after exactly 45 seconds was `{"status":"timeout","timeoutSeconds":45}`. No MCP artifact or server completion was returned.

The first fresh `hoi4.probability_evaluate` retry used a declared random-list source and candidate pool but sent `scenarioSet` as an array. The exact MCP validation response was `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate: Invalid input: expected object, received array at scenarioSet`. No artifact was created.

The second retry changed `scenarioSet` to an object containing `scenarios` but omitted the required set `id`. The exact MCP validation response was `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate: Invalid input: expected string, received undefined at scenarioSet.id`. No artifact was created.

The corrected retry used `scenarioSet={id:"EVENT016_FINAL_REBELLION_AUDIT_2026_08_26",scenarios:[...]}` with the complete two-entry rebellion pool. Its caller-side bounded result after exactly 30 seconds was `{"status":"timeout","timeoutSeconds":30}`. No artifact or MCP completion was returned.

Earlier MCP server calls that did return artifacts used the source revisions and scenario hashes recorded below. Later refresh or render calls for several of those analyses returned the server's exact `timed out awaiting tools/call after 180s` or `PROBABILITY_ANALYSIS_STALE` outcomes. The 180-second server timeout is distinct from the fresh caller-side 45-second and 30-second bounds above.

The structural MCP receipts retained for context are `hoi4.event_inspect`/`hoi4.event_render` for `chaosx.nr16.47` and `chaosx.nr19.1`, `hoi4.focus_inspect`/`hoi4.focus_render` for `dhrondan_focus_tree`, and `hoi4.gui_inspect`/`hoi4.gui_render` for `kruger_directorate_container`. Structural evidence does not replace the probability pass.

## Surface audit

### 1. Exactly four evolutions

Sources and identifiers: `events/016_brilliant_scientist_evolutions.txt:13-319` contains exactly `chaosx.nr16.21`, `.22`, `.23`, and `.24`; the related MTTH entries are in `common/mtth/016_brilliant_scientist_mtth.txt`; the supporting weighted modifiers are centralized in `common/script_constants/016_brilliant_scientist_evolution_constants.txt` and `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt`.

Required first inspect: `hoi4.probability_inspect`, adapter `event_option_ai_chance`, source `events/016_brilliant_scientist_evolutions.txt`. The retained artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31d98b6469875bb8374ad5d798fa076e2041d5a53962232dd4211fc6bc77a282/34a92a927d28d6c1346babf9102e2ab8bd9a2a265394eaf003b76bcfcc07243a/probability-inspect-991079c10600.json`. It discovered 18 option candidates, nine required inputs, and one unresolved source input.

Named evaluate scenario set: `event016_evolution_route_matrix`, 365-day horizon, with `public-university-peaceful`, `secret-militarized-wartime`, `industrial-colonial`, and `refugee-threatened`. The result was `PROBABILITY_ANALYZED_PARTIAL`, 72 candidate-state projections, and 47 unresolved or bounded items. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c78cdc232be5cdd73e1cd687d97f0d8cdba02617f8836541ef28bd7d442c7c16/191482b99cb0041808abc41e75d27a5cc63bb185649b720063d49514c90bf65b/probability-765fc96522ac314a39e4a77c.json`.

Classification: `Score-only`/`Bounded` partial. The artifact keeps host-archetype and evolution modifiers unresolved rather than assuming flags. It does not prove a complete eligible option pool, a normalized selection probability among all Event 016 choices, or a median/MTTH timing distribution. No seeded simulation or sequence was run because no uncertainty distribution, seed, or complete chronology state was declared.

Review finding: the four evolution entries have distinct gated modifiers, but ordering is sensitive to host archetype, public/secret route, war, factory/technology state, project history, and context flags. Those external factors must be typed in an adapter-supported fixture before any dominance or starvation claim is valid.

### 2. Opening, host, and referral

Sources and identifiers: opening dispatcher and first appointment are `events/016_brilliant_scientist.txt:15-183` (`chaosx.nr16.1`, `.2`, `.3`); host-context outcomes are `events/016_brilliant_scientist_context_events.txt` (`chaosx.nr16.4`, `.5`, `.12`); foreign host/referral decisions are `common/decisions/016_brilliant_scientist_foreign_decisions.txt`; context and foreign effects are `common/scripted_effects/016_brilliant_scientist_context_effects.txt` and `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`; MTTH-backed opening entries are in `common/mtth/016_brilliant_scientist_mtth.txt`.

Required first inspect: the fresh broad `event_option_ai_chance` inspect against `events/016_brilliant_scientist.txt` timed out after exactly 45 seconds with no artifact, as recorded above. The retained foreign-operation inspect used `decision_ai_will_do` on `common/decisions/016_brilliant_scientist_foreign_decisions.txt` and found three candidates, eight required inputs, and zero inspect diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bae41df915a513cf153c204919f8ebdc1c6c59313194abbe4e39cdbdc99b5072/283bd2341f14df0bdffa667ba24975599746eeeed8d681fac59cbdb1a97f177d/probability-inspect-0ae25e42fffa.json`.

The source shows public and secret appointment `ai_chance` bases and modifiers for government, stability, war, civilian/military industry, computing technology, public compact, secret Directorate, and host archetypes. Referral options are guarded by initial-referral and eligibility state. The foreign decision array additionally requires valid targets, hostile/capitulated/nonhuman filters, actor locks, incoming caps, event-target persistence, and cleanup. These are score modifiers and eligibility gates, not a complete candidate pool for all eligible countries.

Classification: `Unresolved` for opening/host/referral normalized probabilities and MTTH timing. The retained foreign inspect is `Bounded` source discovery only. No exact fire-once opening rate, host share, referral rate, target-country race, or timing distribution is established. Recommended next fixture: enumerate a complete eligible-country target pool and public, secret, send-away, referral, invalid-target, and dormant-holder states with all country flags and global settings represented in the adapter vocabulary.

#### D'Rhondan response event `.49`

The response surface is `events/016_dhrondan_country_events.txt:20-93`, event `chaosx.nr16.49`, with options `chaosx.nr16.49.a`, `.49.b`, and `.49.c`.

Required first inspect: `hoi4.probability_inspect`, adapter `event_option_ai_chance`, complete three-option pool, source revision `28b43c58202177584f5204452cd5dd11dce10d1557835c1a39736c53fc1029c0`, source hash `3450c0c84ae155683be4e87b3142e167a73a9beca4b56a7a4d8d1239d25f7909`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8646acf2dfdf7d897d8435df5bd30d142b14bb92b6ff21e1f9989308afa067e3/f9850d05c0c85d37f3ebf7b02a959b9dbc5b1fa0a111d4cbece5bed8899ac50e/probability-inspect-3450c0c84ae1.json`.

Named evaluate scenario set: `DHR_EVENT049_EMPTY_FIXTURE_2026_08_26`, scenarios `VALID_PACT`, `NO_CONTACT`, and `EXISTING_DHR`, with state `{}`. Analysis `probability-4b059ff4deb5de803cfb9855`, scenario hash `1dec3e43413e565596e91e561de18c06fb600e79553974dbf071bf1804c6e18c`, three scenarios, nine rows, and source revision `28b43c58202177584f5204452cd5dd11dce10d1557835c1a39736c53fc1029c0`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0c1de79a92467e10d456f5ac10f0468935c9293168f52a29793b0fd5665eac8/e446f258f6f4d2aaa3bb388a4030860e43f5a9b9b88d9de6f6342818e32959cb/probability-4b059ff4deb5de803cfb9855.json`.

Diagnostics were `EVENT_OPTION_FALLBACK_NOT_PROVEN`, `.49.a` never eligible, `.49.b` never eligible, and `.49.c` dominant in all three empty-fixture scenarios. The result is not proof that `.49.c` is a valid live response: the event root requires `dhrondan_compact_response_is_valid=yes` at lines 20-31, while `.49.c` is an invalid-state cleanup path at lines 82-93. Classification: `Score-only`/`Unresolved`; no normalized `.49` option chance or fallback safety claim is valid. Recommended owner review is to separate invalid-state cleanup from the valid response event, or otherwise make the root and option gates mutually coherent, then rerun with complete diplomatic actor, opinion, government, and compact-response fixtures.

### 3. Directorate actions

Sources and identifiers: the project-board weighted surface is `common/decisions/016_brilliant_scientist_directorate_project_board.txt`; related institutions, facilities, and foreign liaison are `common/decisions/016_brilliant_scientist_directorate_institutions.txt`, `common/decisions/016_brilliant_scientist_directorate_facilities.txt`, and `common/decisions/016_brilliant_scientist_directorate_foreign.txt`; outcome helpers are in `common/scripted_effects/016_brilliant_scientist_directorate_outcome_effects.txt` and their constant/trigger files. The Directorate GUI is `kruger_directorate_container`.

Required first inspect: a current source-wide `probability_inspect` was attempted before narrowing but timed out at the 45-second bound. The prior source review records 28 selectable Directorate decisions with `ai_will_do` plus the activated non-selectable `brilliant_scientist_loyalty_review_mission`; no current complete project-board candidate pool and scenario evaluation artifact was produced in this final pass. The old Directorate decision audit is source/trigger evidence, not a current normalized probability result.

Structural context: `hoi4.gui_inspect` returned `GUI_INSPECTED` with 22 Event 016 elements for `kruger_directorate_container` under `event016_directorate_compact_current`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a755b7324445bb88434e9613711b92daefcddd410e50124c56969d43225a3710/316ed573267e20625432412e0b8f9277b772a6022745f36dd9ef95f4c0ea4fa1/gui-inspect.ab24df94636a45c9.json`. The linked GUI render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/eb45207d69a6d48fb59949eb762a10a3b52bbe29908a3cd9dc294bfe54351b64/kruger_directorate_container-full.svg`; this is presentation evidence only.

Static score findings: the source uses route, government, war, Exposure, Project Capacity, Independent Capacity, control, intelligence, resource, and target modifiers. One-use flags, cooldowns, target triggers, resource gates, and host-loss cleanup are present in the reviewed source. However, the complete simultaneous eligible action pool, factor traces, project-stage state, and action cadence were not MCP-resolved. The project-board scores therefore remain `Score-only` and cannot support dominance, starvation, rank reversal, or repetition claims. The old pattern that hardcoded/elevated `ai_high` or `ai_urgent` values should be checked with a complete pool before tuning; no tuning recommendation is made here.

Recommended owner follow-up: inspect the full 28-choice project-board pool with route, cost, cooldown, target, capacity, and host-state fixtures, then sweep factor paths for action dominance and starvation. Treat the GUI artifact and source audit as non-probabilistic context.

### 4. D'Rhondan expeditions

Sources and identifiers: `common/decisions/016_dhrondan_contact_decisions.txt:17-143` contains `dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda`, and `dhrondan_honor_accord`; `common/scripted_effects/016_dhrondan_contact_effects.txt:139-209` owns begin/debit and `dhrondan_ai_try_authorize_expedition`; mission timers and cancellation are in the same decision file; constants are in `common/script_constants/016_dhrondan_contact_constants.txt`.

Required first inspect: `hoi4.probability_inspect`, adapter `mission_ai_will_do`, source `common/decisions/016_dhrondan_contact_decisions.txt`, complete candidate pool `{dhrondan_honor_accord, dhrondan_send_kruger_to_dhronda, dhrondan_send_mengele_to_dhronda}`. The retained inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b6bad52efe5c36c2f44f9c0a6c8f3b313f09a9d34cf89916457a815c94b95ce/6328d96f90d99757cc84d523c1e72e7c35d1391cfd7e8640310bee42445a6585/probability-inspect-4a370bea603b.json`; source hash `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`. It reports three candidates, an incomplete runtime pool, and zero unresolved inspect inputs.

Named evaluate scenario set: `DHR_CONTACT_MISSION_BOUNDARIES_2026_08_25` with `NO_CONTACT`, `KRUGER_VALID`, and `MENGELE_VALID`; the retained evaluation uses source hash `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`, scenario hash `f2a98db3da2f984cb5e3b50312f34f7d96c28a6bb3d1973febfffb8936629326`, and analysis `probability-b8cebaa477512d4b075e6a36`. The result was `PROBABILITY_ANALYZED_PARTIAL`, three scenarios, nine rows, 11 unresolved items, and eight diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9fdf89bef67a4c75ee9babac612d6cf66ce2bd688005202e5b2d6e2248cab1d/5a9702299c2b9ca07aea344ea734044492c28383f0f1db454ea7a5989f515b1d/probability-b8cebaa477512d4b075e6a36.json`. Retained ranking and matrix artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67ba7f7d024b2c562b3c908443b8faccd14c646b9fa358f34ff7464352edb38f/5c2806d7236d50724ba5f1fb3cb6de726c15fcd0789b3296206834627135a741/probability-probability-b8cebaa477512d4b075e6a36-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c1060abfad4b9be2f38f2cefdc928a3075d88c7a8349e74b3028e1dd9d7c06d/e981bfce2588fb59d6a6f70859ee30faf1cf7a9a2c91de54ba2b0e7ebc7b0bc4/probability-probability-b8cebaa477512d4b075e6a36-matrix.svg`; the unresolved view is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82d1506a90f1e34eecbd71aa9448006c988556b0a0b5ba55f9f3529a4c62ee69/1c34a1750006aa5ae8d90de1e391a708ec51454ab316cabc5367a19cf32d1c54/probability-probability-b8cebaa477512d4b075e6a36-unresolved.svg`.

Result: `Score-only` partial. The trace expanded the expedition score from base 1 to 10,000 and emitted `PROBABILITY_EXTREME_MODIFIER_GROWTH`; source constants also expose a dominant expedition AI value. This is a willingness-score warning, not a click probability. The helper is deterministic Kruger-first: when both routes pass it tests/begins Kruger before Mengele, so it is a first-valid route priority rather than a normalized two-way random pool.

External inputs unresolved by the adapter include character existence/identity, project completion, route and country identity, `custom_trigger_tooltip`, pact strain, PP/fuel, cooldown, and live target/helper state. The source contract is 50 political power, 500 fuel, and a 180-day mission. No 180-day success/failure timing distribution, route starvation, or campaign repetition rate is MCP-proven. Honor Accord is a separate score/rule path and not a substitute for a Kruger/Mengele probability.

Recommended owner follow-up: document the intended deterministic Kruger-first priority or expose a complete explicit route pool before tuning the 10,000 value; then rerun the same named scenarios with typed nested helper state and compare only after an owner-applied change.

### 5. Alien Infantry landing

Sources and identifiers: `common/decisions/016_alien_infantry_landing_decisions.txt` defines `alien_infantry_call_landing`; country-scoped receipt and target helpers are in `common/scripted_effects/016_alien_infantry_api_effects.txt` and `common/scripted_triggers/016_dhrondan_country_triggers.txt`; constants are in `common/script_constants/016_alien_infantry_api_constants.txt`.

Required first inspect: the requested decision adapter returned `PROBABILITY_SOURCE_DISCOVERED` with an empty requested route and suggested `mission_ai_will_do`; the discovered candidate was `alien_infantry_call_landing`. The retained inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba5df215c4597dc8b93ed286e3ef8a68f9de8030ef0db45a30451759f9c70bb/c77bf302d219c97c7c01d6cd5f37f42bb13ab7f3d5f0bd7df3da6df2dcd64919/probability-inspect-ee65b59c5aeb.json`; source hash `ee65b59c5aebc613eb16d5e63f8819ef7ad89390e5a7cd50e65777b105b0ebfc`.

Retained evaluate sets were `DHR_LANDING_AI_BOUNDARIES_2026_08_25` and `DHR_LANDING_AI_COMPLETE_RECEIPT_BOUNDARIES_2026_08_25`, each with `NO_CONTACT`, `BASE_VALID`, and `ALL_LANDING_MODIFIERS`. The follow-up analysis is `probability-d7d344df73dc57572483baee`, source hash `ee65b59c5aebc613eb16d5e63f8819ef7ad89390e5a7cd50e65777b105b0ebfc`, scenario hash `94d0aeae0be759d27ad0ce69adc33677b4494b89d41eb219bffe5cb3826f20db`, one candidate, three rows, seven unresolved items, and four diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab13e82780c8b85f6ca381da9279793aa4badc06e0d1ed692dcf9ce42cd4d391/d14c1797ac6ecf52bbfdc03a0bdfba51b65cad959d94502cfc003cbdc5301339/probability-d7d344df73dc57572483baee.json`; ranking and matrix artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a060ddfebb88e996cc6285d04f5b92639f1ffb62202d09cbb1482d385e672f0/9fb8cc3d943075972050f600b3cec29d0906d8ef1d7ad3d249d92e77c2a0c5d8/probability-probability-d7d344df73dc57572483baee-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a3e3a00a8a369d56e03e3b8149da9e684ef28cb392509b3be772044f4b352aa/7e686f6eb14e87c662bbdaf72c6bfe7be004c9b14a026b8e349e9d14d27b6682/probability-probability-d7d344df73dc57572483baee-matrix.svg`; unresolved view `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77ef599430cf74ee4b1abe7791690bbc5f03551a5eb7979dcca65dbc123f5510/9722ebd8ccbec9932c5823944efa14f345fbc69a2e3043012b84a111ab93c61e/probability-probability-d7d344df73dc57572483baee-unresolved.svg`.

Result: `Score-only`/`Unresolved`. The one-candidate pool cannot produce a target selection probability. The source score has network, reserve-priority, guarded-descent, and near-space factors, but all four were inactive or unresolved in the supplied fixtures. The public gate and state-target pool remain unresolved, including five contact receipts, `num_equipment@alien_laser_weapon_equipment_1`, `any_controlled_state`, pending/cooldown/world-end state, and target ownership/control. The accepted contract requires 2,000 alien guns, a valid controlled state, a seven-day reservation, a 30-day base cooldown, and DHR receipt/focus gates, but the adapter did not prove those live states.

No normalized landing probability, target rank, repeated landing cadence, or equipment-starvation result is claimed. Recommended owner follow-up: rerun via `mission_ai_will_do` with all receipt variables, equipment, state target, pending/cooldown/world-end flags, and the four modifier states represented in adapter-supported nested fields.

### 6. Rebellion tiers and 90-day pulse

Sources and identifiers: `common/decisions/016_dhrondan_contact_decisions.txt:147-155` owns the country-scoped 90-day pulse mission; `common/scripted_triggers/016_dhrondan_contact_triggers.txt:141-196` owns arrivals/strain/Chaos tier predicates; `common/scripted_effects/016_dhrondan_contact_effects.txt:324-369` computes temporary weights and enters the two-entry `random_list`.

Required first inspect: `hoi4.probability_inspect` with the complete pool `common/scripted_effects/016_dhrondan_contact_effects.txt:359.entry.1` (revolt) and `common/scripted_effects/016_dhrondan_contact_effects.txt:359.entry.2` (no revolt), using `random_list` after the unsupported custom-pool route was checked. Earlier successful inspect artifacts exist at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c72b074d9aeaae47cd2dc9ca6011d099f0b71d2a8289d6a018e6d9d40936f776/09d5f8b16d74cfa31fb7af4fd4c775213fcd79a4694615babc8fc8128b2dfe47/probability-inspect-4ecd98b765f6.json` and the later refreshed current inspect at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83beb6dc22d96f6c267bec8983dd9fb723a49f1e63c4107be38c5dd87f6583d9/88208a57a0385f1f5421c7d7f3447940ed1ad078f13ba06504f7e2b73c9deb36/probability-inspect-4ecd98b765f6.json`. The later refresh subsequently timed out after the exact server-native 180-second limit.

Named exact conditional evaluation: `DHR_REBELLION_TIERS_2026_08_25`, analysis `probability-fedc30a49c5461669eb47b59`, source hash `4ecd98b765f62b7a2fc88c22fd9c0a461f1722465f80d6ed082b50db505ed86`, scenario hash `94075e1cecd98fc7c4850396fe680b32938962596cd1cdd7a145a31df2344dcf`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa838f159810ca6f095235a1cabd42cf180cf5fcbb486ac6deeb0f6e4d66c73/9b7f24f7e1b5706ef83b53d9eed196e42eaeae20cb2a124f3bcac7107506c32c/probability-fedc30a49c5461669eb47b59.json`.

| Scenario id | Revolt | No revolt | Classification |
| --- | ---: | ---: | --- |
| `NO_CONTACT_BELOW_6` | 0 | 100 | Exact conditional pool probe; event activation gate itself was not typed. |
| `ARRIVALS_6_CHAOS_600_STRAIN_30` | 10 | 90 | Exact conditional weights. |
| `ARRIVALS_7_CHAOS_799_STRAIN_49` | 10 | 90 | Exact conditional weights. |
| `ARRIVALS_8_CHAOS_600_STRAIN_30` | 20 | 80 | Exact conditional weights. |
| `ARRIVALS_9_CHAOS_799_STRAIN_49` | 20 | 80 | Exact conditional weights. |
| `ARRIVALS_7_STRAIN_50` | 20 | 80 | Exact conditional boundary. |
| `ARRIVALS_7_CHAOS_800` | 20 | 80 | Exact conditional boundary. |
| `ARRIVALS_10_CHAOS_800` | 40 | 60 | Exact conditional high-tier boundary. |
| `ARRIVALS_12_CHAOS_900` | 40 | 60 | Exact conditional high-tier result. |

Retained rendered ranking, matrix, sensitivity, threshold, and unresolved artifacts are respectively `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3627dbe1be3cd9dc2af95d6525b55a6443fcedbacd89aaec0466e9e8f2e5e67f/7a83b2f1d6cfd3301a21e8eef31e1fb447d0883e30ce27776337d6d63960da25/probability-probability-fedc30a49c5461669eb47b59-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81bdf51e16e9f36b0b8db1ee467da2ecf821ee19a56fda8aed9a1a42dab7bcfc/c403b40e416d8b68429d913fbd3444562a38fef7f5bd7a4fa67534f64f0b1a76/probability-probability-fedc30a49c5461669eb47b59-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5c9f25c05e945e4802758bf83a6ae6c00e228396e9d6b66826e5e21c99ad27/f63620b16987b158ff0754ceb7f9f6a35a7f588f83f8a0a990a76bd261a656ad/probability-probability-fedc30a49c5461669eb47b59-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a1d04933d4bee944ffe273a6638b17e8217400e7f2a1272f8b890f82789bfc6/1502c4c0e3691122c3e2cc28f600fc69a31a55f44bfaebc72c10c9cc379130db/probability-probability-fedc30a49c5461669eb47b59-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/443e8acd517504f04adcf1e6efea6d55fa28c3055471fff32d40f99bd9ca2ee1/probability-probability-fedc30a49c5461669eb47b59-unresolved.svg`.

Result: `Exact` for the prior declared two-entry pool and direct temporary weights only. The analyzer proved 0/100, 10/90, 20/80, and 40/60 conditional arithmetic and no rank reversal across those rows. The 100% no-revolt row, 90% no-revolt low rows, and 0% revolt below the gate generated dominance/starvation warnings that follow directly from the authored guard and tier values; these are not tuning conclusions.

The one-country pulse cadence is 90 days, but it was not modeled by the random-list adapter. Therefore no cumulative 90-day chance, campaign rebellion timing, pulse repetition distribution, or terminal transition probability is claimed. A current empty-fixture evaluate `DHR_REBELLION_TIERS_2026_08_26` returned partial unresolved temporary weights; its JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/997466e06f37ab3ed70b1006f78eaf719508345605b7527d27295b31437e0863/98047d949568d2807a6adb67824bfada8d9a58d12d8ec46d2d831a4860c6ae62/probability-2d595dd5bd4379910d449446.json` and does not supersede the prior exact direct-weight probe.

Static boundary finding requiring owner review: the low/medium triggers define low maximum 7 and medium maximum 9, but the medium predicate uses `arrivals < high_minimum` without an explicit medium maximum. The resolver checks high, then medium, then fallback low. Thus 10 or more arrivals at Chaos 600-799 and Strain 30-49 can fall through to the low 10% weight instead of a documented medium/high partition. This is a source-logic risk, not a normalized MCP result. Add explicit mutually exclusive 7/8/9/10, 49/50, and 799/800 boundary scenarios after any owner patch and compare with the same named set.

### 7. D'Rhondan focus and AI routes

Sources and identifiers: `common/national_focus/016_dhrondan_focus_tree.txt` contains the 88-focus D'Rhondan tree; `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` contains the Imperial, Synod, and Covenant route plans and their route factors. The accepted architecture has 88 focuses distributed across the eight categories and three regimes, with eight political focuses per regime.

Required first inspect: `hoi4.probability_inspect`, adapter `national_focus_ai_will_do`, source `common/national_focus/016_dhrondan_focus_tree.txt`. Retained artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1647b85b6f7eb3bad1106d090a76185e041c2b68ec4624ea1dc940d8159caf2a/49dab23e27e48bca89bd5b46b56fdd381a88ef7c2974658d8fceda206c217172/probability-inspect-b26c8dfcf7fc.json`.

Named evaluate scenario set: `DHR_FOCUS_EMPTY_FIXTURE_2026_08_26`, scenarios `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, `EXISTING_DHR`, and `LOW_CHAOS`, with state `{}`. Analysis `probability-5da6cbf5638913657ff42674`, source revision `28b43c58202177584f5204452cd5dd11dce10d1557835c1a39736c53fc1029c0`, source hash `b26c8dfcf7fc408dd8bff0459a7f38c03320494de1e8578d293739ea365585c7`, scenario hash `69d23577310be67e773ddc0b748bbd81bef666fc8437a19514da55b04d617229`, 440 rows, 130 unresolved items, and 34 diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a846295be4a94fd0ed0d3717ddbec047569154bc96a77253c51b236538ea05e5/5c66fd2fc920c515e37fae2ee1151adc479572038427d2c2d576ddcfe679ff34/probability-5da6cbf5638913657ff42674.json`.

Result: `Score-only`/`Unresolved`. The pool declaration is 88 focuses, but the empty fixture does not prove dead focuses, route starvation, click probability, or timing. Prerequisites, bypasses, route-plan activation/abort, country identity, crisis choice, prior focus history, and external modifiers remain unresolved. The structural focus inspect independently returned 88 focuses and 102 connectors with zero crossings, intersections, or long connectors; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ab31f7f3b3db75186edae4832c433bb17d3cf8ac4a1c40a5a771b4b80d13ead/c36e3b3ed4f8b3dfe32fffe86a965bb1e0d1cbe54c7519a86ec48824f5dec0da/focus-inspect.cffdde6def51b0c0.json`. The structural render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23b539c032ae69ed551b0d3b9fbf0d05ca7578c374e400fe1a67d49d4eee96d2/f588180f174b5ddf72877f8fcabb4d2ee9bd6deec88183e189875aaafb228af3/dhrondan_focus_tree.focus.html` at 6992 by 2788 pixels.

Static priority finding: support-lane focuses `DHR_guard_the_descent_windows` and `DHR_make_near_space_ours` carry inline factors not represented in the route-plan priority table. This is a potential route-priority/documentation gap, not proof that either focus is unreachable or dominant. Recommended owner follow-up: rerun the complete 88-focus pool with active route plan, abort conditions, prerequisite/bypass history, and crisis state, then sweep route-factor interactions.

### 8. Special-project selector

Sources and identifiers: the nine-entry selector is `common/scripted_effects/cbrn_project_effects.txt:12-88`; the D'Rhondan special project is `sp_dhrondan_envoy_craft` in `common/special_projects/projects/016_dhrondan_envoy_project.txt:15-46`.

Required first inspect: `hoi4.probability_inspect`, adapter `random_list`, complete pool `common/scripted_effects/cbrn_project_effects.txt:29.entry.1` through `:29.entry.9`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eec31b29911f67ae0f646a13e0cb18a4ed5a3bb471cf6428b2b19af41ac5f129/4c9d5c541b830dc95a843a9b23cf98dab2dbabdd4f2e8327fbdda0cca5274785/probability-inspect-fcd942b6523a.json`; source hash `fcd942b6523a72eb7f34bdb0b29097c4a0d3d773e65b07caf23f6c999a8d7066`.

The discovered direct weights are anthrax 10, plague 10, tularemia 8, smallpox 6, zombie 8, Black Plague 8, sarin 8, soman 6, and D'Rhondan craft initialized at 8 with a dynamic eligibility gate. Named evaluate set `DHR_CBRN_PROJECT_SELECTION_EMPTY_FIXTURE_2026_08_26` used `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, and `ANTARCTIC_BYPASS`; analysis `probability-d164c16b542eb43251611f6d`, scenario hash `248820dbd342a96867f54e201684306ac12a165b91b5d74b12a8bfb20a8014cb`, 36 rows. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95ce8893b62263e481b128e1ac83fd4d2df291b1fba8dd6b35a56bf889f5faf9/2d5337c16600c989ef760324b6142d3cf0e9432ca2d473e96e15fb34977894b2/probability-d164c16b542eb43251611f6d.json`.

Result: `Unresolved` for the D'Rhondan selection probability. The nine-candidate pool is complete, but the dynamic D'Rhondan gate depends on route/contact state that the empty fixture did not resolve. The installed adapter set has no `special_project_ai_will_do`; the project `ai_will_do = constant:dhrondan_contact_ai.standard` is therefore source evidence only, not a normalized project-selection result. A later render returned `PROBABILITY_ANALYSIS_STALE` after the source revision changed, so no current render artifact is claimed.

### 9. Event 019 provider selection

Sources and identifiers: registered-provider logic is in `common/scripted_effects/019_infantry_spawn_core_effects.txt` and `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`; provider constants are in `common/script_constants/016_brilliant_scientist_project_force_constants.txt:507-527`; provider 508 is `chaos_unit_family_event16_alien_infantry` with `family_id=508`, `provider_id=508`, `source_event_id=16`, and `spawn_weight=8`.

Required first inspect: `hoi4.probability_inspect`, adapter `custom_weighted_pool`, source `common/scripted_effects/019_infantry_spawn_core_effects.txt`, pool `chaos_unit_family_event16_alien_infantry`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ebdbd52c6e526fe7ad38d20d2cd2ec5b79429659236a31d5450467640893324/9c35bdfa63d622c317cd5bca7f5ce8b868bded9c32ea4c9ab206d090c8d2a5aa/probability-inspect-fa886739163d.json`; source hash `fa886739163d2087a8ab538aeab0edb19fa3c798c7e4953c11eeca5e1f0b2e5f`. The adapter returned `PROBABILITY_SOURCE_INSPECTED`, zero discovered custom-pool candidates, incomplete pool, and one unresolved item.

Named evaluate set `DHR_EVENT019_PROVIDER508_EMPTY_FIXTURE_2026_08_26` used `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, `ANTARCTIC_BYPASS`, `VALID_PACT`, and `EXISTING_DHR`, with state `{}`. Analysis `probability-471a752674c1fdb95fa50d21`, source revision `18f9114cea9c05751a4fbcb078bfbe525794ddcc950fed53aa0b3830eaa306ca`, scenario hash `635c277672806ad03fde8188eec27a1e434406a9823e3eee41304de4fd59d884`, and zero candidate rows. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a63b0ba578e41a8f03756530a35dcac71c6be1d6a186d81749b66214ff7a4d7d/86056e839270c2d9a1bc4f28e00147260d21ebf6469121bcf077c8fb299a8b4e/probability-471a752674c1fdb95fa50d21.json`.

Result: `Unresolved`; the evaluator correctly withheld normalized output with `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. The adapter does not discover the hand-rolled provider arrays in the core/scenario effects, so provider 508's share among providers 504-510 and 522 is not proven. Source arithmetic using `min=1` and exclusive `max=total+1` is not an off-by-one defect, but it remains source-only until the full provider pool is visible to the adapter. No provider starvation, dominance, or sequence result is claimed.

No `probability_sequence` run was valid: the provider pool was incomplete and no complete cadence, cooldown, recovery, removal, reset, timer, or terminal-state manifest was declared. Structural Event 019 inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0676ae7909104fca3360c55205ebbb4cb452f62d4b8be7a19aa28648c2613095/701a8468b6893f1b27cb6829ae2478ce65997462e0eee17b947da8b454a9aaad/event-state_flow-f588a2607444.json`; this is structural provider-chain evidence, not a provider probability.

### 10. Portal raids

Sources and identifiers: native raid definitions are `common/raids/016_brilliant_scientist_portal_raids.txt`; shared raid effects/factors are `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`; the two native raid types are `brilliant_scientist_portal_facility_raid` and `brilliant_scientist_portal_special_project_facility_raid`.

Required first inspect: the retained `hoi4.probability_inspect` attempt used the raid source with the available weighted adapter route and returned no weighted candidates; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7f74f4d0070ec15cb8d64f7f2502e73c739877ef99f163fc92e8afcb2fff7f4/b4df7143e0b7126b39fb8fe723c2922df18504c1181cb210d169ed3e3ffce0d4/probability-inspect-653eee865c1c.json`. A separate `ai_strategy_factor` probe returned `INTERNAL_ERROR` with no usable artifact in the retained raid comparison handoff. No native raid-specific probability adapter was exposed.

Source factors reviewed: both raid types zero AI willingness when actor readiness or target validity fails; then apply Kruger-state, Kruger-AI, major-target, capital-target, and facility-target factors. Native target requirements include controlled/owned industrial or facility targets, six Portal Raider battalions, 60 Teleportation Equipment, a supply-node starting point, a seven-day preparation, 10 command power, and a 30-day re-enable period. Success factors are source-defined base success 0.55, critical 0.15, disaster 0.15 with experience, organisation, strength, and recon terms; `ai_min_success_chance` is 0.25.

Classification: `Unresolved` for raid AI selection, target ranking, success/critical/disaster probabilities, and repetition. Native success-factor source values are not an MCP-normalized result. No raid target pool, external target country set, formation state, or seeded success simulation was declared. The source's destruction of the reconstructed formation after success is an exploit-prevention effect, but no runtime conservation claim is made.

Recommended owner follow-up: use a raid-capable probability adapter or provide a complete native raid target/formation scenario contract before asserting AI dominance, target starvation, or outcome probabilities.

### 11. Terminal and world-end routes

Sources and identifiers: terminal effects are in `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt`; terminal triggers are in `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt` and `common/scripted_triggers/016_brilliant_scientist_triggers.txt`; shared route gates are in `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`; stable IDs are in `common/script_constants/world_end_scenario_registry_constants.txt`; visible terminal events are `chaosx.nr16.901` and `.902` recovery/cleanup events plus the six Event 016 super-event queue IDs. The terminal scenario IDs are `laboratory_world=11` and `strategic_singularity=12`, mapped to visible super-events 93 and 94.

Required first inspect: no installed probability adapter models terminal route gates as a candidate-selection or MTTH surface, and no separate terminal probability artifact was returned before the parent stop. The source-owned terminal audit is therefore structural/source evidence only; it is not an MCP probability result.

Static route evidence: Laboratory World requires the KRG commitment, terminal map/control/administration/submission proof, the final Chaos threshold, enabled scenario, and absence of the armed/fail-deadly Singularity route before setting `world_end`. Strategic Singularity records the pre-lock Chaos threshold and consequences, submits a strategic Fallout request, and only finalizes after the canonical Fallout lock. The two terminal markers and commitments are mutually exclusive, and the shared `world_end`/Fallout lock prevents a second terminal branch after completion. Queue dispatch and actor cleanup are guarded by visibility and fired flags.

Classification: `Unresolved` for terminal route probability, terminal timing, Fallout rejection distribution, and world-end sequence timing. Source constants and flags prove gates and ordering only. No exact terminal date, cumulative world-end chance, rank, or live completion is claimed. No `probability_sequence` run was valid because the complete world state transition, cadence, competing Fallout sources, retries, and terminal states were not declared.

Recommended owner follow-up: if timing evidence is required, declare a complete terminal state machine with Chaos progression, project/commitment gates, Fallout ledger occupancy, retry cadence, settings switches, and terminal absorbing states, then run `probability_sequence` or a supported MTTH evaluation. Until then retain terminal conclusions as source/structural only.

## Cross-surface findings

The Event 016 design mixes three different weighted mechanisms. Event `ai_chance` and `random_list` values are proportional only over an eligible, complete candidate pool. Decision, mission, focus, and strategy `ai_will_do` values are willingness scores that race against other eligible choices and are not automatically percentages. MTTH entries describe timing distributions only when the trigger, base, modifiers, and retry semantics are modeled. The report intentionally keeps these result types separate.

The strongest evidence-backed conditional result is the rebellion two-entry arithmetic: 0/100, 10/90, 20/80, and 40/60 under declared direct weights. The strongest score warning is the expedition trace's expansion to 10,000 and `PROBABILITY_EXTREME_MODIFIER_GROWTH`; this does not mean the expedition is selected 10,000 times more often or that it consumes 100% of clicks.

No complete candidate pool was proven for opening countries, Directorate actions, landing targets, DHR focus routes under live prerequisites, Event 019 providers, raids, or terminal routes. Positive weights on those surfaces therefore cannot be classified as positive probability of a reachable live action without the missing gates and external factors. Empty-fixture “never eligible” diagnostics are not proof of dead content when helper dependencies were unresolved.

No rank-reversal conclusion is valid outside the named complete rebellion direct-weight rows. No starvation conclusion is valid outside the declared below-gate rebellion row and the source-level deterministic Kruger-first expedition helper. No repetition or snowball conclusion is MCP-proven because cadence, cooldown, recovery, removal, and terminal absorption were not sequenced.

## Compare, sweep, simulation, and sequence disposition

No current `hoi4.probability_compare` was run. There was no owner-applied before/after candidate or stable historical fixture for a same-scenario comparison, and the custom probability-auditor route was unavailable. A stale same-source capability receipt must not be treated as a balance comparison.

The earlier rebellion sensitivity/threshold/ranking renders are retained above, but the fresh post-change sweep was not completed. A `probability_sweep` request for `dhrondan_revolt_weight` with four steps, pairwise sensitivity, and rank-reversal search under `DHR_REBELLION_SWEEP_2026_08_25` was stopped before any artifact returned. No sweep conclusion is claimed.

No `probability_simulate` run was made because no uncertain-input distributions and seed were declared. No `probability_sequence` run was made because no complete custom pool and lifecycle manifest was available. No exact normalized probability or live completion claim should be inferred from their absence.

## Recommended owner actions without applying them

1. Make the rebellion low/medium/high predicates explicitly mutually exclusive at arrivals 7/8/9/10, strain 49/50, and Chaos 799/800, then rerun the named tier and pulse scenarios.
2. Preserve and document deterministic Kruger-first expedition priority, or expose a complete Kruger/Mengele candidate pool before changing the dominant score.
3. Add adapter-supported landing receipt, equipment, controlled-state target, pending/cooldown/world-end, and four-factor fixtures before evaluating landing scores.
4. Isolate the `.49` valid-response option pool from invalid-state cleanup or rework the root/option gates so the fallback route is reachable under a declared valid scenario; then rerun `event_option_ai_chance` with friendly, neutral, hostile, and invalid-target actors.
5. Expose Event 019 provider arrays as a declared custom weighted pool or provide an adapter manifest containing every provider, gate, spawn weight, and provider-isolation state.
6. Add a supported special-project adapter or custom selector manifest for `sp_dhrondan_envoy_craft` before making project-selection claims.
7. Rerun the 88-focus DHR pool with route-plan activation/abort, prerequisite/bypass history, crisis choice, and external country state; include inline support-lane factors in the review matrix.
8. Add raid-native probability support or a complete target/formation scenario manifest before evaluating raid factors and outcomes.
9. Declare terminal/world-end state transitions and retry/lock cadence before asking for timing or cumulative route probabilities.
10. After any owner-applied weighted change, rerun the same named scenario IDs through `probability_inspect` and `probability_compare`; do not use this partial handoff as an after-change baseline.

## Simplifications, omissions, and blockers

- No source edits, tuning changes, or fallback mechanics were applied.
- Fresh broad probability inspection stopped at the exact 45-second caller bound; corrected evaluate stopped at the exact 30-second caller bound after two exact schema validation errors.
- Prior MCP refresh/render attempts for dynamic surfaces reached the exact server-native 180-second timeout or returned `PROBABILITY_ANALYSIS_STALE`; their artifacts are retained only with their original source revision and scenario hash.
- Opening/host/referral, full Directorate project-board, current evolution rerun, current Event `.49` rerun, DHR focus/strategy rerun, provider rerun, raids, and terminal probability routes remain incomplete or unresolved for the reasons stated above.
- The exact rebellion tier arithmetic is conditional and revision-bound; it is not a cumulative 90-day campaign probability.
- The expedition and landing findings are score-only/partial; unresolved helper state means empty-fixture eligibility diagnostics must not be generalized to live campaigns.
- No compare, completed sweep, seeded simulation, or complete custom-pool sequence artifact exists for this final audit.
- Structural event, focus, GUI, and Event 019 artifacts are included for context but do not replace the required probability evidence.

This handoff is complete as a read-only evidence record, not as a claim that the Event 016 weighted-logic audit or live balance validation is complete.

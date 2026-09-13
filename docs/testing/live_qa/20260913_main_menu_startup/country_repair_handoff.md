# Event 039 country and reference repair handoff

Date: 2026-09-13

Status: implemented in the shared working tree, source frozen for parent cycle 03, and intentionally uncommitted.

Owner scope: `common/scripted_effects/039_murder_mystery_integration_effects.txt`, `common/scripted_triggers/039_murder_mystery_integration_triggers.txt`, and the parent-authorized exact technology references in `common/scripted_effects/039_murder_mystery_focus_effects.txt`.

The repair addresses the Event 039 loader faults recorded in `docs/testing/live_qa/20260913_main_menu_startup/logs/cycle_02/error.log` at lines 181-184, 187-195, and 252-263, including their repeated startup copies. The cycle 02 log was captured before this source repair and therefore still contains the old diagnostics.

## Changed files

| File | Current locations | Before | After | Contract preserved |
| --- | --- | --- | --- | --- |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | 136, 1410 | `constant:event_chaos_level.one` | `constant:murder_mystery_value.one` | Existing Event 039 level-one value; no new constant category |
| same | 260, 264 | `has_tech = encryption_1`, `has_tech = radar` | `has_tech = basic_encryption`, `has_tech = radio_detection` | Same encryption and radar capability checks using installed technology IDs |
| same | 413, 422, 431, 439, 852, 861, 870, 879 | `create_country_leader` ideology values `democratic`, `fascism`, `communism`, `neutrality` | `liberalism`, `fascism_ideology`, `marxism`, `despotism` | Democratic, fascist, communist, and neutral group branches remain selected by their existing limits and `set_politics` calls |
| same | 1194, 1203, 1211, 1747, 1760, 1772 | `ideology = neutrality` | `ideology = despotism` | Existing neutral route identities and portraits remain unchanged |
| same | 1551-1559 | Runtime `recruit_character` for `murder_mystery_shadow_commander` and `murder_mystery_silent_guard_commander` | Direct character scopes calling `set_nationality = PREV` | Existing character IDs, portraits, corps roles, politics, and carrier transaction remain unchanged |
| `common/scripted_triggers/039_murder_mystery_integration_triggers.txt` | 31-33, 89-91 | Bare `has_country_leader = { ruling_only = yes }` | `any_character = { is_country_leader = yes }` | Generic active-leader existence gate remains generic and country-scoped |
| `common/scripted_effects/039_murder_mystery_focus_effects.txt` | 309 | `set_technology = { motorized = 1 }` | `set_technology = { motorised_infantry = 1 }` | Vehicle-license reward now names the installed motorized infantry technology |
| same | 355 | `engineers = 1` | `tech_engineers = 1` | Conventional adaptation reward now names the installed engineer technology |
| same | 397 | `encryption_1 = 1` | `basic_encryption = 1` | Secure communications reward now names the installed encryption technology |

No leader name, description, portrait, character definition, route branch, country tag, state transfer, party group, AI weight, MTTH, random weight, probability, map, GUI, or event option was changed.

## Source and precedent evidence

Required repository guidance and skills were read before editing: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-debug-playtest/SKILL.md`.

The offline wiki references used were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, and the required core pages for scopes, modifiers, localisation, on actions, event modding, decision modding, idea modding, and AI modding.

The vanilla documentation references used were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

`effects_documentation.md` documents `create_country_leader` as requiring an ideology sub-ideology rather than a regular ideology, and documents `set_nationality` in both COUNTRY and CHARACTER scope with the country form `set_nationality = { target_country = POL character = my_character }` at lines 7397-7417.

The offline Character Modding page lists the modern dual character scope and notes that versions after 1.12.8 do not require prior recruitment at lines 166-169 of `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`. It also records that `set_nationality` can re-add a retired character while retaining all roles at lines 497-506 of `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`. The direct scopes in the runtime repair therefore resolve the globally defined characters first, then use `PREV` for the just-created carrier country. `PREV` is the parent country scope after entering the character scope.

Applying that modern dual-scope rule to an entirely unrecruited character is an inference from the offline documentation rather than a completed live-game observation; the parent’s fresh cycle 03 run must confirm the transfer on the installed engine.

The two records remain defined in `common/characters/039_murder_mystery_characters.txt` at lines 59-75 and 77-93. Their existing army portraits and `corps_commander` role blocks remain intact; no role was regenerated and no character was invented.

Vanilla technology IDs were checked in the installed game files: `motorised_infantry` is top-level at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/technologies/infantry.txt:1975`, `tech_engineers` is top-level at `.../common/technologies/support.txt:98`, `radio_detection` is top-level at `.../common/technologies/electronic_mechanical_engineering.txt:218`, and `basic_encryption` is top-level at `.../common/technologies/electronic_mechanical_engineering.txt:728`. The old `motorized` token is a nested sub-unit modifier at `infantry.txt:2360`, while `encryption_1` and the old `radar` token are not the top-level technology IDs used by `set_technology` or `has_tech`.

The installed and mod ideology definitions were checked in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ideologies/00_ideologies.txt` and `common/ideologies/00_ideologies.txt`. The replacement subtypes are valid members of the intended groups: `liberalism` democratic, `fascism_ideology` fascist, `marxism` communist, and `despotism` neutrality.

## Backup and diff isolation

The two integration originals were copied before the first edit to:

* `docs/testing/live_qa/20260913_main_menu_startup/baseline/country/common/scripted_effects/039_murder_mystery_integration_effects.txt` with SHA-256 `8794AB38F3DE28DE0261EE61B73C3BA693953FE2A9E34A90EF028A592E1C0E58`.
* `docs/testing/live_qa/20260913_main_menu_startup/baseline/country/common/scripted_triggers/039_murder_mystery_integration_triggers.txt` with SHA-256 `B22B9346977EE0EFD41D832AC862DCA6312094B96DBEF78D2589776C1287A52F`.

The focus effects file was untracked in the recorded baseline and had no source snapshot under `baseline/`; its country backup was created at `docs/testing/live_qa/20260913_main_menu_startup/baseline/country/common/scripted_effects/039_murder_mystery_focus_effects.txt` by reversing the three unique substitutions before recording the handoff. The reconstructed backup SHA-256 is `A891DB35C6981FBAD0228DFE838AC0AE1C22BE3F58BA7F28522018CC57199F80`; this limitation is recorded rather than presented as a byte-captured original.

The resulting diffs contain only the listed substitutions and the two direct character-scope blocks. Current source SHA-256 values are `D895464294D34D943FBAF7AB66AF271AECD1EEC9AC8846DCD5DC73DEF77A640F` for integration effects, `6FE66C3D34408C20D8A2049CE40348DF96DE9A898CAEDCF60055CEF062E3A7EB` for integration triggers, and `D1002B314C9D92EEE634F2608E75672221BE554FAC91FC57DABB31BB448AC483` for focus effects.

## MCP evidence and validation limits

The supported read-only Event MCP inspection was run before the final runtime and constant substitutions for selector `{ kind = event eventId = chaosx.nr39.1 }` with `mode = lint`, `expandHelpers = yes`, and both directions. It returned `EVENT_INSPECTED_PARTIAL`, `analysisMode = focused`, `helpers = 0`, `blockingDiagnostics = 0`, and the source inventory truncation diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5dc779cc3b2c1136be0a6df16e4128f855be3b6f6ab14036c27a12a8965236c/eb9f604aaaf55ecabbd7dad2262f052b7d046e9bf15a2d20c9bc65875f444e42/event-lint-b1e9c2d116b0.json`.

The corresponding read-only Event render returned `EVENT_RENDERED_PARTIAL` with the focused graph and the same source-inventory truncation diagnostic. Artifact manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83ccd44137e60ccdbf04d23338ee8854a7aeb331976df72ac92b1466f2fd1785/dcb2917d783c2e97a984d6ef25537e387dbe99adb7fb8c21228bbfd235290c3e/event-overview-4ca537613a23-manifest.json`.

The Event `state_flow` route initially returned `INTERNAL_ERROR` with `Unexpected internal error`, and the final Event inspect, render, and compare calls returned the exact MCP blocker `Transport closed`. The focused artifacts therefore provide source and graph evidence, but not a complete post-edit helper/lifecycle proof; the parent’s cycle 03 launch remains the authoritative fresh-loader check.

The read-only focus routes were also run for `murder_mystery_assassin_focus_tree` in `common/national_focus/039_murder_mystery_assassin_focus.txt`. `hoi4.focus_inspect` returned `FOCUS_INSPECTED`, passed its blocking diagnostic check, and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37d0103c9dae92539880dedebd381833d403ea317361836883015eafdf647a73/7f2af6391cd102ff869bbe43ff106c558a5036d9c5e4a5ec14fea5a4e311a17c/focus-inspect.414a9e20c66df09a.json`. `hoi4.focus_render` returned `FOCUS_RENDERED` and passed its blocking diagnostic check; its HTML artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4d6e164adb177a580609d475a84552315923f6f3e1ea1a1279142a8c4fc28f1/21e5cabfca31370b4c80493a1f04ccee62fe5ea456655ef5abd5217cbd6673bb/murder_mystery_assassin_focus_tree.focus.html`. The focus service reported existing layout-spacing warnings and one unrelated vanilla localisation warning; no focus-tree source was changed.

The required read-only technology inspection and render routes were attempted for all four installed IDs (`motorised_infantry`, `tech_engineers`, `basic_encryption`, and `radio_detection`) and a sequential retry was attempted for `motorised_infantry`; each returned `tool call failed ... Transport closed`. Source and installed vanilla documentation checks are included above, but they do not substitute for unavailable post-edit technology MCP evidence. No standalone Technology Tree Viewer route is exposed by `hoi4-agent-tools`; this is recorded as a package gap rather than invented evidence.

No probability audit was run because the patch changes no AI weight, strategy factor, MTTH, random list, option chance, or weighted target. No map, GUI, technology-tree layout, event option, or focus-tree source was edited.

## Country package coverage for this repair

| Surface | Result |
| --- | --- |
| Carrier tags and country references | Unchanged; no stale tag reference was part of the reported Event 039 faults |
| State ownership, capital, cores, claims, supply, and map | Unchanged; outside this bounded loader repair |
| Politics and ideology groups | Preserved; only invalid `create_country_leader` subtype tokens were replaced |
| Existing leaders and portraits | Preserved; names, descriptions, portrait sprites, and route identities were not changed |
| Runtime commanders | Existing IDs `murder_mystery_shadow_commander` and `murder_mystery_silent_guard_commander` are attached through direct character scope and `set_nationality`; pre-defined corps roles remain the source of skills and traits |
| Focus and technology rewards | Three exact installed technology IDs repaired; focus order, prerequisites, effects, and tree layout remain unchanged |
| AI, probability, decisions, localisation, flags, and assets | Unchanged |

## Parent validation handoff

The parent should run cycle 03 with the source as currently frozen and confirm that the fresh startup log no longer contains the old Event 039 ideology, bare leader, missing constant, invalid technology, or runtime `recruit_character` diagnostics. Live validation should also confirm that the newly created Assassin State exposes both existing commander records with their intended portraits and roles while retaining the existing neutral politics setup.

If the live engine reports that direct character scope cannot attach an unrecruited record, retain the exact runtime diagnostic and revisit only this two-character transfer block; no fake character, portrait, role, fallback leader, or deletion was introduced.

## Simplifications and blockers

No gameplay simplification or identity fallback was used. The only implementation limitations are the reconstructed focus backup noted above and the MCP transport closures that prevent complete post-edit Event and technology helper evidence; parent cycle 03 is required for fresh runtime confirmation. 

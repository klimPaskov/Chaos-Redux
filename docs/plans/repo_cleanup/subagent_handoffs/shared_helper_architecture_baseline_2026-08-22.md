# Shared-helper architecture baseline

Date: 2026-08-22

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`

Scope: Shared scripted infrastructure and helper call sites used by Events 1-20, with Events 21+ inspected only where they consume shared infrastructure.

Mode: Read-only baseline audit.

## Executive summary

No gameplay, GUI, asset, localisation, spreadsheet, or source helper file was edited in this pass.

The strongest conclusion is that Chaos Redux already has useful shared APIs for world-threat aggregation, state population loss, stockpile debits, natural-disaster dispatch, and technology-union transfer; cleanup should preserve and reuse these APIs rather than create parallel event-local versions.

The clearest documentation defect is ownership drift in `common/scripted_effects/chaosx_dynamic_effects.md`: its table of contents names the 17 helpers declared in `chaosx_dynamic_effects.txt`, but later sections also document APIs declared in Event 006, Event 016, the clone system, alien infantry, Mengele bridge, and Event 019 provider files.

The clearest proof-gated cleanup candidates are the uncalled dynamic helpers `modify_value_based_on_chaos_tier` and `damage_buildings_in_random_states`, plus the commented `clear_special_chaos_country_civilian_effects` hook; all three require dynamic/meta-effect and generated-reference searches before any removal.

The event log scripted GUI repeats tab reset, detail-close, and view-rebuild logic, but this baseline recommends no accepted GUI patch. A future functional binding cleanup may be considered only with a bounded MCP before/after inspection and without changing `interface/*.gui`, GUI assets, or visual layout and coordinates.

World-threat state has a central `refresh_world_threat_state` API and should remain centralized. The Event 005 Soviet-collapse opening preview intentionally or historically counts a different source set from the runtime aggregate, so a registry migration must be deferred until preview semantics are proven equivalent.

Global event targets with no local clear are not automatically stale. Death, Fury, Holy Realm, Mengele, Zombie Outbreak, and Utopia targets are used as persistent history, achievement, localisation, scenario, or terminal-state pointers; deletion or automatic clearing needs lifecycle proof from saves, `has_event_target`, localisation, dynamic meta dispatch, and terminal flows.

The main broad migrations to defer are legacy event-category ID normalization, Event 006 country-registry/collection redesign, Event 019 provider dispatch redesign, global event-target lifecycle rewrites, and any interface layout change.

## Constraints and required reading

The following repository instructions and task files were read in full before inspection: `AGENTS.md`, `docs/plans/repo_cleanup/chaos_redux_repo_cleanup_master_prompt.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline wiki snapshot pages were read: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, `Scripted GUI Modding - Hearts of Iron 4 Wiki.md`, and `Interface Modding - Hearts of Iron 4 Wiki.md`.

The required vanilla documentation was read from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`.

The vanilla script-constant schema and examples were also read from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md`.

GUI and scripted-GUI source remained read-only. In particular, this report does not authorize or recommend coordinate, size, layout, asset, or `.gui` edits.

## Evidence and inspection limits

The installed HOI4 MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

Read-only `hoi4.event_inspect` lint inspections were run for the roots `chaosx.nr1.1` through `chaosx.nr20.1`, with downstream direction, `expandHelpers = false`, bounded depth and node limits, and no source writes.

The Event 1-14 artifacts used the workspace revision `bc0062fc8506`; Event 15 used the file-scan artifact below; Events 16-18 used revision `bc0062fc8506`; Events 19-20 used the newer revision `0d89fc74a70e`.

The Event 1-14 and 16-18 results were `EVENT_INSPECTED_PARTIAL` with `MCP_INLINE_FILES_TRUNCATED` because the workspace contained 366 files and only 64 inline files were returned. Their validation fields were false because helper and lifecycle projections were deferred, so they are structural evidence, not runtime proof.

The exact event inspection artifacts are:

| Surface | Artifact |
| --- | --- |
| Event 1 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0620d74e23956aa5e36d8f8b3537da1c2385b5588905e37d89bb4ed01f20206/0aa0d45150c5034e6fc283271a296649b8b84e43a0fa78ebb0ed3ba8ce036077/event-lint-bc0062fc8506.json` |
| Event 2 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6ef89df54944141945d507976411220a268041062d6f1e1bcf13ab8f9bc67e4/dc116911317a575b308a817eebf56e87bdeabb63a61a2fcb3375de24513ca362/event-lint-bc0062fc8506.json` |
| Event 3 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07af47954b12b57f728687e59be1c889df119735101c83aed3c42a1b96c40647/8573157c5e52529ae02f8016d808e329a32172447cbaf0bf82f6044ec13a5f28/event-lint-bc0062fc8506.json` |
| Event 4 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0cc641870e59c0aafe09160b07c69dce4b4f38b6dad3e8aebab1664e25b16a9/173f6f6afee74becf2a60ec9140e719457c5b4188935ad17c4b1b812bb6ad93e/event-lint-bc0062fc8506.json` |
| Event 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9a46bbea4fd49426abbc2b4b4a83b3ac3a54bae36fbf9d7fbd4fc64aada1eff/eb2ebf0aeb8b8ac134828960ee235475504bd17e160367b23205e6b13e98256c/event-lint-bc0062fc8506.json` |
| Event 6 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/440bd3d04a1e0d7617e63ae389692acf1838289aba2ef4461168a7b80d44d5c9/89348b9e318930689c96a75e0bfef0d2e5db9a22d94c3640ec6cbb6b60a2ff1c/event-lint-bc0062fc8506.json` |
| Event 7 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3adb97c2b5a9f3a84e743b67b78ae0259df3e83a7d95c2827be1903cb12ad748/aac835282c1bcffff06ad4d46ff563b1a3613626d9c42f176c3b98e86d0a5fd7/event-lint-bc0062fc8506.json` |
| Event 8 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/187fd81b3cef5582ab56ff1a48fd401736f494c042b838186ec13744a284c25c/e39083c57ec7a78c99d15691bdc95e8a4449019eac71055ecd909bcc8c39caf6/event-lint-bc0062fc8506.json` |
| Event 9 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8fc29b7126a29a623fc457ecd9d0e46897dcb84b04c74088d79872358c5bb223/a25fcd83bcab45e657a7d8053854d8fca863f18d6f35b511c36a3d0d0c9c1cac/event-lint-bc0062fc8506.json` |
| Event 10 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2b1641962fe1e9b204ca0f7144c6bd8f13a2b7e6d7580835ee850d38d0f2f09/5b905230eae7ae0853141636bb11c949f24f3dd1064c0b5ded3a5cad3af08df3/event-lint-bc0062fc8506.json` |
| Event 11 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bae5d5c83fa37a371f8481c7cc4033b525b52617a7d58ce1c3ef520b98569b8a/53bb1b5fe782bf4e4152a6b1dd7eda1cb7bd8e82dcadfdafb1dad47d86bc765b/event-lint-bc0062fc8506.json` |
| Event 12 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dc11275366a8cf9022abd4d22df9f6a950e463518beee05ba03e554c477bb92/4af4befaaccb8d00c7882f5db3b4fbd543f6b3c6546fb6146d35ab5f217064aa/event-lint-bc0062fc8506.json` |
| Event 13 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/344e1a8181ffb785989c7c53d5b094f7dd1ab7edb8011cce9fb5b11d40555178/faf80df3c3cc539129ef30f0b2e5a01f7cd62a6dcda9e8fcf9d850948603bffe/event-lint-bc0062fc8506.json` |
| Event 14 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dce022bd069172c9ff4f09c57f5077fecc961c828ab69a5ec56c57ed29882933/e0862ebad5d5dc8c1d6b1bec6052e1eea49fcb9bf7f71dba2a200c203f33f4bd/event-lint-bc0062fc8506.json` |
| Event 15 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ec388ad91a29d35397f08c4d3b2c299acc9c18f5e58324f659a0e16721c82ec/f7a452ed5f7a52f0e7a5d8a9aa4799b8fc3feff442d1f4ae6f7f064393ae0461/event-scan-bc0062fc8506.json` |
| Event 16 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0db41a23a5c11e679cd558f573c9464fc1885d3d7fe3a1512d9e56ba3084b3ff/ca152d27a534828e8c129c5078b0b3ec2b0a349c69579e7919e1d6ee9d846347/event-lint-bc0062fc8506.json` |
| Event 17 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c13bdf3e5f34121d554877171266e874cdd38144373896b0ab558b99c5a52abd/17d0aa9fcc3eea93ca44128eb486be951248f7d1dc19a676258a6308503e9b3d/event-lint-bc0062fc8506.json` |
| Event 18 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3305a88792b56c8f0349a8a7545c65d2c0418a69d926ee72015f4ad585c7239e/0e5279b11fdd6b2dd33fc889348f82b88b0f683d1980462efcfc5b08483d079d/event-lint-bc0062fc8506.json` |
| Event 19 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc8e7c1ad8d2d0009b471248e13b8a491a42cc0e8d51fde3d61adb3a60a4643e/01cc17d7d05d15ce372a3614f5faeb981d0166e77edde1ef7d672cef2fb36f85/event-lint-0d89fc74a70e.json` |
| Event 20 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73fca50308ab4121784a3b9fbb924095156449c8033caf568f64467d2849c03b/b341e4796ca2a55511e9ddd86aed5e9d575da277397ce13c018e410f4aca7820/event-lint-0d89fc74a70e.json` |

The shared event-log GUI was inspected read-only with `hoi4.gui_inspect` for `events_log_popup_window` under scenario `event_log_shared_architecture_baseline`.

The GUI artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/922e791efa3e7f79b89c8554be19b5da743f0abcb4dcbe4dcbf285f8a420b805/453308075164395336e7c4c3de561b72fba8007710d9826e1f0e617edc436376/gui-inspect.1391d8530b419297.json`.

The GUI result inspected 16 window elements and modelled 156 items, with 2 approximated items, 35 ignored items, 1 missing item, 16 unsupported items, and 1 unresolved item. Aggregate graph diagnostics were truncated at 2,000 entries and reported six visible overlaps, so no layout or coordinate conclusion is made here.

The required probability inspection was started before judging weighted helpers with `hoi4.probability_inspect`, adapter `custom_weighted_pool`, and source `common/scripted_effects/chaosx_logic_effects.txt`.

The probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3a7bed6e8e3d5e23416794b68e928d4a3c14aaecba41d8618761acbcdfc7e8e/d28276c76aee90b542dc05f97871aa4c06fc2f676a36f690d1d545757b012bf2/probability-inspect-6d5d6adb4e5b.json`.

That source inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `47782e8328d107c3cd0f6f80e6c439907a8062b3a4f38b17cd83b85e68e0a8c8`, source hash `6d5d6adb4e5b`, zero custom-pool candidates, and no unresolved required inputs. No weighted patch is proposed in this baseline, so no probability compare or scenario balance claim is made; the custom `chaosx_ai_probability_auditor` route was not available as a callable tool in this runtime.

## Shared helper inventory

### `chaosx_dynamic_effects`

`common/scripted_effects/chaosx_dynamic_effects.txt` contains 773 lines and its matching `common/scripted_effects/chaosx_dynamic_effects.md` contains 563 lines.

The source declarations are listed below with the observed disposition.

| Helper | Observed call sites and scope | Baseline disposition |
| --- | --- | --- |
| `modify_value_based_on_chaos_tier` | Declaration at `chaosx_dynamic_effects.txt:17`; no direct active callers found. | Orphan/template candidate; preserve until dynamic and meta-effect searches prove no generated caller. |
| `calculate_economy_scaled_factory_grant` | Event 5 at `common/scripted_effects/005_soviet_collapse_effects.txt:8861,8924`. | High-confidence reuse; keep as the Event 5 economy-grant API. |
| `damage_buildings_in_random_states` | Declaration at `chaosx_dynamic_effects.txt:87`; no direct active callers found. | Proof-gated orphan candidate; do not delete until generated references and design notes are checked. |
| `get_random_sea_region` | Event 88 at `events/088_mines.txt:31`, which is outside the primary scope. | Retain because an active 21+ caller exists; the duplicate region ID 110 is a weight choice and must not be normalized without map/weight proof. |
| `clear_special_chaos_country_civilian_effects` | Only a commented call appears at `common/on_actions/chaosx_on_actions.txt:57`. | Reserved or unwired cleanup hook; require ownership confirmation and lifecycle proof before removal. |
| `refresh_world_threat_state` | Active calls include Event 5 `005_soviet_collapse_effects.txt:2658`, Event 3 `003_holy_realm_effects.txt:1599`, Event 2 `002_zombie_outbreak_effects.txt:1135,1933`, Event 14 `014_cannibalism_effects.txt:2072,2574`, Event 7 `007_fury_effects.txt:1139,1359`, Event 10 `010_death_effects.txt:1108`, Event 16 `016_brilliant_scientist_super_event_effects.txt:393,466,516,687,709`, Event 18 `018_resources_found_cave_effects.txt:337,2250,2477`, Event 20 `020_black_plague_scenario_effects.txt:666`, and shared/21+ consumers `germany_mengele_effects.txt:300,1584`. | High-confidence central API; reuse and do not split. |
| `union_compatible_researched_technologies_from_donor` | Event 14 at `common/scripted_effects/014_cannibalism_effects.txt:12401,12577,18595` with donor target `event_target:technology_union_donor.researched_techs`. | High-confidence reuse; retain exclusions for flexible/streamlined and concentrated/dispersed branch conflicts. |
| `call_natural_disaster` | Event 13 at `events/013_natural_disasters.txt:60`; shared calls at `012_africa_action_effects.txt:8209`, `012_africa_promoted_tiera_effects.txt:526`, `013_natural_disasters_effects.txt:8525`, `chaosx_event_cluster_effects.txt:1225`, and `chaosx_triggerable_scenarios_effects.txt:1115`; Event 99 uses it at `events/099_desert_storm.txt:36`. | High-confidence public Event 013 API; keep dispatch centralized. |
| `apply_state_population_loss_without_recruitable_manpower_gain` | Internal call at `chaosx_dynamic_effects.txt:719`, shared chaos-meter call at `chaos_meter_effects.txt:2944`, and Fallout call at `fallout_consolidated_effects.txt:40919`. | High-confidence reuse; keep the explicit manpower semantic. |
| `apply_exact_state_civilian_population_loss` | 204 total references; in-scope owners include `014_cannibalism_effects.txt:4102`, `015_utopia_manifesto_decision_effects.txt:915`, `018_resources_found_incident_effects.txt:48`, `020_black_plague_effects.txt:1427`, `020_black_plague_evolution_effects.txt:850`, and `020_black_plague_scenario_effects.txt:314`. | High-confidence shared API; do not replace with event-local population arithmetic. |
| `remove_support_equipment_from_stockpile` | Event 20 at `020_black_plague_response_decisions.txt:721`, `020_black_plague_shared_response_decisions.txt:36`, `020_black_plague_shared_response_effects.txt:108,705`, `020_black_plague_terminal_response_effects.txt:15,48`, and `020_black_plague_weaponization_effects.txt:112,227,256,303`; also 21+ callers. | High-confidence reuse; existing payment contracts already centralize most shared costs. |
| `remove_motorized_equipment_from_stockpile` | Event 20 at response decision `:723`, shared decision `:38`, shared effects `:110,707`, terminal effects `:17,50`, and weaponization effects `:114,229,235`; also 21+ callers. | High-confidence reuse. |
| `remove_convoys_from_stockpile` | Event 20 response decision `:725`. | High-confidence reuse; keep the resource-specific helper. |
| `remove_trains_from_stockpile` | Event 20 shared effects `:123`, terminal effects `:21,54`. | High-confidence reuse. |
| `remove_plague_bombs_from_stockpile` | Event 20 weaponization effects `:254,284,301`. | High-confidence reuse. |
| `remove_infantry_equipment_from_stockpile` | Event 20 terminal effects `:19,52`. | High-confidence reuse. |
| `remove_fuel_from_stockpile` | Event 20 response decision `:728`, shared decision `:40`, shared effects `:112,709`, terminal effects `:23,56`, and weaponization effects `:120,235,262,309`. | High-confidence reuse. |

`modify_value_based_on_chaos_tier` currently encodes tier values 0-3 and a greater-than-3 branch with factors 0-4, while its documented inputs are `base_value` and `add_value` and its output is `modified_value`. The hardcoded ladder is a tuning candidate only if the helper remains an API; no active call justifies a constants migration in this baseline.

`damage_buildings_in_random_states` defaults include a starting controlled-state count of 1, a fallback target percentage of 0.1, a damage modifier of 0.25, and three buildings per state. These are magic-number candidates in principle, but there is no active caller, so centralizing them now would give a dead API a larger surface.

`get_random_sea_region` contains a literal sea-region selection list with duplicate 110. The duplicate is likely a deliberate probability weight, so normalizing or converting it to a collection is deferred.

### `chaosx_dynamic_triggers`

`common/scripted_triggers/chaosx_dynamic_triggers.txt` contains 162 lines and `common/scripted_triggers/chaosx_dynamic_triggers.md` contains 102 lines.

`is_special_chaos_country` is the active classifier for ZZZ, zombies, REV, communist rebels, ZIN, Holy Realm, Mengele, Fury, Death, DHO, resources/cannibalism, Event 19, Event 16, and Event 20 flags.

`is_actual_nonhuman_country` covers zombies, Wendigo, ZIN, Death/DHO, resources/cannibalism, Event 19, Event 16, and Event 20; `uses_normal_civilian_systems` is its inverse classifier.

`is_desert_state` uses a map-sensitive literal state ID list from `chaosx_dynamic_triggers.txt:84-160`. The list is documented but should not be moved or generalized without map inspection and caller comparison.

These three triggers are active classification APIs, not stale duplicates.

### Ownership drift in the dynamic-effects documentation

The matching markdown documents the following APIs that are not declared in `chaosx_dynamic_effects.txt`:

| Documented API family | Actual source of declarations |
| --- | --- |
| Event 006 ledger helpers `independence_wave_change_nav_compact_values` and `independence_wave_change_glc_compact_values` | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` |
| Event 016 custom technology API `chaosx_grant_custom_operational_technology`, `chaosx_grant_custom_technology_upgrade`, and `chaosx_grant_random_custom_operational_technology` | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` |
| Clone APIs `clone_ensure_infantry_template`, `clone_grant_infantry_access`, `clone_select_kruger_refinement`, `clone_select_kruger_weaponization`, `clone_select_mengele_refinement`, and `clone_refresh_reserve_manpower` | `common/scripted_effects/clone_system_effects.txt` |
| Alien API | `common/scripted_effects/016_alien_infantry_api_effects.txt` and its trigger file |
| Mengele bridge `brilliant_scientist_record_mengele_project_prototype` | `common/scripted_effects/016_mengele_project_bridge_effects.txt` |
| Event 019 provider contract `chaos_unit_family_provider_[ID]_event19_*` | Concrete providers in `019_infantry_spawn_unit_registry_effects.txt`, `020_black_plague_effects.txt`, `cbrn_doctrine_effects.txt`, `018_resources_found_cave_effects.txt`, and `016_brilliant_scientist_project_force_event19_effects.txt` |
| Event 006 AI reserve contract | Event 006 subsystem files, not the dynamic-effects source file |

This is a documentation/source-of-truth mismatch, not proof that those helpers are stale. The safe documentation patch is to split the API index into declared dynamic helpers and subsystem-owned contracts, with links to each authoritative file.

The Event 019 provider dispatch is intentionally dynamic: `common/scripted_effects/019_infantry_spawn_core_effects.txt:193` and related derivative package paths build `chaos_unit_family_provider_[PROVIDER]_event19_*` through `meta_effect`. A generic static helper extraction would obscure provider ownership and is deferred.

## Shared subsystem flows

### Event registration and logic

`common/scripted_effects/chaosx_logic_effects.txt` initializes fired-event, event-history, major-event, repeatable-event, evolution, event-detail, cluster, crisis-rescue, and world-end registries in `initialize_event_system` at approximately lines 27-153.

The same initializer calls `initialize_event_categories`, `initialize_all_events_array`, `initialize_event_chaos_level_registry`, `initialize_world_end_scenario_registry`, `initialize_default_disabled_events_for_rework_queue`, `count_total_events_plus_one`, `initialize_event_weights`, `calculate_dynamic_major_weight_gain`, `initialize_crisis_rescue_registry`, and `initialize_event_cluster_system`.

`initialize_event_categories` still mixes hardcoded legacy IDs for major, fire-once, and repeatable categories with newer `constant:` IDs for Africa, cannibalism, utopia, brilliant scientist, Doctor Wu, and Black Plague. This is a real ownership inconsistency, but normalizing all IDs requires proving category membership, aliases, and historical saves; defer the broad registry migration.

Event 6 has both `add_namespace = chaosx.nr6` and `add_namespace = chaosx.nr006` in `events/006_independence_wave.txt:5-6`. This alias is a migration hazard and should not be renamed as part of helper cleanup without checking all event, localisation, log, and dynamic references.

### Event log, history, evolution, details, and cluster flow

`common/scripted_effects/chaosx_events_log_effects.txt` is the central history/evolution/event-detail/cluster persistence layer at 4,767 lines.

`common/scripted_effects/chaosx_event_cluster_effects.txt` is the cluster registry and lifecycle layer at 2,692 lines, with file-scoped `@` cooldown, sentinel, and slot values near lines 15-27.

`common/scripted_guis/chaosx_scripted_gui_events_log.txt` owns the functional event-log shell and details routing. The `events_log_popup_shell_gui` declaration spans approximately lines 1-244.

The scripted-GUI shell repeats the same clear-tab, close-details, and selected-view rebuild sequence for history, evolutions, events, and clusters around lines 40-157. This is a functional duplication candidate only, not a visual/layout patch.

The history dynamic list around lines 491-507 reads global view arrays, copies selected event/date/actor values, and routes to cluster or event details. This is shared framework behavior and should not be duplicated in Event 1-20 files.

`interface/chaosx_events_log_popup.gui` is the visual consumer with tabs, dynamic lists, details windows, world-end scenario details, and cluster details. It remained untouched and is excluded from all accepted patch recommendations.

### Settings and manual event controls

`common/scripted_effects/chaosx_settings_effects.txt` is a 4,899-line shared settings/control surface. The events skill assigns settings and manual event controls to this file, while event log persistence remains in `chaosx_events_log_effects.txt`.

No safe broad extraction was identified from source-only inspection because settings, history, and event firing carry different persistence and UI contracts.

### Named subsystem API anchors

The following exact helper names are the shared subsystem anchors to reuse or trace before proposing new helpers.

| Subsystem | Existing helper names and source files | Baseline disposition |
| --- | --- | --- |
| Event log/history/details | `record_events_log_system_history_entry`, `record_events_log_history_entry`, `record_events_log_evolution_entry`, `record_events_log_cluster_entry`, `refresh_events_log_system_history_views`, `events_log_rebuild_event_detail_world_end_scenarios`, `events_log_open_selected_event_detail`, `events_log_close_history_details_view`, and `events_log_close_all_event_details_entries` in `common/scripted_effects/chaosx_events_log_effects.txt`. | Central framework API; reuse before adding event-local history or detail persistence. |
| Event clusters | `initialize_event_cluster_system`, `initialize_event_cluster_definitions`, `can_event_cluster_fire`, `prepare_event_cluster_firing`, `build_event_cluster_firing_order`, `event_cluster_schedule_next_pending_member`, `event_cluster_fire_next_pending_member`, `record_events_log_cluster_entry`, `events_log_close_cluster_details_view`, and `trigger_selected_event_cluster` in `common/scripted_effects/chaosx_event_cluster_effects.txt`. | Central cluster lifecycle and selection API; broad refactor deferred. |
| Triggerable scenarios | `initialize_triggerable_scenarios_settings`, `triggerable_scenarios_initialize_registry`, `triggerable_scenarios_rebuild_view`, `trigger_selected_chaosx_scenario`, `trigger_disaster_barrage_scenario`, and scenario-specific selectors in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`. | Dynamic scenario registry; do not replace with hardcoded scenario buttons. |
| Settings/manual event control | `clear_all_menu_flags`, `initialize_settings_system`, `initialize_global_settings_system`, `reset_all_settings`, `apply_event_id_manual_entry`, and `trigger_selected_event` in `common/scripted_effects/chaosx_settings_effects.txt`. | Shared settings and manual-control API; keep separate from event-log persistence. |
| Chaos meter | `initialize_chaos_meter_system`, `refresh_chaos_meter_deaths_view_if_open`, `record_chaos_meter_deaths_log_entry`, `chaos_meter_register_deaths`, and `chaos_meter_apply_state_civilian_pop_loss_from_deaths_change` in `common/scripted_effects/chaos_meter_effects.txt`. | Shared meter and deaths-view API; reuse population-loss helper at the boundary. |
| Black Plague shared response | `black_plague_begin_shared_state_action`, `black_plague_finish_shared_state_action`, `black_plague_cancel_shared_state_action`, and `black_plague_clear_shared_state_flags` in `common/scripted_effects/020_black_plague_shared_response_effects.txt`; `black_plague_pay_response_cost` in `common/scripted_effects/020_black_plague_response_effects.txt`; and `black_plague_weaponization_pay_approach_cost` in `common/scripted_effects/020_black_plague_weaponization_effects.txt`. | Existing payment and lifecycle contracts; no new generic payment helper recommended. |
| Black Plague terminal response | `black_plague_start_human_last_response_hold`, `black_plague_start_human_last_response_refuge`, `black_plague_process_human_last_response_missions`, `black_plague_clear_human_last_response_runtime`, and the corresponding resolve/timeout/cancel helpers in `common/scripted_effects/020_black_plague_terminal_response_effects.txt`. | Owner-local lifecycle API with distinct Hold/Refuge costs; do not merge blindly. |

### Triggerable scenarios

`common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` is a 2,541-line dynamic scenario registry. Its initializer sets selected scenario, intensity, and type defaults, calls `triggerable_scenarios_initialize_registry`, rebuilds the view, and registers the Black Plague commit provider.

The registry includes Zombies, Mengele clones, Soviet collapse, Fury, Death, disaster barrage, Independence Wave, coalition, cannibalism, Black Plague, infantry spawn, and Fallout scenarios using shared constants.

This dynamic list is the correct reuse point for scenario selection; no Event 1-20 hardcoded one-button scenario migration is recommended.

### Chaos meter and condemnation flows

`common/scripted_effects/chaos_meter_effects.txt` is a 6,745-line shared meter and escalation flow. `common/scripted_effects/condemnation_response_effects.txt` and `common/scripted_effects/condemnation_sanctions_effects.txt` provide response and sanction helper layers.

The meter already reuses `apply_state_population_loss_without_recruitable_manpower_gain`. Zero, one, and negative-one values are mostly lifecycle sentinels and are already represented in `chaos_meter_constants.txt`; they should not be mechanically converted to tuning constants.

### World-threat aggregate

`refresh_world_threat_state` is the central aggregate API. It reads source flags for zombies, Holy Realm, Mengele, Fury, Death, cannibalism, Black Plague, resources-found caves, and brilliant scientist, then sets or clears the global `world_in_threat` flag and updates `global.world_threat_source_count`.

`common/scripted_triggers/chaosx_world_threat_triggers.txt` has public wrappers for zombies, Holy Realm, Mengele, Fury, Death, cannibalism, resources-found caves, and brilliant scientist, but no Black Plague wrapper.

`docs/systems/world_threat_mechanic.md:122` explicitly says Black Plague has no public wrapper because no caller exists, while `chaosx_dynamic_effects.md` lists `has_world_threat_source_black_plague`. This mismatch should be documented clearly before any trigger API change.

`docs/systems/world_threat_mechanic.md:81` and `:154` contain the stale path `common/scripted_effects/014_cannibalism_core_effects.txt`; the source file is `common/scripted_effects/014_cannibalism_effects.txt`. Correcting those documentation paths is a high-confidence documentation-only patch.

Event 5 has a separate opening preview at `common/scripted_effects/005_soviet_collapse_effects.txt:1564-1585`, which counts only zombies, Holy Realm, Mengele, Fury, Death, cannibalism, and resources-found-caves source flags. The runtime aggregate call is at `:2656-2658`. Because preview and runtime may intentionally use different policy, do not merge them without scenario evidence.

### Cleanup helpers and lifecycle

`clear_special_chaos_country_civilian_effects` is declared but only referenced by a commented on-action call. This is the only clear cleanup-hook orphan found in the dynamic layer; it needs ownership and intended trigger proof before deletion.

The Event 16 flow demonstrates a bounded target cleanup pattern: `events/016_brilliant_scientist_super_events.txt:50-53` checks and clears `brilliant_scientist_super_event_actor`, while `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:77-82` clears and saves it at the lifecycle boundary.

Event 20 payment paths already use `black_plague_pay_response_cost` and `black_plague_weaponization_pay_approach_cost` rather than duplicating a generic payment API. Terminal response effects repeat five resource debits for Hold and Refuge, but the constants and side effects differ; a generic provider bundle is not a safe baseline extraction.

## Event-target lifecycle audit

The filtered repository inventory found approximately 307 `save_global_event_target_as` calls, 1,832 `save_event_target_as` calls, 405 `clear_global_event_target` calls, no `clear_global_event_targets` calls, 1,981 `has_event_target` calls, and 7,502 `event_target` references in the broad shared/in-scope search set.

The following names were saved without a corresponding clear in that filtered set. A no-clear result is a proof target, not a deletion recommendation.

| Target | Evidence and disposition |
| --- | --- |
| `death_black_oath_herald` | Saved only at `common/scripted_effects/010_death_effects.txt:1677` with no direct check found. It is associated with the Death Herald flow; inspect saves, scripted localisation, meta effects, and terminal history before calling it stale. |
| `death_origin_state` | Saved at `common/scripted_effects/010_death_effects.txt:534,541`; read by `common/scripted_localisation/010_death_scripted_localisation.txt:9` through `has_event_target`. Persistent origin-state presentation is plausible; retain pending proof. |
| `fury_pact_leader` | Saved at `common/scripted_effects/007_fury_effects.txt:2328` and used at `:2333,2335`. It likely persists terminal pact identity; do not clear automatically. |
| `fury_world_end_leader` | Saved at `common/scripted_effects/007_fury_effects.txt:1360`, used at `:1431,1437`, and documented by `docs/events/007_fury/overview.md:140`. Retain as persistent terminal actor. |
| `mengele_clone_army_scenario_country` | Saved with a global target and flag at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:2192-2195`. The flag is used by focus, division, decision, and trigger files; direct target checks were not found in the filtered set. Prove registry semantics before cleanup. |
| `outbreak_state` | Saved by Event 2 at `events/002_zombie_outbreak.txt:41,198`, by `common/scripted_effects/002_zombie_outbreak_effects.txt:1707-1708`, and by triggerable scenarios around `:1373,1485`; checks and state uses exist in Event 2 files. This is an intentional persistent scenario pointer. |
| `utopia_manifesto_latest_actor` | Saved at `common/scripted_effects/015_utopia_manifesto_effects.txt:153,163,173`, consumed by event-log default actor logic at `common/scripted_effects/chaosx_events_log_effects.txt:275-278`, and described as historical log state near `015_utopia_manifesto_effects.txt:8032`. Retain. |
| `holy_realm_lotus_bridge_actor` and `holy_realm_lotus_bridge_target` | Saved by `common/scripted_effects/003_holy_realm_effects.txt:542-561` and used by on-action and achievement bridges. Retain pending bounded lifecycle verification. |
| `holy_realm_mandala_of_nations_leader` | Saved at `common/scripted_effects/003_holy_realm_effects.txt:1364-1365` and checked by on-action logic around `:87-93`. Retain as persistent leader identity. |
| `holy_realm_country` | Saved at `common/scripted_effects/003_holy_realm_effects.txt:1854` and used by `events/003_the_holy_realm.txt:258,260,284`. Retain. |

The event-target audit must also account for regular targets that auto-clear at the end of an originating effect chain, global targets that require explicit cleanup, localisation scopes that omit the `event_target:` prefix, and generated meta-effect names. The offline Scripted GUI wiki says event targets cannot be used in scripted GUIs, while the Chaos Redux events skill documents event-target use as valid in the project’s scripted-GUI pattern. This is an unresolved engine/documentation conflict; do not migrate GUI target access until a minimal runtime proof exists.

## Collections and registries

`common/collections/chaosx_country_collections.txt` declares broad country arrays including `chaosx_country_all`, independence-wave, owned, registered, Iberian, selectable-bound/unbound, owned-bound/unbound, registered-bound/unbound, overlay routes, regional overlay groups, Africa, Soviet-collapse, and 14 `chaosx_country_region_*` collections.

`common/collections/006_independence_wave_country_collections.txt` declares Event 006 resolved-carrier, new-tag, registered-reuse, selectable, owned, overlay, and regional arrays.

`common/collections/anti_zombie_league_collections.txt` declares `world_non_zombie_controlled_states`.

The live collection consumers found in the in-scope search are `common/scripted_triggers/012_africa_priority_member_triggers.txt:112`, which uses `collection:chaosx_country_independence_wave_owned`, and `:116`, which uses `collection:chaosx_country_africa_overlap_non_overlay`. `common/scripted_effects/012_africa_priority_member_effects.txt:243` contains a collection reference in a comment.

Most other collection declarations are documented API or future hooks rather than live consumers in Events 1-20. The Event 006 documentation says these are lookup-only semantics with static arrays as the source of truth. Do not remove declarations based on zero local consumers without searching generated meta references and external scenario tooling.

## Meta effects and dynamic dispatch

The source uses meta effects for dynamic equipment names, Event 019 provider dispatch, scenario/provider registration, and other static-field injection where direct variables are unsupported.

The Event 019 provider contract is the highest-risk shared dynamic dispatch surface. Concrete providers include IDs 501 and 502 in `019_infantry_spawn_unit_registry_effects.txt`, 520 in `020_black_plague_effects.txt`, 521 in `cbrn_doctrine_effects.txt`, 518 in `018_resources_found_cave_effects.txt`, and 504-510 and 522 in `016_brilliant_scientist_project_force_event19_effects.txt`.

The dynamic call sites around `019_infantry_spawn_core_effects.txt:193` and the derivative package files construct provider names through `meta_effect`. Any source-only `rg` count can miss these generated calls, so no provider is a stale-helper deletion candidate.

Meta effects and meta triggers must remain part of every future helper proof pass. A helper with zero literal call sites is not dead until generated names, scripted localisation, arrays, and data-driven identifiers have been checked.

## Constants and magic-number candidates

Shared constants are already present in `common/script_constants/event_system_constants.txt`, `event_cluster_constants.txt`, `chaosx_triggerable_scenarios_constants.txt`, `world_end_scenario_registry_constants.txt`, `chaos_meter_constants.txt`, and Event 005, 006, 012, 014, 015, 016, 018, 019, and 020 constant files.

The following are the meaningful remaining candidates.

| Location | Candidate | Disposition |
| --- | --- | --- |
| `chaosx_logic_effects.txt` event category initializer | Legacy literal IDs are mixed with newer `constant:` IDs. | Defer until category ownership, aliases, and historical IDs are proven. |
| `chaosx_dynamic_effects.txt:17-45` | Tier ladder values in an uncalled helper. | Do not centralize until a caller or retained API is confirmed. |
| `chaosx_dynamic_effects.txt:319-407` | Literal sea-region list with duplicate 110. | Defer; duplicate may encode weight. |
| `chaosx_dynamic_effects.txt:93,103,119,123` | Building-damage defaults in an uncalled helper. | Proof-gated; no active tuning owner. |
| `chaosx_event_cluster_effects.txt:15-27` | File-scoped `@` cooldown, sentinel, and slot values. | Possible future `script_constants` migration only after field-support checks and subsystem ownership review. |
| Event log and chaos-meter zero/one sentinels | Repeated numeric initialization. | Mostly lifecycle sentinels; existing constants already cover the meter’s zero/one/negative-one values. Leave. |

Any accepted probability or AI-weight change requires the baseline probability inspection above followed by the same-scenario `hoi4.probability_compare` pass through the project auditor route. No such change is accepted in this report.

## High-confidence patch candidates

These candidates are narrow and preserve current behavior.

### 1. Correct helper documentation ownership

Split `chaosx_dynamic_effects.md` into a declared-helper index and linked subsystem API sections, or add an explicit source-of-truth column for every documented helper family.

The documentation should identify the exact source file for Event 006, Event 016, clone, alien, Mengele bridge, and Event 019 provider contracts, and should explain that generated provider names are dispatched through `meta_effect`.

This is documentation-only and does not require gameplay, GUI, asset, or localisation edits.

### 2. Correct stale world-threat documentation paths and wrapper wording

Update `docs/systems/world_threat_mechanic.md:81,154` from `014_cannibalism_core_effects.txt` to `014_cannibalism_effects.txt`.

Reconcile the `has_world_threat_source_black_plague` mention in `chaosx_dynamic_effects.md` with the absence of a public Black Plague wrapper in `chaosx_world_threat_triggers.txt` and the explicit no-wrapper statement in `world_threat_mechanic.md:122`.

This should remain documentation-only until a gameplay owner requests a wrapper and supplies lifecycle and caller proof.

### 3. Preserve and consolidate call sites onto existing APIs

Event 14, Event 18, Event 20, and shared chaos-meter flows already use the dynamic population, technology-union, stockpile, and natural-disaster APIs. A cleanup tranche should check for local copies around those call sites and replace only exact semantic duplicates with the existing helpers.

No new generic population-loss or equipment-payment helper is justified by this baseline.

### 4. Bounded functional event-log binding review

The repeated tab reset/detail-close/view-rebuild sequence in `common/scripted_guis/chaosx_scripted_gui_events_log.txt:40-157` could be represented by a narrowly scoped functional helper such as `events_log_select_tab` with a tab token, selected-tab flag, detail-close side effects, and view rebuild.

This is a proposal for later review, not an accepted patch in this baseline. It must not modify `interface/*.gui`, GUI assets, coordinates, sizes, layout, or visual states, and it requires read-only MCP inspection before and after any future scripted-GUI binding change.

## Dynamic-reference uncertainty and proof requirements

### Orphan helper deletion proof

Before deleting `modify_value_based_on_chaos_tier`, `damage_buildings_in_random_states`, or `clear_special_chaos_country_civilian_effects`, search all source, markdown, generated Qoder/Codex metadata, scripted localisation, `meta_effect`, `meta_trigger`, collection, and data-driven references.

For `damage_buildings_in_random_states`, also search event and scenario plans because its defaults may represent a deferred mechanic rather than accidental dead code.

### Event-target deletion proof

Before clearing or deleting any no-clear global target, prove its save and read lifecycle, including `has_event_target`, event-target localisation, achievement and on-action use, dynamic effect names, terminal event history, and save compatibility.

Do not infer stale state from the absence of `clear_global_event_target`.

### Collection deletion proof

Before deleting an apparently unused collection, inspect all collection operators, generated collection names, scenario registry references, Event 006 documentation, and any external tooling that reads collection identifiers.

### GUI target proof

Do not migrate event-target access in scripted GUIs based on either source-only reading or a single wiki statement. The offline wiki and project skill disagree, and the GUI MCP inspection returned approximations and unsupported constructs. Obtain a minimal engine-backed proof before changing functional bindings.

### World-threat preview proof

Before consolidating Event 005 preview source counting with `refresh_world_threat_state`, define whether the preview is an intentionally reduced pressure model or a stale duplicate. Compare all source flags, timing, reset behavior, and displayed values under named scenarios.

## Proposed helper map for any later implementation

No helper was implemented in this baseline. The following map records safe reuse and one bounded future candidate.

| Helper/API | Scope | Inputs | Outputs | Side effects | Known call sites |
| --- | --- | --- | --- | --- | --- |
| `refresh_world_threat_state` | Country/global state flow as defined by current source | Source flags and current global threat state | `global.world_threat_source_count`, `world_in_threat` | Sets or clears global aggregate flag | Events 2, 3, 5, 7, 10, 14, 16, 18, 20 and shared/21+ effects listed above |
| `union_compatible_researched_technologies_from_donor` | Country with donor event target | `event_target:technology_union_donor.researched_techs` | Compatible researched technologies on current country | Adds allowed technologies while skipping branch conflicts | Event 14 `014_cannibalism_effects.txt:12401,12577,18595` |
| `call_natural_disaster` | Country/event scenario | Current disaster token and current scenario inputs | Natural-disaster event/effect dispatch | Fires the selected disaster flow | Event 13 and cluster/scenario callers listed above |
| `apply_state_population_loss_without_recruitable_manpower_gain` | State | Population-loss amount and state context | Updated state civilian population | Applies loss without adding recruitable manpower | Dynamic source, chaos meter, Fallout |
| `apply_exact_state_civilian_population_loss` | State | Exact civilian population loss | Updated civilian population | Applies exact loss semantics | Events 14, 15, 18, and 20 call sites listed above |
| `remove_*_from_stockpile` family | Country | Equipment/resource amount | Updated stockpile | Debits the named resource safely | Event 20 response/shared/terminal/weaponization paths and 21+ callers |
| Future `events_log_select_tab` | Shared scripted-GUI functional binding | One tab token or statically dispatched tab selector | Selected tab/view state | Clears sibling tab flags, closes detail views, rebuilds selected view | Four repeated tab handlers around `chaosx_scripted_gui_events_log.txt:64-157` |

The future GUI helper must be designed around the existing shell’s accepted functional state contract, not around visual layout changes.

## Migration and cleanup plan

First, repair documentation ownership and stale paths because these changes reduce future false orphan findings without touching gameplay.

Second, run a targeted generated-reference audit for the three orphan-looking dynamic effects and the no-clear target list.

Third, compare Event 005 preview semantics against the central world-threat aggregate before deciding whether any registry extraction is safe.

Fourth, audit exact local duplicates at Event 14, Event 18, and Event 20 call sites and reuse existing helpers only where inputs, scope, defaults, outputs, and side effects are identical.

Fifth, if the parent elects to clean the event-log scripted GUI, make it a separate bounded functional-binding plan with GUI MCP evidence and explicit confirmation that `interface/*.gui` and assets remain unchanged.

Defer legacy category migration, Event 006 registry redesign, Event 019 provider redesign, global target auto-clearing, collection deletion, sea-region weighting changes, and broad `@` constant conversion.

## Risks and unsupported analysis

The MCP event graphs were partial and span two workspace revisions, so they cannot prove complete helper reachability or save-state lifecycle.

The GUI inspection was structurally useful but aggregate diagnostics were truncated and included unrelated index collisions; it is not evidence for layout changes.

The probability adapter discovered zero custom weighted-pool candidates in `chaosx_logic_effects.txt`, so no weighted helper balance conclusion can be drawn.

The callable tool surface did not expose the named `chaosx_ai_probability_auditor` subagent route, so this report records source probability inspection but does not claim an auditor evidence pass or probability compare.

The offline scripted-GUI wiki and project skill disagree about event-target support in scripted GUIs. This remains an explicit blocker for event-target migration.

No live game was launched and no runtime save was modified, as required by repository instructions.

## Files changed

Only this report was written: `docs/plans/repo_cleanup/subagent_handoffs/shared_helper_architecture_baseline_2026-08-22.md`.

No source, GUI, asset, localisation, spreadsheet, or generated-agent file was changed.

## Simplifications, omissions, and blockers

This is a baseline and intentionally does not delete helpers, clear persistent targets, normalize constants, migrate registries, or change scripted-GUI bindings.

The absence of direct calls in source searches is treated as uncertainty whenever generated names, meta effects, collections, or external scenario data could provide a reference.

Events 21+ were not audited as event-specific systems; only shared-infrastructure consumers were retained in the call-site inventory.

No interface layout, coordinate, asset, or visual behavior recommendation is accepted.

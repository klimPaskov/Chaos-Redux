# CXT country audit — history/runtime follow-up

Date: 2026-09-13.

Mode: read-only country-package audit limited to the six CXT core files, the supplied QA inventories and receipts, the static CXT unit roster, and the already recorded callback/MCP evidence.

No gameplay source, country asset, localisation, skill, or generic callback file was edited by this audit.

## Result

The current source preserves all 83 installed special-project calls, all 71 static stockpile entries, all six facility types, the history pre-unlock sequence, the runtime extension contract, and the public receiver-event ordering.

The static roster independently contains 87 unique CXT templates and 87 matching three-division spawns, yielding 261 divisions.

The source-level repair removes the reported obsolete technology-variable and tank-archetype forms, while actual in-engine execution of dynamic token loops, random-province facility construction, and native history notification behavior remains unverified under the no-game constraint.

## Country-package coverage checklist

| Surface | Evidence | Audit result and boundary |
| --- | --- | --- |
| Tag and history | `history/countries/CXT - Chaos Redux Test Country.txt:8-28` and `common/scripted_effects/chaosx_test_country_effects.txt:306-335` | CXT history is the actual verbose-path history file, starts dormant, pre-grants content, and the console transition queues `chaosx_test_country.1` before `change_tag_from`; tag registration and country-definition files were outside this bounded read-only pass. |
| State and map setup | `common/scripted_effects/chaosx_test_country_effects.txt:53-151` | Facility provisioning preserves existing legal campuses, selects owned/control-valid states, explicitly requires a coastal state for naval facilities, revalidates temporary transfers, and restores rejected owner/controller state; native construction success and map-side province selection were not executed. |
| Politics, leader, portrait, flag, advisor and party | `history/countries/CXT - Chaos Redux Test Country.txt:10-20` | History sets neutrality, disables elections, and sets the four listed ideology popularities; leader, portrait, advisor, party-name, flag and country-localisation coverage were outside this six-file runtime audit. |
| Focus, decision, idea and assets | CXT core files contain no focus-tree, decision-category, idea, asset or localisation definitions | No issue was asserted because those package surfaces were outside the reassigned history/runtime boundary. |
| Starting military | `common/scripted_effects/chaosx_test_country_unit_effects.txt:12-1809` | The static harness has 87 `division_template` blocks, 87 matching `create_unit` blocks, 87 `count = @CXT_TEST_UNIT_COUNT` fields with `@CXT_TEST_UNIT_COUNT = 3`, and 87 unique template names, so the 87/261 roster remains intact. |
| Technology | `common/scripted_effects/chaosx_test_country_technology_effects.txt:11-33` | The helper still enumerates `global.technology`, injects each `GetTokenKey` through `meta_effect`, and uses `popup = no`; no technology ID was filtered or discarded. |
| Projects and special facilities | `common/scripted_effects/chaosx_test_country_special_project_effects.txt:21-210` and `common/scripted_triggers/chaosx_test_country_triggers.txt:21-38` | All 83 static project IDs and all six facility IDs remain; the helper uses the documented project scope and exact native facility-type trigger, while engine execution remains a parent-owned validation limit. |
| Industry, supply and production | `common/scripted_effects/chaosx_test_country_stockpile_effects.txt:52-354` and `common/scripted_effects/chaosx_test_country_effects.txt:143-151` | The stockpile keeps its 71 concrete entries and three gated flame variants, and facility provisioning keeps all six specializations; no balance or production redesign was introduced. |
| AI and playability | Six CXT core files and the facility helper | No AI weights or probability tuning changed; facility random candidate eligibility changed through exact legal filters and is covered by the corrected `facility_probability_corrected` baseline/current same-scenario projection and final specialist review; live playability was not claimed. |

## File-surface checklist

| File | Verified contract | Remaining limit |
| --- | --- | --- |
| `common/scripted_effects/chaosx_test_country_effects.txt:261-280` | Runtime setup grants technologies before facility provisioning and skips the static history grant after `chaosx_test_country_history_unlocks_completed` is set. | Facility construction still ends at the native state-scope `construct_building_in_random_province` call at `:124`; no engine run was available. |
| `common/scripted_effects/chaosx_test_country_effects.txt:306-335` | `country_event = { id = chaosx_test_country.1 hours = [SETUP_DELAY] }` is at line 330 and `change_tag_from = event_target:chaosx_test_origin_country` is at line 331. | The ordering is source-verified only. |
| `common/scripted_effects/chaosx_test_country_technology_effects.txt:11-33` | The runtime inventory is retained and obsolete direct `var:` technology forms are absent. | MCP technology inspection reports `1396` blocking diagnostics and does not execute the runtime loop or token values. |
| `common/scripted_effects/chaosx_test_country_special_project_effects.txt:11-19` | Static completion uses `sp:$PROJECT$`, `show_modifiers = no`, and a completion guard; the registered helper uses the documented `var:` project form. | Dynamic registered projects depend on the package-owned registry contract and were not engine-executed. |
| `common/scripted_effects/chaosx_test_country_special_project_effects.txt:21-210` | The static helper contains 83 unique project calls, sets the silent flag before completion, initializes the CXT zombie profile first, and clears the silent flag after registered completion. | Native history notification suppression is not explicitly guaranteed by the installed documentation. |
| `common/scripted_effects/chaosx_test_country_special_project_effects.txt:238-248` | Registered project completion sets and clears the same temporary silent flag around the registry loop. | The registry owner remains responsible for registering an installed, eligible project token. |
| `common/scripted_effects/chaosx_test_country_stockpile_effects.txt:10-50` | Three domestic variants are created with concrete chassis types and `allow_without_tech = yes` under the No Step Back gate. | Variant construction was source/schema checked but not executed in the game. |
| `common/scripted_effects/chaosx_test_country_stockpile_effects.txt:326-352` | The three reported flame archetypes are replaced by concrete `_3` types with named variants and `producer = CXT`. | No other stockpile entry was removed. |
| `common/scripted_triggers/chaosx_test_country_triggers.txt:21-38` | The state trigger requires CXT ownership, CXT control, no existing special facility, the requested exact building type, and explicit coastal state for naval use. | Installed effects documentation describes the constructor as random-province state-scope behavior, so source checks do not substitute for engine success. |
| `history/countries/CXT - Chaos Redux Test Country.txt:22-28` | The history file grants technologies, initializes the zombie profile, completes projects, repeats the technology grant, and records the history-unlock flag before runtime activation. | Callback coverage and native history popup behavior are recorded below. |

## History unlock and popup coverage

The history sequence at lines 24-28 is `complete_all_technologies`, `initialize_cxt_weaponized_zombie_profile`, `complete_all_special_projects`, `complete_all_technologies`, then `set_country_flag = chaosx_test_country_history_unlocks_completed`.

The static project helper sets `chaosx_test_country_silent_unlocks` before its 83 calls and clears it after the registered-project pass, while the runtime synchronization helper sets it at `common/scripted_effects/chaosx_test_country_effects.txt:292` and clears it at `:297`.

The exact static project set compares equal to `cxt_project_inventory_check.json`, with `expected_count = 83`, `actual_count = 83`, no missing IDs, no extra IDs, and no duplicate IDs.

The project inventory preserves every installed DLC gate, including the dual `Gotterdammerung` plus `Man the Guns` gate for `sp_naval_nuclear_torpedo` and the `Peace For Our Time` gate for `sp_land_large_caliber_kinetic_energy_sabot`.

The seven custom eligibility additions retain the original country predicates and add CXT eligibility for `sp_cw_malodor_bomb_program`, `sp_cw_aphrodisiac_bomb_program`, `sp_japan_pingfang_records_office`, `sp_japan_kwantung_medical_intelligence`, `sp_japan_occupation_test_ledger`, `sp_japan_epidemic_mapping_bureau`, and `sp_japan_cherry_blossom_dossier`.

The custom `allowed` additions are eligibility-only predicates and do not alter foreign-country AI strategies or AI weights.

The already recorded callback audit at `project_popup_audit.md` covers the history-reachable report paths as follows.

| Callback | History behavior | Preservation decision |
| --- | --- | --- |
| `chaosx.nr16.40` from D’Rhondan | The CXT silent path invokes the underlying authorization helper without the visible report. | Mechanical authorization remains available and the ordinary report remains for non-CXT completion. |
| `chaosx_nr20_weaponization.2` and `.6` | The CXT silent path suppresses only the immediate report dispatch. | Stockpile, technology, completion flags and countermeasure effects remain. |
| `chaosx.weaponized_zombies.1` | CXT is excluded from the success report, while the completion bonuses and achievement effect remain. | The CXT initializer runs before project completion. |
| `chaosx.weaponized_zombies.8` | The failure report remains mechanically active outside CXT and is unreachable under the reviewed dormant CXT fixture because the extreme mutation gate is not established. | No broad failure suppression was added. |
| `germany_mengele.24` | The delayed revolt event requires Germany's active/restricted program and original GER scope. | The coup path remains untouched. |
| Event 016 prototype and biological field-test reports | Their host/provider or facility-state actor gates are not satisfied by dormant CXT history completion, and they are not ordinary country completion reports. | No generic callback mechanism was suppressed. |

This coverage prevents the known project-owned report callbacks from being queued during the CXT silent completion transaction, but the installed vanilla documentation does not explicitly state whether the native completion notification itself is suppressed while country history loads.

## Error mapping and changed IDs

The reported invalid technology forms are addressed by the `GetTokenKey` meta-effect path at `common/scripted_effects/chaosx_test_country_technology_effects.txt:16-28`, with no technology IDs filtered.

The three reported tank-archetype forms are replaced as follows: `light_tank_flame_chassis` becomes `light_tank_flame_chassis_3` with `CXT Light Chemical Carrier`, `medium_tank_flame_chassis` becomes `medium_tank_flame_chassis_3` with `CXT Medium Chemical Carrier`, and `heavy_tank_flame_chassis` becomes `heavy_tank_flame_chassis_3` with `CXT Heavy Chemical Carrier`.

The installed effects documentation requires `create_equipment_variant.type` to be a concrete type rather than an archetype, and the current stockpile helper contains 71 unique static `type` fields with no old flame-archetype token.

The six reported facility types remain `naval_facility`, `nuclear_facility`, `air_facility`, `land_facility`, `biowarfare_facility`, and `cw_facility`.

The current facility helper adds exact type-native `can_construct_building` checks, explicit naval-coastal eligibility, temporary transfer revalidation, rejected-state restoration, and incomplete flags, as recorded by `cxt_core_source_check.json`.

The remaining facility limitation is engine execution: the installed documentation defines `construct_building_in_random_province` as a state-scope random-province effect, so this audit records source legality and does not claim that every selected state contains a valid random province at runtime.

## Extension and ownership checks

The public CXT transition keeps the receiver event queued before the player-country transfer, preserving the receiver `ROOT = CXT` contract.

The runtime setup calls `chaosx_test_country_sync_registered_content` after static setup, and that helper applies registered extension effects, registered projects, registered equipment, and registered units inside the silent flag window.

The six audited core files contain no foreign-country AI blocks or AI weight tuning, while facility random candidate eligibility changed through the typed legal-selection path and is covered by the corrected `facility_probability_corrected` baseline/current same-scenario projection and final specialist review.

The unit file's static roster remains separate from the package-owned registered-unit loops beginning after line 1811, so the 87-template/261-division baseline was not replaced by a reduced fixture.

## Evidence and validation limits

The required baseline receipt is `cxt_core_baseline_hashes.json`, and this audit did not overwrite or regenerate any baseline file.

The supplied `cxt_core_source_check.json` reports `status = passed`, 83 retained projects, 71 retained concrete stockpile types, an unchanged public transition block, an unfiltered runtime technology inventory, six retained facility types, and source-level facility scenario coverage.

The local focused checks found 83 unique static project calls, exact equality with the supplied 83-ID inventory, 71 unique static stockpile types, no reported flame archetype, three concrete flame types, three named variants, 87 unique static template names, 87 matching unit creation blocks, and 261 derived divisions.

The installed vanilla references used for this audit are `documentation/effects_documentation.md:1252` for concrete stockpile types, `:2896` for `complete_special_project`, `:2925` for random-province construction, and `:3069` for concrete equipment-variant types.

The offline Paradox wiki core pages and equipment, technology, effects, scopes, triggers, event, and country-history pages were consulted before the source review, and the installed vanilla project/equipment documentation was treated as authoritative for the schema conclusions.

The recorded MCP workspace is `mod_chaos_redux_ea3b2d67c2c0`.

The technology inspection returned `TECH_INSPECTED` but failed validation with `1396` blocking technology diagnostics, while the event inspection returned `EVENT_INSPECTED_PARTIAL` and deferred helper/lifecycle projections; neither route executes CXT history or runtime token loops.

The narrow event timing renders selected zero nodes and therefore do not prove callback edges.
The parent separately inspected the installed package launchers and HTTP routes in `standalone_technology_viewer_package_check.json`; that package has no standalone Technology Tree Viewer UI entrypoint, while independent external viewer installations were not inventoried.

No game launch, log search, reload advice, old-save advice, staging, commit, or source patch was performed by this audit.

## Remaining blockers and handoff

The parent should treat the CXT inventory, queue ordering, silent callback guards, concrete flame variants, and 87/261 roster as source-reviewed and preserved.

The parent should carry two unresolved engine limits into the final report: native history notification suppression is undocumented, and actual random-province facility construction was not executed.

The parent should review the supplied MCP partial artifacts and the root-owned facility candidate evidence before making an engine-level completion claim.

No simplification or content omission was made by this read-only audit.

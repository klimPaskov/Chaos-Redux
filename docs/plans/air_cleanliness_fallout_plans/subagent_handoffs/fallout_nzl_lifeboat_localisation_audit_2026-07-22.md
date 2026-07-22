# Fallout NZL Lifeboat State localisation audit

Date: 2026-07-22
Scope: `localisation/english/fallout_nzl_lifeboat_l_english.yml` and `common/scripted_localisation/fallout_nzl_lifeboat_scripted_localisation.txt`
Status: dormant package preserved

## Audit findings

- Missing key list: none found in the package surfaces audited.
- Duplicate key list: none. The localisation file contains 342 unique keys.
- Scripted localisation issue list: none. All 14 `localisation_key` references resolve to this package. The five `defined_text` names are unique.
- Decision cost coverage: all 15 `custom_cost_text` references have base, `_blocked`, and `_tooltip` keys. The current cost strings already use icon-first tokens, including the motorised and support-equipment groups.
- Focus coverage: all 42 actual focus ids have title and `_desc` keys. The apparent `fallout_nzl_lifeboat_focus_tree` gap is the focus-tree container id, not a missing focus localisation key.
- Idea coverage: all 14 package idea ids have title and `_desc` keys.
- Event coverage: the `.127`, `.129`, `.131`, `.133`, `.135`, `.137`, `.139`, `.141`, `.143`, `.145`, `.147`, `.149`, and `.151` chain references resolve. The source scan found 51 unique event localisation tokens with no missing keys.
- Government and runtime character names and traits are present. The static character file is intentionally empty because runtime generation owns the package character tokens.

## Patch applied

Changed file:

- `localisation/english/fallout_nzl_lifeboat_l_english.yml`

The patch changes player-facing values to New Zealand English while leaving every identifier, variable token, scripted-localisation name, and dormant gate unchanged.

Changed keys:

- `fallout_nzl_relief_speaker_trait_desc`
- `fallout_nzl_harbor_constable_trait_desc`
- `fallout_nzl_empty_harbors`
- `fallout_nzl_storm_ports_desc`
- `fallout_nzl_open_berth_covenant_desc`
- `fallout_nzl_last_berth_doctrine_desc`
- `fallout_nzl_berth_riots_desc`
- `fallout_nzl_dairy_rations_desc`
- `fallout_nzl_improvised_sea_guard_desc`
- `fallout_nzl_splintered_patrols_desc`
- `fallout_nzl_lifeboat_category_desc`
- `fallout_nzl_auckland_storm_port_works_desc`
- `fallout_nzl_weather_station_chain_desc`
- `fallout_nzl_port_militia_training_mission_desc`
- `fallout_nzl_arm_rescue_cutters_action_desc`
- `fallout_nzl_mobilize_home_guard_state_desc`
- `fallout_nzl_cost_home_guard_tooltip`
- `fallout_nzl_cost_dairy_relief_convoy_tooltip`
- `fallout_nzl_seat_the_lifeboat_parliament_desc`
- `fallout_nzl_relay_auckland_radio_desc`
- `fallout_nzl_keep_the_harbor_lights`
- `fallout_nzl_publish_the_berth_ledger_desc`
- `fallout_nzl_guarantee_lifeboat_rights_desc`
- `fallout_nzl_appoint_the_harbor_constable`
- `fallout_nzl_fishery_quota_compacts_desc`
- `fallout_nzl_storm_port_engineers_desc`
- `fallout_nzl_port_militia_drill_desc`
- `fallout_nzl_coastal_denial_batteries_desc`
- `fallout_nzl_punitive_anti_piracy_patrols_desc`
- `chaosx.fallout.127.t`
- `chaosx.fallout.127.d`
- `chaosx.fallout.131.d`
- `fallout_nzl_opening_result_success_text`
- `chaosx.fallout.133.d`
- `fallout_nzl_domestic_result_success_text`
- `chaosx.fallout.141.d`
- `chaosx.fallout.143.b.tt`
- `fallout_nzl_external_result_success_text`
- `chaosx.fallout.147.t`
- `chaosx.fallout.151.a`
- `fallout_nzl_late_result_success_text`
- `chaosx_fallout_nzl_open_harbors_NAME`

Display before and after:

- American spellings such as `harbor`, `defense`, `labor`, `mobilization`, `mobilize`, `rumors`, `program`, and `authorized` in player-facing values now read `harbour`, `defence`, `labour`, `mobilisation`, `mobilise`, `rumours`, `programme`, and `authorised`.
- The noun `license` now reads `licence`. The focus title `License Every Sea Road` remains unchanged because `License` is the verb there. The `licensed` adjective remains valid.
- Dynamic category variables and cost values are unchanged. No new scripted localisation was added.

## Dynamic text opportunities and unresolved decisions

- The category description already exposes the live harbour, food, trust, and sea-lane variables.
- The result selectors intentionally cover success, partial, and failure. There is no explicit `fallout_nzl_chain_result = none` branch. The current effects set a valid result before these descriptions display. Adding a fallback would be a resilience change to the dormant chain, so it was not made in this localisation-only pass.
- The source identifiers retain `harbor`, `license`, and `fallout_nzl_harbor_capacity` spelling for script compatibility. Only visible values were changed.
- Regional grounding remains explicit through Wellington, Auckland, Canterbury, Cook Strait, Northland, the South Island, and the dairy districts. No route lore or mechanic was invented.

## Validation

Meaningful checks run:

- Parsed the package localisation keys and found no duplicates. Confirmed UTF-8 BOM on the `.yml` file.
- Resolved all scripted-localisation references, all 15 decision cost triplets, all 42 actual focus title and description pairs, all 14 idea title and description pairs, and the 51 limited-chain event tokens.
- Scanned player-facing values for em dashes, semicolons, and the targeted American spellings. No prohibited punctuation or targeted spelling remains. The only visible `License` is the intentional verb title.
- Confirmed `common/scripted_localisation/fallout_nzl_lifeboat_scripted_localisation.txt` was audited but not modified. Its non-BOM text encoding is unchanged.

Skipped meaningful validation:

- No HOI4 launch, GUI render, or live save check was run. The parent scope explicitly forbids running HOI4, and this patch changes only localisation wording in a dormant package.

No plan handoff was written because the audit found no missing mechanic that requires gameplay implementation.

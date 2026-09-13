# Decision cost localisation repair

Status: localisation patch and parent texticon wiring implemented; parent production MCP pixel review completed for fifty-two explicit native row fixtures, documented in README.md and decision_native_pixel_receipts.json.

55 changed keys in three localisation files.
Exact old/new text is in `decision_cost_changes.json`; 14 sibling decision scenarios, category IDs, resolved ready/blocked strings, constants, omitted-inline constants and full-tooltip strings are in `decision_cost_scenarios.json`.
Baselines retain exact pre-edit bytes under `baseline/localisation/english/` and SHA-256 receipts are in `decision_cost_sha_receipts.json`.

## Display and payment contract

Wonder operations retain Command Power, support equipment and fuel inline because these are the three immediate debits.
Their fourth entry, civilian factory occupation, remains dynamically resolved in each full cost tooltip and native decision modifier.
Light inline values resolve to 20 Command Power, 75 support equipment and 250 fuel with 2 factories in the tooltip.
Standard and synthesis resolve to 25, 100 and 500, with 2 or 3 factories respectively.
Heavy resolves to 40, 200 and 1,500 with 3 factories.
All existing per-resource scripted affordability colours remain intact, including a blocked factory visible in the full tooltip.

Payload expansion retains support equipment 40, Command Power 20 and fuel 400 inline.
Motorized equipment 20 remains in the new full tooltip, which also names factory occupation 2 and duration 60 days.
Payload destruction retains all three immediate debits inline: support equipment 20, Command Power 10 and fuel 100.
Its full tooltip additionally presents factory occupation 1 and duration 30 days.
Ready and blocked versions use the same dynamic amount tokens with their existing yellow or red state.

Biological surveillance retains instruments 80, support equipment 60 and Medical Capacity 10 inline.
Smallpox vaccination retains instruments 50, support equipment 250 and Medical Capacity 10 inline.
Their respective motorized payments 20 and 100 remain verbatim in new full-cost tooltips.
Native Political Power costs, affordability, payments, occupation modifiers, durations, AI and descriptions are untouched.

## Texticon resources and parent follow-up

Inline resources already available: GFX_support_equipment_text_icon in interface/chaosx_texticons.gfx uses gfx/texticons/support_equipment_text_icon.dds; GFX_motorized_equipment_text_icon uses gfx/texticons/motorized_equipment_text_icon.dds.
Vanilla GFX_fuel_texticon uses gfx/texticons/fuel_texticon.dds; GFX_civ_factory, GFX_command_power and GFX_clock_texticon are vanilla texticons.
New inline biology references require parent-owned GFX_cbrn_instruments_texticon and GFX_medical_capacity_texticon definitions and matching textures.
The parent accepted wiring those sprites with existing matching artwork and no new art.
The CBRN source family exists in interface/cbrn_protection.gfx as equipment medium sprites, including gfx/interface/technologies/stage_2_protective_equipment/equipment/cbrn_instrument_equipment_1.dds.
No proper custom texticon existed at baseline.

New keys: bio_activate_surveillance_network_cost_tooltip, smallpox_vaccination_mass_program_cost_tooltip, black_plague_weaponization_expand_stockpile_cost_tooltip and black_plague_weaponization_destroy_stockpile_cost_tooltip.
Offline Decision modding lines 303-304 explicitly document native <custom_cost_text>_tooltip lookup on hover, so these keys require no gameplay source change.
Wonder tooltip keys were unnested to preserve the complete former four-entry display rather than aliasing the shortened inline string.

## Writing review

Bloat and obvious explanation: removed articles from Wonder and payload titles; shorter synthesis and strike titles preserve the action and route identity.
Overcomplication: Activate the High-Speed Strike Network becomes Activate High-Speed Strikes; Launch a Long-Range Delivery Strike becomes Launch Long-Range Strike.
Repetition and inline filler: long blocked payment sentences become the corresponding compact red resource entries.
Vagueness: retained precise Smallpox identity and Biological Surveillance identity in shorter names.
Style: inline cost rows contain zero ordinary resource-label words after parent texticon wiring, and no filler or punctuation sentences.
No event prose, descriptions or attributed quotations were changed.
All amount tokens that remain inline preserve their original constants, thresholds and numeric formatting.
Omitted inline values are retained in full cost tooltips and never removed from gameplay.

## Validation and limitations

Task-specific source comparison verified every baseline key outside the 55 assigned keys remains unchanged and found no duplicate keys in the touched files.
Fourteen sibling scenarios were resolved against actual script constants and explicit affordability scenarios.
Each inline cost has at most three numeric entries, and all formerly inline payment tokens remain present in its full tooltip.
No missing assigned keys or broken scripted-localisation references were found.
No new dynamic helper was needed; existing Wonder independent affordability branches remain used.
Localisation UTF-8 BOM was preserved.
No catalog prose or workbook was changed because these native cost and title keys are not event-detail catalog wording.

Parent owns native GUI MCP inspect/render/compare, service-health evidence and production pixel fit, so visual completion is pending that evidence.
Standalone Technology Tree Viewer availability was not established in this bounded native-decision text task; no technology tree source was inspected or edited.
The unrelated biological countermeasure decisions in chaosx_disease_containment_category are outside the parent-assigned screenshot rows and their direct siblings.
No new mechanics, design fallbacks or simplifications were introduced.
No staging or commit was performed per parent ownership instruction.
Skills used: chaos-redux-decisions-missions, chaos-redux-events and chaos-redux-subagents; no skills edited.

## Changed keys

- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_launch_predictive_campaign
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_saturate_sensor_region
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_construct_state_synthesis_works
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_activate_high_speed_strike_network
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_launch_long_range_delivery_strike
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_raise_field_projectors
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_light_cost
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_light_cost_tooltip
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_standard_cost
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_standard_cost_tooltip
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_synthesis_cost
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_synthesis_cost_tooltip
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_heavy_cost
- localisation/english/016_brilliant_scientist_technology_actions_l_english.yml :: brilliant_scientist_technology_action_heavy_cost_tooltip
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_expand_stockpile
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_destroy_stockpile
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_expand_stockpile_cost
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_expand_stockpile_cost_blocked
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_expand_stockpile_cost_tooltip
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_destroy_stockpile_cost
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_destroy_stockpile_cost_blocked
- localisation/english/020_black_plague_weaponization_l_english.yml :: black_plague_weaponization_destroy_stockpile_cost_tooltip
- localisation/english/chaosx_decisions_l_english.yml :: bio_activate_surveillance_network
- localisation/english/chaosx_decisions_l_english.yml :: bio_stand_down_surveillance_network
- localisation/english/chaosx_decisions_l_english.yml :: smallpox_vaccination_mass_program
- localisation/english/chaosx_decisions_l_english.yml :: revoke_smallpox_vaccination_mass_program
- localisation/english/chaosx_decisions_l_english.yml :: bio_activate_surveillance_network_cost_tooltip
- localisation/english/chaosx_decisions_l_english.yml :: bio_activate_surveillance_network_cost
- localisation/english/chaosx_decisions_l_english.yml :: bio_activate_surveillance_network_cost_blocked
- localisation/english/chaosx_decisions_l_english.yml :: smallpox_vaccination_mass_program_cost_tooltip
- localisation/english/chaosx_decisions_l_english.yml :: smallpox_vaccination_mass_program_cost
- localisation/english/chaosx_decisions_l_english.yml :: smallpox_vaccination_mass_program_cost_blocked

## Evidence correction

Wonder fixtures evaluate first-match defined_text predicates with explicit resource inputs and record selected leaves, comparisons, thresholds and results for all-affordable, all-resources-unmet and each single-resource-unmet scenario.
Original default-leaf fixture selection incorrectly coloured ready support payments red and has been replaced.
Byte-level inspection confirms U+00A7 and U+00A3 in source, baseline and JSON without U+00C2 prefixes.
Read JSON explicitly as UTF-8 to avoid CP1252 display mojibake.
No localisation source changed during evidence correction.

## Native row components

Supplement decision_native_components.json records exact native PP, factory occupation, duration and cooldown tokens/values for all 14 IDs.
Wonder has no explicit base PP field, surveillance adds native PP40 and vaccination native PP150, with stand-down/revoke PP0.
Wonder and payload actions have native factory occupation in addition to their custom rows.
Original Wonder screenshot is consistent with duplicate factory indicators before shortening, but the engine formatter/order is unavailable in installed source and documentation.
No exact complete engine concatenation is claimed.
Parent production render must include these native fields and timer states where the inspector supports them.

## Final parent-directed title fit repair

brilliant_scientist_order_emergency_regeneration is Emergency Regeneration; smallpox_vaccination_mass_program is Smallpox Vaccination.
The final patch changes 33 keys, with exact baseline text retained in decision_cost_changes.json.
Both title changes preserve action identity and leave descriptions, tooltips and gameplay untouched.

## Source texticon whitespace repair

Parent production renders found Wonder icon names absorbed adjacent colour-reset tokens and became missing sprites.
All 22 technology_action_* leaves now use established icon-first whitespace syntax, for example £command_power §Y[?constant:brilliant_scientist_technology_action.standard_command_power|0]§!.
Amounts, colour codes and affordability predicates remain unchanged.
No closed-£ delimiters remain in the source patch.
Original leaf text and SHA-256 receipts are in decision_texticon_leaf_receipt.json.
All six affordability variants for eight Wonder decisions were regenerated from actual source and recorded source-selected leaves.
Final patch changes 55 keys without gameplay changes.

# Event 014 Cannibalism

Event 014 is a Minor Fire-Once war-horror outbreak. It begins as a discipline and supply collapse inside a country under war pressure, then turns into a local containment system where each affected country must fight its own outbreak. Early containment can defeat it for that country; failed containment opens ritual ideology, organized cults, communes, a global network, and the gated world-end route.

## Runtime Flow

1. `chaosx.nr14.1` selects an origin country using war, army, stability, war support, coastal, island, and prior-containment weighting.
2. `chaosx.nr14.2` opens the first outbreak with discipline, logistics, and secrecy postures.
3. `chaosx.nr14.3` confirms the first command investigation and lets the country follow kitchens, hospital chains, or command secrecy.
4. `cannibalism_start_outbreak_common` creates country variables for hunger pressure, discipline collapse, cult pressure, fear, spread pressure, containment, island silence, Hannibal resonance, and stage.
5. Decisions and timed missions change those values with concrete costs and objective checks.
6. `chaosx.nr14.4` is a hidden public-leak gateway that fires `chaosx.news.17` once when public fear or secrecy pressure exposes the ledgers.
7. If containment fails, `chaosx.nr14.5` hardens the outbreak and can unlock evolutions.
8. If containment reaches the threshold before the deadline, `chaosx.nr14.6` defeats the local outbreak and runs cleanup for that country.
9. Spread uses `chaosx.nr14.7`, so every spread country opens its own response surface rather than inheriting another country's result.
10. `chaosx.nr14.8`, `.9`, `.11`, and `.12` reveal ritual ideology, organized island or commune systems, the global cult network, and the Hannibal or later-unifier connection.

Direct external callers should use `cannibalism_call_direct_fire_once_if_possible` or `cannibalism_call_direct_fire_once_delayed_if_possible`. Africa Gods uses these wrappers so Cannibalism cannot be re-opened after Event 014 has already fired.

## Triggerable Scenario

Event 014 is registered in the manual Triggerable Scenarios window as `SCN-009: Cannibalism`. The scenario integration lives in `common/script_constants/chaosx_triggerable_scenarios_constants.txt`, `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`, `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`, `events/chaosx_triggerable_scenarios.txt`, and `localisation/english/chaosx_gui_l_english.yml`.

The manual launch suppresses Event 014's normal fire-once entry through `cannibalism_triggerable_scenario_suppressed_fire_once`, adds Event 014 to the fired/disabled event arrays, and clears temporary triggerable-scenario context after launch. The original opening still uses `cannibalism_event_dispatch_context` so `chaosx.nr14.2` can fire even though the manual scenario has already marked the fire-once event as spent.

Scenario types:

- War Horror Opening: sends the original `chaosx.nr14.2` outbreak report to a valid war-country origin.
- Cult Seeds: starts ritual ideology pressure in the origin and intensity-scaled extra countries, with each country receiving its own outbreak and containment work.
- Silent Islands: requires a coastal origin, raises the island-stage thresholds, and records the normal silent-islands evolution and super-event.
- Cannibal Commune: forces one origin past containment and calls `cannibalism_create_commune_country`, creating or reinforcing `CBL` through the normal country package.
- Hannibal Network: requires Hannibal, a later accepted unifier, the proxy-unifier flag, or explicit test flag `cannibalism_triggerable_hannibal_network_test_bypass`; it creates or reinforces the commune, links Hannibal discipline, records the global table, and arms future Hannibal hooks without launching world-end directly. The explicit test bypass satisfies Hannibal checks only while `cannibalism_triggerable_scenario_launch_active` is set and does not create a permanent unifier.

Intensity changes advanced starts by scaling extra outbreak countries, cult pressure, spread pressure, network strength, cult nodes, and death records. The Hannibal Network type raises the crisis to the existing Event 014 Hannibal-ready thresholds, but `cannibalism_world_end_route_available` still requires the chaos threshold plus Hannibal or a later accepted unifier before the world-end route can begin.

## Containment Values

Country variables are clamped through `common/scripted_effects/014_cannibalism_effects.txt` and tuned in `common/script_constants/014_cannibalism_constants.txt`.

- `cannibalism_hunger_pressure`
- `cannibalism_discipline_collapse`
- `cannibalism_cult_pressure`
- `cannibalism_public_fear`
- `cannibalism_spread_pressure`
- `cannibalism_containment`
- `cannibalism_island_silence`
- `cannibalism_hannibal_resonance`
- `cannibalism_stage`

The system uses flags for binary state such as local containment, exploitation, Hannibal linkage, island clearance, commune formation, and defeat. Global variables track active countries, spread count, cult nodes, communes, network strength, and world threat.

## Decisions and Missions

`common/decisions/014_cannibalism_decisions.txt` defines the response category. It does not create a political power store. Costs and objectives use direct resources and conditions:

- infantry equipment
- support equipment
- trains
- convoys
- fuel
- Army XP
- Command Power
- manpower
- stability
- war support
- supplied divisions
- controlled states
- naval access
- timed mission deadlines

Main response decisions include guarded kitchens, unit rotation, ration convoys, field-hospital audits, military police sweeps, prisoner transfer freezes, mess-line catechism work, public truth commissions, island inspections, evacuations, ritual-cell raids, commune retaking, anti-copying work, dismantling exploited terror units, exploiting those units, breaking with the cult, post-defeat aftermath cleanup, and the world-end launch route.

Timed missions register a concrete target state when they begin. Ration rail, hospital audit, prison kitchen, silent island, evacuation, ritual cell, commune retake, mainland copying, and terror-unit missions each mark a target state with country-targeted state flags, store that state id on the country for mission localisation, require the appropriate supply, control, naval, or rail access to that state, and clear only that country marker on success, failure, cancellation, or outbreak cleanup. Cleanup scans all states so lost-control targets do not survive after local containment or global defeat without erasing another country's active outbreak work.

The CBL route adds its own concrete project layer inside the same category:

- `cannibalism_cbl_map_the_last_table` spends Command Power, Army XP, trains, convoys, and fuel, then starts `cannibalism_cbl_last_table_map_mission`.
- `cannibalism_cbl_last_table_map_mission` names its selected map-anchor state in the mission description and requires at least four controlled states, coast or rail map projection, and at least one hunting-ground project before the deadline.
- `cannibalism_cbl_region_consumption_project` spends Command Power, support equipment, stability, and war support to expand controlled regional hunting grounds into an unmarked controlled state after the Last Table forms.
- `cannibalism_cbl_pact_courier_run` spends Command Power, a train, convoys, and fuel, then starts `cannibalism_cbl_pact_courier_mission` with a named coast or rail projection anchor.
- `cannibalism_cbl_solitary_border_raid` spends Army XP, infantry equipment, and fuel to claim a neighboring state on the solitary route.

Exploitation is deliberately dangerous. It can add coercive capability, but raises cult pressure, fear, network strength, Hannibal resonance, and foreign condemnation. The decision records that exploitation was used even if the country later breaks with the cult, applies a temporary negative opinion modifier from other countries, and forces the public-leak path. The AI assigns no positive weight to exploitation from availability alone; it needs a crisis or failed-containment condition plus an authoritarian/desperate profile. The `Break With the Cult` decision exists as a costly route exit rather than a free cleanup.

## Evolutions

Evolution records are wired into the Event Log through `chaosx_events_log_effects.txt` and `chaosx_scripted_localisation_events_log.txt`.

- Evolution I, Ritual Ideology: mess-line practice becomes doctrine. Ritual cells and catechism language raise cult pressure unless countries spend command attention, equipment, and supplied formations to break them.
- Evolution II, Organized Cults: silent islands, transfer zones, and communes can appear. Countries must inspect islands, evacuate marked zones, retake communes, and stop mainland copying.
- Evolution III, Global Cult Network: courier methods and Hannibal signals bind local outbreaks into a global table. The stage arms future Hannibal hooks and accepts a later unifier as a valid world-end gate actor.

## Cannibal Commune Package

The cannibal country package uses tag `CBL`.

- Tag registration: `common/country_tags/chaosx_countries.txt`
- Country file: `common/countries/Cannibal Commune.txt`
- History: `history/countries/CBL - Cannibal Commune.txt`
- Starting OOB: `history/units/CBL_1936.txt`
- Character: `common/characters/CBL.txt`
- AI strategy: `common/ai_strategy/014_cannibalism.txt`
- Focus tree: `common/national_focus/014_cannibalism_focus_tree.txt`
- Cosmetic formable route: `CBL_LAST_TABLE` in `common/countries/cosmetic.txt`

Commune creation requires an owned-controlled origin state, transfers that state to CBL, marks the state as a commune, assigns the table council, loads the OOB, sets the capital to the commune state, adds starting equipment, spawns starting forces, and declares war on the origin. Later commune failures reinforce the existing country instead of creating duplicate tags.

Non-CBL outbreak countries receive AI strategy pressure for army rebuilding, infantry and support-equipment production, trains, convoys, infrastructure, naval bases for transport-heavy island stages, and war-restraint during high-meter crisis containment.

The CBL focus tree has 36 focuses and covers:

- Opening and consolidation: first table, origin-state fortification, larder columns, black kitchens.
- Command hierarchy: Council of Knives, Warlord Kitchen, or Hannibal Discipline.
- Supply economy: depot inventory, field-kitchen conversions, prisoner ledger administration, ration codes.
- Military growth: hunger-column organization, scavenger parties, butcher packs, prison processions, Hannibal cadres.
- Origin expansion: silent anchorages for islands, port lists and convoy ambushes for coastal origins, prison roads and rail corridors for inland origins, and mainland hunting corridors for map consequences.
- Route fork: restrained consumption registers and Empty Larder discipline after a major enemy capitulates versus runaway hunting-ground accounts.
- Network fork: Cannibal Pact courier compact or solitary refusal of the wider pact.
- Last Table formable: preparation focus, map mission unlock, validated map gate, rival-table proof for the solitary achievement, Last Table proclamation, and post-formation controlled-region projects.
- World-end gate: `cbl_world_as_larder_gate` remains blocked by `cannibalism_world_end_route_available`, so chaos threshold plus Hannibal or an accepted unifier are required.

CBL cleanup clears commune and hunting-ground state markers, route flags, active CBL missions, CBL route ideas, and the Last Table cosmetic tag when global defeat is recorded.

## World-End Gate

The world-end route is `cannibalism_launch_world_end_route` and `cannibalism_try_world_end_route`. It requires:

- high chaos threshold through `cannibalism_world_end_route_available`
- the global table stage
- enough cult nodes
- enough communes
- Hannibal linkage or `cannibalism_later_unifier_accepted`

The route fires `chaosx.nr14.13`, raises the world-threat source, and emits super-event 143. Ordinary local failures cannot open it by themselves, and Hannibal/global-table achievements must be satisfied before this route begins.

## Super-Events and Audio

Super-event IDs are wired through `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, `sound/chaosx_sound.asset`, and `localisation/english/chaosx_music_l_english.yml`.

- `141`: The Silent Islands
- `142`: Hannibal Ad Portas
- `143`: The World as Larder
- `144`: The Burned Ledgers

Text research lives in `docs/super_events/014_cannibalism_super_event_research.md`. Audio source, final OGGs, and converted WAV sound-effect assets live under `music/super_events/014_cannibalism/` and `sound/`.

## Achievements

Event 014 achievements are registered in `common/achievements/chaos_redux_achievements.txt`, localised in `localisation/english/014_cannibalism_l_english.yml`, and wired in `interface/chaosx_achievements.gfx`.

- `014_cannibalism_clean_mess`
- `014_cannibalism_no_second_table`
- `014_cannibalism_silent_island`
- `014_cannibalism_do_not_feed_the_front`
- `014_cannibalism_trial_without_panic`
- `014_cannibalism_black_larder`
- `014_cannibalism_last_ship_home`
- `014_cannibalism_burn_the_cookbooks`
- `014_cannibalism_hunger_of_hannibal`
- `014_cannibalism_the_living_are_not_cattle`
- `014_cannibalism_empty_larder`
- `014_cannibalism_table_for_one`
- `014_cannibalism_after_the_feast`

Achievement gates match the matrix requirements: `Clean Mess` remains blocked by secrecy or any exploitation use; `No Second Table` is awarded to countries that contained their own outbreak and then survive the defeated commune without losing their capital to it; `Do Not Feed the Front` requires a major at war using the logistics posture without harsh military police or exploitation; `Black Larder` requires exploitation followed by successful terror-unit dismantling before defection or the Hannibal network; `Last Ship Home` requires the naval evacuation route; `Burn the Cookbooks` counts ritual archives destroyed in three different countries without exploitation; `Hunger of Hannibal` requires the Hannibal-linked commune or accepted unifier country plus enough network strength, cult nodes, and communes before the world-end route begins; `After the Feast` requires defeating the Hannibal-linked or global-table threat and completing the paid aftermath cleanup decision before world-end starts.

## Asset Wiring

Runtime sprite registry: `interface/014_cannibalism.gfx`.

Imagegen source, processed PNGs, contact sheets, static icon packages, animation frames, static animation fallbacks, final DDS/TGA files, and subagent handoffs live under `docs/assets/014_cannibalism/`, `docs/plans/014_cannibalism_plans/subagent_handoffs/`, and `gfx/`.

Primary source manifests:

- `docs/assets/014_cannibalism/manifest.md`
- `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`
- `docs/assets/014_cannibalism/static_icons_imagegen/decision_idea/manifest.md`
- `docs/assets/014_cannibalism/static_icons_imagegen/ideas/manifest.json`
- `docs/assets/014_cannibalism/static_icons_imagegen/achievements/manifest.md`
- `docs/assets/014_cannibalism/static_icons_imagegen/focuses_core_opening/manifest.md`
- `docs/assets/014_cannibalism/static_icons_imagegen/focuses_command_military/validation/focuses_command_military_validation.tsv`
- `docs/assets/014_cannibalism/static_icons_imagegen/focuses_islands_pact_last_table/manifest.md`
- `docs/assets/014_cannibalism/animations_imagegen/`

Event pictures:

- `GFX_news_cannibalism`
- `GFX_report_event_cannibalism`
- `GFX_report_event_cannibalism_spread`
- `GFX_report_event_cannibalism_contained`
- `GFX_report_event_cannibalism_failure`
- `GFX_report_event_cannibalism_ritual`
- `GFX_report_event_cannibalism_islands`
- `GFX_report_event_cannibalism_network`
- `GFX_report_event_cannibalism_hannibal_hook`
- `GFX_report_event_cannibalism_commune`
- `GFX_report_event_cannibalism_world_end`
- `GFX_report_event_cannibalism_defeat`

Decision and category sprites:

- `GFX_decision_category_cannibalism_frontline_hunger`
- `GFX_decision_cat_picture_cannibalism_frontline_hunger`
- `GFX_decision_cannibalism_field_kitchens`
- `GFX_decision_cannibalism_rotate_units`
- `GFX_decision_cannibalism_ration_convoy`
- `GFX_decision_cannibalism_hospital_audit`
- `GFX_decision_cannibalism_military_police`
- `GFX_decision_cannibalism_prison_freeze`
- `GFX_decision_cannibalism_chaplain_work`
- `GFX_decision_cannibalism_truth_commission`
- `GFX_decision_cannibalism_island_inspection`
- `GFX_decision_cannibalism_emergency_evacuation`
- `GFX_decision_cannibalism_break_ritual_cell`
- `GFX_decision_cannibalism_retake_commune`
- `GFX_decision_cannibalism_stop_copying`
- `GFX_decision_cannibalism_dismantle_terror`
- `GFX_decision_cannibalism_exploit_terror`
- `GFX_decision_cannibalism_break_cult`
- `GFX_decision_cannibalism_world_end_route`
- `GFX_decision_cannibalism_containment_deadline`
- `GFX_decision_cannibalism_cbl_last_table_map`
- `GFX_decision_cannibalism_cbl_region_project`
- `GFX_decision_cannibalism_cbl_pact_courier`
- `GFX_decision_cannibalism_cbl_solitary_raid`

Ideas, modifiers, and focus sprites:

- `GFX_idea_cannibalism_field_disappearances`
- `GFX_idea_cannibalism_ritual_hunger`
- `GFX_idea_cannibalism_public_truth`
- `GFX_idea_cannibalism_exploitation_scandal`
- `GFX_idea_cannibalism_commune_country`
- `GFX_idea_cannibalism_last_table`
- `GFX_idea_cannibalism_night_transfer_zone`
- `GFX_idea_cannibalism_empty_village_reports`
- `GFX_idea_cannibalism_silent_garrison`
- `GFX_idea_cannibalism_commune`
- `GFX_idea_cannibalism_hunting_ground`
- `GFX_idea_cannibalism_council_obedience`
- `GFX_idea_cannibalism_warlord_kitchen`
- `GFX_idea_cannibalism_hannibal_discipline`
- `GFX_idea_cannibalism_scavenger_logistics`
- `GFX_idea_cannibalism_pact_couriers`
- `GFX_idea_cannibalism_solitary_rampage`
- `GFX_idea_cannibalism_last_table_integration`
- `GFX_goal_cannibalism_first_table`
- `GFX_goal_cannibalism_origin_state`
- `GFX_goal_cannibalism_larder_columns`
- `GFX_goal_cannibalism_black_kitchens`
- `GFX_goal_cannibalism_port_harvests`
- `GFX_goal_cannibalism_ration_codes`
- `GFX_goal_cannibalism_empty_larder`
- `GFX_goal_cannibalism_hunting_ground`
- `GFX_goal_cannibalism_couriers`
- `GFX_goal_cannibalism_table_for_one`
- `GFX_goal_cannibalism_hannibal_hook`
- `GFX_goal_cannibalism_last_table`
- `GFX_goal_cannibalism_restrained_war`
- `GFX_goal_cannibalism_world_larder`
- `GFX_goal_cannibalism_council_knives`
- `GFX_goal_cannibalism_warlord_kitchen`
- `GFX_goal_cannibalism_hannibal_discipline`
- `GFX_goal_cannibalism_depot_inventory`
- `GFX_goal_cannibalism_field_kitchen_conversions`
- `GFX_goal_cannibalism_prisoner_ledger`
- `GFX_goal_cannibalism_hunger_columns`
- `GFX_goal_cannibalism_scavenger_parties`
- `GFX_goal_cannibalism_butcher_packs`
- `GFX_goal_cannibalism_prison_processions`
- `GFX_goal_cannibalism_hannibal_cadres`
- `GFX_goal_cannibalism_island_anchorages`
- `GFX_goal_cannibalism_convoy_ambush`
- `GFX_goal_cannibalism_coastal_port_lists`
- `GFX_goal_cannibalism_prison_roads`
- `GFX_goal_cannibalism_rail_corridors`
- `GFX_goal_cannibalism_mainland_corridors`
- `GFX_goal_cannibalism_restrained_registers`
- `GFX_goal_cannibalism_runaway_accounts`
- `GFX_goal_cannibalism_pact_compact`
- `GFX_goal_cannibalism_last_table_preparations`
- `GFX_goal_cannibalism_map_larder`
- `GFX_goal_cannibalism_region_projects`

Super-event, portrait, and animation sprites:

- `GFX_super_event_cannibalism_islands`
- `GFX_super_event_cannibalism_network`
- `GFX_super_event_cannibalism_world_end`
- `GFX_super_event_cannibalism_defeat`
- `GFX_portrait_CBL_table_council`
- `GFX_portrait_CBL_warlord`
- `GFX_portrait_CBL_hannibal`
- `GFX_cannibalism_frontline_hunger_seal_static`
- `GFX_cannibalism_frontline_hunger_seal_animated`
- `GFX_cannibalism_cult_pressure_warning_static`
- `GFX_cannibalism_cult_pressure_warning_animated`
- `GFX_cannibalism_island_signal_card_static`
- `GFX_cannibalism_island_signal_card_animated`
- `GFX_cannibalism_hannibal_resonance_seal_static`
- `GFX_cannibalism_hannibal_resonance_seal_animated`
- `GFX_cannibalism_council_portrait_overlay_static`
- `GFX_cannibalism_council_portrait_overlay_animated`
- `GFX_cannibalism_world_end_progress_border_static`
- `GFX_cannibalism_world_end_progress_border_animated`

## Spreadsheet Alignment

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` row 15 records Event 014 as implemented, with Minor Fire-Once type, local containment details, Evolutions I-III, and the world-end gate.

## Future Plans

- Add the future Hannibal actor package once the accepted Hannibal design exists.
- Add optional scripted GUI panels for outbreak meters if repeated live testing shows the decision category needs a denser dashboard.
- Add regional or cultural incident variants for named mission targets when there is enough source material to make them specific.
- Add a larger sanctions or isolation route if exploitation becomes a repeatable post-Hannibal diplomatic system.

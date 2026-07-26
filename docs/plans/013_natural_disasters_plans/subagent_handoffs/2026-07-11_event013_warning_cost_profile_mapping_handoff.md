# Event 013 warning cost-profile mapping handoff

> **Historical mapping handoff — implementation closed.** The eight warning cost profiles and their 75 family-specific decisions are implemented and reaudited. The “remaining risks” below preserve the pre-implementation review context; current runtime caveats are tracked only in the final Event 013 audit and live scenario matrix.

Date: 2026-07-11

Mode: bounded read-only analysis. No gameplay, localisation, GUI, GFX, asset, or spreadsheet file was edited.

## Outcome

`common/decisions/013_natural_disasters_decisions.txt` contains exactly 75 `natural_disaster_warn_*` decisions, three for each of the 25 implemented disaster families. Every identifier is mapped below to one of the eight requested cost profiles:

- `air`: 9
- `naval_coast`: 6
- `command_rail`: 10
- `civilian_shutdown`: 11
- `shelter_medical`: 9
- `transport`: 12
- `fuel_convoy`: 6
- `field_research`: 12

The mapping total is 75, and every warning decision identifier appears exactly once.

The current implementation uses only three flat warning packages, `field_teams`, `transport`, and `shelter`. The proposed map separates what the country is physically doing. It also removes the current silent resource substitutions, where support equipment falls back to trucks and trains fall back to convoys according to stockpile availability. Those substitutions do not fit many decision wordings and count as unapproved fallbacks under `AGENTS.md`.

## Sources consulted

### Repository instructions and skills

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`

### Offline Paradox wiki snapshot

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Equipment modding - Hearts of Iron 4 Wiki.md`

### Vanilla documentation and precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/HUN.txt`, for available civilian factory gates and active `civilian_factory_use` burdens
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/ARG.txt`, for construction projects that gate and occupy civilian factories
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/NOR.txt`, for paired convoy and command-power gates and real stockpile deductions
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/CZE.txt`, for train stockpile effects
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/INS.txt`, for train stockpile-aware AI weighting
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AUS.txt`, for equipment custom-cost presentation

### Event 013 sources

- `common/decisions/013_natural_disasters_decisions.txt`
- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml`, read only to compare the actual action wording with protection semantics
- `docs/specs/013_natural_disasters_specs/README.md`
- `docs/specs/013_natural_disasters_specs/manifest.md`
- `docs/specs/013_natural_disasters_specs/docs_alignment/013_source_of_truth_and_disposition_map.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md`

## Shared dynamic-cost contract

The profile name must select a real gate, visible cost string, payment helper, and AI affordability rule. It must not be a cosmetic label over the same generic package.

1. Compute each target's warning costs from script constants and live context. Relevant inputs are disaster severity, warning lead time, target asset value, target population or industry, war state, country capacity, active warning count, and the route type actually used.
2. Store or recompute the same values for `custom_cost_trigger`, scripted cost localisation, `complete_effect`, and `ai_will_do`. A displayed custom cost does not deduct anything by itself.
3. Integral gates that use strict `>` must use an inclusive gate value one unit below the real deduction, matching the repository's existing `natural_disaster_cost_gate` convention. Stability, war support, and command power need matching floors so a payment cannot overdraw them.
4. Negate dynamic payment variables with `multiply_temp_variable` before calling `add_manpower`, `add_equipment_to_stockpile`, `add_fuel`, `add_command_power`, `add_stability`, or `add_war_support`. Do not use unary minus on variable tokens.
5. Equipment type is part of the action contract. Firebreak and sandbag actions can select infantry and support equipment. Airfield actions should use ground-service equipment and fuel, not destroy aircraft as a cost. Evacuations should use motorized equipment. Rail actions should use trains. Coastal actions should use convoys.
6. A route using trains or convoys must choose its route from geography and access before the affordability check. It must show that selected route in the cost. It must not switch to the other resource merely because the country lacks the intended one.
7. Civilian capacity is a duration cost. Gate it with `num_of_civilian_factories_available_for_projects`, then occupy civilian factories with a supported decision modifier or an equivalent timed burden for the warning lock. A one-frame trigger followed by no burden is not a payment.
8. Each new cost key needs the base, `_blocked`, and `_tooltip` localisation forms. The profile keys should be separate, for example `natural_disaster_cost_warning_air` and `natural_disaster_cost_warning_air_blocked`.
9. AI weights must go to zero when the selected profile is unaffordable. The existing strategic state modifiers can still raise priority after the affordability check.

## Cost-profile definitions

The resource rows below describe the core package. Action-specific equipment selection is allowed inside a profile when the mini-spec names it, but silent affordability substitutions are not.

| Profile | Required dynamic gate and payment | Conditional burden or sacrifice | Main scaling inputs |
| --- | --- | --- | --- |
| `air` | Manpower for ground crews, support or motorized equipment, fuel, and conservative command power. Deduct all four through the matching payment helper. | At severe or abnormal scale, apply temporary air-operation disruption. If war support is used for a wartime shutdown, gate and deduct the same dynamic amount. | Airbase level, industrial value, severity, warning lead time, and war state. |
| `naval_coast` | Manpower, convoys, fuel, and conservative command power. Convoys are mandatory for port and quay actions. | Port or dockyard work can add a short civilian factory burden. A public coastal withdrawal can add a stability cost. | Naval base, dockyard and port value, island dependence, coastal population, severity, and war state. |
| `command_rail` | Manpower, trains, fuel, support equipment, and conservative command power. Rail and pass closures pay for the trains they remove from service. | Wartime rail standdowns or formation rotations can use a small war-support cost or a visible temporary supply-readiness burden. | Rail and supply-hub importance, capital connection, active front supply, severity, and war state. |
| `civilian_shutdown` | Available civilian factories, manpower, and the specified support or infantry equipment. Apply a real construction or consumer burden for the warning lock. | Gate and deduct stability when neighborhoods or workplaces are closed. War support can be added only for a visible wartime production shutdown. | Civilian and military factory count in the target, population density, project duration, severity, and concurrent civilian burdens. |
| `shelter_medical` | Manpower, support equipment, and a stability floor. Deduct manpower, equipment, and the displayed stability strain. | Dense, severe, or abnormal shelter actions can occupy civilian factories for the warning lock. Medical distribution can require motorized equipment when the action text names vehicles. | Population density, current death vulnerability, disease or exposure risk, severity, and existing shelter pressure. |
| `transport` | Manpower, motorized equipment, fuel, and stability. Deduct the exact truck, fuel, manpower, and stability amounts shown. | A military evacuation can add conservative command power. Do not add trains or convoys unless the identifier is moved to a route-specific profile. | Population moved, path or valley exposure, severity, road and infrastructure state, and war state. |
| `fuel_convoy` | Fuel plus one preselected logistics mode, either trains for an inland rail route or convoys for a valid coastal route. Add support equipment when the mini-spec requires protected stores or pumps. | Food, water, or ration movement can occupy civilian factories and impose stability or wartime war-support strain. | Route mode, port or rail access, population need, food or water risk, severity, and country import dependence. |
| `field_research` | Manpower, support equipment, conservative command power, and a light civilian research or communications burden. | Mobile fire or observer lines can add motorized equipment or fuel only when named by the mini-spec. Firebreak and perimeter variants can select infantry equipment. | Forecast area, number of path states, abnormal-family status, terrain, severity, and warning lead time. |

## Exact decision-to-profile mapping

`Effective protection` is the value used by impact logic. For the first decision in each family, it is inferred later by `natural_disaster_prepare_warning_route_profile`. For the secondary and tertiary decisions, it is written immediately by `natural_disaster_apply_warning_direction`.

| Family | Exact decision identifier | Cost profile | Effective protection |
| --- | --- | --- | --- |
| Earthquake | `natural_disaster_warn_earthquake_rail_crews` | `command_rail` | `transport` |
| Earthquake | `natural_disaster_warn_earthquake_open_squares` | `transport` | `population` |
| Earthquake | `natural_disaster_warn_earthquake_port_withdrawal_watch` | `naval_coast` | `coast` |
| Flood | `natural_disaster_warn_flood_move_rolling_stock` | `command_rail` | `transport` |
| Flood | `natural_disaster_warn_flood_raise_embankments` | `civilian_shutdown` | `transport` |
| Flood | `natural_disaster_warn_flood_clean_water_stores` | `shelter_medical` | `medical` |
| Tropical cyclone | `natural_disaster_warn_tropical_cyclone_close_ports` | `naval_coast` | `coast` |
| Tropical cyclone | `natural_disaster_warn_tropical_cyclone_disperse_aircraft` | `air` | `industry_air` |
| Tropical cyclone | `natural_disaster_warn_tropical_cyclone_coastal_evacuation` | `transport` | `population` |
| Extreme wind | `natural_disaster_warn_extreme_wind_pause_trains` | `command_rail` | `transport` |
| Extreme wind | `natural_disaster_warn_extreme_wind_anchor_aircraft` | `air` | `industry_air` |
| Extreme wind | `natural_disaster_warn_extreme_wind_secure_roofs` | `civilian_shutdown` | `population` |
| Tornado outbreak | `natural_disaster_warn_tornado_outbreak_shelter_belt` | `shelter_medical` | `population` |
| Tornado outbreak | `natural_disaster_warn_tornado_outbreak_spotter_line` | `field_research` | `medical` |
| Tornado outbreak | `natural_disaster_warn_tornado_outbreak_clear_airfields` | `air` | `industry_air` |
| Thunderstorm | `natural_disaster_warn_thunderstorm_lightning_patrol` | `field_research` | `fire` |
| Thunderstorm | `natural_disaster_warn_thunderstorm_ground_aircraft` | `air` | `industry_air` |
| Thunderstorm | `natural_disaster_warn_thunderstorm_drainage_crews` | `civilian_shutdown` | `transport` |
| Hailstorm | `natural_disaster_warn_hailstorm_cover_aircraft` | `air` | `industry_air` |
| Hailstorm | `natural_disaster_warn_hailstorm_cover_depots` | `civilian_shutdown` | `industry_air` |
| Hailstorm | `natural_disaster_warn_hailstorm_food_reserve` | `fuel_convoy` | `food_water` |
| Blizzard | `natural_disaster_warn_blizzard_fuel_corridor` | `fuel_convoy` | `transport` |
| Blizzard | `natural_disaster_warn_blizzard_rail_snow_crews` | `command_rail` | `transport` |
| Blizzard | `natural_disaster_warn_blizzard_winter_shelter` | `shelter_medical` | `population` |
| Cold wave | `natural_disaster_warn_cold_wave_heat_shelters` | `shelter_medical` | `population` |
| Cold wave | `natural_disaster_warn_cold_wave_protect_water_lines` | `civilian_shutdown` | `food_water` |
| Cold wave | `natural_disaster_warn_cold_wave_frontline_rotation` | `command_rail` | `population` |
| Heat wave | `natural_disaster_warn_heat_wave_water_points` | `fuel_convoy` | `food_water` |
| Heat wave | `natural_disaster_warn_heat_wave_shift_work_hours` | `civilian_shutdown` | `population` |
| Heat wave | `natural_disaster_warn_heat_wave_fire_watch` | `field_research` | `fire` |
| Drought | `natural_disaster_warn_drought_water_trains` | `fuel_convoy` | `transport` |
| Drought | `natural_disaster_warn_drought_crop_salvage` | `transport` | `food_water` |
| Drought | `natural_disaster_warn_drought_firebreaks` | `field_research` | `fire` |
| Dust and sandstorm | `natural_disaster_warn_dust_and_sandstorm_convoy_spacing` | `fuel_convoy` | `transport` |
| Dust and sandstorm | `natural_disaster_warn_dust_and_sandstorm_seal_airfields` | `air` | `industry_air` |
| Dust and sandstorm | `natural_disaster_warn_dust_and_sandstorm_cover_water_stores` | `shelter_medical` | `food_water` |
| Wildfire | `natural_disaster_warn_wildfire_firebreaks` | `field_research` | `fire` |
| Wildfire | `natural_disaster_warn_wildfire_evacuation_columns` | `transport` | `population` |
| Wildfire | `natural_disaster_warn_wildfire_protect_power_lines` | `civilian_shutdown` | `industry_air` |
| Dry mass movement | `natural_disaster_warn_dry_mass_movement_slope_watch` | `field_research` | `transport` |
| Dry mass movement | `natural_disaster_warn_dry_mass_movement_pass_closure` | `command_rail` | `transport` |
| Dry mass movement | `natural_disaster_warn_dry_mass_movement_mine_evacuation` | `transport` | `population` |
| Wet mass movement | `natural_disaster_warn_wet_mass_movement_valley_evacuation` | `transport` | `population` |
| Wet mass movement | `natural_disaster_warn_wet_mass_movement_bridge_watch` | `command_rail` | `transport` |
| Wet mass movement | `natural_disaster_warn_wet_mass_movement_channel_clearance` | `civilian_shutdown` | `medical` |
| Volcanic eruption | `natural_disaster_warn_volcanic_eruption_exclusion_zone` | `transport` | `population` |
| Volcanic eruption | `natural_disaster_warn_volcanic_eruption_observatory_watch` | `field_research` | `industry_air` |
| Volcanic eruption | `natural_disaster_warn_volcanic_eruption_ash_airfield_closure` | `air` | `industry_air` |
| Ashfall | `natural_disaster_warn_ashfall_cover_machinery` | `civilian_shutdown` | `industry_air` |
| Ashfall | `natural_disaster_warn_ashfall_ground_air_traffic` | `air` | `industry_air` |
| Ashfall | `natural_disaster_warn_ashfall_cover_food_and_water` | `shelter_medical` | `food_water` |
| Lahar | `natural_disaster_warn_lahar_valley_sirens` | `shelter_medical` | `population` |
| Lahar | `natural_disaster_warn_lahar_bridge_cordon` | `command_rail` | `transport` |
| Lahar | `natural_disaster_warn_lahar_channel_clearance` | `civilian_shutdown` | `medical` |
| Tsunami | `natural_disaster_warn_tsunami_inland_corridors` | `transport` | `transport` |
| Tsunami | `natural_disaster_warn_tsunami_coast_withdrawal_alarm` | `naval_coast` | `coast` |
| Tsunami | `natural_disaster_warn_tsunami_close_quays` | `naval_coast` | `coast` |
| Storm surge | `natural_disaster_warn_storm_surge_sandbag_low_roads` | `civilian_shutdown` | `transport` |
| Storm surge | `natural_disaster_warn_storm_surge_quay_closure` | `naval_coast` | `coast` |
| Storm surge | `natural_disaster_warn_storm_surge_evacuate_marsh_edge` | `transport` | `population` |
| Meteor impact | `natural_disaster_warn_meteor_impact_crater_evacuation` | `transport` | `population` |
| Meteor impact | `natural_disaster_warn_meteor_impact_observatory_tracking` | `field_research` | `industry_air` |
| Meteor impact | `natural_disaster_warn_meteor_impact_fire_perimeter` | `field_research` | `fire` |
| Meteor shower | `natural_disaster_warn_meteor_shower_shelter_lights_out` | `shelter_medical` | `population` |
| Meteor shower | `natural_disaster_warn_meteor_shower_observer_net` | `field_research` | `industry_air` |
| Meteor shower | `natural_disaster_warn_meteor_shower_fire_patrols` | `field_research` | `fire` |
| Whole-earth rupture | `natural_disaster_warn_whole_earth_rupture_rail_standdown` | `command_rail` | `transport` |
| Whole-earth rupture | `natural_disaster_warn_whole_earth_rupture_coastal_tide_watch` | `naval_coast` | `coast` |
| Whole-earth rupture | `natural_disaster_warn_whole_earth_rupture_regional_triage` | `shelter_medical` | `medical` |
| Massive eruption | `natural_disaster_warn_massive_eruption_food_corridors` | `fuel_convoy` | `food_water` |
| Massive eruption | `natural_disaster_warn_massive_eruption_exclusion_ring` | `transport` | `population` |
| Massive eruption | `natural_disaster_warn_massive_eruption_air_shutdown` | `air` | `industry_air` |
| Moving storm corridor | `natural_disaster_warn_moving_storm_corridor_rail_reroute` | `command_rail` | `transport` |
| Moving storm corridor | `natural_disaster_warn_moving_storm_corridor_path_forecast` | `field_research` | `industry_air` |
| Moving storm corridor | `natural_disaster_warn_moving_storm_corridor_layered_evacuation` | `transport` | `population` |

## Protection-variable audit

Protection is mechanically important. `transport`, `industry_air`, `coast`, and `fire` reduce material damage. `population`, `food_water`, `coast`, and `medical` reduce deaths. Protection also decides whether the selected warning weakens the resolved follow-up chain.

### Clear wording-to-protection mismatches

| Decision | Current protection | Why it does not fit | Recommended disposition |
| --- | --- | --- | --- |
| `natural_disaster_warn_meteor_impact_observatory_tracking` | `industry_air` | The title and description track the object and sharpen the impact warning. They do not claim direct protection of industry or airfields. The current value grants material protection and only matches supply-collapse or wildfire chains. | Add an explicit forecast protection behavior, or intentionally map the result to `population` if the designed benefit is warning-led evacuation. Do not leave it as `industry_air` without rewriting the action into a physical airfield-protection measure. |
| `natural_disaster_warn_moving_storm_corridor_path_forecast` | `industry_air` | The action publishes the path and identifies the next threatened state. `industry_air` records a material-protection operation that the wording does not describe. | Add an explicit forecast protection behavior, or deliberately map it to `population` if forecast time is meant to reduce deaths. |

### Mixed or underfit records that need an explicit parent choice

| Decision | Current protection | Conflict | Safer direction |
| --- | --- | --- | --- |
| `natural_disaster_warn_tornado_outbreak_spotter_line` | `medical` | The action is primarily observation and path forecasting. Medical teams and triage appear only as a secondary benefit. | Prefer a forecast behavior. If no new behavior is approved, `population` better represents earlier shelter time than `medical`. |
| `natural_disaster_warn_volcanic_eruption_observatory_watch` | `industry_air` | The mini-spec says the observatory improves warning. Current localisation adds airfield protection, producing a mixed research and material action. | Keep `industry_air` only if the action is explicitly an airfield-protection watch. Otherwise use forecast behavior and let the separate ash-airfield closure own `industry_air`. |
| `natural_disaster_warn_meteor_shower_observer_net` | `industry_air` | The observer net tracks fragments. Its localisation also mentions runways and rescue corridors, so the current value only covers part of the action. | Prefer forecast behavior. If direct runway protection remains the intended effect, make that physical work explicit and keep `industry_air`. |
| `natural_disaster_warn_drought_water_trains` | `transport` | The mini-spec says the action reduces deaths and food pressure. `transport` protects material damage and does not match famine or disease. | `food_water` is the closer protection value. The cost remains `fuel_convoy`. |
| `natural_disaster_warn_tsunami_inland_corridors` | `transport` | The mini-spec says the corridors reduce refugee and death pressure. `transport` protects material damage, although it can match refugee pressure. | `population` is the closer direct-death protection. `coast` is also defensible if port and wave protection remain bundled. |
| `natural_disaster_warn_wet_mass_movement_channel_clearance` | `medical` | Clearing channels is physical flow and transport protection. Disease reduction is a secondary outcome. | Use `transport` for flood and route protection, or `food_water` if contaminated water is the primary outcome. |
| `natural_disaster_warn_lahar_channel_clearance` | `medical` | The mini-spec says channel clearance reduces repeat flow and flood chains. `medical` only represents contaminated-water consequences. | Use `transport` for physical channel and bridge protection, or `food_water` if water contamination is primary. |
| `natural_disaster_warn_extreme_wind_secure_roofs` | `population` | Current localisation emphasizes trapped civilians, while the stronger deep mini-spec says the action protects factories and infrastructure. | Choose one source direction. Keep `population` only with the current shelter wording. Use `industry_air` if the mini-spec's material protection is authoritative. |

All other warning wordings fit their effective protection closely enough for the current seven-value protection model.

### Primary-choice timing risk

The first warning decision for every family does not write `natural_disaster_warning_choice` or `natural_disaster_warning_protection` when clicked. It sets the generic action flag and preparation score. `natural_disaster_prepare_warning_route_profile` later infers `primary` and the family-specific protection at impact time.

Impact mitigation therefore receives the intended primary protection on the inspected impact paths. Any warning-phase GUI, history snapshot, tooltip, or scripted localisation read between the click and impact can still observe `none`. The implementation pass should either write the primary choice and protection immediately through the same shared direction helper or prove that no warning-phase surface reads those variables.

## Suggested implementation surfaces for the parent

No shared implementation file was changed by this analysis. A future patch should expect to touch these surfaces together:

- `common/script_constants/013_natural_disasters_constants.txt`, for eight profile IDs, resource bases, scaling factors, floors, caps, and exact gate mirrors
- `common/scripted_triggers/013_natural_disasters_triggers.txt`, for eight affordability helpers that use the computed profile and route
- `common/scripted_effects/013_natural_disasters_effects.txt`, for cost calculation, exact payment helpers, primary-choice recording, and any approved forecast protection behavior
- `common/decisions/013_natural_disasters_decisions.txt`, for each identifier's profile, cost key, gate, payment, burden duration, and AI affordability block
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`, for dynamic icon-first cost rendering
- `localisation/english/013_natural_disasters_l_english.yml`, for eight cost keys plus blocked and tooltip forms, and any wording changed to resolve protection conflicts
- `common/ideas/013_natural_disasters_ideas.txt` only if civilian burdens use timed ideas instead of supported active-decision modifiers

Suggested helper family, subject to parent naming review:

- `natural_disaster_prepare_warning_profile_costs`
- `natural_disaster_can_pay_warning_air`
- `natural_disaster_can_pay_warning_naval_coast`
- `natural_disaster_can_pay_warning_command_rail`
- `natural_disaster_can_pay_warning_civilian_shutdown`
- `natural_disaster_can_pay_warning_shelter_medical`
- `natural_disaster_can_pay_warning_transport`
- `natural_disaster_can_pay_warning_fuel_convoy`
- `natural_disaster_can_pay_warning_field_research`
- matching `natural_disaster_pay_warning_*` effects

## Meaningful validation

- Extracted 75 warning decision blocks from the live decision file.
- Verified 75 unique mapping entries, with no missing or extra identifiers.
- Compared every identifier and its final player-facing action wording with the stronger Part 8 family mini-spec.
- Resolved all 25 primary protection values through the impact-time family mapping rather than reporting them as `none`.
- Confirmed that the current three custom costs are flat script-constant packages and that their payment effects silently substitute equipment or transport modes.
- Confirmed from official documentation and vanilla precedents that custom cost text does not pay resources, negative `add_equipment_to_stockpile` removes equipment, fuel and manpower have direct gates and effects, and civilian factory commitments can be represented by an available-factory gate plus an active decision burden.

## Remaining risks and required decisions

1. Forecasting has no dedicated protection value. The parent must decide whether to add one or deliberately translate forecast benefits into an existing death or material category. Silently treating forecast as `industry_air` is not supported by the wording.
2. Civilian burden can overlap across several warning states. A single non-stackable timed idea could undercharge concurrent warnings. The chosen burden implementation must preserve concurrent costs.
3. `fuel_convoy` needs deterministic route selection and readable cost text. An affordability-driven train or convoy substitution would preserve the current fallback problem.
4. The eight profiles need capacity scaling so weak countries retain at least one useful, affordable warning response without making large countries pay trivial costs.
5. Dynamic cost values must be computed identically for UI, gate, payment, and AI. Recomputing from different scopes can create a displayed-cost mismatch in targeted decisions.
6. Several actions have two claimed protection outcomes. The mixed records listed above need an explicit content choice before code changes so protection, localisation, and the mini-spec remain aligned.

## Files changed

- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-11_event013_warning_cost_profile_mapping_handoff.md`

No simplifications or identifier omissions were made in the mapping. The unresolved protection choices are reported explicitly rather than replaced with fallback assumptions.

# Event 013 Decision and Mission Handoff

## Scope

This tranche implements the player-facing warning, aftermath recovery, mission-slot, and foreign-relief gameplay surface for Event 013. It is intentionally isolated from the shared Event 013 engine, localisation, interface, assets, events, and specification files.

Files created:

- `common/decisions/categories/013_natural_disasters_categories.txt`
- `common/decisions/013_natural_disasters_decisions.txt`
- `common/ideas/013_natural_disasters_ideas.txt`
- `docs/plans/013_natural_disasters_plans/013_decision_mission_handoff.md`

No existing files were edited by this tranche. No fallback content was added.

## Implemented Surface

The aftermath category exposes a staged response tied to the live Event 013 warning and aftermath-card state. Family warning decisions spend physical resources before impact. Rescue, stabilization, and reconstruction decisions spend manpower, equipment, fuel, political power, stability, or war support while advancing the engine-owned score variables. Timed missions cap the available response window and distinguish full success, partial response, failure, and cleanup.

Foreign relief is deliberately expensive. Four state-targeted donor variants transfer a bounded package to one eligible affected neighbor or faction member. The recipient must route or refuse the shipment before the inbound mission expires. Donors pay manpower, equipment, convoys, fuel, stability, war support, and a timed consumer-goods burden.

## Categories and Ideas

Category identifiers:

- `natural_disaster_aftermath_category`
- `natural_disaster_foreign_relief_category`

Idea identifiers:

- `natural_disaster_aftermath_idea`
- `natural_disaster_outbound_relief_burden`

`natural_disaster_aftermath_idea` supplies the country-level reconstruction burden referenced by the existing Event 013 engine. `natural_disaster_outbound_relief_burden` represents the temporary economic cost borne by a donor and clears `natural_disaster_outbound_relief_active` when it expires.

## Warning Decision Identifiers

Each warning is state-targeted, checks the exact scheduled family, spends a family-appropriate physical package, records a timed state action flag, sets `natural_disaster_warning_action_taken`, and adds to `natural_disaster_preparation_score`.

- `natural_disaster_warn_earthquake_rail_crews`
- `natural_disaster_warn_flood_move_rolling_stock`
- `natural_disaster_warn_tropical_cyclone_close_ports`
- `natural_disaster_warn_extreme_wind_pause_trains`
- `natural_disaster_warn_tornado_outbreak_shelter_belt`
- `natural_disaster_warn_thunderstorm_lightning_patrol`
- `natural_disaster_warn_hailstorm_cover_aircraft`
- `natural_disaster_warn_blizzard_fuel_corridor`
- `natural_disaster_warn_cold_wave_heat_shelters`
- `natural_disaster_warn_heat_wave_water_points`
- `natural_disaster_warn_drought_water_trains`
- `natural_disaster_warn_dust_and_sandstorm_convoy_spacing`
- `natural_disaster_warn_wildfire_firebreaks`
- `natural_disaster_warn_dry_mass_movement_slope_watch`
- `natural_disaster_warn_wet_mass_movement_valley_evacuation`
- `natural_disaster_warn_volcanic_eruption_exclusion_zone`
- `natural_disaster_warn_ashfall_cover_machinery`
- `natural_disaster_warn_lahar_valley_sirens`
- `natural_disaster_warn_tsunami_inland_corridors`
- `natural_disaster_warn_storm_surge_sandbag_low_roads`
- `natural_disaster_warn_meteor_impact_crater_evacuation`
- `natural_disaster_warn_meteor_shower_shelter_lights_out`
- `natural_disaster_warn_whole_earth_rupture_rail_standdown`
- `natural_disaster_warn_massive_eruption_food_corridors`
- `natural_disaster_warn_moving_storm_corridor_rail_reroute`

Warning packages fall into field, shelter, and transport families. They combine support equipment, motorized equipment, trains or convoys, fuel, and manpower according to the physical action described by the decision. AI weighting responds to family, capital exposure, population density, transport value, industrial value, coast access, and war status.

## Recovery Decision Identifiers

### Early Rescue

- `natural_disaster_rescue_search_teams`
- `natural_disaster_rescue_open_shelters`
- `natural_disaster_rescue_clear_one_route`
- `natural_disaster_rescue_emergency_evacuation`
- `natural_disaster_rescue_medical_triage`
- `natural_disaster_rescue_port_lifeline`

These actions add to `natural_disaster_rescue_score`. Their costs emphasize manpower, support equipment, trucks, trains or convoys, fuel, political power, stability, and war support.

### Middle Stabilization

- `natural_disaster_stabilize_clean_water`
- `natural_disaster_stabilize_restore_rail`
- `natural_disaster_stabilize_reopen_port`
- `natural_disaster_stabilize_secure_food`
- `natural_disaster_stabilize_factory_inspection`
- `natural_disaster_stabilize_chain_prevention`

These actions add to `natural_disaster_stabilization_score`. `natural_disaster_stabilize_chain_prevention` is available in the early or middle phase when the open card has chain risk. It clears the chain risk and contributes to the score appropriate to the current phase.

### Late Reconstruction

- `natural_disaster_reconstruct_resilient_rails`
- `natural_disaster_reconstruct_seismic_retrofit`
- `natural_disaster_reconstruct_coastal_barriers`
- `natural_disaster_reconstruct_firebreak_network`
- `natural_disaster_reconstruct_volcanic_exclusion_routes`
- `natural_disaster_reconstruct_water_security`
- `natural_disaster_reconstruct_crater_or_exclusion_cordon`
- `natural_disaster_reconstruct_weather_shelter_network`
- `natural_disaster_reconstruct_slope_stabilization`

These actions add two points to `natural_disaster_reconstruction_score` and record one persistent resilience flag:

- `natural_disaster_resilient_rails`
- `natural_disaster_seismic_retrofit`
- `natural_disaster_coastal_barriers`
- `natural_disaster_firebreak_network`
- `natural_disaster_volcanic_exclusion_routes`
- `natural_disaster_water_security`
- `natural_disaster_exclusion_cordon`
- `natural_disaster_weather_shelter_network`
- `natural_disaster_slope_stabilization`

## Mission Identifiers

The existing Event 013 engine activates these exact mission slots. They cannot self-activate.

Early rescue slots:

- `natural_disaster_rescue_mission_1`
- `natural_disaster_rescue_mission_2`
- `natural_disaster_rescue_mission_3`

Middle stabilization slots:

- `natural_disaster_stabilization_mission_1`
- `natural_disaster_stabilization_mission_2`

Late reconstruction slots:

- `natural_disaster_reconstruction_mission_1`
- `natural_disaster_reconstruction_mission_2`

Special slots:

- `natural_disaster_chain_mission`
- `natural_disaster_inbound_relief_mission`

Score thresholds use the shared Event 013 script constants. Successful slots set completion flags. Timed-out slots set partial or failure flags according to the accumulated phase score. Mission cancellation clears the mapped state variable and the mission-local transient state.

## Relief Identifiers

Recipient actions:

- `natural_disaster_route_inbound_relief`
- `natural_disaster_refuse_inbound_relief`

Donor variants:

- `natural_disaster_offer_neighbor_convoy_relief`
- `natural_disaster_offer_port_lifeline_relief`
- `natural_disaster_offer_engineer_relief`
- `natural_disaster_offer_medical_relief`

The recipient flow records `natural_disaster_inbound_relief_donor`, `natural_disaster_inbound_relief_target_state`, and the package type. Routing pays the recipient-side manpower, fuel, stability, or war-support cost and applies the package to the stored state. Refusal and mission timeout clear all relief targets and flags.

## Localisation Handoff

Localisation was outside this tranche. Every category, decision, mission, and idea identifier in this document needs a display key and description key in the Event 013 localisation file. Decision identifiers need the normal key plus `<identifier>_desc`. Category and idea identifiers also need their descriptions.

Custom-cost keys required by the implementation:

- `natural_disaster_cost_warning_field`
- `natural_disaster_cost_warning_field_blocked`
- `natural_disaster_cost_warning_field_tooltip`
- `natural_disaster_cost_warning_shelter`
- `natural_disaster_cost_warning_shelter_blocked`
- `natural_disaster_cost_warning_shelter_tooltip`
- `natural_disaster_cost_warning_transport`
- `natural_disaster_cost_warning_transport_blocked`
- `natural_disaster_cost_warning_transport_tooltip`
- `natural_disaster_cost_rescue_either`
- `natural_disaster_cost_rescue_either_blocked`
- `natural_disaster_cost_rescue_either_tooltip`
- `natural_disaster_cost_rescue_train`
- `natural_disaster_cost_rescue_train_blocked`
- `natural_disaster_cost_rescue_train_tooltip`
- `natural_disaster_cost_rescue_convoy`
- `natural_disaster_cost_rescue_convoy_blocked`
- `natural_disaster_cost_rescue_convoy_tooltip`
- `natural_disaster_cost_stabilization_either`
- `natural_disaster_cost_stabilization_either_blocked`
- `natural_disaster_cost_stabilization_either_tooltip`
- `natural_disaster_cost_stabilization_train`
- `natural_disaster_cost_stabilization_train_blocked`
- `natural_disaster_cost_stabilization_train_tooltip`
- `natural_disaster_cost_stabilization_convoy`
- `natural_disaster_cost_stabilization_convoy_blocked`
- `natural_disaster_cost_stabilization_convoy_tooltip`
- `natural_disaster_cost_reconstruction_either`
- `natural_disaster_cost_reconstruction_either_blocked`
- `natural_disaster_cost_reconstruction_either_tooltip`
- `natural_disaster_cost_reconstruction_train`
- `natural_disaster_cost_reconstruction_train_blocked`
- `natural_disaster_cost_reconstruction_train_tooltip`
- `natural_disaster_cost_reconstruction_convoy`
- `natural_disaster_cost_reconstruction_convoy_blocked`
- `natural_disaster_cost_reconstruction_convoy_tooltip`
- `natural_disaster_cost_inbound_relief_route`
- `natural_disaster_cost_inbound_relief_route_blocked`
- `natural_disaster_cost_inbound_relief_route_tooltip`
- `natural_disaster_cost_outbound_relief`
- `natural_disaster_cost_outbound_relief_blocked`
- `natural_disaster_cost_outbound_relief_tooltip`

The custom-cost localisation should state the actual equipment, manpower, fuel, stability, war-support, and political-power requirements. It must not describe implementation details.

## Shared Engine Integration Hooks

The following work belongs in the shared Event 013 engine and was not performed because this tranche was restricted to dedicated decision, category, idea, and handoff files.

### Cleanup Hook

Extend `natural_disaster_configure_scheduled_state` or `natural_disaster_close_aftermath_card` to clear stale engine-owned aftermath results before a state is reused. The shared engine currently leaves `natural_disaster_phase_partial`, `natural_disaster_phase_failed`, and `natural_disaster_reconstruction_partial` persistent. It should also clear stale relief notification state and `natural_disaster_aftermath_category_visible` when the country has no warning, open aftermath card, or inbound relief.

The action flags created in this tranche are timed. The inbound relief mission owns its own target and flag cleanup.

### Resilience Consumption Hook

Consume the nine reconstruction resilience flags in future disaster calculations. The likely insertion points are:

- `natural_disaster_prepare_family_profile`
- `natural_disaster_apply_family_building_damage`
- `natural_disaster_apply_population_loss`

Each resilience flag should reduce only its related hazard or exposure. The flags already record player investment, but the shared engine must apply the benefit before they alter a later disaster outcome.

### Priority Card Selector Hook

Add a reusable scripted effect such as `natural_disaster_select_priority_open_card`. It should choose the most urgent eligible state by severity, capital exposure, population density, transport value, industrial value, and chain due status. Replace the bounded `random_owned_state` recipient selection in these donor decisions:

- `natural_disaster_offer_neighbor_convoy_relief`
- `natural_disaster_offer_port_lifeline_relief`
- `natural_disaster_offer_engineer_relief`
- `natural_disaster_offer_medical_relief`

No existing priority-selector helper was available in the Event 013 engine.

### Donor Relationship Hook

Add a shared donor-response effect if Event 013 is intended to track dependence, influence, or diplomatic obligation. The decision surface stores the donor as `natural_disaster_inbound_relief_donor`, but no current Event 013 helper applies a donor-specific relationship result. Call the helper when `natural_disaster_route_inbound_relief` succeeds and clear the stored donor during normal mission cleanup.

The donor AI should also use a shared hostility and dependency eligibility trigger when the project defines one. The present donor actions remain limited to neighbors or faction members and are never free.

### Archetype-Safe Equipment Spending Hook

Add a reusable scripted effect for spending from equipment archetypes without assuming a specific equipment version. The decisions check support equipment, motorized equipment, trains, and convoys by archetype, but Clausewitz stockpile removal requires a concrete equipment type in the effect. The current effects use the common version-one tokens. Trains are the highest-risk case when a country primarily holds armored trains.

The helper should accept an archetype and amount, resolve a valid owned type, and remove that stockpile. Replace direct version-one deductions in warning, recovery, and outbound-relief actions once the helper exists.

### Notification Cleanup Hook

Clear `natural_disaster_aftermath_category_visible` when no live warning, aftermath card, or inbound relief remains. The category visibility in this tranche follows live state and does not depend on the notification flag, so stale notification state cannot hold the category open.

## Asset and Interface Handoff

Custom icons and interface work were outside this tranche. Decisions currently use standard decision presentation. Ideas use existing vanilla idea sprites:

- `GFX_idea_generic_civilian_industry`
- `GFX_idea_generic_foreign_capital`

If bespoke Event 013 decision art is approved later, keep the identifiers in this document stable and wire the new sprites in the Event 013 interface asset file.

## Validation Evidence

- The file contains exactly 25 family warning decisions.
- Mission capacity is exactly three rescue slots, two stabilization slots, two reconstruction slots, one chain slot, and one inbound-relief slot.
- Four outbound-relief variants and two recipient actions are present.
- Every mission identifier referenced by the existing Event 013 aftermath engine is defined.
- Every `constant:natural_disaster_*` reference resolves to the existing Event 013 script-constant table.
- Every referenced Event 013 scripted trigger is defined.
- Category, decision, and idea block structures close cleanly.
- No existing file was modified by this tranche.

No live-game validation was performed. Localisation, custom icons, priority target selection, resilience consumption, and donor-specific relationship effects remain shared-system follow-up work rather than hidden simplifications.

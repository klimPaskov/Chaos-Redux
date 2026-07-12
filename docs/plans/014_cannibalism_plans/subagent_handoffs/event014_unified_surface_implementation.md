# Event 014 Unified Surface Implementation Handoff

## Scope

This tranche implements the post-reveal CBL player-facing surface assigned by the parent:

- twenty unified route national spirits with centralized tuning
- title, description, and effect-tooltip localisation for all 108 unified focuses
- regular and shine sprite registrations for all 108 unified focus icons
- sprite registrations for all twenty unified route idea icons

It does not edit the unified focus tree, its scripted rewards, decisions, events, unification, world-end effects, pre-reveal content, or final DDS art.

## Files changed

- `common/script_constants/014_cannibalism_unified_route_idea_constants.txt`
- `common/ideas/014_cannibalism_ideas.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `interface/014_cannibalism.gfx`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_unified_surface_implementation.md`

## Unified route idea contract

All twenty ideas use `picture = <idea_id>`, permit civil-war inheritance, and are allowed only for the revealed ordinary CBL country:

```txt
is_cannibalism_unified_country = yes
has_global_flag = cannibalism_reveal_complete
NOT = { has_country_flag = cannibalism_wendigo_hannibal_country }
```

All 107 modifier values resolve through the global fixed-point category `cannibalism_unified_route_idea`. No owned modifier block contains a literal tuning value.

| Family | Route | Root idea | Capstone idea | Preserved tradeoff |
| --- | --- | --- | --- | --- |
| Disposition | Keep Lieutenants | `cannibalism_retained_lieutenants` | `cannibalism_council_of_retained_hosts` | stronger recovery, planning, and command depth for a growing political burden |
| Disposition | Break Warlords | `cannibalism_warlords_broken` | `cannibalism_authority_without_rivals` | direct political and military authority for instability, resistance, and officer replacement cost |
| Disposition | Chain Rivals | `cannibalism_rivals_in_chains` | `cannibalism_dominion_of_chains` | extraction and compliance for resistance and political supervision |
| Hierarchy | One Command | `cannibalism_one_command` | `cannibalism_single_operational_will` | planning, organization, and reinforcement for supply and political strain |
| Hierarchy | Many Jaws | `cannibalism_many_jaws` | `cannibalism_confederation_under_one_name` | army experience and command depth for slower planning and political action |
| Hierarchy | Ritual Administration | `cannibalism_ritual_administration` | `cannibalism_state_of_the_last_table` | stability and long-horizon occupation control for civilian bureaucracy and organized resistance |
| Larder | Rapid Consumption | `cannibalism_rapid_continental_larder` | `cannibalism_short_horizon_continent` | fast training, reinforcement, and attack for supply and factory exhaustion |
| Larder | Managed Reserves | `cannibalism_managed_continental_larder` | `cannibalism_managed_continental_reserve` | supply endurance, efficiency, and extraction for civilian and political administration |
| Larder | Mobile Routes | `cannibalism_mobile_continental_larder` | `cannibalism_larder_that_moves` | land and naval reach for fuel demand and reduced useful dockyard output |
| Larder | Battlefield Receipts | `cannibalism_battlefield_continental_larder` | `cannibalism_harvest_follows_victory` | capture, attack, recovery, and reinforcement after battle for reduced defense |

The four `max_command_power` constants use flat vanilla-scale values of 10, 15, 10, and 20 rather than percentage-scale decimals. Every other percentage or factor follows the value scale used by matching vanilla idea modifiers.

## Three-spirit lifecycle proof

The existing unified focus reward effects were audited against the twenty definitions:

- disposition clearing removes all six disposition root and capstone ideas
- hierarchy clearing removes all six hierarchy root and capstone ideas
- Larder clearing removes all eight Larder root and capstone ideas
- ten route-entry rewards clear their family before adding exactly one root idea
- ten route-capstone rewards swap the matching root for exactly one matching capstone
- the opening reward removes `cannibalism_unified_command_burden`

The resulting focus-owned lifecycle permits at most one disposition spirit, one hierarchy spirit, and one Larder spirit, for a strict maximum of three.

## Unified focus localisation

Each of the following 108 focus IDs has exactly one title key, one `${focus_id}_desc` key, and one `${focus_id}_tt` key. This produces exactly 324 focus localisation keys, and every one of the 108 `custom_effect_tooltip` references in the focus tree resolves.

### Opening, 8

`CBL_reveal_the_command`, `CBL_summon_the_warlords`, `CBL_choose_the_first_command_capital`, `CBL_audit_the_submitted_hosts`, `CBL_bind_the_network_territories`, `CBL_settle_the_host_question`, `CBL_open_the_continental_ledger`, `CBL_establish_the_first_continental_command`

### Warlord disposition, 15

`CBL_keep_the_lieutenants`, `CBL_seat_the_regional_governors`, `CBL_preserve_the_origin_commands`, `CBL_arbitrate_the_captains`, `CBL_council_of_retained_hosts`, `CBL_break_the_warlords`, `CBL_seize_the_hidden_hoards`, `CBL_dissolve_the_regional_commands`, `CBL_appoint_the_bone_officers`, `CBL_authority_without_rivals`, `CBL_chain_the_rivals`, `CBL_take_their_heirs`, `CBL_levy_hostage_tribute`, `CBL_rotate_the_hostage_governors`, `CBL_dominion_of_chains`

### Supreme hierarchy, 15

`CBL_one_command`, `CBL_standardize_host_ranks`, `CBL_centralize_the_larder_quota`, `CBL_command_without_distance`, `CBL_the_single_operational_will`, `CBL_many_jaws`, `CBL_charter_the_regional_hosts`, `CBL_divide_the_campaign_theaters`, `CBL_covenant_of_mutual_predation`, `CBL_confederation_under_one_name`, `CBL_ritual_administration`, `CBL_codify_the_feeding_law`, `CBL_ordain_the_punishment_tables`, `CBL_census_of_mouths_and_chains`, `CBL_the_state_of_the_last_table`

### Continental Larder, 23

`CBL_central_accounting`, `CBL_classify_the_consumption_states`, `CBL_build_the_storage_network`, `CBL_boards_of_captured_industry`, `CBL_continental_larder_doctrine`, `CBL_burn_through_the_near_states`, `CBL_feed_the_legion_surge`, `CBL_exhaust_the_frontier`, `CBL_short_horizon_continent`, `CBL_preserve_the_working_herds`, `CBL_rotate_the_feeding_districts`, `CBL_police_the_long_harvest`, `CBL_managed_continental_reserve`, `CBL_prisoner_trains`, `CBL_escort_the_larder_columns`, `CBL_oceanic_hulk_routes`, `CBL_the_larder_that_moves`, `CBL_mark_the_battlefield_yields`, `CBL_recovery_battalions`, `CBL_convert_the_captured_hospitals`, `CBL_harvest_follows_victory`, `CBL_continents_as_supply_regions`, `CBL_abolish_the_old_supply_ceiling`

### Army, 14

`CBL_integrate_the_warbands`, `CBL_map_the_origin_templates`, `CBL_standardize_captured_calibers`, `CBL_raise_the_cannibal_legions`, `CBL_legion_reinforcement_tables`, `CBL_legions_of_the_continents`, `CBL_bone_guard_command`, `CBL_shield_the_supreme_body`, `CBL_breach_the_enemy_capitals`, `CBL_enemy_collapse_doctrine`, `CBL_harvest_the_rout`, `CBL_break_the_retreating_fronts`, `CBL_coordinate_the_three_armies`, `CBL_the_army_that_does_not_end`

### Navy, 8

`CBL_captured_shipyards`, `CBL_raider_flotillas`, `CBL_prison_hulks`, `CBL_convoy_hunt_tables`, `CBL_amphibious_feeding_columns`, `CBL_silent_anchorages`, `CBL_island_command_network`, `CBL_every_ocean_a_corridor`

### Air, 7

`CBL_repair_the_captured_airframes`, `CBL_terror_reconnaissance`, `CBL_interdiction_markers`, `CBL_airborne_cell_insertion`, `CBL_battlefield_recovery_signals`, `CBL_fear_bombing_tables`, `CBL_skies_over_the_larder`

### Cells, 8

`CBL_global_courier_network`, `CBL_prison_and_port_cells`, `CBL_corrupt_the_enemy_officers`, `CBL_perfect_the_false_surrender`, `CBL_sleep_beneath_retreat`, `CBL_synchronize_the_uprisings`, `CBL_reactivate_the_cured_networks`, `CBL_the_war_begins_inside`

### Expansion, 4

`CBL_read_the_continental_weakness`, `CBL_terror_ultimata`, `CBL_cell_backed_border_incidents`, `CBL_host_theaters_without_borders`

### Counterwar, 4

`CBL_measure_world_hostility`, `CBL_break_the_relief_corridors`, `CBL_sever_the_coalition_command`, `CBL_consume_the_counterwar`

### Ordinary world end, 2

`CBL_final_global_mobilization`, `CBL_dismantle_the_ordinary_world`

The localisation file remains UTF-8 with BOM. The 324 focus keys and forty idea keys contain no `:0`, placeholder text, update-history wording, transform-history wording, or claims that population, Larder, equipment, manpower, or formations appear without their real costs and accounting rules.

## Sprite registration contract

For every focus ID above, `interface/014_cannibalism.gfx` contains exactly one regular sprite and one shine sprite:

```txt
GFX_goal_<focus_id>
GFX_goal_<focus_id>_shine
gfx/interface/goals/014_cannibalism/goal_<focus_id>.dds
```

Every shine sprite uses `gfx/FX/buttonstate.lua`. This is 108 regular registrations plus 108 shine registrations.

For every route idea ID in the route table, the file contains exactly one idea sprite:

```txt
GFX_idea_<idea_id>
gfx/interface/ideas/014_cannibalism/idea_<idea_id>.dds
```

All 236 new sprite names are unique across the repository's interface files, and every registered path matches the handoff contract exactly.

## Audit results

- 108 focus IDs found, all unique
- 324 expected focus localisation keys found exactly once
- 108 focus tooltip references found, all unique and resolved
- 20 idea definitions found exactly once across `common/ideas`
- 20 idea name keys and 20 idea description keys found exactly once
- 107 route-idea constant references matched by 107 unique constant definitions, with no unresolved or unused owned constants
- 27 distinct owned modifiers all have vanilla national-idea precedents
- 108 regular focus sprites, 108 shine sprites, and 20 idea sprites registered with no missing, duplicate, or mismatched registration
- all twenty idea definitions carry the CBL identity, reveal, and ordinary-route gates
- new route ideas appear only in the unified idea definitions, unified focus rewards, unified localisation, unified sprites, and the implementation handoffs, with no pre-reveal gameplay reference

## Simplifications, omissions, and blockers

No fallback, placeholder, or gameplay simplification was used inside the assigned surface.

The exact 108 focus DDS files and twenty idea DDS files registered here are all absent at handoff time. Their deterministic paths are the two path patterns above applied to the exact ID lists in this document. This was an explicit task boundary, so no stand-in DDS was created or substituted. Until the asset package supplies those 128 final files, the registrations are structurally complete but the icons cannot render their intended art.

No commit was created. The parent retains final review, integration, asset routing, validation, and commit ownership.

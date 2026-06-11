# Event 007: Fury

Event 007 Fury is a repeatable Wars-cluster event that transforms safe AI minors into aggressive border-war actors.

## Runtime Flow

1. Each `chaosx.nr7.1` firing selects a fresh eligible AI minor through `fury_can_be_selected`; existing Fury actors are excluded, so repeat firings create additional Fury countries instead of reapplying Fury to the previous actor.
2. The selected country receives `fury_national_fury`, the shared `fury_focus_tree`, starting Fury variables, the base support-equipment and engineer-company unlocks required by the Fury Column template, starting units, equipment, a hidden finite reinforcement reserve, and a self-scheduled weekly event loop.
3. `chaosx.nr7.10` scores every valid neighboring target, prefers weak isolated neighbors, penalizes faction-backed or major targets, saves the best target, and declares an annexation war.
4. `chaosx.nr7.20` runs only on active Fury actors every seven days. Each weekly tick draws one division from the actor's finite reinforcement reserve while any reserve remains, updates Momentum and Overextension, checks whether the current war has ended, and queues another target scan when appropriate.
5. `chaosx.nr7.30` records the first conquest and fires `chaosx.news.7007`.
6. Fury cleanup clears the actor state if the country capitulates or loses controlled territory.

## Selection Safety

Fury selection excludes:

- player countries
- subjects
- majors
- capitulated countries
- countries linked to the player by overlord or faction relationships
- countries with an island capital
- countries without at least two valid neighbor targets
- countries that recently failed as Fury

Ordinary Fury selection prefers safe one-state AI minors, then broadens to two-state and three-state mainland-capital candidates before using the general safe selector. Repeat random firings choose fresh eligible actors instead of reapplying Fury to an existing Fury country. Evolution II and Evolution III can still force additional actors when their setup needs them. The triggerable scenario and terminal world-end branch use separate setup paths, but their safe actor seeding still reuses the same two-valid-neighbor gate.

Ordinary targets can be AI or player-controlled countries. Target validity does not exclude a country for being player-controlled or player-linked; targets must not be subjects, Fury actors, allies, subjects of the Fury actor, or countries already at war with the Fury actor.

## Variables and Flags

- `fury_actor`: active Fury country.
- `fury_current_target`: country variable containing the current target country ID.
- `fury_best_target_score`: highest score from the latest neighbor scan.
- `fury_failed_target_scans`: count of consecutive scans that found no valid scored target.
- `fury_target_preparation`: preparation value raised by focus route choices and read by target scoring.
- `fury_last_target_id`: last declared target country ID, used for audit and future churn prevention.
- `fury_momentum`: escalation strength and target pressure.
- `fury_reinforcement_reserve_pool`: hidden finite reserve pool consumed by weekly spawning.
- `fury_reinforcement_reserve_total_granted`: hidden lifetime reserve counter capped at 100 divisions per Fury actor.
- `fury_reinforcement_spawn_tick`: hidden weekly cadence counter; reserve spawning creates one division per weekly tick while reserve remains.
- `fury_overextension`: occupation strain.
- `fury_compliance_drive`: settlement and coring pressure.
- `fury_reach`: no-neighbor recovery pressure.
- `fury_pact_cohesion`: cooperation route value.
- `fury_occupation_pressure`: recalculated pressure from non-core controlled states, active wars, resistance, rail registry work, and garrison capacity.
- `fury_garrison_capacity`: fielded-division-derived pressure relief.
- `fury_registered_state_count`: current registered non-core settlement workload.
- `fury_evolution_i_applied`, `fury_evolution_ii_applied`, `fury_evolution_iii_applied`: actor evolution state.
- `fury_triggerable_scenario_actor`: actor created by The World in Fury triggerable scenario.
- `fury_first_conquest_recorded_global`: at least one Fury conquest has been recorded.
- `fury_all_actors_defeated`: no Fury actors remain after a cleanup pass.
- `fury_coring_completed`: at least one Fury actor cored a conquered settlement state.
- `fury_pact_formed`: cooperation or scenario pact content created a Fury pact state.
- `fury_actor_fought_actor`: hostile scenario or rivalry content produced Fury-on-Fury conflict.
- `fury_world_end_candidate`: a Fury actor has reached the current candidate focus for terminal escalation.
- `world_end_fury`: the terminal `The World in Fury` branch has begun.
- `fury_world_end_active`, `fury_world_end_started`: terminal Fury is active.
- `fury_world_end_seeded_actor`: actor created by the terminal world-end seeding pass.
- `fury_world_end_seed_blocked`: terminal Fury eligibility was reached but too few safe minor countries remained to seed the branch.
- `fury_world_end_defeated`: no Fury actors remain after terminal Fury began.

## Decisions

Fury actors use `fury_war_office_category`.

- `fury_select_new_target`: selects and attacks a new valid neighbor.
- `fury_open_forward_depots`: spends command power and infantry equipment to spawn an extra reinforcement wave and increase Fury Momentum.
- `fury_register_occupation_settlement`: spends command power, rifles, and support equipment to mark a non-core controlled state for settlement.
- `fury_count_captured_registers`: spends command power, rifles, and support equipment to mark a new occupied state for administrative register work.
- `fury_rail_registry_survey`: spends trains and support equipment to mark a registered state as rail-ready and lower occupation pressure.
- `fury_garrison_the_names_mission`: timed occupation mission that lowers pressure if Fury holds the capital and registered states long enough.
- `fury_core_state_by_administration`: higher-compliance coring path with heavier bureaucracy costs and safer pressure reduction.
- `fury_core_state_by_march`: lower-compliance coring path with heavier manpower, equipment, and stability cost.
- `fury_restore_the_registers_mission`: crisis mission that appears during extreme occupation pressure and can restore the register chain.
- `fury_form_war_table`: cooperation route for Evolution II Fury actors.
- `fury_mark_rival_column`: rivalry route for Evolution II Fury actors.
- `fury_survey_beyond_the_border`: clears the no-neighbor pause and queues a new scan.

Non-Fury responders use `anti_fury_response_category` after the major-Fury threshold or terminal Fury state.

- `anti_fury_border_watch`: pays command power and rifles to start `anti_fury_border_watch_mission`.
- `anti_fury_send_emergency_aid`: sends rifles, support equipment, and trains to one current Fury target, then starts `anti_fury_aid_route_mission`.
- `anti_fury_firebreak_staff_talks`: spends command power and army experience for defensive planning and containment tracking.
- `anti_fury_start_supply_denial`: pays rifles and command authority to start `anti_fury_supply_denial_mission`.
- `anti_fury_recognition_denial`: lowers Fury pact cohesion and adds containment pressure.

Anti-Fury mission success sets responder-side containment hooks used by achievements; stale missions cancel when the local Fury threat disappears.

## Focus Tree

The shared `fury_focus_tree` is a 52-focus AI tree with opening, army, expansion, occupation, cooperation, rivalry, evolution, and world-end candidate branches. It keeps the original anchor IDs used by the runtime helpers while adding route depth around them.

Route coverage:

| Route family | Implemented focus IDs |
| --- | --- |
| Opening trunk | `fury_open_the_war_office`, `fury_war_office_without_a_door`, `fury_count_the_rifles`, `fury_capital_guard`, `fury_first_target_files`, `fury_first_war_office_orders` |
| Army of the March | `fury_field_columns`, `fury_depot_cadres`, `fury_storm_columns`, `fury_forward_depots`, `fury_logistics_under_movement`, `fury_officer_tables` |
| Expansion | `fury_one_border_at_a_time`, `fury_weak_neighbor_doctrine`, `fury_capital_first_plans`, `fury_cut_the_rail_before_the_war`, `fury_the_next_neighbor` |
| Occupation and integration | `fury_occupation_registers`, `fury_census_of_taken_states`, `fury_new_registry_offices`, `fury_rail_and_registry`, `fury_garrison_the_names`, `fury_conquest_coring`, `fury_core_by_administration`, `fury_core_by_march` |
| Cooperation | `fury_second_war_table`, `fury_the_other_fire_answers`, `fury_shared_war_tables`, `fury_partition_before_victory`, `fury_joint_cadre_transfers`, `fury_fury_pact_command` |
| Rivalry | `fury_rival_column`, `fury_no_second_fury`, `fury_claim_the_same_map`, `fury_absorb_the_rival_fire`, `fury_last_fury_standing` |
| Evolution I | `fury_hardened_doctrine`, `fury_harden_the_columns`, `fury_depot_officers_without_leave`, `fury_forced_march_tables`, `fury_occupation_as_recruitment` |
| Evolution III | `fury_all_borders`, `fury_three_war_offices`, `fury_storms_on_all_fronts`, `fury_no_target_is_first`, `fury_all_roads_are_front_roads` |
| World-end candidate | `fury_the_last_neighbor_has_fallen`, `fury_carry_the_orders_overseas`, `fury_continental_ignitions`, `fury_main_fury_pact`, `fury_world_in_fury`, `fury_no_neutral_map` |

The cooperation and rivalry branches are mutually exclusive. World-end candidate focuses set preparation flags and threat. `fury_world_in_fury` calls the terminal starter when the chaos meter is in World Collapse, the candidate passes terminal readiness through no-neutral-map doctrine, major status, broad state control, or no remaining valid neighbors, enough safe AI minors remain for seeding, and the world-end system has not been disabled.

## Evolutions

- Evolution I, Hardened Fury: applies `fury_hardened_fury`, improves Momentum and Reach, and records an evolution entry when enabled.
- Evolution II, Two Fires: ensures up to two Fury actors when safe candidates exist and opens cooperation or rivalry gameplay.
- Evolution III, All Borders at Once: ensures up to three Fury actors when safe candidates exist and makes actors declare on all valid neighbors.

Disabled evolutions do not record entries because the record effects require their unlock flags.

## Triggerable Scenario

`The World in Fury` is registered as triggerable scenario `#005`.

- Type: `Fury Pact` or `Hostile Fury`.
- Intensity: Low 2 actors, Medium 5 actors, High 9 actors, Maximum up to 16 actors when enough safe AI minors exist.
- Intensity changes the starting package and capped hidden reserve bonus. It never changes weekly spawning into an uncapped loop.
- Actor selection makes repeated continent passes before using a global fallback, so the scenario starts dispersed instead of concentrating nearby minors.
- Player countries and player-linked countries remain excluded from becoming Fury actors; after launch they can still become Fury targets when normal target gates allow it.
- Hostile Fury attempts Fury-on-Fury declarations in addition to neighbor wars, which supports the rival-fires achievement route.

## Terminal World-End Branch

`The World in Fury` is separate from the triggerable scenario. It starts only from a prepared Fury actor that has completed the world-end focus path, passes terminal readiness through no-neutral-map doctrine, major status, broad state control, or no remaining valid neighbors, is not in an extreme unresolved occupation crisis unless the final route is unlocked, and the global chaos meter has reached World Collapse.

When it begins, the branch:

- sets `world_end`, `world_end_fury`, `fury_world_end_active`, `fury_world_end_started`, and `world_threat_source_fury`
- saves the starting actor as `fury_world_end_leader`
- creates `The World in Fury` faction and brings all active Fury actors into it
- applies `fury_world_in_fury` to terminal actors
- warns all player countries before terminal Fury rules can threaten them directly; ordinary neighbor targeting can already hit player-controlled countries that meet normal target gates, while the separate `fury_terminal_can_threaten_player_linked_country` helper handles post-grace terminal threats outside the ordinary neighbor scan
- seeds Fury actors across unrepresented continents first, then fills to `fury_balance.world_end_required_actor_count` when enough safe AI minors exist
- unlocks terminal reserve sharing through `fury_share_terminal_reserves` and `fury_assign_terminal_fronts`
- fires super-event slot `60` with `GFX_super_event_world_in_fury`
- blocks visibly with `fury_world_end_seed_blocked` and `chaosx.nr7.51` if too few safe seed countries remain
- reports terminal defeat through `chaosx.nr7.53` when the last World in Fury actor falls

## Achievements

Event 007 adds ten achievements in `common/achievements/chaos_redux_achievements.txt`.

- `achievement_fury_fuse_cut`
- `achievement_fury_no_minor_major`
- `achievement_fury_firebreak`
- `achievement_fury_pact_breaker`
- `achievement_fury_ten_fires`
- `achievement_fury_last_neighbor`
- `achievement_fury_world_without_fury`
- `achievement_fury_rivals_burn`
- `achievement_fury_major_without_faction`
- `achievement_fury_no_cores`

Achievement checks require player-side containment participation through war contribution or the anti-Fury Border Watch path, plus relevant Fury outcome flags. The player remains excluded from normal Fury assignment.

Achievement art uses final Fury-specific DDS triplets under `gfx/achievements/`, with source and contact-sheet notes in `docs/assets/007_fury/achievement_icons/manifest.md`.

## Assets

Current wiring uses stable Fury-specific assets:

- report event: `GFX_report_event_fury_war_office`
- news event: `GFX_news_event_fury_first_conquest`
- super-event slot: `59`
- super-event image: `GFX_super_event_fury_becomes_a_state`, backed by generated final art at `gfx/super_events/fury_becomes_a_state.dds`
- major Fury super-event audio: ID `59`, `music/fury_becomes_a_state.ogg`, `sound/chaosx_super_event_fury_becomes_a_state.wav`
- world-end super-event slot: `60`
- world-end super-event image: `GFX_super_event_world_in_fury`, backed by generated final art at `gfx/super_events/super_event_world_in_fury.dds`
- world-end super-event audio: ID `60`, `music/super_event_world_in_fury.ogg`, `sound/chaosx_super_event_world_in_fury.wav`
- achievement icons: final filenames registered in `interface/chaosx_achievements.gfx`
- Fury leader overlay: `GFX_fury_leader_flame_overlay_animated`, backed by an 8-frame looping sheet at `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_sheet.dds`
- Fury leader overlay static fallback: `GFX_fury_leader_flame_overlay_static`, backed by `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_static.dds`

Final Fury art and audio use stable gameplay IDs. Report, news, and super-event images use street-level Fury outbreak imagery: rogue soldiers, civilians fleeing, smoke, burning streets, and sudden neighbor-war panic. They should not be replaced with map rooms, command desks, ledgers, route strings, globes, or war-office planning scenes.

The leader overlay is a scripted GUI presentation layer, not a replacement country portrait. `common/scripted_guis/007_fury_scripted_guis.txt` shows it on selected Fury countries in the diplomacy leader panel, and on the politics country leader portrait when the current country itself has Fury. `interface/007_fury_leader_overlay.gui` attaches the overlay to the vanilla leader portrait positions without editing vanilla GUI files.

Recommended final asset paths:

- `gfx/event_pictures/fury/fury_war_office.dds`
- `gfx/event_pictures/fury/fury_first_conquest.dds`
- `gfx/interface/ideas/fury/idea_fury_national_fury.dds`
- `gfx/interface/ideas/fury/idea_fury_hardened_fury.dds`
- `gfx/interface/decisions/fury/decision_category_fury_war_office.dds`
- `gfx/interface/decisions/fury/decision_fury_target.dds`
- `gfx/interface/goals/fury/goal_fury_war_office.dds`
- `gfx/event_pictures/fury/fury_first_conquest.dds`
- `gfx/super_events/fury_becomes_a_state.dds`
- `gfx/super_events/super_event_world_in_fury.dds`
- `music/fury_becomes_a_state.ogg`
- `sound/chaosx_super_event_fury_becomes_a_state.wav`
- `music/super_event_world_in_fury.ogg`
- `sound/chaosx_super_event_world_in_fury.wav`
- `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_sheet.dds`
- `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_static.dds`
- `gfx/achievements/achievement_fury_*`

## Validation Notes

- Target scoring reads size, industry, divisions, manpower, war state, faction state, major status, rough terrain, supply nodes, Fury momentum, Fury overextension, target preparation, evolution state, and last-target churn.
- Achievement conditions are tied to containment contribution, scenario intensity/type flags, all-safe-candidate Maximum fallback, Fury-on-Fury declarations, major-Fury defeat, no-coring containment, and terminal world-end defeat.
- Event details intentionally stay concise; live Momentum, Overextension, and current target remain visible through gameplay state rather than expanded event-log text.

## Source Notes

The slot `59` and `60` Hobbes quote source is recorded in `docs/super_events/super_event_quote_sources.md`. The slot `59` and `60` audio sources, licenses, and conversion details are recorded in `docs/super_events/super_event_audio_packages.md`.

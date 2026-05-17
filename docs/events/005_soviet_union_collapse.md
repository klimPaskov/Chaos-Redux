# Event 005 - Soviet Union Collapse

## Overview

Soviet Union Collapse is a one-per-campaign Liberations cluster event that turns the old stub release into an active union crisis. The entry event remains `chaosx.nr5.1`; it now routes to the visible Soviet event `chaosx.nr5.2`, which initializes the crisis, releases the first breakaway republics, grants them defensive support, and activates the opening Soviet objective board.

The baseline crisis stages are ordinary crisis progression, not evolution logs. Evolutions remain reserved for separate mutation tracks such as old movements, depot states, railway authorities, foreign liaison networks, and high-chaos splinters.

## Current Implementation

The implemented opening slices cover the crisis scaffold and the first intervention layer:

- `common/script_constants/005_soviet_collapse_constants.txt` centralizes opening crisis values, breakaway support, objective requirements, objective pressure families, and first response costs.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds active-crisis, breakaway, patron, cost, recovered-capital, second-wave quieting, provincial office, emergency procurator, capital district, western telegraph, grain-file, governors' oath, archive, negotiated-corridor, government-file, regional-command, inner-ring, loyal-rail, militia, amnesty, League-calendar, lost-depot, Soviet-identity, and rump-preparation triggers.
- `common/scripted_effects/005_soviet_collapse_effects.txt` initializes the crisis meter, clamps and recalculates total threat, releases the opening breakaways, gives starting forces, and enforces the Soviet objective cap.
- `common/ideas/005_soviet_collapse_ideas.txt` adds country spirits for the union crisis, Moscow response routes, loyalist officers, captured depots, and breakaway defensive coordination.
- `common/decisions/005_soviet_collapse_decisions.txt` adds four non-political-power Soviet response decisions, forty opening goal-style missions, four breakaway emergency actions, and seven targeted foreign patron decisions.
- `events/005_soviet_collapse.txt` replaces the old hidden release stub with a visible opening event and four posture choices.
- `events/005_soviet_collapse_factory_ancient.txt` adds the triggered notices for the first high-chaos factory and Volga successor states.

## Crisis Meter

The Soviet crisis category uses these variables:

- `soviet_collapse_total_collapse_threat`
- `soviet_collapse_moscow_authority`
- `soviet_collapse_republic_confidence`
- `soviet_collapse_military_obedience`
- `soviet_collapse_depot_vulnerability`
- `soviet_collapse_foreign_appetite`
- `soviet_collapse_league_cohesion`
- `soviet_collapse_evolution_weirdness`
- `soviet_collapse_breakaway_count`

Opening values start from a low baseline in calm conditions, then change from chaos tier, Soviet stability, war support, active wars, and capital control. The total threat is recalculated from the component variables instead of being a fixed timer.

## Opening Breakaways

The normal opening release tries Ukraine and Belarus. Kazakhstan can appear in the opening if chaos is high or the Soviet state is already unstable. Each appearing breakaway receives:

- `soviet_collapse_breakaway` country flag
- manpower and equipment from script constants
- `soviet_collapse_captured_soviet_depots`
- `soviet_collapse_defensive_coordination`
- three `Emergency Republican Guard` divisions at its capital
- one extra division and extra stores in higher chaos bands

When Kazakhstan appears as an event-created opening breakaway, the southern cascade can also begin. Uzbekistan appears with Kazakhstan, Kyrgyzstan can appear at chaos tier 3 and above, Tajikistan can appear at chaos tier 4 and above, and Turkmenistan can appear at chaos tier 5. These southern republics receive the standard breakaway setup package and the shared Central Asian runtime focus tree.

This is only the opening support package. Later slices still need full republic focus expansions, custom countries, serious splinters, AI, and reinforcement routes.

## Republic Focus Trees

Event-created Ukraine, Belarus, Kazakhstan, southern cascade republics, prepared regional tags, and any remaining event-created breakaway without a bespoke tree receive compact runtime focus trees through `load_focus_tree` after the release effect finishes. The loading effect only applies to countries with `soviet_collapse_event_created_republic`, and it does not use `keep_completed`, so it is intended for freshly released tags rather than replacing progress on existing countries.

The implemented trees are:

1. `soviet_collapse_ukraine_focus_tree` in `common/national_focus/005_soviet_collapse_republics.txt`: 18 focuses covering the emergency Rada trunk, legal republic, socialist sovereignty, military directory, foreign liaison, League preparation, and a high-chaos Black Banner lane.
2. `soviet_collapse_belarus_focus_tree`: 14 focuses covering the Minsk junction trunk, legal/statute restoration, railway control, forest defense, counterintelligence, western gate offices, and League preparation.
3. `soviet_collapse_kazakhstan_focus_tree`: 12 focuses covering the steppe congress trunk, Alash restoration, steppe soviets, mobile district command, resource sovereignty, steppe federation, and a high-chaos myth lane.
4. `soviet_collapse_baltic_focus_tree`: 9 focuses for event-created Lithuania, Latvia, and Estonia, covering legal continuity, wire rooms, forests, ports, observers, home guards, restoration pact work, recognition dossiers, and a sovereign Baltic front.
5. `soviet_collapse_caucasus_focus_tree`: 9 focuses for event-created Georgia, Armenia, and Azerbaijan, covering mountain councils, pass guards, oil routes, arbitration, foreign missions, mountain brigades, defense compacts, oilfield security, and sovereign mountain politics.
6. `soviet_collapse_central_asia_focus_tree`: 9 focuses for event-created Uzbekistan, Kyrgyzstan, Tajikistan, and Turkmenistan, covering the supply congress, rail and irrigation, border offices, Basmachi pressure, foreign balance, defense council, federation, school boards, and inland compact.
7. `soviet_collapse_moldova_focus_tree`: 9 focuses for event-created Moldova, covering the Dniester line, river customs, Chisinau ledgers, Romanian and Ukrainian corridors, depot battalions, buffer compact, neutral transit, and bridge-state survival.
8. `soviet_collapse_breakaway_focus_tree`: 22 focuses for remaining event-created breakaways, covering emergency government, legal restoration, socialist sovereignty, military defense, foreign missions, League liaison, regional specialization hooks, and a high-chaos Black Banner pressure lane.

Focus rewards call shared scripted effects for legal recognition, socialist sovereignty, military consolidation, depot control, League preparation, foreign channels, and high-chaos identity pressure. Those effects adjust local breakaway variables and feed the Soviet crisis meter through constants in `soviet_collapse_republic_focus`.

## High-Chaos Tags

The first high-chaos successor tag foundations are registered for later spawn and mechanics work:

1. `CFR` - Civilian Factory of Russia, led by the Construction Board, with existing flag and leader assets.
2. `MFR` - Military Factory of Russia, led by the Arsenal Board, with existing flag and leader assets.
3. `OGB` - Old Great Bulgaria on the Volga, led by the Volga Restoration Council, with existing flag and leader assets.

These tags define country files, history files, politics, basic technologies, leader portraits, localisation, opening decision mechanics, event spawn effects, and evolution-log entries. Their larger focus-tree packages remain separate implementation slices.

At high chaos, the Soviet opening hook can create the first three successor states without using any recurring on-action loop. Each spawn is gated by `is_soviet_collapse_high_chaos_successor_spawn_ready`, which requires the Soviet Collapse to be active for `SOV` and either chaos tier 4, chaos tier 5, or `soviet_collapse_evolution_weirdness` reaching `constant:soviet_collapse_high_chaos_event_log.spawn_weirdness_gate`. Each successor also respects the evolution disable UI by checking `is_current_evolution_enabled` for its own high-chaos stage before any state transfer happens.

The exact opening state packages are:

1. `CFR` receives Yaroslavl (`248`) and Ivanovo (`253`) if both are owned and controlled by `SOV`.
2. `MFR` receives Nizhny Novgorod (`252`) and Samara (`251`) if both are owned and controlled by `SOV`.
3. `OGB` receives Kazan (`249`) and Volga Germany (`829`) if both are owned and controlled by `SOV`.

These are strict prerequisites, not contingency pools. If a required state has already left Soviet ownership or control, that successor is not created by the opening hook. A created high-chaos successor receives the normal breakaway support package, its tag-specific opening ideas, and an event notice in `events/005_soviet_collapse_factory_ancient.txt`. The first eligible successor in each high-chaos tier also records an actor-linked evolution-log entry under `Soviet Collapse: High-Chaos Aberrations`; later successor notices in the same tier remain normal reports so the crisis does not flood the evolution log.

Each tag also has an opening decision board:

1. `CFR` uses `The Reconstruction State` with `Construction Mandates`, `Survey the Unfinished Sites`, and `Issue Reconstruction Contracts`.
2. `MFR` uses `The Arsenal State` with `Arsenal Quotas`, `Audit Arsenal Orders`, and `Convert Depots to Arms Lines`.
3. `OGB` uses `The Volga Restoration` with `Volga Legitimacy`, `Claim the Volga Crossings`, and `Convene Bolghar Scholars`.

These decision boards are deliberately small foundations. They provide the variables, costs, blocked-cost localisation, ideas, and first rewards that later focus trees and event spawn effects can expand.

## Intervention Decisions

Breakaway republics have a small playable emergency board:

1. `soviet_collapse_request_foreign_recognition`
2. `soviet_collapse_mobilize_defense_units`
3. `soviet_collapse_seize_depots`
4. `soviet_collapse_coordinate_fronts`

These actions use stability, army experience, fuel, and support equipment instead of a generic political-power default. They build recognition progress, depot control, defensive ideas, emergency units, and Soviet crisis pressure.

Major foreign patron candidates that are hostile to Moscow can target entries from `global.soviet_collapse_breakaway_countries` with:

1. `soviet_collapse_recognize_breakaway_government`
2. `soviet_collapse_fund_ideological_liaison_offices`
3. `soviet_collapse_ship_border_armaments`
4. `soviet_collapse_dispatch_military_advisers`
5. `soviet_collapse_open_republican_intelligence_channel`
6. `soviet_collapse_sponsor_volunteer_corps`
7. `soviet_collapse_negotiate_republican_trade_mission`

The targeted decision scope follows the vanilla `target_array` pattern: the patron remains `ROOT`, and the chosen breakaway is `FROM`. The aid costs use stability, war support, equipment, army experience, manpower, trains, convoys, and fuel. Effects raise breakaway recognition or military capacity while feeding Soviet `Foreign Penetration`, `Depot Vulnerability`, `League Cohesion`, `Moscow Authority`, or `Armed Breakaway Momentum` as appropriate.

## Soviet Objective Board

The Soviet category currently activates these opening goal-style missions:

1. `soviet_collapse_soviet_mission_001_confirm_the_emergency_chain_of_command`
2. `soviet_collapse_soviet_mission_002_seal_the_first_circular`
3. `soviet_collapse_soviet_mission_003_guard_the_peoples_commissariats`
4. `soviet_collapse_soviet_mission_004_establish_the_crisis_desk`
5. `soviet_collapse_soviet_mission_005_count_the_missing_trains`
6. `soviet_collapse_soviet_mission_006_freeze_unapproved_transfers`
7. `soviet_collapse_soviet_mission_007_order_the_border_posts_to_report_twice`
8. `soviet_collapse_soviet_mission_008_audit_the_republic_radios`
9. `soviet_collapse_soviet_mission_009_open_the_loyalist_courier_line`
10. `soviet_collapse_soviet_mission_010_protect_the_first_reclamation_staging_area`
11. `soviet_collapse_soviet_mission_011_announce_the_legal_continuity_decree`
12. `soviet_collapse_soviet_mission_012_convene_loyal_republican_deputies`
13. `soviet_collapse_soviet_mission_013_publish_the_union_guarantee`
14. `soviet_collapse_soviet_mission_014_register_emergency_autonomy_charters`
15. `soviet_collapse_soviet_mission_015_use_the_supreme_soviet_as_a_shield`
16. `soviet_collapse_soviet_mission_016_certify_loyal_military_districts`
17. `soviet_collapse_soviet_mission_017_restore_the_central_supply_seal`
18. `soviet_collapse_soviet_mission_018_send_the_quiet_governors`
19. `soviet_collapse_soviet_mission_019_prepare_the_reduced_union_formula`
20. `soviet_collapse_soviet_mission_020_declare_the_union_treaty_valid_until_rewritten`
21. `soviet_collapse_soviet_mission_021_prove_one_republic_can_be_recovered`
22. `soviet_collapse_soviet_mission_022_keep_the_second_republic_quiet`
23. `soviet_collapse_soviet_mission_023_rebuild_a_provincial_party_office`
24. `soviet_collapse_soviet_mission_024_assign_the_emergency_procurators`
25. `soviet_collapse_soviet_mission_025_hold_the_capital_district_parade`
26. `soviet_collapse_soviet_mission_026_repair_the_western_telegraph_offices`
27. `soviet_collapse_soviet_mission_027_secure_the_grain_accounting_files`
28. `soviet_collapse_soviet_mission_028_demand_the_governors_oaths`
29. `soviet_collapse_soviet_mission_029_guard_the_union_archives`
30. `soviet_collapse_soviet_mission_030_stabilize_the_first_negotiated_corridor`
31. `soviet_collapse_soviet_mission_031_move_the_government_files_east`
32. `soviet_collapse_soviet_mission_032_declare_emergency_regional_commands`
33. `soviet_collapse_soviet_mission_033_hold_the_inner_ring`
34. `soviet_collapse_soviet_mission_034_secure_the_last_loyal_rail_spine`
35. `soviet_collapse_soviet_mission_035_buy_time_with_local_militias`
36. `soviet_collapse_soviet_mission_036_offer_amnesty_to_the_second_line`
37. `soviet_collapse_soviet_mission_037_break_the_leagues_first_calendar`
38. `soviet_collapse_soviet_mission_038_publicly_recover_a_lost_depot`
39. `soviet_collapse_soviet_mission_039_keep_the_officers_from_choosing_russia_alone`
40. `soviet_collapse_soviet_mission_040_prepare_the_rump_state_without_admitting_it`

The activation effect counts active missions before activating the next one and stops at `constant:soviet_collapse_soviet_objective.active_cap`, currently 10. The missions use equipment, manpower, fuel, trains, stability, war support, army experience, and command power as requirements or costs; political power is not the default cost.

Mission outcomes use family-specific crisis pressure helpers tuned through `constant:soviet_collapse_objective_pressure`. Authority, legal, command, rail, depot, foreign, cleanup, and settlement objectives no longer share the same flat success and failure effects; each family adjusts the relevant Union Crisis Threat components and then recalculates the total threat.

Failed Soviet objective families also trigger short report events in `events/005_soviet_collapse.txt`: authority (`chaosx.nr5.10`), command (`chaosx.nr5.11`), rail (`chaosx.nr5.12`), depot (`chaosx.nr5.13`), foreign exposure (`chaosx.nr5.14`), cleanup/backlog (`chaosx.nr5.15`), and settlement (`chaosx.nr5.16`). These are normal crisis reports, not evolution logs.

## Icon Wiring

This slice reuses existing wired sprites. No new art was generated.

- Ideas use `GFX_idea_union_crisis`, `GFX_idea_emergency_union_authority`, `GFX_idea_new_union_negotiations`, `GFX_idea_loyalist_officer_corps`, `GFX_idea_captured_soviet_depots`, and `GFX_idea_defensive_coordination` from `interface/005_soviet_collapse_icons.gfx`.
- Decision categories use `GFX_decision_category_soviet_collapse_soviet`, `GFX_decision_category_soviet_collapse_breakaway`, `GFX_decision_category_soviet_collapse_foreign_patron`, and `GFX_decision_category_soviet_collapse_regional_faction`.
- Soviet responses use `GFX_decision_restore_party_control`, `GFX_decision_send_loyalist_officers`, `GFX_decision_cut_rebel_supply_routes`, and `GFX_decision_emergency_mobilization`.
- Breakaway actions use `GFX_decision_request_foreign_recognition`, `GFX_decision_mobilize_defense_units`, `GFX_decision_seize_depots`, and `GFX_decision_coordinate_fronts`.
- Foreign patron actions use `GFX_decision_soviet_collapse_foreign_recognition`, `GFX_decision_soviet_collapse_foreign_armaments`, `GFX_decision_soviet_collapse_foreign_advisers`, `GFX_decision_soviet_collapse_foreign_intelligence`, `GFX_decision_soviet_collapse_foreign_volunteers`, and `GFX_decision_soviet_collapse_foreign_trade`.
- The intervention and focus country spirits use `GFX_idea_popular_defense_committees`, `GFX_idea_foreign_volunteers`, `GFX_idea_legal_restoration_claim`, `GFX_idea_socialist_sovereignty`, `GFX_idea_military_defense_council`, and `GFX_idea_old_underground_networks`.
- Soviet objectives use the shared goal sprites in `interface/005_soviet_collapse_icons.gfx`, including `GFX_decision_soviet_collapse_authority_goal`, `GFX_decision_soviet_collapse_command_goal`, `GFX_decision_soviet_collapse_rail_goal`, `GFX_decision_soviet_collapse_depot_goal`, `GFX_decision_soviet_collapse_border_goal`, `GFX_decision_soviet_collapse_foreign_goal`, and `GFX_decision_soviet_collapse_cleanup_goal`.
- The visible opening event uses `GFX_report_union_crisis`; the news event uses `GFX_news_soviet_union_collapse`.
- Republic focus trees use existing sprites from `interface/005_soviet_collapse_icons.gfx`, `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, `interface/005_soviet_collapse_kaz_icons.gfx`, and `interface/005_soviet_collapse_regional_icons.gfx`. No additional focus sprite filenames are required for this slice.
- High-chaos tag foundations use flag assets under `gfx/flags/`, leader portraits under `gfx/leaders/005_soviet_collapse/`, and portrait sprite keys in `interface/005_soviet_collapse_factory_ancient_icons.gfx`. The factory/ancient notice events currently reuse `GFX_report_union_crisis`, so no new report sprite is required for this slice.

## Future Plans

- Expand the Soviet objective board beyond the first forty missions while preserving the ten-active cap.
- Expand breakaway missions, foreign intervention missions, regional faction categories, and action-based foreign aid routes beyond the first playable board.
- Expand the compact Ukraine, Belarus, Kazakhstan, regional, and contingency breakaway runtime focus trees into full country packages with the larger focus counts mapped in the final clean specification.
- Implement full focus-tree packages and longer event chains for every custom country and serious splinter whose tag, history, localisation, ideas, decisions, leaders or councils, flags, opening spawn logic, and docs already exist.
- Wire Free Republics' League formation, super-events, achievements, and evolution logs only where the clean specification allows them.
- Audit existing Soviet Collapse evolution localisation so ordinary crisis stages are not presented as evolutions.

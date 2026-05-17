# Event 005 - Soviet Union Collapse

## Overview

Soviet Union Collapse is a one-per-campaign Liberations cluster event that turns the old stub release into an active union crisis. The entry event remains `chaosx.nr5.1`; it now routes to the visible Soviet event `chaosx.nr5.2`, which initializes the crisis, releases the first breakaway republics, grants them defensive support, and activates the opening Soviet objective board.

The baseline crisis stages are ordinary crisis progression, not evolution logs. Evolutions remain reserved for separate mutation tracks such as old movements, depot states, railway authorities, foreign liaison networks, and high-chaos splinters.

## Current Implementation

The implemented opening slices cover the crisis scaffold and the first intervention layer:

- `common/script_constants/005_soviet_collapse_constants.txt` centralizes opening crisis values, breakaway support, objective requirements, and first response costs.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds active-crisis, breakaway, patron, and cost triggers.
- `common/scripted_effects/005_soviet_collapse_effects.txt` initializes the crisis meter, clamps and recalculates total threat, releases the opening breakaways, gives starting forces, and enforces the Soviet objective cap.
- `common/ideas/005_soviet_collapse_ideas.txt` adds country spirits for the union crisis, Moscow response routes, loyalist officers, captured depots, and breakaway defensive coordination.
- `common/decisions/005_soviet_collapse_decisions.txt` adds four non-political-power Soviet response decisions, ten opening goal-style missions, four breakaway emergency actions, and seven targeted foreign patron decisions.
- `events/005_soviet_collapse.txt` replaces the old hidden release stub with a visible opening event and four posture choices.

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

When Kazakhstan appears as an event-created opening breakaway, the southern cascade can also begin. Uzbekistan appears with Kazakhstan, Kyrgyzstan can appear at chaos tier 3 and above, Tajikistan can appear at chaos tier 4 and above, and Turkmenistan can appear at chaos tier 5. These southern republics currently receive the standard breakaway setup package and are reserved for later regional focus content.

This is only the opening support package. Later slices still need regional republic focus trees, custom countries, serious splinters, AI, and reinforcement routes.

## Republic Focus Trees

Event-created Ukraine, Belarus, and Kazakhstan receive compact runtime focus trees through `load_focus_tree` after the opening release effect finishes. The loading effect only applies to countries with `soviet_collapse_event_created_republic`, and it does not use `keep_completed`, so it is intended for freshly released tags rather than replacing progress on existing countries.

The implemented trees are:

1. `soviet_collapse_ukraine_focus_tree` in `common/national_focus/005_soviet_collapse_republics.txt`: 18 focuses covering the emergency Rada trunk, legal republic, socialist sovereignty, military directory, foreign liaison, League preparation, and a high-chaos Black Banner lane.
2. `soviet_collapse_belarus_focus_tree`: 14 focuses covering the Minsk junction trunk, legal/statute restoration, railway control, forest defense, counterintelligence, western gate offices, and League preparation.
3. `soviet_collapse_kazakhstan_focus_tree`: 12 focuses covering the steppe congress trunk, Alash restoration, steppe soviets, mobile district command, resource sovereignty, steppe federation, and a high-chaos myth lane.

Focus rewards call shared scripted effects for legal recognition, socialist sovereignty, military consolidation, depot control, League preparation, foreign channels, and high-chaos identity pressure. Those effects adjust local breakaway variables and feed the Soviet crisis meter through constants in `soviet_collapse_republic_focus`.

## High-Chaos Tags

The first high-chaos successor tag foundations are registered for later spawn and mechanics work:

1. `CFR` - Civilian Factory of Russia, led by the Construction Board, with existing flag and leader assets.
2. `MFR` - Military Factory of Russia, led by the Arsenal Board, with existing flag and leader assets.
3. `OGB` - Old Great Bulgaria on the Volga, led by the Volga Restoration Council, with existing flag and leader assets.

These tags currently define country files, history files, politics, basic technologies, leader portraits, and localisation. Their decision mechanics, focus trees, event spawn effects, and evolution-log entries remain separate implementation slices.

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

The activation effect counts active missions before activating the next one and stops at `constant:soviet_collapse_soviet_objective.active_cap`, currently 10. The missions use equipment, manpower, fuel, trains, stability, war support, army experience, and command power as requirements or costs; political power is not the default cost.

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
- Republic focus trees use existing sprites from `interface/005_soviet_collapse_icons.gfx`, `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, and `interface/005_soviet_collapse_kaz_icons.gfx`. No additional focus sprite filenames are required for this slice.
- High-chaos tag foundations use flag assets under `gfx/flags/`, leader portraits under `gfx/leaders/005_soviet_collapse/`, and portrait sprite keys in `interface/005_soviet_collapse_factory_ancient_icons.gfx`.

## Future Plans

- Expand the Soviet objective board beyond the first ten missions while preserving the ten-active cap.
- Expand breakaway missions, foreign intervention missions, regional faction categories, and action-based foreign aid routes beyond the first playable board.
- Expand the compact Ukraine, Belarus, and Kazakhstan runtime focus trees into full country packages, then add regional republic and fallback breakaway trees with AI behavior.
- Implement full packages for every custom country and serious splinter: tag, history, localisation, ideas, decisions, leaders or councils, flags, focus content, and docs.
- Wire Free Republics' League formation, super-events, achievements, and evolution logs only where the clean specification allows them.
- Audit existing Soviet Collapse evolution localisation so ordinary crisis stages are not presented as evolutions.

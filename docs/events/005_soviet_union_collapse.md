# Event 005 - Soviet Union Collapse

## Overview

Soviet Union Collapse is a one-per-campaign Liberations cluster event that turns the old stub release into an active union crisis. The entry event remains `chaosx.nr5.1`; it now routes to the visible Soviet event `chaosx.nr5.2`, which initializes the crisis, releases the first breakaway republics, grants them defensive support, and activates the opening Soviet objective board.

The baseline crisis stages are ordinary crisis progression, not evolution logs. Evolutions remain reserved for separate mutation tracks such as old movements, depot states, railway authorities, foreign liaison networks, and high-chaos splinters.

## Current Implementation

The first implemented slice covers the opening crisis scaffold:

- `common/script_constants/005_soviet_collapse_constants.txt` centralizes opening crisis values, breakaway support, objective requirements, and first response costs.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds active-crisis, breakaway, patron, and cost triggers.
- `common/scripted_effects/005_soviet_collapse_effects.txt` initializes the crisis meter, clamps and recalculates total threat, releases the opening breakaways, gives starting forces, and enforces the Soviet objective cap.
- `common/ideas/005_soviet_collapse_ideas.txt` adds country spirits for the union crisis, Moscow response routes, loyalist officers, captured depots, and breakaway defensive coordination.
- `common/decisions/005_soviet_collapse_decisions.txt` adds four non-political-power Soviet response decisions and ten opening goal-style missions.
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

This is only the opening support package. Later slices still need regional republics, custom countries, serious splinters, focus trees, AI, and reinforcement routes.

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
- Soviet objectives use the shared goal sprites in `interface/005_soviet_collapse_icons.gfx`, including `GFX_decision_soviet_collapse_authority_goal`, `GFX_decision_soviet_collapse_command_goal`, `GFX_decision_soviet_collapse_rail_goal`, `GFX_decision_soviet_collapse_depot_goal`, `GFX_decision_soviet_collapse_border_goal`, `GFX_decision_soviet_collapse_foreign_goal`, and `GFX_decision_soviet_collapse_cleanup_goal`.
- The visible opening event uses `GFX_report_union_crisis`; the news event uses `GFX_news_soviet_union_collapse`.

## Future Plans

- Expand the Soviet objective board beyond the first ten missions while preserving the ten-active cap.
- Add breakaway missions, foreign intervention missions, regional faction categories, and action-based foreign aid routes.
- Build non-linear focus trees for Ukraine, Belarus, Kazakhstan, regional republics, and fallback breakaways with AI behavior.
- Implement full packages for every custom country and serious splinter: tag, history, localisation, ideas, decisions, leaders or councils, flags, focus content, and docs.
- Wire Free Republics' League formation, super-events, achievements, and evolution logs only where the clean specification allows them.
- Audit existing Soviet Collapse evolution localisation so ordinary crisis stages are not presented as evolutions.

# Event 005 Soviet Collapse AI Behavior Audit

Audit date: 2026-05-21

## Scope

This audit covers the final-clean AI behavior requirement for Event 005: focus choices, Soviet crisis actions, breakaway actions, foreign sponsor actions, regional league actions, factory-state actions, and high-chaos splinter actions must use route-valid AI behavior instead of flat or missing weights.

Event 005 does not use a dedicated `common/ai_strategy/005_*.txt` file. The current behavior is implemented at the action surface: focus `ai_will_do`, decision `ai_will_do`, sponsor-style scripted triggers, target-access triggers, MTTH release weights, and regional-faction goal triggers.

## Source Findings

| Surface | Evidence | Status |
| --- | --- | --- |
| Focus AI | Event 005 has 1,632 focus blocks across republic, custom-splinter, and factory-state focus files. All 1,632 have `ai_will_do`; 843 include contextual `modifier = { ... }` blocks. | source_pass |
| Soviet crisis decisions | The Soviet category has six non-mission decisions: four direct response actions plus two reintegration offers. All have `ai_will_do` blocks reacting to Moscow Authority, Military Obedience, Depot Vulnerability, Foreign Penetration, war state, Union Crisis Threat, target faction state, and reintegration flags. | source_pass |
| Timed Soviet objectives | The 118 Soviet mission blocks are timed, activated objectives with `allowed = { always = no }`. They are intentionally not ordinary AI-clicked decisions; activation is controlled by scripted objective helpers and the ten-active-objective cap. | source_pass |
| Breakaway decisions | The four breakaway action decisions all have `ai_will_do` blocks reacting to Soviet weakness, war with Moscow, faction membership, League coordination, chaos tier, and local breakaway state. | source_pass |
| Foreign sponsor decisions | The 17 foreign patron decisions all have `ai_will_do` blocks. They use sponsor-style triggers for military, relief, client, border, league-conference, reconstruction, and Caucasus/Central Asian patrons, plus target conditions such as war with Moscow, foreign appetite, depot vulnerability, recognition, resilience, patronage risk, aid corridors, and League channels. | source_pass |
| Foreign target gating | `can_target_soviet_collapse_breakaway_for_aid`, `can_target_soviet_collapse_breakaway_for_league_aid`, and the dependency-chain target triggers restrict AI and player targets by breakaway status, route access, target acceptance, faction/League channels, protection from dependency, dominant sponsor state, and subject/war state. | source_pass |
| Regional league decisions | The 13 regional-faction decisions all have `ai_will_do`. Founding, invitation, coordination, goal selection, success/failure resolution, tension reduction, defensive war call, and withdrawal react to Soviet threat, war with Moscow, foreign appetite, depot vulnerability, goal status, and explicit regional faction membership. | source_pass |
| Factory-state decisions | Civilian and Military Factory state decisions have `ai_will_do` blocks that react to Soviet threat, depot vulnerability, and local stability. | source_pass |
| High-chaos splinter decisions | Each custom high-chaos/special category currently present in `common/decisions/005_soviet_collapse_decisions.txt` has decision-level AI weights. The parser found three non-mission decisions each for the special categories, with no missing `ai_will_do` blocks. | source_pass |
| MTTH release behavior | `common/mtth/005_soviet_collapse_mtth.txt` uses dynamic release and miss weights responding to threat, authority, obedience, breakaway count, regional cascades, depot pressure, foreign pressure, League cohesion, old-movement pressure, failed mission flags, war pressure, chaos tier, and strong-center dampening. | source_pass |

## Decision Parser Results

The current parser result for `common/decisions/005_soviet_collapse_decisions.txt` is:

```text
decision_blocks 240
mission_blocks 118
non_mission_blocks 122
non_mission_with_ai 122
non_mission_missing_ai 0
```

Non-mission decision distribution:

```text
soviet_collapse_soviet_category: 6 non-mission decisions
soviet_collapse_breakaway_category: 4 decisions
soviet_collapse_foreign_patron_category: 17 decisions
soviet_collapse_regional_faction_category: 13 decisions
soviet_collapse_reconstruction_state: 2 decisions
soviet_collapse_arsenal_state: 2 decisions
26 custom/special successor categories: 78 decisions total, three each
```

The 26 custom/special successor categories covered by the decision parser are:

```text
soviet_collapse_kronstadt_council
soviet_collapse_free_territory
soviet_collapse_black_banner_host
soviet_collapse_basmachi_confederation
soviet_collapse_turkestan_national_council
soviet_collapse_alash_restoration_authority
soviet_collapse_union_defense_committee
soviet_collapse_security_directorate_zone
soviet_collapse_green_army_congress
soviet_collapse_don_host_emergency_circle
soviet_collapse_kuban_host_provisional_council
soviet_collapse_far_eastern_republic_revival
soviet_collapse_siberian_zemstvo_authority
soviet_collapse_ural_workers_directorate
soviet_collapse_mountain_republic_of_the_caucasus
soviet_collapse_idel_ural_league
soviet_collapse_birobidzhan_autonomous_commune
soviet_collapse_arctic_naval_directorate
soviet_collapse_northern_lights_commune
soviet_collapse_old_great_bulgaria
soviet_collapse_pale_railway_authority
soviet_collapse_tunguska_star_committee
soviet_collapse_iron_commissariat_of_the_dead
soviet_collapse_red_martyrs_resurrection_cult
soviet_collapse_dead_soldiers_congress
soviet_collapse_northern_revenant_fleet
```

## Evidence Commands

```text
python3 decision block parser over common/decisions/005_soviet_collapse_decisions.txt
python3 focus block parser over common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
rg -n "is_soviet_collapse_(military|relief|client|border|league_conference|reconstruction|caucasus_central_asia)_patron_style|can_target_soviet_collapse_breakaway_for_aid|can_target_soviet_collapse_breakaway_for_league_aid|can_target_soviet_collapse_breakaway_for_foreign" common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt
rg -n "is_soviet_collapse_regional_faction|has_soviet_collapse_regional_faction_goal|can_found_soviet_collapse|can_soviet_collapse_call_regional" common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt common/scripted_effects/005_soviet_collapse_effects.txt
```

## Remaining Notes

This audit closes the AI behavior ledger row at source level. It does not close unrelated partial rows for high-chaos package completeness, achievement placeholder art, final asset reconciliation, source-level validation matrix limits, or the final completion report.

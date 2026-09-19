# Event 021 Random Civil War GFX handoff

The source of truth for sprite registration is `interface/021_random_civil_war.gfx`.
The source of truth for asset lineage and per-consumer status is `manifest.md` plus `docs/events/021_random_civil_war/owned_asset_crosswalk.md`.
All paths below are runtime paths and do not point into `docs/assets/`.

## Event and news sprites

| Sprite | Runtime texture | Consumers |
| --- | --- | --- |
| `GFX_report_event_021_random_civil_war_opening` | `gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds` | `chaosx.nr21.2` through `.9` |
| `GFX_news_event_021_multi_front_war` | `gfx/event_pictures/021_random_civil_war/news_event_021_multi_front_war.dds` | `chaosx.news.211` |
| `GFX_news_event_021_global_fracture` | `gfx/event_pictures/021_random_civil_war/news_event_021_global_fracture.dds` | `chaosx.news.212` |

## Decision category and decisions

| Sprite | Runtime texture | Consumers |
| --- | --- | --- |
| `GFX_decision_category_picture_021_civil_war` | `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds` | `event021_civil_war_crisis_category` |
| `GFX_decision_category_021_civil_war_crisis` | `gfx/interface/decisions/021_random_civil_war/decision_category_021_civil_war.dds` | `event021_civil_war_crisis_category` |
| `GFX_decision_event021_secure_arsenals` | `gfx/interface/decisions/021_random_civil_war/decision_021_secure_arsenals.dds` | `event021_secure_arsenals`, `event021_complete_disarmament`, `event021_protect_communications` |
| `GFX_decision_event021_capital_defense` | `gfx/interface/decisions/021_random_civil_war/decision_021_capital_defense.dds` | `event021_defend_capital` |
| `GFX_decision_event021_loyalty_review` | `gfx/interface/decisions/021_random_civil_war/decision_021_loyalty_review.dds` | `event021_review_loyalty`, `event021_integrate_formations`, `event021_review_regional_administration` |
| `GFX_decision_event021_depot_seizure` | `gfx/interface/decisions/021_random_civil_war/decision_021_opposition_depot.dds` | `event021_seize_depot` |
| `GFX_decision_event021_relief_corridor` | `gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds` | `event021_open_relief_corridor` |
| `GFX_decision_event021_emergency_settlement` | `gfx/interface/decisions/021_random_civil_war/decision_021_emergency_settlement.dds` | `event021_offer_emergency_settlement`, `event021_offer_mediation`, `event021_end_sponsor_commitment`, `event021_complete_coalition_governance` |
| `GFX_decision_event021_reconstruction` | `gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds` | `event021_reconstruct_administration` |
| `GFX_decision_event021_priority_front` | `gfx/interface/decisions/021_random_civil_war/decision_021_priority_front.dds` | `event021_set_priority_front` |
| `GFX_decision_event021_monitor_border` | `gfx/interface/decisions/021_random_civil_war/decision_021_monitor_border.dds` | `event021_monitor_border` |
| `GFX_decision_event021_support_government` | `gfx/interface/decisions/021_random_civil_war/decision_021_support_government.dds` | `event021_support_government` |
| `GFX_decision_event021_support_opposition` | `gfx/interface/decisions/021_random_civil_war/decision_021_support_opposition.dds` | `event021_support_opposition` |

## Missions and ideas

| Sprite | Runtime texture | Consumers |
| --- | --- | --- |
| `GFX_mission_event021_hold_capital` | `gfx/interface/decisions/021_random_civil_war/decision_021_hold_capital_mission.dds` | `event021_hold_the_capital_mission` |
| `GFX_mission_event021_secure_rail` | `gfx/interface/decisions/021_random_civil_war/decision_021_secure_rail_junctions_mission.dds` | `event021_secure_rail_spine_mission` |
| `GFX_mission_event021_settlement_terms` | `gfx/interface/decisions/021_random_civil_war/mission_021_settlement_terms.dds` | `event021_hold_settlement_terms_mission` |
| `GFX_idea_021_fractured_command` | `gfx/interface/ideas/021_random_civil_war/idea_021_fractured_command.dds` | `event021_fractured_command`, `event021_secured_front_depot` |
| `GFX_idea_021_war_torn_administration` | `gfx/interface/ideas/021_random_civil_war/idea_021_war_torn_administration.dds` | `event021_war_torn_administration` |
| `GFX_idea_021_unsettled_settlement` | `gfx/interface/ideas/021_random_civil_war/idea_021_unsettled_settlement.dds` | `event021_unsettled_settlement` |

## Achievements

Each achievement below has a completed sprite, a `_grey` sprite, and a `_not_eligible` sprite under `gfx/achievements/`.

- `GFX_achievement_021_random_civil_war_hold_the_center*` serves `021_random_civil_war_hold_the_center`.
- `GFX_achievement_021_random_civil_war_no_state_left_behind*` serves `021_random_civil_war_no_state_left_behind`.
- `GFX_achievement_021_random_civil_war_a_flag_of_our_own*` serves `021_random_civil_war_a_flag_of_our_own`.
- `GFX_achievement_021_random_civil_war_war_within_a_war*` serves `021_random_civil_war_war_within_a_war`.
- `GFX_achievement_021_random_civil_war_the_terms_hold*` serves `021_random_civil_war_the_terms_hold`.
- `GFX_achievement_021_random_civil_war_fractals_of_sovereignty*` serves `021_random_civil_war_fractals_of_sovereignty`.

The wildcard notation above stands only for the three registered suffixes and does not introduce a fourth state.
The root runtime textures are the active consumer family; the fifteen legacy DDS files under `gfx/interface/achievements/021_random_civil_war/` remain preserved historical orphans and are not wired.

## Handoff boundary

The package is source- and asset-audited for the current `Needs Testing` phase.
Visual inspection and runtime consumer validation remain part of the user-owned live acceptance pass, and the reused Event 006 package provenance remains explicitly blocked where recorded in its separate audit.

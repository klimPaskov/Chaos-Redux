# Event 004: Random War

## Overview

Random War is a repeatable minor event that creates unexpected wars between eligible sovereign countries. The base event creates one declaration. At higher chaos tiers, the War Contagion evolution track increases the number of declarations and makes compatible Chaos Redux special countries more likely to participate.

The root event remains `chaosx.nr4.1`. It is hidden and delegates to `random_war_fire_current_context`; the event picker and event-log trigger path call the same firing effect directly after preparing a valid aggressor/target context.

## Flow

1. `random_war_setup_context` determines the highest enabled War Contagion stage available at the current chaos tier.
2. The event sets declaration count and special-country chance from script constants.
3. A valid aggressor/target pair is selected and saved as `random_war_aggressor` and `random_war_target`.
4. Event accounting records Event ID 4.
5. `random_war_fire_current_context` consumes the prepared context.
6. The first prepared pair is applied. In War Contagion stages, later declarations continue from the previous target and the last declaration closes back toward the original aggressor.
7. Aggressor and target report events fire for each declaration, then one observer news popup summarizes the full declaration set for relevant observers.

## Eligibility

Aggressors must exist, control at least one state, be sovereign, not be capitulated, and be outside the recent aggressor and staff-blame cooldown flags.

Targets must exist, control at least one state, be sovereign, not be capitulated, and be outside the recent target cooldown flag.

Pairs are checked with:

- no existing war between aggressor and target
- target is not a subject of the aggressor
- Calm World does not pair a major country against a non-major country; major-minor pairings open once the chaos tier has advanced beyond Calm World

Compatible special countries use the shared `is_special_chaos_country` trigger. It includes existing Chaos Redux special-country markers, Holy Realm compatibility, and Germany Mengele civil-war or post-coup state markers.

## War Contagion

War Contagion is logged as an event-log evolution type:

- `constant:random_war_evolution_type.war_contagion = 4`

Stages:

| Stage | Chaos Tier | Declaration Count | Special Chance |
| --- | --- | --- | --- |
| Baseline | Calm World | 1 | 0% |
| Triangular Incident | 200+ | 3 | 0% |
| Four Fronts | 400+ | 4 | 20% |
| Contagious Ultimatums | 600+ | 5 | 35% |
| The War Week | 800+ | 6 | 55% |
| Open Season | 1000+ | 7-8 | 70% |

Only the highest enabled stage available under the current chaos tier is used. If an evolution is disabled in the event log UI, the event uses the next enabled lower stage or the baseline profile.

Event-log evolution rows and Random War event-detail preview rows display the stage names above directly, rather than the generic War Contagion type label.

## Player-Facing Events

- `chaosx.nr4.2`: aggressor report, with options to stand by the order or blame the general staff.
- `chaosx.nr4.3`: target report, with options to hold the line or mobilize reserves.
- `chaosx.news.104`: observer news report for humans, relevant majors, neighbors, and compatible special-country cases.

## Variables, Flags, And Constants

Constants live in:

- `common/script_constants/004_random_war_constants.txt`

Important runtime variables:

- `random_war_stage`
- `random_war_declaration_target_count`
- `random_war_special_chance`
- `random_war_context_ready`
- `random_war_declaration_fired_count`
- `global.random_war_last_stage`
- `global.random_war_last_declaration_count`
- `global.random_war_last_special_involved`
- `global.random_war_news_declaration_count`
- `global.random_war_news_country_count`
- `global.random_war_news_first_aggressor`
- `global.random_war_news_first_target`
- `global.random_war_news_third_country`
- `global.random_war_news_last_aggressor`
- `global.random_war_news_last_target`

Cooldown flags:

- `random_war_recent_aggressor`
- `random_war_recent_target`
- `random_war_staff_blamed`
- `random_war_chain_member`

Timed ideas:

- `random_war_hold_the_line`
- `random_war_reserve_mobilization`

Evolution log flags prevent duplicate first-stage milestone rows:

- `random_war_stage_1_logged`
- `random_war_stage_2_logged`
- `random_war_stage_3_logged`
- `random_war_stage_4_logged`
- `random_war_stage_5_logged`

## Cluster Integration

Random War is the required member of the repeatable **Wars** cluster. The cluster unlocks at Gathering Storm, rolls with the chaos-scaled cluster chance, and can be manually triggered from Settings regardless of current availability. The event can still fire normally when the automatic cluster roll does not fire. When the cluster fires, Random War runs through the same repeatable-event accounting path and appears in normal event history as well as the cluster log.

## Icons And Assets

No new final art assets are required.

Existing assets used:

- Report event image: `GFX_report_event_war_or_peace`
- News image: vanilla `GFX_news_event_generic_chaco_war`
- Target response idea images: existing `generic_wall_line` and `generic_infantry_bonus`

If a dedicated report image is added later, use:

- DDS path: `gfx/event_pictures/report_event_random_war.dds`
- Sprite name: `GFX_report_event_random_war`
- GFX file: `interface/chaosx_pictures.gfx`

If a dedicated news image is added later, use:

- DDS path: `gfx/event_pictures/news_event_random_war.dds`
- Sprite name: `GFX_news_event_random_war`
- GFX file: `interface/chaosx_pictures.gfx`

## Files

- `events/004_random_war.txt`
- `events/_chaosx_news.txt`
- `common/script_constants/004_random_war_constants.txt`
- `common/ideas/004_random_war_ideas.txt`
- `common/scripted_effects/004_random_war_effects.txt`
- `common/scripted_triggers/004_random_war_triggers.txt`
- `common/scripted_localisation/004_random_war_scripted_localisation.txt`
- `localisation/english/004_random_war_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`

## Future Plans

- Add more Wars cluster members so Random War can fire alongside related war incidents.
- Add regional weighting for neighbors, claims, cores, and hostile relations.
- Add temporary target-side defensive ideas if the event needs stronger country-specific aftermath.
- Add cluster-specific detail text for why a Random War firing picked its countries.

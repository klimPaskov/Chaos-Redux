# Event 009 White Peace Validation Matrix

This matrix records the static/script-path validation used for the final Event 009 implementation. It is not an in-game save validation; the checks below trace the implemented triggers, effects, constants, and UI state that the live event paths use.

## Availability and Safety

| Scenario | Expected result | Implementation evidence |
| --- | --- | --- |
| No active wars | Event 009 and Peace cluster are unavailable. | `calculate_white_peace_dynamic_cap` resets `global.white_peace_available = 0` and leaves `global.white_peace_skip_reason = constant:white_peace_skip_reason.no_active_war` unless active-war counters find a valid conflict. |
| Protected/special conflicts only | Event 009 remains unavailable and shows a protected/special conflict reason. | `can_country_be_white_peace_target` excludes `white_peace_protected_country`, `white_peace_protected_war_actor`, special chaos countries, and nonhuman countries; `global.white_peace_protected_war_actor_count` drives `protected_conflicts` skip text. |
| Civil war, subject, faction, near-capitulation, or unsafe capital | Candidate is rejected before pair selection. | `can_country_be_white_peace_target` blocks civil-war actors, subjects, factions, capitulated countries, countries at `surrender_progress >= 0.50`, and countries not controlling their capital. |
| Recent pair repeat | Same pair is blocked until exact reciprocal pair memory expires. | `mark_recent_white_peace_pair` sets `recent_white_peace_pair_<partner tag>` on the primary and `recent_white_peace_pair_<primary tag>` on the partner; `can_pair_receive_white_peace` checks `has_recent_white_peace_pair_with_prev`, and `global.white_peace_recent_pair_memory_count` feeds the compact skip reason. |
| Safe major pair before stage II | Event 009 is unavailable if no minor-safe pair exists, with a major-stage lock reason. | `can_major_pair_receive_white_peace_if_stage_unlocked` counts otherwise safe major-involved pairs into `global.white_peace_major_locked_pair_count`; `calculate_white_peace_dynamic_cap` maps that to `major_locked`. |

## Dynamic Weight and Branching

| Scenario | Expected result | Implementation evidence |
| --- | --- | --- |
| One safe minor war | Available with low live cap below ordinary event prominence. | With one normalized active war, one safe minor pair, and one minor-only pair, the environment cap is `125 + 90 + 85 + 60 = 360`, before the repeatable cap ratio and evolution multiplier. |
| Several safe minor wars | Weight rises with war clutter but environment cap never exceeds `1500`. | Active-war, safe-pair, minor-only, and clutter components are clamped individually, then `white_peace_environment_cap` is clamped by `constant:white_peace_weight.max_environment_cap`. |
| Stage I | Can settle several safe minor pairs, not an unbounded loop. | `select_white_peace_branch` can choose `multi_minor`; `white_peace_settlement_pair_cap` is two pairs, or three under high safe-minor pressure. |
| Stage II | Rare major-country branch is possible only after major stage pressure or unlock flag. | `can_country_be_white_peace_major_target` requires `white_peace_stage > stage_repeated_minor`, `global.white_peace_stage > stage_repeated_minor`, or the stage II/III global unlock flags. |
| Stage III | Broad branch can quiet broader safe clutter with capped reach and capped Chaos reduction. | `white_peace_settlement_cap.stage_3_pairs = 5`; broad branch Chaos reduction is clamped by `constant:white_peace_chaos_delta.broad_cap`. |
| Higher stages | Stronger branches become less likely. | `white_peace_stage_multiplier` reduces the live cap at stages I, II, and III to `0.78`, `0.55`, and `0.38` respectively. |
| Repeat firing | Normal repeatable recovery/decay still applies and lowers the live dynamic cap. | `calculate_white_peace_dynamic_cap` multiplies `white_peace_environment_cap` by `global.event_max_caps^9 / global.default_event_weight` before evolution multipliers; `get_event_weight` then clips the recovered stored weight to `global.white_peace_effective_dynamic_cap`. |
| Weighted pair choice | Candidate pairs are not pure random after vetoes. | `select_weighted_white_peace_primary_candidate` and `select_weighted_white_peace_partner_for_current_primary` use temporary scope arrays populated in proportion to `score_white_peace_pair`; both initial selection and follow-up multi/broad selection use this path. |

## Representative Weight Calculations

| State | Environment cap | Repeatable/evolution cap | Result |
| --- | ---: | ---: | --- |
| One safe minor war, no recent repeat decay | `125 + 90 + 85 + 60 = 360` | `360 * 1.00 * 1.00` | Live cap `360`, below default `1000`. |
| Same state after one normal repeatable cap decay to `500` | `360` | `360 * 0.50 * 1.00` | Live cap `180`, with the stored recovered weight still clipped by `get_event_weight`. |
| Eight active wars, four safe minor pairs, stage II | `125 + 540 + 340 + 240 + 175 = 1420` | `1420 * 1.00 * 0.55` | Live cap `781`; clutter raises chance but stage II lowers it. |
| Twelve active wars, six safe minor pairs, stage III | Raw `1640`, clamped to `1500` | `1500 * 1.00 * 0.38` | Live cap `570`; environment never exceeds `1500` before stage/repeat multipliers. |

## Logs, UI, and Achievements

| Surface | Expected result | Implementation evidence |
| --- | --- | --- |
| Event report | One acknowledgement option, no continue-war path. | `chaosx.nr9.2` through `.5` each contain one option, with variant-specific option keys and `apply_white_peace_current_context`. |
| Event history | History actor points to the selected primary. | `prepare_white_peace_runtime_context` saves `white_peace_primary` as `event_cluster_actor`; event-log actor mapping uses `white_peace_primary` for Event 009. |
| Evolution details | Stages I, II, and III record once. | `record_white_peace_evolution_if_needed` writes `constant:white_peace_event_log.evolution_type` and stage constants when evolution logging is enabled. |
| Peace cluster status | Unavailable states expose compact Event 009 reasons. | `GetWhitePeaceClusterUnavailableReason` is used by settings and event-log cluster availability for no active wars, no safe pair, recent memory, major-stage lock, and protected/special conflicts. |
| The Circular achievement | Supports the source prompt's alternate route. | `white_peace_achievement.broad_conflicts_required = 3` and `white_peace_achievement.broad_pairs_required = 5`; `apply_white_peace_current_context` sets `achievement_white_peace_the_circular_ready` if a broad branch meets either threshold. |

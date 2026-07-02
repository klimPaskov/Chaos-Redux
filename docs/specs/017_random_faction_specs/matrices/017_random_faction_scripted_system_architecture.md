# Event 17 scripted system architecture handoff

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `random_faction_prepare_runtime_context` | event root or global | event id, evolution state | target country and option targets | stores temp runtime context | entry event and manual test helper |
| `random_faction_collect_faction_options` | selected country | max option count | event targets for options | clears invalid option targets first | player and AI event setup |
| `random_faction_join_selected_faction` | selected country | selected leader target | faction membership and memory | applies shock, chaos, regional pressure, log | player option, AI option, cascade resolver |
| `random_faction_select_ai_option` | selected country | option targets and AI variables | selected option | reads ideology, relations, war, threat | AI resolver and cascade resolver |
| `random_faction_apply_regional_pressure` | selected country | selected leader and region | regional pressure values | marks neighbors and faction leader memory | after successful join |
| `random_faction_schedule_followup` | selected country | evolution state and region | delayed country event | sets follow-up flags | Evolution I and later |
| `random_faction_clear_pressure` | country | none | clean state | cancels obsolete decisions and missions | cleanup events, on-action hooks if approved |

## Trigger map

| Trigger | Scope | Notes |
| --- | --- | --- |
| `is_random_faction_eligible_country` | country | should reuse shared normal diplomacy and special chaos exclusions |
| `is_random_faction_valid_faction_leader` | country | validates leader exists, faction exists, and leader can receive normal members |
| `random_faction_target_can_join_leader` | target country | compare selected country and leader target safely |
| `random_faction_has_valid_option_count` | selected country | allows event to show unavailable if no faction targets |
| `random_faction_can_show_pressure_category` | country | drives decision category visibility |
| `random_faction_can_use_faction_leader_decisions` | faction leader | checks active target region and cooldown |

## Constants

Create `common/script_constants/chaosx_random_faction_constants.txt` or fold into an existing event constants file if that is the repo pattern.

Suggested groups:

- `random_faction_option.max_player_options`
- `random_faction_cooldown.recent_alignment_days`
- `random_faction_pressure.neighbor_days`
- `random_faction_pressure.region_days`
- `random_faction_evolution.evo1_delay_min`
- `random_faction_evolution.evo1_delay_max`
- `random_faction_evolution.evo3_cascade_min`
- `random_faction_evolution.evo3_cascade_max`
- `random_faction_ai.ideology_weight`
- `random_faction_ai.proximity_weight`
- `random_faction_ai.threat_weight`
- `random_faction_ai.war_weight`

For timed flag fields that reject script constants, use a file-scoped literal mirrored with the script constant and document the mirror in the same helper file.

## Cleanup plan

The cleanup helper must clear:

- pressure flags
- selected target flags
- temporary variables
- active pressure decisions
- active timed missions
- stale region pressure where held by a country
- global event targets if any are used

Cleanup should run from event outcomes and from narrow invalidation hooks. Avoid adding broad daily iteration without explicit approval.

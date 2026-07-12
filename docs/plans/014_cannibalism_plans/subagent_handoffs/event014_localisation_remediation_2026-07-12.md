# Event 014 localisation remediation — 2026-07-12

## Result

The bounded localisation findings from `event014_localisation_reaudit_2026-07-12.md` are remediated except for staged achievement visibility, which the parent explicitly retained for a separate Event Details-equivalent implementation.

This pass changed localisation presentation only. It did not change gameplay meaning, mechanics, achievement definitions, specifications, spreadsheets, Event Details, assets, or terminal-hunt/Wendigo design. No fallback, placeholder, or simplification was introduced.

The shared workspace advanced to commit `60853561d` (`chore: snapshot current project state`) while this subtask was in progress. That snapshot includes the new scripted-localisation source/route selectors and the first localisation tranche. This subagent did not create that commit or any other commit.

## Files and exact identifiers

### `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`

Added two selectors backed by the stored spread data:

- `GetCannibalismSpreadSourceName`
  - `cannibalism_spread_source_inbound`
  - `cannibalism_spread_source_external`
- `GetCannibalismSpreadRouteLabel`
  - `cannibalism_spread_route_retreat`
  - `cannibalism_spread_route_prisoner_transfer`
  - `cannibalism_spread_route_convoy`
  - `cannibalism_spread_route_volunteer_return`
  - `cannibalism_spread_route_occupation_turnover`
  - `cannibalism_spread_route_deliberate_seed`
  - `cannibalism_spread_route_conquest`
  - `cannibalism_spread_route_survivor`

The route selector exhausts the live eight-value `cannibalism_spread_route` enum. No generic fallback branch was added. Its callers are reached only with a validated live spread entry, and the warning state or receiving country holds the corresponding source and route variables.

### `localisation/english/014_cannibalism_l_english.yml`

#### Dynamic source country and route

Before, the spread warning and arrival strings referred only to a generic “route,” “documented wartime route,” or “external source.” After, the recorded source country and one of the eight concrete route labels are shown in the warning, first arrival, reinfection, repeated arrival, and arrival effect tooltip.

Exact keys:

- Source/route values: `cannibalism_spread_source_inbound`, `cannibalism_spread_source_external`, `cannibalism_spread_route_retreat`, `cannibalism_spread_route_prisoner_transfer`, `cannibalism_spread_route_convoy`, `cannibalism_spread_route_volunteer_return`, `cannibalism_spread_route_occupation_turnover`, `cannibalism_spread_route_deliberate_seed`, `cannibalism_spread_route_conquest`, `cannibalism_spread_route_survivor`.
- Callers: `chaosx.nr14.60.d`, `chaosx.nr14.61.d`, `chaosx.nr14.61.reinfection.d`, `chaosx.nr14.62.d`, `cannibalism_external_spread_arrival_tt`.

#### Indirect spoilers

Before, three reachable pre-reveal strings discussed a later public revelation, a later identity, or a hidden leader. After, each describes only evidence currently visible to the player.

Exact keys:

- `cannibalism.evolution.summary`
- `cannibalism_warlord_read_the_common_signs_tt`
- `cannibalism.gui.open_network.tt`

The pre-reveal wording now covers wartime predation, ritual cells, territorial networks, coordinated Host operations, common symbols, stolen corridors, divided local command, actors, state nodes, routes, and countermeasures without foreshadowing the concealed identity.

#### Dynamic international-response and reconstruction values

Before, costs and durations duplicated literal tuning values. After, they render their owning `cannibalism_international_response_cost`, `cannibalism_reconstruction`, or `cannibalism_warlord_decision` constants directly.

Exact keys:

- `cannibalism_synchronize_warlord_attack_desc`
- `cannibalism_joint_suppression_cost_text`
- `cannibalism_convergence_interdiction_cost_text`
- `cannibalism_island_blockade_cost_text`
- `cannibalism_island_blockade_effect_tt`
- `cannibalism_island_landing_cost_text`
- `cannibalism_island_landing_effect_tt`
- `cannibalism_island_rescue_cost_text`
- `cannibalism_aftermath_identification_cost_text`
- `cannibalism_aftermath_institution_cost_text`
- `cannibalism_aftermath_memorial_cost_text`
- `cannibalism_compact_ratification_cost_text`
- `cannibalism_compact_ratification_effect_tt`
- `cannibalism_maintain_international_inspection_compact_desc`
- `cannibalism_compact_vigilance_success_tt`

#### Dynamic unified-command values

Before, hostility gates, population floors and losses, receipt counts and yields, cooldowns, air gates, counterwar results, and terminal costs duplicated literal values. After, fixed tuning renders from `cannibalism_unified_decision_cost`, `cannibalism_unified_hostility`, `cannibalism_unified_operation`, or `cannibalism_unified_profile`, while route-adjusted costs continue to render from their initialized runtime variables.

Exact keys:

- Hostility: `cannibalism_unified_command_category_desc`, `cannibalism_unified_world_hostility_pressure_desc`, `cannibalism_unified_world_hostility_mobilized_desc`, `cannibalism_unified_world_hostility_total_desc`.
- Consumption: `cannibalism_unified_rapid_consumption_requirements_tt`, `cannibalism_unified_rapid_consumption_cost_text`, `cannibalism_unified_rapid_consumption_effect_tt`, `cannibalism_unified_managed_consumption_requirements_tt`, `cannibalism_unified_managed_consumption_cost_text`, `cannibalism_unified_managed_consumption_effect_tt`, `cannibalism_unified_mobile_consumption_requirements_tt`, `cannibalism_unified_mobile_consumption_cost_text`, `cannibalism_unified_mobile_consumption_effect_tt`, `cannibalism_unified_battlefield_consumption_requirements_tt`, `cannibalism_unified_battlefield_consumption_cost_text`, `cannibalism_unified_battlefield_consumption_effect_tt`.
- Air and formations: `cannibalism_unified_air_program_foundation_tt`, `cannibalism_unified_legion_requirements_tt`, `cannibalism_unified_legion_cost_text`, `cannibalism_unified_legion_effect_tt`, `cannibalism_unified_bone_guard_requirements_tt`, `cannibalism_unified_bone_guard_cost_text`, `cannibalism_unified_bone_guard_effect_tt`, `cannibalism_unified_island_specialist_requirements_tt`, `cannibalism_unified_siege_specialist_requirements_tt`, `cannibalism_unified_march_specialist_requirements_tt`, `cannibalism_unified_prison_specialist_requirements_tt`, `cannibalism_unified_origin_specialist_cost_text`.
- Receipts and counterwar: `cannibalism_unified_army_operation_effect_tt`, `cannibalism_unified_naval_operation_effect_tt`, `cannibalism_unified_convoy_harvest_requirements_tt`, `cannibalism_unified_convoy_harvest_cost_text`, `cannibalism_unified_convoy_harvest_effect_tt`, `cannibalism_unified_counterwar_conversion_requirements_tt`, `cannibalism_unified_counterwar_conversion_effect_tt`.
- Terminal mobilization: `cannibalism_unified_terminal_consumption_requirements_tt`, `cannibalism_unified_terminal_consumption_cost_text`, `cannibalism_unified_terminal_consumption_effect_tt`, `cannibalism_unified_terminal_consume_controlled_state_desc`, `cannibalism_unified_locked_terminal_consumption_requirements_tt`, `cannibalism_unified_locked_terminal_consumption_cost_text`, `cannibalism_unified_locked_terminal_consumption_effect_tt`.

Population quantities consistently display the stored thousands unit with `K`. The negative counterwar-relief constant is described as changing World Hostility, avoiding a misleading “reduces by -15” construction.

#### Implementation terminology and punctuation

Before, three strings exposed internal evolution/generation/ledger terminology. After, they describe evidence, forged transfers, prosecution records, and visible outcomes in world-state language.

Exact keys:

- `cannibalism_amnesty_requirements_tt`
- `cannibalism_prison_infiltrate_transfers_effect_tt`
- `cannibalism_captured_warlord_anti_decapitation_escape_tt`

Semicolons and em dashes were replaced with full sentences in these exact keys:

- `cannibalism_unified_command_burden_desc`
- `cannibalism_raise_scavenger_warband_effect_tt`
- `cannibalism_raise_feast_cohort_effect_tt`
- `cannibalism_raise_origin_specialist_effect_tt`
- `cannibalism_raise_bone_guard_effect_tt`
- `cannibalism_seed_foreign_formation_effect_tt`
- `cannibalism_captured_warlord_anti_decapitation_escape_tt`
- `cannibalism_unified_battlefield_consumption_requirements_tt`
- `cannibalism_unified_army_operation_effect_tt`
- `cannibalism_unified_naval_operation_effect_tt`

### `localisation/english/chaosx_achievements_l_english.yml`

Before, the affected achievement tooltips duplicated literal country, island, duration, retained-warlord, Larder, route, continent, consumed-population, Network Reach, Chaos, and compact thresholds. After, they render the same constants used by the achievement triggers and supporting effects.

Exact keys:

- `achievement_cannibalism_three_front_containment_tooltip`
- `achievement_cannibalism_silent_islands_reclaimed_tooltip`
- `achievement_cannibalism_warlord_without_master_tooltip`
- `achievement_cannibalism_host_of_unification_tooltip`
- `achievement_cannibalism_all_mouths_one_command_tooltip`
- `achievement_cannibalism_continental_larder_tooltip`
- `achievement_cannibalism_stop_the_reveal_tooltip`
- `014_cannibalism_ordinary_world_end_DESC`
- `achievement_cannibalism_ordinary_world_end_tooltip`
- `014_cannibalism_wendigo_world_end_DESC`
- `achievement_cannibalism_wendigo_world_end_tooltip`
- `achievement_cannibalism_global_burial_detail_tooltip`

The consumed-population requirement now displays `cannibalism_achievement.continental_consumed_population_k` as `K people`, preserving the trigger’s stored unit. The stop-the-reveal tooltip also replaces “before the public reveal” with the in-world “before the command consolidates.”

## Validation evidence

- Spread data is available at every caller: warning state storage is in `common/scripted_effects/014_cannibalism_spread_effects.txt:427-429`; receiving-country storage is at lines `562-563` and `593-594`; event calls are at lines `433-435` and `666-673`.
- Selector coverage is exact: two source localisation keys, eight unique route-enum values, eight unique route localisation keys, and five source plus five route getter calls across the warning/arrival/reinfection strings.
- All 248 `constant:category.key` references across the two localisation files and the Event 014 scripted-localisation file resolve to live `common/script_constants` definitions. No affected achievement threshold retains a numeric literal outside a dynamic token.
- The international/unified audit range retains no numeric literal outside interpolation tokens; the only unrelated numeric text in that range is the scenario identifier `SCN-010`.
- Both edited English localisation files retain UTF-8 BOM, `l_english:` headers, key syntax without `:0`, zero leading-space keys, zero malformed declarations, zero duplicate keys, and balanced interpolation brackets.
- The scripted-localisation file has balanced braces, tab indentation, and no literal section-sign or pound-sign formatting characters.
- The main Event 014 localisation file contains zero semicolons or em dashes. The retired phrases `Evolution I evidence`, `generation-checked`, `character-outcome ledger`, `public revelation`, `later identity`, `hidden leader`, `thirty-day`, `above one thousand chaos`, and `Chaos is above 1000` are absent from the audited localisation surfaces.
- The ten new spread source/route localisation keys each occur exactly once across English localisation.

## Remaining parent-owned blocker

The staged visibility requirement remains unresolved in the static achievement definitions for these thirteen achievements:

- `014_cannibalism_repentant_weapon`
- `014_cannibalism_break_the_island_host`
- `014_cannibalism_warlord_without_master`
- `014_cannibalism_host_of_unification`
- `014_cannibalism_all_mouths_one_command`
- `014_cannibalism_continental_larder`
- `014_cannibalism_stop_the_reveal`
- `014_cannibalism_defeat_hannibal`
- `014_cannibalism_break_the_winter_hunger`
- `014_cannibalism_ordinary_world_end`
- `014_cannibalism_wendigo_world_end`
- `014_cannibalism_global_burial_detail`
- `014_cannibalism_no_empty_state`

Per parent direction, this pass did not edit `common/achievements/chaos_redux_achievements.txt` or create an unapproved static-hidden fallback. The parent owns the separate Event Details-equivalent staged-discovery surface. Until that surface is implemented and validated, Event 014 still cannot claim complete staged-achievement visibility.

## Simplifications, omissions, fallbacks, and commit status

- No remediation item assigned to this subtask was simplified or omitted.
- No fallback or placeholder was used.
- Staged achievement visibility was explicitly excluded and remains the blocker above.
- No new terminal-hunt or Wendigo content was designed or added.
- This subagent created no commit.

## Skills used

- `chaos-redux-events`
- `hoi4-decisions-missions`
- `hoi4-focus-trees`
- `chaos-redux-subagents`

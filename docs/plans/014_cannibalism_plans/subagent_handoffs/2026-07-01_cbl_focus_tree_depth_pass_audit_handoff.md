# Event 014 CBL Focus Tree Depth Pass Audit Handoff

Scope: Event 014 Cannibal Commune focus tree depth pass.

Files audited:

- `common/national_focus/014_cannibalism_focus_tree.txt`
- `common/script_constants/014_cannibalism_constants.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/ideas/014_cannibalism_ideas.txt`
- `common/ai_strategy/014_cannibalism.txt`
- `interface/014_cannibalism.gfx`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/events/014_cannibalism.md`
- `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md`

References used:

- `AGENTS.md`
- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`
- Vanilla focus precedent for OR prerequisites using multiple `focus = ...` entries in one `prerequisite` block

## High-Priority Fixes

| Priority | File and identifier | Status | Notes |
| --- | --- | --- | --- |
| High | `common/national_focus/014_cannibalism_focus_tree.txt`, route prerequisites | No patch needed | Current OR prerequisites use one `prerequisite` block where route convergence is intended: `cbl_captured_depot_inventory`, `cbl_field_kitchen_conversions`, `cbl_prisoner_ledger_administration`, `cbl_hunger_column_organization`, `cbl_convoy_ambush_plans`, `cbl_rail_corridor_hunts`, `cbl_mainland_hunting_corridors`, `cbl_couriers_between_tables`, and `cbl_world_as_larder_gate`. |
| High | `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_no_public_feasts` / `cbl_hunting_ground_doctrine` | No patch needed | Mutual exclusion is correctly symmetric through opposing `mutually_exclusive` blocks. Downstream `cbl_couriers_between_tables` correctly accepts either route parent. |
| High | `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_cannibal_pact_compact` / `cbl_refuse_the_wider_pact` | No patch needed | Pact and solitary routes are mutually exclusive and set separate route flags plus decision unlock flags. |
| High | `common/scripted_triggers/014_cannibalism_triggers.txt`, `cannibalism_cbl_last_table_map_control` | No patch needed | Current trigger matches `localisation/english/014_cannibalism_l_english.yml` and `docs/events/014_cannibalism.md`: at least four controlled states and at least one hunting-ground project. It uses `greater_than_or_equals` for the project variable and a `NOT < constant` trigger for controlled states. |
| Low | `localisation/english/014_cannibalism_l_english.yml`, `cbl_port_harvests` | Fixed | Removed stale title and description for the old removed focus id. |

## Route Coverage Table

| Required route | Implemented branch | Status | Evidence and notes |
| --- | --- | --- | --- |
| Opening | `cbl_first_table`, `cbl_seal_the_origin_state`, `cbl_night_larder_columns`, `cbl_black_kitchens` | Covered | Uses state hardening, reinforcement forces, support equipment, building slots, factories, and network pressure. |
| Command choices | `cbl_council_of_knives`, `cbl_warlord_kitchen`, `cbl_hannibal_discipline` | Covered | Three-way mutually exclusive fork. Hannibal discipline is availability-gated by `cannibalism_hannibal_or_unifier_exists`. |
| Supply economy | `cbl_captured_depot_inventory`, `cbl_field_kitchen_conversions`, `cbl_prisoner_ledger_administration`, `cbl_commune_ration_codes` | Covered | Rewards vary between equipment, state modifiers, ideas, manpower, stability, and network pressure. |
| Military | `cbl_hunger_column_organization`, `cbl_scavenger_party_mobility`, `cbl_butcher_pack_shock_doctrine`, `cbl_prison_processions`, `cbl_hannibal_cadres` | Covered | Uses Army XP, CP, multiple unit spawn helpers, manpower, equipment, and Hannibal linkage. |
| Island, coastal, inland expansion | `cbl_silent_anchorages`, `cbl_coastal_port_lists`, `cbl_convoy_ambush_plans`, `cbl_prison_road_route`, `cbl_rail_corridor_hunts`, `cbl_mainland_hunting_corridors` | Covered | Origin triggers route island/coastal/inland entries, then converge into claims, war goals, hunting grounds, convoys, trains, fuel, and network gains. |
| Restrained versus hunting-ground discipline | `cbl_no_public_feasts`, `cbl_hunting_ground_doctrine`, `cbl_restrained_consumption_registers`, `cbl_runaway_consumption_accounts`, `cbl_empty_larder_war_discipline` | Covered | Mutually exclusive discipline split; restrained path has achievement payoff through `cannibalism_empty_larder_achieved`. |
| Courier network | `cbl_couriers_between_tables` | Covered | Accepts either discipline parent and records courier network strength through country/global flags and variables. |
| Pact versus solitary route | `cbl_cannibal_pact_compact`, `cbl_refuse_the_wider_pact`, `cbl_listen_for_hannibal`, `cbl_last_table_preparations` | Covered | Mutually exclusive late route split with pact courier unlocks, solitary raid unlocks, and Hannibal hook. |
| Last Table map mission and formable | `cbl_map_the_final_larder`, `cbl_proclaim_the_last_table`, `cannibalism_cbl_map_the_last_table`, `cannibalism_cbl_last_table_map_mission` | Covered | Focus unlocks timed map decision; mission success sets `cannibalism_last_table_map_validated`; proclamation sets `CBL_LAST_TABLE`, `cannibalism_last_table_formed`, and `cannibalism_table_for_one_achieved`. |
| Region projects | `cbl_controlled_region_projects`, `cannibalism_cbl_region_consumption_project` | Covered | Post-formation projects consume resources and add hunting-ground/network/death-record consequences. |
| World-end gate | `cbl_world_as_larder_gate`, `cannibalism_world_end_route_available`, `cannibalism_try_world_end_route` | Covered with design risk | Gate can be reached from Hannibal pact linkage or Last Table proclamation, then still requires global table, accepted unifier/Hannibal, chaos, network, cult nodes, and commune count. |

## Missing or Simplified Content

- No required route from `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md` is missing from the current 36-focus tree.
- `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_world_as_larder_gate`: current prerequisite is intentionally OR between `cbl_listen_for_hannibal` and `cbl_proclaim_the_last_table`. If parent design requires every world-end attempt to pass through the Last Table formable, this is too permissive; the current plan text supports both the Hannibal/pact and Last Table late routes.
- `common/ai_strategy/014_cannibalism.txt`: route-aware strategic AI exists, but there is no separate ordered national-focus strategy plan. This is a remaining behavior-depth risk, not a blocker found in scoped focus script.
- `common/script_constants/014_cannibalism_constants.txt`, `cannibalism_last_table_requirement`: `controlled_states = 4` and `hunting_ground_projects = 1` are used as minimum counts by the current scripted trigger and match player-facing text.

## Icon Coverage Table

| Route group | Focus icon coverage | Status |
| --- | --- | --- |
| Opening | 4 of 4 focus icon ids referenced in the tree are registered in `interface/014_cannibalism.gfx`. | OK |
| Command choices | 3 of 3 registered. | OK |
| Supply economy | 4 of 4 registered. | OK |
| Military | 5 of 5 registered. | OK |
| Island/coastal/inland expansion | 6 of 6 registered. | OK |
| Discipline | 5 of 5 registered. | OK |
| Pact/solitary/Hannibal | 4 of 4 registered. | OK |
| Last Table and world-end | 5 of 5 registered. | OK |

Total focus icon result: 36 focus icon references, 36 matching sprite registrations, no missing normal focus sprites.

## Localisation and Reward Mismatch List

- All 36 current focus ids in `common/national_focus/014_cannibalism_focus_tree.txt` have matching title and `_desc` keys in `localisation/english/014_cannibalism_l_english.yml`.
- Removed stale localisation keys `cbl_port_harvests` and `cbl_port_harvests_desc`; no current focus uses that id.
- `cbl_empty_larder_war_discipline` reward and achievement wiring match: the focus sets `cannibalism_empty_larder_achieved`, and `common/achievements/chaos_redux_achievements.txt` checks that flag for `014_cannibalism_empty_larder`.
- `cbl_proclaim_the_last_table` reward and achievement wiring match: the focus sets `cannibalism_table_for_one_achieved`, and `common/achievements/chaos_redux_achievements.txt` checks that flag for `014_cannibalism_table_for_one`.
- No reward text mismatch was found in the scoped files.

## AI Behavior Gaps

- Every focus has an `ai_will_do` block.
- `common/ai_strategy/014_cannibalism.txt` has route-aware strategic entries for holding before global table formation, wartime reinforcement, island/coastal pressure, pact patience, solitary raids, Last Table preparation, and world-end pressure.
- Remaining gap: focus selection is mostly local weighting rather than a strict national-focus plan. The AI can still choose among command and discipline forks by broad weight rather than a full route script.
- `cbl_world_as_larder_gate` has safe AI behavior: base zero, with pressure only when `cannibalism_world_end_route_available = yes`.

## Changed Files

- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_cbl_focus_tree_depth_pass_audit_handoff.md`

## Changed Focus IDs

- None.

## Route Behavior Before and After

- Before: current route behavior was already coherent for the 36-focus depth pass.
- After: route behavior is unchanged. The only gameplay-facing edit removed unused localisation for an old focus id that is no longer present in the tree.

## Localisation Keys and Icon IDs Changed

- Removed localisation keys: `cbl_port_harvests`, `cbl_port_harvests_desc`.
- Added localisation keys: none.
- Changed icon ids: none.

## Meaningful Validation

- Verified focus count: 36.
- Verified duplicate focus ids: none.
- Verified all 36 focus ids have title and `_desc` localisation after the stale-key cleanup.
- Verified all 36 focus icon references have matching sprite registrations in `interface/014_cannibalism.gfx`.
- Verified `localisation/english/014_cannibalism_l_english.yml` still has UTF-8 BOM after patch.
- Verified Last Table chain wiring: `cbl_map_the_final_larder` sets `cannibalism_last_table_preparation_unlocked`; `cannibalism_cbl_map_the_last_table` starts `cannibalism_cbl_last_table_map_mission`; mission success sets `cannibalism_last_table_map_validated`; `cbl_proclaim_the_last_table` requires validation and sets the formable/achievement flags.
- Verified achievement flag wiring for `cbl_empty_larder_war_discipline` and `cbl_proclaim_the_last_table` against `common/achievements/chaos_redux_achievements.txt`.

## Skipped Meaningful Validation

- No in-game load or runtime save validation was run from this subagent environment.
- No full HOI4 parser validation was run.
- No visual render pass was run for focus icons; validation covered sprite registration only.

## Remaining Route Risks

- Confirm parent intent for `cbl_world_as_larder_gate`: the current OR route allows Hannibal/pact world-end entry without `cbl_proclaim_the_last_table`.
- Consider a future AI focus-plan pass if CBL needs deterministic route personas rather than local route weights.
- The workspace contains many unrelated dirty files outside this audit scope. They were not touched.

## Plan Handoff Path

No new broad improvement plan was written. The existing route-depth plan remains:

`docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md`

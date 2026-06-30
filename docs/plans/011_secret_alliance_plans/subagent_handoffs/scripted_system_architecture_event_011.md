# Event 011 Secret Alliance scripted-system architecture handoff

## Scope

This pass inspected the Event 011 Secret Alliance specs, the earlier event stub, Chaos Redux helper patterns, HOI4 decision and on-action references, and existing event-log and dynamic-helper conventions. No gameplay files were edited in this pass.

Working-tree note: `AGENTS.md` is currently deleted in the worktree. I used the last committed `AGENTS.md` content as the operative repo guidance and did not restore or modify the deleted file.

## Sources read

- `AGENTS.md` from `HEAD:AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/011_secret_alliance_specs/README.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_mechanics.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_decisions_missions.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_ai_balance_localisation.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_map.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_ai_matrix.md`
- `docs/specs/011_secret_alliance_specs/focus_graphs/011_secret_alliance_progression_map.md`
- `docs/specs/011_secret_alliance_specs/inspection/011_secret_alliance_source_reading_manifest.md`
- `docs/super_events/011_secret_alliance_super_event_research.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`

## Existing patterns inspected

- `events/011_anti_player_pact.txt` was the earlier stub. It immediately declared several wars, created `anti_player_pact`, and fired the reveal report. This was queued for replacement by hidden-state setup and a centralized reveal helper.
- `localisation/english/011_anti_player_pact_l_english.yml` has the current Event 011 localisation, including `Anti-[Root.GetName] Pact` in an event title.
- `common/scripted_effects/009_white_peace_effects.txt` has the best existing weighted candidate precedent. It builds weighted scope arrays from computed scores, selects with `random_scope_in_array`, saves event targets, records evolution entries, and mirrors constants with file-scoped `@` values where timed flags cannot use script constants.
- `common/scripted_triggers/009_white_peace_triggers.txt` has clean country and pair validation split into small triggers.
- `common/script_constants/009_white_peace_constants.txt` is the best constants file model for event-specific tuning groups and schema comments.
- `common/scripted_effects/007_fury_effects.txt` has another weighted actor and target selection model, plus cleanup of transient flags and variables.
- `common/scripted_triggers/007_fury_triggers.txt` has useful `can_pay_*_cost` decision-payment patterns.
- `common/script_constants/007_fury_constants.txt` is the best model for actor selection, target scoring, decision cost, and AI tuning groups.
- `common/scripted_effects/002_zombie_outbreak_effects.txt` has `establish_anti_zombie_league`, `join_anti_zombie_league_effect`, and `dismantle_anti_zombie_league` as faction creation, joining, and cleanup precedents.
- `common/on_actions/chaosx_on_actions.txt` already uses `on_war_relation_added` for centralized war-state reactions. Event 011 should integrate there.
- `common/scripted_effects/chaosx_events_log_effects.txt` has default actor and evolution-entry patterns. Event 011 should save the target before history recording and route evolution rows through the existing event-log helpers.
- `common/scripted_effects/chaosx_dynamic_effects.txt` and `common/scripted_effects/chaosx_dynamic_effects.md` should be reused only for shared helpers. Event 011-specific helpers should stay in an Event 011 file.
- `common/scripted_triggers/chaosx_dynamic_triggers.txt` already defines `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems`. Event 011 should call these instead of duplicating exclusions.
- `localisation/english/chaosx_factions_l_english.yml` currently defines `anti_player_pact: "Secret Alliance"`.

## Proposed files

Add these files in the implementation pass:

- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `common/scripted_guis/011_secret_alliance_scripted_gui.txt` if the Dossier Board is implemented as scripted GUI
- `interface/011_secret_alliance_dossier.gui` if the Dossier Board needs a dedicated GUI surface
- `docs/events/011_secret_alliance.md`

Update these existing files in the implementation pass:

- `events/011_anti_player_pact.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/011_anti_player_pact_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_factions_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml` or a new Event 011 decision localisation file if that is the local convention at implementation time
- `localisation/english/chaosx_gui_l_english.yml` if scripted GUI is used

Optional faction framework files if public pact rules or goals become custom rather than vanilla-neutral:

- `common/factions/templates/secret_alliance_public_pact.txt`
- `common/factions/rules/secret_alliance_public_pact_rules.txt`
- `common/factions/goals/secret_alliance_public_pact_goals.txt`

## Script constants plan

Create `common/script_constants/011_secret_alliance_constants.txt` with clear schema comments. Use `constant:category.key` in helpers and decisions. Mirror only duration values into file-scoped `@SECRET_ALLIANCE_*` constants inside script files when the target field rejects script constants.

Proposed groups:

- `secret_alliance_event_log`
  - `event_id = 11`
  - `evolution_type = 11`
  - `stage_hidden_foundation = 0`
  - `stage_widening_table = 1`
  - `stage_patron_counterplay = 2`
  - `stage_public_compact = 3`
  - `reveal_route_war = 1`
  - `reveal_route_evidence = 2`
  - `reveal_route_ultimatum = 3`
  - `reveal_route_leak = 4`
  - `reveal_route_patron = 5`
- `secret_alliance_foundation`
  - `founder_count = 3`
  - `baseline_member_cap = 3`
  - `evolution_i_member_cap_base`
  - `evolution_i_member_cap_chaos_step`
  - `evolution_ii_member_cap_base`
  - `evolution_iii_member_cap_base`
  - `minimum_valid_founder_pool`
- `secret_alliance_candidate_score`
  - `base`
  - `minor_bonus`
  - `independent_bonus`
  - `outside_faction_bonus`
  - `border_bonus`
  - `same_continent_bonus`
  - `target_neighbor_bonus`
  - `target_relation_negative_bonus`
  - `ideology_opposition_bonus`
  - `target_claim_bonus`
  - `candidate_claim_bonus`
  - `already_in_faction_penalty`
  - `major_baseline_penalty`
  - `target_war_block_score`
  - `min_score`
  - `max_score`
- `secret_alliance_major_patron_score`
  - `base`
  - `major_bonus`
  - `rival_ideology_bonus`
  - `faction_leader_bonus`
  - `target_strength_ratio_bonus`
  - `target_expansion_bonus`
  - `member_relation_bonus`
  - `chaos_tier_bonus`
  - `evidence_penalty`
  - `cohesion_bonus`
  - `min_score`
  - `max_score`
- `secret_alliance_thresholds`
  - `suspicion_category_open`
  - `evidence_partial_member_reveal`
  - `evidence_full_member_reveal`
  - `evidence_public_reveal`
  - `pressure_ultimatum`
  - `cohesion_leak_low`
  - `war_preparation_public_reveal`
  - `preparedness_spend_on_reveal`
  - `infiltration_major_patron_expose`
- `secret_alliance_hidden_pulse`
  - `invitation_base_days`
  - `incident_base_days`
  - `leak_check_base_days`
  - `target_dossier_refresh_days`
  - `stale_targeted_decision_cleanup_days`
- `secret_alliance_decision_cost`
  - `investigation_base_cp`
  - `investigation_base_pp`
  - `defense_base_cp`
  - `defense_base_equipment`
  - `diplomacy_base_pp`
  - `border_base_command_power`
  - `war_prep_base_army_xp`
  - `fuel_reserve_base_fuel`
  - `industry_scale_divisor`
  - `evidence_discount_step`
  - `pressure_surcharge_step`
  - `ai_hint_pp_cost_default`
- `secret_alliance_ai_weight`
  - `founder_acceptance_base`
  - `founder_suicide_risk_penalty`
  - `patron_acceptance_base`
  - `target_investigation_weight`
  - `target_defense_weight`
  - `target_diplomacy_weight`
  - `target_border_weight`
  - `target_war_prep_weight`
  - `neutral_reaction_weight`
- `secret_alliance_cleanup`
  - `invalid_member_review_days`
  - `delayed_war_join_retry_days`
  - `post_public_hidden_state_clear_days`
  - `dossier_card_stale_days`

## Helper map

### Scripted triggers in `common/scripted_triggers/011_secret_alliance_triggers.txt`

| Helper | Scope | Inputs | Output | Notes |
| --- | --- | --- | --- | --- |
| `secret_alliance_pact_exists` | any | global flag or global target | boolean | True once Event 011 hidden state exists. |
| `secret_alliance_is_public` | any | global flag or target flag | boolean | True after central reveal. |
| `is_secret_alliance_target` | country | country flags and global target | boolean | Target country marker. |
| `is_secret_alliance_member` | country | member flags | boolean | Hidden or public member. |
| `is_secret_alliance_hidden_member` | country | member flags | boolean | True before public reveal for this country. |
| `is_secret_alliance_public_member` | country | member flags | boolean | True after reveal. |
| `is_secret_alliance_founder` | country | founder flag | boolean | Used for history, leadership, achievements. |
| `is_secret_alliance_patron` | country | patron flag | boolean | Used for leadership priority and patron route. |
| `can_be_secret_alliance_target` | country | normal country checks | boolean | Exclude special chaos countries, nonhuman countries, invalid temporary diplomacy, and destroyed countries. |
| `can_be_secret_alliance_founder_for_prev_target` | candidate country | `PREV` target | boolean | Must not be target, target subject, already member, special chaos country, actual nonhuman country, or at war with `PREV`. Baseline should reject majors. |
| `can_be_secret_alliance_member_candidate_for_prev_target` | candidate country | `PREV` target | boolean | Expansion candidate version. It can be looser than founder validation, but still blocks war with target. |
| `can_be_secret_alliance_major_patron_candidate_for_prev_target` | candidate country | `PREV` target | boolean | Requires major or strategic weight, not at war with target before patron reveal route, and not target subject. |
| `secret_alliance_member_valid_for_public_faction` | member country | global target and leader | boolean | Used during reveal before adding to faction. |
| `secret_alliance_member_can_join_target_war` | member country | target and public leader | boolean | Checks not already at war with target and whether a direct or faction war join path is legal. Exact fields need implementation validation. |
| `secret_alliance_target_can_open_counterplay` | target country | suspicion, evidence, active event | boolean | Opens the decision category. |
| `secret_alliance_has_active_decision_slot_for_type` | target country | action type temp variable | boolean | Enforces active cap by investigation, defensive, and border or diplomacy families. |
| `can_pay_secret_alliance_trace_diplomatic_pouches_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_turn_courier_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_break_radio_net_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_audit_foreign_missions_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_build_public_dossier_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_guard_rail_port_nodes_cost` | target country | dynamic cost variables | boolean | Payment trigger for the decision. |
| `can_pay_secret_alliance_quiet_talks_member_cost` | target country | dynamic cost variables and selected member | boolean | Targeted member decision trigger. |
| `can_pay_secret_alliance_face_saving_exit_cost` | target country | dynamic cost variables and selected member | boolean | Targeted member decision trigger. |
| `can_pay_secret_alliance_contingency_plans_cost` | target country | dynamic cost variables | boolean | War prep decision trigger. |

### Scripted effects in `common/scripted_effects/011_secret_alliance_effects.txt`

| Helper | Scope | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- | --- |
| `secret_alliance_prepare_runtime_context` | event root target | ROOT target | global target, founder arrays, target variables | Called by `chaosx.nr11.1` immediate before hidden setup and history recording. |
| `secret_alliance_reset_runtime_context` | any | none | cleared transient targets and arrays | Called before failed setup retry or cleanup. |
| `secret_alliance_initialize_target_state` | target country | constants | target flags and variables | Sets suspicion, evidence, preparedness, infiltration, pressure, cohesion, war preparation, and public reveal baseline values. |
| `secret_alliance_count_valid_founders_for_current_target` | target country | candidate trigger | `secret_alliance_valid_founder_count` | Blocks founding if fewer than three candidates exist. |
| `secret_alliance_score_current_founder_candidate_for_target` | candidate country | `PREV` target | temp `secret_alliance_candidate_score` | Uses constants and current diplomatic state. |
| `secret_alliance_add_current_founder_candidate_to_weighted_pool` | candidate country | temp score | temp array entry repeats | Based on 007 Fury and 009 White Peace weighted pools. |
| `secret_alliance_select_weighted_founder_candidate` | target country | candidate pool | `event_target:secret_alliance_selected_candidate` | Selects one founder. |
| `secret_alliance_register_selected_founder` | target country | selected candidate event target | member arrays and country flags | Adds founder to `global.secret_alliance_members` and `global.secret_alliance_founders`. |
| `secret_alliance_select_founders_for_current_target` | target country | founder count constant | exactly three founders or failure flag | Loops selection, marks selected countries to avoid duplicates, then revalidates no founder is at war with target. |
| `secret_alliance_apply_foundation` | target country | selected founders | global active flag, event-log actor state | Commits hidden pact only after validation passes. |
| `secret_alliance_initialize_member_variables` | member country | role constants | member confidence and exposure variables | Called for founders, invited members, and patron. |
| `secret_alliance_rebuild_member_arrays` | any | member flags | global member arrays | Recovery helper for stale arrays after load or cleanup. |
| `secret_alliance_record_evolution_if_needed` | target country | stage and route variables | event-log evolution row | Mirrors 009 White Peace event-log pattern. |
| `secret_alliance_invitation_pulse` | target country | member cap and score helpers | possible new hidden member | Called from scheduled event or bounded on-action, not global daily scans. |
| `secret_alliance_score_current_invitation_candidate` | candidate country | `PREV` target | temp score | Uses expansion score constants. |
| `secret_alliance_invite_selected_member` | target country | selected candidate | member flags and target suspicion side effects | Adds hidden member and optional incident trail. |
| `secret_alliance_select_major_patron` | target country | patron score helpers | `event_target:secret_alliance_major_patron` | Evolution II patron selection. |
| `secret_alliance_apply_major_patron` | target country | major patron target | patron flags, member arrays, pressure changes | Adds patron without public reveal unless route demands it. |
| `secret_alliance_open_counterplay_category` | target country | suspicion and evidence thresholds | visible decision category | Activates category and initializes dossier variables. |
| `secret_alliance_prepare_decision_cost_context` | target country | temp `secret_alliance_action_type` and optional selected member | cost variables and localisation variables | Runs before decision availability and effect text. |
| `secret_alliance_pay_decision_cost` | target country | temp `secret_alliance_action_type` | subtracts resources | Must be called in `complete_effect` because `custom_cost_trigger` only displays and gates. |
| `secret_alliance_complete_trace_diplomatic_pouches` | target country | payment helper | evidence and suspicion changes | Investigation decision. |
| `secret_alliance_complete_turn_courier` | target country | payment helper and member target | evidence, known member chance, member exposure | Investigation decision. |
| `secret_alliance_complete_break_radio_net` | target country | payment helper | evidence, delay hidden pulses | Investigation decision. |
| `secret_alliance_complete_guard_rail_port_nodes` | target country | payment helper | preparedness and sabotage resistance | Defensive decision. |
| `secret_alliance_complete_quiet_talks_member` | target country | selected member target | member confidence loss and exit chance | Diplomacy targeted decision. |
| `secret_alliance_complete_face_saving_exit` | target country | selected member target | removes or weakens member | Diplomacy targeted decision. |
| `secret_alliance_complete_contingency_plans` | target country | payment helper | preparedness and war reveal response | War prep decision. |
| `secret_alliance_on_war_relation_added` | on-action ROOT or FROM pair | ROOT attacker, FROM defender | possible immediate reveal | Called from `common/on_actions/chaosx_on_actions.txt` under `on_war_relation_added`. |
| `secret_alliance_reveal_public_pact` | target country | temp reveal route and optional reveal actor | public flags, faction, event-log row, report event | Central reveal helper. Idempotent and guarded by `secret_alliance_reveal_in_progress`. |
| `secret_alliance_prepare_public_leader` | target country | patron, founders, member strength | `event_target:secret_alliance_public_leader` | Patron first, then strongest valid founder, then strongest member fallback. |
| `secret_alliance_create_public_faction` | public leader country | faction loc key | faction created and leader saved | Uses current `create_faction` precedent unless a faction template is added. |
| `secret_alliance_set_public_faction_name` | public leader country | target event target | faction name key | Dynamic target name support must be validated before relying on it. |
| `secret_alliance_mark_public_members` | target country | member array | public flags and known member arrays | Converts hidden members to public members and stops hidden invitations. |
| `secret_alliance_add_member_to_public_faction` | public leader or target loop | member scope | member added or deferred | Leaves invalid cases flagged for retry rather than silently deleting them. |
| `secret_alliance_call_public_members_to_war_if_needed` | target country | reveal route and active wars | war join attempts and deferred flags | War route forces immediate response where engine-valid. Evidence route does not automatically start a war. |
| `secret_alliance_public_war_join_pulse` | target country | deferred member flags | retried joins | Scheduled only while deferred join flags exist. |
| `secret_alliance_cleanup_invalid_member` | member country | global target | member removed or downgraded | Handles annexed, puppeted, or invalid countries. |
| `secret_alliance_cleanup_target_gone` | any | missing target | system teardown | Clears active hidden/public state if the target no longer exists. |
| `secret_alliance_cleanup_hidden_state_after_public_reveal` | target country | public flag | clears hidden-only flags and timers | Keeps history and founder flags intact. |
| `secret_alliance_dismantle_public_pact` | public leader or target | pact ended | faction state and variables cleaned | Use only for explicit end state. |

## Event target and global target plan

Use global event targets only for persistent system anchors:

- `event_target:secret_alliance_target`
- `event_target:secret_alliance_public_leader`
- `event_target:secret_alliance_major_patron`
- `event_target:secret_alliance_latest_revealed_member`
- `event_target:secret_alliance_last_incident_member`

Use short-lived event targets during helper chains:

- `event_target:secret_alliance_selected_candidate`
- `event_target:secret_alliance_current_member_target`
- `event_target:secret_alliance_reveal_actor`
- `event_target:secret_alliance_candidate_primary`

Use arrays because the event is Minor Fire-Once and needs one global compact:

- `global.secret_alliance_members`
- `global.secret_alliance_founders`
- `global.secret_alliance_public_members`
- `global.secret_alliance_known_members`
- `global.secret_alliance_deferred_war_members`

Store IDs or state variables for recovery and localisation:

- target variable `secret_alliance_target_id`
- global variable `secret_alliance_target_id`
- member variable `secret_alliance_member_target_id`
- member variable `secret_alliance_member_confidence`
- member variable `secret_alliance_member_exposure`
- member variable `secret_alliance_member_role`
- target variable `pact_suspicion`
- target variable `pact_evidence`
- target variable `pact_preparedness`
- target variable `pact_infiltration`
- target variable `pact_pressure`
- target variable `pact_cohesion`
- target variable `pact_war_preparation`

Use country flags for boolean lifecycle:

- target flag `secret_alliance_target`
- target flag `secret_alliance_public_reveal`
- member flag `secret_alliance_member`
- member flag `secret_alliance_hidden_member`
- member flag `secret_alliance_founder`
- member flag `secret_alliance_patron`
- member flag `secret_alliance_wavering`
- member flag `secret_alliance_exposed`
- member flag `secret_alliance_public_member`
- member flag `secret_alliance_delayed_war_join`
- member flag `secret_alliance_war_call_attempted`
- global flag `secret_alliance_active`
- global flag `secret_alliance_public`

## Candidate scoring and founding validation

Founder selection should copy the 007 Fury and 009 White Peace weighted-pool shape:

1. In the target scope, clear the temp founder pool.
2. Iterate valid countries.
3. In each candidate scope, call `can_be_secret_alliance_founder_for_prev_target`.
4. Score the candidate with `secret_alliance_score_current_founder_candidate_for_target`.
5. Add repeated candidate entries to a temp array based on the computed score.
6. Select with `random_scope_in_array`.
7. Save the selected country as `event_target:secret_alliance_selected_candidate`.
8. Register the founder, mark it as selected for this pass, and repeat until the founder count is three.
9. Revalidate all founders before committing the compact.

The no-war-with-target rule must exist in both the candidate trigger and the final post-selection commit check:

- `can_be_secret_alliance_founder_for_prev_target` includes `NOT = { has_war_with = PREV }`.
- `secret_alliance_select_founders_for_current_target` aborts and calls `secret_alliance_reset_runtime_context` if any selected founder entered war with the target before `secret_alliance_apply_foundation`.

Baseline selection should reject majors outright unless the spec is later changed. Evolution II adds majors through the patron path instead of founder selection.

## Immediate reveal design

Use `on_war_relation_added`, not only `on_declare_war`, because the specs require all war paths to reveal the pact. HOI4 docs identify `on_war_relation_added` as firing whenever two countries end up at war, with ROOT as attacker and FROM as defender.

Integration point:

- Update `common/on_actions/chaosx_on_actions.txt` under `on_war_relation_added` to call `secret_alliance_on_war_relation_added = yes`.

Helper behavior:

1. If no pact exists or the pact is already public, exit.
2. Check ROOT hidden or public member against FROM target.
3. Check FROM hidden or public member against ROOT target.
4. If either pair matches, save the member as `event_target:secret_alliance_reveal_actor`.
5. Set temp `secret_alliance_reveal_route = constant:secret_alliance_event_log.reveal_route_war`.
6. Scope to `event_target:secret_alliance_target`.
7. Call `secret_alliance_reveal_public_pact = yes`.

Guard with `secret_alliance_reveal_in_progress` so war calls made during reveal do not recursively fire a second reveal.

## Public faction creation and name strategy

Current Event 011 uses `create_faction = anti_player_pact`. Anti-Zombie League uses `create_faction_from_template` and separate faction rules and goals. For Secret Alliance, the first implementation should use the simpler existing `create_faction` path unless public pact rules or goals need bespoke behavior.

Recommended implementation:

- Keep or replace `anti_player_pact` with `secret_alliance_public_pact` in `localisation/english/chaosx_factions_l_english.yml`.
- Create the faction in `secret_alliance_create_public_faction`.
- Save the leader as `event_target:secret_alliance_public_leader`.
- Use `secret_alliance_prepare_public_leader` to select leadership in this order:
  - valid major patron
  - strongest valid founder
  - strongest valid member

Dynamic name risk:

- Event localisation can safely use `[secret_alliance_target.GetName]` once the event target is saved.
- Faction name localisation may not support event-target dynamic namespaces in all UI contexts.
- The implementation pass should test whether `set_faction_name = secret_alliance_public_pact_name` with a key like `secret_alliance_public_pact_name: "Anti-[secret_alliance_target.GetName] Pact"` renders correctly.
- If dynamic faction naming fails, use a static faction name or reserve dynamic target naming for event, report, super-event, and dossier text.
- Do not rely on unvalidated `[Root.GetName]` in a faction name key.

## War-call strategy

War route reveal:

- Public reveal should happen first.
- Public leader should be selected and faction created before war joins.
- Every valid member should receive `secret_alliance_public_member`.
- Members that can legally join the faction should be added through `secret_alliance_add_member_to_public_faction`.
- Members already at war with the target should only be marked and logged.
- Members not at war with the target should be called or declared into war only through `secret_alliance_call_public_members_to_war_if_needed`.
- Each member gets `secret_alliance_war_call_attempted` after a valid attempt.
- Invalid or blocked members get `secret_alliance_delayed_war_join` and go into `global.secret_alliance_deferred_war_members`.

Evidence, leak, ultimatum, and patron reveal routes:

- Public reveal should create the public compact and expose members.
- Evidence and leak routes should not automatically start a war unless the decision or route explicitly requires it.
- Ultimatum route can branch into war only after refusal or route-specific effect.
- Patron route can reveal the patron without forcing every member into immediate war unless the stage design says it should.

Unsupported or uncertain field:

- There is no confirmed Chaos Redux precedent for a clean generic faction call-to-war helper. If HOI4 lacks a direct dynamic call effect for this case, the fallback is controlled `declare_war_on` with validation. That fallback changes war creation semantics and should be explicitly approved during implementation before use.

## Decision cost helper strategy

Decision costs should follow the `hoi4-decisions-missions` guidance:

- Use `custom_cost_trigger` and `custom_cost_text` for display and availability.
- Subtract the actual resource cost in `complete_effect`.
- Use `ai_hint_pp_cost` only where a constant PP hint is useful for AI.
- Do not show resource costs that the complete effect does not actually pay.

Recommended helper shape:

- `secret_alliance_prepare_decision_cost_context`
  - Input: temp `secret_alliance_action_type`
  - Optional input: `event_target:secret_alliance_current_member_target`
  - Output: target-scope variables used by scripted localisation and cost triggers
- `secret_alliance_pay_decision_cost`
  - Input: same action type
  - Output: subtracts PP, command power, army XP, air XP, equipment, fuel, stability, or other resource values
- Specific `can_pay_secret_alliance_*_cost` triggers for decisions that need non-identical resource mixes

Decision IDs from the spec should map to helpers:

- `secret_alliance_trace_diplomatic_pouches`
- `secret_alliance_turn_courier`
- `secret_alliance_break_radio_net`
- `secret_alliance_audit_foreign_missions`
- `secret_alliance_build_public_dossier`
- `secret_alliance_guard_rail_port_nodes`
- `secret_alliance_vet_military_staff`
- `secret_alliance_harden_munitions_plants`
- `secret_alliance_secure_capital_ministries`
- `secret_alliance_protect_war_industries`
- `secret_alliance_quiet_talks_member`
- `secret_alliance_face_saving_exit`
- `secret_alliance_pressure_neutrals`
- `secret_alliance_controlled_leak`
- `secret_alliance_demand_embassy_expulsions`
- `secret_alliance_sweep_frontier_safehouses`
- `secret_alliance_seal_courier_pass`
- `secret_alliance_limited_border_reprisal`
- `secret_alliance_contingency_plans`
- `secret_alliance_fuel_reserve_security`
- `secret_alliance_local_defense_committees`
- `secret_alliance_rally_friendly_governments`
- `secret_alliance_prepare_public_war_case`

Targeted member decisions should use `target_array` or controlled activation so the UI does not scan and display every country every day.

## Dynamic localisation plan

Add `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` for:

- `GetSecretAllianceEstimatedMemberCount`
- `GetSecretAllianceKnownMemberList`
- `GetSecretAllianceLastIncidentText`
- `GetSecretAllianceDecisionCostText`
- `GetSecretAllianceRevealRouteText`
- `GetSecretAlliancePublicName`
- `GetSecretAlliancePreparednessLevel`
- `GetSecretAllianceSuspicionLevel`
- `GetSecretAllianceEvidenceLevel`

Localisation files should keep player-facing prose focused on visible world state. Hidden mechanics, internal caps, and exact scoring should remain in tooltips only when the player has earned that information.

## Event-log integration

Update `common/scripted_effects/chaosx_events_log_effects.txt`:

- In `events_log_set_default_actor_for_current_event`, map Event 011 to `event_target:secret_alliance_target` when that target exists.
- For evolution entries, set:
  - `events_log_evolution_event_id = constant:secret_alliance_event_log.event_id`
  - `events_log_evolution_type = constant:secret_alliance_event_log.evolution_type`
  - `events_log_evolution_stage` based on the stage constant
  - `events_log_evolution_has_actor = 1`
  - `event_target:events_log_evolution_actor = event_target:secret_alliance_target` or reveal actor as appropriate
- Call `record_events_log_evolution_entry` only after these variables and event targets are ready.

Event 011 stub report should become one of several reveal reports:

- hidden foundation report for logs only
- suspicion or dossier open report
- public reveal report
- war reveal report
- patron reveal report

## Cleanup hooks

Recommended cleanup integration:

- `on_war_relation_added` in `common/on_actions/chaosx_on_actions.txt`
  - `secret_alliance_on_war_relation_added = yes`
- existing faction on-actions if needed
  - review `on_join_faction`
  - review `on_leave_faction`
  - review `on_assume_faction_leadership`
- annexation or capitulation on-actions if present in the file
  - call `secret_alliance_cleanup_invalid_member`
  - call `secret_alliance_cleanup_target_gone`

Avoid a global daily scan. If a repeated review is needed, use a scheduled event or a weekly active-only pulse gated by `secret_alliance_active` and documented in the event file. The committed AGENTS guidance requires explicit permission before adding world-iterating daily, weekly, or monthly on-actions.

Cleanup helpers should preserve history flags and founder identity while clearing hidden-only operational state:

- clear `secret_alliance_hidden_member`
- clear timed incident flags
- clear member target cards after public reveal
- clear stale targeted decision activations
- keep `secret_alliance_founder`
- keep `secret_alliance_public_member` until the public pact ends
- keep event-log variables needed for history

## Integration order

1. Add constants in `common/script_constants/011_secret_alliance_constants.txt`.
2. Add triggers in `common/scripted_triggers/011_secret_alliance_triggers.txt`.
3. Add foundation and selection helpers in `common/scripted_effects/011_secret_alliance_effects.txt`.
4. Rework `events/011_anti_player_pact.txt` so `chaosx.nr11.1` calls `secret_alliance_prepare_runtime_context` and `secret_alliance_apply_foundation` instead of immediate wars.
5. Add centralized reveal helpers and update `common/on_actions/chaosx_on_actions.txt`.
6. Add event-log actor and evolution mappings.
7. Add decisions and dynamic cost helpers.
8. Add scripted localisation and localisation strings.
9. Add dossier GUI if selected for the implementation tranche.
10. Add docs in `docs/events/011_secret_alliance.md`.

## Validation notes for the implementation pass

Task-specific validation should include:

- Confirm the hidden founder setup produces exactly three founders.
- Confirm no founder can be at war with the target at commit time.
- Confirm the setup aborts cleanly if fewer than three candidates exist.
- Confirm `on_war_relation_added` reveals the pact when either war direction is member against target.
- Confirm public reveal is idempotent if multiple war relations are added in the same burst.
- Confirm decision custom costs display and the matching `complete_effect` pays the same resource mix.
- Confirm targeted member decisions do not display stale or invalid members.
- Confirm faction name renders correctly if dynamic naming is attempted.
- Confirm war-call helper does not duplicate wars or call members already at war with the target.
- Confirm cleanup removes hidden-only state after public reveal while preserving founder and history data.

## Risks and unresolved engine checks

- Dynamic target names in faction names are not confirmed. Validate before relying on `Anti-[secret_alliance_target.GetName] Pact` in the faction UI.
- A direct generic faction call-to-war effect was not confirmed in existing Chaos Redux files. War joining may need a route-specific validated effect or explicit approval for controlled `declare_war_on`.
- Targeted decisions with many potential member targets can become noisy. Prefer arrays or activated targeted decisions once members become known.
- Global member arrays assume the event remains Minor Fire-Once. If Event 011 becomes repeatable, all arrays, global event targets, and flags need a per-instance design.
- Timed flag durations may reject `constant:` values. Mirror duration constants with file-scoped `@SECRET_ALLIANCE_*` values only where required.
- The public pact may need a faction template if custom faction rules or goals are part of the accepted public-stage design. The current plan keeps that optional to avoid adding unused framework.

## Files changed in this pass

- `docs/plans/011_secret_alliance_plans/subagent_handoffs/scripted_system_architecture_event_011.md`

No gameplay scripts, localisation, decisions, constants, on-actions, assets, or specs were edited in this pass.

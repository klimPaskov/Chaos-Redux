# Event 021 scripted-system architect handoff

Status: complete within the exclusive scripted-system scope. The parent can wire the event, decisions, shared cluster/scenario registry, event log, AI, localization, and CXT files against the contracts below.

## Changed files

- `common/script_constants/021_random_civil_war_constants.txt`
- `common/scripted_triggers/021_random_civil_war_triggers.txt`
- `common/scripted_effects/021_random_civil_war_effects.txt`
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/scripted_system_architect_handoff.md`

No event, decision, localization, AI, cluster, scenario, workbook, asset, generated-agent, or shared helper file was edited by this subagent.

## Parent-facing wrappers

The stable names requested by the parent are present.

| Identifier | Surface | Contract |
| --- | --- | --- |
| `event021_random_civil_war_prepare_target` | effect | COUNTRY input; refreshes pressure, computes bounded target weight, and publishes `random_civil_war_target_weight` plus a candidate flag. |
| `event021_random_civil_war_commit_opening` | effect | COUNTRY input after parent-owned state/country mutation; commits the validated plan, registers one theater, and consumes reservation arrays. |
| `event021_refresh_country_state` | effect | COUNTRY input; recomputes hidden Fracture Pressure and refreshes State Authority/pressure bands. |
| `event021_country_can_manage_crisis` | trigger | COUNTRY input; normal-human active crisis side with a valid management role. |
| `event021_country_can_be_target` | trigger | COUNTRY input; normal-human, non-terminal, non-reserved target with a valid opposition route. |
| `event021_cleanup_crisis` | effect | COUNTRY input; unregisters front/theater/queue/exposure runtime state, preserves durable receipts, and starts cooldown/memory windows. |
| `event021_apply_evolution_i` | effect | ANY input; enables the already-unlocked Evolution I runtime flag and refreshes caps. |
| `event021_apply_evolution_ii` | effect | ANY input; retains Evolution I and enables Evolution II. |
| `event021_apply_evolution_iii` | effect | ANY input; retains earlier evolutions, enables the non-terminal global threat source, and refreshes caps. |
| `event021_apply_settlement` | effect | COUNTRY input; records the settlement family, updates authority/pressure, starts reconstruction and successor grace, and prepares recurrence. |
| `event021_global_review_batch` | effect | ANY input; opens a fixed review/critical-queue budget without iterating countries. |
| `event021_register_cxt_extension` | effect | COUNTRY input from an existing bounded CXT hook; idempotently records Event 021 setup-carrier membership and registers the country for review. |
| `event021_reduce_pressure` | effect | COUNTRY input; consumes optional `random_civil_war_pending_pressure_delta`, otherwise applies centralized reconstruction relief. |
| `event021_add_authority` | effect | COUNTRY input; consumes optional `random_civil_war_pending_authority_delta`, otherwise applies administrative restoration plus live condition deltas. |

## Helper map

### State and target layer

`event021_initialize_country_state`, `event021_update_pressure_band`, and `event021_update_authority_band` own persistent defaults and the four State Authority bands (`0-14` Collapse, `15-39` Failing, `40-69` Contested, and `70-100` Cohesive).

`event021_random_civil_war_prepare_target`, `event021_prepare_archetype_weights`, and `event021_prepare_opening_severity` produce the target score, route weights, and Limited/Serious/Severe/Critical opening severity from centralized constants.

`event021_reserve_target`, `event021_begin_opening_transaction`, `event021_reserve_state`, `event021_record_anchor_state`, `event021_prepare_parent_remnant`, and `event021_prepare_force_package` cover target reservation, connected-state planning, capital/anchor persistence, remnant viability, and dynamic force/stockpile planning.

The state planner uses `global.random_civil_war_plan_states` and `global.random_civil_war_reserved_states`, plus a single global planning lock, so rollback can safely release the one uncommitted opening plan without touching committed theatres.

### Event 006 and same-tag layer

`event021_prepare_event6_admission` bridges normal `random_civil_war_event6_package_id` into temporary `independence_wave_execution_package_id` and invokes the existing Event 006 package preflight/admission predicates.

`event021_confirm_event6_identity`, `event021_record_event6_origin`, and `event021_apply_event6_origin_adapter` keep admission, identity proof, and Event 021 origin recording separate.

The adapter rejects actual non-human countries and origin collisions and never calls `independence_wave_prepare_country_origin`, the Event 006 dispatcher, or any Event 006 fired/evolution/league state mutation.

`event021_prepare_same_tag_route` and `event021_cleanup_same_tag_route` provide the one-state/all-island loyalty-contest route without changing tags or transferring territory.

### Front, exposure, and global scheduler layer

`event021_register_front`, `event021_unregister_front`, `event021_set_priority_front`, and `event021_clear_priority_front` maintain aligned front ID/actor/anchor arrays and the selected-front global target.

`event021_apply_regional_exposure`, `event021_advance_regional_exposure`, and `event021_cleanup_regional_exposure` maintain the Observed/Pressured/Penetrated/Mobilizing exposure ladder and source pointer.

`event021_sync_evolution_state`, `event021_prepare_evolution_log_context`, `event021_schedule_country_review`, and `event021_refresh_global_capacity` derive stage context, publish event-log inputs without logging, schedule bounded reviews, and set theater/front caps.

`event021_register_global_country`, `event021_global_review_batch`, `event021_review_current_country`, and `event021_finish_global_review_batch` provide the bounded review budget. The parent must feed a bounded set of country scopes through `event021_review_current_country`; no unrestricted periodic world loop is defined here.

`event021_queue_critical_country`, `event021_dequeue_critical_country`, `event021_launch_critical_country`, and `event021_finish_critical_launch` provide a capped critical queue and a global launch target without firing an event internally.

### Settlement and cleanup layer

`event021_apply_settlement`, `event021_prepare_recurrence`, `event021_reconstruction_tick`, and `event021_update_achievement_state` maintain settlement, reconstruction, successor grace, recurrence score/date, and six durable achievement-state flags.

`event021_cleanup_crisis`, `event021_cleanup_global_registry`, `event021_clear_scenario_bypass`, and `event021_clear_global_threat_source` clear runtime state and global event targets while preserving durable settlement/origin/achievement receipts.

`event021_register_cxt_extension` and `event021_mark_setup_carrier_consumed` are registration markers only. The parent-owned CXT effect remains responsible for consuming the hidden carrier idea.

## Constants and tuning table plan

The constants file defines Event 021 IDs/stages, severity and archetype enums, authority and pressure bands, exposure stages, settlement/origin/scenario enums, achievement IDs, pressure components, authority deltas, target-weight components, review/cooldown bands, theater/front/generation caps, force ratios, scenario intensity shares, and settlement thresholds.

The four namespaces already referenced by the parent decision file are included: `event021_action_cost`, `event021_action_tuning`, `event021_mission_tuning`, and `event021_ai`.

All numeric tuning used by the three new script files is centralized in `common/script_constants/021_random_civil_war_constants.txt`.

## Parent migration and call sequence

1. Call `event021_refresh_country_state` and `event021_random_civil_war_prepare_target` once per bounded target candidate, then reserve the target and call `event021_prepare_opening_severity`.
2. In the host scope call `event021_begin_opening_transaction`, save the selected `random_civil_war_current_state` and `random_civil_war_anchor_state` targets, call `event021_reserve_state` for each connected state, then call `event021_record_anchor_state`, `event021_prepare_parent_remnant`, and `event021_prepare_force_package`.
3. Perform the parent-owned country creation, identity, state transfer, war, ideas, AI, and event-log operations only after plan validation; finish with `event021_random_civil_war_commit_opening`, or call `event021_rollback_opening` on any failed preflight.
4. For Event 006, set the package and anchor variables in the dormant package scope, call `event021_prepare_event6_admission`, perform the package-specific parent-owned setup, call `event021_confirm_event6_identity`, then call `event021_record_event6_origin` and `event021_apply_event6_origin_adapter`.
5. Register every committed front with `event021_register_front`, set the selected front with `event021_set_priority_front`, and call `event021_unregister_front` when that front settles.
6. Call `event021_apply_settlement`, `event021_reconstruction_tick`, and then `event021_cleanup_crisis` from the parent outcome path. Call `event021_cleanup_global_registry` only after the parent has proved that both active-theater and active-front counts are zero.
7. From an existing bounded CXT hook call `event021_register_cxt_extension`, and from the bounded review hook call `event021_global_review_batch`, feed its limited country batch through `event021_review_current_country`, then call `event021_finish_global_review_batch`.

## Event targets and cleanup

Short-lived chain targets are `random_civil_war_host_country`, `random_civil_war_target_country`, `random_civil_war_current_state`, `random_civil_war_anchor_state`, `random_civil_war_current_actor`, and `random_civil_war_exposure_source`.

Persistent global targets are `random_civil_war_priority_front_state`, `random_civil_war_launch_target`, `random_civil_war_exposure_source_country`, `random_civil_war_global_anchor_state`, and `random_civil_war_scenario_target`.

The corresponding clear operations are in `event021_clear_priority_front`, `event021_finish_critical_launch`, `event021_cleanup_global_registry`, and `event021_clear_scenario_bypass`.

## Validation and evidence

- Read all 41 files under `docs/specs/021_random_civil_war_specs/`, including the master spec, manifest, all ten parts, matrices, research/role/revision notes, and every listed subagent prompt.
- Read `AGENTS.md`, `chaos-redux-events/SKILL.md`, `chaos-redux-subagents/SKILL.md`, the relevant Event 006 runtime/country-registry documentation, and the existing Event 004/007 civil-war/cluster/triggerable-scenario patterns before editing.
- Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localization, scopes, on actions, event modding, decision modding, idea modding, and AI modding.
- Read the relevant vanilla documentation for script concepts/constants, effects, triggers, dynamic variables, script collections, and scripted localization.
- Confirmed brace depth is zero for all three new script files, with no negative depth.
- Confirmed the requested parent constant namespaces and their decision-file references exist in the new constants file.
- Confirmed the new code has no unrestricted country iteration, no `<=`/`>=` operators, no unary-minus variable expressions, and no call to the Event 006 normal initializer. The text search hits for `any_country` are comments describing the deliberate omission, not executable blocks.
- No Hearts of Iron IV process was launched and no live save validation was attempted, per repository rules.

## Unsupported analysis and risks

The installed callable tool inventory did not expose the required `hoi4_agent_tools` server or `hoi4.event_inspect`, `hoi4.probability_inspect`, `hoi4.probability_compare`, or the `chaosx_ai_probability_auditor` route. The required Event 021/Event 006 read-only MCP inspection and weighted baseline/compare evidence therefore remain unresolved and must be completed by the parent when those routes are available.

The Event 006 package-specific executor is intentionally not implemented in these files because the installed executor's normal path calls `independence_wave_prepare_country_origin`; the parent must supply or verify a package-specific adapter that applies the package identity without opening Event 006 provenance.

The shared cluster member registration, scenario ID allocation, event-log registration, decisions, CXT hidden-idea carrier definition, country creation, front war creation, and state transfer are intentionally deferred to the parent because they were outside the exclusive write scope.

No unapproved fallback actor, package, GUI, animation, asset, or world-iteration substitute was added.

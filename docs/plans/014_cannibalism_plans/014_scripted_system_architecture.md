# Event 014 Scripted System Architecture

Status: implementation architecture, plan only

Owner: main Event 014 implementation agent

This document defines the script boundaries, APIs, persistent data, deterministic selection rules, lifecycle behavior, and shared-system changes for Event 014. It does not authorize gameplay edits by the architecture subagent.

## 1. Architecture outcome

Event 014 should be implemented as an event-owned state machine with five supporting integration layers.

1. The event owns hosts, state nodes, spread entries, consumption transactions, warlord incarnations, convergence, Hannibal, local defeat, global defeat, and both terminal routes.
2. The global random-event system owns only availability, pre-fire preparation, dispatch, fire-once history, and event-log handoff.
3. A shared dynamic effect owns exact state civilian population loss. Event 014 wraps it with larder, hunger, node, and cumulative-consumption bookkeeping.
4. The Deaths system owns death reporting when enabled. Real population loss must remain identical when Deaths display and tracking are disabled.
5. Existing zombie helpers own the reusable Wendigo runtime package. Event 014 owns the merged Wendigo-Hannibal identity and terminal countdown.

The runtime must be deterministic in multiplayer. Host selection, state selection, convergence host selection, and Wendigo merge selection use scored arrays and stable tie-breaking. They do not use `random_list`.

The runtime must not use broad `on_daily`, `on_weekly`, or `on_monthly` hooks. One hidden delayed event owns the recurring pulse. Narrow lifecycle on-actions only reconcile or wake that pulse.

## 2. Reference decisions

The design follows these engine and repository precedents.

- Regular event targets carry the selected first host and initial state through the dispatch effect chain.
- One global event target is justified for the pulse anchor because the scheduler must survive beyond the originating chain. It must be cleared during global cleanup.
- Arrays store scopes. A monotonic generation on every actor, node, queue entry, and reusable tag incarnation prevents stale delayed callbacks from mutating a later incarnation.
- Vanilla player-safe country consolidation calls `change_tag_from` on the future host before annexing the former player country. Event 014 must follow that order.
- Script constants are used for shared tuning. Timed flag durations must first be copied into a variable because timed flag fields do not reliably accept `constant:` tokens.
- `modify_state_population_by_percent` is not suitable for Event 014. It does not provide the exact Deaths-disabled behavior or transaction outputs required here.

## 3. File ownership map

| Surface | File | Required ownership |
|---|---|---|
| Event constants | `common/script_constants/014_cannibalism_constants.txt` | All Event 014 enums, thresholds, timing, score weights, yields, slot counts, and route values |
| Scenario constants | `common/script_constants/014_cannibalism_scenario_constants.txt` | Scenario ID alias, type values, scale values, and scenario-only setup tuning |
| Event effects | `common/scripted_effects/014_cannibalism_effects.txt` | Event-owned transactions and state-machine transitions |
| Event triggers | `common/scripted_triggers/014_cannibalism_triggers.txt` | Eligibility, live-scope guards, route gates, cleanup gates, and GUI predicates |
| Event on-actions | `common/on_actions/014_cannibalism_on_actions.txt` | Narrow adapters that normalize callback scopes and call Event 014 handlers |
| Event script | `events/014_cannibalism.txt` | Entry dispatch, visible responses, delayed pulse, evolutions, convergence, reveal, merge, and terminal bridges |
| Event decisions | `common/decisions/014_cannibalism_decisions.txt` | Player actions that call the event-owned API only |
| Event ideas | `common/ideas/014_cannibalism_ideas.txt` | Stage, route, warlord, unified, and terminal modifiers |
| Event scripted localisation | `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` | Route text, actor text, slot tag text, and anti-spoiler display logic |
| Event localisation | `localisation/english/014_cannibalism_l_english.yml` | All player-facing event, decision, idea, tooltip, and scenario text |
| Event assets | `interface/014_cannibalism.gfx` and asset manifest | Stable sprite registration and final asset wiring |
| Country slots | `common/country_tags/chaosx_countries.txt`, `common/countries/Cannibal Warlord.txt`, and the CBL country package | Eight reusable warlord tags, one dedicated ordinary unified host, and their complete history packages |
| Random-event registry | `common/scripted_effects/chaosx_logic_effects.txt` | Fire-once registration and active-pool eligibility |
| Dispatch preparation | `common/scripted_effects/chaosx_settings_effects.txt` | Call pre-fire selection before generic `chaosx.nr[EVENT_ID].1` dispatch |
| Event log | `common/scripted_effects/chaosx_events_log_effects.txt` | Default actor, N/A weight, event history, and evolution rows |
| Shared population effect | `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` | Exact civilian population-loss transaction and API documentation |
| Shared classifications | `common/scripted_triggers/chaosx_dynamic_triggers.txt` and `.md` | Special-country and nonhuman classification |
| Deaths cause | `common/script_constants/chaos_meter_constants.txt`, `common/scripted_effects/chaos_meter_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`, and `localisation/english/chaosx_chaos_meter_l_english.yml` | Full reason 15 pipeline |
| World threat | `common/scripted_effects/chaosx_dynamic_effects.txt`, `common/scripted_triggers/chaosx_world_threat_triggers.txt`, and `docs/systems/world_threat_mechanic.md` | Include the Event 014 source in shared aggregation, predicates, and documentation |
| Wendigo package | `common/scripted_effects/zombie_special_project_effects.txt` | Preserve the existing ZZZ profile and call the existing Wendigo template helper without moving the profile to CBL |
| Wendigo terminal guard | `events/002_zombie_outbreak.txt` | Prevent the old Wendigo world-end event from bypassing Event 014 transformation |
| Triggerable scenario registry | Existing triggerable-scenario constants, effects, triggers, localisation, GUI, docs, and sheet | Register Event 014 as stable scenario 10 |

## 4. Event and scenario identities

### 4.1 Event IDs

The following event IDs are reserved inside namespace `chaosx.nr14`.

| ID | Purpose | Visibility |
|---|---|---|
| `.1` | Entry dispatcher that consumes pre-fire targets and initializes the system | Hidden |
| `.2` | First-host response | Visible to the selected host when human |
| `.3` | Observer report | Visible to eligible human observers |
| `.10` | Recurring runtime pulse | Hidden |
| `.20` | Evolution I presentation and response | Visible when enabled and relevant |
| `.21` | Evolution II presentation and response | Visible when enabled and relevant |
| `.22` | Evolution III presentation and response | Visible when enabled and relevant |
| `.30` | Warlord convergence response | Visible to affected human warlords |
| `.31` | Hannibal reveal | Visible |
| `.32` | Wendigo merge response | Visible to affected human countries |
| `.40` | Ordinary Hannibal terminal bridge | Visible or super-event bridge |
| `.41` | Wendigo-Hannibal terminal bridge | Visible or super-event bridge |
| `.90` | Triggerable-scenario launch adapter | Hidden |

Event `.1` must not assume that its own country scope is the first host. It reads `event_target:cannibalism_first_host` and `event_target:cannibalism_initial_state`, validates both again, initializes persistent state, then dispatches `.2` in the host scope.

### 4.2 Scenario identity

Event 014 is `SCN-010`. IDs 1 through 9 are already occupied. Any Event 014 spec text that calls this scenario 8 is stale and must be aligned before the spreadsheet is treated as authoritative.

Scenario types are fixed.

| Value | Type |
|---:|---|
| 1 | Discipline Collapse |
| 2 | Ritual Cells |
| 3 | Silent Islands |
| 4 | Warlord States |
| 5 | Convergence |

The scenario uses the shared four intensity levels. Manual launch bypasses ordinary event prerequisites but still blocks world end, invalid map targets, missing island candidates for Silent Islands, and insufficient reusable tag slots for Warlord States or Convergence.

Ordinary Convergence also requires `cannibalism_ordinary_unified_host_is_available`. A Wendigo Convergence requires an existing valid dynamic ZZZ Wendigo and does not reserve CBL.

## 5. Script constant schema

All constants below belong in `014_cannibalism_constants.txt` unless marked scenario-only.

### 5.1 Identity and enum categories

| Category | Members |
|---|---|
| `cannibalism_event` | `id = 14`, `evolution_track = 1`, `max_warlord_slots = 8`, `world_end_chaos_threshold = 1000` |
| `cannibalism_phase` | `inactive = 0`, `baseline = 1`, `ritual = 2`, `network = 3`, `convergence = 4`, `unified = 5`, `wendigo_transform = 6`, `terminal = 7`, `defeated = 8` |
| `cannibalism_baseline_stage` | `eligibility = 0`, `evidence = 1`, `predation = 2`, `containment = 3`, `ritual_persistence = 4`, `territorial_fracture = 5`, `warlord = 6`, `unified = 7` |
| `cannibalism_evolution` | `none = 0`, `ritualization = 1`, `organized_network = 2`, `global_reveal = 3` |
| `cannibalism_evolution_tier` | `ritualization = 1`, `organized_network = 2`, `global_reveal = 4` |
| `cannibalism_node_type` | `formation = 1`, `prison = 2`, `port = 3`, `island_commune = 4`, `occupation = 5`, `rail = 6`, `burial = 7`, `feeding_state = 8`, `warlord_capital = 9`, `transformation_anchor = 10` |
| `cannibalism_node_stage` | `dormant = 0`, `suspected = 1`, `active = 2`, `mature = 3`, `territorial = 4`, `recovering = 5`, `cleared = 6` |
| `cannibalism_spread_route` | `retreat = 1`, `prisoner_transfer = 2`, `convoy = 3`, `volunteer_return = 4`, `occupation_turnover = 5`, `deliberate_seed = 6`, `conquest = 7`, `survivor = 8` |
| `cannibalism_spread_status` | `pending = 1`, `resolved = 2`, `cancelled = 3`, `invalid = 4` |
| `cannibalism_consumption_context` | `feeding_state = 1`, `raid = 2`, `prisoner = 3`, `battlefield = 4`, `anchor = 5`, `terminal = 6` |
| `cannibalism_consumption_result` | `invalid_scope = 0`, `blocked = 1`, `duplicate = 2`, `applied = 3`, `exhausted = 4` |
| `state_population_loss_result` | `no_loss = 0`, `applied = 1` |
| `cannibalism_warlord_origin` | `island_host = 1`, `siege_commune = 2`, `march_host = 3` |
| `cannibalism_unification_response` | `pending = 0`, `submit = 1`, `autonomy = 2`, `resist = 3`, `challenge = 4` |
| `cannibalism_scenario_type` | `discipline_collapse = 1`, `ritual_cells = 2`, `silent_islands = 3`, `warlord_states = 4`, `convergence = 5` |

A status enum is used for spread entries instead of a numeric true or false variable. This preserves tombstones for delayed callbacks without violating the repository rule that boolean state uses flags.

### 5.2 Tuning categories

| Category | Required keys | Initial architecture value |
|---|---|---|
| `cannibalism_timing` | `pulse_baseline_days`, `pulse_network_days`, `pulse_convergence_days`, `victory_stabilization_days`, `warlord_slot_quarantine_days`, `evolution_window_center_days` | 14, 10, 7, 90, 45, 90 |
| `cannibalism_consumption` | `first_factor`, `second_factor`, `third_factor`, `fourth_factor`, `floor_factor`, `larder_population_unit`, `severe_fallout_threshold`, `contaminated_yield_factor` | 1.00, 0.60, 0.35, 0.15, 0.05, 10000, 3, 0.25 |
| `cannibalism_host_score` | `war_month_cap`, `war_month_weight`, `casualty_cap`, `casualty_weight`, `convoy_weight`, `low_stability_center`, `low_stability_weight`, `damaged_state_weight`, `minimum_divisions`, `minimum_population_k` | Balance-pass values, never literals in effects |
| `cannibalism_state_score` | `population_cap_k`, `population_weight`, `damaged_building_weight`, `resistance_weight`, `island_weight`, `low_infrastructure_weight` | Balance-pass values, never literals in effects |
| `cannibalism_threshold` | Evolution gates, actor and node reach gates, convergence gates, transformation gates, threat gates, and victory residue limits | Must mirror the accepted Event 014 balance specification |
| `cannibalism_warlord` | Starting force profile, slot quarantine, minimum state, larder inheritance, and generation bounds | Must mirror the accepted Event 014 balance specification |

The host score may use only documented dynamic values until another API is proven. There is no confirmed aggregate division supply ratio or encirclement value. Supply-node pressure is therefore a design dependency, not an assumed trigger.

## 6. Persistent data model

### 6.1 Global flags

- `cannibalism_active`
- `cannibalism_evolution_1_recorded`
- `cannibalism_evolution_2_recorded`
- `cannibalism_evolution_3_recorded`
- `cannibalism_convergence_active`
- `cannibalism_hannibal_revealed`
- `cannibalism_unified`
- `cannibalism_wendigo_merged`
- `cannibalism_global_defeated`
- `cannibalism_scenario_setup_active`
- `world_end_cannibalism`
- `world_end_cannibalism_ordinary`
- `world_end_cannibalism_wendigo`
- `world_threat_source_cannibalism`
- `cannibalism_warlord_slot_1_reserved` through `cannibalism_warlord_slot_8_reserved`

### 6.2 Global scalar variables

- `global.cannibalism_phase`
- `global.cannibalism_evolution_stage`
- `global.cannibalism_network_reach`
- `global.cannibalism_next_actor_generation`
- `global.cannibalism_next_unified_generation`
- `global.cannibalism_next_node_id`
- `global.cannibalism_next_spread_id`
- `global.cannibalism_next_consumption_request_id`
- `global.cannibalism_pulse_sequence`
- `global.cannibalism_actor_count`
- `global.cannibalism_node_count`
- `global.cannibalism_pending_spread_count`
- `global.cannibalism_population_consumed_total`
- `global.cannibalism_convergence_readiness`
- `global.cannibalism_convergence_countdown`
- `global.cannibalism_transformation_progress`
- `global.cannibalism_transformation_countdown`
- `global.cannibalism_prefire_generation`
- `global.cannibalism_prefire_consumed_generation`
- `global.cannibalism_stabilization_start_date`

Counts are caches only. The scope arrays are authoritative. `cannibalism_rebuild_runtime_counts` repairs caches after any lifecycle event.

### 6.3 Global scope and value arrays

- `global.cannibalism_actor_countries`
- `global.cannibalism_node_states`
- `global.cannibalism_convergence_actor_countries`
- `global.cannibalism_transformation_anchor_states`
- `global.cannibalism_spread_queue_id_entries`
- `global.cannibalism_spread_queue_source_country_entries`
- `global.cannibalism_spread_queue_source_state_entries`
- `global.cannibalism_spread_queue_target_country_entries`
- `global.cannibalism_spread_queue_target_state_entries`
- `global.cannibalism_spread_queue_route_entries`
- `global.cannibalism_spread_queue_source_generation_entries`
- `global.cannibalism_spread_queue_due_date_entries`
- `global.cannibalism_spread_queue_status_entries`
- `global.cannibalism_warlord_slot_generation_entries`
- `global.cannibalism_warlord_slot_reuse_date_entries`
- `global.cannibalism_warlord_slot_1_core_states` through `global.cannibalism_warlord_slot_8_core_states`
- `global.cannibalism_unified_core_states`

Every spread array uses the same index. Resolved, cancelled, and invalid entries remain as tombstones until `cannibalism_compact_spread_queue` runs outside queue iteration.

Each slot-specific core-state array belongs to the slot generation stored at the same slot index in `global.cannibalism_warlord_slot_generation_entries`. Allocation requires the array to be empty. Cleanup removes only cores in that array, clears it after successful removal, then begins quarantine.

### 6.4 Country variables

- `cannibalism_stage`
- `cannibalism_field_hunger`
- `cannibalism_command_integrity`
- `cannibalism_cult_cohesion`
- `cannibalism_larder_stores`
- `cannibalism_frenzy`
- `cannibalism_network_alignment`
- `cannibalism_actor_generation`
- `cannibalism_origin_country`
- `cannibalism_origin_state`
- `cannibalism_origin_type`
- `cannibalism_policy_route`
- `cannibalism_last_processed_pulse_sequence`
- `cannibalism_warlord_slot_id`
- `cannibalism_warlord_slot_generation`
- `cannibalism_warlord_setup_generation`
- `cannibalism_warlord_cleanup_generation`
- `cannibalism_unified_generation`
- `cannibalism_unification_response`

Country scope pointers use scope-valued variables only where the engine and existing repository pattern support them. Otherwise the pointer belongs in an array or event target. Numeric country tags must not be encoded as ordinary balance variables.

### 6.5 Country flags

- `cannibalism_active_country`
- `cannibalism_locally_defeated`
- `cannibalism_exploitation_policy`
- `cannibalism_warlord_country`
- `cannibalism_unified_country`
- `cannibalism_wendigo_hannibal_country`
- `cannibalism_pulse_anchor`
- `cannibalism_convergence_host`
- `cannibalism_terminal_route_complete`

### 6.6 State variables

- `cannibalism_node_id`
- `cannibalism_node_generation`
- `cannibalism_node_type`
- `cannibalism_node_stage`
- `cannibalism_node_strength`
- `cannibalism_node_route`
- `cannibalism_node_source_country`
- `cannibalism_node_source_country_generation`
- `cannibalism_node_source_state`
- `cannibalism_registered_controller`
- `cannibalism_population_consumed_total`
- `cannibalism_consumption_ticks`
- `cannibalism_last_consumption_date`
- `cannibalism_last_consumption_request_id`
- `cannibalism_recovery_stage`
- `cannibalism_last_processed_pulse_sequence`

### 6.7 State flags

- `cannibalism_active_node`
- `cannibalism_feeding_state`
- `cannibalism_exhausted_state`
- `cannibalism_recovery_active`
- `cannibalism_transformation_anchor`

### 6.8 Event targets

| Target | Lifetime | Purpose |
|---|---|---|
| `cannibalism_first_host` | Regular chain | Selected opening host |
| `cannibalism_initial_state` | Regular chain | Selected opening incident state |
| `cannibalism_consumption_actor` | Regular chain | Actor credited for one consumption transaction |
| `cannibalism_spread_source_country` | Regular chain | Normalized source for one enqueue or resolve operation |
| `cannibalism_spread_source_state` | Regular chain | Normalized source state |
| `cannibalism_spread_target_country` | Regular chain | Normalized target country |
| `cannibalism_spread_target_state` | Regular chain | Normalized target state |
| `cannibalism_unification_source` | Regular chain | Warlord that supplies the ordinary route's inherited player and gameplay state |
| `cannibalism_unification_host` | Regular chain | Fixed CBL for the ordinary route or dynamic ZZZ for the Wendigo route |
| `cannibalism_player_transfer_source` | Regular chain | Human source country that explicitly accepted transfer |
| `cannibalism_wendigo_host` | Regular chain | Existing dynamic ZZZ Wendigo that remains host |
| `cannibalism_wendigo_merge_source` | Regular chain | Event 014 actor whose runtime and player-safe integration feed the ZZZ host |
| `cannibalism_pulse_anchor` | Global | Country that owns the recurring delayed pulse |

Every use of a regular or global event target must be guarded by `has_event_target` and by `exists` in the target scope.

## 7. Trigger API

All event-owned triggers below belong in `014_cannibalism_triggers.txt`.

| Identifier | Scope | Inputs | Result and contract |
|---|---|---|---|
| `cannibalism_automatic_event_is_available` | Event selection country or global selection scope | None | True only when Event 014 is not active or durably defeated, world end is absent, at least one valid host and incident state exist, and a fire-once launch remains legal |
| `cannibalism_country_is_valid_first_host` | Country | None | Requires an existing ordinary country at war, normal civilian systems, no special-chaos classification, divisions above the constant minimum, and at least one meaningful controlled or owned populated state |
| `cannibalism_state_is_valid_initial_incident` | State | Optional regular target `cannibalism_candidate_host` | Requires meaningful population, a valid controller or owner relationship to the candidate host, and no terminal contamination or incompatible special-state state |
| `cannibalism_country_scope_is_live_actor` | Country | Expected generation temp variable | Requires existence, active flag, array membership, and exact generation match |
| `cannibalism_state_scope_is_live_node` | State | Expected node ID and generation temp variables | Requires existence, active-node flag, array membership, and exact identity match |
| `cannibalism_scope_generation_matches` | Country | Expected generation temp variable | Rejects stale warlord or actor callbacks |
| `cannibalism_spread_context_is_valid` | Any normalized caller | Four spread event targets, route, and source generation | Requires live source and target scopes, legal route, and no terminal or duplicate target state |
| `cannibalism_state_is_usable_consumption_target` | State | Optional actor target and consumption context | Blocks Death and zombie consumed territory, severe fallout, zero population, exhausted states, and invalid actor ownership or control context |
| `cannibalism_can_begin_evolution_1` | Global or pulse anchor | None | Applies setting gate, chaos-tier gate, stage gate, timing gate, and live-host gate |
| `cannibalism_can_begin_evolution_2` | Global or pulse anchor | None | Applies setting gate, chaos-tier gate, network reach, actor or node maturity, and prior-stage gate |
| `cannibalism_can_begin_evolution_3` | Global or pulse anchor | None | Applies setting gate, chaos-tier gate, global reveal conditions, and prior-stage gate |
| `cannibalism_warlord_slot_is_reusable` | Global selection scope | Slot ID and current date | Requires unreserved slot, no live country with the slot and generation, no pending queue reference, no event target reference owned by Event 014, and reuse date reached |
| `cannibalism_ordinary_unified_host_is_available` | Global selection scope | None | Requires fixed tag CBL to be absent or already reserved for the same prepared Event 014 unified generation. It blocks an unrelated live CBL country |
| `cannibalism_has_valid_pulse_anchor` | Global or any country | None | Requires global target, target existence, matching country flag, and active Event 014 state |
| `cannibalism_has_global_residue` | Global or pulse anchor | None | True for any live actor, node, pending spread, commune, island, warlord, unified actor, convergence state, transformation state, or scheduled callback |
| `cannibalism_ordinary_world_end_is_ready` | Unified country | None | Requires ordinary Hannibal route, chaos threshold, terminal readiness, no merged Wendigo identity, and no other world end |
| `cannibalism_wendigo_world_end_is_ready` | Wendigo-Hannibal country | None | Requires merged identity, completed transformation, chaos threshold, terminal readiness, and no other world end |

`cannibalism_state_is_usable_consumption_target` remains event-owned. Its contamination and yield rules are specific to Event 014 and should not be promoted to a misleading general shared trigger.

## 8. Initialization and pre-fire effect API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_initialize_system` | Country that runs `.1` | Valid first-host and initial-state event targets, pre-fire generation | Global flag and phase, empty canonical arrays, counters, slot registry, pulse anchor | Idempotent for one pre-fire generation. It must not clear a live Event 014 runtime |
| `cannibalism_initialize_warlord_slot_registry` | Any stable country | None | Eight generation and reuse-date array entries | Creates missing entries only. It never resets live slot generations |
| `cannibalism_score_first_host_candidate` | Candidate country | None | Temp `cannibalism_candidate_score` | Uses only documented values and script constants. It performs no mutation |
| `cannibalism_score_initial_state_candidate` | Candidate state | Target `cannibalism_candidate_host` | Temp `cannibalism_candidate_score` | Uses population, damage, resistance, infrastructure, island exposure, and host relation. It performs no mutation |
| `cannibalism_select_first_host` | Event-system dispatch country | None | Regular targets `cannibalism_first_host` and `cannibalism_initial_state`, temp `cannibalism_prefire_ready` | Builds deterministic candidate arrays, finds the first highest score, validates both winning scopes again, and writes no persistent Event 014 state |
| `cannibalism_prepare_random_event_fire` | Event-system dispatch country | Event ID already set to 14 | Temp `cannibalism_prefire_ready`, generic `event_single_fire_allowed` | Calls selection. Sets generic fire permission to 0 unless both targets remain valid. Increments pre-fire generation only after success |
| `cannibalism_begin_from_prefire_context` | Event `.1` country | Both regular targets and unconsumed pre-fire generation | Registered host and initial node, visible response dispatch, scheduled pulse | Consumes the generation exactly once and rejects missing or stale targets without partial initialization |
| `cannibalism_apply_prefire_opening` | First host | Initial state, scenario override values when present | Opening stage, hunger, integrity, cohesion, larder, node type, and initial event effects | Central opening transaction shared by automatic and manual launch paths |

### 8.1 Deterministic host selection

`cannibalism_select_first_host` uses two pairs of temporary arrays.

- `temp_cannibalism_host_candidates`
- `temp_cannibalism_host_scores`
- `temp_cannibalism_state_candidates`
- `temp_cannibalism_state_scores`

Every country that passes `cannibalism_country_is_valid_first_host` is appended in deterministic country iteration order. The effect calls `cannibalism_score_first_host_candidate`, clamps the result to a nonnegative score, rounds once, and appends the aligned score. `find_highest_in_array` selects the index. If scores tie, the first maximum in the existing country order wins.

The selected host repeats the same process for eligible states. A state must be owned or controlled by the host according to the accepted opening design. The winning state is validated a second time before its event target is saved.

The host score can safely use these documented terms.

- Capped `longest_war_length`
- Capped `casualties_k`
- `convoy_threat`
- Pressure below a constant stability center
- Count of damaged controlled populated states
- Division count as a hard minimum
- Supply-node count as a descriptive term only if the proxy model is approved

The state score can safely use these documented terms.

- Capped `state_population_k`
- `has_damaged_buildings`
- Pressure from low `infrastructure_level`
- `resistance` when relevant to the host relation
- `is_island_state` weighted by host convoy exposure

No score may claim to measure exact division supply or encirclement until a documented or validated direct API is found. The implementation must stop for the design choice described in the blockers section if those concepts are mandatory.

## 9. Registration and canonical ledger API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_register_actor` | Country | Actor origin data and requested stage | Assigned `cannibalism_actor_generation`, active flag, one actor-array entry | Rejects invalid or already live scopes. A second call for the same live generation is a no-op |
| `cannibalism_unregister_actor` | Country | Expected generation and cleanup reason | Active flag cleared, actor entry invalidated or removed, local defeat state when appropriate | Rejects generation mismatch. It does not trigger global cleanup by itself |
| `cannibalism_register_current_state_node` | State | Node type, route, source targets, source generation, opening strength | New node ID and generation, active flag, one node-array entry | Reuses an existing live node only through an explicit update path. It never silently overwrites one |
| `cannibalism_retire_current_state_node` | State | Expected node ID and generation, recovery mode | Node cleared or moved to recovery, array entry invalidated | Duplicate retirement is a no-op |
| `cannibalism_compact_actor_registry` | Pulse anchor | None | New actor scope array without invalid entries | Runs only after actor iteration |
| `cannibalism_compact_node_registry` | Pulse anchor | None | New node scope array without invalid entries | Runs only after node iteration |
| `cannibalism_rebuild_runtime_counts` | Pulse anchor | None | Actor, node, pending-spread, convergence-actor, and anchor counts | Derives caches from validated arrays. It never trusts old counts |
| `cannibalism_reconcile_runtime_state` | Pulse anchor | Current pulse sequence | Repaired arrays, controllers, generations, counts, and threat source | Central post-on-action and post-pulse integrity pass |

Actor and node registries are the source of truth. Country and state flags are fast local guards. Cached counts are never sufficient proof that a scope remains valid.

## 10. Pulse ownership and narrow on-actions

### 10.1 Scheduling API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_select_pulse_anchor` | Current live actor or stable event-system country | Preferred actor when valid | Global target and one matching country flag | Clears the old anchor flag only after the replacement is valid |
| `cannibalism_schedule_next_pulse` | Pulse anchor | Current phase | One delayed `chaosx.nr14.10` | Copies the phase-specific delay constant into a temp variable before using it as the delay |
| `cannibalism_run_pulse` | Pulse anchor | None | Incremented global pulse sequence and one complete ordered update | Rejects a missing anchor, inactive system, or a sequence already processed by this anchor |
| `cannibalism_process_actor_pulse` | Actor country | Current sequence and expected generation | Hunger, integrity, cohesion, larder, route, AI, and readiness updates | Each actor stores `cannibalism_last_processed_pulse_sequence` before mutations begin |
| `cannibalism_process_node_pulse` | Node state | Current sequence, expected ID and generation | Strength, stage, recovery, spread readiness, and consumption readiness updates | Each state stores its processed sequence before mutations begin |
| `cannibalism_process_spread_queue` | Pulse anchor | Current date and sequence | Due entries resolved or cancelled | Processes only pending entries whose due date is reached |

The order inside `cannibalism_run_pulse` is fixed.

1. Validate or replace the pulse anchor.
2. Increment `global.cannibalism_pulse_sequence`.
3. Reconcile live actor and node scopes.
4. Process each actor once.
5. Process each node once.
6. Resolve due spread entries.
7. Rebuild counts and network reach.
8. Evaluate enabled evolutions in numeric order.
9. Evaluate convergence, transformation, local victory, global victory, and terminal routes.
10. Refresh the Event 014 world-threat source.
11. Compact registries and queue when no iterator is active.
12. Schedule exactly one next pulse when Event 014 remains active.

### 10.2 On-action adapters

Create `common/on_actions/014_cannibalism_on_actions.txt`. Use only these narrow hooks when their documented scopes provide relevant lifecycle information.

- `on_state_control_changed`
- `on_war_relation_added`
- `on_capitulation`
- `on_annex`
- `on_puppet`
- `on_release_as_free`
- `on_release_as_puppet`
- `on_subject_free`
- `on_subject_annexed`
- `on_civil_war_end_before_annexation`
- `on_civil_war_end`
- `on_peaceconference_ended`
- `on_government_change` only if a route predicate needs it

Every adapter first exits unless `cannibalism_active` is set or one documented callback scope has an Event 014 country or state flag. The adapter normalizes the documented callback scopes into regular event targets, then calls one event-owned handler.

| Handler | Primary scope | Normalized inputs | Responsibility |
|---|---|---|---|
| `cannibalism_handle_state_control_changed` | Changed state | Old controller target, new controller target | Update registered controller, feeding control, spread context, and local victory eligibility |
| `cannibalism_handle_war_relation_added` | One belligerent | Opponent target | Refresh eligible military context and wake the pulse if a live actor is involved |
| `cannibalism_handle_capitulation` | Capitulating country | Victor target when documented | Preserve or retire actor state, transfer relevant nodes, and start tag cleanup when appropriate |
| `cannibalism_handle_annex` | Annexed country or annexer according to callback adapter | Annexed and annexer targets | Reassign pulse anchor before old scope cleanup, invalidate stale generation references, and reconcile nodes |
| `cannibalism_handle_country_lifecycle_change` | Released, puppeted, freed, or annexed country | Prior controller or overlord targets when documented | Revalidate actor class, nodes, tag slots, and response state |
| `cannibalism_handle_civil_war_end` | Winning country | Losing country target | Reconcile actor identity, nodes, troops, and tag-slot lifecycle |

The on-actions do not run the full recurring system. They make the minimum safe mutation, set reconciliation state, and ensure one pulse remains scheduled.

## 11. Spread queue API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_prepare_spread_context` | Source actor or state | Source, target, route, delay | Four normalized event targets, source generation, due date | Performs no persistent mutation |
| `cannibalism_enqueue_spread` | Pulse anchor or source actor | Valid normalized context | New spread ID and aligned pending queue row | Duplicate source-generation, target-state, route, and due-window entries are rejected |
| `cannibalism_resolve_spread_entry` | Pulse anchor | Queue index and expected spread ID | Applied node or actor change, status `resolved` | Revalidates every scope and generation immediately before mutation |
| `cannibalism_cancel_spread_entry` | Pulse anchor | Queue index, expected spread ID, cancellation reason | Status `cancelled` or `invalid` | Idempotent and safe for missing scopes |
| `cannibalism_apply_spread_to_target` | Target state | Valid source and target context | New node, strengthened node, or blocked result | Never applies a second mutation for the same spread ID |
| `cannibalism_compact_spread_queue` | Pulse anchor | None | Rebuilt aligned arrays containing pending rows only | Runs outside queue iteration and asserts equal array sizes before replacement |

A delayed spread entry is valid only if its numeric ID, source generation, source scope, target scope, route, and status all still match. Annexation, tag reuse, state transfer, or source defeat can therefore invalidate one row without corrupting later rows.

## 12. Exact civilian population-loss API

### 12.1 Shared dynamic helper

Use and preserve `apply_exact_state_civilian_population_loss` in `common/scripted_effects/chaosx_dynamic_effects.txt` and `common/scripted_effects/chaosx_dynamic_effects.md`.

Scope: state

Required input:

- Temp variable `state_civilian_population_loss_requested`

Optional inputs:

- Temp variable `state_civilian_population_loss_reason`, default shared unknown reason
- Temp variable `state_civilian_population_loss_target_country`, default current state owner
- Temp variable `state_civilian_population_loss_has_target_country`, default 1 when the state owner is used
- Temp variable `state_civilian_population_loss_minimum_remaining`, default 0
- Temp variable `state_civilian_population_loss_log_deaths`, default 1

Outputs:

- Temp variable `state_civilian_population_loss_applied`
- Temp variable `state_civilian_population_loss_result`

Required behavior:

1. Initialize the applied output and result to 0.
2. Confirm state scope and a positive request.
3. Read current civilian population from `state_population_k`, multiply by 1000, and round once.
4. Subtract the configured minimum remaining population from the current population.
5. Clamp the requested loss to that available amount.
6. When the applied loss is positive and Deaths is enabled with logging requested, call `chaos_meter_register_deaths` exactly once with `chaos_deaths_is_civilian = 1` and `chaos_deaths_apply_state_pop = 1`.
7. When Deaths is disabled or logging is disabled, copy the applied loss to a temp variable, multiply that temp by negative 1, and pass it to `add_manpower` in the current state.
8. Return the real applied amount and result 1. Every invalid, empty, or zero-loss path returns result 0.

The helper never updates larder, hunger, Event 014 totals, node strength, or route state. Those belong to the caller.

The old `modify_state_population_by_percent` helper remains untouched until a separate migration is authorized. Event 014 must not call it.

### 12.2 Event-owned consumption transaction

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_prepare_consumption_context` | Actor country | Target state, context, base percent, hard cap, larder factor | Monotonic request ID and normalized actor target | Increments `global.cannibalism_next_consumption_request_id` once |
| `cannibalism_consume_current_state` | State | Actor target, request ID, context, optional base percent, hard cap, larder factor | Result, real population loss, larder gained | State checks its last request ID before any mutation and records the ID only when applying |

Required temp inputs for `cannibalism_consume_current_state`:

- `cannibalism_consumption_request_id`
- `cannibalism_consumption_context`
- `cannibalism_consumption_base_percent`
- `cannibalism_consumption_hard_cap`
- `cannibalism_consumption_larder_factor`

Required temp outputs:

- `cannibalism_consumption_result`
- `cannibalism_population_loss_applied`
- `cannibalism_larder_gained`

The state applies a diminishing factor based on completed consumption ticks.

| Prior completed ticks | Factor |
|---:|---:|
| 0 | 1.00 |
| 1 | 0.60 |
| 2 | 0.35 |
| 3 | 0.15 |
| 4 or more | 0.05 |

Death-consumed territory and zombie-consumed territory yield zero. Severe fallout yields zero. Other tracked contamination yields the configured 0.25 factor unless the accepted balance specification chooses another explicit value.

Larder gain and `global.cannibalism_population_consumed_total` are calculated from `state_civilian_population_loss_applied`, never from the requested loss. They update once even when Deaths is disabled.

### 12.3 Deaths reason integration

Reserve `cannibalism_consumption = 15` for the Deaths cause and wire every reason surface. Do not allocate a second Event 014 cause ID.

- Country cause initialization and reset
- Cause aggregation
- Temporary unsorted cause arrays
- Global view arrays and resizing
- Tooltip cause lines
- Selected-cause and detail-reason scripted localisation
- GUI localisation
- Cause-specific chaos weighting through `cannibalism_consumption_chaos_weight`

The centralized initial chaos weight is 0.20. A balance audit may change that constant without changing callers.

Population loss cannot depend on the Deaths setting. Only Deaths ledger and cause presentation may depend on that setting.

## 13. Evolution API and event-log integration

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_try_begin_evolution_1` | Pulse anchor | None | Evolution I or no-op | Calls the matching trigger and setting gate. Applies no disabled content |
| `cannibalism_try_begin_evolution_2` | Pulse anchor | None | Evolution II or no-op | Requires Evolution I and an eligible network state |
| `cannibalism_try_begin_evolution_3` | Pulse anchor | None | Evolution III or no-op | Requires Evolution II and global reveal readiness |
| `cannibalism_apply_evolution_1_to_current_actor` | Actor country | Expected generation | Ritualization actor state | Idempotent by global stage and actor stage |
| `cannibalism_apply_evolution_2_to_current_actor` | Actor country | Expected generation | Organized-network actor state | Idempotent by global stage and actor stage |
| `cannibalism_apply_evolution_3_to_current_actor` | Actor country | Expected generation | Global-reveal actor state | Idempotent by global stage and actor stage |
| `cannibalism_prepare_prefire_evolution` | Event `.1` country | Event settings and chaos tier | Highest enabled pre-fire evolution | Does not create flags or log rows for disabled stages |
| `cannibalism_record_evolution_stage` | Actor country or pulse anchor with actor target | Stage number and actor | One event-log evolution row | Runs only after the state transition succeeds and the matching recorded flag is absent |

The event log uses one sequential evolution track.

| Evolution | Type | Stage | Tier |
|---|---:|---:|---:|
| Ritualization | 1 | 1 | 1 |
| Organized Network | 1 | 2 | 2 |
| Global Reveal | 1 | 3 | 4 |

`cannibalism_record_evolution_stage` sets these event-log inputs before calling `record_events_log_evolution_entry`.

- `events_log_evolution_event_id = 14`
- `events_log_evolution_type = 1`
- `events_log_evolution_stage = 1`, `2`, or `3`
- `events_log_evolution_tier = 1`, `2`, or `4`
- Regular target `events_log_evolution_actor`
- `events_log_evolution_has_actor = 1` when the actor exists

The helper sets `cannibalism_evolution_1_recorded`, `cannibalism_evolution_2_recorded`, or `cannibalism_evolution_3_recorded` only after the shared log call returns in the same effect chain.

## 14. Fixed warlord tag-slot architecture

### 14.1 Reserved tags

Reserve these eight currently free tags.

| Slot | Tag | Reservation flag | Scripted-localisation result |
|---:|---|---|---|
| 1 | `CBA` | `cannibalism_warlord_slot_1_reserved` | `CBA` |
| 2 | `AHX` | `cannibalism_warlord_slot_2_reserved` | `AHX` |
| 3 | `CBC` | `cannibalism_warlord_slot_3_reserved` | `CBC` |
| 4 | `AIX` | `cannibalism_warlord_slot_4_reserved` | `AIX` |
| 5 | `CBE` | `cannibalism_warlord_slot_5_reserved` | `CBE` |
| 6 | `CBF` | `cannibalism_warlord_slot_6_reserved` | `CBF` |
| 7 | `AMX` | `cannibalism_warlord_slot_7_reserved` | `AMX` |
| 8 | `CBH` | `cannibalism_warlord_slot_8_reserved` | `CBH` |

The scripted localisation key is `GetCannibalismWarlordSlotTag`. A meta effect injects the selected tag into static tag fields such as `add_core_of`, `release`, and tag scope blocks.

The eight warlord tags are origin-agnostic reusable country slots. `CBA` through `CBH` may each receive an Island Host, Siege Commune, or March Host package according to the selected state's geography and the current generation. Their regional identity comes from scripted localisation, character setup, ideas, origin variables, and one distinct flat flag family per reusable slot. No additional warlord cosmetic tags are required.

`CBL` is not a reusable slot. It is the dedicated ordinary unified host. After Hannibal's reveal, its hierarchy focus applies exactly one of `CBL_CENTRAL_COMMAND`, `CBL_HOST_CONFEDERATION`, or `CBL_RITUAL_STATE`; the base `CBL` identity remains visible before that post-reveal choice. The ordinary route transfers the selected source country's player and inherited state into CBL before annexation. The Wendigo route does not use CBL as its host. It keeps dynamic `ZZZ` and applies `ZZZ_CANNIBALISM_HANNIBAL` only during the public merge.

CBL preparation adds only the selected unified core-state set, records those states in `global.cannibalism_unified_core_states`, releases CBL, increments `global.cannibalism_next_unified_generation`, and stores the generation on CBL. Failed preparation removes only cores added by that preparation generation.

### 14.2 Slot allocation and cleanup API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_find_free_warlord_slot` | Pulse anchor or scenario launcher | Current date and requested origin | Temp slot ID and reusable result | Checks slots 1 through 8 in fixed order with `cannibalism_warlord_slot_is_reusable` |
| `cannibalism_allocate_warlord_slot` | Pulse anchor | Valid slot ID, origin state, origin type | Reserved flag, incremented generation, target tag context | Reserves before any country or core mutation. Rolls back only through explicit failed-allocation cleanup |
| `cannibalism_initialize_warlord_country` | Newly released tag | Slot ID, generation, origin state, source actor | Country flag, identity variables, route state, ideas, AI, and actor registration | Rejects an already initialized equal generation as a no-op |
| `cannibalism_prepare_warlord_starting_forces` | Warlord country | Origin, intensity, inherited larder, and balance profile | Temp equipment, unit, manpower, and template values | Computes values only |
| `cannibalism_spawn_warlord_starting_forces` | Warlord country | Prepared temp values | Units, stockpile, manpower, and template state | Guarded by slot generation and a one-incarnation setup marker |
| `cannibalism_begin_warlord_slot_cleanup` | Defeated or absorbed warlord | Slot ID and generation | Country cleanup, tracked-core cleanup, reuse date, reservation retained during quarantine | Invalidates callbacks before removing country-owned state |
| `cannibalism_try_release_warlord_slot` | Pulse anchor | Slot ID | Reservation cleared when safe | Requires quarantine complete and zero live references to the old generation |

Each tag country stores `cannibalism_warlord_slot_id` and `cannibalism_warlord_slot_generation`. The global arrays store the latest generation and earliest safe reuse date for each slot.

Every slot also owns an event-specific array of the states to which that generation added cores. Cleanup removes only those tracked cores. It must not iterate over every state and strip every core of the tag.

A slot stays quarantined until all of these are true.

- The tag has no live Event 014 actor generation
- No node records the generation as its source
- No pending spread row records the generation
- No convergence or transformation array records the generation
- No Event 014 delayed callback can still refer to the generation
- The configured reuse date has passed

This quarantine is required even if the country was annexed immediately. It prevents an old delayed event from applying to a later country that inherited the same fixed tag.

## 15. Convergence, player transfer, and Hannibal API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_calculate_convergence_readiness` | Pulse anchor | Valid actor registry | Readiness value and rebuilt convergence actor array | Uses reconciled live actors only |
| `cannibalism_try_start_convergence` | Pulse anchor | Readiness and evolution state | Convergence flag, countdown, frozen participant generations | Starts once |
| `cannibalism_cancel_convergence` | Pulse anchor | Failure reason | Convergence state cleared, participants released | Does not erase valid actors or nodes |
| `cannibalism_select_unification_host` | Pulse anchor | Frozen participant list and Wendigo participation | Targets `cannibalism_unification_source` and `cannibalism_unification_host` | Deterministically scores the inheritance source. Sets the host to fixed CBL for ordinary Hannibal or dynamic ZZZ for the Wendigo route |
| `cannibalism_prepare_ordinary_unified_host` | Selected inheritance source | Source generation and selected core-state set | Tracked CBL cores, released CBL scope, new unified generation, and target `cannibalism_unification_host` | Calls the availability trigger before any core mutation. Refuses to overwrite a live unrelated CBL scope or stale Event 014 incarnation |
| `cannibalism_dispatch_warlord_response` | Participant warlord | Host target and expected generations | Human event or AI response enum | Does not annex or transfer by itself |
| `cannibalism_integrate_submitted_warlord` | Unification host | Submitting warlord target and expected generations | Annexation with troop transfer, node transfer, larder transfer, cleanup | Runs only for explicit submit or accepted AI response |
| `cannibalism_transfer_player_to_unification_host` | Unification host | Target `cannibalism_player_transfer_source` | Player controls the host | Host calls `change_tag_from` before source annexation |
| `cannibalism_reveal_hannibal` | Selected host | Route and identity context | Hannibal flag, character, cosmetic, ideas, event, and log state | Runs once after valid convergence resolution |
| `cannibalism_complete_unification` | Selected host | Resolved participant responses | Unified flag, actor consolidation, inherited nodes, threat refresh | Does not force unresolved human participants into the host |

Player precedence is fixed.

1. In the ordinary route, deterministic scoring selects one inheritance source and the fixed host is CBL.
2. If the selected ordinary source is player-controlled and accepts unification, CBL calls `change_tag_from` on that source before the source is annexed.
3. In the Wendigo route, dynamic ZZZ remains the host. A player-controlled Wendigo therefore remains the controlling player after consolidation.
4. A non-host human warlord is never silently absorbed.
5. A human participant receives resist, autonomy, or explicit transfer choices.
6. Only a human participant that explicitly accepts transfer can call `cannibalism_transfer_player_to_unification_host`.
7. Multiple human warlords cannot all transfer to the same host. After CBL or ZZZ becomes player-controlled, later human participants must remain autonomous or resist unless an explicit multiplayer design says otherwise.

The annex operation that follows accepted integration must use troop transfer. Nodes and Event 014 values transfer through explicit helper logic rather than relying on annex side effects.

## 16. Wendigo crossover ownership

The existing Wendigo identity uses original dynamic tag `ZZZ`, cosmetic `ZZZ_weaponized_wendigo`, idea `weaponized_zombie_wendigo`, flags `weaponized_zombie_outbreak_country` and `weaponized_zombie_type_wendigo`, archetype `weaponized_zombie_archetype_wendigo`, template `Wendigo Pack`, subunit `wendigo_zombies`, OOB `ZZZ_weaponized_1936`, and helper `weaponized_zombie_unlock_profiled_template`.

### 16.1 Shared zombie boundary

Do not copy the Wendigo package onto CBL or another fixed tag. Dynamic `ZZZ` remains the host for the merged route and already owns the Wendigo profile.

After Event 014 state is integrated into ZZZ, call the existing `weaponized_zombie_unlock_profiled_template` helper in ZZZ scope to reassert its profiled template access. Preserve these existing ZZZ values and identities.

- Wendigo archetype and profiled runtime variables
- Wendigo flags read by downstream zombie logic
- Wendigo idea state
- Wendigo template, subunit access, OOB inheritance, and surviving units

The crossover must not set an Event 002 world-end flag or fire the old Wendigo super event. A new cross-country Wendigo package-copy helper is unnecessary under the frozen ZZZ-host design.

### 16.2 Event-owned merge API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_select_wendigo_merge_country` | Pulse anchor | Valid Wendigo and Event 014 actors | Targets `cannibalism_wendigo_host` and `cannibalism_wendigo_merge_source` | Selects existing dynamic ZZZ as host and a deterministic Event 014 inheritance source |
| `cannibalism_copy_actor_runtime_to_wendigo_host` | Event 014 source | Target `cannibalism_wendigo_host` and both generations | Event 014 larder, route, node, convergence, achievement, and Hannibal state prepared on ZZZ | Does not overwrite the Wendigo profile or cosmetic until the merged cosmetic transition |
| `cannibalism_execute_wendigo_merge` | Dynamic ZZZ Wendigo host | Event 014 source and expected generations | Merged actor, transformation anchors, player-safe source integration, merged cosmetic | Keeps ZZZ as host and performs one atomic route transition |
| `cannibalism_try_start_wendigo_world_end` | Merged country | Readiness trigger | Event 014 terminal route | Cannot call Event 002 terminal event |

The merged ZZZ country sets `cannibalism_wendigo_hannibal_country` and later sets compatibility flag `world_end_wendigo` together with `world_end_cannibalism_wendigo`. It fires Event 014's unique super event.

Add this hard exclusion to `chaosx.nr2.11` eligibility.

```txt
NOT = { has_country_flag = cannibalism_wendigo_hannibal_country }
```

Without this guard, the old Wendigo event can bypass Event 014's transformation countdown because the merged actor intentionally retains Wendigo compatibility flags.

The merged cosmetic identifier is `ZZZ_CANNIBALISM_HANNIBAL`. It requires complete flag and portrait assets before the route can be called complete.

## 17. Cleanup, victory, and threat API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `cannibalism_cleanup_country_runtime` | Country | Expected generation and cleanup mode | Actor state removed or transferred, owned callbacks invalidated | Generation mismatch is a no-op |
| `cannibalism_cleanup_global_runtime` | Pulse anchor | Victory or terminal cleanup mode | Scheduler, targets, arrays, transient flags, queues, and Event 014 threat source cleared | Does not erase durable history, event-log rows, achievement flags, or selected world-end identity |
| `cannibalism_try_local_victory` | Relevant country | Stabilization state | Local defeated flag and local cleanup | Never clears global Event 014 state |
| `cannibalism_try_global_victory` | Pulse anchor | Stabilization start and zero-residue proof | Global defeated flag and global cleanup | Requires the full stabilization interval and no global residue |
| `cannibalism_refresh_world_threat_source` | Pulse anchor | Reconciled actors and nodes | Event 014 source flag plus shared aggregate refresh | Sets or clears only the Event 014 source, then calls `refresh_world_threat_state` |
| `cannibalism_try_start_ordinary_world_end` | Unified country | Readiness trigger | Ordinary terminal flag, world-end state, unique super event | Sets `world_end_cannibalism_ordinary` |
| `cannibalism_try_start_wendigo_world_end` | Merged country | Readiness trigger | Merged terminal flags, world-end state, unique super event | Sets `world_end_cannibalism_wendigo` and compatibility `world_end_wendigo` |

`cannibalism_has_global_residue` must inspect validated arrays and direct persistent flags. It cannot rely only on cached counts. Residue includes live actors, live nodes, pending spread rows, island communes, feeding states, warlords, a unified country, convergence state, transformation state, and scheduled generation-valid callbacks.

Local victory removes one country's Event 014 runtime after its own stabilization conditions. It does not clear other countries, islands, communes, nodes, or spread entries.

Global victory starts its stabilization clock only after the first zero-residue reconciliation. Any later residue clears that clock. Once the full interval passes with zero residue, it clears the pulse anchor and sets `cannibalism_global_defeated`.

Manual scenario launch can explicitly bypass `cannibalism_global_defeated`. Ordinary random selection cannot.

### 17.1 Threat source threshold

`cannibalism_refresh_world_threat_source` sets `world_threat_source_cannibalism` when any one of these conditions is true.

- At least two viable warlord actors exist
- A unified Event 014 actor exists
- A merged Wendigo-Hannibal actor exists
- The accepted mature-network actor, node, and reach thresholds are met

It clears the source only after none of those conditions remain. It then calls the shared `refresh_world_threat_state` helper. The shared helper must include `world_threat_source_cannibalism` alongside the existing zombie, holy realm, Mengele, Fury, and Death sources.

## 18. Triggerable scenario API

| Identifier | Scope | Inputs | Outputs | Contract |
|---|---|---|---|---|
| `trigger_cannibalism_scenario` | Scenario launcher country | Scenario type, shared intensity, selected target context | One validated Event 014 scenario | Central wrapper for scenario 10 |
| `cannibalism_scenario_prepare_scale` | Scenario launcher | Shared intensity | Temp scale variables used by setup | No persistent mutation |
| `cannibalism_scenario_setup_discipline_collapse` | Selected target country | Scale and selected state | Baseline opening | Uses the same opening transaction as automatic fire |
| `cannibalism_scenario_setup_ritual_cells` | Selected target country | Scale and valid states | Multiple early ritual nodes | Registers every node through canonical APIs |
| `cannibalism_scenario_setup_silent_islands` | Scenario launcher | Scale and island candidates | Island communes and spread context | Blocks launch when no valid island exists |
| `cannibalism_scenario_setup_warlord_states` | Scenario launcher | Scale, state candidates, and free slots | Multiple live warlords | Allocates every slot before country release begins |
| `cannibalism_scenario_setup_convergence` | Scenario launcher | Scale, actor candidates, free slots, and route-host availability | Warlords plus near-ready convergence | Still respects player-transfer safety, fixed CBL ownership for ordinary convergence, and dynamic ZZZ ownership for Wendigo convergence |
| `cannibalism_scenario_cleanup_context` | Scenario launcher | Setup result | Scenario flag and temp targets cleared | Failed setup rolls back only resources allocated by that setup generation |

Scenario integration requires these exact registry changes.

- `triggerable_scenario_id.cannibalism = 10`
- `triggerable_scenario_cannibalism_type` enum values 1 through 5
- A stable scenario sort value
- Settings initialization variable `triggerable_scenarios_cannibalism_type`
- Registry entry and all four explicit sort branches
- Type cycling and selector localisation
- Launch gate in `chaosx_triggerable_scenarios_triggers.txt`
- Launch branch in `trigger_selected_chaosx_scenario`
- Wrapper call to `trigger_cannibalism_scenario`
- GUI, scripted localisation, documentation, and spreadsheet alignment

## 19. Exact shared-system call sites

### 19.1 Automatic random-event launch

1. Add Event 014 to `global.fire_once_events` in `common/scripted_effects/chaosx_logic_effects.txt`.
2. Add an Event 014 branch to `evaluate_random_event_active_pool_candidate`.
3. That branch calls `cannibalism_automatic_event_is_available`.
4. `evaluate_random_event_selection_candidate` continues to call the shared active-pool eligibility path.
5. In `fire_event_by_temp_id_no_cluster`, add an Event 014 preparation branch before generic dispatch.
6. That branch calls `cannibalism_prepare_random_event_fire`.
7. If `cannibalism_prefire_ready` is not 1, set `event_single_fire_allowed` to 0.
8. Generic dispatch calls `country_event = chaosx.nr[EVENT_ID].1` only when permitted.
9. Event `.1` calls `cannibalism_begin_from_prefire_context`.
10. The existing post-dispatch handler records fire-once history and the Event 014 event-log history entry.

A failed pre-fire search must not register Event 014 as fired. A successful pre-fire generation can be consumed only once.

### 19.2 Event log

Update `events_log_set_default_actor_for_current_event` with an Event 014 branch.

- Require `has_event_target = cannibalism_first_host`
- Require `event_target:cannibalism_first_host = { exists = yes }`
- Set that scope as the default actor

Update live event weight handling so Event 014 displays N/A when `cannibalism_automatic_event_is_available` is false.

Evolution rows are written only by `cannibalism_record_evolution_stage`. The base fire row remains owned by the shared post-dispatch handler.

### 19.3 Shared classification triggers

Update `is_special_chaos_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt` to include:

- `cannibalism_warlord_country`
- `cannibalism_unified_country`
- `cannibalism_wendigo_hannibal_country`

Update `is_actual_nonhuman_country` to include only `cannibalism_wendigo_hannibal_country`. Ordinary cannibal warlords and ordinary Hannibal remain human for shared civilian-system logic.

Document both changes in `common/scripted_triggers/chaosx_dynamic_triggers.md`. Confirm that `uses_normal_civilian_systems` continues to derive the intended result.

### 19.4 Deaths, population, and world threat

- Preserve and verify `apply_exact_state_civilian_population_loss` and its companion documentation.
- Preserve and verify Deaths cause `cannibalism_consumption = 15` across the full cause pipeline.
- Preserve the centralized initial consumption chaos weight of 0.20 unless the Event 014 balance audit changes it.
- Add `world_threat_source_cannibalism` to `refresh_world_threat_state`, the shared world-threat predicate, and the system documentation.
- Event 014 calls the exact population helper through `cannibalism_consume_current_state` only.
- Event 014 calls `refresh_world_threat_state` through `cannibalism_refresh_world_threat_source` only.

### 19.5 Wendigo compatibility

- Keep dynamic ZZZ as the Wendigo route host and call the existing `weaponized_zombie_unlock_profiled_template` after Event 014 state integration.
- Do not copy the Wendigo profile onto CBL or a reusable warlord tag.
- Add the merged-country exclusion to `chaosx.nr2.11`.
- Keep existing pure-Wendigo terminal behavior unchanged.
- Event 014 owns its two terminal bridges and unique super-event calls.

## 20. Idempotency and invalid-scope rules

| Operation | Idempotency key | Invalid-scope behavior |
|---|---|---|
| Automatic pre-fire | `global.cannibalism_prefire_generation` against consumed generation | Cancel dispatch before history is recorded |
| System initialization | Active flag plus consumed pre-fire generation | Return without clearing existing runtime |
| Actor registration | Country scope plus actor generation | Do not append |
| Node registration | State scope plus node ID and generation | Do not append or overwrite |
| Actor pulse | Global sequence against country last-processed sequence | Skip actor and reconcile registry later |
| Node pulse | Global sequence against state last-processed sequence | Skip node and reconcile registry later |
| Spread resolution | Spread ID, status, source generation, and aligned index | Mark row invalid. Do not mutate target |
| Population consumption | Request ID against state last request ID | Return `duplicate` or `invalid_scope` with zero applied loss |
| Evolution transition | Global stage plus recorded flag | Do not apply content or log a second row |
| Warlord initialization | Slot ID plus slot generation | Do not create cores, units, ideas, or registration twice |
| Warlord cleanup | Slot ID plus expected generation | Do not clean a later incarnation |
| Convergence | Active flag plus frozen participant generations | Cancel or recalculate. Do not annex unmatched participants |
| Player transfer | Explicit response plus source and host generation | Abort before annexation |
| Wendigo merge | Merged flag plus both source generations | Abort and leave both countries intact |
| Local victory | Country local-defeat flag plus stabilization state | No global mutation |
| Global victory | Global defeated flag plus zero-residue stabilization | No second cleanup or terminal transition |
| World end | Route-specific world-end flag plus shared world-end state | No second super event |

Never dereference a scope array entry or event target before an existence check. Never treat a cached count as proof that the associated scopes exist.

For a partially invalid aligned array, the runtime marks the affected entry invalid, completes the current iterator without index deletion, then compacts the arrays afterward. It does not shift array indexes during iteration.

For a missing pulse anchor, lifecycle code chooses a replacement from validated actor scopes. If no live actor exists, it uses a stable eligible event-system country only long enough to reconcile global residue. If no valid country scope exists, it stops scheduling and preserves enough global state for a later narrow lifecycle hook to resume. This is engine-safe suspension, not a gameplay fallback.

## 21. First implementation tranche

The first tranche should establish the transaction-safe core before warlords, convergence, scripted GUI, or terminal routes are implemented.

### Step 1. Constants and shared contracts

- Create `014_cannibalism_constants.txt` with identity enums and opening tuning.
- Add `014_cannibalism_triggers.txt` with opening eligibility and live-scope guards.
- Preserve and verify `apply_exact_state_civilian_population_loss` and its companion documentation.
- Complete or verify the Deaths cause 15 pipeline.
- Add the three shared country classification changes and threat-source input.

### Step 2. Opening selection and registration

- Add `014_cannibalism_effects.txt` with pre-fire selection, system initialization, actor registration, node registration, and count rebuilding.
- Wire Event 014 into the fire-once registry, active-pool candidate evaluation, pre-fire dispatch preparation, default event-log actor, and N/A weight.
- Add the hidden `.1` dispatcher and visible `.2` host response.
- Register the opening host and incident state through canonical APIs.

### Step 3. Consumption and one pulse

- Implement the request-ID consumption wrapper.
- Implement one pulse anchor, one delayed `.10`, actor and node sequence guards, and narrow state-control plus annex reconciliation.
- Validate Deaths-enabled and Deaths-disabled population parity before adding any route content.

### Step 4. Evolution I and completion proof for the tranche

- Implement Evolution I through its setting gate.
- Record its log row only after successful transition.
- Add task-specific localisation, documentation, and opening asset wiring.
- Run the opening, duplicate-dispatch, duplicate-consumption, anchor-annexation, and evolution-disabled scenarios below.

Do not start fixed-tag release or convergence implementation until the first tranche proves deterministic selection, exact population loss, persistent registration, and scheduler recovery.

## 22. Validation scenarios

These are implementation scenarios, not generic syntax checks.

### 22.1 Opening and dispatch

1. No ordinary wartime country is eligible. Event 014 has N/A weight, creates no targets, fires no event, and records no history.
2. Two countries have the same host score. Repeated runs select the same first country and state.
3. The generic event-system dispatch country differs from the selected host. `.1` still initializes the selected host and `.2` appears only to that host.
4. The selected state changes controller between pre-fire selection and `.1`. The second validation cancels initialization without a partial actor.
5. Event 014 is already active. A second automatic dispatch does not clear or duplicate the runtime.

### 22.2 Population and larder

1. Apply the same valid consumption request with Deaths enabled and disabled. The state loses identical population and Event 014 receives identical larder.
2. Repeat the same request ID. No second population, larder, total, node, or Deaths mutation occurs.
3. Request more population than remains above the configured reserve. The helper returns the clamped real loss.
4. Consume the same state across five completed ticks. Applied loss follows the configured diminishing factors.
5. Target Death-consumed, zombie-consumed, severe-fallout, and ordinary contaminated territory. Yields are zero, zero, zero, and the configured partial factor.
6. Invalidate the actor target after request preparation. The state remains unchanged.

### 22.3 Pulse and lifecycle

1. Fire `.10` twice for one global pulse sequence. Every actor and node mutates once.
2. Annex the pulse anchor. The annex handler assigns a valid replacement before old-scope cleanup and exactly one later pulse occurs.
3. Annex a normal actor with live nodes. Nodes either transfer, recover, or retire according to explicit route rules. No array entry crashes or silently points at an unrelated scope.
4. Change control of a feeding state during a due spread. The queue resolution revalidates controller and target context.
5. End a civil war involving a warlord. The winning scope and tag generation reconcile without duplicating actor registration.

### 22.4 Evolution and logging

1. Disable Evolution I. No Evolution I flags, effects, visible event, or log row appear.
2. Enable Evolution I at its threshold. The transition occurs once and records one type 1, stage 1, tier 1 row.
3. Start above multiple pre-fire thresholds. Only enabled stages apply, in numeric order, and each successful stage logs once.
4. Remove the actor before log preparation. The transition aborts or logs without actor only according to the shared event-log contract. It never dereferences a missing target.

### 22.5 Warlord generation and convergence

1. Allocate all eight slots. A ninth request blocks cleanly with no partial country or core changes.
2. Defeat slot 2, leave a delayed spread row from its old generation, and reach the nominal quarantine date. Slot 2 remains reserved until the row is invalidated or resolved.
3. Reuse a released slot after all references clear. A stale old-generation callback makes no change.
4. Two human warlords reach convergence. Neither is silently absorbed. Only explicit accepted transfer can move the selected source player into CBL.
5. Fixed CBL is already live for an unrelated reason. Ordinary convergence blocks before adding cores, transferring a player, or annexing a participant.
6. CBL receives troops, nodes, larder, route state, and one unified generation once. Tracked cores from absorbed slots clean up without stripping unrelated historical cores.
7. A Wendigo convergence keeps dynamic ZZZ as host and never releases CBL.

### 22.6 Wendigo crossover and terminal routes

1. Merge an AI Wendigo with an Event 014 source. Dynamic ZZZ remains host, preserves its Wendigo package, receives Event 014 runtime, and adopts the merged cosmetic.
2. Merge a player-controlled Wendigo. ZZZ remains player-controlled and any source integration occurs only after response safety checks.
3. A merged actor still carries Wendigo compatibility flags. `chaosx.nr2.11` remains blocked.
4. The ordinary Hannibal route fires only the ordinary Event 014 super event.
5. The transformed merged route sets Event 014 and Wendigo compatibility world-end flags, then fires only the unique merged super event.

### 22.7 Victory, cleanup, and scenarios

1. One country clears its local outbreak while another island commune remains. Local victory occurs but global victory does not.
2. Cached actor and node counts are zero while one valid pending spread row exists. Global stabilization does not start.
3. Zero residue persists for the entire stabilization interval. Global cleanup clears the scheduler and threat source and sets durable defeat.
4. Residue reappears during stabilization. The clock resets.
5. Automatic selection after durable defeat stays blocked. Manual scenario launch can bypass it explicitly.
6. Silent Islands has no valid island. Launch is blocked before any mutation.
7. Warlord States and Convergence lack enough reusable slots. Launch is blocked before any tag reservation.
8. All five scenario types at all four intensities use the same canonical registration, consumption, and cleanup APIs.

## 23. Blockers and design dependencies

### 23.1 Exact supply and encirclement measurement

The consulted official documentation and available precedents do not expose a confirmed aggregate country or division supply ratio or a direct encirclement value suitable for automatic host scoring. Documented proxy inputs exist, including infrastructure damage, supply-node count, convoy threat, war duration, casualties, resistance, island status, and divisions relative to nodes.

Implementation needs one explicit choice before those concepts are represented.

- Approve a named proxy model and describe it to players only as pressure, damage, isolation, or attrition.
- Require further discovery and runtime validation of an undocumented direct trigger.

The implementation must not silently present a proxy as exact supply or encirclement.

### 23.2 Asset coverage

The frozen flag ledger contains exactly thirteen families: warlord tags `CBA` through `CBH`, dedicated unified host `CBL`, ordinary cosmetics `CBL_CENTRAL_COMMAND`, `CBL_HOST_CONFEDERATION`, and `CBL_RITUAL_STATE`, and merged dynamic-country cosmetic `ZZZ_CANNIBALISM_HANNIBAL`. Each family requires base, communism, democratic, fascism, and neutrality compositions at 82x52, 41x26, and 10x7. `CBL_LAST_TABLE` is obsolete and must not drive runtime identity. Their portraits, event images, idea icons, super-event art, and any scripted-GUI animation must be produced and wired through the asset workflow before route completion can be claimed.

### 23.3 Scenario source-of-truth mismatch

Existing registry IDs make Event 014 scenario 10. Any spec or spreadsheet row calling it scenario 8 must be corrected. Implementing it as 8 would collide with existing content.

### 23.4 Deaths cause balance validation

The Deaths cause ID is 15 and the centralized initial chaos weight is 0.20. The Event 014 balance audit must validate that value against actual consumption volumes. Callers must not override the shared constant.

### 23.5 Multiplayer convergence policy

The safe baseline is explicit response per non-host human country, one player-controlled host, and no forced absorption. If the design expects several human participants to share or rotate control of one tag, it needs a separate multiplayer design. The engine cannot preserve several human controllers in one country through ordinary `change_tag_from` consolidation.

### 23.6 Wendigo merged identity

The merged route requires Event 002's terminal exclusion, a unique Event 014 super event, the new cosmetic, and explicit compatibility flags. None can be omitted without allowing the older Wendigo path to bypass the specified transformation sequence.

## 24. Implementation handoff checklist

The main agent should not claim Event 014 complete until all items below are implemented and audited.

- Event 014 fire-once registry, availability, pre-fire preparation, dispatch, and history
- Hidden dispatcher and player-visible opening response
- Deterministic host and state selection
- Canonical actor, node, spread, convergence, transformation, and slot ledgers
- Exact population loss with Deaths parity and full cause 15 presentation
- Pulse anchor recovery and narrow lifecycle reconciliation
- All three evolution setting gates and log rows
- All five manual scenarios under stable ID 10
- Eight fixed tag slots with generation quarantine and tracked-core cleanup
- Player-safe convergence, Hannibal reveal, and unification
- Wendigo package preservation on dynamic ZZZ, Event 014 runtime integration into ZZZ, merged identity, Event 002 guard, and both Event 014 terminal routes
- Shared country classifications and Event 014 world-threat source
- Local victory, global residue proof, stabilization, and durable cleanup
- Localisation, icons, portraits, flags, GUI definitions, super-event assets, docs, spreadsheet, and presentation alignment
- Focus-tree, decision, localisation, country-package, and event-completion audits where those surfaces are present

No gameplay simplification is authorized by this architecture. The six dependencies above must be resolved or reported as blockers rather than replaced with weaker substitutes.

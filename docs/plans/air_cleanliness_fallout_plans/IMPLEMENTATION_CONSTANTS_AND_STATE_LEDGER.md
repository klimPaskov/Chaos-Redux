# Implementation Constants and State Ledger

## Naming policy

Use short subsystem names without unnecessary project prefixes. The proposed names below are implementation labels, not final player-facing localisation.

Shared values belong in `common/script_constants/`. Values that must be injected into unsupported static fields may use file-local `@` constants or verified meta effects. Do not duplicate threshold tables across events, decisions, GUI, and effects.

## Global Air state

Existing values to preserve:

| Name | Role | Lifecycle |
| --- | --- | --- |
| `global.air_contamination_bp` | global contamination in basis points | persistent |
| `global.air_contamination_monthly_delta_bp` | last monthly net change | refreshed monthly |
| `global.air_contamination_chaos_buffer_bp` | sub-one-percent Chaos conversion remainder | persistent |
| `global.air_contamination_chemical_states` | current chemical-state count | refreshed monthly |
| `global.air_contamination_irradiated_states` | current nuclear fallout state count | refreshed monthly |
| `global.air_contamination_irreversible` flag or equivalent | contamination floor and terminal ecological decline | persistent after trigger |

New global values:

| Proposed name | Type | Role | Reset rule |
| --- | --- | --- | --- |
| `global.air_winter_generation` | variable | serial number for a new winter cycle | increments when a new global winter cycle begins |
| `global.air_winter_peak_phase` | variable | highest state phase currently present | refreshed monthly |
| `global.air_winter_active_state_count` | variable | states at phase 1 or above | refreshed monthly |
| `global.air_winter_severe_state_count` | variable | states at phase 4 or above | refreshed monthly |
| `global.air_winter_terminal_state_count` | variable | states at phase 6 | refreshed monthly |
| `global.air_winter_population_exposed` | variable | population in active winter states | refreshed monthly |
| `global.air_winter_global_pressure` | variable | global forcing used by each state | refreshed monthly |
| `global.air_winter_recovery_pressure` | variable | global recovery force | refreshed monthly |
| `global.air_winter_flavour_serial` | variable | prevents duplicate incident presentation | increments per incident |
| `global.air_winter_last_summary_date` | variable | controls summary event cadence | updated on summary |
| `global.fallout_eligibility_pressure` | variable | post-100-percent gradual trigger pressure | refreshed monthly |
| `global.fallout_request_source` | variable | cause enum for current request | set on request, cleared after transition or abort |
| `global.fallout_request_intensity` | variable | severity input from caller | set on request |
| `global.fallout_request_date` | variable | audit and countdown date | set on request |
| `global.fallout_transition_phase` | variable | blackout and rewrite state | set during transition, cleared after finish |
| `global.fallout_transition_dirty` | variable | scripted GUI update marker | increment on visible phase change |
| `global.fallout_coordinator_last_reconcile_date` | variable | at-most-once project coordinator receipt | written before daily Fallout reconciliation |
| `global.fallout_event_timeline_generation` | variable | binds the living-world clock to the current transition | written once by the current map-return transaction |
| `global.fallout_event_timeline_start_date` | variable | exact successful map-return date | written once by the current map-return transaction |
| `global.fallout_event_timeline_start_day` | variable | arithmetic reveal day used for elapsed-day phase calculation | written once by the current map-return transaction |
| `global.fallout_event_registry_countries` | scope array | stable ordered post-allocation scheduler identities | frozen after successor allocation proves current |
| `global.fallout_event_registry_generation_entries` | numeric array | transition generation aligned to each registry country | frozen with the registry payload |
| `global.fallout_event_registry_index_entries` | numeric array | exact stable zero-based position for each registry country | frozen with the registry payload |
| `global.fallout_event_registry_cursor` | variable | round-robin index for one primary frozen registry country per coordinator date | wraps to zero after the final row |
| `global.fallout_event_schema_version` | variable | living-world runtime and transaction schema | schema 2 after a new registry commit or guarded dormant promotion |
| `global.fallout_event_ticket_generation` | variable | binds the ticket allocator to the active transition generation | reset only with an uncommitted registry rebuild |
| `global.fallout_event_next_ticket_id` | variable | next monotonic arc, delayed, or bilateral transaction ticket | incremented before a row commit and never decremented |
| `global.fallout_survival_ledger_schema_version` | variable | survival receipt schema | future producer writes before commit |
| `global.fallout_survival_ledger_generation` | variable | binds survival rows to the current transition generation | future producer writes before commit |
| `global.fallout_survival_ledger_country_count` | variable | exact finalized successor-assignment row count | future producer writes before commit |
| `global.fallout_survival_ledger_committed_date` | variable | immutable commit date receipt | future producer writes once |
| `global.fallout_survival_ledger_committed_day` | variable | immutable arithmetic commit-day receipt | future producer writes once |
| `global.fallout_rewrite_batch_index` | variable | persistent batch cursor | cleared on completion |
| `global.fallout_rewrite_error_count` | variable | safety counter for failed assignments | cleared on completion |
| `global.fallout_surviving_country_count` | variable | final survivor count | set after rewrite |
| `global.fallout_successor_country_count` | variable | final new successor count | set after rewrite |

Global flags:

| Proposed flag | Role | Clear rule |
| --- | --- | --- |
| `air_winter_active` | at least one state has winter phase | clear when no active state remains |
| `air_winter_severe_global` | severe share threshold reached | clear when share falls below hysteresis floor |
| `fallout_eligible` | normal contamination route may roll Fallout | clear only if reversible model allows contamination below threshold and no irreversible state exists |
| `fallout_requested` | a valid request is waiting | clear on transition start or abort |
| `fallout_transition_active` | player input locked by blackout | clear only after transition finish or recovery abort |
| `fallout_processing_states` | state grade and damage pass active | clear after state pass |
| `fallout_processing_countries` | country rewrite pass active | clear after country pass |
| `fallout_player_choice_required` | player needs successor selection | clear after valid choice or deterministic timeout choice |
| `fallout_active` | post-rewrite Fallout campaign mode | persistent |
| `world_end` | ordinary event system terminal guard | set at transition lock and retained |
| `world_end_fallout` | Fallout terminal branch marker | persistent |
| `fallout_manual_scenario_active` | manual launch owns the current request | clear after transition begins |
| `fallout_synthetic_strike_batch` | suppresses per-strike log and diplomatic spam | clear immediately after strike pass |
| `fallout_event_scheduler_initialization_pending` | a current map return may initialize the dormant living-world registry | clear only after a successful registry commit or proven dormant schema promotion |
| `fallout_event_scheduler_registry_ready` | the aligned country registry payload passed its commit proof | clear only when an uncommitted payload is rebuilt |
| `fallout_survival_ledger_ready` | all nine-resource rows passed schema, generation, and count proof | no setter until numeric initialization is accepted |
| `fallout_event_scheduler_activation_approved` | manual review approved gameplay scheduling | no setter until the pilot passes review |
| `fallout_event_scheduler_active` | ordinary living-world dispatch is live | no setter until all activation gates pass |

## Transition ledger schemas

| Ledger | Live schema | Contract |
| --- | --- | --- |
| Fallout world transition | 8 | fail-closed snapshot and destructive-phase receipt recovery |
| Government classifier | 2 | frozen-input signal aggregation and provisional archetype |
| Successor pre-allocation inventory | 1 | live countries, possible-country scopes, states, reservations, and package conflicts |
| Successor allocation output | 2 | consumed source receipt, reciprocal conflict links, unique assignments, package layers, capitals, and cleanup |
| Manual province sweep runtime | 2 | generation-bound batch, verifier, and exact seven-day callback provenance |
| Fallout living-world scheduler | 2 | exact reveal timeline, country runtime receipts, transaction history, and structural routing envelopes |
| Fallout living-world registry | 1 | aligned country, generation, and stable-index commit payload |
| Fallout orientation | 1 | five independent current-generation orientation receipts |
| Fallout arc, delayed queue, and bilateral ledgers | 2 | dormant aligned transaction rows, reservation APIs, cancellation, cleanup handoff, and mutation-bounded reconciliation |
| Fallout survival ledger | 1 | reserved schema and nine resource identities only, with no row contract or producer |

Living-world schema 1 contained initialization-only rows and no transaction producer. It may promote to schema 2 only while the map-return receipt is current, both activation flags are absent, the scheduler has no error, every preserved runtime field passes its current invariant, and every arc, delayed, bilateral, cleanup, history, ticket, and dispatch surface is absent or empty as required. A partially populated, corrupt, or active schema-1 row fails closed before mutation.

The region enum has nine live values: North America, Europe, Eurasian Interior, East Asia, South Asia, Middle East and North Africa, Sub-Saharan Africa, Latin America and the Caribbean, and Oceania and Remote Islands.

The tag-conflict resolution enum distinguishes continuation in place, conversion of an existing tag, release of a releasable, dynamic creation, retirement as a landless memory, preservation of another event package, and player reservation. A surviving assignment cannot use the landless-retirement result. Every non-retired frozen source must link to exactly one committed output country. The output must link back to the same source and carry the same resolution, generation, and cleanup owner. Converted outputs require a current conversion receipt. Released outputs require a current release receipt in addition to frozen possible-country membership. Dynamically created outputs require a current materialization receipt and absence from both frozen country collections. A retired source must own no state and must not name an output.

World transition schema 8 records request source and intensity, Chaos and Air Contamination values, every live country scope and government-memory row, and every state owner, controller, population, category, building, damage, resource, nuclear, Air Winter, coastal, contamination, and manual-strike input used by the rewrite. Player and world capture share one epoch generation and date. Air Winter producer schema 1 opens one distinct generation per complete snapshot attempt. Valid states receive a produced source kind only after canonical initialization, normalization, range proof, and exact live-to-frozen comparison. Invalid states receive an explicit N/A kind and Air-owned zero payload without initialization. Snapshot completion is written only after every row passes the synchronous capture proof, exact live owner and controller checks, and all-and-only player-origin checks. Blackout and world-end ownership remain uncommitted until both snapshot halves pass. Exact live ownership and live Air Winter equality are capture-time proofs. Later grading and rewrite receipts validate the frozen scope and provenance payload without requiring ownership or live climate values to remain unchanged. Grading cannot start when either half is incomplete. The same schema binds grading, population-loss, and physical-collapse receipts to the active transition generation. Phase-local population and building checks require current engine observations before advancing. Map return validates durable transaction receipts, so later population changes or normal repair do not invalidate completed destructive work.

The country-memory enum assigns ids 1 through 99 in the exact accepted row order from `matrices/baseline/fallout_successor_country_matrix.md`. The enum is an identity ledger only. It does not activate a candidate or approve a source tag, state package, fallback package, leader, focus tree, or asset set.

## State winter values

| Proposed name | Type | Range | Role |
| --- | --- | --- | --- |
| `air_winter_phase` | variable | 0 to 6 | visible state phase |
| `air_winter_pressure` | variable | 0 and above | current monthly escalation force |
| `air_winter_exposure` | variable | 0 to configured cap | persistent cumulative exposure |
| `air_winter_phase_months` | variable | 0 and above | consecutive months in current phase |
| `air_winter_recovery_months` | variable | 0 and above | consecutive months with recovery force above escalation |
| `air_winter_adaptation` | variable | 0 to 100 | shelter, governance, food, and infrastructure adaptation |
| `air_winter_monitoring` | variable | 0 to 3 | forecast and tooltip precision |
| `air_winter_food_reserve` | variable | 0 to configured cap | local survival stock |
| `air_winter_shelter_capacity` | variable | 0 to configured cap | protected population and administration |
| `air_winter_category_damage` | variable | 0 to configured cap | sustained category degradation progress |
| `air_winter_building_damage_pressure` | variable | 0 to configured cap | bounded building loss progress |
| `air_winter_population_loss_memory` | variable | 0 and above | cumulative winter deaths for map and events |
| `fallout_state_grade` | variable | 0 to 5 | monotonic physical-damage severity class |
| `fallout_state_subtype` | variable | 0 to 1 | separate fictional altered-biosphere overlay |
| `fallout_survival_value` | variable | 0 to 100 | independent continuation and successor viability ledger |
| `fallout_state_survival_value` | variable | 0 to 100 | successor viability and player choice score |
| `fallout_state_direct_strike_count` | variable | 0 and above | manual or live direct-strike memory |
| `fallout_state_cause_mask` | variable or flags | implementation-defined | cause memory for regional content |
| `fallout_pretransition_air_winter_original_category` | variable | Air Winter category enum | frozen category memory for Fallout classification |

Live destructive-phase receipt values:

| Name | Range | Proof role |
| --- | --- | --- |
| `global.fallout_snapshot_epoch_generation` | transition generation | establishes the single frozen world and player snapshot epoch |
| `global.fallout_snapshot_epoch_date` | current date value | proves both snapshot halves were captured during the same effect chain |
| `global.fallout_pretransition_air_winter_ledger_schema_version` | Air Winter producer schema | binds every frozen Air Winter row to the accepted producer contract |
| `global.fallout_pretransition_air_winter_ledger_generation` | positive producer generation | rejects stale same-date Air Winter receipts |
| `fallout_pretransition_snapshot_generation` | snapshot epoch generation | binds every frozen country and state row to the current snapshot epoch |
| `fallout_pretransition_air_winter_source_kind` | produced or N/A | distinguishes canonical values from deliberate non-applicable data |
| `fallout_pretransition_air_winter_source_schema_version` | frozen producer schema | binds the state payload to the global Air Winter schema |
| `fallout_pretransition_air_winter_source_generation` | frozen producer generation | binds the state payload to the exact snapshot attempt |
| `fallout_grade_score` | 0 to 100 | deterministic grade-band receipt |
| `fallout_state_grading_generation` | transition generation | binds grade and survival results to the current rewrite |
| `fallout_grade_score_reconciled` | state flag | proves the persisted grade score matches a fresh calculation from frozen inputs |
| `fallout_survival_value_reconciled` | state flag | proves the persisted survival value matches a fresh calculation from frozen inputs |
| `fallout_population_loss_percent_applied` | grade loss table | records the exact grade-derived Deaths percentage |
| `fallout_population_loss_requested_memory` | 0 and above | records the rounded Deaths request before the population floor |
| `fallout_population_before_loss_people` | 0 and above | records observed state population immediately before the Deaths transaction |
| `fallout_population_available_before_loss` | 0 and above | records population available above the protected one-person floor |
| `fallout_population_expected_loss` | 0 to requested amount | records the request after the observed population floor is applied |
| `fallout_population_after_loss_people` | 0 and above | records observed state population immediately after the Deaths transaction |
| `fallout_population_after_loss_k` | 0 and above | preserves the engine population value used by the phase-local observation check |
| `fallout_population_reconciled_loss` | 0 and above | records the observed before-and-after population difference |
| `fallout_population_loss_memory` | 0 to requested amount | records the population actually removed by the shared Deaths transaction |
| `fallout_population_loss_generation` | transition generation | binds the Deaths receipt to the current rewrite |
| `fallout_population_loss_reconciled` | state flag | proves the stored request, observed transaction output, and recalculated expected loss agree without applying Deaths again |
| `fallout_building_damage_levels_requested` | 0 and above | records the total requested building-damage levels |
| `fallout_building_damage_levels_observed` | 0 and above | records the observed increase across five state-building ledgers |
| `fallout_building_damage_before_<family>` | 0 and above | freezes immediate damaged levels for infrastructure, industrial complex, arms factory, air base, and dockyard |
| `fallout_building_damage_available_<family>` | 0 and above | freezes the undamaged levels available to the grade-derived request for each proven state-building family |
| `fallout_building_damage_requested_<family>` | 0 and above | records the independently calculated request for each proven state-building family |
| `fallout_building_damage_observed_<family>` | 0 and above | records the observed damaged-level increase for each proven state-building family |
| `fallout_building_damage_after_<family>` | 0 and above | records the engine level accepted by the phase-local observation check for each proven state-building family |
| `fallout_building_damage_reconciled` | state flag | proves every stored per-family request and observed delta agree without issuing another destructive effect |
| `fallout_state_rewrite_generation` | transition generation | binds building, category, supply, and modifier receipts to the current rewrite |

Province-scoped `supply_node` and `rail_way` damage are not part of this exact receipt. The documented state scope resolves only a matching province and cannot prove a complete state-wide network rewrite.

State flags:

| Proposed flag family | Role |
| --- | --- |
| `air_winter_phase_1` through `air_winter_phase_6` | optional cached flags if phase comparisons are too expensive in modifier triggers |
| `air_winter_original_category_*` | remembers original category band before permanent degradation |
| `air_winter_recent_phase_change` | gates phase-change flavour and map emphasis |
| `air_winter_recent_building_loss` | prevents repeated incident spam |
| `air_winter_recent_population_crisis` | prevents repeated incident spam |
| `air_winter_relief_route_active` | current foreign or treaty relief project |
| `air_winter_evacuation_active` | current local evacuation action |
| `fallout_state_processed` | state rewrite completed |
| `fallout_state_reserved_for_player` | cannot be assigned away before player handoff |
| `fallout_state_wasteland` | terminal uninhabitable class |
| `fallout_state_mutant_candidate` | fictional high-chaos package may use this region |

Do not store true or false state as numeric variables unless an engine surface requires it.

## Country Fallout values

| Proposed name | Type | Role |
| --- | --- | --- |
| `fallout_country_survival_score` | variable | determines survival, fracture, or extinction |
| `fallout_country_legitimacy` | variable | starting government cohesion |
| `fallout_country_food_security` | variable | starting survival loop |
| `fallout_country_shelter_network` | variable | population protection and recovery |
| `fallout_country_command_cohesion` | variable | military package quality |
| `fallout_country_science_capacity` | variable | research and decontamination route |
| `fallout_country_mutation_pressure` | variable | fictional high-chaos route value |
| `fallout_country_origin_archetype` | variable | archetype enum |
| `fallout_country_region_overlay` | variable | regional enum |
| `fallout_country_memory_overlay` | variable | memory package enum |
| `fallout_country_package_version` | variable | migration and audit version |
| `fallout_government_origin_archetype` | variable | frozen provisional identity assigned before ownership changes |
| `fallout_government_archetype` | variable | final reviewed archetype package applied to the successor |
| `fallout_government_classifier_generation` | variable | binds classification to the active transition |
| `fallout_government_classifier_schema_version` | variable | binds classification to classifier schema 2 |
| `fallout_successor_assignment_generation` | variable | binds the final assignment row to the active transition |
| `fallout_successor_conflict_source_country` | scope variable | links a committed output to its frozen input country |
| `fallout_successor_conflict_result` | variable | records the reviewed tag-conflict outcome |
| `fallout_successor_cleanup_owner` | scope variable | records the country that owns assignment cleanup |
| `fallout_successor_cleanup_generation` | variable | binds output cleanup ownership to the active transition |
| `fallout_live_tag_conflict_output_country` | scope variable | links a non-retired frozen input country to its committed output |
| `fallout_live_tag_conflict_cleanup_generation` | variable | binds source cleanup ownership to the active transition |
| `fallout_releasable_release_generation` | variable | proves an absent frozen possible-country scope was actually released in this transition |
| `fallout_dynamic_country_materialization_generation` | variable | proves a dynamic output was actually materialized in this transition |

### Live schema-2 living-world transaction row

Every frozen registry country owns the following persistent scheduler receipts. The three compact ledgers use aligned arrays. A physical removal always deletes the same index from every array in that family.

| Name | Role |
| --- | --- |
| `fallout_event_runtime_schema_version` | country runtime schema 2 |
| `fallout_event_runtime_generation` | transition generation shared by every local transaction row |
| `fallout_event_registry_generation` | generation of the frozen registry membership |
| `fallout_event_registry_index` | stable zero-based registry identity |
| `fallout_event_arc_schema_version` | compact arc schema 2 |
| `fallout_event_delayed_queue_schema_version` | delayed-result schema 2 |
| `fallout_event_bilateral_schema_version` | reciprocal bilateral schema 2 |
| `fallout_event_active_major_arc_count` | derived compact arc count with a maximum of three |
| `fallout_event_arc_reconcile_cursor` | next compact arc index inspected for this country |
| `fallout_event_delayed_reconcile_cursor` | next delayed index inspected for this country |
| `fallout_event_bilateral_reconcile_cursor` | next bilateral index inspected for this country |
| `fallout_event_last_transaction_reconcile_generation` | generation of the most recent bounded reconciliation |
| `fallout_event_last_transaction_reconcile_day` | arithmetic day of the most recent bounded reconciliation |
| `fallout_event_cancellation_count` | nonnegative count of typed cancellations recorded for this country |
| `fallout_event_last_cancelled_ticket` | most recent cancelled transaction ticket when the count is positive |
| `fallout_event_last_cancellation_reason` | typed owner, actor, target, reciprocal, generation, or caller reason |
| `fallout_event_last_cancellation_generation` | generation of the most recent cancellation |
| `fallout_event_last_cancellation_day` | arithmetic day of the most recent cancellation |
| `fallout_event_transaction_schema_migration_generation` | generation authenticated by a successful dormant schema-1 promotion |
| `fallout_event_transaction_schema_migration_day` | arithmetic day of that promotion |

Major-arc arrays:

| Aligned array | Stored field |
| --- | --- |
| `fallout_event_arc_ticket_entries` | globally allocated ticket |
| `fallout_event_arc_identity_entries` | content-owned stable arc identity |
| `fallout_event_arc_generation_entries` | runtime generation |
| `fallout_event_arc_primary_family_entries` | release-floor ownership family |
| `fallout_event_arc_cooldown_family_entries` | anti-repetition family |
| `fallout_event_arc_stage_entries` | opening through cleanup stage |
| `fallout_event_arc_actor_type_entries` | typed actor identity kind |
| `fallout_event_arc_actor_entries` | actor scope or institution token |
| `fallout_event_arc_outcome_entries` | typed outcome |
| `fallout_event_arc_cancellation_reason_entries` | typed reason for an aborted or cancelled arc |
| `fallout_event_arc_cleanup_token_entries` | content-owned cleanup identity |
| `fallout_event_arc_cleanup_owner_entries` | stable registry index that owns cleanup |

Delayed-result arrays:

| Aligned array | Stored field |
| --- | --- |
| `fallout_event_delayed_ticket_entries` | globally allocated ticket |
| `fallout_event_delayed_key_entries` | idempotent content transaction key |
| `fallout_event_delayed_generation_entries` | runtime generation |
| `fallout_event_delayed_parent_arc_ticket_entries` | optional parent arc ticket |
| `fallout_event_delayed_human_event_token_entries` | token reserved for a visible human result |
| `fallout_event_delayed_ai_event_token_entries` | distinct token reserved for hidden AI handling |
| `fallout_event_delayed_branch_entries` | selected content branch token |
| `fallout_event_delayed_due_day_entries` | earliest arithmetic dispatch day |
| `fallout_event_delayed_status_entries` | scheduled, resolved, cancelled, or cleanup status |
| `fallout_event_delayed_target_type_entries` | optional typed target kind |
| `fallout_event_delayed_target_entries` | optional target scope or institution token |
| `fallout_event_delayed_cleanup_token_entries` | content-owned cleanup identity |
| `fallout_event_delayed_cleanup_owner_entries` | stable local registry index |
| `fallout_event_delayed_outcome_entries` | typed result or cancellation outcome |
| `fallout_event_delayed_cancellation_reason_entries` | typed cancellation reason |

Bilateral arrays:

| Aligned array | Stored field |
| --- | --- |
| `fallout_event_bilateral_partner_entries` | exact reciprocal registry country |
| `fallout_event_bilateral_ticket_entries` | one ticket shared by both countries |
| `fallout_event_bilateral_key_entries` | one idempotent content key shared by both countries |
| `fallout_event_bilateral_generation_entries` | shared runtime generation |
| `fallout_event_bilateral_role_entries` | opposite initiator and responder roles |
| `fallout_event_bilateral_response_token_entries` | participant-specific visible response token |
| `fallout_event_bilateral_ai_response_token_entries` | participant-specific hidden AI token |
| `fallout_event_bilateral_due_date_entries` | shared arithmetic due day |
| `fallout_event_bilateral_status_entries` | reciprocal reservation and terminal status |
| `fallout_event_bilateral_cleanup_owner_entries` | initiator registry index shared by both rows |
| `fallout_event_bilateral_parent_arc_ticket_entries` | optional initiator arc ticket |
| `fallout_event_bilateral_cleanup_token_entries` | shared content-owned cleanup identity |
| `fallout_event_bilateral_outcome_entries` | shared typed outcome |
| `fallout_event_bilateral_cancellation_reason_entries` | shared typed cancellation reason |

The structural dispatch envelope uses `fallout_event_dispatch_source`, `fallout_event_dispatch_ticket`, `fallout_event_dispatch_generation`, `fallout_event_dispatch_mode`, `fallout_event_dispatch_event_token`, `fallout_event_dispatch_branch`, `fallout_event_dispatch_target_type`, and `fallout_event_dispatch_target`. `fallout_event_dispatch_ready` is written last. Validation requires a living owner, the exact current delayed or bilateral row, and the token appropriate to human, hidden AI, or hidden cleanup mode. Human and hidden AI bilateral responses require the responder role. The envelope does not fire an event.

Public transaction effects return acceptance, ticket, row, or pair receipts through temporary variables. An outer caller must create every output temporary variable before invoking the scripted effect. Internal calls follow this pre-seed contract. This is required because a temporary variable first created inside a nested scripted effect is not a persistent return value.

Recurring reconciliation validates full row shape linearly and performs a constant number of selected identity scans. When a delayed or bilateral dispatch envelope is ready, its exact candidate lookup and selected structural uniqueness proof add another constant number of linear passes over that source family. Exact reciprocal proof performs one partner lookup and one selected partner identity scan. A bilateral transaction may mutate that exact partner row. Reservation production alone runs full local uniqueness scans, which are quadratic in each uncapped local delayed or bilateral ledger. No delayed or bilateral queue cap exists.

Scheduler-owned country flags are `fallout_event_runtime_initialized`, `fallout_event_transaction_schema_migrated`, `fallout_event_arc_slot_1_active`, `fallout_event_arc_slot_2_active`, `fallout_event_arc_slot_3_active`, `fallout_event_arc_cleanup_pending`, `fallout_event_delayed_cleanup_pending`, `fallout_event_bilateral_cleanup_pending`, and `fallout_event_dispatch_ready`. Arc-slot and cleanup flags are derived caches. Their source arrays remain authoritative.

Country flags:

- `fallout_surviving_old_government`
- `fallout_successor_country`
- `fallout_warlord_country`
- `fallout_mutant_country`
- `fallout_refuge_government`
- `fallout_technical_enclave`
- `fallout_agricultural_survivor`
- `fallout_maritime_survivor`
- `fallout_bunker_regime`
- `fallout_country_package_applied`
- `fallout_focus_tree_loaded`
- `fallout_player_candidate`
- `fallout_ai_package_initialized`
- `fallout_existing_tag_conversion_committed`
- `fallout_releasable_release_committed`
- `fallout_dynamic_country_materialization_committed`

Actual archetype flags should follow the final accepted archetype identifiers from the matrix.

## Cause enum

Live stable enum values:

| Value | Cause |
| --- | --- |
| 1 | gradual Air Contamination collapse |
| 2 | Final Silence |
| 3 | chemical saturation |
| 4 | biological follow-through |
| 5 | mixed terminal cause |
| 6 | manual Fallout scenario |
| 7 | legacy Fallout request |

The enum affects state grading, regional flavour, successor package weighting, achievements, and post-rewrite memory. It does not replace detailed cause flags when several causes coexist.

## Winter phase enum

| Phase | Working implementation label | Mechanical identity |
| --- | --- | --- |
| 0 | clear | no active winter pressure |
| 1 | dimming | visibility, aviation, and local confidence begin to fail |
| 2 | crop shock | agriculture, food reserves, and rural stability decline |
| 3 | hard freeze | supply, construction, repairs, and population health deteriorate |
| 4 | black harvest | severe population loss, building decay, and migration pressure |
| 5 | ash winter | state category damage, industrial collapse, and warlord pressure |
| 6 | terminal winter | wasteland conversion risk and direct Fallout trigger pressure |

These are working labels only. Final player-facing names are written during implementation after localisation research and UI fit checks.

## State grade enum

| Grade | Working label | Rewrite role |
| --- | --- | --- |
| 0 | remote refuge | strongest administration and successor viability |
| 1 | scarred province | governable with lasting damage |
| 2 | ash zone | severe local loss and one-step category degradation |
| 3 | dead city | supply collapse and emergency-government pressure |
| 4 | wasteland | category conversion to wasteland |
| 5 | vitrified zone | highest physical-damage class |

Altered biosphere is subtype 1, not grade 6. It is fictional high-Chaos content with its own eligibility proof and modifier.

## Lifecycle invariants

1. A state has one visible winter phase at a time.
2. Phase changes use hysteresis. A single good month cannot instantly erase a severe phase.
3. Exposure can remain high while phase falls.
4. Category damage never progresses without sustained severe exposure.
5. A category can only degrade one step per configured minimum interval.
6. Population loss is registered once through the shared death pipeline.
7. Every Fallout state is processed exactly once per transition version.
8. Every active successor receives exactly one country package version.
9. Every human source and every snapshot-origin player state is reserved before the general successor inventory is frozen. A landless human receives an explicit materialization row instead of a fabricated state anchor.
10. Transition flags, arrays, and cursors use persistent script state intended for save-load. Runtime preservation has not been observed because HOI4 was not launched.
11. No inferred abort or partial map return is permitted. An unresolved postcondition keeps the blackout active and records the owning blocker.
12. Manual synthetic strikes suppress repeated global event logs and apply one aggregate history entry.
13. Player reservations become immutable when successor allocation initialization consumes them. Later drift records its own fail-closed error and never rebuilds the consumed ledger.
14. The living-world registry commits only after successor allocation proves current and each stored country index equals its exact array position.
15. Ordinary living-world events remain ineligible until all five orientation receipts are current and both scheduler activation flags are explicitly set by reviewed future work.
16. The future nine-resource ledger must cover every finalized successor after allocation and before player continuation. Survivor-allocation advancement and map return must gain that barrier in the same complete implementation tranche.
17. Arc, delayed-result, and bilateral tickets bind to one transition generation. Compact row removal deletes the same index from every aligned array in its family.
18. Arc occupancy flags derive from the compact array count and cannot exceed three active rows.
19. One primary frozen registry country reconciles per coordinator date and one primary row is selected from each transaction family. A proven bilateral pair may also mutate its exact reciprocal row. Recurring identity reads remain linear in the selected country and partner ledgers. Production-only full uniqueness gates are quadratic in each local ledger. Delayed and bilateral queue caps remain absent.
20. Dispatch and cleanup envelopes are data contracts. They neither schedule nor fire an event, and they do not execute content-owned cleanup.

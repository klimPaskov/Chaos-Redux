# Event 019 ordinary-country management handoff

## Scope and files

This tranche implements the baseline, Evolution I, and Evolution II ordinary-country management surface, plus the paid-country request dispatch boundary used once Evolution III is active. It does not implement Evolution III claimant decisions or Evolution IV anomalous-family decisions.

Created files:

- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
- `common/decisions/019_infantry_spawn_decisions.txt`
- `common/decisions/categories/019_infantry_spawn_decision_categories.txt`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_management_handoff.md`

No shared constants, triggers, localisation, interface, event, on-action, or asset files were edited. This handoff is intentionally uncommitted for the parent tranche review.

## Implemented management contract

- Stable selected-lot management: selection, audit/reveal, territorial assignment, training, standardization, emergency integration, reserve recognition, specialist preservation, and supervised demobilization resolve the current ledger row from a captured lot UID rather than trusting an index across a timed mission.
- Human selection: `infantry_spawn_select_next_ordinary_lot` cycles unresolved ordinary lots; the country pulse seeds the first unresolved ordinary lot only when no valid selection exists.
- Formation Roll Call: a selected auditing lot receives a dynamic audit duration. A valid lot under manageable control, or with Integration Staff, receives the full reveal/control/congestion result. A valid low-control audit without staff receives a partial reveal result; an invalid target fails and adds congestion. Evolution I's revised audit package supplies additional control and relief.
- Territorial roles: resolve a selected ordinary lot immediately, retain its finite template lock, improve control, and reduce structural congestion.
- Standardization: a timed cycle is restricted to baseline/Organized Muster profiles. It verifies the exact template, changes the aligned template row to `integrated`, removes the template UID from the locked-template auxiliary array, and unlocks only that non-prototype template for ordinary recruitment. Arsenal prototype profiles are excluded from this path. Low control fails the cycle unless Integration Staff is present; coherent Evolution I lots and Integration Staff shorten the mission.
- Emergency field integration: resolves a selected ordinary lot without unlocking its template, applies the specified control penalty, and activates officer, training, and supply burdens for a bounded training-cycle duration.
- Supervised demobilization: see the exact teardown proof below.
- Evolution I: Muster Districts assign eligible ordinary lots to `local_authority`, record assigned-lot capacity, improve control/congestion, and expose a future claimant district asset. The mission succeeds only if at least one eligible lot is actually assigned. Integration Staff uses an officer-search mission and creates capacity; Common Tables uses the stronger selected-lot standardization cycle; Specialist Companies uses exact teardown but returns only controlled support-equipment salvage and records the preserved cadre; Emergency Reserve resolves one selected reserve lot, stores its stable UID, and raises its training one step.
- Evolution II: selected-lot training, a state-backed rail-corridor mission, active prototype availability detection, and four random request modes (field reinforcement, mobile reserve, territorial defenders, specialist firepower). Training fails under low control unless Integration Staff is present. The rail mission succeeds only while the exact stored target state remains controlled.
- Requests: costs scale from controlled states, active Event 19 divisions, active lots, Muster Control shortfall, congestion, prior requests, and war state. Modes alter their equipment/fuel/manpower cost mix and weighted family pools. Costs are refreshed for UI/AI, recalculated immediately before payment, and rechecked against exact current stockpiles. Payment, request count, risk, and cooldown are committed before the random result. Failed generation is not refunded and therefore cannot be rerolled for free.
- Request evolution boundary: `infantry_spawn_dispatch_management_request_lot` keeps the weighted baseline/Organized Muster/Arsenal family-profile path through Evolution II. Only when `infantry_spawn_has_evolution_iii = yes` does the same paid-country request call the unrestricted unit-registry draw and materializer, with the chosen four-mode request bias and `country_request` context. Registry success is accepted only through `infantry_spawn_unit_registry_materialization_succeeded`; there is no fallback to an Evolution II draw. Beginning any paid request clears `infantry_spawn_muster_board_dormant`, so a country that declined the first Evolution III opening can deliberately reactivate the Board through the request economy.
- Generation closeout: open/audited generations close only when no unresolved lot state remains. Closeout decrements the unresolved-generation count once, records the stable generation UID, and sets the one-shot handoff flag.
- Pressure integration: `infantry_spawn_apply_management_pressure_adjustments` applies idempotent persistent management relief and paid-request congestion before clamping control, congestion, debt, and liability. The concurrent shared pressure helper calls this adjustment before selecting control, congestion, and equipment-debt idea tiers, while preserving active timed management burdens.

## Public hooks for parent wiring

Call these in country scope:

- `infantry_spawn_evolution_one_reevaluate_management = yes`
  - Idempotent Evolution I active-entry re-evaluation.
  - Sets `infantry_spawn_evolution_one_management_active`.
  - Refreshes the organized audit-success package and coherent-lot accelerated-standardization availability.
- `infantry_spawn_evolution_two_expand_management = yes`
  - Idempotent Evolution II active-entry expansion.
  - Sets `infantry_spawn_evolution_two_management_active` and `infantry_spawn_formation_request_available`.
  - Re-evaluates `infantry_spawn_prototype_management_available` and refreshes all four request-cost previews.
- `infantry_spawn_run_country_management_pulse = yes`
  - Country-scoped pulse/AI-parity hook; performs no global iteration and schedules nothing itself.
  - Initializes telemetry, closes resolved generations, runs active evolution re-evaluation, seeds/updates AI lot selection, refreshes costs, and recalculates pressure.
- `infantry_spawn_close_resolved_generations = yes`
  - Safe after any external lot-resolution effect.
  - Sets `infantry_spawn_generation_closeout_ready` and `infantry_spawn_last_closed_generation_uid` when a generation closes. The parent event-log/detail consumer should clear `infantry_spawn_generation_closeout_ready` after consuming it.
- `infantry_spawn_dispatch_management_request_lot = yes`
  - Paid-country request generation hook used internally by `infantry_spawn_request_random_formation` and available to other Event 19 country request surfaces.
  - Requires the selected mode in `infantry_spawn_request_mode_selection` and a previously committed payment/count/cooldown transaction.
  - Dispatches to the weighted Evolution II family path or the Evolution III unrestricted registry path according to the active evolution trigger, and returns immediate success in `infantry_spawn_request_generation_succeeded`.

Recommended parent invocation points:

1. Call the Evolution I/II hook once for each participant during the matching active-entry dispatch.
2. Call `infantry_spawn_run_country_management_pulse` from the existing per-country Event 19 pulse before rescheduling that country pulse.
3. Consume the closeout-ready flag in the Event 19 event-log/detail integration path.

## Evolution-scoring telemetry

Country counters/flags:

- `infantry_spawn_successful_management_actions`
- `infantry_spawn_failed_management_actions`
- `infantry_spawn_integrated_lot_count`
- `infantry_spawn_standardized_lot_count`
- `infantry_spawn_demobilized_lot_count`
- `infantry_spawn_preserved_specialist_cadre_count`
- `infantry_spawn_last_management_succeeded`
- `infantry_spawn_last_management_failed`
- `infantry_spawn_last_management_partial`
- `infantry_spawn_emergency_reserve_recognized`
- `infantry_spawn_muster_districts_established`
- `infantry_spawn_integration_staff_appointed`
- `infantry_spawn_rail_corridor_secured`

Global counters (defensively initialized on use and incremented in the natural success/payment paths):

- `global.infantry_spawn_total_requests`
- `global.infantry_spawn_total_management_successes`
- `global.infantry_spawn_total_management_failures`
- `global.infantry_spawn_total_integrated_lots`
- `global.infantry_spawn_total_demobilized_lots`

## Exact supervised-demobilization proof

The timed mission stores `infantry_spawn_demobilization_target_lot_uid`. At timeout:

1. The lot row is re-found by stable UID.
2. Each active unit row with the exact stable lot UID loads its unique `infantry_spawn_unit_delete_cohort_id_entries` value.
3. The engine unit is removed with `delete_unit = { id = <exact cohort> disband = no }`.
4. A synchronous `num_divisions` delta of exactly one is required before any obligation is changed.
5. Only obligation rows matching both the stable lot UID and stable unit UID, and only in `outstanding`/`servicing`, are settled. Their exact outstanding amount is removed from country liability/debt and lot debt, then the obligation becomes `forfeited` with zero outstanding.
6. Controlled salvage is calculated from those exact settled amounts. Normal demobilization uses `demobilization_salvage_share`; specialist preservation uses `cannibalization_salvage_share` but grants only support-equipment salvage.
7. Salvage is granted explicitly after teardown with `disband = no`; engine disband refunds are never used.
8. The teardown commits only after at least one exact cohort deletion and only when the lot's remaining unit count is exactly zero; an empty or partial ledger walk cannot resolve the lot.
9. The lot and template ledgers become `demobilized`/`retired`, the exact template is locked against recruitment, active counters decrease, and generation closeout is re-evaluated.
10. A failed exact deletion leaves that unit's obligations untouched, grants no salvage for the failed teardown transaction, records a management failure, and raises `infantry_spawn_ledger_invariant_failure`.

## Decision and mission identifiers

Category:

- `infantry_spawn_formation_management_category`

Decisions:

- `infantry_spawn_select_next_ordinary_lot`
- `infantry_spawn_audit_selected_lot`
- `infantry_spawn_assign_territorial_roles`
- `infantry_spawn_open_standardization_cycle`
- `infantry_spawn_supervised_demobilization`
- `infantry_spawn_emergency_field_integration`
- `infantry_spawn_establish_muster_districts`
- `infantry_spawn_appoint_integration_staff`
- `infantry_spawn_issue_common_tables`
- `infantry_spawn_preserve_specialist_companies`
- `infantry_spawn_recognize_emergency_reserve`
- `infantry_spawn_survey_formation_lots`
- `infantry_spawn_open_training_cycle`
- `infantry_spawn_reserve_rail_corridors`
- `infantry_spawn_request_field_reinforcement`
- `infantry_spawn_request_mobile_reserve`
- `infantry_spawn_request_territorial_defenders`
- `infantry_spawn_request_specialist_firepower`

Activated missions:

- `infantry_spawn_formation_roll_call_mission`
- `infantry_spawn_standardization_cycle_mission`
- `infantry_spawn_supervised_demobilization_mission`
- `infantry_spawn_training_cycle_mission`
- `infantry_spawn_muster_districts_mission`
- `infantry_spawn_officer_search_mission`
- `infantry_spawn_specialist_preservation_mission`
- `infantry_spawn_rail_corridor_mission`
- `infantry_spawn_request_cooldown_mission`

## Required localisation keys

Localisation was outside this tranche. Add UTF-8-BOM English localisation for the category, every decision, and every mission above: each identifier needs its base key and `<identifier>_desc`.

Decision tooltip keys:

- `infantry_spawn_select_next_ordinary_lot_tt`
- `infantry_spawn_audit_selected_lot_tt`
- `infantry_spawn_assign_territorial_roles_tt`
- `infantry_spawn_open_standardization_cycle_tt`
- `infantry_spawn_supervised_demobilization_tt`
- `infantry_spawn_emergency_field_integration_tt`
- `infantry_spawn_establish_muster_districts_tt`
- `infantry_spawn_appoint_integration_staff_tt`
- `infantry_spawn_issue_common_tables_tt`
- `infantry_spawn_preserve_specialist_companies_tt`
- `infantry_spawn_recognize_emergency_reserve_tt`
- `infantry_spawn_survey_formation_lots_tt`
- `infantry_spawn_open_training_cycle_tt`
- `infantry_spawn_reserve_rail_corridors_tt`
- `infantry_spawn_request_field_reinforcement_tt`
- `infantry_spawn_request_mobile_reserve_tt`
- `infantry_spawn_request_territorial_defenders_tt`
- `infantry_spawn_request_specialist_firepower_tt`

Custom-cost keys:

- `infantry_spawn_audit_selected_lot_cost`
- `infantry_spawn_support_equipment_management_cost`
- `infantry_spawn_standardization_cycle_cost`
- `infantry_spawn_muster_districts_cost`
- `infantry_spawn_army_experience_management_cost`
- `infantry_spawn_training_cycle_cost`
- `infantry_spawn_rail_corridor_cost`
- `infantry_spawn_request_field_reinforcement_cost`
- `infantry_spawn_request_mobile_reserve_cost`
- `infantry_spawn_request_territorial_defenders_cost`
- `infantry_spawn_request_specialist_firepower_cost`

The four request-cost strings should show their matching persistent variables (`..._xp_cost`, `..._infantry_cost`, `..._support_cost`, `..._truck_cost`, `..._train_cost`, `..._fuel_cost`, and `..._manpower_cost`) so the displayed price matches the exact pre-payment check.

The rail mission can name its state through `infantry_spawn_rail_corridor_target_state`; the selected lot can be described with `infantry_spawn_selected_lot_index` and the existing lot arrays.

## Assets

No new asset is required for function: all category/decision/mission icons use verified vanilla GFX sprites. Custom Event 19 art can replace those tokens later without changing identifiers or script behavior.

## Requested future constants (shared-constant owner)

The implementation uses only existing Event 19 script constants. For cleaner independent tuning, the shared-constant owner should consider adding these groups and replacing the current derived values:

- dedicated baseline management costs for audit, territorial assignment, standardization, training, Muster Districts, Integration Staff, Specialist Companies, and rail corridors (currently derived from `infantry_spawn_request_cost` bases);
- a dedicated Muster District duration (currently `infantry_spawn_timer.officer_search_days`);
- a dedicated Specialist Preservation duration (currently `infantry_spawn_timer.standardization_days`);
- a dedicated training-cycle control reward (currently `infantry_spawn_control.territorial_assignment`);
- dedicated paid-request scaling factors for active lots and Muster Control shortfall (currently composed from the reusable `infantry_spawn_factor` ladder);
- dedicated ordinary-management and request-mode AI base/factor values (currently the neutral reusable `infantry_spawn_factor` ladder);
- a dedicated category priority if the project wants to replace the file-scoped `@INFANTRY_SPAWN_MANAGEMENT_PRIORITY`.

These are tuning requests, not missing runtime dependencies.

## AI and balance review notes

- AI receives the same selected-lot operations and exact costs as a player. The country pulse chooses weak lots under severe congestion, strong lots in war, and the first unresolved lot otherwise; each decision then applies its own strategic weighting.
- Severe-congestion AI does not request another formation unless an enemy-controlled neighboring state threatens its capital. Low-fuel AI never chooses the mobile mode. Defensive/congested AI favors territorial results; major industrial AI favors specialist requests.
- Request cost examples from the current formula: a small peaceful country with five states, two Event 19 divisions, two active lots, congestion 40, Muster Control 45, and no prior requests pays roughly 17 XP, 723 rifles, 72 support equipment, 41 trucks, 2 trains, 516 fuel, and 2,478 manpower for a field request. A larger country with twenty states, ten Event 19 divisions, five active lots, congestion 60, Muster Control 45, and no prior requests pays roughly 25 XP, 1,111 rifles, 111 support equipment, 64 trucks, 3 trains, 794 fuel, and 3,810 manpower before mode changes. Each prior request adds the configured `prior_request_scale`, request pressure, risk-tail weight, and cooldown extension.
- Finite Arsenal profiles cannot pass ordinary standardization and cannot become recruitable clones. Demobilization never uses engine refund behavior. Requests pay and enter cooldown before the draw, and a failed draw is not refunded. Evolution II request weights do not draw unrestricted battalion/support combinations; that composition model starts only at Evolution III.

## Validation and remaining integration

- All three Clausewitz files have balanced blocks, paired quotes, tab indentation, no trailing whitespace, no unsupported comparison operators, and no unary negation of variable tokens.
- Every referenced `constant:category.key` resolves in the current Event 19 script-constant corpus, including the concurrent Evolution III registry enums used by the dispatch boundary.
- Every referenced Event 19 scripted helper resolves in the current repository; no duplicate top-level effect/decision identifiers were introduced.
- All reused decision/category icon tokens resolve in the vanilla interface files.
- Recovery evidence: after a transient failed write truncated the untracked management file, its exact state was reconstructed in a separate recovery artifact by replaying all 27 successful management-file patches from the local Codex JSONL in timestamp order. The artifact reproduced 1,577 lines and all 53 expected top-level effects, passed structure/inventory checks, and was moved back with `apply_patch`; the two subsequent hardening additions bring the final file to 1,589 lines with the same 53-effect inventory.
- The optional Event Chain Viewer scanned the workspace and produced linked lint evidence, but its event-only analysis skipped the new non-event files; the direct script checks above are the relevant evidence for this tranche.

Remaining parent-owned integration:

1. Wire the Evolution I/II entry hooks and country management pulse, and consume the generation-closeout flag. The request dispatch is already wired to the four management request decisions.
2. Add the required localisation and event-detail/event-log wording using the exact keys above.
3. Run the ordinary-country management audit after the parent merges concurrent Event 19 files.

No requested baseline/Evolution I/Evolution II management surface was omitted, no recurring global on-action was added, and no fallback implementation was used.

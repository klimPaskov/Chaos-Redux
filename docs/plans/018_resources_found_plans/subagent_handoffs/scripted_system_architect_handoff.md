# Event 018 scripted-system architect handoff

## Supersession note, 2026-07-11

This is a preserved early implementation handoff, not the current Event 018 contract or completion status. Its ownership model and API inventory remain useful provenance, but later implementation, specification promotion, and audits supersede its provisional values and parent-integration warnings.

In particular, the accepted opening-strength contract is `6 + floor(score / 5)`, clamped to 6 through 30 after the mandatory 720-resource package floor is removed from the scoring total. The `/ 4` formula stated later in this historical handoff is obsolete. Current evidence is recorded in `rf_018_01_cave_strength_recalibration_handoff.md`, `../018_static_acceptance_report.md`, the Event 018 tuning matrix, and `../improvement_loop_closure_handoff.md`.

The formerly parent-owned event, decision, on-action, cave-country, localisation, UI, documentation, asset, workbook, and audit integration surfaces have since been implemented or dispositioned. No unfinished task listed in this historical status paragraph is a current Event 018 blocker.

## Scope and status

The reusable Event 018 scripting layer is implemented. It is intentionally not a standalone gameplay implementation: the parent still owns event/decision/on-action wiring, the cave-country operational layer, localisation/UI, event-log and settings registration, assets, docs/spec reconciliation, and audits.

Changed files:

- `common/script_constants/018_resources_found_constants.txt`
- `common/scripted_triggers/018_resources_found_triggers.txt`
- `common/scripted_effects/018_resources_found_effects.txt`
- `common/mtth/018_resources_found_mtth.txt`
- this handoff

No shared gameplay file, event, decision, on-action, country/focus file, localisation, asset, spreadsheet, or spec was edited by this subagent. No commit was created.

## Core ownership model

The physical record is state-local. A field state owns:

- exact additions: `resources_found_added_oil`, `resources_found_added_aluminium`, `resources_found_added_rubber`, `resources_found_added_tungsten`, `resources_found_added_steel`, `resources_found_added_chromium`
- preserved pre-Event 018 snapshots: matching `resources_found_preexisting_*` variables
- derived resource totals: `resources_found_total_added`, `resources_found_distinct_resource_count`, `resources_found_resource_roll_count`, `resources_found_discovery_count`
- bounded field values: `resources_found_developed_yield`, `resources_found_excavation_depth`, `resources_found_workforce_safety`, `resources_found_foreign_pressure`, `resources_found_subsurface_disturbance`, `resources_found_breach_pressure`
- owner/controller scope tokens: `resources_found_recorded_owner`, `resources_found_recorded_controller`
- persistent lifecycle flags, contract/commission/border records, maxima, and cave-capacity history

A country owns:

- selected state token: `resources_found_selected_field`
- state-token array: `resources_found_owned_fields`
- for DHO, origin token/enum, cave strength, exact terminal counters, and terminal verification state

The state flag `resources_found_field_transaction_lock` serialises resource packages and full sealing. Callers should not write the six ledgers directly.

## Public effect API

### Discovery and package wiring

All items below use STATE scope:

- `resources_found_initialize_field_record`: creates the field record and country registry entry but adds no resources.
- `resources_found_apply_prefire_opening_package`: chooses the highest enabled pre-fire package. Use immediately after initialisation.
- `resources_found_apply_baseline_package`: one random standard-resource addition in `[80, 121)`, i.e. 80 through 120.
- `resources_found_apply_evolution_i_prefire_package`: 2–4 additions in `[80, 121)`.
- `resources_found_apply_evolution_i_active_package`: 1–3 additions in `[80, 121)`.
- `resources_found_apply_evolution_ii_prefire_package`: 3–5 additions in `[90, 141)`.
- `resources_found_apply_evolution_ii_active_package`: 1–3 additions in `[90, 141)`.
- `resources_found_apply_evolution_iii_all_resources_package`: one independent addition for each of the six standard resources in `[120, 201)`.

Evolution IV pre-fire deliberately uses the Evolution III all-six package, sets `resources_found_compressed_opening`, `resources_found_breach_prone_opening`, and `resources_found_compressed_incident_minimum_date`, and does not set public breach or create DHO. The incident sequence and public-crisis date remain parent-owned gates.

### Field lifecycle and diplomacy

STATE scope:

- `resources_found_suspend_field`
- `resources_found_resume_field`
- `resources_found_begin_partial_closure`
- `resources_found_complete_partial_closure`
- `resources_found_begin_full_seal`
- `resources_found_complete_full_seal`
- `resources_found_activate_contract` — requires regular target `resources_found_contract_partner_target`
- `resources_found_activate_commission` — requires regular target `resources_found_commission_sponsor_target`
- `resources_found_begin_border_crisis` — requires regular target `resources_found_border_claimant_target`
- `resources_found_handle_field_ownership_transfer`
- `resources_found_handle_field_control_change`
- `resources_found_refresh_field_record`

Partial closure and suspension preserve all six additions and ledgers. Full sealing is the only inverse: it first proves every current resource total is at least its corresponding Event 018 ledger, negates a copied temp value (never a scoped variable token), subtracts exactly the six ledgers, archives the removed amounts as `resources_found_sealed_*`, and permanently blocks Evolution IV. If that proof fails it subtracts nothing and sets `resources_found_full_seal_reconciliation_needed`; no substitute outcome or fallback is used.

Ownership transfer removes the old registry entry, binds the state to the current owner, preserves the physical field/ledger, and converts diplomatic records to pending review. Control change records disruption without rebinding legal ownership.

### Cave API

- `resources_found_calculate_cave_starting_strength` — STATE origin scope; requires global target `resources_found_cave_country`; outputs `resources_found_cave_starting_score` and `resources_found_cave_starting_divisions` on both the origin and cave country. Result is `6 + floor(score / 4)`, capped at 30.
- `resources_found_record_cave_origin` — STATE origin scope; requires persistent global target `resources_found_cave_country`; records the origin, enum, discoverer, breach owner/controller, field sequence, exploitation score, emergence date, exact six-resource origin ledger, player-dispossession flag, and removes the field from the old owner's registry.
- `resources_found_refresh_captured_state_capacity` — STATE scope; stores the current six-resource sum and exact capacity `floor(total / 10)`, capped at 10; cave origins always output 0.

Important captured-state order: call `resources_found_refresh_captured_state_capacity` before testing `resources_found_state_can_contribute_cave_capacity`. The trigger is deliberately pure and reads the refreshed `resources_found_capacity_source_total`. Eligibility is continuous DHO control (`is_controlled_by = DHO`), not legal ownership, so wartime enemy-owned captured states can activate after the parent-owned control window. `resources_found_cave_resource_denied` blocks eligibility without deleting either ordinary resources or the Event 018 ledgers.

### Terminal API

COUNTRY/DHO scope:

- `resources_found_reset_world_end_verification_inputs`
- `resources_found_refresh_near_control_status`
- `resources_found_start_world_end_verification`
- `resources_found_cancel_world_end_verification`
- `resources_found_complete_world_end_verification`

The core does not run a periodic world scan. The cave layer must populate and mark ready the exact inputs from its explicit state/control registry or one-shot verification pass:

- flags `resources_found_continent_registry_ready`, `resources_found_foothold_registry_ready`
- mismatch flags `resources_found_continent_scan_mismatch`, `resources_found_foothold_registry_mismatch`
- counts `resources_found_continent_eligible_state_count`, `resources_found_continent_scanned_state_count`, `resources_found_continent_owned_state_count`, `resources_found_continent_controlled_state_count`, `resources_found_continent_owned_controlled_state_count`, `resources_found_continent_remaining_state_count`, `resources_found_valid_foothold_count`

Start and completion both recheck origin ownership/control, exact continent equality, a valid distant foothold, Evolution IV, chaos strictly above 1000, and the shared world-end guards. Completion only sets `resources_found_world_end_verification_complete`; the parent terminal event owns the shared `world_end` write.

## Origin-continent contract

Exact names:

- origin state flag: `resources_found_cave_origin`
- cave-country state token: `resources_found_cave_origin_state`
- state and cave-country numeric enum: `resources_found_cave_origin_continent`
- resolver: `resources_found_resolve_state_continent_enum`

Enum constants mirror vanilla `map/continent.txt` exactly:

| Token | Constant | Value |
|---|---|---:|
| none | `constant:resources_found_continent.none` | 0 |
| europe | `constant:resources_found_continent.europe` | 1 |
| north_america | `constant:resources_found_continent.north_america` | 2 |
| south_america | `constant:resources_found_continent.south_america` | 3 |
| australia | `constant:resources_found_continent.australia` | 4 |
| africa | `constant:resources_found_continent.africa` | 5 |
| asia | `constant:resources_found_continent.asia` | 6 |
| middle_east | `constant:resources_found_continent.middle_east` | 7 |

Use engine tokens such as `is_on_continent = europe` for geography. The numeric enum exists for saved branching and localisation; it is not an engine continent token.

## Public trigger API

Field/selection:

- `resources_found_is_active_field`
- `resources_found_has_event_resource_ledger`
- `resources_found_resource_ledger_is_exactly_reversible`
- `resources_found_field_values_are_in_bounds`
- `resources_found_state_has_standard_resource_presence`
- `resources_found_is_valid_new_field_state`
- `resources_found_is_valid_enrichment_field`
- `resources_found_is_eligible_discovery_owner`
- `resources_found_country_has_valid_selected_field`
- `resources_found_selected_field_is_available_for_action`

Lifecycle/diplomacy:

- `resources_found_can_suspend_field`, `resources_found_can_resume_field`
- `resources_found_can_begin_partial_closure`, `resources_found_can_begin_full_seal`, `resources_found_can_complete_full_seal`
- `resources_found_evolution_iv_is_permanently_blocked`
- `resources_found_field_can_accept_contract`, `resources_found_contract_is_active_and_valid`, `resources_found_contract_requires_review`
- `resources_found_can_propose_commission`, `resources_found_commission_is_stable`
- `resources_found_can_enter_border_crisis`, the six `resources_found_border_is_at_*` stage triggers, and `resources_found_border_military_stage_ready`

Evolution/cave/terminal:

- `resources_found_is_evolution_i_enabled` through `resources_found_is_evolution_iv_enabled`
- `resources_found_can_begin_evolution_iv`
- `resources_found_state_can_form_first_cave_origin`
- `resources_found_state_can_reinforce_existing_cave_host`
- `resources_found_is_cave_origin_state`
- `resources_found_state_can_contribute_cave_capacity`
- `resources_found_cave_starting_strength_is_valid`
- `resources_found_world_end_exact_continent_inputs_valid`
- `resources_found_world_end_origin_inputs_valid`
- `resources_found_world_end_foothold_inputs_valid`
- `resources_found_can_start_world_end_verification`
- `resources_found_world_end_verification_complete`

The four evolution triggers are pure triggers. They directly mirror the shared disabled flags `events_log_disabled_evolution_18_18_1` through `_4` and shared chaos-tier minimum constants. Parent event-log/settings work must register Event 018/type 18/stages 1–4 consistently.

## MTTH variables

Country-scope pre-fire entries:

- `mtth:resources_found_evolution_i_prefire_interval`
- `mtth:resources_found_evolution_ii_prefire_interval`
- `mtth:resources_found_evolution_iii_prefire_interval`
- `mtth:resources_found_evolution_iv_prefire_interval`

State-scope active entries:

- `mtth:resources_found_evolution_i_active_interval`
- `mtth:resources_found_evolution_ii_active_interval`
- `mtth:resources_found_evolution_iii_active_interval`
- `mtth:resources_found_evolution_iv_active_interval`

The caller must check the matching evolution trigger before consuming the entry. The MTTH file centralises war, chaos, country-size, yield/depth, safety, suspension, incident, sealing, and compressed-opening factors; it does not schedule events itself.

## Parent wiring checklist

1. Entry event: choose a valid STATE, call `resources_found_initialize_field_record`, then `resources_found_apply_prefire_opening_package`.
2. Active repeat discoveries: select an active/enrichment state and call the corresponding active package.
3. Decisions/missions: use the public eligibility triggers and lifecycle effects; set `resources_found_full_seal_requirements_met` only after the actual requirements complete.
4. Ownership/control hooks: call the two transfer effects from bounded Event 018 hooks. No daily/weekly/monthly world pulse is needed.
5. Cave creation: save DHO as global target `resources_found_cave_country`, calculate starting strength from the origin state, then record the cave origin before transferring the state so breach owner/controller and player dispossession remain exact. Parent owns actual country creation, state transfer, armies, incidents, and event firing.
6. Capacity: after the parent activation/grace test, refresh each DHO-controlled non-origin state before reading the pure capacity trigger/output.
7. Terminal registry: populate every exact count/flag, mark both registries ready, start verification, cancel it if any input becomes false, and call completion only when its trigger passes.
8. Shared integration: register Event 018 in event availability/evolution settings, event log, actor/name mappings, details/evolution windows, and all required localisation/docs/spreadsheet surfaces.

## Validation evidence and remaining risks

- Every `constant:resources_found_*` reference in the three script consumers resolves to a declared key.
- All four files have balanced block depth; the trigger file contains no variable-mutating effects.
- Capacity arithmetic was checked at boundary totals: 0→0, 9→0, 10→1, 19→1, 20→2, 48→4, 99→9, 100→10, 150→10; origin output is always 0.
- Package range maxima use the documented exclusive `set_temp_variable_to_random` contract.
- Full-seal inversion is ledger-exact and cannot execute when current resource totals cannot cover the ledgers.

Integration remains incomplete until the parent-owned checklist above is wired and audited. There are no deliberate gameplay simplifications or fallback implementations in this core layer.

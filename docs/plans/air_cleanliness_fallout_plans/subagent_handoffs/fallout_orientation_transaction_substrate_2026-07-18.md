# Fallout orientation transaction substrate handoff

## Scope and disposition

This handoff covers the dormant Ash-week Fallout orientation transaction substrate. It adds shared constants, country-scope transaction effects, and scripted triggers only. It does not add event blocks, localisation, assets, GFX, scheduler callers, or scheduler activation.

The substrate is suitable for the parent-owned `chaosx.fallout.62` through `chaosx.fallout.65` pilot, subject to the blockers below. No helper in this handoff sets `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

## Files changed

- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_orientation_transaction_substrate_2026-07-18.md`

## Transaction contract

All public transaction helpers use COUNTRY scope. Callers supply temporary `fallout_orientation_requested_*` inputs, then call the typed begin wrapper and `fallout_orientation_issue_next`. The substrate freezes the payload before writing `fallout_orientation_transaction_pending`. Event issuance writes the complete issued receipt and dispatch payload before writing `fallout_orientation_event_issued`.

The typed begin wrappers are:

- `fallout_orientation_begin_national_orientation`
- `fallout_orientation_begin_capital_condition`
- `fallout_orientation_begin_immediate_resource_crisis`
- `fallout_orientation_begin_government_archetype`
- `fallout_orientation_begin_character_or_institution`

The root event calls `fallout_orientation_choose_branch` after supplying the issued event token and requested branch. Hidden AI roots call `fallout_orientation_choose_ai_branch_and_schedule_result`, which evaluates the same affordable branches, applies deterministic weights, and commits through `fallout_orientation_choose_branch`. Human and AI paths therefore use the same costs, scoring, result delay, and result effects.

The typed result wrappers are:

- `fallout_orientation_resolve_national_orientation`
- `fallout_orientation_resolve_capital_condition`
- `fallout_orientation_resolve_immediate_resource_crisis`
- `fallout_orientation_resolve_government_archetype`
- `fallout_orientation_resolve_character_or_institution`

Each accepted result records the existing orientation component receipt through `fallout_event_record_orientation_component`, retains last-result and memory variables, then clears the transient transaction and state targets. Closure uses `fallout_orientation_begin_closure`, `fallout_orientation_schedule_cleanup`, and `fallout_orientation_cleanup_event84`. Stale generations can be cancelled with `fallout_orientation_reconcile_stale_generation`.

Every entry helper returns `fallout_orientation_transaction_accepted` as a temporary variable. Value `1` means the authenticated transition was accepted. Value `0` means no commit occurred.

## Authentication and state targets

The transaction requires the current Fallout transition generation, durable terminal cause memory, the exact successor assignment country row, the current country event-registry row, and the durable survival country resource row. Root choice and component resolution also require the persistent source state target to:

- exist
- equal `fallout_successor_assignment_capital_state`
- remain owned and controlled by ROOT
- pass `fallout_survival_state_identity_row_is_current`
- pass `fallout_successor_state_inventory_row_is_current`
- pass `fallout_successor_assignment_capital_row_is_current`

Capital evacuation applies the survival and inventory proofs to the receiving state at choice and resolution. The receiver must differ from the exact source capital.

The source state is derived from the durable successor assignment. It is stored in the country variable `fallout_orientation_state_target`. An optional receiving event target is copied into the country variable `fallout_orientation_receiving_state_target`.

Both variables hold scope pointers. Gameplay addresses them with `var:fallout_orientation_state_target` and `var:fallout_orientation_receiving_state_target`. This country-owned route replaced a shared global event-target design after audit showed that two concurrent successor transactions could overwrite one another.

The pointers are saved before the pending marker. They are cleared after an authenticated component finish, authenticated event 84 cleanup, or stale-generation cancellation.

## Frozen payload

The persistent frozen fields are:

- identity and choice context: `fallout_orientation_frozen_region`, `fallout_orientation_frozen_archetype`, `fallout_orientation_frozen_country_memory`, `fallout_orientation_frozen_cause_memory`, `fallout_orientation_frozen_component`, `fallout_orientation_frozen_branch`, `fallout_orientation_frozen_outcome`
- crisis and score context: `fallout_orientation_frozen_crisis_resource`, `fallout_orientation_frozen_crisis_value`, `fallout_orientation_frozen_primary_resource`, `fallout_orientation_frozen_primary_value`, `fallout_orientation_frozen_weakest_resource`, `fallout_orientation_frozen_weakest_value`, `fallout_orientation_frozen_cohesion`, `fallout_orientation_frozen_tailored_resource`
- current resource snapshot: `fallout_orientation_frozen_resource_food`, `fallout_orientation_frozen_resource_clean_water`, `fallout_orientation_frozen_resource_medicine`, `fallout_orientation_frozen_resource_scrap`, `fallout_orientation_frozen_resource_fuel`, `fallout_orientation_frozen_resource_power`, `fallout_orientation_frozen_resource_filters`, `fallout_orientation_frozen_resource_shelter`, `fallout_orientation_frozen_resource_recognition`
- state context: `fallout_orientation_frozen_target_state_grade`, `fallout_orientation_frozen_target_state_phase`, `fallout_orientation_frozen_target_exposure`, `fallout_orientation_frozen_target_shelter`, `fallout_orientation_frozen_target_recovery`, `fallout_orientation_frozen_target_adaptation`, `fallout_orientation_frozen_target_reclamation`, `fallout_orientation_frozen_target_supply`, `fallout_orientation_frozen_target_population`
- population and migration context: `fallout_orientation_frozen_country_population`, `fallout_orientation_frozen_source_population`, `fallout_orientation_frozen_receiving_capacity`, `fallout_orientation_frozen_receiving_shelter`
- match context: `fallout_orientation_frozen_archetype_match`, `fallout_orientation_frozen_regional_match`, `fallout_orientation_frozen_unresolved_crisis`
- government row payload: `fallout_orientation_frozen_archetype_effect_kind`, `fallout_orientation_frozen_archetype_effect_value`, `fallout_orientation_frozen_archetype_effect_days`, `fallout_orientation_frozen_archetype_effect_token`
- candidate payload: slot 1 through slot 3 `id`, `type`, `region`, and `archetype` fields under the `fallout_orientation_frozen_candidate_slot_*` names

## Constants and tuning

The constants file owns schema, stage, status, diagnostics, five branch tables, candidate types, government effect kinds, exact score bands, exact 2, 3, 4, 3, and 2 day result delays, costs, result magnitudes, AI weights, dynamic modifier magnitudes, dynamic modifier durations, death fractions, migration shares, and reserved event tokens 62 through 84.

The transaction branch remains `0` during a root event and must be greater than `0` before any result can resolve. Valid committed branches are `1`, `2`, and `3` for each component.

Timed modifier durations are copied from script constants into temporary variables before passing them to `days =`.

## Deaths and migration accounting

State death helpers route civilian population removal through `apply_exact_state_civilian_population_loss` and retain at least one civilian. Country-proportion losses traverse `global.fallout_survival_ledger_states` in stable order, apply the request across all owned states, disable duplicate state Deaths logging, and record the exact country total once through the Deaths API with reason `fallout_aftermath`. Requested and applied counts are stored separately.

Capital evacuation uses this conserved sequence:

1. Intended evacuation is `round(source population * 0.20)`.
2. Success moves the intended amount. Partial moves `round(source population * 0.12)`. Failure requests movement of `round(source population * 0.06)` plus deaths of `round(intended evacuation * 0.04)`.
3. Movement plus deaths is clamped to receiving capacity before population mutation.
4. The exact population helper removes the clamped total from the source state with Deaths logging disabled for that removal.
5. Destination population gain equals the actual source removal minus applied deaths.
6. Applied deaths are logged exactly once through the country Deaths helper.
7. Source exposure changes stay on the source state. Receiving shelter changes apply to the receiving state.

This keeps source removal equal to destination gain plus Deaths, including source-population and capacity clamps.

## Fail-closed surfaces

`fallout_orientation_surface_status` provides typed `blocked` and `approved` values. This substrate never writes any of the following approval variables:

- `fallout_orientation_capital_repair_surface_status`
- `fallout_orientation_state_result_surface_status`
- `fallout_orientation_government_row_surface_status`
- `fallout_orientation_character_install_surface_status`
- `fallout_orientation_regional_row_surface_status`
- `fallout_orientation_archetype_row_surface_status`
- `fallout_orientation_memory_row_surface_status`

Capital branch 1 requires `fallout_orientation_capital_repair_surface_status = approved`. It therefore remains unavailable until an exact infrastructure repair effect is reviewed and wired. Construction-as-repair and unsupported repair flags were not used.

Government component begin, branch availability, AI affordability, and resolution require `fallout_orientation_government_row_surface_status = approved`. This remains unset until `fallout_orientation_frozen_archetype_effect_token` is authenticated against and dispatched through an exact government-archetype registry row.

Character component begin, branch availability, AI affordability, and resolution require `fallout_orientation_character_install_surface_status = approved`. This remains unset until candidate slot IDs and types are authenticated against a curated registry and the chosen character or institution is installed through the exact registry-backed effect. Numeric receipt variables and flags are not treated as installation proof.

Capital, resource, government, and character results require `fallout_orientation_state_result_surface_status = approved`. This remains unset because the current `fallout_orientation_state_*` variables have no accepted live Air Winter or post-transition supply consumer.

Every component begin requires the regional, archetype, and country-memory row gates. They remain unset until the nine regional rows, twelve archetype rows, and manually reviewed successor overlays authenticate their exact match and Cohesion inputs.

These gates are blockers, not fallback implementations. The parent must not set a gate merely to expose the branch. Each gate should be set only by the future implementation that supplies the missing exact surface.

## Validation evidence

- Confirmed the `constant:fallout_orientation_*` references in the effects and triggers resolve to keys in the owned script-constants file.
- Confirmed every added orientation effect, trigger, and constant category has a unique top-level identifier.
- Confirmed the added orientation sections have balanced braces. This check found and led to correction of four malformed one-line `if` blocks.
- Confirmed the added trigger section contains no mutation effects.
- Confirmed the added sections contain no unsupported `<=` or `>=` operators.
- Confirmed the orientation helpers contain no scheduler activation setter.
- Confirmed `git diff --check` reports no whitespace error in the three gameplay files.
- Confirmed vanilla effect documentation supports `add_manpower` in STATE scope for receiving-state population movement.
- A scoped HOI4 MCP event lint was attempted. Its first selector was rejected by schema, and the corrected scan did not return before the parent requested immediate finalization. It is not counted as passing evidence.

## Simplifications, omissions, and blockers

- Exact capital infrastructure repair remains blocked behind its unset typed approval gate.
- Exact government registry-row token dispatch remains blocked behind its unset typed approval gate.
- Exact curated character or institution installation remains blocked behind its unset typed approval gate.
- Exact state-result mutation remains blocked behind its unset typed approval gate.
- Regional, archetype, and country-memory row producers remain blocked behind three unset typed approval gates.
- Event blocks 62 through 65, their localisation, six assets, and sprite registrations were added by the parent after this substrate handoff. Events 66 through 84, event log detail content, scheduler callers, and activation remain absent.
- Because government and character surfaces remain blocked, the complete five-component orientation sequence cannot yet reach closure.

No fallback or weaker substitute was used for any blocked surface. No files outside the granted ownership were edited.

## Skills and references used

- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-subagents`
- Required offline Paradox wiki core pages, including event targets and event modding
- Vanilla effects and triggers documentation, script constants documentation, and state-scope `add_manpower`
- Existing Chaos Redux survival ledger, event registry, exact state civilian population loss, Deaths logging, and orientation receipt helpers

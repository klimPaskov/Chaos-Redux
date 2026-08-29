# Migration presentation effects

This file documents the state-scoped presentation adapters in `migration_presentation_effects.txt`.

The helpers expose population-scaled dynamic modifiers without changing a population ledger, a transfer receipt, a death record, a reception load, a cohort registry, or a route target.

## Public effects

### `migration_presentation_refresh_state`

Scope: one valid state.

Purpose: rebuild all ten requested presentation phases after an owner has finished an authoritative transaction or lifecycle update.

The helper first removes only this layer's flow modifiers and derived flags, then reads persistent presentation projections and authoritative live ledgers, adds the currently proven modifiers, and forces a dynamic-modifier update.

The helper consumes direct one-shot `migration_presentation_input_*` variables after a successful valid-state refresh, except that active exodus is derived only from the current equal flight pair; it never consumes or clears a persistent projection receipt.

The immediate temporary result is `migration_presentation_refresh_result`, where `1` means a valid state was refreshed and `0` means the helper failed closed.

### `migration_presentation_clear_state`

Scope: one valid state.

Purpose: remove the ten flow presentation modifiers, clear derived presentation-only flags, and zero derived shares and modifier values before a refresh or terminal state cleanup.

This effect intentionally does not clear persistent presentation projection flags or values, authoritative migration ledgers, food-stage modifiers, population, manpower, deaths, reception loads, cohort arrays, route targets, or core lifecycle flags.

### `migration_presentation_compute_share`

Scope: the current state or another scope with the documented temporary variables.

Inputs: temporary `migration_presentation_input_proven`, `migration_presentation_input_people`, and `migration_presentation_input_denominator`.

Output: temporary `migration_presentation_share`.

Formula: `share = clamp(people / denominator, 0, 1)` when proof, people, and denominator are all positive, otherwise `share = 0`.

The helper uses no persistent ledger and has no population side effects.

### Persistent projection record effects

The six record effects accept one exact people/denominator proof plus exact generation and role metadata, compute a clamped share, and set their own active lifecycle flag. Preparing may omit the cohort id because it is legitimately pre-cohort, while the other five records require a positive cohort id.

The phase-specific input variables are consumed by the record effect, while the generic metadata remains action-local until the next successful refresh clears it; this lets sequential role updates in one state chain replace their own metadata without clearing another phase receipt.

`migration_presentation_record_preparing_projection` records `migration_presentation_input_preparing_proven`, `..._people`, and `..._denominator` into the preparing projection.

`migration_presentation_record_organized_evacuation_projection` records `migration_presentation_input_organized_evacuation_proven`, `..._people`, and `..._denominator` into the organized-evacuation projection.

`migration_presentation_record_depopulated_projection` adds `migration_presentation_input_depopulated_districts_people` exactly once for each newer positive core transfer generation, preserves the first exact pre-debit denominator as the cumulative baseline, and records the latest exact cohort/generation/role metadata.

`migration_presentation_record_transit_projection` records `migration_presentation_input_transit_proven`, `..._people`, and `..._denominator` into the hosted transit projection.

`migration_presentation_record_return_readiness_projection` records `migration_presentation_input_return_readiness_proven`, `..._people`, and `..._denominator` into the eligible return-readiness projection.

`migration_presentation_record_resettlement_return_projection` records `migration_presentation_input_resettlement_return_proven`, `..._people`, and `..._denominator` into the survivor-credit or durable resettlement/return projection.

The organized, depopulated, transit, return-readiness, and resettlement/return records require `migration_presentation_input_cohort_id > 0`, `migration_presentation_input_generation > 0`, and a positive `migration_presentation_input_role`. Preparing requires positive generation and role proof but permits a missing or zero cohort id.

The organized record requires the organized-evacuation role, the transit record requires the transit role, and the resettlement/return record accepts only resettlement, voluntary-return, or forced-return roles.

The record effects store phase-specific `..._projection_people`, `..._projection_denominator`, `..._projection_share`, `..._projection_cohort_id`, `..._projection_generation`, and `..._projection_role` variables and set the matching `..._projection_active` state flag. The depopulated record additionally stores `..._projection_last_generation` as its idempotency key, adds only newer generations, and never changes its first valid baseline denominator.

An invalid or non-positive proof leaves an existing receipt unchanged and clears only the attempted one-shot input, so terminal cleanup remains explicit and fail-closed.

### Persistent projection clear effects

`migration_presentation_clear_preparing_projection` clears the preparing receipt and active flag.

`migration_presentation_clear_organized_evacuation_projection` clears the organized-evacuation receipt and active flag.

`migration_presentation_clear_depopulated_projection` clears the cumulative depopulated-district receipt, its last-generation idempotency key, and active flag.

`migration_presentation_clear_transit_projection` clears the hosted transit receipt and active flag.

`migration_presentation_clear_return_readiness_projection` clears the eligible return-readiness receipt and active flag.

`migration_presentation_clear_resettlement_return_projection` clears the survivor-credit or durable resettlement/return receipt and active flag.

`migration_presentation_clear_all_projections` calls all six phase-specific clear effects.

Each phase-specific clear effect is idempotent and touches no other phase receipt, so clearing one role cannot erase a concurrent role.

The generic metadata is one action-local staging bundle, so an owner performing multiple role updates in one chain must set it immediately before each record call; a successful refresh clears the shared staging metadata only after all phase reads complete.

## Owner-call API

All owner inputs are state-scoped normal variables.

For a phase without an authoritative live ledger, the owner must set its phase input variables and the generic metadata variables, call the matching record effect once, and then call `migration_presentation_refresh_state`.

The generic metadata variables are `migration_presentation_input_generation` and `migration_presentation_input_role`, plus `migration_presentation_input_cohort_id` for every persistent role except preparing. Preparing may omit the cohort id or set it to zero because the operation is legitimately pre-cohort.

The role value must come from the core transfer-role enum, including `constant:migration_core_reconciliation.transfer_projection_role_organized_evacuation` for organized evacuation and `constant:migration_core_reconciliation.transfer_projection_role_transit` for transit.

| Phase | Source and formula | Lifecycle contract |
| --- | --- | --- |
| Preparing to leave | Exact planned or accepted amount divided by its exact state denominator. | Record while preparation is live; clear when preparation is canceled or execution begins. |
| Active exodus | The positive equal pair `migration_flight_pressure` and `migration_state_flight_population` divided by the current `state_population_k * 1000` denominator while `migration_displacement_active` proves the current flight obligation. A mismatch fails closed. | Rebuild from the live paired obligation; never infer it from a completed departure receipt, historical role, or prior live cohort. |
| Organized evacuation | Exact prepared/mission/request amount divided by its exact denominator, stored with cohort and generation metadata. | Keep active only until successful debit; clear the organized receipt at that terminal, then record depopulation separately. |
| Depopulated districts | Exact cumulative actual origin debit divided by its exact pre-debit denominator. | Durable history by default; clear only on an exact state retirement or history reset. |
| Reception | Exact live `migration_state_reception_load` divided by current `state_population_k * 1000`. | Rebuild from the live reception ledger; no projection receipt is needed. |
| Overcrowded reception | The same exact live reception load and denominator, gated by `migration_overcrowded_context_active`. | Rebuild from the live owner-capacity breach context; no flat threshold is inferred here. |
| Trapped population | Exact `migration_state_trapped_population` divided by current `state_population_k * 1000`. | Rebuild from the live trapped ledger; route deaths remain in the separate Deaths channel. |
| Transit | Exact hosted transit cohort amount divided by its exact denominator, stored with cohort and generation metadata. | Keep active while the hosted cohort is live; clear on exact departure, integration, or terminal failure. |
| Return readiness | Exact eligible return cohort divided by its exact denominator, stored with cohort and generation metadata. | Keep active while the cohort is eligible; clear when readiness expires, is canceled, or becomes a return transfer. |
| Resettlement/return | Exact survivor credit or durable outcome amount divided by its exact denominator, stored with cohort and generation metadata; the core durable counters are a read-only fallback only while their exact context flags are active. | Preserve the durable outcome until explicit state retirement or history reset. |

Every people value must be a non-negative people-unit amount and every denominator must be a positive people-unit amount.

An omitted or non-positive proof, people value, denominator, cohort, or generation produces a zero share or leaves the previous receipt untouched; no guessed headcount or route proxy is accepted.

## Role separation

The completed `migration_projection_last_origin_departure_share` is historical receipt data and is never used as the active-exodus people amount or as an organized-evacuation amount.

The active-exodus path reads the positive equal `migration_flight_pressure` and `migration_state_flight_population` pair as the presentation people amount and divides it by the current live denominator.

The paired flight amount is presentation-only and is not an origin debit, survivor credit, route-death amount, or destination population.

Active organized projection suppresses the active-exodus presentation so one live obligation cannot appear as two simultaneous movement phases; no historical role receipt is consulted for active exodus.

The origin share and cumulative depopulation share use exact actual origin debit and exact pre-debit population when an owner records them.

The depopulated projection uses the core monotonically increasing `migration_projection_last_generation` as its per-state idempotency key. A newer generation adds one measured actual origin debit, an equal generation is a replay and adds nothing, and the first valid pre-debit denominator remains the stable cumulative baseline.

The destination reception and overcrowding shares use exact surviving reception load and the live destination denominator.

Route deaths are never included in movement, destination credit, reception load, transit load, or any presentation people amount.

## Dynamic modifier map

The existing final icon families are reused truthfully and no new asset is requested by this layer.

| Modifier | Icon | Dynamic fields |
| --- | --- | --- |
| `migration_state_preparing_to_leave` | `GFX_migration_state_exodus` | State production and controller army speed. |
| `migration_state_exodus` | `GFX_migration_state_exodus` | State production and controller army speed. |
| `migration_state_organized_evacuation` | `GFX_migration_state_exodus` | State production and controller army speed. |
| `migration_state_depopulated_districts` | `GFX_migration_state_exodus` | State production, local manpower, and local building-slots factor. |
| `migration_state_reception` | `GFX_migration_state_reception` | Local supplies, state production, and controller army speed. |
| `migration_state_overcrowded` | `GFX_migration_state_overcrowded` | Local supplies, controller attrition, and controller army speed. |
| `migration_state_trapped_border` | `GFX_migration_state_trapped_border` | Local supplies and controller army speed. |
| `migration_state_transit` | `GFX_migration_state_exodus` | Local supplies, state production, and controller army speed. |
| `migration_state_return_readiness` | `GFX_migration_state_return` | State production and controller army speed. |
| `migration_state_return` | `GFX_migration_state_return` | State production and controller army speed. |

The dynamic modifier fields use the clamped share multiplied by a full-share consequence.

The original full-share values reuse `migration_modifier` constants for active exodus, reception, overcrowding, trapped population, and return.

The new full-share values live in `common/script_constants/migration_presentation_constants.txt` under `migration_presentation`.

`local_non_core_manpower` is the percentage-style state modifier field used here; current vanilla documentation gives it two decimal places and vanilla dynamic-modifier precedents use fractional values such as `0.25`. The flat `local_manpower` field is intentionally not used for a 0..1 population share.

The depopulated building consequence uses `local_building_slots_factor`, a ratio field, rather than the flat `local_building_slots` count.

## Lifecycle and cleanup

Call `migration_presentation_refresh_state` after the authoritative transfer projection, reception delta, trapped-ledger update, active flight update, or return/resettlement projection has completed.

Call the matching `migration_presentation_record_*_projection` before that refresh when the phase has no authoritative live ledger and must survive unrelated refreshes. Preparing may be recorded before a cohort id exists; depopulation requires a positive cohort id and generation from the exact transfer receipt.

Call the matching `migration_presentation_clear_*_projection` on the exact terminal transition, then call `migration_presentation_refresh_state` so the modifier is removed.

Call `migration_presentation_clear_state` alongside core dynamic-modifier cleanup when a state is invalidated, removed, annexed, converted to wasteland, or otherwise leaves the accepted state registry.

The core `migration_clear_dynamic_modifiers` effect currently knows only its original modifier identifiers, so the parent/core owner must add this presentation clear call or an equivalent explicit removal of the five new modifier identifiers.

Projection receipts are independent by phase. A preparing update cannot clear transit, a transit terminal cannot clear depopulation history, and a return-readiness update cannot clear organized evacuation.

No event targets are created or cleared by this presentation layer.

No whole-world or uncontrolled recurring scan is performed.

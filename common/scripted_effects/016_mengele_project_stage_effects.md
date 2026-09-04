# Event 016 Mengele Computation stage helpers

This owner-local helper family implements the accepted Mengele Computation slice for Event 016. It is intentionally bounded to existing family ID `constant:brilliant_scientist_project_family.computation` and existing stage IDs `theory`, `prototype`, `deployment`, and `weaponization`.

## Public selector contract

Every entry-point effect is country scope and reads these temporary selectors:

- `mengele_event016_project_family` is the existing one-based Event 016 family ID and must equal `constant:brilliant_scientist_project_family.computation`.
- `mengele_event016_requested_stage` is the existing stage ID and must equal one of `constant:brilliant_scientist_project_stage.theory`, `prototype`, `deployment`, or `weaponization`.

`brilliant_scientist_mengele_clear_project_stage_selectors` resets only those two private selectors and the private index to the shared `none` or zero values. It does not clear the older `brilliant_scientist_project_family` selector or unrelated caller temporaries.

Invalid, missing, unsupported-family, unsupported-stage, or malformed requests are no-ops. In particular, `brilliant_scientist_mengele_begin_project_stage` validates the request before calling the receipt initializer, so an invalid request never creates paid-history arrays or the initialization marker.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| `brilliant_scientist_mengele_initialize_project_stage_receipts` | Country | Validated provider request is required by the caller | `mengele_event016_provider_receipts_initialized` boolean country flag | Creates five aligned fifteen-slot arrays once; slots start at stage `none` and zero costs. |
| `brilliant_scientist_mengele_load_computation_stage_quote` | Country | The two private selectors | Temporary quote fields and `_quote_loaded` | Reads existing Event 016 duration/stage-cost constants and the new Computation Prototype quote. |
| `brilliant_scientist_mengele_begin_project_stage` | Country | The two private selectors | `mengele_event016_stage_started` temporary result | Validates provider, predecessor, stage ownership, and direct stockpiles; debits PP/support/fuel; stores the stage and all four quote receipts. |
| `brilliant_scientist_mengele_cancel_project_stage` | Country | Exact family/stage callback selectors | `mengele_event016_stage_cancelled` temporary result | Snapshots and clears the exact receipt, then refunds PP/support/fuel once; it does not require provider validity or existence. |
| `brilliant_scientist_mengele_finish_project_stage` | Country | Exact family/stage callback selectors | `mengele_event016_stage_finished` and output result temporaries | Settles an exact receipt even when the owner is invalid; only an existing valid provider can receive output, otherwise direct costs are refunded once. |
| `brilliant_scientist_mengele_apply_family_stage_output` | Country | Internal authorization temporary plus exact selectors | `mengele_event016_computation_output_applied` temporary result | Sets provider history, reuses the existing Theory and Mengele Prototype modifiers, and calls the neutral conventional API for the two full later tiers. |
| `brilliant_scientist_mengele_sync_native_project_prototypes` | Country | Computation selector and exact native output context | `mengele_event016_native_prototype_synced` temporary result | Authenticates the completed native computational engine, applies only provider Prototype history, and clears an optional pending marker. |
| `brilliant_scientist_mengele_record_native_project_prototype` | Country | New family selector or existing native callback family selector | `mengele_event016_native_prototype_recorded` temporary result | Routes an exact Computation native callback to the adapter without copying native payment or unrelated rewards. The legacy-selector fallback is accepted only when the private family selector is `none`. |
| `brilliant_scientist_mengele_reconcile_project_availability` | Country | Durable provider history and native state | `mengele_event016_project_availability_reconciled` temporary result | Sets or clears the existing Computation native presentation flag. |
| `brilliant_scientist_mengele_cleanup_provider_receipts` | Country | Existing provider arrays, if initialized | `mengele_event016_provider_cleanup_applied` temporary result | Cancels an active Computation receipt once, clears native pending/presentation markers, and retains completion history and neutral entitlements. |

The trigger file supplies the matching country-scope gates `brilliant_scientist_mengele_project_stage_provider_is_valid`, `brilliant_scientist_mengele_computation_stage_request_is_valid`, `brilliant_scientist_mengele_computation_stage_predecessor_is_valid`, `brilliant_scientist_mengele_computation_stage_can_pay`, `brilliant_scientist_mengele_computation_stage_receipt_is_empty`, `brilliant_scientist_mengele_computation_stage_receipt_matches`, and `brilliant_scientist_mengele_computation_native_output_is_authentic`.

The existing bridge trigger already owns the shorter name `brilliant_scientist_mengele_project_provider_is_valid`. The new stricter provider trigger intentionally uses a unique name to avoid a duplicate scripted-trigger definition. It requires either the actual scenario/victory/faction provider route or the existing full/restricted active-program trigger, which checks the program's live authority, site, and idea state rather than a bare authorization flag. It excludes both final and recently-expired Mengele program flags. The parent must route only the Computation branch that uses this core through the stricter trigger; do not broadly alias the existing nine-family bridge gate, because the other family adapters retain their own reviewed lifecycle and native prerequisites.

## Receipt storage and settlement order

The provider stores these regular arrays aligned to the shared fifteen family IDs at zero-based indexes 0 through 14:

- `mengele_event016_active_project_stage_entries`
- `mengele_event016_active_cost_political_power_entries`
- `mengele_event016_active_cost_support_equipment_entries`
- `mengele_event016_active_cost_fuel_entries`
- `mengele_event016_active_cost_civilian_factory_commitment_entries`

Computation is family ID 1 and therefore uses index 0. The factory array is a native-CIC quote only. The parent decision's `civilian_factory_use` modifier owns reservation and release, and no helper in this file calls `add_factories` or fabricates a factory refund.

Begin validates all gates before initialization and payment. Completion and cancellation require the exact current stage receipt, snapshot the three direct costs, clear every active receipt field first, and then settle exactly once. A wrong family, wrong stage, repeated callback, or absent receipt cannot clear or refund another stage. Finish uses `exists = yes` only inside its output-authority gate; the exact receipt is still settled when an accessible owner is invalid or dead, producing a direct-cost refund and no output, while cancel remains usable without provider validity.

## Computation tuning

Theory reads the existing quote of 1 CIC, 45 PP, 80 support equipment, 0 fuel, and 120 days. Prototype uses the new quote of 2 CIC, 68 PP, 200 support equipment, 100 fuel, and 180 days. Deployment reads the existing quote of 3 CIC, 90 PP, 600 support equipment, 500 fuel, and 270 days. Weaponization reads the existing quote of 5 CIC, 135 PP, 1200 support equipment, 1500 fuel, and 360 days.

The Prototype quote corresponds to the existing base 2 CIC, 75 PP, 250 support equipment, and 500 fuel multiplied by the Computation profile factors 0.80 factory, 0.90 PP, 0.80 equipment, and 0.20 fuel and rounded to whole units. The other three stage values remain sourced from `constant:brilliant_scientist_project_stage_cost` and `constant:brilliant_scientist_project_duration`.

Direct affordability is inclusive on this provider route. The equipment and fuel gates use `NOT = { has_equipment = { ... < quoted_cost } }` and `NOT = { has_fuel < quoted_cost }`, while Political Power uses `greater_than_or_equals`, so an exact balance is accepted without demanding one extra unit. Existing Kruger board gates remain unchanged. Native CIC availability is intentionally outside the scripted cost gate because it belongs to the decision modifier reservation.

## Stage outputs and neutral API

Theory sets `mengele_event016_computation_theory_completed` and applies the existing `brilliant_scientist_computation_theory` modifier. The parent modifier owner must enable this modifier for the provider's durable Theory receipt.

Prototype sets `mengele_event016_computation_prototype_completed`, preserves the existing `directorate_special_project_computation_completed` flag, clears the existing presentation flag, and applies `mengele_directorate_computation_prototype` once. The parent modifier owner removes that temporary provider modifier when the neutral Computation operational package is learned.

Deployment calls `chaosx_grant_conventional_technology_package` with Computation, Deployment, and `constant:mengele_event016_project_stage.provenance_mengele`, then sets `mengele_event016_computation_deployment_completed` only after the API reports success. Weaponization does the same with the full Weaponization tier and sets `mengele_event016_computation_weaponization_completed` after success. The neutral API owns cumulative package flags, runtime reconciliation, provenance arrays, and one-slot research adoption.

The fixed non-event source is `constant:mengele_event016_project_stage.provenance_mengele = 100001`. A repository scan found no current consumer collision; the only textual hit outside this helper is an offline wiki event-number example. The helper does not inherit a caller's optional source and resets the shared neutral API selectors after each call. The existing `brilliant_scientist_project_family` selector remains untouched.

## Native prototype adapter

The parent native presentation path should retain `directorate_special_project_computation_available` as the durable presentation receipt after Theory and must leave it set while the native project is active. If the parent uses `mengele_event016_native_computation_prototype_pending`, that flag describes the exposed native route only; it is not a second clock, payment reservation, or required start callback. Vanilla special-project documentation exposes `project_output` and iteration effects but no project-start callback, so the parent must call `brilliant_scientist_mengele_record_native_project_prototype` only from the exact `sp_brilliant_scientist_computational_engine` `project_output` branch after setting the Computation family selector. The adapter then requires the strict provider, the provider Theory receipt, and `is_special_project_completed = sp:sp_brilliant_scientist_computational_engine`, so a native project that completed before Theory cannot fabricate provider history through a generic poll. It records only the provider Prototype output. It never debits or refunds native project resources, adds CIC, copies a payment, or creates unrelated stage rewards.

The existing computational native project's risky unique-reward branch still calls Kruger accident/incident helpers unconditionally. The smallest safe parent integration is an additive provider branch in that existing reward: a strict Mengele provider must use an existing provider-safe incident/recovery state or existing Event 016 event surface, while only the Kruger branch may call `brilliant_scientist_refresh_project_accident_pressure` and `brilliant_scientist_dispatch_project_accident`. If no provider-safe incident surface exists, the native route must remain an explicit integration blocker rather than silently dropping the risk. This helper intentionally does not edit the native project file.

## Lifecycle, targets, and cleanup

This core uses no event targets. All provider state is country-scoped and persists through the aligned arrays, flags, and neutral API receipts. Parent-owned close, expiry, defeat, victory, annexation, death, and terminal callers must invoke `brilliant_scientist_mengele_cleanup_provider_receipts` in the original provider scope, using an explicit `FROM` or saved owner target when a transfer effect changes the current scope. The cleanup effect does not initialize arrays, does not require the provider gate, and does not delete completed provider history or neutral API entitlements. It clears any optional native pending marker and presentation flag only after settling an active provider decision receipt.

The remaining family IDs 2 through 15 are deliberately not implemented in this file. Terminal and singularity execution, registry-wide cleanup, decisions, localisation, AI, CXT, event surfaces, and native project wiring remain parent-owned.

## Presentation and assets boundary

This helper adds no player-facing localisation, icon, GUI, focus, or event surface. Parent-owned decision rows continue to reference the existing Event 016 family-stage icons and localisation; no new sprite or `.gfx` registration is required for these private effects.

## Validation notes

Static source checks cover the four quote rows, the one-based-to-zero-based array mapping, invalid and unsupported request no-op ordering, exact receipt matching, three direct debits, no factory effects, and reset of API selectors. The intended source scenarios are repeat begin, wrong family, wrong stage, PP/support/fuel shortage, invalid-owner finish, cancel without provider validity, fixed source provenance, and native callback repeat suppression.

The mandatory narrow read-only Event MCP inspection for `chaosx.nr16.1` completed with partial status and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f73ba8df62da3d8579b33366762517f6aaa6585734d6ed6f72b52c2e17b7cf0c/65d6dd558cbb5c6cfd7a88b4a79c57258b7505f20ac876b55862d37f1656506e/event-trace-d9bc467fb6be.json`. The result reported `blockingDiagnostics = 0` but deferred workspace-wide helper/lifecycle projections and therefore did not provide engine execution evidence. No weighted helper exists in this slice, so probability inspection and comparison are not applicable. Agents do not launch the game; live native callback and decision acceptance remain parent/user validation gates.

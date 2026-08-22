# CBRN battlefield operations

## Purpose

The battlefield operation family is retained as an inactive compatibility design for an exact-state ground delivery layer. The installed engine surface does not provide the verified current-version selected-state condition receipt required by the accepted design, so every operation and its agent selector remain hidden and unavailable. No estimator, proxy, neutral receipt, or fallback is used.

The family defines four state-targeted timed decisions:

- Cylinder Release uses a prepared supply node or enemy formation area.
- Projector Barrage uses a prepared supply or fortified target.
- Artillery Fire Plan uses enemy formations and consumes chemical shell lots.
- Armored Delivery uses enemy formations, supply, or city targets and consumes sealed armored-delivery equipment.

The actions are not aircraft proxies, combat estimators, or country-wide pulses. They require a real selected state, an enemy controller, a valid war relationship, an active Army Headquarters chemical operation plan, the applicable battlefield policy, the selected agent project, and real national equipment.

The current installed build does not expose the required selected-state weather and terrain receipt from the timed decision or Army Headquarters scope. The operation family is therefore registered and fully gated but remains unavailable until the verified hook is supplied. The fail-closed gate is intentional: no fixed condition estimate, random state, capital proxy, combat proxy, or aircraft activity substitute is retained.

## Resolution flow

1. The player or route-aware AI selects one chemical agent in the CBRN operations category when the verified condition hook is available.
2. The state-targeted timed decision records the exact state and victim controller. The begin effect persists that selected state in the country-scoped `cbrn_battlefield_active_state` variable before the delayed operation leaves the selection chain; resolution and cancellation use that pointer instead of depending on an expired regular event target.
3. The begin effect checks the route, target, policy, HQ receipt, Chemical Readiness, Command Power, payload stock, and route equipment again.
4. The exact payload lot is consumed before the operation is committed. Gas masks, decontamination equipment, CBRN instruments, support equipment, and route equipment are consumed oldest-model-first. Artillery Fire Plan also consumes `chemical_shell_lot_1`.
5. Chemical Readiness and Command Power are debited at commitment. A bounded delayed event restores the committed readiness amount after the centralized recovery interval; no global periodic update is created.
6. The shared CBRN chemical exposure dispatcher receives the exact state, agent, class, route, severity, protection receipt, and condition receipt.
7. Resolution records disruption, military and civilian deaths, contamination, medical saturation, evidence, attribution, Condemnation, and history through the shared consequence pipeline.
8. Cancelled or invalid operations clean their state ledger. Physical payload and equipment already committed are not fabricated back into stock.

Shortage-ready operations use the explicit lower route floors and receive the centralized command, release-efficiency, and friendly-risk scaling. They do not bypass the route gate. Doctrine can raise operational harm and reduce Condemnation within the shared doctrine floor; it does not remove evidence, attribution, deaths, contamination, medical history, resistance trauma, or responsibility.

## Engine boundary

The current version exposes no verified exact-state receipt for continuous chemical air missions and no verified selected-state weather/terrain receipt for this timed Army-HQ operation family. Continuous missions therefore remain fail-closed, idle chemical-capable aircraft never contaminate a region, and the battlefield family is fail-closed at `cbrn_battlefield_current_version_condition_hook_verified` until an exact current-version hook exists. The old general-wide commander cylinder abilities remain disabled for the same reason. The persistent selected-state variable preserves lifecycle identity only; it is not a condition estimator or proxy. This file documents the boundary rather than retaining an estimator or proxy.

## Files and tuning

| Surface | File |
| --- | --- |
| Central timing, costs, condition receipts, and AI factors | `common/script_constants/cbrn_battlefield_operation_constants.txt` |
| Exact target and equipment gates | `common/scripted_triggers/cbrn_battlefield_operation_triggers.txt` |
| Selection, debit, commitment, resolution, and cleanup | `common/scripted_effects/cbrn_battlefield_operation_effects.txt` |
| Bounded readiness recovery | `events/cbrn_battlefield_operation_events.txt` |
| Player and AI state-targeted decisions | `common/decisions/cbrn_battlefield_operation_decisions.txt` |
| Agent name scripted localisation | `common/scripted_localisation/cbrn_battlefield_operation_scripted_localisation.txt` |
| Dedicated interface registrations | `interface/cbrn_battlefield_operations.gfx` |

Numeric values are gameplay tuning. Historical confidence is low to moderate because a route cost represents an operation-sized preparation and supply package rather than a fixed historical tonnage. The selected chemical agent changes the shared exposure profile; native battlefield operation gates do not use agent-specific success odds.

## Asset contract

The five registered sprites are:

- `GFX_decision_cbrn_battlefield_cycle_agent`
- `GFX_decision_cbrn_battlefield_cylinder_release`
- `GFX_decision_cbrn_battlefield_projector_barrage`
- `GFX_decision_cbrn_battlefield_artillery_fire_plan`
- `GFX_decision_cbrn_battlefield_armored_delivery`

They belong under `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/` and are registered by `interface/cbrn_battlefield_operations.gfx`. Existing Chaos Redux raid icons under `gfx/interface/military_raids/` are preserved and are not overwritten or used as cross-type substitutes. The five DDS outputs are packaged at the dedicated runtime paths, with source-art, alpha extraction, processed PNG, archive DDS, runtime DDS, hash, and final-size contact-sheet evidence in `docs/assets/chaos_warfare_system/stage_6_chemical_delivery/`. No placeholder or resized cross-type asset is accepted. Asset completion does not relax the fail-closed engine-hook gate.

## Future extensions

An exact current-version Army Headquarters target receipt could connect a prepared command ability to a selected state. A verified continuous-air mission hook could then add an explicit mission-activity condition without a region estimator. Neither extension should be enabled until the engine proof is documented and tested against the installed version.

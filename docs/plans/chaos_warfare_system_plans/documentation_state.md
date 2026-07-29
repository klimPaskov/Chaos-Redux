# Chaos Warfare documentation state

This handoff records the implementation surfaces and documentation state for the accepted Chaos Warfare and CBRN package.

## Authority order

The numbered specifications under `docs/specs/chaos_warfare_system_specs/specs/` are the accepted design source.

The system mapping files under `docs/specs/chaos_warfare_system_specs/matrices/` resolve implementation mappings and tuning ranges after the numbered specifications.

The specialist prompts under `docs/specs/chaos_warfare_system_specs/prompts/` provide bounded implementation guidance after the numbered specifications and matrices.

Later user decisions in the task supersede optional estimator retention and supersede any doctrine wording that would create, authorize, or conceal camp or genocide infrastructure.

## Current implementation state

- Chemical delivery routes use one shared exact-target payload and consequence dispatcher when their route proof is available.
- Selected-state chemical air raids and strategic rockets use the native raid result as their explicit condition receipt and never infer exposure from aircraft presence or an idle aircraft.
- Continuous ordinary-air contamination remains rejected fail-closed because no verified current-version eligible-activity hook has been established, and no estimator is retained.
- Chemical state contamination, Air Cleanliness, expiry, and continuing deaths use the canonical state-owned ledger and targeted recovery events.
- Biological agents have distinct lifecycle tuning and the accepted potency order Tularemia, Anthrax, Plague, Smallpox, with only Smallpox using the severe lifecycle result.
- Native biological raid success, critical, and disaster factors remain agent-neutral; agent profiles change downstream lifecycle potency and consequences rather than native raid success.
- Biological delivery is split across native raids, exact-state operative operations, bounded espionage sabotage, and historical country decisions where the current exact target surface supports them.
- Gas masks are producible, model-aware equipment with national reserve, military issue, civilian distribution, filter, stock-loss, and population-scaled decision ledgers.
- Army Headquarters is the theater preparation layer, while CBRN regimental support is the division layer with essential-equipment shortage scaling and finite upkeep cleanup.
- Doctrine increases CBRN operational potency and may improve the efficiency of an already separately authorized camp route where accepted terminal conditions are met, while its systemic diplomatic relief is limited to Condemnation impact.
- Doctrine does not create, authorize, or conceal camp or genocide infrastructure, and it does not erase evidence, attribution, deaths, contamination, medical load, resistance trauma, history, or responsibility.
- Evidence, attribution, deaths, contamination, medical saturation, resistance trauma, confirmed-use history, and responsibility remain recorded after doctrine mitigation.
- Existing `gfx/interface/military_raids` assets are preserved, and new raid assets are kept under their separate `gfx/interface/raids` path.

## Achievement conformance state

The achievement source is now split between exact startup receipts, exact event or operation receipts, and live current-state predicates. The generic achievement registry uses `possible = { always = yes }` for presentation only; the `happened` predicates enforce the recorded campaign receipts.

- The one-time startup transaction writes `cbrn_achievement_start_country_eligible`, `cbrn_achievement_starting_major_power`, and `cbrn_achievement_starting_civil_defence_profile` after accepted starting profiles. The common eligibility trigger requires the start-country receipt, and `A Mask for Every Door` requires the civil-defence receipt, so the prior missing-starting-eligibility finding is implemented and source-audited.
- `Quarantine Without Collapse` is implemented and source-audited. `cbrn_achievement_refresh_bio_containment_receipt` reads current and needed trucks and trains with exact `get_supply_vehicles_temp` receipts, applies the 0.80 `minimum_supply` threshold independently to each needed class, and writes `cbrn_achievement_outbreak_supply_ready_history` only during exact catastrophic-outbreak recovery. Its completion trigger requires that receipt, with no periodic estimator or building proxy.
- `No Wind Is Friendly` remains fail-closed because exact selected-state forecast and friendly-exposure receipts depend on the unavailable ground Chemical weather/terrain hook. Its completion trigger requires `cbrn_achievement_forecast_failure_history`, `cbrn_achievement_friendly_exposure_history`, `cbrn_achievement_operation_recovered_history`, and `cbrn_achievement_no_wind_clean_after_failure_history`, but no writers for those flags exist outside the trigger file.
- `The Antidote Arrived` remains fail-closed because its response receipts are written only by `cbrn_achievement_record_nerve_response`, whose only caller is the exact nerve-suppression state transaction. Sarin/Soman suppression still lacks exact condition and target-loss receipts.
- `Unbroken Supply Corridor` remains fail-closed because no exact assigned-Army supply-ratio receipt or major-offensive-objective completion receipt is available. Its operational and objective flags `cbrn_achievement_corridor_operational_history` and `cbrn_achievement_corridor_supply_objective_history`, plus substantive variables `cbrn_achievement_corridor_state_count` and `cbrn_achievement_corridor_supply_days`, have no current writers.
- `Air Is Still Breathable` remains unresolved because the accepted prompt requires any major or regional power with enemy Chemical use, while the current completion predicate has no accepted regional-power definition or gate and does not consume the startup major-power receipt. The Event 006-specific `is_independence_wave_regional_power` predicate must not be reused.
- `A Poisoned Victory` now requires current Condemnation at or above `constant:cbrn_achievement_threshold.minimum_active_condemnation` rather than only a historical peak; this item is source-audited, subject to the remaining package reachability audit.

## Documentation surfaces now indexed

The CBRN helper index is `common/scripted_effects/cbrn_scripted_effects.md`.

It now indexes the achievement, battlefield, biological-Air-Cleanliness, camp, chemical-state, doomsday, occupation, headquarters, and existing CBRN-specific helper files.

The canonical chemical delivery contract is `docs/systems/cbrn_chemical_delivery.md`.

The broader legacy and historical chemical route context is `docs/chemical_warfare/chemical_warfare_documentation.md`.

Designer, headquarters, protective-equipment, biological-lifecycle, and consequence details remain in their subsystem documentation and require the cleanup pass recorded in `documentation_cleanup_handoff.md`.

## Open evidence and engine-boundary items

- Ground Chemical exact-state Army Headquarters/weather/terrain receipt remains unavailable, so ground release-bearing routes and their forecast/friendly-exposure achievement receipts remain fail-closed.
- Nerve suppression exact state/weather/terrain/target-loss receipt remains unavailable, so its release and `The Antidote Arrived` response receipts remain fail-closed.
- Unbroken Supply Corridor exact assigned-Army supply-ratio and major-offensive-objective receipts remain unavailable; no proxy receipt is permitted.
- The current engine does not expose a verified continuous-air eligible-activity callback, so that route remains intentionally unavailable.
- The current engine does not expose a bombing or facility-capture transaction carrying the exact national decontamination equipment loss, so Hardened Mobile Plant does not claim that unsupported loss reduction.
- The current engine does not expose a static country-assignment API for the custom military industrial organizations, so country differentiation is represented through visibility, eligibility, and AI strategy weights rather than an invented assignment effect.
- Historically sourced unique national MIO identities remain unresolved, even though generic CBRN MIO families, visibility, and AI differentiation are source-audited.
- Precise live production shares and long-run AI pacing remain source-relative or user-owned runtime validation, not exact percentage receipts.
- The current selected-state raid surface does not expose verified live weather and terrain inputs to the outcome effect, so raid condition receipts are explicit native-outcome receipts rather than fabricated weather or terrain values.
- The native operation engine does not expose runtime equipment charged by an operation's `equipment` block, so the biological operative route documents its authoritative native cost and does not fabricate a numeric payload receipt.
- The accepted native decision-category presentation has no accepted consumer for the window-only readiness-seal, contamination-border, or operation-preparation animation concepts.
- The large technology inspection is partial and reports unresolved issues for the wider repository; those diagnostics are not evidence that a CBRN-specific surface is complete.
- Fresh bounded specialist audit prompts were unavailable because the platform rejected the prompts before producing reports; no specialist pass is represented as completed on that basis.

## Legacy migration state

Legacy chemical helper definitions remain load-safe compatibility surfaces while targeted reachability audits continue.

The active shared chemical dispatcher no longer mutates legacy state contamination or continuing-death helpers. The legacy `chem_apply_state_contamination` writer is structurally unreachable, so old callers cannot bypass the canonical payload, protection, evidence, attribution, medical, Air Cleanliness, death, and Condemnation receipts.

The generic Livens profile and old doomsday direct body are structurally unreachable, and commander-cylinder abilities remain unavailable until their exact target and condition contract is proven.

The remaining legacy definitions must not be described as active delivery routes unless a current caller is found and migrated.

The two ledgers still require a final identifier audit before the migration helper can be activated broadly.

## Completion status

This file is a current-state handoff, not a completion claim.

Stage 13 specialist audits, the improvement-loop closure, package scenarios, the achievement reachability findings above, and the final completion checklist remain required before the goal can be marked complete.

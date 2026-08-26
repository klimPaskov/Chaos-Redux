# Event 006 FORM-39 enabled civil-service cost localisation handoff

## Scope

This narrow localisation repair aligns the enabled FORM-39 civil-service cost row with the existing two-civilian-factory reservation applied by the decision.

## Changed path

- `localisation/english/006_independence_wave_formable_registry_l_english.yml`

## Repair

`independence_wave_form39_civil_service_cost` now displays the standard civilian-factory commitment already shown by its hover and blocked variants. Stability, command power, convoy/train alternative, reservation amount, project duration, triggers, payment, AI, cancellation, and cleanup remain unchanged.

## Validation

- The enabled, hover, and blocked rows now all disclose `civilian_factory_standard` and `£civ_factory`.
- The localisation file retains its UTF-8 BOM.
- `python -B .tools/audit_event6_allocator.py`: passed with 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, and the `3/4/5/7/10` ladder.
- The cost surface remains within the accepted four spendable groups: stability, command power, transport alternative, and factory commitment.

## Boundary

This is a wording-only repair. It does not admit FORM-39, change gameplay payment, alter the decision category, or claim live tooltip observation. The whole Event 006 implementation remains **HOLD / PARTIAL**.

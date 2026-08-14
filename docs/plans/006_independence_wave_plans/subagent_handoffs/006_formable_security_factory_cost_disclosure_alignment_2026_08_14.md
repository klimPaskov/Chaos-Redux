# FORM-01/02/04 security-factory cost disclosure alignment

Date: 2026-08-14

Scope: narrow selector and localization repair for three admitted formable-family security decisions.

## Change

`independence_wave_form01_coordinate_maritime_defence`, `independence_wave_form02_build_air_warning_chain`, and `independence_wave_form04_coordinate_corridor_security` each reserve the existing light civilian-factory tier while paying the same security-standard resource bundle.

Their selectors now use the dedicated `independence_wave_cost_security_standard_factory` triplet, which preserves the security-standard manpower, Army Experience, infantry-equipment, and support-equipment wording and adds the existing light-factory reservation through the shared decision-cost constant.

The shared `independence_wave_cost_security_standard` triplet was not changed because many non-factory callers use it.

Only the three selectors and the new base, tooltip, and blocked localization keys changed; payment effects, affordability triggers, durations, AI scores, lifecycle guards, and cleanup remain unchanged.

## Validation

The new key has one base entry and complete `_tooltip` and `_blocked` siblings in the UTF-8-BOM Event 006 decision localization.

The three selectors each have exactly one consumer and their modifiers remain `CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`.

The admitted Event 006 allocator and scenario-matrix audits remain unchanged at 149 publishers, 126 automatic publishers, 138 SCN-008 publishers, 40 adapters, 32 attested packages, 29 compatible groups, and 161 unattested rows.

No central adapter, attestation, Join, portrait, flag, workbook, AI, payment, or cleanup surface was changed.

## Deferred surfaces

The admitted COR mountain-post decision uses the distinct security-light resource tier and remains on its own disclosure track; it was intentionally not redirected to this standard-resource key.

Other custom security and package-local callers remain queued where their accepted cost semantics or admission boundary require separate review.

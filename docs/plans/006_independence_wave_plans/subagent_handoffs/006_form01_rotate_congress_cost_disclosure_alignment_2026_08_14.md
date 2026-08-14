# FORM-01 congress-rotation cost disclosure alignment

Date: 2026-08-14

Scope: narrow player-facing cost disclosure repair for `independence_wave_form01_rotate_congress_session`.

## Change

The decision reserves `civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT` while its dedicated `independence_wave_form0124_administrative_diplomatic_cost` triplet previously described only Command Power, manpower, and convoy/train commitments.

The base, tooltip, and blocked strings now disclose the existing light civilian-factory reservation through `constant:independence_wave_decision_cost.civilian_factory_light`.

Only `localisation/english/006_independence_wave_form01_02_04_l_english.yml` changed in this tranche; the decision selector, payment effects, affordability triggers, duration, AI score, lifecycle, and cancellation behavior are unchanged.

## Validation

The custom key remains owned by the single FORM-01 congress-rotation decision and all three required suffixes remain present.

The localization file retains its UTF-8 BOM and the dynamic constant token resolves against the shared Event 006 decision-cost constants.

The accepted Event 006 allocator and scenario-matrix audits remain unchanged at 149 publishers, 126 automatic publishers, 138 SCN-008 publishers, 40 adapters, 32 attested packages, 29 compatible groups, and 161 unattested rows.

No central adapter, attestation, Join, portrait, flag, workbook, AI, payment, or cleanup surface was changed.

## Deferred surfaces

FORM-01 maritime security, FORM-02 air-warning security, and FORM-04 corridor-security callers still require dedicated security-factory wording if their accepted reservations are to be disclosed; the shared security triplet was intentionally not broadened.

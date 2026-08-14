# Event 006 FORM-03 cost disclosure alignment

Date: 2026-08-14

## Disposition

Implemented a dedicated administration-standard/light-factory cost triplet for four accepted FORM-03 language decisions. Each decision already reserves one civilian factory but previously selected the shared administration-standard card, which displays two factories.

## Changes

The following FORM-03 decisions now select `independence_wave_cost_administration_standard_factory`:

- `independence_wave_form03_convene_language_convention`
- `independence_wave_form03_open_multilingual_service_examinations`
- `independence_wave_form03_establish_federal_language_appeals`
- `independence_wave_form03_repair_language_settlement`

The new base, `_tooltip`, and `_blocked` keys show the existing administration-standard command-power/manpower values plus `civilian_factory_light`. The shared two-factory administration-standard triplet remains unchanged for its other callers.

## Boundary

No FORM-03 language model, progression, affordability trigger, payment effect, AI score, duration, cancellation, cleanup, formable membership, admission, Join, or catalog behavior changed. This is a player-facing selector correction only.

## Validation

The localisation file retains its UTF-8 BOM and all three new keys occur once. All four decision blocks resolve to the new selector beside their existing light factory modifier. Allocator and SCN-008 matrix audits remain passing at 40 adapters, 32 attestations, 29 compatible groups, 161 unattested rows, and the 3/4/5/7/10 ladder. No weighted or eligibility surface changed, so no probability compare is meaningful.

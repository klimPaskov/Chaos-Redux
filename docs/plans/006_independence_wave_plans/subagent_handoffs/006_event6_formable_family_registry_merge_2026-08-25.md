# Event 006 formable-family trigger/effect registry merge

Date: 2026-08-25.

This source-layout tranche consolidates the four small formable-family scripted-trigger files and four matching scripted-effect files into the existing Event 006 formable registries.

## Receiver files

- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`

The removed parser files are the FORM-07, FORM-08, FORM-09, and FORM-16 trigger/effect files. Each moved source block is marked by its former path inside the receiver so ownership and review history remain traceable.

## Preservation evidence

- The merged trigger registry contains 86 unique top-level trigger identifiers with zero duplicates.
- The merged effect registry contains 71 unique top-level effect identifiers with zero duplicates.
- Every old trigger and effect source block appears in the receiver after comment/blank-line normalization; the executable code-line sequences are preserved.
- Receiver brace counts are balanced: 571/571 for triggers and 1559/1559 for effects.
- The maintained `.tools/audit_event6_form16.py` contract reader now targets the receiver registries, so the FORM-16 audit follows the consolidated source paths.
- No package adapter, attestation, preflight, deterministic Join, formable identity, territory, consent, integration, cost, localisation, or AI value was changed.

This is source and static evidence only. No live parser, save/load, GUI, or in-game execution claim is made, and the whole Event 006 boundary remains HOLD / PARTIAL.

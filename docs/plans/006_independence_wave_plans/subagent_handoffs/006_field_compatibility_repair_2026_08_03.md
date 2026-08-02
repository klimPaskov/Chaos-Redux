# Event 006 field-compatibility repair — 2026-08-03

## Scope

This tranche repairs the remaining field-compatibility defects found in the dirty Event 006 gameplay surface. It does not claim package admission, in-game rendering, or whole-event completion.

## Gameplay repairs

- The hidden roster events `chaosx.nr6.10` and `chaosx.nr6.350` retain release-time `recruit_character` effects. Event 006 characters are therefore not preloaded through the invalid `history/general/006_independence_wave_character_recruitment.txt` surface; that file is absent from the working tree. Route-conditional CHU, ASY, and SOK roles remain gated by their existing route flags.
- Event 006 AI strategy files retain the original vanilla train strategy semantics. `equipment_production_factor` continues to target `id = train` for priority rules, and `equipment_production_min_factories` continues to target `id = train` for minimum-factory rules. The temporary `train_equipment` archetype conversion is not present.
- File-scoped `@CR_SC_INDEPENDENCE_WAVE_*` constants mirror the authoritative values from `common/script_constants/006_independence_wave*.txt`; this keeps tuning local to each AI file without changing the strategy meaning.

## Localisation repairs

Added the missing category description keys:

- `independence_wave_cat_industrial_compact_category_desc`
- `independence_wave_evolution_incident_category_desc`
- `independence_wave_mnt_mountain_compact_category_desc`

## Validation

- `.tools/audit_event6_allocator.py` passed with the accepted 6 / 8 / 10 / 14 / 20 ladder and World Collapse 20.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `.tools/audit_event6_gui_matrix.py` passed the Statehood Ledger source matrix.
- `.tools/audit_event6_flags.py --strict` passed 102 complete flag triplets and zero incomplete triplets.
- `.tools/audit_chaosx_country_tags.py --surface-scan` passed with zero external country-definition or identity-surface collisions.
- A targeted localisation scan finds all three category description keys.
- A targeted AI scan finds no `equipment_production_min_factories_archetype` or `id = train_equipment` in Event 006 AI strategy files.

## Remaining status

The event remains HOLD/PARTIAL. The current completion evidence still records 14 attested packages, fail-closed 14/20 and 20/20 automatic bands, unresolved source/rights gates, incomplete formable admission, no runtime GUI proof, and the accepted 6001 audio rights blocker.

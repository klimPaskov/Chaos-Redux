# Event 006 SCN-008 Failure-Summary Ledger Repair

Date: 2026-08-02

## Defect

The scenario summary effect could copy the selected package rows into the released ledger whenever the last plan ID and owner matched, even when scenario execution failed or the transaction was rolled back. That made a failed transaction appear as a successful release in the Scenario Details surface.

## Repair

- `independence_wave_scenario_freeze_summary` now requires the explicit `independence_wave_scenario_committed` ownership barrier before appending selected rows to the released ledger.
- Failed or rolled-back plans append their selected rows to the blocked ledger instead and retain `global.independence_wave_scenario_last_failure` as the blocked reason.
- Failed plans do not derive a host count from the liberation plan; the default zero value remains visible.
- Existing rejected package rows and rejection reasons remain preserved in both success and failure summaries.

## Validation

- `python -B .tools/audit_event6_scenario_matrix.py` — 32 SCN-008 cells and 8 edge-case receipts passed, including the commit-gated summary witness.
- `python -B .tools/audit_event6_allocator.py` — allocator, doubled automatic ladder, pre-wave crisis, joint reservation order, and summary ledger checks passed.
- `python -B .tools/audit_chaosx_country_tags.py` — protected Event 006/Soviet tag collision checks passed with zero external country-definition or identity-surface collisions.
- No live game or consumer test was run; this handoff is source/static evidence only.

## Scope boundary

This repair closes the SCN-008 failure-summary semantic defect. It does not promote unattested country packages, add missing super-event rights/audio, complete the wider asset/UI/achievement surfaces, or replace the accepted generic-tree scope with bespoke country trees.

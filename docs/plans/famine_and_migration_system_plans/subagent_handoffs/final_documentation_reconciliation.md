# Final documentation reconciliation

## Scope

This handoff records the final documentation-only reconciliation for the separate famine and migration mechanics. It does not claim gameplay completion.

## Disposition

- Permanent system documentation defines `famine_register_initial_incident` and `migration_register_initial_incident` as accounting and presentation seams only. No famine or migration event object, event ID, event-pool registration, or pacing pulse is part of this system.
- Binding specifications, prompts, matrices, and current authority documents use separate `famine_*` and `migration_*` identifiers. Narrow shared infrastructure remains limited to neutral civilian-transfer and humanitarian contracts.
- Each decision category exposes exactly three player-facing values: Food Security, Food Reserves, and Relief Access for famine; Displacement Load, Reception Capacity, and Border Policy for migration. Internal ledgers and raw component variables are not additional player-facing values.
- The documented asset inventory is 61 DDS files: 50 root-manifest assets, seven report images, and four mapmode button sprites. The category asset closure handoff contains source, processing, round-trip, and provenance evidence.
- The workbook records Event 149 as unavailable and retired into the migration system. No famine or migration incident row, state-pulse row, event-pool registration, or pacing entry was added. All three CSV exports were refreshed from the workbook.
- Probability documentation distinguishes pre-refund structural evidence from the failed final MCP rerun. The final decision hashes are `bb8d664fb7aac3dff93321b2abc25999f8441d5760979d851b041931df4d12a2` for famine and `2bf5664769c0610d03fe8b075fcb284c89b1b919a0ac6855f0e1bfd0742f69fa` for migration.

## Remaining blockers

- Exact proof-owning receipts remain unavailable for generic occupation-law transitions, strategic bombing attribution and amount, country-level war/peace callbacks, generic cluster/scenario dispatch, and verified relief obstruction.
- Event sources 118, 120, and 131 are absent.
- Final typed probability scenarios, custom-pool evaluation, and post-patch comparison remain unavailable because the HOI4 MCP returned internal errors, timeouts, and comparison-schema rejection.
- Dynamic mapmode color, tooltip, and click-region execution remains outside the evidence returned by the available map/GUI routes.
- Live in-game consumer validation remains user-owned.

## Files reconciled

- `docs/specs/famine_and_migration_system_specs/`
- `docs/systems/famine_system.md`
- `docs/systems/migration_system.md`
- `docs/systems/civilian_transfer_system.md`
- `docs/plans/famine_and_migration_system_plans/completion_report.md`
- `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md`
- `docs/plans/famine_and_migration_system_plans/handoff_dispositions.md`


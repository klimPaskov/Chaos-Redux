# Event 016 manifest status reconciliation

Date: 2026-08-03

## Scope

This handoff records a documentation-only reconciliation of `docs/assets/016_brilliant_scientist/manifest.md`. No gameplay, localisation, GFX, asset binary, spreadsheet, checksum, or 3D-model file was edited. The current no-model boundary remains authoritative.

## Files changed

- `docs/assets/016_brilliant_scientist/manifest.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_manifest_status_reconciliation_2026-08-03.md`

## Reconciled status

- The five binding severe portrait families now point to their produced source and processed frame sets, runtime sheets, static fallback DDS files, package-record entries, contact sheets, previews, and registered `interface/016_brilliant_scientist.gfx` animated sprites.
- The xenobiological-or-alien family is explicitly recorded as two evidence-gated runtime sheets, xenobiological and alien-revealed, so the five-family binding count and six-sheet runtime count no longer conflict.
- The old `Missing` cells were removed without changing any asset binary or runtime wiring. The package record currently resolves all listed severe-package paths in the working tree.
- The old broader-presentation blocker was replaced with the current open gates: the native CBRN callback dependency, quantitative/targeted/live acceptance, unresolved durable portrait-queue ownership, external source-rights uncertainty, and the no-model/deferred or closed-filler boundary.
- Seven 3D entity packages are documented as deferred outside the current no-model scope, not as a blocker or acceptance gate. Broader country chains and additional report-card expansion are documented as closed or rejected as filler under the named closure handoff.

## Validation

- Parsed `docs/assets/016_brilliant_scientist/package_records/portrait_animation_package.json`: 20 package entries, including six `animated_leader` route entries.
- Checked every unique source, processed frame, sheet, runtime DDS, static fallback DDS, preview, and contact-sheet path named by that package record: 194 paths resolve in the current workspace.
- Confirmed the six runtime frame-sheet DDS paths and six static fallback DDS paths are present, and confirmed the six animated sprite registrations in `interface/016_brilliant_scientist.gfx` by route name and texture path.
- Confirmed the working tree still reports fifteen deleted tracked PNGs under `docs/assets/portraits/016_brilliant_scientist/`; those files were not restored or staged because their ownership belongs to another concurrent task.
- Ran `git diff --check` on the manifest edit.

## Open risks and limits

- The path/existence audit does not decode or visually inspect binary DDS/GIF/PNG content and does not claim live GUI animation, state-selection, audio, or super-event acceptance.
- Runtime leader DDS and the Event 016 processed portrait package remain present despite the durable source-queue deletions; parent review must decide whether to restore or otherwise resolve that queue before relying on regeneration provenance.
- This reconciliation does not make a whole-event completion claim and does not reopen CBRN implementation, 3D production, or broader filler content.

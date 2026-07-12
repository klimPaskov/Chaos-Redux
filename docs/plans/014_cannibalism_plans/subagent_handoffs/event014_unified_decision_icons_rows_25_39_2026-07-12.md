# Event 014 Unified Decision Icons — Rows 25–39 Handoff

## Outcome

Completed the final fifteen unified-decision icons covering the naval hunt, convoy harvest, silent anchorage, air interdiction, war-machine mission, cell and global-campaign operations, counterwar, and terminal mobilization decisions. Each icon has its own built-in image-generation source, transparent processed PNG, package DDS, and live DDS at the pre-registered path.

## Deliverables

- Asset manifest: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/manifest_rows_25_39.md`
- GFX handoff: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/gfx_handoff_rows_25_39.md`
- Prompt ledger: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/prompts/icon_prompt_ledger_rows_25_39.json`
- Validation ledger: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/validation/icon_validation_rows_25_39.tsv`
- Validation summary: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/validation/validation_report_rows_25_39.json`
- Source, processed, and decoded-DDS contact sheets: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/contact_sheets/unified_decisions_rows_25_39_*_contact.png`
- Reproducible processor: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/_tooling/process_rows_25_39.py`
- Runtime textures: `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_*.dds` for rows 25–39 in the authoritative manifest.

## Validation evidence

- Coverage is 15/15 at the source, processed PNG, package DDS, and live DDS layers.
- Source, processed, and runtime hashes are unique across the assigned tranche.
- Every processed icon has transparent corners and every decoded DDS is pixel-identical to its processed PNG.
- All fifteen `GFX_decision_cannibalism_unified_*` registrations resolve to their exact live texture paths.
- The parent integration scan found zero missing texture paths across all Event 014 `.gfx` files after this tranche landed.
- The three contact sheets were reviewed for native-size readability and subject distinction.

## Simplifications, omissions, and blockers

None. No existing icon, cross-type asset, placeholder, transform-only substitute, default art, or unapproved fallback was used. No gameplay, localisation, `.gfx`, `.gui`, spec, or spreadsheet file was changed by this asset tranche.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`


# Event 015 Ledger Value and Calling Icon Repair Manifest

## Scope

This bounded package promotes the preserved built-in ImageGen 5x2 Ledger icon atlas into four compact Value icons and six Calling icons. It owns source-cell evidence, keyed intermediates, transparent processed PNGs, package DDS copies, runtime DDS files, decoded verification PNGs, contact sheets, checksums, processing records, and the GFX handoff.

It does not edit `.gfx`, `.gui`, scripted GUI, gameplay, localisation, or top-level Event 015 authority documents.

## Source and provenance

- Source mode: frozen built-in ImageGen atlas.
- Source atlas: `docs/assets/015_utopia_manifesto/source_png/identity_gui/utopia_ledger_value_calling_icons_imagegen_atlas.png`.
- Source dimensions: `1774x887`, RGB, five columns by two rows.
- Source SHA-256: `7a1704f1c6d720ff72b9cdc3715101361bb8b836033607d0ff244dbb31c7d440`.
- Machine-readable cell evidence: `source_records.json`.
- Accepted design authority: Event 015 Part 8, `asset_manifest_plan.md`, the 2026-07-16 requirement-to-runtime crosswalk, and the current Event 015 asset/GFX handoffs.

The repository preserved the atlas and explicitly described it as ImageGen provenance, but it did not preserve the verbatim original generation prompt. This package does not invent a prompt and present it as exact. Visual inspection verifies the accepted semantic sequence: Need, Plenty, Concord, Choice versus Assignment, Provisioning, Workshops, Civic Works, Learning and Care, Maritime and Settlement, and Defense and Watches.

## Processing contract

- The atlas hash and dimensions are pinned by `_tooling/process_value_calling_icons.py`.
- Each atlas cell is preserved as its own raw source PNG and hash record.
- Magenta-key removal uses the installed ImageGen helper with border sampling, a soft matte, thresholds `12` and `220`, and despill.
- The retained art is alpha-fitted with premultiplied Lanczos resampling and a one-pixel minimum canvas margin.
- No visible emblem, object, frame, symbol, line, or texture is drawn, traced, recoloured, reconstructed, or simplified locally.
- The script writes the same one-level uncompressed 32-bit BGRA DDS header layout as `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

## Asset inventory

| Asset | Cell | Type | Native size | Sprite | Runtime DDS | Runtime SHA-256 | Status |
| --- | ---: | --- | ---: | --- | --- | --- | --- |
| Need | r0 c0 | Value icon | 32x32 | `GFX_utopia_ledger_value_need` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_need.dds` | `3deac3e59e2034adabcc4321cf1e76d62b54ee1d7a43ff4568934820fadfd3a5` | handed_off |
| Plenty | r0 c1 | Value icon | 32x32 | `GFX_utopia_ledger_value_plenty` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_plenty.dds` | `5f4f728a3b6e46db159b506cda4e8043188e0de59ecddaa3459be73fd35172d7` | handed_off |
| Concord | r0 c2 | Value icon | 32x32 | `GFX_utopia_ledger_value_concord` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_concord.dds` | `a0ad32201336a34f25c317c8b0ed1e1d76e475ab0a6cd07caef51d3491153727` | handed_off |
| Choice / Assignment | r0 c3 | Value icon | 32x32 | `GFX_utopia_ledger_value_balance` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_value_balance.dds` | `d7b722a88b9336e4db6e7ed646b283345367a216fb08acd8c6fbbe1d753d0b14` | handed_off |
| Provisioning / Agriculture | r0 c4 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_provisioning` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_provisioning.dds` | `85e4a654db25ba8e77054221d2e986de170e2b1ac573035ac250bcc7c67880ac` | handed_off |
| Workshops / Arsenal | r1 c0 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_workshops` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_workshops.dds` | `744b102559feb6da82a4cae98b5b9bbea34b303baab7ea270814aef823770001` | handed_off |
| Civic Works / Transport | r1 c1 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_civic_works` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_civic_works.dds` | `2b2095e7ba4f9a6bc0f10e6f04c53c4d72e71798fd6d68f67950e8cc46db5758` | handed_off |
| Learning / Care | r1 c2 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_learning_and_care` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_learning_and_care.dds` | `119a3a6179c0a13cf701a6e229cba2dc389570b2eb3d0caf1bb70a8ef5b7fa66` | handed_off |
| Maritime / Settlement | r1 c3 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_maritime_and_settlement` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_maritime_and_settlement.dds` | `06c7ccb4d8814fae82a9d3fd955260f850d7937b1af973e9ff504d432bd4fa9a` | handed_off |
| Defense / Watches | r1 c4 | Calling icon | 48x48 | `GFX_utopia_ledger_calling_defense_and_watches` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_calling_defense_and_watches.dds` | `5c7007769e0b7f841c139a8f1b1c2374773f5c3d900d31a1d5104012202af0f4` | handed_off |

Each runtime file has a byte-identical package copy under `dds/`, a source-cell PNG under `source_cells/`, a keyed evidence PNG under `keyed_cells/`, a final alpha PNG under `processed_png/`, and a pixel-identical DDS decode under `decoded_png/`.

## Visual review

- `contact_sheets/source_cells_contact_sheet.png` preserves the atlas cell order and visible ImageGen source art.
- `contact_sheets/processed_alpha_contact_sheet.png` shows the ten native processed files enlarged with nearest-neighbour sampling over a checkerboard.
- `contact_sheets/dds_decoded_contact_sheet.png` shows the ten runtime DDS decodes with the same review treatment.
- Choice versus Assignment remains morally neutral: the divided emblem gives equal visual weight to an open hand and branching choice on one side and measuring instruments and records on the other. It contains no approving, condemning, heroic, punitive, red-versus-green, or text label cue.

## Validation authority

- `validation.json` contains per-asset alpha, DDS header, exact-length, decoded-pixel, package/runtime equality, hash, and distinctness evidence.
- `checksums.sha256` covers the frozen atlas, retained processor, package evidence, documentation, and all ten runtime files.
- `processing_validation_report.md` records the human review and native-size rationale.
- `gfx_handoff.md` gives the parent agent the stable consumer mapping.

## Status and limitations

All ten source cells and all ten runtime assets are present, distinct, transparent, decoded, and handed off. The original verbatim ImageGen prompt is absent from the repository and is recorded honestly as unavailable; the generated atlas itself, its pinned hash, its explicit prior provenance references, and ten cell records remain intact.

No alternate source, placeholder, primitive redraw, resized focus icon, or unrelated decision icon was used.

# Event 014 Remaining Registered Icons Handoff — 2026-07-12

## Outcome

Completed the frozen remaining-registered-icons tranche for Event 014: 68 distinct generated sources, 68 final processed textures, and 68 runtime DDS files.

| Family | Count | Runtime folder | Contract |
| --- | ---: | --- | --- |
| Decision-category panels | 9 | `gfx/interface/decisions/014_cannibalism/` | 114x101, fully opaque |
| Decision-category icons | 9 | `gfx/interface/decisions/014_cannibalism/` | 32x32, true alpha |
| Decision icons | 23 | `gfx/interface/decisions/014_cannibalism/` | 32x32, true alpha |
| Idea/dynamic-modifier icons | 27 | `gfx/interface/ideas/014_cannibalism/` | 64x64, true alpha |
| **Total** | **68** | **41 decision + 27 idea DDS** | **Exact frozen ledger coverage** |

Reports and news images were deliberately excluded because they are outside the assigned tranche.

## Files produced

- Complete evidence package: `docs/assets/014_cannibalism/remaining_registered_icons_imagegen/`
  - `manifest.md`: exact 68-row source/processed/package/runtime/sprite matrix.
  - `prompts/remaining_registered_icons_prompts.md`: all 75 imagegen calls, including accepted and rejected attempt IDs, default output paths, preserved source paths, full prompts, and rejection reasons.
  - `process_remaining_registered_icons.py`: reproducible alpha processing, fitting, DDS conversion, GFX-path audit, decoded-pixel audit, validation output, and contact-sheet generation.
  - `source_png/`: 68 accepted direct generated sources.
  - `source_png/rejected/`: seven preserved first attempts rejected for unintended red-cross emblems.
  - `alpha_png/`: 59 keyed alpha intermediates.
  - `processed_png/`: 68 final target-size PNGs.
  - `dds/`: 68 frozen package DDS files.
  - `contact_sheets/`: source, processed/checkerboard, and decoded-DDS/checkerboard sheets for each of the four asset families.
  - `validation/remaining_registered_icons_validation.tsv`: per-asset technical and registry evidence.
  - `validation/validation_summary.md`: tranche-level validation result.
- Runtime DDS:
  - 41 files under `gfx/interface/decisions/014_cannibalism/`.
  - 27 files under `gfx/interface/ideas/014_cannibalism/`.
- This handoff: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_remaining_registered_icons_2026-07-12.md`.

No gameplay script, localisation, GFX registry, GUI, focus, achievement, event, decision, idea, or spreadsheet file was edited.

## Generation and review record

Every accepted source was produced by a distinct built-in image-generation call. There were no CLI image-model calls, moderation blocks, sourced-photo substitutions, or fallback images.

Visual review found an unintended real-world red-cross emblem in seven first attempts:

1. `cannibalism_wendigo_counterwar_category_panel`
2. `decision_cannibalism_joint_suppression_operation`
3. `decision_cannibalism_land_against_island_host`
4. `decision_cannibalism_rebuild_feeding_state_institutions`
5. `decision_cannibalism_rescue_island_survivors`
6. `idea_cannibalism_island_host_landing_pressure`
7. `idea_cannibalism_wendigo_broken_anchor_recovery`

Those attempts were rejected, preserved as evidence, and regenerated with stricter no-emblem constraints. Final native-size and enlarged contact-sheet review found the four families readable, crop-safe, semantically distinct, free of readable text and real-world insignia, and consistent with the Event 014 1930s–1940s material language.

## Runtime and registry evidence

- The 68 runtime paths each have exactly one matching `spriteType` registration in `interface/014_cannibalism.gfx`.
- Registered sprite names are `GFX_<asset_name>`, and the registered texture paths match the runtime DDS paths exactly.
- Package DDS and runtime DDS hashes are identical for all 68 assets.
- Runtime DDS decoding is pixel-identical to each corresponding processed PNG.
- Panels are exactly 114x101 with alpha 255 throughout.
- Transparent icons are exactly 32x32 or 64x64, retain both transparent and fully opaque pixels, and have zero-alpha corners.
- Generated-source hashes and normalized final-RGBA hashes are unique across all 68 assets.
- No visible chroma-key green remains.

The DDS backend is the parent-approved Microsoft DirectXTex converter, version 2026.5.8.1:

- Path: `C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe`
- Authenticode: valid Microsoft signature
- SHA-256: `DCFDEC10244E02CF5037FBA089C55FB7E1326B1C8181742D77D15FA5CB5EEF06`

The processor pins that exact executable and did not use an alternate conversion fallback.

## Ownership and git

The work stayed inside the assigned evidence package, the two assigned runtime texture folders, and this handoff. No commit was created, as required by the parent task.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- `imagegen`

No skill was created or updated; this tranche did not reveal a reusable workflow gap outside the existing skill guidance.

## Simplifications, omissions, and blockers

None. All 68 assigned assets were individually generated, processed, wired to their pre-existing registered paths, documented, and validated. No asset was shared, substituted, omitted, left unwired, or completed with a fallback.


# Event 014 Warlord Asset Completion Handoff

## Ownership and scope

This was an asset-only completion pass. It did not edit gameplay, localisation, GUI, `.gfx`, or `.gui` files and did not create a commit. Sprite registration remains with the parent implementation owner.

The completed scope is:

- all 72 static warlord-route focus icons from `common/national_focus/014_cannibalism_warlord_focus.txt`;
- all 34 missing pre-reveal/warlord command textures identified in `interface/014_cannibalism.gfx` (two category icons, two category pictures, 18 decision icons, and 12 idea icons);
- `report_event_cannibalism_public_reveal` and `report_event_cannibalism_warlord_submission` for `interface/chaosx_pictures.gfx`.

The pass explicitly excludes Hannibal, the Wendigo, the Hannibal portrait, and `idea_cannibalism_unified_command_burden`. Those surfaces belong to the unified/reveal asset owner. The public-reveal report is the only completed asset that depicts the fictional revealed commander; the submission report keeps the receiving commander off camera, and all other completed artwork remains commander-free.

## Deliverables

### Warlord focus package

- Package root: `docs/assets/014_cannibalism/warlord_focus_icons_imagegen/`
- Complete inventory and provenance: `manifest.md`
- Exact 72-sprite registration table: `gfx_handoff.md`
- Prompt ledger: `prompts/focus_icon_prompt_ledger.json`
- Reproducible processor: `process_warlord_focus_icons.py`
- Sources: 72 PNGs under `source_png/`
- Alpha intermediates: 72 PNGs under `alpha_png/`
- Processed 94×86 PNGs: 72 under `processed_png/`
- Package DDS copies: 72 under `dds/`
- Live DDS files: 72 under `gfx/interface/goals/014_cannibalism/`
- Validation ledger: `validation/warlord_focus_icon_validation.tsv`
- Source, processed-checker, and decoded-DDS sheets: `contact_sheets/`

Seventy focus sources were generated during this pass. Two existing imagegen sources—`goal_cannibalism_warlord_assign_feeding_districts_source.png` and `goal_cannibalism_warlord_battlefield_harvest_source.png`—were preserved and fully processed; their reconstructed prompt records are marked in the ledger. Seven moderation-rejected end-route prompts were safely rephrased, regenerated as distinct art, and recorded in the prompt ledger.

### Warlord command/report package

- Package root: `docs/assets/014_cannibalism/warlord_command_assets_imagegen/`
- Complete 36-asset inventory and provenance: `manifest.md`
- Exact GFX registration table: `gfx_handoff.md`
- Prompt and retry ledger: `prompts/warlord_command_prompt_ledger.json`
- Reproducible processor: `process_warlord_command_assets.py`
- Sources: 36 PNGs under `source_png/`
- Alpha intermediates: 32 PNGs for transparent icon surfaces under `alpha_png/`
- Processed PNGs: 36 under `processed_png/`
- Package DDS copies: 36 under `dds/`
- Live decision/category DDS files: `gfx/interface/decisions/014_cannibalism/`
- Live idea DDS files: `gfx/interface/ideas/014_cannibalism/`
- Live report-event DDS files: `gfx/event_pictures/014_cannibalism/`
- Validation ledger: `validation/warlord_command_asset_validation.tsv`
- Combined and type-specific contact sheets: `contact_sheets/`

The command-category panel's initial imagegen output was moderation-rejected; the documented retry uses a neutral wartime logistics-room composition and produced the required distinct 114×101 category picture. The two report sources use documentary-safe staging. The public-reveal source received a final imagegen edit so its fictional commander matches the localisation's bald, scarred description and uses unmarked fictional tabs instead of recognizable insignia. Both reports were processed with the repository report-event tool into tilted, monochrome/sepia, transparent 210×176 cards.

## Registration handoff

- Register all 72 focus sprites from `warlord_focus_icons_imagegen/gfx_handoff.md` in `interface/014_cannibalism.gfx`.
- Register the 34 non-report command sprites from `warlord_command_assets_imagegen/gfx_handoff.md` in `interface/014_cannibalism.gfx`.
- Register `GFX_report_event_cannibalism_public_reveal` and `GFX_report_event_cannibalism_warlord_submission` from that same handoff in `interface/chaosx_pictures.gfx`.
- Every registration is static with `noOfFrames = 1`; no animation or frame-sheet handoff is applicable.

## Validation evidence

- The focus-tree audit found 72 actual `cannibalism_warlord_*` focus IDs (excluding the focus-tree container ID), 72 ledger icons, zero missing icons, and zero extras.
- File coverage is complete: 72/72 focus sources, processed PNGs, package DDS files, and live DDS files; 36/36 command/report sources, processed PNGs, package DDS files, and live DDS files.
- Every focus DDS is 94×86. Decision/category icons are 32×32, category pictures are 114×101, idea icons are 64×64, and report cards are 210×176.
- All DDS headers report BGRA8 channel masks with one mip. Transparent icon and report surfaces retain alpha; category pictures remain opaque.
- Chroma-key residue checks found zero visible key-green pixels in every transparent surface.
- Normalized RGBA hashes are unique across each package; no generated icon is a byte-identical reuse of another texture.
- The first command validation detected a 3/255 corner-shadow residue on one 32×32 icon. The processor now clears the one-pixel outer alpha perimeter on all small transparent icons, and the complete 36-asset validation rerun passed.
- Visual review of the processed and decoded-DDS contact sheets found no crop failures, empty outputs, commander leakage, or unreadable focus silhouettes. The report cards preserve their intended reveal/off-camera distinction.

## Simplifications, omissions, and blockers

No simplifications, fallback art, placeholder textures, duplicated textures, or blockers remain within the assigned asset scope. GFX registration is intentionally not included because this subtask expressly forbade GFX edits and assigned registration to the parent implementation owner.

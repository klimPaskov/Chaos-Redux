# Event 006 northern/western Europe advisor dossier handoff

Date: `2026-07-15`
Subtask: bounded fictional advisor-dossier asset tranche for RHI, BAY, SCO, and WLS
Role boundary: generated non-icon asset production only; no gameplay, localisation, `.gfx`, GUI, event, focus, idea, decision, history, country-package, or spreadsheet edits

## Outcome

The requested twelve-advisor tranche is produced and installed. Each advisor has:

- one independent official ImageGen full-resolution fictional portrait master;
- one explicit, per-source head-and-shoulders crop recorded in metadata;
- one separately composed native `65x67` advisor dossier PNG from `.tools/process_hoi4_portrait.py advisor`;
- one valid exact-stem runtime DDS under `gfx/interface/ideas/006_independence_wave/advisors/`;
- one package DDS mirror and decoded verification PNG;
- processor comparison evidence, all-three-canonical comparison evidence, native and enlarged-nearest review, prompts, manifest, hashes, and visual notes.

The corrected advisor contract was followed exactly: these are separate `65x67` dossier cards. No leader portrait was created, shrunk, padded, repurposed, or used as a substitute.

All twelve assets are disclosed fictional people. Apparent gender presentation is explicit in per-asset and consolidated metadata: six male-presenting and six female-presenting. Later generated-character names must use the matching gender pool.

## Exact stems delivered

### RHI

- `advisor_RHI_independence_wave_municipal_customs_administrator`
- `advisor_RHI_independence_wave_rail_works_liaison`
- `advisor_RHI_independence_wave_river_defense_planner`

### BAY

- `advisor_BAY_independence_wave_district_finance_administrator`
- `advisor_BAY_independence_wave_estates_constitutional_liaison`
- `advisor_BAY_independence_wave_alpine_supply_inspector`

### SCO

- `advisor_SCO_independence_wave_shipping_authority_commissioner`
- `advisor_SCO_independence_wave_industrial_reconstruction_secretary`
- `advisor_SCO_independence_wave_territorial_defense_planner`

### WLS

- `advisor_WLS_independence_wave_bilingual_civil_service_commissioner`
- `advisor_WLS_independence_wave_coal_rail_organizer`
- `advisor_WLS_independence_wave_mountain_defense_planner`

## Files created

Asset package root:

- `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/`

Package contents:

- `source_png/imagegen_raw/` - twelve raw full-resolution ImageGen PNG masters
- `processed_png/advisors/` - twelve approved native `65x67` dossier PNGs
- `final_dds/advisors/` - twelve byte-identical package DDS mirrors
- `decoded_png/advisors/` - twelve DDS decode-verification PNGs
- `metadata/crops/` - twelve processor/crop/gender/source/review metadata records
- `metadata/advisor_identity_and_crop_metadata.json` - consolidated identity and crop ledger
- `prompts/advisor_prompts.md` - shared prompt contract and twelve independent role briefs
- `contact_sheets/advisor_sources_contact_sheet.png`
- `contact_sheets/advisor_portraits_native_contact_sheet.png`
- `contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- `contact_sheets/advisor_reviews/` - twelve mandated processor comparisons
- `contact_sheets/canonical_all_three/` - twelve per-asset comparisons against all three canonical advisor references
- `manifest.md`
- `visual_review_notes.md`
- `gfx_handoff.md`
- `advisor_validation_2026_07_15.json`
- `checksums.sha256`

Installed runtime assets:

- `gfx/interface/ideas/006_independence_wave/advisors/*.dds` - twelve exact-stem DDS files

This handoff file is the only file created outside the asset and runtime-asset folders.

## Crop and composition evidence

The manifest and consolidated metadata carry every source dimension and crop rectangle. Per-asset JSON files were written directly by `.tools/process_hoi4_portrait.py advisor` and then enriched with fictional disclosure, apparent gender presentation, role, ImageGen mode, canonical-reference paths, final DDS paths, and visual approval status.

Every final metadata record says the card was made by an independent explicit crop from its full ImageGen master and the advisor processor. The records explicitly reject the leader-resize interpretation.

## Visual review

All twelve source masters were inspected before processing. They are subdued, period-appropriate painted portraits with quiet institutional backgrounds and no generated text, logos, flags, medals, watermarks, dossier frames, or modern elements.

All twelve processed finals were inspected:

- at native `65x67` size;
- at 5x nearest-neighbour enlargement;
- through the processor's source/candidate/reference sheet;
- in a separate per-asset sheet beside `generic_europe_1.png`, `generic_female_europe.png`, and `generic_asia_1.png`;
- after DDS decode.

The set passed face readability, crop, silhouette, dossier-frame, paper-overlay, transparent-corner, subdued-palette, and distinctness review. No final was accepted as a generic fallback. No regeneration was necessary because all twelve selected masters met the required style and crop quality.

## Meaningful validation

`advisor_validation_2026_07_15.json` records per-asset hashes and validation facts. The final state is:

- `12/12` raw ImageGen source hashes unique;
- `12/12` processed PNG hashes unique;
- processed and decoded dimensions `65x67` for all assets;
- runtime and package DDS copies byte-identical for all assets;
- decoded DDS pixels identical to the approved processed PNG for all assets;
- each DDS length `17,548` bytes (`128 + 65 * 67 * 4`);
- header size `124`, pitch `260`, pixel-format size `32`, flags `65`, FourCC `0`, bit count `32`;
- masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`;
- caps `0x00001000`, no mipmaps, alpha range `0..255`.

## Parent integration handoff

The existing character file already uses the twelve exact handles:

- `common/characters/006_independence_wave_nwe_advisors.txt`

The parent integrated the ready sprite definitions from:

- `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/gfx_handoff.md`

into the dedicated:

- `interface/006_independence_wave_nwe_advisors.gfx`

The handoff preserves every existing character token and exact `GFX_portrait_advisor_<stem-without-leading-advisor-duplication>` handle. No gameplay or localisation change is required from the asset tranche itself.

## Shared-worktree and ownership note

The worktree contained extensive concurrent Event 006 and unrelated changes. This subtask created only the files listed above and did not modify any gameplay, localisation, `.gfx`, character, country-package, or spreadsheet file. No commit was created; the parent owns final integration and the Event 006 commit.

## Skills and references used

- `chaos-redux-event-assets` - fictional portrait source mode, canonical reference review, independent advisor crop, processor, DDS, manifest, contact-sheet, and handoff requirements
- `chaos-redux-subagents` - bounded asset ownership and parent-owned `.gfx` integration
- official `imagegen` skill - one built-in ImageGen call per fictional portrait master, reference-input handling, project-bound source preservation, and prompt recording
- offline Paradox wiki core pages plus Graphical Asset Modding and Portrait Modding
- vanilla `interface/ideas.gfx` and the three cataloged vanilla advisor DDS precedents

No skill was created or updated; the existing skills already described this reusable workflow.

## Simplifications, omissions, fallbacks, blockers, and residual risks

- Simplifications: none.
- Missing dossiers: none.
- Reused leader portraits: none.
- Transform-only fake styling: none.
- Generic fallback art: none.
- Missing prompts, crop metadata, manifests, hashes, contact sheets, review notes, PNGs, or DDS files: none.
- Asset blockers: none.
- Parent integration complete: the twelve supplied sprite definitions are registered in `interface/006_independence_wave_nwe_advisors.gfx`.
- Commit: intentionally not created, as requested.

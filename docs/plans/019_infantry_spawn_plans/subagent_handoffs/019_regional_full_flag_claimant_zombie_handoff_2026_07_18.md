# Event 019 claimant/zombie regional full-flag raw-source handoff

> **Raw-tranche status (2026-07-18):** This handoff remains valid as source
> evidence for its 35-row raw tranche, but its raw-only boundary is historical.
> The later 7/18 postprocess adds the 91-row spot-master, native PNG, and
> runtime-TGA chain. Visual/runtime rows pass, and the independent remediation
> re-audit handoff
> `019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md` is PASS,
> clearing the regional asset gate for parent-owned package promotion. The
> machine JSON retains its immutable literal
> `candidate_requires_independent_visual_review` processor-state value. Parent
> workbook/catalog reconciliation and export are complete, Event 19 and SCN-013
> now read `Fully Functional`, and package inventory and final completion audit
> are PASS-complete. No closure gate remains. Current package status is owned by
> the manifest and final audit handoff.

Date: 2026-07-18

## Ownership and outcome

This handoff covers only the 35 Event 019 regional raw full-flag masters for CLAIMANT_BREAKAWAY, ZOMBIE_BASE, ZOMBIE_CLAIMANT, ZOMBIE_COLLECTIVE, and ZOMBIE_SPECIES crossed with EUROPE, MIDDLE_EAST, AFRICA, ASIA, AUSTRALIA, NORTH_AMERICA, and SOUTH_AMERICA.

Outcome: 35/35 rows copied byte-for-byte from the existing built-in ImageGen candidate batch into the owned raw directory. 0 rows regenerated, 0 rows missing, and 0 source bytes modified. All five identities and all seven regions are covered exactly once per Cartesian row.

These raws are eligible source evidence under the Event 19-only approved deterministic spot-colour flattening/normalisation exception. They are not final processed flags and must not be wired directly to runtime.

## Files changed

- 35 source PNGs under docs/assets/019_infantry_spawn/source_png/flags/regional_full_flag_raw/claimant_zombie/; filenames are INFANTRY_SPAWN_<IDENTITY>_<REGION>_imagegen_raw.png.
- docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_claimant_zombie_raw_contact_sheet.png (2520x1250, SHA-256 E2D731418D9269080BA5E669BBFFA80DA87D2FCE383F33EC930EC819820B2DF9).
- docs/assets/019_infantry_spawn/prompts/regional_full_flag_claimant_zombie_prompts_2026_07_18.md.
- docs/assets/019_infantry_spawn/notes/regional_full_flag_claimant_zombie_provenance_2026_07_18.md.
- This handoff: docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_claimant_zombie_handoff_2026_07_18.md.

## Source and visual evidence

- Source mode: built-in ImageGen; every row retains its own distinct result handle and generated-images path in the provenance note.
- The raw candidates were the prior batch's only-tonal-falloff rejects. The approved Event 19 pass may flatten them later, but this tranche retains the originals exactly.
- Identity and regional motif contracts are recorded in the owned prompt note and per-row visual survival notes in the provenance note.
- All 35 images were inspected in the owned contact sheet, with full-resolution spot checks of claimant-Europe, zombie-base Middle East, zombie-claimant Middle East, zombie-collective Asia, and zombie-species South America.
- No source showed fabric, folds, poles, scenery, people, faces, text, perspective, watermark, or a missing full-bleed flag field in review. Small-size readability remains pending the normalization pass.

## Validation

- Exact row count: 35.
- Expected identities: 5; expected regions: 7.
- Owned raw files present: 35.
- Missing rows: 0.
- Regenerated rows: 0.
- Owned raw SHA-256 values: 35/35 match the blocker handoff table.
- Built-in result paths: 35/35 found; all 35 hashes match the owned raw files.
- Raw image modes: 35 RGB.
- Raw source dimensions: all positive full-colour masters; dimensions are recorded per row in the provenance note.
- Contact sheet contains all 35 rows and is review-only.

## Deliberate non-deliverables and remaining risks

- No processed PNG previews, normal/medium/small runtime TGAs, DDS files, runtime flag files, main manifest rows, registry files, or .gfx files were created or changed; those are outside this raw-source tranche.
- Consequently there is no final DDS path or sprite handoff to wire yet. A later owner must apply the approved deterministic normalization pass, export 82x52, 41x26, and 10x7 runtime flags, validate orientation and small-size survival, convert if the runtime surface requires DDS, and update the main manifest/GFX surfaces.
- Tonal falloff remains in each unmodified raw by design and is the only inherited rejection condition. Do not treat this handoff or its contact sheet as final visual approval.
- No fallback, recolour-only substitute, monochrome substitute, or locally drawn flag was used.

# Event 014 unified decision icons rows 01-09 handoff

## Scope completed

Completed the deterministic rows 01-09 subset of the registered Event 014 unified-decision icon package:

1. `cannibalism_unified_absorb_warlord`
2. `cannibalism_unified_appoint_governor`
3. `cannibalism_unified_purge_rival`
4. `cannibalism_unified_issue_continental_command`
5. `cannibalism_unified_command_mission`
6. `cannibalism_unified_centralize_larder`
7. `cannibalism_unified_convert_captured_workshop`
8. `cannibalism_unified_abandon_exhausted_frontier`
9. `cannibalism_unified_designate_feeding_capital`

Each decision has its own built-in image-generation call, selected source PNG, keyed alpha PNG, processed transparent 32x32 PNG, package DDS, and exact live DDS. No existing icon, focus art, idea art, category art, crop, or placeholder was reused.

## Files changed

- New package content under `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/`:
  - nine selected files in `source_png/`
  - nine keyed files in `alpha_png/`
  - nine final previews in `processed_png/`
  - nine package copies in `dds/`
  - source, processed-checker, and decoded-DDS contact sheets in `contact_sheets/`
  - `prompts/icon_briefs_rows_01_09.tsv`
  - `prompts/icon_prompt_ledger_rows_01_09.json`
  - `manifest_rows_01_09.md`
  - `gfx_handoff_rows_01_09.md`
  - `validation/icon_validation_rows_01_09.tsv`
  - `validation/validation_report_rows_01_09.json`
  - `_tooling/process_rows_01_09.py`
- Nine exact runtime files under `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_*.dds`, limited to the ids above.
- This handoff.

The master `prompts/icon_briefs.tsv` and `prompts/common_prompt.md` were created before the parent split the original 39-icon job. The retired fourth-origin icon is no longer live, leaving 38 current icons. This handoff claims generated and finalized work only for the nine retained rows 01-09.

## Before and after

Before this tranche, the nine live `GFX_decision_cannibalism_unified_*` definitions pointed to missing DDS paths. They now resolve to visually distinct, period-prop horror icons matching the decisions' localisation and mechanics: command absorption, appointed administration, rival purge, field orders, command-chain timetable, centralized storage, workshop conversion, frontier abandonment, and feeding-capital designation.

No gameplay, localisation, decision, GUI, GFX, focus, event, spreadsheet, skill, or shared event-document file was edited.

## Visual QA and regeneration

- `purge_rival` was regenerated to remove an introduced insignia.
- `command_mission` was regenerated to remove a skull and marked dial detail.
- `designate_feeding_capital` was regenerated to remove a horned skull.
- The selected nine sources contain no real-person likeness, readable text, logo, living Indigenous motif, sacred borrowing, contemporary object, or ancient/classical-general imagery.
- No moderation block occurred.

## Meaningful validation

`validation/validation_report_rows_01_09.json` records:

- 9/9 source PNGs, 9/9 processed PNGs, 9/9 package DDS files, and 9/9 live DDS files
- nine unique source hashes, nine unique processed hashes, and nine unique runtime DDS hashes
- exact 32x32 processed and decoded dimensions
- transparent corners and no visible chroma-key residue
- exact one-level uncompressed BGRA 8.8.8.8 DDS layout at 4,224 bytes per file
- pixel-identical processed-PNG versus decoded-DDS RGBA data
- zero missing or mismatched registered texture paths for rows 01-09

The decoded DDS contact sheet was visually inspected and matches the processed contact sheet.

## Remaining integration boundary

Rows 10-39 were reassigned and are outside this handoff. The parent must run the global 39-file count, uniqueness, contact-sheet, and zero-missing-path audit after all deterministic subsets are merged. No simplification or omission exists inside rows 01-09.

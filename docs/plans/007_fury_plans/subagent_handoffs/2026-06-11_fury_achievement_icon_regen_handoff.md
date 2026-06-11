# Fury Achievement Icon Regeneration Handoff

- Date: `2026-06-11`
- Event: `007 Fury`
- Scope completed: Fury achievement icon package only
- Scope not touched: gameplay, localisation, `.gfx`, GUI, scripts, focuses, decisions, ideas, spreadsheets

## Visual Approach

- Replaced the Fury achievement set with HOI4-style framed medal icons rather than flat symbolic glyphs.
- Kept the set centered on war-office papers, map pins, broken seals, border firebreaks, blackened ledgers, and isolated standards instead of generic fantasy flames.
- Built all `_grey` and `_not_eligible` variants from the completed medal icons so the package stays visually consistent across all ten achievements.

## Changed Files

### Final DDS replacements

- `gfx/achievements/achievement_fury_firebreak.dds`
- `gfx/achievements/achievement_fury_firebreak_grey.dds`
- `gfx/achievements/achievement_fury_firebreak_not_eligible.dds`
- `gfx/achievements/achievement_fury_fuse_cut.dds`
- `gfx/achievements/achievement_fury_fuse_cut_grey.dds`
- `gfx/achievements/achievement_fury_fuse_cut_not_eligible.dds`
- `gfx/achievements/achievement_fury_last_neighbor.dds`
- `gfx/achievements/achievement_fury_last_neighbor_grey.dds`
- `gfx/achievements/achievement_fury_last_neighbor_not_eligible.dds`
- `gfx/achievements/achievement_fury_major_without_faction.dds`
- `gfx/achievements/achievement_fury_major_without_faction_grey.dds`
- `gfx/achievements/achievement_fury_major_without_faction_not_eligible.dds`
- `gfx/achievements/achievement_fury_no_cores.dds`
- `gfx/achievements/achievement_fury_no_cores_grey.dds`
- `gfx/achievements/achievement_fury_no_cores_not_eligible.dds`
- `gfx/achievements/achievement_fury_no_minor_major.dds`
- `gfx/achievements/achievement_fury_no_minor_major_grey.dds`
- `gfx/achievements/achievement_fury_no_minor_major_not_eligible.dds`
- `gfx/achievements/achievement_fury_pact_breaker.dds`
- `gfx/achievements/achievement_fury_pact_breaker_grey.dds`
- `gfx/achievements/achievement_fury_pact_breaker_not_eligible.dds`
- `gfx/achievements/achievement_fury_rivals_burn.dds`
- `gfx/achievements/achievement_fury_rivals_burn_grey.dds`
- `gfx/achievements/achievement_fury_rivals_burn_not_eligible.dds`
- `gfx/achievements/achievement_fury_ten_fires.dds`
- `gfx/achievements/achievement_fury_ten_fires_grey.dds`
- `gfx/achievements/achievement_fury_ten_fires_not_eligible.dds`
- `gfx/achievements/achievement_fury_world_without_fury.dds`
- `gfx/achievements/achievement_fury_world_without_fury_grey.dds`
- `gfx/achievements/achievement_fury_world_without_fury_not_eligible.dds`

### Asset package files

- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_firebreak_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_fuse_cut_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_last_neighbor_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_major_without_faction_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_no_cores_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_no_minor_major_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_pact_breaker_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_rivals_burn_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_ten_fires_source.png`
- `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_world_without_fury_source.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury_grey.png`
- `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury_not_eligible.png`
- `docs/assets/007_fury/achievements_regen/contact_sheets/fury_achievement_regen_sheet.png`
- `docs/assets/007_fury/achievements_regen/manifest.md`
- `docs/plans/007_fury_plans/subagent_handoffs/2026-06-11_fury_achievement_icon_regen_handoff.md`

## Validation

- Verified all 30 target DDS files exist.
- Verified all 30 target DDS files are `64x64`.
- Verified each completed icon has matching `_grey` and `_not_eligible` variants.
- Verified 10 source PNGs were copied into the asset package.
- Verified 30 processed PNG previews were written into the asset package.
- Verified the final contact sheet exists at `docs/assets/007_fury/achievements_regen/contact_sheets/fury_achievement_regen_sheet.png`.

## Blockers And Uncertainty

- No blocked outputs remain.
- `achievement_fury_no_cores` was not separately generated. Per parent instruction, it was derived locally from the dossier/source family to keep the package stylistically coherent and avoid blocking on another generation pass.
- No `.gfx` edits were required because the existing achievement filenames were preserved exactly.

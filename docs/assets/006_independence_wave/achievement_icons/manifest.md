# 006 Independence Wave Achievement Icons Manifest

Package scope: bounded Event 006 Independence Wave achievement icon package only.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_grey.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_not_eligible.png`
- Additional Chaos Redux achievement examples in the same folder for framing, contrast, and readability checks.

Source mode:
- `$imagegen` for generated completed-state source art.
- Generated-derived Event006 source art for `cr_five_small_flags` and `cr_suppression_failed`, assembled from symbolic ledger, banner, petition, seal, and baton shapes without real country symbols.
- Local ImageMagick processing for square crop, 64x64 resize, tonal cleanup, border treatment, grey variant, not-eligible variant, contact sheet, and DDS conversion.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Resulting DDS files validate as `64 x 64` in local `file` and `identify` checks. Earlier icons validate as `RGB888`; `cr_five_small_flags` and `cr_suppression_failed` validate as `ARGB8888`.

## Assets

### `cr_brokers_exposed`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_brokers_exposed`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_brokers_exposed.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_brokers_exposed_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_brokers_exposed.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_brokers_exposed_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_brokers_exposed_not_eligible.png`
- Final DDS: `gfx/achievements/cr_brokers_exposed.dds`
- Final DDS grey: `gfx/achievements/cr_brokers_exposed_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_brokers_exposed_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_cr_no_more_flags_needed`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `cr_brokers_exposed`
- Notes: Torn foreign contract under desk lamp. No readable generated text.
- Asset status: `complete`

### `cr_five_small_flags`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_five_small_flags`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: generated-derived Event006 symbolic art
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_five_small_flags.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_five_small_flags_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags_not_eligible.png`
- Final DDS: `gfx/achievements/cr_five_small_flags.dds`
- Final DDS grey: `gfx/achievements/cr_five_small_flags_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_five_small_flags_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_cr_five_small_flags`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `cr_five_small_flags`
- Notes: Five generic small banners over a New States Congress ledger and seal. No real country flags or readable generated text.
- Asset status: `complete`

### `cr_suppression_failed`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_suppression_failed`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: generated-derived Event006 symbolic art
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_suppression_failed.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_suppression_failed_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed_not_eligible.png`
- Final DDS: `gfx/achievements/cr_suppression_failed.dds`
- Final DDS grey: `gfx/achievements/cr_suppression_failed_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_suppression_failed_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_cr_suppression_failed`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `cr_suppression_failed`
- Notes: Sealed petition beneath a cracked baton. No real country flags or readable generated text.
- Asset status: `complete`

### `cr_partition_without_war`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_partition_without_war`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_partition_without_war.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_partition_without_war_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_partition_without_war.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_partition_without_war_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_partition_without_war_not_eligible.png`
- Final DDS: `gfx/achievements/cr_partition_without_war.dds`
- Final DDS grey: `gfx/achievements/cr_partition_without_war_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_partition_without_war_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_partition_without_war`
- Notes: Survey chain over map with calm white markers. No readable generated text.
- Asset status: `complete`

### `cr_first_old_name`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_first_old_name`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_first_old_name.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_first_old_name_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_first_old_name.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_first_old_name_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_first_old_name_not_eligible.png`
- Final DDS: `gfx/achievements/cr_first_old_name.dds`
- Final DDS grey: `gfx/achievements/cr_first_old_name_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_first_old_name_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_first_old_name`
- Notes: Old seal against modern dossier/passport framing. No readable generated text.
- Asset status: `complete`

### `cr_old_name_modern_state`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_old_name_modern_state`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen` prompt attempted, then generated-derived Event006 source composition from existing generated old-name and charter source art because the live generated image was not exposed as a local file by the tool.
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_old_name_modern_state.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_old_name_modern_state_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state_not_eligible.png`
- Final DDS: `gfx/achievements/cr_old_name_modern_state.dds`
- Final DDS grey: `gfx/achievements/cr_old_name_modern_state_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_old_name_modern_state_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_cr_old_name_modern_state`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `cr_old_name_modern_state`
- Notes: Old seal over a modern charter folder, derived from existing generated Event006 old-name/charter art. No readable text, no flags, and no real national symbols.
- Asset status: `complete`

### `cr_local_land_congress`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_local_land_congress`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_local_land_congress.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_local_land_congress_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_local_land_congress.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_local_land_congress_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_local_land_congress_not_eligible.png`
- Final DDS: `gfx/achievements/cr_local_land_congress.dds`
- Final DDS grey: `gfx/achievements/cr_local_land_congress_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_local_land_congress_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_local_land_congress`
- Notes: Council chair with field boundary marker. No readable generated text.
- Asset status: `complete`

### `cr_railway_country`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_railway_country`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_railway_country.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_railway_country_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_railway_country.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_railway_country_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_railway_country_not_eligible.png`
- Final DDS: `gfx/achievements/cr_railway_country.dds`
- Final DDS grey: `gfx/achievements/cr_railway_country_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_railway_country_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_railway_country`
- Notes: Locomotive front with small neutral sovereignty marker. No readable generated text.
- Asset status: `complete`

### `cr_not_the_collapse`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_not_the_collapse`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_not_the_collapse.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_not_the_collapse_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_not_the_collapse.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_not_the_collapse_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_not_the_collapse_not_eligible.png`
- Final DDS: `gfx/achievements/cr_not_the_collapse.dds`
- Final DDS grey: `gfx/achievements/cr_not_the_collapse_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_not_the_collapse_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_not_the_collapse`
- Notes: Two case files distinguished by symbols and color only. No flags. No readable generated text.
- Asset status: `complete`

### `cr_charter_becomes_state`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_charter_becomes_state`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_charter_becomes_state.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_charter_becomes_state_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_charter_becomes_state.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_charter_becomes_state_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_charter_becomes_state_not_eligible.png`
- Final DDS: `gfx/achievements/cr_charter_becomes_state.dds`
- Final DDS grey: `gfx/achievements/cr_charter_becomes_state_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_charter_becomes_state_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_charter_becomes_state`
- Notes: Charter seal unfolding into a state document. No readable generated text.
- Asset status: `complete`

### `cr_the_ledger_votes_back`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_the_ledger_votes_back`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_the_ledger_votes_back.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_the_ledger_votes_back_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_the_ledger_votes_back.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_the_ledger_votes_back_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_the_ledger_votes_back_not_eligible.png`
- Final DDS: `gfx/achievements/cr_the_ledger_votes_back.dds`
- Final DDS grey: `gfx/achievements/cr_the_ledger_votes_back_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_the_ledger_votes_back_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_the_ledger_votes_back`
- Notes: Ledger page with three official stamps. No readable generated text.
- Asset status: `complete`

### `cr_capital_still_answers`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_capital_still_answers`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_capital_still_answers.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_capital_still_answers_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_capital_still_answers.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_capital_still_answers_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_capital_still_answers_not_eligible.png`
- Final DDS: `gfx/achievements/cr_capital_still_answers.dds`
- Final DDS grey: `gfx/achievements/cr_capital_still_answers_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_capital_still_answers_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_capital_still_answers`
- Notes: Lamp-lit capital ministry beyond a torn administrative map, with one capital marker still glowing. No readable generated text. No flags.
- Asset status: `complete`

### `cr_no_more_flags_needed`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_no_more_flags_needed`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_no_more_flags_needed.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_no_more_flags_needed_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed_not_eligible.png`
- Final DDS: `gfx/achievements/cr_no_more_flags_needed.dds`
- Final DDS grey: `gfx/achievements/cr_no_more_flags_needed_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_no_more_flags_needed_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_no_more_flags_needed`
- Notes: Folded generic banners in a calm map room, processed from generated source art with no real country flags, heraldry, or readable text.
- Asset status: `complete`

### `cr_human_renunciation`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_human_renunciation`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_human_renunciation.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_human_renunciation_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_human_renunciation.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_human_renunciation_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_human_renunciation_not_eligible.png`
- Final DDS: `gfx/achievements/cr_human_renunciation.dds`
- Final DDS grey: `gfx/achievements/cr_human_renunciation_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_human_renunciation_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `not_needed`
- `.gfx` file: `not_needed`
- Related achievement id: `cr_human_renunciation`
- Notes: Generic state seal over a scratched-out human dossier silhouette. Symbolic bureaucratic renunciation motif only, no text, no real flags, no real national symbols, and no horror styling.
- Asset status: `complete`

### `cr_league_war_victory`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `cr_league_war_victory`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/006_independence_wave/achievement_icons/prompts/cr_league_war_victory.txt`
- Source PNG: `docs/assets/006_independence_wave/achievement_icons/source_png/cr_league_war_victory_source.png`
- Processed PNG: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory.png`
- Processed PNG grey: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_grey.png`
- Processed PNG not eligible: `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_not_eligible.png`
- Final DDS: `gfx/achievements/cr_league_war_victory.dds`
- Final DDS grey: `gfx/achievements/cr_league_war_victory_grey.dds`
- Final DDS not eligible: `gfx/achievements/cr_league_war_victory_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_cr_league_war_victory` (proposed; `.gfx` not edited in this asset-only task)
- `.gfx` file: `interface/chaosx_achievements.gfx` (proposed handoff target only)
- Related achievement id: `cr_league_war_victory`
- Notes: Sealed charter held over crossed rifles, composed to keep the charter readable at small size. No flags, no logos, and no readable text.
- Asset status: `complete`

## Package files

- Contact sheet: `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet.png`
- Raw 64 review contact sheet: `docs/assets/006_independence_wave/achievement_icons/contact_sheets/raw_sources_64_contact.png`
- All states contact sheet: `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`

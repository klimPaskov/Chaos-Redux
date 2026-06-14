# 009 White Peace Asset Manifest

Package scope: Event 009 `White Peace` report image and achievement icon package.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_grey.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_not_eligible.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/the_revolution_triumphant.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/assuming_direct_control.png`
- `docs/assets/008_tensions_rising/manifest.md`
- `docs/assets/008_tensions_rising/gfx_handoff.md`

Source mode:
- `$imagegen` for generated completed-state source art.
- Local ImageMagick processing for exact `64x64` achievement resize, grey variants, not-eligible red-cross variants, contact sheet assembly, and DDS conversion.
- Expected sprite aliases follow the repo achievement pattern `GFX_achievement_<achievement_id>`.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Achievement DDS triplets validate at `64x64`.

## Assets

### `report_event_009_white_peace`
- Asset type: report event image
- Intended in-game use: Event 009 White Peace report popups
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/report_event_009_white_peace.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/report_event_009_white_peace_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/report_event_009_white_peace.png`
- Final DDS: `gfx/event_pictures/report_event_009_white_peace.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_009_white_peace`
- `.gfx` file: `interface/009_white_peace_event_images.gfx`
- Notes: Restrained period consular/radio-room scene with a signed armistice note, no readable generated text, no triumphal ceremony.
- Asset status: `complete`

### `achievement_white_peace_status_quo_ante`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_white_peace_status_quo_ante`
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/achievement_white_peace_status_quo_ante.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/achievement_white_peace_status_quo_ante_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/achievement_white_peace_status_quo_ante.png`
- Processed PNG grey: `docs/assets/009_white_peace/processed_png/achievement_white_peace_status_quo_ante_grey.png`
- Processed PNG not eligible: `docs/assets/009_white_peace/processed_png/achievement_white_peace_status_quo_ante_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_white_peace_status_quo_ante.dds`
- Final DDS grey: `gfx/achievements/achievement_white_peace_status_quo_ante_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_white_peace_status_quo_ante_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_white_peace_status_quo_ante`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_white_peace_status_quo_ante`
- Notes: Unchanged border line between two small flags with a sealed peace paper as the focal point. No readable text.
- Asset status: `complete`

### `achievement_white_peace_no_winner`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_white_peace_no_winner`
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/achievement_white_peace_no_winner.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/achievement_white_peace_no_winner_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/achievement_white_peace_no_winner.png`
- Processed PNG grey: `docs/assets/009_white_peace/processed_png/achievement_white_peace_no_winner_grey.png`
- Processed PNG not eligible: `docs/assets/009_white_peace/processed_png/achievement_white_peace_no_winner_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_white_peace_no_winner.dds`
- Final DDS grey: `gfx/achievements/achievement_white_peace_no_winner_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_white_peace_no_winner_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_white_peace_no_winner`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_white_peace_no_winner`
- Notes: Open hands setting aside weapons beside a blank treaty page, with the page kept central for legibility. No readable text.
- Asset status: `complete`

### `achievement_white_peace_chain_of_tables`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_white_peace_chain_of_tables`
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/achievement_white_peace_chain_of_tables.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/achievement_white_peace_chain_of_tables_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/achievement_white_peace_chain_of_tables.png`
- Processed PNG grey: `docs/assets/009_white_peace/processed_png/achievement_white_peace_chain_of_tables_grey.png`
- Processed PNG not eligible: `docs/assets/009_white_peace/processed_png/achievement_white_peace_chain_of_tables_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_white_peace_chain_of_tables.dds`
- Final DDS grey: `gfx/achievements/achievement_white_peace_chain_of_tables_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_white_peace_chain_of_tables_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_white_peace_chain_of_tables`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_white_peace_chain_of_tables`
- Notes: Receding lamp-lit negotiation tables with the front table carrying the composition at small size. No readable text.
- Asset status: `complete`

### `achievement_white_peace_silence_of_giants`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_white_peace_silence_of_giants`
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/achievement_white_peace_silence_of_giants.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/achievement_white_peace_silence_of_giants_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/achievement_white_peace_silence_of_giants.png`
- Processed PNG grey: `docs/assets/009_white_peace/processed_png/achievement_white_peace_silence_of_giants_grey.png`
- Processed PNG not eligible: `docs/assets/009_white_peace/processed_png/achievement_white_peace_silence_of_giants_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_white_peace_silence_of_giants.dds`
- Final DDS grey: `gfx/achievements/achievement_white_peace_silence_of_giants_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_white_peace_silence_of_giants_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_white_peace_silence_of_giants`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_white_peace_silence_of_giants`
- Notes: Two lowered artillery silhouettes under a sealed peace document, with the document dominant. No readable text.
- Asset status: `complete`

### `achievement_white_peace_the_circular`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_white_peace_the_circular`
- Related event id: `009`
- Related event slug: `white_peace`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/009_white_peace/prompts/achievement_white_peace_the_circular.txt`
- Source PNG: `docs/assets/009_white_peace/source_png/achievement_white_peace_the_circular_source.png`
- Processed PNG: `docs/assets/009_white_peace/processed_png/achievement_white_peace_the_circular.png`
- Processed PNG grey: `docs/assets/009_white_peace/processed_png/achievement_white_peace_the_circular_grey.png`
- Processed PNG not eligible: `docs/assets/009_white_peace/processed_png/achievement_white_peace_the_circular_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_white_peace_the_circular.dds`
- Final DDS grey: `gfx/achievements/achievement_white_peace_the_circular_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_white_peace_the_circular_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_white_peace_the_circular`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_white_peace_the_circular`
- Notes: Circular stamp or telegraph ring over several sealed envelopes. No readable text.
- Asset status: `complete`

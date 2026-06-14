# 008 Tensions Rising Asset Manifest

Package scope: Event 008 `Tensions Rising` report art, news art, Stage IV super-event art, and achievement icon package.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_grey.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_not_eligible.png`
- Additional Chaos Redux achievement examples in the same folder for framing, contrast, and readability checks.
- Existing Chaos Redux report, news, and super-event DDS dimensions and sprite wiring in `gfx/event_pictures/`, `gfx/super_events/`, `interface/008_tensions_rising_event_images.gfx`, and `interface/chaosx_super_events.gfx`.

Source mode:
- `$imagegen` for generated completed-state source art.
- `$imagegen` plus local processing for the report, news, and super-event images.
- Local ImageMagick processing for exact event image dimensions, exact `64x64` achievement resize, tonal cleanup, grey variants, not-eligible red-cross variants, blackout window-count correction on the processed icon, and DDS conversion.
- Sprite aliases are registered in `interface/chaosx_achievements.gfx` using `GFX_achievement_<achievement_id>`.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- All final DDS files validate as `64x64`.
- `file` reports a mix of `RGB888` and `ARGB8888` across the triplets; all exports remain valid uncompressed DDS outputs for the HOI4 achievement pipeline.

## Assets

### `report_event_tensions_rising`
- Asset type: report event image
- Intended in-game use: main Event 008 popup
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Source PNG A: `docs/assets/008_tensions_rising/source_png/report_event_tensions_rising_source_a.png`
- Source PNG B: `docs/assets/008_tensions_rising/source_png/report_event_tensions_rising_source_b.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/report_event_tensions_rising.png`
- Final DDS: `gfx/event_pictures/report_event_tensions_rising.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_tensions_rising`
- `.gfx` file: `interface/008_tensions_rising_event_images.gfx`
- Notes: Diplomatic-cable pressure scene for the repeatable report event.
- Asset status: `complete`

### `news_event_tensions_red_line`
- Asset type: news event image
- Intended in-game use: Stage IV Red Line news surface
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Source PNG A: `docs/assets/008_tensions_rising/source_png/news_event_tensions_red_line_source_a.png`
- Source PNG B: `docs/assets/008_tensions_rising/source_png/news_event_tensions_red_line_source_b.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/news_event_tensions_red_line.png`
- Final DDS: `gfx/event_pictures/news_event_tensions_red_line.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_tensions_red_line`
- `.gfx` file: `interface/008_tensions_rising_event_images.gfx`
- Notes: Quiet red-line crisis news image; no readable text.
- Asset status: `complete`

### `super_event_tensions_red_line`
- Asset type: super-event image
- Intended in-game use: one-time non-terminal Stage IV super-event `The Red Line Disappears`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Source PNG A: `docs/assets/008_tensions_rising/source_png/super_event_tensions_red_line_source_a.png`
- Source PNG B: `docs/assets/008_tensions_rising/source_png/super_event_tensions_red_line_source_b.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/super_event_tensions_red_line.png`
- Final DDS: `gfx/super_events/super_event_tensions_red_line.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_tensions_red_line`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Notes: Ministry lights and severed diplomatic line motif for the non-terminal super-event.
- Asset status: `complete`

### `achievement_tensions_thin_wire`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_thin_wire`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_thin_wire.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_thin_wire_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_thin_wire.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_thin_wire_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_thin_wire_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_thin_wire.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_thin_wire_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_thin_wire_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_thin_wire`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_thin_wire`
- Notes: Taut telegraph wire over a dark diplomatic map, no readable text.
- Asset status: `complete`

### `achievement_tensions_only_headlines`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_only_headlines`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_only_headlines.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_only_headlines_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_only_headlines.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_only_headlines_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_only_headlines_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_only_headlines.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_only_headlines_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_only_headlines_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_only_headlines`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_only_headlines`
- Notes: Stacked newspapers under a silent clock, no readable text.
- Asset status: `complete`

### `achievement_tensions_insurance_market`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_insurance_market`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_insurance_market.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_insurance_market_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_insurance_market.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_insurance_market_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_insurance_market_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_insurance_market.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_insurance_market_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_insurance_market_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_insurance_market`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_insurance_market`
- Notes: Marine insurance ledger, ship silhouette, and red wax seal. The seal uses a stylized anchor imprint but no readable text.
- Asset status: `complete`

### `achievement_tensions_red_line`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_red_line`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_red_line.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_red_line_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_red_line.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_red_line_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_red_line_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_red_line.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_red_line_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_red_line_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_red_line`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_red_line`
- Notes: Broken red cord across a dark embassy window.
- Asset status: `complete`

### `achievement_tensions_one_denial`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_one_denial`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_one_denial.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_one_denial_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_one_denial.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_one_denial_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_one_denial_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_one_denial.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_one_denial_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_one_denial_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_one_denial`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_one_denial`
- Notes: Denial-stamp motif over a sealed cable, with the refusal conveyed by shape rather than readable words.
- Asset status: `complete`

### `achievement_tensions_blackout`
- Asset type: achievement icon triplet
- Intended in-game use: custom achievement `achievement_tensions_blackout`
- Related event id: `008`
- Related event slug: `tensions_rising`
- Source mode: `$imagegen`
- Prompt file: `docs/assets/008_tensions_rising/prompts/achievement_tensions_blackout.txt`
- Source PNG: `docs/assets/008_tensions_rising/source_png/achievement_tensions_blackout_source.png`
- Processed PNG: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_blackout.png`
- Processed PNG grey: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_blackout_grey.png`
- Processed PNG not eligible: `docs/assets/008_tensions_rising/processed_png/achievement_tensions_blackout_not_eligible.png`
- Final DDS: `gfx/achievements/achievement_tensions_blackout.dds`
- Final DDS grey: `gfx/achievements/achievement_tensions_blackout_grey.dds`
- Final DDS not eligible: `gfx/achievements/achievement_tensions_blackout_not_eligible.dds`
- Target size: `64x64`
- Sprite name: `GFX_achievement_achievement_tensions_blackout`
- `.gfx` file: `interface/chaosx_achievements.gfx`
- Related achievement id: `achievement_tensions_blackout`
- Notes: Blacked-out embassy facade. The processed `64x64` icon includes a local blackout correction so the shipped icon shows exactly ten lit windows.
- Asset status: `complete`

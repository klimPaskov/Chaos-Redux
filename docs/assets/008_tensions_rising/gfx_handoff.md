# Event 008 Asset GFX Handoff

The Event 008 report, news, super-event, and achievement assets are ready for their HOI4 GFX surfaces.

The icons are registered in `interface/chaosx_achievements.gfx` using the repo achievement sprite pattern `GFX_achievement_<achievement_id>`.

## Event and super-event images

| Asset | Final DDS | Sprite alias | GFX file | Status |
| --- | --- | --- | --- | --- |
| Report image | `gfx/event_pictures/report_event_tensions_rising.dds` | `GFX_report_event_tensions_rising` | `interface/008_tensions_rising_event_images.gfx` | `complete` |
| News image | `gfx/event_pictures/news_event_tensions_red_line.dds` | `GFX_news_event_tensions_red_line` | `interface/008_tensions_rising_event_images.gfx` | `complete` |
| Super-event image | `gfx/super_events/super_event_tensions_red_line.dds` | `GFX_super_event_tensions_red_line` | `interface/chaosx_super_events.gfx` | `complete` |

## Completed DDS triplets

| Achievement id | Base DDS | Grey DDS | Not-eligible DDS | Suggested alias | Status |
| --- | --- | --- | --- | --- | --- |
| `achievement_tensions_thin_wire` | `gfx/achievements/achievement_tensions_thin_wire.dds` | `gfx/achievements/achievement_tensions_thin_wire_grey.dds` | `gfx/achievements/achievement_tensions_thin_wire_not_eligible.dds` | `GFX_achievement_achievement_tensions_thin_wire` | `complete` |
| `achievement_tensions_only_headlines` | `gfx/achievements/achievement_tensions_only_headlines.dds` | `gfx/achievements/achievement_tensions_only_headlines_grey.dds` | `gfx/achievements/achievement_tensions_only_headlines_not_eligible.dds` | `GFX_achievement_achievement_tensions_only_headlines` | `complete` |
| `achievement_tensions_insurance_market` | `gfx/achievements/achievement_tensions_insurance_market.dds` | `gfx/achievements/achievement_tensions_insurance_market_grey.dds` | `gfx/achievements/achievement_tensions_insurance_market_not_eligible.dds` | `GFX_achievement_achievement_tensions_insurance_market` | `complete` |
| `achievement_tensions_red_line` | `gfx/achievements/achievement_tensions_red_line.dds` | `gfx/achievements/achievement_tensions_red_line_grey.dds` | `gfx/achievements/achievement_tensions_red_line_not_eligible.dds` | `GFX_achievement_achievement_tensions_red_line` | `complete` |
| `achievement_tensions_one_denial` | `gfx/achievements/achievement_tensions_one_denial.dds` | `gfx/achievements/achievement_tensions_one_denial_grey.dds` | `gfx/achievements/achievement_tensions_one_denial_not_eligible.dds` | `GFX_achievement_achievement_tensions_one_denial` | `complete` |
| `achievement_tensions_blackout` | `gfx/achievements/achievement_tensions_blackout.dds` | `gfx/achievements/achievement_tensions_blackout_grey.dds` | `gfx/achievements/achievement_tensions_blackout_not_eligible.dds` | `GFX_achievement_achievement_tensions_blackout` | `complete` |

## Notes

- Prompt records live under `docs/assets/008_tensions_rising/prompts/`.
- Source PNGs live under `docs/assets/008_tensions_rising/source_png/`.
- Processed PNGs live under `docs/assets/008_tensions_rising/processed_png/`.
- The completed-state icon for `achievement_tensions_blackout` required one local processed-icon correction so the shipped `64x64` asset displays exactly ten lit windows.

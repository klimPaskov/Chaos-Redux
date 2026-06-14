# Event 009 GFX Handoff

The Event 009 White Peace report image and achievement icons are ready for HOI4 sprite wiring.

## Report image

| Sprite alias | DDS | Expected `.gfx` file | Use | Status |
| --- | --- | --- | --- | --- |
| `GFX_report_event_009_white_peace` | `gfx/event_pictures/report_event_009_white_peace.dds` | `interface/009_white_peace_event_images.gfx` | Event 009 report popups | `complete` |

The expected sprite aliases follow the repo achievement pattern `GFX_achievement_<achievement_id>` and should be registered by the parent in `interface/chaosx_achievements.gfx`.

## Completed DDS triplets

| Achievement id | Base DDS | Grey DDS | Not-eligible DDS | Expected sprite alias | Status |
| --- | --- | --- | --- | --- | --- |
| `achievement_white_peace_status_quo_ante` | `gfx/achievements/achievement_white_peace_status_quo_ante.dds` | `gfx/achievements/achievement_white_peace_status_quo_ante_grey.dds` | `gfx/achievements/achievement_white_peace_status_quo_ante_not_eligible.dds` | `GFX_achievement_achievement_white_peace_status_quo_ante` | `complete` |
| `achievement_white_peace_no_winner` | `gfx/achievements/achievement_white_peace_no_winner.dds` | `gfx/achievements/achievement_white_peace_no_winner_grey.dds` | `gfx/achievements/achievement_white_peace_no_winner_not_eligible.dds` | `GFX_achievement_achievement_white_peace_no_winner` | `complete` |
| `achievement_white_peace_chain_of_tables` | `gfx/achievements/achievement_white_peace_chain_of_tables.dds` | `gfx/achievements/achievement_white_peace_chain_of_tables_grey.dds` | `gfx/achievements/achievement_white_peace_chain_of_tables_not_eligible.dds` | `GFX_achievement_achievement_white_peace_chain_of_tables` | `complete` |
| `achievement_white_peace_silence_of_giants` | `gfx/achievements/achievement_white_peace_silence_of_giants.dds` | `gfx/achievements/achievement_white_peace_silence_of_giants_grey.dds` | `gfx/achievements/achievement_white_peace_silence_of_giants_not_eligible.dds` | `GFX_achievement_achievement_white_peace_silence_of_giants` | `complete` |
| `achievement_white_peace_the_circular` | `gfx/achievements/achievement_white_peace_the_circular.dds` | `gfx/achievements/achievement_white_peace_the_circular_grey.dds` | `gfx/achievements/achievement_white_peace_the_circular_not_eligible.dds` | `GFX_achievement_achievement_white_peace_the_circular` | `complete` |

## Notes

- Prompt records live under `docs/assets/009_white_peace/prompts/`.
- Source PNGs live under `docs/assets/009_white_peace/source_png/`.
- Processed PNGs live under `docs/assets/009_white_peace/processed_png/`.
- Contact sheet preview lives at `docs/assets/009_white_peace/contact_sheet/009_white_peace_achievements_contact.png`.
- No gameplay, localisation, or `.gfx` wiring files were edited in this package.

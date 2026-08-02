# Subagent handoff: Fallout Ash-week orientation report assets

Producer: `/root/fallout_orientation_art`
Parent reviewer: `/root`
Review date: `2026-07-18`
Status: `complete`

## Delivered scope

Six distinct fictional period-documentary source images were generated with Codex's official built-in ImageGen, processed with the repository report-event processor, and converted with the skill-owned DDS converter. The scenes are: national register, damaged capital shelter routing, regionally neutral resource distribution, damaged civic authority meeting, fictional water-engineer institution, and closure orders leaving damaged administration.

No source reuses Air Winter art. The images contain no readable text, flags, logos, zombies, zombie assets, modern objects, or real-person likenesses. All selected source images are unframed. The report-card border, tilt, shadow, and transparent corners are produced locally by `process_report_event_image.py`.

## Files

- Package root: `docs/assets/fallout_world_end/ash_week_orientation/`
- Source PNGs: `source/report_event_fallout_*_source.png` (six)
- Processed PNGs: `processed/report_event_fallout_*.png` (six, `210x176`)
- Contact sheet: `contact_sheet/contact_sheet.png`
- Prompt record: `prompts/fallout_ash_week_orientation_prompts.md`
- Manifest with source/processed/DDS hashes: `asset_manifest.json`
- Requirement-to-runtime crosswalk: `requirement_to_runtime_crosswalk.md`
- GFX note: `gfx_handoff.md`
- Final DDS files: `gfx/event_pictures/fallout/report_event_fallout_{national_orientation,capital_condition,resource_crisis,government_archetype,character_institution,orientation_closure}.dds`

## Runtime sprite mapping

Use `interface/fallout_world_end.gfx` and the stable sprite names below:

| Sprite | Final DDS |
| --- | --- |
| `GFX_report_event_fallout_national_orientation` | `gfx/event_pictures/fallout/report_event_fallout_national_orientation.dds` |
| `GFX_report_event_fallout_capital_condition` | `gfx/event_pictures/fallout/report_event_fallout_capital_condition.dds` |
| `GFX_report_event_fallout_resource_crisis` | `gfx/event_pictures/fallout/report_event_fallout_resource_crisis.dds` |
| `GFX_report_event_fallout_government_archetype` | `gfx/event_pictures/fallout/report_event_fallout_government_archetype.dds` |
| `GFX_report_event_fallout_character_institution` | `gfx/event_pictures/fallout/report_event_fallout_character_institution.dds` |
| `GFX_report_event_fallout_orientation_closure` | `gfx/event_pictures/fallout/report_event_fallout_orientation_closure.dds` |

Contract role mapping: national orientation (62/63 -> 64/65), capital condition (66/67 -> 68/69), resource crisis (70/71 -> 72/73), government archetype (74/75 -> 76/77), character/institution (78/79 -> 80/81), and closure (82/83). Cleanup 84 is hidden and has no dedicated card requirement.

## Validation

The final validation run confirmed all six DDS headers, dimensions, exact lengths, alpha range, transparent corners in their processed inputs, and exact RGBA equality after BGRA DDS decode. SHA-256 values and byte counts are authoritative in `asset_manifest.json`.

Parent visual review approved the contact sheet and six processed cards as distinct, period-plausible, readable at runtime size, and correctly treated. No separate advisor-style visual approval gate applies to these report-event cards.

## Main-agent disposition

The six sprites are registered in `interface/fallout_world_end.gfx`. Event bindings, event localisation, and log or detail consumers remain pending.

## Remaining risks

- Main agent must bind the correct event roots, results, and closure. No gameplay or spreadsheet file was edited by the asset producer.
- The water-engineer is fictional event-scene art only, not a gameplay portrait or generated character record.

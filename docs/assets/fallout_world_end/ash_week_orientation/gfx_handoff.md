# Fallout Ash-week orientation report-art GFX handoff

These six final textures are registered by the main agent in `interface/fallout_world_end.gfx`. Do not edit the DDS files in place. Keep the sprite names stable.

| Sprite | Texture path | Size | Suggested owner / use |
| --- | --- | --- | --- |
| `GFX_report_event_fallout_national_orientation` | `gfx/event_pictures/fallout_world_end/report_event_fallout_national_orientation.dds` | `210x176` | National orientation root/result report card |
| `GFX_report_event_fallout_capital_condition` | `gfx/event_pictures/fallout_world_end/report_event_fallout_capital_condition.dds` | `210x176` | Capital condition root/result report card |
| `GFX_report_event_fallout_resource_crisis` | `gfx/event_pictures/fallout_world_end/report_event_fallout_resource_crisis.dds` | `210x176` | Immediate resource crisis root/result report card |
| `GFX_report_event_fallout_government_archetype` | `gfx/event_pictures/fallout_world_end/report_event_fallout_government_archetype.dds` | `210x176` | Government-archetype root/result report card |
| `GFX_report_event_fallout_character_institution` | `gfx/event_pictures/fallout_world_end/report_event_fallout_character_institution.dds` | `210x176` | First character/institution root/result report card |
| `GFX_report_event_fallout_orientation_closure` | `gfx/event_pictures/fallout_world_end/report_event_fallout_orientation_closure.dds` | `210x176` | Human-visible orientation closure report card |

Suggested sprite snippet pattern (adapt to the existing file's conventions):

```text
spriteType = {
	name = "GFX_report_event_fallout_national_orientation"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_national_orientation.dds"
}
```

Repeat the same `spriteType` shape for the other five names and texture paths. The main agent owns final `.gfx` syntax, ordering, and all event/localisation references. Hidden AI roots/results should retain their gameplay visibility semantics. The art itself is not a fallback or substitute for hidden events.

## Package evidence

- Sources: `docs/assets/fallout_world_end/ash_week_orientation/source/`
- Processed previews: `docs/assets/fallout_world_end/ash_week_orientation/processed/`
- Prompts: `docs/assets/fallout_world_end/ash_week_orientation/prompts/fallout_ash_week_orientation_prompts.md`
- Contact sheet: `docs/assets/fallout_world_end/ash_week_orientation/contact_sheet/contact_sheet.png`
- Manifest and hashes: `docs/assets/fallout_world_end/ash_week_orientation/asset_manifest.json`
- Requirement crosswalk: `docs/assets/fallout_world_end/ash_week_orientation/requirement_to_runtime_crosswalk.md`
- Independent visual review: `/root`, 2026-07-18. All six processed cards were approved.

## Validation evidence

- Every processed PNG is exactly `210x176` RGBA. Each has transparent corner alpha `[0,0,0,0]` and alpha range `0..255`.
- Every DDS is exactly 147,968 bytes (`128 + 210*176*4`) with `DDS ` magic, `DDS_HEADER` size 124, one-level 32-bit BGRA masks, and `DDSCAPS_TEXTURE`.
- DDS decode reproduced each processed PNG's RGBA pixels exactly. Hashes are recorded in `asset_manifest.json`.

## Risks / notes

- Sprite registration is complete. Event consumers remain pending until the matching orientation blocks are implemented.
- The female-presenting water engineer appears only as a fictional scene subject. This package does not authorize a leader/advisor portrait or a personal gameplay identity.
- The report processor supplies the consistent tilt, shadow, sepia, grain, and transparent-edge treatment. Do not feed the processed cards back into ImageGen or reprocess them a second time.

# Event 013 Natural Disasters Generated Event Art Handoff

Status: complete for the requested report and news package, plus one optional super-event candidate.

Scope respected:
- `docs/assets/013_natural_disasters/**`
- `gfx/event_pictures/013_natural_disasters/**`
- `gfx/super_events/super_event_natural_disasters_abnormal_disaster_age.dds`

## Created assets

Report DDS:
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_baseline.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_warning.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_impact.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_recovery.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_earthquake.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_flood.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_storm.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_drought.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_wildfire.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_landslide.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_volcano.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_tsunami.dds`
- `gfx/event_pictures/013_natural_disasters/report_event_natural_disaster_meteor.dds`

News DDS:
- `gfx/event_pictures/013_natural_disasters/news_event_regional_disaster_system.dds`
- `gfx/event_pictures/013_natural_disasters/news_event_disaster_chains.dds`
- `gfx/event_pictures/013_natural_disasters/news_event_abnormal_disaster_age.dds`

Optional super-event candidate:
- `gfx/super_events/super_event_natural_disasters_abnormal_disaster_age.dds`

## Exact proposed sprite names

- `GFX_report_event_natural_disaster_baseline`
- `GFX_report_event_natural_disaster_warning`
- `GFX_report_event_natural_disaster_impact`
- `GFX_report_event_natural_disaster_recovery`
- `GFX_report_event_natural_disaster_earthquake`
- `GFX_report_event_natural_disaster_flood`
- `GFX_report_event_natural_disaster_storm`
- `GFX_report_event_natural_disaster_drought`
- `GFX_report_event_natural_disaster_wildfire`
- `GFX_report_event_natural_disaster_landslide`
- `GFX_report_event_natural_disaster_volcano`
- `GFX_report_event_natural_disaster_tsunami`
- `GFX_report_event_natural_disaster_meteor`
- `GFX_news_event_regional_disaster_system`
- `GFX_news_event_disaster_chains`
- `GFX_news_event_abnormal_disaster_age`
- `GFX_super_event_natural_disasters_abnormal_disaster_age`

## Metadata files

- Manifest: `docs/assets/013_natural_disasters/manifest.md`
- GFX handoff: `docs/assets/013_natural_disasters/gfx_handoff.md`
- Prompt log: `docs/assets/013_natural_disasters/prompts/generated_event_art_prompts.md`
- Review contact sheets: `docs/assets/013_natural_disasters/contact_sheets/*`

## Validation

- Processed PNG sizes verified:
  - report images `210x176`
  - news images `397x153`
  - super-event candidate `457x328`
- DDS outputs verified with `file`:
  - report DDS `210 x 176`, `32-bit color, ARGB8888`
  - news DDS `397 x 153`, `32-bit color, ARGB8888`
  - super-event DDS `457 x 328`, `32-bit color, ARGB8888`

## Blockers and notes

- The repo helper `python3 .tools/convert_to_dds.py` failed on this checkout because its ffmpeg fallback raised a DDS header `struct.pack` error. I used `convert -define dds:compression=none` instead and documented that in the manifest.
- The super-event file is a visual candidate only. No final title, quote, trigger, or audio approval is implied.

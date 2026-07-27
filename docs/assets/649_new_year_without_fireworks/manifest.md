# Asset manifest: 649 The New Year Without Fireworks

## Coverage crosswalk

| Requirement | Accepted design source | Asset package entry | Runtime registration | Live consumer | Status |
| --- | --- | --- | --- | --- | --- |
| `649.report.fallout_new_year_without_fireworks` | Parent asset brief for East Asia Fallout report | `report_event_fallout_new_year_without_fireworks` below | `gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds`, sprite `GFX_report_event_fallout_new_year_without_fireworks` | Registered in `interface/fallout_world_end.gfx` and referenced by events `649` through `655` | `registered` |

## `report_event_fallout_new_year_without_fireworks`

- Related event id: `649`
- Related event slug: `new_year_without_fireworks`
- Asset type: static report event image.
- Intended use: East Asia Fallout report at the year’s turning, “The New Year Without Fireworks.”
- Source mode: `$imagegen`.
- Generation fit: the brief calls for a fictional, alternate-history, regional community scene with no real identity or archival subject. Generation provides the specific ration-table, covered-lamp, memorial-ribbon, civilian, and guard composition without fabricating a real person or historical event.
- Identity classification: no one-person portrait and no identifiable person. Civilians and guards are anonymous scene elements.
- Generation prompt: [`prompts/imagegen_prompt.txt`](prompts/imagegen_prompt.txt).
- Generated source PNG: [`source_png/report_event_fallout_new_year_without_fireworks_source.png`](source_png/report_event_fallout_new_year_without_fireworks_source.png).
- Source PNG dimensions and mode: `1536x1024`, RGB.
- Source PNG SHA-256: `35de80ad3a67fa847f6a31ca782c7de18ab6c217c7c2afa2abf68d6a64f5826f`.
- Processed PNG: [`processed_png/report_event_fallout_new_year_without_fireworks.png`](processed_png/report_event_fallout_new_year_without_fireworks.png).
- Processed PNG dimensions and mode: `210x176`, RGBA.
- Processed PNG SHA-256: `8be3a5ded625b05349a87c2178dfa1a0a5645f997058b2275a6f6fbebf6a6b71`.
- Processed alpha extrema: `0..255`. Transparent corners are intentional report-card edge space.
- Processing command: `python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py docs/assets/649_new_year_without_fireworks/source_png/report_event_fallout_new_year_without_fireworks_source.png docs/assets/649_new_year_without_fireworks/processed_png/report_event_fallout_new_year_without_fireworks.png`.
- Final DDS: [`gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds`](../../../gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds).
- Final DDS dimensions: `210x176`.
- Final DDS SHA-256: `bc48046b0f5cb7a387f32e1e0317174271ff2b46697cb45640658535c4ace5b7`.
- Final DDS format: legacy one-level uncompressed BGRA, `DDS ` magic, header size `124`, pixel-format size `32`, flags `65`, fourCC `0`, 32-bit channels, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, exact length `147968` bytes.
- Final DDS alpha bytes: `0..255`. Transparency matches the processed PNG card corners and soft shadow.
- Sprite name: `GFX_report_event_fallout_new_year_without_fireworks`.
- Target `.gfx`: existing event-picture `.gfx` chosen and edited by the main agent. No `.gfx` file was edited in this package.
- Localisation key: parent-owned. No localisation changes were authorized for this asset package.
- Animation: not applicable. Static single frame only.
- Audio: not applicable.
- Flags and symbols: no real flags, national symbols, religious markers, readable script, modern branding, or watermarks.
- Asset status: `registered` for static `.gfx` and event wiring. Live presentation remains unproven because HOI4 was not launched.

## Validation evidence

- Processed PNG decoded as `210x176 RGBA` with alpha extrema `0..255`.
- DDS decoded header declared `210x176`. Exact file length is `128 + 210*176*4 = 147968` bytes.
- DDS pixel format and texture caps match the repository’s standard legacy BGRA requirements.
- No HOI4 run was performed, as requested. The parent agent owns final `.gfx` registration and runtime validation.

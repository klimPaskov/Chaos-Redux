# Fallout River Ration League report image manifest

## Requirement-to-runtime coverage

| Requirement | Asset | Runtime registration | Status |
| --- | --- | --- | --- |
| Dedicated fictional Europe report image for "The River Ration League". Cold ash-dimmed river junction, rival ration barges, customs boom, lock gate, frost reeds, abstract tally boards, distant church or civic tower. Target 210x176 | `report_event_fallout_river_ration_league` | `gfx/event_pictures/fallout_world_end/report_event_fallout_river_ration_league.dds`. Proposed sprite `GFX_report_event_fallout_river_ration_league`. Main agent-owned `.gfx` registration | Complete / handed off |

## Asset entry

- Asset name: `report_event_fallout_river_ration_league`
- Related event: The River Ration League (Europe air-cleanliness fallout event)
- Asset type: fictional alternate-history report event image
- Intended in-game use: 210x176 HOI4 report-event picture
- Source mode: `$imagegen` / built-in ImageGen generation
- Generation fit: the scene is fictional and alternate-history and requires a specific invented river-lock confrontation that is not an archival event. Generation avoids misrepresenting a real place or real people.
- Source PNG: `docs/assets/air_cleanliness_fallout/fallout_river_ration_league/source_png/report_event_fallout_river_ration_league_source.png`
- Source dimensions/mode: 1536x1024 RGB PNG
- Source SHA-256: `a5e88f786e7ac80a7e2e37e8a210db44908f6544cf84d7cace00d98908e57ce2`
- Processed preview: `docs/assets/air_cleanliness_fallout/fallout_river_ration_league/processed_png/report_event_fallout_river_ration_league.png`
- Processed dimensions/mode: 210x176 RGBA PNG
- Processed SHA-256: `71fa5aefed54d4f6ba5e5ec24ea3589d2f274c14d7d9552ba7363384d59c2f4e`
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_river_ration_league.dds`
- Final DDS dimensions: 210x176
- Final DDS SHA-256: `7f1688f6ef41b1d20e38d5ac8a4a2002bcf77e5373a3d42422f6593af270c8c2`
- Final DDS format: legacy one-level uncompressed BGRA/RGBA 32-bit (`DDS ` magic, header size 124, pixel-format size 32, flags 65, bit count 32, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, exact file length 147,968 bytes)
- Sprite name: `GFX_report_event_fallout_river_ration_league` (proposed, no `.gfx` file was edited in this subagent scope)
- Suggested target `.gfx`: existing Chaos Redux report-event sprite definition file used by the main implementation agent. The exact file remains parent-owned because this package explicitly forbids `.gfx` edits.
- Localisation key: not applicable to this art-only package.
- Source prompt: `docs/assets/air_cleanliness_fallout/fallout_river_ration_league/prompts/report_event_fallout_river_ration_league_prompt.md`
- Reference family inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/` and its `contact_sheet.png`. Report-card treatment was matched through the repository processor rather than generated in-image.
- Processing command: `python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py <source_png> <processed_png>`
- Conversion command: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed_png> --output <final_dds> --width 210 --height 176`
- Visual checks: source review showed the required two barges, central timber-and-cable customs boom, guarded lock gate/control hut, frost-covered reeds, abstract non-legible tally-board marks, and distant European church/civic tower. Processed preview shows the required slight tilt, pale sepia documentary treatment, soft shadow, transparent corners, and unclipped scene. No flags, logos, readable text, watermarks, zombies, or generic wasteland collage are present.
- Technical checks: source decodes as 1536x1024 RGB. Processed PNG decodes as 210x176 RGBA. All four processed corners have alpha 0 and the processed alpha range is 0-255. DDS header, dimensions, length, pixel masks, caps, and alpha range were validated. The DDS pixel payload is 147,840 bytes and its alpha range is 0-255.
- Prompt provenance gaps: built-in ImageGen does not expose a stable seed, model revision, or downloadable generation metadata in the tool result. The retained source path, tool output UUID, normalized prompt, source hash, and copied source PNG provide available provenance. No internet source, attribution, date, or license applies.
- Status: `complete` / `handed_off`, with no user review blocker.

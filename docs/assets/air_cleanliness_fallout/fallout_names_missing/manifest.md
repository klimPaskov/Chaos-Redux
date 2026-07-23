# Names for the Missing asset manifest

## Status

`wired` for the dormant Fallout chain. The package remains in the temporary asset workspace because the larger Fallout goal is incomplete and the chain is intentionally dormant.

## Runtime ownership

- Source: `docs/assets/air_cleanliness_fallout/fallout_names_missing/source/fallout_names_missing_source.png`
- Processed preview: `docs/assets/air_cleanliness_fallout/fallout_names_missing/processed/fallout_names_missing_preview.png`
- Runtime DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds`
- Sprite owner: `interface/fallout_world_end.gfx`
- Sprite: `GFX_report_event_fallout_names_missing`
- Visible consumers: `chaosx.fallout.269`, `chaosx.fallout.271` through `chaosx.fallout.274`, and `chaosx.fallout.279`
- Hidden lanes: events `270`, `275` through `278`, `280`, and `281` do not display this picture

## Requirement crosswalk

| Requirement | Evidence |
| --- | --- |
| Dedicated fictional Fallout art | Generated memorial census scene, no real person or archive claim |
| No Zombie reuse | Asset folder, sprite, and event references use the Fallout Names identity only |
| HOI4 report-event footprint | 210x176 RGBA preview and one-level uncompressed BGRA DDS |
| Engine registration | `interface/fallout_world_end.gfx` owns the sprite definition |
| Runtime path | `gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds` |
| Provenance | `provenance_prompt.md` and `manifest.json` retain source mode, prompt, and hashes |
| Review state | `manifest.json` records dimensions, alpha range, DDS header, and visual review |

## Processing and review

The approved `process_report_event_image.py` workflow produced the selected preview with a report-card crop, tilt, shadow, sepia tone, and grain. `convert_to_dds.py` produced the runtime DDS. The source, processed preview, DDS, handoff, provenance, and JSON manifest remain together until the wider Fallout implementation is complete.

Runtime testing was not claimed. The event chain is dormant, so live dispatch, multiplayer ownership, save recovery, and picture display remain unobserved.

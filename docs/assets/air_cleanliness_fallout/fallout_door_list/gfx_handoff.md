# The Door List report image GFX handoff

Status: generated, processed, converted, and ready for main-agent wiring.

## Sprite contract

| Field | Value |
| --- | --- |
| Proposed sprite | `GFX_report_event_fallout_door_list` |
| Target GFX file | `interface/fallout_world_end.gfx` |
| Final DDS | `gfx/event_pictures/fallout_door_list/report_event_fallout_door_list.dds` |
| Runtime canvas | `210x176` |
| Texture format | one-level uncompressed 32-bit BGRA DDS with alpha |
| Consumer | The Door List report/event image surface; parent implementation owns the exact event id and localisation wiring |
| Hidden AI | no player-facing picture |

Suggested definition for the main agent:

```text
spriteType = {
	name = "GFX_report_event_fallout_door_list"
	texturefile = "gfx/event_pictures/fallout_door_list/report_event_fallout_door_list.dds"
}
```

## Visual use notes

The image is a fictional alternate-history documentary report photograph: a numbered steel shelter door, an intentionally illegible household allocation list under a hooded lamp, chalked household tallies, and a compressed anonymous queue visible through the reinforced viewing slit. It contains no real person, flag, attested symbol, monster, gore, zombie reference, contemporary insignia, modern prop, readable text, generic skyline, UI artifact, or watermark.

## Evidence paths

- Source PNG: `docs/assets/air_cleanliness_fallout/fallout_door_list/source_png/report_event_fallout_door_list_source.png`
- Processed PNG: `docs/assets/air_cleanliness_fallout/fallout_door_list/processed_png/report_event_fallout_door_list.png`
- Review contact sheet: `docs/assets/air_cleanliness_fallout/fallout_door_list/contact_sheets/fallout_door_list_contact_sheet.png`
- Prompt and provenance: `docs/assets/air_cleanliness_fallout/fallout_door_list/prompts/report_event_fallout_door_list.md`
- Manifest: `docs/assets/air_cleanliness_fallout/fallout_door_list/manifest.json`

The asset subagent did not edit the target `.gfx` file. The main agent owns final sprite registration, event wiring, and player-facing localisation.

## SHA-256 evidence

| File | SHA-256 |
| --- | --- |
| `source_png/report_event_fallout_door_list_source.png` | `e28d6c10f9126e9a3aea937ad81c30a7552bae1392fa0c3a09f77a77f9b84eee` |
| `processed_png/report_event_fallout_door_list.png` | `ed32f7ee947ddacf4b88a8c124171be50d2ae49b89a23917c03961dc20cbf7c3` |
| `contact_sheets/fallout_door_list_contact_sheet.png` | `ba1f34244c8b617608bb5b9f8fbe1a81f6a4a189f20e80feb36b16c656296767` |
| `gfx/event_pictures/fallout_door_list/report_event_fallout_door_list.dds` | `74238abd190582e396b7dc29cea75f80c4629c908606a90e1d1e6497d9d702c7` |

## Remaining review

No production fallback was used. The parent/main agent should perform the final in-game visual review after copying the sprite definition into the existing `.gfx` surface.

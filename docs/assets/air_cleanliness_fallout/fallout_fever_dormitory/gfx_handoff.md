# Fever Dormitory report image GFX handoff

Status: generated, processed, converted, and ready for main-agent wiring.

## Sprite contract

| Field | Value |
| --- | --- |
| Stable sprite | `GFX_report_event_fallout_fever_dormitory` |
| Target GFX file | `interface/fallout_world_end.gfx` |
| Final DDS | `gfx/event_pictures/fallout_world_end/report_event_fallout_fever_dormitory.dds` |
| Runtime canvas | `210x176` |
| Texture format | one-level uncompressed 32-bit BGRA DDS with alpha |
| Consumer | Fever Dormitory Fallout report-event chain; parent implementation owns exact event id and callback surface |
| Hidden AI | no player-facing picture |

Suggested definition for the main agent:

```text
spriteType = {
	name = "GFX_report_event_fallout_fever_dormitory"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_fever_dormitory.dds"
}
```

## Visual use notes

The image is a fictional alternate-history documentary report photograph of a concrete shelter dormitory ward after ashfall: narrow iron bunks, anonymous patients under blankets, plain-clothed attendants with hand lamps, enamel wash basins, a stove and a curtained clinic doorway. It contains no identifiable real person, flag, attested symbol, contemporary insignia, modern prop, readable text, monster, gore, zombie reference, generic ruined skyline, UI artifact, or watermark.

## Evidence paths

- Source PNG: `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/source_png/report_event_fallout_fever_dormitory_source.png`
- Processed PNG: `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/processed_png/report_event_fallout_fever_dormitory.png`
- Review contact sheet: `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/contact_sheets/fallout_fever_dormitory_contact_sheet.png`
- Prompt and provenance: `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/prompts/report_event_fallout_fever_dormitory.md`
- Manifest: `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/manifest.json`

The asset subagent did not edit the target `.gfx` file. The main agent owns final sprite registration, event wiring, and player-facing localisation.

## Reuse boundary

This package intentionally reuses no Zombie ids, paths, assets, audio, sprites, or other Zombie-owned material.

## SHA-256 evidence

| File | SHA-256 |
| --- | --- |
| `source_png/report_event_fallout_fever_dormitory_source.png` | `8dea4b7e6a9f8d220ff848746bf8e3014516e72dcae5681df5c5af74f76256ea` |
| `processed_png/report_event_fallout_fever_dormitory.png` | `d01f57de096f15c1b455f925bfad44b3e89d721315abaf76a1286339c298f670` |
| `contact_sheets/fallout_fever_dormitory_contact_sheet.png` | `c01d12737e57aa4e50a576e384d277f1b96289b0c41e3722497dd767e07159dd` |
| `gfx/event_pictures/fallout_world_end/report_event_fallout_fever_dormitory.dds` | `5b7196a0540fc9acff0c3f2cc71a5a66a05bc9813d80e3775dcb0b51d66162e8` |

## Remaining review

No production fallback was used. The parent/main agent should perform final in-game visual review after copying the sprite definition into the existing `.gfx` surface.

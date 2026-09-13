# Event 31 report 04 visual repair handoff

Asset: `report_event_04_bomb_damaged_rail_bridge`

Owner: Event 31 Random Terror.

Producer: `chaosx_generated_event_art` using the official built-in ImageGen tool.

Scope: One bounded replacement of the inherited Event 31 report-art scene for accepted scene 1, damaged railway and civilian evacuation.

## Delivered files

| Surface | Final path | Status |
|---|---|---|
| Durable native ImageGen source | `docs/assets/031_random_terror/source_png/report_event_04_bomb_damaged_rail_bridge_source.png` | Generated, 1536x1024 RGB |
| Processed preview | `docs/assets/031_random_terror/processed_png/report_event_04_bomb_damaged_rail_bridge_processed.png` | Processed, 210x176 RGBA |
| Decoded DDS roundtrip | `docs/assets/031_random_terror/roundtrip/report_event_04_bomb_damaged_rail_bridge.png` | Pixel-equal to processed PNG |
| Runtime DDS | `gfx/event_pictures/031_random_terror/report_event_04_bomb_damaged_rail_bridge.dds` | Replaced, 210x176 legacy BGRA DDS |
| Native-size visual QA | `docs/assets/031_random_terror/review/report_event_04_bomb_damaged_rail_bridge_visual_qa.png` | Reviewed at source size and 3x nearest-neighbour card size |
| Validation record | `docs/assets/031_random_terror/review/report_event_04_bomb_damaged_rail_bridge_validation.md` | Current checks and verdicts |
| Exact prompt/output record | `docs/assets/031_random_terror/prompts/report_event_04_bomb_damaged_rail_bridge_generation_record.md` | Current ImageGen provenance |

The source SHA-256 is `C33C6599FC8BCEE81F5DE266F323548AE7BD568294EF67E57BC88FF4B76988B0`.

The processed PNG SHA-256 is `262B7B4973A79110AB4E8C7990FAC8FB44F644BAC25DD38914ADF917B43F5807`.

The runtime DDS SHA-256 is `EF29842214392FDC9A63AD362297CE4BFF41DB4B41E472B5803F7F79705089BA`.

## Visual result

The new fictional documentary source shows a broken masonry railway bridge with twisted rails and displaced sleepers on the left and middle, while civilians carrying luggage and blankets are guided along the embankment toward a period covered truck on the right by railway, relief, and security personnel.

The source is monochrome, period-authentic, non-graphic, and contains no readable text, watermark, modern prop, real extremist name or symbol, sacred hostile branding, propaganda flag, or UI artifact.

The processed card matches the inspected report family with a subtle four-degree tilt, soft shadow, sepia treatment, readable native-size composition, and transparent photo-card corners.

## Wiring handoff

Final DDS: `gfx/event_pictures/031_random_terror/report_event_04_bomb_damaged_rail_bridge.dds`.

Stable sprite proposal: `GFX_report_event_031_random_terror_04_bomb_damaged_rail_bridge`.

Target `.gfx`: the parent-owned Event 31 report-picture registry after the parent confirms the exact file and event-picture identifier; no `.gfx` file was edited in this bounded task.

Suggested sprite definition:

```text
spriteType = {
	name = "GFX_report_event_031_random_terror_04_bomb_damaged_rail_bridge"
	texturefile = "gfx/event_pictures/031_random_terror/report_event_04_bomb_damaged_rail_bridge.dds"
}
```

Consumer: Event 31 Random Terror report-event picture slot for damaged railway and civilian evacuation.

## Validation

The processed PNG is exactly 210x176 RGBA with alpha extrema `0..255` and alpha `0` at all four canvas corners.

The runtime DDS has `DDS ` magic, 124-byte header, 210x176 dimensions, pitch 840, pixel-format size 32, flags 65, fourCC 0, 32-bit BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, texture caps `0x1000`, mipmap count 0, and exact length `147968 = 128 + 210 * 176 * 4` bytes.

The decoded DDS roundtrip is 210x176 RGBA and pixel-equal to the processed PNG.

The source crop used the standard processor's 192x153 photo plane and retained approximately source coordinates x=120..1406 and y=0..1024 after the 229x153 cover resize, keeping the bridge break and evacuation group inside the safe composition.

The detailed evidence is `docs/assets/031_random_terror/review/report_event_04_bomb_damaged_rail_bridge_validation.md`.

## Review state and blockers

Worker visual review: accepted.

Parent final review: `needs_user_review`.

Parent-owned `.gfx` registration and live event consumer wiring remain pending because the exact Event 31 registry and runtime event-picture identifier were not supplied to this bounded asset task.

No blocker prevents the parent from wiring the replacement DDS by the stable basename and sprite proposal above.

The inherited aerial source was not reused and its temporary copied original was removed from `docs/assets/031_random_terror/source_png/`.

No gameplay, localisation, workbook, portrait, icon, flag, audio, GUI, 3D, custom-unit, or other report/news/super-event file was edited.

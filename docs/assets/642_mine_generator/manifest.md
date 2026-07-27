# Asset manifest: 642_mine_generator

## Requirement-to-runtime coverage

| Requirement ID | Accepted design source | Runtime purpose | Package entry | Runtime registration | Live consumer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `642-mine-generator-report` | Parent asset prompt for dormant Fallout Mine Generator tranche | Static report-event image for the generator settlement event | `report_event_fallout_mine_generator` | `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`, sprite `GFX_report_event_fallout_mine_generator` | Events `642`, `644`, and `646` | `wired_static_pending_runtime` |

## Asset entry

### `report_event_fallout_mine_generator`

- Related event id: `642`.
- Related event slug: `mine_generator`.
- Asset type: Report event image.
- Intended in-game use: Static report-event picture for the dormant Fallout Mine Generator tranche.
- Source mode: `$imagegen` generated fictional alternate-history documentary scene.
- Generation fit: The settlement, ration ledger, guarded generator, and scarcity are invented and have no required real historical source. Generation provided the specific composition needed by the event.
- Identity classification: Not a portrait. No real person or named identity is depicted.
- Prompt: `prompts/report_event_fallout_mine_generator_prompt.txt`.
- ImageGen source handle/path: Built-in ImageGen output `019fa327-8d50-7fb0-8973-df266879c9ba/exec-630fe42c-6bd9-49ee-aeee-90058398de00.png`, copied into the package as the immutable source PNG.
- Source PNG: `source_png/report_event_fallout_mine_generator_source.png`.
- Processed PNG preview: `processed_png/report_event_fallout_mine_generator.png`.
- Review contact sheet: `contact_sheets/report_event_fallout_mine_generator_contact_sheet.png`.
- DDS decode inspection: `processed_png/report_event_fallout_mine_generator_dds_decode.png`.
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`.
- Target size: `210x176`.
- Sprite name: `GFX_report_event_fallout_mine_generator`.
- Registered `.gfx` file: `interface/fallout_world_end.gfx`.
- Related event or UI element: Dormant Fallout Mine Generator report events `642`, `644`, and `646`.
- Report-card treatment: Repository `process_report_event_image.py`. Final canvas is RGBA with transparent corners and edge space, subtle tilt and soft shadow, monochrome plus restrained sepia, grain, and paper border.
- Visual inspection: Source read clearly as a guarded industrial generator shed, ore carts and stockpiles, workers at the ledger, and sparse food stores. No readable text, flags, logos, zombies, gore, or modern branding were observed. Processed preview retains the scene at report-card scale with transparent edge treatment.
- Status: `wired_static_pending_runtime` with `.gfx` registration and event consumers present. Live presentation remains user-owned validation.
- Notes: Static only. No animation or audio requested or produced.

## Validation evidence

- Processed PNG dimensions: `210x176`.
- Processed PNG mode: RGBA.
- Processed PNG corner alpha: transparent at all four corners.
- DDS format: one-level uncompressed 32-bit BGRA with repository converter and `210x176` dimensions.
- DDS runtime path is outside `docs/assets/`. The package and runtime DDS hashes match byte for byte.

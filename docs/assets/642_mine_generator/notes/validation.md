# Validation evidence

The generated source and processed card were visually inspected with the repository image viewer.

The source shows the requested ash-dimmed mining settlement, corrugated generator shed, guarded machinery, ore carts and stockpiles, workers around an unmarked ration ledger, and sparse food stores.

The processed preview keeps the scene readable at `210x176`, applies the repository report-card tilt, soft shadow, grain, restrained sepia, and transparent edge treatment, and contains no readable text, flags, branding, zombies, or gore.

The DDS was decoded with Pillow as `RGBA 210x176` and visually matched the processed preview.

## PNG checks

- Processed mode: `RGBA`.
- Processed size: `210x176`.
- Corner alpha values: `0, 0, 0, 0`.
- Alpha range: `0..255`.

## DDS header checks

- Magic: `DDS `.
- Header size: `124`.
- Declared dimensions: `210x176`.
- Pixel format size: `32`.
- Pixel format flags: `65` (`RGB | ALPHAPIXELS`).
- FourCC: `0`.
- Bit count: `32`.
- BGRA masks: `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`.
- Texture caps: `0x1000`.
- Exact file length: `147968` bytes (`128 + 210 * 176 * 4`).

## SHA-256

- `source_png/report_event_fallout_mine_generator_source.png`: `49ea5b72886d4b55de552a0e1fc1b4dcce68c7188733bf368b97aaeedb2c36f4`.
- `processed_png/report_event_fallout_mine_generator.png`: `f6009c921689291e952f197391f46d45f52120838beb359ee9d7d0fa29921271`.
- `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds`: `fa95b93840cc9003c4ff101e9c014b76486e4cc34f13940a6772f1d1af8d1da0`.

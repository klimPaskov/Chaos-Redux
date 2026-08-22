# Mapmode icon artist handoff

## Delivered

This follow-up delivers exactly two dedicated scripted-mapmode button families with selected and deselected variants.

- `famine_state_map_mode`: grain sheaf and empty ration bowl motif.
- `migration_state_map_mode`: adult and child travelers with luggage and route motif.

The four runtime DDS files are:

- `gfx/interface/mapmode/custom/famine_state_map_mode_selected.dds`
- `gfx/interface/mapmode/custom/famine_state_map_mode_deselected.dds`
- `gfx/interface/mapmode/custom/migration_state_map_mode_selected.dds`
- `gfx/interface/mapmode/custom/migration_state_map_mode_deselected.dds`

The parent-owned consumer sprite IDs are:

- `GFX_mapmode_buttons_selected_small_famine_state_map_mode`
- `GFX_mapmode_buttons_deselected_small_famine_state_map_mode`
- `GFX_mapmode_buttons_selected_small_migration_state_map_mode`
- `GFX_mapmode_buttons_deselected_small_migration_state_map_mode`

The parent owns adding those four sprite definitions to `interface/mapmodes_interface.gfx` and pointing the two mapmode definitions at the IDs above.

## Source and evidence files

The four untouched ImageGen source PNGs are retained under `docs/assets/famine_and_migration_system/mapmode/source/`.

The exact processed 20x18 RGBA previews are under `docs/assets/famine_and_migration_system/mapmode/processed/`.

DDS-decoded round-trip previews are under `docs/assets/famine_and_migration_system/mapmode/dds_roundtrip/`.

The source/processed contact sheet is `docs/assets/famine_and_migration_system/mapmode/contact_sheets/mapmode_icons_source_processed.png`.

The final DDS round-trip contact sheet is `docs/assets/famine_and_migration_system/mapmode/contact_sheets/mapmode_icons_dds_roundtrip_12x.png`.

The inspected reference contact sheet is `docs/assets/famine_and_migration_system/mapmode/reference/reference_contact_sheet.png`.

The complete manifest is `docs/assets/famine_and_migration_system/mapmode/manifest.csv`.

The generation and reference record is `docs/assets/famine_and_migration_system/mapmode/prompts/imagegen_source_log.md`.

The machine-readable validation record is `docs/assets/famine_and_migration_system/mapmode/validation.json`.

## Dimensions, alpha, compression, and generation evidence

Each final DDS is exactly 20x18 pixels, one level, legacy uncompressed BGRA8, with no mipmaps and a 1568-byte file length, matching the installed custom mapmode precedent.

Each source request explicitly required genuine native transparent background, and no background-removal fallback was used.

The processed previews preserve native alpha on a transparent canvas, with each symbol fitted into an 18x16 safe area and centered on the 20x18 consumer canvas.

Selected and deselected states were generated as separate original variants so state treatment is not a transform-only recolor or offset mockup.

The famine family is intentionally wheat/empty-bowl rather than deaths, contamination, Air Winter, or a generic warning symbol.

The migration family is intentionally people/luggage/route rather than famine grain, deaths, contamination, Air Winter, or a generic arrow.

Reference inspection covered the installed vanilla 19-frame 20x18 selected/deselected strips and the installed custom `deaths_state_map_mode`, `contaminated_states_map_mode`, and `air_winter_state_map_mode` one-frame 20x18 DDS pairs before production.

## Validation

All four DDS headers validate as 20x18 legacy BGRA8 with the expected channel masks, one level, and no mipmaps.

All four outputs have alpha range 0-255 and retain transparent unused canvas.

The decoded DDS pixel payload matches its processed RGBA PNG byte-for-byte for all four outputs.

Visual inspection evidence is retained in the two new contact sheets.

## Ownership and blockers

No GFX, mapmode script, localisation, gameplay, or unrelated files were edited.

No shared strip frame, optional deaths icon, portrait, flag, model, animation, or scripted GUI was created.

No blocker remains for the asset package.

Current source contains the four mapmode sprite registrations, while live GUI/render consumer validation remains intentionally pending under the parent-owned scope.

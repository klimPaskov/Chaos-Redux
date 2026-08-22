# Famine and Migration Generated Report-Art Manifest

Status: handed_off. This package contains the complete seven-row generated report-image family accepted by `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_asset_matrix.csv`. The main agent owns final `.gfx` registration and event/report wiring.

Source mode: generated with the official built-in ImageGen workflow. Generation fits because the accepted rows are fictional or dynamic shared-system incidents and do not require a specific real photograph, named person, or identifiable historical victim. The wartime evacuation row is generated period documentary art rather than archival sourcing because the matrix permits either mode and no exact historical image is required. The nuclear evacuation row is alternate-history documentary art.

Reference evidence: the matching canonical family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/` was inspected, including `contact_sheet.png`, `report_event_001.png`, `report_event_african_soldiers.png`, `report_event_airplane_crash.png`, `report_event_soldiers_marching.png`, and `report_event_soldiers_parade.png`. The installed vanilla report family and current Chaos Redux report consumers use the `210x176` report canvas with transparent card margins; the event report window displays the sprite through the report-picture slot. Existing repository report packages use the same processor profile recorded below.

## Runtime crosswalk

| Matrix ID | Runtime role | Source PNG | Processed PNG | Final DDS | Proposed sprite | Target `.gfx` | Size | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fm_report_generic_famine` | first famine report | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_generic_famine_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_generic_famine.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds` | `GFX_report_event_famine_migration_generic_famine` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_island_blockade` | island famine | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_island_blockade_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_island_blockade.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds` | `GFX_report_event_famine_migration_island_blockade` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_wartime_evacuation` | organized evacuation | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_wartime_evacuation_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_wartime_evacuation.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds` | `GFX_report_event_famine_migration_wartime_evacuation` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_closed_border` | trapped population | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_closed_border_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_closed_border.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds` | `GFX_report_event_famine_migration_closed_border` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_relief_arrival` | relief success | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_relief_arrival_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_relief_arrival.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds` | `GFX_report_event_famine_migration_relief_arrival` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_nuclear_evacuation` | nuclear survivor movement | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_nuclear_evacuation_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_nuclear_evacuation.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds` | `GFX_report_event_famine_migration_nuclear_evacuation` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |
| `fm_report_return` | voluntary return | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_return_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_return.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds` | `GFX_report_event_famine_migration_return` | `interface/famine_and_migration_system_event_pictures.gfx` | 210x176 | handed_off |

## Prompt and processing records

The exact generation prompts, seeds, source-mode rationale, and the safety-filter wording correction for the closed-border row are retained in `docs/assets/famine_and_migration_system/report_art/prompts/prompts.md`.

Each source is an untouched `1536x1024` RGB PNG. Each processed preview was made by `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` with `--canvas-size 210x176 --card-size 192x153 --border 2 --angle 3 --shadow-offset 4 5 --shadow-blur 4.5 --shadow-opacity 0.50 --grain 7 --paper-grain 2 --rotate-supersample 4 --edge-soften 0.35` and the row-specific seed in `prompts/prompts.md`. This creates the inspected vanilla-style sepia report card, transparent corners, soft shadow, and antialiased tilted card edge.

Each final DDS was created from its processed PNG with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 210 --height 176`. The outputs are one-level legacy uncompressed 32-bit BGRA DDS files with no mipmaps, `DDS_PIXELFORMAT` flags `65`, fourCC `0`, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, and exact file length `147968` bytes. Decoded DDS payloads match their processed PNGs byte-for-byte after RGBA-to-BGRA channel order conversion.

## Hashes and QA

| Matrix ID | Source SHA-256 | Processed SHA-256 | DDS SHA-256 | Processed alpha | Visible alpha bounds |
| --- | --- | --- | --- | --- | --- |
| `fm_report_generic_famine` | `349ec66bb5efcaa5cd61074900e0691f12ccd64407a1c155364f82747fcedb50` | `e1ed632a80cc9431d173e6ed62cbbee89811ea5a960344531cf3d4b52c80094f` | `c9ecb00e7990a9155286880b22894b354c299f1828249c49857403d765d7e565` | 0-255 | 5,6..208,173 |
| `fm_report_island_blockade` | `cafa7c6d903f98e257ad5ad4131d71d8a8c865bc9599e16cd4e53fcc1477a539` | `d74997e2369c80830b82d93e3bfc13b2ff584fa7e2fe305f06bb1cc78e755def` | `f35662e6e2e504af561e92309b770d1db4bdd9adb3c75eb3325c2480470d6e65` | 0-255 | 5,6..208,173 |
| `fm_report_wartime_evacuation` | `a20a70653c95b54fdb6606092e0673f891040389a7c6a9aa91780105e3490835` | `0b7101196bb48fd7ede2e079e28d0628c8b53e24f2bc16828526953b3b5c7bd2` | `a6c825dd48c994a6434f47e8dbd6972c39f3487aeaf591459faaccf7681c8c85` | 0-255 | 5,6..208,173 |
| `fm_report_closed_border` | `bb149f122e37b1c25a1c09421755d9fcc73218753ea10aa82c1483d23dd80d5a` | `5609173089854ba326e5e1cca13e33f4a3a1b41414758867a9a32621891a4384` | `ff6216908e680ead3a1a25e0d97386d8afac68ca198d0086350358439572bd7a` | 0-255 | 5,6..208,173 |
| `fm_report_relief_arrival` | `dcdec0bc7cfd349f73d6a1b5da1b79f27244c94d4edbb1c9203f9c0ceee23ad6` | `18efd7ce51fc3199edbb8805fbb761434cb5aea4db8e6b254a0a178db875a3a8` | `1fe919b80e5634ddc55b05d980b0d4919408666b9a05cf594f53ac7ce88fa8c5` | 0-255 | 5,6..208,173 |
| `fm_report_nuclear_evacuation` | `5bfc5b05146557d721c1699a852e2651f39d856fa42e6f527b4e0d67713c6d79` | `995140c4a4a740cfcaa2c8f1fe3377dc4b7da41a3405ac7f65989e60ff297a7c` | `8602ac4e3d80f6bc42ad6ef99f940a5b8020bea56f5bc4b4d714466a24225374` | 0-255 | 5,6..208,173 |
| `fm_report_return` | `90d2da0d8f22f9521332e1a173cb2585c9ffe11c888680155660657d401e8ed3` | `49f1ff838198adb0980e43ea593e1d0d1a0a97bdef2f676a4f068e7f42f18bdb` | `456ed6c3d9af7a84e973fe339ec7adcd5925845a81dd758eac147c8ac8df9b37` | 0-255 | 5,6..208,173 |

The processed-family review sheet is `docs/assets/famine_and_migration_system/report_art/contact_sheets/report_art_contact_sheet.png`. All seven cards show period clothing and technology, distinct scene identity, no readable generated text, no modern props, no graphic injury, and clear readable action at the native report footprint.

## Parent wiring handoff

Ready-to-copy sprite definitions for the parent are:

```text
spriteType = { name = "GFX_report_event_famine_migration_generic_famine" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds" }
spriteType = { name = "GFX_report_event_famine_migration_island_blockade" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds" }
spriteType = { name = "GFX_report_event_famine_migration_wartime_evacuation" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds" }
spriteType = { name = "GFX_report_event_famine_migration_closed_border" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds" }
spriteType = { name = "GFX_report_event_famine_migration_relief_arrival" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds" }
spriteType = { name = "GFX_report_event_famine_migration_nuclear_evacuation" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds" }
spriteType = { name = "GFX_report_event_famine_migration_return" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds" }
```

No event IDs, localisation keys, `.gfx` edits, gameplay files, decisions, GUIs, flags, portraits, super-event art, or animation were changed. The proposed `.gfx` filename is a stable handoff suggestion; the parent may use an existing shared-system picture registry if one is selected before wiring.

## Blockers and review gates

No asset is blocked. Final user-side in-game visual approval and parent-owned `.gfx`/event consumer wiring remain open integration gates. The exact event IDs and consumer branches were not supplied to this asset worker, so this package does not invent them.

# Famine and Migration Generated Event-Art Handoff

Status: complete for the seven accepted generated report-image rows and the follow-up `fm_pic_displacement` decision-category picture. Parent owns `.gfx` registration, event IDs, localisation, decision-category wiring, and final runtime wiring. No gameplay, localisation, GUI, event, decision, focus, country, spreadsheet, flag, portrait, super-event, animation, or `.gfx` file was edited.

## Completed family

| Matrix ID | Scene | Source PNG | Processed PNG | Final DDS | Sprite proposal | Target `.gfx` |
| --- | --- | --- | --- | --- | --- | --- |
| `fm_report_generic_famine` | ration line, closed grain store, relief workers | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_generic_famine_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_generic_famine.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds` | `GFX_report_event_famine_migration_generic_famine` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_island_blockade` | damaged island port, idle cranes, waiting relief line | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_island_blockade_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_island_blockade.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds` | `GFX_report_event_famine_migration_island_blockade` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_wartime_evacuation` | organized railway evacuation with families and luggage | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_wartime_evacuation_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_wartime_evacuation.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds` | `GFX_report_event_famine_migration_wartime_evacuation` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_closed_border` | frontier gate, waiting travelers, sentries | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_closed_border_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_closed_border.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds` | `GFX_report_event_famine_migration_closed_border` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_relief_arrival` | grain unloading and local distribution after crisis | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_relief_arrival_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_relief_arrival.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds` | `GFX_report_event_famine_migration_relief_arrival` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_nuclear_evacuation` | alternate-history ash aftermath and organized medical evacuation | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_nuclear_evacuation_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_nuclear_evacuation.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds` | `GFX_report_event_famine_migration_nuclear_evacuation` | `interface/famine_and_migration_system_event_pictures.gfx` |
| `fm_report_return` | returning families, train arrival, station repair | `docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_return_source.png` | `docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_return.png` | `gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds` | `GFX_report_event_famine_migration_return` | `interface/famine_and_migration_system_event_pictures.gfx` |

Exact ImageGen prompts, seeds, source-mode reasoning, and the one safety-filter wording correction are at `docs/assets/famine_and_migration_system/report_art/prompts/prompts.md`. Per-row hashes, status, reference evidence, and the full manifest are at `docs/assets/famine_and_migration_system/report_art/manifest.md`.

## Decision-category picture follow-up

The missing matrix row `fm_pic_displacement` is complete as a distinct opaque 114×101 generated scene. It depicts a period wartime railway reception and relief station with civilians, luggage, relief staff, handcarts, crates, and a steam locomotive, with no readable text, flags, modern objects, interface artifacts, portraits, or graphic injury.

| Matrix ID | Source PNG | Processed PNG | Final DDS | Sprite proposal | Target `.gfx` |
| --- | --- | --- | --- | --- | --- |
| `fm_pic_displacement` | `docs/assets/famine_and_migration_system/category_picture/source_png/fm_pic_displacement_source.png` | `docs/assets/famine_and_migration_system/category_picture/processed_png/fm_pic_displacement.png` | `gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds` | `GFX_fm_pic_displacement` | `interface/famine_and_migration_system.gfx` |

The exact native ImageGen prompt, generation record, source mode, and processing recipe are at `docs/assets/famine_and_migration_system/category_picture/prompts/prompts.md`. The manifest, hashes, reference-family evidence, dimensions, DDS settings, and validation contract are at `docs/assets/famine_and_migration_system/category_picture/manifest.md`. The parent copy-ready sprite handoff is at `docs/assets/famine_and_migration_system/category_picture/gfx_handoff.md`.

The canonical matching family `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/` was inspected through its 13-reference contact sheet. Installed vanilla `interface/decisions.gfx` uses `GFX_decision_cat_*` sprites for this 114×101 picture surface. Chaos Redux's existing package path and registry are `gfx/interface/decisions/famine_and_migration_system/` and `interface/famine_and_migration_system.gfx`; the existing `GFX_fm_cat_displacement` remains the separate 52×40 category icon.

The processed PNG is 114×101 RGBA with alpha fixed at 255. Conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 114 --height 101`. The final DDS is a 46,184-byte legacy 32-bit BGRA8 file with no mipmaps, flags 65, fourCC 0, canonical BGRA masks, and `DDSCAPS_TEXTURE` `0x1000`. DDS payload comparison against the processed PNG after RGBA-to-BGRA ordering reported zero mismatches. Review sheet: `docs/assets/famine_and_migration_system/category_picture/contact_sheets/category_picture_contact_sheet.png`.

## Reference-family and consumer evidence

The canonical report family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/` was inspected before generation, including its labeled contact sheet and five report PNGs. The matching family uses a 210x176 report canvas with an opaque sepia photograph card on transparent margins and a soft shadow/tilt presentation.

The installed vanilla report event consumer is `interface/eventwindow.gui`, where the report picture slot displays a `210x176` sprite. Vanilla `interface/eventpictures.gfx` names report sprites with `GFX_report_event_*` and points them to `gfx/event_pictures/report_event_*.dds`. Chaos Redux follows the established event-scoped folder convention in `interface/chaosx_pictures.gfx` and existing per-package picture registries; the proposed shared-system target is `interface/famine_and_migration_system_event_pictures.gfx`.

The source masters are 1536x1024 landscape photographs so the processor can cover-crop without losing scene identity. Processing uses `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` with `canvas 210x176`, `card 192x153`, `border 2`, `angle 3`, `shadow offset 4,5`, `shadow blur 4.5`, `shadow opacity 0.50`, `grain 7`, `paper grain 2`, `supersample 4`, `edge soften 0.35`, and seeds 7301–7307. Each processed PNG is RGBA with alpha range 0–255, transparent corner, and visible alpha bounds 5,6..208,173.

## DDS conversion and validation

All final DDS files were made from the processed PNGs with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 210 --height 176`. They are one-level uncompressed 32-bit BGRA DDS files with no mipmaps, legacy 124-byte header, pixel-format size 32, flags 65, fourCC 0, bit count 32, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, exact total length `147968`, and alpha bytes 0–255. A local validation pass checked all seven headers, dimensions, lengths, alpha ranges, and decoded payload equality against the processed PNGs after RGBA-to-BGRA ordering.

Review contact sheet: `docs/assets/famine_and_migration_system/report_art/contact_sheets/report_art_contact_sheet.png`. It shows all seven processed cards at enlarged scale over a checkerboard transparency background with native dimensions in the labels.

## Ready-to-copy sprite definitions

```text
spriteType = { name = "GFX_report_event_famine_migration_generic_famine" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds" }
spriteType = { name = "GFX_report_event_famine_migration_island_blockade" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds" }
spriteType = { name = "GFX_report_event_famine_migration_wartime_evacuation" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds" }
spriteType = { name = "GFX_report_event_famine_migration_closed_border" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds" }
spriteType = { name = "GFX_report_event_famine_migration_relief_arrival" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds" }
spriteType = { name = "GFX_report_event_famine_migration_nuclear_evacuation" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds" }
spriteType = { name = "GFX_report_event_famine_migration_return" texturefile = "gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds" }
```

## Blockers and parent follow-up

No requested generated report or category-picture asset is blocked. Parent must add the seven report sprite definitions and the `GFX_fm_pic_displacement` sprite to the selected shared-system `.gfx` file, then bind report-event consumers and the decision category's `picture` field. Exact event IDs and branches were not supplied to this worker, so none are invented here. Final in-game visual approval remains a user-side gate.

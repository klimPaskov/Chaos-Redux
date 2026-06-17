# Event 012 Africa Super-Event Variant Images Handoff

Date: `2026-06-17`
Scope: final candidate image packages only for the two remaining requested Event 012 Africa variant super-events
Authoring mode: generated image asset package only; no `.gfx`, localisation, event, sound, music, GUI, or gameplay edits

## Files changed

- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/source_png/super_event_012_root_and_fang_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/source_png/super_event_012_archive_world_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_root_and_fang_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_archive_world_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/dds/super_event_012_root_and_fang.dds`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/dds/super_event_012_archive_world.dds`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/contact_sheets/root_and_fang_alternatives_source_contact_sheet.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/contact_sheets/archive_world_alternatives_source_contact_sheet.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/contact_sheets/variant_images_batch_root_archive_overview.png`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/manifest.md`
- `docs/assets/012_africa/super_events/variant_images_batch_root_archive/gfx_handoff.md`
- `gfx/super_events/super_event_012_root_and_fang.dds`
- `gfx/super_events/super_event_012_archive_world.dds`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_super_event_variant_images_root_archive_handoff.md`

## Deliverable summary

- Produced one final candidate source PNG, one processed PNG, one package DDS copy, and one live DDS file for each requested role.
- Preserved multi-variant generation evidence through separate root-and-fang and archive-world alternative contact sheets.
- Added a combined overview sheet showing both alternative boards and the selected finals side by side.

## Final asset mapping

| Role | Final source PNG | Final processed PNG | Live DDS |
| --- | --- | --- | --- |
| Parliament of Root and Fang escalation | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/source_png/super_event_012_root_and_fang_source.png` | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_root_and_fang_processed.png` | `gfx/super_events/super_event_012_root_and_fang.dds` |
| Archive-world union terminal | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/source_png/super_event_012_archive_world_source.png` | `docs/assets/012_africa/super_events/variant_images_batch_root_archive/processed_png/super_event_012_archive_world_processed.png` | `gfx/super_events/super_event_012_archive_world.dds` |

## Source and generation notes

- Source mode for both roles: generated with built-in `image_gen`
- Root-and-fang direction: solemn constitutional animal/human parliament under root and tusk architecture; no real faces, no copied sacred regalia, no joke framing
- Archive-world direction: old seats and legal archive expanded into global sovereignty through globe, world table, seals, ledgers, shelves, and a terminal congress atmosphere; no generic office imagery
- Both packages include separate 2x2 alternative boards retained as contact-sheet artifacts

## Dimensions and conversion

- All final super-event outputs were matched to the existing Event 012 super-event format: `457x328`
- Conversion workflow:

```bash
convert <source>.png -filter Lanczos -resize 457x328^ -gravity center -crop 457x328+0+0 +repage <processed>.png
convert <processed>.png <asset>.dds
cp <asset>.dds gfx/super_events/<asset>.dds
```

## Validation

- Existing Event 012 super-event DDS files were inspected first to match target dimensions and general presentation.
- Processed PNG validation:
  - `super_event_012_root_and_fang_processed.png` -> `457x328`
  - `super_event_012_archive_world_processed.png` -> `457x328`
- DDS validation:
  - package DDS copies and live DDS files are `457x328`
  - `file` reports the DDS outputs as Microsoft DirectDraw Surface files compressed using DX10
- Human review sheet:
  - `docs/assets/012_africa/super_events/variant_images_batch_root_archive/contact_sheets/variant_images_batch_root_archive_overview.png`

## Risks

- These are final candidates, not source-historical images. That is correct for the brief, but they still depend on parent acceptance for slot wiring.
- The archive-world final contains decorative pseudo-script on foreground documents and hanging records. It is not readable text at gameplay scale, but it remains the main artifact risk if the parent wants an even cleaner archival surface.
- The root-and-fang final is intentionally crowded to sell parliament scale. If the parent later wants fewer delegates and a stronger throne/dais focal point, regenerate from the saved alternative board rather than stretching this crop.

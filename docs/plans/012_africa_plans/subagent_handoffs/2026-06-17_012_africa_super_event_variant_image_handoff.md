# Event 012 Africa Variant Super-Event Image Handoff

Date: `2026-06-17`
Scope: final candidate image assets for Forest Parliament reveal and World Root Mandate only
Authoring mode: generated image asset handoff only; no `.gfx`, localisation, event, sound, or gameplay edits

## Files changed

- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/manifest.md`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/gfx_handoff.md`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/forest_parliament_candidate_a_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/forest_parliament_candidate_b_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/world_root_mandate_candidate_a_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/world_root_mandate_candidate_b_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/super_event_012_forest_parliament_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/super_event_012_world_root_mandate_source.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/forest_parliament_candidate_a_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/forest_parliament_candidate_b_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/world_root_mandate_candidate_a_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/world_root_mandate_candidate_b_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_forest_parliament_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_world_root_mandate_processed.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/dds/super_event_012_forest_parliament.dds`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/dds/super_event_012_world_root_mandate.dds`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/source_candidates_contact_sheet.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/processed_candidates_contact_sheet.png`
- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/final_candidates_contact_sheet.png`
- `gfx/super_events/super_event_012_forest_parliament.dds`
- `gfx/super_events/super_event_012_world_root_mandate.dds`

## Output summary

Delivered a new scoped asset package under:

- `docs/assets/012_africa/super_events/variant_images_batch_forest_root/`

Delivered live DDS files with the exact requested filenames:

- `gfx/super_events/super_event_012_forest_parliament.dds`
- `gfx/super_events/super_event_012_world_root_mandate.dds`

## Source and generation notes

- Source mode for both roles: generated with built-in `$imagegen`
- Why generation is appropriate: both requested roles are fictional, symbolic, high-chaos super-event scenes with no requirement to depict a real photographed person, object, or archive image
- Variants generated: `2` Forest Parliament candidates and `2` World Root Mandate candidates
- Selected finals:
  - Forest Parliament: `forest_parliament_candidate_a`
  - World Root Mandate: `world_root_mandate_candidate_b`

## Dimensions and format

- Existing Event 012 super-event DDS references inspected first:
  - all current live Event 012 super-event DDS files are `457x328`
  - existing live files identify as `sRGB` DDS with `DXT1` compression
- Final outputs match that pattern:
  - `super_event_012_forest_parliament.dds`: `457x328`, `sRGB`, `DXT1`
  - `super_event_012_world_root_mandate.dds`: `457x328`, `sRGB`, `DXT1`

## Conversion commands

Processed PNG:

```bash
convert <source>.png \
  -resize '457x328^' \
  -gravity center \
  -crop 457x328+0+0 +repage \
  -colorspace sRGB \
  -contrast-stretch 0.3%x0.3% \
  -modulate 100,92,100 \
  -unsharp 0x0.8+0.5+0.02 \
  <processed>.png
```

DDS:

```bash
convert <processed>.png -define dds:compression=dxt1 <output>.dds
```

## Validation

- `identify` confirmed:
  - source finals at `1480x1063` and `1479x1063`
  - processed finals at `457x328`
  - live DDS files at `457x328`
- `identify -verbose` on the live DDS files reports:
  - `Colorspace: sRGB`
  - `Compression: DXT1`
- `file` reports both live DDS files as Microsoft DirectDraw Surface images at `457 x 328`
- Contact sheets were produced for all source candidates, all processed candidates, and the selected final pair

## Risks

- Forest Parliament is readable and solemn, but the nonhuman delegates are visually overt. Keep any future presentation text and music in the same grave register to avoid tonal mismatch.
- World Root Mandate avoids readable generated text, but it still uses a symbolic stitched map surface in the foreground rather than a literal document archive photograph. This fits the route brief better than the rejected text-heavy variant, but it remains overtly symbolic.

## Blockers

- None for the scoped image package itself.
- This pass does not resolve parent wiring for `.gfx`, slot assignment, or gameplay callsites.

# Event 012 Africa Counterfeit Crowns Super-Event Image Manifest

Date: `2026-06-18`
Event id: `012`
Event slug: `africa`
Package root: `docs/assets/012_africa/super_events/counterfeit_crowns_image/`
Source mode: generated with built-in `image_gen`
Status: `handed_off`

## Scope

This package creates the missing generated super-event image for Event 012 Africa slot 71, `Counterfeit Crowns`.

Generation is appropriate because the requested scene is fictional, symbolic, alternate-history, and tribunal-staged rather than a depiction of a real historical photograph, real person, or sourced archive artifact.

## Asset

### `super_event_012_counterfeit_crowns`

- Asset type: super-event image
- Intended in-game use: Event 012 Africa slot 71 super-event image for `Counterfeit Crowns`
- Source mode: built-in `image_gen`
- Source note: generated after reviewing the super-event reference folder and the current Event 012 archive/bestiary art so the result would stay ledger/tribunal-focused and avoid animals
- Prompt summary: dark 1930s-1940s documentary-painterly tribunal exposing forged dynasties, with tarnished crowns, broken seals, blank lineage charts, shadowed witnesses, colonial archive shelves, and a single harsh lamp; no animals, no map focus, no readable text, no real people, no modern props
- Selected source PNG: `source_png/counterfeit_crowns_alt3_source.png`
- Alternate source PNGs:
  - `source_png/counterfeit_crowns_alt1_source.png`
  - `source_png/counterfeit_crowns_alt2_source.png`
- Processed PNG: `processed_png/super_event_012_counterfeit_crowns_processed.png`
- Package DDS: `dds/super_event_012_counterfeit_crowns.dds`
- Final DDS: `gfx/super_events/super_event_012_counterfeit_crowns.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_012_counterfeit_crowns`
- Suggested `.gfx` file: `interface/012_africa.gfx`
- Related super-event slot: `71`
- Contact sheet:
  - `contact_sheets/counterfeit_crowns_alternatives_source_contact_sheet.png`
- Processing command:

```bash
convert source_png/counterfeit_crowns_alt3_source.png \
  -filter Lanczos -resize 457x328^ -gravity center -crop 457x328+0+0 +repage \
  -brightness-contrast 3x7 -unsharp 0x0.6 \
  processed_png/super_event_012_counterfeit_crowns_processed.png
convert processed_png/super_event_012_counterfeit_crowns_processed.png \
  dds/super_event_012_counterfeit_crowns.dds
cp dds/super_event_012_counterfeit_crowns.dds \
  gfx/super_events/super_event_012_counterfeit_crowns.dds
```

- Asset status: `converted`
- Notes: the selected frame keeps witnesses in shadow, uses blank lineage boxes instead of readable writing, and centers the broken regalia table so it reads differently from the current animal/archive Bestiary image

## Shared validation

- Reference folder inspected:
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/`
- Existing Event 012 comparison target inspected:
  - `docs/assets/012_africa/generated_art/processed_png/super_event_012_archive_bestiary_candidate_processed.png`
- Dimension check:
  - processed PNG is `457x328`
  - package DDS is `457x328`
  - live DDS is `457x328`
- Non-blank check:
  - processed PNG bounding box is `(0, 0, 457, 328)`
  - package DDS bounding box is `(0, 0, 457, 328)`
  - processed PNG mean RGB is `37.79, 27.79, 16.88`
  - package DDS mean RGB is `36.78, 27.32, 16.67`
- DDS/file check:
  - `file` reports both DDS copies as Microsoft DirectDraw Surface files compressed using DX10

## Risks

- Alternative 1 and 2 contain more visible pseudo-document detail and more directly lit faces, so they were kept only as review alternatives.
- The final frame still uses stylized blank pedigree charts as props. They are intentionally unreadable at source and final size, but the parent should avoid zoomed promo use without review.

# Event 012 Africa Variant Super-Event Image Manifest

Date: `2026-06-17`
Event id: `012`
Event slug: `africa`
Package root: `docs/assets/012_africa/super_events/variant_images_batch_root_archive/`
Source mode: generated with built-in `image_gen`
Status: `handed_off`

## Scope

This package covers the two missing fictional/high-chaos Event 012 Africa super-event image roles requested in the parent prompt:

- `Parliament of Root and Fang` escalation
- `Archive-world union terminal`

Generation is appropriate for both because the scenes are fictional, symbolic, constitutional, and alternate-terminal rather than depictions of real archival people or historical photographs.

## Assets

### `super_event_012_root_and_fang`

- Asset type: super-event image
- Intended in-game use: Event 012 Africa late high-chaos escalation for the Parliament of Root and Fang route
- Source mode: built-in `image_gen`
- Source note: generated fictional ceremonial parliament scene after reviewing Event 012 super-event DDS patterns and the skill super-event reference folder
- Prompt summary: solemn uncanny constitutional chamber where living roots, carved benches, fang/tusk legal architecture, animal heralds, and human charter-keepers share one parliament; no readable text, no real people, no modern symbols, no comic tone
- Source PNG: `source_png/super_event_012_root_and_fang_source.png`
- Processed PNG: `processed_png/super_event_012_root_and_fang_processed.png`
- Package DDS: `dds/super_event_012_root_and_fang.dds`
- Final DDS: `gfx/super_events/super_event_012_root_and_fang.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_012_root_and_fang`
- Suggested `.gfx` file: `interface/012_africa.gfx`
- Related super-event role: `parliament of root and fang escalation`
- Contact-sheet sources:
  - `contact_sheets/root_and_fang_alternatives_source_contact_sheet.png`
  - `contact_sheets/variant_images_batch_root_archive_overview.png`
- Processing command:

```bash
convert source_png/super_event_012_root_and_fang_source.png \
  -filter Lanczos -resize 457x328^ -gravity center -crop 457x328+0+0 +repage \
  processed_png/super_event_012_root_and_fang_processed.png
convert processed_png/super_event_012_root_and_fang_processed.png dds/super_event_012_root_and_fang.dds
cp dds/super_event_012_root_and_fang.dds gfx/super_events/super_event_012_root_and_fang.dds
```

- Asset status: `converted`
- Notes: final candidate favors a central circular parliament with mixed human and nonhuman delegates, readable at super-event scale, without collapsing into iconography or comedy

### `super_event_012_archive_world`

- Asset type: super-event image
- Intended in-game use: Event 012 Africa terminal Archive of Old Seats global-union route
- Source mode: built-in `image_gen`
- Source note: generated fictional archive-world sovereignty scene after reviewing Event 012 super-event DDS patterns and the skill super-event reference folder
- Prompt summary: cold planetary archive transformed into world order, with monumental shelves, legal ledgers, global cartographic table, bronze globe, and a terminal congress atmosphere; no readable text, no real archive copy, no generic office furniture
- Source PNG: `source_png/super_event_012_archive_world_source.png`
- Processed PNG: `processed_png/super_event_012_archive_world_processed.png`
- Package DDS: `dds/super_event_012_archive_world.dds`
- Final DDS: `gfx/super_events/super_event_012_archive_world.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_012_archive_world`
- Suggested `.gfx` file: `interface/012_africa.gfx`
- Related super-event role: `archive-world union terminal`
- Contact-sheet sources:
  - `contact_sheets/archive_world_alternatives_source_contact_sheet.png`
  - `contact_sheets/variant_images_batch_root_archive_overview.png`
- Processing command:

```bash
convert source_png/super_event_012_archive_world_source.png \
  -filter Lanczos -resize 457x328^ -gravity center -crop 457x328+0+0 +repage \
  processed_png/super_event_012_archive_world_processed.png
convert processed_png/super_event_012_archive_world_processed.png dds/super_event_012_archive_world.dds
cp dds/super_event_012_archive_world.dds gfx/super_events/super_event_012_archive_world.dds
```

- Asset status: `converted`
- Notes: final candidate keeps Africa visible on the globe while making the legal archive, world table, and record-book atmosphere dominant rather than heroic faces

## Shared validation

- Existing Event 012 super-event DDS references inspected first:
  - `gfx/super_events/super_event_012_africa_unification.dds`
  - `gfx/super_events/super_event_012_archive_bestiary.dds`
  - `gfx/super_events/super_event_012_continent_sponsor.dds`
  - `gfx/super_events/super_event_012_dynamic_cross_continent_union.dds`
  - `gfx/super_events/super_event_012_rsa_peace.dds`
  - `gfx/super_events/super_event_012_world_is_one_gate.dds`
- Reference folder inspected:
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/`
- Dimension check:
  - processed PNGs are `457x328`
  - package DDS copies are `457x328`
  - live DDS files are `457x328`
- DDS/file check:
  - `file` reports both DDS copies and live DDS files as Microsoft DirectDraw Surface files compressed using DX10
- Review sheet:
  - `contact_sheets/variant_images_batch_root_archive_overview.png`

## Risks

- Both source images are generated ceremonial illustrations, not sourced documentary material. That matches the route brief, but final acceptance still depends on whether the parent wants the more crowded root-parliament read and the ledger-forward archive-world read.
- The built-in generator introduced small pseudo-script marks inside books and hanging sheets. They are not readable text at gameplay scale, but the implementation should avoid zoomed promotional use without review.

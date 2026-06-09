# Event 006 Great Partition Week Super-Event Image Handoff

Scope completed: generated non-icon super-event image package only. No `.gfx`, localisation, gameplay script, sound, music, spreadsheet, country, or flag edits were made.

## Deliverables

- Source package folder: `docs/assets/006_independence_wave/super_events/great_partition_week/`
- Final DDS: `gfx/super_events/super_event_independence_wave_great_partition_week.dds`
- Processed PNG: `docs/assets/006_independence_wave/super_events/great_partition_week/processed_png/super_event_independence_wave_great_partition_week.png`
- Prompt text: `docs/assets/006_independence_wave/super_events/great_partition_week/prompts/super_event_independence_wave_great_partition_week.txt`
- Manifest: `docs/assets/006_independence_wave/super_events/great_partition_week/manifest.md`
- Package gfx handoff: `docs/assets/006_independence_wave/super_events/great_partition_week/gfx_handoff.md`
- Contact sheet: `docs/assets/006_independence_wave/super_events/great_partition_week/contact_sheets/great_partition_week_super_event_source_contact_sheet.png`

## Asset summary

- Asset slug: `super_event_independence_wave_great_partition_week`
- Source mode: `generated`
- Why generation was appropriate: the requested scene is a fictional World War II-era documentary-style administrative panic during an alternate-history border partition week, so a generated staged scene is a better fit than a real archive photo
- Visual direction delivered: 1936-1945 ministry map room with officials moving neutral map pins, telegram bundles, newspapers, telephones, and crowded desks; serious bureaucratic shock rather than apocalyptic collapse; no modern props; no Soviet-collapse imagery; no flag-asset work
- Primary source selection: source C was chosen for the clearest central exchange of partition documents and the best readable wall-map composition at super-event size

## Validation

- `docs/assets/006_independence_wave/super_events/great_partition_week/processed_png/super_event_independence_wave_great_partition_week.png` validated locally at `457x328`
- `gfx/super_events/super_event_independence_wave_great_partition_week.dds` validated locally at `457x328`
- DDS existence verified at the requested final path
- Source PNG, alternates, prompt file, manifest, gfx handoff, and contact sheet all exist in the package folder

## Wiring notes for main agent

- Proposed sprite name: `GFX_super_event_independence_wave_great_partition_week`
- Suggested texture path:

```txt
gfx/super_events/super_event_independence_wave_great_partition_week.dds
```

- Suggested sprite snippet:

```txt
spriteType = {
	name = "GFX_super_event_independence_wave_great_partition_week"
	texturefile = "gfx/super_events/super_event_independence_wave_great_partition_week.dds"
}
```

## Remaining risks

- The source is intentionally fictional staged-documentary art, so it should be treated as final generated source art rather than archival material
- Minor paper textures remain visible in the raw source variants, but the selected processed crop does not retain readable text at the final playable size

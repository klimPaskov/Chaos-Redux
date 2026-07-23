# Filters Fail at Night report image GFX handoff

Status: generated, processed, converted, and ready for wiring.

## Sprite contract

| Field | Value |
| --- | --- |
| Proposed sprite | `GFX_report_event_fallout_filters_fail` |
| Target GFX file | `interface/fallout_world_end.gfx` |
| Final DDS | `gfx/event_pictures/fallout_filters_fail/report_event_fallout_filters_fail.dds` |
| Runtime canvas | `210x176` |
| Texture format | one level uncompressed 32 bit BGRA DDS with alpha |
| Consumer | Human opening event `chaosx.fallout.217` and its human result or callback surface when selected by the parent implementation |
| Hidden AI | no player facing picture |

Suggested definition for the main agent:

```text
spriteType = {
    name = "GFX_report_event_fallout_filters_fail"
    texturefile = "gfx/event_pictures/fallout_filters_fail/report_event_fallout_filters_fail.dds"
}
```

## Visual use notes

The image shows an empty shelter filter room at night. The torn filter bags, dead pressure apparatus, damp floor, and single practical lamp communicate a failure without identifying a real country or region. It is a fictional alternate history report image. No real person, flag, attested symbol, text, Zombie motif, audio, or reused asset is involved.

## Evidence paths

- Source PNG: `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_fallout_filters_fail_source.png`
- Processed PNG: `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_fallout_filters_fail.png`
- Review contact sheet: `docs/assets/air_cleanliness_fallout/contact_sheets/report_event_fallout_filters_fail_contact_sheet.png`
- Prompt provenance: `docs/assets/air_cleanliness_fallout/prompts/report_event_fallout_filters_fail.md`
- Manifest row: `docs/assets/air_cleanliness_fallout/manifest.md`

The asset subagent did not edit the target GFX file. The main agent owns final registration and event wiring.

## SHA 256 evidence

| File | SHA 256 |
| --- | --- |
| `source_png/report_events/report_event_fallout_filters_fail_source.png` | `e14609cf4833cac613bf8e9f233b94a21dbe2d2f2d3067d19c295caa3a364ef8` |
| `processed_png/report_events/report_event_fallout_filters_fail.png` | `b09f25f2d482bf635aa295051ad530fea80db34346a1f88d8e0fee4f7f4ad7b3` |
| `contact_sheets/report_event_fallout_filters_fail_contact_sheet.png` | `a23e37f8b5120364850873e37f66d3240454a4a9e86eee5734e4dcd5d9681f87` |
| `gfx/event_pictures/fallout_filters_fail/report_event_fallout_filters_fail.dds` | `f07078ba5b49f7f2e2dae2ee3fa12360911975ef6e312b43b15ac3dee5660434` |

# Fallout Bad Batch report art manifest

Package: fallout_bad_batch
Asset class: generated fictional alternate-history report event art
Scope: one global event report image for the Fallout Bad Batch event
Source classification: fictional high-chaos altered ecology
Reference family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
Reference inspection: completed using the canonical report contact sheet and catalog entries. The reference family established the documentary card treatment, transparent corners, and 210x176 canvas. No reference pixels were used in the final asset.

## Requirement to runtime crosswalk

| Requirement | Intended use | Source package | Runtime asset | Sprite or lookup | Live consumer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| fallout_bad_batch_report_art | Global report event image showing altered ecology fallout | `source_png/report_event_fallout_bad_batch_source.png` processed to `processed_png/report_event_fallout_bad_batch.png` | `gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds` | `GFX_report_event_fallout_bad_batch` proposed | Parent event implementation and event picture GFX wiring | handed_off |

## Asset entry

### report_event_fallout_bad_batch

- Related event id: parent Fallout Bad Batch global event id, exact numeric id not supplied to asset worker
- Related event slug: fallout_bad_batch
- Asset type: report event image
- Intended in-game use: global event report card for the first documented altered ecology fallout
- Source mode: `$imagegen`
- Source note: original built-in imagegen scene, generated because the event is fictional and requires an impossible ecology that has no real archive source
- Identity classification: fictional high-chaos alternate history. No real person, real country, real flag, or named institution is shown.
- Generation prompt: `prompts/report_event_fallout_bad_batch_prompt.txt`
- Prompt provenance: `prompt_provenance.md`
- Source PNG: `docs/assets/fallout_bad_batch/source_png/report_event_fallout_bad_batch_source.png`
- Processed PNG preview: `docs/assets/fallout_bad_batch/processed_png/report_event_fallout_bad_batch.png`
- Final DDS: `gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds`
- Target size: 210x176
- Sprite name: `GFX_report_event_fallout_bad_batch`
- Suggested GFX file: the existing event-picture sprite definition file in the parent implementation scope. Parent to confirm the exact filename before wiring.
- Related localisation key: parent scope to assign
- Related event, decision, focus, idea, UI element, or super-event: Fallout Bad Batch global event report surface
- Processing: repository `process_report_event_image.py` applied cover crop, monochrome conversion, sepia, grain, paper border, deterministic tilt, transparent canvas margin, and soft shadow
- DDS conversion: repository `convert_to_dds.py` with explicit width 210 and height 176
- Visual QA: source is monochrome period documentary material with dead orchard, fibrous altered growth, ash haze, damaged farmhouse, and period telephone poles. No readable text, modern props, real person, real flag, or recognizable national insignia.
- Runtime QA: processed PNG is RGBA 210x176 with transparent corners. DDS uses legacy uncompressed BGRA layout with 210x176 dimensions, 32 bit pixels, one level, and valid texture caps.
- Asset status: handed_off. Final art is complete. Parent `.gfx` registration and event reference remain pending by design.

## Package files

- `source_png/report_event_fallout_bad_batch_source.png`
- `processed_png/report_event_fallout_bad_batch.png`
- `gfx_handoff.md`
- `prompt_provenance.md`
- `prompts/report_event_fallout_bad_batch_prompt.txt`
- `gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds`

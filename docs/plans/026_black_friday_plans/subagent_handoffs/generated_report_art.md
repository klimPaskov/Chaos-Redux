# Generated Event 26 report-art handoff

Status: `parent_visual_reviewed_2026-08-30`; the generated source, processed preview, staged DDS, prompt record, manifest, contact sheet, GFX handoff, runtime promotion, and sprite registration are present.

## Runtime identity

- Event: Event 26 Black Friday.
- Preserved event root: `chaosx.nr26.1`.
- Asset basename: `black_friday_report`.
- Proposed sprite: `GFX_report_event_026_black_friday`.
- Intended runtime texture: `gfx/event_pictures/026_black_friday/black_friday_report.dds`.
- Proposed target registry: `interface/026_black_friday.gfx` (parent-owned; not created or edited by this worker).

## Files created

- Source PNG: `docs/assets/026_black_friday/source_png/black_friday_report_source.png` (`1536x1024 RGB`, SHA-256 `bd556ff1bc70f78d9d0187528af20c78c98df1d31c66c754000bec72df31a27a`).
- Processed PNG: `docs/assets/026_black_friday/processed_png/black_friday_report.png` (`210x176 RGBA`, SHA-256 `b38106774c18e4f144a720df03a3bf828747fd046283daf9161f288c33efe987`).
- Staged DDS: `docs/assets/026_black_friday/dds/gfx/event_pictures/026_black_friday/black_friday_report.dds` (`210x176`, 32-bit BGRA, SHA-256 `75f977fe1d78ec6fe25493c2ff94124dd6cfd3e859c4155740595aafd0e41dac`).
- Prompt record: `docs/assets/026_black_friday/prompts/black_friday_report_prompt.txt`.
- Manifest: `docs/assets/026_black_friday/manifest.md`.
- Contact sheet: `docs/assets/026_black_friday/contact_sheets/black_friday_report_contact_sheet.png`.
- DDS decode evidence: `docs/assets/026_black_friday/notes/black_friday_report_dds_roundtrip.png`.
- Sprite handoff: `docs/assets/026_black_friday/gfx_handoff.md`.

## Production and checks

The source was made with the official built-in ImageGen route from the saved prompt at `docs/assets/026_black_friday/prompts/black_friday_report_prompt.txt`. It is fictional period documentary art, so generation fits the requested alternate-history purchasing scene and no external provenance applies.

The matching canonical reference family inspected was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png`; its catalog confirms the `210x176` report-event family.

The source was processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The converter used the repository script's BGRA ffmpeg fallback because `texconv` was unavailable.

The processed PNG has `210x176 RGBA`, all four corner alpha values `0`, and alpha bounding box `(4, 5, 210, 176)`. The DDS header reports `DDS `, `210x176`, `32-bit BGRA`, pitch `840`, and an exact `147840`-byte pixel payload. Decoding the DDS produced `210x176 RGBA` pixel-identical to the processed PNG.

## Parent follow-up and blockers

The parent visually reviewed `docs/assets/026_black_friday/contact_sheets/black_friday_report_contact_sheet.png` on 2026-08-30, promoted the staged DDS to `gfx/event_pictures/026_black_friday/black_friday_report.dds`, and registered the sprite in `interface/026_black_friday.gfx`. No interface, event, localisation, gameplay, GUI, achievement, spreadsheet, or other wiring file was edited by the report-art worker.

The active-sale idea icon and achievement triplet were not produced because they are outside this subagent's assigned generated report-art scope. The parent completed visual review, runtime promotion, and sprite registration on 2026-08-30; the report asset is therefore complete for the current staging boundary, with live in-game texture acceptance still owned by the parent.

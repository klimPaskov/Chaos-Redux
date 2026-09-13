# Event 027 generated event-art handoff

## Result

The final accepted generated report image is complete for parent-owned Event 027 wiring.

The scene is an original fictional 1936-1945 joint-service doctrine-research exercise at a coastal military school, photographed in period documentary style. One officer-instructor anchors the composition while infantry, a field artillery crew, a medium tank, and a period aircraft remain visibly distinct after reduction to the 210x176 HOI4 report canvas.

## Prompt and provenance

- Source mode: generated non-icon event art using the official built-in ImageGen tool.
- Generation date: 2026-08-29.
- Exact prompt: `docs/assets/027_doctrine_research/prompts/027_doctrine_research_source_prompt.txt`.
- Original generated artifact: `C:\Users\klimp\.codex\generated_images\01a04e96-3aef-7513-9901-0518d4618adc\exec-f7cf3fc0-3ecf-4537-8be4-ea64aeb02d98.png`.
- Preserved source copy: `docs/assets/027_doctrine_research/source_png/027_doctrine_research_source.png`.
- Source SHA-256: `39A179BE639D873300E3B3AE9D7B0C363C15E328A562ADC73AEE93A07E5FE3E9`.
- Generation fit: the exercise is fictional and needs a tightly composed multi-service scene, so generated period-documentary art is more suitable than an archive photograph that would likely omit one or more required services.

## Files and dimensions

| Role | Path | Dimensions | Notes |
| --- | --- | ---: | --- |
| Generated source PNG | `docs/assets/027_doctrine_research/source_png/027_doctrine_research_source.png` | `1536x1024` | Opaque RGBA source photograph, retained unchanged. |
| Processed PNG preview | `docs/assets/027_doctrine_research/processed_png/027_doctrine_research_report.png` | `210x176` | Sepia report-card treatment with transparent corners and soft shadow. |
| Final runtime DDS | `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds` | `210x176` | One-level uncompressed BGRA DDS. |
| Manifest | `docs/assets/027_doctrine_research/manifest.md` | — | Requirement crosswalk, provenance, and QA facts. |
| GFX handoff | `docs/assets/027_doctrine_research/gfx_handoff.md` | — | Proposed sprite and parent-owned wiring snippet. |

Processed PNG SHA-256: `25624BBB797C96FB9B17DC8B0450556D59C6FC994F7AC82BF36E92D6A4CBFD90`.

Final DDS SHA-256: `D7299954367B8374142A8A8242CEB8DE9117E80D3809D92CAED1339F188281A5`.

## Processing and conversion

- Report-card processing: `python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py docs/assets/027_doctrine_research/source_png/027_doctrine_research_source.png docs/assets/027_doctrine_research/processed_png/027_doctrine_research_report.png`.
- DDS conversion: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/027_doctrine_research/processed_png/027_doctrine_research_report.png --output gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds --width 210 --height 176`.
- Background treatment: the source was generated as an opaque documentary photograph; the required transparent report-card edge treatment was applied locally by the repository processor, yielding transparent corners and transparent edge space without a fake matte.
- DDS header: legacy 128-byte header, `DDS_HEADER` size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks, and `DDSCAPS_TEXTURE` `0x1000`.
- DDS file length: `147968` bytes, exactly `128 + 210 * 176 * 4`.
- Alpha validation: processed PNG and final DDS alpha range `0-255`; all four corner alpha bytes are `0`.
- Round-trip validation: DDS payload exactly equals the processed PNG pixels encoded as BGRA.

## Visual inspection

The processed native-size preview was inspected. The central instructor remains readable, infantry occupy the left foreground, artillery the right foreground, armor the right midground, the aircraft the upper-right sky, and the coastal horizon remains visible behind the exercise. The result contains no readable text, flags, insignia, modern gear, UI, watermark, or logo.

## Parent handoff

- Proposed sprite name: `GFX_report_event_027_doctrine_research`.
- Target `.gfx`: existing parent-owned Chaos Redux event-picture registry; the exact file was not supplied in the brief and this worker did not inspect or edit GFX registration.
- Ready-to-copy definition is in `docs/assets/027_doctrine_research/gfx_handoff.md`.
- Keep the final texture path unchanged: `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`.
- No gameplay, localisation, GFX registration, GUI, or spreadsheet files were edited.

## Blockers

None for generation, processing, inspection, or DDS conversion.

Parent-owned GFX registration remains intentionally pending because it is outside this subagent's scope.

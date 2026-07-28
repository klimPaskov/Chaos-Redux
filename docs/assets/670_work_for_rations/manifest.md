# Candidate 670 — Work for Rations asset manifest

This active workspace contains the generated fictional Fallout report-event image package for candidate 670, Work for Rations.

## Requirement-to-runtime coverage

| Requirement | Intended use | Source package | Runtime registration | Consumer | Status |
| --- | --- | --- | --- | --- | --- |
| `670.work_for_rations.report_event` | Fallout report-event card showing a Food Compact harvest crew working for ration allocation | `source_png/report_event_fallout_work_for_rations_source.png` → `processed_png/report_event_fallout_work_for_rations.png` | `gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds`; proposed sprite `GFX_report_event_fallout_work_for_rations` | Candidate 670 report-event picture consumer, to be wired by the main agent | handed_off |

## Asset entry

- Asset name: `report_event_fallout_work_for_rations`
- Related event id: `670`
- Related event slug: `work_for_rations`
- Asset type: fictional generated report-event picture
- Intended in-game use: 210x176 Fallout report-event card for the Work for Rations event
- Source mode: `$imagegen` built-in image-generation workflow
- Source note: generated from a new prompt; no repository image, internet image, real person, real flag, or attested symbol was reused
- Canonical reference inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/` and its `contact_sheet.png`
- Source PNG: `docs/assets/670_work_for_rations/source_png/report_event_fallout_work_for_rations_source.png`
- Source PNG SHA-256: `55F4FAD9C56D32D12148D9AFD344970B4C70CE45F5BB7D3705F27D83FE5B1C2B`
- Source dimensions: `1370x1148` RGBA PNG
- Processed PNG: `docs/assets/670_work_for_rations/processed_png/report_event_fallout_work_for_rations.png`
- Processed PNG SHA-256: `25AEACC9B35E296D21977B8370E512FC688BF2435E865DCC2571F3137BDF73A4`
- Processed dimensions: `210x176` RGBA PNG with transparent corners and report-card shadow
- Decoded DDS review PNG: `docs/assets/670_work_for_rations/processed_png/report_event_fallout_work_for_rations_decoded_from_dds.png`
- Decoded DDS review SHA-256: `BDF515BA4CE0062AC377F4DB36721067BFE7F1C303893D245A4F3AD25ABE0EFF`
- Decoded review sheet: `docs/assets/670_work_for_rations/contact_sheets/report_event_fallout_work_for_rations_decoded_review.png`
- Review sheet SHA-256: `4E57B80A8DF20E3926999E5C2566FBDA9760E64316590E22536720E62921F64C`
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds`
- Final DDS SHA-256: `AFA13933B61CE085CCB3425B9E8B38C89A55CC26EED822FA3BF394A3BE3EC763`
- DDS format: legacy one-level uncompressed BGRA, 32-bit, `210x176`, 128-byte header, exact length `147968` bytes, alpha range `0..255`
- Sprite name: `GFX_report_event_fallout_work_for_rations`
- Suggested `.gfx` target: the existing event-picture sprite registry selected by the main agent; the parent request did not name a registry file, so no `.gfx` file was edited or guessed
- Related localisation key: not provided in the asset request
- Related event/UI id: candidate `670`, Work for Rations; gameplay wiring remains parent-owned
- Prompt record: `docs/assets/670_work_for_rations/prompts/report_event_fallout_work_for_rations_prompt.md`
- GFX handoff: `docs/assets/670_work_for_rations/gfx_handoff.md`
- Notes: scene shows a Food Compact harvest crew in an ash-dark winter field with sheltered machinery, a blank/illegible ration ledger, ration tokens, concrete agricultural infrastructure, and an invented geometric crate seal. Faces are obscured and no real person, national flag, attested symbol, readable text, zombie, gore, blood, corpse, modern device, or watermark is present.
- Asset status: `handed_off`

## Validation evidence

The final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` from the processed PNG and decoded with FFmpeg for visual review.

The decoded DDS reports `210x176` and `bgra`; the raw DDS payload has 147840 bytes and alpha bytes spanning `0..255`.

The contact sheet compares the generated source, processed report card, and DDS-decoded card at enlarged review scale.

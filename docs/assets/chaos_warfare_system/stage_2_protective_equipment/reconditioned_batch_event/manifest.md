# cbrn_protection.2 — defective reconditioned batch asset manifest

## Package

- Event id: `cbrn_protection.2`
- Event slug: `reconditioned_batch_event`
- Asset type: generated report-event image
- Intended use: event picture for the discovery of a defective reconditioned civil-defence gas-mask batch during inspection
- Source mode: `$imagegen` using the official built-in image-generation workflow
- Generation rationale: this is a fictional, event-specific late-1930s/early-1940s inspection scene. A generated documentary photograph fits the invented depot and precise defect better than an archive source that would depict a real historical place or object.
- Generation date: 2026-07-13
- Prompt: [`prompts/cbrn_protection_2_defective_reconditioned_batch.md`](prompts/cbrn_protection_2_defective_reconditioned_batch.md)
- Reference folder inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/report_event_images/`
- Reference style used: sepia documentary report photograph, slight card tilt, transparent edge space, and soft shadow.
- License status: original generated artwork; no third-party image, archive, author, or source license is involved. No public-domain claim is made. Treat as project-generated art subject to applicable image-generation and project-use terms.
- Era-fit note: fictional staged documentary scene uses 1936–1945 photographic composition, period respirators, period work clothing, wooden crates, metal shelving, factory windows, and period lighting. No modern equipment, insignia, readable text, gore, or UI artifacts are present.

## Asset: defective reconditioned gas-mask batch

- Asset name: `report_event_cbrn_defective_reconditioned_batch`
- Related event: `cbrn_protection.2`
- Intended in-game use: report-event image
- Source PNG: `docs/assets/chaos_warfare_system/stage_2_protective_equipment/reconditioned_batch_event/source_png/report_event_cbrn_defective_reconditioned_batch_source.png`
- Source dimensions / channels: `1536x1024`, RGB PNG
- Processed PNG preview: `docs/assets/chaos_warfare_system/stage_2_protective_equipment/reconditioned_batch_event/processed_png/report_event_cbrn_defective_reconditioned_batch.png`
- Processed dimensions / channels: `210x176`, RGBA PNG
- Report processing: `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`; canvas `210x176`, card `192x153`, border `4`, positive tilt `4.0°`, grain `7`, paper grain `2`, shadow offset `4,5`, shadow blur `4.5`, shadow opacity `0.50`, supersample `4`, edge soften `0.35`, seed `20260713`
- Final DDS: `gfx/event_pictures/cbrn/report_event_cbrn_defective_reconditioned_batch.dds`
- Final DDS dimensions: `210x176`
- Final DDS format: uncompressed 32-bit RGBA/BGRA-style DDS; `DDPF_RGB | DDPF_ALPHAPIXELS`, `dwFourCC = 0`, `dwRGBBitCount = 32`
- Channel masks: R `0x00FF0000`, G `0x0000FF00`, B `0x000000FF`, A `0xFF000000`; pixel bytes are written in BGRA order for the verified report-event convention
- Mipmaps: `8` levels, full chain `210x176`, `105x88`, `52x44`, `26x22`, `13x11`, `6x5`, `3x2`, `1x1`; base pitch `840` bytes
- DDS size: `197088` bytes
- Sprite name: `GFX_report_event_cbrn_defective_reconditioned_batch`
- Registered `.gfx` file: `interface/cbrn_protection.gfx`
- Localisation key: not applicable to the asset package; event/localisation ownership remains with the main agent
- Contact sheet: `docs/assets/chaos_warfare_system/stage_2_protective_equipment/reconditioned_batch_event/contact_sheets/cbrn_protection_2_reconditioned_batch_contact_sheet.png`
- Status: `complete`; the main implementation registers the sprite in `interface/cbrn_protection.gfx` and uses it in `events/cbrn_protection_events.txt`

## Validation evidence

- The processed PNG is exactly `210x176` and RGBA.
- All four processed PNG corners are `(0, 0, 0, 0)`; alpha extrema are `0–255`.
- The DDS reopens successfully through Pillow as `210x176` RGBA.
- DDS header validation reports `8` mipmaps, `0x41` pixel flags, no compression FourCC, 32-bit pixels, the channel masks above, and `0x401008` texture/mipmap caps.
- The DDS file size matches the header and full uncompressed mip chain: `197088` bytes.

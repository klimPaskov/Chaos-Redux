# Fallout “The Well Queue” report image manifest

## Package

- Asset family: Fallout global-survival / “The Well Queue”
- Asset type: fictional alternate-history report event image
- Related event slug: `fallout_world_end`
- Source mode: `$imagegen` (official built-in ImageGen)
- Source rationale: the scene is fictional and requires a specific regional water-queue composition that has no real archival source. Generation was the accepted mode.
- Canonical reference inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png` and the matching report family entries in `CATALOG.md`.
- Source generation date: 2026-07-22
- ImageGen output record: `C:\Users\klimp\.codex\generated_images\019f8a8a-5d41-70a1-b7da-d017f449f860\exec-2436a480-d297-4850-8496-da3a583c43ee.png` (retained source copy is authoritative for this package).
- Prompt record: `docs/assets/fallout_well_queue/prompts/report_event_fallout_well_queue_prompt.txt`
- Provenance: generated fictional scene. There is no external source link, real person, historical archive claim, or reused zombie or chemical-warfare art.

## Asset entry

| Field | Value |
| --- | --- |
| Asset name | `report_event_fallout_well_queue` |
| Intended use | Report event card for the Fallout global-survival family, depicting a regional queue at a sealed well under ash and cold light |
| Source PNG | `docs/assets/fallout_well_queue/source_png/report_event_fallout_well_queue_source.png` |
| Source dimensions | 1536x1024 RGB |
| Processed PNG preview | `docs/assets/fallout_well_queue/processed_png/report_event_fallout_well_queue.png` |
| Processed dimensions | 210x176 RGBA, black-and-white with sepia, tilted documentary card, transparent edge corners, soft shadow |
| Final DDS | `gfx/event_pictures/fallout_world_end/report_event_fallout_well_queue.dds` |
| Final dimensions | 210x176 |
| Conversion | `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, then `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 210 --height 176` |
| Proposed sprite | `GFX_report_event_fallout_well_queue` |
| Target `.gfx` | Existing Chaos Redux event-picture sprite registry selected by the main agent. This subagent did not edit `.gfx` |
| Related localisation/event id | The main agent binds the proposed sprite to the “The Well Queue” report event |
| Status | `complete` (asset production and handoff complete, with `.gfx` registration owned by the main agent) |

### Visual-fit notes

The generated frame is a grounded documentary-style scene with an orderly civilian queue, sealed concrete well housing, cold gray daylight, airborne ash, cracked ground, and damaged low structures. It contains no readable text, logos, watermarks, named person, zombies, chemical-warfare imagery, modern UI, or military spectacle. The local processor applies the canonical report-card treatment rather than asking ImageGen to draw a tilted card.

### Requirement-to-runtime coverage

| Requirement id | Intended purpose | Source package / manifest entry | Runtime registration | Live consumer | State / visibility | Audit status |
| --- | --- | --- | --- | --- | --- | --- |
| `fallout_well_queue.report_image` | The Well Queue Fallout report-event image | `report_event_fallout_well_queue` in this manifest | `gfx/event_pictures/fallout_world_end/report_event_fallout_well_queue.dds`, proposed sprite `GFX_report_event_fallout_well_queue` | Main-agent event wiring for the “The Well Queue” report event | Event-triggered report card | Covered. `.gfx` and event id remain main-agent-owned |

## Validation evidence

- Source PNG: 1536x1024 RGB.
- Processed PNG: exactly 210x176 RGBA. Alpha range 0–255 confirms transparent corners and opaque card content.
- DDS: legacy uncompressed BGRA, exact 147,968 bytes (`128 + 210*176*4`), `DDS ` magic, header size 124, pixel format size 32, flags 65, fourCC 0, 32-bit channels, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, and `DDSCAPS_TEXTURE` `0x1000`.
- DDS payload alpha range: 0–255.
- SHA-256: source `D1D267B597CB5AD898515E48CD762082AC7F3A6D2BD88821B898C424A14FB983`, processed `EEE2E643FA08B542155F4DB2BE15F37D27D6234F58D50D28702709E4ED3086EC`, DDS `01F7386B2BCEB7D0AB3F871EB63B70F4E88F970C230AEFDBA55B9F15876E3119`.
- No contact sheet was created because this package contains one accepted generated alternative. The processed preview is the review artifact.
- Blocker: none for asset production. `.gfx` sprite registration and exact report-event id are intentionally deferred to the main agent per scope.

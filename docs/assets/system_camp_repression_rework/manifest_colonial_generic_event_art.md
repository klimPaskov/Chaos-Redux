# System Camp Repression Rework: Colonial and Generic Event Art Manifest

Package: `system_camp_repression_rework`

Asset tranche: colonial and generic report/news imagery only.

## Shared provenance

- Source mode: built-in `$imagegen` (`image_gen`), with one distinct generation call for each asset.
- Source rationale: these are fictional or composite discovery and reckoning moments whose exact scenes do not correspond to one verifiable archival photograph. Generation provides route-specific compositions without fabricating the likeness of a real person.
- Source link, author, archive, collection, and source license: not applicable to generated original source art.
- Historical status: historically grounded fictional documentary imagery. These images must not be presented as authentic archival photographs or as evidence of a real photographed person, document, or incident.
- Exact prompts and built-in result identifiers: `docs/assets/system_camp_repression_rework/prompts/colonial_generic_event_art_prompts.md`.
- Live sprite registry: `interface/camp_repression_rework.gfx`.
- Localisation keys and final event ids are assigned through the country event packages and scripted image mappings.
- Animation: not applicable; all ten assets are static.
- Status vocabulary: the retained `handed_off` row label records the original producer milestone. All ten identities are now registered and consumed by live report/news event mappings.

## Processing contract

Report images use the repository-established report-card treatment: cover crop, true monochrome conversion, sepia tone, restrained grain, `4` degree card rotation, transparent `210x176` canvas, and soft shadow. News images use a cover crop to `397x153`, true grayscale mode, period press contrast, sharpening, and restrained monochrome grain. DDS files use one-mip 32-bit BGRA/B8G8R8A8-style masks.

The report processor named by the asset skill is absent from the live `.agents/skills/chaos-redux-event-assets/` checkout. Processing used the exact SHA-256-verified processor already pinned by the Event 011 package:

- processor: `C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`
- SHA-256: `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`

This is the same verified implementation used by `docs/assets/011_secret_alliance/_tooling/process_event_011_raster_assets.py`; no alternate visual treatment was substituted.

## Asset inventory

| Sprite id | Asset type and intended use | Depicted era | Source PNG | Processed PNG | Package DDS | Final runtime DDS | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `GFX_report_event_raj_detention_discovery` | Report image; first discovery of the Raj detention network | Early 1940s | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_raj_detention_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_raj_detention_discovery.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_raj_detention_discovery.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_raj_detention_discovery.dds` | `210x176` | `handed_off` |
| `GFX_news_event_colonial_reckoning` | News image; severe postwar or decolonisation-facing colonial exposure | 1946 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_colonial_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_colonial_reckoning.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/news_event_colonial_reckoning.dds` | `gfx/event_pictures/system_camp_repression_rework/news_event_colonial_reckoning.dds` | `397x153` | `handed_off` |
| `GFX_report_event_usa_relocation_review` | Report image; court or postwar review of U.S. relocation authority | 1945 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_usa_relocation_review_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_usa_relocation_review.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_usa_relocation_review.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_usa_relocation_review.dds` | `210x176` | `handed_off` |
| `GFX_report_event_fr_liberated_camp_records` | Report image; liberated French camp records recovery | 1944 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_fr_liberated_camp_records_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_fr_liberated_camp_records.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_fr_liberated_camp_records.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_fr_liberated_camp_records.dds` | `210x176` | `handed_off` |
| `GFX_news_event_vichy_reckoning` | News image; severe Vichy discovery or postwar reckoning | 1945 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_vichy_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_vichy_reckoning.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/news_event_vichy_reckoning.dds` | `gfx/event_pictures/system_camp_repression_rework/news_event_vichy_reckoning.dds` | `397x153` | `handed_off` |
| `GFX_report_event_libyan_camp_discovery` | Report image; Allied discovery of an abandoned Libyan colonial camp | Early 1940s | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_libyan_camp_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_libyan_camp_discovery.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_libyan_camp_discovery.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_libyan_camp_discovery.dds` | `210x176` | `handed_off` |
| `GFX_report_event_congo_labor_discovery` | Report image; local or international inspection of Congo concession labor evidence | 1940s | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_congo_labor_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_congo_labor_discovery.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_congo_labor_discovery.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_congo_labor_discovery.dds` | `210x176` | `handed_off` |
| `GFX_news_event_congo_colonial_reckoning` | News image; severe international exposure of the Congo concession system | 1946 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_congo_colonial_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_congo_colonial_reckoning.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/news_event_congo_colonial_reckoning.dds` | `gfx/event_pictures/system_camp_repression_rework/news_event_congo_colonial_reckoning.dds` | `397x153` | `handed_off` |
| `GFX_report_event_generic_camp_discovery` | Report image; generic first discovery of an abandoned detention site | 1945 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_generic_camp_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_generic_camp_discovery.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/report_event_generic_camp_discovery.dds` | `gfx/event_pictures/system_camp_repression_rework/report_event_generic_camp_discovery.dds` | `210x176` | `handed_off` |
| `GFX_news_event_global_atrocity_evidence` | News image; first severe global atrocity-evidence disclosure | 1945 | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_global_atrocity_evidence_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_global_atrocity_evidence.png` | `docs/assets/system_camp_repression_rework/dds/colonial_generic_event_art/news_event_global_atrocity_evidence.dds` | `gfx/event_pictures/system_camp_repression_rework/news_event_global_atrocity_evidence.dds` | `397x153` | `handed_off` |

## Per-asset era fit and source notes

| Sprite id | Era-fit and source note |
| --- | --- |
| `GFX_report_event_raj_detention_discovery` | Timber Raj barrack, iron cots, mosquito-net frames, shuttered windows, tropical practical dress, and paper-record inspection support the British India wartime internment anchor. The scene is a fictional composite and depicts no selected protected class. |
| `GFX_news_event_colonial_reckoning` | Period press cameras, formal 1940s attire, staff cars, record crates, and a civic courthouse handover support a postwar colonial accountability scene. It is intentionally broader than the Raj report image. |
| `GFX_report_event_usa_relocation_review` | High-desert barracks, wire-mesh office window, potbelly stove, boxed files, property tags, and an exterior watchtower support the legal and postwar review route without claiming a real photographed camp or person. |
| `GFX_report_event_fr_liberated_camp_records` | Damaged southern-French administration office, paper ledgers, broken filing furniture, field camera, and camp perimeter context support liberation-era evidence recovery. |
| `GFX_news_event_vichy_reckoning` | French courthouse architecture, canvas-backed period truck, archive crates, clerks, gendarmes, and press cameras support a post-liberation public reckoning distinct from the interior records report. |
| `GFX_report_event_libyan_camp_discovery` | Cyrenaican stone huts, improvised shade, wire, water drums, ration tins, rocky desert, and field investigators support the Italian colonial Libya anchor. The scene avoids orientalist spectacle and visible suffering. |
| `GFX_report_event_congo_labor_discovery` | Narrow-gauge ore carts, manual tools, timber transfer shed, humid rail yard, and equal-positioned Congolese/international participants support the Belgian Congo extraction and inspection route. |
| `GFX_news_event_congo_colonial_reckoning` | River-and-rail depot, mineral sacks, civic representatives, international commissioners, and period press cameras support a public Congo reckoning distinct from the worksite report. |
| `GFX_report_event_generic_camp_discovery` | Anonymous cold-frontier compound, rough barracks, watchtower, damaged gate, melting snow, film cans, and record crates support a generic severe discovery without reproducing a recognizable real camp. |
| `GFX_news_event_global_atrocity_evidence` | Captured brick archive warehouse, long evidence tables, film cans, document crates, civilian witnesses, and flash cameras support a global disclosure without depicting bodies or graphic evidence. |

## Review and validation

- Source contact sheet: `docs/assets/system_camp_repression_rework/contact_sheets/colonial_generic_event_art/colonial_generic_event_art_source_contact_sheet.png`.
- Processed contact sheet: `docs/assets/system_camp_repression_rework/contact_sheets/colonial_generic_event_art/colonial_generic_event_art_processed_contact_sheet.png`.
- Validation record: `docs/assets/system_camp_repression_rework/notes/validation_colonial_generic_event_art.md`.
- GFX wiring handoff: `docs/assets/system_camp_repression_rework/gfx_handoff_colonial_generic_event_art.md`.

## Scope and blockers

No placeholders, fallbacks, blocked assets, or runtime-wiring items remain in this ten-asset tranche. All ten identities have live sprite definitions and report/news consumers.

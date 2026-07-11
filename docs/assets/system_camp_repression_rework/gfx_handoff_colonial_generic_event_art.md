# System Camp Repression Rework: Colonial and Generic Event Art GFX Handoff

This handoff covers exactly ten accepted report/news sprites. Their definitions are live in `interface/camp_repression_rework.gfx`, and their report/news mappings are live in the country event packages.

Suggested registry: `interface/camp_repression_rework.gfx`, which already owns the Repression Ledger sprite family.

## Runtime paths and dimensions

| Sprite id | Exact runtime DDS path | Dimensions | Intended route |
| --- | --- | --- | --- |
| `GFX_report_event_raj_detention_discovery` | `gfx/event_pictures/system_camp_repression_rework/report_event_raj_detention_discovery.dds` | `210x176` | First Raj detention-network discovery |
| `GFX_news_event_colonial_reckoning` | `gfx/event_pictures/system_camp_repression_rework/news_event_colonial_reckoning.dds` | `397x153` | Severe postwar or decolonisation-facing colonial exposure |
| `GFX_report_event_usa_relocation_review` | `gfx/event_pictures/system_camp_repression_rework/report_event_usa_relocation_review.dds` | `210x176` | U.S. court or postwar relocation review |
| `GFX_report_event_fr_liberated_camp_records` | `gfx/event_pictures/system_camp_repression_rework/report_event_fr_liberated_camp_records.dds` | `210x176` | Liberated French camp-record discovery |
| `GFX_news_event_vichy_reckoning` | `gfx/event_pictures/system_camp_repression_rework/news_event_vichy_reckoning.dds` | `397x153` | Severe Vichy discovery or postwar reckoning |
| `GFX_report_event_libyan_camp_discovery` | `gfx/event_pictures/system_camp_repression_rework/report_event_libyan_camp_discovery.dds` | `210x176` | Allied discovery of a Libyan colonial camp |
| `GFX_report_event_congo_labor_discovery` | `gfx/event_pictures/system_camp_repression_rework/report_event_congo_labor_discovery.dds` | `210x176` | Congo concession-labor discovery or inspection |
| `GFX_news_event_congo_colonial_reckoning` | `gfx/event_pictures/system_camp_repression_rework/news_event_congo_colonial_reckoning.dds` | `397x153` | Severe international Congo exposure |
| `GFX_report_event_generic_camp_discovery` | `gfx/event_pictures/system_camp_repression_rework/report_event_generic_camp_discovery.dds` | `210x176` | Generic detention-site discovery |
| `GFX_news_event_global_atrocity_evidence` | `gfx/event_pictures/system_camp_repression_rework/news_event_global_atrocity_evidence.dds` | `397x153` | First severe global atrocity-evidence disclosure |

## Live sprite definitions

The following definitions are present inside the existing `spriteTypes = { ... }` block in `interface/camp_repression_rework.gfx`:

```text
	spriteType = { name = "GFX_report_event_raj_detention_discovery" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_raj_detention_discovery.dds" }
	spriteType = { name = "GFX_news_event_colonial_reckoning" texturefile = "gfx/event_pictures/system_camp_repression_rework/news_event_colonial_reckoning.dds" }
	spriteType = { name = "GFX_report_event_usa_relocation_review" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_usa_relocation_review.dds" }
	spriteType = { name = "GFX_report_event_fr_liberated_camp_records" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_fr_liberated_camp_records.dds" }
	spriteType = { name = "GFX_news_event_vichy_reckoning" texturefile = "gfx/event_pictures/system_camp_repression_rework/news_event_vichy_reckoning.dds" }
	spriteType = { name = "GFX_report_event_libyan_camp_discovery" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_libyan_camp_discovery.dds" }
	spriteType = { name = "GFX_report_event_congo_labor_discovery" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_congo_labor_discovery.dds" }
	spriteType = { name = "GFX_news_event_congo_colonial_reckoning" texturefile = "gfx/event_pictures/system_camp_repression_rework/news_event_congo_colonial_reckoning.dds" }
	spriteType = { name = "GFX_report_event_generic_camp_discovery" texturefile = "gfx/event_pictures/system_camp_repression_rework/report_event_generic_camp_discovery.dds" }
	spriteType = { name = "GFX_news_event_global_atrocity_evidence" texturefile = "gfx/event_pictures/system_camp_repression_rework/news_event_global_atrocity_evidence.dds" }
```

## Source and processed review paths

| Sprite id | Source PNG | Processed PNG preview |
| --- | --- | --- |
| `GFX_report_event_raj_detention_discovery` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_raj_detention_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_raj_detention_discovery.png` |
| `GFX_news_event_colonial_reckoning` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_colonial_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_colonial_reckoning.png` |
| `GFX_report_event_usa_relocation_review` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_usa_relocation_review_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_usa_relocation_review.png` |
| `GFX_report_event_fr_liberated_camp_records` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_fr_liberated_camp_records_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_fr_liberated_camp_records.png` |
| `GFX_news_event_vichy_reckoning` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_vichy_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_vichy_reckoning.png` |
| `GFX_report_event_libyan_camp_discovery` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_libyan_camp_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_libyan_camp_discovery.png` |
| `GFX_report_event_congo_labor_discovery` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_congo_labor_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_congo_labor_discovery.png` |
| `GFX_news_event_congo_colonial_reckoning` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_congo_colonial_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_congo_colonial_reckoning.png` |
| `GFX_report_event_generic_camp_discovery` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/report_event_generic_camp_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/report_event_generic_camp_discovery.png` |
| `GFX_news_event_global_atrocity_evidence` | `docs/assets/system_camp_repression_rework/source/colonial_generic_event_art/news_event_global_atrocity_evidence_source.png` | `docs/assets/system_camp_repression_rework/processed/colonial_generic_event_art/news_event_global_atrocity_evidence.png` |

## Source and processing limitations

- Every image is a fictional generated composite, not a sourced archival photograph. Do not caption one as a real photographed person, real document, or exact historical incident.
- The compositions are historically grounded in the accepted Raj, U.S. relocation, France/Vichy, Libya, Belgian Congo, and generic discovery research notes, but generation cannot certify every minor garment, prop, or architectural detail as archival fact.
- All people are anonymous and fictional. No real leader or identifiable historical-person likeness was requested or intended.
- Papers, tags, crates, and photographs were deliberately prompted without readable text. Do not rely on in-image markings for localisation or evidence detail.
- Report images use a deterministic crop and tilted sepia-card treatment. Peripheral environmental context is intentionally secondary; event identity is carried by the crop-safe investigators and physical evidence.
- News images are true grayscale `397x153` crops with period press contrast and grain. They are designed for the news-event strip, not for enlargement into a report or super-event image.
- The live skill checkout lacked its documented report-card script. The exact repository-established processor pinned by Event 011 was used from its preserved path with verified SHA-256 `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`; no substitute treatment was introduced.

## Validation and outstanding wiring

- All ten runtime DDS files decode successfully and match their processed PNG pixels.
- All DDS files use one-mip 32-bit BGRA/B8G8R8A8-style masks.
- All six report cards have transparent corner pixels.
- All four news PNGs are true grayscale before DDS conversion.
- Runtime and package DDS copies are byte-identical for all ten assets.
- Full validation record: `docs/assets/system_camp_repression_rework/notes/validation_colonial_generic_event_art.md`.
- Blocked assets: none.
- Runtime registration, report/news assignment, and localisation/event alignment are complete. No parent-owned wiring item remains for this tranche.

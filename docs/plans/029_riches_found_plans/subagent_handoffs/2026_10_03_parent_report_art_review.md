# Event 029 report and category-picture review

Disposition: implemented visual review with event acceptance still unresolved.
The user's complete Event 029 asset brief authorizes these nine reports and one static category picture.
The parent opened each original source, processed PNG, and decoded final DDS individually through `view_image` on 2026-10-03.
The parent also reran `docs/assets/029_riches_found/notes/validate_and_contact_sheet.py` against the current runtime files.

## Current asset evidence

All source paths below are under `docs/assets/029_riches_found/source_png/`.
All processed paths are under `docs/assets/029_riches_found/processed_png/`.
All decoded final paths are under `docs/assets/029_riches_found/notes/decoded_dds/`.
The nine report runtime files are under `gfx/event_pictures/029_riches_found/`.
The category-picture runtime file is under `gfx/interface/decisions/029_riches_found/`.
The exact source, processed, evidence DDS, runtime DDS, dimensions, alpha, and SHA-256 values are recorded per row in `docs/assets/029_riches_found/notes/validation_report.json`.

| Asset | Individually opened source | Individually opened processed and decoded basename | Runtime DDS | Visual finding |
| --- | --- | --- | --- | --- |
| Discovery | `riches_found_discovery_report_source.png` | `report_event_riches_found_discovery.png` | `report_event_riches_found_discovery.dds` | Miners and a competing crowd remain readable around the exposed seam. |
| Rush | `riches_found_rush_report_source.png` | `report_event_riches_found_rush.png` | `report_event_riches_found_rush.dds` | Camp, labor movement, truck, and cart retain a coherent period composition. |
| Concession | `riches_found_concession_report_source.png` | `report_event_riches_found_concession.png` | `report_event_riches_found_concession.dds` | Gate, guarded access, workers, and processing works remain distinct. |
| Raid | `riches_found_raid_report_source.png` | `report_event_riches_found_raid.png` | `report_event_riches_found_raid.dds` | Armed raid and a stolen assay crate remain visible, with no treasure chest. |
| Collapse | `riches_found_collapse_report_source.png` | `report_event_riches_found_collapse.png` | `report_event_riches_found_collapse.dds` | Broken shaft supports, rubble, lamps, and rescue workers retain the scene's focus. |
| Gold Disease | `riches_found_gold_disease_report_source.png` | `report_event_riches_found_gold_disease.png` | `report_event_riches_found_gold_disease.dds` | Compulsive handling of assay samples and guarded access remain legible, with no biological outbreak or treasure chest imagery. |
| Opened depths | `riches_found_opened_depths_report_source.png` | `report_event_riches_found_opened_depths.png` | `report_event_riches_found_opened_depths.dds` | Workers and the unexplained illuminated opening retain clear silhouettes. |
| Gilded Sovereignty | `riches_found_gilded_sovereignty_report_source.png` | `report_event_riches_found_gilded_sovereignty.png` | `report_event_riches_found_gilded_sovereignty.dds` | Controlled company-district access and ore transport remain visible. |
| Bottomless Account | `riches_found_bottomless_account_report_source.png` | `report_event_riches_found_bottomless_account.png` | `report_event_riches_found_bottomless_account.dds` | Assay scale, workers, account books, and shaft opening remain readable. |
| Static category picture | `riches_found_category_picture_source.png` | `decision_cat_picture_riches_found.png` | `decision_cat_picture_riches_found.dds` | Shaft, ore carts, camp, and controlled entrance read at 114x101 without painted controls or labels. |

## Verification and limits

The nine report DDS files are 210x176 with real transparent corners and the retained tilted sepia card treatment.
The static category picture is 114x101 with a full opaque scene.
The validator confirmed strict legacy BGRA headers, exact processed-to-decoded pixel equality, and byte equality between each evidence DDS and its runtime DDS.
Individual review found no clipping of the principal subject, opaque report matte, fake checkerboard, conversion fringe, stretched subject, modern scene elements, or baked interface controls.
No source regeneration or runtime replacement was needed in this pass.

These are standalone image and file-chain findings.
The report review does not establish event-chain, probability, category-action-budget, icon-family, or full package acceptance.
The 97 icon/state assets have their own current audit assignment.
The temporary asset workspace remains retained while the event is incomplete.

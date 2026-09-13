# Event 32 — Missiles static event-art handoff

Parent integration status: the runtime DDS package is installed under the Event 032 `gfx/` directories, all icon and full-canvas aliases are registered, and the replacement global-news image is the current final. The implementation-level per-file visual audit is maintained at `docs/events/032_missiles/asset_audit.md`.

The bounded asset sidecar is complete through source generation, local processing, DDS conversion, and evidence capture. The parent has completed runtime copying, sprite registration, and consumer wiring; this handoff retains the original provenance and scope record.

## Deliverables

| Asset | Final dimensions | Temporary DDS | Intended sprite | Suggested target `.gfx` |
| --- | ---: | --- | --- | --- |
| Report/event image `032_missiles_country_report` | `210x176` | `docs/assets/032_missiles/dds/032_missiles_country_report.dds` | `GFX_032_missiles_country_report` | existing event-picture registry, expected `interface/events.gfx` |
| Global news image `032_missiles_global_proliferation_news` | `397x153` | `docs/assets/032_missiles/dds/032_missiles_global_proliferation_news.dds` | `GFX_032_missiles_global_proliferation_news` | existing event-picture registry, expected `interface/events.gfx` |
| Ordinary static decision-category picture `032_missiles_program_category` | `114x101` | `docs/assets/032_missiles/dds/032_missiles_program_category.dds` | `GFX_032_missiles_program_category` | `interface/decisions.gfx` |

## Source and treatment

All three source PNGs were generated with the official built-in ImageGen workflow on 2026-08-29 as original fictional alternate-history World War II missile-program scenes. All source canvases are opaque and contain no modern logos, readable generated text, identifiable real people, or recognizable real tragedy photography.

The report source was locally processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` into the required sepia 210x176 tilted documentary card with transparent edge corners and soft shadow. The news source was locally cover-cropped to 397x153, converted to black and white, given period contrast/grain, and retained fully opaque. The category source was locally cover-cropped to the canonical 114x101 decision-category picture canvas with restrained period contrast and remained fully opaque.

The canonical review families inspected were `event_art/report/`, `event_art/news/`, and `icons/decision_categories/pictures/`. The category family is distinct from small decision-category icons and from scripted-GUI assets. It is static and no dedicated scripted GUI was created.

## QA and provenance

The source/processed PNGs, prompts, contact sheet, and full manifest are retained under `docs/assets/032_missiles/`. All final DDS files use the repository-standard legacy one-level 32-bit BGRA layout and pass exact dimensions, byte length, header-mask, texture-cap, alpha, decoder, and pixel-equality checks. Exact SHA-256 values are recorded in `docs/assets/032_missiles/manifest.md`.

The detailed sprite handoff is `docs/assets/032_missiles/gfx_handoff.md`. Suggested post-approval runtime destinations are `gfx/event_pictures/032_missiles/` for the report/news files and `gfx/interface/decisions/032_missiles/` for the category picture. Those runtime files and registrations do not exist as a result of this sidecar.

## Scope boundary

No gameplay, localisation, interface, GFX registration, decision, event, spreadsheet, focus, flag, portrait, super-event, 3D, animation, icon, or generated-agent file was edited.

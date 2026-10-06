# GFX report and category-picture repair handoff

Date: 2026-10-06.

## Scope and completion

This handoff covers the report/news pictures assigned for Events 001, 003, 008, and 013, plus the two Event 013 decision-category pictures. Every assigned asset is complete and has a stable existing runtime path and sprite name. The work leaves GFX wiring to the main agent.

| Group | Runtime repairs | Final size | Main evidence |
| --- | --- | --- | --- |
| Event 001 Communism Spread | communist_state_control and communist_insurgency_start replaced; the prior 15-scene package audited byte-for-byte against current runtime. | 210x176 | docs/plans/gfx_fix_2026-10/001_report.md and evidence/001/ |
| Event 003 Holy Realm | arhat and buddha replaced with distinct anonymous documentary scenes. The report section is photo-only and will combine with the icon worker's package. | 210x176 | docs/plans/gfx_fix_2026-10/003_report.md and docs/assets/gfx_fix_reports_2026-10/notes/003_holy_realm/dds_validation.json |
| Event 008 Tensions Rising | Existing red-line news photo deterministically cropped to remove its smeared lower-left newspaper stacks. | 397x153 | docs/plans/gfx_fix_2026-10/008_report.md and docs/assets/gfx_fix_reports_2026-10/notes/008_tensions_rising/dds_validation.json |
| Event 013 Natural Disasters | regional_aftermath regenerated as a period photo; tropical_cyclone, extreme_wind, and eleven other report photos were remounted from existing images; winter and cyclone category pictures replaced. | 210x176 reports; 114x101 category pictures | docs/plans/gfx_fix_2026-10/013_report.md and docs/assets/gfx_fix_reports_2026-10/contact_sheets/013_natural_disasters_reports_final_14.png |

## Runtime asset map

| Sprite | Final texture path | Target .gfx | Status |
| --- | --- | --- | --- |
| GFX_report_event_communist_state_control | gfx/event_pictures/001_communism_spread/communist_state_control.dds | interface/001_communism_spread.gfx | Complete; existing name and path preserved. |
| GFX_report_event_communist_insurgency_start | gfx/event_pictures/001_communism_spread/communist_insurgency_start.dds | interface/001_communism_spread.gfx | Complete; existing name and path preserved. |
| GFX_report_event_holy_realm_arhat | gfx/event_pictures/003_holy_realm/report_event_holy_realm_arhat.dds | interface/003_holy_realm.gfx | Complete; existing name and path preserved. |
| GFX_report_event_holy_realm_buddha | gfx/event_pictures/003_holy_realm/report_event_holy_realm_buddha.dds | interface/003_holy_realm.gfx | Complete; existing name and path preserved. |
| GFX_news_event_tensions_red_line | gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds | interface/008_tensions_rising_event_images.gfx | Complete; existing name and path preserved. |
| GFX_report_event_nd_regional_aftermath | gfx/event_pictures/013_natural_disasters/report_event_nd_regional_aftermath.dds | interface/013_natural_disasters.gfx | Complete; existing name and path preserved. |
| GFX_report_event_nd_tropical_cyclone | gfx/event_pictures/013_natural_disasters/report_event_nd_tropical_cyclone.dds | interface/013_natural_disasters.gfx | Complete; existing name and path preserved. |
| GFX_report_event_nd_extreme_wind | gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_wind.dds | interface/013_natural_disasters.gfx | Complete; existing name and path preserved. |
| GFX_report_event_nd_tornado_outbreak | gfx/event_pictures/013_natural_disasters/report_event_nd_tornado_outbreak.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_hailstorm | gfx/event_pictures/013_natural_disasters/report_event_nd_hailstorm.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_extreme_cold_wave | gfx/event_pictures/013_natural_disasters/report_event_nd_extreme_cold_wave.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_heat_wave | gfx/event_pictures/013_natural_disasters/report_event_nd_heat_wave.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_wet_mass_movement | gfx/event_pictures/013_natural_disasters/report_event_nd_wet_mass_movement.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_ashfall | gfx/event_pictures/013_natural_disasters/report_event_nd_ashfall.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_lahar | gfx/event_pictures/013_natural_disasters/report_event_nd_lahar.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_storm_surge | gfx/event_pictures/013_natural_disasters/report_event_nd_storm_surge.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_meteor_impact | gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_impact.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_meteor_shower | gfx/event_pictures/013_natural_disasters/report_event_nd_meteor_shower.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_report_event_nd_massive_eruption | gfx/event_pictures/013_natural_disasters/report_event_nd_massive_eruption.dds | interface/013_natural_disasters.gfx | Complete; existing photo remounted, name and path preserved. |
| GFX_decision_cat_picture_nd_winter | gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_winter.dds | interface/013_natural_disasters.gfx | Complete; existing name and path preserved. |
| GFX_decision_cat_picture_nd_cyclone | gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_cyclone.dds | interface/013_natural_disasters.gfx | Complete; existing name and path preserved. |

## Visual and source review

The 001 before/after and 17-card contact sheets were reviewed and accepted by the parent on 2026-10-06. Eleven older 001 findings are covered by the reviewed 15-scene package, whose current runtime DDS SHA-256 values match all fifteen package values; the package also records successful pixel-exact DDS round trips and per-scene subject reviews. Two 001 textures were outside that package and received new scenes. The first insurgency-start candidate was rejected after the contact sheet showed similarity to the existing field assembly; the selected bridge-led composition is retained with its prompt and lineage.

The 003 before/after sheet shows the prior Potala image reused for both sprites and the selected hermitage and courtyard scenes. Neither new scene depicts the historical Buddha as a person or invents a named likeness. The parent reviewed and accepted both cards on 2026-10-06.

The 008 before/after sheet shows the original blurred newspaper stacks and the crop that retains the guard and street crowd. The parent reviewed and accepted the crop on 2026-10-06.

The 013 before-and-after sheets include the exact fourteen assigned report rows; the before sheet exposes the eleven straight mats and the final sheet confirms all fourteen share the tilted thin-border treatment. The drought-famine reference remains unchanged. The category before/after sheet shows the winter painting replacement and the ground-level cyclone illustration without a spiral sky.

## Processing and validation

Report cards use the repository processor at .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py and finish as 210x176 RGBA PNGs with sepia treatment, a slight tilt, thin border, soft shadow, and transparent corners. The 008 news photo remains full-canvas black-and-white at 397x153. Category pictures are opaque full-canvas 114x101 paintings.

Every produced DDS was written with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py. Focused validation records verify the legacy header fields, dimensions, pixel-exact decoding to the processed preview, and alpha behavior: transparent report-card corners and fully opaque news/category images. All prior DDS files that were replaced are retained under docs/assets/gfx_fix_reports_2026-10/notes/ for comparison and rollback.

No unrelated 013 report image was regenerated. The drought-famine report reference remains unchanged. The 013 meteor-impact icons and damaged disaster panel were excluded as directed. No .gfx, GUI, event, gameplay, localisation, or spreadsheet file was edited.

## Remaining integration

The main agent can wire the twenty-one listed textures through their existing sprite names and target GFX files. The final paths, sprite names, and use notes are collected in docs/assets/gfx_fix_reports_2026-10/gfx_handoff.md. Live-game validation remains with the user.

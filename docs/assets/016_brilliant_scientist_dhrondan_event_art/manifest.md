# Event016 D’Rhondan generated non-portrait art manifest

Status: active handoff package. Source mode is native ImageGen for every generated source PNG. Full-canvas flags, report scenes, news scenes, and the country identity panel use `consumer_opaque`. The faction emblem uses `native_transparent` and retains alpha through processing and DDS conversion. No background-removal fallback was used.

Canonical references inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png`, `event_art/report/contact_sheet.png`, `event_art/news/contact_sheet.png`, `icons/special_projects/contact_sheet.png`, and `icons/achievements/contact_sheet.png`. Flag ladder targets are 82x52, 41x26, and 10x7. Report scenes are 210x176. News scenes are 397x153.

## Flags

All flags are fictional, flat, straight-on designs. The four variants are separate ImageGen outputs, not recolours or resized substitutions. Runtime flags are root-only engine assets and therefore do not use a `.gfx` sprite registry.

| Asset | Runtime paths | Source PNG | Processed PNGs | Status |
| --- | --- | --- | --- | --- |
| `DHR` base flag | `gfx/flags/DHR.dds`, `gfx/flags/medium/DHR.dds`, `gfx/flags/small/DHR.dds` | `source_png/flags/dhr_base_source.png` | `processed_png/flags/{normal,medium,small}/dhr_base.png` | complete |
| `DHR_IMPERIAL` cosmetic route flag | `gfx/flags/DHR_IMPERIAL.dds`, `gfx/flags/medium/DHR_IMPERIAL.dds`, `gfx/flags/small/DHR_IMPERIAL.dds` | `source_png/flags/dhr_imperial_source.png` | `processed_png/flags/{normal,medium,small}/dhr_imperial.png` | complete |
| `DHR_SYNOD` cosmetic route flag | `gfx/flags/DHR_SYNOD.dds`, `gfx/flags/medium/DHR_SYNOD.dds`, `gfx/flags/small/DHR_SYNOD.dds` | `source_png/flags/dhr_synod_source.png` | `processed_png/flags/{normal,medium,small}/dhr_synod.png` | complete |
| `DHR_COVENANT` cosmetic route flag | `gfx/flags/DHR_COVENANT.dds`, `gfx/flags/medium/DHR_COVENANT.dds`, `gfx/flags/small/DHR_COVENANT.dds` | `source_png/flags/dhr_covenant_source.png` | `processed_png/flags/{normal,medium,small}/dhr_covenant.png` | complete |

## Report event pictures

Every row below is a purpose-built generated scene with a stable sprite token supplied by the parent. Suggested target file is `interface/016_brilliant_scientist_event_pictures.gfx` or the existing Event016 report registry chosen by the main agent. Runtime textures are full opaque DDS files under `gfx/event_pictures/016_brilliant_scientist/`.

| Event surface | Sprite token | Final DDS | Source / processed PNG | Status |
| --- | --- | --- | --- | --- |
| `.40` craft authorized | `GFX_report_event_016_dhrondan_craft_authorized` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_craft_authorized.dds` | `source_png/report/craft_authorized_source.png` / `processed_png/report/craft_authorized_source.png` | complete |
| `.41` envoy departure | `GFX_report_event_016_dhrondan_envoy_departure` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_envoy_departure.dds` | `source_png/report/envoy_departure_source.png` / `processed_png/report/envoy_departure_source.png` | complete |
| `.42` planetary audience | `GFX_report_event_016_dhrondan_planetary_audience` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_planetary_audience.dds` | `source_png/report/planetary_audience_source.png` / `processed_png/report/planetary_audience_source.png` | complete |
| `.43` pact return | `GFX_report_event_016_dhrondan_pact_return` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_pact_return.dds` | `source_png/report/pact_return_source.png` / `processed_png/report/pact_return_source.png` | complete |
| `.44` UFO landing | `GFX_report_event_016_dhrondan_ufo_landing` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_ufo_landing.dds` | `source_png/report/ufo_landing_source.png` / `processed_png/report/ufo_landing_source.png` | complete |
| `.45` expedition failure | `GFX_report_event_016_dhrondan_expedition_failure` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_expedition_failure.dds` | `source_png/report/expedition_failure_source.png` / `processed_png/report/expedition_failure_source.png` | complete |
| `.46` revolt warning | `GFX_report_event_016_dhrondan_revolt_warning` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_revolt_warning.dds` | `source_png/report/revolt_warning_source.png` / `processed_png/report/revolt_warning_source.png` | complete |
| `.47` rebellion | `GFX_report_event_016_dhrondan_rebellion` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_rebellion.dds` | `source_png/report/rebellion_source.png` / `processed_png/report/rebellion_source.png` | complete |
| `.49-.51` diplomatic compact | `GFX_report_event_016_dhrondan_diplomatic_compact` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_diplomatic_compact.dds` | `source_png/report/diplomatic_compact_source.png` / `processed_png/report/diplomatic_compact_source.png` | complete |
| Special-project/event support scene | `GFX_report_event_016_dhrondan_special_project_envoy_craft` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_special_project_envoy_craft.dds` | `source_png/report/special_project_envoy_craft_source.png` / `processed_png/report/special_project_envoy_craft_source.png` | complete |

## News event pictures

The sovereignty sprite and DDS are stable contracts for `.48`. The envoy and rebellion news sprites are proposed for later global news consumers.

| Surface | Sprite token | Final DDS | Source / processed PNG | Status |
| --- | --- | --- | --- | --- |
| `.48` D’Rhondan sovereignty | `GFX_news_event_016_dhrondan_sovereignty` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_sovereignty.dds` | `source_png/news/sovereignty_source.png` / `processed_png/news/sovereignty_source.png` | complete |
| Envoy craft global news | `GFX_news_event_016_dhrondan_envoy` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_envoy.dds` | `source_png/news/envoy_source.png` / `processed_png/news/envoy_source.png` | handed_off |
| Rebellion global news | `GFX_news_event_016_dhrondan_rebellion` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_rebellion.dds` | `source_png/news/rebellion_source.png` / `processed_png/news/rebellion_source.png` | handed_off |

## Country identity and faction art

| Asset | Proposed sprite token | Final DDS | Source / processed PNG | Status |
| --- | --- | --- | --- | --- |
| D’Rhondan faction emblem | `GFX_dhrondan_faction_emblem` | `gfx/interface/016_brilliant_scientist/dhrondan_faction_emblem.dds` | `source_png/identity/faction_emblem_source.png` / `processed_png/identity/dhrondan_faction_emblem.png` | complete |
| D’Rhondan country identity panel | `GFX_dhrondan_country_identity_panel` | `gfx/interface/016_brilliant_scientist/dhrondan_country_identity_panel.dds` | `source_png/identity/country_panel_source.png` / `processed_png/identity/dhrondan_country_identity_panel.png` | handed_off |

## Ownership-bounded icon surfaces

The special-project icon `sp_dhrondan_envoy_craft` and any Event016 achievement triplet are intentionally not duplicated here. Their canonical consumers are transparent gameplay icon surfaces owned by `chaosx_icon_artist`, not generated event scene art. The craft report scene above is complete and can support the special-project/event presentation. These icon rows remain `blocked` until the icon agent supplies the exact engine-facing IDs, target definitions, and DDS triplet.

| Asset | Required consumer | Status |
| --- | --- | --- |
| `sp_dhrondan_envoy_craft` special-project icon | `icons/special_projects`, 161x98 | blocked, icon-agent-owned |
| Event016 DHR achievement support icon triplet | `icons/achievements`, 64x64 completed/grey/not-eligible | blocked, icon-agent-owned |

## Validation evidence

- `notes/processed_alpha_qa.json` records every processed PNG dimensions and alpha range.
- `contact_sheets/flags_ladders.png`, `contact_sheets/report_art.png`, `contact_sheets/news_art.png`, and `contact_sheets/identity_art.png` provide visual review sheets.
- Repository converter: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- DDS QA: all 27 generated runtime DDS files checked with legacy BGRA header, exact declared dimensions, exact file length, texture caps, and alpha ranges. All checks passed. Flags, report scenes, news scenes, and country panel are opaque with alpha 255. The emblem preserves alpha 0–255.

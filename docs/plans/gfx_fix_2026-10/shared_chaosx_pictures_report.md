# Shared Chaos Redux pictures GFX repair report

Status: in progress, with 2 of 16 findings delivered and 14 findings queued for the next tranche.

Scope is limited to the `shared_chaosx_pictures` findings in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and `gfx_issues.json`.

## Accepted severity-1 repairs

The parent reviewed both processed previews on 2026-10-06 and accepted their visual treatment. The report image uses the repository's standard tilted-card processor, and the news image is an opaque black-and-white period scene. Both existing sprite names and texture paths remain valid, so no `.gfx` edit is required for these two rows.

| Finding | Status | Target `.gfx` / sprite | Runtime DDS | Target size | Source mode |
|---|---|---|---|---:|---|
| Severity 1: `GFX_report_foreign_liaison` | Handed off; parent visual review accepted, live consumer review pending | `interface/chaosx_pictures.gfx` / `GFX_report_foreign_liaison` | `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` | 210x176 | Native ImageGen, opaque documentary scene; standard report-card processing |
| Severity 1: `GFX_news_greenland_sold` | Handed off; parent visual review accepted, live consumer review pending | `interface/chaosx_pictures.gfx` / `GFX_news_greenland_sold` | `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` | 397x153 | Native ImageGen, opaque documentary scene; black-and-white crop and contrast processing |

### `GFX_report_foreign_liaison` evidence

Generated source PNG: `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_foreign_liaison_source.png` (SHA-256 `25404b7c39dfff5b110647194564abc7bf988f332ee2aebbdd64e4f8e93b113b`).

ImageGen prompt: "Use case: historical-scene. Asset type: source art for a Hearts of Iron IV report event image; the repository will apply its standard tilted paper-card treatment after generation. Scene/backdrop: a restrained 1930s diplomatic conference room with dark wood, tall windows, a plain table, and period papers with no legible writing. Subject: three anonymous male diplomats in late-1930s suits seated around the table, one passing a sealed folder; faces are incidental and not individually recognizable. Style/medium: candid 1930s press photograph, natural documentary realism, neutral monochrome tonal base with fine film grain. Composition/framing: medium-wide, table and exchange centered, leave room around the scene for a later cover crop to 210x176. Lighting/mood: soft overcast window light, guarded and formal. Constraints: opaque full-canvas photograph only; do not draw any tilted card, border, paper mat, frame, or drop shadow because those are applied later; no flags, no logos, no readable text, no modern objects, no watermark, no extra people, no theatrical expressions or poster styling."

Processed preview: `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_foreign_liaison.png` (210x176 RGBA, SHA-256 `acf712c4ce24548185ce2601d786c6f05a0b92445c3b54c936a655c433cd3e7a`).

Before-state runtime DDS snapshot: `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/report_foreign_liaison_before.dds` (SHA-256 `7ac6e7f7404a0fc9f93441e52491c427be5b68b230b84f65e8974de4c30a1f5e`); its decoded PNG is `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/report_foreign_liaison_before.png`.

Final runtime DDS: `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` (210x176, SHA-256 `3557a1c114ae0ecab3925a4b577ac0c2d58f601cea0833ea95f21aefe0213804`).

Pixel round-trip is exact between the final DDS decode and the processed PNG. The processed card has alpha range 0-255 and all four canvas corners are transparent. The before snapshot shows the modern three-official podium photograph identified by the raw issue record.

### `GFX_news_greenland_sold` evidence

Generated source PNG: `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_greenland_sold_source.png` (SHA-256 `5be1ccdbad9f5c5f81369c0955d24ab18d9094d77a6db0a685567a5919fdbd48`).

ImageGen prompt: "Use case: historical-scene. Asset type: full-canvas Hearts of Iron IV news event photograph, final target 397x153. Scene/backdrop: a remote west Greenland fjord settlement in the late 1930s, steep rocky mountains and snow beyond a calm harbor, low wooden houses clustered along the shoreline, one small period fishing boat. Subject: the distinctive Greenland coast and settlement, with no people needed. Style/medium: authentic black-and-white 1930s press photograph, natural documentary realism, crisp midtone detail, restrained film grain and high but printable contrast. Composition/framing: very wide horizontal panorama composed for a 397x153 crop, harbor and buildings across the middle third, mountain silhouette readable above them, no important detail at the extreme top or bottom. Mood: quiet, remote, politically consequential without modern editorial polish. Constraints: opaque full canvas; no map, no labels, no signs, no flags, no logos, no readable text, no modern structures or equipment, no watermark, no border or UI frame."

Processed preview: `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_greenland_sold.png` (397x153 RGB, SHA-256 `c174f0656500425c6b9edc0a9cb059ab93db0dae7cc9a95ca6ee9a0ed85cb42d`).

Before-state runtime DDS snapshot: `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/news_greenland_sold_before.dds` (SHA-256 `9161735a6997d1997efb7eb3e41557aba13b7f2d43fe6f34709ff4051f4fc96f`); its decoded PNG is `docs/assets/gfx_fix_shared_chaosx_pictures/source_runtime/news_greenland_sold_before.png`.

Final runtime DDS: `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` (397x153, SHA-256 `d634d6db22878da854becdb6e24781b7db93490c940d944ceca51afd749da69a`).

Pixel round-trip is exact between the final DDS decode and the processed PNG, and all output pixels are opaque. The before snapshot shows the labeled atlas-style map identified by the raw issue record.

### Asset manifest and `.gfx` handoff

| Sprite | Source PNG | Processed PNG | Final DDS | Background mode | `.gfx` owner | Use note |
|---|---|---|---|---|---|---|
| `GFX_report_foreign_liaison` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/report_foreign_liaison_source.png` | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/report_foreign_liaison.png` | `gfx/event_pictures/005_soviet_collapse/report_foreign_liaison.dds` | Opaque source; transparent corners from the standard report-card processor | `interface/chaosx_pictures.gfx` | Sepia 1930s diplomatic-table report image at 210x176; preserve the existing sprite and texture path. |
| `GFX_news_greenland_sold` | `docs/assets/gfx_fix_shared_chaosx_pictures/source_generated/news_greenland_sold_source.png` | `docs/assets/gfx_fix_shared_chaosx_pictures/processed/news_greenland_sold.png` | `gfx/event_pictures/092_greenland_sale/news_greenland_sold.dds` | `consumer_opaque` | `interface/chaosx_pictures.gfx` | Black-and-white 1930s Greenland coast news image at 397x153; preserve the existing sprite and texture path. |

Contact sheet produced from the owning `.gfx` family with the trailer `gfx_sheets.py` utility is retained under `docs/assets/gfx_fix_shared_chaosx_pictures/contact_sheets/severity1_contact_sheet/`. The report JPGs under `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/` were regenerated during the shared session; their current hashes are not treated as before-state evidence. The source runtime DDS snapshots above are authoritative for this tranche.

## Remaining finding statuses

These 14 findings remain queued for the next asset tranche.

| Severity | Sprite | Current runtime DDS | Status |
|---:|---|---|---|
| 2 | `GFX_report_railway_sovereignty` | `gfx/event_pictures/005_soviet_collapse/report_railway_sovereignty.dds` | Queued: create distinct sepia armoured-train or railway-junction report art. |
| 2 | `GFX_report_event_random_war` | `gfx/event_pictures/004_random_war/report_event_random_war.dds` | Queued: create sepia staff-table war-map or dice scene. |
| 2 | `GFX_report_event_greenland` | `gfx/event_pictures/092_greenland_sale/report_event_greenland.dds` | Queued: replace the labeled atlas with an unlabeled sepia coast or map scene. |
| 2 | `GFX_news_california` | `gfx/event_pictures/074_japan_california/news_california.dds` | Queued: replace the vector map with a black-and-white period California coast or fleet image. |
| 2 | `GFX_report_event_california` | `gfx/event_pictures/074_japan_california/report_event_california.dds` | Queued: replace the vector map with a sepia period scene or aged map. |
| 2 | `GFX_news_galicia` | `gfx/event_pictures/093_portugal_galicia/news_galicia.dds` | Queued: replace the GIS map with a black-and-white period scene or aged map. |
| 2 | `GFX_news_old_great_bulgaria` | `gfx/event_pictures/048_old_great_bulgaria/news_old_great_bulgaria.dds` | Queued: replace the labeled vector map with an unlabeled black-and-white period scene or aged map. |
| 2 | `GFX_report_event_old_great_bulgaria` | `gfx/event_pictures/048_old_great_bulgaria/report_event_old_great_bulgaria.dds` | Queued: replace the baked-label map with an unlabeled sepia map scene. |
| 2 | `GFX_news_infrastructure_project` | `gfx/event_pictures/055_great_infrastructure_project/news_infrastructure_project.dds` | Queued: replace the modern interchange with a black-and-white 1930s construction photograph. |
| 3 | `GFX_news_alien_spacecraft` | `gfx/event_pictures/036_alien_spacecraft/news_alien_spacecraft.dds` | Queued: replace the turbine cutaway with a black-and-white documentary-style alien craft or wreck. |
| 3 | `GFX_news_balkans` | `gfx/event_pictures/045_third_balkan_war/news_balkans.dds` | Queued: replace the labeled map with a black-and-white period scene or unlabeled aged map. |
| 3 | `GFX_news_failed_research` | `gfx/event_pictures/060_research_failure/news_failed_research.dds` | Queued: restore period press contrast and retain a distinct research-failure subject. |
| 3 | `GFX_report_event_alien_spacecraft` | `gfx/event_pictures/036_alien_spacecraft/report_event_alien_spacecraft.dds` | Queued: replace the stealth-bomber silhouette with a sepia saucer or wreck scene. |
| 3 | `GFX_report_event_tibet` | Current alias: `gfx/event_pictures/003_holy_realm/report_event_lhasa.dds`; proposed unique path: `gfx/event_pictures/003_holy_realm/report_event_tibet.dds` | Queued: create a distinct sepia monastery or plateau scene and ask the parent to repoint this sprite to the unique path. |

## Remaining live checks

After the parent reviews and integrates the final package, confirm that the report card is fully visible in its tilted thin sepia frame with transparent corners and no crop loss, and that the news event uses the opaque 397x153 black-and-white Greenland coast scene without labels or logos.

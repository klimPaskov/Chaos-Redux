# Event 021 generated event art visual re-audit — 2026-09-01

## Scope and result

This audit covers only the four static Event 021 presentation textures: `report_event_021_random_civil_war_opening`, `news_event_021_multi_front_war`, `news_event_021_global_fracture`, and `decision_category_picture_021_civil_war`.

All four assets are accepted as complete with no material visual defect found, so no source PNG, processed PNG, runtime DDS, prompt, contact sheet, manifest, or shared `gfx_handoff.md` file was replaced or edited.

Event 006 country identity, flags, portraits, focus art, and related assets were not inspected or mutated.

Event 021 custom GUI, animation, super-event, and 3D asset surfaces were not introduced or considered part of this handoff.

## Reference and consumer inspection

The canonical reference root was used directly at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`.

Opened and compared the canonical report family contact sheet and anchor references, the canonical news family contact sheet and anchor references, and the canonical `icons/decision_categories/pictures/contact_sheet.png` plus native-size category-picture anchor references.

Opened the existing Event 021 static-art contact sheet and the existing presentation runtime review sheet.

Inspected the installed Vanilla event-picture sprite definitions in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/eventpictures.gfx`, including the `GFX_news_event_001` through `GFX_news_event_005` family and `GFX_report_event_001` precedent.

Inspected the installed Vanilla decision-category picture definition `GFX_decision_cat_picture_1936_election` in `interface/decisions.gfx` and its `GRE_1936_election_category` `picture` consumer.

Inspected the current Event 021 consumers and sprite registrations without editing them: `events/021_random_civil_war.txt`, `common/decisions/categories/021_random_civil_war_categories.txt`, and `interface/021_random_civil_war.gfx`.

The current category consumer is the static decision-category `picture` field, not the 32px category icon and not a scripted-GUI background.

The current registered category sprite is `GFX_decision_category_picture_021_civil_war` at `interface/021_random_civil_war.gfx:12-13`.

The older generated-art handoff contains a historical proposal named `GFX_decision_cat_picture_021_civil_war` and a different proposed `.gfx` filename; those are not the current consumer identifiers and were not used for this audit.

## Asset-by-asset findings

| Asset | Opened source / processed / runtime decode | Visual acceptance | Consumer and handoff |
| --- | --- | --- | --- |
| `report_event_021_random_civil_war_opening` | `docs/assets/021_random_civil_war/source_png/report/report_event_021_random_civil_war_opening_imagegen_source.png` (`1536x1024`), `docs/assets/021_random_civil_war/processed_png/report/report_event_021_random_civil_war_opening.png` (`210x176`), and decoded `gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds` | Accepted. The source is an opaque period-documentary alternate-history rail-yard rupture with divided formations and civilians. The processed image uses the exact report-event tilted-card treatment: readable central scene, subtle tilt, soft shadow, transparent outer corners, and no opaque matte, fake checkerboard, readable text, UI, map, or portrait framing. Transparent corners are real alpha, not review-board pixels. | Sprite `GFX_report_event_021_random_civil_war_opening`; final DDS `gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds`; target `.gfx` `interface/021_random_civil_war.gfx:91-92`; used by the Event 021 opening report slot and report-style popup consumers. |
| `news_event_021_multi_front_war` | `docs/assets/021_random_civil_war/source_png/news/news_event_021_multi_front_war_imagegen_source.png` (`2021x778`), `docs/assets/021_random_civil_war/processed_png/news/news_event_021_multi_front_war.png` (`397x153`), and decoded `gfx/event_pictures/021_random_civil_war/news_event_021_multi_front_war.dds` | Accepted. The processed shallow strip remains a single coherent monochrome press scene: foreground checkpoint, bridge approach, and distant station-square groups remain visually separable after crop. It matches the opaque Vanilla news family and contains no montage seams, labels, text, UI, literal world map, modern props, or explosion-only composition. | Sprite `GFX_news_event_021_multi_front_war`; final DDS `gfx/event_pictures/021_random_civil_war/news_event_021_multi_front_war.dds`; target `.gfx` `interface/021_random_civil_war.gfx:95-96`; used by the Event 021 multi-front news slot. |
| `news_event_021_global_fracture` | `docs/assets/021_random_civil_war/source_png/news/news_event_021_global_fracture_imagegen_source.png` (`2020x779`), `docs/assets/021_random_civil_war/processed_png/news/news_event_021_global_fracture.png` (`397x153`), and decoded `gfx/event_pictures/021_random_civil_war/news_event_021_global_fracture.dds` | Accepted. The processed shallow strip remains one continuous international-station scene with displaced civilians, a military column, border inspection, and delegations. It matches the opaque monochrome Vanilla news family and contains no montage labels, fake newspaper layout, text, UI, literal world map, fantasy effects, or modern staging. | Sprite `GFX_news_event_021_global_fracture`; final DDS `gfx/event_pictures/021_random_civil_war/news_event_021_global_fracture.dds`; target `.gfx` `interface/021_random_civil_war.gfx:99-100`; used by the Event 021 Global Fracture news slot. |
| `decision_category_picture_021_civil_war` | `docs/assets/021_random_civil_war/source_png/category_picture/decision_category_picture_021_civil_war_imagegen_source.png` (`1254x1254`), `docs/assets/021_random_civil_war/processed_png/category_picture/decision_category_picture_021_civil_war.png` (`114x101`), and decoded `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds` | Accepted. At the verified native `114x101` family canvas the signal, torn unmarked standard, barricade, soldiers, and damaged civic building remain readable as one compact sepia scene. It has an opaque full-canvas treatment appropriate to the current consumer and no fake buttons, meters, controls, labels, map borders, literal map, watermark, or icon-only substitute. | Sprite `GFX_decision_category_picture_021_civil_war`; final DDS `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds`; target `.gfx` `interface/021_random_civil_war.gfx:12-13`; consumer `common/decisions/categories/021_random_civil_war_categories.txt:19`. |

## DDS and pixel validation

Every assigned runtime DDS was decoded independently from its current file into a temporary review folder and opened as an image.

All four DDS files have the strict legacy one-level BGRA layout: `DDS ` magic, 128-byte total header, `DDS_HEADER` size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, zero fourCC, 32-bit pixels, masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, and zero mipmaps.

| Asset | DDS length / expected | Alpha result | Processed PNG ↔ decoded DDS |
| --- | ---: | --- | --- |
| `report_event_021_random_civil_war_opening` | `147968 / 147968` bytes for `210x176` | `alpha_min=0`, `alpha_max=255`; all four corners are zero-alpha; visible bounds `[4,5]-[209,175]`; opaque bounds `[7,8]-[202,167]`; intermediate alpha is present for the soft card shadow and edges | Exact RGBA equality; SHA-256 `71fd0dfa1022ff15eb3b36b4dae4c1a28e4d5823eac90edb50d22726e7fb32ac` |
| `news_event_021_multi_front_war` | `243092 / 243092` bytes for `397x153` | Fully opaque `alpha_min=255`, `alpha_max=255`; all decoded pixels are grayscale | Exact RGBA equality; SHA-256 `8e6e85c982a93484cf199faca60d32b6bdf285f880f78078893501f8dc7206c7` |
| `news_event_021_global_fracture` | `243092 / 243092` bytes for `397x153` | Fully opaque `alpha_min=255`, `alpha_max=255`; all decoded pixels are grayscale | Exact RGBA equality; SHA-256 `2466f59663659c98fee92eff22456084501b4335babcb4321cc97e7be0582068` |
| `decision_category_picture_021_civil_war` | `46184 / 46184` bytes for `114x101` | Fully opaque `alpha_min=255`, `alpha_max=255`, matching the requested full-canvas category-picture treatment | Exact RGBA equality; SHA-256 `f0a4718abbe76971741cdee0670904b36de2b454cf7b2b9178f217d2d63a753e` |

The repository-standard `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was rerun against each processed PNG into a temporary output folder. Each converter output was byte-identical to the current runtime DDS, confirming source-package/runtime equivalence after the required processing step.

Raw source PNG equality with runtime pixels is not expected for these assets because the report processor adds the required card treatment and all four assets are cropped/resized into their distinct engine canvases. The processed PNG and decoded runtime DDS are exactly equivalent for every asset.

## Existing evidence and changes

The existing contact sheet `docs/assets/021_random_civil_war/contact_sheets/021_random_civil_war_static_art_contact_sheet.png` was opened and already shows all four source/processed presentation packages with dimensions and review-only checkerboard context.

No new contact sheet was needed because no alternatives were generated and no asset changed.

Only this handoff file was added: `docs/plans/021_random_civil_war_plans/subagent_handoffs/generated_event_art_visual_reaudit_2026-09-01.md`.

The four source PNGs, four processed PNGs, four runtime DDS files, prompts, existing contact sheets, `docs/assets/021_random_civil_war/manifest.md`, and `docs/assets/021_random_civil_war/gfx_handoff.md` were not edited.

The manifest and shared asset handoff were already modified in the dirty worktree before this audit and were preserved for the parent-owned reconciliation.

## Blockers and simplifications

None for the four assigned assets. No replacement, fallback, placeholder, cross-family resize, fake UI, opaque report matte, DDS repair, or source-mode simplification was used.

Parent-owned follow-up remains limited to reconciling shared manifest/GFX handoff text and any final runtime wiring decisions; this audit found no asset-side blocker or visual repair requirement.

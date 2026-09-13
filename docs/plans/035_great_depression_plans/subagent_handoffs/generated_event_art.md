# Event 35 generated event-art subagent handoff

## Disposition

This is the original asset-worker handoff. Parent-owned sprite and gameplay wiring is complete; `docs/assets/035_great_depression/manifest.md` is the current runtime source of truth. Any `Proposed`, `needs_user_review`, or pending-wiring wording below records the worker handoff state rather than an unresolved runtime task.

Production scope: non-portrait generated report, news, decision-category picture, and Evolution III super-event imagery for Event 35 Great Depression 2.0.

Source mode: official built-in ImageGen for all eight assets. These are fictional country-neutral period scenes. No external source was used and no historical source attribution is claimed.

Canonical references inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event/contact_sheet.png`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/contact_sheet.png`.

Processing evidence: report scenes used `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`; news and category scenes used deterministic smooth crop/resize and monochrome or contrast processing; every DDS used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. All final DDS files passed strict legacy BGRA header, one-level, exact-length, dimension, and alpha validation and were decoded back into `docs/assets/035_great_depression/processed_png/decoded_dds/`.

## Asset inventory

| Asset | Source PNG and dimensions | Processed PNG and dimensions | Final DDS and dimensions | Consumer | Sprite and target `.gfx` | Source SHA-256 | Processed SHA-256 | DDS SHA-256 | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `report_event_great_depression` | `docs/assets/035_great_depression/source_png/report_event_great_depression_source.png` 1536x1024 RGB | `docs/assets/035_great_depression/processed_png/report_event_great_depression.png` 210x176 RGBA, alpha 0-255 | `gfx/event_pictures/035_great_depression/report_event_great_depression.dds` 210x176 BGRA, alpha 0-255 | `chaosx.nr35.1` independent national opening report | Existing `GFX_report_event_great_depression`, `interface/chaosx_pictures.gfx` | `9859620c652f2ae0ce32bd7122bfa0319e47b060baa5c3ba7a55bb96c95940d6` | `a2abe779952722cd6dea01c28c3e82d3beeee66ffb2587a09b95e43eba2e4e96` | `df5a1a72470aa42d679e03a625df577991c1dc8f5669577c352328559dead384` | `needs_user_review` |
| `report_event_great_depression_boom_collapse` | `docs/assets/035_great_depression/source_png/report_event_great_depression_boom_collapse_source.png` 1536x1024 RGB | `docs/assets/035_great_depression/processed_png/report_event_great_depression_boom_collapse.png` 210x176 RGBA, alpha 0-255 | `gfx/event_pictures/035_great_depression/report_event_great_depression_boom_collapse.dds` 210x176 BGRA, alpha 0-255 | Event 34 Industrial Boom collapse inheritance report | Proposed `GFX_report_event_great_depression_boom_collapse`, `interface/035_great_depression_event_pictures.gfx` | `244f2dff17ca8e4af8291efcd699fca0f62d1cb7d6d6546dbb922a94f8c414ca` | `e8e7f02d81f06748fa259f80d320384fe0081b7deacf6c36960d7156c08a5715` | `3c38c8229c069c8012dd07dbea7fec46ad3f0212f4d6ab0cc25a636027986c4f` | `needs_user_review` |
| `report_event_great_depression_contagion` | `docs/assets/035_great_depression/source_png/report_event_great_depression_contagion_source.png` 1536x1024 RGB | `docs/assets/035_great_depression/processed_png/report_event_great_depression_contagion.png` 210x176 RGBA, alpha 0-255 | `gfx/event_pictures/035_great_depression/report_event_great_depression_contagion.dds` 210x176 BGRA, alpha 0-255 | Financial and trade contagion conversion report | Proposed `GFX_report_event_great_depression_contagion`, `interface/035_great_depression_event_pictures.gfx` | `74e3bfcc35ee8c1665af0765b6bd468b1fda9031ab1a01a5cb107c3c9631f303` | `c7ff7c2a547878e14d42e036f31a270648539b0c7d362100ae1815aa953f4b94` | `2f7d68860850c193ffb0365e04fe270bf65139ee05fe0cb81eae545a7d6d7602` | `needs_user_review` |
| `report_event_great_depression_social_collapse` | `docs/assets/035_great_depression/source_png/report_event_great_depression_social_collapse_source.png` 1536x1024 RGB | `docs/assets/035_great_depression/processed_png/report_event_great_depression_social_collapse.png` 210x176 RGBA, alpha 0-255 | `gfx/event_pictures/035_great_depression/report_event_great_depression_social_collapse.dds` 210x176 BGRA, alpha 0-255 | Social Collapse strike, occupation, or conflict milestone report | Proposed `GFX_report_event_great_depression_social_collapse`, `interface/035_great_depression_event_pictures.gfx` | `fefc2e7524445c6e5a99b8c8fb13ccb9d24289e78ee5f426285c1c91dd4787e5` | `41f7fde5dbb4556ea198095d958b7e1a6d86616efe2203b158e08fa9aa54f0ed` | `e7a3f51d6d2524c907b75d58b944840a804784d73bbc907ded193b996bb1eee3` | `needs_user_review` |
| `report_event_great_depression_recovery` | `docs/assets/035_great_depression/source_png/report_event_great_depression_recovery_source.png` 1536x1024 RGB | `docs/assets/035_great_depression/processed_png/report_event_great_depression_recovery.png` 210x176 RGBA, alpha 0-255 | `gfx/event_pictures/035_great_depression/report_event_great_depression_recovery.dds` 210x176 BGRA, alpha 0-255 | International or Evolution III recovery report | Proposed `GFX_report_event_great_depression_recovery`, `interface/035_great_depression_event_pictures.gfx` | `5dadcba711d66c300351edeb7281f0b3b72ef99f4dac7c5e8c2314f47a531254` | `27da4feb39250afdba8cfd2dbee6df6631a112ae3cf6899fb7a8e5e5eb29986f` | `b5b9a33d231fe9d29117936381cc76640183b8baa9d31e804a29289c81028c2b` | `needs_user_review` |
| `news_event_great_depression` | `docs/assets/035_great_depression/source_png/news_event_great_depression_source.png` 2021x778 RGB | `docs/assets/035_great_depression/processed_png/news_event_great_depression.png` 397x153 RGBA, alpha 255-255 | `gfx/event_pictures/035_great_depression/news_event_great_depression.dds` 397x153 BGRA, alpha 255-255 | Public national contraction news event | Proposed `GFX_news_event_great_depression`, `interface/035_great_depression_event_pictures.gfx` | `944e439c7a890c8aeee3cecb1cd5a7817aba80e57b7dd3f6ab4c173ad600d2ae` | `a6e6022ea337af2e846c8161a4db44f82aa5275d93772c5c8303b52d31fc356e` | `a0733482ddbb540a29910889ce529851f83935ff0e83cd30849c0b2468b9052c` | `needs_user_review` |
| `decision_cat_picture_great_depression` | `docs/assets/035_great_depression/source_png/decision_cat_picture_great_depression_source.png` 1254x1254 RGB | `docs/assets/035_great_depression/processed_png/decision_cat_picture_great_depression.png` 114x101 RGB opaque | `gfx/interface/decisions/035_great_depression/decision_cat_picture_great_depression.dds` 114x101 BGRA, alpha 255-255 | Great Depression decision category picture | Proposed `GFX_decision_cat_picture_great_depression`, `interface/035_great_depression_event_pictures.gfx` | `4dbd52349e9c9c170f31ca7247b351a2787edeb861fec0e1c1e41baabed340a3` | `f90b033ecc4fa3e162764afacf402ba398327a981a845385a50ee644df178caa` | `b041aa9068a240c4d30ef4c4c322b5d37bde196e7beb45a53b03115fe94e4c58` | `needs_user_review` |
| `super_event_great_depression` | `docs/assets/035_great_depression/source_png/super_event_great_depression_source.png` 1479x1063 RGB | `docs/assets/035_great_depression/processed_png/super_event_great_depression.png` 457x328 RGB opaque | `gfx/super_events/035_great_depression/super_event_great_depression.dds` 457x328 BGRA, alpha 255-255 | Evolution III The Second Great Depression global super-event | Proposed `GFX_super_event_035_great_depression`, `interface/035_great_depression_super_event.gfx` | `a866c5ab814812e23a9af18bff9b2bdc89daa86fc380ddd7ae7fddff5ff10818` | `5a3507a37e3788d60dd80f2133cc3758d587e12e4c02a6eca87f1511423a08e3` | `d443047390bc4e7b70755a6c36f0f567b9707174fe8109338d5056d4c8e6918f` | `needs_user_review` |

## Review and remaining wiring

Contact sheets: `docs/assets/035_great_depression/contact_sheets/event35_scene_contact_sheet.png` and `docs/assets/035_great_depression/contact_sheets/event35_scene_roundtrip_contact_sheet.png`.

The previous opening DDS was preserved before replacing the stable texture path at `docs/assets/035_great_depression/reference_previews/current_report_event_great_depression_original.dds`, with decoded preview at `docs/assets/035_great_depression/reference_previews/current_report_event_great_depression.png`.

No GFX file, gameplay file, event file, localisation file, achievement file, portrait file, icon family, or workbook file was edited. The parent must register the seven proposed sprites, wire the new report/news/category/super-event consumers, visually review the contact sheets, and perform the final runtime validation.

No asset is blocked. All eight rows are `needs_user_review` because the parent-owned sprite registration, branch wiring, and final review remain outstanding.

## Mapped assets outside this handoff

The full Event 35 asset prompt also names icon and achievement families that are intentionally not produced by `chaosx_generated_event_art`. They remain unmapped by this handoff and require their assigned asset route before Event 35 visual completion.

- Decision-category icon, Cabinet Review icon, Emergency Public Works icon, Rescue Strategic Industry icon, Stabilize Finance and Trade icon, Austerity and Retrenchment icon, Direct State Planning icon, and Let the Market Clear icon require the decision or icon asset route.
- Halt the Panic, Keep Essential Freight Moving, Reopen Depression Center, Prevent a Relapse, Maximum-Severity Emergency, Contain Financial Contagion, Prevent a General Strike, and International Reconstruction mission icons require the mission icon route.
- Opening Economic Shock, Active Great Depression, Economic Contagion, Global Contraction, Post-Depression Recovery, recovery doctrine legacies, and recovery scars require the idea or national-condition icon route.
- Distressed Center, Idled Center, Shuttered Center, Abandoned Works, Protected Center, Public Works Active, Reopened Center, and Hollowed Industrial District state-modifier icons require the state-modifier icon route.
- Financial Contagion, Social Collapse, and The Second Great Depression Event Details evolution icons require the evolution icon route if the shared interface consumes them.
- The six Event 35 achievement triplets require the achievement asset route and are not included here.
- Evolution III audio and researched text or quote material are separate super-event research handoffs and are not included here.

No Event 35 character portraits, flags, faction emblems, or 3D assets are included in the accepted baseline for this scene-art package.

## Asset package paths

- Prompts: `docs/assets/035_great_depression/prompts/generated_scene_prompts.md`.
- Source PNGs: `docs/assets/035_great_depression/source_png/`.
- Processed PNGs: `docs/assets/035_great_depression/processed_png/`.
- DDS round-trip previews: `docs/assets/035_great_depression/processed_png/decoded_dds/`.
- Contact sheets: `docs/assets/035_great_depression/contact_sheets/`.
- Detailed manifest: `docs/assets/035_great_depression/manifest.md`.
- GFX handoff: `docs/assets/035_great_depression/gfx_handoff.md`.

# Event 013 Natural Disasters static-asset validation

Validation date: 2026-07-10

Scope: accepted non-animation completion assets from the 2026-07-10 pass, plus the nine older DDS files explicitly flagged for 24-bit normalization by `docs/plans/013_natural_disasters_plans/013_asset_audit.md`.

## Coverage checked

- 13 added Part 8 report identities
- 1 added live-reference regional-aftermath report identity
- 5 added deep-family news identities
- 7 added decision icons
- 7 added idea or state-modifier icons
- 1 Natural Disaster Aftermath category icon
- 8 Part 9 abnormal-GUI static assets
- 2 retained Part 6 super-event images
- 10 accepted achievement identities with completed, grey, and not-eligible variants
- 8 older news/super-event DDS format corrections with unchanged source art
- 1 provenance-closed `super_event_nd_storm_corridor` source replacement under the stable identity

## Dimension and presentation results

- All 14 new report images are `210x176` RGBA report cards.
- All four corner pixels are transparent on every new report card.
- All 5 new news images are `397x153` and strictly grayscale after press-image processing.
- Both new super-event images are `457x328` and strictly grayscale after processing.
- Decision icons are `32x32`; the aftermath category icon is `53x40`; idea/state icons are `64x64`.
- The abnormal GUI panel pair is `760x520`; the card frame is `280x124`; the three markers/badges are `48x48`; the progress frame/fill are `280x24` and `276x16`.
- All 30 accepted achievement processed variants are `64x64`.

## DDS format and delivery results

The DDS headers were read directly for the 83 files in the completion/normalization set.

- 83 of 83 package DDS files use 32-bit RGB+A masks `00FF0000/0000FF00/000000FF/FF000000`.
- 83 of 83 package DDS dimensions match their processed PNG targets.
- 83 of 83 live DDS copies are byte-identical to the package DDS copies by SHA-256.
- The nine previously 24-bit news/super-event identities are included in those 83 checks and use the same 32-bit BGRA-style format. Eight retain their earlier source art; `super_event_nd_storm_corridor` now uses the fresh generated source documented below.

## Storm-corridor provenance closure

`super_event_nd_storm_corridor` was regenerated as the accepted sustained multi-state moving storm/tornado corridor rather than a local-storm fallback. The final scene shows a broad storm shelf, four separated funnels, a continuous damaged rail and road axis, multiple settlements, and a period rescue/evacuation convoy.

- exact prompt/result ledger: `docs/assets/013_natural_disasters/prompts/2026-07-10_static_completion_prompts.md`, built-in result `exec-f951d9ec-e1c4-49e2-bab7-fbdee7797b5a.png`
- source PNG: `1480x1063`, SHA-256 `7529ED415D7B634A2313D5F0E7F536C1B2D6847935200F0C87FCCF31311467D8`
- processed PNG: strict-grayscale `457x328`, SHA-256 `ADBE2F074FE311F2C4F9331C6F8C367E0308D83560285D835DDD833BA7DCC600`
- package DDS: `457x328` 32-bit RGB+A, SHA-256 `F39B90157F255AA56CB4D0BD4AD5DA778FDD82B12605165897FCE406A2431103`
- live DDS: byte-identical to package DDS, SHA-256 `F39B90157F255AA56CB4D0BD4AD5DA778FDD82B12605165897FCE406A2431103`
- stable sprite and slot contract: `GFX_super_event_nd_storm_corridor`, slot `70`

## Achievement overlay result

The asset-skill overlay path was absent in this checkout. The repository treatment was recovered from the eight existing Event 013 grey/not-eligible DDS pairs rather than replaced with a tint or hand-drawn cross.

- recovered overlay: `docs/assets/013_natural_disasters/source_png/achievement_not_eligible_overlay_recovered.png`
- non-zero-alpha coverage: 939 of 4096 pixels
- mean reconstruction error across the eight existing pairs: `0.07/255` pixel RMSE
- all ten accepted not-eligible PNGs were composited from the corresponding grey PNG plus that recovered overlay

## Visual review

The following current contact sheets were reviewed after final processing:

- `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_report_contact_sheet.png`
- `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_specific_news_contact_sheet.png`
- `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_decision_icons_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_idea_icons_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_abnormal_gui_static_contact.png`
- `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_super_events_contact_sheet.png`
- `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_achievements_contact.png`

The new report and news identities remain distinguishable at final size, including meteor impact versus meteor shower, storm surge versus tsunami, ashfall versus eruption, wet mass movement versus lahar, extreme wind versus tornado outbreak, and broad regional aftermath versus any single-disaster report. The refreshed storm-corridor super-event remains readable at final size and visibly communicates sustained route motion through the rail/road axis, repeated funnels, sequential damage, towns, and relief traffic. Transparent icons show no opaque square backdrop or white matte in the contact sheets.

## Wiring boundary

This section records the original asset-subtask boundary. Parent integration closed it on 2026-07-10: the dedicated report/news identities are registered in `interface/013_natural_disasters.gfx`, the matching family events use those sprites in `events/013_natural_disasters.txt`, and the final texture-resolution scan found no missing Event 013 DDS path.

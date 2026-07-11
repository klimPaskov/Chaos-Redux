# System Camp Repression Rework Report and Super-Event Art Validation

## Build result

The package was processed with:

```text
python docs/assets/system_camp_repression_rework/tools/build_report_super_event_assets.py
```

Result:

- 12 report cards validated at exactly `210x176`;
- five super-event images validated at exactly `457x328`;
- all 17 DDS files use one mip and 32-bit BGRA/B8G8R8A8-style channel masks;
- each DDS decodes pixel-identically to its processed PNG;
- every report card has transparent corner pixels and visible tilted-card edge space;
- all 17 source SHA-256 hashes are unique;
- all 17 processed SHA-256 hashes are unique.

The verified report-card processor had SHA-256 `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`. It is the same processor identity used by the accepted Event 011 raster pipeline. No alternate card treatment was substituted.

## Visual review

The following review surfaces were inspected at original resolution:

- `docs/assets/system_camp_repression_rework/contact_sheets/report_super_event_source_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/report_event_processed_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/super_event_processed_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/super_event_ui_mask_preview_contact_sheet.png`

The final report cards preserve their intended focal subject after the local `192x153` card crop, tilt, shadow, and sepia treatment. The five super-event images remain legible through the current `gfx/super_events/super_event_template.psd` image aperture.

Visual acceptance found no final instance of:

- a recognizable real person;
- readable generated text;
- a swastika, SS rune, or rising-sun flag;
- protected-class selector boards, lineups, or target imagery;
- blood, bodies, human remains, graphic medical procedures, or graphic gore;
- a modern vehicle, computer display, hazard suit, or UI overlay.

The initial Pingfang super-event attempt was rejected because the generated building displayed the readable number `731`. It was not copied into the repository. A separate generation call produced the selected blank-facade source, which passed visual review.

## Sprite and consumer readback

Every requested stable sprite ID appears exactly once in its current `.gfx` file. Every Japan and Soviet report ID appears exactly once in its live event file. Each of the five super-event sprites appears exactly once in `interface/chaosx_super_events.gfx` and exactly once in the `GetSuperEventImage` mapping.

| Surface | GFX definition count | Live consumer / slot-map count |
| --- | ---: | ---: |
| `GFX_report_event_pingfang_authority` through `GFX_report_event_pingfang_tribunal` | `1` each | `1` each |
| `GFX_report_event_soviet_famine_warning` through `GFX_report_event_soviet_records_discovered` | `1` each | `1` each |
| `GFX_super_event_angel_directorate` | `1` | `1` |
| `GFX_super_event_camp_global_discovery` | `1` | `1` |
| `GFX_super_event_camp_soviet_famine_catastrophe` | `1` | `1` |
| `GFX_super_event_camp_pingfang_exposure` | `1` | `1` |
| `GFX_super_event_camp_colonial_reckoning` | `1` | `1` |
| `GFX_report_event_auschwitz_discovery` | `1` | `1` |

The Germany consumer is `chaosx_genocide.56` in `events/genocide_crisis_events.txt`; its source, processed PNG, DDS, GFX definition, and live event reference are complete.

## Blockers and simplifications

No asset-production blocker or simplification remains. No requested identity was omitted, reused, or delivered as a placeholder.

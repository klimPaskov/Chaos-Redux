# Event 020 evolution report-art handoff

Date: 2026-08-01.

Scope: bounded generated non-model report-art package for the five actual Black Plague evolution reports. The producer used the official built-in ImageGen workflow after inspecting the canonical report/news reference families. No gameplay, localisation, GUI, event, focus, decision, country, spreadsheet, or `.gfx` file was edited.

## Completed outputs

| Evolution report | Source PNG | Processed PNG | Final DDS | Proposed sprite |
| --- | --- | --- | --- | --- |
| Evolution I stronger strain | `docs/assets/020_black_plague/evolution_art/source_png/report_event_020_evolution_i_stronger_strain_source.png` | `docs/assets/020_black_plague/evolution_art/processed_png/report_event_020_evolution_i_stronger_strain.png` | `gfx/event_pictures/020_black_plague/report_event_020_evolution_i_stronger_strain.dds` | `GFX_report_event_020_evolution_i_stronger_strain` |
| Evolution II overseas spread | `docs/assets/020_black_plague/evolution_art/source_png/report_event_020_evolution_ii_overseas_spread_source.png` | `docs/assets/020_black_plague/evolution_art/processed_png/report_event_020_evolution_ii_overseas_spread.png` | `gfx/event_pictures/020_black_plague/report_event_020_evolution_ii_overseas_spread.dds` | `GFX_report_event_020_evolution_ii_overseas_spread` |
| Evolution III Rat Nation flag | `docs/assets/020_black_plague/evolution_art/source_png/report_event_020_evolution_iii_rat_nation_flag_source.png` | `docs/assets/020_black_plague/evolution_art/processed_png/report_event_020_evolution_iii_rat_nation_flag.png` | `gfx/event_pictures/020_black_plague/report_event_020_evolution_iii_rat_nation_flag.dds` | `GFX_report_event_020_evolution_iii_rat_nation_flag` |
| Evolution IV Rat King coronation | `docs/assets/020_black_plague/evolution_art/source_png/report_event_020_evolution_iv_rat_king_coronation_source.png` | `docs/assets/020_black_plague/evolution_art/processed_png/report_event_020_evolution_iv_rat_king_coronation.png` | `gfx/event_pictures/020_black_plague/report_event_020_evolution_iv_rat_king_coronation.dds` | `GFX_report_event_020_evolution_iv_rat_king_coronation` |
| Evolution V terminal route | `docs/assets/020_black_plague/evolution_art/source_png/report_event_020_evolution_v_terminal_route_source.png` | `docs/assets/020_black_plague/evolution_art/processed_png/report_event_020_evolution_v_terminal_route.png` | `gfx/event_pictures/020_black_plague/report_event_020_evolution_v_terminal_route.dds` | `GFX_report_event_020_evolution_v_terminal_route` |

The review contact sheet is `docs/assets/020_black_plague/contact_sheets/event20_evolution_report_art_contact_sheet.png`.

## Validation evidence

All source images are retained RGB ImageGen masters at 1536x1024, except Evolution V at 1537x1023. All processed previews are RGBA `210x176` with alpha range `0-255` and were produced with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.

All five DDS files were produced by `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and pass the complete legacy one-level BGRA checks: `DDS ` magic, header size `124`, dimensions `210x176`, pixel-format size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, exact length `147968` bytes, and alpha range `0-255`.

Final DDS SHA-256 values are `377c31affe075ab77264d0ad492426799ca40081eaa38932d3424bcf4cb7228e` (Evolution I), `8e85150e0ee4069f91e8d1b34c583e042e04f3c01262d5a9ac6f8a6a74d1ea55` (Evolution II), `b210f1a721a989d289f9133742d2b0207a6af5fa13ca7b6e93d8d625320e305c` (Evolution III), `831f3864f610f25933150367359a43b2f9ec6607fe14125507ccac432636395c` (Evolution IV), and `df47e8450e147a9354ed33f2090f87e3c7d5602098a3cd1c14f982b546205e54` (Evolution V).

## Parent actions and remaining risks

Parent integration is complete. `interface/020_black_plague_event_pictures.gfx` defines all five stable sprites, and `events/020_black_death.txt` binds them to `chaosx.nr20.20`, `.30`, `.40`, `.50`, and `.60` respectively. The five final DDS files pass the exact 210x176 legacy BGRA checks and have no missing texture paths. Final in-game visual approval remains a user-side gate. The temporary evidence workspace remains ignored but available for provenance while Event 20 is active.

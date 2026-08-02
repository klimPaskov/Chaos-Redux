# Event 016 report-art wiring handoff

Date: 2026-08-02

## Scope

This bounded non-model tranche promoted three existing generated Event 016 report masters into runtime DDS files and assigned them to the three ordinary institutional dossiers whose subjects match the scenes. It does not change project costs, decisions, event timing, route rewards, evolution count, or country setup.

## Runtime assets and consumers

| Runtime DDS | Sprite | Consumer |
| --- | --- | --- |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_first_laboratory.dds` | `GFX_report_event_016_brilliant_scientist_first_laboratory` | `chaosx.nr16.4` laboratory/state briefing |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_university_competition.dds` | `GFX_report_event_016_brilliant_scientist_university_competition` | `chaosx.nr16.5` assistant/school conflict |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_security_expansion.dds` | `GFX_report_event_016_brilliant_scientist_security_expansion` | `chaosx.nr16.10` loyalty dossier |

The source masters are retained in the ignored asset workspace under `docs/assets/016_brilliant_scientist/report_news_expansion/source_masters/report/`. Each runtime file is `210x176`, uncompressed 32-bit BGRA DDS with the same header contract as the existing Event 016 report package. The three processed scenes were visually reviewed at native size.

## Superseded source-master note

The computation/electronics and materials/rocketry breakthrough masters were deferred by this earlier three-scene handoff because the shared `chaosx.nr16.6` report then had one static picture. They are now processed and wired by `016_breakthrough_report_art_wiring_2026-08-02.md` through scripted localisation; this note remains to explain why those two files are absent from the original three-scene package.

## Ownership and validation

The parent owns `.gfx` registration, event picture assignment, localisation and final validation. Focus, decision, character, country, spreadsheet, GUI, audio, and 3D surfaces were not changed by this tranche. The parent checked the three DDS headers, runtime path existence, sprite references, and the affected event IDs with the offline Event Inspector.

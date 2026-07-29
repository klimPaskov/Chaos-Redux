# Event 012 Africa narrative-image manifest

This package contains the twenty generated narrative images requested by the Event 012 Africa asset matrix: ten sepia report-event cards, six black-and-white news panoramas, and four color super-event scenes.

All source masters were generated with the official ImageGen workflow using only the matching canonical vanilla event-art family as visual reference. The generated scenes are alternate-history and symbolic, with period 1930s–1940s technology, clothing, transport, architecture, and reportage composition. No readable text, watermark, UI artifact, or modern prop is present.

## Runtime assets

| Family | Runtime folder | Dimensions | Assets |
| --- | --- | ---: | --- |
| Report event | `gfx/event_pictures/012_africa/` | 210x176 | `report_event_012_africa_entry_proclamation`, `report_event_012_africa_first_protection_request`, `report_event_012_africa_first_defended_partner`, `report_event_012_africa_first_failed_guarantee`, `report_event_012_africa_first_regional_congress`, `report_event_012_africa_first_member_departure`, `report_event_012_africa_first_restoration`, `report_event_012_africa_first_diaspora_arrival`, `report_event_012_africa_first_continental_corridor`, `report_event_012_africa_first_high_chaos_manifestation` |
| News event | `gfx/event_pictures/012_africa/` | 397x153 | `news_event_012_africa_league_formation`, `news_event_012_africa_colonial_withdrawal`, `news_event_012_africa_rival_bloc`, `news_event_012_africa_is_one`, `news_event_012_africa_scramble_response`, `news_event_012_africa_continental_war` |
| Super-event | `gfx/super_events/012_africa/` | 457x328 | `super_event_012_africa_africa_is_one`, `super_event_012_africa_scramble_response`, `super_event_012_africa_continental_wars`, `super_event_012_africa_the_world` |

The report masters were processed through `process_report_event_image.py`; news masters were cover-fitted, autocontrasted, and converted to grayscale; super-event masters were cover-fitted and lightly contrast-tuned. Every final DDS was created with the repository `convert_to_dds.py` converter.

Source masters are in `source_generated/` and mirrored in `source_png/`. Processed previews are in `processed_png/`. DDS-decoded previews and contact sheets are in `comparison/`. The package does not edit `.gfx`, gameplay, localisation, or audio files.

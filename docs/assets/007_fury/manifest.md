# Event 007 Fury Asset Manifest

## Final Wiring

| Use | Current ID | Current asset | Final target |
| --- | --- | --- | --- |
| report event | `chaosx.nr7.2`, `chaosx.nr7.50`, `chaosx.nr7.51`, `chaosx.nr7.52` | final Fury-specific DDS | `gfx/event_pictures/fury/fury_war_office.dds` |
| first conquest news | `chaosx.news.7007` | final Fury-specific DDS | `gfx/event_pictures/fury/fury_first_conquest.dds` |
| major super-event | slot `59` | generated final DDS from `docs/assets/007_fury/super_events/fury_becomes_a_state/processed_png/fury_becomes_a_state.png` | `gfx/super_events/fury_becomes_a_state.dds` |
| major super-event audio | audio ID `59` | `music/fury_becomes_a_state.ogg` / `sound/chaosx_super_event_fury_becomes_a_state.wav` | final `Fury Becomes a State` audio track |
| world-end super-event | slot `60` | generated final DDS from `docs/assets/007_fury/super_events/world_in_fury/processed_png/super_event_world_in_fury.png` | `gfx/super_events/super_event_world_in_fury.dds` |
| world-end super-event audio | audio ID `60` | `music/super_event_world_in_fury.ogg` / `sound/chaosx_super_event_world_in_fury.wav` | final `The World in Fury` audio track |
| Fury War Office category | `fury_war_office_category` | final Fury-specific DDS | `gfx/interface/decisions/fury/decision_category_fury_war_office.dds` |
| Anti-Fury category | `anti_fury_response_category` | final Fury-specific DDS | `gfx/interface/decisions/fury/decision_category_anti_fury.dds` |
| achievements | `achievement_fury_*` | final Fury-specific DDS triplets generated from Fury super-event art | `gfx/achievements/achievement_fury_*.dds` |

## Final Sprite Records

Report, news, idea, decision, category, and key focus branch sprite aliases are registered in `interface/007_fury.gfx`. Report/news source and processed PNGs are documented in `docs/assets/007_fury/event_images/manifest.md`; UI icon source and processed PNGs are documented in `docs/assets/007_fury/ui_icons/manifest.md`.

Final achievement sprite aliases are already registered in `interface/chaosx_achievements.gfx`. Source and processed PNGs are documented in `docs/assets/007_fury/achievement_icons/manifest.md`.

## Handoff Notes

The current implementation intentionally keeps stable code identifiers while using final Fury-specific UI assets. Fury report, news, and super-event images should present Fury as a rogue-country rage outbreak, not as a war-room, map-table, ledger, or route-planning scene.

The major super-event sprite is registered in `interface/chaosx_super_events.gfx` and points at `gfx/super_events/fury_becomes_a_state.dds`, which has generated final art with source and processed PNGs under `docs/assets/007_fury/super_events/fury_becomes_a_state/`. The terminal world-end sprite is registered there and points at `gfx/super_events/super_event_world_in_fury.dds`, which has generated final art with source and processed PNGs under `docs/assets/007_fury/super_events/world_in_fury/`. Achievement icon triplets are final Fury-specific DDS files under `gfx/achievements/` with source notes in `docs/assets/007_fury/achievement_icons/manifest.md`. Report, news, idea, decision, and key focus icons are final Fury-specific DDS files under `gfx/event_pictures/fury/` and `gfx/interface/` with source notes in `docs/assets/007_fury/event_images/manifest.md` and `docs/assets/007_fury/ui_icons/manifest.md`.

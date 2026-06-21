# Event 012 Africa Super-Event Audio Manifest

Updated: `2026-06-21`

Scope: live Event 012 Africa super-event audio for slots `68-80`.

The live package was refreshed on `2026-06-21` after the prior package's European anthem, classical, military-band, and liturgical direction was rejected. The current live `music/super_event_africa_*.ogg` files, canonical `docs/assets/012_africa/super_events/audio/final/*.ogg` copies, and `sound/chaosx_super_event_africa_*.wav` wrappers now use African-source live-performance recordings from Wikimedia Commons.

Detailed source pages, license evidence, transformation notes, source hashes, final hashes, and the source-diversity caveat are preserved in:

- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/manifest.md`
- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/handoff.md`

## Live Slot Package

| Role label | Slot / audio id | Final file | Current source title | License | Duration |
| --- | --- | --- | --- | --- | --- |
| `africa_is_one_unification` | `68` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg` | `Rush Peace dance concert 1 libtheora` | `CC BY-SA 4.0` | `120s` |
| `africa_scramble_reaction` | `69` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_scramble.ogg` | `Kagoma Drummer` | `CC BY-SA 4.0` | `118s` |
| `africa_old_seats_reveal` | `70` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_old_seats.ogg` | `Traditional Sounds - Igbo Language - Nsukka - Enugu State - Nigeria` | `CC BY-SA 4.0` | `112s` |
| `africa_counterfeit_crowns` | `71` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_counterfeit_crowns.ogg` | `Rush Peace dance concert 2 libtheora` | `CC BY-SA 4.0` | `118s` |
| `africa_world_is_one_terminal` | `72` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one.ogg` | `Ghana Dancers Group` | `CC BY-SA 4.0` | `120s` |
| `africa_continent_sponsor` | `73` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_continent_sponsor.ogg` | `Bawa Dance libtheora` | `CC BY-SA 4.0` | `120s` |
| `africa_rsa_allies_peace` | `74` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_rsa_allies_peace.ogg` | `Mapoch.- Playing music in Ndebele Village` | `CC BY-SA 4.0` | `116s` |
| `africa_dynamic_cross_continent_union` | `75` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_dynamic_cross_continent_union.ogg` | `Rush Peace dance concert 1 libtheora` | `CC BY-SA 4.0` | `118s` |
| `africa_forest_parliament_reveal` | `76` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_forest_parliament.ogg` | `Southern Ndebele music video` | `CC BY-SA 4.0` | `118s` |
| `africa_world_root_mandate` | `77` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_root.ogg` | `Traditional Adowa dance form and music performance` | `CC BY-SA 2.0 Generic` | `120s` |
| `africa_parliament_of_root_and_fang_escalation` | `78` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_root_and_fang.ogg` | `Live Band at a Traditional Marriage - Igbo Tribe - Imo State - Nigeria` | `CC BY-SA 4.0` | `117.8s` |
| `africa_archive_world_union_terminal` | `79` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_archive_world.ogg` | `Rush Peace dance concert 1 libtheora` | `CC BY-SA 4.0` | `120s` |
| `africa_world_is_one_root_variant_terminal` | `80` audio id, visible slot `72` | `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one_root_terminal.ogg` | `Traditional Sounds - Igbo Language - Nsukka - Enugu State - Nigeria` | `CC BY-SA 4.0` | `120s` |

## Live Wiring

No script or `.asset` id changed. Existing sound definitions in `sound/chaosx_sound.asset` still point at `sound/chaosx_super_event_africa_*.wav`, and existing music definitions still point at `music/super_event_africa_*.ogg`.

Each live `music/` file matches the corresponding canonical `docs/assets/012_africa/super_events/audio/final/` file by SHA-256. Each live WAV wrapper was regenerated from the same promoted OGG file as stereo `pcm_s16le` at `44.1 kHz`.

## Caveats

Wikimedia began rate-limiting additional binary downloads during the source pass, so this package keeps full slot coverage by reusing two source families in different excerpts and edits:

- `Rush Peace dance concert 1 libtheora` supports slots `68`, `75`, and `79`.
- `Traditional Sounds - Igbo Language - Nsukka - Enugu State - Nigeria` supports slots `70` and `80`.

This is an accepted source-diversity compromise for the immediate correction away from the rejected European direction, not a placeholder asset. A later polish pass can replace one or two reused cues if additional African archival recordings are sourced cleanly.

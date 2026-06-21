# Event 012 Africa Audio Direction Refresh Handoff

Date: `2026-06-21`

## Scope completed

- Researched the current Event `012` Africa super-event audio package and confirmed the live set was still built around European anthem/classical/military material.
- Replaced that direction with a new candidate package built from African-source live-performance recordings from Nigeria, Ghana, and South Africa.
- Preserved downloaded source files.
- Exported replacement `.ogg` finals at `44.1 kHz`.
- Documented source pages, licenses, edits, hashes, and fit notes in `manifest.md`.

## Files changed

- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/manifest.md`
- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/handoff.md`
- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/source/`
- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/final/`

## Parent wiring targets

Use these existing sound ids / music filenames if you want to swap the live package without changing scripted slot logic:

- Slot `68`: `super_event_africa_unification.ogg`
- Slot `69`: `super_event_africa_scramble.ogg`
- Slot `70`: `super_event_africa_old_seats.ogg`
- Slot `71`: `super_event_africa_counterfeit_crowns.ogg`
- Slot `72`: `super_event_africa_world_is_one.ogg`
- Slot `73`: `super_event_africa_continent_sponsor.ogg`
- Slot `74`: `super_event_africa_rsa_allies_peace.ogg`
- Slot `75`: `super_event_africa_dynamic_cross_continent_union.ogg`
- Slot `76`: `super_event_africa_forest_parliament.ogg`
- Slot `77`: `super_event_africa_world_root.ogg`
- Slot `78`: `super_event_africa_root_and_fang.ogg`
- Slot `79`: `super_event_africa_archive_world.ogg`
- Slot `80`: `super_event_africa_world_is_one_root_terminal.ogg`

Suggested parent action if adopted:

1. Review the new finals in `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/final/`.
2. If accepted, replace the matching live `music/super_event_africa_*.ogg` files from these finals.
3. Rebuild or replace the matching `sound/chaosx_super_event_africa_*.wav` wrappers as needed on the parent side.
4. Update whichever Africa audio research note the parent treats as source-of-truth so the dated package becomes the new canonical reference.

## Real blockers and caveats

- Wikimedia file delivery began returning `HTTP 429` during this pass for additional candidate downloads.
- Because of that rate limit, one desired archival source (`Chirillo...`) could not be recovered as audio, only as page metadata.
- To keep a full slot package ready, the final set reuses two source families:
  - `Rush Peace dance concert 1` for slots `68`, `75`, and `79`
  - `Traditional Sounds - Igbo...` for slots `70` and `80`
- This is not a placeholder fallback, but it is a diversity compromise that the parent should know about before promoting the package live.

## Recommendation

- The strongest immediate upgrades are slots `68`, `69`, `70`, `71`, `73`, `76`, and `77`; those are the clearest style correction away from the rejected European feel.
- If the parent wants a later polish pass, the first follow-up target should be downloading one or two extra archival/lament/choral African recordings so slots `72`, `79`, and `80` can become more distinct without reuse.

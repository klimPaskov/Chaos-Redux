# Event 012 Africa Audio Package Handoff

Date: `2026-06-16`
Scope: second-pass audio packaging only

Current status note: the `africa_continent_sponsor` blocker recorded below was resolved by later package work. Use `docs/assets/012_africa/super_events/audio/manifest.md` and `2026-06-16_super_event_missing_roles_audio_handoff.md` for the current wired-role status.

## Files changed

- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/assets/012_africa/super_events/audio/source/south_african_national_anthem.oga`
- `docs/assets/012_africa/super_events/audio/source/holst_mars.ogg`
- `docs/assets/012_africa/super_events/audio/source/holst_first_suite_march.ogg`
- `docs/assets/012_africa/super_events/audio/source/beethoven_egmont_overture_op84.ogg`
- `docs/assets/012_africa/super_events/audio/source/chopin_funeral_march_op72_no2.ogg`
- `docs/assets/012_africa/super_events/audio/source/beethoven_symphony_7_allegretto_john_michel.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_scramble.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_old_seats.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_counterfeit_crowns.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one.ogg`
- `docs/super_events/012_africa_super_event_research.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_audio_package_handoff.md`

## Selected roles

- `africa_is_one_unification`
  - final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
  - source: `South African national anthem`
- `africa_scramble_reaction`
  - final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_scramble.ogg`
  - source: `Mars, the Bringer of War`
- `africa_old_seats_reveal`
  - final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_old_seats.ogg`
  - source: `First Suite in E-flat for Military Band, III. March`
- `africa_counterfeit_crowns`
  - final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_counterfeit_crowns.ogg`
  - source: `Egmont Overture, Op. 84`
- `africa_world_is_one_terminal`
  - final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one.ogg`
  - source: `Funeral March in C minor, Op. posth. 72 no. 2`

## Blocked roles

- `africa_continent_sponsor`
  - status: blocked
  - blocker: no separate unique final packaged with the same confidence level after `Egmont Overture` was assigned to `africa_counterfeit_crowns`
  - preserved but not finalized: `docs/assets/012_africa/super_events/audio/source/beethoven_symphony_7_allegretto_john_michel.ogg`
  - reason not finalized: legally usable, but too sparse and stop-start for a clean sponsor super-event package without heavier editorial intervention

## Validation

- Preserved all downloaded originals under `docs/assets/012_africa/super_events/audio/source/`
- Exported all finals under `docs/assets/012_africa/super_events/audio/final/`
- Verified final sample rates with `ffprobe`

```bash
for f in docs/assets/012_africa/super_events/audio/final/*.ogg; do ffprobe -v error -show_entries format=duration:stream=sample_rate -of default=noprint_wrappers=1 "$f"; done
```

- `ffprobe` results:
  - `super_event_africa_unification.ogg`: `44100 Hz`, `120.000000s`
  - `super_event_africa_scramble.ogg`: `44100 Hz`, `118.000000s`
  - `super_event_africa_old_seats.ogg`: `44100 Hz`, `112.000000s`
  - `super_event_africa_counterfeit_crowns.ogg`: `44100 Hz`, `118.000000s`
  - `super_event_africa_world_is_one.ogg`: `44100 Hz`, `120.000000s`

## Final filenames

- `super_event_africa_unification.ogg`
- `super_event_africa_scramble.ogg`
- `super_event_africa_old_seats.ogg`
- `super_event_africa_counterfeit_crowns.ogg`
- `super_event_africa_world_is_one.ogg`

## Notes for parent wiring

- Suggested sound definition ids are recorded in `docs/assets/012_africa/super_events/audio/manifest.md`
- Do not reuse `super_event_africa_counterfeit_crowns.ogg` for `africa_continent_sponsor` unless you explicitly approve reuse
- The research note now contains only factual audio package outcomes and remaining audio blockers; detailed license and hash data live in the manifest

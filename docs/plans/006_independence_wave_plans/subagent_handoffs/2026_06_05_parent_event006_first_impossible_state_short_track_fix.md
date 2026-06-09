# Event006 First Impossible State Short Track Fix

## Scope

Follow-up for the repeated in-game audio error:

`[22:24:34][no_game_date][pdx_audio.cpp:337]: Missing sound: chaosx_super_event_independence_wave_first_impossible_state_track`

## Fix

- Changed the underlying Event 006 slot `57` audio payload in `sound/chaosx_sound.asset` to the shorter base sound token `chaosx_super_event_57_track`.
- Updated all six dynamic slot `57` soundeffect wrappers:
  - `chaosx_super_event_57_sound_0_5`
  - `chaosx_super_event_57_sound_1_0`
  - `chaosx_super_event_57_sound_1_5`
  - `chaosx_super_event_57_sound_2_0`
  - `chaosx_super_event_57_sound_2_5`
  - `chaosx_super_event_57_sound_3_0`
- Those wrappers now call `chaosx_super_event_57_track` directly, so dynamic playback no longer requests the failing long key.
- Kept `chaosx_super_event_independence_wave_first_impossible_state_track` only as a compatibility `soundeffect` wrapper that points to the shorter base sound.
- Updated Event 006 docs and the shared super-event audio package record to document the internal token and compatibility wrapper.

## Files Changed

- `sound/chaosx_sound.asset`
- `docs/events/006_independence_wave.md`
- `docs/super_events/super_event_audio_packages.md`

## Validation

- Confirmed no active `sounds = { sound = ... }` or `scoped_sound_effect` call in `sound/`, `common/`, `events/`, `interface/`, or `localisation/` still points at `chaosx_super_event_independence_wave_first_impossible_state_track`.
- Confirmed slot `57` wrappers point at `chaosx_super_event_57_track`.
- `sound/chaosx_sound.asset` brace balance: `0`, minimum nesting: `0`.

## Remaining Risk

This cannot prove live runtime behavior without the user reloading and firing the super-event again, but it removes the direct script path that produced the repeated missing-sound lookups.

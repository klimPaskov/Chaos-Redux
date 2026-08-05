# Event 006 super-event ordinary-number normalization v113

Date: 2026-08-05

Scope: normalize the Event 006 super-event identifiers to the ordinary
project-wide numbering sequence. This handoff changes identifiers and linked
documentation only; it does not clear the blocked league-recording rights or
invent a firing package.

## Canonical mapping

| Package | Display slot | Audio ID | Event Log payload | Status |
| --- | ---: | ---: | ---: | --- |
| The League of New States | 23 | 23 | 23 | image and localisation dispatch registered; audio, firing, and rights blocked |
| Every Border a Casus Belli | 24 | 24 | 24 | runtime audio and danger-milestone dispatch wired; reachability remains partial |

The former four-digit identifiers are superseded aliases in dated research
evidence. They are not used by current runtime source, sound wrappers, audio
catalogue rows, constants, or active Event 006 documentation.

## Runtime changes

- `common/script_constants/006_independence_wave_super_event_constants.txt`
  now declares both ordinary-number packages and uses `24` for the dangerous
  milestone audio and history payload.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
  dispatches slot 23 to the league image and all slot-23 text getters, while
  preserving the existing slot-24 dispatch.
- `localisation/english/006_independence_wave_super_event_l_english.yml`
  contains the approved league title, description, button, and Wilson quote
  under `chaosx_super_event.23.*`.
- `sound/chaosx_sound.asset` registers the slot-24 cue as
  `chaosx_super_event_24_track` with the six settings-aware
  `chaosx_super_event_24_sound_*` wrappers.
- The runtime WAV is now
  `sound/006_independence_wave/super_event_24_every_border_a_casus_belli.wav`.
- `music/chaosx_music_track_list.html` and the production manifest use audio
  ID 24 and the renamed WAV path.

## Blockers retained

The accepted London Brass Players recording for The League of New States still
lacks a verified United States redistribution right. No replacement was
selected, converted, or wired. Slot 23 therefore remains a reserved, dormant
presentation package even though its image and text dispatch are registered.
The danger package remains source-wired but still lacks live reachability and
playback evidence for every accepted predicate.

## Validation

- Checked that current Event 006 source surfaces contain no active use of the
  superseded four-digit identifiers.
- Confirmed the renamed WAV exists and retains the recorded SHA-256 and
  duration.
- Confirmed the six slot-24 wrappers all point to the ordinary-number base
  sound.
- No old pasted runtime log was used; no HOI4 process was launched.

This is a bounded identifier/documentation tranche. It does not claim whole
Event 006 completion.

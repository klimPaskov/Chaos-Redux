# Event 012 Africa super-event audio roles 1 and 4 production handoff

Prepared: 2026-08-03

Status: complete for the selected, rights-cleared CC0 masters. This handoff supersedes the earlier original-commission-only disposition for roles 1 and 4. The two cues are distinct public-domain recordings selected for their documented licences, preserved lossless source files, exact edit durations, and stable Event 012 identifiers; they are not silent, generated, transform-only, or generic placeholder audio.

## Source and rights record

| Role | Work | Creator | Source pages | Licence | Preserved source | Source SHA-256 | Source duration |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Africa is one / slot `101` / audio `58` | *West in Africa* | John Bartmann | [Free Music Archive](https://freemusicarchive.org/music/John_Bartmann/Public_Domain_Soundtrack_Music_Album_One/west-in-africa/); [Wikimedia Commons mirror](https://commons.wikimedia.org/wiki/File:John_Bartmann_-_15_-_West_in_Africa.ogg) | CC0 1.0 | `docs/super_events/source_audio/012_africa/role_01_west_in_africa_john_bartmann_source.ogg` | `B557044F2A318081D6DDBA710A2F7F29460D57454BB16D09F7B21770CDC7AA4A` | `174.168980 s` |
| The World / slot `104` / audio `61` | *African Moon* | John Bartmann | [Free Music Archive](https://freemusicarchive.org/music/John_Bartmann/Public_Domain_Soundtrack_Music_Album_One/african-moon/); [Wikimedia Commons mirror](https://commons.wikimedia.org/wiki/File:John_Bartmann_-_07_-_African_Moon.ogg) | CC0 1.0 | `docs/super_events/source_audio/012_africa/role_04_african_moon_john_bartmann_source.ogg` | `A93E1EF4BBAE1C4A5D8EF02ABB01A13C493983E4E18F9A784151450541FFF989` | `144.504966 s` |

Both source files are the original downloaded OGG records from the cited public pages. Their source streams are stereo Vorbis at 44,100 Hz. CC0 permits copying, editing, conversion, redistribution, and synchronization; the catalogue retains creator attribution and the edit notice as courtesy provenance.

## Runtime derivatives

| Role | Runtime WAV | Runtime SHA-256 | Duration | Format | Raw sound | Wrappers |
| --- | --- | --- | ---: | --- | --- | --- |
| Africa is one | `sound/012_africa/super_event_58_africa_is_one.wav` | `275D396227B29AE090742403A46261E5776784C155866B442C34A860B9A86D58` | `110.000 s` | stereo PCM16, 44,100 Hz | `chaosx_super_event_africa_is_one_track` | `chaosx_super_event_58_sound_0_5` through `_sound_3_0` |
| The World | `sound/012_africa/super_event_61_the_world.wav` | `425B1B149E4E1751889D41ADA15D1FD72FC9D782AC92013CF375ABC2B71E4EF8` | `116.000 s` | stereo PCM16, 44,100 Hz | `chaosx_super_event_the_world_track` | `chaosx_super_event_61_sound_0_5` through `_sound_3_0` |

The derivatives are fixed-duration excerpts from the preserved source masters. No looping is used. The full four-role runtime set is `101/58`, `102/59`, `103/60`, and `104/61`; the two existing 115-second role 2 and role 3 masters remain separately documented in the production handoff.

## Runtime wiring

- `sound/chaosx_sound.asset` defines the two raw sound names and all six settings-volume wrappers for each audio ID.
- `common/script_constants/012_africa_world_order_constants.txt` owns the slot/audio mapping.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` maps slots `101`-`104` to the four images, titles, quotes, remarks, and descriptions.
- `common/scripted_effects/012_africa_world_order_effects.txt` emits each role once through one shared presenter, uses the vanilla meta-effect flag-value pattern, and calls `play_current_super_event_audio` for human players.
- `music/chaosx_music_track_list.html` records the source URLs, CC0 status, duration, and edit notice for both cues.

## Validation evidence

`ffprobe` reports stereo, 44,100 Hz PCM16 WAV streams with exact durations of `110.000 s` and `116.000 s`. The source and derivative hashes above are the frozen provenance records used by the Event 012 presentation package. Slots and audio IDs are unique in the current registration, and no extra role, fallback cue, or duplicate store is introduced.

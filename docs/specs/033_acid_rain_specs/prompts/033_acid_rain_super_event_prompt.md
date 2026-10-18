# Event 033 Acid Rain super-event record

The formation super-event is implemented as super-event `117`; Part 9 owns its trigger contract and records its title, quote, allusion, image and audio.

## Implemented package

- Image: `gfx/super_events/033_acid_rain/033_acid_rain.dds`, 457 by 328, sprite `GFX_super_event_033_acid_rain`.
- Text: `chaosx_super_event.117.t`, `.q`, `.a` and `.d` in `localisation/english/033_acid_rain_l_english.yml`.
- Audio: `sound/033_acid_rain/super_event_033_acid_rain_formation.wav` and `.ogg`, playback ID 117, with its rights and audition record in `music/chaosx_music_track_list.html`.

## Rules for any change

- The super-event fires once, after the formation transaction commits, for every player, and never from a failed or rolled-back initialization or a save reconciliation.
- Opening or closing it never advances the weather, alters exposure, adds Chaos or adds contamination.
- A replacement quote, allusion or recording goes through `chaosx_super_event_text_researcher` or `chaosx_super_event_audio_researcher` under [the super-event skill](../../../../.claude/skills/chaos-redux-super-events/SKILL.md), with source, rights, uniqueness and audition records.
- Hearing the audio and seeing the window in game are user live checks.

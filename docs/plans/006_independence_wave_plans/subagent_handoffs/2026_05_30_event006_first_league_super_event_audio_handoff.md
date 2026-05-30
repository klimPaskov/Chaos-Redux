# Event 006 First League Super-Event Audio Handoff

## Scope

- Event: `006`
- Super-event key: `independence_wave_first_league`
- Role: first small-state faction formation, diplomatic world-order signal
- Requested mood: restrained, tense, state ceremony; no action music

## Existing-pattern check

- Checked current package notes in `docs/super_events/super_event_audio_packages.md`.
- Checked current naming/registration patterns in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`.
- No current reference to audio id `52` was found in those files.
- Existing repo tracks do not fit Event 006 tone and should not be reused here.

## Selected track

- Track title: `Suite No. 1 in E-flat, Op. 28 No. 1: I. Chaconne`
- Composer: Gustav Holst
- Performer / recording source: `The President's Own` United States Marine Band
- Recording context: `The Bicentennial Collection`, Disc 10: Guest Conductors
- Official source page: <https://www.marineband.marines.mil/Audio-Resources/Educational-Series/The-Bicentennial-Collection/The-Bicentennial-Collection-Disc-10/>
- Official track listing evidence: the Marine Band page lists `Suite No. 1 in E-flat (1997)` and `2. Chaconne`
- Wikimedia Commons file page: <https://commons.wikimedia.org/wiki/File:Holst_First_Suite_Chaconne.ogg>
- Downloaded source URL: <https://commons.wikimedia.org/wiki/Special:Redirect/file/Holst_First_Suite_Chaconne.ogg>

## License and usage terms

- Composition rights: public domain in the United States and in life-plus-70 jurisdictions because Holst died in `1934`; the Commons file page marks the composition public domain in countries with terms of life plus `70` years or fewer.
- Recording rights: public domain as a U.S. federal government work performed and published by the United States Marine Band; Commons marks the recording as a U.S. federal government work.
- License confidence: `medium-high`
- Usage terms: usable for mod distribution where U.S. public-domain federal-work treatment and public-domain composition status are accepted.
- Attribution required: not legally required for the public-domain recording, but recommended in repo docs for provenance.

## Jurisdiction caveat

- This is not a zero-risk worldwide public-domain case.
- The Commons page notes that some countries with longer terms than life plus `70` may still treat the Holst composition as protected.
- Practical reading: this is a clean U.S. use case and a clean Commons-hosted rights trail, but international redistribution into a few long-term jurisdictions may carry residual uncertainty.
- Because the task asked for honest licensing notes, this caveat should remain in parent-facing documentation if the track is wired.

## Why this fits Event 006

- The opening Chaconne is formal and deliberate rather than heroic or catastrophic.
- Low brass and broad harmonic pacing give it state-ceremony weight without sounding like open war.
- The progression feels like delegates assembling into a recognized bloc, which matches the `first league` reveal better than collapse, victory, or horror music.
- It avoids the Event 005 Soviet-collapse tone and avoids action scoring.

## Rejected candidate

- `Kevin MacLeod - Funeral March for Brass`
- Rejected because the Commons page explicitly says the external license had not yet been reviewed by a reviewer/admin, so the rights trail is not clean enough for this task.
- URL checked: <https://commons.wikimedia.org/wiki/File:Kevin_MacLeod_-_Funeral_March_for_Brass.ogg>

## Source and derivatives

- Original downloaded source path: `docs/plans/006_independence_wave_plans/source_audio/2026_05_30_holst_first_suite_chaconne_us_marine_band_source.ogg`
- Final music path: `music/super_event_independence_wave_first_league.ogg`
- Final sound-channel path: `sound/chaosx_super_event_independence_wave_first_league.wav`

## Duration

- Full downloaded source: `4:50.090`
- Final in-game excerpt: `1:57.987`
- Selected excerpt window: opening excerpt, `0:00` to `1:58`

## Editing and conversion steps

1. Downloaded the original OGG from the Commons original-file redirect for the Marine Band recording.
2. Preserved the full source file unchanged under `docs/plans/006_independence_wave_plans/source_audio/`.
3. Exported the game music derivative as an OGG excerpt using:
   - trim to `118` seconds
   - `0.15` second fade in
   - `3` second fade out starting at `115` seconds
4. Exported the sound-channel derivative as PCM WAV with the same excerpt and fade treatment.
5. Regenerated the OGG with `atrim` and `asetpts` after the initial OGG trim emitted timestamp warnings, so the final OGG is a clean re-encode.

## Final file metadata

- Source codec: `vorbis`, `44100 Hz`, stereo
- Final OGG codec: `vorbis`, `44100 Hz`, stereo
- Final WAV codec: `pcm_s16le`, `44100 Hz`, stereo

## Checksums

- Source OGG SHA-256: `71f61df2bb10ab335dc3c96caa6eb8d7df098950616f524c547e2f18bb9df4f3`
- Final music OGG SHA-256: `4458c90624669cd8a71d4f618eec66af404823f3a89b920d47a0b3b4d5cbfa79`
- Final sound WAV SHA-256: `8279eed988f1181380d5a860e0a9494ccad025170afc054f838e45ea70617aea`

## Parent wiring suggestions

- Proposed audio id: `52`
- Suggested music file: `music/super_event_independence_wave_first_league.ogg`
- Suggested sound-channel file: `sound/chaosx_super_event_independence_wave_first_league.wav`
- Suggested named sound definition: `chaosx_super_event_independence_wave_first_league_track`
- If the parent keeps the current id-based helper pattern, use `52`-based helper entries consistently for music and sound variants.

## Suggested attribution text

- `Gustav Holst, Suite No. 1 in E-flat, I. Chaconne. Performed by The President's Own United States Marine Band. Source: Wikimedia Commons / U.S. Marine Band Bicentennial Collection.`

## Remaining uncertainty

- The only substantive uncertainty is the composition-term caveat outside life-plus-70 jurisdictions.
- If the parent wants a track with cleaner worldwide composition status than Holst `1934`, a second research pass should target a pre-`1926` composer death with equally suitable ceremony tone.

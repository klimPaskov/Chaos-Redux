# Event 006 Independence Wave Super-Event Audio Handoff

## Package summary

- Event: `006 Independence Wave`
- Super-event use: `First Old Name / historical-return reveal`
- Recommended track: `God of Our Fathers`
- Suggested sound definition id: `chaosx_super_event_independence_wave_first_old_name`
- Suggested music id: `super_event_independence_wave_first_old_name`

## Selected track

- Title: `God of Our Fathers`
- Composer: `George William Warren` (composition date listed as 1876)
- Performer / recording source: `United States Air Force Heritage of America Band, Concert Band`
- Performance date: `2005`
- Source page: `https://commons.wikimedia.org/wiki/File:God_of_Our_Fathers_-_Concert_Band_-_United_States_Air_Force_Heritage_of_America_Band.mp3`
- Direct preserved download came from: `https://commons.wikimedia.org/wiki/Special:Redirect/file/God_of_Our_Fathers_-_Concert_Band_-_United_States_Air_Force_Heritage_of_America_Band.mp3`
- Official upstream source cited by the file page: `https://www.music.af.mil/Multimedia/Music/Public-Domain-Music/`

## License and usage

- Composition rights: public domain. The Wikimedia file page identifies the composition as public domain and notes the composer died in 1902.
- Recording / performance rights: public domain as a U.S. federal government work by the United States Air Force, per the Wikimedia file page and its cited official Air Force source.
- Usage terms: usable for mod distribution and derivative conversion based on the public-domain status of both the composition and the federal-government recording.
- Attribution requirement: none required.
- Attribution text if desired: `God of Our Fathers, performed by the United States Air Force Heritage of America Band, Concert Band. Source: U.S. Air Force / Wikimedia Commons.`
- License confidence: `High`
- Confidence note: the Wikimedia page says some metadata was sourced from Air Force file metadata and may not be independently verified, but the rights basis itself is still clear: old public-domain composition plus U.S. federal government performance/recording.

## Duration

- Downloaded source duration: `91.44s`
- Final output duration: `91.43s`

## File outputs

- Original downloaded source path: `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_wikimedia_god_of_our_fathers_usaf_heritage_band_source.mp3`
- Final music path: `music/super_event_independence_wave_first_old_name.ogg`
- Final sound path: `sound/chaosx_super_event_independence_wave_first_old_name.wav`

## Editing and conversion steps

- Preserved the original downloaded MP3 without modification.
- Created the final deliverables from the preserved source with a very light mastering pass only.
- `volume=-3dB`
- `afade=t=in:st=0:d=0.12`
- `afade=t=out:st=90.8:d=0.2`
- Output formats:
- `.ogg`: Vorbis, stereo, 44.1 kHz
- `.wav`: PCM s16le, stereo, 44.1 kHz

## Why this fits

- The track is ceremonial and restrained rather than martial or triumphant.
- Its hymn cadence gives the reveal historical gravity without pushing into horror or overt victory music.
- The arrangement feels archival and official, which suits a restoration / old-name return moment.
- At 1:31 it is short enough for a super-event and does not need a hard cut or loop.

## Suggested use note for parent

- Use the full rendered cue once, no loop required.
- If the parent wants a slightly drier presentation in-game, it is safe to lower playback volume further in definitions rather than re-edit the file.

## Validation

- Confirmed source file download and preservation.
- Confirmed final `.ogg` is audio-only Vorbis.
- Confirmed final `.wav` exists and matches the intended duration.

## Scope notes

- I did not edit gameplay script, localisation, GFX, sound definitions, music definitions, spreadsheets, or visual assets.
- I did not update `docs/super_events/super_event_audio_packages.md`; leaving wiring and package-table docs to the parent matches this subtask boundary.

## Uncertainty / blocker

- No blocker.
- Minor note only: the source MP3 contains a small malformed frame warning at decode end, but both rendered outputs completed successfully and probe cleanly.

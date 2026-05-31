# Event 006 Human Renunciation Super-Event Audio Handoff

## Scope

- Event: `006`
- Super-event key: `independence_wave_human_renunciation`
- Role: anti-mankind doctrine public reveal
- Requested mood: bureaucratic dread, sparse low music, restrained ceremonial inhumanity

## Existing-pattern check

- Checked current package notes in `docs/super_events/super_event_audio_packages.md`.
- Checked current naming and file patterns in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`.
- Existing Event 006 audio package currently covers only `independence_wave_first_league`.
- No current reference to audio id `53` was found in the checked package docs or asset manifests, so `53` is a safe parent-facing suggestion only.

## Selected track

- Track title: `Prelude in C minor, Op. 28 No. 20` (`Funeral March`)
- Composer: Frédéric Chopin
- Performer / recording source: Ivan Ilic via Musopen
- Wikimedia Commons file page: <https://commons.wikimedia.org/wiki/File:Chopin_-_Preludes,_Op._28_-_No._20_%27Funeral_march%27.ogg>
- Original-file redirect used for download: <https://commons.wikimedia.org/wiki/Special:Redirect/file/Chopin_-_Preludes,_Op._28_-_No._20_%27Funeral_march%27.ogg>
- Upstream source page cited by Commons: <https://musopen.org/music/1556-preludes-op-28/>

## License and usage terms

- Composition rights: public domain. Chopin died in `1849`, so the composition is safely public domain.
- Recording rights: clearly licensed under `CC BY 3.0` on the Wikimedia Commons file page.
- License URL: <https://creativecommons.org/licenses/by/3.0/>
- Attribution required: yes.
- License confidence: `high`
- Usage terms: mod redistribution is allowed, including adapted excerpts, if attribution is retained and the derivative edit is disclosed in documentation.

## Why this fits Event 006

- The cue is built from slow, repeated low-register chords rather than melodic uplift or military triumph.
- It sounds procedural and inevitable, which suits a public reveal of doctrine, census, seals, registries, and administrative horror better than battle music or overt horror scoring.
- The pacing feels like a formal declaration that something human has been crossed out in law.
- It stays cold and sparse enough to avoid overlapping with Event 005 collapse tone or with the more diplomatic `first_league` package.

## Source and derivatives

- Original downloaded source path: `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg`
- Final music path: `music/super_event_independence_wave_human_renunciation.ogg`
- Final sound-channel path: `sound/chaosx_super_event_independence_wave_human_renunciation.wav`

## Duration

- Full downloaded source: `1:30.558`
- Head silence removed: `1.133` seconds
- Tail silence removed: `6.366` seconds
- Final in-game excerpt: `1:23.035`
- Selected excerpt window: `0:01.157` to `1:24.192` from source

## Editing and conversion steps

1. Downloaded the original OGG from the Commons original-file redirect.
2. Preserved the source file unchanged under `docs/plans/006_independence_wave_plans/source_audio/`.
3. Detected dead air with `ffmpeg` `silencedetect`.
4. Exported the game music derivative as OGG by trimming only leading and trailing silence, then applying a `0.12` second fade in and a `3.12` second fade out.
5. Exported the sound-channel derivative as PCM WAV with the same trim and fade treatment.

## Validation commands

```bash
curl -L 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Chopin_-_Preludes,_Op._28_-_No._20_%27Funeral_march%27.ogg' -o docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg
ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg' -af silencedetect=noise=-45dB:d=0.25 -f null -
ffmpeg -y -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg' -vn -af "atrim=start=1.15664:end=84.1917,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.12,afade=t=out:st=79.915:d=3.12" -c:a libvorbis -q:a 5 'music/super_event_independence_wave_human_renunciation.ogg'
ffmpeg -y -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg' -vn -af "atrim=start=1.15664:end=84.1917,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.12,afade=t=out:st=79.915:d=3.12" -c:a pcm_s16le 'sound/chaosx_super_event_independence_wave_human_renunciation.wav'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'music/super_event_independence_wave_human_renunciation.ogg'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'sound/chaosx_super_event_independence_wave_human_renunciation.wav'
sha256sum 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_chopin_prelude_20_funeral_march_musopen_source.ogg' 'music/super_event_independence_wave_human_renunciation.ogg' 'sound/chaosx_super_event_independence_wave_human_renunciation.wav'
```

## Final file metadata

- Source codec: `vorbis`, `44100 Hz`, stereo
- Final OGG codec: `vorbis`, `44100 Hz`, stereo
- Final WAV codec: `pcm_s16le`, `44100 Hz`, stereo

## Checksums

- Source OGG SHA-256: `88def081ce1e14ac62bf27675e8885bbceb8b36ffc6cf1f4c5ab1b69f7dd5147`
- Final music OGG SHA-256: `5e3fcf6beea4bc841c9e2f4c9f47548f02a4205474d2488dd5368003935977b6`
- Final sound WAV SHA-256: `e6e6977afa785561d70f599b35fa468182618b9b2479f6f97fefc0caf0467629`

## Parent wiring suggestions

- Proposed audio id: `53`
- Suggested music file: `music/super_event_independence_wave_human_renunciation.ogg`
- Suggested sound-channel file: `sound/chaosx_super_event_independence_wave_human_renunciation.wav`
- Suggested named sound definition: `chaosx_super_event_independence_wave_human_renunciation_track`
- If the parent keeps the current id helper pattern, reserve `53` consistently for both the music and sound-channel helpers.

## Suggested attribution text

- `Frédéric Chopin, Prelude in C minor, Op. 28 No. 20 ("Funeral March"), performed by Ivan Ilic. Source: Musopen via Wikimedia Commons. Licensed CC BY 3.0. Edited for duration and fades.`

## Remaining uncertainty

- No major license blocker remains.
- The only compliance requirement is preserving attribution and noting that the in-game file is an edited excerpt of the Commons-hosted recording.

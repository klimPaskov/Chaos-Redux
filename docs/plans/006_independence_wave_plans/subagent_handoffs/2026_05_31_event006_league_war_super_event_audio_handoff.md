# Event 006 League War Super-Event Audio Handoff

## Scope

- Event: `006`
- Super-event key: `independence_wave_league_war`
- Requested slot assumption: `54`
- Role: small-state bloc enters a serious defensive or recognition war
- Requested mood: tense march or mobilization music, not triumphant

## Existing-pattern check

- Checked current package notes in `docs/super_events/super_event_audio_packages.md`.
- Checked current naming and file patterns in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`.
- Existing Event 006 audio package currently covers `independence_wave_first_league` and `independence_wave_human_renunciation`.
- Existing file pattern for Event 006 uses named files rather than slot-number filenames, so this package follows `music/super_event_independence_wave_league_war.ogg` and `sound/chaosx_super_event_independence_wave_league_war.wav`.
- No existing `league_war` audio files were found in the checked package paths.

## Selected track

- Track title: `Marche Indienne`
- Composer: Adolphe Sellenick
- Performer / recording source: `The President's Own` United States Marine Band
- Official source page: <https://www.marineband.marines.mil/Audio-Resources/Educational-Series/Sound-Off/>
- Official track-list evidence: the `Sound Off!` page lists `Marche Indienne` by `Adolph Sellenick` with a direct download entry and no arranger credit.
- Wikimedia Commons file page: <https://commons.wikimedia.org/wiki/File:Marche_Indienne_-_U.S._Marine_Band.ogg>
- Original-file redirect used for download: <https://commons.wikimedia.org/wiki/Special:Redirect/file/Marche_Indienne_-_U.S._Marine_Band.ogg>

## License and usage terms

- Composition rights: public domain. Sellenick died in `1893`, so the composition clears life-plus-100 jurisdictions.
- Recording rights: public domain as a U.S. federal government work performed and published by the United States Marine Band.
- License confidence: `high`
- Usage terms: usable for mod redistribution and edited excerpt use. Attribution is not legally required for the public-domain recording, but should be retained in repo notes for provenance.

## Why this fits Event 006

- The cue is a formal march with pressure and forward motion rather than victory-parade uplift.
- Its opening section feels like mobilization orders, rail movement, and nervous coalition resolve, which matches the League hardening from congress into armed compact.
- It stays martial without sounding like a major-power imperial anthem or a triumphal end-state cue.
- The slightly severe band texture fits a small-state defensive coalition better than lush orchestral war music.

## Rejected candidate

- `Marche Hongroise` from Berlioz was researched first and temporarily downloaded from the U.S. Marine Band / Wikimedia Commons chain.
- Rejected because the official Marine Band source credits a modern transcription by Howard Bowlin, which leaves arrangement rights unclear for this task even though the recording itself is a federal work.
- Because the task required clear, usable rights, the Berlioz option should not be wired.

## Source and derivatives

- Original downloaded source path: `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg`
- Final music path: `music/super_event_independence_wave_league_war.ogg`
- Final sound-channel path: `sound/chaosx_super_event_independence_wave_league_war.wav`

## Duration

- Full downloaded source: `4:11.664`
- Head silence removed: `0.909` seconds
- Tail silence left unused by excerpt selection.
- Final in-game excerpt: `1:53.091`
- Selected excerpt window: `0:00.909` to `1:54.000` from source

## Editing and conversion steps

1. Downloaded the original OGG from the Commons original-file redirect for the Marine Band recording.
2. Preserved the source file unchanged under `docs/plans/006_independence_wave_plans/source_audio/`.
3. Detected bookend silence with `ffmpeg` `silencedetect`.
4. Exported the sound-channel derivative as PCM WAV from the opening march section after the lead-in silence, with a `0.12` second fade in and a `3.0` second fade out.
5. Regenerated the game music OGG from the finished WAV derivative to avoid OGG timestamp issues during direct source trimming.

## Validation commands

```bash
curl -L 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Marche_Indienne_-_U.S._Marine_Band.ogg' -o docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg
ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg' -af silencedetect=noise=-45dB:d=0.25 -f null -
ffmpeg -y -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg' -vn -af "atrim=start=0.909138:end=114,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.12,afade=t=out:st=110.090862:d=3.0" -c:a pcm_s16le 'sound/chaosx_super_event_independence_wave_league_war.wav'
ffmpeg -y -i 'sound/chaosx_super_event_independence_wave_league_war.wav' -c:a libvorbis -q:a 5 'music/super_event_independence_wave_league_war.ogg'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'music/super_event_independence_wave_league_war.ogg'
ffprobe -v error -show_entries format=duration:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 'sound/chaosx_super_event_independence_wave_league_war.wav'
sha256sum 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_sellenick_marche_indienne_us_marine_band_source.ogg' 'music/super_event_independence_wave_league_war.ogg' 'sound/chaosx_super_event_independence_wave_league_war.wav'
```

## Final file metadata

- Source codec: `vorbis`, `44100 Hz`, stereo
- Final OGG codec: `vorbis`, `44100 Hz`, stereo
- Final WAV codec: `pcm_s16le`, `44100 Hz`, stereo

## Checksums

- Source OGG SHA-256: `80218552bbf8503707c33dc8858efa976e195832bb5c7513a30b88f0d762a53e`
- Final music OGG SHA-256: `c973fbe7dc3977e7e41c7b05b997d0c93f2c1fe813b92a390e76c0f147a7a3cb`
- Final sound WAV SHA-256: `760de943a07eee3c77a2bfdfcfaaae6a4b0ea48a77ab72bc864a3948fd47c59b`

## Parent wiring suggestions

- Proposed audio id: `54`
- Suggested music file: `music/super_event_independence_wave_league_war.ogg`
- Suggested sound-channel file: `sound/chaosx_super_event_independence_wave_league_war.wav`
- Suggested named sound definition: `chaosx_super_event_independence_wave_league_war_track`
- If the parent keeps slot-based helper ids, reserve `chaosx_super_event_music_54` and `chaosx_super_event_sfx_54` consistently around the named files above.

## Suggested attribution text

- `Adolphe Sellenick, Marche Indienne. Performed by The President's Own United States Marine Band. Source: Wikimedia Commons / U.S. Marine Band Sound Off!. Edited for duration and fades.`

## Remaining uncertainty

- No material license blocker remains on the selected track.
- The main caution from this research pass is negative: do not reuse the rejected Berlioz `Marche Hongroise` candidate unless arrangement rights are separately cleared.

# Event 006 Independence Wave Super-Event Audio Handoff

## Scope

Audio-only subtask for Event 006 `Independence Wave`, super-event slot `58`, working title `The Rump That Endures`.

No gameplay script, localisation, GFX, sound definitions, music definitions, spreadsheets, or visual assets were edited.

## Package Summary

- Event: `006 Independence Wave`
- Super-event use: `host survival / one-state rump endurance`
- Recommended track: `Prelude in E Minor, Op. 28 No. 4`
- Suggested sound definition id: `chaosx_super_event_independence_wave_rump_that_endures`
- Suggested music id: `super_event_independence_wave_rump_that_endures`

## Selected Track

- Title: `Prelude in E Minor, Op. 28 No. 4`
- Composer: `Frédéric Chopin` (`1810-1849`)
- Performer / recording source: `Porticodoro / SmartCGArt Media Productions`
- Source page: `https://commons.wikimedia.org/wiki/File:FChopinPreludeOp28n4.OGG`
- Direct preserved download used: `https://commons.wikimedia.org/wiki/Special:Redirect/file/FChopinPreludeOp28n4.OGG`
- Source page summary: the Commons page identifies the file as a complete performance of Chopin's prelude and lists `Porticodoro / SmartCGArt Media Productions` as the source and author.

## License and Usage

- Composition rights: public domain. Chopin died in `1849`, so the composition is safely public domain.
- Recording rights: clear and compatible. The Wikimedia Commons file page licenses the recording under `CC BY 3.0 Unported`.
- Usage terms: usable for mod distribution and derivative conversion with attribution because the file page explicitly permits sharing and adaptation under `CC BY 3.0`.
- Attribution requirement: `Yes`
- Attribution text: `Frédéric Chopin, Prelude in E Minor, Op. 28 No. 4. Recording by Porticodoro / SmartCGArt Media Productions via Wikimedia Commons, licensed CC BY 3.0. Edited for duration and fades.`
- License URL: `https://creativecommons.org/licenses/by/3.0/`
- License confidence: `High`
- Confidence note: the rights chain is simple and explicit on the source page: public-domain composition plus a directly licensed recording on Commons.

## Rights Assessment

- Composition and recording rights are both documented well enough for repository use.
- I rejected candidates that were more tonally similar but carried `CC BY-SA` obligations or weaker provenance.
- I also rejected more ceremonial U.S. military-band material because it read as official endurance or reverence rather than humiliation and diminished survival.

## Why This Fits

This cue is quiet, formal, and defeated without sounding annihilated. The repeated descending phrases feel like a government still speaking in proper forms after losing almost everything that made those forms credible.

That gives `The Rump That Endures` the right tone: not battlefield collapse, not noble last stand, and not horror. It sounds like a capital still issuing orders from a nearly empty state.

## Edit Choice

- Chosen excerpt: nearly full cue, minus front and tail silence
- Source duration: `126.000000s` (`2:06.000`)
- Final `.ogg` duration: `123.860000s` (`2:03.860`)
- Final `.wav` duration: `123.860000s` (`2:03.860`)
- Edit reason: remove dead air before the opening phrase and after the final cadence while preserving the piece's resigned pacing
- Applied processing:
  - `atrim=start=0.86:end=124.72`
  - `asetpts=PTS-STARTPTS`
  - `afade=t=in:st=0:d=0.12`
  - `afade=t=out:st=123.51:d=0.35`

## Output Files

- Original downloaded source:
  - `docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg`
- Final music file:
  - `music/super_event_independence_wave_rump_that_endures.ogg`
- Final sound wrapper file:
  - `sound/chaosx_super_event_independence_wave_rump_that_endures.wav`

## Technical Notes

- Source format:
  - `Vorbis`
  - stereo
  - `44.1 kHz`
- Final `.ogg` format:
  - `Vorbis`
  - stereo
  - `44.1 kHz`
- Final `.wav` format:
  - `PCM s16le`
  - stereo
  - `44.1 kHz`
- File sizes:
  - source `.ogg`: `1,757,568 bytes`
  - final `.ogg`: `1,952,625 bytes`
  - final `.wav`: `21,848,982 bytes`

## Conversion Steps

Source preservation:

```bash
mkdir -p docs/plans/006_independence_wave_plans/source_audio

curl -L --fail 'https://commons.wikimedia.org/wiki/Special:Redirect/file/FChopinPreludeOp28n4.OGG' \
  -o 'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg'
```

Silence check:

```bash
ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg' \
  -af silencedetect=noise=-45dB:d=0.2 -f null -
```

Final renders:

```bash
ffmpeg -y -i 'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg' \
  -vn -af "atrim=start=0.86:end=124.72,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.12,afade=t=out:st=123.51:d=0.35" \
  -c:a pcm_s16le -ar 44100 -ac 2 \
  'sound/chaosx_super_event_independence_wave_rump_that_endures.wav'

ffmpeg -y -i 'sound/chaosx_super_event_independence_wave_rump_that_endures.wav' \
  -vn -c:a libvorbis -ar 44100 -ac 2 -q:a 5 \
  'music/super_event_independence_wave_rump_that_endures.ogg'
```

Validation:

```bash
ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg'

ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'sound/chaosx_super_event_independence_wave_rump_that_endures.wav'

ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'music/super_event_independence_wave_rump_that_endures.ogg'

ffmpeg -v error -i 'music/super_event_independence_wave_rump_that_endures.ogg' -f null -

sha256sum \
  'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_chopin_prelude_op28_no4_porticodoro_source.ogg' \
  'music/super_event_independence_wave_rump_that_endures.ogg' \
  'sound/chaosx_super_event_independence_wave_rump_that_endures.wav'
```

## Checksums

- Source `.ogg`: `874b4955b05b24d084a1087c0468ba80748d8af6f77d8aa153ad6e41f26bd0fc`
- Final music `.ogg`: `2eb2f82d71255fb0e8197bd9219c1461f488eae8a4181a0c84bce7453f17e796`
- Final sound `.wav`: `e5e9bb5975be1a72bea2614d29816dfd3255526c43dddd1f3276b8b3e895af8e`

## Suggested Parent Wiring Handoff

- Suggested sound definition id: `chaosx_super_event_independence_wave_rump_that_endures`
- Suggested music key / logical label: `super_event_independence_wave_rump_that_endures`
- Suggested super-event use: slot `58`
- Suggested playback note: use once, no loop

## Validation

- Confirmed source file download and preservation.
- Confirmed final `.ogg` decodes cleanly with `ffmpeg -v error`.
- Confirmed final `.wav` exists and matches the intended duration.
- Confirmed both final outputs are stereo `44.1 kHz`.

## Uncertainty / Blocker

- No blocker.
- Mild aesthetic risk only: this cue is intentionally subdued. If the parent later wants slightly more visible institutional stiffness, the next pass should stay acoustic and piano-led or chamber-led rather than switching to martial or synthetic tension music.

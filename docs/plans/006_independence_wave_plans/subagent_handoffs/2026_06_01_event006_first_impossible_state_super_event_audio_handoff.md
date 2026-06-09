# Event 006 Independence Wave Super-Event Audio Handoff

## Scope

Audio-only subtask for Event 006 `Independence Wave`, super-event slot `57`, working title `First Impossible State`.

No gameplay script, localisation, GFX, sound definitions, music definitions, spreadsheets, or visual assets were edited.

## Package Summary

- Event: `006 Independence Wave`
- Super-event use: `first strange release / impossible statehood reveal`
- Recommended track: `Gymnopédie No. 1`
- Suggested sound definition id: `chaosx_super_event_independence_wave_first_impossible_state`
- Suggested music id: `super_event_independence_wave_first_impossible_state`

## Selected Track

- Title: `Gymnopédie No. 1` (`Gymnopédies - la 1ére. lent et douloureux`)
- Composer: `Erik Satie` (`1866-1925`)
- Performer / recording source: `Robin Alciatore`
- Source page: `https://commons.wikimedia.org/wiki/File:Erik_Satie_-_gymnopedies_-_la_1_ere._lent_et_douloureux.ogg`
- Direct preserved download used: `https://upload.wikimedia.org/wikipedia/commons/9/90/Erik_Satie_-_gymnopedies_-_la_1_ere._lent_et_douloureux.ogg`
- Upstream source stated on the file page: `http://www.musopen.com`

## License and Usage

- Composition rights: public domain. Satie died in `1925`, and the Wikimedia file page marks the composition public domain.
- Recording rights: public domain. The Wikimedia file page states the recording came from Musopen and reproduces Musopen's then-current public-domain statement; it also separately states that `Robin Alciatore` released this file into the public domain worldwide.
- Usage terms: usable for mod distribution and derivative conversion because both the composition and the recording are documented as public domain on the source page.
- Attribution requirement: `None required`
- Attribution text if desired: `Gymnopédie No. 1 by Erik Satie, performed by Robin Alciatore via Musopen / Wikimedia Commons.`
- License confidence: `High`
- Confidence note: the cleanest rights basis is the recording author's public-domain dedication on the Wikimedia file page, with the Musopen public-domain statement as supporting provenance.

## Rights Assessment

- Composition and recording rights are both clear enough for repo use.
- I rejected the more tonally exact `Gnossienne` recordings on Wikimedia because the available performances I verified were under `CC BY-SA`, not public domain or equivalently clean for this task.
- I did not use modern-electronic CC0 alternatives because they missed the brief's period-compatible tone even when the license was clean.

## Why This Fits

`Gymnopédie No. 1` is restrained, formal, and emotionally detached rather than tragic or triumphant. That gives the reveal a dossier-room quality: something impossible has been signed into existence, but the room has not yet admitted what that means.

The cue also avoids overt horror language. Its unease comes from suspension and stillness, which matches bureaucratic dread, sealed files, and the first glimpse of a high-chaos `strange` release better than a march, lament, or modern ambient pulse.

## Edit Choice

- Chosen excerpt: full track
- Source duration: `183.588571s` (`3:03.589`)
- Final `.ogg` duration: `183.588571s` (`3:03.589`)
- Final `.wav` duration: `183.588571s` (`3:03.589`)
- Edit reason: keep the full cue to preserve phrasing and avoid a mid-sentence musical cut
- Applied processing:
  - `volume=-2dB`
  - `afade=t=in:st=0:d=0.12`
  - `afade=t=out:st=183.30:d=0.28`

## Output Files

- Original downloaded source:
  - `docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_musopen_satie_gymnopedie_no1_robin_alciatore_source.ogg`
- Final music file:
  - `music/super_event_independence_wave_first_impossible_state.ogg`
- Final sound wrapper file:
  - `sound/chaosx_super_event_independence_wave_first_impossible_state.wav`

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
  - source `.ogg`: `3,696,351 bytes`
  - final `.ogg`: `3,081,836 bytes`
  - final `.wav`: `32,385,102 bytes`

## Conversion Steps

Source preservation:

```bash
mkdir -p docs/plans/006_independence_wave_plans/source_audio

curl -L --fail 'https://upload.wikimedia.org/wikipedia/commons/9/90/Erik_Satie_-_gymnopedies_-_la_1_ere._lent_et_douloureux.ogg' \
  -o 'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_musopen_satie_gymnopedie_no1_robin_alciatore_source.ogg'
```

Final renders:

```bash
ffmpeg -y -i 'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_musopen_satie_gymnopedie_no1_robin_alciatore_source.ogg' \
  -vn -af "volume=-2dB,afade=t=in:st=0:d=0.12,afade=t=out:st=183.30:d=0.28" \
  -c:a pcm_s16le -ar 44100 -ac 2 \
  'sound/chaosx_super_event_independence_wave_first_impossible_state.wav'

ffmpeg -y -i 'sound/chaosx_super_event_independence_wave_first_impossible_state.wav' \
  -vn -c:a libvorbis -ar 44100 -ac 2 -q:a 5 \
  'music/super_event_independence_wave_first_impossible_state.ogg'
```

Validation:

```bash
ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'docs/plans/006_independence_wave_plans/source_audio/2026_06_01_wikimedia_musopen_satie_gymnopedie_no1_robin_alciatore_source.ogg'

ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'music/super_event_independence_wave_first_impossible_state.ogg'

ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  'sound/chaosx_super_event_independence_wave_first_impossible_state.wav'

ffmpeg -v error -i 'music/super_event_independence_wave_first_impossible_state.ogg' -f null -
```

## Suggested Parent Wiring Handoff

- Suggested sound definition id: `chaosx_super_event_independence_wave_first_impossible_state`
- Suggested music key / logical label: `super_event_independence_wave_first_impossible_state`
- Suggested super-event use: slot `57`
- Suggested playback note: use once, no loop

## Validation

- Confirmed source file download and preservation.
- Confirmed final `.ogg` decodes cleanly with `ffmpeg -v error`.
- Confirmed final `.wav` exists and matches the intended duration.
- Confirmed both final outputs are stereo `44.1 kHz`.

## Uncertainty / Blocker

- No blocker.
- Mild aesthetic risk only: this cue is intentionally understated. If the parent later wants stronger tension, the next step should still stay acoustic / period-compatible rather than switching to synthetic suspense scoring.

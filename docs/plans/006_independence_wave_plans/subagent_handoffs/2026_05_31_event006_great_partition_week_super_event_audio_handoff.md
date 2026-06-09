# Event 006 Super-Event Audio Handoff

## Scope

Audio-only subtask for Event 006 `Independence Wave`, super-event title direction `The Great Partition Week`.

No gameplay script, localisation, GFX, sound definitions, music definitions, spreadsheets, or visual assets were edited.

## Selected Track

- Track title: `Waiting TTTT`
- Creator / composer / recording source: `Loyalty Freak Music`
- Source page: `https://freemusicarchive.org/music/Loyalty_Freak_Music/MINIMAL_AMBIENT_BOUNCE/Loyalty_Freak_Music_-_MINIMAL_AMBIENT_BOUNCE_-_05_Waiting_TTTT/`
- Direct source download used: `https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Music_for_Video/Loyalty_Freak_Music/MINIMAL_AMBIENT_BOUNCE/Loyalty_Freak_Music_-_05_-_Waiting_TTTT.mp3`
- License: `CC0 1.0 Universal`
- License terms: public-domain dedication / no attribution required
- CC0 legal text: `https://creativecommons.org/publicdomain/zero/1.0/`
- License confidence: `High`
- Attribution requirement: `None required`

## Rights Assessment

- Composition rights: covered because this is an original track published by the creator under `CC0 1.0 Universal`.
- Recording rights: covered because the selected recording is the same creator-uploaded recording distributed under `CC0 1.0 Universal`.
- Rejection basis for unclear alternatives: I rejected unclear archive/classical options where composition and recording status were not both cleanly documented.

## Why This Fits

`Waiting TTTT` fits the brief better than collapse-lament or horror material because it stays procedural and unsettled. The pulse reads as administrative emergency rather than battlefield triumph: restrained momentum, mild techno tension, and enough unease for a week-of-partitions reveal without turning theatrical or mournful.

For `The Great Partition Week`, that gives the right map-room character: states breaking loose in waves, officials reacting late, borders shifting faster than institutions can process them.

## Edit Choice

- Chosen excerpt: full track, minus silent tail
- Source duration: `175.046531s` (`2:55.047`)
- Final duration: `174.567007s` (`2:54.567`)
- Edit reason: remove the `0.43s` trailing silence so the super-event ends cleanly
- Applied processing:
  - trimmed audio to `174.567s`
  - added `0.3s` fade-out from `174.267s` to `174.567s`
  - no loudness normalization applied

## Output Files

- Original downloaded source:
  - `docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3`
- Final music file:
  - `music/super_event_independence_wave_great_partition_week.ogg`
- Final sound wrapper file:
  - `sound/chaosx_super_event_independence_wave_great_partition_week.wav`

## Technical Notes

- Source metadata:
  - title: `Waiting TTTT`
  - artist: `Loyalty Freak Music`
  - album: `MINIMAL AMBIENT BOUNCE`
- Final `.ogg` loudness check:
  - integrated loudness: `-18.0 LUFS`
  - true peak: `-1.2 dBFS`
- File sizes:
  - source mp3: `7,079,715 bytes`
  - final ogg: `3,126,387 bytes`
  - final wav: `30,794,056 bytes`

## Conversion Steps

Source preservation:

```bash
curl -L --fail 'https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Music_for_Video/Loyalty_Freak_Music/MINIMAL_AMBIENT_BOUNCE/Loyalty_Freak_Music_-_05_-_Waiting_TTTT.mp3' \
  -o 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3'
```

Silence check:

```bash
ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3' \
  -af silencedetect=noise=-40dB:d=0.25 -f null -
```

Final renders:

```bash
ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3' \
  -vn -af "atrim=end=174.567,afade=t=out:st=174.267:d=0.3" \
  -c:a libvorbis -q:a 5 \
  'music/super_event_independence_wave_great_partition_week.ogg' -y

ffmpeg -i 'docs/plans/006_independence_wave_plans/source_audio/2026_05_31_fma_loyalty_freak_music_waiting_tttt_source.mp3' \
  -vn -af "atrim=end=174.567,afade=t=out:st=174.267:d=0.3" \
  -c:a pcm_s16le \
  'sound/chaosx_super_event_independence_wave_great_partition_week.wav' -y
```

## Suggested Parent Wiring Handoff

- Suggested sound definition id: `chaosx_super_event_independence_wave_great_partition_week`
- Suggested music key / logical label: `super_event_independence_wave_great_partition_week`
- Suggested super-event use: slot `56` unless parent changes the slot assignment

## Uncertainty / Risk

- License risk: low. The source page explicitly marks the track as `CC0 1.0 Universal`, and the same creator is the composer and recording source.
- Aesthetic risk: low-to-moderate. This is intentionally procedural and restrained; if the parent later wants more visible escalation, the next step would be a more percussive CC0 alternative, not a tragic orchestral cue.

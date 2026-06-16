# Event 013 Natural Disasters Evolution IV Super-Event Audio Research

Research timestamp: `2026-06-16T14:32:48Z`

## Scope note

This note covers only the bounded audio-research task for Event 013 Natural Disasters Evolution IV.

I did **not** edit sound definitions, event files, localisation, `.gfx`, or spreadsheets.

I also did **not** perform a broad repository reuse audit of existing Chaos Redux tracks, because this subagent pass was scoped to external licensing research and packaging rather than repo-wide uniqueness review.

## Super-event role fit

Target role from the prompt and spec: **abnormal disaster age**.

Required tone:

- grave and strange;
- recognisably tied to storm / earth / sea pressure;
- dramatic enough for the first abnormal high-chaos disaster burst;
- not a world-end cue and not a final-apocalypse lament.

## Recommendation

Recommended track: **Ludwig van Beethoven - Symphony No. 6 in F major "Pastoral", Op. 68 - IV. Allegro**

Why this fits:

- it is explicitly Beethoven's storm movement, so the natural-disaster connection is direct rather than abstract;
- the cue communicates pressure, thunder, instability, and mobilisation;
- it avoids the more terminal, funerary, or infernal tone that would push the event toward world-end finality;
- a trimmed excerpt preserves escalating storm force without drifting into a long concert movement.

Suggested sound definition id: `chaosx_super_event_013_abnormal_disaster_age`

Suggested super-event use: first Evolution IV abnormal burst, first abnormal earthquake wave, first meteor shower hitting several states, or first massive eruption / hyperstorm chain that makes governments treat disasters as a recurring global condition.

## Selected source and license review

### Selected candidate

- Track title: `Ludwig van Beethoven - symphony no. 6 in f major 'pastoral', op. 68 - iv. allegro.ogg`
- Composer: Ludwig van Beethoven
- Performer / recording source: Musopen recording distributed via Wikimedia Commons file page; exact ensemble is not named on the Commons page
- Source page: <https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_symphony_no._6_in_f_major_%27pastoral%27,_op._68_-_iv._allegro.ogg>
- Direct download used: <https://upload.wikimedia.org/wikipedia/commons/1/15/Ludwig_van_Beethoven_-_symphony_no._6_in_f_major_%27pastoral%27%2C_op._68_-_iv._allegro.ogg>
- Supporting source page for the composition listing: <https://musopen.org/music/2568-symphony-no-6-in-f-major-pastoral-op-68/>
- Duration of downloaded source: `3:40.152`

### Rights analysis

Composition rights:

- Beethoven died in 1827, so the composition is public domain.
- Commons marks the musical work as public domain / Public Domain Mark 1.0 on the file page.

Recording rights:

- Commons states that the recording was released into the public domain by Musopen, with a VRT-confirmed permission notice on the file page.
- The same page also states that if a public-domain dedication is not legally possible in a given jurisdiction, Musopen grants use for any purpose without conditions except those required by law.

Usage terms:

- usable for redistribution, derivative edits, and commercial/non-commercial mod packaging;
- attribution is courteous and advisable because Commons notes Musopen requested attribution when used inline.

Recommended attribution text:

`Source recording: Musopen / Wikimedia Commons - Ludwig van Beethoven, Symphony No. 6 in F major "Pastoral", Op. 68, IV. Allegro.`

License confidence: **high**

Confidence caveat:

- the license posture is strong enough for practical mod use, but the Commons page does not name the exact performing ensemble on this specific older upload, so performer identification is lower-confidence than the rights grant itself.

## Considered alternatives

### 1. Modest Mussorgsky - Night on Bald Mountain

- Source: <https://commons.wikimedia.org/wiki/File:Modest_Mussorgsky_-_night_on_bald_mountain.ogg>
- License posture: similar Musopen public-domain release statement on Commons
- Suitability: **rejected**
- Reason: the tone leans infernal / supernatural / sabbath-chaos and pushes too close to occult-apocalypse energy instead of abnormal natural systems.

### 2. Beethoven - Egmont Overture, Op. 84

- Source: <https://commons.wikimedia.org/wiki/File:Beethoven_EgmontOvertureOp.84_LudwigVanBeethoven-EgmontOvertureOp.84.ogg>
- License posture: very clear `CC0 1.0` on Commons
- Suitability: **backup only**
- Reason: legally cleaner than the selected cue, but thematically it reads as political tragedy / heroic resistance rather than earth-sky-sea disaster pressure.

## Packaged files

### Source preservation

- Original downloaded source path: `docs/assets/013_natural_disasters/audio/source/beethoven_pastoral_iv_storm_musopen_commons_source.ogg`
- SHA-256: `68df18fa3a5a19dd2375d454cdd622735aaaec176bebc365692d160b3da118a5`
- Size: `3691158` bytes
- Format: Ogg Vorbis, stereo, `48000 Hz`

### Derived preview

- Preview path: `docs/assets/013_natural_disasters/audio/previews/013_natural_disasters_beethoven_pastoral_iv_full_preview_44k.ogg`
- SHA-256: `008cc5c855444a9ac0ec5a534cd60ca049802e0b349e0632e82841eb0b35273a`
- Size: `3457570` bytes
- Format: Ogg Vorbis, stereo, `44100 Hz`
- Duration: `220.152018`

### Final candidate

- Final `.ogg` path: `docs/assets/013_natural_disasters/audio/final/013_natural_disasters_abnormal_disaster_age_beethoven_storm_excerpt.ogg`
- SHA-256: `f096b1a97c07b94bf4bb9db2bbfbfe74458cfe4e42991024869eaf6c57c70159`
- Size: `1719073` bytes
- Format: Ogg Vorbis, stereo, `44100 Hz`
- Duration: `110.000000`

## Editing and conversion steps

Source issue:

- the downloaded Commons file is `48 kHz`, so it is not game-ready under the stated super-event packaging rule.

Processing performed:

1. Downloaded the original Commons `.ogg` and preserved it unchanged under `docs/assets/013_natural_disasters/audio/source/`.
2. Decoded the source to temporary `44100 Hz` stereo WAV to normalize timestamps cleanly before re-encoding.
3. Re-encoded a full-length `44.1 kHz` preview `.ogg`.
4. Re-encoded a trimmed final excerpt:
   - start: `0:00`
   - end: `1:50`
   - gain: `-1.5 dB`
   - fade in: `0.5 s`
   - fade out: final `1.5 s`

Commands used:

```bash
curl -L 'https://upload.wikimedia.org/wikipedia/commons/1/15/Ludwig_van_Beethoven_-_symphony_no._6_in_f_major_%27pastoral%27%2C_op._68_-_iv._allegro.ogg' \
  -o docs/assets/013_natural_disasters/audio/source/beethoven_pastoral_iv_storm_musopen_commons_source.ogg

ffmpeg -y -i docs/assets/013_natural_disasters/audio/source/beethoven_pastoral_iv_storm_musopen_commons_source.ogg \
  -ar 44100 -ac 2 -c:a pcm_s16le /tmp/013_natural_disasters_audio.wav

ffmpeg -y -i /tmp/013_natural_disasters_audio.wav \
  -c:a libvorbis -q:a 5 -af 'volume=-1.5dB' \
  docs/assets/013_natural_disasters/audio/previews/013_natural_disasters_beethoven_pastoral_iv_full_preview_44k.ogg

ffmpeg -y -i /tmp/013_natural_disasters_audio.wav -t 110 \
  -c:a libvorbis -q:a 5 \
  -af 'volume=-1.5dB,afade=t=in:st=0:d=0.5,afade=t=out:st=108.5:d=1.5' \
  docs/assets/013_natural_disasters/audio/final/013_natural_disasters_abnormal_disaster_age_beethoven_storm_excerpt.ogg
```

## Practical implementation notes for the main agent

- The packaged final file is ready for wiring from an audio-format standpoint: Ogg Vorbis, stereo, `44100 Hz`.
- If the main agent wants a slightly more abrupt emergency feel, the easiest safe variant is a later start cut, not a different track.
- If the project wants the legally simplest alternate despite weaker fit, `Egmont Overture` is the cleanest alternate candidate from this pass because its Commons page is explicitly `CC0`.

## Uncertainty and blockers

No hard blocker for packaging the selected candidate.

Remaining uncertainty:

- exact performer credit is not stated on the specific Commons file page for this older Pastoral movement upload;
- because of that, performer identification confidence is lower than license confidence;
- I did not inspect existing Chaos Redux music manifests or live wired super-event tracks in this scoped pass, so uniqueness against current repo usage still needs confirmation by the main agent before final wiring.

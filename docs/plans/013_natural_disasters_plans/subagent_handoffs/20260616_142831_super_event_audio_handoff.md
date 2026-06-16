# Super-Event Audio Handoff — Event 013 Natural Disasters

Timestamp: `2026-06-16T14:32:48Z`

## Recommendation

Use:

- suggested audio id: `chaosx_super_event_013_abnormal_disaster_age`
- recommended display/reference name: `Event 013 Abnormal Disaster Age`
- final candidate path: `docs/assets/013_natural_disasters/audio/final/013_natural_disasters_abnormal_disaster_age_beethoven_storm_excerpt.ogg`

Track:

- title: `Ludwig van Beethoven - Symphony No. 6 in F major "Pastoral", Op. 68 - IV. Allegro`
- composer: Ludwig van Beethoven
- performer / recording source: Musopen recording distributed via Wikimedia Commons; exact ensemble not named on the specific Commons file page
- duration: `110.000000` seconds final, `220.152000` seconds original source

## Why this is the recommendation

This cue is the most on-theme candidate from the research pass. It is explicitly Beethoven's storm movement, so it matches meteor / storm / earthquake / ashfall escalation better than a generic tragic overture. It feels grave and unstable without sounding like the campaign is ending.

## Source and license evidence

- Commons source page: <https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_symphony_no._6_in_f_major_%27pastoral%27,_op._68_-_iv._allegro.ogg>
- Direct download used: <https://upload.wikimedia.org/wikipedia/commons/1/15/Ludwig_van_Beethoven_-_symphony_no._6_in_f_major_%27pastoral%27%2C_op._68_-_iv._allegro.ogg>
- Musopen composition page: <https://musopen.org/music/2568-symphony-no-6-in-f-major-pastoral-op-68/>

License conclusion:

- composition rights: public domain
- recording rights: Commons file page says Musopen released the recording into the public domain and includes VRT-confirmed permission text
- license confidence: **high**

Attribution text if you want to keep one in documentation:

`Source recording: Musopen / Wikimedia Commons - Ludwig van Beethoven, Symphony No. 6 in F major "Pastoral", Op. 68, IV. Allegro.`

## Files produced

- source copy: `docs/assets/013_natural_disasters/audio/source/beethoven_pastoral_iv_storm_musopen_commons_source.ogg`
- full-length preview: `docs/assets/013_natural_disasters/audio/previews/013_natural_disasters_beethoven_pastoral_iv_full_preview_44k.ogg`
- final candidate: `docs/assets/013_natural_disasters/audio/final/013_natural_disasters_abnormal_disaster_age_beethoven_storm_excerpt.ogg`
- manifest: `docs/assets/013_natural_disasters/audio/manifest.json`
- research note: `docs/super_events/013_natural_disasters_super_event_audio_research.md`

## Processing notes

- preserved the original download unchanged
- normalized through temporary WAV because the source Ogg carried timestamp quirks
- converted the deliverables to `44100 Hz` stereo Ogg Vorbis
- final excerpt is the first `110` seconds of the movement with `-1.5 dB` gain, `0.5 s` fade-in, and `1.5 s` fade-out

## Main-agent follow-up

- confirm repo-wide uniqueness before wiring, since this subagent pass did not inspect existing Chaos Redux audio manifests
- wire the final candidate through the project audio definitions and the settings-aware helper
- keep the recommended id unless a local naming convention requires a small rename

## Remaining caveat

The exact performing ensemble is not named on the specific older Commons file page for this Pastoral movement upload. That is a credit-quality gap, not a blocker to using the recording under the documented license posture.

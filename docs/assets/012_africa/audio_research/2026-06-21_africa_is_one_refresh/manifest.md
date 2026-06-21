# Event 012 Africa Is One Audio Refresh Research

Updated: `2026-06-21`

## Scope

- Event ID: `012`
- Target super-event role: `africa_is_one_unification`
- Target visible slot: `68`
- In-game title: `Africa Is One`
- Scope in this note: source audit, legal review, download preservation, conversion, promotion handoff, and parent promotion status
- Live `music/` and `sound/` files were promoted by the main agent after review

## Superseded live slot audit

- Superseded live slot-68 cue path: `music/super_event_africa_unification.ogg`
- Superseded canonical docs copy: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
- Superseded live SHA-256 before promotion: `1d348c562facc87cddbddb0859676cbfb957d369ab00dc0142419bc9331861e2`
- Superseded source direction recorded in older manifests: `Rush Peace dance concert 1 libtheora`
- Why it is a weak fit for this request: the source page describes a peace-dance competition held toward the `2016` election, which is African and legally reusable but less specific to continental unification under pressure than a more clearly traditional ensemble performance

## Recommended replacement candidate

- Track title: `Bawadance`
- Creator / composer: traditional Bawa dance music of the people of Ghana's Upper West Region; no named modern composer is asserted on the source page
- Performer / recording source: live dance ensemble documented by Wikimedia Commons user `Bayelharriet`
- Source URL: <https://commons.wikimedia.org/wiki/File:Bawadance.ogv>
- Direct binary URL used for preservation: <https://upload.wikimedia.org/wikipedia/commons/3/33/Bawadance.ogv>
- License / terms: `CC BY-SA 4.0`
- Required attribution text: `Bayelharriet, "Bawadance", via Wikimedia Commons, CC BY-SA 4.0. Modified for length, fades, loudness, and audio-only conversion.`
- Composition-rights confidence: `medium-high`
- Composition-rights note: the Commons summary describes Bawa as a traditional dance of the people of the Upper West Region in Ghana, performed around xylophone and drums; I found no named contemporary composer claim on the source page
- Recording-rights confidence: `high`
- Recording-rights note: the uploader marks the file as `Own work` and licenses it under `CC BY-SA 4.0`
- Overall license confidence: `medium-high`
- Duration, source: `01:34.912`
- Duration, final candidate: `01:34.903`
- Why it fits: the source is explicitly Ghanaian traditional dance music built around sung ensemble, xylophone, and drums; it reads as celebratory but forceful, which fits Pan-African unification better than the current election peace-dance cue and avoids the rejected European hymn / classical direction

## Preserved files

- Original downloaded source path: `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/source/bawadance_original.ogv`
- Original source SHA-256: `9e3c2253a8b28acc57a1cb00044dc507f5e989372e0df7a528b0ece98daea2a1`
- Final OGG path: `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/final/super_event_africa_is_one_bawadance_candidate.ogg`
- Final OGG SHA-256: `143d58e6dca84bb86446e657987120c15b2c4aa00583df3fd0cbddb260710a2f`
- Final WAV path: `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/final/chaosx_super_event_africa_is_one_bawadance_candidate.wav`
- Final WAV SHA-256: `97ccab5325a709d42b323db08d3502a5786c62a8546890be547709b9fea5832d`

## Technical validation

- Source probe: Theora/Vorbis container, audio stream `48000 Hz`, stereo, duration `94.912s`
- Final OGG probe: Vorbis, `44100 Hz`, stereo, duration `94.902902s`
- Final WAV probe: `pcm_s16le`, `44100 Hz`, stereo, duration `94.890680s`
- Sample-rate target met: yes, both final deliverables are `44.1 kHz`

## Parent promotion status

- Promoted live OGG target: `music/super_event_africa_unification.ogg`
- Promoted docs OGG target: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
- Promoted live WAV target: `sound/chaosx_super_event_africa_unification.wav`
- Promoted live OGG SHA-256: `143d58e6dca84bb86446e657987120c15b2c4aa00583df3fd0cbddb260710a2f`
- Promoted live WAV SHA-256: `97ccab5325a709d42b323db08d3502a5786c62a8546890be547709b9fea5832d`
- `.asset` and playlist identifiers remain unchanged because the promotion replaced the existing slot-68 files in place

## Editing and conversion steps

1. Downloaded the original Wikimedia Commons binary without transcoding and preserved it unchanged.
2. Converted audio only from the source container.
3. Applied `loudnorm=I=-18:LRA=11:TP=-1.5`.
4. Added a short fade-in of `0.5s`.
5. Added a short fade-out over the last `1.2s`.
6. Resampled to `44.1 kHz` stereo Vorbis for the game-ready candidate OGG.
7. Rendered a matching `44.1 kHz` stereo PCM WAV wrapper for promotion into the existing sound-channel path if accepted.

## Suggested promotion / wiring notes for the main agent

- Suggested super-event use: Event `012`, slot `68`, `Africa Is One`
- Suggested sound definition id to keep: `chaosx_super_event_africa_unification_track`
- Suggested music file target to replace if promoted: `music/super_event_africa_unification.ogg`
- Suggested sound file target to regenerate if promoted: `sound/chaosx_super_event_africa_unification.wav`
- Suggested docs copy target if promoted: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`
- No `.asset` or `.txt` identifier changes are required if the main agent promotes this by file replacement only

## Rejected / not promoted in this pass

- The subagent did not promote the candidate over the live file automatically because the main agent owns final promotion
- I did not reuse `Ghana Dancers Group` for the unification replacement candidate because its Commons summary is only `battle dance`, which is a weaker provenance note for composition/origination than the more explicit traditional Bawa page

## Blockers and simplifications

- No hard recording-license blocker remains for this candidate
- Residual caution: the underlying music is documented on Commons as traditional rather than as a separately cataloged public-domain composition, so composition provenance is strong enough for recommendation but not as ironclad as an institutional archive record with explicit folklore/public-domain wording
- Simplification: none for slot-68 promotion; the live files were replaced in place after parent review

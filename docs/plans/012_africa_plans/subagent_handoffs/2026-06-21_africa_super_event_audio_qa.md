# Africa Super-Event Audio QA

Date: `2026-06-21`

Scope: QA of the current Event `012` Africa super-event audio response to the request that Africa music use Africa-related material rather than European-composer hymns / classical / anthem cues.

Files inspected:

- `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/`
- `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/`
- `docs/assets/012_africa/super_events/audio/manifest.md`
- `music/chaosx_super_event_music.asset`
- `music/chaosx_super_event_music.txt`
- `sound/chaosx_sound.asset`
- `docs/super_events/012_africa_super_event_research.md`
- `music/chaosx_music_track_list.html`
- `events/012_african_union.txt`
- `common/scripted_effects/012_africa_effects.txt`

## QA result

Status: pass

I found no broken live path, no broken live id, no missing slot-68 final `.ogg`, and no evidence that the current `Africa Is One` live super-event still points at the rejected European-composer direction.

## Evidence

### 1. `Africa Is One` live wiring points at the intended Africa-related track

- `common/scripted_effects/012_africa_effects.txt` sets `global.current_super_event_audio_id = constant:africa_super_event.africa_is_one` inside `africa_emit_africa_is_one_super_event`.
- `music/chaosx_super_event_music.txt` maps slot `68` to `chaosx_super_event_68_1_5`.
- `music/chaosx_super_event_music.asset` maps every `chaosx_super_event_68_*` entry to `super_event_africa_unification.ogg`.
- `sound/chaosx_sound.asset` maps every `chaosx_super_event_68_sound_*` entry to `chaosx_super_event_africa_unification_track`, which points at `sound/chaosx_super_event_africa_unification.wav`.

This chain is internally consistent.

### 2. The live `Africa Is One` file is the documented `Bawadance` promotion, not an older placeholder

- `music/super_event_africa_unification.ogg` exists.
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg` exists.
- `sound/chaosx_super_event_africa_unification.wav` exists.
- SHA-256 matches:
  - live OGG: `143d58e6dca84bb86446e657987120c15b2c4aa00583df3fd0cbddb260710a2f`
  - docs canonical OGG: `143d58e6dca84bb86446e657987120c15b2c4aa00583df3fd0cbddb260710a2f`
  - dated candidate OGG: `143d58e6dca84bb86446e657987120c15b2c4aa00583df3fd0cbddb260710a2f`
  - live WAV: `97ccab5325a709d42b323db08d3502a5786c62a8546890be547709b9fea5832d`
  - dated candidate WAV: `97ccab5325a709d42b323db08d3502a5786c62a8546890be547709b9fea5832d`

This proves the live slot-68 asset is the promoted `Bawadance` replacement documented in `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/manifest.md`.

### 3. Format requirement is met

Probe result for `music/super_event_africa_unification.ogg`:

- codec: `vorbis`
- sample rate: `44100`
- channels: `2`
- duration: `94.902902s`

Probe result for `sound/chaosx_super_event_africa_unification.wav`:

- codec: `pcm_s16le`
- sample rate: `44100`
- channels: `2`
- duration: `94.890680s`

I also spot-checked all live Africa music OGGs and all live Africa sound WAVs for slots `68-80`; every file probed at `44100 Hz`, stereo.

### 4. Source, title, creator/source, and license are documented

For slot `68`, the live documentation chain now records:

- title: `Bawadance`
- creator/composition description: traditional Bawa dance music from Ghana's Upper West Region
- performer / recording source: Wikimedia Commons recording by `Bayelharriet`
- source URL: `https://commons.wikimedia.org/wiki/File:Bawadance.ogv`
- binary preservation URL: `https://upload.wikimedia.org/wikipedia/commons/3/33/Bawadance.ogv`
- license: `CC BY-SA 4.0`
- attribution text: documented
- duration: `94.9s`
- preserved source path: `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/source/bawadance_original.ogv`
- final candidate path: `docs/assets/012_africa/audio_research/2026-06-21_africa_is_one_refresh/final/super_event_africa_is_one_bawadance_candidate.ogg`
- promoted live path: `music/super_event_africa_unification.ogg`
- promoted docs copy: `docs/assets/012_africa/super_events/audio/final/super_event_africa_unification.ogg`

The same slot is also reflected consistently in:

- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/super_events/012_africa_super_event_research.md`
- `music/chaosx_music_track_list.html`

### 5. No sign of placeholder or test-tone audio

- The live slot-68 file hash matches the preserved conversion from a real Wikimedia Commons field/performance recording.
- The source preservation file is a real Theora/Vorbis media file with video plus live audio, not a synthetic local render.
- The documented conversion chain includes loudness normalization and fades, not waveform generation.
- The live OGG duration, bitrate, and provenance match the preserved candidate package rather than any repository placeholder/test artifact.

On the evidence available, this is a sourced live-performance cue, not a generated tone, beep, or placeholder.

## Residual risks

1. The Africa correction is live and correctly wired, but the repo still keeps older dated replacement-candidate docs under `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/`. That is not a live bug, but future readers need to follow the live manifest and the slot-68 refresh note rather than treating the earlier package as the final authority for `Africa Is One`.
2. The broader Africa package still has documented source-family reuse for slots `70/80` and `75/79`. That is a diversity concern, not a legality or wiring defect.

## Files changed

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_africa_super_event_audio_qa.md`

## No patch needed

I found no concrete broken file path or id that required a gameplay or sound-definition patch.

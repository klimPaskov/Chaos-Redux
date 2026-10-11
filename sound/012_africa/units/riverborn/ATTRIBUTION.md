# Riverborn sound attribution

Every installed file is an edited arrangement of recordings that were already archived in this repository with a recorded licence (cut, fade, pitch-shift, EQ, level, layering, mono, 44.1 kHz, PCM16 conversion). No tone, noise bed, synthesized, generated or newly recorded audio is present. No recording was downloaded for this rework.
Licence statements are inherited from the archived source records; derivative licensing was not independently reassessed. CC BY 4.0 material needs the credit line given in the table; CC0 and public-domain items are credited voluntarily.

## Source recordings

| Key | Recording | Creator | Licence | URL | Archived original (repo-relative) | Source SHA-256 | Note |
|---|---|---|---|---|---|---|---|
| bodyfall_bsb | Body Fall #1 | Joseph SARDIN (BigSoundBank) | CC0 1.0 | https://bigsoundbank.com/body-fall-1-s2452.html | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/impact/2452.wav` | `4770f7b32fcab7437c5b1ce79b80df592f3ff76885c49c62fb367d74a4f3430c` |  |
| bodyfall_dirt | BODY FALL - V HVY - DIRT | leonelmail | CC0 1.0 | https://freesound.org/people/leonelmail/sounds/504626/ | `docs/assets/shared_clone_system/models_3d/clone_infantry/audio/closure_20260912/originals/body_fall_504626_hq.mp3` | `336a44d95279173764073a9b2d4d7e12f4167cfb0c1ad5c58e316895e129c6bb` | official HQ preview |
| swosh16 | Bamboo-stick swishes: swosh-16 | qubodup | CC0 1.0 | https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes | `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/src/staff_swishes/swosh-16.flac` | `0e882f9cef2ca536fae1efa9fadcfc5f8f1fc6a1dafc55d8c2ee62a95cd71b16` | extracted from archived staff_swishes.7z; member of archive `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/staff_swishes.7z` (SHA-256 `2d55b26f918a4d8042e2c97a4db81392757195f5aaac9039f5ec2c557b6f11f2`) |
| swosh20 | Bamboo-stick swishes: swosh-20 | qubodup | CC0 1.0 | https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes | `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/src/staff_swishes/swosh-20.flac` | `a1c28eddda0cc420159805dc8876fa0938ba1b1a36e6d6159b6bb034ca69d79c` | extracted from archived staff_swishes.7z; member of archive `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/staff_swishes.7z` (SHA-256 `2d55b26f918a4d8042e2c97a4db81392757195f5aaac9039f5ec2c557b6f11f2`) |
| swosh22 | Bamboo-stick swishes: swosh-22 | qubodup | CC0 1.0 | https://opengameart.org/content/swish-bamboo-stick-weapon-swhoshes | `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/src/staff_swishes/swosh-22.flac` | `c2d125db98ff2d79f3a89a08a24b6618dc1f0410c2cc717e8cc83ebc6956dcca` | extracted from archived staff_swishes.7z; member of archive `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/staff_swishes.7z` (SHA-256 `2d55b26f918a4d8042e2c97a4db81392757195f5aaac9039f5ec2c557b6f11f2`) |

## Installed files (11 Oct 2026 rework)

| Runtime file | Soundeffect | Role | Composition from the recordings above | Composite SHA-256 | Before SHA-256 | Installed SHA-256 | Length s | Peak dBFS | RMS dBFS | LUFS | TP dBTP | Loudest 5 ms window s | Head trimmed by master s | Designed contact in file s |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `chaosx_riverborn_attack.wav` | chaosx_riverborn_attack_sfx | shot | swosh22 0.000-0.320 s, placed at 0.250 s; bodyfall_dirt 0.400-0.950 s, placed at 0.360 s, pitch +2 st (rubberband), lowpass 900 Hz, -2 dB | `7fd3a68518b5fa3d9ebdccef624cff55e8f401e8919bb58c918cb8e0c58f5b89` | `26ffe43934ac355da6df6887968b061ad54bef41a80bbe7d2bc69f506351d994` | `c887027575df4a5d0cbd763c57b947f510fe554f1465783b7814941db4fa28af` | 0.605578 | -3.01 | -21.31 | -23.5 | -3.0 | 0.08 | 0.2444 | 0.156 |
| `chaosx_riverborn_attack_02.wav` | chaosx_riverborn_attack_sfx | shot | swosh16 0.000-0.440 s, placed at 0.230 s; bodyfall_bsb 0.160-0.710 s, placed at 0.340 s, pitch +1 st (rubberband), lowpass 1100 Hz, -2 dB | `70a5e85b06d3dd8147526838a20a2035435c219563c77c352d89d50b77a748ea` | `new file` | `f218558eb9fa7e7532511fe12f643ba6e844bb5c8dae1f870283d08627e17ad5` | 0.630522 | -3.0 | -21.22 | -23.3 | -3.0 | 0.18 | 0.2195 | 0.181 |
| `chaosx_riverborn_attack_03.wav` | chaosx_riverborn_attack_sfx | shot | swosh20 0.000-0.450 s, placed at 0.220 s; bodyfall_dirt 0.520-1.070 s, placed at 0.360 s, pitch +3 st (rubberband), lowpass 800 Hz, -2 dB | `509dab282aed6eacfb9c86ee84f8252c9258a087dd24716d0985d5c7776b2bdf` | `new file` | `37ed6818b350943199f2bdd4cba4f8ac2f1fca1532e4cfb73ad7e1be18966759` | 0.640499 | -3.02 | -21.1 | -23.1 | -3.0 | 0.065 | 0.2095 | 0.191 |

Every installed file above is pcm_s16le, 44.1 kHz, mono, produced by `.tools/3d_pipeline/audio/master.py batch` (30 Hz high-pass, 8 ms fade-in, 50 ms fade-out, role peak/RMS/loudness gates, source clipping gate, lead silence at most 20 ms). Mastering evidence per file: `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/reports/riverborn_all_report.json` and `cuts/*.recipe.json` (ignored working area).

## BLOCKED cues (missing recording)

- `attack` wet impact: needs a CC0 wet thud or slap impact pack, 0.2-0.5 s. The installed takes are a recorded bamboo-staff whoosh plus a dry recorded ground/body thump; the wet character is missing.
- `move` wet bare-foot steps: needs a CC0 wet footstep recording, 0.1-0.3 s; none is archived. File unchanged (float32, no source record).
- `idle`, `water_transition`: need a water-flow or splash recording (the earlier Flowing-water-100019 and Ducks-landing originals are no longer in the archive). Files unchanged (float32, no source record).
- `select` 5 ms fade-in and `death`: the current files have no source record, so they cannot be re-edited under the licence rule; files unchanged (float32).

## Files not changed in this rework

- `chaosx_riverborn_idle.wav`, `_move`, `_select`, `_death`, `_water_transition`: float32, no source record; see BLOCKED above.

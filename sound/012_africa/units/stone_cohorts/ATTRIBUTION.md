# Stone Cohorts sound attribution

Every installed file is an edited arrangement of recordings that were already archived in this repository with a recorded licence (cut, fade, pitch-shift, EQ, level, layering, mono, 44.1 kHz, PCM16 conversion). No tone, noise bed, synthesized, generated or newly recorded audio is present. No recording was downloaded for this rework.
Licence statements are inherited from the archived source records; derivative licensing was not independently reassessed. CC BY 4.0 material needs the credit line given in the table; CC0 and public-domain items are credited voluntarily.

## Source recordings

| Key | Recording | Creator | Licence | URL | Archived original (repo-relative) | Source SHA-256 | Note |
|---|---|---|---|---|---|---|---|
| debris_crash | Big falling debris (crash) | xkeril | CC0 1.0 | https://freesound.org/people/xkeril/sounds/703247/ | `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/polish_20260927/original/703247_debris_crash_big_hq_preview.mp3` | `6d812be91eec9ceea5d4ad50ab8d0c290977be7f1a24f5ae25327dec0a94b944` | archived HQ preview |
| dynamite | Dynamite explosion in the mountain | felix.blume | CC0 1.0 | https://freesound.org/people/felix.blume/sounds/251401/ | `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/polish_20260927/original/251401_dynamite_mountain_hq_preview.mp3` | `03ede4462a6657fdd181fa65f9aab9d6fcc181be6cdbb2fb461ee2aa638da318` | archived HQ preview |
| metal_drop | Metal drop thump | stephan (PDSounds) | Public domain dedication | https://commons.wikimedia.org/wiki/File:Metal_drop_thump.ogg | `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/original/metal_drop_thump.ogg` | `b8f5506893d2871c86f5c7e01305bff788dfe156a265e63bb9b00cbbd51647c5` |  |
| quern | WWS Quern-stones | Work With Sounds / Monika Widzicka | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg | `docs/assets/012_africa/models_3d/stone_cohorts/audio/source/quern_stones.ogg` | `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7` |  |
| thud_metal | Metal Impact Sounds (thud2.wav) | Brian MacIntosh (BMacZero) | CC0 1.0 | https://opengameart.org/content/metal-impact-sounds | `docs/assets/039_murder_mystery/audio/source/thud2.wav` | `5fb5c1b37a95cb6716d0bb529a0b9fe1ae9f3e2228b8f30c5c3dcbb1b570a3af` |  |

### Credit lines required by the licences

- WWS Quern-stones by Work With Sounds / Monika Widzicka, CC BY 4.0, https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg

## Installed files (11 Oct 2026 rework)

| Runtime file | Soundeffect | Role | Composition from the recordings above | Composite SHA-256 | Before SHA-256 | Installed SHA-256 | Length s | Peak dBFS | RMS dBFS | LUFS | TP dBTP | Loudest 5 ms window s | Head trimmed by master s | Designed contact in file s |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `chaosx_stone_cohorts_attack.wav` | chaosx_stone_cohorts_attack_sfx | shot | debris_crash 0.140-0.400 s, placed at 0.000 s; thud_metal 0.000-0.340 s, placed at 0.060 s | `da47bb363eb95235e96cfb312090a79414b8ffe19e49b220d4dbf91fb1e727b1` | `new file` | `ad6d986d9f97470da4bccc5acb0e0efeb98119568c28f8d9214a95c018225c10` | 0.4 | -3.0 | -16.87 | -17.5 | -3.0 | 0.105 | 0.0 | - |
| `chaosx_stone_cohorts_attack_02.wav` | chaosx_stone_cohorts_attack_sfx | shot | debris_crash 0.320-0.580 s, placed at 0.000 s; thud_metal 0.000-0.340 s, placed at 0.060 s, pitch -4 st (rubberband) | `549c4c6c66465c6c646258f40d2264333b43cd7ae35f7945b7f277f104df57ef` | `new file` | `f3b4b132762a081936d7cc6c1109aca21cd6b0ebfcfe3118cbdcc6dafb2174f7` | 0.4 | -3.0 | -18.37 | -18.6 | -3.0 | 0.11 | 0.0 | - |
| `chaosx_stone_cohorts_attack_03.wav` | chaosx_stone_cohorts_attack_sfx | shot | debris_crash 0.480-0.740 s, placed at 0.000 s; thud_metal 0.000-0.340 s, placed at 0.060 s, pitch -2 st (rubberband), lowpass 3000 Hz; metal_drop 0.340-0.740 s, placed at 0.050 s, lowpass 800 Hz, -8 dB | `1d405207e747bc783ac20a9648c8e25904e522694602fb2beebcd79e38c7d342` | `new file` | `31798c9799a83ac83497c0a74e52d53ed61c4896ea210b4b8ec2bdce73b6f2a3` | 0.42 | -3.0 | -17.84 | -17.9 | -3.0 | 0.1 | 0.0 | - |
| `chaosx_stone_cohorts_death.wav` | chaosx_stone_cohorts_death_sfx | shot | debris_crash 0.000-2.400 s, placed at 0.000 s, pitch -2 st (rubberband); quern 12.000-13.900 s, placed at 0.500 s, highpass 80 Hz, -3 dB | `7d91ec96ad314d1652de51e9c400d182f2a3cd83101bd28ae7fd4e0910e1ef7c` | `new file` | `77dd76f2f93b65d496ad88a4e06a48eda91d2a5f3e9d71c7ace6952e78b8ce1e` | 2.4 | -3.0 | -21.78 | -21.4 | -3.0 | 0.319 | 0.0 | - |
| `chaosx_stone_cohorts_death_02.wav` | chaosx_stone_cohorts_death_sfx | shot | debris_crash 0.600-2.400 s, placed at 0.000 s; dynamite 1.700-3.700 s, placed at 0.200 s, lowpass 2500 Hz, -5 dB | `96b576a3b94fe05e84bde598a4f1814932b6a16f9571211799e5c38edc46094c` | `new file` | `3c58304aada1fe860b7d005d339bdcd9e835d5ad4f46ed7faada97e07d8d8269` | 2.2 | -3.0 | -20.17 | -21.2 | -2.9 | 0.07 | 0.0 | - |
| `chaosx_stone_cohorts_move.wav` | chaosx_stone_cohorts_move_sfx | step | quern 8.620-8.980 s, placed at 0.000 s | `ae9d381ecf16ade2861772400be644b4ac810798badfa882d7822f4763959078` | `new file` | `3f03fd6691196c5aa669e2a777675f065ab352fc92099d670ba430bd6674f65b` | 0.36 | -6.0 | -19.24 | -70.0 | -6.0 | 0.11 | 0.0 | - |
| `chaosx_stone_cohorts_move_02.wav` | chaosx_stone_cohorts_move_sfx | step | quern 20.380-20.740 s, placed at 0.000 s | `a87d7b5d23e5e178aa4b660bfb32b45d6559f463310f2ba3bb61f7d0a5c006b1` | `new file` | `2dd0fe0f31fa3fdab1f83ca18d363734b84033178d29f57a6c04d9c9a952109a` | 0.36 | -6.0 | -19.15 | -70.0 | -5.9 | 0.264 | 0.0 | - |
| `chaosx_stone_cohorts_move_03.wav` | chaosx_stone_cohorts_move_sfx | step | quern 40.820-41.180 s, placed at 0.000 s | `84a672488cc022b09307db4bfa006efb5018a4d55a17a3e7b17c3faa19a864b2` | `new file` | `aec7178d74ad7690770a0d58ed45dc3235e445549aa977c5b8e03f6a11cc196a` | 0.36 | -6.0 | -20.91 | -70.0 | -6.0 | 0.075 | 0.0 | - |
| `chaosx_stone_cohorts_idle.wav` | chaosx_stone_cohorts_idle_sfx | shot | quern 12.000-14.200 s, placed at 0.000 s | `77792a9f2b2d425991bc7e4d8b9891f3fb4e86042ab5abbde47b33cab07e40ee` | `new file` | `9220b9d264d769f22d6ba90c4dccb3d83758c97044caf4e9f6f065410219eafb` | 2.2 | -3.0 | -21.81 | -19.4 | -3.0 | 0.678 | 0.0 | - |
| `chaosx_stone_cohorts_idle_02.wav` | chaosx_stone_cohorts_idle_sfx | shot | quern 33.000-35.200 s, placed at 0.000 s | `90510d354c97716382257861a49c9ecb93e273dc73a197e133c5f502e1d0895b` | `new file` | `cf698a3785660572992d37263374bb6aa4eb49a577521f25e89f7d561e23e001` | 2.2 | -3.0 | -21.38 | -19.1 | -2.9 | 0.284 | 0.0 | - |
| `chaosx_stone_cohorts_select.wav` | chaosx_stone_cohorts_select_sfx | shot | quern 20.300-21.700 s, placed at 0.000 s | `69bcd90631b505251f9d61f82299100bbe14011f276b3df6fbdfd05c3282001f` | `new file` | `77e7a66062cbca10b1b60f115d5dec10871a54b6c44e274585f4198ae64230b2` | 1.4 | -3.0 | -20.19 | -17.7 | -2.9 | 0.344 | 0.0 | - |
| `chaosx_stone_cohorts_select_02.wav` | chaosx_stone_cohorts_select_sfx | shot | quern 40.700-42.100 s, placed at 0.000 s | `cdae1a63825ec9ee4f9997e08931c52ce9a24080f6f45ff74c26b80199900a3a` | `new file` | `e52210257afa83ec6924f95bd4fc8d26d22f1bf81909356bbf19808e84177975` | 1.4 | -3.0 | -20.97 | -18.1 | -2.9 | 0.259 | 0.0 | - |

Every installed file above is pcm_s16le, 44.1 kHz, mono, produced by `.tools/3d_pipeline/audio/master.py batch` (30 Hz high-pass, 8 ms fade-in, 50 ms fade-out, role peak/RMS/loudness gates, source clipping gate, lead silence at most 20 ms). Mastering evidence per file: `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/reports/stone_cohorts_all_report.json` and `cuts/*.recipe.json` (ignored working area).

## BLOCKED cues (missing recording)

- `attack` rock-impact pack: needs three clean CC0 stone-on-stone or stone-on-iron single impacts, 0.3-0.5 s. The installed takes combine one recorded hit out of the CC0 tile/stone/metal debris crash with the recorded metal thud (closest archived match; the debris recording is a crash, not an isolated rock strike).
- `death` rockslide: needs a PD/CC0 rockslide or large rock-fall recording, 1-3 s. Take 1 layers the debris crash with the CC BY quern grind; take 2 layers the crash with the tail of the CC0 rock-blast recording.
- `collapse_recovery` settling-stone rumble from the rockslide source: unchanged (three quern-grind takes installed earlier); needs the same rockslide recording.

## Files not changed in this rework

- `chaosx_stone_cohorts_collapse_recovery.wav`, `_02`, `_03`: installed earlier by the parent from the Work With Sounds quern recording (CC BY 4.0); source chain in `docs/plans/unit_fix_2026-10/wp1_sound_attribution.md`.

# Oracle Recon sound attribution

Every installed file is an edited arrangement of recordings that were already archived in this repository with a recorded licence (cut, fade, pitch-shift, EQ, level, layering, mono, 44.1 kHz, PCM16 conversion). No tone, noise bed, synthesized, generated or newly recorded audio is present. No recording was downloaded for this rework.
Licence statements are inherited from the archived source records; derivative licensing was not independently reassessed. CC BY 4.0 material needs the credit line given in the table; CC0 and public-domain items are credited voluntarily.

## Source recordings

| Key | Recording | Creator | Licence | URL | Archived original (repo-relative) | Source SHA-256 | Note |
|---|---|---|---|---|---|---|---|
| bodyfall_bsb | Body Fall #1 | Joseph SARDIN (BigSoundBank) | CC0 1.0 | https://bigsoundbank.com/body-fall-1-s2452.html | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/impact/2452.wav` | `4770f7b32fcab7437c5b1ce79b80df592f3ff76885c49c62fb367d74a4f3430c` |  |
| bodyfall_dirt | BODY FALL - V HVY - DIRT | leonelmail | CC0 1.0 | https://freesound.org/people/leonelmail/sounds/504626/ | `docs/assets/shared_clone_system/models_3d/clone_infantry/audio/closure_20260912/originals/body_fall_504626_hq.mp3` | `336a44d95279173764073a9b2d4d7e12f4167cfb0c1ad5c58e316895e129c6bb` | official HQ preview |
| exewin11 | Death Sounds, take 11 | Exewin | CC0 1.0 | https://opengameart.org/content/death-sounds-0 | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/death/extracted/11.ogg` | `b34c8b54bf8da277cac46829d3a3e6b729919e62709643dc5de4e1d5235ba865` |  |
| exewin4 | Death Sounds, take 4 | Exewin | CC0 1.0 | https://opengameart.org/content/death-sounds-0 | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/death/extracted/4.ogg` | `dfc67cd0aa6a1d71cd9ec8eea07f64dbbf301e23817331687c66cb42e409b503` |  |
| exewin6 | Death Sounds, take 6 | Exewin | CC0 1.0 | https://opengameart.org/content/death-sounds-0 | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/death/extracted/6.ogg` | `4c8693c3c68a7a44ad27566bb1f5be9c7e411a89e4904ca177cb3989431c5647` |  |

## Installed files (11 Oct 2026 rework)

| Runtime file | Soundeffect | Role | Composition from the recordings above | Composite SHA-256 | Before SHA-256 | Installed SHA-256 | Length s | Peak dBFS | RMS dBFS | LUFS | TP dBTP | Loudest 5 ms window s | Head trimmed by master s | Designed contact in file s |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `chaosx_oracle_recon_death.wav` | chaosx_oracle_recon_death_sfx | shot | exewin6 0.000-1.200 s, placed at 0.000 s; bodyfall_bsb 0.100-1.100 s, placed at 0.620 s, lowpass 3500 Hz, -4 dB | `d1c8c2664069197ee47e954eb4018f33ac086f6a0dc3f615165e82dbdd4c1f95` | `184cb87973ec4933bdb6e4341b13a4f9823c8193c8a08bb32a904692537e2256` | `639885dd4eb62ab07f5ebbb4442678df6c5cc3c42b3064125dc2795c6fcdfa4a` | 1.535057 | -3.0 | -21.8 | -21.9 | -3.0 | 0.723 | 0.0149 | - |
| `chaosx_oracle_recon_death_02.wav` | chaosx_oracle_recon_death_sfx | shot | exewin11 0.000-0.940 s, placed at 0.000 s; bodyfall_dirt 0.300-1.300 s, placed at 0.550 s, pitch -1 st (rubberband), lowpass 2500 Hz, -4 dB | `95413ce4ba0c314ca83c62e1bd8032530ba8071ad0f8a68c0f6d7d78924d65be` | `new file` | `b4fa9d1f53c2890e10400d88f04863b718f4ac518e3f9415198ec2517b8ade13` | 1.575079 | -3.0 | -21.26 | -20.8 | -3.0 | 0.673 | 0.0249 | - |
| `chaosx_oracle_recon_death_03.wav` | chaosx_oracle_recon_death_sfx | shot | exewin4 0.000-0.820 s, placed at 0.000 s; bodyfall_bsb 0.100-1.100 s, placed at 0.500 s, pitch -2 st (rubberband), lowpass 3000 Hz, -4 dB | `a4c0c1bad4e9d23451c33362e6df5fb6815f8c6a18f4a80ad222cc8a1aa0edf3` | `new file` | `a85b07492422d794dbec48f38f7ed944c602abc3f33142dd9e78fa05f678920c` | 1.5 | -3.01 | -21.97 | -22.3 | -3.0 | 0.624 | 0.0 | - |

Every installed file above is pcm_s16le, 44.1 kHz, mono, produced by `.tools/3d_pipeline/audio/master.py batch` (30 Hz high-pass, 8 ms fade-in, 50 ms fade-out, role peak/RMS/loudness gates, source clipping gate, lead silence at most 20 ms). Mastering evidence per file: `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/reports/oracle_recon_all_report.json` and `cuts/*.recipe.json` (ignored working area).

## BLOCKED cues (missing recording)

- `move` barefoot steps: needs a CC0/CC BY barefoot footstep recording, 0.1-0.3 s; none is archived (the archived footsteps are shoes on a subway floor and horse hooves). File unchanged (float32, no source record).
- `idle` breathy chant or whisper (200 Hz-4 kHz) and `observation` chant swell: need a CC0/CC BY vocal-ambience chant or whisper recording, 1-3 s; none is archived (the archived breath is clipped). Files unchanged (float32, no source record).
- `recon` (staff-point cue, 20 ms lead-in) and `select`: no source record exists for the current files, so they cannot be re-edited under the licence rule; files unchanged (float32).
- `death`: installed takes pair a recorded human death vocal (Exewin CC0 takes 6, 11 and 4) with a recorded body fall; a dedicated gasp recording would be closer to the plan.

## Files not changed in this rework

- `chaosx_oracle_recon_idle.wav`, `_move`, `_observation`, `_recon`, `_select`: float32, no source record; see BLOCKED above.

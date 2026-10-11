# Gorilla Heavy Infantry sound attribution

Every installed file is an edited arrangement of recordings that were already archived in this repository with a recorded licence (cut, fade, pitch-shift, EQ, level, layering, mono, 44.1 kHz, PCM16 conversion). No tone, noise bed, synthesized, generated or newly recorded audio is present. No recording was downloaded for this rework.
Licence statements are inherited from the archived source records; derivative licensing was not independently reassessed. CC BY 4.0 material needs the credit line given in the table; CC0 and public-domain items are credited voluntarily.

## Source recordings

| Key | Recording | Creator | Licence | URL | Archived original (repo-relative) | Source SHA-256 | Note |
|---|---|---|---|---|---|---|---|
| bodyfall_bsb | Body Fall #1 | Joseph SARDIN (BigSoundBank) | CC0 1.0 | https://bigsoundbank.com/body-fall-1-s2452.html | `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/audio/recovery_20260912/sources/impact/2452.wav` | `4770f7b32fcab7437c5b1ce79b80df592f3ff76885c49c62fb367d74a4f3430c` |  |
| bodyfall_dirt | BODY FALL - V HVY - DIRT | leonelmail | CC0 1.0 | https://freesound.org/people/leonelmail/sounds/504626/ | `docs/assets/shared_clone_system/models_3d/clone_infantry/audio/closure_20260912/originals/body_fall_504626_hq.mp3` | `336a44d95279173764073a9b2d4d7e12f4167cfb0c1ad5c58e316895e129c6bb` | official HQ preview |
| gbox_step3 | Footsteps (03-footstep.ogg) | GboxMikeFozzy | CC0 1.0 | https://opengameart.org/content/footsteps-0 | `docs/assets/039_murder_mystery/audio/source/03-footstep.ogg` | `9817cc93897ed1de5da87675b26be4196bfda3daa6f1de9dc4398a68d250cdb9` | recorded walking through a subway |
| gbox_step4 | Footsteps (04-footstep.ogg) | GboxMikeFozzy | CC0 1.0 | https://opengameart.org/content/footsteps-0 | `docs/assets/039_murder_mystery/audio/source/04-footstep.ogg` | `b373ff981e44d6f7ba2291225a4803078771029615ed81606136fdb9599906d5` | recorded walking through a subway |
| gbox_step6 | Footsteps (06-footstep.ogg) | GboxMikeFozzy | CC0 1.0 | https://opengameart.org/content/footsteps-0 | `docs/assets/039_murder_mystery/audio/source/06-footstep.ogg` | `39147cc1b98abb4b5378ad07b15d50d18f2aa0f0fd2f5514f078c1e574d14773` | recorded walking through a subway |
| metal_drop | Metal drop thump | stephan (PDSounds) | Public domain dedication | https://commons.wikimedia.org/wiki/File:Metal_drop_thump.ogg | `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/original/metal_drop_thump.ogg` | `b8f5506893d2871c86f5c7e01305bff788dfe156a265e63bb9b00cbbd51647c5` |  |
| thud_metal | Metal Impact Sounds (thud2.wav) | Brian MacIntosh (BMacZero) | CC0 1.0 | https://opengameart.org/content/metal-impact-sounds | `docs/assets/039_murder_mystery/audio/source/thud2.wav` | `5fb5c1b37a95cb6716d0bb529a0b9fe1ae9f3e2228b8f30c5c3dcbb1b570a3af` |  |

## Installed files (11 Oct 2026 rework)

| Runtime file | Soundeffect | Role | Composition from the recordings above | Composite SHA-256 | Before SHA-256 | Installed SHA-256 | Length s | Peak dBFS | RMS dBFS | LUFS | TP dBTP | Loudest 5 ms window s | Head trimmed by master s | Designed contact in file s |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `chaosx_gorilla_heavy_infantry_attack.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | shot | thud_metal 0.000-0.500 s, placed at 0.010 s, pitch -4 st (rubberband); bodyfall_dirt 0.400-1.000 s, placed at 0.000 s, lowpass 450 Hz, -3 dB | `34746151177cfae927cb5a336500c39355b698e44403dd9e2e03c7cd78e7eb0c` | `new file` | `f9320d941edd44fabf5dd803b7d7bdf95c7107d2d6d9b0071a06a18a9c61a361` | 0.62 | -3.0 | -21.33 | -23.3 | -2.9 | 0.045 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_attack_02.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | shot | metal_drop 0.340-1.040 s, placed at 0.000 s, lowpass 900 Hz; thud_metal 0.000-0.500 s, placed at 0.030 s, pitch -7 st (rubberband), lowpass 3000 Hz, -4 dB | `ae79cef38e38d563222c2d593782c27c9d465b9ae9291becd54af93b410f0eb1` | `new file` | `0061fab51dad90c2b527fc80f9625abef047fd34cff0f2274d9f838bb509cef0` | 0.66 | -3.0 | -18.63 | -20.7 | -3.0 | 0.06 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_attack_03.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | shot | bodyfall_bsb 0.160-0.760 s, placed at 0.000 s, lowpass 700 Hz, -2 dB; thud_metal 0.000-0.500 s, placed at 0.030 s, pitch -2 st (rubberband), -2 dB | `4d1d9d39c2d8ca6262c0b1432c95627430cb13216989024f9b3baf84e8ec4c54` | `new file` | `7e6b7beaef9d4425937f1cbd4bc7c7ddcf04e2bd32e0ada71e87a3d442a0f7ab` | 0.6 | -3.0 | -21.71 | -22.8 | -3.0 | 0.06 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_recovery.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | shot | bodyfall_dirt 0.520-0.880 s, placed at 0.000 s, lowpass 380 Hz | `cb8635460988616bc850812f38f079155764631a04b85e68f58aed4e1fd01c5e` | `new file` | `2d00224fd7d57e149d246c899d8f899b6562e043a981f06fda0bd9fcc50f0b27` | 0.36 | -3.0 | -19.46 | -70.0 | -3.0 | 0.085 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_recovery_02.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | shot | bodyfall_bsb 0.800-1.200 s, placed at 0.000 s, lowpass 500 Hz | `318e539e5ae1fca02410b4e13d5725bca00a75a4c0ba5573decccdc7203da423` | `new file` | `567386c3e45a435434fa9ff84b109ac905f1db54a7f3f659076cc5450d9b141f` | 0.4 | -3.0 | -21.32 | -22.4 | -3.0 | 0.055 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_recovery_03.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | shot | bodyfall_dirt 1.100-1.500 s, placed at 0.000 s, lowpass 420 Hz | `a85958adf4cb6af79a877757646aafe0ed3737fb7b916395523eb394f826a6f9` | `new file` | `824a26d0a20ddb70f980e1e8fea679f5cc9919359ce3787a64185f388fa7de2c` | 0.4 | -3.0 | -21.51 | -23.0 | -3.0 | 0.065 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_move.wav` | chaosx_gorilla_heavy_infantry_move_sfx | step | gbox_step4 0.000-0.260 s, placed at 0.000 s, pitch -6 st (tape-rate); bodyfall_dirt 1.100-1.450 s, placed at 0.000 s, lowpass 300 Hz, -4 dB | `d0d3207cd05b0b812aea2777e83d1dcc673434e7097fad71518df4ac4df87635` | `new file` | `c2d3228c21564037ef14f5a86304f718b33e78d62e1b9820bd5f21b4c56ca0bc` | 0.38 | -6.0 | -25.6 | -70.0 | -6.0 | 0.02 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_move_02.wav` | chaosx_gorilla_heavy_infantry_move_sfx | step | gbox_step3 0.000-0.240 s, placed at 0.000 s, pitch -7 st (tape-rate); metal_drop 0.360-0.760 s, placed at 0.000 s, lowpass 250 Hz, -3 dB | `97e9f1918742def450ab211ea1dfd4a6a23898437ea99a65f7fc44e35fb58cc5` | `new file` | `6a3ec3508406b691a8adb68e2035d13ad831194c43ae29672684f825343618ef` | 0.38 | -6.0 | -19.12 | -70.0 | -6.0 | 0.1 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_move_03.wav` | chaosx_gorilla_heavy_infantry_move_sfx | step | gbox_step6 0.000-0.220 s, placed at 0.000 s, pitch -5 st (tape-rate); bodyfall_bsb 0.800-1.150 s, placed at 0.000 s, lowpass 350 Hz, -4 dB | `1a90978d54d69db462079beff344bddfe749167a47ba1ef926ca2692f994386c` | `new file` | `6248fe66fcd83a7ba7c19374221697afc1b531757c8091369c3192b751884aef` | 0.38 | -6.0 | -23.18 | -70.0 | -6.0 | 0.055 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_death.wav` | chaosx_gorilla_heavy_infantry_death_sfx | shot | bodyfall_bsb 0.100-1.100 s, placed at 0.000 s, pitch -3 st (rubberband), lowpass 3000 Hz | `cc6d300c2ab2bbdbb3b232ffbe553fc513951806283ade687fe640d757ec4168` | `new file` | `fc70e43bfdf3c7366ed143ae2cd2b939737698b77a54e9cd212b68cacf6eda61` | 1.0 | -3.0 | -21.92 | -23.8 | -3.0 | 0.125 | 0.0 | - |
| `chaosx_gorilla_heavy_infantry_death_02.wav` | chaosx_gorilla_heavy_infantry_death_sfx | shot | bodyfall_dirt 0.300-1.600 s, placed at 0.000 s, pitch -3 st (rubberband), lowpass 1800 Hz | `88f847a08830fafc30ab359ca46a62ce1777793848885da33e453d9bbba426c7` | `new file` | `fe6a54a3254e22214d5a6910ce6b431b2daffec77b2f2344903cfce9a7029a12` | 1.3 | -3.01 | -21.75 | -22.4 | -3.0 | 0.309 | 0.0 | - |

Every installed file above is pcm_s16le, 44.1 kHz, mono, produced by `.tools/3d_pipeline/audio/master.py batch` (30 Hz high-pass, 8 ms fade-in, 50 ms fade-out, role peak/RMS/loudness gates, source clipping gate, lead silence at most 20 ms). Mastering evidence per file: `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/reports/gorilla_heavy_infantry_all_report.json` and `cuts/*.recipe.json` (ignored working area).

## BLOCKED cues (missing recording)

- `select` (`chaosx_gorilla_heavy_infantry_select.wav`): needs a real gorilla chest-beat (open-hand drumming) or bark, about 0.5-1.5 s, CC0 or CC BY (Wikimedia Commons or Freesound field/zoo recording). The only primate vocal in the archive is the chimpanzee pant-hoot (wrong species), and the archive holds no recorded flesh-on-chest percussion; the file is left as it was.
- `idle` (`chaosx_gorilla_heavy_infantry_idle.wav`): needs a gorilla breathing, rumble or low grunt recording, about 2 s. The only archived breath (primbal, horror breathing) is a human recording whose master source gate reports probable clipped flat tops (3.6 % near-rail samples, 33-sample runs), so it cannot be used; the file is left as it was.
- `death` vocal layer: needs a gorilla scream, roar or groan, about 0.5-1 s. The installed death takes are the recorded heavy body collapse only (closest honest match for the collapse; they carry no vocal).

## Files not changed in this rework

- `chaosx_gorilla_heavy_infantry_select.wav` and `chaosx_gorilla_heavy_infantry_idle.wav` still derive from the chimpanzee pant-hoot (Pawel Fedurek et al., CC BY 4.0) and Metal Clanging Noises (Camshaft64, CC BY-SA 4.0) as stated in the earlier notice below; the per-file source/interval chain is not recorded. Both are BLOCKED above.

## Earlier notice (still applies to the unchanged files named above)


Vocal excerpts: Pawel Fedurek et al., [Pant-hoot call made by a male chimpanzee](https://commons.wikimedia.org/wiki/File:Pant-hoot_call_made_by_a_male_chimpanzee.ogg), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Metal excerpts: Camshaft64, [Metal Clanging Noises](https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Metal derivatives are distributed under CC BY-SA 4.0.
Excerpts were trimmed, loudness-normalized, faded, converted to mono 44.1 kHz, then quantized to PCM16 at unity gain without dither.
Originals, intervals and checksums: docs/assets/012_africa/models_3d/gorilla_heavy_infantry/audio/manifest.md and pcm16_copy_manifest_20260908.json.
These are inherited vocal and equipment sound sources; no species-accurate gorilla recording or footstep recording is claimed.

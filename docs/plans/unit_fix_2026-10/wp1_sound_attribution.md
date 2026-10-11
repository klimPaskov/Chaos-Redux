# WP1 installed sound attribution and handoff

Acceptance basis: the user authorized repair of WP1 using recorded, licensed audio already archived in the repository.
The selected files below use existing recordings, with source/member and output hashes checked before and after runtime copying.
All twelve installed WAVs were reanalysed at their actual runtime paths with the section 3 tools.
No source recording was downloaded, synthesized, or recorded during this pass.

## Sources

- Forest idle: claretcanelon, [Wood Creak](https://freesound.org/people/claretcanelon/sounds/346140/), [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
Original MP3 SHA-256: `63c521d9b6a1c7a32323ea9f6f59cce2f2aed41f5c0b252e21bdbab611d9126a`.
- Plague hoof contacts: D4XX, [Single Horse Galopp](https://freesound.org/people/D4XX/sounds/564628/), and StephenSaldanha, [SRS_Foley_Horse_Galloping](https://freesound.org/people/StephenSaldanha/sounds/165532/), each CC0 according to the archived member credits.
The archived [Horse gallop on different surfaces](https://opengameart.org/content/horse-gallop-on-different-surfaces) collection is by congusbongus under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with mixed per-member licenses.
Only its outdoor ground/grass members are used; their creators and links remain credited here.
Archive SHA-256: `8cafb1ffb6cf17428c32735f2303bd94faa5fe8876eef1d921d2a7d04a84be77`.
Ground member SHA-256: `35b5d4bc7abdfdcc8dde79ddbde48d895f1f6578adea398a1dc7c0450bce919b`.
Grass member SHA-256: `0e0f2d76841a5b8f1af16b37fdbba93a49b7c26abec3671cb0488f1fd4f30db8`.
- Pan death voice: stephan, [Herd of goats bleating](https://commons.wikimedia.org/wiki/File:Herd_of_goats_bleating.ogg), public-domain dedication.
Original OGG SHA-256: `7fadfd47cff33fad6feb71f13d8076b50828919468e2c204bc2b428c9a93280e`.
- Pan body contact: leonelmail, [BODY FALL - V HVY - DIRT](https://freesound.org/people/leonelmail/sounds/504626/), CC0 1.0.
Original MP3 SHA-256: `336a44d95279173764073a9b2d4d7e12f4167cfb0c1ad5c58e316895e129c6bb`.
The clean archived dirt fall supplies the same planned physical component as the named BigSoundBank example; the parent accepted this source choice within the user-authorized pool.
The clipped remaxim/qubodup source is excluded.
- Stone recovery: Work With Sounds / recordist Monika Widzicka, [WWS Quern-stones](https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg), CC BY 4.0.
Original OGG SHA-256: `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7`.

Changes: trim, high-pass/DC removal, fades, level/true-peak correction, resampling, mono conversion and PCM16 conversion using the section 3 master.
The forest loops use only recorded-edge crossfades where required; Pan mixes recorded goat calls with a recorded body fall and uses a 10 ms entry fade.
No tones, noise beds, fake source takes, or generated Foley were added.

## Installed files

| Runtime WAV | Role / source interval in seconds | Duration | Final SHA-256 |
|---|---|---:|---|
| `sound/012_africa/units/forest_giants/chaosx_forest_giants_idle_loop_01.wav` | loop 18.5-21.0 | 2.5 s | `aa0d91e50266bba996154d06d2f3d27b03008230a640bbf3e59a62d629a2fe55` |
| `sound/012_africa/units/forest_giants/chaosx_forest_giants_idle_loop_02.wav` | loop 22.5-25.0 | 2.4 s | `5bbe79902b04bd6c2fa8fb7f99dc6d483dabe4c4bfd2138bb1deffdb5dea53f7` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move.wav` | step 0.0-0.075 | 0.075011 s | `87aabbbf0417eef8f37d8ee81d63a38ee7915f27cc67b873f76a61b1f51d905b` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move_02.wav` | step 0.075-0.155 | 0.050091 s | `90c5dd2db42138d754cdb005bf1c7ee07b4a4c182cf15e385c4a840ee8b3b724` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move_03.wav` | step 0.165-0.25 | 0.075057 s | `8cbe74eea4d2021dc0d414fa493808a5a17bb0be78fb821b6a7335c3f116d0bc` |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move_04.wav` | step 0.145-0.23 | 0.045125 s | `ab0e2f381aac76dcb4f19760f240a0be6186eb975dc0988eff20cb23c6a8fbe9` |
| `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_death.wav` | goat 0.25-0.8; body 0.420-source end, delayed 37339 samples | 2.060408 s | `7314240726e31f04f6b67765b3066c8938b3fe5f0e82a6a5e52f0b409d367c1d` |
| `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_death_02.wav` | goat 3.05-3.6; body 0.420-source end, delayed 37339 samples | 2.060408 s | `baf4be1f00b1792ef59c1121f9fb4f248195277e50ffc1302a3c547c24261d41` |
| `sound/012_africa/units/pan_sappers/chaosx_pan_sappers_death_03.wav` | goat 4.4-4.95; body 0.420-source end, delayed 37339 samples | 2.060408 s | `f31d42bbc9719bc1f351b8d9b2bf40bfd0e67f275e3deb77f519be8592f80afc` |
| `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_collapse_recovery.wav` | shot 5-6.2 | 1.2 s | `7468e87b6fc1a2356a09edd9e40eb664bd072ef3737af92468f445469547a4ef` |
| `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_collapse_recovery_02.wav` | shot 30-31.2 | 1.207438 s | `c9e6ef8b566025dbf61caf03f6ca059186fd3dc99827b15edbd3a1a2799f64f9` |
| `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_collapse_recovery_03.wav` | shot 50-51.2 | 1.2 s | `6b5f151b08bf0144e062b7814e19d9698d159a39fc78cc2e5680a87ceae3634b` |

All files are signed PCM16, 44.1 kHz, mono, with no direct clipped flat tops and at most 20 ms leading silence.
The two forest loops measure -20.8/-20.0 LUFS and -1.0/-1.6 dBTP, with inner-edge RMS differences 1.584/1.211 dB.
The short hoof cues meet the -6 dBFS step peak target; EBU loudness is gated for 45-75 ms clips and is unavailable, rather than a meaningful -70 LUFS reading.
Pan and stone one-shots meet the -3 dBFS peak and -18 +/-4 dBFS RMS bands.

## Consumers and phase

- Forest: `chaosx_forest_giants_idle_loop_sfx` has two different recorded beds, `loop = yes`, `max_audible = 1`, `trigger_once = yes` on idle, and random repetition prevention.
Attack and defend retain their existing one-shot wood cue and WAV.
- Plague: `chaosx_plague_carriers_move_sfx` has four different outdoor hoof contacts and random repetition prevention.
The move/retreat event times are unchanged; exact hoof contacts still require authored/live proof.
- Pan: `chaosx_pan_sappers_death_sfx` has three different goat-call/body-fall takes.
Voice starts with the existing entity event at 0.1000 s; the intended body transient is 0.866689 s into each take, preserving the former 0.9667 s landing phase.
Fresh installed-waveform 10 ms RMS centres place all three body contacts at 0.977834 s in entity time, 11.134 ms from the inherited target.
The previous separate hoof cue on death is removed, so one take carries voice and body contact.
This validates waveform placement and does not prove the anatomical landing in the unchanged animation.
- Stone: `chaosx_stone_cohorts_collapse_recovery_sfx` has three non-overlapping stone-grind takes; existing state/event times and sound range/volume remain unchanged.
It supplies grinding/settling, not the pending rockslide death or thrust impact.

## Evidence and limits

`wp1_evidence/audio_install/manifest.json` records source/cut/output hashes, licenses, commands and protected preimages.
`wp1_evidence/audio_install/installed_verification.json` records fresh destination-byte metrics and resolved consumer samples.
`wp1_evidence/subunit_consumers.json` enumerates all seven formation-to-entity bindings.
The source archives and job cuts stay in the ignored `docs/assets/` working area; this document and the compact proof are the durable handoff.
Selection/order voice routing is distinct from entity-state audio and is not closed by these pools.
Live audio audition, stop-on-transition behavior, planted-frame alignment, and the complete 3D model tickets remain open.
All other unaccepted candidates stay unwired and all genuinely missing recordings are listed in `wp1_africa_audio_needs.md`.

## 11 Oct 2026 rework (audio-only pass)

This pass rebuilt the Africa strange-force cues that had an eligible archived recording from the existing licensed archive only. Nothing was downloaded, synthesized or recorded; every installed WAV is a cut, pitch-shift, EQ, level and layering arrangement of an archived recording, mastered to pcm_s16le 44.1 kHz mono with `.tools/3d_pipeline/audio/master.py batch` (peak, RMS or loudness, clipping, lead silence and true-peak gates all passed).
Each unit's `sound/012_africa/units/<unit>/ATTRIBUTION.md` carries the full source table (title, creator, licence, URL, archived path, source SHA-256), the layer recipe, composite SHA-256, before and after SHA-256, length, peak, RMS, LUFS and true peak per file.
The working files (extracted archive members, composites with `.recipe.json`, allowlists, batch reports, pre-change copies of every replaced runtime WAV) are under the ignored `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/`.
The sound asset gained the numbered variant samples listed below; soundeffect names, volumes, falloffs and every entity event time are unchanged.

### Installed files

#### gorilla_heavy_infantry

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_gorilla_heavy_infantry_attack.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | thud_metal 0.000-0.500 s, @0.010 s, pitch -4st; bodyfall_dirt 0.400-1.000 s, @0.000 s, lowpass 450 Hz, -3 dB | `8680b07b4846a4f12379339fcbe2e65d535283bc519571a2ec87b3bba97c5cd7` | `f9320d941edd44fabf5dd803b7d7bdf95c7107d2d6d9b0071a06a18a9c61a361` | 0.62 | -3.0 | -23.3 |
| `chaosx_gorilla_heavy_infantry_attack_02.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | metal_drop 0.340-1.040 s, @0.000 s, lowpass 900 Hz; thud_metal 0.000-0.500 s, @0.030 s, pitch -7st, lowpass 3000 Hz, -4 dB | `new` | `0061fab51dad90c2b527fc80f9625abef047fd34cff0f2274d9f838bb509cef0` | 0.66 | -3.0 | -20.7 |
| `chaosx_gorilla_heavy_infantry_attack_03.wav` | chaosx_gorilla_heavy_infantry_attack_sfx | bodyfall_bsb 0.160-0.760 s, @0.000 s, lowpass 700 Hz, -2 dB; thud_metal 0.000-0.500 s, @0.030 s, pitch -2st, -2 dB | `new` | `7e6b7beaef9d4425937f1cbd4bc7c7ddcf04e2bd32e0ada71e87a3d442a0f7ab` | 0.6 | -3.0 | -22.8 |
| `chaosx_gorilla_heavy_infantry_recovery.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | bodyfall_dirt 0.520-0.880 s, @0.000 s, lowpass 380 Hz | `5d1766c861562d487c80586784d29b2ed42ef84194dabe1e292245bb2e9da929` | `2d00224fd7d57e149d246c899d8f899b6562e043a981f06fda0bd9fcc50f0b27` | 0.36 | -3.0 | -70.0 |
| `chaosx_gorilla_heavy_infantry_recovery_02.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | bodyfall_bsb 0.800-1.200 s, @0.000 s, lowpass 500 Hz | `new` | `567386c3e45a435434fa9ff84b109ac905f1db54a7f3f659076cc5450d9b141f` | 0.4 | -3.0 | -22.4 |
| `chaosx_gorilla_heavy_infantry_recovery_03.wav` | chaosx_gorilla_heavy_infantry_recovery_sfx | bodyfall_dirt 1.100-1.500 s, @0.000 s, lowpass 420 Hz | `new` | `824a26d0a20ddb70f980e1e8fea679f5cc9919359ce3787a64185f388fa7de2c` | 0.4 | -3.0 | -23.0 |
| `chaosx_gorilla_heavy_infantry_move.wav` | chaosx_gorilla_heavy_infantry_move_sfx | gbox_step4 0.000-0.260 s, @0.000 s, pitch -6st-rate; bodyfall_dirt 1.100-1.450 s, @0.000 s, lowpass 300 Hz, -4 dB | `560ee95a4e1746972cd2c2b8662a90afb866631ae775fa655a3da60cc407d26e` | `c2d3228c21564037ef14f5a86304f718b33e78d62e1b9820bd5f21b4c56ca0bc` | 0.38 | -6.0 | -70.0 |
| `chaosx_gorilla_heavy_infantry_move_02.wav` | chaosx_gorilla_heavy_infantry_move_sfx | gbox_step3 0.000-0.240 s, @0.000 s, pitch -7st-rate; metal_drop 0.360-0.760 s, @0.000 s, lowpass 250 Hz, -3 dB | `new` | `6a3ec3508406b691a8adb68e2035d13ad831194c43ae29672684f825343618ef` | 0.38 | -6.0 | -70.0 |
| `chaosx_gorilla_heavy_infantry_move_03.wav` | chaosx_gorilla_heavy_infantry_move_sfx | gbox_step6 0.000-0.220 s, @0.000 s, pitch -5st-rate; bodyfall_bsb 0.800-1.150 s, @0.000 s, lowpass 350 Hz, -4 dB | `new` | `6248fe66fcd83a7ba7c19374221697afc1b531757c8091369c3192b751884aef` | 0.38 | -6.0 | -70.0 |
| `chaosx_gorilla_heavy_infantry_death.wav` | chaosx_gorilla_heavy_infantry_death_sfx | bodyfall_bsb 0.100-1.100 s, @0.000 s, pitch -3st, lowpass 3000 Hz | `44008b58d83f26c3632299d501a3a801295573acc375bf7015d615529ae885c5` | `fc70e43bfdf3c7366ed143ae2cd2b939737698b77a54e9cd212b68cacf6eda61` | 1.0 | -3.0 | -23.8 |
| `chaosx_gorilla_heavy_infantry_death_02.wav` | chaosx_gorilla_heavy_infantry_death_sfx | bodyfall_dirt 0.300-1.600 s, @0.000 s, pitch -3st, lowpass 1800 Hz | `new` | `fe6a54a3254e22214d5a6910ce6b431b2daffec77b2f2344903cfce9a7029a12` | 1.3 | -3.01 | -22.4 |

#### pan_sappers

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_pan_sappers_sabotage.wav` | chaosx_pan_sappers_sabotage_sfx | spray 1.200-1.370 s, @0.000 s, lowpass 7000 Hz, +9 dB; dynamite 0.030-1.080 s, @0.150 s | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` | `0c070ed2af43e93b694e595465f56b54b4b9282046634bae6b4bb70feb76df02` | 1.2 | -3.0 | -19.7 |
| `chaosx_pan_sappers_sabotage_02.wav` | chaosx_pan_sappers_sabotage_sfx | spray 2.000-2.170 s, @0.000 s, lowpass 7000 Hz, +9 dB; explosion10 0.060-1.060 s, @0.150 s | `new` | `e31c9ffd796496042a408c32ad10dea8f50b35e6663c2bf57f453c1edeef6ac9` | 1.15 | -3.0 | -15.1 |
| `chaosx_pan_sappers_sabotage_03.wav` | chaosx_pan_sappers_sabotage_sfx | spray 3.200-3.370 s, @0.000 s, lowpass 7000 Hz, +9 dB; mech_explosion 0.000-0.950 s, @0.150 s, pitch -2st, lowpass 7000 Hz | `new` | `4a9f949da02fec4cb75ec8dc00ed737534449618bf55bddcd728f5ac8607fb79` | 1.1 | -3.0 | -18.9 |
| `chaosx_pan_sappers_construction.wav` | chaosx_pan_sappers_construction_sfx | shovel 0.000-0.450 s, @0.000 s | `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` | `fcabe9bc89f44b13954b5dd78a09777d1ddac3db1d571e661d57ec8449bc6243` | 0.45 | -3.0 | -18.2 |
| `chaosx_pan_sappers_construction_02.wav` | chaosx_pan_sappers_construction_sfx | shovel 0.000-0.420 s, @0.000 s, pitch -3st | `new` | `e394789f015f498d0f8b3512467bedbbd996fbad9ac0373ca6cfc5bd1faae545` | 0.42 | -3.0 | -18.6 |
| `chaosx_pan_sappers_construction_03.wav` | chaosx_pan_sappers_construction_sfx | shovel 0.000-0.400 s, @0.000 s, pitch +1.5st; door_knock 0.280-0.480 s, @0.140 s, pitch +2st, -9 dB | `new` | `f9ad1c636af6810242c27c651944dc9af211079094a54b49ea03daf1e33464d9` | 0.5 | -3.0 | -19.4 |
| `chaosx_pan_sappers_move.wav` | chaosx_pan_sappers_move_sfx | hoof_muffled 0.000-0.160 s, @0.000 s, pitch +4st | `4a4f7fe38ef2bf21d1aa480bc7a5682834b780054b42c5acb9be50c940148e8d` | `99adfa095e45697b4a34d303667920bbd94ab93e3b933a6518ea2681f14fda26` | 0.16 | -6.0 | -70.0 |
| `chaosx_pan_sappers_move_02.wav` | chaosx_pan_sappers_move_sfx | hoof_muffled 0.200-0.360 s, @0.000 s, pitch +3st | `new` | `d5a528ef57c399d602da2578676cbf8cecb0eddf50dc593b4fb58bb025b05246` | 0.16 | -6.0 | -70.0 |
| `chaosx_pan_sappers_move_03.wav` | chaosx_pan_sappers_move_sfx | hoof_grass 0.000-0.130 s, @0.000 s, pitch +4st, lowpass 7000 Hz | `new` | `0f2ec94d08a0df76d731b2b59947de8ec791fbc6755fc4bb4dc233ad3017aa64` | 0.13 | -6.0 | -70.0 |
| `chaosx_pan_sappers_idle.wav` | chaosx_pan_sappers_idle_sfx | goat 6.850-7.550 s, @0.000 s | `78deabbc26b553fcc9b5d15ec0a61427908bafd3a5bed9c02edd3b831cbfd697` | `e0401f57dfda5a2e1b514ff9436adbf18280c64a509f760bd388a27b40d4a965` | 0.7 | -3.0 | -19.1 |
| `chaosx_pan_sappers_idle_02.wav` | chaosx_pan_sappers_idle_sfx | goat 1.400-2.100 s, @0.000 s | `new` | `a513ec123b73d3200221db861bc4c6f2a9eea67a9bf45ef29dd67e7c1afbc271` | 0.7 | -3.0 | -19.6 |
| `chaosx_pan_sappers_select.wav` | chaosx_pan_sappers_select_sfx | goat 13.450-14.550 s, @0.000 s | `ff66173a723b36b8e6e80550c040f4841bef491d8e49662c597485f0ccac1a19` | `0718cec581e3aeadeb40970b44ca26cd291e39b4bbbf2eba15677d72b151b56e` | 1.1 | -3.0 | -18.1 |
| `chaosx_pan_sappers_select_02.wav` | chaosx_pan_sappers_select_sfx | goat 38.950-40.250 s, @0.000 s | `new` | `9a55145516e309976ec2b7c7f98a46903bd4b0be1b9dc7606c589240b54dab80` | 1.3 | -3.0 | -14.7 |

#### stone_cohorts

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_stone_cohorts_attack.wav` | chaosx_stone_cohorts_attack_sfx | debris_crash 0.140-0.400 s, @0.000 s; thud_metal 0.000-0.340 s, @0.060 s | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` | `ad6d986d9f97470da4bccc5acb0e0efeb98119568c28f8d9214a95c018225c10` | 0.4 | -3.0 | -17.5 |
| `chaosx_stone_cohorts_attack_02.wav` | chaosx_stone_cohorts_attack_sfx | debris_crash 0.320-0.580 s, @0.000 s; thud_metal 0.000-0.340 s, @0.060 s, pitch -4st | `new` | `f3b4b132762a081936d7cc6c1109aca21cd6b0ebfcfe3118cbdcc6dafb2174f7` | 0.4 | -3.0 | -18.6 |
| `chaosx_stone_cohorts_attack_03.wav` | chaosx_stone_cohorts_attack_sfx | debris_crash 0.480-0.740 s, @0.000 s; thud_metal 0.000-0.340 s, @0.060 s, pitch -2st, lowpass 3000 Hz; metal_drop 0.340-0.740 s, @0.050 s, lowpass 800 Hz, -8 dB | `new` | `31798c9799a83ac83497c0a74e52d53ed61c4896ea210b4b8ec2bdce73b6f2a3` | 0.42 | -3.0 | -17.9 |
| `chaosx_stone_cohorts_death.wav` | chaosx_stone_cohorts_death_sfx | debris_crash 0.000-2.400 s, @0.000 s, pitch -2st; quern 12.000-13.900 s, @0.500 s, highpass 80 Hz, -3 dB | `7ffbe2820f00621a1db3743edc6518b7f71f65da8b2e19906ea5e7f504c1d842` | `77dd76f2f93b65d496ad88a4e06a48eda91d2a5f3e9d71c7ace6952e78b8ce1e` | 2.4 | -3.0 | -21.4 |
| `chaosx_stone_cohorts_death_02.wav` | chaosx_stone_cohorts_death_sfx | debris_crash 0.600-2.400 s, @0.000 s; dynamite 1.700-3.700 s, @0.200 s, lowpass 2500 Hz, -5 dB | `new` | `3c58304aada1fe860b7d005d339bdcd9e835d5ad4f46ed7faada97e07d8d8269` | 2.2 | -3.0 | -21.2 |
| `chaosx_stone_cohorts_move.wav` | chaosx_stone_cohorts_move_sfx | quern 8.620-8.980 s, @0.000 s | `9ecc737021ea144c452786879909f98ab422d62d6312468a8c8ab7401b810743` | `3f03fd6691196c5aa669e2a777675f065ab352fc92099d670ba430bd6674f65b` | 0.36 | -6.0 | -70.0 |
| `chaosx_stone_cohorts_move_02.wav` | chaosx_stone_cohorts_move_sfx | quern 20.380-20.740 s, @0.000 s | `new` | `2dd0fe0f31fa3fdab1f83ca18d363734b84033178d29f57a6c04d9c9a952109a` | 0.36 | -6.0 | -70.0 |
| `chaosx_stone_cohorts_move_03.wav` | chaosx_stone_cohorts_move_sfx | quern 40.820-41.180 s, @0.000 s | `new` | `aec7178d74ad7690770a0d58ed45dc3235e445549aa977c5b8e03f6a11cc196a` | 0.36 | -6.0 | -70.0 |
| `chaosx_stone_cohorts_idle.wav` | chaosx_stone_cohorts_idle_sfx | quern 12.000-14.200 s, @0.000 s | `729f14dede6b178678544bbd880a5c71498393f034c1c6684ef3c778cb5d4e49` | `9220b9d264d769f22d6ba90c4dccb3d83758c97044caf4e9f6f065410219eafb` | 2.2 | -3.0 | -19.4 |
| `chaosx_stone_cohorts_idle_02.wav` | chaosx_stone_cohorts_idle_sfx | quern 33.000-35.200 s, @0.000 s | `new` | `cf698a3785660572992d37263374bb6aa4eb49a577521f25e89f7d561e23e001` | 2.2 | -3.0 | -19.1 |
| `chaosx_stone_cohorts_select.wav` | chaosx_stone_cohorts_select_sfx | quern 20.300-21.700 s, @0.000 s | `9e57db53e3f6b73f099d72c54f2d461207765941ccfc76b840d85668023251eb` | `77e7a66062cbca10b1b60f115d5dec10871a54b6c44e274585f4198ae64230b2` | 1.4 | -3.0 | -17.7 |
| `chaosx_stone_cohorts_select_02.wav` | chaosx_stone_cohorts_select_sfx | quern 40.700-42.100 s, @0.000 s | `new` | `e52210257afa83ec6924f95bd4fc8d26d22f1bf81909356bbf19808e84177975` | 1.4 | -3.0 | -18.1 |

#### riverborn

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_riverborn_attack.wav` | chaosx_riverborn_attack_sfx | swosh22 0.000-0.320 s, @0.250 s; bodyfall_dirt 0.400-0.950 s, @0.360 s, pitch +2st, lowpass 900 Hz, -2 dB | `26ffe43934ac355da6df6887968b061ad54bef41a80bbe7d2bc69f506351d994` | `c887027575df4a5d0cbd763c57b947f510fe554f1465783b7814941db4fa28af` | 0.605578 | -3.01 | -23.5 |
| `chaosx_riverborn_attack_02.wav` | chaosx_riverborn_attack_sfx | swosh16 0.000-0.440 s, @0.230 s; bodyfall_bsb 0.160-0.710 s, @0.340 s, pitch +1st, lowpass 1100 Hz, -2 dB | `new` | `f218558eb9fa7e7532511fe12f643ba6e844bb5c8dae1f870283d08627e17ad5` | 0.630522 | -3.0 | -23.3 |
| `chaosx_riverborn_attack_03.wav` | chaosx_riverborn_attack_sfx | swosh20 0.000-0.450 s, @0.220 s; bodyfall_dirt 0.520-1.070 s, @0.360 s, pitch +3st, lowpass 800 Hz, -2 dB | `new` | `37ed6818b350943199f2bdd4cba4f8ac2f1fca1532e4cfb73ad7e1be18966759` | 0.640499 | -3.02 | -23.1 |

#### forest_giants

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_forest_giants_attack.wav` | chaosx_forest_giants_attack_sfx | swosh29 0.083-0.683 s, @0.000 s, pitch -6st-rate; axe 1.790-2.190 s, @0.440 s, pitch -5st; bodyfall_dirt 0.400-1.000 s, @0.460 s, lowpass 420 Hz, -3 dB | `3c2248e6583eb5d0aacf392c8cf300f38b7914f3ffa0a01a3fe16169993771fb` | `fd36c0632fccd05075d4f9a4f179fdcc9dabd2185886ab981eabfc9f9a493bfe` | 1.1 | -3.0 | -19.6 |
| `chaosx_forest_giants_attack_02.wav` | chaosx_forest_giants_attack_sfx | swosh30 0.025-0.575 s, @0.000 s, pitch -5st-rate; axe 3.370-3.770 s, @0.440 s, pitch -6st; bodyfall_bsb 0.160-0.760 s, @0.440 s, lowpass 500 Hz, -3 dB | `new` | `f7133418605ad471bf71555357fdaffbf5c905b8ca78de538eb8da2f78a5c0b4` | 1.05 | -3.0 | -20.6 |
| `chaosx_forest_giants_attack_03.wav` | chaosx_forest_giants_attack_sfx | swosh35 0.286-0.836 s, @0.000 s, pitch -4st-rate; axe 4.390-4.790 s, @0.440 s, pitch -4st; bodyfall_dirt 0.400-1.000 s, @0.460 s, pitch -2st, lowpass 600 Hz, -4 dB | `new` | `65733d0ac82016723badb07d2bed70f0aea9f523719461f37ea30f318f866b91` | 1.1 | -3.0 | -20.2 |
| `chaosx_forest_giants_concealment_emergence.wav` | chaosx_forest_giants_concealment_emergence_sfx | wood_creak 12.250-13.350 s, @0.000 s, highpass 60 Hz, +18 dB; forest_amb 66.600-68.300 s, @0.000 s, -2 dB | `e9ff401c221333d7e1263105706e612caf0410500a5ae47535d9c27654fd98d8` | `bd4fc83f6917733f512fbb35d6400729cc11b75d3c375ae1b06969f418587563` | 1.7 | -3.0 | -14.8 |
| `chaosx_forest_giants_concealment_emergence_02.wav` | chaosx_forest_giants_concealment_emergence_sfx | wood_creak 10.800-11.900 s, @0.100 s, highpass 60 Hz, +18 dB; forest_amb 59.300-60.900 s, @0.000 s, -2 dB | `new` | `3fbaf1b191ce4652db6eefed58a2eb60f1546207029fce1cd99e4477d97bbd99` | 1.6 | -3.0 | -16.7 |

#### oracle_recon

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_oracle_recon_death.wav` | chaosx_oracle_recon_death_sfx | exewin6 0.000-1.200 s, @0.000 s; bodyfall_bsb 0.100-1.100 s, @0.620 s, lowpass 3500 Hz, -4 dB | `184cb87973ec4933bdb6e4341b13a4f9823c8193c8a08bb32a904692537e2256` | `639885dd4eb62ab07f5ebbb4442678df6c5cc3c42b3064125dc2795c6fcdfa4a` | 1.535057 | -3.0 | -21.9 |
| `chaosx_oracle_recon_death_02.wav` | chaosx_oracle_recon_death_sfx | exewin11 0.000-0.940 s, @0.000 s; bodyfall_dirt 0.300-1.300 s, @0.550 s, pitch -1st, lowpass 2500 Hz, -4 dB | `new` | `b4fa9d1f53c2890e10400d88f04863b718f4ac518e3f9415198ec2517b8ade13` | 1.575079 | -3.0 | -20.8 |
| `chaosx_oracle_recon_death_03.wav` | chaosx_oracle_recon_death_sfx | exewin4 0.000-0.820 s, @0.000 s; bodyfall_bsb 0.100-1.100 s, @0.500 s, pitch -2st, lowpass 3000 Hz, -4 dB | `new` | `a85b07492422d794dbec48f38f7ed944c602abc3f33142dd9e78fa05f678920c` | 1.5 | -3.01 | -22.3 |

#### plague_carriers

| Runtime file | Soundeffect | Composition | Before SHA-256 | After SHA-256 | Length s | Peak dBFS | LUFS |
|---|---|---|---|---|---:|---:|---:|
| `chaosx_plague_carriers_idle.wav` | chaosx_plague_carriers_idle_sfx | plague_idle_pre 0.410-0.770 s, @0.000 s | `2da96b2e1e550ba11f68a48f3b81277ce99c03201092de513bcbf85773cf6a76` | `6b0ee2fb8ef22ccdbe917337ae53615b44899e477f2232f45fe673e01e35cdbc` | 0.36 | -3.0 | -70.0 |
| `chaosx_plague_carriers_idle_02.wav` | chaosx_plague_carriers_idle_sfx | plague_idle_pre 0.410-0.770 s, @0.000 s, pitch -2st | `new` | `be0dda5531ca893098c6a702a38fcf6bd4fe5409685db4c485d1f649cb691986` | 0.36 | -3.0 | -70.0 |
| `chaosx_plague_carriers_idle_03.wav` | chaosx_plague_carriers_idle_sfx | plague_idle_pre 0.410-0.770 s, @0.000 s, pitch +2st | `new` | `c79f36f344247ee6b15c44eb4f4f6af45d74f327a84e2cc260484beeae84a7ab` | 0.36 | -3.0 | -70.0 |
| `chaosx_plague_carriers_death.wav` | chaosx_plague_carriers_death_sfx | plague_death_pre 0.000-1.120 s, @0.000 s | `0ff9c42a208e9cd4f536e935c2d9b4268fe6d2811f22bd85bd76388b85df65f4` | `281733bcc6ed29f07c9e5a4b3ca41c14fa71f40d4c56be43982dd769fe0956cc` | 1.12 | -3.0 | -21.3 |
| `chaosx_plague_carriers_death_02.wav` | chaosx_plague_carriers_death_sfx | plague_death_pre 0.000-1.120 s, @0.000 s, pitch -2st | `new` | `03dd401df3820f610ef5a7a507311f6b93d944240d5bb4f1eb8c5da300addacb` | 1.12 | -3.0 | -21.2 |
| `chaosx_plague_carriers_death_03.wav` | chaosx_plague_carriers_death_sfx | plague_death_pre 0.000-1.120 s, @0.000 s, pitch +1.5st | `new` | `14795a95e164e012aae64cd52e4e149462a2aea9e3cfa2f5e95b978afb5584a2` | 1.12 | -3.0 | -21.2 |

### Sample counts per soundeffect and timing data for the entity retiming

| Soundeffect | Samples in the effect now | Timing of the strongest event in each new or replaced take |
|---|---:|---|
| chaosx_gorilla_heavy_infantry_attack_sfx | 3 | gorilla_heavy_infantry_attack: loudest 5 ms window 0.04 s; gorilla_heavy_infantry_attack_02: loudest 5 ms window 0.06 s; gorilla_heavy_infantry_attack_03: loudest 5 ms window 0.06 s |
| chaosx_gorilla_heavy_infantry_recovery_sfx | 3 | gorilla_heavy_infantry_recovery: loudest 5 ms window 0.09 s; gorilla_heavy_infantry_recovery_02: loudest 5 ms window 0.06 s; gorilla_heavy_infantry_recovery_03: loudest 5 ms window 0.07 s |
| chaosx_gorilla_heavy_infantry_move_sfx | 3 | - |
| chaosx_gorilla_heavy_infantry_death_sfx | 2 | gorilla_heavy_infantry_death: loudest 5 ms window 0.12 s; gorilla_heavy_infantry_death_02: loudest 5 ms window 0.31 s |
| chaosx_pan_sappers_sabotage_sfx | 3 | pan_sappers_sabotage: loudest 5 ms window 0.23 s; pan_sappers_sabotage_02: loudest 5 ms window 0.20 s; pan_sappers_sabotage_03: loudest 5 ms window 0.17 s |
| chaosx_pan_sappers_construction_sfx | 3 | pan_sappers_construction: loudest 5 ms window 0.03 s; pan_sappers_construction_02: loudest 5 ms window 0.04 s; pan_sappers_construction_03: loudest 5 ms window 0.18 s |
| chaosx_pan_sappers_move_sfx | 3 | - |
| chaosx_pan_sappers_idle_sfx | 2 | pan_sappers_idle: loudest 5 ms window 0.38 s; pan_sappers_idle_02: loudest 5 ms window 0.45 s |
| chaosx_pan_sappers_select_sfx | 2 | pan_sappers_select: loudest 5 ms window 0.39 s; pan_sappers_select_02: loudest 5 ms window 0.74 s |
| chaosx_stone_cohorts_attack_sfx | 3 | stone_cohorts_attack: loudest 5 ms window 0.10 s; stone_cohorts_attack_02: loudest 5 ms window 0.11 s; stone_cohorts_attack_03: loudest 5 ms window 0.10 s |
| chaosx_stone_cohorts_death_sfx | 2 | - |
| chaosx_stone_cohorts_move_sfx | 3 | - |
| chaosx_stone_cohorts_idle_sfx | 2 | - |
| chaosx_stone_cohorts_select_sfx | 2 | stone_cohorts_select: loudest 5 ms window 0.34 s; stone_cohorts_select_02: loudest 5 ms window 0.26 s |
| chaosx_riverborn_attack_sfx | 3 | riverborn_attack: thrust lands about 0.16 s, loudest window 0.08 s; riverborn_attack_02: thrust lands about 0.18 s, loudest window 0.18 s; riverborn_attack_03: thrust lands about 0.19 s, loudest window 0.07 s |
| chaosx_forest_giants_attack_sfx | 3 | forest_giants_attack: loudest 5 ms window 0.44 s; forest_giants_attack_02: loudest 5 ms window 0.43 s; forest_giants_attack_03: loudest 5 ms window 0.41 s |
| chaosx_forest_giants_concealment_emergence_sfx | 2 | - |
| chaosx_oracle_recon_death_sfx | 3 | - |
| chaosx_plague_carriers_idle_sfx | 3 | plague_carriers_idle: loudest 5 ms window 0.06 s; plague_carriers_idle_02: loudest 5 ms window 0.07 s; plague_carriers_idle_03: loudest 5 ms window 0.06 s |
| chaosx_plague_carriers_death_sfx | 3 | plague_carriers_death: loudest 5 ms window 0.03 s; plague_carriers_death_02: loudest 5 ms window 0.03 s; plague_carriers_death_03: loudest 5 ms window 0.02 s |

Forest giant blows contain a short whoosh lead-in and land at about 0.41-0.44 s into each take, so the entity event for the 1.60 s and 2.53 s contacts must be set about 0.43 s earlier than the contact frame.
Pan sabotage takes carry a 0.15 s hiss and the blast begins at about 0.18 s; gorilla attack takes land at 0.04-0.06 s; stone attack takes strike at about 0.10 s; riverborn thrusts land at about 0.16-0.19 s.

### Still BLOCKED (exact missing recording)

#### gorilla_heavy_infantry
- `select` (`chaosx_gorilla_heavy_infantry_select.wav`): needs a real gorilla chest-beat (open-hand drumming) or bark, about 0.5-1.5 s, CC0 or CC BY (Wikimedia Commons or Freesound field/zoo recording). The only primate vocal in the archive is the chimpanzee pant-hoot (wrong species), and the archive holds no recorded flesh-on-chest percussion; the file is left as it was.
- `idle` (`chaosx_gorilla_heavy_infantry_idle.wav`): needs a gorilla breathing, rumble or low grunt recording, about 2 s. The only archived breath (primbal, horror breathing) is a human recording whose master source gate reports probable clipped flat tops (3.6 % near-rail samples, 33-sample runs), so it cannot be used; the file is left as it was.
- `death` vocal layer: needs a gorilla scream, roar or groan, about 0.5-1 s. The installed death takes are the recorded heavy body collapse only (closest honest match for the collapse; they carry no vocal).

#### pan_sappers
- `construction` tool clatter and wire tick: needs a CC0 workshop-pack recording (hammer or wrench on metal, wire twang or ratchet tick), about 0.2-0.6 s. The installed takes are the recorded shovel-in-dirt contact (digging suits sappers) and, in take 3, a recorded metal door-knocker clack; this is the closest archived match, not a tool-clatter pack.
- `move` goat/deer hoof on dirt: needs a goat or deer hoof recording, 0.1-0.3 s. The installed steps are the archived horse-hoof recordings (muffled trot and grass) pitched up 3-4 semitones toward goat size.
- `idle` breath and cloth rustle: needs a CC0 cloth-rustle recording; the archived breath is clipped (see gorilla). The installed idle takes are quiet bleats from the public-domain goat recording.
- `sabotage` fuse hiss: needs a burning-fuse recording; the 0.15 s lead hiss is the CC0 aerosol Spray recording (closest archived broadband hiss). The blasts are three different recorded explosions.

#### stone_cohorts
- `attack` rock-impact pack: needs three clean CC0 stone-on-stone or stone-on-iron single impacts, 0.3-0.5 s. The installed takes combine one recorded hit out of the CC0 tile/stone/metal debris crash with the recorded metal thud (closest archived match; the debris recording is a crash, not an isolated rock strike).
- `death` rockslide: needs a PD/CC0 rockslide or large rock-fall recording, 1-3 s. Take 1 layers the debris crash with the CC BY quern grind; take 2 layers the crash with the tail of the CC0 rock-blast recording.
- `collapse_recovery` settling-stone rumble from the rockslide source: unchanged (three quern-grind takes installed earlier); needs the same rockslide recording.

#### riverborn
- `attack` wet impact: needs a CC0 wet thud or slap impact pack, 0.2-0.5 s. The installed takes are a recorded bamboo-staff whoosh plus a dry recorded ground/body thump; the wet character is missing.
- `move` wet bare-foot steps: needs a CC0 wet footstep recording, 0.1-0.3 s; none is archived. File unchanged (float32, no source record).
- `idle`, `water_transition`: need a water-flow or splash recording (the earlier Flowing-water-100019 and Ducks-landing originals are no longer in the archive). Files unchanged (float32, no source record).
- `select` 5 ms fade-in and `death`: the current files have no source record, so they cannot be re-edited under the licence rule; files unchanged (float32).

#### forest_giants
- `death` trunk crack and tree crash: needs a CC0 tree-fall recording, 1-3 s; none is archived. File unchanged (derived from the CC0 Wood Creak recording).
- `emergence` roots tearing: needs a root-tearing recording; the installed takes use the CC0 wood-creak recording as the tearing stand-in under a public-domain leaf-rustle bed.
- `attack` is built as whoosh plus wood strike plus ground thump from CC0/PD recordings (bamboo-staff whoosh pitched down, axe-on-wood strike pitched down, heavy ground thump); a larger single heavy-wood recording would still be better.

#### oracle_recon
- `move` barefoot steps: needs a CC0/CC BY barefoot footstep recording, 0.1-0.3 s; none is archived (the archived footsteps are shoes on a subway floor and horse hooves). File unchanged (float32, no source record).
- `idle` breathy chant or whisper (200 Hz-4 kHz) and `observation` chant swell: need a CC0/CC BY vocal-ambience chant or whisper recording, 1-3 s; none is archived (the archived breath is clipped). Files unchanged (float32, no source record).
- `recon` (staff-point cue, 20 ms lead-in) and `select`: no source record exists for the current files, so they cannot be re-edited under the licence rule; files unchanged (float32).
- `death`: installed takes pair a recorded human death vocal (Exewin CC0 takes 6, 11 and 4) with a recorded body fall; a dedicated gasp recording would be closer to the plan.

#### plague_carriers
- `bray` at frame 12: needs a CC0/CC BY donkey bray recording, 0.4-1 s, 2-3 takes (Freesound or Wikimedia Commons); no donkey vocal is archived, so no bray was installed and no soundeffect was created.
- `idle`/`death` donkey vocal: the installed takes are tail-trimmed and pitch-varied (-2/0/+2 and -2/0/+1.5 semitones) versions of the existing cough-derived derivatives; a donkey-appropriate idle and death vocal remains missing.

### Unchanged float32 runtime files with no source record

These ten files are still `pcm_f32le` and have no recorded source or licence, so they were not re-edited: `oracle_recon` idle, move, observation, recon, select; `riverborn` idle, move, select, death, water_transition. Converting them to pcm_s16le is a one-line `ffmpeg -ar 44100 -ac 1 -c:a pcm_s16le` step once their sources are identified or replaced.

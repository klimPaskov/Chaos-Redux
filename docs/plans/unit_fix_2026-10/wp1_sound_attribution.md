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

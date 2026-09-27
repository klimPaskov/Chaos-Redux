# Zombie shared sound package

The base `zombies` battalion uses the rebuilt `chaosx_zombies` sprite: `gfx/entities/chaosx_zombies.asset` defines `chaosx_zombies_entity` on the `chaosx_zombies_mesh` registered in `gfx/entities/chaosx_zombies.gfx`.
`wendigo_zombies` still uses the vanilla `infantry` sprite.
Model production evidence lives under `docs/assets/002_zombie_outbreak/models_3d/zombies/`, and the rebuild handoff is `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/2026-09-27_base_zombie_rebuild_runtime.md`.

## Base zombie voices and impacts

`sound/chaosx_base_zombie_sound.asset` defines the base entity's own soundeffects and registers them in the `Effects` category.
Runtime files live in `sound/002_zombie_outbreak/zombies/base/`, and `ATTRIBUTION.txt` there carries the required notices.

| Soundeffect | Runtime file | Source and licence |
|---|---|---|
| `chaosx_base_zombie_attack_growl` | `base_zombie_attack_growl.wav` | “ZombiePackSFX 2” by Colodical, `zombieattack2sfx.wav`, CC BY 3.0 |
| `chaosx_base_zombie_lunge` | `base_zombie_lunge.wav` | ZombiePackSFX 2, `zombielungesfx.wav`, CC BY 3.0 |
| `chaosx_base_zombie_eating` | `base_zombie_eating.wav` | ZombiePackSFX 2, `zombieeatingsfx.wav`, CC BY 3.0 |
| `chaosx_base_zombie_defeated` | `base_zombie_defeated.wav` | ZombiePackSFX 2, `zombiedefeated2sfx.wav`, CC BY 3.0 |
| `chaosx_base_zombie_body_fall` | `base_zombie_body_fall.wav` | “Falling body” by remaxim, CC BY-SA 3.0; the page describes a dead zombie body hitting the ground |
| `chaosx_base_zombie_grab_contact` | `base_zombie_grab_contact.wav` | `punch_1` from “Rpg Sound Effect Pack” by Delta12 Studio, CC0 |

Each runtime file was converted to mono 44.1 kHz signed 16-bit PCM, trimmed from 5 ms before the −40 dB onset to 20 ms after the −50 dB tail, given 5 ms and 30 ms fades, and peak-normalised to −3 dBFS.
`audio_sources/runtime_base_receipts_20260927.json` records each source hash, trim window, gain, and runtime hash.
The punch recording is very quiet at source and needed +32 dB; its tail still decays cleanly to −52 dB, and it plays at volume 0.4.

The source pages, archives, and review copies are recorded in `audio_sources/source_acquisition_20260925.md` and `audio_sources/source_acquisition_20260926.md`.
The ZombiePackSFX 2 `brains`, `idle`, and `sniffing` clips and the anonymous 24-file artisticdude pack have no runtime role.

## Base entity synchronisation

The actions run at 30 FPS, and every event time is `(frame − 1) / 30` at a phase measured on the final exported actions.

| State | Events |
|---|---|
| `attack` (loops) | growl 1.00 s; grab contact 1.60 s and 2.47 s at the reach peaks of frames 49 and 75 |
| `support_attack` (loops) | lunge 0.50 s; contact 0.77 s and 1.77 s at the jaw closes of frames 24 and 54 |
| `defend` (looping) | shared idle moan once; contact 0.87 s at the frame 27 counter-deflect |
| `move` (looping) | shared footstep at 0.53, 0.90, 1.23, and 1.50 s (plants at frames 17, 28, 39, 46) |
| `retreat` (looping) | shared footstep at 0.33, 0.50, and 0.97 s (plants at frames 11, 16, 30) |
| `training` (looping) | growl 1.00 s before the frame 38 swipe; lunge 3.40 s before the frame 111 lunge; eating 4.33 s as feeding begins at frame 131 |
| `death` | vanilla `blood_particle` at the `Head` bone and the defeated cry at 0.23 s (frame 8 hit); body fall 1.73 s (frame 53 impact) |
| `idle` (looping) | shared idle moan once |

## Shared package

The shared package in `sound/chaosx_zombies_sound.asset` is consumed by the specialized zombie entities, by the base entity's idle, defend, move, and retreat states, and by the `ZZZ_infantry_idle` country selection voice.
It defines 15 retained WAV files: three idle moans, six footsteps, three attacks, and three deaths.
The specialized entities consume the generic `chaosx_zombie_attack` and `chaosx_zombie_death` effects.

The three idle sounds come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, labeled CC0.
The footsteps come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, labeled CC0.
The original source archive for the idle sounds was recorded as `https://opengameart.org/sites/default/files/zombienoises.zip` with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.
The older three attack and three death WAVs remain for specialized consumers; five of those six still lack a durable per-file source-to-runtime mapping, so their provenance remains unresolved.

## Validation limits

No listening tool was available, so audible quality, loudness balance against vanilla infantry, and perceived sync rest on waveform measurement and the source role labels.
Selection audio stays with the country-level `ZZZ_infantry_idle` voice, because HOI4 exposes no per-subunit selection binding.

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

The base zombie is an undead infantryman in a rotting field uniform, rebuilt from the ZZZ leader portraits.
The actions run at 30 FPS, and every event time is `(frame − first frame) / 30` at a phase measured on the final exported actions with `.tools/3d_pipeline/review/review_cli.py actions --humanoid`.

| State | Events |
|---|---|
| `attack` (loops) | growl 0.33 s; grab contact 0.70, 1.43, and 2.37 s at the reach peaks of frames 24, 46, and 74 |
| `support_attack` (loops) | lunge 0.60 s; contact 1.20 and 2.00 s at the grab (frame 39) and pull-in (frame 63); eating 2.23 s as the bite tears from frame 70 |
| `defend` (looping) | shared idle moan once; contact 0.43 s at the frame 14 recoil |
| `move` (looping) | shared footstep at 0.60, 1.40, 2.13, 3.07, 3.83, and 4.77 s (mummy-stagger plants) |
| `retreat` (looping) | shared footstep at 0.17, 0.40, and 1.13 s (plants at frames 6, 13, 35) |
| `training` (looping) | growl 0.40 s leading the frame 27 scream |
| `death` | vanilla `blood_particle` at the `Head` bone and the defeated cry at 0.10 s; body fall 2.13 s (frame 65 impact) |
| `idle` (looping) | shared idle moan once |

## Variant voices

`sound/chaosx_zombie_variant_sounds.asset` gives each variant its own voice family from the CC0 [Zombies Sound Pack](https://opengameart.org/content/zombies-sound-pack) by artisticdude.
The 24 numbered clips were classified by a listening review (Gemini audio judge) into roles and characters, then grouped so no clip is shared between variants:

| Variant | Effects | Clips |
|---|---|---|
| Demonic | `chaosx_demonic_zombie_attack`, `chaosx_demonic_zombie_scream` | 14, 13; 9 |
| Infected | `chaosx_infected_zombie_attack`, `chaosx_infected_zombie_pain` | 10, 23; 11 |
| Mutant | `chaosx_mutant_zombie_attack`, `chaosx_mutant_zombie_roar` | 4, 7; 12 |
| Necrotic | `chaosx_necrotic_zombie_rattle` | 15, 17, 20 |
| Parasitic | `chaosx_parasitic_zombie_gurgle`, `chaosx_parasitic_zombie_feed` | 18, 21; 19 |
| Rabid | `chaosx_rabid_zombie_attack` | 5, 6, 8 |
| Undead | `chaosx_undead_zombie_grunt`, `chaosx_undead_zombie_pain`, `chaosx_undead_zombie_moan` | 1, 2, 3; 22, 24; 16 |

The package is built by `.tools/3d_pipeline/review/sound_pack.py` from `docs/assets/002_zombie_outbreak/models_3d/zombie_variant_sound_spec.json`; `zombie_variant_sound_receipts.json` beside it records every source hash, trim window, gain, and runtime hash.
Each variant entity times these voices, the shared footsteps, the base contact and body-fall impacts, and the vanilla `blood_particle` to phases measured on its own exported actions.

## Shared package

The shared package in `sound/chaosx_zombies_sound.asset` keeps three idle moans and six footsteps: the variants and the base zombie use the footstep effect, several use the idle moan, and `ZZZ_infantry_idle` uses the moans as the country selection voice.
The three idle sounds come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, labeled CC0.
The footsteps come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, labeled CC0.
The original source archive for the idle sounds was recorded as `https://opengameart.org/sites/default/files/zombienoises.zip` with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.
The older shared attack and death effects, whose WAVs mostly lacked a source-to-runtime mapping, had no consumer after the variant rebuild and were removed with their files.

## Validation limits

No listening tool was available, so audible quality, loudness balance against vanilla infantry, and perceived sync rest on waveform measurement and the source role labels.
Selection audio stays with the country-level `ZZZ_infantry_idle` voice, because HOI4 exposes no per-subunit selection binding.

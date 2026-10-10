# WP2 to WP6: Event 014 audio delivery for bone_guard, siege_eaters and march_predation_column

WP2 owns every `sound/014_cannibalism/units/*/*.wav`, `sound/014_cannibalism_units_sound.asset` and `sound/014_cannibalism_voices.asset`. The files below are installed and registered; WP6 places the entity `state` events for its three units in `gfx/entities/014_cannibalism_units.asset` and must not edit the sound assets or WAVs.

Every cue is pcm_s16le, 44.1 kHz, mono, mastered through the shared `.tools/3d_pipeline/audio/master.py` recipe (30 Hz high-pass, lead trimmed to a 10 ms pre-roll, 8 ms fade-in, 50 ms fade-out, bounded limiter, EBU loudnorm, role peak guard: one-shots -3 dBFS, footsteps -6 dBFS, true peak at or below -1 dBTP). The transient sits at 10 ms, so `event time = contact time`.

Full provenance, take windows, SHA-256 values and measurements: `docs/plans/unit_fix_2026-10/wp2_evidence/audio/batch_report.json` and `ATTRIBUTION.md`; the batch tool and spec are `.tools/3d_pipeline/audio/cannibal_batch.py` and `wp2_evidence/audio/cannibal_batch_spec.json`.

## Soundeffect wiring (unchanged identifiers, more takes)

| soundeffect | samples (prevent_random_repetition = yes) | role / placement |
|---|---|---|
| `cannibal_bone_guard_death_sfx` | `cannibal_bone_guard_death.wav`, `cannibal_bone_guard_death_02.wav` | one-shot at the collapse impact frame of the death action |
| `cannibal_bone_guard_movement_sfx` | `cannibal_bone_guard_movement.wav`, `cannibal_bone_guard_movement_02.wav` | one event per measured foot plant in move and retreat (alternates automatically) |
| `cannibal_bone_guard_training_sfx` | `cannibal_bone_guard_training.wav` | one-shot at the exertion peak of the training action |
| `cannibal_bone_guard_weapon_attack_sfx` | `cannibal_bone_guard_weapon_attack.wav`, `cannibal_bone_guard_weapon_attack_02.wav` | swish at the wind-up/acceleration frame of each strike |
| `cannibal_bone_guard_weapon_impact_sfx` | `cannibal_bone_guard_weapon_impact.wav` (unchanged shared-batch master) | impact at the measured strike frame |
| `cannibal_bone_guard_idle_vocal_sfx` | `cannibal_bone_guard_idle_vocal.wav` (trimmed to the voiced part) | trigger_once on idle entry as today |
| `cannibal_bone_guard_selection_sfx` | `cannibal_bone_guard_selection.wav` (trimmed to the voiced part) | selection, not an entity state |
| `cannibal_siege_eaters_death_sfx` | `cannibal_siege_eaters_death.wav`, `cannibal_siege_eaters_death_02.wav` | one-shot at the collapse impact frame of the death action |
| `cannibal_siege_eaters_movement_sfx` | `cannibal_siege_eaters_movement.wav`, `cannibal_siege_eaters_movement_02.wav` | one event per measured foot plant in move and retreat (alternates automatically) |
| `cannibal_siege_eaters_training_sfx` | `cannibal_siege_eaters_training.wav` | one-shot at the exertion peak of the training action |
| `cannibal_siege_eaters_weapon_attack_sfx` | `cannibal_siege_eaters_weapon_attack.wav`, `cannibal_siege_eaters_weapon_attack_02.wav` | swish at the wind-up/acceleration frame of each strike |
| `cannibal_siege_eaters_weapon_impact_sfx` | `cannibal_siege_eaters_weapon_impact.wav`, `cannibal_siege_eaters_weapon_impact_02.wav` | impact at the measured strike frame |
| `cannibal_siege_eaters_idle_vocal_sfx` | `cannibal_siege_eaters_idle_vocal.wav` (trimmed to the voiced part) | trigger_once on idle entry as today |
| `cannibal_siege_eaters_selection_sfx` | `cannibal_siege_eaters_selection.wav` (trimmed to the voiced part) | selection, not an entity state |
| `cannibal_march_predation_column_death_sfx` | `cannibal_march_predation_column_death.wav`, `cannibal_march_predation_column_death_02.wav` | one-shot at the collapse impact frame of the death action |
| `cannibal_march_predation_column_movement_sfx` | `cannibal_march_predation_column_movement.wav`, `cannibal_march_predation_column_movement_02.wav` | one event per measured foot plant in move and retreat (alternates automatically) |
| `cannibal_march_predation_column_training_sfx` | `cannibal_march_predation_column_training.wav` | one-shot at the exertion peak of the training action |
| `cannibal_march_predation_column_weapon_impact_sfx` | `cannibal_march_predation_column_weapon_impact.wav` (unchanged shared-batch master) | impact at the measured strike frame |
| `cannibal_march_predation_column_idle_vocal_sfx` | `cannibal_march_predation_column_idle_vocal.wav` (trimmed to the voiced part) | trigger_once on idle entry as today |
| `cannibal_march_predation_column_selection_sfx` | `cannibal_march_predation_column_selection.wav` (trimmed to the voiced part) | selection, not an entity state |

## File facts

| runtime file | length s | peak dBFS | RMS dBFS | source (take) | SHA-256 |
|---|---|---|---|---|---|
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_death.wav` | 1.701 | -3.00 | -19.28 | thebardofblasphemy: Grunts of male death and pain (distinct male death grunt take 7) | `6c8cd5879b5b3825c3e706b25c20707b7efdffcb6d3b08a5c03d14377b8cc83c` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_death_02.wav` | 0.893 | -3.02 | -20.72 | Exewin: Death Sounds, take 11.ogg (extracted from exewinDeathSoundsPack.zip) (second death take (Exewin 11.ogg)) | `e194d6be32bfb4b3ab23f710c2284df3ed55fa01e2bf8d4305a721eaa1e05649` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_training.wav` | 0.680 | -3.00 | -17.70 | thebardofblasphemy: Grunts of male death and pain (distinct exertion grunt take 15) | `9744a148de9f6370462c72c80479d3bf4504665bedd5c1aef2c1da7d316605bd` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_weapon_attack.wav` | 0.576 | -3.03 | -21.36 | qubodup (Iwan Gabovitch): Bamboo stick swish swosh-03.flac (extracted from swoshes.7z) (recorded staff swish, whole take) | `8f754bb68135b06f2fca88d3b1ed8b2e787552e62741c0cfb213bafd956b89b2` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_weapon_attack_02.wav` | 0.277 | -3.01 | -20.87 | qubodup (Iwan Gabovitch): Bamboo stick swish swosh-01.flac (extracted from swoshes.7z) (second swish take) | `e052286b359aa7ed60ae6924078f7e106c0a44435760c509da85495d2da3ac46` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_movement.wav` | 0.134 | -6.00 | -25.81 | GboxMikeFozzy: Footsteps 01-footstep.ogg (footstep take A) | `e00178106d62df20d0ef222b04539cfc9045d0a57cb38413afcfcf2abd160e80` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_movement_02.wav` | 0.333 | -6.00 | -29.12 | GboxMikeFozzy: Footsteps 04-footstep.ogg (footstep take B) | `4531dc2be3b63a9de52a9933e66fcd004a6e1947cc6c216b541fe4cbd062d23a` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_selection.wav` | 0.812 | -3.00 | -15.30 | kurt: Soldier Voice Acting: wounded.ogg (groan takes) (groan take 0 (the sustained yell sat outside the shared RMS band)) | `517a4313f1c5398f65b5a7e0ea72df64009d612625aae502049c1a23b9f85701` |
| `sound/014_cannibalism/units/cannibal_bone_guard/cannibal_bone_guard_idle_vocal.wav` | 0.700 | -3.00 | -18.67 | thebardofblasphemy: Grunts of male death and pain (idle grunt take 14 (the previous sustained HaelDB moan sat outside the shared RMS band)) | `bf180da0390f53a89127a5535c2bb494a7442f68aa74eb78d85e4dceaa89bd40` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_death.wav` | 1.930 | -3.00 | -16.10 | thebardofblasphemy: Grunts of male death and pain (distinct male death grunt take 8) | `610c8fc0d676dc3952ba981a26035389ffdf788cc4e8f242dc88a14fe8a7f5a0` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_death_02.wav` | 0.821 | -3.01 | -19.87 | Exewin: Death Sounds, take 4.ogg (extracted from exewinDeathSoundsPack.zip) (second death take (Exewin 4.ogg)) | `217e703ed8b2d791e8d988e33150ca78b71fa0826ecb85839fa8d2b599d5bd60` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_training.wav` | 0.861 | -3.00 | -16.30 | thebardofblasphemy: Grunts of male death and pain (distinct exertion grunt take 3) | `65665ff2dfb880774b0da38079bc5c760e093fbe03888debe906068a5fc57f90` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_weapon_attack.wav` | 0.416 | -3.00 | -21.89 | qubodup (Iwan Gabovitch): Bamboo stick swish swosh-05.flac (extracted from swoshes.7z) (recorded staff swish, whole take) | `3e210edb2f0304b218a083592d01d815c782f6afd77a6232ae9ab2e01ce6659c` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_weapon_attack_02.wav` | 0.256 | -3.00 | -18.78 | qubodup (Iwan Gabovitch): Bamboo stick swish swosh-04.flac (extracted from swoshes.7z) (second swish take) | `8e1e64a786e0ba96ec926b783961727a8df1700295a8498e94e0a30c4ed63f39` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_weapon_impact_02.wav` | 0.176 | -3.03 | -21.53 | Ben Jaszczak and Brian Nelson / Still North Media: Spear Spear Haft on Haft.wav (extracted from medieval_sfx_weapon_on_weapon_2_of_2.7z) (second impact take: recorded spear contact hit 0, hit window plus 90 ms tail) | `5688a772561730c78ccf086ef9446f230fb989b9befa34beb71aedc2ae60b45c` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_movement.wav` | 0.317 | -6.01 | -25.23 | GboxMikeFozzy: Footsteps 03-footstep.ogg (footstep take A) | `e313563456b299e43cb231d050a5b5b5a4fc8a9186d11d2d53f61630617bf69a` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_movement_02.wav` | 0.246 | -6.00 | -22.30 | GboxMikeFozzy: Footsteps 06-footstep.ogg (footstep take B) | `eab0b002d836669bc09fa23543ed0d071e81e0ed9f9a618ecdc7c04ea0f1ab9e` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_selection.wav` | 0.990 | -3.00 | -18.24 | HaelDB: Male Grunt/Yelling Sounds (current runtime derivative; original pack archival gap recorded in provenance_review.json) (existing CC0 take re-trimmed to the voiced part) | `becca5d592e72392f2fe4457b4545e691cf4bf867fe949da8b352c002a37ae0f` |
| `sound/014_cannibalism/units/cannibal_siege_eaters/cannibal_siege_eaters_idle_vocal.wav` | 1.126 | -3.00 | -20.80 | HaelDB: Male Grunt/Yelling Sounds (current runtime derivative; original pack archival gap recorded in provenance_review.json) (existing CC0 take re-trimmed to the voiced part) | `766434253ac6546ebb0f42bcd8fba8e64f440d4ee9e93fda8d0eab245b999aeb` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_death.wav` | 1.740 | -3.00 | -19.59 | thebardofblasphemy: Grunts of male death and pain (distinct male death grunt take 18) | `648e1c59bae4773f08fd246169e4608cde2373fd658366350d2f9f1e90b454aa` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_death_02.wav` | 0.891 | -3.00 | -16.29 | Exewin: Death Sounds, take 5.ogg (extracted from exewinDeathSoundsPack.zip) (second death take (Exewin 5.ogg)) | `1ad29601ed7af67430b7e4ea1395d5ff953757ecc7c08ea90da92516d3b3295e` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_training.wav` | 1.101 | -3.00 | -20.88 | thebardofblasphemy: Grunts of male death and pain (distinct exertion grunt take 17) | `9ed46f3f51bbd03d50127d8bcf768dd1edbbb3863459d2ecfa6a163f4432414a` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_movement.wav` | 0.333 | -6.00 | -29.12 | GboxMikeFozzy: Footsteps 04-footstep.ogg (footstep take A) | `4531dc2be3b63a9de52a9933e66fcd004a6e1947cc6c216b541fe4cbd062d23a` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_movement_02.wav` | 0.134 | -6.00 | -25.81 | GboxMikeFozzy: Footsteps 01-footstep.ogg (footstep take B) | `e00178106d62df20d0ef222b04539cfc9045d0a57cb38413afcfcf2abd160e80` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_selection.wav` | 0.786 | -3.00 | -19.03 | HaelDB: Male Grunt/Yelling Sounds (current runtime derivative; original pack archival gap recorded in provenance_review.json) (existing CC0 take re-trimmed to the voiced part) | `3307dcc017cb761943b24139db8adb463ab20848cd78242ff95c0e8dac413189` |
| `sound/014_cannibalism/units/cannibal_march_predation_column/cannibal_march_predation_column_idle_vocal.wav` | 0.800 | -3.00 | -17.47 | HaelDB: Male Grunt/Yelling Sounds (current runtime derivative; original pack archival gap recorded in provenance_review.json) (existing CC0 take re-trimmed to the voiced part) | `16664ae50ab22365ec3e9ecdb68befbac1ba342f4de00eab61d7d1150f208e33` |

## Not delivered

- Second impact takes for bone_guard from the Still North Media spear-contact recordings failed the shared one-shot RMS band (sharp transients, RMS 10 dB under the band after peak normalization); the single existing rubberduck impact take stays. Only siege_eaters received a passing second impact take.
- `cannibal_bone_guard_selection.wav` is now a kurt (CC-BY 3.0) wounded-groan take because the previous sustained HaelDB yell could not meet the shared RMS band; `cannibal_bone_guard_idle_vocal.wav` is a thebardofblasphemy (CC0) grunt take for the same reason.
- Cue lengths above are the authoritative durations for your event placement; WP2 did not receive `wp6_to_wp2.md`, so no WP6 frame numbers were applied here.

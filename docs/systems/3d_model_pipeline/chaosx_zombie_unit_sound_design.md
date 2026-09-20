# Chaos Redux zombie unit sound design

## Purpose

The shared zombie model uses a dedicated sourced audio identity for its creature vocalizations, movement, attacks, and deaths.

Current disposition: runtime WAVs and sound definitions are installed, while sonic clip choice is **needs_user_review**, exact visual/audio contact synchronization is **blocked pending listening and live playback review**, and subunit-specific acknowledgement selection has no verified consumer. The current model lineage is Meshy 7 body task `01a0ba94-9607-729b-92e5-53951c59e8e1` (30 credits) and recovery remesh `01a0ba9f-8b53-77e5-a132-ea513bcd0672` (5 credits); the parent then accepted corrected v2 rig/actions and conservative death v5. The current package handoff is `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/zombies_3d_pipeline_20260919.md`.

`common/units/zombies.txt` gives the base `zombies` and `wendigo_zombies` sub-units `sprite = zombies`, so those consumers resolve the shared `zombies_entity`. The infected, rabid, parasitic, mutant, undead, necrotic, and demonic families use their own `chaosx_*_zombies` sprite stems and separate entity files; their audio packages have separate evidence and are outside this shared base-zombie contract.

## Runtime contract

| Surface | Runtime identifier or path | Role |
| --- | --- | --- |
| Unit consumer | `common/units/zombies.txt` | Resolves `zombies` and `wendigo_zombies` to the shared sprite; specialized families have separate stems |
| Entity | `zombies_entity` in `gfx/entities/chaosx_zombies.asset` | Receives state-entry sound events |
| Selection consumer | `ZZZ_infantry_idle` | Country/original-tag infantry selection voice used by `ZZZ` zombie armies |
| Sound definitions | `sound/chaosx_zombies_sound.asset` | Declares source WAVs and soundeffect wrappers |
| Runtime audio | `sound/002_zombie_outbreak/zombies/*.wav` | 24 installed signed-16 PCM WAV assets (`pcm_s16le`, 44.1 kHz, mono); 15 older shared files and nine later sourced derivatives |

The entity binds distinct corrected v2 actions for idle, move, attack, defend, support attack, retreat, and training, plus death v5. The following times are implemented in the entity file; audible and contact accuracy still require review.

| State | Soundeffect | Synchronization |
| --- | --- | --- |
| `idle` and `training` | `chaosx_zombie_idle` | One trigger-once event without a numeric offset |
| `move` and `retreat` | `chaosx_zombie_move` | Events at 0.3333 and 1.0000 in each looping state; boot-contact alignment unverified |
| `attack` | `chaosx_zombie_attack_vocal`, `chaosx_zombie_attack_impact` | Events at 0.3333 and 0.6667, corresponding to frames 8 and 16 at 24 fps |
| `defend` | `chaosx_zombie_defend_contact` | Event at 0.5000, corresponding to frame 12 at 24 fps |
| `support_attack` | `chaosx_zombie_attack_vocal`, `chaosx_zombie_support_attack_contact` | Events at 0.3333 and 0.6667, corresponding to frames 8 and 16 at 24 fps |
| `death` | `chaosx_zombie_death_vocal`, `chaosx_zombie_death` | Events at 0.5000 and 1.5000 in death v5; the latter uses the older death files |

`chaosx_zombie_hurt` is declared but has no verified entity-state consumer. The older `chaosx_zombie_attack` wrapper remains declared but is no longer invoked by the base zombie entity. Distinct `chaosx_zombie_retreat_step` and per-subunit acknowledgement remain proposals, not runtime bindings.

## Selection-audio consumer

The national soldier-voice consumer constructs `TAG_infantry_idle` for selection and the related `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat` identifiers for other army voice situations.

The zombie package defines `ZZZ_infantry_idle` in the vanilla `Voices` category and maps it to the three sourced zombie idle moans.
The direct `ZZZ` outbreak and the dynamically created outbreak countries use `original_tag = ZZZ`, so this is the intended country-voice selection family for zombie armies.

This hook is country/original-tag based, not sprite or sub-unit based.
If another country fields zombie battalions while retaining a different original tag, its infantry selection voice remains that country's voice family because HOI4 exposes no per-subunit selection key.

## Vanilla precedents

The movement event follows the installed vanilla infantry pattern in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`, where the `move` state plays `infantry_move_animation`.

The sound wrapper structure follows `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/soundeffects.asset` and the source declaration structure follows `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/sound.asset`.

The country-selection voice follows `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/integrated_dlc/dlc018_together_for_victory/sound/vo.asset`, where `GER_infantry_idle`, `SOV_infantry_idle`, and the other tag-prefixed families are registered in the `Voices` category.
The installed executable also contains the consumer templates `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat`.

The entity event shape follows the offline `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md` sound-event example.

## Runtime audio format contract

The installed vanilla infantry voice precedent is signed 16-bit PCM (`pcm_s16le`), 44.1 kHz, mono, and the runtime zombie voice files use that same delivery format.
The three older idle originals and the nine later derived originals have preserved hashes and source-to-runtime mappings; twelve older movement/attack/death mappings remain unresolved in the scoped evidence. The mapped runtime copies are mechanically converted from source files whose pages state CC0.
The deterministic conversion is `ffmpeg -map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`.
A runtime unit package is not complete until `ffprobe` reports `pcm_s16le,44100,1,16` for every installed WAV, because float WAVs such as `pcm_f32le` are not accepted by the runtime voice contract.

## Source provenance and processing

The idle and attack zombie vocal candidates come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, which is marked CC0 on the source page.
The selection wrapper reuses the three mechanically converted idle one-shots from that same CC0 source instead of duplicating or synthesizing audio.

The movement candidates come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, which is marked CC0 and states that no attribution is required.

The nine later vocal, impact, and hurt derivatives come from the archived [Zombie / Skeleton / Monster Voice Effects](https://opengameart.org/content/zombie-skeleton-monster-voice-effects) pack by ArcadeParty, the archived [Impact](https://opengameart.org/content/impact) pack by Iwan “qubodup” Gabovitch, and the archived ianzazz pack. `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/runtime_derivations_20260919.json` gives an exact source path, source hash, conversion command, runtime path, and runtime hash for each of those nine files. The impact page labels the derivative CC0, but its underlying Freesound recordings were not independently audited. An older note named Ogrebane's Monster Sound Pack as an attack/death candidate; no corresponding original or per-file derivation was found in this package, so it is not treated as established provenance for an installed file.

The selection source archive is `https://opengameart.org/sites/default/files/zombienoises.zip`, downloaded for verification on 2026-08-12 with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.

| Source member | Source SHA-256 | Runtime file | Runtime SHA-256 |
| --- | --- | --- | --- |
| `zombienoise1.ogg` | `E3105F5259AD8B17BD1134C5A5CEE79FC7F2F3662466D348BC05944CB92F16AE` | `zombie_idle_moan_01.wav` | `C0AA8630E25E0A446B9605EDA6711291DE2B4F78F1AB2FB0A92C2A08A6DB94FF` |
| `zombienoise2.ogg` | `F9E23D6545F64798D29F2B7AC767DA6208C1DC43B6D0928DC037FAE4BCA13B13` | `zombie_idle_moan_02.wav` | `8F8FAA368A6148914FDBCBA4966BF08AB8A8987481AB4D219BB931860D85DE5B` |
| `zombienoise3.ogg` | `968B48B14A83A17B387E7373C83D3B9553BF21D2B0E03A67909EAD4FC21F38B1` | `zombie_idle_moan_03.wav` | `4D97968CFE6FFB1DCC3519A697D09402A126B0DE2C0F95CAC062F89E025C6A` |

The three idle/selection derivatives reproduce byte-for-byte with FFmpeg using `-map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`. The nine later derivatives have matching source and runtime hashes in `runtime_derivations_20260919.json`. The six installed movement files and six older attack/death files do not yet have an equally durable per-file source-to-runtime mapping in the scoped evidence; a source page or filename alone does not close that gap. No synthesis, test tones, placeholder audio, or unrelated vanilla sound files are recorded in the verified derivations.

All 24 installed WAV files probed as 44.1 kHz signed 16-bit PCM in mono on 2026-09-19, matching the installed vanilla voice delivery format.

## Runtime tuning

The wrappers use vanilla falloff names, `is3d = yes`, capped audible counts, small timing and pitch variation, and random-repetition prevention to keep large zombie formations readable without producing a single undifferentiated wall of sound.

The durable selection source-to-runtime mapping and checksums are recorded above so the runtime package does not depend on a temporary model-job workspace.

## Validation boundary

The 24 installed WAV formats, runtime source declarations, soundeffect identifiers, entity event identifiers and numeric times, and base/Wendigo shared sprite consumers were checked locally. The nine later WAVs matched their recorded runtime SHA-256 values. The earlier specialized-zombie intake at `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/specialized_zombie_audio_counter_intake.md` is a dated snapshot with old float-WAV hashes and old entity bindings, not current runtime evidence.

Each installed zombie WAV reports `pcm_s16le,44100,1,16` through `ffprobe`.

The `ZZZ_infantry_idle` identifier, `Voices` category membership, three selection candidates, and `ZZZ` original-tag consumer were checked against the installed vanilla voice package.

Sonic suitability, impact and footstep contact alignment, the older movement/attack/death per-file provenance mapping, and live playback in Hearts of Iron IV remain unresolved. The agent does not launch the game; live playback is user-owned.

## Future extensions

Review whether `wendigo_zombies` should continue to share the base zombie sprite and sound package, and preserve the separate entity/audio contracts for specialized families when their distinct models are the intended consumers.

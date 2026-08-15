# Chaos Redux zombie unit sound design

## Purpose

The shared zombie model uses a dedicated sourced audio identity for its creature vocalizations, movement, attacks, and deaths.

All twelve zombie sub-unit definitions in `common/units/zombies.txt` use `sprite = zombies`, so the shared `zombies_entity` and its sound events apply consistently to the base and disease-family zombie units.

## Runtime contract

| Surface | Runtime identifier or path | Role |
| --- | --- | --- |
| Unit consumer | `common/units/zombies.txt` | Resolves every zombie sub-unit to the shared sprite |
| Entity | `zombies_entity` in `gfx/entities/chaosx_zombies.asset` | Receives state-entry sound events |
| Selection consumer | `ZZZ_infantry_idle` | Country/original-tag infantry selection voice used by `ZZZ` zombie armies |
| Sound definitions | `sound/chaosx_zombies_sound.asset` | Declares source WAVs and soundeffect wrappers |
| Runtime audio | `sound/002_zombie_outbreak/zombies/*.wav` | Signed-16 PCM WAV assets (`pcm_s16le`, 44.1 kHz, mono) |

The entity keeps the existing custom actions and adds one-shot sound events to the corresponding vanilla land-unit states.

| State | Soundeffect | Synchronization |
| --- | --- | --- |
| `idle` | `chaosx_zombie_idle` | State entry, with low-volume randomized moans |
| `move` and `retreat` | `chaosx_zombie_move` | State entry, with randomized footstep one-shots matching the shamble loop |
| `attack`, `defend`, and `support_attack` | `chaosx_zombie_attack` | State entry, with randomized creature attack vocalizations |
| `death` | `chaosx_zombie_death` | State entry, with randomized death vocalizations |

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
The source files remain preserved with their original checksums; the runtime copies are license-permitted mechanical derivatives.
The deterministic conversion is `ffmpeg -map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`.
A runtime unit package is not complete until `ffprobe` reports `pcm_s16le,44100,1,16` for every installed WAV, because float WAVs such as `pcm_f32le` are not accepted by the runtime voice contract.

## Source provenance and processing

The idle and attack zombie vocal candidates come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, which is marked CC0 on the source page.
The selection wrapper reuses the three mechanically converted idle one-shots from that same CC0 source instead of duplicating or synthesizing audio.

The movement candidates come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, which is marked CC0 and states that no attribution is required.

Additional attack and death candidates come from [Monster Sound Pack, Volume 1](https://opengameart.org/content/monster-sound-pack-volume-1) by Ogrebane, which is marked CC0 and described as containing monster growls, grunts, and death sounds.

The selection source archive is `https://opengameart.org/sites/default/files/zombienoises.zip`, downloaded for verification on 2026-08-12 with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.

| Source member | Source SHA-256 | Runtime file | Runtime SHA-256 |
| --- | --- | --- | --- |
| `zombienoise1.ogg` | `E3105F5259AD8B17BD1134C5A5CEE79FC7F2F3662466D348BC05944CB92F16AE` | `zombie_idle_moan_01.wav` | `C0AA8630E25E0A446B9605EDA6711291DE2B4F78F1AB2FB0A92C2A08A6DB94FF` |
| `zombienoise2.ogg` | `F9E23D6545F64798D29F2B7AC767DA6208C1DC43B6D0928DC037FAE4BCA13B13` | `zombie_idle_moan_02.wav` | `8F8FAA368A6148914FDBCBA4966BF08AB8A8987481AB4D219BB931860D85DE5B` |
| `zombienoise3.ogg` | `968B48B14A83A17B387E7373C83D3B9553BF21D2B0E03A67909EAD4FC21F38B1` | `zombie_idle_moan_03.wav` | `4D97968CFE6FFB1DCC3519A697D09402A126B0DE2C0F95CAC062F89E025C6A` |

The derived files reproduce byte-for-byte with FFmpeg using `-map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`; no synthesis, test tones, placeholder audio, or unrelated vanilla sound files were used.

The final assets are 44.1 kHz signed 16-bit PCM WAV files in mono, matching the installed vanilla voice delivery format.

## Runtime tuning

The wrappers use vanilla falloff names, `is3d = yes`, capped audible counts, small timing and pitch variation, and random-repetition prevention to keep large zombie formations readable without producing a single undifferentiated wall of sound.

The durable selection source-to-runtime mapping and checksums are recorded above so the runtime package does not depend on a temporary model-job workspace.

## Validation boundary

Source files, derived WAV format, runtime file references, soundeffect identifiers, entity event identifiers, and all twelve sprite consumers were checked locally.

The installed zombie WAVs were additionally probed with `ffprobe` and each reports `pcm_s16le,44100,1,16`.

The `ZZZ_infantry_idle` identifier, `Voices` category membership, three selection candidates, and `ZZZ` original-tag consumer were checked against the installed vanilla voice package.

Live playback in Hearts of Iron IV remains user-owned because the agent does not launch the game.

## Future extensions

If the disease families later need distinct audio identities, add separate entity profiles only when the gameplay design requires audible differentiation; otherwise keep the shared package to preserve the one-model and one-sound-family contract.

# Chaos Redux zombie unit sound design

## Purpose

The shared zombie model uses a dedicated sourced audio identity for its creature vocalizations, movement, attacks, and deaths.

All twelve zombie sub-unit definitions in `common/units/zombies.txt` use `sprite = zombies`, so the shared `zombies_entity` and its sound events apply consistently to the base and disease-family zombie units.

## Runtime contract

| Surface | Runtime identifier or path | Role |
| --- | --- | --- |
| Unit consumer | `common/units/zombies.txt` | Resolves every zombie sub-unit to the shared sprite |
| Entity | `zombies_entity` in `gfx/entities/chaosx_zombies.asset` | Receives state-entry sound events |
| Sound definitions | `sound/chaosx_zombies_sound.asset` | Declares source WAVs and soundeffect wrappers |
| Runtime audio | `sound/002_zombie_outbreak/zombies/*.wav` | HOI4-compatible PCM WAV assets |

The entity keeps the existing custom actions and adds one-shot sound events to the corresponding vanilla land-unit states.

| State | Soundeffect | Synchronization |
| --- | --- | --- |
| `idle` | `chaosx_zombie_idle` | State entry, with low-volume randomized moans |
| `move` and `retreat` | `chaosx_zombie_move` | State entry, with randomized footstep one-shots matching the shamble loop |
| `attack`, `defend`, and `support_attack` | `chaosx_zombie_attack` | State entry, with randomized creature attack vocalizations |
| `death` | `chaosx_zombie_death` | State entry, with randomized death vocalizations |

The package does not add a separate selection or order-acknowledgement voice because the verified land-unit entity path exposes animation-state events, while the vanilla selection and order sounds are global army UI effects rather than per-subunit entity consumers.

## Vanilla precedents

The movement event follows the installed vanilla infantry pattern in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`, where the `move` state plays `infantry_move_animation`.

The sound wrapper structure follows `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/soundeffects.asset` and the source declaration structure follows `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/sound.asset`.

The entity event shape follows the offline `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md` sound-event example.

## Source provenance and processing

The idle and attack zombie vocal candidates come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, which is marked CC0 on the source page.

The movement candidates come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, which is marked CC0 and states that no attribution is required.

Additional attack and death candidates come from [Monster Sound Pack, Volume 1](https://opengameart.org/content/monster-sound-pack-volume-1) by Ogrebane, which is marked CC0 and described as containing monster growls, grunts, and death sounds.

The original downloads, extracted source candidates, source checksums, and the source-to-runtime mapping are retained under `docs/assets/002_zombie_outbreak/models_3d/zombies/audio/`.

The derived files were converted with FFmpeg using `-ar 44100 -c:a pcm_f32le`; no synthesis, test tones, placeholder audio, or unrelated vanilla sound files were used.

The final assets are 44.1 kHz PCM float WAV files, preserving stereo for vocal sources and mono for the footsteps source.

## Runtime tuning

The wrappers use vanilla falloff names, `is3d = yes`, capped audible counts, small timing and pitch variation, and random-repetition prevention to keep large zombie formations readable without producing a single undifferentiated wall of sound.

The source role map and derived SHA-256 values are recorded in `docs/assets/002_zombie_outbreak/models_3d/zombies/audio/source_manifest.md`.

## Validation boundary

Source files, derived WAV format, runtime file references, soundeffect identifiers, entity event identifiers, and all twelve sprite consumers were checked locally.

Live playback in Hearts of Iron IV remains user-owned because the agent does not launch the game.

## Future extensions

If the disease families later need distinct audio identities, add separate entity profiles only when the gameplay design requires audible differentiation; otherwise keep the shared package to preserve the one-model and one-sound-family contract.

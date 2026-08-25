# Event 014 Remaining Unit Audio Runtime Wiring

Status date: 2026-08-25 parent-owned source-definition pass

## Scope

The four Event 014 model packages that are not yet runtime-promotable already contained licensed, source-derived audio candidates. This pass copied those final WAV derivatives into the engine-facing `sound/014_cannibalism/units/` tree and added their `sound` and `soundeffect` definitions to `sound/014_cannibalism_units_sound.asset`. It did not promote any model, author or alias skeletal actions, or claim live playback.

## Installed audio

| Package | Roles installed | Runtime folder | Source evidence |
| --- | ---: | --- | --- |
| `cannibal_bone_riders` | 6 source files and 7 wrappers, with horse-neigh used for selection and idle | `sound/014_cannibalism/units/cannibal_bone_riders/` | `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/audio/audio_manifest.md` |
| `cannibal_island_reavers` | 7 | `sound/014_cannibalism/units/cannibal_island_reavers/` | `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/audio/sound_design_handoff.md` |
| `cannibal_scavenger_warband` | 6 | `sound/014_cannibalism/units/cannibal_scavenger_warband/` | `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/manifest.md` and its audio receipts |
| `cannibal_network_cadre` | 7 source files and wrappers, including the training cue documented in the source manifest | `sound/014_cannibalism/units/cannibal_network_cadre/` | `docs/assets/014_cannibalism/models_3d/cannibal_network_cadre/evidence/audio_sources/source_manifest.json` |

All 26 copied runtime files were hash-compared against their immutable `audio/derived/` sources. `ffprobe` reports signed 16-bit PCM, 44,100 Hz, mono for the four package sets. No generated, synthesized, test-tone, default, or unlicensed replacement was added.

## Definition and consumer boundary

The shared Event 014 sound asset now contains unique source IDs and `soundeffect` wrappers for all four package sets. `sound/014_cannibalism_voices.asset` registers the exact country-level selection consumer for CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH, and CBL as `<TAG>_infantry_idle`, using the approved cannibal selection source. The definitions are source-ready, but the following remain intentionally open:

- Meshy-sourced skeletal actions, action-specific frame synchronization, and PDX export/reimport for all four blocked model packages.
- Entity/action runtime binding and live map playback review.
- Per-subunit selection routing is not possible on this HOI4 surface. The country-level idle bindings intentionally cover every infantry division under CBA-CBH and CBL; action-specific frame synchronization and live playback remain pending the accepted model/action consumers.

The five previously installed model packages retain their existing definitions and 35 runtime WAVs. This pass expands the source-definition layer to all nine custom unit families without treating audio presence as model completion.

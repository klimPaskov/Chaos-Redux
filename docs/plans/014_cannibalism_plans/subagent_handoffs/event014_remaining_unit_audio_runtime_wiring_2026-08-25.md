# Event 014 Remaining Unit Audio Runtime Wiring

Status date: 2026-08-25 parent-owned source-definition pass; model-gate wording superseded by the 2026-08-26 vanilla-visual reuse decision

## Scope

The two Event 014 gameplay consumers that formerly had custom model packages already contained licensed, source-derived audio candidates. This pass also records the already-installed Island Reavers and Scavenger Warband audio companions. The final WAV derivatives are copied into the engine-facing `sound/014_cannibalism/units/` tree and their `sound` and `soundeffect` definitions are in `sound/014_cannibalism_units_sound.asset`. Audio presence is not treated as a substitute for bespoke-package live playback, and the approved vanilla-visual decision removes custom model/action acceptance from Bone Riders and Network Cadre.

## Installed audio

| Package | Roles installed | Runtime folder | Source evidence |
| --- | ---: | --- | --- |
| `cannibal_bone_riders` | 6 historical source files and 7 wrappers, with horse-neigh used for selection and idle | `sound/014_cannibalism/units/cannibal_bone_riders/` | Retained in superseded model/audio handoffs; the removed model workspace is lineage-only |
| `cannibal_island_reavers` | 7 | `sound/014_cannibalism/units/cannibal_island_reavers/` | `docs/assets/014_cannibalism/models_3d/cannibal_island_reavers/audio/sound_design_handoff.md` |
| `cannibal_scavenger_warband` | 6 | `sound/014_cannibalism/units/cannibal_scavenger_warband/` | `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/manifest.md` and its audio receipts |
| `cannibal_network_cadre` | 7 historical source files and wrappers, including the training cue documented in the source manifest | `sound/014_cannibalism/units/cannibal_network_cadre/` | Retained in superseded model/audio handoffs; the removed model workspace is lineage-only |

All 26 copied runtime files were hash-compared against their immutable `audio/derived/` sources. `ffprobe` reports signed 16-bit PCM, 44,100 Hz, mono for the four package sets. No generated, synthesized, test-tone, default, or unlicensed replacement was added.

## Definition and consumer boundary

The shared Event 014 sound asset now contains unique source IDs and `soundeffect` wrappers for all four package sets. `sound/014_cannibalism_voices.asset` registers the exact country-level selection consumer for CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH, and CBL as `<TAG>_infantry_idle`, using the approved cannibal selection source. The definitions are source-ready, but the following remain intentionally open:

- Entity/action runtime binding and live map playback review for the seven bespoke model packages.
- Per-subunit selection routing is not possible on this HOI4 surface. The country-level idle bindings intentionally cover every infantry division under CBA-CBH and CBL; model-specific action synchronization applies only to the seven bespoke model entities, while Bone Riders and Network Cadre use vanilla animation families.

The seven installed bespoke model packages retain their definitions and 48 runtime WAVs. This pass expands the source-definition layer to all nine gameplay families without treating audio presence as live playback completion.

# Stone Cohorts audio manifest

Package date: 2026-08-06.

Revalidated again on 2026-08-27. All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`; the current codec/hash receipt is `audio/evidence/ffprobe_revalidation_2026-08-27.json`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `quern_stones.ogg` | `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7` | Work With Sounds; recordist Monika Widzicka | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg |
| `metal_clanging.ogg` | `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408` | Camshaft64 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg |

## Derived ledger

Every WAV was mechanically converted from the retained derivative to signed 16-bit PCM (`pcm_s16le`), 44,100 Hz, mono with metadata removed. The earlier trim, loudness normalization, and fades remain source-derived; no synthesis, generation, pitch alteration, layering, or invented audio was used. FFprobe revalidation reports `pcm_s16le`, 44,100 Hz, mono, 16 bits for every file.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_stone_cohorts_select.wav` | `quern_stones.ogg` 1.0–2.4 s | `selection/acknowledgement` | one-shot; exact engine selection consumer unresolved | `f31f41c0d58a037387ea73e17a9ba7a8d24b66963457523da0baffd837d2eaf0` |
| `chaosx_stone_cohorts_idle.wav` | `quern_stones.ogg` 10.0–12.2 s | `chaosx_stone_idle` | provisional; resync to accepted provider action | `d18fb5226e6aecc5f5633376069dac7c518ed603409035405fe59905e9c0caad` |
| `chaosx_stone_cohorts_move.wav` | `quern_stones.ogg` 20.0–21.6 s | `chaosx_stone_move` | provisional; resync to accepted provider action | `dcd1815b6d900e47e2bd574aed3438000f497c70342bd9be2949ca49211d2345` |
| `chaosx_stone_cohorts_attack.wav` | `metal_clanging.ogg` 4.0–5.4 s | `chaosx_stone_attack` | provisional; resync to accepted provider action | `102b77c251e5056458d5e062a6734a43c1981976f1458f50f1e55912b85326cf` |
| `chaosx_stone_cohorts_collapse_recovery.wav` | `metal_clanging.ogg` 8.0–9.5 s | `chaosx_stone_collapse_recovery` | provisional; resync to accepted provider action | `4b76b3c3342c17fd286d9c67c0c671c3aa81fe334456d2000ec54afd2709421e` |
| `chaosx_stone_cohorts_death.wav` | `quern_stones.ogg` 45.0–47.2 s | `chaosx_stone_death` | provisional; resync to accepted provider action | `2c28148dc2bd58125fda0e2b3f594fb33cbe50a1153d20227e84ddb94e2fbe13` |

The source and derived hashes above were recomputed after conversion and matched on 2026-08-27. Source licensing and files pass. The actual installed vanilla land-unit selection consumer is the global `select_army` soundeffect in `sound/soundeffects.asset`; no per-subunit selection hook was found in the inspected unit/entity surface. The existing `scoped_sound_effect = "chaosx_stone_cohorts_select_sfx"` call is a formation-creation cue, not unit-selection evidence. Package status remains `blocked` for the mandatory selection role and because action synchronization must be rebuilt against accepted provider actions; the legacy locally authored action timings are not valid synchronization evidence.

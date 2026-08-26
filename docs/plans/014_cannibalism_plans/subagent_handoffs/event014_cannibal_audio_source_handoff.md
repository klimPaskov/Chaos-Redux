# Event 014 cannibal unit audio source handoff

Status: **source and conversion package complete; runtime sound definitions and playback validation remain parent-owned**.

Scope limitation: this handoff covers the eight foot-family audio packages only. `cannibal_bone_riders` is a separate cavalry gameplay package whose custom model/audio work is superseded by the approved vanilla `sprite = cavalry` decision; `cannibal_network_cadre` retains its source-audio row but uses vanilla `sprite = infantry` without a custom model entity. Do not infer live nine-family audio playback completion from this document.

All candidates below are mechanical conversions of legally reusable Internet-sourced recordings. No sound was synthesized, generated, recorded, or replaced with a placeholder. Every job preserves its selected immutable originals under `evidence/audio_sources/originals_selected/`, archived source pages under `evidence/audio_sources/source_pages/`, and a machine-readable `evidence/audio_sources/ffprobe_and_hash_receipt.json`. Every derived candidate under `audio/derived/` passes `pcm_s16le`, 44100 Hz, mono inspection.

## Source catalogue

| Source | Creator | Chosen license | Source page | Direct download | Use |
| --- | --- | --- | --- | --- | --- |
| Male Grunt/Yelling Sounds | HaelDB | CC0 option published on the asset page | https://opengameart.org/content/male-gruntyelling-sounds | https://opengameart.org/sites/default/files/yelling%20sounds.zip | Selection, acknowledgement, and occasional idle vocal candidates. |
| Footsteps | GboxMikeFozzy | CC0 | https://opengameart.org/content/footsteps-0 | `https://opengameart.org/sites/default/files/01-footstep_0.ogg` and numbered `02-footstep.ogg` through `06-footstep.ogg` | Individual movement footfalls. |
| Swishes Sound Pack | artisticdude | CC0 | https://opengameart.org/content/swishes-sound-pack | https://opengameart.org/sites/default/files/swishes.zip | Spears, cleaver, polearm, axe, harpoon, and sledgehammer attack swings. |
| 100 CC0 Metal and Wood SFX | rubberduck | CC0 | https://opengameart.org/content/100-cc0-metal-and-wood-sfx | https://opengameart.org/sites/default/files/100-CC0-wood-metal-SFX.zip | Weapon impacts matched to wood, metal, or hammer construction. |
| Fantasy Sound Effects (Tinysized SFX) | Vehicle | CC0 | https://opengameart.org/content/fantasy-sound-effects-tinysized-sfx | https://opengameart.org/sites/default/files/tinysized.zip | Mud/soil movement and bow-arrow wood impacts. |
| Archers Shooting | copyc4t (Paolo D'Emilio) | CC-BY 3.0 | https://opengameart.org/content/archers-shooting | https://opengameart.org/sites/default/files/Archers-shooting.flac | Bow release for March Predation Column and Network Cadre. Attribution must name `copyc4t (Paolo D'Emilio) from OpenGameArt` and link the source page. |
| Male Pain Grunts | stilgar | Public domain | https://commons.wikimedia.org/wiki/File:Male_pain_grunts.ogg | https://upload.wikimedia.org/wikipedia/commons/e/e3/Male_pain_grunts.ogg | Distinct trimmed death-vocal segments. |

Download date for the preserved sources and pages: 2026-08-22.

## Family coverage and synchronization

| Family | Movement | Attack source | Impact source | Animation synchronization |
| --- | --- | --- | --- | --- |
| `cannibal_scavenger_warband` | OGA footstep 01 | `swish-1.wav`, spear thrust/swing | `wood_hit_01.ogg` | Move frames 0 and 12; attack frame 12; impact frame 16; death vocal starts frame 12 and ends by frame 36. |
| `cannibal_feast_guard` | OGA footstep 02 | `swish-2.wav`, cleaver swing | `metal_hit_01.ogg` | Move frames 0 and 12; cleaver attack frame 12; shield/cleaver impact frame 16; death 12-36. |
| `cannibal_feast_cohort` | OGA footstep 03 | `swish-3.wav`, forked polearm | `metal_hit_02.ogg` | Move frames 0 and 12; polearm attack frame 12; impact frame 16; death 12-36. |
| `cannibal_bone_guard` | OGA footstep 04 | `swish-10.wav`, heavy bone axe | `hammer_01.ogg` | Move frames 0 and 12; heavy swing frame 12; impact frame 16; death 12-36. |
| `cannibal_island_reavers` | OGA footstep 05 | `swish-5.wav`, harpoon/hatchet | `wood_hit_02.ogg` | Move frames 0 and 12; attack frame 12; impact frame 16; death 12-36. |
| `cannibal_siege_eaters` | OGA footstep 06 | `swish-11.wav`, siege tool | `hammer_02.ogg` | Move frames 0 and 12; sledge swing frame 12; impact frame 16; death 12-36. |
| `cannibal_march_predation_column` | `mud-steps-01.wav` | `Archers-shooting.flac`, bow release | `wood-twigs-break-01.wav` | Move footfalls at frames 0 and 12; bow release at attack frame 16; arrow impact at frame 24; death 12-36. |
| `cannibal_network_cadre` | `soil-steps-01.wav` | `Archers-shooting.flac`, bow release | `wood-twigs-break-02.wav` | Move footfalls at frames 0 and 12; bow release at attack frame 16; arrow impact at frame 24; death 12-36. |

Every family also has `<slug>_selection.wav`, `<slug>_idle_vocal.wav`, and `<slug>_death.wav`. Selection and acknowledgement may share the selected country voice candidate. Idle vocal candidates are occasional one-shots, not falsely claimed seamless loops.

## Consumer limitation

Selection and acknowledgement are not honest per-subunit consumers in installed HOI4. They bind through country/original-tag voice templates such as `<TAG>_infantry_idle`. The intended Event 014 voice consumers are `CBA`, `CBB`, `CBC`, `CBD`, `CBE`, `CBF`, `CBG`, `CBH`, and `CBL`; the parent must choose country-level mappings rather than pretending the eight subunit ids directly select voices. Entity-state movement, attack, impact, support-attack, retreat, training, and death events may remain family-specific through each bespoke `<slug>_entity`, while Network Cadre uses the installed vanilla infantry entity and animation family under the visual-reuse decision.

Installed precedents inspected for the handoff were the infantry entity state events and the available unit sound/voice asset consumers. The installation does not contain the earlier proposed root `sound/units_sfx.asset` or `sound/vo.asset` paths, so the parent must bind against the actual installed split sound-definition files and preserve this limitation.

## Transformations and runtime boundary

- Selection, idle, movement, attack, and impact candidates are channel/codec/sample-rate conversions only.
- Death candidates are distinct 2.2-second excerpts from the immutable public-domain recording, with a 0.03-second fade-in and 0.2-second fade-out, then channel/codec/sample-rate conversion.
- Exact original and derived hashes, durations, codecs, sample formats, sample rates, and channel counts are in each job's `ffprobe_and_hash_receipt.json`.
- No runtime sound definition, entity file, `.asset`, `.gfx`, localisation, or gameplay consumer was edited by this package.
- Final loudness balancing, soundeffect definitions, wrapper events, country mapping, and in-game playback remain parent-owned.

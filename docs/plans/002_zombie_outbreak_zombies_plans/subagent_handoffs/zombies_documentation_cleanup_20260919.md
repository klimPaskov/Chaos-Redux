# Base zombie 3D and audio documentation cleanup, 2026-09-19

Scope: `chaosx.event002.zombies` base model lineage, final repaired rig/actions, death v9, shared base-zombie runtime audio, the one Meshy rig attempt, and the dated specialized-audio intake where its base-zombie observations had become stale. This is documentation reconciliation only; the parent owns runtime edits and final review, and the user owns live-game validation.

## Source-of-truth map

| Claim | Authority or current evidence | Boundary |
| --- | --- | --- |
| Approved current model input and route | Parent task instruction, `docs/assets/002_zombie_outbreak/models_3d/zombies/job.yaml`, `refs/original/input_manifest.json`, and `refs/derived/base_zombie_meshy_reference_blender_reconstructed_dark_olive_prompt_20260919.txt` | Earlier input and provider tasks are historical; approval basis is the recorded user decision, not the manifest's status label |
| Meshy spend | Official body task `01a0ba94-9607-729b-92e5-53951c59e8e1` at 30 credits, remesh `01a0ba9f-8b53-77e5-a132-ea513bcd0672` at 5 credits, and the one rig task `01a0be3d-955a-7743-960b-45c494c2cf2b` at 5 credits, documented with response receipts and hashes in `zombies_3d_pipeline_20260919.md` | Total 40 credits; the rig was rejected after topology and required-action checks, with no paid animation attempt or retry |
| Current model and animation | `docs/assets/002_zombie_outbreak/models_3d/zombies/manifest.md`, final checkpoint `77_final_zombie_actions_v1.blend`, eight final action exports/reimport reports, final death export/reimport report, and `gfx/entities/chaosx_zombies.asset` | Parent-promoted runtime package; user live-game review remains absent |
| Current bound audio | `sound/chaosx_zombies_sound.asset`, `gfx/entities/chaosx_zombies.asset`, and `sound/002_zombie_outbreak/zombies/` | Source wiring and numeric event times are present; sonic fit and observed contact synchronization are unverified |
| Nine newer audio derivatives | `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/runtime_derivations_20260919.json` and matching installed hashes | Exact source-to-runtime crosswalk exists; role choice and underlying qubodup Freesound chain still need review |
| Older shared audio derivatives | `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md`, `evidence/audio/older_move_runtime_crosswalk_20260920.json`, and `evidence/audio/older_attack_death_partial_crosswalk_20260920.json` | Three idle/selection files, six movement files, and `zombie_attack_01.wav` have durable crosswalks; five older attack/death files remain specialized-wrapper assets without equally durable per-file mappings |
| Source research and open audio roles | `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/source_ledger.md` and `source_design_20260919.md` | Candidate names, page terms, and waveform metadata do not prove audible suitability |
| Specialist intake | `specialized_zombie_audio_counter_intake.md` | Historical base and specialized sprite observations; current `common/units/zombies.txt` gives seven specialized families separate stems, while the tag-scoped selection-consumer limitation remains open |

## Dispositions and handoffs

| Document or working material | Disposition and basis |
| --- | --- |
| `zombies_3d_pipeline_20260919.md` | Implemented for the parent-promoted final body, repaired rig/actions, death v9, model runtime copies, and current audio definitions, with source/reimport references in its final sections; historical dependency and topology-stop sections are superseded by its named continuation sections. Audio listening, contact proof, and live-game review remain unresolved. |
| `docs/assets/002_zombie_outbreak/models_3d/zombies/manifest.md` | Implemented for parent-promoted model and current runtime audio presence, with current continuation appended. Earlier approved-source and blocked-status paragraphs are retained as chronological evidence and superseded by later sections. |
| `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/source_design_20260919.md` | Source research retained; runtime-installation statements reconciled to current sound files and entity events. Clip suitability remains `needs_user_review`; contact synchronization and subunit acknowledgement remain `blocked`. |
| `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md` | Current shared audio runtime contract, supported by source files and format/hash checks. Complete per-file provenance and audible synchronization are unresolved. |
| `specialized_zombie_audio_counter_intake.md` | Superseded for its old base-zombie float-WAV inventory, four-action/entity observations, and assertion that all seven specialized units use `sprite = zombies`; current unit source gives those families separate stems. Its broader specialized routing needs its own current-source audit, so it was not merged or deleted. |
| `source_ledger.md` and `runtime_derivations_20260919.json` | Left unchanged as source and conversion evidence. The ledger's proposed roles are not accepted clip choices. |

## Contradictions and superseded material

The old worker paragraph in `zombies_3d_pipeline_20260919.md` and the former opening of `source_design_20260919.md` said no game-ready audio or sound definition existed; the parent has since installed 24 signed-16 PCM WAVs, expanded `sound/chaosx_zombies_sound.asset`, and added timed entity events. The final continuation in the handoff and the revised source-design opening identify the old worker statement as historical.

The earlier sound-design timing table called move, attack, support, defend, and death sounds state-entry events; `gfx/entities/chaosx_zombies.asset` instead gives numeric times of 0.3333, 0.5000, 0.6667, 1.0000, or 1.5000 depending on state. The table now states the implemented times without claiming audible alignment.

The old specialized intake recorded float-WAV hashes, a four-action base entity, and seven specialized units on the shared sprite before the corrected v2/v5 package, PCM conversion, and separate specialized sprite assignments. Its top notice directs readers to current replacements. No documents were merged or deleted; the chronological worker evidence remains identifiable.

`chaosx_zombie_unit_sound_design.md` formerly said all twelve zombie sub-units used the shared sprite and that separate disease-family audio was future work. Current `common/units/zombies.txt` instead assigns only `zombies` and `wendigo_zombies` to the shared `zombies` sprite and gives the seven specialized families separate sprite stems. The design document now limits its contract to the shared consumers; separate specialized packages require their own audit.

`chaosx_zombie_unit_sound_design.md` formerly named Ogrebane's Monster Sound Pack as an attack/death candidate without an archived original or per-file conversion in this scoped package. It now distinguishes that historical mention from verified provenance. The three idle source-to-runtime pairs, six movement pairs, one older attack pair, and nine newer pairs have exact hashes; the other five legacy attack/death files remain specialized-wrapper assets without a durable per-file crosswalk.

## Stale instructions, hard wraps, and parent decisions

No prompt file was named in this cleanup scope, so no prompt was revised or certified current. No accidental mid-sentence Markdown hard wrap was found in the changed prose; headings, table rows, block quotes, and chronological section breaks were preserved. No accepted spec was rewritten or promoted from an old handoff status.

The parent should decide whether to retain or replace the five older specialized-wrapper attack/death WAVs after a source-to-runtime derivation audit, review the qubodup source chain if those impact clips remain selected, and review the current sonic choices against final action playback. A subunit-specific selection or acknowledgement claim needs a verified consumer; the current `ZZZ_infantry_idle` route is tag scoped. The declared `chaosx_zombie_hurt` wrapper needs a real consumer before hurt playback can be claimed.

## Changes and validation

Changed documentation: `source_design_20260919.md`, `chaosx_zombie_unit_sound_design.md`, `zombies_3d_pipeline_20260919.md`, the base zombie `manifest.md`, and this handoff. `specialized_zombie_audio_counter_intake.md` remains historical and was not edited in this continuation. No gameplay, sound, entity, GFX, localisation, binary asset, or spreadsheet file was edited by the documentation curator.

`docs/assets/` is ignored by `.gitignore`, so the revised `manifest.md` and `source_design_20260919.md` require explicit force-addition when the parent commits the accepted documentation and runtime continuation.

Task-specific checks: all 24 installed zombie WAVs probed as `pcm_s16le`, 44.1 kHz, mono, 16-bit; all nine newer installed hashes matched `runtime_derivations_20260919.json`; all six movement files matched the 2026-09-20 byte-for-byte crosswalk; `zombie_attack_01.wav` matched its partial crosswalk; sound definitions and entity event identifiers/times were read from their current source files; the final eight-action and Meshy-rig inspection reports were reviewed. The installed vanilla infantry entity/sound and tag-scoped voice precedents and offline entity/graphical wiki snapshots were consulted. No HOI4 MCP route covers this audio/model documentation surface; exposed focus/event/technology/weighted/GUI/map routes were not invoked as unrelated evidence.

Meaningful checks not completed: no listening review, independent qubodup underlying-source audit, five-file legacy specialized-wrapper derivation reconstruction, observed contact-frame comparison, or live-game consumer validation. Those limits prevent an audio-complete or in-game-complete claim. No model or audio simplification was introduced by this documentation patch.

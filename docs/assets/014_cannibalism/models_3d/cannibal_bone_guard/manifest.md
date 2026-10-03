# Cannibal Bone Guard 3D manifest — CURRENT reconciled record

Record status: `needs_user_review`. This is a new current reconciliation based on the interrupted partial manifest, not a recovered historical JSON record.

## Package and consumer

Event 014 `cannibalism`; asset `chaosx.event014.cannibal_bone_guard`; profile `humanoid_unit`.

Unit consumer: `common/units/014_cannibalism_irregular_infantry.txt#cannibal_bone_guard`.

Entity consumer: `gfx/entities/014_cannibalism_units.asset#cannibal_bone_guard_entity`; model registration: `gfx/entities/014_cannibalism_units.gfx`.

Runtime model folder: `gfx/models/units/014_cannibalism/cannibal_bone_guard/`.

## Accepted artwork and input selection

Recorded source: CMON / CoolMiniOrNot, *Um'Kator Warrior #3 for the Um'Kator Tribe, HATE board game*, source SHA-256 `DB4164F9435588C85672B51CE0F81AF4B47A950CE43686755FB6406D8F1D7F41`.

The source pages were recorded as `https://www.cmon.com/hate-the-um-kator-tribe/` and `https://patrickmasson.artstation.com/projects/m2zR1?album_id=36250`; retrieval is recorded as 2026-08-24.

The source is copyrighted/all rights reserved with no reuse or AI-use license recorded; the parent authorized this exact source hash in `reference_only_user_authorized` mode, as recorded in `refs/original/input_manifest.json` and `refs/prepared/rebuild_2026-09-25_source_and_inputs.md`.

The rebuild record says no explicit NoAI or no-derivatives restriction was found on the reviewed pages; that finding does not grant a license and remains separate from the exact-hash parent authorization.

The original source bytes are absent at the recorded source path, so this reconciliation cannot reverify that source hash.

Parent-approved separated inputs from 2026-09-25 are `refs/prepared/body/candidate_02.png` (item-free body, SHA-256 `B2493A5D71079261B301BEDE22D25DD0B3A91272721B0192453E9E7767B3F752`) and `refs/equipment/poleaxe/meshy_input.png` (poleaxe-only item, SHA-256 `F464391AF83A97FC256D6FE1F8E248FB1B41D4E9191A571EDEFA68E5D89CF0FC`).

The rebuild record preserves source-to-prepared comparison notes and reconstructed prompt summaries, not verbatim native ImageGen prompts.

`refs/original/meshy_input.png` (SHA-256 `1CE0692A404194C80358CE5B05A5CC1BBCED8E48328D1EE4CB0245084A64F74A`) is an older approved one-image input and is superseded as a body input by the later separated body/item approvals.

`refs/processing_manifest.md` records a different source and input hash and is retained as a conflicting historical record; it is not the selected source record.

The unrelated Vornyx *The Bone Hunter* research is not selected.

## Provider and export lineage

`job.yaml` still records recovery-v6 as in progress and names generation task `01a033f3-60c4-77a8-ad80-3f667b277422` from the superseded one-image input.

The selected recovery-v6 GLB recorded by the job and provider history is absent at `provider/downloads/generation_recovery_v6_retry3_weapon_model.glb` (recorded SHA-256 `8A79DA3C164F42167F6E1F0A6A9ED8F0548F67C04020012FFEDABDFFD8829A7C`); the recorded rig source GLB is also absent.

The package retains `provider/downloads/cannibal_bone_guard_body_meshy7.glb` (SHA-256 `8CE1F66504AADF9C2BB635A06B28354BE06D970E27FBC7407C3C377BEAA70BC2`) without a recorded task id or a verified link to the selected export.

No poleaxe geometry task output or task id is retained, so the approved isolated item input is not linked to the exported assembly.

The export report names the absent recovery-v6 weapon-inclusive generation and rig inputs; the current job does not reconcile those sources with the 2026-09-25 separate inputs.

The recorded recovery-v6 paid operations total 94 credits; this manifest reconciliation incurred zero credits and zero Blender operations.

## Verified export-to-runtime bytes

The selected package export `exports/cannibal_bone_guard.mesh` and all eight named `.anim` exports were rehashed and match their installed runtime counterparts byte-for-byte.

The current mesh SHA-256 is `89C9BAC619A98753AC0D9510A51E3B8ABDAA371A26A3F9ED767D74083937ACC0`.

All eight provider action-import receipts match the provider action manifest's task/action references and source SHA-256 values; the reconciliation evidence records each task id, source hash, receipt hash, runtime path/hash, and reimport report hash.

The runtime binding receipt decodes one mesh node `mesh.001`, 24 bones, and eight actions at 30 FPS with matching bone order.

The source action manifest records 24 FPS and remains marked pending visual/export/reimport gates; that status and the later runtime audit are both retained as distinct records.

The retained 2026-08-22 toolchain receipt records Blender 5.1.2 build `ec6e62d40fa9`, adapter `chaosx_blender_hoi4` 1.8.1, Blender add-on 1.0.0, and `io_pdx_mesh` 0.91.0 with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

A later recovery report references adapter 1.10.7, while the selected export report does not bind its output to an adapter version; no current toolchain or health verification was performed during this metadata-only reconciliation.

## Materials, audio, and counters

The installed diffuse, normal, and specular DDS files each match the retained texture-receipt hash; their processed DDS bytes are absent from the job root, so only receipt-to-runtime hash equality is verified.

Six derived audio files match six unique installed per-unit WAVs: idle vocal, movement, weapon swing, impact, training exertion, and death.

The seventh derived selection/acknowledgement WAV is recorded for the country/original-tag voice consumer and has no matching per-unit path in the named runtime audit.

Audio attribution, source URLs, licenses, original and derived hashes, transformations, and proposed synchronization points remain in `evidence/audio_sources/provenance_manifest.json` and `ffprobe_and_hash_receipt.json`.

The large, on-map, and texticon counter DDS files rehash to the listed package hashes and are linked from `event014_cannibal_counter_art_handoff.md`; visual/live consumer review is pending.

## Calibration, action, and review status

The vanilla reference is `western_european_infantry.mesh#polySurface106` with `infantry_rifle_entity` scale `0.8`, source height `7.351824797689915 m`, effective runtime height `5.881459838151932 m`, forward `-Y`, and up `+Z`.

The export report records height `7.355273246765137 m`, a `0.0034484490752220154 m` delta, 30,000 triangles, 14,934 checkpoint vertices, zero reported boundary/non-manifold/degenerate findings, and no exporter warnings.

The grounded attack reimport report separately records 23,957 export vertices and 16,444 raw loose boundary edges across 745 components, while its position-weld diagnostic reports zero loose boundary and non-manifold edges; interpretation remains unresolved.

No visual action/contact acceptance or live in-game consumer review is inferred from these hashes or reports.

The complete one-package hash ledger, report paths, task/action lineage, and explicit gaps are in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_cannibal_bone_guard_manifest_reconciliation.json`.

## Reconciliation scope

No Meshy call, balance check, API-key check, Blender/adapter operation, geometry/rig/weight/key edit, export/reimport operation, runtime asset/wiring edit, or game launch was performed.

The event resume scope remains nine gameplay families and seven bespoke model packages, with the parent-approved cavalry/infantry reuse and no animation toggle; this single-package manifest does not change that scope or claim event completion.

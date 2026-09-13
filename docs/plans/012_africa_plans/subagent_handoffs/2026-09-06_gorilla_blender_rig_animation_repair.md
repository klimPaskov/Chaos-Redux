# Gorilla Blender repair: final 3D handoff

Status: 3D repair exported and reimported; parent runtime promotion and inherited sound/counter acceptance remain pending.
The user authorized direct repair of the existing body, a separately modeled hammer, all missing required components, and five genuine skeletal roles.
GPT-6-astra performed manual rigging, skin repair, component modeling, and animation through the locked repository Blender adapter.
No Meshy operations, new body, paid credits, runtime edits, or in-game completion claims are part of this handoff.

## Authoritative selected files

The job root is `docs/assets/012_africa/models_3d/gorilla_heavy_infantry`; asset paths below are job-relative.
`runtime_copy_manifest_20260908.json` is the exact nine-file source-to-runtime copy contract, including SHA-256, bytes, stream/material rows, action IDs, frame crosswalks, and pending parent copy status.
Final editable export source: `blender/checkpoints/77_export_mesh_br39.blend`, SHA-256 `450EDC718D509AA97BC54DB147AE57AA6649AABC41AF422C4D782BFAF09ECB46`.
Final mesh, five animations, and three DDS maps: `export/20260908_blender_repair/`.
All previous checkpoints, failed native receipts, original textures, and prior source/reference history remain preserved.

## Source and repair lineage

Protected provider source SHA-256: `F2ED6FFCAD8A86C0AB780D2063BD68574A7AFA1246A02D2AAB8A7521A6E45CA3`.
The repair begins from preserved `11_runtime_candidate_sanitized.blend`, SHA-256 `B5CB4FB0A82E8B5CB1814D0AED137A8310F9900D54D4025581A9130205A4456E`; its old elephant-derived hierarchy and empty hands were rejected.
The approved existing-body lineage is historical Meshy 6 geometry; the separate approved Meshy 7 reference history in `manifest.md` is provenance, not a newly generated body.
Checkpoint 51 contains the measured 29-bone rig and 196-triangle hammer.
Checkpoint 60 applies exact adjacency-smoothed weights to 12,194 retained body vertices with at most four influences, preserving positions and UVs.
The overhead stretch audit found maximum3.5688, p99 1.5173, and no edges above5; native views confirm the armpit sheet is gone.
Checkpoints 61–67 preserve distinct idle, move, hammer attack, recovery, and articulated death actions.
The parent accepted the source overhead attack and death impact/settle silhouettes.
Checkpoint 70 applies exactly 2,503 reviewed face orientation changes; the parent-approved job-only 0.5-degree bound admits measured native normal encoding drift 0.493285626 degrees, unchanged after reopen.
Default adapter tolerance remains 0.25 degrees; this is recorded serialization tolerance, not a broad normal reset.
Native patches 71–74 remove 215 exact conflict/duplicate faces and close 234 reviewed local loops.
Three flat isolated caps rejected by native face creation were replaced by shallow explicit weighted closures offset 0.00258–0.00455 source units; the final v2 plan is `evidence/blender_repair_20260906/exact_topology_patches_v2.json`.
Checkpoint 75 binds preserved-resolution 2048 PDX maps, and 76b divides only polygon material assignments into identical export batches.

## Final geometry, materials, scale, and skin

The assembled mesh has 24,852 triangles: 24,656 body and 196 hammer.
Native source has zero boundary edges, non-manifold edges, degenerate faces, or zero-length normals.
Actual-byte reimport has expected UV/normal split vertices; its diagnostic positional weld restores zero true boundaries and non-manifold edges without editing exported seams.
The 29-bone measured rig has no zero-weight body vertices, at most four body influences, and every hammer vertex weighted 1.0 to `hammer_R`.
The body remains 10.147683 source units high; entity scale 1.0 is applied once.
The named vanilla comparison is `refs/vanilla/asian_infantry.mesh`, source height 7.516803, `asian_gfx_infantry_entity` scale 0.8, effective height 6.0134424.
No arbitrary human-height scale or repeated entity scaling is used.
The diffuse DDS is byte-identical to the retained approved diffuse.
The normal map uses PDX RRxG channels; specular is RGB specular/metallic with alpha gloss derived from immutable provider roughness, not the prior uniform 255 alpha.
`textures/20260908_repair/copy_provenance.json`, `dds_validation.json`, and export `dds_copy_provenance.json` retain exact map lineage and hashes.

| Runtime meshsettings name | index | vertices | triangles | index entries |
|---|---:|---:|---:|---:|
| `Mesh_0.003` | 0 | 24910 | 20000 | 60000 |
| `Mesh_0.003` | 1 | 6797 | 4656 | 13968 |
| `Gorilla_Hammer` | 0 | 546 | 196 | 588 |

All three rows use `PdxMeshAdvanced` and exact filenames `chaosx_gorilla_heavy_infantry_br29_diffuse.dds`, `chaosx_gorilla_heavy_infantry_br29_specular.dds`, and `chaosx_gorilla_heavy_infantry_br29_normal.dds`.
Export maximum stream count is 24,910 vertices and 60,000 triangle-index entries, below the conservative 65,535 limits.

## Five roles and sound synchronization

| Role | Selected source action | Source frames | Reimport frames | Runtime behavior |
|---|---|---|---|---|
| idle | `gorilla_idle_br29` | 0–60 | 1–61 | loop |
| move | `gorilla_move_br29` | 0–48 | 1–49 | loop |
| attack | `gorilla_attack_br29` | 0–60 | 1–61 | one-shot |
| recovery | `gorilla_recovery_br29` | 0–60 | 1–61 | loop |
| death | `gorilla_death_contact_br33` | 0–60 | 1–61 | one-shot |

Every role is 30 FPS and retains genuine bone articulation; no static pose aliases or whole-rig-only motion substitute for a role.
Attack is a closed authored cycle but the existing attack/defend/support_attack consumers play it once and return to idle.
Recovery loops for the existing training consumer.
Death is terminal and non-looping: parent must remove inherited `next_state = idle`.
Cue time is `(source_frame - source_frame_start) / fps`; reimport frame equals source-relative frame plus 1.
Hammer impact is source 30, reimport 31, time 1.0 seconds; overhead is source 22/reimport 23/time 0.733333; recoil source 36/reimport 37/time 1.2.
Movement contacts are source 0/reimport 1/time 0.0 and source 24/reimport 25/time 0.8; cycle endpoint source 48/reimport 49/time 1.6.
Recovery grip check is source 30/reimport 31/time 1.0.
Death collapse is source 36/reimport 37/time 1.2, impact source 48/reimport 49/time 1.6, and settle source 60/reimport 61/time 2.0.
The copy manifest contains every phase crosswalk; do not apply a blanket `(frame-1)/fps` to source frame labels.

## Actual-byte proof and contact reconciliation

Five `.anim` exports and the assembled `.mesh` exported without warnings, with unit rig scales and no translation/scale normalization changes.
Each role was actually reimported with `stage_default_textures=false`, retaining the exact selected 2048 DDS bytes.
Each reimport samples five phases and renders front, left, and three-quarter views; source authoring also measured every frame for ground correction.
The 25 actual-byte sampled ground clearances span 0.000996796–0.001000911 source units around the intended 0.001 offset.
Key views: `reimport_gorilla_br39_idle_frame_001_three_quarter.png`, `reimport_gorilla_br39_move_frame_013_three_quarter.png`, `reimport_gorilla_br39_attack_frame_031_three_quarter.png`, `reimport_gorilla_br39_recovery_frame_031_three_quarter.png`, and `reimport_gorilla_br39_death_frame_061_three_quarter.png`, all under `blender/previews/`.
Actual-byte overhead 23 has original and opaque-clay culling-on proof at `gorilla_br39_reimport_overhead23_*_three_quarter.png`; the closed shoulder/arm and held hammer remain coherent.
The parent noticed a floating-body impression in the death left view and requested region-level reconciliation before promotion.
Native read-only inspection measured 328 exported seam vertices mapping exactly to 151 unique source 67 body vertices, with maximum source-to-reimport support displacement 2.176e-6.
Actual QA plane is Z 0.000998974, explicitly the evaluated global minimum used by the renderer.
Head clearance is 0.01848555 above that plane and pelvis clearance 0; within 0.05 are 6 head and 13 pelvis vertices, and within 0.2 are 59 head, 47 pelvis, 45 other body vertices.
These counts match the accepted source exactly and span World Y−5.18325 to 0.02928, proving separate head/pelvis support regions rather than one isolated lowest point.
The parent accepted this reconciliation without changing the pose.
Soft-shadow/framing can still suggest hovering in the side preview; not every limb contacts the floor, and this limitation is not hidden.
Detailed evidence: `evidence/blender_repair_20260906/death_support_reconciliation.json` and `.svg`, including exact native receipts and source/reimport frame crosswalk.

## Parent work and companion status

The parent owns the nine runtime copies, three Gorilla-only meshsettings rows, existing animation/state aliases, terminal death fix, sound timing, and commit.
Existing sourced-audio provenance remains in `audio/manifest.md` and `validation/audio_revalidation_2026-08-24.md`; its recorded pcm_f32le conversion and action-sync acceptance remain explicitly parent-owned.
Existing bespoke counters and exact vanilla comparison remain in `counters/` and `validation/counter_revalidation_2026-08-24.md`; the inherited chroma-key-route review status is not silently promoted.
No new audio or counter assets were generated by this bounded repair.
No required 3D component or role was omitted; parent runtime integration and companion acceptance are explicit remaining package work.
No live-game validation was performed or claimed.

## Tool and dependency evidence

Blender 5.1.2 build `ec6e62d40fa9`, checksum-locked io_pdx_mesh 0.91.0, final export/reimport adapter 1.10.39.
`evidence/blender_repair_20260906/final_dependency_snapshot.json` records the final lock and SHA; each native receipt records its actual adapter version and request ID.
The stdio transport lost two successful responses; partition 76b and move reimport were recovered from their exact native receipts and artifact hashes without rerunning mutations.
Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
Required offline wiki, vanilla model/entity/shader documentation, locked routes, and source job were consulted.
Costs: zero new provider calls and zero credits.

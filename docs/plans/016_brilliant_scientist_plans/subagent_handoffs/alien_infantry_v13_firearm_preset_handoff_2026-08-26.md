# Alien infantry V13 Meshy firearm-preset handoff

Status: the bounded 3D package and its static runtime promotion are complete through actual-byte PDX export/reimport. The accepted output is a textured 59,999-triangle alien infantry mesh with its Meshy-authored 24-bone rig and seven distinct Meshy preset actions, including a genuine firearm sequence and a complete collapse death. The promoted entity/GFX/animation/sound references are source-level evidence only; the effect locator, strict audio-role gaps, live consumer validation, and live in-game acceptance remain parent-owned or explicitly unresolved.

The detailed immutable package manifest is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`. Machine-readable provider lineage is beside it in `provider_lineage.json`.

## Routing and ownership

This V13 package is routed through `chaosx_3d_model_pipeline`. Provider output and provider hashes remain evidence under `docs/assets`, while static runtime registration and final live-consumer acceptance are separate parent-owned gates.

## Accepted runtime candidates

- Mesh: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh`, SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`.
- Actions: `alien_infantry_idle.anim`, `alien_infantry_move.anim`, `alien_infantry_laser_attack.anim`, `alien_infantry_defend.anim`, `alien_infantry_support_attack.anim`, `alien_infantry_retreat.anim`, and `alien_infantry_death.anim` in the same export folder. Their exact hashes and provider action/task IDs are in the final manifest.
- Textures: `alien_infantry_v13_diffuse.dds`, `alien_infantry_v13_normal.dds`, and packed `alien_infantry_v13_specular.dds` in the same export folder. The packed map uses R=0, G=32, B=provider metallic scaled to 0.35, and A=provider roughness; it is not raw grayscale roughness masquerading as a specular map.

## Source, cost, and recovery record

- The only provider image was the user-approved `meshy_input_v13_tpose_right_pointing_colored.png`, SHA-256 `2D72EEB020C8989B463F214D4B5FC1C29C4AB313AEEE9F033B71E6DE1881BF3A`.
- Meshy 7 task `01a03dbc-7913-7257-961a-56dea6cf6b04` was rejected because it omitted the pistol; its files remain preserved. Recovery task `01a03dc3-905a-7d02-aba6-05500f877b97` retained the integrated pistol and was accepted.
- Remesh task: `01a03dc9-8951-79ad-bc08-ae94ad607dfe`; rig task: `01a03dcf-f0ba-7b67-b769-5a2678b03a40`.
- Seven animation task IDs and action IDs are recorded in the final manifest. No role aliases or static/manual replacement clips were used.
- Paid operations consumed 91 credits: two 30-credit generations, one 5-credit remesh, one 5-credit rig, and seven 3-credit preset actions. Balance was 103 before work and 12 after work.
- One local 99,857-triangle PDX export failed because exporter stream expansion produced 86,556 vertices, above the 65,535 limit. The rejected checkpoint/log was preserved. A bounded working-duplicate decimation to 59,999 triangles produced a 59,451-vertex stream and exported successfully; no additional provider spend was required.

## Validation result

- Calibration mirrors `western_european_infantry.mesh` and `units_infantry.asset#infantry_rifle_entity`: source height 7.3518242835, entity scale 0.8 once, effective runtime height 5.8814594268, forward -Y, up +Z. Final mesh source height is 7.3518023491.
- Final reimport inspection found 59,999 triangles, no degenerate faces, no negative-scale objects, and no zero-length normals. Provider rig inspection found 24 bones and no zero-weight deforming vertices.
- `laser_attack` visibly performs draw, aim, discharge, recoil, and recovery. The right hand retains its grip, the left hand makes legitimate support contact during firing, and the muzzle continues to point away from the body.
- `support_attack` is a separate advancing-fire motion. Idle, move, defend, retreat, and death are distinct provider actions. Death visibly reacts, collapses backward, impacts the ground, and settles.
- Each final `.anim` was reimported from its actual bytes with the final `.mesh`; all seven roles have proof blends, JSON reports, and multi-frame preview evidence under the job root.

## Audio and counter status

- CC0 source packages exist for laser discharge, movement, idle, and death with source pages, direct-download URLs, authors, licenses, original/derived hashes, and transformations in `evidence/audio/provenance/audio_sources.json`.
- Proposed sync: laser discharge frame 145 / 4.800 seconds; support fire frame 50 / 1.633 seconds; move contacts frames 1 and 19; retreat contacts frames 1 and 16; death onset frame 1 and future impact near frame 80 / 2.633 seconds. The promoted entity contains corresponding static event references, but these timings do not prove positional playback or live acceptance.
- Selection/acknowledgement remains blocked because the nearest vanilla consumers are tag-wide. Distinct impact and special-action roles remain blocked because no defensible sourced candidates were accepted. No synthesized or placeholder audio was used.
- Existing bespoke vanilla-green counters are complete and preserved: large 152x42 two-frame DDS SHA-256 `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`; on-map 60x12 two-frame DDS SHA-256 `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`. Exact installed-vanilla definition/DDS/reference-family and palette evidence remain in `runtime/counter_handoff.md`.

## Parent-owned next steps and risks

- Review the byte-identical mesh, animations, DDS files, and static registrations promoted by commit `0e724fb8a`; do not point runtime consumers into `docs/assets`.
- Review the seven distinct semantic states in the promoted entity/asset without aliasing roles, verify entity scale 0.8 is applied exactly once, and review the proposed sound/effect timings.
- Resolve a runtime muzzle/effect point. No locator was created because the adapter lacks a locator-authoring operation and manual firearm attachment/parenting was forbidden. The cyan muzzle cap is only visual evidence of the effect location.
- Decide whether the explicit selection, impact, and special-audio blockers are acceptable or require a later licensed-source research tranche.
- Review the somewhat patchy provider surface highlights in the final material proofs at game camera distance. The PBR maps resolve and reimport, but live aesthetic acceptance is not claimed.
- Perform final entity/GFX/sound/gameplay review, resolve the supported effect-point route and strict audio-role gaps, and obtain user-owned live in-game validation. This handoff does not claim live runtime acceptance.

## Files changed by this finalization tranche

- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`, `crosswalk.md`, and `sound_handoff.md`.
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/alien_infantry_v13_firearm_preset_handoff_2026-08-26.md`.

The full V13 production tranche additionally created the provider downloads, texture working files, Blender checkpoints/previews/reports, final `.mesh`/`.anim`/DDS exports, validation JSON, adapter logs, and provenance records enumerated by the attempt manifest and job tree. No gameplay, entity, GFX, sound-definition, localisation, event, focus, decision, or spreadsheet file was edited by this worker.

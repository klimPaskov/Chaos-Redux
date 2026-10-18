# Clone infantry arm repair — 18 October 2026

Status: incomplete; continuity correction staged, no runtime installation.
The reported long arm/plank has not been reproduced or conclusively explained by the installed-byte inspection.
Do not describe this package as the completed arm repair or as validated in game.
The movement acceptance check also remains failed, so the staged package is not approved for wholesale installation.

## Scope and source

Job: `models_1018_clone`.
Job root: `docs/assets/shared_clone_system/models_3d/clone_infantry/`.
This report uses job-relative paths below unless explicitly prefixed by `gfx/`, `.tmp/`, or `docs/plans/`.
The owned hidden Blender Lab used port 9882 and PID 36320, Blender 5.2.2 LTS build `d13f752e3b9c`, with the locked Lab 1.0.3 and io_pdx_mesh 0.91 compatibility stack.
A second owned session, PID 39452 on the same port after the first exited, finished the read-only vanilla death framing review.
Both owned Blender processes were closed; the final process check is retained at `.tmp/models_1018/clone/final_process_closure.json`.
No other Blender port/process, HOI4 process, game settings, sibling model, gameplay script, unit definition, entity, sound definition, or runtime model was changed.
No commit was made.

The baseline mesh is `gfx/models/units/clone_infantry/clone_infantry.mesh`, SHA-256 `810e83f81c29c5833cb68dcbf04cf587d25a6c5fc0afd34a0fa47e33e70334b6`.
The active registration has four body streams under `mesh.001` and separate `CloneRifleWood`, `CloneRifleSteel`, `CloneRifleBolt`, and `CloneRifleSling` objects.
`gfx/entities/zz_clone_infantry_aryan.asset` inherits `GER_infantry_entity` and its snow/desert variants; it does not use the custom clone mesh, so it received no modification.
The WP4 clone report and the shared geometry/animation, texture, and audio evidence were consulted to preserve the existing assembly and sound timing.

## Findings and changes

The installed `.anim` files contain 25 adjacent quaternion sign discontinuities: attack 4, death 1, move 4, retreat 4, support attack 4, training 4, and wounded 4.
Affected arm channels include `RightHand`, `LeftUpperArm`, and `LeftHand`; locomotion also has thigh discontinuities.
Idle and defend have none.
This is a confirmed continuity defect, but its connection to the reported very long ground plank is unproven.

All nine actions have the same complete 44-bone ordering as the mesh, all five mesh skeletons are identical, every positively weighted bone index is valid, no vertex is unweighted, weights sum to one within approximately 4.5e-8, and all decoded animation scales are 1.
Initial transforms agree with first samples.
The rifle parts remain rigidly weighted to `RifleControl` or `RifleBolt`.
The body is one closed component; all five logical objects pass the current manifold, boundary, duplicate, degenerate, and winding checks.
The unused negative-index slots and floating-point reconstructed fourth-weight residuals also occur in inspected vanilla infantry and were not treated as proof of corruption.

The current shipped bytes were freshly imported into the isolated live Lab, preserving all actions as separate datablocks.
The maintained `normalize_quaternion_curve_signs` operation negated existing quaternion values and matching handles in that live session, without adding keys, changing their timing, changing any orientation at a keyed frame, or creating bones or weights.
Working-object and action-slot metadata were prepared for the adapter.
Seven actions were re-exported through the locked adapter; the maintained `review/anim_signs.py` corrected the exporter’s serialized q/-q branch changes.
The new selected bytes independently match the earlier interrupted job’s staged candidates exactly.
Their integer-frame translation differences from installed actions are below 0.000002 source units and orientation differences below 0.000060 degrees.
Idle, defend, the mesh, and all six DDS maps are byte-identical to runtime.
No replacement role motion was authored or ingested, so no new preset was substituted for the existing actions.

Selected candidate folder: `export/models_1018_current/selected/`.
Live source checkpoints: `blender/checkpoints/models_1018_current_shipped.blend`, `models_1018_current_continuous.blend`, and `models_1018_current_export.blend`.
Actual selected-byte proof checkpoint: `blender/checkpoints/models_1018_final_reimport.blend`.
The existing job-local `validation/animation_delivery_policy.json` was rebound to the current export checkpoint, retaining its roles, loop flags, and empty strike windows.
The previous policy is preserved at `export/models_1018_current/previous_delivery_policy.json`.
Scratch scripts and MCP receipts are under `.tmp/models_1018/clone/`; they are task-specific diagnostics, not shared tooling.

## Review evidence and limits

`evidence/models_1018/current_baseline/*_scan.json` and `final_reimport/*_scan.json` each cover 969 poses across all nine actions, including every integer and half frame, with object bounds and maximum rest-to-pose displacement for each dominant-bone region.
`evidence/models_1018/native_transition_probe.json` separately evaluates native PDX parent-local transforms and linear blend skinning for 969 poses and 2,070 transition samples, including bind-to-action and wounded transitions.
Its candidate hashes were checked against the fresh selected exports before reuse.
Transitions use shortest-hemisphere normalized quaternion interpolation as an explicitly offline approximation; this is not observed Clausewitz blending.
The maximum measured arm-region mesh edge is about 0.6951 source units during actions and 0.7802 during the sampled transitions; no sampled vertex escapes into a long ground plank.
Edge measurements use unique index pairs per stream, not deduplicated physical seam edges.
`evidence/models_1018/current_geometry.json`, `current_candidate_verification.json`, `unused_weight_probe.json`, `current_live_continuity.json`, and `final_delivery_audit.json` retain the detailed findings.

The parent model agent personally inspected the final reimport contact sheets:

- `evidence/models_1018/final_reimport_front_sheet.png`
- `evidence/models_1018/final_reimport_side_sheet.png`
- `evidence/models_1018/final_reimport_map_sheet.png`

They contain 135 actual selected-byte renders: nine roles, five phases each, three views each.
The map camera is approximately 53 degrees downward at a three-quarter angle.
The individual render paths are listed in `evidence/models_1018/final_reimport_review.json`.
The renders preserve the full body and rifle, show no runaway arm, show distinct port-arms/training and wounded motion, and show the death collapse and final lying pose.
Workbench diffuse previews establish geometry/pose visibility, not a new engine-material acceptance claim.
The baseline map sheet and the current-source wounded/attack front sheet were also personally reviewed.

Installed vanilla references were `GER_infantry.mesh` with `GER_infantry_idle_rifle.anim`, `GER_infantry_moving_rifle.anim`, `GER_infantry_attack_stand_rifle.anim`, and `GER_infantry_death_rifle.anim`.
The collision box was explicitly excluded from the corrected reference renders.
Their hashes and ranges are in `evidence/models_1018/vanilla_review.json`, and reviewed map/side comparisons are `vanilla_reference_visible_map_sheet.png` and `vanilla_reference_visible_side_sheet.png`.
The initial death framing clipped the final fall; widening the fixed camera was insufficient, so the final `vanilla_death_fitted/` views follow the evaluated reference-body bounds and retain those bounds and camera measurements in `framing.json`.
The fitted vanilla death side and map views were personally reviewed; the earlier clipped previews remain rejected evidence.
Vanilla sampled spans are 6.0 seconds idle, 1.333 seconds moving, 2.6 seconds standing attack, and 2.1 seconds death at 30 FPS; clone spans remain 2.0, 1.0, 2.5, and 2.5 seconds respectively at 24 FPS.
No timing or entity scale was changed to force a passing result.

After serialized sign cleanup, eight actions pass the decoded motion checks under the declared roles, and all nine have zero sign discontinuities.
Move still has 19 world-motion limit findings, with a maximum step of 0.387589 units against the tool’s 0.36-unit per-frame threshold, and zero qualifying stationary sole plants on either side under the retained contact test.
Different source FPS complicates a physical speed comparison, but neither the threshold nor the foot-plant failure was waived.
The move role therefore remains unaccepted; no complete gait repair is claimed.

## Runtime and timing

No source-to-runtime copy was performed.
All runtime filenames, mesh/action identifiers, state bindings, particles, locators, textures, and sound files remain unchanged.
The staged correction preserves the 24 FPS frame count and existing action timing, including attack discharge 0.75 seconds, support/defend discharge 1.0 second, cartridges at 1.5833/1.8333 seconds, and death impact at 1.5 seconds.
`evidence/models_1018/runtime_and_candidate_hashes.json` records installed and candidate SHA-256 values separately, with installation explicitly false.

## Candidate SHA-256

All paths in this table are under `export/models_1018_current/selected/`.

| Candidate file | SHA-256 |
|---|---|
| `clone_infantry_attack.anim` | `536c81e76f76edb3f827a4a339f5f977bbcd3f36ccd8324f584e133fc63a6b9f` |
| `clone_infantry_death.anim` | `7c7223a21ebfeae8715eab1162543f200c8aa76c9cc01431e4882d1703575df0` |
| `clone_infantry_move.anim` | `feafd4d9eb58d96f7e43dcdebc726c969d9e295c6d30eab641dcf31fa7c4ad63` |
| `clone_infantry_retreat.anim` | `55e7c4c559dcc32d1e75e3e587e62ccdce4fc33e11a0ea01628df46b791eaaf4` |
| `clone_infantry_support_attack.anim` | `0f3a10ab9f161a3d072c8751e29fed5f3875115cab1e4adb56232e65b8b99c24` |
| `clone_infantry_training.anim` | `52a5d3ff59a34d6708b28f20c7f4114096d76b40fd48b0ea39826fe903eeba31` |
| `clone_infantry_wounded.anim` | `ac6835d2daa4e9b5c727c35d8788413d94b04fec2f313b5cf028233b65f71b7e` |

`evidence/models_1018/file_hashes.json` supplies the complete per-path SHA-256 inventory for this job’s source checkpoints, policies, exports, render/measurement evidence, scratch scripts, adapter receipts, and this handoff.
It includes preserved interrupted-run artifacts with their original paths, without presenting them as independent new validation.
The index excludes its own bytes to avoid a self-referential digest.

## Provider, sounds, and counters

Provider task IDs created: none.
Meshy calls, including balance calls: zero.
Credits used: zero.
No sound was downloaded, generated, synthesized, recorded, processed, renamed, or installed.
Existing bespoke counters were retained under their existing handoff; no counter or unit-definition change was needed for this investigation.
Existing sound provenance remains in `audio/sound_design_handoff.md`, `audio/closure_20260912/`, `evidence/wp4_audio_takeover/`, and `sound/shared_clone_system/clone_infantry/WP4_ATTRIBUTION.md`.
Relevant preserved sources include the following:

| Role | Creator / source | Licence |
|---|---|---|
| Recorded Lee-Enfield rifle report | kyles, https://freesound.org/people/kyles/sounds/450851/ | CC0 1.0 |
| Body landing | leonelmail, https://freesound.org/people/leonelmail/sounds/504626/ | CC0 1.0 |
| Battlecry and wounded voices | kurt, https://opengameart.org/content/soldier-voice-acting | CC BY 3.0 |

These are retained attribution records, not claims of fresh source-page or listening verification.

## Tool and reference evidence

Blender Lab and HOI4 reference tools were absent from the connected tool inventory.
The repository’s locked Lab stdio wrapper was used with `BLENDER_MCP_HOST=127.0.0.1` and `BLENDER_MCP_PORT=9882`, with its live `execute_blender_code(code)` schema retained in `.tmp/models_1018/clone/current_lab_schema.json`.
The first read-only tools/list attempt hit the documented premature-stdin-EOF problem; one corrected SDK handshake succeeded, and no unchanged failed request was replayed.
`.tmp/models_1018/clone/current_environment.json` verifies the locked Blender-only dependencies with no findings and no Meshy probe.
The live source initially lacked the adapter’s `chaosx_working` selection metadata; the failed export produced no animation, its saved receipt was inspected, and a new metadata-only checkpoint corrected that input before the second export attempt.
Raw exported quaternion continuity refusals were addressed by the maintained sign-only cleanup and then rechecked on the actual selected bytes.
The movement findings remain unresolved.
The widened vanilla death review first hit a UTF-8 BOM parsing error; the corrected read uses `utf-8-sig` and reuses the already imported reference without replaying the import.

Local references read include offline `Entity modding - Hearts of Iron 4 Wiki.md` lines 24–183, the Graphical asset snapshot introduction, installed `gfx/entities/units_infantry.asset` lines 10–55, and installed `gfx/FX/pdxmesh.shader` lines 156–166, 236, and 279–307.
The installed documentation search found no dedicated skeleton/mesh format documentation; the installed shader and locked importer/exporter supplied the relevant concrete source rules.
Source hashes and the line spans are retained in `evidence/models_1018/reference_citations.json`.
Skills used: `chaos-redux-3d-model-pipeline` with its start, Blender/export, audio/counter, and unit-rebuild references; `chaos-redux-event-assets` for the preserved texture/DDS conventions.
No skill was modified.

## Remaining requirements

The original arm-plank root cause and its correction in installed runtime bytes remain unresolved.
The action or transition associated with the reported screenshot was requested through the pending clarification, because the supplied description does not identify it and the inspected offline states remain bounded.
The move role needs a proper accepted gait/contact repair before this staged package can meet the full requested quality bar.
No design fallback, placeholder, aliased role, generated motion, or speculative reweighting was shipped.
This is a documented partial investigation and source correction, not a completed repair.

## Parent review and installation (18 October 2026)

The parent installed the sign continuity correction for the seven affected actions, since the arm channels named above are where the user saw the stretched arm.
The worker's offline transition probe used shortest-hemisphere interpolation, which hides a serialized q/-q flip; the in-game blend between keys is not assumed to make the same correction, so a flip in `RightHand`, `LeftUpperArm`, or `LeftHand` can send the arm through a wrong rotation between those keys.
The installed bytes are the maintained `.tools/3d_pipeline/review/anim_signs.py` output applied directly to the previously shipped files, so only whole quaternion samples were negated and no key, bone, translation, or timing changed; the tool re-read each written file and reports zero negative-dot transitions.
The worker's re-exported candidates under `export/models_1018_current/selected/` were not installed because they also carry sub-micro translation differences from the re-export.
Idle, defend, the mesh, and the textures are unchanged.

| File | Before SHA-256 | Installed SHA-256 |
|---|---|---|
| `clone_infantry_attack.anim` | `6CB11C8141A9E8B5AC976FE7D1CF124B9D131BE9AA1BF6FC28FF8E24046FF33B` | `AF7B85EA6629021C62822855597E41954EB8903434927BF766121EB381E62926` |
| `clone_infantry_death.anim` | `2F3F44819868DA8C03585D23361CE478876C196082701BD28127BB3EDE8B7057` | `21A106746B513DFBADD59B00D71DA95B4431910092CE3468A5CE47DA2455CD63` |
| `clone_infantry_move.anim` | `E7C344069AF6EE39A84B4A93D156661234C073A5A6FB17FD414190380D1E5019` | `A1F6C8C8441A9EDF321AB6E27DADD05BAFEF5C20D91864741D484D06633EA65E` |
| `clone_infantry_retreat.anim` | `2E6B43FC7D650A417238042FFE9EE956360C46CE8E04E4B4F65B21D66E33BBE0` | `2019244CFE6DDF50B1D29A11392E58BD4C5E61DFE8483FBE1DA6A4687348DBCC` |
| `clone_infantry_support_attack.anim` | `F3D034696546B8FFA4BE4B84F5ACE38487A36A68684B39C522C06CB5E31A9D42` | `310DF92AD4719AEEDCC710429421274FA6E69EDD89002B3D72CEBC778B8E2684` |
| `clone_infantry_training.anim` | `EE9FEACD6CCF2CE8AA3AEEBFC002320306B7ECB71305BE24D0DC418D4EF8124B` | `3EF1BEF154D5C108E66DDAD72946FD0EDB0222E1AEAA74AA6FA7891B5F376D90` |
| `clone_infantry_wounded.anim` | `86101E24B2652F95B1F199796C224BCB6B40CAF5EC47F2122CC17704BA3D4F4B` | `85A2A7A34E77FD74F67D8410277139F4165371C238A72376B6AFB4B1812F4323` |

The link between the flips and the in-game plank is the strongest remaining explanation, not an observed result; the user's next session is the check. The move foot-plant finding above stays open.

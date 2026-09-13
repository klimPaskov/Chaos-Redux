# Temporal Guard existing-model repair

## Sourced audio repair follow-up, 2026-09-08

Nine concrete WAV cues are prepared under the job's `audio/final/20260908`.
Read `audio_manifest.json`, `gfx_sound_handoff.md` and `ATTRIBUTION.md` there for exact source/copy hashes, licenses and animation-event times.
A physical clock recording replaces the rejected square-wave candidate; two isolated sourced boots serve move and retreat under parent approval.
Metallic contact/death and recorded electrical cues fit their motion phases; all cues are mono 44.1 kHz signed 16-bit PCM with zero clipped samples.
Four missing usable originals were restored byte-identically to historical hashes, and the new clock original is preserved.
This supersedes the missing retreat source and unsuitable ambient-source gaps in historical sections below.
Per-subunit selection/acknowledgement remains blocked under mixed owner tags; no global voice replacement is authorized.
Parent auditory review remains pending because this runtime cannot consume audio input; waveform checks do not claim listening review.
No Blender, provider or runtime edits occurred; zero credits.

Status: action repair implemented and exported/reimported; common mesh topology/material repair remains in progress.
This is a working handoff and does not approve runtime replacement yet.

## Authority and ownership

The parent accepted direct Blender repair under `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the current user authorization to repair faulty/missing rigs/actions and restore required physical elements.
The unit is a non-firing, unarmed temporal guard.
No separate firearm, weapon, or held tool is required by the inherited model reference.
Its dark iron/bronze armor, helmet, clock core, cyan conduits, gauntlets, hip plates, and boots remain the intended identity.
The parent explicitly accepted bounded reconstruction of the measured malformed inner-thigh patch, with culling-on before/after review and preservation of unaffected UVs, weights, rig, and actions.

The worker owns only `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/` and this handoff.
The parent owns runtime copying, GFX/entity/sound wiring, final source selection, and commit.
No runtime files were edited by this worker and no in-game completion is claimed.

## Source, route, and scale

The selected existing source is `blender/checkpoints/06_runtime_base.blend`, SHA-256 `A4767A97A200636A13EC9C13F06DE0478537CEF8867DD9DB021FC4B5917117CC`.
It preserves the original hidden provider objects and the working `char1.001` / `Armature.001` pair with 24 bones and eight existing actions.
The older manual recovery candidate is preserved as historical evidence.
The current source mesh has 14,997 vertices and 30,000 triangles, normalized weights on every working vertex, and at most four influences per vertex.
The source rig is retained; no replacement rig was necessary for the two missing/faulty semantic roles.

Blender is 5.1.2, build `ec6e62d40fa9`, with checksum-locked io_pdx_mesh 0.91.0.
The archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
Initial evidence used adapter 1.10.21; measured action authoring and first exports/reimports used 1.10.22; later bounded inspection used the parent-published 1.10.24 route.
Versioned live tool schemas, source checks, dependency-lock hashes, wrapper lifecycle receipts, and a separate listening socket probe at `127.0.0.1:9876` are in `evidence/20260906_repair/dependency_preflight*.json` and `live_tools*.json`.
The job helper refuses every call while shared adapter sources differ from their lock.
All Blender operations used the verified structured adapter; no unrestricted Blender Python was used.
Technology Tree Viewer availability is outside this model-only task and remains unverified, as directed by the parent.

The installed precedent is `gfx/models/units/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`.
The selected vanilla render body is `polySurface106`; collision-only `pCube1` is excluded.
Vanilla source height is `7.351824797689915`, and `gfx/entities/units_infantry.asset` sets the infantry entity scale to `0.8`, giving effective runtime height `5.881459838151932`.
The custom source height is `7.3518242835998535`; its axes remain +Z up and -Y forward, with the same entity scale applied once.
Source armature scale `0.01000000350177288` is baked into armature data and local translation channels once by the export adapter; exported bone scales are normalized to one.
Exact vanilla mesh/entity/GFX/shader/counter hashes are in `evidence/20260906_repair/current_reference_and_audio_checks.json`.

## Actions and actual-byte proof

The eight existing role binaries remain byte-identical and are copied into `export/20260906_repair/anim/` with a copy ledger.
The new support and retreat clips use explicitly authored measured bone phases, with genuine shoulder, elbow, wrist, spine, hip, knee, and ankle motion as applicable.
The numeric planning script writes declarative requests only and never runs Blender code.

| Role | Frames at 24 FPS | Source/disposition | Root/loop policy |
|---|---:|---|---|
| idle | 1-97 | Existing role retained | Existing in-place loop |
| move | 1-32 | Existing role retained | Existing in-place gait loop |
| attack | 1-60 | Existing melee role retained | Existing guard/strike/recovery loop; no firing |
| defend | 1-84 | Existing guard role retained | Existing in-place loop |
| entrain | 1-40 | Existing compressed stance retained | Existing in-place loop |
| death | 1-53 | Existing articulated collapse retained | Non-looping collapse, impact, and settling |
| temporal_anchor | 1-65 | Existing brace/anchor gesture retained | Existing in-place loop |
| synchronization | 1-104 | Existing coordinated arm gesture retained | Existing in-place loop |
| support_attack | 1-49 | Dedicated manual GPT-6-astra action | Both ankles planted; pulse and guard recovery; exact loop endpoints |
| retreat | 1-49 | Dedicated manual GPT-6-astra action | Backward stance/swing trajectories; raised forearms; exact loop endpoints |

Support phases are guard 1, draw 10, charge 18, pulse 26, aftershock 32, retract 42, guard return 49.
The left gauntlet protects the temporal core while the right palm extends from Y=-1.029 to Y=-2.084 at the pulse.
Both ankle positions stay fixed in the authored support phase measurements.
Retreat alternates left/right plants at frames 1/25/49, with swing reaches at 13/37 and 0.24 source-unit peak ankle lift.
Its intended stance sweep is 0.96 source units per second toward -Y relative to the stationary body, representing backward +Y locomotion when the parent binds movement.

The first support binary is `export/20260906_repair/anim/chaosx_temporal_guard_support_attack.anim`, 25,035 bytes, SHA-256 `4733FB4DAE6C335AE9063BDC81EB9D891C62A688D975C8FB45A664D0690528A4`.
The first retreat binary is `export/20260906_repair/anim/chaosx_temporal_guard_retreat.anim`, 38,781 bytes, SHA-256 `8D62D4BD2D8C9DE3C8AF50F58348166D77643B6D713661FDF5DADAD4668BD017`.
They reimported through the locked extension against the existing common skeleton with exact matching first/last bounds.
Sampled reimport ground Z is -0.00000177 for support and 0.00099727-0.00100352 for retreat.
The source and actual-byte reimport contact sheet is `evidence/20260906_repair/authored_motion_reimport_before_surface.jpg`.
These proofs establish motion survival; final repaired-surface deformation/reimport review remains pending.

Editable candidates are `blender/checkpoints/tg26_support_attack_v1.blend`, `tg26_retreat_v1.blend`, and the combined `tg26_actions_v1.blend`.
The detailed phase keys, source/native action hashes, FPS, root/contact measurements, request IDs, and proposed bindings are in `evidence/20260906_repair/action_crosswalk_candidate.json` and the `author_*.request.json` / `*.result.json` records.

## Surface and material repair

The source has 630 inconsistent shared edges across 920 incident faces.
Both rest and posed reimports have visible missing surfaces with backface culling enabled, including with neutral diagnostic normal/specular maps and diffuse alpha uniformly 255.
This is a measured topology defect.
A coherent orientation solve identifies an additional tiny nonorientable inner-thigh feature.
The parent-approved local reconstruction consists of the 66 exact source faces recorded in `evidence/20260906_repair/inner_thigh_patch_diagnostic.json`, within the measured centroid AABB `[0.30,-0.40,2.79]` to `[0.41,-0.24,2.96]`.
The source has ten small boundary loops totaling 38 edges, including the small hole inside that local patch.
The exact malformed faces, boundary loops, and proposed orientation diagnostics are preserved separately; no full surface repair is claimed yet.
Stored corner normals follow the existing geometric winding in both sampled flipped and unflipped regions, supporting paired winding/normal correction.

The source preview material wires packed specular RGB directly to Roughness and the packed normal as a conventional normal texture.
The installed `gfx/FX/pdxmesh.shader:478` uses specular alpha as glossiness.
The derived engine material candidate packs RGBA `(0,32,source metallic,255-source roughness)` after independently resizing scalar channels to 1024.
The packed normal preserves `(0,source normal R,0,source normal G)`.
The official DDS converter was used, and decoded pixels match the packed PNG bytes exactly.
The pinned importer links specular alpha directly to Blender Roughness; a fixed preview node correction must invert it without changing engine pixels.

Candidate runtime maps are `textures/20260906_repair/runtime/chaosx_temporal_guard_diff.dds`, `chaosx_temporal_guard_normal.dds`, and `chaosx_temporal_guard_spec.dds`, all 1024-square legacy BGRA DDS.
The diffuse is byte-identical to the preserved existing diffuse.
The new normal SHA-256 is `77A342BF40D9C65A36F74829EFA94A174C634AD5341C72E16A85CF0360EB805A`.
The engine specular SHA-256 is `A482D6BACACE80C23EA97E36849B2F79118EC59D5A2501F4057905835F1B64AE`.
Uniquely named copies are staged next to the proposed final mesh under `export/20260906_repair/mesh/`.
Diagnostic neutral maps and earlier alpha-as-roughness candidate maps are not runtime selections.

## Sound, counters, and historical provenance

All six sourced derived WAVs and their originals remain unchanged.
Their inspected source pages, creators, licenses, transformations, hashes, and proposed sound ids remain in `audio/provenance.md`; current file-format/hash checks are in `current_reference_and_audio_checks.json`.
No audio was synthesized, recorded, generated, or newly sourced for this repair.
The support temporal-special cue should align to pulse frame 26, at `(26-1)/24 = 1.041667` seconds.
Retreat footfall candidates align to the alternating plants at frames 1 and 25, at 0 and 1 seconds, with the next loop at 2 seconds.
Other inherited timings remain attack/contact 30, temporal anchor 44, synchronization 52, and death impact 36 with its settling tail through 53.
Parent retains exact event-marker, loop-boundary, selection/acknowledgement consumer, attribution, and sound-definition review.

The old job-local counter brief is superseded by the parent-reviewed `016_final_generic_counter_completion_2026-09-01.md`.
The accepted bespoke counter outputs remain unchanged and their current hashes match that receipt.
The installed large infantry strip is 152x42 with two 76x42 frames; the on-map strip is 60x12 with two 30x12 frames, from `interface/subuniticons.gfx` and the exact installed infantry DDS files.
Tokens are `GFX_group_temporal_guard_icon`, `GFX_unit_temporal_guard_icon_medium`, and `GFX_unit_temporal_guard_icon_medium_white`, registered in `interface/016_brilliant_scientist_generic_counters.gfx`.
The inspected reference families and green palette are recorded in `counters/gfx_handoff.md` and the current reference receipt.
No vanilla counter was relabeled as original art.
The large runtime DDS is `gfx/interface/counters/divisions_large/unit_temporal_guard_icon.dds`, SHA-256 `50622212016AC090ADD2D076E3E0B40896B932BCDA6A124083D0B1D0DDBF7C78`.
The on-map runtime DDS is `gfx/interface/counters/divisions_small/onmap_unit_temporal_guard_icon.dds`, SHA-256 `995FF164E56AA3BBA23315203EBFA8D72CBCCF92D74F66485D718BA42BAFF8D7`.
Original and processed PNGs, exact prompts, contact-sheet comparison, and DDS roundtrip evidence are retained under `docs/assets/016_brilliant_scientist/generic_counter_package/`.
The inherited selection/ambient square-wave hum still needs source-role acceptance; its public-domain status does not waive the ban on primitive-waveform final audio.
The older visual handoff also records a missing distinct retreat cue; reusing the sourced footstep recording with the revised retreat markers remains a parent sound-design decision, not an invented new sound.

The inherited input image SHA-256 is `F3D705EC5C7E8BF23F1BB74B3AE5E2D3DD50669ACC9A1463437319B7FEAF87D4`; the source image is `B704CC7286C3F76DC20A80D9DDEF44EADE350DA535E35B9DA64D02246A03F4DC`.
Source URL/title/creator/terms, original retrieval and explicit artwork authorization, exact ImageGen prompt/receipt, and approval remain absent from the inherited records.
Historical Meshy lineage is generation `01a0427c-4e13-7b24-a0c4-56b4e1288288`, abbreviated local remesh `remesh_01a04281`, and rig `01a04284-b375-7973-909c-8abd29417e11`; the complete remesh id and old credit reconciliation remain missing.
Those records are not fabricated or retroactively approved by this repair.
This Blender-only repair used no Meshy calls, no key/balance gate, and zero estimated or consumed credits.

## Remaining work and evidence limits

The common mesh still needs the approved localized reconstruction, outward winding, fixed packed-material preview binding, culling-on before/after silhouette comparison, and actual-byte reimport of all ten selected roles.
The final mesh must retain the original rest binding and vanilla calibration for the eight byte-identical existing actions.
The combined editable checkpoint must contain the corrected geometry/materials and all required actions before final selection.
The historical provenance, complete remesh/credit receipts, selection/ambient source-role review, and retreat sound-role selection remain explicit package gaps, independent of the repair work.
The exact per-subunit selection/acknowledgement consumer is an engine limitation to document when unsupported, with global voices preserved.
No requested role has been replaced by a semantic alias or static asset.
No live-game validation was performed.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
Shared adapter changes are parent/adapter-worker owned; this worker did not edit tooling, config, or lock files.

## Selected physical repair, 2026-09-08

Disposition: implemented physical reconstruction and export; final action proof inventory is `evidence/20260906_repair/final_repair_manifest.json` when present.
This section supersedes the earlier adapter-image blocker and pending physical-repair statements above; historical provenance and audio limitations remain explicitly open.
The parent accepted the V2 original-material three-quarter view and culling coverage, original06 rest binding, and exact replay of the two accepted action specifications onto the repaired eight-action base.

The authoritative source is `blender/checkpoints/06_runtime_base.blend`, SHA-256 `A4767A97A200636A13EC9C13F06DE0478537CEF8867DD9DB021FC4B5917117CC`.
The preserved old combined source `tg26_actions_v1.blend` has a +0.001002603 source-unit grounding offset and is not the exported mesh rest basis.
The source remains a non-firing, unarmed temporal clock-armored humanoid with 24 bones; no regeneration, new provider call, or paid operation occurred (estimated and consumed credits both zero).

Native `resume_base_winding`, `resume_base_patch`, `resume_base_material`, `resume_partition`, and `resume_export_mesh` receipts record the selected pipeline.
Exact 12,198 face flips and the reviewed patch remove 67 triangles, add 33 triangles, and discard 24 unused interior vertices: 14,973 retained vertices and 29,966 triangles.
All retained positions, UV corners, weights, original rig and actions were preserved by native mutation and save/reopen checks.
There are zero remaining boundary edges, non-manifold edges, degenerate faces, or zero-length normals before export.
This is localized reconstruction, not decimation or a silhouette simplification.
The patch specification SHA-256 is `6F038E344A9655BDD12869139C7AB70AE3BA149684EA6040106118266ED829B7`; `complete_patch_numeric_verification.json` independently checks the declared topology.

The accepted V2 winding recomputes geometric normals.
A later stricter normal-preserving sibling diagnosis measured approximately 0.0867 degrees of native normal quantization; that unselected diagnostic is retained and does not replace the visually accepted V2 source.
No silent claim of exact source custom-normal preservation is made.
Source-material and opaque-clay culling-on/off previews restore the full torso, legs, boots and limbs; each culling comparison differs in only nine pixels, with maximum channel differences six front and nine three-quarter, without silhouette loss.
The parent personally accepted `blender/previews/tg26_surface_after_v2_original_three_quarter.png`.

The selected mesh is `export/20260906_repair/mesh/chaosx_temporal_guard.mesh`, SHA-256 `BF13AA313FDB3D7869665810ACDFE64A77C555EEFC802D947FF332986BB39848`, 7,554,535 bytes.
Two identical-material streams contain 20,000 and 9,966 triangles, with 60,000 and 29,898 seam-split vertices and maximum indices 59,999 and 29,897.
The conservative 60,000-entry partition retains all geometry and emits no exporter warning.
`rest_bind_export_equality.json` verifies exact exported skeleton-block text equality against the canonical original mesh: all 24 rest bindings remain identical.
The armature's calibrated 0.01000000350177288 scale is normalized once by the exporter; vanilla source height 7.351824797689915 and custom height 7.3518242835998535 remain matched, with entity scale 0.8 applied once by the consumer.

Material textures are the three 1024x1024 legacy BGRA DDS files beside the selected mesh.
Diffuse SHA-256 is `82071750202D2435542841E8354313DDB4B46BFD4B23CEBA0308CE4DE6DB4044`; normal is `77A342BF40D9C65A36F74829EFA94A174C634AD5341C72E16A85CF0360EB805A`; specular is `A482D6BACACE80C23EA97E36849B2F79118EC59D5A2501F4057905835F1B64AE`.
Normal packing is (0, normal R, 0, normal G); specular packing is (0, 32, metallic, 255 minus roughness).
The engine consumes alpha as glossiness, and the native source preview applies the required roughness inversion; provider originals remain immutable.

The final editable checkpoint is `blender/checkpoints/tg26_repaired_actions_v2.blend`, SHA-256 `75B0585D0DC62A09E167766FA9833C7446F1A2987E67D40A1EAFBE6F0DF69592`.
The eight original actions remain in the repaired source; exact support and retreat declarative specifications were replayed through the locked adapter using GPT-6-astra.
`editable_action_replay_equivalence.json` records maximum phase-bone world-component differences of 9.5367431640625e-7 for each replay, accepted by the parent as grounded-world equivalence.
Native key hashes differ because the current editable source grounds the root bone instead of the old rig-object location; no native-key identity is claimed and no accepted animation binary was replaced.
The successful retreat native receipt `8f1684bd673a4045ac981bb7499a9194` was recovered from worker stdout after caller receipt loss; a later duplicate was rejected for the existing output without overwrite.

The ten selected binaries remain under `export/20260906_repair/anim/` and are compared against `resume_input_hashes.json`.
Support SHA-256 remains `4733FB4DAE6C335AE9063BDC81EB9D891C62A688D975C8FB45A664D0690528A4`; retreat remains `8D62D4BD2D8C9DE3C8AF50F58348166D77643B6D713661FDF5DADAD4668BD017`.
`resume_reimport_<role>.result.json` records actual selected mesh and animation reimports, five sampled frames in three views, 24 bones, and 29,966 triangles.
The apparent 89,898 split boundary edges are export UV/normal seams; read-only positional weld diagnostics recover 14,973 vertices with zero boundary or non-manifold edges without mutating runtime data.
Final role review sheets and the manifest record the completed semantic/contact review and its sampled-frame limits.

Dependency evidence spans coherent adapter 1.10.29 through 1.10.32 locks as the adapter owner fixed lazy DDS and missing hidden-reference-image auditing.
Blender is 5.1.2 build ec6e62d40fa9; io_pdx_mesh is 0.91.0 with locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2` (the exact authoritative full checksum is in dependency preflight records).
Fresh stdio schemas and the listening bridge were verified; no unrestricted Blender Python or shared adapter edits were used.

Remaining parent work is exact runtime copying and hash synchronization, entity/material/action/audio wiring review, and final commit.
No in-game completion is claimed.
Historical source-art URL/creator/terms, authorization and refinement prompt receipts, complete remesh/credit lineage, primitive-waveform selection/ambient source-role review, and a distinct retreat sound decision remain unresolved as described above.
Bespoke large/on-map counters are complete under the 2026-09-01 parent-reviewed handoff and are not missing.
No unapproved simplifications were made; localized reconstruction and the documented grounding representation change are explicitly accepted exceptions, with original sources and all ten selected animation bytes preserved.

## Parent integration values and review closure

The parent reviewed and accepted all three final role sheets, intact surfaces, and articulated terminal death.
The exported object name is `char1.002` for both material streams: mesh index 0 / stream index 0 and mesh index 1 / stream index 1.
The selected Blender export object is `char1.001`; this source-object label must not replace the actual exported `char1.002` name in runtime material overrides.
`resume_export_mesh.result.json` records the exact exported names and stream indices.
Approved entity scale is 0.8 applied once, as recorded in `current_reference_and_audio_checks.json`; no further mesh compensation is needed.
Suggested runtime loop policy is yes for idle, move, attack, defend, entrain, temporal_anchor, synchronization, support_attack and retreat; death is non-looping and terminal.
Both stale final-surface pending fields in `action_crosswalk_final.json` are replaced with completed actual-byte receipt status, consistently populated for all ten roles.
Sound limitations remain the primitive square-wave 60 Hz hum proposed for selection/idle/ambient (not an acceptable final sourced-recording substitute), missing distinct retreat cue or explicit sourced-footstep reuse decision, parent-owned cue/loop alignment, and attribution/share-alike obligations on the sourced recordings.
Per-subunit selection audio consumer support remains limited; no global voice replacement is authorized.

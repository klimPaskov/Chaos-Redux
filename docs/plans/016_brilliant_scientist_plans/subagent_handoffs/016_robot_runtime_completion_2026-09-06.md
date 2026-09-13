# Event016 preserved Autonomous Robot — implementation and acceptance record

Status: incomplete; authored candidates are not accepted runtime actions.
Owner: `/root/robot_runtime_completion`, 2026-09-06.
The explicit parent-transmitted user exception preserves existing geometry, integrated twin guns, topology and materials without regeneration or provider calls.
Concurrent `attempts/20260906_weaponfree_blender` work is not selected by this handoff and was not edited.
Job-wide manifests and runtime files are untouched.

## Source and dependencies

Job: `docs/assets/shared_robot_system/models_3d/autonomous_robot`, adapter job ID `autonomous_robot`.
The protected `blender/checkpoints/manual_recovery_2026_08_27.blend` was verified as SHA-256 `FEB2BB03E2DE7EAF84547C0864500C821A7DDD05A0BEE1958948C969F2BDB25D`.
The selected locator-bearing sibling `manual_recovery_2026_08_27_muzzle_export_probe_2026_09_04_both.blend` was verified as `2ECDC375C90F4C3784B2BAB215C7D60A22A26EF392479A9EE41982F70828757C` and remains immutable.
Historical Meshy6 provenance is retained; this repair made no provider calls and consumed zero credits.
Fresh repository `BlenderAdapterClient` stdio calls used checksum-locked adapters 1.10.22 through 1.10.24 as shared owners relocked approved changes; cached app exposure was older and not used for repair.
Blender is 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh is 0.91.0, and the locked extension archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
Health request `f73ecd6b5d8b4fc28391fd8332263c7d` confirms the selected Blender/export extension route.

Required skills read: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`.
Offline core wiki pages and graphical-assets/entities/sound references were consulted together with installed vanilla infantry entity and counter references.
The retained calibration record names geometry height 7.3518247604 against vanilla western-European infantry 7.3518242835, entity scale 0.8 exactly once, effective height 5.8814598083, -Y forward and +Z up.
Fresh selected-checkpoint geometry inspection measures rest height 7.3567042351 (effective 5.8853633881 at scale 0.8), approximately 0.0664% above that vanilla reference; the historical calibration number is not substituted for the current measured height.
No scale or source-geometry mutation was made in this pass.

## Actual authored source chain

Every row is a new sibling working checkpoint preserving prior actions, not a source overwrite.
All actions use explicit role-specific skeletal keys authored through the measured-action adapter by GPT-6-astra, not whole-object transforms or sine templates.
The eight legacy actions remain available, including training, whose semantic acceptance has not yet been re-established.

| Checkpoint under `blender/checkpoints/` | SHA-256 | Role and phases |
| --- | --- | --- |
| `robot_preserved_acceptance_attack.blend` | `C374E20220AA4AF7C20F2A81F0DCFC1469A0C4074B79F959B04E8A0B5F19E342` | 30 FPS, 0–48; aim, three firing/recoil pulses, recovery |
| `robot_preserved_acceptance_idle.blend` | `61CEF118A9F6617432378569FDCBCF6E4211FF88F3A27B942617AF67065B9663` | 30 FPS, 0–48 loop; articulated observation |
| `robot_preserved_acceptance_defend.blend` | `4270530C1E7266F9D3D8CC1B5B599193CA57998F5F828BA0BF772F7B00BAA60A` | 30 FPS, 0–48 loop; brace, scan left/right, return; not an idle alias |
| `robot_preserved_acceptance_move.blend` | `1C6EDA7628D4B2B554C466AE93AA79070CA47BEE1E86AF1FEAC06E7386E65AB4` | 30 FPS, 0–48 loop; alternating contact/loading/clearance/extension |
| `robot_preserved_acceptance_retreat.blend` | `FED8F58803AA46912056BF04AB1F69D6FFA9ADF7497F756397B4CABFC02CD21A` | 30 FPS, 0–48 loop; backward reach and weight transfer |
| `robot_preserved_acceptance_support_attack.blend` | `7AAC3C496DBEAE320058D9045E74E963C5E21140BD2CA2BC474CF47C8B6825DB` | 30 FPS, 0–72; two aimed sectors and two separate bursts |
| `robot_preserved_acceptance_death.blend` | `86EF46DC4FF08F13F9238177D4E3D349DEC3FB296C9CEE15CA5D35C4EC3BC440` | 30 FPS, 0–72; stagger, failed knees, fall, impact and settle candidate |

Exact specifications are `evidence/robot_preserved_acceptance/<role>_spec.json`; full evaluated ground/phase reports are `blender/reports/robot_preserved_acceptance_<role>.json`.
The death report and checkpoint match the intended source/spec chain, but a later authoring request `10d06a3810c546cda69d055f0f9ba6fc` rejected that already-existing output; the immutable existing output was inspected rather than overwritten.
No source-action approval is implied by these file hashes.

## Concrete failures and repairs still required

- Source `char1.003` retains 15123 vertices and 29971 triangular faces, one UV layer, one material and the existing 24-bone rig.
- All vertices have four normalized influences, but that is not sufficient deformation proof: inspected right forearm-region vertex 12348 carries RightUpLeg 0.13347055, RightHand 0.33574551, RightForeArm 0.32266843 and RightArm 0.20811550.
- Current registered `muzzle_export` and `muzzle_left_export` are retained by name but sit near Z6.1 at attack frame12, visibly above the gun barrels; placement and discharge axes need correction from measured geometry.
- Actual attack frame12 front/right renders keep both integrated guns and planted feet; discrete recoil/recovery and weapon rigidity remain unaccepted until full phase and export review.
- The source material preview is excessively reflective; source specular is linked to Blender roughness, and packed-map interpretation must not be confused with engine specular conventions.
- The old mesh references PNG basenames absent beside its export, causing magenta actual-byte reimport previews; no material or runtime texture substitution was made.
- The old death actual-byte proof hunches without convincing body impact/settle; removing its obsolete provenance gate alone would not make it acceptable.
- Newly authored raw gait and death candidates penetrate the ground; root-local vertical correction and stance-foot review are required after weights stabilize.
- Source adjacency shows one fused 14988-vertex body component, so guns cannot be assigned through automatic loose-component classification.

Evidence: source landmark request `935ec77abd29407ab85417ee5f4f4e07`, landmark JSON SHA-256 `1850EA79A4E9A013B2E8082F1CAA5882B2E8D1877DD60B4A40556A7D7E7594CF`; detailed frame12 mesh-region request `635e4e6ed8444e1b89c546e6975bbc46`; neutral source front/right request `af7f713c0d09418680000c67e4110814`.

## Export evidence

The new attack `.anim` exists at `export/robot_preserved_acceptance/robot_preserved_acceptance_attack.anim`, 24444 bytes, SHA-256 `E830562D7E5BB81AE561DF59CCF1CDB1BAB0C70754BD7EAD72AD97554FCE6BD8`; export request `aba65907e8fa4112a33e82d32fff87a0` reported no warnings.
Direct mesh export request `cdc06d63c5634c91a880b87b52487aca` wrote a stream with 27922 vertices and 89913 triangle-index entries, then failed the project's conservative 65535-entry batch budget.
That budget is not asserted to be an engine index-count limit; the maximum referenced vertex index was 27921.
The existing skeletal material-batch partition route is the intended topology-preserving export preparation after source selection.
No failed or provisional export is selected for runtime.

Old death actual-byte proof uses mesh SHA-256 `DC081A642954D203BCE7E7BA1B5F5465BB38D398D2A64C72F912A657891DCF57` and animation SHA-256 `4FC1CF58C3ECC7969397D0B3387626A1621A9BCD296D88D1EE0D6ACD2CEAFF13`.
Fresh corrected-parser reimport request `fd4a07fbba0548aa94899a7614b9518d` produced `validation/reimport_robot_preserved_acceptance_death.json` and five-frame, three-view previews.
This is diagnostic evidence, not semantic acceptance.

New attack actual-byte reimport request `9a891a3a1bd24ec39063e3823fcc67c8` used that preserved mesh and the new `E830562D…` attack animation.
It produced `validation/reimport_robot_preserved_acceptance_attack_bytes.json` and `blender/checkpoints/reimport_robot_preserved_acceptance_attack_bytes.blend` with five three-view samples.
Frame13 three-quarter was visually reviewed: articulated gun pose corresponds to source, but the proof remains magenta with unresolved texture paths and conspicuous faceting.
Its validation JSON SHA-256 is `F726C0018A5CC3F2BA2A3B661BCA210C1FC256844529B574083A21B3EAE243D8`; actual reimport checkpoint SHA-256 is `3FA408C64D48827B74EEEF98BE4DE54D95DA8A95879D80B6C08C19464C782FF1`.

Root-local grounding request `03de984da6fb4dbb940008a0e8669263` preserved every non-root body key and original action, producing `robot_preserved_acceptance_death_ground_preview.blend`, SHA-256 `8A77258B9D72DDA6A3B209BEC6F2B0A95718CF307A118165536215CDFB26F33D`.
Grounded action native hash is `4D388874CA752BEB36E2E64ED9D692EB4227C17417A3A276E392EF7BF7726E61`.
Actual frame48 front/right inspection `f604cfe4cfdb439d9962002c10ae4221` is explicitly rejected: the falling body balances above ground on a downward-pointing gun barrel, with torso and legs hovering.
Passing minimum-Z correction does not establish body impact or physical settling; arms/guns must be folded clear after the weight repair and reviewed again.

## Sourced audio and counters

`evidence/robot_preserved_acceptance/audio_reconciliation.md` records four restored source files matching historical hashes, the preserved licensed MG42 preview, four mechanically converted WAV candidates, exact source URLs/attributions/licenses, transformation details and proposed phase times.
No audio was synthesized, generated, mixed from primitives, or installed into runtime.
Audible acceptance and seamless-loop review remain pending; source licensing uncertainty for the MG42 description's underlying layers is explicitly retained.
No country/global selection voice replacement is authorized or proposed.
The entity-state movement/attack/impact/death surface is the supported handoff boundary; distinct unit-selection routing remains unproven.

Existing large and small counter DDS files are preserved, with SHA-256 `147CF90C3D053947640F7865F1DADE6D8FFABA99942E8401ED4575D53DB61B09` and `BDEB527F8A73494B918ADEC27C26AEC97C299F51AD00D2DA2946A37A278EDD4B` respectively.
The large strip is 152×42 (two 76×42 frames), small is 60×12 (two 30×12 frames); existing tokens are `GFX_group_autonomous_robot_icon`, `GFX_unit_autonomous_robot_icon_medium` and `GFX_unit_autonomous_robot_icon_medium_white`.
The existing counter contact sheet was visually inspected and retains its documented vanilla green/white frame treatment.
Its source depicts a tracked robot while the preserved model is bipedal; the explicit preserve-existing-counters instruction was honored without silently replacing art or claiming exact silhouette parity.

## Narrow shared repair capability

Parent subsequently authorized ownership of standalone `.tools/3d_pipeline/adapter/explicit_skin_repair.py` and `.tools/3d_pipeline/tests/test_explicit_skin_repair.py` only.
The helper supports SHA-bound exact-index weight replacement with explicit prior weights, maximum four normalized existing-bone influences, untouched-weight retention, full promotion fingerprints, and save/reopen verification.
Its read-only companion renders copied rest geometry with red fully selected faces and cyan mixed boundary faces, exposing every exact index and prior weight in the report.
Ten pure validation tests pass; actual Blender repair proof is not yet complete.
Shared worker/wrapper/config/lock edits belong to the parent; the proposed thin integration patch is `evidence/robot_preserved_acceptance/explicit_skin_thin_integration.patch`.

## Remaining parent and worker work

Finish exact forearm/gun ownership review and guarded reweight; repair and verify both muzzle frames; ground and visually evaluate every role, feet and arm-gun deformation; retain training only with role evidence; partition and export the final selected source; reimport actual final bytes with matching textures and compare poses/locators; complete sourced-audio listening/timing acceptance.
The parent owns reviewed runtime `.asset`, GFX, particles, sound definitions and final documentation/manifest integration.
No runtime file, gameplay file, job-wide manifest, staging index or commit was changed by this worker.
No live-game acceptance is claimed.

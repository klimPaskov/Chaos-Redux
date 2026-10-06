# WP3 Model Repair Handoff

Status: `in progress`. The mutant zombie mesh and idle passed export and hash-bound reimport, and the parent approved and installed the mesh, idle, diffuse, and normal bytes. The eight-model package remains incomplete because six other model tickets, seven mutant action roles, mutant material gates, demonic repairs, sourced audio, filmed acceptance, and live-game review remain open.

## Scope and evidence boundary

The initial WP3 baseline covers `zombies`, `infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, and `demonic_zombies`. On resume, the parent narrowed this worker's production ownership to `mutant_zombies` and one bounded demonic surface-preview comparison; the remaining six model repair tickets are separately assigned by the parent.

Meshy was not used, no provider balance or key gate was needed, no credit was spent, no downloads were made, and no production bones or weights were synthesized. The only authored keys so far are deliberate manual keys on the existing mutant rig, using the locked hidden Blender Lab bridge and a saved new checkpoint.

The parent owns runtime wiring, audio, final report, and live-game acceptance. The parent installed the approved mutant mesh, idle, diffuse, and normal as an uncommitted, hash-checked runtime tranche. The texture worker supplied the mutant diffuse and normal candidates and still owns undead, necrotic, and demonic texture work. This resumed worker owns mutant geometry, rig, action, and UV work, plus the bounded demonic map-surface comparison. The six other WP3 geometry and action tickets remain outside this worker's resumed ownership. Existing `.asset`, `.gfx`, entity, and sound definitions were not edited.

## Locked route and source references

The earlier Blender-only route report is `docs/assets/002_zombie_outbreak/models_3d/zombies/validation/wp3_model_repair_route_verification_20261006.json`. This resume independently reverified Blender 5.2.2 build `d13f752e3b9c`, adapter 1.11.0, `io_pdx_mesh` 0.91.0, all 36 locked adapter source hashes, matching 32-operation lock/config arrays, and compatible extension archive SHA-256 `508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702`; current evidence is `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/validation/wp3_blender_route_resume_20261006.json`. The locked Blender Lab MCP route is exposed with `execute_blender_code` schema `{code: string}`. On this resume the Lab socket is closed, no Blender process is running, and only 2.5 GB of system memory is free, so no new Lab process has been started yet. The parent confirmed that other large processes must remain untouched and is serializing the model-worker slots.

This subagent runtime exposed `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup`; schemas and actual responses are in `docs/plans/unit_fix_2026-10/wp3_model_repair_reference_evidence.json`. The parent runtime also currently exposes the reference tools. An earlier retry encountered a closed transport, and current searches are slow; those are route-health gaps rather than missing tool exposure. Offline wiki citations are `Entity modding > Adding a Mesh`, lines 25–44, and `Adding an Animation`, lines 169–186, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`. The reference route does not expose a server semantic version.

Installed vanilla files were read directly because the current source lookup returned no indexed definition: `gfx/entities/infantry.gfx`, lines 76–80, binds `generic_western_european_rifle_infantry_mesh` to `gfx/models/units/western_european_infantry.mesh`; `gfx/entities/units_infantry.asset`, lines 11–96, defines `infantry_rifle_entity` at scale 0.8. The calibrated source height is 7.3518242835 units, effective runtime height is 5.8814594268, forward is -Y, up is +Z, and ground contact is z-min. The posed scene measurement 7.216438 is not used for rescaling.

The requested `docs/plans/unit_fix_2026-10/unit_s3_report.md` remains absent. The existing `pipeline_report.md`, `wp3_zombies_report.md`, and `per_model_delivery_metrics.json` are the package baseline sources; their installed meshes/actions were unchanged by the shared delivery tranche.

## Mutant zombie candidate

A read-only recheck found no mutant `job.yaml`, so a full repair-intake profile was created at `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/job.yaml`. It keeps status `needs_user_review`, records the calibrated source and scale, existing 24-bone rig, original source checkpoint and provider hash, all eight required action roles, exact repair counts, material gates, candidate paths, and parent-owned installation.

The immutable working checkpoint is `blender/working/v1/blender/checkpoints/21d_export_batches.blend`, SHA-256 `817EAB983785315F85EDDB61EA87E1DE1864091EEB45D701E274A60D39E751B0`; the provider GLB SHA-256 is `BE6DEEC8C0119EC27F8C7D013284A7ECE66C14E785764E98021A5CB64E06A7FD`. The starting working mesh had 27,055 source vertices and 31,282 triangles; the pure positional gate at 0.0005 found eight boundary and four non-manifold edges. The parent reviewed the exact localized face evidence and authorized removing only faces 17,493, 22,420, 26,115, and 26,169. That removal eliminated 11 resultant loose edge records and ten source vertex records (indices 2338, 2366, 2374, 6602, 6649, 6652, 19888, 19915, 19923, and 19947); it did not globally weld or remap UVs. The mesh now has 27,045 source vertices, 31,278 triangles, zero positional boundary or non-manifold edges at 0.0005, zero same-direction edges, and unchanged retained vertex weights, UV corners, material assignments, and normals. The mesh is triangulated and its exported source height is 7.3518238 with ground at z=0.

Topology evidence is `validation/wp3_mutant_topology_pre_20261006.json`; source-specific before/after region renders are under `blender/previews/wp3_mutant_*_pre_edit_20261006*.png` and `wp3_mutant_post_geo_20261006_*.png`. The topology checkpoint is `blender/checkpoints/wp3_mutant_topology_20261006.blend`, SHA-256 `eaeea47bf903ac3559d598fc791d95e5ed877e38553bbcc5ba7a0478e89ea3cf`.

A deliberate in-place idle was authored on the existing 24-bone rig from its hunched frame-127 pose. It preserves the prior idle under `wp3_source_chaosx_mutant_zombies_idle` and keys breathing, head sweep/sniff, and wrist claw flex; the existing rig has no finger or jaw bones, and none were added. The action is 30 FPS, frames 1–180, six seconds, with 102 F-curves and 348 keys. The authored endpoint seam is 0 degrees and 0 local units. Parent review of the direct Blender front/quarter previews at frames 1, 45, and 135 found restrained head/wrist motion, grounded feet, and no large silhouette jump. Adapter motion peak is 2.0063 degrees at a wrist. The parent approved and installed this idle byte, while the plan's `peak_motion 0.8..3.0` acceptance still needs a filmed measurement. Foot contacts remain `unmeasured` because this idle has no authored plant event and no world-foot measurements were supplied. Authoring evidence is `validation/wp3_mutant_idle_authoring_20261006.json`; the authored checkpoint is `blender/checkpoints/wp3_mutant_idle_authored_20261006.blend`, SHA-256 `52AA97C2CE0CB666FD495DF6ABD7C3096529567CCC5C4E485FB48BD8B1B8E51B`.

The adapter exported the mesh from `blender/checkpoints/wp3_mutant_idle_authored_20261006.blend` to `export/wp3_20261006_retry1/chaosx_mutant_zombies.mesh`, SHA-256 `E16D492DE38C49AF4A73AEA30C8657AE0D6A091C59542CEB95817EB325ED4E07`, with delivery gate pass and zero boundary, non-manifold, degenerate, duplicate, or same-direction edges at 0.0005, 0.001, and 0.002. Export request ID is `58889c81013b422eada4c443e6372341`.

The action exported to `export/wp3_20261006_retry1/chaosx_mutant_zombies_idle.anim`, SHA-256 `9480E6DE7EACBB00B172319C2C868E29AD3F8FDD23EAC65174322F5BDFC96BF1`, request ID `d2f80107ebb446999e2c17679ec18636`. It passes the 30 FPS, 180-frame, six-second loop and 0-degree/0-unit seam checks. The parent approved and installed these action bytes; filmed peak_motion and live consumer acceptance remain pending.

The first mesh export attempt wrote bytes but failed the delivery gate because the required job profile was absent. Those failed-attempt bytes are not a candidate: `export/wp3_20261006/chaosx_mutant_zombies.mesh`, SHA-256 `7DA5B81EDCD700654749CEDE62C7CA493B54CEE634C38ECF2F2834284E96AC68`. The new intake profile allowed a clean retry at a new path.

Hash-bound mesh+idle reimport passed using the registered DDS copies that were present before the parent-approved texture install. Receipt: `validation/reimport_wp3_mutant_export_20261006_current_registered_dds.json`, request ID `e25064c8bc5244bc9ae9a5ffaf14adcf`; mesh/idle hashes read back exactly as above. Reimport reports 31,278 triangles, zero positional boundary/non-manifold/degenerate edges, source height 7.3518238, 24 bones, and ground-contact bound z=0.004002 across frames 1, 46, 90, 135, and 180. The historical pre-install registered map preimages copied for that proof are diffuse `E5354E5B1255F89E49C785D675502F508071A5A21A397C01A2234BE7735CF139`, normal `0916A7213C2808A24086D077009B1B9060493BCF0D7582F12F27E9849344A5B7`, and specular `96BB4591771C50C62EC344AC6DB2AC32C708C8E20AB73CEC9F720E33022BB226`. The parent later installed diffuse `ECD5BB5E4AED1C2114158C54204C2585E8EF395F890419E389A07E0DFF53A2F9` and normal `ED43B774293D559F1300BA7A3318260F2DD6D2AA45E8C1EA4436BCAE8465564A`; the specular preimage remains current. The GFX consumer is `gfx/entities/chaosx_mutant_zombies.gfx`, with all four mesh stream indices 0–3 bound to those same texture filenames.

The first reimport previews are `blender/previews/reimport_wp3_mutant_export_20261006_current_registered_dds_frame_001_front.png`, `..._frame_090_front.png`, `..._frame_135_front.png`, and `..._frame_135_three_quarter.png`. They showed Blender magenta because the reimported PDX material image nodes had empty image paths; a read-only `inspect_scene` confirmed one missing-path image node on each of the four PDX material slots.

A raw `bind_existing_pdx_material` attempt was rejected because the then-current BC1 diffuse did not meet that adapter operation's BGRA/uncompressed or BC3/BC7 input gate. The texture worker prepared a preview-only BC3 wrapper with exact RGB parity to the production candidate across all ten mips, plus a source-derived 1.15× normal-detail candidate.

The final parent-reviewed previews are `blender/previews/wp3_mutant_diffuse8674_normal115_f135_front.png` (SHA-256 `8C21E8C5889F0E429623C130B46F60C59DB3A5EBD97CC2699D851BD17FC8EA1D`) and `blender/previews/wp3_mutant_diffuse8674_normal115_f135_three_quarter.png` (SHA-256 `BAF0D280ED53F0B0F5DE232CC98F2041C487B546199453640539A4D05D7A87C1`). Their source checkpoint is `blender/checkpoints/wp3_mutant_preview_diffuse8674_normal115_20261006.blend`, SHA-256 `38C8FDC53D17668CBB8DBF7C11A240B08F71F9EFD928234AE35813CCE773385B`; a fresh adapter `inspect_scene` verified the preview uses the exact diffuse wrapper, byte-identical normal preview copy, and current specular map on all four streams.

The parent approved and installed the diffuse (`ECD5BB5E4AED1C2114158C54204C2585E8EF395F890419E389A07E0DFF53A2F9`) and normal (`ED43B774293D559F1300BA7A3318260F2DD6D2AA45E8C1EA4436BCAE8465564A`) DDS. The normal QA reports G/A standard deviations 15.2255/15.2545 and `mean_tangent_tilt` 0.123562 (unitless). The specular map remains unchanged at `96BB4591771C50C62EC344AC6DB2AC32C708C8E20AB73CEC9F720E33022BB226`; specular classification and jaw-wetness remain unresolved, so production material acceptance is still open.

### Parent-installed mutant four-file tranche

The exact uncommitted runtime files for the parent's focused commit are:

| Runtime file | Immutable source | SHA-256 |
|---|---|---|
| `gfx/models/units/chaosx_mutant_zombies/chaosx_mutant_zombies.mesh` | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/export/wp3_20261006_retry1/chaosx_mutant_zombies.mesh` | `E16D492DE38C49AF4A73AEA30C8657AE0D6A091C59542CEB95817EB325ED4E07` |
| `gfx/models/units/chaosx_mutant_zombies/chaosx_mutant_zombies_idle.anim` | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/export/wp3_20261006_retry1/chaosx_mutant_zombies_idle.anim` | `9480E6DE7EACBB00B172319C2C868E29AD3F8FDD23EAC65174322F5BDFC96BF1` |
| `gfx/models/units/chaosx_mutant_zombies/chaosx_mutant_zombies_diffuse.dds` | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/wp3_textures_20261006/delivery/approved_stage/wp3_mutant_approved_diffuse_normal_20261006/mutant_diffuse_approved_candidate/output.dds` | `ECD5BB5E4AED1C2114158C54204C2585E8EF395F890419E389A07E0DFF53A2F9` |
| `gfx/models/units/chaosx_mutant_zombies/chaosx_mutant_zombies_normal.dds` | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/wp3_textures_20261006/delivery/approved_stage/wp3_mutant_approved_diffuse_normal_20261006/mutant_normal_strength1p15_approved_candidate/output.dds` | `ED43B774293D559F1300BA7A3318260F2DD6D2AA45E8C1EA4436BCAE8465564A` |

The mesh and idle copy receipt is `docs/plans/unit_fix_2026-10/wp3_evidence/mutant_parent_install_receipt.json`; the diffuse and normal compare-and-swap receipt is `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/wp3_textures_20261006/delivery/approved_manifest.json`. Final geometry, action, and map evidence is under the mutant job's `validation/` and `wp3_textures_20261006/evidence/` folders. The installed specular map and all runtime definitions remain outside these four files and were not changed.

The remaining seven mutant roles (move, attack, defend, support_attack, retreat, training, and death) are still blocked on the existing package audit. The parent owns the current mesh, idle, diffuse, and normal runtime installation and its focused commit.

## Per-ticket status

The table preserves the earlier installed-byte baseline at positional tolerance 0.0005. Counts for models without a new candidate are baseline findings, not results of this repair pass.

| Model | Baseline boundary/non-manifold; same-direction edges | Baseline action audit | Model ticket and current disposition |
|---|---:|---:|---|
| `zombies` | 129 / 129; 5 | 1 pass, 7 blocked | Coherent head/torso/arm/leg/helmet UVs and field-uniform bake, region specular, authored idle shifts and claw curls, topology and seven blocked roles remain open; this worker has not changed its mesh/actions. |
| `infected_zombies` | 201 / 312; 12 | 0 pass, 8 blocked | Coat/skin/feet bake and masks, 1.17-second chest-height attack, defend/training closure and skull clearance, coat-hem skinning, topology, eight roles, and actual cough/retch/spit sources remain open; mesh/actions unchanged. |
| `rabid_zombies` | 81 / 112; 7 | 1 pass, 7 blocked | Standing four-second frantic idle, move seam, forward lunge instead of back kick, wrist/forearm skinning, suit bake, topology, seven roles, and distinct shriek/death gasp remain open; mesh/actions unchanged. |
| `parasitic_zombies` | 296 / 554; 23 | 1 pass, 7 blocked | Tentacle rig/weights/idle/whip lag, forward lash/grab, defend closure, death ≤4.5 seconds, tube caps and duplicate removal, topology, seven roles, and wet-lash/suction sources remain open; mesh/actions unchanged. |
| `mutant_zombies` | 8 / 4; 0 | 0 pass, 8 blocked | Four spur triangles were removed and topology passes; repaired mesh and authored idle passed export/reimport and are parent-approved and installed. The seven other roles remain blocked. The parent-approved diffuse and normal are installed; specular classification, jaw wetness, and filmed peak_motion remain open. |
| `undead_zombies` | 251 / 330; 61 | 1 pass, 7 blocked | Source-based suit/skin grade and gloss masks, substantial idle, plant/training easing, retreat seam, attack-knee and armpit/hem weights, topology, seven roles, and two extra moan takes remain open; mesh/actions unchanged. Texture worker owns diffuse/normal candidates. |
| `necrotic_zombies` | 84 / 73; 1 | 1 pass, 7 blocked | Bone/teeth gloss masks, distinct skin/rags, foot plants, arm sweep, transition easing, retreat seam, rag/thigh skinning, topology, and seven roles remain open; mesh/actions unchanged. Texture worker owns diffuse/normal candidates. |
| `demonic_zombies` | 50 / 36; 2 | 1 pass, 7 blocked | Forearm/hand/wing skinning and joints, standing slash, leap landing, death/training/idle/retreat/plant repairs, source-island padding and region grade, topology, seven roles, and own idle/defend growls remain open; mesh/actions unchanged at this handoff. The bounded current-map versus skin10 surface comparison remains this worker's only demonic task; texture work remains owned by the texture worker and its regional mask must stay bound to the selected mesh/UV hash. |

## Files created or changed in this model tranche

- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/job.yaml`: new full repair-intake profile, after an absence check.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/blender/checkpoints/wp3_mutant_topology_20261006.blend`, `wp3_mutant_idle_authored_20261006.blend`, `wp3_mutant_export_20261006_retry1.blend`, and `reimport_wp3_mutant_export_20261006_current_registered_dds.blend`: separate geometry, action, export, and reimport checkpoints.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/export/wp3_20261006_retry1/`: exported mesh/idle, delivery receipts, and hash-bound copies of the currently installed registered DDS files for reimport proof only.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/validation/`: exact topology, action authoring, and current reimport receipts.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/blender/previews/`: pre/post geometry regions and authored/reimport idle frames.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/validation/wp3_blender_route_resume_20261006.json`: resume lock, route, live-schema, Blender build, extension, and adapter evidence.
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/validation/wp3_mutant_material_preview_review_20261006.json`: parent-reviewed final map preview, approved runtime map hashes, and remaining material gate.
- `docs/plans/unit_fix_2026-10/wp3_model_repair_route_verification_20261006.json` and `wp3_model_repair_reference_evidence.json`: locked route and actual reference-tool evidence.
- `docs/plans/unit_fix_2026-10/wp3_model_repair_handoff.md`: this handoff.

No files under runtime `gfx/models`, `gfx/entities`, `sound`, `common`, or `.tools/3d_pipeline` were changed by this worker. There were no paid calls, credits consumed, or external files downloaded.

## Remaining acceptance and risks

The final diffuse-plus-normal preview is non-magenta and parent-reviewed, and the parent installed both DDS files through the approved texture delivery path. The preview-only BC3 diffuse wrapper is evidence only. The adapter material-binding operation still rejects the production BC1 diffuse, while the specular recipe and jaw-wetness class remain unresolved; no specular substitute was installed.

The mutant idle has passed export/reimport but does not close the action ticket: world-space foot contacts were not measured, peak-motion acceptance is pending, and seven required roles remain unchanged. The source geometry/armature rest relation was preserved through export/reimport; the source height and entity scale remain the calibrated 7.3518242835 and 0.8.

All seven other packages retain their exact baseline topology/action blockers above until a localized, source-reviewed geometry or action repair is performed and passes export/reimport. Parent review, final runtime installation, texture approval, entity/audio wiring, counter completion status, and live-game acceptance remain outside this handoff.


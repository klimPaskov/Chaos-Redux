# Event 016 Alien Infantry V13 muzzle/export recovery handoff

Status: blocked pending mandatory locked-route verification and a supported locator-authoring path.

Scope: bounded recovery of a muzzle locator on the accepted Alien Infantry V13 package. No geometry regeneration, remesh, ImageGen, provider purchase, body-animation replacement, runtime wiring, counter regeneration, audio wiring, or live-game validation was performed.

## Authority and unchanged accepted inputs

The current source authority is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`. Historical `job.yaml`, `manifest.md`, and the rejected `manual_recovery_2026_08_27` instructions are not recovery authority.

The accepted mesh is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh` with SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`.

The accepted geometry has 59,999 triangles and 59,451 exported vertices, an integrated cyan-tipped pistol, and the 24-bone provider rig. Existing reimport diagnostics report 30,035 vertices after diagnostic weld, with no degenerate or non-manifold geometry; that diagnostic count is not a replacement for the exported-vertex count.

The accepted runtime material is `PDXmat_char1.002` on mesh object `char1.002`. Existing accepted map checksums are diffuse `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`, normal `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39`, and specular `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D`.

The calibration precedent is installed vanilla `western_european_infantry.mesh` against `units_infantry.asset#infantry_rifle_entity`: source height `7.3518242835`, entity scale `0.8` exactly once, effective runtime height `5.8814594268`, forward `-Y`, and up `+Z`.

The accepted actual-byte action checkpoints are `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/reimport_v13_firearm_preset_<role>_final.blend`, with corresponding validation records `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/validation/reimport_v13_firearm_preset_<role>_final.json`. These are the only accepted V13 checkpoint/reimport inputs used by this handoff.

| Role | Existing accepted action evidence | Runtime SHA-256 | Timing and semantic note |
|---|---|---|---|
| `idle` | provider action checkpoint/reimport record | `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF` | distinct idle role |
| `move` | provider action checkpoint/reimport record | `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F` | distinct move role |
| `laser_attack` | provider action checkpoint/reimport record | `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0` | action 223 `Draw_and_Shoot_from_Back_1`, 236 frames at 30 FPS; discharge frame 145 / 4.8 s; recovery near frame 190 |
| `defend` | provider action checkpoint/reimport record | `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73` | provider `Combat_Stance`; non-firing stance, not a firing action |
| `support_attack` | provider action checkpoint/reimport record | `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061` | action 234 `Walk_Forward_While_Shooting`, 99 frames at 30 FPS; supplied discharge frame 50 / 1.6333 s |
| `retreat` | provider action checkpoint/reimport record | `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC` | distinct retreat role |
| `death` | provider action checkpoint/reimport record | `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0` | distinct death role |

Thus Alien V13 has all seven distinct provider action roles in existing evidence. The seven roles remain the source motion and are not to be replaced. Attached-pistol body contacts are preserved in the accepted checkpoints; a dedicated muzzle/discharge-axis contact has not been proven.

## Current active runtime facts

The existing consumers are `common/units/016_brilliant_scientist_project_forces.txt#alien_infantry`, `gfx/entities/alien_infantry.asset`, and `gfx/entities/alien_infantry.gfx`, with entity `alien_infantry_entity` and mesh token `alien_infantry_mesh`.

The existing effect definitions are `alien_laser_muzzle_particle` in `gfx/entities/alien_infantry_particles.gfx` and `alien_laser_muzzle_flash` in `gfx/entities/alien_infantry_lights.asset`. Both are currently unbound because no accepted node or locator is available. These active files were not edited.

The sourced audio evidence is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/provenance/audio_sources.json`, with derived candidate `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/derived/alien_infantry_laser_fire.wav`, SHA-256 `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770`. It remains unwired. No selection audio or global infantry voice replacement is proposed.

The bespoke counter package is already parent-reviewed and is not regenerated here. Counter completion does not imply 3D locator, mesh export, action, audio, or live-consumer acceptance.

## Rejected evidence kept separate

The rejected diagnostic line is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/logs/adapter/0024d10f2f6a4dc59c19e0a9210f1a0c.result.json`, referring to `blender/checkpoints/manual_recovery_2026_08_27.blend` and `export/manual_recovery_2026_08_27/...`. Its export request `f8de71553aa541799162CCC3ED1C0420` stalled topology validation with 5,373 boundary components and 48,189 loose boundary edges, so it cannot be promoted.

That rejected diagnostic contains an Empty named `muzzle` parented to `alien_infantry_rig` with `parent_type: BONE`, local location `[-1.1899864673614502, -0.2889678478240967, -0.9782130718231201]`, and matrix-world translation `[-0.821446418762207, -0.794110119342804, 6.553159713745117]`. The parent bone name is not recorded there, and these coordinates are not accepted V13 locator data. Do not copy them blindly into the accepted checkpoint.

## Locked-route gate and capability result

`MESHY_API_KEY` was present and non-blank at the required first process check, without exposing its value. No provider call, balance call, paid operation, Blender call, generation, or asset download was made.

The mandatory environment verifier was run before any route use. It reported a hard checksum mismatch for the locked adapter file `.tools/3d_pipeline/adapter/normalization_convergence.py`: expected SHA-256 `91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`, actual SHA-256 `5D014E0D1058AB0C58FFBB774A1AC8AB3E8536A03F9FDA524488F835725E33D3`. The adapter route therefore did not pass verification and was not invoked. The generated environment report was restored to its pre-check state; no lock content was changed.

The repository lock remains the authority: schema `1.0.0`, official `@meshy-ai/meshy-mcp-server` `0.4.0` at git `d8c77d1cb897e345eb41d38b510b8391b1664346`, exact Meshy model `meshy-7`, Blender `5.1.2` build `ec6e62d40fa9`, locked `chaosx_blender_hoi4` adapter `1.10.14`, and `io_pdx_mesh` `0.91.0` archive checksum `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`. Lock evidence recorded in prior package records is dependencies `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`, schema `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`, and adapter config `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.

The discovered adapter schema exposed scene inspection, export, reimport, checkpoint, sanitation, texture, grounding, humanoid-rig, and action operations, but no supported locator/bone-node authoring operation such as `author_locator`, `create_locator`, or `attach_locator`. No unsupported operation or unrestricted Blender path was attempted. Exact adapter support for a non-deforming named muzzle node is therefore unverified and unavailable under the current route gate.

## Required recovery order using existing geometry

1. Parent resolves the adapter checksum mismatch through the repository-owned installation/verification path and reruns the mandatory lock checks; no substitute adapter or unrestricted Blender route is acceptable.
2. After verification, duplicate an accepted V13 actual-byte checkpoint into a dated Alien recovery checkpoint and inspect the accepted armature to identify the actual gun-bearing bone. The accepted gun-bone name, locator name, and muzzle coordinate/axis are currently unknown and must be measured from the integrated pistol.
3. Add one non-deforming, named muzzle node/locator parented to that measured gun-bearing bone, preserving the accepted mesh, material, texture maps, armature, scale, and provider actions. Do not reuse the rejected Empty or its coordinates without direct accepted-checkpoint evidence.
4. Export and reimport the candidate `.mesh`, then prove that the named node survives the actual mesh bytes. Compare before/after geometry metrics and mesh/material/map checksums, requiring 59,999 triangles, 59,451 exported vertices, unchanged `PDXmat_char1.002`, unchanged map hashes, and unchanged bounds within the exporter’s documented byte-normalization behavior.
5. Reimport all seven existing `.anim` outputs against the candidate mesh without editing their source motion. Capture normal-scale visual proof and close-up discharge-axis/contact samples at `laser_attack` frame 145 and `support_attack` frame 50 at 30 FPS, including the gun contact and muzzle direction. The locator must follow the muzzle at both samples.
6. Preserve the truth that `defend` is `Combat_Stance` and non-firing. Record each action’s byte reimport separately and retain the seven distinct role bindings.
7. Parent performs repository/MCP consumer review and wires `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and the sourced laser audio only after locator/export evidence is accepted. The user owns all live/in-game acceptance; parent owns repository/MCP and consumer-wiring review only.

## Gate matrix and ownership

| Gate | State | Evidence or next owner |
|---|---|---|
| Accepted V13 geometry/material preserved | proven | accepted mesh, final manifest, map hashes above |
| Seven distinct provider actions retained | proven at source/reimport-evidence level | seven role records above; no replacement motion |
| Firearm mesh present | proven | integrated cyan-tipped pistol in accepted V13 mesh |
| Accepted gun-bone name and muzzle coordinate/axis | unknown | parent-owned accepted-checkpoint inspection after route verification |
| Named locator survives actual `.mesh` byte reimport | blocked | no accepted locator export exists; requires verified export/reimport |
| Attack/support muzzle follow proof | blocked | requires frames 145 and 50 close-up evidence |
| Particle/light runtime attachment | unmet | definitions exist but are unbound; parent owns wiring |
| Sourced laser audio runtime mapping | unmet | sourced candidate exists; parent owns consumer wiring and synchronization review |
| Bespoke counter package | parent-reviewed | no regeneration; independent of 3D acceptance |
| Live/in-game acceptance | not performed | user-owned; no game launch or logs used |

## Deliverables and cost

Only this handoff is created: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_alien_muzzle_recovery_2026-09-02.md`. No new checkpoint, export, `.mesh`, `.anim`, texture, audio, counter, runtime, or configuration file was created. No provider credits were estimated or consumed, and no Blender or Meshy operation was run.

This is an inventory/recovery handoff, not a 3D runtime certification or overall Event 016 completion claim.

## Follow-up locked-checksum diagnosis (2026-09-02)

The apparent adapter checksum mismatch is a Windows line-ending conversion, not an unreviewed code update or a stale generated adapter hash. `git status` reports working-tree `M` entries for `.tools/3d_pipeline/adapter/normalization_convergence.py`, `.tools/3d_pipeline/config/dependencies.lock.json`, and `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, but the normalized content diff and cached diff are empty.

Repository configuration has `core.autocrlf=true`, and `.gitattributes` does not assign a text or `eol` rule to these Python and JSON files. The checked-out files contain CRLF bytes while the committed blobs contain LF bytes. The current raw SHA-256 values are `5D014E0D1058AB0C58FFBB774A1AC8AB3E8536A03F9FDA524488F835725E33D3` for `normalization_convergence.py`, `21DFC25B66294EC4927C578BDD83FBF3B5D37D2040946EB8DAAFBA02A8C4FEE2` for `dependencies.lock.json`, and `1936B5978FAE8EA88C557697E35DAA4C4AA01ECFA542E708F8397219976CEBD7` for `meshy_tool_schema.lock.json`.

After CRLF-to-LF normalization, those exact files hash to `91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`, `98FB949D0ABBF43DCF65F3B8FCD48487051165173A5C0377BF5690FF5838F938`, and `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`, respectively, which match their committed `HEAD` bytes and the locked adapter/schema expectations. The adapter file has no post-creation source commit after `a3e0a1497b6926b025070267eb9c75bd00b77c93` (`Harden dual-source Blender preparation`, 2026-08-24); the latest working bytes are that same implementation after line-ending conversion.

The verifier contract explains the false failure: `verify_environment.py` compares each locked `source_sha256` entry to `lib/paths.py::sha256_file`, and `sha256_file` reads raw bytes with `open("rb")` and performs no text normalization. Therefore the lock correctly records canonical repository LF bytes, while a default Windows CRLF checkout fails the raw-byte comparison. This is a verification/environment contract mismatch, not evidence that `normalization_convergence.py` was changed or that its lock entry is stale.

Do not refresh the lock to the CRLF digests. The parent should either run the verifier from an LF-preserving checkout/working copy or propose a reviewed cross-platform checksum contract that hashes Git-clean canonical bytes for locked text sources while continuing to hash binary artifacts byte-for-byte. Until one of those repository-owned verification paths passes unchanged lock evidence, the adapter route remains gated and no adapter operation was invoked in this diagnosis.

## Exact locator implementation and current adapter gap

The locked extension is `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh`, version `0.91.0`, with locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`. Its `pdx_blender/blender_import_export.py::get_locators_info` already serializes Blender Empty objects into locator records with `name`, `p`, `q`, and optional `tx`; a bone-parented Empty is recognized by `obj.parent_type == "BONE"` and records `obj.parent_bone` as `pa` while converting the transform to bone-local space.

The same extension’s `export_meshfile` writes those records under the `.mesh` `<locator>` root, and `import_meshfile(..., imp_locs=True)` calls `create_locator`. `create_locator` reconstructs a `PLAIN_AXES` Empty, sets `parent`, `parent_bone`, and `parent_type = "BONE"`, then restores the coordinate-swapped transform. Thus the approved `io_pdx_mesh` extension already has the necessary locator file-format path; it does not require an extension replacement.

The current adapter does not expose a locator-authoring operation. The locked `blender_hoi4_adapter.json` operation list contains export, reimport, checkpoint, rig, action, grounding, and inspection operations, but no `author_locator`, `create_locator`, or `attach_locator`. The current `blender_worker.py::export_mesh` calls `export_meshfile(..., exp_mesh=True, exp_skel=True, exp_locs=True, exp_selected=True)` after selecting only approved working meshes. Because the extension filters locator empties by `obj.select_get()` when `exp_selected=True`, an unselected muzzle Empty would not be serialized even if it existed in the scene. The current `reimport_export` path does pass `imp_locs=True`, so it can recover a locator only after export actually includes it.

The minimal repository-owned capability fix for parent review is a new narrowly allowlisted adapter operation in `chaosx_blender_hoi4_mcp.py` and `blender_worker.py`, with its operation token added consistently to `blender_hoi4_adapter.json` and the source/operation lock evidence. It should open an existing job-relative accepted checkpoint, validate one exact armature and one exact gun-bearing bone, create one non-deforming Empty with a caller-supplied stable name and measured bone-local transform, mark/select only that approved locator for export, save a checkpoint and report `parent_bone` plus the exact local/world transform, and leave geometry, materials, and all actions untouched. The existing `export_meshfile(..., exp_locs=True)` and `reimport_meshfile(..., imp_locs=True)` paths should then be reused unchanged.

The new operation or its report must include `parent_bone`, because the current adapter `inspect` object records expose `name`, `type`, `parent`, `parent_type`, and transform but omit Blender’s `parent_bone`. Export/reimport acceptance must separately prove that the named locator is present in actual `.mesh` bytes and is reconstructed with the intended parent. No such capability fix was authored in this bounded task, and no current operation can safely perform it.

Recommendation: treat the checksum finding as a line-ending verification blocker requiring parent-owned environment/contract resolution, not as permission to alter the adapter or lock in this handoff. After that resolution, implement or explicitly approve the narrow locator operation above, then run the already documented Alien V13 geometry/material/action preservation and frame-145/frame-50 locator-follow proof.

## V13 intake readiness (2026-09-02)

This is a bounded intake audit only. No Blender or Meshy call, model edit, geometry regeneration, provider spend, runtime wiring, or commit was performed.

### Accepted source and checkpoint identity

The authoritative source remains `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md` and its accepted runtime mesh `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh` (SHA256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`).

The exact accepted V13 proof checkpoints are `blender/checkpoints/reimport_v13_firearm_preset_<death|defend|idle|laser_attack|move|retreat|support_attack>_final.blend`. They are actual-byte reimport proof scenes, not approved WORKING source checkpoints.

The proof reports identify the imported armature as `io_pdx_rig`, the mesh as `char1.002`, and the material as `PDXmat_char1.002`; they report 24 bones, 59,451 exported vertices, and 59,999 polygons. No accepted proof checkpoint records both a `chaosx_working` rig and mesh, and no current package manifest names a separate V13 non-proof WORKING checkpoint. Therefore the exact approved WORKING checkpoint requested for locator intake is **missing/not recorded** and is a gate blocker.

The only current evidence containing `chaosx_working` together with `alien_infantry_rig`, `char1.002`, and an Empty named `muzzle` is the rejected `blender/checkpoints/manual_recovery_2026_08_27.blend` lineage and its result JSON. That lineage manually authored replacement actions and stalled topology validation, so it is not an acceptable V13 intake source.

### Rig, firearm, and measurement status

`RightHand` is present in the accepted provider 24-bone name set and is the only evidenced semantic right-hand candidate. The pistol is fused into the accepted mesh, with no separate weapon object, parenting, constraint, or accepted firearm attachment metadata. Consequently, `RightHand` is not yet proven to be the actual gun-bearing parent for a new locator; that relationship must be inspected on an accepted working/source object after the parent-owned route gate passes.

There is no accepted numeric muzzle position, muzzle axis, vertex subset, color/material sample, or locator transform in the V13 evidence. The rejected Aug27 `muzzle` Empty transform is explicitly excluded and must not be reused or treated as a calibration. Existing V13 close-up and action previews prove only the visible cyan muzzle cap; they do not provide an engine locator measurement.

Accepted V13 geometry/material baselines for any later preservation comparison are 59,999 triangles, 59,451 exported vertices, 30,035 position-welded source positions, one UV set, zero degenerate triangles, and the current accepted material/texture hashes already recorded in the manifest: diffuse `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`, normal `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39`, and specular `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D`.

### Allowlisted inspection path and capability gap

After the parent resolves the existing adapter checksum/contract gate, the safe inspection path is the repository-owned `chaosx_blender_hoi4_inspect_scene` operation through `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`, `.tools/3d_pipeline/adapter/blender_worker.py`, and `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd`, using only job-relative checkpoint paths. The current operation can report object transforms, aggregate geometry, materials, armature/action names, weights, pose bones, and previews, but its object report does not expose `parent_bone` and it has no vertex/color/material-region sampler for identifying the fused cyan muzzle cap.

The existing export path selects `chaosx_working` mesh objects and invokes locked `io_pdx_mesh` with `exp_selected=True`, `exp_skel=True`, and `exp_locs=True`. The extension's locator reader/exporter and `reimport_export` path can preserve a selected Empty and its bone-local transform, but the current allowlisted adapter has no locator-authoring operation and an unselected locator can be omitted by the selected export. The exact extension implementation is `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/pdx_blender/blender_import_export.py`, where `get_locators_info` reads Empty transforms and `parent_bone`, and `create_locator` reconstructs them during import.

The minimal parent-owned capability needed for this intake is either a narrow read-only scene query that samples accepted V13 vertex positions plus exact material/color membership around the cyan tip, or a narrowly validated locator-authoring operation that records the measured local/world transform and `parent_bone`, selects only that approved locator, saves a non-proof `chaosx_working` checkpoint, and reuses the existing locked export/reimport path. Neither capability is currently present in the verified adapter surface, and no coordinate or axis may be inferred until it is added and verified.

### Gate summary and ownership

Accepted geometry, accepted material baseline, and all seven semantically distinct provider actions are available as final artifacts and proof evidence. An accepted non-proof WORKING checkpoint, proven gun-bearing parent, numeric muzzle measurement, locator export/reimport candidate, and frame-145/frame-50 follow proof remain unmet. The existing runtime particle/light definitions, sourced audio mapping, and live consumer acceptance remain parent-owned repository review and user-owned in-game acceptance; this intake does not certify any of them.

No additional provider credits were estimated or consumed. Parent owns adapter/config/lock verification, any minimal allowlisted capability addition, repository consumer wiring review, and final live-validation handoff; the user alone owns live/in-game acceptance.

## Accepted V13 export provenance trace (2026-09-02)

The accepted output file exists at `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh`, is 5,478,802 bytes, and is clean in the current worktree. `git log --follow` records one addition, commit `115fc0f5724c284693dcfcc124d1a01f6f3d98f7` (`Add V13 Meshy alien infantry firearm package`, 2026-08-26 15:47:14 +0300), with the accepted mesh SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`.

That commit adds the final export binaries, manifest, provider/action provenance, and reimport validation records, but it does not add a V13 source `.blend`, an `export_mesh` request JSON, or an `export_mesh` result/report. The package’s current `logs/adapter` request inventory contains no accepted `export_mesh` payload whose `output_rel` is `export/v13_firearm_preset/alien_infantry.mesh`. The sole logged `export_mesh` request is `logs/adapter/f8de71553aa541799162ccc3ed1c0420.json`: request `f8de71553aa541799162ccc3ed1c0420`, `blend_rel` `blender/checkpoints/manual_recovery_2026_08_27.blend`, and `output_rel` `export/manual_recovery_2026_08_27.mesh`. That is the rejected Aug27 manual lineage and is not accepted V13 provenance.

The accepted mesh is instead evidenced as an input to seven actual-byte `reimport_export` requests: idle `14f0da7ee55c42d6b156cf830afa3dbd`, support attack `2b1f46f9e6984a158342add202ba8dbc`, death `45f84dfe4b6a4412a0a37aedaad0f6ff`, move `494d325dd20d4d649f2b40cc40fdfe26`, laser attack `557e9557048540f4bba7cd975989d21d`, retreat `d25ea42ad0a54a38bad95bc8e02940af`, and defend `dfbb5f5300c84133ab6ce3b41af1ead9`. Their request payloads specify the accepted `mesh_rel` and the corresponding `.anim`, while their result records name the `reimport_revalidation_2026_08_26_<role>.blend` proof outputs. The separate `validation/reimport_v13_firearm_preset_<role>_final.json` records name the final proof checkpoint files, but neither set identifies the historical source `.blend` that originally produced the accepted `.mesh`.

The current worktree implementation of `.tools/3d_pipeline/adapter/blender_worker.py::export_mesh` returns `exported_checkpoint` as `blender/checkpoints/06_exported.blend` and writes `blender/reports/export_mesh.json` after a successful invocation. Neither `blender/checkpoints/06_exported.blend` nor `blender/reports/export_mesh.json` exists in this package, so these are current contract defaults, not evidence that the accepted V13 export used that checkpoint. No exact accepted V13 `blend_rel` or historical `exported_checkpoint` can be recovered from the bounded records without guessing.

Therefore the prior “no approved non-proof WORKING checkpoint” finding is not an overlooked filename: the accepted mesh is real, committed, and reimport-proven, but its original export-source checkpoint and export request receipt were not preserved or recorded. Do not promote any reimport proof scene or the rejected manual checkpoint as the missing V13 source. Parent-owned intake must choose an explicitly accepted existing checkpoint or create a new locator-only checkpoint from a verified accepted scene, with fresh source and export lineage recorded before any muzzle work.

## Guarded accepted-proof working-copy design (2026-09-02)

This section supersedes only the earlier capability snapshot for the current parent-owned working tree. Parent reports commit `f372565525` and the currently verified route now expose adapter `1.10.15` with `author_locator`; no adapter, Blender, Meshy, provider, or asset operation was invoked for this design audit. Earlier sections retain their historical 1.10.14/no-locator observations and must not be read as a current claim that the parent-owned adapter lacks `author_locator`.

### Existing operation boundaries

`reimport_export` imports an actual `.mesh` and optional `.anim` with `imp_locs=True`, saves a proof scene, and writes a report, but it does not promote the proof scene to an approved `chaosx_working` rig/mesh and does not create a recovery source.

`save_checkpoint` opens a `.blend` and saves a stage-named copy, but the current implementation does not refuse an existing destination, set `chaosx_working`, capture source or output hashes, or emit geometry/material/bone/action equality evidence, so it is not an audited promotion operation.

`inspect_scene` can set `chaosx_working` flags in memory when an action and target armature are supplied, but it does not save a new checkpoint and that metadata side effect is not a durable or audited promotion contract.

`prepare_export_coordinate_checkpoint` is an action-specific PDX coordinate conversion that deliberately changes armature data and action location channels under its scale policy, so it is not a no-change working-copy operation.

`sanitize_runtime_candidate` can sanitize weights and materials, and the general `prepare` route duplicates and normalizes candidate content, so neither satisfies the requested no-geometry/no-weight/no-action/no-coordinate/no-material edit invariant.

`import_animation_action` is an action-transfer operation that can promote a target as a side effect and copies provider action data; it must not be invoked merely to obtain working metadata for this recovery.

The current `author_locator` operation is the smallest existing locator mutation after a valid working checkpoint exists. Its exact payload is `blend_rel`, `checkpoint_rel`, `target_armature_name`, `parent_bone`, `locator_name`, `bone_local_position`, and `bone_local_rotation_xyzw`; it requires a new sibling `.blend`, refuses overwrite, rejects protected or ambiguous rigs, snapshots every action, verifies the bone-local transform round-trip, saves a new checkpoint, and rechecks the source SHA-256. It intentionally does not set `chaosx_working` on the rig or mesh, and `export_mesh` requires both a `chaosx_working` mesh and a `chaosx_working` armature for locator export.

No currently exposed operation therefore both creates a new non-proof `chaosx_working` checkpoint from an accepted reimport proof and emits the required before/after invariants. The smallest safe route is one new guarded, non-provider promotion operation, followed by the existing `author_locator` operation on its output.

### Exact single-operation promotion contract for parent review

The following is a proposed contract only; it was not implemented or run in this bounded task.

| Contract field | Exact value or requirement |
|---|---|
| Input checkpoint | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/reimport_v13_firearm_preset_laser_attack_final.blend` |
| Input checkpoint SHA-256 | `CFF8D96C29A91DD6ACB9E8CE638521AD70171092EB354DC8D787FC113350E748` (`4,361,834` bytes) |
| Accepted validation receipt | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/validation/reimport_v13_firearm_preset_laser_attack_final.json`, SHA-256 `A418B8AAF3E77D9B5550D30329609651818EC16F40DE4E69972C350188E73174` (`6,112` bytes) |
| Runtime mesh receipt | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh`, SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342` |
| Matching action receipt | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_laser_attack.anim`, SHA-256 `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0` |
| Exact input identities | armature `io_pdx_rig`; mesh `char1.002`; material `PDXmat_char1.002`; expected 24 bones, 59,999 triangles/polygons, and 59,451 exported vertices |
| Proposed new checkpoint | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/v13_firearm_preset_alien_locator_working_2026_09_02.blend` |
| Proposed report | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/reports/promote_v13_reimport_to_working_2026_09_02.json` |

The operation must accept only job-relative `.blend` paths, require the input and output checkpoints to be siblings, refuse any pre-existing output, open the input with scripts disabled, and verify the input SHA-256 both before and after saving. The accepted proof file, accepted mesh, validation receipt, and matching action receipt above are immutable inputs and must never be relabelled or overwritten.

The operation must validate exactly one local scene armature named `io_pdx_rig`, exactly one local mesh named `char1.002`, the mesh's armature modifier target, the `PDXmat_char1.002` slot, positive transforms, and the accepted material/image bindings before changing anything. It may set only explicit promotion metadata on those exact existing rig/mesh objects, including `chaosx_working=true` and a source-receipt property; it must not change vertices, polygon indices, UVs, normals, vertex groups, weights, object transforms, armature rest coordinates, bone names/parents, material nodes/image bindings, or action key data.

Before saving, the operation must record a deterministic fingerprint of mesh vertex positions, polygon/index/material assignments, UV layers, normals, bounds, dimensions, object matrices, vertex-group/weight data, armature bone names/parents/rest head-tail coordinates, material names and image bindings, and every action data block present in the input. For the selected `laser_attack` proof, the report currently identifies the action as `io_pdx_rigAction`; this single proof does not establish that all seven actions coexist in one `.blend`.

The action fingerprint must include action names, frame ranges, F-curve data paths and array indices, every key and handle coordinate, interpolation, FPS, and recorded provenance properties. The operation must fail on an unretained action rather than silently losing it, and it must not call `import_animation_action` or import any new action.

The operation must save the new checkpoint with a copy-style save that leaves the source file path and bytes untouched, reopen the new checkpoint, recalculate the same fingerprints, and write a report whose only permitted scene-data difference is the explicit promotion metadata and ordinary `.blend` serialization. Geometry/material/bone/action fingerprints must match exactly or within a documented serialization tolerance; any topology, coordinate, weight, material/image, bone, action-key, action-range, FPS, or provenance drift is a hard failure. The report must include input/output SHA-256 values, byte sizes, object identities, all fingerprints, permitted metadata differences, source immutability result, `new_provider_call=false`, and `status=pass|fail`.

The output is only a working-copy source for subsequent recovery and is not an export approval. Parent may then run the existing `author_locator` against this new checkpoint using an accepted-checkpoint measurement of the actual gun-bearing bone and muzzle-local transform, writing a second new sibling checkpoint; no coordinate may be copied from the rejected Aug27 Empty. The existing `author_locator` report must prove the locator's parent bone, local/world transform, source hash, output hash, and unchanged action snapshot before `export_mesh` is attempted.

The seven accepted `.anim` files remain separate immutable runtime authorities and must be reimported one by one against the later locator candidate mesh. This promotion step neither merges, renames, rewrites, nor certifies the seven roles; the existing role-specific actual-byte proofs remain the evidence for distinct provider motion, with `defend` truthfully retained as non-firing `Combat_Stance`.

### Current gate consequence

The exact accepted source receipt is now identified, so the prior missing-path finding is narrowed from “no source checkpoint recorded” to “accepted laser proof exists, but no current operation can promote it into an audited working checkpoint without adding the guarded promotion contract above.” The Alien V13 locator/export gate remains blocked until parent-owned route verification, promotion evidence, accepted gun-bone/muzzle measurement, locator authoring, selected locator export, and actual `.mesh`/`.anim` reimport proofs are complete.

No provider credits were estimated or consumed, no Blender or Meshy call was made, and no model, material, action, audio, counter, gameplay, runtime, tooling, lock, or configuration file was changed by this design task. The user owns live/in-game acceptance; parent owns the repository/MCP promotion, locator, export/reimport, and consumer-wiring review.

## V13 promotion failure and bounded material diagnosis (2026-09-02)

The locked route health probe passed with adapter `chaosx_blender_hoi4` `1.10.16`, Blender `5.1.2` build `ec6e62d40fa9`, and all four `io_pdx_mesh` operators loaded from the versioned `0.91.0` extension. The hash-bound `promote_accepted_reimport` request used the exact laser proof, validation, mesh, and animation receipts recorded above and failed closed during independent save/reopen invariant comparison; it made no provider call.

The failed promotion evidence is `logs/adapter/b34014549dfb44be99d95b0aac57d7ff.result.json` and `blender/reports/promote_v13_firearm_preset_alien_locator_working_2026_09_02.json`. The proposed output exists as `blender/checkpoints/v13_firearm_preset_alien_locator_working_2026_09_02.blend` with SHA-256 `70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185` and is explicitly unapproved; it must not be used as an `author_locator` source, export source, or runtime candidate.

The promotion report proves that `actions`, `geometry`, `images`, `objects`, `rigs`, and `scene` fingerprints are identical before and after save/reopen: actions `9ABE1B60669EFD0E41C3B235C77B97E2EDA7139BBD101E78C6474B9FD13B3EA7`, geometry `5C075E92F04E0F03C87F9C3E54A13C0BA861D915F1F24CA217EE64F2E54BA7D8`, images `F5140F34B51AF6DE81F0E648ED566FCE05A25CA855A62F2E64810EBEECF5CF7D`, objects `239533D5393151754BBA923CCB7B6C6D8B53BB6AEFC8A8DB18B782A8CB2BBFD2`, rigs `565D676DF2DB60F68C442B04AFE8EC21EC67D68D32B3F4CBE32AE68174371BAF`, and scene `A7C729267E9D1F2BFF4F6FA8C6B944D88618AB55A9B1D7674333F0B8B9823EEF`.

Only the material fingerprint changed, from `7FBC9DCCA9F50802AD566677B0E970628F6EE09A6127A555A167C4F1C65689EA` to `1C98AEF3FE1A8E8C4954A0CD91A7ED7F0BC5385E1A3A77044A7A0308D61F0ABE`. The source inspection request `080c12a86111471ea99641f36d3a651d` reports two material datablocks: an unused default `Material` with no image links and a runtime `PDXmat_char1.002`; the failed-copy inspection request `deaffb66672645998bed0a1af5a84b14` reports only `PDXmat_char1.002`. Blender dropped the unused default datablock during copy/reopen, which explains the material-section hash difference without changing the runtime material.

The runtime material fields are identical in both bounded inspections: `PDXmat_char1.002` binds `alien_infantry_v13_diffuse.dds` to Base Color, `alien_infantry_v13_specular.dds` to Roughness through the specular Alpha channel, and `alien_infantry_v13_normal.dds` through Normal Map; Metallic remains driven by `Separate Color` Blue; the Principled surface remains connected to the same output. The source-only `Material` has no image bindings, no Base Color/Metallic/Roughness/Normal links, Metallic default `0.0`, Specular IOR Level `0.5`, and zero Emission Strength.

This is a promotion-contract failure caused by non-runtime orphan-material loss during `.blend` serialization, not evidence of altered accepted PDX material bytes or permission to skip the material invariant. No tolerance, hash bypass, material repair, datablock deletion, or output relabelling was performed. The adapter owner must make the contract deterministic by either preserving and fingerprinting the complete source datablock set through save/reopen or documenting and testing an explicit non-runtime-orphan policy while retaining exact runtime material/image equality; parent review is required before any retry.

Because the promotion output is unapproved, no gun-bearing bone or muzzle coordinate may be measured from it, and `author_locator`, `export_mesh`, or seven-action reimport must not consume it. The accepted laser proof and all four hashed inputs remain immutable and verified; the next bounded step is the adapter-owner material-contract correction, followed by a fresh new sibling checkpoint path and a new promotion receipt. No provider credits were estimated or consumed, and no production geometry, action, material, audio, counter, runtime, or configuration asset was changed here.

## Production promotion and bounded muzzle-inspection gate (2026-09-02)

The post-freeze environment verifier returned `findings=[]` before the production route call. The accepted laser proof was promoted with adapter request `961b49a74d3f4c968254b4ba4a1e906f` on `chaosx_blender_hoi4` `1.10.17`, and the result is `status=pass`, `source_immutable=true`, and `all_inputs_immutable=true`.

The approved new working checkpoint is `blender/checkpoints/v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.blend` with SHA-256 `70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185` and `4,355,355` bytes. Its report is `blender/reports/promote_v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.json`, and the adapter receipt is `logs/adapter/961b49a74d3f4c968254b4ba4a1e906f.result.json`.

The promotion compared the exact source, validation, mesh, and laser-animation receipts already listed above and preserved all four input hashes and byte lengths. Geometry, action, image, object, rig, and scene fingerprints are exact; the retained material aggregate is exact; the only removed datablock is `Material`, whose pre-save inventory proves native `users=0`, `fake_user=false`, local, unprotected, no tree retention, no ID consumers, and no mesh/object material slots. Its record SHA-256 is `8FB745202B8BA3E154845C27D5AA32DBD9BDC2F236FC89DB8FE4227D1D830A9C`. The runtime `PDXmat_char1.002` record is retained exactly with native `users=2`, `fake_user=true`, the `char1.002` mesh slot, and the three accepted DDS bindings.

The prior failed candidate `blender/checkpoints/v13_firearm_preset_alien_locator_working_2026_09_02.blend` and its failure report remain untouched, unapproved, and excluded from every subsequent operation.

### Approved-working inspection evidence

The read-only inspection request `df5d1c100cd24d13bb4a3e87de399ed7` opened only the approved retention-checked checkpoint with `io_pdx_rigAction` at `laser_attack` frame `145` and rendered `blender/previews/v13_muzzle_inspection_laser_145_front.png`, `blender/previews/v13_muzzle_inspection_laser_145_left.png`, and `blender/previews/v13_muzzle_inspection_laser_145_three_quarter.png`. The normal-scale views visibly retain the integrated cyan-tipped pistol, trigger-hand contact, support-hand contact, and the accepted body geometry; they are inspection evidence, not locator or runtime acceptance.

The inspected working scene has armature `io_pdx_rig`, mesh `char1.002`, material `PDXmat_char1.002`, 24 bones, 59,999 triangles, 59,451 vertices, one `map1` UV layer, and no existing locators. The working mesh still uses the exact `io_pdx_rig_skin` armature modifier targeting `io_pdx_rig`; no separate firearm object exists.

At frame `145`, the pose report records the semantic right-hand candidate `RightHand` at world head `[-0.6533132195472717, -0.025624103844165802, 5.138009071350098]` and tail `[-0.5280998349189758, -0.24190038442611694, 5.1312174797058105]`. The support-hand candidate `LeftHand` is at world head `[0.7098851799964905, -1.3259068727493286, 5.109981060028076]` and tail `[0.7902715802192688, -1.562125921276855, 5.0945353507995605]`. These are accepted current-rig pose-bone observations only; `RightHand` remains a candidate and is not promoted to an accepted gun-bearing parent by visual inference.

### Exact remaining capability blocker

The locked `inspect_scene` operation reports aggregate geometry, object transforms, material links, weights summaries, pose-bone head/tail transforms, action metrics, and existing locator records, but it does not expose per-vertex positions, UVs, vertex-group weights, texture-pixel membership, face/material indices, or a deterministic mesh-region selector. The accepted pistol is fused into `char1.002` and shares the runtime material, so the current output cannot identify the barrel endpoint or discharge axis as a numeric point from the mesh itself.

`author_locator` correctly requires an explicit measured `bone_local_position` and unit quaternion and refuses implicit normalization or guessed coordinates; it cannot derive those values from the fused pistol. The rejected Aug27 Empty coordinates remain excluded. No exact muzzle point, axis, or gun-bearing parent was therefore supplied, and no `author_locator` call was made.

The minimal parent-owned adapter capability needed before locator authoring is a read-only accepted-checkpoint mesh-region inspection that returns deterministic evaluated vertex/face records for `char1.002` at requested action frames, including vertex index, world/source position, UV, normal, material index, vertex-group weights, and sampled diffuse/attribute identity sufficient to select the cyan pistol muzzle; it must also return the selected endpoint, axis, and bone-local transform against `io_pdx_rig` without mutating or saving the source. The same operation must provide frame `145` for `laser_attack` and frame `50` for `support_attack`, with exact source/action receipt binding, so the later locator report can prove follow-through rather than rely on preview pixels.

Until that bounded sampler or an equivalent parent-verified measurement operation exists, the approved working checkpoint is ready but the muzzle gate remains `blocked`: do not call `author_locator`, `export_mesh`, or seven-action reimport with a guessed point or axis. No provider credits were estimated or consumed, no geometry/material/action edits or runtime wiring were made, and the user remains the sole owner of live/in-game acceptance.

## Read-only frame-145 material QA (2026-09-02)

This QA inspected the approved retention-checked working checkpoint and immutable texture files only. No adapter or Blender operation was invoked during the adapter source-patch window, no checkpoint or texture was written, and no material, mesh, action, runtime, audio, or counter file was changed.

The approved working checkpoint is `blender/checkpoints/v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.blend` with SHA-256 `70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185`. The inspected frame-145 preview is `blender/previews/v13_muzzle_inspection_laser_145_three_quarter.png`. The older failed promotion path has the same bytes hash, but its path, report, and receipt remain rejected; only the retention-checked sibling path and receipt are approved.

### Exact texture inputs and material bindings

The immutable provider source set is under `provider/downloads/v13_firearm_revalidation/remesh_accepted_textures/`: `base_color.png` (2048x2048 RGBA, SHA-256 `A17B3AEEB21E8BD8A2413AFA8DC06F63B920FE899E9DA3A04B6EC28FDC9213D2`), `metallic.png` (4096x4096 L, SHA-256 `61CA0F39FE758B51CD3E8A1E488ED12EC54551F0F2E6FB77D1915F36414D9E3C`), `roughness.png` (4096x4096 L, SHA-256 `0EC40386FD9A3C5465439EB20371C72E5904A1C40B77314A025C12D7717D0A88`), `metallic_roughness.png` (4096x4096 RGBA, SHA-256 `A673A8BF44A24B715E873A71D1BCC0F0470549BEFB6E714A7CEE5154AEEFDABC`), and `normal.png` (2048x2048 RGB, SHA-256 `8B4C7854F3D40AC91643EDE7532532C21DDFC3C3E13DB5B252914A94078D5ADB`).

The current exported maps are `export/v13_firearm_preset/alien_infantry_v13_diffuse.dds` (SHA-256 `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`), `export/v13_firearm_preset/alien_infantry_v13_specular.dds` (SHA-256 `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D`), and `export/v13_firearm_preset/alien_infantry_v13_normal.dds` (SHA-256 `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39`). Each is 1024x1024, 32-bit uncompressed BGRA, 4,194,432 bytes, and uses the current PDX material image names.

The read-only inspection receipt `logs/adapter/df5d1c100cd24d13bb4a3e87de399ed7` reports material `PDXmat_char1.002` on mesh `char1.002`: diffuse Color feeds Principled Base Color, specular Blue from `Separate Color` feeds Metallic, specular Alpha feeds Roughness, normal feeds the Normal Map node, and the Principled surface feeds the output. This is the only runtime material slot; the removed default `Material` was a native zero-user orphan and is covered by the retention-aware promotion receipt.

### Decoded channel comparison

- The current diffuse DDS is an exact pixel/channel match to `remesh_accepted_textures/base_color.png` after the deterministic 2048-to-1024 Lanczos resize. The current and resized-source channel means are identical at R `57.1681`, G `59.0746`, and B `46.7418`; the raw 2048 source means are slightly different because resizing is part of the export path.
- The current normal DDS is an exact pixel/channel match to `remesh_accepted_textures/normal.png` after the deterministic 2048-to-1024 Lanczos resize: decoded RGBA MAE `0`, RMSE `0`, and exact pixel fraction `1.0`. It is conventional RGB normal data with non-zero R/B and opaque A, not the repository packer's PDX-normal layout of R `0`, G `source R`, B `0`, A `source G`.
- The current specular DDS has R `0` everywhere and G `32` everywhere. Its Alpha channel is an exact pixel/channel match to the resized provider roughness map, with mean `99.7356`, median `106`, p95 `119`, and max `154`.
- The current specular Blue channel preserves the resized provider metallic pattern with correlation `0.999759` and approximately `0.35008317 * metallic + (-0.02243)`. Current Blue mean is `5.9904`, p95 `30`, max `51`, median `1`, and `504,578` of `1,048,576` pixels are zero. The provider metallic source before this attenuation has mean `17.2145`, p95 `88`, max `138`, and is visibly patchy across its UV islands.
- The current repository packer contract in `.tools/3d_pipeline/pack_pdx_material.py` and `.tools/3d_pipeline/run_pilot.py` is R `0`, G `32`, B `metallic`, A `roughness`; no `0.35` metallic-strength operation appears in that contract or in the inspected current job evidence. The Blue attenuation is therefore a provenance gap requiring parent review, not a proven intentional grading step.

### Vanilla precedent and visual finding

The closest normal German infantry precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/GER_infantry_alt_0_specular.dds`, consumed by `PdxMeshAdvanced` through `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`. Its decoded Blue channel is sparse and low (median `0`, p95 `0`, mean `0.7893`, max `156`), while the Alien Blue mask is more widespread but still low-to-moderate (median `1`, p95 `30`, max `51`). The Alien Alpha roughness is substantially higher than the GER reference (median `106` versus `40`), so the frame-145 glints are not explained by a simple low-roughness or full-metal body map.

The frame-145 patchy silver appearance is materially source-driven because the diffuse, normal, roughness, and metallic spatial patterns are preserved from the immutable remesh source, and the source metallic map itself contains broad patchy islands. Blender's Principled preview lighting and exact source normal can amplify those islands into mirror-like highlights, so the visual strength is also preview-sensitive. This is not evidence of a roughness-as-specular channel swap: the PDX R/G layout is correct, Blue follows metallic rather than roughness, and Alpha follows roughness. The later PDX convention trace resolves the normal question: the current conventional-RGB runtime normal is also an engine-facing packing defect, while the unexplained Blue attenuation remains a separate provenance gap; the accepted runtime material remains `needs_user_review` pending parent review and a deterministic correction from the immutable sources.

No source-intent claim beyond the byte/channel evidence is made, and no material acceptance or live/in-game acceptance is claimed. Parent owns the repository/MCP material and runtime-consumer review; the user alone owns live/in-game acceptance. No provider credits were estimated or consumed.

## PDX normal convention resolution (2026-09-02)

This bounded source check resolves the normal-map ambiguity using the installed vanilla shader, the exact vanilla infantry material files, the locked `io_pdx_mesh` 0.91 importer, and the repository packer. No adapter or Blender operation was invoked, and the accepted Alien source/runtime bytes remain unchanged.

### Engine-side channel contract

The installed shader is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/FX/pdxmesh.shader`. `PdxMeshAdvanced` enables `EMISSIVE` and `PDX_IMPROVED_BLINN_PHONG` at lines `787-793`; the pixel path samples `NormalMap` at lines `470-476`, takes `vEmissive = vNormalMap.b`, and calls `UnpackRRxGNormal(vNormalMap)`. `standardfuncsgfx.fxh:311-315` defines that decoder as `x = G * 2 - 1`, `y = -(A * 2 - 1)`, and `z = sqrt(saturate(1 - x*x - y*y))`. The normal's Blue channel is therefore emissive in this shader family, not tangent-Z, and Red is not consumed by this decoder.

The same shader's improved-lighting path uses specular Green for `SpecRemapped` and specular Blue for `MetalnessRemapped` at `pdxmesh.shader:523-527`; the repository's R `0`, G `32`, B `metallic`, A `roughness` specular contract is consistent with that use. The engine-side normal contract is consequently consumed channels G `tangent-X`, A `tangent-Y` with the shader's Y inversion, B `emissive`, and R unused. A non-emissive PDX normal must have B `0`; R may be left nonzero by legacy vanilla files, although the repository packer safely zeros it.

### Vanilla infantry proof

The default `infantry_rifle_entity` binds `generic_western_european_rifle_infantry_mesh` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset:11-13`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx:76-83` binds that mesh to `gfx/models/units/western_european_infantry.mesh`. The binary mesh material record contains `PdxMeshAdvanced` at byte offset `133438`, `western_europe_infantry_normal.dds` at offset `133517`, and `western_europe_infantry_spec.dds` at offset `133567`.

The exact default normal is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_europe_infantry_normal.dds`, 256x256, DXT5, 87,536 bytes, SHA-256 `3F68F72485136EC7B2C70C9051E891AE5C8C5E1D18196EF96F6F40663D6136BD`. Its decoded channels are R mean `127.8575`, G mean `127.5130`, B exactly `0` for all `65,536` pixels, and A mean `127.7637`; G/A are centered normal channels exactly where the shader consumes them.

The normal-German alternate material is explicitly declared with `texture_normal = "GER_infantry_alt_0_normal.dds"` and `shader = "PdxMeshAdvanced"` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx:1983-1989`. Its exact normal is `gfx/models/units/GER_infantry_alt_0_normal.dds`, 512x512 DXT5, 349,680 bytes, SHA-256 `80F3579B07A4FF1AF8ABC388EE4343E46F944AF2D977CC0ADE864CE7A6FDF366`; decoded B is also exactly `0`, while R/G/A means are `126.7283/127.0433/127.1993`. Both installed vanilla infantry normal precedents therefore disprove treating a conventional RGB normal's Blue and opaque Alpha as the engine-facing PDX `n` layout.

### Locked importer versus working-preview route

The locked extension manifest is `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/blender_manifest.toml`, version `0.91.0`. Its `pdx_blender/blender_import_export.py:620-646` loads texture data with `alpha_mode = "CHANNEL_PACKED"` and `is_data = as_data`. Its PDX material decoder at `:719-742` creates a Separate Color node, feeds texture Green to Combine Color Red, sets Combine Color Blue to `1.0`, feeds texture Alpha to Combine Color Green, and sends the reconstructed RGB to Blender's Normal Map node. This is the Blender-side equivalent of the engine's G/A decoder, not a conventional-RGB pass-through.

The repository's `.tools/3d_pipeline/pack_pdx_material.py:211-249` states the same conversion explicitly: a conventional provider RGB normal must become R `unused_zero`, G `source.R`, B `unused_zero`, A `source.G`. Its `prepare_texture_source_rels` path keeps the conventional RGB map in the Blender working scene and selects the packed companion only for the runtime DDS. Conversely, `.tools/3d_pipeline/adapter/blender_worker.py:1167-1179` directly links a supplied working `normal` image Color to Blender's Normal Map node; that direct link is appropriate only when the supplied image is the conventional provider source, not when a runtime PDX-packed texture is being inspected as if it were conventional.

### Alien consequence

The current `export/v13_firearm_preset/alien_infantry_v13_normal.dds` is an exact 1024x1024 resized match to the immutable conventional provider `provider/downloads/v13_firearm_revalidation/remesh_accepted_textures/normal.png`: decoded R/G/B means `126.5486/125.9786/237.3853`, A is `255` everywhere, and decoded MAE/RMSE against the resized source are both `0`. Under the installed `PdxMeshAdvanced` shader, this means source G is incorrectly consumed as tangent-X, Alpha `255` forces tangent-Y to `-1` after the shader inversion, and source normal Blue is incorrectly consumed as emissive with mean `237.3853/255 = 0.9309`. This is a real engine-facing normal/material defect and a plausible contributor to the frame-145 bright or mirror-like surfaces, separate from the source-derived metallic islands and unexplained specular-Blue attenuation documented above.

### Smallest deterministic correction recommendation

The correction is now materialized only as the fresh, unlinked source-first candidate documented in the following section, while the accepted current DDS remains untouched. The exact channel operation after the deterministic 2048-to-1024 Lanczos resize is R `0`, G `source.R`, B `0`, A `source.G`; the candidate statistics and hashes are recorded below.

This remap preserves the immutable provider normal data, changes no mesh, geometry, weights, actions, material node identity, or weapon, and requires no provider call. Parent's follow-up should reimport the candidate runtime texture/material path through the locked route and compare frame-145/50 visuals and engine-facing channel reports. Until that review, material acceptance remains `needs_user_review`; no live/in-game acceptance is claimed.

## Source-first PDX normal candidate (2026-09-02)

This bounded technical pass created a new normal-texture candidate from the immutable provider normal only. No accepted texture, mesh, animation, checkpoint, material, runtime file, provider task, Blender operation, adapter operation, or source file was changed, and no provider credits were estimated or consumed.

### Candidate lineage and exact bytes

The immutable source is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/downloads/v13_firearm_revalidation/remesh_accepted_textures/normal.png`, 2,048x2,048 RGB, 6,532,108 bytes, SHA-256 `8B4C7854F3D40AC91643EDE7532532C21DDFC3C3E13DB5B252914A94078D5ADB`.

The conventional RGB source was resized first to the consumer size of 1,024x1,024 with Pillow `11.1.0` and deterministic `Image.Resampling.LANCZOS` into `textures/closure_candidates/pdx_normal_2026_09_02/alien_infantry_v13_normal_sourcefirst_1024.png`, 1,945,142 bytes, SHA-256 `6C67EE64FB08D0D6FAF901F6C6F6469C6BC6E75756E6EF558FB3ADD96D8D4E10`.

The repository packer `.tools/3d_pipeline/pack_pdx_material.py` (current script SHA-256 `AAECA8F48D2075BEC928903D0DBC0DA4E92CA801F5311ACE3898976143DC5B57`) then produced `textures/closure_candidates/pdx_normal_2026_09_02/alien_infantry_v13_normal_pdx_sourcefirst_1024.png`, 1,773,407 bytes, SHA-256 `EE778C7C2D18578AF6FC09661A0C58B47A2AAFD9CB195F91FD0F99560C256569`.

The pack layout was exactly R `0`, G `sourcefirst.R`, B `0`, and A `sourcefirst.G` at 1,024x1,024; no packed RGBA image was resized after this operation.

The existing event-assets converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` (current script SHA-256 `347C68404FDFC4A458E584EA22A5279C4F2EB6FC87273DBBD7D3799D920BB82C`) converted that already-sized PNG without width or height arguments. The verified fallback backend was FFmpeg `N-123778-g3b55818764-20260331` because `texconv` was unavailable, producing `textures/closure_candidates/pdx_normal_2026_09_02/alien_infantry_v13_normal_pdx_sourcefirst_1024.dds`, 4,194,432 bytes, SHA-256 `56CF3A704B6BFD4F05B7FD91456139F2DD362CF54CDC5E273B3B763958462CCB`.

The candidate DDS header is 1,024x1,024, `dwFlags=0x100f`, pitch `4096`, uncompressed 32-bit BGRA (`pfFlags=0x41`, RGB bits `32`, masks `[16711680,65280,255,4278190080]`, caps `0x1000`), with header SHA-256 `6D646FF419F94B00906EF423A38637C4E48DDAAA07705C833CF6034B25F73B18`. That header is byte-identical to the accepted current `export/v13_firearm_preset/alien_infantry_v13_normal.dds`, whose whole-file SHA-256 remains `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39`.

### Deterministic channel proof

The resized conventional source has R mean `126.548618` and quantiles q01/q05/q25/q50/q75/q95/q99 `19/59/117/127/136/194/235`; G mean `125.978627` and quantiles `21/62/117/127/135/188/231`; B mean `237.385258`; and opaque A `255`.

The packed PNG has R and B exactly zero, G exactly equal to the resized source R, and A exactly equal to the resized source G. Its decoded channel means are R `0`, G `126.548618`, B `0`, and A `125.978627`, with the same quantiles listed above for G and A.

The final DDS was decoded directly from its uncompressed BGRA body using the header masks. The decoded DDS was byte-for-byte equal to the packed PNG RGBA pixels, with exact G-to-resized-source-R and A-to-resized-source-G equality and R/B zero across all 1,048,576 pixels. This proves that no second alpha-aware interpolation or channel ringing occurred.

The immutable source hash remains `8B4C7854F3D40AC91643EDE7532532C21DDFC3C3E13DB5B252914A94078D5ADB`, and the accepted runtime normal hash remains `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39` after candidate creation.

For installed vanilla convention comparison, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_europe_infantry_normal.dds` is 256x256 DXT5, SHA-256 `3F68F72485136EC7B2C70C9051E891AE5C8C5E1D18196EF96F6F40663D6136BD`, with decoded R/G/A means `127.8575/127.5130/127.7637` and B exactly zero. The normal German alternate `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/GER_infantry_alt_0_normal.dds` is 512x512 DXT5, SHA-256 `80F3579B07A4FF1AF8ABC388EE4343E46F944AF2D977CC0ADE864CE7A6FDF366`, with decoded R/G/A means `126.7283/127.0433/127.1993` and B exactly zero. The candidate follows this installed PdxMeshAdvanced convention by keeping engine-consumed normal data in G/A and clearing non-emissive B.

The earlier `alien_infantry_v13_normal_pdx_1024_exact.dds` probe, SHA-256 `BD0D3886CF34A803C643545680A664D3BD758217B8B070828F832EBBA20B8D23`, is rejected because packed RGBA was resized with ordinary interpolation and biased the data-valued G/A channels. The earlier `alien_infantry_v13_normal_pdx_1024.dds` probe, SHA-256 `E5E0B8138BB5E1652641EDBB120D04414A276A54B38B1473D792FE3C749E4529`, is rejected because converter-side scaling introduced nonzero R/B ringing. Neither rejected probe may be relinked or consumed.

### Parent-owned relink and export/reimport plan

The candidate DDS is not yet a runtime material replacement and was not linked into the accepted checkpoint. Parent should use only a new sibling working/derived checkpoint, retain the approved `v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.blend` and its receipt as immutable, and relink only the PDX normal image to `alien_infantry_v13_normal_pdx_sourcefirst_1024.dds` after review.

The relinked candidate must preserve the current `PDXmat_char1.002` node graph, accepted diffuse/specular/metallic/roughness bindings, mesh/object/rig/action fingerprints, and accepted image identities other than the explicitly reviewed normal image. The engine-facing material report must show the locked io_pdx_mesh G/A normal decoder and non-emissive B zero; the `.mesh` itself does not embed the DDS bytes, so parent-owned runtime consumer mapping remains separate.

After relink, parent should export and reimport through the locked Blender HOI4 adapter and io_pdx_mesh path into another unique output, compare geometry/material/object/rig/action invariants and source immutability, and reimport each of the seven immutable accepted `.anim` bytes against the candidate mesh. Any material, geometry, action, image-binding, or serialization drift beyond the reviewed retention rule is a hard failure; do not repair, bypass, or overwrite the accepted artifacts.

Only after parent approves the material evidence and the bounded mesh-region/locator measurements should the candidate be carried into the locator export and frame-145 laser/frame-50 support follow-through proof. This texture pass does not prove muzzle alignment, animation acceptance, runtime wiring, or live/in-game acceptance.

### Gate status

The source-first normal candidate passes the technical source, size, header, channel-layout, decoded-byte, and source-immutability gate. Material relink, mesh export/reimport, seven-action reimport, locator proof, runtime consumer wiring, and user live acceptance remain pending parent review and must not be inferred from this candidate alone.

## Read-only Alien mesh-region evidence (2026-09-02)

This bounded sampler pass ran only after the source-first texture candidate was verified and after `python -B .tools/3d_pipeline/verify_environment.py` returned exit code zero with `findings: []`. The environment report is `.tools/3d_pipeline/reports/environment_report.json`. Adapter `chaosx_blender_hoi4` was version `1.10.18` and Blender was `5.1.2` build `ec6e62d40fa9`; no source, checkpoint, mesh, animation, texture, runtime, or provider asset was written by these inspections.

### Native action and immutable checkpoint

The ordinary read-only `inspect_scene` request was `715deeca05e94431b12f3104a5090550` against `blender/checkpoints/v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.blend`, with `io_pdx_rig`, `io_pdx_rigAction`, and frame `145`. It returned native action SHA-256 `EC91F36EB20B4131CC4329852CD265B287991D55AD8674239FD17FCFC5C70FB9`, which is the existing curve-slot/key/interpolation identity and not an exported `.anim` file hash. The action is 30 FPS, frames `1-236`, and the inspection showed one `io_pdx_rig` armature with 24 bones, one `char1.002` mesh with 59,999 triangles and 59,451 vertices, `PDXmat_char1.002`, one `map1` UV layer, and no locators.

The sampler echoed source SHA-256 `70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185`, source byte count `4,355,355`, topology SHA-256 `047DA36DD69934B61C72321F02C958E6D970C5D52C0EFB2BFC172DB8DA2417A0`, and action-integrity SHA-256 `0517C7546F8CF47FE017096F99A494428F7BD2E4BC1D60C689ED6A7972357F27`. Every sampled receipt reported `source_immutable=true`, `all_actions_unchanged=true`, `checkpoint_saved=false`, and `new_provider_call=false`.

### Bounded frame-145 selector

The read-only selector was `mesh_name=char1.002`, `bone_name=RightHand`, weight range `RightHand 0.05-1.0`, and a WORLD AABB of `min=[-2.5,-1.5,4.5]`, `max=[-0.2,0.8,6.0]` at frame `145`. The initial count request was `f02706f31758463b85b6cd109acd887b` and returned `3,483` matched vertices; the full bounded page sequence was `f48eab60c16e46809b45c5ec5ddd2251`, `43381f25002749229728264cc2955ae4`, `22452bedd1e64218ac4d6e49f74e03c6`, `5469db0ba1e4497b989876fd42733eba`, `6fb21951953d4cccbb80828f3fa0980f`, `3392930cd5bd40759d7b4e9d93a93445`, `b5b6f01d8173422ebae72c92afc8899e`, `60c4b43cfcf54f67a2de3d3472e54ce6`, `a6ccea102e4345d3a568a2c443dba3ef`, `d2f7d20fe0b845ce9e3ac5f63c371cd8`, `321ad8d711c64d95922d3516a7f0a5c9`, `8a42365f69054ee8b531a47b8c732553`, `1d9bce4ed04745329b26342452fdf573`, and `571e0579d560419f91de750b225ebd28`. The final page returned 155 vertices after 13 full 256-vertex pages, with no corner-cap truncation.

The selector's complete matched-index SHA-256 was `057462FF79697BF35F3BEA3E7940016B0595056488D8AE5C3364C10CEA6209CC`; all 3,483 records retained source positions, evaluated frame-145 positions, source/evaluated normals, `map1` UVs, material index/name, and complete original vertex-group weights. This is an observation set only; no adapter measurement set was supplied and no muzzle transform was produced.

### Observed firearm-cap candidate

A small connected nine-triangle patch within the bounded records is a measured firearm-cap candidate, not an approved semantic muzzle. Its exact source vertex indices are `[3089,3090,3091,3121,3122,3139,3143,3144,3164,3166,3185]`, with polygon indices `[3053,3082,3083,3102,3104,3125,3126,3129,3148]` and 27 returned corners. The complete cap UV range is `u=[0.69582701,0.70846099]`, `v=[0.01505297,0.02476299]` on `map1`.

The earlier read-only UV-to-diffuse crosswalk against unchanged `export/v13_firearm_preset/alien_infantry_v13_diffuse.dds` (SHA-256 `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`) sampled `x=round(u*1023), y=round(v*1023)` and provisionally reported cyan at vertices `3143` (`[138,224,222]`) and `3166` (`[134,221,218]`). The subsequent importer/exporter trace below shows that this direct-V sample is not the correct top-down DDS mapping for Blender-space `map1` UVs, so that cyan identification is superseded and must not be used as muzzle proof. The immutable source for that same map remains `provider/downloads/v13_firearm_revalidation/remesh_accepted_textures/base_color.png`, SHA-256 `A17B3AEEB21E8BD8A2413AFA8DC06F63B920FE899E9DA3A04B6EC28FDC9213D2`. The cap remains semantically unapproved because the mesh has one shared PDX material and many source islands.

The cap evaluated frame-145 world centroid is `[-0.754595735,-0.025545922,5.076822758]` with AABB `min=[-0.765802979,-0.036115110,5.054632187]`, `max=[-0.734954596,-0.018867612,5.102562428]`. Its source centroid is `[-2.348053260,0.525383142,5.389686498]` with source AABB `min=[-2.357996702,0.503818274,5.367467403]`, `max=[-2.342484474,0.537334204,5.415216923]`. Its current-rig bone-local centroid is `[-0.044960018,-0.049133028,0.097808473]` with AABB `min=[-0.066192225,-0.054262757,0.080107756]`, `max=[-0.022524701,-0.039730296,0.115628347]`.

The cap's evaluated world surface-normal mean, normalized, is `[-0.032444609,-0.949751084,-0.311320134]`; the corresponding normalized bone-local normal is `[-0.293595486,0.813842604,0.501459776]`, and the normalized source-normal mean is `[-0.934225039,0.162002652,-0.317771487]`. These are observed surface normals and useful axis candidates only; the sampler explicitly does not infer a weapon axis or supply a locator quaternion. The cap point-cloud principal in-plane axes were `[0.38082410,0.26745747,-0.88512118]` and `[0.91794886,-0.22437283,0.32714939]`, but their sign/choice is not a semantic gun-up marker, so no stable roll can be accepted from this patch alone.

The cap weights are predominantly `RightForeArm`, not `RightHand`: across all 11 vertices, `RightForeArm` is `0.6874929-0.7382823` (mean `0.7220920`) and `RightHand` is `0.2617177-0.3125071` (mean `0.2779080`). Therefore `RightHand` remains only the bounded inspection candidate; the actual gun-bearing parent is not proven and must not be assumed from this region.

### Support-action boundary and remaining gates

The current approved working checkpoint contains only `io_pdx_rigAction` for the laser proof. The separate accepted support proof is `blender/checkpoints/reimport_v13_firearm_preset_support_attack_final.blend`, 4,000,525 bytes, SHA-256 `FA7C008A0E9BD30DFFB5FABAACD252B48F77F7E7506FBF86DD405EF6544BC9E3`; its validation receipt is `validation/reimport_v13_firearm_preset_support_attack_final.json`, 6,135 bytes, SHA-256 `D656EA0B564426D6A75C9C2166CD17E8C19CBB0644ECEA13BA7529F38701C8FD`; and its accepted action is `export/v13_firearm_preset/alien_infantry_support_attack.anim`, 78,163 bytes, SHA-256 `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061`. The historical accepted support reimport receipt is `logs/adapter/2b1f46f9e6984a158342add202ba8dbc.json`; no support frame-50 mesh-region call was made because the approved working checkpoint and current sampler action binding are laser-only, and the adapter boundary was released for the parent-owned action-phase work.

The frame-145 sampler evidence is sufficient to hand the parent an exact, source-grounded cap candidate and current-rig measurements, but it does not establish a gun-bearing bone, a semantic discharge axis, a stable roll, or an accepted locator. Parent must review the cap/UV evidence, obtain a separate accepted support working source if frame `50` is required, choose explicit disjoint origin/endpoint measurement sets, and only then authorize `author_locator` with a measured bone-local transform. Locator export/reimport, all seven immutable action reimports, normal/close-up follow proof, runtime wiring, and user live acceptance remain open gates. No geometry, material, action, audio, counter, runtime, or configuration fallback was used.

## Isolated normal-relink export candidate and UV convention audit (2026-09-02)

Parent-approved source-first normal correction was staged as a unique sibling candidate without invoking Blender or the adapter. The candidate directory is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset_normal_corrected_2026_09_02/`, with provenance manifest `candidate_manifest.json`. Its `alien_infantry.mesh` is a byte-identical copy of the accepted V13 mesh, SHA-256 `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342`, 5,478,802 bytes; its diffuse companion is byte-identical, SHA-256 `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA`, 4,194,432 bytes; and its specular companion is byte-identical, SHA-256 `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D`, 4,194,432 bytes.

The candidate normal is the verified source-first DDS copied to the exact basename already referenced by the mesh, `alien_infantry_v13_normal.dds`, SHA-256 `56CF3A704B6BFD4F05B7FD91456139F2DD362CF54CDC5E273B3B763958462CCB`, 4,194,432 bytes. The mesh's binary material record already references `alien_infantry_v13_diffuse.dds`, `alien_infantry_v13_normal.dds`, and `alien_infantry_v13_specular.dds`, so this directory requires no mesh edit or node replacement. The accepted `v13_firearm_preset` directory and every accepted proof file remain untouched; the candidate is unreimported and not runtime-approved.

The installed locked `io_pdx_mesh` 0.91.0 implementation at `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/pdx_blender/blender_import_export.py` explicitly flips V in both directions. Export reads Blender UVs and applies `swap_coord_space(tuple(uv))` at lines `285-291`; `swap_coord_space` returns `(u, 1-v)` for a two-component UV at lines `594-609`. Import reconstructs Blender UVs as `[u, 1-v]` at lines `1059-1063`. Therefore the read-only sampler's `map1` values from the imported Blender checkpoint are Blender-space values, while the uncompressed DDS byte rows are sampled top-down with `x=round(u*1023)` and `y=round((1-v)*1023)`.

The prior direct-V cap crosswalk was consequently invalid for cyan identification. Against the unchanged accepted diffuse DDS, vertex `3143` at UV `[0.698160,0.020955]` was `[138,224,222]` under the mistaken direct-V row `y=round(v*1023)`, but `[88,90,66]` under the traced top-down row `y=round((1-v)*1023)`. Vertex `3166` at UV `[0.695905,0.022611]` similarly changed from `[134,221,218]` to `[42,44,26]`. Across the 11 measured cap vertices, RGB means were `(56.455,74.727,69.273)` direct-V versus `(71.091,71.364,50.545)` V-flipped; using the previously stated rough cyan test that both G and B exceed R by 40, the counts are `2/11` versus `0/11`. The earlier cyan-island claim is superseded and cannot identify the muzzle.

The remaining cap measurements are geometric observations only: exact source indices `[3089,3090,3091,3121,3122,3139,3143,3144,3164,3166,3185]`, evaluated frame-145 centroid `[-0.754595735,-0.025545922,5.076822758]`, and dominant `RightForeArm` weights. No gun-bearing bone, endpoint, axis, roll, locator, or authoring input is inferred from the corrected texture crosswalk. Parent may perform the first material-only reimport against this candidate after the adapter 1.10.19 freeze is released; do not proceed to locator authoring or seven-action reimports from this candidate until the first frame-145 visual/material result is reviewed.

## Material-only candidate reimport and frame-145 review (2026-09-02)

The fresh client health gate passed before production work: request `78dc9f6116d2424c82bbc0bf5198c0af`, adapter `chaosx_blender_hoi4` `1.10.19`, Blender `5.1.2`, locked `io_pdx_mesh` `0.91.0`, all four import/export operators present, config SHA-256 `121580FAFFC6FE2DE059F5F6E35E6DFEEF9941F2D11A60F9AC3042185F3636B`, and worker SHA-256 `5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40`. `MESHY_API_KEY` was present and its value was withheld; no provider or paid operation occurred.

The first unique reimport request `e03423a1154f4a75858c667989919132` imported the candidate mesh, all three adjacent DDS companions, and the accepted laser animation, and wrote the frame-1 front/left previews. It failed only when OpenImageIO could not write the first three-quarter PNG, before checkpoint/report save; its request/result logs and partial previews remain preserved and unapproved. No accepted input was overwritten.

The bounded retry request `094aa586290b4d3a8dd6ac702eb6ced9` succeeded with the same candidate mesh and accepted laser animation, using proof name `v13_normcorr_laser_20260902a`. The new checkpoint is `blender/checkpoints/reimport_v13_normcorr_laser_20260902a.blend`, 4,361,825 bytes, SHA-256 `9B9ECF79A1A676956BFE13DF0ECB4EE15C33B81027C8A05C41822D609A32404B`; the adapter validation report is `validation/reimport_v13_normcorr_laser_20260902a.json`, 6,288 bytes, SHA-256 `47CC0044004F761F2B65E8B3E5BFE40FB6ECD514F1302F179E7F5F4B4CC3A716`; and the full reimport result is `logs/adapter/094aa586290b4d3a8dd6ac702eb6ced9.result.json`. The result contains 15 normal-scale previews at frames `1,60,118,177,236` across front/left/three-quarter views.

The successful candidate reimport reports one mesh `char1.002` with 59,999 triangles and 59,451 vertices, one `io_pdx_rig` armature with 24 bones, action `io_pdx_rigAction` at 30 FPS and frames `1-236`, no locators, zero degenerate faces, zero non-manifold edges, zero zero-length normals, and no vertices over four influences. The geometry JSON is exactly equal to the accepted laser reimport geometry, with canonical JSON SHA-256 `78594AFDA1C17A38CBE7A0FD9EA29400535351E7E2E7F72A3571CB4A2EC164DE`; the animation-bound values are also exactly equal after ignoring the retry report's additional empty `locators=[]` field, with canonical JSON SHA-256 `908C51F8EEBD645D15F84D4B9FC23B99ADC11B638907CD6B607EB6105978C5DC`. Mesh, armature, action, object identity, and runtime-texture-staging comparisons are exact after accounting for the adapter's added empty locator field and the deliberately different mesh directory.

The follow-up read-only frame-145 inspect request `8c083fa866524c65b1f0ca8bb907b165` opened only the new checkpoint and rendered `blender/previews/v13_normcorr_laser_20260902a_frame145_three_quarter.png`, 187,103 bytes, SHA-256 `FDA7815E85940E7D67E2A9AE82B8DD71514C549DD10B4268305F69BEEB746CDE`. Its `PDXmat_char1.002` node graph is unchanged: diffuse Color to Base Color, specular Blue to Metallic, specular Alpha to Roughness, and normal through the Normal Map node. The only intended image-binding difference is the three sibling filepaths under `export/v13_firearm_preset_normal_corrected_2026_09_02`, with the candidate normal SHA `56CF3A704B6BFD4F05B7FD91456139F2DD362CF54CDC5E273B3B763958462CCB`; diffuse/specular retain their accepted hashes. The candidate preview appears materially less mirror-like than the old accepted frame-145 three-quarter preview, but this is visual evidence for parent review, not material or runtime acceptance.

This successful pass proves candidate texture decoding, accepted mesh/action reimport, preservation metrics, material-node wiring, and a frame-145 visual checkpoint only. It does not prove a muzzle coordinate, axis, locator, support frame-50 follow-through, seven-action reimport, runtime consumer wiring, or live/in-game acceptance. The candidate checkpoint, report, preview, failed first-attempt evidence, accepted source files, and all prior proof files remain separate and immutable. No geometry, action, locator, runtime, audio, counter, configuration, or provider asset was edited, and no credits were estimated or consumed.

## Bounded laser/support muzzle measurement and parent-release checkpoint (2026-09-02)

This section supersedes the earlier sampler boundary that said support frame-50 evidence was unavailable. The corrected-material laser and support reimports are now separate immutable measurement sources, and every native adapter call in this bounded sequence has ended; no Blender or adapter operation is in flight and the 1.10.19 source freeze is released for parent-owned capability work.

The current route was the locked repository-owned Blender HOI4 adapter 1.10.19 with Blender 5.1.2 and io_pdx_mesh 0.91.0. The completed fresh-client health request was 78dc9f6116d2424c82bbc0bf5198c0af with config SHA-256 121580FAFFC6FE2DE059F5F6E35E6DFEEF9941F2D11A60F9AC3042185F3636B and worker SHA-256 5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40. The environment verifier had already returned exit code zero with findings=[]; no provider or paid operation occurred.

### Immutable reimport sources and visual evidence

The laser measurement source is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/reimport_v13_normcorr_laser_20260902a.blend, SHA-256 9B9ECF79A1A676956BFE13DF0ECB4EE15C33B81027C8A05C41822D609A32404B, with native action SHA-256 EC91F36EB20B4131CC4329852CD265B287991D55AD8674239FD17FCFC5C70FB9. Its accepted source action is export/v13_firearm_preset/alien_infantry_laser_attack.anim, SHA-256 288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0, at 30 FPS and frames 1-236.

The support measurement source was produced by request 50a6735103e548fd86f1889a0770250e from the accepted support action export/v13_firearm_preset/alien_infantry_support_attack.anim, SHA-256 DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061. The new checkpoint is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/reimport_v13_normcorr_support_20260902a.blend, SHA-256 4A4C6AB291BAF3F5FBA37F3D71566B78715D83FCAAD4FBC33701507C7B1EE39D, and its validation receipt is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/validation/reimport_v13_normcorr_support_20260902a.json, SHA-256 6C5AAE06C3BE63993F523387E0C7C54D06E86C9F3F05685195B3ABB2920217CD. The native support action SHA-256 in that checkpoint is BF63F0FFCCE0E49D4A6ACECE744118A44D304689DE8E8ACE15AFE4F46C426D78, at 30 FPS and frames 1-99, and the report contains no locators, 59,999 triangles, 59,451 vertices, and 24 bones.

The normal-scale frame-145 laser three-quarter preview is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/previews/v13_normcorr_laser_20260902a_frame145_three_quarter.png, SHA-256 FDA7815E85940E7D67E2A9AE82B8DD71514C549DD10B4268305F69BEEB746CDE. Its muzzle close-up is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/previews/v13_normcorr_laser_20260902a_frame145_muzzle_closeup.png, SHA-256 D4E11A2E336876B981F4538C9D823E6A5FA2672E567C5A44167EBF172997ABFE. The normal-scale frame-50 support three-quarter preview is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/previews/reimport_v13_normcorr_support_20260902a_frame_050_three_quarter.png, SHA-256 67C63D799068814DA311AB89E4FE07ED54181879B37DA8EB8F45879FFC2ADA9B, and its muzzle close-up is docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/previews/v13_normcorr_support_20260902a_frame50_muzzle_closeup.png, SHA-256 9E7DC8B24420B3E92739895212BF295B33E65794D6EEDBCBE323414532D1BB77. The close-ups are derived crops of the existing adapter renders and did not modify model, material, or animation bytes; they visibly corroborate the integrated pistol, cyan-tipped front ring, and both hand contacts, but visual color is not used as semantic muzzle proof.

Both corrected reimports retain the accepted mesh identity char1.002, rig io_pdx_rig, material PDXmat_char1.002, 59,999 triangles, 59,451 vertices, 24 bones, and no locator. The accepted source mesh remains export/v13_firearm_preset/alien_infantry.mesh, SHA-256 D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342, with topology SHA-256 047DA36DD69934B61C72321F02C958E6D970C5D52C0EFB2BFC172DB8DA2417A0. The accepted source and all proof bytes remain untouched.

### Exact native mesh-region reads

The sampler used the same bounded geometric patch in both actions: source vertex indices [3089, 3090, 3091, 3121, 3122, 3139, 3143, 3144, 3164, 3166, 3185], which form a connected nine-triangle front-ring patch with polygon indices [3053, 3082, 3083, 3102, 3104, 3125, 3126, 3129, 3148]. This is a geometric candidate only. The earlier direct-V cyan texture identification is rejected after the importer/exporter V-flip audit and must not be used to name the muzzle.

| Request | Action/frame | Bone or selector | Result |
| --- | --- | --- | --- |
| af87e4678579423e9ca96872862eeb76 | laser_attack/145 | RightHand, tight world AABB min [-0.77,-0.04,5.05], max [-0.73,-0.01,5.11] | 37 matched vertices; every measured cap index included. |
| 39afd32ed5f54f75848696faea40d5ea | laser_attack/145 | RightForeArm, same tight world AABB | 37 matched vertices; every measured cap index included. |
| 26fb0196ceba49f48d08c17998e18048 | support_attack/50 | RightHand weight range [0,1], total mesh 59,451 | Complete measured ring records returned. |
| dc0a88a777ad46fb8be666166585d7ef | support_attack/50 | RightForeArm weight range [0,1], total mesh 59,451 | Complete measured ring records returned. |
| a2155256b79c4147871a0910fec4dce9 | support_attack/50 | RightHand, tight world AABB min [-0.20,-0.28,4.92], max [-0.10,-0.19,4.99] | 75 matched vertices; every measured cap index included. |
| 3c83b58b57d14dd38c8d795b3b308d08 | support_attack/50 | RightForeArm, same tight world AABB | 75 matched vertices; every measured cap index included. |

The laser cap world centroid at frame 145 is [-0.754595735,-0.025545922,5.076822758], with world AABB min [-0.765802979,-0.036115110,5.054632187] and max [-0.734954596,-0.018867612,5.102562428]. The support cap world centroid at frame 50 is [-0.147636869,-0.233511524,4.953468626]. The immutable source centroid is [-2.348053260,0.525383142,5.389686498], with source AABB min [-2.357996702,0.503818274,5.367467403] and max [-2.342484474,0.537334204,5.415216923].

The explicit measurement sets were origin indices [3089, 3090, 3091, 3121, 3122] and endpoint indices [3139, 3143, 3144, 3164, 3166, 3185]. The weighted laser RightForeArm-local origin center is [-0.105127320,0.835513234,0.037573252], endpoint center is [-0.093338579,0.834821343,0.065765858], and their 5:6 weighted ring center is [-0.098697097,0.835135839,0.052951037]. The corresponding support values are origin [-0.087126993,0.821147144,0.054838616], endpoint [-0.070478596,0.822072030,0.081591219], and weighted ring center [-0.078046049,0.821651627,0.069430945].

The same measured ring transformed from laser to support changes only about 2.639 degrees in RightForeArm-local surface-normal direction, versus about 28.271 degrees in RightHand-local surface-normal direction. RightForeArm local cap-centre change is approximately [+0.020651,-0.013484,+0.016480] in the stated local coordinate order after comparing the two weighted centers, while RightHand local cap-centre change is approximately [-0.050172,+0.049010,-0.030501]. The cap weights are predominantly RightForeArm, 0.6874929-0.7382823 with mean 0.7220920, versus RightHand 0.2617177-0.3125071 with mean 0.2779080. These measurements make RightForeArm the stronger empirical gun-bearing-parent candidate, but they do not constitute engine semantic certification.

### Explicit locator proposal before authoring

The smallest source-grounded proposal is a nondeforming locator parented to RightForeArm at a reviewed bone-local position near the averaged laser/support ring centre [-0.088371573,0.828393733,0.061190991]. The outward axis candidate is the normalized average of the measured local surface normals, approximately [-0.46027911,0.85969590,0.22150870]. A geometric roll/up candidate is obtained from the ring-plane PCA, using local +Z-oriented in-plane vectors laser [0.352424934,-0.022310757,0.935574100] and support [0.513191254,0.042112080,0.857240520], projected onto the plane orthogonal to the averaged outward axis.

For an explicit proposal only, the locator frame convention is local +X = outward muzzle axis, local +Z = the projected geometric-up candidate, and local +Y = local +Z cross local +X. Under that convention the averaged local basis is +X [-0.46027911,0.85969590,0.22150870], +Y [-0.77196307,-0.51079644,0.37836493], +Z [0.43842463,0.00315694,0.89876241], with proposal quaternion xyzw [0.19477866,0.11260580,0.84702980,0.48158251]. This is not an accepted author_locator input: the sampler returns no quaternion, the provider rig's weapon attachment semantics are not exposed by this read-only operation, and the PDX runtime particle local-axis convention still requires parent review. The proposal must therefore remain needs_user_review until the parent chooses the semantic forward axis and roll convention.

The measured world cap diameter vectors are not muzzle axes. In particular, the laser measurement vector is world origin [-0.761428058,-0.030212356,5.091297627] to endpoint [-0.748902201,-0.021657229,5.064760685], length 0.030566265, and the support vector is world origin [-0.163137779,-0.240674362,4.955486298] to endpoint [-0.134719461,-0.227542520,4.951787949], length 0.031523386. They describe the explicit ring-diameter sample and must not be wired as a discharge axis.

### Gates, release state, and recovery order

No author_locator operation, locator-bearing export, locator byte reimport, seven-action reimport, or runtime wiring was performed in this bounded sequence. The provider actions remain unchanged and semantically distinct; support_attack is the accepted provider action and defend remains the existing Combat_Stance action whose firing/nonfiring semantics must be described truthfully by the parent. No geometry regeneration, weapon remodel, action authoring, audio/counter change, provider call, or credit spend occurred.

The next minimal recovery order is: parent reviews the RightForeArm attachment evidence and the explicit axis/up convention; parent opens a fresh working copy derived from the corrected reimport rather than any proof file; parent authors one nondeforming muzzle locator with the reviewed transform; parent exports and verifies the locator survives actual .mesh byte reimport; parent reimports laser_attack and support_attack first and checks frame 145 and frame 50 follow-through plus hand contacts; parent then reimports the remaining five immutable accepted action bytes and checks all seven semantic roles; parent owns consumer wiring review; and the user alone owns live/in-game acceptance. The old failed or rejected checkpoints remain rejected and must not be relabelled or overwritten.

Current status is measured-but-unaccepted: the ring candidate, parent candidate, origin, axis, and roll proposal are concrete; semantic muzzle approval, locator export/reimport, all-seven proof, runtime effects/audio/counter consumers, and live acceptance remain open. The adapter source-freeze release is complete because no native call remains in flight.

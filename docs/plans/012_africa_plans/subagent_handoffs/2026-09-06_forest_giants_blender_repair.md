# Forest giant Blender repair handoff

Status: in progress; no new mesh or action is selected for runtime.
Accepted scope: `docs/plans/3d_model_workflow_plans/2026-09-06_existing_unit_blender_repairs.md` and the explicit parent assignment.
Existing non-firearm repair, manual GPT-6-astra rigging/actions, broad axe and bound-log reconstruction are authorized.
Meshy calls: zero; estimated and consumed repair credits: zero.
Legacy provider-only action prohibitions are superseded by this scope; historical source jobs remain preserved.

## Intake and ownership

Own only forest artifacts with `blender_repair_20260906` naming and this handoff.
The parent owns runtime copies, `.gfx`, `.asset`, entity, sound, gameplay, companion reconciliation, review, and commits.
Selected preserved checkpoint: `docs/assets/012_africa/models_3d/forest_giants/blender/checkpoints/00_selected_body_blender_repair_20260906.blend`, SHA-256 `0FEA15FBC95A19A5B324E39E6FBD657884FB9C48993F0BD9D7BC3B13677B4637`.
Source Meshy 7 task `01a04333-952c-7726-a8c9-8e9ae388049a` and GLB SHA-256 `60E01F77E07E0EFD6E2FF00F76A34184DEEE606AF2307C5C17C6122F5C4923B1` remain unchanged.
Source provenance, authorization, original/refined hashes, and prompt remain in `refs/source/provenance.json`, `refs/briefs/replacement_source_faithful_cleanup_prompt.md`, and the historical `manifest.md`.
The approved reference and baseline front view were visually inspected: bark body, white crown, green mantle are present; broad double-curved axe and bound timber bundle are missing from the body.

## Validation and current dependency gate

Offline core wiki pages, graphical assets/entity pages, repository guidance and 3D/event-assets/subagents skills were consulted.
Installed vanilla `gfx/entities/units_infantry.asset` gives `asian_gfx_infantry_entity` scale 0.8, distinct runtime state binding, hand-node equipment attachment, and movement sound events.
Retain custom source/effective height 18.792008 at scale 1.0; the historical infantry measurement includes collision geometry, while rendered infantry height is 7.390917778 and effective height 5.912734222 as the parent measured.
Bridge `127.0.0.1:9876` was separately reachable.
Shared adapter source hashes changed during the gorilla owner's extension; Blender authoring is paused until the owner stabilizes the route and the parent refreshes the dependency lock.
Prepared `evidence/blender_repair_20260906/review_components_blender_repair_20260906.py` calls only the repository adapter, fails closed on every locked source mismatch, and keeps large report data on disk.

## Companion verification

`evidence/blender_repair_20260906/intake_companion_hashes_blender_repair_20260906.json` records actual intake source and companion hashes.
All six signed-16-bit WAV candidate hashes match the retained audio manifest.
The claimed immutable originals `audio/source/forest_ambience.ogg` and `audio/source/quern_stones.ogg` are absent from the current job; original-source verification is blocked.
Historical licensing evidence remains `audio/evidence/source_research.md`: public-domain nille/PDSounds forest ambience and CC BY 4.0 Work With Sounds/Monika Widzicka quern stones.
No new audio was generated or transformed.
Selection remains blocked at the actual unit-specific consumer: vanilla `sound/soundeffects.asset` exposes global `select_army`; formation creation is not selection.
Action synchronization awaits authored and reviewed phase timings.

Current counter contact sheet visually shows the axe and bound-log redo with native-alpha sources, whereas `counters/manifest.json` and `counters/manifest.md` still describe the former chroma-key source.
Actual large DDS SHA-256 is `A369280FA608623B7C087E6A28929BD3A6BD325989BA58EED136AA71F978D7B9`; map DDS is `B2EBC30345353B2B81E886FAE81850FC08D79BE2DE1A3A4800904165A3DEF7D8`.
Current `counters/contact_sheet.png` SHA-256 is `4D0031E8CC8442425FBCC745D6AFCC6988153610EEED7EF2FA0EB43C5C776802`.
These disagree with the historical manifest hashes; parent companion reconciliation is required before claiming source provenance or runtime synchronization.
Installed `interface/subuniticons.gfx` references two-frame infantry large 152x42 and map 60x12 DDS precedents; the retained comparison family records dominant green RGB 73,106,73.

## Remaining required work

Measured rig/weights, complete axe/log assembly, PDX material binding, five distinct 30 FPS in-place roles, contact/deformation/multi-phase previews, complete mesh and animation exports, actual-byte reimports, and final checksums remain in progress.
Roles are idle, move, axe attack, concealment/emergence, and articulated death.
No source-to-runtime synchronization, runtime promotion, or in-game completion is claimed.
No required component or role has been substituted or omitted from the scope.

## Authored checkpoints and review findings

The locked compact landmark inspection completed through request `f0c88f94a0854fb19cf86cc75b524989`.
Its report is `evidence/blender_repair_20260906/landmarks_blender_repair_20260906.json`, SHA-256 `0B9AB40CAFFC235C4F13273FCD9751E4B0130B0CE7B290F4B9588D3457A6541E`.
The adapter health request `c3a6c0e057964f2181448998309f715a` verified Blender 5.1.2, loaded io_pdx_mesh, and mesh/animation import/export operators.
The live wrapper schema and six passing source checksum rows are retained in `evidence/blender_repair_20260906/`.
Standalone Technology Tree Viewer discovery is outside this model-only repair scope under the parent's explicit directive; availability is unverified and is not an absence blocker.

Measured rig request `fd699741eac74159bd01669dc5f1c24c` created `blender/checkpoints/01_measured_rig_blender_repair_20260906.blend`, SHA-256 `3FE6604997FEFB64963D4874AC3A8C99CF2FB57DB496A2623455F7F3F70A06B4`.
The 27-bone `forest_giant_rig` has measured spine/head/crown, paired clavicle/upperarm/forearm/hand/finger/thumb/leg/foot chains, and independent `axe_control` and `log_control` bones.
All 11,724 reduced body vertices are covered by 15 explicitly ordered anatomical weight regions.
The reduced body has exactly 23,500 triangles and unchanged bounds, with zero boundary, non-manifold, or degenerate findings.

Both required implements are modeled using bounded explicit geometry and existing atlas material `material`.
`forest_broad_axe` has 460 triangles and binds rigidly to `axe_control`; `forest_bound_log` has 684 triangles and binds rigidly to `log_control`.
The log includes three irregular closed timbers and two closed bindings; the axe includes a bark haft, two broad curved blades, and a socket binding.
The assembled checkpoint `blender/checkpoints/03_assembled_blender_repair_20260906.blend` has SHA-256 `316703357EE75202878EE54D09C97385483B53F0101CDA6876F506996995F5E1`.
It contains three working mesh objects, 12,308 vertices, 24,644 triangles, UVs, and no open, non-manifold, or degenerate geometry.
Editable component geometry, UV declarations, authoring requests, and receipts are retained in `evidence/blender_repair_20260906/`.

First idle action checkpoint `blender/checkpoints/04_idle_blender_repair_20260906.blend` is retained as rejected grip evidence.
Front/right previews `blender/previews/forest_idle_1_blender_repair_20260906_*.png` show a preserved tree body and readable axe/log, but visibly open dangling fingers.
The corrected curl was authored into sibling `blender/checkpoints/04_idle_v2_blender_repair_20260906.blend`; its visual review is pending because the shared MCP source changed again before the preview call and the checksum gate stopped execution.
Five separate semantic phase plans exist in `forest_actions_blender_repair_20260906.py`; only idle has reached Blender so far.
Remaining roles, material binding, grip/contact review, full multi-phase evidence, exports, and reimports remain required.
`companion_audit_blender_repair_20260906.json` independently confirms all six WAV candidates are mono 44,100 Hz signed-16-bit PCM and records actual durations and checksums.
It also records all four current native counter source PNG hashes.
The current map frame 0 has 82 of 82 opaque pixels with RGB channel spread above 5 and median RGB 73.5,71.5,39; it is colored rather than the assigned neutral-grayscale family.
No new counter production was performed; parent review retains this discrepancy along with the stale counter manifests and missing original audio files.

## Resume evidence, 2026-09-08

The earlier only-idle progress statement is superseded by the saved action receipts below.
All five required roles have Blender candidates; this is authoring evidence, not semantic or export acceptance.
The latest cumulative checkpoint is `blender/checkpoints/11_death_settled_blender_repair_20260906.blend`, SHA-256 `9BDD9A97876FDA59908BD18AD076CE1E29E92307EF1073DE2A0593792D51B220`.

| Candidate action | Frames at 30 FPS | Loop | Receipt request |
| --- | --- | --- | --- |
| `chaosx_forest_giant_idle` | 1-61 | True | `6329fb61d1fd44a99a9abfb4113c728e` |
| `chaosx_forest_giant_move_repaired` | 1-49 | True | `0ce009b4e76d4674a009aa1126c443cb` |
| `chaosx_forest_giant_attack` | 1-61 | False | `0a617f637a4346a3bb57df58967dd0c3` |
| `chaosx_forest_giant_concealment_emergence` | 1-76 | False | `5d5613e8835f47e18961357ce5032ce5` |
| `chaosx_forest_giant_death_settled` | 1-91 | False | `3be05fadff5948058946be6fb2426cee` |

Exact checkpoint and native-action hashes are in `evidence/blender_repair_20260906/resume_action_inventory_20260908.json`.
The prior death-repaired frame-91 preview shows excessive body clearance and is rejected as final contact evidence.
The subsequent death-settled checkpoint was rendered at frame 91 under adapter 1.10.27, request `7d583eac652f4e309d67c8542787856d`.
Both the right and three-quarter views reject final contact: the legs remain below the trunk and leave the trunk suspended.
`evidence/blender_repair_20260906/author_death_contact_resume_20260908.py` prepares a finite final-leg correction while preserving the rest of the action.
The actual cumulative assembly includes the additional 192-triangle grip-vines component: four meshes total 24,836 triangles, with zero open boundaries, non-manifold edges, or degenerate faces.
The source-hash-bound three-map material binding draft is `evidence/blender_repair_20260906/pdx_material_request_draft_resume_20260908.json`; its source checkpoint hash must be filled only after a successful corrected checkpoint.
The resume render stopped before Blender when shared adapter MCP/worker/config hashes changed during the adapter owner's maintenance; the verification gate was preserved.
No runtime copies, new provider calls, or credits were consumed.
Materials, final contact review, mesh/action exports, actual-byte reimports, source-to-runtime synchronization, and inherited companion blockers remain unresolved.

## Contact and material continuation

Checkpoint `12b_death_contact_v4_resume_20260908.blend`, SHA-256 `17257183F76A489DCD8B6D0E910BD1438888435A1DC035DF904011C28734FA97`, successfully corrected final leg orientation.
Its frame-91 region query found the lowest body vertices at the neck foliage, while the pelvis remained elevated; the visual result was rejected.
Checkpoint `14_death_contact_v5_resume_20260908.blend`, SHA-256 `B7C995F758499F22F9E3F034B38A15FFBCDAE661F396BDAEE061E0B30E920C97`, reduces the final root pitch to bring the pelvis toward the same supporting plane.
Request `25089db8806644ffa02647b8f8239a61` passed save/reopen proof under adapter 1.10.31; visual contact review remains pending.
The independent checkpoint-13 material binding passed under adapter 1.10.31, request `fcc03ec9473b41fdaa20e1b551876452`, SHA-256 `40643AAFEEAA954E19E32733FA2616AC9C4A93C1183253BFD49BE63AEF14DD9B`.
All repair-worker Blender calls have drained; zero heavy calls remain outstanding while the parent resource hold is active.
Because checkpoint 14 derives from 12b, a successful checkpoint 13 does not automatically give checkpoint 14 its PDX binding; the final action and material branches must be combined explicitly.
The 23,500-triangle body will require conservative export-batch partitioning before mesh export, retaining the 24,836-triangle complete assembly.
No additional Blender calls will start until the parent releases the resource hold.

Forest V5 frame-91 quarter/right previews completed, request `90ebe45815334c129998b6fa25b5a770`, under adapter 1.10.33.
The torso is visibly inclined and elevated, so V5 remains rejected pending focused pose/contact correction; this is not treated as a material or renderer excuse.
The bounded contact tranche is drained and the shared Blender slot has been released for other owners.

`16_death_v6_request_draft_resume_20260908.json` is the next finite candidate and has not been executed.
It starts from successful PDX material checkpoint 13 and the V4 action, retaining the near-horizontal root while adding 8–10 degrees of lumbar articulation in the final settle.
This lowers the pelvis relative to the thick neck mantle after contact correction; axe/log world orientations remain unchanged in the pure pose reconstruction.
`16_death_v6_pose_solve_draft_resume_20260908.json` records the proposed bone centers and prop orientation error below 1e-15.
The pose reconstruction was checked against actual V5 Blender heads with maximum error below 0.000004 units; this verifies the coordinate calculation, not final deformation or contact acceptance.
Actual Blender authoring, broad ground contacts and focused visual review are still pending the next shared slot.

# Event 014 Feast Guard adapter 1.10.3 revalidation pause

> Historical revalidation pause. Superseded by the accepted installed Feast Guard runtime receipt; retain this file for adapter provenance only.

## Status

The Feast Guard revalidation is incomplete and intentionally paused at the shared adapter-lock boundary. No runtime, gameplay, GFX, entity, asset, or sound-definition file was edited, and no completion commit was created.

## Accepted 1.10.3 evidence

- Environment verification against committed adapter 1.10.3 commit `1be22d5ae661f3a71bdc052c60e4840c9aa4bdec` returned `findings: []` before production resumed.
- The old final checkpoint reopened with the 24-bone rig, DDS material image nodes, both oversized cleavers, and all eight genuine Meshy actions, but failed the new persistence gate at `7.375270366668701` versus the calibrated `7.351824797689915` target.
- Clean GLB rebuild request `4df280e42a3e41abbc5cdca638fda5e4` failed the same gate at `7.375270366668701`.
- Same-task FBX rebuild request `ada5ab6ffb0d4eea8469567e14fbe9c4` reduced the drift but still failed at `7.351057052612305`.
- Dual-source request `872e2d7af41845748bab545fc5ad5ead` reused the already audited old io_pdx_mesh reimport geometry, the immutable accepted rig task `01a03360`, and topology preservation. It passed save/reopen at `7.351825714111328`, a delta of `0.0000009164214134216309`, within the adapter tolerance `0.00007351824797689916`.
- Material-preserving weight-only request `8a1d948cb5fc4ce08d5599ec98aeae61` retained geometry, UV `map1`, DDS image nodes, transforms, and the 24-bone skeleton. It pruned 321 vertices to four influences, removed 329 excess influences, and left zero unweighted vertices.
- Accepted persistent bind checkpoint: `blender/checkpoints/13_v1103_persistent_bind_weight_only.blend`, SHA-256 `AD5CADEC2C588A274395FBB950E5FA35BA9B693A9316BF41FE054B7BF15E22E3`.
- All eight original verified Meshy animation GLBs were imported onto the corrected bind under adapter 1.10.3. Request ids: idle `df4367b4b0cc46758db1ffffa746cde4`, move `82c72a781aec460c99dbf6f7b73354e8`, attack `0d890e1f874849138dbaf3a4a1d5871c`, defend `cc04ea1b0edf456aa3bc5f4f2b5e1686`, support attack `e43d691996004694a979f576b355401d`, retreat `231af85748be42c39ceedff6fab22998`, training `30068282d5464f36b8217d6e16f353b9`, and death `a015ef18fe5f4649a2a955844bcf0165`.
- Accepted all-actions resume checkpoint: `blender/checkpoints/14_v1103_actions_08_death.blend`, SHA-256 `77E6C52373657A35E895D44823D502A7454542D6C9866252F68055FC2AF05172`.
- Eight role-phase inspections under adapter 1.10.3 reopened at `7.351825714111328` and wrote front, left, and three-quarter previews with stems `cannibal_feast_guard_v1103_<role>_phase`. Visual review confirmed distinct attached cleavers and substantive action motion without sphere/blob explosion.

## Rejected mixed-version evidence

The shared dependency lock changed concurrently to an uncommitted adapter 1.10.4 line while the grounding loop was running. This worker did not author any `.tools/3d_pipeline/**` or `.codex/**` change.

- Provisional 1.10.4 grounding requests completed for idle `7cf8200612be4fc481193ae6fa3f9b10`, move `ac6f823a83764631a1f2cdabc9b01b37`, attack `56d382e817b44ef4b2bbd2f99e5f3a67`, and defend `0a718db23e2846f19967b83e606793fa`.
- Support-attack request `0002821411f84eae9cb07303ab255c38` was created but has no result or checkpoint after interruption.
- All `blender/checkpoints/15_v1103_grounded_*` files are provisional and rejected until an authoritative committed lock is selected. They must not seed export.

## Exact safe resume point

After the parent resolves and verifies the authoritative committed adapter lock, resume from `blender/checkpoints/14_v1103_actions_08_death.blend`, not from any `15_v1103_grounded_*` checkpoint. Re-run grounding for all eight roles under one verified adapter version, inspect fresh grounded phase previews, export the mesh and all eight animations through io_pdx_mesh, cleanly reimport each result, verify reimport bounds and action phases, update package manifests/checksums/runtime handoff, and create an exact owned-path commit only when the complete chain is coherent.

## Blockers

- Authoritative adapter version and dependency lock are unresolved because the workspace contains concurrent uncommitted 1.10.4 / `geometry_object_name` changes of unknown ownership.
- Fresh PDX mesh/animation exports and clean reimports have not been run for this revalidation tranche.
- No completion claim or commit is valid at this pause point.

## Committed 1.10.7 continuation and second pause

The parent later authorized committed adapter 1.10.7 at `a3e0a1497b6926b025070267eb9c75bd00b77c93`. A fresh one-shot wrapper health request `ec7ae8d3126e48e6beade9b82576f4a1` verified adapter 1.10.7, Blender 5.1.2, and loaded io_pdx_mesh operators. Reopen request `b61857113bec4c03bb7b31d1991c7390` preserved the `7.351825714111328` height, 24 bones, all eight required actions, zero over-four influences, and zero unweighted working vertices.

All eight grounding mutations completed entirely under committed adapter 1.10.7:

- idle `1f35a319f50047d4adf1b2558545c020`
- move `d05a5553bb274080be450c5841555e4e`
- attack `ef1174bc851944079ba0494cacf70718`
- defend `7bbba8f1345446538385389d9a35e44d`
- support attack `3f942953cffe44169a1933b690ef73cc`
- retreat `f703243acca04982af4de4327a75b932`
- training `6529d617bb2f4fdea5c4f4a0f11f190c`
- death `596ee739bbc546ac86539e4ff8744a71`

The accepted grounded chain ends at `blender/checkpoints/16_v1107_grounded_08_death.blend`, SHA-256 `BDC6E2F771C1B2808B6DC99DE709CDE7124B397D273FB8DA84ABC19226FDB371`.

During subsequent read-only action-phase rendering, another concurrent uncommitted adapter change appeared. Idle, move, attack, defend, and support-attack inspections remained 1.10.7, but retreat request `e107ee957d174a4db535097279b33773`, training `c5680ec6269c49ff922bb145a113b8b4`, and death `0249ccf8de434187b0d378bc8a0f3a44` reported uncommitted adapter 1.10.8. Those three inspections and their previews are rejected as mixed-version evidence. The parent directed another pause before export until a stable later adapter hash and explicit reload gate exist.

The current safe resume checkpoint is the accepted 1.10.7 grounded chain above. No PDX export or reimport was attempted after either mixed-version boundary.

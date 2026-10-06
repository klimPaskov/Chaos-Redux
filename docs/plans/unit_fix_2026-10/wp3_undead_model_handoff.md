# WP3 Undead Zombies Model Handoff

Status: partial production handoff. The parent accepted the native AO bake narrowly as real source evidence for the unchanged current geometry and UVs. This does not approve runtime or material-grade use. The semantic head masks remain rejected drafts, and no runtime installation or full undead model completion is claimed.

All repository-relative paths in this handoff resolve from `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.

## Scope and review state

This tranche covered hash-bound source UV extraction, a manually traced head-region draft, and one native geometry-derived ambient-occlusion bake for `ownerundead_zombies`.

The parent accepted the source-face to installed-triangle correspondence only: all 30,474 faces map one-to-one with identity UVs and no unmatched or ambiguous IDs at the recorded comparison precision. The acceptance is recorded in `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/history.jsonl`; the earlier correspondence JSON still carries its draft approval field, so the history record is the decision evidence.

The parent rejected the current head masks as production masks because exposed face, forehead, and neck coverage is patchy, rear and ear hair boundaries include pale tissue, the eye/socket mask misses bright eye surfaces, 278 faces remain ambiguous, and 51 atlas texels overlap across classes. Preserve these exact drafts and conflicts. Do not fill the gaps using bone weights or color thresholds.

The class intent remains useful: dark scalp hair; pale exposed face, ears, and neck; eye lenses separated from socket margins; and mouth/teeth only where their surface and UV regions are separable. The next mask pass needs manually traced subregion UV coverage tied to the actual ray/UV correspondence, including the bright lenses and continuous exposed neck above the collar. The ear/scalp shards remain deferred for geometry, component, and winding review and were not deleted or reclassified.

Clothing, lining, hands, and shoes were not masked in this head-only review tranche. Their source regions remain pending. The source mask request in `wp3_textures_20261006/masks/requests/material_region_mask_request.json` is unchanged.

## Source and correspondence

The exact source checkpoint is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/checkpoints/06_exported.blend`, SHA-256 `c7439c1af44891d480082fa85efee73f848f0a8a086bbc05e9e0676878f269bf`.

The current export mesh is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/export/v2/chaosx_undead_zombies.mesh`, SHA-256 `de3f5f66b6d724221200a883941ebcda649d880a07780f71d1820c7a2c301052`.

The protected provider GLB is SHA-256 `acd462a4a6d3adc16788c82a1169e790e6e33518d21c6ce190fb44cad7575101`; its base-color image is `a1cd159979ebfd5904f44a66df73d67f55aba21bfcc6fca1c3b4824d69d40717`, and its normal image is `51443810c3fc5bf3073bc64e00c4b7df6019149a44aa0e1b4a26bdcd96eba785`.

The source mesh has 40,875 vertices, 64,933 edges, 30,474 triangles, and 91,422 loops. Its `UVMap` loop hash is `ffc52fc345baf26d8aff6f89f2f3907bf7f7a0063b47e829715ace401c564401`.

The parent-reviewed correspondence report is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/source_to_runtime_triangle_uv_correspondence_20261006.json`, SHA-256 `7dbd42bdde00a0d2c90674bc09b80a35214eddfa7b04c8de36f6583efbf81158`. It records 30,474 one-to-one matches, zero unmatched or ambiguous source IDs, identity UV transforms, and the four PDX material-stream split explanation for differing raw vertex-record counts.

The source UV loop records are `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/source_face_uv_loops_20261006.bin`, SHA-256 `ea70191a226221521f97c820691184d6ee265bf29bdbd22fa1d4ae80472daa46`, with receipt `source_face_uv_loops_20261006.json`, SHA-256 `9034d4799678b461d75795050ddd12d3682c5b0f4eedef4e1cf5222468a2fd11`.

The source-to-runtime match was not re-exported or edited during this tranche. The installed mesh and source checkpoint hashes remain unchanged.

## Head-region draft evidence

The exact face-ID and per-class UV report is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_region_faces_draft_20261006.json`, SHA-256 `95326a7807e235eaa2ce9432b0e793875b302888aea3f01ae98ab0c0801f6178`.

The draft selects 860 exposed head/neck skin faces covering 3,367 atlas texels, 681 hair faces covering 2,768 texels, 37 eye/socket faces covering 169 texels, and 61 conditional mouth/teeth faces covering 237 texels. It excludes 278 cross-view ambiguous faces and records 51 cross-class UV-overlap texels: 28 hair/skin, 6 eye/skin, and 17 skin/mouth.

Manual region-trace overlaps excluded from face votes are 184 pixels in the front, 843 in the left profile, 843 in the mirrored right profile, and 3,400 in the rear. The large rear overlap and the visibly patchy projected mask are reasons to retain, not approve, this candidate.

The labelled review views are `head_front_regions_draft_512.png` SHA-256 `f5c058f3fc65e910af3e0969865b7dc21cb5e3e1de1cea88958c48df42829964`, `head_left_regions_draft_512.png` SHA-256 `944e23612955c6374a3d1f060a3e9449a39e77bc517f9a87c71fcddb6f3cafbe`, `head_right_regions_draft_512.png` SHA-256 `0032fa670363b34fb1a6ac6cf9548cf59b58dba76fae2bbed3be941869cb5394`, and `head_rear_regions_draft_512.png` SHA-256 `7e6e635715524f472387932b135d372fd080c4fd3647a80c3809d5cd185bbff1`.

The UV evidence view is `head_uv_regions_draft_512.png`, SHA-256 `8d0cda922a2367780ba990b4ffc974cd1f1ac5586b561d8dec4403d5d5862f36`. Per-class grayscale candidates are `head_mask_pale_gray_skin_headneck_512.png` SHA-256 `ba2034a8c2c762f6bbc532deccffa2d2533e93f7d2013bde866dd0e4c7c58f53`, `head_mask_black_hair_512.png` SHA-256 `76b1337500139e47d51486ec6cd94cd4546a4ff85dabbdf8ddf19c74defed073`, `head_mask_eyes_socket_margins_512.png` SHA-256 `953c74eef8b930b285e3df968f58996dee71f84ff4c6026b59be033c2d6ab4ce`, and `head_mask_teeth_mouth_512.png` SHA-256 `8aabab89f143ed290d8ae52080178cf046c7e79e701d5f416d481e5d40df4eac`.

The reproducible draft builder is `head_region_mask_builder_20261006.py`, SHA-256 `bef4a658557c8b4d06ef4ebe98aaaa89e72d03eb655029c531f1cc671c7b132e`. It resolves manually traced source-view polygons through hash-bound raycast face-ID maps and projects source triangle UVs; it uses no bone masks, color thresholds, or image segmentation.

The existing runtime occupancy image contains 175,845 white texels. A separate simple triangle-raster comparison from the UV loop records produced 176,547 covered texels, with 0.8163 white-mask Jaccard against that occupancy image. This comparison depends on raster edge conventions and does not change the parent-approved identity UV correspondence. AO summary statistics below use the hash-bound existing occupancy image as their explicitly recorded region of interest.

## Native ambient-occlusion bake

The source model did not have an AO map. The AO candidate was baked from the source geometry through its existing armature modifier in REST pose, using an isolated duplicate as the sole render-visible mesh. The bake used no floor, reference model, or other visible geometry.

The native operation was Blender Cycles `bpy.ops.object.bake(type="AO")` at 512×512, CPU, 128 samples, no denoising, seed 0, AO factor 1.0, `UVMap`, zero margin, `use_clear=true`, selected-to-active false, cage false, and maximum ray distance 0.0. The AO distance was 0.15361598420781314 world units, measured as the 90th percentile of source-mesh edge lengths transformed by the source object world matrix.

Each of the four temporary target material slots had an active image node pointing to the bake image. The bake returned `FINISHED`. The first wrapper then raised `ReferenceError: StructRNA of type Object has been removed` while reading the removed temporary target's data during cleanup, after the native image had already been saved. Recovery reopened the immutable source, preserved the exact AO samples without rebaking, saved the source-preserving rest-pose checkpoint, reopened it, and verified the mesh, UV, weights, rig, action inventory, packed image, and unbound status.

The raw Blender output is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/undead_zombies_ao_512.png`, SHA-256 `31c94862a7a72c70aee2a0c5f5fa8578094178c03fdbfd1d556e1194d5e0ad10`.

The Blender PNG retained sRGB/gamma display metadata even though the image data was marked `Non-Color`. The reviewable scalar candidate is `undead_zombies_ao_512_linear.png`, SHA-256 `7434a9f799f4af17bd578379a6a31cba453b65ad3aa0359495c59d99c6884932`; it is a 512×512 single-channel `L` PNG with the exact unchanged native red-channel sample bytes, no rescaling or gamma transform, and no sRGB, gamma, or ICC metadata. This linear image is the 512 review preview and is packed into the checkpoint without a material binding. The parent accepted this image only as source AO evidence for the current unchanged geometry and UVs.

Using the existing 175,845-texel occupancy mask, the linear scalar samples have min 0.0, p05 0.0, median 0.4235294, mean 0.4808402, p95 1.0, max 1.0, standard deviation 0.4375163, and 81 distinct 8-bit levels. The 86,299 texels outside that occupancy image have mean 0.0492112 and p95 0.5137255; interpret this with the occupancy/raster-edge comparison above.

The reopened evidence checkpoint is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/checkpoints/07_ao_baked_restpose_20261006.blend`, SHA-256 `a2ec19b34ca139350c114c4355775cf800d10d5207e075a4da0be9dc0f2b961a`. Its armature pose-position display is REST and its rest-pose world height is 7.351823329925537, matching the calibrated source geometry height within measurement precision. The original `06_exported.blend`, runtime mesh, rig bones, weights, UVs, source actions, and source material slots are unchanged.

The raw bake used zero margin, so black atlas gutters are expected. Apply occupancy-aware padding before any texture use while preserving the linear scalar values. The parent did not approve material binding or a material recipe. Any later geometry or UV change invalidates this AO bake and requires a rebake and correspondence check.

The complete AO receipt is `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/ao_bake_receipt_20261006.json`, SHA-256 `6df227a4dfaf65a49ac071c5ef214760c40f43214fab2b36667672b52391dd59`. The native bake recipe is `bake_native_ao_20261006.py`, SHA-256 `40d0620f1aeecc709a47c84b47334374458ec44c179bac652e1fd4f28ef0393b`.

## Toolchain, session, and costs

The verified dependency lock is `.tools/3d_pipeline/config/dependencies.lock.json`, SHA-256 `cb8d29299776135e33acb5fed4da5cf1f3188719704c0d9c81ad6e52a0a51856`; adapter configuration is `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, SHA-256 `788858e3dc9e7d43a1717c419815f23935dc031f7beeb1d50b13601e8aeb8543`.

The live Blender build was 5.2.2 LTS, build `d13f752e3b9c`; Blender Lab MCP/add-on was 1.0.3, commit `2cea8d566dde07fbac28a61d698909d69724e853`. The locked `io_pdx_mesh` 0.91.0 archive was verified at SHA-256 `508643626fefe78511903b1894b8b4d68c387edd6228ad70487699a866886702`; it was not used for an export. The locked `chaosx_blender_hoi4` adapter 1.11.0 was verified but not called.

Lab worker PID 12544 was launched hidden only after acquiring the `.tools/3d_pipeline/staging/blender_worker.lock` OS lock. Its command used the lock-selected Blender executable, factory startup, `bl_ext.user_default.mcp,bl_ext.user_default.io_pdx_mesh`, and the Blender Lab MCP bridge at `127.0.0.1:9877`. The factory-startup default scene was Camera, Cube, and Light. The worker peaked at 478.8 MiB RSS; free RAM at closure was 7,778 MiB. PID 12544 was stopped, port 9877 was closed, and the staging lock was reacquired/released successfully to verify it is free.

The live authoring tool schema was `mcp__blender_lab_dev__execute_blender_code({code:string})`. The verified bake operator accepts `uv_layer` as an operator argument; `BakeSettings` has no `uv_layer` property. Read-only action inventory uses available `ActionSlot.identifier`/`display_name` fields and does not bind, edit, or retime actions.

This Blender-only tranche used no Meshy/provider calls, downloads, game launch, or paid credits. No mesh/animation export or reimport was performed, and no runtime material or game files were changed.

## Remaining work and ownership

The parent review accepts the AO image as native source evidence for the current geometry and UVs only. Runtime texture material binding, occupancy-aware padding, runtime installation, commits, and overall completion claims remain parent-owned. The texture owner may read the AO evidence but must treat the head masks as rejected drafts pending a finer source-face/UV subregion pass.

No AO source is copied into runtime. No material recipe, metallic/specular tuning, texture grading, geometry, topology, normals, rig, weights, actions, sound definitions, `.asset`, `.gfx`, entity, gameplay, audio, counter, or game files were changed.

The work is incomplete as a full undead model package: apparel, lining, hands, footwear, accepted semantic masks, AO padding/material binding, runtime installation, exports, and live consumer review remain outside this closed tranche.


## Final owned artifact paths and hashes

The following paths are repository-relative and resolve from the root stated above.

| Artifact path | SHA-256 | State |
|---|---|---|
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/source_face_uv_loops_20261006.bin` | `ea70191a226221521f97c820691184d6ee265bf29bdbd22fa1d4ae80472daa46` | Exact source UV-loop evidence |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/source_face_uv_loops_20261006.json` | `9034d4799678b461d75795050ddd12d3682c5b0f4eedef4e1cf5222468a2fd11` | Validated extraction receipt |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_region_mask_builder_20261006.py` | `bef4a658557c8b4d06ef4ebe98aaaa89e72d03eb655029c531f1cc671c7b132e` | Review-only traced face-ID/UV builder |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_region_faces_draft_20261006.json` | `95326a7807e235eaa2ce9432b0e793875b302888aea3f01ae98ab0c0801f6178` | Rejected semantic-mask draft and exact conflicts |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_front_regions_draft_512.png` | `f5c058f3fc65e910af3e0969865b7dc21cb5e3e1de1cea88958c48df42829964` | Rejected visual draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_left_regions_draft_512.png` | `944e23612955c6374a3d1f060a3e9449a39e77bc517f9a87c71fcddb6f3cafbe` | Rejected visual draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_right_regions_draft_512.png` | `0032fa670363b34fb1a6ac6cf9548cf59b58dba76fae2bbed3be941869cb5394` | Rejected visual draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_rear_regions_draft_512.png` | `7e6e635715524f472387932b135d372fd080c4fd3647a80c3809d5cd185bbff1` | Rejected visual draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_uv_regions_draft_512.png` | `8d0cda922a2367780ba990b4ffc974cd1f1ac5586b561d8dec4403d5d5862f36` | Rejected atlas visual draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_mask_pale_gray_skin_headneck_512.png` | `ba2034a8c2c762f6bbc532deccffa2d2533e93f7d2013bde866dd0e4c7c58f53` | Rejected mask draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_mask_black_hair_512.png` | `76b1337500139e47d51486ec6cd94cd4546a4ff85dabbdf8ddf19c74defed073` | Rejected mask draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_mask_eyes_socket_margins_512.png` | `953c74eef8b930b285e3df968f58996dee71f84ff4c6026b59be033c2d6ab4ce` | Rejected mask draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/regions/head_mask_teeth_mouth_512.png` | `8aabab89f143ed290d8ae52080178cf046c7e79e701d5f416d481e5d40df4eac` | Conditional, rejected mask draft |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/bake_native_ao_20261006.py` | `40d0620f1aeecc709a47c84b47334374458ec44c179bac652e1fd4f28ef0393b` | One native AO attempt recipe; cleanup recovery documented |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/undead_zombies_ao_512.png` | `31c94862a7a72c70aee2a0c5f5fa8578094178c03fdbfd1d556e1194d5e0ad10` | Raw native Blender AO output |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/undead_zombies_ao_512_linear.png` | `7434a9f799f4af17bd578379a6a31cba453b65ad3aa0359495c59d99c6884932` | Parent-accepted linear scalar source evidence; padding/material use pending |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/checkpoints/07_ao_baked_restpose_20261006.blend` | `a2ec19b34ca139350c114c4355775cf800d10d5207e075a4da0be9dc0f2b961a` | Saved and reopened source-preserving AO checkpoint |
| `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/blender/evidence/ao_20261006/ao_bake_receipt_20261006.json` | `6df227a4dfaf65a49ac071c5ef214760c40f43214fab2b36667672b52391dd59` | Validated native AO, occupancy, invariants, and reopen receipt |

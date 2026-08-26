# V11 firearm recovery rejection evidence

Date: 2026-08-26

## Existing V10 rig action 234

Meshy action 234 `Walk_Forward_While_Shooting` was applied to V10 rig task `01a03a0c-d468-7725-a48e-3352eed26db8` as materially different support-fire recovery. Animation task `01a03d2c-6a68-7c9b-90af-5e79adc4f75c` succeeded and consumed 3 credits. The immediate FBX download is `provider/downloads/animation_firearm_recovery_v11_support_action234.fbx`, 10,835,340 bytes, SHA-256 `DDB3E6004A3D0DB38E59415C293AE0F7D0871F1A7F7F719D675C77FA032158C2`.

Locked-adapter preparation request `369d60ed95604c5cb20bdcc463cbe696` produced the protected review source `blender/source/alien_infantry_v11_support234_review_provider_source.blend`. Request `c7e22875c0674ee6816d1c5c64486a74` failed only because the request used `expected_mesh_height` instead of adapter key `mesh_height`; request `48eb14f3a1084d8d8e9d8c078ea3a113` failed only because topology preservation was combined with a nonzero reduction target. Neither tooling-input error is a model rejection.

Adapter renders at frames 1, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, and 99 establish the model rejection. The right trigger hand is empty, the left support hand is empty, and the firearm remains fixed diagonally across the back/shoulder. The clip has no weapon aim, discharge, recoil, or recovery. The 24-bone rig has no firearm or muzzle bone/node. Action SHA-256 is `A0B4C095846CDD5AA6650F2AE2B7BDE91ABEEB24B9E85022470E6DA32D5B4327`.

## New approved two-hand Meshy 7 lineage

The approved exact input is `refs/original/meshy_input_v11_two_hand_firearm.png`, SHA-256 `CFF2E684F0D7D50A01084CEA76F2BA22CC4CF11BEB5D48AD829AD733FA2976D1`.

Generation task `01a03d3b-927e-72fc-99fc-b260df1dc178` used exact `ai_model=meshy-7`, one local `file_path`, triangle topology, PBR textures, lighting removal, and no provider pose conversion. It consumed 30 credits. Immediate GLB `provider/downloads/generation_firearm_recovery_v11_model.glb` is 64,429,320 bytes, SHA-256 `4C9349EE589DC5DE5E3BF633946F23E31BADB8572A370BAA7F738895FFB64D3F`.

Adapter request `93e2312f9e694be685f9e47d71e9473b` verified the raw geometry from front, left, right, rear, three-quarter, top, and underside. Firearm contacts pass: the right trigger hand continuously grips the handle/trigger region, the left hand cups the lower weapon body/barrel assembly, the pistol has no stock, and its body and circular muzzle are continuous and unobstructed. The raw model is not riggable through Meshy because it has 1,577,348 triangles / 817,649 vertices, above the documented 300,000-face rig ceiling. It also has 57,512 loose boundary edges.

Three provider remesh recoveries were rejected before rigging:

- Task `01a03d40-48d2-735d-b087-a328ecfc2c7c`, 100,000-triangle request, consumed 5 credits. GLB `provider/downloads/remesh_firearm_recovery_v11_model.glb`, SHA-256 `206974D2EA23F625F60A0FFD19320AFE92880B2F7946BB3B60D899EF88076629`. Adapter request `5c03156aa9324edaba16e551d253dde8` found 101,683 triangles, 59,507 loose boundary edges, and visible breakup/perforation around the face, neck, shoulders, torso, cuffs, and boots.
- Task `01a03d44-1037-7422-b378-17a3ea098c2e`, 299,000-triangle request, consumed 5 credits. GLB `provider/downloads/remesh_firearm_recovery_v11_299k_model.glb`, SHA-256 `A530793D46F1FA63EA7DA0BB22D8B42E8D2AFBA310168FB7D8F4ECE255939606`. Adapter request `0bc21eb0d6394c22885be628b45a4d59` found 302,019 triangles, 111,943 loose boundary edges, and the same visible perforation; it also exceeded the provider rig ceiling.
- Task `01a03d48-6562-7571-95f1-5eb38dfa20b0`, materially different 250,000-quad request, consumed 5 credits. GLB `provider/downloads/remesh_firearm_recovery_v11_250k_quad_model.glb`, SHA-256 `9FD0E97B606B0EF202D3210BE8B1FAABCB9CDBD466B7ECDD8D4B38B586C09A9A`. Adapter request `7bd820f38ad84dabab1cdb47bc6436a9` found 497,610 triangles, 74,264 loose boundary edges, 9 degenerate faces, and a result above the rig ceiling.

No V11 remesh was rigged. No V11 firearm animation was purchased. The successful raw-contact generation cannot reach Meshy rig/animation without a conforming provider remesh, and local repair/decimation cannot be uploaded into the locked Meshy rig route.

## Professional-package and locator closure

The existing CC0 Quaternius Universal Animation Library Standard audit remains the strongest genuine character-motion source. `Pistol_Shoot` provides aim/discharge/recoil/recovery with frame 6 discharge and retained integrated-pistol contact, but no distinct support-fire action and no firearm/muzzle locator. Archive SHA-256 remains `18FF1A7215F4852B320203E8AAF02A1578B5C8EEF9027FBAEDFCEDC7B85A3AC2`.

The official Quaternius Universal Animation Library page states that its universal humanoid rig is retargetable, includes combat/gun motion, is available in FBX/GLB/Blend, and is CC0: `https://quaternius.com/packs/universalanimationlibrary.html`. Its animation-only rig does not provide a locator for this model's integrated pistol.

The official Quaternius Animated Guns Pack page states that it contains six animated firearm props in FBX/OBJ/Blend under CC0: `https://quaternius.com/packs/animatedguns.html`. It does not provide humanoid aim/fire/recoil/support-fire coverage and would require replacing or manually attaching a separate weapon, which is forbidden. It was not downloaded.

Pichuliru's Flat Guns West page advertises rigged gun props and attachment bones, but the same page conflicts between a CC0 prose statement and an itch.io asset-license field of CC BY 4.0: `https://pichuliru.itch.io/cc0-flat-guns-west`. It provides weapon props rather than retargetable humanoid firearm motion and would require replacing/attaching the integrated pistol. It was not downloaded or used.

No searched package provides both a retargetable humanoid aim/fire/recoil/recovery plus independent support-fire action and a stable locator already belonging to the accepted integrated alien pistol. A locator from a different weapon rig is not equivalent and cannot be inferred or manually transplanted.

## Final status

Blocked. Required `laser_attack`, distinct `support_attack`, stable muzzle locator, discharge synchronization, final `.mesh`/`.anim`, packed materials, and export/reimport proof remain unavailable. Live Meshy balance after all V11 calls was 153 credits. No fallback was staged and no runtime wiring changed.

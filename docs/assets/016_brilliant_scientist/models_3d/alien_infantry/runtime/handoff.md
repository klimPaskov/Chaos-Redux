# Alien infantry runtime handoff

Status: **blocked — pose-correct V8 Meshy R2 rig passed; the parent-approved KayKit CC0 one-handed aim/shoot/reload actions are exported and reimported on a 30k PDX-material candidate, but runtime acceptance still waits for muzzle/effect/audio synchronization, remaining semantic actions, and parent entity wiring**.

## Runtime selection state

The selected diagnostic/runtime candidate is the Meshy 7 V8 lineage `01a037ff-1e09-7757-aa2c-ee123fc7c2e2` with its R2 rig, adapter-prepared 30k mesh, and KayKit retargeted firearm actions. It is not final gameplay acceptance because the muzzle/effect/audio and remaining semantic-action gates are still open.

- Historical GLB SHA-256: `DD96097BFAB051A59D08E918B0EF741E4BA400FB0784225B073CA96614BFC050`.
- Historical FBX SHA-256: `69514019CED0D60EDAB6C6C70F96D79DED994E6E5CCB0D234CFD6D6CDEBBD6AA`.
- Provider binaries and Blender sources/checkpoints were deleted after compact rejection evidence was retained; none may be treated as an accepted runtime source.

Do not revive v1 through v7. Their rejection records and task hashes are diagnostic evidence only.

## Geometry and scale state

The v2 multi-angle gate passed the alien identity, integrated ray gun, continuous muzzle, two-hand low-ready contact, grounded boots, and absence of floating weapon mass. Its protected source is 1,629,142 triangles. The Blender QA candidate is 30,000 triangular faces / 14,986 vertices with no reported loose boundary edges, non-manifold edges, degenerate faces, or negative-scale objects.

Calibration uses installed `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`: source height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, up +Z. Entity scale is applied exactly once.

## Historical v2 continuation state (superseded by V7 gate below)

The locked read-only route recheck at `2026-08-24T14:15:09Z` reported 1,410 credits. The mandatory remaining route needs at least 31 credits before recovery margin:

- remesh accepted task to the Meshy rig ceiling: 5 credits;
- rig the retained weapon-bearing character: 5 credits;
- seven distinct required Meshy actions: 21 credits.

No paid call was made during this probe. The route is fundable. Resume by remeshing task `01a03404-752c-7d05-be14-b204c817f9dd`, inspecting weapon retention, rigging, validating neutral weights/contact, and producing distinct idle, move, laser attack, defend, support attack, retreat, and articulated death actions. Reject the lineage if any action fuses, stretches, swings, detaches, or destroys the gun or hand contact. Blender must not attach or repair the gun and must not author replacement motion.

## Runtime identifiers and ownership

Proposed identifiers remain `alien_infantry_mesh`, `alien_infantry_entity`, `alien_infantry_idle`, `alien_infantry_move`, `alien_infantry_laser_attack`, `alien_infantry_defend`, `alien_infantry_support_attack`, `alien_infantry_retreat`, and `alien_infantry_death`.

The candidate `.mesh`, three firearm `.anim` files, staged texture companions, and actual-byte reimport proof now exist. Seven final semantic actions, packed DDS/asset registration, muzzle/effect/audio synchronization, parent entity wiring, and in-game acceptance remain open. The parent owns `.asset`, entity, GFX, sound-definition, particle/light, gameplay wiring, runtime synchronization, live consumer testing, and in-game acceptance.

## Superseding V7 firearm gate

Do not resume the stale v2 instructions above. The automatic route advanced through V6 and V7. V7 generation `01a03499-135b-7a19-b5f3-eef4fc9d1515`, remesh `01a0349e-d89f-76b4-baca-da8a190aafe5`, and neutral rig `01a034a4-700b-7a32-b9a8-ed95969a139a` passed geometry and neutral review. The same V7 rig then failed action 690 `Walk_Forward_While_Shooting_inplace`, action 104 `Side_Shot`, and action 232 `Cowboy_Quick_Draw_Shooting` with catastrophic arm/torso/rifle stretching and loss of a stable muzzle and two-hand grip.

The alternate-action audit deliberately tested reduced-locomotion and quick-draw/fire/recovery motion, so action 690's locomotion is not the sole cause. V3–V7 now reproduce the same failure class across independent generations, rigs, and firearm clips. The provider capability blocker is documented at `provider/rejections/generation_recovery_v7_firearm_capability.md`.

No valid firing action exists, so `alien_infantry_laser_attack` and `alien_infantry_support_attack` cannot be bound; exact discharge frames/times, muzzle node, `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` synchronization remain intentionally unset. The other five semantic actions were not purchased after the mandatory firing gate failed. Under the current Meshy-only instruction, recovery must wait for a provider capability change or a newly viable Meshy lineage; Blender repair or replacement animation remains forbidden.

## Superseding pose-correct V8 runtime state

Do not revive V1-V7 or the rejected two-handed input. The current accepted-neutral diagnostic lineage is generation `01a037ff-1e09-7757-aa2c-ee123fc7c2e2`, remesh `01a03804-cf34-7873-a71f-a6b3360619e2`, and R2 rig `01a0380c-df10-7a2c-ab1e-c28d2248b616` via provider FBX SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`. It preserves the right-hand upright pistol and free left arm, but remains non-runtime diagnostic evidence because the firing gate failed.

Action 232 `Cowboy_Quick_Draw_Shooting` has no credible firing sequence; action 104 `Side_Shot` has no visible discharge/recoil/recovery; action 690 `Walk_Forward_While_Shooting_inplace` imposes a two-handed low-ready walk and still has no distinct discharge/recoil/recovery. Therefore both firing consumers remain unbound. There is no verified discharge frame/time or stable muzzle locator for `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, or `alien_infantry_laser_fire`.

The other five roles were not purchased after the mandatory Meshy firing gate failed. The accepted candidate exports the three firearm actions only; idle, move, defend, support-attack, retreat, and a genuine articulated death action still need source verification and retargeting. Parent wiring must remain unchanged. No Blender repair, weapon manipulation, semantic alias, or locally authored replacement motion is permitted.

## Parent-approved professional fallback

The user approved a free external package after the official Meshy firearm-action gate failed. The fallback is limited to retargeting and export through the adapter; it does not permit Blender-authored replacement motion or manual weapon attachment.

- KayKit Character Animations 1.1: [official asset page](https://kaylousberg.com/game-assets/character-animations) and [official itch.io page](https://kaylousberg.itch.io/kaykit-character-animations).
- Archive SHA-256 `65882F31F905AD2E953819648A59287CDEAB8F623908D5EF701971D3758BE20F`; bundled CC0 `License.txt` SHA-256 `373B159044D1A886ED15F57CA5A7673BA14E2623C460283452705F2056912ED9`.
- Source FBX `provider/downloads/kaykit_rig_medium_combat_ranged.fbx`, SHA-256 `B70E1D5EF64FAFAAD5C50CA2225C238F33EC9622876014F38478DEEB10EE2BA4`, source armature `Rig_Medium`, 23 bones, 30 FPS.
- `Rig_Medium|Ranged_1H_Shoot` retargeted successfully to `alien_infantry_laser_attack` on `Armature.001`, frames 1–33 at 30 FPS. The adapter reported 239 source curves, 154 target F-curves, motion peaks 8.6347 to 8.5157, zero scale curves, and no warnings. The required provenance is `evidence/professional_animation/kaykit_ranged_1h_shoot_provenance.json`.
- `Rig_Medium|Ranged_1H_Aiming.001` retargeted successfully to `alien_infantry_laser_aim`, frames 1–33 at 30 FPS, with motion peaks 8.1330 to 8.0139 and no warnings. Provenance is `evidence/professional_animation/kaykit_ranged_1h_aiming_provenance.json`.
- `Rig_Medium|Ranged_1H_Reload.002` retargeted successfully to `alien_infantry_laser_reload`, frames 1–36 at 30 FPS, with motion peaks 5.7048 to 5.5402 and no warnings. Provenance is `evidence/professional_animation/kaykit_ranged_1h_reload_provenance.json`.
- The sustained `Rig_Medium|Ranged_1H_Shooting` action failed the adapter static-motion guard and remains rejected. It cannot be aliased into the runtime.
- Checkpoints are `blender/checkpoints/alien_infantry_runtime_30k_shoot_retargeted.blend`, `blender/checkpoints/alien_infantry_runtime_30k_aiming_retargeted.blend`, `blender/checkpoints/alien_infantry_runtime_30k_reload_retargeted.blend`, and `blender/checkpoints/06_exported.blend`. Candidate exports are `export/mesh/alien_infantry_runtime_30k.mesh`, `export/anim/alien_infantry_runtime_30k_laser_attack.anim`, `export/anim/alien_infantry_runtime_30k_laser_aim.anim`, and `export/anim/alien_infantry_runtime_30k_laser_reload.anim`; `export/mesh/base_color.png`, `export/mesh/roughness.png`, and `export/mesh/normal.png` are staged beside the mesh for PDX reimport.

The secondary free MoCap Online Pistol Starter pack was audited because it advertises explicit standing single-shot FBX clips. Its archive SHA-256 is `9D5A6FF26A0E70FA36625B9FF3FAB2CBFFAD7D8A4200A0CE12A225D87BCC5559`, and its Standard License is documented at `https://mocaponline.com/pages/standard-license`. Its `W1_Stand_Fire_Single` action retargeted cleanly at the curve level (frames 1–31, 30 FPS, 730 source curves to 154 target curves), but the target preview loses the integrated pistol/hand contact against the posed Meshy rest state. The license also restricts standalone redistribution, so this pack remains rejected and unwired; the CC0 KayKit package remains the preferred documented fallback candidate.

This is a **candidate export, not a final runtime handoff**. The adapter material pass tagged the working Meshy mesh as `PdxMeshAdvanced`, bounded it to 29,916 triangles, exported it, staged its texture companions, and reimported the actual bytes with a 24-bone skeleton and no texture warnings. The reduction leaves 108 loose boundary edges as a documented residual risk. The firearm clip has not yet established a stable muzzle node or verified discharge frame, so `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` remain unbound. The other semantic actions still need source verification and retargeting. Parent-owned entity wiring must wait for those gates.

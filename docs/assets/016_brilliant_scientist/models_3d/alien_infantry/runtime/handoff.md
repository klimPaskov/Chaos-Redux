# Alien infantry runtime handoff

Status: **blocked — accepted-neutral V7 rig fails all audited Meshy firearm actions**.

## Runtime selection state

There is no selected runtime lineage. Meshy 7 task `01a03404-752c-7d05-be14-b204c817f9dd` passed historical neutral-geometry review but was not accepted as a model package because the mandatory firearm animation gate never passed.

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

No final `.mesh`, `.anim`, packed DDS set, discharge frame/time, muzzle node, particle/light binding, actual-byte reimport proof, or runtime copy exists. The parent owns `.asset`, entity, GFX, sound-definition, particle/light, gameplay wiring, runtime synchronization, live consumer testing, and in-game acceptance.

## Superseding V7 firearm gate

Do not resume the stale v2 instructions above. The automatic route advanced through V6 and V7. V7 generation `01a03499-135b-7a19-b5f3-eef4fc9d1515`, remesh `01a0349e-d89f-76b4-baca-da8a190aafe5`, and neutral rig `01a034a4-700b-7a32-b9a8-ed95969a139a` passed geometry and neutral review. The same V7 rig then failed action 690 `Walk_Forward_While_Shooting_inplace`, action 104 `Side_Shot`, and action 232 `Cowboy_Quick_Draw_Shooting` with catastrophic arm/torso/rifle stretching and loss of a stable muzzle and two-hand grip.

The alternate-action audit deliberately tested reduced-locomotion and quick-draw/fire/recovery motion, so action 690's locomotion is not the sole cause. V3–V7 now reproduce the same failure class across independent generations, rigs, and firearm clips. The provider capability blocker is documented at `provider/rejections/generation_recovery_v7_firearm_capability.md`.

No valid firing action exists, so `alien_infantry_laser_attack` and `alien_infantry_support_attack` cannot be bound; exact discharge frames/times, muzzle node, `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` synchronization remain intentionally unset. The other five semantic actions were not purchased after the mandatory firing gate failed. Parent action is limited to deciding whether to wait for a provider capability change or explicitly approve a professional authored firearm-animation source; Blender repair or replacement animation remains forbidden.

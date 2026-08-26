# Alien infantry professional animation fallback handoff

> Superseded by the Meshy V13 package and static runtime promotion recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`; retain this file for fallback provenance only.

## Scope

This handoff records the parent-approved free animation fallback for the Meshy-rigged alien infantry model. It does not claim a finished runtime entity and it does not authorize manual weapon attachment or manually authored replacement motion.

## Source and license

- Official source: [KayKit Character Animations](https://kaylousberg.com/game-assets/character-animations) and [KayKit itch.io distribution](https://kaylousberg.itch.io/kaykit-character-animations).
- Package: `KayKit_Character_Animations_1.1`, archive SHA-256 `65882F31F905AD2E953819648A59287CDEAB8F623908D5EF701971D3758BE20F`.
- License: bundled `License.txt` is CC0, SHA-256 `373B159044D1A886ED15F57CA5A7673BA14E2623C460283452705F2056912ED9`.
- Source FBX: `Animations/fbx/Rig_Medium/Rig_Medium_CombatRanged.fbx`, adapter copy `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/downloads/kaykit_rig_medium_combat_ranged.fbx`, SHA-256 `B70E1D5EF64FAFAAD5C50CA2225C238F33EC9622876014F38478DEEB10EE2BA4`.

## Meshy model state

Meshy 7 generation `01a037ff-1e09-7757-aa2c-ee123fc7c2e2`, remesh `01a03804-cf34-7873-a71f-a6b3360619e2`, and rig R2 `01a0380c-df10-7a2c-ab1e-c28d2248b616` produced the accepted-neutral source. The rig FBX SHA-256 is `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`. Neutral review found one skinned mesh, 24 bones, and zero zero-weight vertices. Official Meshy firearm actions 232, 104, and 690 failed the required aim/discharge/recoil/recovery gate and remain rejected.

## Retarget evidence

- Source armature: `Rig_Medium`, 23 bones.
- Source action: `Rig_Medium|Ranged_1H_Shoot`.
- Target armature: `Armature.001`.
- Target action: `alien_infantry_laser_attack`.
- Adapter result: frames 1–33 at 30 FPS; 239 source curves to 154 target F-curves; motion peak 8.6347 to 8.5157; zero scale curves; no warnings.
- Provenance: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/professional_animation/kaykit_ranged_1h_shoot_provenance.json`.
- Retarget checkpoint: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/kaykit_ranged_1h_shoot_retargeted.blend`.
- Coordinate-safe checkpoint: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/kaykit_ranged_1h_shoot_export_ready.blend`.
- Candidate text animation: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/anim/alien_infantry_kaykit_laser_attack.anim`.
- Preview evidence: `blender/previews/alien_infantry_kaykit_shoot_frame_1`, `_9`, `_17`, `_25`, and `_33` with front/right/three-quarter views.

The same source package also retargeted `Rig_Medium|Ranged_1H_Aiming.001` to `alien_infantry_laser_aim` (frames 1–33, motion peaks 8.1330 to 8.0139) and `Rig_Medium|Ranged_1H_Reload.002` to `alien_infantry_laser_reload` (frames 1–36, motion peaks 5.7048 to 5.5402). Both transferred through the same explicit bone chains with no warnings; their provenance files are `kaykit_ranged_1h_aiming_provenance.json` and `kaykit_ranged_1h_reload_provenance.json`.

The sustained source action `Rig_Medium|Ranged_1H_Shooting` failed the adapter static-motion guard and is recorded only as rejected evidence. It must not be used as a semantic alias.

## Runtime gates still open

1. Establish a stable muzzle locator and exact discharge frame from an accepted skeletal action.
2. Bind the existing laser muzzle particle/light and sourced firing audio at that verified frame; no effect or sound may be guessed from a still render.
3. Retarget and validate idle, move, defend, support-attack, retreat, and a genuine articulated death action from the package or another explicitly approved professional source.
4. Parent review of the supported 30k adapter candidate: `export/mesh/alien_infantry_runtime_30k.mesh` (29,916 triangles), the three `export/anim/alien_infantry_runtime_30k_*.anim` actions, and the staged `base_color.png`, `roughness.png`, and `normal.png` companions. Actual-byte reimport proof is `blender/checkpoints/reimport_alien_infantry_runtime_30k_textured.blend`; it recovered 24 bones and emitted no texture warnings. The reduction leaves 108 loose boundary edges as a residual geometry risk.
5. Establish a stable muzzle locator and exact discharge frame from the accepted skeletal action, then bind the existing laser particle/light and sourced firing audio at that verified frame.
6. Retarget and validate idle, move, defend, support-attack, retreat, and a genuine articulated death action from the package or another explicitly approved professional source.
7. Only after the remaining gates above pass may the parent bind `alien_infantry_entity`, the runtime action consumers, particles, audio, and final counters as accepted gameplay assets.

## Validation and ownership

The successful retarget and coordinate checkpoint were produced through the Blender HOI4 adapter. No manual Blender attachment or replacement animation was used. The 3D worker owns source/animation provenance, retargeting, export/reimport, and audio synchronization; the parent owns entity/GFX/gameplay wiring and final in-game acceptance. This handoff intentionally leaves runtime wiring unchanged while the gates remain open.

## Rejected secondary source

MoCap Online's free Pistol Starter pack was also tested because it explicitly includes `W1_Stand_Fire_Single`. The archive is `mocap_online_free_pistol_starter_27a.zip`, SHA-256 `9D5A6FF26A0E70FA36625B9FF3FAB2CBFFAD7D8A4200A0CE12A225D87BCC5559`, under the provider's Standard License. Its action transferred through the adapter with 730 source curves and 154 target curves, but the posed Meshy rest state loses the integrated pistol/hand contact in the rendered result. Its standalone-redistribution restrictions also make it unsuitable for an openly inspectable mod package without a separate rights decision. It remains evidence-only and unwired.

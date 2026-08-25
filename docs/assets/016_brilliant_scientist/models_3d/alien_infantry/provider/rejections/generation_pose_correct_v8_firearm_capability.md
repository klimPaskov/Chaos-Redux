# Pose-correct V8 Meshy firearm capability rejection

Status: **blocked at the mandatory firearm-action gate**. The pose-correct geometry and neutral FBX rig passed, but no audited official Meshy action supplied genuine aim, discharge, recoil, and recovery while preserving the one-handed right-pistol identity. No remaining semantic actions or exports were purchased.

## Accepted geometry lineage

- Sole Meshy input: `refs/original/meshy_input.png`, 1254x1254, SHA-256 `E024BF5B536FB289744268D16389D17F2E2A09F15B211882F437FCF500CFE8AA`.
- Meshy 7 generation `01a037ff-1e09-7757-aa2c-ee123fc7c2e2`, 30 credits. GLB SHA-256 `19DC95E967D5C4ED3E7DAC875740FDD277BBE78DCDD235E6DC93697E06FEB65E`; FBX SHA-256 `7DDCD369A94C9A30916AB60A55405D1FC321DCC16835E58A7377A80E7D58AF0D`.
- Multi-angle gate passed a complete olive alien, integrated upright laser pistol in the right trigger hand, readable muzzle, free left arm, grounded boots, and no extraneous parts.
- Triangle remesh `01a03804-cf34-7873-a71f-a6b3360619e2`, 5 credits. GLB SHA-256 `DC8413BC151CD7E86D7CA910BD5BFCCD9DB6AD952525DFEBAA246927A248D7E9`; FBX SHA-256 `0C9561AF4C84F07378A7BAAA7AE0916283120A5A3E6ABD104F3CACEF639CF301`. Adapter inspection reported 101,598 triangles / 86,201 vertices and retained the accepted pose and weapon silhouette.

## Rig recovery and neutral result

- Rig R1 `01a03809-f1e2-77e6-968c-49de78148e81`, 5 credits. The GLB exposed a giant visible `Icosphere.001` import artifact and was rejected. No object was manually removed or repaired.
- Recovery rig R2 `01a0380c-df10-7a2c-ab1e-c28d2248b616`, 5 credits. The FBX is the accepted-neutral diagnostic source, SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`. The corresponding GLB SHA-256 is `49F4F8C178D1B7DF1E1ED1E48850626EB17F961964FE8F6F4EA35F15702135F4` and reproduces the icosphere import artifact, so it is not selected.
- Adapter request `fcc9eb378c0240bea524f4a2bbb4556d` inspected the R2 FBX as one 100,924-triangle / 50,510-vertex skinned mesh with a 24-bone `Armature.001`, zero zero-weight vertices, no degenerate faces, and no negative-scale objects. Neutral multi-angle previews preserve the right-hand pistol, stable muzzle, left arm, anatomy, and boots.
- Calibration preserved target source height 7.3518242835, entity scale 0.8 exactly once, effective runtime height 5.8814594268, forward -Y, and up +Z.

## Official firearm action audit

| Action | Task / cost | Source range | Full-phase evidence | Verdict |
|---|---|---:|---|---|
| 232 `Cowboy_Quick_Draw_Shooting` | `01a0380f-e102-799d-b23c-a1ea9b2a614d`, 3 | 1-220 at 30 FPS | Frames 1, 35, 45, 55, 65, 75, 85, 100, 105, 115, 125, 135, 145, 155, 165, 190 | Pistol is lowered and manipulated, including left-hand contact, then returned upright. No credible aim, discharge, recoil, and recovery sequence. FBX SHA-256 `5AFEA59C090CD9D6D0C8C9BAC9C94A4FC3F65D184B3ADAE5FDB58C5193166292`. |
| 104 `Side_Shot` | `01a03814-bf31-79e3-9ba2-cf509381878c`, 3 | 1-121 at 30 FPS | Frames 1, 20, 40, 60, 80, 100, 121 | Kneeling lateral flourish with the pistol held near the head. No visible aim/discharge/recoil/recovery. FBX SHA-256 `8B312212A1E92B069881C6E446641266B8CF4DB9A81841C694301602C5071068`. |
| 690 `Walk_Forward_While_Shooting_inplace` | `01a03817-1453-7e17-9d5a-92618c4d9450`, 3 | 1-99 at 30 FPS | Frames 1, 15, 30, 45, 60, 75, 90, 99 | Continuous two-handed low-ready walk. It violates the one-handed identity and never shows a distinct discharge, recoil, or recovery. FBX SHA-256 `D0DEFBE0B68422BC2FECE8BEA4986CA92D8B9F657E6DBBB816BAEAD0D2F4E065`. |

The three actions are materially distinct and exhaust the official firearm candidates already verified for this package: quick-draw manipulation, stationary side-shot motion, and locomoting shooting motion. Regenerating geometry cannot add missing discharge/recoil phases to these provider action sources, and the R2 rig already passed neutral integrity. This is therefore a provider-action capability blocker, not a balance blocker.

## Spend and hard stop

V8 consumed 54 credits: generation 30, remesh 5, two rigs 10, and three firearm actions 9. Live balance was 291 before generation and 237 after the final action. The account was sufficient; no insufficient-balance condition occurred.

Per the mandatory firing gate, idle, move, defend, support attack, retreat, and death were not purchased. No exact discharge frame/time, stable muzzle locator/node, particle/light/audio synchronization point, packed runtime textures, `.mesh`, `.anim`, export, or actual-byte reimport can be accepted. No Blender weapon attachment, separation, parenting, constraints, weapon bone, weight repair, replacement animation, static alias, transform-only action, or whole-rig manipulation was used.

Parent cleanup resolved every target inside this job root and deleted the redundant generation/remesh FBX copies, rejected R1 rig binaries, rejected R2 GLB, all three rejected action GLB/FBX pairs, their disposable Blender source files, and shared adapter checkpoints. It reclaimed 657,362,751 bytes. The accepted-neutral recovery set remains protected: generation GLB, remesh GLB, R2 FBX, remesh and R2-FBX Blender sources, compact task/hash records, reports, and representative phase previews. No accepted runtime candidate existed or was deleted.

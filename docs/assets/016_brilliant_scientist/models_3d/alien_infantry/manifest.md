# Alien infantry 3D package manifest

Status: **blocked — the current Meshy V10 lineage has a firearm-bearing 24-bone rig and five accepted genuine source roles, but no compliant firearm action, support attack, or muzzle locator; no runtime entity is wired**. Earlier V8/Quaternius exports and reimports remain historical evidence only.

## Authoritative source and input

- Sole immutable user source: `refs/source/user_supplied_alien_reference.png`, SHA-256 `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`.
- Sole current exact-one Meshy input: `refs/original/meshy_input.png`, 1254x1254, SHA-256 `E024BF5B536FB289744268D16389D17F2E2A09F15B211882F437FCF500CFE8AA`.
- Rejected historical two-handed input: `refs/derived/rejected_two_handed_meshy_input.png`, 1024x1536, SHA-256 `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`; never submitted during V8.
- Authorization: the user supplied the source and explicitly requested the faithful ImageGen preparation used as the Meshy input.
- Meshy received exactly that one image. No multi-view, auxiliary image, A-pose, or T-pose input was used.

## Provider lineage and spend

The rejected first lineage is represented only by `provider/rejections/generation_user_supplied_v1.md`. It consumed 46 credits: generation 30, remesh 5, rig 5, action 98 3, and action 690 3. The neutral rig retained the ray gun, but two independent firing actions catastrophically stretched the arms/body and destroyed the gun silhouette, so the complete lineage was rejected and its large artifacts were deleted.

The historical v2 geometry lineage was accepted only for neutral geometry review and was later rejected with the rest of the package because no valid firearm animation could be produced:

- Meshy 7 image-to-3D task `01a03404-752c-7d05-be14-b204c817f9dd`, succeeded, 30 credits.
- Historical GLB SHA-256 `DD96097BFAB051A59D08E918B0EF741E4BA400FB0784225B073CA96614BFC050` and FBX SHA-256 `69514019CED0D60EDAB6C6C70F96D79DED994E6E5CCB0D234CFD6D6CDEBBD6AA`.
- Historical PBR map hashes: base color `13C75C37A732A2FDCC3E8C970F6C60917636754CB9F5D275198A4E096DA229ED`; metallic `5096AF6F13E54FA3DD4D68C6608823F93C99F83296C6BAC97C44DB7ABC7AC920`; normal `3F5101F06915E5A58B0C718BB6A970EDEFC353C36FCD04305FFF3FD38037FF85`; roughness `28F5F5A2519787CDB390E60F2113698FB46C96B142BB8AFB088C1CC158C1098D`.
- Spend through the initial and historical v2 lineages was 76 credits. This is not the package-wide total because later V3 through V7 recovery calls are recorded separately in `history.jsonl` and the compact rejection records; the shared account was also used concurrently, so balance deltas are not treated as an authoritative package total.

## Accepted v2 geometry gate

Adapter request `d422c421fcfa4b8386555049ef515feb` prepared and rendered the v2 source. The front, left, rear, right, three-quarter, top, and underside previews are under `blender/previews/alien_infantry_user_v2_*.png`. The alien identity, supplied retro ray gun, continuous muzzle, two-hand low-ready contact, grounded boots, and absence of an overhead/floating weapon mass passed visual review.

The protected provider source contains 1,629,142 triangles. The working QA candidate is exactly 30,000 triangles / 14,986 vertices, triangular, with zero loose boundary edges, zero non-manifold edges, zero degenerate faces, and no negative-scale objects. It uses `PdxMeshAdvanced` bindings to the immutable provider maps. This is geometry evidence only, not a final weighted/exportable model.

Vanilla calibration used `blender/reference/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`: mesh height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, up +Z. The v2 QA mesh measured 7.3527107239 high after reduction, for effective runtime height 5.8821685791 and delta +0.0007091523.

## Historical v2 continuation state (superseded by V7 closure below)

The locked live route was rechecked read-only at `2026-08-24T14:15:09Z`. The account balance is 1,410 credits. The minimum remaining mandatory provider route costs 31 credits: remesh 5, rig 5, and seven distinct Meshy actions at 3 each. The route is fundable with retry margin. No paid call was made during this recheck, so no v2 remesh, rig, animation, weight approval, action sampling, firing discharge/node synchronization, death-collapse proof, packed DDS output, `.mesh`, `.anim`, export, or actual-byte reimport proof exists yet.

Reserved runtime identifiers remain `alien_infantry_entity`, `alien_infantry_mesh`, `alien_infantry_idle`, `alien_infantry_move`, `alien_infantry_laser_attack`, `alien_infantry_defend`, `alien_infantry_support_attack`, `alien_infantry_retreat`, and `alien_infantry_death`. Parent owns final entity, particle, light, audio, and gameplay wiring. No in-game completion is claimed.

## Dependencies and companion packages

- Dependency lock SHA-256 `01CAE764172374943B0718048B136C029E3CEBDBFCFA737C24AFC75DF7EA08EF`; Meshy schema lock SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config SHA-256 `24F865F90077104493EA092C015E140B8519780B400B4AD2CFF748EA7AF91875`.
- Official Meshy MCP 0.4.0 with repository compatibility `meshy-7-v4` and explicit live `meshy-7`; Blender 5.1.2; adapter 1.10.3; io_pdx_mesh 0.91.0 with locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- The CC0 source/provenance package remains under `evidence/audio/`, and the derived PCM WAV files plus sound definitions are installed under `sound/shared_alien_system/alien_infantry/`, `sound/alien_infantry_sound.asset`, and the four package registrations in `sound/chaosx_sound.asset`. Exact entity-event synchronization remains blocked because the accepted idle, movement, and laser-attack actions still need parent entity wiring, the firing action lacks a supported muzzle locator, and defend, support-attack, retreat, and death remain unresolved.
- Reusable muzzle particle and light definitions are installed as `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash`; they remain intentionally unbound because no stable muzzle node exists. Frame 6 / 0.1667 seconds is an evidence-only discharge phase for the accepted Quaternius laser-attack export.
- Existing counters remain outside this job at `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, registered by `interface/alien_infantry_system.gfx`. They were inspected/reconciled but not recreated or overwritten.

## Authoritative recovery closure: V6–V7

The earlier v2 continuation text above is superseded by the completed automatic recovery audit. V6 and V7 were generated from the same immutable exact-one input. V6 passed generation/remesh/neutral-rig review but failed action 690 with catastrophic upper-body and integrated-rifle deformation. V7 likewise passed geometry/remesh/neutral-rig review, then failed action 690 and two materially distinct official-library alternatives: action 104 `Side_Shot` and action 232 `Cowboy_Quick_Draw_Shooting`.

The authoritative V7 lineage is generation `01a03499-135b-7a19-b5f3-eef4fc9d1515`, remesh `01a0349e-d89f-76b4-baca-da8a190aafe5`, and rig `01a034a4-700b-7a32-b9a8-ed95969a139a`. The firearm tasks are action 690 `01a034a6-9666-79b9-8929-cc3598191272`, action 104 `01a034ab-1c04-7c5a-ab0d-00687510cedf`, and action 232 `01a034b5-7230-7789-831b-e2ad3faae058`. Exact hashes, credits, and phase frames are recorded in `provider/rejections/generation_recovery_v7_firearm_capability.md`.

No remaining semantic actions, packed runtime textures, `.mesh`, or `.anim` files were produced after the firing gate failed. No discharge frame/time or muzzle node can be accepted from a deformed clip. The package is blocked on current Meshy firearm-animation capability, not on balance; the final observed shared balance was 433 credits.

After compact task, hash, rejection, report, and representative frame evidence was retained, failed provider downloads, transient provider request/response/credit receipts, and Blender source/checkpoint files were removed from this event workspace. The cleanup reclaimed 2,537,107,276 bytes and left the compact package at approximately 42.2 MiB. No deleted artifact was an accepted runtime candidate.

## Superseding pose-correct V8 closure

The user explicitly superseded the historical two-handed direction. V8 used only the 1254x1254 input hash above and preserved the original one-handed identity: upright retro pistol in the right trigger hand, free left arm, readable muzzle, complete anatomy, and grounded boots.

- Meshy 7 generation `01a037ff-1e09-7757-aa2c-ee123fc7c2e2`, 30 credits; GLB `19DC95E967D5C4ED3E7DAC875740FDD277BBE78DCDD235E6DC93697E06FEB65E`; FBX `7DDCD369A94C9A30916AB60A55405D1FC321DCC16835E58A7377A80E7D58AF0D`.
- Remesh `01a03804-cf34-7873-a71f-a6b3360619e2`, 5 credits; GLB `DC8413BC151CD7E86D7CA910BD5BFCCD9DB6AD952525DFEBAA246927A248D7E9`; FBX `0C9561AF4C84F07378A7BAAA7AE0916283120A5A3E6ABD104F3CACEF639CF301`. Multi-angle retention passed at 101,598 triangles.
- Rig R1 `01a03809-f1e2-77e6-968c-49de78148e81`, 5 credits, exposed a giant GLB icosphere import artifact and was rejected without local repair.
- Rig R2 `01a0380c-df10-7a2c-ab1e-c28d2248b616`, 5 credits. Its FBX SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124` passed neutral review as one skinned mesh, 24 bones, and zero zero-weight vertices. The corresponding GLB is diagnostic only because it reproduces the icosphere artifact.

The mandatory firing audit rejected action 232 `Cowboy_Quick_Draw_Shooting` task `01a0380f-e102-799d-b23c-a1ea9b2a614d`, action 104 `Side_Shot` task `01a03814-bf31-79e3-9ba2-cf509381878c`, and action 690 `Walk_Forward_While_Shooting_inplace` task `01a03817-1453-7e17-9d5a-92618c4d9450`. Actions 232 and 104 contain no credible aim/discharge/recoil/recovery sequence; action 690 is a continuous two-handed low-ready walk without a distinct discharge/recoil/recovery and violates the selected one-handed identity. Exact ranges, hashes, and representative phase frames are recorded in `provider/rejections/generation_pose_correct_v8_firearm_capability.md`.

At the provider-only V8 checkpoint, 54 credits had been consumed and the live balance was 237. The official Meshy firearm-action blocker was recorded before the parent-approved professional fallback below; no provider-generated semantic actions, discharge timestamp, muzzle node, export, or actual-byte reimport was accepted at that checkpoint. The later KayKit retarget is explicitly documented below and is not a local replacement motion.

Parent cleanup retained the accepted-neutral recovery set and compact audit evidence while deleting redundant or rejected V8 binaries, disposable action/source blends, and shared adapter checkpoints. It reclaimed 657,362,751 bytes and left the job workspace at 264,424,877 bytes. Retained recovery binaries are `provider/downloads/generation_pose_correct_v8.glb`, `provider/downloads/remesh_pose_correct_v8.glb`, and `provider/downloads/rig_pose_correct_v8_r2.fbx`; none is a runtime candidate.

## 2026-08-26 local evidence compaction

The Event 016 evidence workspace was compacted locally while the runtime package remains blocked. The deletion set contained only ignored, superseded, rejected, or exact-duplicate binaries: the obsolete D'Rhondan focus-source package (its 40 source hashes are byte-identical to the accepted completion package), the temporary hidden-technology alpha directory, obsolete Blender checkpoints and `.blend1` backups, rejected Meshy/professional provider copies, and extracted binaries from rejected animation packages. No runtime file, tracked file, accepted Meshy recovery binary, accepted export, actual-byte reimport proof, manifest, hash, license, or provenance record was removed.

The accepted Quaternius Standard archive, audit, and license remain available for future adapter work. Rejected MoCap Online, ZenXChaos, KayKit, and Quaternius 2 Standard binary payloads were removed after their hashes, rights findings, and rejection evidence were retained in this manifest, the compact audit files, and the provenance JSON records. Historical provider paths below describe formerly staged artifacts and are not runtime dependencies.

## Parent-approved professional animation fallback candidate (superseded by Quaternius promotion)

The user approved a free external animation package after the official Meshy firearm-action gate failed across independent V6 through V8 lineages. This fallback does not replace the Meshy-created model or authorize manual weapon attachment or replacement motion.

- Source: [KayKit Character Animations](https://kaylousberg.com/game-assets/character-animations) and its [official itch.io distribution page](https://kaylousberg.itch.io/kaykit-character-animations).
- Package: `KayKit_Character_Animations_1.1`, archive SHA-256 `65882F31F905AD2E953819648A59287CDEAB8F623908D5EF701971D3758BE20F`.
- License: the archive `License.txt` is Creative Commons Zero (CC0); its SHA-256 is `373B159044D1A886ED15F57CA5A7673BA14E2623C460283452705F2056912ED9`. The package permits commercial use and makes attribution optional.
- Source animation binary: `Animations/fbx/Rig_Medium/Rig_Medium_CombatRanged.fbx`, formerly staged for the adapter as `provider/downloads/kaykit_rig_medium_combat_ranged.fbx`, SHA-256 `B70E1D5EF64FAFAAD5C50CA2225C238F33EC9622876014F38478DEEB10EE2BA4`. The local provider copy was pruned after the Quaternius source superseded KayKit.
- Source rig: `Rig_Medium`, 23 bones, 30 FPS. The package includes one- and two-handed aiming, shooting, sustained shooting, and reload actions alongside other combat actions.
- `Rig_Medium|Ranged_1H_Shoot` retargeted through the Blender HOI4 adapter to `alien_infantry_laser_attack` on `Armature.001`, frames 1–33 at 30 FPS, with 239 source curves reduced to 154 target F-curves, source motion peak 8.6347, target motion peak 8.5157, no scale curves, and no adapter warnings. Provenance is recorded in `evidence/professional_animation/kaykit_ranged_1h_shoot_provenance.json`.
- `Rig_Medium|Ranged_1H_Aiming.001` retargeted to `alien_infantry_laser_aim`, frames 1–33 at 30 FPS, with 239 source curves reduced to 154 target F-curves, source motion peak 8.1330, target motion peak 8.0139, no scale curves, and no adapter warnings. Provenance is recorded in `evidence/professional_animation/kaykit_ranged_1h_aiming_provenance.json`.
- `Rig_Medium|Ranged_1H_Reload.002` retargeted to `alien_infantry_laser_reload`, frames 1–36 at 30 FPS, with 239 source curves reduced to 154 target F-curves, source motion peak 5.7048, target motion peak 5.5402, no scale curves, and no adapter warnings. Provenance is recorded in `evidence/professional_animation/kaykit_ranged_1h_reload_provenance.json`.
- `Rig_Medium|Ranged_1H_Shooting` was rejected by the adapter static-motion guard and is not a runtime action. Its failed provenance is retained only as evidence in `evidence/professional_animation/kaykit_ranged_1h_shooting_provenance.json`.
- The superseding 30k candidate checkpoints retained for resume are `blender/checkpoints/alien_infantry_runtime_30k_shoot_retargeted.blend`, `blender/checkpoints/alien_infantry_runtime_30k_aiming_retargeted.blend`, `blender/checkpoints/alien_infantry_runtime_30k_reload_retargeted.blend`, and `blender/checkpoints/06_exported.blend`. The older KayKit retarget checkpoints were compacted after their metrics and rejection state were recorded in the provenance JSON. Candidate exports are `export/anim/alien_infantry_runtime_30k_laser_attack.anim`, `export/anim/alien_infantry_runtime_30k_laser_aim.anim`, `export/anim/alien_infantry_runtime_30k_laser_reload.anim`, and `export/mesh/alien_infantry_runtime_30k.mesh`; the runtime texture companions are `export/mesh/base_color.png`, `export/mesh/roughness.png`, and `export/mesh/normal.png`.
- Visual evidence is the `alien_infantry_kaykit_shoot_frame_1`, `_9`, `_17`, `_25`, and `_33` preview set under `blender/previews/`. The clip shows a one-handed aim/fire/recovery silhouette without a Blender-authored replacement action.
- A mirrored-left/right KayKit mapping probe (`Rig_Medium|Ranged_1H_Shoot.002`) also transferred without adapter warnings but lost the pistol/hand contact in the frame-17 preview. Its evidence-only provenance remains in `evidence/professional_animation/kaykit_ranged_1h_shoot_mirrored_provenance.json`; the disposable probe blend and preview frames were compacted and it is not a semantic alias.

### Secondary free pistol-pack audit (rejected)

- MoCap Online's [Free Pistol Animation Pack](https://mocaponline.itch.io/free-pistol-animation-starter-pack) explicitly lists standing and crouching single-round fire actions and FBX output. Its [Standard License](https://mocaponline.com/pages/standard-license) permits integration into a game but restricts standalone redistribution/extraction and requires separate written permission for AI applications, so it is not a safe final source for an openly inspectable HOI4 mod without a rights decision.
- The formerly downloaded archive was `mocap_online_free_pistol_starter_27a.zip`, SHA-256 `9D5A6FF26A0E70FA36625B9FF3FAB2CBFFAD7D8A4200A0CE12A225D87BCC5559`. Its `W1_Stand_Fire_Single.fbx` SHA-256 is `DEA52960642BE5BF2C6C3A8C933B464F5FBD13B77274F29D399182F1BD45DEB4`; the license-restricted archive and extracted binaries were removed during local evidence compaction after the rejection was recorded.
- `Armature.002|W1_Stand_Fire_Single|W1_Stand_Fire_Single:BaseAnimation` retargeted through the adapter to `alien_infantry_mocap_w1_fire_candidate`, frames 1–31 at 30 FPS, 730 source curves to 154 target F-curves, source motion peak 0.9846, target peak 0.8038, and no transfer warnings. The preview still loses the integrated pistol/hand contact against the posed Meshy rest state, so this action is rejected and is not wired.

The KayKit candidate remains **retargeted/exported but superseded for the primary firing role**. The adapter material pass tagged `Material_1` as `PdxMeshAdvanced`, reduced the provider mesh from 100,924 to 29,916 triangles, exported the `.mesh`, and reimported the actual bytes with a 24-bone skeleton and no reimport warnings after texture companions were staged beside the mesh. The reduction leaves 108 loose boundary edges as a documented residual geometry risk. A stable muzzle locator and exact discharge timestamp were not proven, so the laser particle/light and sourced firing audio remained intentionally unbound. No manual attachment, transform-only animation, or unlicensed source was used.

## Superseding 30k export and reimport evidence

- Supported adapter preparation used the Meshy R2 FBX, the measured vanilla reference `blender/reference/western_european_infantry.mesh`, `PdxMeshAdvanced` material tagging, and the provider base-color/roughness/normal maps. The bounded reduction produced 29,916 triangles and 14,982 source vertices with no non-manifold edges or degenerate faces; 108 loose boundary edges remain and require parent review before final promotion.
- `export/mesh/alien_infantry_runtime_30k.mesh` is 2,957,433 bytes and uses one stream under the 65,535 vertex limit. `export/anim/alien_infantry_runtime_30k_laser_attack.anim`, `..._laser_aim.anim`, and `..._laser_reload.anim` are 30 FPS exports with frames 1–33, 1–33, and 1–36 respectively.
- `blender/checkpoints/reimport_alien_infantry_runtime_30k_textured.blend` is the actual-byte reimport proof. The adapter recovered a 24-bone `io_pdx_rig`, the mesh, and `io_pdx_rigAction`; texture companions were found with no warnings. Preview frames 1, 9, 17, 25, and 33 are under `blender/previews/reimport_alien_infantry_runtime_30k_textured_*`.
- This evidence clears material, export, and reimport gates only. It does not establish the exact discharge frame, muzzle locator, particle/light/audio timing, all seven required semantic actions, final `.asset` entity wiring, counters, or in-game acceptance.

## V9 Meshy recovery and Quaternius CC0 candidate audit (historical pre-promotion record)

The locked environment reverified on 2026-08-25 with zero findings: official `@meshy-ai/meshy-mcp-server` 0.4.0, Meshy schema compatibility revision `meshy-7-v5`, exact `meshy-7`, Blender HOI4 adapter 1.10.14, Blender 5.1.2, io_pdx_mesh 0.91.0, and a listening adapter bridge at `127.0.0.1:9876`. The environment report is `.tools/3d_pipeline/reports/environment_report.json`.

One materially different official Meshy firearm action was attempted on the accepted R2 rig. Action 236 `Draw_and_Shoot_Left`, task `01a038ed-330b-77ea-b344-91361978b5d5`, cost 3 credits and was formerly staged as `provider/downloads/animation_v9_action236_draw_and_shoot_left.fbx`, SHA-256 `69F0C530574439CF122410CE13ED107DC02145B1FCE078028ED91E93D5A808E1`. Its 161-frame clip retained the pistol but failed the aim/discharge/recoil/recovery gate and is rejected. The disposable provider binary was pruned after its hash and rejection evidence were retained. Live balance fell from 13 to 10.

The Quaternius Universal Animation Library Standard was then audited as a free professional-source candidate. The archive is CC0, SHA-256 `18FF1A7215F4852B320203E8AAF02A1578B5C8EEF9027FBAEDFCEDC7B85A3AC2`; its Unreal FBX SHA-256 is `C836C5D47DE2A414818F7644632AC43AA84475DF6709F4514B9410D232800FD9`. `Rig|Rig|Pistol_Shoot` transferred without adapter warnings to a 20-frame, 30 FPS alien candidate. Motion peaks at frame 6 and recovers by frame 20, and multi-view evidence confirms the integrated pistol remains in the right hand. Exact evidence is in `evidence/professional_animation/quaternius_universal_animation_library_standard/audit.md`.

At this historical checkpoint, the Quaternius clip was not yet promoted because source approval and a stable muzzle locator were unresolved. The candidate discharge crosswalk was frame 6 / 0.1667 seconds after clip start; `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` remained unbound. The later approved-promotion section below records the actual exports and reimports; defend, support attack, retreat, and death remain blocked.

## Approved Quaternius promotion and actual-byte proof

The user's prior broad approval and explicit request for a free firing-animation package approve Quaternius Universal Animation Library Standard CC0 as the professional source. This supersedes the approval blocker above but does not waive contact, semantic, locator, export, or runtime gates.

Three source actions passed retarget and visual review, exported through io_pdx_mesh, and reimported from their actual bytes against `export/mesh/alien_infantry_runtime_30k.mesh`:

- `Rig|Rig|Pistol_Shoot` -> `alien_infantry_laser_attack`, frames 1-20 at 30 FPS. Export `export/anim/alien_infantry_quaternius_laser_attack.anim`, SHA-256 `5B5260F21FAFC8827275827FF99A6D5BCAC29A02D8EAA99ED7ECEAE8D555C4AC`. Reimport proof `blender/checkpoints/reimport_reimport_alien_infantry_quaternius_laser_attack.blend`, SHA-256 `FC6EEC2317B15BD5104DBEC700A20A84CCE57BB839147B25D46225FF553C6A63`.
- Actual-byte firing contact sheet: `blender/previews/quaternius_laser_attack_actual_byte_reimport_contact_sheet.png`, SHA-256 `305B0149BD1A4544E8A5B93A4D90F42169599764146DE08DA6797B72E4152273`.
- `Rig|Rig|Pistol_Idle_Loop` -> `alien_infantry_idle`, frames 1-51 at 30 FPS. Export `export/anim/alien_infantry_quaternius_idle.anim`, SHA-256 `710D86BE58C74CC6BCE58A5BB9411D975BE31693B8D6530A1390A2BBE64EE09F`. Reimport proof `blender/checkpoints/reimport_reimport_alien_infantry_quaternius_idle.blend`, SHA-256 `4478C538AD813B1A66A3172B19F6A58D759EEF9043EBB645F9F2B9542D99EE12`.
- `Rig|Rig|Walk_Loop` -> `alien_infantry_move`, frames 1-41 at 30 FPS. Export `export/anim/alien_infantry_quaternius_move.anim`, SHA-256 `79E561F831D9C40C752D38412CF0C415A1FE03C07914AFE70A52DB58F35D4E79`. Reimport proof `blender/checkpoints/reimport_reimport_alien_infantry_quaternius_move.blend`, SHA-256 `C2188F2651613931414AEE80BCDBAA93FB452000A2B481E2DB0963E0185FE4B6`.

The approved `Crouch_Idle_Loop` defend probe was rejected because it produces an implausible one-leg balance. The approved `Death01` probe was rejected because the integrated pistol separates from the hand during collapse and settling. Neither was exported. Exact evidence is in `provider/rejections/quaternius_defend_death_contact_failures.md`.

The firing export is still not ready for runtime binding. The verified adapter schema exposes no supported muzzle-locator authoring or derivation operation, and creating one through unrestricted Blender or manual weapon parenting is forbidden. Frame 6 / 0.1667 seconds remains the exact discharge phase, but the particle, light, and sound identifiers remain unbound. Defend, support attack, retreat, and death remain blocked; support attack is not aliased to `Pistol_Shoot`.

## Final free-package search closure

The Meshy R2 rig remains valid and was preserved; no re-rig was justified. Its provider task is `01a0380c-df10-7a2c-ab1e-c28d2248b616`, and `provider/downloads/rig_pose_correct_v8_r2.fbx` retains SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`.

An additional Unlicense candidate, [ZenXChaos ThirdPersonShooter-AnimationSets](https://github.com/ZenXChaos/ThirdPersonShooter-AnimationSets), was archived and rights-verified at commit `f19adc2ece4cab0f89c9236223abb97d4d2badea`. It advertises revolver aim-shoot, backward aiming movement, crouch states, and multiple deaths. The archive SHA-256 is `8FA46E350F2B913CFC6A85A923DA358A8BFC7EABA5E177AA96885B7D68923D58`; its bundled Unlicense SHA-256 is `88D9B4EB60579C191EC391CA04C16130572D7EEDC4A86DAA58BF28C6E14C9BCD`.

The locked adapter rejected its `RevolverAimShoot.fbx` before scene creation because the source is FBX version 6000 and Blender 5.1.2 requires 7100 or newer. Adapter request `c328aa3a6afd45548ebebc6313596a23` is the exact evidence. Meshy conversion task `01a03958-ecee-79e3-af7c-4e39af57b978` was started as pre-authorized recovery, consumed 1 credit, and remained at 1% when the parent stopped the unsupported conversion route; no output was downloaded or used. ZenXChaos is evidence-only.

Rokoko did not yield a clearer redistributable open package in the search, while MoCap Online remained license-restricted and failed contact in the prior audit. Quaternius Universal Animation Library Standard is therefore the selected qualifying genuinely free package: CC0 rights verified, genuine firearm recoil/recovery verified, three actions exported and reimported, and all unresolved roles explicitly blocked rather than aliased or fabricated.


## 2026-08-25 additional free-package follow-up

Quaternius Universal Animation Library 2 Standard was retrieved from the creator's official page and creator-uploaded OpenGameArt distribution as a second CC0 candidate. The archive SHA-256 is `EC0E40D6D78FE9AAAD59E322F40865A8675C22F0745E291622E54520391A9217`, embedded license SHA-256 is `F9B1DE4E8FEFF135555AC1C7D2EEC65035A05FD74E4D632A3F826AC985C3F22C`, and Unity FBX SHA-256 is `D4A2DD67BB12BF0C01891BC59EE697E04DB679D26883D30BD937C2F3FB6FEC90`.

Locked-adapter request `8450b7c3d19a4f298e69c220bda462e9` inspected all 42 substantive clips. The free Standard tier has melee, shield, traversal, work, idle, and zombie actions, but no firearm aim/fire/reload, terminal collapse/death, armed retreat, or pistol-compatible defend action. It has no firearm object or stable muzzle locator. No clip was retargeted or exported, no Meshy credits were spent, and no runtime file was changed. Exact inventory and source evidence are in `evidence/professional_animation/quaternius_universal_animation_library_2_standard/audit.md`.

## 2026-08-26 evidence compaction after V10 review

The parent removed superseded V7/V8 preview frames and provider downloads, reproducible Blender preparation checkpoints and `.blend1` backups, per-action/source review blends, and the rejected candidate export directory. These ignored binaries were not runtime dependencies; hashes, rejection records, adapter logs, current V10 source-role FBXs, and the retained V10 base/remesh/rig sources remain available. The historical export and checkpoint paths in earlier sections are preserved as provenance and are not present locally after compaction.

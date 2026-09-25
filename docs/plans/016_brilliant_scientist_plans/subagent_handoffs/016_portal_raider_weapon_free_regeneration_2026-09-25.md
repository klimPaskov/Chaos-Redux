# Event 016 Portal Raider weapon-free regeneration — subagent handoff

Date: 2026-09-25  
Owner: chaosx_3d_model_pipeline  
Status: **canceled by the user before provider work; no model was created or altered**

> **Parent disposition, 2026-09-25:** The user explicitly directed that no models be created and that Portal Raider, Alien Infantry, and Autonomous Robot models remain untouched. The parent interrupted and closed the 3D worker, removed the unused Event 016 regeneration adapter allowlist, and will not resume model work under this goal. No Meshy generation, rig, or animation call was made; no `.blend`, `.glb`, `.fbx`, `.mesh`, or `.anim` file was produced in this isolated preflight job root. The historical preflight below is retained only as an audit record; its proposed parent recovery action is canceled.

## Scope and authorization

This covers only Portal Raider under docs/assets/016_brilliant_scientist/models_3d/portal_raider. Parent explicitly authorized one fresh weapon-free body Meshy7 generation, separate ray-rifle generation, at most one rig attempt, and one attempt for each required action. This supersedes the earlier preservation-only instruction for Portal Raider. The separate preservation acceptance job was not overwritten. No other models were touched.

## Outcome

The process MESHY_API_KEY gate passed: the environment variable existed and was non-blank; its value was not exposed. Preflight then found two hard locked-route blockers:

- Live Meshy image-to-3D schema accepts latest in addition to locked meshy-7 and describes pricing that conflicts with the lock. The lock requires meshy-7 only. No balance query or provider operation was made.
- The repository-owned Blender adapter has no allowlisted mapping for the specified Event 016 job root. Existing Portal Raider aliases point to shared or pilot roots. Read-only health through the recovery alias failed because its pilot directory is absent. Adapter operation identifiers and locked source hashes match, but this does not authorize a different root.

The locked loopback socket 9876 was listening. Locked Blender line/build is 5.1.2; executable metadata exposed 5.1, so exact build confirmation through adapter health is unavailable. No Blender asset operation was attempted.

## Inputs and provenance

The parent-provided visually reviewed body-only input is refs/original/meshy_input.png (1024×1536 RGBA), SHA-256 58F3F699C8B56796435B2C51FC2409478674FAE9539A01E40DEA89F6CBDEAE45. It shows the olive insulated suit, goggles, respirator, transit backpack and tubes with empty neutral hands.

The separate rifle input is refs/attachments/ray_rifle/original/meshy_input.png (1536×1024 RGBA), SHA-256 146C25D8A2E6D1A8ADF088DE911EED759D01221B6EAE66277345243A1577CBFA. It depicts the intended dark-metal/brass alternate-history ray rifle.

Historical source: “Sci Fi Soldier and Guns” by DasBilligeAlien, OpenGameArt, stated CC0, https://opengameart.org/content/sci-fi-soldier-and-guns. Historical source checksum in prior handoff: B704CC7286C3F76DC20A80D9DDEF44EADE350DA535E35B9DA64D02246A03F4DC. Current local refs/source/legacy_portal_raider_concept.png is SHA-256 9670EA470735AB87679741C9E6D110199E1BE15388624E480597AC4A80B733A3, so it is not byte-identical. The original ImageGen prompt and selected refinement lineage are absent in this job root. Parent confirms current input visual approval; source-byte/prompt linkage and native-alpha lineage remain unresolved here. Source pixels are not proposed as runtime art.

## Locks and versions

- dependencies.lock.json SHA-256: 1302A4CD4E35BDFE32FADE30BE75E425329C7538C73515704253FC8BDC0F26FE
- meshy_tool_schema.lock.json SHA-256: 2AA3E3761DCBE66BA56164E408C3FD279B253037ADC6388123D9389BF017AA7C
- blender_hoi4_adapter.json SHA-256: F54B526CE2E0DDF3C747270AB521D62714F1F16A8867FC38478FEA86E5DFA2C7
- Locked official Meshy package: @meshy-ai/meshy-mcp-server 0.4.0, git d8c77d1cb897e345eb41d38b510b8391b1664346; active schema mismatch above.
- Adapter version was read from dependencies lock: 1.10.51; config also identifies 1.10.51. Its live 32-operation list and 18 locked source checksums match.
- Locked Blender line/build: 5.1.2 / ec6e62d40fa9; exact build not confirmed through adapter.
- io_pdx_mesh installed manifest: 0.91.0, SHA-256 C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC; locked archive SHA-256 A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2.
- Locked socket 9876; loopback probe listening.

## Lineage, costs, and deliverables

No Meshy task or response IDs exist for this job. No provider result, Blender source/checkpoint, model or animation export, preview, material, or export checksum was produced. Conditional locked estimate: 92 credits (body 30 + rifle 30 + rig 5 + nine actions at 3 each). Consumed: 0. Live balance not checked because schema verification failed. Additional recovery credits authorized: 0; retries disabled.

All nine roles are blocked: idle, move, attack with aim/discharge/recoil/recovery, non-firing defend, moving-fire support_attack, retreat, portal_arrival, wounded, and articulated death. No static or transform-only substitute was made.

Vanilla reference is western_european_infantry.mesh with units_infantry.asset#infantry_entity. Parent-provided collision-excluded height is 7.3518242835; scale 0.8 once gives 5.8814594268 effective height; axes are -Y forward and +Z up. Fresh adapter measurement was blocked.

Existing audio and counter handoffs remain separate parent-owned artifacts and were not modified. This handoff does not certify their files, licensing, or runtime bindings for the current regeneration job. Parent-owned .asset, .gfx, sound/gameplay wiring and final review remain outstanding. The user owns live-game validation; no game was launched.

## Files written

- docs/assets/016_brilliant_scientist/models_3d/portal_raider/job.yaml
- docs/assets/016_brilliant_scientist/models_3d/portal_raider/manifest.md
- docs/assets/016_brilliant_scientist/models_3d/portal_raider/history.jsonl
- docs/assets/016_brilliant_scientist/models_3d/portal_raider/evidence/preflight_2026-09-25.md
- docs/assets/016_brilliant_scientist/models_3d/portal_raider/runtime/crosswalk.md
- docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_raider_weapon_free_regeneration_2026-09-25.md

## Historical proposed action — canceled by user direction

Repair and verify the pinned Meshy route so its live schema exactly matches the repository lock, including only meshy-7 and locked capability/cost behavior. Add a lock-authorized mapping for the Event 016 job root in the repository-owned adapter and refresh integrity evidence through approved bootstrap. Then reconcile source/refinement prompt lineage and rerun preflight. Only after both routes pass should the operator query live balance and spend within the recorded attempt policy.

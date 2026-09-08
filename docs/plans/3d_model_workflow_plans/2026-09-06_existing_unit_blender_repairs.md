# Existing unit model Blender repairs

## Accepted scope

The user requested one Meshy rigging attempt per model and one animation attempt per required action, with manual Blender rigging and animation under GPT-6-astra after the first failure or unusable result.
The user also explicitly requested direct Blender repairs of existing unit models with missing or faulty rigs and animations.
This authorizes repair of existing geometry without a new Meshy call; it does not authorize replacing unit identities or accepting static or whole-object motion as skeletal animation.

The user subsequently authorized automatic addition of every missing required model element in Blender, without further confirmation.
Every current firearm-bearing unit must be redone with a freshly generated Meshy 7 body without firearms, followed by direct GPT-6-astra Blender rigging, weights, modeled/attached weapons and held objects, and skeletal animation.
This firearm-specific route bypasses Meshy rigging and animation calls.
Native ImageGen removal of firearms and preparation of clear anatomy and neutral A/T-pose hands for the sole Meshy input are authorized.
Preserve the intended body identity, clothing, armor, proportions, and colors; retain the weapon design as separate Blender reconstruction evidence.

## Firearm worker dispatch contract

Use current canonical 3D/asset skills and this recorded user authorization when historical manifests require fused firearms or provider-only motion.
Read the package's current manifest, job, and handoff for original scale, materials, components, action roles, and runtime consumers.
Create sibling `attempts/20260906_weaponfree_blender/`, `refs/derived/20260906_weaponfree_body.png`, and `export/20260906_weaponfree_blender/` outputs; preserve previous accepted/runtime files until parent promotion.
Inspect the existing approved reference before native ImageGen editing, and send the resulting body-input path and checksum to the parent for visual review before generation.
Submit exactly one accepted weapon-free body image to the exact Meshy 7 model and download/checksum body and textures immediately.
Use current wrapper schemas and existing locked dependencies, not a hidden direct REST route.
The parent verified an account balance of 512 credits at the start of this tranche.
Each of the four firearm packages has a coordination reservation of 75 credits, with an initial expected body generation of 30 and optional remesh of 5; coordinate with the parent before exceeding its reservation rather than independently consuming another package's allocation.
Normal authorized body-generation recovery remains allowed within the live available balance and coordinated reservation.
No Meshy rig or animation call belongs to this firearm route.
Load the supplied credential from the Windows User `MESHY_API_KEY` environment value into each provider-wrapper process; existing tool hosts may retain the previous credential.
Never print the credential, include it in a command log or handoff, or save it in a repository file.

All Blender work uses the verified repository adapter, including structured calls through `BlenderAdapterClient.call` or `lib.mcp_stdio` and `wrappers/run_blender_hoi4_adapter.cmd` when the session tool list is stale.
Live discovery confirmed manual bone-phase editing and creature operations in addition to humanoid operations.
The gorilla worker owns the necessary shared adapter extension; other asset workers must send capability requirements to the parent and must not edit adapter/client/config/lock files concurrently.
Create real role-specific skeletal actions, separately controlled rigid weapons/props, measured grip/stock/muzzle contacts as applicable, and firing-state aim/discharge/recoil/recovery and sound/effect synchronization evidence.
Include all required components in the final geometry budget; limited body reduction to make room for props is authorized with visual/material/deformation comparison.
Retain existing licensed audio and counters and hand off revised animation synchronization; do not create unrelated new assets.
Every accepted package needs editable checkpoints, anatomy/weight/geometry/material checks, multi-frame action previews, actual-byte mesh/animation export and reimport proof, and exact source paths/checksums and runtime binding instructions.
The parent owns runtime copies, entity/GFX/animation/sound definitions, overall review, and commits.

| Firearm package | Authoritative job root | Required roles |
| --- | --- | --- |
| Alien infantry | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry` | idle, move, laser_attack, defend, support_attack, retreat, death |
| Autonomous robot | `docs/assets/shared_robot_system/models_3d/autonomous_robot` | idle, move, attack, defend, support_attack, retreat, training, death |
| Clone infantry | `docs/assets/shared_clone_system/models_3d/clone_infantry` | idle, move, attack, defend, support_attack, retreat, training, wounded, death |
| Portal raider | `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider` (adapter job `portal_raider_meshy7_recovery`) | idle, move, attack, defend, support_attack, retreat, portal_arrival, wounded, death, guard |

The legacy `docs/assets/shared_portal_raider_system/models_3d/portal_raider` package supplies historical identity/role context and must not trigger duplicate body production.

## Workflow implementation

Commit `f06bad9` updates the canonical 3D agent, five related skills, repository guidance, and pipeline README.
The generated Qoder and Cursor agent definitions were synchronized from the canonical TOML.
Blender-only client, wrapper, and server startup no longer require a Meshy API key.
The live wrapper returned 28 tools with the key absent, including manual bone-phase editing and creature rig/action operations.
The Blender health probe reported Blender 5.1.2, loaded io_pdx_mesh mesh/animation exporters, and adapter 1.10.21.
All five skill entrypoints passed the official skill validator.
Independent behavioral review covered a passing rig with a failed action, a creature repair without a provider key, and a successful provider task whose contacts fail visual review.

## Repair register

| Package | Evidence and disposition | Required repair |
| --- | --- | --- |
| `012_africa/gorilla_heavy_infantry` | Existing geometry and rig are present; Blender worker confirmed elephant trunk, tail, howdah, and rider bones in the gorilla rig, with incorrect vertex assignments. Accepted and in progress. | Correct gorilla anatomy and rigid hammer binding; inspect and repair idle, move, attack, recovery, and death; export and reimport actual bytes. |
| `012_africa/forest_giants` | Inventory identifies missing required axe/bound log in the geometry. | Add missing required components in Blender under the expanded user authorization and repair animation. |
| `016_brilliant_scientist/alien_infantry` | V13 is the previous accepted package. | Fresh weapon-free body plus Blender assembly/rig/animation is mandatory under the firearm redo request. |
| `oracle_recon` | Initial inventory identifies a current package rather than confirmed rig/action failure. | Check firearm status before deciding whether the firearm redo applies. |

The remaining package inventory is in progress.
This register is not a completion claim.

The gorilla baseline front/right renders also confirm an empty-handed mesh, although the job identity requires an oversized hammer.
The user explicitly selected: “Add a hammer in Blender and animate a hammer attack.”
The gorilla worker may model the hammer, bind it rigidly to the gripping hand, and author the complete hammer attack in Blender.
The parent permits only the small body reduction needed to keep the body and hammer within the existing 25,000-triangle ceiling, with before/after silhouette and material validation.

## Gorilla tool dependency

The existing creature-rig operation only handles a winged-biped exception; other family strings fall through to an elephant skeleton.
The existing action operation has the same anatomy assumption.
The parent authorized a narrow adapter extension for a measured custom rig, explicit weights, and rigid hammer attachment, with preservation of source geometry/materials and rejection of unsupported inputs.
This extension must be followed by actual model repair, semantic animation review, and export/reimport evidence.
The gorilla worker owns the bounded extension and package artifacts; the parent owns dependency-hash review and runtime promotion.

## Acceptance and ownership

Keep provider sources and previous accepted checkpoints intact.
Author repairs in sibling checkpoints and retain editable rigs, weights, and skeletal keys.
Require anatomy, deformation, ground/root policy, loop closure where applicable, and role-specific multi-frame visual evidence before promotion.
Use the package's existing sound and counter assets; report changes to animation synchronization for parent review.
The parent must compare selected source and runtime hashes, review active mesh/action bindings, and record every remaining defect or omission.
No live-game validation is performed by agents.

## Active repair coverage

The parent approved all four prepared weapon-free body references after visual source comparison.
The parent released paid body generation after reviewing deployed io_pdx_mesh modernization differences: Python 3 and Blender compatibility changes, with no mesh/animation binary-layout or skinning-limit changes identified.
Exact deployed source hashes and diffs are recorded in the alien attempt io_pdx_reconciliation/source_comparison.json; the deployed build is not falsely described as byte-identical to the archived release.
Actual-byte export/reimport remains required for each final candidate.
The confirmed balance at intake was 512 credits, with a 75-credit reservation for each firearm package.

| Repair assignment | Current scope |
| --- | --- |
| Gorilla | Replace incorrect elephant rig, add hammer, author five roles. |
| Pan sappers and Riverborn | Replace incorrect elephant rigs, complete shovel or spear/shield assembly, five roles each; Riverborn uses latest approved recovery4 body. |
| Stone cohorts and forest giants | Use accepted dark ornate stone body and existing tree body, correct rigs, add missing polearm/axe/bound log and required actions. |
| Plague carriers | Use accepted pack-donkey body with anatomy-specific quadruped rig, rigid cargo controls and five roles. |
| Paleogenetic creature and xenobiological assault organism | Preserve good existing rigs/actions, repair duplicate or missing semantic roles and validate material/deformation evidence. |
| Temporal guard | Inspect newer support/retreat checkpoints and repair action/material/deformation faults using accepted unarmed body. |
| Base, undead, rabid and infected zombies | Recover immutable source from runtime where source jobs are missing; inspect four current actions and implement eight proper semantic roles. |
| Parasitic, mutant, necrotic and demonic zombies | Recover runtime source, preserve anatomy including demonic wings, repair rigs/actions and cover eight roles. |

Oracle recon is unarmed and does not enter the firearm regeneration route.
Current rat and cannibal packages have accepted non-firearm bodies and are not automatically regenerated.
The assault battalion is dispatched for confirmed aim/action/death faults and source recovery; its material filename mismatch remains parent-owned integration work.
The cave monster has valid existing actions whose historical rejection was provider provenance only; ghost hosts have accepted reimported actions, and elephant shared base is retired in favor of vanilla elephantry.
Those three packages require no model repair based on current evidence.
Counter identity and historical audio provenance defects discovered during companion inspection remain explicitly recorded separately from the requested physical model repairs.

## Recorded implementation progress

Workflow commit `b4ea245ac` records automatic missing-component completion and the firearm-free Meshy body/direct Blender assembly route.
Material commit `b69a3bcc5` corrects provider roughness to engine glossiness in both PDX packers and adds a test proving source preservation, channel inversion, and unchanged glTF roughness semantics.
The installed shader and the importer interpret specular alpha differently; a Blender preview alone cannot validate the engine map.

All four weapon-free Meshy 7 body tasks succeeded and were downloaded immediately with checksum evidence.
Each task reports 30 consumed credits: 120 total, with the observed account balance at 392 after completion.
No Meshy rigging or animation calls were used.

| Package | Meshy task |
| --- | --- |
| Alien infantry | `01a07659-5c46-71ee-b05f-8cb3fa8cc1d4` |
| Autonomous robot | `01a07650-7b7a-713a-ae14-bb0a933eedb6` |
| Clone infantry | `01a07650-77c9-7244-ad86-b0434c78452c` |
| Portal raider | `01a07650-f80a-7523-b547-7d1f7ccc0221` |

The parent visually reviewed the alien and portal fresh body front previews and accepted their identities for continued rig work, with final topology, materials, assembly and animation still pending.
The gorilla has an actual 29-bone measured rig and rigid 196-triangle hammer, totaling 24,595 triangles after a bounded body reduction that reserves surface-repair capacity; overhead-pose review requires smooth exact skin weights and local topology correction before acceptance.
The pack-donkey has an actual anatomy-specific rig, hinged wooden cargo closure and five authored roles; final cargo settling and export/reimport review remain in progress.
Pan has a measured digitigrade rig and required tool/kit components in progress.
Stone has a measured rig on its latest approved body.
Paleogenetic and xenobiological action repairs are integrated into runtime files after parent pose review and complete source-to-destination checksum validation: eleven paleogenetic roles and ten xenobiological roles, with six repaired actions and corrected gloss maps.
Their accepted source meshes and other valid action bytes remain preserved.
The detailed action handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-09-06_pilot_creature_action_repairs.md`; inherited audio limitations and paleogenetic small boundary edges remain explicit.
These are implementation progress records, not completed package or live-game claims.

The shared adapter provides measured rest geometry/bone inspection, explicit bone/weight-region authoring, rigid component geometry and manual role phase keys.
A namespaced prepare route protects previous fixed-name checkpoints; input and output path isolation, source containment, legacy behavior and overwrite rejection were checked before release.
Concurrent adapter maintenance in other active tasks changes shared source hashes; each worker must use a coherent published lock and must never bypass mismatches.
The bounded adapter recovery owner is preparing source-preserving export checkpoint, recovered-mesh metadata, material attachment, winding and grounding fixes while asset workers continue independent production.

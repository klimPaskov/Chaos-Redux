# Event 018 cave monster current package manifest

Date: 2026-09-12.

Disposition: `implemented` for the current static runtime package.

Acceptance basis: the parent task for this documentation reconciliation carries the current exhaustive read-only audit finding that the installed action set consists of four authored actions and that the entity aliases `defend` and `support_attack` to `attack`, `retreat` to `move`, and `training` to `idle` are intentional for the accepted current package. This acceptance basis supersedes the eight-distinct-Meshy-action recovery requirement recorded on 2026-08-22, but it does not create user-provided in-game evidence.

The authoritative current package consists of one registered mesh, three registered material maps, four present and registered skeletal actions, one canonical entity, five sprite-resolving entity aliases, and five live sub-unit consumers. Current runtime bytes match the production hashes preserved by the 2026-08-10 handoff and visual-closure evidence.

Package-level `complete` is not claimed under the current 3D pipeline contract because the deterministic source/job root, current job manifest, approved input image, Blender checkpoints, selected export copies, and reimport artifacts are absent from the checkout. The missing job package is the true remaining production and reproducibility blocker. It does not negate the current runtime implementation evidence, but it blocks deterministic continuation, repair, regeneration, or strict source-to-runtime reconstruction from this checkout alone.

Live HOI4 presentation, entity-state transitions, audible playback, sound synchronization, audible density, and map-zoom readability remain unverified user-owned validation limits. They are not represented as completed in-game evidence.

## Current runtime byte inventory

| Runtime file | Bytes | SHA-256 | Current role |
| --- | ---: | --- | --- |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster.mesh` | 1,876,278 | `60C256EC1D958F77A93B6F9019A4B7C60072EA2F6B13E69C3672B84C474A491C` | canonical creature mesh |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_diffuse.dds` | 4,194,432 | `A876F57B87A36A79FE7A320D4445BD112CBA957474028E1E5680C0439626FE11` | diffuse map |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_normal.dds` | 4,194,432 | `9EF36A184A57A7BD451A6F90C6CB23D50CFC884EE6EE7FBF0958ABB0F3309D19` | packed normal map |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_spec.dds` | 4,194,432 | `9CFC7A88676CE46E4F017381DB38860BDBF84555C1BC59020C2D0FE4D2B88CDF` | packed specular map |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_idle.anim` | 25,276 | `A8EA9301744231054D3DA131AAF7D2EF264E13FD48A5F737325BA531DC9762D0` | idle and training |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_move.anim` | 14,367 | `077D8ADCB45484215DB7BA6F4F45D95B184785358441DA67980B0D061EB52246` | move and retreat |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_attack.anim` | 17,798 | `13D54654770BD0E82846F847F4CDD14535755F061BA83DB2254F821FD2BB19AA` | attack, defend, and support attack |
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_death.anim` | 20,660 | `5A4677B24D0CB4ED3F506DDB1666B263AABF6D3CDB098255560DF6F773E1601A` | death |
| `gfx/models/units/018_resources_found_cave_monster/animation_018_resources_found_cave_monster.asset` | 538 | `DD93E540F5A518CFDB606A325B0B42033EC0B0C156EF41A29D9C40AC6542851A` | four animation type registrations |

## Current registration and consumer inventory

| Surface | SHA-256 | Current evidence |
| --- | --- | --- |
| `gfx/entities/018_resources_found_cave_monster.gfx` | `99E2196F8EA4A5A7E7FB483E631EA429C3BFA8D225FC83AF3B2E69CB6D5F2931` | registers `resources_found_cave_monster_mesh`, the four action IDs, `Mesh_0.001`, the three material maps, and `PdxMeshAdvanced` |
| `gfx/entities/018_resources_found_cave_monster.asset` | `72F8AD8EEACB9770727D9A4B488E4117326F614153F7AAEAFE0DDBF018B7548A` | registers the canonical entity, state-to-action aliases, timed sound hooks, scale `0.8`, and five clone aliases |
| `common/units/018_resources_found_cave_broods.txt` | `504074622815060DE81DC351157C3A6979F1222AF3E3AB286F071420765D0087` | five sub-units declare the five sprite tokens resolved by the entity aliases |
| `interface/chaosx_subuniticons.gfx` | `D925EDF770E9A7888216DAC20DA6E51B865996BCA99C893AE00860F78AF0D492` | owns the five bespoke large and on-map counter registrations; the file hash covers the full shared registry |
| `sound/chaosx_resources_found_cave_monster_sound.asset` | `F0B02F305B7BA83B042506B3BA5FFC39F077F81361A9A7D83D3A9B0EB1667460` | owns the cave-monster sound definitions consumed by the entity state events |

The five sprite consumers are `cave_monster_brood`, `cave_stone_phalanx_brood`, `cave_burrow_war_brood`, `cave_scree_tide_brood`, and `cave_anchor_guard_brood`. Their resolving entities clone `resources_found_cave_monster_entity`.

## Durable evidence and validation limits

- `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md` preserves production lineage, geometry, rig, action, material, audio, counter, export, and reconstructed static-evidence facts.
- `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_visual_closure_2026-08-10.md` preserves the later actual-runtime-byte visual closure, including the combined idle/move contact-sheet SHA-256 `FC5D8A8AB3CCA0BE8143B7767DC55EE710E60CC7D4691C825958C8C5E03258AB`.
- `docs/plans/018_resources_found_plans/018_cave_monster_3d_integration_addendum.md` records the implemented sprite-to-entity repair and sound synchronization contract.
- `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md` remains the durable runtime behavior contract.
- The 2026-08-10 static closure audit is superseded because the later visual closure supplied the review evidence that it lacked.
- The 2026-08-22 eight-role Meshy recovery blocker is superseded as the current package disposition because its eight-distinct-provider-action premise is not the accepted current action contract. Its provider-capability finding remains valid only if that discarded requirement is explicitly adopted again.

## Exact remaining blocker

`docs/assets/018_resources_found/`, `docs/assets/018_resources_found/models_3d/cave_monster/`, and `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/` are absent. No current cave-monster job or package manifest exists elsewhere under `docs/` apart from this durable current-state manifest.

The absent source/job package blocks deterministic re-export, regeneration, action repair, and fresh source-to-runtime proof. Recovery would require a newly authorized production tranche that reconstructs a complete current job package under the then-current 3D pipeline rules; historical paths and hashes alone are not equivalent to the missing source files, checkpoints, and reimport artifacts.


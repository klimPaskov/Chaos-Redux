# Chaos Redux 3D model pipeline handoff: Death ghost hosts

## Outcome

Status: `runtime_staged_needs_user_validation`. The existing Meshy generation, rig, preserved provider actions, Blender checkpoints, corrected `.mesh`/`.anim` exports, previews, reimport proof, and all six sourced-audio roles are complete. The parent runtime package is wired to the shared entity and all three Death ghost host consumers. No model regeneration was used.

The package root is `docs/assets/010_death/models_3d/ghost_hosts`. Detailed validation is in `validation/package_report.md`; provider lineage is in `provider/lineage.json`; runtime copy guidance is in `runtime/handoff.md`; audio evidence is in `sound/handoff.md`.

## Provider and cost lineage

- The only provider input was `refs/original/meshy_input.png`, 1024x1536, 2,314,312 bytes, SHA-256 `1E639F23A5F6E7447B5A6BA590546FC70547E5F73457A474C8D42C3E7E68E596`. No second input, turnaround, collage, side sheet, or multi-view provider image was created.
- Legacy Meshy generation task `019fd5e1-5b10-7987-bb1d-39dea4078341`: 30 credits. GLB SHA-256 `2FDE05AF70E5A371EFC23A45E2E8873DF5DA427ED80324B640990C6CFBCFCA98`; FBX SHA-256 `094635F69A115061CFE664674D54FE4CC2F2263FDE0236BC4940E4ADF2BBF598`. Future regeneration uses Meshy 7.
- Rig task `019fd5e7-93d7-7ad0-84bc-1a9689fbd6b0`: 5 credits, measured provider height 1.8984103203 m. Rigged GLB SHA-256 `8E85A1D42429D3751DFDF92ED92A92A4323178E953971AAA468419B488940C9F`.
- Idle task `019fd5e9-86fd-7cc9-a649-8ef75d18e402`, attack task `019fd5e9-8978-7ae7-8f8a-15d8507ee296`, death task `019fd5e9-8b5b-7f13-8e19-04c621c5a705`: 3 credits each, all converted to 24 FPS by the provider.
- Balance: 598 before generation, 554 after all calls. Total consumed: 44 credits. Extra recovery consumed: 0.
- The Meshy route returned provider task IDs but did not expose separate provider response IDs; none were invented.

## Dependency and adapter evidence

- Environment bootstrap with Meshy probe passed.
- `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Blender 5.1.2 build `ec6e62d40fa9`; Blender MCP add-on 1.0.0; repository adapter `chaosx_blender_hoi4` 1.2.2.
- Structured health request `ead642305eb74d2b9c61aee35fbb8108` passed and exposed the required io_pdx_mesh mesh/animation functions and operators.
- io_pdx_mesh 0.91.0, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Lock hashes are recorded in `validation/package_report.md`. Failed local prepare requests `472d008ca0ae43a3ab77c2b19e05ada5` and `4784c4e5ed384ba491d2fbd82fb8b98a` were schema-key mistakes, were corrected without provider spend, and remain in adapter logs as evidence.

## Model and material results

- Candidate geometry is 30,000 triangles / 14,983 vertices, triangulated, UV-mapped, zero degenerate faces, zero non-manifold edges, zero negative-scale objects, and zero zero-length normals.
- The remaining 128 boundary edges are 31 tiny torn-coat/wisp components reviewed in front, rear, side, top, underside, and three-quarter previews. Bounded repair refused unsafe caps.
- Calibration passed against installed `western_european_infantry.mesh` and `infantry_rifle_entity`: source height 7.3518242835, entity scale 0.8 exactly once, effective runtime height 5.8814594268, forward -Y, up +Z, base z approximately zero, collision-only object excluded.
- PdxMeshAdvanced is exported with 1024x1024 diffuse, packed specular, and packed normal DDS maps. Exact texture and export hashes are in `runtime/handoff.md`.
- Exported mesh: `export/mesh/death_ghost_hosts.mesh`, SHA-256 `897E178D4B558A7B11EDEE9031111A69EC8B19CA58130FDDCE079F2116464CCB`.
- Final weight audit on `blender/checkpoints/07_runtime_candidate_sanitized.blend` reports 14,983 working vertices with zero unweighted deforming vertices, zero vertices over four influences, and maximum four influences.

## Actions and reimport

- Idle: 24 FPS, frames 1-97, real skeletal loop, in place, exported and reimported; accepted action candidate. SHA-256 `51F1ADD1A63FDAE5DFEAB4453DE17F9AD958A194126B37BE3B1B985FEB915101`.
- Attack: 24 FPS, frames 1-68, real skeletal one-shot, in place, exported and reimported; accepted spectral lunge candidate. SHA-256 `1FC2407121292CAC8C105725E7B821FD448AA493CC5EA2CD2CD180341BA77D08`.
- Move: 24 FPS, frames 0-24, real Blender-authored skeletal loop, exported and reimported after structured grounding correction; accepted. Final reimport evidence is `validation/reimport_death_ghost_move_final_reimport.json`.
- Death: 24 FPS, frames 1-72, real provider skeletal one-shot, exported and reimported after a bounded existing-action root correction; accepted. Final reimport evidence is `validation/reimport_death_ghost_death_offset_reimport.json`.
- Retreat: real preserved provider run FBX retimed from 30 FPS to 24 FPS through the locked adapter, grounded, exported, and reimported; accepted. Final action is `death_ghost_retreat.anim`.
- Defend and support_attack map to the accepted attack action, and training maps to idle, matching installed vanilla entity precedents.

## Audio

- All six roles have licensed source originals and derived 44.1 kHz mono PCM16 WAV candidates with checksums, transformations, attribution, URLs, synchronization points, and proposed identifiers in `sound/handoff.md`.
- The Wikimedia death derivative was rate-limited, so the exact CC0 Internet Archive FLAC linked by that source page was downloaded and mechanically trimmed. The death candidate is wired but still needs parent creative review because it is the recognizable Wilhelm scream.
- Parent-owned sound/soundeffect definitions and entity-event wiring are complete for the runtime package; selection remains a registered soundeffect because it is a UI/unit-selection role rather than an entity animation event.

## Runtime and parent work

Reserved identifiers are now staged as sprite `death_ghost`, entity `death_ghost_entity`, pdxmesh `death_ghost_hosts_mesh`, mesh destination `gfx/models/units/death_ghost_hosts/death_ghost_hosts.mesh`, entity registration `gfx/entities/010_death_ghost_hosts.gfx`, entity definition `gfx/entities/010_death_ghost_hosts.asset`, and animation registration `gfx/models/units/death_ghost_hosts/animation_death_ghost_hosts.asset`.

Source-to-runtime synchronization is complete for the mesh, five animations, three counter DDS files, three model textures, and six derived WAV files. Every runtime binary was copied from the accepted job evidence and its SHA-256 matches the source handoff. The three unit definitions now use `sprite = death_ghost`.

The counter handoff is also wired through `interface/chaosx_subuniticons.gfx` and `interface/chaosx_texticons.gfx`. Live HOI4 rendering and consumer verification remain user-owned.

## Correction tranche resolution

The adapter was refreshed to version 1.2.2 and the structured operations `sanitize_runtime_candidate`, `import_animation_action`, `retime_animation_action`, `correct_action_grounding`, and `offset_action_root` were exposed through the locked MCP route. The correction work used only the preserved model, rig, and provider action downloads; no Meshy call or paid recovery was made. The resolved route evidence is in `validation/correction_route_blocker.md`.

## Files created or updated

- Job metadata: `job.yaml`, `manifest.md`, `history.jsonl`.
- Provider evidence and downloads: `provider/lineage.json`, `provider/downloads/`.
- Blender source/checkpoints/reports/previews: `blender/`.
- Processed textures and final DDS: `textures/`.
- Candidate PDX exports and text proofs: `export/mesh/`, `export/anim/`.
- Reimport reports and runtime guidance: `runtime/`.
- Audio source selection, originals, derived WAVs, and handoff: `sound/`.
- Validation: `validation/package_report.md`.
- This permanent handoff.

No model regeneration or transform-only animation fallback was used. The remaining user-owned review items are live HOI4 rendering/consumer validation and creative acceptance of the recognizable death sound.

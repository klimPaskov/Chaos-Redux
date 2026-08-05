# Event 018 cave monster 3D model handoff

Status: `needs_user_review`. A bounded model package was produced with source evidence, PDX textures, a custom creature rig, grounded idle/move/attack/death exports, previews, reports, checksums, io_pdx_mesh actual-byte reimports, four licensed audio originals and mechanically converted runtime WAVs. The parent has copied and hash-verified the selected model/actions, wired the shared entity and animation asset, registered sound hooks, and installed five bespoke counter families. Remaining review is limited to the subtle idle/move read and live consumer validation.

## Provider and dependency lineage

- Reference: `docs/assets/018_resources_found/models_3d/cave_monster/refs/original/meshy_input.png`, SHA-256 `F04C5C4B934959D436A1888A3AB0F520D054ECE9CBE56A58D95C5CD22967A361`.
- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, wrapper `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`.
- One Meshy-6 image-to-3D call: task `019fd394-e30c-7fbb-b0da-ee8078b86c38`, 20 estimated credits, 30 consumed credits. No retry, remesh, retexture, provider rig, conversion, or provider animation call was used.
- Locked Blender adapter: 1.2.0, wrapper `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd`; Blender 5.1.2 build `ec6e62d40fa9`; io_pdx_mesh 0.91.0.
- Lock hashes: dependencies `F84BC430746C016888D3AEFE2D5ED2969E5E5B8CF90D7EEBD52EB9C49DB08431`; Meshy schema `DBB9CAD7FB12AFE81ECA05A2F381EF4251C035F4D22BF17856A2F6D41F16A62D`; adapter config `0AE3432A008C06F7C7ECFC2877B5C2775C12C0B9C0AD5FCD68F412B0C76722E6`.
- Initial adapter requests rejected an absolute path and unsupported metallic/roughness roles. Their immutable result logs are retained. Corrected preparation request `d9cc5b3bf6504924912e75618b566689` passed.

## Selected artifacts

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `provider/downloads/cave_monster_meshy6.glb` | 31,304,560 | `B1F260FA6BE86F89B9D56CD5647403398CF0E3FEC5F86E0C95E797C3BF1ED3C3` |
| `provider/downloads/cave_monster_meshy6.fbx` | 45,159,996 | `515543F98A1965D702BD28BEC228B36B7E036957F4B437B4E2228A34AA178261` |
| `export/mesh/resources_found_cave_monster.mesh` | 1,876,278 | `60C256EC1D958F77A93B6F9019A4B7C60072EA2F6B13E69C3672B84C474A491C` |
| `export/anim/resources_found_cave_monster_idle.anim` | 25,276 | `A8EA9301744231054D3DA131AAF7D2EF264E13FD48A5F737325BA531DC9762D0` |
| `export/anim/resources_found_cave_monster_move.anim` | 14,367 | `077D8ADCB45484215DB7BA6F4F45D95B184785358441DA67980B0D061EB52246` |
| `export/anim/resources_found_cave_monster_attack.anim` | 17,798 | `13D54654770BD0E82846F847F4CDD14535755F061BA83DB2254F821FD2BB19AA` |
| `export/anim/resources_found_cave_monster_death_revised.anim` | 20,660 | `5A4677B24D0CB4ED3F506DDB1666B263AABF6D3CDB098255560DF6F773E1601A` |
| `textures/dds/resources_found_cave_monster_diffuse.dds` | 4,194,432 | `A876F57B87A36A79FE7A320D4445BD112CBA957474028E1E5680C0439626FE11` |
| `textures/dds/resources_found_cave_monster_normal.dds` | 4,194,432 | `9EF36A184A57A7BD451A6F90C6CB23D50CFC884EE6EE7FBF0958ABB0F3309D19` |
| `textures/dds/resources_found_cave_monster_spec.dds` | 4,194,432 | `9CFC7A88676CE46E4F017381DB38860BDBF84555C1BC59020C2D0FE4D2B88CDF` |

Protected source is `blender/source/resources_found_cave_monster_provider_source.blend` with SHA-256 `CF4FB11A6D5ACE9422A2084A37598D583724D40A30AE71E3FA2E8661A0D3F3EA`. Final checkpoint is `blender/checkpoints/05_pre_export_final.blend` with SHA-256 `2AE19F648671D024657A1C38C336109920EB4A6785F436E91536F8040268565E`.

## Geometry, material, rig, action, and export results

- The provider source was protected; the working duplicate was reduced from 745,600 to 30,000 triangles and has 14,998 vertices, one UV map, zero boundary edges, zero non-manifold edges, and zero degenerate faces.
- The selected vanilla references are `western_european_infantry.mesh` and `infantry_rifle_entity`. Measured source height is 7.3518247977, entity scale is 0.8 exactly once, effective runtime height is 5.8814598382, forward is `-Y`, and up is `+Z`.
- The one coherent armored quadruped retains head, four limbs, carapace, and tail. Seven textured views were rendered. The underside view was occluded by the adapter ground plane. The adapter does not expose wireframe or untextured preview modes.
- Provider PBR sources were packed to the verified PDX channels. The mesh text references only the three stable selected DDS names. Auto-generated `texture_0.dds`-family staging maps are rejected and must not be copied.
- The custom nonhumanoid armature has 17 bones. All 14,998 working vertices have a normalized weight and no deforming vertex is unweighted.
- Idle: 24 fps, frames 0-48, loop, in-place. Move: 24 fps, frames 0-24, loop, in-place. Attack: 24 fps, frames 0-32, non-loop, in-place. Death: 24 fps, frames 0-36, non-loop. No scale F-curves or unit-location rescaling were introduced.
- Final v4 action exports use the corrected semantic angle envelope for this hard-weighted creature rig: idle and move remain restrained loops, attack is a short grounded strike, and death is a short grounded collapse without visible mesh shear in the reviewed previews. Final action reimports contain the 17-bone rig and 30,000-polygon mesh with contact ranges within approximately +/-0.000015 m. The final source/runtime hashes are recorded in `runtime/crosswalk.md` and `validation/final_checksums.sha256`.
- This worker's first corrected export request `eed3fc1b521f4240a583d6578645af7d` hung after a long preview call and produced no result or output mutation. The parent retried through the same repository-owned adapter; the successful request and byte hash above supersede the hung request.
- Mesh and all four actual animation bytes were reimported through io_pdx_mesh. Reimports contain the 17-bone `io_pdx_rig` and 30,000 polygons; position-weld diagnostics pass closure. Export request IDs and reports are preserved under `blender/reports/` and `logs/adapter/`.

## Sourced audio

Research pages, direct URLs, creators, and licenses are recorded under `evidence/audio/source_urls.md`.

- Idle candidate: `evidence/audio/original/idle_alligator_bellow.ogg`, U.S. Fish and Wildlife Service public domain, SHA-256 `72A5612E99B6A941D751EFBCCF1E44F816C06C7884E3108C5298A2BA84B25169`.
- Move candidate: `evidence/audio/original/move_walking_on_gravel.ogg`, CC0 1.0, SHA-256 `14990DE1FD15418B55A2C939B0A99348446E613C1C4A5A307E49A87D228DE5EF`.
- Attack candidate: `evidence/audio/original/attack_lion_roar.ogg`, public-domain dedication, SHA-256 `AB237D0F960E83412251D0C11F69959F3C2E8D3B14595F7181C3056F7FA18BF7`.
- Death candidate: `evidence/audio/original/death_gravel_rocks.ogg`, public-domain dedication, SHA-256 `BC254F5C70EE0252FDC79278F83E5428B6953807CFC21805052E6A617F2BB330`.
- No audio was synthesized, recorded, generated, or unlicensed. Wikimedia initially returned HTTP 429, then the recorded direct upload URLs succeeded with an explicit user agent. The parent mechanically converted all four immutable originals to mono 44.1 kHz PCM WAV runtime candidates, trimmed four movement contacts plus bounded attack/death derivatives, recorded their hashes and durations, and wired timed entity hooks. The exact roles, synchronization points, source URLs, and transformations are in `evidence/audio/sound_design_handoff.md`.

## Bespoke counters

Exact installed-vanilla inspection is recorded in `evidence/counter/counter_artist_handoff.md`. The five consumers are `cave_monster_brood`, `cave_stone_phalanx_brood`, `cave_burrow_war_brood`, `cave_scree_tide_brood`, and `cave_anchor_guard_brood`.

The inspected references are `interface/subuniticons.gfx` lines 36 and 189, `unit_mountain_icon.dds` at 152 by 42 with two 76 by 42 frames, and `onmap_unit_mountain_icon.dds` at 60 by 12 with two 30 by 12 frames. The matching skill-local land counter contact sheets were inspected. Large olive-green samples include RGB 73/106/73, 62/89/62, 85/116/85, and 112/138/112. Ten original strips were produced, round-tripped, copied into the two runtime counter folders, and registered with the five subunit tokens. The parent owns the final consumer review.

## Parent-owned remaining work

1. Review the restrained idle/move motion; attack and revised death grounding are corrected and proven.
2. Review the four mechanically converted licensed WAVs; sound definitions and entity hooks are already wired.
3. Review the ten bespoke DDS strips and their five registered subunit tokens.
4. Perform live in-game validation of the copied model, actions, sound hooks, and counters; source-to-runtime hashes and static bindings already match.

The worker boundary remained source-only: it did not edit gameplay, event, focus, decision, country, history, AI, localisation, GUI, GFX, entity, `.asset`, sound definition, on_action, spreadsheet, or runtime files. The parent applied the runtime model, animation, sound, counter, entity aliases, and subunit wiring described above. No fallback or scope reduction was silently accepted.

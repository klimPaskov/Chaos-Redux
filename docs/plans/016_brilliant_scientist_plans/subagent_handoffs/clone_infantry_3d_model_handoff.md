# Clone infantry 3D model production handoff

> Current documentation disposition, 2026-08-09: the clone infantry model/entity package is installed and reusable by generic consumers. This handoff's historical `needs_user_review` action-gate wording remains evidence for any parent-owned playback or action review, but it does not mean that the package is absent. Its installed status does not claim whole Event 016 completion.

Status: **needs_user_review; recovery geometry/material/rig/non-weapon actions/audio/counters complete; rifle attachment proofs blocked; death terminal sample repaired**

Owner id: `shared_clone_system`

Asset slug: `clone_infantry`

Deterministic job root: `docs/assets/shared_clone_system/models_3d/clone_infantry/`

## Outcome

The job produced a clean weaponless legacy Meshy recovery mesh, a verified PDX material set, a 24-bone rig, nine exported and reimported skeletal action candidates, a legally sourced human-infantry audio package, and bespoke frame-aware counters plus clone-cohort equipment and technology art under `counter_art/`. The original fused-rifle candidate remains preserved as rejected evidence. Future regeneration uses Meshy 7.

The exact installed vanilla `ENG_weapon_rifle.mesh` is staged with matching hashes and reimports with genuine `muzzle` and `cartridge` locators. The package still cannot be marked complete because locked adapter 1.2.2 has no operation to attach that second mesh to recovered `RightHand`, fit or reorient its local transform, preserve the locator hierarchy, or render combined attack/support/training contact and muzzle-alignment proofs. The recovery death terminal offset was independently repaired and verified through export/reimport.

## Superseded original 3D files

- Mesh: `export/mesh/clone_infantry.mesh`, SHA-256 `7b172ca905b870aeeb3fbd46302b8b4722c6b82990369467fc8049bc2a2f5f3f`.
- Diffuse: `textures/dds/texture_0.dds`, SHA-256 `e56bafe99d3d8fa49b977517f7f4cacf3b99346434b930e3669078546c2c263d`.
- Packed specular: `textures/dds/texture_specular.dds`, SHA-256 `c1736236bd78d3d42d29b4ced163e30f2dba9fd5028a455dc16205248bbbb06c`.
- Packed normal: `textures/dds/texture_normal.dds`, SHA-256 `da0248deb182875350bca3d7b94842d36176b39627018ca89a14cfbdee401899`.
- Actions: `export/anim/clone_infantry_{idle,move,attack,defend,support_attack,retreat,training,wounded,death}.anim`; exact hashes and acceptance states are in `blender/reports/action_manifest.md`.

## Provider and credit lineage

- Reference: `refs/original/meshy_input.png`, SHA-256 `adfe9bf039975e6048daf64d06c2aa45562adbb96c1074330d04bb3293db5981`.
- Legacy Meshy generation task `019fd2f4-8ffa-7c67-8c2d-cfc3503f6f9c`, 30 credits.
- Rig task `019fd311-4488-7174-905a-ae7b87d7e378`, 5 credits.
- Eight paid animation task ids and their downloaded GLB/FBX hashes are recorded in the job provider manifests and `blender/reports/action_manifest.md`, 24 credits total.
- Attributable spend: 59 credits. Latest observed balance: 740. The 30-credit difference between attributable spend and the shared-account balance delta is not claimed by this job.
- No remesh, retexture, conversion, retry, or recovery credit was spent.

## Technical evidence

- Dependencies: official Meshy MCP `0.4.0`; Blender `5.1.2` build `ec6e62d40fa9`; adapter `chaosx_blender_hoi4` `1.2.2`; `io_pdx_mesh` `0.91.0` SHA-256 `a683df08318cb700014c7fe9a3d15139e5fb2313c7e98715204263e48931f7c2`.
- Canonical geometry: 29,999 triangles, 14,991 welded vertices, one mesh, zero degenerates, zero non-manifold edges, no negative scale.
- Vanilla calibration: installed `gfx/models/units/western_european_infantry.mesh` / local staged `blender/reference/western_european_infantry.mesh`; mesh height `7.3518242835`; `infantry_entity` scale `0.8`; effective height `5.8814594268`; forward `-Y`; up `+Z`.
- Material: `PdxMeshAdvanced`; final runtime specular uses R=0, G=32, B=metallic, A=roughness. Request `23ddcc6700b34a9d9f13f35eb4696c36` is preview-only raw-roughness evidence and is not the final runtime material proof.
- Canonical export request `3c67ae7d719e42468f73165d29a2ea78`; grounded attack export `37b47e1f1eca4a81b06372869840cdcd`; grounded attack reimport `0299f824d0b7497499e20088d6d97182`.
- All nine actions reimported with grounded first/mid/final samples. See `blender/reports/action_manifest.md` and `validation/reimport_*.json`.

## Audio handoff

Original source URLs, authors, licences, original hashes, transformations, derived hashes, roles, wrapper proposals, and synchronization points are in:

- `audio/evidence/provenance.md`
- `audio/sound_design_handoff.md`

The package contains selection, acknowledgement, two frame-synchronized move footsteps, battle voice, rifle, casing, wounded, and death candidates. Rifle/casing wiring is blocked with the invalid weapon action. Exact voice wording requires parent listening.

## Counter and equipment-art handoff

Required tokens are `GFX_group_clone_infantry_icon`, `GFX_unit_clone_infantry_icon_medium`, `GFX_unit_clone_infantry_icon_medium_white`, and `GFX_archetype_clone_equipment`. The equipment token represents a viable standardized clone cohort/manpower reserve and must show a readable generic clone growth capsule or cohort silhouette, not a rifle or infantry weapon.

Exact counter mapping: `GFX_group_clone_infantry_icon` and `GFX_unit_clone_infantry_icon_medium` both consume the 152x42 large strip; `GFX_unit_clone_infantry_icon_medium_white` consumes the 60x12 map strip. All three counter consumers use `noOfFrames = 2` with normal then schematic frame order.

Installed vanilla references inspected:

- `interface/subuniticons.gfx`.
- `gfx/interface/counters/divisions_large/unit_infantry_icon.dds`: 152x42, two 76x42 frames.
- `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`: 60x12, two 30x12 frames.
- `interface/Technologies.gfx`.
- `gfx/interface/archetypes/archetype_infantry_equipment.dds`: 81x23.
- `gfx/interface/technologies/infantry_equipment_0.dds`: 120x24.
- Matching skill-local families under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/` and `units/equipment/technology_art/`.

Sampled muted green evidence includes RGBA `(73,106,73,255)`, `(74,107,74,255)`, `(83,114,83,255)`, `(100,128,100,255)`, and `(116,141,116,255)`. Final outputs and comparison evidence are recorded in `counter_art/manifest.md`, `counter_art/gfx_handoff.md`, and `counter_art/evidence/contact_sheet.png`. Parent owns all `.gfx` registration and consumer wiring.

Final counter-art selections:

- `counter_art/dds/clone_infantry_large_strip.dds`, 152x42, two 76x42 frames, SHA-256 `ccc3cf926beea92caead6ac54cb8006694b5c1ccf6e957c4ceae63f83f9edde8`.
- `counter_art/dds/clone_infantry_map_strip.dds`, 60x12, two 30x12 frames, SHA-256 `5dd84708accc4cd9ce5e8de3f307eea8a3b64661c1cfb8dca4548750f7f8344b`.
- `counter_art/dds/clone_equipment_archetype.dds`, 81x23, single clone-growth capsule, SHA-256 `21ee953054fe6546b58e242d935f803e879d0c3c1cb15389cccd02791ada6056`.
- `counter_art/dds/clone_equipment_technology.dds`, 120x24, three-capsule cohort bank, SHA-256 `39b356a06d68b05c4baa60dcfe93f3439f821f47ede0d2130672f9ac3ed22adb`.

The earlier rifle-based archetype experiment is rejected source evidence only and is absent from final DDS files and proposed runtime consumers.

## Recovery requiring confirmation

Do not spend recovery credits without user confirmation. The least-risk route is a clean weaponless Meshy 7 humanoid plus a separately attached vanilla-compatible weapon and verified muzzle/cartridge locators. A full fresh provider tranche is estimated at 59 credits (30 generation + 5 rig + 24 actions). A narrower 44-credit tranche (30 + 5 + 9 for attack/support/training) risks incompatible action reuse. A repository-adapter/runtime attachment strategy must be verified before either paid route, because regeneration alone does not solve weapon binding.

## Remaining parent work

- Add and lock the narrow attachment/reorientation/combined-proof adapter operation described in the rifle attachment audit, then fit the verified rifle to recovered `RightHand` and review attack/support/training contact.
- Wire the repaired death candidate only after normal parent-owned runtime review; its source/export/reimport contact evidence now passes.
- Review `counter_art/gfx_handoff.md` and wire the four requested tokens plus the parent-selected technology sprite token.
- Audition the derived voice/audio candidates and select wrappers.
- Register final mesh, material, entity, action, sound, equipment, technology, subunit, localisation, and GFX consumers.
- Synchronize selected job outputs to runtime and record source/runtime hashes.
- Use `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/source_to_runtime_selection.md` as the explicit pre-copy hash ledger.
- Validate the live consumer in game. This worker does not claim in-game completion.

## Simplifications, omissions, and blockers

No static action, renamed vanilla counter, generic placeholder, raw roughness-as-specular map, or unlicensed/generated audio substitute was used. Attack/support-attack weapon semantics, muzzle/cartridge synchronization, exact voice audition, runtime synchronization, runtime wiring, and in-game validation remain incomplete as stated above.

## Recovery completion addendum — 2026-08-06

The user-authorized 59-credit weaponless recovery completed without retry: legacy Meshy task `019fd5c7-4456-74a5-b276-2c2694e5c9bc` cost 30, rig task `019fd5d0-471a-76c3-962a-171f0bb253fe` cost 5, and eight action tasks cost 24. The balance moved from 657 before recovery to 598 after recovery. No paid budget remains.

The clean selected recovery mesh is `export/recovery/mesh/clone_infantry.mesh`, SHA-256 `b45d4eb3c63e9346125b372746113cca7d87687dcf9df1db426a4b247a13c0e6`. It is weaponless, 30,000 triangles, one UV mesh, 24 bones, and reimports through io_pdx_mesh. The provider-added `Icosphere` calibration object was explicitly excluded. Weight transfer covered all 23,520 source vertices; exporter sanitization enforces four influences and normalization. Thirty-eight small boundary edges remain and require review.

The nine recovery actions are under `export/recovery/anim/`. Exact task IDs, frames, hashes, status, adapter requests, and reimport evidence are in `blender/reports/recovery_action_manifest.md` and `blender/reports/recovery_action_pipeline.json`. Death is accepted after a bounded terminal correction; attack, support attack, and training remain withheld pending rifle proof.

Separate-weapon proof was initially partial. Installed vanilla `gfx/entities/units_infantry.asset` attaches right-, left-, root-, and long-idle weapon entities through `Right_Hand_node`, `Left_Hand_node`, `Root_node_2`, and `mid_back_node`, and emits muzzle/cartridge effects from named nodes. The recovered Meshy skeleton exposes `RightHand` and `LeftHand` instead. The rifle asset and its locators were verified in the subsequent attachment audit below; only the body-node bridge, local fitting/reorientation, combined proof, and runtime wiring remain blocked.

The previous fused-rifle GLB/FBX, mesh, actions, previews, reports, and hashes remain preserved under their original paths as rejected evidence. Audio and bespoke counter packages are reused without modification. No gameplay, GFX, entity, sound-definition, localisation, or runtime file was edited.

## Rifle attachment audit addendum — 2026-08-06

This addendum supersedes the earlier statement that a rifle asset and rifle-side locators were absent. The installed British infantry rifle package is now verified and preserved:

- `blender/reference/ENG_weapon_rifle.mesh`, SHA-256 `6cf9711a575dc72a5ce8f796fd04f9cac30c134db7d48aeded36cb4b07acd485`.
- `blender/reference/ENG_infantry_diffuse.dds`, SHA-256 `95f45d8db078aaaf620a99443a7edac2e76dd36d6f2039b0fbcf92f397f4979d`.
- `blender/reference/ENG_infantry_spec.dds`, SHA-256 `623a5ed117c22002fa80e81215be4997c0ae76403de62361ec895a2c07a7e871`.
- `blender/reference/ENG_infantry_normal.dds`, SHA-256 `b6b66489afaaf315d7472402f372e70e799314f44c32767376a7edbb1b5c728f`.

Adapter reimport request `fc80503271484c488ce6cfd55730c7da` produced `blender/checkpoints/reimport_vanilla_ENG_weapon_rifle.blend`, SHA-256 `3b9243f43f4ecc49538703aa3113e0eb34daeb2eebb61b1e7837d134f93214a9`. Metadata request `40356ca2d13c44168572c5be3c059ab2` verifies a 409-triangle rifle, local `-Y` barrel direction, `muzzle` at `[0.0, -3.429081, 0.286201]`, and `cartridge` at `[0.0, -0.108757, 0.434303]`. The matching installed entity is `ENG_infantry_weapon_rifle_right_entity`, with the left and long-idle variants in installed `gfx/entities/units_infantry.asset`.

Direct entity attachment to recovered `RightHand` is syntactically plausible, but it is not visually accepted. Locked adapter 1.2.2 adds `retime_animation_action`, `offset_action_root`, and `sanitize_runtime_candidate` to the earlier operation set, but it still has no second-mesh import/attachment, bone-parenting, bounded weapon transform/reorientation, helper-node mutation, locator hierarchy preservation, or combined body-and-weapon proof rendering. `prepare_candidate` is not a valid substitute: it normalizes a full candidate against profile scale and does not preserve and reorient this rifle as an animated attachment or parent it to `RightHand`. Unrestricted Blender Python is forbidden.

Exact blocker evidence and the smallest proposed adapter extension are in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/recovery_rifle_attachment_adapter_blocker.md`. Attack, support attack, and training remain blocked; their files are retained as candidates and must not be wired as accepted actions. Death is accepted. No additional Meshy operation was called, so recovery spend remains exactly 59/59 credits and the last observed balance remains 598.

Current dependency evidence: `dependencies.lock.json` SHA-256 `39d3f78c5473ccc72783af1876de088653b32d8d0c64a50771821c944ff4770e`, Meshy schema lock SHA-256 `dbb9cad7fb12afe81eca05a2f381ef4251c035f4d22bf17856a2f6d41f16a62d`, and adapter config SHA-256 `519fdc14260828c7ccc48a50b4840a7833df20702cec145242143c201e40b6f6`.

Adapter 1.2.2 death repair evidence: bounded offset request `49af0170e1fe4b918ac7577fa5d47a50`, canonical export request `779f5cbc58a345b3b69fd8f9624786e7`, canonical reimport request `eb141253317e40f988bd834c71892f54`, final death SHA-256 `f2732e4e5d0eb4a4d31dc0de689955ef1f4e1b45c4dca7a0482f2302bf36f285`, and frame-73 ground contact `Z=0.0000447035`.

Consumer boundary: normal clone formations and Kruger formations using the `clone_infantry` subunit are intended to consume this generic package. Mengele Aryan clone formations intentionally retain the normal German infantry model/entity/sprite family and must not be redirected to `clone_infantry_mesh` or `clone_infantry_entity`.

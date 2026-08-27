# Clone infantry recovery audit handoff — 2026-08-27

Status: `blocked_fail_closed`

Owner: `chaosx_3d_model_pipeline`

Asset: `clone_infantry`

Deterministic job root: `docs/assets/shared_clone_system/models_3d/clone_infantry`

## Outcome

The existing generic clone infantry package cannot satisfy the requested firearm animation package without changing its geometry or attachment/weighting strategy.

The preserved weapon-bearing mesh keeps its rifle fused upright to the clone's back during every provider action, including attack and support attack.

The separate recovery mesh has clean provider actions but deliberately contains no rifle.

No paid Meshy call, new generation, ImageGen call, Blender mutation, manual attachment, manual weighting, locally authored skeletal motion, semantic alias, or transform-only substitute was performed in this audit.

Live Meshy balance was 13 credits, and the parent explicitly prohibited paid calls.

Estimated and consumed credits for this audit are therefore both 0.

The package remains unwired and must not be represented as a complete firearm infantry model.

## Files created or refreshed by this audit

- Created this handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_clone_infantry_recovery_audit_handoff.md`.
- Refreshed `.tools/3d_pipeline/reports/environment_report.json` through the repository verifier; the report records the current locks, tools, route probe, and 13-credit balance.

No model, animation, texture, audio, counter, gameplay, entity, GFX, or sound-definition file was changed.

## Required reading and references

This audit applied `AGENTS.md`, `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline Paradox wiki core pages were consulted together with the graphical asset and entity pages.

Installed vanilla documentation was searched for model, entity, animation, and audio guidance.

The relevant runtime precedents were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, and the installed vanilla infantry counter DDS files listed below.

Vanilla rifle attack states attach muzzle and cartridge events to named `muzzle` and `cartridge` nodes.

Representative vanilla timings in `units_infantry.asset` are muzzle discharge at 1.15 seconds and cartridge ejection at 2.2 seconds, with alternate attack states using muzzle discharge at 0 and cartridge ejection at 1.2 seconds.

The clone package has no accepted hand-held rifle alignment or animated muzzle/contact proof to support equivalent events.

## Current dependency and route verification

`python .tools/3d_pipeline/verify_environment.py --probe-meshy` completed with `hard_gate = passed` and no findings.

The resulting evidence is `.tools/3d_pipeline/reports/environment_report.json`, current SHA-256 `8ab8a91bed9ad3aac98170ca684278d70cab6f5e87c28164244bbe6ee5e94724`.

| Dependency or route | Verified value |
|---|---|
| Official Meshy MCP | `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346` |
| Meshy compatibility route | revision `meshy-7-v5`, exact image model identifier `meshy-7` |
| Meshy tools | `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate` verified present |
| MCP SDK | `@modelcontextprotocol/sdk` `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32` |
| Blender adapter | `chaosx_blender_hoi4` `1.10.14` |
| Blender | `5.1.2`, build commit `ec6e62d40fa9` |
| Blender bridge | `127.0.0.1:9876`, verified by the environment probe |
| `io_pdx_mesh` | `0.91.0`, archive SHA-256 `a683df08318cb700014c7fe9a3d15139e5fb2313c7e98715204263e48931f7c2` |
| Live Meshy balance | 13 credits |

Current configuration checksums are:

- `.tools/3d_pipeline/config/dependencies.lock.json`: `c27768297fb7ad5acc9c555e7c83dc77856908e2c628bf16d9a420095c64266a`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: `e45fe80f3b8ac49a365ea2d4221e82e969ae55279639f817bb6fa75407d1c233`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: `4bc97ca0b07580f5aa04b49e7b9fbd1c07ec88df5c4d56cd3ba8846e630117ab`.

The existing package manifest records obsolete adapter and lock values from its 2026-08-05/06 production run.

Those historical values remain valid provenance for the old exports, but they are not the current verified dependency state and must not be copied into a new completion claim.

## Source and provider lineage

No reference image was generated, edited, selected, or sent to a provider during this audit.

The existing package has these historical source lineages:

| Lineage | Reference and hash | Provider task and result | Status under this audit |
|---|---|---|---|
| Original weapon-bearing candidate | `refs/original/meshy_input.png`, SHA-256 `adfe9bf039975e6048daf64d06c2aa45562adbb96c1074330d04bb3293db5981` | Meshy 6 image-to-3D task `019fd2f4-8ffa-7c67-8c2d-cfc3503f6f9c`; downloaded GLB `provider/downloads/clone_infantry_meshy6.glb`, SHA-256 `e36b1c816da15d4d09b739e8a40d8cb05bf53f06bba0f96a4bac7c7333f4760d` | Rejected for fused rifle/contact failure |
| Weapon-bearing rig | inherited original reference | rig task `019fd311-4488-7174-905a-ae7b87d7e378`; `provider/downloads/rigged_character.glb`, SHA-256 `07e1fff3ae1c2ea2393c2b56871e79dac7f402cc316ca3a7f8d13314127738c9` | Historical provider rig only |
| Weaponless recovery | `refs/recovery/meshy_input_weaponless.png`, SHA-256 `36b33b93531230a859a7f2b2c0c5f7c4f96e1e85600848280d12a45de887c4bc` | Meshy 6 generation task `019fd5c7-4456-74a5-b276-2c2694e5c9bc`; rig task `019fd5d0-471a-76c3-962a-171f0bb253fe` | Excluded because the current scope requires preservation of the firearm |

The existing `refs/original/input_manifest.json` records user authorization for its agent-generated reference.

There is no Internet artwork source or source-to-ImageGen refinement in this audit because the parent restricted work to the existing package and prohibited new generation.

The model geometry is historical Meshy 6 output, not Meshy 7 output.

The current schema verifies Meshy 7 only for new image-to-3D work; it cannot retroactively change the provenance of these files.

## Geometry, material, rig, and export evidence

The weapon-bearing canonical export is `export/mesh/clone_infantry.mesh`, SHA-256 `7b172ca905b870aeeb3fbd46302b8b4722c6b82990369467fc8049bc2a2f5f3f`.

It retains the rifle geometry, but the rifle remains fused to the back and does not establish a hand, muzzle, or cartridge relationship in the required attack motions.

The visual evidence is `blender/previews/clone_infantry_candidate_three_quarter.png` and `blender/previews/clone_infantry_attack_three_quarter.png`.

The weaponless recovery export is `export/recovery/mesh/clone_infantry.mesh`, SHA-256 `b45d4eb3c63e9346125b372746113cca7d87687dcf9df1db426a4b247a13c0e6`.

The visual evidence is `blender/previews/clone_infantry_recovery_candidate_three_quarter.png` and `blender/previews/clone_infantry_recovery_attack_three_quarter.png`.

The recovery mesh cannot be selected because it omits the required firearm.

The existing geometry reports record a calibrated source height of `7.3518242835`, one application of entity scale `0.8`, and effective runtime height `5.8814594268`, with forward `-Y`, up `+Z`, and ground contact at Z=0 against the installed western European infantry precedent.

The existing weapon-bearing geometry report records 29,999 triangles, 14,991 welded vertices, zero degenerate faces, zero non-manifold edges, one UV map, a 24-bone rig, and no zero-weight deforming vertices before export.

The existing PDX material package uses `PdxMeshAdvanced` with 1024x1024 diffuse, packed specular, and packed normal DDS files.

These geometry and material properties do not resolve the firearm contact failure.

No Blender inspection, mutation, export, or reimport request was issued during this audit because the existing immutable previews and reimport records already prove the upstream geometry/skin blocker, and none of the currently permitted cleanup operations can change that relationship.

## Provider-authored action disposition

All listed files are substantive multi-frame Meshy provider actions processed by the historical locked adapter at 24 FPS.

No action was replaced with an alias or locally authored motion.

Accepted below means only that the historical action remains a usable non-firearm candidate on the weapon-bearing mesh; it does not make the blocked package complete.

| Required role | Provider lineage | Frames and policy | Export and SHA-256 | Disposition |
|---|---|---|---|---|
| idle | task `019fd319-eb08-7492-b45b-c6e4fad2955e`, action 0 | 0-97, loop, in place | `export/anim/clone_infantry_idle.anim`, `ed34a20238f33873c5eb95bf58bb8df155a23fc8d0c01d7ee93f221d260bb221` | Existing candidate accepted |
| move | free walking action from rig task `019fd311-4488-7174-905a-ae7b87d7e378` | 0-26, loop, in place | `export/anim/clone_infantry_move.anim`, `c6b1a14280127d80431ab75e0a09949436eae92b0a1ca867092b928616febcef` | Existing locomotion candidate accepted |
| attack | task `019fd319-eee0-75b3-8745-66feade8bcac`, action 4 | 0-68, attack loop, in place | `export/anim/clone_infantry_attack.anim`, `b260fef3e763ec8bee69ec961a58aa6fbfff1b3db00e410eca314af3d4c0c228` | Blocked and rejected; empty-hand attack while rifle stays on back; no genuine aim, discharge, recoil, or recovery with the firearm |
| defend | task `019fd319-f129-75b4-8961-c8a0ad9e3732`, action 138 | 0-84, loop, in place | `export/anim/clone_infantry_defend.anim`, `bbb2dd078a6a15dc0803bf629195525a0c15709eb8e69bc0ac6e957c94097d76` | Existing non-firearm candidate accepted |
| support attack | task `019fd319-f33a-7fa7-9bb2-9f338fff39be`, action 98 | 0-17, support loop, in place | `export/anim/clone_infantry_support_attack.anim`, `aef9b6577f2b270906784d0c3fbbcd51133d6fd0b062031f8a82d88dbcd95a06` | Blocked and rejected; invisible-weapon pose while rifle stays on back |
| retreat | task `019fd319-f515-7fa8-a989-402f6bca122e`, action 20 | 0-43, loop, in place | `export/anim/clone_infantry_retreat.anim`, `79b67ae5edcac038814499f06556cfb9b15d2c7ad76b318e871c1dcb93bb8e59` | Existing locomotion candidate accepted with no firearm-discharge claim |
| training | task `019fd319-f73b-75b5-9e0d-d35aeea4fa28`, action 89 | 0-41, loop, in place | `export/anim/clone_infantry_training.anim`, `c7e9a83d1fe21038999917824b064b1fc0a300c89876989c0114a2fb0816e609` | Blocked; combat stance does not handle or train with the required rifle |
| wounded | task `019fd319-f984-7399-9e0d-254d91fdc1f7`, action 177 | 0-73, one shot, in place | `export/anim/clone_infantry_wounded.anim`, `f8ced4bbec3087325ffba44acb8e06eda3234c7edfbf882081ff85d408b6f36d` | Existing articulated reaction candidate accepted |
| death | task `019fd319-fbf1-75b7-8e8a-a92a6c7946e3`, action 8 | 0-72, one shot and hold final frame | `export/anim/clone_infantry_death.anim`, `dbc4748165dd6e11cb7c8ccaccf4cf67ba92ac0bce91f6eb5a1a84eea5a342ad` | Existing articulated collapse/settling candidate accepted |

The existing reimport request IDs are `b0f31410b3bf406186acc720c4d48296`, `b23d22d837ee42fa83f036562f120741`, `0299f824d0b7497499e20088d6d97182`, `e61e81d986c84f34a26755a395322eba`, `78c0be26f19148e8966c44b0c36a2624`, `2b396414f7e046f587795d3d013464f4`, `66d20a277721413ab198f3c673f34a29`, `5239bc6b1306495b812e24b53582164d`, and `57f6ad6bad83443fb085677e899ee3e0` in the same role order.

The weaponless recovery actions also have complete Meshy task/export/reimport evidence in `blender/reports/recovery_action_manifest.md`, but selecting them would violate the current preserve-firearm requirement.

In particular, its attack, support attack, and training files are explicitly blocked in that manifest because they have no combined rifle/contact proof.

## Why provider animation alone cannot repair this package

`meshy_animate` supplies skeletal motion to the existing rig.

It cannot turn back-skinned rifle vertices into a hand-held rigid weapon, author a separate rifle attachment hierarchy, or add accepted hand/muzzle/cartridge relationships to the immutable mesh.

Any local correction that changed this relationship would require attachment, weighting, or substantive geometry/rig work that the parent explicitly prohibited.

A new provider action could therefore produce a different body gesture but would still leave the rifle on the back.

The only honest disposition is fail-closed.

## Sourced audio audit

The original downloads and their hashes match `audio/evidence/provenance.md`.

No new audio was downloaded or transformed during this audit.

| Roles | Source page, author, and license | Original hash | Audit disposition |
|---|---|---|---|
| selection, acknowledgement, battle voice, wounded voice | `https://opengameart.org/content/soldier-voice-acting`, kurt, CC BY 3.0 | `soldierintro.ogg` `efa2b3029430e7cbcd56cebfbbe189558673d5feea8fe0021204f58967297640`; `unitselection.ogg` `08038defe513e49cf00c1a15c6eb6926ed82a2b8aaae62af031a2b9fc1670b2d`; `acknowledgement.ogg` `3a0eb82f860d6ef65864197e7f95d2503fb21c1f3ef4348d4592663ae2ccdee9`; `battlecries.ogg` `26fbe5af927786b854389e5ba6d2e04d0283f95e47aa16214a1d82943ba9db74`; `wounded.ogg` `eeb48bd1abee14052941df29fe93b660df4a811998146616f5d6eaa138484ee6` | Legally usable with attribution; exact spoken wording and role fit remain `needs_user_review` |
| death and pain | `https://opengameart.org/content/grunts-male-death-and-pain`, thebardofblasphemy, CC0 | `death_pain_grunts.wav` `3f00fba827f20ff9ccea1bc07d2c21ab8d3a36e81b48a6005cf8459f02779586` | Legally usable candidate; parent must select the exact death/wound event |
| marching and steps | `https://bigsoundbank.com/marching-in-1-s3023.html`, Joseph SARDIN, CC0/public-domain equivalent | `marching_boots.wav` `4fb97dbd1fc20ecd2c806569f539b3ef1cb632935497489ff13fbef7e55b689c` | Legally usable candidate for move/retreat contacts |
| cartridge | `https://bigsoundbank.com/douille-de-7-62mm-sur-beton-1-s1367.html`, Joseph SARDIN, CC0/public-domain equivalent | `cartridge_762_concrete.wav` `32b91f41785d61b68a5174a231314d8912c7065f263bd13ff30260dbd7f770df` | Legally usable, but synchronization is blocked because there is no valid firearm discharge/ejection action |
| rifle discharge | `https://commons.wikimedia.org/wiki/File:Gunshots_8.ogg`, aradlaw, public-domain dedication | `gunshots_8.ogg` `0107c3a14e256c2a4c2e94f7494df6994edba75f4de05fced2d8900cf19b4c0b` | Rejected: the source page identifies it as simulated/synthesized in Audacity, which violates the no-synthesized-audio rule even though its license is permissive |
| bullet impact | none | none | Blocked; no defensible sourced file exists in the package |

All existing derived candidates are mono Vorbis OGG at 48 kHz.

Their final hashes are recorded in `audio/sound_design_handoff.md`; spot verification reproduced, among others, selection `1def8eeffbb9daf93046d19ba6322f9bb6490e4d64ddb4a851cf6586b460f336`, acknowledgement `cb319bc7ace81865b7b7b6480d5569c028395c2b593e8310e7ddadc4423ce467`, rifle `99bd04b69e6d05c9f05ae852569a68cc9a1e4a6a2d706945b15525422f8c2fa4`, casing `74c4c657d67372492b2c2a29e74b0f288e213c0f82e095c3affc65f9549e995c`, movement `ec71b5795ea680f07c28996d7c513d51a67ca619a894aafb50d534453ac4f470`, wounded `701cfe05fcc8693808a78e92d6896e722579093ec7b6787c15031d7d18c4c791`, and death `67a96a9d3538433e108e8fd0951f037c9823982504c753da12d5ef9693781471`.

The current 3D pipeline voice-processing default is PCM signed 16-bit WAV at 44.1 kHz mono.

The existing selection, acknowledgement, and battle-voice OGG files therefore remain candidates rather than approved game-ready voice files under the current workflow.

No audio role is wired, and attack/casing synchronization must remain absent while the firearm action is blocked.

## Bespoke vanilla-green counter evidence

The generic clone counter package is present and its current hashes match `counter_art/manifest.md`.

The separate `counter_art/aryan_clone_infantry` family is outside this generic package and must not be substituted for it.

| Consumer/token proposal | Selected file | Canvas and states | SHA-256 |
|---|---|---|---|
| `GFX_group_clone_infantry_icon` and `GFX_unit_clone_infantry_icon_medium` | `counter_art/dds/clone_infantry_large_strip.dds` | 152x42, two 76x42 frames, normal olive then white schematic | `ccc3cf926beea92caead6ac54cb8006694b5c1ccf6e957c4ceae63f83f9edde8` |
| `GFX_unit_clone_infantry_icon_medium_white` | `counter_art/dds/clone_infantry_map_strip.dds` | 60x12, two 30x12 frames, normal muted then white schematic | `5dd84708accc4cd9ce5e8de3f307eea8a3b64661c1cfb8dca4548750f7f8344b` |
| clone equipment archetype proposal | `counter_art/dds/clone_equipment_archetype.dds` | 81x23, one frame | `21ee953054fe6546b58e242d935f803e879d0c3c1cb15389cccd02791ada6056` |
| parent-selected clone technology token | `counter_art/dds/clone_equipment_technology.dds` | 120x24, one frame | `39b356a06d68b05c4baa60dcfe93f3439f821f47ede0d2130672f9ac3ed22adb` |

The inspected installed-vanilla definitions and DDS precedents are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

The matching repository reference family is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/`.

Recorded vanilla-green samples are RGBA `(73,106,73,255)`, `(74,107,74,255)`, `(83,114,83,255)`, `(100,128,100,255)`, and `(116,141,116,255)`.

Original source PNGs, frame-aware processed PNGs, DDS decode round trips, and the comparison sheet are present under `counter_art/`.

The comparison sheet is `counter_art/evidence/contact_sheet.png`, SHA-256 `56dc3cc87ac7eead0961294230e127c010d483c92c83997e929bd2aa175965f1`.

Counter art is complete for parent review and wiring, but no destination/runtime copy hash exists because this worker did not edit GFX or runtime assets.

## Requirement-to-runtime status

| Requirement | Status | Runtime implication |
|---|---|---|
| Preserve clone identity and firearm geometry | Partially present, but invalidly fused to the back | Do not select a firearm entity from this package |
| idle | Existing provider candidate | May be proposed only if a later accepted mesh/weapon strategy preserves the same skeleton |
| move | Existing provider candidate | Same restriction |
| attack with aim/discharge/recoil/recovery | Blocked | No `clone_infantry_attack` binding, muzzle event, rifle sound, or casing event |
| defend | Existing provider candidate | Same skeleton restriction |
| support attack | Blocked | No `clone_infantry_support_attack` binding or firearm events |
| retreat | Existing provider candidate | Same skeleton restriction |
| training | Blocked | No `clone_infantry_training` binding |
| wounded | Existing provider candidate | Same skeleton restriction |
| articulated death | Existing provider candidate | Same skeleton restriction |
| sourced selection/acknowledgement/voice | Needs user review and current-format processing | No voice binding |
| sourced rifle discharge | Blocked | Existing candidate is synthesized and rejected |
| sourced impact | Blocked | No candidate |
| bespoke counters | Complete for parent review/wiring | Parent copies DDS files and registers exact consumers |
| entity, GFX, sound definition, and gameplay wiring | Parent-owned and intentionally absent | No in-game completion claim |

Proposed stable identifiers remain `clone_infantry_mesh`, `clone_infantry_entity`, `clone_infantry_idle`, `clone_infantry_move`, `clone_infantry_defend`, `clone_infantry_retreat`, `clone_infantry_wounded`, and `clone_infantry_death`.

They are proposals only and must not be registered against the rejected weapon-bearing candidate as a completed firearm unit.

## Meaningful validation performed

- Re-ran the repository dependency and live route verifier with a Meshy schema/balance probe.
- Visually compared the weapon-bearing candidate and attack previews with the weaponless recovery candidate and attack previews.
- Recomputed SHA-256 values for the exported mesh/action files, audio originals and derivatives, and final counter DDS files.
- Probed every derived audio candidate and confirmed Vorbis, mono, 48 kHz encoding.
- Rechecked the recorded source pages and licensing basis for the existing audio package; the gunshot source's synthesized origin changes its disposition from legally usable to workflow-rejected.
- Inspected the installed vanilla infantry entity attack event structure and the exact large/map counter definitions and DDS family recorded by the package.
- Reconciled the historical package dependency claims against the current verified locks instead of treating the old adapter/schema values as current.

## Validation not performed

- No paid provider task was created, retried, or queried beyond the allowed balance/schema probe.
- No Blender mutation, re-export, or new reimport was attempted because allowed cleanup cannot repair the weapon skin/attachment relationship.
- No new professional animation source was authorized or supplied.
- No new rifle discharge or impact audio was sourced because the parent restricted this tranche to audit/handoff completion.
- No GFX, entity, sound, equipment, subunit, technology, localisation, or gameplay file was edited.
- No in-game consumer validation was performed; it remains parent/user-owned.

## Parent work and unblock conditions

The package can be reconsidered only after the user authorizes a materially different geometry/attachment route or supplies an explicitly approved professional source package that includes a hand-held, locator-complete rifle relationship compatible with the clone skeleton.

Simply purchasing another Meshy action is not an unblock because it will not change how the existing rifle geometry is attached or weighted.

If an acceptable geometry/rig strategy is later authorized, every downstream action must be revalidated against the final skeleton, and attack/support/training must show two-hand contact plus genuine aim, discharge, recoil, recovery, muzzle alignment, and cartridge alignment.

The parent must then source a non-synthesized, clearly licensed firearm recording and a defensible impact recording, mechanically process the selected voice files to the approved consumer format, copy counter DDS files with source/destination checksum equality, perform all GFX/entity/sound/gameplay wiring, and validate the live consumer.

## Simplifications, omissions, and blockers

No fallback or simplification was used.

The omitted firearm actions and audio roles are explicit fail-closed blockers, not substituted content.

The existing model is historical Meshy 6 geometry, the firearm remains fused to the back, the weaponless recovery violates the preserve-firearm requirement, attack/support/training lack valid weapon semantics, the rifle sound source is synthesized and rejected, bullet-impact audio is absent, the voice derivatives need semantic review/current-format processing, and runtime wiring remains intentionally parent-owned.

Because these blockers are unresolved, this audit is intentionally not a completion claim and no Git commit was created for the blocked package.

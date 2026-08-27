# Alien infantry V13 recovery audit handoff — 2026-08-27

Status: `blocked_fail_closed`

Owner: `chaosx_3d_model_pipeline`

Asset: `alien_infantry`

Deterministic job root: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry`

## Outcome

The accepted V13 Meshy 7 model, rig, seven provider-authored actions, PDX exports, integrated cyan-tipped ray pistol, material package, and runtime copies remain the best valid generic alien infantry package.

The seven accepted action roles are idle, move, laser attack, defend, support attack, retreat, and articulated death.

The current runtime additionally maps `training` to the idle animation and `wounded` to the defend animation.

Those mappings are semantic aliases and violate the required no-alias rule.

Training cannot safely be removed on the evidence available because installed vanilla infantry entities expose genuine training states and distinct training animations.

Wounded is not a stock vanilla infantry state, and a repository search found no gameplay or entity requester outside the custom alien/clone asset packages, so the parent may remove the alien wounded state rather than purchase a provider reaction action.

This worker did not edit the parent-owned runtime files.

One provider-authored training recovery was attempted against the existing V13 rig with Meshy action 326 `jumping_jacks`.

Meshy returned `Resource not found` before creating an animation task because rig task `01a03dcf-f0ba-7b67-b769-5a2678b03a40` has aged out of the live provider endpoint.

A free task-status query independently returned `Task 01a03dcf-f0ba-7b67-b769-5a2678b03a40 not found on any endpoint.`

The live balance remained 13 credits, so the failed request consumed 0 credits.

No wounded request was submitted.

After the parent reserved up to 6 credits for the portal work, no further paid call was made.

The live `meshy_rig` route accepts a provider task id or provider-accessible model URL, not a local GLB/FBX path, and this package preserves no approved live provider URL for the rig.

Accordingly, distinct training and wounded actions are blocked until a provider-supported re-rig/upload route and sufficient coordinated balance exist, or the parent removes a state that is demonstrably unnecessary.

No new base model, ImageGen call, image-to-3D call, remesh, retexture, re-rig, animation artifact, manual attachment, manual weighting, locally authored motion, procedural motion, transform-only substitute, gameplay edit, entity edit, GFX edit, or sound-definition edit was made.

## Files created or restored by this audit

- Created this handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_alien_infantry_v13_recovery_audit_handoff.md`.
- Restored the already-approved immutable sourced-audio originals under `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/` from the recorded direct-download URLs.
- Restored byte-identical evidence copies of the already-approved derived audio under `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/derived/` from the runtime WAV files.
- Refreshed `.tools/3d_pipeline/reports/environment_report.json` through the repository verifier; its current SHA-256 is `8AB8A91BED9AD3AAC98170CA684278D70CAB6F5E87C28164244BBE6EE5E94724`.

The audio evidence roots are intentionally ignored by the repository-wide `docs/assets/` rule, but the files are present locally with exact provenance hashes recorded below.

## Required reading and references

This audit applied `AGENTS.md`, `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline Paradox wiki core pages were consulted together with Graphical asset modding, Entity modding, Unit modding, and Division modding.

Installed vanilla documentation was consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.

The exact model/entity precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`.

The installed vanilla infantry entity defines distinct `training`, `jumping_jacks`, `pushup`, `guard_rifle`, and `aim_exercise` animations for the training state.

No `wounded` state was found in installed vanilla `gfx/entities/`, and no active alien-infantry wounded requester was found elsewhere in the repository.

The exact counter precedents are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

## Current dependency and route verification

`python .tools/3d_pipeline/verify_environment.py --probe-meshy` completed with no findings and recorded the 13-credit balance.

The Blender adapter health request was `e62f73ddef65470f89183261fbc6bac6`.

| Dependency or route | Verified value |
|---|---|
| Official Meshy MCP | `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346` |
| Meshy compatibility route | revision `meshy-7-v5`, exact image model identifier `meshy-7` |
| Meshy MCP SDK | `@modelcontextprotocol/sdk` `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32` |
| Verified Meshy tools | `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate` |
| Blender adapter | `chaosx_blender_hoi4` `1.10.14` |
| Blender | `5.1.2`, build commit `ec6e62d40fa9` |
| Blender bridge | `127.0.0.1:9876`, listening |
| `io_pdx_mesh` | `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2` |
| Live Meshy balance before and after failed request | 13 credits |

Current configuration checksums are:

- `.tools/3d_pipeline/config/dependencies.lock.json`: `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.

## Source and provider lineage

No reference image was generated, edited, or submitted during this audit.

The reused input is `refs/original/meshy_input_v13_tpose_right_pointing_colored.png`, SHA-256 `2D72EEB020C8989B463F214D4B5FC1C29C4AB313AEEE9F033B71E6DE1881BF3A`.

Its recorded source mode is `user_supplied_approved_exact_input`.

There is no Internet-artwork source, source-to-ImageGen refinement, refinement prompt, or refined checksum because the parent expressly restricted this recovery to the accepted existing model and prohibited a new base model and ImageGen/image-to-3D.

The source remains non-shipping evidence.

Historical V13 provider lineage is:

| Operation | Task id | Credits | Disposition |
|---|---|---:|---|
| Rejected Meshy 7 generation | `01a03dbc-7913-7257-961a-56dea6cf6b04` | 30 | Rejected because the provider omitted the firearm |
| Accepted Meshy 7 generation | `01a03dc3-905a-7d02-aba6-05500f877b97` | 30 | Accepted integrated cyan-tipped right-hand ray pistol |
| Triangular remesh | `01a03dc9-8951-79ad-bc08-ae94ad607dfe` | 5 | Accepted; provider target 100,000 triangles, runtime working duplicate 59,999 |
| Humanoid rig | `01a03dcf-f0ba-7b67-b769-5a2678b03a40` | 5 | Accepted historical 24-bone rig; live endpoint now reports not found |
| Seven provider actions | task ids below | 21 | Accepted historical action package |

Historical V13 consumption was 91 credits from a balance of 103.

This recovery estimated up to 3 credits for one training action but consumed 0 because the provider rejected the expired rig id before task creation.

## Geometry, material, rig, weights, and export evidence

The accepted source geometry height is `7.3518023491`, compared with installed vanilla source height `7.3518242835`.

The runtime entity scale is `0.8` exactly once, producing the vanilla effective height `5.8814594268`.

The accepted axes are forward `-Y`, up `+Z`, with grounded contact.

The final mesh has 59,999 triangles, 59,451 exported vertices, 30,035 position-welded source positions, one UV layer, zero degenerate faces, zero negative-scale objects, and no zero-length normals in reimport evidence.

The ray pistol is fused to the provider mesh and remains present in every accepted action.

No separate weapon object, manual parenting, constraint, weight repair, or identity-changing geometry operation was used.

Fresh adapter inspection of `blender/checkpoints/reimport_revalidation_2026_08_26_laser_attack.blend` returned request `c78a90b536ca4ee9991e059e6c73f913`.

It found one armature `io_pdx_rig`, one mesh `char1.002`, normalized weights, zero zero-weight deforming vertices, no more than four influences per vertex, and exactly 24 pose bones.

The bones are `Hips`, `LeftUpLeg`, `LeftLeg`, `LeftFoot`, `LeftToeBase`, `RightUpLeg`, `RightLeg`, `RightFoot`, `RightToeBase`, `Spine02`, `Spine01`, `Spine`, `LeftShoulder`, `LeftArm`, `LeftForeArm`, `LeftHand`, `RightShoulder`, `RightArm`, `RightForeArm`, `RightHand`, `neck`, `Head`, `head_end`, and `headfront`.

There is no muzzle, weapon, effect, or locator bone or object.

The locked Blender adapter exposes no locator-creation operation.

Therefore the cyan muzzle cap is a visual synchronization point only and does not justify inventing a positional engine node.

The accepted PDX material package uses the preserved 1024x1024 diffuse, normal, and specular maps.

The source exports and runtime copies are byte-identical:

| Runtime artifact | Bytes | SHA-256 |
|---|---:|---|
| `alien_infantry.mesh` | 5,478,802 | `D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342` |
| `alien_infantry_idle.anim` | 95,059 | `D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF` |
| `alien_infantry_move.anim` | 30,547 | `727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F` |
| `alien_infantry_laser_attack.anim` | 183,379 | `288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0` |
| `alien_infantry_defend.anim` | 41,299 | `F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73` |
| `alien_infantry_support_attack.anim` | 78,163 | `DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061` |
| `alien_infantry_retreat.anim` | 25,939 | `DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC` |
| `alien_infantry_death.anim` | 83,539 | `D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0` |
| `alien_infantry_diffuse.dds` | 4,194,432 | `0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA` |
| `alien_infantry_normal.dds` | 4,194,432 | `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39` |
| `alien_infantry_specular.dds` | 4,194,432 | `5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D` |

## Provider-authored actions and synchronization evidence

Every accepted action retains substantive Meshy motion at 30 FPS and received only adapter-permitted import, per-frame root-Z grounding correction, export, and reimport processing.

Blender authored no replacement motion.

| Role | Meshy action and task | Frames | Export disposition |
|---|---|---:|---|
| idle | 0 `Idle`, `01a03dd1-23a5-7728-9c09-f09683d64ffe`, source FBX SHA `AB6C219F928734095BA516F138EEAE87DD8C7B2E47E34AB325211A00FF9785FF` | 121 | Genuine breathing/body motion; loop candidate; grounded and weapon retained |
| move | 692 `walking_2_inplace`, `01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01`, SHA `338B65DAEF2C9927BC94FFA1F27790963D7B22046F835982885142BE17C1EBE8` | 37 | Distinct in-place walk; loop; grounded contacts and weapon retained |
| laser attack | 223 `Draw_and_Shoot_from_Back_1`, `01a03dd1-2d74-70b2-a151-e8d98c82e4de`, SHA `5CB8EA5140D6F43222527695EB5F1658D5D258641DCD6B2677FC5C0ED4340996` | 236 | Genuine draw, two-hand aim/support, discharge, recoil, recovery, and return to rest |
| defend | 89 `Combat_Stance`, `01a03dd1-31cc-7729-9612-26eb8f7d44c3`, SHA `EFD7DAEC817A565ABD2E0D8967C374D2CC28EDA705CFF555EF5345995ADC364B` | 51 | Distinct defensive stance motion with weapon retained |
| support attack | 234 `Walk_Forward_While_Shooting`, `01a03dd1-35e5-7f37-a601-70982bdf5f74`, SHA `1BDBD13EEC79F53F6A9779178DD2708AFBBF6EED056BFC9309DE69287EB8F733` | 99 | Genuine advancing fire, aiming, and recoil with weapon retained |
| retreat | 685 `Walk_Backward_with_Gun_inplace`, `01a03dd1-3a02-7f38-8f3c-0236be3dc57e`, SHA `5FC3937B5410B661A75F9CB9AD11E47F10A5A7CD7DC827859CA2A86B252C0ABA` | 31 | Distinct grounded in-place backward motion; loop and weapon retained |
| death | 183 `Shot_and_Fall_Backward`, `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4`, SHA `7A4C9264704E2CCF9CFD831AC3798D985C9FB42EAF63A72D0D401EE9397642C5` | 106 | Genuine hit, articulated backward collapse, impact, and settled pose |
| training | proposed 326 `jumping_jacks`; no task created | none | Blocked: existing provider rig id is no longer present on any live endpoint |
| wounded/reaction | proposed 177 `Gunshot_Reaction`; not submitted | none | Blocked unless parent retains this non-stock custom state and a valid provider route/budget becomes available |

Final accepted-action reimport request ids are `135501327e2d41eeaa6d02288a590442`, `16b2e84c426e4f87b952e032513e5be1`, `d0a7b69a74d34f8d90a45fbbf74f3c66`, `0170c12bab23470e9179cb26756cd561`, `1f55f798bb714cedbb2c0857dc178e64`, `4c8c301143e440b3a9029c2f12dc892f`, and `24ff4f5352654a11b4d66ea73b57ae98` in the seven-role order above.

The 2026-08-26 locked-adapter revalidation request ids are `14f0da7ee55c42d6b156cf830afa3dbd`, `494d325dd20d4d649f2b40cc40fdfe26`, `557e9557048540f4bba7cd975989d21d`, `dfbb5f5300c84133ab6ce3b41af1ead9`, `2b1f46f9e6984a158342add202ba8dbc`, `d25ea42ad0a54a38bad95bc8e02940af`, and `45f84dfe4b6a4412a0a37aedaad0f6ff` in the same order.

Laser attack frame 145 at 30 FPS is the curated visual discharge point, or approximately 4.8 seconds from the action start under the package convention.

Support attack frame 50 at 30 FPS is the curated firing phase, or approximately 1.6333 seconds.

The accepted preview evidence shows the same cyan-tipped weapon, two-hand aim, and retention through discharge and recovery.

Because no actual muzzle locator exists, an effect can be synchronized to the phase but cannot be honestly positioned at an invented node.

## Sourced audio evidence

The already-approved sources were rechecked at their exact source pages on 2026-08-27.

All four are stated CC0 on OpenGameArt and permit the recorded mechanical transformations.

| Roles | Source page, title, creator, and license | Original evidence path, bytes, and SHA-256 | Derived evidence/runtime path, format, duration, and SHA-256 |
|---|---|---|---|
| laser discharge | `https://opengameart.org/content/space-laser`, `Space Laser`, bart, CC0 | `evidence/audio/original/space_laser.wav`, 1,234,188, `3A26ECAB8F36DCA14A91519657E60351566A268D28A2EC4F933B0F9718A7258D` | `alien_infantry_laser_fire.wav`, PCM S16LE 44.1 kHz mono, 1.200000 s, `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770` |
| move and retreat contacts | `https://opengameart.org/content/footsteps-0`, `Footsteps: 01-footstep`, GboxMikeFozzy, CC0 | `evidence/audio/original/footstep_01.ogg`, 9,715, `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC` | `alien_infantry_move.wav`, PCM S16LE 44.1 kHz mono, 0.153923 s, `E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E` |
| idle mechanical ambience | `https://opengameart.org/content/sci-fi-vehicle-sound`, `Sci-Fi Vehicle Sound`, Ogrebane, CC0 | `evidence/audio/original/sci_fi_idle.wav`, 286,692, `46AB090FAE668CD83D613019EBC42F8F24B4C511572F4EAC024AD5006680E350` | `alien_infantry_idle.wav`, PCM S16LE 44.1 kHz mono, 1.624989 s, `B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A` |
| articulated death | `https://opengameart.org/content/various-sound-effects-0`, `Various Sound Effects: snd_death1`, Julie Damsgaard / Spring Spring / Spring Enterprises, CC0 | `evidence/audio/original/snd_death1.wav`, 419,862, `9216E8A1E252765392CB30637489F8E58831280B1139FA5E2E916B79E375C916` | `alien_infantry_death.wav`, PCM S16LE 44.1 kHz mono, 2.379252 s, `AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B` |

The recorded transformations are trimming, silence removal where applicable, fades, normalization, mono conversion, resampling, and PCM conversion; the immutable originals are preserved.

The proposed stable identifiers remain `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death` with parent-owned soundeffect/wrapper registration.

Laser audio should synchronize to attack frame 145 and support-attack frame 50.

Death audio should follow the collapse/impact phase selected by the parent from the accepted 106-frame death action.

Movement contacts should follow actual foot-contact phases rather than free-running from an arbitrary frame.

Selection and acknowledgement remain blocked because the closest vanilla consumer is country/original-tag-wide rather than per-subunit.

Impact and special-action roles have no accepted sourced candidate and remain blocked.

No generated, synthesized, recorded, test-tone, placeholder, or unlicensed audio was used.

## Bespoke vanilla-green counters

The required large and on-map counter strips exist in the runtime tree and match their package records.

| Consumer/token | File | Canvas and states | SHA-256 |
|---|---|---|---|
| `unit_alien_infantry_icon` for subunit token `alien_infantry` | `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` | 152x42, two 76x42 frames; muted vanilla-green alien silhouette then white schematic; alpha 0-255 | `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A` |
| `onmap_unit_alien_infantry_icon` for map counter | `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds` | 60x12, two 30x12 frames; muted vanilla-green then white schematic; alpha 0-255 | `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B` |

The installed vanilla definition uses `noOfFrames = 2`.

The matching skill-local families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`.

The sampled vanilla-green anchor is RGB `(73,106,73)`, with adjacent `(74,107,74)`.

Original source PNGs, processed frame-aware PNGs, DDS decode validation, manifest rows, and comparison evidence are present under `docs/assets/016_brilliant_scientist/dhrondan_icon_package/`.

Visual review of `contact_sheet/dhrondan_icon_package_contact_sheet.png` confirmed the two alien strips preserve the expected green/white state order, border treatment, transparent unused canvas, and legible silhouette.

The runtime registration is parent-owned in `interface/alien_infantry_system.gfx`; this worker made no GFX edit and makes no live-display claim.

## Requirement-to-runtime status

| Requirement | Status | Runtime implication |
|---|---|---|
| preserve alien identity and integrated cyan-tipped firearm | Accepted and byte-identical in runtime | Keep the V13 mesh and textures |
| idle | Accepted provider action | Existing binding may remain |
| move | Accepted provider action | Existing binding may remain |
| laser attack with aim/discharge/recoil/recovery | Accepted provider action | Existing binding may remain; do not invent a positional muzzle node |
| defend | Accepted provider action | Existing binding may remain |
| support attack | Accepted provider action | Existing binding may remain |
| retreat | Accepted provider action | Existing binding may remain |
| articulated death | Accepted provider action | Existing binding may remain |
| training | Blocked | Remove the idle alias; a distinct provider clip is still required for a stock infantry training state |
| wounded/reaction | Blocked or removable by parent | Remove the defend alias; either omit this non-stock custom state or later obtain a distinct provider reaction clip |
| muzzle/effect locator | Blocked | Phase timing is proven, positional locator is not |
| sourced laser/move/idle/death audio | Source and derived files verified | Parent owns definitions, wrappers, and bindings |
| sourced selection/acknowledgement/impact/special audio | Blocked | Do not invent substitutes |
| bespoke two-state vanilla-green counters | Verified complete in runtime | Parent/user owns live consumer acceptance |
| gameplay, entity, GFX, and sound-definition wiring | Parent-owned | This audit intentionally did not edit those surfaces |

## Meaningful validation performed

- Re-ran the repository dependency verifier with the live Meshy schema and balance probe.
- Verified the Blender 5.1.2 bridge and locked adapter/io_pdx_mesh extension through the adapter health route.
- Issued one provider animation request against the historical V13 rig and confirmed it fails before task creation because the rig no longer exists on the provider endpoint.
- Rechecked the balance after the failure and confirmed it remained 13 credits.
- Recomputed every accepted V13 source-export and runtime mesh, animation, and texture hash and confirmed byte equality.
- Reimport-inspected the accepted attack checkpoint and recorded the exact armature, bone set, weight status, and absence of a muzzle/weapon/locator node.
- Visually rechecked the curated attack/support/death evidence and the bespoke counter contact sheet.
- Re-downloaded the four already-approved CC0 audio originals from the recorded URLs and reproduced every recorded source hash.
- Rebuilt the evidence copies of the four derived WAVs from byte-identical runtime files and verified codec, sample rate, channels, duration, and hashes.
- Inspected the installed vanilla infantry training-state family and searched installed vanilla plus the repository for wounded consumers.

## Validation not performed

- No new generation, remesh, retexture, re-rig, or successful animation task was created.
- No provider recovery was attempted after the parent reserved balance for portal work.
- No local animation authoring, weapon attachment, weight change, locator creation, PDX mutation, export, or new reimport was performed.
- No new audio source was accepted for the blocked selection, acknowledgement, impact, or special-action roles.
- No gameplay, entity, GFX, sound-definition, localisation, spreadsheet, or unrelated asset file was edited.
- No in-game consumer validation was performed; it remains parent/user-owned.

## Parent work and unblock conditions

The parent must remove both semantic aliases from `gfx/entities/alien_infantry.asset` and `gfx/entities/alien_infantry.gfx`.

Training should remain fail-closed until a provider-supported route can ingest the existing rig/model and return a distinct substantive training action, or until a separately evidenced runtime design proves the training state is not required.

The present installed-vanilla evidence favors retaining a genuine training state.

For wounded, the parent may remove the custom state because it is absent from the stock vanilla infantry state family and no active requester was found, or retain it only after a distinct provider-authored reaction action exists.

The parent must not bind the existing idle or defend actions under those semantics.

A future provider recovery needs a valid provider-accessible model/rig source.

If re-rigging becomes necessary, all seven accepted downstream actions and exports must be reprocessed and revalidated because skeleton changes invalidate them.

The parent must decide whether to leave muzzle particles unbound, use a genuinely supported existing runtime effect point, or authorize a later provider/adapter route that creates a verifiable locator without manual attachment or invented coordinates.

The parent also owns soundeffect/wrapper definitions, exact frame-event bindings, GFX/entity registration corrections, strict audio-gap disposition, and live consumer validation.

## Simplifications, omissions, and blockers

No fallback or simplification was accepted.

The unresolved training and wounded states are explicit blockers rather than aliases or substitute motions.

The historical V13 rig task has expired from the provider endpoint, the live route cannot accept a local rig file, the parent reserved the available balance for another asset, the accepted skeleton has no muzzle locator, and four strict audio roles remain unsourced or consumer-blocked.

Because those blockers remain, this handoff is not a package-completion or in-game-completion claim.

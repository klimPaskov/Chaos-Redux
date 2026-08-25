# Alien infantry firearm Meshy rig and free-animation handoff

Date: 2026-08-25  
Owner: `chaosx_3d_model_pipeline` bounded Alien Infantry firearm tranche  
Package: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/`  
Overall status: **partial asset pass; approved Quaternius idle, move, and laser-attack actions exported and actual-byte reimported, while runtime firing synchronization and four required roles remain blocked**.

## Scope completed

- Preserved the accepted Meshy V8 R2 neutral rig and all prior rejection evidence.
- Reverified the locked Meshy, Blender adapter, Blender, and io_pdx_mesh environment before provider work.
- Audited official Meshy firearm previews and attempted one materially different Meshy action on the accepted weapon-bearing rig.
- Downloaded and hashed the provider result immediately, prepared it through the locked adapter, and reviewed multi-phase renders.
- Researched, downloaded, licensed, hashed, inspected, retargeted, and visually audited Quaternius Universal Animation Library Standard as a free CC0 professional-source candidate.
- Updated only model-package documentation/evidence surfaces. No gameplay, event, focus, localisation, GFX, `.asset`, entity, particle, or sound-definition file was edited.

## Dependency and route evidence

- Environment report: `.tools/3d_pipeline/reports/environment_report.json`, SHA-256 `8B5887AA835D852EC1498FCAC18D4A44229E4B08EBD90CBDA0F074843EB23FFA`; zero findings at `2026-08-25T12:35:48Z`.
- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` 0.4.0; package git head `d8c77d1cb897e345eb41d38b510b8391b1664346`; Meshy SDK 1.29.0, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32`; compatibility revision `meshy-7-v5`; exact model identifier `meshy-7` exposed.
- Blender HOI4 adapter: `chaosx_blender_hoi4` 1.10.14.
- Blender: 5.1.2.
- io_pdx_mesh: 0.91.0, checksum-locked and loaded.
- Adapter bridge: `127.0.0.1:9876`, listening.
- Relevant adapter requests: Meshy action preparation `27e57671d89c494babdfad6b20151615`; Quaternius source preparation `03c4ac448bc0489288fe483b308c9cfa`; Quaternius retarget `91c2db2ab03b4fc3a233e589f355ddce`; export-coordinate evidence `c794b322fcaf4ffa83b8ea8bee47dc77`; final phase renders `ae4804d2a69a468784487b8333e71d6a`, `4ca70342f86c4264affc0bdcbd92129a`, `5f63c5068f624ba4b1665f5a17565152`, `8caf49db4ac04f4ab1d382857631743e`, `978e719f73614fd9b29b8659efeb7821`, and `ac8a63e0266744f6bdad16b329e293e6`.

## Meshy provider lineage and credits

- Accepted neutral source: rig task `01a0380c-df10-7a2c-ab1e-c28d2248b616`; `provider/downloads/rig_pose_correct_v8_r2.fbx`, SHA-256 `398E796CF47539FAF7EE4D1AE4C860B73EEA69D4B90C59FF5A0425DADCC54124`.
- Pre-tranche live balance: 13 credits.
- Action: official action ID 236, `Draw_and_Shoot_Left`.
- Animation task: `01a038ed-330b-77ea-b344-91361978b5d5`.
- Cost: estimated and consumed 3 credits.
- Download: `provider/downloads/animation_v9_action236_draw_and_shoot_left.fbx`, SHA-256 `69F0C530574439CF122410CE13ED107DC02145B1FCE078028ED91E93D5A808E1`.
- Prepared range: frames 1-161 at 30 FPS; 24 bones; 100,924 triangles; zero zero-weight vertices.
- Result: rejected. The pistol remains integrated, but the right hand holds it upright while the opposite arm gestures; the clip does not establish pistol aim, discharge, recoil, and recovery. It is not a firing action and was not exported.
- Final live balance: 10 credits.

## Historical pre-approval snapshot (superseded by approved-source continuation)

The following source, candidate, and blocker notes preserve the pre-approval state for audit history. The approved-source continuation below is the current status authority.

### Quaternius source, rights, and hashes

- Official page: https://quaternius.com/packs/universalanimationlibrary.html
- OpenGameArt page: https://opengameart.org/comment/108833
- Direct archive: https://opengameart.org/sites/default/files/universal_animation_librarystandard.zip
- Creator/publisher: Quaternius / @Quaternius.
- Retrieval date: 2026-08-25.
- Archive: `evidence/professional_animation/quaternius_universal_animation_library_standard/universal_animation_librarystandard.zip`, 14,541,205 bytes, SHA-256 `18FF1A7215F4852B320203E8AAF02A1578B5C8EEF9027FBAEDFCEDC7B85A3AC2`.
- Bundled license: CC0 1.0 Universal; `License.txt` SHA-256 `11EAC7504A28077E9D8DBAC8DDFCA2566510EFBA7EEF46E11F21CDD2BC96D4D5`.
- Source FBX: `Unreal Engine/AL_Standard.fbx`, copied to `provider/downloads/quaternius_universal_animation_library_standard_unreal.fbx`, SHA-256 `C836C5D47DE2A414818F7644632AC43AA84475DF6709F4514B9410D232800FD9`.
- Provenance record: `evidence/professional_animation/quaternius_universal_pistol_shoot_provenance.json`, SHA-256 `0BBACD0F9D6221C2B1F2A8638408F9CCC00A98606D5E13D2E13F8D261099FF9E`.
- License/source audit: `evidence/professional_animation/quaternius_universal_animation_library_standard/audit.md`.
- Source approval: **needs user review**. The CC0 package is legally redistributable, but the project rule still requires explicit user approval before a professional-source action becomes final.

### Quaternius animation identity and transfer

Adapter inspection found a 65-bone universal source rig and 45 actions. Relevant actions include `Pistol_Aim_Down`, `Pistol_Aim_Neutral`, `Pistol_Aim_Up`, `Pistol_Idle_Loop`, `Pistol_Reload`, `Pistol_Shoot`, general idle/walk/jog/sprint actions, and `Death01`.

- Source action: `Rig|Rig|Pistol_Shoot`.
- Target candidate: `alien_infantry_quaternius_pistol_shoot_candidate` on Meshy R2 `Armature.001`.
- Range: frames 1-20 at 30 FPS.
- Transfer: 659 source curves to 154 target F-curves; no scale curves; no warnings; no authored body motion.
- Sampled motion source/target: frame 1 `0.001381/0.000691`; frame 6 `1.367575/1.367576`; frame 10 `0.620214/0.620205`; frame 15 `0.252098/0.252096`; frame 20 `0.001381/0.000691`.
- Phase evidence: aimed pose frame 1; maximum recoil and candidate discharge frame 6; recovery frames 10 and 15; aimed return frame 20.
- Candidate discharge time: `(6-1)/30 = 0.1667 s` after clip start.
- Contact: front, right, and three-quarter renders at frames 1, 4, 6, 10, 15, and 20 show the integrated pistol remaining in the right-hand skinned mesh through aim, recoil, and recovery.
- Contact sheet: `blender/previews/alien_infantry_quaternius_pistol_shoot_active_contact_sheet.png`, SHA-256 `54CDDCB52E485F8C90F170F014D1F6DC640CE6C0064D2EABD0458CFC46C5B21E`.
- Candidate checkpoint: `blender/checkpoints/alien_infantry_quaternius_pistol_shoot_export_coordinate_probe.blend`, SHA-256 `5C684AC1747CDBAB8CEFE17A1C5781137BD0F02D327A559E660A0B511D7F64BE`.
- Coordinate/topology guard: bounds drift 0.0; 29,916 triangles; zero non-manifold edges, degenerate faces, and negative-scale objects; 154 action F-curves preserved. The pre-existing 108 loose boundary edges remain a geometry risk.

### Required action status

| Role | Status | Evidence or blocker |
|---|---|---|
| Idle | Blocked | Quaternius has candidates, but professional-source approval must precede promotion |
| Move | Blocked | Same; no final locomotion retarget/export performed |
| Laser attack | Needs user review, then still blocked on muzzle locator | Quaternius `Pistol_Shoot` contact/motion candidate passes; frame 6 is provisional only |
| Defend | Blocked | No distinct verified final action |
| Support attack | Blocked | No independent firing action; semantic reuse of `Pistol_Shoot` is forbidden |
| Retreat | Blocked | No distinct verified final action |
| Death | Blocked | `Death01` exists in source but was not promoted; collapse/settling on alien still unverified |

No requested role was filled by a static pose, transform-only clip, manually authored motion, or semantic alias.

### Muzzle, particle, light, and audio crosswalk

The integrated pistol passes visual hand contact, but no stable muzzle locator/node is exposed or verified across the candidate frames. Therefore frame 6 is a provisional synchronization marker only.

- Proposed particle: `alien_laser_muzzle_particle` -> candidate frame 6 / 0.1667 s, **unbound**.
- Proposed light: `alien_laser_muzzle_flash` -> candidate frame 6 / 0.1667 s, **unbound**.
- Proposed sound: `alien_infantry_laser_fire` -> candidate frame 6 / 0.1667 s, **unbound**.
- Support attack: no candidate discharge frame because no independent action exists.
- Existing sourced sound package was not changed.

### Files created or changed

Documentation and ledgers:

- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/job.yaml`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/history.jsonl`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/crosswalk.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/sound_handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/rejections/animation_v9_action236_and_quaternius_audit.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/professional_animation/quaternius_universal_pistol_shoot_provenance.json`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/professional_animation/quaternius_universal_animation_library_standard/audit.md`
- This handoff.

Provider/source evidence and checkpoints:

- `provider/downloads/animation_v9_action236_draw_and_shoot_left.fbx`
- `provider/downloads/quaternius_universal_animation_library_standard_unreal.fbx`
- `provider/library_previews/` official Meshy firearm-action GIFs and contact frames.
- `evidence/professional_animation/quaternius_universal_animation_library_standard/` immutable archive, extracted license, and source files.
- `blender/checkpoints/alien_infantry_quaternius_pistol_shoot_retarget_probe.blend`
- `blender/checkpoints/alien_infantry_quaternius_pistol_shoot_export_coordinate_probe.blend`
- `blender/previews/alien_infantry_action236_contact_three_quarter.png`
- `blender/previews/alien_infantry_quaternius_pistol_shoot_active_frame_*_{front,right,three_quarter}.png`
- `blender/previews/alien_infantry_quaternius_pistol_shoot_active_contact_sheet.png`
- Adapter request/result logs for the IDs listed above.
- `.tools/3d_pipeline/reports/environment_report.json` was refreshed by the required verifier.

No files were deleted. Existing accepted evidence was preserved. Disposable failed outputs were not removed because the compact action FBX, previews, and request logs are the evidence supporting rejection and no safe cleanup was necessary.

### Validation and limitations

- JSON parse of updated `job.yaml` passed and reports the V9 blocked status.
- Adapter transfer motion guard passed with near-identical source and target motion peaks.
- Export-coordinate reopen drift guard passed before and after save with zero bounds drift and all action curves preserved.
- Multi-view renders were reviewed at six meaningful phase frames.
- The Quaternius archive license and exact source hashes were verified locally.
- No final `.anim` export or actual-byte `.anim` reimport was performed because source approval and muzzle-locator gates remain open.
- No in-game validation was performed; that belongs to the user/parent after final wiring.

### Exact parent integration steps

1. Ask the user to explicitly approve or reject Quaternius Universal Animation Library Standard as the professional animation source for this alien unit.
2. If approved, retain `Pistol_Shoot` as a laser-attack source candidate and use only the locked adapter to retarget distinct Quaternius actions for idle, move, defend, retreat, and death. Do not reuse one semantic action for another.
3. Find a distinct verified firing source for `support_attack`; the current 45-action Standard subset exposes only one `Pistol_Shoot` clip, so support attack remains blocked unless another approved substantive firing action is sourced.
4. Establish a stable muzzle locator through a supported provider/adapter route without attaching, parenting, or reweighting the weapon manually. Validate its position and orientation at frames 1, 6, 10, 15, and 20.
5. Only after steps 1-4 pass, promote/export the accepted actions, perform actual-byte `.anim` reimport, and bind particle, light, and sound at the verified discharge frame.
6. Parent owns `.asset`/entity/action-state/GFX/gameplay wiring, final texture/material choice, live consumer validation, and the completion claim. Do not wire the current candidate files directly.

### Blockers and needs-user-review

- **Needs user review:** explicit approval of the Quaternius CC0 package as the professional action source.
- **Blocked:** stable muzzle locator and orientation.
- **Blocked:** independent substantive support-attack firing action.
- **Blocked:** final idle, move, defend, retreat, and death action transfers and evidence.
- **Blocked:** final action export/reimport, particle/light/audio synchronization, runtime entity wiring, and live validation.

No simplification was accepted and no runtime completion is claimed.

## Approved-source continuation

The parent confirmed that the user's earlier “i approve everything” statement and explicit request for a free gun-firing package constitute approval of Quaternius Universal Animation Library Standard CC0 as the professional source. This resolves the source-approval blocker recorded earlier in this handoff. It does not waive any contact, semantic, muzzle, export, or runtime gate.

The locked environment was reverified before continuation. `.tools/3d_pipeline/reports/environment_report.json` has SHA-256 `E18165AE5D4465B6164561C8FD59F1CC609FC661B3DE7752EF0681CBBB0B9412` and zero findings. No additional Meshy credits were consumed; balance remains 10.

### Promoted and exported actions

| Role | Source -> target | Transfer request | Export request | File and SHA-256 | Actual-byte reimport |
|---|---|---|---|---|---|
| Laser attack | `Rig|Rig|Pistol_Shoot` -> `alien_infantry_laser_attack`, 1-20 @ 30 FPS | `d6684681f7ad446485126754d105f624` | `a3ed484918f84378aee060a7861998dc` | `export/anim/alien_infantry_quaternius_laser_attack.anim`, `5B5260F21FAFC8827275827FF99A6D5BCAC29A02D8EAA99ED7ECEAE8D555C4AC` | Passed, request `cb76807b9ae840c6be44fa35f422acb8`; proof blend `FC6EEC2317B15BD5104DBEC700A20A84CCE57BB839147B25D46225FF553C6A63` |
| Idle | `Rig|Rig|Pistol_Idle_Loop` -> `alien_infantry_idle`, 1-51 @ 30 FPS | `fbcf2e0a2c7142ec833bb14ece76e82b` | `4ae1efddab9f4bd680d910eeed36206d` | `export/anim/alien_infantry_quaternius_idle.anim`, `710D86BE58C74CC6BCE58A5BB9411D975BE31693B8D6530A1390A2BBE64EE09F` | Passed, request `424012b1d37d44269d95a5b69c450db2`; proof blend `4478C538AD813B1A66A3172B19F6A58D759EEF9043EBB645F9F2B9542D99EE12` |
| Move | `Rig|Rig|Walk_Loop` -> `alien_infantry_move`, 1-41 @ 30 FPS | `df53c24922dc404db94a9fc4884f8ef4` | `64d9f44b047f46f8ab0f420c89e1473e` | `export/anim/alien_infantry_quaternius_move.anim`, `79E561F831D9C40C752D38412CF0C415A1FE03C07914AFE70A52DB58F35D4E79` | Passed, request `04690c9bbd63427483f1dcddc95374eb`; proof blend `C2188F2651613931414AEE80BCDBAA93FB452000A2B481E2DB0963E0185FE4B6` |

All three transfers retained substantive professional-source motion and returned no adapter warnings. Export-coordinate reopen guards passed with zero bounds drift and preserved action curves. Reimport recovered one 24-bone `io_pdx_rig`, one 29,916-triangle mesh, and `io_pdx_rigAction` for each exact action file.

### Rejected approved-source probes

- Defend: `Rig|Rig|Crouch_Idle_Loop` -> `alien_infantry_defend`, frames 1-89 @ 30 FPS. Transfer request `5663271fffde4525b206f553bfc408f3`; coordinate request `9201270ec2904a869611dce7c44fb2eb`. Motion transfer passed, but visual review shows an implausible raised-knee one-leg balance throughout the loop. It was rejected and not exported.
- Death: `Rig|Rig|Death01` -> `alien_infantry_death`, frames 1-73 @ 30 FPS. Transfer request `a941364b545a4b1aab8edb22695b5709`; coordinate request `767a184b89ef4a1380cd6332a5b21c32`. The collapse is articulated, but the integrated pistol separates from the hand in mid-fall and remains detached at settling. It was rejected and not exported.
- Evidence: `provider/rejections/quaternius_defend_death_contact_failures.md`; `blender/previews/quaternius_defend_contact_sheet.png`, SHA-256 `B238C23724C4580D94B0B2CEC71D5E39563B0F6DD71A33A7BD4984E5019EE9F5`; `blender/previews/quaternius_death_contact_sheet.png`, SHA-256 `5316C75E8C42C27EF152987534A7A0A80992AABAE98EAE674648FFD11D1A9924`.

### Muzzle, effects, and audio gate

The firing action still passes its integrated-weapon gate across aim, peak recoil, and recovery. Frame 6 is the exact discharge phase, 0.1667 seconds after the frame-1 start. The actual-byte reimport reproduces the action across frames 1, 6, 10, 15, and 20.

Actual-byte phase evidence is `blender/previews/quaternius_laser_attack_actual_byte_reimport_contact_sheet.png`, SHA-256 `305B0149BD1A4544E8A5B93A4D90F42169599764146DE08DA6797B72E4152273`.

The verified locked adapter schema exposes no operation to create, derive, or validate a muzzle locator/socket. The Meshy rig exposes hand and humanoid bones but no weapon or muzzle bone. Using unrestricted Blender, manually parenting an empty, attaching the weapon, or inventing a fixed offset would violate the task constraints. Therefore:

- `alien_laser_muzzle_particle`: unbound.
- `alien_laser_muzzle_flash`: unbound.
- `alien_infantry_laser_fire`: unbound.
- Candidate discharge phase: frame 6 / 0.1667 seconds, evidence-only until a supported locator exists.

No gameplay, entity, `.asset`, GFX, particle, or sound-definition file was edited.

### Current role closure

| Role | Status |
|---|---|
| Idle | Export and actual-byte reimport passed; parent wiring pending |
| Move | Export and actual-byte reimport passed; parent wiring pending |
| Laser attack | Export and actual-byte reimport passed; runtime synchronization blocked by muzzle locator |
| Defend | Rejected; implausible retargeted stance |
| Support attack | Blocked; no independent substantive firing action and no alias permitted |
| Retreat | Blocked; no semantically valid retreat action in Standard package |
| Death | Rejected; weapon/hand contact lost during collapse |

### Files added in continuation

- `evidence/professional_animation/quaternius_pistol_idle_provenance.json`, SHA-256 `6A2D9A27E9A9998EAF738B9FF4293C9B48EB3CCBEB0003A1E4380D1B6FC5D06A`.
- `evidence/professional_animation/quaternius_walk_provenance.json`, SHA-256 `7C8F4102E8F6B23194B88EC2C7C26C125DFFD2841AD9B065A86DEB02073DB01E`.
- `evidence/professional_animation/quaternius_crouch_defend_provenance.json`, SHA-256 `F8E333B3829E1B640BEC983690A9AE67B06E145C81C730358EF0F0C41CAB888A`.
- `evidence/professional_animation/quaternius_death01_provenance.json`, SHA-256 `8BB9AF6A347AF45626B1D51579EE0498447BBD076FCB45D7DB1FF36C4B00AF28`.
- Updated firing provenance SHA-256 `F06D2124057A038C30B33BC470B3ACD83AD98350E84E7118F588DB73E889A508`.
- Approved transfer/export/reimport checkpoints, phase previews, three `.anim`/`.txt` pairs, and adapter logs named by the request IDs above.
- `provider/rejections/quaternius_defend_death_contact_failures.md`.

### Remaining parent steps

1. Do not wire the three exports yet as a complete package; defend, support attack, retreat, death, and muzzle synchronization are unresolved.
2. A future locked-adapter revision or provider rig must expose a verifiable muzzle locator before particle/light/audio binding can proceed.
3. Source distinct professional actions for defend, support attack, retreat, and death. Support attack must not reuse `Pistol_Shoot`, and death must retain the integrated pistol through settling.
4. After every remaining action passes and actual-byte reimports, the parent may perform entity/action-state/particle/light/sound wiring and the user may validate the live consumer.

The package remains incomplete and no runtime completion is claimed.

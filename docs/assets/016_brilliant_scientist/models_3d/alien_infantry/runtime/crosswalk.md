# Alien infantry requirement-to-runtime crosswalk

## Historical V8 baseline (superseded by approved-source export state)

| Requirement | Proposed runtime consumer | Evidence | Status |
|---|---|---|---|
| Reusable alien identity and one integrated upright right-hand pistol | `alien_infantry_entity` / `alien_infantry_mesh` | V8 generation `01a037ff-1e09-7757-aa2c-ee123fc7c2e2`; remesh previews `blender/previews/alien_infantry_pose_correct_v8_remesh_*.png` | Neutral geometry accepted as diagnostic evidence only |
| Vanilla-calibrated scale | entity scale `0.8` exactly once | V8 R2 FBX Blender prepare report; source height `7.3518242835`, effective runtime height `5.8814594268` | Passed neutral geometry gate |
| Rigid pistol, right-hand grip, and free left arm | all skeletal states | V8 neutral R2 FBX and actions 232, 104, and 690 full-phase previews | Neutral passed; firing gate failed because no official action supplies the required one-handed aim/discharge/recoil/recovery sequence |
| Idle | `idle` -> `alien_infantry_idle` | Not purchased after firearm gate failed | Blocked: Meshy firearm-animation capability |
| Move | `move` -> `alien_infantry_move` | Not purchased after firearm gate failed | Blocked: Meshy firearm-animation capability |
| Laser attack | `attack` -> `alien_infantry_laser_attack` | `provider/rejections/generation_pose_correct_v8_firearm_capability.md` | Blocked: no accepted aim/discharge/recoil/recovery, stable muzzle node/time, beam/light/audio sync |
| Defend | `defend` -> `alien_infantry_defend` | Not purchased after firearm gate failed | Blocked: Meshy firearm-animation capability |
| Support attack | `support_attack` -> `alien_infantry_support_attack` | Not purchased after attack gate failed | Blocked: independent firing evidence and synchronization absent |
| Retreat | `retreat` -> `alien_infantry_retreat` | Not purchased after firearm gate failed | Blocked: Meshy firearm-animation capability |
| Death | `death` -> `alien_infantry_death` | Not purchased after firearm gate failed | Blocked: collapse/impact/settling evidence absent |
| Laser, movement, idle, death sounds | entity-state sounds | `evidence/audio/provenance/audio_sources.json`; `sound/alien_infantry_sound.asset`; `sound/shared_alien_system/alien_infantry/`; `runtime/sound_handoff.md` | Sources, derivatives, sound definitions, and shared category registration complete; entity-event synchronization intentionally unbound |
| Large and on-map counters | Event 016 counter consumers | `runtime/counter_handoff.md` | Existing bespoke package reconciled; parent/user live review remains |
| Packed PDX textures | `alien_infantry_mesh` material | Historical provider map hashes are recorded in `manifest.md`; rejected provider binaries were deleted during compact cleanup | Blocked pending a final accepted Meshy rig/action lineage and fresh processing |
| PDX `.mesh` and seven `.anim` files | model/animation definitions | No accepted firing lineage | Blocked; no exports or actual-byte reimports |
| Runtime registration and live validation | `alien_infantry_entity` | Parent-owned consumer | Not performed |

No semantic action is substituted or aliased. No manual weapon attachment, manual motion, partial paid tranche, or fallback is accepted.

V8 ended with live balance 237 after 54 credits. The other semantic actions and all exports were deliberately skipped after the mandatory firing gate failed.

## Historical V9 pre-promotion crosswalk (superseded by approved-source export state)

| Candidate | Source | Range | Contact/discharge evidence | Status |
|---|---|---:|---|---|
| `alien_infantry_laser_attack` | Meshy action 236 `Draw_and_Shoot_Left`, task `01a038ed-330b-77ea-b344-91361978b5d5` | 1-161 @ 30 FPS | Pistol retained, but no credible aim/discharge/recoil/recovery | Rejected; no export or binding |
| `alien_infantry_quaternius_pistol_shoot_candidate` | Quaternius `Rig|Rig|Pistol_Shoot`, CC0 source FBX `C836C5D4...00FD9` | 1-20 @ 30 FPS | Aim at frame 1, peak recoil/candidate discharge at frame 6 (`0.1667 s`), recovery through frames 10/15, aimed return at frame 20; pistol retained throughout | Candidate contact/motion pass; needs explicit professional-source approval and stable muzzle locator; not exported |

The seven requested runtime roles remain blocked. The Quaternius library also contains real idle, locomotion, pistol idle/reload, and articulated death actions, but none was promoted because professional-source approval must precede the remaining retarget tranche and `support_attack` still requires independent firing evidence. Particle, light, sound, entity, and gameplay wiring remain unchanged.

## Approved-source export state

| Requirement | Export/reimport evidence | Final status |
|---|---|---|
| Idle | `export/anim/alien_infantry_quaternius_idle.anim`, SHA-256 `710D86BE...EE09F`; actual-byte reimport request `424012b1d37d44269d95a5b69c450db2` | Asset evidence passed; parent runtime wiring pending |
| Move | `export/anim/alien_infantry_quaternius_move.anim`, SHA-256 `79E561F8...D4E79`; actual-byte reimport request `04690c9bbd63427483f1dcddc95374eb` | Asset evidence passed; parent runtime wiring pending |
| Laser attack | `export/anim/alien_infantry_quaternius_laser_attack.anim`, SHA-256 `5B5260F2...5C4AC`; actual-byte reimport request `cb76807b9ae840c6be44fa35f422acb8` | Action/contact/export passed; runtime binding blocked by absent stable muzzle locator |
| Defend | `Crouch_Idle_Loop` probe and `quaternius_defend_contact_sheet.png` | Rejected: implausible one-leg balance |
| Support attack | No independent substantive firing action in Standard package | Blocked; no alias permitted |
| Retreat | No semantically valid retreat action in Standard package | Blocked |
| Death | `Death01` probe and `quaternius_death_contact_sheet.png` | Rejected: pistol separates from hand during collapse |

No gameplay/entity/GFX/sound definition was wired. Frame 6 / 0.1667 seconds is the verified firing phase only; particle/light/audio synchronization remains unbound until a stable muzzle locator exists.

## Additional CC0 package audit

| Source package | Candidate actions inspected | Muzzle locator | Crosswalk result |
|---|---|---|---|
| Quaternius Universal Animation Library 2 Standard, CC0, FBX SHA-256 `D4A2DD67...FEC90` | 42 substantive clips, including shield, sword, hit, traversal, idle, work, and zombie roles; no firearm or death/collapse clip | None; no firearm object and no supported adapter locator operation | No eligible retarget. Defend, support attack, retreat, and death remain blocked; existing attack remains unbindable without a stable muzzle locator. |

The follow-up did not create semantic aliases or substitute `Hit_Knockback`, `LayToIdle`, shield, sword, or zombie motion for a required firearm/unit role.

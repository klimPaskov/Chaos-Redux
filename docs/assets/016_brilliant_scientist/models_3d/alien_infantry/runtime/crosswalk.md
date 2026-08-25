# Alien infantry requirement-to-runtime crosswalk

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

# Meshy mounted rider action research

The official Meshy animation library was searched and archived from `https://docs.meshy.ai/en/api/animation-library` on 2026-08-24.
The archived HTML is `provider/meshy_rider_action_research/evidence/animation_library.html`, SHA-256 `C9ACCFDA572BE609B2357DAA5EF2EBAF2401ABD6ECCF249947771BFFF0B0F0D0`.

Search terms covered `sling`, `stone`, `throw`, `discus`, `lasso`, `rope`, `whip`, `seated`, `mounted`, `horse`, `pitch`, `grenade`, `bow`, and `shoot`.
The library contains no sling, stone, lasso, whip, discus, mounted, horseback, or seated-projectile preset.

Official CDN GIFs and mechanically extracted phase PNGs are archived under `provider/meshy_rider_action_research/previews/` and `provider/meshy_rider_action_research/phase_frames/`.
These are research evidence only and are not runtime art.

## Conditionally approved eight-action plan

The motion donor can reuse verified successful Meshy humanoid rig task `01a03456-275c-7f92-8e53-4a7bdbf97826` from the package-owned Cannibal Scavenger Warband evidence.
This avoids generating replacement rider geometry; the donor contributes only receipt-verified Meshy skeletal motion for retargeting onto the segmented bespoke Bone Riders rider.

| Runtime role | Meshy action ID | Official action name | Mapping policy |
| --- | ---: | --- | --- |
| idle | 307 | `Sitting_Answering_Questions` | Seated torso and hand life; retain mounted pelvis and legs. |
| move | 33 | `Chair_Sit_Idle_M` | Distinct seated brace/bob while the horse provides gallop motion; retain mounted pelvis and legs. |
| attack | 280 | `Female_Crouch_Pick_Throw_Forward` | Upper-body-only mapping. Must visibly use the bespoke sling and pouch as a load, sling-stone release, follow-through, and recovery; no empty-hand read. |
| defend | 361 | `Sit_Dodge` | Seated dodge/brace; retain mounted pelvis and legs. |
| support_attack | 393 | `baseball_pitching` | Upper-body-only mapping. Must read as a second, distinct sling-stone volley with the bespoke sling visible; no baseball or empty-hand read. |
| retreat | 356 | `Sit_Hands_on_Head_Lean_Back` | Seated backward brace during the horse trot; retain mounted pelvis and legs. |
| training | 354 | `Sitting_Clap` | Provisional mounted handling/drill cue paired with the horse eating action; retain mounted pelvis and legs. |
| death | 183 | `Shot_and_Fall_Backward` | Full articulated rider collapse synchronized to the horse collapse; final contact and detach behavior require compound preview acceptance. |

All action IDs are distinct.
The combat pair is conditionally approved only if final compound previews show a visible sling and pouch, preserved seated lower body, two distinct projectile attacks, and readable load/release/follow-through/recovery phases.

## Rejected combat candidates

| Action ID | Official name | Rejection reason |
| ---: | --- | --- |
| 239 | `Crouch_Pull_and_Throw` | Starts kneeling and produces a weaker mounted load/release read than action 280. |
| 398 | `Crouch_Charge_and_Throw` | Remains deeply crouched and conflicts with the mounted seat. |
| 389 | `Grip_and_Throw_Down` | Reads as a downward slam rather than a projectile volley. |
| 421 | `Over_Shoulder_Throw` | Reads as a grappling/body throw, not sling fire. |
| 515/628 | `Female_Throwing_Stance_Charge` and in-place variant | Running charge motion has no readable projectile release in the official preview. |
| 46 | `Jump_Rope` | Contains circular hand motion but no load, projectile release, or combat recovery. |
| 304 | `Seated_Fist_Pump` | Celebration, not a substantive support attack. |

## Spend and processing gate

No rider action task has been launched in this tranche.
The planned provider cost after an authoritative adapter reload is eight `meshy_animate` calls at three credits each, 24 credits total.
The latest verified balance was 587 credits.
Compound processing remains paused until the adapter registration recovery is loaded and its dependency/route state is authoritative.

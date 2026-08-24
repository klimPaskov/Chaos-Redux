# Installed vanilla cavalry precedents

Inspected installed files:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_cavalry.asset`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/animation.asset`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/cavalry_horse.mesh`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/cavalry_frame.mesh`

`infantry_cavalry_horse_mesh` binds `cavalry_idle`, `cavalry_move`, `cavalry_attack`, `cavalry_attack_2`, and `cavalry_idle_forward` to the horse mesh and applies pdxmesh scale `0.45`. The compound frame uses scale `1.0`. `units_cavalry.asset` supplies `cavalry_entity`, `generic_cavalry_rifle_combined_entity`, and `infantry_cavalry_horse_entity`, with rider attachment through `Saddle_Node` and a separate `0.65` attached horse-entity scale precedent.

Exact installed horse animation files registered in `animation.asset` are `cavalry_horse_idle.anim`, `cavalry_horse_idle_forward.anim`, `cavalry_horse_walk.anim`, `cavalry_horse_charge.anim`, and `cavalry_horse_charge_2.anim`. Exact frame registrations are `cavalry_frame_attack.anim`, `cavalry_frame_cavalry_idle.anim`, and `cavalry_frame_cavalry_move.anim`. Installed rider precedents include `GER_infantry_cavalry_rider_idle_rifle.anim` and `GER_infantry_cavalry_rider_moving_rifle.anim`.

These are professional installed sources and may be evaluated for compatible horse idle/move/charge and rider idle/move retargeting after a final skeleton exists. They are not pre-approved final Bone Riders actions. No installed precedent supplies a mounted sling aim/discharge/recoil/recovery cycle, mounted sling training cycle, or articulated compound horse+rider death. Defend, support attack, retreat, and training cannot be satisfied by semantic aliases of idle/move/attack.

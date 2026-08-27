# Reusable alien infantry unit system

`alien_infantry` is a shared land-unit database entry rather than a Kruger-owned or D’Rhondan-owned duplicate. Event 016, Event 019 provider 508, D’Rhondan contact, and future event packages consume the same subunit, equipment, technology, tactic, counter, entity, and sound identifiers through the source-counted contact API.

The unit is spawn-only (`active = no`) and has no training or wounded animation state. Those states are not requested by the landing API and must not be represented by an idle/defend alias. The runtime entity therefore registers only the seven provider-authored actions that exist in the package: idle, move, laser attack, defend, support attack, retreat, and death.

## Unit and equipment contract

Each battalion has two combat width, zero human manpower, 40 HP, 90 organisation, 0.75 recovery, 10 reconnaissance, 0.50 initiative, five suppression, and 0.04 supply consumption. It requires exactly 200 `alien_laser_weapon_equipment` and no Infantry Equipment, Support Equipment, or other ordinary equipment. The subunit has `active = no`, so a technology unlock does not expose it as a freely selectable division-designer battalion.

`alien_laser_weapon_equipment_1` is the first and only buildable variant of the `alien_laser_weapon_equipment` archetype. It provides 0.98 reliability, 6.5 km/h speed, 60 defense, 40 breakthrough, 40 percent hardness, 30 armor, 30 soft attack, 20 hard attack, 80 piercing, 10 air attack, and a 0.75 IC cost. Licensing and lend lease are disabled. Production also requires a positive source-counted contact-access trigger; possessing the hidden unit technology without contact cannot open the production line.

The public API creates the only alien template: the locked ten-battalion, twenty-width `D’Rhondan Landing Cohort`. One complete cohort requires exactly 2,000 laser weapons. Project-force reconstruction does not create, unlock recruitment for, or raise a division cap on a second template.

## Technology and tactics

`brilliant_scientist_alien_infantry_tech` is a hidden grant-only bridge that enables the laser-equipment variant. The technology may exist before contact, but the equipment production gate still requires positive contact authorization. It deliberately does not use `enable_subunits`, preserving the battalion's inactive division-designer status while the public API can still construct the locked template. `brilliant_scientist_alien_predictive_warfare_tech` depends on it and unlocks the two alien-only tactics.

`tactic_alien_predictive_vector_assault` is an attacking standard-phase tactic with base factor four. It grants 35 percent attacker combat power, reduces the defender by 15 percent, increases attacker movement by 25 percent, and increases attacker organization damage by 30 percent.

`tactic_alien_probability_screen` is a defending standard-phase tactic with base factor four. It reduces the attacker by 35 percent, grants 30 percent defender combat power, and reduces attacker organization damage by 30 percent.

Both tactics are inactive until the predictive-warfare technology unlocks them, and each trigger requires `has_unit_type = alien_infantry`. Their values deliberately exceed vanilla basic and assault tactics, but their side and standard-phase gates prevent them from applying to ordinary formations or replacing phase-owned tactics.

## Runtime identifiers

- Subunit: `alien_infantry`
- Equipment archetype: `alien_laser_weapon_equipment`
- Equipment variant: `alien_laser_weapon_equipment_1`
- Operational technology: `brilliant_scientist_alien_infantry_tech`
- Predictive-warfare technology: `brilliant_scientist_alien_predictive_warfare_tech`
- Attacker tactic: `tactic_alien_predictive_vector_assault`
- Defender tactic: `tactic_alien_probability_screen`
- Runtime entity consumer: `alien_infantry_entity`
- Public contact API: `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`
- Event 019 provider 508 uses source receipt `constant:alien_infantry_contact_source.event019_provider_508` (receipt 3), routes every spawn surface through Event 019’s ordinary unit ledger transaction, and contributes no separate training or sustainment obligation. One Event 019 request or scenario actor may materialize exactly one cohort; automatic generation narrows its selected-state target to one, and anomalous scenarios use an actor-local target so the shared scenario intensity remains unchanged for other actors. The API creates the cohort with Event 019’s allocated engine deletion ID and debits exactly 2,000 laser weapons, but defers state markers, landing history, Alien Presence, Pact Strain, cooldown, and pact callbacks until the innermost or enclosing Event 019 transaction has passed its final ledger proof. Persistent transaction receipts survive a delayed same-tag rollback retry; a failed transaction deletes that exact cohort and refunds the one proven debit only after absence is proved and before Event 019 checks the restored stockpile and ledger snapshot. D’Rhondan’s one-time sovereignty bootstrap may pass temporary `alien_infantry_initial_force_mode = 1` only with batch mode and a positive sovereignty receipt; that exact branch preserves the 2,000-laser debit and cohort materialization while suppressing pact-host telemetry and the ordinary landing callback.
- Ordinary DHR landings keep the seven-day reservation and exact 2,000-laser debit. After a successful landing, the shared API applies the highest active recovery tier: 30 days by default, 24 with `dhrondan_landing_network_enabled`, 18 with `dhrondan_descent_windows_guarded`, or 12 with `dhrondan_near_space_secured`; the sovereignty bootstrap batch never sets this cooldown. The landing decision's AI base weight is modified by the network, reserve-priority, guarded-descent, and near-space flags through `constant:alien_infantry_landing_ai` factors.

## Visual, model, and sound contract

The source declarations use stable final paths. Static binary art and the seven provider-authored action files are installed, but the V13 package is not runtime-complete: the provider rig has no supported muzzle/effect locator, and the current recovery audit cannot certify positional particle/light playback or the complete sound-role contract. Its immutable package record is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`, and the latest parent-facing recovery handoff is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_alien_infantry_v13_recovery_audit_handoff.md`. Historical Quaternius, V10, and V11 records remain preserved but do not control the V13 package.

### V13 Meshy package (static/action evidence; runtime gates open)

- Approved Meshy input: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/refs/original/meshy_input_v13_tpose_right_pointing_colored.png`, SHA-256 `2D72EEB020C8989B463F214D4B5FC1C29C4AB313AEEE9F033B71E6DE1881BF3A`.
- The accepted Meshy 7 rig task is `01a03dcf-f0ba-7b67-b769-5a2678b03a40`, with 24 bones and a final 59,999-triangle mesh.
- Final mesh: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry.mesh`.
- Final textures: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_v13_diffuse.dds`, `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_v13_normal.dds`, and `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_v13_specular.dds`.

| Role | Final export | Meshy action | Provider task |
| --- | --- | --- | --- |
| `idle` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_idle.anim` | 0 `Idle` | `01a03dd1-23a5-7728-9c09-f09683d64ffe` |
| `move` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_move.anim` | 692 `walking_2_inplace` | `01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01` |
| `laser_attack` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_laser_attack.anim` | 223 `Draw_and_Shoot_from_Back_1` | `01a03dd1-2d74-70b2-a151-e8d98c82e4de` |
| `defend` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_defend.anim` | 89 `Combat_Stance` | `01a03dd1-31cc-7729-9612-26eb8f7d44c3` |
| `support_attack` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_support_attack.anim` | 234 `Walk_Forward_While_Shooting` | `01a03dd1-35e5-7f37-a601-70982bdf5f74` |
| `retreat` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_retreat.anim` | 685 `Walk_Backward_with_Gun_inplace` | `01a03dd1-3a02-7f38-8f3c-0236be3dc57e` |
| `death` | `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset/alien_infantry_death.anim` | 183 `Shot_and_Fall_Backward` | `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4` |

Every V13 action is a distinct Meshy preset action exported through io_pdx_mesh and reimported from its actual `.anim` bytes with the final `.mesh`; Blender did not author replacement motion. The detailed hashes, frame counts, reimport request IDs, and proof artifacts are recorded in `final_manifest.md`.

- Large counter: `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds`, registered as `GFX_group_alien_infantry_icon` and `GFX_unit_alien_infantry_icon_medium` in `interface/alien_infantry_system.gfx`.
- Map counter: `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, registered as `GFX_unit_alien_infantry_icon_medium_white`.
- Equipment icon: `gfx/interface/technologies/shared_alien_infantry/alien_laser_weapon_equipment.dds`, registered as `GFX_alien_laser_weapon_equipment_medium`.
- Operational technology icon: `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_infantry.dds`, registered as `GFX_brilliant_scientist_alien_infantry_tech_medium`.
- Predictive-warfare technology icon: `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_predictive_warfare.dds`, registered as `GFX_brilliant_scientist_alien_predictive_warfare_tech_medium`.
- Tactic icons: `gfx/interface/landcombat/tactics/tactic_alien_predictive_vector_assault.dds` and `gfx/interface/landcombat/tactics/tactic_alien_probability_screen.dds`, registered under matching `GFX_` names.
- KRG laser-batch decision icon: `gfx/interface/decisions/016_brilliant_scientist/decisions/decision_alien_laser_batch.dds`, registered as `GFX_decision_brilliant_scientist_krg_alien_laser_batch` in `interface/016_brilliant_scientist_kruger_state_decisions.gfx`.
- Sourced laser-fire, movement, idle, and death WAV files and their sound definitions are installed under `sound/shared_alien_system/alien_infantry/` and `sound/alien_infantry_sound.asset`.
- Reusable `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` definitions are installed under `gfx/particles/alien_infantry/` and `gfx/entities/`.
- Commit `0e724fb8a` promoted the V13 mesh, seven animations, entity/GFX/animation registrations, and four state sound references into the engine-facing runtime tree. The provider evidence remains under `docs/assets/`, no runtime consumer points into that evidence tree, and live in-game integration is not claimed. The current runtime entity deliberately omits unsupported training and wounded aliases; it must not be treated as a complete package until a supported locator/effect path and remaining audio gates are resolved.
- The locked adapter exposes no supported muzzle-locator authoring operation, and the Meshy rig has no muzzle bone. The fused cyan muzzle cap is visual evidence only, so `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` remain registered but unbound; attack/support firing sound references are statically present, while positional playback and live acceptance remain unresolved.
- Sourced audio currently covers laser discharge, movement, idle, and death. Per-subunit selection or acknowledgement remains blocked by tag-wide vanilla consumers, and no defensible sourced candidates were accepted for distinct impact or special-action roles; no synthesized or placeholder audio is accepted. The current timing crosswalk is recorded in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/sound_handoff.md` and does not replace live consumer evidence.

## Future extensions

Future events can grant their own source receipt and call the same landing API without copying the unit or production line. Additional alien doctrines may unlock new tactics or country modifiers, but they should preserve the exact battalion equipment contract, contact-gated production, inactive designer status, and single locked-template ownership boundary.

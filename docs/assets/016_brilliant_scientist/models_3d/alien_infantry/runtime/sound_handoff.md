# Alien infantry sound handoff

Status: sourced entity-state audio and sound definitions installed; Quaternius idle, move, and laser-attack actions have actual-byte reimport evidence, but entity events, muzzle-locator synchronization, mixing acceptance, and live validation remain blocked.

The exact vanilla model precedent is `gfx/entities/units_infantry.asset#infantry_rifle_entity`. Its states expose `attack`, `defend`, `support_attack`, `move`, `retreat`, `death`, and `idle`; the installed movement precedent fires `infantry_move_animation` from a state event. Entity-state sound identifiers proposed for the custom consumer are `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death`.

The installed definitions are `sound/alien_infantry_sound.asset`, the four category registrations in `sound/chaosx_sound.asset`, and the PCM WAV files under `sound/shared_alien_system/alien_infantry/`. The final accepted entity should fire laser audio from the muzzle event in `attack` and `support_attack`, movement audio at grounded foot contacts in `move` and `retreat`, the idle one-shot on idle entry, and death audio at the death onset. Exact action frames remain blocked until an accepted weapon-bearing mesh and final actions exist.

The V7 firearm audit did not yield a valid synchronization point. Action 690 `Walk_Forward_While_Shooting_inplace`, action 104 `Side_Shot`, and action 232 `Cowboy_Quick_Draw_Shooting` all catastrophically deformed the integrated rifle and destroyed a stable muzzle. Therefore there is no accepted discharge frame/time or muzzle node for either `alien_infantry_laser_attack` or `alien_infantry_support_attack`, and `alien_infantry_laser_fire` must not be wired by inference. The sourced CC0 WAV and soundeffect definition are installed but unsynchronized pending an acceptable provider-authored firing action.

All source URLs, authors, CC0 licenses, immutable originals, transformations, checksums, and derived PCM receipts are recorded in `evidence/audio/provenance/audio_sources.json`.

Selection and acknowledgement are intentionally blocked at the subunit level. Installed HOI4 uses country/original-tag-wide `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat` voice consumers. Replacing them would also replace ordinary infantry voices, which is forbidden by the accepted brief.

## Historical pose-correct V8 synchronization audit (superseded)

V8 preserved the upright right-hand pistol in neutral geometry and rig evidence, but official actions 232 `Cowboy_Quick_Draw_Shooting`, 104 `Side_Shot`, and 690 `Walk_Forward_While_Shooting_inplace` all failed to supply a genuine aim/discharge/recoil/recovery sequence. Action 690 also converted the selected one-handed identity into a two-handed low-ready hold. Consequently there is still no accepted discharge frame/time or stable muzzle locator for either firing consumer.

The exact crosswalk remains intentionally empty: `alien_infantry_laser_attack` and `alien_infantry_support_attack` have no accepted provider action; `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` remain unbound. Movement, idle, and death synchronization also remains unset because those actions were not purchased after the mandatory firing gate failed. No audio file or sound definition was recreated or overwritten during V8.

## Historical V9 candidate synchronization audit (superseded by approved export status)

Meshy action 236 remains rejected and yields no synchronization point. The Quaternius CC0 `Pistol_Shoot` candidate supplies a genuine recoil cycle with maximum transferred motion at frame 6 of frames 1-20 at 30 FPS. If and only if the user approves Quaternius as the professional source and a stable muzzle locator is verified, the provisional discharge event would be frame 6, `0.1667 s` after clip start, shared by `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire`.

That timing is not accepted runtime data yet. The candidate remains unwired because source approval and muzzle-locator gates are open. `support_attack`, movement, retreat, idle, and death audio synchronization also remain unset.

## Approved Quaternius export status

Quaternius source approval is resolved. `alien_infantry_quaternius_laser_attack.anim` exported and actual-byte reimported successfully, and the integrated pistol remains in the hand through aim, maximum recoil at frame 6, and recovery at frame 20. The exact discharge phase is frame 6 / 0.1667 seconds after clip start.

The locator gate remains unresolved: the locked Blender HOI4 adapter exposes no operation that can create or derive a muzzle node, and manual Blender parenting/attachment is forbidden. Therefore `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` remain intentionally unbound despite the verified frame. Move and idle actions also reimported, but their sound event frames were not bound because parent entity wiring is out of scope. Support attack, retreat, defend, and death have no accepted actions.

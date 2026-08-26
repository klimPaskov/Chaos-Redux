# Alien infantry V13 sound handoff

Status: sourced CC0 audio for four roles and static entity-state sound references are present; positional effect binding, strict selection/acknowledgement/impact/special-role coverage, live playback, and in-game acceptance remain unresolved.

The vanilla precedent is `gfx/entities/units_infantry.asset#infantry_rifle_entity`. The current V13 entity uses the provider-authored Meshy actions and static references `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death` in `gfx/entities/alien_infantry.asset`.

## Provider and source evidence

Meshy V13 action evidence is recorded in `attempts/v13_firearm_preset/final_manifest.md`; it is separate from audio-provider evidence and from runtime wiring. Audio provenance, source URLs, authors, CC0 licenses, immutable-source hashes, derived hashes, and PCM receipts are recorded in `evidence/audio/provenance/audio_sources.json`.

The accepted sourced roles are laser discharge, movement, idle, and death. The current static sound definitions are in `sound/alien_infantry_sound.asset`, their category registrations are in `sound/chaosx_sound.asset`, and the derived PCM WAV files are under `sound/shared_alien_system/alien_infantry/`.

## Current synchronization crosswalk

| Consumer state | Meshy V13 evidence | Handoff timing | Static reference |
| --- | --- | --- | --- |
| `attack` | Action 223 `Draw_and_Shoot_from_Back_1`, 236 frames at 30 FPS | Frame 145 / 4.8000 seconds, with recovery by approximately frame 190 | `alien_infantry_laser_fire` in `gfx/entities/alien_infantry.asset` |
| `support_attack` | Action 234 `Walk_Forward_While_Shooting`, 99 frames at 30 FPS | Frame 50 / 1.6333 seconds | `alien_infantry_laser_fire` in `gfx/entities/alien_infantry.asset` |
| `move` | Action 692 `walking_2_inplace`, 37 frames at 30 FPS | Ground contacts at frames 1 and 19 | `alien_infantry_move` in `gfx/entities/alien_infantry.asset` |
| `retreat` | Action 685 `Walk_Backward_with_Gun_inplace`, 31 frames at 30 FPS | Ground contacts at frames 1 and 16 | `alien_infantry_move` in `gfx/entities/alien_infantry.asset` |
| `idle` | Action 0 `Idle`, 121 frames at 30 FPS | One-shot on state entry; no loop is assumed | `alien_infantry_idle` in `gfx/entities/alien_infantry.asset` |
| `death` | Action 183 `Shot_and_Fall_Backward`, 106 frames at 30 FPS | Death onset at frame 1; future impact candidate near frame 80 / 2.6333 seconds | `alien_infantry_death` in `gfx/entities/alien_infantry.asset` |

These timings are provider/evidence crosswalk selections and static event references, not proof of positional playback. The current entity contains the listed static references, but no live consumer or in-game acceptance is claimed.

## Unresolved effect and audio roles

No supported Meshy or Blender-authored muzzle locator exists. The locked adapter exposes no locator-create operation, the rig has no muzzle bone, and the fused cyan muzzle cap is visual evidence only; no origin, hand point, or inferred locator may be used as a substitute.

`alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` are registered definitions, but they remain intentionally unbound until a provider- or adapter-supported runtime effect point is available. Without that point, positional laser audio and effect synchronization cannot be accepted.

Per-subunit selection and acknowledgement remain blocked because the closest vanilla consumers are country/original-tag-wide `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat` voices. Replacing those consumers would alter ordinary infantry voices and is outside the accepted scope.

No defensible sourced impact candidate or distinct special-action candidate was accepted. No synthesized or placeholder audio is used, and these roles remain explicit package blockers.

The provider package was routed through `chaosx_3d_model_pipeline`; provider audio evidence, static sound references, positional effect binding, and live acceptance are separate ownership and evidence gates.

Historical V8, V10, V11, KayKit, and Quaternius synchronization sections are retained in their dated handoffs as evidence-only records and must not be used as current runtime instructions.

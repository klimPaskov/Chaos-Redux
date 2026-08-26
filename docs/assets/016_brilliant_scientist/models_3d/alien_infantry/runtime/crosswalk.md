# Alien infantry V13 requirement-to-runtime crosswalk

The V13 provider package is the current model source of truth. Provider evidence in `attempts/v13_firearm_preset/final_manifest.md` proves export and actual-byte reimport; the rows below separately record static runtime registration and the still-pending live consumer gate.

| Requirement | Provider evidence | Static runtime registration | Current status |
| --- | --- | --- | --- |
| Reusable alien identity with an integrated upright right-hand pistol | Meshy V13 accepted recovery generation and 59,999-triangle final mesh | `alien_infantry_entity` uses `alien_infantry_mesh` from `gfx/entities/alien_infantry.asset` | Provider and static registration present; live consumer acceptance pending |
| Vanilla-calibrated scale | Final source height `7.3518023491` against vanilla `7.3518242835` | `scale = 0.8` in `alien_infantry_entity` | Static calibration recorded; live visual acceptance pending |
| Idle | Meshy action 0 `Idle`, task `01a03dd1-23a5-7728-9c09-f09683d64ffe`, 121 frames at 30 FPS | `idle` state references `alien_infantry_idle` | Provider export/reimport and static state present; live acceptance pending |
| Move | Meshy action 692 `walking_2_inplace`, task `01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01`, 37 frames at 30 FPS | `move` state references `alien_infantry_move` with movement events | Provider export/reimport and static state present; live foot-contact acceptance pending |
| Laser attack | Meshy action 223 `Draw_and_Shoot_from_Back_1`, task `01a03dd1-2d74-70b2-a151-e8d98c82e4de`, 236 frames at 30 FPS | `attack` state references `alien_infantry_laser_attack` and the firing sound at the proposed event time | Provider export/reimport and static state present; effect-point and live positional acceptance pending |
| Defend | Meshy action 89 `Combat_Stance`, task `01a03dd1-31cc-7729-9612-26eb8f7d44c3`, 51 frames at 30 FPS | `defend` state references `alien_infantry_defend` | Provider export/reimport and static state present; live acceptance pending |
| Support attack | Meshy action 234 `Walk_Forward_While_Shooting`, task `01a03dd1-35e5-7f37-a601-70982bdf5f74`, 99 frames at 30 FPS | `support_attack` state references `alien_infantry_support_attack` and the firing sound at the proposed event time | Provider export/reimport and static state present; effect-point and live positional acceptance pending |
| Retreat | Meshy action 685 `Walk_Backward_with_Gun_inplace`, task `01a03dd1-3a02-7f38-8f3c-0236be3dc57e`, 31 frames at 30 FPS | `retreat` state references `alien_infantry_retreat` with movement events | Provider export/reimport and static state present; live foot-contact acceptance pending |
| Death | Meshy action 183 `Shot_and_Fall_Backward`, task `01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4`, 106 frames at 30 FPS | `death` state references `alien_infantry_death` and the death sound at onset | Provider export/reimport and static state present; live acceptance pending |
| Training and wounded presentation | No separate provider actions were requested because the subunit is not trainable | `training` uses `alien_infantry_idle` and `wounded` uses `alien_infantry_defend` | Static presentation aliases are explicit and distinct from provider-role aliases; live acceptance pending |
| Laser, movement, idle, and death audio | CC0 source and derived PCM provenance in `evidence/audio/provenance/audio_sources.json` | Four sound definitions and entity state references are present in `sound/alien_infantry_sound.asset` and `gfx/entities/alien_infantry.asset` | Static source-level wiring present; positional playback and live acceptance pending |
| Selection and acknowledgement audio | No accepted per-subunit route because vanilla consumers are tag-wide | No new global tag-wide replacement is wired | Explicitly blocked to avoid changing ordinary infantry voices |
| Impact and special-action audio | No defensible sourced candidates accepted | No synthesized or placeholder roles are wired | Explicitly blocked |
| Muzzle particle and light | The fused cyan cap is visual evidence only and no supported locator authoring operation exists | `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` definitions are registered but unbound | Explicitly blocked pending a supported effect point |
| Large and on-map counters | Bespoke counter evidence is recorded in `runtime/counter_handoff.md` | Existing counter definitions and DDS files remain installed | Provider package complete; live display acceptance pending |
| Provider-to-runtime file boundary | Promotion handoff records byte-identical copies and hashes in commit `0e724fb8a` | Runtime consumers use `gfx` and `sound` paths outside `docs/assets` | Static promotion recorded; live consumer acceptance pending |

The provider package was routed through `chaosx_3d_model_pipeline`. Static registration is not provider evidence, and neither provider evidence nor static registration constitutes live in-game acceptance.

Historical V8, V10, V11, KayKit, and Quaternius crosswalks remain retained for rejection and provenance history only; they do not describe the current runtime state.

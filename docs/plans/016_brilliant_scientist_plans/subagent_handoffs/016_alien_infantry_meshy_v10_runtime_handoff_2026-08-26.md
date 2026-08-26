# Event 016 alien infantry Meshy V10 runtime handoff

> Superseded by the Meshy V13 package and static runtime promotion recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`; retain this file for V10 rejection evidence only.

## Outcome

The requested complete reusable `alien_infantry_entity` package is **blocked**, not complete. Meshy 7 produced a faithful firearm-bearing model, a stable humanoid rig, and genuine accepted source clips for idle, move, defend, retreat, and death. Meshy did not produce a compliant `laser_attack` or `support_attack`, and the 24-bone rig has no verified muzzle locator. No fake action, semantic alias, manual/procedural Blender motion, inferred locator, or partial entity completion claim was made.

The authoritative attempt record is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/rejections/generation_user_source_recovery_v10_firearm_capability.md`.

## Dependency and route evidence

- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK 1.29.0, compatibility revision `meshy-7-v5`.
- Live schema exposed exact `meshy-7` and the locked `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate` routes.
- Blender 5.1.2, build `ec6e62d40fa9`.
- `chaosx_blender_hoi4` 1.10.14; health request `33c188c4b93446958b7a9259a5cf04ac`; socket `127.0.0.1:9876` independently verified listening.
- io_pdx_mesh 0.91.0; locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Dependency lock SHA-256 `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`.
- Meshy schema lock SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- Blender adapter config SHA-256 `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- `python .tools/3d_pipeline/verify_environment.py --probe-meshy` returned zero findings before paid work.

## Source and provider lineage

The sole input was the user-provided 720x720 grayscale clay reference, preserved at `refs/source/user_supplied_alien_reference.png`, SHA-256 `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`. It exactly matches the supplied temporary file. Source mode is user-supplied, reference-only, and explicitly authorized for this attempt. There is no Internet source URL, named creator, or external license to report. It is non-shipping provenance evidence.

No ImageGen refinement was used. Meshy received the exact source with image enhancement disabled and only the approved material prompt recorded in the authoritative rejection report. Visual comparison passed for the alien identity, pose, uniform, boots, free left arm, right-hand pistol grip, weapon silhouette, and visible muzzle.

Provider lineage and credits:

- Generation `01a03a00-e325-7edd-8f68-8452634ab806`: 30 credits.
- Remesh `01a03a06-59a2-70db-987b-e0d5ac85b84e`: 5 credits.
- Rig `01a03a0c-d468-7725-a48e-3352eed26db8`: 5 credits.
- Rejected firing tests: action 4 task `01a03a11-e098-7486-8ee2-eb72a3073805`, action 104 task `01a03a14-1042-791b-9758-132d66b6743d`, action 98 task `01a03a16-a25f-7aca-9654-1dd029dc85c1`; 9 credits total.
- Accepted paid roles: death 183 task `01a03a18-63da-7ab2-8bbe-1cd106ccb312`, idle 0 task `01a03a1a-38b5-7b6e-8c1b-0ca74ffd452c`, defend 2 task `01a03a1c-5718-7215-9721-cec7a91073f3`, retreat 688 task `01a03a1e-ac62-7cb2-b1f0-0865c2fb9d82`; 12 credits total.
- Move is the genuine walking artifact included in the rig at zero additional credits.
- Initial live balance: 76. Final live balance: 15. Total V10 consumption: 61 credits.

## Geometry, scale, rig, and action result

The selected vanilla precedent is installed `gfx/models/units/western_european_infantry.mesh` with entity precedent `gfx/entities/units_infantry.asset#infantry_rifle_entity`. The package copy is `blender/reference/western_european_infantry.mesh`. The exact source height is 7.3518242835, entity scale is 0.8, effective runtime height is 5.8814594268, forward is -Y, and up is +Z. V10 applies the entity scale exactly once.

Neutral rig adapter request `a74750ee3e514a4188d975d087564107` reports 101,136 triangles, 50,609 vertices, 24 bones, 68 non-manifold edges, 172 loose boundary edges, no negative-scale objects, no degenerate faces, and no zero-weight deforming vertices. The persisted mesh height is 7.3518238068 and effective runtime height is 5.8814590454. The pistol remains genuinely integrated with the skinned mesh and stable in the accepted previews.

Accepted source roles:

- `alien_infantry_idle`: Meshy action 0, 121 frames at 30 FPS, loop, in place. Source FBX SHA-256 `5888197AD4ED3EF43C1517DE46A7E33A3488673873A13E18EDD3A93271EC803C`.
- `alien_infantry_move`: Meshy rig walking artifact, 32 frames at 30 FPS, loop, root translation normalized in place. Source FBX SHA-256 `8C11739661713AFA28AB9E989F36074D2CF2FCCD96A56C72CF2C6785E4D912E4`.
- `alien_infantry_defend`: Meshy action 2 `Alert`, 121 frames at 30 FPS, loop, in place. Source FBX SHA-256 `AD1EF84E8C38BDF8A0DF4B7CC258E6C16393DCFFA91533ED4F8AE7072A27132E`.
- `alien_infantry_retreat`: Meshy action 688, 53 frames at 30 FPS, loop, in place. Source FBX SHA-256 `76F0E3006AA8E44787D6549258A827C4B0A24797A06605C732B4A0492B32C12B`.
- `alien_infantry_death`: Meshy action 183, 106 frames at 30 FPS, one-shot. Source FBX SHA-256 `F6B68CDC5E1563A385341A735DC6380B87C186FCAD48FD3CAE04DC96361190E1`.

Blocked roles:

- `alien_infantry_laser_attack`: actions 4, 104, and 98 all fail the aim-discharge-recoil-recovery gate.
- `alien_infantry_support_attack`: no distinct accepted firing source exists; action 98 is rejected and is not aliased.
- `muzzle`: absent from the provider's 24-bone rig; no stable locator or equivalent attachment point was verified.

Exact action FBX hashes, adapter request IDs, action hashes, phase-frame reviews, and rejection reasons are in the authoritative V10 report. Previews are under `blender/previews/alien_infantry_v10_*` and protected source checkpoints are under `blender/source/alien_infantry_v10_*_provider_source.blend`.

## Materials, export, and reimport

Provider generation/remesh textures were immediately downloaded under `provider/downloads/generation_user_source_recovery_v10_textures/` and `provider/downloads/remesh_user_source_recovery_v10_textures/`. They were not promoted into a packed <=1024 PDX DDS material set because the required firing and locator gates failed.

No V10 `.mesh` or `.anim` was exported, and no V10 io_pdx_mesh actual-byte reimport exists. This missing evidence is an explicit blocker, not a skipped success claim. Earlier professional-source/Quaternius exports are historical rejected/fallback evidence and are not accepted for this Meshy-only attempt.

Reserved parent-owned runtime identifiers remain `alien_infantry_mesh`, `alien_infantry_entity`, `alien_infantry_idle`, `alien_infantry_move`, `alien_infantry_laser_attack`, `alien_infantry_defend`, `alien_infantry_support_attack`, `alien_infantry_retreat`, `alien_infantry_death`, `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire`. None is newly wired by this tranche.

## Audio synchronization

The existing sourced audio package is preserved in `evidence/audio/provenance/audio_sources.json` and `runtime/sound_handoff.md`. All four derived files remain mono 44.1 kHz signed 16-bit PCM.

- Laser: OpenGameArt `Space Laser`, bart, CC0, source page `https://opengameart.org/content/space-laser`; original SHA-256 `3A26ECAB8F36DCA14A91519657E60351566A268D28A2EC4F933B0F9718A7258D`; derived SHA-256 `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770`. Deliberately unbound because there is no accepted discharge frame or muzzle locator.
- Movement: OpenGameArt `Footsteps: 01-footstep`, GboxMikeFozzy, CC0, source page `https://opengameart.org/content/footsteps-0`; original SHA-256 `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC`; derived SHA-256 `E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E`. Candidate consumer is move/retreat foot contact, but exact exported event frames are not promoted without final `.anim` bytes.
- Idle: OpenGameArt `Sci-Fi Vehicle Sound`, Ogrebane, CC0, source page `https://opengameart.org/content/sci-fi-vehicle-sound`; original SHA-256 `46AB090FAE668CD83D613019EBC42F8F24B4C511572F4EAC024AD5006680E350`; derived SHA-256 `B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A`. Candidate consumer is idle-state entry as a one-shot; looping remains blocked pending seam audit.
- Death: OpenGameArt `Various Sound Effects: snd_death1`, Julie Damsgaard / Spring Spring / Spring Enterprises, CC0, source page `https://opengameart.org/content/various-sound-effects-0`; original SHA-256 `9216E8A1E252765392CB30637489F8E58831280B1139FA5E2E916B79E375C916`; derived SHA-256 `AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B`. Candidate consumer is the death reaction/impact, but exact exported event frame remains pending final `.anim` bytes.

Country/global infantry selection and acknowledgement voices were not replaced. Existing global TAG infantry voice consumers are not safe for a subunit that may coexist with ordinary infantry.

## Counter reconciliation

The bespoke counters already exist and were not overwritten:

- Registered consumer file: `interface/alien_infantry_system.gfx`.
- Large token: `unit_alien_infantry_icon`; `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds`, 152x42, two frames, SHA-256 `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`.
- On-map token: `onmap_unit_alien_infantry_icon`; `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, 60x12, two frames, SHA-256 `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`.
- Installed definition precedent: `interface/subuniticons.gfx`.
- Matching skill-local reference families: `units/land/counters_large/` and `units/land/map_counters/`.
- Parent/user retains final live visual review and GFX/runtime ownership.

## Files created and preserved

- New V10 provider GLB/FBX/texture downloads under `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/downloads/`.
- New protected Blender sources and multi-frame previews under `blender/source/` and `blender/previews/`.
- New adapter request/result evidence under `logs/adapter/`.
- New authoritative provider report: `provider/rejections/generation_user_source_recovery_v10_firearm_capability.md`.
- This handoff: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_v10_runtime_handoff_2026-08-26.md`.

The adapter also preserved one safe failed request, `logs/adapter/865c0422c36e45ee918e300f56247447.result.json`, where an absolute vanilla path violated the job boundary before any model mutation. It is retained as failure evidence.

## Simplifications, omissions, and blockers

- Complete entity package: blocked.
- Genuine `laser_attack`: blocked by Meshy preset semantic capability after three distinct actions.
- Genuine distinct `support_attack`: blocked; no alias accepted.
- Stable muzzle locator/equivalent: absent from the 24-bone rig and unavailable through the locked adapter route.
- Particle/light/laser-audio synchronization: blocked by the missing accepted firing action and locator.
- Packed PDX DDS materials: not produced after the firing gate failed.
- Final `.mesh`, seven `.anim` files, export hashes, and actual-byte reimports: absent by design; partial/fake completion was not staged.
- Live runtime and in-game validation: parent/user-owned and not claimed.

Remaining recovery requires a Meshy/provider capability change that yields both compliant firearm clips and a verifiable locator path, or a new explicit user decision broadening the permitted source route. The current 15-credit balance is sufficient for five animation calls but does not remove the demonstrated capability blocker. Do not wire historical professional-source or transform-only substitutes into this V10 package.

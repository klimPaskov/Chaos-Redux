# Event 014 Bone Riders paid v9 handoff

Historical supersession notice: this paid v9 recovery record is retained for provider, adapter, cost, and provenance evidence only. The 2026-08-26 approved visual-reuse decision assigns Bone Riders vanilla `sprite = cavalry`, removes the custom model/action/provider requirement, and makes the former adapter blocker non-current.

Historical status: incomplete and blocked because the callable Blender HOI4 MCP process remained adapter 1.10.3 while the repository-authoritative lock was 1.10.7. The approved professional horse source, conditional Meshy rider source plan, sourced-audio package, and counter package are preserved as historical evidence.

## Adapter 1.10.7 resume audit — 2026-08-24

Repository recovery is authoritative at adapter 1.10.7 commit `a3e0a1497b6926b025070267eb9c75bd00b77c93`, with registration commit `7e3af24ac4af87b12cd49c782d89f998d7fab915`. The current dependency lock resolves 1.10.7 and the environment verifier returns zero findings.

The live MCP process did not reload. Health request `fe776868337d4ce1ae9e98a07ad62228` reports adapter 1.10.3, and the callable registry still exposes only 11 legacy tools. It omits `segment_creature_components`, `calibrate_creature_scale`, `import_animation_action`, `retime_animation_action`, `correct_action_grounding`, and `sanitize_runtime_candidate`; its `prepare_candidate` schema also lacks the 1.10.7 compound-preparation surface.

This is the exact current blocker. The installed vanilla frame/horse/`Saddle_Node` rider architecture can preserve independent actions without merging them, but the stale live registry cannot segment the bespoke geometry or transfer and validate the approved professional horse and rider sources into separate exportable children. Local authored motion, static substitution, aliasing, and merged compound actions remain forbidden. No Meshy animation call was made, so this resume tranche consumed zero credits; total historical spend remains 35 and the planned 24-credit rider tranche remains paused.

Evidence is `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/evidence/adapter_1_10_7_reload_gate_2026-08-24.md`. Restart or reload Codex MCP, require live health 1.10.7 plus the full registered operation surface, then rerun the dependency gate before spending.

## Approved professional-source recovery addendum — 2026-08-24

The parent approved the Mesh2Motion `mesh2motion-assets` horse library at commit `6bab14fa197957bf7851477cad0c372960a48824` as the professional quadruped source under CC0-1.0.
The exact GitHub source trees, LICENSE bytes, Blender source files, consolidated GLB, action inventory, and SHA-256 hashes are archived under `provider/external_animation/mesh2motion_horse/`.
The source audit is `evidence/mesh2motion_horse_action_audit.md`.

The self-contained GLB exposes one 56-bone horse rig and 15 genuine multi-frame actions.
Eight distinct horse mappings passed visual phase review: `Idle`, `Run`, `Rear`, `Kick`, `Head_But`, `Trot`, `Eating`, and `Death` for idle, move, attack, defend, support_attack, retreat, training, and death respectively.
These are approved sources, not yet transferred runtime actions.

The official Meshy animation library was exhaustively searched and archived under `provider/meshy_rider_action_research/`.
No explicit sling, stone, lasso, whip, discus, mounted, horseback, or seated-projectile preset exists.
The conditionally approved eight-action rider plan is documented in `evidence/meshy_rider_action_research.md`.
Its combat pair is action 280 `Female_Crouch_Pick_Throw_Forward` for attack and action 393 `baseball_pitching` for support_attack, both upper-body-only retargets that are acceptable only if the bespoke sling and pouch remain visible and the mounted previews read as two distinct sling-stone volleys with load, release, follow-through, and recovery.
No rider action spend has occurred; the planned tranche is 24 credits and the latest verified balance is 587.

Installed vanilla `gfx/entities/units_cavalry.asset` proves that HOI4 cavalry uses a separate frame, horse, and saddle-attached rider architecture.
The exact installed file is archived at `evidence/vanilla/units_cavalry.asset`, SHA-256 `5AC30F2E98F29A95A56675AE19E51C3C4FAD7B2F1B6453F6AA0C7D6415696AE6`, and the line-specific implementation consequence is recorded in `evidence/vanilla_cavalry_entity_architecture.md`.
The former v9 recovery plan would have exported separate bespoke horse and rider meshes/actions and attached the rider at an audited horse `Saddle_Node`; that plan is superseded by the approved vanilla `sprite = cavalry` decision and must not be resumed without a new parent scope decision.

Processing is paused at the adapter route gate.
The live process exposed adapter 1.10.3 health but omitted required structured segmentation, sourced retarget, calibration, grounding, and weight-sanitize tools.
Registration recovery commit `7e3af24ac` requires a fresh Codex/MCP process before those operations become callable.
An unrelated uncommitted adapter/lock 1.10.4 state is not authoritative and was not created or modified by this worker.
No shell Blender workaround, authored substitute motion, merged compound action, or runtime fallback was used.

## Outcome

The accepted Meshy 7 geometry remains visually approved and unchanged: one living pale horse, one painted skull-masked living rider, skull/rib/long-bone barding, loaded sling and stone pouch. Generation task `01a03404-f74d-7d5b-876d-5f426afe11f6` consumed 30 credits; remesh task `01a03418-57e3-7399-bf55-2d769bedabee` consumed 5. Total consumed credits remain 35.

The sole approved Meshy input is `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/refs/original/meshy_input.png`, SHA-256 `16C02D09E025CF3548BAF7BA390B37656448CF3A04D0A85689B350870C2D4E89`. Generation downloads are GLB `EA2E4E40B88BD67DE45AC0964305786602499902CEC584A12DE666794AD38E4E` and FBX `66A8EB69F7D1995B52141400B79D9C4F89FC97B85BFF140FED6F64ADC196C79D`. Remesh downloads are GLB `D105CAC2E1D1CC0C37D420FB6E54776D0F15B68126015A3AB734F8900497C348` and FBX `90ED7511BEAC37D76A1032B2E673D27F80A224061C701F4B9B183C25EF95B743`. The approved local geometry checkpoint is 90,000 triangles and 44,670 vertices with zero remaining boundary/non-manifold/loose/degenerate defects and SHA-256 `0DC4A64B675735B45126CA93953CD81853E4389E564DEA808339D6A836EE3617`.

The live locked environment passes with official Meshy MCP 0.4.0, exact `meshy-7`, balance 1320, adapter 1.10.0, Blender 5.1.2, io_pdx_mesh 0.91.0, and a listening Blender bridge. Meshy's current official rigging endpoint supports standard humanoid bipeds and explicitly excludes nonhumanoid assets. Its animation endpoint requires a successful Meshy rig task ID. Splitting the accepted geometry can make only the rider eligible; it cannot produce Meshy-sourced quadruped horse motion. A rider-only animation over a static or locally keyed horse would violate the mounted-safe action brief.

No extra paid recovery was attempted because the live provider contract proves the missing horse capability. No Blender-authored action, transform-only clip, static alias, semantic reuse, unrelated model, or silent vanilla horse-motion substitution was used. All eight roles remain blocked: idle, move, attack, defend, support_attack, retreat, training, and death. Therefore no valid final armature/weights, PDX textures, `.mesh`, `.anim`, export, or reimport exists.

## Completed stone-impact audio

- Source page: `https://commons.wikimedia.org/wiki/File:Grinding_and_tapping_ro.ogg`.
- Direct download: `https://upload.wikimedia.org/wikipedia/commons/3/35/Grinding_and_tapping_ro.ogg`.
- Title: *Grinding and tapping Rocks*.
- Creator: stilgar / PDSounds.org, transferred to Commons by Fæ.
- Terms: public-domain dedication; unrestricted use stated on the Commons description page.
- Retrieved: 2026-08-24.
- Original: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/audio/sources/original/stone_impact_taps.ogg`, SHA-256 `B12D320A30327099A661E4BAECC2E23FFA5B8A03C9B60199783B24D74789A5EE`.
- Archived source page: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/audio/evidence/source_pages/stone_impact_taps.ogg.html`, SHA-256 `5FE9F7AAE73B2587D8D4CE97E5939BB7AC27103115F3C186C80D2D40F4FE7484`.
- Derived: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/audio/derived/stone_impact.wav`, SHA-256 `F36A4426138E4F5D546EE6D17E8A5D902B59C962A45A1956630FE5E23EFD0BAE`.
- Transformation: trim 43.35-44.30 seconds, 5 ms fade-in, 100 ms fade-out from 0.85 seconds, loudness normalize to I=-20 LUFS / TP=-2 dB / LRA=5, encode PCM S16LE 44100 Hz mono with metadata removed.
- Probe: 0.950 seconds, signed 16-bit PCM, 44100 Hz, mono, peak -2.0 dB.
- Proposed identifier: `cannibal_bone_riders_stone_impact`.
- Synchronization: projectile-contact phase after sling release for attack and support_attack; exact frame remains blocked until compliant skeletal actions exist.

## Dependency evidence

- `dependencies.lock.json`: `58FA9FC6486FDA304FDC344962C63ADD276938E2D4402D0E44ACA02A392F1286`.
- `meshy_tool_schema.lock.json`: `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- `blender_hoi4_adapter.json`: `1ADD938E9FCECB9410AA0430629A4E78E956ADB78362004E075481D6484081BB`.
- Clean environment report: `62059171D51622F8BBC39078CBB58A35CB3927C3FD885AD1B55C58894B7F25DC`.
- Detailed report: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/evidence/final_v9_dependency_and_capability_report.md`.

## Counter and parent-owned runtime work

The existing bespoke vanilla-green counter package remains valid for `GFX_unit_cannibal_bone_riders_icon_medium`, `GFX_unit_cannibal_bone_riders_icon_medium_white`, and `GFX_unit_cannibal_bone_riders_icon_small`; its large, small, and texticon DDS files pass exact decoded roundtrip validation. Installed definitions were `interface/subuniticons.gfx#GFX_unit_cavalry_icon_medium`, `interface/subuniticons.gfx#GFX_unit_cavalry_icon_medium_white`, and `interface/texticons.gfx#GFX_unit_cavalry_icon_small`. Installed DDS references were `gfx/interface/counters/divisions_large/unit_cavalry_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_cavalry_icon.dds`, and `gfx/texticons/unit_cavalry_icon_small.dds`; full hashes, frame bounds, alpha, headers, and sampled vanilla-green treatment are retained in `docs/assets/014_cannibalism/counters/irregular_units/validation/cavalry_reference_gate.json` and `visible_bounds.json`.

Final counter DDS hashes are `FA0CA9F1E5FEC9931B89DCA0E29843720F0E9D15C9A8D3372D5E2D60B5B15504` for the 152x42 large strip, `BABF1034AE0180B890A2EBB38E78C2A6228264E58E33E84439801EFF22DBA5FD` for the 60x12 on-map strip, and `3799FB8E85B608800529EB8CFB879114756A214A24006D86C16882226055A304` for the 60x12 texticon strip. Parent-owned GFX/entity/sound-definition/runtime wiring and live in-game validation remain pending. Do not wire the 3D model as complete.

## Files created or changed

- Added the public-domain original, archived source page, and PCM derivative under `audio/`.
- Updated `job.yaml`, `manifest.md`, `history.jsonl`, `runtime/handoff.md`, `evidence/action_manifest.md`, and `audio/audio_manifest.md` inside the deterministic job root.
- Added `evidence/final_v9_dependency_and_capability_report.md`.
- Added this exact parent handoff, `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_bone_riders_paid_v9.md`.

## Meaningful validation and skipped validation

The final audio was probed with FFprobe for codec, sample rate, channels, bit depth, and duration, then checked with FFmpeg volume detection for peak level. The current dependency lock, Meshy schema, adapter checksums, Blender build, io_pdx_mesh archive and manifest, live Meshy balance, exact `meshy-7` declaration, wrapper cleanup, and Blender bridge port were reverified. The official Meshy rigging and animation contracts were checked against the live schema. No animation preview, `.mesh`/`.anim` export, reimport, material DDS packing, action synchronization, deformation test, or runtime hash synchronization was performed because no compliant horse rig/action source exists; running those checks would falsely imply an approved skeleton or action set.

## Simplifications, omissions, and blockers

No simplification or substitute was used. The eight actions, final rig/weights, PDX textures, `.mesh`, eight `.anim` files, export, and reimport remain absent because the required Meshy quadruped/mounted motion source does not exist in the verified provider surface. Resolution requires either a future Meshy capability or explicit user approval of a professional mounted animation source.

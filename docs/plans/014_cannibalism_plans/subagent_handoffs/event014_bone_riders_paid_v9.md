# Event 014 Bone Riders paid v9 handoff

Status: incomplete and blocked at a verified Meshy quadruped/mounted-motion capability boundary. The independent sourced-audio package is complete.

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

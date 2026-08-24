# Event 014 Bone Riders final v8 handoff

Status: incomplete and explicitly blocked at the Meshy compound-rig capability gate.

## Completed

- Selected the user-authorized modern fictional Tatyana Kupriyanova reference and retained it as non-shipping evidence.
- Produced exactly one approved RGBA Meshy input, `refs/original/meshy_input.png`, SHA-256 `16C02D09E025CF3548BAF7BA390B37656448CF3A04D0A85689B350870C2D4E89`. The parent approved this exact checksum.
- Generated one Meshy 7 mounted unit: task `01a03404-f74d-7d5b-876d-5f426afe11f6`, 30 credits.
- Immediately downloaded GLB `EA2E4E40B88BD67DE45AC0964305786602499902CEC584A12DE666794AD38E4E` and FBX `66A8EB69F7D1995B52141400B79D9C4F89FC97B85BFF140FED6F64ADC196C79D`.
- Used adapter 1.10.0 and Blender 5.1.2 only for Blender work. The clean working geometry is exactly 90,000 triangles, 44,670 vertices, closed, triangular, UV-mapped, non-negative, and free of non-manifold, loose, or degenerate geometry.
- Created protected Blender source/checkpoints and seven previews. Visual review confirms the living painted rider, living horse, loaded sling, stone pouch, skull/rib/long-bone barding, four complete legs, coherent mounted silhouette, and absence of prohibited weapons/motifs.
- Measured against installed `cavalry_horse.mesh` and `cavalry_frame.mesh`, retaining pdxmesh scale 0.45 as one scale layer.
- Sourced and mechanically converted five licensed audio candidates to PCM S16LE 44100 Hz mono: selection/horse idle, hoof movement, sling release, training/rider acknowledgement, and rider death.
- Reaudited the existing bespoke green counter package. Its large, small, and texticon DDS files all pass exact two-frame decoded roundtrip validation.

## Provider recovery and blocker

The original provider result contained 1,994,058 faces, so Meshy rejected the first rig request before billing. A live balance of 25 credits supported the authorized recovery. Remesh task `01a03418-57e3-7399-bf55-2d769bedabee` succeeded at 90,000 triangles for 5 credits; its GLB SHA-256 is `D105CAC2E1D1CC0C37D420FB6E54776D0F15B68126015A3AB734F8900497C348` and FBX is `90ED7511BEAC37D76A1032B2E673D27F80A224061C701F4B9B183C25EF95B743`.

With a live balance of 20, the second Meshy rig request failed before billing with HTTP 422: `Pose estimation failed, please provide a valid model`. Meshy’s standard pose estimator cannot coherently rig this dynamic compound horse+rider. There is therefore no valid `rig_task_id` for `meshy_animate`.

The required idle, move/gallop, attack/sling, defend, support_attack, retreat, training, and death actions are all blocked. No Blender-authored action, static alias, transform-only action, or semantic reuse was substituted. Consequently no final armature, weights, HOI4 `.mesh`, eight `.anim` files, DDS model textures, io_pdx_mesh export, or reimport is claimed.

The audio stone-impact role also remains blocked because the bounded licensed-source search did not find a semantically defensible candidate. Sound-to-animation synchronization remains provisional because action frame ranges do not exist.

## Dependencies and spend

- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` 0.4.0; SDK 1.29.0; exact model `meshy-7`.
- Blender adapter: `chaosx_blender_hoi4` 1.10.0.
- Blender: 5.1.2 build `ec6e62d40fa9`.
- io_pdx_mesh: 0.91.0, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Credits consumed: 35 total—30 generation and 5 remesh. Rig failures consumed zero. No animation credits were spent.
- The transient verifier wrapper/Node children exited naturally; the second environment probe was clean. This was documented as the known transient cleanup defect, not a permanent blocker.

## Parent work

Do not wire the model as complete. Resolution requires either a future Meshy capability that supports coherent compound mounted rigs and all eight substantive actions, or an explicitly user-approved professional mounted animation source compatible with the prepared geometry. The parent retains entity, GFX, sound-definition, runtime, and live in-game validation ownership.

Package evidence: `docs/assets/014_cannibalism/models_3d/cannibal_bone_riders/manifest.md`, `job.yaml`, `evidence/final_v8_dependency_and_provider_report.md`, `evidence/action_manifest.md`, `audio/audio_manifest.md`, and `runtime/handoff.md`.

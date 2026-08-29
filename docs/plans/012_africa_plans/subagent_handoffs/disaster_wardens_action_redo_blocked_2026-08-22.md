# Disaster Wardens action-redo handoff

Status: `blocked_session_restart_required`.

## Outcome

The deterministic package remains ready for a clean Meshy 7 T-pose regeneration, but this task stopped before paid work because its Codex MCP inventory was created before adapter `1.8.2` became available. A standalone fresh adapter `tools/list` probe passes and exposes the three required bounded operations, while this already-running Codex task still exposes the stale callable inventory.

The body is a standard humanoid biped and must use a Meshy humanoid rig. The installed consumer requires ten distinct semantic roles: `attack`, `defend`, `support_attack`, `move`, `retreat`, `deploy`, `supply_load`, `death`, `idle`, and `training`. Every role still requires its own credible `meshy_animate` source; no local motion, transform-only clip, static pose, alias, or semantic reuse is permitted.

## Fresh preflight evidence

- `MESHY_API_KEY`: present and non-blank; value was not exposed.
- Approved provider input: `docs/assets/012_africa/models_3d/disaster_wardens/refs/original/meshy_input.png`.
- Approved input SHA-256: `40D9D93F5CEEB3801FD0A610390070915CEB9B492FD54460B44F28FB06AA0616`; verified exact match.
- Approved input size: `1,984,988` bytes.
- Live Meshy balance: `724` credits.
- Live Meshy image-to-3D schema: exact `ai_model = meshy-7` is exposed together with local `file_path` and `pose_mode = t-pose`.
- Locked Meshy MCP: official `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility SDK `1.29.0`, compatibility revision `meshy-7-v4`.
- Locked Blender: `5.1.2`, build `ec6e62d40fa9`.
- Locked Blender HOI4 adapter: `chaosx_blender_hoi4` `1.8.2`.
- Locked `io_pdx_mesh`: `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Standalone fresh adapter `tools/list`: pass for `chaosx_blender_hoi4_import_animation_action`, `chaosx_blender_hoi4_retime_animation_action`, and `chaosx_blender_hoi4_correct_action_grounding`.
- Current Codex task callable inventory: stale; those three tools are absent even though the locked source and standalone fresh process expose them.

## Provider and credit status

- Geometry task started: `no`.
- Provider task ID: none.
- Credits consumed in this continuation: `0`.
- Planned first tranche after restart: `30` credits for textured Meshy 7 image-to-3D using the approved one-image input and `t-pose`.
- Planned later tranche, only after the geometry visual gate is accepted: `5` credits for Meshy humanoid rigging and `3` credits for each of the ten distinct required `meshy_animate` roles.
- Failure-driven extra recovery remains unapproved and must be confirmed after any rejected paid attempt.

## Files changed in this continuation

- Updated this handoff only: `docs/plans/012_africa_plans/subagent_handoffs/disaster_wardens_action_redo_blocked_2026-08-22.md`.

No model-package file, provider request, runtime model, gameplay file, entity, GFX, localisation, sound definition, skill, tool, or Qoder file was edited. No runtime synchronization was attempted.

## Blocker and resume action

Restart the MCP/Codex session or begin a new task turn that rebuilds the Blender HOI4 callable inventory from adapter `1.8.2`. Before the 30-credit geometry call, live-list the three exact operations again inside that new callable session and record their current schemas. Then resume this same deterministic job from the approved image; do not restore quarantined Meshy 6 geometry or locally authored legacy actions, and do not synchronize runtime files until all ten dedicated provider-sourced actions have passed Blender import, retime/grounding where required, PDX export, actual-byte reimport, and visual QA.

## Simplifications, omissions, and blockers

No fallback or simplification was used. Geometry generation, visual gating, remesh decision, rigging, all ten animation roles, Blender processing, PDX export/reimport, and runtime handoff refresh remain unperformed because the current task inventory is stale.

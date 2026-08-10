# Event 016 3D adapter lock-guidance maintenance handoff

Date: 2026-08-05

Scope: reusable 3D skill and custom-agent guidance only, plus this handoff. No gameplay, runtime asset, adapter configuration, or dependency-lock file was edited.

## Completed changes

- Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` so every adapter-version record is read from `routes.blender_hoi4_adapter.version` in `.tools/3d_pipeline/config/dependencies.lock.json`.
- Updated `.codex/agents/chaosx_3d_model_pipeline.toml` to name the same lock property while preserving the parent edit that removed the stale fixed adapter version.
- Kept the skill's `resolution_policy = latest_at_bootstrap` guidance and fail-closed behavior for missing, mismatched, or unverifiable routes.
- Added bridge recovery guidance to the skill and agent: a running Blender process is not bridge evidence; probe `127.0.0.1:<socket_port>` using `blender_mcp_addon.socket_port` from the lock and, when absent, launch the lock-selected executable in hidden background mode with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port <socket_port>`, then probe and record the result.

## Lock evidence

At audit time, `.tools/3d_pipeline/config/dependencies.lock.json` resolved `chaosx_blender_hoi4` to `1.2.0` under `routes.blender_hoi4_adapter.version`. The lock SHA-256 was `F84BC430746C016888D3AEFE2D5ED2969E5E5B8CF90D7EEBD52EB9C49DB08431`. This is point-in-time evidence only; future runs must reread the lock rather than copy this value into guidance.

## Related surface reconciliation

The parent also updated `.tools/3d_pipeline/README.md` to defer adapter, Blender, Meshy, Blender Lab MCP, and `io_pdx_mesh` versions and checksums to the dependency lock. No fixed adapter-version literal remains in the inspected 3D skill, agent, or pipeline README guidance.

## Validation

- Parsed `.tools/3d_pipeline/config/dependencies.lock.json` with PowerShell `ConvertFrom-Json` and confirmed the adapter id, version, and lock checksum.
- Searched the scoped 3D skill and agent files for fixed `chaosx_blender_hoi4` version literals; none remain after the patch.
- Reviewed `.tools/3d_pipeline/README.md` after the parent reconciliation and confirmed it now defers adapter versions to the lock.
- Parsed `.codex/agents/chaosx_3d_model_pipeline.toml` with Python TOML support and confirmed the lock-property and bridge-recovery guidance are present.
- Inspected the lock's `blender_mcp_addon.socket_port` (`9876`) and the installed/vendor Blender MCP add-on CLI/server sources, which confirm the `blender_mcp` command and default bridge port used in the recovery guidance.
- Ran `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-3d-model-pipeline`; it returned `Skill is valid!`.
- No MCP, gameplay, runtime, provider, Blender, or in-game validation was attempted because this was a documentation-only maintenance patch.

## Remaining risk

The bridge command and endpoint are documented from the verified installed route, but no live bridge probe was rerun during this documentation-only pass. Runtime verification remains parent-owned.

# Event 012 Oracle Recon 3D subagent handoff

Superseded by `012_africa_models_runtime_completion_2026-08-06.md`; the complete package is at `docs/assets/012_africa/models_3d/oracle_recon/`.

Status: `blocked` at dependency verification. The model package is incomplete.

## Outcome

The credential gate passed, but the mandatory live repository-owned Blender HOI4 adapter health gate failed before reference generation, balance inspection, or provider work. The locked files correctly map `oracle_recon` to `docs/assets/012_africa/models_3d/oracle_recon`; the live adapter instead attempted the generic pilot root. This route/configuration mismatch forbids all downstream work and cannot be replaced with unrestricted Blender Python or another Blender route.

## Files created

- `docs/assets/012_africa/models_3d/oracle_recon/job.yaml`
- `docs/assets/012_africa/models_3d/oracle_recon/history.jsonl`
- `docs/assets/012_africa/models_3d/oracle_recon/manifest.md`
- `docs/assets/012_africa/models_3d/oracle_recon/evidence/dependency_lock_verification.md`
- `docs/assets/012_africa/models_3d/oracle_recon/validation/blocked_dependency_gate.md`
- `docs/assets/012_africa/models_3d/oracle_recon/runtime/handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_model_oracle_recon_2026-08-06.md`

No gameplay, GFX, `.asset`, entity, sound-definition, localisation, spreadsheet, or runtime asset file was edited.

## Source and provider lineage

- Reference source: not generated because the dependency gate failed.
- Reference prompt/hash: absent.
- Provider requests/responses/tasks/downloads: none.
- Credits estimated for executed tranches: `0`.
- Credits consumed: `0`.
- Extra recovery attempts: none; limits remain zero.

## Verified dependencies

- Meshy MCP lock: `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Blender: `5.1.2`, build commit `ec6e62d40fa9`.
- Blender MCP add-on: `1.0.0`; bridge port `9876` listening.
- Blender HOI4 adapter lock: `1.2.2`.
- io_pdx_mesh manifest: `0.91.0`.
- Exact lock and manifest checksums are recorded in the job manifest and dependency evidence.

## Geometry, material, rig, action, and export results

All are `blocked` and absent. No `.mesh` or `.anim` was created, so no reimport or parser proof exists. No scale crosswalk was fabricated; the required installed-vanilla measurement remains pending.

## Sound package

Blocked before web research. No source URL, attribution, license, original file, derived file, checksum, transformation, or synchronization evidence exists. No generated, synthesized, placeholder, or unlicensed audio was used.

## Counter package

Blocked before production. The accepted tokens and proposed target paths are preserved in the runtime handoff, but installed-DDS palette sampling, frame-state evidence, ImageGen source art, processed PNG, DDS, contact sheet, and `chaosx_icon_artist` handoff/output are absent. No vanilla counter was copied or renamed.

## Required parent action

Restart or reload the live repository-owned `chaosx_blender_hoi4` adapter so it reads the current locked `job_overrides.oracle_recon` mapping. Then verify that `chaosx_blender_hoi4_health(job_id = oracle_recon)` succeeds against the Event 012 job root and resume this exact package. Do not approve a fallback route.

## Simplifications and omissions

No fallback or simplification was used. Every unproduced requirement is explicitly blocked by the adapter job-root mismatch.

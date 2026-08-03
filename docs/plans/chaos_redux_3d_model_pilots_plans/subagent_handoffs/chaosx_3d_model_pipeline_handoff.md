# chaosx_3d_model_pipeline integration handoff

Status: offline runtime repair complete; live renderer proof remains intentionally pending.

## Route

- Skill: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`
- Subagent definition: `.codex/agents/chaosx_3d_model_pipeline.toml`
- Parent routing rule: `AGENTS.md` Repo Skills section
- Required spawn mode: `fork_context=false`
- Job owner: `chaos_redux_3d_model_pilots`
- Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/anomaly_signal_beacon/`

## Parent-owned boundary

The worker route owns provider lineage, Blender checkpoints, PDX exports, texture evidence, reimport proofs, manifests, crosswalks, and handoffs.
The parent implementation owns the narrow runtime registration in `gfx/`, entity state bindings, the building/unit consumers, the isolated showcase consumer, and live-game evidence.
The production files are wired and the isolated consumers are prepared.
The user explicitly waived launching HOI4 and capturing in-game screenshots on 2026-07-22, so no live renderer claim or screenshot checksum is added.

## Corrected runtime evidence

- The active `3d_pipeline` test mod is synchronized against the corrected source runtime files by SHA-256.
- The building consumer is wired to entity `building_anomaly_signal_beacon_pilot`, spawn entity `building_anomaly_signal_beacon_pilot_spawn`, and Brandenburg province 9560.
- The provider mesh retains 31,520 loose boundary edges, which remains an explicit topology review item rather than a claimed hole repair.

## Completed worker evidence

- The beacon pilot has exactly one `refs/original/meshy_input.png`, and no Meshy side sheet or multi-view board exists.
- Meshy generation task IDs, request/response lineage, credits, and local checksums are retained.
- Blender 5.1.2, the allowlisted HOI4 adapter, and checksum-locked `io_pdx_mesh` 0.91.0 produced the corrected `.mesh` and `.anim` candidates.
- The beacon has source/working checkpoints, processed textures, export reports, and reimport proof.

## Remaining proof

The corrected package still needs the user's live renderer recheck for final confirmation of model appearance, movement, topology visibility, and building visibility.
No live-game proof is claimed because the user instructed that HOI4 does not need to be run.

# chaosx_3d_model_pipeline integration handoff

Status: integrated; complete under explicit live-validation waiver.

## Route

- Skill: `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`
- Subagent definition: `.codex/agents/chaosx_3d_model_pipeline.toml`
- Parent routing rule: `AGENTS.md` Repo Skills section
- Required spawn mode: `fork_context=false`
- Job owner: `chaos_redux_3d_model_pilots`
- Job roots: `docs/assets/chaos_redux_3d_model_pilots/models_3d/anomaly_signal_beacon/` and `anomaly_recon_trooper/`

## Parent-owned boundary

The worker route owns provider lineage, Blender checkpoints, PDX exports,
texture evidence, reimport proofs, manifests, crosswalks, and handoffs. The
parent implementation owns the narrow runtime registration in `gfx/`, entity
state bindings, the building/unit consumers, isolated showcase consumer, and
live-game evidence. The production files are wired and the isolated consumers
are prepared. The user explicitly waived launching HOI4 and capturing in-game
screenshots on 2026-07-22, so no live renderer claim or screenshot checksum is
added.

## Completed worker evidence

- Each pilot has exactly one `refs/original/meshy_input.png`; no Meshy side sheet or multi-view board exists.
- Meshy generation and humanoid post-processing task IDs, request/response lineage, credits, and local checksums are retained.
- Blender 5.1.2, the allowlisted HOI4 adapter, and checksum-locked `io_pdx_mesh` 0.91.0 produced the `.mesh`/`.anim` candidates.
- Both pilots have source/working checkpoints, processed textures, export reports, and reimport proof.
- The humanoid uses provider rig/action artifacts fetched from signed `assets.meshy.ai` URLs; exploratory conversion outputs are not final replacements.

## Remaining parent proof

None within the user-authorized scope. A later live-game validation pass may use
the retained isolated showcase, but it is outside this completed handoff.

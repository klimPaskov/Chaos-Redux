# Event 012 gorilla heavy infantry 3D model handoff

Superseded by `012_africa_models_runtime_completion_2026-08-06.md`; the complete package is at `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/`.

Status: `blocked` at dependency verification.

## Outcome

The worker produced and preserved exactly one user-authorized native ImageGen reference image, but did not call Meshy balance or any paid/provider operation. The initial `chaosx_blender_hoi4` health call failed to honor the dependency-lock job override. After the parent restarted the corrected adapter process, a second mandatory health request returned no payload through approximately 55 seconds of bounded waits and was terminated. No fallback route was used.

## Files created

- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/job.yaml`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/history.jsonl`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/manifest.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/original/meshy_input.png`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/original/input_manifest.json`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/refs/briefs/meshy_input_prompt.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/provider/credits/blocked_before_balance.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/evidence/dependency_verification.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/validation/reference_preflight.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/runtime/crosswalk.md`
- `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/runtime/handoff.md`

## Source and lineage

- Source mode: native built-in ImageGen.
- Prompt: `refs/briefs/meshy_input_prompt.md`.
- Reference: `refs/original/meshy_input.png`.
- Reference SHA-256: `50555A252651030F62062AD1A411E89C07423F546F79051E6F30F98E16B083DF`.
- Dimensions: `1180x1333`; bytes: `1,908,934`.
- Authorization: user permitted one generated single view and derived geometry use.
- Meshy tasks/responses: none.
- Credits estimated for executed work: 0; consumed: 0.

## Dependency evidence and blocker

- Official Meshy server lock: `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`.
- Blender: `5.1.2`, build `ec6e62d40fa9`.
- Adapter lock: `chaosx_blender_hoi4` `1.2.2`.
- `io_pdx_mesh`: `0.91.0`, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Independent bridge probe: `127.0.0.1:9876` listening.
- Failed operation: `chaosx_blender_hoi4_health({ job_id: "gorilla_heavy_infantry" })`.
- Actual erroneous root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/gorilla_heavy_infantry`.
- Required locked root: `docs/assets/012_africa/models_3d/gorilla_heavy_infantry`.
- Exact lock checksums and manifest hashes are in `evidence/dependency_verification.md`.

Required installation/verification: reload or repair the live adapter so version `1.2.2` honors `job_overrides.gorilla_heavy_infantry`, then rerun health. Source-only or unrestricted Blender work is not equivalent.

Post-restart retry evidence:

- Retry time: `2026-08-06T18:59:56+03:00`.
- Operation: `chaosx_blender_hoi4_health({ job_id: "gorilla_heavy_infantry" })`.
- Transport result: no MCP response or error payload after approximately 55 seconds; request terminated.
- Independent Blender bridge result after termination: `127.0.0.1:9876` listening.
- New exact blocker: the repository-owned adapter MCP transport remains unresponsive despite the listening Blender bridge.
- Provider/credit state remains unchanged: no balance probe, no provider task, no paid calls, and zero credits consumed.

## Reference and counter inspection completed before the blocker

- Vanilla infantry mesh and three material maps were present and checksummed.
- Vanilla cavalry horse mesh, infantry/cavalry entities, animation asset, sound precedents, `subuniticons.gfx`, and the two infantry counter DDS files were present and checksummed.
- Large infantry counter definition uses `noOfFrames = 2`; installed file path is `gfx/interface/counters/divisions_large/unit_infantry_icon.dds`.
- Small on-map infantry definition uses `noOfFrames = 2`; installed file path is `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.
- Matching skill-local land counter families were named by the brief, but palette extraction and icon-artist production were not continued past the dependency blocker.
- Cave monster precedent was found at the passed path.
- Rat precedent current path is `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh`; the parent-provided `rat_ground_unit_shared.mesh` path is stale.

## Blocked requirements

- Meshy 7 image-to-3D generation and immediate download/checksum.
- Candidate multi-view geometry review, repair, triangulation, and protected source/working checkpoints.
- Measured vanilla source height, 1.35x target-height crosswalk, axes, ground contact, and entity-scale proof.
- PDX material conversion and source/final texture evidence.
- Custom creature rig, weights, deformation audit, and action authoring.
- All four real `.anim` exports and `.mesh` export with reimport/parse proof.
- Legally sourced sound candidates, downloads, licensing, checksums, transformations, and synchronization handoff.
- Bespoke vanilla-green large and on-map counters, palette sampling, ImageGen source evidence, DDS round-trip, contact sheet, and icon-artist handoff.
- Runtime synchronization and gameplay/GFX/entity/sound-definition wiring.

## Required actions and intended synchronization

- `chaosx_gorilla_idle`: 24 fps, frames 0-47, loop, in-place.
- `chaosx_gorilla_move`: 24 fps, frames 0-47, loop, in-place; movement sound phases at frames 0 and 24.
- `chaosx_gorilla_attack`: 24 fps, frames 0-35, non-loop, in-place; attack/impact at frame 18.
- `chaosx_gorilla_recovery`: 24 fps, frames 0-35, non-loop, in-place.
- Death role requested by the sound brief has no matching requested skeletal action; parent must either add a death action to the accepted 3D scope or bind a sourced death cue to an existing final-state event after explicit design review. No substitute was chosen.

## Parent work

1. Restore the repository-owned adapter MCP transport and confirm that health returns successfully for the locked job override; resume this exact job without regenerating the reference unless it is explicitly rejected.
2. Review the reference preflight.
3. After complete exports and companion packages exist, own `.asset`, entity, counter GFX, gameplay, and sound-definition wiring.
4. Perform live-consumer and in-game validation.

## Simplifications, omissions, and blockers

No simplification or fallback was used. All absent model, animation, sound, and counter outputs are explicitly blocked by the mandatory route mismatch. The package is not gameplay-ready.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `imagegen`.

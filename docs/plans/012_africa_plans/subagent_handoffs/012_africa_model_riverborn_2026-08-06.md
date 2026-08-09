# Riverborn 3D model package handoff

Superseded by `012_africa_models_runtime_completion_2026-08-06.md`; the complete package is at `docs/assets/012_africa/models_3d/riverborn/`.

## Status

`blocked` — required Blender HOI4 adapter installation/verification failed before reference generation, Meshy balance inspection, or any paid provider call.

The `MESHY_API_KEY` hard gate passed. The repository dependency locks match the corrected brief, but the callable `chaosx_blender_hoi4` route does not match its locked schema or deterministic Riverborn job mapping. No fallback is authorized.

## Dependency-lock evidence

- `.tools/3d_pipeline/config/dependencies.lock.json`: SHA-256 `D6E29506E02336F8EB888EDAB05FA788F21739AA4FC2672F772A39CE5EB5C8B2`; declares Meshy MCP `0.4.0`, Blender `5.1.2`, Blender HOI4 adapter `1.2.2`, and `io_pdx_mesh` `0.91.0`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: SHA-256 `DBB9CAD7FB12AFE81ECA05A2F381EF4251C035F4D22BF17856A2F6D41F16A62D`; declares schema revision `live-declaration-2026-08-05`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: SHA-256 `88D485D954B727D334146694FA0443D07CD6360097B1B17BFDEE2089D9583DF4`; maps job id `riverborn` to `docs/assets/012_africa/models_3d/riverborn` and allowlists that write root.
- Locked `io_pdx_mesh` archive: SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`, exactly matching the lock.
- Installed `io_pdx_mesh` manifest: SHA-256 `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC`.
- Installed Blender reports `Blender 5.1.2`, build date `2026-05-19`.

## Live-route mismatch

The live adapter exposed only these callable operations:

- `chaosx_blender_hoi4_health`
- `chaosx_blender_hoi4_prepare_candidate`
- `chaosx_blender_hoi4_inspect_scene`
- `chaosx_blender_hoi4_process_textures`
- `chaosx_blender_hoi4_author_locomotion_action`
- `chaosx_blender_hoi4_export_mesh`
- `chaosx_blender_hoi4_export_animation`
- `chaosx_blender_hoi4_reimport_export`
- `chaosx_blender_hoi4_save_checkpoint`

The dependency lock and adapter configuration additionally require nonhuman production operations that are absent from the live route, including `segment_creature_components`, `calibrate_creature_scale`, `author_creature_rig`, `author_creature_action`, `correct_action_grounding`, `offset_action_root`, and `sanitize_runtime_candidate`. These are necessary for the Riverborn custom rig, four real actions, water/ground contact checks, and export sanitation.

The read-only health call with `job_id = riverborn` failed and resolved the job to:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\chaos_redux_3d_model_pilots\models_3d\riverborn`

That is the obsolete default pilot root, not the locked override:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\012_africa\models_3d\riverborn`

This indicates that the callable adapter process is not honoring the current `1.2.2` job override/configuration even though the repository lock is correct.

## Work and costs

- Reference image: not generated; no prompt or image hash exists because the dependency gate failed first.
- Meshy balance: not queried because adapter verification must pass first.
- Provider task lineage: none.
- Credits estimated for executed operations: `0`.
- Credits consumed: `0`.
- Blender checkpoints, geometry, textures, rig, weights, actions, `.mesh`, `.anim`, previews, and reimport proof: not created.
- Internet audio research/download: not started.
- Counter inspection and `chaosx_icon_artist` handoff: not started.
- Runtime synchronization: not started; parent-owned runtime files were not touched.

## Required installation/verification

Restart or repair the repository-owned Blender HOI4 MCP adapter so its live declarations match adapter `1.2.2`, it loads `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, resolves `riverborn` to the locked Event 012 job override, and exposes the locked nonhuman operations. Re-run `chaosx_blender_hoi4_health` for `riverborn` before resuming.

## Skipped meaningful validation

- Blender bridge socket probing/startup was not attempted because the adapter failed job-root containment before a valid Riverborn health result could be established.
- Vanilla mesh measurement, source/reference checksum capture, Meshy schema/balance calls, generation, geometry QA, PDX material conversion, animation contact tests, export, and reimport were not attempted because downstream work is forbidden after a dependency-route mismatch.
- Audio and counter work were not started because the model package cannot enter production until the dependency gate passes.

## Parent work

The parent must restore and verify the locked adapter route, then resume this same deterministic job without changing the reference count, paid-attempt limits, action requirements, sound requirements, counter requirements, or runtime ownership boundary. No gameplay, GFX, entity, sound-definition, localisation, or spreadsheet file was edited.

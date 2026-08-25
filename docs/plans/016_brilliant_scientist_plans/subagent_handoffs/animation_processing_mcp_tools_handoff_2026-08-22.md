# Animation processing MCP exposure handoff

## Result

Adapter `1.8.2` exposes the three existing bounded animation-processing operations through a fresh `blender_hoi4` MCP process and through `BlenderAdapterClient`.

The tools do not accept Python, shell commands, URLs, absolute paths, or unrestricted paths.
Every file argument remains job-relative and is checked by the adapter's existing job-root containment logic.

## Changed files

- `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`
- `.tools/3d_pipeline/adapter/blender_worker.py`
- `.tools/3d_pipeline/blender_client.py`
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`
- `.tools/3d_pipeline/config/dependencies.lock.json`
- `.tools/3d_pipeline/tests/test_animation_processing_tools.py`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/animation_processing_mcp_tools_handoff_2026-08-22.md`

The adapter files were already being edited by other tasks in the shared working tree.
Those unrelated edits were preserved.

## Live tools and schemas

### `chaosx_blender_hoi4_import_animation_action`

Required inputs: `job_id`, `blend_rel`, `source_rel`, `provenance_rel`, `checkpoint_rel`, `source_action_name`, `target_armature_name`, `target_action_name`, `source_kind`, `source_reference_id`, and `source_sha256`.

`source_kind` is schema-locked to `meshy_animate` or `professional_source`.
The worker requires a job-relative JSON receipt whose `verification_status`, source kind, reference id, source action name, and SHA-256 match the request and the actual source file.
It transfers the named source action to the named target armature and action, stamps retained lineage on the Blender action, removes imported provider objects, and returns provenance plus source/target motion-retention evidence.

### `chaosx_blender_hoi4_retime_animation_action`

Required inputs: `job_id`, `blend_rel`, `checkpoint_rel`, `action_name`, `target_armature_name`, `source_fps`, and `target_fps`.

The worker refuses an action without retained verified-source lineage.
It rescales keyframe and handle times only and returns the retained provenance, before/after F-curve counts, and an explicit no-replacement-motion result.

### `chaosx_blender_hoi4_correct_action_grounding`

Required inputs: `job_id`, `blend_rel`, `checkpoint_rel`, `action_name`, `target_armature_name`, and `grounding_policy`.
`root_bone` is optional and defaults to `Hips`.

`grounding_policy` is schema-locked to `per_frame_root_contact_zero_clearance`.
The worker refuses an action without retained verified-source lineage and limits correction to the detected root location channel.
It returns provenance, before/after contact measurements, F-curve retention counts, and an explicit no-replacement-motion result.

## Fresh-process discovery proof

The focused test launched `.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd` as a new MCP process and called `tools/list`.
All three tool identifiers were present with the exact properties above.
The import schema exposed the two-value `source_kind` enum, and the grounding schema exposed the single allowed policy as a JSON Schema `const`.

A newly started subagent process will therefore discover these tools.
An MCP server process that was already running before this change must be restarted because MCP tool declarations are loaded at process startup.

## Validation evidence

Command:

```powershell
python -m unittest discover -s .tools/3d_pipeline/tests -p test_animation_processing_tools.py -v
```

Result: three tests passed, covering fresh-process `tools/list`, schema restrictions, adapter/config lock version agreement, operation registration, and all three client wrappers.

Command:

```powershell
python .tools/3d_pipeline/verify_environment.py --help
```

The verifier executes directly and returned `findings: []` with its report at `.tools/3d_pipeline/reports/environment_report.json`.

The final locked source hashes are:

- MCP server: `DDE2F1A346401E1901C590A9DD5628B659E15EDB9F0D8B485DB70328F34E0C99`
- Blender worker: `DAE76EAC7A531496F9CF9AA303BCDAB8536E9F39E9638F7933CE5D6767F69074`
- client: `D6DF6BE84D3E51708B00ACC051DBC090E93DC3D52D9C08EA3CAD5A0478CFE970`
- adapter config: `71B138604D875AF041E13715F82336CA4D9148AB41799B2AABE7669BEDBE0FA2`

## Skipped validation and remaining risks

A Blender synthetic integration was not started; the parent requested the minimal exposure patch to finish with unit/schema/client coverage and environment verification.
The first real provider action should therefore be treated as the Blender-side integration exercise for receipt matching, imported source-action naming, and retained custom action properties.

`.tools/3d_pipeline/run_pilot.py` still calls the older permissive client signature and is outside this subtask's ownership.
It must be updated to create or select a verified provenance receipt and pass the exact source action, target armature/action, source kind, source reference id, and source checksum before that legacy pilot route can use the stricter `1.8.2` import wrapper.

No manual, procedural, simple, whole-rig, transform-only, or semantic replacement animation was added.
No alien, disaster, gameplay, model-package, skill, or `.qoder` file was edited by this task.

# Blender HOI4 MCP Allowlist Contract

## Purpose

The production MCP server exposes deterministic HOI4 operations without accepting arbitrary Python, shell commands, URLs, or unrestricted filesystem paths.

Every call requires:

- `job_id`
- approved job-root path
- operation-specific structured parameters
- dependency-lock identifier
- expected input checkpoint where relevant

Every response includes:

- operation ID
- start and end time
- Blender version
- adapter version
- script checksum
- input and output paths
- output checksums
- warnings and findings
- state transition proposal

## Path policy

Writable roots:

- current job root
- approved final staging root

Read-only roots:

- selected vanilla HOI4 model and documentation paths
- selected Chaos Redux reference paths
- adapter scripts and templates

Rejected:

- paths containing unresolved `..`
- network paths unless explicitly approved
- arbitrary user home paths
- system directories
- URLs
- symbolic-link escapes

## Allowed tools

### `blender_hoi4_health`

Checks Blender, adapter, extension, profile, and path policy.

Writes: environment report only.

### `blender_hoi4_create_scene`

Creates a job scene from the locked template.

Inputs:

- job root
- template ID
- output checkpoint path

### `blender_hoi4_inspect_scene`

Returns object, collection, material, armature, action, transform, bounds, and file-path metadata.

Writes: optional JSON report only.

### `blender_hoi4_import_candidate`

Imports one local GLB or FBX into the protected provider-source collection.

Inputs:

- source file inside job root
- importer preset
- expected source checksum

Rejects OBJ unless the job explicitly permits diagnostic import.

### `blender_hoi4_import_reference`

Imports one approved local vanilla or Chaos Redux model as read-only reference data.

Inputs are restricted to the job's approved reference paths.

### `blender_hoi4_duplicate_working_mesh`

Duplicates selected source objects into the working collection and records lineage.

### `blender_hoi4_audit_geometry`

Reports:

- triangles and vertices
- loose components
- manifold and boundary data
- degenerates
- normals
- UVs
- materials
- transforms
- bounds and ground contact
- profile semantic check inputs

### `blender_hoi4_apply_geometry_repairs`

Accepts only an array of enumerated operations:

- `recalculate_normals`
- `merge_by_distance`
- `remove_degenerate_geometry`
- `fill_approved_small_holes`
- `separate_loose_components`
- `join_approved_components`
- `apply_transforms`
- `set_origin`
- `triangulate`
- `decimate_to_profile_target`

Every operation requires explicit limits. The call returns before-and-after reports.

### `blender_hoi4_normalize_transform`

Normalizes axis, ground plane, origin, and scale against an approved reference.

Inputs:

- reference object
- profile axes
- relative scale
- pivot policy

### `blender_hoi4_configure_materials`

Creates PDX material assignments from a named, versioned mapping preset.

Inputs cannot contain Python expressions or arbitrary node source.

### `blender_hoi4_export_texture_preview`

Renders controlled preview views for material QA.

### `blender_hoi4_import_provider_rig`

Inspects and registers an imported armature without changing it.

### `blender_hoi4_create_rig_from_recipe`

Creates a rig from a version-controlled recipe ID and structured landmark coordinates.

No free-form bone script is accepted.

### `blender_hoi4_map_skeleton`

Creates a semantic source-to-target mapping from enumerated roles and explicit bones.

### `blender_hoi4_bind_weights`

Supports controlled methods:

- `empty_groups`
- `rigid_component_assignment`
- `approved_automatic_seed_then_audit`
- `copy_from_approved_source`

### `blender_hoi4_audit_weights`

Reports zero-weight vertices, influence counts, normalization, opposite-side influences, and profile-specific rigid-part violations.

### `blender_hoi4_create_test_poses`

Creates temporary test poses from a versioned profile recipe. Test actions are never exported as runtime actions.

### `blender_hoi4_import_action`

Imports a local action source and records source skeleton and frame metadata.

### `blender_hoi4_retarget_action`

Uses a named semantic mapping, explicit FPS, frame range, root policy, and bake options.

### `blender_hoi4_author_action_from_recipe`

Creates mechanical or simple creature actions from a version-controlled recipe plus numeric key poses. Complex authored animation still requires artist review.

### `blender_hoi4_audit_action`

Reports frame range, FPS, keyed bones, root motion, loop delta, contact markers, and scale keys.

### `blender_hoi4_render_action_preview`

Creates evidence video or GIF plus a key-pose contact sheet.

### `blender_hoi4_prepare_export_collection`

Copies only approved objects, armature, materials, and one action into the export collection or scene state.

### `blender_hoi4_export_mesh`

Invokes the locked `io_pdx_mesh` mesh export preset.

### `blender_hoi4_export_animation`

Invokes the locked animation export preset for one approved action.

### `blender_hoi4_reimport_export`

Reimports a local exported file when supported and produces a comparison report.

### `blender_hoi4_save_checkpoint`

Saves a new checkpoint with stage, parent checkpoint, and checksums. It cannot overwrite an approved checkpoint.

### `blender_hoi4_package_evidence`

Builds the machine-readable evidence ledger from existing approved reports and artifacts. It does not change the model.

## Explicitly forbidden tools or parameters

- `execute_python`
- `eval`
- `exec`
- shell command strings
- PowerShell or command prompt strings
- arbitrary module imports supplied by the caller
- URL download
- unrestricted file read or write
- delete directory
- install extension during an asset job
- change dependency versions during an asset job
- send scene data to an external service

## Human review boundaries

The adapter can report and perform bounded operations. Human or parent review is required for:

- substantial sculpting
- unseen-side design
- component deletion or replacement
- skeleton design for novel anatomy
- complex keyframe animation
- material interpretation that changes identity
- any fallback or simplification

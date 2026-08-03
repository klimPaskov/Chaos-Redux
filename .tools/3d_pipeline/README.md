# Chaos Redux autonomous 3D model pipeline

This repository-owned package runs the bounded path:

~~~text
one approved reference image
  -> verified Meshy MCP route and balance gate
  -> image-to-3D and immediate GLB/FBX download with lineage
  -> repository-owned allowlisted Blender HOI4 adapter
  -> Blender checkpoints, PDX material processing, and texture QA
  -> checksum-locked io_pdx_mesh .mesh/.anim export
  -> reimport proof, validation evidence, and parent runtime handoff
~~~

The first process gate is a non-blank `MESHY_API_KEY` environment variable.

The package never prints or writes the key.

If the key is missing or blank, print this exact PowerShell command and tell the user to restart the shell or Codex:

~~~powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
~~~

The key gate precedes repository or job path discovery, reference generation, route discovery, balance checks, provider calls, and downstream work.

## Lock and route gate

From the repository root, verify the selected Meshy MCP route, the pinned official Meshy server, the narrow Blender HOI4 adapter route, Blender, and checksum-locked `io_pdx_mesh` before any balance or paid/provider work.

The lock and schema evidence surfaces are `.tools/3d_pipeline/config/dependencies.lock.json`, `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, and `.tools/3d_pipeline/config/blender_hoi4_adapter.json`.

The current pilot lock records `@meshy-ai/meshy-mcp-server@0.4.0`, Blender `5.1.2`, the `chaosx_blender_hoi4` adapter `1.1.0`, and `io_pdx_mesh` `0.91.0` with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The isolated Blender Lab MCP route is locked at tag `v1.0.0`, commit `03004fd0216bfe5e0a3d9ac9b47d5efadc3d78c4`, with verified server version `1.28.1` in the current dependency lock.

Record exact package versions, git heads, route and wrapper identifiers, schema versions, actual tool names, paid flags, required arguments, input exclusivity, adapter arguments, task IDs, response IDs, dependency-lock evidence, and artifact checksums.

The current verified Meshy tool names are `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.

Use only names and arguments returned by the verified live route.

The existing unattended Meshy route is `wrappers/run_meshy_mcp.cmd`, and the existing unattended Blender route is `wrappers/run_blender_hoi4_adapter.cmd`, which exposes structured job-root-bounded `chaosx_blender_hoi4_*` operations and no arbitrary Blender Python, shell, URL, or unrestricted absolute write path.

The adapter's `correct_action_grounding` operation is narrowly restricted to an existing attack action and the `Hips` root bone. It inserts measured integer-frame Hips-Z keys, corrects only the root contact offset, records before/after evaluated bounds, and rejects the checkpoint if any frame remains outside the contact tolerance. It does not author a replacement action, alter geometry, create a new rig, or call a provider.

Use the Blender Lab MCP route only for isolated development inspection after verifying its locked version and live interface.

Keep viewer, inspector, renderer, and comparison tools read-only, and record an absent capability such as a Technology Tree Viewer instead of inventing one.

## Deterministic job layout

Resolve the job root from the repository root, normalized owner id, and normalized asset slug rather than from chat assumptions.

~~~text
docs/assets/<owner_id>/models_3d/<asset_slug>/
  job.yaml
  manifest.md
  history.jsonl
  refs/
    original/
      meshy_input.png
      input_manifest.json
    derived/
    briefs/
  provider/
    requests/
    responses/
    tasks/
    credits/
    downloads/
    rejected/
  blender/
    source/
    reference/
    working/
    checkpoints/
    previews/
    reports/
  textures/
    source/
    processed/
    dds/
  export/
    mesh/
    anim/
  validation/
  evidence/
  logs/
  runtime/
    handoff.md
    crosswalk.md
~~~

Pass job-relative paths to provider and adapter calls after root-containment checks.

Keep history, manifest state, checksums, dependency records, and copy provenance inside the job root, and never archive secrets.

## Reference and material rules

Meshy receives exactly one clean final image at `refs/original/meshy_input.png`.

When no ready reference is supplied, generate exactly one Meshy-ready image through the approved route and retain its prompt, source mode, approval note, and checksum.

Never send a side-profile sheet, turnaround board, collage, multi-view board, or separate front/rear images to Meshy.

Blender front, rear, side, top, underside, wireframe, and material QA views are evidence only and are never provider inputs.

Preserve provider geometry and texture sources as immutable evidence.

Repair or reject holes, loose components, non-manifold edges, and degenerate geometry before acceptance.

Use the verified PDX material mapping and packed specular channels, and never use a raw grayscale roughness map as the PDX specular map.

Keep model textures within the verified runtime dimension budget, which is `1024` pixels for the current pilot surface.

If the provider diffuse is too dark, derive a documented deterministic grade from the immutable provider base and rebuild the derivative from that base instead of compounding edits.

## Humanoid animation and export rules

For humanoids, read-only import the installed vanilla infantry mesh and its entity, measure the source mesh, and record source geometry height, entity scale, effective runtime height, axes, and ground contact.

Match custom geometry to the calibrated vanilla source height and apply entity scale exactly once.

Keep source geometry height distinct from effective runtime height, and never guess `1.8m` or compensate with arbitrary scale.

Clean, retarget, and bake humanoid animation candidates, normalize armature transforms, scale keyed location channels deliberately exactly once when units differ, define in-place or root-motion policy, check foot and ground contacts, and validate real idle, move, and attack actions when required.

Never substitute a static still for a requested skeletal action.

Export `.mesh` and `.anim` only with the locked `io_pdx_mesh` setup, then reimport or parse the actual exported bytes and save proof with output checksums.

## Runtime handoff and ownership

Select final source geometry, materials, textures, and actions before synchronizing any runtime copy.

Active runtime files can be stale or can be overwritten by an older mapped texture even when the source export is correct.

Record source and destination paths, both SHA-256 hashes, copy provenance, and the final synchronization result, then compare destination hashes after the copy.

The parent owns `.asset`, entity, `.gfx`, gameplay wiring, active runtime consumers, and in-game screenshots.

Runtime source files may be staged under `.tools/3d_pipeline/staging` for parent review, but `docs/assets/...` is evidence and working material, not a runtime source root.

## Entrypoints

Run these commands from the repository root after the start and dependency gates pass:

~~~powershell
python .tools/3d_pipeline/verify_environment.py --probe-meshy
python .tools/3d_pipeline/run_pilot.py --asset anomaly_signal_beacon
python .tools/3d_pipeline/run_pilot.py --asset anomaly_recon_trooper
python .tools/3d_pipeline/run_pilot.py --all
~~~

This workflow supports both skeletal 3D `.mesh`/`.anim` production and static HOI4 map-building `.mesh` production.

The pilot runner routes `building` and `static_building` jobs through the static mesh path, requires their named installed vanilla scale reference, and never attempts humanoid rigging or animation for them.

## Static map-building contract

Use the `building` asset profile for any model consumed by `show_on_map` building entities. Calibrate against the installed vanilla mesh and the exact entity scale, then enforce both source height and runtime X/Y footprint. The current profile uses `facility_land.mesh` with `building_land_facility` at source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a `4.0m` maximum runtime footprint.

The adapter rejects an over-budget footprint by default. A job may explicitly request `fit_to_budget`, which applies one uniform X/Y factor after height normalization and records the before/after dimensions and factor. It never silently stretches X and Y independently.

Static building materials follow the installed vanilla consumer shader, currently `PdxMeshAdvancedSnow`, and the GFX meshsettings name must match the exported mesh object. Runtime material packing uses `Image_0.dds` for diffuse, `Image_1.dds` for PDX specular, and `Image_2.dds` for PDX normal after channel QA.

Never use `special_project_facility_spawn` for a custom map-building consumer. Use a dedicated provincial spawn pool for direct map buildings. For state-level gameplay with one visual per state, keep the gameplay building non-map and create a hidden provincial anchor with `province_max = 1`, `state_max = 1`, a dedicated spawn pool, and `construct_building_in_random_province` plus explicit cleanup/conversion logic. This route does not require `map/buildings.txt`.

Run the read-only runtime audit from the repository root:

~~~powershell
python .tools/3d_pipeline/validate_runtime_contract.py --all
~~~

The audit checks the profile calibration, runtime files, GFX consumers, building definitions, provincial anchor declarations, reimport topology, and packed DDS dimensions/channels without requiring a paid provider call.

Route 2D frame-sheet animation, animated sprites, GIF previews, and frame-by-frame UI packages to `chaos-redux-frame-animation`.

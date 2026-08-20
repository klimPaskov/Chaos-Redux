# Chaos Redux autonomous 3D model pipeline

This repository-owned package runs the bounded path:

~~~text
one approved reference image
  -> verified Meshy MCP route and balance gate
  -> image-to-3D and immediate GLB/FBX download with lineage
  -> repository-owned allowlisted Blender HOI4 adapter
  -> Blender checkpoints, PDX material processing, and texture QA
  -> checksum-locked io_pdx_mesh .mesh/.anim export
  -> sourced unit-audio package and licensing evidence when the asset is a unit
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

Treat `.tools/3d_pipeline/config/dependencies.lock.json` as the authoritative record for the currently resolved Meshy, Blender, `chaosx_blender_hoi4`, Blender Lab MCP, and `io_pdx_mesh` versions and checksums. Do not duplicate fixed adapter versions in this README because the bootstrap may resolve a newer compatible route.

The isolated Blender Lab MCP route is locked at tag `v1.0.0`, commit `03004fd0216bfe5e0a3d9ac9b47d5efadc3d78c4`, with verified server version `1.28.1` in the current dependency lock.

Record exact package versions, git heads, route and wrapper identifiers, schema versions, actual tool names, paid flags, required arguments, input exclusivity, adapter arguments, task IDs, response IDs, dependency-lock evidence, and artifact checksums.

The current verified Meshy tool names are `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`.

Use only names and arguments returned by the verified live route.

The existing unattended Meshy route is `wrappers/run_meshy_mcp.cmd`, and the existing unattended Blender route is `wrappers/run_blender_hoi4_adapter.cmd`, which exposes structured job-root-bounded `chaosx_blender_hoi4_*` operations and no arbitrary Blender Python, shell, URL, or unrestricted absolute write path.

A running Blender process is not bridge evidence. Probe `127.0.0.1:<socket_port>` using `blender_mcp_addon.socket_port` from the dependency lock; when the endpoint is absent, start the lock-selected Blender executable hidden with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port <socket_port>`, then reprobe and record the listening process before using the adapter.

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

Clean, retarget, and bake humanoid animation candidates, normalize armature transforms, scale keyed location channels deliberately exactly once when units differ, define in-place or root-motion policy, check foot and ground contacts, and validate real idle, move, attack, and death actions when required.

Never substitute a static still for a requested skeletal action.

### Credit-aware humanoid family batches

When several custom units use the same verified standard humanoid skeleton, a job family may declare `shared_humanoid_batch`, `shared_humanoid_rig_owner`, and `shared_humanoid_role` in its job manifest. Run:

~~~powershell
python .tools/3d_pipeline/run_pilot.py --specialized-zombie-batch <configured_batch_id>
~~~

The batch creates one distinct Meshy image-to-3D geometry candidate per unit, pays for the owner rig and provider idle/attack/death actions once, copies those immutable provider artifacts with checksums, and binds every recipient's own geometry to that shared standard skeleton through the locked dual-source Blender operation. Every recipient exports its own `.mesh`, idle/move/attack/death `.anim` files, textures, and reimport proofs. Sharing a skeleton/action source never permits reused geometry, a static-only package, or skipped action validation. Creature jobs in the batch continue through their dedicated Blender rig/action route.

The specialized zombie manifests use the verified textured Meshy-6 estimate of 30 credits for image-to-3D, 5 for a required over-300,000-triangle remesh when the source exceeds the rig limit, 5 for rigging, and 3 per provider animation. The shared seven-unit route therefore preflights every unit's geometry plus the owner's conditional rig/remesh/action stages; planned paid work is still checked against the live balance before calls, and every completed provider task's actual `consumed_credits` value supersedes the estimate for later runs.

Export `.mesh` and `.anim` only with the locked `io_pdx_mesh` setup, then reimport or parse the actual exported bytes and save proof with output checksums.

## Nonhumanoid creature route

Creature jobs must declare a numeric, measured scale crosswalk against the installed vanilla runtime reference and a dedicated `creature_rig_family` before the pilot runner will check balance, call Meshy, or export anything.

Winged or digitigrade bipeds use the `winged_biped` route, which creates separate wing-root, wing-mid, wing-tip, arm, hand, leg, foot, spine, neck, head, pelvis, and root bones with spatial semantic weights and authored idle, move, attack, and death actions.

Do not route winged, digitigrade, or quadrupedal silhouettes through `humanoid_unit`; a pending or non-numeric creature crosswalk is a hard preflight blocker rather than a value to coerce or infer.

The creature continuation stages loose components, writes a custom-rig checkpoint, preserves the complete action set across checkpoints, exports the mesh and four skeletal animations, and reimports each animation against the exported mesh before the parent can wire a runtime entity.

Ground each authored action by measuring from the uncorrected pose at every frame and keying an absolute armature-object translation. Root-bone-only offsets are not sufficient when the creature mesh is parented to the armature object, and any action that fails the ground-contact gate must stop the continuation before export.

## Custom-unit sound-design handoff

Every custom unit job must include a source-only sound package with a mandatory selection one-shot plus applicable acknowledgement or voice, idle or creature loop, movement, attack, impact, special-action, and death roles.

Use the exact installed vanilla land-unit consumer as the wiring precedent, including `sound/*.asset` source declarations, `soundeffect` wrappers, and entity `state` events in `gfx/entities/*.asset`.

Audit selection separately from entity-state audio. Infantry country voices use `TAG_infantry_idle` on selection and related `TAG_infantry_*` identifiers for orders and combat states. Inspect the installed executable templates and vanilla `vo.asset` precedents, then use `<TAG>_infantry_idle` for a dedicated country/original-tag unit family. This remains country/original-tag routing rather than per-subunit routing, so list every infantry consumer under that identity. If custom and ordinary infantry coexist under one tag and require distinct voices, mark per-subunit selection blocked. A custom selection soundeffect without an exact engine-consumed identifier is unwired.

Research and preserve legally usable source audio under the deterministic job root, record the source page, direct download, creator, license, original checksum, derived checksum, and permitted mechanical conversion, and never synthesize a test tone or placeholder effect.

Before runtime handoff, probe each installed WAV against the inspected consumer precedent. For a `Voices` category soundeffect such as `<TAG>_infantry_idle`, use signed 16-bit PCM (`pcm_s16le`), 44.1 kHz, mono, matching the installed vanilla voice assets; `pcm_f32le` float WAVs are not a valid completion format. A license-permitted mechanical conversion is `ffmpeg -map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`, and the handoff must retain original and derived hashes plus the `ffprobe` results.

The parent must enumerate every `common/units` sub-unit that resolves the custom `sprite` token before claiming family-wide audio coverage. A sound event attached to one entity reaches only the unit consumers that resolve that entity, so deliberate exclusions must be documented and every intended family member must share the sprite binding.

The parent owns final `sound/*.asset` definitions, runtime WAV copies, entity-state wiring, selection-consumer wiring, and live playback validation. The worker handoff must leave exact sound and soundeffect identifiers, selection binding scope, state synchronization points, source evidence, and remaining parent checks.

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
python .tools/3d_pipeline/run_pilot.py --all
~~~

This workflow supports both skeletal 3D `.mesh`/`.anim` production and static HOI4 map-building `.mesh` production.

The pilot runner routes `building` and `static_building` jobs through the static mesh path, requires their named installed vanilla scale reference, and never attempts humanoid rigging or animation for them.

## Static map-building contract

Use the `building` asset profile for any model consumed by `show_on_map` building entities. Calibrate against the installed vanilla mesh and the exact entity scale, then enforce both source height and runtime X/Y footprint. The current profile uses `facility_land.mesh` with `building_land_facility` at source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a `4.0m` maximum runtime footprint.

The adapter rejects an over-budget footprint by default. A job may explicitly request `fit_to_budget`, which applies one uniform X/Y factor after height normalization and records the before/after dimensions and factor. It never silently stretches X and Y independently.

Controlled reduction must finish at or below the requested triangle target. Dense sources may require multiple bounded decimation passes; a stalled pass or a final count above the declared target is a hard failure, not an acceptable near-target result.

Before a static-building export, run the allowlisted `bake_static_mesh_transforms` operation on the approved working checkpoint. It rejects non-static profiles, armatures, actions, protected/shared source data, negative or non-finite transforms, and bounds drift; it bakes location, rotation, and scale into mesh data while retaining names, UV layers, materials, world bounds, and ground contact. Static `.mesh` export then fails closed unless every approved working mesh has exact identity location, rotation, and scale.

If a visually accepted static building would exceed the PDX per-stream index envelope after UV and normal seam splitting, preserve its geometry and run `partition_static_mesh_export_batches` after transform baking. The operation assigns unchanged triangles to duplicate, texture-identical material batches beneath the same mesh object, caps each batch at a worst-case 60,000 exported vertices, and proves that geometry, bounds, transforms, UV layers, and object names did not change. Every export parses its text proof and fails if any individual PDX mesh stream exceeds 65,535 vertices.

Static building materials follow the installed vanilla consumer shader, currently `PdxMeshAdvancedSnow`, and the GFX meshsettings name must match the exported mesh object. Runtime material packing uses `Image_0.dds` for diffuse, `Image_1.dds` for PDX specular, and `Image_2.dds` for PDX normal after channel QA.

Never use `special_project_facility_spawn` for a custom map-building consumer. Use a dedicated provincial spawn pool for direct map buildings. Every custom `spawn_point` must have a matching `building_<spawn_point>` entity in the active `.asset` file. Different meshes must use different spawn points because one spawn point resolves to one map entity. When every state-level gameplay building level must appear, wire the gameplay building directly and provide one spawn position per possible level. Use a hidden provincial anchor only for a deliberate single visual independent of gameplay level, and maintain it with state-scoped `set_building_level`. Leave automatic nudging enabled unless a complete `map/buildings.txt` coordinate table exists.

Route 2D frame-sheet animation, animated sprites, GIF previews, and frame-by-frame UI packages to `chaos-redux-frame-animation`.

Regenerate the full map-building coordinate override after an installed vanilla map update with `python .tools/generate_chaosx_building_positions.py --vanilla-map "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/map" --output map/buildings.txt --force`. The generator preserves all vanilla rows and derives distinct in-province positions for both custom warfare facilities, five concentration-camp levels, and five extermination-camp levels.

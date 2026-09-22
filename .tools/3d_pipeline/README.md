# Chaos Redux autonomous 3D model pipeline

This repository-owned package runs the bounded path:

~~~text
one approved reference image
  -> verified Meshy MCP route and balance gate
  -> image-to-3D and immediate GLB/FBX download with lineage
  -> Meshy rig task, then Meshy preset actions or Text-to-Motion, for a provider-eligible bipedal model
  -> repository-owned allowlisted Blender HOI4 adapter
  -> candidate preparation, provider action ingestion, mesh geometry repair, PDX material processing, and texture QA
  -> live skeleton, skinning, and skeletal action authoring in Blender for every asset the provider route does not cover
  -> checksum-locked io_pdx_mesh .mesh/.anim export
  -> sourced unit-audio package and licensing evidence when the asset is a unit
  -> reimport proof, validation evidence, and parent runtime handoff
~~~

For work that calls Meshy, first verify a non-blank `MESHY_API_KEY` environment variable. Blender-only repairs of existing models skip this provider gate.

Meshy model selection is live-route gated. Meshy 7 is the only accepted generation model. Inspect the repository-owned `meshy_image_to_3d` declaration before paid work and pass explicit `ai_model: meshy-7`; the wrapper applies a deterministic compatibility patch when the official Meshy API changes before the published MCP package. Require `tools/list` proof, record the exact provider model, and never use an alias, relabel an older output, or bypass MCP with a hidden REST call.

The compatibility patch must be idempotent and UTF-8 stable. Verify it with two consecutive schema probes and reject patched runtime files above the wrapper's size guard. The shared stdio client owns cleanup of descendants created by each exact wrapper process so repeated status polls do not leave provider servers running after the call returns.

The package never prints or writes the key.

If Meshy work requires a key and it is missing or blank, print this exact PowerShell command and tell the user to restart the shell or Codex:

~~~powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
~~~

The key gate precedes Meshy route discovery, balance checks, and provider calls. Blender-only repairs verify their job boundary, Blender adapter, and export stack without a provider dependency.

## Skeleton, skinning, and action policy

No repository Python script and no adapter operation may generate bones, skin weights, or keyframes from a declarative spec, a template, or a formula. Provider results are ingested as authored assets and are never synthesized by repository code.

The Meshy provider route is the preferred route for rigging and animating provider-eligible bipedal models: the worker generates the body, drives the Meshy rig task and the Meshy animation tasks, and ingests the provider results into the job.

A provider-eligible biped is a bipedal asset with clearly defined limbs and body structure, and it does not have to be human; a bipedal creature or machine that meets that structure may use the provider route. Programmatic provider rigging currently handles only such assets: quadrupeds, winged, serpentine, amorphous and other non-bipedal anatomy are outside it, and the provider rejects pose estimation for them. Verify the live locked route's current rigging constraints before committing an unusual anatomy to the provider route, and move a model to live Blender authoring when the provider rejects it.

Live Blender authoring covers everything the provider route does not: non-bipedal and non-humanoid anatomy, creature rigs, mechanical and articulated assemblies, firearm-specific rig and attachment work, measured creature rigs, component and prop modeling, and every missing or faulty provider result. Live authoring is iterative and holds every result to visual and deformation review.

A pipeline operation that would generate a rig, transfer skin weights automatically, or synthesize an action from a declarative spec, a template, or a formula is not permitted and must not be introduced.

A provider-eligible bipedal body receives its skeleton and skinning inside the downloaded Meshy-rigged model, and every asset the provider route does not cover is rigged and skinned live in Blender.

Repository Python keeps provider generation and download planning, candidate import and preparation of provider geometry, texture and material processing, mesh geometry repair, static transform baking and export partitioning, mesh and action export, reimport proof, accepted-reimport promotion, locator authoring, inspection and render QA, and health and checkpoint plumbing.

The accepted authoring or ingestion result is saved as a job checkpoint inside the job root, and the locked exporter writes the `.mesh` and `.anim` files from that checkpoint.

## Lock and route gate

From the repository root, verify the selected Meshy MCP route, the pinned official Meshy server, the narrow Blender HOI4 adapter route, Blender, and checksum-locked `io_pdx_mesh` before any balance or paid/provider work.

The lock and schema evidence surfaces are `.tools/3d_pipeline/config/dependencies.lock.json`, `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, and `.tools/3d_pipeline/config/blender_hoi4_adapter.json`.

Treat `.tools/3d_pipeline/config/dependencies.lock.json` as the authoritative record for the currently resolved Meshy, Blender, `chaosx_blender_hoi4`, Blender Lab MCP, and `io_pdx_mesh` versions and checksums. Do not duplicate fixed adapter versions in this README because the bootstrap may resolve a newer compatible route.

The isolated Blender Lab MCP route is locked at tag `v1.0.0`, commit `03004fd0216bfe5e0a3d9ac9b47d5efadc3d78c4`, with verified server version `1.28.1` in the current dependency lock.

Record exact package versions, git heads, route and wrapper identifiers, schema versions, actual tool names, paid flags, required arguments, input exclusivity, adapter arguments, task IDs, response IDs, dependency-lock evidence, and artifact checksums.

The current verified Meshy tool names are `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, `meshy_animate`, `meshy_text_to_motion`, `meshy_get_motion_status`, `meshy_list_motion_tasks`, `meshy_download_motion`, and `meshy_animation_library`.

Use only names and arguments returned by the verified live route.

Provider work in this package uses that route for balance preflight, geometry generation, task status, download, remesh, conversion, the humanoid rig task, and the preset-action and Text-to-Motion animation tasks. The provider rig and its actions are ingested as authored assets, and no repository script and no adapter operation generates a skeleton, skin weights, or keyframes from a declarative spec, a template, or a formula.

### Meshy runtime recovery

Lock the official `@meshy-ai/meshy-mcp-server` and its transitive `@modelcontextprotocol/sdk` by exact version, package integrity, and git head in `config/dependencies.lock.json`. Keep a versioned compatibility runtime keyed by those versions, verify both `dist/esm/server/index.js` and `dist/esm/server/streamableHttp.js`, and serialize install and patch work with a named interprocess mutex. Apply the patch once per runtime file and record matching patched-file checksums or sizes across the consecutive probes to prove idempotence.

After install and patch, run two consecutive `tools/list` probes and one concurrent probe pair through `wrappers/run_meshy_mcp.cmd`; every response must expose `meshy_image_to_3d` with `meshy-7`, then run a live `meshy_check_balance` probe through the same route. Snapshot process IDs matching the exact wrapper or provider entrypoint before each probe and require that no probe-started ID survives after it; processes belonging to another concurrent task are not leaks and must not be terminated. On Windows, attach each stdio wrapper to a kill-on-close Job Object or equivalent process-tree owner because descendants can outlive JSON-RPC completion; only descendants started by the current probe that remain alive after cleanup fail the health gate.

The existing unattended Meshy route is `wrappers/run_meshy_mcp.cmd`, and the existing unattended Blender route is `wrappers/run_blender_hoi4_adapter.cmd`, which exposes structured job-root-bounded `chaosx_blender_hoi4_*` operations and no arbitrary Blender Python, shell, URL, or unrestricted absolute write path.

A running Blender process is not bridge evidence. Probe `127.0.0.1:<socket_port>` using `blender_mcp_addon.socket_port` from the dependency lock; when the endpoint is absent, start the lock-selected Blender executable hidden with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port <socket_port>`, then reprobe and record the listening process before using the adapter.

Bones, skin weights, and keyframes produced by live authoring are created and edited only inside that live bridge session, where the model agent works on the approved working checkpoint, reviews the deformation and the motion visually, and saves the accepted result as a job checkpoint. An ingested provider action is checkpointed inside the same job root and reviewed with the same deformation, contact, and role-motion evidence.

Verify the locked Blender Lab MCP version and live interface before using the bridge session for authoring or for isolated development inspection.

Keep viewer, inspector, renderer, and comparison tools read-only, and record an absent capability such as a Technology Tree Viewer rather than inventing one.

### Provider credit preflight

Every paid provider stage is checked against the live balance before its call, and every paid task writes a before/after balance reconciliation.

Textured Meshy 7 image-to-3D generation is estimated at 30 credits, and the remesh of a source above 300,000 triangles is estimated at 5 credits.

The provider's actual `consumed_credits` value supersedes the estimate for later runs.

## Supported adapter operations

The adapter exposes these job-root-bounded operations:

- Health and checkpoint plumbing: `health`, `save_checkpoint`.
- Candidate preparation: `prepare_candidate`.
- Inspection and QA: `inspect_scene`, `review_humanoid_components`, `inspect_mesh_winding`, `inspect_mesh_landmarks`, `inspect_animation_source`.
- Texture and material processing: `process_textures`, `bind_existing_pdx_material`.
- Mesh geometry repair: `repair_mesh_winding`, `repair_explicit_mesh_winding`, `repair_explicit_mesh_winding_batch`, `remove_explicit_duplicate_faces`, `repair_explicit_mesh_patch`, `edit_explicit_mesh_vertices`, `repair_explicit_vertex_remap`, `replace_explicit_corner_normals`.
- Working assembly: `rotate_existing_assembly_yaw`, `author_locator`.
- Static baking and export partitioning: `bake_static_mesh_transforms`, `partition_static_mesh_export_batches`, `partition_skeletal_mesh_export_batches`.
- Provider animation ingestion: `import_animation_action`, `import_bvh_animation_action`, `retime_animation_action`.
- Export, reimport, and promotion: `prepare_export_coordinate_checkpoint`, `export_mesh`, `export_animation`, `reimport_export`, `promote_accepted_reimport`, `sanitize_runtime_candidate`.

The surface publishes 32 job-root-bounded operations, and `routes.blender_hoi4_adapter.version` in the dependency lock is the authoritative adapter version for every run.

`.codex/config.toml` enables a 16-operation subset of this surface for production runs, including all three ingestion operations.

An operation that would generate a rig, transfer skin weights automatically, or synthesize an action from a declarative spec, a template, or a formula is outside this surface.

`author_locator` creates or updates one job-owned bone-parented Empty and never geometry or motion.

`inspect_animation_source` reads a standalone FBX source's skeleton and action identity in a disposable scene without a target checkpoint.

`import_animation_action` transfers one receipt-verified provider or professional skeletal action onto the target armature by its exact source action id with hash-bound provenance. It requires a new sibling checkpoint, a new target action name, an explicit 64-character `source_sha256`, and a provenance receipt whose `verification_status`, `source_kind`, `source_reference_id`, `source_action_name`, and `source_sha256` all match, with `source_kind` one of `meshy_animate`, `meshy_text_to_motion`, or `professional_source`. It reads the real bone channels from the provider file and leaves the runtime scene with one model and one armature.

`import_bvh_animation_action` native-imports and retargets one receipt-verified BVH action. It requires the verified BVH filename stem, a non-empty `bone_chains` map, `root_motion_policy = in_place_xy_preserve_z`, finite positive `source_fps` and `target_fps` where the declared source rate matches the file header, a `global_scale` between `0.0001` and `1000000`, distinct signed forward and up axes, a `semantic_role` that appears in the target action name, and a provenance receipt recording `source_format = bvh`.

`retime_animation_action` retimes one already-ingested action between frame rates without changing its motion: it rescales keyframe times and handles by `target_fps / source_fps`, keeps every keyed value unchanged, and reports `body_motion_replaced = false`, `new_rig_created = false`, and `keyframe_values_changed = false`.

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

## Candidate preparation

`prepare_candidate` prepares provider geometry inside the job root, and its payload uses `source_rel`, `asset_kind`, `target_height_m`, `runtime_stem`, `runtime_entity_scale`, `target_triangles`, `excluded_provider_objects`, `vanilla_reference`, `texture_source_rels`, `preserve_geometry_topology`, `repair_before_reduction`, `topology_weld_distance`, `max_runtime_footprint_m`, `runtime_footprint_policy`, and `output_namespace_rel`.

Preparation keeps provider geometry, applies the calibrated height and scale exactly once, and never creates a skeleton, binds geometry to a rig, or produces skin weights. A Meshy-rigged body arrives with its skeleton and skinning inside the downloaded provider model, so `prepare_candidate` imports that provider result as authored data and sanitizes provider scale channels on humanoid assets.

Every asset the provider route does not cover is rigged and skinned live in Blender.

### Runtime weight sanitization

`sanitize_runtime_candidate` creates a runtime checkpoint, and its `weight_only` mode preserves geometry, the rig, weapons, and materials.

Weight sanitation enforces engine limits such as the maximum influence count: it removes invalid and zero-weight influences, keeps the strongest influences within that count, renormalizes the remaining weights, and reports the result per mesh.

An unweighted vertex is a rigging defect that the report surfaces for real authoring in Blender, and the pipeline never pins it to the root bone.

## Reference and material rules

Meshy receives exactly one clean final image at `refs/original/meshy_input.png`.

When no ready reference is supplied, generate exactly one Meshy-ready image through the approved route and retain its prompt, source mode, approval note, and checksum.

Never send a side-profile sheet, turnaround board, collage, multi-view board, or separate front/rear images to Meshy.

Blender front, rear, side, top, underside, wireframe, and material QA views are evidence only and are never provider inputs.

Preserve provider geometry and texture sources as immutable evidence.

Repair or reject holes, loose components, non-manifold edges, and degenerate geometry before acceptance.

Use the verified PDX material mapping and packed specular channels, and never use a raw grayscale roughness map as the PDX specular map.

Keep model textures within the verified runtime dimension budget, which is `1024` pixels for the current pilot surface.

If the provider diffuse is too dark, derive a documented deterministic grade from the immutable provider base and rebuild the derivative from that base rather than compounding edits.

## Humanoid calibration and action rules

For humanoids, read-only import the installed vanilla infantry mesh and its entity, measure the source mesh, and record source geometry height, entity scale, effective runtime height, axes, and ground contact.

Match custom geometry to the calibrated vanilla source height and apply entity scale exactly once.

Keep source geometry height distinct from effective runtime height, and never guess `1.8m` or compensate with arbitrary scale.

Each required role is a real skeletal action, ingested from a receipt-verified provider result or authored live in Blender, and the accepted action is checkpointed in the PDX export coordinate system before export.

Every role declares its in-place or root-motion policy, keeps foot and ground contact, and is reviewed as real idle, move, attack, and death motion where required.

Never substitute a static still for a requested skeletal action.

### Action authoring and validation

Bones, skin weights, and keyframes produced by live authoring are created and edited only in the live Blender session, and repository Python works on the checkpoint that session saves. A provider action is ingested onto the rig by the receipt-verified ingestion operations, and repository Python never generates a skeleton, skin weights, or keyframes.

Role-specific bone motion must be real, and whole-rig transforms alone, static-pose aliases, and semantic reuse of one action for another role are not final animation.

Attack and fire roles require aim, discharge, recoil, and recovery where applicable, and death requires articulated collapse, impact, and settling.

Preserve the existing contact, loop, root-motion, scale, preview, export, and reimport acceptance requirements.

Record the authoring or ingestion session, the accepted checkpoint, the action source, and the proof paths for every action.

If a required authoring capability is unavailable, report the exact capability gap rather than substituting mock motion.

An external animation source requires its verified provenance receipt and its separate approval.

### Equipped item generation and Blender assembly

Meshy is unreliable at a subject holding an object, so a body is never generated with anything in its hands and every held item is produced separately.

Every current equipped unit must receive a fresh item-free Meshy 7 body, even when its armed predecessor was considered complete.

Prepare exactly one body-only reference with every held item excluded, with clear anatomy and neutral hands in a suitable A/T pose; keep each item's design as separate reconstruction evidence.

Generate each required held item — firearm, melee weapon, tool, shield, staff, banner, instrument, or carried object — through its own Meshy 7 geometry task from exactly one item-only image, firearms under `refs/firearms/<firearm_id>/meshy_input.png` and other items under `refs/equipment/<item_id>/meshy_input.png`. Never submit the body and an item together, and never two items together.

The Meshy rig task and the Meshy animation tasks supply this body's skeleton, skinning, and provider actions, and the live Blender session attaches each item with rigid controls and real contacts.

Provider actions authored for an empty-handed body are a source candidate, not the final equipped performance: author and review grip, carry, aim, discharge, recoil, recovery, and retention on the assembled model, per frame, and re-check the item's contacts through the whole action. Animating the body alone and parenting the item afterwards is a shortcut and fails acceptance.

Keep each item rigid and separately controlled, validate both hand contacts and the shoulder/stock relationship when applicable, and retain a measured muzzle locator, aim/discharge/recoil/recovery phases, and synchronized effects and sourced audio.

A fused provider weapon or prop is historical evidence, not the final assembly route.

Add all missing required model elements in Blender without asking again, including melee tools, weapons, held objects, and equipment.

Preserve the intended unit identity and document component design, dimensions, materials, attachment, and editable source geometry.

Budget the complete model including props against its calibrated ceiling; perform only the bounded body reduction needed for required additions and compare the silhouette/materials/deformation.

Use verified structured adapter operations and source-preserving working copies; add a narrow validated mesh operation when the required component is unsupported rather than omitting it.

Keep the current runtime assets intact until the complete replacement passes visual, deformation, and actual-byte export/reimport review.

Death validation measures the evaluated silhouette rather than requiring every frame to decrease monotonically. Require a substantial final centre drop while bounding any preparatory rise and terminal settling; record the exact peak-rise, final-drop, and rebound metrics and pair them with start/mid/end visual evidence from the approved articulated source. Do not add a whole-rig transform or accept an upright or rebounding final pose.

## Nonhumanoid calibration

A nonhumanoid job declares a measured, numeric scale crosswalk against the installed vanilla runtime reference, and a missing, pending, or non-numeric crosswalk is a hard blocker rather than a value to coerce or infer.

A non-bipedal or non-humanoid skeleton, its skin weights, and its actions are authored live in Blender on the dedicated custom-rig route.

## Export and reimport proof

Export `.mesh` and `.anim` only with the locked `io_pdx_mesh` setup, then reimport or parse the actual exported bytes and save proof with output checksums.

Reimport proof is required for every output, and a viewport, a provider preview, a file that merely exists, or a plausible filename is not reimport evidence.

`promote_accepted_reimport` promotes one hash-bound accepted reimport proof.

## Custom-unit sound-design handoff

Every custom unit job must include a source-only sound package with a mandatory selection one-shot plus applicable acknowledgement or voice, idle or creature loop, movement, attack, impact, special-action, and death roles.

Use the exact installed vanilla land-unit consumer as the wiring precedent, including `sound/*.asset` source declarations, `soundeffect` wrappers, and entity `state` events in `gfx/entities/*.asset`.

Audit selection separately from entity-state audio. Infantry country voices use `TAG_infantry_idle` on selection and related `TAG_infantry_*` identifiers for orders and combat states. Inspect the installed executable templates and vanilla `vo.asset` precedents, then use `<TAG>_infantry_idle` for a dedicated country/original-tag unit family. This remains country/original-tag routing rather than per-subunit routing, so list every infantry consumer under that identity. If custom and ordinary infantry coexist under one tag and require distinct voices, mark per-subunit selection blocked. A custom selection soundeffect without an exact engine-consumed identifier is unwired.

Research and preserve legally usable source audio under the deterministic job root, record the source page, direct download, creator, license, original checksum, derived checksum, and permitted mechanical conversion, and never synthesize a test tone or placeholder effect.

Before runtime handoff, probe each installed WAV against the inspected consumer precedent. For a `Voices` category soundeffect such as `<TAG>_infantry_idle`, use signed 16-bit PCM (`pcm_s16le`), 44.1 kHz, mono, matching the installed vanilla voice assets; `pcm_f32le` float WAVs are not a valid completion format. A license-permitted mechanical conversion is `ffmpeg -map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`, and the handoff must retain original and derived hashes plus the `ffprobe` results.

The parent must enumerate every `common/units` sub-unit that resolves the custom `sprite` token before claiming family-wide audio coverage. A sound event attached to one entity reaches only the unit consumers that resolve that entity, so deliberate exclusions must be documented and every intended family member must share the sprite binding.

The parent owns final `sound/*.asset` definitions, runtime WAV copies, entity-state wiring, and selection-consumer wiring, and reviews the live playback evidence supplied by the user. The worker handoff must leave exact sound and soundeffect identifiers, selection binding scope, state synchronization points, source evidence, and remaining parent checks.

## Custom-unit counter handoff

Every custom unit also requires new counter art for every counter surface it uses.

The counter must be original to that unit, use the exact vanilla green counter palette sampled from an inspected reference, and follow the installed consumer's canvas, frame order, and alpha treatment.

Inspecting the closest matching installed vanilla counter definition and DDS plus the matching skill-local counter reference family is a hard gate, and a reused, renamed, generic, or uninspected counter cannot satisfy completion.

Route counter production through `chaos-redux-event-assets` and `chaosx_icon_artist`.

The worker handoff records each runtime counter consumer and token, the required states and sizes, the inspected installed vanilla definition and DDS paths, the matching skill-local counter reference family, the original counter-art paths, the final DDS paths, and the sampled green evidence.

The parent owns final GFX and gameplay wiring and reviews the counter contact sheet.

## Runtime handoff and ownership

Select final source geometry, materials, textures, and actions before synchronizing any runtime copy.

Active runtime files can be stale or can be overwritten by an older mapped texture even when the source export is correct.

Record source and destination paths, both SHA-256 hashes, copy provenance, and the final synchronization result, then compare destination hashes after the copy.

The parent owns `.asset`, entity, `.gfx`, gameplay wiring, and active runtime consumers.

The user performs live in-game validation and supplies the in-game screenshots, and the parent reviews that evidence.

Runtime source files may be staged under `.tools/3d_pipeline/staging` for parent review, but `docs/assets/...` is evidence and working material, not a runtime source root.

## Entrypoints

Run these commands from the repository root after the start and dependency gates pass:

~~~powershell
python .tools/3d_pipeline/verify_environment.py --probe-meshy
python .tools/3d_pipeline/run_pilot.py anomaly_signal_beacon
python .tools/3d_pipeline/run_pilot.py --phase candidate anomaly_signal_beacon
python .tools/3d_pipeline/run_pilot.py --phase candidate --all
~~~

The pilot runner is a provider-generation, static-mesh, and export orchestrator, and it is not a rigging or animation route. A provider-eligible bipedal rig and its actions come from the Meshy provider route and its ingestion operations, and every other skeleton, skin weight set, and action is authored live in Blender through the Blender MCP bridge. `--phase candidate` stops after provider generation and candidate preparation for the selected pilots.

This workflow supports both skeletal 3D `.mesh`/`.anim` production and static HOI4 map-building `.mesh` production.

The pilot runner routes `building` and `static_building` jobs through the static mesh path, requires their named installed vanilla scale reference, and schedules no skeleton, skinning, or action work for them.

## Static map-building contract

Use the `building` asset profile for any model consumed by `show_on_map` building entities. Calibrate against the installed vanilla mesh and the exact entity scale, then enforce both source height and runtime X/Y footprint. The current profile uses `facility_land.mesh` with `building_land_facility` at source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a `4.0m` maximum runtime footprint.

The adapter rejects an over-budget footprint by default. A job may explicitly request `fit_to_budget`, which applies one uniform X/Y factor after height normalization and records the before/after dimensions and factor. It never silently stretches X and Y independently.

Controlled reduction must finish at or below the requested triangle target. Dense sources may require multiple bounded decimation passes; a stalled pass or a final count above the declared target is a hard failure, not an acceptable near-target result.

Before a static-building export, run the allowlisted `bake_static_mesh_transforms` operation on the approved working checkpoint. It rejects non-static profiles, armatures, actions, protected/shared source data, negative or non-finite transforms, and bounds drift; it bakes location, rotation, and scale into mesh data while retaining names, UV layers, materials, world bounds, and ground contact. Static `.mesh` export then fails closed unless every approved working mesh has exact identity location, rotation, and scale.

If a visually accepted static building would exceed the PDX per-stream envelope after UV and normal seam splitting, preserve its geometry and run `partition_static_mesh_export_batches` after transform baking. The operation assigns unchanged triangles to duplicate, texture-identical material batches beneath the same mesh object, defaults each batch to a conservative worst-case 24,000 exported vertices, and proves that geometry, bounds, transforms, UV layers, and object names did not change. Every export parses its text proof and fails if any individual PDX mesh stream exceeds either 65,535 vertices or 65,535 triangle indices. Treat duplicate texture-identical slots as render streams rather than distinct logical materials, and register every exported stream index with its own matching `meshsettings` block; registering only index 0 produces incomplete, shard-like map geometry even when Blender reimport is clean.

Static building materials follow the installed vanilla consumer shader, currently `PdxMeshAdvancedSnow`, and the GFX meshsettings name must match the exported mesh object. Runtime material packing uses `Image_0.dds` for diffuse, `Image_1.dds` for PDX specular, and `Image_2.dds` for PDX normal after channel QA.

Never use `special_project_facility_spawn` for a custom map-building consumer. Use a dedicated provincial spawn pool for direct map buildings. Every custom `spawn_point` must have a matching `building_<spawn_point>` entity in the active `.asset` file. Different meshes must use different spawn points because one spawn point resolves to one map entity. When every state-level gameplay building level must appear, wire the gameplay building directly and provide one spawn position per possible level. Use a hidden provincial anchor only for a deliberate single visual independent of gameplay level, and maintain it with state-scoped `set_building_level`. Leave automatic nudging enabled unless a complete `map/buildings.txt` coordinate table exists.

Route 2D frame-sheet animation, animated sprites, GIF previews, and frame-by-frame UI packages to `chaos-redux-frame-animation`.

Regenerate the full map-building coordinate override after an installed vanilla map update with `python .tools/generate_chaosx_building_positions.py --vanilla-map "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/map" --output map/buildings.txt --force`. The generator preserves all vanilla rows and derives distinct in-province positions for both custom warfare facilities, five concentration-camp levels, and five extermination-camp levels.

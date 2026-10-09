---
name: chaos-redux-3d-model-pipeline
description: Use when creating, rigging, animating, converting, exporting, auditing, or documenting a custom Hearts of Iron IV 3D model, Internet-sourced sound-design handoff, and bespoke vanilla-green counter handoff for a Chaos Redux unit, building, vehicle, aircraft, ship, creature, or articulated asset.
---

# Chaos Redux 3D Model Pipeline

Use this skill for final 3D geometry and skeletal animation assets. It covers the bounded path from one approved reference image through provider generation, provider rigging and provider animation for provider-eligible bipedal models, Blender normalization, live skeleton, skinning, and skeletal action authoring where the provider route does not apply, PDX materials, Paradox export, QA evidence, and a parent-owned runtime handoff.

Do not use it to draw 2D equipment illustrations, unit counters, focus or idea icons, 2D frame-sheet animation, leader portraits, or concept-only requests. The 3D workflow owns the custom-unit counter requirement, vanilla-reference gate, and bounded artist handoff, while final counter art remains with `chaos-redux-event-assets` and `chaosx_icon_artist`. Other 2D surfaces remain with `chaos-redux-event-assets` and `chaos-redux-frame-animation` where applicable.

## Skeleton, skinning, and action policy

No repository Python script and no adapter operation may generate bones, skin weights, or keyframes from a declarative spec, a template, or a formula. Provider results are ingested as authored assets and are never synthesized by repository code.

The Meshy provider route is the preferred route for rigging and animating provider-eligible bipedal models. The worker generates the body, drives the Meshy rig task and the Meshy animation tasks, and ingests the provider results into the job.

A provider-eligible biped has clearly defined limbs and body structure and need not be human; a suitable bipedal creature or machine may use the provider route. Verify the live locked route against the actual anatomy before a supported attempt. Quadrupedal, serpentine, amorphous, or otherwise unsupported body structures require live Blender authoring. Wings, tails, machinery, and other extra articulations need their own supported controls and actions; a bipedal body alone does not establish support for those parts. Do not classify an asset as static or provider-ineligible merely from its creature, mechanical, vehicle, building, air, or naval label; use its required motion and the actual provider constraints.

Live Blender authoring remains for everything the provider route does not cover well: non-bipedal and non-humanoid anatomy, creature rigs, mechanical and articulated assemblies, firearm-specific rig and attachment work, measured creature rigs, missing or faulty provider results, and component and prop modeling.

Skeletons, skinning, and skeletal actions that the provider route does not supply are authored live in Blender by the model agent itself through the Blender MCP bridge, iteratively, with visual and deformation review of the real result before it is accepted. The worker saves the accepted result as a job checkpoint for the export and reimport proof steps.

A Meshy-rigged body arrives with its skeleton inside the downloaded provider model, so `prepare_candidate` imports it, and `import_animation_action`, `import_bvh_animation_action`, and `retime_animation_action` bring the provider's actions onto that rig. `import_animation_action` transfers one receipt-verified provider or professional skeletal action onto the target armature by its exact source action id with hash-bound provenance, `import_bvh_animation_action` native-imports and retargets one receipt-verified BVH action with explicit bone chains, root-motion policy, scale and axes, and `retime_animation_action` retimes one already-ingested action between frame rates without changing its motion. `export_animation` and `reimport_export` prove the exported bytes.

An operation that would generate a rig, transfer skin weights automatically, or synthesize an action is outside this surface and must not be introduced.

## No shortcuts in model work

Shortcut work is a failed package, not a simplification to disclose afterwards. Every element this pipeline produces must be authored, reviewed, and evidenced deliberately, and a missing capability is reported as a blocker rather than covered by a shortcut.

This rule covers the whole surface, not only animation: geometry repair, component modeling, materials and textures, skeleton construction, skin weights, and every skeletal action.

- No skeleton, skin weight set, or keyframe may come from repository Python, a declarative spec, a template, or a formula. Bones, weights, and keys are either ingested from the provider route as authored assets or authored deliberately in the live Blender session.
- No incomplete or mismatched rig: no missing limb, spine, neck, finger, jaw, wing, or tail segments, no floating or unweighted bones, no joint placed by guesswork rather than measurement, no humanoid armature carrying nonhumanoid anatomy, and no bone set that cannot reach the poses its actions need.
- No skinning: no unreviewed automatic or bulk weighting, no uncorrected nearest-bone assignment, no rigid single-bone binding across a deforming region, and no weights that were never checked in representative poses.
- No motion: no static pose, no single-frame or transform-only stand-in, no whole-rig translation or rotation presented as an action, no formulaic loop with no role content, no reuse or light retiming of one role's action for another role, and no action copied from another model without real re-authoring on this rig.
- No component: no omitted required element, no painted or flat stand-in replacing modeled geometry, no fused provider weapon or prop kept as the final assembly, and no prop attached through whole-object transforms rather than a real control.
- No evidence: no reuse of another model's renders, previews, measurements, or acceptance, no role reported as validated from a viewport glance, and no pass claimed from file existence without decoded or reimported proof of the delivered bytes.
- No export or runtime: no skipped reimport proof, no entity scale that compensates for authored scale or proportion errors, no baking of a defective rig or action to hide the defect, and no runtime candidate shipped without checking its consumer source bindings.

When the live session cannot produce a required element or role to this standard, stop and report the exact capability or blocker.

## Ownership and completion boundary

Keep `.tools/3d_pipeline/` limited to shared adapters, clients, libraries, wrappers, and maintained tests.
Put unit-specific runners, fixed checkpoint probes, pilot specifications, and repair batches in `.tmp/<task>/` or the owning job workspace; do not embed them in the shared toolchain.
Temporary placement does not relax any authoring, source, licensing, dependency, or approval rule in this skill.

A provider result is a source candidate, a `.blend` is a working artifact, and a `.mesh` or `.anim` is a runtime candidate. Worker completion requires the requested production, review, export/reimport, sound-source, counter, and handoff outputs; the parent completes exact runtime registration and source consumer checks. User-supplied in-game evidence is reviewed when available but never requested or awaited as a delivery gate under AGENTS.md. Do not claim live validation from production or source checks.

The 3D worker may create source files, Blender checkpoints, textures, `.mesh`, `.anim`, sourced unit-audio candidates, mechanically derived audio, previews, manifests, reports, and handoffs. It must not edit gameplay, sound definitions, localisation, `.gfx`, `.gui`, `.asset`, entity, event, focus, decision, country, history, AI, on-action, or spreadsheet files unless the parent grants a narrow exception explicitly. The parent owns runtime identifiers, source wiring, final review, and the overall completion claim. The user performs live consumer validation.

`chaos-redux-event-assets` remains the owner of broad asset inventories, source provenance conventions, texture/DDS conventions, and requirement-to-runtime coverage across asset types. Keep model geometry, model materials, entity wiring, and any separate 2D concept reference distinct. `chaos-redux-frame-animation` governs 2D frame-sheet animation. It does not replace skeletal 3D `.anim` production.

Every new custom unit, custom subunit, creature, vehicle, aircraft, or ship also requires a custom sound-design package, defined under `Custom unit sound-design companion`, and every new custom unit requires new counter art for every counter surface it uses, defined under `Custom unit-counter companion`. For both packages the parent owns final definitions, runtime wiring, and evidence review, and the user performs in-game validation.

Final unit audio is source-only. The worker must never create, synthesize, record, generate, or manually author sound, and must never replace a missing source with test tones, primitive waveforms, placeholder beeps, noise beds, or an unlicensed stock effect. If a suitable sourced file cannot be found and licensed, mark the affected role or package `blocked`.

## Required reading and local calibration

Before 3D work, read:

- `AGENTS.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md` when a subagent is used.
- `.tools/3d_pipeline/README.md`, `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, and the operation array in `.tools/3d_pipeline/config/dependencies.lock.json` for the adapter surface and job-root rules.
- The parent brief, accepted spec, plan, manifest, job, dependency lock, and handoff.
- The offline Paradox wiki pages relevant to the target surface, especially `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`.
- Relevant character or interface pages when the target consumes those systems.
- Relevant documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.
- Local vanilla `.mesh`, `.anim`, `.asset`, entity, material, texture, and model precedents for the exact domain, plus existing Chaos Redux model precedents.
- For custom units, the exact installed vanilla sound, voice, soundeffect, and entity precedents used by the closest matching unit surface.
- For custom units, the exact installed vanilla counter consumer, sprite definition, DDS, canvas, frame order, alpha treatment, and closest visual precedent, plus the matching `chaos-redux-event-assets/assets/gfx_references/units/` counter family and contact sheet.

Use existing Chaos Redux paths under `gfx/models/` and `gfx/entities/` as local precedents where applicable, but confirm the final path, shader, material channels, scale, axes, skeleton, action names, and entity structure against the installed vanilla version. Do not lock tutorial values or assume that a nearby asset belongs to the same runtime surface. Treat tutorial polygon counts, texture dimensions, and provider defaults as starting heuristics only. The installed game and latest verified toolchain decide acceptance.

For a humanoid land-unit pilot, this is a hard calibration gate, not a suggestion: import the installed vanilla infantry `.mesh` into the Blender reference collection read-only, identify the exact entity and runtime `scale`, exclude collision-only geometry, and record the measured source-mesh height, effective runtime height, forward axis, ground contact, and the comparison result in the job and manifest. When the custom entity retains the vanilla entity scale, normalize the exported mesh to the measured source-mesh height so the engine applies that scale exactly once. Do not normalize to the effective runtime height and then multiply it by the entity scale again. Do not use a generic real-world height or an arbitrary entity `scale` as a substitute. Keep the provider/animation height and the Blender source-mesh calibration height as separate fields when the provider and HOI4 coordinate spaces differ.

For a static map-building pilot, this is also a hard calibration gate: import the installed vanilla mesh used by the actual building entity, identify the exact `pdxmesh` and entity scale, measure the source dimensions and effective runtime dimensions, and record the reference in the job and manifest. Height-only calibration is invalid for buildings. The current `building` profile uses `facility_land.mesh` with `building_land_facility`, source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a hard runtime X/Y footprint ceiling of `4.0` meters. A candidate over that ceiling must be explicitly fit with one uniform X/Y factor and must record before/after dimensions. Silent anisotropic stretching is forbidden.

## Route selection and component completion

Choose the route from the requested operation before provider calls. Geometry generation uses Meshy 7: prepare exactly one item-free body image and a separate item-only image and geometry task for each required firearm or other held item. Download each item independently. For provider-eligible bipedal bodies, try the supported Meshy rig once and each required action once on a usable rig, then ingest the usable results. Blender supplies assembly, rigid item controls, locators, contact corrections, missing components, and fallback rig/action authoring. A static profile needs no skeleton; an articulated asset needs a rig suitable for its anatomy and motion, with provider eligibility determined from the actual body and supported operation, not a mechanical, creature, vehicle, or building label. Repair, assembly, retexturing, export, and explicitly requested rebuild work retain their own required operations; the mere existence of a model never mandates generation or excludes an otherwise appropriate route.

Always create or restore every missing required model component, anatomy element, equipment piece, weapon, or held tool in Blender without renewed approval, preserving intended identity and source-informed design. Record an inventory that maps each required element to its modeled geometry, material, rig/attachment, action usage, and export/reimport evidence. Use verified bounded modeling and authoring operations; absent capability is a blocker, not permission to omit the element or replace it with a static/action alias. The authorization covers required component completion and modest budget-preserving reduction, while other provider/source substitutions retain their separate approval rules. Never store credentials in job files, skill files, manifests, prompts, logs, or handoffs.

### Equipped items are generated separately and animated as an assembly

Meshy is unreliable at a subject holding an object, so a body is never generated with anything in its hands. Every held or equipped item — firearm, melee weapon, tool, shield, staff, banner, instrument, or carried object — uses the separated route, and a provider candidate that already holds an item is historical evidence only. A firearm is the special case of this rule: the item-free body for a firearm unit is a weapon-free body, and that unit's extra requirements are the `fires_in_combat` or `non_firing` declaration, per-firing-state discharge timing, muzzle or weapon locator, particle and light effects, licensed weapon-matched sound, and grip and stock contacts, or the zero-state audit of firing states, effects, locators, and sounds for `non_firing`.

- The body input shows the subject with empty, neutral hands and no held or wielded item, and the body geometry task receives that item-free image alone.
- Each required equipped item is generated through its own Meshy 7 geometry task from exactly one item-only image, firearms under `refs/firearms/<firearm_id>/meshy_input.png` and other items under `refs/equipment/<item_id>/meshy_input.png`. Never submit the body and an item in one task, and never submit two items in one task.
- Archive the identity, proportions, materials, and reference of every excluded item so its item-only input and the Blender fitting reproduce it faithfully, and record the item inventory with its task id, source evidence, and download.
- Attach each item in the live Blender session with rigid controls, real contacts, and the bones, parenting, or constraints the part needs. An item attached through a whole-object transform, or left fused in a provider result, does not satisfy this route.
- Animate the assembled model. Provider actions authored for an empty-handed body are a source candidate, not the final equipped performance: author and review the grip, carry, aim, discharge, recoil, recovery, and retention behaviour of every role on the assembled model, per frame, and re-check the item's contacts through the whole action. Detached item animation, where the body alone is animated and the item is parented afterwards, fails acceptance.
- Report each item's provider task, input proof, attachment evidence, and per-frame contact validation in the manifest.

## Hard start gates

### Provider key and Blender-only repair

For provider-dependent jobs, the first process check is `MESHY_API_KEY`, which must be a non-blank process environment variable before provider preparation, balance checks, or provider calls. Blender-only work may inspect the approved model, job, dependency lock, and Blender routes without this key and must not start a provider call. If the key is missing or blank for provider-dependent work, stop that work, print this exact PowerShell command, and tell the user to restart the shell or Codex:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

For an operation that only requires Blender repair or authoring, use Blender directly without a provider rig or animation stage. Verify the observed Blender, Blender Lab MCP/add-on when live authoring is needed, adapter, and `io_pdx_mesh` dependencies against the lock, actual callable schemas, approved source/checkpoint paths, and export support before repair. Verify the Lab bridge socket only when using that live authoring route. A missing Meshy key or unavailable Meshy service does not block this Blender-only route; a missing required Blender capability remains `required installation/verification` or `blocked`.

### Dependency resolution and route verification

Resolve the repository and job roots from repository-owned files. For provider work, apply the Meshy key gate before route discovery, balance checks, or paid calls. Read `.tools/3d_pipeline/config/dependencies.lock.json` as observed dependency evidence, then verify the exact installed Blender build, repository-owned `chaosx_blender_hoi4` adapter and its schema, and checksum-locked `io_pdx_mesh` archive against that record. Provider work additionally verifies the locked Meshy MCP compatibility route and Meshy 7 schema. There is no repository bootstrap command that installs or updates this stack; the parent or toolchain maintainer resolves the available Blender Lab MCP release and matching add-on, Blender build, and `io_pdx_mesh` release or compatibility archive, installs and probes them, and records exact versions, source revisions, checksums, and results in the lock before the model worker relies on them. Read the adapter version from `routes.blender_hoi4_adapter.version` for every run. A lock entry or installed process alone does not prove current compatibility.

The production `chaosx_blender_hoi4` adapter launches its own factory-startup background Blender worker for each allowlisted operation; it does not use the Blender Lab socket. Its OS-level lock in `.tools/3d_pipeline/adapter/worker_lock.py` serializes adapter-owned background workers across repository clients to bound memory use; use the adapter rather than launching competing workers. Lock-file existence does not identify a live owner, so never delete the file to bypass contention. Use the separate verified Blender Lab MCP/add-on route for live manual component, rig, weight, and keyframe authoring when the adapter does not expose that work. Confirm its live tools and arguments, including `execute_blender_code` when that is the verified authoring tool, and keep its use within the approved job and source roots. Only when using that route, verify the add-on installation and configured endpoint, probe `127.0.0.1:<socket_port>` using `blender_mcp_addon.socket_port` from the lock, and start the lock-selected Blender executable in hidden background mode with `--background --factory-startup --addons <lock_selected_importable_modules> --online-mode --command blender_mcp --host 127.0.0.1 --port <socket_port>` if needed. Reprobe before authoring. Do not treat the Lab bridge as the adapter's transport or require its socket for adapter-only processing and export. If a required route, live schema, bridge, installed version, compatibility patch, or checksum cannot be verified, report `required installation/verification` or `blocked`; do not invent a tool or substitute an unverified dependency.

A task-owned live Lab should start from the factory scene rather than loading the user's startup file.
Derive importable add-on module names from the installed module layout, not only extension manifest IDs; for the current locked extension repository they are `bl_ext.user_default.mcp,bl_ext.user_default.io_pdx_mesh`.
Keep `--command` last because it consumes the remaining arguments.
When work requires one Blender worker, acquire the shared worker lock before launching Lab, record the owned PID, default-scene inventory, process working set and free memory before loading a model, then close that PID and release the lock before an independent adapter operation.
If memory is inadequate, preserve the checkpoint and defer the next step; do not stop another actor's process.

Use the lock-selected `io_pdx_mesh` compatibility archive for the installed Blender/Python build. Where that build requires the three-file compatibility changes for removal of `imp` and a `shadow_method` guard, verify their exact archived bytes and installed extension before export. After any Blender, Blender Lab, or `io_pdx_mesh` update, require an isolated `.mesh` and skeletal `.anim` export and actual-byte reimport probe; retain the probe paths, hashes, frame count, warnings, and result. A prior probe on another build is not current compatibility evidence.

Record the exact verified server package, version, git head, route or wrapper, schema version, actual tool identifiers, paid flags, input exclusivity, required arguments, adapter operation names and arguments, Blender build, extension manifest, provider task IDs, and response IDs. The verified Meshy route identifiers available to this pipeline include `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, `meshy_animate`, `meshy_text_to_motion`, `meshy_get_motion_status`, `meshy_list_motion_tasks`, `meshy_download_motion`, and `meshy_animation_library`; provider work here uses that route for balance preflight, geometry generation, task status, download, remesh, conversion, the humanoid rig task, and the preset-action and Text-to-Motion animation tasks, and every provider result is ingested as an authored asset rather than synthesized by repository code. Use only names returned by the live locked route and record the exact arguments used. If a route, schema, package, version, checksum, or capability required for the selected operation is missing or mismatched, stop that operation and report `required installation/verification` or `blocked`, naming exactly what is missing and which output it prevents. Preserve completed outputs and continue independent authorized work; do not repeatedly probe an unchanged missing dependency. Do not install packages, substitute an unapproved route, or invent a live MCP/tool name.

Inspect the live `meshy_image_to_3d` declaration through `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd` and `run_meshy_mcp.ps1` before geometry work. Require `ai_model = meshy-7`, confirm the dependency lock's `verified_image_models` contains only `meshy-7`, record the compatibility revision and exact model in task evidence, and use only the identifiers returned by the live locked route. When Meshy's official API changes before the published MCP package catches up, update and verify the repository-owned compatibility wrapper against the official API documentation and require a `tools/list` proof that `meshy-7` is exposed. Keep base-body generation inside that Meshy 7 route; missing required components, equipment, and held props may be modeled in Blender under the component-completion contract in `Route selection and component completion`. Do not use a model alias, direct REST fallback, or unverified generation route. Tie credit preflight to Meshy 7.

### Compatibility-wrapper integrity and probe cleanup

Treat the compatibility wrapper as deterministic production code. Lock the official `@meshy-ai/meshy-mcp-server` and its transitive `@modelcontextprotocol/sdk` by exact version, package integrity, and git head in `dependencies.lock.json`. Fail closed on any mismatch. Keep a versioned compatibility runtime keyed by those locked versions, verify both `dist/esm/server/index.js` and `dist/esm/server/streamableHttp.js` before patching or startup, and serialize install and patch work with a named interprocess mutex. Apply the schema patch exactly once per runtime file, preserve UTF-8 without re-encoding growth, and enforce a maximum patched-file size.

After install and patch, require two consecutive `tools/list` probes and one concurrent probe pair through the locked wrapper, recording matching patched-file checksums or sizes across the consecutive probes to prove idempotence. Every response must expose `meshy_image_to_3d` with explicit `meshy-7` accepted, followed by a live `meshy_check_balance` probe through the same route. Snapshot exact wrapper/provider process IDs before the probes and require that no probe-started ID survives afterward. Processes already owned by other concurrent repository tasks are not leaks and must not be terminated. On Windows, attach every stdio wrapper process started by the probe to a kill-on-close Job Object or equivalent process-tree owner and close it after the response or timeout because wrapper descendants can remain after JSON-RPC completes. A successful response with a surviving probe-started process is not healthy.

Keep provider and Blender integration guidance in this skill and the job's dependency lock. Do not create a central MCP router or an unverified replacement for the repository's existing wrappers. Any viewer, inspector, renderer, or comparison route used for QA must be read-only. This package does not provide unrelated viewers, including a Technology Tree Viewer. Record such a capability as absent when requested.

### Authorized Blender transitions

Live Blender rigging, weight work, and skeletal action authoring are standing authorized work for every asset the provider route does not cover, as listed in `Skeleton, skinning, and action policy`, including explicitly requested rig, weight, action, or component repairs. Open the bridge session and author there without asking for renewed approval, and record the session, the working checkpoint, and the accepted result. A receipt-verified provider action that fails role, contact, or ground-contact acceptance is repaired in the live session rather than accepted as delivered. Other provider or source substitutions and design simplifications still require explicit approval. A static pose, transform-only clip, or companion preview may document missing motion but never satisfies a requested skeletal action.

### Nonhumanoid preflight

After the key gate and job-root resolution, the job loader must preflight every `nonhumanoid_creature` or other nonhumanoid/creature job before any balance check or paid/provider call. Require a declared, measured `scale_crosswalk` with units and finite numeric reference dimensions, provider/Blender target dimensions, entity scale, effective runtime dimensions, and conversion or fit factor, plus a named dedicated custom-rig route for the live Blender authoring session and a written rig map. Reject missing, pending, placeholder, non-numeric, or unmeasured crosswalk values. Do not infer them from profile defaults. This preflight is also a hard gate before provider generation or export.

### Adapter publication

For adapter publication, verify exact operation-array agreement between `.tools/3d_pipeline/config/blender_hoi4_adapter.json` and `routes.blender_hoi4_adapter.operations` in the dependency lock, matching source hashes, and the complete local import closure. A required locked route omitted from the operation arrays is a publication failure even when its implementation exists; record the blocker until the publication is coherent. For hash-locked text sources, verify that Git-clean canonical bytes and raw working-tree bytes agree before recording release hashes; line-ending conversion must not invalidate the lock on checkout.

The adapter publishes the job-root-bounded operations listed in `routes.blender_hoi4_adapter.operations`, and `routes.blender_hoi4_adapter.version` in the dependency lock is the authoritative adapter version for every run. Verify that list against the live adapter schema. The currently documented operation families are:

- health and checkpoint plumbing: `health`, `save_checkpoint`.
- candidate preparation: `prepare_candidate`.
- inspection and QA: `inspect_scene`, `review_humanoid_components`, `inspect_mesh_winding`, `inspect_mesh_landmarks`, `inspect_animation_source`.
- texture and material processing: `process_textures`, `bind_existing_pdx_material`.
- mesh geometry repair: `repair_mesh_winding`, `repair_explicit_mesh_winding`, `repair_explicit_mesh_winding_batch`, `remove_explicit_duplicate_faces`, `repair_explicit_mesh_patch`, `edit_explicit_mesh_vertices`, `repair_explicit_vertex_remap`, `replace_explicit_corner_normals`.
- working assembly: `rotate_existing_assembly_yaw`, `author_locator`.
- static transform baking and export partitioning: `bake_static_mesh_transforms`, `partition_static_mesh_export_batches`, `partition_skeletal_mesh_export_batches`.
- provider animation ingestion: `import_animation_action`, `import_bvh_animation_action`, `retime_animation_action`.
- export, reimport, and promotion: `prepare_export_coordinate_checkpoint`, `export_mesh`, `export_animation`, `reimport_export`, `promote_accepted_reimport`, `sanitize_runtime_candidate`.

`inspect_mesh_landmarks` and `repair_explicit_mesh_winding` are implemented in `.tools/3d_pipeline/adapter/mesh_inspection_repair.py`. `author_locator` creates or updates one job-owned bone-parented Empty and never geometry or motion. `inspect_animation_source` reads a standalone FBX source's skeleton and action identity in a disposable scene without a target checkpoint. `sanitize_runtime_candidate` creates a runtime checkpoint and reports the enforced engine weight limits. `prepare_export_coordinate_checkpoint` checkpoints one accepted action in the existing PDX export coordinate system. `import_animation_action` requires a new sibling checkpoint, a new target action name, an explicit 64-character source SHA-256 digest, and a provenance receipt whose `verification_status`, `source_kind`, `source_reference_id`, `source_action_name`, and `source_sha256` all match the request, and `source_kind` is one of `meshy_animate`, `meshy_text_to_motion`, or `professional_source`; the operation reads the real bone channels from the provider file and leaves the runtime scene with one model and one armature. `import_bvh_animation_action` requires the verified BVH filename stem, a `bone_chains` map, `root_motion_policy = in_place_xy_preserve_z`, finite positive `source_fps`/`target_fps` within the header's tolerance, a `global_scale` between `0.0001` and `1000000`, distinct signed forward and up axes, a `semantic_role` present in the target action name, and a provenance receipt recording `source_format = bvh`. `retime_animation_action` rescales keyframe times and handles by `target_fps / source_fps`, keeps every keyed value unchanged, and reports `body_motion_replaced = false`, `new_rig_created = false`, and `keyframe_values_changed = false`. A Text-to-Motion retarget is rejected without an explicit measured `root_scale_reference` carrying only `source_head_bones` and `target_head_bones` joint-head pairs. `.codex/config.toml` enables the full published surface for production runs, including the three ingestion operations.

## Job intake and deterministic layout

Validate the job before any paid work. The parent must provide:

- event or system owner, stable asset ID, and lowercase asset slug
- one ready reference image path, or enough brief input for the documented modern-designed-artwork source search and one source-informed model-ready ImageGen preparation on a separate derivative. The intake must include the source-style decision, the selected `pose_preparation_mode`, and a source-free reference remains a separate explicit fallback only after documented search failure
- source mode (`licensed_search` or `reference_only_user_authorized`), immutable Internet source path or documented search record, source URL/page, title, creator/publisher, stated license/terms, retrieval date, provenance/rights and AI-use status, explicit user authorization where reference-only use is required, exact ImageGen prompt, source-to-prepared comparison, pose mode or `pose_preparation_mode = none` with its reason, and parent approval evidence
- one asset profile declared in `.tools/3d_pipeline/config/asset_profiles.json`
- geometry intent, required components, forbidden additions, texture direction, and unseen-side/rear-geometry policy
- a hard style-preflight result that rejects anime, manga, manhwa, chibi, cel-shaded anime-game-character, exaggerated anime facial or body proportions, and similar anime-derived presentation while keeping grounded professional fantasy, horror, tabletop, and game concept illustration eligible when it is not anime-derived
- for every firearm-bearing unit, an explicit `fires_in_combat` or `non_firing` declaration. The body Meshy input must be the item-free body, which for a firearm unit is weapon-free, with source firearm identity archived for a separate firearm-only Meshy 7 task; assembled firing actions must pass grip, stock, muzzle, and recoil/contact gates, while a declared non-firing unit receives no firing effects
- period-fit declaration for the event or system, including every explicitly intended anachronistic, electronic, advanced-optical, plastic, modern-tactical, or science-fiction element. Absent an explicit exception, the source must fit the 1936-1945-era world
- color status and palette direction. Black-and-white, grayscale, desaturated monochrome, clay-render, and untextured sources require an approved faithful ImageGen colorization before Meshy, while already colored sources retain their exact palette
- named vanilla reference paths and the expected scale relationship
- for buildings, the measured runtime footprint budget and whether the consumer is a dedicated provincial map building or a state-level gameplay building with a provincial visual anchor
- required action roles with their in-place or root-motion policy, the required bone set or anatomy map, the runtime consumer, baseline paid provider operations including the humanoid rig task and the preset-action or Text-to-Motion animation tasks, live balance and preflight records, the provider ingestion route and the live Blender authoring route for every asset the provider route does not cover, the requested operation and its route selection, and exact capability and budget stop conditions. Every firing role and state must have a discharge synchronization crosswalk, and a `non_firing` declaration must exclude firing roles and states
- for every custom unit, a sound-design brief with a mandatory selection role plus applicable acknowledgement, movement, idle or engine loop, attack, impact, special-action, and death or destruction roles, the selected vanilla precedents, the exact selection consumer, and animation synchronization points
- for every custom unit, a counter brief naming each exact runtime counter consumer, token, required state and size, final sprite and DDS path, inspected installed-vanilla definition and texture paths, matching skill-local counter reference family, and `chaosx_icon_artist` handoff path
- the locked provider, Blender, adapter, and `io_pdx_mesh` dependencies
- the deterministic job root and exact handoff path

When the parent does not supply a root, derive it from the resolved repository root, a normalized stable owner id, and a normalized asset slug:

```text
docs/assets/<owner_id>/models_3d/<asset_slug>/
  job.yaml
  manifest.md
  history.jsonl
  refs/
    source/
      untouched.<ext>          # immutable selected or user-supplied source; evidence only
      provenance.json
      source_search.md         # required when no authoritative source is supplied
    original/
      meshy_input.png        # the only image sent to Meshy
      input_manifest.json
    firearms/<firearm_id>/
      meshy_input.png        # one firearm-only image per required gun
    equipment/<item_id>/
      meshy_input.png        # one item-only image per other required equipped item
    derived/                  # prepared ImageGen derivatives, comparisons, and processing evidence
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
```

Use the same derived path every time and pass job-relative paths to provider and adapter calls after root-containment checks. Do not use chat assumptions, timestamps, random IDs, pilot names, or workstation paths as the primary path. Keep append-only task history, manifest state, copy provenance, and dependency records inside the job root. Never archive secrets. Final runtime files must not remain runtime-referenced from `docs/assets/`.

Read and write job YAML, JSON receipts, and Markdown handoffs with explicit UTF-8, preserving the existing BOM and line endings.
Write metadata updates to a new sibling, parse and validate their required fields and array shapes, then replace the original; an unsupported parser option or failed parse must never overwrite a good receipt with null or `{}`.
If evidence metadata is recovered, mark it reconstructed and name the surviving measured inputs; leave lost fields unavailable instead of inventing them.

When `owner_id` identifies an event, the model job belongs under that event's temporary `docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/` evidence workspace. Keep source files, checkpoints, exports, manifests, QA evidence, and handoffs there while work is active, blocked, awaiting review, or undergoing acceptance scenarios. Before the event goal is genuinely complete, promote durable provenance, licensing, QA/reimport results, crosswalk facts, and runtime-handoff facts into permanent event, plan, spec, or other owner-approved documentation, place final runtime files in engine-facing folders, verify that no runtime reference points into `docs/assets/`, then delete the complete event-scoped workspace. Never delete skill-local references, durable portrait archives, or another event's workspace. Retain this workspace for blocked or incomplete work and report the blocker.

## Reference images

### Designed-artwork source-first reference gate

After the mandatory key and job-root gates, search for and select actual Internet-sourced modern designed artwork before approving any model reference. Build the candidate pool from game concept art, game character or unit art, game production or promotional art, tabletop or miniature concept art and renders, fantasy or horror illustration, and professional character or creature design sheets. Do not use archival photographs, museum works, historical paintings or drawings, historical plates, antiquities, archaeological images, ethnographic records, reenactment photography, or documentary imagery as model-reference candidates, shortlist entries, comparison images, or selected sources. Prefer official artist, game-studio, publisher, portfolio, or asset pages and sources with explicit reusable licensing. Use the repository's normal web-search workflow and record the search scope, queries, date, eligible artwork candidate URLs, rights decisions, and exact rejection reasons in `refs/source/source_search.md`.

Anime-derived presentation is a hard source and preflight rejection for 3D references and model-ready Meshy inputs. Reject obvious anime, manga, manhwa, chibi, cel-shaded anime-game-character styling, exaggerated anime facial or body proportions, and similar anime-derived presentation. This is not a blanket ban on grounded professional fantasy, horror, tabletop, or game concept illustration. Those remain eligible when their presentation is not anime-derived. Record the style decision and rejection reason in the source ledger and manifest, and do not use ImageGen cleanup to disguise or restyle an ineligible source.

The selected artwork must also fit the event's period and accepted unit brief. Unless the brief or spec explicitly intends an exception for that unit, reject modern electronics, digital devices, advanced optics, obvious modern plastics, contemporary tactical equipment, science-fiction machinery, and other technology or styling that does not belong in the 1936-1945-era world. Fantasy, supernatural, creature, or alternate-history elements remain eligible when they are the intended unit identity, but their ordinary equipment and technology must still respect the declared period boundary. ImageGen cleanup may not periodize, replace, or redesign an otherwise ineligible source. Select artwork that already passes the period-fit gate. Record the review and every intentional exception in the source ledger and manifest.

For firearm-bearing units, the prepared-input gate is the item-free body plus separate-firearm route defined under `Equipped items are generated separately and animated as an assembly`: retain source firearm identity, proportions, materials, and equipment references as the basis for a firearm-only Meshy input, but exclude all wielded items from the prepared body input. A source firearm need not already be held in a firing pose; Blender supplies the final scale, fit, grip, attachment, controls, locators, and action. Preserve the intended body, clothing, armour, period, non-anime style, and unit identity while cleaning the body pose and restoring source-obscured body areas. Declare `fires_in_combat` or `non_firing`; only firing consumers require discharge actions/effects.

Do not submit monochrome, clay-render, or untextured sources to Meshy. Prepare a colored derivative using an identity-, period-, role-, species-, and material-appropriate palette and retain color/source comparison evidence. Weapon exclusion, body-pose cleanup, and source-informed restoration for the firearm body route are authorized preparation steps and may be combined with colorization. Preserve intended identity and distinctive design; do not use colorization to conceal omitted components.

For each selected candidate, record the source URL/page, title, creator or publisher, stated license or terms, retrieval date, provenance and AI-use decision, and any explicit user authorization in `refs/source/provenance.json`. Licensed modern designed artwork is an allowed visual reference. A copyrighted source may proceed in `reference_only_user_authorized` mode when the user explicitly authorizes that actual artwork. The parent's broad authorization permits selecting and approving named source candidates without another per-source prompt unless provenance or terms are ambiguous or incompatible. This source-candidate authorization retains final prepared-input comparison and parent review before Meshy, including item-free body preparation when applicable. A license label alone does not override stated terms: reject explicit `NoAI`, no-derivatives, or other restrictions incompatible with generative reference use. Reject unclear provenance or terms unless explicit reference-only authorization applies and no explicit restriction forbids the workflow.

Treat the original source as immutable: never edit, resize, recompress, or send it as the ImageGen target, and never overwrite `refs/source/untouched.<ext>`. Where the terms permit local archival, preserve the selected source bytes unchanged as non-shipping evidence at that path. If the terms do not permit archival, transiently hash the retrieved bytes when permitted, discard them after review, and retain the source URL/page, identifying fingerprint, and provenance record without storing or shipping the source pixels. Stage every ImageGen operation on a separate derivative, never use source pixels as runtime art, and never leave a runtime reference pointing into the evidence workspace.

For a licensed or explicitly user-authorized source, use native ImageGen on a separate derivative to prepare one full, colored subject with genuine transparency or the required clean plain background. Preserve intended identity, proportions, clothing, armour, materials, palette, and distinctive traits. Record a neutral T-pose or A-pose when useful, or `pose_preparation_mode = none` with its reason. On the equipped-item route, strip equipped items, clean the body pose, and reconstruct obscured or missing required body detail using source-informed references; archive the identity of every excluded item and prepare a separate item-only reference for Meshy generation. Missing specified components are completion work, not permission to omit them. Record the exact prompt, comparison, pose mode, reconstructed and excluded elements, and parent review. Each derivative is a separate geometry task input under `Exactly one reference image per Meshy geometry task`.

If no eligible source survives provenance, rights, AI-use, or visual-identity review, mark the job `needs_user_review` or `blocked` and stop provider work. A source-free from-scratch reference is a distinct fallback that requires explicit parent/user approval after the documented search fails. Ordinary model-production authorization does not waive that fallback gate.

### Exactly one reference image per Meshy geometry task

Each Meshy geometry task receives exactly one approved, fully colored, full-subject image with genuine transparency or the required plain background. Use `refs/original/meshy_input.png` for the body; for firearm units this body image must be weapon-free. Prepare each required item as a separate item-only input under `refs/firearms/<firearm_id>/meshy_input.png` or `refs/equipment/<item_id>/meshy_input.png` and submit it through its own Meshy 7 geometry task, never alongside the body or another item. Preserve intended identity and distinctive non-equipment traits while allowing authorized weapon exclusion, pose cleanup, and restoration. Record source URL, creator, terms, rights/AI-use status, prompt, comparison, pose mode, and parent review for every task. Never submit multi-view boards, comparison sheets, search-result pages, or additional images to a single geometry task; never overwrite immutable source evidence. A source-free fallback still needs separate approval after documented search failure. An unavailable required provider route remains a blocker.

Preflight each input before generation for non-anime style, intended period and identity, alpha/background quality, complete color and material cues, and provenance/AI-use rights. Body inputs also require complete readable anatomy, full body coverage, limb separation, and pose preparation. For firearm units, verify zero firearms or wielded props in the body image, one complete isolated gun in each firearm-only image without a character, hands, or unrelated equipment, and a complete generation and assembly inventory linked to source equipment evidence; authorized body-pose normalization and restoration do not need to preserve source weapon contacts. Validate the complete trigger-hand, support-hand, stock/shoulder, and clear-muzzle relationship on the assembled Blender model and every firing action, rejecting unintended barrel-held, slung, fused, obscured, floating, or otherwise non-fireable contacts there; hand, stock, and muzzle checks apply to the assembled model, not to the item-free body input. If the applicable input or assembled-model gate cannot pass, mark the job `needs_user_review` or `blocked`. A declared `non_firing` firearm-bearing unit must have no firing roles or effects. Restore missing specified elements through the authorized source-informed preparation and Blender completion routes; do not hide omissions. Preserve immutable sources, prompts, comparisons, and parent review before generation.

For a sourced artwork with an unwanted opaque background, request genuine transparency in the ImageGen preparation and preserve the alpha channel in the prepared input. A clean plain background is acceptable when transparency is not required by the consumer. Preserve the source and prepared evidence, and reject halos, matte pixels, clipped geometry cues, internal alpha holes, cast-shadow remnants, or design drift. A verified local background-removal or chroma-key process is a documented fallback only when the ImageGen preparation fails transparency. It must not replace the preparation or silently alter the design.

Do not create or submit a turnaround sheet, multi-view board, collage, side-profile set, or separate front/rear images. Vanilla references may be imported into Blender read-only for calibration, and Blender may render front, rear, side, top, underside, wireframe, or material QA views after generation, but none of those views is a Meshy input or may be sent back to the provider.

#### Portrait fidelity gate

For a portrait-inspired custom unit, compare the prepared candidate against the source portrait before any paid Meshy call and preserve the exact head or face identity, silhouette, proportions, clothing or anatomy, distinctive attachments, palette, and intended unit identity. Preserve the source pose unless the approved derivative records `pose_preparation_mode = t_pose` or `pose_preparation_mode = a_pose` without unintended identity drift; the equipped-item route strips source items for separate Meshy generation and may restore hidden body details. Do not accept a generic redesign that preserves only the unit category. Require explicit parent or user acceptance of the source-to-prepared comparison. Without it, mark the job `needs_user_review` or `blocked` and do not call Meshy. Record the source/prepared comparison, exact prompt, pose mode and reason, approval or status, and revision lineage in the job manifest, with each revision identifying its predecessor. Reference review is separate from provider generation, under `Exactly one reference image per Meshy geometry task`.

## Provider generation and lineage

For a new model, the provider sequence is:

```text
verified balance -> image-to-3D -> status -> immediate download
                 -> optional remesh/retexture
                 -> Meshy rig task for a provider-eligible bipedal body
                 -> Meshy preset actions or Meshy Text-to-Motion
                 -> receipt-verified ingestion onto the rig
                 -> live Blender authoring for every asset the provider route does not cover
                 -> deformation/visual QA -> PDX export/reimport
```

Each provider stage keeps its own task id, credit preflight, reconciliation, and download record, and a paid rig or animation attempt is not repeated. Provider results are ingested into the job through the ingestion operations listed under `Adapter publication`.

Failed geometry generation, remesh, retexture, or conversion retains the authorized provider-recovery path while balance and verified capability permit it. A rig result or an action result that the provider cannot deliver to this standard is repaired in the live Blender session or reported as the exact blocker, under the generation policy in `Skeleton, skinning, and action policy`. Inspect the live schema and balance before paid calls, preserve estimates and task/response IDs, and never expose the API key. Do not promise a general geometry prompt when Image-to-3D exposes only texture-direction text.

Before a humanoid source over 300,000 triangles reaches `meshy_remesh`, every job manifest and generated spec must declare the verified `remesh_estimate_credits = 5` estimate, or the loader must apply and materialize that verified default. The runner must never index an undeclared `remesh_estimate_credits` key.

Use **Meshy 7** as the only image-to-3D generation model. Require the verified repository-owned route to expose the exact `meshy-7` identifier and record it in task evidence. Never silently downgrade or use a model alias. If Meshy 7 is unavailable or incompatible, stop with `needs_user_review` or `blocked`.

The ordinary planned paid path is pre-authorized. Do not ask for confirmation before the initial model generation, before planned remesh, retexture, and conversion calls belonging to the accepted brief, or before the planned humanoid rig task and its planned animation tasks. Check the live balance before each batch of paid operations and record estimates, operations, attempt numbers, and consumed credits, but routine credit use and balance checks are not confirmation gates.

For the live locked Meshy MCP route with `ai_model=meshy-7`, `enable_pbr=true`, and `should_texture=true`, require a live cost/preflight record before the image-to-3D call and reconcile it with the response and post-call balance. The documented textured Meshy-7 charge is 30 credits. Never use the upstream MCP package's stale 20-credit prose for planning or reconciliation.

When geometry recovery is authorized, keep the rejected task, responses, downloads, and QA evidence immutable. Give the retry an explicit attempt-scoped provider stage such as `generation_recovery_2`, and derive its model filenames, extracted texture directory, credit preflight, selected task, and every downstream Blender source from that stage. Never let a generic `generation` task or filename select a rejected predecessor. Do not use broad response-name recovery for an attempt-scoped stage because provider response filenames do not encode the logical attempt. Resume it only from its exact task record. Preserve the earlier evidence in place rather than renaming, deleting, or overwriting it.

For geometry, remesh, retexture, or conversion recovery, do not repeat an identical input after two failures. Where separately authorized and supported by the official MCP schema, `model_url` may use an official `https://assets.meshy.ai/` artifact URL from the immutable completed source-task record; bind it to that source, redact signed URLs, and retain its own attempt record. Do not use URL substitution, changed identifiers, or a new stage name to bypass the provider attempt and recovery rules.

Prefer smart topology when suitable, triangular output, PBR maps when textures are required, and removal of baked lighting when supported. A humanoid body reference should depict a complete readable body. Each equipped item is generated through its own Meshy 7 geometry task from one item-only prepared image, then imported into Blender for scale, topology, material, fit, attachment, locator, and contact work under `Equipped items are generated separately and animated as an assembly`. Use native ImageGen on a separate derivative to attempt a neutral T-pose or A-pose when feasible, while retaining the original pose with `pose_preparation_mode = none` and a recorded reason when neutralization would break required body anatomy or intended identity. Use the suitable provider pose or `none` for static or mechanical assets. Download every successful artifact immediately, retain the GLB as the canonical provider archive, retain FBX when a downstream route needs it, and record exact arguments, provider version, task IDs, request/response lineage, credits, and local download paths. Remote URLs are never the only accepted copy.

Treat every provider result as a candidate. Review textured/untextured, wireframe, and relevant front/rear/side/top/underside views for identity, topology, anatomy, and component completeness. Author or restore missing required components and repair detached, fused, or broken geometry in Blender without renewed approval, preserving intended identity and source evidence. Regenerate only when a usable body or separate firearm candidate cannot be repaired through verified operations. Item-free bodies intentionally omit equipped items until the separately generated item assets are fitted and attached in Blender; the assembled candidate must contain every required element before acceptance. Do not spend provider credits on a rejected geometry candidate. Preserve all candidate lineage.

Tutorial values near 10,000 vertices and the 25,000–30,000 caution band are seed heuristics only. Local vanilla calibration and measured runtime evidence decide the profile target.

## Skeletal authoring gate

Required articulated motion needs real bones, skinning, and authored skeletal actions. Use the verified live authoring session for unsupported or unusable provider results.
Read the complete requirements in [Skeletal authoring gate](references/blender-processing-and-export.md#skeletal-authoring-gate) before this work.

## Blender processing and checkpoints

Preserve provider originals and work in staged Blender checkpoints with the required dependency and topology checks.
Read the complete requirements in [Blender processing and checkpoints](references/blender-processing-and-export.md#blender-processing-and-checkpoints) before this work.

## Geometry, materials, rigging, and actions

Complete all required components, calibrated geometry and PDX materials, weights, semantic actions, contacts, and family consumers.
Read the complete requirements in [Geometry, materials, rigging, and actions](references/blender-processing-and-export.md#geometry-materials-rigging-and-actions) before this work.

## Custom unit-counter companion

Every custom unit needs bespoke counters for all of its runtime surfaces, using exact installed-vanilla definitions, DDS references, and the matching reference family.
Read the complete requirements in [Custom unit-counter companion](references/unit-audio-and-counters.md#custom-unit-counter-companion) before this work.

## Custom unit sound-design companion

Every custom unit needs legally usable Internet-sourced audio with selection and applicable action roles, exact attribution, and animation synchronization. Generated or placeholder audio cannot satisfy this contract.
Read the complete requirements in [Custom unit sound-design companion](references/unit-audio-and-counters.md#custom-unit-sound-design-companion) before this work.

## PDX export and reimport evidence

Export and reimport the actual deliverables, checking skeleton, materials, scale, and action coverage before handoff.
Read the complete requirements in [PDX export and reimport evidence](references/blender-processing-and-export.md#pdx-export-and-reimport-evidence) before this work.

## Evidence package and handoff

The job package must contain, as applicable:

- job intake and append-only history
- selected source and source-informed model-ready preparation or documented failed-search fallback, preflight, non-anime style decision, source URL/page, title, creator/publisher, stated license/terms, retrieval date, provenance and AI-use decision, explicit user authorization, declared period-fit review and intentional exceptions, source color status, palette direction, colorization evidence when applicable, preparation prompt, source-to-prepared comparison, `pose_preparation_mode` and reason, parent approval, and evidence that any archived source bytes are non-shipping
- for every firearm-bearing unit, firearm/body route selection, `fires_in_combat` or `non_firing`, weapon-free prepared-body proof and separate firearm-only input/task records when generating that geometry, complete prop inventory, the provider body rig and its ingested action lineage, Blender fit/attachment and contact evidence, and assembled per-frame trigger-hand, support-hand, stock/shoulder, muzzle and recoil checks. Every firing state requires discharge timing, locator, synchronized effects/light, licensed weapon-matched sound; `non_firing` records zero firing-state/effect/sound requirements
- provider requests, responses, task IDs, versions, balance, credits, downloads, and retained passing outputs
- requested operation and route selection, the complete required-component inventory and added-geometry/prop provenance, the provider rig and animation tasks with their exact source action ids and provenance receipts, the ingestion or live Blender authoring session record, exact adapter operations and arguments, rig/weight/action checkpoints, and before/after deformation and role-motion review
- source and checkpoint `.blend` files
- geometry, material, rig, weight, action, and export reports
- source and final textures, animation previews, `.mesh`, and `.anim`
- immutable Internet-sourced unit audio candidates, licensing records, derived files, and transformations
- export/reimport evidence, manifest, and requirement-to-runtime crosswalk
- a runtime handoff with proposed stable names, paths, material/shader mapping, action mapping, and the exact files/identifiers the parent must wire
- for every custom unit, a sound-design handoff with sourced audio files, source URLs, attribution, licensing evidence, sound roles, voice direction where applicable, vanilla precedents, animation synchronization points, proposed runtime identifiers, and remaining parent-owned wiring
- for every custom unit, a counter handoff with inspected installed-vanilla definitions and DDS files, matching skill-local counter family, exact consumers and tokens, required frames/states/sizes, original counter-art paths, final DDS paths, sampled vanilla green evidence, comparison evidence, proposed sprite definitions, and remaining parent-owned wiring
- for static buildings, footprint/scale evidence, meshsettings object-name evidence, dedicated spawn or provincial-anchor evidence, and runtime-consumer evidence

Each model manifest entry records the asset ID/slug, profile, source mode, source reference, source URL/page, title, creator/publisher, stated license/terms, retrieval date, explicit authorization where applicable, provenance and AI-use decision, non-anime style-gate status, declared period fit and every intentional exception, source and final color status, palette direction, colorization prompt/comparison/approval when applicable, source-informed preparation prompt, route selection, weapon-free input proof where applicable, missing-component inventory, Blender-authored component/prop and attachment evidence, source-to-prepared comparison and approval, `pose_preparation_mode` and reason, firearm intent (`fires_in_combat` or `non_firing`) and explicit complete-weapon, trigger-hand, support-hand, stock/shoulder, and muzzle-continuity results when applicable, provider lineage, the provider rig task and animation tasks with their exact source action ids and provenance receipts, selected candidate, the ingestion or live authoring session and accepted checkpoint, geometry counts, objects/materials, armature/bones, actions/frame data, explicit `attack`, `defend`, `support_attack`, and additional-state discharge and muzzle/effect/sound synchronization rows or a zero firing-state/effect/sound audit for `non_firing`, custom-unit sound requirements and synchronization points, custom-unit counter consumers, installed-vanilla counter references, sampled green evidence, bespoke counter handoff and status, source/final textures, exports, exporter version/settings, proposed runtime identifiers, actual runtime registration only after parent wiring, live consumer, user-provided in-game evidence only after parent review, and status. Use `complete`, `needs_user_review`, `blocked`, or `canceled`. Never create a fallback completion state.

For nonhumanoid/creature jobs, `manifest.md` and `runtime/handoff.md` must repeat the measured numeric scale crosswalk, dedicated rig route, `scale_crosswalk_status`, `rig_route_status`, provider/export route status, and the exact blocker text for every unavailable or pending route. A bare `blocked` or `pending` label is insufficient.

When the event/system owner and slug are known, place the subagent handoff under the parent-provided `docs/plans/<owner_id>_<owner_slug>_plans/subagent_handoffs/` path. The parent must review every artifact and either wire it, queue it with a reason, reject it with a reason, or carry its blocker forward.

### Runtime copy synchronization

Treat the selected source exports, staged runtime copies, and active consumer files as separate surfaces. A runtime file can be stale or be overwritten by an older mapped texture even when the current source export is correct. Select the final geometry, material maps, and actions first, then lock the selected source paths in the manifest before synchronizing any runtime copy. Record each source and destination path, source and destination SHA-256, copy tool or actor, copy time, and provenance link, then compare destination hashes after synchronization. Never synchronize from an older provider or processed path, never let a filename alone choose the source, and never synchronize before final source selection. The parent owns active runtime copies, `.asset`, entity, `.gfx`, gameplay wiring, and live consumer bindings. The user supplies in-game screenshots and live validation. The worker owns the evidence and exact handoff needed for parent wiring and review.

## Bounded subagent route

Use `chaosx_3d_model_pipeline` only when the parent provides the exact job root, approved source or model-input paths, output folders, handoff path, profile, named vanilla references, scale relationship, required actions with their rig map and root policy, custom-unit sound roles and Internet-source requirements, custom-unit counter consumers and tokens, inspected vanilla counter definition/DDS paths, matching skill-local counter family, counter-artist handoff path, synchronization requirements where applicable, source mode and permissions, dependency lock, and forbidden simplifications. The subagent's production scope, including crosswalk rows and handoffs, and its ban on final gameplay, GFX, entity, sound-definition, localisation, and spreadsheet wiring are the ones in `Ownership and completion boundary`, and the user performs live consumer validation and supplies in-game evidence.

### Source eligibility in the prompt

The prompt must require the source, style, and period gates stated in `Designed-artwork source-first reference gate`, including the `reference_only_user_authorized` path, the `NoAI` and no-derivatives rejections, and the eligible non-anime source families. The prompt must also declare the event or system's period boundary and every explicitly intended exception.

### Firearm route in the prompt

For every firearm-bearing unit, the prompt must carry the route in `Route selection and component completion` and the input rules in `Equipped items are generated separately and animated as an assembly`, and must declare `fires_in_combat` or `non_firing`. Require independent body and item task IDs, credits, downloads, source-identity comparisons, the Meshy rig task for the body, the Meshy preset-action or Text-to-Motion tasks, receipt-verified ingestion of every transferred action, rigid-control attachment, and completion of all missing specified parts without renewed approval. Require grip, stock, and muzzle contact; aim, discharge, recoil, and recovery phases; independent `attack`, `defend`, `support_attack`, and additional firing-state timing, locator, particle/light, licensed sound, and synchronization rows; and, for `non_firing`, retained equipment with the zero firing-state/effect/sound audit.

### Prepared-input evidence in the prompt

The prompt must require the prepared-input gates in `Designed-artwork source-first reference gate` and `Exactly one reference image per Meshy geometry task`. Colorization may accompany authorized item exclusion, pose cleanup, and source-informed body restoration; preserve the intended identity, material distinctions, and non-anime style, and record source/final color status, prompt, comparison, and parent review. For a selected source, native ImageGen must create one source-informed model-ready derivative with a full colored body, an identity- and period-appropriate palette, a suitable transparent or plain background, and non-anime style. Preparation may strip equipped items, restore obscured or missing body detail, and normalize to a useful T-pose or A-pose without preserving source item contacts. Archive the identity of every excluded item and its reconstruction references for Blender. Complete all missing specified model elements through the authorized Blender route rather than accepting omissions, and record the prompt, source-to-prepared comparison, pose mode, reconstructed and excluded elements, and parent review. Sources and prepared references remain non-runtime evidence.

### Failed search and provenance in the prompt

If the documented search across eligible artwork families finds no suitable source, mark the reference `needs_user_review` or `blocked`, and hold the source-free from-scratch fallback to the separate approval gate in `Designed-artwork source-first reference gate`. Record that section's provenance and archival fields, including the exact ImageGen preparation prompt, the source-to-prepared comparison, and `pose_preparation_mode` with its reason.

### Provider tasks and context in the prompt

Each Meshy 7 geometry task must receive exactly one approved, fully colored source-informed image under the paths in `Exactly one reference image per Meshy geometry task`; sources and comparison sheets remain evidence only. The provider sequence is the one in `Provider generation and lineage`; the route, separate item generation, ingestion onto the rig, live fitting and attachment, and Blender-only operations are the ones in `Route selection and component completion` and `Equipped items are generated separately and animated as an assembly`. All missing required model components are authorized Blender completion work without renewed approval. Keep geometry-recovery rules, live credit preflight for provider calls, and recorded attempt/source lineage. Put every needed conversation constraint into the prompt or named repository files.

## Final state and fallback disclosure

Mark each requested 3D requirement as `complete`, `needs_user_review`, `blocked`, or `canceled` in the package. A requirement produced through a shortcut is not `complete`: mark it `blocked` or `needs_user_review` and name the shortcut that was avoided. For a custom unit, the package must also record the sourced sound candidates, licensing evidence, synchronization handoff, bespoke counter package, installed-vanilla counter inspection evidence, and parent-owned audio/counter wiring status. A package-level `complete` means the worker's requested source, processing, export, sound-source research, counter handoff, and evidence outputs are present. It does not mean the Chaos Redux runtime feature is complete. Report every omitted component, rejected candidate, unverified capability, budget stop, missing reimport proof, missing sound source, missing counter, and proposed static companion explicitly. Never hide a simplification behind a successful export or a parent-owned runtime handoff.

---
name: chaos-redux-3d-model-pipeline
description: Use when creating, rigging, animating, converting, exporting, auditing, or documenting a custom Hearts of Iron IV 3D model, Internet-sourced sound-design handoff, and bespoke vanilla-green counter handoff for a Chaos Redux unit, building, vehicle, aircraft, ship, creature, or articulated asset.
---

# Chaos Redux 3D Model Pipeline

Use this skill for final 3D geometry and skeletal animation assets. It covers the bounded path from one approved reference image through provider generation, Blender normalization, PDX materials, rigs, actions, Paradox export, QA evidence, and a parent-owned runtime handoff.

Do not use it to draw 2D equipment illustrations, unit counters, focus or idea icons, 2D frame-sheet animation, leader portraits, or concept-only requests. The 3D workflow owns the custom-unit counter requirement, vanilla-reference gate, and bounded artist handoff, while final counter art remains with `chaos-redux-event-assets` and `chaosx_icon_artist`. Other 2D surfaces remain with `chaos-redux-event-assets` and `chaos-redux-frame-animation` where applicable.

## Ownership and completion boundary

A provider result is a source candidate, a `.blend` is a working artifact, and a `.mesh` or `.anim` is a runtime candidate. The package is not complete merely because a provider task, Blender preview, or export succeeded. Completion requires the exact runtime registration, a live consumer, and in-game evidence owned by the parent implementation agent.

The 3D worker may create source files, Blender checkpoints, textures, `.mesh`, `.anim`, sourced unit-audio candidates, mechanically derived audio, previews, manifests, reports, and handoffs. It must not edit gameplay, sound definitions, localisation, `.gfx`, `.gui`, `.asset`, entity, event, focus, decision, country, history, AI, on-action, or spreadsheet files unless the parent grants a narrow exception explicitly. The parent owns runtime identifiers, source wiring, live consumer validation, and the overall completion claim.

`chaos-redux-event-assets` remains the owner of broad asset inventories, source provenance conventions, texture/DDS conventions, and requirement-to-runtime coverage across asset types. Keep model geometry, model materials, entity wiring, and any separate 2D concept reference distinct. `chaos-redux-frame-animation` governs 2D frame-sheet animation; it does not replace skeletal 3D `.anim` production.

Every new custom unit, custom subunit, creature, vehicle, aircraft, or ship also requires a custom sound-design package. The 3D worker must research the Internet for legally usable sourced audio, preserve the original downloads and licensing evidence, define the required sound roles, map animation synchronization points, inspect vanilla precedents, propose runtime identifiers, and write the handoff. The parent owns final sound definitions, runtime wiring, and in-game validation, while mechanical trimming or format conversion remains allowed only when it preserves the sourced file and its license permits the transformation.

Every new custom unit also requires new counter art for every counter surface it uses. The counter must be original to that unit, use the exact vanilla green counter palette sampled from the inspected reference, and follow the installed-vanilla consumer and visual style. Inspecting the closest matching installed-vanilla counter definition and DDS plus the matching skill-local counter reference family is a hard gate. A reused vanilla counter, renamed existing counter, generic placeholder, arbitrary green counter, or counter created without recorded vanilla-reference inspection cannot satisfy completion. Route counter production through `chaos-redux-event-assets` and `chaosx_icon_artist`; the parent owns final GFX and gameplay wiring.

Final unit audio is source-only. The worker must never create, synthesize, record, generate, or manually author sound, and must never replace a missing source with test tones, primitive waveforms, placeholder beeps, noise beds, or an unlicensed stock effect. If a suitable sourced file cannot be found and licensed, mark the affected role or package `blocked`.

## Hard start gates

The first process check is `MESHY_API_KEY`, which must be a non-blank process environment variable before any path discovery, job intake read, reference inspection or generation, route discovery, balance check, provider call, or downstream work. If the key is missing or blank, stop immediately, print this exact PowerShell command, and tell the user to restart the shell or Codex:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

Do not resolve the repository root or job root, read a job or brief, inspect or generate a reference, discover a route, call balance, make a provider call, invoke Blender, or begin downstream work before this gate passes.

After the key gate passes, resolve the repository and job roots from repository-owned files, then run the repository-owned bootstrap before any balance or paid/provider call. The bootstrap must resolve the latest official Meshy package, latest Blender Lab MCP release or default-branch head, the discovered Blender executable/build, and the latest io_pdx_mesh release, then write the exact observed resolution and checksums to `.tools/3d_pipeline/config/dependencies.lock.json`. It must also install and enable the matching Blender MCP add-on in the discovered Blender extension repository, configure the add-on's resolved bridge endpoint, start Blender when needed, and verify that the bridge is reachable. Treat that file as generated evidence with `resolution_policy = latest_at_bootstrap`, not as a permanent version pin. Read the adapter version from `routes.blender_hoi4_adapter.version` in that lock for every run; any version repeated in role, skill, README, or template prose is non-authoritative evidence only. Verify the selected Meshy route, the narrow repository-owned `chaosx_blender_hoi4` adapter route when the repository provides one, the resolved Blender server and add-on route, the reachable bridge, and the latest io_pdx_mesh installation. A running Blender process is not proof that the configured bridge is listening: probe `127.0.0.1:<socket_port>` separately using `blender_mcp_addon.socket_port` from the lock, and when it is absent start the lock-selected Blender executable in hidden background mode with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port <socket_port>`, then probe again and record the result. If latest resolution, live schema, add-on installation, bridge reachability, compatibility, or checksum verification fails, stop and report `required installation/verification` or `blocked`; do not substitute an older dependency or invent a live MCP/tool name.

Record the exact verified server package, version, git head, route or wrapper, schema version, actual tool identifiers, paid flags, input exclusivity, required arguments, adapter operation names and arguments, Blender build, extension manifest, archive checksum, dependency-lock checksums, provider task IDs, response IDs, and output checksums. The current verified Meshy tool identifiers include `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`; use only names returned by the live locked route and record the exact arguments used. If a required route, schema, package, version, checksum, or capability is missing or mismatched, stop and report `required installation/verification` or `blocked`; do not install packages, substitute an unapproved route, or invent a live MCP/tool name.

Inspect the repository-owned route's live `meshy_image_to_3d` declaration before provider work, require the explicit `ai_model=meshy-7` identifier, and record that exact model in task evidence. When Meshy's official API changes before the published MCP package catches up, update and verify the repository-owned compatibility wrapper against the official API documentation, require a `tools/list` proof that `meshy-7` is exposed, and keep all provider work inside that MCP route. Do not hide a direct REST fallback, use an alias in job manifests, or relabel an older generation. Tie credit preflight to Meshy 7.

Treat the compatibility wrapper as deterministic production code. Apply its schema patch exactly once per runtime file, preserve UTF-8 without re-encoding growth, enforce a maximum patched-file size, and prove idempotence with two consecutive `tools/list` calls whose patched-file checksums or sizes match. Every one-shot stdio call must terminate only the descendants spawned beneath its own wrapper process after the response or timeout; a successful tool response with leaked provider processes is a failed route-health check.

Keep provider and Blender integration guidance in this skill and the job's dependency lock. Do not create a central MCP router or tool-specific wrapper. Any viewer, inspector, renderer, or comparison route used for QA must be read-only. This package does not provide unrelated viewers, including a Technology Tree Viewer; record such a capability as absent when requested.

There is no silent fallback or simplification. Discuss every fallback with the parent/user before use and record the decision. If approval is not explicit, mark the item `blocked` or `needs_user_review`. A static animation fallback is an explicit companion artifact for review or unavailable motion, never a replacement for a requested skeletal action.

After the key gate and job-root resolution, the job loader must preflight every `nonhumanoid_creature` or other nonhumanoid/creature job before any balance check or paid/provider call. Require a declared, measured `scale_crosswalk` with units and finite numeric reference dimensions, provider/Blender target dimensions, entity scale, effective runtime dimensions, and conversion or fit factor, plus a named dedicated custom-rig route and written rig map. Reject missing, pending, placeholder, non-numeric, or unmeasured crosswalk values; do not infer them from profile defaults. This preflight is also a hard gate before provider generation or export.

## Required reading and local calibration

Before 3D work, read:

- `AGENTS.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md` when a subagent is used.
- The parent brief, accepted spec, plan, manifest, job, dependency lock, and handoff.
- The offline Paradox wiki pages relevant to the target surface, especially `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`.
- Relevant character or interface pages when the target consumes those systems.
- Relevant documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.
- Local vanilla `.mesh`, `.anim`, `.asset`, entity, material, texture, and model precedents for the exact domain, plus existing Chaos Redux model precedents.
- For custom units, the exact installed vanilla sound, voice, soundeffect, and entity precedents used by the closest matching unit surface.
- For custom units, the exact installed vanilla counter consumer, sprite definition, DDS, canvas, frame order, alpha treatment, and closest visual precedent, plus the matching `chaos-redux-event-assets/assets/vanilla_reference/units/` counter family and contact sheet.

Use existing Chaos Redux paths under `gfx/models/` and `gfx/entities/` as local precedents where applicable, but confirm the final path, shader, material channels, scale, axes, skeleton, action names, and entity structure against the installed vanilla version. Do not lock tutorial values or assume that a nearby asset belongs to the same runtime surface. Treat tutorial polygon counts, texture dimensions, and provider defaults as starting heuristics only; the installed game and latest verified toolchain decide acceptance.

For a humanoid land-unit pilot, this is a hard calibration gate, not a suggestion: import the installed vanilla infantry `.mesh` into the Blender reference collection read-only, identify the exact entity and runtime `scale`, exclude collision-only geometry, and record the measured source-mesh height, effective runtime height, forward axis, ground contact, and the comparison result in the job and manifest. When the custom entity retains the vanilla entity scale, normalize the exported mesh to the measured source-mesh height so the engine applies that scale exactly once; do not normalize to the effective runtime height and then multiply it by the entity scale again. Do not use a generic real-world height or an arbitrary entity `scale` as a substitute. Keep the provider/animation height and the Blender source-mesh calibration height as separate fields when the provider and HOI4 coordinate spaces differ.

For a static map-building pilot, this is also a hard calibration gate: import the installed vanilla mesh used by the actual building entity, identify the exact `pdxmesh` and entity scale, measure the source dimensions and effective runtime dimensions, and record the reference in the job and manifest. Height-only calibration is invalid for buildings. The current `building` profile uses `facility_land.mesh` with `building_land_facility`, source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a hard runtime X/Y footprint ceiling of `4.0` meters. A candidate over that ceiling must be explicitly fit with one uniform X/Y factor and must record before/after dimensions; silent anisotropic stretching is forbidden.

## Job intake and deterministic layout

Validate the job before any paid work. The parent must provide:

- event or system owner, stable asset ID, and lowercase asset slug
- one ready reference image path and checksum, or enough brief input to generate it
- source provenance, license status, or explicit user-provided authorization
- one asset profile: `static_prop`, `building`, `humanoid_unit`, `nonhumanoid_creature`, `vehicle_land`, `aircraft`, `naval`, or `articulated_attachment`
- geometry intent, required components, forbidden additions, texture direction, and unseen-side/rear-geometry policy
- named vanilla reference paths and the expected scale relationship
- for buildings, the measured runtime footprint budget and whether the consumer is a dedicated provincial map building or a state-level gameplay building with a provincial visual anchor
- required action roles, runtime consumer, baseline planned paid operations, extra-recovery credit limit, and extra paid-attempt limit
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
    original/
      meshy_input.png        # the only image sent to Meshy
      input_manifest.json
    derived/                  # optional, approved clarification only
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

Use the same derived path every time and pass job-relative paths to provider and adapter calls after root-containment checks. Do not use chat assumptions, timestamps, random IDs, pilot names, or workstation paths as the primary path. Keep append-only task history, manifest state, checksums, copy provenance, and dependency records inside the job root; never archive secrets. Final runtime files must not remain runtime-referenced from `docs/assets/`.

When `owner_id` identifies an event, the model job belongs under that event's temporary `docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/` evidence workspace. Keep source files, checkpoints, exports, manifests, QA evidence, and handoffs there while work is active, blocked, awaiting review, or undergoing acceptance scenarios. Before the event goal is genuinely complete, promote durable provenance, licensing, checksums, QA/reimport results, crosswalk facts, and runtime-handoff facts into permanent event, plan, spec, or other owner-approved documentation, place final runtime files in engine-facing folders, verify that no runtime reference points into `docs/assets/`, then delete the complete event-scoped workspace. Never delete skill-local references, durable portrait archives, or another event's workspace; retain this workspace for blocked or incomplete work and report the blocker.

## Exactly one Meshy reference image

Meshy receives exactly one clean final reference image. If the parent supplies one, preserve it and use it only after checksum and rights preflight. If no image is supplied, generate exactly one production reference through the approved image-generation route, save it as `refs/original/meshy_input.png`, and retain its prompt, source mode, checksum, and approval note. If that route is unavailable, mark the job as `required installation/verification` or `blocked` rather than substituting.

Do not create or submit a turnaround sheet, multi-view board, collage, side-profile set, or separate front/rear images. Vanilla references may be imported into Blender read-only for calibration, and Blender may render front, rear, side, top, underside, wireframe, or material QA views after generation, but none of those views is a Meshy input or may be sent back to the provider.

Preflight the one input for silhouette, cropped parts, limb/component separation, dark gaps, strong shadows, background complexity, thin structures, painted details that may be mistaken for geometry, symmetry/asymmetry, unseen-side ambiguity, and source rights. An approved derived image may clarify exposure, background, or an accidental seam; it may not silently redesign the subject. Keep the original and both checksums.

### Portrait fidelity gate

For a portrait-inspired custom unit, compare the candidate reference against the source portrait before any paid Meshy call and lock the head/face identity, silhouette, proportions, clothing/anatomy, distinctive attachments, and palette. Do not accept a generic redesign that preserves only the unit category. Require explicit parent or user acceptance of the comparison; without it, mark the job `needs_user_review` or `blocked` and do not call Meshy. Record the source/candidate comparison, acceptance or status, and revision lineage in the job manifest, with each revision identifying its predecessor. Reference review is separate from provider generation: after approval, exactly one approved provider image is sent to Meshy, while the source portrait and comparison views remain evidence only.

## Provider generation and lineage

The normal provider sequence is:

```text
verified balance -> image-to-3D -> status -> immediate download
                 -> optional remesh/retexture
                 -> optional suitable humanoid rig/animation candidate
```

For a configured humanoid family batch, the runner may use one verified standard humanoid rig and one provider idle/attack/death action set as the animation source for several distinct generated geometries. This is a credit-aware family route, not a static fallback: every unit still receives its own Meshy geometry task, dual-source weight transfer, textures, `.mesh`, four exported `.anim` files, and per-action reimport proofs. The shared source must be recorded with owner task IDs, copied-artifact checksums, and recipient lineage; recipient geometry may never be reused.

Use the repository batch entrypoint `python .tools/3d_pipeline/run_pilot.py --specialized-zombie-batch <configured_batch_id>` when a job manifest declares `shared_humanoid_batch`, `shared_humanoid_rig_owner`, and `shared_humanoid_role`. The owner pays for the standard rig and provider actions; recipient humanoids use the locked dual-source Blender preparation and import each shared action onto their own armature. Creature jobs in the same batch remain on their dedicated custom-rig route.

Before a humanoid source over 300,000 triangles reaches `meshy_remesh`, every job manifest and generated spec must declare the verified `remesh_estimate_credits = 5` estimate, or the loader must apply and materialize that verified default; the runner must never index an undeclared `remesh_estimate_credits` key.

Use **Meshy 7** as the only image-to-3D generation model. Require the verified repository-owned route to expose the exact `meshy-7` identifier and record it in task evidence. Never silently downgrade or use a model alias. If Meshy 7 is unavailable or incompatible, stop with `needs_user_review` or `blocked`.

The ordinary planned paid path is pre-authorized. Do not ask for confirmation before the initial model generation or before planned remesh, retexture, rigging, conversion, and required animation calls belonging to the accepted brief. Check the live balance before every paid tranche and record estimates, operations, attempt numbers, and consumed credits, but routine credit use and balance checks are not confirmation gates.

For the live locked Meshy MCP route with `ai_model=meshy-7`, `enable_pbr=true`, and `should_texture=true`, require a live cost/preflight record before the image-to-3D call and reconcile it with the response and post-call balance. The documented textured Meshy-7 charge is 30 credits; never use the upstream MCP package's stale 20-credit prose for planning or reconciliation.

Ask for confirmation only before additional paid recovery made necessary by a failed or rejected generation, remesh, retexture, rig, conversion, or animation attempt. State the failed operation, credits consumed, proposed extra operation, estimated extra cost, and remaining balance. In every other case, do not ask for credit-spend confirmation. Inspect the live schema before paid calls; do not promise a general geometry prompt when the current Image-to-3D surface exposes only texture-direction text. Record the exact verified arguments and response/task IDs without exposing the API key.

When recovery is authorized, keep the rejected task, responses, downloads, checksums, and QA evidence immutable. Give the retry an explicit attempt-scoped provider stage such as `generation_recovery_2`, and derive its model filenames, extracted texture directory, credit preflight, selected task, and every downstream Blender source from that stage. Never let a generic `generation` task or filename select a rejected predecessor. Do not use broad response-name recovery for an attempt-scoped stage because provider response filenames do not encode the logical attempt; resume it only from its exact task record. Preserve the earlier evidence in place rather than renaming, deleting, or overwriting it.

Prefer smart topology when suitable, triangular output, PBR maps when textures are required, removal of baked lighting when supported, and A/T pose for a riggable humanoid. Use the suitable provider pose or `none` for static or mechanical assets. Download every successful artifact immediately, retain the GLB as the canonical provider archive, retain FBX when a rig/action route needs it, and record exact arguments, checksums, provider version, task IDs, request/response lineage, credits, and local download paths. Remote URLs are never the only accepted copy.

Treat every provider result as a candidate. Review front, rear, sides, top, and underside where relevant, plus wireframe, untextured shading, and textured views. Block on rejected geometry and ask for confirmation before any additional paid recovery attempt for missing major components, floating critical parts, fused limbs/weapons/turrets/wings, open holes, identity mismatch, broken thin structures, or unacceptable unseen-side invention. Do not spend retexture, rig, or animation credits on rejected geometry. High-detail generation followed by controlled reduction is allowed only when the job explicitly permits it and the lineage records both candidates.

Tutorial values near 10,000 vertices and the 25,000–30,000 caution band are seed heuristics only. Local vanilla calibration and measured runtime evidence decide the profile target.

## Blender processing and checkpoints

Use a versioned scene template with protected provider-source, working, rig, action, export, reference, and evidence collections. Unattended work must use the verified repository-owned allowlisted adapter. Do not expose unrestricted Blender Python, shell commands, arbitrary URLs, or paths outside the job and approved reference roots. A development-only Blender route is allowed only in the isolated profile and only after the parent verifies its installation and actual callable interface.

Required stages:

1. import the approved GLB or FBX and preserve provider objects
2. duplicate into the working collection
3. import named vanilla references read-only; humanoid land units must include the installed vanilla infantry reference and its entity scale, and building jobs must include the installed mesh and exact map-building entity scale
4. inspect scene and geometry
5. normalize orientation, scale, origin, and ground/water contact
6. measure and enforce the profile runtime footprint budget for static map buildings
7. perform only bounded local repairs
8. triangulate before final rig and export QA
9. convert PBR inputs to the locally verified PDX material convention
10. process textures and record DDS paths
11. create or validate the rig
12. create, retarget, clean, and bake actions
13. save checkpoints, export, and build evidence

Save stable checkpoint stages in `blender/checkpoints/` (source import, normalized, repaired, material, rigged, actions, and pre-export). Preserve source checkpoints, working checkpoints, Blender version, adapter version, checksums, and stage transitions. Never edit provider-source objects in place. Substantial missing geometry is not an automatic repair: regenerate, request explicit manual modeling scope, or block.

## Geometry, materials, rigging, and actions

Record triangles, vertices, objects, material slots, loose components, non-manifold and boundary edges, holes, degenerates, normals, UV layers and relevant overlap, transforms, negative scale, bounds, origin, ground/water contact, reference comparison, and profile semantic checks. Repair or reject holes, loose components, non-manifold edges, and degenerate geometry before acceptance; any intentional open surface must be named by the profile and marked for review. Final topology is triangular unless a verified local engine path says otherwise.

Retain provider source maps unchanged. Convert through the exact local PDX material precedent and record shader, channel mapping, color space, alpha behavior, texture dimensions, DDS paths, and unsupported maps. For the latest installed PDX packed specular route, use the recorded layout of red unused or mask zero, green specular level, blue metallic, and alpha roughness; never use a raw grayscale roughness map as the PDX specular map. Use the repository converter at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for final PNG to DDS conversion and follow that skill's complete DDS-header and alpha validation. For HOI4 model textures, enforce the profile's verified maximum dimension, currently 1024 pixels for the local vanilla model surface unless fresh installed references prove otherwise, and record any resize. If the provider diffuse is too dark, derive a documented deterministic grade from the immutable provider base and rebuild the runtime derivative from that base on every run; never compound a grade from an older processed or runtime texture. Do not pass materials QA with missing, black, magenta, invisible, accidentally transparent, or implausibly reflective surfaces.

Use one profile's calibrated axes, scale, triangle range, material/texture limits, rig route, action roles, root policy, instance density, semantic checks, export preset, and runtime pattern. A profile must be calibrated before paid or export work begins.

For map buildings, the profile's footprint budget is a hard runtime gate. The default policy is `reject`; `fit_to_budget` is allowed only when the job explicitly requests it and applies a uniform X/Y fit after height normalization. The adapter report must retain `runtime_dimensions_before_fit_m`, `runtime_dimensions_after_fit_m`, `fit_factor_xy`, `runtime_footprint_before_m`, and `runtime_footprint_after_m`.

The reusable pilot runner treats `building` and `static_building` as static routes, prepares their `Image_0`/`Image_1`/`Image_2` texture sources, and never sends them through humanoid rig or action continuation. A building job without a named installed vanilla reference is rejected before Blender preparation.

For static map-building materials, use the shader from the installed vanilla building consumer. With the current vanilla surface this is `PdxMeshAdvancedSnow`. The GFX `meshsettings.name` must equal the actual exported mesh object name, such as `Mesh_0.001`; provider labels, job slugs, and guessed names are not accepted. Verify packed PDX normal and specular channel statistics before synchronizing runtime DDS files.

For humanoids, provider rigging is a candidate only for a clear standard humanoid biped within the verified endpoint's constraints; inspect and map it in Blender. For nonhumanoids, create a custom rig with a written rig map. For mechanical assets, use rigid components and deliberate pivots: turrets, barrels, recoil, propellers, rotors, doors, wheels, and tracks must not bend from blended weights.

For winged, digitigrade, quadrupedal, multi-limbed, or otherwise nonhumanoid anatomy, the dedicated custom-rig route is mandatory. Never silently route such an asset through a humanoid armature; reject a returned humanoid armature and record the exact blocker and route status.

## Custom unit-counter companion

Every new custom unit or subunit must ship with bespoke counter art for every counter surface it uses. At minimum, a land subunit that emits the standard tokens needs its own large `unit_<subunit_id>_icon` counter strip and small `onmap_unit_<subunit_id>_icon` map counter. Air and naval units need the corresponding domain-specific map counters and inverted or state variants when the verified consumer exposes them. Derive the actual required tokens from the installed unit and `interface/subuniticons.gfx`; do not infer them only from this example.

This skill owns the custom-unit counter requirement and routes actual 2D counter production to `chaos-redux-event-assets` and `chaosx_icon_artist`. The shared `chaos-redux-event-assets` section 9.1 2D icon and counter generation contract owns ImageGen source evidence, alpha processing, native-canvas QA, contact sheets, DDS round-trip validation, and parent-review states. Do not make the 3D worker draw, trace, reconstruct, resize, recolor, or otherwise author 2D icons itself.

Before counter design, inspect the closest matching installed-vanilla definition and DDS. Record source paths, native canvas, per-frame dimensions, `noOfFrames`, frame order, alpha/background behavior, border treatment, visual scale, silhouette, exact green hues and value range, shading, contrast, and owning consumer. Also inspect the matching skill-local reference and contact sheet: `units/land/counters_large/`, `units/land/map_counters/`, `units/air/map_counters/`, or `units/naval/map_counters/`. If the installed definition, DDS, and matching reference family cannot be inspected, mark counter production `blocked`; never guess the canvas, frames, sprite contract, or style.

Route the counter brief to `chaosx_icon_artist` through `chaos-redux-event-assets` and require that worker to return the shared contract's original source PNG, saved prompt, processed alpha PNG, final DDS, native-size contact sheet, decoded round-trip evidence, manifest entry, and `gfx_handoff.md`. Preserve the sampled vanilla green palette and selected, inverted, or frame-state behavior rather than using arbitrary green. The parent owns `.gfx`, texticons, subunit definitions, localisation, and runtime wiring. A missing bespoke counter is `needs_user_review` or `blocked`; do not use a copied vanilla counter, renamed counter, generic placeholder, or other fallback for runtime promotion or completion.

The 3D worker must keep the counter source, processed evidence, and runtime copy distinct, report the selected source and hashes, and never silently synchronize an older candidate back into the runtime surface. Until the parent visually reviews the counter contact sheet, the handoff remains `needs_user_review` or `blocked`, and the worker must not claim in-game completion.

Before claiming family-wide model or sound coverage, enumerate every `common/units` subunit that resolves the custom `sprite` token. An entity-state sound package reaches only consumers that resolve that entity, so intended shared-family consumers must share the binding and deliberate exclusions must be recorded in the handoff.

Require no zero-weight deforming vertices, normalized weights, influence counts within local precedent, no unapproved opposite-side stretch, rigid assignment for rigid parts, and deformation tests in representative poses. Automatic weights are only a seed where the profile allows them.

Every requested action must have a semantic role, final name, source route, FPS, frame range, loop state, root policy, preview, exported `.anim`, proposed runtime binding, and validation result. For humanoid animation candidates, clean, retarget, and bake the action in Blender, normalize armature object and pose transforms deliberately, inspect and sanitize scale F-curves, and scale keyed location channels deliberately when the provider and calibrated mesh units differ. Define in-place or root-motion policy before editing keys, apply any location conversion exactly once, and record the factor and before/after channels. Check foot and ground contacts at representative frames and validate the required idle, move, and attack roles as real skeletal actions. Provider animations are source candidates and missing actions must be authored in Blender when the job allows it. Do not replace a requested action with a static pose. For loop actions, first/middle/last reimport screenshots are insufficient because the midpoint may intentionally return to neutral: sample at least the first, quarter, middle, three-quarter, and last phases. Retain decoded-pixel or pose/bounds comparisons that prove the quarter phases differ as intended and that the loop endpoints return appropriately, and record contact and actor-bounds checks at every sampled phase. For non-loop terminal actions, retain start/mid/end samples or other role-appropriate phases. A skeleton change invalidates weights, actions, exports, and downstream evidence.

For creature meshes parented to the armature object by the Blender adapter, measure ground-contact correction from the uncorrected pose on each frame and key it as an absolute armature-object translation; root-bone-only offsets are insufficient.
Require a grounded pass for every authored action before export.

## Custom unit sound-design companion

Every new custom unit package must define a coherent custom sound identity. Do not leave a distinctive unit silent or attach an unrelated default sound family. A vanilla sound family may be reused only when the accepted design says it genuinely matches the unit.

Selection audio is mandatory for every custom unit package. Provide at least one sourced selection one-shot, a stable runtime identifier, and an exact consumer/binding plan; do not treat idle entry, entity creation, or another animation-state event as unit selection.

Inspect the exact vanilla consumer before planning the package because land units, creatures, vehicles, aircraft, and ships do not necessarily expose the same sound roles. Include these roles:

- selection, plus order acknowledgements or unit voice when the consumer exposes them
- idle, ambient, engine, rotor, mechanical, or creature loops
- movement
- weapon discharge and attack
- impact, hit, or contact
- special actions
- death, destruction, shutdown, or disappearance

The installed HOI4 infantry voice path uses the hardcoded templates `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat`; installed `vo.asset` files realize them as entries such as `GER_infantry_idle` and `SOV_infantry_idle`. Recheck these templates and their installed vanilla definitions for every job.

For a custom infantry family owned by a dedicated country or original tag, define the exact `<TAG>_infantry_idle` selection soundeffect in the vanilla `Voices` category. Verify the actual tag or `original_tag` used by every intended country, including dynamic countries and cosmetic-tag transitions. This is country/original-tag routing, not subunit or sprite routing: enumerate every infantry division under that tag as a consumer. If custom and ordinary infantry coexist under the same tag and require distinct selection voices, mark per-subunit selection `blocked`; do not replace another unit family's voice. A new soundeffect name without the exact engine-consumed identifier is not a binding by itself.

Use the repository web-search workflow to locate candidate files on the Internet, inspect the source page and direct download terms, and save only approved candidates under the deterministic job evidence root. Prefer public-domain, Creative Commons, official archive, institutional, user-authorized, or otherwise clearly licensed sources. Reject unclear provenance, unclear recording rights, unclear modification rights, vague royalty-free claims, and sources that do not permit the intended mod use.

Download and preserve the original source file under the deterministic job evidence root. Record the source page URL, direct download URL when distinct, title, creator or performer, license, usage terms, download date, original format and duration, and SHA-256 checksum. Keep the source file immutable and link every derived file back to it.

Mechanical transformations such as trimming, fading, silence removal, normalization, channel conversion, resampling, and codec conversion are permitted only when the source license allows them. Keep the original source, transformation recipe, derived checksum, and final format in the evidence package. These operations must never become a way to create audio from scratch.

Probe every runtime WAV against the actual installed consumer precedent before the parent wires it. For a `Voices` category soundeffect, including `<TAG>_infantry_idle`, the default delivery contract is signed 16-bit PCM (`pcm_s16le`), 44.1 kHz, mono, matching the installed vanilla and approved custom voice precedents; a float WAV such as `pcm_f32le` must not be called runtime-compatible. A permitted mechanical conversion may use `ffmpeg -map 0:a:0 -ar 44100 -ac 1 -c:a pcm_s16le -map_metadata -1`, while preserving the original source and recording both hashes. Do not mark the handoff complete until every installed WAV has an `ffprobe` receipt for codec, sample rate, channels, and bit depth.

The sound handoff must define:

- the unit or subunit id and runtime consumer
- the chosen vanilla sound and voice precedents
- the mandatory selection source, soundeffect identifier, exact engine consumer, binding scope, resolved country or original tag, and every infantry consumer under that identity
- proposed sound, soundeffect, wrapper, and file identifiers
- one-shot or loop behavior
- the animation action and exact frame or phase that each sound should follow
- source mode, provenance, licence status, and forbidden substitutions
- expected final file format and runtime path based on verified local precedent
- any volume, range, variation, or randomization behavior supported by that precedent
- the Internet source URL, attribution, license, original file path, derived file path, and checksums for every sourced audio candidate
- the parent-owned files that must be wired and the validation still required

Custom vocal units should have voice direction that matches their culture, language, body, and role. Nonhuman or impossible units should use purpose-built, sourced vocalizations or mechanical sounds instead of ordinary soldier acknowledgements. Do not manufacture final audio from test tones, primitive oscillators, placeholder beeps, or unrelated stock effects.

The model worker does not claim the sound package complete merely because synchronization points and identifiers are documented. It must provide sourced audio candidates and licensing evidence or mark the role blocked. Selection acceptance requires evidence from the actual selection consumer and cannot be inferred from idle or another entity state. Sound definitions, entity or unit wiring, and in-game playback validation remain parent-owned unless the task explicitly grants that production scope.

## PDX export and reimport evidence

Before export, ensure the export collection contains only approved objects and that transforms, topology, materials, armature, actions, exporter version, and preset pass. Export `.mesh` and required `.anim` files using the checksum-locked verified `io_pdx_mesh` route. Capture every warning, output path, byte size, and checksum.

Treat the requested triangle target as a hard ceiling. If a dense source needs several bounded decimation passes, keep reducing through the allowlisted operation until the reported final count is at or below the target; fail on a stalled pass or any over-target result instead of accepting a one-pass floor.

For a static building, the final working checkpoint must pass the allowlisted static transform-bake gate before export: bake location, rotation, and scale into mesh data without changing world bounds, ground contact, UVs, materials, normals, or object name, then require exact identity object transforms. Reject armatures/actions, protected or shared source data, non-finite or negative transforms, bounds drift, and any retained non-identity transform; do not compensate through entity scale.

When an accepted static-building silhouette would exceed the PDX per-stream vertex/index envelope after UV and normal seam splitting, do not destroy the shape through aggressive decimation. After transform baking, use the allowlisted static material-batch partition operation to keep the same object, geometry, UVs, normals, textures, bounds, and transforms while emitting several bounded PDX mesh streams. Default to a conservative worst-case 24,000 vertices per batch unless fresh installed-vanilla calibration proves another limit, parse the actual text export, and fail if any individual stream exceeds either 65,535 vertices or 65,535 triangle indices. Texture-identical batch slots are render streams rather than distinct logical materials, but every exported stream index must have a matching `meshsettings` block in the active `.gfx`; an index-0-only registration is invalid even when the locked importer can rejoin and render every stream.

For every output, retain the export log and reimport or parse the actual `.mesh` or `.anim` bytes through the locked stack, saving the proof scene or parser report, measured geometry/action facts, output checksum, and any warnings. If the verified stack cannot re-import or parse that format, record an explicit `required installation/verification` or `blocked` result. A Blender viewport, provider preview, file existence, or plausible filename is not reimport evidence. Do not silently ignore exporter warnings, missing actions, unsupported material channels, or an absent parser.

For static map buildings, also audit the runtime consumer after reimport: the `.gfx` scale and shader, meshsettings object name, runtime mesh and DDS paths, building definition, and spawn policy must agree. A custom map building must not use vanilla `special_project_facility_spawn`. Use a dedicated `type = province` spawn pool for a direct map consumer, and define the matching `building_<spawn_point>` entity in the active `.asset` file. Different meshes must never share one spawn point because HOI4 resolves one map entity per spawn point. When every gameplay building level must appear, wire the gameplay building directly and provide one explicit spawn position per possible rendered level. Use a hidden provincial anchor only for an intentional single visual independent of gameplay level, place it with state-scoped `set_building_level`, and explicitly clean it up on conversion, dismantlement, annexation, or deletion. Leave automatic nudging enabled unless complete `map/buildings.txt` coverage is maintained; if nudging fails, preserve every vanilla row in a deterministic generated override and add complete custom coverage.

## Evidence package and handoff

The job package must contain, as applicable:

- job intake and append-only history
- source reference, preflight, provenance, license, and checksums
- provider requests, responses, task IDs, versions, balance, credits, and downloads
- source and checkpoint `.blend` files
- geometry, material, rig, weight, action, and export reports
- source and final textures, animation previews, `.mesh`, and `.anim`
- immutable Internet-sourced unit audio candidates, licensing records, derived files, transformations, and checksums
- export/reimport evidence, manifest, and requirement-to-runtime crosswalk
- a runtime handoff with proposed stable names, paths, material/shader mapping, action mapping, and the exact files/identifiers the parent must wire
- for every custom unit, a sound-design handoff with sourced audio files, source URLs, attribution, licensing evidence, sound roles, voice direction where applicable, vanilla precedents, animation synchronization points, proposed runtime identifiers, and remaining parent-owned wiring
- for every custom unit, a counter handoff with inspected installed-vanilla definitions and DDS files, matching skill-local counter family, exact consumers and tokens, required frames/states/sizes, original counter-art paths, final DDS paths, sampled vanilla green evidence, comparison evidence, proposed sprite definitions, and remaining parent-owned wiring
- for static buildings, footprint/scale evidence, meshsettings object-name evidence, dedicated spawn or provincial-anchor evidence, and runtime-consumer evidence

Each model manifest entry records the asset ID/slug, profile, source reference and checksum, provider lineage, selected candidate, checkpoint, geometry counts, objects/materials, armature/bones, actions/frame data, custom-unit sound requirements and synchronization points, custom-unit counter consumers, installed-vanilla counter references, sampled green evidence, bespoke counter handoff and status, source/final textures, exports/checksums, exporter version/settings, proposed runtime identifiers, actual runtime registration only after parent wiring, live consumer, in-game evidence only after parent validation, and status. Use `complete`, `needs_user_review`, `blocked`, or `canceled`; never create a fallback completion state.

For nonhumanoid/creature jobs, `manifest.md` and `runtime/handoff.md` must repeat the measured numeric scale crosswalk, dedicated rig route, `scale_crosswalk_status`, `rig_route_status`, provider/export route status, and the exact blocker text for every unavailable or pending route; a bare `blocked` or `pending` label is insufficient.

When the event/system owner and slug are known, place the subagent handoff under the parent-provided `docs/plans/<owner_id>_<owner_slug>_plans/subagent_handoffs/` path. The parent must review every artifact and either wire it, queue it with a reason, reject it with a reason, or carry its blocker forward.

## Runtime copy synchronization

Treat the selected source exports, staged runtime copies, and active consumer files as separate surfaces. A runtime file can be stale or be overwritten by an older mapped texture even when the current source export is correct. Select the final geometry, material maps, and actions first, then lock the selected source paths in the manifest before synchronizing any runtime copy. Record each source and destination path, source and destination SHA-256, copy tool or actor, copy time, and provenance link, then compare destination hashes after synchronization. Never synchronize from an older provider or processed path, never let a filename alone choose the source, and never synchronize before final source selection. The parent owns active runtime copies, `.asset`, entity, `.gfx`, gameplay wiring, live consumers, and in-game screenshots; the worker owns the evidence and exact handoff needed to perform that work.

## Bounded subagent route

Use `chaosx_3d_model_pipeline` only when the parent provides the exact job root, reference path or asset brief, output folders, handoff path, profile, named vanilla references, scale relationship, required actions, custom-unit sound roles and Internet-source requirements, custom-unit counter consumers and tokens, inspected vanilla counter definition/DDS paths, matching skill-local counter family, counter-artist handoff path, synchronization requirements where applicable, source permissions, baseline planned paid operations, extra-recovery credit and attempt limits, dependency lock, and forbidden simplifications. The prompt must require Meshy 7 exclusively and state that ordinary planned paid operations need no confirmation while failure-driven extra paid recovery does. Spawn it with `fork_context=false`; put every needed conversation constraint into the prompt or named repository files.

The subagent may produce source models, Blender files, textures, `.mesh`, `.anim`, sourced unit-audio candidates, mechanically derived audio, previews, manifests, reports, crosswalk rows, and handoffs. It must not perform final gameplay/GFX/entity/sound-definition/localisation/spreadsheet wiring or claim in-game completion. The parent owns those changes, the live consumer, in-game evidence, and the overall completion claim.

## Final state and fallback disclosure

Mark each requested 3D requirement as `complete`, `needs_user_review`, `blocked`, or `canceled` in the package. For a custom unit, the package must also record the sourced sound candidates, licensing evidence, synchronization handoff, bespoke counter package, installed-vanilla counter inspection evidence, and parent-owned audio/counter wiring status. A package-level `complete` means the worker's requested source, processing, export, sound-source research, counter handoff, and evidence outputs are present; it does not mean the Chaos Redux runtime feature is complete. Report every omitted component, rejected candidate, unverified capability, budget stop, missing reimport proof, missing sound source, missing counter, and proposed static companion explicitly. Never hide a simplification behind a successful export or a parent-owned runtime handoff.

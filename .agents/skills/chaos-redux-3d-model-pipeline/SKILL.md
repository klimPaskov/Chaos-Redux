---
name: chaos-redux-3d-model-pipeline
description: Use when creating, rigging, animating, converting, exporting, auditing, or documenting a custom Hearts of Iron IV 3D model for a Chaos Redux unit, building, vehicle, aircraft, ship, creature, or articulated asset.
---

# Chaos Redux 3D Model Pipeline

Use this skill for final 3D geometry and skeletal animation assets. It covers the bounded path from one approved reference image through provider generation, Blender normalization, PDX materials, rigs, actions, Paradox export, QA evidence, and a parent-owned runtime handoff.

Do not use it for 2D equipment illustrations, map counters, focus or idea icons, 2D frame-sheet animation, leader portraits, or concept-only requests. Those remain with `chaos-redux-event-assets` and `chaos-redux-frame-animation` where applicable.

## Ownership and completion boundary

A provider result is a source candidate, a `.blend` is a working artifact, and a `.mesh` or `.anim` is a runtime candidate. The package is not complete merely because a provider task, Blender preview, or export succeeded. Completion requires the exact runtime registration, a live consumer, and in-game evidence owned by the parent implementation agent.

The 3D worker may create source files, Blender checkpoints, textures, `.mesh`, `.anim`, previews, manifests, reports, and handoffs. It must not edit gameplay, localisation, `.gfx`, `.gui`, `.asset`, entity, event, focus, decision, country, history, AI, on-action, or spreadsheet files unless the parent grants a narrow exception explicitly. The parent owns runtime identifiers, source wiring, live consumer validation, and the overall completion claim.

`chaos-redux-event-assets` remains the owner of broad asset inventories, source provenance conventions, texture/DDS conventions, and requirement-to-runtime coverage across asset types. Keep model geometry, model materials, entity wiring, and any separate 2D concept reference distinct. `chaos-redux-frame-animation` governs 2D frame-sheet animation; it does not replace skeletal 3D `.anim` production.

## Hard start gates

Before any workflow action, verify that `MESHY_API_KEY` exists and is non-blank, and verify that the selected Meshy route is reachable. If the key is missing, stop immediately and tell the user to set it, then restart the shell or Codex:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

Do not generate a reference image, discover paths, make a provider call, or begin downstream work before this gate passes.

Treat the intended official Meshy MCP integration through a version-pinned wrapper, the official Blender Lab MCP development route, the repository-owned allowlisted Blender adapter, the Blender version, and the checksum-locked `io_pdx_mesh` extension as dependencies that require installation and verification. These are capability labels, not callable tool names. This skill does not assume they are installed or callable. If any required capability is missing, its live schema is unavailable, or its lock does not match, stop and report `required installation/verification` or `blocked`; do not install packages, substitute an unapproved route, or invent a live MCP/tool name. Record the actual discovered server/tool identifiers and arguments only after live verification.

Keep provider and Blender integration guidance in this skill and the job's dependency lock. Do not create a central MCP router or tool-specific wrapper. Any viewer, inspector, renderer, or comparison route used for QA must be read-only. This package does not provide unrelated viewers, including a Technology Tree Viewer; record such a capability as absent when requested.

There is no silent fallback or simplification. Discuss every fallback with the parent/user before use and record the decision. If approval is not explicit, mark the item `blocked` or `needs_user_review`. A static animation fallback is an explicit companion artifact for review or unavailable motion, never a replacement for a requested skeletal action.

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

Use existing Chaos Redux paths under `gfx/models/` and `gfx/entities/` as local precedents where applicable, but confirm the final path, shader, material channels, scale, axes, skeleton, action names, and entity structure against the installed vanilla version. Do not lock tutorial values or assume that a nearby asset belongs to the same runtime surface.

For a humanoid land-unit pilot, this is a hard calibration gate, not a suggestion: import the installed vanilla infantry `.mesh` into the Blender reference collection read-only, identify the exact entity and runtime `scale`, exclude collision-only geometry, and record the measured source-mesh height, effective runtime height, forward axis, ground contact, and the comparison result in the job and manifest. When the custom entity retains the vanilla entity scale, normalize the exported mesh to the measured source-mesh height so the engine applies that scale exactly once; do not normalize to the effective runtime height and then multiply it by the entity scale again. Do not use a generic real-world height or an arbitrary entity `scale` as a substitute. Keep the provider/animation height and the Blender source-mesh calibration height as separate fields when the provider and HOI4 coordinate spaces differ.

## Job intake and deterministic layout

Validate the job before any paid work. The parent must provide:

- event or system owner, stable asset ID, and lowercase asset slug
- one ready reference image path and checksum, or enough brief input to generate it
- source provenance, license status, or explicit user-provided authorization
- one asset profile: `static_prop`, `building`, `humanoid_unit`, `nonhumanoid_creature`, `vehicle_land`, `aircraft`, `naval`, or `articulated_attachment`
- geometry intent, required components, forbidden additions, texture direction, and unseen-side/rear-geometry policy
- named vanilla reference paths and the expected scale relationship
- required action roles, runtime consumer, credit hard/soft limits, and paid-attempt limit
- the locked provider, Blender, adapter, and `io_pdx_mesh` dependencies
- the deterministic job root and exact handoff path

When the parent does not supply a root, derive it from the repository root and stable owner/asset slugs:

```text
docs/assets/<owner_id>_<owner_slug>/models_3d/<asset_slug>/
  job.json
  history.jsonl
  reference/
    source.png
    derived/                 # optional, approved clarification only
    meshy_input.png          # the only image sent to Meshy
  provider/
    requests/
    downloads/
  blender/
    source/
    working/
    checkpoints/
  textures/
    source/
    processed/
  export/
  previews/
  reports/
  runtime/
    handoff.md
```

Use the same derived path every time. Do not put timestamps, random IDs, pilot names, or workstation paths into the primary layout. Keep append-only task history, checksums, and dependency records inside the job root; never archive secrets. Final runtime files must not remain runtime-referenced from `docs/assets/`.

## Exactly one Meshy reference image

Meshy receives exactly one clean final reference image. If the parent supplies one, preserve it and use it only after checksum and rights preflight. If no image is supplied, generate one production reference through the approved image-generation route, save it as `reference/meshy_input.png`, and retain its prompt, source mode, checksum, and approval note. If that route is unavailable, mark the job as `required installation/verification` or `blocked` rather than substituting.

Do not create or submit a turnaround sheet, multi-view board, collage, side-profile set, or separate front/rear images. Vanilla references may be imported into Blender read-only for calibration, but they are not additional Meshy inputs.

Preflight the one input for silhouette, cropped parts, limb/component separation, dark gaps, strong shadows, background complexity, thin structures, painted details that may be mistaken for geometry, symmetry/asymmetry, unseen-side ambiguity, and source rights. An approved derived image may clarify exposure, background, or an accidental seam; it may not silently redesign the subject. Keep the original and both checksums.

## Provider generation and lineage

The normal provider sequence is:

```text
verified balance -> image-to-3D -> status -> immediate download
                 -> optional remesh/retexture
                 -> optional suitable humanoid rig/animation candidate
```

Before every paid tranche, check the live balance through the verified provider route and record the estimate, hard limit, attempt number, and consumed credits. Inspect the live schema before paid calls; do not promise a general geometry prompt when the current Image-to-3D surface exposes only texture-direction text. Record the exact verified arguments and response/task IDs without exposing the API key.

Prefer smart topology when suitable, triangular output, PBR maps when textures are required, removal of baked lighting when supported, and A/T pose for a riggable humanoid. Use the suitable provider pose or `none` for static or mechanical assets. Download every successful artifact immediately, retain the GLB as the canonical provider archive, retain FBX when a rig/action route needs it, and record checksums, provider version, task IDs, request/response lineage, and local download paths. Remote URLs are never the only accepted copy.

Treat every provider result as a candidate. Review front, rear, sides, top, and underside where relevant, plus wireframe, untextured shading, and textured views. Block or retry within the approved budget for missing major components, floating critical parts, fused limbs/weapons/turrets/wings, open holes, identity mismatch, broken thin structures, or unacceptable unseen-side invention. Do not spend retexture, rig, or animation credits on rejected geometry. High-detail generation followed by controlled reduction is allowed only when the job explicitly permits it and the lineage records both candidates.

Tutorial values near 10,000 vertices and the 25,000–30,000 caution band are seed heuristics only. Local vanilla calibration and measured runtime evidence decide the profile target.

## Blender processing and checkpoints

Use a versioned scene template with protected provider-source, working, rig, action, export, reference, and evidence collections. Unattended work must use the verified repository-owned allowlisted adapter. Do not expose unrestricted Blender Python, shell commands, arbitrary URLs, or paths outside the job and approved reference roots. A development-only Blender route is allowed only in the isolated profile and only after the parent verifies its installation and actual callable interface.

Required stages:

1. import the approved GLB or FBX and preserve provider objects
2. duplicate into the working collection
3. import named vanilla references read-only; humanoid land units must include the installed vanilla infantry reference and its entity scale
4. inspect scene and geometry
5. normalize orientation, scale, origin, and ground/water contact
6. perform only bounded local repairs
7. triangulate before final rig and export QA
8. convert PBR inputs to the locally verified PDX material convention
9. process textures and record DDS paths
10. create or validate the rig
11. create, retarget, clean, and bake actions
12. save checkpoints, export, and build evidence

Save stable checkpoint stages in `blender/checkpoints/` (source import, normalized, repaired, material, rigged, actions, and pre-export). Preserve source checkpoints, working checkpoints, Blender version, adapter version, checksums, and stage transitions. Never edit provider-source objects in place. Substantial missing geometry is not an automatic repair: regenerate, request explicit manual modeling scope, or block.

## Geometry, materials, rigging, and actions

Record triangles, vertices, objects, material slots, loose components, non-manifold and boundary edges, degenerates, normals, UV layers and relevant overlap, transforms, negative scale, bounds, origin, ground/water contact, reference comparison, and profile semantic checks. Final topology is triangular unless a verified local engine path says otherwise.

Retain provider source maps. Convert through the exact local PDX material precedent and record channel mapping, color space, alpha behavior, texture dimensions, DDS paths, and unsupported maps. Use the repository converter at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` for final PNG to DDS conversion and follow that skill's complete DDS-header and alpha validation. For HOI4 model textures, enforce the profile's verified maximum dimension (1024 pixels for the current vanilla model surface) and record any resize. Do not pass materials QA with missing, black, magenta, invisible, accidentally transparent, or implausibly reflective surfaces.

Use one profile's calibrated axes, scale, triangle range, material/texture limits, rig route, action roles, root policy, instance density, semantic checks, export preset, and runtime pattern. A profile must be calibrated before paid or export work begins.

For humanoids, provider rigging is a candidate only for a clear standard humanoid biped within the verified endpoint's constraints; inspect and map it in Blender. For nonhumanoids, create a custom rig with a written rig map. For mechanical assets, use rigid components and deliberate pivots: turrets, barrels, recoil, propellers, rotors, doors, wheels, and tracks must not bend from blended weights.

If a custom `common/units` subunit identifier is introduced, the parent runtime handoff must register its generated `unit_<subunit_id>_icon_small` texticon (and any other emitted icon token) against a verified vanilla sprite. A missing custom texticon is a runtime failure even when the `.mesh` loads.

Require no zero-weight deforming vertices, normalized weights, influence counts within local precedent, no unapproved opposite-side stretch, rigid assignment for rigid parts, and deformation tests in representative poses. Automatic weights are only a seed where the profile allows them.

Every requested action must have a semantic role, final name, source route, FPS, frame range, loop state, root policy, preview, exported `.anim`, proposed runtime binding, and validation result. Provider animations are source candidates: clean, retarget, bake, and validate them in Blender. Author missing creature or mechanism actions in Blender when the job allows it. Do not replace a requested action with a static pose. For loops, compare first and last evaluated poses, root/contact drift, and the result at normal HOI4 map zoom. A skeleton change invalidates weights, actions, exports, and downstream evidence.

## PDX export and reimport evidence

Before export, ensure the export collection contains only approved objects and that transforms, topology, materials, armature, actions, exporter version, and preset pass. Export `.mesh` and required `.anim` files using the checksum-locked verified `io_pdx_mesh` route. Capture every warning, output path, byte size, and checksum.

For every output, retain the export log and either a successful re-import/parse report or an explicit `required installation/verification`/`blocked` record when the verified stack cannot re-import or parse that format. A Blender viewport, provider preview, file existence, or plausible filename is not reimport evidence. Do not silently ignore exporter warnings, missing actions, unsupported material channels, or an absent parser.

## Evidence package and handoff

The job package must contain, as applicable:

- job intake and append-only history
- source reference, preflight, provenance, license, and checksums
- provider requests, responses, task IDs, versions, balance, credits, and downloads
- source and checkpoint `.blend` files
- geometry, material, rig, weight, action, and export reports
- source and final textures, animation previews, `.mesh`, and `.anim`
- export/reimport evidence, manifest, and requirement-to-runtime crosswalk
- a runtime handoff with proposed stable names, paths, material/shader mapping, action mapping, and the exact files/identifiers the parent must wire

Each model manifest entry records the asset ID/slug, profile, source reference and checksum, provider lineage, selected candidate, checkpoint, geometry counts, objects/materials, armature/bones, actions/frame data, source/final textures, exports/checksums, exporter version/settings, proposed runtime identifiers, actual runtime registration only after parent wiring, live consumer, in-game evidence only after parent validation, and status. Use `complete`, `needs_user_review`, `blocked`, or `canceled`; never create a fallback completion state.

When the event/system owner and slug are known, place the subagent handoff under the parent-provided `docs/plans/<owner_id>_<owner_slug>_plans/subagent_handoffs/` path. The parent must review every artifact and either wire it, queue it with a reason, reject it with a reason, or carry its blocker forward.

## Bounded subagent route

Use `chaosx_3d_model_pipeline` only when the parent provides the exact job root, reference path or asset brief, output folders, handoff path, profile, named vanilla references, scale relationship, required actions, source permissions, credit and attempt limits, dependency lock, and forbidden simplifications. Spawn it with `fork_context=false`; put every needed conversation constraint into the prompt or named repository files.

The subagent may produce source models, Blender files, textures, `.mesh`, `.anim`, previews, manifests, reports, crosswalk rows, and handoffs. It must not perform final gameplay/GFX/entity/localisation/spreadsheet wiring or claim in-game completion. The parent owns those changes, the live consumer, in-game evidence, and the overall completion claim.

## Final state and fallback disclosure

Mark each requested 3D requirement as `complete`, `needs_user_review`, `blocked`, or `canceled` in the package. A package-level `complete` means the worker's requested source, processing, export, and evidence outputs are present; it does not mean the Chaos Redux runtime feature is complete. Report every omitted component, rejected candidate, unverified capability, budget stop, missing reimport proof, and proposed static companion explicitly. Never hide a simplification behind a successful export or a parent-owned runtime handoff.

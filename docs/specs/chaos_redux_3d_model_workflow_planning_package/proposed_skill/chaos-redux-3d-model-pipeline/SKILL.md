---
name: chaos-redux-3d-model-pipeline
description: Use when creating, rigging, animating, converting, exporting, auditing, or documenting a custom Hearts of Iron IV 3D model for a Chaos Redux unit, building, vehicle, aircraft, ship, creature, or articulated asset.
---

# Chaos Redux 3D Model Pipeline

Use this skill for final 3D geometry and skeletal animation assets.

This skill owns the workflow from one approved reference image through Meshy generation, Blender normalization, PDX materials, rigs, actions, Paradox export, QA evidence, and runtime handoff.

It does not treat 2D equipment illustrations, map counters, focus icons, or concept art as final 3D models. Those remain with `chaos-redux-event-assets` and its normal asset routes.

## Core rule

A Meshy result is a source candidate. A Blender file is a working artifact. A `.mesh` or `.anim` export is a runtime candidate. The asset is complete only after exact runtime registration, a live consumer, and in-game evidence exist.

No silent fallback or simplification is allowed.

## Hard gate: Meshy API availability

Before the workflow does anything else, verify that `MESHY_API_KEY` exists as an environment variable and that the Meshy route is reachable. If the key is missing or blank, stop immediately and tell the user to run this PowerShell command, then restart the shell or Codex:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

Do not continue with reference-image generation, path discovery, Meshy calls, or downstream work until the key exists. A successful key check is the start gate for this skill.

## Required reading

Before 3D work:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md` when a subagent is used
- the parent brief, spec, plan, manifest, or handoff
- the offline Paradox wiki graphical asset and relevant interface, entity, character, or model pages required by the target surface
- relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`
- local vanilla `.mesh`, `.anim`, `.asset`, entity, material, texture, and model precedents for the exact domain
- existing Chaos Redux model precedents
- the locked Meshy, Blender MCP, Blender, and `io_pdx_mesh` dependency records

Do not rely on tutorial numbers or memory when local files can answer scale, axes, action names, material channels, skeletons, or paths.

## Autonomous start behavior

This workflow is autonomous by default. If the parent does not provide a ready Meshy reference image, the workflow must generate one single production reference image itself from the asset brief through the approved image-generation route, save it under the resolved job root, and use that file as the only Meshy input. Do not generate a multi-view board, turnaround sheet, or separate side-profile images for Meshy.

The workflow should also resolve or create its own deterministic paths from the repository structure, owner, asset slug, and runtime target. The user does not need to pre-create the reference-image path or every working directory.

## When to use

Use for:

- humanoid land units
- nonhuman and supernatural units
- animals and creatures
- tanks, trucks, walkers, artillery vehicles, and trains
- aircraft and rotorcraft
- ships and submarines
- map buildings and static props
- animated turrets, barrels, doors, wings, rotors, claws, jaws, tails, and other mechanisms
- PDX mesh and animation export
- 3D QA, manifests, previews, and runtime handoffs

Do not use for:

- 2D unit counters or equipment art
- focus, idea, decision, technology, or achievement icons
- 2D frame-sheet animation
- leader portraits
- unimplemented concept-only model requests unless the user asked only for a design brief

## Tool architecture

### Meshy

Use the official Meshy MCP server through a version-pinned wrapper. Store the API key only in an environment variable or secret store.

The normal tool route is:

```text
balance -> image-to-3D -> status -> immediate download
        -> optional remesh or retexture
        -> optional humanoid rig
        -> optional provider animation candidates
```

Inspect the live MCP tool schema before paid calls. Record the server version and exact arguments.

### Blender

The official Blender Lab MCP server may be used in an isolated development profile. It is privileged because it can execute Blender Python operations.

Unattended production work must use the repository-owned `blender_hoi4` allowlisted adapter. Do not expose unrestricted Python, shell commands, arbitrary URLs, or unrestricted file paths to the production agent.

### Paradox export

Use a version and checksum-locked `io_pdx_mesh` extension. Verify both mesh and animation export for the selected Blender version before the first asset job.

## Required job intake

Every job must provide:

- event or system owner
- stable asset ID and slug
- either one ready reference image path and checksum, or enough asset-brief input for the workflow to generate the final Meshy reference image autonomously
- source provenance and license status
- asset profile
- geometry intent
- required components
- forbidden additions
- texture direction
- rear-side or unseen-geometry policy
- target vanilla reference paths
- expected scale relationship
- required action roles
- runtime consumer
- credit soft and hard limits
- paid-attempt limits
- dependency lock
- job root and handoff path

Validate the job before paid work.

## Reference preflight

Single-image reconstruction depends heavily on the input.

Check the final single Meshy input image, whether user-supplied or workflow-generated:

- complete silhouette
- cropped parts
- limb and component separation
- dark gaps that may become holes
- strong shadows
- native transparency and preserved alpha for a workflow-generated reference
- background complexity for an inherited, sourced, or user-provided opaque reference
- thin structures
- painted detail that may be mistaken for geometry
- symmetry and intended asymmetry
- unseen-side ambiguity
- source rights

Preserve the original. Request a real transparent background in the initial ImageGen call for every workflow-generated reference and preserve its alpha. Background removal is fallback-only when native transparency fails or an inherited, sourced, or user-provided reference has an unwanted opaque backdrop. An approved derived image may clarify exposure, perform that documented fallback, or fix an accidental dark seam, but it may not silently redesign the subject.

## Meshy generation rules

- prefer the current smart-topology route when appropriate
- request triangular topology
- use the calibrated profile target, not one universal count
- enable PBR maps when textures are required
- remove baked lighting when supported and appropriate
- use an A or T pose for riggable humanoids when supported
- use `none` or the suitable provider pose for static or mechanical assets
- download GLB as the canonical provider archive and FBX when rigs or actions require it
- download every successful output immediately
- record task IDs and consumed credits

The current Image-to-3D surface may expose text direction for textures without exposing a general geometry prompt. Do not promise unsupported prompt control. Keep geometry instructions as review and Blender requirements when the provider cannot consume them.

## Candidate review

Inspect front, rear, sides, top, underside where relevant, wireframe, untextured shading, and textured views.

Block or retry for:

- missing major components
- floating critical parts
- fused limbs, weapons, turrets, or wings
- large open holes
- identity mismatch
- broken thin structures
- unacceptable unseen-side invention

Use a high-detail source and controlled reduction when a low-count generation loses required geometry. Tutorial values around 10,000 vertices and the 25,000 to 30,000 caution band are only seed heuristics. Local vanilla calibration and runtime performance are authoritative.

## Asset profiles

Use one profile:

- `static_prop`
- `building`
- `humanoid_unit`
- `nonhumanoid_creature`
- `vehicle_land`
- `aircraft`
- `naval`
- `articulated_attachment`

Each profile defines axes, scale reference, triangle ranges, material and texture limits, rig route, action roles, root policy, instance density, semantic checks, export preset, and runtime consumer pattern.

Do not start paid or export work with uncalibrated null profile values.

## Blender processing

Use a versioned scene template with protected provider-source, working, rig, action, export, reference, and evidence collections.

Required stages:

1. import GLB or FBX
2. preserve source objects
3. duplicate into working collection
4. import approved vanilla reference read-only
5. inspect scene and geometry
6. normalize orientation, scale, origin, and ground or water contact
7. perform only bounded local repairs
8. triangulate before final rig and export QA
9. convert PBR inputs to the locally verified PDX material convention
10. process and convert final textures
11. create or validate rig
12. create, retarget, or clean actions
13. save stage checkpoints
14. export mesh and actions
15. build runtime handoff and evidence

Substantial missing geometry is not an automatic Blender repair. Regenerate, request manual modeling scope, or block.

## Geometry QA

Record:

- triangles and vertices
- objects and material slots
- loose components
- non-manifold and boundary edges
- degenerates
- normals
- UV layers and relevant overlap
- transforms and negative scale
- bounds, origin, and ground or water contact
- profile semantic checks

Final topology is triangular unless a locally verified engine path says otherwise.

## Materials

Retain provider source maps. Convert through the exact local PDX material precedent. Record channel mapping, color space, alpha behavior, texture dimensions, DDS paths, and unsupported maps.

Do not pass materials QA with missing, black, magenta, invisible, accidentally transparent, or implausibly reflective surfaces.

## Rig route

### Humanoid

Meshy rigging may be used as a candidate only for a clear standard humanoid biped within the live endpoint's constraints. Inspect and map it in Blender. Retarget or rebuild when the provider hierarchy does not match the runtime precedent.

### Nonhumanoid

Create a custom Blender rig. Write a rig map first. Use a root, body segments, limb chains, and disconnected IK controls where needed. Chain length follows the actual limb, not a fixed tutorial value.

### Mechanical

Use rigid components and deliberate pivots. Turret, barrel, recoil, propeller, rotor, door, and wheel or track structures must not bend from blended weights.

## Weight rules

- no zero-weight deforming vertices
- normalized weights
- influence count within local precedent
- no opposite-side stretch without a physical reason
- rigid parts use rigid assignment
- joints pass deformation test poses
- automatic weights are a seed only when allowed by the profile

Parent with empty groups and assign deliberately when automatic weights create cross-body errors.

## Animation rules

Every required action has a semantic role, final name, source route, FPS, frame range, loop state, root policy, preview, exported `.anim`, runtime binding, and in-game result.

Provider animations are source candidates. Clean, retarget, bake, and validate them in Blender.

Author animations in Blender when the provider lacks a suitable action, especially for creatures, mechanisms, recoil, and special attacks.

A requested action cannot be replaced by a static pose.

For looped actions, compare the first and last evaluated pose, inspect root and contact drift, and review at normal HOI4 map zoom.

Changing the skeleton after action approval invalidates weights, actions, exports, and runtime evidence.

## Export

Before export:

- export collection contains only approved objects
- transforms and scale pass
- topology and materials pass
- armature and action pass when required
- exporter version and preset are recorded
- output is versioned or empty

Export `.mesh` and one or more `.anim` files according to the exact local precedent. Capture every warning and output checksum.

Re-import or parse the export when supported. In-game validation remains mandatory.

## Required output package

```text
job and history
reference and preflight
provider requests, responses, tasks, credits, and local downloads
source and checkpoint `.blend` files
geometry, material, rig, weight, and action reports
source and final textures
animation previews
final `.mesh` and `.anim`
export log
manifest
runtime handoff
requirement-to-runtime crosswalk
in-game validation evidence
```

## Subagent routing

Use `chaosx_3d_model_pipeline` for bounded asset production when the parent supplies exact paths, profile, reference, budgets, actions, dependency lock, and handoff location.

All project subagents use `fork_context=false`. Put every needed conversation constraint into the prompt or named files.

The subagent may create source files, Blender files, textures, `.mesh`, `.anim`, previews, manifests, reports, and handoffs. It does not edit gameplay, localisation, `.gfx`, `.gui`, `.asset`, entity, event, focus, decision, country, or spreadsheet files unless the parent explicitly grants a narrow exception.

## Completion

Use these final states:

- `complete`
- `needs_user_review`
- `blocked`
- `canceled`

There is no fallback completion state.

The main agent owns final runtime source wiring, in-game validation, and the completion claim.

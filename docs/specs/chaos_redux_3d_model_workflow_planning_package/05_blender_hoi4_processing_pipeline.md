# Blender HOI4 Processing Pipeline

## Blender is the normalization authority

All provider outputs enter Blender as source candidates. Blender owns the final decisions for:

- orientation
- scale
- origin and pivot
- transforms
- topology
- object separation
- UV and material conversion
- armature
- vertex groups and weights
- action names and frame ranges
- PDX export

## Scene template

A versioned job template should contain:

```text
CR_JOB_ROOT
  00_reference
  10_provider_source
  20_working_mesh
  30_rig
  40_actions
  50_export
  90_evidence
```

Rules:

- provider files import into `10_provider_source`
- provider source objects are locked and never edited
- working duplicates live in `20_working_mesh`
- vanilla scale references live in `00_reference`
- only approved export objects enter `50_export`
- cameras, lights, and evidence objects stay outside export collections

## Import

Preferred import order:

1. GLB for canonical geometry and PBR inspection
2. FBX for provider rig and animation interchange
3. OBJ only as a diagnostic fallback when approved

Record:

- source format
- importer version
- import settings
- object count
- material count
- armature count
- animation count
- original transforms

Do not silently merge all objects on import. Object boundaries can carry meaningful components.

## Orientation and facing

The workflow must inspect a local vanilla precedent for the target domain. The profile records:

- forward axis
- up axis
- object local rotation
- armature local rotation
- mesh origin
- ground plane
- expected entity facing in game

The tutorial's manual 90-degree correction becomes a measured transform in the profile. It is not applied blindly to every asset.

## Scale normalization

Scale is calibrated against one or more imported vanilla models from the same runtime surface.

Examples:

- infantry against a vanilla infantry unit
- tank against a same-class vanilla tank
- aircraft against a comparable air model
- ship against a comparable hull class
- building against the same map-building family

Procedure:

1. import the approved vanilla reference read-only
2. align ground planes and forward axes
3. measure bounding boxes
4. apply the profile's intended relative size
5. apply object scale
6. verify armature and mesh transforms
7. save the scale ratio in the report

Entity-level scale may remain available for small tuning, but it is not a substitute for a normalized source asset.

### Humanoid land-unit hard gate

For a humanoid land-unit pilot, import the installed vanilla infantry mesh into the Blender reference collection read-only before normalizing the candidate. Record the exact `.mesh` path, entity definition, entity `scale`, collision-object exclusion, forward axis, ground contact, source-space height, effective runtime height, and the final comparison in the job, manifest, and scale report. Provider height and Blender runtime-calibration height are separate values when the provider coordinate system differs from HOI4's unit coordinate system. A generic human height is not sufficient.

The current pilot reference is `gfx/models/units/western_european_infantry.mesh` against `gfx/entities/units_infantry.asset#infantry_rifle_entity`: the main imported mesh measures `7.351824` source units and the vanilla entity uses `scale = 0.8`, producing an effective runtime height of `5.881459` units. The custom mesh target is therefore `7.351824` source units when it retains `scale = 0.8`; applying the entity scale to a mesh already normalized to `5.881459` would make it 20 percent too short. This is a measured precedent, not a universal constant for other runtime surfaces.

## Geometry audit

Automated report fields:

- object count
- triangle and vertex counts per object and total
- loose parts
- connected components
- non-manifold edges
- boundary edges
- zero-area faces
- zero-length edges
- duplicate vertices within tolerance
- intersecting components where detectable
- inverted normals
- UV layer count
- UV overlap ratio where appropriate
- material slot count
- unapplied transforms
- negative scale
- bounding box and ground penetration

Profile-specific checks add wheel count, wing symmetry, turret separation, bone influence, and other semantic requirements.

## Repair scope

The adapter may perform only selected local repairs automatically:

- recalculate normals
- merge duplicate vertices within a small recorded tolerance
- triangulate
- remove isolated zero-area geometry
- fill explicitly approved small holes
- separate loose components
- join approved components
- apply transforms
- move origin or pivot to an approved location
- limited decimation or remesh with before-and-after comparison

It may not automatically:

- sculpt missing anatomy
- invent a hidden side
- replace a vehicle suspension
- redesign a weapon
- fuse major components to pass a connectedness check
- remove a component because it is difficult to rig

Substantial modeling work becomes manual review or a new generated candidate.

## Triangulation

The final export mesh must be triangular unless a locally verified exporter or engine path proves otherwise. Triangulation happens before final weight and export validation so face changes cannot invalidate later evidence.

Record:

- triangulation method
- triangle count before and after
- changed normals or UV issues
- whether the provider already supplied triangles

## Object separation policy

Keep a part separate when it requires:

- independent animation
- distinct pivot
- distinct material treatment
- damage or state switching
- reuse across variants
- visibility control

Typical separate parts:

- turret
- gun barrel
- recoil slide
- propeller
- rotor
- wheels or tracks when animated
- doors
- wings or control surfaces when animated
- creature jaw or special appendage

Object count must still match a tested local precedent and exporter behavior.

## UV and textures

### Source preservation

Retain provider source textures unchanged in the docs asset package.

### Processing

- verify UVs are nonempty
- inspect seams at normal map-view scale and close range
- remove baked lighting when practical or retexture
- fix color-space assignments
- convert or pack channels according to the exact PDX material precedent
- resize only to profile-approved dimensions
- enforce the profile maximum texture dimension; the current HOI4 model profile is capped at 1024 pixels on the longest side
- generate mipmaps or DDS through the repository's approved texture workflow
- keep alpha behavior explicit

### Texture names

Use stable asset-scoped names such as:

```text
<asset_slug>_diffuse.dds
<asset_slug>_normal.dds
<asset_slug>_specular.dds
```

The actual channel set follows the local vanilla material and `io_pdx_mesh` conventions. Do not assume a modern metallic-roughness set maps directly to HOI4.

## PDX materials

The adapter should create or configure PDX materials using a locally verified vanilla material from the same domain.

The material report records:

- PDX shader or material type
- source PBR inputs
- channel conversion
- texture paths
- alpha mode
- double-sided state if relevant
- unsupported provider maps
- visual differences after conversion

No asset passes materials QA while it displays magenta, black, unlit, overly glossy, transparent by accident, or with missing paths.

Runtime texticons are part of model QA. If a custom subunit id is consumed by `common/units`, register its generated `unit_<subunit_id>_icon_small` token against a verified vanilla icon before the live gate.

## Rig processing

Rig work follows `07_rigging_and_animation_pipeline.md`. The Blender stage may:

- import and preserve a provider rig
- map or rebuild bones
- create a custom armature
- create control bones not exported to runtime when supported
- create vertex groups
- assign and normalize weights
- bake constraints into export actions

## Action processing

Each action is isolated and named by semantic role. The scene must not rely on an arbitrary active action at export time.

Action report fields:

- source action
- final action name
- frame range
- FPS
- loop state
- root translation and rotation summary
- keyed bones
- constraint bake state
- start/end pose delta
- foot or contact drift
- exported filename

## Export preparation

Before export:

- only approved objects are visible in the export collection
- no reference or evidence object is selected
- transforms are approved
- mesh is triangulated
- texture paths are relative and valid
- armature is approved when required
- action frame range is explicit
- exporter version and settings are recorded
- output folder is empty or versioned

## PDX export

Export separately:

- one or more `.mesh` files as required by the precedent
- one `.anim` per approved action or the exact local pattern
- exporter logs

The adapter must surface every exporter warning. A file existing does not mean export passed.

## Post-export checks

Where supported:

- re-import the mesh into a fresh scene
- re-import each animation against the approved skeleton
- compare bounding boxes
- compare material slots
- compare bone names and count
- compare action frame count
- verify all referenced texture paths exist

If re-import is not supported or reliable, document the limitation and rely on parser checks plus the in-game test.

## Runtime handoff

The 3D worker proposes:

- final mesh path
- final animation paths
- texture paths
- entity and asset identifiers
- animation role mapping
- scale recommendation
- variant relationships
- required consumer files
- ready-to-copy snippets only when a local precedent has been inspected

The main agent owns the final source edits and completion claim.

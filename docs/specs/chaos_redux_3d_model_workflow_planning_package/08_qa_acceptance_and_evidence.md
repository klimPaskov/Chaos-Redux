# QA, Acceptance, and Evidence

## Quality model

QA is a sequence of blocking gates. A later gate cannot compensate for a failed earlier gate.

1. source and rights
2. generation geometry
3. Blender geometry
4. materials
5. rig
6. actions
7. PDX export
8. runtime wiring
9. in-game presentation

## Finding severity

| Severity | Meaning | Completion effect |
| --- | --- | --- |
| `blocker` | Invalid identity, missing required artifact, broken geometry, unsafe dependency, failed export, or failed runtime | Cannot proceed or complete |
| `major` | Visible defect, bad deformation, wrong scale, missing action, material error, or unreliable loop | Must be fixed before handoff |
| `minor` | Small visual or documentation defect that does not alter identity or runtime behavior | May proceed only with recorded disposition |
| `note` | Observation or future improvement | Does not block |

A known simplification is not automatically minor. It must be discussed under the project's no-fallback rule.

## Source gate

Required evidence:

- original reference file
- checksum
- provenance
- license or user-provided status
- preflight report
- derived-reference diff and approval when used
- one-subject confirmation

Blockers:

- unknown rights for an asset that needs documented reuse
- real design changed without approval
- unusable silhouette
- missing or corrupt reference

## Generation gate

Required evidence:

- redacted request
- provider version and task ID
- consumed credits
- downloaded outputs and checksums
- multi-view contact preview
- candidate review report

Blockers:

- missing major component
- floating or disconnected critical component
- identity mismatch
- large open geometry caused by hallucination
- unrecoverable fused limbs or mechanisms
- missing local download

## Geometry gate

Automated checks:

- triangle and vertex counts
- transforms
- loose parts
- non-manifold and boundary edges
- degenerate geometry
- normals
- UV layers
- material slots
- bounds and ground contact

Semantic checks depend on the profile.

Blockers:

- invalid topology for the exporter
- geometry outside the hard-block profile band without an approved precedent
- required animated component cannot move
- source and working model lineage is unclear
- unapproved destructive repair

## Material gate

Required evidence:

- source texture set
- channel-conversion note
- processed PNG or lossless intermediates
- final DDS files
- PDX material configuration
- Blender render using the PDX-equivalent setup
- file-path audit

Blockers:

- missing runtime texture
- wrong alpha behavior
- baked lighting that makes the model unusable and was not approved
- material displays incorrectly in Blender or game
- unsupported PBR map silently discarded without documentation

## Rig gate

Required evidence:

- rig map
- skeleton hierarchy listing
- semantic bone mapping for provider rigs
- weight report
- deformation pose contact sheet
- zero-weight and influence audit

Blockers:

- missing required bone or pivot
- invalid hierarchy
- severe deformation
- unweighted vertices
- opposite-side stretch
- rigid mechanism bends
- exporter-incompatible skeleton

## Animation gate

Required evidence:

- action manifest
- source action lineage
- frame range and FPS
- root-motion report
- loop delta report
- preview and key-pose contact sheet
- export mapping

Blockers:

- required action missing
- unapproved static substitution
- broken loop
- severe foot or contact sliding
- whole-model drift
- wrong semantic action
- deformation failure

## Export gate

Required evidence:

- exporter version and checksum
- export settings
- `.mesh` and `.anim` checksums
- full exporter log
- optional re-import report
- texture-path report

Blockers:

- exporter exception
- missing output
- warning that affects geometry, skeleton, action, or material integrity
- path points outside the mod or uses a missing file
- export cannot be associated with an approved Blender checkpoint

## Runtime wiring gate

The requirement-to-runtime crosswalk must contain one row per accepted requirement.

Required columns:

| Requirement ID | Design source | Purpose | Source artifact | Working artifact | Final runtime file | Registration | Consumer | State/action binding | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Examples of exact rows:

- base mesh
- each material and texture map
- skeleton
- idle action
- movement action
- attack action
- turret action
- building state variant
- entity definition
- equipment or unit model consumer

Counts do not prove coverage. An extra action cannot replace a missing required action without an accepted design amendment.

## In-game gate

### Visual checks

- correct scale relative to vanilla
- correct ground or water contact
- correct facing
- textures load at all expected zooms
- no magenta, black, invisible, or transparent failure
- no severe shimmer from excessive detail
- no visible holes during motion
- silhouette remains readable

### Animation checks

- correct action plays for the correct state
- idle loops
- movement loops and speed reads correctly
- attack timing is readable
- turret, recoil, propeller, limb, jaw, or special motion uses the correct pivot
- transitions do not snap unexpectedly
- no exported reference object appears

### Performance checks

- expected number of simultaneous instances does not cause an unacceptable frame-time increase
- material and texture count match the profile
- animation does not trigger excessive update cost

The pilot defines a repeatable capture scene and comparison method rather than relying on memory.

## Evidence package

A complete model package includes:

```text
reference and provenance
preflight
provider request and response
provider task and credit ledger
provider source files
chosen and rejected candidate notes
blend source and checkpoints
geometry report
material report
texture sources and DDS
rig report
weight report
action manifests
animation previews
mesh and animation exports
export log
runtime handoff
requirement-to-runtime crosswalk
in-game validation report
final manifest
```

## Completion states

### `complete`

Every accepted row has a source, runtime registration, live consumer, evidence, and in-game pass.

### `needs_user_review`

A visual, identity, license, or design decision requires the user. The asset is not complete.

### `blocked`

A technical, rights, cost, dependency, or runtime issue prevents completion.

### `canceled`

Work stopped intentionally, with artifacts and credits recorded.

There is no `complete_with_fallback` state.

## Audit after late changes

Any change to the accepted design, reference, skeleton, profile, action list, material set, or runtime consumer requires a fresh coverage diff:

- added rows
- removed rows
- replaced rows
- changed rows
- still-uncovered rows

Do not reuse a prior total or contact sheet as completion evidence after a material change.

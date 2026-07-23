# Job Lifecycle and Orchestration

## Job identity

Every request becomes one model job before any paid request or Blender write occurs.

Recommended ID:

```text
3d_<event_id_or_system>_<asset_slug>_<yyyyMMdd_HHmmss>
```

Examples:

```text
3d_003_holy_realm_temple_20260722_143000
3d_014_cannibal_raider_20260722_150500
3d_shared_chemical_tank_20260722_161500
```

The ID remains stable across retries. Attempts receive separate ordinal IDs.

## Job directory

```text
docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/
  job.yaml
  history.jsonl
  references/
    original/
    derived/
  briefs/
  provider/
    requests/
    responses/
    downloads/
    rejected/
  blender/
    source/
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
    logs/
  runtime/
    handoff.md
    crosswalk.md
    validation/
  manifest.md
```

Final runtime assets move to their approved gameplay folders. The docs package retains source, evidence, and lineage.

## Intake contract

The job must define:

- asset owner and purpose
- exact asset class and profile
- one reference image
- provenance and license or user-provided status
- intended subject, silhouette, visible parts, and rear-side assumptions
- forbidden additions
- desired texture treatment
- whether generation must preserve a real design or may interpret it
- target vanilla reference model or reference family
- required scale relationship
- static or animated requirement
- required action roles
- runtime consumer
- credit ceiling
- maximum paid attempts
- review authority

Ambiguity is not hidden. It is recorded under `known_ambiguity` and resolved before generation or accepted as an intentional interpretation risk.

## Reference preflight

The reference receives one of four statuses:

- `approved_original`
- `approved_derived`
- `needs_user_review`
- `blocked`

A derived reference may perform only approved clarification work such as:

- background removal
- exposure correction
- filling an obviously accidental dark seam that the generator may interpret as a hole
- cropping to one complete subject
- removing a caption or UI border without removing subject geometry

It may not invent unseen parts, redesign the subject, or silently change identity.

## Paid-call gate

Before a paid Meshy tool is called, orchestration must verify:

1. job schema passes
2. reference preflight is approved
3. requested operation is allowed for the profile
4. current balance is known
5. estimated cost fits both job and session budgets
6. paid attempt count is below the ceiling
7. output directory exists
8. download and retention handling is ready

The gate writes an approval record before submission.

## Attempt model

Each provider operation creates an attempt record:

```text
attempt_id
operation
provider_task_id
submitted_at
completed_at
request_summary
estimated_credits
consumed_credits
status
output_checksums
review_result
rejection_reasons
parent_attempt_id
```

A remesh, retexture, rig, and animation each receive their own attempt. They are not merged into the generation attempt.

## Orchestration stages

### Stage 1: intake and preflight

- create job
- validate schema
- hash reference
- write preflight report
- choose asset profile
- estimate cost range

### Stage 2: source generation

- check balance
- submit image-to-3D
- poll or receive status updates
- download immediately
- hash all outputs
- record consumed credits
- create contact preview
- run generation review

### Stage 3: optional provider post-processing

- remesh only when profile and geometry review justify it
- retexture only when geometry is already accepted
- rig only for supported humanoid candidates
- animate only after rig approval and action inventory review

### Stage 4: Blender processing

- create job scene from template
- import candidate into protected source collection
- duplicate into working collection
- inspect and repair
- normalize scale and orientation
- create PDX materials and textures
- create or validate skeleton
- author or clean actions
- save checkpoints after every gate

### Stage 5: PDX export

- export mesh
- export required animations
- record exporter log and checksums
- package runtime handoff

### Stage 6: main-agent wiring

- register materials, assets, entities, models, or gameplay consumers
- keep exact identifiers in the crosswalk
- do not rename the asset without updating the job and manifest

### Stage 7: in-game validation

- test at normal map zoom and close inspection
- test every action transition and loop
- test material and texture loading
- test multiplayer-safe deterministic configuration where relevant
- record screenshots or video evidence

## Review authorities

| Gate | Minimum reviewer |
| --- | --- |
| Reference preflight | Parent agent or user-defined asset owner |
| Paid retry beyond normal budget | Parent agent |
| Generation geometry approval | 3D asset worker plus human review for ambiguous identity |
| Blender geometry and materials | 3D asset worker |
| Rig and animation | 3D asset worker, with manual review of deformation |
| Runtime wiring | Main implementation agent |
| In-game acceptance | Main implementation agent |
| Simplification or fallback | User discussion required |

## Retry policy

Retries are bounded by cause.

### Provider retry

Use when the candidate is globally wrong, missing important components, heavily fused, or contains unrecoverable hallucinated geometry.

### Reference revision

Use when the source image contains a misleading gap, shadow, cropped component, or overlapping silhouette.

### Blender repair

Use when the identity is correct and defects are local, such as loose pieces, small holes, normals, limited intersections, minor topology cleanup, or material conversion.

### Manual modeling review

Use when the model needs substantial authored reconstruction that exceeds the planned automated repair scope.

### Hard block

Use when identity, license, technical feasibility, budget, exporter support, or runtime precedent is unresolved.

No job may loop indefinitely. Reaching the paid retry ceiling requires a parent decision to revise the reference, change the profile, increase the budget, or stop.

## Concurrency

Meshy queue and request limits are account-scoped and can change. The orchestrator therefore uses configurable limits rather than fixed assumptions.

Recommended initial policy:

- one paid generation at a time during the pilot
- up to two status or download operations concurrently
- one Blender write job per Blender profile
- one PDX export at a time
- exponential backoff with jitter for 429 and transient provider errors
- no automatic retry for validation, billing, authentication, or unsupported-input errors

## Naming rules

Use lowercase snake_case for:

- asset slugs
- Blender collections
- objects
- armatures
- bones where the runtime convention permits it
- actions
- material names
- texture filenames
- mesh and animation filenames

Provider task IDs remain unchanged and are stored as metadata, not used as asset names.

## Checkpoints and rollback

Mandatory Blender checkpoints:

1. imported candidate
2. geometry-approved
3. materials-approved
4. rig-approved
5. each action family approved
6. pre-export
7. exported

A repair step writes to a new checkpoint. It does not overwrite the previous approved state until the next gate passes.

## Cancellation

Cancellation stops new paid work and Blender writes. It does not delete evidence. The job records:

- who canceled it
- time
- reason
- credits already consumed
- retained artifacts
- cleanup actions
- whether the asset can be resumed

## Update: autonomous Meshy start gate and single-image reference rule

Before any modeling work begins, verify that `MESHY_API_KEY` exists as an environment variable. If it is missing, stop and instruct the user to run the documented PowerShell command, then restart the shell or Codex.

This workflow may generate its own Meshy-ready reference image when the user provides only an asset brief. Meshy still receives exactly one clean final reference image. Do not create side-profile sheets, multi-view boards, or other multi-image collages for Meshy. The workflow resolves its own deterministic working paths and saves the final reference image there before Meshy starts.

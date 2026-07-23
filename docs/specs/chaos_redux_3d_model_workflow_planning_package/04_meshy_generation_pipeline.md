# Meshy Generation Pipeline

## Provider role

Meshy creates candidate geometry, PBR texture sources, and, for suitable humanoid characters, optional rig and preset animation sources. It is not the authority for HOI4 scale, topology budget, skeleton policy, action names, material format, or runtime readiness.

## Single-reference contract

The normal job uses exactly one reference image. It can also include structured instructions in the job brief, but the current Image-to-3D API surface must be treated honestly:

- the image is the primary geometry input
- text direction can be used for texture generation where the tool exposes `texture_prompt`
- orchestration notes can guide candidate selection and later Blender work
- a general free-form geometry prompt must not be assumed when the live MCP tool schema does not expose one

At job start, inspect the current MCP tool schema. Store the schema version and exact submitted fields.

## Reference-image quality rules

Prefer:

- one complete subject
- unobstructed silhouette
- neutral or simple background
- strong separation between limbs, turrets, wings, legs, antennae, and body
- even lighting
- minimal cast shadow
- enough resolution to see component boundaries
- a view that communicates the subject's dominant form

Flag:

- black gaps that may be interpreted as missing geometry
- cropped extremities
- heavy perspective distortion
- components hidden behind the body
- mirrored or asymmetric details that the image does not explain
- translucent parts
- thin wires or barrels near pixel width
- painted details that could be mistaken for geometry
- multiple subjects
- readable text that should not become texture noise

## Generation defaults

The initial request should prefer the current smart-topology route when it is available and appropriate.

Conceptual defaults:

- model family: current smart topology model
- topology: triangles
- target polygon count: profile value, not a universal number
- PBR maps: enabled
- lighting removal: enabled when the source contains baked lighting
- pose: `none` for static assets, suitable A or T pose for humanoids when supported
- auto-sizing: disabled for final scale because Blender owns scale normalization
- output: GLB as the canonical provider archive plus FBX when rig or animation interchange requires it
- transparent preview: enabled when available and useful

The exact MCP field names are taken from the current tool schema and stored in the request evidence.

## Topology strategy

### Strategy A: smart-topology first

Use for most jobs. It should target the asset profile's working range while preserving major components.

### Strategy B: high-detail source then controlled reduction

Use when the low-count candidate leaves gaps, breaks thin structures, fuses limbs, or loses the subject's identity.

Sequence:

1. generate the higher-detail source
2. approve its geometry before reducing it
3. remesh through Meshy or Blender according to comparative tests
4. compare component survival and silhouette
5. select the lowest acceptable candidate, not simply the lowest count

### Strategy C: reference revision

Use when the same defect repeats and corresponds to source-image ambiguity. The derived reference must be approved and documented.

### Strategy D: stop

Use when repeated generation cannot produce a viable core without redesigning the subject.

## Polygon budget policy

The tutorial's approximately 10,000-vertex target and 25,000 to 30,000 upper caution are recorded as useful historical heuristics. They are not universal HOI4 limits.

Every asset profile obtains a tested budget from local vanilla precedents:

- triangle count
- vertex count
- material slots
- texture dimensions
- bone count
- action complexity
- expected simultaneous on-map instances

The profile can define a preferred, review, and hard-block band. Exceeding the preferred band is not an automatic rejection when a vanilla precedent and runtime test justify it.

## Texture generation

Use PBR generation and retain all returned maps. The texture brief should specify:

- period and faction style
- base materials
- finish and wear
- camouflage or paint placement
- what must remain unpainted
- forbidden text, symbols, and modern details
- whether color must follow the reference strictly

The texture prompt is limited by the provider's current schema. Store the exact prompt and character count.

Texture approval occurs after geometry approval. Do not spend retexture credits on a rejected mesh.

## Candidate review

Create a review sheet with at least:

- front
- rear
- left
- right
- top or high three-quarter
- underside where relevant
- wireframe
- untextured shaded view
- textured view

Inspect:

- overall identity
- missing or duplicated components
- floating geometry
- fused limbs or weapons
- hollow openings
- disconnected parts
- thin-part survival
- symmetry errors
- rear-side invention
- wheel, track, wing, mast, barrel, and propeller shape
- surface noise
- texture seams and baked shadows

The candidate receives one of these decisions:

- `approved_for_blender`
- `approved_for_blender_with_local_repairs`
- `retry_generation`
- `revise_reference`
- `blocked`

## Download and retention

Provider URLs are temporary. Every successful task is downloaded immediately and verified before the task is considered captured.

Required downloads when available:

- GLB
- FBX
- OBJ only when needed for inspection
- base color
- normal
- roughness
- metallic
- any packed texture maps
- thumbnail
- transparent thumbnail
- rigged output
- each animated output
- task response JSON

After download:

1. calculate SHA256
2. verify file size is nonzero
3. attempt format open or import
4. record the local path
5. keep the remote URL only in redacted evidence

## Remesh decision

Remesh when:

- face count exceeds the approved working range
- topology density is badly distributed
- deformation requires cleaner topology
- source detail needs controlled simplification

Do not remesh merely because the operation exists. Compare provider remesh with Blender reduction during the pilot.

Required remesh settings:

- triangular output
- target count or adaptive quality from the profile
- preserve texture or regenerate texture deliberately
- no automatic quad route for final HOI4 export unless the mesh is subsequently triangulated and deformation tests prove the route better

## Meshy rigging route

Meshy auto-rigging is permitted only when all of these are true:

- the subject is a standard humanoid biped
- limbs and body structure are clear
- the mesh is textured or otherwise supported by the current API
- face count is within the current rigging service limit
- the model faces the provider's required direction
- the intended HOI4 skeleton can be mapped without destructive deformation

Nonhuman creatures, vehicles, aircraft, ships, buildings, and unusual humanoids use Blender-authored rigs unless a future provider revision is locally verified for that class.

## Meshy animation route

Provider animations are source candidates. The workflow must:

1. enumerate currently available actions or approved action IDs
2. choose the closest semantic action
3. request an approved frame rate
4. download both GLB and FBX when available
5. inspect the skeleton and root behavior
6. retarget or clean the action in Blender
7. rename it to the project action role
8. verify the loop and HOI4 export

Do not hard-code undocumented action IDs in the skill.

## Cost control

Every paid operation records estimated and consumed credits. A typical planning calculation is:

```text
image_to_3d + optional_remesh + optional_rig + action_count * animation_cost + optional_retexture
```

The live balance and live provider pricing page override package examples. `tools/estimate_meshy_credits.py` provides a planning estimate and labels it with the snapshot date.

## Provider error handling

| Error class | Response |
| --- | --- |
| Authentication or authorization | Stop, do not retry, repair secret or entitlement |
| Insufficient credits | Stop, report required and available balance |
| Rate limit | Backoff with jitter, preserve same job attempt |
| Unsupported input | Stop or revise input, do not retry unchanged |
| Provider processing failure | Record failure and consumed credits, then apply paid retry policy |
| Expired output URL | Attempt provider task lookup once, otherwise mark artifact capture failure |
| Corrupt download | Redownload while URL is valid, then block if checksum/open still fails |
| Content or license concern | Stop and escalate to parent |

## Update: autonomous Meshy start gate and single-image reference rule

Before any modeling work begins, verify that `MESHY_API_KEY` exists as an environment variable. If it is missing, stop and instruct the user to run the documented PowerShell command, then restart the shell or Codex.

This workflow may generate its own Meshy-ready reference image when the user provides only an asset brief. Meshy still receives exactly one clean final reference image. Do not create side-profile sheets, multi-view boards, or other multi-image collages for Meshy. The workflow resolves its own deterministic working paths and saves the final reference image there before Meshy starts.

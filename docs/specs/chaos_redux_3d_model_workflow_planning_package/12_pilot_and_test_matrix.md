# Pilot and Test Matrix

## Pilot purpose

The first release is not promoted after one easy static prop. It must prove the four most important failure classes:

1. single-image architectural reconstruction
2. provider humanoid rig and animation interchange
3. custom nonhumanoid rigging and IK
4. mechanical pivots and multiple actions

The actual reference images must be supplied or approved before paid generation.

## Primary pilot A: static building

### Suggested subject

A distinctive event building with a clear silhouette and limited repeated facade detail.

### Profile

`building`

### Required outputs

- textured source model
- normalized `.blend`
- PDX materials and DDS textures
- final `.mesh`
- runtime handoff
- in-game scale and material proof

### Tests

- unseen rear-side invention review
- base and ground alignment
- isometric readability
- material-slot economy
- no animation path

### Pass

The building reads correctly at expected map zoom, uses a calibrated budget, sits on the ground, and has no missing runtime texture.

## Primary pilot B: humanoid unit

### Suggested subject

A clear full-body soldier or humanoid special unit with a visible weapon and separated limbs.

### Profile

`humanoid_unit`

### Required actions

- idle
- move
- attack

### Required routes

- smart-topology generation
- Meshy auto-rig candidate
- at least one Meshy animation candidate
- Blender retarget or cleanup
- PDX mesh and animation export

### Tests

- provider rig suitability
- target skeleton mapping
- weapon and hand deformation
- foot contact
- in-place movement
- idle and movement loops
- attack recovery

### Pass

All three actions are wired and play correctly in game. No static substitution is permitted.

## Primary pilot C: nonhumanoid creature

### Suggested subject

A crab-like, quadrupedal, insectoid, or other multi-limbed creature similar to the tutorial's rigging problem.

### Profile

`nonhumanoid_creature`

### Required actions

- idle
- move
- attack or claw strike

### Required routes

- Meshy geometry and texture only
- custom Blender rig map
- mirrored limb chains
- disconnected IK targets where needed
- explicit vertex-group assignment and weight audit

### Tests

- dark-gap reference failure risk
- leg and body connectedness
- correct chain lengths
- all planted limbs remain stable enough
- no opposite-side weight stretch
- body lift and attack extremes

### Pass

The creature retains its identity, all required limbs deform correctly, and every action passes in game.

## Primary pilot D: land vehicle

### Suggested subject

A tank, walking vehicle, artillery vehicle, or unusual armored machine with a turret and recoil-capable weapon.

### Profile

`vehicle_land`

### Required actions

- idle
- move where the runtime surface uses it
- attack or recoil
- turret or barrel movement when supported

### Tests

- hull and turret separation
- pivot placement
- barrel integrity
- wheel or track alignment
- rigid weights
- recoil return
- correct origin and ground contact

### Pass

The turret, barrel, and recoil hierarchy behaves correctly and the unit loads with the approved scale and materials.

## Secondary promotion pilots

After the primary pilots pass:

| Pilot | Profile | Critical proof |
| --- | --- | --- |
| Fighter or bomber | `aircraft` | wing symmetry, propeller or rotor, air model scale |
| Ship or submarine | `naval` | waterline, mast detail, turret pivots |
| Static special device | `static_prop` | low-cost source and high-instance performance |
| Modular weapon | `articulated_attachment` | parent transform and reusable action |

## Failure-injection tests

### Reference tests

| Test | Expected result |
| --- | --- |
| dark joint looks like a hole | Preflight warning or derived-reference approval required |
| cropped barrel or limb | Block before generation |
| multiple subjects | Block or crop to one approved subject |
| workflow-generated reference has an opaque background or strong shadow | Reject the source and request native transparent output; use documented edit/removal only if native transparency fails |
| inherited, sourced, or user-provided reference has an opaque background with a strong shadow | Warn and use documented fallback removal or approve the reconstruction risk |
| source rights omitted | Block |

### Provider tests

| Test | Expected result |
| --- | --- |
| authentication failure | Stop without retry |
| insufficient credits | Stop with cost report |
| 429 | Backoff and preserve attempt |
| succeeded task with corrupt file | Redownload then block if still corrupt |
| task URL near expiry | Immediate capture and warning |
| repeated fused limbs | Switch strategy or revise reference, do not loop indefinitely |

### Blender security tests

| Test | Expected result |
| --- | --- |
| free-form Python argument | Rejected |
| output path outside job root | Rejected |
| listener bound to non-loopback | Environment verification fails |
| unapproved extension checksum | Installation and job fail |
| source collection edit attempt | Rejected or detected by checksum |

### Geometry tests

| Test | Expected result |
| --- | --- |
| negative scale | Block until normalized |
| non-triangular final mesh | Block |
| zero-weight vertices | Block rig approval |
| floating critical component | Block or bounded repair review |
| hard-budget exceedance | Block unless approved precedent and runtime test exist |

### Animation tests

| Test | Expected result |
| --- | --- |
| first and last loop poses diverge | Block action |
| unexpected root drift | Block action |
| rigid turret bends | Block rig |
| attack action missing | Block runtime handoff |
| skeleton changed after action approval | Invalidate all downstream actions and exports |

### Runtime tests

| Test | Expected result |
| --- | --- |
| texture path missing | Block in-game gate |
| wrong facing | Return to orientation stage |
| model floats or sinks | Return to origin and scale stage |
| action mapping wrong | Return to runtime mapping or action stage |
| unacceptable high-instance cost | Optimize and retest |

## Metrics

Record per pilot:

- number of paid generation attempts
- credits estimated and consumed
- time spent in each stage
- original and final triangle count
- original and final object count
- texture count and dimensions
- bone count
- action count
- number of blocking findings
- number of manual modeling interventions
- in-game performance delta in the repeatable test scene

## Promotion criteria

The workflow can be promoted from pilot to production only when:

- all four primary pilots pass
- all security injection tests pass
- no pilot used an undisclosed fallback
- actual costs are within documented expectations or the model is updated
- every pilot has complete requirement-to-runtime coverage
- the main agent confirms the handoff was sufficient to wire without guessing
- the dependency lock can reproduce the environment on a clean profile

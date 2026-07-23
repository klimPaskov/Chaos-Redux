# Asset Profiles

## Profile purpose

One universal model pipeline would create bad results. Each asset class receives a profile with semantic checks, Blender operations, animation expectations, and runtime evidence.

All numeric budgets are configuration values derived from local vanilla examples. The examples below describe policy, not fixed engine limits.

## Shared profile fields

Every profile defines:

```text
profile_id
runtime_domain
vanilla_reference_paths
forward_axis
up_axis
ground_rule
preferred_triangle_band
review_triangle_band
hard_block_triangle_band
material_slot_limit
texture_set
texture_dimensions
rig_route
action_roles
root_motion_policy
instance_density
semantic_checks
export_preset
runtime_consumers
```

## Profile matrix

| Profile | Meshy role | Default rig route | Typical animation roles | Most important QA |
| --- | --- | --- | --- | --- |
| `static_prop` | Generate geometry and PBR | None | Optional state animation | silhouette, pivot, scale, materials |
| `building` | Generate massing and facade candidate | None or limited mechanical rig | smoke, door, machinery only when required | ground contact, camera readability, material economy |
| `humanoid_unit` | Generate posed character, optional rig and motion | Meshy candidate then Blender mapping, or Blender rig | idle, move, attack, death or special roles as required | limbs, weights, feet, weapon, loop, scale |
| `nonhumanoid_creature` | Generate geometry and texture | Blender custom armature | idle, move, attack, special | anatomy, limb chains, IK, deformation, silhouette |
| `vehicle_land` | Generate body and components | Blender mechanical rig | idle, move, attack, recoil, turret | wheel/track alignment, turret pivots, barrel, ground contact |
| `aircraft` | Generate airframe candidate | Blender mechanical rig | idle, move, attack, propeller or rotor | wing symmetry, landing alignment, propeller pivot, scale |
| `naval` | Generate hull and superstructure | Blender mechanical rig when needed | idle, move, attack, turret or radar | waterline, hull integrity, mast thin parts, turret pivots |
| `articulated_attachment` | Generate or source one modular part | Blender mechanical rig | recoil, rotate, open, pulse | pivot, attachment transform, action isolation |

## Static prop

Use for equipment on the map, monuments, wrecks, stationary devices, and non-building objects.

Requirements:

- one clear origin and ground point
- no rig unless an actual runtime action is required
- low material count
- silhouette readable at expected zoom
- optional collision or locator data only when the target surface uses it
- no hidden high-detail interior unless the camera can see it

Generation notes:

- smart topology is normally preferred
- use a higher-detail source only when thin parts fail
- separate meaningful moving parts before export

## Building

Use for map buildings, special structures, towers, facilities, temples, bunkers, factories, and event-specific structures.

Requirements:

- test against a vanilla building from the same surface
- align the base to the ground plane
- confirm expected camera and isometric readability
- preserve large facade features and roofline
- reduce micro-detail that creates shimmer
- define damage, construction, or state variants only when the runtime system consumes them

Meshy limits:

- a single perspective image can hallucinate the unseen side
- generated windows and doors may become geometry noise
- repetitive architecture may need Blender cleanup or manual correction

Animation:

- no ambient motion by default
- machinery, doors, emitters, or occult mechanisms require explicit actions and runtime support

## Humanoid unit

Use for infantry, monsters with human structure, special soldiers, leaders used as map units, and humanoid robots.

Reference preflight:

- full body visible
- arms separated from torso where possible
- legs separated
- weapon or held object visible and not fused across limbs
- neutral A or T pose preferred for rigging

Rig route:

1. Meshy rig is allowed for a clear biped.
2. Import rigged output into Blender.
3. Compare provider skeleton with the target HOI4 precedent.
4. Retarget or rebuild as needed.
5. Bake approved actions to the export skeleton.

Minimum semantic bones or controls depend on the target skeleton, but usually cover:

- root
- pelvis/body
- spine or body chain
- head
- left and right upper and lower limbs
- feet and hands when deformation needs them
- weapon or attachment bone when the asset requires it

Animation roles are profile and consumer driven. Do not assume every unit needs all roles.

## Nonhumanoid creature

Use for quadrupeds, insects, crustaceans, tentacled creatures, supernatural forms, and event monsters.

Default route:

- Meshy generates geometry and texture only
- Blender creates a custom armature
- bone hierarchy follows body mass, limb chains, jaws, tails, wings, and special appendages
- IK is added where planted limbs need stable contact
- control bones are separated from deform bones when the exporter pattern supports it

Semantic QA:

- all major legs and appendages exist
- mirrored anatomy is intentional
- joints contain enough topology to bend
- no body part is assigned to a distant opposite-side bone
- planted limbs do not skate excessively
- idle pose does not collapse the body

The tutorial's root, body, mirrored limb, disconnected IK target, and chain-length approach is a starting pattern. Each creature receives a documented rig map.

## Land vehicle

Use for tanks, trucks, artillery carriers, walkers, armored trains, and other land machines.

Object plan should identify:

- hull
- turret
- gun barrel
- recoil part
- wheels
- tracks
- antennas
- mounted equipment
- optional damage parts

Default rig:

- root at a tested vehicle pivot
- hull bone or object
- turret yaw bone
- barrel pitch bone
- recoil bone when visible
- wheel or track animation only when runtime precedent supports it and it is visible

Hard semantic blockers:

- asymmetric wheel count without design basis
- floating tracks
- fused turret that must rotate
- bent or sealed gun barrel
- underside far above or below ground
- obvious modern or incorrect component introduced by the generator

## Aircraft

Use for fixed-wing aircraft, helicopters, strange aircraft, drones, and airborne creatures that use model assets.

Requirements:

- wing and tail symmetry unless intentionally asymmetric
- control surfaces coherent
- propeller or rotor separated when animated
- landing alignment or airborne origin based on the local precedent
- no baked ground shadow
- thin antennae and landing gear reviewed after reduction

Animation roles may include:

- propeller or rotor loop
- idle
- move
- attack
- gear or door state only when the consumer supports it

## Naval

Use for ships, submarines, sea creatures used as naval units, and floating structures.

Requirements:

- approved waterline
- hull closed where visible
- no accidental keel or deck holes
- mast and gun thin parts survive
- turrets have correct pivots
- scale against a same-class vanilla ship
- material gloss remains readable without mirror-like artifacts

Animation roles may include:

- idle or bob only if runtime precedent exists
- move
- attack
- turret rotation or gun recoil
- radar, propeller, or special mechanism

Avoid generating extensive unseen underwater detail unless it affects the runtime view.

## Articulated attachment

Use for modular weapons, turrets, launchers, doors, tentacles, equipment packs, and replaceable mechanisms.

Requirements:

- attachment origin and parent locator documented
- local axis documented
- action affects only the intended hierarchy
- no duplicate root movement
- static fallback available when the action is not used
- variant compatibility proven against each parent model

## Instance-density factor

A model seen once can tolerate more cost than an infantry asset rendered many times. Profiles record expected instance density:

- `rare_unique`
- `low`
- `medium`
- `high`
- `very_high`

Triangle and material budgets must become stricter as instance density rises, subject to local runtime testing.

## Profile calibration record

Before a profile is promoted, inspect at least three local precedents when available. Record:

| Reference | Runtime use | Triangles | Vertices | Bones | Actions | Materials | Textures | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |

The profile's preferred band should reflect the reference family and intended simultaneous count, not a generic web guideline.

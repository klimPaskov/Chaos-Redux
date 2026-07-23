# Rigging and Animation Pipeline

## Rig route decision

```text
Need animation?
  no -> no armature unless runtime precedent requires one
  yes -> standard humanoid biped?
           yes -> evaluate Meshy rig candidate
                    compatible with HOI4 export skeleton?
                      yes -> map, clean, bake, validate
                      no -> retarget or rebuild in Blender
           no -> build custom Blender armature
```

The route decision is recorded before rig work.

## Skeleton principles

- one clear root for runtime movement
- parent hierarchy follows physical motion
- deform bones are distinguished from controls
- bone names remain stable after animation production begins
- mirror naming uses the project's tested convention
- exporter limits and local vanilla skeletons take priority over generic Blender practice
- every exported bone has a purpose
- unused provider bones are removed or explicitly retained with justification

## Humanoid rig path

### Provider-rig intake

Audit:

- root count
- bone count
- bone orientations
- forward direction
- scale
- hierarchy
- mesh binding
- unexpected facial or finger bones
- source actions

The provider rig may be used as:

- the final export skeleton if a local precedent proves compatibility
- a source skeleton for retargeting
- a temporary deformation rig while an export skeleton is built

### Retargeting

Retarget by semantic mapping, not bone-name similarity alone.

Required mapping record:

```text
source_bone
semantic_role
target_bone
rotation_correction
translation_policy
scale_policy
notes
```

Bake constraints before export. Verify the baked action with constraints disabled.

## Custom nonhumanoid rig path

### Rig map

Before adding bones, write a rig diagram that identifies:

- root
- primary body mass
- secondary body segments
- each limb chain
- planted contact points
- jaws, claws, tails, wings, turrets, barrels, and appendages
- IK targets and poles
- export and non-export controls

### Parenting

The tutorial pattern is retained as a useful default:

1. root controls the whole asset
2. body bones parent to root with offset where appropriate
3. limb chains parent to the body segment that carries them
4. IK target bones are not connected to the deform chain
5. mirrored limbs are inspected after mirroring rather than assumed correct

### IK

Use IK when it improves contact or posing. Record:

- target bone
- constrained bone
- chain length
- pole target
- stretch state
- whether constraints are baked for export

The tutorial's chain length of two is appropriate for a two-bone limb, not a universal value.

## Mechanical rigs

Vehicles and mechanisms use rigid or near-rigid weighting.

Typical hierarchy:

```text
root
  hull_or_body
    turret_yaw
      barrel_pitch
        recoil
    left_wheel_group
    right_wheel_group
```

Aircraft and ships follow the same principle with domain-specific parts.

Rigid components should not bend because of blended weights. Assign them to one deform bone or keep them as correctly parented objects according to the exporter precedent.

## Binding and weights

### Empty-group route

For custom rigs, parent the mesh with empty groups when automatic weights would create unsafe cross-body influences. Then assign groups deliberately.

### Weight rules

- every deforming vertex has a valid total weight
- weights are normalized
- zero-weight vertices are reported
- excessive influence count is reported against the local exporter and runtime precedent
- no opposite-side influence without a physical reason
- rigid parts use rigid weights
- joints have enough transition area to bend
- hidden source groups and provider groups are removed or documented

### Isolation workflow

The tutorial's hide-after-assignment technique is preserved as a manual review method. In automation, equivalent checks should track unassigned and multiply assigned regions without relying only on visibility state.

### X-ray selection warning

Manual edits must select through the full mesh when assigning cross-sections. Front-only selection is a known source of unweighted rear vertices.

## Deformation test poses

Before animation, create profile-specific test poses.

Humanoid:

- arm raise
- elbow bend
- leg lift
- knee bend
- torso twist
- weapon pose

Creature:

- each limb chain at minimum and maximum useful bend
- body lift
- jaw or claw motion
- tail or wing extremes

Mechanical:

- full turret yaw
- barrel pitch extremes
- maximum recoil
- door or hatch limits
- propeller or rotor full rotation sample

A rig cannot pass solely because the rest pose looks correct.

## Action inventory

Each job defines required semantic actions. Example roles:

- `idle`
- `move`
- `attack`
- `attack_alt`
- `death`
- `deploy`
- `recoil`
- `turn`
- `special`

The final runtime names come from local vanilla and Chaos Redux entity precedents. The role remains stable even if the actual action token differs.

## Animation source routes

### Meshy preset source

Use when a suitable provider action exists. Clean and retarget in Blender.

### Blender-authored action

Use for:

- nonhumanoid creatures
- mechanical motion
- special attacks
- route-specific idle behavior
- actions unavailable from the provider
- replacement of an unacceptable provider action

### Sourced animation

Permitted only when provenance, license, skeleton compatibility, and transformation rights are documented.

No route may silently replace a requested animation with a static pose.

## Animation authoring rules

- set explicit FPS and frame range
- keep one action per semantic role
- key only necessary controls or baked deform bones
- avoid sub-frame or unsupported interpolation assumptions
- keep contacts readable at map scale
- exaggerate small motion only when needed for HOI4 zoom readability and after review
- preserve the asset identity and physical limits
- remove accidental scale keys
- constrain root motion according to profile

## Root motion policy

Each action is classified:

- `in_place`
- `runtime_translation`
- `limited_recoil`
- `mechanical_rotation`

Most unit locomotion sources are converted to in-place movement unless the local runtime entity explicitly consumes root translation.

Checks:

- root starts at approved origin
- root does not drift vertically
- loop does not jump
- attack does not translate the whole unit unless intended
- recoil returns to the rest transform

## Loop QA

For looped actions:

- compare first and last evaluated pose
- inspect position and rotation deltas per exported bone
- inspect contact drift
- play at native FPS for at least five loops
- inspect at normal HOI4 map zoom
- inspect transitions from idle to action and back

A technically closed loop can still look bad. Human review remains required.

## Required preview package

For each action:

- viewport or rendered MP4/GIF for review
- frame range and FPS overlay in the evidence report, not inside runtime textures
- side and three-quarter views where deformation matters
- skeleton overlay preview when diagnosing weights
- static contact sheet of key poses

The preview is evidence only. The final HOI4 asset is the exported `.anim` package.

## Action acceptance

An action passes when:

- semantic role is clear
- required body parts move
- unintended parts stay stable
- no severe mesh collapse or stretch occurs
- loop or one-shot ending is correct
- root policy passes
- exporter accepts it
- runtime mapping exists
- in-game behavior passes

## Change control

Changing the skeleton after action approval invalidates:

- weight approval
- all baked actions
- export evidence
- runtime animation checks

The job state must return to rigging and regenerate downstream evidence.

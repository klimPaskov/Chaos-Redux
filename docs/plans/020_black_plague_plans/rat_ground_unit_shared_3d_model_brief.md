# Event 020 shared rat ground model brief

This package adds one reusable skeletal ground-creature model for the Black Plague armies. It is a single mesh and entity consumed by every rat subtype, every rat division template, the reusable Rat Nation `RTA`, and the separate Rat King `RTX`.

## Runtime scope

- Asset owner: `020_black_plague`
- Asset slug: `rat_ground_unit_shared`
- Job root: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`
- Proposed mesh registration: `black_plague_rat_mesh`
- Proposed entity registration: `black_plague_rat_entity`
- Consumers: `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, and `rat_tunnelers`
- Country consumers: `RTA` and `RTX`
- Model count: exactly one shared mesh/entity; no subtype meshes, brood variants, cosmetic-tag variants, or additional rat country tags

The parent-owned runtime wiring is now installed: all six subunits use `sprite = black_plague_rat`, all five locked templates use `override_model = black_plague_rat_entity`, the shared counter aliases and runtime DDS strips are registered, and the active `.gfx`/`.asset` files and runtime copies are hash-recorded. Sound definitions remain a separate review-gated handoff.

## Visual brief

Create a fictional plague rat creature suitable for a Hearts of Iron IV land-unit map entity. The silhouette is a large, low four-legged rat with a heavy shoulder line, long tail, strong paws and claws, scarred black fur, a plague-bleached muzzle, small ears, and visible whiskers. The mesh must remain readable at normal map zoom and must not include weapons, armor, uniforms, human anatomy, a crown, a royal prop, text, scenery, or a separate second creature.

One clean three-quarter full-body reference is allowed for Meshy. Front, rear, side, top, underside, wireframe, and material views are Blender evidence only and must never be sent to Meshy as additional input images.

## Profile and calibration

Use the `nonhumanoid_creature` profile with a custom Blender rig and a written rig map. Calibrate the source mesh against the installed vanilla `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity` precedent, including source height, baseline entity scale, effective runtime height, forward axis `-Y`, up axis `+Z`, ground contact, and origin. Use a single documented custom entity scale of `1.35` against the vanilla infantry scale `0.8`, producing an approximately `1.69x` infantry runtime height so the rat is clearly oversized on the map. Apply that custom scale exactly once and record both the baseline and final measurements.

The creature root must be at the ground origin and all authored movement must be in-place. The worker must record the measured values rather than substituting a generic real-world height.

## Required actions

- `idle`: looping in-place breathing, ear, whisker, and tail motion
- `move`: looping in-place quadruped locomotion
- `attack`: non-looping lunge or bite/claw action with no root translation
- `retreat`: looping in-place withdrawal using the same rig and mesh
- `death`: non-looping collapse/death action

Each action needs a semantic role, FPS, frame range, loop/root policy, contact review, preview, exported `.anim`, proposed runtime binding, and reimport evidence. The entity state table must cover `idle`, `attack`, `defend`, `support_attack`, `move`, `retreat`, `death`, and `training` without introducing a second mesh.

## Materials and package evidence

Use the verified PDX material channel mapping and 1024-pixel texture ceiling. Export repaired triangulated geometry, final DDS maps, `.mesh`, all required `.anim` files, Blender checkpoints, previews, actual-byte reimport proof, checksums, manifest, runtime handoff, and crosswalk. Do not leave runtime references pointing into `docs/assets/`.

Because this is a custom unit, the package also needs a legally usable Internet-sourced sound-design handoff for creature idle/ambient, movement, attack/impact, and death roles. Preserve source files, URLs, attribution, licensing evidence, checksums, synchronization points, and proposed runtime identifiers. Generated, synthesized, recorded, placeholder, or unlicensed audio is not acceptable.

## Counter companion and consumer handoff

Every listed subunit resolves the same shared `black_plague_rat` sprite/entity, so the package enumerates the exact installed vanilla counter definitions and DDS consumers discovered during inspection rather than inventing token names. The active `interface/subuniticons.gfx` and its referenced large/map counter DDS families were inspected alongside the matching skill-local vanilla reference families under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/`. The six subunit consumers, their exact runtime icon aliases, sampled vanilla-green palette evidence, and the bespoke `chaosx_icon_artist` handoff are recorded in the counter package manifest. The delivered DDS strips are installed at the parent-owned runtime paths; they are marked `needs_user_review` for live visual validation and do not use copied vanilla art.

## Explicit non-goals

Do not create a second Rat King model, a model per subtype, a model per brood, new country tags, a human-style weapon attachment, or a silent default sound package. Do not edit gameplay, localisation, GFX, entity, or sound-definition files inside the worker package; those remain parent-owned runtime wiring.

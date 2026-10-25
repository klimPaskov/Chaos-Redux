# Unit model rebuild workflow

Read this reference for explicitly requested custom land-unit repair or rebuild work using `.tools/3d_pipeline/review/`. Select only the stages required by that operation under the parent skill; an existing model does not automatically require replacement.
Every command runs from the mod root.
Each step lists the evidence to keep and the defects that step exists to catch.

## 1. Free triage of the shipped model

```bash
python .tools/3d_pipeline/review/review_cli.py triage --out <scratch>/triage --model <name>=gfx/models/units/<folder>
```

The worker imports the shipped `.mesh` and every `.anim`, renders sampled frames front and side, and records per-action ground contact in `triage_report.json` with a `sheet_<name>.png`.

Decide the route from the evidence, not from the file list:

- Count distinct actions. An entity that maps `defend`, `support_attack`, `retreat`, or `training` onto another action is aliasing and needs real actions.
- Look for rig breakage: knees bending backward, whole-body tilt in idle or move, legs crossing, spider-splayed deaths, meshes splitting into hundreds of loose pieces that separate in motion.
- Look for mesh tears (seam slivers showing the background) and flat untextured grey.
- Compare the triangle count with the project norm in `config/asset_profiles.json` (`triangle_range.working_triangle_target`).
- A provider operation that requires the original task ID cannot proceed without a verified ID. Recover it from the job records when possible; otherwise use authorized Blender repair/authoring. Generate replacement geometry only when the requested operation requires it, never merely to recover a missing provider ID or reset rig/action attempt limits.

## 2. Identity sources

Collect every picture the game already uses for the unit before writing a reference:

- the unit's leader or type portraits (`gfx/leaders/<event>/`), decision-category pictures, and counter art;
- renders of the current model, even when it is broken, because they carry silhouette features a portrait crops out (wings, tails, growths, carried gear):

```bash
python .tools/3d_pipeline/review/review_cli.py legacy-ref --folder gfx/models/units/<folder> --out <job>/refs/legacy_model/<name>_legacy
```

DDS portraits in DXGI formats PIL cannot read convert with `ffmpeg -i portrait.dds portrait.png`.

## 3. Reference image

Write one full-body reference per unit: front-facing symmetrical A-pose, arms about 30 degrees from the body, open empty hands clear of clothing, feet flat, whole figure with margin, soft studio light, dark neutral vignette background, no props or text.
Pass the portrait as image 1 (face and identity) and the legacy render as image 2 (body, silhouette, outfit), and say in the prompt what each contributes.
Reject a reference that looks generic next to its portrait: a clean face where the portrait shows decay, a closed mouth where it gapes, missing wings or growths.

Image generation may refuse gore on realistic human portraits, especially female subjects.
When that happens, drop the portrait image and describe its features in words, frame the subject as a fictional game creature design, or edit an accepted plainer reference in a second pass ("keep pose, body, clothing, framing; make the parasite larger…").
Record which fallback produced the accepted reference.

Compare before spending credits:

```bash
python .tools/3d_pipeline/review/review_cli.py compare --row <portrait> <legacy_front> <reference> --out <sheet.png>
```

## 4. Provider generation

Meshy 7 image-to-3D, `pose_mode: a-pose`, `should_remesh: true`, `target_polycount` at the profile's working target, `topology: triangle`, `enable_pbr: true`, formats `glb` and `fbx`.
Download the GLB with its textures, then review it against the portrait before rigging:

```bash
python .tools/3d_pipeline/review/review_cli.py glb-ref --glb <body.glb> --out <job>/evidence/<body> --face
```

Rig once with `meshy_rig` on the body task id.
Choose presets per role from `meshy_animation_library` and vary them between sibling units so they do not move identically.
Roles without a fitting preset (claw attacks, grabs, bites, casting, weapon strikes) use `meshy_text_to_motion` in `prime` mode with a unit-specific prompt that names the held item and which hand holds it.
Write the intake manifest (step 5) with `preset` or `motion_task` per role and no `task`, then queue every animate call at once; the tool writes each task id back into the manifest so a rerun never pays twice:

```bash
python .tools/3d_pipeline/review/provider_intake.py <manifest.json> --submit
```

Preset choice rules learned from rebuilds:

- A looping role (idle, move, retreat, defend, training) needs a preset that starts and ends standing. Seated presets ("Dozing Elderly"), falling presets ("Sliding Stumble"), and prone presets ("Crawl Backward") cannot loop.
- A death preset must fit the body's weight: acrobatic knock-downs that flip the legs over the head read wrong on heavy creatures; use collapses ("Fall Dead from Abdominal Injury", "Shot and Fall Backward").
- Weapon-holding presets ("Axe Breathe and Look Around", "Spear Walk", "Walk Backward with Sword & Shield", "Heavy Hammer Swing", "Two-handed Parry") give the empty-handed body arm poses that the separately generated item later fits.

A rejected role is replaced with a second small manifest holding one new role name (for example `death2`, `base_blend` = the last intake checkpoint), queued with `--submit`, imported with a normal run, and swapped in by `lab_finalize`'s `replace` map.
Record every task in the job's credit ledger with its cost and status, including rejected ones.

Held items (weapons, staffs, shields, tools) are never in the body.
Generate each from its own item-only reference (`refs/equipment/<item>/meshy_input.png`, a single object on a plain background with no hands) as its own Meshy 7 task at `target_polycount` about 4,000, and review it with `glb-ref` next to its reference before fitting.

## 5. Intake

Write `<job>/blender/working/<ns>/intake_manifest.json` (format in the tool docstring) with the rig task, `rig_glb`, a `prepare` block, and one entry per role, then run:

```bash
python .tools/3d_pipeline/review/provider_intake.py <manifest.json>
```

The tool downloads anything missing through the locked Meshy route, calibrates against the profile's vanilla reference mesh, writes one verified provenance receipt per role, and chains `import_animation_action` one sibling checkpoint per role.
It handles two adapter traps automatically:

- Meshy rig downloads contain a stray `Icosphere` helper; `prepare` excludes it, otherwise the footprint inflates to several units.
- Importing into a scene that already holds a rig renames the source armature (`Armature` → `Armature.002`) and prefixes the action id with the new name; the tool accepts the renamed id only when exactly one exposed action keeps the identical remainder and the file hash is unchanged.

## 6. Action review and grounding

```bash
python .tools/3d_pipeline/review/review_cli.py actions --blend <final intake checkpoint> --armature Armature.001 --mesh char1.001 --action <prefix>_<role> ... --out <evidence dir> --tag <tag> --humanoid
```

The report lists per-frame floor contact (`below_floor_frames`, `floating_frames`), hand reach peaks, foot plants, jaw opens, and fast spine drops.
Provider actions typically float between a few centimetres and several units and must be grounded.
Ground every role headless with `lab_finalize.py` (config format in its docstring; `replace` retires a rejected action for its replacement):

```bash
python .tools/3d_pipeline/review/review_cli.py blender --script lab_finalize.py --config <finalize.json>
```

It grounds each role (root keyed so the lowest vertex sits 4 mm up), repairs slot identifiers, clears NLA and drivers, and purges orphan materials and unused images, which the partition step requires.
The same helpers are available in a live Lab session through `import lab_actions as la` for hand edits.
Grounding flattens deliberate jumps; review the rendered sheet after grounding.
Re-author any role that reads as the wrong character (for example a boxer's guard on a zombie) with `la.pose_bone_directions`, keeping the provider legs, and review every change from at least two views.

## 6a. Extra appendages and non-provider creatures

Meshy rigs two arms and two legs.
Wings, a second pair of arms, tentacles, tails, and growths either follow the nearest provider bone (wings wrapping the head, a second arm pair weighted to `Hips`) or do not move.
`lab_limbs.py` handles them in four config-driven modes, run headless with `review_cli.py blender --script lab_limbs.py --config <cfg.json>` (formats in its docstring):

1. `survey` measures the rest pose. Probes report vertex counts, bounds, the bones a region currently follows (`weights`), per-axis histograms (`hist`), and connected pieces (`components`). Cutting the torso core away with `exclude` leaves each appendage as its own piece with a root, tip, and centreline to place joints on.
2. `rig` builds one bone chain per appendage from those joints, parented to a torso bone, and heat-weights only the selected vertices through a welded duplicate (provider meshes are triangle soup, which heat weighting rejects on the original). Where an appendage's root stays fused to a provider-weighted region, set `feather` (about 4% of rig height) so the seam blends instead of tearing.
3. `skeleton` builds a whole skeleton for a creature the provider cannot rig at all (quadrupeds), replacing any template rig, and heat-weights the full mesh.
4. `keys` keys chains per action from authored `[swing, lift]` angles (and `loc` offsets for body bob), carried through a torso bone so limbs follow the body; `tips` defines segment directions on rigs whose bones have stub tails; `create` makes new actions. Run its `floor` pass on every role afterwards: it re-keys a chain's first bone on frames where the chain sinks below the ground (deaths and slams).

Review every role with `review_cli.py actions` from front and side, and zoom into the appendage roots in the fastest poses for tearing.
Mirror the right side, but offset looping roles by half a cycle so the two sides do not move in lockstep.

## 6b. Held items

`lab_items.py` fits each item to its carrying bone, packs body and item textures into one atlas so the unit keeps one PDX material, joins the items into the body mesh weighted 1.0 to that bone, and renders and measures the result.
Write `<ns>/items_config.json` (format in the docstring) and iterate with `"review_only": true` until the close-ups look right, then run once more without it:

```bash
python .tools/3d_pipeline/review/review_cli.py blender --script lab_items.py --config <ns>/items_config.json
```

Fitting rules:

- Orientation is semantic: `head` is the item-local direction from the grip to the head (read it from the `glb-ref` renders, and flip it if the head ends up in the fist), `head_to` and `side_to` are the bone-local axes it follows. On Meshy rigs the grip axis through a closed fist is the hand bone's Z and the fingers run along Y, so shafts use `head_to: "-Z"` and `side_to: "X"`; shields on the forearm use the face normal as `head` with `head_to: "X"`.
- Meshy bone lengths are meaningless and the rig carries a 0.05 object scale, so `length` and `offset` are fractions of rig height. A palm grip sits at about `offset [0, 0.05, 0]`; a very large hand needs more.
- `grip_along` is measured from the butt (0) to the head (1); the grip centres on the real shaft cross-section.
- `contacts` reports the off-hand distance to the shaft per frame; a two-handed weapon whose off-hand drifts far from the shaft needs a live pose correction or an honest note in the handoff.
- `floor_items` runs the measured floor correction on the listed actions: on frames where any sampled item vertex sinks below the floor it re-keys only the carrying bone about its head until the lowest point rests at the clearance height. List every role; frames above the floor are untouched. A wrist that is itself at the floor (fists pounding the ground) cannot lift the item fully; report the residual.
- `aim_items` runs before the floor pass on firing roles: provider actions made for an empty body often hold the weapon raised or across the chest. Each frame re-keys only the carrying bone toward a level axis (`elevation_deg`), keeping the heading unless `heading` and `heading_weight` pull it toward the unit's facing (`[0, -1]`); `max_deg` clamps the wrist. Review the result, then time shots only on frames where the measured muzzle axis is level and forward.
- A pistol-grip weapon lays its barrel along the hand bone's Y (`head_to: "Y"`) with the grip hanging out of the fist (`side: "-Z"`, `side_to: "Z"` on Meshy rigs); iterate the Z offset in small steps until the grip sits inside the fist in the side close-up.
- The muzzle locator for a held firearm uses `head_bone_local` and the vanilla rifle muzzle orientation (weapon forward on the locator's local −Y, up on +Z); on a Meshy hand holding a weapon along +Y with the grip toward +Z that is `bone_local_rotation_xyzw [1, 0, 0, 0]`.
- Review the final `sheet_items.png` for every role, then use `textures_atlas/` as the texture source in step 7 and `--diffuse <atlas>/base_color.png` for later action reviews.

## 6c. Vehicles and variants

A provider vehicle arrives unrigged; build it with `lab_limbs` as for a creature:

1. `import` with `"glb"`, `yaw_deg` so it faces −Y, and `fit` to the vanilla precedent's length (the armoured car `US_mechanized_01.mesh` is about 7.35 long at entity scale 0.6).
2. `skeleton` with a non-deform `root` and a `chassis` bone carrying the whole mesh, then `rig` the moving parts: a wheel bone per wheel selected with `cylinders` (`a`, `b` on the axle, `r` just under the measured tyre radius so fenders stay on the chassis; survey the wheel boxes first), and a turret bone pointing forward.
3. `keys`: wheels use `{"spin": [[1, 0, 0], degrees]}` (a `dir` key cannot pass 180° and tears the wheel), keyed every 60° so interpolation turns the right way; key the chassis rotation (`dir [0, 0]`) and location in every action, or a pose from another action leaks in.
4. `locate` converts measured rest-world points into `author_locator` inputs. Vanilla vehicle locators are world-identity: `barrel` on the turret or weapon bone at the gun tip, `left_tracks` (+X) and `right_tracks` (−X) on the chassis at the rear wheels' ground contact.
5. `mark` re-tags a checkpoint for the partition step (PDX shader properties, mesh index, 30 fps) and is run on the last checkpoint before export.
6. `lab_finalize` with `"root": "root"` grounds the actions; ground contact is then 4 mm in every frame, which also cancels chassis bob.

A variant that shares a unit's mesh and actions (an elite company) gets its own diffuse from `texture_variant.py <spec.json>` (spec format in its docstring; it dyes low-saturation cloth toward a tint and keeps skin and the item cells), converted with `pdx_textures.py` under the variant's stem.
Register it as a second `pdxmesh` with the same mesh file and animations in a separate `<stem>_variants.gfx` (so rewiring the base unit does not overwrite it), and as an entity `clone` of the base entity that overrides only `pdxmesh`, as vanilla does for artillery variants.
A `clone` resolves only against entities already loaded: entity files load in file-name order, and vanilla never clones across files (0 of 208 clones), so clone only an entity defined earlier in the same file. To reuse a vanilla entity from another file (a rider, a weapon carrier), copy its `pdxmesh`, states, attachments and `scale` instead; a cross-file clone fails at startup with `Couldn't find parent clone entity`.
Render the variants side by side before converting; a near-black base needs `value_scale` above 1 for a dye to read at map scale.

## 7. Export

```bash
python .tools/3d_pipeline/review/pdx_textures.py --textures <body>_textures|<ns>/textures_atlas --out-dir <ns>/textures_pdx --stem <runtime stem>
python .tools/3d_pipeline/review/export_package.py --job <job> --partition-from <grounded or items checkpoint> --blend <new partition checkpoint> \
    --stem <runtime stem> --out export/<new version> --role <role>=<action> ... --install gfx/models/units/<folder> --textures <ns>/textures_pdx
```

`--partition-from` runs the adapter partition first; every attempt needs a new `--blend` name and a new `--out` version.

`export_package.py` flags any `.anim` under 10 KB: that is an action whose slot did not bind, which exports every bone frozen.
Read the exported node name and stream count from `export_report.json`; the `.gfx` needs one `meshsettings` block per stream with that node name and `index` 0…n−1.

## 8. Runtime wiring

`--install` copies the proven files into `gfx/models/units/<folder>/` with hash parity; delete files there that the new package no longer uses (old `.anim` names, an old `_spec.dds`).
Register the mesh and animations with:

```bash
python .tools/3d_pipeline/review/wire_unit.py --report <job>/export/<v>/export_report.json --stem <stem> --folder <folder> --title "<unit>" \
    [--retire <shared .gfx> --retire <shared entity .asset> --retire <shared animation .asset>]
```

`--retire` removes the unit's previous pdxmesh block, entity block, and animation lines from shared files when the rebuilt unit moves to its own files, preserving the files' encoding and line endings.
Author `gfx/entities/<stem>.asset` by hand, keeping the entity name the `sub_units` sprite resolves to (for example `riverborn_entity` for `sprite = riverborn`).
A mesh built taller with `prepare.height_scale` keeps the vanilla entity `scale`; the height difference is the point.
New sourced voices go through `sound_pack.py <spec.json>` (trim, fade, peak normalise, mono 44.1 kHz, `.asset` with the Effects category, and a receipts file; spec format in its docstring); a unit that already owns licensed sound effects reuses them.
Time sound and particle events from the phase report: `time = (frame − first frame) / fps`, one event per measured contact, plant, or impact.
Point `sub_units` `sprite` at the entity (`sprite = x` resolves `x_entity`), and check the counter set still shows a unique silhouette.

## Gotchas collected from rebuilds

| Symptom | Cause | Fix |
|---|---|---|
| Export fails over 65,535 vertices | one stream too large | partition, and reduce to the profile target when far above it |
| `.anim` of a few KB, frozen in game | action slot identifier differs from `OB<rig name>` | `la.fix_slot_identifiers` |
| Partition error "driver/NLA proof scenes" | NLA track left by action swaps | `la.clear_nla_and_drivers()` |
| Partition error "texture must be packed or inside the job" | leftover calibration images | remove unused images outside the job |
| Partition error "evidence already exists" | a failed attempt used the name | use a new checkpoint name |
| MCP `execute_blender_code` returns no response | long scripts time out the bridge | run read-only work through `review_cli.py` (background Blender) |
| Provider body looks generic | reference drifted from the portrait | regenerate the reference from the portrait before paying for geometry |
| Partition error "image identities" | orphan materials still hold images | `lab_finalize` purges orphan materials first, then images no material uses; never bind preview textures into a checkpoint |
| Partition error "every source material slot must be a nonempty PDX material" | a mesh join left empty slots | keep exactly one material slot (`lab_items` does this) |
| Renders from a worker never appear | Blender resolves relative render paths against the unsaved blend | pass absolute paths (`review_cli` absolutises them) |
| Parallel `glb-ref` runs crash with an access violation | several EEVEE renders at once | run renders one after another |
| Winged, tailed, or caped anatomy follows the arms | Meshy's humanoid rig has no bones for it | add bones live, weight a welded duplicate with heat weighting, map weights back by position, author keys as absolute directions through the spine pose |
| A giant or heavy creature looks infantry-sized | calibrated to the vanilla source height | `prepare.height_scale` (about 1.15–1.3) in the intake manifest |
| Weapon sinks through the ground in slams and deaths | provider motion was authored empty-handed | `lab_items` `floor_items` on every role |
| Triage shows identical frame ranges and heights across actions | the importer writes each `.anim` into the rig's bound action | fixed in `blender_review` triage (unbind and reset before each import); re-triage anything judged with the old tool |
| Render save fails with "cannot save" on long job paths | Windows 260-character path limit | review tools drop the shared action prefix from file names |
| Adapter `author_locator` fails a round-trip check of a few 1e-4 | Meshy armature units are about 20x world units | the adapter tolerance is relative to coordinate size (lock updated) |
| A weapon or nozzle needs a particle node | the item is joined into the body mesh | `lab_items` reports `head_bone_local`; pass it to `author_locator` and orient the locator like the vanilla precedent (flame-tank `flamethrower` emits along local +Z, local +Y up) |
| Appendage root tears into spikes in fast poses | the root stays weighted to a provider bone while the rest follows the new chain | re-rig with `feather` |
| A quadruped or creature never moves properly | it was skinned to an unrelated template rig (a cave monster on an elephant rig with howdah and rider bones) | `lab_limbs` `skeleton` on the existing mesh, then author gaits with `keys` |
| Wheel spin tears the mesh or snaps backwards | `dir` keys take the shortest rotation and cannot pass 180° | `spin` keys about the axle in 60° steps; weight each wheel rigidly inside a measured cylinder |
| An action shows another action's pose (a tilted idle) | the bone has no key in that action, so the last evaluated pose stays | key every animated bone in every action, even at rest values |
| Grounding lifts a vehicle or creature by many units mid-action | a sparse-keyed root: each new key shifted the next frame's interpolated pose before its offset was added | fixed in `lab_actions.ground_action` (offsets apply to the pose captured before keying) |
| Entity sounds drift late against the motion | a factory-startup blend exports at 24 fps while the pipeline times events at 30 | `lab_limbs` `import` and `mark` set the scene to 30 fps; check `fps` in the exported `.txt` dump |
| Partition error "nonempty PDX material" on a glTF-imported model | the material lacks io_pdx's `shader` property | `lab_limbs` `mark` |
| The MCP adapter rejects a new job with the default job root | the running server read its config before the job override was added | call the adapter through `provider_intake.adapter(...)`, which starts a fresh server |
| Review renders silently missing | the tag plus action name pushes the path past 260 characters | short `--tag` and `--out` names |
| Firing role never points the weapon forward | the provider motion was authored empty-handed | `lab_items` `aim_items`, then time shots on measured aim frames |

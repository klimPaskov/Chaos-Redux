# Unit model rebuild workflow

This is the step-by-step route for rebuilding an existing custom land-unit model, or building a new provider-eligible biped, with the repository tools in `.tools/3d_pipeline/review/`.
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
- A model whose provider task ids were never recorded cannot be rigged by the provider; it needs a fresh body.

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
Roles without a fitting preset (claw attacks, grabs, bites, casting) use `meshy_text_to_motion` in `prime` mode with a unit-specific prompt, applied to the rig through `meshy_animate(motion_task_id=…)`.
Record every task in the job's credit ledger with its cost and status.

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
In the live Lab session:

```python
import sys; sys.path.insert(0, r"<mod>/.tools/3d_pipeline/review"); import lab_actions as la
la.ground_action(rig, [mesh], "<action>", "<action>_grounded")   # then swap names
la.fix_slot_identifiers(rig, "<prefix>_")                        # every imported action needs it
la.clear_nla_and_drivers()                                        # partition refuses NLA/driver scenes
```

Grounding flattens deliberate jumps; review the rendered sheet after grounding.
Re-author any role that reads as the wrong character (for example a boxer's guard on a zombie) with `la.pose_bone_directions`, keeping the provider legs, and review every change from at least two views.

## 7. Export

Partition with the adapter (`partition_skeletal_mesh_export_batches`, a new checkpoint name per attempt, textures inside the job or packed), then:

```bash
python .tools/3d_pipeline/review/pdx_textures.py --textures <body>_textures --out-dir <ns>/textures_pdx --stem <runtime stem>
python .tools/3d_pipeline/review/export_package.py --job <job> --blend <partition checkpoint> --stem <runtime stem> --out export/<version> --role <role>=<action> ...
```

`export_package.py` flags any `.anim` under 10 KB: that is an action whose slot did not bind, which exports every bone frozen.
Read the exported node name and stream count from `export_report.json`; the `.gfx` needs one `meshsettings` block per stream with that node name and `index` 0…n−1.

## 8. Runtime wiring

Copy the proven files into `gfx/models/units/<folder>/`, record hash parity, and keep the `.gfx` animation ids, `animation_<stem>.asset` file names, and the entity states aligned.
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

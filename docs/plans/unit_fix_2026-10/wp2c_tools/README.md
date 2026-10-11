# Unit-fix working scripts, second pass (11 Oct 2026)

These scripts produced the finger rigs and grips of the four Event 014 cannibals, the tentacle chains and weight repairs of the zombie units, and the Africa action repairs.
They are archived because `.tmp/` is ignored; the files carry the placeholder `<mod root>` where the absolute repository path was and are not part of the shared toolchain.
They run inside the Blender Lab socket (`run.py <script> '<json cfg>'` injects `CFG`), except the adapter drivers (`export_*`, `mesh_only.py`, `install_anims.py`, `remap_events.py`, `make_policy2.py`).
The reusable gate change that came out of this work (finger leaf bones are exempt from the per-frame world translation limit, their rotation limits still apply) lives in `.tools/3d_pipeline/adapter/animation_delivery_checks.py` with a regression test.

## Cannibal grips (WP2)

Order for one unit (`configs/cfg_<unit>.json`, run `python chain.py <cfg>`):

1. `fingers_build.py` (library `fingers.py`) finds the four finger tips and the thumb of each hand mesh by component growth along the hand axis, builds twelve bones per hand (thumb 2, index 3, middle 3, ring 2, pinky 2) from slice centroids, skins the finger segments with smooth hat weights over the hand's own weights and saves `<tag>_01_fingers.blend`.
   The skeleton is 24 + 24 = 48 bones, inside the 50-bone shader array.
2. `unit_stage.py` computes the grip frame of each hand (diagonal grip axis, palm normal, palm surface), moves the item rigidly onto the palm side, counter-rotates the hand rotation keys of every action so the item keeps its world orientation, and records the off-hand stations and shaft radii (`regrip.py`).
3. `scav_post.py` smooths over-limit windows, closes loops, keeps the items above the floor (arm lift for two-hand items, tilt about the wrist otherwise) and re-reaches the off hand onto the shaft.
4. `finger_keys.py` curls every finger segment onto the shaft by contact against the item surface (`grip.py`) and keys all twelve bones on every frame of every action.
5. `export_unit.sh` / `mesh_only.py` / `install_anims.py` export through the adapter, run the delivery gate on the exported bytes with reimport proofs, and install with hash parity.

## Zombie units (WP3)

- `stretch.py`, `fix_stretch.py`, `stretch_scan.py` measure the edges that grow more than 0.3 units in representative poses and smooth the skin weights of the region around them until the counts fall under the targets (skeleton and actions unchanged, `mesh_only.py` exports and proves the mesh).
- `tentacles.py`, `para_rig.py`, `para_whip.py` build the parasitic bundle chains (tube vertices found by flesh colour and measured wall thickness, bundles by direction from the root hub) and key the follow-through; `fix_stretch.py` then blends the weights.

## Africa actions (WP1)

- `mk_working.py` assembles a working scene from the installed mesh and the eight reimport proof blends, `wp1_doctor.py` applies the authored layers and runs the gate pass (sign continuity, speed-limited re-timing in `regrip.speed_retime`, deglitch, loop seal, floor), `export_queue.sh` / `export_role.sh` export the actions with the installed mesh, and `remap_events.py` / `compose_fmap.py` carry the entity event times through the re-timing.

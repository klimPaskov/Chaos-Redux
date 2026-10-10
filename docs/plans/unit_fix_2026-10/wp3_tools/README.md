# WP3 unit-fix working scripts (11 Oct 2026)

These are the scripts that rebuilt the eight zombie units.
They are archived here because `.tmp/` is ignored; they carry absolute paths (`C:/Users/klimp/.../chaos_redux`) that a reuse must edit, and they target the 24-bone Meshy humanoid rig (the demonic unit adds 20 wing bones).
Nothing here is part of the shared toolchain; the reusable parts were promoted to `.tools/3d_pipeline/` (`review/anim_signs.py`, the recalibrated `animation_delivery_checks.role_motion_limits`, and the `matte_cloth` and `dry_skin` texture classes).

Order of use for one unit (`<job>` = the job folder under `docs/assets/002_zombie_outbreak/models_3d/`):

1. Start the Blender Lab socket (see the skill, `Hard start gates`) and take the shared Blender lock.
2. `prep_bake.sh <job> <21*_export_batches.blend> <provider texture folder>` runs `prep_uv.py` in the Lab (weld at 0.5 mm, drop the smallest face on every over-shared edge, close boundary loops, fix mis-wound faces, collapse stubborn conflict edges, flip inside-out closed shells, triangulate, planar-cluster unwrap with shelf packing, blender pack) and `rebake.py` (barycentric re-projection of the provider base colour, roughness, metallic and normal through the old Meshy UV onto the new UV) and `grade.py` (per-class tone, vanilla-calibrated specular through `textures/conventions.py`, PDX RRxG normal).
3. `chain_model.sh <job> <folder> <stem> <prefix> <tag> <actions cfg json> [stagger_move]` runs `actions_model.py` in the Lab (quaternion sign continuity, local pose smoothing windows until every joint step is inside the role limits, loop-seam easing, authored additive layers, hold-and-layer new actions, thigh clamp, grounding), `tex_deliver.py` (hash-bound texture batch through `textures/cli.py`), `make_policy.py` (hash-bound action policy) and `export_model.py` (adapter mesh and action export, `anim_signs.py` repair, offline re-gate of the final bytes, reimport proof per role).
4. `install_model.py <job> <folder> <stem> <export dir> <texture tag>` refuses unless all eight roles passed, then installs textures through the repository CAS CLI and copies mesh and animations with hash parity.
5. Commit with `commit.py` (temporary index from HEAD, compare-and-swap ref update) or the shared-git-commit skill.

`configs/` holds the grade and action configurations used for each unit; the authored layers are explicit `[frame, degrees]` key lists per bone and local axis, reviewed on rendered contact sheets.

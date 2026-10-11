# WP2 regeneration working scripts (11 Oct 2026)

These scripts rebuilt the four Event 014 cannibal units after the original Meshy tasks turned out to be gone.
They are archived because `.tmp/` is ignored; the Python files carry the placeholder `<mod root>` where the absolute repository path was, and the shell scripts still carry it literally.
They build on the WP3 scripts in `../wp3_tools/` (same 24-bone Meshy humanoid rig) and are not part of the shared toolchain.

Order of use for one unit (`<job>` under `docs/assets/014_cannibalism/models_3d/`):

1. Meshy: body image-to-3D, rig, eight preset animate tasks and one image-to-3D per item, each downloaded immediately (Meshy assets expire after three days).
   Provider intake: `provider_intake.py` with `blender/working/wp2b/intake_manifest.json` (prepare, calibrate, eight action imports).
2. `stage1.sh`: `finalize.py` (ground), `partition.py` (adapter partition), `prep_uv.py` (weld, repair, planar unwrap), `rebake.py` and `grade.py` (provider base colour, roughness, metallic and normal re-projected and graded), `actions_model.py` (sign continuity, smoothing, seams).
3. Items: `item_prep.py` (weld, unwrap), `rebake.py` and `grade_item.py`, `items_attach.py` (fit to the carrying bone, rigid weights, own material). Two-hand items then go through `holdpass.py`: the carrying hand is turned about the wrist so the item axis follows the measured hand-to-hand line, and the off arm is reached onto the shaft with a two-bone solve.
4. `chain_run.py <config>` runs `post_hold.py` (remaining over-limit steps), `finish_floor.py` (item floor clearance within the hold tolerance), `seal.py` (loop closure and grounding), `refresh.py` (off-hand contact restore).
5. `make_policy.py`, `export_model.py` (adapter export, sign repair, final-byte gate, reimport proof), `tex_deliver.py`, `install_model.py`, `wire2.py` (meshsettings and event times), `commit.py`.

`evidence/` holds each unit's per-frame hand-to-shaft and floor measurements, the exported-byte gate summary and the provider lineage; `configs/` holds the grade, chain and wiring configurations and the task id table.
Known gap: a long two-hand polearm held low by a preset made for a short axe cannot be lifted clear of the floor without moving the off hand off the shaft; `finish_floor.py` keeps the hold and reports the remaining penetration.

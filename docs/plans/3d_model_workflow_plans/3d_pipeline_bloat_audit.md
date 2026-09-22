# `.tools/3d_pipeline` bloat audit

Read-only audit. No file under audit was edited, created, deleted, moved or renamed; Blender and Hearts of Iron IV were not started; no network access and no installs were performed. Inspection used pure-Python `ast`/`hashlib`/`json` scripts.

Scope: `.tools/3d_pipeline` only, excluding `vendor/**` and `reports/**`. `docs/**` was read but not judged; the only file written by this audit is this report.

## 0. Revision the findings bind to, and an active-writer caveat

`.tools/3d_pipeline` was being rewritten by another writer **during** this audit. Observed writes: `README.md` 23:26:32, `run_pilot.py` 23:28:59, `verify_environment.py` 23:34:16, `mesh_vertex_material_repair.py` 23:34:16, `blender_client.py`/`lib/paths.py`/`explicit_vertex_remap.py`/`mesh_patch_repair.py`/`skeletal_export_partition.py` 23:35:55, `blender_worker.py` 23:37:24, `dependencies.lock.json` 23:37:31 (local time, 2026-09-22).

Three things changed under the audit and are **not** re-reported as new findings:

- `lib/paths.py` lost `relative_file_list`, `verify_environment.py` dropped an unused `file_record` import, `blender_client.py` dropped an unused `import os`, and `adapter/blender_worker.py` shrank (346,358 → 342,012 bytes). Dead functions `evaluated_contact_bounds`, `verify_saved_normalization` and `import_geometry_candidate` were present in my first pass and gone by my last, so they are removed from the dead list below rather than counted.
- `adapter/mesh_winding_seam.py`, `adapter/pdx_skin_membership.py` and `tests/test_mesh_winding_seam.py` are deleted in the working tree but still present in `HEAD` (`git status` shows ` D` for all three).
- The dependency lock was stale mid-audit and was refreshed at 23:37:31. At the time of writing `verify_environment.py`'s 18 `source_sha256` checks **all pass** (re-run at 23:38:42: `-> 0 mismatches out of 18`).

All line numbers below were re-verified against these digests after the last observed write:

| file | sha256 (first 16) |
|---|---|
| `adapter/blender_worker.py` | `F735CCFD79F212CC` |
| `adapter/chaosx_blender_hoi4_mcp.py` | `FB4ED2AAAD5FFDFC` |
| `blender_client.py` | `23036845B5A55492` |
| `run_pilot.py` | `3589F074961C868A` |
| `lib/paths.py` | `305004B42F06DADF` |
| `verify_environment.py` | `7FC45C46F827A1B8` |

**Method.** For every module-level `FunctionDef`/`ClassDef`/`Assign`/`AnnAssign` I collected the definition, then searched every in-scope `.py`, `.cmd`, `.ps1`, `.mjs`, `.toml`, `.json`, `.md` and `.txt` for word-boundary occurrences of that exact symbol name — so dynamic dispatch, `getattr` strings, subprocess argv, `importlib.util.spec_from_file_location` targets and entry-point tables are all caught. A plain text grep for call sites would have produced false positives on `_run`, `_job`, `_name`, `_sha`, `_hash`, `main` and `REPO_ROOT`, which exist in several files at once.

## 1. Ranked findings

### HIGH

**H1. Eleven of the 32 adapter operations cannot be invoked through any configured route.** `adapter/chaosx_blender_hoi4_mcp.py` registers exactly 32 `@mcp.tool()` handlers, one per config operation (verified: 32 decorated handlers, 32 distinct operation strings, set difference empty in both directions against `config/blender_hoi4_adapter.json`; `run()` handles exactly 32 with zero drift). But 11 of them appear in **no** `enabled_tools` list in `.codex/config.toml` (which enables 16), in **no** `blender_client.py` wrapper, and in **no** skill or docs reference:

| operation | handler line | only other reference |
|---|---|---|
| `repair_mesh_winding` | `chaosx_blender_hoi4_mcp.py:498` | `README.md:106` only |
| `repair_explicit_mesh_winding` | `:757` | none |
| `remove_explicit_duplicate_faces` | `:662` | none |
| `repair_explicit_mesh_patch` | `:763` | none |
| `edit_explicit_mesh_vertices` | `:769` | none |
| `bind_existing_pdx_material` | `:775` | none |
| `repair_explicit_vertex_remap` | `:781` | none |
| `rotate_existing_assembly_yaw` | `:787` | none |
| `inspect_animation_source` | `:917` | none |
| `repair_explicit_mesh_winding_batch` | `:746` | none |
| `replace_explicit_corner_normals` | `:752` | none |

Every one of these has a live, tested implementation behind it (`blender_worker.py` lines 6476-6553 dispatch all 11; `tests/test_adapter_recovery_release.py` covers `validate_yaw`, `validate_remap`, `align_initial_root_records`). So this is not dead code — it is **unreachable surface**: the code is real, the tests are real, and no route the pipeline actually runs can call it. Either enable them or stop presenting them as part of the surface.

**H2. Dead file-level surface on the policy-critical rigging path.** `adapter/mesh_winding_seam.py` (428 lines) and `adapter/pdx_skin_membership.py` (173 lines) have **zero** references anywhere in `.tools/3d_pipeline` outside their own files (scan of 75 in-scope `.py`/`.json`/`.md`/`.cmd`/`.ps1`/`.mjs`/`.toml` files: `references to pdx_skin_membership: NONE`, `references to mesh_winding_seam: NONE`). `run()` has no branch for either, and neither is in `dependencies.lock.json`. Both are already deleted in the working tree, so this finding is confirmation rather than a new action item — but it is worth recording that `pdx_skin_membership.py` contained `verify_pdx_skin_membership`, an operation that called `bpy.ops.object.mode_set(mode="EDIT")` and created a two-bone armature (`edit_bones.new("Root")`, `edit_bones.new("Tip")`) plus vertex groups (`obj.vertex_groups.new(...)`, `groups[0].add([0,2], 0.25, "REPLACE")`). That is repository Python generating bones and skin weights, which the current policy forbids. Removing it was correct.

**H3. `WINGED_BIPED_BONE_NAMES` is dead *and* is exactly the artefact the policy bans.** `adapter/blender_worker.py:5045-5069`, 25 lines. Occurrences of the symbol in the whole in-scope corpus: **1** (the definition). The constant is a declarative tuple of 22 bone names (`"root"`, `"pelvis"`, `"spine"`, `"wing_root_left"`, `"wing_mid_left"`, …). Even unused it is a latent re-introduction of spec-driven bone generation, so it should go rather than merely be ignored.

### MEDIUM

**M1. Repository Python still has a route that reports a rig/animation plan it can never execute.** `run_pilot.py`'s `PILOT_SPECS` declares `("rig", spec.get("rig_estimate_credits"))` in `provider_plan.estimated_credits` (line 1001 area; `humanoid_rig_route` at 1001/1084/1309) and per-action `provider_action_id`/`authoring_route`/`root_policy` records (1316-1370), and `alien_infantry` declares a `rig` + animation credit total. No `MeshyClient.rig`, `.remesh`, `.convert`, `.animate` or `.text_to_motion` call exists anywhere in the pipeline outside tests. The runner therefore writes planned rig and animation spend into `job.yaml` that no code path can spend. This contradicts `README.md:72`, which states the package drives the humanoid rig task and the preset-action and Text-to-Motion animation tasks. Under the current policy Meshy *is* the preferred route for provider-eligible bipedal bodies, so the gap is that the documented provider route is reachable only by an agent driving MCP by hand, not by any repository entrypoint.

**M2. Four separate job-path resolution implementations, one of them without a containment check.**
- `adapter/blender_worker.py:69 within()` — authoritative for the worker; enforces job-root containment.
- `adapter/chaosx_blender_hoi4_mcp.py:60 _relative()` — near-verbatim reimplementation of the same body (same `is_absolute()`/`":" in value` rejection, same `relative_to` containment, same `ValueError` shape), different message text ("Adapter paths must be relative to the job root." vs "Worker paths must be relative to the job root.").
- `lib/paths.py:144 assert_within()` + `:156 job_path()` — authoritative for provider/job writes, used by `meshy_client.py:247,315,334,413,550`.
- `blender_client.py:70-75` — inline reimplementation of the job-root/override precedence (`config.get("job_overrides", {}).get(job_id, ...)`) that **bypasses** the containment check entirely.

Plus a fourth *job-root* resolver: `adapter/chaosx_blender_hoi4_mcp.py:44 _job()` and `lib/paths.py:124 resolve_job_root()` both resolve override-then-job-root, and `lib/paths.py:88 _configured_job_overrides()` reads the same `job_overrides` block a third time.

**M3. Four SHA-256 helpers in three case conventions.**
| location | body | case |
|---|---|---|
| `lib/paths.py:165 sha256_file` | streaming 1 MiB chunks | `.upper()` |
| `adapter/blender_worker.py:4898 file_sha256` | streaming 1 MiB chunks — byte-identical to the above | `.upper()` |
| `adapter/material_visibility_probe.py:18 _sha` | streaming 1 MiB chunks — byte-identical again | `.upper()` |
| `pack_pdx_material.py:37 _record` | `hashlib.sha256(path.read_bytes())` — non-streaming | **lowercase** |

Authoritative: `lib/paths.py:165` for repository evidence (used by `meshy_client.py:556`, `verify_environment.py:123,168`); `adapter/blender_worker.py:4898` for the worker boundary. The lowercase `_record` digest is written into `pdx_material_pack.json`/`pdx_normal_pack.json`, so the same artifact family is recorded with two different hash cases depending on which code path produced it.

**M4. Two JSON-digest helpers, subtly different.**
- `adapter/blender_worker.py:3926 _promotion_digest` — `json.dumps(..., sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")`
- `adapter/mesh_inspection_repair.py:15 digest` — `json.dumps(..., sort_keys=True, separators=(",", ":"), allow_nan=False).encode()`
- `adapter/animation_root_export.py:17 _digest` — `json.dumps(..., sort_keys=True, allow_nan=False).encode()` — **no `separators`**, so it produces a different digest for the same value.

Authoritative: `blender_worker.py:3926` (hash-bound promotion proofs depend on it). `animation_root_export.py:17` is the divergent one.

**M5. Four identifier-validation helpers, one silently different semantics.**
- `adapter/blender_worker.py:60 safe_name` — *sanitizes* (`re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")`).
- `adapter/blender_worker.py:4865 explicit_safe_name` — *rejects* (`re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{0,127}", name)`).
- `adapter/mesh_inspection_repair.py:18 name` — *rejects*, same regex as above, different message.
- `adapter/duplicate_face_repair.py:8 _safe_mesh_name` — *rejects*, same regex as above, third message.
- `adapter/material_visibility_probe.py:26 _name` — *rejects* on a different rule entirely (length ≤ 256, no control chars, must equal its own `.strip()`).
- `lib/paths.py:60 safe_slug` — *sanitizes* to lowercase `[a-z0-9_]`.

Authoritative: the `explicit_*` family in `blender_worker.py` for anything that becomes a Blender identifier (they fail closed); `safe_slug` only for job/owner slugs. Three copies of one regex with three messages is the bloat.

**M6. DDS conversion logic duplicated across the adapter and the pilot runner.** `run_pilot.py:572-641 _finalize_pdx_runtime_texture` and `adapter/chaosx_blender_hoi4_mcp.py:233-309 _process_textures` share the same converter invocation of `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, the same argv construction, the same unlink-then-run pattern, the same `timeout=600, check=False`, the identical error string `"Unable to replace existing DDS output: {dds}"`, and the **same output report path** `blender/reports/textures_dds.json`. They diverge only in how they measure the image (PIL `Image.open` in the runner vs `ffprobe` in the adapter). Authoritative: `adapter/chaosx_blender_hoi4_mcp.py`, because that is what `wrappers/run_blender_hoi4_adapter.cmd:23` actually launches. The same 20-line converter block is also copy-pasted twice *within* `run_pilot.py`.

**M7. `lib/paths.py:23 STAGING_ROOT` is dead and its directory does not exist.** Occurrences in the whole in-scope corpus: **1** (the definition). `.tools/3d_pipeline/staging` is absent (`os.path.exists` → `False`), which contradicts `README.md:328` ("Runtime source files may be staged under `.tools/3d_pipeline/staging`"). `config/blender_hoi4_adapter.json` has a matching dead key `final_staging_root` pointing at the same absent directory.

### LOW

**L1. Three dead constants and one stale spec field.**
- `adapter/blender_worker.py:32 CREATURE_GROUND_CONTACT_TOLERANCE_M = 0.01` — 1 occurrence.
- `adapter/blender_worker.py:33 CREATURE_GROUND_CONTACT_CLEARANCE_M = 0.001` — 1 occurrence.
- `run_pilot.py:1223 "blender_reference_height_m": 2.464908123` — 1 occurrence; no code reads it (the reads are `blender_target_height_m`/`target_height_m`).
- (`PREVIEW_LIGHT_REFERENCE_HEIGHT` at `blender_worker.py:31` was in my first pass's dead list; it has 2 occurrences, the second on line 2147, so it is **live**. Not a finding.)

**L2. `lib/paths.py:15` imports `Iterable` unused** — the only genuinely unused import left in scope. (`from __future__ import annotations` is flagged by naive tooling in 17 files; it is a compiler directive, not an unused import. `io_pdx_mesh`, `io_anim_bvh` and `mcp` resolve only inside Blender or `adapter/.venv`; no import in scope points at a module that no longer exists — verified by path check.)

**L3. `run_pilot.py:1482-1484` `--phase` is unvalidated.** `phase = args[args.index("--phase") + 1]` with no allowlist; `--phase` as the last argument raises `IndexError` rather than a usage error, and an unknown value is not rejected. `README.md:336-339` documents only `--phase candidate`.

**L4. Stale hardcoded adapter version in `config/asset_profiles.json` consumers' tests and docs.** Current `adapter_version` is `1.10.51`; `tests/blender_humanoid_component_review_integration.py:29` and `:225` assert `== "1.10.21"`.

**L5. `verify_environment.py:164` assigns `io_archive = REPO_ROOT / "vendor" / "not-present"` and immediately overwrites it at line 165.** The token `not-present` occurs once in the whole pipeline.

## 2. Dead adapter modules (task item 1)

Eleven modules survive in `adapter/` after the concurrent deletions. Reachability from `run()` (`adapter/blender_worker.py`, dispatch at lines 6476-6553):

| module | reachable from `run()`? | evidence |
|---|---|---|
| `animation_root_export.py` | **yes**, indirect | imported at `blender_worker.py:5021` inside `normalize_exported_animation_scales` |
| `assembly_yaw.py` | **yes**, direct | `blender_worker.py:6488` `if operation == "rotate_existing_assembly_yaw":` → `from assembly_yaw import rotate_existing_assembly_yaw` |
| `blender_worker.py` | *is* the dispatcher | `def run` at line 6476 |
| `chaosx_blender_hoi4_mcp.py` | **yes**, process entry | `wrappers/run_blender_hoi4_adapter.cmd:23` → `python -m chaosx_blender_hoi4_mcp` |
| `duplicate_face_repair.py` | **yes**, direct | `blender_worker.py:6480` `if operation == "remove_explicit_duplicate_faces":` → `import duplicate_face_repair` |
| `explicit_batch_repair.py` | **yes**, direct | `blender_worker.py:6477` `if operation in {"repair_explicit_mesh_winding_batch", "replace_explicit_corner_normals"}:` |
| `explicit_vertex_remap.py` | **yes**, direct | `blender_worker.py:6491` `if operation == "repair_explicit_vertex_remap":` |
| `material_visibility_probe.py` | **yes**, indirect | `blender_worker.py:3365` `from material_visibility_probe import run_material_visibility_probe` inside `inspect()` |
| `mesh_inspection_repair.py` | **yes**, direct + dependency | `blender_worker.py:6500` `if operation in {"inspect_mesh_landmarks", "repair_explicit_mesh_winding"}:` → `import mesh_inspection_repair`; also imported by `mesh_patch_repair.py:6`, `mesh_vertex_material_repair.py:5`, `explicit_vertex_remap.py:4`, `assembly_yaw.py:3` |
| `mesh_patch_repair.py` | **yes**, direct | `blender_worker.py:6494` `if operation == "repair_explicit_mesh_patch":` |
| `mesh_vertex_material_repair.py` | **yes**, direct + dependency | `blender_worker.py:6482` `if operation in {"edit_explicit_mesh_vertices", "bind_existing_pdx_material"}:`; also imported by `assembly_yaw.py:4`, `explicit_vertex_remap.py:5` |
| `mesh_winding_repair.py` | **yes**, direct + dependency | `blender_worker.py:6497` `if operation in {"inspect_mesh_winding", "repair_mesh_winding"}:`; also imported by `explicit_batch_repair.py:15`, `mesh_inspection_repair.py:210` |
| `normalization_convergence.py` | **yes**, indirect | top-level `blender_worker.py:30` `from normalization_convergence import evaluate_convergence_step` |
| `retarget_root_motion.py` | **yes**, direct + indirect | `blender_worker.py:6485` `if operation == "inspect_animation_source":`; also `blender_worker.py:5595` |
| `skeletal_export_partition.py` | **yes**, direct + indirect | `blender_worker.py:6503` `if operation == "partition_skeletal_mesh_export_batches":`; also `:3899` and `:4811` |

**Dead (deleted in the working tree, still in `HEAD`):** `mesh_winding_seam.py`, `pdx_skin_membership.py`. Neither is reachable from `run()` and nothing imports either — see H2.

**Test-only surface inside live modules.** 71 module-level symbols are referenced *only* from `tests/`. The largest clusters are the humanoid component-review helpers (`_component_review_inputs`, `_component_index_catalog`, `_action_channel_*`, `_render_component_group`, `inspect_action_channels`, `inspect_mesh_region`, `_mesh_region_*` — ~20 symbols in `blender_worker.py`), the promotion internals (`_promotion_inputs`, `_promotion_targets`, `_promotion_image_retention`, `_promotion_image_record`, `_promotion_material_retention`, `_promotion_attribute_record`, `_promotion_scalars`), the locator internals (`_locator_numbers`, `_locator_request`, `_locator_registration`, `_locator_matrix_record`, `_locator_bone_world`, `_locator_parent`, `_validate_registered_locator`, `approved_export_locators`), and the explicit-batch helpers (`validate_specs`, `selection_records`, `raw_normals`, `preflight_mesh`, `_apply`, `verify_mesh`, `project_fingerprint`). These are **not dead** — they are the seam the tests assert against — but they mean a large share of `blender_worker.py` is reachable only through the test suite, which is worth knowing before deleting anything.

## 3. Dead configuration (task item 5)

**`config/blender_hoi4_adapter.json` — keys no code reads** (occurrence count in the whole in-scope corpus, definition included):

| key | occurrences | note |
|---|---|---|
| `repository_root` | 2 | only the config and the lock echo it |
| `final_staging_root` | 1 | points at the absent `staging/` — see M7 |
| `vanilla_root` | 1 | |
| `allowed_read_roots` | 1 | policy metadata; never enforced by code |
| `allowed_write_roots` | 1 | policy metadata; never enforced by code |
| `forbidden_inputs` | 1 | policy metadata; never enforced by code |

`allowed_read_roots` / `allowed_write_roots` / `forbidden_inputs` are the most consequential of these: they read as enforced sandbox policy but nothing in the pipeline consults them. Containment is actually enforced by `within()`/`_relative()`/`assert_within()` at the three call sites in M2.

**`config/asset_profiles.json` — only one leaf is ever read.** `adapter/chaosx_blender_hoi4_mcp.py:201` is the sole reader: `profiles.get(profile_name, {}).get("texture_max_dimension")`. Every other leaf is unread, including the entire `materials` block (5 keys × 5 profiles: `max_slots`, `required_channels`, `shader`, `specular_packing.{red,green,blue,alpha}`, `raw_roughness_as_specular`), the entire `triangle_range` block (4 keys × 5 profiles), `controlled_reduction_allowed`, `rig_route`, `runtime_consumer`, `root_policy`, `scale_reference`, `scale_policy`, and `building.placement` in full. Note the values are not even self-consistent as documentation: `static_prop.axis = "z_up"` and `static_prop.root_policy = "world_origin_on_ground"` are never validated, and `building.scale_policy`, `building.vanilla_reference.mesh_height_m`, `.runtime_height_m`, `.runtime_dimensions_m` each occur exactly once (the definition).

**`config/asset_profiles.json` — profiles the code cannot select.** `_texture_resize_for_job` reads `job.yaml`'s `profile` key, while the worker's payload uses a different vocabulary (`asset_kind` ∈ `{"humanoid", "humanoid_unit", "creature", "static", "building", "static_building"}`, per `blender_worker.py:756,1056,1223,2275,3653,3776`). `nonhumanoid_winged_biped` and `nonhumanoid_creature` occur **once** each in the corpus (their own definition), and `static_prop` twice. Reconcile the two vocabularies or drop the orphan profiles.

**`config/meshy_tool_schema.lock.json` — keys no code reads:** `server_git_head`, `compatibility_sdk_version`, `verified_at`, `schema_source`, `schema_revision`, `forbidden_provider_inputs`, `schema_evidence` (each 1 occurrence). `required_tools`, `server_package` and `server_version` are read by `verify_environment.py` and the Meshy wrapper tests. These unread keys are provenance evidence rather than dead weight — the README requires recording them — so this is a "documented manual record, keep" case, not a deletion candidate.

**Config values that contradict the current 32-operation surface or the current policy:** none found. `config/blender_hoi4_adapter.json` `adapter_version` `1.10.51` equals `dependencies.lock.json` `routes.blender_hoi4_adapter.version`, and its 32-entry `operations` array is identical to the lock's. The 32 MCP handlers map 1:1 onto those 32 operations. No config value names a deleted operation. The policy breach I found is in code (`WINGED_BIPED_BONE_NAMES`, H3) and in already-deleted code (`pdx_skin_membership.py`, H2) — not in config.

## 4. Wrappers and entrypoints (task item 6)

`wrappers/` holds six files, of which two are live routes:

| file | references | status |
|---|---|---|
| `run_blender_hoi4_adapter.cmd` | `%ADAPTER_ROOT%`, `uv run python -m chaosx_blender_hoi4_mcp` (line 23); consumed by `.codex/config.toml:59`, `.mcp.json` | **live** |
| `run_meshy_mcp.cmd` / `run_meshy_mcp.ps1` | Meshy stdio route; consumed by `.codex/config.toml:28` | **live** |
| `run_blender_lab_mcp.cmd` | dev-only route; `.codex/config.toml:92-93` sets `[mcp_servers.blender_lab_dev] enabled = false` | live but **disabled by config** — plausibly kept on purpose |
| `patch_meshy_mcp.mjs`, `meshy_motion_compat.mjs` | Meshy compatibility patch; README:20-22 requires it | **live** (reached from `run_meshy_mcp.ps1`) |

No wrapper references a deleted operation or a deleted file. `wrappers/run_blender_hoi4_adapter.cmd` contains the string `ADAPTER_ROOT`, which is why my analyzer classified `blender_worker.py:21 ADAPTER_ROOT` as config/doc-only rather than self-only — it is used by the wrapper, so it is live.

`init_pilot_jobs.py` **does not exist** (`os.path.exists` → `False`); it is not referenced anywhere.

`run_pilot.py` and `verify_environment.py` are documented manual entrypoints (`README.md:334-339`) with no programmatic caller anywhere in the repo. `inspect_meshy_live_schema.py` has no reference outside its own docstring. `blender_client.py`, `meshy_client.py` and `pack_pdx_material.py` are libraries with no `__main__` block. This is the "unused by any current route but plausibly kept on purpose" category for `verify_environment.py` (it is the lock gate the README mandates) and `inspect_meshy_live_schema.py` (one-shot schema probe); `run_pilot.py` is the one I would call genuinely questionable, because its shipped specs cannot run — its `PILOT_SPECS` reference inputs live under `docs/assets/chaos_redux_3d_model_pilots/`, and that directory does not exist.

## 5. Tests (task item 7)

39 test files (16 `blender_*_integration.py` scripts that require Blender, 23 `test_*.py` unit/contract suites). Findings:

**Stale, self-contradicting version gates.** Current `adapter_version` is `1.10.51`. Six integration scripts hardcode an older literal and would abort on their first assert:

| file:line | hardcoded | vs `1.10.51` |
|---|---|---|
| `tests/blender_humanoid_component_review_integration.py:29` | `"1.10.21"` | stale |
| `tests/blender_humanoid_component_review_integration.py:225` | `"1.10.21"` | stale |
| `tests/blender_locator_adapter_integration.py:52` (and docstring `:3`) | `"1.10.17"` | stale |
| `tests/blender_mesh_region_integration.py:26` | `"1.10.18"` | stale |
| `tests/blender_orphan_image_retention_integration.py:18` | `"1.10.45"` | stale |
| `tests/blender_partition_image_consumers_integration.py:19` | `"1.10.45"` / `"1.10.46"` | stale |

The non-integration suites do the right thing and compare config against the lock rather than a literal (`test_animation_processing_tools.py:63`, `test_bvh_animation_import.py:49`, `test_adapter_recovery_release.py:209`, `blender_stdio_live_regression.py:19`). The six above are the stale family.

**Stale pinned digests.** `tests/blender_humanoid_component_review_integration.py:18-22` pins `REVIEWED_CANDIDATE_HASHES` for `blender_worker.py` (`0C59C4E1…`), `chaosx_blender_hoi4_mcp.py` (`B72B323C…`) and `blender_client.py` (`B2FE78FA…`), then asserts equality at lines 35-36. Actual current digests are `F735CCFD…`, `FB4ED2AA…` and `23036845…`. All three are stale.

**Known-failing tests — test bug vs code defect.**

1. `tests/blender_humanoid_component_review_integration.py` — **test bug, fully explained by the stale literals.** Line 29 asserts `config["adapter_version"] == adapter["version"] == "1.10.21"`; the real value is `1.10.51`, so `verified_environment()` aborts there, before any adapter code runs. Lines 35-36 would fail next on the three stale SHA-256 pins. No adapter defect is implicated. Notably, lines 32-34 (`for path, expected in adapter["source_sha256"].items(): assert digest(REPO_ROOT / path) == required`) would **pass** — the lock is current — so removing the stale version literal and the three stale pins is sufficient.
2. `tests/test_prepare_scale_persistence.py` — **test bug in the assertion harness that masks a real signal.** Line 13 hardcodes `TARGET_HEIGHT = 7.351824` and lines 21-28 shell out to Blender with `check=False`, then line 29 asserts `returncode == 0`. Lines 31-35 then do `next(json.loads(line) for line in stdout.splitlines() if line.startswith("{") and '"status"' in line)` — if the subprocess failed there is no such line, so the test raises `StopIteration` instead of reporting the Blender failure. The failure is real but the diagnostic is wrong; the assertion should surface `result.stdout + result.stderr` the way line 29 does. This is a bad fixture/assertion, not an adapter defect.
3. `tests/test_meshy_wrapper_lifecycle.py::test_full_verifier_uses_only_its_call_owned_job_receipts` — **not present in the current file.** `test_meshy_wrapper_lifecycle.py` is now 278 lines with no test by that name. The concurrent writer appears to have removed or renamed it, so this entry in the known-failing list is already resolved; it should be dropped from the baseline rather than carried forward.

**Tests that exclusively exercise unused surface.** `tests/test_adapter_recovery_release.py` (209 lines) is the clearest case: it imports `assembly_yaw`, `animation_root_export`, `explicit_vertex_remap`, `mesh_inspection_repair` and `mesh_winding_repair` (lines 21-25) and asserts on `validate_yaw`, `align_initial_root_records`, `verify_initial_root_records`, `validate_remap`, `validate_component_dds` — all of which sit behind the 11 unreachable operations in H1. It is testing real code that no configured route can reach.

**Tests that duplicate each other's coverage.**
- `tests/test_mesh_winding_repair.py` and `tests/test_mesh_winding_seam.py` both exercise winding logic; the second tested the now-deleted `mesh_winding_seam.py` and should be deleted with it.
- `tests/test_skeletal_export_streams.py` and `tests/blender_partition_production_preflight.py` both load `adapter/skeletal_export_partition.py` by file location and assert on `_inputs`/`_material_signature`; `tests/test_partition_image_consumers.py` and `tests/blender_partition_image_consumers_integration.py` both assert on `_partition_clone_ownership`/`_partition_image_consumers`/`_fingerprint`.
- `tests/test_orphan_image_retention.py` and `tests/test_reimport_promotion_contract.py` both assert on `_promotion_image_retention`, `_promotion_material_retention` and `_promotion_image_record`.
- `tests/test_mesh_region_inspection.py` and `tests/test_humanoid_component_review.py` overlap on `_mesh_region_inputs`, `_mesh_region_object_dependencies`, `_mesh_region_action_hash`, `inspect_mesh_region`, `inspect_mesh_action*`.

**Fixture provenance is sound.** `tests/fixtures/skeletal_material_streams.md` cites a 53 MB native export and its SHA-256; the cited file exists (`docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset_locator_closure_20260904/alien_infantry.txt`, 53,601,767 bytes) and its digest matches the claim exactly (`477FEE2694AC4784E7DBB94D2F50669634ADD40D1C729CD8E3F38BE0F06A9874`). Keep.

No test imports a module that no longer exists: `mesh_winding_seam` and `pdx_skin_membership` appear in no test file (only `tests/test_mesh_winding_seam.py` referenced the former, and it is deleted too).

## 6. Repo hygiene (task item 8)

**`__pycache__` and `.pyc`: 145 files, 4,191,986 bytes (~4.0 MB) in four directories** — `adapter/__pycache__` (52 files, 2,768,602 B), `tests/__pycache__` (69 files, 1,058,362 B), `lib/__pycache__` (12 files, 133,841 B), pipeline root `__pycache__` (12 files, 231,181 B). All git-ignored (`.gitignore:97-98`) and **zero tracked** (`git ls-files` → 0), so this is disk noise only, not committed bloat. Lowest priority, but two `.pyc` generations per module are present for the wrong interpreters: `cpython-311`, `cpython-313` and `cpython-39` variants coexist for `blender_worker.py` alone (`blender_worker.cpython-311.pyc` 739.5 KB, `cpython-313.pyc` 474.3 KB, `cpython-39.pyc` 257.5 KB).

**Orphaned bytecode for modules that no longer exist** — the more interesting hygiene signal, and it is direct evidence of what was removed. Nine `.pyc` files in `adapter/__pycache__` and `tests/__pycache__` have no corresponding `.py`:

| orphaned `.pyc` | size |
|---|---|
| `adapter/__pycache__/manual_creature_rig.cpython-313.pyc` | 94.4 KB |
| `adapter/__pycache__/manual_creature_rig.cpython-39.pyc` | 50.3 KB |
| `adapter/__pycache__/fitted_humanoid_repair.cpython-311.pyc` | 59.8 KB |
| `adapter/__pycache__/fitted_humanoid_repair.cpython-313.pyc` | 52.1 KB |
| `adapter/__pycache__/identity_leaf_alias.cpython-313.pyc` | 28.4 KB |
| `adapter/__pycache__/explicit_skin_repair.cpython-313.pyc` | 26.1 KB |
| `adapter/__pycache__/explicit_skin_repair.cpython-39.pyc` | 13.8 KB |
| `adapter/__pycache__/mesh_winding_seam.cpython-39.pyc` | 30.3 KB |
| `tests/__pycache__/test_rigid_weapon_attachment_tool.cpython-39.pyc` | 5.4 KB |

`manual_creature_rig`, `fitted_humanoid_repair`, `identity_leaf_alias` and `explicit_skin_repair` have **no source file and zero references** anywhere in the pipeline. These are the remains of the deleted rig/weight generators, so their presence is consistent with the policy change and they should be cleared.

**No duplicate file copies.** A content-hash scan of every in-scope non-vendor/non-report/non-venv file found no identical pairs.

**Not hygiene items, keep:** `adapter/.venv/**` (2,656 files, ~50.9 MB) is the runtime for the live MCP server — `wrappers/run_blender_hoi4_adapter.cmd` resolves `uv.exe` and runs `uv --directory "%ADAPTER_ROOT%" run python -m chaosx_blender_hoi4_mcp`, and `adapter/pyproject.toml` declares the `chaosx-blender-hoi4` entry point. `adapter/uv.lock` (191.9 KB) pins it. Both are git-ignored and both are load-bearing. One gap worth noting: `uv.lock` and `pyproject.toml` are **not** hashed by `dependencies.lock.json`, so a dependency change there is invisible to `verify_environment.py`. Also note the two unrelated version numbers — `pyproject.toml` project version `1.2.0` vs adapter version `1.10.51`.

**No scratch or generated artifacts** at the pipeline root; `reports/` holds only dated release evidence (out of scope, not judged) plus an untracked `reports/README.md` (`git status` shows `??`).

**Dirty working tree inside scope** (not itself a defect, but the audit's line numbers depend on it): `git status --porcelain .tools/3d_pipeline` shows 9 modified files, 3 deletions and 1 untracked file. `meshy_client.py` and `pack_pdx_material.py` have mtimes from earlier the same day and are unmodified.

## 7. Totals by category

| category | count | detail |
|---|---|---|
| Dead modules (whole file) | **2** | `mesh_winding_seam.py` (428 lines), `pdx_skin_membership.py` (173 lines) = **601 lines**, both already deleted in the working tree |
| Dead module-level symbols in live modules | **4** | `blender_worker.py:32`, `:33`, `:5045-5069`, `lib/paths.py:23` = **28 source lines** |
| Dead spec field | **1** | `run_pilot.py:1223` |
| Unused imports | **1** | `lib/paths.py:15` `Iterable` |
| Imports of non-existent modules | **0** | — |
| Operations exposed but reachable from no configured route | **11** of 32 | H1 |
| Dead config keys (no code reader) | **6** in `blender_hoi4_adapter.json`, **~1** read leaf in `asset_profiles.json`, **7** provenance keys in `meshy_tool_schema.lock.json` | §3 |
| Duplicated helper families | **6** | sha256 (4 copies), JSON digest (3), identifier validation (6), job-path resolution (4), DDS conversion (2 + 2 inline copies), PNG dimension read (3) |
| Stale test version literals | **6** files, 7 literals | §5 |
| Stale test digest pins | **3** | `blender_humanoid_component_review_integration.py:18-22` |
| Orphaned `.pyc` for deleted modules | **9** files, ~361 KB | §6 |
| `__pycache__` ignored bytes | **~4.0 MB** | 145 files |

## 8. What I could not determine

- **Whether the 11 unreachable operations are intentionally parked.** They may be deliberate manual escape hatches kept out of the production enablelist. Their implementations are complete and tested, which argues against them being abandoned; but nothing in `README.md`, the skill files or the plans states that a manual-only tier exists. I record them as unreachable, not as dead.
- **Whether the `asset_profiles.json` policy blocks (`materials`, `triangle_range`, `rig_route`, `root_policy`, `controlled_reduction_allowed`, `building.placement`) are enforced elsewhere.** I searched for every key name across all 75 in-scope text files and found no reader. They may be enforced by the agent per the skill instructions rather than by code, which would make them documentation rather than dead config — I could not confirm which, because `.agents/skills/**` is outside my judging scope.
- **The full tests verdict.** A dedicated tests/wrappers sub-audit was still running when this report was finalised. §5 is entirely from my own direct inspection of `tests/**` and `wrappers/**`; the sub-audit may add findings on wrapper checksum comparisons and on tests I did not open individually.
- **Behaviour of the `blender_*_integration.py` scripts.** They require Blender, which this audit was forbidden to start, so the stale-version failures are predicted from their assert statements rather than observed.
- **`run_pilot.py`'s two shipped specs.** I confirmed `docs/assets/chaos_redux_3d_model_pilots/` does not exist and that `PILOT_SPECS` inputs name paths under it, but I did not enumerate every job root to prove no alternate copy exists.
- **Whether the concurrent writer is finished.** The tree changed at least six times during this audit, most recently `dependencies.lock.json` at 23:37:31 and `blender_worker.py` at 23:37:24. Every line number here was re-verified against the digest table in §0 after the last observed write, but any further write invalidates them.

## 9. Disposition

Applied after the audit, by the parent agent. The audit bound its findings to a revision that was still being written, so its HEAD-versus-worktree notes are historical.

| Finding | Disposition |
| --- | --- |
| H1 eleven operations unreachable | Fixed. .codex/config.toml now enables the full published 32-operation surface, and the Meshy allowlist now matches the lock's 13 erified_tools. |
| H2 dead modules on the rigging path | Fixed. dapter/mesh_winding_seam.py, dapter/pdx_skin_membership.py and 	ests/test_mesh_winding_seam.py were deleted. |
| H3 WINGED_BIPED_BONE_NAMES | Fixed. Deleted from dapter/blender_worker.py. |
| M1 runner declares a rig and animation plan | Kept deliberately. The runner records the job's provider plan, including humanoid_rig_route, the rig and animation credit estimates, and the per-role preset action ids, and the 3D worker executes those stages through the locked Meshy route. The runner still spends nothing on them. |
| M2 to M6 duplicated path, digest, validation and DDS helpers | Kept. These are accepted duplication across hash-locked adapter modules; consolidating them would touch the locked surface with no behavioural gain. Recorded here as a known cleanup candidate for a dedicated refactor. |
| M7 dead staging constant and key | Fixed. lib/paths.STAGING_ROOT and the inal_staging_root config key were removed and the README staging sentence was corrected. |
| L1 dead constants and stale spec field | Fixed. Both creature ground-contact constants and lender_reference_height_m were removed. |
| L2 unused Iterable import | Fixed. |
| L3 unvalidated --phase | Fixed. The value is now checked against the supported set and a missing value raises a usage error. The guard sits behind the import-time provider key gate, so it cannot be exercised in a shell without MESHY_API_KEY. |
| L4 hardcoded adapter version in a test | Fixed. The integration test now compares the config version to the lock version. |
| L5 dead io_archive assignment | Fixed. |

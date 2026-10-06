# Geometry and animation delivery checks handoff

Disposition: implemented within the authorized shared pipeline scope.
Parent integration, actual export refusal, native reimport proof and installed-byte findings are recorded in `pipeline_report.md`; full model acceptance remains open.

The change covers the shared geometry and animation tooling requested in sections 3.3, 3.4, and the motion-peak output requested in section 3.8 of `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md`.

No Blender process, GUI, Meshy provider, sound source, runtime model, entity, gameplay file, adapter operation schema, dependency lock, or skill file was changed.

## Files changed

- `.tools/3d_pipeline/adapter/animation_delivery_checks.py` adds decoded PDX animation inspection, hierarchy-based world-motion checks, and existing quaternion-curve sign cleanup.
- `.tools/3d_pipeline/adapter/geometry_delivery_checks.py` adds read-only positional topology, winding, split-normal, provider-intake boundary, and per-stream capacity reports.
- `.tools/3d_pipeline/adapter/mesh_winding_repair.py` now returns non-manifold island evidence from inspection and marks those islands ambiguous for orientation repair.
- `.tools/3d_pipeline/tests/test_animation_delivery_checks.py` adds pure-Python tests for continuity, loop/root gates, strike windows, world motion, and measured foot plants.
- `.tools/3d_pipeline/tests/test_geometry_delivery_checks.py` adds tests for tolerance topology, duplicate faces, split normals, boundary limits, and combined material streams.
- `.tools/3d_pipeline/tests/test_mesh_winding_repair.py` adds a non-manifold island diagnostic test.

## Integration API

`normalize_quaternion_curve_signs(fcurves)` preflights each quaternion data path for all four components and exactly matching key times, then negates only the existing key values and both Bézier-handle values when the next quaternion has a negative dot product with the preceding quaternion.

The quaternion helper performs no key insertion or deletion, bone creation, weighting, or action synthesis, and it fails before mutation if a curve group is incomplete or time-misaligned.

`inspect_animation_delivery(anim_tree, skeleton_tree=..., action_name=..., role=..., looped=..., root_bone=..., humanoid=..., strike_windows=..., foot_world_measurements=...)` expects actual decoded PDX bytes and explicit action metadata from the parent’s entity/job inventory.

The animation report contains quaternion-sign evidence, loop seam metrics, in-place root checks, single-frame rotation and world-displacement violations, a local-channel `motion_peak_table`, and a separate `world_motion.world_motion_peak_table` built by composing local `.anim` TRS through the matching `.mesh` skeleton `ix`/`pa` hierarchy.

The local peak table has `frame`, `bone`, `angular_deg`, `translation_step`, and `time_seconds` columns and describes local channel deltas; the world table measures actual decoded joint-head steps and is the source for the `0.25` units-per-frame speed gate.

PDX coordinates are treated as Y-up with X/Z horizontal and -Z forward, following the installed `io_pdx_mesh` source; `in_place_xy_preserve_z` therefore constrains PDX X/Z while preserving PDX Y.

The non-death planar drift ceiling and death forward ceiling are both `0.2` units as directed by the parent.

Foot-plant counts are produced only from supplied measured Blender world-foot positions with a ground plane, contact and stationary tolerances, measurement uncertainty, and minimum contact-frame count; absent evidence returns `unmeasured` and no suggested plant event times.

Unknown action loop state, profile, root selection, mesh skeleton, or required humanoid move contacts keeps the action at `needs_review` instead of passing.

`inspect_geometry_delivery(positions, triangles, normals=...)` reports hypothetical weld topology at `0.0005`, `0.001`, and `0.002` units without mutating the input.

`inspect_pdx_mesh_tree(mesh_tree)` combines every material mesh stream under the same named object with offset indices before topology or winding analysis, while reporting each stream’s vertex and index capacity separately.

The geometry report retains evidence for boundary and non-manifold edges, disconnected islands, degenerate and duplicate faces, edge-direction winding counts, split-normal groups, and the exact-position outward-winding plan.

Provider intake requires fewer than 200 boundary edges at every requested positional tolerance; the export gate requires clean manifold topology, no duplicates or degenerates, and an outward-winding plan that proposes no face flips.

Non-manifold components return `blocked` evidence and no outward-volume result; `repair_mesh_winding` continues to reject every ambiguous plan before any face is changed.

## Evidence and validation

`python -m py_compile` succeeded for both new modules, the winding repair module, and all three focused test modules.

`python -m unittest tests/test_animation_delivery_checks.py tests/test_geometry_delivery_checks.py tests/test_mesh_winding_repair.py` passed all 26 tests without launching Blender.

The test suite includes a two-bone case where a static local hand translation produces a measured world displacement over `0.25` units per frame when its parent rotates.

The locked parser helper `.tools/3d_pipeline/runtime/pdx_reader.py` decoded the actual mod runtime pair `xenobiological_assault_organism_idle.anim` and `xenobiological_assault_organism.mesh` from `.tools/3d_pipeline/config/blender_hoi4_adapter.json`’s installed `io_pdx_mesh` path.

That `.anim` is 30 fps with 192 samples and 30 joints; under an idle-loop and root-Hips assumption it measures a `9.4518` degree loop angle gap, a `0.04991` unit position gap, four raw quaternion sign discontinuities, and 93 composed world-motion threshold violations.

The matching `.mesh` has one logical object with four material streams, 34,351 source positions, 31,233 triangles, 28 boundary edges, and 18 non-manifold edges at `0.002` units; these are diagnostic measurements and not an acceptance claim.

The installed vanilla reference `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/ENG_infantry.mesh` decoded into two logical objects; the infantry object has one stream, 2,107 positions, 3,113 triangles, 102 boundary edges, and 9 non-manifold edges at `0.002` units, while `pCubeShape1` has one stream, 8 positions, 12 triangles, and zero boundary or non-manifold edges.

The source-informed parser evidence is the installed extension manifest version `0.91.0`, installed `pdx_data.py` SHA-256 `B1002FDF6A0C23DA4219EFBDBA2DBE0A68AAA97558C528E64EE89EEDD1928541`, and installed `pdx_blender/blender_import_export.py` SHA-256 `9A88A5529623FB7EF9D572DA87991980B691D790749F0A32C278580628BC0781`.

The dependency lock currently records adapter version `1.10.51`, `io_pdx_mesh` version `0.91.0`, and compatibility archive SHA-256 `508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702`; the repository archive hash matched that lock value.

The reference basis is `.tools/3d_pipeline/config/dependencies.lock.json` SHA-256 `BCD467495372E4678F60490F2273A59177378E6EA452C72DA67BD160D765CF1D`, `.tools/3d_pipeline/runtime/pdx_reader.py` SHA-256 `55F088EC6F6C364109A7E2830284CEA0010A04A39BF4041C2582690526940C7B`, the installed vanilla mesh SHA-256 `D7B66F4C5ECCEE8D8321125B02E1A8A1E98BDDF2511DF0EF4709C62AD16E466F`, and the matching mod `.anim`/`.mesh` SHA-256 values `22869AE9C47066C27DF129E37311E2EB4EB72E2890C3D022A8D8FD616F4DD6FE` and `66830DA246460CEF9E6112B0F81D642196F92268A6394B0C114CF8444F034EDB`.

The installed decoder’s `read_meshfile` accepts binary `@@b@` files at `pdx_data.py:203-225`; an installed vanilla text `.anim` with `@@t@` is rejected by that function, so vanilla text animation decoding remains a known parser limitation.

The installed coordinate mapping and animation semantics are documented in the exact source at `blender_import_export.py:455-479` for skeleton `ix`/`pa`/`tx`, `530-545` for root-first hierarchy order, `548-570` for parent-relative frame transforms, and `600-614` for PDX Y-up coordinate conversion.

The offline wiki and installed documentation reference routes are being handled by the parent agent and are not repeated in this implementation handoff.

No Meshy task was created, so estimated and consumed Meshy credits are both zero; no MESHY_API_KEY or balance gate was needed.

Blender was not launched, no adapter worker was invoked, and no Blender process or export/reimport result is claimed.

## Parent integration and remaining limits

The parent must call quaternion continuity before retiming or export, then decode the actual exported `.anim` bytes and pass the exact matching mesh skeleton to `inspect_animation_delivery`.

The parent must pass the entity-verified root bone, semantic role, loop or state-chain behavior, humanoid profile, and explicit strike windows; the first serialized info bone remains an evidence-bearing fallback and is not a pass without an explicit root selection.

The parent must preserve separate local and world peak tables when wiring entity-event timing checks and must use measured Blender sole/contact evidence for move plants.

The parent must add the new import closure and operation wiring to the adapter config, live schema, source-hash lock, and worker export path after its integration review.

The audit did not validate live Blender reimport, entity timing lint, sounds, counters, GFX wiring, or in-game consumers; those remain parent-owned or package-owned work.

The decoded actual-file measurements above are evidence for triage only and do not replace Blender visual review, exported-byte reimport, or user runtime validation.

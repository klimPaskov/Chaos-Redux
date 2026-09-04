# Read-only humanoid component review: candidate contract

Date: 2026-09-02.
Status: parent-reviewed plan implemented as an unregistered adapter 1.10.19 candidate; registration, version/lock refresh, route alias, and production review remain parent-owned.
Scope: the smallest repository-owned inspection addition required to identify existing loose geometry without separating or changing a production mesh.
The adapter remains frozen at 1.10.19 while Alien and Robot use it.

## Confirmed blocker and route correction

The appended probe evidence in `016_final_portal_preserved_weapon_intake_2026-09-02.md` distinguishes two issues: a missing pilot job override and an absent component-review operation.
The existing `portal_raider` override intentionally resolves to the shared body-only job and must remain unchanged.
The pilot's actual directory exists at `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider`; its `job.yaml` explicitly declares `job_id = portal_raider_meshy7_recovery`.
The default slug resolver instead looks for a nonexistent sibling directory named `portal_raider_meshy7_recovery`.

The parent-owned route change is exactly one `job_overrides` entry in `.tools/3d_pipeline/config/blender_hoi4_adapter.json`:

```json
"portal_raider_meshy7_recovery": "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider"
```

Do not add arbitrary job-root input, change slug validation, move the pilot, rewrite its intake, or redirect the shared `portal_raider` alias.
The proposed first source is `blender/checkpoints/accepted_static_geometry_pre_rig.blend`, whose SHA-256 was independently remeasured in this turn as `214DCF6067C49DD79E1CBFBB871E284D8D7BDD6803D97490456C1C01ABB5429D`.
Its exact mesh name must come from a successful read-only inventory after the route is registered; the plan does not guess it from another checkpoint's object names.

## Minimal callable schema

Add the already skill/README-prescribed tool `chaosx_blender_hoi4_review_humanoid_components`, mapped only to worker operation `review_humanoid_components`.
Keep `inspect_scene` and its `mesh_region` schema and output unchanged.

```python
def chaosx_blender_hoi4_review_humanoid_components(
    job_id: str,
    blend_rel: str,
    expected_source_sha256: str,
    mesh_name: str,
    render_group: bool = True,
    component_ids: list[str] | None = None,
    component_offset: int = 0,
    component_limit: int = 16,
    preview_view_names: list[str] | None = None,
) -> dict:
    ...
```

- `blend_rel` is an existing same-job `.blend`; absolute, traversal, backslash, non-file, and escaping symlink paths fail.
- Require a canonical 64-hex source hash and exact existing local `MESH` object name, with no object selection by prefix, bounds, material, or inferred weapon semantics.
- This first capability reads an unrigged static mesh only: no parent, modifiers, shape keys, constraints, object/data animation, drivers, or NLA on the selected mesh.
  Existing protected/provider-source metadata is permitted and preserved because this is read-only.
  Other source objects and actions are neither evaluated nor rendered and remain untouched.
- `render_group` must be the literal boolean `true`; a bounds-only result is not this operation's completed review evidence.
- With no explicit IDs, render a stable catalog page beginning at `component_offset`, containing 1–16 components.
  With `component_ids`, require 1–16 unique exact catalog IDs and default offset/limit; reject every unknown, duplicate, or stale ID rather than dropping it.
- Views are unique members of `front`, `left`, `right`, `rear`, `top`, and `three_quarter`, defaulting to all six.
  Render at a fixed 1024×1024 per view, with no custom cameras, scripts, shaders, URLs, arbitrary output paths, or render-engine arguments.
- Initial hard caps are 250,000 source vertices, 500,000 polygons, 1,500,000 loops, 1,000,000 edges, and 8,192 components.
  The preserved reduced static candidate and remesh fit this bounded intake; the original million-vertex generation is explicitly outside this first capability and must fail before rendering rather than be decimated or sampled silently.
- No action/frame argument, checkpoint output, geometry import, extraction, rigging, attachment, material conversion, or provider operation is included.

## Deterministic component identity and measured records

Use the source mesh's vertex/edge incidence graph, including loose edges and isolated vertices, without position welding or a distance tolerance.
Faces must refer only to valid source indices and all face vertices must belong to the same graph component; inconsistent source topology fails.
Components touching through a shared source vertex remain one component, while coincident but separately indexed vertices remain separate.
Sort components by minimum source vertex index and name them `c_v<minimum-index>`; bind every ID to the source SHA, exact object/data names, and full `_mesh_region_topology` hash.
Do not use face count or iteration order as identity, and do not call a component a rifle, body, hand, stock, or muzzle automatically.

Write one request-ID-scoped job report containing the complete catalog and exact source vertex, edge, polygon, and loop membership for every component.
The normal adapter receipt returns the catalog/report SHA, total counts, rendered page, next offset, and explicit pagination status rather than a huge inline vertex dump.
The bounded full report must not truncate component membership; reject a report that exceeds its declared size ceiling instead of silently omitting indices.
Use a 64 MiB serialized report ceiling for this initial intake.

For every component, record:

- vertex/edge/polygon/loop and derived triangle counts; loose-wire, isolated-vertex, surface, or mixed topology class; face-incidence boundary/non-manifold counts; degenerate face counts; boundary graph component and closed-loop counts, without calling every open boundary a proven hole;
- exact source memberships and their canonical hashes, object-space coordinates/normals, source loop corner normals, and finite object/world matrices, origin, determinant, bounds, dimensions, and measured centroid;
- per-material polygon/loop counts, exact slot names and material graph fingerprint, and linked image identity, resolved same-job file hashes or packed-byte hashes;
- every UV layer's exact source loop mapping and UV coordinates/hash, finite UV bounds and UV-island membership using exact shared-edge endpoint equality rather than a seam-distance heuristic;
- existing vertex-group names and weights where present, without adding, deleting, normalizing, or reinterpreting them.

Reuse `_mesh_region_topology`, `_locator_numbers`, `_locator_matrix_record`, and typed `_promotion_value`/digest/material-record primitives where their contracts fit.
For positive nonuniform transforms, positions use the full affine matrix and normals use its inverse transpose followed by normalization.
Reject negative or singular selected-object transforms and nonfinite geometry/UV/normal data.
Do not reuse promotion's working-object eligibility, retained-action, or orphan-material acceptance policy: a read-only source may be protected or contain harmless unused data, and no original datablock is allowed to disappear in this operation.

## Grouped labelled previews and non-mutation proof

`render_previews` currently changes source scene render/world state and creates QA objects/materials in that scene, so calling it directly would not meet this contract.
Reuse its named view directions and camera-framing mathematics only.
Build one disposable QA scene whose dim neutral whole-body reference is a copy of the exact selected mesh at the measured source matrix.
Highlight the requested components in stable contrasting colors using only temporary evidence copies of their observed faces, with a source-index mapping retained in the report.
Display explicit component IDs with matching legend swatches in every named view; use leader lines and a fixed legend area rather than allowing overlapping ID text to appear as a valid label.
Do not reposition, explode, enlarge, complete, smooth, weld, repair, or decimate source components for the grouped view.
Zero-face components remain in the catalog and are labelled as wire/point evidence rather than being silently discarded or rendered as invented surfaces.

The preview report records source/data hashes, component IDs, view/camera matrices, preview file hashes, and visibility limitations for small or occluded components.
An unreadable, fully occluded, or zero-face component must retain that explicit status; numerical bounds and a legend entry alone do not establish its visual identity.
These are neutral geometry identity views, not PDX material/render acceptance.
Actual source UV/material bindings remain numeric evidence and source textured previews remain separate reference evidence.

Open with `use_scripts=False`; do not run source handlers or evaluate dependency graphs for this static path.
Capture the exact selected mesh/topology/UV/normals/material/image/weight record plus original scene, object, collection, action, selection, camera, visibility, frame, and render-state fingerprints before creating evidence data.
Track each temporary datablock explicitly; do not run global orphan purge or remove anything merely by name prefix.
Use `finally` to restore context and remove only those tracked temporary objects/scenes/materials/meshes/cameras/lights/text/image outputs from memory.
After cleanup require exact equality of the original data inventory and all before/after fingerprints, plus original source file size and SHA in both success and failure paths.
No save-mainfile, save-as, export, library-write, source texture write, or checkpoint write may occur.
Only request-ID-scoped report/PNG evidence inside the job and the adapter's existing request/result logs may be written.
On any mismatch, return failure with the exact section delta; do not label the review accepted.

## Small integration surface and release order

After all active model workers release the frozen-source boundary, the anticipated implementation owns only:

1. `.tools/3d_pipeline/adapter/blender_worker.py`: one input validator, source-component collector, disposable grouped renderer, and operation dispatch entry beside existing inspect helpers; the bounded opt-in action-channel inventory branch below.
2. `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py`: the explicit typed forwarding function above and the two optional inspect arguments below.
3. `.tools/3d_pipeline/blender_client.py`: matching `review_humanoid_components` forwarding wrapper and optional inspect-argument forwarding.
4. `.tools/3d_pipeline/tests/test_humanoid_component_review.py` and `.tools/3d_pipeline/tests/blender_humanoid_component_review_integration.py`: focused fast contract and disposable native fixture tests.

The parent separately owns one alias addition, one operation allowlist entry, Codex enabled-tool registration, version decision, source hashes, lock refresh, and environment/schema verification.
Do not change shared configuration, locks, runtime registration, provider schemas, install scripts, or existing inspection semantics while implementing the candidate.
Use the existing repository-owned adapter worker launch; do not add a secondary runtime, custom executable, Python/script parameter, socket route, or component-repair framework.

Before any pilot review, require:

1. Fast tests for stable index IDs, coincident-but-unwelded components, shared-vertex connectedness, loose edges/points, complete membership, UV seams/material partition, cap/pagination limits, bad names/IDs/views, malformed hashes, source hash mismatch, path escape, invalid transforms, and forwarded schema.
2. A synthetic native fixture with several disconnected colored/UV-mapped components in one mesh, a loose edge and isolated vertex, a positive nonuniform transform, protected source metadata, and an unrelated retained action.
   It must prove exact component membership, world/normal arithmetic, complete labelled six-view evidence, complete cleanup, exact original fingerprints/source bytes, and failure immutability after an injected render exception.
3. Parent review, deliberately registered/relocked version, `verify_environment` with no provider probe, live schema proof, and the native fixture through that exact locked version.
4. A read-only pilot inventory and grouped review using the remeasured source SHA; parent visual acceptance of exact component IDs before any separate extraction/attachment work is designed or authorized.

If the actual rifle and body are one connected component, this operation must report that fact and stop short of a clean-separability claim.
It does not introduce texture-color segmentation, automatic gun detection, caller-defined spatial cutting, or a fallback weapon.
Measured contact/endpoints require a later explicit selection of observed vertices after visual identification; the component review does not invent stock/grip/muzzle coordinates.

## Read-only action-channel inventory addendum

The parent reported one exact failed Robot attack diagnostic: `Source action has unsupported object, scale, or non-quaternion bone channels.`
At worker lines 6351–6352, the condition rejects a curve when its path either does not start with `pose.bones[` or does not end with `.location` or `.rotation_quaternion`.
This aggregate error does not prove Euler animation: object channels, scale, axis-angle, custom-property, or other unsupported bone paths can produce the same message.
No source key, channel class, or offending bone has been measured by this planning task.

The minimal addition is an opt-in inventory branch inside existing `inspect_scene`, not another operation or action-conversion framework.
Add only `include_action_channels: bool = False` and `expected_source_sha256: str = ""` to its MCP/client declarations.
For inventory mode require the existing exact `action_name` and `target_armature_name` arguments, an existing job-relative `blend_rel`, and the matching canonical source SHA.
Require `render_previews=false`, `mesh_region=null`, `preview_frame=-1`, and no preview views/runtime stem; reject mixed modes.
Default calls and existing inspector output remain unchanged.

The inventory branch must occur before the normal inspector's action-selection/evaluation path, because that path creates animation data, marks objects working, changes visibility, and mutes NLA in memory.
Open the source using `use_scripts=False`, locate the exact rig/action without binding them, and enumerate the action's existing legacy or layered F-curves using `action_fcurves`.
Do not create animation data, set a frame, assign an action/slot, alter a rotation mode, mute tracks, update curves, normalize values, clone anything, render, export, or save.
Each row contains exactly these four diagnostic fields:

```json
{
  "data_path": "<literal F-curve RNA path>",
  "array_index": 0,
  "group": "<literal existing F-curve group name, or null>",
  "rotation_mode": "<existing resolved owner enum, or null>"
}
```

For a bone path, match the exact escaped `PoseBone.path_from_id()` prefix from the named rig and read that bone's current `rotation_mode`; do not derive the bone from its F-curve group name and do not use `eval` or arbitrary path execution.
For recognized armature-object location/rotation/scale paths, read the exact rig object's `rotation_mode`.
Unresolved owners and other paths receive `rotation_mode=null`; retain the literal path rather than guessing its meaning or discarding the row.
The enum describes the owner's stored mode, not proof that a particular curve is active, meaningful, or the failure's sole cause.
Preserve duplicate path/index rows, including layered duplicates, and report them without conversion or deduplication.
Use deterministic ordering by the four reported fields while retaining duplicate multiplicity.
Require at most 4,096 curves and bounded exact names/path strings; fail explicitly above the cap rather than truncate the channel list.

Return the rows under a new inventory-only `action_channels` result with the exact source path/hash/size, rig and action names, existing native action fingerprint, row count, source-immutable and action-data-unchanged assertions.
The native action fingerprint is the existing inspector curve fingerprint, not the `.anim` file hash.
Read-only hashing may inspect existing keys internally for integrity, but this small diagnostic output must not become a key-edit or pose-sampling endpoint.
Compare complete pre/post native action data and the rig's action/slot/frame/mode bindings, and recheck source SHA/size in a `finally` path; write only the adapter's normal job-bound receipt.
Protected source metadata, orphan materials, and unsupported channel types are not rejection reasons for this inventory: they are precisely the data being inspected without promotion.

Focused tests must distinguish object `location`, bone `scale`, bone Euler, bone axis-angle, quaternion, custom-property, ungrouped, unresolved-owner, escaped bone-name, and duplicate layered records without changing them.
The disposable native fixture must retain at least one Euler curve, one object curve, one scale curve, an unrelated action, and NLA state, then prove that inventory does not bind an action, mute NLA, change rotation modes/keys/handles/interpolation, move the frame, or change source bytes.
These cases extend the same bounded test ownership; they do not authorize a new runtime or fixture copy of the adapter.

### Minimum measurement before any pose-preserving recovery proposal

First obtain this complete inventory for the exact failed action and its named rig from the unchanged source checkpoint.
Bind it to the source SHA and native action SHA, and identify every offending path/index rather than choosing one presumed cause.
Do not infer that the other role actions share those channels; inventory each exact action before proposing a shared recovery.

Only after the channel classes are known should the parent select a further bounded measurement: native FPS/range, relevant source key times/values/interpolation and owner modes, and evaluated local/world bone matrices at all retained output sample frames plus relevant between-key samples.
For object or scale channels, measure their actual contribution to world transforms, deformed mesh bounds, and contacts before deciding whether any representation change could preserve motion.
For a proven Euler or axis-angle rotation track, a future proposal would need source-versus-candidate local/world matrix equivalence, continuity, and contact preservation at those same samples; stored mode names alone cannot establish this.
No deletion of constant channels, Euler-to-quaternion conversion, scale baking, object-to-root transfer, resampling, or replacement motion is approved or implemented by this addendum.
The Portal alias/component review remains independently necessary and is not replaced by this Robot diagnostic.

The parent reports Robot is idle, but Alien has not released the active 1.10.19 boundary.
All production source, config, and lock changes therefore remain prohibited until the parent explicitly releases that boundary.

## Evidence from this planning turn

The `MESHY_API_KEY` presence gate passed without exposing the key.
The 3D model pipeline skill's read-only grouped humanoid review requirement and the matching README requirement were read alongside the intake, current adapter resolver, inspector/mesh-region helpers, renderer, promotion fingerprints, and nonhumanoid segmentation implementation.
Offline core/entity/graphical wiki references and installed vanilla entity documentation and infantry mesh/weapon-attachment precedents were consulted; no gameplay or entity implementation is proposed.
The source checkpoint hash above was read-only verified.
The initial planning turn made no adapter/Blender/provider invocation, production model change, source extraction, staging, or commit.
The later implementation tranche is recorded separately below.

The three production source hashes remain the previously reviewed 1.10.19 bytes:

| File | SHA-256 |
|---|---|
| `.tools/3d_pipeline/adapter/blender_worker.py` | `5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40` |
| `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` | `2011F13EFF2887A67C52A1662381EC7CBE2146132B13B1122285F5E86D2FF935` |
| `.tools/3d_pipeline/blender_client.py` | `ADA7C52EB14AE7A48AEB4D7369E4464E1AA3F447878EB989A0EBCDEA7C6A99A8` |
| `.tools/3d_pipeline/config/blender_hoi4_adapter.json` | `121580FAFFC6FE2DE059F5F6E35E6DFEEF9941F2D11A60F9AC3042185F3636B0` |
| `.tools/3d_pipeline/config/dependencies.lock.json` | `E463B656832F5940420E05F18C96923F1FAE73D3F2115D5612C9DF0A0A1A2FC1` |

No simplification or substitute was introduced into a production asset.
The missing registered route, production visual component identity, clean separability, and subsequent weapon recovery remain explicit blockers rather than implied completed work.

## Implemented unregistered candidate freeze

After Alien and Robot released the adapter boundary, the parent explicitly authorized implementation of the reviewed plan without configuration, allowlist, version, or lock changes.
The following candidate is now frozen for parent source review:

- `review_humanoid_components` is a distinct worker operation and typed MCP/client wrapper.
  It requires the exact job-relative Blend, source SHA-256, exact local unrigged static mesh, `render_group=true`, stable optional component IDs or a 1–16 component page, and 1–6 fixed named views.
- Component identity is deterministic source vertex/edge/polygon connectivity, without position welding, distance thresholds, or semantic weapon detection.
  Coincident separately indexed vertices remain separate; a shared source vertex joins its faces.
- The complete report retains full source vertex, edge, polygon, loop, UV, material, image, weight, transform, bounds, normal, boundary/non-manifold, degenerate, and component-membership evidence under the reviewed caps.
  It calls an open boundary a boundary graph, not automatically a hole.
- Positive nonuniform object transforms use full affine positions and inverse-transpose normalized world normals.
  Negative, singular, nonfinite, animated, parented, constrained, modified, shape-keyed, linked, ambiguous, excessive, and malformed inputs fail closed.
- A disposable QA scene renders the exact mesh copy with requested source faces highlighted against the dim whole body.
  Every page uses stable colors, fixed component-ID text, swatches, centroid leader lines, and 1024×1024 named views.
  Wire/point components remain explicitly catalogued and labelled; their legend/bounds do not claim visible surface identity.
- Only request-UUID-scoped PNGs and the complete report are written under the job.
  No checkpoint, mesh, material, action, provider, export, or source file is written.
  Temporary scene/object/mesh/curve/material/camera/world/render-result data is explicitly removed, and the source record plus original objects/scenes/actions/data inventory must match after success or render failure.
- The opt-in `inspect_scene(include_action_channels=true, expected_source_sha256=...)` branch occurs before the legacy action-binding path and cannot combine with previews or `mesh_region`.
  It binds no action or frame and returns literal `data_path`, `array_index`, group name/null, and resolved existing owner `rotation_mode`/null for every retained curve, including duplicates.
  Complete action data, active action/slot, drivers, NLA strips/mutes, frame/subframe, and object/bone rotation modes are fingerprinted unchanged.
- Legacy `inspect_scene` defaults and `mesh_region` remain unchanged because the two new inventory arguments are forwarded only when the caller explicitly sets `include_action_channels=true`.
- `review_humanoid_components` bypasses `io_pdx_mesh` loading and exposes no code, Python, shell, URL, arbitrary camera, output path, geometry selection, or modification input.

### Files and frozen SHA-256

| File | SHA-256 |
|---|---|
| `.tools/3d_pipeline/adapter/blender_worker.py` | `3C798ACF9182F4644DC3B92A3B7BC3A71399AC0D5EB3BD3D1FE0D86F470C511E` |
| `.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py` | `B72B323CC9B0C9D70597F662F951D1EC0B18F566BB9CFC3854E321D6D03849A4` |
| `.tools/3d_pipeline/blender_client.py` | `B2FE78FA84E297C6A913F4E2E17E2E3C1620F417306E33F3066B6F9162241A50` |
| `.tools/3d_pipeline/tests/test_humanoid_component_review.py` | `CD32F136A12C488427626BFA588751DCF447AD759CB40AC8CEC8C8E8F4CB4088` |
| `.tools/3d_pipeline/tests/blender_humanoid_component_review_integration.py` | `093CF8C44FD64565548F196EA833827D44EFAF1BFA19020D918910ECFE859426` |

The native-fixture hash constants pin the three reviewed production candidate files while shared config/lock remain registered at 1.10.19 without this operation.
The parent must deliberately revise that gate after registering and locking the chosen next adapter version.

### Test evidence

The focused contract suite passed 13 tests in 2.106 seconds:

```powershell
python -B -m unittest discover -s .tools/3d_pipeline/tests -p test_humanoid_component_review.py -q
```

The final shared regression pass also passed: locator 32/32, promotion 29/29, mesh region 14/14, and action phase patch 13/13, for 101 fast tests including the new 13.

The disposable native command was:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 5.1/blender.exe' --background --factory-startup --python-exit-code 1 --python .tools/3d_pipeline/tests/blender_humanoid_component_review_integration.py
```

Its final run exited 0 under Blender 5.1.2 build `ec6e62d40fa9` in 7.094 seconds.
It was explicitly a reviewed unregistered 1.10.19 candidate fixture, not a production adapter call or production asset acceptance.
The fixture created only temporary synthetic data and proved:

- exact action inventory for object location, bone Euler rotation, bone scale, bone custom property, and bone quaternion rotation while preserving the source, keys, action fingerprint, action/slot, NLA, frame, and rotation modes;
- four stable components `c_v0`, `c_v3`, `c_v6`, and `c_v8`, including two surfaces, one loose wire, and one isolated point;
- exact catalog SHA-256 `8E58B70445A2E10D3F78571B63B8385C44085B1E11AB83845CC58E742E66B89D` and native action SHA-256 `A707786E7EBEA6A20E50CF65A1EA2C167F099C3813B50E66A544935F3C400AA0`;
- six nonempty 1024×1024 grouped PNGs, explicit-ID review, UV/material evidence, positive nonuniform world/normal records, full report hash/size, source immutability, and no semantic acceptance;
- unknown component rejection and an injected render failure created no report and left the source bytes unchanged.

During native recovery, the first attempt failed only in fixture construction because an EditBone RNA wrapper was read after leaving Edit Mode; the fixture was corrected to retain the exact names as strings.
The first production-code render reached the candidate and exposed `Object.type` as read-only; the camera type assignment was corrected to `camera.data.type`.
The next run proved that Blender retained a new `Render Result` image datablock after rendering; cleanup was narrowed to remove every image absent from the exact pre-render inventory, after the disposable scene was removed.
The following run passed, then the strict UUID/failure-integrity refinements were applied and the final run above passed again.
No production geometry, checkpoint, report, preview, action, provider route, configuration, lock, or job asset was involved.

### Remaining parent-owned registration and production gates

1. Review the exact candidate diff and hashes above.
2. Add only the accepted pilot alias and operation allowlist/tool declarations, choose the next adapter version, refresh all source hashes through the approved lock path, and run `verify_environment` without a provider probe.
3. Convert the native fixture from its pinned unregistered-candidate gate to the exact registered lock and rerun it before any pilot inspection.
4. Use ordinary read-only pilot inspection to obtain the exact mesh name; then invoke the registered component review with the independently verified checkpoint SHA.
5. Parent-review the actual grouped component visuals and records.
   If the firearm remains joined to the body in one source-index component, this tool must not imply clean separability.
6. Separately inventory the exact rejected Robot action channels before proposing any representation change; the current aggregate error still does not prove Euler as the offender.

No simplification, component extraction, attachment, animation conversion, production recovery, or semantic acceptance was introduced.
No MCP process was restarted, no live adapter/provider call was made, and no file was staged or committed.

## Parent registration and locked validation

The parent reviewed and registered the frozen candidate as adapter `1.10.20` without changing its production source bytes. The registration adds only `review_humanoid_components`, the two opt-in `inspect_scene` arguments already present in the typed source, and the exact `portal_raider_meshy7_recovery` job override. The existing shared `portal_raider` alias remains unchanged.

Current registration hashes:

| File | SHA-256 |
|---|---|
| `.tools/3d_pipeline/config/blender_hoi4_adapter.json` | `DB13ADE86BCA579B38E32094B967CC4F25FACC506E989AADCFFA48166FCD54C9` |
| `.tools/3d_pipeline/config/dependencies.lock.json` | `47A9D051F58BAB64E8BB8829F2C0195A34A869C1F2FD85F58D3F5BD9CA04CB9D` |
| `.tools/3d_pipeline/reports/environment_report.json` | `D89E20731B87B9C7F3A5D41588BC7D7FD46FABF7B25CB8A4F883A4EC9BE90280` |
| `.codex/config.toml` | `24BCAC71960D42D2958FC98B49FD38A5244B0946BF80CF3DDB879A633C269427` |

Post-registration evidence:

- The focused 13-test component-review suite passed.
- `verify_environment.py` returned an empty findings list without a provider probe and rewrote the environment report against adapter `1.10.20`.
- The registered native Blender fixture exited zero under Blender `5.1.2` and reproduced component catalog `8E58B70445A2E10D3F78571B63B8385C44085B1E11AB83845CC58E742E66B89D` and native action fingerprint `A707786E7EBEA6A20E50CF65A1EA2C167F099C3813B50E66A544935F3C400AA0` while preserving the source.
- The live-wrapper registration suite passed all three tests, proving that the enabled tool is exposed with the exact bounded schema and that the adapter operations in the config and lock agree.

This registers a read-only production inspection capability. It does not accept any Portal or Robot component, alter geometry, repair an action, or complete a runtime model package.

## Production-report compaction and Portal evidence

The first registered Portal review rendered all six views but rejected the evidence report because indentation pushed the complete component membership beyond the fixed 64 MiB ceiling.
Adapter `1.10.21` serializes that same report with lossless compact JSON separators.
The ceiling remains 64 MiB, every record and membership index remains present, and no sampling, truncation, cap increase, or geometry change was introduced.

The corrected production call completed against `blender/checkpoints/accepted_static_geometry_pre_rig.blend`, source SHA-256 `214DCF6067C49DD79E1CBFBB871E284D8D7BDD6803D97490456C1C01ABB5429D`, and exact mesh `output_unwrapped.001`.
Its report is `blender/reports/component_review_49eecb73b65b4fdeb07c61f3064e7c85.json`, 42,654,407 bytes, SHA-256 `9A18A5CFF2648BCC891C2DAED92D63D6B094741D5E5A52D3985AA4178BD4A257`.
The component catalog SHA-256 is `6E09C06F4C2785EE14FE07D72640901C0E63ECF86FC4ECD4DEC4874C0DAAD91C`, with exactly one connected component, `c_v0`: 14,909 vertices, 45,041 edges, 29,999 polygons/triangles, 89,997 loops, 83 boundary edges, zero non-manifold edges, zero degenerate polygons, and one loose edge.
The source-data comparison returned `original_data_unchanged = true`.
All six production previews were parent-reviewed together with separate textured front, right, and three-quarter views.
They show the accepted Portal body and its large two-handed firearm as one visually coherent, source-index-connected mesh; the firearm is not a loose component and must not be extracted or replaced.

The adapter source hash for `1.10.21` is `0C59C4E1D6A241003F59458F5DD130C05670633D304A05AB017E554410216FD6`.
The focused component suite passes 14 tests, the legacy locator/promotion/mesh-region/action suites pass 88 tests, the live registration suite passes three tests, the native Blender 5.1.2 fixture passes, and `verify_environment.py` reports no findings.
The native fixture is pinned to the `1.10.21` worker hash and reproduces the frozen synthetic catalog and action fingerprints.
This evidence proves read-only source identity and preserved weapon presence only; rigging, two-hand contact, firing actions, export/reimport, particles, sound, and runtime acceptance remain pending.

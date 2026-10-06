# WP1 Africa model repair handoff

Disposition: `incomplete`. The current source and installed model bytes remain unchanged. The seven tickets still have geometry and/or semantic-action defects; this worker produced no replacement `.mesh`, `.anim`, or texture candidate. The repair handoff is complete for parent review, but WP1 model acceptance remains open.

## Scope and ownership

The approved ticket source is `C:\Users\klimp\Videos\chaos_redux_trailer\records\showcase\unit_fix_plan.md`: common rules at lines 74–79, the full WP1 package at lines 81–145, and cross-cutting section 3 at lines 422–457. Raw evidence is `C:\Users\klimp\Videos\chaos_redux_trailer\records\showcase\unit_defects.json`. The requested `docs\plans\unit_fix_2026-10\unit_s3_report.md` does not exist; this handoff uses `pipeline_report.md`, `geometry_animation_tools_handoff.md`, `texture_tools_handoff.md`, and `per_model_delivery_metrics.json`, plus the parent’s `wp1_evidence` records.

This pass owned only the seven `docs\assets\012_africa\models_3d\<unit>` job roots and this handoff. No runtime `.mesh`, `.anim`, `.asset`, `.gfx`, audio, counter, gameplay, shared tool, lock, skill, job, or manifest source was edited. The parent’s approved `plague_carriers_entity` scale change to `0.75` is parent work; it changed no mesh or animation bytes.

## Route and cost evidence

This was a Blender-only repair of existing models. No Meshy operation, provider balance check, internet download, source selection, ImageGen refinement, or paid call was made. Current-task estimated and consumed Meshy credits are both `0`. The historical plague job records Meshy 7 generation task `01a03d43-63b9-7204-9873-ebafb3c18cd6` and 30 credits consumed; its recorded additional shared-balance delta of 10 credits remains historical and unattributed. No provider result was regenerated or replaced.

The dependency lock schema is `1.0.0` with SHA-256 `CB8D29299776135E33ACB5FED4DA5CF1F3188719704C0D9C81AD6E52A0A51856`; the adapter config schema is `1.0.0` with SHA-256 `788858E3DC9E7D43A1717C419815F23935DC031F7BEEB1D50B13601E8AEB8543`. Adapter health request `a297948ea7c34fed839f30f9b1f5fe6b` reported Blender `5.2.2`, build `d13f752e3b9c` as separately verified by the parent, and `chaosx_blender_hoi4` `1.11.0`. All 36 locked adapter-source checksums matched. The locked `io_pdx_mesh` `0.91.0` compatibility archive matched SHA-256 `508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702`; all three installed patch-file hashes matched, and the health response loaded both mesh and animation exporter functions. The installed extension manifest is `C:\Users\klimp\AppData\Roaming\Blender Foundation\Blender\5.2\extensions\user_default\io_pdx_mesh\blender_manifest.toml`.

The exact callable adapter operations used were `mcp__blender_hoi4__chaosx_blender_hoi4_health` with `{job_id:"gorilla_heavy_infantry"}` and `mcp__blender_hoi4__chaosx_blender_hoi4_inspect_scene` with job `plague_carriers`, source checkpoint `blender/checkpoints/reimport_installed_32e03d669af9c1c4.blend` SHA-256 `1FC9EE0AEEBDD0DCAFD2697C8C483F349D78743689961DD0EEC8AF83516957A3F`, `expected_source_sha256` set to that checkpoint hash, `include_action_channels:false`, `render_previews:false`, `preview_frame:1`, and `runtime_stem:"chaosx_plague_carriers"`; request ID was `b7c83c1d2e844429a50b95b91a5a54fd`. It was read-only and found one mesh object, a 25-bone rig, 25 vertex groups, 74,884 vertices, 25,000 polygons, no zero-weight vertices, and no imported actions. The per-vertex influence distribution was 56,199 vertices at one influence (75.048%), 10,963 at two, and 7,722 at three; normalized weight sums were approximately 1.0. The 75.048% single-influence share fails the WP1 target of under 40%.

The Blender Lab bridge answered a read-only path-summary request. The first response was an empty unsaved scene; the parent’s later live check found the shared session occupied by `mutant_zombies/.../21d_export_batches.blend`, clean and owned by WP3. This worker did not load another file or author in that session. The current blocker is the lack of an exclusive live authoring session and the adapter’s serialized worker lock, not the initial TCP probe. One read-only `inspect_scene` request timed out after the tool call's 1,800-second wait: request `5f73ed5a349447198e82d001b991d803`, job `plague_carriers`, checkpoint `blender/checkpoints/reimport_v4_move.blend` SHA-256 `EB7C3ABEDA071282ECCA0D7155878BE7E7C070D8ABF930EC4FC10E6F33265D02`, action `io_pdx_rigAction`, frames `[1, 11, 21, 31, 41]`. Its request log exists at `docs\assets\012_africa\models_3d\plague_carriers\logs\adapter\5f73ed5a349447198e82d001b991d803.json`; the result log is absent. After timeout, process inventory showed only the shared Blender Lab process, PID `52956`; no adapter worker remained, and this worker did not start or terminate that shared process. No result or contact finding is claimed for this request.

## Baseline and source references

The parent’s installed-byte baseline is `docs\plans\unit_fix_2026-10\wp1_evidence\before_inventory.json`, `before_audit\summary.json`, `before_audit\motion_reports.json`, and `measured_baseline_compact.json`. It reports all seven WP1 meshes blocked and, across their 56 registered actions, 5 pipeline passes and 51 blocked actions. A pipeline pass on a specific action does not close its semantic ticket. `per_model_delivery_metrics.json` and the package jobs remain the source for each action and geometry detail; this worker did not rerun that audit.

Parent reports the shared DDS compression/mipmap delivery and audio mastering tranche complete. Those existing DDS files and audio files were preserved. No model-specific specular mask, prop-island paint, normal rebake, or sound change was made here. Sound definitions and candidate installation, bespoke counters, entity/runtime wiring, and live-game review remain parent-owned; this worker created no audio or counter asset.

The offline wiki pages read were `paradox_wiki\Entity modding - Hearts of Iron 4 Wiki.md` SHA-256 `74FF51B8EA0924281EB1C067300B52DC373EA9D112341BBB9C34FCB1A11D2D6A`, lines 19–43 for `.gfx` mesh registration and entity scale and lines 171–184 for animation `.asset` references, and `paradox_wiki\Graphical asset modding - Hearts of Iron 4 Wiki.md` SHA-256 `F8E3D4AD382F4E5F8E170492A484D090BAD62E3711CABFB5D3BF84E58AB32DD9`, lines 32–75 for sprite paths and frame declarations. That graphical-asset section does not define 3D material compression. The installed `standardfuncsgfx.fxh` normal decode at lines 311–318 uses tangent X from G and tangent Y from negative A. The installed vanilla `ENG_infantry.mesh` reference is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\models\units\ENG_infantry.mesh`; parent calibration records source height `7.352` and entity scale `0.8`. `forest_giants` retains the plan’s deliberate `1.1–1.69×` scale relationship; this worker made no scale change. The installed vanilla `asian_infantry.mesh`, `infantry.gfx`, and `units_infantry.asset` remain the recorded material, animation-binding, and entity-scale precedents. No installed markdown documentation file provided a more detailed 3D model-format chapter.

## Plague scale and current-hash contact evidence

`docs\plans\unit_fix_2026-10\wp1_evidence\plague_scale_rest_bounds.json` SHA-256 `94246AA038198229B3B0531BDFD0D64AA8EEE4FE758EB327518FD799B7FB60BB` binds its measurements to installed mesh SHA-256 `32e03d669af9c1c4466e345171861fe568e01a96fb995b26c0a6589af7cd98e8`. In PDX Y-up coordinates, source bounds are minY `0.0`, maxY `8.26848220825`, and height `8.26848220825`. Scale `1.0` gives effective height `8.26848220825`; the parent’s `0.75` scale gives `6.20136165619`, which rounds to the ticket comment’s `6.201362`. The rest minimum remains at ground, `0.0` before and after uniform scale. This is a rest-bounds proof only.

The existing `export/v4/chaosx_plague_carriers.mesh` is byte-identical to the installed mesh. All eight `.anim` files under `export/v4` are byte-identical to their installed counterparts; no final candidate was copied or synchronized by this worker.

| Runtime action | Installed SHA-256 and matching `export/v4` file |
|---|---|
| attack | `1AF0715EAA9B386ACAC029761606AA0A349C1AA400191FBBE55DB66266495F67` |
| death | `BD9EDD1AE0EE5CC8AA1BDC32E05BE08D6FF25D9272A605CEAFD2587778AD71A1` |
| defend | `BBBF3FCFAE89B74E9EAF056F5566A7230810C8EF0013831C756E74E577A7D921` |
| idle | `B0FECBBFE3856A2AC901D3FF6001FE882B3888D6CD0A9324F13BC19EC379148F` |
| move | `BE9518A058B7DD17B6D9DA2A20223B870E98B5624BD25A28F4F054D8940A48F4` |
| retreat | `46B371C5655BD28991282DE048CD1877CEC0E828290410F40DAC2235EFDC35C0` |
| support_attack | `35B8186B8F944F14F0A5CCAB76237FE91B16B497EFA89EDCE96BA1499E6ECA48` |
| training | `6D7F5C01A209C7A18B42BBBFF71DA134D17AF8FA349494DED496BA249A9F3074` |

The exact installed `idle` and `move` native reimport receipts are `validation/reimport_v4_idle.json` and `validation/reimport_v4_move.json`, with proof checkpoints `blender/checkpoints/reimport_v4_idle.blend` SHA-256 `2A7C9B723115C29F246A348A115C44EE1FEA20891AF94F734F0D2BB0B86D7DC3` and `blender/checkpoints/reimport_v4_move.blend` SHA-256 `EB7C3ABEDA071282ECCA0D7155878BE7E7C070D8ABF930EC4FC10E6F33265D02`.

The reimport receipts’ whole-mesh `ground_contact_z` samples, multiplied by the new entity scale `0.75`, yield:

| Action | Frame | Whole-mesh minimum before scale | Whole-mesh minimum after scale |
|---|---:|---:|---:|
| idle | 1 | 0.00401469 | 0.00301102 |
| idle | 21 | 0.00401531 | 0.00301148 |
| idle | 40 | 0.00401410 | 0.00301058 |
| idle | 60 | 0.00401436 | 0.00301077 |
| idle | 80 | 0.00401377 | 0.00301033 |
| move | 1 | 0.00400500 | 0.00300375 |
| move | 11 | 0.00400940 | 0.00300705 |
| move | 21 | 0.04547143 | 0.03410357 |
| move | 31 | 0.00401044 | 0.00300783 |
| move | 41 | 0.00401234 | 0.00300926 |

These are whole-mesh lower bounds in source units, not labeled hoof or basket vertices. The move frame 21 lower bound is `0.03410357` after scale, exceeding the ticket’s 0.01-unit contact tolerance if it is a support point; its component is unidentified. Thus these readings do not establish hoof contact, basket-pole clearance, or a contact pass. The older per-hoof report uses move action SHA-256 `E5388D3BAC97758A3DC6B510F21473F00D171292D3AF7B5A9DD8772BF0C06167`, which does not match the current installed move action SHA-256 `BE9518A058B7DD17B6D9DA2A20223B870E98B5624BD25A28F4F054D8940A48F4`; that older report is stale for current-action acceptance. No current per-part basket clearance proof was found.

## WP1 ticket dispositions

`Blocked` below means no accepted replacement was authored. The shared authoring session was unavailable for this package while owned by WP3, and broad automatic topology cleanup would violate the approved bounded-repair rule. Existing source and runtime files remain intact.

### `gorilla_heavy_infantry`

1. Support attack frames 60–90: blocked; Hips yaw/pitch correction, pelvis interpolation, head clearance, and shoulder/elbow pound keys require manual review and authoring.
2. Attack easing and recovery/seam: blocked; no attack keys or return frames changed.
3. Idle breathing, weight shift, shoulder roll, and hammer-tip tap: blocked; no idle keys changed.
4. Fur/leather/iron specular recipe: inherited shared DDS delivery only; this pass did not make or audit a new class-masked map.
5. Manifold gate and mesh re-export: blocked; the parent baseline still marks the mesh blocked, and no exact local patch was approved or applied.

### `pan_sappers`

1. Sabotage flask visibility/throw, shovel back slot, and cleaver hip attachment: blocked; no Blender-authored geometry, controls, or keyed visibility was added.
2. Fuse pull/arm/throw/crouch/return attack under 3 seconds: blocked; no action keys were authored.
3. Breathing, ear/tail flicks, weight shift, and glance: blocked.
4. Support attack return frames and `deploy`/`supply_load` aliases: blocked.
5. Thirty-frame two-plant move loop and sound timing: blocked; no current-action foot-contact evidence was authored.
6. Inner-thigh/underarm map rebake and manifold repair: blocked/inherited DDS only; no map bake, exact geometry patch, or export was made.

### `stone_cohorts`

1. Stone/metal specular mask and alpha recipe: inherited shared DDS delivery only; no model-specific candidate or audit was made here.
2. Halberd grip constraint, closed hand, thrust, wind-up in-betweens, turn easing, and height drift: blocked; no rig or action keys changed.
3. Two-plant move loop and sound timing: blocked.
4. Halberd island repaint and manifold repair/export: blocked; no prop-texture or mesh candidate was produced.

### `riverborn`

1. Attack/support-attack yaw, spear chest clearance, lunge/throw behavior: blocked; no weapon control/contact or action changes.
2. Attack step easing and support return frames: blocked.
3. Cloak/feather loop repair and manifold gate: blocked; no exact face/vertex patch or export.
4. Skin/feather/water-cloak/bronze specular and spear/shield atlas repack: inherited shared DDS delivery only; model-specific materials were not reworked here.

### `forest_giants`

1. Attack wind-up tilt/rotation, hold, and ground follow-through: blocked; no attack keys changed.
2. Axe head enlargement, haft thickening, and bound-log geometry decision: blocked; no component geometry was modified.
3. Bark/leaf specular and manifold gate: inherited DDS delivery only; mesh remains blocked in the parent baseline.
4. Showcase re-film after in-place attack: not performed; no game was launched and capture remains parent/user-owned.

### `oracle_recon`

1. Two-plant move loop and pause removal: blocked; no action keys changed.
2. Idle yaw/head scan and loop: blocked.
3. Attack/support return frames, staff aim, and skull-node locator: blocked; no locator or action was created.
4. Plate/skin manifold repair, staff/skull island, and material review: blocked/inherited DDS only; no exact topology repair or export.

### `plague_carriers`

1. Entity scale `1.0`→`0.75`: parent completed the entity edit. Source height `8.26848220825` and effective height `6.20136165619` are verified. The current-hash whole-mesh samples above do not identify hoof or basket components, so move/idle contact acceptance remains blocked.
2. Attack chest/pelvis pitch and weight shift; idle head/hip/breath/tail/ear cycles: blocked; no action authoring. The parent baseline marks move and attack blocked.
3. Tangent-normal rebake: not performed; existing DDS delivery was preserved and no new normal candidate was produced.
4. Neck/head/leg weight smoothing with rigid cargo: blocked; current hash-bound inspection reports 75.048% single-influence vertices, above the under-40% ticket limit. No weights were changed.

## Remaining parent work and handoff files

The parent should retain all existing runtime model/action bytes until a full replacement candidate passes the required geometry, semantic-action, material, weight, export, and reimport checks. The parent owns the `0.75` entity scale, runtime `.asset`/`.gfx` wiring, audio and counter surfaces, final integration, and live-game review. The user owns live in-game consumer validation. No runtime synchronization or copy operation was performed by this worker.

Files written by this worker: `docs\plans\unit_fix_2026-10\wp1_model_worker_handoff.md`. Read-only adapter evidence added under approved job roots: `gorilla_heavy_infantry\logs\adapter\a297948ea7c34fed839f30f9b1f5fe6b.result.json` and `plague_carriers\logs\adapter\b7c83c1d2e844429a50b95b91a5a54fd.result.json`; the latter proves geometry/skeleton import only. The move inspection request timed out without a result and is not acceptance evidence. No source-to-runtime checksum synchronization, `.mesh`/`.anim` export, Blender source edit, texture derivation, audio production, or counter production was performed.

Meaningful checks completed: lock/config/checksum verification; adapter health; exact actual `.mesh`/`.anim` SHA comparison for plague `export/v4` versus installed runtime; native current-byte idle/move reimport receipt review; installed PDX rest-bound and scale crosswalk; and one read-only adapter scene inspection of the exact installed-mesh reimport checkpoint. No modified candidate existed for multi-view visual review. New model exports and live action/deformation checks remain blocked by the shared WP3 authoring session and the serialized adapter worker lock.

# Autonomous Robot 3D model production handoff

Status: **production package complete; parent runtime wiring and live consumer validation pending**.

The deterministic package root is `docs/assets/shared_robot_system/models_3d/autonomous_robot/`. The accepted generic retro-WW2 automaton retains its complete biped, two independent integrated forearm machine guns, visible barrels/muzzles, ammunition feeds and rear housing, grounded feet, olive/steel/bakelite palette, and provider-neutral identity.

## Provider lineage and cost

- Legacy Meshy generation `01a001f1-9a6f-73c0-a45a-88082c95421c`: 30 credits. Future regeneration uses Meshy 7.
- 300k remesh `01a0040a-c4cb-7dd8-9aa3-952c2a6f206d`: 5 credits; rejected at 310,853 faces.
- 280k remesh `01a00422-4450-762d-8fbd-db589e6e9bf9`: 5 credits; accepted at 290,165 faces.
- Rig `01a0043b-dc34-7795-a542-7d9657a3820e`: 5 credits; succeeded with 24 bones.
- Six successful custom animation tasks: 18 credits total. Failed retreat task `01a00442-7010-787d-b3cb-48e9e1972191` was refunded.
- Final observed balance: 156. Attributable job spend: 63 credits.

Exact tasks and the full ledger are in `validation/credit_ledger.md` and `provider/`.

## Blender, calibration, and QA

- Blender 5.1.2 build `ec6e62d40fa9`; adapter `chaosx_blender_hoi4` 1.2.2; io_pdx_mesh 0.91.0 checksum verified.
- Vanilla reference: `western_european_infantry.mesh` plus `units_infantry.asset#infantry_rifle_entity`.
- Vanilla source height `7.3518247977`; final source height `7.3518247604`; entity scale `0.8`; effective runtime height `5.8814598083`; forward `-Y`, up `+Z`, feet at `Z=0`.
- Final working geometry: 29,971 triangles, 15,123 vertices, zero degenerate/non-manifold faces, zero negative scales, zero zero-length normals. The 1,973 open boundary edges are recorded mechanical panel/component seams.
- Weight sanitizer request `b7e61752fd684c5e8dbd2529fb5c92f4` removed 8,568 influences. Final working mesh has zero vertices over four influences and zero zero-weight vertices.
- Parent accepted `previews/action_phase_contact_sheet.png`. All eight real skeletal actions are 24 FPS and contain no scale F-curves.
- The first death reimport exposed late airborne ground contact. Allowlisted root-only correction request `a128ea895c824a4da6be2a9ce02c2031` preserved body motion and corrected all 73 frames. Final reimport request `40aa065075e447bc8f4d58f4c1f3c30f` remains within approximately `1.2e-5` of ground.

## Runtime staging and hashes

Staged evidence root: `runtime/gfx/models/units/autonomous_robot/`.

| File | SHA-256 |
| --- | --- |
| `autonomous_robot.mesh` | `694352c5778e608120474773728317efa776572a2ebe0175f70b67ae7825f3c5` |
| `autonomous_robot_idle.anim` | `ff043370ea408294a3f0e069c0f17542ce5dac20f9ee4388a9258dd9de4a060f` |
| `autonomous_robot_move.anim` | `bd86173d096c45b4cb8a4b292bd01ce2d3a842a8b3270afe75747b8258489fbd` |
| `autonomous_robot_attack.anim` | `5b1f24b1b87d3baf9242e42da6164414dc61ffed0bf4023369f00fe2356f1e0a` |
| `autonomous_robot_defend.anim` | `b76bc8952e04d9348030653069f1c2b609f66d082eda3345f9023014c71dcb1a` |
| `autonomous_robot_support_attack.anim` | `652f2f04442fdc0d2c1c29120f42f10f88c957376cdc50ebfc448a995a10542b` |
| `autonomous_robot_retreat.anim` | `ef427279c18abb21cd9404d0ab145b9106d55957770efb38f5d84272166b1985` |
| `autonomous_robot_training.anim` | `c48167ec8e6c57b3a7490fb218dda46bfc23527c6e79fb231bafb8d37c5b3295` |
| `autonomous_robot_death.anim` | `b9e97aa5f6466f7bfa3e17d3020e30c7506ea1b4c40ae9afeabcf932ba9bfb32` |
| `autonomous_robot_diffuse.dds` | `48f9e5488deb14cd2d058c907a9f00bd8c4a4d09c887731334d7ce875b117922` |
| `autonomous_robot_normal.dds` | `da1253f4def8caa054d2fc84f4478f8b77d432eff94421c919e72d90ed72e65a` |
| `autonomous_robot_specular.dds` | `ca4cfd87de234b63480ba32d07c21d45d6d2a1214ea27ca84b78ebb79fafef1f` |

Proposed identifiers are `autonomous_robot_mesh` and `autonomous_robot_entity`. Apply entity scale 0.8 exactly once. The parent owns copying these files to the mod-root equivalent paths and all `.asset`/entity bindings.

## Sourced sound package

Six mechanically derived OGGs are under `evidence/audio/derived/`: selection, movement servo, idle mechanical loop, impact/footfall, dual-MG attack, and death. Sources are CC0, CC BY-SA 4.0, CC BY 4.0, or public domain and are preserved with page/direct URLs, creators, hashes, transformations, and attribution in `evidence/audio/source_plan.md` and `source_ledger.md`.

Action synchronization proposed to the parent:

- selection starts immediately on acknowledgement;
- movement servo loops across move frames 0-26; impact/footfall one-shots at frames 1, 14, and 27/loop boundary;
- idle loop spans idle frames 0-97;
- dual-MG burst starts at attack frame 8 and continues through the visible recoil sequence to the action end;
- support attack may use the same licensed burst beginning at frame 8;
- armored impact uses the impact source at a hit phase selected by the parent consumer;
- destruction starts at death frame 1, with collapse phases at frames 37 and 55.

The runtime sound, soundeffect, wrapper, and entity event definitions remain parent-owned.

## Counter and remaining parent work

Accepted counter art handoff: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/autonomous_robot_counter_art_handoff.md`. It contains both final DDS strips, exact consumers, frame counts, palette/reference evidence, and hashes. The parent must register `GFX_group_autonomous_robot_icon`, `GFX_unit_autonomous_robot_icon_medium`, and `GFX_unit_autonomous_robot_icon_medium_white`.

No gameplay, localisation, interface GFX, `.asset`, entity, sound definition, decision, event, or spreadsheet file was edited. No in-game completion is claimed. No visual, action, audio, or counter fallback remains in the package; only parent-owned wiring and live validation remain.

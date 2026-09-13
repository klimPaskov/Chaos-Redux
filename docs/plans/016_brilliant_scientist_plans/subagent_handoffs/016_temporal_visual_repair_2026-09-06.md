# Temporal Guard visual and export repair — 2026-09-06

Status: `in progress`; native culling isolation has confirmed the missing-looking regions, but the existing canonical mesh and its damaged previews are not visually accepted.

## Scope and acceptance basis

The parent assigned Blender-only repair of the existing Temporal Guard package under the accepted `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` and the user's Final Completion Plan section 8.
Existing geometry, identity and required components must be preserved; manual rig, weight, action, material and export repairs are allowed without regeneration.
This handoff supplements `2026-09-05_temporal_guard_runtime_closure.md` and does not promote its provisional visual claims.
No Meshy operation, key check, balance query, provider retry or credit spend is needed or performed in this repair.
New provider calls: **0**; estimated and consumed credits: **0**.
Runtime copies, entity/asset/GFX definitions, sound wiring, gameplay and commits remain parent-owned.
Shared adapter integration and dependency relocks are coordinated by the parent and `/root/alien_stream_repair`.
This worker owns only the parent-approved standalone visibility, winding and tiny-seam helper modules/tests; it does not edit the shared dispatcher, MCP server, client or lock.

## Preserved sources and baseline

Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard`.

| Source | SHA-256 | Role |
| --- | --- | --- |
| `blender/checkpoints/03_rig_approved.blend` | `E9D2C8B100A5764231CC2F3793B7D3A2C907763FEDD45C999B6039640129BD49` | Immutable selected identity/geometry reference |
| `blender/checkpoints/runtime_support_attack_grounded.blend` | `52BE347032FBF23F1AC9B5D08F4642C41853CCFECCA389E0AD42C62AE1F7ABF2` | Existing authored support action candidate |
| `blender/checkpoints/runtime_retreat_grounded.blend` | `278E729370459FDDBCED8A3B5D69017329B0C890E1B0F715A056FC2B1D1DBF22` | Existing authored retreat action candidate |
| `export/mesh/chaosx_temporal_guard.mesh` | `EA0C72AAC11CDA1B1A46CF74C6DC6A38EF3DC9833EC35DFE984E82D7FFD59516` | Existing canonical bytes; visual acceptance withdrawn |
| `blender/checkpoints/reimport_reimport_runtime_support_attack_grounded_actual.blend` | `662B1D4FB6CF58529E70DB931349A05D0DE0932261AA22A702B461E1CF45A2A1` | Actual canonical/support byte reimport used for diagnosis |

The source working mesh is `char1.001` with 14,997 vertices and 30,000 triangles.
The canonical reimport mesh is `char1.002` with 38,906 UV/normal seam-split vertices and the same 30,000 triangles, bound to the 24-bone `io_pdx_rig`.
Position-weld diagnostic evidence in the inherited reimport reports returns 14,997 vertices, 38 boundary edges in 10 tiny closed boundary loops, no non-manifold edges and no degenerate faces.
The working source and canonical reimport share bounds `[-2.9375689,-0.8063117,-0.000000593]` to `[2.9375684,0.8063122,7.3518238]` before pose evaluation.
The source has no visually missing torso or limb regions in the new inspection render.
The canonical reimport has large apparent cutouts in those regions and cannot be passed on structural counts alone.

Before evidence (job-relative):

- `blender/previews/visual_repair_source_20260906_three_quarter.png` and `_front.png`, adapter request `89aabebe2adc4b018c3fc65665963329`.
- `blender/previews/visual_repair_canonical_20260906_three_quarter.png` and `_front.png`, support frame 24, request `f815ce14cee7491b8c27b773884545ea`.
- Parent-reviewed existing `reimport_reimport_runtime_support_attack_grounded_actual_frame_{001,030,060}_three_quarter.png` remain failed visual evidence, not acceptance.

## Material and stream diagnosis

The diffuse DDS is 1024×1024 legacy BGRA, with all 1,048,576 alpha samples equal to 255.
Its SHA-256 is `82071750202D2435542841E8354313DDB4B46BFD4B23CEBA0308CE4DE6DB4044`.
The canonical material's Principled Alpha socket has no incoming link.
The installed locked io_pdx_mesh importer explicitly enables `use_backface_culling`, keeps diffuse-alpha linking commented out, and maps packed specular blue to metallic and alpha to roughness.
These facts exclude missing diffuse alpha as the established cause; they do not alone prove the remaining cause.
Retained earlier `tg26_material_repair` and neutral normal/specular diagnostic renders still show the same holes and have not been selected as a fix.
They remain preserved prior-attempt artifacts whose names and dates do not establish acceptance.

Raw canonical text at `export/mesh/chaosx_temporal_guard.txt` contains 116,718 position floats (**38,906 vertices**), 90,000 triangle-index entries (**30,000 triangles**), and maximum referenced vertex index **38,905**.
The text SHA-256 is `D9C86D4AC3A260347C77960523A74D6E44CD7F045AEE622D83FD1F5F94EF24B2`.
A numeric winding-versus-summed-normal diagnostic found 29,999 positive and one negative dot products, with none zero.
This does not establish outward orientation or visual acceptance.
A separate read-only adjacency diagnostic rounds coincident positions to six decimal places, recovering exactly 14,997 positional vertices and 45,019 geometric edges.
It finds 44,351 correctly opposed shared-edge pairs, **630 same-direction shared-edge pairs**, 38 boundary edges and zero non-manifold edges.
The same-direction pairs establish inconsistent orientation between adjacent patches while preserving the full triangle set.
The paired native culling evidence confirms that culling hides those inconsistent regions: original and canonical opaque-clay culling-on views retain the holes, while culling-off views show the full body.
An index-entry count is not a maximum index value: 90,000 entries alone do not violate a 16-bit vertex-addressing envelope when the largest referenced index is 38,905.
The locked extension does not expose an explicit 65,535 index-entry-count limit in its exporter implementation.
Any additional entry-count partition budget is conservative pipeline policy, not a demonstrated engine limit.
The failed newer export with 90,000 actual vertices is a separate vertex-cap failure.
Final binary stream validation and any selected partition are pending the corrected depth-aware adapter parser and skeletal partition operation.

The parent approved `.tools/3d_pipeline/adapter/material_visibility_probe.py` with `.tools/3d_pipeline/tests/test_material_visibility_probe.py`.
The helper requires source/action hashes, exact mesh/rig/action names, one bounded frame and 1–3 exact views.
It reports material scalar settings, Alpha/Transmission defaults and graph links, normal chains, image data/alpha/color-space state, and posed world-space directional front/back/edge counts.
It renders original materials and opaque clay with culling on/off using temporary material-slot bindings, then reloads the untouched checkpoint with script execution disabled.
It never saves or exports Blender data.
Seven pure guard tests pass.
Native canonical probe request `eea666dd922045e09d96e59ca3d3126b` and immutable-source probe request `130df3bed7034198afc52050109c1a39` pass on fresh locked adapter 1.10.22 with identical before/after source checksums.
The source's material has culling disabled; the canonical reimport material has culling enabled.
Both have Alpha default 1 with no link and Transmission Weight default 0 with no link.
The parent has reviewed the canonical culling pair and accepted it as decisive diagnosis, not a final fix.
Job-relative paired screenshots are `blender/previews/vr06_visibility_{canonical,source}_opaque_clay_culling_{on,off}_{front,three_quarter}.png`.
The complete material graph, directional face counts and screenshot checksums are in `evidence/20260906_repair/vr06_visibility_{canonical,source}.result.json`.
Disabling runtime culling is expressly not the selected repair.

The parent approved a strictly orientation-only correction with exact hash/mesh guards and no final weld, face deletion or face addition.
The new standalone `mesh_winding_repair.py` planner/test checks orientation consistency and outward signed volume, preserves UV/normal corner associations, and blocks ambiguous open/non-orientable components.
Nine pure tests pass, including all 16 reversed-face patterns of a tetrahedron and a genuinely non-orientable Möbius-strip rejection fixture.
Read-only native original-source inspection `9c4455ebdaf84257a0baccc54a62bddb` and canonical inspection `1ef63390854c4679b80e0b7e40ba20e3` establish the same four orientation-conflict face pairs: 18604/18855, 18679/18842, 18777/19083 and 19083/19254.
The original source has 14,997 vertices and 14,997 exact unique positions, so the defect exists in original indexed topology and is not an invented UV-seam/rounded-position adjacency.
The canonical source-index graph is split by export attributes, but its exact-position graph reproduces the original source's face numbers and conflict coordinates.
Complete evidence is `evidence/20260906_repair/vr06_winding_{source,canonical}.result.json`.

### Explicitly approved minimal seam

After reviewing the full `evidence/20260906_repair/vr06_seam_proposal.json`, the parent approved exactly three knee faces (18842, 18855, 19083), five coincident attribute-vertex duplicates and the recorded outward orientation proposal.
The accepted preservation criterion is unchanged spatial surface, not byte-identical index topology.
No final caps, position edits, new/deleted faces, positional weld or silhouette changes are authorized.
The duplicate map is 24472→38906, 24525→38907, 24527→38908, 24632→38909 and 25082→38910.
Attribute vertices become 38,911; exact unique positions remain 14,997 and triangles remain 30,000.
Every original corner's position, UV, source normal before orientation and corresponding bone-weight/joint values remain exact copies in the pure numeric proposal.
The body contains 29,997 faces and becomes coherently orientable after the approved seam; its conservative hypothetical-cap signed-volume interval is [8.44893564595355, 8.600957473331544], entirely positive.
The hypothetical cap-area upper bound is only 0.200114% of body area; no hypothetical cap is written to the model.
The three-face open patch uses the explicitly approved outward body neighbors 18604, 18679, 18777 and 19254, with area-weighted normal alignment 0.9870052804325493 and individual alignments 0.5842, 0.9408 and 0.8972.
The exact 12,195 reversed-face list has SHA-256 `8917252F7EE785DBF65B9ACB9BB9727EC55CECA3EBDDF2B5E395AD463946DCCD`.
The standalone helper `mesh_winding_seam.py` and ten pure regression tests implement this guarded contract, including actual canonical-byte invariants and a repaired numerical plan with no remaining flips or shared seam vertices.
All ten tests pass; native mutation/save/reopen, copied-vertex deformation and fresh culling-on export/reimport approval are still pending.
The prepared native request is `evidence/20260906_repair/vr06_apply_seam.request.json`; no repair checkpoint has yet been produced or approved.

An additional evidence defect was found in the old renderer: `render_previews` frames unevaluated rest vertices while death frame 53 is a prone evaluated pose extending approximately 7.9 source units forward.
That old death screenshot is cropped, and older action previews also have unresolved pink textures.
These previews are not acceptable final motion/material evidence.
The parent approved evaluated-pose framing inside preview rendering only; adapter 1.10.22 uses evaluated bounds there without changing calibration measurements.

## Calibration retained

Vanilla reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`.
Entity reference: `gfx/entities/units_infantry.asset#infantry_entity`, scale **0.8**.
Mesh definition: `gfx/entities/infantry.gfx#generic_western_european_rifle_infantry_mesh`.
The read-only measured vanilla display mesh is `polySurface106`; collision-only `pCube1` is excluded.
Vanilla source geometry height is 7.351824797689915 and its effective entity height is 5.881459838151932.
Custom source height is 7.3518242835998535, with effective height 5.881459426879883 at the same single entity scale.
Axes remain +Z up and −Y forward, with source ground approximately zero.
Evidence: `blender/reports/chaosx_temporal_guard_prepare.json` and `blender/reference/western_european_infantry.mesh`.

## Required action inventory and proposed parent mapping

All paths below are job-relative and all hashes were rechecked from the existing bytes in this repair.
These are the preserved candidates, not a final visual acceptance declaration.
No skeleton changes or semantic aliases have been introduced.

| Runtime state/action | Selected existing file under `export/anim/` | Frames / FPS | SHA-256 |
| --- | --- | --- | --- |
| `idle` | `chaosx_temporal_guard_idle.anim` | 1–97 / 24 | `C2BE045CF4079A647E012EFF8145B07CFE69CF3018E9F616FC898E90EF603563` |
| `move` | `chaosx_temporal_guard_move.anim` | 1–32 / 24 | `E3839142F49EA48A5182DB4145CAF04A462EAFEE9ABB8F39B42FF53DE947DAE4` |
| `attack` | `chaosx_temporal_guard_attack.anim` | 1–60 / 24 | `F22DF39A34FADEF4ECA718102E966EA7AC704E3B3D89244D715D619CE406B3DF` |
| `defend` | `chaosx_temporal_guard_defend.anim` | 1–84 / 24 | `F468CB8B13041D18FC8D894557F82E70E3E31B79E0D15B2C53EBABC582655128` |
| `entrain` | `chaosx_temporal_guard_entrain.anim` | 1–40 / 24 | `E130DDEF7FD1650C6D62E44F496F44CAF89784BF3575AA402306AD55AD6D7FEE` |
| `death` | `chaosx_temporal_guard_death.anim` | 1–53 / 24 | `409714D9C162A0A2C072781327BBA73869021BC5CAA115A732EBFDCFE4494133` |
| `temporal_anchor` | `chaosx_temporal_guard_temporal_anchor.anim` | 1–65 / 24 | `CF35348B9AE481D606240EFCA2722ACBB5CDACB4F5A858FBACAC4A37F28A715A` |
| `synchronization` | `chaosx_temporal_guard_synchronization.anim` | 1–104 / 24 | `1DE85573412CE3A4A121AC6D4B6A5178EC308B3B37FD1FF1F4047E61B331624B` |
| `support_attack` | `chaosx_temporal_guard_support_attack_grounded.anim` | 1–60 / 24 | `5591274702F3A998ED02F281CBCF975A405C320DCF0E532358289B5589BBB917` |
| `retreat` | `chaosx_temporal_guard_retreat_grounded.anim` | 1–32 / 30 | `03CE8BC9EF27671CCF9323422A26841C2A058A739D6CF23A3309AA802425A972` |

Proposed mesh/entity IDs remain `chaosx_temporal_guard_mesh` and `chaosx_temporal_guard_entity` for `common/units/016_brilliant_scientist_project_forces.txt#temporal_guard`.
Support ready/aim/pulse/recoil/recovery phases are 1/12/24/36/60; retreat inspected phase candidates are 1/14/32.
The support action is a non-firearm temporal action: do not bind a muzzle flash, gunshot, firearm tracer or generic firing animation.
Temporal-anchor effect proposal: a core/hand-linked temporal pulse at frame 44.
Synchronization effect proposal: a distinct linking pulse at frame 52.
Support effect proposal: a brief palm/core temporal pulse at frame 24 with recovery to frame 60.
These effects remain proposals until the parent selects exact engine-supported locator/effect consumers; this worker has not silently wired them.

## Sound and counter continuity

Preserved sound source/derived bytes and attribution live under `audio/originals/`, `audio/derived/` and `audio/provenance.md`.
The inherited roles cover movement, metal contact/attack, impact, temporal special action, death and a proposed selection/ambient bed.
The selection/ambient source is `60Hz_hum_square.ogg`; its primitive-waveform identity needs review against the project's ban on primitive-waveform final audio and must not be silently accepted merely because it is public domain.
A distinct sourced retreat cue is absent from the inherited handoff.
These are actual sourced-audio package gaps; this worker preserved the files and notified the parent rather than synthesizing replacements.
Per-subunit selection audio is only required where supported: lack of a supported consumer is documented as a limitation, not by itself a blocker, and global voices must remain untouched.

The job's old `counters/gfx_handoff.md` and manifest are stale about counter absence.
Accepted counter evidence is `016_final_generic_counter_completion_2026-09-01.md`, not the old blocked brief.
Temporal large DDS: `gfx/interface/counters/divisions_large/unit_temporal_guard_icon.dds`, 152×42 with two 76×42 frames, SHA-256 `50622212016AC090ADD2D076E3E0B40896B932BCDA6A124083D0B1D0DDBF7C78`.
Temporal on-map DDS: `gfx/interface/counters/divisions_small/onmap_unit_temporal_guard_icon.dds`, 60×12 with two 30×12 frames, SHA-256 `995FF164E56AA3BBA23315203EBFA8D72CBCCF92D74F66485D718BA42BAFF8D7`.
Tokens include `GFX_group_temporal_guard_icon`, `GFX_unit_temporal_guard_icon_medium` and `GFX_unit_temporal_guard_icon_medium_white`, with parent-owned registration in `interface/016_brilliant_scientist_generic_counters.gfx`.
Exact vanilla infantry counter definitions, DDS references, palette samples, source PNGs, processed frames and DDS roundtrip evidence are retained in that dated accepted handoff and `docs/assets/016_brilliant_scientist/generic_counter_package/`.
No replacement art or runtime counter edit was made during this repair.

## Dependency and validation evidence

Initial locked route health succeeded at adapter 1.10.21 with Blender 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh 0.91.0 and all required import/export operators loaded.
Health request: `d20160c240ce43f591b35ac916ead546`, with job adapter receipt under `logs/adapter/`.
The separate 127.0.0.1:9876 socket probe succeeded; no Blender launch or process replacement was required.
The checksum-locked extension archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
All nine adapter source hashes were independently checked against the selected 1.10.22 lock before native probe calls.
That lock snapshot has SHA-256 `84BA72A9E01527E59F5C96F9DAE7F25357BD8593A1FF392C44493C5F5FE455A7`.
The already-running app MCP health still reported adapter 1.10.21, so new calls use a fresh instance of the repository-owned locked wrapper through `BlenderAdapterClient` rather than accepting stale tool exposure as current health.
Fresh 1.10.22 health request `b8816f2c4dca49858988ff9334eff5c0` passes with Blender 5.1.2 and all required extension operators loaded.
Exact structured requests and fresh receipts are retained under `evidence/20260906_repair/vr06_*.request.json` and `.result.json`.
Fresh 1.10.24 health request `8892b7ebec5b4db095581605f5b080d7` passes; its lock SHA-256 is `1EDF5E73DD129E7C59A976F08F56EBCC9F444D7A612131409242BDA9CE552207`.
The parent is integrating the standalone approved seam route; every subsequent native call remains gated on the matching current source hashes and schema.
No live-game test was run or claimed.

## Outstanding acceptance

- Native application of the approved coincident-vertex seam/winding correction, exact protected-data preservation, save/reopen and deformation proof, and reviewed culling-on after screenshots.
- Corrected actual-byte stream validation, selected final mesh checksum and ten-action reimport/contact/semantic review against that exact mesh.
- Reconciled job manifest and final parent runtime mapping.
- Inherited modern-source artwork/ImageGen authorization lineage and complete historic provider-credit receipts remain unresolved; this repair does not fabricate or retroactively establish them.
- Parent-owned sourced retreat/primitive-waveform audio resolution and exact temporal-effect wiring remain outside this worker's mutation scope.

No geometry regeneration, static substitution, omitted required action or unapproved identity simplification has been made.
The package is incomplete until the outstanding acceptance items are resolved or explicitly recorded as blocked by the parent.

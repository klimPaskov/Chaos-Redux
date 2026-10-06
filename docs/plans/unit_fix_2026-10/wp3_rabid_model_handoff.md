# WP3 rabid_zombies model repair preflight

Status: production repair is blocked pending the parent’s explicit “Blender slot granted” message. This handoff records read-only readiness evidence only; no Blender or provider operation has run.

Scope is limited to the rabid_zombies model source, topology, materials, rig weights, actions, and model-package evidence under docs/assets/002_zombie_outbreak/models_3d/rabid_zombies. The parent retains runtime installation and wiring. The separate WP3 audio owner retains sourced voice/contact work. This preflight does not complete sound or counter requirements.

## Accepted repair target

The authoritative ticket is the rabid_zombies entry in C:\Users\klimp\Videos\chaos_redux_trailer\records\showcase\unit_fix_plan.md, with its common rules and section 3 gates. The ticket requires a planted standing frantic idle of at least four seconds with a closed seam and peak_motion above 0.8; a move cycle that matches its seam and contains exactly one left and one right plant in a 1.0–1.5 second cycle; a forward lunge in place of the back kick, with UpLeg extension no more than 30 degrees behind the hip during frames 65–90 and the 3.40-second contact on the reach; localized Hand/wrist/ForeArm weighting; source-derived suit, collar, torn-sleeve and blood color detail; and manifold geometry. The idle’s existing parser pass does not meet the ticket: it is a 57-frame, 1.9-second imported mid-stride walk pose.

The required calibrated reference remains the installed western_european_infantry.mesh with infantry_rifle_entity. Prior WP3 route evidence records source height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, up +Z, and ground contact at z-min. Preserve this source height and apply the entity scale once; no pose or entity rescaling is authorized.

The inherited WP3 plan additionally requires a 512 BC1 diffuse, 256 BC3 specular, full mip chains, local material provenance, a 60-degree native smoothing review, exact-byte export/reimport proof, and stationary visual acceptance. Section 3’s geometry gate requires local topology repair before winding acceptance; its animation gate requires continuity, declared root policy, genuine role motion, seam and measured contact checks.

## Immutable source and current baseline

The existing provider body GLB is C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\002_zombie_outbreak\models_3d\rabid_zombies\provider\downloads\rabid_body_01.glb, SHA-256 DCD456AECE728539E4E437E3680AFCC34A16DB8EF6888A14A7DF7D6B53BEAE14. The legacy rigged GLB is blender/working/v1/rigged.glb, SHA-256 E782BC961107131BA7DE99347380034A5DCA7B0070D1E35A2021D9867F0FD258. The final legacy action-import checkpoint is blender/working/v1/blender/checkpoints/17_support_attack_imported.blend, SHA-256 AA0CCDA6D60FD040F28095A845510A69A115FEB5CFBDAE1AF67D4B992BACD817; it is an action-source candidate, not yet confirmed as the current geometry source.

The current exported and installed mesh is gfx/models/units/chaosx_rabid_zombies/chaosx_rabid_zombies.mesh, SHA-256 391615A40B786A2320B996410B1FDD29EF87CB940EAB14CD4DF0BF2338C82B0F. The same bytes are present at docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/export/v2/chaosx_rabid_zombies.mesh. Its geometry-only reimport checkpoint is blender/checkpoints/reimport_installed_391615a40b786a23.blend, SHA-256 390B94C7A093B3C5B07904B4AC24B20D9CB62396BEA7E84983FA675AAE10543D; the matching receipt is validation/reimport_installed_391615a40b786a23.json, SHA-256 74E4C8E23717ECD5E95E9B173CCCEB71903762CCB248057B0E1CFA9C78118FE7. This checkpoint proves the installed mesh bytes can be imported; it does not prove materials, deformation, or actions.

The compact installed audit at docs/plans/unit_fix_2026-10/wp3_evidence/installed_model_audit_compact_20261006.json records 43,581 source positions, 31,119 faces, 81 boundary edges, 112 non-manifold edges, seven same-direction shared edges, and no degenerate or duplicate faces at positional tolerance 0.0005. Geometry remains blocked. The prior package report confirms the model and actions were unchanged in the shared delivery tranche.

The original Meshy input image exists at refs/original/meshy_input.png, SHA-256 E2AED9EB9F233E157418DEAC475201F1BD513B0568BD2A57870441936CF90C80. No source-provenance/input manifest was found in the rabid package during this bounded intake; its source page, creator/terms, retrieval details, preparation prompt, and parent approval therefore remain unverified here. No new source search or reference approval was performed because this is an existing-model repair and no provider input is planned.

Immutable provider PBR sources are present: base_color.png SHA-256 62F18AA592E29AB637F8486DECF64D3744C0835D324D5B7C9B595868D52FF90A; normal.png 29BC522DF62B6875B62119B8398DA6F51CE6701851854ED162A091E564758A29; roughness.png B280B25B8104A81504FC25C746418317CD2BA2C0CC610EEE43D18FE9138DE758; metallic.png 07DE25B05F4F5F95A1EA4400B2A4AA9ECE47CE254C68E96EB4706E7222FBBC05. Keep these as immutable source maps.

## Hash-bound action baseline

These are the existing installed-byte records from the compact audit, not newly re-audited or accepted actions. All are 30 FPS.

| Role | Frames | Existing status | Installed SHA-256 |
|---|---:|---|---|
| idle | 57 | parser pass only; ticket role fails duration, stance, and semantic requirements | 28A3B37987554A24D1B2DD1271CBA2C459BC07949C274F7E93048DD71B896CD4 |
| move | 79 | blocked | 2FB5884E0B950B963E6B0A2E1BC7A7B55C2BDAF731C0D6A84804C30EEA364007 |
| attack | 120 | blocked | 0852FBDBD08273D561440489B600D88046F5303F915A80AC042F9471F5B1578D |
| defend | 86 | blocked | 97ED730DBAA0292EF3476EC2775854F26D1001A77F097DB7C03BE653A6D2E558 |
| support_attack | 120 | blocked | 28959EB72267B4091ACD9E580282A4016ECD5535931BA4E88A0F5F0D9570C52D |
| retreat | 50 | blocked | 854AA97AB9AE0F58ED6C672CD4FCE4E7311E67F28E757DA07A0282E00D0E2216 |
| training | 43 | blocked | 2356B114FDA98FC25FE22A68B7FECA28207FB233CCD6189B11BE46EB99F51ABF |
| death | 67 | blocked | 73832E9B2126EBC31EE226207AA09582BADEF435220BF6502E8991D76E28E429 |

The legacy intake manifest declares humanoid_unit and the existing rig/action provider tasks. Its base_blend points to blender/checkpoints/05_pre_export.blend, which is absent. A complete package-level job.yaml and manifest.md are also absent. Do not export against this incomplete intake or overwrite the old v1 files; create a new full repair intake and new source-preserving checkpoint names inside the rabid job root before production.

## Bounded repair route after the slot grant

First reverify the current locked route, actual adapter schema, Blender build, extension manifest/archive and checksums against .tools/3d_pipeline/config/dependencies.lock.json and the adapter config. The existing shared route report under the zombies job records Blender 5.2.2, adapter 1.11.0 and io_pdx_mesh 0.91.0, but it is prior evidence rather than a fresh health/schema check for this session. The current dependency-lock SHA-256 is CB8D29299776135E33ACB5FED4DA5CF1F3188719704C0D9C81AD6E52A0A51856; adapter-config SHA-256 is 788858E3DC9E7D43A1717C419815F23935DC031F7BEEB1D50B13601E8AEB8543. The locked io_pdx_mesh compatibility archive is .tools/3d_pipeline/vendor/io_pdx_mesh/blender-io_pdx_mesh-0.91-py313.zip, SHA-256 508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702. The config and lock both declare adapter 1.11.0 and the same 32-operation published surface. Do not use the historical verification as proof of current service health.

After the parent grants the sole slot, acquire the shared staging OS lock before opening the hidden Blender Lab bridge, use one global worker, close the bridge after each authoring step, and do not wait with an open session for review. Preserve the two existing checkpoints above. Compare the action-source checkpoint against the exact installed-mesh reimport source before selecting the repair base; do not assume the v1 geometry matches installed bytes.

Inspect the affected fans and loops on a new checkpoint before editing. Repair only reviewed local neighborhoods: merge coincident points only within a measured 0.0005–0.002 tolerance, remove only confirmed duplicate faces, and fill only reviewed loops of at most eight sides. Do not apply a global fill/weld or blanket normal reset. Keep ambiguous fans, overlapping shells, UV aliases, and unsupported repair neighborhoods unresolved for review. Recalculate outside and apply the verified native 60-degree smoothing state only after the localized topology repair, then require zero boundary/non-manifold and same-direction edges on the final decoded mesh.

Reauthor real skeletal motion on the existing rig. Keep the new idle at least 120 frames/30 FPS, with standing planted feet, controlled Hips X/Z, weight shifts, head jerks every 15–24 frames, chest-height hand twitches, and a closed seam. Repair move to one measured left/right plant cycle in 1.0–1.5 seconds and match the endpoint by a reviewed stride cut or eased closure. Replace the attack back kick with the ticketed forward lunge and retain the 3.40-second contact only if it lands on the measured reach; send any retimed contact frame/time to the audio owner and parent. Inspect and deliberately repair the Hand vertices, wrist ring and forearm edge growth rather than applying formulaic weights. Preserve all other non-static semantic roles; no role aliases, copied actions from another model, or generated keyframes.

Build source-derived diffuse and PDX maps from the immutable provider PBR inputs and reviewed material regions. The accepted rabid ticket asks for suit G 60–80/A 70, skin G 130–160/A 150 and wet blood G 220/A 200. The current six-class shared material validator cannot express the wet nonmetal blood class, as recorded in wp3_pipeline_capability_handoff.md; do not fake it as steel or fur or claim this material gate passes. The shared tool owner must resolve the regional recipe route before texture acceptance. Confirm the final UV/layout binding, 512 BC1 diffuse, 256 BC3 specular, full mip chains, BC3 RRxG normal, and decoded semantic/fidelity gates from the actual selected final mesh.

For every edited/exported output, preserve the log, byte hash, locked operation/schema evidence, export settings and actual-byte parser/native reimport receipt. All eight action roles must be continuity-, root-policy-, loop/contact-, deformation-, and export/reimport-reviewed on the selected rig. A failing candidate stays outside runtime. Refilm and user live-consumer validation remain parent/user acceptance work.

## Work performed and remaining ownership

Read: AGENTS.md; chaos-redux-3d-model-pipeline, chaos-redux-event-assets and chaos-redux-subagents; the full unit fix plan including common rules, WP3 rabid ticket and section 3; pipeline_report.md; wp3_zombies_report.md; wp3_model_repair_handoff.md; wp3_pipeline_capability_handoff.md; and wp3_texture_repair_handoff.md.

No Blender process or Lab bridge was started, no live adapter operation was called, no Meshy key/balance/provider route was checked, no paid task or download occurred, and no audio, counter, runtime, gameplay, shared tool, lock, or other model file was edited. No new checkpoint or export was created in this preflight.

The separate audio owner remains responsible for rabid shriek, death gasp and contact source recovery/synchronization. The custom-unit counter requirement remains unresolved in this bounded model preflight and must be carried separately before the overall package is complete. No runtime claim or commit is made.

Next action is waiting for the parent’s explicit “Blender slot granted” message.

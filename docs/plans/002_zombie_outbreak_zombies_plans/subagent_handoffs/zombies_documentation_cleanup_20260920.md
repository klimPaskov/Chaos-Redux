# Base zombie 3D documentation cleanup handoff, 2026-09-20

## Scope and files changed

- Updated `docs/assets/002_zombie_outbreak/models_3d/zombies/manifest.md` with the current clean final v3 source-of-truth section and an explicit historical-status boundary.
- Updated `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/zombies_3d_pipeline_20260919.md` with the parent-supplied final export, material, runtime, reimport, and residual-defect evidence.
- Created this documentation-only cleanup handoff.

No gameplay, localisation, GFX, entity, sound, image, DDS, animation, mesh, Blender, spreadsheet, or other binary file was edited. The original production sections in both documents were left in place because they record real lineage and repair attempts.

## Current source-of-truth map

| Surface | Current reference | Evidence and limit |
| --- | --- | --- |
| Pre-export model, UV, rig, and actions | `docs/assets/002_zombie_outbreak/models_3d/zombies/blender/checkpoints/93_clean_uv_final_v3.blend` | Parent-designated final source; one UV layer, 30,436 triangles, 15,021 vertices. |
| Targeted death winding repair | `docs/assets/002_zombie_outbreak/models_3d/zombies/blender/checkpoints/91_death_backface_repair_v2.blend` | Parent reports 37 flips, excluding faces `10418` and `10911` that were already correct. |
| Locked model and action exports | `docs/assets/002_zombie_outbreak/models_3d/zombies/export/mesh/chaosx_zombies_clean_final_v3.mesh`; `export/anim/clean_final_v3/{attack,defend,idle,move,retreat,support_attack,training,death}.anim` | Promoted to canonical names under `gfx/models/units/chaosx_zombies/`; export/runtime equality and hashes are indexed by the final summary. |
| Runtime materials | `docs/assets/002_zombie_outbreak/models_3d/zombies/export/runtime_materials_v6/` | `base_color`, `normal`, and `roughness` PNGs and runtime DDS files; cross-category overlap report and culling render previews are offline evidence. |
| Concise final validation | `docs/assets/002_zombie_outbreak/models_3d/zombies/validation/clean_final_v3_summary.json` | Existing report indexes mesh and runtime hashes, all eight reimports, culling differences, credits, and user-owned live validation. |
| Detailed export and reimport | `docs/assets/002_zombie_outbreak/models_3d/zombies/logs/adapter/add82a35f9af4f2586d92f07a7fce1ee.result.json`; `validation/reimport_clean_final_v3_*.json`; `blender/checkpoints/reimport_clean_final_v3_*.blend` | Adapter transaction and actual-byte proof artifacts, relative to the zombie asset root. |
| Present package status | `docs/assets/002_zombie_outbreak/models_3d/zombies/manifest.md` current section | Offline runtime candidate promoted with a measurable death-culling residual; parent review and user-owned listening/live validation remain. |

The runtime mesh SHA-256 in the summary is `342FF7A8F28AD07D04C70A4686A064602DB03E9C65E6893E1032F6E901F2D698`. Runtime diffuse, normal, and specular SHA-256 values are `EFFE1B8D9D2013E6DBF680AC344F0943EDACF45B3AAA3D457856D77A763D7DA3`, `143BCFEB0C4827CE25CAAEA9E2558B12C15C7446656A5EACD8CEF1C01ABD44D0`, and `1BA6E652A9ED2F3E375BE6FA09585C65D65B6183D89B79ACFC6D8B62FE0A5267D0`. The cross-category UV edge-sample overlap is 3,263 of 334,514 covered texels (0.975%), with no four-way overlap; the prior layout was reported at 91.58%. The culling comparisons count pixels above a 40-difference threshold as attack `0`, move `7`, retreat `0`, and death frame 37 `612`.

## Document and handoff disposition

| Document or claim | Disposition | Basis and reason |
| --- | --- | --- |
| Manifest current clean final v3 section | Implemented as documentation of an offline runtime candidate | Parent supplied the locked source/export/runtime checkpoint within this delegated scope; `validation/clean_final_v3_summary.json` records the current exported and promoted bytes. This does not grant live-game acceptance. |
| Pipeline handoff current clean final v3 section | Implemented as documentation of an offline runtime candidate | Same parent acceptance basis and final evidence; the section is a current-state overlay on the historical handoff. |
| Manifest and pipeline handoff older dependency, v2/v4, v1 final, and action-deformation status claims | Superseded for present runtime status by the named clean final v3 sections | Those sections remain useful historical evidence, but their checkpoints, hashes, costs, and blockers no longer describe the promoted files. |
| Death frame 37 residual | Unresolved for final visual acceptance | The final evidence measures 612 culling-difference pixels on folded inner faces; the parent has not accepted this residual as a final visual outcome in the supplied scope. |
| Audio listening and live HOI4 consumer validation | Blocked pending user-owned validation | The supplied evidence covers offline model export and reimport, not listening or live engine behavior. |
| Earlier audio provenance, contact-timing, hurt-wrapper, acknowledgement, and specialized-counter review notes | Unresolved in this cleanup | These are recorded in the historical documents but were not included in the final model repair evidence; their owners must reconcile them separately. |

## Contradictions, duplicates, and stale instructions

- Resolved for readers: the old handoff ends with a blocked action-deformation audit while the current final summary records a promoted clean final v3 candidate. Both documents now put the superseding current state first and identify the older blocker as historical.
- Resolved for readers: v2, v4, and `final_v1` sections called different mesh and action files final. Their production evidence is preserved, and the clean final v3 checkpoint/export/runtime map is now the only current one.
- Resolved for readers: historical 35-credit statements precede the one paid Meshy rig attempt. The current total is 40 credits: 30 body, 5 remesh, 5 rig; there was no paid animation attempt, and Blender recovery is canonical.
- Open: death frame 37 retains 612 culling-difference pixels. The parent should decide whether the residual is acceptable before a zero-defect visual claim; the docs make no such claim.
- Duplicate or superseded document list: neither named document was merged or deleted. Their overlapping historical export narratives are explicitly superseded by the current sections and retained for provenance.
- Stale prompt or instruction list: no prompt file was inside the parent-assigned scope, and no prompt was edited. The historical dependency-stop and blocked-status instructions are labeled as dated records rather than continuation instructions.
- Markdown hard-wrap issue list: no accidental mid-sentence or mid-clause hard wrap was found in the scoped prose; deliberate headings, paragraphs, and list/table rows were preserved. No hard-wrap correction was needed.

## Validation and parent continuation

The current `validation/clean_final_v3_summary.json` was read and compared with the parent-supplied checkpoint, mesh and material hashes, eight role names, credit ledger, and culling numbers. The eight named reimport JSON paths, checkpoint/export/material paths, adapter result path, and preview families were confirmed present by targeted path checks. No HOI4 MCP focus, event, technology, weighted-logic, GUI, or map surface was part of this documentation scope; a 3D model export is outside those routes. This handoff does not claim Blender visual review or live-game evidence.

The parent should review the remaining 612-pixel death residual, reconcile the separate audio and specialized-counter notes if those packages are being closed, and keep live HOI4 and audio listening acceptance with the user. A docs-only commit was left to the parent so these changes can be reviewed with the concurrent final runtime repair.

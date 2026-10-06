# 005 Soviet Collapse: shared edge repair

Implemented the authorized chroma-edge cleanup on 472 inherited focus textures, preserving their 94x86 canvas, sprite names and frame declarations.
The selected set contained 78,373 detected chroma edge pixels before processing and zero after DDS decoding.
Each installed texture passes the literal nonzero-subject alpha mean of at least 200.
No focus logic, country content, portraits, localisation or weights changed.

The complete per-file fix list is the `005` subset with `runtime_status = installed` in `repair_candidates.json`.
Each row records original and output SHA-256, exact runtime path, current registered aliases and registry hashes, alpha/bounds diagnostics, selected candidate version and any explicit spill-mask coordinates.
`installed_checks.json` contains the final decoded DDS checks.
`final_contact_sheet_index.json` maps every installed texture to its reviewed before/after pair, including byte/pixel-identical copies, with sheets under `final_contact_sheets/005_*.png`.
The parent reviewed all final pairs; repacking the sheets after rejected candidates were removed retains the verified pair hashes and prior review locations.

The parent selected the 1 px erosion/interior-colour bleed requested by cross-cutting rule 1, then restricted opaque recolouring to the boundary band so vivid interior paint remains intact.
Six files sharing four paintings also use explicit reviewed masks for internal neon-green contamination; masks are under `spill_masks/`, with exact coordinates and source hashes in the fix rows.
Original sources and intermediate candidates remain in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/shared_tools_2026-10-06/`.
No generated replacement or opacity boost was substituted for the source art.

## Remaining issues and decisions

- 12 thin-detail textures have reviewed colour-only candidates pending an explicit exception to erosion; originals remain installed.
- Six candidate textures were rejected because erosion lowered their subject-alpha mean below 200; originals remain installed.
- Two opaque BLR forest-scene textures and three deeply ghosted Ukrainian textures cannot supply a safe cut-out/opaque interior; the pass refuses them and leaves their originals intact.
- 395 inspected textures have no confirmed chroma fringe requiring a runtime replacement; incidental key-like colours are not sufficient evidence to recolour otherwise intact paint.
- 95 installed textures produce margin or footprint warnings, listed individually in `installed_checks.json`; their existing framing needs its asset owner and was not silently rescaled in the edge pass.
- Named TNC/Ukraine and shared alpha warnings are retained in `alpha_audit_after.json`; this pass implements the check, not automatic opacity correction or missing-art generation.
- Narrow MCP focus inspection returned `JOB_WORKER_EXIT`; `focus_mcp_evidence.json` retains the exact failed requests/results, so these source/pixel checks are not claimed as engine-render proof.

The remaining art exceptions are unresolved, not accepted fallbacks.
This group is not claimed to be fully visually complete.
The tools themselves have no omitted requested command family.

## Orchestrator live check

Use a paused 1936 USA graphics fixture at 1920x1080, UI scale 1.
Use country-scoped console effects to load each tree without completing focuses: `effect load_focus_tree = { tree = soviet_collapse_ukraine_focus_tree }`, then the corresponding `soviet_collapse_baltic_focus_tree`, `soviet_collapse_belarus_focus_tree`, `soviet_collapse_kazakhstan_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_central_asia_focus_tree`, `soviet_collapse_moldova_focus_tree`, `soviet_collapse_internal_republic_focus_tree` and `soviet_collapse_breakaway_focus_tree`.
Open the focus view and compare installed rows against the final sheets at normal and close zoom, including military-border government, Basmachi autonomy/roads, sponsor-aid audit and border/rail liaisons.
Expected: neutral cut-out edges, no magenta/green rim or added opaque rectangle, readable retained interior paint, and stable icon anchors in hover and locked states.
Do not mark the listed retained/pending textures as fixed from this test.
The `load_focus_tree` block syntax was read from installed `documentation/effects_documentation.md` lines 4771–4786.

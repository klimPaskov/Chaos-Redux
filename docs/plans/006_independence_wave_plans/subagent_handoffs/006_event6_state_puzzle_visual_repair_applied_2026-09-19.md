# Event 006 state-puzzle visual repair — 2026-09-19

Disposition: `implemented; whole-event HOLD / PARTIAL remains`.

This owner-applied repair closes the concrete presentation defect recorded by the bounded review in `006_event6_state_puzzle_visual_repair_2026-09-19.md`. The fourteen accepted Event 006 state-puzzle families now use the established non-colour treatment required by `docs/formables/formable_state_puzzle_system.md`: unresolved pieces have a grey fill, diagonal hatch, and interior light outline; qualifying pieces have a green fill, dark inner silhouette outline, and pale inset keyline where the mask has enough interior width.

## Scope and provenance

The repair touched the 100 manifest-attested runtime pieces across FORM-01, FORM-02, FORM-03, FORM-04, FORM-05, FORM-07, FORM-08, FORM-09, FORM-12, FORM-13, FORM-16, FORM-18, FORM-39, and FORM-48. The four unmanifested Form12/Form13 state-256 DDS pairs remain unchanged and are retained as documented `unused_orphan` evidence.

The original authored source and processed PNGs were absent at the start of this repair. Each missing source path is now populated from a lossless decode of its pre-repair engine DDS, and every manifest records `source_mode = runtime_recovered_exact_geometry` plus a note that the file is not an original authored master. The existing nonzero-alpha silhouette, tight canvas, dimensions, sprite names, GFX paths, GUI references, map geometry, and per-pixel alpha mask were preserved.

## Palette and processing contract

The treatment matches the inspected established formable state-puzzle family:

- unresolved: base `RGB (98, 101, 108)`, diagonal hatch `RGB (66, 69, 75)`, interior outline `RGB (151, 154, 161)`;
- qualifying: base `RGB (70, 148, 103)`, dark inner outline `RGB (25, 56, 45)`, pale inset keyline `RGB (155, 216, 165)` where a second interior ring exists.

All 100 processed PNGs were converted back to their existing runtime DDS paths through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. No cross-family substitute, generated map shape, sprite rename, GUI rewrite, gameplay edit, or fallback image was introduced.

## Files and evidence

- Repair tool: `.tools/repair_event6_state_puzzle_assets.py`.
- Fourteen manifests: `docs/formables/state_puzzles/006_form*_state_puzzle/manifest.json`.
- One hundred recovered source PNGs under each manifest's `source/` directory.
- One hundred processed PNGs under each manifest's `processed/` directory.
- One hundred existing engine-facing DDS files under `gfx/interface/formables/state_puzzles/006_form*_state_puzzle/states/`.
- Fourteen unresolved/qualifying 440x180 projection previews regenerated from the repaired pieces.
- Review sheet: `docs/assets/006_independence_wave/contact_sheets/state_puzzles_repaired_contact_sheet.png`.

## Validation

- All 14 manifests and 100 asset records now have existing source, processed, and DDS paths; source, processed, DDS, and manifest SHA-256 fields recompute exactly.
- Every repaired DDS decodes as RGBA at its manifest dimensions. Processed PNG and decoded DDS pixels are equal for all 100 pieces.
- All unresolved/qualifying pairs retain identical masks, with zero alpha outside the pre-repair silhouette and no alpha-mask mismatch between source, processed, and runtime DDS.
- Native and enlarged review of representative small and large pieces, plus the complete contact sheet, shows the required hatch/outline/keyline treatment without canvas overflow or geometry drift.
- `python -B .tools/audit_event6_gui_matrix.py` passes the existing Statehood Ledger semantic matrix. This is source/static GUI evidence; no live game, save/load, or family-isolated GUI MCP render claim is made.

## Remaining limits

The four unmanifested Form12/Form13 state-256 DDS pairs remain unchanged as `unused_orphan` evidence. Dynamic qualification, click-region fidelity, grouped scripted-GUI state, live blendframe behavior, and whole-event live/save-load acceptance remain open under ASSET-039/ASSET-046 and the existing visual authority. The repaired source PNGs are runtime-recovered evidence, not original authored masters. Whole Event 006 remains **HOLD / PARTIAL**.

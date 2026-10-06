# Event003 Holy Mandala Real-Frame Repair Handoff

Disposition: `implemented`. The parent approved all seven 218px sixteen-frame contacts on 2026-10-06 and authorized promotion of all fourteen DDS files to their existing runtime paths.

## Scope and result

Rebuilt the seven `holy_realm_mandala_<state>` static and animated visual candidates for dormant, teaching, meditation, awakened, wrathful, final_silence, and empty. Each animation has 16 individually drawn motion poses in a generated source atlas, a 16-frame 420x420 processed PNG set, a 6720x420 horizontal sheet PNG, a static fallback PNG, a native GIF, and a 218px production-panel GIF.

The exact preview index is `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/preview_index.md`. The promoted package digest is `F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56`.

## Changed files

All new source, processed, preview, candidate DDS, manifest, and QA files are under `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/`. This includes preserved prior DDS binaries, decoded source references, per-state ImageGen prompts and atlas lineage, 112 raw frame crops, 112 processed frames, seven static fallbacks, seven horizontal sheets, fourteen GIFs, twenty-eight contact sheets, frame metadata, and DDS round-trip evidence.

This handoff is the only file created under `docs/plans/003_holy_realm_plans/subagent_handoffs/` by this worker. No `.gfx`, `.gui`, scripted GUI, gameplay, localisation, focus, decision, event, history, or spreadsheet file was edited.

## Validation evidence

The prior source archive path `docs/assets/003_holy_realm_buddhahood/animations/` was absent. The old handoff `docs/plans/003_holy_realm_plans/subagent_handoffs/2026-06-13_holy_mandala_state_animation_rebuild.md` confirms the previous glow loops derived motion from one still; those glow cells were not used as final frames.

The canonical decision-category contact sheet and `decision_category_generic.png` were inspected, followed by the visual-component catalog and matching contact sheet. The 52x40 `decision_category_background_blue_roundel.png` was not layered because the actual consumer is a standalone 420x420 GUI medallion.

Every processed state has 16 unique 420x420 RGBA frames with transparent corner pixels, a 6720x420 sheet, four contact sheets at exact dimensions, and 16-frame GIF previews totalling exactly 2.000 seconds. Native and 4x contacts were reviewed alongside 218px consumer previews for anchor stability and frame-specific motion.

Native ImageGen transparency was requested for each state atlas and every edit. The initial outputs had colored edge specks; targeted ImageGen edge edits did not fully remove them. The verified local fallback `rembg 2.0.61` with cached `isnet-general-use.onnx` (SHA-256 `60920E99C45464F2BA57BEE2AD08C919A52BBF852739E96947FBB4358C0D964A`), `alpha_matting=False`, and `post_process_mask=False` was applied per raw frame after the ImageGen edits. One representative frame per state was reviewed over both the exact production crop background `#17202A` and light gray before the full state batches were processed.

The repository DDS converter produced fourteen uncompressed BGRA32 candidates. Pillow strictly decoded every DDS, and every decoded pixel exactly matches its corresponding processed PNG; alpha extrema are `(0,255)`. The sorted candidate package digest is `F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56`, and the complete file hashes are in `notes/dds_roundtrip_report.json`.

The fourteen previous DDS binaries remain preserved byte-for-byte in `previous_rejected_dds/`. All promoted runtime DDS hashes match the approved candidate package and the exact PNG round-trip report. No GFX or GUI file was edited. No game or desktop was used; nothing was staged or committed.

## Parent follow-up

The remaining parent evidence gate is a matched post-asset GUI render. `gui003_release` reports its post-change MCP render timed out without artifacts and visual acceptance remains unresolved in `docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005.md`; this asset worker did not run GUI/MCP validation. The GFX entries still use the existing names, paths, 16-frame count, and 8 fps. The current GUI source uses `GFX_holy_realm_mandala_dormant` as its static base; `GetHolyRealmMandalaSprite` in `common/scripted_localisation/003_holy_realm_scripted_localisation.txt:387-443` returns the matching animated names, but that visual switch was not engine-rendered in the unavailable MCP pass.

The exact owned force-add list is `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/notes/force_add_files.txt`. No files have been staged or committed.

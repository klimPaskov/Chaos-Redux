# Repression ledger decision-category icon handoff

Status: `needs_user_review`.

## Deliverable

One purpose-built static Hearts of Iron IV decision-category icon for the shared repression ledger system is complete as an asset package.

Runtime sprite identifier: `GFX_decision_category_repression_ledger`.

Final DDS path: `gfx/interface/camp_repression/decision_category_repression_ledger.dds`.

Final native canvas: `52x40` pixels.

The art is an original, country-neutral locked state dossier/archive file with one dark iron clasp and a restrained deep-red wax seal inside an irregular aged steel-and-brass medallion.

## Created files

- `docs/assets/system_camp_repression_rework_ui_repair/source_png/decision_category_repression_ledger_source.png` is the untouched native-alpha ImageGen source.
- `docs/assets/system_camp_repression_rework_ui_repair/processed_png/decision_category_repression_ledger_52x40.png` is the exact-size transparent processed preview.
- `gfx/interface/camp_repression/decision_category_repression_ledger.dds` is the final one-level legacy BGRA DDS.
- `docs/assets/system_camp_repression_rework_ui_repair/contact_sheets/contact_sheet.png` is the visual evidence sheet.
- `docs/assets/system_camp_repression_rework_ui_repair/contact_sheets/processed_52x40_enlarged_smooth.png` is the enlarged smooth processed preview.
- `docs/assets/system_camp_repression_rework_ui_repair/contact_sheets/decoded_dds_roundtrip.png` and `decoded_dds_roundtrip_enlarged.png` are DDS decode evidence.
- `docs/assets/system_camp_repression_rework_ui_repair/manifest.md` records the asset manifest, evidence, hashes, and validation.
- `docs/assets/system_camp_repression_rework_ui_repair/gfx_handoff.md` records parent wiring steps.
- `docs/assets/system_camp_repression_rework_ui_repair/prompts/decision_category_repression_ledger_imagegen_prompt.txt` preserves the exact generation prompt.

## Prompt, source, and background mode

The official built-in ImageGen skill was used in native generation mode.

The source was generated from the recorded prompt without any input image.

The initial generation explicitly requested genuine transparent background and the source was retained unchanged.

No background-removal fallback was used.

No checkerboard, matte, halo, opaque square, or chroma background is present in the runtime PNG or DDS.

## Canonical reference evidence

The required canonical library README and catalog were inspected under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`.

The exact contact sheet inspected was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/contact_sheet.png`.

The installed-vanilla category family was checked against `decision_category_generic.png` (`51x40`), `decision_category_border_conflicts.png` (`52x40`), `decision_category_border_war.png` (`52x40`), `decision_category_generic_crisis.png` (`52x39`), `decision_category_infiltration.png` (`50x40`), and `decision_category_generic_prospect_for_resources.png` (`52x41`).

The installed Vanilla definitions were checked at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/decisions.gfx`, with direct texture paths under `gfx/interface/decisions/`.

The reference family establishes the compact medallion silhouette, dark outline, painterly shading, high contrast, and transparent unused canvas used by this asset.

## Technical evidence

Native source: `1430x1100` RGBA, alpha bounds `(30, 38, 1404, 1080)`, alpha counts zero/full/partial `569917/639/1002444`, transparent corners.

Processed PNG: `52x40` RGBA, smooth Lanczos resize, alpha values `0..4` from resize fringe set to zero, visible bounds `(1, 1, 51, 38)`, alpha counts zero/full/partial `690/93/1297`, transparent corners.

DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; `texconv` was unavailable and the tool used its ffmpeg BGRA fallback (`ffmpeg version N-123778-g3b55818764-20260331`).

DDS header: magic `DDS `, header size `124`, flags `0x100f`, dimensions `52x40`, pitch `208`, depth `0`, mip count `0` (one level), pixel format size `32`, flags `0x41`, fourCC `0`, 32-bit channel masks `0x00ff0000/0x0000ff00/0x000000ff/0xff000000`, texture caps `0x1000`.

DDS length: `8448` bytes, exactly `128 + 52*40*4`.

Decoded DDS round-trip: pixel-equal to the processed PNG with zero channel difference and identical bounds/alpha counts.

## Hashes

- Source PNG: `1b2f035ac24b775bdd6c09c128bfdcfc6137cd28a9d36f0f0850a39ebe63cd2d`.
- Processed PNG: `38c79302c78b9fad5fb2202ad69208f75928bf745aefac73dd9236cd8a1e51fe`.
- Final DDS: `898c81e28bd40e00784edd76d9bb806b59374a3416120efe2c1b7428bbb7fb65`.
- Contact sheet: `6509ac7979ed6af6b6e4157a4abeef1174e3e0dfa72930cd151eb17095b85af8`.

## Rejected candidates

The inspected `gfx/interface/camp_repression/GFX_decision_category_repression_ledger.dds` (`53x53`, SHA-256 `a7ec3a6844e0c328318cda5a1c0ad3ff22692952d1a900872a884e59acfab4d5`) was rejected as a square crate/optics thumbnail.

The inspected `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_repression_ledger.dds` (`52x40`, SHA-256 `c380e247a5ea4251840f6edc8a3f45ec30f997f7dcb1b48a6aa796e8247053a5`) was rejected as a cramped collage.

Neither rejected candidate was used in generation or processing.

## Parent wiring and acceptance boundary

The parent should add a stable `spriteType` named `GFX_decision_category_repression_ledger` pointing to `gfx/interface/camp_repression/decision_category_repression_ledger.dds` in the parent-owned `.gfx` file.

The parent should review the native-size preview and contact sheet, then validate the linked consumer in the live game.

No `.gfx`, `.gui`, localisation, decision, gameplay, or spreadsheet files were edited by this handoff.

In-game validation and parent visual acceptance were skipped by scope and remain the only completion risks.

The temporary evidence workspace remains intentionally retained at `docs/assets/system_camp_repression_rework_ui_repair/`.

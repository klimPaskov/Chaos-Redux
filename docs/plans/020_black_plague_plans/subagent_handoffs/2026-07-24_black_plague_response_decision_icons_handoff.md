# Event 020 response decision-icon production handoff

Status: complete for the 15 decision icons currently referenced by `interface/020_black_plague_response.gfx`.

## Scope and ownership

This handoff covers only visual production and evidence for the response decision icons. Gameplay, localisation, GUI, and `.gfx` files were not edited. The parent implementation owner retains final wiring and live-game review ownership.

## Delivered files

- Fifteen preserved or newly generated source PNGs under `docs/assets/020_black_plague/source_png/`.
- Fifteen chroma-key-removed full-resolution RGBA intermediates under `docs/assets/020_black_plague/alpha_intermediate/`.
- Fifteen exact 33×32 RGBA previews under `docs/assets/020_black_plague/processed_png/decisions/`.
- Fifteen archived DDS files under `docs/assets/020_black_plague/dds_archive/decisions/`.
- Fifteen runtime DDS files under `gfx/interface/decisions/020_black_plague/`.
- `docs/assets/020_black_plague/contact_sheets/decision_icons_contact_sheet.png` and `docs/assets/020_black_plague/previews/decision_icons_preview.png` for review.
- `docs/assets/020_black_plague/prompts/decision_icons_2026-07-24.md` for the seven newly generated source prompts.
- `docs/assets/020_black_plague/decision_icons_manifest.md` and `decision_icons_crosswalk.md`.
- `docs/assets/020_black_plague/gfx_handoff.md` with a ready-to-review sprite snippet.

## Icon set

The eight existing source concepts are medical reserve, clean city rats, sealed food stores, clear sewers, flea control, transport purge, demolition, and emergency hospital. The seven generated additions are quarantine, cordon, treatment reserves, warren purge, countermeasure program, Doctor Wu protocol, and Doctor Wu foreign access.

## Processing evidence

The canonical decisions contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/contact_sheet.png` was inspected before generation. The official imagegen built-in tool produced the seven new sources on flat magenta chroma-key fields. The installed `remove_chroma_key.py` helper created RGBA intermediates. A deterministic Pillow pass trimmed only transparent margins, fit each silhouette inside a 31×30 safe area, and centered it on the 33×32 decision canvas. The repository `convert_to_dds.py` tool produced the final one-level uncompressed BGRA DDS files.

## Validation and remaining review

All 15 processed PNGs report dimensions 33×32 and transparent corners. All 15 runtime DDS headers report width 33, height 32, BGRA masks, one mip level, and the expected 33×32×4 payload. The contact sheet makes silhouette alignment and alpha edges reviewable. Parent-side live UI review should confirm that the existing `.gfx` declarations resolve these runtime paths in the decision list.

No fallback, placeholder, recolor-only, or transform-only asset was used. No icon remains blocked in this bounded set.

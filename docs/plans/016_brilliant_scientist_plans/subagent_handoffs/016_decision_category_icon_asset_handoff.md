# Event 016 decision and decision-category icon asset handoff

Date: 2026-07-24

## Scope completed

The current eight `common/decisions/016_brilliant_scientist_kruger_state_*.txt` files parse to exactly 134 decision or mission IDs after the accepted hazardous-mission objectives were added. The package contains exactly 40 distinct decision-family icon compositions at `32x32` and exactly 10 distinct decision-category compositions at the verified vanilla `50x40` category size. Each current decision or mission ID maps to exactly one decision sprite, and each of the ten current categories maps to its own category sprite.

No fallback, recolor-only variant, focus-icon resize, or transform-only pseudo-uniqueness was used. The masters are three retained ImageGen atlases with independently composed cells, cropped into source masters before alpha processing.

## Runtime outputs

- Decisions: `gfx/interface/decisions/016_brilliant_scientist/decisions/decision_<sprite_name>.dds` (40 files).
- Categories: `gfx/interface/decisions/016_brilliant_scientist/categories/decision_category_<sprite_name>.dds` (10 files).
- Decision sprite prefix: `GFX_decision_brilliant_scientist_krg_`.
- Category sprite prefix: `GFX_decision_category_brilliant_scientist_krg_`.
- Parent copy-ready blocks: `docs/assets/016_brilliant_scientist/package_records/decision_category_sprite_blocks.txt`.
- Parent wiring target: `interface/016_brilliant_scientist_kruger_state_decisions.gfx`.

## Evidence and ledgers

- Source masters: `docs/assets/016_brilliant_scientist/source_png/decision_icons/` and `source_png/decision_categories/`.
- Keyed alpha evidence: `docs/assets/016_brilliant_scientist/alpha_png/decision_icons/` and `alpha_png/decision_categories/`.
- Processed previews: `docs/assets/016_brilliant_scientist/processed_png/decision_icons/` and `processed_png/decision_categories/`.
- Source, processed, and decoded-DDS contact sheets: `docs/assets/016_brilliant_scientist/contact_sheets/decision_icons_016_*contact_sheet.png` and `decision_categories_016_*contact_sheet.png`.
- Prompt and provenance: `docs/assets/016_brilliant_scientist/prompts/decision_category_icon_generation_record.md`.
- Machine manifest and hashes: `docs/assets/016_brilliant_scientist/package_records/decision_category_icon_manifest.json`.
- Decision assignment ledger: `docs/assets/016_brilliant_scientist/package_records/decision_assignment_ledger.tsv` (134 rows).
- Category assignment ledger: `docs/assets/016_brilliant_scientist/package_records/decision_category_assignment_ledger.tsv` (10 rows).
- Technical validation: `docs/assets/016_brilliant_scientist/validation/decision_category_icon_validation_detailed.tsv`.

## Validation evidence

`python -B docs/assets/016_brilliant_scientist/package_records/validate_decision_category_icons.py` reports 50 assets, 40 decisions, 10 categories, 134 assignment rows, and 10 category-assignment rows with status `ok`. The validator checks exact PNG dimensions, alpha range and transparent corners, legacy DDS magic/header size, `DDS_PIXELFORMAT` size 32 and flags 65, BGRA masks, `DDSCAPS_TEXTURE`, exact file length, successful Pillow decoding with pixel identity against the processed PNG, unique source hashes, duplicate assignment IDs, complete sprite coverage, and no orphan decision or category sprite.

## Parent wiring notes

The parent registered the 50 exact sprite blocks in `interface/016_brilliant_scientist_kruger_state_decisions.gfx` and replaced every generic consumer in the eight KRG decision files and ten category definitions with its ledger sprite identifier. The four later hazardous-mission objectives were assigned to existing semantic families and added to the generator and ledger.

No unresolved asset blocker remains in this bounded package. Visual review of the contact sheets is still parent/user acceptance work; the producer does not self-approve final art.

## Parent review disposition

Parent review accepted the package on 2026-07-24 after inspecting the source, processed, and decoded-DDS contact sheets for all forty decision families and ten categories, plus representative native-size decision and category PNGs.

The sources have distinct silhouettes and project semantics; the native-size portal, foundation-repair, and terminal-program samples remain legible; the transparent processed output is clean; and the decoded DDS sheets visually match the processed sheets.

The 134/134 decision assignment and 10/10 category assignment ledgers are accepted and wired.

This disposition accepts the bounded art package, not the entire Event 016 asset inventory or implementation.

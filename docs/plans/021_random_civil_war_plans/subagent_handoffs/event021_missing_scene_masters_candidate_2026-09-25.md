# Event 021 missing scene-master reconstruction candidates — 2026-09-25

Disposition: `implemented`; the parent individually reviewed and promoted all four as dated generated replacements on 2026-09-25. Their absent original source masters remain unrecovered.

The user authorized a visual-asset audit and repair and identified the accepted design files as `docs/specs/021_random_civil_war_specs/021_random_civil_war_asset_prompt.md` and `docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_9_presentation_assets_achievements.md`.

## Deliverables

The isolated package root is `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/scenes/`.

It contains four generated high-resolution source masters, exact prompt/source-mode notes, processed PNG previews, candidate DDS outputs, DDS-decoded PNG round-trips, a labeled contact sheet, a manifest with source/processed/DDS SHA-256 hashes and validation, and `gfx_handoff.md`.

The four candidate assets are the opening report (`E021-GEN-REPORT-V1`), multi-front news (`E021-GEN-NEWS-MULTIFRONT-V1`), Global Fracture news (`E021-GEN-NEWS-GLOBAL-FRACTURE-V1`), and civil-war category picture (`E021-GEN-CATEGORY-PICTURE-V1`).

The separate GFX handoff is `[gfx_handoff.md](../../../assets/021_random_civil_war/recovery_candidates_2026-09-25/scenes/gfx_handoff.md)`.

## Processing and evidence

The report candidate uses the established `process_report_event_image.py` card treatment and the repository-standard `convert_to_dds.py` converter.

The news previews are opaque `397x153` grayscale images with deterministic contrast and period grain; the category picture is an opaque `114x101` sepia scene.

All four DDS outputs pass the expected one-level BGRA header and file-size checks and decode pixel-identically to the processed previews, with zero changed pixels and zero maximum channel difference.

The report DDS preserves transparent corner alpha; the news and category DDS files remain fully opaque.

The processed PNGs and DDS-decoded round-trips were inspected at each native consumer size; the labeled sheet is `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/scenes/contact_sheets/event021_missing_scene_masters_candidates_2026-09-25.png`.

The existing sprite declarations were located read-only in `interface/021_random_civil_war.gfx`; no `.gfx` file was edited.

## Ownership and remaining work

All candidate packages remain preserved under the dated recovery root, and the parent copied byte-identical source and processed files to separately named dated paths under the canonical `source_png/` and `processed_png/` asset trees.

The built-in ImageGen originals remain at their tool-reported `C:\Users\klimp\.codex\generated_images\...` paths outside the repository; byte-identical source-master copies are retained inside the candidate package.

Git visibility: the repository ignore rule `.gitignore:80` ignores `docs/assets/`; candidate and canonical PNG source packages remain local working assets, while the active runtime DDS files and tracked evidence documents are version-controlled.

The original canonical source filenames remain absent. The six runtime DDS files were backed up under `docs/assets/021_random_civil_war/validation/pre_generated_replacement_promotion_2026-09-25/` and replaced using the reviewed, repository-converter-produced candidates; `.gfx`, event/category consumers, and localisation were not changed.

The generated candidates are not the missing original ImageGen sources. They establish a new, fully recorded source-to-runtime lineage for the active textures without claiming original recovery.

## Parent review and promotion

The parent opened each generated source master, processed preview, and DDS round-trip individually. All four scenes were reviewed at source and exact native consumer size; the report's transparent card corners, grayscale news scenes, compact opaque category image, and calm documentary framing match their specified consumer families.

The final DDS files were copied byte-for-byte from the isolated candidate packages to their existing active paths, preserving stable sprite wiring. Independent header checks confirmed the expected dimensions, one-level 32-bit BGRA layout, masks, pitch, texture caps, and exact lengths. Active DDS SHA-256 values are report `4eb8cc83fd7134d2b2462f60ab1a988cbe92a417930b791cf6a291d73b459fb2`, multi-front `33b80197a17d74ca9467ea96ba84ac44c92486814efd1a6f3cb3666b84baa7be`, Global Fracture `845d735ac39aad81bb334627cbbea514537e9edbf94b6275635fd5ca470ace45`, and category picture `794d01167648995a2023920f11a607e80484acb32a80c21b17e6e6f00434c666`.

The permanent source, processed, and runtime paths and hashes are listed in `docs/events/021_random_civil_war/owned_asset_crosswalk.md`. Actual in-game consumer presentation remains a user-owned test.

No fallback or runtime substitute was used; the first parallel ImageGen prompt batch was rejected by the output safety filter, then all four final generations succeeded with calm non-combat documentary wording.

# Event 26 Black Friday icon-art handoff

Status: `parent_visual_reviewed_2026-09-01_after_triplet_rebuild`; the generated icon visuals, deterministic achievement triplet rebuild, and repaired report package were reviewed. The assigned source PNGs, processed previews, DDS staging files, manifest, GFX handoff, prompts, superseded diagnostic evidence, contact sheets, runtime promotion, and sprite registration are present. No gameplay, achievement registry, spreadsheet, portrait, or counter files were edited by the icon worker.

## Assigned identifiers and runtime destinations

- Active-sale idea asset `black_friday_sale`; proposed sprite `GFX_idea_026_black_friday_sale`; staged DDS `docs/assets/026_black_friday/dds/gfx/interface/ideas/026_black_friday/black_friday_sale.dds`; intended runtime DDS `gfx/interface/ideas/026_black_friday/black_friday_sale.dds`; parent-owned target `.gfx` `interface/026_black_friday.gfx`.
- Achievement asset `026_black_friday_five_departments`; proposed sprites `GFX_achievement_026_black_friday_five_departments`, `GFX_achievement_026_black_friday_five_departments_grey`, and `GFX_achievement_026_black_friday_five_departments_not_eligible`; staged DDS files are under `docs/assets/026_black_friday/dds/gfx/achievements/`; intended runtime DDS files are rooted at `gfx/achievements/`; parent-owned target `.gfx` `interface/026_black_friday.gfx`.
- The Event 26 consumer remains `chaosx.nr26.1`; no event id or gameplay wiring was changed here.

## Files delivered

- Original generated sources: `docs/assets/026_black_friday/source_png/black_friday_sale.png` and `026_black_friday_five_departments.png`, `_grey.png`, `_not_eligible.png`.
- Processed idea preview: `docs/assets/026_black_friday/processed_png/idea/black_friday_sale_64x64.png`.
- Processed achievement source layers: `docs/assets/026_black_friday/processed_png/achievement_layers/026_black_friday_five_departments.png`, `_grey.png`, `_not_eligible.png`.
- Superseded diagnostic evidence: `docs/assets/026_black_friday/processed_png/fallback/026_black_friday_five_departments_grey_bg_removed.png` and `_not_eligible_bg_removed.png`.
- DDS staging: `docs/assets/026_black_friday/dds/gfx/interface/ideas/026_black_friday/black_friday_sale.dds` plus the three achievement DDS files under `dds/gfx/achievements/`.
- Processor review PNGs: `docs/assets/026_black_friday/dds/gfx/achievements/review/`.
- Visual review: `docs/assets/026_black_friday/contact_sheets/icon_package_contact_sheet.png`.
- Documentation: `docs/assets/026_black_friday/manifest.md`, `docs/assets/026_black_friday/gfx_handoff.md`, `docs/assets/026_black_friday/prompts/`, `docs/assets/026_black_friday/notes/source_mode.md`, and the assigned processor `docs/assets/026_black_friday/notes/process_icon_package.py`.

## Provenance and alpha evidence

The official built-in ImageGen route was used on 2026-08-29, with genuine transparency requested in each initial prompt. The idea source is `1341x1173 RGBA`, alpha `0..255`, transparent corners, SHA-256 `E1796DE2962F2E3D03524BA9EAEFF57F94ADCDB28BF4191C6D5D71DA2EDBF272`. The completed achievement source is `1254x1254 RGBA`, alpha `0..255`, transparent outer corners, SHA-256 `1722E96C0261E1A2A109DA84A6E88B8A125780FB717099BC9A7F237F8380798C`.

ImageGen returned opaque checkerboard-like matte pixels for the grey and not-eligible source layers. Those untouched RGB sources are retained with alpha `255..255` and SHA-256 `584496855D13520D4C520631A75CCB7FB688EB1A99F47E43B071AB8EEFA29D30` and `4B067D708871619CD1D363CBBF2996816187676DEE3AC942ADB70F0AB643DA25`. The final triplet does not use those independent variants: the grey 64x64 layer is deterministic grayscale of the completed layer with alpha preserved, and the not-eligible layer is that grey layer composited with the unchanged canonical red-X overlay (`89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`). The earlier edge-connected matte-removal outputs remain diagnostic evidence only.

The processed idea/state layers are exact `64x64 RGBA`, alpha `0..255`, transparent corners. The composed achievement DDS states intentionally include the canonical Vanilla template coverage and decode as `64x64 RGBA`, alpha `254..255`, full canvas. All four DDS files are strict `16512`-byte uncompressed 32-bit BGRA with a `16384`-byte pixel payload and no mipmaps. Idea DDS SHA-256 is `375ECA0DB0A0375A36DB9F1292D6264E112153F0AEFF2A723821A5B02D28A434`; achievement DDS hashes are `507BC29D3C8785F54EAE7D33AE392C4E173DAB2B8B862CB1A2DE18FD00FFD57C`, `BE8EACEEE6EEA39C2A6241B84B9F63564C2A48D163DCEB8D3062BA198C202F70`, and `A7A29A4A18FD601A65A8BC7EAAC51927A0AAA0F7420661783D876665AE364596` in completed, grey, not-eligible order.

## References, checks, and remaining action

The canonical `icons/ideas/contact_sheet.png` and `icons/achievements/contact_sheet.png` were inspected before individual family references. The matching Vanilla achievement state examples, exact supplied templates, and no final reference PNG reuse were recorded in the manifest. The canonical achievement processor returned `AUDIT OK 026_black_friday_five_departments: strict 64x64 BGRA triplet and source-layer equality verified`. The contact sheet shows source, derived, canonical overlay, and DDS round-trip views.

Parent action completed on 2026-09-01: the parent visually approved the repaired contact sheet and native-size outputs, promoted the four staged DDS files to the intended runtime paths, and registered the sprite names in `interface/026_black_friday.gfx`. No production blocker remains for asset staging. The opaque ImageGen state variants remain documented as rejected provenance, while the final state triplet uses the completed source, deterministic grayscale, and the canonical red-X overlay.

# Event 014 Unified Decision Icons — Rows 10–24 Handoff

## Outcome

Completed all 15 assigned unified-decision icons. Each asset has an independent built-in `$imagegen` source, a transparent `32x32` processed PNG, and an exact registered-path DDS. No gameplay, `.gfx`, `.gui`, localisation, spec, spreadsheet, or non-owned asset was edited.

## Identifiers

- `cannibalism_unified_rapid_consumption`
- `cannibalism_unified_managed_consumption`
- `cannibalism_unified_mobile_consumption`
- `cannibalism_unified_battlefield_consumption`
- `cannibalism_unified_larder_mission`
- `cannibalism_unified_establish_air_program_foundation`
- `cannibalism_unified_create_cannibal_legion`
- `cannibalism_unified_surge_cannibal_legion`
- `cannibalism_unified_recruit_island_reavers`
- `cannibalism_unified_recruit_siege_eaters`
- `cannibalism_unified_recruit_march_predation_column`
- `cannibalism_unified_recruit_lockhouse_column`
- `cannibalism_unified_raise_bone_guard`
- `cannibalism_unified_launch_continental_hunt`
- `cannibalism_unified_collapse_enemy_front`

## Files

- Source PNGs: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/source_png/decision_<ID>_source.png` for the 15 identifiers above.
- Processed PNGs: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/processed_png/decision_<ID>.png` for the same identifiers.
- Runtime DDS files: `gfx/interface/decisions/014_cannibalism/decision_<ID>.dds` for the same identifiers.
- Subset manifest: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/manifest.md`.
- Validation ledger: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/validation.tsv`.
- Runtime hash ledger: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/runtime_hash_ledger.tsv`.
- Reviewed contact sheet: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/rows_10_24_contact_sheet.png`.
- Reproducible subset processor: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/subsets/rows_10_24/process_rows_10_24.py`.

## Validation evidence

- Source, processed, and runtime coverage is `15/15` for each stage.
- Every processed icon is `32x32`, has real transparency, zero-alpha corners, fully opaque subject pixels, and zero visible chroma-key-green pixels.
- Every DDS is a `4,224`-byte, one-mip, uncompressed 32-bit BGRA/B8G8R8A8-style texture and decodes pixel-identically to its processed PNG.
- All 15 registered `GFX_decision_<ID>` to runtime texture mappings in `interface/014_cannibalism.gfx` were read and matched exactly; that file was not edited.
- All 15 source hashes and normalized processed RGBA hashes are unique. The final scan found no owned normalized-pixel collision against the 86 non-owned Event 014 decision-folder textures present during validation.
- The contact sheet was reviewed at `4x` and native `32x32`; the furnace, carousel, prison wheel, stretcher/hopper, ledger wheel, propeller/anvil, two Legion states, grappling hook, sledge impact, tire/boot, wheeled cage, bone helmet, binocular snare, and collapsing tread/barricade remain materially distinct.

## Simplifications, omissions, and blockers

None. No placeholder, reused source, cross-type reuse, procedural core artwork, transform-only substitute, unapproved fallback, missing artifact, or blocker remains. No commit was created, as requested.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`

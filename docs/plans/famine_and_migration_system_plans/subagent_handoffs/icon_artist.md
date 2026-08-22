# Icon artist handoff: famine and migration system

Status: complete for the assigned icon surfaces; parent wiring remains.

## Delivered files

- Source PNGs: `docs/assets/famine_and_migration_system/source/` (1 category icon, 9 state modifiers, 10 decisions, 8 achievement masters), all retained from built-in ImageGen output.
- Processed PNGs: `docs/assets/famine_and_migration_system/processed/` (28 gameplay/achievement masters plus 16 derived achievement states).
- Final DDS: 1 category icon under `gfx/interface/decisions/famine_and_migration_system/`, 9 state modifiers under `gfx/interface/state_modifiers/famine_and_migration_system/`, 10 decision icons under `gfx/interface/decisions/famine_and_migration_system/`, and 24 root achievement DDS files under `gfx/achievements/`.
- Manifest: `docs/assets/famine_and_migration_system/manifest.csv`.
- GFX handoff: `docs/assets/famine_and_migration_system/gfx_handoff.md`.
- Review sheets: `docs/assets/famine_and_migration_system/contact_sheets/`, including source/processed/DDS round-trip comparisons and 4x nearest-neighbor previews.

## Consumer contract

- Category icon `fm_cat_displacement`: 52x40, proposed `GFX_fm_cat_displacement`, target `interface/chaosx_decisions.gfx`.
- State modifier IDs `fm_state_supply_strain`, `fm_state_acute_shortage`, `fm_state_famine`, `fm_state_catastrophic_famine`, `fm_state_exodus`, `fm_state_reception`, `fm_state_overcrowded`, `fm_state_trapped_border`, and `fm_state_return`: 32x32, proposed `GFX_fm_state_*`, target `interface/countrystateview.gfx`.
- Decision IDs `fm_dec_release_reserves`, `fm_dec_relief_convoy`, `fm_dec_airlift`, `fm_dec_evacuate`, `fm_dec_open_border`, `fm_dec_close_border`, `fm_dec_quarantine`, `fm_dec_distribute`, `fm_dec_integrate`, and `fm_dec_return`: 32x32, proposed `GFX_fm_dec_*`, target `interface/chaosx_decisions.gfx`.
- All eight achievements use exact stable IDs from the parent prompt and three root DDS filenames each: completed, `_grey`, and `_not_eligible`, all 64x64. Explicit aliases may be added to `interface/chaosx_achievements.gfx`; no GFX edits were made here.

## Generation and reference evidence

The built-in ImageGen tool was available and used for each original icon/achievement master with genuine transparent background requested in the initial call. No reference PNG was copied, traced, recolored, or used as runtime art. The canonical contact sheets and catalogs were inspected first at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` for decisions, decision categories, category pictures, state modifiers, and achievements.

Achievement gray states were derived as grayscale from each completed master; not-eligible states were derived by compositing the canonical `icons/achievements/overlay.png` over that grayscale state, following the skill contract.

## Processing and validation

- Processed canvases: category 52x40, state modifiers 32x32, decisions 32x32, achievements 64x64.
- All source and processed alpha checks report real zero-alpha padding and nonzero subject pixels; no chroma, checkerboard, matte, or fallback background removal was used.
- `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced all 44 final DDS files as uncompressed BGRA8, one mip level.
- Header, mask, caps, declared dimensions, exact byte length, and alpha range checks passed for all 44 DDS files.
- Decoded DDS pixels matched their processed PNGs byte-for-byte for all 44 outputs; round-trip mismatches: 0.

## Remaining boundaries

- `fm_pic_displacement` is intentionally not included: it is the separate opaque 114x101 decision-category picture surface and belongs to generated event-art work.
- `fm_deaths_famine` and `fm_deaths_displacement` remain uncreated because the parent did not provide a verified Deaths reason-icon/texticon consumer. This is a consumer-proof blocker, not a substituted asset.
- Parent agent owns `.gfx`, gameplay, localisation, achievement definitions, and final in-game consumer validation.

# Icon artist handoff: famine and migration system

Status: complete for the assigned icon surfaces and the Deaths texticon follow-up; current GFX/localisation wiring is present, while visual runtime validation remains parent-owned.

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
- `fm_deaths_famine` and `fm_deaths_displacement` are now delivered as parent-wiring texticons under `gfx/texticons/` at 18x18. Source prompts, original PNGs, processed PNGs, DDS round-trips, validation JSON, and a 4x contact sheet are under `docs/assets/famine_and_migration_system/{prompts,source,processed,dds_roundtrip,contact_sheets}/deaths/`. Sprite IDs `GFX_fm_deaths_famine` and `GFX_fm_deaths_displacement` are registered in `interface/chaosx_texticons.gfx`.
- The Deaths details surface remains a text-key renderer around `interface/chaosx_chaos_meter_popup.gui:1971-1979` and `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt:848-860`, while the current cause localisation consumes the registered inline texticons.
- `localisation/english/chaosx_chaos_meter_l_english.yml` consumes `£fm_deaths_famine` in `chaos_meter.deaths.cause.famine` and `£fm_deaths_displacement` in `chaos_meter.deaths.cause.forced_displacement`, with the file's UTF-8 BOM and existing wording preserved.
- Deaths DDS validation: both outputs are 18x18, 1-level uncompressed BGRA8, 1,424 bytes, alpha 0..255, and byte-identical to processed PNG round-trips (0 mismatches). SHA-256: `fm_deaths_famine.dds` `3016C7B420C59A626C52DA344B6B73340602BA74CACA8FA763E1AD86F6010DD4`; `fm_deaths_displacement.dds` `4CC527A54F5B304EB92DD3573280315096BF14E7BBA2BC90BFD4D4EDBC635F23`.
- Parent agent owns `.gfx`, gameplay, localisation, achievement definitions, and final in-game consumer validation.

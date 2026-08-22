# Famine and migration icon GFX handoff

This package contains original built-in ImageGen source PNGs, alpha-preserving processed PNGs, and final one-level BGRA8 DDS files for the icon and achievement surfaces assigned to `chaosx_icon_artist`.

## Runtime paths and proposed sprite names

Use the existing GFX registries; this package does not edit them.

```text
interface/chaosx_decisions.gfx
  GFX_fm_cat_displacement -> gfx/interface/decisions/famine_and_migration_system/fm_cat_displacement.dds (52x40)
  GFX_fm_dec_<suffix> -> gfx/interface/decisions/famine_and_migration_system/fm_dec_<suffix>.dds (32x32)

interface/countrystateview.gfx
  GFX_fm_state_<suffix> -> gfx/interface/state_modifiers/famine_and_migration_system/fm_state_<suffix>.dds (32x32)

interface/chaosx_achievements.gfx (optional explicit aliases; achievement lookup also uses the root filenames)
  GFX_achievement_<achievement_id> -> gfx/achievements/<achievement_id>.dds
  GFX_achievement_<achievement_id>_grey -> gfx/achievements/<achievement_id>_grey.dds
  GFX_achievement_<achievement_id>_not_eligible -> gfx/achievements/<achievement_id>_not_eligible.dds
```

The exact basename IDs in `manifest.csv` are the stable handoff names. Achievement files are root-only and match the eight requested achievement IDs exactly.

## Completed families

- `fm_cat_displacement`: one 52x40 native-alpha decision category icon.
- `fm_state_supply_strain`, `fm_state_acute_shortage`, `fm_state_famine`, and `fm_state_catastrophic_famine`: four distinct 32x32 famine-stage state modifier icons.
- `fm_state_exodus`, `fm_state_reception`, `fm_state_overcrowded`, `fm_state_trapped_border`, and `fm_state_return`: five distinct 32x32 migration/reception state modifier icons.
- Ten 32x32 decision icons: reserves, relief convoy, airlift, evacuation, border opening, border closure, controlled reception, distribution, integration, and return.
- Eight achievement triplets at 64x64: completed source-derived art, grayscale state, and grayscale plus the canonical red-X overlay.
- Two Deaths reason texticons at 18x18: `fm_deaths_famine` (empty bowl and broken grain) and `fm_deaths_displacement` (broken rail route and luggage).

## Source and reference evidence

Every gameplay icon and achievement master was generated with the built-in ImageGen tool using a distinct surface-specific prompt and a genuine transparent background request. Native-alpha source files are preserved under `docs/assets/famine_and_migration_system/source/`; processed files are under `processed/`.

Deaths source prompts are preserved under `prompts/deaths/`; native source and processed files are under `source/deaths/` and `processed/deaths/`.

Canonical review material inspected before generation was the single reference root at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`, including `icons/decisions/contact_sheet.png`, `icons/decision_categories/contact_sheet.png`, `icons/decision_categories/pictures/contact_sheet.png`, `icons/state_modifiers/contact_sheet.png`, and `icons/achievements/contact_sheet.png`, plus `README.md` and `CATALOG.md`.

## Validation evidence

- All 46 DDS files exist at the final runtime paths, including the two Deaths reason texticons.
- `gfx/texticons/fm_deaths_famine.dds` and `gfx/texticons/fm_deaths_displacement.dds` are each 18x18, 1-level uncompressed BGRA8, 1,424 bytes, alpha range 0..255, and round-trip byte-identical to their processed PNGs (0 mismatches). SHA-256: `3016C7B420C59A626C52DA344B6B73340602BA74CACA8FA763E1AD86F6010DD4` and `4CC527A54F5B304EB92DD3573280315096BF14E7BBA2BC90BFD4D4EDBC635F23` respectively.
- DDS headers were checked as uncompressed 32-bit BGRA8 (`B8G8R8A8_UNORM` masks), one mip level, texture caps, exact declared dimensions, and exact `128 + width*height*4` file length.
- Every DDS retains alpha range 0..255; no alpha-backed output has an opaque square background.
- All 46 DDS files were decoded back to RGBA and compared byte-for-byte with the processed PNG at the native canvas; mismatches: 0.
- Contact sheets in `docs/assets/famine_and_migration_system/contact_sheets/` show source, processed, and decoded DDS round-trip views, with separate 4x nearest-neighbor review sheets.

## Out-of-scope or blocked rows

- `fm_pic_displacement` is a 114x101 opaque decision-category picture surface owned by generated event-art work, not this icon package; it remains unproduced here rather than being satisfied by a resized icon.
- `fm_deaths_famine` and `fm_deaths_displacement` have final 18x18 parent-wiring texticon files and registered sprites `GFX_fm_deaths_famine` / `GFX_fm_deaths_displacement` in `interface/chaosx_texticons.gfx`. The current Deaths cause localisation consumes `£fm_deaths_famine` in `chaos_meter.deaths.cause.famine` and `£fm_deaths_displacement` in `chaos_meter.deaths.cause.forced_displacement`, with the existing UTF-8 BOM preserved.
- The Deaths details surface remains a text-key renderer around `interface/chaosx_chaos_meter_popup.gui:1971-1979` and `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt:848-860`; the cause text now carries the registered inline texticons, so the documented consumer is source-wired while visual runtime confirmation remains parent-owned.
- Report-image rows remain with the generated event-art/source-research routes.

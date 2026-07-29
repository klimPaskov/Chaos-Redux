# Event005 Parent Tranche: Ancient Reward Cleanup and Ukraine Overlap

## Scope

- Parent-side follow-up after the current focus audit subagent pass.
- No flag files, flag sprites, or flag directories were inspected or edited.

## Files changed

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focus reward cleanup

The following ancient restoration focuses kept their existing gameplay payloads but now expose one compact `custom_effect_tooltip` instead of a long raw effect stack. The actual flags, claims, equipment, variables, war plans, buildings, cores, and AI strategy effects were moved into `hidden_effect`.

- `APX_old_border_files`
- `APX_expansionist_steppe_levy`
- `APX_khazar_charter`
- `APX_restoration_survives_modern_war`
- `SOG_old_city_border_files`
- `SOG_expansionist_merchant_claims`
- `SOG_sogdian_city_charter`
- `SOG_restoration_survives_modern_war`
- `ANX_old_oasis_border_files`
- `ANX_expansionist_water_claims`
- `ANX_khwarazmian_water_charter`
- `ANX_restoration_survives_modern_war`
- `ABX_old_pass_border_files`
- `ABX_expansionist_mountain_claims`
- `ABX_alan_pass_charter`
- `ABX_restoration_survives_modern_war`

## Layout fix

- Moved `ukr_soviet_collapse_the_bread_line_becomes_a_border` from `x = 24, y = 11` to `x = 17, y = 13`.
- This removes the exact coordinate overlap with `ukr_soviet_collapse_minority_autonomy_statutes` and lowers the high-chaos bread-state lane away from the central political branch.

## Localisation

Added route-specific tooltip keys for the compact ancient restoration rewards in:

- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Validation

Parent validation run after the tranche:

- Brace balance checked for touched focus/localisation files.
- `git diff --check` passed for touched files.
- Localisation BOM for `005_soviet_collapse_custom_countries_l_english.yml` remained `efbbbf`.
- The active focus auditor independently reported no exact repeated idea/helper inside one current focus reward, but systemic helper repetition remains across the focus layer.

## Remaining issues

- This is not the full focus-tree rework. Major route-depth, helper-repetition, layout, and mechanics-linking work remains across Ukraine, Belarus, Central Asia, Kazakhstan, CFR/MFR, and chaos splinters.
- The focus auditor identified the highest-priority remaining pathline clusters: Ukraine high-chaos/political lanes, Central Asia four-way route selector, CFR four-way mutex, and MFR route fork.

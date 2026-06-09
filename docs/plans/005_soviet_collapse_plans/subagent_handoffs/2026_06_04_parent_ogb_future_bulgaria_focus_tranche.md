# 2026-06-04 Parent OGB Future Bulgaria Focus Tranche

## Scope

Patched one bounded Event005 focus-reward gap identified by current focus-tree audits: `OGB_future_bulgaria_file` was still mostly a political-power and variable focus despite being the route bridge toward Old Great Bulgaria's wider Volga restoration.

No flag files, flag images, or flag interface files were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Gameplay Change

`OGB_future_bulgaria_file` now:

- uses political, annexation, and army filters;
- unlocks the existing `ogb_press_trade_city_claims` decision tooltip;
- calls the new helper `soviet_collapse_apply_ogb_future_bulgaria_file`;
- prepares the claim file immediately instead of only adding political power and legitimacy.

The new helper:

- claims the Volga trade-city states used by the existing OGB trade-city system;
- grants militia manpower, infantry equipment, support equipment, and army experience;
- raises `ogb_volga_legitimacy`, `ogb_river_authority`, and recognition progress;
- applies compact or rival AI posture toward Idel-Ural depending on the chosen route;
- increases old-movement pressure while Soviet Collapse is active.

The later `ogb_press_trade_city_claims` decision remains meaningful because it still presses the claim line, cores controlled claim states, and escalates against Idel-Ural.

## Localisation

Updated `OGB_future_bulgaria_file_desc` to remove meta wording about a future event chain.

Added:

- `OGB_future_bulgaria_file_tt`

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: clean.
- `rg -n "<=|>="` over touched files: no unsupported operators.
- Brace balance over touched files: all balanced, no early negative brace depth.
- Localisation BOM check for `005_soviet_collapse_custom_countries_l_english.yml`: true.
- `support_equipment_1` token checked against existing repo uses and `common/script_enums.txt`.
- `git status --short -- gfx/flags interface/flags`: no entries.

## Remaining Gaps

This is not a completion claim for Event005 focus-tree quality. Current audits still call out Kazakhstan geometry, Ukraine high-chaos branch uniqueness, Belarus strategic payoff, many zero-decision-link custom splinter trees, and broad helper-reward repetition across the four Event005 focus files.

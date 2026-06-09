# Event005 Parent Mission Popup And MFR Reward Tranche

Date: 2026-06-04

## Scope

Parent-side implementation tranche for the active Soviet Collapse goal. This patch deliberately avoided `gfx/flags`, `interface/flags`, `.tga`, and all flag asset paths.

## Files changed

- `events/005_soviet_collapse.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Mission popup behavior

Converted the Soviet mission result reports `chaosx.nr5.71` through `chaosx.nr5.94` from `news_event` definitions to `country_event` definitions while preserving `minor_flavor = yes`, `major = no`, pictures, titles, descriptions, and options.

Updated the two active mission callbacks that fire the first mission-result reports:

- `soviet_collapse_soviet_mission_016_certify_loyal_military_districts`
- `soviet_collapse_soviet_mission_017_restore_the_central_supply_seal`

Those callbacks now use `country_event = { id = chaosx.nr5.71/72/73/74 }` instead of `news_event`, so the mission results behave as minor country notifications rather than news popups.

## MFR focus reward cleanup

Addressed the focus-audit finding that several Military Factory of Russia late-route focuses were shallow helper-only rewards:

- `MFR_war_market_never_sleeps`
  - Unlocks `mfr_audit_arsenal_orders`.
  - Unlocks `mfr_convert_depots_to_arms_lines`.
  - Adds a guarded arms factory line in a controlled core state.
  - Feeds the existing war-market contract helper.

- `MFR_output_is_victory`
  - Unlocks `mfr_convert_depots_to_arms_lines`.
  - Adds offsite arms-factory capacity.
  - Grants an infantry weapons production tech bonus.
  - Keeps the existing output doctrine helper.

- `MFR_no_peace_without_orders`
  - Unlocks `mfr_convert_depots_to_arms_lines`.
  - Adds offsite arms-factory capacity and artillery.
  - Dynamically creates annexation war goals against eligible neighboring countries.
  - Adds conquer/antagonize AI strategies for those eligible neighbors.

Updated the existing MFR arsenal decisions and conversion effect so the new route flags actually matter:

- `mfr_audit_arsenal_orders` is visible from the war-market route and grants its extra arms-line payoff there.
- `mfr_convert_depots_to_arms_lines` is visible from the war-market, output-doctrine, and no-peace routes.
- `soviet_collapse_apply_mfr_convert_depots_to_arms_lines` now rewards the war-market route with client-ledger depth and the output/no-peace routes with contract backlog and war support.

No new national spirits were added.

## Localisation

Added concise tooltips:

- `MFR_war_market_never_sleeps_tt`
- `MFR_output_is_victory_tt`
- `MFR_no_peace_without_orders_tt`

## Validation

- Brace balance clean:
  - `events/005_soviet_collapse.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
- `git diff --check` passed for all touched files.
- No `<=` or `>=` found in touched script/localisation files.
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` still has UTF-8 BOM.
- `git status --short -- gfx/flags interface/flags` returned no touched flag files.

## Remaining work

This tranche does not complete the active Event005 goal. Remaining audited focus work includes Kazakhstan early fork geometry, Ukraine high-chaos bread-state reward uniqueness, OGB future-Bulgaria payoff depth, and DHC/UWD/BAC long lateral pathlines.

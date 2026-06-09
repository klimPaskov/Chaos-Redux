# Parent Focus Reward and Evolution Detail Tranche

Date: 2026-06-04

Scope: bounded parent implementation tranche for Event005 Soviet Collapse focus reward readability and evolution-detail clarity. This is not a completion claim for the full Soviet Collapse rework.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_kaz_focus_l_english.yml`
- `localisation/english/005_soviet_collapse_regional_focus_l_english.yml`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

## Focus Reward Cleanup

Converted four high-priority raw reward dumps into single visible country-specific tooltips with the actual effects moved under `hidden_effect`:

- `ukr_soviet_collapse_black_sea_port_ledgers`
- `kaz_soviet_collapse_industrial_settlement_compacts`
- `central_asia_soviet_collapse_khwarazm_restoration_debate`
- `TSC_perimeter_regiments`

This keeps the current balance effects but stops the focus panel from showing long raw lists of buildings, equipment, claims, and random-state blocks.

## Evolution Detail Cleanup

Updated Soviet Collapse event-log wording and scripted localisation routing:

- Renamed the player-facing `soviet_collapse_secession` label from "Republic Secession Progression" to "Republic Secession Timeline" so it reads as baseline crisis tracking rather than a mutation evolution.
- Kept the spreadsheet secession stage body text intact for Gathering Storm, Rising Chaos, Chaos Tier, and Terminal Rupture.
- Renamed the two high-chaos generic stages to "High-Chaos Successor Wave" and "Extreme Successor Wave" to avoid duplicate world-collapse wording.
- Added class-specific high-chaos detail bodies for:
  - Ancient Claims Return
  - The Dead Are Citizens
  - Pale Railway Authority / Depots Choose Flags
- Routed selected-detail and event-detail high-chaos body lookup to these class-specific bodies.

## Validation

- `git diff --check` passed for touched files.
- No `<=` or `>=` operators found in touched files.
- Localisation BOM check passed for all touched localisation files.
- Brace balance check returned `balance 0 min 0` for touched script files.
- `git status --short -- gfx/flags interface/flags` showed no flag or interface-flag changes.

## Remaining Work

- Full focus-tree rework is still incomplete.
- Remaining audit blockers include ARD, FEV, NLC, MFR layout, Baltic/Central Asia route-choice layout, Ukraine bread-state same-row pathline, and broader focus route depth.
- Release/scenario logic still needs a proof pass against every possible Soviet/internal/high-chaos splinter.
- Decision expansion panels still need validation for empty target groups.
- No commit was made for this tranche because the active Soviet Collapse goal remains incomplete and the worktree already contains broad uncommitted Event005 changes.

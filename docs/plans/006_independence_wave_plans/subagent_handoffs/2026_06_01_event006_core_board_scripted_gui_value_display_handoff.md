# Event 006 Core Board Scripted GUI Value Display Handoff

Date: 2026-06-01

## Scope

Added the first decision-category scripted GUI value-display layer for the Event 006 core boards.

## Files changed

- `common/decisions/categories/006_independence_wave_categories.txt`
  - Mounted scripted GUI panels on the Independence Dossier Board, New States Congress, Patron Ledger, Formation Ledger, and Border Commission categories.
- `common/scripted_guis/006_independence_wave_scripted_guis.txt`
  - Added four decision-category scripted GUI definitions.
  - All four are display-only and disabled for AI.
- `interface/006_independence_wave_scripted_gui.gui`
  - Added four `containerWindowType` display panels using existing Event 006 decision-category sprites.
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
  - Added `GetIndependenceWavePackageLabel` for Formation Ledger package labels.
- `localisation/english/006_independence_wave_l_english.yml`
  - Added GUI headers, value text, and package-label localisation.
- `docs/events/006_independence_wave.md`
  - Documented the scripted GUI value layer and remaining UI work.

## Implemented boards

- `independence_wave_dossier_board_scripted_gui`
  - Shows dossier count, host anger, and foreign attention.
- `independence_wave_congress_board_scripted_gui`
  - Shows coalition cohesion, patron leverage, compact members, and mutual guarantees.
- `independence_wave_patron_ledger_scripted_gui`
  - Shows patron leverage, foreign attention, legitimacy, and militia strength.
- `independence_wave_formation_ledger_scripted_gui`
  - Shows the resolved package file label, claim ambition, legitimacy, and coalition cohesion.
- `independence_wave_border_commission_scripted_gui`
  - Shows claim ambition, open disputes, peaceful resolutions, and foreign attention.

## Validation

- Brace balance checked cleanly for:
  - `common/decisions/categories/006_independence_wave_categories.txt`
  - `common/scripted_guis/006_independence_wave_scripted_guis.txt`
  - `interface/006_independence_wave_scripted_gui.gui`
  - `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
  - `localisation/english/006_independence_wave_l_english.yml`
  - `docs/events/006_independence_wave.md`
- No unsupported comparison operators found in touched files.
- `localisation/english/006_independence_wave_l_english.yml` retained UTF-8 BOM.
- No `:0` localisation keys found in the touched localisation file.
- Cross-reference check passed:
  - all category `scripted_gui =` references have matching scripted GUI definitions
  - all scripted GUI `window_name` values have matching interface containers
  - all GUI text keys have localisation
  - all `GetIndependenceWavePackageLabel` keys have localisation
- No trailing whitespace found in touched files.
- `git diff --check` passed for tracked touched files.

## Assets and flags

No country flags, flag artwork, new sprites, DDS files, or animation assets were changed in this tranche. The panels reuse already registered Event 006 decision-category sprites.

## Remaining risks and follow-up

- This is a value-display layer only. It does not close the remaining final UI requirement for animated route seals, dynamic major-route state art, or richer target-list scripted GUI.
- No live game UI screenshot was captured in this tranche.

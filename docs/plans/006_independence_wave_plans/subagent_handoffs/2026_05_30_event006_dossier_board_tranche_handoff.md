# Event 006 Dossier Board Tranche Handoff

## Scope completed

- Converted the host aftermath decision-category presentation into the on-screen `Independence Dossier Board`.
- Added live dossier-board description values for open dossier count, host anger, and foreign attention.
- Added two host-response decisions:
  - `independence_wave_open_dossier_talks`
  - `independence_wave_evacuate_host_archives`
- Added scripted triggers and scripted effects for both decisions.
- Added script constants for costs, command-power spending, anger relief, foreign attention, stability, and political power rewards.
- Updated `docs/events/006_independence_wave.md` so the implemented surface is documented as a decision-category Dossier Board, not a missing placeholder GUI.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Validation run

- Brace balance passed for the touched Event 006 constants, triggers, effects, decisions, and decision category files.
- Unsupported operator scan found no `<=` or `>=`.
- Localisation BOM check passed for `localisation/english/006_independence_wave_l_english.yml`.
- Localisation `:0` scan found no matches.
- No files under `gfx/flags`, `common/countries`, or `history/countries` were changed by this tranche.

## Remaining risks

- This is a decision-category Dossier Board tranche, not a full scripted GUI. The improvement addendum explicitly recommends staying with decision-category ledgers until stable data and target arrays justify full GUI.
- The full Event 006 source-spec pack remains incomplete. Remaining broad work includes additional country packages, full visual asset families, animated major-route assets, final audits, spreadsheet alignment, and improvement-loop closure.

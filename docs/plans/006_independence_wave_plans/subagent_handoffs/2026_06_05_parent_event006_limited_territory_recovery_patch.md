# Event 006 Limited-Territory Recovery Patch

## Scope

Parent patch for the user request that newly released Event 006 countries need starting forces, ways to build an army, and a generic way to expand beyond one-state starts.

## Gameplay changes

- `independence_wave_setup_released_country` already gives each release startup manpower, infantry equipment, support equipment, an unlocked provisional guard division template, two capital guard divisions, an emergency arms workshop, and the shared `independence_wave_liberation_provisional_tree`.
- Added `independence_wave_mark_limited_territory_start`, which flags one-state releases with `independence_wave_limited_territory_start`.
- Added `has_independence_wave_limited_border_recovery_claim`, shared by reduced-footprint starts and one-state starts.
- Widened `independence_wave_recover_surveyed_core` so limited one-state starts can use the Border Commission recovery lane after filing a border survey.
- Updated the decision wording from reduced-core-only language to generic surveyed-district recovery language.
- Kept the route design generic: no country-specific stacked focuses were added, and no Kuban or Altai expansion work was introduced.

## Files Changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Validation

- Brace balance passed for touched Event 006 script/localisation files.
- `rg "<=|>="` found no unsupported operators in touched Event 006 runtime files.
- `git diff --check` passed for the touched files.
- `localisation/english/006_independence_wave_l_english.yml` still has UTF-8 BOM (`efbbbf`).
- `tmp/hoi4-error-logs` currently contains only `watchdog.log`; no current `error.log` was present for additional log-based fixes.

## Remaining Risks

- This is a runtime patch, not a live in-game verification pass.
- The broader Event 006 completion audit remains open; final animated UI assets, full spreadsheet parity after later wording changes, and every optional package detail still need separate completion proof before the whole Event 006 goal can be called complete.

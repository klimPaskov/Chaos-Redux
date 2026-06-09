# Parent Event006 Mapuche Recovery And News Audit Handoff

Date: 2026-06-05

## Scope

This tranche fixed a narrow recovery blocker in the Mapuche package and audited the current-wave news release list path. It did not claim full Event 006 completion.

## Gameplay Change

- `independence_wave_map_mapuche_land_petitions_effect` now makes Aysen `949` and Rio Negro `512` surveyed cores only.
- The effect no longer adds regular claims to those two states.
- This keeps the states eligible for `independence_wave_recover_surveyed_core`, whose target trigger intentionally rejects already claimed states while allowing unowned non-capital cores held by a surviving owner.

## Files Changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_parent_event006_mapuche_package_handoff.md`

## Identifiers

- `independence_wave_map_mapuche_land_petitions_effect`
- `independence_wave_recover_surveyed_core`
- `is_independence_wave_border_commission_target_state`
- `can_independence_wave_recover_surveyed_core`
- `MAP`
- states `949`, `512`, `950`

## News Audit

The current `chaosx.news.6` display path already lists all current-wave releases up to the resolver cap:

- `independence_wave_prepare_release_count` clears `global.independence_wave_country_1` through `global.independence_wave_country_16` before each wave.
- `independence_wave_register_successful_release` increments `global.independence_wave_actual_release_count`, adds the release to `global.independence_wave_current_wave_releases`, and fills the matching display slot from `global.independence_wave_country_1` through `global.independence_wave_country_16`.
- `GetIndependenceWaveReleasedCountryList` selects the longest matching list from 16 down to 1.
- `chaosx.news.6.d` includes `[This.GetIndependenceWaveReleasedCountryList]` under `Confirmed releases:`.

Vanilla precedent exists for storing a scope in a variable and using `[?SCOPE.variable.GetName]` style localisation.

## Validation

- Brace balance:
  - `common/scripted_effects/006_independence_wave_effects.txt` open `3168`, close `3168`, delta `0`
  - `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` delta `0`
  - this handoff delta `0`
- Unsupported operator scan over touched files produced no hits.
- Trailing whitespace and CRLF scan over touched files produced no hits.
- `git diff --check` passed for the touched files.
- Targeted search confirmed `independence_wave_map_mapuche_land_petitions_effect` no longer contains `add_claim_by = ROOT`; remaining `add_claim_by = ROOT` hits are the separate Border Commission claim and ultimatum effects.
- `tmp/hoi4-error-logs/` still only contained the old `watchdog.log`; no fresh Event 006 error log was present.

## Remaining Risks

- This does not prove every package expansion route is complete. It only fixes the proven Mapuche surveyed-core self-filter.
- The current-wave news list is implemented for 16 releases, which matches the known resolver slot cap, but live UI readability for a 16-country sentence still needs in-game review.
- A fresh read-only completion audit was spawned after this tranche to re-check full-spec parity and remaining gaps.

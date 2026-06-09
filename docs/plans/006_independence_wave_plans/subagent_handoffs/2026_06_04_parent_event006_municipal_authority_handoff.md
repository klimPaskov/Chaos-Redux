# Event 006 Municipal Authority Tranche Handoff

Date: 2026-06-04

Owner: parent Codex agent

## Scope

Implemented the first non-port city-state package variant for Event 006. A non-Danzig city-package release without harbor or canal control now receives the `municipal_authority` package identity instead of falling through to Free Port Authority.

This tranche does not add tags, country files, history files, portraits, or flag assets.

## Gameplay Wiring

- Added `independence_wave_package_municipal_authority` identity assignment for inland city-package releases without controlled harbor or canal states.
- Added city-state package detection using vanilla-supported state categories `city`, `large_city`, `metropolis`, and `megalopolis`.
- Kept Danzig on its bespoke Free City Board path, kept canal states on Canal Authority, and restricted Free Port Authority to controlled harbor states.
- Added Formation Ledger actions for opening the municipal charter file, organizing the service board, proclaiming the Municipal Authority, and post-proclamation integration.
- Added `independence_wave_municipal_authority_spirit`.
- Added the Municipal Charter File focus at `x = 30`, `y = 8`.
- Added AI strategy behavior for municipal authorities that favors defense, infantry supply, public works, civilian industry, and restraint.
- Added event-log package and formation milestone rows for Municipal Charter File and Municipal Authority.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`

## Validation

- `git diff --check` passed on the touched gameplay, localisation, and documentation files.
- Unsupported operator scan found no raw `<=` or `>=` tokens in touched Event 006 script/localisation surfaces.
- Brace counts were balanced for touched Event 006 script files.
- Localisation BOMs were preserved for `006_independence_wave_l_english.yml` and `chaosx_gui_l_english.yml`.
- Localisation scan found no old `:0` key style.
- Municipal package constants, package labels, decision keys, idea keys, focus key, and event-log labels were found across expected files.
- Event 006 focus count is now 79, and the focus-icon reuse ledger has 79 rows with no unmatched focus IDs.
- Focus coordinate check did not find a new collision for `x = 30`, `y = 8`; duplicate rows reported by the scan were pre-existing overlaps.
- No changes were present under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states` for this tranche.

## Asset Notes

The route reuses existing Event 006 free-city board, municipal workshop, decision, idea, and focus icon families. No flag changes were needed for this gameplay tranche. Future bespoke municipal seals, council portraits, animated route art, or flag variants should go through the Event 006 asset workflow.

## Remaining Package Gaps

- Border buffer or border protectorate variant.
- Deeper second-layer Free Port, Canal Authority, Municipal Authority, Protected Mandate, Oil Protectorate, and railway package branches.
- Package-specific portraits, seals, animation, and optional flag variants for routes that need unique visual identity.

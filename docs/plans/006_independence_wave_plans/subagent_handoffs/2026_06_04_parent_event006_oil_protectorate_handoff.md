# Event 006 Oil Protectorate Tranche Handoff

Date: 2026-06-04

Owner: parent Codex agent

## Scope

Implemented the first oil-specific protectorate variant for Event 006 protectorate-package releases. A protectorate release that owns a controlled oil-producing state now receives the `oil_protectorate` package identity instead of the generic protected mandate route.

This tranche does not add tags, country files, history files, portraits, or flag assets.

## Gameplay Wiring

- Added `independence_wave_package_oil_protectorate` identity assignment when a protectorate package has controlled oil-state access.
- Kept the generic `independence_wave_package_protectorate_mandate` route for non-oil protectorate packages.
- Added Formation Ledger actions for oil concession audit, fuel-board seating, Oil Protectorate proclamation, and post-proclamation integration.
- Added the `independence_wave_oil_protectorate_spirit` startup and route spirit.
- Added an Oil Concession Audit focus at `x = 28`, `y = 10`.
- Added AI strategy behavior for oil protectorates that favors fuel security, infantry production, infrastructure, and restrained war behavior.
- Added event-log package and formation milestone rows for Oil Concession Audit and Oil Protectorate.

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

## Validation

Pre-documentation mechanical checks passed:

- `git diff --check` on the touched gameplay and localisation files.
- Unsupported operator scan found no matches.
- Brace counts were balanced for touched script files.
- Localisation BOMs were preserved for `006_independence_wave_l_english.yml` and `chaosx_gui_l_english.yml`.
- Localisation scan found no old `:0` key style.
- Oil package constants, package labels, decision keys, idea keys, and event-log labels were found across the expected files.
- Event 006 focus count is now 77.
- `independence_wave_oil_concession_audit` is the only focus found at `x = 28`, `y = 10`.
- No changes were present under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states` for this tranche.

Final validation should be rerun after this handoff file is committed with the tranche.

## Asset Notes

The route reuses the existing Event 006 sponsored-cabinet focus, idea, and decision icon families. No flag changes were needed for this gameplay tranche. Future bespoke oil-concession seals, treaty-broker portraits, animated route art, or flag variants should go through the Event 006 asset workflow.

## Remaining Package Gaps

- Canal authority variant.
- Border buffer or border protectorate variant.
- Non-port city-state variants.
- Deeper second-layer protected mandate and oil protectorate route branches.
- Package-specific portraits, seals, animation, and optional flag variants for routes that need unique visual identity.

# Event 006 Canal Authority Tranche Handoff

Date: 2026-06-04

Owner: parent Codex agent

## Scope

Implemented the first canal-specific city/port package variant for Event 006. A non-Danzig city/port release that controls a canal state now receives the `canal_authority` package identity instead of the generic Free Port Authority route.

This tranche does not add tags, country files, history files, portraits, or flag assets.

## Gameplay Wiring

- Added `independence_wave_package_canal_authority` identity assignment for city/port packages with controlled canal-state access.
- Kept Danzig on its bespoke Free City Board path and kept non-canal city/port releases on the generic Free Port Authority path.
- Added canal-state detection using documented canal building-count triggers for Kiel and Panama plus vanilla canal-control state precedents for Suez, Kiel, and Panama.
- Added Formation Ledger actions for opening the canal register, negotiating the transit charter, proclaiming the Canal Authority, and post-proclamation integration.
- Added `independence_wave_canal_authority_spirit`.
- Added the Canal Register focus at `x = 30`, `y = 11`.
- Added AI strategy behavior for canal authorities that favors defensive transit security, convoy production, infrastructure, and restraint.
- Added event-log package and formation milestone rows for Canal Register and Canal Authority.

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
- Canal package constants, package labels, decision keys, idea keys, and event-log labels were found across the expected files.
- Event 006 focus count is now 78.
- Initial coordinate check found a collision at `x = 28`, `y = 11`; the Canal Register focus was moved to `x = 30`, `y = 11`.
- No changes were present under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states` for this tranche.

Final validation should be rerun after this handoff file is committed with the tranche.

## Asset Notes

The route reuses the existing Event 006 free-city board focus, idea, and decision icon families. No flag changes were needed for this gameplay tranche. Future bespoke canal seals, transit-board portraits, animated route art, or flag variants should go through the Event 006 asset workflow.

## Remaining Package Gaps

- Border buffer or border protectorate variant.
- Non-port city-state variants.
- Deeper second-layer Free Port, Canal Authority, Protected Mandate, and Oil Protectorate route branches.
- Package-specific portraits, seals, animation, and optional flag variants for routes that need unique visual identity.

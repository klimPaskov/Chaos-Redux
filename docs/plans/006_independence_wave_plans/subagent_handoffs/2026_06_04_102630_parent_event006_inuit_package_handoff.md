# Parent handoff: Event 006 Inuit Arctic Council package

Date: 2026-06-04 10:26 UTC

## Scope

Implemented the first Event 006 `iw_pkg_inuit` local-polity package using vanilla `INU` support.

The package is gated to chaos tier IV/V, requires `INU` to be inactive, and releases only from Alaska state `463` when the current host can survive the release. Event 006 temporarily seeds the vanilla Inuit core set on `463`, `864`, `472`, `683`, `466`, `332`, `101`, and `861` for candidate validation and restores or clears those temporary core flags after the release pass. The first start remains Alaska-only; the wider Arctic map is recorded as petition/proof territory, not direct expansion.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## New identifiers

- Package flag/label: `independence_wave_package_inuit`, `independence_wave_package_label_inuit`
- Package constant: `constant:independence_wave_package.inuit`
- Formation family: `constant:independence_wave_decision.formation_family_inuit_arctic_council`
- Event-log types: `inuit_arctic_register_package_type`, `inuit_arctic_council_formation_type`
- Seed trigger: `can_independence_wave_seed_inuit_package`
- Route triggers: `is_independence_wave_inuit_package`, `has_independence_wave_inuit_arctic_control`, `can_independence_wave_open_inuit_arctic_register`, `can_independence_wave_map_inuit_arctic_petitions`, `can_independence_wave_proclaim_inuit_arctic_council`, `has_independence_wave_inuit_arctic_council_failure`
- Route effects: `independence_wave_open_inuit_arctic_register_effect`, `independence_wave_map_inuit_arctic_petitions_effect`, `independence_wave_proclaim_inuit_arctic_council_effect`, `independence_wave_finish_inuit_arctic_council_integration`, `independence_wave_discredit_inuit_arctic_council`
- Focuses: `independence_wave_inuit_arctic_register`, `independence_wave_inuit_arctic_petitions`
- Decisions/missions: `independence_wave_open_inuit_arctic_register`, `independence_wave_map_inuit_arctic_petitions`, `independence_wave_proclaim_inuit_arctic_council`, `independence_wave_integrate_inuit_arctic_council`
- Idea: `independence_wave_inuit_arctic_council_spirit`

## Asset and flag handling

No new flags were created or edited. Vanilla `INU` already provides ideology/base/medium/small flags, country history, localisation, the `INU_inuit_council` character, and council portrait wiring. This tranche reuses existing Event 006 local-polity decision/focus/idea icon families and does not need placeholder art.

## Validation

- Offline Paradox wiki references and vanilla documentation were consulted before the implementation tranche.
- Vanilla evidence checked directly:
  - `history/countries/INU - Inuit.txt` uses capital `463` and comments the core set `463`, `864`, `472`, `683`, `466`, `332`, `101`, `861`.
  - `common/decisions/CHL.txt` has the vanilla `CHL_mapuche_liberate_inuit` precedent that dynamically adds the same core set before transfer.
  - Vanilla INU country localisation, character, portrait, and flag assets exist.
- Script brace balance: clean for all touched Event 006 script files.
- Unsupported operators: no `<=` or `>=` found in touched script files.
- Localisation format: `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` remain UTF-8 with BOM and have no `:0` keys.
- Focus coverage: `common/national_focus/006_independence_wave_focus.txt` now has 87 focus blocks, 87 focus ids, and no missing focus name or description localisation.
- Workbook validation: `docs/spreadsheets/chaos_redux_events_catalog.xlsx` opens/converts through LibreOffice headless and contains no `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, or `#NAME?` tokens.

## Remaining risks and gaps

- This is a bounded starter package tranche. Event 006 as a full source-spec pack remains incomplete until future packages, formables, overlays, GUI states, assets, catalog rows, and final validation are closed.
- Optional vanilla Inuit liberation states `875` and `650` were intentionally not included in this first Event 006 package to avoid widening the first release beyond the documented Arctic core set.
- No in-game live-session validation was performed in this tranche.

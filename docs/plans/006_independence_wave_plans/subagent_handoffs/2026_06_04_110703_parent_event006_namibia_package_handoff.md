# Parent Handoff: Event 006 Namibia Land Council Package

## Scope

Added a vanilla-backed `NMB` Namibia local-polity package for Event 006 Independence Wave.

## Gameplay identifiers

- Package flag: `independence_wave_package_namibia`
- Package id constant: `constant:independence_wave_package.namibia`
- Formation family: `constant:independence_wave_decision.formation_family_namibia_land_council`
- Event-log types:
  - `constant:independence_wave_event_log.namibia_land_council_formation_type`
  - `constant:independence_wave_event_log.namibia_land_records_package_type`
- Seed trigger: `can_independence_wave_seed_namibia_package`
- Package trigger: `is_independence_wave_namibia_package`
- Control trigger: `has_independence_wave_namibia_land_control`
- Focuses:
  - `independence_wave_namibia_land_records`
  - `independence_wave_namibia_land_petitions`
- Decisions and mission:
  - `independence_wave_open_namibia_land_records`
  - `independence_wave_map_namibia_land_petitions`
  - `independence_wave_proclaim_namibia_land_council`
  - `independence_wave_integrate_namibia_land_council`
- Startup spirit: `independence_wave_namibia_land_council_spirit`

## Vanilla reference

- Vanilla tag: `NMB`
- Vanilla history file: `~/projects/Hearts of Iron IV/history/countries/NMB - Namibia.txt`
- Vanilla capital/core anchor: state `541` Khomas from `~/projects/Hearts of Iron IV/history/states/541-South West Africa.txt`
- Vanilla assets: `NMB_democratic.tga`, `NMB_communism.tga`, `NMB_fascism.tga`, `NMB_neutrality.tga` in base, medium, and small flag folders.

## Implementation notes

- The package is gated to chaos tier IV/V, inactive `NMB`, and weakened host control of Khomas.
- The initial release uses vanilla `NMB` core state `541`; no new tag, country history, leader, portrait, or flag assets were created.
- Reduced-territory release anchoring now prefers Khomas for `NMB`.
- Formation Ledger routing mirrors existing local-polity packages: records, petition map, proclamation, and post-formation integration mission.
- The package records both a package milestone and a formation milestone in the Event 006 event log.
- The Event 006 catalog workbook marker was updated from `93-focus` to `95-focus`.

## Files changed

- `common/ai_strategy/006_independence_wave.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

## Asset stance

No new flags were created. The package uses vanilla `NMB` flag assets and existing Event 006 local-polity focus, decision, and idea sprites.

## Validation status

Validated after implementation:

- Focus block count is `95`; `ai_will_do` count is `95`; `completion_reward` count is `95`.
- No missing focus localisation was found for the Event 006 focus tree.
- Namibia decision localisation was found for all four new decisions/mission.
- Namibia package label, spirit, requirement tooltip, integration failure/success tooltips, and event-log GUI keys were found.
- Brace balance passed across the touched Event 006 script and localisation files.
- Unsupported-operator scan found no `<=` or `>=`.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` still have UTF-8 BOMs, no `:0` keys, and no duplicate localisation keys.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` has the `95-focus` marker, passed `unzip -t`, and opened/re-exported through LibreOffice headless conversion.
- Cross-reference check found the Namibia seed, reduced anchor, classification, focus, decision, AI, event-log, docs, and localisation wiring.
- Event005 scan found only pre-existing Event006 origin/collision guards and shared GUI event-log routing, not a Namibia-specific Event005 dependency.
- Bounded country-package audit handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_111359_namibia_land_council_country_package_audit.md`.

Remaining risk: static validation only; no in-game or full Clausewitz parser validation was run.

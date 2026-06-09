# Event 006 Maya Package Parent Handoff

Date: 2026-06-04

## Scope

Implemented the `iw_pkg_maya` Maya Yucatan Assembly package as a bounded Event 006 Independence Wave local-polity tranche.

This tranche does not claim full Event 006 completion.

## Vanilla evidence

- Vanilla `MAY` is registered in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Vanilla `history/countries/MAY - Maya.txt` has capital `475` and comments the intended core set `313`, `475`, `476`, and `474`.
- Vanilla `common/characters/MAY.txt` defines `MAY_maya_council`.
- Vanilla `common/decisions/CHL.txt` dynamically adds MAY cores on `313`, `475`, `476`, and `474` before releasing/transferring the Maya tag.
- Vanilla `gfx/flags` includes MAY root, medium, and small ideology flags.

## Gameplay implementation

- Added high-chaos MAY package seed gate through state `475`.
- Added temporary dynamic MAY core seeding on states `313`, `474`, `475`, and `476`.
- Added cleanup that removes temporary MAY cores if MAY does not release and clears temporary seed flags if it does.
- Added reduced release anchor priority for MAY on state `475`, so the first start is Chiapas only.
- Added MAY startup identity:
  - `independence_wave_package_maya`
  - local-polity package candidate flag
  - package id `constant:independence_wave_package.maya`
  - formable family `constant:independence_wave_decision.formation_family_yucatan_assembly`
  - idea `independence_wave_maya_yucatan_assembly_spirit`
- Added Formation Ledger decisions and matching focus pair:
  - `independence_wave_open_maya_council_records`
  - `independence_wave_map_maya_peninsula_petitions`
  - `independence_wave_proclaim_maya_yucatan_assembly`
  - `independence_wave_integrate_maya_yucatan_assembly`
- Added delayed claims on states `313`, `474`, and `476` only after peninsula petition mapping.
- Added formation and integration checks requiring independence and owned/controlled state `475`.
- Added event-log recording helpers and display mappings for:
  - Maya council records package row
  - Maya Yucatan Assembly formation row

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Assets and flags

No new flag artwork was required.

No files under `gfx/flags`, `common/country_tags`, `common/countries`, `history/countries`, or `history/states` were changed for this tranche. The implementation reuses vanilla MAY flags, country history, council leader, and portrait data.

## Validation

Parent checks:

- `git diff --check` on touched gameplay, localisation, and docs files: clean.
- Forbidden inclusive-operator scan on touched files: no hits.
- Brace-count check on touched script files: all deltas `0`.
- Focus count in `common/national_focus/006_independence_wave_focus.txt`: `74`.
- Localisation BOM check:
  - `localisation/english/006_independence_wave_l_english.yml`: `efbbbf`
  - `localisation/english/chaosx_gui_l_english.yml`: `efbbbf`
- Localisation `:0` key scan on touched localisation files: no hits.
- Event-log key coverage check against `chaosx_gui_l_english.yml`: no missing keys.
- `git status --short -- gfx/flags common/country_tags common/countries history/countries history/states`: no output.

Subagent audit:

- Agent `019e9181-fe22-7f70-8867-fcaf5fc87a98` reported no findings.
- The audit independently confirmed vanilla MAY tag, history, core comments, council character, Chile dynamic-core precedent, and vanilla MAY flags.
- The audit confirmed no forbidden operators, localisation BOMs intact, no `:0` keys, brace balance, no new whole-world on-actions, and no flag/country/history touches.

## Remaining risks

- No live game-parser or in-game validation was run in this environment.
- This is one bounded package tranche. Full Event 006 completion still depends on the remaining package, asset, balance, catalog, and final audit work tracked in Event 006 docs and plans.

## Simplifications, omissions, and blockers

- No fallback or flag-art simplification was used.
- No Event 005 mechanics were used.
- No new bespoke MAY art was created because vanilla MAY assets are present and reused.

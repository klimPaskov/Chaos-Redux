# Event 006 Dahomey Package Audit

Date: 2026-06-04
Role: `chaosx_country_package_auditor`
Scope: Dahomey package tranche only (`iw_pkg_dahomey`, carrier `DAH`, anchor state `776`)

## Verdict

Pass with no Dahomey-blocking findings.

The implemented tranche matches the requested identity: `independence_wave_package_dahomey`, package id `constant:independence_wave_package.dahomey`, historical-return package type, and formation family `constant:independence_wave_decision.formation_family_palace_council`. It reuses vanilla DAH country support and does not require new flag, country, or history files.

## Vanilla Support Checked

- Vanilla tag exists: `/home/klim/projects/Hearts of Iron IV/common/country_tags/00_countries.txt` contains `DAH = "countries/Dahomey.txt"`.
- Vanilla country file exists: `/home/klim/projects/Hearts of Iron IV/common/countries/Dahomey.txt` uses African graphical culture and a defined country color.
- Vanilla history exists: `/home/klim/projects/Hearts of Iron IV/history/countries/DAH - Dahomey.txt` sets `capital = 776`, starting tech, politics, popularities, convoys, and recruits vanilla DAH characters/advisors.
- Vanilla state support exists: `/home/klim/projects/Hearts of Iron IV/history/states/776-Dahomey.txt` defines state id `776`, owner `FRA`, and `add_core_of = DAH`.
- Vanilla localisation exists: `/home/klim/projects/Hearts of Iron IV/localisation/english/countries_l_english.yml` defines DAH ideology names, `_DEF`, `_ADJ`, and base `DAH`.
- Vanilla flags exist for all four ideologies in large, medium, and small sizes under `/home/klim/projects/Hearts of Iron IV/gfx/flags/`.

## Wiring Audit

- Constants are present in `common/script_constants/006_independence_wave_constants.txt`:
  - event-log types `dahomey_palace_formation_type = 42`, `dahomey_palace_package_type = 43`
  - formation family `formation_family_palace_council = 13`
  - package id `dahomey = 14`
  - Dahomey costs, thresholds, gains, integration stage, and failure pressure.
- Seed gate and candidate exclusion are present in `common/scripted_triggers/006_independence_wave_triggers.txt`:
  - `can_independence_wave_use_candidate_tag` excludes DAH unless `can_independence_wave_seed_dahomey_package = yes`
  - `can_independence_wave_seed_dahomey_package` requires chaos tier IV/V, inactive DAH, non-capital state `776`, host control, host survival floor, and weakened host conditions.
- Release anchor is present in `common/scripted_effects/006_independence_wave_effects.txt`:
  - DAH package anchor chooses state `776` when owned and controlled by `independence_wave_current_host`, core of DAH, and not host-survival reserved.
  - the event release path calls `release = PREV`, then `independence_wave_setup_released_country`, core restoration, and release registration.
- Startup identity is present:
  - DAH clears ordinary release, sets `independence_wave_package_dahomey`, sets historical-return candidate, clears local-polity and strange candidates, clears strange identity, sets `independence_wave_package_id = constant:independence_wave_package.dahomey`, sets `independence_wave_package_type = constant:independence_wave_startup.historical_return_package`, sets `chaosx_independence_wave_formable_family = constant:independence_wave_decision.formation_family_palace_council`, grants old-state memory, and adds `independence_wave_dahomey_palace_council_spirit`.
- Focus loading is shared and valid for DAH:
  - `independence_wave_setup_released_country` calls `independence_wave_load_provisional_focus_tree`.
  - `independence_wave_load_provisional_focus_tree` loads `independence_wave_liberation_provisional_tree` for `is_independence_wave_release`.
  - focus nodes `independence_wave_dahomey_palace_council` and `independence_wave_bight_customs_charter` exist with package gates, rewards, bypasses, icons, and AI weights.
- Decisions/missions exist:
  - `independence_wave_open_dahomey_palace_council`
  - `independence_wave_register_bight_customs_charter`
  - `independence_wave_proclaim_dahomey_palace_council`
  - `independence_wave_integrate_dahomey_palace_council`
- Trigger/effect support exists:
  - package identity trigger, core-control trigger, open/register/proclaim gates, integration failure gate, open/register/proclaim effects, integration success/failure effects, and formation/package event-log effects.
- Idea support exists:
  - `independence_wave_dahomey_palace_council_spirit` is defined and intentionally reuses the existing Sokoto-style old-state spirit sprite.
- AI support exists:
  - `independence_wave_old_name_package_restraint` includes `independence_wave_package_dahomey` and `independence_wave_dahomey_palace_council_opened`.
- Scripted localisation exists:
  - package label scripted loc maps `constant:independence_wave_package.dahomey` to `independence_wave_package_label_dahomey`.
  - event-log scripted localisation maps both Dahomey log types across current list, history detail, event detail, selected detail title, and selected detail body classification.
- Localisation exists and is UTF-8 with BOM:
  - package label, idea, focus names/descriptions, decision names/descriptions, requirement tooltip, mission failure/success tooltips, and event-log labels are all present exactly once.
- Docs are aligned:
  - `docs/events/006_independence_wave.md` documents DAH state `776`, package route, vanilla data reuse, and no new flag/country/history art requirement.
  - `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` documents `iw_pkg_dahomey` in the African package matrix and implemented starter package table.

## Flag/Country/History Scope

No new Dahomey flag, country, or history files are required.

Repo checks found no DAH/Dahomey entries under mod `common/country_tags`, `common/countries`, `history/countries`, `history/states`, or `gfx/flags`, and `git status --short -- common/country_tags common/countries history/countries history/states gfx/flags` returned no changes.

## Syntax And Surface Checks

- No unsupported `<=` or `>=` appeared in the audited Event006 files.
- Brace-depth audit returned `brace_depth=0` for the audited script, localisation-script, focus, decision, idea, AI, and constants files.
- Required Dahomey localisation keys are present exactly once.
- `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` both have UTF-8 BOM.
- Package classification is valid for the requested historical-return package.
- Event-log mapping surfaces include both `dahomey_palace_formation_type` and `dahomey_palace_package_type`.

## Risks / Notes

- No Dahomey-specific blocker found.
- The audited files contain uneven indentation in some neighboring package blocks, but mechanical brace depth is balanced and the Dahomey blocks themselves have the expected gates and call sites. This is a readability risk, not a Dahomey package failure.
- I did not edit gameplay, localisation, GFX, country, history, or flag files.

## Validation Commands

```bash
rg -n "DAH|Dahomey|776" "/home/klim/projects/Hearts of Iron IV/common/country_tags" "/home/klim/projects/Hearts of Iron IV/common/countries" "/home/klim/projects/Hearts of Iron IV/history/countries" "/home/klim/projects/Hearts of Iron IV/history/states" "/home/klim/projects/Hearts of Iron IV/localisation/english"
find "/home/klim/projects/Hearts of Iron IV/gfx/flags" -maxdepth 3 \( -name "DAH.tga" -o -name "DAH_*.tga" -o -name "DAH.dds" -o -name "DAH_*.dds" \) -print | sort
rg -n "dahomey|DAH|iw_pkg_dahomey|palace_council|bight_customs|dahomey_palace|independence_wave_package_dahomey|formation_family_palace_council" common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/ideas/006_independence_wave_ideas.txt common/national_focus/006_independence_wave_focus.txt common/decisions/006_independence_wave_decisions.txt common/ai_strategy/006_independence_wave.txt common/scripted_localisation/006_independence_wave_scripted_localisation.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_gui_l_english.yml docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md
rg -n "<=|>=" common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/ideas/006_independence_wave_ideas.txt common/national_focus/006_independence_wave_focus.txt common/decisions/006_independence_wave_decisions.txt common/ai_strategy/006_independence_wave.txt common/scripted_localisation/006_independence_wave_scripted_localisation.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_gui_l_english.yml docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md
git status --short -- common/country_tags common/countries history/countries history/states gfx/flags
```

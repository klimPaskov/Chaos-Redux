# Parent Handoff: Event006 Expanded Report Call-Site Wiring

Date: 2026-06-04

## Scope

Parent implementation pass wiring the completed Event 006 report-event image set into bounded gameplay report popups.

This pass did not create assets, flags, country files, history files, or Event 005 integration. It uses already-registered report sprites from `interface/006_independence_wave_report_event_images.gfx`.

## Changed Files

- `events/006_independence_wave.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_parent_event006_report_callsite_wiring_handoff.md`

## Added Report Events

- `chaosx.nr6.6`: committee consolidation, `GFX_report_event_independence_wave_committee`
- `chaosx.nr6.7`: congress negotiation, `GFX_report_event_independence_wave_negotiation`
- `chaosx.nr6.8`: league secretariat, `GFX_report_event_independence_wave_league`
- `chaosx.nr6.9`: Border Commission, `GFX_report_event_independence_wave_border_commission`
- `chaosx.nr6.10`: patron brokers, `GFX_report_event_independence_wave_patron_brokers`
- `chaosx.nr6.11`: old-name formation, `GFX_report_event_independence_wave_old_name`
- `chaosx.nr6.12`: local-polity formation, `GFX_report_event_independence_wave_local_polity`
- `chaosx.nr6.13`: host-rump survival, `GFX_report_event_independence_wave_host_rump`
- `chaosx.nr6.14`: failed formation or containment proof, `GFX_report_event_independence_wave_failed_wave`
- `chaosx.nr6.15`: impossible-state dossier recognition, `GFX_report_event_independence_wave_impossible_state`

## Helper Effects

Added one-shot helper effects in `common/scripted_effects/006_independence_wave_effects.txt`:

- `independence_wave_show_committee_report_once`
- `independence_wave_show_negotiation_report_once`
- `independence_wave_show_league_report_once`
- `independence_wave_show_border_commission_report_once`
- `independence_wave_show_patron_brokers_report_once`
- `independence_wave_show_old_name_report_once`
- `independence_wave_show_local_polity_report_once`
- `independence_wave_show_host_rump_report_once`
- `independence_wave_show_failed_wave_report_once`
- `independence_wave_show_impossible_state_report_once`

Each helper sets a country flag before firing the report event, so repeated targeted decisions or missions do not spam the same popup for one actor.

## Gameplay Call Sites

The helpers are called from existing Event 006 effects, including:

- compact petition, delegate acceptance, mutual guarantees, regional compact formation, and compact secretariat recognition
- Border Commission filing
- patron broker exposure
- old-name and free-city recognition paths
- local-polity package proclamations
- host aftermath/rump survival handling
- failed package integration, failed compact integration, failed Timetable Authority integration, and failed containment review
- impossible delegate recognition and unmarked congress reveal

## Validation To Run

- `git diff --check`
- focused brace/trailing-whitespace scan on changed Event006 script/docs/localisation files
- unsupported comparison-operator scan on changed files
- report event id and localisation coverage scan for `chaosx.nr6.6` through `chaosx.nr6.15`
- report sprite reference check against `interface/006_independence_wave_report_event_images.gfx`
- Event006 localisation BOM and `:0` key scan
- country flag dirty-path check

## Remaining Risks

- This is presentation wiring for existing mechanics. It does not complete the broader Event 006 package-depth, animated UI, final spreadsheet/catalog, or final audit gates.
- The reports are intentionally one-shot per actor, so later repeated successes in the same category do not create extra popups.
- No new country flag art was created or modified.

# Event005 Parent Handoff: Secession Evolution Stage Names

Date: 2026-06-05

## Scope

Updated the Soviet Collapse secession evolution stage display names so the stage title is an actual crisis milestone instead of the chaos tier label.

## Changed Files

- `localisation/english/chaosx_gui_l_english.yml`

## Identifiers Updated

- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.title.stage_1`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.title.stage_2`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.title.stage_3`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.title.stage_4`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.event_detail`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_1`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_2`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_3`
- `chaosx.events_log.window.evolution_details.soviet_collapse_secession.body.stage_4`

## Result

The stage names now read:

- First Durable Secession
- Regional Cascade
- Union Unmade
- Maximum Rupture

The body text uses the same names as lead-ins. The separate chaos tier display remains intact through the existing event-log tier fields, so a stage can be shown alongside its current chaos tier without reusing the same label twice.

## Validation

- `git diff --check -- localisation/english/chaosx_gui_l_english.yml` passed.
- Confirmed `localisation/english/chaosx_gui_l_english.yml` still has a UTF-8 BOM.
- Scoped search found no remaining Soviet Collapse secession stage title/body keys using `Gathering Storm`, `Rising Chaos`, `Chaos Tier`, or `Terminal Rupture`.

## Remaining Notes

Scripted localisation already maps the secession stage ids to these keys, so no script edit was needed for this narrow naming fix. Broader spreadsheet/detail alignment remains part of the larger Event005 documentation pass.

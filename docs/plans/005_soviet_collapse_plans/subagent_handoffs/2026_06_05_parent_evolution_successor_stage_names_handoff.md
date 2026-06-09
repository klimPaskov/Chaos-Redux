# Parent Handoff: Soviet Collapse Successor Stage Names

Date: 2026-06-05

## Scope

Updated the remaining Soviet Collapse evolution labels that still described stages with chaos-tier wording instead of event-state names.

## Changed Files

- `localisation/english/chaosx_gui_l_english.yml`

## Changed Keys

- `chaosx.events_log.evolution.type.soviet_collapse_high_chaos`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title.event_detail`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title.stage_3`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title.stage_4`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title.totalen_successor`
- `chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title.world_collapse_successor`
- matching `body`, `body.event_detail`, `body.stage_3`, `body.stage_4`, `body.totalen_successor`, `body.world_collapse_successor`, `body.civilian_factory`, `body.military_factory`, and `body.successor`

## Behavior

The player-facing successor mutation stages now read as named crisis developments:

- Parallel Authorities Take Office
- Fringe Authorities Seize Ministries
- Parallel Successor Wave
- Fringe Successor Wave

The separate UI chaos-tier metadata remains unchanged because it is a summary field, not the evolution stage name.

## Validation

- Confirmed `localisation/english/chaosx_gui_l_english.yml` still has UTF-8 BOM.
- Ran `git diff --check -- localisation/english/chaosx_gui_l_english.yml`.
- Scanned Soviet Collapse evolution detail title keys for raw tier labels: `Calm World`, `Gathering Storm`, `Rising Chaos`, `Chaos Tier`, `Totalen Chaos`, `World Collapse`, `High-Chaos`, and `Extreme Successor`.
- Confirmed no `gfx/flags` files are touched.

## Remaining Risks

- This handoff only covers the naming/text request. It does not complete the wider Event005 focus tree, release pacing, decision visibility, or chaos-country depth cleanup.

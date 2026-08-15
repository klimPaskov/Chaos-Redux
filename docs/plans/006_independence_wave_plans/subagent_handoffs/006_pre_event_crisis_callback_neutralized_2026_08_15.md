# Event 006 pre-event callback neutralization — 2026-08-15

## Disposition

The public Event 006 report is the first player-facing Independence Wave entry point. The hidden `chaosx.nr6.3` callback no longer launches a standalone incident, applies pressure, queues a wave, records a crisis outcome, or fires the public report.

## Source change

`events/006_independence_wave.txt` now treats `chaosx.nr6.3` as retired compatibility cleanup only. Its immediate block clears stale crisis queue, requester, receipt, origin, active, blocked, abandoned, and retry state without calling the planner or any crisis consequence/history effect.

The deleted pre-event decision/category and removed crisis cost/title localisation remain covered by `006_pre_event_crisis_surface_removed_2026_08_15.md`. The old scripted crisis constants/effects/triggers remain parser-compatibility sources only; the opening trigger is hard-disabled and no current decision/category caller exists.

## Evidence

- Targeted `rg` found no live `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, or `independence_wave_cost_pre_wave_crisis` keys in current decision/localisation/event surfaces.
- Mandatory `hoi4.event_inspect` for `chaosx.nr6.3` returned `EVENT_INSPECTED_PARTIAL`, revision `8ac996f680565cfe7d19f1fba4f12dc0c9c9bb81a0d620dfd20ace9b8a9ccd5a`, with zero selected blocking diagnostics; workspace-wide helper/lifecycle projection remains deferred by the MCP server.
- Mandatory `hoi4.event_render` state view returned `EVENT_RENDERED_PARTIAL` for the same revision and produced source-linked JSON/SVG/PNG artifacts; the same workspace-wide deferral is recorded, not treated as a completion claim.

## Boundaries

This cleanup does not remove post-event host-response events, founding projects, evolution incidents, or active-origin decision categories. It does not widen or alter central adapter, attestation, scenario-preflight, or Join lists.

# Fallout Ash-week orientation event-log proof

Status: dormant additive substrate. The five orientation components remain
uncredited toward the 660-block release floor until an approved scheduler
caller, coverage ledger, activation gate, and runtime gate are live. The shared
Event Log detail route is statically proven below.

## History identity

`fallout_orientation_log.history_id` is `9110` in
`common/script_constants/fallout_consolidated_constants.txt`. It uses the
existing `event_system_event_type.fallout_country_memory` type and the shared
`record_events_log_system_history_entry` API. The writer never changes
`global.last_fired_event_id`, so ordinary event history is not reassigned to an
orientation result.

`fallout_orientation_record_history` in
`common/scripted_effects/fallout_consolidated_effects.txt`
is called from the authenticated orientation resolver only after the five
receipt arrays accept the component. It writes one row for a newly recorded
component and stores the transition generation plus component as the duplicate
guard. A retry of the same component in the same generation cannot append a
second row. The shared views are refreshed after the system row is committed.

## Payload matrix

Payloads use `component * 100 + branch * 10 + outcome`. The fixed matrix has
45 reviewed payloads.

| Component | Branches | Payload families |
| --- | --- | --- |
| National orientation | household work, district settlement, emergency command | 111-113, 121-123, 131-133 |
| Capital condition | seal heat civic, disperse stores offices, evacuate poisoned core | 211-213, 221-223, 231-233 |
| Immediate resource crisis | ration, requisition, tailored | 311-313, 321-323, 331-333 |
| Government archetype | consolidate, division, rival | 411-413, 421-423, 431-433 |
| Character or institution | relief administration, security extraction, regional institution | 511-513, 521-523, 531-533 |

Each family has success, partial, and failure text. The invalid payload is
rendered as an unverified orientation receipt and cannot be emitted by the
writer’s input gate.

## Localisation and Event Log routing

`common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`
maps every payload to a dedicated text key. The name and detail routes are
registered in `GetEventsLogHistoryEventName` and
`GetEventsLogEventDetailDescription` in
`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.
`events_log_get_event_type_for_open_detail` recognizes history `9110` as a
Fallout memory row. Player-facing text is in
`localisation/english/fallout_consolidated_l_english.yml`
and uses the approved regional and government-aware orientation vocabulary.

## Static checks

- 45 payload selectors have a matching constant and localization key.
- The history id is routed through the system-history type and open-detail
  type helper.
- The writer is called only on a newly accepted result and clears its temporary
  system inputs after the shared row is appended.
- No scheduler activation flag, caller, or release-floor credit is written.
- No HOI4 process was launched. Runtime rendering and save/reload behavior are
  therefore still unobserved.

## Event Details route

The history row reaches the player-facing detail window through the existing
generic history path. A click on a history row stores the selected event id,
history type, date, sequence, payload, and actor in
`common/scripted_guis/chaosx_scripted_gui_events_log.txt`, then calls
`events_log_open_history_event_details_entry` in
`common/scripted_effects/chaosx_events_log_effects.txt`. That effect rebuilds
the open detail arrays. The detail window is
`events_log_event_details_window` in `interface/chaosx_events_log_popup.gui`.

The open-detail type helper recognizes `fallout_orientation_log.history_id`
`9110` as `event_system_event_type.fallout_country_memory`. The history detail
localisation dispatch recognizes the same id and returns
`fallout.event_log.orientation.detail`. The scripted selector
`GetFalloutOrientationEventLogDetail` maps all 45 payload values to dedicated
localisation keys. The history-name selector returns
`fallout.event_log.orientation.name` for the same row.

This is a source-level route proof only. No runtime click, payload rendering,
save reload, or multiplayer observation is claimed because HOI4 was not
launched.

## Remaining gates

The orientation caller remains dormant by contract. The full Ash-week block
coverage, scheduler activation, and live campaign review remain required before
this surface can receive release-floor credit.

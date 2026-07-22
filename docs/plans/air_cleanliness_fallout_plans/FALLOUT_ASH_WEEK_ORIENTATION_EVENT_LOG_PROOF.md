# Fallout Ash-week orientation event-log proof

Status: dormant additive substrate. The five orientation components remain
uncredited toward the 660-block release floor until an approved scheduler
caller, coverage ledger, event details surface, and runtime gate are live.

## History identity

`fallout_orientation_log.history_id` is `9110` in
`common/script_constants/fallout_world_end_event_constants.txt`. It uses the
existing `event_system_event_type.fallout_country_memory` type and the shared
`record_events_log_system_history_entry` API. The writer never changes
`global.last_fired_event_id`, so ordinary event history is not reassigned to an
orientation result.

`fallout_orientation_record_history` in
`common/scripted_effects/fallout_world_end_orientation_event_log_effects.txt`
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

`common/scripted_localisation/fallout_world_end_orientation_event_log_scripted_localisation.txt`
maps every payload to a dedicated text key. The name and detail routes are
registered in `GetEventsLogHistoryEventName` and
`GetEventsLogEventDetailDescription` in
`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.
`events_log_get_event_type_for_open_detail` recognizes history `9110` as a
Fallout memory row. Player-facing text is in
`localisation/english/fallout_world_end_orientation_event_log_l_english.yml`
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

## Remaining gates

The orientation caller remains dormant by contract. The full Ash-week block
coverage, event detail window proof, scheduler activation, and live campaign
review remain required before this surface can receive release-floor credit.

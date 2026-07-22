# Shared Event Log scripted effects

## `record_events_log_system_history_entry`

This additive helper serves system-owned histories that use dedicated history
card identities and are not ordinary `global.all_events` rows.

Scope: the system country that owns the record.

Temporary inputs:

- `events_log_system_event_id`
- `events_log_system_event_type`
- `events_log_system_payload`
- `events_log_system_actor`
- `events_log_system_has_actor`
- `events_log_system_secondary_actor`
- `events_log_system_has_secondary_actor`

Outputs and side effects:

- Prepends one row to every shared Event Log history array.
- Leaves `global.last_fired_event_id` unchanged.
- Uses the supplied actor values instead of ordinary event actor dispatch.
- Does not refresh player windows itself. A system caller must finish its
  system-specific payload ledger and then call
  `refresh_events_log_system_history_views`.
- Does not add an on action or scheduled world iteration.

The Fallout NZL package is the first caller. Its four history cards use
`constant:event_system_event_type.fallout_country_memory` and preserve a
separate snapshot ledger keyed by the resulting history sequence. The helper
is intentionally narrow and does not alter ordinary event catalogue
population or event firing.

## `refresh_events_log_system_history_views`

Scope: the system country after its shared history row and private payload
ledger are both committed.

Outputs and side effects:

- Rebuilds the History, Events, and open Event Details surfaces for human
  countries that currently have the Event Log open.
- Rebuilds the NZL Fallout package card when its world-end detail surface is
  already open.
- Performs no recurring or scheduled iteration.

## `events_log_get_event_type_for_open_detail`

Scope: player country during the open Event Details rebuild.

Input: temporary `event_id`.

Output: temporary `event_type`. The four Fallout history-card identities
resolve to `constant:event_system_event_type.fallout_country_memory`. Every
other id delegates to the existing `get_event_type` effect.

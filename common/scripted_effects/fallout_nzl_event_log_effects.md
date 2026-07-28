# Fallout NZL Event Log scripted effects

This file documents `common/scripted_effects/fallout_nzl_event_log_effects.txt`.
The package remains dormant because its activation helper has no caller. These
history helpers add no on action or scheduler.

## Helper map

### `fallout_nzl_event_log_set_payload`

- Scope: current NZL country.
- Inputs: temporary `fallout_nzl_event_log_family`, current
  `fallout_nzl_chain_choice`, `fallout_nzl_chain_result`, and the current
  external no-partner receipt.
- Output: temporary `fallout_nzl_event_log_payload`.
- Side effects: none beyond temporary variables.
- The payload identifies family, choice, and result. External no-partner
  branches use separate payload values.

### `fallout_nzl_record_opening_event_log`

- Scope: current NZL country.
- Inputs: current opening choice and result after `.130` applies the outcome.
- Outputs: one shared Event Log row and one country-memory snapshot.
- Side effects: sets a generation receipt flag and stores the transition
  generation for duplicate protection.
- Package reset preserves this durable receipt. A same-generation reactivation
  therefore cannot append the opening row twice, while a later transition
  generation remains eligible.
- Call site: `events/fallout_world_end_events.txt`, resolver `.130`.

### `fallout_nzl_record_domestic_event_log`

- Scope: current NZL country.
- Inputs: current domestic choice and result after `.136` applies the outcome.
- Outputs and side effects: same shape as the opening helper.
- Package reset preserves the domestic generation receipt for the same reason.
- Call site: `events/fallout_world_end_events.txt`, resolver `.136`.

### `fallout_nzl_record_external_event_log`

- Scope: current NZL country before external cleanup.
- Inputs: current external choice and result, current route, and the stored
  partner target when the transaction has one.
- Outputs: one shared Event Log row and one snapshot per resolved transaction.
- Side effects: records the exact partner as secondary actor when present and
  sets a transaction receipt flag. The start-transaction helper clears that
  flag before a new transaction, so repeated external contacts remain visible.
- Call site: `fallout_nzl_close_external_chain`, before transaction cleanup.

### `fallout_nzl_record_external_mission_event_log`

- Scope: current NZL country before rescue-passage cleanup.
- Inputs: current partner transaction and completed rescue-passage mission.
- Outputs: one external history row with the exact partner, a Rescue Passage
  choice token, a success result, and the four values after the mission reward.
- Side effects: uses the same transaction deduplication receipt as the authored
  external chain.
- Call site: `fallout_nzl_offer_rescue_passage` timeout effect.

### `fallout_nzl_record_late_event_log`

- Scope: current NZL country.
- Inputs: current Year 10 choice and result.
- Outputs and side effects: one shared Event Log row, one snapshot, and a
  generation receipt flag.
- Package reset preserves the Year 10 generation receipt for the same reason.
- Call site: `fallout_nzl_record_year_ten_order`.

### `fallout_nzl_event_log_append_snapshot`

- Scope: current NZL country.
- Inputs: system-event temporary values prepared by the record wrapper and the
  four live package values.
- Outputs: parallel global arrays keyed by the shared history sequence.
- Stored fields: root identity, payload, date, exact Fallout country-memory
  id, choice, result, domestic prior-opening result, route, NZL actor,
  optional partner actor, four values, and transition generation.
- Side effects: clears only its own temporary snapshot values.

### `fallout_nzl_load_open_history_payload`

- Scope: player country while shared Event Details rebuilds.
- Inputs: selected Fallout history-card id and selected sequence, or the open detail's
  latest matching history sequence.
- Outputs: selected payload and detail variables for date, actor, choice,
  result, route, four values, generation, and optional partner scope.
- Side effects: clears stale detail variables before loading the stored row.
  It reads global history and snapshot arrays only. It does not read current
  NZL values, so later decisions cannot rewrite old details.
- Call site: shared `events_log_rebuild_open_event_details_view`.

### `fallout_nzl_prepare_event_log_card`

- Scope: dormant post-consequence NZL country-memory package view.
- Inputs: current package receipts and the NZL snapshot ledger.
- Outputs: one package-card view for the latest relevant transition generation.
- Current package behavior: after at least one current-generation memory is
  committed, reads the four live values, current route, and current proven
  aggressor receipt from `NZL`, then writes the display snapshot on the human
  country viewing a future post-consequence package view.
- Historical behavior: uses the latest snapshot from the newest stored
  transition generation. A newly reactivated package with no memory in its
  current generation continues to show the newest historical generation.
- Chain summary: loads the latest opening, domestic, external, and Year 10
  outcomes and dates from that same generation only.
- Partner summary: names up to the two distinct Pacific contacts available to
  this pilot and never fabricates a partner.
- Call site: none. The helper is dormant and must not be wired to the Fallout
  consequence boundary. The consequence has no Event Details row, evolution
  entry, or ordinary event-log registration. Only later NZL country-memory
  history may use this package view.

## Shared Event Log contract

`record_events_log_system_history_entry` in
`common/scripted_effects/chaosx_events_log_effects.txt` appends a system row
without changing `global.last_fired_event_id`. It writes the same parallel
history arrays as ordinary Event Log entries and uses a dedicated type value.
The shared row payload stores the result band needed by the compact History
line. The NZL private ledger stores the detailed family, choice, and result
payload used by exact Event Details.
The NZL wrapper appends its sequence-keyed payload next, then calls
`refresh_events_log_system_history_views`. The only `every_country` operation
is that bounded visible-window refresh. NZL adds no recurring hook.

History-card identities are `9101`, `9102`, `9103`, and `9104`. The authored
Fallout event suffixes remain `.127`, `.133`, `.139`, and `.147`, but they are
not borrowed as shared Event Log ids. The history cards are not placed in
`global.all_events`, do not appear in the ordinary Events catalog, and do not
replace Event 2 or create a manual Fallout scenario row.

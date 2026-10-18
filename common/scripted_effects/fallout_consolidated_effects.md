# Fallout consolidated scripted effects

## Fallout NZL Event Log scripted effects

This section documents the NZL Event Log helpers in `common/scripted_effects/fallout_consolidated_effects.txt`.
The package remains dormant because `fallout_nzl_activate_lifeboat_package` is reached only from the dormant B7 successor slice, `fallout_successor_b7_run_vertical_slice`, which has no live caller.
These history helpers add no on action or scheduler.

## Delayed-result target-loss cancellation

### `fallout_event_cancel_target_lost`

- Scope: COUNTRY.
- Input: temporary `fallout_event_requested_ticket`, the unissued delayed row to cancel.
- Defaults: sets `fallout_event_requested_outcome` to `cancelled_before_choice` and `fallout_event_requested_cancellation_reason` to `target_lost` itself.
- Output: `fallout_event_transaction_accepted` from `fallout_event_cancel_delayed_result`.
- Side effects: the delayed row becomes cancelled; the caller keeps its own `fallout_event_<N>_target_invalidated` flag, history stage, and any `fallout_event_prepare_delayed_cleanup` handoff.
- Call sites: the result and callback resolvers of events 579, 586, 600, 607, 614, 621, 740, and 747.
- Usage: `set_temp_variable = { fallout_event_requested_ticket = fallout_event_614_result_ticket } fallout_event_cancel_target_lost = yes`

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

## Fallout NZL lifeboat scripted effects

This reference documents the NZL Lifeboat runtime helpers in `common/scripted_effects/fallout_consolidated_effects.txt`.
The package remains dormant until its allocator receipts are current.
These helpers add no activation caller of their own.

### `fallout_nzl_add_chain_context_score`

Scope: country (the NZL package owner).

Inputs:

- `fallout_nzl_chain_score` is the caller's current value average in a
  temporary variable.
- `fallout_nzl_prior_result` is a temporary result token supplied by the
  caller. Callers use `fallout_nzl_chain_result.none` when no earlier chain is
  available.
- `fallout_nzl_chain_choice`, route flags, `has_war`, and the five package
  states provide current context.

Outputs and side effects:

- Adds deterministic state-control, choice, route, war-pressure, and prior-result adjustments to `fallout_nzl_chain_score`.
- Uses only temporary variables and clears both helper temporaries before it
  returns.
- Reads all tuning values from the `fallout_nzl_score` script-constant
  category. No score magic numbers are embedded in the effect.

Call sites:

- `fallout_nzl_calculate_opening_result`
- `fallout_nzl_calculate_domestic_result`
- `fallout_nzl_calculate_external_result` (partner branch)
- `fallout_nzl_calculate_late_result`

### `fallout_nzl_clear_partner_response_receipt`

Scope: partner country. Clears the three response flags and the generation
receipt written by events `chaosx.fallout.141` and `chaosx.fallout.142`.

It is called through the stored partner event target before a new external
transaction, package reset, or external-chain cleanup. This prevents a stale
partner response from surviving a generation change while retaining the
response flags for any current-generation diagnostics.

### Numbered sea-road helpers

`fallout_nzl_activate_sea_road_licensing` records the current Fallout transition generation and opens the existing Fishery Quota Compact. The focus caller retains the immediate Sea-Lane Security gain and does not remove convoys.

`fallout_nzl_issue_sea_road_patrol_window` fails closed unless the licence receipt is current. It writes one 90-day timed flag through a temporary duration variable, stamps the current generation, increments the licence serial, and adds the visible `fallout_nzl_quiet_seas_patrol_window` dynamic modifier. Reissuing the window refreshes the same timed flag and does not create a second countdown.

`fallout_nzl_close_quiet_seas_patrol_window` clears the timed flag, generation receipt, and visible modifier during package cleanup. Natural expiry satisfies the modifier's `remove_trigger`, so no recurring on action is required.

The reusable Fishery Quota Compact pays five convoys under current licensing, raises Food Security and Sea-Lane Security, and renews the window. The one-shot Quiet-Seas Patrol pays ten convoys under current licensing, retains its navy-experience and factory commitments, raises Sea-Lane Security by twelve, and renews the same window. Their non-licensed branches retain the earlier costs and results.

### `fallout_nzl_add_sea_road_score`

Scope: country (the NZL package owner).

Input: temporary `fallout_nzl_chain_score` after the shared context score.

For a current isolation-route licence, the helper adds four points when the patrol window is current and subtracts four points when it has lapsed. Only the external and Year 10 result calculators call it. Opening, domestic, and humanitarian scoring remain unchanged. Both values come from `fallout_nzl_sea_road` script constants.

### `fallout_nzl_start_external_transaction`

Scope: NZL country. Chooses the deterministic lowest-id valid partner. When a
partner exists, it records the current generation and target. When no partner
exists, it records a generation-bound no-partner receipt and dispatches the
authored human (`.139`) or AI (`.140`) external choice event. The choice event
continues to own payment, delayed result resolution (`.144`), visible result,
and cleanup.

### Runtime character roster

`fallout_nzl_recruit_package_characters` is idempotent on each token and uses
`generate_character` with stable `token_base`, inline portraits, and the full
country-leader/advisor role definition. The former static definitions in the NZL section of
`common/characters/fallout_consolidated_characters.txt` are intentionally empty
apart from an ownership note, so the engine cannot load duplicate token
definitions.

### Dormant activation and Year 10 clock

`fallout_nzl_activate_lifeboat_package` remains dormant outside the B7 vertical slice. It is called from `fallout_successor_b7_materialize_dynamic_nzl` and from `fallout_successor_b7_run_vertical_slice` in `common/scripted_effects/fallout_consolidated_effects.txt`, and neither path has a live caller outside the slice. The slice caller reaches it only after the guarded existing-tag assignment commits its current-generation receipts. After the receipt gate passes, it resets NZL-owned package state and writes a timed `fallout_nzl_before_year_ten` country flag for 3,650 days. The duration field uses the file-scoped literal `@FALLOUT_NZL_YEAR_TEN_DAYS`, mirrored by `constant:fallout_nzl_duration.year_ten` for shared tuning and documentation surfaces. `fallout_nzl_year_ten_values_are_ready` requires the timed flag to have expired. Reset clears the old flag before any later valid activation writes a fresh one.

### Bounded formation placement

`fallout_nzl_create_starting_force_family` remains guarded by the exact NZL
state package and one generation receipt. Its three two-battalion formations
use explicit province priorities for Wellington (`1814`), Auckland (`4543`),
and Canterbury (`2197`) while retaining the state scope and enemy-province
spawn restriction. `fallout_nzl_create_extra_escort_formation` places its
one-shot Southern Escort Volunteers at Auckland province `4543`.

### Pirate terminal outcomes

`common/on_actions/fallout_consolidated_on_actions.txt` enters NZL scope for
capitulation, peace-conference completion, and annexation. Each path matches
the exact stored aggressor before calling `fallout_nzl_record_pirate_settlement`.
Annexation therefore closes when any actor annexes the recorded aggressor and
does not settle an unrelated country.

`fallout_nzl_record_pirate_defeat` is the paired losing terminal helper.

Scope: NZL country.

Inputs:

- the current Lifeboat package
- a generation-bound exact pirate-war receipt
- no current settlement or defeat receipt

Outputs and side effects:

- writes `fallout_nzl_pirate_defeat_recorded`
- writes `fallout_nzl_pirate_defeat_generation`
- closes the force-settlement decision

The capitulation and peace-conference hooks call it only when New Zealand is
the defeated side. This unlocks the late isolation focus with a reduced
security reward and a trust loss. It does not counterfeit a settlement and it
does not satisfy the Closed Seas achievement settlement condition.

The four hidden delayed resolver events admit the scheduled scope without a
tag-only trigger. Their immediate result branch remains package- and
generation-guarded. When that branch is stale, the existing close helper runs
without the package gate so stale callbacks still clean their runtime state.

### Tuning and validation notes

The `fallout_nzl_score` constants are shared by all four result families and
keep state weights, choice adjustments, route pressure, war pressure, and
prior-result quality in one tuning table. Settlement surrender uses an
inclusive `check_variable` comparison so the forced-settlement boundary is
reachable. Delayed resolver events `.130`, `.136`, `.144`, and `.150` no longer
have a tag-only admission trigger. Their immediate blocks still require the
current package and current chain receipts before applying any result.

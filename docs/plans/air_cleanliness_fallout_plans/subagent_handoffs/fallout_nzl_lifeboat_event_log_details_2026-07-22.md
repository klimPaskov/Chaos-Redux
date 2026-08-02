# Fallout NZL Lifeboat Event Log and Event Details handoff

Current-source note: this handoff describes a dormant post-consequence
country-memory package. The Fallout consequence itself has no Event Details
row, evolution entry, ordinary event-log row, or world-end details opener.
Any package summary must remain separate from that consequence boundary.

## Status

Implemented as dormant Fallout-owned country-memory history integration. The
package still has no activation caller. Event 2 remains Zombie-only. No
ordinary event row, SCN-014 row, world-end scenario substitute, or new
super-event was added. These blocks remain outside the 660-event release
floor.

## Architecture proof

The shared Event Log stores numeric history-card ids in parallel global arrays
and opens the shared Event Details view by id and history sequence. The four
NZL history-card identities are dedicated system ids:

- `9101` for the opening chain
- `9102` for the domestic chain
- `9103` for external transactions
- `9104` for the Year 10 chain

The authored Fallout roots remain `chaosx.fallout.127`, `.133`, `.139`, and
`.147`. They are never borrowed as shared history ids. The dedicated ids are
not registered in `global.all_events`, so they cannot enter the ordinary
Events catalogue. Shared type value 4 and history filter value 4 expose them
as Fallout memories without classifying them as major, repeatable, or
fire-once events.

`record_events_log_system_history_entry` appends a row without mutating
`global.last_fired_event_id`. Its shared payload is the compact result band
used by the History row. The NZL wrapper appends its exact sequence-keyed
detailed payload before the bounded visible-window refresh runs. The NZL
carrier is the primary actor. Each external transaction stores the exact
accepted partner as the secondary actor when one exists. Existing shared
history-array sanitisation and visible-window refresh are retained.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call site |
| --- | --- | --- | --- | --- | --- |
| `fallout_nzl_event_log_set_payload` | NZL country | family, choice, result, no-partner state | family, choice, and result payload | temporary only | record wrappers |
| `fallout_nzl_record_opening_event_log` | NZL country | current opening choice and applied result | one shared row and one NZL ledger row | one receipt per transition generation | resolver `.130` |
| `fallout_nzl_record_domestic_event_log` | NZL country | current domestic choice and applied result | one shared row and one NZL ledger row | one receipt per transition generation | resolver `.136` |
| `fallout_nzl_record_external_event_log` | NZL country before cleanup | current external choice, result, route, and partner | one shared row and one NZL ledger row per transaction | transaction receipt | `fallout_nzl_close_external_chain` |
| `fallout_nzl_record_external_mission_event_log` | NZL country before cleanup | completed rescue-passage transaction and exact partner | one successful external row with Rescue Passage choice | transaction receipt | rescue-passage timeout |
| `fallout_nzl_record_late_event_log` | NZL country | current Year 10 choice and result | one shared row and one NZL ledger row | one receipt per transition generation | `fallout_nzl_record_year_ten_order` |
| `fallout_nzl_event_log_append_snapshot` | NZL country | shared-row temporaries and four live values | parallel NZL ledger arrays keyed by shared sequence | clears local temporaries | record wrapper |
| `fallout_nzl_load_open_history_payload` | player country | selected history-card id and exact sequence | stored date, actor, partner, choice, result, route, values, and generation | clears stale detail variables | shared detail rebuild |
| `fallout_nzl_prepare_event_log_card` | player country | current package or stored NZL ledger | current or newest-generation package summary | writes display variables only | dormant post-consequence package view |
| `record_events_log_system_history_entry` | shared logger | system id, type, payload, and actors | shared history arrays | no presentation refresh until the private ledger commits | NZL record wrapper |
| `refresh_events_log_system_history_views` | shared presenter | completed shared and private rows | refreshed visible History, Events, Event Details, and open NZL package card | bounded human-window iteration | NZL record wrapper after private append |

## Stored fields and generation isolation

`global.fallout_nzl_event_log_*_entries` are keyed by the shared history
sequence. Each row stores its dedicated id, payload, date, country-memory id
91, choice, result, domestic prior-opening result, route, NZL actor, optional
partner actor, Harbour Capacity, Food Security, Parliament Trust, Sea-Lane
Security, and transition generation.

Opening, domestic, and Year 10 generation receipts survive package runtime
reset. A same-generation reactivation cannot duplicate those rows, while a
later transition generation remains eligible. The history loader requires the exact selected sequence. The Fallout package
card first selects one transition generation. A current package uses the live
four values and current route only after it owns a memory in the current
generation. It scopes those live reads through NZL and writes the presentation
on each viewing human country. A historical package, or a newly reactivated package with no
current-generation memory, uses the newest stored generation and the latest
value row within that generation. Opening,
domestic, external, and Year 10 results are summarized only from the selected
generation. External contacts are deduplicated and the card names no more than
the two distinct partners supported by this pilot. The current proven pirate
aggressor is shown only while its current receipt remains valid.

## Constants and UI routing

`common/script_constants/event_system_constants.txt` owns the shared type
value `event_system_event_type.fallout_country_memory = 4`.
`common/script_constants/fallout_consolidated_constants.txt` owns the four
dedicated ids, family tokens, Rescue Passage choice, and payload identities.

The History filter includes Fallout memories. The shared history row displays
the exact result band. A partnered external row displays two flags, the partner
name, and a second navigation target. The shared history row and Event
Details title use dedicated localisation keys, not `chaosx.event_name.127`,
`.133`, `.139`, or `.147`. Trigger and enable or disable controls are hidden or
disabled for the system cards. The package card is not attached to a Fallout
world-end details surface. It does not add a manual scenario row or any
consequence registration.

## Engine references

The installed official `effects_documentation.md` documents `add_to_array`,
`clear_array`, `for_loop_effect`, and `while_loop_effect`. `add_to_array` with
`index = 0` inserts the new row and shifts older rows, matching the shared
history ordering. The installed `dynamic_variables_documentation.md`
documents the comparable and localisable `date` variable used for exact row
dates and `GetDateStringNoHour` output. Existing repository Event Log arrays
provide the precedent for storing country ids as actor scopes.

## Validation and remaining uncertainty

- Static review confirmed balanced braces and equal NZL parallel-array append
  counts.
- Static review confirmed unique dedicated history ids and 26 unique authored
  Fallout event blocks from `.127` through `.152`.
- Static review confirmed no ordinary Event 2 mapping, SCN-014 row, manual
  dispatch, recurring on action, activation caller, or Zombie-owned path.
- Player-facing NZL memory text contains no em dash, semicolon, placeholder,
  stale state name, or implementation-process wording.
- HOI4 was not launched, as instructed.
- The read-only HOI4 GUI inspection service closed its transport before it
  returned a result. No offline GUI render artifact was produced. Numeric
  actor-scope persistence, date persistence, save recovery, and multiplayer
  observation therefore remain runtime or tool-availability uncertainties.
- The final focused source audit passed both promoted corrections with no
  unresolved regression. See
  `2026-07-22_fallout_nzl_sea_road_event_log_completion_audit.md`.

## Files owned by this tranche

- `common/script_constants/event_system_constants.txt`
- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.md`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `interface/chaosx_events_log_popup.gui`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/decisions/fallout_consolidated_decisions.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_consolidated_l_english.yml`

## Blockers carried forward

This tranche does not authorize activation. Allocator and materialization
work, Samoa and Aotearoa conflicts, vanilla NZL AI-plan retirement, the blocked
radio adviser asset, exact manual-sweep runtime proof, map-return proof,
multiplayer host authority, SCN-014 registration, and the 660-event review
floor remain unresolved.

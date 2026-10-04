# Receiver-front reception intent effects

Source: [migration_reception_front_intent_effects.txt](migration_reception_front_intent_effects.txt).
Predicates: [migration_reception_front_intent_triggers.md](../scripted_triggers/migration_reception_front_intent_triggers.md).
Tuning: [migration_reception_front_intent_constants.txt](../script_constants/migration_reception_front_intent_constants.txt).

These effects keep a private, identity-only record on the receiving front state of an evacuation corridor.
The record lets the receiving country see in the migration map mode that civilians have been requested, that reception was paid for, or that it agreed to the passage.
It is presentation only.
It never moves people, binds a cohort or destination, grants route permission, changes services, reception load or capacity, reveals a decision category, registers a job, applies an outflow modifier, or adds a fourth headline value.
A failed or rejected record never changes the result of the mechanical action that tried to publish it.

## Storage

Each front state holds six aligned arrays, one row per live corridor that targets it:

| Array | Value |
|---|---|
| `migration_reception_front_intent_origins` | Origin state scope |
| `migration_reception_front_intent_generations` | Corridor route generation |
| `migration_reception_front_intent_requesters` | Requesting country ID |
| `migration_reception_front_intent_receivers` | Receiving country ID |
| `migration_reception_front_intent_cohorts` | Exact cohort ID |
| `migration_reception_front_intent_phases` | `requested` 1, `prepared` 2 or `agreed` 3 from `migration_reception_front_intent` |

`migration_reception_front_intent_schema_version` marks an initialized row set.
No people, amounts, capacity or route data are stored.
Several rows can coexist, so an older agreed passage and a newer pending request at the same front survive each other's terminal.

The cache written by the projection is `migration_reception_front_intent_cache_active` plus `migration_reception_front_intent_cache_origin_id`, `_generation`, `_requester`, `_receiver`, `_cohort` and `_phase`.
Map readers use only this cache.

## Effects

### `migration_refresh_reception_front_intent_projection`

Scope: FRONT state.
Inputs: none beyond the state's own arrays.
Output: temporary `migration_reception_front_intent_refresh_result` (1 when the whole row set was read, 0 otherwise); the caller declares it before the call when it reads it.
Behaviour: clears the cache, walks every row once and selects the current row with the lowest phase (requested before prepared before agreed), then the newest generation, then the lowest origin ID.
Rows whose origin contract no longer matches are ignored.
A misaligned row set, a malformed row, a duplicate current origin or an incomplete walk leaves the cache neutral.
Side effects: the cache only.

### `migration_record_reception_front_intent`

Scope: FRONT state.
Inputs: event targets `migration_reception_front_intent_origin`, `_requester` and `_receiver`; temporary `migration_reception_front_intent_request_proven`, `_reveal_proven`, `_setup_proven`, `_generation_request`, `_cohort_request` and `_phase_request`.
Output: temporary `migration_reception_front_intent_record_result`, declared by the caller.
Behaviour: requires a valid, preparable front owned and controlled by the receiver, a current exact origin contract and cohort, the existing reveal threshold and, for `prepared`, a proven paid setup.
For `prepared` and `agreed` it also requires full current headroom for the whole request.
It appends a new row, or raises the phase of the matching row; it never lowers a phase or overwrites a colliding identity.
All one-shot inputs are reset to zero on exit.

### `migration_clear_reception_front_intent`

Scope: FRONT state.
Inputs: temporary `migration_reception_front_intent_clear_proven`, `_clear_front_id`, `_clear_origin_id`, `_clear_generation`, `_clear_requester`, `_clear_receiver` and `_clear_cohort`, captured before the contract was torn down.
Output: temporary `migration_reception_front_intent_clear_result`.
Behaviour: removes exactly one matching row, refreshes the cache and resets every input.
Actors may already have ceased to exist; the stale row is still removed.

### `migration_publish_reception_front_intent_from_contract`

Scope: ORIGIN state of an evacuation corridor.
Inputs: temporary `migration_reception_front_intent_phase_request`, `_reveal_proven` and `_setup_proven`.
Behaviour: reads the origin's live corridor identity, saves the three event targets and calls `migration_record_reception_front_intent` on the front.
Relief corridors and incomplete identities publish nothing.

### `migration_retire_reception_front_intent_from_contract`

Scope: ORIGIN state.
Behaviour: captures the origin's corridor identity, unless the caller already supplied a captured tuple, and clears the matching row on its front.

### `migration_reception_front_intent_handle_control_change`

Scope: FRONT state whose owner or controller just changed.
Behaviour: walks the rows from the last to the first and removes every row whose recorded receiver is no longer a valid country that owns and controls the state.
Rows of a receiver that still holds the state survive.
Malformed metadata is left in place and only the cache is cleared.
This is a local walk of one state's rows, not a registry scan.

## Callers

| Seam | File | Phase or action |
|---|---|---|
| Successful evacuation offer submission | `humanitarian_corridor_submit_offer` in `humanitarian_corridor_effects.txt` | Publish `requested` |
| Successful paid reception preparation for the pending request | `migration_prepare_reception_services` in `migration_reception_preparation_effects.txt` | Publish `prepared` |
| Successful acceptance, before the receiver's pending mirror is cleared | `humanitarian_corridor_accept_offer` | Publish `agreed` |
| Measured, conserved passage | `humanitarian_corridor_record_evacuation` | Retire the row |
| Rejection, expiry, completion, attack, relation or control invalidation | `humanitarian_corridor_cleanup` | Retire the row |
| Front state changes owner or controller | `humanitarian_corridor_handle_state_control_change` | Prune rows of receivers that lost the state |

## Usage

```text
# ORIGIN state of a just-submitted evacuation corridor.
set_temp_variable = { migration_reception_front_intent_record_result = constant:migration_reception_front_intent.zero }
set_temp_variable = { migration_reception_front_intent_reveal_proven = constant:migration_reception_front_intent.one }
set_temp_variable = { migration_reception_front_intent_setup_proven = constant:migration_reception_front_intent.zero }
set_temp_variable = { migration_reception_front_intent_phase_request = constant:migration_reception_front_intent.requested }
migration_publish_reception_front_intent_from_contract = yes
```

## Presentation

`common/map_modes/chaosx_state_map_modes.txt` colours a front with a current visible row in the corridor-offer, preparing or corridor palette, but only when the state has no real migration role.
`common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` adds the intent role, the detail line and `GetMigrationReceptionFrontIntent`, with keys in `localisation/english/chaosx_map_modes_l_english.yml`.
Only the front's owner or controller sees the intent; other viewers keep the public map text.
No art, sprite or map button is added.

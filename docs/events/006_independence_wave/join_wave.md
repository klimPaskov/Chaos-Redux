# Event 006: Join the Independence Wave

The join-wave path is a voluntary conversion offer for a living country that has lost a significant share of its territory. It is dispatched only from scoped war-entry, state-control, peace-conference, capitulation, and release callbacks. If a qualified source reaches a callback while the shared release coordinator is busy, one country-local hidden retry (`chaosx.nr6.40`) is queued and rechecks the source before rescheduling or opening the offer. There is no daily, weekly, monthly, or on-game-start world scan.

## Eligibility and baseline

`independence_wave_join_observe_war_entry` records both belligerents before wartime state losses. `on_state_control_changed` re-evaluates the old controller and the current owner, but it does not manufacture an owned-state loss because the callback also fires for control-only changes. `independence_wave_join_update_peak_baseline` retains the largest observed owned-state count in `independence_wave_join_peak_owned_state_count`; only a country with no prior observation uses the larger of current territory and core-state footprint as a last-resort fallback. The offer threshold is a 50% or greater reduction and at least two states lost. The ratio is evaluated against the centralized percentage and reduction constants.

The source must be living, independent, and at peace. It must not already carry Event 006 or Event 005 origin, must not be an Event 006 registry-owned tag, and must not have a pending offer, operation, or cooldown. The peace requirement prevents conversion from erasing an active war, while the independence requirement prevents it from silently escaping an overlord. The callback scope supplies only the affected country participants.

## Package proof and reservation

The planner opens an ordinary Event 006 shared release plan with one expected country. It probes the attested package adapters through the existing `independence_wave_reserve_package_iw_*` wrappers. Those wrappers remain the sole package-content authority and publish their fixed anchor/compact/extended state rows, target identity, region, archetype, force, and setup metadata.

After each wrapper, the planner requires both an equal row count and an `every_owned_state` proof that every state still owned by the source is in the current reservation. A mismatch rolls back the candidate reservation, clears its selected metadata, reopens the same allocating contribution, and tries the next attested package. The two checks together reject both extra package states and missing source states. Exactly one package row may be selected.

The source's anchor is used as the temporary protected host state while the plan is collecting. The local Join-the-Wave plan identifier is captured before package probing, and global runtime markers are cleared only when the stored ledger ID, owner, and source still match. The zero-host exception requires the active Join-the-Wave plan identifier to equal the shared coordinator plan identifier and is consumed only during execution-time host preparation. Shared validators still require the frozen ownership, target, host, controller, core, and array ledgers. A stale report cannot abort, reset, or inherit a newer shared release plan; after a coordinator reset it may close only its own local receipt.

The deterministic Join probe currently follows the 32-package Event 006 content-attestation set, with IW-038 Ruthenia immediately after IW-031 Kosovo, IW-040 Kuban immediately after IW-038, IW-044 Tatarstan immediately after IW-040, and IW-045 Bashkiria immediately after IW-044. The exact first-success order is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-045, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184. Every admitted ID has one matching reservation wrapper, and the probe remains first-success rather than weighted or random.

## Player choice and execution

Event `chaosx.nr6.36` is a normal report event with a twenty-day response window. Expiry keeps the existing country, so an unattended report cannot convert the player or hold the shared release coordinator indefinitely. Accept fires hidden Event `chaosx.nr6.37`, which rechecks the pending plan, locks it, and invokes `independence_wave_execute_standalone_frozen_plan`. The ordinary release path instantiates the dormant tag, assigns the generic Event 006 focus framework and package mechanics, transfers the frozen states, performs package setup and final validation, records origin/history, and commits the plan. Only after the commit barrier succeeds does the target scope receive `change_tag_from = ROOT` for a human source.

Decline fires hidden Event `chaosx.nr6.38`. It clears Event 006 reservations and coordinator arrays only when the stored plan identifier still matches, records a history row, and applies a 90-day country cooldown. Event `chaosx.nr6.39` is a normal failure receipt for post-mutation or finalization failures. The shared compensating rollback remains authoritative when it is still safe. A finalization failure preserves its ledger and coordinator lock for diagnosis instead of pretending that the conversion committed or clearing an uncertain transaction.

## Files and identifiers

Gameplay is in `common/scripted_effects/006_independence_wave_join_effects.txt` and `common/scripted_triggers/006_independence_wave_join_triggers.txt`. Callback wiring is in `common/on_actions/006_independence_wave_join_on_actions.txt`. Reports and the scoped retry event (`chaosx.nr6.36` through `chaosx.nr6.40`) are in the shared `events/006_independence_wave_support_events.txt` registry, with player-facing localisation in `localisation/english/006_independence_wave_join_l_english.yml`. Retry timing is centralized at `constant:independence_wave_join.retry_days`. Shared zero-host exceptions are narrow edits in `common/scripted_effects/chaosx_liberation_release_effects.txt`, `common/scripted_triggers/chaosx_liberation_release_triggers.txt`, and `common/scripted_effects/006_independence_wave_package_planner_effects.txt`.

No formable GUI/category generator or IW031 portrait asset is touched. No broad diplomacy, war, faction, or relationship copy effect is introduced. Existing release and autonomy helpers remain the only mutation path.

## Future extensions

The attested package list can be promoted to a generated array once the package registry exposes a safe runtime array API. A future audit can also add a dedicated receipt detail payload for the exact package tag and state footprint without changing the transaction contract.

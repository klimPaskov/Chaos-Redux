# Event 016 remaining timer arithmetic audit — 2026-09-02

## Status and scope

This is a bounded, read-only source audit of remaining elapsed-time arithmetic in Event 016, D’Rhondan (DHR), and the shared Alien, Portal, and biological transaction paths that Event 016 directly invokes.

No gameplay files, localisation, configuration, save data, logs, or unrelated event families were changed.

The audit read `AGENTS.md`, the Chaos Redux decisions/missions, events, and subagents skills, the required offline Paradox wiki pages, the vanilla dynamic-variable documentation, and the Event 016 completion contract.

The authoritative date distinction is in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`: `global.date` is a date value intended for date comparison/localisation, while `global.num_days` is the current total elapsed days.

The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` likewise states that `date` is the current date identifier and that one game hour advances it by `0.00001`, whereas `num_days` is the elapsed-day axis.

Vanilla `events/LaR_espionage_operations.txt:185-193` provides a direct elapsed-day subtraction precedent using `global.num_days`.

## Severity-ranked findings

### P1 — DHR compact response expiry adds elapsed days to `global.date`

The live DHR receipt is written in `common/scripted_effects/016_dhrondan_country_effects.txt:288-291` by `dhrondan_refresh_compact_expiry`:

```text
set_variable = { dhrondan_diplomatic_offer_expiry_date = global.date }
add_to_variable = { dhrondan_diplomatic_offer_expiry_date = constant:dhrondan_decision_duration.compact_response_timeout }
add_to_variable = { dhrondan_diplomatic_offer_expiry_date = constant:dhrondan_decision_duration.compact_cleanup_grace }
```

The constants are the intended `13` response days and `1` cleanup-grace day in `common/script_constants/016_dhrondan_country_constants.txt:77-79`.

The same malformed field is read as a live expiry by `events/016_dhrondan_country_events.txt:33-45` for the `.49` response popup and by `events/016_dhrondan_country_events.txt:143-151` for the `.52` watchdog.

The recipient-side response guard in `common/scripted_triggers/016_dhrondan_country_triggers.txt:207-214` also compares the field to `global.date`.

The remaining-delay calculation in `common/scripted_effects/016_dhrondan_country_effects.txt:296-300` subtracts `global.date` and passes the result to the `.52` event, so it shares the same unit mismatch.

The write is reached from the compact decision completion at `common/decisions/016_dhrondan_country_decisions.txt:188-203`, and is refreshed again on first delivery at `events/016_dhrondan_country_events.txt:42-45`.

Expected scenario: completing the compact decision or delivering the compact starts the contract’s thirteen-day response plus one-day cleanup window, but `global.date + 14` is not fourteen elapsed days because the date axis advances by `0.00001` per hour.

The popup and receipt can therefore remain valid for roughly `14 / 0.00024` calendar days rather than fourteen days, and the watchdog can repeatedly reschedule instead of closing at the intended deadline.

Smallest repair: store an explicit elapsed-day receipt, for example `dhrondan_diplomatic_offer_expiry_num_days = global.num_days`, add the existing `compact_response_timeout` and `compact_cleanup_grace` constants to that field, compare it with `global.num_days` in `.49`, `.52`, and `dhrondan_compact_response_can_commit`, and subtract `global.num_days` when scheduling `.52`.

All receipt ownership, native event timing, 13/1 values, diplomacy, rewards, and cleanup flow can remain unchanged.

If a date is later wanted for presentation, it must be a separate snapshot; it must not be the functional due-day field.

### P1 — Shared Black Plague devastation receipt uses the date axis on the Event 016 biological path

Event 016’s weaponized Black Plague route reaches the shared biological transaction helper through `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:367-380` (`brilliant_scientist_dispatch_black_plague_release` → `black_plague_apply_exposure`).

The shared helper is `common/scripted_effects/020_black_plague_effects.txt:513-524` (`black_plague_set_next_devastation_date`):

```text
set_variable = { black_plague_next_devastation_date = global.date }
add_to_variable = { black_plague_next_devastation_date = constant:black_plague_timing.rat_devastation_interval_days }
add_to_variable = { black_plague_next_devastation_date = constant:black_plague_timing.collapsed_devastation_interval_days }
add_to_variable = { black_plague_next_devastation_date = constant:black_plague_timing.severe_devastation_interval_days }
```

The same receipt is checked by `common/scripted_effects/020_black_plague_effects.txt:1597-1672` (`black_plague_process_current_state_pulse`) with `global.date >= black_plague_next_devastation_date`, and it is rewritten after each devastation.

The writer is called by the severe, collapsed, and rat-controlled phase-entry branches of `black_plague_set_current_state_phase` at `common/scripted_effects/020_black_plague_effects.txt:528-635`.

Expected scenario: an eligible Event 016 biological target that is already in one of those active states, or a later phase transition reached by the shared exposure lifecycle, receives a devastation due-day that is many years beyond the configured interval instead of the configured number of days.

This is a shared-helper defect, not a claim that every Event 016 release immediately creates a devastation receipt; ordinary threatened/incubating weaponized exposure may transition to infected without entering one of the three devastation branches.

The Event 016 target guards do not exclude an existing Black Plague state, and the shared `black_plague_state_can_receive_exposure` guard at `common/scripted_triggers/020_black_plague_triggers.txt:66-78` permits eligible non-wasteland, populated, human-host or rat-controlled states.

Smallest repair: add `black_plague_next_devastation_num_days = global.num_days`, add the selected interval constant to that field, and compare the field with `global.num_days` in `black_plague_process_current_state_pulse`.

Keep a separate date snapshot only if presentation requires one.

This repair is limited to the devastation receipt; it does not alter exposure amounts, phase outcomes, pulse cadence, or rewards.

### P2 — Evolution `next_check_date` is malformed metadata, but is not the live timer

`common/scripted_effects/016_brilliant_scientist_evolution_effects.txt:652-767` schedules the actual callback using `brilliant_scientist_evolution_scheduled_delay_days` and `country_event = { id = chaosx.nr16.90 days = brilliant_scientist_evolution_scheduled_delay_days }`, but also writes:

```text
set_variable = { brilliant_scientist_evolution_next_check_date = global.date }
add_to_variable = { brilliant_scientist_evolution_next_check_date = brilliant_scientist_evolution_delay_days }
```

The callback is `events/016_brilliant_scientist_evolutions.txt:323-328`, and immediately dispatches the evolution pulse.

The full-repository identifier search found only the clear at `016_brilliant_scientist_evolution_effects.txt:578-582` and the write at `016_brilliant_scientist_evolution_effects.txt:763-765`; there is no current reader of `brilliant_scientist_evolution_next_check_date`.

Disposition: this is a confirmed unit-mismatch in a dead/latent receipt field, but it is not a current evolution scheduling defect because `.90` uses the separate elapsed-day delay field.

Smallest repair: either remove the two writes until a consumer exists, or rename/store the field as an explicit `_next_check_num_days` value based on `global.num_days` and update a future consumer at the same time.

Do not change the current `.90` event delay or evolution outcomes solely for this metadata issue.

## Confirmed no-findings in the other bounded paths

The exact Alien landing/API files have no `global.date` arithmetic: `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, and `common/scripted_triggers/016_alien_infantry_api_triggers.txt` use pending reservation day values and native timed-decision/mission timers.

The exact Portal raid files have no `global.date` arithmetic: `common/raids/016_brilliant_scientist_portal_raids.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, and `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt` use native raid preparation/cooldown fields and constants.

The Event 016 biological decision and API files have no `global.date` arithmetic: `common/decisions/016_brilliant_scientist_biological_operations.txt`, `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`, and `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt` route into shared lifecycle helpers without constructing date-based due days.

The directly inspected shared lifecycle helpers `common/scripted_effects/biological_lifecycle_effects.txt`, `biological_battlefield_effects.txt`, `biological_raid_effects.txt`, and `biological_operation_effects.txt` use `global.num_days` for due-day writes, comparisons, and remaining-delay subtraction.

The Event 016 world-threat duration path also uses `global.num_days`, matching `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:221`.

Other `global.date` writes found by the bounded `016*` scan are date-history snapshots, presentation dates, or identity/revision fallbacks, not elapsed timers; they should remain date-based.

## Explicit evidence boundaries

The analogous `black_plague_scheduler_due_day` write/check at `common/scripted_effects/020_black_plague_effects.txt:1712-1715` and `1814-1817` was not elevated as an Event 016 direct-path finding because the bounded call graph from Event 016’s `black_plague_apply_exposure` does not call `black_plague_schedule_next_pulse`; it belongs to a separate Black Plague scheduler audit.

Likewise, `black_plague_phase_entry_day = global.date` at `020_black_plague_effects.txt:560` and date-valued famine adapter IDs are not due-day arithmetic and were preserved.

No game was launched, no logs were requested, and no runtime or MCP event trace was used for this arithmetic-only review.

The findings are source-level evidence of unit mismatch; live engine ordering, save migration behavior, and actual popup/pulse cadence remain unverified.

The existing terminal-duration review owned by the lifecycle tranche was not duplicated.

## Audited source hashes

The following SHA-256 values identify the source inspected for this handoff:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/016_dhrondan_country_effects.txt` | `953B15AB38A0F71A2D4364D4CABEC6DCC78EACF1B16ADBCFFA9EB4AF5391FC56` |
| `common/scripted_triggers/016_dhrondan_country_triggers.txt` | `0A948FACF31A241B3108FED3E81EB36E916B0E0A737DC5A27E61BB283ECE8A3A` |
| `events/016_dhrondan_country_events.txt` | `6BFE2A945FA02DCDA157F8E3EB50C553B41530FFBA3D6BAE914312BF83115B00` |
| `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` | `B888AB495BB1846E5289405E4F96D1FD5BC1AF5B8F799A9000F3938ECEC324B4` |
| `events/016_brilliant_scientist_evolutions.txt` | `742E4855DC4B47074E39F3A310C2C1180C55471A39DA646FC2C8AB0B3A56C907` |
| `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt` | `DED6A1DBF25AA8ADB7C8ABA20905FB349ED4CAC4A7EB45EFAE4E12F4E511450D` |
| `common/scripted_effects/biological_lifecycle_effects.txt` | `1B5DFF3DC9E00319C90C73145BECBF6F92F57A7C85E72B7404234A205A9CC687` |
| `common/scripted_effects/020_black_plague_effects.txt` | `84A8A59DD37EC1F5722E3B177D97DD17C4045079C6A5FC1C607F532695C85A48` |

No gameplay source was modified and no commit was created.

# Event 013 and Event 020 bounded cleanup

Date: 2026-08-22

## Scope

This tranche applies the proof-backed Event 013 and Event 020 cleanup candidates from `subagent_handoffs/events_011_020_cleanup_audit_2026-08-22.md`.

No `interface/*.gui`, scripted-GUI layout, coordinate, click-region, sprite, or GUI asset file is changed.

## Event 013 shared selector repair

`GetSettingsEventName` and `GetLastEventName` in `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` now map Event 013 to `chaosx.event_name.13`.

The event was already registered, manually dispatchable, and named by the Event Log and debug selectors, so the missing settings branches were an isolated presentation bug rather than an unavailable event.

## Event 020 dead code removed

Thirteen definition-only `black_plague_country_has_*_target` wrappers were removed from `common/scripted_triggers/020_black_plague_response_triggers.txt`.

Their state-level `black_plague_response_can_*` triggers remain live and unchanged.

The superseded `black_plague_rat_set_initial_evolution_ready_day`, `black_plague_rat_load_evolution_log_context`, and `black_plague_rat_record_current_evolution` effects were removed from `common/scripted_effects/020_black_plague_rat_effects.txt`.

The five superseded `black_plague_rat_evolution_*_is_eligible` triggers were removed from `common/scripted_triggers/020_black_plague_rat_triggers.txt`.

The active `black_plague_evolution_record_stage` and `black_plague_evolution_runtime_pulse` subsystem remains the evolution owner, and the live `black_plague_rat_schedule_next_evolution_check` scheduler remains intact.

Exact and identifier-family searches across gameplay, scripted localisation, localisation, interface, and documentation found no live consumer or dynamically generated call for the deleted definitions.

Historical audit handoffs retain their original observations as provenance, with explicit cleanup-status notes marking the retired helper family as superseded.

## Player-facing prose cleanup

Two Event 016 foreign-operation strings now describe Doctor Kruger's transfer and confirmed death in world-state language instead of character-token implementation terminology.

The Event 018 withdrawal tooltip now describes the claim, offers, and commercial interest being abandoned instead of exposing stored targets and flags.

## Validation boundary

A post-change `hoi4.event_inspect` lint request for `chaosx.nr20.1` used a bounded event selector with helper expansion disabled.

The installed MCP route timed out awaiting `tools/call` after 180 seconds and returned no artifact, so no post-change event-graph validation is claimed.

The source checks prove only the bounded selector coverage, reference removal, preserved active evolution owners, and unchanged GUI-layout boundary described above.

The four Event 020 weighted literals identified by the audit were not changed because the required same-scenario probability comparison is not yet available.

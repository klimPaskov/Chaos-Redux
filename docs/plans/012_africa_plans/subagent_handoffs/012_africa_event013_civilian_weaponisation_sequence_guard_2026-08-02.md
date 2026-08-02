# Event 012 Event 013 civilian-witness sequence guard

Date: 2026-08-02.

Status: implemented source guard, live acceptance still open.

## Scope

The Event 012 hostile-nature callback needs to coexist with Event 013's delayed report system. Event 013 intentionally keeps caller type, caller ID, and caller country on an impacted state so later reports can notify the caller. Reusing that metadata as the only achievement witness would allow a later generic impact on the same state to inherit an old Event 012 caller.

## Runtime contract

When Event 013 schedules a call whose caller type is `constant:natural_disaster_caller.hostile_actor` and whose caller ID is `constant:africa_natural_disaster.caller_event_id`, it writes `natural_disaster_event012_weaponisation_pending` and stores the current `natural_disaster_sequence_id` in `natural_disaster_event012_weaponisation_sequence_id` on the scheduled state.

The Event 012 callback now requires the pending state flag and an exact sequence-ID match in addition to its existing caller metadata and positive `natural_disaster_last_deaths` check. A positive ordinary impact records the existing Event 012 civilian-weaponisation disqualifier and clears the one-sequence witness. A zero-death impact leaves the witness available for a later impact in the same Event 013 sequence. An expired scheduled state clears the witness. Non-Event-012 callers clear any stale witness when they schedule a new state.

Caller metadata remains intact for Event 013 reports and is not used as a substitute for the freshness marker. No new action store, country tag, cosmetic tag, model, or recurring loop is introduced.

## Files changed

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `docs/events/012_africa/natural_disaster_weapons.md`
- this handoff

## Validation

Targeted source inspection confirms one schedule-time Event 012 witness branch, one sequence-aware callback, and one expired-state cleanup branch. The existing ordinary impact callback remains immediately after `natural_disaster_apply_population_loss = yes`. The shared Event 013 file still contains unrelated pre-existing worktree edits that are outside this tranche and must remain unstaged.

Hearts of Iron IV was not launched and no live-save validation was performed, per repository instructions.

## Remaining blockers

The row 37 ecological-covenant achievement still needs live positive and negative scenario evidence, including the complete bargain, containment, five-year stability, and no-disqualifier route. The six-package W5 receipt contract, external continent identities, models, terminal presentation/audio, focus/UI runtime acceptance, and broader achievement and AI scenario audits remain open.

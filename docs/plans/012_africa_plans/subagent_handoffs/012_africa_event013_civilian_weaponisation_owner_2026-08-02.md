# Event 012 Event 013 civilian-weaponisation owner handoff

Date: 2026-08-02

Status: implemented source owner, live acceptance still open

## Scope

This tranche closes the exact source-side witness for the Event 012 achievement disqualifier `africa_achievement_disaster_weaponised_against_civilians`.

The implementation does not broaden the hostile nature action, add a country tag, add a model, or create a second action ledger.

## Runtime contract

Event 012 still prepares one exact selected enemy country and calls the public `call_natural_disaster = yes` contract with `hostile_actor` and caller ID `constant:africa_natural_disaster.caller_event_id`.

Event 013 persists the caller type, caller ID, and caller country on the impacted state.

After the ordinary impact path runs `natural_disaster_apply_population_loss`, it calls `natural_disaster_record_event012_civilian_weaponisation` once for that impact.

The helper requires all of the following:

- persisted caller type is `constant:natural_disaster_caller.hostile_actor`;
- persisted caller ID equals `constant:africa_natural_disaster.caller_event_id`;
- the persisted caller country exists;
- `natural_disaster_last_deaths` exists and is greater than zero; and
- the lifetime Event 012 disqualifier is not already set.

When the conditions pass, the helper scopes to `var:natural_disaster_caller_country` and calls the existing Event 012 owner `africa_achievement_record_disaster_weaponised_against_civilians`.

This is a positive civilian-deaths witness, not an accepted-call proxy. Warnings, target selection, building damage, rejected calls, generic Event 013 callers, and impacts with zero recorded deaths cannot set the disqualifier.

## Scope and repeat behavior

The callback is attached only to the ordinary Event 013 impact path. The existing Event 012 call remains single-sequence and random-family, and its strength, severity, target, cooldown, rejection, backfire, and cleanup behavior are unchanged.

The lifetime global flag makes the owner idempotent if a later chained impact carries the same persisted Event 012 caller metadata.

The row 37 achievement remains acceptance-gated. The source owner is now exact, but a live scenario still needs the ecological bargains, contained disasters, high-chaos route, deadline, and no-disqualifier proof.

## Files changed

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `docs/events/012_africa/natural_disaster_weapons.md`
- `docs/events/012_africa/overview.md`
- this handoff

The existing Event 012 achievement owner in `common/scripted_effects/012_africa_achievement_effects.txt` was reused without modification.

## Validation

The required offline Paradox wiki pages and vanilla documentation for effects, triggers, scopes, event targets, and script constants were read before this patch.

Targeted source inspection confirms one helper definition, one ordinary-impact callsite, and one Event 012 owner invocation.

The worktree already contained unrelated edits in the shared Event 013 file. Those hunks were preserved and are not part of this Event 012 tranche's staged commit.

Hearts of Iron IV was not launched and no live-save validation was performed, per repository instructions.

## Remaining blockers

The 44 achievement rows still need their live scenario evidence, and row 37 remains blocked until its complete ecological-covenant route is proven in-game.

The W5 initial six-package receipt, external continental package identities, original super-event masters and rights, the ten unit-model packages, focus and GUI runtime acceptance, and the 64 AI scenario audits remain open in the Event 012 overview.

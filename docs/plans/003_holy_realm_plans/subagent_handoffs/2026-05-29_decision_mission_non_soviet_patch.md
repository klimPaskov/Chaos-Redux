# Holy Realm Decision/Mission Non-Soviet Patch Handoff

Date: 2026-05-29

Scope: bounded decision/mission audit and patch for the non-Soviet Holy Realm items in `tmp/chaos_redux_multi_system_fix_spec.md`. Soviet collapse files and `common/national_focus/003_holy_realm.txt` were not edited.

## Changed Files

- `common/decisions/003_holy_realm_decisions.txt`
- `common/script_constants/003_holy_realm_constants.txt`
- `common/scripted_triggers/003_holy_realm_triggers.txt`
- `common/scripted_effects/003_holy_realm_effects.txt`

The worktree already contained unrelated Holy Realm edits in these files before this handoff. This patch only covers the identifiers listed below.

## Changed Identifiers

- Decisions:
	- `THR_white_scarf_relief_caravans`
	- `THR_mandala_open_granaries`
	- `THR_stand_between_armies`
	- `THR_send_global_final_warning`
- Scripted trigger:
	- `holy_realm_can_fund_mandala_peacekeeping`
- Scripted effects:
	- `holy_realm_cleanup_final_warning_target_memory`
	- `holy_realm_create_mandala_peacekeeping_template`
	- `holy_realm_spawn_mandala_peacekeeping_brigade`
	- cleanup call sites in `holy_realm_receive_peaceful_submission_from_event_target`, `holy_realm_on_country_capitulation`, `holy_realm_renounce_final_silence`, and `holy_realm_interrupt_final_silence`
- Constants:
	- `holy_realm_decision.refuge_relief_cooldown_days`
	- `holy_realm_decision.mandala_member_relief_cooldown_days`
	- `holy_realm_decision.mandala_peacekeeping_cooldown_days`
	- `holy_realm_decision.mandala_peacekeeping_manpower`
	- `holy_realm_decision.mandala_peacekeeping_infantry_equipment`
	- `holy_realm_decision.mandala_peacekeeping_support_equipment`
- Flags:
	- `holy_realm_refuge_relief_stage_cooldown`
	- `holy_realm_mandala_development_recent`
	- `holy_realm_mandala_peacekeeping_template_created`
	- `holy_realm_mandala_peacekeeping_recent`
	- existing `holy_realm_final_warning_received_from_realm` is now cleaned when invalid.

## Before And After

- Refuge relief:
	- Before: `THR_white_scarf_relief_caravans` could be repeatedly taken whenever war/high chaos conditions existed, and mostly paid out domestic manpower/stability.
	- After: it applies a 180-day stage cooldown and repairs one damaged or non-core controlled state with infrastructure and resistance reduction.

- Final warning:
	- Before: target memory blocked duplicate warnings, but stale flags could remain after a target became invalid, integrated, annexed, made a subject, joined the Mandala/faction, or after Final Silence was renounced/interrupted.
	- After: target selection excludes subject, faction, and Mandala-protectorate targets. A cleanup helper clears stale warning memory during warning send, peaceful submission, capitulation settlement, Final Silence renunciation, and Final Silence interruption.

- Mandala relief/development:
	- Before: `THR_mandala_open_granaries` mainly improved Holy Realm-owned states.
	- After: it also selects eligible faction-member states in Africa, South America, or Asia, prioritizing poor, rural, pastoral, war-torn, or low-infrastructure states, then adds infrastructure, possible industry, stability, and occupation recovery with a per-state cooldown.

- Peacekeeping:
	- Before: `THR_stand_between_armies` was a generic non-targeted political-power exchange.
	- After: it targets eligible minor democratic defenders in defensive wars, requires real manpower and equipment reserves, transfers a limited Mandala Peacekeeping Brigade, adds a target cooldown, and only permits faction-member targets after `holy_realm_focus_shelter_exiles`.

## Audit Notes

- Decision category lifecycle: the Mandala category still mixes early path relief, post-Mandala consolidation, and final doctrine pressure. The patched decisions now have cooldowns and target gates, but the broader category could still use clearer stage grouping if the parent wants a larger cleanup.
- Mission quality: no new timed mission was added. The audited mission-like surfaces are decision timers. `THR_white_scarf_relief_caravans` owner is Holy Realm, category is Mandala, region is controlled Realm states, requirement is Bodhisattva path plus war/high chaos, duration uses `refuge_days`, success is state recovery plus legitimacy/chaos effects, failure is no completion, duplicate risk is reduced by the new cooldown. `THR_stand_between_armies` owner is Holy Realm, category is Mandala, region is target country capital, requirement is Buddha path plus peacekeeping doctrine and target eligibility, duration uses `diplomacy_days`, success is limited unit/equipment support, failure is no support, duplicate risk is reduced by target cooldown and equipment cost.
- Cost and requirement clarity: peacekeeping now has real manpower/equipment costs in script, but player-facing localisation still only describes the concept and does not list the hidden equipment/manpower transfer.
- AI validity and route-lock: final warning and peacekeeping target triggers now exclude invalid/absorbed targets. Faction-member peacekeeping is route-locked behind `holy_realm_focus_shelter_exiles`; the focus file was intentionally not edited.
- Localisation and tooltip gaps: no localisation file was edited. The existing `THR_stand_between_armies_desc` and `THR_mandala_open_granaries_desc` are now under-descriptive for the new concrete target effects. A follow-up localisation pass should add a custom tooltip for the peacekeeping manpower/equipment transfer and target limits.
- Cleanup and exploit risk: relief spam, final-warning spam, repeated same-target peacekeeping, and repeated same-state Mandala development are now bounded. Broader two-sided arbitration, diplomatic letter chains, and fully dynamic regional aid offices remain outside this small patch.

## Remaining Gaps

- The full post-Mandala arbitration/development/peacekeeping suite is still shallow compared with the spec. This patch improves existing decisions but does not implement a new arbitration system or multi-stage development office.
- Poor/war-torn Africa/South America/Asia aid now has one real map recovery pass through `THR_mandala_open_granaries`, but there are no bespoke region-specific offices, missions, or escalation/failure outcomes.
- Final warning is once per target while valid, with cleanup for stale targets. It is not yet once per stage because no separate stage-scoped warning memory table exists.
- Mandala reach balance was not deeply retuned here. Existing reach/debug presentation should be reviewed by the parent if the broader system still feels opaque.
- Localisation was not updated because the existing localisation file was not touched in this bounded script patch.

## Validation

- `rg -n "<=|>=" common/decisions/003_holy_realm_decisions.txt common/script_constants/003_holy_realm_constants.txt common/scripted_triggers/003_holy_realm_triggers.txt common/scripted_effects/003_holy_realm_effects.txt` returned no matches.
- `git diff --check -- common/decisions/003_holy_realm_decisions.txt common/script_constants/003_holy_realm_constants.txt common/scripted_triggers/003_holy_realm_triggers.txt common/scripted_effects/003_holy_realm_effects.txt` returned clean.
- A read-only brace-balance script reported `brace_balance=0` and `early_closes=0` for all four touched script files.

## Skipped Validation

- No in-game validation was run by this subagent.
- No full repository parser was available in this task.
- No git commit was created because the parent worktree is already dirty with unrelated changes and this is a subagent handoff patch.

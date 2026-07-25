# Event 006 decision and mission repair re-audit, 2026-07-25

## Verdict

**FAIL.**

The repaired cost-localisation and country-value presentation surfaces pass static review.
DM-58 now creates finite, state-specific war goals instead of only setting an orphaned global flag.
Its shared lifecycle and preflight contract remain incomplete, so the repaired decision layer cannot receive a completion pass.

This is a read-only re-audit of the worktree after `f4b10808b` and the current uncommitted repair set.
No gameplay, localisation, GUI, or asset file was changed by this re-audit.

## Repaired surfaces that pass

### Custom-cost display contract, PASS

The current static scan finds 100 Event 006 `custom_cost_text` base keys and zero missing `<base>_blocked` or `<base>_tooltip` keys.
This includes every previously missing core, FORM-01/02/04, FORM-05, and FORM-48 cost surface.

The key examples that previously blocked DM-58 and the high-chaos family are present in `localisation/english/006_independence_wave_decisions_l_english.yml:62-77`.
The FORM-05 and FORM-48 paired variants are present in `localisation/english/006_independence_wave_form05_l_english.yml:88-113` and `localisation/english/006_independence_wave_pacific_l_english.yml:172-238`.

### Five live country values, PASS

`independence_wave_founding_category_desc` and `independence_wave_government_category_desc` in `localisation/english/006_independence_wave_decisions_l_english.yml:3-5` now show Legitimacy, Recognition, Government Capacity, Security, and Instability from their live variables.
The values are visible in categories already available to every active Event 006 country.

No decision-owned scripted GUI is present for this surface, so `hoi4.gui_inspect` and `hoi4.gui_render` do not apply.
The existing Event Log GUI references Event 006 rival-bloc detail data and is not the decision-value presentation surface.

### DM-58 target safety and finite war-goal construction, PASS

`independence_wave_execute_reclamation_front` in `common/scripted_effects/006_independence_wave_decision_effects.txt:667` now selects one valid state per eligible league member, requires a living non-member external owner, verifies that the member can declare war, and creates a state-specific `take_state_focus` war goal with the centralized 365-day `reclamation_front` duration.

`is_valid_independence_wave_reclamation_front_state` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:381` restricts targets to current claims or adjacent owned states, prevents duplicate targets in the same operation, excludes current league members and existing wars, and records the owner generation for duplicate resistance.

This follows the existing Event 006 `take_state_focus` generator pattern at `common/decisions/006_independence_wave_decisions.txt:3165-3171` and the vanilla `take_state_focus` definition.
The repair does not create an unconditional war or generic fallback state.

## Remaining issues, ordered by severity

### High: DM-58 has no preflight for the required multi-member compatible front

The accepted DM-58 contract requires several members with compatible claims and a synchronized operation.
`independence_wave_coordinate_reclamation_fronts` at `common/decisions/006_independence_wave_decisions.txt:3477` only checks the radical charter, minimum league membership, reserve, and material costs before the mission starts.
It performs target discovery only after it charges the strategic and major-security costs at lines 3506-3517.

The completion check succeeds when `global.independence_wave_reclamation_front_count` is greater than zero at lines 3520-3525.
One valid state for one member therefore passes a decision explicitly designed for several coordinated fronts.
Zero valid states produces a full paid failure and league crisis after the 180-day mission rather than preventing an impossible operation from starting.

Recommended bounded repair: add a non-mutating shared preflight trigger that counts valid reclamation-front candidates for current, compliant, non-client league members and requires the accepted multi-member minimum before DM-58 is available.
Use the same helper immediately before execution so target loss during the mission has an explicit partial-success or failure branch.
Keep material costs committed only when the operation can begin.

### High: shared reclamation state is cleared at the wrong lifecycle boundary and not cleared at league transitions

`independence_wave_cleanup_decision_layer` at `common/scripted_effects/006_independence_wave_decision_effects.txt:715` clears `independence_wave_reclamation_fronts_coordinated`, the shared arrays, and every current league member's ready flag.
`independence_wave_end_active_origin` calls that country-local cleanup before unregistering the departing member at `common/scripted_effects/006_independence_wave_effects.txt:2658-2672`.
The end of any one Event 006 member can therefore cancel the shared operation for every surviving member while the finite war goals it already created remain in force.

Conversely, `independence_wave_clear_league_phase_flags` at `common/scripted_effects/006_independence_wave_effects.txt:2288`, `independence_wave_leave_league`, and `independence_wave_dissolve_league_to_network` at line 2517 do not call a dedicated reclamation cleanup.
League dissolution clears member arrays without clearing the current reclamation flag, ready flags, target arrays, or count.
Those states can remain until their timed flags expire or another DM-58 completion clears them.

Recommended bounded repair: split the current global cleanup from `independence_wave_cleanup_decision_layer` into a dedicated shared operation resolver.
Call that resolver only when the operation resolves, fails, expires, the league dissolves or resets, or the operation can no longer retain its required number of members.
On an individual member exit, remove that member's ready receipt and revalidate the operation instead of unconditionally clearing every member's shared state.
The resolver should leave finite war goals to their explicit expiry unless the accepted design authorizes an early revocation effect.

### Medium: DM-58 is not gated by its named focus

The decision matrix classifies DM-58 as a focus-unlocked shared mission.
`independence_wave_focus_coordinate_reclamation_fronts` at `common/national_focus/006_independence_wave_focus.txt:1926` provides equipment, army experience, and revisionist pressure, but it sets no flag used by DM-58.
DM-58 instead relies on `can_independence_wave_use_high_chaos_actions`, which at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:469` checks only Regional Power, Radical Sovereignty, and the Open Sovereignty evolution.
The earlier `independence_wave_sponsor_further_ruptures` focus opens the category, so a qualified country can see and use DM-58 before completing `independence_wave_focus_coordinate_reclamation_fronts`.

Recommended bounded repair: either add the named completed-focus requirement to DM-58 activation or amend the accepted decision matrix if the intent is that the focus supplies preparation rather than unlock authority.
Do not leave the focus label and decision unlock contract contradictory.

### Medium: whole-event decision completion remains blocked by accepted fail-closed coverage

The current source-of-truth map still records FORM-06 through FORM-47 as fail closed and FORM-48 as unreachable through its required admitted member set.
Most accepted package and formable decision lanes remain intentionally unavailable.
This re-audit does not reopen that documented fail-closed safeguard, but it remains a completion blocker for an Event 006-wide PASS verdict.

## Lifecycle, AI, and exploit notes

DM-58 now has a real success path, a no-target failure path, finite 365-day war goals, state/target de-duplication, current owner validation, and a centralized material cost.
The owner decision remains `fire_only_once = yes`, but the global operation has no durable completion record.
After its timed global lock expires, a different eligible member can begin a later front and issue another set of member war goals.
This may be intended as sequential radical escalation, but it needs an explicit global operation-history or escalation policy before balance can be marked complete.

The repair uses a flat high DM-58 AI base after strict route and charter gates.
Until the multi-member preflight exists, AI can spend the full cost on a zero-target operation and trigger the failure branch.

The state-specific generation receipts intentionally prevent the same country and generation from selecting the same state again.
They are not cleared by the shared cleanup, which is acceptable only if they are retained as permanent duplicate-prevention receipts for that country generation.
Document that retention or add a narrow generation cleanup if the state record is intended to be temporary.

## Validation performed and limits

Static validation scanned all Event 006 decision `custom_cost_text` bases against all English localisation keys and found zero missing blocked or tooltip variants.
It inspected the live category descriptions, DM-58 decision, resolver, target trigger, duration constant, focus relationship, league end/dissolution paths, and vanilla/Event 006 state-war-goal precedents.

No Hearts of Iron IV session was launched.
No live multi-member radical-league scenario, league departure during an active front, dissolution during an active front, or AI target-selection scenario was executed.
Those scenarios remain necessary to establish runtime balance after the two high-severity lifecycle corrections.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_mission_repair_reaudit_2026_07_25.md`

## Simplifications, omissions, and blockers

No implementation was simplified or altered by this re-audit.
The remaining blockers are the DM-58 multi-member preflight, correctly scoped shared-operation cleanup, the named-focus unlock mismatch, and the previously documented fail-closed package/formable coverage.

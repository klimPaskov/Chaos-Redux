# Event 021 agent decisions, 2026-10-04

Disposition: accepted agent decisions under the user's full-authority takeover grant, recorded by the Claude implementing engineer for Event 021.
Acceptance basis: the user granted the takeover engineer authority to choose the recommended, spec-consistent option and record it here; the lead's round-1 assignment for Event 021 lists the same choices.
Each entry states the decision, its basis, and where it is implemented.

## D1. Adopt the stopped thread's uncommitted tranche

Decision: adopt, review, and commit the stopped Codex thread's uncommitted Event 021 work instead of discarding or rewriting it.
Basis: every called scripted effect and trigger, every `constant:` reference, and every localisation key resolved in the working tree; the ledger tranche had an independent re-review; the external-war fallback carries the user's explicit approval in `docs/specs/021_random_civil_war_specs/021_random_civil_war_external_war_successor_addendum.md`; the mission rework closes the 2026-09-26 audit findings and holds the routed `exists` fixes 1(a) and 1(b).

Focused review of the parent-effects diff before commit found no country-only trigger in state scope, no scope-prefixed temporary variable, no timed flag fed `days = constant:`, no date arithmetic outside `event021_days_to_date_offset`, and correct `on_state_control_changed` scoping (ROOT new controller, FROM old controller, FROM.FROM the state).
The new mission hook fails a hold for FROM, the country that lost control, which is the intended holder.

The commit split follows the code rather than the six suggested groups, because the parent-effects file interleaves the ledger, scenario cap, provenance and external-queue hooks hunk by hunk.
Splitting those hunks across commits would have produced intermediate trees calling undefined helpers.
Every commit below was built in an isolated index and checked for definition, constant and brace closure against its own tree.

| Commit | Content |
| --- | --- |
| `de3f7de71` | External-war successor prompt: new effects, triggers, event and localisation, its annex and on-action wiring, and the external-queue gates in target triggers. |
| `4c041ead2` | Dynamic front ledger, candidate traversal, crisis-scoped secondary review, successor roster rebuild, MTTH actor predicates, Maximum scenario front envelope, opening provenance, and the ledger contract test. |
| `00fe90801` | Mission continuity and sponsor gating, including the routed fixes 1(a) and 1(b), and the decision text rewording. |
| `628a50c32` | KUB Ivanis placeholder portrait and deletion of the fifteen orphaned achievement DDS files. |

The documentation commit that carries this file records the plans, specs, handoffs and probability snapshots of the same tranche, plus only the Event 021 hunk of `.gitattributes`.

## D2. Selectable missions resolve on selection, not at the timer

Finding: HOI4 runs `complete_effect` when a selectable mission is selected and then removes the mission, while `timeout_effect` runs only when the timer expires unselected.
Vanilla precedents `AST.txt` (Canberra cabinet mission) and `CHI_warlord_decisions.txt` (`TSR_pay_for_support_from_warlord_PP`) treat the two blocks as alternative terminal outcomes.
The adopted Event 021 missions used `complete_effect` to start a hold and `timeout_effect` to judge it, so a selected hold never resolved and an unselected one did nothing.
Decision: repair this in a dedicated commit after the tranche commits (see D3).

## D3. Mission repair shape

Decision: keep each selectable mission as the player's commitment, and on selection start a non-selectable hold mission through `activate_mission`.
The hold mission shows the native countdown, cannot complete early, judges the objective in its `timeout_effect`, and is cancelled when the hold breaks or the crisis ends.
The existing `on_state_control_changed` hook still fails a capital or rail hold the moment control of the bound state changes.
Basis: the mission spec (`021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md`, Mission families) requires timed holds with success and failure; vanilla `ETH_time_based_war_escalation_mission` uses a non-selectable mission with `available` never true to run a visible timer.
No cost, AI weight or reward changes.

## D4. Switched-off evolution stages are independent

Decision: follow the Event 004 precedent of independent stages.
`event021_parent_process_evolution_schedule` builds each stage's Events Log context and checks `is_current_evolution_enabled` before it samples a due date or fires the hidden callback.
A stage switched off in the settings is never sampled, fired, activated, or recorded, and a stale due date is cleared.
Evolution II needs Evolution I recorded or switched off; Evolution III needs both earlier stages recorded or switched off, which keeps enabled stages in order without letting a switched-off stage block a later one.
`event021_apply_evolution_ii` and `event021_apply_evolution_iii` no longer call the earlier core effects, and the parent wrappers accept a switched-off earlier stage, so a later stage never switches on a disabled stage's mechanics.
Re-enabling a stage returns it to normal scheduling through its own wrapper.
Basis: the lead's round-1 assignment, the audit finding EV21-DISABLED-01 in `subagent_handoffs/event021_date_units_probability_audit_2026-10-03.md`, and `common/scripted_effects/004_random_war_effects.txt`, which checks `is_current_evolution_enabled` per stage.
Contract: `common/scripted_effects/021_random_civil_war_parent_effects.md` (scheduler section).

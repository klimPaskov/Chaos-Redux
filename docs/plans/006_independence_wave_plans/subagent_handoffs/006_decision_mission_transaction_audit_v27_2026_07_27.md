# Event 006 Decision and Mission Transaction Audit v27

Date: 2026-07-27.

Scope: static source audit after `4ef5f9aa9`, with narrow repairs limited to Event 006 decisions, transaction triggers, and their player-facing localisation.

## Verdict

Two source-level transaction defects and one concrete custom-cost localisation gap were repaired.

The source now has complete base, tooltip, and blocked localisation coverage for all 104 `custom_cost_text` keys discovered in the Event 006 decision files.

This audit provides no runtime or live-session evidence.

The accepted transaction matrix still needs an explicit runtime row disposition and the scenario coverage recorded below.

No decision-owned scripted GUI was changed or inspected because no GUI source was in this task surface.

## Issues, sorted by severity

### P1 fixed — DM-03 could debit resources without a fresh affordability gate

`independence_wave_register_population` previously paid `independence_wave_decision_pay_administration_light` directly in `timeout_effect`.

The mission did not expose that charge through `custom_cost_trigger` and `custom_cost_text`, and a resource loss during its timer could therefore produce a debit below its intended affordability threshold.

The decision now requires `can_pay_independence_wave_administration_light_cost` at activation, exposes `independence_wave_cost_administration_light`, and rechecks the same trigger before payment at completion.

If the completion check fails, the existing registration-failure state and equivalent failure deltas apply instead of charging resources or applying the success flag.

The description now reads `independence_wave_decision_duration.founding` dynamically instead of claiming an obsolete fixed 180-day duration.

### P1 fixed — FORM-39 civil service validated one transport reserve twice

`can_pay_independence_wave_form39_civil_service_cost` invoked the strategic and diplomatic-standard affordability triggers, while its effect pays both helpers in sequence.

Each helper accepts either a convoy or train reserve, so one stockpile slightly above the standard threshold could satisfy both prechecks even though the first payment left too little for the second.

The validator now requires either one major convoy reserve, one major train reserve, or both standard reserves before the first payment.

That mirrors the effect's convoy-first, train-second fallback order without adding a magic number.

### P2 fixed — FORM-39 project costs lacked complete player-facing variants

The shipping, civil-service, and plebiscite `custom_cost_text` identifiers had only a short base sentence and lacked their `_tooltip` and `_blocked` entries.

All nine entries now disclose dynamic values from the shared constants, including the civil service's two independent convoy-or-train commitments and spare-factory requirement.

### P2 outstanding — transaction runtime matrix remains unexecuted

Static review cannot prove that the engine calls each timeout, cancel, flag, target, and helper path in the intended scope.

The Event 006 completion audit already records missing live matrices for league, rival bloc, contribution, rescue, expulsion, challenge, dissolution, faction war, exploit, DM-58, FORM-39, allocator, save/load, and focus-decision integration paths.

Do not treat this handoff as evidence for those scenarios.

### P3 outstanding — some pre-existing cost text remains prose-first

The repaired FORM-39 text uses dynamic values and explains the two-transport rule, but it follows the surrounding prose-first style rather than a full icon-first cost presentation.

This is a consistency improvement opportunity, not a reason to rewrite unrelated Event 006 localisation in this narrow audit.

## Decision category lifecycle notes

The central founding, government, recognition, security, host-relations, patron, network, league, border, formable, and high-chaos categories use active-origin or progression gates and hide when their associated Event 006 state is absent.

Central mission cleanup is centralised in `independence_wave_cleanup_decision_layer`, which cancels the central active mission flags and clears the central decision state.

`independence_wave_end_active_origin` dispatches package cleanup before the central decision-layer and rival-bloc cleanup, providing the expected ownership boundary for origin replacement and closure.

FORM-01, FORM-02, FORM-04, FORM-05, FORM-39, and FORM-48 categories use invitation or post-formation carrier gates rather than exposing the complete set to unrelated countries.

The static scan found eight automatic deadline or completion missions without `ai_will_do`, which is expected because they are timer consequences rather than AI-selected transactions: FORM-01, FORM-02, FORM-04, two FORM-05 missions, and three FORM-48 missions.

## Mission quality notes

| Owner and category | Region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| DM-01 / founding | Origin capital | Capital control, garrison, and founding timer | Provisional government or failure state | Central active-founding lock limits parallel founding missions. |
| DM-02 / founding | Origin-wide | Administrative standard affordability and founding timer | Revenue service or salary crisis | Central active-founding lock limits parallel founding missions. |
| DM-03 / founding | Origin capital | Revenue service, administration-light affordability, capital control, non-severe instability, and founding timer | Population registration after payment, or registration failure after cancellation or a failed completion affordability check | Central active-founding lock and `fire_only_once` limit duplication. |
| DM-58 / Council of Communities | Middle Volga | Recorded witness, ownership/controller and route checks, package rules, and configured deadline | Package-specific integration state or defined failure cleanup | Static source was previously reconciled, but valid, invalid, collision, witness-loss, controller-change, AI, and save/load runtime rows remain required. |
| FORM-39 shipping, civil service, plebiscites / federal compact | Melanesia | Bound live members, carrier proof, project exclusivity, concrete costs, and project-specific duration | Project-specific federal values and consent changes, or cancellation cleanup | The shared `has_independence_wave_form39_project_active` lock prevents concurrent projects. |
| FORM-39 dissolution / federal compact | Melanesia | Live carrier and post-formation state | Federation teardown and relation cleanup | Runtime proof remains needed for member loss, war, collision, host survival, and save/load. |

The accepted 80-row matrix has not been converted into a complete row-by-row runtime disposition by this audit.

## Cost and requirement clarity notes

Costs are centralised through Event 006 script constants and existing payment helpers instead of newly introduced fixed literals.

DM-03 now displays the same administration-light cost it must pass before it can start and before it succeeds.

FORM-39 civil-service validation now models both transport commitments as an aggregate requirement, so its availability condition corresponds to its two helper payments.

FORM-39 project custom-cost localisation has a base value, hover text, and blocked text for all three actions.

## AI validity and route-lock notes

The central decisions provide AI weighting, and the reviewed FORM-39 AI path requires an AI carrier, runtime commit proof, sufficient formable willingness, no severe instability, consent from both member governments, and no member war with the carrier.

The reviewed host, patron, league, and formable actions use live target or carrier predicates rather than unconditional country-target effects.

Static review does not substitute for hostile target, dead target, closed route, ownership transition, or focus-unlock runtime scenarios.

## Localisation and tooltip notes

`independence_wave_register_population_desc` now takes its displayed duration from `independence_wave_decision_duration.founding`.

The six missing FORM-39 hover and blocked entries were added, and the three existing base entries now name their dynamic resource commitments.

All Event 006 `custom_cost_text` identifiers discovered by the static scan resolve to a base key, `_tooltip`, and `_blocked` key in English localisation.

## Cleanup and exploit-risk notes

The DM-03 timeout now pays before it mutates the success state and has an explicit no-payment failure path.

The FORM-39 civil-service project no longer allows a single barely-sufficient transport stockpile to qualify for two sequential transport debits.

Existing central and FORM-39 exclusivity locks are present in source, but the exploit suite must still prove cancellation, cooldown, repeat, resource-farming, target-loss, and operation-collision behavior in the engine.

## Changed files and identifiers

- `common/decisions/006_independence_wave_decisions.txt`: `independence_wave_register_population` (DM-03).
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt`: `can_pay_independence_wave_form39_civil_service_cost`.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: `independence_wave_register_population_desc`.
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`: `independence_wave_form39_shipping_cost`, `independence_wave_form39_civil_service_cost`, `independence_wave_form39_plebiscite_cost`, and their `_tooltip` and `_blocked` variants.

## Meaningful validation

The static custom-cost scan found 104 Event 006 `custom_cost_text` identifiers and zero missing base, `_tooltip`, or `_blocked` English-localisation variants after the patch.

The FORM-39 validator was reviewed against all valid aggregate transport patterns implied by its sequential payments: a major convoy reserve, a major train reserve, or one standard reserve of each type.

The touched diff passed `git diff --check`.

## Skipped meaningful validation

No Hearts of Iron IV session was launched, and no runtime evidence is claimed.

The unresolved matrix needs game-engine scenarios for DM-03 late affordability loss, FORM-39 human and AI consent, member loss, cancellation, dissolution, host survival, war, collision, target death, focus integration, save/load, and exploit repetition.

No `hoi4.gui_inspect` or `hoi4.gui_render` artifact was produced because no decision-owned scripted GUI surface was in scope.

## Simplifications, omissions, and blockers

No fallback or substitute implementation was used.

The task remains incomplete only with respect to the explicitly missing runtime transaction matrix and related live consumer evidence.

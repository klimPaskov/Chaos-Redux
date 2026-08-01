# Event 020 incremental decision and mission audit handoff

## Scope and result

This incremental audit covered `020_black_plague_shared_response_decisions.txt`, `020_black_plague_response_decisions.txt`, `020_black_plague_rat_decisions.txt`, and `020_black_plague_weaponization_decisions.txt` with their immediate triggers, effects, constants, localisation, the shared disease category, the Event 020 decision/mission matrix, and the accepted two-tag correction.

The accepted correction permits exactly two Rat country tags: `RTA` for the Rat Nation and `RTX` for the Rat King.

No model, new category, event chain, formable, or decision-owned scripted GUI was created or changed.

The shared containment category remains the human Black Plague decision surface, while the Rat Nation and Rat King retain their country-scoped categories.

## Narrow patch applied

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/scripted_triggers/020_black_plague_shared_response_triggers.txt` | `black_plague_shared_can_start_port_inspections`, `black_plague_shared_can_start_relief_corridor`, `black_plague_shared_can_start_evacuation` | The three actions removed trains on completion without testing the stockpile first, and Relief Corridor tested its state flags inside `ROOT` country scope. | Each train-consuming action requires the required train stockpile, and Relief Corridor tests quarantine or cordon on the selected state. |
| `common/scripted_effects/020_black_plague_shared_response_effects.txt` | `black_plague_begin_shared_state_action` | Restrict Troop Routes and Seal All Transport displayed and required command power but never paid it. | Each action builds the correct existing response-payment command value and uses `black_plague_pay_response_cost` to debit it only after the action starts. |
| `common/decisions/020_black_plague_weaponization_decisions.txt` | `black_plague_weaponization_safety_first`, `black_plague_weaponization_military_acceleration`, `black_plague_weaponization_dual_use`, `black_plague_weaponization_defensive_conversion` | The unchosen approaches stayed visible but unavailable after a choice had completed. | The approach surface closes when its existing lifecycle trigger says the project cannot continue. |
| `common/decisions/020_black_plague_rat_decisions.txt` | removed `black_plague_rat_absorb_a_weaker_brood` | The action consumed Brood Mass and called a no-op helper while promising an adjacent-brood absorption that cannot exist under the two-tag correction. | The misleading and exploit-prone no-op action is unavailable. |
| `localisation/english/020_black_plague_response_l_english.yml` | `black_plague_shared_restrict_troop_routes_cost`, `black_plague_shared_restrict_troop_routes_blocked`, `black_plague_shared_restrict_troop_routes_tooltip`, `black_plague_shared_seal_all_transport_cost`, `black_plague_shared_seal_all_transport_blocked`, `black_plague_shared_seal_all_transport_tooltip` | Text described command power as a requirement rather than a paid resource. | Cost and tooltip text describe the real material, fuel, and command-power payment. |
| `localisation/english/020_black_plague_rat_decisions_l_english.yml` | removed `black_plague_rat_absorb_a_weaker_brood` keys | Text advertised a nonexistent annexation of a weaker brood. | Stale decision text is removed with its decision. |

The command-power patch deliberately reuses the established dynamic response-payment helper rather than duplicating a direct debit.

## Decision category lifecycle notes

The shared and local response actions use the existing selected-response-state contract for human players and the existing target path for AI countries.

Their `cancel_trigger` and cancellation helpers continue to clean a state action when its target becomes unusable, and the repaired train and command-power gates align availability with the exact completion payment.

Weaponization approach decisions remain mutually exclusive during their timed choice, and now disappear after a choice resolves instead of leaving a permanent row of disabled alternatives.

The rat categories are limited by active Rat Nation and Rat King predicates, with no decision reference to a third Rat tag.

The category lifecycle is still not compliant with the accepted coexistence rule, because the Evolution IV transfer retires the selected `RTA` source before the grace period begins.

## Mission quality notes

No audited Event 020 decision file contains `days_mission_timeout`, `mission_timeout`, or `activate_mission`.

The current timed content uses `days_remove` decisions, so there is no current mission owner, category, region, success, failure, or duplicate-risk record to assess.

The decision matrix's mission rows therefore remain a broader design and implementation gap rather than a local mission defect.

## Cost and requirement clarity notes

The patched shared actions now verify all equipment that they remove, and their two command-power requirements are genuine costs rather than a display-only gate.

The shared heavy-material eligibility gates are still higher than the standard population-scaled payment actually charged by `black_plague_begin_shared_state_action`.

This may be deliberate reserve-stock policy, but the decision text does not distinguish a gate from a payment and needs a parent design decision before any repricing.

Rat Nation and Rat King meter decisions rely on variable availability checks and generic descriptions rather than custom cost lines showing the exact Brood Mass, Dominion, Sentience, Cohesion, or Hunger change.

That is a player-clarity gap across the full Rat economy and should be addressed as one coherent localisation and UI pass rather than by isolated strings.

## AI validity and route-lock notes

The audited response decisions retain controlled-state and selected-state validation, so the local patches do not introduce an invalid AI target.

The weaponization decisions keep their existing hostile-state target checks, cancellation checks, and AI weights; no AI weight was altered in this pass.

No decision calls a Rat tag other than the two accepted roles.

The early retirement of the `RTA` source in `black_plague_rat_transfer_to_king` at `common/scripted_effects/020_black_plague_rat_effects.txt:817` route-locks the promised RTA/RTX coexistence grace period and must be resolved at the rat lifecycle level.

## Localisation, tooltip, and GUI notes

The patched response localisation keys match the two decision `custom_cost_text` references, and the removed rat decision has no remaining decision or English-localisation reference.

Both touched localisation files retain UTF-8 BOM encoding.

No Event 020 decision-owned scripted GUI exists in the inspected scope, so no `hoi4.gui_inspect`, `hoi4.gui_render`, or GUI artifact applies.

## Cleanup and exploit-risk notes

Removing `black_plague_rat_absorb_a_weaker_brood` closes a direct Brood Mass sink with no success effect.

`black_plague_rat_try_absorb_adjacent_brood` remains a no-op and is still called from `black_plague_rat_run_merger_pulses`, so obsolete merger constants, triggers, and scheduled cleanup should be removed or repurposed during the parent-owned two-tag lifecycle correction.

`black_plague_rat_king_send_the_royal_strike` remains a flat Dominion-to-Brood-Mass conversion with no selected front, enemy, map objective, success branch, failure branch, or cooldown beyond its repeatable timer.

`black_plague_rat_harden_the_immune_blood` remains a one-time permanent immunity and idea grant with no Rat-pool cost, so its intended opportunity cost needs design confirmation before a balance patch.

## Remaining issues sorted by severity

1. High — `black_plague_rat_transfer_to_king` retires `RTA` before creating `RTX` and setting the grace-period flag, contradicting the accepted requirement that both countries coexist throughout that grace period. This needs a rat lifecycle patch, not a decision-only change.
2. High — `black_plague_shared_can_strike_royal_node` exists at `common/scripted_triggers/020_black_plague_shared_response_triggers.txt:392`, but `black_plague_shared_strike_royal_node` has no matching decision in the shared response category despite the decision matrix requiring it. The missing counterplay needs parent-owned mechanic and localisation wiring.
3. Medium — `black_plague_rat_try_absorb_adjacent_brood` and `black_plague_rat_run_merger_pulses` remain obsolete no-op merger machinery after the two-tag correction. Clean the helper, caller, related constants, and any stale progression documentation together.
4. Medium — The rat decision surface still obscures meter payments and includes a targetless Royal Strike conversion. A coherent Rat economy and operation design pass is needed before changing individual balances.
5. Medium — The matrix's weaponization stockpile expansion or destruction paths and mission rows are not present in the audited decision files. Verify whether they are implemented through the special-project system; otherwise plan the missing player-facing routes.
6. Low — The state-action reserve-stock gates and their displayed population-scaled costs need a documented distinction if the higher availability threshold is intentional.

## Meaningful validation and evidence

Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.

Read the required Vanilla effects, triggers, script-constants documentation, and a vanilla decision lifecycle precedent before patching.

Compared the live decisions to `docs/specs/020_black_plague_specs/matrices/decision_mission_matrix.md` and `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`.

Confirmed that all changed script files have balanced braces, both changed localisation files retain BOMs, and `git diff --check` reported no task-file whitespace errors.

Searched the full Event 020 decision and localisation scope for `black_plague_rat_absorb_a_weaker_brood` and found no remaining call site or player text.

Searched the audited decision files for mission fields and confirmed there is no Event 020 mission implementation to validate.

No decision-owned GUI artifact applies because no decision-owned GUI surface exists in scope.

Probability simulation was not run because this patch did not alter an AI score or weighted pool, and no scenario inputs were declared for the fixed availability and payment paths.

No Hearts of Iron IV session was launched, in accordance with repository policy.

## Recommended next owner actions

The parent should assign the RTA/RTX coexistence and obsolete merger cleanup as one bounded rat lifecycle patch, preserving exactly one Rat Nation and one Rat King through the grace period.

The parent should decide whether to implement the matrix-required Royal Node strike, weaponization stockpile paths, and mission family as a connected response expansion rather than isolated decisions.

No simplification was made within this narrow patch; every broader omission remains explicitly listed above.

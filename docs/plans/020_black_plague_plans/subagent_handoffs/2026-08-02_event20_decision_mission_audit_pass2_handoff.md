# Event 020 decision and mission audit pass 2 handoff

> Superseded for the Crown/Seal API disposition by the parent 2026-08-02 native mission bridge tranche. The audit's state-target selector correction and other findings remain useful; its deferred shared-timed-action wording is historical.

## Scope and result

This audit covered the Event 020 shared disease-response category, state-targeted response, weaponization, Rat Nation, Rat King, and last-response mission surfaces against the accepted runtime contract.

No tag, model, category, event chain, formable, or decision-owned scripted GUI was added or changed.

The human response surface remains in the single existing `chaosx_disease_containment_category` category, while `black_plague_rat_brood_category` and `black_plague_rat_king_court_category` remain country-scoped Rat surfaces.

## Narrow patch applied

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/020_black_plague_shared_response_decisions.txt` | `black_plague_shared_strike_royal_node`, `black_plague_shared_strike_the_crown`, `black_plague_shared_seal_royal_burrows` | Each state-targeted decision used `state_target = any_state`. | Each uses the documented `state_target = any` value and retains its existing state-specific `target_trigger`. |
| `common/decisions/020_black_plague_weaponization_decisions.txt` | `black_plague_weaponization_deliver_payload` | The state-targeted payload decision used `state_target = any_state`. | It uses `state_target = any` and retains `black_plague_weaponization_delivery_state_is_valid`. |
| `common/decisions/020_black_plague_rat_decisions.txt` | `black_plague_rat_decode_route_memory`, `black_plague_rat_follow_refugee_road`, `black_plague_rat_king_send_the_royal_strike` | Each state-targeted Rat operation used `state_target = any_state`. | Each uses `state_target = any` and retains its existing hostile-target, route, and cooldown gates. |

The offline decision reference documents `any`, `yes`, `any_owned_state`, `any_controlled_state`, and continent keys for `state_target`; it does not document `any_state`.

## Issue list sorted by severity

1. Medium — Hold the Line and Secure the Refuge can be launched concurrently because neither launch trigger excludes the other active mission.
The source describes two human-only projects, while one contract sentence says a country can start “one of two.”
Each mission has its own full material cost, progress, success, timeout, and cooldown, so this may be intentional parallel counterplay rather than an exploit.
Parent design confirmation is required before adding a mutual-exclusion gate because the change would materially reduce the intended terminal-response capacity.

2. Resolved high — Seven Event 020 state-targeted decisions used unsupported `state_target = any_state` syntax.
The corrected `any` selector now lets their existing target triggers provide the complete legal-target filter instead of relying on an undocumented selector value.

3. Deferred by accepted contract — Crown Strike and Seal Royal Burrows remain shared timed state actions using `days_remove`, rather than native missions.
The current contract explicitly leaves any conversion to a parent decision, so this audit did not create a second action family.

## Decision category lifecycle notes

`chaosx_disease_containment_category` is the single human Black Plague response store, with the board-selection and direct-response predicates controlling visibility and state eligibility.

State actions delegate scaled payment, result resolution, cancellation, cooldowns, and board refresh to the existing shared response helpers.

The Rat Nation and Rat King categories remain gated by their active-country predicates, and the reviewed operations neither create a third Rat tag nor address one outside `RTA` or `RTX`.

## Mission quality notes

| Mission | Owner and category | Region and requirement | Duration and resolution | Duplicate risk |
| --- | --- | --- | --- | --- |
| `black_plague_shared_last_response_hold_mission` | Human country, `chaosx_disease_containment_category` | Evolution V terminal context, active RTX route, and at least one controlled established non-Rat state; launch pays equipment, trains, fuel, manpower, command power, factories, stability, and war support. | `constant:black_plague_last_response.mission_days` is 120 days; weekly country-pulse progress determines success; success reduces terminal preparation and improves containment; timeout raises terminal pressure, hunger, and exposure; invalidation clears active state and progress. | The mission cannot duplicate itself, but can coexist with Refuge. |
| `black_plague_shared_last_response_refuge_mission` | Human country, `chaosx_disease_containment_category` | Same terminal context plus a held established terminal capital, refuge node, or city; launch pays the larger complete material package. | 120 days; weekly progress depends on a held refuge target; success supplies stronger terminal and containment relief; timeout applies stronger pressure and exposure; invalidation clears active state and progress. | The mission cannot duplicate itself, but can coexist with Hold. |

`black_plague_clear_human_last_response_runtime` removes both active missions and clears their flags, cooldowns, and progress during terminal cleanup.

## Cost and requirement clarity notes

The reviewed shared response and last-response actions expose custom cost text and use named constants rather than local magic numbers.

The launch helpers make the actual deductions after the matching affordability trigger passes, including negative manpower, command power, stability, and war-support constants for the last-response missions.

Rat Nation and Rat King operations expose their dynamically evaluated Brood Mass, Dominion, Sentience, Cohesion, or Hunger costs in the reviewed English localisation, including target and cooldown requirements for Route Memory, Refugee Road, and Royal Strike.

## AI validity and route-lock notes

Last-response launches are human-only and have `ai_will_do = { base = 0 }`, matching their intended player-facing terminal-counterplay role.

Route Memory and Refugee Road require a real human enemy state adjacent to Rat-controlled ground, an appropriate logistics or ordinary-exposure condition, and a state cooldown.

Royal Strike requires a real human enemy controller at war with the Rat King, an exposure-eligible non-Rat state, and both country and selected-state cooldowns.

The shared Royal Node, Crown, and Seal actions retain separate Royal-node, RTX basin, military-route, defeat-aftermath, ownership, and response-capacity gates.

No invalid AI target, dead-country reference, disabled route, or impossible border was found in the reviewed decision paths.

## Localisation, tooltip, cleanup, and exploit-risk notes

All seven corrected decisions retain their existing localisation and custom-cost keys, so the selector correction adds no player-facing identifier.

The Royal Node, Crown, Seal, last-response, Rat-route, and Royal Strike text describes costs, target restrictions, duration, and outcome rather than exposing raw trigger script.

The Rat operations debit their meters only in their successful completion helpers and set target or country cooldowns.
Their cancellation paths clear a pending target cooldown only when the timed decision is invalidated before its completion.

The shared response helpers clean action flags, ownership, capacity burden, selected-target state, cooldown state, and map-mode refresh through the existing cancellation and terminal-runtime cleanup paths.

No decision-owned scripted GUI exists in this scope, so no `hoi4.gui_inspect`, `hoi4.gui_render`, GUI artifact, or fidelity finding applies.

## Meaningful validation

Read the required offline Paradox decision reference and the required vanilla decision/effects/triggers/script-constants documentation before patching, and compared the corrected selectors with vanilla decision precedents.

Searched the three changed Event 020 decision files after the patch and found no remaining `state_target = any_state` values.

Confirmed every corrected state-targeted decision still has a dedicated `target_trigger` and a matching availability or cancellation validation helper.

Reviewed the two native mission declarations and their launch, weekly-progress, success, timeout, cancellation, and terminal cleanup helpers.

No weighted-logic simulation was run because this patch changes no AI score or weighted pool.

No GUI inspection applies because the audited decisions do not own a scripted GUI surface.

No Hearts of Iron IV session was launched, in accordance with repository policy.

## Remaining issues and recommended next action

The only unresolved audited concern is the intentionality of concurrent Hold and Refuge missions.
If the parent confirms they must be mutually exclusive, add reciprocal active-mission exclusions to `black_plague_human_last_response_hold_can_start` and `black_plague_human_last_response_refuge_can_start` in `common/scripted_triggers/020_black_plague_terminal_response_triggers.txt` and update the launch descriptions.

No plan handoff was written because that choice requires parent design authority rather than a local decision or mission fix.

No simplification was made in this narrow patch.

# Event 020 Decision and Mission Audit

> Category-ownership findings in this historical audit are superseded by the accepted 2026-08-09 dedicated-response-category correction and its new decision audit. State containment remains shared; national cure and strategic management use `black_plague_response_category`.

Date: 2026-08-06.

Scope: Event 020's shared disease-containment category, Black Plague response, weaponization, Rat Nation, Rat King, terminal human missions, SCN-012 launch controls, and the shared disease-board and scenario-window hooks that expose those actions.

Result: No safe gameplay-source patch remains from this pass.
The only tentative source edit was reverted after review because Event 020 already follows the repository-required temporary-variable bridge for `days =` in timed flags.
The required probability audit is in progress through `chaosx_ai_probability_auditor` and is not replaced by this source review.

## Issue list

### Medium — Hold and Refuge can run concurrently

`black_plague_human_last_response_hold_can_start` only checks its own active, completed, and cooldown flags.
`black_plague_human_last_response_refuge_can_start` does the same and does not exclude an active Hold mission.
Both can therefore be launched by the same eligible human country, pay both packages, and progress in the same weekly Event 020 pulse.
The decision matrix describes choosing one of two terminal responses, while the current implementation and the nearby decision comment call them two projects.
This is a design-authority question rather than a safe local patch because a mutual exclusion would change terminal-counterplay balance.
If exclusivity is intended, add reciprocal active/completed checks in `common\scripted_triggers\020_black_plague_terminal_response_triggers.txt` and ensure the inactive mission is hidden or blocked with a dedicated tooltip.

### Medium — mandatory shared disease-board visual evidence is blocked

The only relevant decision board is the shared `disease_containment_board_window`, not an Event 020-owned scripted GUI.
`hoi4.gui_inspect` and `hoi4.gui_render` were attempted against the Event 020 selected-state scenario in workspace `mod_chaos_redux_ea3b2d67c2c0`.
Both calls failed with `SCAN_BYTE_LIMIT` and produced no artifact reference.
No `hoi4.gui_rewrite` was performed because there is no bounded Event 020 layout issue and the source review cannot substitute for the required MCP evidence.

### Low — scenario availability failure remains intentionally generic

`GetTriggerableScenarioLaunchStatus` supplies terminal, bootstrap, repeat-ready, launched, setup-failed, ready, and a generic Black Plague unavailable status.
The generic state can cover missing RTA or RTX package readiness, the commit provider, two eligible continents, a human port, candidate capacity, or the Rat slot.
This is clear enough to avoid leaking setup internals, but it is less actionable than a reason-specific tooltip.
Do not expand it without design approval because these technical preconditions are deliberately fail-closed.

## Decision category lifecycle notes

`chaosx_disease_containment_category` remains the single human response surface.
`black_plague_response_decisions_are_visible` gates its Black Plague entries, while state-targeted entries use `black_plague_response_state_is_selected_or_ai_target` and Event 020 phase/state helpers rather than creating a duplicate category.
Ordinary state actions use capacity reservation, an active-state marker, cancellation, short cooldown, result resolution, map-mode invalidation, and board refresh through `020_black_plague_shared_response_effects.txt`.
The human terminal entries activate only after the Evolution V route opens and use native missions for their visible duration and outcome.
`black_plague_rat_brood_category` owns RTA's growth and operation decisions, while `black_plague_rat_king_court_category` owns RTX policy, target selection, terminal preparation, and the Crown-the-Continent mission.
The Rat categories are visible only to their respective live carrier and are guarded by route, target, territory, meter, war, and cooldown triggers in the rat scripted-trigger surface.

## Mission quality notes

| Mission | Owner and category | Region and requirement | Duration and outcomes | Duplicate risk |
| --- | --- | --- | --- | --- |
| `black_plague_shared_emergency_countermeasure_drive` | Human host, shared disease category | Any severe active human crisis with support equipment, motorization, fuel, and project capacity | Native timed mission; completion gains countermeasures, timeout adds stability and exposure pressure, cancellation clears its active flag | One per country through active and failed flags |
| `black_plague_shared_strike_the_crown_mission` | Human host, shared disease category | Selected RTX-held Royal Basin that remains a valid human counterattack target | 180-day native mission; success, timeout, and cancellation each resolve or release the stored state action and marker | One target per owner through mission-active country and target-owner state variables |
| `black_plague_shared_seal_royal_burrows_mission` | Human host, shared disease category | Selected former Royal Node or Basin during the Rat King aftermath | 180-day native mission; timeout applies the anti-rat result and cancellation is outcome-free | One target per owner through mission-active country and target-owner state variables |
| `black_plague_shared_last_response_hold_mission` | Human host, shared disease category | Evolution V route, a surviving established human state, and its full equipment, manpower, fuel, command-power, stability, and war-support package | Native terminal-duration mission; weekly progress can succeed, loss of eligibility cancels, timeout strengthens terminal pressure | Parallel with Refuge is currently possible and needs design confirmation |
| `black_plague_shared_last_response_refuge_mission` | Human host, shared disease category | Hold requirements plus an established city, terminal capital target, or refuge node still under human control | Same native terminal duration; weekly progress can succeed, loss of target cancels, timeout has the larger refuge penalty | Parallel with Hold is currently possible and needs design confirmation |
| `black_plague_rat_king_crown_the_continent_mission` | RTX, Rat King court category | Valid target continent, earned route, three royal meters, and retained geographic threshold | Native target-continent duration; success earns the crown, cancellation/timeout removes the active route and applies the failure result | One RTX mission through its active country flag |

## Cost and requirement clarity notes

The response actions do not reduce to a flat political-power exchange.
State measures draw scaled project capacity plus the scripted resource packages, while the emergency mission, Crown Strike, Royal Seal, terminal Hold, terminal Refuge, weaponization actions, and Rat operations use the appropriate equipment, fuel, factories, manpower, command power, stability, war support, meter, territory, or map-target gates.
The cost checks are repeated in `available` and `custom_cost_trigger` where required, so a player cannot launch an action that the displayed cost cannot pay.
Every direct custom cost name, description, and effect tooltip key referenced by the four Event 020 decision files resolves in the Event 020 localisation surfaces checked for this pass.
The Rat timed-operation flags intentionally load the authoritative `constant:black_plague_rat_decision.*_duration_days` values into temporary variables before passing them to `days =`, which is the repository-prescribed compatibility bridge for timed flags.

## AI validity and route-lock notes

All human state-targeted response decisions use the selected-state-or-AI-target bridge, ownership/control checks, phase checks, live state target checks, and a human-host restriction.
The anti-Rat and Crown decisions additionally use RTX/RTA state and carrier tests, so dead or displaced carrier tags, closed aftermath, invalid targets, and terminal closure fail closed.
RTA and RTX retain separate category and country identity checks, preserving the two-tag contract.
AI does not select the terminal Hold or Refuge projects because both explicitly use `ai_will_do = { base = 0 }`.
Complex AI scores remain on Crown Strike, Royal Node Strike, Rat operations, Rat King court operations, and terminal execution; probability evidence must be taken from the separate auditor handoff before a balance-complete claim.

## Localisation and tooltip notes

The player-facing decision names, descriptions, custom costs, mission success/timeout/cancellation tooltips, and scenario launch-status keys are present in the Event 020 localisation reviewed for the referenced identifiers.
The SCN-012 button directly launches only when Black Plague is selected, while `triggerable_scenario_can_launch_selected` applies `black_plague_scenario_can_launch_from_triggerable_scenarios` to the actual button enablement.
The scenario path preserves the campaign event timer, handles a repeat launch as reconciliation only, clears temporary candidate arrays and reservation flags, and exposes failure through `black_plague_triggerable_scenario_setup_failed` rather than adding duplicate disease or Rat tags.

## Cleanup and exploit-risk notes

`black_plague_resolve_shared_crown_mission_success`, timeout, and cancel paths remove the native mission, clear the active country flag, target state flag, target owner variable, pending action, and refresh map/board state as applicable.
The corresponding Royal Seal paths perform the same ownership-scoped cleanup.
`black_plague_clear_country_response_runtime` and `black_plague_clear_shared_state_flags` remove residual shared response actions, missions, lane ownership, state markers, and mission-owner variables at episode teardown.
The human terminal clear helper removes both missions and both progress variables before terminal takeover.
The Rat operation actions have meter costs, target gates, per-operation flags, and route-lock triggers; no free-unit, equipment-farming, core-spam, or uncooldowned war-goal loop was found in this scope.
`black_plague_rat_absorb_a_weaker_brood` is not a no-op: its existing scripted effect reconciles real adjacent brood state markers under the two-tag carrier contract.

## Changed files and identifiers

No gameplay or localisation file remains changed by this audit.
`common\decisions\020_black_plague_rat_decisions.txt` was inspected and deliberately left with the existing temporary-variable timed-flag bridges for `black_plague_rat_citadel_stockpile`, `black_plague_rat_open_migration_lanes`, `black_plague_rat_tide_manifest`, `black_plague_rat_rail_breach_order`, `black_plague_rat_infect_the_occupation_line`, `black_plague_rat_king_crown_tithe`, `black_plague_rat_king_council_audit`, and `black_plague_rat_king_hierophant_broadcast`.
This handoff is the only file created by this subtask.

## Meaningful validation

Reviewed the Event 020 decision categories, 108 decision/mission entries, state-selection bridge, launch availability bridge, mission activation/completion/timeout/cancellation paths, the terminal cleanup helper, and the scenario repeat-cleanup path.
Confirmed no direct `state_target = any_state` remains in the four Event 020 decision files and no direct localisation reference is missing for their names, descriptions, custom costs, or effects.
Attempted mandatory GUI inspection and render evidence for the shared disease board, but both calls were blocked by `SCAN_BYTE_LIMIT` with no returned artifact.
No live game session was launched, in accordance with repository policy.
The probability auditor has begun Event 020 MCP work; its initial event-option inspect was partial because helper numeric inputs were undeclared to the evaluator, and the required decision-score evidence is still pending at the time of this handoff.

## Remaining issues and blockers

1. Parent design authority is needed to decide whether Hold and Refuge are intentionally concurrent or must be mutually exclusive.
2. Shared disease-board GUI MCP visual evidence is blocked by `SCAN_BYTE_LIMIT`; no source-only review should be treated as equivalent evidence.
3. Probability audit evidence for the decision and mission AI surfaces is pending from `chaosx_ai_probability_auditor` and must be reviewed before any AI-balance completion claim.
4. No dedicated Event 020 scripted GUI exists, so no Event UI worker or GUI layout patch is in scope.

No broader-mechanic plan was written because the unresolved concurrency question requires design direction before a plan can state a legitimate target behaviour.

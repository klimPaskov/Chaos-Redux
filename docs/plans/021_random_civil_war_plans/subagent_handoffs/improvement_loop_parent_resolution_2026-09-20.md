# Event 021 improvement-loop parent resolution

Date: 2026-09-20.
Event: 021 Random Civil War, root `chaosx.nr21.1`, manual scenario `SCN-018`.
Status: current source dispositions recorded for the prior improvement-loop findings. Test entry remains `Needs Testing`, and final acceptance remains open.

The fresh planner handle requested for this closure pass no longer existed and produced no new handoff. The parent therefore reviewed the existing 2026-09-13 improvement-loop findings against the current source and records the dispositions below. This note is a parent resolution, not a live test certificate or a completion claim.

## Findings resolved in current source

F01, frozen secondary receipt authority, is resolved for the current scenario transaction. `event021_parent_freeze_scenario_plan` stores the selected ordinary secondary state on the host country through `random_civil_war_scenario_frozen_secondary_state`, stores its route and objective beside that pointer, and marks the row only after the route is prepared. `event021_parent_apply_frozen_scenario_plan` restores those exact receipts before the opening transaction and does not search the changed map for a replacement. The receipt cleanup is bounded to the selected host and its reserved states.

F02, preparation and commitment separation, is resolved at the source-contract level. `random_civil_war_trigger_manual_scenario` freezes the selected target set, sends `chaosx.nr21.19` to each selected country for host-correct preparation, builds an explicit commit set from frozen receipts, and sends `chaosx.nr21.15` only to that set. A failed freeze is placed in the unavailable accounting path and cannot be rerolled after ownership mutation.

F03, same-tag scenario compatibility, is resolved at the source-contract level. The same-tag topology trigger is checked before type-specific route restrictions, `event021_parent_prepare_scenario_country` selects the same-tag archetype when its evidence is valid, and the freeze accepts that archetype for Political Fracture, Independence Cascade, Command Collapse, and Universal Fragmentation. The route keeps the original country tag and identity.

## Bounded front-plan disposition

F04 is implemented as a bounded four-row plan rather than an unbounded actor quota. The current plan can contain the host remnant, primary claimant, one ordinary secondary claimant, and one complete Event 006 secondary carrier. Each row carries an aligned front id, actor type, anchor and capital scope, objective, route, package receipt, state receipt, force envelope, relationship, and lifecycle status. `event021_parent_validate_front_plan` checks the aligned arrays and the centralized planned-front cap before any opening mutation.

This source contract supports the requested three-belligerent and stronger four-belligerent forms without manufacturing actors. It does not prove every FRT-02, FRT-03, or FRT-05 fixture in the engine, does not prove a five-belligerent result, and does not prove surviving-war settlement or successor behavior. Those remain explicit testing and MCP evidence obligations.

No new mechanic layer, world iterator, actor quota, fallback route, or Event 006 substitute was introduced by this resolution. The shared fixed-target helper remains an external dependency and is not invented here.

## Evidence boundary and next checks

The current narrow Event MCP lint is still partial because helper and lifecycle projection is deferred. User-owned testing must exercise ordinary and Event 006 secondary rows, the four scenario types on unsafe topology, pre-commit collisions, invalidated receipts, surviving fronts, settlement, recurrence, save and reload, and performance. The independent current-revision probability comparison and final completion audit remain open.

The supporting source references are `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`, `events/021_random_civil_war.txt`, and the prior handoff `improvement_loop_final_current_2026-09-13.md`.

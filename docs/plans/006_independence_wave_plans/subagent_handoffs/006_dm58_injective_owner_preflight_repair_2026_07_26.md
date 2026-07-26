# Event 006 DM-58 Injective Owner Preflight Repair

Date: 2026-07-26.

Status: Narrow decision and mission repair complete at source level.

This handoff does not claim Event 006 completion.

## Scope and issue list

| Severity | Status | Finding | Resolution |
| --- | --- | --- | --- |
| High | Resolved | DM-58's prior preflight counted three members that could independently find a legal state, but did not require different state owners. Three members aimed only at one external owner could therefore expose the mission and only fail during the paid resolver's pre-cost transaction. | The preflight is now an existential three-member, three-distinct-owner matcher. |
| Medium | Open | The paid resolver still randomly chooses each member's legal state after activation instead of preserving the proof's exact witness triple. A valid matching can exist while a greedy random choice later blocks a subsequent member. | The existing no-cost rollback remains authoritative. A later deterministic staging transaction would be required to make execution consume the exact preflight witness. |
| Low | Managed | The matcher is intentionally fixed to the accepted three-slot contract. | The source and lifecycle documentation tie it to `independence_wave_decision_gate.formation_member_minimum`, which is currently `3`. Expand the matcher if that contract changes. |

## Changed files and identifiers

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`: added `is_independence_wave_reclamation_front_member_eligible` and `is_independence_wave_reclamation_front_preflight_state`, and replaced `has_independence_wave_reclamation_front_preflight` with the injective matcher.
- `common/decisions/006_independence_wave_decisions.txt`: wrapped DM-58's activation preflight in `independence_wave_coordinate_reclamation_fronts_preflight_tt`.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: updated `independence_wave_coordinate_reclamation_fronts_desc` and added `independence_wave_coordinate_reclamation_fronts_preflight_tt`.
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md`: documented the injective requirement and explicit scope proof.

The edited decision is `independence_wave_coordinate_reclamation_fronts` (DM-58).

The reviewed but unchanged failure and cleanup authorities are `independence_wave_execute_reclamation_front`, `independence_wave_rollback_reclamation_front_staging`, and `independence_wave_cleanup_reclamation_front_operation`.

## Before and after behavior

Before this repair, `has_independence_wave_reclamation_front_preflight` tested only for a minimum count of individually eligible members.

It could return true when every eligible member's legal state belonged to the same external owner.

After this repair, the pure trigger searches the frozen `global.independence_wave_league_member_country_entries` ledger for member one, state one, owner one; member two, state two, owner two; and member three, state three, owner three.

Each member must be active, a league member, and not client-locked.

Each state must have a living external non-league owner, a living controller, claim-or-border connectivity to its selected member, no current war with that member, a declaration that is currently legal, no existing `take_state_focus` wargoal against that owner, and no existing DM-58 reservation.

Member two excludes member one, owner two excludes owner one, member three excludes both earlier members, and owner three excludes both earlier owners.

Owner uniqueness implies state uniqueness because a state has exactly one owner.

An unavoidable one-owner or two-owner collision therefore leaves DM-58 unavailable instead of creating a doomed mission.

The preflight is non-mutating and uses no flags, arrays, variables, claims, war goals, or costs.

Live state changes after the check still use the existing pre-cost rollback and crisis branch.

## PREV scope proof

The offline Scope reference states that `PREV` targets the containing scope and can be chained indefinitely.

The offline Scope reference and vanilla `documentation/triggers_documentation.md` describe `any_of_scopes` as scoping into each array element and returning when any element fulfills its trigger block.

The frozen member ledger contains country scopes because Event 006 adds `THIS` to `global.independence_wave_league_member_country_entries` and later iterates it as country scopes.

| Current scope | Ordered predecessor scopes | Required comparison | Source depth |
| --- | --- | --- | --- |
| Member two | owner one, state one, member one | member two differs from member one | `PREV.PREV.PREV` |
| Owner two | state two, member two, owner one | owner two differs from owner one | `PREV.PREV.PREV` |
| Member three | owner two, state two, member two | member three differs from member two | `PREV.PREV.PREV` |
| Member three | owner two, state two, member two, owner one, state one, member one | member three differs from member one | `PREV.PREV.PREV.PREV.PREV.PREV` |
| Owner three | state three, member three, owner two | owner three differs from owner two | `PREV.PREV.PREV` |
| Owner three | state three, member three, owner two, state two, member two, owner one | owner three differs from owner one | `PREV.PREV.PREV.PREV.PREV.PREV` |

The member comparisons execute while the current scope is the member-ledger country.

The owner comparisons execute while the current scope is the selected state owner's country.

Consequently all six `tag` inequalities compare country tags of the intended type, never an owner tag with a member tag.

## Decision category lifecycle and mission quality

| Field | Evidence |
| --- | --- |
| Owner | The activating compliant radical-league country owns the decision, while all three selected countries are drawn from the frozen league-member ledger. |
| Category and region | High-chaos league action spanning each selected member's claimed or border-connected external state. |
| Activation and requirements | High-chaos access, charter compliance, radical route, focus authorization, no crisis or completed or failed operation, minimum member ledger, and injective preflight. |
| Resource availability | Existing strategic, major-security, and shared-reserve checks remain in `available` and `custom_cost_trigger`. |
| Duration | Existing mission timeout is `independence_wave_decision_duration.long` at 180 days, while resulting war goals and member-ready flags use `independence_wave_decision_duration.reclamation_front` at 365 days. |
| Success | The existing resolver must stage the configured minimum of unique legal member, state, and owner pairs before material costs, coordination timing, and league deltas apply. |
| Failure | A collision that is unavoidable at activation is unavailable. A target that disappears after activation or a greedy resolver shortfall invokes provenance-aware rollback before material costs and then opens the existing crisis failure branch. Timeout also enters crisis without generic targets. |
| Duplicate risk | The injective owner gate prevents repeated owner fronts in the proof, and the existing owner/state arrays plus state markers prevent repeated staged targets during execution. |

## Cost, localisation, AI, and cleanup notes

DM-58 remains a concrete strategic operation, not a political-power store.

Its existing cost layer checks and later spends stability, war support, command power, a convoy-or-train commitment, manpower, army experience, infantry equipment, and support equipment, while requiring spare civilian factories and the configured shared reserve.

The custom cost text already explains that concrete package, and the new description and preflight tooltip explain the distinct-owner operational requirement instead of exposing raw trigger logic.

`ai_will_do` remains the existing high weighting, but the AI must satisfy the same activation proof and resource availability checks as a player.

No AI target is introduced by this patch, and no dead target, client-locked member, league member owner, already-warred owner, or existing `take_state_focus` target may satisfy a slot.

No scripted-GUI surface is owned by this decision, so no GUI artifact was inspected or changed.

No new flags, targets, arrays, variables, or mission cleanup paths were introduced.

Existing rollback removes only transaction-created claims and finite war goals from its aligned member, state, and owner arrays, while the shared operation cleanup clears reservations and receipts.

There is no free-unit, equipment-farming, core-spam, war-goal-spam, or cooldown loop added by this patch.

## Validation evidence

- Confirmed `independence_wave_decision_gate.formation_member_minimum = 3` in `common/script_constants/006_independence_wave_decision_constants.txt`.
- Ran a static matching model covering a three-distinct-owner success, one shared-owner collision, a backtracking-required valid matching, and an only-two-owner failure. The results were `True`, `False`, `True`, and `False` respectively.
- Ran a static source-contract check for the three ledger slots, three shared state predicates, member exclusions, owner exclusions, the activation tooltip, localisation, lifecycle documentation, trigger braces, and the UTF-8 BOM localisation header. Result: `PASS`.
- Ran a dedicated PREV-depth structural proof against the actual source. Expected and observed depths were member two to member one `3`, owner two to owner one `3`, member three to member two `3`, member three to member one `6`, owner three to owner two `3`, and owner three to owner one `6`. Result: `PASS`.
- Ran `python .tools\\audit_event6_allocator.py`; the Event 006 allocator audit passed without a regression in its registered package totals.
- Ran `git diff --check` over the four touched source and documentation files; no whitespace errors were reported.

## Skipped meaningful validation

No live HOI4 run, save/load scenario, or in-game AI observation was performed because live consumer validation belongs to the user and agents must not launch the game.

`hoi4.probability_inspect` was attempted for DM-58 AI evidence, but the MCP transport closed and produced no artifact.

No GUI inspection or rendering was needed because the patch changes no decision-owned scripted GUI surface.

## Remaining checks and recommendation

Run the following live scenarios before any Event 006 completion claim: three members with three distinct owners must stage successfully; three candidates sharing one owner must leave DM-58 unavailable; a target invalidated after activation must invoke no-cost provenance-aware rollback; timeout must not create targets; a low-resource AI must not select the mission; and save/load must preserve an active successful front's reservations and finite war goals.

If deterministic execution is required in addition to deterministic feasibility, hand off a separate scoped design to bind the resolver to the preflight's exact matching witnesses before the member loop runs.

No fallback or simplification was introduced in this repair, but the existing random resolver means the source proof is a feasibility gate rather than a commitment of the selected triple.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_dm58_injective_owner_preflight_repair_2026_07_26.md`.

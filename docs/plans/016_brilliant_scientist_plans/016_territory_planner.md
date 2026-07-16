# Event 016 Kruger State Territory Planner

## Purpose

The territory planner freezes a verified set of former-host states before the parent-owned Kruger State formation effect changes ownership, control, cores, capitals, countries, or characters. It implements three independent territorial contracts:

- peaceful charter;
- one-state or two-state enclave;
- prepared laboratory rebellion.

Institutional takeover is not evaluated here. Failure to assemble territory never unlocks, selects, or rerolls takeover.

The planner is invoked only by a targeted Event 016 resolution. It adds no daily, weekly, monthly, or other recurring whole-world on-action.

## Sources and precedents

The implementation follows the offline Paradox wiki pages for data structures, scopes, triggers, effects, modifiers, localisation, on-actions, events, decisions, ideas, AI, country creation, and state modding. Persistent target and state-transfer behavior was cross-checked against the current official documentation in the vanilla `documentation/` folder.

The principal live precedents are:

- vanilla `events/BBA_Ethiopia.txt`, where an effect iterates owned core states and transfers each selected state to a newly created country scope;
- vanilla `common/national_focus/congo.txt`, where an authored civil-war package freezes territory and creates forces around that package;
- Chaos Redux Event 006's package planner and execution effects, which clear verification before mutation, reserve only host-safe states, freeze a plan, revalidate it, and transfer the exact frozen membership.

Event 016 uses the fixed `KRG` package owned by the parent implementation. This planner does not create a dynamic country and does not transfer a state.

## Candidate authority

Territory is derived only from current Event 016 state facts. A facility state is recognized by the existing facility variable or one of these existing state flags:

- `brilliant_scientist_primary_facility`;
- `brilliant_scientist_secondary_facility`;
- `brilliant_scientist_joint_laboratory_site`;
- `brilliant_scientist_quantum_transit_terminal`;
- `brilliant_scientist_cloning_growth_site`;
- `brilliant_scientist_robotics_assembly_complex`;
- `brilliant_scientist_paleogenetic_reserve`;
- `brilliant_scientist_paleogenetic_hatchery`;
- `brilliant_scientist_xenobiological_vat_complex`;
- `brilliant_scientist_xenobiological_control_center`;
- `brilliant_scientist_alien_interface_chamber`;
- `brilliant_scientist_temporal_anchor`.

A state with `brilliant_scientist_facility_destroyed` is never eligible.

Every selected state must be owned and controlled by the host at planning and at immediate revalidation. This excludes foreign joint laboratories and third-party occupied states without removing their facility records. If the host later lawfully owns and controls such a state, a newly prepared plan may consider it.

The current host capital is never selected. It remains the former host's viable capital; the only Event 016 route allowed to use the existing host capital is the separately proven institutional takeover route.

## Route packages

### Enclave

The enclave target is bounded at two states and accepts one valid state. Its first state must be a real facility that can serve as a capital and has a land supply connection, hub, railway, or serviced port. A second connected facility or strategic support state is selected when available. The standard Event 016 territory score makes a connected core facility capital exactly sufficient for the one-state contract; a non-core or unsupplied fragment is rejected.

### Charter

The charter target begins with the count of eligible facility states plus one support state, bounded from two through six. Every charter state must be a former-host core. At least one selected factory and one logistics-connected state are required. The former host must retain its capital, the shared retained-state and retained-factory floors, and at least one core state.

### Rebellion

The rebellion target begins with the eligible facility count plus a support state. Deployment history, Weaponization history, and a verified multi-site network can each increase the bounded target. The final target remains between three and eight states. At least three states, one actual facility, one selected factory, and one logistics-connected state are required.

The target is an upper bound, not permission to fill with arbitrary land. A plan can stop below its target when all remaining states fail the facility, adjacency, strategic-support, or host-survival rules. It is valid only if the route minimum still passes.

## Selection order

The planner uses deterministic state iteration and explicit priority passes; it does not choose a random state.

1. Select the current valid primary facility as capital when it is not the host capital and the host can spare it.
2. Recover a marked primary if its target was stale but its live state marker remains valid.
3. Try the current or marked secondary facility.
4. Try the current or marked joint laboratory, but only if the host currently owns and controls it.
5. Try Event 016 transport facilities, then supplied or industrial facility states, then any remaining viable facility.
6. Grow connected secondary, joint, transport, and other facility states out from the selected capital. Repeated bounded passes make the result independent of state-ID iteration order.
7. If `brilliant_scientist_multi_site_network_verified` exists, consider separated facility states only when the state itself has a quantum/temporal terminal, serviced air base, or serviced port.
8. Add connected core support states with an actual hub, railway, port, civilian factory, military factory, or dockyard. Bounded repeated passes can create a short corridor, but adjacency alone is never sufficient.

Each candidate is tested before it is marked. The planner projects the host's remaining owned states, core states, and factories after that candidate and skips it if any retained floor would be crossed.

## Frozen plan representation

Selected states receive exactly one role in addition to the shared membership flag:

- `brilliant_scientist_formation_territory_selected`;
- `brilliant_scientist_formation_territory_capital`;
- `brilliant_scientist_formation_territory_connected_facility`;
- `brilliant_scientist_formation_territory_multi_site_facility`;
- `brilliant_scientist_formation_territory_support`.

The persistent targets are:

- `brilliant_scientist_formation_territory_host`;
- `brilliant_scientist_formation_capital_state`.

Route identity is frozen with one of:

- `brilliant_scientist_formation_territory_route_charter`;
- `brilliant_scientist_formation_territory_route_enclave`;
- `brilliant_scientist_formation_territory_route_rebellion`.

The planner publishes the existing formation counters consumed by Event 016, including `brilliant_scientist_formation_selected_state_count`, `brilliant_scientist_formation_facility_state_count`, `brilliant_scientist_formation_territory_score`, `brilliant_scientist_formation_host_remaining_state_count`, and `brilliant_scientist_formation_host_remaining_factory_count`. It also publishes selected factories, selected cores, logistics states, support states, multi-site states, remaining host cores, and frozen snapshot values.

## Verification transaction

`brilliant_scientist_prepare_formation_territory_plan = yes` is the only preparation entry point.

It performs this sequence:

1. clear the old verification flag;
2. clear every stale planner state mark and named planner target;
3. prove exactly one route request;
4. bind the current host target;
5. require `brilliant_scientist_project_mode_history_is_coherent` so no contradictory xenobiological host-control modes can enter formation;
6. calculate eligible facilities and the route target;
7. select a viable capital, connected facilities, verified multi-site facilities, and strategic support;
8. rebuild every counter from the selected state marks;
9. validate state roles, route bounds, capital, logistics, territory score, and host survival;
10. snapshot the accepted plan;
11. set `brilliant_scientist_formation_territory_prepared` and `brilliant_scientist_formation_territory_revalidated`;
12. set `brilliant_scientist_formation_territory_verified` last.

The stable route predicates are:

- `brilliant_scientist_verified_charter_territory_plan_is_valid`;
- `brilliant_scientist_verified_enclave_territory_plan_is_valid`;
- `brilliant_scientist_verified_rebellion_territory_plan_is_valid`;
- `brilliant_scientist_has_verified_formation_territory_plan`;
- `brilliant_scientist_formation_territory_plan_can_be_committed`.

## Required parent formation sequence

The parent-owned `brilliant_scientist_form_kruger_state_from_verified_plan` must run in the former-host country scope and use this order:

```hoi4
brilliant_scientist_revalidate_formation_territory_plan = yes
if = {
	limit = {
		brilliant_scientist_formation_territory_plan_can_be_committed = yes
	}
	# First mutation begins only here.
	# Instantiate/release fixed tag KRG, transfer exactly the marked states,
	# set the frozen capital, reconcile cores/control, then initialize KRG.
}
else = {
	# Fire the explicit invalid-plan outcome owned by the parent route.
}
```

`brilliant_scientist_revalidate_formation_territory_plan` never rebuilds or substitutes territory. It clears verification first, rescans the marked states, compares the frozen snapshot, and restores verification only if the same host, route, capital, state roles, ownership, control, facility facts, score, and survival floors still pass.

After a successful transfer, or after any explicit cancellation, the parent must call `brilliant_scientist_clear_formation_territory_plan = yes` after it has consumed the capital and host targets.

## Invalid-plan contract

An invalid preparation or revalidation clears all transfer-capable state marks and both persistent planner targets. It retains only route identity, attempted metrics, the flag `brilliant_scientist_formation_territory_invalid`, and an enum value in `brilliant_scientist_formation_territory_invalid_reason`.

`brilliant_scientist_formation_territory_plan_is_invalid` is the stable fail-closed predicate. Invalid reasons distinguish ambiguous route, invalid host, incoherent project-mode history, no eligible facility, no viable capital, host-survival failure, route-contract failure, missing plan, stale host, stale route, stale state, stale capital, and changed snapshot.

The planner never changes the requested route. The parent must not turn a failed rebellion into an enclave, a failed enclave into arbitrary land, or any territory failure into institutional takeover unless a separately authored player-facing resolution explicitly evaluates and selects that different outcome before preparing a new plan.

## Integration notes

Two existing Event 016 integration surfaces need parent edits outside this planner's ownership:

1. `brilliant_scientist_can_form_enclave` currently inherits the old two-state global minimum. It must consume `brilliant_scientist_verified_enclave_territory_plan_is_valid` so a verified one-state enclave can form without falsifying its state count.
2. `brilliant_scientist_resolve_full_kruger_rebellion` currently calls the partial-uprising resolver after an invalid rebellion plan. That is route substitution. It must instead expose an explicit invalid-rebellion resolution or return to an authored choice that separately selects the enclave route before a new plan is prepared.

The existing charter and rebellion numerical minimums match this planner, but their formation gates should still include the corresponding verified route trigger so stale or mismatched route flags cannot pass on counters alone.

## Validation scenarios

The parent integration should exercise these scenario contracts:

| Scenario | Expected planner result |
| --- | --- |
| One valid connected core primary facility; host retains required states, cores, and factories | Valid one-state enclave |
| Same primary plus adjacent rail/factory state | Valid two-state enclave |
| Charter with one facility and one strategic adjacent core state | Valid two-state charter |
| Charter would remove host capital or reduce the host below a retained floor | Explicit invalid plan; no marks or targets remain |
| Rebellion with one facility and two connected strategic support states | Valid three-state rebellion |
| Several connected marked facilities | Larger deterministic charter/rebellion package up to its route cap |
| Foreign joint laboratory still owned or controlled by a third party | Excluded, never transferred |
| Disconnected facility without verified multi-site network or local transport proof | Excluded |
| State ownership/control or facility marker changes after preparation | Immediate revalidation invalidates and clears the plan |
| Requested route flags are ambiguous | Explicit ambiguous-route invalid plan |
| More than one xenobiological host-control mode is active | Explicit incoherent-project-mode invalid plan before state selection |

## Icons and UI assets

No new player-facing object, decision icon, state icon, sprite, or GUI surface is created by the territory planner. No `.gfx` registration or visual asset is required in this tranche. If the parent later exposes route previews or invalid reasons in UI, that UI package must define and document its own stable sprite names before art production.

## Future plans and suggestions

- Add a player-visible territory preview that reads the frozen state marks without being allowed to mutate them.
- Add route-specific invalid-plan localisation mapped from the reason enum.
- Add a dedicated Event 016 power-site marker if project content creates real grid or reactor states; the planner should then prioritize that explicit marker rather than infer power from generic infrastructure.
- Add a post-formation audit helper in the parent country package that proves KRG owns every frozen state, owns its frozen capital, and received no unmarked state before planner cleanup.
- If future routes need a larger corridor, increase the bounded constants only after map-shape and former-host balance review; do not replace the strategic-support predicate with generic adjacency.

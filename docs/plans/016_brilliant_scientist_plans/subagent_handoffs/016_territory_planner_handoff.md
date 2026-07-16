# Event 016 Territory Planner Handoff

## Scope completed

Implemented the isolated Event 016 Kruger State territory-selection planner. The planner owns preparation, deterministic state membership, route-specific verification, stable invalid-plan state, immediate non-rebuilding revalidation, and cleanup. It does not create `KRG`, transfer states, change cores/control, edit containment resolution, edit the country package, or alter localisation/assets.

## Files added

- `common/script_constants/016_brilliant_scientist_territory_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`
- `docs/plans/016_brilliant_scientist_plans/016_territory_planner.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_territory_planner_handoff.md`

No pre-existing gameplay, localisation, country, focus, asset, spreadsheet, or shared documentation file was edited.

## Public entry points

Preparation:

- `brilliant_scientist_prepare_formation_territory_plan = yes`

Required immediate pre-mutation recheck:

- `brilliant_scientist_revalidate_formation_territory_plan = yes`

Post-commit or cancellation cleanup:

- `brilliant_scientist_clear_formation_territory_plan = yes`

Stable verified-plan predicates:

- `brilliant_scientist_verified_charter_territory_plan_is_valid`
- `brilliant_scientist_verified_enclave_territory_plan_is_valid`
- `brilliant_scientist_verified_rebellion_territory_plan_is_valid`
- `brilliant_scientist_has_verified_formation_territory_plan`
- `brilliant_scientist_formation_territory_plan_can_be_committed`

Stable invalid-plan predicate:

- `brilliant_scientist_formation_territory_plan_is_invalid`

## Planner behavior

- Derives facility candidates from the existing primary, secondary, joint-laboratory, project-site, transport-terminal, and temporal-anchor state facts.
- Requires the former host to own and control every state at preparation and revalidation.
- Never selects the former host capital.
- Excludes foreign/third-party joint laboratories while their ownership or control remains foreign.
- Prioritizes primary, secondary, joint, transport, supplied/industrial, and remaining facility capitals in that order.
- Grows contiguous facility chains through bounded deterministic passes.
- Admits separated facilities only when the host has `brilliant_scientist_multi_site_network_verified` and the state has a terminal, serviced air base, or serviced port.
- Adds only adjacent core support states with a concrete rail, supply, port, or factory role.
- Projects retained host states, cores, and factories before marking each candidate.
- Requires `brilliant_scientist_project_mode_history_is_coherent` before selecting a state and again during immediate revalidation.
- Supports a verified one-state or two-state enclave, a two-through-six-state charter target, and a three-through-eight-state rebellion target.
- Freezes state membership with planner-only state flags and persistent host/capital targets; this file performs no state mutation.
- Clears verification before cleanup or revalidation and writes verification last.
- On any invalid path, snapshots attempted metrics, clears every transfer-capable state mark and both planner targets, and publishes an explicit reason enum, including incoherent xenobiological project-mode history. It never selects another route.

## Parent integration required

The parent-owned `brilliant_scientist_form_kruger_state_from_verified_plan` must execute from the former-host country scope and follow this boundary:

```hoi4
brilliant_scientist_revalidate_formation_territory_plan = yes
if = {
	limit = {
		brilliant_scientist_formation_territory_plan_can_be_committed = yes
	}
	# Instantiate/release fixed KRG and begin the first mutation here.
	# Transfer exactly states marked brilliant_scientist_formation_territory_selected.
	# Use brilliant_scientist_formation_capital_state as the KRG capital.
}
else = {
	# Resolve the explicit invalid-plan path. Do not substitute territory/route.
}
```

The formation effect must consume the persistent host and capital targets before calling `brilliant_scientist_clear_formation_territory_plan = yes`.

## Existing integration conflicts requiring parent edits

1. `common/scripted_triggers/016_brilliant_scientist_triggers.txt` currently makes `brilliant_scientist_can_form_enclave` inherit `minimum_origin_states = 2` and separately requires `enclave_minimum_states = 2`. This blocks the verified one-state enclave required by the accepted country-package spec. The parent should make the enclave gate consume `brilliant_scientist_verified_enclave_territory_plan_is_valid` and remove the obsolete two-state dependency for that route. The planner reports the true selected count and does not falsify it to satisfy the old gate.
2. `common/scripted_effects/016_brilliant_scientist_containment_effects.txt` currently calls `brilliant_scientist_resolve_partial_laboratory_uprising` when a full rebellion plan is invalid. That rebuilds under another route and is a route fallback. The parent should replace it with an explicit invalid-rebellion outcome or return to an authored choice that separately selects the enclave route before calling the planner again.
3. Charter and rebellion minimums numerically align with the planner, but their existing gates should include the corresponding stable verified-route predicate rather than accept the shared verification flag and counters alone.
4. The parent formation effect named above was absent during this tranche. Its release/transfer/capital/core/character transaction remains required and is deliberately outside this subagent's file ownership.

## Evidence and validation

- Read the required offline wiki core pages plus country/state pages and the current official vanilla script-concept, script-constant, trigger, and effect documentation.
- Inspected vanilla `events/BBA_Ethiopia.txt` state-transfer/dynamic-country code and the authored Congolese breakaway precedent recorded in the Event 016 vanilla handoff.
- Inspected Chaos Redux Event 006's frozen package planner and exact state-transfer execution path, including host-loss floors, verification-before-mutation, and `set_state_owner_to`/`set_state_controller_to` execution.
- Confirmed every planner-owned helper called by the three new script files resolves. The parent-announced `brilliant_scientist_project_mode_history_is_coherent` dependency was not yet defined in the shared tree at this handoff's final local scan; the parent owns that trigger and must land it with integration.
- Confirmed no new top-level helper name collides with an existing scripted trigger/effect.
- Confirmed the three scripts have structurally balanced blocks/quotes and tab-indented Clausewitz nesting.
- Confirmed the gameplay scripts contain no hardcoded state/capital IDs, recurring on-actions, random state selection, route substitution, or state ownership/control effects.
- Walked the one-state enclave, two-state enclave, two-state charter, three-state rebellion, multi-facility corridor, foreign joint-lab exclusion, separated-site, host-survival failure, and stale-state revalidation scenarios against the implemented contracts.

The read-only HOI4 MCP lint was attempted for all three files but could not scan them because the MCP server returned `ARTIFACT_STORAGE_LIMIT` with no files scanned or diagnostics. This is a tooling-storage blocker, not a passing lint result. The local structural and call-graph checks above were used instead.

## Assets, localisation, and documentation

No icon, sprite, image, localisation key, player-facing object, or spreadsheet row is introduced by the planner, so no asset or localisation handoff is required. The planner document records the state flags, targets, counters, parent sequence, invalid reasons, scenario matrix, icon status, and future extensions.

## Simplifications, omissions, and blockers

No territory route in this planner was replaced with a fallback or arbitrary-state substitute. The planner implements its full bounded scope.

Event 016 country formation as a whole is not complete from this tranche: the parent still owns fixed-tag instantiation, exact marked-state transfer, capital/core/control setup, character reconciliation, force setup, containment gate edits, route-specific invalid outcomes, and post-formation cleanup. The two existing gate/fallback conflicts above must be resolved before a one-state enclave or strict no-fallback rebellion can be claimed complete.

No commit was created, per parent instruction.

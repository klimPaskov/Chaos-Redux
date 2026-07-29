# Event 016 Containment Implementation Handoff

## Scope

This tranche implements the hosted sovereignty board, its eight timed actions, deterministic causal resolver, exact outcome history, Evolution IV integration, forced deadline resolution, invalid-contract handling, outcome reports, localisation, asset contract, and system documentation.

It does not claim completion of the Kruger State country or focus package. The territory planner and country-formation effects remain separate consumers/providers and must be reviewed before this tranche can be accepted as fully wired.

## Files

Added:

- `common/script_constants/016_brilliant_scientist_containment_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`
- `common/decisions/016_brilliant_scientist_containment_decisions.txt`
- `events/016_brilliant_scientist_containment_events.txt`
- `localisation/english/016_brilliant_scientist_containment_l_english.yml`
- `docs/systems/016_brilliant_scientist_containment.md`
- this handoff

Modified:

- `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt`
- `events/016_brilliant_scientist_evolutions.txt`
- `common/decisions/016_brilliant_scientist_evolution_missions.txt`
- `interface/016_brilliant_scientist.gfx`

## Stable interfaces

Parent callers may use:

- `brilliant_scientist_prepare_sovereignty_board = yes`
- `brilliant_scientist_resolve_containment_action = yes` with temporary `brilliant_scientist_containment_action`
- `brilliant_scientist_resolve_unanswered_sovereignty_deadline = yes`
- `brilliant_scientist_calculate_containment_scores = yes`

The resolver consumes these territory/country interfaces:

- `brilliant_scientist_prepare_formation_territory_plan = yes`
- `brilliant_scientist_can_form_by_charter = yes`
- `brilliant_scientist_can_form_by_rebellion = yes`
- `brilliant_scientist_can_form_enclave = yes`
- `brilliant_scientist_form_kruger_state_from_verified_plan = yes`
- `brilliant_scientist_transform_host_into_kruger_state = yes`

The first four belong to the isolated territory-planner surface. The last two belong to the parent-owned KRG country package.

## Resolution guarantees

- No random roll chooses a containment outcome.
- Every coercive action recalculates government and Kruger strength at completion.
- Release is restricted to low authority risk, low Dependence, low Independent Capacity, no weaponization, and a small facility network.
- Exile and foreign defection use the guarded existing character-transfer transaction.
- Charter, rebellion, and enclave plans are route-specific and revalidated before land moves.
- Institutional takeover requires proven institutional capture; Evolution IV cannot offer concession without that proof.
- Failed legal/map validation explicitly reopens the board through event `.32`; it does not silently choose another country outcome.
- Completed outcomes close the mission, clear the exile target, and record one exact `ever_*` history flag.
- Event `.30` resolves an unanswered deadline from the earlier Evolution IV response and live state.

## Validation performed

- Event IDs `.30`, `.31`, and `.32` are unique in the live event tree.
- Every new decision, event title, description, option, trigger tooltip, and effect tooltip has English localisation.
- All decision icons resolve to registered vanilla sprites.
- The new scripts have balanced delimiters and contain no unsupported comparison operators.
- The localisation file is UTF-8 with BOM and uses the repository's no-`:0` key form.
- No periodic world iteration was added. The only country scan is the one-shot exile-recipient selection executed when the board is prepared.

## Open integration risks

- The confrontation DDS is registered but must be supplied and reviewed by the Event 016 asset worker before acceptance.
- Territory-planner interfaces are deliberately unresolved until their separately reviewed implementation lands.
- KRG formation and host-transformation effects are deliberately unresolved until the country package lands.
- Event-log and event-details entries for the containment/KRG outcomes belong to the later shared integration tranche.
- Country and decision audit subagents must review the fully wired result before completion.

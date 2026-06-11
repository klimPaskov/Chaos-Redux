# Decision and mission implementation prompt for Event 007 Fury

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the Fury decision spec.

Source spec:

- `docs/specs/007_fury_specs/specs/007_fury_decisions_missions_spec.md`
- `docs/specs/007_fury_specs/matrices/007_fury_ai_balance_matrix.md`

## Implement the Fury War Office category

The category must support:

- target selection.
- target preparation.
- finite reserve reinforcement controls.
- depot conversion.
- conquest settlement.
- compliance and coring.
- cooperation with other Fury actors.
- rivalry with other Fury actors.
- no-neighbor setup.
- world-end preparation when eligible.

## Costs

Do not make the category a political power store.

Use varied costs:

- army XP.
- command power.
- infantry equipment.
- support equipment.
- manpower.
- trains.
- trucks.
- convoys.
- fuel where relevant.
- stability and war support risks.
- compliance and state control.
- supplied divisions in named border states.

Political power can appear for diplomacy or bureaucracy, but it must not be the default cost.

## Missions

Implement map-action missions where specified:

- Guard the Fury Capital.
- Secure the First Depot Belt.
- Hold the New Registers.
- Border Watch for non-Fury neighbors.
- Keep the Aid Route Open.

Missions must use named regions or scripted localisation. Do not expose raw state id lists.

## AI behavior

AI Fury should actively use the category.

AI rules:

- choose next target when valid.
- prepare target when at war readiness is low.
- use capped emergency reserve tools if losing.
- use occupation and coring when overextension is high.
- cooperate in pact type.
- use rivalry in hostile type.
- avoid impossible targets and protected invalid targets.

## Cleanup

Clear stale decisions, missions, target flags, state group flags, and scenario setup flags.

No decision should remain visible after target death, target invalidation, country capitulation, Fury defeat, or state coring completion.

## Validation scenarios

Run or document targeted checks for:

- Fury actor with a valid target.
- Fury actor with no valid target.
- Fury after first conquest.
- Fury with high overextension.
- two Fury actors in pact type.
- two Fury actors in hostile type.
- player neighbor after Fury major threshold.
- Maximum scenario with many active Fury actors.

Report any simplification or missing decision family.

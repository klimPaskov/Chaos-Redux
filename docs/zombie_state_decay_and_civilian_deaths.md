# Zombie State Decay and Civilian Death Pressure

## Overview

This mechanic adds two linked layers of long-term collapse pressure:

- zombie-controlled states now physically decay over time,
- combat now causes stronger civilian deaths in enemy frontline states.

Both mechanics feed into the existing chaos-meter deaths pipeline instead of creating a parallel casualty tracker.

## Zombie State Decay

Zombie-controlled states now deteriorate while they remain under outbreak control.

### Population loss

- each zombie-controlled state loses `0.5%` of its current population every `30` days,
- the loss is applied for at most `36` monthly ticks per state,
- after `36` ticks, population decline stops permanently for that state unless the system is redesigned later.

Implementation notes:

- the timer follows actual zombie captures through `on_state_control_changed`,
- existing outbreak states that predate the capture hook self-initialize the first time the zombie runtime processes them,
- deaths use the normal chaos-meter state-population pipeline and appear as civilian deaths with the cause `Zombie occupation collapse`.

### Structural degradation

Every `180` days under zombie control, the state attempts one degradation pass:

1. remove one productive state building if one still exists,
2. degrade the state category by one step toward `wasteland`.

Current building removal priority:

- civilian factory
- military factory
- dockyard
- synthetic refinery
- fuel silo
- infrastructure
- air base
- bunker
- coastal bunker
- anti-air
- radar

Current category ladder:

- `rural -> pastoral -> wasteland`
- island and enclave categories collapse directly to `wasteland`

Urban and town categories are intentionally preserved. Zombie occupation still strips buildings there, but category collapse only begins once a state is already `rural` or lower.

## Combat Civilian Deaths

Combat civilian deaths are now actually applied from leader combat hooks instead of only being defined in constants.

Rules:

- only offensive combat is considered,
- deaths are applied to a random enemy frontline state where the leader is actively fighting,
- fascist countries have the highest baseline,
- communist countries are next,
- non-aligned countries are lower,
- democratic countries trigger this only rarely,
- `chaos_warfare` increases both the death rate and the chance to trigger,
- higher global chaos tiers further scale the death rate upward.

This keeps the mechanic focused on countries actively inflicting devastation into enemy territory instead of always hitting both sides symmetrically.

## Shared Death Pipeline

The new mechanics reuse:

- `chaos_meter_register_state_civilian_deaths_percent`
- `chaos_meter_register_deaths`

That means they:

- reduce state population directly,
- increase the global civilian death total,
- contribute to chaos through the existing deaths-to-chaos rule,
- show up in the deaths UI with proper cause text.

## Tuning Files

- `common/script_constants/zombie_constants.txt`
- `common/script_constants/chaos_meter_constants.txt`
- `common/scripted_effects/002_zombie_outbreak_effects.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `common/on_actions/chaosx_on_actions.txt`

## Icon Wiring

No new icons or audio are required.

## Future Plans

1. Add separate devastation rules for special zombie classes such as Wendigo if they should ruin states faster than ordinary outbreaks.
2. Add regional famine and refugee pressure as follow-on effects once a state has spent long enough under zombie decay.
3. Split combat civilian deaths into artillery, urban assault, encirclement starvation, and scorched-earth sub-causes if the deaths UI should become more granular.

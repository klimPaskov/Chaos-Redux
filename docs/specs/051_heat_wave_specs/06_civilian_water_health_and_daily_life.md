# Civilian Water, Health, and Daily Life

## Water as the central civilian pressure

Water is the main civilian theme of Event 51. It should shape city survival, sanitation, hospitals, agriculture, industry, and military supply without becoming a universal stockpile.

The event should calculate hidden state Water Pressure and use it to change Local Heat Stress, report selection, decision targets, mortality risk, Famine proof, Migration proof, and infrastructure damage.

## Hidden Water Pressure

Water Pressure should consider:

- Local Heat Stress
- state population
- urban and industrial concentration
- agricultural load
- military load
- infrastructure
- local supply
- recent drought pressure
- reservoir and pumping-system condition represented by event state
- power availability
- occupation and damage
- active relief access
- current national protection priority
- completed water decisions and missions

Water Pressure is not shown as a third meter. The state tooltip uses a concise causal status such as stable service, rationing, severe shortage, or system failure.

## Water condition stages

Working internal stages:

| Stage | Meaning | Player-facing consequence |
| --- | --- | --- |
| Stable | Demand remains within local capacity | No special water action required |
| Pressured | Demand exceeds ordinary capacity | Water actions become useful and local penalties rise |
| Rationed | Emergency allocation is active | Civilian and industrial tradeoffs become visible |
| Severe shortage | Service is unreliable or inadequate | Health, sanitation, food, and migration risks rise |
| System failure | Pumping, treatment, or distribution cannot meet basic demand | Evolution I death risk and emergency movement become possible |

The event should use confirmation windows before stage changes.

## Urban water crisis

Dense cities can reach dangerous civilian conditions even when nearby rural states remain manageable. Urban pressure should reflect:

- high population density
- heat retained through the night
- power demand
- hospital load
- water distribution limits
- worker exposure
- displaced arrivals
- damaged infrastructure

A city should not receive an automatic penalty merely because it is the capital. Capital and victory-point status should increase the consequence and action priority, not replace the actual calculation.

## Rationing

Emergency rationing should reduce immediate demand and protect basic service. It should create real costs:

- reduced factory or construction activity
- lower stability or local public confidence only when shortages are severe
- lower agricultural allocation when cities are prioritized
- administrative or transport burden
- increased black-market or enforcement reports where conditions support them

Rationing should be most effective when started before system failure. Late rationing can reduce death risk but cannot instantly restore service.

## Cooling centers and shelters

Cooling centers represent shaded public halls, underground spaces, schools, transit buildings, hospitals, and other period-appropriate communal shelters.

They should:

- reduce urban mortality risk
- reduce hospital overflow
- protect vulnerable population
- consume civilian capacity, manpower, support equipment, fuel, or transport
- work better with functioning power and water
- become overcrowded when displacement or population exposure is very high

They should not give a flat national heat immunity.

## Hospitals and medical capacity

The event should derive an internal medical-response factor from available shared state or country facts. It can consider:

- infrastructure
- population pressure
- active war damage
- Famine stage
- relevant national preparation
- cooling-center coverage
- local supply

Hospital overflow can:

- raise Evolution I mortality
- reduce recovery speed
- create local report events
- increase demand for transport and support equipment

The event should not create a separate hospital capacity meter unless a future shared health system owns it.

## Sanitation

Severe water shortage should increase sanitation failure risk. Effects can include:

- local stability or compliance pressure where supported
- higher disease vulnerability through a bounded owner callback
- weaker factory and construction labor
- increased Migration pressure
- hospital burden
- local incidents involving contaminated emergency sources

Event 51 should not directly start a disease outbreak unless the owning disease system provides a compatible validated gateway. Report text can describe sanitation problems without claiming a separate epidemic.

## Baseline health effects

Baseline Heat Wave is dangerous but does not apply systematic recurring mass mortality.

Baseline can cause:

- isolated fatal incidents tied to specific reports
- temporary worker illness and lost productivity
- hospital pressure
- reduced civilian output
- unit heat illness without recurring manpower loss
- local evacuation from a failed building, factory, or water system

Any isolated population loss should be bounded, condition-linked, and recorded through the shared exact population path. It should not imitate the recurring mortality loop reserved for Evolution I.

## Evolution I mortality

The Killing Heat permits recurring civilian population loss.

A state must meet all of these conditions:

- uses ordinary civilian systems
- Extreme or Scorched Local Heat Stress
- sufficient lethal exposure duration
- current population above the protected floor
- valid owner and target-country proof
- no duplicate transaction for the current pulse

Mortality scales with:

- exposed population
- current Heat Stress
- water condition
- nighttime retention
- infrastructure
- medical response
- food security
- war and devastation
- mitigation
- duration of uninterrupted lethal exposure

Dense cities with failed water and power can suffer more than sparsely populated desert states. Prepared states can reduce loss substantially.

The exact transaction should use the shared population-loss helper and register one Deaths reason for heat. The event must not maintain a second death ledger.

## Vulnerable population without a new demographic ledger

The calculation can use broad vulnerability proxies, but it should not create a new age, disability, or medical demographic model. The player needs actionable state conditions, not a population simulator.

Use existing population, urban, health, infrastructure, Famine, displacement, and devastation facts to represent vulnerability.

## Daily-life report families

Daily-life flavour should be tied to real state conditions. Useful families include:

- night sleeping outdoors
- schools or offices closing during peak hours
- factories shifting to night work
- water queues at rail stations or public squares
- municipal fountains running dry
- hospitals opening improvised wards
- workers collapsing on construction sites
- crowded rivers, lakes, beaches, and tunnels
- ration cards and guarded water points
- water deliveries by truck or train
- animals moved into shaded public structures
- public baths or laundries closing
- funeral services operating at night during Evolution I
- unusually warm northern nights
- prisoners, refugees, and occupied populations facing unequal access

Reports should use current state, country, ideology, war state, and mitigation to determine viewpoint and tone.

## Public order

Water shortages can create unrest, but unrest should follow severe scarcity, unequal distribution, failed missions, or coercive choices. Heat alone should not randomly remove stability from every country.

Possible responses include:

- orderly rationing
- municipal self-organization
- military distribution
- black-market diversion
- protests at closed pumps
- violent seizure of a depot
- local corruption
- mutual aid

The event should choose the response from government capacity, stability, occupation, current priority, and severity.

## Unequal allocation

The national priority system can create explicit tradeoffs:

- Protect Population Centres sends water and cooling capacity to major cities.
- Sustain the Front shifts transport and water toward military supply.
- Defend the Harvest reserves water and transport for agriculture.
- Preserve Industrial Output protects power and factory cooling.
- Balanced Emergency Plan spreads weaker mitigation across sectors.

The player should see the visible consequence of the chosen priority. Hidden formulas should not obscure which sectors lose protection.

## Recovery

Water systems should recover more slowly than air temperature.

Recovery actions can restore:

- pumping capacity
- treatment capacity
- distribution networks
- reservoirs and storage
- emergency transport reserves
- hospital normal operations

A state that reached System Failure should require a recovery mission or a longer passive restoration period. A state that remained only Pressured can recover automatically as Heat Stress falls.

## Acceptance cases

1. A dense, damaged capital reaches Severe shortage before a supplied rural state.
2. Early rationing prevents System Failure but reduces factory or agricultural activity according to priority.
3. Cooling centers reduce mortality risk only where they operate.
4. Evolution I deaths use real state population and appear once in Deaths.
5. Ending the Heat Wave does not instantly repair a failed pumping system.
6. An actual nonhuman country does not receive ordinary civilian water decisions or reports.

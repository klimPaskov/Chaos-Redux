# Decisions and Missions

## Presentation model

Event 51 uses one compact ordinary decision category with a strong category picture and dynamic header. It should not open a separate full mechanic window.

The category header shows:

- Global Heat Wave Intensity band and trend
- national exposure summary
- up to three current hotspots
- active national protection priority
- one dominant risk line
- one recovery line when the episode is declining

The header should not display raw internal Water Pressure, Agricultural Pressure, Cooling Pressure, military load, or exposure points.

## Visibility budget

Per phase, show:

- three to five primary clickable actions
- no more than six primary actions
- one or two active missions normally
- up to three active missions during Evolution II or III when the country has several distinct urgent fronts

Obsolete actions disappear when their target, phase, or protection state is invalid.

## National protection priorities

The country chooses one priority. Switching has a meaningful cooldown and conversion cost.

| Working priority | Strong protection | Accepted sacrifice | AI profile |
| --- | --- | --- | --- |
| Protect Population Centres | Urban water, cooling centers, hospitals, mortality reduction | Weaker farm, industry, or army allocation | Dense urban countries, peace, Evolution I mortality |
| Sustain the Front | Military water, supply, acclimatization, rotation support | Higher civilian and agricultural pressure | Countries in major war with hot active fronts |
| Defend the Harvest | Irrigation, farm labor, livestock, food transport | Stricter urban rationing or lower industrial output | Agrarian and food-vulnerable countries |
| Preserve Industrial Output | Power, factory cooling, rail, ports, extraction | Higher water demand and civilian exposure | Industrial majors and critical war producers |
| Balanced Emergency Plan | Moderate mitigation across all sectors | No sector receives maximum protection | Countries with mixed exposure or low administrative capacity |

Priority effects should scale with actual committed resources and national capacity. Selecting a priority is not a free permanent bonus.

## Priority switching

Suggested cooldown: 30 days.

Switching should cost one to three fitting resources, such as political power, civilian factory burden, trains, fuel, command power, or stability. The cost must reflect the sectors being redirected.

Emergency override can allow one early switch before the first major surge or one late switch after an evolution activation. Repeated switching should become expensive or unavailable.

## Primary actions

### Emergency Water Rationing

**Role:** Reduce immediate civilian and industrial demand in selected high-pressure states.

**Availability:** At least one owned or controlled ordinary-civilian state has Pressured water or worse.

**Targeting:** Highest-risk urban or mixed state, with manual selection where the decision framework supports it cleanly.

**Costs:** Civilian factory burden, transport, temporary factory output, and possibly stability when coercive enforcement is chosen. Maximum four cost types.

**Effects:** Lower Water Pressure, reduce lethal exposure gain, protect basic service, increase sector tradeoff according to national priority.

**Risk:** Starting too late cannot immediately reverse System Failure. Overlong rationing can create unrest or industrial loss.

**AI:** High priority when a populated state is approaching System Failure.

### Open Cooling Centres

**Role:** Protect exposed urban population and reduce hospital overload.

**Availability:** Dangerous or higher urban Heat Stress and ordinary civilian systems.

**Costs:** Civilian capacity, manpower, support equipment, fuel or trucks.

**Effects:** Strong local mortality mitigation, lower hospital pressure, better Migration reception.

**Risk:** Overcrowding and weak power or water reduce effectiveness.

**AI:** High under Evolution I in dense cities.

### Establish Army Heat Protocols

**Role:** Build acclimatization, work-rest, hydration, night movement, and rotation support.

**Availability:** Country fields units in Dangerous or higher states, or expects a hot front soon.

**Costs:** Army XP or command power, support equipment, motorized equipment, fuel, or temporary training loss.

**Effects:** Lower division exposure gain, improve acclimatization, reduce heat casualty risk.

**Risk:** Cannot compensate for complete supply failure. Consumes scarce logistics assets.

**AI:** High during war, low for countries without exposed forces.

### Protect the Harvest

**Role:** Protect one key agricultural region.

**Availability:** A valid agricultural hotspot is Dangerous or rising quickly.

**Costs:** Civilian capacity, trains, trucks, fuel, manpower, or temporary urban water allocation.

**Effects:** Starts or strengthens a harvest mission, reduces agricultural pressure, improves Famine projection.

**Risk:** Diverts transport and water from cities, industry, or the front.

**AI:** High for food-vulnerable or embargoed states.

### Railway Heat Maintenance

**Role:** Keep a critical corridor functioning.

**Availability:** A critical rail, supply, port, front, or agricultural corridor is at risk.

**Costs:** Trains, civilian capacity, support equipment, manpower, fuel.

**Effects:** Reduces throughput loss and damage risk, starts corridor mission where appropriate.

**Risk:** Speed restrictions reduce short-term throughput even when damage is prevented.

**AI:** High when the corridor supplies a front, capital, or food region.

### Convert to Night Shifts

**Role:** Move industrial and construction work away from peak daytime heat.

**Availability:** Industrial hotspot at Dangerous or higher, not already converted.

**Costs:** Temporary production disruption, civilian capacity, fuel or transport, administrative cost.

**Effects:** Lower worker and machinery pressure, smaller industrial contribution to Heat Stress.

**Risk:** Weak effect during very hot nights, lower coordination in damaged states.

**AI:** High in industrial states when controlled shutdown would be too costly.

### Controlled Industrial Shutdown

**Role:** Sacrifice current output to prevent damage.

**Availability:** Extreme or Scorched industrial state with rising damage risk.

**Costs:** Direct temporary factory, dockyard, extraction, or construction loss.

**Effects:** Strong reduction in sector pressure and building-damage chance.

**Risk:** Major wartime opportunity cost.

**AI:** Use when expected permanent damage is worse than temporary output loss.

### Emergency Food Imports

**Role:** Support food reserves and relief access after crop loss.

**Availability:** Food pressure rising, valid ports or land route, and no owner-system block.

**Costs:** Civilian factories, convoys or trains, fuel, and foreign access.

**Effects:** Submit or strengthen relief through Famine's owner path, reduce immediate food pressure.

**Risk:** Embargo, convoy losses, port heat, or route disruption can reduce delivery.

**AI:** High for import-capable countries facing harvest failure.

### Reservoir and Pumping Protection

**Role:** Protect state water infrastructure before failure.

**Availability:** Pressured or Rationed water stage with functioning system still present.

**Costs:** Civilian capacity, fuel, motorized equipment, support equipment.

**Effects:** Slow Water Pressure growth, reduce power-failure interaction, improve recovery.

**Risk:** Competes with industrial and military logistics.

**AI:** High for capital and major urban states.

### Organize Heat Evacuation

**Role:** Prepare an orderly movement request before a state becomes uninhabitable.

**Availability:** Migration owner accepts the request profile, destination safety exists, and the origin is Extreme or Scorched.

**Costs:** Trains or convoys, trucks, fuel, manpower, civilian capacity.

**Effects:** Submit organized evacuation through Migration with better route safety and lower trapped-population risk.

**Risk:** Reception pressure at destination and loss of local labor.

**AI:** Use only when mitigation cannot keep the origin safe.

## Recovery actions

### Restore Water Service

Targets a state that reached Severe shortage or System Failure. It shortens the recovery lag and removes a persistent temporary water-service penalty after concrete repair work.

### Reopen Heat-Damaged Industry

Targets a state whose factories were shut down or damaged. It restores temporary closure effects and supports normal building repair. It does not recreate destroyed factory levels.

### Repair the Critical Corridor

Targets rail or infrastructure damage created or intensified by the episode. It should connect to normal repair and supply systems.

### Rebuild Agricultural Capacity

Targets a damaged agricultural state and reduces lingering pressure. Permanent terrain degradation requires the owning environmental route and cannot be removed by one recovery decision.

### Rest Exhausted Formations

Accelerates division exposure recovery after units leave severe states. It temporarily reduces availability or training.

## Mission family

### Maintain Water Deliveries in [State]

**Duration:** 90 to 120 days.

**Objective:** Keep the target state supplied with the required transport and prevent Water Pressure from reaching System Failure.

**Success:** Strong water mitigation, lower mortality risk, better recovery.

**Partial success:** System avoids total failure but remains in Severe shortage.

**Failure:** Water-system failure, hospital pressure, possible Migration request, Evolution I death risk.

### Keep [Corridor] Operational

**Duration:** 120 to 180 days.

**Objective:** Maintain named rail and infrastructure links and commit required trains or repair capacity.

**Success:** Preserve throughput and reduce damage risk.

**Partial success:** Corridor remains open under severe restriction.

**Failure:** Real damage or a serious route penalty.

### Rotate Formations from [Front]

**Duration:** 60 to 100 days.

**Objective:** Move overexposed divisions into lower-stress states while maintaining an adequate defense where required.

**Success:** Reduce exposure, lower local military load, strengthen protocols.

**Partial success:** Some units recover while others remain Critical.

**Failure:** Higher exposure and Evolution I casualty risk.

### Protect the [Agricultural Region] Harvest

**Duration:** 120 to 180 days.

**Objective:** Keep key states below catastrophic agricultural pressure while preserving transport and water access.

**Success:** Avoid or weaken Famine request, preserve resilience.

**Partial success:** Protect part of the region and reduce the request severity.

**Failure:** Harvest failure, Famine proof, Migration pressure.

### Secure the Emergency Food Route

**Duration:** 90 to 150 days.

**Objective:** Keep a port, land route, convoy flow, or rail connection valid long enough for relief delivery.

**Success:** Famine-owned reserve or relief improvement.

**Partial success:** Reduced delivery with ongoing shortage.

**Failure:** Lost delivery, transport cost, stronger shortage.

### Restore Reservoir and Pumping Capacity

**Duration:** 120 to 180 days during recovery.

**Objective:** Repair water-service proxies and maintain fuel, transport, and civilian commitment.

**Success:** Remove recovery penalty and protect against later episode vulnerability.

**Failure:** Extended recovery and continued urban pressure.

## Dynamic cost design

Costs should scale by:

- exposed population
- target state importance
- number of states covered
- current Heat Stress
- current infrastructure
- country industry
- transport stockpiles
- current war state
- national priority alignment
- previous use in the same episode

Costs should use multiples of five where authored. Decision text must display each cost with the correct texticon and use no more than four spendable cost types.

## Category phasing

### Onset

Visible actions should favor preparation: national priority, reservoir protection, army protocols, early harvest protection, rail monitoring.

### Expansion and surge

Visible actions should favor emergency response: rationing, cooling centers, rotation, night shifts, food routes, controlled shutdown.

### Decline

Emergency actions remain only for states still hot. Recovery missions begin appearing for cooled states.

### Recovery

Only repair, reopening, return-support, and formation-rest actions remain.

## Anti-store rule

The category must not become a set of buttons that all reduce Heat Stress. Each action has a distinct target, sector, cost, and failure it prevents.

The player should often be unable to fund every useful action. Clicking one action can make another harder by consuming transport, fuel, factories, manpower, or water allocation.

## AI-equivalent path

AI should evaluate the same actions without requiring a human target-selection interface. It can use hidden target scoring, event-owned decisions, or supported timed pulses.

AI decisions must be probability-audited under named scenarios. Invalid targets, dead countries, annexed states, closed routes, missing ports, absent fronts, and owner-system rejection must force weight to zero.

## Cleanup

Every decision and mission must define cleanup for:

- state changes controller
- target becomes invalid
- country is annexed
- Heat Wave enters recovery
- Heat Wave cleanup completes
- evolution is disabled before activation
- owner system rejects a request
- a new episode generation begins

No stale selected target, mission, category, or mitigation flag may survive into the next episode.

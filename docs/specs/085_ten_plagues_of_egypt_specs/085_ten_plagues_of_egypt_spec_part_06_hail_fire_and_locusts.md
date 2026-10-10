# 6. Hail and Fire, Then Locusts

## VII. Hail and Fire

A supernatural storm of enormous hail, lightning and fire strikes the warned states.
It is the sequence's main physical-destruction phase, and it hits places the player can name and prepare.

### Warning

The warning arrives with Boils, five days before the first impact, and names each threatened state.
A state added later by an Evolution or a moving continuation receives its own five-day warning.
No phase change shortens an accepted warning.

The biblical warning to bring people in from the fields gives sheltering its role.
The game extends it to shelters, rail workers, depots and airfields without claiming modern precautions explain the anomaly.

### Responses

- **Shelter Before the Storm** (Part 14) shelters a threatened state's exposed population before impact.
It is the main protective action and the main Wrath credit of the phase.
- A site variant protects equipment, an air base or a rail hub instead; it saves material, not people, and earns partial credit.
- Migration's **Evacuate Civilians** can move people to a safe state if the transfer completes before impact; evacuees outside the state at impact are not exposed.
- **Harden Our Hearts** keeps factories and airfields working through the warning.

Decision text distinguishes saved people, saved material and continued production.

### Impact

| Element | Anchor |
| --- | --- |
| Civilian mortality | 250 basis points of the exposed population before Wrath, intensity and shelter, as one budget for hail and fire together |
| Building damage | About a quarter of vulnerable local infrastructure, rail, air base, industry and civilian service capacity, repairable; more under high Wrath and Evolutions |
| Crop damage | A food shock to Famine for the destroyed harvest |
| Equipment and divisions | Only stockpiles and divisions actually in the struck state; military casualties stay with the military owner |

### Natural Disasters ownership

Every impact goes through the public `call_natural_disaster` gateway with a selected-state target and supplied proof, and no Event 013 history row.
Natural Disasters owns impact scheduling, physical damage, mortality under its disaster Deaths reason, reports and aftermath; Event 085 supplies the plague, Wrath-scaled severity and shelter result.
A correlation tag lets Event 085 reports and achievements recognize the result.

The gateway already exposes hailstorm and wildfire families.
Hail with a causal fire needs one composite call or owner extension that shares a single exposed-population budget, keeps independent building damage and uses the original warning.
Two uncoordinated full-strength calls are not acceptable.
Existing disaster rescue and repair actions stay with Natural Disasters; a completed shelter or rescue result is credited once to Divine Wrath.

## VIII. Locusts

Locust fronts move across states and consume surviving crops and exposed food.
The phase needs a geography; a single 25-day national modifier is not enough.

### Fronts

The event seeds fronts among eligible states, each moving through a bounded chain of adjacent states.
Disconnected islands and land regions can get their own seed; no front jumps between continents.
Each forecast names the next threatened state a few days ahead.
Equivalent candidates have equal weight.
Evolutions add fronts and widen coverage instead of rolling the whole world repeatedly.

### What the locusts consume

Locusts consume only what remains.
A state that lost most of its harvest to Hail and Fire takes a smaller additional food shock, not the same loss twice.
Once a front leaves a state, its loss is settled.
Urban states without fields can still lose stored food through the same Famine shock; do not invent field damage there.

The combined damage of Livestock, Hail and Fire and Locusts makes this the event's largest indirect mortality period, and all of that hunger mortality belongs to Famine.
Event 085 applies no locust death percentage of its own.

### Responses

- **Preserve the Remaining Harvest** (Part 14) protects or moves food in the next threatened state before the front arrives.
Full success cancels most of that state's locust food shock.
A route destroyed by the storm makes the transport variant impossible; the player sees the reason and can choose the local variant while time remains.
- Foreign relief can open a corridor from a safer donor that is also feeding its own people (Part 10).
- **Harden Our Hearts** requisitions food for the army; the extraction goes to Famine and deliberate abandonment of a started harvest objective raises Wrath (Part 2).

## The landscape before Darkness

By the end of Locusts the map should show protected refuges, damaged transport, hungry regions and working relief routes through existing state and humanitarian displays, not new Event 085 meters.
Famine does not pause for Darkness and storm damage does not repair itself.
Countries that kept civilian services alive can carry out the last preparation efficiently; countries that kept only their armies have fewer institutions left to do it.

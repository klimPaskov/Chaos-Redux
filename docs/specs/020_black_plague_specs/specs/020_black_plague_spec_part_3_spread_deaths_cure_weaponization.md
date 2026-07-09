# 020 Black Plague spec Part 3 - Spread, deaths, cure, and weaponization

## State-to-state spread

Spread should run from infected states into nearby threatened states. It should feel local at first. The ordinary spread path should be land adjacency, with ports and overseas jumps locked behind Evolution II.

Spread risk should be built from factors the player can understand.

| Factor | Effect on spread |
| --- | --- |
| Shared border with infected state | Main early spread path. |
| High population | Higher chance and higher death impact after infection. |
| Low development | Higher chance due to weaker response. |
| Poor infrastructure | Higher chance and weaker treatment movement. |
| Active port | Higher chance for coastal threat and later overseas spread. |
| Active combat | Higher chance due to troop movement, bodies, chaos, and refugees. |
| Occupied or resisted state | Higher chance due to broken administration. |
| Open borders and faction movement | Higher chance through regular movement. |
| Army presence from infected states | Higher chance when troops move or retreat. |
| Refugee pressure | Higher chance after harsh fighting, famine, or state loss. |
| Quarantine and border controls | Lower chance. |
| Medical capacity and cure progress | Lower chance and lower severity if infection starts. |
| Rat-held neighbor | Very high chance unless militarily sealed. |

The disease should not randomly teleport across the map in baseline. Distant spread without Evolution II should be rare and tied to troop movement, special projects, or accidents.

## Spread stages inside a state

Ordinary state progression should not be logged as evolutions. It is the normal disease lifecycle.

| Stage | Meaning | Main risks |
| --- | --- | --- |
| Exposure | State has pressure from neighbor, port, troops, or refugees. | Can become threatened. |
| Threatened | Local alarms, screenings, and rumors begin. | Can become infected if ignored. |
| Early infection | The disease has taken root. | Deaths start and spread pressure rises. |
| Established infection | Disease load grows. | Deaths become severe and containment costs rise. |
| Crisis infection | Local systems fail. | Large death ticks, panic, riots, and neighboring spread. |
| Collapse infection | Normal governance weakens. | Rat warren pressure and breakaway risk rise. |

## Death integration

Deaths must be passed into the shared Deaths system. The death log should classify the loss as civilian deaths unless a military unit or battle-specific event caused the loss. Military disease losses can exist when army cordon or troop movement events fire, but the core population decline should be civilian.

Death log entries should include:

- affected country
- affected state where supported
- death type: civilian or military
- source label direction: Black Death, weaponized Black Death, or rat-held plague state
- recent death count
- cumulative event death contribution if the existing Deaths UI supports it

The Black Death should also add chaos through the existing death-to-chaos conversion. It should not create a parallel chaos source for the same deaths.

## Population loss scale

The event must be capable of very large population loss. The implementation should use population-share bands with flat death numbers only as support values.

Design bands:

| Response quality | Expected long-run state outcome |
| --- | --- |
| Fast strong response | Small to moderate population loss, slow recovery, and high economic cost. |
| Late response | Severe population loss in the first infected state and moderate spread. |
| Weak response | Multiple states lose large population shares over time. |
| Wartime collapse | High-population states can be devastated. |
| Weaponized strike | Target state can suffer fast high death pressure and become a spread source. |
| Rat-held collapse | Population death continues until the state is retaken and cleared. |

The spec does not set exact real-world values. The implementation should balance through script constants and test scenarios. The player must notice the losses through population, manpower, local industry, supply, resistance, stability, and Deaths UI updates.

## Cure and countermeasure progress

A cure or countermeasure should be a progress track, not an instant cleanup button. The owner of infected states can work on treatment progress. Advanced countries and countries with biowarfare capability should work faster, but even they need time and resources.

Cure progress should do three things in order:

1. Lower death pressure.
2. Lower spread pressure.
3. Allow cleanup and recovery when local disease load is low enough.

Cure progress should scale from:

- medical capacity
- field hospital investment
- industrial capacity
- research capacity
- disease samples from infected states
- cooperation with countries that have infected states
- existing biowarfare tech
- containment safety tech
- chaos tier and evolution stage
- damage from lab accidents or weaponized misuse

Cure progress should be disease-specific where needed but presented through the shared disease UI. A country can have Black Death treatment progress without creating a separate category.

## Shared international research

Countries should be able to help global countermeasure progress when the disease becomes large enough. This can happen through shared medical missions, sample exchanges, and field hospital support. Cooperation should reduce deaths, but countries using Black Death as a weapon should face trust penalties and condemnation.

Possible choices:

- Share samples openly to accelerate cure progress and reduce condemnation risk.
- Keep samples secret for weaponization and lose cooperation benefits.
- Accept foreign medical teams for faster treatment and possible intelligence exposure.
- Send field hospitals to a neighbor for improved containment and diplomatic goodwill.
- Close all borders and reject cooperation for lower exposure but slower research.

## Weaponization path

Once Black Death exists in the world, countries with biological warfare capability can begin a long special project to weaponize it. This must use the existing special-project and biowarfare structure. It should not be a one-click event button.

The path should remain gameplay-only abstraction.

Special project phases:

| Phase | Gameplay meaning | Main risks |
| --- | --- | --- |
| Acquire samples | The country obtains infected material from an infected state, ally, occupied area, or covert network. | Exposure risk and diplomatic exposure. |
| Study countermeasures | The country learns how to survive handling and counterstrike exposure. | Slow progress but safer stockpile. |
| Delivery planning | The country adapts existing biowarfare delivery systems. | Condemnation, accident risk, and project failures. |
| Payload readiness | Weaponized Black Death becomes usable through existing biowarfare deployment. | Stockpile accidents and retaliation risk. |
| Field deployment | Target enemy state is hit through the existing delivery system. | Runaway spread, global condemnation, and blowback. |

The project should have many iterations and events. It should be long, expensive, and risky.

Special project iteration families:

- sample acquisition incident
- infected courier exposure
- field lab safety problem
- foreign intelligence discovery
- containment team death
- treatment breakthrough that can slow weaponization or reduce accident risk
- pressure from military leadership to rush deployment
- ethical dissent or sabotage in democratic countries
- accident that creates a local outbreak
- successful stabilization that lowers self-exposure risk
- final weaponization readiness event

## Weaponized deployment

Weaponized Black Death should be extremely dangerous. Deployment should use existing biowarfare delivery systems. It can target enemy states and apply weaponized exposure status.

Deployment effects should include:

- strong initial disease load in target state
- fast death pressure if target lacks preparation
- high spread pressure from the target
- condemnation increase for the attacker
- retaliation risk
- lab or stockpile accident risk for the attacker
- chance of blowback through ports, troops, or captured samples
- world threat contribution if the outbreak becomes large enough

The strongest counterplay should be preparation before the strike. A state with high medical capacity, surveillance, and containment law can reduce the initial effect and prevent runaway spread.

## Accident and blowback model

Weaponization should be risky for the user. Accident risks should scale with:

- stockpile size
- low containment safety
- project rushing choices
- bombing, sabotage, or occupation of biowarfare sites
- low stability
- high resistance in host states
- air raids on storage sites
- previous accident history

Accidents should create local outbreaks, Deaths entries, condemnation exposure when discovered, and possible political consequences.

## Ethical and diplomatic consequences

Weaponization should interact with condemnation and diplomacy.

- Democratic or lawful countries should face severe domestic cost or route blockers unless already radicalized by chaos.
- Fascist, extremist, or high-chaos routes can pursue the project more readily, but still face global condemnation.
- Countries known to deploy weaponized Black Death should receive embargo, isolation, or counterstrike risk through the existing condemnation system when that system is expanded.
- Countries hit by a weaponized attack should gain emergency containment options and retaliation paths.

## Cure versus weapon tradeoff

A country should not be able to freely maximize cure and weaponization without tradeoff. Sharing data helps cure progress and reduces global spread. Secrecy helps weaponization and increases accident risk. The player should decide whether Black Death is treated as a disease to defeat, a weapon to keep, or a crisis to exploit.

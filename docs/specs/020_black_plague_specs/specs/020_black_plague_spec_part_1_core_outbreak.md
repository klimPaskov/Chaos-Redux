# 020 Black Plague spec Part 1 - Core outbreak

## Event identity

Event 020 is a Minor Fire-Once event in the Diseases cluster with Severe member severity. The first firing creates a new Black Death strain in one mainland state. The event is state-based from the beginning. It does not select a continent, does not apply one generic temporary national idea, and does not copy ordinary bubonic plague content under another name.

The Black Death strain is a high-chaos disease identity that can start quietly, spread through state networks, kill real state population over time, feed the Deaths and Chaos systems, connect with shared biological warfare responses, and later mutate into nonhuman rat-country content.

## Player promise

The player should feel that the map has gained a living disease layer. The first outbreak is not a single modifier that times out. It is a state condition that can spread, relapse, move through ports, become contained, be studied, be weaponized, and eventually create political or nonhuman consequences.

The strongest design rule is that the Black Death must punish neglect. A prepared country can slow it, reduce deaths, and eventually clean infected states. A careless country can keep its economy moving for a while, but the disease should kill large portions of state population as infection severity rises.

## First outbreak selection

The first infected state should be a mainland state with enough population to make the outbreak matter. The weighted target should prefer neglected, crowded, low-capacity states.

Important selection factors:

| Factor | Weight direction | Design reason |
| --- | --- | --- |
| Mainland status | Strong positive | The first outbreak should begin on a land network so state spread can matter immediately. |
| High population | Strong positive | The disease needs victims and crowded conditions. |
| Low development | Strong positive | The user wanted a neglected region where response is late. |
| Poor infrastructure | Positive | Weak state capacity and bad logistics reduce response. |
| Poor disease protection | Strong positive | Prevention laws and medical preparation should matter before infection. |
| Port present | Moderate positive | Ports are useful later, but the first stage should still prefer land spread. |
| Active war or occupation | Positive | Disrupted movement and refugees make the outbreak worse. |
| High supply strain | Positive | Sick states should become harder to manage when logistics already fail. |
| Island-only geography | Strong negative | The first outbreak should not start on an isolated island. |
| Existing strong containment | Negative | Prepared states should be safer, though not immune. |

The first infected state should receive a Black Death state condition and become visible in the shared disease mapmode. The owner should gain access to the shared disease and biological warfare response surface if it was hidden.

## Disease state model

Every relevant state should be able to move through a compact set of statuses. These statuses are shared disease-board concepts, not a duplicate Black Plague-only category.

| Status | Meaning | Player-facing use |
| --- | --- | --- |
| Clean | No known infection or immediate exposure. | Normal state with possible prevention decisions only. |
| Prepared | No infection, but national or local prevention exists. | Surveillance, stockpiles, inspections, and local medical readiness. |
| Threatened | Adjacent to infection or exposed by port, troop route, war, or refugees. | Border controls, port checks, troop route restrictions, and emergency medical buildup. |
| Infected | Active Black Death disease load exists. | Quarantine, army cordon, hospitals, treatment, cleanup crews, and local movement restrictions. |
| Contained | Infection exists but spread has been suppressed. | Maintain cordon, controlled reopening, treatment continuation, and relapse monitoring. |
| Recovering | Cure and cleanup have reduced disease load. | Restoration, return of supply, population recovery support, and final inspections. |
| Cured | Disease load is removed from active state tracking. | Optional prevention and recovery actions remain for a short period. |
| Weaponized | State was hit by a weaponized payload or holds weaponized sample exposure. | High-risk containment, evidence, condemnation, and retaliation hooks. |
| Rat-held | A rat nation controls the state or has turned it into a rat warren. | Human containment is mostly unavailable, population death continues, and military response becomes the main answer. |

## Black Death state variables

The spec should keep values dynamic. Final implementation names can differ, but the design needs these concepts:

| Value | Stored on | Purpose |
| --- | --- | --- |
| Disease load | State | The current intensity of infection. Deaths and spread scale from this. |
| Spread pressure | State | How likely the state is to infect neighbors or ports. |
| Death pressure | State | The current death output after containment and medical reductions. |
| Containment strength | State and owner | Local and national suppression power. |
| Medical capacity | Owner and state | Treatment strength, hospital capacity, and cure support. |
| Rodent pressure | State | Rat and flea reservoir strength, later used by rat nation emergence. |
| Panic pressure | Owner and state | Stability, compliance, resistance, refugee movement, and underreaction risk. |
| Cure progress | Owner or coalition | The long-term progress toward suppressing Black Death severity. |
| Weaponized exposure | State | Marks states struck by an intentional payload or exposed through accidents. |
| Rat warren pressure | State | Tracks Evolution III emergence risk and rat unit growth. |

The player does not need every raw value on screen. The shared disease UI should expose readable summaries: infection severity, spread risk, deaths trend, containment status, cure progress, and local response burden.

## Opening stage behavior

The first outbreak should begin with a local report, not a global apocalypse announcement. Deaths should be noticeable but not instantly decisive. The danger grows because the state remains infected and the owner must decide how much harm to accept.

Opening behavior:

- One mainland state becomes infected.
- Initial disease load is moderate, with a low first death tick.
- Nearby states become threatened.
- The owner sees shared disease responses tied to the infected state.
- Nearby countries can see prevention decisions if borders, ports, or troop routes expose them.
- The mapmode highlights the infected state and threatened neighbors.
- The first report should focus on sickness, missing workers, empty streets, sick animals, sudden burials, and fear spreading through transport routes.

The opening should avoid direct world-end language. The player should understand the risk from the state condition and spread pattern.

## Death model

Black Death deaths must reduce real state population over time and feed the shared Deaths and Chaos systems. The numbers should be high enough to matter. A state ignored for a long period can lose a large share of its population.

Death output should scale from:

- current disease load
- state population
- population density proxy
- infrastructure and development
- containment strength
- medical capacity
- cure progress
- occupation or war disruption
- supply strain
- open borders and troop movement
- evolution stage
- whether the state is weaponized or rat-held

Death ticks should start lower, then rise as infection severity rises. The design should avoid an opening instant massacre, but it must allow severe loss if countries keep delaying.

Suggested death bands for implementation tuning:

| Band | State condition | Design outcome |
| --- | --- | --- |
| Early infection | Low disease load and no mutation | Local deaths are visible but still controllable. |
| Established infection | Rising disease load and weak response | State population loss becomes strategically important. |
| Crisis infection | High disease load with poor containment | The state can lose huge population over months. |
| Collapse infection | Uncontrolled infection in war, occupation, or panic | The state becomes a mass-death source and spread engine. |
| Rat-held infection | Rat nation controls the state | Deaths continue unless humans retake and clear the state. |

## Strategic tradeoff

The event should never become an obvious list of cure buttons. The response should hurt.

Underreaction keeps factories, movement, ports, borders, and army logistics working for longer. It also lets disease load grow, creates more death pressure, and makes the state a spread source.

Overreaction lowers disease pressure. It damages the economy, supply, stability, war support, local compliance, relations, trade, and military readiness. A player should sometimes accept short-term spread risk because the war situation makes full lockdown impossible.

## Country response tiers

Countries should enter different response states based on geography and exposure.

| Country position | Main choices |
| --- | --- |
| No nearby infection | Surveillance, medical stockpiles, early warning, and port hygiene. |
| Bordering threatened state | Border checks, troop route restrictions, border quarantine, and refugee screening. |
| Has infected state | Quarantine, lockdown, treatment, army cordon, emergency hospitals, cleanup crews, and cure development. |
| Has contained state | Maintain containment, controlled reopening, relapse monitoring, and recovery funding. |
| Has cured state | Restore population recovery, rebuild medical networks, and retain optional prevention. |
| Has weaponized exposure | Emergency secrecy, evidence handling, condemnation risk, countermeasure surge, and retaliation risk. |
| Borders rat-held state | Military quarantine, fortified border, extermination operations, and emergency evacuation. |

## Event-log and detail direction

Event Details should describe the disease premise and state-based crisis. It should not list mechanical effects, death formulas, or hidden rat outcomes.

Event-log direction:

- Entry row should name the first infected state and owner when available.
- Evolution rows should record the actual evolution track and stage, not ordinary spread stages.
- Rat nation emergence should record the first rat country actor if one exists.
- King of Rats formation should record the new king country actor.
- World-end row should record the King of Rats scenario.

## Localisation direction

The planning spec is direction-only for final text. Implementation must write final localisation from the design.

Event text should focus on the visible fear: sickness in streets, sudden loss of workers, dead animals, sealed neighborhoods, rural panic, port gossip, and the state changing in ways the public cannot explain. Do not write final text that calls the outbreak a warning or explains the future rat route.

Options should communicate the owner’s first stance:

- practical containment tone for a responsible government
- cynical minimization tone for an underreacting government
- harsh emergency tone for lockdowns
- research and sample direction for biological warfare countries
- fear-driven local response for weak countries

The implementation agent should research any cultural remarks before using them. No unresearched quote, slogan, song fragment, or final option line is provided here.

# Event 19 Infantry Spawn
## Part 1: Core identity, player promise, and crisis model

## Canonical identity

- **Event ID:** `19`
- **Event name:** Infantry Spawn
- **Classification:** Minor Repeatable
- **Catalog status at planning start:** To Be Reworked
- **Working slug:** `infantry_spawn`
- **Request label:** `017# Infantry Spawn`, retained only as request metadata

The event remains a global repeatable incident. Its opening is simple enough to understand immediately: countries discover new formations across territory they control. The rework makes the consequences depend on geography, war state, military institutions, available equipment, prior event firings, evolution state, and how each country handles the formations afterward.

The event is not an equipment gift and it is not a one-click reinforcement button. It is a sudden claim on the state. Barracks, depots, railways, local officials, officers, recruits, animals, vehicles, ammunition, and food are drawn into an army that did not exist the day before. Some formations arrive with coherent staff work. Others arrive with the wrong guns, no transport, contradictory orders, or a commander who already regards the new troops as a personal following.

## Player promise

The system should make the player ask five recurring questions.

1. **Where did the formations appear?**
   The territorial pattern matters. Capital districts, industrial states, ports, rail junctions, front-line regions, mountains, deserts, islands, and remote colonies should produce different burdens and formation families.

2. **What actually appeared?**
   The answer ranges from weak local rifle cadres to support-heavy reserve formations, mounted patrols, advanced armored groups, mechanically absurd template lots, and eventually registered Chaos unit families.

3. **Can the country equip and command them?**
   A division on the map is not automatically useful. The player must solve shortages, training, officer assignment, supply congestion, incompatible equipment, and command ownership.

4. **Who benefits from the disorder?**
   At higher evolution, possessed or otherwise frightening claimant generals use event formations as a political base. Their requests can be useful, coercive, or openly separatist.

5. **How far is the country willing to gamble?**
   The decision layer lets a country request additional random formations. Repeated requests can produce extraordinary military value, but they increase congestion, claimant power, and anomalous saturation.

The strongest play should come from managing uncertainty rather than rerolling until a perfect division appears.

## Event identity across repeated firings

Each firing creates a **muster generation**. A generation is a country-scoped set of event formations, liabilities, and records created by one global firing. A country can still be resolving one generation when the event fires again.

Repeated generations create campaign memory:

- A country that integrated earlier formations efficiently begins with better records and higher institutional control.
- A country that disbanded formations through a legitimate demobilization process begins with less congestion but may have weaker reserve depth.
- A country that repeatedly ignored unprocessed formations receives stronger penalties and worse future quality distributions.
- A country that empowered claimant generals carries those networks into later generations.
- A country that reached Evolution IV retains its anomalous registry and family-specific containment history.

The event can therefore repeat without each firing feeling identical. The same country may welcome one wartime muster, fear the next peacetime burden, and later refuse to risk another formation draw while a claimant controls several army districts.

## Ordinary lifecycle

The ordinary lifecycle is not an evolution track. It is the expected handling sequence for every firing.

### Stage A: Manifestation

The global event selects eligible controlled states and creates one or more **formation lots** for each affected country. A formation lot is a group of divisions that share a generated template, readiness profile, equipment condition, origin pattern, and integration status.

The player sees the territorial spread and a concise summary of the new burden. The text direction should focus on people, trains, animals, vehicles, depot queues, improvised camps, and officers arriving or being found in place. It should not present the event as a changed map or a mechanical reward screen.

### Stage B: Registration

The country receives a short audit period. During this period, the new formations are event-owned and cannot be freely converted into ordinary equipment profit.

The player identifies:

- coherent lots suitable for rapid field integration
- weak lots suitable for garrison, retraining, or controlled demobilization
- supply-heavy lots that need rail or depot work
- formations whose equipment cannot be replenished normally
- formations already attached to a claimant general
- anomalous lots that require family-specific handling

The AI performs the same classification through weights and scripted effects rather than a human-only interface.

### Stage C: Disposition

The country chooses how to deal with each active lot or group of lots.

Possible dispositions include:

- integrate into the field army
- assign to territorial defense
- merge compatible lots into a standardized template
- retrain through a timed mission
- quarantine or isolate anomalous formations
- place under a claimant general
- break claimant influence through reassignment
- demobilize under state supervision
- gamble on another requested formation

The choice changes current strength and future event quality.

### Stage D: Closeout

A generation closes when its active lots are integrated, demobilized, revolted, destroyed, or transferred into a persistent anomalous system. Closeout removes temporary clutter and records the generation outcome.

A country does not need to resolve every individual division manually. The UI and decision system work at lot, district, or policy level. The event should create strategic choices rather than an administrative chore for every unit.

### Stacked muster state

When another global firing reaches a country with unresolved lots, the country enters **stacked muster**.

Stacked muster should:

- raise Army Congestion sharply
- reduce the share of coherent new templates
- increase claimant recruitment opportunities
- increase the chance that advanced or strange equipment is distributed incorrectly
- shorten the safe audit period
- unlock emergency consolidation actions
- increase AI reluctance to request extra formations unless at war or desperate

A well-managed country can avoid stacked muster most of the time. A deliberately reckless player can use it as a high-risk route to enormous but unstable force growth.

## Core visible values

The system uses four main values. They unlock gradually so the player is not shown irrelevant complexity at baseline.

### Muster Control

**Range:** 0 to 100

Muster Control measures the state’s ability to register, assign, standardize, supply, and demobilize event formations.

It rises through:

- successful audit missions
- adequate officer capacity
- standardization decisions
- controlled demobilization
- rail and depot preparation
- integrating lots before the audit period expires
- defeating or peacefully resolving a claimant crisis
- maintaining stable command during war

It falls through:

- stacked muster
- unresolved equipment debt
- supply collapse
- rushed integration
- mass template switching
- claimant concessions that bypass the normal chain of command
- failed retraining missions
- revolt
- uncontrolled anomalous recruitment

High Muster Control improves coherent formation chances and reduces revolt risk. Low Muster Control produces stronger penalties and shifts later random generation toward strained, absurd, and catastrophic outcomes.

Muster Control should be visible in the decision category from the first firing.

### Army Congestion

**Range:** 0 to 100

Army Congestion measures the burden created by too many formations competing for command, supply, rail movement, training grounds, and equipment.

It rises through:

- number of event divisions relative to country size
- units per selected state
- supply-heavy templates
- low infrastructure or train availability
- overlapping front redeployments
- repeated on-demand spawns
- unresolved lots
- hostile claimant assignments
- anomalous families with special sustainment needs

It falls through:

- integration and consolidation
- controlled demobilization
- completing supply district missions
- assigning units to appropriate terrain or garrison roles
- constructing or repairing rail and supply capacity
- ending stacked muster

Army Congestion changes available incidents, AI behavior, claimant demands, and template outcome weights in addition to its direct penalties. At extreme levels, new formations can appear without usable deployment orders, block rail movement, or become attached to whichever general feeds them first.

### Claimant Influence

**Range:** 0 to 100 per active claimant

Claimant Influence appears at Evolution III. It measures how much control a possessed general or frightening military claimant has over event formations, officers, depots, and local political networks.

The system normally tracks up to three active claimants for a country. Additional generated personalities should enter as officers, subordinate rivals, or replacements rather than creating an unreadable list.

Claimant Influence rises through:

- granting command districts
- assigning event formations
- meeting equipment demands
- allowing independent recruitment
- accepting a political or military office
- military victories by claimant-controlled lots
- high Army Congestion
- low stability or low Muster Control

It falls through:

- reassignment missions that succeed
- removing loyal formations from the claimant’s district
- public military failure
- negotiated retirement
- counter-command networks
- claimant defeat or death
- stable integration of their formations into ordinary command

The value should be visible only when a claimant has entered play.

### Anomalous Saturation

**Range:** 0 to 100

Anomalous Saturation appears at Evolution IV. It measures the share and operational intensity of registered Chaos unit families within the country’s event formations.

It rises through:

- spawning or training eligible Chaos units
- using family abilities
- assigning anomalous formations to claimants
- ignoring containment or sustainment requirements
- placing incompatible families in one formation lot
- losses that trigger family-specific spread or replacement behavior
- repeated on-demand anomalous draws

It falls through:

- quarantine and cantonment
- family-specific binding or containment missions
- controlled deployment limits
- destroying or demobilizing eligible trainable units where appropriate
- defeating derivative revolt networks
- maintaining high Muster Control

Anomalous Saturation affects derivative country risk and the strength of any revolt. It never turns this event into the parent Zombie Outbreak, Death, golem, or future parent event chain.

## Country pressure profile

The event must scale by country rather than use one global package.

Each country receives a pressure profile based on:

- controlled state count
- total and recruitable population
- industrial capacity
- rail, supply hub, port, and train availability
- number of existing divisions
- average supply status
- current war state
- enemy proximity and front pressure
- stability and war support
- officer and command capacity proxies
- equipment stockpiles
- current evolution state
- unresolved generations
- existing claimant or anomalous pressure

The profile determines state coverage, units per selected state, readiness, equipment share, template family weights, audit duration, and AI response.

Large countries receive more total units, but each additional controlled state contributes less to the number of selected spawn states. Small countries receive high territorial coverage but cannot obtain the same absolute force size as continental empires.

## War and peace asymmetry

Countries at war may receive stronger formations because the event draws on active mobilization networks, captured equipment, emergency staffs, and existing front-line demand. This advantage must carry a real burden.

At-war countries should tend toward:

- higher readiness
- more equipment on arrival
- heavier support and combat formations
- more front-adjacent spawn states
- shorter audit periods
- greater Army Congestion
- stronger claimant leverage
- higher immediate supply strain

Countries at peace should tend toward:

- weaker and more irregular lots
- longer audit periods
- better demobilization options
- lower initial congestion
- more political resistance to permanent mobilization
- stronger opportunity to standardize before war

The design should not make peace strictly inferior. A peaceful country can turn a weak but manageable muster into a standardized reserve system. A country already fighting for survival can gain immediate force at the cost of command collapse.

## Immediate effects and temporary penalties

The event should create strong, readable consequences without applying identical penalties to every country.

Possible temporary national or dynamic effects include:

- supply allocation strain
- training ground saturation
- command docket confusion
- officer reassignment burden
- reserve equipment requisition
- transport competition
- local requisition anger
- emergency recruitment enthusiasm

These effects should be generated from the country pressure profile. A small country receiving two weak cadres should not suffer the same disruption as a large country receiving dozens of armored, mounted, and irregular lots.

The effects need real gameplay weight. They should alter supply, training, reinforcement, organization, mobilization, factory burden, or command behavior enough to influence decisions. They should not be a collection of tiny decorative modifiers.

## Event information direction

### Entry popup

The player-facing entry should describe simultaneous military formation across the country. The viewpoint should be national but grounded in local scenes. It can mention newly occupied barracks, schoolyards used as drill grounds, rail sidings full of recruits, mounted columns, incompatible uniforms, unrequested artillery, and officers whose orders do not match the government’s records.

The text should preserve uncertainty about origin. It should not explain the hidden randomization tables or future evolutions.

### Event Details direction

Event Details should describe the premise and recurring pattern. It should explain that new formations appear across controlled territory and differ in quality, organization, and composition. It should not list modifiers, exact ranges, evolution outcomes, claimant revolt mechanics, or anomalous country possibilities.

### Event log direction

The event history row represents the global manifestation. It does not require one actor flag because every valid country can be affected. Country-specific claimant incidents and derivative revolts belong in follow-up history events.

### Option direction

The entry response should be a short reaction to an impossible administrative and military burden. Minor-event absurdity is appropriate, but the line should not make mass coercion, child soldiers, or historical atrocities into a joke. Final wording must be written during implementation.

## Repeatability rules

The event remains repeatable under the standard repeatable event system. Its local mechanics need additional safeguards:

- A country with no eligible controlled state receives no units and no fake generation.
- A derivative revolt country or other special nonhuman country is still evaluated. It receives a registry-aware compatible package or a deliberately defined auxiliary package rather than a silent exclusion.
- A country currently undergoing an impossible tag transition, annexation cleanup, or terminal parent-event conversion should defer local processing safely.
- The event must not duplicate divisions when a state changes controller during the generation effect.
- State selection and lot creation must be deterministic within one firing once random rolls are made.
- A country cannot repeatedly reload or reopen the UI to reroll a generated lot.
- On-demand draws consume their cost before the generated result is revealed.

## Success states

The event does not have one victory condition. A country can succeed in several ways.

### Professional integration

The country turns most useful lots into standardized formations, resolves equipment debt, keeps congestion low, and prevents claimants from controlling autonomous forces.

### Territorial reserve doctrine

The country accepts weaker local formations and uses them as garrisons, border guards, or terrain-specific reserves without overloading the field army.

### Controlled gamble

The country requests additional random formations, receives some extraordinary results, and contains the resulting command and supply risk.

### Political accommodation

The country grants a claimant limited authority, gains military value, and prevents the arrangement from becoming a revolt or takeover.

### Anomalous containment

The country uses registered Chaos units while keeping saturation below derivative revolt thresholds and respecting family-specific training or spawn rules.

## Failure states

### Administrative failure

Unresolved formations remain understrength, drain supply, and worsen future generation quality.

### Command capture

A claimant gains enough influence to control several lots and dictate national policy.

### Military revolt

Claimant-controlled or anomalous formations revolt with a coherent regional base or attempt a one-state takeover.

### Derivative secession

A registered Chaos family forms an independent, aggressive, weaker derivative country with its own identity and limited mechanics.

### Self-created front collapse

A country at war accepts too many divisions, overloads supply, and weakens the existing front despite having more units on paper.

## Design limits

The following boundaries protect the event’s identity and prevent scope drift.

- The event does not provide a direct world-end scenario.
- The event does not copy the full Zombie Outbreak, Death, golem, or future parent event mechanics.
- The event does not create a unique focus tree for every ordinary country.
- The event does not require individual decisions for every spawned division.
- The event does not animate all 20 claimant army/muster identity scenes held in the fixed portrait slots.
- The event does not unlock advanced zombie variants through Evolution IV.
- The event does not allow all future Chaos units automatically. Future unit families require explicit registry opt-in.
- The event does not use one-member event clusters.
- The event does not create free equipment through disbanding, template conversion, or repeated requests.
- The event does not turn every claimant dispute into a civil war. Negotiation, takeover, reassignment, retirement, and collapse are valid outcomes.

These limits leave room for a deep system while preventing it from swallowing the parent events or the entire military game.

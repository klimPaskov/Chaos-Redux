# Event 20 Black Plague Specification, Part 3

## Countermeasures, advanced spread, biological warfare, and cross-system integration

All labels in this file are working labels, not final localisation.

## Countermeasure philosophy

The Black Plague countermeasure is a package of diagnosis, treatment, prevention, production, and cleanup knowledge. The interface can call it a cure in player-facing shorthand, but the mechanic must not erase active disease instantly.

A completed countermeasure does four things.

- reduces mortality pressure
- reduces outgoing and incoming spread
- improves containment and treatment efficiency
- allows a sufficiently suppressed state to begin final cleanup

A completed countermeasure does not set disease load to zero, remove an active state modifier, restore lost population, or prevent weaponized reinfection.

## Country countermeasure progress

Each country can develop its own Black Plague countermeasure progress from 0 to 100. A shared world knowledge pool represents published or exchanged findings. Countries can receive a fraction of global knowledge through alliances, aid, espionage, conferences, or deliberate sharing.

### Progress stages

| Progress band | Working stage role | Gameplay change |
| --- | --- | --- |
| 0 to 19 | Recognition and sampling | Earlier diagnosis, minimal death reduction |
| 20 to 39 | Treatment protocol | Meaningful treatment coverage improvement |
| 40 to 59 | Emergency production | Medicine and hospital actions become cheaper and stronger |
| 60 to 79 | Transmission control | Spread and relapse reduction improves |
| 80 to 99 | Cleanup doctrine | Contained states can enter Recovery more reliably |
| 100 | Complete countermeasure | Final cleanup can begin after local thresholds are met |

The final names require implementation localisation. The stages should describe visible medical progress and avoid modern clinical jargon that breaks the period tone.

### Progress sources

- studying cases in an owned infected state
- operating emergency hospitals
- maintaining accurate surveillance and death records
- obtaining samples through an ally or subject
- receiving foreign research exchange
- stealing research from another country
- successful special-project iterations that favor safety and treatment
- rare event interaction with Event 163 Doctor Wu when that event is active and compatible
- liberation and cleanup of a rat-controlled state
- capturing a foreign biowarfare facility that has Black Plague research

### Progress penalties

- state collapse and loss of hospital access
- destroying records to hide a crisis
- redirecting the same scientific capacity into weaponization
- lab accidents
- low stability and scientist loss
- blockade or supply failure
- repeated mutation after Evolution I

### Dynamic research pace

A well-funded country with active cases, safe facilities, strong medical capacity, and foreign cooperation should reach full countermeasure status in roughly six to twelve months. A country at war with weak capacity may need one to two years. A country without samples or cooperation should progress very slowly until it gains direct evidence.

The pace must not be a single timer. It should react to research resources, cases, safety, shared knowledge, evolution stage, and political choices.

## Countermeasure milestones

Progress milestones should create visible changes rather than tiny bonuses.

### First diagnosis milestone

- reveals Incubating states earlier
- improves the accuracy of disease load and mortality forecasts
- lowers false quarantine risk

### Treatment milestone

- emergency hospital and treatment reserve actions gain a strong mortality benefit
- state treatment coverage can exceed its previous cap
- foreign medical aid becomes more effective

### Production milestone

- medical reserve can be produced more efficiently
- large countries can support several infected states without exhausting all reserves
- field hospital construction time drops

### Transmission milestone

- quarantine and port inspection actions receive stronger spread reduction
- controlled reopening becomes safer
- military decontamination reduces troop-route spread

### Cleanup milestone

- Contained states can enter Recovery when disease load and exposure are low
- burial, sanitation, and residual tracing actions gain stronger load reduction
- relapse risk falls faster

### Complete countermeasure

- enables final state cleanup
- reduces ordinary Black Plague mortality to a manageable level when treatment reaches the population
- lowers but does not eliminate Evolution I severity
- creates a national prevention memory after eradication

## Global knowledge and diplomacy

Countries should make strategic choices about knowledge.

### Publish findings

Shares a large portion of progress with allies, faction members, and countries that accept the exchange. It reduces global deaths and can improve relations. It also makes weaponization easier for hostile biowarfare powers.

### Restricted alliance exchange

Shares progress with a chosen group at a smaller diplomatic risk. It requires relations, access, or faction membership.

### Hoard the protocol

Protects military advantage and slows foreign weaponization, but increases international suspicion and allows neighboring deaths to continue.

### Steal foreign progress

Uses intelligence resources and creates diplomatic exposure. Failure can reveal a domestic weaponization program or sabotage the research effort.

### International medical mission

Creates a time-limited cooperative program. Countries contribute industry, supplies, or scientists. The global knowledge pool grows while the mission succeeds.

The system should use existing diplomacy, intelligence, and disease mechanics where available instead of creating a full new international organization.

## Event 163 Doctor Wu connection

Event 163 is cataloged as a mysterious doctor who cures every disease. The Black Plague should support a rare, high-value connection without allowing an instant map cleanup.

When Doctor Wu is active and reaches an eligible infected country, the event can:

- grant a large countermeasure progress increase
- reveal hidden Incubating states in the host country
- improve treatment coverage in one selected Severe Crisis state
- unlock an accelerated cleanup protocol
- create a foreign request chain as other countries seek access

Doctor Wu cannot remove the Black Plague modifier from every state in one effect. Local containment and cleanup remain required. This preserves the identity of both events while respecting the user's rule that the cure is not instantaneous.

## Spread engine

The spread engine evaluates an infected source, one or more valid routes, and target protection. It should operate from registered infected and threatened state lists rather than scanning every state every day.

### Spread pulse pacing

- state disease and death updates can use a daily or several-day cadence when required for smooth mortality
- outgoing spread should normally evaluate on a weekly or similarly batched pulse
- long-distance port jumps after Evolution II should use a slower pulse than land adjacency
- major movement events, weapon deployment, rat occupation, and loss of containment can trigger immediate targeted exposure updates

The implementation should avoid an unrestricted whole-world on-action loop. The user requested dynamic spread, so event-owned scheduled processing is appropriate. The exact engine-safe pattern must be chosen after reading the live repository and vanilla documentation.

## Land spread scoring

A source state emits a route score based on:

- source disease load
- source status
- source population density
- uncontrolled movement
- war and occupation
- rat control
- Evolution I severity

A target resists with:

- preparedness
- local containment
- border controls
- treatment and surveillance
- natural geographic separation
- active monitoring memory

### Route families

#### Direct adjacency

The default and most common route. It is strongest when a border is open, the target is densely populated, and the source is Severe Crisis or Collapsed.

#### Same-country transport

Railways, major supply lines, and strategic redeployment can expose nonadjacent states within the same country. The route is weighted toward important transport hubs and states receiving divisions.

#### Cross-border troop movement

An active front, occupation transfer, volunteer return, or expeditionary route can move the disease between countries. Protective equipment and route restrictions reduce risk.

#### Refugee and migration movement

When a real migration or refugee route exists, it contributes exposure. The Black Plague should not create a duplicate migration map if another Chaos Redux system already provides one.

#### Diplomatic and trade access

Open borders, faction supply access, and intense trade can provide small background exposure. This should not be strong enough to make every trading partner immediately infected.

## Evolution II overseas spread

Evolution II unlocks sea and long-range port transmission. It does not make every island automatically infected.

### Source requirements

An overseas jump normally needs:

- an Infected, Severe Crisis, Collapsed, or Rat-Controlled coastal state
- an active port or sea access route
- sufficient source disease load
- a valid destination port connected by trade, convoy, naval access, faction supply, or scripted transport activity

### Destination scoring

| Factor | Effect |
| --- | --- |
| Large port | strong increase |
| High population | strong increase |
| Major convoy activity | moderate increase |
| Troops arriving from source region | strong increase |
| Weak port inspections | strong increase |
| Strong preparedness | decrease |
| Active travel restriction | decrease |
| Island isolation with closed port | strong decrease |
| Existing threatened status | increase |

### Port jump stages

A successful jump should usually create Threatened or Incubating status rather than immediate Severe Crisis. Weaponized cargo, a Rat King focus, or an evolved collapse route can begin at a higher load.

### Sea route visibility

Countries with surveillance should see likely source and destination links in the disease interface. Others see only the destination outbreak after recognition. The UI should not reveal secret enemy deployment before attribution.

## Air, convoy, and strategic delivery

Ordinary civilian air travel is limited in the period and should not become the main natural spread path. Air transport can still contribute through military transport, evacuation, or a biological strike when the existing system provides a real route.

Convoys and port traffic are the main overseas mechanism. The player should be able to reduce risk through inspections and closures, but complete isolation should damage trade and supply.

## Biological warfare registration

Once Event 20 fires, the Black Plague becomes a valid disease object for the existing biological warfare system.

Registration should provide:

- disease identity and severity class
- natural spread behavior
- mortality curve reference
- countermeasure progress reference
- special-project sample eligibility
- delivery compatibility
- accident behavior
- condemnation and attribution behavior
- mapmode and UI status
- exclusion of nonhuman countries from ordinary disease harm

The ordinary bubonic plague disease remains separate. A country can know, cure, stockpile, or deploy one without automatically receiving the same status for the Black Plague.

## Sample access

A country can begin serious countermeasure or weaponization work only after gaining valid access.

### Valid access paths

- own or control an infected state
- receive an approved sample from an ally or subject
- capture an infected laboratory or biowarfare facility
- steal samples through intelligence
- recover material after a foreign biological strike
- obtain samples from a rat-controlled state through a successful military operation

### Sample risks

- transport accident
- lab leak
- intelligence interception
- sample degradation that delays work
- political scandal
- foreign condemnation when the purpose appears offensive

Sample access should be a reusable shared disease mechanism.

## Long weaponization special project

The Black Plague weaponization route uses the existing biological warfare special-project structure. It must be long, costly, iterative, and dangerous.

### Project role

The project converts medical and military knowledge into a stable deployable payload compatible with existing biowarfare delivery systems. The specification intentionally stays at a high level and must not describe real pathogen engineering procedures.

### Entry requirements

- Event 20 has fired and the disease exists in the world knowledge registry
- country has biological warfare capability
- country has valid sample access
- country has a suitable special-project facility
- country is not prohibited by its own route or law
- country can commit research and industrial capacity

### Project duration target

A safety-first project should normally require eighteen to thirty months. A reckless high-chaos country can compress the schedule toward twelve to eighteen months by accepting sharply higher accident, exposure, and condemnation risk. Severe disruption can make the project take longer than thirty months.

The project must not be a single button or one event option.

### Project phases

#### Phase 1: Acquisition and containment

The country secures samples, validates provenance, and establishes a secure facility. Failure can destroy the sample or cause an early leak.

#### Phase 2: Strain characterization

Scientists determine how the Black Plague differs from ordinary plague and what countermeasures affect it. Choices can favor treatment knowledge or offensive reliability.

#### Phase 3: Safe handling and production control

The project establishes procedures that limit domestic exposure. Skipping safeguards saves time while increasing accident risk.

#### Phase 4: Delivery compatibility

The project adapts the payload to the existing biological delivery system at an abstract level. No real delivery instructions should appear in text or documentation.

#### Phase 5: Stockpile and command control

The country decides who can authorize deployment, how much material is stored, and what happens during retreat or capitulation.

#### Phase 6: Final certification

The project becomes deployable, aborts into a defensive program, or suffers a major failure.

## Unique project iterations

The project should draw from a large pool of distinct iteration events. These are narrative and strategic choices, not repeated progress bars.

| Iteration role | Choice tension | Possible consequences |
| --- | --- | --- |
| Contaminated courier | destroy, quarantine, or conceal | time loss, leak risk, exposure risk |
| Disputed sample provenance | verify or proceed | reliability versus schedule |
| Facility power failure | halt work or use emergency systems | cost, delay, accident risk |
| Exhausted laboratory staff | rotate personnel or force overtime | progress versus safety and scientist loss |
| Medical team conflict | prioritize cure data or offensive data | countermeasure gain versus weapon progress |
| Security breach | purge staff, investigate, or move facility | stability, time, intelligence exposure |
| Foreign scientist offer | accept, refuse, or secretly recruit | progress, espionage risk, relations |
| Containment material shortage | divert industry or improvise | factory burden versus accident risk |
| Animal-vector panic | suspend work or continue under secrecy | public order, delay, concealment |
| Rival intelligence theft | counterspy or feed false data | intelligence cost, foreign project delay, exposure |
| Hospital requests samples | share or deny | cure progress versus project secrecy |
| Military demands a test | refuse, simulate, or authorize a controlled fictional trial | command relations, condemnation, accident risk |
| Civilian outbreak near facility | reveal, contain, or cover up | domestic deaths, stability, project exposure |
| Stockpile seal failure | destroy batch or risk retention | project setback versus future accident risk |
| Scientists seek an exit | permit transfer, detain, or compromise | safety, research, political cost |
| Command authorization dispute | civilian, military, or leader control | deployment speed, coup pressure, accident risk |
| International inspection threat | suspend, relocate, or deceive | delay, diplomatic cost, exposure |
| Final safety review | certify, delay, or redirect to defense | unlock, safer stockpile, defensive conversion |

The final implementation can add more iterations, but it should not reduce the project below this level of variety.

## Project choices and branches

### Safety-first branch

- slower progress
- lower accident risk
- larger countermeasure knowledge gain
- more expensive facility requirements
- lower chance of public exposure

### Military acceleration branch

- faster progress
- higher accident and stockpile risk
- greater condemnation if discovered
- weaker defensive benefits
- more likely scientist conflict

### Dual-use branch

- balanced progress
- develops both countermeasure and deployment knowledge
- highest total industrial cost
- intelligence exposure from a larger program

### Defensive conversion

At several milestones, the country can abandon weaponization and redirect the facility into countermeasures. This preserves some progress and reduces future condemnation. It does not erase accidents or earlier exposure.

## Weaponized stockpile

A completed project unlocks a Black Plague stockpile within the existing biowarfare inventory.

The stockpile should be dangerous to hold.

### Risk factors

- stockpile size
- containment safety level
- war damage and bombing
- low stability
- retreat or capitulation
- scientist purges
- reckless project choices
- active sabotage

### Accident outcomes

- local Incubating state near facility
- immediate Infected state after severe failure
- scientist death and project setback
- public exposure and condemnation
- foreign intelligence gain
- stockpile destruction

The highest containment safety level can reduce ordinary accident risk heavily. It should not remove risk from deliberate reckless choices, enemy action, or doomsday release.

## Deployment through existing delivery systems

A completed project unlocks Black Plague as a payload for existing biological strikes, raids, and approved delivery systems. It does not add a separate one-off event button.

### Deployment effects

A successful deployment:

- seeds the target state at a high Incubating or Infected load
- records weaponized provenance when attribution is known
- creates immediate Threatened exposure in strongly connected states
- applies civilian deaths only through the normal ongoing disease ticks
- raises condemnation sharply
- increases retaliation pressure
- can activate the world-threat source at a lower global infection threshold

A failed or partial deployment can:

- consume stockpile with little effect
- expose the attacker
- infect a friendly staging state
- create an accident in transit
- seed a lower target load

### Attribution

Attribution depends on intelligence, delivery visibility, captured agents, project exposure, and prior condemnation. A country may avoid immediate blame, but deliberate weaponized provenance remains internally tracked for later discovery.

### International consequences

- severe condemnation increase
- relations collapse with threatened countries
- countermeasure sharing among rivals
- retaliation and preemptive strike pressure
- possible war goals or sanctions through existing systems
- increased foreign intelligence targeting

## Biological doomsday interaction

If the existing biological doomsday protocol allows a country near capitulation to release all stockpiles, Black Plague payloads join that system after weaponization.

The release can seed several controlled states and consume the stockpile. It should carry extreme domestic mortality, condemnation, and rat-emergence risk. The decision must clearly warn that the plague persists after the country falls.

No special duplicate Black Plague doomsday decision is created.

## Cure and weaponization conflict

Medical and offensive work compete for samples, scientists, facilities, and production.

A country can pursue both, but:

- project costs rise
- countermeasure progress slows unless extra capacity is committed
- accident risk grows
- foreign aid partners may withdraw
- public exposure creates larger stability and condemnation effects

A country that publishes its cure findings can still weaponize later, but other countries will be better prepared.

## Air cleanliness integration

Every active outbreak state contributes to the shared air cleanliness or contamination system using the established low, base, and high intensity bands.

Suggested mapping:

- Threatened and Incubating do not add contamination until active disease is confirmed
- Infected contributes the base outbreak amount
- Severe Crisis and Collapsed contribute the high outbreak amount
- Contained contributes the low amount
- Recovery contributes the low amount until disease load reaches zero
- Rat-Controlled states contribute at least the high amount

The Black Plague should not invent a parallel global contamination meter.

## Deaths and Chaos Meter integration

Black Plague civilian deaths flow through the shared death tracker. The established million-death conversion then changes Chaos automatically.

The event also uses event-specific cumulative deaths for rat and Rat King thresholds. This secondary counter must read from the same attributed death effects and must not generate a second population reduction.

## Condemnation integration

Natural outbreaks do not create condemnation. Condemnation rises from:

- deliberate weapon deployment
- reckless lab accidents that are exposed
- doomsday release
- attacks on relief missions
- concealment when it causes cross-border spread and evidence becomes public

Ordinary quarantine severity can create opinion and stability damage, but it should not use the unconventional warfare condemnation value unless the country has actually used or mishandled a weapon.

## World-threat integration

The shared world-threat source for Black Plague activates when the crisis becomes existential. Suitable triggers include:

- Evolution III is active and a Rat Nation exists
- a defined share of the world population lives in infected states
- a defined global death threshold is reached
- the Rat King exists

The source clears only when no rat country exists, no Severe Crisis or Collapsed state remains, and global infection has fallen below the threat threshold for a sustained period.

This source contributes to the existing `world_in_threat` framework. It must not create a parallel global cooperation flag.

## Other event connections

### Event 41 Disease in Divisions

When Event 41 is reworked, active frontline disease should increase troop-route exposure, division attrition, and military quarantine needs. Until then, Event 20 should expose a clean shared hook rather than hardcoding assumptions about Event 41.

### Event 118 Plague of Locusts

A future locust crisis can reduce food and state capacity, increasing mortality and containment burden. Event 20 should not assume Event 118 is implemented.

### Event 149 Immigration

A future migration crisis can provide real movement routes and receiving states. Event 20 should consume those routes when available instead of duplicating them.

### Event 2 Zombie Outbreak and Event 10 Death

Zombie, Death, alien, and other nonhuman countries must be excluded through shared nonhuman classifiers. They should not receive ordinary Black Plague deaths or normal prevention decisions unless their own spec explicitly opts in.

## Global eradication

The natural outbreak is eradicated when:

- no state is Incubating, Infected, Severe Crisis, Collapsed, Contained, Recovery, or Rat-Controlled by an active rat country
- no scheduled overseas or transport exposure remains
- no rat resurgence basin remains active
- every remaining monitored state completes cleanup

Eradication records a major event-chain milestone and removes the active natural world-threat source. It does not erase:

- completed weaponization projects
- foreign stockpiles
- historical event log entries
- country countermeasure progress
- permanent prevention reforms
- demographic losses

## Balance and abuse protections

- A country cannot farm cure progress by repeatedly infecting and cleaning the same state without meaningful new cases.
- Medical aid cannot duplicate equipment or create population.
- Weaponized deployment always consumes real stockpile and delivery capacity.
- A state cannot receive multiple simultaneous mortality effects from natural and weaponized provenance.
- Rat occupation does not add a second disease instance.
- Publishing research cannot be repeated for unlimited diplomatic rewards.
- Project accident chances cannot be removed by saving and reopening a single iteration choice.
- AI does not start weaponization without sample access, capacity, and route permission.
- Countries cannot use disease cleanup to bypass occupation, resistance, or other unrelated state systems.

## Acceptance criteria for countermeasures and biowarfare

This surface is complete only when:

- the Black Plague has separate disease identity from ordinary bubonic plague
- country progress uses visible milestones
- full progress lowers deaths and spread without instant removal
- state cleanup requires local containment and low disease load
- foreign sharing and theft use real costs and diplomacy
- Doctor Wu can accelerate treatment without instant global cure
- Evolution II opens port jumps through real route logic
- the special project has several phases and a large iteration pool
- safety, acceleration, dual-use, and defensive conversion choices have distinct consequences
- stockpile accidents use the same outbreak state machine
- delivery uses existing biowarfare systems
- condemnation, air cleanliness, deaths, chaos, and world threat are aligned
- the dedicated Black Plague strategic-response category reuses the existing disease state, contamination, death, countermeasure, and world-end systems instead of duplicating them

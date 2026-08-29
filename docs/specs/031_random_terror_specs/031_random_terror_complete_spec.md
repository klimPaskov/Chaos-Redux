# Event 31 Random Terror complete specification

This file compiles the thirteen canonical specification parts into one reading copy.

The individual part files remain the authoritative units for implementation review and change tracking.

## Contents

- [Part 1: Event identity and player loop](#part-1-event-identity-and-player-loop)
- [Part 2: Targeting and incident engine](#part-2-targeting-and-incident-engine)
- [Part 3: Government response decisions and missions](#part-3-government-response-decisions-and-missions)
- [Part 4: Evolutions and escalation](#part-4-evolutions-and-escalation)
- [Part 5: Territorial insurgency and country packages](#part-5-territorial-insurgency-and-country-packages)
- [Part 6: Focus tree and political routes](#part-6-focus-tree-and-political-routes)
- [Part 7: Global Jihad triggerable scenario](#part-7-global-jihad-triggerable-scenario)
- [Part 8: The False Revelation world-end branch](#part-8-the-false-revelation-world-end-branch)
- [Part 9: AI, balance, and probability](#part-9-ai-balance-and-probability)
- [Part 10: Cross-event and shared-system interactions](#part-10-cross-event-and-shared-system-interactions)
- [Part 11: Assets, presentation, and localisation direction](#part-11-assets-presentation-and-localisation-direction)
- [Part 12: Achievement package](#part-12-achievement-package)
- [Part 13: Documentation, catalog alignment, and acceptance](#part-13-documentation-catalog-alignment-and-acceptance)

---

## Part 1: Event identity and player loop

### Catalog identity

- Event ID: `31`
- Event name: `Random Terror`
- Event type: `Minor Repeatable`
- Chaos level: `1`, Calm World
- Entry event: `chaosx.nr31.1`
- Status after implementation: Reworked and enabled for normal selection
- Future cluster role: severe member of the proposed Internal Fracture cluster

The event remains repeatable because a defeated network does not remove the possibility of another unrelated movement appearing later.

Each firing is one global pacing event even when several countries are affected.

The event history row should describe the worldwide incident and identify the player-facing primary actor when one exists. Country crisis reports, territorial seizures, and evolutions use their own follow-up records without advancing the global random-event timer again.

### Event promise

Random Terror creates a security crisis that can remain local, spread between states, cross borders, or become a territorial war.

The opening should be immediately understandable.

Several countries receive attacks in specific active states. The state suffers deaths, damage, lower output, and supply disruption. The government receives a compact response category and must decide how much force, intelligence, infrastructure protection, victim support, and international cooperation to commit.

A successful government can dismantle the active cells and restore normal control.

A weak or reckless government can produce wider recruitment, stronger networks, coups, insurgent territory, civil war, and an extremist state.

The baseline must support the full ordinary rise and defeat of a territorial movement. Evolutions widen coordination, range, survival, ideology, and military ambition. They do not replace the baseline chain or reserve all meaningful escalation for late Chaos tiers.

### Representation and fictionalization rules

Every Event 31 organization, leader, emblem, country identity, slogan, and faction is fictional.

Terrorism is defined through violent organization and conduct. It is never defined through religion, ethnicity, nationality, civilization, refugee status, or ordinary political identity.

Target selection never gives extra weight to a country because it is Muslim-majority, Christian-majority, Jewish-majority, Hindu-majority, Buddhist-majority, secular, or associated with another faith.

Recruitment never receives a population bonus from religious or ethnic composition.

Evolution IV creates one fictional jihadist branch with a specific extremist doctrine. Muslim governments, Muslim soldiers, Muslim clerics, Muslim communities, and rival Muslim movements can become its main opponents.

The movement's hostility toward Muslim governments comes from its fictional claim that those governments are illegitimate. This hostility is an actor-specific strategic rule and never becomes a general rule about Islam.

Displaced civilians and refugees are victims of the crisis. They can create relief and transport pressure because people need protection and services. Their identity never raises terror recruitment or infiltration chance.

Player-facing text must describe fictional actors by their actions, structure, stated goals, territory, and public behavior. It must not use real extremist propaganda, real organization names, real symbols, sacred calligraphy, slurs, or collective suspicion.

### Core national values

Affected countries manage two visible values.

#### Terror Pressure

Terror Pressure is the primary value and uses a visible range from `0` to `100`.

It summarizes the network's ability to maintain cells, recruit, coordinate attacks, conceal survivors, support territorial actors, and attempt political takeover.

| Range | Public state | Main gameplay meaning |
| --- | --- | --- |
| `0` | Cleared | No active Event 31 crisis remains in the country |
| `1` to `20` | Traces | Dormant contacts or one isolated cell remain |
| `21` to `40` | Local Cells | Repeated incidents and one or two active states are possible |
| `41` to `60` | Sustained Campaign | Coordinated attacks, cross-state movement, and stronger missions become possible |
| `61` to `80` | State Challenge | Armed enclaves, defections, capital infiltration, and territorial seizure become serious risks |
| `81` to `100` | Takeover Risk | Coup attempts, civil war, capital seizure, and coordinated uprisings become likely |

Terror Pressure rises through unresolved attacks, failed or indiscriminate operations, foreign supply, safe havens, active training areas, military defections, repeated state loss, and victories by connected territorial actors.

It falls through clean intelligence successes, loss of active cells, disruption of external support, protection of transport and depots, defections, retaken territory, successful prosecutions, restoration of services, and the defeat of connected actors.

Pressure should move in meaningful steps. Ordinary actions must not reduce a severe crisis to zero in one click.

#### Response Legitimacy

Response Legitimacy is a supporting value and uses a visible range from `0` to `100`.

It represents public trust in the government's conduct, local willingness to share information, the credibility of public protection, the reliability of institutions, and the extent to which civilians distinguish the state from arbitrary violence.

High legitimacy improves intelligence quality, defection rates, local protection, mission reliability, and post-crisis recovery.

Low legitimacy increases concealment, retaliatory recruitment, false reports, abusive-operation risk, regional resistance, and political destabilization.

Legitimacy rises through victim support, restored services, precise operations, public accountability, local defense cooperation, protected worship and community sites, credible surrender terms, and restraint after victory.

Legitimacy falls through collective punishment, civilian deaths caused by state action, indiscriminate restrictions, abandoned victims, concealed abuses, arbitrary destruction, repeated failed raids, and occupation policies that punish a whole state.

Legitimacy does not make a country immune to attacks. It changes the quality, cost, and long-term result of the response.

### State activity ladder

Every affected state uses one clear Event 31 activity stage.

| Stage | Working state | Visible meaning |
| --- | --- | --- |
| `0` | Clear | No active modifier or cell remains |
| `1` | Dormant | Contacts and safe locations exist, but recurring attacks are uncommon |
| `2` | Active | The state can generate recurring incidents and local damage |
| `3` | Entrenched | The network has recruitment, supply, and concealment capacity inside the state |
| `4` | Armed Insurgency | Organized armed formations, defections, and state-seizure incidents become available |
| `5` | Lost Local Control | The government no longer exercises reliable control and territorial transfer can occur |

A state normally advances one stage at a time.

Major failures, coordinated attack waves, or a connected territorial actor can accelerate progression. A single minor incident must not jump a stable state directly to loss of control.

State recovery also moves in stages. A retaken state can remain damaged, frightened, or contested after the armed modifier is removed.

### Supporting global and actor values

Later evolutions introduce additional values only when they become useful.

- Network Reach appears after Evolution II and measures the ability of connected organizations to act outside permanent cell states.
- International Unity appears after Evolution IV and measures cooperation among fictional jihadist actors.
- Territorial Control, Network Authority, and External Supply appear only for territorial extremist countries.
- Apocalyptic Readiness remains hidden and is used only to test whether The False Revelation can begin.

The early national response category must not show these later values before they matter.

### Baseline incident lifecycle

A normal affected country moves through the following cycle.

#### Opening shock

The country receives one visible attack report tied to an exact state.

The report establishes civilian harm, state damage, the apparent incident family, and the government's immediate choices.

The state enters Active activity unless the firing represents an already entrenched recurrence.

The country gains Terror Pressure and opens the response category.

#### Assessment

The government chooses its first emphasis from protection, intelligence, victim support, or rapid coercion.

The choice changes the available actions, the next mission pool, and the likely outcome of the first operation.

It should not permanently lock the country into one doctrine.

#### Recurring crisis

Active states can produce further incidents through event-owned pacing.

The player responds through decisions and timed objectives.

Successful response lowers pressure and state activity.

Failure adds damage, creates another hotspot, exposes a foreign connection, or advances the state toward armed insurgency.

#### Escalation or containment

A country that lowers every state to Clear and reduces Terror Pressure to zero closes the category after a short recovery report.

A country that reaches State Challenge can face training camps, military defections, capital infiltration, an enclave, or a connected coup attempt.

A country at Takeover Risk can face civil war, capital seizure, a government replacement attempt, or territorial transfer to a new actor.

#### Aftermath

A contained local crisis leaves a short memory through reconstruction, victim support, security reform, or a damaged-legitimacy aftermath.

A defeated territorial movement creates a larger aftermath with prisoners, displaced civilians, damaged states, captured records, foreign sponsors, and the future treatment of former members.

### Repeatable firing behavior

The event's global repeatable weight follows the ordinary Chaos Redux repeatable-event rules.

A later firing can affect countries that have never experienced Event 31 and countries where a previous crisis was fully cleared.

A country with an active Event 31 crisis should normally receive reinforcement of its current chain instead of a second separate category.

A repeat firing can add one new hotspot, intensify one active hotspot, expose a link to another country, or create a coordinated incident wave.

The event should prefer geographic and political variety across consecutive firings.

A recently cleared country receives a recovery cooldown before it can be selected again unless a connected transnational network deliberately re-enters it.

A territorial Event 31 country cannot be selected as an ordinary victim. It can receive actor-specific internal rivalry, supply, merger, defection, and collapse incidents.

### Global firing scale

The number of newly affected countries rises with the current evolution and the available eligible pool.

The following values are tuning anchors, not unconditional promises.

| State of Event 31 | Normal affected-country target |
| --- | --- |
| Baseline | `3` countries |
| Evolution I | `5` countries |
| Evolution II | `7` countries |
| Evolution III | `10` countries |
| Evolution IV | `15` countries |
| Evolution V | up to `20` countries |

The actual count is clamped by valid targets, cooldowns, geographic diversity, performance, and the need to avoid flooding one multiplayer session with popups.

One country normally receives one opening hotspot at baseline.

Later evolutions can begin with two or three linked hotspots. Evolution V can seed three to five hotspots only in the most severe setup or the Maximum manual scenario.

### Player experience by campaign stage

#### Calm World

The event appears as a serious but manageable security crisis.

Most countries can contain it with focused spending and careful choices.

Territorial escalation is possible after repeated failure, but it should be unusual in a stable, well-governed country.

#### Gathering Storm and Rising Chaos

Networks coordinate, cross borders, exploit wars, and place more pressure on transport and government control.

Cooperation between affected countries becomes more valuable.

Territorial actors survive longer and foreign sponsors become more important.

#### Chaos Tier and Totalen Chaos

Territorial insurgencies can become lasting states.

Several conflicts may connect through supply, training, propaganda, and coordinated takeover attempts.

Evolution IV can introduce the fictional jihadist international and its conflict with Muslim governments and other rivals.

#### World Collapse

Evolution V can coordinate active networks and territorial countries into global war.

The False Revelation remains a separate terminal branch with its own readiness, enable state, territorial proof, and delayed trigger.

### Government outcome families

A government can reach any of these outcomes without changing the event's identity.

#### Clean containment

Cells are dismantled, victims receive support, state damage is repaired, and legitimacy remains high.

The country gains a limited long-term counterterror capacity and a longer recurrence cooldown.

#### Coercive containment

The immediate network is broken, but legitimacy falls and dormant traces remain.

A later recurrence is easier and can begin at a higher state stage.

#### Negotiated surrender

A local territorial movement gives up weapons under enforceable terms.

The government avoids a costly assault but inherits prisoners, reintegration, monitoring, and political backlash.

This outcome is available only when the actor is materially weakened and no active mass-atrocity route blocks negotiation.

#### Frozen enclave

The government contains but does not retake an extremist enclave.

The enclave survives as a weak territorial actor and can become a safe haven, sponsor proxy, or future target.

#### Government victory in civil war

The parent state defeats the actor and begins a post-conflict recovery chain.

#### Extremist takeover

The actor captures the government, wins the civil war, or seizes enough of the country to replace the prior regime.

The country package changes to an Event 31 actor identity with its own routes and obligations.

#### Partition

Neither side wins quickly.

The extremist country remains on the map and the parent country retains a viable core territory.

### Multiplayer behavior

Event 31 uses the existing multiplayer event-delivery rules.

One global firing should not produce duplicate mechanical application because several players receive information.

Each affected player controls their own national response.

AI countries resolve the same choices through route-aware weights.

When several players are affected by one connected network, intelligence sharing and joint operations require explicit participation. One player's decision cannot spend another player's stockpile or commit another player's divisions without an accepted interaction.

A player controlling an Event 31 territorial country receives the full country package, focus tree, decisions, and diplomacy.

A player controlling a Muslim-majority government is never treated as secretly aligned with the jihadist movement. The player receives the same vulnerability rules as any other government and additional actor-specific opposition content only after the jihadist branch exists.

### Event log and Event Details direction

The event name remains visible as Random Terror.

Event Details should explain that fictional armed cells attack several countries, damage active states, and can grow into territorial movements when governments fail to contain them.

It should mention the compact response loop, recurring state activity, cross-border growth, and possible extremist countries.

It should not reveal The False Revelation conditions, hidden readiness, future leaders, surprise incidents, or internal probability formulas.

The Evolutions view shows the five accepted evolution names and public premises.

The public World End Scenarios section shows one independent row for The False Revelation with its own persistent enable toggle.

The manual scenario appears only in the Triggerable Scenarios registry.

### Completion standard for the core loop

The core design is satisfied only when all of the following are true.

- Several countries can be affected by one firing without creating several global pacing events.
- Every attack is tied to an exact eligible state.
- Terror Pressure and Response Legitimacy visibly change choices and outcomes.
- State activity can rise, spread, fall, and clear.
- The ordinary response stays within the action and mission budgets.
- Baseline progression can produce and defeat a territorial extremist country.
- A stable country has a credible path to containment.
- A failing country can reach coups, civil war, partition, or takeover.
- Repeat firings deepen active crises without creating duplicate categories.
- Religion, ethnicity, nationality, and refugee identity never affect baseline vulnerability or recruitment.
- AI countries can use the same system without a human-only interface dependency.

---

## Part 2: Targeting and incident engine

### Targeting purpose

The target engine should create variety without treating random selection as careless selection.

The event needs countries that can support meaningful incidents, states whose damage matters, and enough geographic spread that one firing feels global.

It must avoid invalid territories, empty regions, terminal actors, repeated harassment of the same country, and identity-based weighting.

### Country eligibility

A country is normally eligible when it exists, controls at least one valid populated state, and can receive an ordinary civilian and government crisis.

The following countries are excluded from ordinary victim selection.

- Event 31 extremist countries and countries currently transformed by an Event 31 takeover
- countries classified as special Chaos actors when ordinary civilian crisis logic does not fit them
- actual nonhuman countries
- countries that have reached a terminal world-end state incompatible with ordinary event progression
- countries with no eligible state
- countries under an active Event 31 recovery cooldown, unless a connected network has a specific re-entry route
- countries already assigned the maximum active hotspot count for their stage

A country with an active ordinary crisis remains eligible for escalation through its current chain.

It should not receive a second independent Event 31 identity or duplicate decision category.

### Country selection factors

Selection uses a broad opportunity score.

Useful positive factors include:

- low stability
- an active war
- severe war exhaustion or recent defeat
- occupied or contested territory
- high resistance or weak local control
- a recent civil war
- exposed transport and supply networks
- a long or poorly secured border
- existing Event 31 pressure in a neighboring country
- an active safe haven or territorial actor nearby
- a foreign sponsor with access to the region
- a previous unresolved Event 31 trace

Useful negative factors include:

- a very recent Event 31 firing
- successful complete containment
- strong current protection of likely target states
- no meaningful populated or connected state
- a severe crisis load from unrelated event systems that would create unusable UI or performance pressure
- geographic duplication inside the same firing when other regions remain available

Country size can increase the number of possible hotspots, but it must not make major powers automatic targets every time.

Small countries remain eligible when an incident can create a meaningful national crisis.

### Forbidden target factors

The following factors must never increase ordinary target chance.

- religion
- Muslim-majority status
- ethnic composition
- nationality
- civilization labels
- refugee population
- immigrant population
- ordinary ideology by itself
- a real historical stereotype about violence or instability

A country can become relevant because it is at war, unstable, occupied, adjacent to a network, or strategically exposed. Identity alone is never an opportunity score.

### Geographic diversity

A normal global firing should try to cover more than one region.

The selection process should avoid choosing several neighboring countries unless the incident is explicitly a connected regional wave.

At higher evolutions, a mixture is preferred.

- one established network region
- one vulnerable new region
- one country connected through a sponsor or route
- one distant demonstration attack after transnational reach exists

The system should remember recently selected countries and continents long enough to prevent a small pool from dominating repeat firings.

### State eligibility

A valid incident state should normally be owned or controlled by the affected country and contain a real civilian, transport, industrial, administrative, or military target context.

Strong state candidates include:

- populous urban states
- state or national capitals
- rail junctions
- ports
- supply hubs
- major infrastructure corridors
- industrial states
- airbase states
- border states connected to an active network
- states with existing activity or a neighboring active state

The following states are excluded.

- wastelands
- empty or nearly empty regions with no meaningful target
- isolated ocean islands that cannot support the selected incident
- states held by an invalid actor when the incident requires the government's actual administration
- states already destroyed or depopulated beyond the event's minimum civilian threshold
- states under an incompatible terminal modifier

The system should prefer an exact active state over a capital proxy.

A capital is used only when the incident is genuinely a capital attack, political takeover attempt, or emergency government crisis.

### State weighting and repetition

The first hotspot should normally be meaningful but not always the country's capital.

A state gains weight from population, infrastructure, railways, ports, depots, industry, administrative importance, and adjacency to an active cell.

A state loses weight after a recent incident so the same city does not absorb every attack.

A connected network may deliberately return to a state when it has an entrenched cell, unfinished mission, surviving safe house, captured depot, or symbolic rivalry.

A rural border state can be selected for a training area, safe haven, smuggling corridor, or armed enclave.

An urban state is preferred for hostage incidents, civic attacks, capital infiltration, or transport disruption.

### Incident families

The incident pool should remain tactically abstract.

It describes outcomes, targets, and public consequences without teaching real attack preparation, evasion, recruitment, or financing methods.

#### Civilian attack

An armed cell attacks a civilian gathering, residential area, market, workplace, or public service.

The state suffers an immediate civilian death loss, panic, and a temporary local-output penalty.

A larger attack can create national mourning, victim-support actions, and a public strategic shock.

#### Transport disruption

The network damages rail, road, port, train, or supply infrastructure.

The state loses infrastructure or railway capacity and receives temporary supply disruption.

The government can protect the corridor, repair it, or accept military supply pressure elsewhere.

#### Depot sabotage

A military or logistics depot is damaged and some equipment can be lost.

An entrenched cell or territorial actor can capture a bounded share of the equipment when local control is weak.

The event never grants equipment that did not plausibly exist in the country or the state.

#### Port or convoy attack

A coastal network damages port facilities, disrupts convoy use, or targets a relief and supply route.

This incident requires an eligible coastal state and meaningful naval logistics.

#### Assassination attempt

A fictional or generic public official, security commander, local administrator, judge, union organizer, journalist, religious leader, or community organizer is targeted.

The default incident does not kill a real named historical country leader through uncontrolled random selection.

A named Event 31 fictional character can be killed when the character package and succession rules support it.

#### Hostage crisis

The network seizes civilians or officials and creates a timed response.

The government chooses between negotiation, a prepared rescue, delay, or a rapid assault.

Intelligence quality and Response Legitimacy influence casualties and later recruitment.

#### Security-site assault

A police, intelligence, barracks, courthouse, prison, or local administration site is attacked.

Failure can free prisoners, capture weapons, weaken local control, or create defections.

#### Propaganda surge

A public atrocity, failed government response, foreign victory, or captured town increases recruitment and copycat pressure.

This remains an abstract communications effect and does not reproduce real propaganda.

#### Arms theft

The network captures a bounded amount of ordinary equipment from a poorly protected state or defeated local formation.

The incident can strengthen an armed-insurgency stage or territorial actor.

#### Foreign funding discovery

Evidence reveals support from a fictional sponsor, criminal patron, rival government, or aligned territorial actor.

The government gains diplomatic and intelligence choices.

A false or manipulated trail remains possible when intelligence quality is low.

#### Smuggling corridor

A neighboring state or country becomes connected to the active network.

The corridor raises External Supply or Network Reach and creates a timed disruption mission.

The event identifies broad state connections and does not present real-world evasion methods.

#### Training area

An entrenched rural or border cell establishes an armed training area.

The state advances toward Armed Insurgency unless the government acts.

#### Copycat wave

An attack inspires disconnected imitators.

A second state gains low-level activity without immediately joining the same organization.

Evolution I can later absorb copycats into an organized network.

#### Failed raid

A government operation misses its target, causes avoidable damage, or drives survivors into another state.

Terror Pressure rises and Response Legitimacy falls according to the failure.

#### Intelligence breakthrough

Informants, captured records, financial evidence, defectors, or foreign intelligence expose a cell.

The government receives a limited window for a precise operation.

#### Defector testimony

A member abandons the organization and reveals internal weakness.

A credible protection and surrender policy makes this more likely.

Abuse of prior defectors makes it rarer.

#### Border displacement and relief strain

Civilians flee an active state or territorial front.

Nearby states receive relief, housing, transport, and service pressure.

The event treats displaced people as victims and never adds terror activity because refugees arrived.

A network can exploit disrupted routes only through a separate corridor or criminal-support incident with its own evidence.

#### Military defection

A local police or military formation defects, collapses, or surrenders equipment.

This incident requires high Terror Pressure, low local control, or an existing armed insurgency.

It can create a limited unit transfer or advance a territorial seizure.

#### Capital infiltration

An entrenched network prepares attacks on the capital, government offices, radio, transport, or command sites.

The country receives an emergency timed mission.

Failure can trigger a coup, temporary government paralysis, or capital seizure.

#### Inter-group rivalry

Two Event 31 organizations compete over leadership, recruits, funding, territory, or doctrine.

The government can exploit the split, but violence and civilian harm may increase first.

#### Community rejection

Local civic, labor, religious, tribal, municipal, or professional institutions reject the network and protect civilians.

This lowers recruitment and can improve intelligence.

After Evolution IV, Muslim religious and community opposition receives additional fictionalized reaction variants without becoming a special resource stereotype.

#### Joint operation

Two or more countries coordinate an intelligence, border, relief, or military action.

The incident requires explicit participating actors and cannot spend resources from a country that did not join.

#### Sponsor exposure

Public evidence links a foreign government or network to material support.

The result can create opinion penalties, Condemnation, sanctions pressure, covert escalation, or sponsor withdrawal.

#### Cannibal clash

An Event 31 organization fights an Event 14 cannibal faction over territory, supplies, prisoners, or public fear.

The two sides cannot cooperate or merge.

The clash can damage both actors and harm civilians.

### Incident selection by stage

Low activity favors isolated attacks, copycats, local sabotage, hostage incidents, and intelligence discoveries.

Entrenched activity adds corridors, training areas, arms theft, repeated waves, sponsor links, and failed government raids.

Armed Insurgency adds military defections, enclave formation, depot capture, capital infiltration, and open territorial clashes.

Lost Local Control moves into territorial transfer, civil war, coup, government takeover, or negotiated surrender.

An incident family must be valid for the selected state.

A port incident cannot occur in an inland state.

A rail incident requires a meaningful railway or infrastructure context.

A military defection requires an armed or security presence.

When no suitable incident exists, the engine should select another state or postpone the pulse. It should not substitute an unrelated capital event.

### Recurring incident pacing

Event-owned pacing applies only to affected countries and active states.

The design does not require a recurring whole-world daily, weekly, or monthly scan.

A country crisis should receive an assessment pulse around every `30` days while active.

Individual incident timing should vary with state activity, Terror Pressure, protection, foreign supply, and current missions.

Useful timing bands are:

- `60` to `90` days for a low-pressure dormant or active cell
- `30` to `60` days for an entrenched cell
- `15` to `35` days for an armed insurgency or coordinated wave
- shorter emergency countdowns only for a visible capital attack, hostage crisis, or territorial offensive

A successful protection mission can delay the next incident even if it does not remove the cell.

A failed operation can accelerate the next pulse.

### Cross-state spread

Spread requires a reason.

Valid causes include adjacency, a transport corridor, an exposed border, surviving members displaced by a raid, a connected sponsor, a copycat wave, a safe haven, or a territorial actor.

A state does not spread activity merely because time passed.

Normal cross-state spread uses a meaningful cooldown, with `90` days as the main tuning anchor.

High Network Reach can shorten the cooldown or permit a non-adjacent demonstration attack.

The system should prefer one new hotspot at a time so the player can understand the change.

### Cross-border spread

Cross-border spread becomes common only after an organization has an external connection or Evolution II is active.

A neighboring country is selected through its own valid-target rules.

The receiving country gets a clear opening report and can cooperate with the source country.

Foreign spread does not transfer the source government's decisions or costs.

A territorial actor can support cells abroad through Network Authority and External Supply.

### State modifier effects

Each state activity stage should have a distinct dynamic modifier or clear staged state modifier.

Effects can include:

- local output loss
- construction disruption
- infrastructure and railway damage risk
- supply penalties
- lower local compliance or control where relevant
- recurring civilian death risk
- resistance or garrison pressure when the state is occupied
- increased chance of arms theft, defection, or territorial seizure at severe stages

The modifier should not apply every severe penalty at Stage 1.

State impact must grow visibly with activity.

The modifier follows the state, but Event 31 ownership and crisis attribution must update when control changes.

An occupying Event 31 actor should not receive the same government-victim response category as the original owner.

### Deaths and population loss

Every civilian death removes real state population and records the loss through the shared Deaths system when enabled.

Death amounts scale with incident type, state population, activity stage, protection, current war damage, and outcome quality.

The design uses broad severity bands.

- small incidents can kill hundreds
- serious attacks can kill low thousands
- coordinated high-chaos attacks can kill several thousand or tens of thousands in a dense state
- territorial atrocities and world-end actions can exceed those ranges when supported by the event stage and state population

Every amount is clamped against a protected population floor.

The same deaths must not be applied twice through an event effect and a recurring state modifier.

Government-caused civilian deaths use a separate Deaths reason so the aftermath can distinguish attack victims from counterterror casualties.

### Building and infrastructure damage

Damage should affect real buildings when the incident supports it.

Possible targets include infrastructure, railways, supply hubs, ports, airbases, factories, anti-air, depots represented through local systems, and administrative capacity represented by state modifiers.

Damage scales with available building levels.

The event should not destroy a building that does not exist or turn every attack into industrial devastation.

Repair and restoration decisions must use real construction capacity, equipment, trains, convoys, or civilian-factory commitment according to the damaged surface.

### Chaos and Condemnation

Ordinary incidents feed Chaos indirectly through tracked deaths and wider campaign consequences.

A major public attack, captured capital, coordinated international wave, or territorial atrocity can also add a modest direct Chaos shock.

Direct Chaos should be reserved for a public strategic change and must not duplicate the full effect of the same deaths.

Condemnation can arise from:

- public extremist atrocities
- public state-sponsored support
- public government counterterror atrocities
- exposed cover-ups
- forced rule, expulsions, or mass killing in captured territory

A hidden ordinary cell attack does not automatically create an international sanctions system.

### Pressure changes after incidents

Every incident outcome should state what changes Terror Pressure, Response Legitimacy, state activity, and any later network value.

The following ordering should hold in ordinary cases.

- clean government success produces the strongest pressure reduction and no legitimacy loss
- costly success produces a smaller pressure reduction and can reduce legitimacy
- partial success prevents one consequence but leaves the cell active
- operational failure raises pressure and can advance state activity
- abusive failure raises pressure, lowers legitimacy, and makes recruitment or spread easier
- extremist victory raises pressure, activity, Network Reach, or territorial control according to stage

### Coup, civil war, and territorial outcome choice

At severe pressure, the engine chooses the outcome that best fits the country.

#### Coup attempt

Use when the network has capital access, compromised officials, defecting security units, or a strong political front but insufficient rural territory for a normal secession.

Success can replace the government, create a short internal war, or give the actor control of the capital and nearby states.

#### Territorial seizure

Use when the movement has one or more Stage 5 states, a contiguous enclave, local armed strength, and a viable carrier package.

#### Civil war

Use when the country has several contested states, a divided army, and enough viable territory for both sides.

The Event 31 chain should coordinate with Event 21 so the same country does not receive two unrelated civil wars at once.

#### Government collapse

Use when the actor controls the capital, the parent has almost no viable territory, and a tag transfer is safer than an invalid one-state remnant.

#### Negotiated enclave

Use when the government is exhausted, the actor is locally entrenched, and neither side can achieve a clean victory.

The result creates a weak territorial actor or an autonomous settlement with a high recurrence risk.

### Cleanup

A country closes the ordinary crisis only when:

- no active Event 31 state remains
- no connected territorial actor controls its core territory
- no active capital, hostage, corridor, or retaking mission remains
- Terror Pressure reaches zero
- temporary response commitments have been released

Cleanup removes obsolete decisions, missions, map highlights, temporary modifiers, targets, and scheduled incident jobs.

It preserves history, Deaths records, Condemnation records, recovery modifiers, territorial actors that still exist, and any lasting institutional reform earned through play.

A defeated or annexed country must not leave an active incident job pointing to an invalid state or actor.

### Acceptance cases

The target and incident engine is complete only when it can pass these cases.

1. A stable inland country receives a valid urban or transport incident without a port-only result.
2. A small island country receives an incident suited to its real states and does not lose its only state through invalid partition logic.
3. A Muslim-majority country has the same baseline vulnerability factors as an otherwise comparable country.
4. Refugee movement creates relief pressure without creating terror activity by identity.
5. A recently targeted country is skipped when other valid regions exist.
6. An entrenched border cell spreads through an evidenced corridor after a cooldown.
7. A failed raid pushes survivors into a named neighboring state and lowers legitimacy.
8. A successful protection mission delays or prevents a transport incident.
9. A state with no port never receives a port attack.
10. Civilian deaths reduce real population once and appear once in the Deaths log.
11. A government and Event 21 do not start duplicate civil wars in the same country.
12. Clearing every hotspot closes the category and cancels scheduled jobs.

---

## Part 3: Government response decisions and missions

### Presentation choice

The national response uses an ordinary decision category.

It should have:

- one static category picture
- concise dynamic category text
- the current Terror Pressure stage
- the current Response Legitimacy stage
- the number and names of active states
- one next important threshold or objective
- three to five visible primary actions
- no more than three active missions
- an event-owned map highlight for active states and current operation targets

A full custom scripted GUI would add cost without enough gameplay value.

The player makes normal decisions, reads exact state tooltips, and follows timed missions. A separate window would add maintenance and duplicate information without improving target management.

The category picture should show a fictional period security and relief response, not a tactical diagram, real extremist imagery, or fake controls.

### Decision-category phases

The category changes its visible actions by crisis phase.

#### Phase 1: Immediate shock

The country has one or two active states and limited information.

The category should show protection, assessment, victim support, and one rapid response choice.

#### Phase 2: Active network

The country has sustained Terror Pressure, several incidents, or an entrenched state.

The category should show targeted operations, finance and corridor disruption, intelligence cooperation, defections, and limited restrictions.

#### Phase 3: Territorial challenge

The country has an armed insurgency, lost state, enclave, coup risk, or civil war.

The category should show military reinforcement, capital security, relief corridors, retaking operations, surrender terms, and foreign intervention.

#### Phase 4: Recovery

No active armed cell remains, but victims, damaged transport, displaced civilians, and damaged legitimacy still require attention.

The category should show only relevant reconstruction and institutional choices, then close.

### Cost design

No action may use more than four spendable cost types.

Political power and command power can appear when they fit the action, but they cannot become the only generic payment used across the category.

The main cost families are:

- infantry equipment
- support equipment
- trucks
- trains
- convoys
- fuel
- manpower commitment
- command power
- army experience
- air experience for air-supported operations when relevant
- temporary civilian-factory commitment
- temporary military-factory output burden
- tied-down divisions in exact states
- stability or war support as an accepted consequence
- Response Legitimacy risk
- intelligence exposure or sponsor escalation

Costs scale with country size, active-state count, state geography, current pressure, current war, and the chosen operation.

A small country should not face the same absolute equipment debit as a major power.

A major power should not suppress a nationwide crisis for a token payment.

### Immediate-response decisions

#### Establish Joint Response Cell

This action creates the country's basic Event 31 coordination capacity.

It combines police, intelligence, military liaison, transport administration, emergency services, and local government reporting.

It should cost a temporary administrative and command commitment, not a permanent political-power purchase.

Effects:

- improves incident identification
- unlocks targeted intelligence actions
- reduces duplicate or false response penalties
- reveals a concise breakdown of active states
- creates a stronger chance of clean outcomes

The action can be skipped in favor of rapid coercion, but later operations become less reliable.

AI preference rises with several active states, high industry, or a previous failed raid.

#### Protect Critical Transport

The country selects the most exposed active transport state or corridor.

Costs can include trains, support equipment, fuel, and tied-down divisions.

Effects:

- starts a timed protection mission
- reduces railway, infrastructure, port, convoy, and supply-hub incident chance in the target area
- limits equipment theft
- can redirect an attempted attack toward a less protected target

The protection remains local and temporary.

AI preference rises when the state contains a supply hub, active front, capital connection, major port, or railway bottleneck.

#### Support Victims and Restore Services

The country commits civilian factories, support equipment, trains or convoys, and emergency manpower according to the state.

Effects:

- restores damaged services and transport
- improves Response Legitimacy
- reduces panic and copycat pressure
- improves local information flow
- protects displaced civilians
- accelerates recovery after the cell is removed

This action does not directly dismantle an armed cell.

Its value comes from making later operations safer and reducing the network's ability to exploit harm.

AI preference rises after high civilian losses, low legitimacy, or severe service disruption.

#### Targeted Intelligence Sweep

The country commits intelligence capacity, support equipment, and a bounded command or manpower burden.

Effects:

- improves the chance of finding a safe house, sponsor, corridor, or active leader
- can produce an Intelligence Breakthrough window
- lowers the risk that a later raid targets the wrong site
- can reveal that two apparent incidents belong to different organizations

Failure can expose informants, create false leads, or let the cell go dormant.

AI preference rises with high legitimacy and an established response cell.

#### Immediate Security Surge

The country deploys military or police forces rapidly to an active state.

Costs include command power, fuel, support equipment, and a tied-down unit requirement.

Effects:

- reduces immediate incident chance
- can stop an emergency attack or hostage transfer
- raises the chance of local arrests
- creates a stronger civilian-harm and legitimacy risk when intelligence is poor

This is a short-term tool.

It should not be the most efficient long-term response in every situation.

AI preference rises during capital risk, an active war front, or a mission with a short deadline.

### Active-network decisions

#### Conduct Targeted Raid

The country selects one exact active state after meeting an intelligence threshold or accepting a high-risk assault.

Costs can include command power, army experience, support equipment, and tied-down divisions.

The raid can produce clean success, costly success, partial success, failure, or abusive failure.

A successful raid can lower state activity, capture records, free hostages, or remove a local leader.

A failed raid can kill civilians, damage buildings, expose informants, or drive survivors into another state.

The decision must show the current public risk band and the main factors affecting it.

It must not reveal the hidden random roll.

#### Disrupt Finance and Smuggling

The country targets the active network's current External Supply source.

Costs can include convoys, intelligence exposure, civilian-factory burden, and support equipment.

The action can:

- reduce foreign supply
- close a border corridor
- expose a sponsor
- create a diplomatic incident
- move the network toward criminal predation or territorial seizure when outside funding collapses

The action is weak when used against the wrong support profile.

An intelligence breakthrough should identify the likely source before the player commits.

#### Request Allied Intelligence

The country asks eligible allies, faction members, neighbors, or selected partners for a joint intelligence action.

The request requires relations, route access, or a shared threat.

The responding country chooses whether to participate.

Successful cooperation can reveal cross-border cells, improve raid outcomes, and start a joint corridor mission.

Refusal can preserve secrecy or avoid entanglement.

No country spends resources until it accepts.

#### Offer Defection and Amnesty Channel

The country creates a protected surrender and testimony route for low-level members, coerced recruits, defectors, and local intermediaries.

Costs include administrative capacity, security manpower, and a Response Legitimacy commitment.

Effects:

- raises defection chance
- can split an organization
- can expose a sponsor or training area
- lowers recruitment when defectors are protected
- creates backlash from hardline security actors or victims when terms are too broad

The action is blocked for leaders publicly responsible for mass atrocities and for actors that reject surrender under their current route.

#### Temporary Movement Restrictions

The country imposes a bounded restriction on one exact state or corridor.

Costs include stability, transport output, support equipment, and tied-down manpower.

Effects:

- lowers short-term spread and movement
- disrupts ordinary production and supply
- reduces Response Legitimacy when prolonged or indiscriminate
- can increase smuggling value elsewhere

The restriction expires automatically and cannot be chained without rising costs and legitimacy damage.

#### Protect Community and Religious Sites

This action becomes available when the network attacks local institutions, worship sites, minority neighborhoods, union halls, schools, or community leaders.

It commits local security and emergency services.

Effects:

- prevents intimidation and retaliatory violence
- improves Response Legitimacy
- increases community rejection and information sharing
- lowers the chance that a jihadist actor can present itself as the sole religious authority

The action is available in any country and adapts its visible target to the institutions actually threatened.

It must not imply that religion itself causes the crisis.

#### Expose the Sponsor

After sufficient evidence, the country can publish a foreign-support case.

The player chooses between quiet leverage and public exposure.

Quiet leverage can make the sponsor withdraw or feed false information to the network.

Public exposure can raise Condemnation, unlock sanctions or coalition support, and risk open retaliation.

A weak evidence case can damage the government's credibility.

### Timed missions

#### Contain the Attack Wave

Typical duration: `90` to `120` days.

The country must prevent new state activity while reducing pressure or clearing the original hotspot.

Success:

- lowers Terror Pressure
- prevents one spread attempt
- improves Response Legitimacy when civilian harm stays low

Partial success:

- no new state appears, but the original cell remains

Failure:

- one valid new hotspot appears or an existing state advances

#### Protect the Transport Network

Typical duration: around `120` days.

The country must keep named rail, supply, port, or convoy assets operational and maintain the required protection commitment.

Success:

- prevents major transport damage
- lowers External Supply or local activity
- preserves military supply

Partial success:

- the route remains open, but one building or stockpile suffers damage

Failure:

- the corridor is disrupted and the network gains pressure or captured supplies

#### Break the Cross-Border Corridor

Typical duration: around `150` days.

Two or more countries coordinate control of named border states, ports, or transport links.

Success:

- removes the corridor
- lowers Network Reach or External Supply
- improves future joint-operation efficiency

Partial success:

- the corridor weakens but shifts to another valid connection

Failure:

- the network spreads into another country or exposes the participating states to retaliation

#### Prevent Capital Seizure

Typical duration: `60` to `90` days.

This emergency mission appears only after credible capital infiltration or takeover preparation.

The country must protect the capital, maintain command continuity, and reduce the relevant network stage.

Success:

- blocks the current coup or seizure attempt
- can expose compromised officials or defecting units

Partial success:

- the capital remains held, but nearby states or infrastructure are lost

Failure:

- triggers a coup attempt, civil war, government paralysis, or capital transfer according to country conditions

#### Retake the Lost State

Typical duration: around `180` days.

The country must regain control of an Event 31 enclave or lost state and hold it long enough to restore administration.

Success:

- removes territorial control
- begins recovery and prisoner-handling decisions
- weakens connected cells elsewhere

Partial success:

- military control returns, but the state remains contested and requires a second stabilization phase

Failure:

- the territorial actor entrenches, gains equipment, and may receive recognition or foreign support

#### Restore Civil Authority

Typical duration: `120` to `180` days after military recapture.

The country must repair services, protect civilians, prevent revenge attacks, and rebuild local administration.

Success:

- clears residual activity
- restores Response Legitimacy
- extends recurrence cooldown

Failure:

- dormant cells return or local resentment keeps the state at Entrenched activity

### Territorial-crisis decisions

#### Military Reinforcement

The country commits specific divisions, fuel, equipment, and command capacity to threatened states.

The commitment improves defensive control and blocks easy state transfer.

It also weakens other fronts and creates supply pressure.

Units must actually remain in the required states for the benefit to continue.

#### Emergency Capital Security

The government establishes command continuity, guarded communications, protected transport, and reserve forces around the capital.

It can prevent a sudden takeover, but it consumes elite units and can reduce activity elsewhere.

#### Isolate the Enclave

The country cuts an extremist territory off from external supply while protecting civilian exits.

Costs include divisions, fuel, trains, convoys where relevant, and a diplomatic burden if the enclave crosses a border.

The action lowers External Supply and can open surrender terms.

An indiscriminate siege harms civilians, raises Condemnation, and lowers legitimacy.

#### Secure Relief Corridor

The country protects civilian movement, food, medicine, and services around a contested state.

The action reduces civilian deaths and recruitment pressure while preserving military options.

A hostile actor can attack the corridor and create a visible mission.

#### Retake State Operation

The country begins a state-targeted military operation after meeting force, supply, and intelligence requirements.

The result depends on relative force, local control, External Supply, terrain, preparation, civilian protection, and support from nearby states.

The action should not instantly transfer the state through a button.

It creates an objective and a conflict state the player must resolve.

#### Negotiate Local Surrender

The government offers terms to an isolated and materially weakened actor.

Possible visible terms include disarmament, prisoner transfer, local amnesty limits, civilian protection, foreign departure, and monitored reintegration.

The action can split moderates from hardliners.

It is unavailable to a dominant actor pursuing mass atrocities or an apocalyptic route.

#### Request Foreign Intervention

The country asks a neighbor, ally, faction, regional coalition, or major power for military or logistical help.

The responder can send equipment, volunteers, intelligence, air support where valid, blockade support, or direct intervention.

Aid creates influence, dependency, diplomatic risk, or postwar claims according to the sponsor.

The player must understand the public price before accepting.

### Operation outcome model

Operations use five public outcome classes.

#### Clean success

The objective is achieved, civilian harm stays low, the cell loses capacity, and Response Legitimacy holds or rises.

#### Costly success

The objective is achieved, but the state suffers casualties, damage, or lost legitimacy.

#### Partial success

One objective is achieved while another remains unresolved.

Examples include freeing hostages while the leaders escape, holding a rail line while another route opens, or retaking a town while the rural cell survives.

#### Failure

The operation misses, stalls, or loses the target.

Terror Pressure rises and the network can relocate, recruit, or capture supplies.

#### Abusive failure

The operation fails and causes major civilian harm, arbitrary destruction, revenge violence, or a public cover-up.

This outcome creates the largest legitimacy loss, can add Condemnation, and strengthens extremist narratives.

The outcome chances should use intelligence quality, legitimacy, state activity, network supply, force preparation, terrain, local support, and previous actions.

### Country route tendencies

A government is not permanently assigned one response ideology.

AI and player choices can create tendencies.

#### Intelligence-led response

Favors response cells, targeted sweeps, evidence, defectors, and joint operations.

It is slower to start and depends on capacity, but it gives the best clean-success chance.

#### Protection-led response

Favors transport defense, victim support, community protection, and relief corridors.

It limits damage and recruitment but may leave leaders active longer.

#### Military response

Favors rapid surges, reinforcement, state isolation, and retaking operations.

It can prevent territorial loss but carries high costs and civilian-risk pressure.

#### Coercive response

Favors broad restrictions, mass detention, rapid raids, and secrecy.

It can suppress a weak cell quickly and can also produce severe legitimacy damage, false arrests, and future recurrence.

#### Negotiated response

Favors defections, surrender, local settlements, and conflict isolation.

It is useful against divided or weakened actors and dangerous against a strong organization using talks to rebuild.

### AI decision principles

Government AI should compare:

- current Terror Pressure
- current Response Legitimacy
- number and stage of active states
- capital and supply risk
- war fronts
- available equipment, fuel, trains, convoys, manpower, and divisions
- expected civilian harm
- sponsor and ally availability
- whether the action addresses the current support source
- whether a mission is already active

AI should not start a costly raid with no intelligence, impose endless restrictions, abandon every war front, or request intervention from an enemy.

AI should protect the capital and critical supply when the threat is immediate.

AI should support victims after major civilian losses even when it also pursues a military response.

### Clutter control and cleanup

Only decisions valid for the current phase, state, and route are visible.

One exact state or corridor is selected at a time for detailed targeted decisions.

Obsolete decisions disappear after a state clears, a corridor closes, a sponsor dies, a war ends, an actor is annexed, or the crisis changes phase.

Basic decisions should be replaced by stronger phase versions instead of remaining beside them.

The category closes after the final recovery obligations end.

No debug-style list of every possible state, sponsor, corridor, or actor should remain visible.

### Exploit controls

The system must prevent:

- repeated victim-support rewards without a real active crisis
- free equipment capture from empty depots
- repeated intervention aid from the same sponsor without cooldown or cost
- endless movement restrictions that permanently suppress spread
- raid cancellation that avoids costs
- surrender loops that repeatedly grant legitimacy
- retake missions against a state already restored
- duplicate capital-security missions
- artificial farming of Terror Pressure for bonuses
- state switching that leaves tied divisions or factory burdens unreleased

Costs are paid once at commitment.

Failure and cancellation release only the portion that was genuinely committed and not consumed.

### Player-facing writing direction

Decision text should name the visible state, corridor, actor, or institution involved.

Costs should be icon-first and concise.

Tooltips should explain the next important threshold, the public risk band, and the exact blocked requirement.

Text must avoid collective blame and real extremist terminology.

Victim-support text should focus on people, services, transport, and recovery.

Coercive actions should describe what the government is doing and the visible public cost without presenting abuse as neutral efficiency.

Religious-opposition content should describe fictional local leaders and communities rejecting the movement's claim. It should not use sacred text as flavor or frame ordinary believers as a security category.

### Completion standard

The government response design is complete only when:

- the category presents one primary and one supporting value clearly
- each phase exposes no more than six primary actions and normally three to five
- no more than three active missions appear
- every action has at most four spendable cost types
- decisions use concrete costs suited to the action
- missions require real map, supply, unit, or crisis work
- clean, costly, partial, failed, and abusive outcomes have distinct consequences
- victim support and service restoration materially affect play
- foreign cooperation requires consent and valid access
- the system can proceed from one attack to containment, territorial war, surrender, partition, or takeover
- AI can use every major action family without a custom GUI
- obsolete actions and commitments clean up correctly

---

## Part 4: Evolutions and escalation

### Evolution model

Event 31 has five true evolutions.

The ordinary rise from one attack to a local cell, armed insurgency, coup, civil war, territorial actor, and defeat remains baseline progression.

An evolution changes the global character of the event.

It adds coordination, reach, territorial durability, a distinct extremist doctrine, or a global war structure.

An evolution should not fire immediately when its Chaos threshold becomes available unless Event 31 has never fired and the campaign begins from a manual scenario or an already evolved opening.

Active evolution pacing should normally use a delayed incident with a meaningful mean time to happen.

The following values are planning anchors.

| Evolution | Minimum Chaos tier | Normal active-event pacing anchor | Main change |
| --- | --- | --- | --- |
| Organized Cells | Gathering Storm | about `90` days after eligibility | local cells form stable regional organizations |
| Transnational Terror Network | Rising Chaos | about `120` days after eligibility | networks act across borders and maintain safe havens |
| Territorial Insurgency | Chaos Tier | about `150` days after eligibility | territorial actors become durable states and support cells abroad |
| The Jihadist International | Totalen Chaos | about `180` days after eligibility | one fictional jihadist movement gains international structure |
| The Final Jihad | World Collapse | about `210` days after eligibility | jihadist actors coordinate global uprisings and conquest |

Campaign state should modify these anchors.

Strong existing networks, multiple active countries, territorial victories, foreign sponsorship, failed government operations, high Network Reach, and captured capitals make an evolution more likely.

Widespread successful containment, collapsed networks, low active-country count, severe internal rivalry, and destroyed territorial actors slow the next evolution.

The evolution engine must distinguish exact timing evidence from score-only tuning. Final implementation needs named probability scenarios and a before and after audit.

### Evolved opening behavior

When Event 31 has not fired before an evolution becomes active, the first ordinary firing should begin at the new global level.

An evolved opening changes the number of countries, initial state stages, incident families, and available organization structures.

It does not replay every lower evolution as a sequence of immediate popups.

The evolution itself receives one log entry, then the opening event describes the current public form.

When Event 31 already has active crises, the evolution appears through a transition incident that changes existing networks and unlocks new content.

### Evolution enable and disable behavior

Every evolution has an independent enable state in Event Details.

A disabled evolution must not set its recorded flag, expose its hidden branch, change its incident pool, or become a prerequisite that blocks baseline resolution.

If one evolution is disabled, later evolutions that depend on its specific content remain unavailable unless the manual scenario provides a tightly scoped bypass for setup.

Baseline territorial actors continue to function when Evolution III is disabled. They remain smaller, less coordinated, and less durable.

Disabling Evolution IV removes the jihadist branch and therefore prevents Evolution V and The False Revelation.

### Evolution I: Organized Cells

#### Public change

Previously disconnected cells begin sharing leadership, resources, intelligence, recruits, and safe locations.

The player sees coordinated attack waves, common organization identities, survivors relocating between states, and evidence of foreign or criminal support.

#### New organization structure

Several active cells in one country or region can consolidate into a named fictional organization.

The organization receives:

- one fictional name and emblem
- one broad ideological or strategic profile
- one regional operating area
- one leadership form
- one current support source
- one rivalry or sponsor relationship when relevant
- one pressure contribution across its active countries

The identity must be specific enough to support player recognition but broad enough to remain fictional and non-operational.

Possible profiles include:

- revolutionary absolutists seeking state collapse
- ultranationalist restorationists seeking a fictional territorial order
- millenarian political cults seeking purification through violence
- criminal-political networks seeking protected rule and profit
- military splinter organizations seeking government takeover
- ethno-revanchist fictional movements tied to invented claims or alternate-history identities

A profile never treats an ordinary ideology or ethnic group as inherently terrorist.

#### Coordinated attack waves

Several active states can receive incidents during one wave.

The wave should have a common public purpose, such as disrupting transport, freeing prisoners, testing government response, or retaliating for a raid.

It should not become several independent global event firings.

A successful government can break the wave by protecting key targets or capturing the coordinating cell.

#### Survivor displacement

Suppressing one cell can send survivors into another state or country.

This result is more likely after a rapid operation with low intelligence and poor border control.

It is less likely after a clean intelligence success, a protected defection channel, or a joint operation.

#### Sponsors and criminal support

An organized cell can gain one current support profile.

- foreign government sponsor
- criminal patron
- sympathetic territorial actor
- captured local revenue
- dispersed external donations
- coerced local extraction

The player must identify and address the actual profile.

Using a generic finance action against every profile should produce weak results.

#### Government content

Evolution I adds:

- joint intelligence requests
- sponsor investigation
- organization-specific targeted raids
- coordinated-wave protection missions
- defection and amnesty channels
- regional information sharing

#### AI change

Organizations should preserve their active network, relocate endangered cells, prioritize exposed transport and depots, and avoid wasting every cell in one attack.

Government AI should recognize when several incidents belong to one organization and target the shared support source.

#### Escalation proof

Organized Cells is complete when at least one fictional organization can exist across several states, receive a recognizable identity, coordinate a wave, lose cells, relocate survivors, split, collapse, and appear correctly in event reports and Event Details.

### Evolution II: Transnational Terror Network

#### Public change

Organizations establish international recruitment, transport, funding, propaganda, training, and assassination networks.

A network can act in a country where it has no permanent entrenched cell.

Weak states can become safe havens.

Several countries can face one connected crisis.

#### Network Reach

Network Reach becomes a visible global Event 31 value after this evolution.

It measures the ability of connected organizations to project attacks, move support, create distant cells, and coordinate government takeover attempts.

Network Reach rises through:

- active countries in several regions
- undisturbed safe havens
- foreign sponsors
- captured ports and transport hubs
- successful demonstration attacks
- surviving territorial actors
- coordinated propaganda victories
- government failures that create international prestige

It falls through:

- exposed sponsors
- broken corridors
- defeated safe havens
- captured records
- coordinated international operations
- rival splits
- loss of territorial actors

Network Reach should change what the event can do.

Low reach limits the network to neighboring states and established cells.

High reach allows distant attacks, faster cross-border spread, foreign fighters, and synchronized takeover attempts.

#### Safe havens

A safe haven is a country or territorial actor that permits the network to train, rest, store supplies, or direct foreign operations.

A safe haven can arise through state weakness, government complicity, an uncontrolled border region, or a territorial Event 31 actor.

The host receives political and military consequences.

Foreign powers can demand action, offer aid, conduct a raid where lawful and reachable, manipulate the network, or redirect it toward a rival.

A safe haven is not automatically a Muslim-majority country or a refugee area.

#### Distant demonstration attacks

A high-reach network can attack an eligible country without a permanent cell.

The attack creates Traces or Local Cells only if survivors, copycats, or support links remain.

A distant attack should be rarer and more expensive for the network than an attack from an entrenched local cell.

#### Foreign fighters

The network can recruit fictional foreign fighters after establishing reach and a viable route.

Foreign fighters add manpower and experience to territorial actors and can strengthen cells in another country.

They use existing unit types and do not create a custom battalion.

Disrupted routes, poor supply, rival factions, and government cooperation reduce their value.

#### Cross-border takeover planning

Several organizations can coordinate coups, civil wars, or state seizures across neighboring countries.

The player should see evidence and emergency missions before the largest attempt unless intelligence capacity has completely collapsed.

A coordinated takeover is a major public event and can raise Chaos directly.

#### Foreign-power choices

Foreign governments can:

- support counterterror forces
- exchange intelligence
- protect a border corridor
- sanction a public sponsor
- demand action from a safe-haven host
- conduct a limited intervention
- covertly manipulate a network
- redirect support toward a rival

Manipulation carries a serious blowback risk.

A state that uses the network against a rival can become a later target or public sponsor.

#### AI change

Networks should compare safe-haven security, route distance, local pressure, sponsor reliability, and government weakness.

They should not attack every possible country merely because Network Reach is high.

Governments should prioritize corridors and safe havens that materially support their active cells.

#### Escalation proof

Transnational Terror Network is complete when one organization can connect several countries, maintain a safe haven, conduct a distant attack, move support, lose a corridor, suffer sponsor exposure, and coordinate a cross-border crisis without duplicating national response systems.

### Evolution III: Territorial Insurgency

#### Public change

Strong organizations hold towns, border regions, isolated states, training areas, or captured capitals.

They form territorial countries with divisions, leaders, economy, decisions, focus routes, diplomacy, and survival goals.

#### Baseline relationship

Baseline can already create a temporary extremist country.

Evolution III changes quality and durability.

After the evolution:

- territorial actors are more likely to receive contiguous viable territory
- captured formations and equipment are more organized
- reinforcement systems are stronger
- several actors can coordinate or merge
- safe-haven support becomes more reliable
- neighboring countries receive more intervention choices
- territorial victory strengthens cells abroad
- defeat produces a wider network collapse

#### Territorial control

Territorial countries manage Territorial Control, Network Authority, and External Supply.

Territorial Control reflects administration and military grip over held states.

Network Authority reflects the actor's ability to command cells and claim leadership.

External Supply reflects sponsors, corridors, ports, captured depots, and connected territory.

These values should appear in the actor's decision category and affect force growth, focus access, diplomacy, and collapse risk.

#### State seizure

An organization needs an Armed Insurgency or Lost Local Control state, adequate local strength, a viable carrier identity, and a parent country able to survive the split or undergo a valid takeover.

Territory should normally form a contiguous enclave.

The first seizure should avoid a random isolated state when a connected area exists.

The parent keeps at least one viable core state unless the result is a government takeover.

#### Military and police defection

Defections can transfer a bounded portion of units, equipment, commanders, and local control.

The transfer should reflect actual units and stockpiles.

It must not create advanced equipment or an entire army from nothing.

#### Parent missions

The parent country gains:

- Retake the Lost State
- Restore Civil Authority
- Secure Relief Corridor
- Isolate the Enclave
- Expose the Sponsor
- Negotiate Local Surrender when valid

#### Regional reactions

Neighbors can intervene, blockade, support the parent, sponsor the actor, accept refugees, protect a border, or exploit the conflict.

The response depends on ideology, relations, rivalry, faction, claims, border access, and fear of spread.

#### Actor survival outcomes

A territorial actor can:

- be defeated
- negotiate surrender
- remain a frozen enclave
- merge with another Event 31 actor
- split through rivalry
- conquer the parent
- become a sponsor and safe haven
- enter the fictional jihadist branch after Evolution IV

#### AI change

Territorial AI should defend supply and capitals, secure contiguous states, raise existing unit types, avoid suicidal fronts, support connected cells, and seek a sponsor when isolated.

It should attack the parent or adjacent strategic states before distant prestige targets.

#### Escalation proof

Territorial Insurgency is complete when a created actor can survive for a meaningful campaign period, raise forces through real resources, use a focus route, support cells abroad, lose supply, split, merge, conquer its parent, and be cleanly defeated.

### Evolution IV: The Jihadist International

### Public change

One fictional jihadist current emerges from the wider network and attempts to bind several organizations into an international movement.

It declares secular governments, rival Muslim movements, nonbelievers, and Muslim governments that reject its authority to be enemies.

The branch is specific to Event 31 and appears only after Evolution IV.

#### Representation rules

The movement must remain fictional.

Its name, leaders, flag, emblem, doctrine, institutions, and territorial claims are invented.

It must not use the name, iconography, slogans, uniforms, sacred calligraphy, or propaganda of a real organization.

Its leaders cannot be generated caricatures of a real ethnicity or religious community.

The movement's claim to religious authority is publicly contested.

Muslim clerics, communities, governments, soldiers, and rival movements can condemn it, organize resistance, protect civilians, dispute its claims, and fight it.

Religious opposition must change gameplay through legitimacy, defections, local support, resistance, recruitment pressure, and diplomacy.

#### International Unity

International Unity becomes visible after this evolution.

It measures cooperation among jihadist organizations and territorial actors.

It rises through:

- shared offensives
- recognized leadership
- successful mergers
- captured symbolic capitals
- foreign-fighter flows
- victories over rival governments
- common enemies
- defeat of internal challengers

It falls through:

- doctrinal rivalry
- competing leaders
- sponsor conflict
- defeat
- loss of territory
- religious and civic rejection
- exposed atrocities
- unequal distribution of supplies
- failed offensives

High unity unlocks coordinated wars, common faction behavior, and the path to Evolution V.

Low unity creates splinter wars and weakens foreign-cell control.

#### Faction and coordination structure

The movement can create an event-owned faction or coordination structure.

Only Event 31 jihadist actors can become full members.

Ordinary Muslim-majority governments cannot join through generic ideology logic.

Cannibal actors cannot join under any condition.

Membership requires a compatible Event 31 route, a minimum authority contribution, and no active rivalry that blocks cooperation.

Members can refuse a leader, compete for authority, leave, split, or fight one another.

#### Priority enemies

The movement initially prioritizes:

- its parent country
- adjacent weak governments
- states controlling its claimed fictional core areas
- Muslim-majority governments it labels false regimes
- rival jihadist factions
- Event 14 cannibal actors when practical
- governments actively dismantling its safe havens or foreign routes

The Muslim-majority classification is used only for actor-specific reaction and enemy priority after this evolution.

It never affects ordinary Event 31 vulnerability or recruitment.

#### Captured territory

Captured states can face forced rule, expulsions, destruction, prison systems, coerced extraction, and mass killing.

These actions cause real population loss and can add Condemnation.

They also damage long-term control and can create resistance, defections, and foreign intervention.

The route should not reward atrocity without a strategic cost.

#### Muslim opposition content

Eligible governments and communities can receive:

- public rejection by fictional religious councils and local leaders
- protection of worship and community sites
- local defense and civil-protection committees
- safe passage for threatened civilians
- defection appeals to foreign fighters and low-level members
- regional conferences against the movement's authority claim
- joint military operations
- public documentation of forced rule and atrocities

These actions can lower the movement's International Unity and Network Authority.

#### Rival jihadist factions

Not every jihadist actor accepts one leader.

Rival factions can fight over doctrine, territory, sponsors, prisoners, and recognition.

The government can exploit the split, but the conflict can also increase civilian deaths and create new splinters.

#### AI change

Jihadist AI should pursue its parent, adjacent strategic territory, rival Muslim governments, internal rivals, and network objectives according to strength and access.

It should not launch distant wars it cannot supply.

Muslim-majority government AI should treat the movement as an actor-specific threat and prioritize protection, rejection, border defense, and coalition support according to capacity.

#### Escalation proof

The Jihadist International is complete when the fictional movement can form, receive distinct assets and leaders, recruit foreign fighters, create several actors, unite or split, attack rival Muslim governments, face Muslim religious and military opposition, and interact with Condemnation and Deaths without changing baseline target rules.

### Evolution V: The Final Jihad

#### Public change

Jihadist countries and connected networks attempt global political and military unification behind an apocalyptic leadership.

Cells become coordinated uprisings during major offensives.

Territorial actors merge or enter a shared command.

Governments with severe Terror Pressure face higher takeover risk.

#### Final command

A dominant leadership is selected from existing jihadist actors through Network Authority, territory, victories, capitals, International Unity, and surviving organization strength.

The final command can be contested.

A failed leadership contest can delay unification, start a jihadist civil war, or create two rival global fronts.

#### Coordinated uprisings

When a member launches a major offensive, high-pressure countries can receive synchronized uprisings behind existing cells.

An uprising requires real prior pressure or an established cell.

The evolution does not create an unsupported rebel army in every country.

The strength of each uprising scales with:

- Terror Pressure
- active state stages
- local captured equipment
- military defections
- connected corridors
- Network Reach
- nearby territorial actors
- government legitimacy and readiness

#### Global conquest campaign

The shared command sets strategic goals.

- secure connected regional blocs
- capture member and enemy capitals
- preserve foreign-fighter corridors
- destroy rival Muslim governments
- eliminate cannibal rivals
- break major counterterror coalitions
- raise International Unity
- create the territorial proof needed for the terminal branch

#### Recruitment and strength

The movement gains strength from instability, occupied population, captured depots, controlled industry, safe havens, foreign fighters, and connected high-pressure states.

Deaths alone do not generate free manpower.

Civilian suffering can raise fear and chaos, but force growth still requires population, equipment, supply, or defections.

#### Government response

Governments gain emergency coalition, capital defense, corridor, resistance, defection, and intervention content.

A country with high Response Legitimacy should have stronger local resistance and weaker uprising conversion.

A country with low legitimacy can face faster seizure even with a large army.

#### False Revelation eligibility

Evolution V makes The False Revelation eligible for later readiness testing.

It does not fire the world-end branch.

The branch still requires:

- World Collapse Chaos
- an enabled public branch toggle
- substantial territorial success
- widespread active crises
- high International Unity
- a major strategic victory
- hidden Apocalyptic Readiness
- no existing world end
- its own delayed trigger

#### AI change

Final-command AI should coordinate fronts, support uprisings where they can matter, preserve supply, avoid isolated prestige wars, merge actors when the transaction is safe, and suppress internal rivals that threaten command.

Government AI should prioritize capital continuity, connected coalition defense, restoration of high-pressure states, and destruction of the network's command and supply structure.

#### Escalation proof

The Final Jihad is complete when existing networks can support synchronized uprisings, territorial actors can merge or coordinate, the movement can run global objectives, governments can form an effective response, and the terminal branch remains separately gated.

### Evolution log requirements

Each evolution records one shared evolution entry with:

- Event 31 as the source event
- the accepted evolution name
- the evolution stage and tier
- the relevant actor when the milestone belongs to one country or territorial organization
- the actual date
- enabled state

The main Evolutions history and the selected event's related-evolution history show the real log metadata.

The Event Details evolution catalog shows the public premise without a fake date or sequence number.

A disabled evolution does not produce a record or set content flags.

### Cross-evolution continuity

Existing organizations should be upgraded in place when possible.

A named Organized Cells actor can become transnational, territorial, jihadist, and part of the final command without losing its history.

A local baseline actor can remain secular or regionally focused after Evolution IV.

The jihadist branch does not convert every Event 31 organization.

Rival secular, criminal-political, nationalist, cult, and military-splinter actors can survive and fight the international movement.

This diversity prevents one late evolution from erasing the rest of Event 31.

### Completion standard

The evolution package is complete only when:

- baseline territorial escalation remains playable without any evolution
- each evolution changes a real system and public incident pool
- evolution pacing responds to campaign state
- evolved openings do not replay lower stages as immediate spam
- disabled evolutions leave a safe baseline route
- existing actors upgrade without losing history
- the jihadist branch remains fictional and limited to Evolution IV and later
- Evolution V does not automatically fire The False Revelation
- evolution records appear correctly on every relevant log surface

---

## Part 5: Territorial insurgency and country packages

### Country-package purpose

A territorial Event 31 actor must be a real playable country package.

It needs viable territory, a capital, a political identity, a fictional leader or council, starting forces, equipment, technology, economy, decisions, focus routes, reinforcement, diplomacy, AI, defeat behavior, and visible assets.

A flag and a handful of militia divisions are not enough.

The package should still be reusable because several countries can appear in one campaign.

It should adapt to the organization's profile, region, origin, evolution, and current territory.

### Territorial actor profiles

#### Local Cell State

A small actor formed from one isolated or border state.

It has limited administration, improvised units, weak supply, and a narrow survival goal.

It normally seeks a sponsor, a corridor, more territory from the parent, or a negotiated enclave.

#### Regional Insurgent State

A stronger actor formed from several connected states or a large civil-war share.

It has a functioning command, captured industry, a recruitment system, and a route toward regional domination or settlement.

#### Transnational Network State

A territorial safe haven that directs cells across borders.

It values ports, border corridors, training areas, intelligence, foreign sponsorship, and Network Reach.

Its domestic administration can remain weak while its external network is strong.

#### Jihadist International State

A territorial actor that enters the Evolution IV fictional jihadist route.

It combines forced rule, foreign fighters, international coordination, rivalry over religious authority, and conflict with Muslim governments and other enemies.

#### Final Revelation State

The world-end actor led by the ambiguous entity.

It is a terminal transformation of existing jihadist power, not an ordinary baseline country spawn.

Its abilities and presentation are defined in Part 8.

### Organization identity generation

Each actor receives a stable fictional package identity when its parent organization becomes durable.

The identity draws from:

- broad region
- leadership form
- strategic profile
- ideology family
- current evolution
- territorial origin
- sponsor or rivalry history
- takeover or secession origin

Possible leadership forms include:

- clandestine directorate
- war council
- ideological secretariat
- military command
- revolutionary committee
- territorial emirate for the fictional jihadist branch
- divided coalition
- charismatic fictional leader
- institutional council

Names should sound plausible inside the alternate-history campaign without copying real organizations.

No name should combine a real community, religion, ethnicity, or nationality with terrorism as a generic label.

The final identity must remain stable through state gains, losses, save reload, and ordinary focus progression.

Route transformations can add a cosmetic name and flag while preserving the actor's event lineage.

### Territory-seizure requirements

A normal territorial seizure requires:

- at least one Armed Insurgency or Lost Local Control state
- sufficient Terror Pressure
- an organization with an active local base
- evidence of local armed strength, defection, captured equipment, or collapsed government control
- a viable country carrier
- a valid capital state
- a parent country that can retain viable territory or undergo a full takeover

The first territorial package should prefer a contiguous enclave.

A noncontiguous package is allowed only when the movement has separate established strongholds and the actor can maintain them through ports, corridors, or an existing war.

Wastelands, invalid empty states, isolated meaningless regions, and occupied enemy territory outside the crisis cannot be transferred simply to enlarge the actor.

### Parent-country survival

A secession should leave the parent with at least one owned and controlled core state, a capital or valid replacement, and a viable path to continue the conflict.

When that is impossible, the event chooses between:

- a government takeover
- a capital crisis with a smaller rebel enclave
- a civil war division that preserves both sides
- a negotiated autonomous actor
- postponing territorial creation until a valid map exists

The engine should not create a one-state parent with no capital, no supply, and no army merely to preserve a formal split.

### Capital selection

The actor's capital should normally be:

- a controlled state inside its founding territory
- populated
- connected to its main territory
- defensible enough to serve as a command center
- supported by infrastructure or local administration
- distinct from a frontline tile when a safer valid alternative exists

A captured national capital can become the actor's capital only when the takeover branch supports it.

A local or regional actor can rename a fictional administrative center through scripted localisation when the route and state identity support it.

No invented city name should overwrite a well-known real city without a route-specific reason and player-facing event.

### Carrier and identity transaction

The implementation must use the shared country-carrier registry and release transaction patterns.

Before assigning a carrier, the implementation needs a collision audit across:

- vanilla countries
- active Chaos Redux countries
- protected Event 006 and Soviet Collapse carriers
- installed Workshop references
- other local mods included in the project audit scope
- active Event 31 actors

A carrier must preserve origin, parent, organization, region, route, and package identity.

A carrier is cleared only after its actor is fully defeated, annexed, merged, or transformed and every reference has been cleaned.

Two active organizations cannot silently share one carrier.

### Political identity

Ordinary Event 31 territorial actors use an event-owned extremist political identity.

The political package should distinguish leadership and route without treating a vanilla ideology as a direct synonym for terrorism.

The ruling identity can be represented through a dedicated subideology, event-owned politics, party names, cosmetic names, and route-specific AI.

Possible route families include authoritarian military command, revolutionary absolutism, criminal-political rule, millenarian cult government, fictional ultranationalist restoration, and the later jihadist current.

The exact political presentation should fit current Chaos Redux ideology infrastructure and avoid a new ideology family unless the live repository proves it is necessary.

### Leaders and portraits

Every visible Event 31 leader is fictional or institutional.

The portrait source classification is therefore `fictional_high_chaos` for one-person leaders and fictional institutional for councils.

Portraits are produced through `chaosx_portrait_creator` with native ImageGen.

Requirements:

- full `156x210` country-leader framing
- period-appropriate clothing and photographic treatment
- one memorable invented motif tied to the actor's route
- no real-person resemblance target
- no ethnic caricature
- no real extremist insignia
- no modern tactical equipment
- no readable generated text
- matching gender and name metadata
- stable runtime identity

Institutional councils can use a staged group only when the accepted portrait brief authorizes it. A symbolic empty-chair, masked council chamber, or seal portrait can be used when it reads clearly at leader size and does not become a generic placeholder.

Leadership succession must be planned.

A territorial actor should not become leaderless when a fictional commander dies, defects, loses a power struggle, or merges into another actor.

### Flags and emblems

Every flag uses ImageGen under the flat flag-design workflow.

The design must be:

- fictional
- flat
- readable at normal, medium, and small sizes
- free of fabric folds, scenery, gradients, perspective, and fake lettering
- free of real extremist symbols
- free of sacred calligraphy used as hostile branding
- distinct between base, route, jihadist, merger, and final identities

A coordinated family can share geometry or a color relationship.

Ideology and route variants must remain genuinely distinct designs, not simple recolors.

The same symbol can appear on a faction emblem, focus icon family, and country flag only when each asset is independently designed for its surface.

### Starting ideas

A new actor should begin with no more than three deep ideas.

#### Improvised Command

Starting role:

- weak coordination
- limited planning
- militia fragmentation
- unreliable officer structure

Mitigation paths:

- Shadow Council route improves concealment and coordination
- War Directorate centralizes field command
- Ideological Secretariat improves obedience and recruitment

Failure forms:

- rival commanders
- purges
- splinter warfare

Final forms vary by route.

#### Captured Economy

Starting role:

- disrupted factories
- stolen or improvised supply
- dependence on captured stockpiles
- poor repair capacity

Mitigation paths:

- controlled extraction
- criminal and smuggling economy
- foreign sponsorship
- civil administration and taxation
- captured industrial reconstruction

Failure forms:

- looting spiral
- famine and collapse
- sponsor dependency

#### Contested Legitimacy

Starting role:

- population resistance
- weak recognition
- parent-government claims
- unstable local compliance

Mitigation paths:

- coercive rule
- service provision
- ideological mobilization
- foreign recognition
- merger into a larger Event 31 structure

Failure forms:

- local revolt
- defections
- negotiated surrender
- leadership split

The focus tree and decisions should replace or transform these ideas.

The actor must not finish the campaign with the starting negative stack unchanged.

### Country values

Territorial actors manage three visible values.

#### Territorial Control

Measures administration, garrison reach, local compliance, and secure control of held states.

Low control raises resistance, defection, sabotage, and collapse risk.

High control unlocks taxation, recruitment, construction, and integration.

#### Network Authority

Measures the actor's influence over cells, foreign fighters, splinters, and other territorial organizations.

High authority improves overseas support and merger leadership.

Low authority creates rivalry and limits external operations.

#### External Supply

Measures sponsors, captured depots, smuggling corridors, ports, foreign assistance, and protected transport.

It affects equipment replacement, fuel, force growth, and foreign operations.

These values should be shown in a normal decision category with clear stages and concise tooltips.

No dedicated country mechanic window is required.

### Starting research and technology

A local cell state begins with `2` research slots.

A regional insurgent state begins with `3` research slots.

A transnational or jihadist state can reach `4` through administration and captured institutions.

The final world-end state can reach `5` as part of its terminal package.

The actor receives a safe union of compatible technologies from its parent and actual donors.

Technology grants should reflect:

- the parent's researched equipment
- captured military units and stockpiles
- controlled industry
- defecting officers and scientists
- current date
- sponsor support

The actor does not receive every parent technology automatically.

Mutually exclusive industry and doctrine branches must remain valid.

No advanced custom technology is granted merely because the actor formed.

An actor that captures a real research center or receives a sponsor project can gain a bounded research bonus or later technology through play.

### Starting forces

Starting force size depends on territory, population, captured units, state activity, defection, and evolution.

The following values are balance anchors.

| Actor profile | Typical starting formations |
| --- | --- |
| Local Cell State | `4` to `8` militia or irregular infantry divisions |
| Regional Insurgent State | `8` to `16` mixed infantry and mobile formations |
| Transnational Network State | `12` to `24` formations with stronger support and reserves |
| Jihadist International State | `15` to `30` formations, scaled by real territory and foreign-fighter routes |
| Final Revelation State | merged surviving formations plus pressure-scaled uprisings |

The actor uses existing combat battalions and support companies.

Suggested templates can include:

- light militia infantry
- captured regular infantry
- mobile raiding infantry using available trucks
- defensive urban infantry
- border and mountain infantry when the territory supports it

No new Event 31 battalion is required.

No template receives equipment that the actor cannot obtain.

Formations should spawn in controlled states with supply and avoid immediate encirclement when a safer valid state exists.

### Equipment and manpower

The starting package draws from:

- a bounded share of captured parent stockpile
- equipment held by defecting units
- local arms and support equipment created by the event's abstract buildup
- sponsor transfers already established in the chain
- controlled factories and production lines

The actor receives enough basic equipment to make its starting divisions functional.

It should not receive years of reserve stockpile or top-tier equipment without a source.

Manpower comes from controlled population, existing armed cells, defectors, foreign fighters, and recruitment decisions.

Deaths do not convert directly into manpower.

Force growth must remain connected to population, equipment, supply, and Territorial Control.

### Reinforcement pathways

A fighting actor needs several future force paths.

- recruit local militia from controlled population
- absorb armed cells after a state seizure
- integrate defecting police or military units
- capture depots and production lines
- receive sponsor equipment
- attract foreign fighters after Evolution II or IV
- convert militia into regular formations through the military route
- raise emergency defenders during a parent offensive
- inherit bounded forces during an actor merger

Every pathway has a cost, cooldown, resource source, or control requirement.

No repeatable free-unit loop is allowed.

### Industry and construction

The actor inherits the real buildings in controlled states, including damage.

The starting economy should reflect disruption.

A local actor can have weak construction and production penalties until it stabilizes administration.

The economy routes can:

- repair captured factories
- protect depots
- rebuild railways and infrastructure
- expand controlled extraction
- establish coerced requisition
- create a criminal trade network
- accept sponsor construction
- build a civil tax administration
- fortify border corridors
- improve ports or airbases when they exist

Rewards should be state-based when possible.

A landlocked actor should not receive a token naval branch or free dockyards.

### Air force

No actor receives a free air force by default.

An air capability can arise through:

- captured aircraft at a controlled airbase
- defecting pilots
- sponsor transfers
- repaired local production
- later focus and decision investment

The actor should begin with no aircraft when no source exists.

A developed territorial actor can use reconnaissance, interception, transport support, or ground support according to equipment.

No unique Event 31 aircraft model is required.

### Navy

No actor receives a free navy by default.

A coastal actor can begin with convoys needed for supply and can later acquire limited patrol or escort capacity through captured ports, defections, purchases, or sponsors.

Capital ships require a real defection or capture event and should remain rare.

A landlocked actor has no naval branch.

### Intelligence agency

A formal intelligence agency is optional.

It should be created only for a durable transnational, jihadist, or final actor that can use operations meaningfully.

Local actors use decisions and hidden network values instead of receiving an agency for flavor.

### Advisors and commanders

Durable actors can receive fictional advisors and commanders tied to route identity.

Useful roles include:

- field commander
- quartermaster
- captured-industry administrator
- foreign liaison
- internal security chief
- ideological organizer
- civil administrator
- smuggling coordinator
- faction negotiator

Advisors should unlock through focuses or events and change play.

They should not be added as decorative portrait workload.

Each authorized visible character needs its own portrait requirement.

### Diplomacy

A territorial actor can:

- seek recognition
- seek a sponsor
- join an Event 31 coordination structure
- merge with a compatible actor
- support cells abroad
- negotiate with the parent
- accept a ceasefire
- exchange prisoners
- enter a proxy relationship
- fight rival Event 31 actors
- fight Event 14 cannibals
- enter the fictional jihadist faction after meeting its route conditions

It cannot join the cannibal faction or treat cannibal actors as natural allies.

Normal factions should use strict acceptance based on ideology, sponsor interest, war, and international cost.

A major power can exploit an actor without granting full faction membership.

### Actor mergers

A merger requires:

- compatible route or a successful leadership contest
- connected or supportable territory
- clear carrier ownership
- valid capital and army transfer
- safe handling of wars, subjects, factions, leaders, ideas, and equipment
- player consent when a player-controlled actor would be absorbed

The merger preserves history and records which organization became dominant.

A weaker actor can become a regional command, subject, faction member, or annexed territory according to the route.

A merger should not duplicate units, equipment, technology, or country ideas.

### Actor splits

A split can follow:

- leadership death
- low Network Authority
- failed merger
- unequal sponsor support
- doctrinal conflict
- military defeat
- resistance in a distant enclave
- jihadist leadership rivalry

The split uses valid territory and carrier availability.

It should not fire when no second viable actor can exist.

### Takeover of the parent

A victorious actor can replace the parent government.

The takeover should:

- preserve valid country ownership and capital
- replace or transform the country identity
- integrate surviving actor forces once
- reconcile technologies and stockpiles safely
- remove obsolete parent response decisions
- create resistance and legitimacy consequences
- open the Event 31 focus route suited to the takeover
- preserve foreign wars and diplomatic consequences where valid

The actor does not gain instant full cores or loyalty over every parent state.

Large or culturally divided states require staged consolidation.

### Defeat and cleanup

A defeated actor enters one of these outcomes.

#### Military destruction

Territory returns to the parent or valid controller.

Surviving cells can remain dormant according to pressure and legitimacy.

#### Negotiated surrender

The actor disarms under terms and the parent begins reintegration.

Hardliners can reject the settlement and remain as a smaller cell.

#### Leadership decapitation and fragmentation

The actor loses central authority and splits into local cells or rival remnants.

#### Foreign evacuation

Leaders and selected units escape to a sponsor or another Event 31 actor.

#### Merger under pressure

The actor is absorbed by a stronger organization before defeat.

Cleanup must remove:

- country-specific decisions and missions
- active actor values
- invalid cell links
- temporary occupation and supply modifiers
- obsolete focus access
- world-threat source contribution when no qualifying actor remains
- carrier ownership after every consumer is cleared

It preserves Deaths, Condemnation, event history, lasting state damage, and surviving dormant cells.

### Special-country classification

Every territorial Event 31 actor and takeover identity is a special Chaos country.

It should be added to the shared `is_special_chaos_country` classification through a generic Event 31 actor marker.

It is not an actual nonhuman country.

The Final Revelation state remains a human-populated extremist country led by an ambiguous entity, so it also stays outside `is_actual_nonhuman_country` unless a later accepted design explicitly transforms the population.

### Asset and model boundary

The actor package requires flags, portraits, focus icons, idea icons, decision icons, a category picture, faction emblems, report art, and super-event art where relevant.

It does not require:

- a custom combat battalion
- a custom equipment archetype
- a 3D unit model
- a custom building model
- custom unit audio
- a bespoke unit counter

Existing HOI4 units and equipment are sufficient for the design.

This is an accepted scope decision, not a temporary fallback.

### Completion standard

A territorial country package is complete only when:

- the territory and capital are valid
- the parent remains viable or undergoes a valid takeover
- the carrier is collision-safe and origin-aware
- the actor has a stable fictional identity
- leader, flag, parties, ideas, and localisation agree
- the actor has functioning starting forces and equipment
- research slots and technology fit the actor profile
- economy, supply, air, and navy setup follow real territory and sources
- force growth requires resources and control
- the focus tree and decisions are playable
- AI can survive, expand, negotiate, split, merge, and lose
- defeat and annexation clean every active surface
- the actor is special Chaos but not nonhuman

---

## Part 6: Focus tree and political routes

### Tree purpose

Every durable Event 31 territorial actor uses a shared event-owned focus framework that adapts to its organization profile, region, origin, evolution, territory, sponsor, and leadership.

The shared framework must not make every actor read and play the same.

Scripted localisation, route availability, leader pools, decisions, state targets, AI, icons, rewards, country identities, and diplomatic goals should reflect the actor package.

A small local enclave can use a reduced version of the tree.

A regional, transnational, jihadist, or takeover actor receives the full route structure.

### Starting problems

The tree opens around three existing country problems.

- Improvised Command
- Captured Economy
- Contested Legitimacy

The opening should show the player that the actor must survive, organize, and choose how to rule.

It should not expose every late route on day one.

The first focus or compact opening group should reveal three early commitments.

- build a covert and distributed command
- centralize military rule
- centralize ideological authority

Industry, military, diplomacy, and expansion branches open from the stabilization stage and change according to that commitment.

### Architecture map

```text
Founding Crisis
|
+-- Hold the Enclave
|   +-- Restore Supply
|   +-- Secure the Command Center
|   +-- Define the Leadership
|
+-- Leadership Family
|   +-- Shadow Council
|   +-- War Directorate
|   +-- Ideological Secretariat
|
+-- Captured Economy
|   +-- Smuggling and External Supply
|   +-- Coerced Extraction
|   +-- Civil Administration
|   +-- Foreign Sponsorship
|
+-- Armed Movement
|   +-- Local Militia
|   +-- Defectors and Captured Formations
|   +-- Mobile Cells
|   +-- Territorial Brigades
|   +-- Foreign Fighters when unlocked
|
+-- Network and Diplomacy
|   +-- Protect Safe Havens
|   +-- Sponsor Alignment
|   +-- Rival Networks
|   +-- Merger or Confederation
|   +-- Event 31 Faction Route
|
+-- Expansion and State Capture
|   +-- Border Corridors
|   +-- Urban Seizure
|   +-- Break the Parent Government
|   +-- Absorb Compatible Enclaves
|   +-- Consolidate Captured Territory
|
+-- Crisis and Failure Routes
|   +-- Leadership Split
|   +-- Local Revolt
|   +-- Negotiated Enclave
|   +-- Sponsor Dependency
|
+-- Hidden Evolution Routes
    +-- Jihadist International after Evolution IV
    +-- Final Jihad after Evolution V
    +-- False Revelation terminal route after readiness
```

The final implementation chooses exact focus count and coordinates.

The branch map and route logic are fixed.

### Opening survival group

#### Founding crisis

The opening establishes how the actor formed, where its capital is, what equipment it captured, which parent it fights, and which starting idea is most dangerous.

A takeover actor controls the old government, so its text and requirements must differ from those for a secession enclave.

#### Hold the enclave

This group improves immediate defense, supply, and command continuity.

It can unlock:

- emergency recruitment decisions
- protection of the capital and depots
- one limited construction or repair project
- local stockpile accounting
- first commander appointment
- a temporary defensive mission

Rewards should be immediate and concrete.

The group should not create several new national spirits.

#### Define the leadership

This is the first real route lock.

It opens one of the three main authority families.

The choice changes decision costs, idea upgrades, AI, diplomacy, military organization, merger behavior, and eventual identity.

### Leadership family: Shadow Council

#### Narrative role

A concealed collective leadership treats secrecy, compartmentalization, intelligence, and distributed control as the foundation of survival.

#### Mechanical role

The route improves Network Authority, intelligence resistance, cell support, foreign operations, and survival after territorial loss.

It gives weaker direct field-command bonuses than the War Directorate.

#### Main focus groups

- compartmentalize the command
- establish regional cells
- protect communications and couriers in abstract form
- control information and internal access
- build a counterintelligence office
- prepare continuity after capital loss
- direct foreign cells
- manipulate rivals and sponsors

#### Decision integration

Unlocks:

- support a dormant foreign cell
- relocate a threatened cell
- false-lead and sponsor manipulation incidents
- protect organization leadership
- exploit government intelligence failure
- preserve Network Authority after losing territory

#### Idea lifecycle

Improvised Command becomes Distributed Command and can later become Network Directorate.

Failure through low authority or exposed records creates Compromised Network.

#### Tradeoff

The actor gains resilience and reach but has weaker conventional command, lower Territorial Control, and a higher risk of internal cells acting independently.

#### AI profile

Preferred by actors with little territory, high Network Reach, strong intelligence capability, several foreign cells, or a powerful enemy parent.

Avoided by actors fighting an immediate conventional war with no safe haven.

#### End state

A durable covert state that can survive territorial setbacks, control foreign networks, and lead a transnational coordination structure.

### Leadership family: War Directorate

#### Narrative role

Military commanders centralize the movement into a conventional territorial army and security state.

#### Mechanical role

The route improves planning, organization, reinforcement, depot protection, conventional divisions, and rapid state seizure.

It sacrifices some secrecy, legitimacy, and foreign-cell flexibility.

#### Main focus groups

- establish unified field command
- integrate defecting officers
- standardize captured formations
- secure depots and railways
- create a general staff
- fortify the territorial core
- plan the parent offensive
- subordinate local commanders

#### Decision integration

Unlocks:

- convert militia into regular infantry
- raise emergency territorial brigades
- seize and repair depots
- prepare state offensives
- compel rival commanders to submit
- establish military occupation zones

#### Idea lifecycle

Improvised Command becomes Unified Field Command and can later become Directorate General Staff.

Failure through defeat or low legitimacy creates Rival Warlords.

#### Tradeoff

The actor gains strong conventional power and control while becoming easier to identify, more dependent on supply, and more vulnerable to defeat of its field army.

#### AI profile

Preferred by actors with several connected states, captured regular units, adequate supply, and a weaker parent.

Avoided by tiny isolated enclaves with no equipment base.

#### End state

A centralized insurgent military state able to conquer the parent or dominate a regional alliance.

### Leadership family: Ideological Secretariat

#### Narrative role

An ideological leadership builds authority through doctrine, internal discipline, political institutions, and mobilization.

#### Mechanical role

The route improves recruitment, obedience, resistance to surrender, political control, and route-specific identity.

It creates stronger purges, faction conflict, and atrocity risk when pushed toward absolutism.

#### Main focus groups

- codify the movement's doctrine
- establish political schools and local committees
- control appointments
- mobilize supporters
- absorb or purge rival currents
- build a territorial administration
- define the new state identity
- claim leadership over aligned organizations

#### Decision integration

Unlocks:

- ideological mobilization
- internal loyalty campaigns
- recruit local committees
- purge or reconcile a splinter
- change party and cosmetic identity
- claim authority over a compatible actor

#### Idea lifecycle

Improvised Command becomes Cadre Authority and can later become Ideological State.

Failure through low legitimacy or rivalry creates Purge Spiral or Doctrinal Schism.

#### Tradeoff

The actor gains recruitment and obedience while risking internal purges, civilian resistance, diplomatic isolation, and weaker technical administration.

#### AI profile

Preferred by actors with strong local recruitment, a charismatic fictional leader, high pressure, or an evolution-specific doctrine.

Avoided by purely criminal-political actors unless they transform deliberately.

#### End state

A consolidated ideological regime able to absorb related movements or enter the hidden jihadist branch when eligible.

### Captured Economy branch

The economy branch supports the chosen leadership and should be geographically grounded.

It has four approaches that can coexist in limited form, with one becoming dominant.

#### Smuggling and External Supply

Focus groups:

- reopen a border corridor
- protect clandestine trade in abstract form
- secure convoys or transport
- bargain with criminal patrons
- diversify external supply
- build reserve depots

Rewards:

- External Supply
- convoys, trucks, trains, and support equipment from real routes
- sponsor and corridor decisions
- limited construction and repair

Tradeoff:

- dependency on vulnerable routes
- criminal influence
- foreign exposure

#### Coerced Extraction

Focus groups:

- requisition controlled stocks
- direct factory output
- seize agricultural and industrial supply
- impose labor and transport obligations
- expand arms production

Rewards:

- immediate equipment and factory use
- local resource extraction
- military-factory output
- emergency construction

Tradeoff:

- lower Territorial Control
- civilian deaths and flight
- resistance
- Condemnation after public atrocities

#### Civil Administration

Focus groups:

- restore utilities
- reopen local government
- establish taxation
- repair railways
- regulate markets
- create public services
- integrate captured towns

Rewards:

- higher Territorial Control
- construction and production recovery
- lower resistance
- stronger long-term recruitment
- staged replacement of Captured Economy

Tradeoff:

- slower immediate military output
- administrative and civilian-factory burden
- ideological hardliner opposition

#### Foreign Sponsorship

Focus groups:

- seek a patron
- negotiate equipment and training
- accept industrial missions
- grant basing or influence concessions
- diversify or reject dependency

Rewards:

- equipment, research, volunteers, intelligence, and industry suited to the sponsor

Tradeoff:

- patronage risk
- diplomatic exposure
- possible subject status
- sponsor demands

The branch should let a player make selective investments.

It should not require every economy focus before expansion or military progression.

### Armed Movement branch

#### Local militia

Improves immediate recruitment and defense using controlled population and basic equipment.

It unlocks militia-raising decisions with caps and cooldowns.

#### Defectors and captured formations

Integrates actual defecting units, officers, and stockpiles.

It can unlock captured regular infantry templates and commander appointments.

#### Mobile cells

Supports fast movement, state raids, foreign cells, and survival outside the territorial core.

It needs trucks, fuel, and Network Authority.

#### Territorial brigades

Builds stronger conventional formations for holding and taking states.

It needs adequate Territorial Control, equipment, and supply.

#### Foreign fighters

Appears only after Evolution II or the relevant manual scenario.

It creates a recruitment and transport system, not a custom unit type.

The route can bring experienced manpower and internal rivalry.

#### Specialist support

Artillery, engineers, reconnaissance, anti-air, and logistics support can be integrated when technology and stockpiles exist.

The branch does not grant equipment without a source.

#### Army payoff

The route ends in a force structure suited to the chosen leadership.

- Shadow Council receives distributed mobile formations and continuity
- War Directorate receives regular territorial divisions and planning
- Ideological Secretariat receives disciplined political formations and mass mobilization

### Network and diplomacy branch

#### Protect safe havens

Improves foreign-cell survival and creates aid or evacuation routes.

#### Sponsor alignment

Chooses a patron, balances several patrons, or rejects external control.

#### Rival networks

Offers infiltration, truce, proxy conflict, merger, or destruction of other Event 31 actors.

#### Merger or confederation

Creates a negotiated coordination structure when actors are compatible.

The stronger actor can lead, but player-controlled members require consent before absorption.

#### Event 31 faction route

A durable regional actor can create an event-owned coordination faction after minimum membership, compatible routes, and a shared war or threat.

The faction needs a goal and cohesion system.

It should not form because one actor completed one focus.

#### Diplomacy payoff

The actor becomes a sponsor, coalition leader, patron client, recognized enclave, or transnational command.

### Expansion and state-capture branch

#### Border corridors

Targets connected border states, ports, and transport links that support the actor's territory.

#### Urban seizure

Prepares attacks on administrative and industrial centers after local cells or pressure exist.

#### Break the parent government

Uses capital infiltration, military defection, civil war, and field offensives to defeat the parent.

#### Absorb compatible enclaves

Creates merger, subject, or faction decisions for other Event 31 actors.

#### Consolidate captured territory

Handles resistance, services, cores, claims, local administration, and postwar integration.

The actor should not gain instant full cores over every conquered state.

#### Expansion payoff

A local actor becomes a viable regional state, replaces the parent, or leads a connected Event 31 bloc.

### Crisis and failure routes

Failure routes should appear only when the relevant danger exists.

#### Leadership split

Low Network Authority, leadership death, or a failed merger can reveal a crisis branch.

The player chooses compromise, purge, decentralization, or civil war.

#### Local revolt

Low Territorial Control and public abuse can create a civilian and military revolt.

The player can reform, repress, negotiate, or lose territory.

#### Negotiated enclave

A losing actor can seek a ceasefire, autonomy, evacuation, or disarmament.

The route trades expansion for survival and can create a later return.

#### Sponsor dependency

An actor that relies on one patron can become a client state, reject the patron, or balance another sponsor.

Failure routes should have real consequences and routes back into play.

They should not become a collection of permanent penalties.

### Hidden jihadist route

The route appears only after Evolution IV and only for compatible fictional actors.

It is never a generic option for every actor or every Muslim-majority region.

#### Entry conditions

- compatible ideological route
- Event 31 actor status
- sufficient Network Authority
- one active jihadist contact or founding incident
- no route lock that rejects the doctrine
- Evolution IV enabled and recorded

#### Main focus groups

- accept or contest the international claim
- recruit foreign fighters
- challenge rival Muslim governments
- create a fictional religious authority structure
- bind territorial commands
- establish cross-border supply
- purge or reconcile rival jihadists
- impose forced rule or seek disciplined administration
- join or lead the Jihadist International

#### Internal choice

The route should include at least two incompatible methods.

- centralized apocalyptic command
- distributed international insurgency

A third limited method can focus on territorial state-building and selective alliances.

#### Muslim opposition consequences

Aggressive claims against Muslim governments trigger additional opposition events, local resistance, defections, and diplomatic coalitions.

A focus cannot erase that opposition through a flat modifier.

#### Route payoff

The actor becomes a faction member, faction leader, rival claimant, or independent jihadist state with access to Evolution V objectives.

### Final Jihad route

The route appears after Evolution V.

It requires a jihadist actor with sufficient authority, territory, and network position.

Focus groups include:

- contest the final leadership
- coordinate foreign uprisings
- prepare global offensives
- merge or subordinate member states
- preserve strategic corridors
- capture symbolic capitals
- suppress rival commands
- raise International Unity
- approach the hidden terminal readiness threshold

The route does not expose The False Revelation's hidden formula.

It can show that a final unification claim is gaining support.

### False Revelation terminal route

The terminal route is hidden until the public world-end transition begins.

After The False Revelation fires, the final state receives a replacement or overlay focus branch suited to the world-end campaign.

It includes:

- consolidate the entity's command
- trigger uprisings in high-pressure countries
- secure the final supply network
- destroy religious and civic opposition
- capture command capitals
- impose final territorial rule
- respond to global coalition counterplay

The final state should not use an ordinary nation-building tree after the terminal transition.

### Focus and decision integration

Every major branch must unlock or alter a decision family.

| Focus family | Decision and mission connection |
| --- | --- |
| Opening survival | capital defense, depot protection, emergency recruitment |
| Shadow Council | foreign cells, relocation, intelligence, continuity |
| War Directorate | unit conversion, state offensives, command centralization |
| Ideological Secretariat | recruitment, loyalty, purge or reconciliation, identity change |
| Smuggling | corridors, convoys, sponsor deals, external supply |
| Civil Administration | repairs, services, taxation, integration |
| Armed Movement | recruitment, templates, foreign fighters, force growth |
| Diplomacy | recognition, sponsorship, merger, faction actions |
| Expansion | state targeting, war preparation, postwar consolidation |
| Jihadist route | faction unity, rival claims, foreign fighters, opposition campaigns |
| Final Jihad | coordinated uprisings, global objectives, merger and command |

A branch that only adds modifiers has failed.

### Reward diversity

Focus rewards can include:

- repaired or constructed factories
- railways, infrastructure, forts, anti-air, airbases, supply hubs, and ports
- equipment production lines
- bounded stockpiles from real sponsors or captured depots
- new or upgraded division templates
- commanders and authorized advisors
- decisions and missions
- technology or research bonuses
- claims and staged cores
- leader, party, flag, and cosmetic-name changes
- faction and merger actions
- event chains
- idea upgrades and replacements
- Network Authority, Territorial Control, External Supply, Network Reach, or International Unity changes

Political power, stability, war support, and tiny modifiers can support a reward package.

They should not fill the tree.

### Idea lifecycle table

| Idea | Start | Mitigation | Route upgrade | Failure form | Final forms |
| --- | --- | --- | --- | --- | --- |
| Improvised Command | all new actors | opening survival | Distributed Command, Unified Field Command, or Cadre Authority | Compromised Network, Rival Warlords, or Doctrinal Schism | Network Directorate, Directorate General Staff, or Ideological State |
| Captured Economy | all new actors | repair, supply, administration | External Supply System, Directed War Economy, Civil Administration, or Patron Development Mission | Looting Spiral, Famine, or Sponsor Dependency | route-specific stable economy |
| Contested Legitimacy | all new actors | service, coercion, recognition, ideology | Security State, Claimed Revolutionary Authority, Recognized Enclave, or International Mandate | Local Revolt, Mass Defection, or Failed Rule | route-specific territorial identity |

No route should create a large stack of separate ideas when one lifecycle can carry the institution.

### Focus layout and visual rules

The final tree must use compact branch families and short connectors.

It must avoid crossing lines, overlapping focuses, decorative ladders, and fake nonlinearity.

The full tree should read at normal zoom.

The opening, leadership, economy, military, diplomacy, expansion, crisis, and hidden evolution regions should be identifiable without reading every tooltip.

Focus Navigation shortcuts should cover spatially separate major regions.

Suggested navigation groups:

- Leadership
- Economy
- Armed Movement
- Network and Diplomacy
- Expansion
- Crisis
- Jihadist International when revealed
- Final Jihad when revealed

Every focus needs accurate search filters matching its primary branch.

Hidden routes must not appear in navigation or filters before reveal.

A focus inlay window is not required because the actor's three values can be presented through the decision category and tooltips.

### Icon direction

Each branch needs a coordinated but distinct focus-icon family.

- Shadow Council: divided masks, sealed files, hidden radios, layered cells
- War Directorate: command tables, captured standards, field radios, fortified headquarters
- Ideological Secretariat: fictional seal, cadre assembly, printed doctrine without readable text, disciplined ranks
- Economy: depots, damaged factories, railways, convoys, market control, foreign crates
- Armed Movement: militia, defectors, captured weapons, trucks, defensive lines
- Diplomacy: sponsor hands, divided emblems, border links, negotiation table, faction seal
- Expansion: gates, city silhouettes, corridors, captured government buildings
- Crisis: fractured council, abandoned depot, local uprising, broken patron chain
- Jihadist branch: wholly fictional geometric emblem and military-political imagery with no sacred calligraphy or real extremist symbol
- Final route: fractured sky, synchronized columns, sealed command, ambiguous light without depicting a deity

Icons must be designed for the focus surface and cannot be resized decision or idea icons.

### Route-specific AI

AI route choice considers:

- actor size
- territory shape
- parent strength
- current war
- equipment and supply
- Network Authority
- Territorial Control
- External Supply
- existing foreign cells
- sponsor availability
- organization profile
- current evolution
- player and rival routes

Shadow Council should dominate among small dispersed actors.

War Directorate should dominate among large territorial actors with regular units.

Ideological Secretariat should dominate among actors with a strong fictional doctrine, recruitment base, or Evolution IV access.

AI must set invalid routes to zero when a required sponsor, border, state, faction, evolution, or enemy does not exist.

Complex route weights require the probability-auditor workflow.

### Merger and larger-state question

Event 31 does not need a generic regional formable suite.

Its larger identities arise through event-owned actor mergers, parent-country takeover, transnational confederation, the Jihadist International, and the Final Revelation state.

These transformations already provide territorial and political ambition.

Adding unrelated historical or regional formables would dilute the event and create large asset and integration work without improving its core play.

### Route coverage requirements

The final implementation report must compare these required route families with the actual tree.

| Required route family | Required payoff |
| --- | --- |
| Opening survival | viable capital, supply, forces, first decisions |
| Shadow Council | resilient covert network and foreign-cell control |
| War Directorate | conventional territorial army and parent offensive |
| Ideological Secretariat | consolidated political authority and route identity |
| Captured Economy | stable supply and production path |
| Armed Movement | sustainable force growth and templates |
| Network and Diplomacy | sponsors, rivals, mergers, or faction leadership |
| Expansion and State Capture | connected territorial growth and postwar handling |
| Crisis and Failure | playable split, revolt, dependency, or settlement responses |
| Jihadist International | fictional Evolution IV identity and faction role |
| Final Jihad | coordinated global objectives and leadership contest |
| False Revelation | terminal world-end campaign branch |

Missing, renamed, merged, simplified, or replaced routes must be reported.

### Completion standard

The focus package is complete only when:

- the shared tree remains actor-specific in text, targets, rewards, AI, and identity
- starting problems have visible lifecycles
- every major route changes play
- branches interact through values, decisions, forces, diplomacy, and territory
- route payoffs are visible
- hidden routes remain hidden until valid
- focus filters and navigation match branch ownership
- final layout is clean at normal zoom
- AI understands route validity and situation
- no filler ideology route or unrelated formable suite is added

---

## Part 7: Global Jihad triggerable scenario

### Scenario identity

- Scenario name: `Global Jihad`
- Proposed scenario ID: `SCN-014`
- Owner event: Event 31 Random Terror
- Scenario role: manual advanced crisis setup
- Intensity stops: Low, Medium, High, Maximum
- Type selector: scenario-specific deployment pattern

`SCN-014` is the next visible candidate after the supplied scenario export.

The implementation must verify the authoritative workbook and live registry before reserving it.

### Scenario purpose

Global Jihad lets the player launch the advanced fictional jihadist crisis without waiting for Event 31 selection, Chaos progression, or evolution pacing.

It should create a playable world state immediately.

The setup must include real territorial actors, active cells, government responses, foreign-fighter and supply systems, shared coordination, and valid wars or takeover crises.

It should not be a button that merely sets Evolution IV and lets the ordinary system build the crisis later.

The scenario remains separate from the random-event timer.

It does not count as a normal Event 31 firing and does not advance minor-event pacing.

### Availability

The scenario is directly launchable unless:

- a world-end state already exists
- another incompatible terminal transition is active
- the map has too few valid countries or states to create the selected intensity
- the scenario has already been launched and its active setup has not been cleared
- the carrier registry cannot provide the minimum valid actor package

The launch must not be blocked by:

- current Chaos
- current Chaos tier
- Event 31 firing history
- evolution history
- current date
- ordinary event weight
- route prerequisites
- prior super-event history

A tightly scoped scenario flag can bypass those normal prerequisites during setup.

It is cleared when setup finishes.

### Scenario type selector

#### Dispersed Networks

The scenario creates more active countries and fewer territorial actors.

Cells begin in urban, transport, border, and capital contexts across several regions.

Network Reach begins high enough for connected attacks, but territorial control remains weak.

Government players receive time to break corridors before states are lost.

#### Border Corridors

The scenario concentrates actors around connected borders, ports, rail routes, and weak neighboring governments.

Territorial actors begin smaller but have stronger External Supply and mutual support.

The scenario favors regional wars and intervention.

#### Capital Uprisings

The scenario seeds high-pressure cells in capitals and major administrative states.

Several countries begin with Prevent Capital Seizure missions, coup attempts, or short civil wars.

Territorial actors receive less remote territory and more takeover potential.

#### Territorial Fronts

The scenario creates larger contiguous extremist countries and active conventional wars.

Fewer countries begin with only hidden cells.

Governments receive retaking, blockade, relief, and coalition content immediately.

#### Random Pattern

The scenario selects a valid mixture from the four patterns while respecting intensity, carrier limits, geographic diversity, and map validity.

The UI should show the selected type and its broad world-state effect without exposing exact target formulas.

### Low intensity

#### World footprint

- one or two small extremist countries
- a limited number of countries with active cells
- weak International Unity
- limited foreign-fighter and corridor activity
- no immediate Final Jihad

#### Territorial actors

Actors normally begin as Local Cell States or small Regional Insurgent States.

They receive viable capitals, four to eight basic formations, functional equipment, two or three research slots according to profile, and weak starting economy.

#### Government condition

Affected governments begin with Local Cells or Sustained Campaign pressure.

They receive a response category and enough time to prepare.

#### Player experience

The scenario should feel like an early challenge setup.

A coordinated player coalition can contain it before a global war begins.

### Medium intensity

#### World footprint

- several extremist countries across different regions
- multiple active countries
- several uprisings or civil wars
- foreign recruitment and supply routes active
- some weak governments near State Challenge
- a functioning jihadist coordination structure

#### Territorial actors

Actors normally include Regional Insurgent States and one stronger Transnational Network State.

They receive eight to sixteen formations, captured stockpiles, three research slots, and active reinforcement decisions.

#### Government condition

Several countries begin with capital, corridor, or retaking missions.

Major powers receive optional intervention and intelligence cooperation.

#### Player experience

The crisis is already international.

Governments can still isolate regions and exploit movement rivalry before the Final Jihad.

### High intensity

#### World footprint

- large territorial footholds in several regions
- several countries already in civil war
- major powers with domestic cells and sabotage pressure
- active foreign-fighter routes
- high Network Reach
- strong International Unity
- coordinated territorial offensives

#### Territorial actors

Actors include several Regional and Transnational States and at least one plausible faction leader.

Starting formations normally range from fifteen to thirty according to real territory and equipment.

They receive four research slots only when their captured institutions and profile support them.

#### Government condition

Governments begin with immediate military, capital, and coalition objectives.

Some weak governments can begin one failure away from collapse.

#### Player experience

The world begins in a connected war.

A passive response should allow rapid spread.

A coordinated response still has clear command, corridor, legitimacy, and territorial targets.

### Maximum intensity

#### World footprint

- organized extremist countries across much of the world
- large territories under Event 31 actors
- numerous coup attempts and civil wars
- widespread active cells
- high Network Reach and International Unity
- the Final Jihad active immediately

#### Territorial actors

The setup creates the largest valid actor count the carrier registry and map can support without invalid duplication.

Actors begin with viable territory and forces scaled to their real states.

The scenario must not create a free army unrelated to population, units, equipment, or captured infrastructure.

#### Government condition

Major and regional powers receive emergency coalition and capital-defense content.

High-pressure countries can begin with synchronized uprisings.

#### False Revelation rule

Maximum intensity does not fire The False Revelation.

It can make the branch eligible for readiness once:

- Chaos reaches the normal World Collapse requirement
- the public branch remains enabled
- territorial and crisis conditions are met
- the hidden readiness threshold is reached
- the branch's delayed trigger resolves

The scenario must not bypass the `1000+` Chaos gate or world-state proof.

### Setup sequence

The scenario launch should behave as one transaction.

#### Step 1: Validate the world

Check the terminal state, carrier availability, valid countries, valid state groups, selected type, selected intensity, and minimum territorial viability.

If the selected setup cannot be built, the launch is blocked with a clear reason.

No partial setup should remain after a failed validation.

#### Step 2: Select regions and governments

Choose a geographically diverse set of valid regions and vulnerable governments.

Use war, stability, state connectivity, transport, and existing country viability.

Do not use religion, ethnicity, nationality, or refugee population as vulnerability factors.

#### Step 3: Allocate territorial actors

Create the required actor packages with valid territory, capitals, leaders, flags, parties, ideas, forces, technology, supply, and wars.

Avoid overlapping state transfers.

Preserve viable parent countries or use a takeover branch.

#### Step 4: Seed national crises

Add active cells, Terror Pressure, state activity, capital missions, corridor missions, coup attempts, or civil wars according to pattern and intensity.

Do not create duplicate Event 31 categories.

#### Step 5: Activate the advanced network

Record or provide scenario-scoped access to Evolution IV content.

Set Network Reach and International Unity to intensity-appropriate starting bands.

Create the Jihadist International coordination structure when the setup has enough valid actors.

#### Step 6: Give governments response tools

Open the compact response category for affected countries.

Give eligible foreign powers intervention, intelligence, relief, and coalition choices.

#### Step 7: Finish and clean bypass state

Record the scenario launch ledger.

Clear the setup bypass.

Start event-owned pacing for the created countries and actors.

The ordinary event system resumes under the new world state.

### Actor distribution rules

The scenario should avoid placing every actor in one continent unless Border Corridors and the available map justify it.

At Medium and above, at least two broad regions should normally receive territorial actors.

At High and Maximum, the scenario should include:

- one strong actor capable of faction leadership
- one rival or independent actor
- one vulnerable government with a major capital or corridor crisis
- one distant network region
- at least one government with a credible path to early containment

This mixture creates strategy and prevents a uniform map of identical actors.

### Government selection rules

The scenario can choose stable major powers as domestic-cell targets because the scenario is an explicit challenge setup.

It should still vary intensity.

A stable major can receive an entrenched urban network and capital mission without immediately losing half its states.

A weak government can begin with a territorial actor or civil war.

The same identity-based exclusions from ordinary Event 31 apply.

### Scenario diplomacy

The setup can establish:

- an Event 31 jihadist faction or coordination structure
- internal rivalries
- wars against parent governments
- wars against adjacent governments when the territorial setup supports them
- hostility toward Event 14 cannibal actors
- public opposition and coalition options for Muslim-majority governments
- optional major-power intervention interests

It should not place every Event 31 actor into one faction automatically.

Some actors should remain rivals, clients, or independent commands.

### Scenario AI

Government AI should immediately assess capital, supply, active-state, and territorial risks.

It should protect urgent objectives before spending on distant intervention.

Major powers should intervene only when access, capacity, relations, threat, and strategic interest support it.

Extremist AI should secure its capital and supply, coordinate with compatible actors, attack parent states, support high-pressure cells, and avoid distant unsupported fronts.

Scenario AI needs its own probability scenarios because ordinary event pacing no longer describes the opening.

### Scenario logging and Event Details

The scenario appears in the Triggerable Scenarios list with:

- stable ID
- public name
- concise premise
- selected deployment type
- selected intensity
- impact direction
- launch eligibility

The confirmation window reads the current stored type and intensity at launch time.

The launch creates a scenario history record and its own setup report.

It should not create a false ordinary random-event history row or consume Event 31 repeatable weight.

Evolutions provided by setup should appear through the scenario's accepted logging policy and must not generate duplicate evolution rows.

### Relaunch and idempotence

The scenario cannot be launched twice into the same active setup.

A completed or defeated scenario can permit a later launch only if the event-owned scenario ledger, all actor carriers, and all active setup state have been fully cleared and the implementation explicitly supports replay.

The default design is one launch per campaign.

The launch helpers must remain idempotent when ordinary Event 31 progression has already created one of the needed actors or networks.

Existing valid actors should be upgraded or counted.

They should not be duplicated.

### Save and reload

The selected type, intensity, active scenario state, actor packages, network values, faction membership, government crises, and world-end eligibility state must survive save and reload.

The setup bypass must not survive after launch completion.

### Acceptance cases

The scenario is complete only when these cases pass.

1. Low creates one or two viable small actors and limited cells.
2. Medium creates several regions, uprisings, corridors, and a functioning coordination structure.
3. High creates large territorial fronts, major-power domestic pressure, and coordinated offensives.
4. Maximum activates the Final Jihad but does not fire The False Revelation.
5. Every actor has valid territory, capital, forces, leader, flag, ideas, technology, and decisions.
6. Every parent remains viable or undergoes a valid takeover.
7. No country is selected because of religion or ethnicity.
8. The scenario type visibly changes the opening pattern.
9. The confirmation window uses the stored selection at launch time.
10. Cancel changes nothing.
11. A failed validation leaves no partial actors or transferred states.
12. Existing Event 31 actors are reused without duplication.
13. The launch does not advance random-event pacing or spend repeatable weight.
14. The bypass flag clears after setup.
15. Save and reload preserves the complete setup.

---

## Part 8: The False Revelation world-end branch

### Terminal role

The False Revelation is Event 31's public world-end branch.

It marks the transition from a global extremist war to a terminal campaign led by an ambiguous supernatural or impossible entity.

The branch must feel larger than a strong Evolution V offensive.

It changes leadership, unifies or subordinates existing actors, synchronizes uprisings, activates terminal abilities, freezes ordinary random-event progression, and gives the world a final counter-campaign.

The branch is public in Event Details and has its own persistent enable toggle.

Disabling the branch does not disable Event 31, the jihadist route, or the Final Jihad.

### Ambiguity rule

The entity appears before the extremist leadership and is proclaimed divine by the movement.

The game never confirms that the entity is Allah.

The entity can be interpreted as:

- a demon
- an alien intelligence
- a temporal anomaly
- a psychic or technological projection
- a mass hallucination
- a constructed fraud with impossible effects
- another supernatural force

The event must preserve uncertainty.

No hidden tooltip, leader biography, Event Details text, achievement, asset manifest, or final localisation should reveal a canonical answer.

The entity is an impossible fictional leader and may use native ImageGen.

Its followers' claim is part of their ideology, not a statement by the game.

### Religious representation

The world-end branch must make Muslim opposition visible and consequential.

Fictional Muslim religious authorities, communities, soldiers, scholars, and governments can reject the claim, protect civilians, organize resistance, encourage defections, and join the final coalition.

The branch must not depict Allah.

It must not use Quranic calligraphy, Quran recitation, the call to prayer, sacred chant, or another Islamic sacred practice as hostile branding or enemy audio.

It must not use real extremist symbols or reproduce real propaganda.

The entity's art should focus on ambiguous physical presence, altered light, followers, damaged architecture, or impossible atmospheric effects.

It should avoid a direct sacred iconography claim.

### Eligibility

The branch becomes eligible only when all public and hidden requirements are satisfied.

#### Public requirements

- global Chaos is at least `1000`
- Evolution V, The Final Jihad, is enabled and recorded
- no world-end state already exists
- The False Revelation public branch toggle is enabled
- at least one viable jihadist territorial actor exists
- substantial extremist territorial success exists
- widespread active terror crises exist
- International Unity is high enough to support a common claim
- the movement has achieved at least one major strategic victory

#### Major strategic victory

A qualifying victory can include:

- capture of an original national capital of a major or regional power
- destruction of a major counterterror coalition command
- successful unification of several territorial actors
- control of a broad connected regional bloc
- survival of a coordinated global offensive through a major campaign phase

A minor isolated state does not satisfy the requirement by itself.

#### Hidden requirement

Apocalyptic Readiness must reach its threshold.

The value can rise through:

- controlled states and population
- captured capitals
- number and strength of member actors
- high-pressure foreign countries
- regional spread
- major victories
- successful leadership unification
- extremist control of strategic corridors
- prolonged Final Jihad activity

It can fall through:

- member defeat
- leadership rivalry
- loss of capitals
- falling International Unity
- destruction of safe havens
- successful defections
- religious and civic rejection
- restoration of high-pressure countries

The exact formula remains hidden.

Player-facing text can show broad signs that the movement is approaching final unification without exposing the threshold.

### Delayed transition

Eligibility does not trigger the branch instantly.

The branch uses its own delayed event with mean time to happen influenced by readiness, unity, territorial success, and leadership stability.

This gives the world a final chance to reduce readiness.

A dominant actor can also attempt to accelerate the transition through a visible high-risk route, but it cannot bypass the `1000+` Chaos gate or public enable state.

### Dominant actor selection

The transition chooses one existing jihadist actor as the host or creates a safe final carrier from the shared registry when transformation of the existing actor would be invalid.

The dominant actor score considers:

- Network Authority
- International Unity contribution
- controlled territory and population
- captured capitals
- military strength
- surviving foreign cells
- external supply
- faction leadership
- recent victories
- internal rival support

A player-controlled actor should not be silently deleted.

When several player-controlled members exist, the transition should preserve control through faction subordination, a consent choice, or a clear player takeover rule defined for multiplayer.

### Revelation incident

The transition begins with an event at the selected command location.

The public sees:

- the entity's appearance
- extremist leaders accepting or contesting the claim
- synchronized movement orders
- fear, defections, and resistance
- a new final country identity
- the first global uprising wave

The event should describe observable reactions and uncertainty.

It should not state what the entity truly is.

Rival leaders can reject the claim and begin a final internal war.

That rejection should not cancel the world end after the terminal flag is set. It becomes part of the final campaign.

### World-end transition

The transition must:

- guard against an existing world end
- set the shared world-end state
- set a scenario-specific False Revelation flag
- activate the dedicated super-event
- stop ordinary random-event firing
- preserve Event 31 terminal missions and campaign logic
- transform or create the final state
- assign the entity as visible leader
- reconcile faction membership and actor mergers
- trigger uprisings in valid high-pressure countries
- set final values and objectives
- block incompatible future branches

The transition is one transaction.

A failed validation must not set the world-end flag or partially merge countries.

### Actor unification

Existing jihadist actors can enter one of four outcomes.

#### Direct merger

Compatible AI actors or consenting player actors are absorbed into the final state.

Territory, units, stockpiles, technologies, characters, wars, and subjects are reconciled once.

#### Subordinate command

An actor remains a country and joins the final faction under a terminal command relationship.

This is preferred when direct merger would break player control, geography, subjects, or wars.

#### Rival claimant

An actor rejects the entity and fights the final state.

It loses access to the shared Final Jihad command but can cooperate with governments against the entity.

#### Fragmentation

A weak actor collapses into cells, local enclaves, or defectors during the transition.

The unification system must not duplicate units, equipment, territory, technology, or leaders.

### Final state identity

The final state receives:

- a unique fictional country name and adjective
- a unique flat flag and faction emblem
- the ambiguous entity as leader
- a terminal politics identity
- five research slots
- a replacement focus route
- terminal decisions and missions
- extreme but staged national abilities
- a distinct world-threat source
- player-facing rules that explain its campaign objectives

The human population remains human.

The state is a special Chaos country and not an actual nonhuman country.

### Final state ideas

The final package should use a small number of powerful staged ideas.

#### Presence of the Entity

Represents command cohesion, fear, recovery, and resistance to ordinary leadership disruption.

Its strength depends on command capitals, International Unity, and successful uprisings.

#### World in Revolt

Represents synchronized cells and uprisings behind enemy lines.

Its strength depends on high-pressure countries and surviving networks.

#### Supply Through Ruin

Represents captured depots, coerced transport, corridors, and extreme logistical adaptation.

Its strength depends on real controlled infrastructure, ports, supply hubs, and territory.

These ideas should change as the final campaign advances or loses key objectives.

They should not give unlimited power at full strength regardless of world state.

### Extreme abilities

The user brief requires intentionally extreme recruitment, organization, recovery, supply, resistance, uprising, expansion, and combat abilities.

The branch should deliver that power through staged systems.

#### Recruitment

The final state can draw from controlled population, absorbed actors, foreign fighters, defecting units, and high-pressure uprisings.

It receives very strong recruitable-population and mobilization support.

It still needs population and equipment.

#### Organization and recovery

The final state receives high organization recovery and reduced disruption while the entity holds command centers and unity remains high.

Loss of command capitals or rival rejection weakens the effect.

#### Supply

The state receives strong supply grace, captured-supply use, reduced out-of-supply penalties, and emergency corridor decisions.

It does not receive unlimited supply in an isolated empty state.

Ports, railways, hubs, convoys, fuel, and territory remain strategic targets.

#### Resistance and occupation

The state can create Event 31 uprisings and resistance support in high-pressure countries.

Occupied states can face forced rule and atrocities that generate Deaths, Condemnation, and resistance.

High Response Legitimacy and successful local opposition reduce conversion.

#### Expansion

The final state receives rapid war planning, coordinated war goals, and terminal objectives against coalition command regions.

It should prioritize connected fronts and strategic capitals.

#### Combat

The state receives strong attack, defense, breakthrough, planning, reinforcement, and recovery bonuses in terminal phases.

These bonuses scale down when the entity loses command sites, International Unity collapses, or the final network is severed.

### Uprising system

The transition triggers uprisings only in countries with real Event 31 groundwork.

Uprising strength uses:

- Terror Pressure
- active state stage
- local captured equipment
- military defection
- Network Reach
- connected territorial actors
- government Response Legitimacy
- capital security
- current war and occupation

A country with zero pressure and no active cell cannot receive a full rebel army from the branch.

A high-pressure country can receive:

- sabotage and state modifiers
- temporary control loss
- defecting units
- a civil war actor
- state transfer to the final state when contiguous and valid
- a capital seizure mission

The setup should choose the outcome that fits geography and carrier capacity.

### Terminal campaign phases

#### Phase 1: Revelation and synchronized uprisings

The final state consolidates command, chooses merger outcomes, and triggers the first uprising wave.

Governments receive emergency capital, relief, defection, and coalition actions.

The phase ends after the initial transaction, major uprising objectives, and first command front are resolved.

#### Phase 2: Coordinated global offensive

The final state launches regional campaigns, protects corridors, captures capitals, and supports foreign cells.

The coalition targets command capitals, safe havens, transport, International Unity, and Network Authority.

#### Phase 3: Forced world order

The final state attempts to consolidate conquered regions through forced administration, expulsions, mass killing, ideological control, and permanent military occupation.

These actions create severe Deaths and Condemnation, but can also raise resistance, foreign unity, and internal defections.

#### Phase 4: Collapse or final victory

The branch ends through one of the final outcomes.

- the entity state conquers or subordinates every meaningful opposition center
- the world coalition destroys the final state and command network
- the entity disappears after loss of readiness and command, leaving fragmented actors
- rival claimants destroy the final unity and the world enters a prolonged extremist civil war

The exact campaign resolution should be defined in implementation once the repository's terminal-state conventions are inspected.

### Global counterplay

The world needs clear objectives beyond winning every front conventionally.

#### Recapture command capitals

Each major command capital strengthens Presence of the Entity.

Recapturing and holding it weakens final bonuses and can free local resistance.

#### Sever strategic corridors

Destroying or controlling named ports, rail links, border states, and supply hubs reduces Supply Through Ruin and prevents reinforcement of distant fronts.

#### Restore high-pressure countries

Governments can lower Terror Pressure, protect capitals, support victims, and defeat uprisings.

Each restored country lowers World in Revolt.

#### Support defectors and rival claimants

The coalition can encourage members, commanders, and communities to reject the entity.

This lowers International Unity and can create internal fronts.

#### Protect religious and civic opposition

Fictional Muslim religious authorities and other threatened institutions can undermine the movement's claim, protect civilians, and support defections.

Their survival affects recruitment and legitimacy.

#### Expose atrocities and coercion

Public evidence increases Condemnation, coalition participation, sanctions, resistance, and sponsor withdrawal.

#### Destroy the central command

The final state should have one or more clear command sites whose loss changes its abilities.

The entity cannot become immune to every conventional objective.

### Coalition behavior

Existing factions can cooperate through a terminal coalition system without requiring every country to leave its faction.

The coalition can coordinate:

- intelligence
- command-capital targets
- relief corridors
- lend-lease
- volunteers and expeditionary support
- naval blockade
- air defense
- resistance support
- reconstruction after liberation

Membership and contribution depend on access, threat, ideology, relations, war state, and capacity.

Muslim-majority governments should be strong likely participants when targeted, without receiving magical bonuses based on identity.

### Player control

A player controlling the dominant actor can accept the entity, contest it, or attempt to preserve independent command during the transition.

Accepting the entity gives control of the final state or preserves player control through the safest supported route.

Contesting the claim creates a rival actor or internal war and places the player against the terminal state.

A player controlling a victim government receives immediate objectives and coalition choices.

In multiplayer, no player country should disappear without an explicit handoff, consent path, or documented terminal takeover rule.

### Super-event presentation direction

The world-end transition receives one dedicated super-event.

#### Role

First reveal and terminal campaign announcement.

#### Title direction

The title should be short, specific, and centered on false divinity, disputed revelation, or the movement's final claim.

The researcher must not treat the working branch name as automatically final localisation.

#### Description direction

Describe the entity's appearance, the acceptance by extremist leaders, simultaneous uprisings, public fear, and open rejection by religious and civic opponents.

Preserve uncertainty about the entity.

#### Button direction

Use a brief researched reaction suited to an impossible and coercive claim.

Avoid a sacred Islamic phrase, cheap joke, generic statement, or unverified cultural reference.

#### Quote direction

Research public-domain religious, philosophical, literary, or historical material about false prophets, deception, idolatry, coercive belief, or judgment.

Do not invent or misattribute a quote.

Do not use a Quranic verse as villain presentation without a carefully justified and user-approved treatment. The preferred direction is a broader public-domain source that preserves the event's ambiguity and avoids turning Islamic scripture into enemy branding.

#### Image direction

Generated period-authentic documentary or surreal report art.

Show the entity indirectly through impossible light, a command hall, altered shadow, followers, damaged architecture, or a mass reaction.

Do not depict Allah, sacred calligraphy, real extremist emblems, modern equipment, or a generic fantasy demon portrait detached from the 1936 to 1945 world.

#### Audio direction

Research a unique licensed or public-domain musical recording with an ominous, processional, or apocalyptic structure.

Do not use Quran recitation, the call to prayer, Islamic sacred chant, generated audio, drones, test tones, or unlicensed commercial music.

The final cue needs source and recording rights evidence.

### Entity portrait and animation

The entity is an impossible fictional subject and can use native ImageGen through the portrait worker.

The static portrait must work at `156x210`.

One animated portrait or transparent portrait overlay is justified because the visual state marks a terminal identity transformation.

A possible loop can show subtle impossible light, shifting shadow, or a presence that does not remain optically stable.

Every frame must be separately generated or edited under the frame-animation rules.

Transform-only motion, glow filters, or a GIF made from one shifted still cannot be the final asset.

The animation needs a static fallback and verified GUI consumer before implementation.

### Defeat aftermath

Defeating the final state qualifies for a major aftermath because the threat is global, prolonged, and destructive.

The aftermath should include:

- a reflective defeat super-event
- liberation and reconstruction missions
- victim and survivor support
- treatment of prisoners and defectors
- restoration of states and governments
- a counterterror and human-rights compact
- remaining splinter cells
- debate over the entity's nature
- memorial and vigilance events
- continuing Condemnation and Deaths history

The world should not return instantly to normal.

The aftermath can reduce Chaos through liberation and reconstruction while preserving long-term damage and political consequences.

The defeat super-event requires separate quote, image, remark, and audio research.

### Event Details public branch

The False Revelation receives one stable public scenario registry row owned by Event 31.

The row includes:

- branch title
- premise
- terminal-state summary
- current enabled state
- current broad availability state when useful
- persistent independent toggle

It must not show:

- Apocalyptic Readiness
- exact territorial score
- exact capital count
- hidden MTTH
- entity identity
- secret transition branches

Disabling the row skips automatic selection and leaves Event 31 active.

### World-threat interaction

The final state activates the strongest Event 31 world-threat source.

Defeat, collapse, or terminal replacement clears or updates the source through the shared aggregate.

The world-threat flag must reflect real surviving qualifying actors and not remain active after total cleanup.

### Acceptance cases

The world-end branch is complete only when:

1. It cannot fire below `1000` Chaos.
2. It cannot fire before Evolution V is enabled and recorded.
3. It cannot fire when its public toggle is disabled.
4. It requires substantial territory, widespread crises, unity, and a major strategic victory.
5. Eligibility starts a delay instead of an immediate transition.
6. A failed transaction does not set `world_end`.
7. Existing actors merge, subordinate, reject, or fragment without duplication.
8. Player-controlled actors retain a clear control path.
9. Uprisings require actual prior pressure or cells.
10. Final abilities remain extreme and respond to command, territory, supply, unity, and counterplay.
11. Muslim religious and governmental opposition is visible and mechanically meaningful.
12. The game never confirms that the entity is Allah.
13. No sacred Islamic audio or real extremist visual is used.
14. Ordinary random events freeze while terminal content continues.
15. The final state is special Chaos but not actual nonhuman.
16. Defeat creates a structured aftermath and a separate researched super-event.

---

## Part 9: AI, balance, and probability

### Balance purpose

Event 31 should create uncertainty and hard choices without turning every firing into an unavoidable state loss.

A stable country that responds well should normally contain the opening crisis.

A weak country, a country at war, or a government that repeatedly chooses poor responses should face a credible path to spread, insurgency, coup, and territorial loss.

Territorial actors should survive long enough to matter without receiving unsupported armies or endless free growth.

The Jihadist International and Final Jihad should be late campaign threats created by real network and territorial success.

The False Revelation should be rare outside its manual setup and should still have clear counterplay after it begins.

### Difficulty curve

#### Baseline

The opening should pressure several countries but remain manageable.

A well-prepared country with one active state should be able to clear the crisis through one protection or intelligence mission, one targeted operation, and recovery work.

A country that ignores the crisis should see pressure rise over several incident pulses instead of losing a state immediately.

#### Organized and transnational stages

The main challenge shifts from one cell to coordination, corridors, safe havens, and sponsor support.

A country can win locally while the wider network survives.

International cooperation becomes valuable but should not be mandatory for every small crisis.

#### Territorial stage

The challenge becomes a war and state-restoration problem.

A territorial actor should begin weak enough that a prepared parent can counterattack, but strong enough to survive a token response.

#### Jihadist and final stages

The movement gains broader recruitment and coordination while also facing internal rivalry, stronger international reaction, Muslim opposition, and greater logistical burden.

Power should come with more fronts and more enemies.

#### World end

The final state receives extreme staged strength.

The coalition can still weaken it through command capitals, supply corridors, restored high-pressure countries, defections, and unity loss.

### Government AI profiles

Current conditions determine government AI actions. Permanent national labels do not.

#### Capacity-led government

Traits:

- high industry
- adequate equipment
- functioning intelligence
- high stability
- few active states

Behavior:

- establishes coordination early
- uses intelligence before raids
- supports victims after major attacks
- protects critical supply
- accepts joint operations with trusted partners
- avoids indiscriminate restrictions

#### Security-first government

Traits:

- active war
- threatened capital
- low patience
- available military units
- high war support

Behavior:

- reinforces states quickly
- protects the capital
- uses rapid raids and restrictions
- accepts a higher legitimacy risk
- shifts toward relief and accountability after severe civilian harm when capacity allows

#### Fragile government

Traits:

- low stability
- weak industry
- low equipment
- several internal crises
- divided army

Behavior:

- seeks foreign aid
- protects the capital and one priority corridor
- avoids expensive simultaneous missions
- may negotiate with a weakened enclave
- faces a higher failure and takeover risk

#### Authoritarian coercive government

Traits:

- low concern for legitimacy
- strong police or army
- high political control
- active opposition

Behavior:

- favors broad restrictions and rapid raids
- accepts civilian harm risk
- conceals some failures
- can achieve fast local suppression
- creates stronger recurrence and Condemnation risk

The profile does not guarantee abuse. High-quality intelligence and severe immediate danger can still produce a precise operation.

#### Coalition-oriented government

Traits:

- faction membership
- good relations with neighbors
- transnational threat
- adequate convoys and intelligence

Behavior:

- shares intelligence
- protects corridors
- supports a threatened ally
- exposes sponsors
- avoids unilateral intervention without access

#### Isolationist government

Traits:

- no faction
- low foreign trust
- limited overseas capacity
- domestic priority

Behavior:

- focuses on national cells
- refuses expensive distant operations
- accepts border cooperation when the threat is adjacent
- can reconsider after a demonstration attack

### Government priority ordering

Government AI should normally use this priority order.

1. Prevent immediate capital seizure or government collapse.
2. Keep critical military supply and transport open.
3. Stop an active state from reaching Lost Local Control.
4. Protect civilians and restore services after severe harm.
5. Target the current network support source.
6. Retake lost territory when force and supply are credible.
7. Support allies and foreign corridors when domestic survival is secure.
8. Pursue long-term accountability, reform, and recovery.

The ordering changes when one objective has an imminent deadline.

AI should not start a distant intervention while its own capital mission is failing.

### Government action validity

AI assigns zero weight when:

- the target state is invalid or already clear
- the required units are absent
- the country cannot preserve a minimum equipment, fuel, train, convoy, or manpower reserve
- the action duplicates an active mission
- the sponsor or ally does not exist
- route access is impossible
- the movement has no matching support source
- the decision belongs to a disabled evolution
- a surrender action targets an actor that rejects negotiation
- a foreign intervention would create an impossible front

### Extremist cell AI

A cell should behave like a network trying to survive and gain power.

It should compare:

- state activity
- government protection
- Response Legitimacy
- local population and infrastructure
- access to supplies
- adjacent cells
- risk of exposure
- current organization goals
- likely political value of the target
- current evolution

Low-stage cells favor survival, recruitment, local sabotage, and limited attacks.

Entrenched cells favor coordinated waves, depots, corridors, training areas, and political targets.

Armed insurgencies favor defections, state control, capital pressure, and support from territorial actors.

A cell should sometimes remain dormant after a government surge instead of attacking into certain defeat.

### Territorial actor AI

Territorial AI priorities are:

1. preserve a viable capital and supply base
2. keep held territory connected
3. maintain equipment and manpower reserves
4. defend against a parent counteroffensive
5. improve Territorial Control
6. secure External Supply
7. raise and upgrade existing formations
8. support nearby high-value cells
9. expand toward strategic connected states
10. merge, sponsor, negotiate, or split according to Network Authority

A local actor should not attack a distant major for prestige while its only capital is exposed.

A transnational actor can spend more on foreign cells when its territorial core is secure.

### Route AI

#### Shadow Council

Preferred when:

- territory is small or scattered
- Network Reach is high
- foreign cells exist
- the parent is much stronger
- intelligence capacity is strong

#### War Directorate

Preferred when:

- territory is contiguous
- regular units defected
- supply is adequate
- the parent is vulnerable
- a conventional war is active

#### Ideological Secretariat

Preferred when:

- recruitment is high
- a charismatic fictional leader or strong doctrine exists
- internal political control matters
- Evolution IV access is desired

#### Economy AI

Smuggling and sponsorship rise when domestic industry is weak.

Civil administration rises when the actor expects to hold territory.

Coerced extraction rises under immediate war pressure and falls when resistance threatens collapse.

### Jihadist AI

After Evolution IV, a compatible actor evaluates:

- parent government strength
- adjacent Muslim-majority governments identified through an event-local reaction registry
- rival jihadist claimants
- Event 14 cannibal actors
- faction leadership
- International Unity
- Network Authority
- supply and border access
- religious and civic opposition

The event-local Muslim-majority registry is used only for this actor-specific enemy and reaction behavior.

It is never used for ordinary targeting, recruitment, or cell formation.

Jihadist AI should prefer its parent, adjacent strategic territory, rival claimants, and governments directly blocking its routes.

It should avoid declaring distant unsupplied wars only because the target matches an ideological enemy category.

### Final-command AI

Final-command AI should coordinate several systems.

- support uprisings where pressure and local capacity make them useful
- merge or subordinate actors without breaking player control
- capture command capitals
- preserve strategic corridors
- respond to coalition attacks on the entity's command sites
- maintain International Unity
- suppress or negotiate with rival claimants according to strength
- avoid scattering forces across every active cell

The final state should pursue a small number of major regional objectives at a time.

### Target-selection balance

The ordinary target pool should preserve this ordering under comparable conditions.

1. countries with active unresolved Event 31 pressure
2. countries connected to an active corridor or territorial actor
3. unstable or war-damaged countries with meaningful states
4. stable countries with exposed high-value infrastructure
5. recently cleared countries after their cooldown

Religion, ethnicity, nationality, refugee population, and ordinary ideology must have no positive factor.

The target audit should include paired scenarios where two countries differ only in Muslim-majority status. Their ordinary target scores must remain equal.

### State-selection balance

State weighting should make important targets more likely without making capitals automatic.

A protected capital can lose weight.

An entrenched border state can exceed the capital when it contains the real network.

The state pool must remain complete when normalized probabilities are audited.

Port, rail, depot, capital, and border incident pools need separate validity checks.

### Incident probability principles

The incident pool should react to state and organization state.

- civilian and transport incidents remain common at low activity
- copycat and sponsor incidents rise after visible attacks
- corridor and training incidents require support and geography
- military defections require severe pressure and local weakness
- capital seizure requires capital infiltration
- territorial transfer requires Lost Local Control or an equivalent collapse
- distant attacks require Network Reach
- synchronized uprisings require Evolution V or the Maximum scenario

No rare severe outcome should dominate because several positive modifiers stack without a cap.

### Evolution pacing

Evolution pacing uses campaign evidence.

The intended ordering is:

- a world with many active organized networks evolves faster than one with one contained cell
- territorial victories accelerate Evolution III and later
- successful international cooperation slows Evolution II growth
- high International Unity accelerates Evolution V
- repeated internal jihadist wars slow Evolution V
- an event that has never fired can begin at the current enabled evolution without logging lower stages as immediate incidents

The implementation must not claim an exact mean time from incomplete external state.

### Country-spawn balance

A stable country should not lose territory from the first ordinary attack.

A territorial spawn normally needs several failures, high pressure, a severe state stage, and armed capacity.

The country-package strength should follow:

- number and quality of held states
- parent military defections
- actual captured equipment
- controlled population
- sponsor support
- current evolution
- parent weakness

A local actor should be dangerous near its territory and weak in a long conventional war.

A regional actor should be capable of surviving and expanding.

A transnational actor should trade some conventional strength for network reach.

A jihadist actor should gain recruitment and coordination while attracting stronger enemies and internal rivalry.

### Force-balance anchors

The starting formation bands in Part 5 are ceilings and floors for tuning, not automatic grants.

The final force count should be derived from viable state and resource inputs.

The implementation should compare:

- actor divisions per controlled state
- equipment fill
- parent divisions and fronts
- supply
- manpower reserve
- expected foreign aid
- nearby hostile countries

An actor should not spawn with more fielded combat power than its entire population, equipment, and defection evidence supports.

### Response-cost balance

Costs should create a choice between domestic security and other war priorities.

A normal early response should be affordable.

Running every response at once should not be affordable.

A major territorial campaign should require actual divisions, fuel, equipment, and supply.

Victim support and reconstruction should compete for civilian capacity without becoming a punitive trap.

Command power costs remain conservative and never exceed the project limit.

### Response-outcome balance

High intelligence and legitimacy should improve clean outcomes.

They should not guarantee success against a strong entrenched actor.

Military force should matter against armed insurgency.

It should not erase the effect of poor intelligence and civilian protection.

Negotiation should work against divided, isolated, or weakened actors.

It should be dangerous against a strong actor using time to rebuild.

### Network-value balance

Network Reach and International Unity should move through public events and objectives.

They should not drift upward without active networks.

They should have gains, losses, caps, and meaningful thresholds.

The same victory should not add to the same value several times through country, organization, and global handlers.

### World-end balance

The False Revelation needs enough preconditions that it is rare in ordinary play.

Once active, its strength should be unmistakable.

The coalition needs several non-identical ways to weaken it.

A player should be able to identify:

- which command capital matters
- which corridor feeds a front
- which high-pressure country can be restored
- which rival or defector can reduce unity
- which final ability weakens after an objective

The branch should not become a single enormous modifier that remains fixed until annexation.

### Performance budget

The event can affect many countries, but it must remain bounded.

Design rules:

- no recurring whole-world daily, weekly, or monthly scan
- only affected countries and active actors receive event-owned pulses
- active state arrays are cleaned after containment or annexation
- global incident count has a practical cap
- the Maximum scenario respects carrier and performance limits
- distant networks use selected targets instead of iterating every country each pulse
- AI target pools are rebuilt only when needed
- obsolete missions and event targets are cleared

Performance pressure should reduce new target count before it removes the current player's active content.

### Exploit and failure audit

The implementation must test for:

- farming Terror Pressure for beneficial decisions
- farming victim support or legitimacy
- creating free equipment through repeated depot capture
- duplicating units during merger or takeover
- canceling missions to recover consumed costs
- preserving sponsor aid after the sponsor dies or turns hostile
- repeated free foreign fighters
- endless restriction stacking
- repeated surrender rewards
- invalid retake objectives
- AI draining every train, convoy, or fuel reserve
- player tag switching to preserve actor and parent rewards
- scenario relaunch duplication
- world-end transition duplication
- uprising strength from stale pressure

### Mandatory probability scenarios

The implementation and probability auditor should use these named scenarios.

#### `P01_stable_peace_state`

A stable country at peace with one active urban state, high legitimacy, functioning intelligence, and adequate resources.

Expected result:

- containment actions dominate severe coercion
- territorial spawn remains very unlikely
- state spread remains slow

#### `P02_unstable_wartime_authoritarian`

A low-stability country in war with weak legitimacy, several fronts, strong military, and poor intelligence.

Expected result:

- rapid security actions become attractive
- abusive failure risk rises
- capital and territorial escalation become materially more likely than in P01

#### `P03_occupied_resistance_context`

A country controls occupied states with resistance, supply strain, and one active Event 31 network.

Expected result:

- occupied-state activity matters
- civilian and resistance consequences are visible
- the event does not classify the entire occupied population as terrorists

#### `P04_successful_response`

A country has completed protection, victim support, and an intelligence breakthrough.

Expected result:

- clean raid and defection outcomes improve
- recurrence and spread fall
- severe incidents do not retain their old weight

#### `P05_transnational_safe_haven`

One weak host supports a network across three countries with a sponsor and two corridors.

Expected result:

- corridor and safe-haven actions dominate unrelated domestic actions
- network reach creates distant but bounded options
- destroying one corridor does not erase the entire network

#### `P06_territorial_spawn`

A country has high pressure, one Lost Local Control state, defecting units, captured equipment, and viable parent territory.

Expected result:

- territorial creation is available and materially likely
- invalid isolated states remain excluded
- actor strength follows resources

#### `P07_muslim_government_against_jihadist`

A Muslim-majority government faces an Evolution IV jihadist actor and has strong local religious opposition.

Expected result:

- actor-specific enemy priority and opposition content activate
- ordinary Event 31 target chance remains unchanged
- community rejection reduces recruitment and unity

#### `P08_cannibal_border`

An Event 31 actor and Event 14 cannibal country share a border while both fight a third government.

Expected result:

- alliance and faction cooperation remain impossible
- rivalry actions and hostile strategy gain weight
- neither actor ignores a vulnerable immediate front merely to satisfy rivalry

#### `P09_major_intervention`

A major power has capacity and access to assist a weak ally while its own country has low domestic pressure.

Expected result:

- intelligence, aid, and limited intervention become plausible
- direct intervention does not dominate when access or support is poor

#### `P10_maximum_scenario`

Global Jihad Maximum has several actors, active cells, high reach, and immediate Final Jihad.

Expected result:

- extremist AI coordinates strategic fronts
- government AI protects capitals and forms coalitions
- The False Revelation remains unavailable below `1000` Chaos

### Probability evidence contract

Every complex or balance-sensitive weight needs:

1. source inspection through the HOI4 probability tool
2. a complete candidate pool or an explicit statement that the pool is incomplete
3. named scenarios from this specification
4. baseline evidence
5. an owner-applied tuning change when needed
6. comparison against the same scenarios
7. a clear distinction between exact, bounded, sampled, score-only, and unresolved results

The probability auditor remains read-only and does not choose the design target.

The owner chooses the intended ordering from this specification and applies the patch.

### Completion standard

AI and balance are complete only when:

- stable countries normally have a credible containment path
- failure escalates through visible causes
- government AI protects urgent domestic objectives
- cells and actors preserve supply and survival
- route AI matches territory and organization state
- identity does not enter ordinary target or recruitment scores
- country strength follows real resources
- extreme world-end strength has objective-based counterplay
- named probability scenarios have baseline and comparison evidence
- performance remains bounded to active countries and actors

---

## Part 10: Cross-event and shared-system interactions

### Interaction purpose

Event 31 should exist inside the Chaos Redux world.

Its cells, territorial actors, wars, deaths, sponsors, state damage, and final branch should respond to other event systems without duplicating their ownership.

A connection is useful when it changes play, creates a valid new incident, or prevents two systems from contradicting each other.

It should not become a list of references with no mechanics.

### Event 14 Cannibalism

This interaction is mandatory.

Event 31 actors and Event 14 cannibal actors are hostile rival movements.

They cannot:

- ally
- join the same faction
- enter a nonaggression arrangement presented as natural cooperation
- merge
- exchange volunteers
- share safe havens
- treat one another as an ordinary compatible extremist actor

They can:

- fight border wars
- raid supplies
- compete for prisoners, recruits, transport, depots, and territory
- spread propaganda against one another
- accept defectors from the rival
- massacre captured members
- exploit the rival's attack on a government
- temporarily avoid a front through ordinary military necessity without creating a formal partnership

#### Shared-border incidents

Possible incidents include:

- cannibal raid on an Event 31 depot
- Event 31 attack on a cannibal settlement
- prisoner escape during a clash
- civilians trapped between both actors
- defections from one movement to the other side's enemies
- a contested border state changing activity stage
- the parent government exploiting the clash
- foreign intervention after mass killing

#### AI rule

The actors receive high hostility and strategic priority when they share a border or compete for the same state.

They still compare immediate survival and supply.

A weak actor should not abandon its capital to attack the rival across an unreachable front.

#### Condemnation and Deaths

Clashes can cause real population loss and public atrocities.

Each actor's responsibility is recorded separately when attribution is known.

### Event 21 Random Civil War

Event 31 can create civil wars through baseline failure.

Event 21 can create an unrelated civil war in a country that later develops terror cells.

The two events need a shared conflict check.

#### Rules

- Event 31 does not launch a duplicate civil war when the country already has an active Event 21 internal war.
- Event 31 can attach cells to one or more sides through incidents, support, sabotage, or a later breakaway.
- Event 21 can use an established Event 31 territorial actor as one side when the country and state setup fit.
- A defeated Event 21 side can leave weapons, officers, and grievances that strengthen Terror Pressure.
- Event 31 takeover victory can satisfy the internal-war resolution without creating a second rebel country.
- Event 31 and Event 21 keep separate history and evolution identity.

The proposed Internal Fracture cluster can later coordinate their shared firing.

### Event 4 Random War

A random war can increase Event 31 opportunity through mobilization, exposed supply, occupation, and weakened administration.

Event 31 can:

- target transport behind a front
- exploit a newly occupied state
- create sabotage during an offensive
- receive weapons from a belligerent sponsor
- start a local uprising when pressure already exists

Random War remains owner of the war it creates.

Event 31 should not add a second generic war goal merely because the same countries are fighting.

A peace settlement does not automatically clear active cells.

### Event 6 Independence Wave

Newly released countries can become Event 31 targets after their foundation period.

They can also inherit active cells from the territory they receive.

Rules:

- Event 31 uses the shared carrier registry and does not reserve duplicate Event 006 carriers.
- A new country receives an origin-aware Event 31 crisis only after its history, capital, and state package exist.
- Independence does not mark the released population as extremist.
- A pre-existing cell follows its actual state and controller.
- A released country can become the parent of a later Event 31 territorial actor.
- Event 31 country creation must pass the protected carrier audit.

### Event 7 Fury

Fury actors and Event 31 actors can become rivals, sponsors, or targets depending on the actual Fury package.

A Fury country classified as special Chaos should not receive the ordinary civilian Event 31 opening.

Possible connections:

- Fury warfare raises regional Terror Pressure in ordinary neighboring countries
- an Event 31 actor seeks weapons from a Fury actor
- a Fury actor destroys a safe haven without regard for civilians
- Final Jihad and a global Fury threat compete for world leadership

A connection must respect Fury's own faction and world-end rules.

Event 31 cannot absorb a Fury actor into the Jihadist International.

### Event 10 Death

Death and its countries are excluded from ordinary Event 31 victim selection.

Human governments fighting Death can still suffer Event 31 attacks if they have valid cells.

Possible interactions:

- a cell exploits mass panic and abandoned transport
- an Event 31 actor attempts to bargain with Death and is destroyed or ignored
- the final jihadist command treats Death as an existential rival
- terrified members defect after contact with Death

Death remains owner of its supernatural rules and world threat.

Event 31 does not classify Death as a terrorist actor.

### Event 13 Natural Disasters

Natural disasters can weaken administration, damage transport, displace civilians, and create temporary safe-haven opportunities.

Event 31 can react through:

- attacks on damaged transport
- relief-corridor protection
- exploitation of an evacuated border
- recruitment pressure after abusive or absent government response
- community defense and victim support
- extremist attacks on relief operations
- territorial actors providing or denying aid

Rules:

- displaced civilians are victims and do not add terror activity by identity
- Event 13 owns disaster damage and disaster Deaths
- Event 31 owns later deliberate attacks and recruitment consequences
- the same destroyed building is not damaged twice by one causal incident
- a disaster can temporarily modify targeting but cannot create an unsupported cell

### Event 16 Brilliant Scientist

Brilliant Scientist can connect through technology, surveillance, medicine, transport, or strange projects.

Possible government benefits include:

- better incident identification
- protected communications
- faster infrastructure repair
- improved hostage or disaster medicine
- a bounded intelligence breakthrough

Possible extremist interactions include:

- attempt to kidnap a scientist
- raid a research facility
- capture an existing prototype after territorial seizure
- seek sponsor access to a technology

Rules:

- Event 31 does not activate Event 16 host state or project history
- no advanced custom technology is granted without a real Event 16 bridge and source event
- the scientist connection is optional and not required for core progression
- dangerous technology capture needs its own guarded incident and consequence

### Event 19 Infantry Spawn

Event 31 creates no custom land unit family.

It uses existing combat battalions and support companies.

Therefore Event 31 requires no Event 19 provider registration, no provider callbacks, no custom unit counters, no custom unit sound package, and no 3D unit model.

If implementation later adds a distinct Event 31 combat unit, the Event 19 integration obligation becomes mandatory in the same change.

The current accepted design should not add such a unit.

### Event 20 The Black Plague

Rat Nations, Rat King actors, zombie outbreaks, and other actual nonhuman or special plague actors are excluded from ordinary Event 31 victim selection when the civilian crisis model does not fit.

Human countries suffering plague can still receive Event 31 attacks.

Possible interactions:

- attacks on quarantine or relief transport
- plague panic increasing state disruption
- an extremist actor concealing an outbreak
- government response resources divided between outbreak and cells
- forced movement increasing relief pressure
- Event 31 actors fighting Rat Nations over territory

Event 20 owns outbreak spread, plague immunity, Rat Nation packages, and plague Deaths.

Event 31 owns deliberate attacks and its own state pressure.

### Event 23 SOV Nuclear Bombs

A territorial Event 31 actor can threaten or attempt to seize an existing nuclear stockpile only through a rare guarded incident.

Requirements should include:

- actual nuclear stockpile or relevant facility
- actual control or seizure risk in the state
- severe territorial or capital crisis
- valid actor and command structure
- clear consequences and international reaction

Event 31 does not create nuclear bombs, nuclear technology, or delivery systems.

A successful seizure uses the shared nuclear, fallout, Deaths, Condemnation, and Chaos systems.

The possibility should remain rare and visible enough for counterplay.

### Event 29 Riches Found

A Riches Found state can attract criminal support, extortion, sabotage, or territorial competition.

Possible interactions:

- an organized cell taxes or steals from the wealth rush
- a territorial actor captures the state and inherits the controller-facing modifier
- a government protects mines and transport
- criminal patrons fund a network
- demons or gold disease create a separate high-chaos crisis

Event 29 remains owner of the persistent state wealth modifier and its supernatural evolutions.

Event 31 cannot duplicate or remove the wealth source through a generic raid.

### Event 32 Missiles

A territorial actor can capture operational missiles or a launch site only when it actually takes a state containing them or defeats a force that owns them.

Rules:

- Event 31 does not grant missile technology or stockpiles by itself
- the Missiles system remains owner of launch sites, technology, packages, and automatic retaliation
- government players can receive an emergency Secure the Launch Site mission
- a successful actor seizure creates a major public strategic shock
- unconventional warhead use follows the shared weapon and Condemnation systems
- a local cell without territory cannot fire a strategic missile through an abstract attack

This interaction belongs in a later implementation tranche only after Event 32 has a stable runtime contract.

### Chemical, biological, nuclear, and thermonuclear systems

Event 31 actors use unconventional weapons only when they obtain the actual technology, equipment, payload, delivery route, and target proof required by the shared systems.

No Event 31 decision bypasses those gates.

Public use adds Condemnation and Deaths through the owning warfare system.

A cell attack cannot be used as a generic fallback for a chemical or biological strike.

The final state can pursue existing weapons through capture or research, but the world-end package does not grant every unconventional weapon automatically.

### Deaths system

Every Event 31 civilian death uses the shared exact population-loss route and a stable Event 31 reason.

Separate reasons should distinguish:

- terrorist attack
- hostage or public attack
- territorial atrocity
- government counterterror casualties
- Event 31 civil war or uprising where the shared military ledger needs attribution
- False Revelation occupation and uprising

The event must avoid double counting between immediate events, state pulses, battles, and aftermath.

Deaths remain in the global history after the crisis ends.

### Condemnation system

Event 31 can add public sources for:

- exposed state sponsorship
- public extremist atrocities
- forced rule and mass killing
- government collective punishment
- government cover-up
- unlawful intervention
- repeated public abuse

Hidden evidence remains hidden until exposure.

Ordinary police or intelligence work does not generate Condemnation merely because it targets a terror cell.

The selected country detail should identify the responsible actor and source category.

### Chaos Meter

Event 31 contributes to Chaos through:

- tracked deaths
- major public attack waves
- captured capitals
- civil wars
- territorial actor formation
- global network milestones
- Final Jihad activation
- world-end transition

Containment, liberation, reconstruction, and defeat of a global threat can reduce Chaos through the appropriate shared systems.

Direct Event 31 Chaos changes should remain modest outside major strategic milestones so deaths and wars are not counted twice.

### Air Cleanliness

Ordinary Event 31 attacks do not change Air Cleanliness.

Air Cleanliness changes only when the event uses an owning contamination source such as nuclear, chemical, biological, wildfire, volcanic, or another registered system.

A bombing or fire does not become global atmospheric contamination without the owning system's evidence.

### World-threat aggregate

Event 31 needs one registered source flag, working identity `world_threat_source_random_terror`.

The source becomes active when Event 31 reaches a genuine existential level, such as:

- the Jihadist International controlling meaningful territory and several countries
- the Final Jihad becoming active
- the False Revelation state existing

Ordinary local cells should not mark the whole world as under existential threat.

The source is rebuilt through the shared `refresh_world_threat_state` aggregate.

It clears when no qualifying Event 31 actor or final state remains.

### Special-country classifiers

Event 31 territorial countries use one generic actor marker in the shared special-country trigger.

This prevents ordinary civilian systems from treating them like stable normal states.

They remain human and do not enter the actual-nonhuman trigger.

The classifier should cover:

- territorial Event 31 countries
- parent countries transformed by takeover
- jihadist countries
- the final state

It should not classify an ordinary government merely because it has active Terror Pressure.

### Country-carrier registry

Event 31 uses the shared country collections and protected carrier audit.

It must record:

- carrier ID
- Event 31 origin
- parent country
- organization identity
- region
- territorial states
- route profile
- current leader and flag package
- active or clear state

The same carrier cannot be used by Event 006, Soviet Collapse, another active Event 31 actor, or another protected package at the same time.

### Event logs and history

Event 31 uses the shared history and evolution systems.

Connections to another event do not convert the incident into that event's history row unless the owning event actually fires.

Examples:

- a disaster-created relief weakness remains Event 13 history, while a later attack is Event 31 history
- a civil war remains Event 21 history when Event 21 created it, while Event 31 support incidents remain Event 31 reports
- a captured missile remains Event 32 state, while the seizure incident belongs to Event 31

### Proposed Internal Fracture cluster

Working cluster identity:

- proposed ID: `9`
- working name: `Internal Fracture`
- Event 31 role: severe member

Potential future members:

- Event 21 Random civil war
- Event 31 Random Terror
- Event 95 Occupation Revolt
- Event 131 Widespread Mutiny
- Event 142 Partisans

The cluster should not be registered until enough member events are reworked and their member roles are stable.

Event 31 remains fully functional without the cluster.

A future cluster firing counts as one global pacing event while each member keeps its own effects and history.

### Interaction acceptance cases

Cross-event integration is complete only when:

1. Event 31 and cannibal actors cannot ally or share a faction.
2. Their AI attacks one another when practical without abandoning survival.
3. Event 21 and Event 31 do not create duplicate civil wars.
4. Independence Wave carriers are not duplicated.
5. Natural-disaster displacement does not classify refugees as terror risks.
6. Death, Rat Nations, zombies, and other incompatible special actors are excluded from ordinary targeting.
7. Event 31 creates no custom Event 19 unit provider.
8. Nuclear or missile seizure requires real owning-system state and proof.
9. Deaths and Condemnation are attributed once to the correct actor.
10. The Event 31 world-threat source activates and clears from real world state.
11. Event 31 actors are special Chaos and remain outside actual nonhuman classification.
12. The proposed cluster remains unregistered until its member package is ready.

---

## Part 11: Assets, presentation, and localisation direction

### Presentation strategy

Event 31 needs strong visual identity across four scales.

- national crisis response
- named fictional organizations
- territorial extremist countries
- terminal False Revelation campaign

The presentation should help the player distinguish state activity, organization profile, country route, and evolution.

It must not use real extremist imagery, sacred calligraphy, modern tactical aesthetics, or generic map diagrams as the main art.

### Decision-category presentation

#### Government response category

Presentation layer: ordinary decision category with one static category picture.

The picture should show a period emergency response involving damaged transport, guarded civilians, relief workers, and security personnel.

The scene should communicate protection, uncertainty, and material disruption.

It should avoid:

- a modern command center
- a tactical map covered in arrows
- visible real flags or organization symbols
- a staged propaganda poster
- fake UI controls
- unreadable generated text

#### Territorial actor category

Presentation layer: ordinary decision category with one static category picture.

The picture should show an improvised command center inside captured civic or industrial space, with damaged infrastructure and mixed militia or defecting regulars.

It must remain fictional and period-authentic.

#### Final state category

Presentation layer: ordinary terminal decision category with a distinct static picture.

A full custom GUI remains unnecessary.

The image should show the altered command environment and worldwide uprising state without depicting a deity.

### State and map presentation

The event needs an event-owned state map mode or map highlight family.

Required states:

- dormant activity
- active cell
- entrenched network
- armed insurgency
- lost local control
- current government operation target
- current corridor or safe-haven connection

Color and icon treatment must include non-color cues such as borders, symbols, patterns, or tooltips.

The map mode should name the state, activity stage, organization, current mission, and broad next risk.

It should not expose hidden incident probability or Apocalyptic Readiness.

### Report and event art inventory

The event should use a curated report-art family.

Recommended generated period-documentary scenes:

1. damaged railway and civilian evacuation
2. guarded station and emergency transport
3. hostage or public-building crisis shown indirectly
4. burned depot and captured equipment aftermath
5. intelligence raid aftermath with recovered documents
6. relief workers and victims after an attack
7. border corridor under military protection
8. armed enclave in a captured town
9. defecting soldiers or police joining an insurgency
10. government capital under emergency guard
11. rival extremist groups fighting in an urban or border setting
12. local religious and civic leaders rejecting the fictional jihadist movement
13. territorial actor proclamation inside a captured public building
14. jihadist international gathering using wholly fictional emblems
15. synchronized uprising during the Final Jihad
16. defeat, liberation, and reconstruction aftermath

These images can be generated because the incidents and organizations are fictional and need unique compositions.

They should use 1936 to 1945 photographic technology, clothing, vehicles, architecture, and documentary framing.

Readable generated text, modern weapons, modern body armor, cinematic color grading, and real organization imagery are forbidden.

### News-art inventory

Major public milestones need wider news treatment.

Recommended news images:

1. first large coordinated international attack wave
2. first durable territorial extremist country
3. creation of the Jihadist International
4. activation of the Final Jihad
5. defeat of a major territorial network
6. defeat aftermath of The False Revelation

The False Revelation reveal itself uses dedicated super-event art.

### Leader portrait pool

The event can create many simultaneous fictional countries.

It needs a prebuilt portrait pool large enough to avoid obvious duplicate leaders in one campaign.

Recommended minimum full leader pool:

- `6` fictional military-command leaders
- `6` fictional clandestine or council delegates
- `6` fictional revolutionary or ideological leaders
- `6` fictional criminal-political leaders
- `6` fictional millenarian or cult leaders
- `8` fictional jihadist-route leaders
- `6` fictional institutional council portraits
- `1` False Revelation entity portrait

Total recommended leader and council masters: `45`.

The final count can rise after live carrier and simultaneous-actor limits are verified.

Every one-person portrait uses the `fictional_high_chaos` route through `chaosx_portrait_creator`.

Each portrait should have:

- `156x210` framing
- period photographic treatment
- role-specific clothing
- a memorable fictional motif
- varied age, gender, appearance, pose, and regional context without stereotype
- no real-person target
- no real extremist symbol
- no modern equipment
- no readable text
- matching name and gender metadata

Council portraits are fictional institutional assets and require explicit group or symbolic composition briefs.

The pool should be manually reviewed for accidental resemblance, repeated faces, stereotype, drift, and route mismatch.

### Advisor and commander portrait authorization

Separate advisor dossier portraits are not authorized as a blanket family.

The final country-package implementation should first determine which advisors or commanders add meaningful gameplay.

For the accepted minimum package, authorize up to `12` route-critical fictional characters across the shared actor framework.

Possible roles:

- field commander
- quartermaster
- civil administrator
- foreign liaison
- intelligence chief
- ideological organizer

A character used in both leader and advisor roles needs separate role-specific outputs and wiring.

Do not infer or generate a broad advisor roster from every focus or idea.

### False Revelation portrait animation

One animated entity portrait or transparent portrait overlay is authorized.

The animation should show subtle impossible change, such as unstable shadow, shifting reflected light, or a presence that appears optically inconsistent.

Requirements:

- separately generated or edited source frames
- stable identity, camera, framing, and anchor
- static `156x210` fallback
- horizontal frame-sheet PNG and DDS
- preview GIF for review only
- verified `.gfx` and GUI consumer
- no transform-only motion
- no simple filter pulse
- no fake sacred imagery

The animation should be reserved for the terminal state and removed when that leader is no longer active.

### Flag pool

The event needs enough flat fictional flags for simultaneous territorial actors.

Recommended minimum:

- `24` ordinary Event 31 base flag designs
- `8` jihadist-route flag designs
- `4` merger or transnational-command flag designs
- `1` final False Revelation flag design

Every design needs normal, medium, and small HOI4 variants.

All final flags use ImageGen and follow the flat flag workflow.

Required design qualities:

- strong geometry
- clear contrast
- readable small size
- no text
- no real organization symbol
- no sacred calligraphy
- no fabric folds
- no perspective
- no gradients or lighting
- no invented claim that resembles a real community symbol without review

The ordinary pool should cover military, clandestine, revolutionary, criminal-political, and millenarian profiles.

Jihadist flags should use wholly fictional geometric symbols and colors with no copied real emblem.

### Faction emblems

Required emblem families:

- regional Event 31 coordination structure
- transnational network confederation
- Jihadist International
- Final Jihad command
- possible anti-Event 31 terminal coalition only if the existing faction UI requires a dedicated emblem

Each emblem is a separate asset designed for the faction surface.

It cannot be a resized country flag.

### Focus icons

The shared focus framework needs a broad coordinated icon set.

Recommended minimum by branch:

- opening survival: `6`
- Shadow Council: `10`
- War Directorate: `10`
- Ideological Secretariat: `10`
- Captured Economy: `12`
- Armed Movement: `12`
- Network and Diplomacy: `12`
- Expansion and State Capture: `12`
- Crisis and Failure: `8`
- Jihadist International: `12`
- Final Jihad and terminal route: `10`

Recommended total: about `114` focus icons before exact tree count.

The implementation agent should finalize the count after the actual focus tree is built.

Each icon must be designed for `94x86` focus presentation.

Focus icons cannot be resized idea or decision icons.

### Idea and national-spirit icons

Required lifecycle families:

- Improvised Command and route upgrades
- Captured Economy and route upgrades
- Contested Legitimacy and route upgrades
- Presence of the Entity
- World in Revolt
- Supply Through Ruin
- government recovery and response-capacity ideas when implementation confirms they are persistent

Recommended planned total: `18` to `24` idea icons.

Each lifecycle stage needs a distinct compact `64x64` composition when the visible idea identity changes.

A minor numerical upgrade can reuse the same icon when the institution remains visibly the same.

### Decision and mission icons

Required government action families:

- response cell
- transport protection
- victim support
- intelligence sweep
- security surge
- targeted raid
- finance and corridor disruption
- allied intelligence
- defection channel
- movement restriction
- community-site protection
- sponsor exposure
- military reinforcement
- capital security
- enclave isolation
- relief corridor
- retake operation
- surrender negotiation
- foreign intervention
- reconstruction

Required actor action families:

- militia recruitment
- unit integration
- depot capture and repair
- external supply
- sponsor agreement
- foreign cell support
- actor merger
- faction leadership
- state offensive
- territorial administration
- jihadist unity
- coordinated uprising
- terminal command objective

Decision icons should use simple strong silhouettes designed for their actual final size.

Mission icons remain a separate family when the UI surface requires them.

### State-modifier icons

Required activity icons:

- dormant
- active
- entrenched
- armed insurgency
- lost local control
- recovery or restored authority

Additional state icons can cover:

- damaged transport
- relief corridor
- safe haven
- foreign corridor
- capital infiltration
- forced rule

These icons should remain readable beside state modifiers and map tooltips.

### Achievement icons

Part 12 defines `12` achievements.

Every achievement needs:

- completed `64x64` icon direction
- grey state
- not-eligible state
- stable achievement filename triplet
- event-specific symbolism

Achievement art must not reuse a focus or decision icon through resizing.

### Super-event images

Required super-event images:

1. The False Revelation reveal
2. Defeat of The False Revelation

Possible later major milestones can use normal news events unless implementation proves a separate super-event is justified.

The reveal image should be generated, period-authentic, ambiguous, and focused on the entity's appearance and human reaction.

The defeat image should show liberation, ruins, survivors, and the uncertain absence of the entity.

Neither image should depict Allah, sacred calligraphy, real extremist symbols, modern equipment, or fantasy concept-art framing.

### Super-event audio

Each super-event requires a unique licensed or public-domain musical recording.

The audio researcher must verify composition and recording rights separately.

The final cue should normally last one to two minutes and be converted to the established game-ready WAV format.

Generated audio, test tones, drones, sound-effect beds, Quran recitation, the call to prayer, Islamic sacred chant, unlicensed commercial recordings, and undocumented repository audio are forbidden.

The reveal and defeat need different tracks.

### Super-event text research

The final title, button text, quote, and cultural reference remain research-gated.

The text researcher should compare several candidates and record exact sources and confidence.

Preferred quote themes:

- false prophecy
- coercive belief
- deception
- idolatry
- judgment
- resistance to false authority
- survival after fanatic rule

The final quote should be concise enough for the UI and should avoid using Islamic scripture as hostile branding.

### Localisation direction

#### Event titles and reports

Use specific incident and state context.

Mention the affected state, government, organization, corridor, sponsor, or territorial actor when known.

Avoid generic crisis language, dramatic filler, and map-summary prose.

#### Organization names

Use fictional names that fit the profile and region without copying real organizations.

Do not place an ordinary ethnic, religious, or national group name beside a generic terror label.

#### Government decisions

Describe the action, exact target, resource commitment, public risk, and visible consequence.

Costs remain concise and icon-first.

#### Extremist-country focuses

Each route needs a distinct voice.

- Shadow Council uses controlled secrecy and internal discipline
- War Directorate uses military command and territorial necessity
- Ideological Secretariat uses doctrinal authority and state-building
- criminal-political variants use patronage, extraction, and coercive bargains
- jihadist variants use fictional absolutist religious claims while preserving clear opposition by Muslim actors
- terminal text focuses on the entity's command, uprisings, coercion, and uncertainty

Do not copy real propaganda or sacred text.

#### Muslim opposition

Describe local leaders, scholars, soldiers, communities, and governments rejecting the movement's claim, protecting civilians, preserving worship and public life, and supporting resistance.

Do not reduce the content to a disclaimer.

The opposition should appear in events, decisions, focus effects, and AI behavior.

#### Victims and civilians

Describe human consequences, emergency services, missing people, damaged transport, displacement, and reconstruction.

Avoid turning every death report into spectacle.

#### Event Details

Describe the premise and public progression.

Do not expose hidden readiness, exact probability, future surprises, or the identity of the entity.

#### Spreadsheet wording

Event details, evolution details, scenario details, and world-end details should match the final in-game wording.

The authoritative workbook remains the only editable catalog source.

### Source and manifest rules

Every asset package needs:

- source mode
- exact asset type
- stable filename
- target size
- final DDS path
- sprite proposal
- prompt or source record
- generated source PNG or archived source
- processed preview
- contact sheet
- status
- reviewer notes
- final runtime hash after wiring

Temporary work belongs under the event-scoped asset workspace while implementation is active or blocked.

Before full completion, durable provenance and handoff facts move into permanent event or plan documentation, runtime files move to engine folders, no runtime reference points into `docs/assets/`, and the temporary event workspace is deleted.

The durable portrait archive remains separate and is not deleted.

### Asset review gates

The asset package is complete only when:

- every accepted asset row has a runtime consumer
- no required asset remains a placeholder
- flags are flat and distinct
- portraits are fictional, varied, and free of real-person targeting or stereotype
- icons remain readable at final size
- transparent assets have real transparency
- no focus, idea, decision, mission, achievement, or faction family is satisfied by resizing another family
- super-event image, text, quote, and audio agree
- entity animation has real source frames and a static fallback
- no real extremist symbol or sacred hostile branding appears
- all final DDS files, manifests, and wiring handoffs exist

---

## Part 12: Achievement package

### Achievement design rules

Event 31 achievements should reward mastery of pressure, legitimacy, territorial war, cross-border networks, the manual scenario, actor play, and the world-end branch.

An achievement must require deliberate play.

It should not unlock from the first event popup, a passive threshold, a debug trigger, or a scenario setup before the player acts.

Each achievement needs:

- a stable internal ID
- public title direction or working label
- public description direction
- eligible countries
- exact unlock conditions
- disqualifiers
- persistent tracking
- difficulty rating
- visible or hidden status
- completed, grey, and not-eligible icon variants
- documentation and catalog coverage where relevant

The working labels below are not final localisation.

### 1. No Second Blast

- Proposed ID: `031_no_second_blast`
- Working label: No Second Blast
- Eligibility: any ordinary government affected by Event 31
- Difficulty: hard
- Visibility: visible

#### Unlock

Begin with at least `60` Terror Pressure and at least three active states.

Clear every active state and reduce Terror Pressure to zero within `180` days.

During the run:

- no new state becomes active
- no territorial actor forms
- no government-caused civilian death is recorded
- no abusive failure occurs

#### Disqualifiers

- force-trigger or debug bypass
- Global Jihad scenario setup
- changing away from the tracked country
- a new Event 31 firing that replaces the tracked crisis conditions

#### Why it is difficult

The player must combine protection, intelligence, precise operations, and recovery under a deadline.

#### Icon direction

A guarded city skyline behind one extinguished fuse or shattered detonator symbol, with no real device detail.

### 2. The Long Watch

- Proposed ID: `031_the_long_watch`
- Working label: The Long Watch
- Eligibility: any ordinary government
- Difficulty: hard
- Visibility: visible

#### Unlock

Experience five separate automatic Event 31 firings in the same country.

Clear every crisis without:

- losing a state to an Event 31 actor
- suffering a successful coup
- dropping Response Legitimacy below `50`

The country must end the fifth crisis at zero Terror Pressure.

#### Disqualifiers

- manual scenario launch
- force-triggered Event 31 firing
- tag switch away from the country

#### Why it is difficult

The player must manage recurrence over a long campaign and cannot rely on one extreme coercive response.

#### Icon direction

A period watchtower or guarded station with five marked lamps and a calm city below.

### 3. The City Still Stands

- Proposed ID: `031_the_city_still_stands`
- Working label: The City Still Stands
- Eligibility: any government with an active capital-seizure mission
- Difficulty: medium to hard
- Visibility: visible

#### Unlock

Prevent Capital Seizure while:

- Terror Pressure is at least `80`
- the country is already at war
- at least one non-capital state is Armed Insurgency or worse

Hold the capital through the mission and lower pressure below `60` within the following recovery window.

#### Disqualifiers

- moving the capital through a debug or unrelated forced effect during the mission
- scenario setup that begins after the capital mission already counts as complete

#### Icon direction

A fortified government building with intact lights behind damaged streets.

### 4. Cut Every Route

- Proposed ID: `031_cut_every_route`
- Working label: Cut Every Route
- Eligibility: any ordinary government or coalition leader
- Difficulty: hard
- Visibility: visible

#### Unlock

During one connected transnational crisis:

- break at least three distinct cross-border corridors
- expose or neutralize one sponsor
- eliminate one safe haven
- reduce Network Reach by at least one major stage
- clear every domestic Event 31 state

#### Disqualifiers

- corridors created and destroyed through repeated launch exploitation
- the network disappearing because every actor was removed by an unrelated terminal event before the player completes the objectives

#### Icon direction

Three broken transport lines converging on a sealed border gate.

### 5. The False Claim Rejected

- Proposed ID: `031_the_false_claim_rejected`
- Working label: The False Claim Rejected
- Eligibility: an ordinary Muslim-majority government identified through the event-local reaction registry
- Difficulty: hard
- Visibility: visible

#### Unlock

After Evolution IV:

- publicly reject the fictional jihadist movement through the eligible opposition chain
- maintain Response Legitimacy at `70` or above
- protect all threatened community and worship-site objectives
- defeat or force the surrender of the current Jihadist International faction leader
- remain independent

#### Disqualifiers

- joining or materially sponsoring the jihadist faction
- using collective punishment
- losing the tracked government through takeover

#### Why it is difficult

The player must combine military victory, civilian protection, and political resistance against an actor that prioritizes the country.

#### Icon direction

A fictional council seal and protected city gate facing a broken false crown, with no sacred calligraphy.

### 6. No Collective Punishment

- Proposed ID: `031_no_collective_punishment`
- Working label: No Collective Punishment
- Eligibility: any ordinary government fighting an Event 31 territorial actor
- Difficulty: very hard
- Visibility: visible

#### Unlock

Defeat or secure the full surrender of a territorial Event 31 actor while:

- Response Legitimacy never falls below `70` after the war begins
- no movement restriction exceeds its ordinary duration
- no abusive failure occurs
- no government atrocity or cover-up Condemnation source is recorded
- every recaptured state completes Restore Civil Authority

#### Disqualifiers

- annexing the actor through an unrelated console or debug path
- tag switching

#### Icon direction

A restrained sword beside an open relief gate and restored civic building.

### 7. The Enemy of My Enemy Is Still My Enemy

- Proposed ID: `031_enemy_of_my_enemy`
- Working label: The Enemy of My Enemy Is Still My Enemy
- Eligibility: any ordinary government or Event 31 actor
- Difficulty: hard
- Visibility: visible

#### Unlock

Defeat both:

- one Event 31 territorial actor
- one Event 14 cannibal actor

The two hostile actors must have shared a border or contested the same state during the campaign.

The tracked country must never ally, join a faction with, send volunteers to, or sponsor either actor.

#### Disqualifiers

- any formal cooperation with either actor
- one target disappearing through an unrelated cleanup before the player contributes materially to defeat

#### Icon direction

Two broken hostile emblems separated by one defended civilian settlement.

### 8. Fracture from Within

- Proposed ID: `031_fracture_from_within`
- Working label: Fracture from Within
- Eligibility: a player-controlled Event 31 territorial actor
- Difficulty: very hard
- Visibility: hidden until the player controls an eligible actor

#### Unlock

Enter the jihadist route after Evolution IV, then reject the dominant international leader and cause one of these outcomes:

- win the resulting leadership war
- split at least three member actors from the faction
- reduce International Unity below its lowest active stage

The player must remain independent at completion.

#### Disqualifiers

- accepting subordination to the final command
- winning only because an unrelated world-end branch deletes the faction

#### Icon direction

A fictional faction seal split through its center with three diverging banners.

### 9. Maximum Survivor

- Proposed ID: `031_maximum_survivor`
- Working label: Maximum Survivor
- Eligibility: the player country selected when Global Jihad launches at Maximum intensity
- Difficulty: extreme
- Visibility: visible

#### Unlock

Launch Global Jihad at Maximum intensity, then:

- survive without changing player country
- preserve or restore the original capital
- clear domestic Terror Pressure
- defeat every Event 31 territorial actor or end them through valid surrender and cleanup
- prevent The False Revelation or defeat it if it fires

#### Disqualifiers

- launch through debug bypass outside the scenario UI
- lower the selected intensity after confirmation
- tag switching
- an incomplete scenario ledger

#### Icon direction

A battered national capital surrounded by cleared crisis markers and broken faction emblems.

### 10. The False Revelation Denied

- Proposed ID: `031_false_revelation_denied`
- Working label: The False Revelation Denied
- Eligibility: any country fighting the final state
- Difficulty: extreme
- Visibility: hidden until the world-end branch begins

#### Unlock

After The False Revelation:

- contribute materially to recapturing at least one command capital
- help sever at least one strategic corridor
- restore at least one high-pressure country or defeat one major uprising
- participate in the final defeat or disappearance of the entity state
- survive the terminal campaign

#### Disqualifiers

- joining or submitting to the final state
- changing player country
- final defeat occurring without the tracked contribution thresholds

#### Icon direction

An ambiguous dark figure fading above a recaptured command hall at dawn, without sacred imagery.

### 11. Victims Before Victory

- Proposed ID: `031_victims_before_victory`
- Working label: Victims Before Victory
- Eligibility: any ordinary government with major Event 31 civilian losses
- Difficulty: hard
- Visibility: visible

#### Unlock

Before completing the final defeat of the connected organization:

- run victim support in every affected state with major civilian losses
- restore every destroyed critical transport link
- maintain protected relief access during the territorial phase
- finish with Response Legitimacy at `80` or above

The player must then defeat or secure the surrender of the organization.

#### Disqualifiers

- an affected state remains without completed recovery
- an abusive failure occurs after the support chain begins

#### Icon direction

Relief workers opening a restored railway station while soldiers remain outside the civilian area.

### 12. War Without a Capital

- Proposed ID: `031_war_without_a_capital`
- Working label: War Without a Capital
- Eligibility: any ordinary government
- Difficulty: extreme
- Visibility: hidden until the capital is lost to Event 31

#### Unlock

Lose the original capital to an Event 31 actor without capitulating.

Establish a valid backup capital, continue the war, retake the original capital, and restore civil authority there within one year.

The original government must survive and Terror Pressure must fall below `40` at completion.

#### Disqualifiers

- losing the country through takeover
- retaking the capital through an unrelated scripted transfer
- changing player country

#### Icon direction

A government seal carried from a dark temporary headquarters back to a restored capital skyline.

### Tracking requirements

The achievement system needs persistent tracking for:

- automatic versus manual firing
- player country at start
- tag-switch disqualification
- active crisis start date
- highest and lowest Response Legitimacy during the run
- government-caused civilian deaths
- abusive failures
- lost states and capital history
- corridor, sponsor, and safe-haven objectives
- Event 31 and Event 14 actor hostility and defeat contribution
- scenario type and intensity
- evolution and world-end state
- command-capital and corridor contribution
- recovery completion in each affected state
- force-trigger and debug disqualification

Tracking should use flags for boolean state and variables only for actual counts or thresholds.

Achievements must survive save and reload.

### Icon production

Every achievement needs one original completed icon designed for the achievement surface.

The grey and not-eligible variants follow the project achievement pipeline.

Achievement images cannot be resized focus or decision icons.

The icons should avoid real extremist symbols, graphic gore, sacred hostile branding, and readable generated text.

### Completion standard

The achievement package is complete only when:

- all `12` achievements have stable IDs
- unlock conditions and disqualifiers are implemented exactly
- manual and debug paths cannot grant automatic-play achievements
- tag switching is handled
- contribution achievements require real contribution
- hidden achievements reveal at the intended stage
- localisation and icon triplets exist
- tracking survives save and reload
- achievement docs and coverage tables match implementation

---

## Part 13: Documentation, catalog alignment, and acceptance

### Source-of-truth location

The completed specification package belongs under:

`docs/specs/031_random_terror_specs/`

Implementation plans, subagent handoffs, audit follow-up notes, blocked reports, and completion reports belong under:

`docs/plans/031_random_terror_plans/`

The final event documentation should use an event-owned folder under `docs/events/` that matches current repository convention.

The implementation agent must inspect the live repository before choosing exact documentation filenames.

### Catalog alignment

The authoritative catalog source is:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

The supplied CSVs are export-only snapshots.

They must not be edited directly.

After the workbook update, run:

`python .tools/export_event_catalog_csv.py`

The exporter should refresh the Events, Clusters, and Scenarios CSV snapshots.

### Event catalog row

Event 31 should contain player-facing fields aligned with final in-game wording.

#### Identity fields

- ID: `31`
- Event Name: `Random Terror`
- Type: `Minor Repeatable`
- Status after completion: the repository's accepted implemented or playable status
- Chaos level: `1` where the workbook exposes it
- Cluster ID: blank until Internal Fracture is formally registered, then the verified cluster ID
- Member severity: severe after cluster registration

#### Details direction

The detail should explain that several countries suffer fictional armed attacks in exact active states, governments manage a compact response, unresolved cells spread and organize, and severe failure can create coups, civil wars, territorial extremist countries, and international networks.

It should state that the later jihadist movement is fictional and that Muslim governments and communities can be among its main opponents.

It should not list raw modifiers, exact thresholds, hidden readiness, or the entity's true identity.

#### Evolution fields

The workbook should use the accepted names and public premises:

- Organized Cells
- Transnational Terror Network
- Territorial Insurgency
- The Jihadist International
- The Final Jihad

#### World-end field

Public title: The False Revelation.

The detail should explain that a united extremist movement accepts an ambiguous entity as divine and begins a terminal global conquest after substantial territorial and network success.

It must state that the game does not confirm the entity's identity.

#### Scenario field

The Event row can reference Global Jihad and direct the player to the Triggerable Scenarios entry.

### Scenario catalog row

Global Jihad needs one authoritative Scenarios-sheet row after its ID is verified.

Required fields include:

- stable ID, proposed `SCN-014`
- scenario name
- owner Event 31
- public details
- type selector descriptions
- Low impact
- Medium impact
- High impact
- Maximum impact
- launch limitations
- Final Jihad behavior
- False Revelation gate behavior

The wording must match the scenario UI.

### Cluster catalog row

The proposed Internal Fracture cluster should not be added until its members are ready.

When approved, the authoritative Clusters sheet should include:

- verified ID, proposed `9`
- name
- public premise
- minimum Chaos tier
- member list
- Event 31 severe role
- member availability and skip behavior
- cluster firing and history behavior

Until then, Event 31's Cluster ID remains blank.

### Event registration and status

Implementation should register Event 31 in the repeatable-event array and add it to the reworked-event default enable allowlist only in the same change that delivers the complete playable event.

The event must resolve through the shared type and name selectors.

It should show a live weight when available and `N/A` only when no valid target exists.

A partially implemented event should remain disabled by default.

### Event log history

The automatic global firing records one history row.

The row should show:

- Event 31
- Minor Repeatable type
- date
- meaningful primary actor or global context
- the affected-country count
- the public incident stage when useful

Follow-up national incidents do not create false global pacing rows.

Territorial actor formation, major attack waves, the Jihadist International, the Final Jihad, and the world-end branch can receive event-owned reports or evolution records according to their role.

### Default actor mapping

The generic fired-event handler records history before the entry event's immediate block can create a new actor.

Implementation should prepare any needed primary actor or representative target through the shared pre-fire helper before history recording.

If no meaningful actor exists, the row should use a global event context instead of a stale target.

### Evolution log coverage

Every recorded evolution needs consistent display across:

- main Evolutions tab
- selected History details related evolutions
- Event Details evolution catalog
- selected evolution detail title and body
- actor flag and name when relevant

History surfaces show real index and date.

The Event Details catalog does not show fake history metadata.

Disabled evolutions do not set recorded flags or unlock content.

### Event Details content

The Event Details page should include:

- event identity
- type
- current enabled state
- current weight or `N/A`
- fired count
- concise public premise
- five evolution rows
- one public world-end row
- actor display when a meaningful territorial organization exists
- scenario reference only through the normal scenario system

The public premise should describe the event's current idea and progression.

It should not expose implementation history, hidden formulas, secret variants, Apocalyptic Readiness, or the entity's identity.

### Public world-end row

The False Revelation requires:

- stable registry identity
- Event 31 owner ID
- one row
- independent persistent toggle
- default enabled state
- premise and terminal-state details
- broad current status when useful
- automatic-selection gate tied to the toggle

Toggling the branch must not disable Event 31, its evolutions, or another event's world end.

### Triggerable Scenarios UI

Global Jihad should use the existing data-driven scenario window.

Required UI behavior:

- stable sort order
- row selection
- detail update
- scenario-specific type cycle
- four-stop intensity slider
- current impact text
- confirmation window
- cancel behavior
- launch button state using the same eligibility as the launch effect

The scenario does not need dedicated art unless the current scenario UI cannot present its details.

A required technical sprite can use the established UI pattern, but a placeholder must be reported until replaced.

### Event documentation

The event documentation should explain:

- event identity and classification
- core values
- state activity stages
- targeting principles
- incident families
- response category and missions
- baseline territorial escalation
- five evolutions
- country package and focus framework
- Global Jihad scenario
- The False Revelation
- interactions with Event 14 and shared systems
- Deaths and Condemnation integration
- asset inventory
- AI and balance model
- achievement package
- debug and acceptance scenarios
- future cluster role

Player-facing documentation should not expose hidden route conditions or implementation-only variable names.

Technical docs can record stable identifiers, inputs, outputs, cleanup, and validation.

### System documentation updates

Implementation should update the owning documentation for:

- world-threat source registry
- special Chaos country classification
- country-carrier consumption
- scenario registry
- event log evolution and Event Details coverage
- Deaths reasons
- Condemnation source mapping
- event-owned state map mode
- any reusable dynamic effect or trigger created for several systems

A helper used only inside Event 31 belongs in Event 31 documentation.

It should not be added to the public dynamic helper registry merely because several Event 31 files call it.

### Technical identity proposals

The following identifiers are accepted working identities and need collision verification in the live repository.

- entry event: `chaosx.nr31.1`
- event actor marker: `random_terror_actor`
- takeover marker: `random_terror_takeover_country`
- ordinary crisis marker: `random_terror_crisis_active`
- world-threat source: `world_threat_source_random_terror`
- scenario ID: `SCN-014`
- future cluster ID: `9`
- world-end flag family: Event 31 False Revelation specific
- state map mode: Event 31 active-state map mode

The implementation agent can refine internal names to match repository style.

Public names, IDs, scenario title, evolution names, and world-end title remain stable unless a collision or research gate requires a reported change.

### Required implementation audits

#### Repository exploration

Map the existing Event 31 placeholder, event registration, event log, scenario registry, carrier registry, country collections, special-country trigger, world-threat aggregate, state map modes, decisions, focus-tree loading, achievement registry, assets, super-event slots, sound registry, and docs.

#### Event-chain MCP pass

Use event inspection and rendering before edits, then compare the final chain.

The pass should cover entry, national incidents, evolutions, territorial creation, scenario launch, and world-end transition.

#### Decision and mission audit

Check:

- action count
- cost variety
- four-cost limit
- mission count
- target validity
- AI
- cleanup
- exploit protection
- dynamic text
- category presentation

#### Focus-tree audit

Check:

- route coverage
- first-glance branch clarity
- layout
- prerequisites
- mutual exclusions
- search filters
- Focus Navigation
- AI
- idea lifecycles
- icons
- decision integration

#### Country-package audit

Check:

- carrier
- territory
- capital
- leader
- flag
- parties
- ideas
- forces
- technology
- supply
- focus loading
- AI
- merger
- split
- defeat cleanup

#### Localisation audit

Check every event, decision, mission, focus, idea, character, country, flag identity, achievement, Event Details row, evolution row, scenario row, world-end row, and scripted value.

#### Probability audit

Use the named scenarios in Part 9 for target selection, incident pools, response choices, route AI, evolution pacing, territorial creation, scenario AI, and world-end readiness.

#### Event completion audit

Compare every spec part, matrix, prompt, asset manifest, research handoff, and accepted improvement addendum with the final repository.

### Required implementation validation scenarios

#### V01 Baseline containment

A stable country receives one attack, uses intelligence and victim support, clears the state, and closes the category.

#### V02 Coercive recurrence

A country uses rapid coercion, clears the first cell, loses legitimacy, and receives a stronger later recurrence.

#### V03 Cross-state spread

A failed raid displaces survivors into a valid neighboring state after the cooldown.

#### V04 Transnational network

One organization connects several countries through a safe haven and corridor, then loses the corridor through joint action.

#### V05 Territorial creation

A valid actor seizes connected territory, receives a complete country package, and fights the parent.

#### V06 Parent viability

A small country reaches severe pressure without producing an invalid zero-state or capital-less parent.

#### V07 Government takeover

An actor captures the government and transforms the country without duplicating units or leaving stale response content.

#### V08 Actor defeat

The parent defeats the actor, restores authority, clears the carrier, and preserves history and Deaths.

#### V09 Cannibal rivalry

Event 31 and Event 14 actors share a border, remain unable to ally, and fight according to practical AI priorities.

#### V10 Evolution disable

Each disabled evolution leaves baseline progression playable and does not set its recorded state.

#### V11 Jihadist representation

Evolution IV creates a fictional movement, Muslim opposition content activates, and ordinary target scores remain identity-neutral.

#### V12 Global Jihad intensities

Low, Medium, High, and Maximum create distinct valid setups.

#### V13 Scenario cancellation and failure

Cancel changes nothing and a failed setup validation leaves no partial state.

#### V14 Final Jihad

Existing networks coordinate uprisings using real prior pressure and actors merge or subordinate safely.

#### V15 False Revelation blocked

The branch remains blocked below `1000` Chaos, when disabled, or without territorial proof.

#### V16 False Revelation transition

The branch sets one terminal state, assigns the entity, triggers valid uprisings, and freezes ordinary events.

#### V17 World-end counterplay

Coalition action against capitals, corridors, unity, and high-pressure countries weakens final abilities.

#### V18 Defeat aftermath

The final state is defeated and the aftermath, reconstruction, second super-event, and cleanup function.

#### V19 Save and reload

Ordinary crisis, territorial actor, scenario, evolution, and world-end state survive save and reload.

#### V20 Multiplayer

Several player countries receive one global firing without duplicate effects, and a player actor is not silently absorbed.

### Asset acceptance

The implementation must reconcile every accepted asset row with a final runtime consumer.

No required flag, portrait, icon, category picture, report image, news image, super-event image, animation fallback, achievement triplet, or audio cue can remain a placeholder in a completion claim.

The final asset manifest should show source, processing, final path, sprite, consumer, review, and hash.

### Documentation and temporary workspace cleanup

During implementation, event assets can use:

`docs/assets/031_random_terror/`

Before full completion:

- durable provenance, licensing, review, and crosswalk facts move into permanent docs
- final runtime files move into engine folders
- no runtime path points into the temporary workspace
- the temporary event workspace is deleted
- the durable portrait source archive remains

A missing temporary folder after proper cleanup is expected.

### Git and completion report

After each complete implementation plan, create a focused Git commit.

The final completion report should list:

- files changed
- event chain and registration
- decisions and missions
- evolutions
- country packages
- focus routes
- AI and probability evidence
- assets and audio
- achievements
- scenario
- world end and aftermath
- shared-system integrations
- docs and workbook updates
- meaningful validation findings
- unresolved blockers
- simplifications or fallbacks

No completion claim is valid while an accepted route, asset, AI surface, evolution, scenario intensity, achievement, world-end component, documentation row, or audit remains missing.

### Simplification reporting

The final implementation must report every deviation from this specification.

This includes:

- merged or removed decisions
- reduced country count
- reused portraits or flags
- missing focus routes
- missing AI
- missing animation
- missing audio
- unavailable carrier
- reduced scenario intensity
- weaker world-end ability
- hidden placeholder
- unvalidated probability
- stale documentation

The planning package itself uses no unapproved fallback or quick-output truncation.

Its deliberate exclusions are the custom unit family, 3D model package, and dedicated scripted GUI because the accepted design is stronger and cleaner with existing units and normal decision surfaces.

### Final acceptance statement

Event 31 is complete only when a normal automatic firing can progress through containment or territorial crisis, every evolution works and can be disabled safely, created countries are fully playable, Global Jihad supports all four intensities, The False Revelation meets the terminal contract, AI and assets are complete, shared systems agree, and the final repository passes the required audits without an unreported simplification.

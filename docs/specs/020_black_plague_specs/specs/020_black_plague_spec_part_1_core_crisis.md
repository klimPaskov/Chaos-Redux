# Event 20 Black Plague Specification, Part 1

## Core crisis and baseline outbreak

All route names, event labels, decision labels, country names, focus labels, achievement labels, and asset names in this specification are working labels, not final localisation.

## Event identity

Event 20 remains a **Minor Fire-Once** event because the random event picker starts it only once. The resulting disease system is persistent and can remain active for years. The first popup is therefore the ignition point of a long crisis, not the whole event.

The outbreak is a fictional Black Death strain with traits associated with several historical plague forms. It begins through an ordinary disease ecology of close contact, local vectors, crowding, and movement. Its lethality and rate of crisis escalation exceed the ordinary plague disease already present in the biological warfare system. The game must never treat it as a renamed copy of that disease.

The event promise is that one neglected mainland state can become the origin of a crisis that destroys a large share of its population, travels through war and transport networks, becomes a subject of medical and military competition, produces nonhuman rat states under severe escalation, and can eventually create a terminal Rat King world order.

The first weeks should create uncertainty and pressure without immediate mass extermination. The mortality curve becomes progressively steeper when disease load, time, movement, war, state collapse, and failed containment reinforce each other. A strong response can flatten that curve. A careless response can lose tens of percent of a state's population over a year. Evolved or rat-occupied outbreaks can destroy most of the human population in the worst states.

## Player experience

The intended player experience has six layers.

1. **Recognition**. A populous, neglected state begins reporting clustered illness and unexplained deaths. Countries with surveillance see the problem earlier and gain time to prepare.
2. **Containment choice**. The owner and neighbors decide how much economic and military capacity to sacrifice. Borders can close, ports can slow, divisions can be tied down, and hospitals can consume industry.
3. **Escalating mortality**. The state continues losing real population while the disease remains active. Deaths accelerate as disease load rises and medical systems fail.
4. **Regional spread**. Adjacent states, troop routes, occupied territory, refugees, and transport hubs carry the disease. Evolution II opens overseas port jumps.
5. **Medical and military competition**. Countries study samples, build countermeasures, share or steal knowledge, and may redirect the disease into a long weaponization project.
6. **Nonhuman collapse**. Evolution III can create Rat Nations in uncontrolled connected infection basins. Evolution IV unifies them under a sentient Rat King. Evolution V opens the route to the terminal scenario.

The player must be able to underreact and overreact. Underreaction preserves production and mobility while allowing more spread and death. Overreaction can save lives while damaging trade, supply, construction, stability, war support, relations, and military readiness.

## Initial outbreak selection

The event begins in exactly one eligible mainland state. The initial state is not chosen by continent and does not infect every country on a continent.

### Hard eligibility

An initial state must satisfy all of the following.

- It belongs to or is controlled by a living human country.
- It is not owned or controlled by a country classified as a special nonhuman country.
- It is not a wasteland or another state type that cannot sustain the disease system.
- It has a land connection to a meaningful continental landmass. Small isolated islands and disconnected island chains are excluded from the first outbreak.
- It contains a civilian population large enough for the outbreak to establish.
- It is not already carrying the Black Plague.
- It is not protected by a temporary hard immunity created by a recent successful disease cleanup.
- The event can identify a valid owner or controller for notices, decisions, and death attribution.

If no state satisfies the mainland requirement, Event 20 is unavailable and should display `N/A` in the event catalog weight surface. The implementation must not silently fall back to an island.

### Weighted preference

Eligible states receive a dynamic origin score. The score should strongly reward the combination of high population and weak capacity instead of rewarding either condition alone.

| Factor | Weight direction | Design purpose |
| --- | --- | --- |
| High civilian population | Very strong increase | The first state should be crowded enough to sustain a major epidemic |
| Low development or low state category | Strong increase | Favors neglected regions rather than the best prepared capitals |
| Poor infrastructure | Strong increase | Represents weak sanitation, slow medical access, and fragile transport control |
| Weak owner preparedness | Strong increase | Makes prior disease prevention materially useful |
| Low local medical capacity | Strong increase | Increases the chance that early cases remain uncontrolled |
| Occupation or high resistance | Moderate increase | Represents disrupted administration and concealment |
| Active frontline or heavy troop presence | Moderate increase | Creates a plausible movement and crowding route |
| Refugee or migration pressure | Moderate increase | Connects the outbreak to displacement systems when those are active |
| Port or major rail connection | Small increase | Helps the outbreak escape later without turning every origin into a major city |
| Capital state | Moderate decrease | Keeps origins focused on neglected regions unless the capital is genuinely vulnerable |
| Strong prevention laws | Strong decrease | Rewards national preparedness before the event fires |
| Existing hospital and surveillance investments | Strong decrease | Makes prevention visible in the origin roll |

The final score should use multiplicative or tiered interaction where possible. A very populous state with weak infrastructure should be far more likely than a sparsely populated state with the same infrastructure. A highly developed state with strong disease protection should remain possible but rare.

### Opening package

When the state is selected, the event creates the following baseline state.

- The origin state enters **Incubating** status.
- It receives a low initial disease load and a hidden early mortality pressure.
- Two to four nearby or strongly connected states receive **Threatened** exposure when valid.
- The owner receives access to the shared disease crisis board if it was not already available.
- Countries with sufficient surveillance receive an early report and can act before public recognition.
- Countries without surveillance see the crisis only after recognition or a neighboring alert.
- The event records the origin state and owner for event log history.
- The global Black Plague strain is registered in the existing biological warfare and disease systems.
- The world-threat source remains inactive until the crisis reaches a defined global danger threshold.

The opening must not cause a large one-time population loss. The first deaths occur through ongoing ticks and are intentionally low during incubation.

## Baseline disease state machine

The disease uses one state machine across natural outbreak, accidental release, overseas jump, and weaponized deployment. Provenance is tracked separately so the same containment and cure tools work everywhere.

### Clear

The state has no active infection and no current exposure pressure. It can still receive preparedness actions.

### Threatened

The state has meaningful exposure from an adjacent state, transport connection, port, troop route, refugee route, or known weapon threat. It is not yet losing population from the Black Plague. Threatened states unlock targeted inspections, medical buildup, movement control, and early warning actions.

Threatened status should decay if all exposure routes disappear and prevention remains strong. It should grow into Incubating if exposure pressure crosses the current protection level.

### Incubating

The disease is present but has not reached full public recognition. Deaths are small and spread is possible. Strong surveillance can reveal the state to its owner and selected allies. Poor surveillance can leave it hidden until disease load or death signals cross a recognition threshold.

Incubation normally lasts long enough for the player to react, with a dynamic target band of roughly two to six weeks. Evolution I, a weaponized seeding, a collapsing state, or a high existing exposure load can shorten this phase.

### Infected

The disease is publicly recognized. The state appears in the shared disease mapmode and crisis board. Population deaths, local manpower loss, construction disruption, supply damage, resistance pressure, and recovery penalties become increasingly severe.

An Infected state can move upward into Severe Crisis or downward into Contained. It cannot jump directly to Cured.

### Severe Crisis

Disease load, mortality pressure, and failed capacity have passed a major threshold. This is the state in which the event becomes genuinely frightening.

Expected consequences include:

- rapidly increasing civilian deaths
- severe recruitable population and local manpower loss
- large supply throughput and construction penalties
- resistance and compliance damage in occupied territory
- factory and infrastructure disruption
- weakened population recovery
- stronger spread emission into neighboring and connected states
- higher chance of administrative collapse
- eligibility for Evolution III rat emergence when wider conditions are also met

Severe Crisis should remain reversible with exceptional effort. It should not guarantee rat emergence or total population collapse.

### Collapsed

A Collapsed state has lost effective human control of the outbreak. Disease load is near its maximum, public administration has broken down, and ordinary treatment has little reach.

Collapse is a local state status, not a new evolution. It can occur before or after Evolution I. It is a major eligibility condition for rat emergence after Evolution III is enabled.

A human country can still attempt to retake control through army cordons, relief corridors, emergency hospitals, and cleanup. The cost should be extreme. Rat occupation can replace human collapse with a Rat-Controlled layer while leaving the disease status active.

### Contained

The state still carries the disease, but its effective reproduction and spread pressure are below the containment threshold. Deaths continue at a reduced rate. The player must maintain cordons, treatment, surveillance, and controlled movement.

Containment is fragile. Reopening too early, losing a hospital program, moving large armies through the state, or receiving a fresh exposure can cause relapse.

### Recovery

Disease load is declining and sustained containment has held long enough for cleanup. Recovery restores local systems in stages. Population does not return instantly. The state carries long-term demographic and economic scars.

Recovery decisions can rebuild hospitals, transport, local administration, and population growth. They should not replace lost population through a one-click reward.

### Cured

Active disease load has reached zero, no new exposure remains, and cleanup has completed. The Black Plague state modifier is removed and a temporary surveillance memory prevents immediate re-seeding from weak exposure.

A Cured state can be infected again by a major new exposure, a weaponized deployment, a severe overseas jump, or a Rat Nation occupation. A cure is a countermeasure, not permanent magical immunity.

## Disease values

Every affected state tracks a small set of meaningful values. These values should be shown in the shared disease interface rather than hidden entirely in script.

| Value | Meaning | Main sources | Main reducers |
| --- | --- | --- | --- |
| Disease Load | Amount of active Black Plague pressure in the state | time, incoming exposure, crowding, severe strain, rat control, weapon release | treatment, quarantine, cleanup, medical capacity |
| Mortality Pressure | How quickly population loss accelerates | disease load, elapsed time, state collapse, medical failure, Evolution I | hospitals, treatment progress, medicine, relief access |
| Spread Pressure | Chance and reach of outgoing infection | disease load, movement, ports, troop routes, refugees, open borders | cordons, border controls, port inspections, travel limits |
| Containment | Ability to keep the disease below crisis growth | preparation, divisions assigned, local administration, quarantine | war disruption, resistance, supply failure, panic |
| Treatment Coverage | Share of affected population receiving effective support | hospitals, medicine, cure progress, foreign aid | state collapse, blockade, damaged infrastructure |
| Relapse Risk | Probability that Contained or Recovery status fails | remaining load, rushed reopening, renewed exposure, war movement | monitoring, gradual reopening, strong prevention |
| Rat Infestation | Black Plague-specific vermin and nest pressure that increases transmission, mortality, and later rat emergence | dense cities, ports, warehouses, broken sanitation, food shortages, corpse accumulation, rat occupation | city rat clearing, sealed food stores, sewer clearance, shelter treatment, functioning administration |

Rat Infestation is visible only when the Black Plague is the selected disease. It can be implemented as a stored state value or a derived value from local conditions, but the player must see a readable band and the decisions that change it. The system should avoid creating additional state values unless implementation evidence shows they are necessary. Country and global values are defined in later parts.

## Mortality design

The disease kills real state population over time and records civilian deaths through the shared Deaths system. The effect must not be simulated only through recruitable population modifiers.

### Mortality curve

Mortality should follow a nonlinear curve. Early deaths are visible but limited. The curve steepens with disease load, elapsed untreated time, state collapse, and evolution stage.

The tuning target is expressed as cumulative outcomes rather than one fixed daily number.

| Response quality | About 90 days | About 180 days | About 365 days |
| --- | ---: | ---: | ---: |
| Exceptional preparation and treatment | 0.5 to 2 percent population loss | 2 to 6 percent | 5 to 15 percent |
| Strong but imperfect response | 1 to 4 percent | 5 to 12 percent | 10 to 25 percent |
| Weak response | 3 to 8 percent | 12 to 30 percent | 25 to 50 percent |
| Neglect or administrative collapse | 5 to 15 percent | 20 to 45 percent | 40 to 70 percent |
| Evolved strain or prolonged rat control | 8 to 20 percent | 30 to 60 percent | 60 to 85 percent or more in terminal states |

These are balance targets for untreated or continuously affected states. They are not guaranteed losses. Countries that intervene early should move toward the upper rows. A state that repeatedly relapses or remains under Rat Nation control can move toward the lower rows.

The normal disease system should preserve a small surviving population floor for nonterminal play so the state remains usable. The world-end sequence can override that protection because the campaign is entering a terminal state.

### Death attribution and downstream effects

Every mortality tick must:

- reduce the actual state population
- add civilian deaths to the shared Deaths tracker
- add the appropriate death log entry with country and state context
- allow the shared deaths-to-chaos conversion to operate
- update event-specific cumulative Black Plague deaths
- update rat emergence and Rat King thresholds where relevant
- avoid counting the same death twice through overlapping state effects

The disease should also damage local manpower, supply, construction, resistance control, and recovery. Those penalties should scale with the same disease state and should not be implemented as unrelated flat modifiers.

## Baseline spread before evolutions

Before Evolution II, the Black Plague spreads state by state through land and tightly connected transport routes. It cannot make ordinary long-distance overseas jumps.

### Land adjacency

Adjacent infected states create the strongest baseline exposure. Source disease load, target population, target preparedness, border policy, and local movement determine whether the target becomes Threatened or Incubating.

### Internal transport

States under the same controller can expose each other through railways, supply routes, strategic redeployment, and major population movement. Good infrastructure makes treatment easier but also allows uncontrolled travel to carry infection farther. This produces a real tradeoff instead of treating infrastructure as only good or only bad.

### Troop movement and war

Active fronts, strategic redeployment, large troop concentrations, occupied territory, and recently captured states increase spread pressure. Army routes can carry the disease across a border even when civilian travel is restricted.

A country can restrict troop movement through threatened regions, but doing so should reduce reinforcement speed, supply flexibility, planning, or front response.

### Refugees and occupied territory

A state with high resistance, collapsing administration, population displacement, or a recent front movement creates additional exposure to neighboring states. If Event 149 Immigration or another refugee system is active in a compatible form, the Black Plague should use its real migration routes rather than creating a duplicate refugee variable.

### Ports before Evolution II

Ports increase local spread and make a state more dangerous, but they do not create independent overseas jumps until Evolution II. Port inspections can still matter before that point because they reduce local exposure and prepare for the evolved stage.

## Outbreak reveal and event presentation

The event chain should reveal the crisis through player-facing observations rather than explaining hidden variables.

### Early owner report

Countries with surveillance receive an early report focused on clustered illness, sudden household deaths, missing workers, and overcrowded care sites. The text direction should identify the state dynamically and keep the cause uncertain.

Countries without surveillance receive a later report after death records, local movement, or hospital collapse make concealment impossible.

### Foreign awareness

Neighboring countries become aware when they border a recognized Infected state, receive a transport exposure, host returning troops, or share intelligence with the owner. Distant countries do not receive repetitive popups for every state. They see major milestones through news, the disease UI, and the event log.

### Major baseline milestones

The baseline event family should support the following milestone roles.

- initial owner recognition
- first neighboring exposure
- first foreign infection
- first state entering Severe Crisis
- first ten million event-attributed deaths
- first successful Containment state
- first Recovery state
- first Cured state
- first major relapse
- first known weaponization attempt
- global eradication

These are ordinary event-chain milestones, not evolutions unless an evolution threshold is explicitly met.

## Outcomes before rat emergence

The baseline crisis can end or stabilize in several ways.

### Local containment

The origin is contained before another state becomes infected. This is the best early outcome. The owner still pays recovery costs and the global strain remains known to the biowarfare system.

### Regional epidemic

Several connected states become infected, but coordinated containment reduces the disease to recovery. The event remains active until every state is cured or cleaned.

### Endemic danger

The world fails to eradicate the disease but keeps it contained in a small number of states. Monitoring, relapse, and cure work remain available. This state can last for years and still evolve if conditions worsen.

### Medical victory

The global outbreak is eradicated after at least one country reaches full countermeasure progress and every infected state completes cleanup. The disease remains available for historical event log and weaponization knowledge, but no active natural outbreak remains.

### Weaponized return

A country can reintroduce the disease after natural eradication through a completed weaponization project. The same state machine, mapmode, decisions, and cure protections apply.

## Event classification and cluster placement

Event 20 remains registered as a Minor Fire-Once event. It should become enabled by default only after the rework is implemented and audited.

The event belongs to the live **Diseases** cluster with **Severe** member severity. The registry assigns cluster ID `8`, and the cluster initially lists only Event 20 as a confirmed member. Event 41 Disease in Divisions and Event 163 Doctor Wu are related systems, but they remain outside the cluster until their own reworks define compatible cluster behavior.

The live implementation has resolved the numeric cluster ID as `8`. The catalog and event overview retain this ID as the source for Event 20 cluster references.

The normal random-event opening still begins in one mainland state. The triggerable scenario in Part 9 is a separate manual setup that deliberately bypasses the ordinary origin and evolution sequence for one instant multi-continent challenge. It must reuse this same disease identity and state machine rather than creating a parallel scenario-only plague.

## Connections established by the baseline

The baseline event connects to the following shared systems immediately.

- biological warfare disease registry
- shared disease prevention and selected-state containment decisions plus one dedicated Black Plague national cure and strategic-management category
- disease mapmode and selected state UI
- real population deaths and death log
- Chaos Meter deaths conversion
- air cleanliness outbreak contribution
- world threat framework when global danger thresholds are reached
- condemnation when a country weaponizes or deliberately releases the disease
- event log history and event details
- event cluster catalog

Later parts define the cure path, weaponization project, evolutions, Rat Nations, Rat King, focus trees, assets, AI, terminal world-end scenario, and the separate triggerable instant-chaos scenario.

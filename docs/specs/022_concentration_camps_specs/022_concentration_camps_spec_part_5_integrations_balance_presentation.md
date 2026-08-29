# Event 22 Concentration Camps

## Part 5: Integrations, balance, and presentation

## Integration principle

Event 22 is an entry and escalation event for systems that already exist in Chaos Redux. It should register its sites and actors with shared mechanics, call their public helpers, and let those systems own their normal consequences.

It must not duplicate:

- the Deaths ledger
- the Chaos Meter death conversion
- Condemnation thresholds and sanctions
- camp buildings and responsibility attribution
- chemical or biological contamination
- natural-disaster damage
- famine or migration population accounting
- country-specific German, Japanese, or Soviet camp categories
- the shared event log and event-details framework

## Deaths system integration

### Exact population removal

Every camp death must remove real state civilian population through `apply_exact_state_civilian_population_loss` or the current public replacement for that effect.

The caller must supply:

- requested people to remove
- protected minimum remaining population
- Event 22 Deaths reason
- target country for the ledger
- valid-target proof
- one-shot contract proof

The implementation must use the actual applied amount returned by the helper. It must not register the requested amount when the protected floor or rounding reduced the loss.

The helper already reconciles recruitable-manpower credit. Event 22 must not add a second manual manpower debit after a successful public-helper call.

### Event 22 Deaths reasons

The Deaths reason registry should distinguish at least these causes:

- concentration-camp detention and deprivation
- forced-labour overwork and accidents
- camp famine and starvation
- camp disease and medical neglect
- extermination-camp killing
- camp transport and deportation deaths
- forced evacuation or death march
- restricted chemical-site operation
- experiment-linked camp deaths
- evidence destruction and liquidation during retreat
- abandonment before relief
- post-liberation relief failure

The player-facing Deaths category can group these under a broader camp or state-atrocity heading while retaining cause-specific detail in tooltips and records.

### Dynamic detained population

Ongoing deaths should draw from an internal detained-population or workforce capacity, not directly remove a fixed percentage of the entire state every pulse.

The internal capacity is an abstraction based on:

- state population
- intake policy
- valid target source
- occupation and resistance
- refugee or displaced-person markers
- transfer decisions
- prior release, escape, death, or liberation
- network reach and transport capacity

It is not an ethnicity census. It must not be displayed as one.

Deaths reduce both the detained capacity and real state population. Release, escape, transfer, and liberation reduce the capacity without causing a death. New intake or transfer raises the capacity only through a visible policy, incident, or valid country adapter.

### Mortality pressure

A site's mortality request should be derived from:

- site type
- policy intensity
- local detained capacity
- food and medical condition
- forced-labour assignment
- terrain and climate
- famine and blockade
- disease or contamination
- bombing and infrastructure damage
- guard violence
- evacuation or retreat
- relief actions

Recommended design bands for a normal operation pulse:

- restrictive review produces low but nonzero mortality until release and closure are complete
- ordinary concentration-camp operation produces sustained moderate mortality
- forced-labour operation produces higher mortality that rises with quota intensity
- extermination operation produces severe mortality and rapid detained-capacity loss
- restricted chemical operation adds a stockpile-backed severe pulse
- retreat liquidation or a failed death march can create an exceptional one-time spike

Exact values belong in centralized constants and must be tested across small, medium, and large states.

### Chaos Meter

Event 22 should not add chaos directly for each action. The Deaths system already converts accumulated deaths into Chaos Meter growth under the shared rule. This prevents double counting.

## Condemnation integration

### Hidden and public layers

Event 22 adds hidden atrocity and cover-up evidence during operation. It adds a public Condemnation source only when discovery reaches the required confidence.

Public source families should distinguish:

- verified concentration and forced-labour network
- verified extermination network
- verified experiment sites
- verified restricted chemical sites
- verified forced evacuation or retreat liquidation
- verified cover-up and evidence destruction
- verified successor continuation

Each state source is added once per responsible actor and evidence generation. National network verification adds one bounded network source. Reopening the same report must not duplicate the public value.

### Condemnation outcomes

The shared Condemnation system owns diplomatic concern, censure, arms embargoes, strategic restrictions, total isolation, and pariah status. Event 22 provides:

- source severity
- confidence
- responsible actor
- discovery actor
- state and network identifiers
- cover-up bonus
- experiment or chemical bonus

Event 22 does not recreate sanctions in its own category.

### Genuine accountability

Transparent closure, relief, records, and trials can reduce future pressure or add mitigating sources where the Condemnation system supports them. Mitigation cannot remove the original history or reduce the Deaths count.

## Famine system integration

Camp famine can originate from:

- national famine
- blockade
- destroyed railways
- occupation supply policy
- crop failure
- ration diversion
- forced-labour quotas
- deliberate starvation
- overcrowding

Integration rules:

- the famine system owns the state famine modifier and general famine deaths
- Event 22 owns extra camp-specific mortality caused by restricted rations, confinement, and policy
- the two systems must share a causal context so one person is not counted twice in the same pulse
- relief supplies can reduce both famine pressure and camp mortality when delivered to the state
- guards, army, civilians, and detainees can become competing ration priorities
- deliberate starvation against a qualifying protected group can contribute to destructive-intent classification
- famine can create escape, revolt, epidemic, corruption, and discovery incidents

A future famine API should expose state severity and the amount already removed during the current causal segment. Event 22 should then calculate only the additional confined-population loss.

## Migration and refugee integration

Event 22 can create migration through:

- escape
- deportation and transfer
- camp closure
- liberation
- forced evacuation
- civil war
- survivor return or resettlement
- family reunification

Integration rules:

- deaths and migration are separate transactions
- migration should use the shared migration system when available
- the origin state must not lose the same people through both a migration transfer and a death transaction
- receiving states gain temporary housing, food, medical, and political pressure
- testimony can raise evidence confidence
- forced deportation should record the responsible actor and transport route
- return requires safety, border access, and destination capacity
- a receiving country can refuse, limit, or support admission, with visible consequences

Until the shared migration API exists, Event 22 should use bounded state and country markers. It should not create a permanent parallel population-transfer framework.

## Occupation, resistance, and garrison integration

### Occupation

Camps in occupied or non-core states should interact with:

- resistance target
- compliance
- garrison equipment and manpower
- supply and rail control
- local collaboration
- intelligence networks
- foreign observer access

Terror can lower open resistance for a short time in one state. It should also increase hidden opposition, escape support, sabotage, and long-term insurgency.

### Garrison burden

Every active site requires a guard burden. The burden scales with:

- site type
- detained capacity
- Resistance Pressure
- local terrain and infrastructure
- proximity to the front
- forced-labour intensity
- extermination intensity
- evidence or escape crisis

The burden can consume manpower and support equipment, reduce the effectiveness of occupation garrisons, or tie down divisions through missions. It must not be represented only by a small political-power cost.

### Resistance outcomes

High local pressure can cause:

- escape networks
- railway sabotage
- factory disruption
- guard ambushes
- document theft
- local uprising
- coordinated liberation attempt
- foreign intelligence access
- Event 31 terror or counterterror incidents
- Event 21 civil-war pressure after the purge reaches core supporters

Violent suppression can win one mission while worsening the long-term state.

## Disease, air cleanliness, and contamination

### Ordinary disease

Overcrowding, malnutrition, poor sanitation, damaged infrastructure, and lack of medicine raise camp disease pressure. Disease can spread beyond the site through guards, transports, escapees, refugees, or contaminated water.

### Air cleanliness

Low air cleanliness should raise respiratory illness, disease mortality, and recovery time in camp states. Camp smoke, industrial overwork, chemical accidents, burning records, bombardment, and nearby contamination can lower local air cleanliness where the shared system supports state contributions.

Air cleanliness does not serve as a cosmetic modifier. It should affect the camp epidemic mission and post-liberation relief.

### Black Plague and Event 20

When Event 20 plague exists:

- overcrowded camps are high-risk outbreak states
- plague deaths remain Event 20 deaths unless confinement or deliberate neglect caused an additional Event 22 loss
- Rat Nation or Rat King actors are excluded as normal Event 22 countries through the special-country trigger
- abandoned camps can become plague reservoirs
- humane relief can reduce spread while extermination or abandonment can accelerate it

### Biological warfare

A bioweapon strike or stockpile accident can contaminate a camp state. Event 22 handles confinement, relief, evidence, and operator choices. The biological system handles strain, contamination, outbreak, and disease spread.

An experiment site linked to Event 16 or a country package can add source-specific evidence and deaths. It must not grant Event 16 project progress unless that system explicitly authorizes the link.

### Chemical warfare

Restricted chemical-site operation uses the existing nerve-agent technology, stockpile-debit, contamination, and discovery contracts. A camp cannot create chemical stockpile, technology, or project completion.

A chemical accident can:

- kill detainees, guards, or nearby civilians
- contaminate the state
- interrupt operation
- reveal the site
- leave evidence after liberation

## Natural Disasters integration

Event 13 owns disaster targeting, warning, physical damage, and its own Deaths reasons. Event 22 supplies camp-specific aftermath hooks.

A disaster affecting a camp state can:

- damage or destroy the camp building
- interrupt food, medicine, water, rail, or power
- create escape or abandonment
- expose records or physical evidence
- increase disease and mortality
- force emergency evacuation
- create a relief mission for the responsible or liberating country

The caller should pass a bounded causal context. Event 22 must not invoke a second generic disaster merely because a camp exists.

## War and peace integration

### Random War and ordinary wars

War raises event eligibility through:

- occupied non-core territory
- prisoners and detainees
- labour and construction demand
- railway pressure
- security emergency
- front movement

Peace lowers some eligibility but does not automatically close sites. A regime can keep a peacetime repression network, while a successor can inherit one.

### White Peace Event 9

A white peace returns control without erasing camp evidence or survivor needs. If the responsible actor regains a state, operation resumes only through an explicit continuation effect.

### Nuclear and asteroid damage

Nuclear, missile, or asteroid damage can destroy a site and create a liberation or evidence crisis. Catastrophe deaths remain attributed to their physical cause. Event 22 retains pre-impact deaths and adds only distinct abandonment, confinement, or relief-failure losses.

## Event 5 Soviet Collapse

The Soviet adapter should bridge to Event 5:

- republics and successor states inherit sites they control
- original Soviet responsibility remains recorded
- a successor that continues gulag or extermination operation creates a new actor generation
- collapse can release detainees, expose records, or leave abandoned sites
- transport breakdown, famine, and local war can raise relief deaths
- successor governments can use disclosure to gain legitimacy or concealment to protect former officials

No successor should receive automatic guilt for operation it did not continue.

## Event 6 Independence Wave

A newly released country can inherit camp states from its former controller.

Possible outcomes:

- liberate and close the sites
- use records to expose the former ruler
- continue repression against rivals
- request foreign relief
- face displaced-person and return disputes

The Event 6 release package should call an Event 22 inheritance helper only for states that actually contain registered evidence or sites.

## Event 13 Natural Disasters

Event 13 hooks are described above. A camp state can also become a priority humanitarian target after a disaster. The disaster must not clear responsibility or discovery status.

## Event 16 Brilliant Scientist and Mengele routes

Event 16 can connect through:

- experiment-linked sites
- medical or biological projects
- clone, chemical, or special-project detainee use
- scientist or administrator defection
- discovery of experiment records

Rules:

- Event 22 cannot grant a random Event 16 technology for operating a camp
- experiment content must use Event 16's public bridge or country-specific package
- deaths, evidence, discovery, and liability remain Event 22 surfaces
- the Kruger State and nonhuman sovereignties require the special-country exclusion or a dedicated adapter
- Mengele-linked Germany uses the existing package and does not use a generic scientist event

## Event 20 Black Plague

The disease integration is described above. Plague can also create a cover-up conflict when a regime blames all missing detainees on disease. Verified records can expose the false attribution.

## Event 21 Random Civil War

Event 21 can be triggered or intensified by:

- purge broadening into core supporters
- military refusal
- security-service coup
- resistance uprising
- successor conflict over disclosure
- regional commanders retaining camps

Event 22 should pass pressure and actor context. Event 21 owns the civil-war creation and territorial split.

## Event 31 Random Terror

Event 31 can receive bounded hooks from:

- retaliatory attacks
- resistance bombing
- guard or administrator assassination
- extremist terror after closure
- witness intimidation
- cover-up murders

Event 22 should not treat every sabotage incident as Event 31. Use the link only when the incident becomes an independent terror campaign.

## Future occupation-law integration

A future occupation-law system can affect:

- intake rate
- forced-labour policy
- garrison burden
- target purpose
- visibility
- local compliance and resistance
- closure after liberation

Ordinary lawful occupation policy should not activate Event 22. The adapter requires arbitrary detention, persecution, forced labour, mass killing, or comparable abuse.

## Country politics and ideology

Ideology influences willingness and internal reaction. It does not automatically determine guilt or create a target population.

Relevant factors:

- authoritarian or totalitarian institutions
- radicalized focus route
- emergency law
- active occupation
- stability and war support
- security-service power
- democratic or judicial constraints
- civil-society and military objection
- previous atrocities and cover-up
- threat, defeat, and resource pressure

A democratic country can still receive Event 22 through occupation breakdown, civil war, extremist takeover, colonial abuse, emergency detention, or inherited sites. Its normal AI should strongly prefer review, closure, and relief unless its route has changed those institutions.

A fascist, communist, monarchist, or non-aligned country should not receive one generic behavior solely from ideology. Historical packages, route flags, institutions, and campaign state matter more.

## Country selection balance

The global event picker should use a complete candidate pool and explicit exclusions.

Positive eligibility factors:

- war and occupied non-core territory
- active civil war
- radicalized or repressive government route
- low stability and high security power
- labour, resource, or construction crisis
- existing quiet camp infrastructure
- inherited camp sites
- famine, migration, or resistance pressure
- prior Event 22 evolution availability

Negative or zero-weight factors:

- special Chaos country
- no eligible states
- recent transparent closure protection
- active liberation or relief government
- country already at the same firing stage with no valid incident
- invalid target source for an extermination-only opening
- one-state country whose only state is protected by the capital rule and no exception applies

The probability audit must prove that countries with no valid path have zero selection chance and that new countries are normally preferred over repeat incidents.

## AI policy profiles

The implementation should assign one current Event 22 AI profile to each affected country.

### Dismantler

Prefers:

- freeze intake
- food and medicine
- record preservation
- closure and release
- survivor relief
- public investigation after predecessor rule

Avoids:

- expansion
- forced labour
- extermination
- cover-up

### Restrictive reviewer

Prefers:

- inspection
- registration
- ration improvement
- limited detention review
- gradual closure

Can drift toward exploitation under severe war or industrial pressure.

### Exploitative authoritarian

Prefers:

- forced labour
- selected expansion
- guard reinforcement
- restricted access

Avoids extermination unless radicalization, target purpose, and route support exist.

### Extermination extremist

Prefers:

- Evolution I conversion
- targeted killing policy
- concealment
- forced evacuation or liquidation near defeat

Requires explicit extremist, historical, or high-chaos conditions. Ideology alone is insufficient.

### Cover-up escalator

Appears when Exposure is high or defeat is near. Prefers record destruction, relocation, staged inspection, and site demolition. It should still compare the risk of a failed cover-up with transparent closure.

### Retreat and collapse

Appears when front distance, supply, authority, or state control is collapsing. Prioritizes immediate state actions and can ignore long-term economic plans.

### Liberator and relief administrator

Applies to a new controller that does not continue operation. Prefers security, medical relief, survivor registration, evidence preservation, and transfer to safe accommodation.

The full scenario and ordering requirements are in the AI probability matrix.

## Tuning model

All important values should be centralized in script constants or one documented tuning file.

### Coverage anchors

- baseline opening target: 20 percent of eligible states
- ordinary generic expansion ceiling before Evolution III: recommended 35 percent
- Evolution III target and generic late-stage ceiling: 50 percent
- country-specific routes can exceed the generic ceiling only through an explicit accepted design

### Extermination share anchors

- Evolution I opening or active conversion: 50 percent of valid concentration camps
- further selected conversion can raise the share under an explicit extermination policy
- Evolution III guarantees at least the roughly even split
- the system never downgrades an existing extermination site automatically

### Pulse timing

Recommended starting bands:

- operation pulse: about monthly, with event-owned jitter or batching
- low-intensity review and closure check: slower than active exploitation
- exposure and resistance incident check: event-driven plus a bounded registered pulse
- same-country event refire protection: several months to more than one year depending on resolution
- transparent closure protection: longer than concealment or dormant-network protection

The implementation should avoid synchronizing every active country on the same day.

### Assignment strength

Starting balance direction for a fully staffed and supplied state:

- industrial assignment can provide a strong local factory-output increase
- construction assignment can provide a strong local construction and repair increase
- extraction assignment can provide a strong local resource-output increase
- logistics assignment can improve a real rail, depot, port, repair, or supply role

The bonus scales down with depleted workforce, low supplies, sabotage, disease, bombing, transport failure, and high Resistance Pressure.

A network-wide cap should prevent a large country from multiplying local bonuses into an unlimited national economy. The cap should depend on staffed sites, administration, trains, guards, and policy.

### Dismantlement burden

Closure duration and cost scale with:

- site count
- detained capacity
- extermination and chemical status
- records and missing-person condition
- contamination and disease
- state control
- transport access
- hardliner resistance
- current war and front distance

A small network can close in one regional mission. A half-country network requires several staged regional missions.

### Exposure and Resistance scales

Both values should use a documented bounded scale, recommended `0` to `100`.

Exposure thresholds should control:

- report confidence
- inspection pressure
- public discovery
- linked-site discovery
- cover-up risk

Resistance thresholds should control:

- escape missions
- sabotage
- guard burden
- armed uprising
- civil-war or terror links

The player sees bands and the next threshold. Intermediate formula components remain hidden.


## Recommended initial tuning values

These are implementation starting values for testing. Keep them in centralized constants. The probability and live-balance passes can change them after evidence. The implementation should preserve the relationships even when an engine limitation requires another modifier form.

### Detained-capacity initialization

| Site opening | Starting capacity direction |
| --- | --- |
| baseline concentration site | `0.5%` of current state population, minimum `2,000`, maximum `100,000` |
| forced-labour mobilization | can raise the site's target capacity toward `1.0%`, maximum `200,000`, through valid intake or transfer |
| security-expansion site | `0.75%` of current state population, subject to valid source capacity |
| Evolution I conversion | preserve existing detained capacity, no automatic refill |
| Evolution III new concentration site | `1.0%` of current state population, maximum `250,000` |
| Evolution III new extermination site | `1.5%` of current state population, maximum `300,000`, subject to valid source capacity |

No site can initialize more people than the active campaign source can supply. A minimum is ignored when the source, state population, or protected floor cannot support it.

### Operation pulse

Recommended base interval: `30` days with distributed offsets.

Recommended mortality request as a share of current detained capacity per normal pulse:

| State policy | Base request |
| --- | --- |
| restrictive review with adequate supplies | `0.25%` to `0.75%` |
| ordinary concentration-camp operation | `1%` to `2%` |
| standard forced labour | `2%` to `4%` |
| high-intensity forced labour | `5%` to `8%` |
| ordinary extermination operation | `10%` to `20%` |
| intensified extermination | `20%` to `35%` |
| restricted chemical-site additional pulse | `10%` to `20%`, only after successful stockpile debit |
| unstable post-liberation site without relief | `1%` to `5%` |

Pressure multipliers can raise or lower the request:

- adequate food, medicine, sanitation, and closure progress reduce it
- famine, plague, contamination, harsh climate, bombing, overcrowding, and high quotas raise it
- the combined normal-pulse request should be capped before an exceptional retreat or liquidation event is added
- all requests remain limited by detained capacity, current state population, and the protected population floor

Recommended exceptional one-time ranges:

| Incident | Loss direction from affected transferred or detained capacity |
| --- | --- |
| fully supplied transfer | `0%` to `3%` |
| disrupted transfer | `3%` to `15%` |
| forced march | `10%` to `30%` |
| retreat liquidation | `50%` to `100%`, limited by exact available capacity and state floor |
| abandoned site before relief | `2%` to `10%` |

Evolution II and Evolution III percentage shocks remain separate direct state-population effects and do not use these detained-capacity rates.

### Workforce condition multipliers

| Condition | Assignment output multiplier |
| --- | --- |
| full | `1.00` |
| strained | `0.75` |
| depleted | `0.35` |
| exhausted | `0.00` |

Additional recommended output multipliers:

- low supply: `0.50`
- active epidemic: `0.70`
- coordinated sabotage: `0.60`
- heavy bombing or broken transport: `0.50`
- successful guard and logistics support: up to `1.10`, never above the national cap

### Forced-labour assignment effects

Starting state-effect equivalents at standard intensity:

| Assignment | Standard effect direction | High-intensity ceiling before other multipliers |
| --- | --- | --- |
| industrial | about `+15%` effective output from factories assigned to the state | about `+30%` |
| construction | about `+25%` state construction and repair speed | about `+50%` |
| extraction | about `+20%` local resource output | about `+40%` |
| logistics | about `+10%` local supply contribution and `+25%` rail or depot repair | about `+20%` supply and `+50%` repair |

If the engine cannot provide one effect locally, implement a documented dynamic national equivalent scaled only by valid staffed assignment states. Do not silently turn every state assignment into a full national bonus.

Recommended generic national caps from Event 22 assignments:

- factory-output equivalent: `+20%`
- construction-speed equivalent: `+25%`
- resource-output equivalent: `+30%`
- supply or logistics equivalent: `+15%`

Country-specific systems can propose different caps through a separate accepted balance pass.

### Guard and transport commitments

Recommended per-site starting commitments:

- guard manpower: maximum of `500` and `0.5%` of current detained capacity
- support equipment: one per `1,000` detained people, minimum `25`, maximum `250`
- trains for a rail-linked active assignment: base `2` plus one per `20,000` detained people
- trucks for local assignment support: base `10` plus one per `2,000` detained people, capped through centralized constants
- overseas operation: minimum `5` convoys plus capacity scaling
- extermination, high resistance, or retreat emergency multiplies guard need by roughly `1.5`

The exact debit can be represented as a timed equipment commitment or decision cost according to current repository precedent. It must be real and refundable only through a valid wind-down or closure path.

### Visible value thresholds

Recommended `0` to `100` bands:

| Value | 0 to 19 | 20 to 39 | 40 to 59 | 60 to 79 | 80 to 100 |
| --- | --- | --- | --- | --- | --- |
| Exposure | controlled secrecy | persistent rumours | credible leaks | verified-site risk | publicly documented network |
| Resistance Pressure | disorganized opposition | escape networks | coordinated sabotage | armed resistance | administrative breakdown |

Recommended Network Reach bands:

- below `10%`: isolated sites
- `10%` to `19%`: regional network
- `20%` to `34%`: national network
- `35%` to `49%`: entrenched network
- `50%` or more: half-country network

The label can remain at the highest reached band when a country-specific route exceeds the generic late-stage ceiling.

### Time-to-consequence targets

Balance toward these campaign outcomes:

- standard forced labour should create a noticeable advantage for roughly `6` to `12` months when supplied
- continuous high intensity should create severe workforce, resistance, or exposure failure within roughly `12` to `24` months
- an ordinary extermination network in occupied or externally observed territory should become difficult to conceal within roughly one year
- a closed authoritarian core network can remain hidden longer when witnesses, foreign access, and state loss remain low
- a medium transparent closure should take roughly `180` to `360` days
- an Evolution III national closure can take up to `730` days and several regional missions
- post-liberation survival should demand action in the first `90` to `120` days

These are scenario targets, not guaranteed timers. War, famine, disease, state count, transport, resistance, and policy should move them.

## Exploit prevention

### No infinite workforce

- detained capacity is finite
- deaths, release, escape, and liberation reduce it
- intake requires a valid target source and visible action
- broad domestic purge has severe national costs
- site conversion does not refill capacity

### No free state bonuses

- assignments require a camp, workforce, supply, transport, and guard capacity
- invalid state roles cannot select the matching assignment
- bonuses decay when prerequisites fail
- one state cannot run several assignments at once
- extermination sites cannot keep forced-labour output bonuses

### No repeated evolution deaths

- store per-state, per-generation Evolution II and Evolution III markers
- conversion and controller change preserve markers
- pre-fire Evolution III skips the Evolution II opening shock

### No Condemnation farming or suppression loop

- each public evidence source is unique by actor, state, source family, and generation
- concealment can lower immediate Exposure but creates cover-up evidence
- reopening an inspection cannot repeatedly grant mitigation
- genuine closure mitigation is one-time and requires relief and records

### No easy building deletion

- deleting or losing the building does not clear evidence, responsibility, survivors, or relief
- scripted closure uses the full state transition
- player construction cancellation cannot remove an operational scripted site

### No puppet or annexation laundering

- original responsibility persists
- later operators receive their own generation
- annexation does not reset shocks or evidence
- puppet transfer records contributing orders where explicit

### No event-refire site multiplication

- an active country receives an incident, not another automatic 20 percent batch
- expansion uses policy decisions and caps
- same-country cooldown and protection are enforced

### No ordinary internment false positive

- lawful POW and civilian internment do not register
- humane medical quarantine does not register
- the event requires abuse conditions defined in Part 1

## Performance architecture

### Registered actors and states

Use event-owned arrays, targets, flags, or the current registered-system pattern to track only:

- active Event 22 countries
- active camp states
- liberated or closing states that still need pulses
- responsibility actors
- discovery and relief jobs

Do not scan every country or every state on daily or weekly on-actions.

### Delayed jobs

Large network creation, evolution conversion, percentage shocks, and liberation processing should use bounded delayed jobs or batched effects.

Each job needs:

- generation identifier
- target state and country proof
- expected controller or safe revalidation
- reason and stage
- cleanup after execution or rejection

### Trigger safety

Dynamic selectors should fail closed when:

- actor no longer exists
- state is invalid
- site was removed by a valid transition
- target purpose disappeared
- evolution is unavailable
- stockpile debit failed
- responsibility record is missing

A failure should not substitute another state, target group, or technology silently.

## Multiplayer behavior

- The affected player sees the opening and management event.
- Other human players receive public information only when their country has a valid witness, intelligence, diplomatic, liberation, or discovery relation.
- Secret evidence is not revealed globally through multiplayer UI.
- A player switching tags inherits the current country's visible category and state values without reinitializing the network.
- Simultaneous players controlling civil-war sides receive only the sites and responsibility generations they operate.
- Decision targets and saved event targets must be country-safe and must not use one global player selection for several countries.
- Pause-sensitive large sequences should use normal event pacing and not require every player to answer the same popup.

## Decision category presentation

### Category layer

Use the normal decision category with a static archival picture.

The header should present:

- current policy
- Network Reach band and percentage
- Exposure band
- Resistance Pressure band
- one current priority state or crisis

The header should not expose hidden evidence totals, target-census inventions, or a large formula ledger.

### Visual states

Use icons and short status labels for:

- stable operation
- closing
- high mortality
- high resistance
- discovery risk
- extermination
- chemical or biological danger
- liberation and relief

Colour must be paired with shape, icon, text, or frame changes.

### Map interaction

State-targeted decisions should highlight only valid states. Hover should show:

- why the state qualifies
- assignment or closure status
- cost summary
- main consequence
- blocked reason when invalid

Use existing state modifiers, building icons, target highlights, and the decision map as the complete map interaction layer.

### Category clutter

A phase normally shows three to five primary actions and one to three missions. Use replacement rules:

- opening options disappear after policy choice
- basic assignment decisions are hidden until a state is selected or eligible
- emergency retreat actions replace ordinary management in threatened states
- liberated states use a relief category or relief section, not perpetrator actions
- completed closure actions disappear
- country-specific packages replace generic duplicates

## Event, news, and sound presentation

### Report images

Use archival, non-graphic, documented photographs for grounded report events. Good subjects include fences, gates, barracks, transport infrastructure, records, empty sites, relief teams, displaced-person facilities, or liberation aftermath without graphic bodies.

### News images

Use black-and-white archival photographs for verified large networks, major liberation, or tribunal thresholds. Small incidents remain report events.

### Sound

Use a restrained existing event sound pattern. Avoid alarm, horror, or spectacle audio that turns the subject into entertainment.

## Localisation direction

### Naming

Use accurate terms based on the current site and policy:

- detention site
- concentration camp
- forced-labour camp
- gulag network
- extermination camp
- experiment site
- restricted chemical site
- liberated site
- survivor relief center

Do not call every detention genocide. Do not conceal extermination mechanics behind harmless production terms.

### Dynamic content

Text should name actual dynamic actors and places when available:

- responsible country
- current controller
- selected state
- occupied region
- policy
- site type
- valid target purpose
- current evidence confidence
- network reach
- liberation or closure stage

### Tone by surface

- opening event: grave administrative crisis with clear policy stakes
- perpetrator decisions: official, ideological, coercive, or evasive according to route
- witness reports: incomplete but concrete observations
- liberation: urgent relief and evidence preservation
- foreign reaction: political and humanitarian response grounded in confidence
- tribunal: documentation, responsibility, and institutional conflict
- achievements: recovery, rescue, evidence, and closure

Do not write exact final localisation in this planning pack.

## Asset summary

Event 22 needs:

- static decision category picture
- report images for activation, forced labour crisis, discovery, liberation, and closure or aftermath
- limited news images for verified network and major liberation
- decision and mission icons
- country and state idea icons
- achievement icons
- building or state-modifier icon review

The full required list and source modes are in the asset manifest.

## Documentation and catalog integration

Implementation should update:

- Event 22 source specs and implementation docs
- Camps and Genocide system documentation
- Deaths reason documentation
- Condemnation source documentation
- event log and detail text
- authoritative event catalog workbook
- cluster workbook row if Random Chaos is newly registered
- exported CSV snapshots through the repository exporter
- asset manifest and permanent provenance notes
- AI probability evidence
- live QA report

The current CSV export is read-only evidence. It must not be edited directly.

## Improvement-loop stop condition

The accepted planning scope is complete when the implementation contains:

- global event selection and coverage
- baseline decision loop
- all three evolution entry paths
- exact population loss and Deaths reasons
- discovery, liberation, relief, and accountability
- shared-system integrations
- AI profiles and probability evidence
- restrained assets and localisation
- docs, catalog, and validation

Once these surfaces pass acceptance, the improvement loop should issue a closure handoff. Broader expansion belongs in a separate accepted addendum supported by implementation evidence.

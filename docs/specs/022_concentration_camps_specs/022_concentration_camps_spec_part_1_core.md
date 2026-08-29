# Event 22 Concentration Camps

## Part 1: Core event architecture

## Catalog entry

- Event ID: `22`
- Event name: Concentration Camps
- Type: Minor Repeatable
- Status: To Be Reworked
- Cluster: Random Chaos
- Intended member severity: Severe
- Baseline availability: Calm World
- Evolution I association: Gathering Storm
- Evolution II association: Rising Chaos
- Evolution III association: Chaos Tier

The chaos tiers influence opening severity and evolution eligibility. They do not replace ordinary event progression.

## Shared pacing and repeatable weight

Event 22 uses the standard Minor Repeatable pacing contract.

- initial event weight uses the shared default, currently `1000`
- after a firing, current weight falls to `0`
- the event recovers by the configured monthly recovery rate, currently `20`, up to its current cap
- the cap is reduced by the configured factor after each firing, currently `50%`
- the normal default cap progression is `1000`, `500`, `250`, `125`, `63`, `32`, `16`, `8`, `4`, `2`, `1`
- Event 22 does not apply an extra private weight penalty or recovery loop
- eligibility, same-country cooldown, and transparent-closure protection still filter candidates after the shared weight roll
- a Random Chaos cluster firing applies Event 22's normal repeatable firing and cap change once, while the cluster remains one global pacing event

A repeat incident counts as an Event 22 firing because it consumed the global event slot. It must still pass the active-network incident gate. Force Trigger Mode can bypass ordinary selection for manual testing, but it does not prove normal weight, cap, recovery, or eligibility behavior.

## Event purpose

Event 22 is the generic world-level incident that creates, activates, or expands a camp network. The shared Camps and Genocide system remains the owner of camp buildings, responsibility attribution, ongoing population loss, evidence, discovery, condemnation, and tribunal pressure.

The event has four purposes:

1. It makes camp infrastructure a crisis that can appear outside the three existing historical country packages.
2. It makes dismantlement a costly process, so a country cannot remove the network with one harmless click.
3. It represents why coercive regimes may pursue detention and forced labour while showing the human, military, economic, and diplomatic damage that follows.
4. It connects camp sites to war, occupation, resistance, migration, famine, disease, chemical weapons, civil war, liberation, and regime change.

## Historical and legal boundary

The event distinguishes several concepts that should not be collapsed into one label.

- A concentration camp is an extrajudicial detention and repression site. It can also support forced labour, deportation processing, hostage taking, and political terror.
- A forced-labour camp extracts work under coercion. It can exist within a concentration-camp system or a gulag network.
- An extermination camp is designed around systematic killing. It can coexist with forced labour, but killing is its central function.
- A gulag network is the existing Soviet-specific forced-labour and repression building family. Event 22 can activate or connect to it, but it does not rename every gulag site as an extermination camp.
- A prisoner-of-war camp or lawful civilian internment site is not part of Event 22 merely because people are detained there. The event requires persecution, arbitrary mass detention, forced labour, extermination, severe deprivation, or comparable abuse.
- A camp system is not automatically genocide. Genocide requires the relevant destructive intent against a protected group. The game may still classify other conduct as persecution, mass atrocity, extermination, or crimes against humanity.

These distinctions control event text, discovery severity, foreign reaction, and achievement logic.

## Event ownership and shared-system contract

Event 22 must reuse the following shared surfaces:

- the `concentration_camp` state building
- the `extermination_camp` state building
- the `gulag_labor_camp_network` state building
- `genocide_responsible_country` attribution or its current repository equivalent
- the existing hidden camp evidence and cover-up evidence ledgers
- the existing genocide escalation, visibility, deaths, resistance, foreign pressure, cover-up, and discovered-site variables where they remain current
- the exact state civilian population loss contract
- the Deaths ledger and Chaos Meter death conversion
- the shared Condemnation source system
- the country-specific Germany, Japan, and Soviet camp categories
- the restricted chemical site, sarin, soman, contamination, and discovery systems

Event 22 may add event-owned state or country markers needed to distinguish one network generation, evolution shock, local assignment, labour depletion, closure, or relief status. It must not duplicate the shared evidence, responsibility, condemnation, or population transaction systems.

## Normal firing scope

A normal firing affects one eligible country.

The initial report goes to the selected country. Other countries do not receive a global popup merely because the hidden network exists. Foreign governments learn through leaks, intelligence, refugees, occupation, liberation, or public discovery.

A manual force trigger may bypass normal picker restrictions, but it should still fail cleanly when no eligible country or state exists. Force-triggered testing must record whether the trigger bypassed normal country weighting.

## Eligible country rules

A country can be selected when it:

- exists and controls at least one eligible civilian state
- is not a nonhuman, terminal, wasteland, or other special Chaos country whose population and government logic cannot support the mechanic
- is not already inside an incompatible country-destruction or total evacuation sequence
- is not protected by an active scenario rule that explicitly disables ordinary event interference
- can receive the management category or a country-specific camp-category handoff

The following factors increase selection weight:

- existing quiet concentration camps, gulag networks, or atrocity-site markers
- active war, civil war, occupation, or a large non-core population under control
- high resistance, low compliance, recent annexation, or mass refugee movement
- authoritarian, fascist, radical communist, militarist, colonial, or emergency-rule politics
- high extremist party support
- low stability, high war support, total mobilization, or severe manpower shortage
- previous use of repression, deportation, forced labour, chemical weapons, biological weapons, or unethical experiments
- a prior Event 22 network that was concealed, partially dismantled, or transferred to a successor
- higher chaos and active related cluster pressure

The following factors reduce selection weight:

- high stability, high compliance, no war, no occupied territory, and no extremist political pressure
- a recent transparent dismantlement with completed survivor relief
- strong rule-of-law or humanitarian route markers
- high public condemnation that already makes a new hidden network implausible
- a very recent Event 22 firing on the same country

A democratic country is not absolutely immune. In a low-risk democracy the opening should represent a security apparatus, emergency government, colonial administration, or radical faction attempting to create the network. The country receives stronger and cheaper closure options, and exploitative AI behavior should be close to zero unless the political situation has already broken down.

## Eligible state rules

An eligible state must:

- be owned or controlled by the selected country
- contain enough civilian population for the protected population floor to remain meaningful
- be a normal land state that can support the camp building and its state modifier
- not be impassable, empty, ownerless, submerged, a wasteland, or a special state reserved by another terminal system
- not already contain an incompatible duplicate site at the same building slot

Existing concentration camps, extermination camps, and gulag networks count toward coverage when compatible with the selected country’s package.

State selection uses weighted pools. Preferred states include:

- occupied or non-core states with resistance
- states containing railways, ports, mines, industry, or construction projects that can support a forced-labour assignment
- states near population centres but outside the capital when the network is still concealed
- states with refugee, minority, political-detainee, resistance, or country-specific persecution markers
- states connected to an existing camp network by rail or adjacency
- states with existing quiet camp infrastructure

The system should reduce weight for:

- the capital at baseline, unless the country is very small or no other valid state exists
- recently liberated states under active humanitarian relief
- states already suffering extreme population collapse
- states whose infrastructure has been destroyed so completely that a new site cannot operate
- isolated islands without the transport capacity needed for the selected assignment

The state pool must not infer ethnicity from state owner, core status, ideology, or cosmetic tag.

## Baseline coverage rule

On the first ordinary firing for a country, the event brings active concentration-camp coverage to 20 percent of eligible states.

- Round upward so a valid small country receives at least one site.
- Existing compatible active sites count toward the 20 percent target.
- Quiet sites can be activated before new buildings are created.
- A state cannot receive more than one primary camp type at the same time.
- Very large networks may be established over a short delayed sequence so the event does not create all buildings and reports on one frame. The final coverage still reaches the required percentage.
- Every created site stores the responsible country and the current network generation.

The initial event creates concentration camps only. Evolution I can convert part of the active network to extermination camps.

## Repeat firing behavior

Event 22 is globally repeatable. Repeatability should spread the mechanic without allowing one country to receive another free 20 percent batch every few months.

Country selection should normally prefer:

1. a valid country that has never received Event 22
2. a country whose previous network was completely dismantled and whose protection period has expired
3. a country with a dormant inherited network that has not yet entered the active loop
4. an active country whose network has reached a new crisis threshold and can receive an incident instead of new automatic coverage

When the selected country already has an active network, the repeat firing does not automatically add another 20 percent. It triggers one of the following context-sensitive incidents:

- a security apparatus attempts expansion into a new region
- a labour quota crisis develops
- evidence leaks from one site
- an epidemic or famine strikes the camps
- a resistance or escape network expands
- the front approaches a site
- a new government inherits responsibility
- a country-specific package takes ownership of the active network

A repeat incident can open a decision, mission, or state target. New coverage comes from the country’s decisions, an evolution, or a rare incident whose conditions clearly justify it.

## Same-country cooldown and protection

The same country receives a dynamic cooldown after a firing. The cooldown rises when:

- the country has a small number of states
- the network is still active
- the last incident created many sites
- the country recently completed a large management mission

The cooldown falls when:

- the network is expanding rapidly
- the country is at war and losing camp states
- resistance, exposure, or famine pressure is high
- an evolution has just activated
- a civil war or regime collapse has divided responsibility

A country that transparently dismantles all sites and completes survivor relief receives a longer protection period. Secret demolition without relief does not qualify.

## Initial event resolution

The opening report should state the visible facts without providing finished localisation. It should establish that detention sites now exist across several states, that local officials are already moving people and resources, and that the government must decide whether to stop, restrict, exploit, or expand the network.

The first response sets the opening policy and starts the relevant phase. The event should not resolve the full crisis in one option.

### Opening policy: immediate closure

- freezes new intake
- begins a national dismantlement burden
- lowers the ongoing mortality rate as supplies and medical access improve
- unlocks state closure missions
- raises hardliner or security-service resistance where relevant
- preserves evidence unless the player later chooses to destroy it

### Opening policy: restrictive review

- pauses expansion and the harshest assignments
- opens inspection, ration, registration, and release actions
- costs less immediately than full closure
- can drift toward closure or exploitation
- carries a risk that local administrators continue abuses during the review

### Opening policy: forced-labour administration

- activates labour assignments and strong local output choices
- diverts trains, guards, equipment, and administration
- increases death, resistance, disease, sabotage, and evidence pressure
- consumes a finite local detained workforce
- cannot be maintained indefinitely at full output

### Opening policy: security expansion

- increases Network Reach through targeted decisions
- emphasizes detention, deportation processing, and repression
- may lower short-term resistance target in selected states
- raises exposure, resistance, logistical burden, and later discovery severity
- is heavily restricted for lawful or humanitarian governments

Evolution I adds an extermination policy branch. It does not replace these baseline policies.

## Country-specific ownership

When the selected country has an established camp package, Event 22 should activate or intensify that package instead of presenting a duplicate generic system.

- Germany keeps its wartime camp administration, occupied Poland, extermination, deportation, experiment, and retreat-cover-up content.
- Japan keeps its forced labour, anti-partisan reprisal, prisoner experimentation, occupation records, and biological-warfare links.
- The Soviet Union keeps its gulag, deportation, famine, forced-labour quota, administrator purge, evidence destruction, and Soviet Collapse connections.

Event 22 still owns the world-level fire, coverage calculation, evolution entry, and event log. The country package owns country-specific decisions and localisation.

If a country-specific package is missing a required Event 22 action, implementation should add an adapter to that package. It should not expose two overlapping categories.

## Responsibility and succession

Every site retains a responsibility record.

- The builder or activating regime is the original responsible country.
- A new controller does not automatically inherit criminal responsibility merely by occupying the state.
- A controller that continues operation or reuses the site becomes a later responsible actor for its own generation.
- A successor government inherits the management burden and evidence. Its political liability depends on whether it continues, conceals, acknowledges, or dismantles the network.
- If the original country ceases to exist, its evidence remains on the state and in the event log.
- If a civil war splits the country, each side receives responsibility only for the sites it operates after the split, while the original pre-split evidence remains attributable to the former government.

## Baseline completion states

The ordinary event system remains active until one of these states is reached:

### Transparent closure

All sites are closed, survivor relief is complete, records are preserved or transferred to a tribunal, no new intake is active, and residual camp deaths have ended. This grants the longest refire protection.

### Secret demolition

All operational buildings are removed, but hidden evidence, missing-person pressure, and cover-up evidence remain. The network is not considered cleanly resolved and can return through discovery or a repeat incident.

### Dormant repression network

Sites remain but intake and high-intensity assignments are suspended. The country keeps low-level repression and evidence risk. The event remains registered and can reactivate.

### Entrenched exploitation network

Forced labour remains active and the network has become part of the wartime economy. It continues to generate pulses, labour depletion, resistance, and evidence.

### Extermination network

At least one extermination site is active. The system remains active until the sites are closed, liberated, destroyed, or the responsible regime disappears.

### Liberated network

The responsible country no longer controls the sites. Operations stop unless the new controller deliberately reuses them. Relief, evidence, displacement, and tribunal content continue under the liberator.

## Event logging

The event history should record:

- first network activation in each country
- repeat incidents that materially change coverage, policy, or responsibility
- every evolution entry
- public discovery of a network
- liberation of a large network
- complete transparent closure
- extermination-site activation
- chemical-site integration
- responsibility transfer or deliberate reuse by a new regime

Routine monthly or pulse deaths should use the Deaths log and should not spam the event history.

## Cluster role

The user-defined cluster role is Random Chaos. Event 22 is a Severe member because it can create widespread state modifiers, deaths, internal resistance, and international consequences.

The current cluster CSV export does not contain a registered Random Chaos row. Implementation must inspect the authoritative workbook and current repository registry, then create or recover the cluster with a collision-free ID. The spec does not assign a numeric ID from an incomplete snapshot.

Event 22 must remain fully functional outside cluster firing. A cluster firing cannot bypass the event’s valid-country and valid-state checks.

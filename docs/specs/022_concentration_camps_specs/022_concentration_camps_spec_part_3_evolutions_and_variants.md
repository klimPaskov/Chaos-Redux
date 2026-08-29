# Event 22 Concentration Camps

## Part 3: Evolutions and campaign variants

## Evolution architecture

Event 22 has three evolutions. Each evolution changes the rules of the active camp system and also changes the opening package when the event first reaches a country after that evolution is already available.

The event must support both entry paths:

- **Active-network entry** applies the new rules immediately to countries whose Event 22 network is still active.
- **Pre-fire evolved entry** changes the first Event 22 firing for a country that has not yet received the event.

An evolution is logged once per country and once in the global evolution history. Routine baseline incidents are not logged as evolutions.

The implementation must store a network generation and per-state evolution-shock markers. These markers prevent duplicate population shocks after save and reload, state transfer, building conversion, or repeated event firing.

## Evolution I: Extermination network

### Core change

Evolution I converts 50 percent of the selected network's existing concentration camps into extermination camps when the evolution first reaches that network.

The conversion changes the purpose of those sites. Killing becomes the central operation. Forced labour can still occur before death, but extermination sites do not provide a stable industrial, construction, extraction, or logistics assignment bonus.

This evolution opens the most severe policy family, raises death pressure sharply, increases Resistance Pressure, creates much stronger hidden atrocity evidence, and makes public discovery far more damaging.

### Active-network entry

When Evolution I activates for a country with an existing Event 22 network:

1. Count all active Event 22 concentration-camp states in the current network generation.
2. Exclude sites already closing, liberated, destroyed, or controlled by a country that is not continuing operation.
3. Calculate 50 percent of the remaining concentration camps.
4. Convert `floor(valid_site_count / 2)` sites. This leaves the extra site as a concentration camp when the count is odd and converts at least one site whenever two or more valid sites exist.
5. If only one valid concentration camp exists, convert it only when the responsible regime has chosen an extermination policy or meets an extreme AI profile. Otherwise, flag it as a conversion target and open an immediate crisis decision.
6. Convert the selected sites through the shared camp-building and responsibility helpers.
7. Preserve the original responsible actor, network generation, evidence, detained-workforce record, and state history.
8. Replace incompatible forced-labour assignments with an extermination-site state status.
9. Start the evolution-specific death and resistance pulses.
10. Log the conversion count and the responsible actor.

The event should use a short delayed sequence for large networks so reports, building changes, and state updates do not all occur on one frame.

### Pre-fire evolved opening

When a country receives Event 22 for the first time after Evolution I is available:

- bring total active camp coverage to 20 percent of eligible states
- split the opening sites as evenly as possible between concentration camps and extermination camps
- use concentration camps for the extra site when the total is odd, unless the country has chosen an explicit extermination opening
- assign responsibility and the current network generation to every site
- open the extermination policy family immediately
- do not apply the Evolution II or Evolution III population shock unless those evolutions are also active

The opening report should make clear that some sites are detention and forced-labour facilities while others are organized killing sites. Final wording must use country and campaign context instead of a generic historical label.

### Conversion-state selection

Conversion should not be uniformly random. It should prioritize states that fit the active regime's logistical and targeting conditions.

Higher selection priority:

- occupied or non-core states controlled by the responsible country
- states with a registered persecuted population or country-specific target-group marker
- states connected by rail to the responsible country's core territory
- states with an existing detention, deportation, experiment, or restricted-site role
- states with low foreign access and strong regime control
- states close to large detained populations or transfer routes

Lower selection priority:

- the capital
- states already close to liberation
- states with no transport link
- states with severe contamination that would make operation impossible
- states under an active transparent inspection or closure mission
- states whose population is already at the protected floor

The selection logic must not infer ethnicity from ownership, cores, ideology, or cosmetic tags.

## Target purpose and intent

### Why target purpose is required

The rough concept asks for killing directed at other ethnicities and later broadening into the regime's own population. HOI4 does not provide a reliable ethnicity-demography system, so the event must use a controlled target-purpose registry.

Every extermination policy stores a target purpose. It describes who the regime is persecuting in campaign terms and why the network is operating. This affects event text, resistance, discovery classification, foreign reactions, and the legal label used by the documentation system.

### Target-source hierarchy

Use the first valid source in this order:

1. **Country-specific protected-group registry**
   - used only when an established historical or alternate-history package defines a real persecuted national, ethnic, racial, or religious group
   - requires its own sourced localisation and trigger contract
   - can support a genocide classification when the required destructive intent is also established

2. **Occupied or non-core civilian population**
   - used for occupation terror, deportation, population removal, reprisals, and settler or annexation programs
   - does not automatically establish genocide

3. **Refugee, migrant, displaced-person, or minority markers**
   - used when another event has created a real campaign population marker
   - the marker must identify the population without inventing state percentages

4. **Resistance-linked detainees and hostage populations**
   - used during occupation, counterinsurgency, or civil war
   - increases local resistance and reprisal cycles

5. **Political, ideological, religious, or social enemies defined by the regime**
   - used for purges, class repression, opposition detention, and security-state campaigns
   - usually classified as persecution or crimes against humanity unless a protected-group genocide condition is separately met

6. **Broad domestic purge**
   - used only after the network has exhausted or lost access to its earlier target source and the regime deliberately continues
   - affects core-state population, officials, soldiers, workers, and former supporters
   - marks the regime as consuming its own social base

The player-facing text should name the campaign category when known. It must not claim a census or group distribution that the game does not track.

### Specific destructive intent

The genocide classification requires all of the following:

- a qualifying protected-group registry
- a policy or event establishing intent to destroy the group in whole or in substantial part
- an active extermination, lethal-deprivation, birth-prevention, child-transfer, or comparable destructive program represented by the campaign
- responsibility attribution to the acting regime

Without those conditions, the system should use a more accurate classification such as mass detention, persecution, forced labour, extermination, mass killing, or crimes against humanity.

This distinction is documentation and reaction logic. It does not reduce the Deaths count or the seriousness of other mass atrocities.

## Evolution I policy family

### Convert a selected concentration camp

Purpose: turn one active detention site into an extermination site after the automatic evolution conversion.

Requirements:

- Evolution I active
- selected state contains an active concentration camp attributed to the acting regime
- state is not closing, liberated, or under binding inspection
- valid target purpose remains
- extermination share is below the route's current cap or an extreme route has explicitly removed that cap

Costs and commitments:

- trains or convoys where transport is required
- support equipment and guard manpower
- administrative or political commitment
- transport and supply burden

Effects:

- replaces the concentration camp with an extermination camp
- removes the state's forced-labour assignment
- raises Exposure, Resistance Pressure, hidden atrocity evidence, and death pressure
- increases the future discovery and tribunal severity of the site
- records the conversion date and responsible actor

### Establish a killing program

Purpose: choose the national target purpose and operational intensity of the extermination network.

The decision should offer only target purposes that are valid in the current campaign. A country with no valid registered group, occupied population, resistance population, refugee marker, or political purge context cannot invent one merely to use the decision.

Intensity directions:

- restricted lethal program
- systematic extermination program
- emergency liquidation during retreat

The final labels must fit the actor and should not sanitize the conduct. Higher intensity causes more deaths and shortens the network's time before resistance, exposure, labour loss, or collapse becomes severe.

### Halt extermination operations

Purpose: stop the killing program without pretending that the site and its victims disappear.

Effects:

- ends the extermination pulse
- converts the site into a secured detention and relief state pending closure, or leaves the extermination building inactive until a proper conversion helper is completed
- preserves evidence
- raises short-term hardliner conflict
- opens food, medical, registration, and release missions
- does not restore population or erase responsibility

### Broaden the purge

This decision appears only when the earlier target source is exhausted, inaccessible, or deliberately abandoned and the regime refuses to close the network.

Effects:

- allows intake from the responsible country's own core population
- raises short-term security-apparatus and hardliner control
- sharply reduces stability, recruitable population, officer loyalty, factory reliability, and administrative capacity
- raises Resistance Pressure and civil-war risk
- creates purge-of-the-perpetrator evidence and country-specific internal opposition events
- can trigger Event 21 Random Civil War or Event 31 Random Terror links

This route is a failure spiral. It is not an efficient way to refresh the detained workforce.

## Restricted chemical-site integration

Evolution I can connect a limited number of extermination sites to the existing restricted chemical-site system.

### Historical accuracy boundary

Historical Nazi killing centers used carbon monoxide and hydrogen-cyanide pesticide formulations such as Zyklon B. The Event 22 sarin or soman route is alternate-history Chaos Redux content tied to the mod's existing nerve-agent technologies. Player-facing text and documentation must not present nerve-agent integration as historical fact.

### Requirements

- Evolution I active
- existing sarin or soman technology and its valid project prerequisites
- a steady usable stockpile of the required agent or delivery material
- an eligible extermination site
- restricted-site capacity below the centralized cap
- no active dismantlement, liberation, or transparent inspection at the state

### Operation contract

A restricted chemical site:

- consumes a real stockpile amount on every operation pulse
- cannot operate when the stockpile debit fails
- raises deaths sharply for that pulse
- increases contamination and accident risk
- creates source-specific hidden evidence
- raises later discovery condemnation
- increases guard and specialist burden
- can poison workers, guards, nearby civilians, or infrastructure after an accident
- must use the shared Deaths and contamination systems

The decision should never describe technical procedures, equipment construction, or operational methods. It is a strategic stockpile and consequence mechanic.

### Failure and interruption

Operation stops when:

- stockpile is exhausted
- the site is bombed, liberated, closed, or contaminated beyond its operating threshold
- the responsible government changes policy
- the state changes controller and the new controller does not continue operation

A failed restricted site can leave contamination, survivors, destroyed records, and stronger physical evidence.

## Extermination route benefits and costs

The route may provide temporary internal benefits that explain why an extremist regime continues it:

- short-lived hardliner support
- temporary security-apparatus obedience
- temporary reduction of open opposition in heavily terrorized states
- confiscated property or budget relief that decays into corruption
- temporary control over occupied transport corridors

It must also create larger and growing costs:

- high civilian deaths
- major labour and demographic depletion
- resistance, sabotage, escape, and armed opposition
- guard and transport consumption
- reduced factory reliability and railway efficiency
- military objection and desertion
- disease and famine pressure
- foreign intelligence attention
- extreme exposure and condemnation after discovery
- tribunal and regime-change liability
- loss of administrative capacity when the purge broadens inward

No extermination-site modifier should grant stable factory output, construction speed, or resource extraction.

## Evolution II: One-percent camp-state loss

### Core change

Evolution II applies one exact population loss equal to 1 percent of current state population in every state containing an active Event 22 camp.

The shock represents a synchronized escalation in deprivation, killing, disease, transport deaths, overwork, and administrative violence. It is not the only source of camp deaths. Continuing operation still uses the dynamic pulse system.

### Active-network entry

For each active camp state in the current network generation:

1. Calculate 1 percent of the state's current civilian population at the moment of application.
2. Clamp the request against the shared protected population floor.
3. Apply the exact loss through `apply_exact_state_civilian_population_loss`.
4. Register the actual amount removed in the Deaths ledger with an Event 22 evolution reason.
5. Reconcile any recruitable-manpower credit through the shared helper.
6. Mark the state as having received the Evolution II shock for this network generation.
7. Add local evidence, Resistance Pressure, and relief burden in proportion to the actual loss.

The effect must never use a manpower-only modifier as a substitute for population loss.

### Pre-fire evolved opening

When a country first receives Event 22 while Evolution II is active but Evolution III is not:

- create the applicable baseline or Evolution I opening network
- finish responsibility and state registration
- apply the 1 percent shock once to every new active camp state
- mark every affected state before the normal pulse begins

### New sites after Evolution II

A site added after Evolution II is active receives the 1 percent shock once when it becomes operational in the current network generation. Moving or converting the same site does not apply the shock again.

A state that closes all sites and later receives a genuinely new Event 22 network generation can receive a later evolution shock only if the repeat-firing and protection rules allow a new network.

### Protected floor and tiny states

The shared protected population floor prevents a single percentage effect from emptying a state. When the calculated request is below the engine's meaningful whole-person threshold, the applied loss can be zero. The state still receives the evolution marker so repeated evaluation does not accumulate rounding exploits.

## Evolution III: Half-country network

### Core change

Evolution III brings total active camp coverage to 50 percent of the selected country's eligible states. The resulting network is split as evenly as possible between concentration camps and extermination camps.

Every active camp state receives a one-time exact population loss equal to 2 percent of current state population for the Evolution III shock.

### Coverage calculation

1. Rebuild the eligible-state pool using the normal state rules.
2. Count all active Event 22 concentration and extermination camp states in the current network generation.
3. Calculate the target as 50 percent of eligible states, rounded upward.
4. Add only the number of sites required to reach the target.
5. Determine an even concentration and extermination split across the final target count.
6. Convert or add sites as needed, while preserving any extermination share already above the minimum split.
7. Never downgrade an extermination site automatically to make the split exact.
8. When the final count is odd, concentration camps receive the extra site unless the country has an explicit extermination-dominant route.
9. Store the final coverage and split in the event log.

Existing gulag sites can count toward reach when the Soviet package marks them as active Event 22 sites. They are not automatically renamed or converted. The country-specific adapter decides how they affect the concentration and extermination split.

### Active-network entry

An active country receives:

- the coverage expansion to 50 percent
- enough conversion to ensure at least the intended extermination share
- the Evolution III 2 percent shock in every active camp state
- an immediate national network crisis report
- stronger resistance, transport, supply, evidence, and administrative burdens
- emergency closure and regional relief missions if the government opposes the expansion

A state that already received the Evolution II 1 percent shock can also receive the later Evolution III 2 percent shock. The two represent separate escalations at different moments.

### Pre-fire evolved opening

A country whose first Event 22 firing begins at Evolution III receives:

- 50 percent total eligible-state coverage
- an even concentration and extermination split
- the 2 percent Evolution III shock once in each camp state
- no separate 1 percent Evolution II shock for that opening
- the full late-stage decision category immediately

This prevents a pre-fire evolved opening from taking an unintended 3 percent stacked loss before the player receives control.

### New sites after Evolution III

A new site created later in the same network generation receives the Evolution III 2 percent shock once when it becomes operational. It does not also receive the Evolution II shock.

### Strategic consequences

A half-country network should alter national strategy:

- rail and convoy capacity becomes a binding constraint
- guard manpower and support equipment compete with the army
- factory and resource output becomes unreliable under sabotage and workforce collapse
- local famine, disease, and migration become common
- foreign intelligence and resistance networks gain many access points
- exposure becomes difficult to suppress
- a losing war creates several simultaneous retreat and liberation crises
- broad domestic purges can fracture the officer corps, party, bureaucracy, and industry

The event should be severe enough that even an extremist AI must choose priorities instead of operating every site at maximum intensity.

## Evolution sequencing and shock matrix

| Network entry state | Opening coverage | Opening site split | Population shock on opening |
| --- | --- | --- | --- |
| Baseline only | 20 percent | concentration camps | continuing dynamic operation |
| Evolution I active | 20 percent | roughly half concentration and half extermination | continuing dynamic operation |
| Evolution II active without Evolution III | 20 percent | depends on Evolution I | 1 percent in every camp state |
| Evolution III active before first firing | 50 percent | roughly half concentration and half extermination | 2 percent in every camp state |
| Active baseline network gains Evolution I | unchanged reach | convert 50 percent of valid concentration sites | continuing dynamic operation |
| Active network gains Evolution II | unchanged reach | unchanged | 1 percent in every active camp state |
| Active network gains Evolution III | expand to 50 percent | ensure at least even split | additional 2 percent in every active camp state |

A conversion, controller change, save reload, or repeated incident must not reapply a shock that the state already received for its network generation.

## Campaign variants

The event should choose a variant from campaign facts. Variants alter state selection, text direction, AI, and consequences. They do not create separate parallel mechanics.

### Occupation deportation network

Conditions:

- responsible country controls substantial non-core territory
- active resistance or occupation pressure
- rail or convoy routes connect occupied states to camp states

Characteristics:

- detainees are drawn mainly from occupied civilians and resistance-linked populations
- garrison and transport costs are high
- escape and foreign-intelligence incidents are common
- liberation discovery is likely
- annexation or peace can leave displaced-person and missing-family chains

### Civil-war detention network

Conditions:

- active civil war or recent Event 21 fracture
- rival government controls part of the original country
- security forces are detaining suspected supporters of the other side

Characteristics:

- responsibility is split by operator and network generation
- detainees can include political rivals, families, deserters, and regional communities
- prisoner exchanges, amnesties, reprisals, and mass escape incidents appear
- victory does not erase the losing or winning side's evidence
- continued killing can prolong insurgency after the civil war

### Extractive frontier network

Conditions:

- camp states contain mines, forests, quarries, plantations, or major resource deposits
- infrastructure is weak or terrain is harsh

Characteristics:

- extraction assignment is strong at first
- mortality, accident, disease, and infrastructure damage rise quickly
- private concession holders or local administrators can steal output
- depleted labour and damaged infrastructure can leave the resource state worse than before

### Island or colonial transport network

Conditions:

- overseas or island states
- maritime connection to the responsible country
- convoy capacity and port access

Characteristics:

- convoys and port labour are central costs
- blockade can create famine and epidemic crises
- escape by sea, transport loss, and foreign observation are more likely
- a destroyed convoy can create a mass-death and evidence incident

### Famine detention network

Conditions:

- state famine, blockade, crop failure, severe supply loss, or future famine-system marker
- camp population depends on restricted rations

Characteristics:

- camp mortality rises faster than surrounding mortality
- officials can divert food to prisoners, guards, army, or civilians
- relief decisions compete with national famine policy
- deliberate starvation can establish extermination intent when the target-purpose rules support it
- famine deaths must not be double-counted between systems

### Disease and quarantine-abuse network

Conditions:

- plague, bioweapon contamination, or severe epidemic
- government uses emergency detention beyond lawful public-health containment

Characteristics:

- medical isolation can become arbitrary detention, forced labour, abandonment, or killing
- genuine treatment and release can move the network toward review or closure
- biological experiments connect to Event 16 or country-specific packages
- disease spread and camp deaths use distinct Deaths reasons
- lawful, humane, time-limited quarantine is not classified as an Event 22 camp

### Corporate or concession network

Conditions:

- state has a major industrial or extraction assignment
- private concession, collaboration government, colonial company, or corrupt administrator marker exists

Characteristics:

- part of the output is lost to corruption
- the state can continue operation despite a central closure order
- documentary evidence includes contracts, shipments, and payroll records
- postwar liability can reach collaborators and firms, not only the former government

### Regime-inheritance network

Conditions:

- government, ideology, puppet status, or tag changes while sites remain

Characteristics:

- the successor chooses continuation, suspension, transparent closure, concealment, or reuse
- a successor that closes and exposes the network gains a different liability path from one that continues it
- puppet masters can pressure a subject to continue or close
- the original evidence remains attributed to the original operator

### Underground network

Conditions:

- official government orders closure but local security, military, party, or occupation administrators resist
- low authority or active internal faction struggle

Characteristics:

- some sites continue covertly
- national Network Reach can fall while hidden local evidence and deaths continue
- discovery creates both atrocity and disobedience crises
- the government can prosecute the operators, absorb them, or restore official control

## Country-specific adapters

### Germany

Event 22 should call the established German camp package. It can activate quiet camp infrastructure, occupied-territory deportation routes, extermination conversion, evidence destruction, Mengele-linked experiment sites, restricted chemical integration, and retreat crises.

Historical text and target registries require sourced research. The generic system must not overwrite those registries with invented demographic logic.

### Japan

Event 22 should call the established Japanese forced-labour, anti-partisan, occupation, experiment, and biological-warfare package. Maritime transport, occupied non-core populations, prisoner experimentation, and evidence destruction are central variants.

The lawful POW exclusion still applies. Abuse, forced labour, experiments, severe deprivation, reprisals, and mass killing bring a site into Event 22.

### Soviet Union

Event 22 should call the established gulag, deportation, famine, forced-labour quota, administrator-purge, evidence-destruction, and Soviet Collapse package.

Gulag sites count toward Network Reach only when the adapter marks them as active Event 22 sites. Evolution I must not automatically rename half of all gulags as extermination camps. The Soviet adapter must identify which sites are converted, which remain forced-labour camps, and which become lethal through famine, purge, or direct killing policies.

### Other countries

Other countries use the generic policy and target-purpose system unless a researched country adapter exists. Ideology alone is not enough to invent a historical persecution package. Country-specific text can draw on real institutions, colonial systems, security laws, civil wars, occupation practices, or alternate-history route decisions after those connections are researched.

## Rare incidents unlocked by evolutions

Possible incidents include:

- administrators refuse a conversion order
- guards desert with records or witnesses
- a railway worker network diverts a transport
- a factory manager reports labour deaths
- a local commander demands closure before retreat
- hardliners attempt a coup after the government stops extermination
- a resistance group frees one site and cannot feed the survivors
- an epidemic spreads from an overcrowded camp into a nearby city
- chemical stockpile leakage poisons guards and nearby civilians
- a natural disaster uncovers graves or records
- a bombing raid destroys transport and leaves detainees trapped
- a collaborator offers records in exchange for immunity
- a successor government discovers a network operated by its predecessor
- domestic purges reach senior officers, scientists, administrators, or party officials
- foreign radio broadcasts publish names and transport routes
- a site command steals confiscated property and becomes semi-independent

Each incident needs a clear campaign trigger, state or actor, immediate choice, follow-up consequence, AI response, and cleanup condition. They are not filler popups.

## Evolution completion and containment

An evolution remains part of global Event 22 history after it activates. A country can still contain its own network.

Containment requires:

- no active intake
- no active extermination or restricted chemical operation
- all sites closed, liberated, or under a verified relief process
- ongoing death pulses stopped
- survivors registered and supplied
- evidence transferred, preserved, or publicly accounted for
- no covert local site still operating

A country that meets these conditions exits the active evolution mechanics and receives refire protection. The evolution itself remains available for future countries.

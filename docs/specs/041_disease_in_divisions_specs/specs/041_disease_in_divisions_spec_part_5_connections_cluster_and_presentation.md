# Event 41 connections, cluster role, and presentation specification

## Cross-system ownership rule

Disease in Divisions owns the military epidemic. It owns military targeting, affected formations, Army Infection Pressure, military responses, military recovery, military deaths, cross-front military transmission, and the proof used to request civilian spillover.

It does not take ownership of civilian outbreak progression, famine, migration cohorts, Air Cleanliness, condemnation, chemical contamination, biological weapon use, disaster damage, or the shared Deaths ledger.

Every connection should use a bounded request, receipt, marker, or published fact. Event 41 should not read another system's private arrays or rewrite another system's lifecycle.

## Shared Deaths integration

Fatal military cases enter the shared Deaths system as military casualties.

The integration must ensure:

- only fatal cases are registered
- active sick and convalescent soldiers are not counted as deaths
- one fatality is registered once
- country and global military totals receive the same transaction
- the episode keeps its own cumulative military-death record for outcome and achievement checks
- generic Chaos from deaths remains owned by the shared Deaths system

Civilian deaths created after a War Plague handoff are registered by the civilian outbreak owner. Event 41 must not register them again.

## Biological warfare and outbreak integration

### Biological attacks against an infected military sector

A biological strike or compatible biological exposure should increase military risk through a bounded input. The effect can include:

- stronger pressure rise
- higher exposure in the struck node
- reduced sanitation effectiveness
- a greater fatal share
- stronger civilian spillover risk under Evolution II

The biological warfare system retains ownership of weapon effects, agent identity, contamination, condemnation, and civilian outbreak creation.

### Existing biological outbreak in the same state

When military formations operate in a state with an active compatible civilian outbreak, the military node gains exposure risk. Event 41 should read a public state-level risk fact or adapter result. It should not copy the civilian disease into a new military ledger without a valid exposure transaction.

### Military source entering civilians

War Plague uses the civilian adapter defined in Part 4. The civilian owner returns a receipt that confirms rejection, new outbreak, or strengthening of an existing outbreak.

## Air Cleanliness integration

Low Air Cleanliness can increase military vulnerability where the current biological and environmental systems define a relevant effect. Event 41 should use the published global or state risk status, not create a separate pollution calculation.

When civilian spillover creates a biological outbreak footprint, that outbreak can contribute to Air Cleanliness through its own owner. Event 41 does not add direct air contamination for military sickness alone.

This distinction keeps a contained camp epidemic from polluting the global atmosphere without a civilian or environmental pathway.

## Chemical contamination integration

Chemical contamination can worsen respiratory and medical conditions in an infected node. It can:

- raise operational strain
- increase mortality
- reduce recovery
- overload field hospitals
- increase civilian spillover risk under War Plague

The chemical system keeps ownership of contamination, weapon-use consequences, Air Cleanliness, and Condemnation.

## Famine integration

Famine pressure can raise military disease risk by weakening supply, sanitation, local health, and hospital access.

Event 41 can publish or consume these limited facts:

- the affected military node is inside a famine-pressured state
- relief access is low
- food and water security are poor
- local medical demand is high

Military decisions can temporarily compete with relief transport or civilian medical capacity. This competition should be expressed through the owning adapters or shared capacity facts. Event 41 should not debit famine reserves or alter famine stages directly without an approved public API.

## Migration integration

Migration and displacement can affect military disease through crowded routes, reception pressure, camps, and transport hubs.

Event 41 can publish:

- a corridor has military infection risk
- a state needs controlled medical reception
- a port or rail hub is restricted by military quarantine

Migration retains ownership of cohorts, transfers, border policy, reception, settlement, and displacement deaths.

A closed border or military district does not erase civilians. It can create trapped-population pressure inside Migration when the validated adapter supports that result.

## Natural-disaster and bombardment integration

A disaster or bombardment can create the conditions that make a military epidemic harder to contain:

- damaged infrastructure and railways
- destroyed hospitals
- unsafe water
- mass displacement
- lost supply hubs
- blocked ports
- overcrowded rear areas

Event 41 should read the resulting world state. It should not call a second disaster merely to justify stronger disease.

When a disaster occurs during an active episode, one milestone report can explain the changed military situation. Routine building damage remains in the disaster owner.

## Field hospitals, logistics, and technology

Existing HOI4 and Chaos Redux military systems should directly shape Event 41.

Relevant protection includes:

- field-hospital support companies
- field-hospital technology
- logistics support
- supply status
- infrastructure and rail quality
- trains, motorized equipment, fuel, ports, and convoys
- military medical or support technologies already present in the mod

The event should recognize these systems without creating duplicate technologies. A new dedicated technology branch is unnecessary.

## Diseases cluster role

Disease in Divisions belongs to Cluster 8, Diseases, as a Low member.

Its cluster identity is distinct from the larger outbreak events:

- Event 41 begins inside one wartime military system
- its baseline has no automatic civilian spread
- its baseline uses one country and a bounded frontline sector
- wider military and civilian spread requires evolutions

### Cluster participation

When Event 41 is the selected event that causes a Diseases cluster roll, it should remain the required member for its own incident. Other disease members can participate according to their cluster rules and valid targets.

When another Diseases member causes the cluster roll, Event 41 can participate as an optional Low member if a valid ordinary country at war exists.

If no valid wartime military target exists, Event 41 should be skipped with a clear cluster reason. The cluster should not invent a war or target an invalid country.

### Cluster interaction limits

Cluster firing should not automatically grant Evolution I or Evolution II. It should not create civilian spillover from Event 41 at Calm World.

If another cluster member already creates an outbreak in the selected military state, Event 41 can receive higher opening exposure through the shared integration route. It must still create one military episode and avoid duplicate civilian disease.

### Cluster pacing

The cluster counts as one global pacing event. Event 41 still applies its own repeatable weight and firing history. Its member effects must not advance the global event timer a second time.

## Event report family

The following report roles define the player-facing chain. Their labels are working roles, not final localisation.

### Opening report

The target country's military command receives the first account of formations losing personnel to sickness. The report should identify the affected sector and the visible military problem. It should not identify a precise pathogen.

### Spread report

This report appears when the disease leaves the opening formation group or creates another military node. It should show the practical route of spread through camps, supply, hospitals, or movement.

### Medical overload report

This report appears when field hospitals and evacuation can no longer handle the active burden. It should direct the player toward a meaningful response without listing hidden formulas.

### Front at risk report

This report appears when the selected front approaches the intended half-strength danger band. It should describe missing companies, empty positions, delayed replacements, and commanders losing operational options.

### Reversal report

This report appears when a severe episode begins a sustained fall. It should show that rotation, hospitals, sanitation, or evacuation are working.

### Resolution report

This report closes active transmission and explains the remaining convalescent burden and aftermath.

### Foreign military transmission report

Under Evolution I, the source and receiving countries receive appropriate reports after the first proven cross-border military case. The receiving country should learn the likely military route and gain its own category.

### Civilian spillover report

Under Evolution II, the military source country receives a report when a civilian handoff is accepted. The affected civilian country or state follows the owning outbreak system's presentation.

### International War Plague report

This report appears when the episode reaches a meaningful international milestone. It should communicate the military and transport network clearly and keep the focus on the linked operational crisis.

## Event option direction

The opening option should acknowledge that the army must choose a response. Its tone should be serious and operational.

Response reports can use military understatement, strained confidence, or direct medical advice. Cheap jokes would weaken the event because it concerns large-scale illness and death.

The fight-through posture can use a hard, self-damning command tone. The wording should make clear that the government accepts the medical cost. It should not celebrate sickness or hide the visible risk.

Resolution options should differ by outcome. Clean containment can sound disciplined and relieved. Medical exhaustion should sound depleted and practical. A shattered front should focus on the soldiers and the rebuilding task.

Final wording belongs to implementation. The spec provides direction and dynamic subjects only.

## Event Details direction

Event Details should explain the premise:

- a wartime country can suffer disease among frontline formations
- the outbreak spreads through military conditions
- the country can contain it by sacrificing tempo and resources
- higher evolutions permit military and civilian spread

It should not list raw modifiers, exact hidden profile rules, future surprise reports, or achievement conditions.

The details view should show:

- Event ID and type
- Chaos level 1
- Diseases cluster membership
- Low member severity
- current enabled state
- repeatable firing history
- Evolution I and Evolution II preview directions

## Event Logs integration

The root firing should create one normal event-history entry with the selected country as actor.

Secondary national outbreaks created by Evolution I should create linked Event 41 history entries only when they become full national incidents. A mere exposure test should not create history spam.

Evolution entries should record only:

- Camp Fever Across the Trenches
- War Plague

Pressure stages, spread reports, and resolution reports remain part of the event history or internal episode record. They do not become evolution rows.

The event detail and history surfaces should be able to show the original actor, current episode status where supported, and cumulative firing count without exposing private ledgers.

## Map presentation

The temporary category should provide a map mode or map highlight that helps the player find the military disease.

Useful node states are:

- exposed
- active
- severe
- recovering

The map should distinguish state without relying on color alone. It can use border treatment, icons, hatch, or status tooltips.

The map highlight should remain bounded to event nodes. It should not paint every state in the target country because one sector is infected.

## Formation presentation

Affected formations should have a visible status icon or modifier tooltip.

The tooltip should state:

- the formation is affected by military disease
- the main combat and recovery penalties
- whether it is active or recovering
- the broad action that helps it

It should not show raw hidden transmission scores.

## Decision category picture direction

The category picture should depict a World War II field medical environment tied to one active front. Suitable subjects include a crowded field hospital, an ambulance column beside a damaged rail line, sick soldiers in a temporary treatment camp, or medical staff separating a military camp.

The image should show soldiers, medical staff, transport, tents, stretchers, and period equipment. It should avoid gore, modern protective equipment, modern ambulances, readable generated text, and a generic map-table scene.

The picture is presentation only. It must not paint fake buttons, meters, or values.

## Core icon families

The event needs distinct art for:

- report event image
- decision category icon
- decision category picture
- Army Infection Pressure status or texticon
- affected-formation modifier
- recovering-formation modifier
- field epidemic preparedness aftermath
- medical exhaustion aftermath
- rotation decision
- quarantine decision
- field-hospital expansion decision
- sanitation decision
- medical evacuation decision
- corridor repair decision
- offensive posture control
- military district isolation decision
- port closure or controlled demobilization under War Plague
- achievements

Each icon family should use its correct HOI4 reference surface. A focus icon should not be resized into a decision or idea icon. Event 41 does not need a focus icon family.

## Multiplayer behavior

The event belongs to the shared global event system and selects one valid country per firing.

A player country that becomes a secondary national outbreak under Evolution I receives its own category and reports.

All relevant players should be able to see international milestones when their countries are involved. Uninvolved players should receive only major public reports that affect their military access, faction, or civilian outbreak risk.

The episode generation and target proofs must prevent duplicate categories when several players share one front.

## Accessibility and clarity

The system should use:

- one visible meter
- short cause tooltips
- named sector targets
- clear blocked reasons
- distinct state and formation icons
- trend arrows or labels that do not rely only on color
- compact costs with matching texticons

The category should avoid:

- raw variable names
- long component ledgers
- several overlapping medical currencies
- hidden extra costs
- a wall of target decisions
- repeated popups for ordinary weekly changes

## Documentation alignment

The permanent event documentation should describe:

- target eligibility
- Army Infection Pressure
- military manpower and recovery logic
- decision families
- baseline resolution
- evolution entry paths
- military and civilian integration boundaries
- cluster role
- Chaos impact map
- assets and their runtime consumers
- AI and probability evidence

The event catalog workbook should use the same player-facing premise and evolution directions as Event Details. The exported CSVs should be regenerated from the workbook after implementation.

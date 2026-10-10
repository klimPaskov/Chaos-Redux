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

Every camp death removes real state civilian population, and every Event 22 request goes through `camp_admin_record_deaths`, the shared camp owner's only physical debit.
That helper calls `apply_exact_state_civilian_population_loss` (or its current public replacement) once, measures the accepted result, consumes the same number of people from the aligned living custody rows, and projects one receipt to the Deaths ledger with its physical-debit flag disabled so nobody is removed twice.

The caller supplies:

- the requested people (`camp_admin_death_requested_k`, in thousands)
- the shared cause (`camp_admin_death_cause`: custody, labor, violence or institutional)
- the one-shot contract proof (`camp_admin_death_contract = 1`)
- an optional single custody row

The registered state supplies the protected minimum, the responsible country and the valid-target proof.
The implementation must use the actual applied amount (`camp_admin_death_actual_k`) and never register the requested amount when the protected floor, the cohort or rounding reduced the loss.

The helper already reconciles recruitable-manpower credit. Event 22 must not add a second manual manpower debit after a successful call.

### Deaths reasons

Event 22 reuses the four shared camp causes for all recurring harm.
It registers a distinct Deaths reason only where those causes do not already describe the loss:

- evolution shocks (one reason per evolution)
- forced evacuation or death march
- restricted chemical-site operation (owned by the existing restricted-site effects)
- evidence destruction and liquidation during retreat
- abandonment before relief and post-liberation relief failure

Camp disease, famine, bombing and nuclear losses keep their owners' reasons so no person is counted twice.
The player-facing Deaths category groups these under the existing camp or state-atrocity heading while retaining cause-specific detail in tooltips and records.

### Detained population

The detained population is the shared custody ledger (`camp_admin_detainees_k` and the aligned rows), not an Event 22 capacity.
A cohort is created only by `camp_admin_admit_detainees`, which needs a proven source of people already present in the state, is clamped by free capacity, the civilian floor and the shared population-share ceiling, and returns the accepted amount.
There is no automatic intake from a pressure score or from the entire state population.

Deaths reduce both the cohort and real state population. Release, escape, transfer and liberation reduce the cohort without a death (`camp_admin_release_detainees`, `camp_admin_close_site`).
New intake or transfer raises a cohort only through a visible policy, incident or valid country adapter that supplies the source proof.
The cohort is not an ethnicity census and must not be displayed as one.

### Mortality

Recurring mortality is owned by the shared monthly processor and its constants (`camp_admin_value`: `custody_monthly_rate`, `labor_monthly_rate`, `violence_monthly_rate`, `shortage_mortality_factor`; institutional rates in `camp_admin_institution_mortality`; legacy `genocide_death_percent`).
Event 22 contributes only:

- the policy that sets the mandate and roles (review lowers harm, forced labour adds the labour cause, extermination adds the violence cause under the radical mandate)
- the evolution shocks and the retreat spikes above
- relief actions that raise the shared support ratio

The original design tabled its own monthly rates (about 1 to 2 percent of a private capacity for ordinary operation, 10 to 35 percent for extermination).
Those tables are removed: they used a different base and different magnitudes from the shared constants (for example `violence_monthly_rate = 0.02` of the living cohort), and a second rate table would double the processor.
Balance targets stay in the time-to-consequence section; the numbers live in the shared constants and are tested across small, medium and large states.

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
- Event 22 and the shared camp owner own extra camp-specific mortality caused by restricted rations, confinement, and policy
- the two systems must share a causal context so one person is not counted twice in the same month
- relief supplies can reduce both famine pressure and camp mortality when delivered to the state
- guards, army, civilians, and detainees can become competing ration priorities
- deliberate starvation against a qualifying protected group can contribute to destructive-intent classification
- famine can create escape, revolt, epidemic, corruption, and discovery incidents

The famine system is implemented.
Its `famine_adapt_camp_state` already turns a site's monthly camp deaths into famine pressure for the state, and `famine_food_stage_requires_mortality` and `famine_food_stage` expose the state's food stage.
Event 22 reads that stage as an input of the epidemic and famine incident and of the camp-epidemic mission, and writes no famine value.
The reverse direction (a worse food stage raising the shared camp support shortfall) is a proposal for the camp owner; until it lands, Event 22 adds only incident and mission weight and never a second mortality request for the same people.

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

The [independent migration mechanic](../famine_and_migration_system_specs/README.md) owns displacement, reception, return, and exact population movement; Event 149's retired event identity is not a provider.
Use its [living-cohort and reception contract](../famine_and_migration_system_specs/famine_and_migration_system_spec_part_3_displacement_migration_return.md#population-movement-principle) and the camp owner's proved custody provenance for survivor movement.
A request or location marker does not prove that anybody moved.
Until the exact source cohort, real destination capacity, passage, and inverse/commit contract are verified, retain survivors in their current accommodation and report the transfer as unresolved rather than inventing population credit or transport deaths.
The existing secure-site and food/medical-relief actions remain available; their ordinary safety and affordability gates still apply.

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

Every active site already pays the shared monthly maintenance (support equipment per thousand detainees, `maintenance_support_per_k`, scaled by the budget tier) and loses output when the support ratio falls.
Event 22 adds no second guard payment.
The burden rises through the support shortfall, Resistance Pressure and front proximity, and can pull units or equipment away from the front through the escape and front-approach missions.
It must not be represented only by a small political-power cost.

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

The air contamination ledger tracks six global footprints and has no camp footprint or state-level cleanliness value, so Event 22 adds no air source and no state air value (proposal P-022-F).
The camp epidemic incident may read the existing global air contamination level as one weight, and a chemical accident uses the existing contamination system.
Air cleanliness is never a cosmetic modifier.

### Black Plague and Event 20

The connection requires a registered site or recorded survivor accommodation in a state with proven active Black Plague or an eligible Event 20 exposure route.
Overcrowding and neglect amplify that existing hazard; a camp building alone neither proves infection nor starts Event 20.
Rat Nation and Rat King actors remain outside the ordinary human camp loop.

The affected operator or liberator uses the existing food/medical-relief and quarantine/decontamination actions, together with Event 20's hospital, sanitation, and relief-corridor response.
Care in place reduces neglect and supports disease containment while committing local supply and medical capacity.
Medically supported transfer can relieve overcrowding, but requires a proved living cohort, receiver approval, actual capacity, and a safe route under the migration and disease owners' current rules.
If those gates fail before departure, the request moves nobody and produces no successful movement receipt; payment reservations and spent preparation costs retain the migration owner's existing rejection and cancellation rules.
Local care remains a meaningful response.
A noncontinuing capture or transparent camp closure stops coercive operation but leaves the state's infection, containment requirements, and residual medical needs intact.
An Event 20 cure removes active plague only through its own state machine and does not itself dismantle the site, preserve records, or complete survivor relief.

Event 20 owns strain, epidemic mortality, and spread.
The shared camp mortality owner owns any separate confinement, violence, deprivation, or relief-failure loss from still-proved living custody.
Before such a loss, it reconciles accepted outside population/death observations under the [current finite-custody contract](../../systems/camp_institutional_mortality.md#existing-systems-and-remaining-attribution-work).
A whole-state plague death total cannot identify which camp origins died.
An unlabelled outside loss with mixed living origins retains the accepted PAUSE until source-labelled provenance is restored; it cannot be resolved by proportional or newest-first assignment.

Criminal responsibility and the medical cause of death remain separate.
Original operator and neglect evidence survive relief or transfer, but the same victim is not re-registered as an Event 22 death or a second shared Chaos source.
An actual jointly delivered medical service can support both owners through its one paid receipt; opening two projects does not automatically pay or complete either twice.
Relief AI prioritizes supported care in place when routes or receivers are unsafe, and considers transfer only when the same exact-cohort and medical gates available to the player pass.
With Event 20 absent, disabled, or merely initialized without an outbreak, ordinary camp disease and relief retain their existing behavior.

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

The Soviet adapter should bridge to Event 5 and extends the existing `camp_rework_soviet_apply_union_crisis_repression_bridge`:

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

### Timing

- recurring harm and output: the shared 28-day country timer and one calendar-month guard (`camp_admin_dispatch.period_days`); Event 22 adds no pulse
- exposure and resistance incident check: event-driven plus the same monthly visit
- same-country event refire protection: several months to more than one year depending on resolution
- transparent closure protection: longer than concealment or dormant-network protection

### Output limits

Forced-work output uses the shared priority, spending ceiling and caps (40 percent industrial contribution, 25 percent national factory modifier, 40 percent construction and extraction), scaled down by the shared support ratio.
Event 22 sets no assignment bonus and no national cap of its own.

### Dismantlement burden

Closure duration and cost scale with:

- site count
- living custody at the sites
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

Only the values Event 22 owns are listed here. Keep them in centralized constants; the probability and live-balance passes can change them after evidence.
Recurring rates, caps, maintenance and workforce multipliers belong to the shared camp constants (`camp_administration_constants.txt`).

### Initial cohort

The opening seeds each site's cohort through `camp_admin_admit_detainees` from a proven source. Starting direction:

| Site opening | Starting cohort direction |
| --- | --- |
| baseline concentration site | `0.5%` of current state population, minimum `2,000`, maximum `100,000` |
| security-expansion site | `0.75%` of current state population |
| Evolution I conversion | keeps the existing cohort, no automatic refill |
| Evolution III new concentration site | `1.0%` of current state population, maximum `250,000` |
| Evolution III new extermination site | `1.5%` of current state population, maximum `300,000` |

No site can admit more people than the campaign source supplies, and a minimum is ignored when the source, the state population, the shared population-share ceiling or the protected floor cannot support it.

Consistency check (proposal P-022-C): these cohorts are smaller than the 1 percent and 2 percent evolution shocks, and the shared death helper cannot remove more people than the cohort holds.
Evolution entry therefore first admits an additional source-proved sweep cohort equal to the shock request, within the shared ceiling, and then applies the shock; if the source cannot supply it, the shock is clamped to the living cohort and the clamped amount is what is recorded.
The parent chooses between that sweep and plain clamping.

### Exceptional one-time losses

| Incident | Loss direction from the affected cohort |
| --- | --- |
| fully supplied transfer | `0%` to `3%` |
| disrupted transfer | `3%` to `15%` |
| forced march | `10%` to `30%` |
| retreat liquidation | `50%` to `100%`, limited by the exact living cohort and the state floor |
| abandoned site before relief | `2%` to `10%` |

Evolution II and Evolution III shocks are separate requests of 1 and 2 percent of current state population and do not use these rates.

### Visible value thresholds

Recommended `0` to `100` bands:

| Value | 0 to 19 | 20 to 39 | 40 to 59 | 60 to 79 | 80 to 100 |
| --- | --- | --- | --- | --- | --- |
| Exposure | controlled secrecy | persistent rumours | credible leaks | verified-site risk | publicly documented network |
| Resistance Pressure | disorganized opposition | escape networks | coordinated sabotage | armed resistance | administrative breakdown |

Fallback Network Reach bands, used only if the parent keeps Reach as a third meter (proposal P-022-A):

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

- the custody cohort is finite and created only by `camp_admin_admit_detainees` with a proven source
- deaths, release, escape, and liberation reduce it
- intake requires a valid target source and visible action
- broad domestic purge has severe national costs
- site conversion does not refill the cohort

### No free state bonuses

- output requires a labour-role site with a living, supported cohort (the shared rule)
- the shared caps bound every contribution
- output decays when support fails
- one site has one role at a time
- extermination sites cannot keep forced-labour output

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

Register only through the shared registries (`global.camp_repression_active_countries` and the registered active-site states, via `camp_rework_register_country_for_monthly_pulse` and `camp_rework_register_active_site`) and event-owned flags or arrays for:

- active Event 22 countries
- liberated or closing states that still need work
- responsibility actors
- discovery and relief jobs

Do not scan every country or every state on daily or weekly on-actions, and do not add a new periodic hook.

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
- Exposure band
- Resistance Pressure band
- Network Reach as one line (sites of eligible states)
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
- site role or closure status
- cost summary
- main consequence
- blocked reason when invalid

Use existing state modifiers, building icons, target highlights, and the decision map as the complete map interaction layer.

### Category clutter

A phase normally shows three to five primary actions and one to three missions. Use replacement rules:

- opening options disappear after policy choice
- targeted decisions are hidden until a state is eligible
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

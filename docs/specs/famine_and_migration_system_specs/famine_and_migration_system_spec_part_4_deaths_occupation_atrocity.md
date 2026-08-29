# Famine and Migration Mechanics

## Part 4: Deaths, occupation, forced labor, deportation, and atrocity

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any wording in this historical specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Deaths-system purpose

The shared Deaths system remains the only public ledger for civilian and military deaths. Famine and migration add new source adapters and new reasons. They do not create a second casualty total.

The player should be able to distinguish deaths caused by hunger, occupation repression, forced labor, deportation and forced movement, bombing, nuclear effects, outbreaks, camps, genocide, chemical exposure, and military combat.

## New civilian death reasons

### From famine

Use this reason when hunger, malnutrition, dehydration caused by food-system collapse, or hunger-related physical decline is the proximate cause.

Examples:

- recurring mortality in a famine state
- starvation during a siege
- starvation caused by blocked relief
- malnutrition deaths in a camp or gulag
- starvation after crop destruction or nuclear winter
- starvation among a trapped border population

### From occupation repression

Use this reason for fatal occupation policy that is not already owned by camps, genocide, famine, chemical or biological attack, bombing, or combat.

Examples:

- punitive raids
- collective reprisals
- fatal curfew enforcement
- hostage killing
- lethal security sweeps
- deliberate denial of basic civilian protection where the direct mechanism is repression

### From forced labor

Use this reason when exhaustion, dangerous labor conditions, workplace violence, or labor-site deprivation is the proximate cause.

Examples:

- fatal gulag labor
- mine or factory death under forced labor
- labor battalion mortality
- coerced construction under extreme conditions
- prisoner labor mortality that is distinct from execution or famine

### From forced displacement

Use this reason for deaths caused by coercive movement or a dangerous route when no more direct death reason owns the physical cause.

Examples:

- forced march deaths
- overcrowded deportation transport
- lethal exposure during expulsion
- deaths during violent border pushback
- dangerous forced return
- people abandoned along a deportation route
- route deaths during an organized evacuation when coercion or route exposure is the direct cause

### From border closure

This reason should be used sparingly and only if the project benefits from a separate public breakdown.

The preferred design is to keep the proximate physical cause visible:

- famine for starvation at a closed border
- outbreak for disease
- forced displacement for violent pushback or exposure during forced return
- bombing for an attack on the trapped population
- occupation repression for deliberate lethal enforcement

A distinct `From border closure` reason is useful only when the system can prove that denial of entry itself caused the fatal outcome and no clearer physical source applies. The implementation agent should decide after inspecting the current Deaths reason capacity and UI clarity.

## Ownership rule

One physical death has one ledger owner.

The owner is selected from the closest proven cause of death, not from every system that contributed to the crisis.

Examples:

- A civilian dies in the initial nuclear blast. The nuclear reason owns the death.
- A survivor later dies from fallout exposure. Fallout owns the death.
- Another survivor later dies because the strike destroyed all food access. Famine owns the death.
- A camp prisoner is executed. Camp or atrocity processing owns the death.
- A camp prisoner dies from withheld food. Famine owns the death.
- A camp prisoner dies from forced mine labor. Forced labor owns the death.
- A deportee dies during an overcrowded train journey. Forced displacement owns the death.
- A deportee arrives in a famine state and later starves. Famine owns the later death.
- A refugee with a proven outbreak infection dies from the disease in a reception camp. The outbreak reason owns the death.
- A refugee is killed by border guards. Occupation repression or forced displacement owns the death, according to the responsible system and action.

The implementation should use a reason-priority helper only when a single transaction could receive several candidate causes. It should not use priority to reclassify already recorded deaths.

## Exact transaction contract

Every death adapter must eventually produce an exact number of people actually removed from a state.

The shared population-loss contract should:

- receive a positive requested loss
- receive a protected population floor
- receive one Deaths reason
- receive one target country for the ledger
- apply state population loss once
- return the actual applied amount
- reconcile recruitable-manpower side effects
- clear one-shot inputs

Famine mortality can call the documented exact state civilian loss effect directly.

Occupation, forced labor, deportation, and border actions should use the same exact effect with their own reason.

Migration transfers should not call a logged death effect for the origin debit. They should use an unlogged exact population transfer debit and then register only route deaths separately.

## Occupation-law integration

Occupation policy is a major source of civilian pressure and should connect to Deaths, famine, displacement, resistance, evidence, and condemnation.

### Law profile mapping

The implementation agent should inspect all current vanilla and Chaos Redux occupation laws and map each relevant law to a shared profile.

Possible profiles:

- protective administration
- limited requisition
- standard occupation
- harsh extraction
- forced labor administration
- collective punishment
- population transfer
- exterminatory policy
- CBRN coercive administration

A profile can modify:

- food extraction pressure
- forced-labor pressure
- displacement pressure
- route restrictions
- resistance and opposition
- hidden atrocity evidence
- public visibility
- relief access
- inspection access

The same profile should be reusable by event-owned occupation systems without duplicating logic.

### State and controller responsibility

The responsible country is normally the current controller that applies or benefits from the policy. The state owner remains the affected country for population and local political effects when appropriate.

The implementation must resolve controller, owner, occupier, and puppet responsibility according to the existing condemnation and camp contracts.

### Timing

Occupation pressure should update on scoped hooks:

- occupation-law change
- control change
- state entry into an occupation profile
- camp or forced-labor site activation
- requisition decision
- deportation action
- relief denial
- peace or liberation

The design should not require a global occupation scan.

## Protective administration

A protective profile can reduce famine and displacement pressure through:

- lower requisition
- maintained local administration
- civilian ration protection
- relief access
- inspection access
- local police restraint
- transport repair

The profile should still have occupation costs and resistance risk. It is not a free stability bonus.

## Harsh extraction

A harsh extraction profile can provide short-term resources, labor, or military supply while creating:

- food pressure
- forced-labor deaths
- local production decline
- displacement
- resistance
- hidden atrocity evidence
- later condemnation
- stronger post-liberation opposition

The military or economic benefit should be visible enough to create a real tradeoff.

## Collective punishment and deliberate starvation

Deliberate starvation can occur through:

- removal of food reserves
- blocking relief
- closing escape routes
- burning crops or storage
- ration exclusion
- sealing a city, ghetto, camp, or state
- punitive requisition after resistance activity

This is an atrocity path. It can create strong hidden evidence immediately and public condemnation after discovery or attribution.

The famine system owns the hunger deaths. The occupation and condemnation systems own responsibility, evidence, sanctions, diplomatic response, and tribunal pressure.

## Forced labor

Forced labor should be a living system input, not only a one-time death event.

A forced-labor program can:

- remove working-age civilians from origin states
- reduce agricultural and industrial labor at the origin
- create labor-site population at a destination
- produce military, construction, mining, or factory output
- create recurring forced-labor deaths
- create famine pressure when rations are inadequate
- create outbreak pressure through crowding and unsafe conditions
- create escape and migration incidents
- increase resistance and foreign pressure

The system should distinguish ordinary labor mobilization, punitive labor, prisoner labor, gulag labor, and exterminatory labor according to existing project definitions.

## Deportation and forced relocation

A deportation is a movement transaction with coercion, responsibility, and route risk.

The action should define:

- targeted origin state
- targeted cohort
- stated or hidden purpose
- destination state or camp site
- transport route
- escort and security
- food and medical provision
- property policy
- return eligibility
- concealment and evidence

Possible purposes include:

- ethnic or national removal
- political purge
- forced settlement
- labor transfer
- security-zone clearance
- occupation consolidation
- population exchange
- scorched-earth withdrawal
- camp transfer

A deportation can produce short-term control or labor. It creates serious long-term resistance, evidence, diplomatic, and return consequences.

## Camps and extermination sites

The existing camps and genocide mechanics remain the owner of site creation, site type, site operation, evidence, discovery, concealment, foreign response, and tribunals.

The separate famine and migration mechanics use narrow shared adapters for:

- food deprivation
- forced labor mortality
- transfer into or out of sites
- escape and flight
- local population removal
- nearby fear and exodus
- liberation and survivor return
- border response to escapees

### Nearby civilian fear

A discovered or feared camp can raise flight pressure in nearby states, especially for targeted cohorts.

This should use visibility. A hidden site does not automatically create public mass flight unless disappearances, escapees, raids, or local knowledge make the threat credible.

### Camp liberation

Liberation can create:

- immediate medical and food need
- survivor evacuation
- return requests
- evidence exposure
- host-country reception
- family reunification
- political testimony

Survivors should not be converted into normal destination population without a recovery stage.

## Gulag integration

The Soviet gulag and repression surfaces should connect through:

- labor removal from origin states
- camp destination population
- forced-labor mortality
- famine mortality from inadequate rations
- deportation-route mortality
- local fear and opposition
- hidden evidence and later disclosure
- Event 5 Soviet Collapse pressure

The 1932 to 1933 famine should normally appear in a 1936 campaign as historical memory and state vulnerability, not as an active automatic death script. New grain extraction, deportation, gulag expansion, movement restriction, or concealed crop failure can reactivate the profile dynamically.

## Genocide and targeted persecution

Targeted persecution changes movement and border behavior.

The targeted cohort receives:

- very high desire to leave
- lower trust in same-ideology assurances
- preference for destinations with protection or community ties
- increased risk of closed-border trapping
- higher danger from forced return
- stronger family-reunification pressure

Receiving countries can choose humanitarian entry, limited quotas, transit, internment, closure, or forced return. The consequences depend on known danger and actual policy.

## Border closure and responsibility

A closed border is not automatically an atrocity. Countries can close or control borders for war, capacity, security, or outbreak reasons.

Responsibility rises when:

- the threatened population faces a proven severe danger
- the closing country knows the danger
- safe controlled entry or transit was feasible
- the country uses violence
- the country forces return to camps, extermination, famine, or active combat
- the country blocks neutral relief or resettlement offers
- the country conceals the outcome

The system should use public and hidden evidence according to what observers can prove.

## Outbreak quarantine and coercion

Quarantine can protect public health when it includes food, water, shelter, medical care, and a time-limited containment plan.

Quarantine becomes abusive when people are sealed without aid, used for forced labor, selectively targeted, or forcibly returned to danger.

Deaths inside a quarantine use the physical cause:

- outbreak
- famine
- occupation repression
- forced displacement

## Bombing and occupation overlap

A state can suffer both enemy bombing and occupation repression.

The system should avoid assigning bombing deaths to the occupier unless the occupier's action directly caused them through human shields, blocked evacuation, or another proven policy.

Bombing can increase occupation resistance and movement. Occupation can block shelters, evacuation, or relief. Each system records its own physical losses and contributes to shared pressure.

## Nuclear evacuation and exclusion zones

A nuclear strike can create an exclusion zone or prolonged fallout state.

The responsible attacker owns nuclear and fallout condemnation. The controller of the affected state can still gain responsibility for:

- blocking evacuation
- forcing people into contaminated labor
- denying medical relief
- concealing fallout
- forcing premature return

Deaths are split by physical cause.

## Condemnation integration

The condemnation system should receive source records for:

- deliberate starvation
- blocked verified relief
- lethal forced labor
- deportation
- violent pushback
- forced return to known atrocity or famine zones
- camp deprivation
- concealment and destroyed records
- repeated public abuse

The source can remain hidden until discovery, inspection, occupation, escapee testimony, captured records, or foreign observation exposes it.

Public condemnation should scale with deaths, visibility, intent, repeat use, targeted cohorts, and obstruction of relief. It should not scale only with a binary flag.

## Resistance and ideology movements

Occupation, famine, and forced movement can create opposition through several channels:

- partisan support
- local resistance
- separatism
- anti-colonial movements
- worker or peasant organization
- military mutiny
- religious relief networks
- democratic opposition
- communist opposition
- nationalist opposition
- fascist or collaborationist movements

The selected channel should reflect actual local and national conditions.

A movement can gain strength from:

- visible responsibility
- unequal relief
- targeted deportation
- camp discovery
- closed-border deaths
- foreign sponsorship
- prior ideology support
- weak legitimacy
- successful local relief outside government control

The system should not generate a full civil war from one state pulse. Pressure should accumulate, produce incidents, and connect to existing civil-war, independence, resistance, and ideology systems.

## Liberation and aftermath

Liberation should not instantly remove every consequence.

A liberated state can face:

- famine relief
- survivor recovery
- camp closure
- return and property claims
- collaborator disputes
- labor shortage
- destroyed transport
- evidence collection
- revenge violence
- political competition over relief

A liberating country can gain trust through food, medical support, safe return, and protected administration. Requisition, forced return, or political exclusion can recreate opposition.

## Source adapters

The famine and migration mechanics should expose separate bounded adapters for other systems.

Conceptual adapters include:

- request state food-security pressure
- request state flight pressure
- request organized evacuation
- request deportation or forced relocation
- request reception and border response
- request return or resettlement
- register occupation-repression deaths
- register forced-labor deaths
- register forced-displacement deaths
- add hidden or public deliberate-starvation evidence

Each adapter should require an actor, target, cause, severity, and proof fields. Unknown or incomplete calls fail closed.

## Death-log presentation

The Deaths tab should support the new reasons in the same style as existing sources.

At minimum the player should see:

- total civilian deaths from famine
- recent famine entries with affected country and state context where supported
- occupation-repression deaths
- forced-labor deaths
- forced-displacement deaths

The tab should not become a dense accounting screen. It can group rare related reasons under an expandable occupation and displacement family while preserving the specific reason in the detail entry.

## Acceptance outcomes for death-source integration

The death-source design is complete only when:

- exact state population loss is used once per death transaction
- movement debits are unlogged and route deaths are separately logged
- `From famine` is visible in the Deaths breakdown
- occupation repression, forced labor, and forced displacement have clear source ownership
- camps, genocide, gulags, deportation, and occupation laws call shared adapters
- deliberate starvation and relief obstruction create condemnation evidence
- ideology and resistance consequences use real campaign context
- liberation creates recovery and return work
- no death can be recorded under two reasons
- the cause matrix is documented and tested through mixed-cause scenarios

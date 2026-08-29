# Famine and Migration Mechanics

## Part 8: Balance, validation, and acceptance

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any wording in this historical specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Balance objective

The system should make severe civilian crises matter without turning every war into an automatic population collapse.

The balance target has four parts:

- ordinary war creates local displacement and occasional supply strain
- prolonged isolation, heavy bombing, harsh occupation, major disaster, outbreak, nuclear damage, or deliberate policy can create famine and mass movement
- strong preparation and timely relief can prevent the worst outcomes
- catastrophic neglect or exploitation can kill a large share of an affected state's population and destabilize the country

## Meaningful death standard

Famine mortality must be large enough to affect:

- state population
- labor and production
- country manpower base
- political stability
- resistance and ideology movements
- the global Deaths total
- Chaos through the existing death threshold

The system fails if a catastrophic famine left unmanaged for months removes only an amount too small to notice in a dense state.

The system also fails if a brief supply interruption kills an implausibly large share before the player can respond.

The tuning should create a clear gap between:

- supply strain
- acute shortage
- managed famine
- unmanaged famine
- catastrophic famine with blocked relief

## Relative mortality targets

The package does not prescribe final numeric constants. It prescribes ordering and campaign behavior.

### Supply strain

Expected mortality:

None from the famine system.

Expected gameplay:

A warning stage with manageable economic and political pressure.

### Acute shortage

Expected mortality:

Low or intermittent. Persistent shortage can cause deaths, especially with outbreak, contamination, camp conditions, or harsh winter.

Expected gameplay:

The player should respond before the state reaches famine.

### Managed famine

Expected mortality:

Material but sharply reduced by active relief. The state can still lose a serious number of civilians while routes are restored.

Expected gameplay:

The player sacrifices transport, industry, military supply, or diplomacy to prevent catastrophic loss.

### Unmanaged famine

Expected mortality:

High and recurring. Several months should noticeably depopulate the state.

Expected gameplay:

Political opposition, flight, and production collapse become serious.

### Catastrophic famine

Expected mortality:

Very high. A dense state left isolated, repressed, contaminated, and without relief can lose a substantial share of its population over the crisis.

Expected gameplay:

The player faces national or international consequences. Recovery requires major action.

## No historical casualty target

Historical profiles should produce realistic orders of pressure when their causes are recreated. They should not continue killing until a stored historical total is reached.

The same profile can produce:

- low deaths if the campaign opens routes and relief early
- severe deaths if the campaign repeats extraction and restriction
- no crisis if the causes never exist
- a different regional pattern if front lines and control differ

This is required for replay value and historical honesty.

## Migration balance

### Flow scale

A movement incident should scale with:

- origin state population
- danger severity
- duration
- cohort ability to travel
- available transport
- route capacity
- destination capacity
- border policy

Small incidents should remain local. Nuclear strikes, front collapse, severe bombing, genocide, catastrophic famine, and mass deportation can create very large flows.

### Cohort pacing

Large flows should normally resolve in cohorts. This gives the player and AI time to:

- open or close routes
- add transport
- distribute arrivals
- negotiate a corridor
- improve reception
- reverse an unsafe destination

An immediate one-time flow is appropriate for a direct forced expulsion, sudden disaster evacuation, or terminal state conversion where delay would be false.

### Destination capacity

Reception capacity should meaningfully limit flow without acting as a hard arbitrary cap.

When capacity is exceeded:

- arrivals can still enter under open policy
- shelter, food, sanitation, and political pressure worsen
- route processing slows
- destination famine or outbreak risk can rise
- the host gains reasons to distribute, seek aid, integrate, resettle, or close entry

### Long-term benefit

Integration can produce a long-term population and labor benefit. It should require enough time and investment that a player cannot farm free population by repeatedly inducing migration.

## Exploit prevention

### Population duplication

A transfer must add no more population than the actual amount removed from the origin minus route deaths.

### Manpower farming

New arrivals should not instantly provide full recruitable manpower.

Recruitment can become available through:

- legal integration
- naturalization
- exile or volunteer formations
- route-specific mobilization

Each route needs time, political conditions, and equipment.

### Forced-migration farming

A player should not be able to move population repeatedly between two states to generate bonuses, remove penalties, or reset exposure age.

Use cohort identity, recent-movement memory, cooldowns, and origin history.

### Relief reward farming

Relief decisions should not produce more resources than they consume. Repeated relief should address real active pressure.

### Requisition loop

A player should not be able to solve every famine by draining a sequence of safe states without consequence.

Requisition transfers food pressure, creates grievance, and can eventually make donor states unsafe.

### Border toggle abuse

Rapidly switching border policy should not repeatedly trigger benefits or erase trapped populations.

Use policy cooldown, transition delay, or persistent route state.

### Integration cycling

A population integrated into the host should not remain eligible as a refugee cohort for resettlement rewards or return bonuses.

### Forced-return deletion

Forced return must have an actual origin or other destination. It cannot remove the host modifier without transferring the population.

### Empty-state exploitation

Evacuation cannot reduce a state below its protected floor unless an accepted terminal or wasteland system owns the result.

### AI route spam

AI should not launch repeated corridor, relief, evacuation, or resettlement actions against invalid or unchanged targets.

## Political balance

Famine and migration should create political pressure according to scale and responsibility.

### Low responsibility

A government that reports honestly, spends resources, opens routes, and shares relief can retain legitimacy even when deaths occur.

### Administrative failure

A government that delays or distributes unfairly receives stronger opposition.

### Deliberate harm

A government that extracts, traps, deports, starves, conceals, or forces return receives the strongest opposition, evidence, and condemnation.

### Host politics

Host-country pressure should depend on actual load, capacity, duration, and policy. Ideology changes the form of opposition and solidarity, not the existence of material costs.

## AI balance requirements

AI should preserve its country while still making ideologically coherent choices.

The AI must avoid these failures:

- sending civilians to unsafe states
- choosing a destination with no route
- accepting a flow into catastrophic famine without distribution
- closing a border when it has large spare capacity and strong humanitarian preference unless a valid security reason exists
- opening a border when no receiving state or route exists
- evacuating all workers from a critical defense state without a military reason
- spending all convoys on relief while national survival requires military supply
- maintaining lethal extraction after it causes strategic collapse without an ideological or exterminatory reason
- forcing return before the origin is safe unless the regime accepts the consequences

## Performance acceptance

The system must use bounded processing.

### Active food-security registry

Only states with an active pressure source, recovery process, or recent memory requiring settlement are processed.

### Active displacement registry

Only countries and states with active flows, trapped cohorts, reception, return, or integration are processed.

### Scheduled jobs

Mortality, route movement, relief delivery, and return can use delayed jobs or state flags with bounded scheduling.

### Cleanup

A state or country leaves the active registry when its issue is resolved and its memory record is settled.

### Forbidden performance shortcut

The implementation should not add a whole-world daily, weekly, or monthly scan without explicit user approval.

## Save and reload acceptance

The following must survive save and reload:

- famine stage and exposure age
- active causes and major pressure components
- relief state
- active movement cohorts
- origin and destination records
- route state
- border policy
- reception load
- trapped population
- return and integration progress
- hidden and public evidence
- Deaths totals and recent log
- category unlock and dormant state

No cohort should duplicate, disappear, or replay an arrival after reload.

## Invalid-scope behavior

The system must fail safely when:

- origin state no longer exists in the expected ownership context
- destination becomes invalid
- country is annexed
- route state changes during movement
- war ends
- border opens or closes
- state becomes wasteland
- controller changes
- special Chaos country transformation changes civilian eligibility
- a camp is destroyed or liberated
- a famine source disappears

Safe behavior includes retargeting to a valid state, pausing a flow, converting to trapped status, returning resources where appropriate, or cancelling without population change.

## Mixed-cause validation scenarios

### Island blockade with relief

Setup:

A populous island at war, no land route, damaged port, convoy shortage, hostile naval pressure, low reserves.

Expected behavior:

Food pressure rises quickly. Relief convoy, port repair, airlift, evacuation, and corridor options appear. Successful relief reduces mortality. Continued blockade can reach catastrophic famine.

### Island war without effective blockade

Setup:

An island at war with functioning port, convoys, escorts, local production, and no hostile route control.

Expected behavior:

No major blockade famine pressure.

### Leningrad-style siege

Setup:

Dense urban state encircled through winter with limited route access.

Expected behavior:

Famine, trapped population, evacuation and relief-route missions. Restored access causes gradual recovery.

### Bengal-style wartime access collapse

Setup:

Crop shock, import route loss, convoy priority, transport damage, delayed relief.

Expected behavior:

Multi-causal shortage and migration. A government that diverts transport and accepts aid can prevent the worst mortality.

### Soviet extraction and gulag escalation

Setup:

Low production, high extraction, movement restriction, deportation, forced labor, concealed reports.

Expected behavior:

Famine, forced movement, hidden evidence, regional opposition, Event 5 integration. Reducing extraction and opening relief reverses the crisis over time.

### Strategic-bombing exodus

Setup:

Repeated heavy bombing of a dense industrial state with damaged housing and rail.

Expected behavior:

Movement preparation, then organized or spontaneous exodus. Safe internal destinations receive population and pressure. Bombing deaths remain bombing deaths.

### Nuclear evacuation

Setup:

Nuclear strike on a dense state with nearby fallout.

Expected behavior:

Blast deaths first, then survivor movement, fallout restrictions, food pressure, and delayed return. No duplicate population loss.

### Genocide escapees and closed borders

Setup:

A targeted cohort flees a visible camp and reaches a neighboring closed border.

Expected behavior:

High desire, trapped population, foreign response, smuggling or humanitarian corridor options, possible deaths by proximate cause, condemnation for violent return.

### Outbreak flight with controlled reception

Setup:

An exposed state generates flight toward a neighbor with medical capacity.

Expected behavior:

Controlled reception can accept people and contain risk. Refugees do not automatically create an outbreak without exposure and containment failure.

### Postwar return

Setup:

War ends, origin is safe but damaged, host has a large displaced cohort.

Expected behavior:

Voluntary return, integration, resettlement, and forced return options. Return requires food, housing, route, and protection.

### Destination overload

Setup:

A small safe state receives a flow larger than its capacity.

Expected behavior:

Overcrowding, food and medical pressure, distribution and aid options. The population remains present and cannot be deleted by closing the category.

### Controller change during flow

Setup:

A route or destination changes control while movement is active.

Expected behavior:

Flow pauses, redirects, or becomes trapped. No duplicate debit or arrival.

## Probability acceptance

Weighted surfaces should satisfy scenario ordering.

Examples:

- relief is more likely as mortality and population rise
- concealment is more likely for repressive regimes with low visibility and high political cost
- concealment becomes less attractive as exposure and collapse risk rise
- safe internal destinations outrank unsafe foreign destinations
- open allied borders outrank distant neutral borders when capacity is similar
- direct persecution overwhelms same-ideology affinity
- quarantine reception outranks closure when outbreak exposure is proven and capacity exists
- forced return weight approaches zero for humanitarian AI when the origin remains exterminatory or catastrophic
- deliberate-starvation AI can choose harmful policy only when a compatible regime profile and strategic motive exist

The implementation agent should compare pre-patch and post-patch results using the same named scenarios whenever weights change.

## Asset acceptance

Every planned visible asset must have:

- an asset-type-specific brief
- matching vanilla or Chaos Redux reference inspection
- source mode
- source PNG or sourced original
- processed PNG
- final DDS
- correct path
- sprite handoff
- manifest or permanent provenance note
- in-game consumer

Icons for different surfaces must not be resized copies of one source icon.

## Localisation acceptance

Player-facing text must:

- name dynamic states, countries, routes, and values
- explain visible requirements and costs
- use concise cause breakdowns
- avoid raw internal variables
- avoid hidden future outcomes
- keep serious treatment for mass death and atrocity
- avoid treating refugees as inherently diseased or criminal
- distinguish voluntary evacuation, refugee flight, deportation, and forced return
- use current campaign facts and avoid fixed historical prose when the campaign differs

## Documentation acceptance

The final implementation should update:

- separate permanent famine and migration documents plus the neutral civilian-transfer contract document
- Deaths reason documentation
- Air Cleanliness integration documentation
- camps and genocide documentation
- occupation and condemnation documentation
- affected event docs
- decision and AI docs where separate
- the authoritative event catalog workbook for affected rows
- generated CSV exports through the repository tool
- dynamic effect and trigger registries for new public adapters

## Completion audit

The event completion auditor should be adapted to a system completion audit and compare:

- every source-spec requirement
- every accepted improvement-loop item
- every adapter
- every death reason
- every decision family
- every AI scenario
- every asset row
- every localisation surface
- every doc and catalog update
- every cleanup path

No fallback, simplification, missing asset, missing AI behavior, unlogged death, untransferred population, stale event row, or unresolved accepted plan can be hidden in the completion claim.

## Final acceptance checklist

The system can be called complete only when all of these are true:

- it has no random-event ID
- state famine severity is dynamic and visible
- unmanaged famine produces significant population-scaled deaths
- `From famine` is present in the Deaths breakdown
- migration transfers real population between real states
- route deaths are separate
- island blockade famine requires full evidence
- Air Cleanliness affects food pressure and recovery
- occupation, camps, gulags, forced labor, deportation, genocide, bombing, nuclear attacks, outbreaks, disasters, sanctions, war, and peace connect through adapters
- ideology is bounded and direct persecution can override it
- closed borders create trapped populations
- the decision category is hidden until the issue becomes sustained
- AI can use the same system
- the system avoids whole-world recurring scans
- Event 149 is absorbed or retired
- mixed-cause, save, reload, invalid-scope, probability, asset, localisation, and documentation checks pass
- no fixed historical casualty total is used
- no accepted design requirement remains simplified or unimplemented

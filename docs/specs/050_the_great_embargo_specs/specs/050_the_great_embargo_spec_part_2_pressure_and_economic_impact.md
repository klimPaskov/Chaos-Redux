# Event 050: The Great Embargo

## Part 2: Embargo Pressure and economic impact

All labels are working design labels. Final game text belongs to implementation and localisation review.

## One public value

The event exposes one persistent custom value, **Embargo Pressure**.

Embargo Pressure represents how effectively the coalition is isolating the target. It includes coalition unity, economic importance of participants, enforcement reach, replacement-route failure, and the target's diplomatic isolation.

The value should use a clear zero to one hundred range. The player must be able to see the current stage, current direction, next important threshold, and the largest actionable reasons for recent movement.

The target does not track a second custom dependence meter. Resource dependence, shipping exposure, industrial strain, coalition relevance, smuggling exposure, and intermediary reliability remain hidden calculations. They affect visible shortages, national modifiers, decision tooltips, stage consequences, and report events.

## Pressure stages

### 0: Embargo broken

The active embargo can no longer function. Resolution begins and crisis-owned restrictions are removed through the relevant outcome route.

### 1 to 19: Collapsing coalition

Restrictions survive mainly on paper. Replacement trade is broadly available and important members are leaving or ignoring enforcement. The target receives modest residual penalties while the coalition receives a final chance to reorganize.

Pressure should not end the crisis after one brief dip. The collapsing state must persist across two review checks, or a decisive coalition-collapse action must complete.

### 20 to 39: Porous embargo

Important restrictions remain, but neutral routes and commercial leakage prevent full isolation. Import-dependent countries still face friction and higher costs. Self-sufficient countries can operate with limited disruption.

This stage should favor diplomacy and opportunistic trade. Core participants begin asking whether the embargo still serves their interests.

### 40 to 59: Coordinated restrictions

The coalition functions as intended. The target loses meaningful access to imported resources, foreign support, and normal commercial cooperation. Replacement routes exist but require investment, risk, or political concessions.

Most baseline firings should open in this band or slightly above it.

### 60 to 79: Severe isolation

Major suppliers, ports, shipping states, and coalition partners are enforcing restrictions. Import-dependent production suffers sharp disruption. Fuel security, rubber, tungsten, chromium, steel, aluminum, convoys, and foreign equipment access can become urgent according to the target's actual economy.

Resource Seizure becomes possible when additional conditions are met. Defiance becomes stronger politically and more expensive economically.

### 80 to 100: Near-total isolation

The coalition has closed most important routes or punished the states that kept them open. The target must rely on domestic resources, protected routes, allies willing to defy the coalition, or military access to new supply.

This stage should create major pressure without making every country unplayable. A self-sufficient target can continue with significant trade and efficiency losses. A highly import-dependent target may face a severe production and fuel crisis.

## Opening Pressure

A normal opening should usually fall between 45 and 75. The starting value reflects the coalition assembled at the moment of firing.

Opening Pressure rises when:

- the convenor is a major diplomatic or economic power
- several core enforcers are major powers
- the target's largest plausible resource suppliers comply
- nearby land routes and important ports are covered
- the target has few willing allies
- the justification is supported by public campaign facts
- the target already has high public Condemnation
- the target is diplomatically isolated
- Evolution I is active before firing

Opening Pressure falls when:

- the target belongs to a strong faction whose members refuse the embargo
- important resource suppliers remain neutral
- a neighboring corridor state is willing to trade
- the coalition is divided by ideology or war
- the target controls large domestic resource reserves
- the justification is vague and relations are mixed
- the convenor has weak influence or is losing a major war

Opening Pressure should not directly include every target weakness. The same coalition can create similar Pressure against two targets, while their economic damage differs because one depends heavily on imports.

## Hidden dependence profile

The event needs a hidden target profile that estimates how much economic damage each Pressure stage should cause. It is a model of relevant exposure, not a false claim of exact bilateral trade volume.

The profile should consider:

- current deficits in oil, rubber, tungsten, chromium, steel, and aluminum
- domestic resource extraction
- synthetic refinery capacity and other substitutes
- current fuel stockpile and net fuel pressure
- convoy dependence
- usable ports and land corridors
- faction and subject access to resources
- number and importance of foreign trade partners where script can observe useful proxies
- industrial scale and resource demand
- active shortage penalties
- infrastructure and railway capacity for internal substitution
- current wars that make routes unsafe
- prior self-sufficiency investments

The implementation should group the result into internal profiles and keep the precise score hidden.

### Low dependence

The target can meet most essential demand from domestic resources, subjects, faction access, or reliable land routes. High Pressure mainly reduces efficiency, flexibility, and foreign support.

### Moderate dependence

The target can replace some imports, but several industries remain exposed. Coordinated restrictions create production choices and fuel planning problems.

### High dependence

The target relies on foreign supply for several strategic inputs or depends heavily on convoys. Severe Pressure can reduce output, mobility, aviation, naval operations, and reinforcement capacity.

### Critical dependence

The target lacks a workable replacement for one or more essential resources and has little stockpile depth. Near-total isolation creates an immediate strategic emergency and makes concessions, smuggling, or resource seizure much more attractive.

## Coalition effectiveness profile

Pressure changes should also use an internal coalition-effectiveness model. A country contributes according to its practical role.

Useful contribution factors include:

- major-power status
- share of relevant world resources
- location on a likely land corridor
- control of nearby ports, canals, or sea routes
- merchant shipping and convoy capacity
- financial and commercial reach
- faction leadership
- ideological influence over other participants
- ability to threaten neutral intermediaries
- rivalry with the target
- economic cost of participation

Small distant participants can add diplomatic breadth without producing the same Pressure as a resource supplier or shipping power.

## Economic consequence families

### Strategic resource access

The event should make imported strategic resources harder to obtain and less reliable. It may use native embargo behavior where available, event-owned trade penalties, access restrictions, target modifiers, or other validated means.

The final implementation must avoid pretending it can cancel exact bilateral trades when the engine cannot identify them safely. Player-facing text can describe lost access and halted shipments while the mechanic applies pressure through supported economic surfaces.

### Fuel and mobility

An import-dependent target should feel fuel risk quickly. Pressure can reduce access to oil, make fuel imports less effective, increase the cost of replacement routes, and create emergency stockpile decisions.

Fuel effects must use the target's current position. A country with a deep stockpile receives a warning window. A country already near exhaustion faces immediate operational choices.

### Industrial efficiency

The embargo can reduce factory output, production efficiency retention, efficiency growth, construction throughput, or other supported economic statistics. The penalty should scale with Pressure and dependence.

A low-dependence country should not receive the same industrial penalty as a country whose factories cannot obtain essential inputs.

### Foreign military support

New lend-lease, volunteers, attachés, production cooperation, and other foreign support can become harder where the engine supports reliable checks. The event should not promise generic cancellation of agreements that script cannot revoke safely.

Existing support should be treated according to validated engine behavior. Event-owned penalties can represent delays, insurance risk, inspection, and political reluctance when direct cancellation is unavailable.

### Diplomatic and commercial isolation

The target loses opinion with coalition members, has greater difficulty securing economic agreements, and may face higher costs when negotiating through neutral states. The penalty should depend on coalition breadth and the public reason.

### Shipping and route friction

Convoy-dependent replacement imports should consume more convoys, fuel, civilian capacity, or time. Landlocked targets should care more about border corridors. Island targets should care more about ports, shipping, and escort exposure.

### Domestic substitution pressure

High Pressure makes domestic extraction, synthetic production, rationing, salvage, and infrastructure projects more valuable. These options carry real construction and consumption costs. They should not appear as free compensation for the event penalty.

## Scaling model

The intended result can be thought of as:

`economic impact = pressure stage x dependence profile x active route conditions x mitigation`

This is a design relationship, not a required literal formula.

Pressure answers how unified and effective the coalition is. Dependence answers how much that isolation hurts this target. Route conditions account for wars, ports, borders, faction access, and active intermediaries. Mitigation reflects self-sufficiency projects, smuggling success, stockpiles, and temporary emergency measures.

The implementation should centralize thresholds and effect bands. It should avoid scattered one-off values across events, decisions, ideas, and scripted effects.

## Review rhythm

The crisis should use a bounded review rhythm, normally around thirty days. Reviews recalculate the parts of the crisis that can reasonably change:

- active coalition membership
- role of core enforcers
- neutral-route status
- completed target responses
- exposed smuggling
- accepted concessions
- coalition fatigue
- current target viability
- active evolution rules

Reviews should process registered active crises and their stored participants. They should not scan every country every day.

Immediate actions can change Pressure between reviews. A major participant leaving, a smuggling network being exposed, or a settlement being accepted should have an immediate effect. The next review then reconciles the full state.

## Pressure movement

### Reliable reasons for Pressure to rise

- a core enforcer joins
- a major supplier closes access
- a neutral route fails
- smuggling is publicly exposed
- the target openly defies settlement demands
- the target threatens a coalition member
- an intermediary accepts coalition pressure
- secondary sanctions are imposed on a trader
- coalition enforcement is renewed after a review
- a target begins resource-seizure preparation and the coalition discovers it

### Reliable reasons for Pressure to fall

- a core participant leaves
- a major supplier secretly trades and remains undiscovered
- a neutral intermediary opens a replacement route
- a self-sufficiency project reduces the coalition's leverage
- the target accepts a meaningful concession
- a coalition member is distracted by war or internal collapse
- coalition fatigue weakens enforcement
- rivalries split the core enforcers
- several minor participants defect together
- a settlement framework receives enough support

### Reasons that should not move Pressure by themselves

- ordinary passage of one day
- a decision click before its action resolves
- evolution eligibility
- a normal resource deficit already counted through dependence
- generic war, annexation, death, or contamination effects
- a flavor report with no state change

## Dynamic duration

The ordinary crisis should last several months to more than a year.

Suggested design bands:

- fragile coalition: roughly 180 to 300 days
- normal coalition: roughly 270 to 540 days
- highly unified coalition: roughly 450 to 600 days
- absolute ordinary hard cap: roughly 720 days

The final duration should depend on opening Pressure, coalition structure, justification strength, target responses, world wars, participant fatigue, and evolution state.

A collapsing coalition can end early after the required confirmation period. A unified coalition can extend the crisis during review rounds, but cannot create an endless lock. The hard cap forces a final political review or settlement outcome.

## Coalition fatigue

Fatigue is internal. It represents the cost of lost trade, changing war priorities, domestic opposition, administrative effort, and declining attention.

Fatigue grows faster when:

- the target is a major market for participants
- the embargo creates shortages inside the coalition
- the justification is weak
- the target has adapted and Pressure no longer produces visible concessions
- core participants are fighting major wars
- secret trade becomes widespread
- the crisis lasts beyond a year

Fatigue grows slower when:

- the target continues the behavior that caused the embargo
- public Condemnation remains high
- the coalition has low economic exposure
- the target threatens participants
- hardliners dominate the coalition
- Evolution I provides strong enforcement tools

The player sees fatigue through stage movement, member reports, and a concise trend explanation. It should not become another meter.

## Feedback and clarity

The target category must answer:

- current Embargo Pressure and stage
- recent direction
- next threshold that matters
- the most urgent visible economic exposure
- the leading coalition members
- the current replacement route or active mission
- the likely effect of each available response

The tooltip can list a small number of material causes. It should not show a full internal ledger of every country and coefficient.

Outside participants should see their own role, the target, the coalition's current stage, the cost of staying, and the consequence of leaving or trading. They do not need access to the target's complete hidden dependence model.

## DLC resilience

Event 50 must function without a native diplomatic embargo feature.

A DLC feature can reinforce the crisis when available. It cannot become the only source of economic pressure, coalition membership, target responses, or resolution.

The baseline event-owned layer must provide:

- visible Pressure
- target penalties
- coalition roles
- replacement-route play
- participant choices
- concessions
- smuggling consequences
- duration and resolution

DLC-specific additions should stay additive and clearly bounded.

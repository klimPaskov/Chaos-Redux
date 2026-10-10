# Event 22 Concentration Camps

## Part 2: Baseline progression and decision system

## Baseline progression

The baseline is a living crisis, not one event option followed by a permanent modifier. It moves through six ordinary stages. These stages can occur at any chaos tier and do not count as evolutions.

### Stage 1: Network imposed

The selected country reaches 20 percent camp coverage. The opening policy is chosen, the management category appears, responsibility is recorded, and the country joins the shared camp processor.

The player should immediately understand:

- how many eligible states contain camps
- which policy currently governs the network
- whether intake is open or frozen
- which state has the highest immediate risk
- what the first useful response is

The opening does not expose every hidden consequence. It must still explain visible deaths, resource commitments, output direction, resistance, and discovery risk.

### Stage 2: Policy commitment

The initial response becomes a concrete program.

- Closure starts the regional closure mission and the shared reform path.
- Review sets the custody mandate and opens inspections, ration support, registration, and release actions.
- Forced labour sets the coercive mandate; the Ledger economic priority chooses industry, works or extraction.
- Security expansion creates new state targets and transport demands.
- Evolution I can add extermination conversion.

A country can change policy later, but changing direction costs time and creates institutional conflict. A regime cannot collect a full exploitation cycle and then close every site instantly before evidence rises.

### Stage 3: Operational cycle

Operational sites are processed by the shared camp processor: `camp_admin_monthly_country` visits each registered operational site once per calendar month and applies custody, labour and violence causes through `camp_admin_record_deaths`.
Event 22 adds no pulse, no private death rate and no second scan.
It reads the processor's results to update:

- Exposure
- Resistance Pressure
- hidden atrocity and cover-up evidence
- foreign-observer pressure where witnesses or external access exist

Only registered countries and registered states participate. The event must not scan the whole world every day or every week.

### Stage 4: Fracture and leak

The network develops visible problems. Possible incidents include:

- escape networks
- sabotage of railways, factories, mines, or records
- guard desertion or military objection
- local famine and ration theft
- disease outbreaks
- labour exhaustion
- missing transports
- foreign intelligence reports
- family searches and refugee testimony
- administrators stealing seized property
- a natural disaster exposing the site
- an air raid or front advance damaging the camp

These incidents are baseline consequences. They are not evolutions.

### Stage 5: Exposure or retreat

Exposure crosses a threshold, enemy forces approach, a civil war changes control, or the government begins to collapse. The category replaces ordinary actions with emergency choices. The country may close sites, preserve records, destroy evidence, relocate prisoners, force an evacuation, abandon the network, or intensify killing before retreat.

The design must make retreat choices costly and visible. A player should not be able to erase a network with one hidden cleanup effect.

### Stage 6: Closure, liberation, or entrenchment

The crisis ends in transparent closure, secret demolition, liberation, dormant repression, entrenched forced labour, or extermination. Long-term evidence and survivor effects can continue after active camp operation ends.

## Player-facing values

The Event 22 category shows two event-owned meters and one status line.
The shared Condemnation value remains in the Chaos Meter.
The original design showed three meters; the third, Network Reach, is reduced to a status line by proposal P-022-A (the band ladder below is the fallback if the parent keeps three values).

### Network Reach (status line)

Network Reach is the share of eligible states containing an operational concentration camp, extermination camp, or compatible active gulag site attributed to the current network.

Player-facing information:

- operational site count of eligible states
- current coverage percentage
- the next target that matters (the generic ceiling or the Evolution III target)

Reach rises through expansion, conversion of quiet sites, inherited operation, or Evolution III. It falls through closure, liberation, state loss, or destruction. Conversion from a concentration camp to an extermination camp does not change reach.

Fallback status bands, if three values are kept: isolated sites, regional network, national network, entrenched network, half-country network.

### Exposure

Exposure represents the chance that the network's purpose, deaths, records, and responsible officials become publicly verifiable.

Exposure rises through:

- deaths and disappearances
- extermination sites
- medical or chemical sites
- foreign observers
- occupied non-core territory
- escapees, refugees, and family searches
- resistance networks
- damaged or abandoned sites
- retreat and hurried evacuation
- inconsistent records
- failed cover-up actions
- natural disasters, bombing, or loss of local control
- the discovery of one linked site

Exposure falls slowly through genuine closure, transparent inspection, survivor registration, and orderly record transfer. Secret concealment can reduce immediate Exposure, but it creates cover-up evidence and a larger later discovery penalty.

Status bands:

- Controlled secrecy
- Persistent rumours
- Credible leaks
- Verified evidence
- Publicly documented network

The player can see the current band and main causes. The full hidden evidence ledger remains internal.

### Resistance Pressure

Resistance Pressure combines local opposition, escape networks, sabotage, guard strain, military objection, partisan recruitment, and political conflict caused by the camp system.

It rises through:

- high deaths
- non-core or occupied-state camps
- forced labour and extermination policies
- overcrowding, famine, disease, and abuse
- low garrison coverage
- high local resistance
- family and refugee networks
- foreign support
- evidence destruction
- purge broadening into core populations

It falls through:

- closure and release
- medical relief and food delivery
- real improvement in conditions
- secure but nonviolent administration during dismantlement
- successful mediation with military, civil service, or local authorities

Violent suppression can reduce one local resistance incident temporarily, but it raises hidden pressure, deaths, and future rebellion risk. It cannot permanently solve the value.

Status bands:

- Disorganized opposition
- Escape networks
- Coordinated sabotage
- Armed resistance
- Administrative breakdown

## State-level information

A camp-state tooltip shows at most:

- site role and responsible actor
- operational status (operating, under inspection, closing, abandoned, liberated)
- one local pressure direction (mortality, resistance or evidence, whichever is the highest)
- closure or relief mission status

The full state ledger (living custody, causes, records) stays in the Ledger Locations and Records views.
The tooltip must not show a fictional racial census. It should use the actual campaign source of detainees when known, such as occupied civilians, refugees, political detainees, resistance suspects, or a country-specific persecuted group registry.

## Hidden state values

The implementation tracks internal values only where a rule reads them:

- living custody cohort, causes and release totals (owned by the shared custody ledger)
- local evidence (owned by the shared evidence system)
- network generation
- Evolution II shock applied
- Evolution III shock applied
- closure progress and relief progress
- chemical-site integration

Intake pressure, guard capacity, transport dependency, ration condition, disease pressure and the other components of the original list are summarized into Exposure, Resistance Pressure and the shared support ratio, and are not tracked as separate Event 22 values.
Only values that change an immediate player choice appear directly.

## Decision category presentation

### Recommended layer

Use an ordinary decision category with:

- one static archival category picture
- a concise header showing Exposure, Resistance Pressure and the Reach line
- one current policy line
- one current priority state line
- normal decision rows
- state-targeted decisions when needed
- no fake buttons or meters painted into the image

A full scripted GUI would add maintenance without improving the choice structure, and the shared Ledger already provides the management window. Animation is unnecessary because the values can be read through status icons, bands, and replacement decisions.

### Visible action budget

A phase should normally expose three to five primary actions. Six is the hard maximum. The category may show one to three active missions.

Actions are replaced when the policy or crisis stage changes. Earlier weak versions should disappear when stronger or more specific versions become available.

## Opening policies

The opening event sets one of four baseline policy families (a fifth, extermination, joins at Evolution I). The final event options should be written from this direction and should not be copied from the working labels.

### Policy A: Freeze intake and close the network

Immediate effects:

- new detentions stop
- operational deaths fall but do not end instantly
- local food and medical access improve
- the regional closure mission becomes available
- forced-labour output winds down
- hardliners, security services, or wartime ministries may resist
- evidence remains intact unless separately destroyed

This is the safest long-term route, but it has meaningful costs. The country must replace lost output, secure sites, feed survivors, move people safely, investigate missing records, and absorb political conflict.

### Policy B: Restrict, inspect, and review

Immediate effects:

- expansion is frozen
- forced work stops (custody mandate)
- inspections and registration begin
- low-level detention can continue while cases are reviewed
- Exposure may rise because records and witnesses become visible
- public Condemnation can later fall if the process becomes transparent and real closure follows

This route is useful for governments that cannot immediately dismantle every site. It can drift into closure, controlled repression, or renewed exploitation.

### Policy C: Mobilize forced labour

Immediate effects:

- the coercive mandate starts forced-work output at the sites with a labour role
- trains, guards, support equipment, and local supplies are committed through the shared maintenance cost
- local output rises up to the shared caps
- mortality, resistance, disease, sabotage, evidence, and labour depletion rise
- national benefits scale with the surviving supported workforce, not raw building count

The route is a wartime shortcut. It is powerful over a short period and destructive over a longer period.

### Policy D: Expand the security network

Immediate effects:

- targeted expansion decisions appear
- detention and deportation capacity rise
- short-term local resistance target may fall in states under terror
- local garrison and transport needs rise
- Exposure and Resistance Pressure rise
- extremist factions gain temporary internal leverage

This policy is unavailable or strongly blocked for governments whose current political route rejects arbitrary detention. A breakdown, emergency law, or radicalization event can change that validity.

## Dismantlement route

Dismantlement is a staged program run as `chaosx_022_mission_regional_closure`. It should not be a political-power purchase.

Objectives, each completed by the mission and not by a separate click:

- freeze new detentions (shared reform freezes admissions; local administrators in high-resistance or low-authority states can continue intake, which raises Exposure and domestic conflict)
- supply and medical relief, scaled by site count, local supply, famine, disease and distance from the capital, lowering mortality, disease and Resistance Pressure
- register detainees and missing persons (may raise immediate Exposure because it produces verifiable records; improves release safety, tracing and tribunal accuracy)
- preserve or transfer records according to the evidence policy
- release or relocate survivors safely
- remove the camp building through the shared timed site closure, never as a free deletion

Mission duration rises with site type, population, damage, disease, front proximity and local resistance, and falls with infrastructure, relief preparation, government authority and foreign assistance.

Outcomes:

- success: operation stops, survivors leave custody safely, reach falls, records follow policy
- partial success: operation stops but records are incomplete or survivors remain displaced, with a follow-up relief mission
- failure: deaths continue, the site becomes chaotic or abandoned, Exposure and Resistance Pressure rise, a repeat mission is harder

Replacing coerced output uses the shared civilian workforce replacement of the reform path.
It costs more than keeping forced labour for one short cycle, but creates a stable replacement without deaths, sabotage or evidence growth, so dismantlement is strategically viable and not a moral button that accepts permanent economic defeat.

Complete national closure appears when every site has stopped intake and every closure or relief mission is resolved:

- transparent closure grants the longest event protection and lowers future foreign pressure
- quiet closure leaves hidden evidence and a weaker protection period
- destroyed records create cover-up evidence and later liability

## Review and restriction route

The review route is a middle path. It can buy time, reduce deaths, and expose illegal administration. It cannot turn Event 22 sites into lawful internment through a label change.

- Minimum conditions (food, shelter, sanitation, medical commitments) lower mortality and disease, reduce the strongest forced-labour output, and raise administrator resistance in exploitative regimes.
- Controlled inspections allow domestic judiciary, military, church, civil service, neutral commission, or foreign observer access depending on country; they lower hidden abuses when access is real, raise immediate Exposure, can reduce public condemnation if violations are corrected, and fail if officials stage the inspection.
- Case review releases people who lack even the regime's stated grounds, reducing the cohort, resistance and future deaths, with political conflict from hardliners.
- Conversion to ordinary prisons or lawful detention is available only when the country has functioning legal institutions and the site population can be individually reviewed. It removes the Event 22 camp building and ends the atrocity loop in that state without preserving forced labour or mass detention output.

A review can end in full closure, a smaller dormant repression network, failed reform and renewed exploitation, public scandal and forced resignation, or military or civil-service refusal to continue.

## Forced-labour route

Forced labour is the main short-term economic temptation, and it is owned by the shared administration.

- The coercive mandate lets labour-role sites produce; the Ledger economic priority (industry, works or extraction) chooses what they produce, and the spending ceiling limits it.
- Output follows the surviving, supported workforce. The shared caps hold: developed contributions reach at most 40 percent equivalent participating industrial output, capped at 25 percent nationally, 40 percent relevant state construction and 40 percent local extraction.
- Extermination (killing-role) sites lose productive allocations.
- The detained workforce is finite. It falls through deaths, release or escape, transfer, disease and incapacity, successful resistance and liberation. A depleted site loses its output before it loses its mortality and evidence consequences.
- The regime can close the site, lower the priority, move detainees through a visible deportation (the shared exact-cohort transfer needs real transport and a proved cohort), or broaden persecution. It cannot generate workers from nothing.
- Deportation and transport consume real trains or convoys, add congestion and Exposure, and can trigger escape, bombing, disease or disappearance incidents. The spec requires no detailed schedules or procedural depiction.

The original design had four per-state assignments (industrial, construction, extraction, logistics) with intensity tiers.
They are replaced by the shared priority because the Ledger already offers that choice, and the logistics assignment had no rule that read it.

## Security expansion route

`chaosx_022_expand_network_into_state` is the only expansion action.

Requirements: the state passes eligibility, reach is below the applicable ceiling, policy permits expansion, and transport, guard and construction capacity exist.

Dynamic costs: construction burden, support equipment, trains or convoys, manpower or garrison commitment.

Effects: adds a concentration camp, raises reach, records responsibility, seeds an initial cohort from valid campaign markers through the shared admission helper, raises Exposure and Resistance Pressure.

Guard reinforcement is an option of the escape incident.
Centralized administration and seizing local property are dropped; their consequences are carried by network verification (more linked sites make a verified network) and by the administrator corruption incident.

## Concealment and evidence actions

Concealment is available to active perpetrators. It is not a clean way to lower consequences.
It is offered as options of the leak, inspection and front-approach events, which reuse the shared evidence effects.

- Restrict access reduces immediate foreign-observer pressure, harms diplomacy and intelligence transparency, increases suspicion when leaks already exist, and is weaker in occupied, coastal, border, or high-resistance states.
- Falsify records lowers immediate Exposure if successful, creates cover-up evidence, risks contradictory transport, labour and population records, and makes later verified discovery more damaging.
- Destroy records reduces surviving documentation but cannot remove survivor testimony, physical evidence, demographic loss or foreign intelligence. It raises cover-up evidence, harms the ability to release, trace or compensate survivors, and can trigger administrator conflict or whistleblowing.
- Relocate detainees requires transport, can move people away from an exposed state, raises death, escape, bombing and discovery risk, and can become a death march when transport fails or the front is close.
- Abandon a site stops organized operation without completing relief, leaves survivors, guards, records and infrastructure in a dangerous state, raises Exposure sharply, and can cause post-liberation deaths from neglect.

## Resistance and emergency missions

The category may run one to three active missions (`chaosx_022_mission_prevent_escape`, `chaosx_022_mission_contain_epidemic`, `chaosx_022_mission_underground_network` and the closure mission).

- Prevent a coordinated escape: relief and de-escalation can reduce the underlying pressure, reinforcement may prevent the immediate escape while raising long-term burden, and violent suppression can stop the attempt but causes deaths and stronger evidence.
- Contain a camp epidemic: success requires medical supplies, food, transport and time; failure causes deaths, regional disease spread, escape and discovery. Inputs are overcrowding, the famine stage (`famine_food_stage_requires_mortality`), plague, biological contamination and destroyed infrastructure.
- The front-approach emergency is an event with the retreat options of Part 4, not a mission.
- Regional closure groups several nearby sites under one objective, which reduces decision clutter in large countries.

## National and state modifiers

The event prefers staged upgrades and replacements over many separate tiny ideas, and adds a modifier only when a rule reads it.

### Country-level idea families

Working labels only:

- Camp Network Administrative Burden
- Security Apparatus Ascendant
- Network Under Review
- National Dismantlement Program
- Publicly Exposed Atrocities
- Survivor Relief and Resettlement
- Tribunal and Documentation Pressure

Each family changes stage as policy and exposure change. Do not create one new idea for every decision.
The original eighth family, Forced-Labour War Economy, is dropped because the shared national output modifier already represents it.

### State-level status families

Possible state statuses (shared site role plus Event 22 status):

- Active Detention Site
- Extermination Site
- Site Under Inspection
- Site Closing
- Abandoned Site
- Liberated Site
- Survivor Relief Centre
- Evidence Preserved
- Evidence Destroyed

The building shows physical presence. The status shows how the site is operating.
Per-assignment and "Overcrowded" or "Labour Pool Exhausted" statuses of the original list are not modifiers; the Ledger shows exhaustion.

## Effect strength rule

The economic route must be strong enough to tempt a wartime player. The penalties must be strong enough that the route changes strategy and cannot be treated as a free modifier.

Balance direction, all inside the shared constants:

- one fully supplied, high-workforce site can materially improve one state's role
- a national network can support a noticeable wartime output surge, never above the shared 25 percent national cap
- the surge declines as workforce, supply and support deteriorate (the shared support ratio)
- high-intensity operation should begin creating serious strategic costs within several months
- extermination sites do not improve industrial output
- transparent closure creates a credible long-term recovery path

Exact numbers belong in the shared camp constants and the probability and balance pass. The implementation should test several country sizes and war situations before locking values.

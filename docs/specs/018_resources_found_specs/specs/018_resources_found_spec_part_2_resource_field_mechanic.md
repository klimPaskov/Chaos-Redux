# Event 018 Resources Found Specification, Part 2

## Resource field management system

All names in this file are working labels for design structure. They are not final localisation.

## The management promise

The resource field should feel like a living state project rather than a passive modifier. The owner chooses how quickly to develop it, who receives access, what infrastructure is built, how workers are protected, how the field is defended, and when extraction has gone too far.

The system should stay compact. The player needs one decision category with a small field overview and a controlled set of current actions. A large separate custom window is unnecessary. The preferred presentation is a decision category with a scripted GUI header that shows the selected field, its resource composition, four baseline values, one status image or seal, and buttons to cycle between the owner’s active fields.

Human players should see only decisions relevant to the selected field. AI countries should evaluate all valid fields directly without depending on the human selection interface.

## Field data model

Each active field needs enough persistent state to support repeated discoveries, state transfer, foreign contracts, closure, and evolution.

### Field identity

The field record needs:

- a unique field sequence
- the state that contains the field
- the country that discovered it
- current owner
- current controller
- discovery date
- discovery count
- current lifecycle stage
- current administrative posture
- current selected resource presentation
- whether the site is active, suspended, closing, closed, or converted into a cave origin

### Event-owned resource ledger

The field must store Event 018 additions separately for every standard resource type.

The ledger needs to answer:

- how much Event 018 oil is in the state
- how much Event 018 aluminium is in the state
- how much Event 018 rubber is in the state
- how much Event 018 tungsten is in the state
- how much Event 018 steel is in the state
- how much Event 018 chromium is in the state
- the total Event 018 resource amount
- the number of distinct resource types found
- the largest single-resource Event 018 deposit

These values support closure, achievement tracking, international interest, and cave-country spawn strength. They must never be reconstructed by subtracting assumptions from the state’s total resource values.

### Field values

The field stores:

- Developed Yield
- Excavation Depth
- Workforce Safety
- Foreign Pressure
- Subsurface Disturbance after the mechanic begins tracking it
- Breach Pressure after the public monster phase begins
- closure progress
- transport capacity
- security level
- local labor strain
- foreign ownership share or concession influence
- smuggling pressure
- active contract count
- accumulated field deaths
- accumulated exploitation score

Not every value needs a permanent space in the visible header. The four baseline values are always shown. Disturbance becomes visible only when Evolution II makes it meaningful. Breach Pressure becomes visible in Evolution III.

### Country and contract references

The field can remember:

- primary foreign concession partner
- secondary trade partner when relevant
- international commission sponsor or guarantor
- current claimant in a border dispute
- country responsible for active sabotage or smuggling when known
- former owner with unresolved compensation

These references require cleanup when countries disappear, annex, change sides, or become invalid.

## Visible field header

The compact header should provide immediate answers without requiring the player to open several tooltips.

### State and resource summary

The header shows the selected state and a row of resource icons with integer amounts added by Event 018. It should distinguish event-owned additions from the state’s total resource amount through wording or tooltip structure.

The resource row should not show an empty icon for every type when only one resource exists. It can show the active types and a compact total. The detailed tooltip can list all six types and the exact Event 018 contribution.

### Status seal

A central seal or field illustration communicates the current lifecycle and danger state. The baseline asset can show geological survey marks, a mine headframe, a drill derrick, or a resource authority emblem. Evolution states replace or overlay this art with distinct visual states.

The static fallback is mandatory. An animated seal is useful because slow movement can show active development, a warning pulse can show unsafe pressure, and later frames can show abnormal vibration. The animation must be state-driven and use real source frames through the frame-animation workflow.

### Value display

Each value appears with:

- an integer number
- a named band
- a short cause-and-effect tooltip
- a consistent color identity
- a breakdown of recent or permanent contributors where practical

Suggested color direction:

- Developed Yield uses industrial gold or warm yellow
- Excavation Depth uses stone grey or dark orange
- Workforce Safety uses green when healthy and red when failing
- Foreign Pressure uses diplomatic purple or blue
- Subsurface Disturbance uses a muted unnatural color introduced only after reveal
- Breach Pressure uses a severe warning color

The exact color codes belong to implementation.

### Field switching

Countries with several active fields can cycle through them. The UI should show the number of active fields and selected position. Closing or losing a selected field should automatically select the next valid field or close the category cleanly.

## Administrative postures

The initial posture shapes costs, decisions, AI, and foreign reaction. It is not an irreversible ideology path. Changing posture later should require a transition project and can create compensation or labor consequences.

### National resource authority

This posture maximizes sovereign control and domestic allocation.

Strengths:

- lower foreign ownership pressure
- stronger ability to reserve output for domestic use
- easier national security and closure orders
- better integration with state infrastructure projects
- more reliable contract enforcement

Costs:

- higher civilian construction burden
- slower early machinery access for weak countries
- greater responsibility for safety and worker compensation
- greater diplomatic pressure from countries denied access

### Domestic commercial charter

This posture relies on local firms and private investment.

Strengths:

- faster early development
- lower direct state construction burden
- stronger local employment and market growth
- flexible trade contracts

Costs:

- higher labor strain during a rush
- more smuggling and corruption exposure
- harder suspension and closure
- companies may resist safety rules or national direction

### Foreign concession

This posture gives one foreign partner a large role.

Strengths:

- machinery, expertise, transport, and capital arrive quickly
- the partner becomes diplomatically invested in the owner’s stability
- development can continue when the owner lacks industry
- export contracts are easier to establish

Costs:

- foreign influence and compensation claims
- part of the field’s benefit is committed abroad
- contract-breaking can damage relations and trigger pressure
- rival powers may support smuggling, sabotage, or competing claims

### International commission

This posture becomes available after severe foreign pressure or a negotiated demilitarization process.

Strengths:

- reduces immediate seizure risk
- distributes access through a supervised quota
- lowers border-war chance
- can attract neutral engineering and inspection support

Costs:

- restricts unilateral military use and fortification
- limits national control over contracts
- slows emergency extraction
- creates political friction with nationalists and military leaders

### Strategic reserve administration

This posture suspends most extraction and preserves the resource.

Strengths:

- lowers Excavation Depth and disturbance growth
- reduces labor casualties and foreign visibility
- preserves reopening options
- can deny an occupier a fully developed asset

Costs:

- lowers current economic return
- may breach contracts
- requires guarding and maintenance
- foreign partners can demand reopening during war

## Core actions

The decision category should use phases and replacement decisions. The player should not see every action at once.

## Survey and appraisal actions

### Commission geological appraisal

Purpose:

- improve reserve confidence
- reveal whether another deposit roll is possible
- reduce waste in later development
- establish the first transport and safety requirements

Costs should reflect engineering work. Appropriate components include civilian factory use, trucks, trains, fuel, support equipment, construction time, and a modest political or administrative cost.

The action should have partial outcomes. A weak survey can confirm the current amount without finding more. A strong survey can reveal an extension or improve Developed Yield. Aggressive methods can also increase Excavation Depth.

### Drill or shaft a deeper test

Purpose:

- seek a richer layer
- increase the chance of an enrichment firing
- unlock high-yield development

This action should be attractive and dangerous. It consumes machinery and raises Excavation Depth. Before Evolution II, its risks are ordinary accidents, overruns, and labor strain. After Evolution II, it also raises Subsurface Disturbance.

### Map the surrounding basin

Purpose:

- improve transport planning
- reduce the chance that later investment targets the wrong state area
- identify local settlement, water, or rail constraints

This action favors careful administration. It can lower future infrastructure cost and improve closure planning.

## Development actions

### Open primary works

This is the first major development project. It constructs the shafts, wells, processing yards, pumping stations, or collection system that makes the deposit a mature asset.

The project should require actual industrial commitment. It can use a temporary civilian factory burden, construction materials represented by support equipment, trucks, trains, or fuel, and a duration scaled by infrastructure and war conditions.

Completion raises Developed Yield substantially and can add a building, rail connection, or infrastructure improvement in the state.

### Extend the rail and road corridor

This project improves resource movement and supply. It should target the field state and one practical connection rather than granting abstract national infrastructure.

Benefits can include:

- infrastructure or rail improvements
- lower transport strain
- higher Developed Yield
- lower smuggling if the state controls the route
- better military supply if the field is near a front

The project becomes harder under occupation, bombing, severe terrain, or a broken connection to the owner’s capital network.

### Install heavy machinery

This project consumes or commits equipment and industrial capacity to raise extraction.

It should be especially valuable for countries with low initial development. Foreign concession partners can supply part of the requirement. Heavy machinery increases output and Excavation Depth, so it is not a free safety upgrade.

### Build local processing

This project adds refining, sorting, smelting, storage, or preparation capacity. The exact flavor follows the resource type.

The project should create one meaningful map or production change, such as an industrial building, a local processing modifier, or stronger resource-to-market efficiency. It should not grant a tiny generic national bonus.

### Expand worker settlement

This project relieves housing and labor strain, improves local administration, and can raise Workforce Safety. It consumes civilian construction and can increase the state’s strategic importance.

The project should help distinguish regulated development from pure rush extraction.

## Labor and safety actions

### Recruit regional labor

The owner expands the workforce through wages, migration, labor offices, or mobilization.

Benefits:

- faster projects
- higher Developed Yield
- lower immediate labor shortage

Costs and risks:

- local population movement
- housing and food strain
- higher exposed population if safety is poor
- political tension if coercive methods are used

The player should choose between voluntary recruitment, state-directed labor, military labor, and foreign specialist teams only when the country’s politics and route support those variants.

### Shorten shifts and rotate crews

This decision lowers extraction tempo for a period and raises Workforce Safety. It should reduce sickness and later disturbance exposure. Its cost is lost output and possible contract penalties.

### Reinforce shafts and ventilation

This decision consumes support equipment, construction capacity, and time. It provides a substantial safety improvement and reduces ordinary accident chance. It should remain useful in Evolution II, though it cannot fully explain or stop supernatural corrosion.

### Establish a field hospital and inspection office

This creates medical and regulatory capacity. It lowers deaths from ordinary accidents, improves information quality during Evolution II, and makes early symptoms visible sooner.

The institution can become a staged idea or state modifier that is upgraded rather than replaced by many separate safety bonuses.

### Compensate affected families

This action responds to accidents, sickness, or missing workers. It costs money through political and civilian capacity proxies, reduces unrest, and can improve trust in official reporting. It does not reverse population loss.

### Conceal the casualty reports

Authoritarian or desperate owners can suppress information. This delays Foreign Pressure and public panic, but worsens labor trust, increases future revelation impact, and makes safe closure harder. AI should use this mainly when regime survival, war pressure, or extreme extraction goals outweigh legitimacy.

## Security and integrity actions

### Organize field guards

The owner protects equipment, depots, shafts, and access roads. Appropriate costs include manpower commitment, infantry equipment, support equipment, and command attention.

The action lowers theft and sabotage but can raise local tension. It should not create free field divisions.

### Counter foreign survey teams

This action targets espionage, illegal sampling, and contract manipulation. It uses intelligence or security capacity where available. Success lowers Foreign Pressure and can expose a foreign actor. Failure can create a diplomatic incident.

### Break the smuggling network

This is a short mission or decision chain, not a flat political power purchase. The player may need to secure rail hubs, ports, border crossings, or the field state while spending equipment and police capacity.

Success lowers smuggling and raises control. Failure can strengthen criminal networks or foreign influence.

### Prepare controlled demolition

This action creates a defensive denial option if the state is about to be lost. It requires engineering equipment, security, and time. Using it damages Developed Yield and infrastructure, but it should not erase the geological reserve unless the full closure project succeeds.

## Economic and trade actions

### Reserve output for domestic industry

This route prioritizes national use. It lowers foreign access and can strengthen war production when the country has a real resource deficit. It raises Foreign Pressure if major partners expected exports.

### Offer long-term export contracts

The owner invites eligible countries to compete for a contract. The choice should use diplomatic need and not simply pick the strongest major. Bidders can offer machinery, factories, rail support, equipment, guarantees, or favorable trade relations.

### Create a spot market

The owner sells broadly without granting one deep concession. This increases short-term economic activity and foreign traffic, but it also raises smuggling and volatility.

### Renegotiate the concession

This becomes available when the field’s value changes, the partner is weak, or the owner gains leverage. Results include better terms, increased investment, partial nationalization, or dispute.

### Nationalize the field

This is a major political action with compensation, diplomatic, and economic consequences. It should not be a cheap button. The owner may need sufficient stability, administration, security, and domestic development to replace foreign management.

Nationalization can succeed cleanly, trigger compensation negotiations, lead to embargo pressure, or encourage sabotage. It should create a strong national-control payoff when the owner has prepared.

## Rush extraction modes

The field can enter one of several temporary extraction modes. Only one can be active at a time.

### Regulated output

Balanced default. Moderate yield, moderate depth growth, strong compatibility with safety actions.

### Maximum shifts

High output and faster projects. Raises labor strain, Depth, accident chance, and later Disturbance.

### Wartime requisition

Available during major resource shortage or war. Directs output to the state, uses military guards, and can tie the field to war production. It raises foreign pressure and makes the state a military target.

### Concession surge

The foreign partner provides machinery and specialists for a temporary boom. It increases the partner’s influence and makes unilateral suspension costly.

### Emergency suspension

Stops most extraction quickly. It lowers output, prevents new deep work, and begins a safety review. It is faster than closure but does not remove the deposit or settle the field permanently.

## Suspension

Suspension is a reversible state. It should:

- suppress most development actions
- reduce Developed Yield
- slowly lower Excavation Depth or prevent it from rising
- reduce ordinary accidents
- reduce Disturbance growth after Evolution II
- retain security and maintenance decisions
- retain contract and diplomatic consequences
- preserve the Event 018 resource ledger
- allow reopening after a minimum duration and review

A foreign concession partner can object to suspension. A wartime government can demand reopening. A field in an active border crisis can be suspended as part of a ceasefire.

## Closure project

Closure is a multi-step project whose complexity depends on the field’s stage.

### Baseline closure steps

1. Freeze new concessions and deep works.
2. Inventory the field and secure machinery.
3. Settle or break contracts.
4. relocate or compensate workers.
5. dismantle processing facilities where appropriate.
6. seal shafts, cap wells, flood galleries, or collapse access points.
7. remove every Event 018 resource addition from the state.
8. remove field decisions and modifiers.
9. mark the state permanently closed for Event 018.

The final step must verify the exact event-owned ledger and subtract only those amounts.

### Closure scaling

Closure becomes harder with:

- higher Developed Yield
- higher Excavation Depth
- more distinct resources
- more active contracts
- occupation or active combat
- lower Workforce Safety
- foreign concession ownership
- Evolution II or III danger
- public panic and evacuation pressure

Closure becomes easier with:

- prior controlled-demolition planning
- strong engineering capacity
- high safety
- suspension already active
- secured state control
- good transport for worker evacuation
- an international agreement that helps settle claims

### Closure outcomes

A complete success permanently ends the site. A partial closure can reduce depth, remove some development, and delay the crisis without removing all resources. A failed closure can damage infrastructure, kill workers, raise Foreign Pressure, or accelerate Breach Pressure during Evolution III.

The player must understand whether the action is a temporary suspension, partial seal, or final closure. These cannot share vague wording.

## Local state consequences

The field should visibly affect its state.

Positive consequences can include:

- infrastructure and rail growth
- processing or industrial buildings
- local construction speed
- employment and migration
- stronger supply importance
- garrison or security presence

Negative consequences can include:

- labor strain
- accident deaths
- sabotage
- bombing attraction
- smuggling
- housing pressure
- public panic in evolved stages
- local population loss

The field should not receive every consequence simultaneously. The administration posture and decisions determine which path develops.

## Dynamic scaling principles

Costs, durations, gains, and risks should react to the country and field.

Important factors include:

- state infrastructure
- country civilian and military industry
- current war state
- resource deficit
- stockpile and trade dependence
- stability and war support
- terrain and access
- Developed Yield
- Excavation Depth
- Workforce Safety
- Foreign Pressure
- number of active fields
- active concession partner
- occupation or contested control
- chaos tier
- evolution stage

A small country should be able to develop the field through time, foreign partnership, and focused investment. A large country should be able to develop faster, but its strategic extraction can attract more foreign attention and deepen the site more quickly.

## Value thresholds and feedback

Values should use meaningful bands rather than hidden breakpoints.

### Developed Yield bands

- Dormant
- Surveyed
- Operating
- Industrial
- Maximum Extraction

### Excavation Depth bands

- Surface Works
- Primary Shafts
- Deep Galleries
- Lower Strata
- Extreme Depth

### Workforce Safety bands

- Protected
- Managed
- Strained
- Dangerous
- Catastrophic

### Foreign Pressure bands

- Curiosity
- Commercial Interest
- Strategic Competition
- Coercive Pressure
- Crisis

These working labels describe information density. Final localisation can use resource-specific or regional wording.

Each threshold should change available decisions, event frequency, AI behavior, or risk. A value that only changes a tooltip has no reason to exist.

## Human and AI parity

Every meaningful human action needs an AI equivalent. AI does not need to use the selected-field buttons, but it should evaluate:

- whether the country needs the resource
- whether it can afford development
- whether foreign partnership is useful
- whether safety spending is justified
- whether to conceal casualties
- whether a field is defensible
- whether suspension or closure is safer
- whether concession or nationalization fits ideology and strength

AI should avoid opening maximum shifts in every field. It should use risk based on war pressure, resource deficit, government type, stability, safety, and evolution knowledge.

## Mechanic completion standard

The management system is complete when it supports multiple persistent fields, exact event-owned resource tracking, selected-field UI, dynamic values, phased decisions, state-level development, trade contracts, safety, security, suspension, final closure, ownership transfer, AI use, and clean removal. A decorative header with passive buttons is not sufficient.

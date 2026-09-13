# Decision and mission implementation prompt for Event 044 Yakub Returns

Use `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `AGENTS.md`.

Read spec parts 1 through 5, the outcome map, focus architecture, AI strategy matrix, probability scenarios, acceptance criteria, and asset prompt.

Implement the Event 44 decision and mission layer as a set of actor-specific categories. Do not put every action into one permanent category and do not introduce a full scripted GUI.

## Category structure

### American crisis category

Owner:

United States or accepted American host during the baseline domestic crisis.

Public state:

- Yakubite Influence as the one persistent public value
- current qualitative stage
- concise recent-cause or trend text
- Yakub's known status
- relevant chapter-state map highlights

Presentation:

One ordinary decision category with a static category picture and a compact meter or attached status display. Do not paint fake controls into the picture.

Phases:

- Phase I: observation and first policy
- Phase II: institutions and political settlement
- Phase III: sovereignty or suppression crisis

Expose three to five primary actions per phase, with six as the hard maximum. Keep one to three active missions visible.

Required action families from spec part 1:

- Map the chapters
- Place local informants
- Open municipal talks
- Emergency employment and housing program
- Permit monitored organization
- Prepare an arrest
- Audit movement finance
- Support independent community institutions
- Regulate schools and security groups
- Offer a legal separatist charter
- Convene a constitutional commission
- Decapitation operation
- Secure rail hubs and arsenals
- Federalize local security
- Protect municipal government
- Negotiate the territorial compact
- Launch a general suppression campaign
- Recognize the New Nation

Required missions:

- Establish the truth about Yakub
- Keep the federal corridor open
- Prevent a martyr crisis
- Complete the constitutional commission

Each action needs dynamic cost, target proof, cooldown, founder-state handling, AI intent, effect tooltip, and cleanup.

### New Nation state-building category

Owner:

The formed American Event 44 state.

Purpose:

Build administration, food systems, schools, economy, defense, recognition, and territorial integration. Replace the baseline movement crisis category for the new state's player.

Core action families:

- establish or upgrade institution families
- organize community defense
- integrate defectors
- secure depots
- invite volunteer cadres
- build the national arsenal
- demobilize emergency militias
- convene the founding convention
- seek recognition
- negotiate transit and trade
- integrate controlled or acceding states
- manage resistance and local compacts
- prepare North American New Nation formation
- prepare Diaspora Federation formation after Evolution III

Route focuses should unlock and transform these actions. Do not make the category a store.

### Foreign local crisis category

Owner:

Countries selected by Evolution II.

Purpose:

Manage one local movement through a region-specific module.

Public state:

Use qualitative local chapter status and a concise relationship to Yakubite doctrine. Do not expose another large numeric ledger unless the implemented local route has a proven need and stays inside the event-wide value budget.

Action families:

- intelligence and surveillance
- political inclusion and anti-discrimination reform
- rival movement support
- legal recognition
- local institutional regulation
- negotiation
- repression
- doctrinal rejection
- tactical cooperation
- autonomy or independence talks
- foreign-aid acceptance with dependency risk

Use country-specific localization, targets, costs, and AI. Do not copy the American category unchanged.

### International headquarters category

Owner:

The Yakubite International anchor.

Public state:

International Cohesion as the primary bloc value, current International form, member count by status, and current strategic objective. Domestic Influence should not remain an equal primary meter here.

Required actions:

- Call a congress
- Fund a member institution
- Send organizers
- Coordinate legal defense
- Open an aid corridor
- Dispatch volunteers
- Share intelligence
- Mediate a member dispute
- Discipline an abusive member
- Demand doctrinal conformity
- Propose federation
- manage member admission, suspension, exit, and associate status
- respond to schism
- prepare terminal commitment

The target-management flow should let the player inspect one selected member or foreign target at a time while AI evaluates all valid targets.

### Terminal command category

Prefer transforming the International category after world-end activation rather than creating a second oversized category.

Terminal actions include:

- coordinate uprisings with local proof
- move volunteers and equipment through valid routes
- establish regional commands
- demand accession
- negotiate submission or treaty support
- suppress or mediate member revolts according to route
- manage coalition fronts
- pursue route-specific victory objectives

Every terminal action must be bounded by equipment, manpower, industry, supply, route access, member capacity, or Cohesion. No free infinite uprising loop is allowed.

## Value rules

The American crisis exposes only Yakubite Influence as its persistent custom meter.

The International exposes International Cohesion as its main meter.

Institutional scores, chapter strength, faction strength, intelligence penetration, grievance, martyr risk, and regional suitability remain hidden, qualitative, or summarized.

Every public value needs a consistent label, icon, color identity, range, threshold, consequence, recent cause, and response.

## Costs

Use costs that fit the action. A decision may consume at most four spendable cost types.

Possible costs include:

- political power for law, negotiation, or bureaucracy
- command power for military security actions, kept within the project cap
- army XP for militia integration or doctrine work
- infantry and support equipment
- trucks, trains, convoys, or fuel
- manpower
- stability or war support
- consumer-goods or factory commitment
- intelligence exposure
- local legitimacy or institutional capacity
- International Cohesion
- tied-down divisions or state-control requirements
- time and deadline risk

Do not use political power as the only cost for most actions. Do not hide extra costs in effects or confirmation text. Every visible spendable cost needs the correct texticon.

## Missions and durations

Use goal-style missions when the player should act on the map or complete a condition.

Mission examples include:

- hold named rail hubs and the federal corridor
- keep supplied divisions in named states
- complete evidence collection before an arrest window expires
- protect a constitutional commission
- keep a relief corridor open
- prevent member war during a congress period
- secure member votes for federation
- maintain a terminal regional command

Use varied durations. Ordinary easy objectives should normally allow at least 90 days, medium objectives 120 to 180 days, and major constitutional or international projects longer where needed. Emergency missions may be shorter only when the narrative and map state justify it.

Every mission needs distinct success, failure, and useful partial-success behavior where relevant.

## AI

Implement the AI strategy matrix. AI should consider:

- current Influence or Cohesion stage
- founder state
- government ideology and civil-rights posture
- stability, war support, unemployment or depression pressure
- intelligence strength
- war losses and current fronts
- equipment, manpower, supply, and industry
- chapter institutions
- recognition and diplomatic risk
- local movement identity
- member relations and route form
- enemy strength and terminal viability

Complex or balance-sensitive decision weights require the probability audit workflow. Establish named baseline scenarios before patching, then compare the same scenarios after implementation.

## Cleanup and exploit control

Cleanup must cover:

- founder death, disappearance, detention, release, and discredit
- target annexation or invalidation
- chapter resolution
- state formation
- war end
- route change
- International formation and dissolution
- member exit or suspension
- schism
- world-end activation and defeat
- scenario setup and bypass removal

Prevent:

- repeated Influence farming
- repeated martyr farming
- free unit loops
- depot reward farming
- foreign-aid farming
- recognition farming
- repeated federation attempts without cost
- member-selection stale targets
- infinite terminal uprisings

## Validation and handoff

Create a decision and mission inventory with category, actor, phase, action ID, target, costs, duration, success, failure, AI, visibility, and cleanup.

Run the decision and mission auditor after implementation. Run the probability auditor for weighted action and target logic. Patch narrow findings, then compare the final state against the same named scenarios.

Do not call the decision system complete until every accepted action family has a real gameplay purpose, proper localization, correct icons, AI use, blocked text, cleanup, and exploit evidence.

# Event 029 decision and mission implementation prompt

Implement the complete decision and mission system for Chaos Redux Event 029, Riches Found.

Read repository `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the current Event 029 source, every file under `docs/specs/029_riches_found_specs/`, the relevant offline Paradox wiki pages, installed vanilla decision documentation, and current Chaos Redux decision precedents before editing.

Use `chaosx_decision_mission_auditor` with `fork_context=false` after implementation and before completion.

Route every complex AI weight and mission timing surface through `chaosx_ai_probability_auditor` using the named scenarios in `029_riches_found_ai_probability_scenarios.md`.

The accepted design uses one ordinary decision category with a static category picture.

Do not create a dedicated scripted GUI.

Do not add a whole-world daily, weekly, or monthly scan.

Do not simplify the decision system into political-power purchases or passive modifiers.

## Category behavior

Create one Event 029 controller category that appears while the country controls at least one active, damaged, closed, quarantined, partially sealed, or permanently sealed Event 029 mine with relevant aftermath.

Use the repository's current selected-target pattern when a country controls several mines.

The player sees one selected mine's actions at a time.

AI evaluates all valid mines directly.

The category header must show:

- selected mine state
- current operating condition
- Extraction Pressure
- Mine Development
- Local Order
- Revenue Legitimacy
- current policy profile
- one concise current objective or threshold

Show one primary value and three supporting values with consistent color, icon, threshold, and tooltip treatment.

Do not expose hidden capture, concession exposure, deep excavation, Gold Disease pressure, or supernatural pressure as raw values.

The category should normally expose three to five primary decisions and one to three missions in the current phase.

Six primary actions is the hard maximum.

Emergency actions replace obsolete ordinary actions.

## Cost contract

Every action can use at most four spendable cost types.

Use costs and requirements that match the action.

Possible costs include:

- civilian-factory burden
- political power for administration, contracts, and law
- command power for bounded military action
- army XP for military organization when justified
- manpower
- infantry equipment
- support equipment
- trucks
- trains
- convoys
- fuel
- stability
- war support
- reduced mine receipts
- temporary unit commitment

State control, route control, supplied divisions, ports, rail connection, legitimacy, order, or an active crisis are requirements and do not count as spendable costs.

Use compact icon-first cost localisation.

Every custom visible cost requires a valid texticon.

Use the same dynamic cost calculation for display, trigger, payment, refund where needed, and AI evaluation.

## Core decision families

Implement every accepted family below.

Final decision IDs and localisation must follow repository naming rules.

Working labels are direction, not finished localisation.

### Claims and access

Implement:

- Survey the Discovery
- Register Private Claims
- Freeze All Claims
- Recognize Local Claims
- Reserve the Deposit for the State
- Open an Emergency Claims Court

Requirements:

- policies create different starting order, legitimacy, development, and capture pressure
- claims court uses a mission or timed resolution
- state reserve slows opening development and strengthens state control
- local claims improve legitimacy and reduce central revenue
- private claims accelerate investment and increase fraud risk
- no policy is a clearly dominant reward choice

### Rush administration

Implement:

- Build a Camp Administration
- License Traders and Lodgings
- Recruit Local Labor First
- Import a Specialist Workforce
- Authorize Worker Cooperatives
- Establish Public Health and Sanitation

Requirements:

- actions change settlement incidents and visible values
- local and specialist labor routes differ
- public health uses physical and administrative costs
- cooperatives are unavailable under incompatible exclusive or purge routes
- camp administration is a real prerequisite for later civil actions

### Physical development

Implement geography-aware versions of:

- Build the Rail Spur
- Improve the Port and Convoy Route
- Drain and Reinforce the Shafts
- Expand Processing Works
- Build Worker Housing and Services
- Open a Development Fund
- Drive Deeper

Requirements:

- use exact map data and current repository helpers
- invalid rail or port actions remain hidden or disabled with precise blocked text
- permanent state-building rewards are one-time project or mission results
- Drive Deeper raises output ceiling, pressure, collapse risk, and later evolution likelihood
- safety projects reduce risk and temporarily reduce output
- development projects cannot duplicate after cancellation, transfer, destruction, or repair

### Revenue and governance

Implement:

- Pay a Citizens' Dividend
- Earmark Local Revenue
- Centralize Treasury Receipts
- Create a Stabilization Fund
- Audit the Shipment Ledger
- Replace the Mine Administration
- Tolerate Patronage
- Create an Independent Revenue Authority when repository scope supports the required staged administration

Requirements:

- revenue routes change immediate contribution, legitimacy, dependence, and later options
- a one-time dividend does not erase entrenched corruption
- stabilization reserve cannot be farmed
- audit uses mission state and can reveal, clear, or fail
- replacement administration carries transition cost and risk
- patronage provides short-term political value and long-term capture

### Concessions and foreign access

Implement:

- Auction a Limited Concession
- Grant an Exclusive Concession
- Sign an Offtake Agreement
- Trade Access for Infrastructure
- Require Beneficial-Owner Disclosure
- Publish the Contract
- Nationalize with Compensation
- Nationalize without Compensation
- Buy Out the Concession

Requirements:

- use a bounded selected-foreign-target flow
- one exclusive concession maximum per mine
- limited contracts require compatibility checks
- foreign actors need plausible access and interest
- hostile actors cannot sign cooperative contracts through a normal offer
- contract rewards, infrastructure, and payments cannot duplicate
- controller transfer re-evaluates one surviving contract
- disclosure and public terms change legitimacy and corruption risk
- nationalization routes have distinct cost, damage, foreign pressure, and AI logic

### Security and armed control

Implement:

- Form Mine Police
- Hire Private Guards
- Deploy an Army Cordon
- Arm the Workers
- Escort the Pay Train
- Clear the Claimant Barricades
- Negotiate a Mine Truce
- Disarm Private Forces

Requirements:

- civil, private, military, and worker security differ in order, legitimacy, cost, and autonomy
- army actions require supplied divisions or verified equivalent presence
- private guards can become a lasting political problem
- raids target a concrete route or asset
- killing and abuse call Deaths and Condemnation where applicable
- resolution hides obsolete actions and clears unit commitments

### Emergency and containment

Implement:

- Close the Mine Temporarily
- Quarantine the Mine District
- Replace the Workforce
- Seal the Deep Sections
- Restore Sabotaged Works
- Evacuate the Workforce
- Permanently Seal the Mine

Requirements:

- temporary closure ends positive output and reduces pressure through time or mission state
- reopening requires recovery and cannot erase crisis instantly
- quarantine is used only for Gold Disease or another accepted movement crisis and does not call biological systems
- workforce replacement can fail if source conditions remain
- partial sealing lowers output and deep risk
- evacuation reduces later deaths and takes time and transport
- permanent sealing ends ordinary reopening and preserves aftermath

### Supernatural response

Implement after Evolution III only:

- Seek Scientific Assistance
- Seek Religious Assistance
- Seek Occult Assistance
- Continue Controlled Exploitation
- Make an Agreement
- Close the Account
- Bind the Terms
- Pay in Material
- Spend Authority
- Accept Predatory Prosperity

Requirements:

- assistance routes use country context and existing valid systems
- scientific help cannot grant Event 016 progression or ownership
- religious text cannot invent claims about real faith
- agreement terms are visible and bounded
- no open-ended supernatural currency shop
- unrelated deaths cannot satisfy obligations
- permanent sealing and account closure are viable routes

## Mission family

Implement all missions with dynamic duration, real objectives, success, partial success where accepted, failure, cleanup, AI, and named state or route localisation.

### Secure the First Rush

Objective:

- establish administration
- keep the state controlled
- maintain order above the crisis floor
- resolve at least one active claims problem

Duration:

90 to 120 days after dynamic factors.

### Open the Railhead

Objective:

- complete a valid rail or port route
- keep required states controlled and supplied
- protect the project from sabotage

Duration:

120 to 180 days after geography and damage factors.

### Protect the Pay Train

Objective:

- hold named route states with supplied security
- prevent a robbery during real risk

Duration:

90 to 120 days.

### Break the Claim War

Objective:

- restore access through court, negotiation, or bounded clearing

Duration:

90 to 150 days.

### Restore the Shaft

Objective:

- complete drainage, reinforcement, and repair before deterioration becomes permanent

Duration:

120 to 240 days depending on damage.

### Hold the Mine During War

Objective:

- retain the mine state
- retain access route
- maintain supplied forces

Duration:

120 to 240 days or a valid war-state end condition.

### Complete the Public Settlement

Objective:

- maintain legitimacy and order
- complete a local project
- honor the revenue settlement

Duration:

180 to 365 days.

### Audit the Concession

Objective:

- preserve records
- protect auditors
- identify owners
- compare contract obligations with actual performance

Duration:

90 to 180 days.

## Mission quality rules

Do not use passive checklist missions.

A mission must require action after it starts.

Do not make the player click a second completion decision after meeting an objective that can auto-complete.

Use no more than three active missions per selected mine.

Prevent duplicate mission instances.

Loss of control, target invalidation, contract end, permanent sealing, or mine destruction must cancel or transform the mission safely.

## Controller transfer

All decisions and missions must call the shared Event 029 controller reconciliation.

On loss of control:

- cancel controller-owned missions
- remove temporary unit commitments
- close selected-mine actions
- remove old contribution
- clear invalid foreign target state
- preserve local mine values, development, damage, contracts, evolution, and operating condition

On new control:

- save the new controller
- rebuild the bounded contribution
- apply occupation and core factors
- open valid new decisions
- re-evaluate surviving contract

Do not duplicate the state or contribution.

## AI

Use the exact named scenarios in `029_riches_found_ai_probability_scenarios.md`.

The AI must:

- choose one coherent policy profile
- avoid rapid route oscillation
- value development according to geography
- prefer public settlement under stable democratic conditions
- prefer state and military extraction under authoritarian war conditions
- accept limited foreign finance when poor
- avoid exclusive concessions when strong and independent
- close or seal when crisis loss exceeds expected value
- almost never bargain under stable peaceful conditions
- bargain only under high chaos plus desperation, dependence, or accepted regime profile
- suppress invalid targets and actions

Run the baseline audit, apply the patch through the parent or owning agent, then run `hoi4.probability_compare` against the same scenarios.

## Clutter and lifecycle

The category should change as the mine develops.

Early actions disappear after settlement.

Basic development actions disappear after project completion.

Emergency actions appear only during their crisis.

Concession actions appear only with valid foreign actors and contract state.

Supernatural actions remain hidden until reveal.

Permanent sealing removes ordinary operating actions.

Do not solve clutter by creating many new categories.

## Tooltips and localisation

Use custom trigger tooltips for complex requirements.

Name exact selected states, route states, foreign actors, costs, and mission objectives.

Do not expose raw state IDs, raw triggers, hidden variables, random chances, future evolution conditions, or secret actors.

Gold Disease text must describe behavior and movement without claiming a virus.

Mass violence and forced entombment must show visible human consequences.

## Validation and audit handoff

The decision and mission auditor must return:

- files changed
- categories, decisions, missions, triggers, effects, constants, and localisation keys
- before and after behavior
- category phase map
- visible action counts per phase
- cost-type count for every action
- mission objective and duration table
- AI and probability evidence references
- controller-transfer and cleanup findings
- exploit findings
- remaining blockers

The parent must run the acceptance scenarios in `029_riches_found_acceptance_criteria.md` before claiming completion.

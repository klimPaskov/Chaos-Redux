# Decisions, missions, and failure recovery

## Decision design principles

Event 38 decisions represent military, political, logistical, territorial, religious, and diplomatic actions. They cannot become a store where political power buys small modifiers.

Each phase should show three to five primary actions, with six as the hard maximum. One to three missions can be active. Costs use no more than four spendable types per action.

Player-facing costs are icon-first. Complex requirements use concise summaries and named-state tooltips.

## Decision categories

The event should use a small number of long-lived categories:

1. **The Crusade Council** for order, authority, relic, and government actions
2. **Mediterranean Campaigns** for target selection, war preparation, ports, and settlements
3. **Crusader Principalities** for created subject obligations and disputes
4. **The Eleventh Crusade** only during failure recovery
5. **The Holy World** only during public terminal preparation and terminal war

Do not create one category per order or region. Target selectors and phased visibility keep the categories readable.

## Crusade Council actions

### Resolve the active order demand

**Visibility:** one active demand exists.

**Choices:** accept, negotiate, refuse, or defer once.

**Costs:** depend on the demand and can include equipment, command power, civilian factory burden, territory, order autonomy, or legitimacy.

**Result:** moves the three public values and the requesting order's hidden grievance.

**AI:** weighs war state, order route, current values, and ability to pay.

### Convene a joint command

**Purpose:** address low Cohesion or coordinate an offensive.

**Requirements:** at least two active orders and no recent failed conference.

**Costs:** command power, army experience, and temporary planning delay.

**Success:** raises Cohesion and creates a timed mixed-order command benefit.

**Failure:** exposes rivalry, lowers Authority, and can start an incident.

### Reassign a headquarters

**Purpose:** move an order's center to a valid controlled city.

**Requirements:** named eligible state, stable control, supply, and no active siege.

**Costs:** trains, support equipment, and civilian capacity.

**Consequences:** changes local unit recruitment, order influence, and regional stability.

### Arbitrate Jerusalem

**Purpose:** settle competing claims over sacred and administrative control.

**Requirements:** stable control of Jerusalem and at least one claimant.

**Outcomes:** central administration, order custody, principality custody, local church compact, or Papal administration.

**Consequences:** major Authority, Cohesion, and Legitimacy movement. This is not repeatable without a major constitutional change.

### Reform the Crusade Council

**Purpose:** enact the route settlement chosen by focuses.

**Requirements:** route focus, threshold proof, no active council rupture.

**Result:** transforms opening ideas, changes decision families, and may install a dominant order or confederation.

## Logistics actions

### Escort the Malta to Cyprus route

**Goal:** protect a named sea route for a timed period.

**Requirements:** convoys, escorts or naval presence, and valid ports.

**Costs:** fuel, convoys, and naval commitment.

**Success:** improves supply and Authority.

**Failure:** convoy losses, delayed reinforcements, and lower Authority.

### Repair the Holy Land rail corridor

**Goal:** control and repair named rail and supply nodes.

**Costs:** trains, support equipment, and civilian factory commitment.

**Duration:** 120 to 180 days depending on damage and war state.

**Success:** visible infrastructure improvement and lower future campaign costs.

### Build a fortified port

**Target:** one selected eligible coastal state.

**Costs:** civilian capacity, steel or equipment abstraction, and time.

**Result:** naval base, coastal defence, depot support, and order headquarters eligibility.

**Restriction:** no repeatable free port spam. Each region uses a bounded project ledger.

### Emergency air bridge

**Availability:** land and sea routes are blocked or severely disrupted.

**Costs:** transport aircraft, fuel, air command, and temporary equipment loss risk.

**Result:** limited supply relief and evacuation support.

### Requisition local transport

**Purpose:** short-term logistics at a legitimacy and local cooperation cost.

**Result:** temporary supply improvement, hidden local grievance, and possible migration pressure.

## Recruitment and equipment actions

### Raise a knight banner

**Requirements:** order capacity, manpower, complete equipment, and a valid training state.

**Costs:** equipment, manpower, army experience, and training time.

**Result:** one formation only after the mission completes. No instant free unit.

### Call foreign volunteers

**Requirements:** eligible sponsor, relations, route access, and no recent refusal.

**Costs:** diplomatic obligation, convoys, or sponsor influence.

**Result:** volunteer receipt, equipment, officers, or a capped expeditionary unit.

### Convert captured weapons

**Target:** selected stockpile family.

**Costs:** captured equipment, civilian or military factory burden, and time.

**Result:** crusader equipment according to a dynamic conversion rate.

### Establish a siege workshop

**Target:** valid industrial state.

**Costs:** steel, support equipment, civilian capacity, and construction time.

**Result:** siege equipment production capacity and regional recruitment.

### Create a remount service

**Costs:** manpower, local agricultural burden, equipment, and time.

**Result:** Mounted Knight sustainment and recovery.

## Campaign preparation actions

### Select the next regional objective

The human player selects one target region at a time. AI can evaluate all valid targets directly.

Target families:

- Jerusalem and Jordan restoration
- Levantine frontier
- Cyprus and Aegean
- southern Anatolia and Cilicia
- Greek mainland
- North African ports
- Rome under valid routes

Selecting a target activates only the relevant actions and missions.

### Survey the coast

**Purpose:** identify ports, naval risk, supply, and local allies.

**Costs:** naval or air experience, fuel, and intelligence capacity.

**Result:** improves invasion preparation and target information.

### Prepare the landing fleet

**Costs:** convoys, fuel, support equipment, and temporary dockyard burden.

**Result:** creates a time-limited invasion opportunity.

### Establish local contacts

**Costs:** political capital, equipment, and exposure risk.

**Result:** local support, intelligence, or a negotiated entry route.

### Demand passage or surrender

**Requirements:** sufficient Authority, credible force, and valid diplomacy.

**Outcome:** target can accept, bargain, refuse, or mobilize resistance.

### Launch the regional crusade

**Requirements:** completed preparation, supplied forces, valid target, and no duplicate war.

**Result:** limited war or intervention. It must not declare against every holder in one tick.

## Hold and secure missions

Examples:

### Hold Jerusalem for 120 days

Requires stable control and supply. Failure opens a local crisis and lowers legitimacy.

### Keep Malta connected for 150 days

Requires an active supply route and at least one usable bridge port.

### Guard the Jordan corridor

Requires supplied divisions in named states and functional rail or road access.

### Protect the Grand Harbour

Requires garrison strength, naval access, and air or anti-air readiness according to current threat.

### Break a named fortress line

Requires control of approach states and a Siege Host or equivalent support.

### Relieve a principality capital

Requires restoring supply or lifting a siege before the deadline.

Mission timers vary by difficulty. Ordinary missions should not be shorter than 90 days without a real emergency.

## Settlement actions

After victory, the player chooses a governance form for each eligible region.

### Direct commandery

**Benefit:** direct output and military access.

**Cost:** occupation burden, resistance, administration, and lower Cohesion if orders expected land.

### Grant to an order

**Benefit:** specialized unit and local administration.

**Cost:** order autonomy and rival grievances.

### Create a principality

**Benefit:** local recruitment, reduced direct occupation burden, subject contribution.

**Cost:** lower direct output and future succession risk.

### Restore a local Christian government

**Benefit:** legitimacy, local acceptance, diplomatic improvement.

**Cost:** reduced direct control and possible ideological divergence.

### Papal administration

**Benefit:** Sacred Legitimacy and Papal route support.

**Cost:** clerical control, local church disputes, and reduced political flexibility.

### Withdraw under treaty

**Benefit:** peace, lower condemnation, and possible Chaos reduction from a concrete settlement.

**Cost:** territorial ambition and Authority.

The settlement action freezes the selected region and owner facts before applying effects. It cannot be used twice on the same settlement generation.

## Relic actions

### Sponsor an expedition

**Requirements:** a valid claim location and no active relic expedition.

**Costs:** convoys, civilian capacity, equipment, or intelligence resources.

**Outcome:** find nothing, find a disputed object, recover a recognized tradition, expose a fraud, or trigger foreign competition.

### Submit a relic for examination

**Purpose:** improve public credibility at the risk of exposure.

### Transfer custody

**Targets:** selected order, Jerusalem, Malta, or Pope.

**Consequences:** order relations, legitimacy, foreign claims, and theft risk.

### Protect the pilgrimage route

A timed mission tied to real route control and security.

## Order incidents

Incidents occur when Cohesion is low, demands fail, or land distribution is badly skewed.

Possible incidents:

- refusal to reinforce another order
- seizure of a treasury
- rival appointments in Jerusalem
- disputed relic custody
- independent foreign negotiations
- a headquarters refuses central orders
- command duel or disciplinary crisis
- principality aligned with one order

Incidents offer bounded responses. They should not default to civil war. Severe repeated incidents can create a breakaway headquarters or leadership contest when the map and force package support it.

## Eleventh Crusade failure route

### Activation

The category activates when any accepted failure condition is met:

- Jerusalem and the Holy Land command are lost for a sustained period
- Malta controls fewer than the minimum expeditionary footholds
- the maritime bridge is lost and no alternative route exists
- Crusade Authority falls below the collapse threshold after a major defeat

It does not activate from a one-day occupation change.

### Recovery phases

#### Phase 1: Count the survivors

Visible actions:

- evacuate exposed formations
- rescue order headquarters
- consolidate equipment
- fortify Malta
- negotiate temporary refuge

Primary mission: preserve a minimum trained force and one viable port.

#### Phase 2: Rebuild the crusade

Visible actions:

- call foreign volunteers
- rebuild convoys
- reopen workshops
- select a new landing target
- reconcile the council

Primary mission: assemble a dynamic invasion package.

#### Phase 3: Launch the Eleventh Crusade

Visible actions:

- feint in one region
- secure local allies
- stage the fleet
- commit the knight banners
- launch the invasion

Primary mission: establish and hold a new foothold.

#### Phase 4: Settlement

Outcomes:

- restore Jerusalem
- establish an alternative principality
- negotiate a limited protectorate
- accept a fortified Malta ending
- dissolve the expedition into a humanitarian order state

### Failure of the comeback

A second failed crusade increases costs and can permanently close some aggressive routes. It should not create an infinite loop of free armies. A final negotiated or island-focused route remains available when possible.

## Holy World decisions

Preparation and terminal decisions are detailed in the terminal specification. The decision category must remain hidden until the route is publicly available.

## AI behavior

Decision AI evaluates:

- current phase and active mission
- supply and equipment
- value bands
- target strength and distance
- naval access
- order route
- sponsor availability
- resistance and local cooperation
- principality loyalty
- current war burden
- terminal or hidden-route state

AI must not launch an invasion without a viable route and supplied force. It must not create a principality without a valid country package. It must not spend scarce convoys on a low-value relic expedition during supply collapse.

## Exploit controls

Required controls include:

- one active regional target for human presentation
- one active relic expedition
- one major order demand
- region settlement generation flags
- escalating or dynamic unit-raising costs
- formation caps
- no equipment refund above remaining strength
- cooldowns after failed sponsor requests
- no repeated capital or port construction in the same slot
- no duplicate war creation
- cleanup after owner or target invalidation
- AI visibility separate from human target selection where needed

## Decision audit evidence

Completion requires:

- category lifecycle and phased visibility
- named-state tooltips
- icon-first costs with no more than four spendable types
- meaningful success and failure
- varied mission durations
- one to three active missions
- route-specific AI
- target cleanup
- save and reload persistence
- exploit audit
- probability audit for every weighted decision or target selection
- event-owned GUI helper alignment

# Event 029: Decisions, missions, and foreign interference

## Decision category structure

The event uses one controller-facing decision category.

Working category label: Riches Found.

The category opens when the country controls at least one active, closed, damaged, quarantined, or sealed Event 029 mine state.

The category closes when the country controls no Event 029 mine and has no surviving contract, compensation claim, or short aftermath action.

The category uses an ordinary decision list with a static category picture.

It does not require a dedicated scripted GUI.

The category header uses scripted localisation to show the selected mine state, its operating condition, the four visible values, the controller's current policy profile, and one concise current objective.

A country controlling one mine sees that state automatically.

A country controlling several mines uses one selected-mine decision flow.

The human player sees actions for one mine at a time.

The AI evaluates every valid mine through the same scripted effects and triggers without needing the player-facing selection step.

## Visible action budget

Each phase should normally show three to five primary decisions.

Six is the hard maximum.

The category should normally show one to three active missions.

Emergency actions replace ordinary actions while an urgent crisis is active.

Obsolete decisions are hidden after their contract, phase, target, controller, or crisis ends.

Basic decisions can be replaced by stronger variants after development or policy changes.

The decision category must not become a permanent list of every action described in this spec.

## Cost rules

A decision can use at most four spendable cost types.

Every cost must fit the action.

Political power is appropriate for law, contract, audit, revenue, and administrative actions.

Command power is appropriate for a bounded military deployment or command intervention, and it must remain conservative.

Physical work should use construction capacity, trains, trucks, support equipment, fuel, convoys, manpower, or equipment.

Security actions can use infantry equipment, support equipment, fuel, manpower, army XP, supplied divisions, and temporary unit commitment.

A requirement such as controlling a state, holding a rail route, fielding divisions, or meeting a legitimacy threshold is not a spendable cost.

Dynamic costs should respond to state population, development, damage, distance, war state, supply, local order, concession exposure, and previous failure.

The visible cost string must use the correct texticons and remain compact.

## Selected-mine flow

When the controller owns several mines, the category shows one selector decision for each valid mine only through the established selected-target pattern.

The selector displays the state name, operating condition, and crisis marker.

Selecting a mine hides the other mine-specific actions and opens the current mine's action set.

A close or return decision clears the selected mine.

Invalid selections clear automatically after loss of control, permanent destruction, release, annexation, or state transfer.

The decision that applies an effect and the tooltip that previews it must read the same selected-mine scope.

## Phase 1 decision family: claims and access

### Survey the Discovery

- Role: Establish the deposit profile, opening quality, workable area, and first access route.
- Availability: Immediately after discovery until the survey is completed or bypassed by an emergency concession.
- Requirements: Control of the mine state and basic access to it.
- Cost profile: Civilian-factory burden, manpower, trucks or trains when the state requires transport, and time.
- Immediate result: Raises Mine Development, improves the reliability of future output, and reveals the commodity profile.
- Risk: A rushed survey raises the chance of false claims, unsafe access, or concealed ownership.
- AI direction: Nearly universal priority unless the country is collapsing, the state is about to be lost, or a foreign emergency project is the only viable route.

### Register Private Claims

- Role: Create a legal claims system for prospectors and firms.
- Availability: Before the claim settlement is fixed.
- Requirements: Survey progress and minimum Local Order.
- Cost profile: Political power, administrative manpower, and a temporary civilian-factory burden.
- Immediate result: Faster opening development and more private investment.
- Long-term effect: Moderate concession exposure and bribery risk.
- Failure risk: Duplicate claims, claim jumping, and violence when order is weak.
- AI direction: Preferred by market-oriented states with adequate institutions and by weak states that need rapid private development.

### Freeze All Claims

- Role: Suspend private activity until the government creates a state regime.
- Availability: Early claims phase and after a major fraud exposure.
- Requirements: Sufficient control of the state.
- Cost profile: Political power, temporary stability pressure, and unit presence when the rush is already large.
- Immediate result: Lowers Extraction Pressure and reduces claim fraud.
- Long-term effect: Slower Mine Development and stronger state control.
- Failure risk: Clandestine digging and local resentment when the freeze lasts too long.
- AI direction: Preferred by centralized, communist, military, and high-capacity states.

### Recognize Local Claims

- Role: Give residents, customary holders, local institutions, or an existing community first access.
- Availability: Core, non-core, colonial, and indigenous-context variants where local claims exist.
- Requirements: No active violent eviction and a valid local settlement.
- Cost profile: Reduced national revenue share, political power, and administrative time.
- Immediate result: Raises Revenue Legitimacy and Local Order.
- Long-term effect: Slower central extraction and stronger local resistance to foreign concessions.
- AI direction: Preferred by democratic, reformist, localist, and legitimacy-focused governments.

### Reserve the Deposit for the State

- Role: Establish a state monopoly before private ownership becomes entrenched.
- Availability: Early claims phase or after nationalization.
- Requirements: Administrative capacity, state control, and no binding exclusive concession unless revoked.
- Cost profile: Political power, civilian-factory burden, manpower, and equipment for site administration.
- Immediate result: Increases state control and prepares the State Extraction policy.
- Long-term effect: Stronger potential national contribution and higher dependence risk.
- AI direction: Preferred by communist, fascist, military, and major-power governments with enough capacity to develop the site.

### Open an Emergency Claims Court

- Role: Resolve duplicate claims, violent disputes, fraudulent documents, and water or access rights.
- Availability: Claims crisis or low-order opening.
- Requirements: At least one unresolved claims incident.
- Cost profile: Political power, administrative manpower, and a time commitment.
- Immediate result: Starts a mission whose success depends on order, legitimacy, and non-interference.
- Failure result: Corrupt judgment, armed eviction, or a renewed claim war.
- AI direction: Preferred when the government has moderate institutions and wants to avoid military clearing.

## Phase 2 decision family: rush administration

### Build a Camp Administration

- Role: Establish basic government presence in the growing settlement.
- Availability: Rush phase until a permanent settlement administration exists.
- Requirements: Mine is open and controlled.
- Cost profile: Civilian-factory burden, manpower, support equipment, and time.
- Immediate result: Raises Local Order and unlocks sanitation, licensing, and policing actions.
- Long-term effect: Reduces incident frequency and improves project completion.
- AI direction: High priority for every stable controller.

### License Traders and Lodgings

- Role: Regulate housing, markets, transport services, and commercial entry.
- Availability: Active rush with settlement pressure.
- Requirements: Camp administration or an equivalent company administration.
- Cost profile: Political power and administrative manpower.
- Immediate result: Reduces price gouging, fire, and criminal incidents.
- Tradeoff: Slows the fastest private growth and can create bribery opportunities.
- AI direction: Preferred by orderly states, avoided by laissez-faire and desperate controllers when short-term growth is more important.

### Recruit Local Labor First

- Role: Give residents priority in mine and construction employment.
- Availability: Open mine with a local population.
- Requirements: No forced-labor policy and enough local workforce.
- Cost profile: Administrative effort, wage cost represented through reduced immediate mine contribution, and training time.
- Immediate result: Raises legitimacy and local support.
- Tradeoff: Slower specialist development.
- AI direction: Preferred in non-core states, democracies, and countries facing resistance.

### Import a Specialist Workforce

- Role: Bring engineers, miners, surveyors, and skilled operators from elsewhere.
- Availability: Deep reef, platinum seam, damaged works, or advanced development projects.
- Requirements: Safe access route and enough housing or company accommodation.
- Cost profile: Trains or convoys, civilian-factory burden, money represented through political or economic cost, and time.
- Immediate result: Raises Mine Development and project success.
- Risk: Local resentment, wage gaps, and Gold Disease movement through workforce rotation after Evolution II.
- AI direction: Preferred by industrial states and high-development strategies.

### Authorize Worker Cooperatives

- Role: Let organized workers hold claims, shares, or management seats.
- Availability: Open claims, local-claim route, or labor settlement.
- Requirements: No exclusive company monopoly and no active military purge.
- Cost profile: Reduced central revenue, political power, and administrative time.
- Immediate result: Raises legitimacy and can improve order.
- Long-term effect: Creates an armed or political worker constituency if security is later militarized.
- AI direction: Preferred by communist, socialist, democratic, and labor-friendly governments.

### Establish Public Health and Sanitation

- Role: Control ordinary disease, unsafe water, fires, and settlement crowding.
- Availability: Rush settlement with sufficient population.
- Requirements: Access and camp administration.
- Cost profile: Civilian-factory burden, manpower, trucks or trains, and support equipment.
- Immediate result: Reduces population-loss incidents and improves order.
- Long-term effect: Raises legitimacy and strengthens recovery from closure.
- AI direction: High priority for stable and high-capacity governments.

## Phase 3 decision family: physical development

### Build the Rail Spur

- Role: Connect the mine to the existing rail network.
- Availability: A valid land route exists and the mine lacks adequate rail access.
- Requirements: Proven map connection, state control, and no active route destruction.
- Cost profile: Civilian-factory burden, trains, steel or support-equipment proxy only if repository precedent supports it, and time.
- Immediate result: Starts the Open the Railhead mission.
- Success result: Strong Mine Development, better supply, and safer shipments.
- Failure result: Wasted construction, sabotage, or an incomplete route.
- AI direction: Strong priority for deep mines and inland sites.

### Improve the Port and Convoy Route

- Role: Give coastal or island mines a valid transport path.
- Availability: Coastal or island state where rail is not the main solution.
- Requirements: Controlled port or a valid port construction route.
- Cost profile: Civilian-factory burden, convoys, trucks, and time.
- Immediate result: Improves development, shipment reliability, and foreign access.
- Risk: Greater exposure to blockade and foreign concession pressure.
- AI direction: Used only when geography makes it valid.

### Drain and Reinforce the Shafts

- Role: Improve safety, depth access, and collapse resistance.
- Availability: Deep mine, damaged workings, high water risk, or pressure threshold.
- Requirements: Mine remains accessible.
- Cost profile: Civilian-factory burden, support equipment, manpower, and time.
- Immediate result: Raises development and sealed-depth integrity, and lowers collapse risk.
- Tradeoff: Temporarily reduces output.
- AI direction: High priority before aggressive deep mining and after a collapse warning.

### Expand Processing Works

- Role: Increase the share of value captured inside the state.
- Availability: Organized extraction or higher development.
- Requirements: Transport and power access.
- Cost profile: Civilian-factory burden, trucks, fuel, and time.
- Immediate result: Raises the mine's possible controller contribution.
- Risk: Raises foreign interest and makes sabotage more costly.
- AI direction: Preferred by industrial and state-extraction routes.

### Build Worker Housing and Services

- Role: Turn the temporary camp into a durable settlement.
- Availability: High rush pressure or organized extraction.
- Requirements: State control and construction capacity.
- Cost profile: Civilian-factory burden, manpower, trucks, and time.
- Immediate result: Raises legitimacy and order, and reduces housing and health incidents.
- Tradeoff: Lower immediate national contribution.
- AI direction: Preferred by public-development and long-term routes.

### Open a Development Fund

- Role: Earmark part of the mine's revenue for infrastructure and services.
- Availability: Stable receipts and a functioning ledger.
- Requirements: Minimum legitimacy or a reform decision after corruption.
- Cost profile: Reduced immediate mine contribution and political power.
- Immediate result: Unlocks repeated bounded state projects through missions. It grants no free building clicks.
- Risk: The fund becomes a corruption target under Evolution I.
- AI direction: Preferred by democracies and governments trying to contain dependence.

### Drive Deeper

- Role: Open lower workings and increase the high-value output ceiling.
- Availability: Mature development, working transport, and an open mine.
- Requirements: Pressure below the emergency ceiling unless a desperation route overrides it.
- Cost profile: Civilian-factory burden, support equipment, manpower, and temporary output loss.
- Immediate result: Raises development and future contribution potential.
- Risk: Strong Extraction Pressure, collapse risk, deep-excavation pressure, and later evolution likelihood.
- AI direction: Preferred by aggressive, wartime, concession, and desperate governments, avoided by low-capacity or crisis-ridden controllers.

## Phase 4 decision family: revenue and governance

### Pay a Citizens' Dividend

- Role: Distribute a broad share of receipts.
- Availability: Open mine with positive receipts and a functioning administration.
- Requirements: No emergency suspension and a valid beneficiary system.
- Cost profile: Reduced mine contribution and administrative capacity.
- Immediate result: Raises legitimacy and reduces hidden capture.
- Long-term effect: Weakens patronage and dependence.
- AI direction: Preferred by democratic and high-legitimacy governments with adequate finances.

### Earmark Local Revenue

- Role: Guarantee a defined share to the mine state or local authorities.
- Availability: Open mine, especially non-core or colonial state.
- Requirements: Local administration or agreement.
- Cost profile: Reduced national contribution and political effort.
- Immediate result: Raises legitimacy, compliance, order, and development.
- Risk: Local officials can capture the fund when oversight is weak.
- AI direction: Preferred when resistance, low legitimacy, or local unrest threatens output.

### Centralize Treasury Receipts

- Role: Route the mine's revenue directly to the national treasury.
- Availability: State-extraction or emergency government route.
- Requirements: State control and a functioning shipment route.
- Cost profile: Administrative effort and a local legitimacy loss.
- Immediate result: Raises short-term national contribution.
- Long-term effect: Raises dependence and Resource Curse pressure.
- AI direction: Preferred during war, financial crisis, authoritarian rule, or urgent rearmament.

### Create a Stabilization Fund

- Role: Save part of the windfall for closure, reconstruction, or economic diversification.
- Availability: Stable mine and functioning ledger.
- Requirements: Minimum order and legitimacy.
- Cost profile: Reduced immediate contribution and political power.
- Immediate result: Adds a bounded reserve that can pay for later repairs or soften dependence.
- Anti-exploit rule: The reserve cannot be withdrawn repeatedly for free rewards.
- AI direction: Preferred by stable long-term planners and high-capacity democracies.

### Audit the Shipment Ledger

- Role: Examine official output, prices, contractors, beneficial owners, and missing receipts.
- Availability: Suspicion, low legitimacy, concession, or periodic governance check.
- Requirements: Access to the mine and records.
- Cost profile: Political power, administrative manpower, and time.
- Immediate result: Starts an audit mission with outcomes based on institutions, hidden capture, and interference.
- Success result: Reveals theft or clears the administration, raises legitimacy, and enables prosecution or contract reform.
- Failure result: Records disappear, auditors are bribed, or the audit becomes a political purge.
- AI direction: Preferred by reformist and legitimacy-focused governments, avoided by entrenched patronage unless pressure is severe.

### Replace the Mine Administration

- Role: Remove a corrupt, failed, or captured local authority.
- Availability: Confirmed corruption, failed audit, low order, or controller transfer.
- Requirements: Sufficient national authority and a replacement capacity.
- Cost profile: Political power, administrative manpower, stability risk, and time.
- Immediate result: Reduces hidden capture and temporarily lowers development.
- Risk: Purge abuse, document destruction, and local power struggle.
- AI direction: Used when the existing administration is causing more loss than it prevents.

### Tolerate Patronage

- Role: Allow officials, officers, party bodies, or local bosses to retain part of the windfall in exchange for loyalty.
- Availability: Low stability, personalist government, or active political crisis.
- Requirements: Positive receipts.
- Cost profile: Reduced effective revenue and long-term corruption.
- Immediate result: Short-term order or political support.
- Long-term effect: Strong hidden capture and Resource Curse progression.
- AI direction: Preferred by personalist, weak authoritarian, and desperate governments.

## Phase 5 decision family: concessions and foreign access

### Auction a Limited Concession

- Role: Invite selected foreign actors to compete for a bounded contract.
- Availability: Survey complete and no incompatible monopoly.
- Requirements: At least one valid foreign actor and enough legitimacy to run an auction.
- Cost profile: Political power and administrative time.
- Immediate result: Selects a limited foreign partner, adds development finance, and raises modest concession exposure.
- Risk: Bid rigging, hidden ownership, and pressure for renewal.
- AI direction: Preferred by market-oriented and capital-poor states with adequate oversight.

### Grant an Exclusive Concession

- Role: Give one foreign actor dominant access in exchange for rapid development or emergency support.
- Availability: No existing exclusive concession and at least one valid foreign actor.
- Requirements: Government authority to sign and a selected partner.
- Cost profile: Sovereignty and revenue share represented through reduced future contribution, plus political power.
- Immediate result: Strong development, infrastructure, or security support.
- Long-term effect: High concession exposure, foreign leverage, private-security autonomy, and revocation cost.
- AI direction: Preferred by weak, isolated, or desperate states, avoided by strong majors and ideological anti-concession governments.

### Sign an Offtake Agreement

- Role: Promise a share of future output to a foreign government or company network.
- Availability: Open mine and valid foreign partner.
- Requirements: Shipment route and no incompatible contract.
- Cost profile: Reduced future flexibility and a share of output.
- Immediate result: Finance, equipment, transport, or diplomatic support.
- Risk: Contract pressure during closure, war, or controller change.
- AI direction: Preferred when the controller needs a specific physical or diplomatic benefit.

### Trade Access for Infrastructure

- Role: Exchange long-term access for rail, port, power, housing, or processing works.
- Availability: Low development and a valid foreign builder.
- Requirements: Defined infrastructure target and contract capacity.
- Cost profile: Future revenue share and political authority.
- Immediate result: Starts a foreign-built development mission.
- Failure result: Incomplete works, inflated cost, hidden clauses, or foreign security demand.
- AI direction: Preferred by infrastructure-poor states and island sites.

### Require Beneficial-Owner Disclosure

- Role: Screen the real owners behind bidders, contractors, and intermediaries.
- Availability: Before an auction, contract renewal, or after suspicious ownership evidence.
- Requirements: Administrative and legal capacity.
- Cost profile: Political power, time, and a possible delay to development.
- Immediate result: Reduces corruption and hidden capture, and can remove high-risk bidders.
- Tradeoff: Some foreign actors withdraw or demand weaker terms.
- AI direction: Preferred by reformist governments and states with strong institutions.

### Publish the Contract

- Role: Make the core fiscal, employment, security, and development terms public.
- Availability: New or existing contract.
- Requirements: Government willingness and contract records.
- Cost profile: Political effort and possible foreign-relations pressure.
- Immediate result: Raises legitimacy and improves later compliance checks.
- Risk: Exposes a bad contract and can trigger domestic opposition.
- AI direction: Preferred by democracies, reformists, and governments trying to contain the Resource Curse.

### Nationalize with Compensation

- Role: Bring a concession under state control while paying a negotiated settlement.
- Availability: Existing concession and enough resources.
- Requirements: State control, government authority, and no immediate military impossibility.
- Cost profile: Civilian-factory burden, political power, foreign-relations cost, and time.
- Immediate result: Reduces concession exposure and increases state control.
- Risk: Financial burden, sabotage, or dispute over valuation.
- AI direction: Preferred by major powers, left-wing states, and governments with high legitimacy.

### Nationalize without Compensation

- Role: Seize a concession immediately.
- Availability: Existing concession, crisis, war, exposed corruption, or ideological route.
- Requirements: Sufficient control and security.
- Cost profile: Stability or war-support risk, foreign-relations cost, command attention, and possible equipment commitment.
- Immediate result: Removes foreign control quickly.
- Risk: Sanctions, sabotage, intervention, capital flight, damaged works, and private-guard resistance.
- AI direction: Used by hostile, radical, wartime, or desperate governments when negotiation is unacceptable.

### Buy Out the Concession

- Role: End a contract through a negotiated purchase.
- Availability: Existing concession and functioning relations.
- Requirements: Sufficient economic capacity and no active seizure crisis.
- Cost profile: Civilian-factory burden, political power, and time.
- Immediate result: Clean transfer with limited legitimacy damage.
- AI direction: Preferred by wealthy governments seeking control without escalation.

## Phase 6 decision family: security and armed control

### Form Mine Police

- Role: Create a civil force focused on claims, transport, theft, and settlement order.
- Availability: Camp administration and an open or reopening mine.
- Requirements: Minimum legitimacy and administrative capacity.
- Cost profile: Manpower, infantry equipment, support equipment, and political power.
- Immediate result: Raises order and reduces crime and raid risk.
- Risk: Corruption when pay or oversight is weak.
- AI direction: Preferred by stable civilian governments.

### Hire Private Guards

- Role: Use a concession or contractor force for rapid site protection.
- Availability: Open mine, concession, or low government capacity.
- Requirements: Valid contractor and payment capacity.
- Cost profile: Reduced receipts, infantry equipment or foreign support, and political authority.
- Immediate result: Raises short-term order around the mine.
- Long-term effect: Raises private-security autonomy and legitimacy risk.
- AI direction: Preferred by concession states and weak governments under immediate threat.

### Deploy an Army Cordon

- Role: Place regular forces around the mine and its transport route.
- Availability: Raid crisis, war, low order, or strategic emergency.
- Requirements: Supplied divisions in the mine state or named route states.
- Cost profile: Command power, fuel, support equipment, and temporary unit commitment.
- Immediate result: Strong raid defense and order.
- Long-term effect: Lower legitimacy if maintained after the emergency.
- AI direction: Preferred by military governments, wartime controllers, and states facing armed seizure.

### Arm the Workers

- Role: Distribute weapons to organized workers or local defense committees.
- Availability: Worker participation route, weak state security, or raid crisis.
- Requirements: Sufficient worker organization and no active Gold Disease barricade.
- Cost profile: Infantry equipment, support equipment, political authority, and training time.
- Immediate result: Improves defense against raids and private guards.
- Risk: Creates an armed local power center and can intensify labor conflict.
- AI direction: Preferred by communist, worker-led, and desperate local-defense governments.

### Escort the Pay Train

- Role: Protect wages, official receipts, and high-value shipments.
- Availability: Valid rail or convoy route and active shipment threat.
- Requirements: Supplied units or security force along the route.
- Cost profile: Fuel, command power, unit commitment, and support equipment.
- Immediate result: Starts a timed escort mission.
- Success result: Raises order and legitimacy and prevents stolen receipts.
- Failure result: Pay robbery, mutiny, strike, or criminal expansion.
- AI direction: High priority when the mission is active and the route can be defended.

### Clear the Claimant Barricades

- Role: Remove armed claimants or gangs from the workings.
- Availability: Armed access crisis.
- Requirements: Adequate forces and a valid target within the mine state.
- Cost profile: Command power, manpower, infantry equipment, and stability risk.
- Immediate result: Starts a short military mission.
- Success result: Restores access with outcome based on restraint and legitimacy.
- Failure result: Casualties, mine damage, wider rebellion, or guard defection.
- AI direction: Used when negotiation fails or the mine is already closed by armed groups.

### Negotiate a Mine Truce

- Role: Suspend fighting among workers, claimants, guards, and authorities.
- Availability: Armed-control crisis without an irreconcilable massacre route.
- Requirements: At least one recognized counterpart and some legitimacy.
- Cost profile: Revenue share, political authority, and time.
- Immediate result: Lowers pressure and starts a settlement mission.
- Risk: Rival actors use the pause to entrench.
- AI direction: Preferred by weak governments, democracies, and controllers lacking forces.

### Disarm Private Forces

- Role: Remove company or syndicate weapons after the immediate threat passes.
- Availability: Private guards or armed claimants exist.
- Requirements: State control and enough regular security.
- Cost profile: Political power, unit commitment, stability risk, and possible compensation.
- Immediate result: Lowers private-security autonomy and raises sovereignty.
- Risk: Sabotage, contract dispute, or armed refusal.
- AI direction: Preferred when private forces threaten government control.

## Emergency decision family

### Close the Mine Temporarily

- Role: Stop extraction during collapse risk, disorder, disease, sabotage, investigation, or supernatural uncertainty.
- Availability: Open mine under a defined crisis.
- Requirements: Government can enforce closure.
- Cost profile: Loss of contribution, stability or worker-support burden, and security commitment.
- Immediate result: Sets temporary closure, lowers pressure, and opens recovery actions.
- Risk: Unemployment, smuggling, contract disputes, and maintenance decay.
- AI direction: Used when expected crisis losses exceed current output.

### Quarantine the Mine District

- Role: Restrict movement during Gold Disease or another defined internal contamination of behavior.
- Availability: Evolution II crisis only.
- Requirements: Control of access routes and enough security.
- Cost profile: Unit commitment, support equipment, trains or trucks, and stability risk.
- Immediate result: Reduces spread through workforce and shipments.
- Risk: Violence, shortages, smuggling, and legitimacy loss.
- AI direction: Preferred when disease pressure is high and the district can be isolated.

### Replace the Workforce

- Role: Remove affected teams and bring in new workers under controlled conditions.
- Availability: Gold Disease, severe mutiny, or entrenched criminal capture.
- Requirements: Alternative workforce and secure transport.
- Cost profile: Trains or convoys, manpower, civilian-factory burden, and time.
- Immediate result: Reduces immediate crisis pressure.
- Risk: The replacement force can become affected if extraction pressure remains high.
- AI direction: Used when closure is too costly and the source of disorder is concentrated.

### Seal the Deep Sections

- Role: Close the most dangerous workings while preserving safer extraction.
- Availability: Deep mine, collapse warning, Gold Disease source, or supernatural signs.
- Requirements: Control of shaft entrances and engineering capacity.
- Cost profile: Civilian-factory burden, support equipment, manpower, and time.
- Immediate result: Lowers pressure and deep-excavation risk, and reduces maximum output.
- Risk: Workers or guards resist when valuable material remains below.
- AI direction: Preferred by cautious and legitimacy-focused controllers before permanent closure.

### Restore Sabotaged Works

- Role: Repair transport, power, processing, drainage, or shaft damage.
- Availability: Damaged mine with no immediate uncontrolled fighting at the target.
- Requirements: State control and a valid repair target.
- Cost profile: Civilian-factory burden, trucks, support equipment, and time.
- Immediate result: Starts a repair mission.
- Failure result: Repeated sabotage, unsafe reopening, or wasted construction.
- AI direction: High priority when the mine's expected future contribution is meaningful.

### Evacuate the Workforce

- Role: Remove workers and nearby residents before permanent sealing or catastrophic collapse.
- Availability: Severe collapse or supernatural crisis.
- Requirements: Open transport route and enough time.
- Cost profile: Trains or convoys, trucks, manpower, and temporary construction burden.
- Immediate result: Reduces later civilian deaths and legitimacy loss.
- Tradeoff: Slows every other response and ends current output.
- AI direction: Preferred by high-legitimacy governments and any controller facing near-certain collapse.

### Permanently Seal the Mine

- Role: End extraction and close the site beyond ordinary reopening.
- Availability: Severe crisis, exhausted deposit, or accepted containment route.
- Requirements: Confirmed decision, control of entrances, and no active foreign or local force holding the workings.
- Cost profile: Construction capacity, support equipment, manpower, and permanent loss of output.
- Immediate result: Ends positive contribution and most mine incidents.
- Long-term effect: Leaves a permanent state identity and aftermath.
- AI direction: Rare, used only when survival, containment, or irreversible collapse outweighs the mine's value.

## Timed missions

### Secure the First Rush

- Start: Early rush after the claim policy is chosen.
- Duration band: 90 to 120 days depending on state size, infrastructure, and disorder.
- Objective: Maintain control, complete the camp administration, and keep Local Order above the crisis floor.
- Player actions: Build administration, resolve a claim incident, or place a supplied security presence.
- Success: Stronger opening settlement, reduced crime, and higher legitimacy.
- Partial success: Administration exists, but claim fraud or local resentment remains.
- Failure: Claim war, criminal capture, or armed eviction incident.

### Open the Railhead

- Start: Rail or port development project.
- Duration band: 120 to 180 days.
- Objective: Complete the valid transport connection while retaining control and supply.
- Player actions: Commit construction, trains or convoys, protect route states, and repair sabotage.
- Success: Major development and shipment reliability.
- Partial success: Route opens with low capacity or a foreign operator.
- Failure: Abandoned works, debt, sabotage, or route damage.

### Protect the Pay Train

- Start: Shipment threat, raid warning, or low-order transport route.
- Duration band: 90 to 120 days.
- Objective: Keep supplied divisions or security forces on the named route and avoid a successful robbery.
- Success: Higher order, worker confidence, and legitimate receipts.
- Failure: Stolen wages, strike, mutiny, criminal expansion, and lost revenue.

### Break the Claim War

- Start: Armed claimant conflict.
- Duration band: 90 to 150 days.
- Objective: Restore access through court settlement, negotiated truce, or controlled clearing.
- Success: Claims resolved and mine reopened.
- Partial success: One faction accepts while another becomes a long-term criminal or political actor.
- Failure: Mine damage, casualties, and local armed control.

### Restore the Shaft

- Start: Collapse, sabotage, flooding, or deep-section failure.
- Duration band: 120 to 240 days depending on damage.
- Objective: Complete drainage, reinforcement, and transport work before deterioration becomes permanent.
- Success: Development restored and collapse risk reduced.
- Partial success: Safer upper workings reopen while deeper sections remain sealed.
- Failure: Permanent development loss or catastrophic collapse.

### Hold the Mine During War

- Start: Enemy threat, front proximity, civil war, or active occupation attempt.
- Duration band: Based on war conditions, normally 120 to 240 days.
- Objective: Retain the mine state, its access route, and supplied forces.
- Success: Preserves receipts and raises national confidence.
- Partial success: State held but development damaged or contract leverage lost.
- Failure: Controller transfer or deliberate denial action.

### Complete the Public Settlement

- Start: Public-development route after basic administration and ledger exist.
- Duration band: 180 to 365 days.
- Objective: Maintain legitimacy and order while completing a local project and paying the agreed revenue share.
- Success: Durable managed-mine state and lower ordinary incident frequency.
- Failure: Public disappointment, patronage capture, or route collapse.

### Audit the Concession

- Start: Contract suspicion, renewal, or Resource Curse pressure.
- Duration band: 90 to 180 days.
- Objective: Preserve records, protect auditors, identify beneficial owners, and compare promised obligations with actual work.
- Success: Clean renewal, prosecution, buyout, or justified nationalization path.
- Partial success: Fiscal terms clarified but hidden influence remains.
- Failure: Record destruction, intimidation, political scandal, or foreign pressure.

## Foreign target management

Foreign concession and pressure decisions should not dump one row for every country into the main category.

The player selects one plausible foreign actor through a bounded target list.

The list is rebuilt from valid actors and ranked by interest.

The selected actor's available contract forms appear while that target is active.

The selection clears when the actor stops existing, relations make the contract impossible, the mine changes controller, the contract is signed, or the player closes the target view.

AI actors evaluate the full valid pool directly.

## Foreign-interest score

Foreign interest should use a dynamic score.

Positive factors include:

- major-power status
- high industry
- geographic proximity
- faction or alliance relationship
- good relations
- access to the mine through land, port, or convoy route
- strategic interest in the commodity profile
- controller weakness
- active invitation
- existing concession network
- wartime need
- rival power involvement

Negative factors include:

- no plausible access
- hostile ideology without a coercive route
- active war with the controller unless seizure or sabotage is intended
- existing exclusive concession by an ally
- severe mine crisis
- permanent closure
- low expected value
- sanctions or diplomatic isolation
- lack of convoys for an overseas project

The foreign actor should not enter merely because it is a major country.

## Foreign interference outside contracts

A foreign actor can interfere without a signed concession when it has strategic interest and a plausible route.

Possible actions include:

- fund a rival claimant
- bribe mine officials
- steal survey data
- recruit engineers
- sabotage transport
- support a local armed group
- expose a corrupt contract
- demand inspection rights
- threaten sanctions after nationalization
- prepare seizure during war
- recognize a local revenue claim
- offer emergency repair or security assistance

Interference should create evidence and attribution conditions.

It should not automatically reveal the actor when the operation remains covert.

The controller should receive counterplay through audit, counterintelligence, security, diplomacy, contract reform, or public exposure.

## Neighboring-country behavior

A neighboring country becomes more likely to pressure or raid the mine when:

- it has a border with the state
- relations are hostile
- the mine is weakly defended
- Local Order is low
- the controller is at war or in civil war
- the neighbor has a claim, core, or local proxy
- a foreign concession threatens the neighbor's interests
- the commodity profile has strategic value

A friendly neighbor can instead offer transport access, labor, policing cooperation, or a joint venture.

The event should not create a full war goal from a minor commercial dispute by default.

Seizure pressure can contribute to border incidents, justification weight, or war planning when the wider campaign supports it.

## Occupation behavior

An occupier sees a dedicated set of actions:

- reopen under military control
- requisition current output
- keep the previous administration
- replace the concession
- share revenue to lower resistance
- strip equipment and close the site
- deny the mine before retreat

Occupation output is reduced by resistance, low compliance, damaged transport, and non-core status.

Predatory occupation raises deaths, resistance, condemnation, and chaos when it uses forced labor, mass killing, or exposed coverups.

The mine should remain valuable enough to create a real tradeoff between immediate extraction and long-term control.

## Controller-loss cleanup

When a country loses the mine state:

- cancel its mine-specific missions
- remove its selected-mine state
- remove its contribution from the aggregate
- clear mine-specific unit commitments and temporary decisions
- preserve foreign compensation claims only when a valid contract creates them
- preserve national scandal or corruption aftermath when it no longer depends on control
- transfer the state identity and unresolved local crisis to the new controller
- clear invalid event targets and target flags

The old controller should not retain a positive mine modifier.

The new controller should not receive duplicate project rewards.

## Contract cleanup

A contract ends or changes through a defined outcome.

The system clears:

- selected foreign actor
- active negotiation mission
- temporary bid flags
- expired rights
- invalid security force state
- contract-specific decisions
- duplicate payment obligations

A contract that survives controller transfer must be represented once and renegotiated through one route.

## Decision exploit controls

The implementation must prevent:

- repeated free building grants
- repeated political-power extraction from one decision
- repeated contract signing with the same actor without ending the first contract
- cancel and re-sign loops that duplicate infrastructure
- nationalization compensation farming
- repeated audit rewards
- mine-selector duplication
- keeping old-controller benefits after conquest
- repeated reopening without paying recovery costs
- closure and reopening loops that erase pressure for free
- mission completion through passive conditions that were already satisfied before the mission began
- AI clicking an action whose target, route, cost, or crisis has become invalid

Use one-time project flags, mission state, dynamic costs, contract IDs, cooldowns, contribution-ledger reconciliation, and cleanup helpers.

## Decision writing direction

Decision titles should name a concrete action.

Descriptions should explain what the government, workers, company, army, or foreign actor will do.

Effect tooltips should show the visible immediate result, principal cost, operating-state change, and main risk.

They should not reveal hidden corruption rolls, Gold Disease entry, supernatural incidents, or future evolution thresholds.

Options involving mass violence, forced labor, or sealed workers should use severe in-world language and clear visible consequences.

They should not use cheap humor.

Ordinary claims, commercial absurdity, bureaucracy, and speculative excess can support restrained irony when it fits the actor and stakes.

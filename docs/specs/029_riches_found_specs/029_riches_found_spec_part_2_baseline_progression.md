# Event 029: Baseline progression

## Ordinary lifecycle

The baseline is a complete event system.

A campaign can receive the discovery, develop it, fight over it, settle its revenue, recover from ordinary crises, and reach a stable long-term operating state without unlocking any evolution.

Ordinary stages are not recorded as evolutions.

They progress through the mine's own state, decisions, missions, incidents, controller changes, and time.

The baseline lifecycle has five stored milestones and two overlays.

The milestones are discovery and claims, the rush, physical development, revenue settlement, and foreign concessions.

The mine stores only the highest milestone it has reached; it advances one step when the current milestone is complete and never moves back.

Armed protection and raids, and closure, collapse, or control crisis, are overlays worked out from current conditions on every refresh.

When an overlay ends, the mine returns to its milestone decisions, including any it had not yet taken.

The phases therefore overlap without losing progress: a mine can face a raid during development, receive a concession before full expansion, or fall into a claims dispute after conquest, and the player still sees one readable layer with a limited action set.

Implemented (agent decisions D20, D32, D38, D43): the layer order and per-layer action budget are owned by [Part 3](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md#decision-layers).

## Phase 1: Discovery and claims

### Situation

The first survey confirms that the material is real, accessible, and valuable enough to alter national politics.

Prospectors, landowners, workers, soldiers, merchants, local officials, and private investors begin staking claims before the government has decided how ownership works.

The state experiences sudden traffic, rising prices, improvised camps, disputed land, forged documents, and early violence.

### Opening policy and claims

The entry event's five options set the mine's lasting policy profile (Part 1); the claims decisions then decide who can claim access.

The claims approaches are:

- register private claims (faster development, more disorder and bribery);
- freeze all claims pending the state survey (lower pressure, slower development, clandestine digging);
- recognize local or customary claims (legitimacy and resistance to foreign capture, weaker central revenue);
- reserve the deposit for the state (strong national control, local resentment when residents are excluded);
- open an emergency claims court (a mission that settles disputes when order and legitimacy hold).

An emergency concession and a hands-off rush are not separate claims choices: the Concession Economy and Predatory Extraction openings already carry those directions, and a second copy would only add a button.

Implemented: the five opening options and the claims decisions; the dormant claims-policy constants `open_claims` to `minimal_interference` in `riches_found_policy` are never set and can be removed in a cleanup pass.

### Claims incidents

The baseline claims pool should include:

- a genuine rich strike inside a registered claim
- a fraudulent assay promoted by a speculator
- duplicate claim documents issued by different officials
- claim jumpers occupying a prepared shaft
- a landowner refusing access to a discovered seam
- a local community demanding recognition before work begins
- prospectors crossing a colonial or administrative boundary
- soldiers staking claims while assigned to guard the site
- foreign nationals presenting old contracts or exploration rights
- a local court accepting bribes
- a miners' assembly creating its own rules
- a violent eviction
- a disputed water, road, or rail easement
- a rush toward a false secondary discovery
- a valuable specimen disappearing from the survey office

Each incident should respond to current policy and values.

A registered claim system reduces duplicate claims but creates bribery opportunities.

A state reserve reduces claim jumping and increases clandestine digging.

Local-recognition policy reduces dispossession and can create disputes between local authorities.

A concession moves many disputes into the company contract and raises hidden ownership risks.

### Phase objectives

The player should be able to complete at least one active objective:

- establish an enforceable claim register
- complete the state survey
- hold the mine district with supplied units while claims are resolved
- open a temporary court or arbitration body
- secure the main access route

Success moves the mine into the rush with stronger Local Order.

Failure does not cancel the event.

It starts the rush with competing claims, higher violence, and a larger chance of private seizure.

## Phase 2: The rush

### Situation

The mine district becomes a fast-growing settlement.

Workers and prospectors arrive from other states and countries.

Merchants, lenders, gambling houses, transport firms, labor recruiters, brothels, religious groups, newspapers, criminal networks, and political organizers follow them.

The local population gains employment and business opportunities while housing, food, water, health services, policing, and transport come under pressure.

### Rush composition

The rush population is represented through incidents and modifier effects.
No separate population pool is needed.

Its character depends on:

- deposit profile
- core or non-core status
- local population
- state infrastructure
- recipient ideology
- war state
- neighboring unemployment or instability
- foreign access
- claim policy
- current order and legitimacy

An alluvial field produces more transient prospectors and traders.

A deep reef produces more engineers, contractors, and organized labor.

A gemstone field produces more smugglers, brokers, and concealed trade.

A platinum seam produces more state officials, industrial missions, and foreign supply delegations.

### Rush management approaches

The controller can build a camp administration, license traders and lodgings, recruit local labour first, import a specialist workforce, authorize worker cooperatives, and establish public health and sanitation.

Company housing is the Worker Housing project under a concession, and tolerating informal growth is simply not acting, so neither needs its own decision.

Costs follow [the Part 3 cost rules](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md#cost-rules).

### Rush benefits

A managed rush can improve:

- infrastructure
- building slots
- local construction speed
- local supply
- civilian factories or construction capacity where physically justified
- workforce availability
- mine development
- local order
- revenue legitimacy

The strongest permanent improvements require missions or timed projects.

A click should not grant repeated free factories or infrastructure.

### Rush pressures

An unmanaged rush can create:

- housing inflation
- food shortages
- strained local services
- disease and sanitation incidents that remain ordinary public-health events
- fires
- theft
- labor exploitation
- forced displacement
- wage disputes
- gambling debt
- violent gangs
- price gouging
- local resentment toward outsiders
- corruption among police and customs officials
- smuggling routes
- uncontrolled building sprawl

These effects should create active problems and decisions.

They should not become a stack of tiny decorative penalties.

Proposed (unresolved): food shortage is the one rush pressure that matters beyond the district.
While a mine in the rush milestone has no camp administration, or runs under Predatory Extraction, it submits one bounded unmet-need component for the mine state through the famine system's owner-proven adapter (`docs/systems/famine_system.md`, Adapters), and the component ends when the administration stands or the policy changes.
Alone it stays below supply strain, so it only matters when war, blockade, or a disaster already press the state, which is exactly when an unmanaged rush should hurt.
It gives Camp Administration and Sanitation a visible consequence without a new meter, and it adds no famine decision, popup, or scan to Event 029.

### Settlement outcomes

The rush matures into the settlement its policy profile and state-modifier stage describe: a public mining town, a state industrial district, a concession company town, a militarized extraction zone, or a loosely governed boom settlement.

There is no separate settlement-profile value; the policy profile already changes incident weights and which later decisions are strongest, and the controller can change direction through its revenue, security, and concession choices.

## Phase 3: Physical development

### Development principle

Mine Development represents a real physical system.

It rises through projects that can fail, be sabotaged, or be destroyed.

Development is not a passive monthly number gained from the initial discovery.

### Development projects

| Project | Lasting physical result | When it appears |
| --- | --- | --- |
| Rail Spur, then Open the Railhead | One infrastructure level; on success, one railway level from the mine to the controller's capital where `can_build_railway` allows it | Inland mine without a route |
| Port Route | One naval base level on the coast | Only where rail cannot serve: islands and railless coasts |
| Shaft Reinforcement | Lower collapse risk and stronger sealed depths | Any route-served mine; deep veins need it most |
| Processing Works | Higher output ceiling | Organized extraction with a route |
| Worker Housing | Higher order and legitimacy, output held back | Rush settlement or later |
| Sanitation | Fewer health and settlement incidents | After camp administration |
| Development Fund | Earmarked revenue for works and services | Stable receipts |
| Drive Deeper | Higher output ceiling, more pressure and deep excavation | Industrial band, steady order, a working route |
| Repair, then Restore the Shaft | Clears damage, route damage, and severe collapse | Any damaged mine |

Drainage, ventilation, washing works, power, storage, the assay office, explosives magazines, tailings, clinics, markets, fire brigades, courts, police posts, treasury offices, customs posts, and dividend registries are the narrative content of these projects and their reports, not separate decisions.

Every lasting building or infrastructure result is a one-time project identity that cancellation, transfer, or recapture cannot reset; destroyed buildings are repaired through ordinary construction and Restore the Shaft, never re-granted.

Costs follow [the Part 3 cost rules](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md#cost-rules); the construction projects commit civilian factories while they run instead of spending political power.

Implemented (D11, D29, R11), including the AI rule that a mine builds one project at a time.

### Development risk

Faster development raises Extraction Pressure.

Safety and reinforcement reduce collapse risk but consume time and construction capacity.

Foreign finance can accelerate development at the cost of concession exposure.

Military labor can accelerate development at the cost of legitimacy and order.

Worker cooperatives can raise legitimacy and local support while slowing central control.

A weak state may need to choose between rapid foreign-built capacity and slow domestic development.

### Development bands

Mine Development is shown as a band, which is all the player needs to plan:

| Band | Development | What changes |
| --- | --- | --- |
| Provisional workings | below 35 | Reduced output; Trade Access for Infrastructure is attractive |
| Organized extraction | 35 to 64 | Normal operation; processing and housing become worthwhile |
| Industrial mine district | 65 to 79 | Drive Deeper opens; foreign interest rises |
| Mature extraction complex | 80 and above | Public Fortune's hold period can start; collapse and evolution stakes are highest |

The thresholds are `riches_found_threshold.minimum_operating_development`, `riches_found_decision_threshold.development_high`, and `riches_found_threshold.mature_development`.

High development unlocks stronger extraction and stronger consequences; it never raises every positive modifier without limit.

## Phase 4: Revenue settlement

### Purpose

The controller decides how the windfall enters the state and national economy.

This choice is the main ordinary defense against the Resource Curse.

### Revenue routes

#### Citizens' dividend

A broad share of revenue is distributed to the population.

This raises legitimacy and reduces patronage pressure.

It gives less direct construction capacity and less concentrated state output.

The dividend can be national, local, or split.

The route should cost administrative capacity and reduce the mine's immediate controller contribution.

#### Local development settlement

A defined share funds the mine state and nearby infrastructure.

This raises development, order, and legitimacy.

It creates less immediate national political power.

It is especially effective in non-core or colonial states.

The route can reduce resistance when paired with real local representation.

#### Central treasury monopoly

The national government captures most revenue.

This provides the strongest immediate political and construction benefit.

It raises dependence, corruption pressure, and local resentment when oversight is weak.

It is attractive during war or national emergency.

#### Stabilization or future fund

A share of revenue is withheld from current spending.

This gives weaker immediate bonuses and a stronger long-term protection against dependence, price shock, closure, and reconstruction costs.

The fund builds one reserve that pays one later bill (a repair's stockpile cost or one closure's idle crews) and is then spent; only a new fund builds another, so it cannot be farmed.

#### Worker or community participation

Workers and local institutions receive a formal share through worker cooperatives (rush) and the local revenue share.

This improves legitimacy and order, and it can lower central control.

It creates political consequences under authoritarian and colonial governments.

#### Patronage distribution

Revenue is routed through favored officials, officers, party organizations, local bosses, or elite families.

This buys short-term order and political loyalty.

It raises hidden capture and makes later reform harder.

#### How the routes work in play

The chosen settlement is a standing route, not a one-time payment.

Central receipts add 20 percent output; a dividend, a local share, a fund, worker housing, or a workers' share hold some output back; patronage leaks output; the route factor stays between 0.6 and 1.25 (`riches_found_revenue_route`).

Each controller pulse the route drifts the mine: unwatched central receipts and patronage grow illicit capture, while a dividend or a local share raise order and lower capture until capture reaches its gate, so one payment cannot erase entrenched corruption.

Central receipts also raise treasury dependence, which drives the Resource-Dependent Treasury stage.

Implemented (D35, D46).

### Revenue legitimacy incidents

Baseline incidents include:

- an audit finds missing shipments
- local officials demand a fixed share
- a national ministry changes the royalty formula
- workers strike over bonuses
- a public dividend list contains false names
- a development fund builds visible infrastructure
- a central fund is diverted to unrelated military spending
- local leaders accuse the government of theft
- a treasury official disappears
- the assay office reports substitution or undercounting
- a political party builds a machine around mine revenue
- local businesses grow dependent on mine payroll
- agricultural or ordinary industrial activity loses workers to the mine

The last point supports economic dependence without requiring a full macroeconomic simulation.

### Mature settlement

A mine with high legitimacy, high order, and moderate pressure can reach a managed settlement.

This creates the most reliable long-term contribution.

It does not produce the highest immediate output.

A mine with low legitimacy and high pressure can reach an extractive settlement.

This creates stronger short-term rewards and more frequent crises.

## Phase 5: Foreign concessions

### Foreign interest

Foreign governments and companies can seek access after the discovery becomes public or after the controller invites investment.

The event should select plausible foreign actors through dynamic factors:

- geographic proximity
- major-power status
- faction relationship
- trade access
- ideology
- existing relations
- industrial capacity
- war state
- strategic interest in the deposit profile
- naval access for overseas sites
- hostility or rivalry with the controller
- prior concessions

The actor is a government scope even when the narrative interest is a company.

No new company country tag is required.

Implemented (D33, D36): the mine keeps a ranked list of at most four interested governments, rebuilt only at discovery and after deliberate actions; the offer goes to the most interested, and a human controller can court any other listed government through Court a Partner.
At war, hostile (opinion below -25), excluded, and capitulated actors are never listed.
Pending: the distant naval-power route (`RF_FOREIGN_02_DISTANT_NAVAL_POWER`) still needs a convoy and port access test.

### Concession forms

#### Limited concession

A foreign actor receives a bounded share, term, or project.

The controller gains development and a temporary finance benefit.

Concession exposure rises modestly.

The contract can be renewed, bought out, or allowed to expire.

#### Exclusive concession

One foreign actor receives dominant access.

Development rises quickly.

The controller receives a strong immediate benefit and accepts higher foreign leverage, private-security pressure, and hidden ownership risk.

Revoking the contract becomes expensive and can trigger sanctions, sabotage, or intervention.

#### Offtake agreement

The controller keeps formal ownership and promises future output to a foreign actor.

The agreement improves finance, transport, or industrial support.

It can reduce freedom to close the mine or redirect revenue.

#### Infrastructure-for-access agreement

A foreign actor builds rail, port, roads, power, or processing works in exchange for long-term access.

This provides visible development and creates a durable leverage relationship.

It is offered only below the industrial development band, so it never competes with Drive Deeper.

#### Forms folded into other actions

A foreign security contract is Hire Private Guards under a running concession, and a joint public venture is a limited concession with beneficial-owner disclosure and a published contract.
Separate contract types would repeat those choices with new names, so the four contract types are limited concession, exclusive concession, offtake, and infrastructure access (`riches_found_contract_type`).

Signing gives the partner one bounded Mine Concession Share modifier however many contracts it holds, and both governments a contract opinion pair; buyouts and compensated nationalization pay the partner, while uncompensated nationalization leaves a lasting grievance that makes the sponsor the preferred interference actor (D13, R6).

### Contract visibility

The player should know the public terms and visible consequences.

Hidden owners, kickbacks, or conflicts of interest remain incident material until an audit or exposure event reveals them.

Contract transparency, beneficial-owner checks, and public auctions reduce corruption pressure.

Secret awards and emergency wartime contracts raise it.

### Foreign actor choices

A foreign actor can:

- accept the offered terms
- demand a larger share
- offer infrastructure instead of cash
- request security rights
- seek exclusive access
- use a local intermediary
- withdraw
- secretly support a rival claimant
- pressure the controller after a contract breach

The AI must evaluate the mine's value, distance, relations, risk, and existing exposure.

It should not pursue every mine in the world.

### Contract end states

Contracts can:

- expire normally
- be renewed
- be bought out
- be nationalized with compensation
- be nationalized without compensation
- survive a controller change
- be suspended during war
- be voided by collapse or permanent sealing
- be exposed as corrupt
- become the basis for foreign pressure or intervention

A controller change should re-evaluate the contract.
It must not erase or duplicate the contract automatically.

## Phase 6: Armed protection and raids

### Security problem

The mine contains portable wealth, payrolls, explosives, transport chokepoints, and politically valuable contracts.

Ordinary armed competition is part of the baseline.

It can occur before any evolution.

### Security approaches

#### Mine police

A dedicated civil force protects claims, transport, and the settlement.

It is slower to build and strongest when legitimacy is high.

It has lower atrocity risk than military or private control.

#### Private guards

A company or concession employs armed guards.

This can improve order quickly around the mine and worsen community relations, labor conflict, and sovereignty.

Guard loyalty follows pay, concession control, and leadership.

#### Army cordon

The controller deploys regular forces to the state.

This is effective during raids or war.

It consumes command attention, supply, equipment, and divisions.

Long-term military control lowers legitimacy unless paired with a public settlement.

#### Armed workers

Workers or cooperatives receive weapons and organize mine defense.

This can protect against raiders and private guards.

It creates an armed political constituency and raises the risk of a local power struggle.

A mine keeps one standing force at a time; a mixed security board is not a separate approach, because Recognize the Board in The Gilded Sovereignty already covers shared local authority where it matters.

### Raid actors

Possible raid or sabotage actors include:

- local criminal groups
- rival claim syndicates
- private guards acting without authority
- foreign agents
- hostile neighboring countries
- resistance movements in occupied or colonial states
- retreating forces
- corrupt army units
- smugglers
- workers barricading the site during a labor dispute

A raid does not always mean a full military battle.

It can target the assay office, payroll, train, bridge, power supply, storage compound, concession records, or shaft entrance.

### Raid escalation

Raid severity depends on:

- low local order
- low legitimacy
- high development
- high pressure
- border proximity
- war state
- foreign concession exposure
- resistance
- security policy
- number and supply of divisions in the state
- previous successful raids

The system should choose a concrete target and consequence.

It should not apply generic random damage without context.

### Raid consequences

Possible consequences include:

- stolen revenue
- damaged infrastructure
- reduced development
- temporary closure
- destroyed transport
- guard casualties
- civilian deaths
- exposed foreign interference
- concession crisis
- increased resistance
- loss of order
- higher pressure through emergency extraction
- a chance for another country to seize control during war

Deaths caused by raids, massacres, and collapse should use the shared Deaths system.

Public atrocities and coverups should use the shared Condemnation system.

### Armed control crisis

A severe baseline crisis occurs when a guard force, worker militia, corrupt army unit, or claimant syndicate controls access more effectively than the government.

The mine remains inside the state.

No new country tag is created by default.

The controller must choose among negotiation, pay settlement, military clearing, recognition of a local board, contract transfer, or temporary closure.

Failure can suspend the mine's contribution and damage state control.

If the state changes controller through normal war or civil war, the persistent mine transfers through the controller contract.

## Phase 7: Consolidation, closure, and control crisis

### Managed consolidation

A well-managed mine can reach a durable ordinary settlement.

Requirements should include:

- strong development
- manageable pressure
- adequate order
- adequate legitimacy
- resolved claim system
- functioning transport
- no unresolved armed-control crisis

The reward is reliability, lower incident frequency, and a stable bounded contribution.

The mine remains vulnerable to war, conquest, sabotage, and later evolutions.

### Extractive consolidation

A mine can also stabilize under state force, a concession, or private control.

This produces higher pressure and lower legitimacy.

It remains productive and more likely to enter corruption or armed crises.

It is a valid route, not an automatic failure.

### Temporary closure

The controller can suspend extraction for a defined period.

Temporary closure:

- removes ordinary positive contribution
- lowers pressure
- allows repairs and investigation
- weakens local employment and payroll
- can improve order if the closure is enforceable
- can lower legitimacy if workers receive no support
- can trigger foreign-contract disputes

Reopening requires a safety, order, or contract check.

The mine should not reopen automatically into the exact condition that caused closure.

Implemented (D5, R1, R2): every closing action uses one closure helper; the maintenance pulse lowers pressure and collapse pressure until the review date, and legitimacy slips unless the crews hold a standing share or were paid within the revenue cycle.
Reopen the Mine is a paid inspection that needs pressure below the reopening ceiling, a route, and adequate order or a security force, and a 180-day cooldown blocks closure loops.

### Partial sealing

The controller can seal deeper sections while leaving safer workings open.

This reduces maximum output and deep-excavation risk.

It preserves part of the mine's value.

It becomes a central response during Gold Disease and Demons Beneath the Mine.

### Permanent sealing

Permanent sealing ends positive output and prevents ordinary reopening.

It should require a confirmed decision, clear consequences, and a strong visible reason.

The state keeps a permanent historical modifier.

Later events should not silently reopen the site without an explicit accepted route.

### Ordinary collapse

A mine can collapse without supernatural involvement.

Risk rises through:

- high pressure
- low development in reinforcement and drainage
- sabotage
- fighting
- rapid deepening
- temporary closure without maintenance
- earthquake or relevant natural disaster
- Gold Disease barricades and unsafe digging

A collapse can be minor, severe, or catastrophic.

Minor collapse damages development and causes bounded deaths.

Severe collapse closes the mine and damages state infrastructure.

Catastrophic collapse can permanently destroy the workings after a major population loss and building damage.

Event 029 owns the collapse effect and applies exact state damage through its own bounded helpers (implemented, `riches_found_collapse_mine`).

Event 013 Natural Disasters is not called for ordinary collapses; a later adapter may call its public exact-state API only when a real earthquake or landslide is the physical cause and every required proof exists.

A mine in a state struck by an Event 013 earthquake should take a collapse-pressure increase from that disaster's existing state report rather than a second disaster roll (proposed, unresolved).

### Exhaustion

Ordinary exhaustion should be rare because the event premise is a vast source of wealth.

It can occur through a defined predatory-extraction endpoint, catastrophic failure, or long-term balancing rule.

It should not occur through an invisible random timer that removes the player's investment.

Accepted design (user approval 2026-10-18): exhaustion has two endpoints, both through actions and failures the player can see.
Cumulative Deep Excavation is the extraction counter: each Drive Deeper project adds `riches_found_action_delta.positive_15`, Seal the Deep Sections removes `negative_12`, and the ceiling is `riches_found_event.public_value_maximum`.
A mine run under a predatory profile (Predatory Extraction or open claims) exhausts when its Deep Excavation reaches `riches_found_exhaustion.deep_excavation_predatory`, five full projects.
Every other mine exhausts only at `riches_found_exhaustion.deep_excavation_ordinary`, the ceiling at which Drive Deeper stops being offered.
The Drive Deeper tooltip states both depths and warns when the project it starts would end the deposit.
`riches_found_review_deposit_exhaustion` runs when a Drive Deeper project lands and during the controller pulse, and `riches_found_exhaust_mine` closes the mine for good and sends the controller one report, `chaosx.nr29.50`.
A catastrophic collapse that leaves the sealed workings with no integrity (`riches_found_exhaustion.catastrophic_integrity_floor`) destroys them beyond recovery through the same helper, and a collapsed mine is accepted by it.
An exhausted mine cannot be repaired or reopened, and the ordinary Permanent Seal remains available for it.
The AI never drives a non-predatory mine into exhaustion and takes the last predatory project at half weight.

### Recovery

A damaged or closed mine can recover through:

- shaft repair
- drainage
- transport reconstruction
- workforce settlement
- guard reform
- contract renegotiation
- audit and revenue settlement
- local relief
- controlled reopening

Recovery should preserve the history of earlier choices.

A captured or corrupt mine should not reset to a clean state because the player clicked repair.

## Controller-change variants

### Conquest

An invader who occupies the state receives reduced output until control is consolidated.

Resistance, non-core status, damaged transport, and contract disputes reduce value.

The occupier can exploit, negotiate, close, or restore the mine.

Predatory occupation raises legitimacy and condemnation risks.

Implemented (D10, D24, D34): the occupier's set is reopen, requisition output, keep the previous administration, replace the concession, share revenue, strip equipment, and deny the mine before retreat; sharing revenue lowers resistance, keeping the administration raises compliance, and requisition or stripping raise resistance, which feeds the occupied output factor.
The hostile capture itself already sends war refugees through the shared humanitarian capture adapter, so Event 029 adds no flight of its own.

### Civil war

The mine becomes a strategic objective.

Each side can receive a temporary mission to hold the state, protect the transport route, or deny the mine to the enemy.

The mine contribution belongs to the actual controller and must never be counted for both sides.

### Annexation

The annexing country inherits the physical site and unresolved contracts.

The previous controller loses its aggregate contribution.

Foreign actors can recognize, renegotiate, or dispute the transfer.

### Liberation or release

A released country that receives the mine state gains control of the site and its current condition.

It does not receive another 1,000 political power unless Event 029 independently selects it in a later firing.

The new country may start with low administrative capacity, high foreign interest, and a strong local legitimacy opportunity.

### Peace settlement without direct transfer

If the original controller regains the state, its mine contribution is rebuilt from the current condition.

The system must not restore prewar development or erase damage without a repair route.

## Peacetime variants

In peace, the ordinary challenge is governance, development, labor, and foreign leverage.

Raids are less frequent and more likely to involve criminals, claimants, smugglers, or covert foreign actors.

Revenue settlement has more room to improve legitimacy.

Development projects can use longer time horizons.

## Wartime variants

In war, the mine becomes a strategic treasury and supply target.

The controller may increase pressure, militarize security, requisition transport, suspend dividends, or promise output to a foreign supporter.

The site faces stronger sabotage, occupation, and pay-route risk.

Wartime emergency extraction should deliver a clear temporary advantage and a later cost.

It must not become a free permanent increase.

When the controller's war is being lost or no troops hold the district, the mine is marked about to fall and the owner may Deny the Mine to the Enemy, wrecking and closing the workings so the occupier inherits damage instead of output (implemented, D38, D43, D44).

## Colonial and non-core variants

A colonial or non-core mine begins with lower revenue legitimacy and stronger local claims.

The controller pursues direct extraction (central receipts), a local revenue share, concession company rule, or a military zone through the ordinary decisions; negotiated autonomy is Share Sovereignty or Recognize the Board once The Gilded Sovereignty arises.

Direct extraction gives strong short-term national benefit and increases resistance, foreign propaganda, and armed interference.

A local settlement gives less immediate national benefit and improves order, compliance, and long-term reliability.

The writing direction must describe land, labor, revenue, and control concretely.

It should not rely on generic colonial flavor.

## Multiple mine states

A country controlling several Event 029 mines uses the same policy framework, but each state keeps its own values, contracts, crises, and history.

One mine can be public and well managed while another is occupied, concession-controlled, or Gold-Sick.

The controller aggregate applies diminishing returns.

The selected-mine flow prevents a wall of duplicate decisions.

The system should prioritize a mine with an active mission, crisis, recent control change, or threshold warning when the category opens.

## Baseline completion states

The ordinary event has several valid long-term results:

- public development success
- stable state monopoly
- regulated concession
- militarized but functioning mine
- private enclave under government supervision
- recurring contested district
- temporary closure and recovery
- permanent closure
- catastrophic collapse
- transfer to another controller

The event remains repeatable after one mine reaches any of these states.

A future firing chooses another valid country and state pair.

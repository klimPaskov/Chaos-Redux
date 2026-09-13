# Decisions, Missions, and Player Loop

## Presentation layer

The member experience uses one hidden decision category with a static category picture that changes by evolution.

The category is visible only to:

- active members
- dormant or suspended members with remediation actions
- former members with a live reconnection offer

Outsiders do not receive this category. A country with evidence against one route receives a separate temporary counter-smuggling category tied to that case.

The category header shows:

- Market Credit
- Exposure
- Network Reach
- current government posture
- primary route status
- next offer-rotation date or current delivery mission

Market Credit, Exposure, and Network Reach are the only persistent custom values the member must actively track.

## Clarity budget

A normal phase should show three to five primary actions. Six is the absolute maximum.

The category should show one to three active missions.

When the inventory has more offers than the action budget can show cleanly, use a selected-offer flow:

1. one selector action cycles or selects an offer
2. only the chosen offer's details and purchase action are active
3. one close action clears the selection
4. AI evaluates every valid offer directly without using the player selector

The implementation must not solve clutter by creating several similar categories or a decorative full-screen interface.

## Category phases

### Active trading

Visible content normally includes:

- current offer access
- list surplus
- route action
- government posture action
- Exposure response when relevant

### Delivery in progress

The category replaces weak actions with:

- active delivery mission
- reroute or reinforce delivery when valid
- current route status
- one continuing trade action when capacity remains

### Dormant network access

The category shows:

- restore a route
- contact a former sponsor
- reconcile locked credit
- withdraw permanently

Normal offers are hidden.

### Suspension

The category shows only the actions that address the suspension reason, such as settle an account, replace a compromised route, cooperate with an inquiry, or withdraw.

### Suppression campaign

Normal trading disappears. The category shows the local route and intermediary objectives required to dismantle the cell.

## Purchase flow

A purchase should use the following player sequence:

1. Review the offer class, amount, quality band, provenance class, price, route family, delivery-time band, and risk class.
2. Confirm that the buyer can pay the visible costs and use the cargo.
3. Reserve the offer.
4. Debit Market Credit and any immediate logistics commitment.
5. Dispatch the source package through its provider receipt.
6. Start the delivery mission.
7. Resolve success, delay, partial loss, seizure, cancellation, or sting.
8. Settle the receipt once.

The purchase tooltip must explain all visible costs, the expected Exposure increase, the delivery-time band, and the main blocked reason. It should not reveal the exact hidden outcome chance.

## Purchase decision families

Working design labels are used below. Implementation should write final localisation from their purpose.

### Acquire Current Lot

This is the main offer purchase action.

It changes with the selected offer and uses dynamic localisation for:

- equipment or service class
- amount
- price
- route
- risk
- delivery time
- blocked reason

One generic decision should not expose raw internal equipment tokens.

### Reserve the Lot

High-demand or auction-linked offers can require a short reservation step. Reservation commits credit but does not dispatch until route proof passes.

Reservation is useful only when it creates a real contest or route problem. Ordinary small offers should not require an extra click.

### Commission a Category

Evolution I unlocks a request for one broad offer family in the next rotation.

The action has a long cooldown, Market Credit cost, and partial refund when no supplier appears.

### Arrange a Safer Route

When two paths are valid, the member can commit extra logistics or credit to use the safer path. This changes time, cost, and risk. It does not guarantee success.

### Accept the Dangerous Route

A member can choose the high-risk path when the cargo is urgent. The tooltip must state the risk class and likely Exposure consequence plainly.

## Sale flow

### List Surplus

The member chooses one valid sale family.

The action opens a bounded report with only categories that have verified surplus. The player chooses Small, Medium, or Large where the reserve supports them.

The final confirmation states:

- exact amount to be removed
- protected reserve after the sale
- expected Market Credit return
- expected Exposure
- listing duration
- whether the lot can expire unsold

### Withdraw an Unsold Lot

A seller can withdraw before reservation. The stock returns only when it was never debited or dispatched.

The action has a cooldown to prevent free inventory manipulation.

### State Reserve Release

State Patronage can list a larger government lot. This action has higher Exposure and a stricter readiness check.

### Contribute Intelligence

A member with usable intelligence can publish a bounded information package through the provider API and receive credit after another member buys it.

The action must not expose all agency or operative state to Event 57.

## Route decisions

### Open a New Route

The member selects a valid route family based on geography and evolution. The action starts the relevant mission.

### Repair a Disrupted Route

The action creates a state, port, or logistics objective. It should auto-complete when the player satisfies the condition.

### Shift Traffic

A member with more than one route can move future deliveries away from a pressured path. This lowers pressure on one route and raises it on another.

### Burn the Route

A member can permanently destroy one compromised route to reduce Exposure. The action also reduces Reach and can strand a delivery. It must ask for confirmation when a transaction is still in transit.

## Exposure decisions

### Compartmentalize the Cell

The member spends Market Credit and temporary administrative or intelligence capacity to remove compromised contacts.

It lowers Exposure, reduces route capacity for a period, and can delay the next offer rotation.

### Replace the Manifests

A route-specific action lowers investigation pressure and changes the cargo cover. It is effective only once per investigation episode.

### Sacrifice an Intermediary

A severe action can save a route or government identity by burning one broker. It destroys trust, reduces Reach, and blocks that intermediary from immediate reuse.

### Cooperate with an Inquiry

A penetration or legalist government can allow a bounded investigation. This can lower national Exposure while creating evidence against one route or counterparty.

### Deny State Involvement

State Patronage can attempt to isolate the scandal from the government. Success preserves access. Failure creates harsher evidence and diplomatic effects.

## Government posture decisions

Posture changes should use one selector or event choice. Four permanent buttons would clutter the category.

The player sees:

- current posture
- public effect direction
- change cooldown
- immediate cost or consequence
- route and offer changes

The decision should not reveal hidden infiltration detection chances.

## Delivery missions

### Standard Delivery

Every dispatched purchase starts a visible timed mission.

The mission shows:

- cargo class
- expected arrival range
- current route state
- public risk class
- one or two actions that can materially change the route

The mission auto-completes on settlement. The player does not pay a second click to receive goods.

### Route Security Objective

A large land or occupied-corridor delivery can require the player to hold named states, keep a railway connected, or place supplied divisions along the route.

The objective should use a duration of at least `90` days when the player must move units or repair infrastructure.

Success improves the delivery outcome. Failure can spare part of the cargo while creating a substantial risk increase.

### Escort the Freight

A maritime delivery can require convoys, fuel, and a naval-security condition. Where direct naval supremacy checks are supported, the mission can read them. Otherwise it should use verified convoy and escort proxies.

### Clear the Air Corridor

A covert air delivery can require airbase control, fuel, and a minimum air condition. It is a short emergency mission with severe Exposure.

### Delivery Crisis

A delayed or compromised transaction can create one short follow-up mission. The member chooses to reinforce, reroute, abandon, or accept partial delivery.

A transaction cannot create an endless chain of rescue missions.

## Brokerage missions

### Move Another Member's Cargo

A broker country can earn Market Credit by carrying a delivery between two other members.

The broker commits route capacity and accepts Exposure. It does not learn both endpoint identities unless the route contract requires it.

### Restore a Regional Link

A broker can reconnect two cells through a named port, border, or corridor. Success creates Reach and can prepare Evolution I.

## Grand Auction mission

Evolution III can create one exceptional-lot auction.

The mission sequence is:

1. a valid provider publishes the lot
2. eligible members receive a private bidding event
3. each member submits one bid or abstains
4. the auction closes after a fixed short window
5. the winner and losing refunds are recorded
6. the winning route is validated
7. the delivery begins

The auction should not display a list of member countries or bids.

A player can improve a bid through one bounded action, such as providing better handling capacity or accepting greater Exposure. It should not become a repeated click competition.

## Outsider discovery

An outsider receives no counter-smuggling actions without evidence.

Evidence can come from:

- a seized shipment in owned or controlled territory
- a compromised route through one of its ports
- an intelligence operation
- a member's Exposure breach
- a courier or intermediary arrest
- a former member sharing records
- an owner event that publishes a valid evidence receipt

The first evidence event identifies one case, not the whole network.

## Temporary counter-smuggling category

The category is tied to one known route, intermediary, or member.

It shows:

- evidence confidence as a qualitative state
- known route or cargo class
- investigation deadline
- current action

Evidence confidence can remain internal if the qualitative state and blocked reasons are clear. It should not become a fourth persistent Black Market meter for outsiders.

## Outsider decision families

### Inspect Suspicious Cargo

The country commits customs, intelligence, or military resources to one route endpoint.

Success can seize one shipment or increase evidence. Failure raises route caution and can close the case.

### Watch the Rail Depots

The country places a real state or railway objective on a known corridor.

### Pressure the Intermediary

The country uses diplomacy, sanctions, or security pressure against one proven intermediary.

This action should not reveal countries with no evidence connection.

### Turn a Broker

An intelligence-backed action can convert one intermediary into a source. It is unavailable without sufficient evidence and an intelligence basis.

### Coordinate a Seizure

A mature case can target one active delivery. Success creates a seizure result and route damage. Failure can expose the investigation.

### Dismantle the Local Cell

This is a capstone objective that requires several completed proofs, no active unresolved delivery, and control over the relevant route area.

Success removes the regional route set. It does not automatically end the global network.

## Suppression campaign missions

A member that starts Suppression uses its local knowledge against the network.

The campaign should normally include two or three objectives selected from:

- seize the local clearing account
- close the primary route
- arrest or turn the intermediary
- secure the depot
- prevent one evacuation delivery
- expose a foreign sponsor

The player should not see every possible mission at once.

Partial success can burn the route but fail to expose the clearinghouse. Failure can lead to expulsion and retaliation.

## Decision costs

Costs should match the action.

Useful cost families include:

- Market Credit
- convoys
- trains
- trucks
- fuel
- infantry or support equipment
- civilian factory burden
- army, navy, or air experience
- command power within the project's conservative cap
- political power for real government or diplomatic actions
- stability or war support as a consequence of public exposure
- temporary intelligence exposure
- tied-down divisions through mission requirements

A single action can use no more than four spendable cost types.

Costs must be icon-first and use matching texticons. Requirements such as holding a port or fielding supplied divisions belong in the requirement tooltip.

## Effects that should feel meaningful

A purchase should solve a visible military or logistics problem, create a strategic option, or provide useful intelligence.

A sale should convert genuine surplus into enough credit to matter.

A route mission should open, restore, or protect an actual path.

An Exposure response should save access, reduce risk, or sacrifice capability.

Avoid decisions whose whole result is a tiny generic modifier, a trivial amount of political power, or a token stockpile.

## Decision cleanup

The event-owned cleanup contract must remove or replace decisions when:

- an offer expires
- a selected offer is bought or invalidated
- a route disappears
- a country leaves membership
- a member becomes dormant or suspended
- a posture changes
- a delivery settles
- an investigation closes
- a target country disappears
- a known intermediary changes government or enters war
- the network is dismantled

No stale target, route, offer, or transaction decision should remain visible.

## AI equivalents

Every action available to AI members must have an AI path that does not depend on clicking a player-only selector.

The AI should:

- evaluate all valid offers
- buy only strategically useful cargo
- respect protected reserves when selling
- choose route missions it can complete
- respond to high Exposure
- avoid impossible state or port objectives
- use penetration only with intelligence capacity
- avoid suppression when an existential shortage makes withdrawal irrational
- abstain from auctions it cannot handle

Detailed scenario expectations are defined in the AI and balance specification.

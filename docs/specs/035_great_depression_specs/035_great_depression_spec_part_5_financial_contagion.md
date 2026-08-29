# Great Depression 2.0 specification, part 5: Evolution I, Financial Contagion

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

Financial Contagion turns one national depression into an international economic risk. It adds a sparse relationship network, lighter secondary-country pressure, foreign intervention, supplier opportunities, and the possibility that another country develops a full Event 35 crisis.

The evolution does not give every related country the full decision category. Most secondary countries receive a compact Economic Contagion condition and a small action set. Full Event 35 activation requires sustained exposure plus local vulnerability.

## Availability and activation

Financial Contagion becomes available at Rising Chaos.

Normal active-event activation should require:

- Event 35 is active in a valid origin country.
- Evolution I is enabled in Event Details.
- The origin has meaningful external relationships.
- Severity or one hidden external component is high enough to create an international risk.
- The evolution has not already been recorded for this episode.
- The dynamic evolution delay has elapsed.

A base timing target near `90` days is appropriate under strong conditions. Lower Severity, secure trade, successful finance policy, weak international links, and coordinated aid should slow activation. Deep Depression, failed finance missions, large external exposure, and an Event 34 speculative collapse should accelerate it.

An Event 34 Evolution I collapse activates the enabled Financial Contagion module immediately when Event 35 begins. It still records the Event 35 evolution context once. The Event 34 evolution log is not reused as the Event 35 log.

Evolution activation itself adds zero Chaos. Chaos changes belong to concrete spread outcomes described later.

## Evolution logging

The evolution record uses:

- Parent event ID `35`.
- Evolution type for Financial Contagion.
- Evolution stage `1`.
- Display tier Rising Chaos.
- Origin country as actor.
- Current crisis episode ID in the Event 35 ledger.

The event-detail preview explains international financial exposure, aid, market retreat, and possible spread. It must not state that a specific country will be infected before a valid relationship and pressure exist.

## Exposure network

The network is built from relationships the game can prove. It must not claim exact bilateral trade volume when script cannot observe it.

### Strong exposure links

- Subject to overlord.
- Overlord to subject.
- Shared economic market when the relevant system and DLC are present.
- Explicit Event 35 credit, clearing, rescue, supplier, or reconstruction agreement.
- A country that has provided a large Event 34 or Event 35 industrial support package.
- A creditor or debtor link created by an Event 35 decision.

### Medium exposure links

- Faction membership.
- Direct land adjacency with substantial normal economic contact.
- Guarantee or close alliance with an active aid relationship.
- Shared war economy with an exact equipment, convoy, or industrial-support transaction.
- A major port or clearing partner created by the event.

### Light exposure links

- High opinion and a valid commercial relationship.
- Regional proximity.
- Common dependence on an explicit distressed supplier.
- A one-time distressed-asset transaction.

A light link alone should rarely cause a full crisis. It can add a minor condition, open a decision, or combine with other links.

## Sparse registry

The evolution should maintain a sparse list of exposed countries for each origin episode.

Each row records:

- Origin episode ID.
- Origin country.
- Exposed country.
- Relationship type.
- Current exposure stage.
- Peak exposure stage.
- Last material source.
- Aid or abandonment state.
- Full-crisis conversion receipt.
- Propagation depth.
- Cooldown and cleanup state.

The registry should be built from bounded candidate scopes when the evolution activates and when an event-owned relationship changes. It must not create a new recurring whole-world scan.

## Economic Contagion condition

Secondary countries see one qualitative condition. It is not a new public numerical meter.

| Exposure stage | Working condition | Effect direction | Available response |
| ---: | --- | --- | --- |
| `1` | Exposed Markets | Small confidence and trade pressure | Monitor or reduce exposure |
| `2` | Credit Strain | Lending and construction begin to weaken | Ring-fence finance or support partner |
| `3` | Contracting Economy | Output, construction, and stability pressure become material | Strong intervention, retreat, or aid |
| `4` | Near Depression | Local conditions can convert into full Event 35 | Emergency containment mission |

The exact effects scale with the exposed country's vulnerability. A small subject tied to one market may suffer more than a diversified major at the same qualitative stage.

## Exposure pressure

Exposure rises through:

- Origin Severity and trend.
- Origin bank panic or trade-credit failure.
- Strong relationship type.
- Failed foreign aid.
- Abandonment of a distressed partner.
- Shared dependence on a failed supplier or debtor.
- Evolution III world pressure.
- A boom supplier that accepts excessive distressed demand and later fails.
- Currency, debt, or clearing incidents created by this evolution.

Exposure falls through:

- Origin recovery.
- Ring-fencing domestic institutions.
- A successful coordinated rescue.
- A clearing agreement.
- Diversification of trade or supply.
- Temporary capital controls where valid.
- Debt standstill or restructuring.
- Ending the exact relationship that created exposure, with its political and economic consequences.

## Secondary-country actions

The exposed country receives a compact decision category or a small section in an existing Event 35 category when it already has the full crisis.

### Ring-Fence Domestic Finance

Restricts the transmission of credit and banking stress. It costs administrative and civilian capacity, may reduce foreign flexibility, and lowers exposure drift.

It is strongest for countries with stable institutions. It is weaker after the country reaches Near Depression.

### Extend Emergency Credit

Supports the origin through a real resource or industrial commitment. It can lower origin Severity and the provider's future exposure. It risks larger losses if the origin continues to deteriorate.

The provider chooses the scale. Costs may include civilian factories, political authority, convoys, fuel, or another exact transfer. No more than four spendable costs are shown.

### Shift Import and Contract Dependence

Reduces exposure to the origin by finding another supplier or market. It requires a valid alternative, time, convoys, and possible output disruption. It can raise relations or dependence with the new partner.

### Abandon the Distressed Market

Cuts the strongest relationship quickly. It reduces future exposure while causing an immediate shock to the origin, diplomatic damage, and possible loss of investment or supply.

The action should be attractive when the origin is near Economic Paralysis and the exposed country has little ability to help. It should not be a free universal solution.

### Acquire Distressed Assets

Uses spare capital, industrial capacity, or a current Industrial Boom to purchase failed assets, contracts, or concessions. It gives the origin short-term relief and the buyer a bounded advantage. It can create dependency, resentment, or later political action.

### Coordinate an International Rescue

Available to a major, overlord, faction leader, or coalition of valid providers. It requires several material contributions and a timed mission. Success reduces exposure across the registered network. Failure can accelerate several countries at once.

## Origin-country actions

### Request Emergency Credit

Seeks a valid provider. The origin accepts dependency, concessions, or oversight. The provider must be able and willing to pay.

### Offer a Debt Standstill

Temporarily suspends or restructures event-created obligations. It lowers immediate credit pressure and can reduce contagion. It harms confidence, relations, or future access according to the relationship.

### Sell Distressed Assets

Raises immediate support by transferring a bounded economic interest to another country. It cannot sell the same asset twice. A state, concession, or industrial receipt must have one owner.

### Establish a Clearing Bloc

Creates a limited group of countries that keep essential exchange working through reciprocal commitments. It lowers trade pressure while reducing flexibility outside the bloc.

### Accept External Supervision

A desperate country accepts stronger foreign control over finance, trade, or reconstruction. It provides relief and can create subject pressure, influence, or an event-specific dependency. It cannot silently change autonomy without a visible consequence chain.

## Full-crisis conversion

An exposed country converts into full Event 35 only when all of the following are true:

- It uses normal civilian systems.
- It does not already have Event 35 active.
- Exposure has reached Near Depression or an equivalent severe state.
- Local vulnerability is high enough.
- A conversion delay or incident has resolved.
- No conversion receipt exists for this origin episode.
- Event 35 is enabled for the country and no conflict contract blocks activation.

Local vulnerability considers:

- Stability.
- Trade and convoy dependence.
- Industrial concentration.
- Existing damage or famine pressure.
- Strong subject, market, or creditor dependence.
- Earlier depression scars.
- Current war and blockade.
- Recovery reforms.

The new crisis records:

- Entry source Financial Contagion.
- Origin country and origin episode.
- Propagation depth.
- Starting exposure stage.
- Foreign actions already taken.
- Starting Severity based on exposure and local vulnerability.

The conversion is a consequence call. It does not consume another normal random-event pacing transaction.

## Propagation depth and anti-loop rules

A country converted through contagion can become a new source only after its own Financial Contagion evolution is valid and active. The new propagation link records its depth from the original episode.

Initial rules:

- Direct origin links have depth `1`.
- A converted country's links begin at depth `2` or greater.
- Pressure declines with each additional depth.
- No country can convert twice from the same original episode.
- The network cannot immediately send the same shock back to the country that sent it.
- A source-target pair has a cooldown after aid, abandonment, or conversion.
- A recovered country clears outgoing spread after a proof period.
- Duplicate faction, subject, and event-created links are merged into one strongest relationship row.

These rules prevent rapid ping-pong spread and repeated consequence farming.

## Industrial Boom interaction

A country with an active Event 34 Industrial Boom becomes a special potential supplier.

### Supply Depressed Markets

The boom country accepts large foreign orders. It gains stronger output demand and project opportunity. Its Overheating rises through added order, freight, labor, and credit pressure.

The depressed recipient receives lower trade, demand, or logistics stress. The transaction uses a real relationship receipt and cooldown.

### Finance Reconstruction

The boom country commits civilian capacity, convoys, fuel, equipment, or credit to a recovery project. It can create a lasting trade relationship or foreign influence. It raises Overheating more slowly than unrestricted supplier demand.

### Acquire Distressed Industry

The boom country buys assets or concessions. It receives a bounded benefit and stronger long-term exposure to the recipient. The recipient gains immediate relief but can incur dependency and Social Collapse pressure.

### Refuse the Orders

The boom country protects its Overheating and gives up the foreign opportunity. The recipient receives no new arbitrary penalty unless it had already committed to the supplier relationship.

### Boom collapse during rescue

If the supplier boom collapses:

- Event 34 hands the supplier into Event 35.
- Existing rescue agreements are frozen.
- Recipient countries receive a registered trade or credit shock.
- Evolution III world pressure can rise.
- The same failed agreement is not counted once for Event 34 and again for every Event 35 origin without separate receipts.

## Foreign aid and exploitation balance

Aid and exploitation are both supported. Neither is a free optimal path.

Aid risks:

- Provider Overheating or fiscal strain.
- Losses if the origin fails.
- Convoy and equipment burden.
- Domestic criticism.

Exploitation risks:

- Dependency and resentment.
- Evolution II political backlash.
- Exposure to the purchased market.
- Condemnation or diplomatic pressure only when another registered system supports it.

Abandonment risks:

- Origin shock.
- Lost influence and investment.
- Faction or subject strain.
- A stronger chance that the crisis spreads through another route.

## Contagion incidents

Incident families include:

- A correspondent institution fails.
- A foreign-currency obligation becomes unpayable.
- Trade credit is withdrawn.
- A bank holiday is declared in an exposed country.
- A debt conference opens.
- A rescue loan fails to arrive.
- A supplier demands concessions.
- Capital leaves one market for another.
- A clearing bloc forms.
- A coordinated rescue succeeds.
- A country abandons an exposed partner.

Every incident names the relevant countries and relationship. It should not use generic global text when only two countries are involved.

## Event and news presentation

The origin receives a report when the evolution activates and when a major foreign action changes the network. Exposed countries receive local reports only when their own pressure becomes material.

World news is reserved for:

- A major international rescue.
- The first full secondary depression from one origin.
- Collapse of a major clearing or credit network.
- A large market bloc abandoning the origin.

Routine exposure changes remain in the category and event history.

## Chaos impact

Financial Contagion activation adds zero Chaos.

Concrete one-shot outcomes may add Event 35 Chaos:

- First secondary country enters full Event 35 from one origin episode.
- A third or later country enters the same contagion chain.
- A major international rescue fails and causes several new severe exposures.
- A large clearing or credit network breaks apart.

The values should be small and guarded, for example `+1` for first spread and a larger one-time milestone for a genuine multi-country chain. Generic Chaos from war, annexation, ideology change, deaths, or world tension is not repeated.

Recovery can remove only the matching Event 35 spread pressure that was previously added. It cannot subtract Chaos for ordinary aid or one country's recovery when the wider chain remains active.

## Resolution

The origin's contagion episode enters resolution when:

- Origin Severity remains below the safe range.
- No exposed country remains at Near Depression.
- No unresolved rescue or abandonment mission remains.
- No new transmission occurs during the proof period.

Resolution:

- Stops new exposure from the origin episode.
- Decays lighter conditions.
- Preserves converted countries as independent Event 35 crises.
- Records countries aided, abandoned, exploited, or converted.
- Removes temporary foreign decisions.
- Preserves valid dependency or clearing agreements that have a post-crisis purpose.

A converted country does not recover automatically because the origin recovered.

## AI behavior

AI evaluates exposure according to:

- Own stability and Severity.
- Relationship strength.
- Faction or subject responsibility.
- Provider resources.
- War state.
- Convoys and trade access.
- Existing foreign influence.
- Origin importance.
- Expected contagion risk.
- Event 34 Overheating when the provider has an active boom.

An AI should aid a vital subject or ally when it can afford the cost. It should ring-fence or abandon an origin that is unlikely to recover and threatens its own survival. A boom AI should not accept every distressed order when Overheating is already dangerous.

Named scenarios are defined in part 9.

## Disabled evolution behavior

If Financial Contagion is disabled:

- No new exposure registry is created.
- Existing lighter exposure from a previously enabled state is retired safely.
- No full-crisis conversion can occur through this module.
- Event 34 inherited Evolution I still affects starting Severity and state conversion, but does not activate disabled contagion content.
- Baseline recovery remains fully possible.
- A higher enabled evolution does not silently recreate this module.

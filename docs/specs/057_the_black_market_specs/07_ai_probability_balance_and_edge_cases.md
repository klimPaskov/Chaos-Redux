# AI, Probability, Balance, and Edge Cases

## AI design goal

AI countries should use the Black Market to solve real strategic problems and dispose of real surplus. They should not join, buy, sell, sponsor, suppress, or bid merely because an action is available.

AI decisions must respect:

- membership state
- route validity
- current war
- equipment deficits and reserves
- fuel and convoy position
- legal market access
- embargoes
- government posture
- stability and war support
- intelligence capacity
- Network Reach
- Exposure
- provider permissions
- current delivery capacity
- active investigations
- recent transaction history

## AI strategic roles

The system can derive one or more hidden roles for each member.

### Desperate buyer

Typical conditions:

- at war
- major equipment or fuel deficit
- poor legal market access
- embargoed or isolated
- valid route

Behavior:

- accepts invitations readily
- values useful current offers
- tolerates higher Exposure
- invests in route security
- avoids selling essential stock

### Surplus seller

Typical conditions:

- stockpile well above readiness reserve
- weak need for the equipment class
- low current Market Credit
- reliable route

Behavior:

- lists bounded surplus
- avoids selling below reserve
- favors Compartmentalized Tolerance or State Patronage according to government type
- does not buy back the same category while a recent-import lock exists

### Broker

Typical conditions:

- central location
- several borders or ports
- good relations with several members
- strong routes
- moderate equipment demand

Behavior:

- opens and repairs routes
- carries third-party cargo
- values Network Reach
- protects Exposure to retain access

### State patron

Typical conditions:

- authoritarian or security-led route
- prolonged war or embargo
- large state stockpile
- high tolerance for diplomatic risk

Behavior:

- chooses State Patronage
- underwrites Market Credit
- sells larger surplus lots
- pays for route capacity
- reacts strongly to investigations

### Penetrator

Typical conditions:

- strong intelligence or internal-security capacity
- low ordinary demand
- high anti-corruption or hostile-network policy
- evidence of a route

Behavior:

- uses cover trades sparingly
- builds evidence
- attempts one coordinated seizure
- avoids random exposure-generating purchases
- abandons penetration if an existential shortage makes access more valuable than suppression

### Opportunistic auction bidder

Typical conditions:

- high credit
- route capacity
- strong need for the exceptional lot
- ability to deploy or use it

Behavior:

- bids within reserve
- abstains when the lot has no strategic use
- invests in handling only when the expected value is high

## Invitation AI

An AI candidate first checks hard blockers.

Hard zero conditions include:

- no valid route proposal
- actual nonhuman or excluded special-country state
- active permanent dismantlement policy
- current expulsion exclusion
- no government scope capable of accepting
- the network is fully dismantled
- the candidate cannot use, sell, broker, or investigate anything in the current cell

Acceptance score then considers need, access, politics, trust, and risk.

### Desired ordering

A country under embargo, at war, with a severe equipment shortage and a valid land route should score far above a peaceful country with open legal trade and no shortage.

A country with a direct border and moderate relations should normally score above a friendly country with no physical route.

A recent rejection or suppression campaign should dominate small positive factors.

## Government posture AI

### Compartmentalized Tolerance

Preferred when:

- the country needs access
- Exposure is moderate
- institutions fear scandal
- trade volume is limited
- the country lacks capacity for State Patronage

### State Patronage

Preferred when:

- war or embargo creates high demand
- the government can commit state resources
- a large surplus exists
- Exposure is low or the government accepts the risk
- intelligence and route capacity are sufficient

Avoid when:

- Exposure is already high
- a public scandal would threaten regime stability
- there is no large trade opportunity

### Counterintelligence Penetration

Preferred when:

- the country has intelligence capacity
- ordinary market need is low
- evidence or policy supports suppression
- at least one route or broker can be investigated

Avoid when:

- the country lacks a valid intelligence path
- the network is the only realistic source of essential equipment
- active war makes the cover operation too costly

### Suppression Campaign

Preferred when:

- Exposure is severe
- strategic need is low
- an investigation has mature proof
- the government has the resources to close the route
- the network threatens internal policy or diplomatic survival

Avoid when:

- an existential equipment or fuel deficit remains
- every route objective is impossible
- the government has an unsettled exceptional delivery it urgently needs

## Purchase AI

The AI should rank offers by strategic utility, not nominal rarity.

Utility inputs include:

- current deficit in the exact equipment class
- current production and time to solve the deficit legally
- current and expected war
- equipment age and compatibility
- fuel and storage
- airbases, ports, and templates
- route cost and risk
- Market Credit reserve
- current Exposure
- recent import lock
- legal market alternatives
- expected delivery time

### Hard zero purchase conditions

- invalid or unsupported equipment token
- no valid route
- insufficient credit
- insufficient required logistics
- buyer cannot use the package
- purchase would exceed handling capacity
- provider permission expired
- buyer is suspended
- buyer is the source seller when self-purchase is forbidden
- recent-import lock or transaction state makes the action exploitative

### Credit reserve

AI should retain a dynamic credit reserve for:

- emergency fuel
- route repair
- active delivery crisis
- expected commission
- current auction commitment

A normal purchase should not spend the final reserve unless the cargo solves an existential problem.

## Sale AI

The AI calculates protected reserve before listing.

Hard zero sale conditions include:

- stock at or below reserve
- recent-import lock covers the apparent surplus
- equipment is reserved for another transaction
- sale would create an immediate deployment deficit
- no valid buyer or route class exists
- seller is suspended

A seller with at least `150%` of its dynamic reserve should receive a strong positive score for a Small or Medium lot. A seller near `110%` should usually score zero. A Large lot should require a much higher surplus and favorable war conditions.

## Route AI

Route selection order should be contextual.

Typical preference:

1. open direct land route
2. reliable international corridor
3. stable maritime route
4. neutral relay
5. occupied corridor
6. covert air route

This order can change for islands, blockades, poor infrastructure, hostile fronts, or urgent intelligence cargo.

AI must not start a route mission whose state, port, intermediary, or logistics requirement is impossible.

## Exposure AI

Exposure should change AI behavior before it reaches `100`.

| Exposure band | AI response |
| --- | --- |
| Hidden | Normal strategic use |
| Rumored | Prefer low-risk routes and limit low-value trades |
| Under Investigation | Spend on cover, shift traffic, avoid large nonessential lots |
| Compromised | Repair, burn, withdraw, or suppress according to need and posture |
| Breach | Resolve the breach before ordinary trading resumes |

A desperate country can accept higher Exposure for essential cargo. That exception should be tied to measurable shortage and war state.

## Auction AI

AI bids only when:

- the package is valid
- it can use the package
- a route can carry it
- the strategic utility exceeds a threshold
- the bid leaves an acceptable reserve, unless the need is existential

AI should not bid more than about `70%` of available credit in ordinary circumstances. A higher bid requires an existential strategic condition and a viable delivery route.

The AI should not bid on a rare technology it already owns, aircraft it cannot base or fuel, ships it cannot receive, or equipment with no valid template use.

## Counter-smuggling AI

An outsider needs evidence before acting.

AI evaluates:

- confidence of evidence
- route through its territory
- hostile or sanctioned participant
- value of the suspected cargo
- cost of investigation
- current war and internal priorities
- diplomatic consequences

A country should prioritize a route that carries enemy strategic material through its own territory. It should ignore weak rumors with no route or target.

## Named probability scenarios

Every weighted surface must receive a baseline inspection, owner patch, and post-change comparison through `chaosx_ai_probability_auditor`.

The auditor starts with `hoi4.probability_inspect` and uses the same named scenarios before and after implementation changes.

### BM-P01: Invitation under desperation

| Input | Candidate A | Candidate B |
| --- | --- | --- |
| War | active defensive war | peace |
| Embargo | active major embargo | none |
| Equipment | severe infantry deficit | full reserve |
| Legal market | poor access | open access |
| Route | open land route | open land route |
| Expected result | strong acceptance | low acceptance |

Acceptance score for Candidate A should be at least three times Candidate B before normalization, unless a hard political blocker applies.

### BM-P02: Route proof over friendly relations

| Input | Candidate A | Candidate B |
| --- | --- | --- |
| Relations to sponsor | moderate | high |
| Route | direct border | no valid route |
| Need | moderate | high |
| Expected result | eligible | hard zero |

A friendly country with no route must not enter the normalized invitation pool.

### BM-P03: Safe surplus sale

| Input | Seller A | Seller B |
| --- | --- | --- |
| Stock relative to reserve | `180%` | `108%` |
| War | peace | active war |
| Recent imports | none | present |
| Expected result | Small and Medium valid | all sale sizes zero |

### BM-P04: Fuel purchase utility

| Input | Buyer A | Buyer B |
| --- | --- | --- |
| Navy and air demand | high | low |
| Fuel days | fewer than `10` | more than `90` |
| Route | maritime valid | land valid |
| Expected result | fuel offer ranks first | fuel offer low or zero |

### BM-P05: Route selection

| Input | Route A | Route B |
| --- | --- | --- |
| Type | land | maritime |
| Status | Open | Strained |
| Time | shorter | longer |
| Risk | Low | High |
| Cargo | medium small arms | medium small arms |
| Expected result | land dominates | maritime selected only after material state change |

A separate island variant should reverse the hard feasibility result when no land route exists.

### BM-P06: High-Exposure posture response

| Input | Member A | Member B |
| --- | --- | --- |
| Exposure | `82` | `18` |
| Posture | State Patronage | Compartmentalized Tolerance |
| Strategic shortage | low | moderate |
| Expected result | cover, route burn, withdrawal, or suppression preferred | normal trade preferred |

### BM-P07: Provider approval gate

| Input | Package A | Package B |
| --- | --- | --- |
| Owner registration | valid | missing |
| Minimum evolution | met | met |
| Source debit | proven | unproven |
| Expected result | eligible pool entry | exact zero and reject reason |

No modifier may rescue Package B.

### BM-P08: Grand Auction utility

| Input | Bidder A | Bidder B |
| --- | --- | --- |
| Package use | fills severe tank deficit | no armored template use |
| Credit | adequate | abundant |
| Route | heavy cargo valid | heavy cargo valid |
| Expected result | bids within reserve | abstains despite more credit |

### BM-P09: Embargo-circumvention demand

Compare the same member before and during Event 50.

Expected changes:

- invitation score rises
- fuel and equipment commission scores rise
- neutral and maritime route value rises
- Exposure tolerance rises only when shortage is real

The embargo flag alone should not make every package desirable.

### BM-P10: Counter-smuggling evidence

| Input | Observer A | Observer B |
| --- | --- | --- |
| Evidence | mature route receipt | rumor only |
| Route through territory | yes | no |
| Enemy cargo | proven | unknown |
| Expected result | investigation and seizure actions score high | no active action |

## Probability evidence methods

Use:

- `hoi4.probability_evaluate` for complete invitation, option, offer, and bid pools
- `hoi4.probability_sweep` for Exposure, shortage, reserve, and route-pressure thresholds
- `hoi4.probability_compare` after every weight patch
- `hoi4.probability_simulate` for offer rotations and invitations when exact pools are too large but fully declared
- `hoi4.probability_sequence` only after cadence, recovery, caps, offer expiry, invitations, cooldowns, route loss, and terminal states are fully declared
- `hoi4.probability_render` for matrix and sensitivity evidence when it improves review

The audit must label evidence as exact, bounded, sampled, score-only, or unresolved.

## Balance anchors

### Founding

- target founders: `3`
- minimum founders: `2`
- maximum founders: `4`
- one initial route per founder where possible
- one-time founding credit only

### Offer slots

- baseline: `3`
- Evolution I: `4`
- Evolution II: `5`
- Evolution III: `6`

### Route limits

- baseline ordinary member: `1`
- Evolution I established member: up to `2`
- Evolution II or III mature broker: up to `3`

These are caps, not guaranteed free routes.

### Active jobs

- one selected offer for the human-facing flow
- no more than two ordinary deliveries per member without additional capacity
- one Grand Auction commitment per member
- one to three visible missions in the category

### Reach and evolution

- Evolution I Reach: `35+`
- Evolution II Reach: `65+`
- Evolution III Reach: `85+`

Evolution also needs Chaos, membership, region, route, and MTTH proof.

### Exposure

Exposure must rise enough that repeated large transactions force a response. It should fall slowly enough that the player cannot erase every risk between rotations.

A member using Compartmentalized Tolerance for small occasional trades can remain hidden with active management. A State Patron moving large exceptional packages should approach investigation or breach unless it invests heavily in routes and cover.

### Lot handling

Amounts should be limited by the smaller of:

- verified source amount
- buyer need
- route capacity
- buyer handling capacity
- current evolution's lot band

An exceptional source can create a large effect, but handling capacity should stop a tiny route from moving a major power's entire arsenal at once.

## Credit pricing and sinks

Important sinks are:

- purchase price
- network fee
- route opening and repair
- commissions
- Exposure cleanup
- auction bids
- withdrawal settlement

Credit income must remain lower than the buyer price for the same lot.

The recent-import lock, network fee, seller reserve, and one-time receipt prevent simple buy and resale farming.

## Exploit controls

### Founding credit farming

- one permanent country receipt
- no second grant after reconnection, civil war, annexation, release, or tag transfer
- a genuine successor needs a new invitation and receives only the normal successor package defined by the implementation

### Buy and resale loop

- recent-import ledger subtracts purchased cargo from saleable surplus
- seller yield is below buyer price
- self-purchase is forbidden
- same transaction cannot create a new provider lot

### Stockpile duplication

- source debit occurs once before dispatch
- transaction state is persisted
- delivery effect checks settlement receipt
- partial delivery uses the already-debited source
- seizure cannot give full cargo to both observer and buyer

### Offer reroll abuse

- rotation interval is persistent
- commission has a cooldown
- opening and closing the category cannot reroll offers
- reloading cannot reroll a committed rotation

### Route mission farming

- route IDs are stable
- reopening the same unchanged route does not award new Reach or credit
- broker rewards require a settled third-party delivery
- burned routes require new proof

### Exposure cleanup farming

- cleanup actions have cooldowns
- each investigation episode has one-use responses
- burning a route creates a real capacity and Reach loss
- changing posture cannot reset Exposure

### Auction abuse

- one bid per member
- one bounded bid-improvement action
- full route and use validation
- losing refund lower than committed bid when a real handling cost was spent
- no repeated auction for the same provider receipt

### Civil-war duplication

- membership, credit, recent imports, offers, and routes transfer to at most one side through explicit proof
- unresolved state produces candidates, not copied active members

### Annexation inheritance

- annexer receives no automatic membership, credit, or provider rights
- dispatched cargo resolves against persisted buyer scope or cancels through explicit successor rules

## Important edge cases

### No valid founding cell

Event 57 is unavailable. It remains unfired and keeps its normal future eligibility.

### Only two eligible countries

Create a two-country founding cell with lower starting Reach and prioritize a third invitation after the first successful delivery.

### Player is not invited

The system proceeds under AI control. The player can later be invited or discover a route.

### All founders reject

The founding transaction retries only through one bounded alternate cell attempt. If that also fails, the event returns to unfired availability through the normal event-system rejection contract and leaves no half-created network.

The implementation must confirm whether the random-event framework supports transactional rollback before choosing the exact firing order.

### Seller disappears before debit

Cancel the offer and clear the reservation. No buyer delivery starts.

### Seller disappears after dispatch

The cargo remains a debited anonymous shipment. It can arrive, be delayed, or be seized according to the route.

### Buyer disappears before dispatch

Cancel and refund according to the reservation contract.

### Buyer disappears after dispatch

Use the explicit successor or seizure rule. Never grant the cargo twice.

### Route disappears during delivery

The job enters a delivery crisis once. It can reroute, partially deliver, or fail.

### Equipment definition becomes invalid

Invalidate the offer before purchase. A dispatched transaction requires an owner migration or safe cancellation contract.

### DLC changes between saves

DLC-dependent packages must fail closed and settle safely. The core member, credit, route, and exposure ledgers remain valid.

### Network reaches zero active members

Enter dormancy. Stop normal rotations. Keep sparse reconstruction records and history.

### Network is fully dismantled

Clear reconstruction eligibility, settle jobs, retain logs and achievements, and prevent a second initial firing.

### World-end state begins

The ordinary global event system stops according to shared rules. Event 57 should stop new invitations and rotations, then settle or freeze active transactions according to the owning terminal system's compatibility contract.

It must not run an independent world-end process.

## Performance constraints

- no whole-world daily, weekly, or monthly scan
- registered member and route arrays only
- bounded candidate samples
- dirty-route refresh after relevant world changes
- one committed invitation per growth pulse
- one rotation job for the global market
- one receipt per offer and transaction
- cleanup of invalid records before new generation

## Balance review scenarios

Implementation balance review should run at least these campaign states:

1. small neutral member in peace with modest surplus
2. embargoed minor in defensive war
3. major power with huge stockpile and several legal alternatives
4. island member under blockade
5. landlocked member with one neutral corridor
6. State Patron at high Exposure
7. penetrator with mature evidence
8. Evolution I network with two regional cells
9. Evolution II network with one experimental provider
10. Evolution III Grand Auction with several valid AI bidders
11. all routes destroyed and reconstruction pending
12. full dismantling attempt

The report should record actual offers, prices, route times, AI choices, Exposure movement, Reach movement, and exploit findings. A statement that the system feels balanced is insufficient.

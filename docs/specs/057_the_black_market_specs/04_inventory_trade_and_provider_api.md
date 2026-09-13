# Inventory, Trade, and Provider API

## Inventory principle

Every offer needs three proofs:

1. A source exists.
2. At least one active member can receive the cargo.
3. A valid route can move it.

An offer that lacks any proof does not appear. The system must not create fake seller stockpiles, placeholder equipment types, empty technology grants, or cargo that no member can use.

## Offer slots and rotation

| Event state | Maximum visible slots | Normal rotation interval |
| --- | ---: | ---: |
| Baseline | `3` | `45-75` days |
| Evolution I | `4` | `40-70` days |
| Evolution II | `5` | `35-65` days |
| Evolution III | `6` | `30-60` days |

Six is the hard maximum for one inventory phase.

A rotation can preserve one unsold offer when it remains valid and has not reached its expiry. It should replace invalid, expired, or repeatedly ignored offers. It should not reroll several times in one day to search for a perfect reward.

The interval should respond to:

- Network Reach
- number of active members
- number of active routes
- recent completed deliveries
- war and embargo pressure
- route disruptions
- provider availability
- recent inventory starvation
- recent repeated offers from the same class

All values must be centralized in the Event 57 tuning source.

## Offer record

Each slot should store a complete immutable offer receipt until it is replaced or purchased.

Required fields include:

- offer ID
- source package ID
- provider ID
- source class
- seller country when one exists
- hidden source identity state
- equipment or service class
- concrete equipment token or owner effect
- quantity
- quality or era band
- Market Credit price
- network fee
- optional logistics cost
- expected Exposure band
- valid route family
- expected delivery-time band
- buyer eligibility trigger
- creation date
- expiry date
- current reservation owner
- source-debit state
- transaction state
- project-completion isolation proof for special packages

A purchased offer becomes a transaction. It must not remain available to another buyer unless the source package explicitly represents several independent lots.

## Source classes

A member sees a provenance class, not necessarily a country name.

Useful classes are:

- member surplus
- diverted state reserve
- captured battlefield stock
- surrendered or collapsed-state stock
- neutral commercial diversion
- stolen industrial shipment
- recovered depot stock
- intelligence package
- technical dossier
- owner-approved experimental package
- unknown broker lot

The source class must be truthful. A member-surplus lot cannot be relabeled as captured stock merely to conceal a debit error.

## Baseline offer families

### Small arms

Includes valid infantry equipment tokens and closely related basic weapons.

Amount should derive from:

- verified seller surplus
- buyer deficit
- buyer army size
- route capacity
- world date and equipment generation
- recent imports that cannot be resold

A baseline offer should be large enough to equip a meaningful number of battalions, but should not erase a major country's full deficit through one small route. Small foreign or captured lots can use this family when their source receipt is valid.

### Support and artillery equipment

Includes support equipment, artillery, anti-tank, anti-air, and other ordinary support classes that the current equipment registry marks valid.

The system must validate the exact token and DLC state. It should not offer an archetype with no concrete equipment implementation.

### Trucks and trains

These are high-value logistics offers for countries whose supply system is constrained.

A seller must retain a dynamic reserve based on army size, active fronts, supply use, and current route commitments.

### Fuel

Fuel offers should scale to a number of days of current consumption.

Suggested handling bands:

- emergency lot: roughly `7-15` days of current consumption
- operational lot: roughly `15-30` days
- strategic reserve: roughly `30-45` days, later evolution only

The final amount is bounded by seller surplus or provider capacity, buyer storage, route capacity, and current evolution.

### Convoys

Convoy offers can come from member surplus, captured or surrendered stock, Event 56 packages, or verified commercial diversion.

A seller must keep enough convoys for active trade, supply, invasions, and route commitments.

### Intelligence

Baseline intelligence offers can provide one bounded temporary advantage against a named target.

Possible classes include:

- military estimates
- naval deployment information
- air-force estimates
- industrial estimates
- convoy route information
- mobilization plans
- local network access

The buyer must have a strategic reason to use the package. A generic global intelligence bonus is too broad.

## Evolution I offer families

Evolution I adds larger conventional military and logistics cargo. Small foreign and captured lots can already appear at baseline, while this evolution opens major battlefield and surrendered-stock packages.

### Tanks and armored vehicles

Offers require a valid concrete equipment token, source proof, buyer ability to use the equipment class, and a route that can handle heavy cargo.

The buyer does not need to own the source technology merely to deploy foreign equipment. The offer must not grant that technology.

### Aircraft

Aircraft offers follow the same source and buyer rules. Airframe and module compatibility must be checked against the installed DLC and equipment definition.

A buyer needs airbases and fuel before AI should value the offer highly.

### Larger artillery and transport lots

These packages can solve serious operational shortages. Their handling capacity should scale from the buyer's army, logistics, and route network.

### Captured wartime stockpiles

A captured-stock provider must publish a receipt before the source country, battlefield record, or surrender state is lost.

The receipt states:

- equipment class and token
- available amount
- captor or custodian
- whether the stock is already assigned elsewhere
- expiry
- source country when known
- whether the buyer can learn the source

Event 57 does not estimate destroyed armies and create stock from nothing.

## Evolution II offer families

### Embargo-circumvention contracts

These offers give isolated countries a temporary, route-backed way to obtain fuel, equipment, convoys, or strategic industrial inputs.

The contract should be valuable during Event 50 or a condemnation-based embargo. It should lose value or become invalid when ordinary trade access is restored.

### Industrial procurement

HOI4 does not treat most strategic resources as a country stockpile. Industrial-material lots should therefore use supported temporary procurement effects. Steel, aluminum, rubber, tungsten, and chromium cannot be assumed to exist as stored country units.

A procurement package can provide:

- temporary access to a resource source
- a bounded reduction in a named shortage
- temporary local or national resource extraction support
- a route-backed production contract
- construction material for one defined project family
- an owner-provided industrial effect

The effect needs a duration, source proof, route requirement, and cleanup.

### Naval packages

Ships and naval assets use Event 56 or another owner-provided adapter.

Valid packages may include:

- convoys
- naval equipment tokens
- a transfer of specific ships when the engine and owner contract support it
- captured hulls
- naval design information
- mines, escorts, or invasion support through an owner effect

Event 57 must not invent a generic ship-transfer fallback. When a package cannot be transferred safely, it is unavailable.

### Experimental equipment

Experimental and unusual equipment appears only through the approved provider registry.

Possible owners include:

- Brilliant Scientist systems
- Alien Technology in Antarctica
- chemical and biological warfare systems
- special projects
- unusual vehicles or aircraft
- experimental submarines
- future event-owned weapons

An owner decides which package can be traded, at which evolution, in what quantity, and with what consequences.

## Evolution III offer families

### Exceptional stockpiles

These are very large, source-backed military packages from collapsing powers, surrendered depots, major surplus releases, or event-owned caches.

The amount is limited by:

- verified source quantity
- route handling capacity
- buyer storage and organizational capacity
- recent market imports
- one exceptional-lot cooldown

The event should permit a dramatic military change when the source and route justify it. It should not hand every minor country a major power's full arsenal without handling limits.

### Strategic intelligence

These packages can reveal important plans, networks, research direction, naval deployments, or mobilization windows.

They need a named target, a bounded duration, a strategic use, and strong Exposure.

### Complete technical dossiers

A complete dossier can grant one normal technology only when all of these are true:

- the owner or normal technology registry marks it tradeable
- the technology is compatible with the buyer's tree
- it does not create a mutually exclusive conflict
- the buyer does not already hold it
- the package has a verified source
- the current evolution permits it
- the buyer completes the delivery

Partial dossiers should normally give a research bonus or ahead-of-time reduction instead of the full technology.

The broad shared technology-union helper is not appropriate for one Black Market offer because it grants every compatible missing technology from a donor. Event 57 needs a bounded single-package contract.

### Rare owner packages

Evolution III can admit high-value assets such as special-project equipment, unusual weapons, event-owned technology, or unique intelligence.

Every package remains owner-controlled. Anything Has a Price is an access tier, not permission to bypass another system's lifecycle.

## Member surplus sales

Selling is a real stockpile transaction.

The member selects a supported sale family. The system calculates a saleable amount above a readiness reserve, presents the amount and credit return, then debits the source before publishing the lot.

A sale must fail closed when the debit cannot be proven.

### Dynamic readiness reserve

The reserve should consider:

- deployed army and air force
- active fronts
- war state
- mobilization plans
- current deficits
- fuel consumption
- convoy commitments
- trains and trucks required for supply
- equipment already reserved for another transaction
- recent market imports
- member posture

A country at or below its reserve cannot sell that category.

State Patronage can lower the safety margin, but it cannot reduce it to zero for essential equipment.

### Sale amount bands

The member can choose a Small, Medium, or Large sale when enough surplus exists.

The exact amounts are dynamic. A Large sale should represent a larger share of surplus and create more Exposure, not a fixed universal number.

### Source debit timing

The seller's stockpile is debited when the offer becomes committed for sale, not when the buyer receives it.

Possible transaction states are:

1. listed and not reserved
2. reserved by buyer
3. debited and dispatched
4. settled
5. canceled before debit
6. lost after debit

A seller cannot cancel after dispatch and recover the goods.

### Seller proceeds

The seller receives Market Credit only when the lot is reserved and the source debit succeeds.

A portion of the buyer's price becomes a network fee. Suggested starting seller yield is `60-80%` of the buyer's Market Credit price, modified by posture, scarcity, route risk, and broker role.

This spread is an important anti-arbitrage sink.

## Recently imported equipment lock

A buyer cannot immediately resell the same market cargo for profit.

Each completed purchase adds a category-level recent-import ledger amount. That amount is subtracted from the country's saleable surplus for a long lock period, suggested at `365` days.

The lock can reduce earlier when the equipment is demonstrably consumed or lost through an owner-supported receipt. It must not require scanning every individual item.

A recent-import lock follows the equipment category and transaction ID. Repeated purchases add to the locked amount without duplicating the receipt.

## Market Credit economy

### Sources

Valid credit sources include:

- verified equipment and fuel sales
- brokerage missions
- route service for another member
- intelligence contributions
- limited government underwriting
- a Grand Auction refund or settlement
- owner-approved event payments

### Government underwriting

A country with no saleable surplus needs a bounded way to enter the market.

A working decision family can commit civilian industrial capacity for `90-180` days in exchange for Market Credit. The amount scales from the country's economy and current credit cap. It has a long cooldown and increases Exposure under State Patronage.

Underwriting is not an unlimited credit exchange. It should not let a rich major buy the entire inventory every rotation.

### Credit cap

The cap should scale from:

- civilian and military factory total
- current evolution
- government posture
- completed settlements
- broker role

The implementation should use a floor and cap so small countries can participate while major countries cannot store limitless credit.

A transaction that would exceed the cap should show the payable amount before confirmation. Excess value can remain unsold or be converted into a smaller lot. It should not disappear after the player commits unknowingly.

### Credit on withdrawal and expulsion

- Voluntary withdrawal locks the remaining credit and settles a network fee.
- Dormancy preserves locked credit.
- Reconnection restores only the surviving balance.
- Suppression forfeits a larger share and can turn it into counter-smuggling resources.
- Expulsion freezes or confiscates the balance according to the betrayal outcome.
- Annexation does not transfer the credit automatically to the annexer.

## Pricing

Price should derive from equipment value, quantity, scarcity, source class, route risk, delivery time, and current evolution.

Useful price tendencies:

- member surplus is cheaper than a commissioned shortage lot
- collapsed-state and captured stock can be discounted
- embargo pressure creates a markup
- a dangerous route can lower the posted price while increasing expected loss and Exposure
- technical dossiers and intelligence use strategic value for pricing
- an exceptional lot includes a high network fee

The player sees the final Market Credit cost and all additional spendable costs. Internal valuation components stay in the tooltip only when they explain a material difference.

## Cost budget

A purchase or sale action can use at most four spendable cost types. Most offers should use two or three.

Typical purchase costs are:

- Market Credit
- one route-specific logistics cost, such as convoys, trains, trucks, fuel, or aircraft capacity
- an optional temporary civilian-factory burden for handling or concealment

Exposure is a consequence, not a spendable cost.

A route requirement such as controlling a port is a requirement, not a cost.

Every visible cost needs the correct texticon. Market Credit requires its own texticon before the decision can ship.

## Demand weighting

Inventory generation should respond to registered member demand.

Demand inputs include:

- equipment deficits
- fuel days
- convoy and train shortages
- current war
- planned invasions
- airbase and port capacity
- legal market access
- embargoes
- current offers
- recent purchases
- technology and equipment compatibility
- AI strategy

The global demand model can aggregate only active members. It does not need a world scan.

A baseline rotation should try to include at least one broadly useful logistics or small-arms lot when a valid source exists. It should not guarantee a reward when no source exists.

## Commissions

Evolution I unlocks a commission action.

A commission lets one member influence the next rotation toward one broad class, such as small arms, fuel, transport, armor, aircraft, intelligence, or industrial procurement.

It does not select an exact token or guarantee success.

The action uses Market Credit, has a cooldown, increases route pressure, and can fail when no valid source enters the registry.

A failed commission should refund part of the credit and explain that no supplier accepted the request. It must not generate fake stock to satisfy the player.

## Grand Auction

Evolution III unlocks a recurring Grand Auction mission for one exceptional lot.

The auction should occur at a long interval, suggested at `180-360` days, only when a valid exceptional provider package exists.

Members submit bids based on:

- Market Credit
- route handling capability
- strategic need
- Exposure tolerance
- government posture
- trust

The player receives the lot details, minimum handling requirement, bid cost, expected Exposure, and settlement date. Other bidder identities remain hidden.

The winner pays the committed bid and receives a delivery job. Losing bidders receive the documented refundable share after settlement. A bid cannot exceed the bidder's current credit or route capacity.

AI must not bid for prestige alone when it cannot use the cargo.

## Technology isolation

Receiving equipment never grants its technology.

Receiving a research bonus does not mark a source project complete.

Receiving an owner-approved special technology does not fire the source event, set the source event's completion flag, unlock unrelated source branches, or count as winning the source project.

The provider receipt must state which exact effect is allowed.

## Condemnation and dangerous packages

A chemical, biological, nuclear, atrocity-linked, or otherwise condemned package can appear only when its owner permits trade.

The provider must state:

- whether possession is public or hidden
- whether delivery creates condemnation
- whether use creates condemnation through the existing owner system
- whether a seizure exposes the buyer or seller
- whether special storage or equipment support is required

Event 57 does not create a second condemnation ledger. It calls the owning consequence path when the approved transaction requires it.

## Provider registry

The Black Market needs an event-owned public provider API so other events can offer packages without giving Event 57 ownership of their systems.

Suggested owner files:

- `common/scripted_effects/057_the_black_market_provider_effects.txt`
- `common/scripted_triggers/057_the_black_market_provider_triggers.txt`
- `docs/events/057_the_black_market/systems/provider_api.md`

The shared dynamic-effects registry can index this API for discovery. It should not copy the event-owned implementation.

## Provider package contract

Every package registers:

| Field | Required meaning |
| --- | --- |
| `provider_id` | Stable owning event or system |
| `package_id` | Stable package identity |
| `offer_class` | Equipment, fuel, intelligence, industrial, technology, naval, or special |
| `minimum_evolution` | Earliest allowed Event 57 evolution |
| `availability_trigger` | Source-world condition that must still be true |
| `buyer_trigger` | Countries allowed to receive it |
| `source_debit_effect` | Exact stockpile or owner-ledger debit |
| `delivery_effect` | Exact buyer effect after successful settlement |
| `quantity_rule` | Dynamic amount and bounds |
| `price_rule` | Market Credit valuation |
| `route_rule` | Supported route classes and capacity |
| `exposure_rule` | Expected transaction risk |
| `reveal_rule` | Evidence and public-consequence behavior |
| `completion_isolation` | Proof that source lifecycle remains unchanged |
| `DLC_rule` | No-DLC and enhanced paths |
| `cleanup_rule` | Invalidation, expiry, annexation, and duplication handling |

Missing required fields make the package unavailable.

## Request and receipt flow

A provider request should be versioned and fail closed.

Conceptual flow:

1. Event 57 submits a package request with a unique request ID.
2. The owner validates current availability and buyer eligibility.
3. The owner returns a bounded offer receipt.
4. Event 57 stores the receipt in one inventory slot.
5. Purchase reserves the receipt.
6. Dispatch calls the owner debit once.
7. Successful delivery calls the owner delivery effect once.
8. Settlement returns a final status to the owner.
9. Expiry or invalidation clears the request without changing the source system.

Public inputs and outputs should be reset after each call. A stale request must not be reused for a different buyer.

## Provider safety

The API must prevent:

- a missing source from creating goods
- the same source package being sold twice
- a buyer receiving an incompatible token
- a seller avoiding the debit
- Event 57 completing the source event
- an unapproved experimental package entering the pool
- a package remaining valid after its owner removes permission
- a DLC-only token appearing without its DLC
- a delivery effect firing twice after reload

## Event connection adapters

### Event 50: The Great Embargo

Event 50 publishes target and restriction pressure. Event 57 uses that proof to raise demand, mark embargo-circumvention offers, alter invitation scoring, and create the related Chaos milestone after a successful delivery.

Event 57 does not remove the embargo.

### Event 54: Gift from Scientists

Event 54 can move advanced normal technology into world circulation earlier. Event 57 can then find equipment produced by countries that possess those technologies.

Event 54 does not automatically create a Black Market lot. A country or owner still needs to publish real equipment or a technical package.

### Event 55: The Great Infrastructure Project

Event 55 can publish ports, railways, highways, tunnels, bridges, and trade corridors as route assets.

Event 57 reads the route receipt and leaves project ownership with Event 55.

### Event 56: The Navy

Event 56 can publish convoys, captured naval assets, unusual naval equipment, or supported ship-transfer packages.

Event 57 accepts only packages that Event 56 marks tradeable and safe.

### Wars, occupations, and collapse

War and surrender systems can publish captured or abandoned stock before their source records disappear.

Event 57 does not infer exact equipment from casualties, deaths, annexation, or a country ceasing to exist.

## International market distinction

Where the Arms Against Tyranny international market is available, the Black Market remains separate.

The legal market is public and follows legal access, seller visibility, and ordinary restrictions. The Black Market uses invitation-only membership, Market Credit, hidden source classes, route jobs, Exposure, seizures, and owner approvals.

The DLC path may reuse verified valuation or equipment-compatibility logic when safe. It must not expose Black Market offers on the legal market or require the DLC for Event 57's core loop.

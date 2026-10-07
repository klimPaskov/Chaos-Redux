# Greenland Sale: purchasing power and payment

## What a bid buys with

The auction uses one event-owned Industrial Reserve.
This is accumulated civilian construction capacity that a government has deliberately set aside, not an invented national treasury with free opening balances.
Its working display unit is one unmodified civilian-factory day.
One usable civilian factory committed for one full day earns one reserve point.
The final localisation should explain the economic meaning without expecting the player to understand an internal resource name.

The reserve is the chosen DLC-neutral economic design for this specification.
It is separate from the International Market's economic-capacity bank.
Existing native market funds are neither copied into it nor silently spent by it.
The implementation must prove the factory reservation and construction-redemption interfaces before treating this design as implemented.
The evidence and native-bank alternative are recorded in the planning handoff, rather than disguised as already verified engine behavior.

Industrial Reserve has two uses throughout the event's life.
It can fund territorial bids, and it can pay for eligible construction in the holder's own territory.
A seller therefore receives the same usable economic resource that the buyer surrendered.
A losing bidder is not left holding an unusable event token after the auction ends.

## Producing a reserve

A country may assign a light, medium, or heavy commitment of 1, 5, or 10 available civilian factories.
These are selections within one allocation action, not three separate permanent decision families.
Larger economies may scale the commitment through additional whole 5-factory steps when their available industry supports it.
A small country must retain the ability to commit a single factory.

Only capacity actually withheld from other civilian construction earns points.
Factories already tied up in consumer goods, trade, other event projects, or a separate industrial commitment cannot back this reserve a second time.
Destroyed, occupied, unavailable, or merely promised factories earn nothing.
A commitment that becomes only partly supportable earns the supported amount and shows the reduced rate.
It never continues to earn its original nominal rate because a modifier is still present.

The economic unit measures base factory-days.
Construction-speed bonuses do not create additional reserve points.
A highly efficient builder consequently gives up more ordinary construction by diverting the same number of factories, which is a real opportunity cost rather than an extra auction subsidy.
The reserve does not receive passive interest or an event-firing endowment.

Countries may lower or stop an allocation without losing previously earned points.
Switching allocation is immediate for future production, with already accrued production settled only once.
A save and reload, repeated cancellation, or an interrupted fraction of a day cannot duplicate that day's earnings.
Unused fractional production may be retained internally, but public bids and construction payments use whole quoted amounts.

The default AI funds a particular intended bid and then stops at its chosen target.
It does not permanently divert construction just because the market exists.
A player may retain a reserve for later opportunities, but the interface must make the lost construction capacity clear.

## Why bidding uses escrow

A funded bid moves value out of the bidder's freely spendable reserve into the lot's escrow.
The amount remains attributable to that bidder until an outbid, a valid refund, or settlement.
The seller cannot spend it while the auction is open.
The buyer cannot use it to finance a construction project or lead another auction.

Two simultaneous auctions are therefore competing uses of the same purchasing power.
A country leading one lot may still bid on another, but only with its remaining uncommitted reserve.
Its displayed total wealth must not imply that the same points are available twice.
There is no installment debt, promised future factory lease, or post-purchase repayment schedule in the baseline design.

When a challenger bids, the challenger must be able to fund the entire new bid before the previous leader's escrow is released.
The previous leader receives exactly what it paid.
No refund is calculated from the current price, the minimum next offer, a later discount, or the value of Greenland after a resource discovery.
A refund can succeed once only.

## The buyer and seller at closing

A completed auction exchanges the lot for its committed principal.
The seller receives exactly that principal and the buyer's escrow becomes spent.
If the winning bid is 450 points, the transfer creates a 450-point seller receipt and extinguishes the corresponding 450-point escrow.
It does not also subtract 450 points from the buyer's free reserve.

The seller receipt is unrestricted Industrial Reserve, subject to the same construction and bidding rules as other funds.
It can rebuild ports at home, finance new mainland industry, strengthen an existing border, or serve as purchasing power in a later auction.
The event does not decide that every seller should receive the same temporary construction-speed bonus regardless of the price paid.

This direct exchange is deliberately independent of the buyer's economy at closing.
A buyer that loses factories after funding its bid has already paid the economic cost.
Its loss of future production alone does not invalidate a valid escrow.
Country disappearance, hostile relations with the seller, or inability to take ownership are different problems and invoke cancellation rules.

## Using proceeds for construction

A country can redeem its freely available reserve for a complete, currently legal construction increment in an owned and controlled state.
The eligible menu is ordinary buildings and infrastructure that the country could presently construct under its technology, state capacity, coastal geography, and applicable game rules.
It cannot purchase a secret project, unavailable building, extra building slot, new resource deposit, or a free technology by relabeling it as public works.

The quoted price is the selected increment's current base construction work divided by the game's base daily output of a civilian factory, rounded upward to the common 5-point payment quantum.
This is a design formula, not a claim about the current numeric values of vanilla construction constants.
The implementation must obtain those inputs from the installed game and preserve their units.
Country-specific construction-speed bonuses do not discount this redemption price, just as they did not increase reserve production.

A completed increment may be a civilian factory, military factory, dockyard, infrastructure level, port level, airfield level, or another eligible ordinary construction type.
The state and province selection must obey the same restrictions that make the corresponding native building legal.
A country chooses one clear project at a time through a target-and-project selection, rather than a permanently visible list of every building in every state.

The payment creates only the increment actually delivered.
A queued native project for the same increment must not be duplicated or silently replaced.
Insufficient space, changed ownership, a lost coast, a new construction restriction, or a changed quote prevents the action from spending anything.
Where an engine operation produces a partial result unexpectedly, the receipt must distinguish delivered value from undelivered value rather than claim a full project succeeded.

Small receipts remain banked until they can fund a legal increment, and can be combined with later earned points or sale proceeds.
The final interface should show at least one affordable use when one exists, or the remaining amount needed for a selected legal project.
There is no compulsory conversion into political power to dispose of a small balance.

Receipt-backed construction retains enough provenance to establish which sale's proceeds actually paid for the delivered work.
The active homeland-reconstruction receipt has priority for qualifying construction, followed by other sale receipts and ordinary earned reserve.
One point of reserve can support one delivered unit of construction only and cannot satisfy several independent receipt-spending claims.
Moving a receipt's value into a bid does not count as reinvestment in construction, and an outbid refund restores only the value and provenance actually committed.

## Discounts and the exchange principal

The price of a territorial transfer is the competitive principal between two countries.
It is not an administrative decision fee.
Black Friday or another universal discount must not let a buyer pay half an accepted bid while the seller receives the full price from nowhere.
It must also not alter a funded bid retroactively or reduce a refund below the actual deposit.

The baseline treats auction principal, reserve production, and reserve-backed redemption as an exchange and production loop outside ordinary discretionary purchase discounts.
This classification must be explicit in the shared cost-surface register.
The exclusion prevents one government from earning industrial credit, receiving a discounted redemption, and immediately turning the extra construction into a systematically subsidized reserve cycle.
A later change to discount eligibility requires a complete conservation and balance review, rather than an automatic application of an all-family mask.

The shared transaction framework remains useful for the common principles of actual-paid receipts, one-time refunds, affordability parity, and completed settlement.
An unsupported reserve component requires its own proven payment and refund adapter.
Reusing the framework's name does not prove that the adapter exists.

## Interrupted governments and terminal cleanup

An auction does not transfer escrow to a conqueror merely because the conqueror has annexed the bidder.
It also does not credit a dead tag and hope that the money will become meaningful later.
When an established shared state-succession system supplies an explicit successor for financial obligations, that system may receive the refund once under its own rules.
Without such a supported successor, the escrow is recorded as an unrecoverable loss of the abolished government.
The seller is not paid and no new claimant is invented.

A completed seller receipt belongs to the seller's country and subsequently follows whatever succession rules already govern that country's event resources.
The auction does not retroactively reverse a completed sale because the seller later loses a war.
Likewise, a buyer's later defeat is handled by ordinary territorial changes rather than by a hidden repossession clause.

Event disablement closes outstanding auctions and returns still-refundable escrow before removing their display.
It stops new reserve production commitments and returns the actual civilian capacity being reserved.
Unspent reserve must retain a construction-redemption path, or be settled through a proven equivalent before the event's economic interface is removed.
Disabling an event is not permission to confiscate accumulated player value.

## What economic validation must establish

At every point, free reserve, committed escrow, delivered construction value, and explicit losses have an understandable source.
Funding is the only baseline creation route.
A bid moves value, an outbid moves it back, a sale moves it to another country, and construction redemption consumes it for a measured result.
The economy cannot depend on an unobserved factory, a repeated callback, a duplicated refund, or an assumed atomic transfer.

The core economic loop must work with and without DLC and on a save that has never used the native equipment market.
Until those requirements are proven, the payment design remains a specified acceptance target rather than a verified engine feature.
The implementation must report the failed interface directly instead of replacing the auction with a fixed political-power price or giving participants free reserve.

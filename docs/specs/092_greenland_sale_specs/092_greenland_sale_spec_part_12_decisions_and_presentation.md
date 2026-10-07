# Greenland Sale: following the auction

## One market category

The player uses a single event-owned decision category for the founding auction, later listings, purchasing reserve, and relevant reconstruction follow-through.
The category should feel like a territorial auction desk inside the existing game rather than a separate economic simulator.
A static category picture provides its visual identity.
Native decision, mission, tooltip, and map-targeting surfaces carry the actual interaction.

Only the selected or actively followed lot needs to be expanded in detail.
Other active lots can show a compact identity, seller, status, and a way to inspect them.
The player should not be forced to read three full state dossiers whenever it opens the decisions interface.
A country with no active interest can dismiss routine updates while retaining access to the public market.

The category remains accessible while the country has usable reserve or an outstanding economic obligation, even when no auction is active.
A dormant market with no reserve, relevant mission, or active lot does not need to occupy permanent screen space.
The opening news and event details preserve the ability to understand what happened earlier.

## The four value families

The recurring auction display has four numeric value families: the current bid, the next acceptable bid, the country's free purchasing reserve, and time remaining.
The bidder and seller are identities, and the lot is a set of named states.
A leading country's committed amount is the displayed current bid rather than a second escrow meter.
Its total historical income, hidden AI ceiling, valuation component scores, seller desperation, and market reputation are not additional persistent gauges.

The inspection and no-bid periods use the same time-remaining role before a high bid exists.
The current-bid role then shows that no bid has yet been accepted, and the next-price role shows the opening reserve.
The interface must not show a fictitious high bidder with a zero-valued funded offer.

The Industrial Reserve allocation selector explains its native factory commitment and production rate when the player manages that allocation.
Those costs should not become a permanent fifth economy dashboard.
Reconstruction objectives use the same money and deadline concepts, with clear completion conditions and project status rather than a new political-credit currency or progress score.

## Before and during a bid

The ordinary buyer's useful actions are to inspect or follow a lot, allocate reserve production, make the next bid, and redeem uncommitted reserve for construction.
Making a bid disappears or becomes clearly unavailable when the country is already the leader, the opening period has not begun, the quote is unaffordable, or a transaction restriction prevents participation.
The reason must be visible rather than hidden behind an apparently broken button.

Bid confirmation states the actual amount, the lot, the current seller, and the consequence of becoming the funded leader.
It explains that another country's higher bid refunds the deposit and restarts the full closing period.
It also explains that the leader cannot voluntarily cancel its own accepted offer.
The player should not discover those rules only after spending its reserve.

A stale quote does not debit a different amount.
The changed price is presented for a new decision.
A country that becomes unaffordable between display and execution receives an honest refusal with no clock change and no partial bid.
The same boundary applies to the native action's availability and its actual payment.

## Preparing a sale

The seller's useful actions are to prepare or edit one candidate, inspect the exact lot and retained country, select a reserve posture, and publish or withdraw the draft.
State selection should use an appropriate native targeted-decision or map-selection flow rather than a new screen full of free-form state identifiers.
Regional selection exposes connected additions and removals without showing an action for every possible subset of the empire.

The preview makes the proposed state's economic role, core status, strategic importance, and protected remainder understandable.
For subject sellers, it also shows whether overlord authorization is outstanding.
For homeland sellers, it identifies the political cost and achievable reconstruction objective before publication.
The actual published conditions must match that preview.

After publication, the seller manages its wider strategy rather than editing or voluntarily withdrawing the bargain.
It cannot withdraw the lot, raise the reserve, substitute a state, or change the eligible winner after seeing the contest.
A valid external cancellation is explained as such and remains distinct from an unsold outcome.

## The missions that deserve a timer

The auction has one active phase clock per published lot.
Inspection, the first-bid window, and the high-bid closing period are successive uses of that clock, not three overlapping missions that the player must reconcile.
Only the selected lot's detailed mission needs expansion.
Other active auctions remain inspectable without flooding the interface.

A completed homeland sale can create one domestic-reconstruction mission for its seller.
Its fixed objective and 90-day deadline come from Part 09.
The player sees what qualifying construction remains and whether completed work has satisfied the pledged value.
There is no separate repetitive post-purchase mission attached to every ordinary island, colony, and port.

The reconstruction mission resolves as success, expired, or externally interrupted.
It does not imply that a canceled mission returned land or that an expired one erased the seller's remaining reserve.
The explanation connects the objective to the actual territorial sacrifice and the promised use of its proceeds.

## Notification discipline

The founding publication is globally noteworthy.
A player controlling the seller receives the appropriate role context, and prospective buyers receive a way to inspect the auction.
The game should not require every country to accept a popup merely to become legally eligible to bid.
Eligibility is a property of the country and lot, not a flag granted only by dismissing an offer event.

Outbid notifications go to the affected player and identify the refund, new leader, and new closing period.
Observers receive them only when they explicitly follow that lot.
Routine AI increases are not global news.
A completed founding, major regional, strategic, or homeland sale receives the appropriate level of public result, while a small routine outpost sale can remain a market update.

There is one successful result for one sale.
A regional lot does not send a separate sold event for every state.
A generic news handler and an event-specific handler must not duplicate the same announcement.
No-bid results are distinct from invalidated lots, and both are distinct from a completed purchase.

## Event details and history

Event Details explains the original Greenland premise, the funded-bid rule, the ordinary closing process, and the four evolved permissions.
It also explains that the random event is fire-once while later market activity can continue.
A disabled stage is shown honestly as disabled rather than advertised as an available action.

The history of a lot records its publication, completed sale or terminal failure, final seller and buyer where relevant, territory, and actual price.
Individual bid changes remain local auction information rather than separate global-event history entries.
Evolution history records actual capability activation and does not treat inspection or settlement as additional stages.
The participant named in a historical record must be the actor in that record, not a stale country target inherited from another event.

## Localisation direction

All player-facing names, descriptions, option text, tooltip prose, and achievement titles remain a writing handoff.
Working role labels in these specifications identify purpose and are not approved final localisation.
The text should be specific to the seller, buyer, territory, stakes, and outcome that actually occurred.

The opening can find humor in officials pricing an Arctic possession, governments discovering an unexpected appetite for distant real estate, and bureaucratic confidence in an uncertain bargain.
The humor should target the transaction and the governments, not imply that the residents are saleable objects or that a colonial population is automatically pleased with its new owner.
Later homeland-sale text should carry the political weight of a government disposing of part of its own country.

Every report must distinguish a whole Greenland sale from a partial holding, a sale from a lease, a funded bid from an accepted purchase, and ownership from military access.
Avoid a historical country's name where the current actor can differ.
Avoid a promised benefit such as new ports or resources when the actual lot contains none.
A dynamic description should be truthful before it is clever.

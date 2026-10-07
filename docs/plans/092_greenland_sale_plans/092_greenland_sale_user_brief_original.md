# Greenland Sale

## Catalog entry

- Event ID: `092`
- Event name: Greenland Sale
- Type: Minor Fire-Once
- Status: To Be Reworked
- Chaos level: 1
- Cluster: None

## Core idea

> Greenland is suddenly put up for sale and countries across the world can bid for it.

The current owner of Greenland becomes the seller.

Every valid country can enter the auction.

The highest bid must remain unbeaten for about **10 days**.

If another country raises the bid, the countdown resets for the new highest bidder.

If nobody raises the bid before the countdown ends, Greenland is sold to the current highest bidder.

There is no predetermined winner.

## Baseline auction

The auction begins with Greenland as the only lot.

The current bid, bidder, and required next bid are calculated dynamically.

Bids should reflect both the value of Greenland and what each bidder can realistically afford.

Important influences can include:

- the bidder's economy
- Greenland's current industry and resources
- Greenland's strategic position
- nearby bases and sea access
- existing claims or regional interests
- current wars and rivalries
- how badly the bidder wants another Arctic or Atlantic position

A country can keep raising the bid while it still considers the purchase worthwhile.

AI countries should stop when the next bid is no longer worth the cost to them.

The player can choose whether to enter the auction and whether to continue raising the bid.

## Dynamic price

There is no fixed Greenland price.

The value is calculated from the current campaign state.

A heavily developed Greenland should cost much more than an undeveloped Greenland.

If other events have added factories, resources, infrastructure, ports, airbases, or other important value to Greenland, the auction should reflect that.

The winning bid should create a meaningful economic cost for the buyer and a corresponding benefit for the seller.

The full planning pass should determine the best Hearts of Iron IV systems for representing that transaction.

## Ownership changes

The auction always uses Greenland's actual current owner.

If Greenland has already changed hands before Event 092 fires, the new owner sells it.

The event should not assume Denmark still controls Greenland.

If Greenland has been divided between several countries, the planning pass should decide the cleanest way to treat the remaining Greenland territory without forcing a historical setup.

## No-bid outcome

If nobody is willing or able to bid, Greenland remains with its current owner and the auction ends without a sale.

## Evolution I: Overseas Auctions

- Chaos requirement: `200+`.

The Greenland sale creates a precedent.

Other countries can begin putting distant overseas possessions up for sale.

Possible lots can include:

- islands
- remote overseas states
- isolated enclaves
- distant possessions that are expensive to defend

The available territories are selected dynamically from the current map.

## Evolution II: Colonial Markets

- Chaos requirement: `400+`.

Larger colonial regions and groups of connected overseas states can be sold as one lot.

The size of the lot depends on the live geography and ownership rather than a fixed number of states.

Countries with large colonial empires can therefore sell much more valuable territory.

## Evolution III: Strategic Auctions

- Chaos requirement: `600+`.

Strategically important territory can enter the market.

Possible lots can include:

- major islands
- naval chokepoints
- resource regions
- important ports
- military staging areas
- valuable enclaves

Competition can become much more aggressive because some territories are worth far more for their position than for their economy.

## Evolution IV: Everything Has a Price

- Chaos requirement: `800+`.

Even parts of a country's own homeland can be offered for sale.

Countries under severe pressure become more willing to sell territory they would normally never consider giving up.

Core territory should remain much harder to sell than distant possessions, but it is no longer impossible.

A country should never be able to sell itself completely out of existence.

## Repeat auction behavior

After the Greenland sale establishes the system, evolved auctions can continue placing new territories on the market.

Only a limited number of auctions should be active at once so the event remains easy to follow.

Every new lot uses the same basic rule:

> The highest bid wins if nobody raises it before the countdown ends.

## Connections

**World Claims** can make countries more interested in buying territory they already claim.

**Independence Wave** and other liberation events can change which territories still belong to an empire and therefore what can later be sold.

Economic and resource events can make a territory much more or less valuable before it reaches auction.

## Your Task

Create the full specs and expand the idea thoroughly using the full planning skill, all the other skills, and provided subagents. Before writing the specs, fully and thoroughly read and process all required project source files and must-read skill files. If you are unable to fully read every file, then say so directly and be honest in your final output. If you simplified or truncated things for a quicker output then also be honest about it.

# Smuggling Routes and Network Growth

## Route graph

The market is modeled as a sparse graph.

- Members and approved intermediaries are nodes.
- Smuggling routes are edges.
- Regional cells are connected components.
- A delivery must name one valid path through the graph.

The network can have several disconnected regional cells. These cells do not share full inventory or membership until an interregional route joins them.

Each route record stores:

- stable route ID
- route type
- origin member or broker
- destination member
- optional intermediary
- endpoint states or ports when relevant
- current status
- hidden capacity
- hidden reliability
- current route pressure
- current investigation owner when one exists
- supported cargo classes
- evolution requirement
- creation and latest refresh dates
- active delivery count
- one-time regional connection receipts

Capacity and reliability remain internal. The member sees a simple status, supported cargo class, current delivery time band, and current risk class.

## Public route states

| State | Meaning | Member consequence |
| --- | --- | --- |
| Open | The path can accept normal cargo | Normal offers and delivery timing |
| Strained | War, shortage, or scrutiny reduces throughput | Smaller lots, higher costs, longer deliveries |
| Disrupted | One endpoint or segment is temporarily unusable | No new dispatch, repair action available |
| Compromised | An observer holds evidence against the route | Severe seizure risk and Exposure pressure |
| Burned | The route was dismantled and cannot be reopened through ordinary repair | A new route proof is required |

A route cannot be both Open and Compromised as two independent flags. Compromised is a status with its own restrictions.

## Route families

### Land border route

A land route uses a direct border or a verified controlled corridor between the participating countries.

Useful factors:

- direct adjacency
- terrain and weather
- railway connection
- infrastructure
- state control
- resistance and compliance
- front-line proximity
- trucks and trains
- enemy occupation
- local intelligence pressure

Land routes are the safest baseline path when the border is stable. A front-line route can carry urgent cargo, but it should have lower capacity and higher seizure risk.

The route can be disrupted by loss of the endpoint state, a new hostile controller, railway destruction, a sealed border, or an active counter-smuggling operation.

### Neutral intermediary route

A neutral country or territory can relay goods without becoming a full member.

The intermediary needs a reason to cooperate, such as:

- commercial access
- corrupt officials
- currency arbitrage
- intelligence sponsorship
- political neutrality
- a large port or rail junction
- previous smuggling memory
- diplomatic access to both endpoints

The intermediary does not receive the member category. It can gain hidden route-host status and local evidence risk.

A neutral relay should be vulnerable to diplomatic pressure, sanctions, government change, war entry, and counterintelligence.

### Port and merchant-shipping route

A maritime route requires usable ports and a supported shipping connection.

Useful factors:

- port level and control
- convoy availability
- fuel
- naval supremacy and enemy raiding
- blockade or embargo
- distance
- access to neutral ports
- occupation status
- Event 55 corridor and port improvements
- Event 56 naval escorts or surplus convoys

Maritime routes can move larger cargo than improvised land crossings, but blockades and intelligence scrutiny can make them unstable.

A purchase that uses this route can require convoys and fuel as logistics costs. The route itself should not destroy convoys on every clean delivery. Convoy loss belongs to a failed or partially intercepted outcome.

### Occupied-territory corridor

An occupied route uses controlled foreign territory, collaborators, resistance channels, captured depots, or military transport offices.

Useful factors:

- controller and owner
- compliance
- resistance
- garrison strength
- military access
- current front
- local railways and supply hubs
- intelligence network strength

This route can be profitable because official records are already confused. It is also vulnerable to partisan action, occupation changes, and military investigations.

The route should not treat civilian harm as a direct Black Market effect. Any deaths, repression, or forced movement caused by a connected event remain owned by their existing systems.

### International corridor route

Event 55 can publish a route package for major railways, highways, tunnels, bridges, ports, and trade corridors.

A published corridor can:

- increase route capacity
- reduce delivery time
- connect otherwise distant members
- create a new intermediary node
- make a route more valuable to investigators

Event 57 reads only the approved corridor receipt. It does not inspect or take ownership of Event 55's project ledger.

### Covert air route

A covert air route is an emergency or evolved option.

It requires:

- suitable airbases
- aircraft or an owner-approved transport package
- fuel
- range
- a route that is not fully covered by hostile air control
- Evolution II or an explicit event-owned exception

Air routes deliver small, valuable cargo quickly. They are poor choices for bulk tanks, large fuel reserves, or major industrial shipments.

The route should carry high Exposure and severe loss risk. It exists for urgent equipment, intelligence, technical files, and small special packages.

## Route creation

A route can be created through:

- the founding transaction
- a successful invitation
- a member decision
- a route-repair mission
- an Event 55 corridor receipt
- an Event 56 convoy or escort package
- an owner-provided special route adapter
- a successful reconstruction pulse

Every creation requires endpoint proof and a stable route ID. Repeated calls must return the existing valid route or replace a proven obsolete record. They must not create duplicate parallel copies of the same route by accident.

## Route-opening missions

The following are working mission families.

### Secure a Land Crossing

The member commits trucks, trains, equipment, and local security to one named border or corridor.

The objective should depend on real state control, rail access, and unit or security presence. It should not auto-complete from a passive stockpile condition alone.

Suggested duration is `90-150` days, modified by terrain, war, infrastructure, and local control.

Success creates or upgrades the route. Failure increases Exposure, consumes part of the committed logistics, and can create outsider evidence.

### Charter Neutral Freight

The member builds a relay through a neutral commercial partner.

Requirements can include relations, port access, convoys, Market Credit, and a valid intermediary. The mission should be longer when the intermediary is ideologically distant, under pressure, or far from the endpoints.

Success creates a neutral relay. Failure can expose the intermediary without proving the full membership chain.

### Compromise a Port Authority

The member places brokers, dock officials, and shipping agents inside one port.

The action uses intelligence capacity, Market Credit, and a temporary civilian or convoy burden. It should be unavailable when the member has no route to the port.

Success creates a maritime endpoint. Failure can raise local investigation pressure and close the port to further attempts for a long cooldown.

### Reopen the Corridor

This mission repairs a Strained or Disrupted route.

The objective can require control of named states, restored railway access, a minimum supplied unit presence, or a logistics commitment. It should not be a simple political power payment.

### Emergency Air Bridge

This evolved mission opens one short-lived air route for a named delivery or invitation.

It uses fuel, aircraft or air capacity, and Market Credit. It carries a public Extreme risk class and cannot become the normal cheapest route.

## Route selection for a delivery

A delivery chooses a path after purchase validation.

Selection should consider:

- whether the path supports the cargo class
- capacity relative to lot size
- expected delivery time
- current reliability
- buyer and seller hostility
- embargo and blockade state
- logistics the buyer can provide
- Exposure impact
- active investigation
- current number of deliveries on the path

The player sees the selected route family, time band, risk class, and important reasons. The exact hidden chance is not shown.

A player can pay for a safer available route when more than one valid path exists. This is a route choice, not a direct purchase of success.

## Delivery timing

Suggested starting bands:

| Route | Small cargo | Medium cargo | Large cargo |
| --- | ---: | ---: | ---: |
| Land border | `25-50` days | `40-75` days | `60-110` days |
| Neutral relay | `45-80` days | `70-120` days | `100-160` days |
| Maritime | `40-75` days | `65-120` days | `90-180` days |
| Occupied corridor | `35-70` days | `60-110` days | `90-150` days |
| International corridor | `20-45` days | `35-70` days | `55-100` days |
| Covert air | `10-25` days | `20-45` days | Not normally valid |

Final duration is dynamic. Distance, infrastructure, port strength, war, blockade, route pressure, evolution, cargo class, and government posture should modify it.

## Delivery capacity

Capacity controls the largest offer that can use the route.

It should be derived from:

- route family
- endpoint infrastructure or ports
- member posture
- current evolution
- logistics commitment
- convoy, train, truck, fuel, and aircraft availability
- route pressure
- active deliveries

Capacity is not displayed as another number. The offer tooltip states whether the current route can handle Small, Medium, Large, or Exceptional cargo.

## Route disruption

A route can be marked for refresh by:

- war declaration
- peace or armistice
- state-controller change
- annexation
- capitulation
- port loss
- blockade
- embargo activation or removal
- faction change
- corridor completion or destruction
- member posture change
- investigation outcome
- exposure breach
- active delivery result

The event-owned refresh processes only affected routes.

A route that loses one temporary condition becomes Disrupted. A route whose endpoint no longer exists or whose intermediary permanently rejects cooperation becomes Burned.

## Route pressure

Route pressure is an internal value that combines traffic, scrutiny, blockade, war, and recent failures.

It affects reliability and delivery time. It should not be exposed as a fourth public meter.

Pressure rises through:

- several deliveries in a short period
- large cargo
- repeated use of one intermediary
- high member Exposure
- hostile naval or air control
- sanctions
- an active investigation

Pressure falls during quiet periods, after route investment, or when traffic shifts to another path.

Quiet-period recovery can run through a bounded route pulse over the registered route array.

## Transaction outcomes

A delivery can resolve in five main ways.

### Clean delivery

The buyer receives the full reserved package. The transaction receipt is settled. Exposure changes by the stated amount. Network Reach grows according to lot size and novelty.

### Delayed delivery

The cargo remains in transit. The mission extends once, route pressure rises, and the buyer can accept the delay, pay for rerouting, or abandon the package under the stated refund rules.

A delivery cannot be delayed forever. A second failure must resolve as partial loss, seizure, cancellation, or a route-specific final outcome.

### Partial delivery

The buyer receives a bounded share of the reserved package. The source remains fully debited because the missing cargo was lost or seized. Exposure and route pressure rise.

The player sees the delivered amount and lost amount.

### Seizure

The buyer receives no ordinary cargo. The observer gains an evidence receipt. The route becomes Compromised or Burned. Credit refund depends on whether the seller, broker, or buyer caused the failure.

A seizure can transfer part of the cargo to the seizing country only when the engine and transaction record support a clear captured-stockpile result. It must not duplicate the package.

### Sting or betrayal

This rare result requires Counterintelligence Penetration, mature evidence, or a proven hostile broker.

The buyer, seller, or intermediary may lose credit, contacts, or route access. One side gains evidence. The outcome never publishes the complete network.

## Exposure changes

Exposure should respond to actions, not drift without explanation.

Suggested starting bands:

| Action | Exposure change |
| --- | ---: |
| Small clean purchase | `+1` to `+3` |
| Medium clean purchase | `+2` to `+5` |
| Large or exceptional purchase | `+4` to `+9` |
| Verified sale | `+1` to `+5` |
| Neutral relay opening | `+2` to `+6` |
| Covert air delivery | `+6` to `+12` |
| Delayed delivery | additional `+2` to `+5` |
| Partial delivery | additional `+5` to `+10` |
| Seizure | `+10` to `+25` |
| Successful cover cleanup | `-4` to `-12` |
| Quiet registered-member pulse | `-1` to `-5` |

Posture, route type, cargo class, current investigation, war, and intelligence state modify these anchors.

At Exposure `100`, a breach incident must resolve before the value can rise again. The incident should reduce Exposure to a post-breach band so the member does not remain permanently locked at `100`.

## Network Reach changes

Suggested starting contributions:

| Outcome | Reach change |
| --- | ---: |
| Small clean delivery | `+1` |
| Medium clean delivery | `+2` |
| Large clean delivery | `+3` |
| Exceptional or first-of-class delivery | `+4` |
| New active member | `+2` |
| Reconnected lost member with restored route | `+1` |
| First route into a new region | `+5` |
| First connection between two regional cells | `+5` |
| Route upgraded to a higher cargo class | `+1` |
| Delayed delivery | `0` |
| Partial delivery | `0` or `-1` |
| Seizure | `-2` to `-5` |
| Route burned | `-3` |
| Member expelled | `-2` |
| Regional cell dismantled | `-5` to `-10` |

The same transaction cannot award Reach for several labels that describe the same fact. A first interregional connection can award its one-time route milestone plus the ordinary delivery value only when a real delivery also completed.

## Regional cells

A regional cell is a connected set of active routes and members.

The system should track:

- cell ID
- member count
- route count
- regions represented
- access to ports, land corridors, and air routes
- highest supported cargo class
- active investigations
- whether it is connected to another cell

Cell identity is internal. Members can receive a qualitative regional status without seeing the full graph.

## Joining cells

Evolution I makes deliberate interregional connection more likely.

A connection requires:

- two live cells
- one shared intermediary, corridor, maritime path, or air route
- enough Network Reach
- no unresolved breach at the endpoints
- route capacity for at least one medium cargo

The first completed connection creates one event-owned Chaos milestone described in the evolution and Chaos specification. The mere creation of a route proposal changes no Chaos.

## Dormancy and reconstruction

When a cell loses every active route, its members become dormant or former according to their local state.

Reconstruction can use:

- a surviving former member
- a known intermediary
- an Event 55 corridor
- a port that changed hands
- a new war or embargo
- a successful route-opening mission
- an invitation from another active cell

The reconstruction pulse should have a long base interval, such as `240-480` days, and should commit only one route attempt at a time.

## Full dismantling

A mature network cannot be dismantled by destroying one route.

Full dismantling requires a sequence of local victories that removes the network's ability to settle accounts and rebuild:

1. Active cells are reduced to zero.
2. No delivery remains in transit.
3. At least one high-confidence clearinghouse or broker-chain case succeeds.
4. Network Reach falls below the dismantling threshold.
5. A final event-owned dismantling effect clears reconstruction eligibility.

The full dismantling outcome is intentionally difficult. It creates a one-time negative Chaos source and a permanent history state.

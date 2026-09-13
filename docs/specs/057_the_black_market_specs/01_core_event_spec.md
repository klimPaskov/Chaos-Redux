# Event 57: The Black Market

## Catalog entry

- Event ID: `57`
- Event name: The Black Market
- Type: Minor Fire-Once
- Status: To Be Reworked
- Chaos level: `1`
- Cluster: Positive Economy
- Cluster role: High member

## Playable promise

The Black Market creates a secret international economy that can move restricted military and industrial goods between countries that ordinary diplomacy keeps apart.

The event should make shortages, surplus stockpiles, blockades, neutral routes, captured equipment, intelligence contacts, corrupt officials, and foreign wars matter in a new way. A member can solve a dangerous shortage or turn useless surplus into influence, but every transaction depends on a physical route and increases the chance that governments, customs services, or intelligence agencies find part of the network.

The market must feel alive after its first event. Membership changes. Regional cells connect or break apart. Offers rotate. A route can become strained, compromised, or unusable. A member can tolerate the network, sponsor it, penetrate it, or destroy its local section. The strongest goods appear only after the network earns wider reach and the required evolutions become active.

The market is distinct from the legal international market. It uses separate rules, separate membership, separate currency, delayed deliveries, uncertain provenance, route risk, seizures, and compartmentalized knowledge. War, ideology, faction membership, hostility, and embargoes can lower trust or close particular routes, but none of them is an automatic transaction ban when a working underground path exists.

## First firing

The canonical entry is `chaosx.nr57.1`.

The entry event performs one bounded founding transaction:

1. It identifies a valid broker country.
2. It builds a connected founding cell around that broker.
3. It creates the first smuggling routes.
4. It sends private invitations to the selected governments.
5. It creates the persistent event-owned runtime.
6. It records Event 57 once in the shared event history without publishing the founders.

The target founding group is three countries. Two countries are permitted when the world state cannot support a connected three-country cell. Four countries are permitted when one additional country is required to bridge two otherwise valid route segments. The first firing must never create more than four members.

A valid founding cell requires at least one proven route between every member and the connected component. The graph can use one broker linked to two endpoints. Every founder does not need a direct route to every other founder.

The event is unavailable when fewer than two eligible ordinary countries can form a route-backed cell. Normal manual firing retains that requirement. Force Trigger Mode may bypass the event's Chaos level and selection state, but it must not create invalid countries, nonexistent ports, false borders, or route records with no endpoints.

## Founder selection

Founder selection should favor countries that have a reason to use illicit trade and a practical way to support it.

Strong positive factors include:

- an active embargo, sanction, or major trade restriction
- an equipment, fuel, convoy, train, truck, or industrial shortage
- a current war
- access to a neutral border, major port, occupied corridor, or international transport route
- a useful equipment surplus
- weak access to the legal international market
- intelligence contacts or an established agency
- previous smuggling or underground-trade memory
- relations with one selected founder
- state tolerance of criminal intermediaries or covert procurement

Strong negative factors include:

- no route to the proposed cell
- no meaningful demand, surplus, brokerage role, or intelligence role
- a recent successful suppression campaign
- very high confidence in ordinary trade access
- a government route that explicitly forbids covert foreign procurement
- a previous expulsion for betrayal that is still inside its exclusion period

The current player receives a moderate inclusion bonus when eligible. This increases the chance of direct interaction without forcing membership onto a country whose policy, geography, or circumstances make no sense. An ineligible player can first encounter the system later through an invitation, a seized shipment, a discovered intermediary, or an intelligence operation.

## Country eligibility

Ordinary human countries are the default participants.

The shared country classifiers are the first exclusion contract. Ordinary selection requires `uses_normal_civilian_systems = yes` and excludes `is_special_chaos_country = yes`. Actual nonhuman countries therefore fail automatically, and special human Chaos actors also remain outside the normal pool. An owning event can provide a narrow explicit Black Market adapter for a special human actor when its design truly supports clandestine trade, but a missing adapter means exclusion.

Eligibility must also account for:

- country existence and valid government scope
- access to at least one route family
- independence, autonomy, exile status, and host-country access
- civil-war status and control of relevant states
- capitulation and government-in-exile conditions
- subject restrictions
- current wars and hostile borders
- current policy toward the network
- temporary suspension or expulsion

Subjects can participate when they possess usable territory, stockpiles, officials, or routes. Their overlord does not automatically learn this. Integrated or powerless subjects with no independent logistics, no controllable stockpile, and no valid route are excluded until that changes.

Governments in exile can buy arms or intelligence only through a host-backed route and a verified recipient package. They cannot act as normal founding sellers without controlled stockpiles and a delivery endpoint.

## What outsiders know

Countries outside the network receive no Black Market decision category and no global member list.

The shared event history may show that Event 57 fired as a mod-level record. It must not show a founder flag, founder name, seller list, route map, inventory, or regional cell. This is meta history, not country knowledge.

Country-level knowledge is compartmentalized:

- a member knows its own government posture
- a member knows the direct routes it uses
- a buyer knows the offered goods and stated provenance class
- a direct counterparty can become known only when the offer type requires it
- a regional broker may know the adjacent cell, but not every distant member
- an outsider learns only the route, intermediary, shipment, or member proven by its evidence

A global public reveal can occur only through a concrete breach. Even then, public knowledge concerns the existence and broad scale of illicit trade. It does not reveal the complete membership ledger.

## Persistent runtime

The random event fires once. Everything after the founding transaction belongs to a persistent event-owned system.

The runtime keeps sparse registries for:

- active members
- dormant members
- suspended members
- former members
- invitation candidates
- active routes
- disrupted routes
- open offers
- active deliveries
- current evidence cases
- registered provider packages
- completed transaction receipts
- recent market imports that cannot be resold immediately

Processing should use the registered arrays and active jobs. It must not run a whole-world daily, weekly, or monthly country scan.

A bounded global pulse can process registered members and routes at an event-owned interval. Founding, invitation, transaction, route, war, annexation, capitulation, embargo, exposure, and provider events should mark only the affected records for refresh.

## Public mechanic values

Members manage three public values.

### Market Credit

Market Credit represents hard currency, barter claims, shell-company balances, favors, letters of credit, and the market's internal settlement ledger.

It is spent on offers, commissions, route services, and auctions. It is earned through verified sales, brokerage, intelligence contributions, and limited underwriting. It is not political power with another name.

Market Credit has a visible amount, a stable texticon, a country-specific cap, and clear gain or loss tooltips. The cap scales from the country's economy, market posture, and current evolution. Rejoining the network never grants a second founding balance.

### Exposure

Exposure measures how likely the country's routes, officials, and transactions are to become known.

Its range is `0` to `100`.

| Band | Public state | Main effect |
| --- | --- | --- |
| `0-24` | Hidden | Normal access and low investigation pressure |
| `25-49` | Rumored | Higher delivery risk and occasional local evidence |
| `50-74` | Under Investigation | Counterintelligence actions and route scrutiny become more common |
| `75-99` | Compromised | Severe seizure risk, member distrust, and posture restrictions |
| `100` | Network Breach | A breach incident resolves against the country and affected routes |

The exact value is visible to members because it changes immediate choices. Outsiders never see another country's Exposure score.

### Network Reach

Network Reach represents the market's shared ability to find suppliers, connect regions, clear payments, and move larger cargo.

Its range is `0` to `100`. It grows through real transactions, members, regional connections, and restored routes. It falls through seizures, expulsions, broken routes, and dismantled cells.

Network Reach never replaces the three formal evolutions. It provides the world-state proof that an evolution has earned its next capability set.

A member sees the current value, current reach stage, and the next public threshold. The contributor ledger stays hidden. The tooltip summarizes the largest actionable causes, such as successful deliveries, a lost route, or a recent breach.

## Reach stages

| Reach | Working stage label | System state |
| --- | --- | --- |
| `0-14` | Fragmented Contacts | The network is dormant or rebuilding |
| `15-34` | Local Circuit | Small regional lots and one primary route per member |
| `35-64` | Linked Regions | Wider suppliers, larger logistics lots, and Evolution I readiness |
| `65-84` | Underground Exchange | Embargo circumvention, specialist providers, and Evolution II readiness |
| `85-100` | Hidden World Market | Grand auctions, rare packages, and Evolution III readiness |

These are working labels, not final localisation.

## Baseline member experience

A member should normally make one of five kinds of decisions:

1. Buy a current lot that solves a real shortage.
2. Sell a verified surplus and gain Market Credit.
3. Repair or improve a route.
4. Change the government's relationship with the network.
5. Manage Exposure after a risky transaction or investigation.

The baseline offer pool focuses on small arms, support equipment, artillery where valid, trucks, trains, convoys, fuel, modest intelligence packages, and small source-backed foreign or captured lots. Tanks, aircraft, large captured stockpiles, unusual equipment, and complete technical packages belong to later capabilities unless the world date and a provider make an early appearance reasonable.

Every purchase creates a delivery job. The goods do not appear immediately merely because the player clicked a decision.

## Dormancy, reconstruction, and final dismantling

The network becomes dormant when it has no active route-backed cell capable of generating and delivering an offer.

Dormancy does not automatically delete the event. Former members, surviving brokers, locked credit, and old route knowledge remain. A bounded reconstruction pulse can try to reconnect a former member or build one new route after a long delay.

A full dismantling is possible only when all of these are proven:

- no active members remain
- no active routes remain
- no delivery job remains unsettled
- the clearinghouse or equivalent settlement chain has been exposed
- Network Reach has fallen below the final dismantling threshold
- no reconstruction request is already committed

Full dismantling ends automatic growth and offer rotation. It preserves history and achievement records. A later event cannot silently recreate Event 57 as a second first firing.

## Tone and text direction

The event should use period clandestine logistics as its visual and writing language.

Useful subjects include false cargo manifests, guarded warehouses, mismatched crates, railway sidings after dark, neutral freight offices, diverted fuel drums, merchant holds, captured guns with altered markings, anonymous couriers, customs seizures, and intelligence officers dealing through intermediaries.

Avoid modern digital-market terms, online-market language, generic gangster-film dialogue, ornate criminal guild lore, or a single named mastermind. The network is an international system of brokers and routes, not a new country or a central villain.

Member invitation text should convey limited knowledge and practical need. Acceptance, patronage, penetration, and refusal should have different government voices. Final wording belongs to implementation and localisation review.

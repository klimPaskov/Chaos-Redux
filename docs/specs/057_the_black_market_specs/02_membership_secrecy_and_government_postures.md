# Membership, Secrecy, and Government Postures

## Membership model

The Black Market is invitation-only. Membership is a country-owned relationship with the network, not a public diplomatic status.

Each country can occupy one of the following states:

| State | Meaning | Category access |
| --- | --- | --- |
| Candidate | The network has identified a possible contact but has not sent an invitation | None |
| Invited | A live invitation is pending | Invitation report only |
| Active member | The country has at least one usable route or a committed route-opening mission | Full current phase |
| Dormant member | The country retains contacts and locked credit but has no usable route | Reconnection actions only |
| Suspended member | Access is blocked by a breach, unpaid settlement, or internal conflict | Remediation actions only |
| Former member | The country withdrew or lost access without permanent expulsion | No normal category until reconnection |
| Expelled member | The network recorded betrayal, repeated exposure, or deliberate seizure | No normal category during exclusion period |
| Dismantler | The country is running a verified counterintelligence penetration against a known cell | Counter-smuggling actions only |

A country cannot hold two contradictory states. State transitions must be idempotent and must clean up obsolete decisions, missions, selected offers, route flags, and temporary targets.

## Invitation ownership

An invitation belongs to one sponsoring member and one candidate country.

The sponsor provides the initial route proof. The candidate receives only the information needed to decide whether to accept. The invitation does not reveal the wider member list.

An invitation record should store:

- sponsoring member
- candidate
- proposed route type
- route endpoint or intermediary proof
- invitation issue date
- invitation expiry date
- current evolution
- expected founding credit or access package
- candidate acceptance score
- rejection reason when invalidated
- one-time receipt ID

A live invitation is invalidated when the sponsor disappears, the route becomes impossible, the candidate is annexed, the candidate enters a mutually incompatible policy state, or the network is dismantled.

## Invitation cadence

Membership growth occurs through event-owned pulses, not through repeated random-event firings.

Suggested starting cadence:

| Network state | Base invitation interval | Factors that shorten it | Factors that lengthen it |
| --- | ---: | --- | --- |
| Baseline | `150-240` days | war, embargoes, two successful deliveries, a new regional route | recent breach, low Reach, several refusals |
| Evolution I | `100-180` days | connected regions, broker surplus, active shortages | disrupted routes, high average Exposure |
| Evolution II | `75-150` days | major embargo pressure, neutral relays, provider demand | public investigations, suspended members |
| Evolution III | `60-120` days | Grand Auction cycle, global wars, several mature cells | regional dismantling, route saturation |

These are tuning anchors. Final intervals should be centralized and modified by live state.

A pulse chooses one active sponsor, builds a bounded candidate shortlist, and commits at most one new invitation. The same pulse cannot invite several countries merely because the network is large.

## Candidate shortlist

Candidate search should begin from the sponsor's actual connections.

Preferred candidate sources are:

- direct land neighbors
- countries connected through a valid neutral intermediary
- countries with ports that can support the sponsor's maritime route
- countries controlling part of an existing international corridor
- countries with strong relations to the sponsor
- countries currently trading, fighting, sanctioning, or sharing intelligence with the sponsor when script evidence exists
- former members with a valid reconnection route
- countries named by an owner-provided event adapter

The implementation can use a small number of bounded random candidate samples when a direct collection is unavailable. It must not iterate over every country every day or every month.

## Acceptance factors

The candidate decides whether to accept, reject, delay, or infiltrate.

### Demand

Acceptance rises when the candidate has:

- severe equipment shortages
- low fuel reserves
- inadequate convoys or trains
- a current war
- an active embargo or strategic sanction
- poor legal market access
- an urgent intelligence requirement
- a large but unusable stockpile it could sell
- an isolated or threatened government

### Route confidence

Acceptance rises when:

- the proposed route is open
- the sponsor shares a border
- the candidate owns a usable port
- a neutral intermediary is stable
- the route avoids an enemy blockade
- the candidate has sufficient convoys, trains, trucks, fuel, or airlift capacity

### Political and security fit

Ideology alone does not decide compatibility.

A stable democracy with open trade and a strong anti-corruption policy should usually reject an unnecessary invitation. The same country may accept during blockade, invasion, or acute shortage.

An authoritarian government may find state patronage easier, but a highly centralized security state can also suppress an independent criminal network. A planned economy may reject private brokerage while still using intelligence-controlled procurement. A neutral commercial state may prefer an intermediary role and decline full membership.

Relevant factors include:

- ruling ideology and route flags
- internal repression
- corruption or anti-corruption policy
- intelligence capacity
- stability
- war support
- faction obligations
- legal trade access
- recent scandals
- previous dealings with the network
- relations with the sponsor

### Trust and memory

Hidden trust rises through completed settlements, clean deliveries, route assistance, and reliable sales. It falls through missed deliveries, seizures, leaked identities, hostile posture changes, and selling the same information to several sides.

Trust is an internal input. It is not a fourth public meter.

## Candidate responses

### Accept and keep distance

The government enters active membership under the compartmentalized posture. It receives its one-time founding credit and one route. The founding credit is never granted again after withdrawal, suspension, annexation, tag restoration, or reconnection.

### Accept and sponsor the network

This response is available only when the government can commit state resources. It enters State Patronage immediately and gains stronger brokerage and route capacity at the cost of higher Exposure.

### Accept and penetrate

The country joins under Counterintelligence Penetration. It can trade enough to maintain cover, but its primary goals are evidence, control, and possible dismantling.

The route should be available only when the country has a valid intelligence or internal-security basis. Without La Résistance, base-game political and security conditions provide the equivalent route.

### Reject

Rejection does not expose the sponsor by default. The candidate can quietly refuse, threaten a local crackdown, or preserve the contact for later.

A quiet refusal creates a long invitation cooldown. A hostile refusal creates a shorter investigation opportunity and reduces trust. The network should not repeatedly invite a country that keeps rejecting it.

## Member knowledge

A member does not automatically know every other member.

The knowledge model should distinguish:

- **direct contact**, meaning a route or transaction names the counterparty
- **regional awareness**, meaning the member knows that another cell exists in a named region
- **broker knowledge**, meaning a country knows one intermediary or settlement office
- **network awareness**, meaning the member understands the market's broad reach but not its membership
- **proven identity**, meaning an evidence receipt names a specific participant

Direct trading at Evolution I can reveal a counterparty to the two participants. Hostile countries can transact at any stage when a valid route, source, and trust proof exist. Evolution III makes masked hostile transactions more frequent, larger, and easier to route without forcing identity disclosure.

## Government postures

A member chooses one active posture. These are working design labels, not final localisation.

### Compartmentalized Tolerance

This is the default member posture.

It represents officials ignoring selected routes while keeping the government formally distant.

Effects and rules:

- normal offer access
- lower Exposure per transaction
- one primary route at baseline
- lower sale volume from state stockpiles
- faster passive Exposure recovery during quiet periods
- limited ability to influence the next inventory rotation
- low diplomatic damage if a local route is exposed

AI countries use this posture when they need the market but have stable institutions, moderate shortages, or a strong fear of scandal.

### State Patronage

The government places officials, depots, transport offices, or intelligence services behind the network.

Effects and rules:

- larger sale and purchase handling capacity
- higher Market Credit cap
- faster route repair
- stronger ability to commission a category
- access to state reserve sales when readiness floors remain satisfied
- higher Exposure from every major transaction
- harsher consequences if evidence proves government direction
- more pressure from foreign intelligence and sanctions

State Patronage should be attractive for isolated regimes, countries in long wars, and governments with large surplus stockpiles. It must not become the universal best posture.

### Counterintelligence Penetration

The government allows a controlled cell to operate while security services build evidence.

Effects and rules:

- reduced ordinary offer access
- normal access to small cover transactions
- higher chance to identify an intermediary after a failed or delayed delivery
- ability to feed false manifests, mark a shipment, or prepare a coordinated seizure
- a route toward regional dismantling
- a risk that the network detects the operation and expels the country
- lower Market Credit cap

This posture needs real intelligence or security capacity. It should not be a free choice for every weak minor.

A country under penetration can remain a member for a long time. The network should react to evidence of suspicious behavior. It cannot automatically know the government's intent.

### Suppression Campaign

The government ends normal trading and attempts to destroy the local network.

Effects and rules:

- normal purchase and sale actions close
- current undisbursed credit becomes locked
- active deliveries resolve according to dispatch state
- route seizure and intermediary arrest missions become available
- Exposure rises at the start because contacts begin disappearing
- success can turn the country into a former member or regional dismantler
- failure can expose the government, destroy evidence, and produce expulsion

Suppression is a committed route, not a posture that can be toggled for one reward and immediately reversed.

## Posture changes

Changing posture requires a cooldown and a valid political or security basis.

Suggested base cooldown is `180` days, modified by:

- recent breach
- war emergency
- government change
- intelligence leadership change
- successful suppression
- major embargo activation
- network evolution

A shift from State Patronage directly into Suppression creates a betrayal incident and a large Exposure increase. A shift from Compartmentalized Tolerance into Counterintelligence Penetration is quieter but requires intelligence capacity and time.

Posture changes must not grant repeated credit, repeated route rewards, or repeated Reach.

## Voluntary withdrawal

A member can withdraw when it has no unsettled delivery and no active route mission.

Normal withdrawal:

- closes ordinary access
- preserves the former-member record
- locks most Market Credit
- settles a network fee against the remainder
- keeps one reconnection lead when Exposure is below the breach threshold
- applies a long re-entry cooldown

The country does not receive another founding balance after re-entry.

A government can burn its contacts during withdrawal. This forfeits more credit and reduces Exposure, but makes reconnection harder.

## Suspension

Suspension is temporary and can result from:

- unpaid or inconsistent transaction state
- a route breach
- Exposure reaching `100`
- loss of every route
- government collapse during an unsettled transaction
- provider package invalidation
- suspected penetration

A suspended member sees only remediation, settlement, route repair, or withdrawal actions. It cannot buy or sell until the suspension reason is cleared.

## Expulsion

Expulsion follows proven betrayal or repeated serious failure.

Possible causes include:

- a successful sting against another member
- exposing several member identities
- seizing a dispatched shipment under false pretenses
- attempting to resell recently imported market equipment
- failing several settlements
- deliberate state confiscation under State Patronage
- a detected Counterintelligence Penetration operation

Expulsion:

- closes all normal access
- cancels undisbursed offers
- resolves dispatched deliveries through the receipt ledger
- freezes or confiscates remaining Market Credit
- destroys direct trust
- records a country-specific exclusion period
- may create a targeted retaliation or false-manifest incident

Expulsion does not make the complete network public.

## Reconnection

Former and dormant members can reconnect through a surviving sponsor, old intermediary, or route reconstruction mission.

Reconnection requires:

- one valid route proof
- no active expulsion exclusion
- a compatible government posture
- no unsettled hostile case against the network
- a bounded Market Credit reconciliation

Reconnection does not increase Reach unless it restores a route or regional cell that had genuinely been lost.

## Annexation, civil war, and tag changes

Membership belongs to the current country scope and must not silently duplicate during country splits.

### Annexation

When a member is annexed:

- its active routes are marked for refresh
- undisbursed offers are canceled
- dispatched cargo keeps its transaction receipt
- its credit is frozen
- the annexer does not inherit membership automatically
- a successor can receive a reconnection invitation only through a new proof

### Civil war

A civil-war split can produce one of three outcomes:

- the original government retains membership and the breakaway knows nothing
- one side inherits the active cell because it controls the route state and depot
- the cell fractures and both sides become candidates with no normal access until the network chooses one

The split must use route, capital, stockpile, intelligence, and government evidence. It cannot copy full membership and credit to both sides.

### Cosmetic and tag changes

A cosmetic identity change preserves membership. A genuine tag replacement or release uses an explicit transfer or reconnection path. Stable transaction receipts must survive only when their buyer and seller scopes remain valid.

## Secrecy failure and evidence

Exposure is country-local. Evidence is observer-local.

An outsider's evidence record should name only what has been proven:

- suspicious cargo class
- route endpoint
- intermediary
- shipment date
- known member
- probable member
- source country when recovered serials or documents support it

Evidence can mature through several incidents. One seized truck does not reveal a global organization.

A member's Exposure breach may create evidence for:

- the route host
- the country that performed the seizure
- a current war enemy with intelligence access
- a sanctioning coalition leader
- a country named by the breach event

The breach must remain bounded. It should never notify every ordinary country through a hidden whole-world loop.

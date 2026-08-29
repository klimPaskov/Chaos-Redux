# Cost surface coverage

## Coverage boundary

The implementation must audit every purchase cost in the supported Vanilla build and the Chaos Redux repository at the implementation commit. Coverage is not limited to the examples in this specification.

The guaranteed boundary includes:

- all enabled Chaos Redux event, decision, mission, focus, scripted GUI, country, warfare, intelligence, research, and shared-system transactions
- all Vanilla cost surfaces that the installed engine exposes to script, database modifiers, event-aware variants, or verified GUI adapters
- DLC-gated surfaces present in the installed build, with their normal DLC gates preserved

The guaranteed boundary does not include arbitrary third-party scripted transactions that bypass both native affected modifiers and the public Chaos Redux cost adapter.

## Qualifying transaction test

A surface qualifies when all of these statements are true:

1. A country voluntarily pays or commits a resource to take an action.
2. The amount is known or calculable before the action commits.
3. The action has a real affordability, payment, or commitment surface.
4. Reducing the amount does not change the action's identity or bypass a non-cost requirement.

The following do not qualify by default:

- casualties and population deaths
- attrition and supply loss
- bombing and building damage
- contamination and outbreak damage
- condemnation and sanction penalties
- mission failure effects
- enemy-inflicted resource loss
- focus duration and research time
- construction time and production output
- unit training time
- cooldowns and mission deadlines
- target, route, state-control, ideology, technology, law, or unit requirements
- passive upkeep and ongoing negative modifiers that are not committed as a purchase

An owning system can register an unusual qualifying transaction, but the ledger must explain why it is a purchase.

A logical action with several spendable resources receives one transaction row plus one component row for each cost. Every qualifying component is discounted independently. The registry also assigns one primary achievement family to the completed logical action, so one click cannot satisfy several achievement families at once.

## Coverage strategies

| Code | Strategy | Acceptance condition |
| --- | --- | --- |
| A | Native dynamic composition | A verified engine modifier changes the real and displayed cost with correct stacking and expiry |
| B | Shared scripted transaction | Quote, affordability, payment, display, and refund use the shared adapter |
| C | Event-aware static coverage | Complete normal, 50 percent, and 75 percent records or equivalent conditional data exist and behave as one action |
| D | Engine-inaccessible | Exact source and engine evidence proves the surface cannot be altered without a false replacement |

A surface with strategy D remains a documented compatibility limitation. It is not silently called supported.

## Required cost families

The following table is the minimum audit map. The implementation audit must add every discovered family or surface that is missing.

| Cost family | Common examples | Discounted component | Preserved components | Expected strategy |
| --- | --- | --- | --- | --- |
| Political power decisions | reforms, diplomacy, event actions, appointments | Political power payment | availability, target, cooldown, route locks | A, B, or C |
| Laws | economy, trade, conscription, political laws | Real law-change cost | law eligibility and replacement rules | A or C |
| Advisors and personnel | political advisors, theorists, chiefs, high command | Real hiring cost | slot limits, traits, ideology, country access | A or C |
| Command power | commander abilities, military actions, emergency commands | Command power payment | combat state, commander state, cooldown | A, B, or C |
| Army experience | doctrines, templates, army programs, specialist actions | Army experience payment | technology, template, doctrine, route rules | A, B, or C |
| Navy experience | naval doctrines, ship design, naval programs | Navy experience payment | hull, doctrine, technology, design rules | A, B, or C |
| Air experience | air doctrines, aircraft design, air programs | Air experience payment | airframe, doctrine, technology, design rules | A, B, or C |
| Officer corps purchases | spirits, roles, doctrine-linked appointments | The registered experience or power cost | slot, branch, doctrine, trait requirements | A or C |
| Doctrine unlock costs | any doctrine paid through experience or a custom currency | Payment amount | prerequisites and exclusivity | A, B, or C |
| Equipment stockpile payments | rifles, support equipment, artillery, trucks, tanks, aircraft, ships, custom equipment | Exact stockpile debit | equipment type, stockpile availability, project gates | B or C |
| Convoys | aid, intervention, transport, expedition, intelligence, market actions | Convoy debit | route access, port access, target validity | B or C |
| Trains | rail programs, logistics commitments, evacuation, transport | Train debit | rail control, supply, target validity | B or C |
| Fuel | operations, special deployments, expeditions, emergency programs | Fuel debit | unit, target, route, war-state requirements | B or C |
| Manpower payments | unit raising, cadres, labor programs, operations | Voluntary manpower debit | manpower floor, unit and state requirements | B or C |
| Stability payments | deliberate public or political sacrifice | Voluntary stability reduction | minimum floor, route and crisis requirements | B or C |
| War support payments | deliberate morale or political sacrifice | Voluntary war support reduction | minimum floor, war-state and route rules | B or C |
| Civilian factory commitments | agency, construction, projects, foreign aid, expeditions | Number of committed civilian factories | duration, target, project identity | A, B, or C |
| Military factory commitments | special production, mobilization, emergency contracts | Number of committed military factories | duration, production and route requirements | B or C |
| Dockyard commitments | naval projects, repairs, expeditions, special construction | Number of committed dockyards | duration, port and naval requirements | B or C |
| Consumer-goods commitments | temporary economic burden taken to start an action | Committed burden when modeled as a purchase | duration and policy identity | A, B, or C |
| Intelligence agency upgrades | upgrade payments and preparation commitments | Real resource or factory cost | agency existence, upgrade prerequisites, DLC gate | A or C |
| Intelligence operations | operation preparation resources and committed factories | Upfront or atomic preparation cost | network strength, operatives, target, duration | A, B, or C |
| Military industrial organizations | funds, upgrades, policy assignments, task costs | Real MIO payment | organization access, trait path, task rules | A or C |
| International market | purchase payment, convoy commitment, contract fee where scriptable | The buyer's real committed cost | seller, delivery, contract, market limits | A or D |
| Special projects | facility, project, prototype, resource, or scientist purchase costs | Registered payment component | facility, scientist, project, technology requirements | A, B, or C |
| Diplomatic transactions | guarantees, recognition, aid, influence, treaty actions with payment | Registered voluntary payment | relations, faction, ideology, target rules | B or C |
| State-targeted projects | forts, shelters, rail, ports, extraction, local campaigns | Upfront payment or committed factories | state ownership, control, slots, target validity | B or C |
| Custom mechanic currencies | legitimacy, cohesion, influence, authority, readiness, corruption reduction payments | Explicit spendable amount | thresholds, route, actor, target, floor | B or C |
| Scripted GUI actions | any button that spends a registered resource | Real button payment | button state, selected target, cooldown, AI equivalent | B or C |
| Event options with payment | player options that buy an outcome | Explicit voluntary payment | event scope, target, option availability | B or C |
| Research and design purchases | variant, module, template, equipment, doctrine, prototype costs exposed to script | Exposed purchase amount | design validity and technology requirements | A, C, or D |
| Subject and autonomy actions | actions that pay power, equipment, factories, or autonomy currency | Registered payment | subject relation, autonomy stage, target validity | B, C, or D |
| Trade and resource agreements | discrete scripted fees or commitments | Registered fee | market access, relations, routes, resource availability | B, C, or D |
| Shared stockpile debit helpers | all public and event-owned equipment and fuel debit helpers | Exact helper input | resource type and caller validity | B |

## Resource-specific rounding ledger

Every surface records one quantum. Recommended semantics are:

| Resource | Quantum | Minimum positive payment |
| --- | --- | --- |
| Political power | 1 point | 1 |
| Command power | 1 point | 1 |
| Army, navy, and air experience | 1 point unless the owning UI supports a smaller exact unit | One quantum |
| Equipment, trains, convoys, aircraft, vehicles, and ships | 1 unit | 1 |
| Fuel | The smallest exact unit used by the payment helper | One quantum |
| Manpower | 1 person or the owning system's exact displayed block | One quantum |
| Stability and war support | The owning system's supported displayed percentage quantum | One quantum |
| Factories and dockyards | 1 building commitment | 1 |
| Custom currencies | The owning mechanic's displayed and payable quantum | One quantum |

The implementation agent must confirm each quantum against current source and engine behavior. The table is a semantic default, not permission to display false precision.

## Native database audit

The implementation pass must inspect all relevant Vanilla and Chaos Redux databases, including:

- decisions and decision categories
- laws and ideas
- characters and advisor roles
- commander abilities
- officer corps and doctrine systems
- intelligence agency upgrades and operations
- military industrial organizations
- international market and contract definitions
- special projects and facilities
- equipment designers and variant systems
- scripted GUI click effects
- event options
- focus completion effects that launch paid actions
- shared scripted effects that debit resources

The audit must identify the actual consumer. A localisation string that says an action costs fuel is not proof that fuel is paid. A negative resource effect in a failure branch is not automatically a qualifying purchase.

## Chaos Redux source audit

The audit should search for at least these patterns and then review each match manually:

- static `cost` fields
- custom cost triggers and cost text
- negative political power, command power, and experience effects
- negative manpower, stability, and war support transactions
- equipment stockpile debit helpers
- fuel debit helpers
- convoy and train removals
- factory and dockyard commitment modifiers
- custom mechanic currency reductions
- scripted GUI payment effects
- quote, pay, refund, and reserve-floor helpers
- AI willingness that depends on affordability or reserve state
- multi-resource actions whose components use different helpers or refund paths
- overlapping temporary cost sources and their exclusions

Mechanical search output is a discovery tool. Every result requires classification and an owner file in the registry.

## Static variant coverage

A static surface that cannot call the shared quote API requires complete variants or another verified conditional method.

For each logical action, confirm:

- normal price record
- 50 percent price record
- 75 percent price record
- shared availability and visibility
- shared completion and cooldown state
- shared effect and target logic
- one visible record at a time
- one AI-valid record at a time
- correct price after save and reload
- correct restoration after expiry
- no duplicate localisation or event-log entries

A partial set of handpicked variants fails the coverage requirement.

## DLC handling

DLC-gated surfaces remain gated by their normal DLC. Event 26 does not expose a system the player does not own.

The registry records the DLC or base-game dependency for each surface. Testing must cover the supported DLC-present and DLC-absent states when the surface changes loaded data or UI behavior.

## Engine-inaccessible findings

A strategy D entry must include:

- exact engine or source surface
- cost type and current value source
- attempted modifier, database, scripted, and GUI routes
- offline documentation and Vanilla precedent checked
- reason the real cost cannot be changed
- whether the displayed value can also not be changed
- why a replacement action would be inaccurate
- player-facing compatibility note, if the limitation is visible

The implementation must not claim complete universal coverage while a strategy D entry is hidden from the completion report.

## Future coverage rule

Any later Chaos Redux feature that adds a voluntary cost must register it with the shared cost framework or record a deliberate exclusion. The Event 26 completion audit should treat an unregistered new cost as a regression.

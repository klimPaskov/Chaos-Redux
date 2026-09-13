# Event 40: Federation Country and Focus Package

## Country-package boundary

Ordinary intervention targets keep their existing country packages. Event 40 adds decisions, ideas, character roles, AI strategy, and outcome memory to them. It does not give every target a large new focus tree.

A dedicated country package becomes necessary only when Evolution III creates a durable united Arabian state. That federation must be playable, militarily viable, politically distinct, and able to continue after the Event 40 intervention campaign ends.

## Federation identity selection

The implementation must audit installed vanilla, Chaos Redux, installed Workshop mods, and sibling local mods before reserving any new country tag or cosmetic tag.

A federation can use one of three carrier approaches:

1. Transform the strongest valid member and integrate the others.
2. Use a protected Chaos Redux regional carrier when the country registry already provides one.
3. Use a new tag only after collision review proves that no suitable carrier exists.

The selected approach must preserve origin and membership history. The country must know which Event 40 outcome created it, which governments joined, which refused, and which core state supplied the federal center.

### Core candidate selection

The strongest existing participant normally becomes the federation core. The score should consider:

- political legitimacy
- population and industry
- controlled core territory
- functioning capital and supply
- military strength
- leadership accepted by other participants
- contribution to the congress or regional system
- British backing for British Arabia
- sovereign standing for the Independent Arab Federation
- personal Lawrence support for Lawrence's Kingdom

Britain cannot simply choose the smallest compliant client when a much stronger participant would make the new state unviable.

### Capital selection

The capital is chosen from valid member capitals or a congress city that is owned, controlled, supplied, and politically acceptable.

The choice can vary by outcome:

- British Arabia favors a secure administrative and transport center with British access.
- Independent Arab Federation favors a congress-backed capital with sovereign legitimacy.
- Lawrence's Kingdom can use a city tied to the successful campaign, but it still needs infrastructure and member acceptance.

The specification does not hardcode one universal capital because the current map and participating countries can differ greatly.

## Formation transaction

Federation formation is one validated transaction. It must not be implemented as a loose sequence that can stop halfway.

The transaction covers:

- participating countries and refusal records
- ownership and control of transferred states
- capital
- cores, claims, compliance, and resistance
- armed forces
- equipment stockpiles
- manpower
- ships and air wings where engine behavior allows safe transfer
- commanders, advisers, leaders, and institutions
- subjects, guarantees, factions, and military access
- wars and peace state
- technologies and research sharing
- factories, production, fuel, convoys, trains, and supply
- Event 40 outcome and generation memory
- player switching when a player-controlled member joins
- rollback if validation fails

The transaction cannot delete armies, duplicate equipment, strand units without supply, or leave several simultaneous copies of one character.

## Territorial settlement

Member-owned and member-controlled core states can transfer at formation when the charter covers them.

Contested, occupied, foreign, or culturally disputed territories normally begin as claims or integration zones. The federation earns cores through control, compliance, local support, member consent, and post-formation work.

The country must not receive instant cores on the whole Arabian registry.

### Integration categories

- Founding member territory can receive immediate cores when consent and control are proven.
- Acceding member territory can use a short ratification and administrative-integration mission.
- Occupied or disputed territory begins with claims and a longer settlement route.
- Territory held by a refusing independent state remains outside the federation.
- A British subject that joins British Arabia requires an autonomy and transfer settlement.
- A counter-bloc member that joins an independent federation must retain its negotiated protections.

## Starting armed forces

The federation inherits valid member forces through a bounded merge.

The force package must preserve:

- existing divisions and experience where possible
- equipment ownership and deficits
- commanders without duplication
- member military traditions
- local garrisons
- realistic supply and transport limits

The federation should not receive a large free army in addition to all inherited member units.

### Command integration

The new state begins with competing command systems. It must solve:

- British-trained formations versus national forces
- regular officers versus irregular leaders
- member-country seniority
- language and staff practice
- supply standards
- equipment diversity
- political loyalty

Early decisions and focuses create a federal general staff, regional commands, or a looser member-defense system.

### Force growth

Later growth comes through:

- member levies and federal recruitment law
- British training and equipment for British Arabia
- sovereign military schools for the Independent Arab Federation
- loyalist formations and personal guards for Lawrence's Kingdom
- integration of irregular units
- desert reconnaissance and mobile logistics
- air-route and coastal-defense programs
- arms standardization decisions

No custom 3D unit is required. Existing HOI4 unit families can express the military package.

## Starting economy and logistics

The federation inherits real member factories, resources, ports, airbases, railways, and supply hubs. It does not receive an abstract industrial package detached from the map.

The starting economic problem is coordination.

- customs and currencies differ
- oil and port access can be politically contested
- rail networks may not connect
- British contracts can conflict with sovereign policy
- member governments may protect their own revenue
- military equipment and repair standards differ

The early economy route should create visible map and production changes. It can repair railways, connect ports, expand air routes, improve oil transport, establish federal depots, and build industry in underconnected founding regions.

## Starting ideas and lifecycle

The federation begins with no more than three major focus-owned national spirits.

### Uneven Administration

Role: mixed negative starting spirit.

It represents incompatible laws, ministries, customs, records, currencies, and local administrations.

Mitigation:

- federal census and revenue agreement
- common customs administration
- member civil-service guarantees
- regional administrative offices

Possible final forms:

- Central Federal Administration
- Charter Administration
- Imperial Liaison Administration

Failure can worsen it into Administrative Secession when members refuse revenue or law enforcement.

### Rival Commands

Role: military starting weakness.

It represents British-trained units, member armies, irregular commands, and competing senior officers.

Mitigation:

- federal general staff
- member command council
- arms standardization
- officer oath and promotion settlement

Possible final forms:

- Unified Arab General Staff
- Federal War Council
- British Arabian Command
- Lawrence's Field Household, only for the rare personal route

Failure can produce mutiny, duplicated command, or regional army autonomy.

### Promise Debt or Federal Mistrust

Role: political and diplomatic starting pressure.

The exact form depends on the outcome.

- British Arabia begins with Promise Debt, which records the gap between British guarantees and client fears.
- Independent Arab Federation begins with Federal Mistrust, which records member doubts about domination by the core.
- Lawrence's Kingdom begins with Personal Settlement, which records dependence on one unusual ruler and the unresolved standing of local dynasties and governments.

The idea changes through constitutional and diplomatic routes. It does not remain a permanent unresponsive penalty.

## Post-formation public mechanic

### Federal Authority

The federation uses one public persistent value, `Federal Authority`, after formation. Lawrence's Influence closes when the intervention campaign is superseded.

Federal Authority measures the practical ability of the center to collect revenue, coordinate defense, enforce the charter, run common infrastructure, and represent members abroad.

The value affects:

- focus availability
- integration missions
- command reform
- member autonomy
- foreign policy
- secession risk
- federal projects

The player should see the exact value, qualitative band, recent trend, and next threshold. Member trust, local administration, British pressure, military cohesion, and congress support remain internal contributors.

## Focus tree architecture

The federation receives a full route-based tree. The implementation agent chooses final focus count, names, coordinates, and connections while preserving this architecture.

### Lane map

| Lane | Role | Main payoff |
| --- | --- | --- |
| Opening constitutional settlement | Establish the federation's legal and political structure | A functioning charter and route lock |
| Political identity | British compact, sovereign congress, or rare personal settlement | Final government identity and leadership |
| Federal center and member autonomy | Balance central capacity with local rights | Stable Federal Authority model |
| Economy, oil, and logistics | Connect member economies and routes | Federal customs, rail, ports, oil, and production network |
| Army and irregular integration | Unite commands and equipment systems | Federal general staff or member war council |
| Air, coast, and transport | Defend long distances and regional access | Air-route, port, convoy, and coastal-defense capability |
| Diplomacy and recognition | Win recognition and manage Britain, rivals, and neighbors | Faction, league, or independent regional status |
| Integration and regional settlement | Add willing members and settle disputed territory | Staged cores, claims, protectorates, or association |
| Late regional order | Define the federation's long-term role | British partner, sovereign power, or personal kingdom end state |

### Opening group

The opening should contain one clear first focus or a very small group.

It establishes:

- the provisional federal government
- the founding charter
- the temporary capital
- member representation
- starting Federal Authority
- the three starting idea lifecycles

After the opening, the player sees a limited set of meaningful choices:

- define the political settlement
- address command rivalry
- secure revenue and transport
- negotiate member rights

The opening must not expose every late route immediately.

## Political route family

### British-Aligned Federal Compact

Narrative role: convert British Arabia into a stable dominion, protectorate, or allied federation.

Mechanical role:

- British equipment and training
- bases and route agreements
- preferential trade and oil contracts
- shared intelligence
- autonomy progression
- client coordination

Tradeoff:

- high short-term security and support
- continuing British leverage
- internal opposition to bases and foreign-policy limits

Important focus groups:

- Ratify the Imperial Compact
- Define Dominion or Protectorate Status
- British Military Mission
- Oil and Transport Convention
- Federal Voice in the Empire
- Demand Equal Partnership, optional autonomy branch

The route can end as a loyal partner, an autonomous dominion, or a breakaway federation after a severe dispute. The route does not trap the player in permanent helplessness.

### Sovereign Arab Congress

Narrative role: create a federation through member sovereignty and a public congress.

Mechanical role:

- recognition diplomacy
- constitutional government
- balanced member representation
- independent military and industry
- regional association
- British treaty or separation

Tradeoff:

- stronger long-term sovereignty
- slower early consolidation
- higher risk of member veto and rival sponsorship

Important focus groups:

- Convene the Constituent Congress
- Ratify Member Guarantees
- A Federal Cabinet
- Independent Foreign Service
- The Common Defense Charter
- Recognition Beyond the Region

The route can end as a nonaligned federation, a friendly British ally, or the center of an independent Arab bloc.

### Lawrence's Personal Settlement

Narrative role: resolve the rare kingdom, military federation, or personal union around Lawrence.

Visibility:

- hidden until Evolution III forms Lawrence's Kingdom
- unavailable to British Arabia and ordinary independent federations

Mechanical role:

- personal authority
- loyal field commands
- arbitration among dynasties and member governments
- unusual relations with Britain
- succession and institutionalization

Tradeoff:

- fast decisions and strong personal coordination
- severe succession risk
- legitimacy disputes
- tension between local rulers and the imported monarch or military ruler

Important focus groups:

- The Personal Oath
- Council of Founding Houses
- Lawrence's Field Government
- A Crown Bound by Charter or The Commander's State, mutually exclusive political structure
- Secure a Succession
- Separate the State from the Man, reform route

The route must answer what happens after Lawrence dies. A stable constitution, named succession institution, or peaceful dissolution path is required.

## Federal center and member autonomy

This branch uses Federal Authority and provides two broad methods.

### Central federal state

- common tax and customs
- unified ministries
- federal courts
- direct command
- faster integration

Costs:

- member resistance
- larger administrative burden
- stronger secession risk after failure

### Charter federation

- member guarantees
- shared revenue formulas
- regional commands
- slower central projects
- easier accession of cautious states

Costs:

- slower action
- member vetoes
- weaker emergency response

The methods should interact and can converge after reforms. They should not be two unrelated modifier ladders.

## Economy, oil, and logistics branch

The branch is geographically grounded.

Focus groups include:

- Federal Customs Line
- Connect the Member Railways
- Red Sea and Gulf Port Plan
- Oil Revenue Settlement
- Federal Supply Depots
- Air Route Infrastructure
- Industrial Projects Outside the Core
- Common Equipment Repair Standards

Rewards include real infrastructure, railways, ports, airbases, supply hubs, resources, building slots, production lines, and decision families. The route should name valid states and adapt to actual membership.

The branch can choose between British capital, member-funded development, or balanced foreign investment. Each method has dependency and timing consequences.

## Army and irregular integration branch

Focus groups include:

- Register the Member Armies
- Resolve Officer Seniority
- Integrate the Irregulars
- Desert Reconnaissance Schools
- Common Artillery and Support Standards
- Federal General Staff or Member War Council
- Mobile Supply Columns
- Defend the Long Frontier

The branch changes templates, command structures, training, supply, and decisions. It should not fill the tree with separate tiny army spirits.

A Lawrence military role can improve irregular coordination or mobile operations, but local commanders remain important and should receive real roster treatment when historically or procedurally available.

## Air, coast, and transport branch

This branch supports countries that need long-distance movement and coastal defense.

Focus groups include:

- Desert Airfields
- Coastal Observation Service
- Federal Transport Command
- Red Sea Convoy Protection
- Gulf Port Defense
- Air Liaison Schools
- Long-Range Communications

The route can improve commercial shipping, supply, reconnaissance, and regional access. It is useful even for a player who does not build a large air force or navy.

## Diplomacy and recognition branch

Focus groups include:

- Recognition Missions
- Settle Relations with Britain
- Negotiate with France and Other Regional Powers
- Invite New Members
- Guarantee the Charter States
- Build an Arab League or Join an Existing Faction
- Mediate Regional Wars
- Oppose External Protectorates

The branch defines faction and league rules. A new federation-led bloc needs membership, refusal, exit, war, leadership, and failure logic.

## Integration and regional settlement branch

Expansion occurs through several tools:

- voluntary accession
- associated-state status
- protectorate or guarantee arrangements
- negotiated border settlement
- claims on disputed member territory
- war goals only after failed diplomacy or an actual hostile threat
- postwar occupation and integration missions

The branch does not grant instant claims or cores on every Arabian state.

A willing government can join while keeping negotiated autonomy. A refusing government remains independent unless the federation pursues a valid conflict route.

## Late regional-order routes

### Pillar of British Strategy

British Arabia becomes a powerful regional partner with bases, supply access, and negotiated autonomy.

### The Sovereign Arab Order

The Independent Arab Federation leads a recognized regional league or stands as a major independent power.

### The Kingdom After Lawrence

Lawrence's Kingdom establishes a durable succession, constitutional settlement, or personal military state. The route must resolve the country's future beyond one character.

### A Federation of Members

Any outcome can choose a looser long-term federation that prioritizes member rights and association.

### One Federal State

Any outcome with sufficient authority can pursue deeper integration at the cost of resistance and political conflict.

## Focus-tree presentation requirements

The implementation must:

- keep branch lanes visually clear at normal zoom
- avoid overlapping focuses and crossing lines
- use the shortest clean prerequisite paths
- give each visible focus one primary branch identity
- use accurate search filters
- add Focus Navigation for separated major branches
- hide the Lawrence personal route until revealed
- render and inspect the full tree through the HOI4 MCP workflow
- compare the accepted architecture against the implemented route coverage

A focus inlay is not required. Federal Authority can be shown through decisions, focus tooltips, and a national-spirit or category header unless implementation proves that tree-local display is necessary.

## Leaders, advisers, and portraits

All grounded people require attributed archival sources and portrait ownership checks.

Potential role families include:

- founding member leaders
- federal prime minister or council chair
- member-state representatives
- military chiefs from inherited commands
- engineers and transport administrators
- British liaison figures for British Arabia
- Arab nationalist diplomats for the sovereign route
- Lawrence in the roles permitted by his current state

Do not invent a generic grounded Arab leader when a defensible historical or existing country figure is required. A council can use an authentic institutional source when the government is genuinely collective.

## Flags and country names

Every final federation identity needs normal, medium, and small flags plus valid ideology or cosmetic variants when the route changes the flag.

Historical and attested symbols require source research before ImageGen produces the final flat design. Fictional federation variants can use generated flat designs grounded in the accepted route.

Possible working country-name families:

- British Arabian Federation
- Arabian Federal Dominion
- Arab Federation
- Federation of Arab States
- Kingdom of Arabia under Lawrence
- Lawrence's Arabian Union

These are working labels. Final names should respond to route, government form, and member composition.

## AI plans

The federation AI chooses routes from origin and current conditions.

- British Arabia favors compact consolidation when Britain is strong and reliable.
- A client federation seeks autonomy when Britain is weak, overextended, or repeatedly breaks promises.
- An independent federation prioritizes recognition, command integration, and balanced development.
- Lawrence's Kingdom prioritizes succession and institutional stability before expansion.
- Low Federal Authority AI addresses administration and command before pursuing aggressive integration.
- Strong federations invite willing members and avoid suicidal wars against overwhelming powers.
- Route-invalid focuses receive zero weight or remain hidden.

All focus and decision weights require scenario-based probability review.

## Country-package completion evidence

Implementation cannot call the federation complete without evidence for:

- collision-safe tag or transformation carrier
- flags and names
- capital and territory
- leaders and portrait provenance
- parties and government
- starting ideas and lifecycles
- armed forces and equipment
- technology and production
- fuel, convoys, trains, supply, and ports
- focus tree and route loading
- decisions and Federal Authority
- AI strategy
- diplomacy and faction behavior
- staged integration
- defeat, annexation, release, and cleanup
- multiplayer player-switch behavior

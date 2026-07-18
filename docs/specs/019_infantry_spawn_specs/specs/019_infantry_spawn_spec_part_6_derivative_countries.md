# Event 19 Infantry Spawn
## Part 6: Derivative country packages and route architecture

## Country package purpose

A derivative revolt country is a playable or AI-capable regional actor created when an ordinary country loses control of registered Chaos formations. It must have enough identity and gameplay to survive, fight, grow, and be defeated without becoming a hollow tag.

The packages share a common structural framework, but zombie, ghost, golem, and future families need distinct recruitment, economy, military, diplomacy, text tone, and visual identity.

The package should support dynamic regional creation rather than require one permanent tag per possible revolt.

## Shared creation flow

Natural creation freezes one of three centralized release modes before any
actor is created: ordinary claimant, anomalous claimant, or
claimant-independent family breach. The transaction nonce owns at most one
active release for the source country. Scenario creation remains a separate
direct context and does not inherit these natural prerequisites.

### 1. Determine revolt family

For a family-capable mode, the system selects the complete registry row with the
strongest valid derivative pressure based on:

- family presence
- family-controlled divisions
- claimant control
- local territorial base
- saturation
- registry derivative eligibility

An ordinary claimant release carries no family row. It needs only Evolution III,
a valid claimant, and at least one exact loyal Event 19 formation. An anomalous
claimant release carries both claimant UID and provider row. A
claimant-independent breach carries the provider row and explicitly proves that
its transfer set contains no claimant-linked rows.

### 2. Determine territory

The revolt territory should form a coherent region around:

- claimant headquarters
- family cantonments
- controlled depots or supply hubs
- states containing loyal event formations
- weak central control

The system avoids isolated single-state islands whenever a controlled, passable,
non-capital mainland state exists. If no such mainland base exists, a controlled,
passable, non-capital island may anchor the same connected-region and exact-
formation transaction. A protected parent capital is never transferred; when a
claimant headquarters is the parent capital or otherwise unsafe, an exact loyal
formation origin becomes the breakaway headquarters. This is the only-viable-
base branch of the normal geography contract, not a fixed-tag or random-state
fallback.

### 3. Determine leader

The derivative leader can be:

- the claimant general who led the revolt
- a new family-specific fictional leader
- a family-specific collective or symbolic authority

When a claimant becomes leader, the country uses that claimant’s existing identity-scene sprite and personal name. The claimant character explicitly uses `female = no`. The fixed sprite slot depicts an army or host scene without an individual focal person.

When a new one-person leader is generated, he uses a matching regional male name and explicit `female = no` metadata. His fixed sprite slot remains an army or host scene without an individual focal person.

When the authority is collective or symbolic, its player-facing identity remains institutional and uses an appropriate collective host-scene sprite. The supported engine character carrying that council identity also explicitly uses `female = no`; this technical field does not turn the council into an individual person.

### 4. Transfer forces

The derivative receives:

- claimant-loyal event formations in the revolt territory
- family formations attached to the revolt
- a limited share of compatible local event lots
- no unrelated free army

Ordinary national divisions remain with the parent unless a severe command-collapse event explicitly defects them.

All natural releases implement this force transfer as one mode-aware exact locked
transaction because HOI4 exposes no documented division-scoped ownership
effect. The source freezes every selected Event 19 UID, delete cohort, ledger
identity, template/component manifest, obligation, auxiliary membership, and
starting factor. Ordinary claimant mode freezes and proves claimant-loyal rows
without demanding a family. Anomalous claimant mode freezes and proves the exact
union of claimant-loyal and selected-family rows. Claimant-independent mode
freezes and proves only claimant-free rows of the selected family. A dynamic
actor recreates only the mode-selected set and must prove its territory, private
ledgers, applicable claimant or provider identity, and complete replacement army
before any source cohort is deleted. Deletion uses the exact frozen cohort with
no refund.

If any pre-commit proof fails, the actor's exact replacements are removed and
proved absent, its provisional cores are removed, it is annexed with troop
transfer disabled, selected territory is proved returned, and only missing
frozen source UIDs are recreated and rebound. Both sides remain locked until the
full source set and unchanged global Event 19 accounting are proved. Once source
accounting commits, later failure is terminal and locked; it must not invoke the
pre-commit rollback.

The transfer cannot preserve live-only organization, veterancy, decorations,
officer history, army assignment, orders, exact current manpower fill, or exact
per-equipment composition because those properties are not exposed to this
script path. It instead preserves the immutable Event 19 issue manifest,
identities, recorded starting factors, and liabilities. A two-sided strength
gate rejects a source below the larger recorded starting factor and rejects a
replacement above it, preventing the transaction from repairing damage.

### 5. Establish identity

The country receives:

- Event 19 derivative origin flag
- family derivative flag
- direct public country name
- adjective
- species-appropriate ruling ideology or fixed-purpose political identity
- distinct flag family
- starting ideas
- shared derivative focus tree or overlay with family modules
- decision category
- AI strategy
- shared classification registration

### 6. Start war

The derivative normally begins at war with its former parent.

A verified one-state claimant-independent family breach instead converts the
same tag to the provider identity after exact family and ledger proof. That path
clears former-parent war surfaces and does not declare war on itself.

It can also receive immediate hostility toward:

- adjacent countries that hold family-important territory
- countries that actively purged or hunted the family
- scenario-designated enemies

It should not declare random global wars without strategic reach.

## Naming principles

Public map names must be direct country names. Avoid administrative terms such as office, bureau, authority, mission, or board.

The exact name should use:

- region
- people
- family identity
- claimant name or epithet when appropriate
- simple state form when useful

Working structural examples, not final localisation:

- `[Region] Dead Host`
- `[Region] Haunting`
- `[Region] Stone Host`
- `[Claimant Name]’s Host`

Final names need country and language-sensitive wording. They should not copy the parent Zombie or Death country names.

## Flag principles

Each family needs a generated fictional flag system with normal, medium, and small HOI4 variants.

Requirements:

- distinct from parent-event flags
- readable at 10 by 7
- region-aware variation
- no simple recolor of one universal flag
- stable family motif plus local secondary motif
- distinct ideology or route variants only when the package actually uses them

### Zombie derivative motif direction

- fragmented ranks, broken ring, divided skull, torn muster marks, or regional emblem altered by repetition
- avoid copying the parent zombie flag

### Ghost derivative motif direction

- empty standard, pale procession, inverted shadow, regional monument reduced to silhouette, or spectral knot
- avoid copying Death imagery closely enough to imply the Death country

### Golem derivative motif direction

- stone hand, quarry mark, bound block, cracked regional emblem, or assembled geometric creature silhouette
- keep the design intentional rather than primitive shape-only final art

## Shared starting political package

Derivative countries are fixed-purpose chaos actors. They do not need ordinary democratic, fascist, communist, and neutrality route families unless a specific family concept supports them.

They still need internal choice.

The shared political struggle is between:

- claimant sovereignty
- collective host organization
- instinctive or species command

This struggle changes leader, recruitment, discipline, expansion, and diplomacy.

## Shared starting ideas

Working labels are not final localisation.

### Unrecognized Host

Role:

- weak diplomatic acceptance
- high war readiness
- low stability or legitimacy equivalent
- difficult trade and recognition

Lifecycle:

- claimant route transforms it into personal command
- collective route transforms it into host cohesion
- survival successes can remove the worst diplomatic and administrative penalties

### Seized Muster Districts

Role:

- reflects control of local depots, barracks, and event formations
- grants limited immediate military support
- creates supply and administration weakness

Lifecycle:

- logistics route integrates districts
- expansion route creates more districts
- defeat or loss of headquarters worsens it

### Species Burden

Family-specific starting weakness.

- zombie: fragmented command and limited controlled recruitment
- ghost: unstable manifestation and weak material administration
- golem: slow replacement and heavy material demand

Lifecycle differs by family module.

### Pursued by the Former State

Role:

- former parent receives containment and reconquest tools
- derivative gains defensive urgency
- foreign powers initially hesitate to assist

Lifecycle:

- ends through victory, negotiated survival, parent collapse, or long-term recognition

## Starting economy and supply

Derivative countries begin with local assets, not a generic economy grant.

The creation effect should evaluate:

- factories in controlled states
- local resources
- supply hubs and rail
- ports
- population where relevant
- family sustainment needs
- captured stockpiles

The country can receive a temporary emergency production or sustainment modifier, but it should not create factories from nothing unless the family’s supernatural identity explicitly justifies a bounded effect.

## Shared focus tree scale

The derivative country tree should contain roughly 25 to 35 focuses or equivalent focus groups, depending on the final layout.

It uses a common architecture with family-specific modules and localisation. A shared tree is acceptable only when the families do not read and play identically.

Major lanes:

1. survival and assembly
2. hierarchy
3. sustainment and economy
4. reinforcement and military method
5. aggression and expansion
6. family-specific transformation
7. late regional predator outcome

## Route architecture map

A diagram is provided in `focus_graphs/019_derivative_country_route_map.md`.

### Opening trunk: Survive the Separation

Narrative role:

- establish headquarters
- secure supply
- prevent immediate collapse
- organize starting formations

Mechanical role:

- reveal starting decisions
- stabilize control of the capital or headquarters state
- assign first commander or collective body
- repair or seize one local supply route
- begin the Species Burden lifecycle

Focus group directions:

- secure the muster grounds
- establish local command
- gather scattered formations
- ration the first stockpiles
- identify the former parent’s reconquest plan

This trunk should take long enough to create danger but not leave the new country helpless.

## Hierarchy route family

### Claimant Sovereignty

Unlock condition:

- the revolt was led by a claimant or the country appoints one

Narrative role:

- one possessed general turns personal loyalty into state power

Mechanical identity:

- stronger command and offensive coordination
- claimant leader traits
- more direct recruitment
- lower internal pluralism
- risk of succession collapse or personal overreach

Key focus groups:

- proclaim the commander
- bind the districts to one staff
- purge rival captains
- create a personal guard
- turn victories into obedience

Decision links:

- loyalty oaths
- claimant guard recruitment
- district governor appointments
- succession preparation

Failure state:

- leader defeat, removal, or death can reopen fragmentation

Late payoff:

- a centralized war host with strong offensive AI

### Collective Host

Unlock condition:

- claimant influence is weak, several claimant rivals exist, or local formations reject personal rule

Narrative role:

- councils, assemblies, nests, circles, or family-specific collectives organize the state

Mechanical identity:

- better local recruitment and resilience
- slower offensive concentration
- stronger resistance to leader loss
- more internal decision management

Key focus groups:

- assemble the host council
- divide command districts
- settle disputes over captured supplies
- rotate battlefield command
- codify family obligations

Decision links:

- host votes
- district aid
- emergency commander selection
- local reinforcement quotas

Failure state:

- low cohesion can split the state or empower a claimant

Late payoff:

- durable regional network with better defense and reinforcement

### Species Command

Unlock condition:

- high family pressure, no viable claimant, or family-specific transformation

Narrative role:

- the unit family’s own logic replaces human political command

Mechanical identity:

- strongest family mechanics
- weakest ordinary diplomacy
- high-chaos behavior
- narrow but powerful military specialization

Key focus groups depend on family.

Zombie direction:

- instinct hierarchy and controlled hunger

Ghost direction:

- chorus, procession, or binding place

Golem direction:

- pattern of makers, stones, and commands

Failure state:

- inability to manage ordinary territory or local resources

Late payoff:

- species-pure regional actor with no world-end route

## Sustainment and economy lane

This lane must solve the actual family burden.

### Shared focus groups

- seize or repair depots
- organize rail and transport
- convert local industry
- build family-specific sustainment sites
- establish a captured-equipment policy
- protect the headquarters supply corridor

### Zombie module

- base zombie training grounds or conversion controls
- fragmented command mitigation
- limited population or casualty-based recruitment
- captured ordinary equipment for auxiliaries where allowed

Tradeoff:

- faster growth raises fragmentation, saturation legacy, or local devastation

### Ghost module

- manifestation anchors
- haunted infrastructure
- slow extraction of labor or presence from occupied states
- controlled population drain

Tradeoff:

- stronger anchors increase local decline and foreign hostility

### Golem module

- quarries
- binding workshops
- heavy transport routes
- resource conversion
- repair and reconstruction pits

Tradeoff:

- more golems consume industry, resources, and movement capacity

## Reinforcement and military method lane

### Shared early goals

- organize starting formations
- recruit commanders or family equivalents
- establish a reserve method
- choose defensive or offensive use

### Zombie reinforcement

Methods:

- train base zombie units
- rally scattered derivative bands
- limited casualty recovery if safe
- capture local populations or manpower through explicit harsh decisions with real costs and condemnation where relevant

No advanced zombie variants.

### Ghost reinforcement

Methods:

- spawn units from manifestation anchors
- use long haunting missions in devastated or controlled states
- recover destroyed formations slowly through presence values

No ordinary training queue.

### Golem reinforcement

Methods:

- spawn units through quarry and industrial projects
- restore damaged golems through material expenditure
- capture construction resources

No ordinary manpower replication.

### Military doctrine forks

#### Concentrated Host

- fewer stronger units
- higher command coherence
- vulnerable to losses

#### Scattered Bands

- more local units
- better territorial coverage
- weaker concentration

#### Captured Auxiliaries

- permits limited ordinary or regional support units
- improves administration and combined arms
- creates loyalty and identity risks

The availability and exact effects vary by family.

## Aggression and expansion lane

Derivative countries are aggressively hostile to ordinary states. Expansion still follows strategic reach and coherent targeting so the AI fights everyone it can reach over time without issuing meaningless wars against inaccessible countries.

### Former Parent War

Early focuses support:

- defend against reconquest
- seize former muster districts
- target depots that supplied the revolt
- exploit parent claimant networks

### Adjacent Weak-State Pressure

The derivative can claim or target nearby states that provide:

- sustainment resources
- coherent borders
- family anchors
- population or industry
- rail connection

It should not receive unrestricted global war goals.

### Regional Host Ambition

Late expansion can create:

- a coherent regional country identity
- claims on a bounded region
- subject or tributary options where appropriate
- family-specific occupation and integration decisions

### Postwar handling

Conquered states do not receive instant full integration by default.

The package uses:

- family-specific integration missions
- compliance or local presence
- supply and anchor construction
- slow claims-to-cores progression only when appropriate
- resistance and population consequences

## Family-specific transformation lane

### Zombie derivative transformations

Possible focus group directions:

- mend fragmented command
- choose controlled recruitment versus unrestrained growth
- create disciplined base-zombie formations
- negotiate or destroy surviving human officers
- decide whether ordinary auxiliaries have a place

Final route outcomes:

- disciplined dead host
- proliferating fragmented bands
- claimant-led war host

All remain below parent zombie escalation power.

### Ghost derivative transformations

Possible focus group directions:

- bind manifestations to places
- choose slow habitation versus predatory haunting
- organize a ghost command chorus
- control population drain
- establish a capital anchor

Final route outcomes:

- stable spectral state
- wandering procession
- claimant-bound haunting

All use slow wasteland and population effects.

### Golem derivative transformations

Possible focus group directions:

- choose central pattern versus independent constructs
- expand quarry and binding capacity
- improve mobility at material cost
- create smaller support constructs or preserve a few heavy hosts
- decide whether human technicians remain

Final route outcomes:

- centralized stone host
- distributed construct communes
- claimant master-builder state

All remain weaker than the parent golem route.

## Late regional predator outcome

The tree’s capstone should make the derivative a serious regional threat without granting a world-end mechanic.

Requirements can include:

- survive the former parent war
- control a bounded regional set
- resolve Species Burden to a final form
- establish sustainable reinforcement
- complete a hierarchy route

Payoff direction:

- stronger regional claims or war plans
- improved family reinforcement
- final flag or cosmetic identity
- route-specific leader or council state
- achievement eligibility
- possible major news event if the country becomes regionally dominant

A normal event popup or news event is sufficient. No super-event is required by this source design.

## Decisions for derivative countries

### Secure a Muster Depot

Targeted state decision to capture, repair, or protect a depot.

### Rally Scattered Formations

Reinforcement decision using family-specific resources.

### Break the Former Parent’s Command Net

Targets the former parent’s claimant or event formation infrastructure.

### Establish a Family Sustainment Site

Zombie, ghost, golem, or future family version.

### Integrate a Conquered District

Timed state mission with family-specific costs and consequences.

### Suppress Internal Fragmentation

Improves cohesion at a real military or political price.

### Demand Local Submission

Expansion action against an adjacent weak state. AI checks strategic validity and avoids impossible naval targets.

### Preserve or Replace the Claimant

Hierarchy-specific decision chain.

## Derivative AI strategy

### Shared goals

1. survive the opening war
2. secure headquarters and supply
3. consolidate starting units
4. obtain family reinforcement
5. target former parent assets
6. expand into coherent adjacent territory
7. avoid suicidal distant wars

### Zombie AI

- values population and accessible land
- trains base zombies when sustainment permits
- favors quantity under fragmented route
- favors concentration under claimant route
- does not seek parent zombie mutations

### Ghost AI

- values devastated, low-control, and anchor-capable states
- avoids wasting spawn-only units in repeated frontal attacks when weak
- uses slow pressure and regional expansion
- does not trigger parent Death logic

### Golem AI

- values resources, quarries, industry, rail, and supply
- preserves expensive units
- expands slowly until reinforcement is secure
- avoids broad low-value fronts

### Diplomacy AI

Derivative countries regard ordinary countries as eventual enemies. Outside the triggerable scenario, they secure the opening revolt before beginning a continuing sequence of aggressive wars against reachable targets.

They can:

- accept a short tactical nonaggression arrangement when facing destruction
- trade or receive covert aid only when it supports later aggression
- refuse ordinary faction membership unless a route permits it
- create limited regional subjects or auxiliaries
- resume aggressive expansion once the immediate survival crisis passes

The triggerable scenario can override this caution and force immediate wars.

## Defeat and cleanup

When a derivative country is defeated:

- parent-event systems remain untouched
- surviving family units are destroyed, transferred, contained, or converted only through explicit safe rules
- Event 19 derivative flags and event targets are cleaned
- former parent receives an aftermath decision or incident
- slow ghost wasteland or population effects stop or decay under their own rules
- claimants are removed, captured, killed, exiled, or returned through a resolved event
- focus and decision categories close
- shared classification remains correct for any surviving exiled or relocated derivative actor

## Country package acceptance criteria

Every derivative family package is complete only when it has:

- safe dynamic creation or an explicitly approved tag alternative
- public names and adjectives
- distinct flags in three sizes
- leader or collective identity
- fixed identity-scene coverage
- ruling politics
- starting ideas with lifecycles
- starting territory and capital rules
- starting units based on actual revolting formations
- economy and supply setup
- reinforcement path
- 25 to 35 focus-scale route content or equivalent shared modules
- decisions and missions
- route-specific AI
- postwar integration
- parent isolation
- shared special and nonhuman classification
- defeat cleanup
- documentation and asset manifest coverage

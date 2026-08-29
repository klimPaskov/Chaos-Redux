# Murder Mystery Specification Part 5: International Cell Network

## Network purpose

The international network makes Evolution II and later globally reactive without turning every country into a daily scripted workload. The system tracks only countries with an Event 39 cell, a recent immunity state, an active cooperation role, or an Assassin derivative package.

## Bounded cell registry

The owner system maintains an aligned registry of active cell countries and their event-owned state. Each row has a stable country reference or safe replacement identity, cell stage, maturity, Local Case Progress, exposure, current threat role, last incident date, last investigation result, inherited evidence level, revolt readiness, immunity state, and current movement parent.

The registry must remain sparse. It adds a country only when a cell is seeded, a country begins active cooperation, a derivative is created, or a short-lived immunity record is needed. It retires rows after full cleanup and immunity expiration.

## Cell stages

| Stage | Working role | Gameplay |
| --- | --- | --- |
| 0 | None | No active cell and no scheduled Event 39 incident |
| 1 | Rumor | A route or supporter exists, but no operational capability |
| 2 | Active Cell | Local murders, protection threats, and investigation actions are possible |
| 3 | Entrenched Cell | Institutional infiltration, safe houses, mature recruitment, and escape routes |
| 4 | Insurrection Cell | Territorial revolt preparations, local cadres, and foreign support routes |
| 5 | Territorial Movement | A foreign Assassin derivative exists and owns the local movement package |

Stage changes follow concrete actions. Network Reach and Chaos permit higher stages but do not create them without a valid seed, survival, or revolt result.

## Network size budgets

The event should use dynamic caps that reflect current phase and world capacity. The caps are tuning bands, not immutable constants.

| Phase | Normal active foreign cell range | Hard design purpose |
| --- | --- | --- |
| Early Evolution II | 2 to 5 | Teach international defense and cooperation |
| Mature Evolution II | 4 to 10 | Create real global pressure without universal coverage |
| Evolution III | 5 to 12 | Support the new state while governments can still contain cells |
| Evolution IV | 8 to 18 | Permit several revolt candidates and subject routes |
| Evolution V | 12 to 28 | Endgame network, still bounded below all ordinary governments |

The system should lower caps for small multiplayer worlds, extensive country collapse, performance pressure, or many active complex events. It should raise caps cautiously in a large intact world. A cap blocks new cell creation, not existing local resolution.

## Seed routes

A cell may be seeded by:

- an escaped courier or witness from the original host
- a foreign safe house revealed during a failed mission
- a completed Assassin focus or decision
- a mature subject network
- transport access through a border, port, faction, subject, volunteer, or commercial route
- a major public murder that produces imitators in a vulnerable country
- an Event 39 cluster interaction that supplies a valid intelligence route
- the Assassin Network scenario setup

A country does not receive a cell merely because it has low stability. There must be a plausible event-owned route or a bounded network spread action.

## Country weighting

Eligible countries receive seed weights from:

- shared border with an active cell or Assassin country
- sea or transport access to a known route
- diplomatic, faction, subject, volunteer, or trade contact with an active node
- weak counterintelligence
- low stability or active civil conflict
- exposed leadership after another event
- recent occupation, exile, or government transition
- a local high-value target pool
- existing radical or underground pressure supported by an explicit integration

Weights fall for:

- strong intelligence agencies
- recent cell dismantling immunity
- high protection coverage
- active allied evidence sharing
- no safe target or office-casualty path
- special Chaos or nonhuman classification
- an incompatible event-owned country transition
- no valid future revolt territory when Evolution IV is the intended seed purpose

## Local Case Progress

Each affected country has Local Case Progress from 0 to 100. It uses the same public stage names as the original case but begins with inherited evidence. Local progress is easier to gain because target profiles and methods are known.

The local case can end in:

- cell dismantled, which removes the cell and grants immunity
- cell disrupted, which lowers stage and delays incidents
- cell escaped, which may move the cell or seed a route
- cell concealed, which hides public threat while maturity continues
- cell revolt preparation, which converts local play to counterinsurgency

Local Case Progress is retired when the cell is removed. The country retains only a short institutional memory or immunity state.

## Intelligence sharing network

Affected governments may join an Event 39 intelligence exchange. Membership is not a faction. It can include countries from opposing blocs when they share the threat.

Members can exchange:

- target profiles and attack methods
- captured route records
- false-document signatures
- witness testimony
- equipment and safe-house patterns
- border and port watch information
- operative liaison access

Sharing creates benefits and risks. A compromised member can leak information. A repressive member may provide poor evidence or create diplomatic conflict. A country may withhold information to protect sources, pursue unilateral capture, or conceal its own failures.

The exchange should use a compact cooperation state, not a second large visible value. The player sees membership, current shared evidence stage, and any active compromise warning.

## Network operations

### Route interdiction

A government targets a border, port, air route, or rail corridor linked to a cell. The action needs named geography, route access, and security resources. Success reduces the cell's escape and supply capacity. Failure can move the route or expose the government's method.

### Coordinated arrest window

Two or more governments synchronize raids so one cell cannot warn another. The operation requires sufficient shared evidence and compatible access. Success damages several cells and Network Reach. Failure can trigger a coordinated murder wave.

### Exchange protected-person protocols

Governments share protection methods for leaders and command staff. The action strengthens one office group across members for a limited period and creates adaptation if used repeatedly without new intelligence.

### Turn a captured courier

A country uses a captured cell member to feed controlled information. This can reveal a parent cell, protect a baited target, or expose a foreign route. It carries a risk that the courier remains loyal and compromises the operation.

### Expose state support

If an Assassin State exists, governments can reveal material support to foreign cells. This can change recognition, sanctions, covert action, faction behavior, and public Network Reach. It should use proof gathered through the case, not an automatic diplomatic penalty.

## Murder handling abroad

The first incident in a newly affected secondary country should normally be an attempted attack, generic office casualty, or discovered plot. Named deaths become possible after the cell has matured or the government has ignored a public warning state.

A national leader death abroad requires safe succession, a mature cell, a high-value operation, and a strong public consequence. It should not become the default way every foreign cell proves it exists.

## Cell immunity and reseeding

A dismantled country receives a local immunity window whose length depends on the completeness of the operation, evidence sharing, border security, and remaining Network Reach. Immunity blocks ordinary reseeding. It can be broken only by a new concrete route such as a neighboring territorial revolt, a compromised cooperation member, a successful Assassin operation, or a terminal war action.

Repeated cells in one country should be rare and increasingly expensive for the movement. The event must not farm incidents, Chaos, or investigation rewards through endless reseeding.

## Territorial revolt readiness

A stage 4 cell accumulates revolt readiness through local maturity, captured arms, foreign support, government weakness, route access, and the Assassin State's focus and decisions. Government investigation, protection, garrison presence, supply control, cell arrests, and international support reduce readiness.

The player sees a public state such as dormant, preparing, imminent, or disrupted. Exact internal score components can remain hidden, but the tooltip must name the main actionable causes.

## Foreign split transaction

A foreign revolt uses the same map safety principles as the original Assassin State with smaller territory and stricter limits. It must produce:

- one connected or defensibly coherent state cluster
- a viable capital
- sufficient population for the starting force
- some industry or a bounded emergency grant
- supply access or a documented emergency supply solution
- a viable parent-government remnant
- no transfer of protected or unrelated event states
- no duplicate tag, cosmetic identity, or active country ownership

The revolt begins at war with the parent government, becomes a subject of the central Assassin State, and joins the Veiled Compact. Setup must be one idempotent transaction.

## Reduced derivative package

A foreign Assassin derivative receives:

- a dynamic public name tied to its parent region or country
- a fictional institutional or high-chaos leader package
- a reduced starting army with Assassin Cadres and one role-specific formation when affordable
- local security and recruitment ideas
- local cell ledger ownership
- a compact shared focus route or overlay content
- decisions for survival, reinforcement, central support, local infiltration, and postwar administration
- subject and faction AI
- no automatic access to the central terminal focus route

A derivative must be playable if a human switches to it. It cannot be an empty disposable tag.

## Central support

The central Assassin State can support a foreign revolt through equipment, volunteers, operatives, transport, intelligence, training, or a synchronized diversion. Support costs real resources and raises exposure. Supporting too many cells weakens central supply and Cohesion.

A foreign cell may revolt without full support only when local captured capacity is sufficient. Such revolts begin weaker and may demand autonomy after survival.

## Subject hierarchy

The Veiled Compact has one central movement actor. Foreign derivatives are subjects and faction members at Evolution IV. Their autonomy depends on the central route, local contribution, Cohesion, and whether the original movement leader survives.

Centralized routes can demand equipment, intelligence, and military coordination. Decentralized routes grant wider local freedom but reduce synchronized operations. Pragmatic routes may allow ordinary state administration and diplomatic agreements at the cost of ideological support.

## Movement inheritance

If the original Assassin State is defeated while a viable foreign derivative survives, the system evaluates one inheritance transaction. Candidates require:

- territorial survival
- minimum industry, population, and supply
- an active mature network
- sufficient Cohesion or local legitimacy
- no incompatible subject or terminal ownership
- a safe central leader package

The highest valid candidate becomes the movement heir, gains the central network ledger, and can continue Evolution IV or V content at a reduced state. All other derivatives rebind to it or become autonomous according to route and Cohesion.

If no candidate passes, the territorial movement ends. Surviving cells become hunted remnants with a bounded cleanup period. They cannot recreate a central state through endless inheritance.

## Global dismantling

Before Evolution III, global victory for ordinary governments requires the original core movement and every mature foreign cell to be resolved. Stage 1 rumor routes can be retired through aftermath without another full investigation.

After Evolution III, global victory requires the central Assassin State or heir defeated, all foreign derivatives defeated or detached from the movement, and every stage 3 or 4 cell dismantled. Lower-stage remnants enter cleanup and cannot trigger new evolution.

## Performance and ownership

Cell processing runs only over the event-owned registry. Incident schedules should be per-row dates or bounded queues. Spread actions select from a prefiltered candidate pool at event moments. No daily or weekly all-country scan is allowed.

Country invalidation, annexation, tag switching, subject transfer, and terminal state changes must revalidate or retire the row. The registry cannot retain dead country targets or stale movement parents.

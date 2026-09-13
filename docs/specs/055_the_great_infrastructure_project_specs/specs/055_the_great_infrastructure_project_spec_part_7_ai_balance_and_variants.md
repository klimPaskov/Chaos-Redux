# Event 55 Specification, Part 7

## AI, Balance, Rare Variants, and Failure States

## Balance objective

Event 55 begins with one of the strongest positive territorial rewards in the minor event pool. That strength is intentional.

Balance should preserve the opening reward and control its campaign effect through:

- one-time application per recipient
- strong preference for countries that have not received the event
- no automatic maximum infrastructure in future conquests
- project slot limits
- dynamic National Works Capacity
- long project durations
- real equipment and civilian construction commitments
- partner consent
- route disruption and maintenance
- limited repeat assistance

Reducing the initial grant to a small percentage bonus would remove the event's identity and is not an acceptable balance solution.

## Recipient scale

The opening grant naturally gives more absolute value to a large country because it owns more states.

The target system should not exclude large countries merely because the reward is strong. It should instead avoid repeated concentration and preserve world variety.

Suggested target principles:

- every valid ordinary country begins with a chance
- never-served countries receive the strongest preference
- recent recipients receive zero chance during a long cooldown
- countries with very few useful projects receive lower first-time preference unless a port, crossing, or compact project is valid
- fully capitulated or invalid actors receive zero
- a very large country should not be selected repeatedly while most countries remain unserved

The future probability audit must use the complete candidate pool before claiming exact odds.

## National Works Capacity balance

National Works Capacity should prevent a weak country from starting a project it cannot sustain without permanently locking small countries out.

A small country can reach the Ready stage through stability, a manageable route, strong equipment reserves, foreign support, and a low current burden.

A large industrial country gains more base capacity but also receives larger project scales and can overextend itself through simultaneous works.

Capacity should not rise only from factory count. That would make the system a major-power feature despite the event's random-country premise.

## Project cost scaling

Project cost should scale from:

- route length band
- terrain difficulty
- project family
- number of partners
- number of major nodes
- construction method
- current evolution
- current recipient economy

Economy scaling should avoid two failures:

- a fixed cost that is trivial for a major and impossible for a minor
- proportional scaling that makes a major pay so much that economic strength never matters

Use bounded bands with floors and caps. A major should pay more absolute equipment and carry more civilian burden for a continent-scale project, while gaining a larger route.

## Duration balance

Long projects need visible progress and useful intermediate events. They should not become passive timers.

Duration should respond to:

- route scale
- terrain
- construction method
- National Works Capacity
- evolution
- incidents
- partner performance
- war and embargo

Players should be able to estimate whether a project fits their campaign horizon before authorization.

An AI should avoid a project whose likely completion date falls beyond a reasonable strategic need when a smaller alternative exists.

## Reward balance

Completed projects should have strong local and route-specific effects.

Avoid unrestricted national stacking from repeated projects. Suggested safeguards include:

- local effects tied to route states
- one staged national institution idea instead of a new national spirit per project
- capped completion experience
- diminishing national trade benefit from several similar corridors
- one primary project family count per project
- network benefits that depend on critical nodes
- no repeated free supply hubs without strong route need

A country that completes several distinct project families should become a genuine logistics power. It should still remain vulnerable to war, route loss, fuel shortage, and embargo.

## AI design principles

AI should treat the system as a strategic investment problem.

It needs to decide:

- whether it can safely start a project
- which family best fits its geography and current needs
- which construction method fits its time pressure
- whether to accept a foreign invitation
- when to counteroffer
- when to suspend, reduce, repair, reroute, or abandon
- whether another active project would overextend the country

AI should not click every available project because the decision is positive.

## AI project start gate

An AI should normally require:

- a free project slot
- the required National Works Capacity stage
- the first phase costs
- a route that remains likely to be controlled
- no severe imminent capitulation risk
- no unresolved project emergency with higher priority
- a project benefit that fits current strategy

A poor or wartime country can still start an urgent lifeline when the route can finish soon enough and the cost does not destroy current defense.

## AI construction method

### Accelerated schedule preference

AI preference rises when:

- a front is supply-constrained
- famine relief needs a route
- an embargo makes a domestic resource corridor urgent
- a critical port or border connection is needed soon
- the country has strong current reserves
- the project is short enough that acceleration has strategic value

AI preference falls when:

- National Works Capacity is low
- the project is an extreme tunnel or bridge
- overrun risk is already high
- stability is weak
- the country has another active project

### Standard public works preference

This is the normal default when urgency and risk are balanced.

### Conservative engineering preference

AI preference rises when:

- the project is a tunnel, bridge, or extreme terrain route
- the country is at peace
- the route has high long-term value
- the country has strong civilian industry
- failure would sever an important international agreement

AI preference falls when the route addresses an immediate war or relief emergency.

## AI family priorities

### Railway

High priority for:

- wide continental countries
- land powers with weak rail links
- resource and industrial separation
- active supply problems
- countries with train reserves

### Highway

High priority for:

- compact or medium continental countries
- motorized armies
- industrial and urban belts
- poor all-weather access
- routes where another railway would duplicate existing capacity

### Trade corridor

High priority for:

- friendly regional blocs
- trade-oriented states
- complementary industry and resource partners
- countries seeking alternative transit
- countries with stable borders

### Tunnel or bridge

High priority only when:

- a validated crossing exists
- the strategic connection is important
- capacity and costs are strong
- partner willingness is high
- the current evolution allows it

### Grand port

High priority for:

- maritime countries
- island states
- convoy-dependent powers
- naval logistics hubs
- ports linked to resource or trade corridors

### Resource corridor

High priority for:

- remote valuable resources
- import dependence despite domestic deposits
- a new Event 18 discovery
- embargo pressure
- weak connection between source and industry or port

### Continental network

High priority only for:

- experienced hosts
- stable blocs
- high National Works Capacity
- several completed or linked projects
- no active war among core participants

## AI partner decisions

An AI partner should compare its contribution with its route share and strategic benefit.

Acceptance rises from:

- strong relations
- faction membership
- shared war or threat
- trade complementarity
- direct route states in its territory
- a useful port or resource terminal
- relief need
- prior successful projects with the host

Refusal rises from:

- hostile claims
- active war
- embargo participation
- weak capacity
- excessive requested burden
- low local benefit
- unstable route control
- dependence on a rival
- too many existing international commitments

Counteroffers should be common when the project is useful but the initial burden is unfair.

## AI response to project trouble

The AI should prioritize responses in this order:

1. Protect or repair a critical operational project needed for war supply or relief.
2. Resolve a suspended project near completion.
3. Reduce scope when full completion is no longer feasible but a useful route remains.
4. Reroute when one lost segment blocks an otherwise valuable corridor.
5. Abandon when recovery cost exceeds strategic value or the route is permanently invalid.

The AI should not pour resources into a tunnel whose terminal state is permanently held by a hostile great power.

## AI active project limit

AI should use fewer slots than the hard maximum when its capacity is marginal.

Suggested behavior:

- one project at baseline
- a second project under Evolution I only at very high capacity and without serious war pressure
- two projects under Evolution II when at least one is financially safe
- a third project under Evolution III only for an experienced, stable, high-capacity host

The AI should reserve capacity for repair when it owns a vulnerable fixed link or multinational network.

## Weighted logic evidence

Every weighted surface requires the future audit cycle:

1. Inspect the full weighted structure and candidate pool.
2. Define named scenarios.
3. Evaluate score ordering and hard zero cases.
4. Apply the owner-selected balance patch.
5. Compare the same scenarios after the patch.

Do not claim exact percentages from an incomplete country pool, project pool, or partner set.

The detailed scenario matrix is stored in `quality/055_the_great_infrastructure_project_probability_scenario_matrix.md`.

## Rare project variants

Rare variants should emerge from geography and campaign state. They should not be arbitrary easter eggs.

### Two coasts, one route

Conditions:

- one country controls meaningful states on two distant coasts
- a connected national route exists
- the route crosses several regions
- no completed equivalent project exists

Outcome:

- a coast-to-coast railway or highway proposal
- high national integration and trade value
- long duration and strong construction burden

### The desert spine

Conditions:

- Evolution I or II
- a long route crosses several desert states
- endpoints have major population, resource, industrial, or port value

Outcome:

- severe fuel, water, and maintenance pressure
- strong access and resource benefit
- high weather and overrun risk

### The mountain passage

Conditions:

- Evolution II
- a route crosses major mountain terrain
- no reasonable lowland route provides the same purpose

Outcome:

- tunnels, viaducts, and long survey stage
- high construction cost
- strong strategic shortcut and supply resilience

### The polar line

Conditions:

- Evolution I or II
- arctic or severe winter route
- important resource, port, or frontier endpoint

Outcome:

- seasonal incidents and high maintenance
- strong access to remote territory

### The iron lifeline

Conditions:

- active Great Embargo or severe import vulnerability
- an underused domestic resource state exists
- a route can connect it to industry or a port

Outcome:

- domestic resource corridor
- partial resilience against one shortage
- no removal of the wider embargo

### The relief artery

Conditions:

- severe famine, displacement, or relief-access problem
- a safe origin and destination exist
- a route can materially improve access

Outcome:

- project receives relief priority
- faster emergency construction method access
- commercial benefits are weaker until the crisis ends
- Famine and Migration consume the route through adapters

### The peace line

Conditions:

- two recent enemies are at peace
- relations have improved enough for negotiation
- a valid border corridor exists
- no current claims or preparations make cooperation impossible

Outcome:

- a difficult bilateral corridor
- strong diplomatic value if sustained
- high withdrawal risk

### The island chain

Conditions:

- Evolution III
- several registered strait crossings or port links form one connected chain
- every crossing and port has map evidence

Outcome:

- a network of fixed links and ports
- high maintenance and naval sensitivity
- strong movement and trade value

### The continental relief network

Conditions:

- Evolution III
- several countries face famine or displacement pressure
- multiple operational route nodes can be linked

Outcome:

- multinational relief network
- route capacity and reception benefits
- lower immediate commercial return
- strong cooperative achievement potential

## Rare incident variants

Rare incidents can deepen a project when their conditions are real.

### A route beneath the old route

A survey discovers an abandoned tunnel, old railway grade, military road, or unfinished prior project that can reduce time but increase safety risk.

### The city demands a station

A major population state near the route demands inclusion. Adding it increases cost and long-term value.

### The generals demand priority

During war, the military seeks exclusive route use. Accepting improves supply but reduces civilian and partner benefits.

### The port cannot take the traffic

A successful inland corridor overwhelms its terminal port, creating a grand port extension proposal.

### The missing standard

Partner railways or border systems prove incompatible. The host can fund conversion, accept delay, or operate a weaker transshipment system.

### The honest engineer

An internal report reveals a serious defect before completion. Repairing it costs time and preserves long-term reliability. Suppressing it risks later failure.

### The impossible schedule works

A rare accelerated project reaches a milestone without overrun and gains a modest permanent maintenance advantage. This should reward a real high-risk choice without becoming common.

## Failure ladder

Failure should escalate through clear states.

### Minor delay

A short schedule extension or limited extra cost.

### Major overrun

The project needs a new commitment, reduced scope, or temporary suspension.

### Segment failure

One route section or facility component must be redesigned.

### Project suspension

Construction stops until the cause is resolved.

### Abandonment

The project ends and receives stage-based salvage.

### Operational collapse

A completed project becomes Severed or Dormant after damage, loss of control, or agreement collapse. It remains repairable or renegotiable.

The event should avoid instant permanent deletion except when the physical object is deliberately destroyed and no restoration path remains.

## Exploit prevention

The design should prevent:

- repeated maximum infrastructure in newly conquered states
- repeat firing equipment farming
- survey refresh spam
- authorizing and cancelling projects to gain experience
- counting one multimodal project as several achievement families
- accepting partner contributions, cancelling, and retaining all equipment
- duplicate project objects after transfer or rerouting
- persistent route benefits after losing every critical state
- repeated one-time Chaos reduction from the same network
- fixed links that remain active after severe physical damage
- AI project loops that consume all trains or convoys during war

## Player challenge

A strong player should be able to use Event 55 for serious strategic planning.

The event should reward:

- choosing routes that solve real logistics problems
- timing long projects around war and industry
- maintaining equipment reserves
- negotiating fair partner shares
- building redundancy into networks
- using relief routes during humanitarian crises
- repairing critical nodes quickly
- avoiding vanity projects that the country cannot sustain

The event should remain a positive economic event. Failure creates stranded investment, diplomatic damage, and lost opportunity. It should not become a routine death or civil-war generator.

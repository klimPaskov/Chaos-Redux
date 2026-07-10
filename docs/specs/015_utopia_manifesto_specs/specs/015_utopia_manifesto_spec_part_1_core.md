# Event 15 Utopia Manifesto, Part 1: Core Event Design

All names in this specification are working labels, not final localisation.

## Event identity

- Event ID: `15`
- Event slug: `utopia_manifesto`
- Classification: Minor Fire-Once
- Cluster membership: none
- Canonical entry: `chaosx.nr15.1`
- Replacement rule: this design completely replaces the reserved World Tension Subsides event and its repeatable classification.

The event places a recovered or revived utopian manifesto in the hands of an economically modest country. The manifesto promises a society organized around common provision, useful labor, learning, local communities, and territorial demands justified by necessity. It also contains or attracts arguments for assignment, colonization, penal labor, forced unity, and the externalization of war.

An AI recipient always accepts the manifesto. A human recipient chooses whether to accept or reject it. Acceptance activates a new national system and replaces the country's current focus tree only when the country passed the replacement-safety gate. Rejection ends the event for that country and leaves the global fire-once event consumed.

## Playable promise

Acceptance begins a country transformation campaign rather than granting a national spirit and a line of bonuses. The player must answer four questions over several years.

1. Can the state provide enough food, housing, transport, tools, and reserves to make common provision credible?
2. Can people choose their work while shortages, war, and reconstruction demand particular skills?
3. Can a doctrine of taking land only when needed remain restrained once the country gains power?
4. Can a literary ideal survive administration, dissent, occupation, and foreign rivalry without becoming a coercive state?

The answer is built through the Commonwealth Ledger mechanic, a comprehensive focus tree, evolving decisions, route events, local integration projects, and a final national identity.

## Recipient fantasy

The ideal recipient is a minor country whose small scale makes radical institutional rebuilding plausible and whose limited industry gives the manifesto something concrete to solve. The event should often reach a random weak AI country, but an eligible human player should remain a meaningful candidate.

The event must avoid feeling like a punishment that deletes years of unique content. A player should receive the manifesto only when the current tree is generic, event-approved for replacement, or still shallow enough that replacement is a fair campaign transformation. The eligibility system is therefore part of the event's identity, not a hidden technical afterthought.

## Recipient selection

### Candidate classes

The selection pass builds three candidate pools in order.

1. Eligible human players.
2. Eligible AI minors with generic or approved replaceable trees.
3. Eligible AI minors with lightly developed non-generic trees that are explicitly safe for replacement.

The first nonempty class is used. Within that class, the final recipient is chosen by a weighted weak-country score.

This priority keeps the event relevant to players without forcing it onto a major or an established bespoke campaign. It also guarantees that the event can normally find an AI recipient when no player qualifies.

### Hard exclusions

A country is excluded when any of the following is true.

- It is a major country.
- Its industrial capacity exceeds the event's upper safety band.
- It is a faction leader with a large subject or member network.
- It is in a civil war, near capitulation, or under an active country-replacement sequence.
- It is a special Chaos country, nonhuman country, terminal scenario actor, or world-end actor.
- It was created by another event and is using that event's country package or focus tree.
- It is currently using a focus tree that the repository marks as protected from replacement.
- It has completed enough political or identity focuses that replacement would erase a mature route.
- It lacks a valid capital or controllable core territory.
- It is a subject whose overlord relationship makes independent constitutional transformation impossible, unless the event-specific subject route is enabled by implementation review.
- It already has the Utopia Manifesto event state.

### Weak-country score

The weighted score should prefer countries that have a reason to gamble on the manifesto.

Positive factors include:

- low civilian, military, and naval factory count
- a generic or repository-approved replaceable focus tree
- limited research capacity
- low infrastructure or weak internal transport
- high unemployment represented by unused manpower, low mobilization, or route-appropriate proxies
- refugee or migration pressure from compatible events
- weak international position without an immediate fatal war
- a small number of controlled states
- a coastal or island situation that can support the island-society fantasy
- a landlocked capital that can support the Inland Island variant
- human control, provided every safety gate passes

Negative factors include:

- active offensive war
- high industrial growth already underway
- major-power guarantees that make early external cases trivial
- extensive colonies or occupied territory
- many subjects
- a large completed focus count
- a strong unique tree
- current domination of a region
- recent receipt of another full country transformation event

The score should use shared tuning bands rather than one brittle factory threshold. The implementation should expose the important rejection reason in debug and manual-fire tools, while ordinary player-facing text only needs to communicate that the manifesto has appeared in a country able to attempt it.

### Human fairness rules

When an eligible player is selected, the opening option that accepts the manifesto must clearly warn that the country's current focus tree will be replaced. The warning should explain the scope of the transformation without listing hidden branches.

The reject option must be real. It should not apply a crippling penalty, fire a civil war, or secretly force the route later. Rejection represents a government deciding that the document is too disruptive or too uncertain to become state doctrine.

The event remains fire-once after rejection. This preserves the user's requested event identity and prevents a player from repeatedly refusing until another country receives it.

## Opening event chain

### Stage 1: recovery

The source of the manifesto varies with country context.

- An island or maritime country may recover a translated copy through a port library, religious house, customs archive, or private collection.
- A landlocked country may receive a copied manuscript through a university, refugee network, antiquarian society, or exiled political circle.
- A socialist or labor-oriented country may revive it as an old precursor to common ownership.
- A democratic country may present it as a constitutional provocation.
- An authoritarian country may treat it as a manual for measured order and self-sufficiency.
- A country with strong religious institutions may debate its moral and communal claims.

The event description direction should focus on the book's physical return, its rapid circulation, and the competing groups that find useful passages in it. It should not summarize the entire future system or announce that the book is dangerous.

### Player options

#### Accept the manifesto

The speaking voice is the government or head of state choosing to convene a public interpretation and reconstruction program. The tone should fit the country's existing ideology. Democratic acceptance should sound open and provisional. Socialist acceptance should sound collective and material. Neutral acceptance should sound practical. Fascist acceptance should sound confident and disciplinary.

Visible consequence direction:

- the current replaceable focus tree will be replaced
- the Commonwealth Ledger will open after the initial survey
- the country will begin an interpretive congress
- existing military and map ownership remain intact

Hidden route details, evolution gates, final identities, and achievement conditions must remain unspoken.

AI always chooses this option.

#### Reject the manifesto

The speaking voice is a government deciding that a literary plan should not become a constitutional program. The tone can be skeptical, cautious, amused, or hostile according to ideology.

Visible consequence direction:

- the event ends for the country
- the focus tree remains unchanged
- the manuscript may remain a cultural curiosity through a short-lived, low-impact modifier or a one-time research effect only if that addition improves closure

The rejection outcome must not create a second full route.

### Stage 2: public circulation

Acceptance begins a short preparation period before the new tree becomes fully active. The country receives a temporary Found Manifesto idea that represents public debate, administrative distraction, and intellectual enthusiasm.

The preparation period produces three immediate tasks.

1. Translate and publish a usable edition in the country's political language.
2. Survey households, occupations, stores, transport, housing, and state capacity.
3. Convene an interpretive congress that establishes how literally the text will be followed.

The new focus tree loads immediately or at the safest supported transition point. Its opening focuses represent these tasks, so the player is never left without a route.

### Stage 3: the first ledger

The survey establishes initial values for Need, Plenty, Concord, and Choice versus Assignment. Starting values are dynamic.

- A poor or blockaded country begins with high Need and low Plenty.
- A stable democracy begins with higher Concord and Choice.
- An authoritarian country begins nearer Assignment.
- A country with extensive occupied territory begins with lower Concord and greater territorial contradiction.
- An island country begins with a modest advantage in the island-society project.
- A landlocked country begins with a stronger Inland Island requirement and no penalty for lacking a coast.
- A subject begins with dependency pressure if the implementation approves subject eligibility.

The first ledger should make the player's starting problem readable. It should not predetermine the route.

## Baseline campaign flow

### Phase 1: interpretation and survival

The player establishes the public edition, surveys the country, opens common stores, and chooses initial labor rules. The immediate goal is to keep the country functional while the old institutions are being measured and reorganized.

Key pressures:

- shortages
- administrative overload
- elite or property resistance
- worker and household expectations
- the risk of promising more than the country can provide

### Phase 2: institutions

The interpretive congress commits the country to a political route. The player develops callings, housing, public works, defense, trade, and local government. Focuses begin to unlock route-specific decisions rather than simply granting modifiers.

Key pressures:

- Choice versus Assignment
- reserve targets
- regional imbalance
- religious and political dissent
- the treatment of property and local autonomy

### Phase 3: external need

The country decides whether its shortages can be solved internally. If they cannot, it can open a Necessary Ground case. Peaceful routes use purchase, lease, migration, and joint administration first. Coercive routes can escalate faster.

Key pressures:

- whether the claimed need is genuine
- whether the target has a fair alternative
- whether the country can house and supply settlers or refugees
- whether local people accept the arrangement
- whether foreign powers see a small experiment or a new expansionist doctrine

### Phase 4: commonwealth or closed island

The country forms associate municipalities, a cooperative league, a planned regional network, or a closed and militarized island-state. The final identity depends on route, values, conduct, and external relationships.

The late game should continue after formation through integration, league politics, aid, defense, and ideological competition. Formation is a major payoff, not the end of play.

## Core route families

The interpretive congress opens five coherent interpretations.

1. **Consent of Households**, a democratic and voluntary social commonwealth.
2. **Common Table**, a council-socialist system of common ownership and worker governance.
3. **Guardians of Measure**, a technocratic planning state centered on surveys, quotas, and standardization.
4. **Closed Island**, an authoritarian system that uses unity, assignment, and necessity to justify exclusion and coercion.
5. **The Joke Understood**, a hidden humanist route that treats the manifesto as satire and reforms institutions without making the book infallible.

The route labels are structural. Implementation writes final focus names and player-facing prose.

## Event memory and connections

Event 15 should remember important conduct rather than only the final ideology.

Persistent conduct flags or equivalent records should distinguish:

- accepted or rejected manifesto
- voluntary or assigned labor dominance
- first common-store success or failure
- first external Need case
- peaceful acquisition, coerced acquisition, or unjustified acquisition
- first local charter
- first integration by consent
- first use of penal labor
- first use of auxiliary mercenaries
- league creation
- final commonwealth formation
- hidden humanist interpretation
- high-chaos Perfect Island path

These records support route events, achievements, AI reactions, and the final super-event variant.

Optional soft connections can respond to nearby Chaos Redux concepts without becoming prerequisites.

- Independence Wave can make local autonomy and associate status more attractive.
- Tensions Rising can increase the cost of external Need cases.
- White Peace can support arbitration and demilitarized settlements.
- End Subject Status and Autonomy can affect a subject recipient or associate municipality.
- Collaboration can alter local integration calculations.
- Demilitarization can support a peaceful island-defense variant.
- The Book should remain thematically distinct. Event 145 is a demonic power text for a major or player. Event 15 is a political thought experiment for a weak country.
- Pacifism can strengthen nonviolent settlement routes.
- Immigrations can create genuine housing and settlement Need.
- The Free World can react to a mature voluntary commonwealth if that event is later implemented.

No connection should make Event 15 impossible when the other event is disabled or unreworked.

## Design boundaries

- The event does not turn every recipient into the same ideology.
- The event does not give instant cores or free industrial parity with majors.
- The focus tree does not consist mainly of new national spirits.
- The decision system does not become a political-power store.
- The territorial doctrine does not make every shortage a free war goal.
- The humane routes do not receive coercive tools without political and social consequences.
- The authoritarian route is not an unrelated villain branch. It grows from the manifesto's real tensions around necessity, assignment, colonization, slavery, and unity.
- The hidden humanist route does not become the only correct route. It offers adaptability and civil liberty, but it sacrifices the strongest planning efficiencies and the easiest route to rapid transformation.
- The final state identity must remain readable on the map and must use route-specific cosmetic identity rather than replacing the original tag by default.

# Event 018 Resources Found Specification, Part 5

## Nonhuman cave country package

All names in this file are working labels for design structure. They are not final localisation.

## Country role

Evolution IV creates one persistent, fully playable, actual nonhuman country. The working label is **The Deep Host**. Its public identity should be short, original, readable on the map, and clearly nonhuman. It must not borrow the name of a real ethnic, national, religious, or folklore group.

The country is a slow territorial predator. It does not recruit people, manufacture equipment, or trade. It awakens brood formations from resource-bearing states and uses those states as anchors. Its military strength grows through captured strategic resources, while its operational weakness comes from speed, supply reach, organization recovery away from resource anchors, and vulnerability to concentrated hard attack.

The package must be playable by a human who switches to or begins controlling the cave country after emergence. It also needs competent AI because it will usually be AI-controlled.

## Tag and origin handling

The final tag must be checked against vanilla, Chaos Redux, and approved reference mods before assignment. The package should use one stable country tag for the persistent cave country.

The emergence effect needs to record:

- the origin field state
- the country that discovered the field
- the country that owned the state at breach
- the country that controlled the state at breach
- the origin continent
- the exploitation score
- the starting army count
- the original Event 018 resource ledger
- the date of emergence
- whether the player was the dispossessed owner

The country should set flags showing that it originated from Event 018 and that it is an actual nonhuman country. Shared country-classification triggers must recognize it. Other systems that affect ordinary civilians, politics, disease, migration, ideology, diplomacy, or manpower should exclude it through shared classification instead of event-local duplicate checks.

## Map creation

### Starting territory

The cave country begins with the field state. It should not receive a random surrounding empire at spawn. Its initial army and combat design provide the opening threat.

The state becomes the capital and first brood origin. Its original owner loses ownership and control. Cores, claims, and cleanup should follow the final country-creation pattern, with the cave country receiving the legal map basis needed to function.

### Last-state safety

If the field state is the final state of the owner, the transition can annex or remove the owner through normal safe country cleanup. The owner’s player should receive a clear defeat or continuation choice if the mod has an established pattern for switching to the cave country, an exile, or an ally. The specification does not require a guaranteed continuation for every map state, but it requires clean handling rather than an invalid owner.

### Capital and supply

The origin state must receive enough supply structure for the starting army to function. This can include a supply hub, infrastructure repair, local rail creation, or a cave-specific supply abstraction. The country should not receive a full ordinary logistics economy if its concept does not use it.

The best design is a hybrid:

- cave divisions still interact with terrain, supply, combat width, and fronts
- resource-anchor states provide cave-specific local supply and recovery
- long distances away from anchors create severe operational weakness
- captured railways and hubs help movement but do not replace the need for resource anchors

This preserves HOI4 counterplay and makes resource states strategically important.

## Public country identity

### Country name direction

The final name should imply an organized subterranean polity or host. It should be direct, short, and map-readable. Avoid agency names, humorous mine puns, and borrowed folklore labels.

### Adjective direction

The adjective should work for divisions, states, and diplomatic text. It should sound like the species or polity rather than a human nationality.

### Ideology and ruling identity

The country can use one existing ideology slot for engine compatibility, but its player-facing sub-ideology and party identity should be original and nonhuman. The ruling structure is a brood hierarchy organized around depth, mineral consumption, and command resonance.

The package is fixed-purpose, but fixed-purpose does not mean politically empty. Its internal focus routes can choose central command, distributed brood autonomy, resource-hoarding hierarchy, or aggressive surface adaptation.

### Party and institution direction

The ruling body should not read like a human parliament, ministry, or company. Internal institutions can include:

- a central brood command
- deep chambers or elder nests
- war-brood councils
- feeding or resource chambers
- tunneling castes
- armor-growing chambers
- memory or resonance keepers

These are direction categories. Final names require original writing during implementation.

## Leader package

### Leader identity

The leader is literally a cave monster. It is not a masked human, mutated miner, possessed official, or symbolic empty chair.

The leader should have:

- an original personal or species-specific name
- an epithet or office that communicates command role
- a generated nonhuman portrait
- a generated animated portrait package for the major emergence identity
- a static fallback
- nonhuman leader traits tied to brood command, armor, slowness, and resource hunger

Because the portrait depicts a nonhuman creature, it should not use human regional random-name pools. The implementation should assign one authored fictional name or select from a small original nonhuman pool designed for the species.

### Portrait direction

The portrait should show one intelligent cave creature in HOI4 leader framing. It needs a strong face or head structure, mineral armor, subterranean anatomy, and enough political presence to read as a ruler rather than a generic combat monster.

The animation can use subtle real source-frame changes such as slow breathing, eye or sensory-organ movement, mineral plate tension, dust fall, and low subterranean light changes. It must not use a filter pulse or a shifted still as final motion.

### Leadership variants

The focus tree can replace or modify the leader through route outcomes, but the package does not need many separate characters. Strong variants include:

- central sovereign creature
- collective brood council portrait
- war-form leader after military centralization
- continental world-end identity

Each visible replacement needs its own asset and localisation plan.

## Flag and emblem package

The cave country needs intentional generated flag art in normal, medium, and small sizes. The design should remain readable at 10 by 7 pixels.

The base flag direction should use:

- one strong central mineral or cavern symbol
- high contrast
- no readable text
- no borrowed national insignia
- a design that looks like a flag rather than a cropped illustration

The world-end transformation can use a distinct cosmetic flag or emblem if the country’s identity changes after continent consumption. Ideology variants should only be created when the country can actually use them. Do not make meaningless recolors.

A separate faction emblem is not needed because the cave country does not create a normal faction.

## Starting politics and laws

The country should begin with:

- no elections
- no ordinary party competition
- no manpower law progression
- no trade law progression in the normal sense
- no ordinary economy law progression unless a cave-specific substitute is required for engine functionality
- maximum hostility toward ordinary neighboring countries
- no diplomatic acceptance of faction invitations, guarantees, trade, military access, or volunteers

The player still needs visible internal choices. These belong to focus routes and resource-brood mechanics rather than democratic popularity.

## Starting national spirits

The package should use a small number of deep spirits with clear lifecycles.

### Mineral Carapaces, working label

Role:

- very high armor and hardness
- strong defense and breakthrough appropriate to the template
- resistance to ordinary soft attack
- high production cost is irrelevant because units are not built through equipment

Lifecycle:

- base form at emergence
- route-specific upgrades through armor adaptation
- possible weakness exposure after enemies complete hard-attack research or study captured remains

### Slow Blood, working label

Role:

- severe movement penalty
- lower strategic redeployment
- slower planning and pursuit
- possible terrain-specific mitigation underground, in hills, or in mountains

Lifecycle:

- partially mitigated through adaptation route
- never fully removed, because slowness is the core counterplay

### Resource-Born Broods, working label

Role:

- disables ordinary training and recruitment
- enables automatic unit creation from captured resource capacity
- removes manpower and equipment dependence
- explains the origin-state exclusion

Lifecycle:

- expands through focus and decision improvements
- changes spawn pacing and capacity conversion
- does not become ordinary recruitment later

### Surface Starvation, working label

Role:

- weak recovery and supply away from resource anchors
- penalties in low-resource states
- pressure to capture and hold strategic-resource provinces

Lifecycle:

- adaptation can reduce but not erase it
- world-end form can weaken it after continent consumption

### Untranslatable Command, working label

Role:

- blocks ordinary diplomacy and faction systems
- provides resistance to ideology and politics systems that assume human institutions
- supports special AI behavior

Lifecycle:

- remains throughout ordinary cave-country play
- world-end transformation can replace it with a stronger terminal identity

The exact number of spirits can be reduced if several roles fit cleanly into one staged institution. The package should avoid a stack of small passive ideas.

## Starting military package

### Division family

The cave country begins with one core division family, working label **Cave Monster Brood**. Variants can be unlocked later.

The base formation should have:

- very high armor
- high hardness
- strong defense
- useful breakthrough
- strong close-combat power
- low speed
- limited organization recovery away from anchors
- low or no manpower and equipment requirements
- no normal reinforcement cost
- low flexibility against prepared hard-attack forces

The unit should be extremely difficult for soft-attack infantry to remove. Anti-tank, tank destroyers, heavy guns, armor-piercing support, and strong armored formations should be the intended counters.

### Hard-attack counterplay

Enemy countries need a readable way to learn that hard attack matters.

The event can reveal this through:

- after-action reports
- captured plates or remains
- military survey decisions from Evolution II and III
- a global news or intelligence event after first battles
- emergency anti-armor aid decisions
- focus or research bonuses for threatened neighbors

The cave units should not be invulnerable. Serious hard attack must create a dramatic difference.

### Starting count

The opening count uses the 6 to 30 dynamic range defined in Part 4. The count is calculated once from origin exploitation and recorded for history and achievement checks.

### Deployment positions

Starting divisions should appear in the origin state and nearby controlled provinces if the engine supports safe distribution. They should not spawn encircled outside their territory or stack in a way that creates instant supply collapse.

### Commanders

The country can use a small set of fictional nonhuman commanders or a brood-command system that creates commanders through the focus tree. It should not use human portraits or names.

Commanders can represent distinct roles:

- siege brood
- tunnel brood
- armor brood
- pursuit brood
- anchor guard

The asset burden should remain proportionate. A small set of strong fictional commander portraits is better than dozens of generic creatures.

## No manpower and equipment economy

### Manpower

The country should not gain, lose, or consume normal manpower for brood creation. Combat casualties can reduce division strength and destroy divisions, but replacement should use the cave-specific resource system or automatic regeneration rather than a human population pool.

The player-facing manpower display can remain at zero or use a custom explanation. The country should be excluded from systems that interpret zero manpower as ordinary conscription failure.

### Equipment

The country should not produce or stockpile infantry equipment, artillery, tanks, aircraft, ships, or support equipment for its core brood divisions.

It should not receive ordinary production lines as the primary army system. Captured factories can be converted into cave-specific bonuses, excavation speed, anchor fortification, or enemy denial.

### Training

The training interface should not allow normal cave divisions to be queued. New formations appear automatically when captured resource capacity becomes active.

The human player needs a clear tooltip explaining:

- why training is disabled
- how resource capacity creates divisions
- current capacity
- current active formations
- next spawn timing
- which states are contributing
- which states are excluded

### Reinforcement

Existing cave divisions can recover through resource anchors and brood regeneration. Recovery should be slow away from resource states and stronger in active anchors.

A destroyed division frees capacity for a replacement after the normal spawn delay. This prevents permanent army collapse from one lost battle while preserving pacing.

## Captured resource capacity

### Core rule

Every captured state other than the origin state contributes:

**one cave division capacity for every 10 total strategic resources in that state, capped at 10 divisions per state**.

The total uses the state’s current strategic resources of all standard types. A state with 7 total resources gives no capacity. A state with 10 gives 1. A state with 48 gives 4. A state with 100 or more gives 10.

The cap applies to total resources in the state, not separately to each resource type.

### Control requirement

A newly occupied state should not grant immediate permanent capacity the hour it changes controller. The cave country must hold it continuously for an activation period, recommended around 30 days before modifiers.

This creates counterplay through rapid recapture and prevents combat-front flicker from spawning units.

### Anchor activation

During activation, the state becomes a **resource anchor** through a visible mission or state marker. Enemy countries can see that the cave country is consolidating the resource.

Activation can be slowed by:

- active combat
- state damage
- resistance from surviving defenders
- low cave organization
- deliberate resource denial or demolition
- enemy containment decisions

Activation can be accelerated by cave focuses and adjacent active anchors.

The implemented denial contract is exact. A completed controlled demolition visibly damages local output, adds 30 days to every activation attempt while the preparation remains unconsumed, and stores a one-shot capacity penalty of three. The penalty is applied only when an activation finally succeeds, is clamped at zero, and is then consumed. Recapture before activation interrupts the timer without deleting the preparation, geological reserve, or any Event 018 resource ledger. Liberation cleanup removes the denial and anchor identities through the same restoration project.

### Automatic spawning

Once capacity is active, divisions appear automatically at a paced rate until active cave formations equal total available capacity plus any protected origin allocation.

Spawning must not happen as an instant stack when several rich states fall. A queue or pulse system should create formations over time.

Suggested pacing direction:

- one division per active spawn interval
- interval shortens with several active anchors and focus upgrades
- newly conquered distant anchors spawn more slowly
- world-end transformation can accelerate the process

### Capacity loss

If the cave country loses a contributing state, its available capacity falls after a short grace period.

Existing divisions should not vanish instantly. When active divisions exceed capacity, the excess receives an **Unfed Broods** state with penalties such as:

- lower organization recovery
- lower reinforcement
- lower speed
- attrition or gradual strength decay
- reduced armor repair

The cave AI should prioritize recapturing anchors or disbanding the weakest excess formations through a controlled system if necessary. A human player should understand which states are supporting the army.

### Origin allocation

The starting divisions are protected as origin allocation and are not counted against later captured-state capacity. The origin state itself never contributes to the 10-resources-per-division calculation.

If the origin state is lost, the protected allocation should not disappear instantly. The country suffers a severe command and recovery crisis, and can be defeated if it cannot establish a new deep capital or retake the origin. The final balance can allow a late focus to designate one replacement deep capital, but this should be difficult.

## Resource-anchor state effects

An active anchor should:

- support local cave supply and organization recovery
- provide automatic brood capacity
- fortify or alter the state over time
- reduce normal civilian and industrial use
- attract enemy strategic attention
- expose the amount of capacity it provides in a tooltip

The state can lose normal resource output to the world market as the cave country consumes it. This creates global trade consequences and makes the cave expansion economically disruptive.

The exact method should avoid permanently deleting vanilla resources unless the world-end route intentionally does so. A dynamic modifier or occupation effect can represent consumption while allowing restoration after liberation.

## Economy and construction

The cave country does not use a normal economy, but the player needs things to build and manage.

### Resource conversion

Captured resources can provide:

- brood capacity
- anchor recovery
- tunneling progress
- carapace adaptation
- fortress growth
- world-end progress

### Captured factories

Factories can be converted into:

- faster anchor activation
- surface-material processing
- tunnel reinforcement
- faster focus or decision projects
- enemy-equipment study
- state fortification

The country should not become a normal industrial major producing human weapons.

### Construction choices

Useful cave construction or decisions include:

- deepen anchor
- reinforce tunnel mouths
- open a buried approach route
- create a surface feeding chamber
- consume industrial district
- collapse rail junction behind the front
- create an underground reserve route

These need map and balance effects. They should not be decorative names for small modifiers.

## Diplomacy and war

### Neighbor war rule

The cave country declares war immediately on all land neighbors at emergence. A refresh mechanism should declare war on new land neighbors created by expansion or political changes.

The refresh should avoid repeated war-goal spam and should not target countries with which it is already at war or countries that no longer exist.

### No ordinary peace

The cave country should reject ordinary negotiated peace, faction membership, guarantees, trade, military access, non-aggression pacts, and volunteer exchange.

A scripted containment or defeat settlement can exist only when the cave threat is broken or the world-end aftermath is triggered.

### Naval and overseas limits

The ordinary cave country is land-focused and slow. It should not build a normal navy or conduct routine naval invasions. Cross-continent emergence belongs to the world-end branch.

The country can cross narrow land connections and use captured ports only for supply if technically needed. It should not become a generic overseas empire before continent consumption.

## Air and naval forces

The baseline country has no air force and no navy. Its counterplay is land warfare, resource denial, and containment.

A late adaptation route can create anti-air resilience, burrowing defenses, or limited subterranean bypasses. It should not create monster aircraft or ships unless a later accepted expansion specifically designs them.

## Technology and research

The cave country needs a compact custom technology or focus-driven upgrade model.

It can begin with:

- basic land combat capability
- resource-anchor mechanics
- strong armor
- slow movement
- no human equipment production

Research or focuses can improve:

- armor resilience
- movement in selected terrain
- organization recovery at anchors
- spawn pacing
- hard-attack resistance within limits
- tunneling and fortification
- adaptation to urban or cold conditions

It should not use the full human technology tree as meaningful content. The implementation can hide invalid categories or use focus-driven technologies.

## AI identity

The cave AI should behave as a resource predator.

Primary goals:

- secure the origin state
- identify nearby high-resource states
- attack toward the richest reachable anchors
- maintain land adjacency wars
- avoid wasting the army in low-resource deserts when a richer route exists
- hold active anchors
- concentrate against enemies with high hard attack
- spawn and organize new broods
- complete continent consumption

The AI should prefer slow concentrated offensives rather than constant broad-front attacks. It can use several armored spearheads with anchor guards behind them.

## Country package completion standard

The cave country is complete only when it has a registered tag, safe emergence, map identity, original names and flags, literal nonhuman leader, portrait package, starting spirits with lifecycles, dynamic 6 to 30 division opening, unique templates, no manpower or equipment dependence, disabled normal training, automatic captured-resource deployment, anchor supply, land-neighbor war logic, focus tree, decisions, AI, localisation, assets, docs, shared classification, and defeat cleanup.

# Event 31 Random Terror specification

## Part 4: Evolutions and escalation

## Evolution model

Event 31 has five true evolutions.

The ordinary rise from one attack to a local cell, armed insurgency, coup, civil war, territorial actor, and defeat remains baseline progression.

An evolution changes the global character of the event.

It adds coordination, reach, territorial durability, a distinct extremist doctrine, or a global war structure.

An evolution should not fire immediately when its Chaos threshold becomes available unless Event 31 has never fired and the campaign begins from a manual scenario or an already evolved opening.

Active evolution pacing should normally use a delayed incident with a meaningful mean time to happen.

The following values are planning anchors.

| Evolution | Minimum Chaos tier | Normal active-event pacing anchor | Main change |
| --- | --- | --- | --- |
| Organized Cells | Gathering Storm | about `90` days after eligibility | local cells form stable regional organizations |
| Transnational Terror Network | Rising Chaos | about `120` days after eligibility | networks act across borders and maintain safe havens |
| Territorial Insurgency | Chaos Tier | about `150` days after eligibility | territorial actors become durable states and support cells abroad |
| The Jihadist International | Totalen Chaos | about `180` days after eligibility | one fictional jihadist movement gains international structure |
| The Final Jihad | World Collapse | about `210` days after eligibility | jihadist actors coordinate global uprisings and conquest |

Campaign state should modify these anchors.

Strong existing networks, multiple active countries, territorial victories, foreign sponsorship, failed government operations, high Network Reach, and captured capitals make an evolution more likely.

Widespread successful containment, collapsed networks, low active-country count, severe internal rivalry, and destroyed territorial actors slow the next evolution.

The evolution engine must distinguish exact timing evidence from score-only tuning. Final implementation needs named probability scenarios and a before and after audit.

## Evolved opening behavior

When Event 31 has not fired before an evolution becomes active, the first ordinary firing should begin at the new global level.

An evolved opening changes the number of countries, initial state stages, incident families, and available organization structures.

It does not replay every lower evolution as a sequence of immediate popups.

The evolution itself receives one log entry, then the opening event describes the current public form.

When Event 31 already has active crises, the evolution appears through a transition incident that changes existing networks and unlocks new content.

## Evolution enable and disable behavior

Every evolution has an independent enable state in Event Details.

A disabled evolution must not set its recorded flag, expose its hidden branch, change its incident pool, or become a prerequisite that blocks baseline resolution.

If one evolution is disabled, later evolutions that depend on its specific content remain unavailable unless the manual scenario provides a tightly scoped bypass for setup.

Baseline territorial actors continue to function when Evolution III is disabled. They remain smaller, less coordinated, and less durable.

Disabling Evolution IV removes the jihadist branch and therefore prevents Evolution V and The False Revelation.

## Evolution I: Organized Cells

### Public change

Previously disconnected cells begin sharing leadership, resources, intelligence, recruits, and safe locations.

The player sees coordinated attack waves, common organization identities, survivors relocating between states, and evidence of foreign or criminal support.

### New organization structure

Several active cells in one country or region can consolidate into a named fictional organization.

The organization receives:

- one fictional name and emblem
- one broad ideological or strategic profile
- one regional operating area
- one leadership form
- one current support source
- one rivalry or sponsor relationship when relevant
- one pressure contribution across its active countries

The identity must be specific enough to support player recognition but broad enough to remain fictional and non-operational.

Possible profiles include:

- revolutionary absolutists seeking state collapse
- ultranationalist restorationists seeking a fictional territorial order
- millenarian political cults seeking purification through violence
- criminal-political networks seeking protected rule and profit
- military splinter organizations seeking government takeover
- ethno-revanchist fictional movements tied to invented claims or alternate-history identities

A profile never treats an ordinary ideology or ethnic group as inherently terrorist.

### Coordinated attack waves

Several active states can receive incidents during one wave.

The wave should have a common public purpose, such as disrupting transport, freeing prisoners, testing government response, or retaliating for a raid.

It should not become several independent global event firings.

A successful government can break the wave by protecting key targets or capturing the coordinating cell.

### Survivor displacement

Suppressing one cell can send survivors into another state or country.

This result is more likely after a rapid operation with low intelligence and poor border control.

It is less likely after a clean intelligence success, a protected defection channel, or a joint operation.

### Sponsors and criminal support

An organized cell can gain one current support profile.

- foreign government sponsor
- criminal patron
- sympathetic territorial actor
- captured local revenue
- dispersed external donations
- coerced local extraction

The player must identify and address the actual profile.

Using a generic finance action against every profile should produce weak results.

### Government content

Evolution I adds:

- joint intelligence requests
- sponsor investigation
- organization-specific targeted raids
- coordinated-wave protection missions
- defection and amnesty channels
- regional information sharing

### AI change

Organizations should preserve their active network, relocate endangered cells, prioritize exposed transport and depots, and avoid wasting every cell in one attack.

Government AI should recognize when several incidents belong to one organization and target the shared support source.

### Escalation proof

Organized Cells is complete when at least one fictional organization can exist across several states, receive a recognizable identity, coordinate a wave, lose cells, relocate survivors, split, collapse, and appear correctly in event reports and Event Details.

## Evolution II: Transnational Terror Network

### Public change

Organizations establish international recruitment, transport, funding, propaganda, training, and assassination networks.

A network can act in a country where it has no permanent entrenched cell.

Weak states can become safe havens.

Several countries can face one connected crisis.

### Network Reach

Network Reach becomes a visible global Event 31 value after this evolution.

It measures the ability of connected organizations to project attacks, move support, create distant cells, and coordinate government takeover attempts.

Network Reach rises through:

- active countries in several regions
- undisturbed safe havens
- foreign sponsors
- captured ports and transport hubs
- successful demonstration attacks
- surviving territorial actors
- coordinated propaganda victories
- government failures that create international prestige

It falls through:

- exposed sponsors
- broken corridors
- defeated safe havens
- captured records
- coordinated international operations
- rival splits
- loss of territorial actors

Network Reach should change what the event can do.

Low reach limits the network to neighboring states and established cells.

High reach allows distant attacks, faster cross-border spread, foreign fighters, and synchronized takeover attempts.

### Safe havens

A safe haven is a country or territorial actor that permits the network to train, rest, store supplies, or direct foreign operations.

A safe haven can arise through state weakness, government complicity, an uncontrolled border region, or a territorial Event 31 actor.

The host receives political and military consequences.

Foreign powers can demand action, offer aid, conduct a raid where lawful and reachable, manipulate the network, or redirect it toward a rival.

A safe haven is not automatically a Muslim-majority country or a refugee area.

### Distant demonstration attacks

A high-reach network can attack an eligible country without a permanent cell.

The attack creates Traces or Local Cells only if survivors, copycats, or support links remain.

A distant attack should be rarer and more expensive for the network than an attack from an entrenched local cell.

### Foreign fighters

The network can recruit fictional foreign fighters after establishing reach and a viable route.

Foreign fighters add manpower and experience to territorial actors and can strengthen cells in another country.

They use existing unit types and do not create a custom battalion.

Disrupted routes, poor supply, rival factions, and government cooperation reduce their value.

### Cross-border takeover planning

Several organizations can coordinate coups, civil wars, or state seizures across neighboring countries.

The player should see evidence and emergency missions before the largest attempt unless intelligence capacity has completely collapsed.

A coordinated takeover is a major public event and can raise Chaos directly.

### Foreign-power choices

Foreign governments can:

- support counterterror forces
- exchange intelligence
- protect a border corridor
- sanction a public sponsor
- demand action from a safe-haven host
- conduct a limited intervention
- covertly manipulate a network
- redirect support toward a rival

Manipulation carries a serious blowback risk.

A state that uses the network against a rival can become a later target or public sponsor.

### AI change

Networks should compare safe-haven security, route distance, local pressure, sponsor reliability, and government weakness.

They should not attack every possible country merely because Network Reach is high.

Governments should prioritize corridors and safe havens that materially support their active cells.

### Escalation proof

Transnational Terror Network is complete when one organization can connect several countries, maintain a safe haven, conduct a distant attack, move support, lose a corridor, suffer sponsor exposure, and coordinate a cross-border crisis without duplicating national response systems.

## Evolution III: Territorial Insurgency

### Public change

Strong organizations hold towns, border regions, isolated states, training areas, or captured capitals.

They form territorial countries with divisions, leaders, economy, decisions, focus routes, diplomacy, and survival goals.

### Baseline relationship

Baseline can already create a temporary extremist country.

Evolution III changes quality and durability.

After the evolution:

- territorial actors are more likely to receive contiguous viable territory
- captured formations and equipment are more organized
- reinforcement systems are stronger
- several actors can coordinate or merge
- safe-haven support becomes more reliable
- neighboring countries receive more intervention choices
- territorial victory strengthens cells abroad
- defeat produces a wider network collapse

### Territorial control

Territorial countries manage Territorial Control, Network Authority, and External Supply.

Territorial Control reflects administration and military grip over held states.

Network Authority reflects the actor's ability to command cells and claim leadership.

External Supply reflects sponsors, corridors, ports, captured depots, and connected territory.

These values should appear in the actor's decision category and affect force growth, focus access, diplomacy, and collapse risk.

### State seizure

An organization needs an Armed Insurgency or Lost Local Control state, adequate local strength, a viable carrier identity, and a parent country able to survive the split or undergo a valid takeover.

Territory should normally form a contiguous enclave.

The first seizure should avoid a random isolated state when a connected area exists.

The parent keeps at least one viable core state unless the result is a government takeover.

### Military and police defection

Defections can transfer a bounded portion of units, equipment, commanders, and local control.

The transfer should reflect actual units and stockpiles.

It must not create advanced equipment or an entire army from nothing.

### Parent missions

The parent country gains:

- Retake the Lost State
- Restore Civil Authority
- Secure Relief Corridor
- Isolate the Enclave
- Expose the Sponsor
- Negotiate Local Surrender when valid

### Regional reactions

Neighbors can intervene, blockade, support the parent, sponsor the actor, accept refugees, protect a border, or exploit the conflict.

The response depends on ideology, relations, rivalry, faction, claims, border access, and fear of spread.

### Actor survival outcomes

A territorial actor can:

- be defeated
- negotiate surrender
- remain a frozen enclave
- merge with another Event 31 actor
- split through rivalry
- conquer the parent
- become a sponsor and safe haven
- enter the fictional jihadist branch after Evolution IV

### AI change

Territorial AI should defend supply and capitals, secure contiguous states, raise existing unit types, avoid suicidal fronts, support connected cells, and seek a sponsor when isolated.

It should attack the parent or adjacent strategic states before distant prestige targets.

### Escalation proof

Territorial Insurgency is complete when a created actor can survive for a meaningful campaign period, raise forces through real resources, use a focus route, support cells abroad, lose supply, split, merge, conquer its parent, and be cleanly defeated.

## Evolution IV: The Jihadist International

## Public change

One fictional jihadist current emerges from the wider network and attempts to bind several organizations into an international movement.

It declares secular governments, rival Muslim movements, nonbelievers, and Muslim governments that reject its authority to be enemies.

The branch is specific to Event 31 and appears only after Evolution IV.

### Representation rules

The movement must remain fictional.

Its name, leaders, flag, emblem, doctrine, institutions, and territorial claims are invented.

It must not use the name, iconography, slogans, uniforms, sacred calligraphy, or propaganda of a real organization.

Its leaders cannot be generated caricatures of a real ethnicity or religious community.

The movement's claim to religious authority is publicly contested.

Muslim clerics, communities, governments, soldiers, and rival movements can condemn it, organize resistance, protect civilians, dispute its claims, and fight it.

Religious opposition must change gameplay through legitimacy, defections, local support, resistance, recruitment pressure, and diplomacy.

### International Unity

International Unity becomes visible after this evolution.

It measures cooperation among jihadist organizations and territorial actors.

It rises through:

- shared offensives
- recognized leadership
- successful mergers
- captured symbolic capitals
- foreign-fighter flows
- victories over rival governments
- common enemies
- defeat of internal challengers

It falls through:

- doctrinal rivalry
- competing leaders
- sponsor conflict
- defeat
- loss of territory
- religious and civic rejection
- exposed atrocities
- unequal distribution of supplies
- failed offensives

High unity unlocks coordinated wars, common faction behavior, and the path to Evolution V.

Low unity creates splinter wars and weakens foreign-cell control.

### Faction and coordination structure

The movement can create an event-owned faction or coordination structure.

Only Event 31 jihadist actors can become full members.

Ordinary Muslim-majority governments cannot join through generic ideology logic.

Cannibal actors cannot join under any condition.

Membership requires a compatible Event 31 route, a minimum authority contribution, and no active rivalry that blocks cooperation.

Members can refuse a leader, compete for authority, leave, split, or fight one another.

### Priority enemies

The movement initially prioritizes:

- its parent country
- adjacent weak governments
- states controlling its claimed fictional core areas
- Muslim-majority governments it labels false regimes
- rival jihadist factions
- Event 14 cannibal actors when practical
- governments actively dismantling its safe havens or foreign routes

The Muslim-majority classification is used only for actor-specific reaction and enemy priority after this evolution.

It never affects ordinary Event 31 vulnerability or recruitment.

### Captured territory

Captured states can face forced rule, expulsions, destruction, prison systems, coerced extraction, and mass killing.

These actions cause real population loss and can add Condemnation.

They also damage long-term control and can create resistance, defections, and foreign intervention.

The route should not reward atrocity without a strategic cost.

### Muslim opposition content

Eligible governments and communities can receive:

- public rejection by fictional religious councils and local leaders
- protection of worship and community sites
- local defense and civil-protection committees
- safe passage for threatened civilians
- defection appeals to foreign fighters and low-level members
- regional conferences against the movement's authority claim
- joint military operations
- public documentation of forced rule and atrocities

These actions can lower the movement's International Unity and Network Authority.

### Rival jihadist factions

Not every jihadist actor accepts one leader.

Rival factions can fight over doctrine, territory, sponsors, prisoners, and recognition.

The government can exploit the split, but the conflict can also increase civilian deaths and create new splinters.

### AI change

Jihadist AI should pursue its parent, adjacent strategic territory, rival Muslim governments, internal rivals, and network objectives according to strength and access.

It should not launch distant wars it cannot supply.

Muslim-majority government AI should treat the movement as an actor-specific threat and prioritize protection, rejection, border defense, and coalition support according to capacity.

### Escalation proof

The Jihadist International is complete when the fictional movement can form, receive distinct assets and leaders, recruit foreign fighters, create several actors, unite or split, attack rival Muslim governments, face Muslim religious and military opposition, and interact with Condemnation and Deaths without changing baseline target rules.

## Evolution V: The Final Jihad

### Public change

Jihadist countries and connected networks attempt global political and military unification behind an apocalyptic leadership.

Cells become coordinated uprisings during major offensives.

Territorial actors merge or enter a shared command.

Governments with severe Terror Pressure face higher takeover risk.

### Final command

A dominant leadership is selected from existing jihadist actors through Network Authority, territory, victories, capitals, International Unity, and surviving organization strength.

The final command can be contested.

A failed leadership contest can delay unification, start a jihadist civil war, or create two rival global fronts.

### Coordinated uprisings

When a member launches a major offensive, high-pressure countries can receive synchronized uprisings behind existing cells.

An uprising requires real prior pressure or an established cell.

The evolution does not create an unsupported rebel army in every country.

The strength of each uprising scales with:

- Terror Pressure
- active state stages
- local captured equipment
- military defections
- connected corridors
- Network Reach
- nearby territorial actors
- government legitimacy and readiness

### Global conquest campaign

The shared command sets strategic goals.

- secure connected regional blocs
- capture member and enemy capitals
- preserve foreign-fighter corridors
- destroy rival Muslim governments
- eliminate cannibal rivals
- break major counterterror coalitions
- raise International Unity
- create the territorial proof needed for the terminal branch

### Recruitment and strength

The movement gains strength from instability, occupied population, captured depots, controlled industry, safe havens, foreign fighters, and connected high-pressure states.

Deaths alone do not generate free manpower.

Civilian suffering can raise fear and chaos, but force growth still requires population, equipment, supply, or defections.

### Government response

Governments gain emergency coalition, capital defense, corridor, resistance, defection, and intervention content.

A country with high Response Legitimacy should have stronger local resistance and weaker uprising conversion.

A country with low legitimacy can face faster seizure even with a large army.

### False Revelation eligibility

Evolution V makes The False Revelation eligible for later readiness testing.

It does not fire the world-end branch.

The branch still requires:

- World Collapse Chaos
- an enabled public branch toggle
- substantial territorial success
- widespread active crises
- high International Unity
- a major strategic victory
- hidden Apocalyptic Readiness
- no existing world end
- its own delayed trigger

### AI change

Final-command AI should coordinate fronts, support uprisings where they can matter, preserve supply, avoid isolated prestige wars, merge actors when the transaction is safe, and suppress internal rivals that threaten command.

Government AI should prioritize capital continuity, connected coalition defense, restoration of high-pressure states, and destruction of the network's command and supply structure.

### Escalation proof

The Final Jihad is complete when existing networks can support synchronized uprisings, territorial actors can merge or coordinate, the movement can run global objectives, governments can form an effective response, and the terminal branch remains separately gated.

## Evolution log requirements

Each evolution records one shared evolution entry with:

- Event 31 as the source event
- the accepted evolution name
- the evolution stage and tier
- the relevant actor when the milestone belongs to one country or territorial organization
- the actual date
- enabled state

The main Evolutions history and the selected event's related-evolution history show the real log metadata.

The Event Details evolution catalog shows the public premise without a fake date or sequence number.

A disabled evolution does not produce a record or set content flags.

## Cross-evolution continuity

Existing organizations should be upgraded in place when possible.

A named Organized Cells actor can become transnational, territorial, jihadist, and part of the final command without losing its history.

A local baseline actor can remain secular or regionally focused after Evolution IV.

The jihadist branch does not convert every Event 31 organization.

Rival secular, criminal-political, nationalist, cult, and military-splinter actors can survive and fight the international movement.

This diversity prevents one late evolution from erasing the rest of Event 31.

## Completion standard

The evolution package is complete only when:

- baseline territorial escalation remains playable without any evolution
- each evolution changes a real system and public incident pool
- evolution pacing responds to campaign state
- evolved openings do not replay lower stages as immediate spam
- disabled evolutions leave a safe baseline route
- existing actors upgrade without losing history
- the jihadist branch remains fictional and limited to Evolution IV and later
- Evolution V does not automatically fire The False Revelation
- evolution records appear correctly on every relevant log surface

# Murder Mystery Specification Part 7: Assassin State Focus Tree Architecture

## Tree purpose

The Assassin State focus tree must solve the country that Event 39 creates. It begins during an active war, with a small clandestine movement suddenly responsible for territory, civilians, supply, production, command, diplomacy, and foreign cells. The tree should let the player decide whether the movement becomes a secret dictatorship, a federation of autonomous cells, or a temporary conventional state.

The tree must alter the Event 39 mechanic. It cannot sit beside Network Reach, Brotherhood Cohesion, foreign cells, Assassin units, subjects, and World of Anarchy without changing them.

## Design scale

The final focus count belongs to implementation after render and route review. The accepted architecture supports a substantial country tree, likely in the range of 65 to 90 meaningful focuses when every branch is implemented without filler. The count is not a quota. Branches should be deep enough to change play, then stop.

Most opening survival choices should use 35-day focuses. Narrow emergency handoffs can use 7 days. Institutional, military, economic, and diplomatic programs normally use 35 or 70 days. Longer commitments are reserved for large programs whose duration and aftermath are visible.

## First-glance lane plan

The full tree should be compact and symmetrical. The political route family forms the center. Survival and founding content sits above it. Industry and logistics sit to the left. Military and custom units sit to the right. Intelligence and foreign cells expand from the lower left. Diplomacy, subjects, and the Veiled Compact expand from the lower right. Evolution V and the terminal route converge at the bottom center.

```text
                         Founding and survival
                                  |
                         State contradiction
                         /        |        \
              Central command  Cell federation  Necessary mask
                    |             |             |
     Industry and logistics     Route institutions     Military doctrine
                    \             |             /
              Intelligence and foreign cells
                         \        |        /
                   Veiled Compact and subjects
                                  |
                   Evolution V command settlement
                                  |
                       World of Anarchy route
```

Cross-branch junctions should be limited to deliberate convergence focuses or mechanic thresholds. Do not draw long connector lines between distant lanes.

## Opening group: From safe houses to front lines

The opening group establishes the state and gives the player immediate actions.

### Opening focus directions

- secure the transferred capital and emergency supply network
- inventory captured factories, depots, records, and transport
- organize the first Assassin Cadres and local holding formations
- establish the starting intelligence office and foreign contact ledger
- decide how public the revealed murderer will become
- identify the first internal command dispute
- unlock the Brotherhood Operations decision category

The opening should present two to four choices within the first few focuses. The player should choose how to distribute scarce resources between front-line survival, clandestine operations, industrial conversion, and foreign cells.

### Opening requirements

Opening focuses can require control of the Assassin capital, a minimum supplied force, completion of the captured-inventory decision, or survival for a short period. Requirements must connect to their rewards and be visible.

## Central political fork

### Route A: The Hidden Hand

This route accepts one secret command structure. The revealed murderer, or a successor selected by the movement, becomes the central authority. Public institutions remain thin and the real state operates through compartmented command.

Gameplay identity:

- highest direct Brotherhood Cohesion ceiling
- strongest synchronized military planning and subject obedience
- better access to Master Assassins and central operations
- faster response to disloyal cells
- greater risk from leader capture or death
- stronger accusation that the movement has recreated the hierarchy it condemns
- difficult succession crisis if the First Knife is lost

The route should include a balance between personal authority and the operational directorate. It can use Cohesion thresholds, decisions, and events. Add a full native balance-of-power interface only when live inspection proves it is cleaner.

Key payoff direction:

- a centralized campaign command that can coordinate foreign revolts and terminal waves
- a strong elite force cap
- direct subject demands
- a terminal doctrine that preserves hidden command after ordinary governments are destroyed

Failure state:

- a captured or discredited leader can split the directorate, lower Cohesion, trigger subject defiance, or force an emergency successor route

### Route B: Cells Without Masters

This route turns the movement into a federation of autonomous cells. Local councils choose tactics, administration, and military priorities. The central country becomes a coordination point with limited formal authority.

Gameplay identity:

- stronger resistance support, cell recruitment, local revolt survival, and foreign derivative autonomy
- cheaper foreign operations and wider Network Reach
- lower conventional planning, production coordination, and subject extraction
- larger risk of contradictory operations, rogue murders, and unaffordable simultaneous uprisings
- more flexible survival after the central state loses its capital

The route should let the player issue broad campaign goals while local cells decide execution. This can lower action costs but reduce certainty and make outcomes depend on local maturity.

Key payoff direction:

- autonomous derivative states that can survive without constant central support
- rapid reseeding after territorial loss, within global caps
- terminal campaign councils whose authority expires after each objective
- post-victory decentralized administration without one world state

Failure state:

- low Cohesion can turn autonomy into fragmentation, local peace deals, rogue violence, and subject departure

### Route C: The Necessary Mask

This route treats statehood as a temporary instrument. The movement builds ministries, contracts, formal command, trade, and diplomacy to win the current war. It may retain a public government after survival or return to terminal doctrine later.

Gameplay identity:

- strongest ordinary economy, logistics, research, diplomacy, and conventional force development
- access to trade, limited recognition, foreign volunteers, and pragmatic agreements
- slower Network Reach and weaker radical recruitment
- lower immediate access to the most ideological terminal tools
- internal pressure from hard-line cells that regard administration as betrayal

Key payoff direction:

- a functioning state that can defeat the original host through conventional and covert power
- staged integration and lower resistance after conquest
- Mechanized Assassin and combined-arms capability
- a late choice between permanent statehood, limited international order, or a return to World of Anarchy preparation

Failure state:

- excessive dependence on ordinary ministries and foreign contracts can collapse Cohesion, empower hard-liners, or lock the country out of terminal preparation until a costly internal settlement occurs

## State contradiction branch

A central branch visible after the opening should manage `Leadership Is a Crime`. It asks how an anti-leadership movement writes orders, appoints commanders, disciplines units, and governs civilians.

The branch should transform the starting spirit through route-specific stages. It should not create several overlapping permanent ideas.

Common mechanics:

- temporary campaign mandates
- revocable command tokens
- cell votes or directorate appointments
- punishment for unauthorized murders
- succession arrangements for the First Knife
- civilian administration and food distribution
- public treatment of captured officials
- limits on cult mythology and personal worship

This branch links politics to Cohesion, unit command, subject behavior, and terminal victory.

## Industry and logistics branch

The country begins with a converted clandestine economy. The branch should solve real map and production problems.

### Route families

#### Clandestine workshops

Use dispersed hidden production, captured tools, local cells, and small arms. The route improves resistance to bombing and occupation, local repair, Assassin equipment output, and supply from cells. It has lower total throughput and weaker heavy industry.

#### Seized state industry

Take direct control of transferred factories, depots, railways, and resource sites. The route gives faster conventional output and repair while increasing administrative strain and vulnerability to sabotage or bombing.

#### Pragmatic contracts

Available mainly through The Necessary Mask. Use foreign trade, neutral intermediaries, captured firms, and formal production boards. It improves research, imports, vehicles, and mechanized production while increasing dependency and hard-line opposition.

### Geographic work

Focus rewards should repair or build factories, railways, infrastructure, supply hubs, ports, anti-air, airbases, and resource extraction in named transferred or conquered states. Dynamic state selection must identify actual states and explain them in tooltips.

### Economic payoff

The capstone should replace `Underground Becomes Government` with a route-specific mature economy. It should unlock a continuing decision family, not end with one passive modifier.

## Military branch

The military branch develops the custom unit family and the conventional support needed to keep it alive.

### Assassin doctrine trunk

- formalize Assassin Cadre training and caps
- integrate reconnaissance, night movement, infiltration, and rapid exploitation
- establish reinforcement, medical, transport, and equipment standards
- unlock Saboteur Cell support
- improve operational planning without erasing low hit points and heavy-combat weakness

### Shadow Companies

An elite offensive branch focused on planned breakthroughs, raids, rough terrain, and rapid operational movement. It raises quality and formation cap slowly. It should remain expensive in training, support equipment, intelligence preparation, and command capacity.

### Silent Guard

A defensive branch for capitals, urban areas, supply nodes, archives, and movement leadership. It improves defense and entrenchment in specific contexts while giving up speed and offensive reach.

### Conventional adaptation

Adds ordinary infantry, artillery, anti-air, engineers, trucks, armored support, and later mechanization. This branch is essential because pure Assassin formations should fail in long open warfare.

### Mechanized Assassins

A late branch, strongest under The Necessary Mask but accessible through expensive alternatives elsewhere. It unlocks a distinct vehicle-backed formation with fuel, production, supply, and maintenance costs. It should not be a free upgrade to every Assassin unit.

### Master Assassins

Evolution V elite capstone. It creates a small special-forces family for key operations and command disruption. It uses a hard cap, high training cost, and low hit points. It cannot hold an entire front.

## Intelligence and foreign cells branch

This branch links the country to the Event 39 cell registry.

### Core focus directions

- formalize the foreign route ledger
- contact surviving cult cells
- improve secure communications
- train foreign organizers and saboteurs
- identify weak governments and valid revolt territory
- establish intelligence exchange countermeasures
- support one selected foreign cell at a time
- coordinate arrests, escapes, or disinformation against government investigations
- convert stage 3 cells into stage 4 insurrection cells
- protect central networks when one cell is captured

The branch should not give a global cell button with no target or route. Every operation uses an eligible target, costs, exposure, cooldown, and cleanup.

The centralized route favors precise high-value operations. The decentralized route favors wider local autonomy. The pragmatic route favors state intelligence, false fronts, and material support.

## Diplomacy, faction, and subjects branch

Before Evolution IV, this branch manages covert aid, opportunistic sponsors, prisoner exchanges, neutral intermediaries, and recognition pressure. After Evolution IV, it creates and manages the Veiled Compact.

### Veiled Compact goals

- keep the central movement alive
- protect or reinforce foreign derivatives
- coordinate selected revolts
- share Assassin training and equipment
- maintain sufficient Brotherhood Cohesion
- prevent local subjects from making uncontrolled peace
- prepare common objectives against ordinary governments

### Subject choices

The central country can demand obedience, grant autonomy, assign campaign sectors, exchange cadres, support local administration, or punish unauthorized violence. Each choice changes Cohesion, subject autonomy, local survival, and route identity.

The faction capstone should create an ongoing campaign council and decision set. It should not be a one-time faction creation reward.

## Original host conquest branch

The tree needs a war-specific branch that reacts to front state and map control.

Content directions:

- seize or bypass the host capital
- capture archives and command records
- turn military defections into local formations
- negotiate surrender with isolated regions
- decide treatment of captured leaders and officers
- establish provisional administration
- integrate starting claims in stages
- prevent the original government from returning through exile or faction aid

The route should support partial success and failed offensives. It must not grant automatic annexation through focuses.

## Evolution V convergence

Evolution V reveals a lower central branch. It should remain hidden before World Collapse and movement readiness.

The branch begins with an internal command settlement. Each political route must answer how terminal operations receive authority. The settlement affects final war mechanics, Cohesion, subjects, unit caps, and post-victory administration.

The route then unlocks:

- final recruitment and training systems
- synchronized uprising preparation
- leadership target dossiers
- government dismantling policy
- treatment of ordinary populations and protected Chaos countries
- terminal war logistics
- World of Anarchy activation focus or decision

World of Anarchy must require a deliberate final commitment after preparation. The focus or decision should explain the public objective and costs without exposing protected character lists or hidden conquest callbacks.

## Nonterminal late-game route

The Necessary Mask can choose to preserve statehood and reject the terminal route. Centralized or decentralized routes may also stop after defeating the original host. A nonterminal country retains Event 39 country content, cells, and faction play while World of Anarchy remains inactive.

This route provides a real strategic choice. World Collapse makes the terminal route available, not mandatory.

## Focus and decision integration

Every major branch must unlock or transform decisions:

- opening focuses unlock capital defense, inventory, and recruitment
- political routes change Cohesion actions and succession
- industry routes change construction and production decisions
- military routes unlock training, conversion, cap expansion, and doctrine missions
- intelligence routes unlock cell targeting, route support, and counterintelligence actions
- diplomacy routes unlock subject, faction, and recognition actions
- conquest routes unlock postwar handling
- Evolution V unlocks terminal preparation and worldwide objectives

Obsolete decisions disappear when a route changes. Costs, AI, and public descriptions change with the route.

## National spirit lifecycle

| Starting spirit | Centralized outcome | Decentralized outcome | Pragmatic outcome |
| --- | --- | --- | --- |
| Underground Becomes Government | compartmented command economy | federated local workshops | provisional state economy |
| Cells Under Arms | directorate-controlled elite corps | autonomous regional cadres | integrated special operations command |
| Leadership Is a Crime | secret central mandate | revocable cell councils | temporary constitutional mask |

Each row should use replacements or staged upgrades. Do not stack all stages.

## Advisor and character direction

The tree may unlock fictional high-chaos characters for operational roles, institutional councils, or commanders. Character work must pass through the portrait creator. The movement should not receive a large generic advisor roster.

Advisor directions include clandestine quartermaster, communications organizer, cell jurist, captured-industry engineer, foreign liaison, special operations trainer, and campaign council representative. Each belongs to a route or branch and changes a mechanic.

## Focus Navigation and filters

The final tree needs accurate search filters and navigation shortcuts for:

- founding and politics
- industry and logistics
- military and custom units
- intelligence and foreign cells
- diplomacy and Veiled Compact
- Evolution V and terminal route when revealed

Hidden terminal navigation stays unavailable before reveal. Icons, lane placement, filters, and navigation labels must agree.

## AI route plans

The AI should choose:

- Hidden Hand when Cohesion is high, the leader survives, territory is compact, and synchronized war offers a clear advantage
- Cells Without Masters when the country is dispersed, foreign cells are numerous, central industry is weak, or the capital is threatened
- Necessary Mask when the country has meaningful industry, trade access, diplomatic opportunity, a long conventional war, or low radical support

AI must re-evaluate tactical focus priorities after route lock without changing its political route illegally. It should prioritize survival, supply, and force readiness before foreign revolt expansion.

## Layout acceptance

The tree is incomplete until mandatory MCP focus inspection, rendering, rewrite, and comparison show that every major branch is visible at normal zoom, connectors do not cross unrelated branches, route locks and hidden content work, search filters are correct, Focus Navigation reaches each major lane, icons are varied and accurate, and each branch ends in a playable payoff.

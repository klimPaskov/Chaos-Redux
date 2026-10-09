# Advanced event system design

Read the relevant complete section before specifying a major focus tree, country package, starting or reinforcing forces, or an event that can materially change global Chaos.

## Focus tree path design standard

Focus trees must be planned clearly, but the event-planning spec should not try to micromanage every final focus node, every coordinate, or every exact connection. The spec writer should define the tree's routes, branch architecture, major choices, mutual exclusions, story logic, mechanics, rewards, and design standards. The implementation agent should then create the final in-game focus tree layout and exact focus connections cleanly.

A good focus-tree spec should answer:

- what major paths the country has
- what each path means in the story
- what each path changes mechanically
- which paths are mutually exclusive
- which paths can cooperate or converge
- which paths are hidden, rare, chaos-locked, evolution-locked, foreign-aid-locked, crisis-locked, or similarly gated
- what kinds of focuses belong in each path
- what kinds of rewards each path uses
- what decisions, missions, units, ideas, leaders, flags, claims, buildings, factions, or events each path should unlock
- what starting weaknesses the tree lets the country solve
- what late-game ambitions each route can reach
- how AI should choose between the routes

Do not write only vague branch names. A focus-tree plan must still be detailed enough to prevent generic or boring implementation. The spec should describe the internal logic of each path, the rough order of ideas inside it, its major focus groups, its expected route locks, and its major payoff. It should also name important focuses or focus groups where the story requires them.

Do not require a literal list of every focus unless the user specifically asks for a focus-by-focus blueprint. The default planning style should be path-level and branch-level design. It is acceptable to provide non-final focus-role labels or important anchor focus groups.

### Focus tree architecture map

Every major focus tree still needs an architecture map. The architecture map should show the intended path structure, not every final focus.

The map should include:

- opening situation and early survival choices
- main political routes
- industry and economy branches
- military branches
- diplomacy and faction branches
- expansion or reunification branches
- internal faction or balance-of-power branches
- hidden, rare, crisis, evolution, and high-chaos branches where relevant
- late-game ambition routes
- mutually exclusive route families
- paths that can converge later
- paths that require foreign aid, high threat, chaos, war, a specific evolution, or prior choices

Use a readable structure such as a table, bullet tree, route diagram, or lane map. The implementation agent should understand the intended tree shape and design, but does not need exact focus coordinates from the spec unless the user asks for them.

### Branch and path detail

For each major path, define:

- path name or working route label
- narrative role
- mechanical role
- unlock conditions
- mutually exclusive paths
- compatible paths
- rough focus groups inside the path
- key anchor focuses when needed
- major decisions, missions, ideas, units, leaders, advisors, advisor discounts, flags, country names, party changes, claims, cores, war goals, buildings, leagues, or events unlocked
- reward style and what should be avoided
- AI behavior
- late-game outcome or failure state

For each important anchor focus or focus group, define:

- rough purpose
- what it connects to
- whether it is a route opener, route lock, side branch, convergence point, hidden branch, crisis branch, or finisher
- what it unlocks or changes
- what kind of reward it should use
- what idea, decision, mission, unit, building, leader, flag, or event it affects
- what should be mutually exclusive with it, if anything

The coding agent may create more or fewer individual focuses than the spec examples as long as the final tree preserves the path design, story logic, route choices, and gameplay depth.

### Focus reward diversity standard

Focus rewards must be varied. Do not design focus trees where most focuses add a new national spirit, add political power, add stability, add war support, or repeat the same modifier pattern.

A new national spirit or idea should be used only when the focus creates a persistent institution, doctrine, crisis condition, political identity, military structure, economic system, or long-term route effect. If the branch already has an idea representing that institution, prefer modifying, upgrading, replacing, temporarily strengthening, or adding a timed modifier to the existing idea instead of creating another separate idea.

Good focus reward types include:

- civilian factories
- military factories
- dockyards
- forts
- coastal forts
- anti-air buildings
- radar stations
- airbases
- infrastructure
- railways
- supply hubs
- resources
- building slots
- production lines
- equipment stockpiles
- unit templates
- route-specific spawned units
- commanders or advisors
- decisions
- timed missions or objective families
- laws
- technologies or research bonuses
- claims or cores
- leader changes
- ruling party changes
- cosmetic names
- flag changes
- faction mechanics
- diplomacy routes
- foreign aid systems
- crisis value changes
- objective completion bonuses
- events or event chains

When a specification adds or changes technologies, doctrines, folders, prerequisites, unlocks, grants, or research bonuses, the coding-agent prompt must require the implementation agent to inspect the affected graph with `hoi4.tech_inspect`, render the relevant folder or branch with `hoi4.tech_render`, and compare the implemented source with `hoi4.tech_compare`. The plan must identify intended placement, prerequisites, exclusivity, unlocks, bonuses, and asset needs so the implementation agent has a concrete result to verify. Apply the AGENTS.md retry limits and use direct source checks when a route remains unavailable; missing tool output does not remove any placement, prerequisite, unlock, bonus, or asset requirement.

Every focus path should have a distinct purpose. If two focus groups would grant nearly the same effect, merge them, rewrite one, or make one an upgrade of the other.

Reject focus trees where most focus groups grant new ideas without a clear reason. A tree that uses repeated new ideas as filler has failed even if it has many focuses.

### Dynamic idea lifecycle standard

New countries, transformed countries, civil-war splinters, emergency governments, and unstable successor states should not start with a long stack of generic positive ideas. It is usually better for them to start with a small number of deep, readable ideas that define their starting weakness, identity, and strategic problems.

Starting ideas can be negative, mixed, unstable, or conditional. These ideas should represent real problems the country must solve, such as broken administration, improvised command, disputed legitimacy, militia fragmentation, supply confusion, foreign dependence, refugee pressure, factional mistrust, ruined industry, contested railways, disorganized officers, or unclear laws.

Negative starting ideas should not be permanent dead weight unless the story requires that. The spec should map how decisions, missions, focuses, leader choices, foreign aid, victories, reforms, purges, compromises, or crisis outcomes can mitigate, transform, upgrade, or remove them.

Prefer fewer ideas with more depth over many shallow ideas. A good idea can have a lifecycle:

- starting negative or mixed form
- mitigated form after early stabilization
- reformed form after a political or institutional branch
- positive route-specific form after the country commits to a path
- corrupted, radicalized, or dangerous form after a high-chaos or failure route

When designing focus trees, do not create a new idea in every focus. If an institution already exists as an idea, prefer changing that existing idea through staged upgrades, replacing it with a route-specific version, adding a temporary modifier, unlocking decisions tied to it, or changing how it interacts with missions and crisis values.

For every important idea, define:

- why the country starts with it or unlocks it
- whether it is negative, mixed, positive, temporary, staged, or route-specific
- what decisions, focuses, missions, events, or outcomes change it
- what its upgraded or mitigated forms are called
- what route can remove it completely
- whether it can become worse through failure, high chaos, foreign dependence, civil war, or bad decisions
- what icon direction it needs
- how AI should prioritize solving or exploiting it

Every major country package should include a starting idea plan and an idea lifecycle table. The table should show which ideas exist at start, which are unlocked later, which are upgraded, which are removed, and which are route-specific.

Example table:

| Idea | Start or unlock | Starting role | Mitigation path | Upgrade path | Failure path | Final forms |
| --- | --- | --- | --- | --- | --- | --- |

Reject specs where a country starts with too many unrelated ideas, where every focus creates a separate idea, or where negative ideas cannot be meaningfully addressed through play.

### Focus, politics, expansion, and decision integration

When planning a major focus tree, define more than politics and industry. A large tree needs a distinct expansion, reunification, liberation, settlement, or regional ambition branch. This branch should be separate from the main political tree and separate from the industry tree.

Expansion branches should define real strategic effects, such as claims, cores, war goals, protectorates, guarantees, declarations, leagues, border settlements, ultimatum decisions, or postwar integration choices. Do not reduce expansion to generic bonuses.

Political branches should change politics directly. Define ideology paths, ruling party shifts, party popularity changes, leader changes, advisor unlocks, advisor discounts, laws, councils, juntas, congresses, committees, faction struggles, cosmetic names, and flag changes where they fit. Leader changes imply portrait needs. Route both sourced real portraits and generated fictional or symbolic portraits to `chaosx_portrait_creator`.

Focus trees and decision systems must be planned together. Focuses should unlock or change decisions and missions. Industry focuses can unlock construction decisions. Military focuses can unlock unit, depot, border, or offensive missions. Diplomacy focuses can unlock recognition, aid, volunteer, and influence decisions. Expansion focuses can unlock declarations, league votes, protectorate demands, border incidents, claims, cores, war goals, and settlement decisions.

For each major focus path, describe which decision or mission families it unlocks and how those decisions expand the mechanic.

### Branch interaction, payoff, and country identity

Political, industry, and expansion are the minimum branch families, not the full design for important countries. Important countries should usually also define military, diplomacy, internal faction, intelligence or security, special mechanic, and late-game branches when their identity supports them.

Branches should not be isolated columns. Political choices should change which expansion, industry, military, diplomacy, and decision paths are available. Industry should support military or expansion. Expansion should create political consequences. Diplomacy should affect foreign aid, war options, faction choices, and sponsor risk.

Every major branch needs a clear payoff. A political branch can end in a new government, leader, ideology, law system, ruling party, or country identity. An industry branch can end in a rebuilt economy, arsenal, resource system, railway authority, construction mechanic, or production network. An expansion branch can end in a league, empire, federation, protectorate network, reunification, liberation order, regional settlement, or external war plan.

A good focus path should unlock new gameplay, not only stats. The plan should describe decisions, missions, units, advisors, leaders, laws, claims, cores, war goals, buildings, events, mechanics, route access, and AI behavior where they fit. Flat modifiers are supporting rewards, not the main design.

Political routes should update the visible country package where relevant: leader, leader portrait, advisor roster, high command, ruling party, party names, ideology drift or swap, cosmetic name, flag, ideas, and AI strategy.

Expansion branches should create consequences. Claims, cores, and war goals should interact with diplomacy, factions, resistance, foreign guarantees, local leagues, legitimacy, threat, or postwar settlement decisions.

Industry branches should create map or production changes. Define factories, infrastructure, railways, supply hubs, forts, anti-air, airbases, dockyards, resources, production lines, or construction decisions.

Specify the focus skill’s complete [branch interaction and payoff](../../chaos-redux-focus-trees/references/major-country-design.md#branch-interaction-and-payoff) requirements for evolving decision categories.

The fixed-purpose exception is narrow. A country is fixed-purpose only when its concept clearly cannot support normal politics, such as a death-state, machine-state, plague-state, or pure destruction actor, and such a country may then have one ideological purpose and narrower politics. Even then, the tree still needs meaningful internal choices and branches inside that purpose, such as doctrine, method, expansion, recruitment, economy, hierarchy, and endgame ambition.

### Branch depth, AI, localisation, and aftermath

A branch does not count as real unless it changes gameplay. In the spec, each major branch should have several focus groups, a mechanical unlock, a route consequence, and an end-state or payoff.

Major routes need route-specific AI plans. Do not let the implementation use generic focus weights for every route. The spec should say which AI types choose each route and when they avoid it.

Major routes need distinct localisation tone. A socialist route, military route, democratic route, nationalist route, religious route, machine route, death-state route, or foreign client route should not read like the same generic branch with different rewards.

Expansion branches should include postwar handling. War goals alone are not enough. Define claims, cores, puppet options, protectorates, occupation decisions, integration missions, border settlement events, resistance risks, diplomacy reactions, faction consequences, or achievement tracking.

Industry branches should be geographically grounded where possible. Define which states or regions receive factories, resources, ports, railways, supply hubs, forts, anti-air, dockyards, airbases, or infrastructure.

Advisor unlocks should match route identity. Political routes unlock ideological and government figures. Industry routes unlock engineers and economic boards. Military routes unlock commanders and high command. Diplomacy routes unlock envoys and foreign liaisons. High-chaos routes unlock route-specific councils, symbolic leaders, or strange authorities.

Large focus trees should include achievement hooks for difficult route completions, rare branch combinations, expansion outcomes, internal reform, avoiding foreign dependency, league formation, high-chaos survival, or late-game ambitions.

The final implementation prompt should ask for a route coverage table comparing required routes against implemented routes. Missing, renamed, merged, simplified, fallback, or replaced routes must be reported.

### Route visibility, pacing, tradeoffs, and failure states

A major route should leave visible evidence in the game. The spec should describe what the player actually sees or gains: map changes, decisions, units, advisors, leaders, flags, cosmetic names, faction behavior, focus availability, diplomacy, or visible mechanics. A route that only changes hidden variables or tiny modifiers is not meaningful.

Large focus trees should have early, middle, and late pacing. Early content solves survival and basic identity. Middle content creates route mechanics and real choices. Late content delivers major payoffs, expansion, faction or League outcomes, high-chaos routes, postwar settlement, or world-order ambitions.

Every major route should have a tradeoff. The spec should define what the route risks or sacrifices. Military routes may reduce freedom or legitimacy. Foreign-aid routes may create dependency. Expansion routes may create backlash. Industry routes may consume civilian capacity or weaken short-term defense. High-chaos routes may gain power while damaging stability, diplomacy, or normal politics.

Do not overuse mutual exclusions. Mutually exclusive paths should represent real identity changes, strategic commitments, or incompatible institutions. Support branches such as industry, army, diplomacy, and logistics should usually coexist unless the route logic says otherwise.

Specify route-specific failure states under [route visibility, pacing, tradeoffs, and failure states](../../chaos-redux-focus-trees/references/major-country-design.md#route-visibility-pacing-tradeoffs-and-failure-states).

Focus and decision localisation should describe the visible baseline effect of the route or action. It should not reveal hidden effects, secret outcomes, hidden variables, or future surprises. The player-facing text should explain the public action and visible direction, not the hidden implementation.

### Special mechanics, dynamic values, and faction systems

Large events should usually include at least one special mechanic. A special mechanic can be a pressure meter, influence system, balance of power, faction cohesion system, legitimacy system, corruption system, outbreak tracker, coalition command system, resource race, regional authority map, or similar play layer.

A special mechanic should define its important values clearly. Examples include legitimacy, authority, influence, cohesion, obedience, corruption, foreign penetration, military readiness, industrial capacity, public panic, faction unity, sponsor pressure, religious authority, revolutionary zeal, or regional control.

#### Public-facing mechanic value budget

A main mechanic should ask the player to actively track as few persistent custom values as possible. Complexity belongs in the simulation, not in the player's memory.

Use this budget:

- One or two public-facing values are preferred for most mechanics.
- Three public-facing values are acceptable when each one changes a distinct player decision.
- Four public-facing values are the absolute hard maximum for one mechanic. Use four only when all four have distinct causes, consequences, thresholds, and player responses.
- More than four public-facing values that the player must actively monitor or remember are forbidden.

The cap applies to the mechanic as a whole, not to one screen. Count every persistent event-specific meter, score, pressure, influence value, readiness value, legitimacy value, corruption value, cohesion value, or similar state that the player is expected to monitor or remember. A value still counts if it is placed in a different decision category, scripted GUI tab, focus inlay, national spirit tooltip, Event Details panel, popup, or secondary window. Do not split a five-value system across several surfaces to evade the budget.

Hidden internal simulation values are not subject to the four-value cap. Use additional internal variables, weights, memories, regional scores, timers, subcomponents, and derived calculations when they make the system more reactive, immersive, or believable. They should normally feed a public value, qualitative state, threshold, event condition, AI behavior, or other consequence instead of becoming extra player counters.

If a public total is built from many hidden inputs, show the total and only the supporting values that the player can meaningfully manage as separate long-term states. A hidden contributor can be explained through a short causal tooltip, icon, trend, or status label without exposing its raw number. Once a contributor becomes a persistent number that the player is expected to monitor, it counts toward the four-value ceiling.

A fourth public-facing value needs a clear reason to exist. If it overlaps another value, can be inferred from another value, or does not change a distinct player response, merge it, summarize it, or keep it hidden. A custom scripted GUI is not justification for exposing more values.

Mechanic values must be dynamic. They should move through focuses, decisions, missions, events, wars, state control, foreign influence, AI actions, and prior outcomes. Do not design a mechanic where values only drift passively or change through a few flat scripted effects.

Every public-facing mechanic value should have a consistent colour identity in localisation. Hidden internal values do not need public colour identities. If several hidden values contribute to a public total, do not expose a full numeric component ledger by default. Show only the material, actionable contributors that still fit within the public-facing value budget, and summarize the rest qualitatively.

If a mechanic has values such as legitimacy, authority, influence, cohesion, obedience, power, or readiness, then focuses, decisions, and missions should interact with those values directly. A focus tree should not sit beside the mechanic without changing it. A decision system should not sit beside the mechanic without changing it.

Mechanic values should unlock or block content: decisions, focuses, events, missions, leaders, advisors, factions, war goals, reforms, crises, achievements, super-events, or endings. A mechanic should change what the player can do.

When a country has two or more internal power centers, consider a balance-of-power or equivalent system. Focuses and decisions should push the balance, unlock branch content, create risks, and change leaders, laws, advisors, events, or crises.

When an event creates a faction, league, bloc, coalition, compact, or alliance, define its goals and internal rules. The faction should have a reason to exist, membership rules, joining conditions, refusal logic, expulsion or removal logic where relevant, war goals, shared decisions, AI behavior, victory conditions, and failure conditions.

Important event-created factions should usually have a mechanic such as cohesion, shared command, war council support, joint reserves, recognition, member confidence, sponsor pressure, or strategic goals. Focuses and decisions should interact with that faction mechanic.

A faction should not form just because one country exists. Define minimum membership, crisis conditions, ideological compatibility, war pressure, diplomatic preparation, and regional logic.

A special mechanic should define success, failure, partial success, and runaway failure states. These states should unlock events, decisions, focus branches, faction changes, wars, reforms, aftermath, achievements, or super-events.

AI must understand mechanic values. It should know when to lower threat, build legitimacy, increase influence, join a faction, avoid dependence, push balance of power, or trigger escalation.

For every special mechanic, the completion report should list mechanic values, what changes them, what they unlock, UI and localisation coverage, AI behavior, focus hooks, decision hooks, event hooks, and balance checks.

### Mechanic presentation, faction outcomes, validity, and tuning

Every special mechanic should define where the player sees its public state: decision category header, custom scripted GUI, progress meter, scripted localisation tooltip, focus tooltip, national spirit tooltip, or another clear presentation surface. The player-facing state must fit within the public-facing mechanic value budget. Hidden internal values may remain entirely internal when the player does not need to track them directly. Do not create extra UI surfaces only to expose more counters.

When a special mechanic uses a scripted GUI, consider visual presentation beyond static text. Useful designs can include progress bars, meter fill variants, state icons, status frames, warning frames, selected or locked variants, animated frames, or frame-by-frame visual changes that make the mechanic feel alive. The visual layer should make the mechanic easier to understand.

Special mechanics can hide future surprises, but they should not hide basic cause and effect. The player should understand why a visible value rose or fell, which public action changed it, and what kind of response is available.

Faction, league, bloc, or coalition goals should have rewards and failure states. A successful faction goal can unlock shared decisions, war goals, legitimacy, cohesion, member rewards, or postwar settlements. A failed goal can reduce cohesion, trigger exits, invite foreign pressure, start leadership contests, or weaken shared defenses.

New playable country packages must not be generic. Each needs a specific identity, starting problem, political direction, map role, military style, economy, diplomacy, AI behavior, and at least one mechanic or decision family that makes it play differently.

AI strategy must respect route validity. AI should not pick a branch or action that requires a missing state, dead sponsor, non-existent faction, unavailable ideology, disabled evolution, impossible border, invalid target, or absent enemy. Invalid routes should be hidden, bypassed, or weighted to zero.

When a route changes leader, ideology, faction, cosmetic name, flag, advisor roster, or special mechanic identity, define the needed visible assets and whether they are sourced, generated, reused, or blocked.

Shared trees are allowed, but they must have country-specific localisation, route names, decisions, AI weights, leaders, rewards, icons, and scripted localisation where relevant. A shared tree fails if every country using it reads and plays the same.

Important mechanic thresholds, caps, gains, losses, duration bands, AI weights, and scaling values should be centralized in script constants or a clearly documented tuning file. Do not scatter magic numbers across decisions, events, focuses, scripted effects, and scripted triggers.

### Reward dumps and exploit checks

Avoid one-time reward dumps as the main design. A focus, decision, or mission can give factories, units, equipment, resources, buildings, or influence, but important content should often unlock a repeatable decision, timed mission family, production route, advisor, mechanic, route branch, or long-term gameplay system.

One-time rewards are acceptable when they fit the story and balance. They should not become the default design pattern for a major event, large focus tree, or decision system.

Balance planning should include exploit checks. Look for free unit loops, repeated factory rewards, cheap construction loops, equipment farming, influence farming, puppet abuse, war-goal spam, claim or core spam, advisor discount stacking, bypass abuse, mission success farming, and decisions that can be clicked without meaningful cost or risk.

The spec should tell the implementation agent how to prevent abuse with flags, cooldowns, dynamic costs, escalating costs, one-time completion flags, route locks, target limits, AI limits, cleanup effects, or scripted triggers.

### Decision category clutter control

Large decision systems should not show every possible decision at once. The spec should define how decision categories stay readable.

Use phases, caps, priorities, regional pools, route locks, mechanic thresholds, or crisis-state filters so the player sees decisions that matter in the current situation.

Good planning patterns include:

Specify the full [progressive decision-category contract](../../chaos-redux-decisions-missions/SKILL.md#151-progressive-decision-categories), including tiers, mission caps, target pools, visibility, replacement, and cleanup.

A decision category should feel curated by the current route and campaign state, not like a debug menu.

### Decision category presentation choice

Every planned decision category should use the least complex presentation that communicates its purpose and current state clearly.

Apply the [decision-category picture eligibility rules](../../chaos-redux-decisions-missions/references/formables-and-category-presentation.md#decision-category-picture-reference-workflow), including the exceptions for ordinary decision buttons and basic value tables.

Use this order:

1. ordinary category icon and concise text
2. static category picture when eligible
3. animated category picture with a static fallback when eligible
4. compact attached display or category header
5. full scripted GUI or separate mechanic window

Do not plan a full scripted GUI only because a category is important. Within the eligibility gate, a static or animated category picture is usually the better choice when the category needs identity, atmosphere, propaganda, territorial context, or a clear visual theme but the decisions already carry the gameplay.

Within this gate, strong category-picture candidates include:

- propaganda, ideology, elections, monarchism, party control, and trade-union politics
- civil-war preparation, insurgency, mobilization, and national preparedness
- faction management, treaties, naval agreements, and foreign intervention
- formables that need a territorial overview
- one-theme national campaigns and crisis categories

A category picture is presentation, not a fake interface. Do not paint buttons, meters, dynamic values, or controls into it.

Use a full scripted GUI only when the player must manage several interacting values, repeated target selection, competing factions, persistent state changes, or exact dynamic state pieces that cannot be presented clearly through normal decisions, category text, tooltips, and one picture.

The asset handoff should point to this canonical picture reference family:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

If its `contact_sheet.png` is missing, the implementation prompt should require the asset agent to create it, label each reference with its filename and native dimensions, and update the reference README and catalog. The references and contact sheet are review-only assets.

### What the implementation agent owns

The implementation agent is responsible for the final exact focus tree shape unless the user asks otherwise.

The implementation agent should:

- choose the exact number of focuses needed for each path
- write final focus names and descriptions from the path design
- place focuses cleanly in the in-game grid
- create visually readable branches
- avoid ugly, tangled, or overly linear layouts
- create exact prerequisites and `mutually_exclusive` blocks
- wire bypasses and availability
- assign icons and search filters
- balance focus durations and rewards
- implement AI path weights
- report any design gap that prevents clean implementation

The spec should give enough creative and structural direction that the agent cannot make a shallow generic tree, while still allowing the agent to build a clean in-game layout.

## Country package and dynamic identity standard

When an event creates, releases, transforms, or significantly modifies a country, the spec must define that country as a full package. This applies to new custom tags and to existing countries that gain event-specific political identities, focus trees, flags, leaders, cosmetic names, ideology names, starting forces, or mechanics.

Before assigning a new tag, inventory vanilla country tags and identities, Chaos Redux tags, every installed Workshop mod's country tags, and other local mods. A new tag must be unused across that complete installed set. If the country or national identity already exists in vanilla, reuse the vanilla tag and plan safe additive content. Do not create a duplicate country under a new tag. Preserve a living vanilla country and any meaningful vanilla or existing tree. When an event requires a naming family such as a suffix convention, apply that convention only after the collision audit. Record the audited source roots, conflicts, reused vanilla tags, and unresolved identity matches in the specification or coding-agent prompt.

For every new country, and every existing country that is meaningfully changed, the spec should provide a country package matrix or equivalent structured section. It must cover:

- tag or placeholder tag, with a note that final tags must avoid conflicts
- spawn, release, transformation, or takeover conditions
- core territory, claimed territory, disputed territory, and fallback territory
- history file needs for new custom tags, generated startup scientists for existing countries when characters are needed, and additive startup setup for existing countries
- public country name and cosmetic names, following the country naming rules below
- ideology-specific names
- focus-tree route names
- faction names and possible faction cosmetic names
- ruling party names, sub-ideology labels, and political movement names
- starting politics and possible ideology shifts
- starting military package, including initial divisions, template families, manpower, equipment, command structure, supply assumptions, and dynamic scaling factors
- unit growth routes through decisions, focuses, objectives, volunteers, mobilisation, depots, foreign support, faction reserves, or special mechanics
- starting leader, leader traits, portraits, and possible leader replacements
- council, junta, committee, regency, cult, military, monarchist, democratic, communist, fascist, anarchist, or factional leadership variants when relevant
- flags for the base country, ideology variants, focus-tree variants, cosmetic variants, puppet variants, and major route transformations
- national spirits, ideas, decisions, events, focus tree, achievements, mechanics, and unit systems tied to that country
- AI behavior and route preferences
- asset needs for every visible identity state
- localisation tone and naming rules
- documentation needs
- compatibility notes if the country already exists in vanilla, Chaos Redux, or common mods
- a relevance-gated detail pass for capitals and settlement names, optional intelligence and MIO identity, useful character flavour, navy and air forces when relevant, starting research, economy, stockpiles, laws, subject status, equipment identity, and DLC compatibility

Do not treat a custom country as complete because it has a tag and one flag. A serious country needs identity, politics, names, flags, leaders, starting forces, force-growth routes, mechanics, decisions, AI, localisation, assets, and route changes. If the country is only temporary and does not need a full package, the spec must explain why.

Political identity should be dynamic when the content supports it. Focus routes, ideology changes, coups, faction victories, foreign puppeting, religious transformations, high-chaos mutations, monarchist restorations, military takeovers, revolutionary councils, or world-order paths should be able to change the country name, flag, ruling party, leader, leader portrait, leader trait, cosmetic tag, national spirits, available decisions, and available recruitment systems when appropriate.

### Relevance-gated country detail pass

Small country details must be assessed deliberately, but they must not become a quota. Include a detail only when it supports the country's identity, starting position, military role, route logic, or player experience. Omit optional surfaces that would exist only to make the package look larger. Do not add an absence section for every omitted surface.

Persistent playable countries, countries with fixed historical or fictional identities, and countries expected to survive for a meaningful part of the campaign need the deepest assessment. Short-lived emergency actors and highly dynamic random countries may use shared packages when custom content would add no value. Dynamic generation does not excuse missing setup when the country still needs a valid capital, economy, army, laws, research base, or equipment package.

#### Capitals, settlements, culture, and names

Plan capital and settlement details when territory or cultural identity makes them meaningful.

For a country with fixed or bounded territory, define:

- primary capital and the states or cities that can serve as backup capitals
- relocation behavior after the capital is lost, transferred, isolated, or made invalid
- whether the capital changes through a political route, formable, conquest, restoration, evacuation, or cultural transformation
- victory-point, city, port, and regional renames caused by language, culture, religion, ideology, restoration, colonisation, decolonisation, or another real identity change
- route-specific renames and the conditions that apply or reverse them
- localisation and research direction for every culturally or historically grounded name

For a dynamic country without fixed starting territory, define how the event selects a valid controlled city or victory point after the territory is chosen. The selected city may become the capital and may receive a new name when the country's culture, ideology, mythology, or route gives a clear reason. Dynamic naming should use a researched or designed naming pool that matches the country's identity. The plan should also explain how a backup capital is selected from the country's remaining valid cities when the first capital is lost.

Do not rename cities because a government changed its cabinet or party label. City and regional renames should reflect a deeper cultural, linguistic, religious, historical, colonial, revolutionary, or high-chaos identity change.

#### Optional intelligence, MIO, and character flavour

An intelligence package is optional and should remain minimal. Plan it only when espionage, internal security, clandestine politics, resistance, infiltration, cryptology, foreign sponsorship, or a secret route is part of the country's identity or gameplay. A useful package may define a country-specific agency name and emblem, one or more meaningful upgrades, a small operative identity, or a relevant operation family. Do not create a custom agency package for a country that would play the same without it.

Custom military industrial organizations are optional. Plan them for countries with a fixed identity, a distinctive industrial institution, a meaningful equipment tradition, a route built around military production, or a country-specific manufacturer that changes equipment development. A small number of specific MIOs is better than a complete generic roster. Dynamic countries should not receive custom MIOs by default. Do not create MIOs only because the DLC system exists.

Advisors, theorists, high command, commanders, scientists, operatives, and other characters can strengthen country identity. Add them when a person, institution, faction, profession, or regional tradition gives the country useful flavour or supports a real route. Do not fill every available role. One memorable and mechanically relevant character is better than a padded roster of interchangeable bonuses.

For every optional institution or character that is included, define its role, route connection, availability, removal or replacement conditions, AI use, localisation direction, and visible identity. If a surface does not add flavour or gameplay, omit it cleanly.

#### Navy and air force relevance gate

Assess whether the country should have a navy or air force from its territory, ports, islands, airbases, inherited forces, strategic role, industrial capacity, culture, doctrine, and event premise.

When a navy matters, plan it thoroughly. Define the starting fleet or dynamic generation rule, deployment ports, ship classes and variants, naming direction, admirals, doctrine, repair and fuel needs, starting stock, production path, reinforcement path, mission priorities, route changes, and AI use. A dynamic country can scale its navy from controlled ports, dockyards, coastline, captured ships, former-owner forces, chaos tier, and foreign support.

When an air force matters, plan it thoroughly. Define the starting air wings or dynamic generation rule, deployment bases, aircraft types and variants, naming direction, air commanders or chiefs when useful, doctrine, fuel and pilot assumptions, starting stock, production path, reinforcement path, mission priorities, route changes, and AI use. A dynamic country can scale its air force from controlled airbases, military factories, inherited aircraft, chaos tier, foreign support, and available fuel.

Do not add a token navy or air force to satisfy a checklist. If naval or air power is part of the country's survival, expansion, geography, or identity, omitting its full plan is a country-package failure.

#### Starting research, economy, laws, stockpiles, and equipment identity

Every persistent playable country and every country expected to fight or develop independently needs a coherent starting setup.

Plan:

- exact starting research-slot count, including the reason for unusually low or high access
- exact starting technologies, doctrine progress, disabled or unavailable technologies, and any inherited research
- dynamic technology rules for random countries, based on origin, former owner, date, territory, industry, route, chaos tier, and event intensity
- starting civilian factories, military factories, dockyards, damaged industry, construction capacity, and production lines
- initial manpower, infantry equipment, support equipment, artillery, trucks, trains, convoys, fuel, aircraft, ships, tanks, and special stockpiles that the country actually needs
- supply position, railway access, ports, resource access, imports, production licences, foreign contracts, and dependence on a sponsor or former owner when relevant
- starting conscription, economy, trade, and occupation laws
- subject type, autonomy level, guarantees, military access, docking rights, faction status, government-in-exile status, and other starting diplomatic constraints
- equipment identity, including country-specific names, variants, module presets, improvised or inherited equipment, upgrade paths, production ownership, and visual or 3D requirements when relevant
- AI research, production, stockpile, law, trade, and equipment priorities

The setup can use exact values for a fixed country or clear generation rules for a dynamic country. Do not copy one default package across countries whose territory, culture, military role, or origin should produce different capabilities.

#### DLC and feature compatibility

Every event must remain playable and complete with every DLC combination, including no DLC. The spec must identify every planned surface that depends on DLC and define how the core event works when that DLC is absent.

Treat the no-DLC route and DLC-enhanced route as supported implementations. The no-DLC route must preserve the event premise, progression, AI behavior, balance role, cleanup, and main outcomes. DLC systems may add deeper presentation, institutions, decisions, operations, organizations, designers, markets, special projects, or other supported mechanics. They must not become a hidden requirement for the event to start or finish.

For every relevant DLC-backed surface, define:

- what the DLC version adds
- what base-game system represents the same core action when the DLC is absent
- what differences in cost, timing, visibility, AI behavior, and balance need separate tuning
- how saved flags, variables, characters, units, and country setup remain valid in both paths

If a DLC feature adds flavour only, it may be omitted in the no-DLC version without a substitute. If it carries core gameplay, the base-game implementation needs an equivalent playable action. The coding-agent prompt should require validation with no DLC, with each directly relevant DLC, and with the full supported DLC set.

### Country naming rules

Country names must be direct public country names that remain readable on the map.

Do not build public country names from internal political attachments. Avoid names that use terms such as `Military Office`, `Compact`, `Bureau`, `Authority`, `Mission`, `Board`, or similar administrative labels as the country name. These terms can exist as mechanics, focus groups, advisors, decisions, councils, ministries, internal institutions, route labels, or faction mechanics when they fit. They should not be the public name printed on the map.

Ideology-specific country names are allowed when they fit the route. Sultanate, Kingdom, Empire, Republic, Union, Commune, Federation, and similar public state forms are valid when they match the ideology, historical claim, route, or formable identity.

Prefer names built from the country, people, dynasty, region, or formable identity, then add a simple public state form only when it improves clarity. Style examples include:

- `Asante`
- `Kingdom of Asante`
- `Asante Republic`
- `Sultanate of Kilwa`
- `Kongo`
- `Kongo Commune`

Do not overload country names with political office language. The political office, emergency cabinet, military committee, colonial mission, compact council, bureau, authority, or board can be a mechanic or institution inside the country package. The map name should stay short and readable.

Names may depend on ideology, route, leader, formable status, puppet status, or high-chaos transformation. Even then, the public name should remain a country name, not an agency name.

For alternate governments, design internal bodies and party names separately from public country names. A route can have named councils, committees, directorates, juntas, congresses, restoration offices, cult offices, leagues, syndicates, ministries, synods, communes, or military commands. Those institution names should fit the country story, region, history, route, and ideological language without replacing the public country name.

### Formable nations and formation routes

When an event creates, transforms, releases, or empowers countries, check whether formable nations should be part of the design. A formable is a meaningful country identity that appears after a country satisfies territorial, political, event, focus, or hidden-route requirements. Do not treat formables as only a cosmetic rename.

Formable public names must follow the country naming rules above. The formation decision, congress, authority structure, charter, settlement, or council can have its own institutional name, but the formed map name should stay a direct country or formable name.

A formable design should define:

- formable name and tag handling
- whether it uses a new tag, an existing tag, a cosmetic tag, or a dynamic country name
- required owned and controlled states
- required cores, claims, subjects, puppets, allies, faction members, or occupied areas
- alternate state sets for different borders or reduced maps
- focus route or event route that reveals the formation
- decision that performs the formation
- hidden unlock conditions, if the formable is secret
- ideology, leader, government, legitimacy, recognition, chaos tier, crisis, patron, or achievement gates
- effects on cores, claims, compliance, resistance, subjects, puppets, factions, advisors, laws, technologies, and ideas
- visible country identity after formation, including name, adjective, flag, leader, portrait, parties, ruling ideology, advisors, and focus tree access
- post-formation ambitions, claims, diplomatic reactions, rivals, league or faction behavior, and failure states
- AI willingness to pursue the formable and AI safety checks that prevent impossible or suicidal formation attempts
- super-event, achievement, and asset implications

Do not write vague lines such as `can form a greater country`. Define the concrete formation web. If the player must control this state, this state, and this state, name those states or name the scripted state group and explain what it contains. If the exact state ids are left to implementation, describe the intended geographic set clearly enough that the implementation agent can build a scripted trigger without guessing.

Hidden formables should still be designed fully. The spec can hide player-facing names and spoilers, but the coding-agent prompt must describe the unlock route, required flags, reveal event, decision visibility, AI behavior, rewards, assets, and disqualifiers.

Formation routes should interact with focus trees and decisions. A focus can reveal or prepare the claim, while a decision performs the formation after the map requirement is met. A decision can form the country directly, while later focuses stabilize it, core it, claim further territory, or resolve internal factions. Avoid giving a formable through a focus alone when the player should prove control over named land first.

#### Formable state-puzzle presentation

When exact control of named states is the main proof for a formable, plan the reusable formable state-puzzle display from `chaos-redux-decisions-missions`.

The display should assemble the required territory from the exact in-game shapes of its states in their real geographic positions. Each state remains its own dynamic piece:

- grey when the state does not currently satisfy the formation requirement
- green when the state currently satisfies the formation requirement
- an outline, texture, label, or another non-colour cue that keeps the states readable without relying on colour alone
- a tooltip that names the state and explains its current qualification
- a summary showing qualifying states, required states, and current formation eligibility

The pieces must use exact installed-map state geometry. Do not ask the asset agent to invent borders, trace a modern map, or turn states into generic puzzle tiles. Alternate state sets, subject or ally counting rules, route locks, and ownership or control rules must be defined in the spec so the visible pieces and the formation decision use the same logic.

The interface should update from current campaign state and must not show stale qualification. Keep it compact. Do not surround the territory with unrelated values, fake buttons, or long prose.

The coding prompt should require reusable templates under:

`.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`

The template package should cover the state manifest, GUI, GFX, scripted GUI, helper triggers and effects, scripted localisation, static category-picture alternative, AI equivalent, cleanup, and validation. Skill-local templates are reference scaffolding and must be copied into system-owned files before runtime use.

A small formable whose map requirement is obvious may use a static territorial category picture instead only when the category passes the picture eligibility gate and has no interactive state-puzzle GUI. The spec should state why the static picture is clearer than a dynamic state-puzzle display.

## Starting forces and reinforcement pathway standard

When an event creates, releases, transforms, restores, or revives a country that is expected to fight, survive, defend itself, or matter militarily, the spec must define its starting forces. Newly appearing countries should not spawn as empty tags unless they are explicitly non-military administrative placeholders and the spec explains why.

### Distinct army identity and new unit-type gate

When an event introduces a new type of country with its own army, explicitly assess whether that army needs new unit types instead of only renamed vanilla division templates. Plan at least one distinct unit family when the country's biology, doctrine, recruitment source, battlefield role, equipment relationship, movement, supply behavior, or visual silhouette differs materially from an ordinary national army.

A renamed division template made entirely from ordinary vanilla battalions does not count as a new unit type. If vanilla battalions are sufficient, the spec must explain why their mechanics accurately represent the country and must still define distinct templates, recruitment rules, caps, costs, AI use, progression, and visible identity. Do not let implementation silently substitute renamed infantry for a military concept that calls for custom behavior.

For every planned new unit family, define:

- gameplay role, battlefield strengths, weaknesses, and intended counterplay
- custom sub-unit, support unit, unit category, equipment, or modifier needs
- division-template consumers and the countries, routes, evolutions, or decisions that can use them
- manpower, population, equipment, supply, fuel, training, and reinforcement rules
- availability gates, formation caps, upgrade or conversion paths, and cleanup behavior
- AI template priorities, role ratios, production needs, recruitment limits, and operational use
- localisation, bespoke vanilla-green large/map-counter consumers and tokens, icon, technology, doctrine, modifier, and script-enum implications
- 3D entity, model, material, idle, movement, attack, death, and runtime-consumer requirements when the unit should look different on the map

Every new custom unit family must also receive a voice and sound design pass. A custom unit should not inherit ordinary infantry voices, weapon sounds, vehicle sounds, or movement sounds by accident when those sounds conflict with its identity.

Every new custom unit family must also receive original counters for every counter surface it uses. The plan must name the exact installed-vanilla definition and DDS, matching skill-local counter family, runtime consumers and tokens, required states and sizes, final paths, sampled vanilla green palette, and `chaosx_icon_artist` handoff. Missing vanilla-reference inspection blocks counter production; reused counters, arbitrary green, and unreferenced imitations are not final.

For each custom unit family, define:

- spoken language, accent, cultural register, command style, or nonverbal vocal identity
- selection, acknowledgement, movement, attack, retreat, idle, damage, destruction, and death sound roles that the unit actually uses
- weapon, engine, mechanical, creature, magical, environmental, impact, and movement sounds required by its equipment and animation set
- sound variation needs so frequent actions do not repeat one clip constantly
- route, culture, ideology, equipment, or transformation conditions that change the voice or sound set
- synchronization needs for attack, movement, recoil, impact, death, destruction, and other visible actions
- source mode, rights, attribution, file format, sound identifiers, runtime consumers, looping behavior, volume, distance, and mix direction
- which vanilla sounds can be reused, with a concrete reason that they fit the unit
- which sounds require new Internet sourcing and which approved vanilla or sourced files can be reused; recording, generation, synthesis, and manual authoring are forbidden

Sound design is part of the unit identity and runtime package. A visually or mechanically custom unit with no planned voice or sound treatment is incomplete unless the spec explains why silence or an existing sound set is intentional.

All custom-unit audio must come from an identified vanilla or externally sourced file with provenance, licensing, and intended-use evidence. If a suitable source cannot be found, the sound role remains blocked instead of being filled with generated or manually created audio.

Treat the unit package as part of the country package. A new military country archetype with an army represented only by renamed vanilla formations is a planning failure unless the spec gives a concrete mechanical and visual justification for reusing those formations.

Starting units must be dynamic. Do not define one flat number of divisions for every country. The spec should explain what makes the starting force stronger, weaker, larger, smaller, better equipped, more irregular, more professional, more defensive, more foreign-backed, or stranger.

Useful scaling factors include:

- chaos tier and chaos value
- event threat, crisis pressure, evolution state, and ordinary stage state
- local population, industry, terrain, ports, rail hubs, depots, and capital control
- local legitimacy, public support, militia networks, and command obedience
- defecting army districts, security units, sailors, railway guards, border guards, police forces, or factory guards
- captured equipment, depot vulnerability, foreign aid, volunteer corridors, and faction support
- parent-country weakness, missed deadlines, lost objectives, supply failure, war state, and previous choices
- whether the tag is an ordinary republic, emergency committee, factory state, ancient restoration, partisan movement, cult, railway state, naval state, or other special actor

For every meaningful new or transformed country, map:

- starting division families or template concepts
- expected starting strength in weak, normal, severe, and high-chaos openings
- equipment and manpower source
- whether units are militia, regular defectors, border guards, mountain detachments, factory guards, railway troops, sailors, cavalry, foreign volunteers, ancient levies, or special high-chaos formations
- starting commanders, officer shortages, or leader ties when relevant
- defensive bonuses, training penalties, supply weaknesses, morale problems, or legitimacy risks
- how the package affects threat meters, foreign attention, depot pressure, old-movement resurgence, or parent-country authority
- what report, event text, or localisation direction should explain why those troops exist

The spec must also map how newly appearing countries can get more units after spawning. This should include decisions, timed objectives, focus rewards, volunteer systems, depot captures, foreign missions, local mobilization, League or faction training, factory guard mobilization, border guard formation, or special high-chaos recruitment where appropriate.

Do not make reinforcement depend only on political power or command power. Use concrete goals and resources such as holding a capital, guarding a border, controlling a depot, controlling rail lines, spending army XP, consuming equipment, committing manpower, using fuel or trains, securing local support, opening a foreign corridor, finishing a construction quota, proving legitimacy by a deadline, placing divisions in required states, or keeping a volunteer route open.

Unit-creating focuses and decisions must be specific. Avoid repeated generic rewards such as `add two infantry divisions` across many countries. A unit reward should explain the institution and story behind the unit, such as capital defense committees, local garrison defections, railway guards, factory guard shifts, mountain pass detachments, Black Banner columns, sailor battalions, Basmachi cavalry, ancient host militias, medical volunteers, foreign-trained cadres, or high-chaos special units.

Each unit-creating focus or decision should define:

- what unit or template family appears
- what unlocks it
- what non-political-power requirements it uses when appropriate
- whether it is repeatable, timed, risky, route-locked, or one-time
- what pressure or threat values it changes
- what downside it creates if repeated or failed
- what AI should do with it
- what blocked localisation direction should communicate when requirements are missing
- what icon, spirit, report event, or commander asset it needs when relevant

For focus trees, military growth should be integrated into branches. Some focuses can spawn units directly, but others should unlock decisions, improve templates, recruit commanders, create volunteer corridors, integrate militias, convert irregulars into regulars, expand special units, or change mobilisation rules. A deep tree should offer different ways to build an army depending on politics, foreign influence, economy, terrain, ideology, and chaos state.

### 3D model and skeletal animation planning standard

When a feature adds a visible unit, building, creature, vehicle, aircraft, naval object, map entity, or other 3D surface, plan the model package as a first-class feature surface rather than treating it as an optional render.

Classify the asset before writing the 3D asset section: static prop, building, humanoid unit, non-humanoid creature, vehicle, aircraft, naval object, or articulated attachment.

For a unit, define the gameplay consumer, unit category or sub-unit, entity key, `.asset` key, `.mesh` key, material and texture paths, large/map-counter consumers and tokens, idle action, movement action, attack action, death or destruction action when relevant, and the exact country, province, state, or map test that will show it.

For a building or map entity, define the building key, entity key, mesh key, state and province placement, valid state-to-province relationship, level or construction behavior, zoom visibility, rotation, runtime scale, and a test location that is inside the intended state and does not hide the model behind an existing building.

If the user does not provide a ready reference image, plan exactly one clean Meshy-ready reference image for the asset and route it through the approved image-generation workflow before the provider gate.

Meshy 7 is the generation model. The plan must forbid silent downgrade and require the exact live model identifier in provider evidence.

Select the requested model operations and required components under [Route selection and component completion](../../chaos-redux-3d-model-pipeline/SKILL.md#route-selection-and-component-completion). The specification must retain separate generated body/item inputs, one supported rig/action attempt, authorized Blender completion/fallback, calibrated component budgets, source and credit limits, contact/deformation/semantic review, and export/reimport. Existing geometry alone never mandates a rebuild.

Never plan a side-profile sheet, turnaround board, collage, or multi-view board as a Meshy input. Blender QA views and contact sheets are review evidence only and must never be sent to Meshy.

The planning spec must name the installed vanilla mesh and entity that establish axes, orientation, source geometry height, entity scale, origin, ground or water contact, and effective runtime height.

For humanoid units, the custom source geometry must match the named vanilla source mesh height and the entity scale must be applied exactly once. Record source height, entity scale, effective runtime height, coordinate axes, facing direction, origin, and the measurement evidence in the plan.

For every requested skeletal action, define the semantic role, action name, FPS, frame range, loop policy, root-motion or in-place policy, ground-contact requirement, retarget or authoring route, static fallback policy, runtime binding, and acceptance evidence.

Do not let a static render or still mesh stand in for a requested skeletal animation. If an action cannot be produced, the coding-agent prompt must mark it blocked or needs_user_review with the reason.

Plan every output in [Evidence package and handoff](../../chaos-redux-3d-model-pipeline/SKILL.md#evidence-package-and-handoff), including source/runtime separation and final hash-aware synchronization so an older copy cannot replace the approved runtime candidate. User-supplied live observations remain optional for agent delivery.

Route production to `chaosx_3d_model_pipeline` with every input and boundary required by [Bounded subagent route](../../chaos-redux-3d-model-pipeline/SKILL.md#bounded-subagent-route); the specification and coding prompt must carry that complete contract.

The coding-agent prompt must state that the main implementation agent owns `.asset`, entity, `.gfx`, unit/building/gameplay wiring, valid province and state placement, code review, useful local checks, and any game results supplied by the user. The user performs live runtime validation; agents neither request nor await it as a delivery gate.

#### 3D model planning matrix

| Surface | Minimum planned evidence |
| --- | --- |
| Humanoid unit | Vanilla source-height measurement, entity-scale crosswalk, repaired geometry, PDX material audit, idle/move/attack actions, `.mesh`/`.anim` reimport proof, unit consumer/source binding, plus any available user-supplied movement observations and screenshot |
| Building or static map entity | Vanilla building precedent, valid state/province pair, entity and `.asset` existence, mesh/material proof, scale and placement/source checks, construction or level contract, plus any user-supplied zoom/construction observations and screenshot |
| Creature, vehicle, aircraft, or naval object | Profile-specific axis and contact calibration, topology/material proof, required action list, export/reimport proof, entity/runtime wiring, plus any user-supplied domain-appropriate live observations |

## Chaos generation and feedback standard

Chaos is a measure of global instability, abnormality, and breakdown. It is not a moral score. A beneficial but impossible incident can raise Chaos because the world has become stranger and less predictable, while successful containment can lower Chaos because a destabilizing force has actually been pushed back.

Events must be active sources of Chaos, not only consumers of the current Chaos tier. The intended campaign loop is that higher Chaos makes events more severe and strange, then successful strange movements, concrete consequences produced by evolved behavior, failed containment, special Chaos countries, and other abnormal outcomes can push the Chaos Meter higher again. This feedback loop should be strong enough to matter without letting one repeatable action farm the campaign from calm conditions to World Collapse.

A genuinely strange, anomalous, violent, reality-breaking, extremist, supernatural, or system-disrupting event should normally create at least one positive Chaos source when its first meaningful manifestation occurs. Do not add Chaos merely because the random-event picker selected an event. The incident itself must have changed the world in a destabilizing or abnormal way.

Ordinary beneficial development should not raise Chaos just because it makes a country stronger. A factory program, normal military reform, ordinary election victory, or routine research success is not a Chaos source unless the event gives that success a wider destabilizing, anomalous, or threatening meaning.

### Required Chaos impact map

Every event that can materially destabilize the campaign must include a Chaos impact map in its specification. The coding agent should never have to invent the event's Chaos feedback during implementation.

Use a table or equivalent structured section with at least these fields:

| Milestone or outcome | Why global Chaos changes | Direction | Starting magnitude or band | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | --- | --- | --- | --- | --- |

Map the event from first manifestation through later success, spread, evolution-enabled consequences, containment, defeat, and aftermath. A large event may need many rows. A small event may need only a few.

If a genuinely strange or destabilizing event has no positive Chaos source, the spec must explain why. Do not omit Chaos simply because the event already uses Chaos as an evolution gate.

### Chaos source families to inspect

Actively look for Chaos sources in these event outcomes when they fit the event:

- first public or material manifestation of a strange incident
- an event-created movement reaching a meaningful support, organization, territorial, or institutional threshold. Peaceful success can still raise Chaos when it proves that the event-created movement has become a real new political or social force
- a movement winning a revolt, coup, election crisis, government struggle, or other route that materially expands the event's power or destabilizes the country or world
- creation, release, transformation, or public recognition of a special Chaos country
- a special Chaos country gaining meaningful territory, population, industry, subjects, allies, faction members, strategic capitals, or regional reach
- an abnormal actor defeating a major enemy, containment coalition, anti-event league, or other force that was holding it back
- a dangerous focus-route, decision-route, project, doctrine, technology, unit family, weapon, supernatural power, or special capability becoming operational
- spread into a new state group, strategic region, country, sea route, continent, or other meaningful geographic layer
- failed containment, missed crisis objectives, broken quarantine, collapsed negotiations, radicalization, mutiny, mass defection, or another event-specific failure
- a concrete consequence caused or intensified by an evolution, such as a new outbreak, spawned actor, territorial breakthrough, government transformation, destructive incident, capability actually entering use, or another material escalation
- a normal country adopting, sponsoring, weaponizing, legitimizing, or exporting an event-created abnormal system
- a new event-created faction, league, cult, military order, machine network, plague realm, supernatural authority, or other power structure reaching a meaningful milestone
- an event-to-event interaction or cluster combination creating a new level of instability beyond the ordinary effects of its member events
- a super-event-level reveal, irreversible transformation, or global escalation milestone
- progress toward an event-owned terminal state when that progress represents a real new loss of world order rather than a hidden bookkeeping threshold

Do not treat this list as a requirement to add every source to every event. Use the sources that represent real changes in the event's power, reach, or abnormality.

Evolution status is never itself a real change for Chaos accounting. Eligibility, MTTH completion, stage activation, evolution logging, unlocking a branch, or incrementing an evolution variable must have zero direct Chaos effect unless the same operation also causes a separate concrete outcome.

### Special Chaos country power growth

When an event creates or manages a country that counts as a special Chaos actor, its growth should feed the Chaos Meter through meaningful milestones. Do not let a supernatural, extremist, plague, death-state, machine, cannibal, anomalous, or other event-created Chaos country become a continental power while the meter reacts only to its initial creation.

Useful power milestones include:

- creation or transformation into the Chaos identity
- first durable territorial gain
- capture of an important capital, refuge, holy site, laboratory, industrial center, or event-specific strategic objective
- control of a meaningful territorial, population, industrial, or military band
- first subject, protectorate, faction partner, converted government, or foreign client
- first expansion into another region or continent
- defeat of a major opponent or organized containment bloc
- completion of a route that unlocks a much stronger army, special unit family, weapon, power, technology, or recruitment system
- transition from a local actor into a regional, continental, or global threat

Use thresholds and one-shot milestones. Do not award Chaos for every factory built, every division spawned, every daily population change, or every single state tick when several changes are part of one continuous expansion.

### Source sizing and scaling

Use the existing shared Chaos sources as calibration. Event-specific additions should normally use several readable milestones instead of one huge opening jump. Suggested starting bands are:

| Event-specific change | Starting Chaos band | Typical use |
| --- | ---: | --- |
| Local strange manifestation | `+2` | First meaningful appearance, small abnormal incident, first durable local success |
| Regional escalation | `+3` to `+5` | Movement breakthrough, new Chaos polity, failed containment, spread into another region |
| National or systemic power gain | `+10` to `+15` | Government capture, major Chaos-country growth, dangerous capability entering use, major consequence produced by evolved behavior |
| Major international or global escalation | `+20` to `+50` | Cross-continental spread, major-power collapse into the event, global reveal, near-terminal breakthrough |

These are planning anchors, not universal constants. Scale with the event's footprint, severity, actor strength, geographic reach, rarity, and existing generic Chaos consequences. Keep authored values easy to tune and use dynamic factors when the same milestone can occur at very different scales.

Current Chaos can influence an event-specific gain when it genuinely changes the severity of the outcome, but do not strongly multiply every gain by the current Chaos value. The event system already accelerates and evolves at higher Chaos, so aggressive direct multiplication can create an uncontrolled feedback spiral.

Do not use a giant event-specific Chaos grant merely to force the meter over `1000`. World-end readiness should emerge from accumulated campaign consequences and the owning terminal route's real prerequisites.

### Shared-source overlap and abnormal significance

The shared Chaos Meter already reacts to wars, annexations, puppeting, faction changes, ideology changes, nuclear use, world tension, military buildup, deaths, air contamination, and other global systems. Event planning must account for those existing sources.

Do not duplicate the same fact twice. If an event kills civilians and the Deaths system already converts those deaths into Chaos, do not add another event-specific gain whose only reason is the same deaths. If contamination already raises Chaos, do not repeat the contamination value as a separate event bonus.

An event-specific premium is valid when the same action has additional abnormal significance that the generic source does not measure. For example, annexation already has a generic Chaos effect. A supernatural Chaos country taking its first major capital can also receive a separate event-specific milestone because the abnormal actor itself has crossed a new power threshold. Those are two different causes and should be documented as such in the Chaos impact map.

Cluster incidents should follow the same rule. Member events keep their distinct Chaos sources, while a separate cluster-level Chaos source should exist only when the combined incident creates an additional destabilizing condition that the members do not already represent.

### Repetition, cooldowns, and anti-farming

Repeatable sources need explicit protection against farming. Use one or more of these patterns:

- one-time milestone flags
- first-time-per-region or first-time-per-continent rewards
- power-band thresholds
- cooldowns
- diminishing returns for repeated ordinary incidents
- stronger rewards only when a repeated event reaches a genuinely new severity or footprint
- caps on one event family's direct contribution over a short period

A repeatable event can still keep raising Chaos when each firing creates a real new crisis. Repetition alone should not be enough.

Do not require recurring whole-world scans merely to discover that a Chaos actor became stronger. Prefer event-owned actions, state-control changes, focus or decision completions, evolution-owned incidents that actually change the world, war outcomes, and bounded milestone checks that already occur when the relevant state changes.

### Evolutions and triggerable scenarios

Reaching, unlocking, activating, logging, or advancing an evolution must not add Chaos by itself. Evolution state only changes what the event is capable of doing. Chaos changes when an evolution causes a concrete world consequence, such as spread, conquest, a spawned actor, government capture, a destructive incident, failed containment, or a dangerous capability actually being used or becoming materially present. Attach the Chaos source to that consequence and guard it there.

If an evolution activates and only unlocks future focuses, decisions, AI behavior, incidents, or capabilities, Chaos remains unchanged until one of those unlocked paths produces a mapped destabilizing outcome. If the evolution activation event itself simultaneously causes a real world change, attribute Chaos to that real change, not to the abstract evolution stage.

A pre-fire evolved opening receives no extra Chaos merely for starting at a higher evolution stage. Its stronger opening can generate Chaos through the concrete incidents and outcomes that actually occur during that opening.

Triggerable scenarios already create instant Chaos from their setup controls. The spec should define how scenario type and intensity affect that initial amount when relevant. After setup, the resulting event actors and mechanics should continue to use the same normal Chaos impact map as automatic play. Manual launch must not suppress later movement victories, Chaos-country power milestones, evolution-enabled consequences, or containment reversals.

### Containment, defeat, and Chaos reduction

Events can lower Chaos when the player or AI materially reverses an event-created source of instability. Useful negative sources include:

- destroying or dissolving a special Chaos country
- defeating an event-created movement after it had established real power
- curing, sealing, banishing, dismantling, or permanently containing an abnormal system
- retaking a major event-specific objective from a Chaos actor
- breaking an event-created faction, cult, network, or weapon program that had become a major source of instability
- completing a durable peace or restoration outcome that actually reverses the event's destabilizing state

Do not automatically refund every point previously added. Deaths, destruction, contamination, political fragmentation, and other lasting consequences may remain. A containment reduction should represent the instability that has genuinely been removed.

### Handoff and completion requirements

The coding-agent prompt must require implementation of the complete Chaos impact map, including positive sources, negative sources, dynamic scaling, repeat guards, shared-source overlap, evolution-enabled consequence sources, and special Chaos-country power milestones.

The goal prompt must treat Chaos-source coverage as a pass or fail requirement for destabilizing events. A completed event should be able to show where its Chaos comes from across the full lifecycle, not only at the opening popup.

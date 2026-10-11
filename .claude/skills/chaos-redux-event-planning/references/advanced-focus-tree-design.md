# Focus tree, mechanic, and decision design standards

Read the relevant complete section before specifying a major focus tree, its reward and idea design, its special mechanics and faction systems, or its decision categories.

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

When a specification adds or changes technologies, doctrines, folders, prerequisites, unlocks, grants, or research bonuses, the coding-agent prompt must require the implementation agent to inspect the affected graph with `hoi4.tech_inspect`, render the relevant folder or branch with `hoi4.tech_render`, and compare the implemented source with `hoi4.tech_inspect` (`mode = compare`). The plan must identify intended placement, prerequisites, exclusivity, unlocks, bonuses, and asset needs so the implementation agent has a concrete result to verify. Apply the AGENTS.md retry limits and use direct source checks when a route remains unavailable; missing tool output does not remove any placement, prerequisite, unlock, bonus, or asset requirement.

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

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.claude\skills\chaos-redux-event-assets\assets\gfx_references\icons\decision_categories\pictures`

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

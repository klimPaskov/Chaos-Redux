---
name: chaos-redux-event-planning
description: Use when expanding Chaos Redux event ideas into detailed specifications before implementation.
---

# Chaos Redux Event Planning

Use this skill to design or expand events for the Hearts of Iron IV mod Chaos Redux (https://github.com/klimPaskov/Chaos-Redux).

This skill creates event specifications. It does not implement code. Implementation belongs to `chaos-redux-events`. Visual asset generation and processing belongs to `chaos-redux-event-assets`. Animated sprite planning, frame-sheet requirements, animated portrait packages, and animation handoff details belong to `chaos-redux-frame-animation` when motion is needed. Super-event quote, remark, music, and presentation research belongs to `chaos-redux-super-events`.

## 1. Required reading

Before writing the event specification, use the following as the design baseline:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets` when the event needs visual assets
- `chaos-redux-frame-animation` when the event has animated sprites, animated UI, animated route emblems, animated portraits, warning pulses, hover loops, glow loops, float loops, particle loops, or frame-by-frame presentation needs
- `chaos-redux-super-events` when the event needs a super-event
- `chaos-redux-improvement-loop` before a near-completion review, and whenever the design may still be shallow, disconnected, bloated, or missing deeper playable consequences
- `chaos-redux-subagents` before spawning `chaosx_improvement_loop_planner` or any other project subagent
- `chaos-redux-focus-trees` or the current focus-tree skill when the event needs focus trees
- `chaos-redux-decisions-missions` when the event needs decisions, missions, timed objectives, influence actions, or decision-driven mechanics
- the event catalog export-only CSV snapshots
- provided existing event docs
- provided Chaos Redux mechanics docs

Use those sources to understand how Chaos Redux already works, then expand creatively from there.

Inspecting the repo is mandatory, but the specification should not read like a technical audit. Use repo findings to prevent mistakes and match patterns. Keep proof of inspection in the final response checklist, not in admin sections inside the spec.

## 2. Input

The user will provide either:

- a rough event idea
- a partly developed concept
- an existing event that needs deeper rework
- a detailed spec that needs cleanup before implementation

Treat the user idea as the starting point. Do not assume it is final.

When the idea is rough, expand it into a deeper design.

When the idea is already detailed, preserve the core direction and improve structure, clarity, missing connections, and implementation readiness.

## 3. Design purpose

The goal is to create an event that feels like a layered Chaos Redux system, not a basic popup.

The event should have atmosphere, player choice, consequences, escalation, lore, replay value, and enough visual support to feel finished.

The design should be ambitious. Do not get lazy, conservative, or minimal unless the event is genuinely small. Depth matters more than speed. Take the time needed to research, compare patterns, think through consequences, and design the event as if the coding agent will implement exactly what is written.

The finished spec should make the coding agent feel that the event has already been designed in full.

## 3.1 Idea-first specification style

The spec should focus on the event idea, not on obvious implementation plumbing.

Do not put sections such as:

- `Scope`
- `Source baseline`
- `Repository context`
- `Spreadsheet row`
- `Existing implementation audit`
- `Generic trigger safeguards`

The spec should be player-facing design and implementation-relevant event design.

Avoid obvious lines such as:

- the event only fires if enabled
- the event should not fire after a world-end scenario
- disabled events should not fire
- the coding agent should use valid syntax
- the system should respect existing global settings

Those are baseline system responsibilities. Include technical notes only when they prevent a likely mistake, explain non-obvious behavior, or define a unique rule for this event. Otherwise, its just noise.

Do not create negative capability notes for absent event surfaces. If an event does not have a world-end scenario, do not mention world-end scenarios. If an event does not have a manual triggerable scenario, do not mention triggerable scenarios. Do not write sections, bullets, event-detail notes, spreadsheet-facing summaries, implementation prompts, or player-facing text that say `no world-end scenario`, `does not have a world-end scenario`, `no manual triggerable scenario`, `does not have a triggerable scenario`, or similar absence wording. Omit the surface completely unless it actually exists or the user explicitly asks for an explanation of why it is absent.

### Tone and presentation direction standard

For every player-facing text surface, the planning spec should define the writing direction and leave finished wording to implementation. This includes event titles, event descriptions, report text, news text, focus text, decision text, option text, achievement text, super-event setup, GUI labels, route flavour, event-detail text, and spreadsheet-facing summaries.

Give the coding agent clear direction for:

- actor or viewpoint
- force driving the event
- information visible to the player
- information that should remain uncertain
- tone, severity, and humour mode
- references that need research
- words, frames, or clichés to avoid
- dynamic actors, states, countries, values, or routes that final text should mention

Do not provide pasteable localisation. Do not include `sample line`, `possible line`, `placeholder text`, `temporary title`, or exact draft wording that could be copied into localisation. When a structural label is needed for a file, row, route, branch, asset, or prompt, mark it as a working label, not final localisation.

Text direction should avoid bland map-summary framing and generic communications clichés. Do not make the emotional center of an event a changed map, a line of advance, a staff-table scene, a failed broadcast, or another stock image of crisis administration.

When planning player-facing warning, threat, suspicious-report, and escalation text, do not instruct the coding agent to say that something is a warning, that something is not a warning, that a threat is coming, or that a danger signal has appeared. The text should show the pattern through partial information: fearful witnesses, rumours, anomalies, mysterious powers seen, etc

A report can make the player uneasy without naming the unease. Use mystery, information gaps, fear, rumours, etc. The player should infer that something may be wrong from the content and consequences, not from a label.

When a concept benefits from mystery, fantasy, surrealism, myth, occult signs, prophecy, impossible resolve, strange energy, or unclear public rumours, state that direction clearly without drafting the final prose.

### Event option humour, irony, and cultural remark direction

The planning spec may define what an option should feel like, what stance it represents, and how it should vary by route or actor. It must not write final option text.

Do not let the implementation agent default to bland buttons unless plainness is intentional. Describe the intended option style, such as official denial, sarcastic acceptance, bitter understatement, cultural allusion direction, period propaganda tone, frightened understatement, arrogant boast, administrative absurdity, local proverb direction, or grim irony that condemns the speaker.

For each important option or option family, define:

- who is speaking or reacting
- what the option means mechanically and narratively
- whether the tone should be serious, ironic, sarcastic, cruel, frightened, resigned, bureaucratic, or absurd
- what kinds of cultural references may fit
- which references need research before wording is written
- how route, ideology, chaos tier, campaign state, or country culture should change the reaction

Humour should fit the stakes. Minor chaotic events can use sharper jokes and visible sarcasm. Major disasters, massacres, atrocities, mass death, and real-world suffering should use severity, official euphemism, cynical propaganda, hypocrisy, or self-damning grim irony. Cheap comedy is forbidden there.

Cultural remarks should be treated as research directions unless already sourced. The spec may say that a line should draw from a period slogan, military idiom, folk saying, religious register, old newspaper style, literary echo, propaganda formula, or local public habit. It must not invent the exact remark.

Do not list example option lines. Do not write sample buttons. Do not write placeholder localisation for options. Coding agents may paste those into the game.

Some events need one cutting reaction direction and one plain practical reaction direction. Some need several route-specific reaction directions. The spec should state the intended option tone and purpose, then leave the final wording to the coding agent.

## 3.2 Depth standard

The specification should be as deep as the event idea deserves.

For small events, this may mean a compact but complete spec. For major events, world crises, custom UI systems, event chains, focus trees, custom tags, or events with evolutions, the spec should become very large and multi-part.

Do not aim for a short answer. Aim for a complete design.

For larger events, it is acceptable and expected for the finished specification to span many files and potentially reach tens of thousands or more than 100,000 lines. A huge event with multiple countries, full focus trees, rare variants, and world-order routes can justify 100,000+ lines, and even more, across all parts if the content is meaningful. Do not shorten the spec because it becomes long.

Do not add filler to reach a size target. Add depth by thinking through the event from every useful angle:

- player experience
- event pacing
- escalation
- alternate paths
- rare outcomes
- decision maps
- branch maps
- AI strategy matrices
- country package matrices
- starting armies, unit templates, force-growth decisions, and dynamic military setup for newly appearing countries
- dynamic country identities, cosmetic names, flags, leaders, and politics
- AI behavior
- world reactions
- country-specific reactions
- ideological interpretations
- UI presentation
- event log presence
- assets
- super-events
- achievements and difficult achievement routes
- world-end branches
- event cluster behavior
- focus trees
- clear focus-tree path maps with major routes, anchor focuses, mutual exclusions, and branch logic
- custom tags
- flag, portrait, emblem, and country-identity asset needs
- historical source needs for real flags, leaders, symbols, and portraits
- interactions with existing Chaos Redux systems
- documentation needs

Every section should add usable design, player-facing detail, implementation clarity, asset direction, or system connection.

## 3.3 Research depth standard

Use research to make the event richer. Do not rely on the first obvious idea.

When the event has historical, cultural, scientific, political, regional, military, religious, or ideological inspiration, research enough to produce specific variants, names, factions, symbols, motives, and consequences.

Research should help answer:

- what real or plausible movements inspire the event
- what old conflicts, myths, institutions, military traditions, or political factions can return
- what regional differences should matter
- what foreign governments would believe
- what soldiers, civilians, journalists, scientists, diplomats, or observers would think
- what rare branches can appear only in unusual campaign states
- what assets and symbols would fit each branch
- what focus tree paths each new country should have
- what starting forces and later unit-generation routes each new country should have
- what each major focus path and anchor focus should do, unlock, represent, and connect to
- what achievements would reward deep mastery, rare routes, and difficult campaign outcomes

If the topic is niche, current, uncertain, or historically specific, verify with reliable sources. Do not invent source claims. If a source-dependent point is uncertain, mark it as uncertain.

Research should not make the spec dry. Use it to create better event content.

## 3.4 Full decision, rare variant, and branch mapping

When the event includes decisions, rare variants, country paths, custom actors, or special outcomes, map them out fully.

Do not write vague lines such as:

- add some decisions
- add rare variants
- create several flavor events
- the country should get a focus tree
- the branch can become extreme
- some strange countries may appear

Instead, define the content. For each meaningful decision or decision group, map:

- who sees it
- when it becomes available
- what it means in the story
- what the player is choosing between
- what short-term consequence follows
- what long-term consequence it can create
- what pressures, cooldowns, costs, sacrifices, or risks it changes
- what the decision costs beyond political power or command power, such as army XP, navy XP, air XP, equipment, manpower, stability, war support, fuel, trains, convoys, supply strain, tied-down divisions, local support, faction cohesion, foreign influence debt, legitimacy, or crisis pressure
- what AI should prefer and why
- what variants or follow-up events it can unlock
- what assets, icons, or localisation it needs

For rare variants, map:

- the conditions that make them possible
- the campaign state that makes them more likely
- what the player first sees
- how observers interpret it
- what new rules or actors it adds
- what decisions, focuses, spirits, events, or super-events it unlocks
- how it ends, spreads, mutates, or is contained
- what makes it different from the baseline event

For branch trees or outcome webs, show the structure. Use headings, named routes, tables, or lists. The coding agent should not have to invent the branch map.

## 3.5 Focus tree path design standard

Focus trees must be planned clearly, but the event-planning spec should not try to micromanage every final focus node, every coordinate, or every exact connection. The spec writer should define the tree's routes, branch architecture, major choices, mutual exclusions, story logic, mechanics, rewards, and design standards. The implementation agent should then create the final in-game focus tree layout and exact focus connections cleanly.

A good focus-tree spec should answer:

- what major paths the country has
- what each path means in the story
- what each path changes mechanically
- which paths are mutually exclusive
- which paths can cooperate or converge
- which paths are hidden, rare, chaos-locked, evolution-locked, foreign-aid-locked, or crisis-locked, etc
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

When a specification adds or changes technologies, doctrines, folders, prerequisites, unlocks, grants, or research bonuses, the coding-agent prompt must require the implementation agent to inspect the affected graph with `hoi4.tech_inspect`, render the relevant folder or branch with `hoi4.tech_render`, and compare the implemented source with `hoi4.tech_compare`. The plan must identify intended placement, prerequisites, exclusivity, unlocks, bonuses, and asset needs so the implementation agent has a concrete result to verify.

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

Fixed-purpose chaos countries can have narrower politics when their identity demands it. A death-state, plague-state, machine-state, or pure destruction actor may have one ideological purpose. Even then, the tree should still provide meaningful internal choices inside that purpose, such as doctrine, expansion method, recruitment, economy, hierarchy, or endgame ambition.

Focus trees and decision systems must be planned together. Focuses should unlock or change decisions and missions. Industry focuses can unlock construction decisions. Military focuses can unlock unit, depot, border, or offensive missions. Diplomacy focuses can unlock recognition, aid, volunteer, and influence decisions. Expansion focuses can unlock declarations, league votes, protectorate demands, border incidents, claims, cores, war goals, and settlement decisions.

For each major focus path, describe which decision or mission families it unlocks and how those decisions expand the mechanic.


### Branch interaction, payoff, and country identity

Political, industry, and expansion are the minimum branch families, not the full design for important countries. Important countries should usually also define military, diplomacy, internal faction, intelligence or security, special mechanic, and late-game branches when their identity supports them.

Branches should not be isolated columns. Political choices should change which expansion, industry, military, diplomacy, and decision paths are available. Industry should support military or expansion. Expansion should create political consequences. Diplomacy should affect foreign aid, war options, faction choices, and sponsor risk.

Every major branch needs a clear payoff. A political branch can end in a new government, leader, ideology, law system, ruling party, or country identity. An industry branch can end in a rebuilt economy, arsenal, resource system, railway authority, construction mechanic, or production network. An expansion branch can end in a league, empire, federation, protectorate network, reunification, liberation order, regional settlement, or external war plan.

A good focus path should unlock new gameplay, not only stats. The plan should describe decisions, missions, units, advisors, leaders, laws, claims, cores, war goals, buildings, events, mechanics, route access, and AI behavior where they fit. Flat modifiers are supporting rewards, not the main design.

Political routes should update the visible country package where relevant: leader, leader portrait, advisor roster, high command, ruling party, party names, ideology drift or swap, cosmetic name, flag, ideas, and AI strategy. Leader changes imply portrait needs.

Expansion branches should create consequences. Claims, cores, and war goals should interact with diplomacy, factions, resistance, foreign guarantees, local leagues, legitimacy, threat, or postwar settlement decisions.

Industry branches should create map or production changes. Define factories, infrastructure, railways, supply hubs, forts, anti-air, airbases, dockyards, resources, production lines, or construction decisions.

Decision categories should evolve with focus progress. Early focuses may unlock basic decisions. Later focuses should add new targets, stronger actions, cheaper costs, new risks, or new mission families. A decision category should feel different after a route develops.

The fixed-purpose exception is narrow. A country is fixed-purpose only when its concept clearly cannot support normal politics, such as a death-state, machine-state, plague-state, or pure destruction actor. It still needs meaningful internal branches around method, hierarchy, economy, recruitment, expansion, and endgame.


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

Important routes should define failure states. A failed political reform can empower radicals. Failed expansion can trigger backlash or settlement. Failed industry can create dependency. Failed foreign-aid balancing can create a client state. Failed military centralization can create rogue generals or militias.

Focus and decision localisation should describe the visible baseline effect of the route or action. It should not reveal hidden effects, secret outcomes, hidden variables, or future surprises. The player-facing text should explain the public action and visible direction, not the hidden implementation.


### Special mechanics, dynamic values, and faction systems

Large events should usually include at least one special mechanic. A special mechanic can be a pressure meter, influence system, balance of power, faction cohesion system, legitimacy system, corruption system, outbreak tracker, coalition command system, resource race, regional authority map, or similar play layer.

A special mechanic should define its important values clearly. Examples include legitimacy, authority, influence, cohesion, obedience, corruption, foreign penetration, military readiness, industrial capacity, public panic, faction unity, sponsor pressure, religious authority, revolutionary zeal, or regional control.

Mechanic values must be dynamic. They should move through focuses, decisions, missions, events, wars, state control, foreign influence, AI actions, and prior outcomes. Do not design a mechanic where values only drift passively or change through a few flat scripted effects.

Every important mechanic value should have a consistent colour identity in localisation. If several values contribute to a total, each contributing value should use its own colour consistently across tooltips, scripted localisation, decision text, event text, and UI summaries. If a mechanic has a total value made from components, the tooltip should show a readable breakdown with named and coloured components.

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

Every special mechanic should define where the player sees it: decision category header, custom scripted GUI, progress meter, scripted localisation tooltip, focus tooltip, national spirit tooltip, or another clear presentation surface. Important mechanic values should not exist only as hidden variables.

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

- early, middle, and late decision tiers
- active mission caps
- region pools that rotate or unlock gradually
- decisions hidden when their route is invalid
- obsolete decisions removed after war, peace, settlement, or route change
- basic decisions replaced by stronger later decisions
- decisions grouped by target region, sponsor, faction, or mechanic value
- emergency decisions visible only during emergency states
- late-game decisions hidden until the route payoff is reached

A decision category should feel curated by the current route and campaign state, not like a debug menu.

### Decision category presentation choice

Every planned decision category should use the least complex presentation that communicates its purpose and current state clearly.

Use this order:

1. ordinary category icon and concise text
2. static category picture
3. animated category picture with a static fallback
4. compact attached display or category header
5. full scripted GUI or separate mechanic window

Do not plan a full scripted GUI only because a category is important. A static or animated category picture is usually the better choice when the category needs identity, atmosphere, propaganda, territorial context, or a clear visual theme but the decisions already carry the gameplay.

Strong category-picture candidates include:

- propaganda, ideology, elections, monarchism, party control, and trade-union politics
- civil-war preparation, insurgency, mobilization, and national preparedness
- faction management, treaties, naval agreements, and foreign intervention
- formables that need a territorial overview
- one-theme national campaigns and crisis categories

A category picture is presentation, not a fake interface. Do not paint buttons, meters, dynamic values, or controls into it.

Use a full scripted GUI only when the player must manage several interacting values, repeated target selection, competing factions, persistent state changes, or exact dynamic state pieces that cannot be presented clearly through normal decisions, category text, tooltips, and one picture.

The asset handoff should point to this canonical picture reference family:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\icons\decision_categories\pictures`

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


## 3.6 Focus tree visual planning standard

Focus tree visuals should help the user and implementation agent understand the intended branch structure. The spec may include a high-level branch diagram, lane map, or route sketch for major trees, but it should not try to lock every final focus coordinate unless the user explicitly asks for that.

A useful focus tree visual should show:

- major path families
- route locks
- mutually exclusive choices
- hidden or rare paths
- convergence points
- late-game route families
- which paths should be visually separate
- which paths should be placed near each other because they interact
- reserved space for a focus inlay window when one is planned

The visual should be readable, symmetrical where possible, and free of tangled connector lines. It should not contain random crossing lines or misleading geometry.

When a special mechanic belongs directly to the focus tree and needs to stay visible while the player chooses focuses, plan a focus inlay window. Define what it shows or controls, its visibility conditions, the tree area reserved for it, and how it affects focus choices. Do not plan an inlay only for decoration or when decisions, tooltips, or a separate mechanic window are clearer.

If the spec creates a graph or diagram, it should be treated as a design guide unless the user says it must match the final in-game tree exactly. The implementation agent may adjust the final layout to make the actual HOI4 tree cleaner.

Do not spend excessive planning effort forcing exact graph coordinates if the result becomes ugly, brittle, or unhelpful. A clear path architecture is more important than a fake exact graph.


## 3.7 Achievement design standard

Achievements are mandatory for event specifications unless the user explicitly says not to include them or the event is so small that achievements would be dishonest. Major events, custom countries, deep focus trees, rare variants, world-order routes, or super-events always need achievements.

Achievements should be creative and difficult. Do not design achievements that unlock just because the event fired, because the player clicked the obvious option, or because a country survived a few days. Achievements should reward mastery, unusual campaign states, risky choices, hidden routes, hard containment, difficult victories, or rare evolved outcomes.

A good achievement should usually require several conditions at once, such as:

- playing a specific country or route
- completing a difficult focus tree branch
- surviving a dangerous crisis state
- defeating or containing a major enemy
- avoiding an easy exploit, puppet shortcut, or foreign bailout
- triggering or suppressing a specific evolution track
- forming a special faction under strict conditions
- completing a rare high-chaos route
- winning while keeping a fragile coalition together
- using a special mechanic successfully without taking the safest path

Do not make achievements conservative. If the event has dark paths, high-chaos tags, strange mechanics, foreign influence systems, coalition politics, or world-order ambitions, design achievements for them. Difficult achievements can require long campaigns, high chaos, multiple wars, internal crises, and careful decision play.

For each achievement, define:

- achievement id or working key
- title direction or working label, not final title
- player-facing description direction
- eligible starting country or countries
- exact story route or campaign situation required
- unlock conditions
- failure or disqualifying conditions
- whether it is visible, hidden, rare, or secret
- difficulty tier
- why it is interesting and not trivial
- icon direction and visual motif
- related focus paths, decisions, evolutions, tags, factions, super-events, or assets
- implementation notes for tracking if the unlock cannot be checked from a single final state

Achievement design must include asset planning. Each achievement needs a 64x64 completed icon direction, and the asset prompt must hand those icons to `chaos-redux-event-assets`. Grey, locked, and not-eligible variants can be produced later if the achievement system requires them.

The achievement list should include a spread of routes. Do not put all achievements on the safest or most obvious path. Cover containment, failure recovery, republic victories, foreign influence, special factions, strange countries, high-chaos routes, and secret or hard branches when those exist.

If an event creates many playable tags, design achievements for the most important ones and for the event-wide systems. A large event can justify dozens of achievements. The achievement prompt should still explain which ones are highest priority if implementation must be staged.

## 3.8 Baseline stages versus evolutions

Baseline stages and evolutions are different.

Baseline stages describe the ordinary flow of the event. They are the expected crisis lifecycle, such as first outbreak, containment attempt, spread, coalition formation, deep collapse, settlement, or defeat.

Evolutions are mutation tracks layered on top of the baseline. They make the event more predictable in some ways, more severe, stranger, more patterned, or more replayable. They can add new actors, new rules, new incidents, new tags, old movements, strange variants, stronger breakaways, or rare side branches.

Do not log ordinary stages as evolutions.

Do not use chaos tiers as simple walls that lock ordinary stage progression. Ordinary stages should flow from the event state. Chaos should affect intensity, probability, severity, weirdness, and opening strength.

### Evolution entry paths

When an event has evolutions, the spec must say how each evolution enters play. Do not write evolutions only as future modifiers or only as post-fire upgrades unless that is truly the design.

Use two separate entry-path concepts when the event supports both.

**Active-event evolution** means the event has already fired and an evolution unlocks while one or more actors from that event still exist or the event system is still active. The spec must define what changes immediately for the active actors: focus paths, decision families, national spirits, unit growth, targeting rules, AI strategy, faction behavior, super-event eligibility, and cleanup. The event should not need to fire again for the active actor to receive the evolution content.

**Pre-fire evolved opening** means the event has not fired yet, but the world state, chaos tier, previous evolution memory, or other allowed event trigger lets the first firing start in a more evolved form. The spec must define the changed opening package: number of actors, target selection, starting ideas, initial units, first decisions, opening events, AI plan.

If both entry paths exist, write both explicitly under one evolution. For example, an event may have an active evolution that unlocks a focus path for an already spawned country, while a later first firing may start with multiple spawned countries.

Each chaos tier can have only one evolution stage. The maximum amount of evolutions is 5.

Good evolutions can include:

- the same kind of crisis becoming easier to recognize and harder to stop
- foreign liaison networks appearing
- old historical movements returning in changed form
- new custom tags appearing that did not exist in vanilla
- extremist, occult, scientific, cultic, or ideological splinters appearing at high chaos
- strange fighter movements, partisan networks, or paramilitary identities forming
- new focus tree routes and decision categories opening

Each evolution should define:

- what changes from the baseline
- what conditions make it possible
- what makes it more likely
- what new player-facing content appears
- what new incidents or variants it unlocks
- what the evolution log title direction should represent
- how it interacts with chaos tier without being only a chaos-tier lock
- how it can be contained, spread, or escalate

## 3.9 Dynamic mechanics standard

Everything that acts like pressure, cooldown, progress, chance, support, duration, cost, tempo, AI willingness, spawn strength, aid amount, stage movement, or recognition should be dynamic by default.

Avoid fixed values as design answers. A fixed number may exist as a tuning anchor, but the spec should define the factors that shape it.

Dynamic factors can include:

- chaos tier and chaos value
- current wars
- stability and war support
- ideology and reforms
- political power, command power, army XP, navy XP, and air XP
- manpower, equipment, fuel, trains, convoys, and supply
- military losses
- supply and rail control
- distance and terrain
- local legitimacy
- foreign access
- diplomatic recognition
- previous choices
- previous Chaos Redux events
- evolution state
- crisis duration
- faction cohesion
- AI personality and strategic situation

Do not say only that a cooldown is 30 days or a pressure increase is 5. Say what makes it shorter, longer, stronger, weaker, safer, or more dangerous.

Dynamic behavior should still be readable. Define cause and effect clearly so the player can learn the pattern through events and decisions.


## 3.10 Cost and sacrifice design standard

Political power and command power are useful, but they are usually the least interesting costs. Do not let major decisions, missions, focuses, or crisis responses become a long list of political power and command power purchases.

A good cost should express what the country is actually spending, risking, or sacrificing in the story. A military crackdown may spend command power, but it should also strain units, consume equipment, lower stability, damage war support, pull divisions away from another front, increase resistance, or worsen a crisis pressure. A foreign intervention may spend political power, but it should also require relations work, liaison access, convoys, fuel, equipment shipments, intelligence exposure, or patronage risk. A mobilization decision may use manpower, infantry equipment, support equipment, training time, army XP, supply, local support, or legitimacy.

When mapping costs, use a varied cost palette where it fits the mechanic:

- army XP, navy XP, and air XP
- infantry equipment, support equipment, artillery, trucks, trains, convoys, ships, aircraft, tanks, or special equipment
- manpower, trained reserves, officer quality, or temporary unit locks
- fuel, supply capacity, rail access, port access, convoy routes, or depot control
- stability, war support, legitimacy, local support, public trust, or faction cohesion
- command power and political power only when they match the story
- construction capacity, civilian factories, military factories, dockyards, repair capacity, or production disruption
- relations, recognition pressure, foreign influence debt, intelligence exposure, or diplomatic credibility
- crisis pressure, threat-meter components, condemnation, deaths, pollution, contamination, or other Chaos Redux system values when relevant
- time, deadlines, objective failure risk, opportunity cost, or visible map requirements such as holding borders, guarding depots, or placing divisions in key states

Political power or command power may still be one part of a cost, but they should not be the default answer. If a section uses mostly political power or command power, redesign it unless the story clearly demands bureaucratic or command attention.

Costs should be dynamic. The amount and type of cost should react to country size, chaos tier, stability, war state, equipment stockpiles, supply state, front pressure, foreign access, local legitimacy, previous choices, AI situation, and current event pressure. A weak country should not pay the same cost as a strong country when the story says the burden is different.

Map blocked localisation for nonstandard costs. The player should understand whether they lack infantry equipment, support equipment, divisions in the right state, local support, army XP, fuel, rail control, relations, foreign route access, or another requirement.

For every major decision family, include at least one cost or requirement that is not political power or command power unless the spec explains why that family is purely bureaucratic.


## 3.11 AI strategy and behavior mapping standard

Major event specs must include a real AI section. Do not leave AI behavior as a vague note that the coding agent can decide later.

The AI section should map how every important affected country behaves across the event. This includes the event owner, breakaways, custom tags, transformed existing tags, foreign sponsors, faction leaders, nearby countries, rivals, allies, and countries that can exploit or contain the event.

For each important AI actor or actor group, define:

- what routes it can choose
- which routes it prefers under ordinary conditions
- which routes it only chooses under high chaos, desperation, ideology, war, foreign pressure, hidden path, or special evolution conditions
- what choices it should almost never make
- how it evaluates decisions, focuses, faction formation, volunteers, recognition, military action, negotiation, puppeting, annexation, and escalation
- how it reacts to dynamic pressures such as strength, stability, war state, proximity, casualties, supply, chaos tier, ideology, and previous outcomes
- how it uses or avoids rare variants and evolved tracks
- how it behaves when it is player-adjacent, major-power-adjacent, or a possible snowball threat
- what cleanup or fallback behavior it should use if its preferred route becomes impossible

For weighted behavior, route the audit through `chaosx_ai_probability_auditor`, give the implementation agent named scenarios and the expected ordering, timing band, dominance limit, or starvation limit to test, and require the coding-agent prompt to begin with `hoi4.probability_inspect`, use `hoi4.probability_evaluate` for the scenario matrix, `hoi4.probability_sweep` for thresholds and rank reversals, and `hoi4.probability_compare` after implementation. Reserve `hoi4.probability_simulate` for explicitly declared uncertain inputs and `hoi4.probability_sequence` for a complete declared custom pool with cadence and state transitions. Request `hoi4.probability_render` when a ranking, matrix, timing, sensitivity, sequence, comparison, or unresolved view will make the handoff easier to review. Do not specify an exact selection probability when the candidate pool or external factors are incomplete.

For focus trees, the spec must define AI path behavior at the branch level and for key individual focuses. If a large tree has mutually exclusive paths, secret routes, or dangerous high-chaos paths, specify which AI personalities or campaign states can choose them. High-chaos AI should be allowed to make strange or extreme choices when that is the point, but ordinary AI should not accidentally choose suicidal or nonsensical branches.

For foreign influence mechanics, the AI section must explain how major powers decide whether to recognize, fund, arm, infiltrate, puppet, betray, or abandon new countries. If volunteers, expeditionary support, proxy wars, or faction invitations exist, AI behavior must be mapped for those too.

A good AI section should make the implementation agent unable to create generic AI weights while claiming to follow the spec.

## 3.12 Country package and dynamic identity standard

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

## Formable nations and formation routes

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

### Formable state-puzzle presentation

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

A small formable whose map requirement is obvious may use a static territorial category picture instead. The spec should state why the static picture is clearer than a dynamic state-puzzle display.

## 3.13 Starting forces and reinforcement pathway standard

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

Every new custom unit family must also receive original counters for every counter surface it uses. The plan must name the exact installed-vanilla definition and DDS, matching skill-local counter family, runtime consumers and tokens, required states and sizes, final paths, sampled vanilla green palette, and `chaosx_icon_artist` handoff. Missing vanilla-reference inspection blocks counter production, reused counters, arbitrary green, and unreferenced imitations are not final.

For each custom unit family, define:

- spoken language, accent, cultural register, command style, or nonverbal vocal identity
- selection, acknowledgement, movement, attack, retreat, idle, damage, destruction, and death sound roles that the unit actually uses
- weapon, engine, mechanical, creature, magical, environmental, impact, and movement sounds required by its equipment and animation set
- sound variation needs so frequent actions do not repeat one clip constantly
- route, culture, ideology, equipment, or transformation conditions that change the voice or sound set
- synchronization needs for attack, movement, recoil, impact, death, destruction, and other visible actions
- source mode, rights, attribution, file format, sound identifiers, runtime consumers, looping behavior, volume, distance, and mix direction
- which vanilla sounds can be reused, with a concrete reason that they fit the unit
- which sounds require new Internet sourcing and which approved vanilla or sourced files can be reused, recording, generation, synthesis, and manual authoring are forbidden

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

## 3.13.1 3D model and skeletal animation planning standard

When a feature adds a visible unit, building, creature, vehicle, aircraft, naval object, map entity, or other 3D surface, plan the model package as a first-class feature surface rather than treating it as an optional render.

Classify the asset before writing the 3D asset section: static prop, building, humanoid unit, non-humanoid creature, vehicle, aircraft, naval object, or articulated attachment.

For a unit, define the gameplay consumer, unit category or sub-unit, entity key, `.asset` key, `.mesh` key, material and texture paths, large/map-counter consumers and tokens, idle action, movement action, attack action, death or destruction action when relevant, and the exact country, province, state, or map test that will show it.

For a building or map entity, define the building key, entity key, mesh key, state and province placement, valid state-to-province relationship, level or construction behavior, zoom visibility, rotation, runtime scale, and a test location that is inside the intended state and does not hide the model behind an existing building.

If the user does not provide a ready reference image, plan exactly one clean Meshy-ready reference image for the asset and route it through the approved image-generation workflow before the provider gate.

Meshy 7 is the generation model. The plan must forbid silent downgrade and require the exact live model identifier in provider evidence.

Normal planned generation, remesh/retexture, rigging, conversion, and required animation credit use is pre-authorized and must not trigger a confirmation prompt. Require confirmation only before additional paid recovery caused by a failed or rejected provider operation, otherwise the worker must not ask for credit confirmation.

Never plan a side-profile sheet, turnaround board, collage, or multi-view board as a Meshy input. Blender QA views and contact sheets are review evidence only and must never be sent to Meshy.

The planning spec must name the installed vanilla mesh and entity that establish axes, orientation, source geometry height, entity scale, origin, ground or water contact, and effective runtime height.

For humanoid units, the custom source geometry must match the named vanilla source mesh height and the entity scale must be applied exactly once. Record source height, entity scale, effective runtime height, coordinate axes, facing direction, origin, and the measurement evidence in the plan.

For every requested skeletal action, define the semantic role, action name, FPS, frame range, loop policy, root-motion or in-place policy, ground-contact requirement, retarget or authoring route, static fallback policy, runtime binding, and acceptance evidence.

Do not let a static render or still mesh stand in for a requested skeletal animation. If an action cannot be produced, the coding-agent prompt must mark it blocked or needs_user_review with the reason.

The model package must plan provider lineage, Blender source and normalized/repaired/material/rigged/action/pre-export checkpoints, processed textures, PDX material channel mapping, `.mesh` and `.anim` exports, reimport proof, runtime hashes, and final live-consumer screenshots.

The asset prompt must distinguish provider source files from final runtime copies. It must require a final hash-aware synchronization step so an older mapped texture, mesh, entity, or animation cannot overwrite the approved runtime candidate.

Route production to `chaosx_3d_model_pipeline` with `fork_context=false` and give it the exact job root, reference status, asset profile, vanilla references, scale relationship, action list, custom-unit sound roles, counter consumers/tokens and inspected vanilla paths, dependency lock, baseline planned paid operations, extra-recovery credit limits, and handoff path. Require Meshy 7 and the no-routine-confirmation credit policy.

The coding-agent prompt must state that the main implementation agent owns `.asset`, entity, `.gfx`, unit/building/gameplay wiring, valid province and state placement, live runtime validation, and in-game evidence.

### 3D model planning matrix

| Surface | Minimum planned evidence |
| --- | --- |
| Humanoid unit | Vanilla source-height measurement, entity-scale crosswalk, repaired geometry, PDX material audit, idle/move/attack actions, `.mesh`/`.anim` reimport proof, unit consumer, movement test, and screenshot |
| Building or static map entity | Vanilla building precedent, valid state/province pair, entity and `.asset` existence, mesh/material proof, scale and zoom test, construction or level test, and screenshot |
| Creature, vehicle, aircraft, or naval object | Profile-specific axis and contact calibration, topology/material proof, required action list, export/reimport proof, entity/runtime wiring, and domain-appropriate live test |

## 3.14 Mandatory asset coverage and source-mode standard

Everything visible or meaningful needs an asset plan. A major spec should not only define a few event pictures. It should identify assets for countries, focus trees, decisions, ideas, national spirits, achievements, flags, portraits, faction emblems, super-events, event pictures, UI, unit systems, and route-specific identity changes.

Every focus in a mapped focus tree needs an icon direction. Large trees may use reusable icon packs, but the spec must still state which focuses use which motif or icon category. Do not leave hundreds of focuses with no asset guidance.

Every decision, decision category, idea, national spirit, achievement, faction emblem, UI panel, news image, report image, super-event image, leader or council portrait, and important special-unit identity that appears in the event needs an asset entry or a clear asset-family entry.

Every country package must include flags. Required flag coverage includes normal, medium, and small sizes for each implemented flag state. If the country has ideology-specific names, focus-tree transformations, puppet identities, restored historical forms, radical routes, or high-chaos mutations, the spec must identify whether those states need separate flags.

Every new flag uses `$imagegen`. For a real or historically attested country, movement, party, military authority, or restoration path, the asset prompt must first require reliable design research and a cited reference. Imagegen then reconstructs that exact design as a flat flag under the reference constraint. It must not produce waving fabric, painterly flag artwork, scenery, gradients, perspective, fake lettering, or invented heraldry. The asset prompt must require a manual geometry, colour, orientation, and symbol comparison before HOI4 flag resizing. Fictional and alternate flags also use imagegen, while remaining flat flag designs rather than illustrations.

Historical or real leaders must not be generated, and grounded polities must not receive invented substitute people. Treat a polity as grounded when it existed in whole or in part, represents a real community, or claims continuity from a real institution. The spec must identify its real portrait or institutional-material needs and instruct `chaosx_portrait_creator` to source attributed material, document source and license status, choose an explicit head-and-shoulders crop for a person, prepare the placeholder, and review the user-supplied HOI4-style final against the canonical reference root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` plus its role-specific contact sheet. Generated one-person portraits are reserved for wholly fictional leaders of wholly fictional, deliberately high-chaos polities and must be created and processed by the portrait worker. Fictional councils and symbolic bodies should use people-free institutional compositions.

When an asset source is historically sensitive, disputed, or politically loaded, the asset prompt must require source notes and a clear distinction between sourced historical use and fictional alternate-history invention.

## 3.15 Effect strength and impact standard

Do not design important event effects with timid, decorative, or micro values. If an idea, decision, focus, mission, national spirit, crisis response, starting debuff, or route payoff is supposed to matter, its effects must be strong enough for the player to feel and plan around.

Micro modifiers do not count as meaningful design. Avoid values such as plus 2 percent, minus 3 percent, or tiny flat changes as the main reward, penalty, starting debuff, crisis modifier, or route payoff. A small modifier can support a larger effect package only when it belongs to a visible stacking system, a frequent tick, or a clearly explained cumulative mechanic. It cannot be the whole design.

Starting negative debuffs must matter. They should create real pressure on survival, production, mobilisation, logistics, legitimacy, command, diplomacy, state control, AI behavior, or player priorities. A starting problem that the player can ignore has failed. The spec should map how the player feels the debuff, why it exists, which choices mitigate it, and what happens if it is left unresolved.

A good effect package should do at least one meaningful thing:

- change player incentives
- unlock a new decision, mission, focus branch, unit type, mechanic, or route
- move a crisis, loyalty, legitimacy, recognition, stability, or threat value in a visible way
- create a real cost, risk, or tradeoff
- apply a strong positive or negative modifier that changes army, economy, diplomacy, internal politics, logistics, production, intelligence, state control, or AI behavior in a visible way
- create an urgent weakness, route identity, or route payoff the player cannot ignore
- change how a country plays for a meaningful period
- connect to later events, evolutions, achievements, or super-events

Effects should fit the event story. A desperate military measure should affect units, equipment, losses, command, supply, stability, or war support. A logistical crisis should interact with trains, fuel, depots, supply, equipment, routes, or tied-down units. A legitimacy crisis should affect stability, war support, recognition, internal factions, local support, or authority. A foreign intervention system should create influence, dependence, access, backlash, or diplomatic consequences.

Normal countries still need balance, but balance must come from costs, timing, risks, limits, tradeoffs, counterplay, AI validity, and route locks. Do not create fake balance by making the numbers too small to matter.

Special chaos countries are different. They do not have to be balanced against ordinary countries. If a special chaos country finishes its path, final route, high-chaos transformation, or full mechanic loop, the payoff must be absurd, dangerous, and visibly overpowered when the concept supports it. A completed chaos country can receive extreme buffs, extreme penalties to enemies, impossible-seeming armies, unnatural production, severe combat bonuses, global pressure, map-changing powers, or other absurd effects if the route earned them.

The spec should still prevent accidental exploits for ordinary countries, repeated free rewards, and unintended cross-route stacking. It should not weaken a completed special chaos country into ordinary balance values. The absurdity must be intentional, visible, and connected to the event identity.

The spec should explain why a value is strong, weak, temporary, risky, conditional, escalating, or deliberately absurd. Reject effect plans whose main outcomes are tiny percentage modifiers, flavour-only ideas, harmless starting debuffs, invisible penalties, or rewards that the player would not notice during normal play.

## 4. What the specification should explore

A strong specification usually explores:

- the core event concept
- why the event matters
- how the event first appears
- what the player sees and chooses
- what tone the event options use, including irony, sarcasm, cultural remarks, humour, or plain severity where appropriate
- what consequences follow
- how the situation can escalate
- what rare variants can happen
- how AI countries react and choose routes
- how the event changes under different world conditions
- what decisions exist and how they interlock
- whether the event should create focus tree content
- whether the event should create new tags or transform existing countries
- what starting units and reinforcement routes new countries receive
- how each new or transformed country changes names, flags, leaders, ideologies, parties, and politics
- whether the event should use a super-event
- what achievements should exist and why they are difficult
- what UI or visual presentation would make it stronger
- what other Chaos Redux systems it should interact with
- what assets the event needs, including all route-specific country assets
- what historical flag designs and symbols need sourced references, and what portraits must be sourced rather than generated
- what the coding agent needs to know before implementation

When exploring these areas, do not stop at the first obvious answer. Consider multiple versions and choose or describe the strongest ones.

For important events, think through edge cases, country differences, country package completeness, player incentives, AI incentives, abuse risks, pacing, cooldown factors, narrative tone, repeat play, and evolved behavior.

## 5. Chaos Redux system awareness

Consider links to existing Chaos Redux systems when they strengthen the event.

Possible links include:

- Chaos Meter
- evolutions
- super-events
- world-end scenarios
- event clusters
- condemnation
- deaths
- air cleanliness
- chemical warfare
- biological warfare
- world threats
- existing or planned events

Leave out connections that feel artificial.

## 6. Escalation and uncertainty

Dangerous systems should not reveal themselves too early.

Player-facing escalation text must not label itself as a warning, a non-warning, a threat, a danger signal, or a world-ending risk. Do not tell the coding agent to write text that announces what the player is supposed to infer. Do not frame an event-detail entry, report, news item, tooltip, decision category, focus description, super-event direction, or spreadsheet-facing summary around that direct label.

Use mysterious information, fear, and uncertainty instead. Early information should feel incomplete because people cannot yet explain what is happening.

Do not build mystery from bureaucratic document motifs, archive-style secrecy, diplomatic evasions, or paperwork drama. Avoid staged contrast formulas that make tension from one side saying or seeing something while an official body denies, delays, softens, avoids, or reacts to it. Avoid timing formulas that make one observation happen before an official admission, public reaction, government response, or wider consequence. Describe the observed fear and uncertainty directly.

The player should understand deeper danger through patterns and consequences over time. It should not explain that the content is a warning or reassure the player that it is not one.

## 7. Depth and hidden connections

Look for design connections the user may not have considered.

Useful connection types can include:

- callbacks to existing events
- links to planned events
- rare unlock conditions
- alternate branches
- campaign-state dependent outcomes
- ideological interpretations
- historical parallels
- secret projects
- military exploitation
- propaganda themes
- myths or rumours
- diplomatic consequences
- internal faction disputes
- scientific uncertainty
- black market effects
- civilian behaviour
- regional differences
- long-term instability
- old movements returning under new conditions
- custom countries that only make sense in specific campaign states

Add these when they make the event stronger.

## 8. Custom UI and presentation

If the event benefits from custom UI, design one.

Describe what the player sees, how it changes, and what visual assets are needed.

Map the UI states if the UI represents pressure, route choice, threat, stage, faction cohesion, recognition, contamination, loyalty, or any other living value.

## Interactive mechanic UI and animated presentation in event specs

When an event has an important decision category, choose its presentation layer before designing a custom window. Start with an ordinary category, then test whether a static or animated category picture is enough. Use a richer scripted GUI or a separate mechanic window only when the system needs active visual management that normal decisions, tooltips, and one category picture cannot provide.

If the named event specifically introduces a dedicated scripted GUI, include a bounded `chaosx_event_ui_worker` handoff in the implementation prompt. Name the event-owned GUI identifiers, files, entry point, layout regions, states, resolutions, decisions, assets, allowed files, and handoff path. Require mandatory `hoi4.gui_inspect`, comprehensive `hoi4.gui_render`, in-scope `hoi4.gui_rewrite`, and post-change comparison evidence plus the full layout contract from `chaos-redux-decisions-missions`. Explicitly exclude the shared event log, event-details framework, settings, super-event framework, shared registries, and unrelated existing UIs.

For major events, important decision categories, custom mechanic windows, formable routes, high-chaos route reveals, active crisis meters, special leader transformations, faction boards, patron influence networks, or occult and supernatural systems, run a presentation-choice pass. The pass must choose between ordinary category presentation, a static picture, an animated picture, a compact attached display, and a full scripted GUI. Animation should be planned only when it clarifies a changing state or materially strengthens the category. Static presentation needs no defensive justification when it is the clearer option.

A mechanic UI spec should include:

- chosen presentation layer and why a simpler layer would be insufficient
- category picture direction when a static or animated picture is used
- formable state-puzzle layout and exact state-piece rules when map qualification is the mechanic
- where the UI appears, such as decision category header, attached scripted GUI, custom window, event-details panel, or country mechanic panel
- what button opens or closes the window
- what values, targets, meters, cards, lists, tabs, or map states the player sees
- what buttons the player can click and what each costs
- how unavailable buttons explain missing requirements
- what scripted effects and scripted triggers own the button logic
- how AI performs equivalent actions without relying on human-only clicks
- how the UI cleans itself up after route change, tag change, annexation, civil war, peace, or event completion
- what localisation and scripted localisation the UI needs
- what static assets, animated sprites, hover states, selected states, locked states, warning states, and progress variants it needs
- what animated state communicates, such as available action, rising pressure, critical danger, selected target, active ritual, foreign influence spread, reform momentum, hidden route reveal, route corruption, or completion
- which animation surfaces are state-driven and which are decorative
- which static fallback appears when animation is disabled, unsupported, not yet produced, or hidden by route state
- exact `chaosx_event_ui_worker` scope and MCP evidence when the named event introduces and owns the UI, plus explicit exclusions for every shared interface it merely opens or references

The spec should not make an interactive window for every small modifier. Use custom UI when it improves readability, choice, atmosphere, or management of a living system.

Animation is useful when the player needs to notice a changed state without reading a long tooltip. Use it for pressure rising, corruption spreading, a council activating, an occult meter pulsing, a patron influence network changing, a formable seal becoming available, a faction board entering crisis mode, a route emblem changing after a focus, or a warning frame appearing near failure. It should not hide information or add noise.

Do not animate a category only to make it look important. Strong static pictures are often better for propaganda, ideology, civil-war preparation, national preparedness, elections, treaties, and formable territory overviews. Animated category pictures are appropriate when the picture itself represents active mobilization, escalating crisis, a changing map state, or route transformation.

For each planned animated asset, the spec should define the in-game use, target surface, state logic, frame count expectation, loop behavior, static fallback, source mode, asset handoff owner, and proposed sprite names when they are known. The final animation must follow `chaos-redux-frame-animation`, meaning real source frames, a frame sheet, a static fallback, a preview GIF for review only, and a `.gfx` handoff. Do not describe a GIF, filter pulse, recolour loop, shifted still image, or transform-only mockup as the final game animation.

Leader portraits can have animated variants for major route reveals, high-chaos leaders, supernatural leaders, symbolic councils, final formables, or dramatic country transformations. The spec should say when the animated portrait appears, what static fallback exists, whether the portrait is sourced or generated, what state or route controls it, what removes or replaces it, and how the animation remains period-appropriate and readable at leader-portrait size.

## 9. Super-event planning

If the event needs a super-event, design the super-event as part of the event emotional and gameplay pacing.

A super-event should not be used only because something large happens. It should mark a moment that changes how the player understands the campaign, the event chain, the world state, or the stakes of the current crisis.

When planning a super-event, define:

- why this moment deserves super-event treatment
- what exact event state triggers it
- whether it is a reveal, escalation, transformation, defeat, aftermath, or world-end moment
- what the player should feel when it appears
- what the world believes has happened
- what information is still uncertain
- what image direction would fit
- what quote direction would fit
- what cultural remark direction would fit
- what audio mood would fit
- whether it needs follow-up events, decisions, or focus routes

Keep the super-event tone specific to the event. Do not make every super-event feel like the same apocalypse with a different image.

Do not fully research quotes, cultural remarks, or music inside this skill. Use `chaos-redux-super-events` for that work.

The event spec should provide enough direction for `chaos-redux-super-events` to find real quotes, meaningful cultural remarks, and suitable audio.

### Super-event text boundary and research gate

This skill is direction-only for super-event title text, `.a` button text, `.q` quote text, and any cultural reference. Do not write a final title, option, button line, quote, lyric fragment, slogan, proverb, scripture excerpt, literary allusion, or film, song, book, or game reference inside the event spec unless the exact wording has already been researched, sourced, and documented through the super-event skill or a provided source file.

If research has not been done, use neutral research gates instead of lines that could be pasted into localisation:

- `Reveal super-event title: research required`
- `Button remark: research required`
- `Main quote: research required`
- `Cultural reference: research required`

Do not include unresearched `possible line`, `sample title`, `placeholder quote`, or `temporary button text`. Implementation agents may treat those as final localisation.

Describe the desired shape instead. For example, write `short title direction about public recognition of the threat, avoiding generic apocalypse wording`, not a finished title.

Functional labels are allowed for spec structure, asset filenames, and prompt routing, but they must be neutral and explicitly non-final. Use labels such as `mainland reveal super-event`, `world-end super-event`, or `se_death_mainland_reveal`. Do not name assets, localisation keys, or prompt files after unresearched title concepts.

### Major-event defeat aftermath

Some major events should also have a structured aftermath when the threat is beaten.

Use a defeat aftermath package when all of these are true:

- the defeated threat was global or near-global in reach
- the campaign lasted long enough to feel like a world crisis
- the cost in casualties, destruction, or political disruption was high enough that the world should not simply snap back to normal

Typical aftermath content:

- a defeat super-event or defeat-stage super-event effect
- postwar treaties, compacts, or new world orders
- recurring remembrance, reconstruction, or vigilance events
- lasting ideas, tech-sharing groups, or diplomatic rules that exist because the world learned from the crisis

Do not add a treaty/new world order after every contained or short-lived disaster. Those only make sense when the event genuinely reshaped the campaign.

## 10. Writing style

For player-facing text, define the same style as direction only. Event description direction can stay grounded while option direction can use irony, sarcasm, cultural remarks, and humour that fit the actor and stakes.

Avoid:

- generic disaster wording
- empty dramatic language
- making every event apocalyptic
- random chaos without purpose
- implementation code
- excessive technical detail
- filler text that repeats obvious system behavior
- displaying event effects in event details
- long sentences without actually saying anything
- short staccato sentences that are dramatic and just make comprehension more confusing
- option direction that would lead to bland placeholder buttons
- absence notes for systems that are not present, such as saying an event has no world-end scenario or no manual triggerable scenario

Mention implementation only where it matters for the design, such as super-event treatment, custom UI, AI behavior, documentation, assets, dynamic factors, focus tree structure, custom tags, or important system connections.

This planning skill defines direction for player-facing text. It must not write final player-facing localisation. This includes event titles, event option text, event descriptions, news and report prose, decision names, decision descriptions, focus names, focus descriptions, achievement titles, achievement descriptions, GUI labels, event-detail text, spreadsheet-facing wording, super-event titles, super-event button text, super-event quotes, cultural remarks, source-like allusions, and final audio selections.

The planning spec may define tone, actor viewpoint, structure, visible information, route variation, dynamic placeholders that final text should use, and research needs. If a working label is needed for a row, filename, prompt, branch, route, asset, diagram, or internal handoff, mark it clearly as `working label, not final localisation`.

Important super-event boundary: this planning skill may define super-event role, trigger, tone, image direction, quote direction, cultural-remark direction, and audio mood. Any source-dependent wording belongs to `chaos-redux-super-events` and must stay blocked until researched and documented.

### General text writing style

1. Never use the em dash or semicolons in sentences.
2. Absolutely avoid dialectical hedging. Do not frame sentences as thesis, antithesis, synthesis.
  - Dialectical hedging examples:
    - `The invasion is not merely a border crisis, but a crisis of identity.`
    - `The regime is not only losing the war, it is losing itself.`
    - `This is not just a strike. This is a warning.`
    - `The cult is not fighting for land, but for meaning.`
    - `The disaster is both a local tragedy and a global sign.`
    - `The government is neither dead nor alive, but something worse.`
    - `The army did not collapse. It transformed.`
    - `This is less a rebellion than a confession.`
    - `The question is not whether order can return, but what kind of order will survive.`
    - `What looks like defeat is actually a new form of power.`
  - Thesis, antithesis, synthesis examples:
    - `The army claims the province is secure. Refugees say it is already lost. The truth lies between them.`
    - `Some call the new state liberation. Others call it occupation. In reality, it is both.`
    - `The priests call it a miracle. The generals call it a weapon. History will call it both.`
    - `The committee promises order. The opposition sees tyranny. The new system contains both impulses.`
    - `The papers call it a victory. The hospitals call it a defeat. The country has become both at once.`
    - `The rebels ask for justice. The regime asks for peace. The settlement gives neither and both.`
3. Avoid AI-style explanatory templates. Do not write lines that sound prebuilt or reusable across any event.
4. Absolutely avoid staccato sentences. Do not split one simple thought into a chain of tiny lines for artificial weight or dramatic effect. Use complete, readable sentences with enough context to be clear.
  - Staccato examples:
    - `The radios died. The roads emptied. The city listened.`
    - `No orders. No mercy. No dawn.`
    - `The border fell. Then the capital. Then the government.`
    - `They marched. They burned. They vanished.`
    - `A knock at the door. A list on the table. A train in the dark.`
    - `The guns stopped. The screaming did not.`
    - `First hunger. Then anger. Then flags.`
    - `No king. No cabinet. No law.`
    - `Ash in the streets. Smoke over the port. Silence at noon.`
    - `One order. One shot. One missing officer.`
    - `The gate opened. The crowd moved. The guards ran.`
5. Avoid staged contrast formulas. Do not write sentences or paired clauses built as `claim X while officials Y`, `reports say X while authorities Y`, `people do X before governments Y`, `X happens before Y admits it`, or similar. Do not manufacture tension by contrasting unofficial fear with official denial, silence, delay, admission, or reaction. Write the observed fear, behaviour, rumours, anomalies, and consequences directly.
6. Absolutely avoid empty dramatic filler. Do not lean on vague intensity words when concrete detail would do the work.
7. Do not paste instruction text, task labels, prompt fragments, or process notes into in-game text, specs, docs, localisation, spreadsheet fields, or reports.
  - For example, when I say: `Do not reveal the hidden mechanics here.`, don't write `This path purposely doesn't reveal the hidden mechanics`

## 11. Specification shape

Do not force the specification into a fixed template.

Choose the structure that best fits the event idea.

The specification should still be easy for a coding agent to use. Use clear headings, explain the logic in a natural order, and make sure important design decisions are not buried.

For major events, split the spec into parts if needed. Do not compress deep design just to fit one file.

Only include sections for surfaces that exist or that need design. If a world-end scenario, manual triggerable scenario, super-event, focus tree, custom country, achievement set, or asset family is absent, omit that section instead of writing that it is absent. Because negative notes create noise and can mislead later agents into thinking the absence is a designed feature.

## 12. Depth, file splitting, and continuation prompts

Do not compress the spec so much that important ideas become shallow.

The goal is depth, not speed.

Think through the event as far as the idea can reasonably go. If the event has multiple branches, evolutions, rare variants, custom countries, focus trees, UI elements, super-events, or major system connections, treat each of those as deserving real design space.

Large events should be written across multiple spec files and multiple chat responses when needed. Split at clean design boundaries such as core loop, evolutions, focus trees, decisions, country packages, assets, super-events, achievements, AI, research, or acceptance criteria.

Each part and file should be complete enough to be useful on its own. Stop at a clean section or subsection boundary when possible. If a large surface must continue, stop after a complete paragraph, table, route, country package, or list item instead of cutting a thought in half.

Do not summarize later sections because the current response is getting long. Continue in another part and save that part as another specification file for the final package. Use the available response space for real specification content.

### Temporary continuation prompt

When a large event specification cannot fit into one response, end the current part with a temporary continuation prompt for the next iteration. This prompt is a working chat handoff. It is not part of the final specification, downloadable package, event docs, prompt files, or repository source.

The continuation prompt should be concise and precise. It should include:

- the event id, event name, event slug, and current part number when known
- the exact section and subsection where the previous part stopped
- the last completed heading, route, table, country package, or file
- the next file, heading, table, route, country package, decision family, asset group, research task, or prompt file to write
- the files already completed or updated
- constraints that must continue to apply, including direction-only localisation, country naming rules, source rules, tag collision rules, animation rules, and the user's core event idea
- unresolved research needs, blockers, and accepted assumptions
- a reminder to continue with full-depth design and not summarize missing sections
- a reminder to avoid repeating completed sections except for the short context required to continue cleanly

Use the heading `Temporary continuation prompt, not part of the spec`. Keep it outside saved specification content. Every later part must create an updated prompt that reflects the new stopping point. Do not reuse an older prompt after the design has moved forward.

When the final part is complete, do not write another continuation prompt. Provide the completed package and completion summary.

### Optional resume packet

For very large work, compaction, interruption, or handoff to another agent, a separate `resume_packet.md` may be created as a working file. It belongs under `docs/plans/<event_id>_<event_slug>_plans/` after extraction, not inside the source specification files.

A resume packet should include:

- event id, event slug, and intended source spec folder
- files already written or updated
- exact section, subsection, route, table, or country package where work stopped
- next file, heading, route, decision family, country package, asset group, research brief, or prompt file to write
- constraints that must continue to apply
- unresolved research needs, blockers, and accepted assumptions
- a reminder to continue with full-depth design and avoid repeating completed sections

A resume packet may remain in a plan-only package when it is useful for later work. Temporary continuation prompts must never remain in the final source spec package.

For major events, the final combined specification may be extremely long. A 10,000 line, 50,000 line, or 100,000+ line specification is valid when the event needs that detail. Do not compress focus trees, rare variants, or decision webs into summaries to keep the package short.

Avoid filler. Every section should add useful design, player-facing detail, implementation clarity, asset direction, research evidence, or system connection.

Before saving the final files, run a cleanup pass. Remove generic safeguards, obvious implementation boilerplate, empty labels, repeated wording, admin audit sections, temporary continuation prompts, and temporary compaction notes that do not belong in the final package.

## 13. Asset planning

The event specification should identify all important visual assets. For major events, assume every visible system needs asset planning unless the spec explicitly explains why it does not.

Consider whether the event needs:

- idea icons
- national spirit icons
- focus icons for every focus or focus-family in each mapped tree
- decision category icons
- static and animated decision category pictures for categories that need visual identity or territorial context
- exact formable state-puzzle pieces and composed territory previews when dynamic state qualification is central
- decision icons
- achievement icons
- news event pictures
- report event pictures
- super-event images
- leader portraits
- council, committee, regency, cult, junta, or symbolic leadership portraits
- faction emblems
- flags for every new country, modified country identity, ideology variant, focus-route variant, puppet identity, and major cosmetic transformation
- UI
- animated decision category seals, mechanic-window elements, warning pulses, route emblems, hover loops, selected states, glow loops, float loops, particle loops, and animated leader portraits when motion clarifies the mechanic
- progression-state variants
- static fallbacks for every animated UI piece, route emblem, icon, or portrait
- country-selection, event-log, or custom-window graphics when relevant

Asset generation, sourcing, cropping, resizing, DDS conversion, file placement, sprite handoff notes, and manifests belong to `chaos-redux-event-assets`. Animated frame planning and frame-sheet handoff requirements belong to `chaos-redux-frame-animation`. Final `.gfx` wiring belongs to the main implementation agent unless a parent prompt explicitly grants that scope.

This skill should define what assets are needed, what they should represent, what source mode they require, and which visible states, if any, benefit from animation. Static presentation is valid whenever it communicates the mechanic more clearly. Do not require animation only because a mechanic is important.

Historical or real-world assets need special care. Historical flags and symbols require reliable cited design references, and every final flag still uses imagegen as a reference-constrained flat reconstruction. `chaosx_portrait_creator` owns sourced photographs, explicit head-and-shoulders crops, placeholders, and user-supplied HOI4-style finals for real leaders. Grounded polities must use sourced real subjects or authentic institutional material even when their route is alternate history. The portrait worker generates one-person portraits only for wholly fictional leaders of wholly fictional high-chaos polities. Generated non-portrait art remains appropriate for people-free symbolic councils, invented high-chaos identities, idea icons, focus icons, decision icons, achievements, faction emblems, UI art, and fictional or alternate-history report, news, and super-event images unless the user says otherwise.

### Reference examples for asset planning

When a spec or asset prompt asks for generated or sourced assets, tell the asset agent to inspect the matching reference examples before creating anything.

Use this single canonical reference root:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

The catalog and every category below are relative to that exact folder:

```text
CATALOG.md
icons
event_art
flags
portraits
units
event_art/super_event
icons/achievements
```

Reference mapping:

- idea and national spirit icons: `icons/ideas/`
- news event images: `event_art/news/`
- report event images: `event_art/report/`
- super-event images: supplemental `event_art/super_event/` plus the live Chaos Redux super-event UI
- technology icons: `icons/technologies/`
- special-project icons: `icons/special_projects/`
- achievement states: `icons/achievements/`. The reusable not-eligible overlay is `icons/achievements/overlay.png`
- decisions and missions: their separate folders under `icons/`
- decision category icons: `icons/decision_categories/`
- decision category pictures: `icons/decision_categories/pictures/`
- flags: the complete normal, medium, and small ladder under `flags/`
- focus icons: `icons/national_focus/`
- officer corps spirits and balance-of-power icons: their separate folders under `icons/`
- leader portraits: `portraits/leaders/`
- 2D equipment, two-frame unit counters, and 3D material references: their separate pipelines under `units/`
- other matching categories when needed

The decision category picture family is a separate reference surface. Its exact path is:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\icons\decision_categories\pictures`

The implementation or asset prompt must require `contact_sheet.png` in that folder. If it is missing, the asset agent should build it from the references, label filenames and native dimensions, and update `assets/vanilla_reference/README.md` and `assets/vanilla_reference/CATALOG.md` before producing new category pictures.

The event spec does not need to analyze those images itself. It should make the handoff explicit so the asset agent knows which example set to inspect before generation, sourcing, cropping, or wiring.

## 14. Asset prompt handoff

After the full event specification is complete, create a separate asset prompt file for `chaos-redux-event-assets`.

The asset prompt should include:

- required assets
- visual style
- symbols and motifs
- target sizes
- intended in-game use
- country package asset coverage, including base flags, ideology flags, focus-route flags, cosmetic flags, leaders, portraits, and faction emblems
- suggested filenames
- suggested sprite names
- suggested static fallback sprite names and animated sprite names when animation is planned
- whether each asset is for an event, report event, news event, super-event, decision, idea, focus, achievement, flag, leader portrait, faction emblem, or UI element
- animation brief needs for every animated asset, including state logic, frame count target, target frame size, expected sheet size, frames per second, loop behavior, `play_on_show` expectation, static fallback, source mode, and target `.gfx` or `.gui` surface when known
- achievement icon list with completed icon directions for every achievement
- manifest requirements
- source mode, including whether a flag, symbol, or portrait must be sourced historically instead of generated
- reference example folder that must be inspected before asset work
- decision category picture list, source mode, presentation role, static or animated state, and exact reference folder when category pictures are planned
- formable state-puzzle manifest needs, exact state geometry source, grey and green qualification states, projection, sprite ownership, and static category-picture alternative when formables are planned
- instruction to create the decision category picture reference contact sheet and catalog entries when the canonical sheet is missing

The asset prompt must state the correct source mode where relevant.

It must also state the relevant reference folder from the list above when a matching folder exists.

Use `chaos-redux-event-assets` rules for source selection. Symbolic icons usually use `$imagegen`. News event images, report event images, and super-event images may be sourced or generated. Prefer generated assets for fictional, alternate-history, symbolic, high-chaos, or unique scenes, and sourced assets for photographed events and archival artifacts. Every flag uses `$imagegen`. Historical flags first require a cited design reference and must remain flat, faithful reconstructions. Route all portrait prompts to `chaosx_portrait_creator`; name the leader and advisor reference folders, require an explicit head-and-shoulders crop and identity preservation for grounded subjects, and request separate `156x210` leader and `65x67` advisor outputs when both uses exist.

Do not make the asset prompt vague. If a country has multiple cosmetic identities, ideology names, focus-route transformations, or leader changes, the asset prompt must list the required assets for each visible identity state. Use animation only when the state change benefits from motion. A completed formable or living mechanic may use a strong static category picture, an animated picture, a compact state-puzzle display, or a full window according to the presentation-choice pass.

## 15. HOI4 asset size reference

Use these sizes when planning assets:

- report event images: 210x176
- news event images: 397x153, black and white
- leader portraits: 156x210
- flags small: 10x7
- flags medium: 41x26
- flags normal: 82x52
- tech icons small: 64x64
- tech icons medium: 132x52
- achievements: 64x64
- super-event images: 457x328
- decision icons: 32x32
- idea and national spirit icons: 64x64
- focus icons: 94x86

Use other sizes when the event UI or asset type requires it.

## 16. Asset style reference

When planning visuals, use these style expectations.

Report and news event images should look like documentary photographs, whether sourced or generated. News event images should be black and white.

Super-event images should have a strong central composition, clear dramatic theme, readable subject, and enough contrast for HOI4 UI.

Focus icons should look like HOI4 focus icons, with a central symbol, readable silhouette, aged texture, painterly detail, and strong contrast.

Idea and national spirit icons should look like compact HOI4 icon art. They need strong symbolic shapes and clear readability at 64x64. They are similar to focus icons, but they are missing the main frame.

Achievement icons should be readable at 64x64 and have a clear completion theme. The completed version is generated first. Grey and not-eligible variants can be produced later.

Flags should use clean symbols that remain readable at HOI4 flag sizes.

Progression-state variants may include selected, dim, active, locked, completed, rejected, damaged, corrupted, urgent, meter-fill, and bar-fill states.

## 17. Super-event research handoff

If the event has one or more super-events, create a separate super-event prompt file for `chaos-redux-super-events`.

The prompt should ask that skill to research or create the full super-event presentation package.

For each super-event, include:

- super-event purpose
- trigger moment
- tone
- title direction, not a final title unless researched and sourced
- description direction
- quote direction, not quote text unless researched and sourced
- cultural remark direction, not final button text unless researched and sourced
- audio mood, not a final track unless researched and licensed
- image direction
- whether it is a normal escalation, defeat moment, aftermath moment, or world-end moment
- any special constraints from the event spec

The `chaos-redux-super-events` prompt should ask the agent to:

- find a real quote using the repository web research workflow from `AGENTS.md`
- verify quote wording and attribution
- find a meaningful cultural remark, reference, allusion, or short line where appropriate
- follow copyright limits for songs, films, books, and other protected works
- find suitable public domain or clearly licensed audio
- document all sources, license notes, and uncertainties
- coordinate super-event image needs with `chaos-redux-event-assets`

Do not claim a quote, cultural reference, or audio track is usable without checking.

If a license or attribution is unclear, mark it as uncertain.

The super-event prompt must explicitly state that unresearched titles, button text, quotes, cultural remarks, slogans, lyric fragments, allusions, and audio choices are blockers. The implementation agent must not convert research directions, working labels, achievement names, asset names, or draft-like wording into final super-event localisation.

## Improvement-loop expansion specs

When `chaos-redux-improvement-loop` produces an expansion addendum, treat it as event-planning input. The addendum should be folded into the main spec pack with the same seriousness as the original user idea. Do not treat it as a loose suggestion if the parent accepted it.

An improvement-derived spec can be shaped freely. It does not need to copy the section order of this skill. It should still make the design concrete. A useful addendum explains the playable promise, the route or mechanic that feels shallow, the deeper player loop, the choices that change outcomes, the AI behavior, the visual and localisation needs, and the surfaces that must align.

### Mandatory near-completion improvement loop pass

Before any event-planning goal is treated as near complete, the coding agent must spawn `chaosx_improvement_loop_planner` for a final depth and anti-bloat pass. This is mandatory for event specs, large addenda, country packages, focus-tree plans, decision systems, super-event planning, asset-heavy plans, formable plans, custom UI plans, and any goal that creates or changes meaningful Chaos Redux design.

Run this pass after the main design is mostly assembled and before the final completion report. The loop planner should inspect the current spec, accepted plans, unresolved handoffs, asset needs, AI plans, mechanic surfaces, and implementation handoff needs. Its job is to find remaining shallow systems, disconnected mechanics, missing route depth, missing AI behavior, missing asset states, missing aftermath, or scope bloat.

Spawn the loop planner with `fork_context=false`. The parent prompt must explicitly pass the event id, event slug, current goal, user constraints, current spec paths, relevant plan paths, known unresolved decisions, and the exact question to answer. Do not rely on inherited conversation context.

The loop planner may return either an expansion addendum or a closure handoff. If it returns an expansion addendum, the parent must resolve it before completion by folding accepted content into `docs/specs/<event_id>_<event_slug>_specs/`, implementing or queuing it with a clear reason, or rejecting it with a clear reason. If it returns a closure handoff, record that closure and proceed with final checks.

A goal is not complete while an accepted loop addendum is unresolved, while a loop-recommended closure handoff has not been recorded, or while the mandatory loop pass was skipped without a tooling blocker. If the loop agent cannot be spawned because the tool is unavailable, the completion report must state that as a blocker and must not hide it as finished work.

Tiny known-file text edits, narrow typo fixes, and direct one-line skill updates can skip the loop pass only when they do not create or change event design, mechanics, focus trees, decisions, country packages, assets, super-events, or implementation handoff rules.

## General localisation handoff

When a spec includes text-bearing content, give a localisation handoff, not final copy.

The handoff should list each needed text surface and describe its direction:

- event title direction
- event description direction
- option reaction direction
- news or report direction
- decision name and description direction
- focus name and description direction
- achievement title and description direction
- GUI label direction
- event-detail and event-log wording direction
- dynamic placeholders the coding agent should use
- research gates for quotes, slogans, songs, films, books, speeches, scriptures, proverbs, or other source-dependent references

The coding agent writes the final in-game text during implementation. The planning spec should not provide final prose for the coding agent to paste.

The planning agent should preserve the open structure of the addendum where that helps the idea. Use tables, route maps, prose, diagrams, or country package matrices only when they make the design easier to implement. Do not convert every improvement into a rigid checklist.

When an improvement addendum proposes formables, scripted GUI, animated sprites, animated portraits, or hidden routes, the final spec pack should carry those ideas into the relevant files instead of leaving them isolated. The core spec explains why the expansion matters. The decision and focus files explain how the player reaches it. The asset prompt explains the static and animated visual work. The coding prompt and goal prompt tell the implementation agent to wire and validate it.


## Specification folder convention

From now on, event source specifications should live in event-specific subfolders under `docs/specs/`.

Use this shape:

```text
docs/specs/<event_id>_<event_slug>_specs/
```

Examples:

```text
docs/specs/006_independence_wave_specs/006_independence_wave_spec.md
docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md
docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md
```

Use `docs/plans/<event_id>_<event_slug>_plans/` for subagent plans, improvement addenda, audit follow-up notes, blocked reports, and implementation handoffs. Plans can become source design later, but the main agent should promote or merge them into `docs/specs/` when they are accepted as part of the final event design.

## 18. Output rules

The event specification itself should be created as Markdown files.

Full event specification output belongs under `docs/specs/<event_id>_<event_slug>_specs/`. This is the source-of-truth design folder for the event spec pack.

Subagent planning addenda, audit follow-up plans, implementation notes, and temporary handoffs belong under `docs/plans/<event_id>_<event_slug>_plans/`. The plans folder is a working area. Accepted plan content should be folded into the relevant spec under `docs/specs/` when the final source-of-truth spec is updated.

Do not create new event specs, addenda, prompt packages, or extracted handoffs under `docs/planning/`, `planning/`, or any other planning folder. If a prompt says "planning folder", interpret that as `docs/plans/` for subagent plans and `docs/specs/` for source specs unless the user explicitly provides a different path.

The spec file should contain only the event specification.

Do not put the asset prompt, super-event prompt, coding-agent prompt, or goal prompt inside the spec file.

Keep planning files readable as design handoffs, not implementation blueprints. Prefer route purpose, player-facing behavior, balance intent, asset direction, AI intent, and acceptance criteria. Avoid long technical tables, exact constant lists, full scripted-effect recipes, exhaustive file inventories, parser-level implementation notes, and detailed code wiring. The specs you create are not implementation oriented. You do not give implementation guidance, you are just handing off ideas.

Create sequential files:

- `<event_id>_<event_slug>_spec_part_1_core.md`
- `<event_id>_<event_slug>_spec_part_2_<theme>.md`
- `<event_id>_<event_slug>_spec_part_3_<theme>.md`
- and more as needed

Do not repeat earlier sections unless needed for clarity.


## 18.1 Final ZIP package requirement

The final chat-facing output must be delivered as one ZIP file containing every necessary file for the planning handoff. Individual files may also be linked for convenience, but the ZIP is the main deliverable.

The ZIP should include, when relevant:

- all specification Markdown files
- focus-tree path specification parts
- route diagrams or focus-tree sketches
- the asset prompt
- the super-event research prompt
- the achievement prompt
- the decision and mission prompt
- the coding-agent prompt
- the goal prompt
- research notes and bibliography files
- country package matrices, AI matrices, probability scenario matrices, decision maps, technology graph notes, 3D model briefs, and acceptance criteria created separately
- an optional resume packet for plan-only or interrupted work

Do not include temporary chat continuation prompts in the ZIP.

Use a clear package name such as:

`<event_id>_<event_slug>_planning_package.zip`

The ZIP should be directly extractable into the repository. For a completed source-spec package, use one top-level folder named:

```text
<event_id>_<event_slug>_specs/
```

That folder is intended for `docs/specs/`. Use descriptive repo-ready filenames inside it, for example:

```text
<event_id>_<event_slug>_spec_part_1_core.md
<event_id>_<event_slug>_spec_part_2_<theme>.md
<event_id>_<event_slug>_asset_prompt.md
<event_id>_<event_slug>_super_event_prompt.md
<event_id>_<event_slug>_achievement_prompt.md
<event_id>_<event_slug>_decision_mission_prompt.md
<event_id>_<event_slug>_coding_prompt.md
<event_id>_<event_slug>_goal_prompt.md
```

Use a top-level `<event_id>_<event_slug>_plans/` folder only when the ZIP contains subagent plans, follow-up handoffs, audits, blocked reports, or resume packets rather than the accepted source spec.

Do not force generic packaging-only folders such as `specs/`, `prompts/`, `research/`, or `matrices/` when descriptive repo-ready files in the event folder are clearer. Subfolders are allowed when a very large package genuinely benefits from them.

The goal prompt inside the package should be between 3500 and 4000 characters when the task needs that detail, and it must never exceed 4000 characters.

## 19. Final prompt files

Only after the full specification is complete, create separate prompt files outside the spec file and include them in the final ZIP package.

Required prompt files:

- `<event_id>_<event_slug>_asset_prompt.md`
- `<event_id>_<event_slug>_super_event_prompt.md` when the event has one or more super-events
- `<event_id>_<event_slug>_achievement_prompt.md`
- `<event_id>_<event_slug>_decision_mission_prompt.md` when the event has large decision or mission systems
- `<event_id>_<event_slug>_coding_prompt.md`
- `<event_id>_<event_slug>_goal_prompt.md`

The final answer should point to the final ZIP package as the deliverable and briefly summarize what the package contains.

### Asset prompt file

Create an asset prompt for `chaos-redux-event-assets`.

The prompt should cover all required visual assets, progression-state variants, final asset packaging, reference folders, source modes, and manifest requirements.

### Super-event prompt file

Create a super-event prompt for `chaos-redux-super-events` if the event has one or more super-events.

The prompt should cover title direction, description direction, quote research, cultural remark research, audio research, image direction, source documentation, licensing notes, and coordination with asset work.

The prompt must not provide unresearched final titles, button text, quotes, slogans, lyric fragments, cultural references, or final audio choices. Use research gates and role labels instead. It must tell the super-event researcher to produce the final text package only after source checks.

### Achievement prompt file

Create a separate achievement prompt file for the coding and asset agents.

The achievement prompt must include every planned achievement with id, title direction or working label, description direction, eligible countries, unlock conditions, disqualifiers, difficulty, hidden or visible status, why it is not trivial, icon direction, and all required tracking notes.

The achievement prompt should tell the implementation agent to inspect existing achievement patterns, implement the achievements, wire localisation and icons, create any required tracking flags or variables, document them, and avoid easy unlocks.

### Coding-agent prompt file

Create a coding-agent implementation prompt that summarizes the finished event spec.

The prompt must tell the coding agent to:

- implement the event according to the spec
- implement all mapped decisions, variants, evolutions, focus trees, custom tags, country packages, achievements, assets, and super-events included in the spec
- implement the mapped cost and sacrifice model, avoiding boring political power or command power only decisions when the spec calls for XP, equipment, manpower, stability, war support, fuel, supply, units, local support, foreign access, or other concrete costs
- implement focus trees according to the path design, with coherent non-linear branches, route locks, side paths, convergence nodes, hidden routes, focus filter tags or search categories, varied reward types, proper icons, final localisation written from the spec direction, AI behavior, event integration, and no filler shortcuts
- implement any planned focus inlay window through `chaos-redux-focus-trees`, reserve its space in the tree layout, and keep it clear of focuses and tree controls
- create the final exact focus layout and connections cleanly in implementation while preserving the spec's path logic
- implement every country package from the spec, including tag, history, names, cosmetic names, ideology names, ruling parties, leaders, leader changes, flags, route-specific identity changes, starting divisions, dynamic unit packages, force-growth decisions and focuses, volunteer routes, decisions, ideas, AI behavior, localisation, assets, and docs
- implement the full AI strategy matrix from the spec, including route preferences, foreign influence behavior, focus choices, unit-raising choices, decision choices, faction behavior, and high-chaos exceptions
- perform the full vanilla, Chaos Redux, Workshop, and local-mod tag collision audit before creating a new country tag, reuse existing vanilla identities when they already exist, and preserve living vanilla countries and meaningful existing trees
- use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` when technologies, doctrines, folders, prerequisites, unlocks, grants, or research bonuses are involved
- spawn `chaosx_ai_probability_auditor` and use the probability inspection, evaluation, sweep, comparison, rendering, simulation, and sequence tools according to the scenario plan when weighted behavior is involved
- route required 3D model and skeletal animation production through `chaosx_3d_model_pipeline` with `fork_context=false`, then implement and validate the final `.asset`, entity, `.gfx`, unit or building consumer, placement, animation, and live in-game evidence
- follow the flat reference-constrained imagegen rule for every flag and the sourced identity-preserving portrait rule for every grounded polity and real person
- follow `AGENTS.md`
- follow `chaos-redux-events`
- use `chaos-redux-event-assets` if visual assets are required
- use `chaos-redux-super-events` if super-events are required
- write final player-facing event, decision, focus, achievement, GUI, event-detail, and spreadsheet-facing localisation from the direction in the spec. Do not expect the planning spec to provide finished copy
- treat unresearched super-event titles, button text, quotes, cultural remarks, slogans, allusions, and audio choices as blockers, not as implementation-ready localisation
- keep all Chaos Redux systems aligned
- report anything that cannot be implemented cleanly
- keep iterating until the full spec is implemented to its fullest extent
- spawn `chaosx_improvement_loop_planner` with `fork_context=false` before claiming the goal is near complete, then resolve its addendum or closure handoff before final completion
- avoid fallbacks, simplifications, temporary versions, and good-enough approximations
- not claim completion until the implemented files satisfy the spec

### Goal prompt file

Create a separate `/goal` prompt file.

The goal prompt should be between 3500 and 4000 characters when the task needs that detail, and it must never exceed 4000 characters.

The goal prompt should not contain the whole spec or all long instructions. It should point to the spec files and the other prompt files, then state the most important pass or fail requirements.

The goal prompt must tell the implementation agent to keep iterating until the goal is accomplished to its fullest extent. It must also say not to claim completion until the implemented files satisfy the spec.

A good goal prompt should include:

- the spec folder and specification file paths
- the coding prompt file path
- the asset prompt file path
- the super-event prompt file path when relevant
- the achievement prompt file path
- the required skills or docs to follow
- the top design non-negotiables
- the requirement to create all required static and animated assets, static fallbacks, tags, starting divisions, reinforcement pathways, non-linear focus trees based on the mapped paths, focus filter tags, decisions, evolutions, achievements, and docs
- the requirement to research and source final super-event titles, button text, quotes, cultural remarks, and audio through the proper super-event workflow when super-events exist
- the requirement to spawn `chaosx_improvement_loop_planner` near completion and resolve its addendum or closure handoff before claiming completion
- the requirement to audit all installed tag sources before adding custom tags and to reuse existing vanilla identities when applicable
- the requirement to use the technology graph tools when technology content exists
- the requirement to spawn `chaosx_ai_probability_auditor` and use the probability tool workflow when weighted behavior exists
- the requirement to route and validate 3D model or skeletal animation work through `chaosx_3d_model_pipeline` when relevant
- the requirement to provide a concrete completion report

If the goal prompt is near 4000 characters, shorten it by pointing to files instead of repeating details.

## Formation and UI questions for planning passes

Before finishing a major event spec, ask:

- Can any country created or empowered by the event form a larger state later?
- Are there regional, ideological, hidden, or high-chaos formables that should be locked behind focuses, decisions, or events?
- Does each formable have concrete map requirements and a clear post-formation identity?
- Do formation rewards avoid free core spam, free war-goal spam, and instant runaway snowballing?
- Which presentation layer should each category use: ordinary category, static picture, animated picture, compact display, or full scripted GUI?
- Would a static or animated category picture communicate the category more clearly than a complex custom window?
- If exact state control is central to a formable, does the plan use exact state shapes as grey and green dynamic puzzle pieces and keep them synchronized with real eligibility?
- If the named event introduces a full UI, does the plan route only the event-owned window to `chaosx_event_ui_worker` with exact identifiers and mandatory MCP before-and-after evidence while excluding shared interfaces?
- Are animated sprites, leader portraits, particles, glow, warning states, selected states, or button states planned only where motion makes a changing state clearer?
- Does the asset prompt include category pictures, formable state pieces, sprite names, state logic, static fallbacks, and frame-sheet needs where animation is actually used?
- Does the goal prompt tell the implementation agent to verify formables, category pictures, state-puzzle eligibility, justified UI windows, and any animated sprite handoffs?

## 20. Final response checklist

The final response should include:

- the final ZIP package and a downloadable link
- the event id, slug, intended extraction folder, and package filename
- the specification files created
- the asset prompt, coding-agent prompt, goal prompt, achievement prompt, decision and mission prompt, and super-event prompt paths when relevant
- the authoritative workbook row or export-only CSV snapshot used when applicable
- repo context inspected
- event cluster role defined when relevant
- assets defined when needed, including country identity assets
- a presentation-choice pass for important decision categories, custom UI, formables, route reveals, high-chaos states, and major leader transformations
- static or animated category picture needs mapped where a picture is clearer than a full GUI
- formable state-puzzle requirements mapped with exact state shapes, dynamic qualification, static alternative, reusable templates, and eligibility agreement where relevant
- animated sprite and portrait needs mapped with static fallbacks, state logic, and `chaos-redux-frame-animation` handoff expectations only when motion is useful
- historical flags, symbols, and real leader portraits assigned the correct source workflow
- every flag assigned the flat reference-constrained imagegen workflow
- tag collision audit requirements mapped for new or reused country identities
- super-event direction and research gates defined when needed
- direction-only localisation handoff for event titles, options, descriptions, decisions, focuses, achievements, GUI labels, event details, and spreadsheet wording
- no unresearched super-event title, button text, quote, cultural remark, slogan, lyric fragment, allusion, or audio choice presented as final localisation
- country package matrices for new or modified countries when relevant
- starting force and reinforcement pathway plans for new or transformed fighting countries
- voice and Internet-sourced sound design plans plus bespoke vanilla-green counter plans for every new custom unit family
- relevance-gated country setup covering capitals and settlement renames, optional institutions and characters, navy and air when relevant, starting research, economy, stockpiles, laws, subject status, equipment identity, and DLC compatibility
- AI strategy matrices for major events or country-creation events
- weighted-behavior scenario matrices, `chaosx_ai_probability_auditor` routing, and probability-tool instructions when relevant
- technology graph placement and tool instructions when technology content exists
- 3D model and skeletal animation planning, vanilla scale references, Meshy reference requirements, pipeline routing, and live validation requirements when relevant
- clear focus-tree path maps, non-linear architecture, anchor focuses, mutual exclusions, convergence, hidden routes, crisis branches, late-game paths, filters, reward diversity, and idea lifecycle audits when relevant
- decisions, rare variants, evolutions, achievements, route identities, leader changes, flags, and unit-generation systems mapped when they exist
- varied costs, risks, requirements, and sacrifices instead of default political power or command power purchases
- uncertainties and blockers stated clearly
- strong enough effects for the intended role
- `chaosx_improvement_loop_planner` spawned near completion, with its addendum resolved or closure handoff recorded
- temporary continuation prompts removed from every final package file
- a brief package summary that does not repeat the full specification

## 21. Cleanup and quality gate

Before saving the final files, perform a strict review.

Reject the draft if it has any of these problems:

- vague placeholder decisions
- vague rare variants
- vague country paths
- custom tags without full country identity, assets, politics, leaders, flags, AI, and content expectations
- new or modified countries without country package matrices when they matter
- fixed or bounded countries whose territorial identity needs a capital and backup-capital plan but has none
- dynamic countries whose premise selects or renames a city but does not define how a valid capital, backup capital, and naming pool are chosen
- culture-changing routes that leave relevant city, victory-point, port, or regional names unchanged without a clear reason
- intelligence agencies, MIOs, advisors, theorists, high command, scientists, or operatives added only to fill a roster instead of supporting identity or gameplay
- countries whose naval or air role matters but whose starting forces, bases, variants, commanders, production, reinforcement, and AI behavior are not planned
- persistent playable countries without exact or dynamically derived starting research slots, technologies, economy, production, stockpiles, laws, subject status, and equipment identity
- events that cannot start, progress, finish, clean up, or remain balanced with no DLC or with a relevant DLC missing
- newly appearing crisis countries without dynamic starting unit packages or a clear reason why they start without troops
- country-created crisis specs without decisions, focuses, objectives, depots, volunteers, or faction systems that let those countries gain more units later
- new fighting countries without starting force plans, dynamic unit scaling, or reinforcement pathways
- new military country archetypes whose armies use only renamed vanilla division templates without an explicit unit-type assessment and a concrete mechanical and visual justification
- new custom unit families without a voice and Internet-sourced sound design pass, runtime sound roles, licensing/provenance direction, synchronization needs, bespoke counters for every consumer, exact installed-vanilla counter inspection, sampled vanilla green evidence, and icon-artist handoff
- long-lived new countries without dynamically scaled starting units or credible reinforcement routes
- newly appearing or transformed countries without mapped starting divisions, unit templates, equipment/manpower assumptions, and dynamic scaling factors
- countries with no designed way to gain, improve, convert, or coordinate more units through focuses, decisions, objectives, volunteers, depots, or faction mechanics
- generic repeated unit focuses or unit decisions that hand out identical divisions without story, route identity, or conditional requirements
- historical countries or movements with invented flag designs, uncited references, or unverified flat reconstructions
- real historical leaders planned as generated portraits instead of sourced portraits
- playable countries without clear focus-tree path maps
- focus tree sections that list only branch names without explaining path logic, mutual exclusions, rewards, and connections
- focus tree plans that give only vague samples without enough path detail for implementation
- focus trees where most focuses grant a new idea or national spirit without a clear reason
- focus trees with repeated new ideas where modifying or upgrading an existing idea would be better
- focus trees without an idea audit when many ideas or national spirits are used
- focus rewards that are mostly political power, stability, war support, or repeated flat modifiers
- focus trees missing varied reward types such as factories, forts, anti-air, airbases, railways, supply hubs, units, decisions, missions, advisors, leaders, identities, claims, or diplomacy where those rewards would fit
- major focus paths without focus filter categories or search categories
- major focus trees without a focus filter taxonomy or path category table
- major countries without separate political, military, industry, diplomacy, and expansion or special-mechanic sections when those sections fit the country
- focus trees that are too small, generic, linear, or boring for the country role
- focus trees missing distinct political, industry, and expansion branches
- important country trees with isolated branches that do not affect each other
- major branches without clear payoff
- political branches that do not change politics, leaders, advisors, parties, laws, names, flags, or country identity where relevant
- industry branches that do not change the map, production, logistics, construction, or resources
- expansion branches that do not create claims, cores, war goals, leagues, protectorates, settlement decisions, or external diplomacy
- expansion routes without postwar handling
- industry routes without geographic grounding where relevant
- major routes without route-specific AI behavior or localisation tone
- large events without a special mechanic or clear reason for not needing one
- special mechanics without clearly named values
- mechanic values without dynamic focus, decision, mission, event, war, state-control, foreign-influence, or AI hooks
- important mechanic values without consistent colour identity or readable breakdowns
- focus trees or decision systems disconnected from the mechanic values they should affect
- event-created factions without goals, rules, membership logic, shared decisions, AI behavior, rewards, or success and failure states
- special mechanics without a defined player-facing presentation surface
- decision categories with no documented presentation choice
- simple propaganda, ideology, civil-war, preparedness, treaty, faction, or territorial categories expanded into full scripted GUI windows when a category picture would be clearer
- scripted GUI mechanics that genuinely need progress meters, status frames, variants, or animation but define only static text
- formable routes whose central proof is exact state control but have no exact-shape state-puzzle display or explicit reason for using a static territorial picture
- special mechanics that hide basic visible cause and effect
- generic playable country packages with no specific identity, map role, military style, economy, diplomacy, AI, or mechanic
- shared trees with no country-specific localisation, route names, decisions, AI weights, leaders, or rewards
- AI routes that can choose invalid, impossible, or unavailable branches
- important mechanic values scattered as magic numbers instead of script constants or documented tuning
- reward dump design used as the main pattern
- balance plans without exploit checks for free units, factory loops, equipment farming, influence farming, puppet abuse, war-goal spam, claim or core spam, advisor stacking, bypass abuse, or repeatable decision abuse
- decision systems that show every possible action at once instead of using phases, caps, priorities, pools, route locks, thresholds, or crisis filters
- factions that form too easily without minimum membership, crisis pressure, ideological compatibility, war state, or diplomatic preparation
- routes with no visible game evidence beyond hidden variables or tiny modifiers
- large trees with no early, middle, and late pacing
- routes with no tradeoff or failure state
- overuse of mutual exclusions where support branches should coexist
- localisation that reveals hidden effects, secret outcomes, or future surprises instead of visible baseline effects
- route-unlocked advisors that do not match route identity
- major focus trees without achievement hooks
- completion prompts missing a route coverage table requirement
- near-completion work that skipped the mandatory `chaosx_improvement_loop_planner` pass without a tooling blocker
- unresolved loop-agent expansion addendum, missing addendum disposition, or missing closure handoff before completion
- focus trees where unit rewards are repeated generic division spawns instead of route-specific military institutions, decisions, templates, or mobilization systems
- unit-granting focuses that exist only as filler or repeated free divisions with no story, route logic, or constraints
- major focus trees that read like one vertical checklist instead of a branching system
- focus tree sections without an architecture map or path plan showing route locks, optional branches, convergence points, hidden routes, crisis branches, and late-game branches where relevant
- branches where every focus simply follows the previous one without a strong story reason
- expansion trees that are only linear claim ladders instead of ideology, trauma, patron, military, economic, or chaos-driven ambitions
- evolutions that are really just ordinary stages
- evolution specs that do not define whether each evolution enters through active-event evolution, pre-fire evolved opening, or both
- active-event evolutions that do not state what changes immediately for existing active actors
- pre-fire evolved openings that do not state how the first firing changes before the ordinary baseline starts
- triggerable scenarios with prerequisites, such as Chaos Meter state, event progression, evolution unlocks, date gates, global flags, or prior campaign state, unless the user explicitly requested a locked scenario
- triggerable scenarios that do not create instant chaos directly from setup controls, intensity sliders, or scenario options
- fixed cooldowns or pressure values without dynamic factors
- decision, mission, or focus cost plans that rely mostly on political power or command power when concrete costs such as XP, equipment, manpower, fuel, stability, war support, supply, local support, foreign access, or unit commitments would fit better
- achievements missing from a major event spec
- achievements that unlock too easily or only reward the obvious route
- achievements without conditions, disqualifiers, icon directions, or tracking notes
- missing asset handoff for required assets
- major mechanic, formable, hidden reveal, high-chaos route, scripted GUI, or dramatic leader transformation with no presentation-choice pass
- animated asset plan that lacks static fallback, state logic, frame-sheet handoff, target surface, sprite names, or `chaos-redux-frame-animation` ownership
- missing asset coverage for country names, cosmetic identities, ideology flags, focus-route flags, leader changes, portraits, faction emblems, decisions, focuses, ideas, achievements, and UI where relevant
- missing AI route matrix for major events, country-creation events, or foreign-influence systems
- missing super-event handoff for required super-events
- final event titles, event options, event descriptions, report prose, news prose, decision names, decision descriptions, focus names, focus descriptions, achievement titles, achievement descriptions, GUI labels, event-detail text, or spreadsheet-facing wording written as pasteable localisation when the spec should give direction only
- sample, possible, temporary, or placeholder player-facing text included in the spec when the coding agent should write the final wording
- super-event title, button text, quote, cultural remark, slogan, lyric fragment, allusion, or audio choice written as final content without research and source documentation
- placeholder, sample, or working super-event text that could be pasted into localisation
- role labels, asset names, achievement titles, or prompt filenames reused as final super-event localisation without research
- coding prompt or goal prompt that lets unresearched super-event text be implemented instead of treating it as blocked
- goal prompt over 4000 characters
- goal prompt that tries to contain the whole spec instead of pointing to files
- missing final zip package containing all required spec files, prompt files, route diagrams if used, research notes, and matrices
- new country tags created without inventorying vanilla, Chaos Redux, installed Workshop mods, and other local mods
- duplicate country identities created when a valid vanilla identity already exists
- living vanilla countries or meaningful existing trees overwritten without an explicit event requirement
- technology or doctrine changes without `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` requirements in the coding prompt
- weighted AI or event behavior without named probability scenarios and the correct inspection, evaluation, sweep, comparison, or rendering workflow
- visible 3D units, buildings, creatures, vehicles, aircraft, naval objects, or map entities without an asset profile, vanilla scale reference, source geometry measurement, action plan, provider lineage, export and reimport proof, live consumer, and screenshot evidence
- a side-profile sheet, turnaround board, collage, or multi-view board planned as a Meshy input instead of one clean reference image
- requested skeletal animations replaced by a static mesh or render
- historical or grounded flags that skip cited design research, flat reconstruction, or manual geometry comparison
- grounded polities assigned invented substitute people
- real leaders planned without sourced attribution, licensing notes, head-and-shoulders crop, identity preservation, and role-specific outputs
- temporary continuation prompts included in a saved specification, prompt file, or final ZIP package
- admin audit sections inside the spec
- major event ideas or spirits whose main effect is a tiny modifier with no meaningful strategic role
- obvious system plumbing repeated as design

The spec should be ambitious, detailed, researched, and usable. Do not stop at a conservative minimum when the idea supports more.

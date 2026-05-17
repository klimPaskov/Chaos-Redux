---
name: chaos-redux-event-planning
description: Use when turning a rough Chaos Redux event idea into a detailed event specification before implementation.
---

# Chaos Redux Event Planning

Use this skill to design or expand events for the Hearts of Iron IV mod Chaos Redux.

This skill creates event specifications. It does not implement code. Implementation belongs to `chaos-redux-events`. Visual asset generation and processing belongs to `chaos-redux-event-assets`. Super-event quote, remark, music, and presentation research belongs to `chaos-redux-super-events`.

## 1. Required reading

Before writing the event specification, use the following as the design baseline:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets` when the event needs visual assets
- `chaos-redux-super-events` when the event needs a super-event
- provided event spreadsheet rows
- provided existing event docs
- provided Chaos Redux mechanics docs
- existing event files, localisation, assets, scripted effects, scripted triggers, decisions, focus trees, event logs, event clusters, and related systems

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

The final response may mention that the repo and spreadsheet were inspected. The downloadable spec should be player-facing design and implementation-relevant event design.

Avoid obvious lines such as:

- the event only fires if enabled
- the event should not fire after a world-end scenario
- disabled events should not fire
- the coding agent should use valid syntax
- the system should respect existing global settings

Those are baseline system responsibilities. Include technical notes only when they prevent a likely mistake, explain non-obvious behavior, or define a unique rule for this event.

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
- full focus-by-focus maps with every individual focus named and described
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
- what every individual focus in those trees should do, unlock, represent, and connect to
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
- what pressures, cooldowns, costs, or risks it changes
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

## 3.5 Exhaustive focus tree mapping standard

Focus trees must be fully designed in the specification. This does not mean giving a theme list, branch overview, sample branch, or note that a tree is needed. It means literally writing out every focus the tree should contain, one by one. A spec that says a tag needs a deep tree but does not list the actual focuses has failed the focus tree requirement.

When an event creates a playable country, long-lived tag, major splinter, major faction, rare high-chaos actor, alternate state, or world-order contender, the spec must map the full focus tree focus by focus. The coding agent should not have to invent the focus names, branch layout, prerequisites, unlocks, internal logic, route purpose, story meaning, or late-game ambitions. The spec should not provide a few examples and imply the rest. The rest must be written too.

For each focus, define the details that make the focus implementable and meaningful. Each focus must include the fields below unless a field is clearly irrelevant to that focus:

- focus name or working title
- branch, sub-branch, and rough tree position
- prerequisite structure
- mutual exclusions and route locks
- unlock conditions, including event, chaos, evolution, ideology, war, faction, tag, decision, hidden flag, or campaign-state conditions
- narrative purpose and in-world meaning
- research or inspiration note when the focus depends on history, culture, religion, politics, military practice, or regional context
- gameplay purpose and effect direction
- important effects, modifiers, claims, wars, technologies, divisions, ideas, characters, laws, decisions, events, or mechanics it unlocks
- follow-up focuses, events, decisions, crises, or hidden routes it leads into
- AI preference and path behavior when relevant
- focus icon direction and visual motif
- localisation tone or key phrase direction when useful
- research basis or historical, regional, ideological, cultural, military, religious, economic, or thematic inspiration when relevant
- how the focus connects to the country story and the wider event
- failure, bypass, alternate, or cleanup behavior when relevant

A focus tree map should read like a design blueprint. A coding agent should be able to implement the focus tree without filling in creative gaps. The spec may use tables, numbered entries, or structured sections, but every focus needs its own entry. Placeholder names, `TBD`, generic bonus rows, and sample-only focus lists are not acceptable. Do not provide sample focuses and imply the rest. If the tree needs 240 focuses, list and design all 240 focuses.

Every focus must earn its place. It should create a real choice, unlock a meaningful effect, reveal lore, change the country direction, support a playstyle, advance an internal faction struggle, alter diplomacy, move the economy, change the military, create a new risk, or connect back into the event chain. Do not use filler focuses to inflate the count.

Major countries, serious custom tags, high-chaos actors, and world-order contenders can require hundreds of focuses each. This is acceptable when the country has enough politics, factions, wars, economy, diplomacy, military development, hidden routes, special mechanics, and late-game ambitions. If an event creates several major playable countries, the spec may need to map hundreds and hundreds of focuses across the event, and sometimes thousands. This is expected for major country-creation events when the scope supports it. Depth, research, and coherence matter more than speed.

Do not treat 80 to 120 focuses as a ceiling. That can be a medium tree. A major outcome, custom high-chaos country, or campaign-defining splinter may need 150, 200, 300, or more individually mapped focuses when the design supports that scale. The only unacceptable large tree is one filled with generic or disconnected focuses.

For major or strange countries, the focus tree should usually have separate, fully mapped sections instead of one small political tree. Each section must then have its individual focuses mapped. Map separate branch groups where they fit the country identity, such as:

- opening survival and emergency authority branch
- main political tree
- internal faction tree or balance-of-power path
- legitimacy, law, and administration tree
- separate expansionism, reunification, liberation, or war-goal tree
- military reform tree
- army doctrine and special units tree
- navy tree when relevant
- air force tree when relevant
- industry and economy tree
- infrastructure, resource, logistics, and rail tree
- diplomacy and faction tree
- intelligence, underground, propaganda, security, or police tree
- science, religion, cult, magic, technology, or special-mechanic tree when relevant
- ideology-specific branches
- historical or cultural restoration branches
- rare campaign-state branches
- evolution-unlocked branches
- high-chaos branches
- hidden or secret routes
- late-game ambition tree
- world conquest, world revolution, world-end, or world-order tree when the identity supports it

A large focus tree must be a branching design, not a long linear list. Do not write focus after focus in a single vertical sequence unless the country is intentionally tiny and temporary. For any major or playable country, the spec must include a focus tree architecture map before the individual focus entries. That map should show the rough visual structure, including opening trunk focuses, fork points, mutually exclusive route gates, optional side branches, convergence focuses, route-locked subtrees, hidden offshoots, crisis branches, and late-game branches. Use headings, diagrams in text, indentation, numbered lanes, tables, or row and column notes. The coding agent should be able to see where the tree branches before reading the individual focus details.

A strong focus tree should create different playthroughs. It should contain real choices, not only a checklist. Use several types of structure where they fit:

- early survival trunk that quickly fans into politics, economy, army, diplomacy, and special-mechanic branches
- mutually exclusive ideological or faction routes that change later available focuses
- optional side branches that solve problems in different ways
- cross-branch prerequisites where political choices alter industry, military, diplomacy, and expansion options
- convergence focuses that resolve a route and open a new stage
- failure or crisis branches that appear after defeats, coups, lost capitals, foreign betrayal, or high chaos
- evolution-unlocked branches that are not visible in a normal run
- hidden routes that require specific decisions, achievements, foreign influence, leader choices, or strange campaign states
- expansionist branches that have their own internal logic and are not just a straight list of claims
- late-game ambition branches that fork again based on the earlier route

Linear focus trains are not acceptable for major trees. A branch where every focus only requires the previous focus is usually a sign that the branch is boring. Redesign it unless the linearity has a clear story reason, such as a short emergency sequence, a ritual sequence, a timed evacuation, or a final irreversible march. Even then, it should connect back into a wider branching tree.

Every major route should have a different rhythm. A constitutional route might have negotiation gates, coalition concessions, and diplomacy side branches. A military junta route might split between professional army, secret police, and expansion doctrine. A cult route might branch through doctrine, recruitment, ritual economy, forbidden science, and war aims. A railway state might branch through schedules, armored trains, logistics law, foreign transit, and rail conquest. Do not reuse the same generic political, industry, and army ladder for every country.

When mapping each individual focus, include its exact branch role. Mark whether it is a trunk focus, fork focus, route lock, side focus, convergence focus, hidden focus, crisis focus, route finisher, or late-game unlock. The focus list should prove that the tree is non-linear. If the focus entries read like a numbered sequence with no forks, locks, side routes, or cross-links, the spec has failed.

Each branch must make story sense and connect to the other branches. Political choices should alter which industrial, military, diplomatic, and expansionist options are credible. Internal faction choices should feed purges, compromises, coups, civil wars, coalitions, secret paths, and AI strategy. Expansionism should not be a generic claim list. It should express the country's ideology, trauma, myth, economic need, military doctrine, foreign patrons, or evolved chaos identity.

Do research before mapping serious focus trees. Use historical, regional, cultural, political, military, religious, ideological, economic, and existing HOI4 context to make the branches specific. Focus names and routes should connect to plausible institutions, movements, leaders, symbols, geography, resources, military traditions, foreign relationships, and the event story. Weird and supernatural paths still need internal logic and thematic grounding. Research should shape the actual focuses, not only the intro paragraph before the tree.

When a custom country is strange, historical, extremist, supernatural, or high-chaos, its focus tree must explain how that state survives, what it believes, how it fights, how it treats civilians, how it governs, how it handles dissent, how it funds itself, how it expands, how it interacts with the parent event, and how it can become dangerous later. Extreme paths such as world conquest, dead internationalism, machine-cult rule, railway sovereignty, cult expansion, cosmic politics, resurrection doctrine, or global revolution are valid when the country identity supports them.

Smaller temporary tags may receive compact trees or decision-based content only when the spec explains why they are temporary and why a full tree would be wasteful. A compact tree still needs every focus individually mapped. Do not write only branch names for temporary tags unless they are deliberately not playable and not expected to survive.

When a large event would require hundreds or thousands of focuses, split the specification into dedicated focus-tree files or appendices. Do not reduce the number of mapped focuses because the file is becoming long. For example:

- `event_name_spec_part_1.md` for the main event
- `event_name_spec_part_2_focus_tree_country_a.md`
- `event_name_spec_part_3_focus_tree_country_b.md`
- `event_name_spec_part_4_focus_tree_high_chaos_tags.md`

A spec can have focus-tree-only parts. A single event spec can exceed 100,000 lines if that is what is needed to map every focus, country path, rare variant, decision, asset, super-event, and cleanup path without shallow summaries. That is acceptable. The limit is usefulness, not length. Do not shorten a full focus tree because the answer is already long. Continue in another spec part.

The finished focus tree sections should make it impossible for an implementation agent to create a tiny, generic, or boring tree while claiming to follow the spec.


## 3.6 Achievement design standard

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
- title
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

## 3.7 Baseline stages versus evolutions

Baseline stages and evolutions are different.

Baseline stages describe the ordinary flow of the event. They are the expected crisis lifecycle, such as first outbreak, containment attempt, spread, coalition formation, deep collapse, settlement, or defeat.

Evolutions are mutation tracks layered on top of the baseline. They make the event more predictable in some ways, more severe, stranger, more patterned, or more replayable. They can add new actors, new rules, new incidents, new tags, old movements, strange variants, stronger breakaways, or rare side branches.

Do not log ordinary stages as evolutions.

Do not use chaos tiers as simple walls that lock ordinary stage progression. Ordinary stages should flow from the event state. Chaos should affect intensity, probability, severity, weirdness, and opening strength.

Good evolutions can include:

- the same kind of crisis becoming easier to recognize and harder to stop
- breakaways learning from earlier breakaways
- depots, officers, or railways changing behavior before declarations happen
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
- what event log title should represent it
- how it interacts with chaos tier without being only a chaos-tier lock
- how it can be contained, spread, or escalate

## 3.8 Dynamic mechanics standard

Everything that acts like pressure, cooldown, progress, chance, support, duration, cost, tempo, AI willingness, spawn strength, aid amount, stage movement, or recognition should be dynamic by default.

Avoid fixed values as design answers. A fixed number may exist as a tuning anchor, but the spec should define the factors that shape it.

Dynamic factors can include:

- chaos tier and chaos value
- current wars
- stability and war support
- ideology and reforms
- manpower and equipment
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


## 3.9 AI strategy and behavior mapping standard

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

For focus trees, the spec must define AI path behavior at the branch level and for key individual focuses. If a large tree has mutually exclusive paths, secret routes, or dangerous high-chaos paths, specify which AI personalities or campaign states can choose them. High-chaos AI should be allowed to make strange or extreme choices when that is the point, but ordinary AI should not accidentally choose suicidal or nonsensical branches.

For foreign influence mechanics, the AI section must explain how major powers decide whether to recognize, fund, arm, infiltrate, puppet, betray, or abandon new countries. If volunteers, expeditionary support, proxy wars, or faction invitations exist, AI behavior must be mapped for those too.

A good AI section should make the implementation agent unable to create generic AI weights while claiming to follow the spec.

## 3.10 Country package and dynamic identity standard

When an event creates, releases, transforms, or significantly modifies a country, the spec must define that country as a full package. This applies to new custom tags and to existing countries that gain event-specific political identities, focus trees, flags, leaders, cosmetic names, ideology names, or mechanics.

For every new country, and every existing country that is meaningfully changed, the spec should provide a country package matrix or equivalent structured section. It must cover:

- tag or placeholder tag, with a note that final tags must avoid conflicts
- spawn, release, transformation, or takeover conditions
- core territory, claimed territory, disputed territory, and fallback territory
- history file needs and starting setup
- country name and cosmetic names
- ideology-specific names
- focus-tree route names
- faction names and possible faction cosmetic names
- ruling party names, sub-ideology labels, and political movement names
- starting politics and possible ideology shifts
- starting leader, leader traits, portraits, and possible leader replacements
- council, junta, committee, regency, cult, military, monarchist, democratic, communist, fascist, anarchist, or factional leadership variants when relevant
- flags for the base country, ideology variants, focus-tree variants, cosmetic variants, puppet variants, and major route transformations
- national spirits, ideas, decisions, events, focus tree, achievements, and mechanics tied to that country
- AI behavior and route preferences
- asset needs for every visible identity state
- localisation tone and naming rules
- documentation needs
- compatibility notes if the country already exists in vanilla, Chaos Redux, or common mods

Do not treat a custom country as complete because it has a tag and one flag. A serious country needs identity, politics, names, flags, leaders, mechanics, decisions, AI, localisation, assets, and route changes. If the country is only temporary and does not need a full package, the spec must explain why.

Political identity should be dynamic when the content supports it. Focus routes, ideology changes, coups, faction victories, foreign puppeting, religious transformations, high-chaos mutations, monarchist restorations, military takeovers, revolutionary councils, or world-order paths should be able to change the country name, flag, ruling party, leader, leader portrait, leader trait, cosmetic tag, national spirits, and available decisions when appropriate.

When planning alternate governments, do not use only generic ideology labels. Design specific in-world names, such as named councils, committees, directorates, juntas, congresses, restoration authorities, cult offices, leagues, syndicates, ministries, synods, communes, or military commands. These names should fit the country's story, region, history, route, and ideological language.

## 3.11 Mandatory asset coverage and source-mode standard

Everything visible or meaningful needs an asset plan. A major spec should not only define a few event pictures. It should identify assets for countries, focus trees, decisions, ideas, national spirits, achievements, flags, portraits, faction emblems, super-events, event pictures, UI, and route-specific identity changes.

Every focus in a mapped focus tree needs an icon direction. Large trees may use reusable icon packs, but the spec must still state which focuses use which motif or icon category. Do not leave hundreds of focuses with no asset guidance.

Every decision, decision category, idea, national spirit, achievement, faction emblem, UI panel, news image, report image, super-event image, and leader or council portrait that appears in the event needs an asset entry or a clear asset-family entry.

Every country package must include flags. Required flag coverage includes normal, medium, and small sizes for each implemented flag state. If the country has ideology-specific names, focus-tree transformations, puppet identities, restored historical forms, radical routes, or high-chaos mutations, the spec must identify whether those states need separate flags.

Historical and real-world flags should not be invented with `$imagegen` by default. If a country, movement, party, military authority, or restoration path has a real historical flag or a well-attested symbolic design, the asset prompt should instruct the asset agent to source that flag or symbol from a reliable source, document it, and convert it into HOI4 flag sizes. Use `$imagegen` only for fictional, alternate, supernatural, or deliberately invented flag identities when generated art is appropriate.

Historical or real leaders should not be generated. The spec should identify likely real portrait needs and instruct the asset agent to source real images, document source and license status, and crop them to HOI4 portrait size. Fictional leaders, council portraits, cult leaders, alternate invented officers, and symbolic committee portraits can use `$imagegen` when generated art is appropriate.

When an asset source is historically sensitive, disputed, or politically loaded, the asset prompt must require source notes, and a clear distinction between sourced historical use and fictional alternate-history invention.


## 4. What the specification should explore

A strong specification usually explores:

- the core event concept
- why the event matters
- how the event first appears
- what the player sees and chooses
- what consequences follow
- how the situation can escalate
- what rare variants can happen
- how AI countries react and choose routes
- how the event changes under different world conditions
- what decisions exist and how they interlock
- whether the event should create focus tree content
- whether the event should create new tags or transform existing countries
- how each new or transformed country changes names, flags, leaders, ideologies, parties, and politics
- whether the event should use a super-event
- what achievements should exist and why they are difficult
- what UI or visual presentation would make it stronger
- what other Chaos Redux systems it should interact with
- what assets the event needs, including all route-specific country assets
- what historical flags, symbols, and portraits must be sourced rather than generated
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

Avoid blunt labels such as:

- Warnings
- Danger
- Threat
- World Ending Risk
- any direct UI label that tells the player too plainly what is coming

Early information should feel incomplete. Use uncertainty, conflicting reports, rumours, cautious diplomatic language, intelligence disagreements, unexplained incidents, and unclear public reactions.

The player should understand deeper danger through patterns and consequences over time.

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
- whether it needs follow-up events, decisions, focus routes, or event log entries

Keep the super-event tone specific to the event. Do not make every super-event feel like the same apocalypse with a different image.

Do not fully research quotes, cultural remarks, or music inside this skill. Use `chaos-redux-super-events` for that work.

The event spec should provide enough direction for `chaos-redux-super-events` to find real quotes, meaningful cultural remarks, and suitable audio.

## 10. Writing style

Write in a serious, direct, grounded HOI4 style.

Avoid:

- generic disaster wording
- empty dramatic language
- making every event apocalyptic
- random chaos without purpose
- implementation code
- excessive technical detail
- filler text that repeats obvious system behavior

Mention implementation only where it matters for the design, such as super-event treatment, custom UI, AI behavior, documentation, assets, dynamic factors, focus tree structure, custom tags, or important system connections.

## 11. Specification shape

Do not force the specification into a fixed template.

Choose the structure that best fits the event idea.

The specification should still be easy for a coding agent to use. Use clear headings, explain the logic in a natural order, and make sure important design decisions are not buried.

For major events, split the spec into parts if needed. Do not compress deep design just to fit one file.

## 12. Depth and continuation

Do not compress the spec so much that important ideas become shallow.

The goal is depth, not speed.

Think through the event as far as the idea can reasonably go. If the event has multiple branches, evolutions, rare variants, custom countries, focus trees, UI elements, super-events, or major system connections, treat each of those as deserving real design space.

Large events should be written across multiple parts instead of being rushed into one response.

Each part should be complete enough to be useful on its own. Stop at a clean point and state what section should continue next.

Do not summarize later sections just because the current response is getting long. Continue in the next part instead.

For major events, the final combined specification may be extremely long. That is acceptable. A 10,000 line, 50,000 line, or 100,000+ line specification is valid if the event truly needs that much design detail. Do not compress focus trees, rare variants, or decision webs into summaries just to keep the file short. For required focus trees, keep writing focus-tree parts until every focus has been individually mapped.

Avoid filler. Every section should add useful design, player-facing detail, implementation clarity, asset direction, or system connection.

Before saving the final spec, run a cleanup pass. Remove generic safeguards, obvious implementation boilerplate, empty labels, repeated wording, and admin audit sections.

## 13. Asset planning

The event specification should identify all important visual assets. For major events, assume every visible system needs asset planning unless the spec explicitly explains why it does not.

Consider whether the event needs:

- idea icons
- national spirit icons
- focus icons for every focus or focus-family in each mapped tree
- decision category icons
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
- progression-state variants
- country-selection, event-log, or custom-window graphics when relevant

Asset generation, sourcing, cropping, resizing, DDS conversion, file placement, `.gfx` wiring, and manifests belong to `chaos-redux-event-assets`.

This skill should define what assets are needed, what they should represent, and what source mode they require.

Historical or real-world assets need special care. Historical flags, historical symbols, and real leader portraits should be sourced from reliable references and converted to HOI4 style rather than generated. Generated art is appropriate for fictional flags, fictional leaders, symbolic council portraits, invented high-chaos identities, idea icons, focus icons, decision icons, achievements, faction emblems, and UI art unless the user says otherwise.

### Reference examples for asset planning

When a spec or asset prompt asks for generated or sourced assets, tell the asset agent to inspect the matching reference examples before creating anything.

Use Linux project paths:

```text
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/tech_icons
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags
~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/focuses
```

Reference mapping:

- idea and national spirit icons: `assets/ideas`
- news event images: `assets/news_event_images`
- report event images: `assets/report_event_images`
- super-event images: `assets/super_event_images`
- tech icons: `assets/tech_icons`
- achievement icons: `assets/achievements`
- decision and decision category icons: `assets/decisions`
- flags: `assets/flags`
- focus icons: `assets/focuses`

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
- whether each asset is for an event, report event, news event, super-event, decision, idea, focus, achievement, flag, leader portrait, faction emblem, or UI element
- achievement icon list with completed icon directions for every achievement
- manifest requirements
- source mode, including whether a flag, symbol, or portrait must be sourced historically instead of generated
- reference example folder that must be inspected before asset work

The asset prompt must state the correct source mode where relevant.

It must also state the relevant reference folder from the list above when a matching folder exists.

Use `chaos-redux-event-assets` rules for source selection. Symbolic icons usually use `$imagegen`. News event images, report event images, super-event images, and real leader portraits use sourced images unless the user explicitly asks otherwise. Historical flags and historically attested symbols should be sourced and documented, then converted to HOI4 flag sizes. Fictional, supernatural, invented, or alternate-history flags can use `$imagegen` through `chaos-redux-event-assets` when appropriate.

Do not make the asset prompt vague. If a country has multiple cosmetic identities, ideology names, focus-route transformations, or leader changes, the asset prompt must list the required assets for each visible identity state.

## 15. HOI4 asset size reference

Use these sizes when planning assets:

- report event images: 210x176
- news event images: 397x153, black and white
- leader portraits: 156x210
- flags small: 10x7
- flags medium: 42x26
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

Report and news event images should look like documentary photographs. News event images should be black and white.

Super-event images should have a strong central composition, clear dramatic theme, readable subject, and enough contrast for HOI4 UI.

Focus icons should look like HOI4 focus icons, with a central symbol, readable silhouette, aged texture, painterly detail, and strong contrast.

Idea and national spirit icons should look like compact HOI4 icon art. They need strong symbolic shapes and clear readability at 64x64. They are similar to focus icons, but they are missing the main frame.

Achievement icons should be readable at 64x64 and have a clear completion theme. The completed version is generated first. Grey and not-eligible variants can be produced later.

Flags should use clean symbols that remain readable at HOI4 flag sizes.

Progression-state variants may include selected, dim, active, locked, completed, rejected, damaged, corrupted, urgent, meter-fill, and bar-fill states.

Photoshop may be mentioned only for progression-state variants.

## 17. Super-event research handoff

If the event has one or more super-events, create a separate super-event prompt file for `chaos-redux-super-events`.

The prompt should ask that skill to research or create the full super-event presentation package.

For each super-event, include:

- super-event purpose
- trigger moment
- tone
- title direction
- description direction
- quote direction
- cultural remark direction
- audio mood
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

## 18. Output rules

The event specification itself should be created as one or more downloadable Markdown files.

The spec file should contain only the event specification.

Do not put the asset prompt, super-event prompt, coding-agent prompt, or goal prompt inside the spec file.

For multi-part specs, create sequential files:

- `event_name_spec_part_1.md`
- `event_name_spec_part_2.md`
- `event_name_spec_part_3.md`
- `event_name_focus_tree_country_or_tag_part_1.md` when a focus tree is too large for the main spec
- `event_name_focus_tree_country_or_tag_part_2.md` and later files as needed

Continuation files should continue directly from the previous part so they can be combined later without cleanup.

Do not repeat earlier sections unless needed for clarity.

## 19. Final prompt files

Only after the full specification is complete, create separate downloadable prompt files outside the spec file.

Required prompt files:

- `event_name_asset_prompt.md`
- `event_name_super_event_prompt.md` when the event has one or more super-events
- `event_name_achievement_prompt.md`
- `event_name_coding_prompt.md`
- `event_name_goal_prompt.md`

The final answer should link all of those files and provide the goal prompt in a copy-pasteable code block.

### Asset prompt file

Create an asset prompt for `chaos-redux-event-assets`.

The prompt should cover all required visual assets, progression-state variants, final asset packaging, reference folders, source modes, and manifest requirements.

### Super-event prompt file

Create a super-event prompt for `chaos-redux-super-events` if the event has one or more super-events.

The prompt should cover titles, descriptions, quotes, cultural remarks, audio research, image direction, source documentation, licensing notes, and coordination with asset work.

### Achievement prompt file

Create a separate achievement prompt file for the coding and asset agents.

The achievement prompt must include every planned achievement with title, id, description direction, eligible countries, unlock conditions, disqualifiers, difficulty, hidden or visible status, why it is not trivial, icon direction, and all required tracking notes.

The achievement prompt should tell the implementation agent to inspect existing achievement patterns, implement the achievements, wire localisation and icons, create any required tracking flags or variables, document them, and avoid easy unlocks.

### Coding-agent prompt file

Create a coding-agent implementation prompt that summarizes the finished event spec.

The prompt must tell the coding agent to:

- implement the event according to the spec
- implement all mapped decisions, variants, evolutions, focus trees, custom tags, country packages, achievements, assets, and super-events included in the spec
- implement every individually mapped focus in the spec, with coherent non-linear branches, route locks, side paths, convergence nodes, hidden routes, proper icons, localisation, AI behavior, event integration, and no filler shortcuts
- implement every country package from the spec, including tag, history, names, cosmetic names, ideology names, ruling parties, leaders, leader changes, flags, route-specific identity changes, decisions, ideas, AI behavior, localisation, assets, and docs
- implement the full AI strategy matrix from the spec, including route preferences, foreign influence behavior, focus choices, decision choices, faction behavior, and high-chaos exceptions
- follow `AGENTS.md`
- follow `chaos-redux-events`
- use `chaos-redux-event-assets` if visual assets are required
- use `chaos-redux-super-events` if super-events are required
- keep all Chaos Redux systems aligned
- report anything that cannot be implemented cleanly
- keep iterating until the full spec is implemented to its fullest extent
- avoid fallbacks, simplifications, temporary versions, and good-enough approximations
- not claim completion until the implemented files satisfy the spec

### Goal prompt file

Create a separate `/goal` prompt file.

The goal prompt must be less than 4000 characters.

The goal prompt should not contain the whole spec or all long instructions. It should point to the spec file and the other prompt files, then state the most important pass or fail requirements.

The goal prompt must tell the implementation agent to keep iterating until the goal is accomplished to its fullest extent. It must also say not to claim completion until the implemented files satisfy the spec.

A good goal prompt should include:

- the spec file path
- the coding prompt file path
- the asset prompt file path
- the super-event prompt file path when relevant
- the achievement prompt file path
- the required skills or docs to follow
- the top design non-negotiables
- the requirement to create all required assets, tags, fully mapped non-linear focus trees, decisions, evolutions, achievements, and docs
- the requirement to provide a concrete completion report

If the goal prompt is near 4000 characters, shorten it by pointing to files instead of repeating details.

## 20. Final response checklist

The final response should include:

- spec file created
- asset prompt file created if assets are needed
- super-event prompt file created if super-events are needed
- achievement prompt file created
- coding prompt file created
- goal prompt file created
- spreadsheet row used when applicable
- repo context inspected
- event cluster role defined when relevant
- assets defined when needed, including country identity assets
- historical flags, real symbols, and real leader portraits marked for sourced asset work when relevant
- super-event direction defined when needed
- country package matrices created for new or modified countries when relevant
- AI strategy matrix created for major events or country-creation events
- focus trees mapped literally focus by focus when the event creates playable or long-lived countries, with every focus individually named and described
- every major focus tree written with individual focus entries, not only branch summaries
- every major focus tree includes a non-linear architecture map with trunk focuses, fork points, route locks, optional branches, convergence nodes, hidden routes, crisis branches, and late-game branches where relevant
- focus tree files split into separate parts when the tree is too large for one file
- decisions and rare variants mapped when they exist
- achievements mapped with difficult conditions, icon directions, and tracking notes
- ideology-specific names, cosmetic names, leader changes, and flag changes mapped when relevant
- uncertainties or blockers
- downloadable links to all created files
- copy-pasteable `/goal` prompt under 4000 characters

## 21. Cleanup and quality gate

Before saving the final files, perform a strict review.

Reject the draft if it has any of these problems:

- vague placeholder decisions
- vague rare variants
- vague country paths
- custom tags without full country identity, assets, politics, leaders, flags, AI, and content expectations
- new or modified countries without country package matrices when they matter
- historical countries or movements with invented `$imagegen` flags when sourced historical flags should be used
- real historical leaders planned as generated portraits instead of sourced portraits
- playable countries without focus-by-focus mapped trees
- focus tree sections that list only branch themes instead of every focus
- focus tree plans that give samples instead of every required focus
- major countries without separate political, military, industry, diplomacy, and expansion or special-mechanic sections when those sections fit the country
- focus trees that are too small, generic, linear, or boring for the country role
- major focus trees that read like one vertical checklist instead of a branching system
- focus tree sections without an architecture map showing trunk focuses, forks, route locks, optional branches, convergence points, hidden routes, crisis branches, and late-game branches where relevant
- branches where every focus simply follows the previous one without a strong story reason
- expansion trees that are only linear claim ladders instead of ideology, trauma, patron, military, economic, or chaos-driven ambitions
- evolutions that are really just ordinary stages
- fixed cooldowns or pressure values without dynamic factors
- achievements missing from a major event spec
- achievements that unlock too easily or only reward the obvious route
- achievements without conditions, disqualifiers, icon directions, or tracking notes
- missing asset handoff for required assets
- missing asset coverage for country names, cosmetic identities, ideology flags, focus-route flags, leader changes, portraits, faction emblems, decisions, focuses, ideas, achievements, and UI where relevant
- missing AI route matrix for major events, country-creation events, or foreign-influence systems
- missing super-event handoff for required super-events
- goal prompt over 4000 characters
- goal prompt that tries to contain the whole spec instead of pointing to files
- admin audit sections inside the spec
- obvious system plumbing repeated as design

The spec should be ambitious, detailed, researched, and usable. Do not stop at a conservative minimum when the idea supports more.

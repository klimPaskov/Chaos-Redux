---
name: chaos-redux-event-planning
description: Use when expanding Chaos Redux event ideas into detailed specifications before implementation.
---

# Chaos Redux Event Planning

Use this skill to design or expand events for the Hearts of Iron IV mod Chaos Redux (https://github.com/klimPaskov/Chaos-Redux).

This skill creates event specifications. It does not implement code. Implementation belongs to `chaos-redux-events`. Visual asset generation and processing belongs to `chaos-redux-event-assets`. Animated sprite planning, frame-sheet requirements, animated portrait packages, and animation handoff details belong to `chaos-redux-frame-animation` when motion is needed. Super-event quote, remark, music, and presentation research belongs to `chaos-redux-super-events`.

## Reference map

The root keeps every section heading with its guarantee. Read the complete reference file below before the matching work.

- [Advanced event system design](references/advanced-system-design.md): index of the three advanced standards below, read first when unsure which part applies.
- [Focus tree, mechanic, and decision design standards](references/advanced-focus-tree-design.md): read when specifying a major focus tree, its reward and idea design, special mechanics and faction systems, or decision categories.
- [Country package, starting forces, and model planning standards](references/advanced-country-and-forces-design.md): read when specifying a country package, naming, a formable nation, starting or reinforcing forces, a new unit type, or a 3D model.
- [Chaos generation and feedback standards](references/advanced-chaos-generation-design.md): read when an event adds, scales, repeats, or reduces global Chaos.
- [Player-facing text direction](references/player-facing-text-direction.md): read when writing tone, option, humour, writing-style, or localisation-handoff direction.
- [Event presentation and asset planning](references/presentation-and-assets.md): read when specifying custom UI, super-events, asset planning, asset prompts, sizes, style, or the super-event research handoff.
- [Specification delivery, prompts, and review](references/specification-delivery.md): read when shaping, splitting, delivering, prompting, and reviewing the finished specification.

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

### Source authority and shared identifiers

Identify the authoritative design parts and their acceptance basis before extending a package; use combined reading copies as navigation when they duplicate those parts. Original archive manifests, source snapshots, and dated QA receipts establish historical evidence, not current checkout integrity or tool availability. Link mutable workflow instructions to the current owner skill and discover current capabilities when the handoff depends on them.

Before proposing a shared scenario or cluster ID, check all active spec packages and reservations, implemented registry definitions and constants including hidden entries, and the canonical workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. CSV exports can orient research but do not establish current occupancy. Distinguish event IDs, manual triggerable-scenario IDs, world-end registry IDs, cluster IDs, and display/sort values explicitly; equal numbers in different namespaces do not establish a collision. Record proposed reservations centrally in `docs/specs/shared_identifier_registry.md` with namespace, owner, status, and source evidence before other packages consume them; a reservation does not prove design acceptance or runtime registration. Preserve implemented IDs and remap colliding proposals with their package references instead of renumbering live content to fit a plan.

## 2. Input

The user will provide either:

- a rough event idea
- a partly developed concept
- an existing event that needs deeper rework
- a detailed spec that needs cleanup before implementation

Treat the user idea as the starting point. Do not assume it is final.

When the idea is rough, expand it into a deeper design.

When the idea is already detailed, preserve the core direction and improve structure, clarity, missing connections, and implementation readiness.

### Specification folder convention

Event source specifications should live in event-specific subfolders under `docs/specs/`.

Use this shape:

```text
docs/specs/<event_id>_<event_slug>_specs/
```

Examples:

```text
docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md
docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md
docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md
```

Use `docs/plans/<event_id>_<event_slug>_plans/` for subagent plans, improvement addenda, audit follow-up notes, blocked reports, and implementation handoffs. Plans can become source design later, but the main agent should promote or merge them into `docs/specs/` when they are accepted as part of the final event design.

## 3. Design purpose

The goal is to create an event that feels like a layered Chaos Redux system, not a basic popup.

The event should have atmosphere, player choice, consequences, escalation, lore, replay value, and enough visual support to feel finished.

The design should be ambitious. Do not get lazy, conservative, or minimal unless the event is genuinely small. Depth matters more than speed. Take the time needed to research, compare patterns, think through consequences, and design the event as if the coding agent will implement exactly what is written.

The finished spec should make the coding agent feel that the event has already been designed in full.

### 3.1 Idea-first specification style

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

Those are baseline system responsibilities. Include technical notes only when they prevent a likely mistake, explain non-obvious behavior, or define a unique rule for this event. Otherwise, it's just noise.

Do not create negative capability notes for absent event surfaces. If an event does not have a world-end scenario, do not mention world-end scenarios. If an event does not have a manual triggerable scenario, do not mention triggerable scenarios. Do not write sections, bullets, event-detail notes, spreadsheet-facing summaries, implementation prompts, or player-facing text that say `no world-end scenario`, `does not have a world-end scenario`, `no manual triggerable scenario`, `does not have a triggerable scenario`, or similar absence wording. Omit the surface completely unless it actually exists or the user explicitly asks for an explanation of why it is absent.

#### Tone and presentation direction standard

Every player-facing text surface in the spec gets writing direction (actor or viewpoint, visible and uncertain information, tone and humour mode, research needs, words to avoid, dynamic placeholders), never pasteable localisation or draft wording. Warning, threat, and escalation text is planned as a pattern shown through partial information, never as a label.
Read the complete requirements in [Tone and presentation direction standard](references/player-facing-text-direction.md#tone-and-presentation-direction-standard) before this work.

#### Event option humour, irony, and cultural remark direction

Important options and option families get a defined stance, speaker, tone, and research-gated cultural direction that varies by route and actor, without any final option text or sample buttons. Humour must fit the stakes, and atrocities and mass suffering take grim irony or euphemism, never cheap comedy.
Read the complete requirements in [Event option humour, irony, and cultural remark direction](references/player-facing-text-direction.md#event-option-humour-irony-and-cultural-remark-direction) before this work.

### 3.2 Depth standard

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

### 3.3 Research depth standard

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

### 3.4 Full decision, rare variant, and branch mapping

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

### 3.5 Focus tree path design standard

For a specification with focus paths, design country-specific routes with connected decisions, AI, rewards, and full route coverage.
Read the complete requirements in [Focus tree path design standard](references/advanced-focus-tree-design.md#focus-tree-path-design-standard) before this work.

### 3.6 Focus tree visual planning standard

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

### 3.7 Achievement design standard

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

### 3.8 Baseline stages versus evolutions

Baseline stages and evolutions are different.

Baseline stages describe the ordinary flow of the event. They are the expected crisis lifecycle, such as first outbreak, containment attempt, spread, coalition formation, deep collapse, settlement, or defeat.

Evolutions are mutation tracks layered on top of the baseline. They make the event more predictable in some ways, more severe, stranger, more patterned, or more replayable. They can add new actors, new rules, new incidents, new tags, old movements, strange variants, stronger breakaways, or rare side branches.

Do not log ordinary stages as evolutions.

Do not use chaos tiers as simple walls that lock ordinary stage progression. Ordinary stages should flow from the event state. Chaos should affect intensity, probability, severity, weirdness, and opening strength.

#### Evolution entry paths

When an event has evolutions, the spec must say how each evolution enters play. Do not write evolutions only as future modifiers or only as post-fire upgrades unless that is truly the design.

Use two separate entry-path concepts when the event supports both.

**Active-event evolution** means the event has already fired and an evolution unlocks while one or more actors from that event still exist or the event system is still active. The spec must define what changes immediately for the active actors: focus paths, decision families, national spirits, unit growth, targeting rules, AI strategy, faction behavior, super-event eligibility, and cleanup. The event should not need to fire again for the active actor to receive the evolution content.

**Pre-fire evolved opening** means the event has not fired yet, but the world state, chaos tier, previous evolution memory, or other allowed event trigger lets the first firing start in a more evolved form. The spec must define the changed opening package: number of actors, target selection, starting ideas, initial units, first decisions, opening events, AI plan.

If both entry paths exist, write both explicitly under one evolution. For example, an event may have an active evolution that unlocks a focus path for an already spawned country, while a later first firing may start with multiple spawned countries.

Each chaos tier can have only one evolution stage. The maximum number of evolutions is 5.

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

#### 3.8.1 Chaos generation and feedback standard

Destabilizing events need a full Chaos impact map, calibrated gains and containment reductions, overlap checks, and repeat guards. Evolution status alone never awards Chaos.
Read the complete requirements in [Chaos generation and feedback standard](references/advanced-chaos-generation-design.md#chaos-generation-and-feedback-standard) before this work.

### 3.9 Dynamic mechanics standard

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

Dynamic behavior should still be readable. Define cause and effect clearly so the player can learn the pattern through events and decisions. Dynamic does not mean public-facing. Internal calculations can track many values when useful, while the public layer should summarize them into one or two values when possible, three when needed, and never more than four persistent values the player must actively track for the mechanic.

### 3.10 Cost and sacrifice design standard

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

### 3.11 AI strategy and behavior mapping standard

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

For weighted behavior, route the audit through `chaosx_ai_probability_auditor`, give the implementation agent named scenarios and the expected ordering, timing band, dominance limit, or starvation limit to test, and require the coding-agent prompt to begin with `hoi4.probability_inspect`, use `hoi4.probability_inspect` for the scenario matrix, `hoi4.probability_analyze` (`analysis = sweep`) for thresholds and rank reversals, and `hoi4.probability_analyze` (`analysis = compare`) after implementation. Reserve `hoi4.probability_analyze` (`analysis = simulate`) for explicitly declared uncertain inputs and `hoi4.probability_analyze` (`analysis = sequence`) for a complete declared custom pool with cadence and state transitions. Request `hoi4.probability_analyze` (`analysis = render`) when a ranking, matrix, timing, sensitivity, sequence, comparison, or unresolved view will make the handoff easier to review. Do not specify an exact selection probability when the candidate pool or external factors are incomplete.

For focus trees, the spec must define AI path behavior at the branch level and for key individual focuses. If a large tree has mutually exclusive paths, secret routes, or dangerous high-chaos paths, specify which AI personalities or campaign states can choose them. High-chaos AI should be allowed to make strange or extreme choices when that is the point, but ordinary AI should not accidentally choose suicidal or nonsensical branches.

For foreign influence mechanics, the AI section must explain how major powers decide whether to recognize, fund, arm, infiltrate, puppet, betray, or abandon new countries. If volunteers, expeditionary support, proxy wars, or faction invitations exist, AI behavior must be mapped for those too.

A good AI section should make the implementation agent unable to create generic AI weights while claiming to follow the spec.

### 3.12 Country package and dynamic identity standard

For every new or transformed country, specify its complete playable package and identity transitions.
Read the complete requirements in [Country package and dynamic identity standard](references/advanced-country-and-forces-design.md#country-package-and-dynamic-identity-standard) before this work.

### 3.13 Starting forces and reinforcement pathway standard

For event actors with forces or custom units, specify their opening strength, reinforcement path, ownership, and model consumers.
Read the complete requirements in [Starting forces and reinforcement pathway standard](references/advanced-country-and-forces-design.md#starting-forces-and-reinforcement-pathway-standard) before this work.

### 3.14 Mandatory asset coverage and source-mode standard

Everything visible or meaningful needs an asset plan. A major spec should not only define a few event pictures. It should identify assets for countries, focus trees, decisions, ideas, national spirits, achievements, flags, portraits, faction emblems, super-events, event pictures, UI, unit systems, and route-specific identity changes.

Every focus in a mapped focus tree needs an icon direction. Large trees may use reusable icon packs, but the spec must still state which focuses use which motif or icon category. Do not leave hundreds of focuses with no asset guidance.

Every decision, decision category, idea, national spirit, achievement, faction emblem, UI panel, news image, report image, super-event image, leader or council portrait, and important special-unit identity that appears in the event needs an asset entry or a clear asset-family entry.

Every country package must include flags. Required flag coverage includes normal, medium, and small sizes for each implemented flag state. If the country has ideology-specific names, focus-tree transformations, puppet identities, restored historical forms, radical routes, or high-chaos mutations, the spec must identify whether those states need separate flags.

Every new flag uses image generation (see the Image-generation route section of chaos-redux-event-assets). For a real or historically attested country, movement, party, military authority, or restoration path, the asset prompt must first require reliable design research and a cited reference. Image generation then reconstructs that exact design as a flat flag under the reference constraint. It must not produce waving fabric, painterly flag artwork, scenery, gradients, perspective, fake lettering, or invented heraldry. The asset prompt must require a manual geometry, colour, orientation, and symbol comparison before HOI4 flag resizing. Fictional and alternate flags also use image generation, while remaining flat flag designs rather than illustrations.

Historical or real leaders must not be generated, and grounded polities must not receive invented substitute people. Treat a polity as grounded when it existed in whole or in part, represents a real community, or claims continuity from a real institution. The spec must identify its real portrait or institutional-material needs and instruct `chaosx_portrait_creator` to source attributed material, document source and license status, choose an explicit head-and-shoulders crop for a person, prepare the placeholder, and review the user-supplied HOI4-style final against the canonical reference root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.claude/skills/chaos-redux-event-assets/assets/gfx_references` plus its role-specific contact sheet. Generated one-person portraits are reserved for wholly fictional leaders of wholly fictional, deliberately high-chaos polities and must be created and processed by the portrait worker. Fictional councils and symbolic bodies should use people-free institutional compositions.

When an asset source is historically sensitive, disputed, or politically loaded, the asset prompt must require source notes and a clear distinction between sourced historical use and fictional alternate-history invention.

### 3.15 Effect strength and impact standard

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

Chaos Meter feedback is a core event contract for strange or destabilizing events. Use the Chaos generation and feedback standard above to map how the event raises and lowers Chaos across manifestation, success, spread, concrete consequences produced by evolved behavior, special-country growth, containment, and defeat. Do not treat the Chaos Meter as an optional connection when the event materially destabilizes the world.

Consider links to other existing Chaos Redux systems when they strengthen the event.

Possible links include:

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

Plan custom windows only when the event needs them, including interaction, layout, animation, and native UI integration.
Read the complete requirements in [Custom UI and presentation](references/presentation-and-assets.md#custom-ui-and-presentation) before this work.

## 9. Super-event planning

For each proposed super-event, define its trigger, presentation, research needs, and event-specific aftermath.
Read the complete requirements in [Super-event planning](references/presentation-and-assets.md#super-event-planning) before this work.

## 10. Writing style

Player-facing text is specified as direction only and never as final localisation. The general text writing style rules (no em dash or semicolons, no dialectical hedging, no staccato, no staged contrast formulas) and the localisation handoff format apply to every spec, and source-dependent super-event wording stays blocked for `chaos-redux-super-events`.
Read the complete requirements in [Writing style](references/player-facing-text-direction.md#writing-style) before this work.

## 11. Specification shape

Keep the specification navigable and organized around the event and its implementation needs.
Read the complete requirements in [Specification shape](references/specification-delivery.md#specification-shape) before this work.

## 12. Depth, file splitting, and continuation prompts

Split large specifications by coherent subject without reducing their depth; use the continuation and resume formats when work spans tasks.
Read the complete requirements in [Depth, file splitting, and continuation prompts](references/specification-delivery.md#depth-file-splitting-and-continuation-prompts) before this work.

## 13. Asset planning

Include every required asset and consumer in the specification; assign the correct source mode and reference family.
Read the complete requirements in [Asset planning](references/presentation-and-assets.md#asset-planning) before this work.

## 14. Asset prompt handoff

When assets are required, deliver production prompts with subject, style, canvas, source, and consumer requirements.
Read the complete requirements in [Asset prompt handoff](references/presentation-and-assets.md#asset-prompt-handoff) before this work.

## 15. HOI4 asset size reference

Use the inspected consumer and the owning asset skill to select native dimensions.
Read the complete requirements in [HOI4 asset size reference](references/presentation-and-assets.md#hoi4-asset-size-reference) before this work.

## 16. Asset style reference

Use the matching HOI4 reference family for each planned asset.
Read the complete requirements in [Asset style reference](references/presentation-and-assets.md#asset-style-reference) before this work.

## 17. Super-event research handoff

When a super-event needs text or audio research, provide its complete bounded research brief.
Read the complete requirements in [Super-event research handoff](references/presentation-and-assets.md#super-event-research-handoff) before this work.

## 18. Output rules

Deliver the complete specification package, including the required final ZIP and its contents.
Read the complete requirements in [Output rules](references/specification-delivery.md#output-rules) before this work.

## 19. Final prompt files

Prepare the required final asset, super-event, achievement, coding-agent, and goal prompts according to their applicable scope.
Read the complete requirements in [Final prompt files](references/specification-delivery.md#final-prompt-files) before this work.

## 20. Final response checklist

The final response should include:

- the final ZIP package and a downloadable link
- the event id, slug, intended extraction folder, and package filename
- the specification files created
- the asset prompt, coding-agent prompt, goal prompt, achievement prompt, decision and mission prompt, and super-event prompt paths when relevant
- the authoritative workbook row or export-only CSV snapshot used when applicable
- repo context inspected
- event cluster role defined when relevant
- Chaos impact map defined for strange or destabilizing events, including manifestation, movement success, special Chaos-country power milestones, spread, evolution-enabled consequences, failed containment, reversals, repeat guards, and shared-source overlap
- assets defined when needed, including country identity assets
- a presentation-choice pass for important decision categories, custom UI, formables, route reveals, high-chaos states, and major leader transformations
- static or animated category picture needs mapped only for eligible simple categories where a picture is clearer than a full GUI
- formable state-puzzle requirements mapped with exact state shapes, dynamic qualification, static alternative, reusable templates, and eligibility agreement where relevant
- animated sprite and portrait needs mapped with static fallbacks, state logic, and `chaos-redux-frame-animation` handoff expectations only when motion is useful
- historical flags, symbols, and real leader portraits assigned the correct source workflow
- every flag assigned the flat reference-constrained image-generation workflow
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
- 3D model and skeletal animation planning, vanilla scale references, Meshy reference requirements, pipeline routing, and user-owned live validation separated from implementation delivery when relevant
- clear focus-tree path maps, non-linear architecture, anchor focuses, mutual exclusions, convergence, hidden routes, crisis branches, late-game paths, filters, reward diversity, and idea lifecycle audits when relevant
- decisions, rare variants, evolutions, achievements, route identities, leader changes, flags, and unit-generation systems mapped when they exist
- varied costs, risks, requirements, and sacrifices instead of default political power or command power purchases
- a public-facing value budget for every main special mechanic, with one or two values preferred, three acceptable when needed, four as the hard maximum, and hidden internal values separated from player-facing state
- uncertainties and blockers stated clearly
- strong enough effects for the intended role
- useful depth review completed and actual findings resolved or explicitly scoped/queued, without a tool or closure-report completion gate
- temporary continuation prompts removed from every final package file
- a brief package summary that does not repeat the full specification

## 21. Cleanup and quality gate

Review the completed specification and handoffs against the full design; resolve duplication and contradictions while preserving every accepted requirement.
Read the complete requirements in [Cleanup and quality gate](references/specification-delivery.md#cleanup-and-quality-gate) before this work.

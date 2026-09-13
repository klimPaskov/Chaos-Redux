# Event 044 Yakub Returns planning review

## Review scope

This review checks the finished design against the supplied Chaos Redux event-planning, events, decisions and missions, focus-tree, asset, super-event, frame-animation, 3D, improvement-loop, subagent, mechanics, shared API, catalog, repository, and subagent-definition files.

The planning pass read and processed every supplied top-level text file, all three catalog CSV exports, and all 20 subagent TOML definitions contained in the supplied ZIP. The role requirements from those subagents were used as review lenses. No independent subagent process was available through the active interface, so this document does not claim separate subagent execution or handoffs.

## Core promise test

The event promises a domestic American political crisis that can become a state-building project, an international movement, and a terminal world order. The design now supports that promise through one connected progression:

- a claimant appears and begins organizing
- the government chooses containment, reform, negotiation, tolerance, or repression
- chapters build institutions
- factions compete over the movement's purpose
- a state may emerge through settlement, secession, collapse, or autonomy
- the state chooses a political route and develops ordinary military and economic capacity
- foreign movements adapt or reject the doctrine
- an International forms only from durable transnational proof
- a world-end route requires a state, bloc, leader, and geopolitical footprint
- succession preserves or changes the project after Yakub's death, disappearance, or discredit

The event can end at baseline, remain a persistent political issue, create a state, or reach world scale. It does not require every campaign to follow the full chain.

## Player-facing complexity review

The domestic mechanic exposes one persistent value, Yakubite Influence. Chapter conditions, institutional reach, government approach, faction strength, intelligence penetration, martyr risk, and regional suitability remain hidden or qualitative.

The International exposes one primary bloc value, International Cohesion. The anchor should not require the player to monitor domestic Influence and International Cohesion as equal long-term meters after the International becomes the main system. Domestic state conditions continue through decisions, ideas, and local statuses.

This design stays inside the public value budget. It avoids the common failure of exposing every internal component because a custom GUI has room for it.

## Decision and mission review

The crisis uses an ordinary decision category because the player manages one central value, several state targets, and a phase-based action set. Normal decisions, missions, map highlights, and a category picture can communicate this clearly.

The action set includes intelligence, finance, public services, legal status, constitutional settlement, arrest, security, and suppression. These actions affect distinct risks and do not reduce the category to spending political power for modifiers.

The category uses phase replacement, visible action limits, and active mission limits. This prevents a large event from turning into a permanent debug menu.

## Focus-tree review

The state package has five political routes because they represent real internal coalitions, not an ideology quota:

- personal religious authority
- federal separatism
- secular Black republicanism
- Originalist Black supremacy
- Diaspora Congress internationalism

Supporting branches address institutions, economy, defense, diplomacy, intelligence, integration, and the International. Political decisions alter route access and country identity. Each route has costs and late-game consequences.

The architecture is large enough for a long-lived state without requiring every foreign movement to receive an entirely bespoke tree. Foreign states use a shared regional structure with module-specific content, identity, decisions, leaders, and AI.

## Country-package review

The American anchor state receives the full package because it is the event's durable playable actor. It has state-formation logic, territory packages, government, ideas, economy, forces, reinforcement, diplomacy, routes, formables, and AI.

Foreign breakaways receive smaller but valid packages. They should not inherit all American institutions or one generic flag. Their starting problem and route identity come from the local module.

The state is human and remains inside ordinary civilian systems. This avoids a routing error that could exclude it from famine, migration, occupation, or population mechanics.

## Historical and doctrinal review

The Detroit opening, institutional development, surveillance conflict, and separate-territory demand have historical grounding. The wider evolution uses interwar Black internationalism as a field of competing movements rather than as one unified Yakubite tendency.

The design separates Yakubite theology from mainstream Islam. It avoids assigning fictional extremist allegiance to real historical figures. The research notes require final verification for names, dates, slogans, quotations, organizations, and religious terms.

The event treats the racial creation narrative as doctrine. The Original Supremacy route openly embraces Black supremacy, while objective narration records it as an authoritarian extremist ideology.

## Supremacist-route review

The user asked for an explicit Black supremacist route. The design includes it as a complete political state path with citizenship, education, loyalty, security, International control, opposition, repression, Condemnation, sanctions, member defection, and reform possibilities.

Its strength comes from mobilization, centralized command, coercive administration, and ideological discipline. Its costs come from resistance, isolation, economic weakness, institutional rigidity, dissent, and bloc fragmentation.

The route has no racial biology mechanic and no race-targeting action. This keeps the game focused on government and political systems while preserving the route's stated ideology and consequences.

## International review

Foreign chapters can adopt, adapt, cooperate, reject, or oppose. The regional modules preserve local religious, civic, labor, colonial, parliamentary, and anti-colonial politics.

The International requires viable participants and can take several forms. Cohesion allows common institutions without assuming automatic unity. Membership states, suspension, exit, and schism give local actors agency.

The target system needs careful bounded scripting. It should use registered active hosts and explicit selection jobs instead of broad daily world scans.

## Terminal-route review

The Yakubite World is a true terminal branch because it reorganizes the campaign around a global replacement order. It is not a reward for reaching 1000 Chaos.

The readiness contract requires state capacity, International capacity, leadership, and footprint. Multiple paths can prove readiness. This supports federal, revolutionary, congress, conquest, and multi-state campaigns.

The terminal route retains internal differences. Its route variants change supporting-state logic, member treatment, mobilization, victory, and aftermath. The supremacist variant is one possible terminal order, not the required conclusion of every Yakub-derived route.

## Scenario review

The proposed scenario ID `SCN-015` follows the current export sequence and avoids filling the missing `SCN-004` identity. Implementation must still verify the live registry and authoritative workbook before locking the ID.

Movement type preserves a campaign arc at every intensity. World Order type begins the final conflict directly. Intensity changes setup depth and geography rather than only adding flat modifiers.

The scenario plan includes bypass cleanup, duplicate prevention, valid actor creation, and route selection.

## Asset review

The asset plan requires a fictional high-chaos Yakub portrait, route flags, regional flags, report images, category art, separate icon families, achievements, International emblem, and two super-event packages.

No custom 3D unit or animation is required. This is a deliberate scope decision. The event's identity depends on political institutions, reports, flags, portraits, and route visuals. Custom models or animated overlays would add maintenance burden without improving the core decisions.

## AI and balance review

The design defines distinct American government approaches, foreign government approaches, state routes, member behavior, and terminal behavior. The named probability scenarios create a measurable audit plan.

The strongest balance risks are:

- martyr feedback causing unstoppable Influence
- negotiated statehood becoming the always-correct American choice
- a tiny state receiving excessive free military power
- foreign modules overwhelming the event queue
- supremacist mobilization becoming stronger than every other route
- International aid producing unlimited equipment or volunteers
- terminal uprisings creating infinite forces

The balance and acceptance files provide direct checks for each risk.

## Cross-system review

Connections are included only where they change play. Depression affects grievance and recruitment. Murder Mystery can alter succession. Famine and Migration use shared adapters. Condemnation and Deaths receive supported consequences. Liberation events can read state and International outcomes.

The event does not duplicate generic Chaos sources. Event-owned Chaos changes attach to concrete milestones, failures, spreads, settlements, and terminal acts.

## Improvement-loop stop condition

Broad design expansion should stop here. The event has a complete crisis loop, outcomes, three evolutions, a playable country, five routes, regional modules, an International, a terminal branch, succession, a manual scenario, achievements, AI, assets, writing direction, balance cases, probability scenarios, and acceptance criteria.

Further broad additions would likely create bloat. In particular, the following should not be added during implementation without a new accepted design decision:

- a racial demographic system
- more persistent public meters
- a full scripted GUI
- custom 3D units
- a dedicated foreign tree for every affected country
- several separate International factions before a real schism
- multiple public world-end rows for route variants
- additional evolutions beyond the accepted three
- a cluster assignment
- a super-event for every stage

A second improvement pass is justified only after implementation reveals a new design gap that this package does not cover. Small implementation questions belong in audits and handoffs.

## Remaining implementation risks

The specification does not choose an exact carrier tag, exact state IDs, exact focus IDs, final variable names, final script constants, final modifiers, final AI numeric weights, final event images, final flags, final portraits, final quotes, or final music. Those decisions require repository inspection, installed vanilla references, MCP evidence, provider work, or source verification.

The implementation must also confirm which existing United States content can coexist with a state breakaway, how civil-war armies are divided safely, and how regional population or discrimination evidence can be approximated with available HOI4 state and country data. These are implementation tasks, not missing design routes.

## Planning verdict

The design is ready for implementation planning. It is complete as a source specification package and does not use a reduced fallback version of the user's concept. It does not claim code, assets, MCP runs, workbook edits, or live testing.

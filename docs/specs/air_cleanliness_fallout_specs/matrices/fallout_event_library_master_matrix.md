# Fallout Event Library Master Matrix

Working labels are not final localisation.

## Library size

The release floor is 660 unique, manually reviewed Fallout event blocks. The full planned range is 660 to 910 blocks. Expansion above the release floor is allowed only when the added blocks have distinct eligibility, choices, effects, AI behavior, memory, follow-up, cleanup, and presentation.

The matrix separates event blocks from design anchors. One anchor can require several blocks for opening, choice, delayed result, failure, and callback. One event block has one primary ownership family even when it changes several systems.

| Primary family | Planned blocks | Mapped design basis | Eligible scope | Main time window | Core job |
| --- | --- | --- | --- | --- | --- |
| Transition and orientation | 20 to 30 | One request flow, blackout handoff, continuation, two to four country orientation popups | Every playable country | Ash week | No ordinary scheduler traffic until closed |
| Global survival and society | 70 to 90 | 58 mapped anchor families | All normal successor governments | Ash week onward | Food, water, medicine, shelter, power, salvage, family, law, culture |
| Regional and biome | 90 to 120 | 108 mapped anchor families | Nine broad regional pools | First month onward | Geography, food ecology, climate appearance, routes, infrastructure |
| Government archetype | 120 to 160 | 120 mapped anchor families | Twelve archetypes, ten anchors each | Opening through Year 10 | Institutions, legitimacy, coercion, citizenship, route change |
| Successor country memory | 190 to 260 | 99 candidates with four linked arc obligations | Spawned selected successor only | Opening through Year 10 | Unique founding memory, domestic conflict, external partner, late identity |
| Character and leader | 50 to 70 | 30 recurring role blueprints | Countries with matching institution and capacity | First month onward | Advisors, leaders, commanders, loyalties, trials, succession |
| Diplomacy, trade, war, settlement | 45 to 65 | 57 mapped anchor families | Contacted countries and active corridors | First contact onward | Recognition, compacts, trade, raids, wars, armistices, integration |
| Cause memory and altered fiction | 35 to 55 | 36 cause-memory plus 31 fictional altered anchors | Cause-qualified and route-qualified countries | Opening through late game | Cause-specific memories, fictional altered societies, ecology |
| Recovery and late world order | 40 to 60 | 49 mapped anchor families | Qualified countries and connected regions | Year 2 onward | Thaw, rebuilding, constitutions, generations, blocs, Year 10 ambitions |

## Release floor composition

The floor is reached only when all of the following are true:

- transition and orientation are complete for every playable continuation path
- all global survival systems have incident, crisis, competence, recovery, and failure coverage
- each of the nine regional pools has at least eight implemented anchors
- each government archetype has at least eight implemented anchors and one late institutional outcome
- every selected successor has an opening chain, domestic chain, external chain, and late identity chain
- recurring character arcs can change gameplay roles and do not remain decorative names
- contact, recognition, trade, refugee, border, war, peace, and settlement all have event support
- every supported Fallout cause has memory that affects play
- fictional altered content remains route-gated and explicitly fictional
- Years 5 through 10 contain new politics, relationships, and ambitions

## Ownership and id allocation

All event blocks belong to `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

No suffix range is reserved in this planning package. Implementation must scan the dedicated file, assign the next free suffix in each stable section, and record the allocation in a maintained event ledger.

The event file should be physically divided by clear comments into the same primary families used here. Large families may use helper files for scripted effects, triggers, constants, and scripted localisation, but Fallout event definitions remain in the dedicated event file unless local engine proof establishes a stronger event-file split that still uses the Fallout namespace and ownership.

## Anchor-to-block conversion

A standard major anchor usually becomes four to seven event blocks:

1. opening or discovery
2. first public or internal choice
3. delayed complication
4. success, partial success, or failure
5. institutional or character consequence
6. later callback
7. optional regional or route variant

A routine anchor usually becomes one to three blocks:

1. incident
2. delayed result or escalation
3. optional callback

A bilateral anchor usually becomes three to six blocks because each side needs invitation, response, failure, and memory behavior.

## Campaign density

The library size must never become a popup quota. The scheduler uses phase, country size, active arcs, family fatigue, state eligibility, bilateral reservations, and player-facing cooldowns. Human countries normally receive 90 to 180 meaningful visible events over ten years.

Hidden AI resolutions are allowed when the same incident needs to affect AI countries without creating player popups. Hidden resolution must use the same mechanical logic and memory as the player-facing path.

## Content uniqueness rule

An event is unique when its eligibility, conflict, choice, effects, or future memory differ materially. Changing only the country name, state name, or flavour noun does not create a unique event.

Country overlays can share a mechanical helper, but the event conflict and consequences must reflect that country's founder institution, state classes, resource profile, government archetype, regional role, and external behavior.

## Minimum cross-system coverage

The final library must collectively change:

- food, water, medicine, salvage, power, shelter, radiation burden, and survival cohesion
- population, displacement, civilian deaths, state categories, buildings, infrastructure, supply, and local damage
- government legitimacy, coercion, citizenship, corruption, faction balance, leaders, advisors, and commanders
- decisions, missions, focus branches, idea lifecycles, country identity, flags, and AI plans
- contact, recognition, trust, trade, corridors, compacts, war causes, war exhaustion, peace, and integration
- winter phase, visible climate class, adaptation, recovery, thaw, and late climate hazards

## Audit rule

Completion auditing must count real event blocks by primary family, then sample chains for depth. Raw block count cannot compensate for missing successor coverage, shallow choices, missing AI, missing effects, repeated text structure, or absent late-game content.

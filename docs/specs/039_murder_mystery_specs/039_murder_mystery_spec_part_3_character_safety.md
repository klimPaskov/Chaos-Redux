# Murder Mystery Specification Part 3: Character Safety and Succession

## Safety principle

Event 39 can remove important characters only through a verified ownership and succession contract. Character loss is part of the event premise, but broken rosters, missing leaders, duplicated characters, invalid focus routes, and damage to unrelated event systems are unacceptable.

The system must decide whether a character is safe before selecting that character as a target. It must not remove a character first and then try to repair the country.

## Character disposition registry

Every character that Event 39 may target has an explicit disposition row. The row identifies the character token, normal owner or owning roster, eligible roles, valid date or country contexts, successor or replacement requirements, protected dependencies, current transfer state, Event 39 result, and cleanup behavior.

Allowed dispositions are:

- `eligible_named_target`, which allows a real character death after all current-state checks pass
- `eligible_opening_leader`, which allows the opening murder and names the safe succession route
- `generic_office_only`, which forbids character removal and lets the event report a generic office casualty
- `temporarily_protected`, which blocks selection while an owning focus, decision, event, transfer, or roster state is active
- `permanently_protected`, which blocks Event 39 in every state
- `owner_managed`, which allows removal only through a callback from the character's owning system
- `already_removed`, which prevents duplicate targeting and clears stale pool membership

An absent row is not permission. Unregistered characters default to `generic_office_only` or are excluded entirely.

## Required ownership audit

Before implementation, search the complete repository, installed vanilla, and approved reference context for every candidate name, identifier, portrait, character token, advisor token, corps role, history assignment, focus reference, decision reference, event reference, idea reference, scripted localisation reference, and country transfer.

The audit must distinguish live character ownership from incidental text. A name mentioned in prose is not proof of runtime ownership. A character used by a live roster, focus unlock, advisor system, commander grant, civil war, country transformation, or another Chaos event is protected until its owning system explicitly supports Event 39 removal.

## Opening leader gate

The sitting leader can be murdered only when the transaction has all of the following:

- current leader resolved to a stable token or verified generated-leader record
- explicit `eligible_opening_leader` disposition
- one safe successor or one safe institutional replacement already prepared
- successor is not simultaneously active as another country's leader
- successor portrait, name, ideology, party, gender metadata, and country ownership are valid
- focus tree, decisions, ideas, and history do not require the murdered leader to remain active without an alternate path
- leader removal will not break a route that the player has already committed to
- event and country scopes remain valid during the transition
- no unrelated Chaos system has a stronger ownership claim

If any requirement fails, the country is invalid as the opening host. The event should select another country. A generic report that a senior official died cannot substitute for the required opening leader murder because that would change the event premise.

## Succession routes

### Historical or current roster successor

Use an existing country character when the roster already defines a lawful or plausible successor and the character is not active elsewhere. The route should preserve ideology and government unless the country's existing succession logic says otherwise.

### Route-aware successor

If the host has already completed a political route, select from successors compatible with that route. A democratic government should not receive an unrelated autocratic replacement merely because the character exists. A monarchy, military government, revolutionary council, exile government, or event-created polity should use its own verified succession family.

### Institutional emergency replacement

An institutional council, acting cabinet, regency, military committee, or collective presidency is allowed only when the country is grounded and authentic institutional source material or existing repo presentation can support it. It must not invent a fake real person. It is a valid fallback for a generated or dynamic leader whose individual successor cannot be safely represented.

This route requires its own character or country leader package, localisation direction, portrait source classification, duration, transfer back to normal leadership, AI behavior, and focus compatibility. It is prepared before host selection. It cannot be improvised after the murder.

### Generated ordinary leader

A generated ordinary leader may be used only when the engine and existing country package already use generated leaders safely and no grounded portrait or named identity is being invented. The spec does not authorize generated portraits for grounded real people.

## Target role pools

### National leadership

This pool contains later heads of state or government only when a second safe succession can be proven. It should have the longest cooldown and highest protection priority. Repeated national leader murders are rare outside Evolution V.

### Army command

This pool contains eligible generals and field marshals. The system must preserve a minimum command reserve. It may not remove all commanders, all field marshals, or the only commander required by another event. It should consider current assignment, skill, visibility, protection, and whether the commander is already wounded, captured, retired, or transferred.

### Naval command

This pool contains eligible admirals. Landlocked countries or countries without valid admirals use no named naval target. The event may report a generic naval office casualty only when a naval institution exists.

### Cabinet and political advisors

This pool contains eligible advisors, ministers, theorists, and high command. A candidate is blocked while required by a focus, idea lifecycle, active decision, balance of power, country transition, or another event. Removing an advisor must also remove or disable its recruitment and active assignment safely.

### Intelligence personnel

This pool represents agency leadership, operatives, security officials, and investigators. Named operatives can be targeted only through a verified operative ownership path. Generic intelligence casualties should be common because HOI4 does not expose every agency official as a character.

### Judiciary and administration

This pool normally uses generic office casualties because judges, prosecutors, senior civil servants, and local officials are not consistently represented as characters. Their deaths can affect evidence, stability, compliance, investigation capacity, and public order without deleting a roster token.

### Event 39 investigators

Event 39 may create one or more investigation officers or institutional case teams. A grounded country should use an institutional presentation unless a sourced real person is explicitly added. Fictional high-chaos Assassin personnel may use generated portraits through the portrait worker. Investigator loss affects Case Progress and witness safety but does not break the category.

## Murder selection sequence

1. Determine whether an incident is eligible from pacing, cooldown, and current phase.
2. Select an office group from dynamic weights based on exposure, recent protection, movement goals, current war, and evolution.
3. Build the current safe named target pool for that office group.
4. If the pool is empty, decide whether a generic office casualty is valid.
5. If neither exists, cancel the murder and convert the incident into surveillance, attempted attack, or discovered plot content.
6. Resolve protection before applying death.
7. Apply the named removal or generic casualty effect through the owning helper.
8. Record role, character when present, country, date, responsible cell, public knowledge, deaths contribution, and cooldown.
9. Update Case Progress, Network Reach, target protection, Condemnation only when a mapped public atrocity or cover-up source exists, and Chaos only through the event-specific consequence map.
10. Update event, report, and news presentation without revealing protected registry state.

## Protection and failed attacks

A protected target may survive, be wounded, be evacuated, or expose the attacker. The result should depend on protection level, agency capacity, cell maturity, selected method, and the target's office group.

Failed attacks are meaningful content. They can increase Case Progress, expose a safe house, strengthen public resolve, reveal an infiltrated guard, or allow the cult to build mythology around the attempt. A failed attack must not be treated as no event.

## Character removal effects

A named death helper must perform all owner-approved cleanup in one bounded transaction. Depending on role, this can include:

- remove or retire the character from active country ownership
- disable recruitment paths that cannot remain valid
- release command assignment safely
- update advisor or high-command availability
- clear Event 39 target flags
- create a replacement or vacancy state where needed
- update portrait or office presentation
- notify the owning system through its callback
- record the death in Event 39 history and the shared deaths system when the source represents actual population loss

The helper must not clear unrelated global targets or broad character state.

## Protected categories

The following are blocked unless their owning system explicitly provides a safe removal callback:

- leaders and characters owned by special Chaos countries
- actual nonhuman leaders and nonhuman government actors
- leaders required by active world-end routes
- event-created leaders whose removal would break their parent event
- characters in the middle of a transfer, exile, civil war, return, or succession transaction
- unique characters required by a focus tree with no alternate route
- characters that act as hidden ledgers, scripted GUI actors, or system identifiers
- historical leaders whose country has no safe current replacement
- temporary duplicate character representations used for portraits or roster transitions
- characters already dead, retired, captured, or removed

## Caps and cooldowns

Each country has an incident cooldown, each office group has a role cooldown, and each named character can be targeted only once. The baseline should allow long quiet periods. Evolution I shortens the incident cooldown. Evolution II allows parallel countries but preserves one active murder incident per country. Evolution V can create coordinated waves, but each country still processes a bounded target count per wave.

A country must retain:

- one functioning national leader or institutional replacement
- a minimum viable army command pool when it fields an army
- a minimum viable navy command pool when it has a navy
- at least one route to recruit or generate future command staff
- required advisors and system characters owned by unrelated content

## Generic office casualty design

Generic casualties prevent unsafe character deletion while preserving the crisis. They should name the office type and visible consequence, not invent a person. Examples include a cabinet secretary, regional prosecutor, naval staff officer, intelligence section chief, railway security director, or local judge.

Generic office casualties can reduce investigation capacity, disrupt command, damage stability, expose routes, add tracked deaths, or change protection priorities. They must not be presented as a named character portrait.

## Foreign cells and character safety

Secondary countries use the same registry and stricter named-target threshold. Their investigations are easier and their named character losses should be less frequent. A newly seeded cell should normally begin with attempted attacks, generic office casualties, or one protected-role crisis before it can target a named leader.

Foreign territorial revolts must transfer only characters explicitly assigned to the derivative package. They cannot steal the parent country's protected roster. The foreign Assassin administration should begin with a fictional institutional leader or generated high-chaos leader package, not a copied real person.

## Evolution V leadership removal

World of Anarchy does not mean deleting every character token in the game. It means dismantling ordinary government leadership as countries fall. The conquest transaction should remove or retire a curated safe set of leaders and offices, transfer protected survivors where their owning systems require it, and replace the government with an Assassin administration.

Large-scale processing uses office groups and owner callbacks. It respects country-level caps, prevents duplicate death records, and never removes special Chaos or nonhuman actors through ordinary human logic.

## Character aftermath

A resolved country may gain memorial, succession, veteran investigator, reformed security, politicized command, or institutional trauma outcomes according to its losses and response philosophy. Memorial content should use the murdered office and role history without exposing hidden registry details.

A government that protected every later named target after the opening murder can qualify for a difficult achievement. A government that used baited targets, tolerated exposed offices, or accepted a high number of preventable deaths should receive different aftermath and cannot qualify.

## Acceptance criteria

Character handling is accepted only when every possible named target has an explicit disposition, every opening host has a verified successor transaction, every protected owner has been audited, no unregistered character can be deleted, role caps preserve viable rosters, duplicate targeting is impossible, generic office casualties cover unsafe roles, and all active transfers, deaths, replacements, and cleanups survive save and reload.

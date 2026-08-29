# Event 31 Random Terror improvement-loop review

## Review role

This review applies the Chaos Redux improvement loop to the completed Event 31 specification.

The purpose is to test whether the event promise has become a playable, connected, readable system and whether another broad expansion would improve play or create bloat.

The review was performed manually from the supplied improvement-loop and subagent contracts.

The project subagent definitions were fully read, but this environment did not expose the Codex subagent-spawn interface. No subagent execution is claimed.

## Playable promise

The event promises fear, disruption, government choice, escalation, territorial rupture, ideological transformation, and a possible terminal global war.

The strongest version of that promise requires the player to understand three questions at any time.

1. Where is the crisis active?
2. How close is the government or movement to losing control?
3. Which action changes the next important risk?

The completed specification answers those questions through Terror Pressure, Response Legitimacy, the state activity ladder, limited missions, exact state targets, and actor-specific territorial values.

## Gaps found in the initial brief

### The response system could become a permanent decision wall

The original idea included police, intelligence, military, checkpoints, raids, hostages, restrictions, sponsors, smugglers, coups, territory, foreign intervention, and global networks.

Showing all of those actions at once would create a debug menu.

### Baseline escalation and evolutions could overlap

The brief correctly allowed baseline coups, civil wars, and temporary countries.

Without a clear split, Evolution III could duplicate that content or make baseline escalation meaningless.

### The jihadist branch could erase every other organization

The late evolutions could turn all Event 31 actors into one religiously framed movement.

That would reduce replay value and undermine the brief's representation rule.

### Muslim opposition could remain a disclaimer

A line stating that ordinary Muslims oppose the movement would not be enough if the game gave them no events, decisions, AI, resistance, or diplomatic role.

### Territorial actors could become empty tags

The brief required countries, divisions, leaders, decisions, and political identity.

Without a full package, a spawned actor could appear with generic units, no economy, no reinforcement, and no route.

### The world-end branch could become one fixed extreme modifier

The requested final state needs extreme power.

A permanent modifier with no objective-based counterplay would create a simple annexation grind and would fail to justify a terminal system.

### The manual scenario could become a flag setter

Activating Evolution IV without building territorial actors, cells, wars, government tools, and AI would not create the promised scenario.

### Victim support could become flavor

Deaths, damage, and displaced civilians were central to the brief, but a military-first implementation could leave victim support as a small legitimacy button with no strategic value.

### Cross-event hostility could remain an opinion modifier

The Cannibalism connection needs real rivalry, incidents, AI, diplomacy blocks, and territorial competition.

## Improvements accepted into the specification

## Compact phase-based response

The government category exposes three to five current actions and no more than three missions.

Actions are replaced by phase instead of accumulating.

One selected state or corridor receives detailed targeted actions.

This preserves depth without overwhelming the player.

## Two national values and one state ladder

Terror Pressure is the primary national value.

Response Legitimacy changes operation quality, recruitment, defections, and recovery.

The state ladder shows local progression from dormant contacts to lost local control.

Later global and actor values appear only when their systems become active.

## Baseline and evolution separation

Baseline can reach territorial actors, coups, civil war, partition, takeover, surrender, and defeat.

Evolution III makes territorial actors more durable, coordinated, and internationally connected.

It does not reserve ordinary state loss for late Chaos.

## Organization diversity

Organized Cells can produce military splinters, revolutionary absolutists, criminal-political networks, millenarian cults, fictional ultranationalists, and other invented profiles.

Evolution IV introduces one fictional jihadist current.

Compatible actors can join, reject, or fight it.

The later movement does not overwrite every Event 31 actor.

## Mechanically meaningful Muslim opposition

Muslim governments, communities, soldiers, clerics, and fictional religious councils can protect sites, reject the movement's claim, improve legitimacy, support defections, lower recruitment, reduce International Unity, and fight the faction.

Muslim-majority status enters only the later actor-specific opposition and enemy-priority system.

It never enters ordinary vulnerability or recruitment.

## Full territorial country package

Every durable actor has valid territory, capital, origin, fictional identity, leader, flag, ideas, values, forces, technology, economy, focus routes, decisions, reinforcement, diplomacy, AI, and cleanup.

Starting forces and technology come from real territory, parents, defectors, stockpiles, production, and sponsors.

## Objective-based world-end power

The False Revelation state receives extreme strength through Presence of the Entity, World in Revolt, and Supply Through Ruin.

Those systems respond to command capitals, corridors, high-pressure countries, International Unity, territory, and defections.

The coalition can weaken the final state through several strategic objectives.

## Transactional manual scenario

Global Jihad validates the map, allocates actors, seeds crises, activates advanced network values, creates government tools, and clears its bypass after setup.

Each intensity and deployment type creates a distinct world state.

Maximum activates the Final Jihad but preserves the normal world-end gate.

## Victims as gameplay

Victim support and service restoration affect legitimacy, intelligence, recruitment, copycats, recovery, relief corridors, achievements, and aftermath.

Government-caused civilian deaths receive separate tracking and consequences.

## Cannibal rivalry as a full interaction

The two movements cannot ally, merge, join the same faction, exchange support, or become natural partners.

They receive border clashes, raids, competition, defections, AI hostility, and separate Deaths and Condemnation attribution.

## Asset scale aligned with dynamic country count

The specification plans a large fictional leader and flag pool, route-specific icon families, state-stage visuals, two super-events, and one optional terminal portrait animation.

It limits advisor portrait authorization to meaningful roles.

## Additions considered and rejected

### Custom Event 31 combat unit

Rejected.

Existing infantry, militia, mobile, artillery, engineer, reconnaissance, and logistics structures can express the actor's forces.

A custom unit would add Event 19 callbacks, equipment, counters, sound, 3D model, animation, and validation without creating a distinct combat role.

### Custom 3D models

Rejected.

The event does not own a creature, vehicle, building, aircraft, ship, or unit that needs a unique map model.

### Permanent custom mechanic window

Rejected.

The government system has two visible values, a state map mode, and phase-limited actions.

The territorial actor has three values in a normal category.

A full window would duplicate normal decisions and create unnecessary UI maintenance.

### Separate focus tree for every spawned actor

Rejected.

A shared framework with origin, route, region, profile, and actor-specific text gives more reliable depth and supports many simultaneous countries.

The shared tree still needs route-specific AI, targets, leaders, flags, rewards, and localisation.

### Broad advisor roster

Rejected.

Only route-critical fictional characters are authorized.

Decorative advisors would add portrait and localisation work without changing play.

### Regional historical formables

Rejected.

Event-owned mergers, takeover, confederation, the Jihadist International, and the final state already provide territorial ambition.

Unrelated formables would dilute the event and create identity conflicts.

### New ideology family

Not accepted as a default.

The implementation should first use existing ideology and subideology infrastructure with event-owned identities.

A new ideology family is justified only if live repository inspection proves existing politics cannot represent the actors safely.

### Tactical attack-planning simulation

Rejected.

The event models incident outcomes, targets, protection, networks, and strategic consequences.

It does not model real attack preparation, evasion, or recruitment techniques.

### Real organizations or symbols

Rejected.

Every movement, leader, flag, emblem, and claim remains fictional.

### Sacred Islamic media as hostile presentation

Rejected.

The False Revelation cannot use Quran recitation, the call to prayer, sacred chant, Quranic calligraphy, or a depiction of Allah as enemy branding.

### Free nuclear, missile, chemical, or biological access

Rejected.

Event 31 actors can use those systems only through actual technology, equipment, payload, sites, delivery routes, capture, and owning-system consequences.

## Clarity review

The design stays within the decision-system budgets.

- one primary national value
- one supporting national value
- one five-stage state ladder
- no more than six primary decisions in one phase
- no more than three missions
- no action with more than four spendable cost types
- three actor values shown only to territorial countries
- two late global values shown only after their evolution
- one hidden readiness value

No new GUI is needed to explain these values.

## Replay review

Replay value comes from:

- different selected countries and states
- organization profiles
- leadership routes
- sponsor types
- government response choices
- network spread
- territorial origin
- actor mergers and splits
- jihadist acceptance or rejection
- scenario deployment types and intensities
- world-end readiness and counterplay

The design does not rely on one random rare event to create variety.

## AI review

Every player action family has an AI equivalent.

AI plans cover governments, cells, territorial actors, leadership routes, jihadist priorities, scenario setup, final command, coalition behavior, and invalid routes.

The specification supplies named probability scenarios and paired identity-fairness tests.

Implementation evidence remains required.

## Asset review

Every visible country identity has a source mode and asset family.

Every portrait is fictional or institutional.

Every flag uses the flat ImageGen workflow.

The final entity animation has a static fallback and real source-frame requirement.

Separate icon families remain separate.

Super-event text and audio remain research-gated.

## Closure decision

The design loop should stop after this package.

Another broad expansion is not recommended before implementation.

The current design has:

- meaningful player choices
- baseline and evolved progression
- compact presentation
- country play
- route identity
- AI intent
- cross-event behavior
- asset coverage
- achievements
- scenario play
- terminal counterplay
- aftermath

Further additions would likely create duplicate decisions, more visible values, excessive country variants, unnecessary assets, or additional systems that do not improve the core event.

## Remaining implementation decisions

The following are implementation gates, not missing design depth.

1. Verify `SCN-014` in the authoritative workbook and live registry.
2. Verify the proposed Cluster `9` identity before future registration.
3. Audit the protected country-carrier pool and simultaneous actor limit.
4. Inspect the current Event 31 placeholder and pre-fire actor pipeline.
5. Choose the exact event-owned state map-mode implementation from live precedents.
6. Build and render the exact focus tree count and layout.
7. Verify technology-union behavior and every affected technology graph.
8. Research final super-event titles, quotes, remarks, images, and licensed audio.
9. Verify the entity portrait or overlay consumer before animation production.
10. Run baseline and comparison probability audits.
11. Run the required event, decision, focus, country, localisation, and completion audits.
12. Align the authoritative workbook and export the CSV snapshots.

## Improvement-loop verdict

Broad expansion is closed.

Implementation should follow the completed specification, resolve the listed gates, and use a later improvement pass only after a meaningful implementation tranche exposes a new design problem that is not covered here.

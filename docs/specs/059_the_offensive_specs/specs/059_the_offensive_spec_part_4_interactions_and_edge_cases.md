# Event 059: The Offensive

## Part 4: Interactions, lifecycle, and edge cases

## Event lifecycle

The event has a compact lifecycle with a long campaign effect.

1. Event 059 is selected normally or enters through the Diplomacy cluster.
2. The global activation state is set once.
3. The one-time manifestation adds its bounded Chaos amount.
4. Every human player receives the activation report.
5. Every AI-controlled eligible country begins using the baseline layer.
6. Enabled evolutions already eligible at first firing join through the pre-fire evolved opening.
7. Later enabled evolutions enter through their MTTH paths as Chaos rises.
8. New and released AI countries inherit active layers.
9. Human takeover suspends the behavior for that country.
10. AI handback restores the active layers.

The event has no ordinary repeat loop. All later change comes through evolution, control state, country creation, and normal campaign conditions.

## Relationship with ordinary AI behavior

The event should add pressure to existing AI priorities. It should not replace the full strategic identity of a country.

Country focus routes, event-owned target rules, subject relationships, faction plans, scripted historical objectives, and special actor behavior remain valid. Event 059 changes willingness, concentration, persistence, and risk only where the country has a legitimate action available.

When a country has no valid attack, claim, war goal, intervention reason, invasion route, or useful front, the event can remain dormant for that country. A country does not need to manufacture activity merely to prove the event is active.

## Cross-event interaction principles

Event 059 should connect to other events through campaign state and a small number of explicit hooks. It should not create recursive firing, duplicate other events, or add a special case for every catalog entry.

### War-generating events

Events that create wars give the offensive posture new theaters to use. Event 059 should improve AI conduct inside those wars without refiring the source event or adding duplicate declarations.

Relevant examples include:

- Random War
- Fury
- Third Balkan War
- Allies Backstab
- civil-war and liberation events that create active fronts

The interaction should be strongest through front selection, reserve use, air allocation, logistics, and viable naval operations.

### Diplomatic-pressure events

Events that create claims, faction pressure, guarantees, hostility, or war goals provide valid strategic opportunities. Predatory Powers can give those opportunities more weight.

Relevant examples include:

- Tensions Rising
- A Faction Comes Calling
- The Great Embargo
- Subjects Break Free
- other events that create legitimate claims, interventions, or faction obligations

Event 059 must not turn flavour hostility into a war path when the source event did not create one.

### Intelligence events

Intel Leaked can make a target appear more exposed. When the leaked information is available to an AI country, the opportunity and front-scoring layers can place more confidence in known weakness, mobilization gaps, industrial strain, or an exposed navy.

The interaction should use the intelligence advantage already created by the event. It should not duplicate the intelligence effect or reveal hidden data to a player.

### Military abundance and preparation events

Events that provide equipment, ships, infrastructure, research, or economic capacity can move a country above an offensive feasibility threshold.

Relevant examples include:

- The Navy
- The Great Infrastructure Project
- Gift from Scientists
- Industrial Boom
- The Black Market

These events should not receive direct Event 059 bonuses. Their ordinary material effects can make a previously impossible operation viable.

### Economic and research setbacks

Events that reduce military production, research, fuel access, or industrial capacity should make the AI scale back, delay, or narrow its offensive plans.

Relevant examples include:

- The Great Embargo
- Great Depression 2.0
- Return to Peacetime
- Research Failure
- natural disasters that damage supply or production

The aggression envelope must react to the resulting material state. Event 059 cannot force a country to behave as if those losses did not happen.

### Peace events

White Peace and other settlement events retain authority over the wars they end. Event 059 does not block peace effects.

After peace, the global posture remains active. A fresh declaration still needs a valid path and should not occur immediately as an automatic reversal of the settlement.

### Liberation and country-creation events

Subjects Break Free, Independence Wave, civil wars, restored countries, and other creation systems can add countries after Event 059 has fired.

Every new ordinary AI country should receive the active layers through the chosen declarative or event-driven registration architecture. Newly created player countries remain under human control and do not use the layers until returned to AI.

### Special Chaos actors

Fury states, undead actors, anomalous countries, and other special actors often have strong owner-specific targeting and expansion rules.

Event 059 must use a compatibility rule:

- hard owner restrictions always win
- compatible generic offensive behavior can improve execution
- Event 059 cannot add forbidden targets
- Event 059 cannot make a contained or dormant actor active before its own event allows it
- Event 059 cannot replace special force-production logic with generic ratios

## Diplomacy cluster interaction

### Membership

Event 059 is a High-severity member of the Diplomacy cluster.

The accepted cluster update fixes the membership and severity but does not create a special event-specific member role or chance. The implementation must inspect the authoritative aligned member arrays and use the current Diplomacy defaults for required or optional role, participation chance when relevant, and member minimum tier. The old Diplomatic Panic name must not survive as a second cluster.

### Anchor firing

When Event 059 is selected as the anchor:

- its normal event eligibility has already passed
- the cluster can include eligible Diplomacy members
- Event 059 activates exactly once
- the cluster counts as one global pacing event
- each included member keeps its own history and effect

### Member firing

When Event 059 joins another Diplomacy anchor:

- it must still be unfired and enabled
- its minimum Chaos level must be met
- it uses the same activation, report, evolution, and Chaos logic as a normal firing
- it becomes permanently unavailable after the cluster resolves

### Cluster exclusions

Event 059 should be skipped as a member when:

- it has already fired
- it is disabled
- its event level is unavailable
- a terminal campaign state blocks ordinary event firing
- the cluster resolver has already committed the same event ID in the current incident

### Cluster Chaos accounting

The cluster itself should not add another Event 059 premium. The one-time manifestation is the only event-owned direct gain. Companion wars, casualties, annexations, and other outcomes feed the shared Chaos systems through their own sources.

## Multiplayer behavior

### Global state

The activation and evolution layers are global. Every player sees the same campaign state.

### Player reports

Each human player receives the activation report and later active-event evolution reports. The report should not be restricted to the country that happened to be the local event scope.

### Country control

- a human-controlled country never uses the event's AI choices
- a co-op country counts as human-controlled
- hotjoining into an AI country suspends Event 059 behavior for that country
- leaving or handing the country back to AI restores all active layers
- observer mode does not prevent AI-controlled countries from using the posture

### Desynchronization protection

The event should use deterministic global state and native AI evaluation. It should not rely on unsynchronized local variables, player-only random rolls, or local periodic loops.

## New country and tag transition behavior

The implementation must cover:

- newly released countries
- civil-war breakaways
- countries restored by event or decision
- countries created through Independence Wave and later liberation systems
- cosmetic tag changes
- ideology changes
- annexed tags that later return
- countries becoming subjects or independent

A cosmetic tag or ideology change should not lose the global strategy layer. A full country creation or restoration should receive it through the chosen registration path.

Annexed countries have no active behavior. If restored while the event remains active, they return with the current layers when AI-controlled.

## Subject and faction edge cases

### Subjects

Subjects can use the posture inside wars they legally participate in. They should not:

- justify or declare wars forbidden by autonomy rules
- ignore overlord call and command relationships
- open fronts that destroy the overlord's strategic plan without a strong local reason
- redirect production away from required subject or owner systems

### Faction leaders

Faction leaders can place more weight on:

- calls to arms
- intervention that protects faction survival
- opening a useful shared front
- finishing an isolated enemy
- supporting a threatened member

They should still consider faction-wide enemies and likely escalation.

### Faction members

A member should not join every war merely because the faction leader asks. Strategic value, distance, supply, homeland safety, subject status, and current wars remain important.

### Faction collapse and expulsion

After Allies Backstab or another expulsion event, former allies become ordinary valid enemies according to the new war and diplomatic state. Event 059 can make the remaining faction pursue the conflict more actively. It must not make expelled countries attack one another unless a separate war or valid objective exists.

## War and front edge cases

### No active war

Baseline behavior can prepare production, logistics, and valid objectives. It should not force a declaration without the Evolution II opportunity layer or normal country content.

### No valid enemy front

A country fighting only through naval or air access should use those valid channels. A land army should not receive meaningless front aggression with no land front.

### Encircled or isolated forces

The AI should prioritize restoring supply, escaping, or linking with friendly forces when feasible. The event should not treat an isolated pocket as a platform for a broad offensive.

### Collapsing homeland

Defense of the capital, core supply, and ports becomes the priority. Offensive layers can support a counterattack that directly relieves the crisis. They should not draw the last reserves into a distant objective.

### Enemy near capitulation

The strategic value of finishing the enemy rises. Evolution I and Evolution III should support sustained pressure when supply and replacement remain adequate.

### Long static fortified front

The event should seek concentration, logistics, air support, another axis, or a viable naval route. It should not solve a static front through repeated unsupported attacks.

### Front with severe attrition

Attrition, supply loss, equipment decline, and fuel failure should suppress broad attack. The AI can prepare repairs or a narrower operation.

### Multiple fronts

The country should rank fronts and assign a capacity budget. A major may support several. A minor should choose. Evolution III can add scale only after reserve and homeland needs are covered.

## Naval edge cases

### Island country without transport capacity

The AI can prioritize convoys, escorts, and preparation. It should not repeatedly plan an invasion it cannot execute.

### Naval superiority without supply access

Superiority alone is insufficient. The target needs a credible port or follow-up supply route.

### Strong landing without home defense

The landing should be delayed or reduced when it would leave the homeland open to an enemy invasion.

### Failed landing

A failed landing creates a reassessment period. The next attempt needs a changed target, improved escort, stronger force, better air support, or better supply.

## Production edge cases

### Equipment deficit

Replacement takes priority over expansion of offensive templates.

### Fuel collapse

Armour, aircraft, and naval operations should scale down. The AI can preserve them for decisive sectors or prepare fuel access.

### Research regression

If Research Failure removes access to equipment generations or supporting technology, the AI should use what it can produce. It must not keep a plan that depends on lost equipment.

### Return to Peacetime

Factory conversion and demobilization can make a planned offensive impractical. Event 059 remains active, but feasibility gates should reduce activity until the country rearms or finds a smaller plan.

### Sudden abundance

A large equipment or naval grant can raise capability quickly. The AI should still account for training, manpower, fuel, ports, supply, and command capacity before committing it.

## Player takeover during an operation

When a player takes control of a country during an active AI offensive:

- the game should stop evaluating Event 059 AI choices for that country
- no direct modifier should remain
- existing battle plans and unit orders remain ordinary game state that the player can cancel or change
- hidden Event 059 strategy state may remain dormant if required by the engine
- no popup or penalty should punish the player for taking control

When control returns to AI, the AI should reassess current conditions instead of blindly resuming an obsolete operation.

## Evolution activation during an operation

An active evolution should update willingness and priority without destroying current plans.

- Evolution I can reinforce and extend a viable operation
- Evolution II can add strategic opportunity evaluation outside the current war
- Evolution III can expand scale or add a second axis when capacity permits

An evolution must not instantly teleport units, create equipment, cancel player orders, or force a war declaration on the day it activates.

## Event disable state

Before firing, disabling Event 059 removes it from ordinary selection and cluster membership according to the shared event system.

After firing, the event's historical activation remains. The event enable toggle should not be treated as a rollback control for permanent AI state. Evolution toggles continue to govern whether unactivated evolution stages can occur.

## Save migration and old saves

When the rework is added to an existing save:

- an unfired Event 059 remains eligible according to the normal event system
- an old legacy firing flag, if one exists, must be mapped to the new active state without granting a second history row or Chaos gain
- old saves with an unclear legacy state should fail safely and avoid duplicate activation
- current Fire-Once weight and history must remain coherent

The implementation must inspect the existing event file and save-facing identifiers before choosing migration logic.

## DLC compatibility

The event must remain functional without optional DLC.

A behavior channel that depends on a DLC-specific system should be skipped or mapped to a base-game equivalent. The baseline front, war, production, and control behavior must remain available. Missing naval, intelligence, designer, or special-country features must not break activation or evolution.

## Performance and bounded evaluation

The event should rely on native AI evaluation wherever possible. It must avoid:

- a whole-world daily country loop
- a whole-world front scan written only for Event 059
- recurring state-by-state target searches
- repeated application and removal of the same strategy every day
- one event pulse per country for ordinary control checks

One-time activation, bounded country-creation hooks, native plan conditions, and existing shared on-actions are the intended tools.

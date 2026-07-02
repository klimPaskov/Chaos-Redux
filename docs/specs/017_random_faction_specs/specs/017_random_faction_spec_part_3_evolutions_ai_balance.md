# Event 17: Random faction evolutions, AI, and balance

## Evolution philosophy

The evolutions should be true mutation tracks, not ordinary baseline stages. The baseline event already chooses a minor and a faction. Evolutions change the meaning of that choice.

Each evolution has two entry paths:

- active-event evolution, where prior Event 17 pressure already exists and the new evolution changes current regional behavior
- pre-fire evolved opening, where Event 17 has not fired in the current campaign state but the first firing starts in a more intense form

The event uses three evolution stages. Evolution IV and Evolution V are intentionally unused for this design unless a later accepted plan adds a new diplomacy mechanic.

## Evolution I: Regional Bloc Race

### Design role

The first evolution changes the event from one isolated faction join into a local diplomatic race. One minor joining a faction makes nearby neutral minors reconsider their own position. Some try to copy the move. Others choose a rival faction to avoid being surrounded by one bloc.

### Unlock direction

Evolution I should become possible when at least one of these conditions is true:

- Event 17 has fired several times in different regions
- a region has two or more eligible neutral minors near faction members
- chaos has reached the first meaningful escalation tier
- world tension is already high enough that a new faction entry feels plausible
- the diplomacy cluster has recently fired related tension or panic events

### Active-event evolution

If a country joined a faction through baseline Event 17 and pressure memory still exists, Evolution I should:

- mark the region as a bloc race region
- select one nearby eligible neutral minor for a delayed follow-up
- give that minor a visible pressure event or mission
- let a rival faction leader react with propaganda, staff mission, or guarantee-style pressure
- update evolution logs with the selected region and actor when a concrete country receives the follow-up

### Pre-fire evolved opening

If Event 17 has not yet fired under the evolved state, the first firing can:

- select the initial minor normally
- immediately schedule one nearby neutral minor for a delayed reaction
- increase the chance that the second minor chooses a different faction
- apply a short regional pressure memory after the first alignment

### Player experience

If the player is the initial selected minor, they still must choose a faction. After the choice, a nearby neutral may react later. If the player is a neighboring neutral, they may receive a follow-up event or mission that asks whether to hold neutrality, copy the aligned neighbor, or seek a counterweight.

### AI behavior

- AI neighbors with similar ideology and good relations may copy the first country.
- AI neighbors that border the newly aligned country and fear encirclement should prefer a rival faction.
- Democracies and high-stability neutral governments should be more likely to resist pressure.
- Low-stability countries should be less able to resist.
- Aggressive AI faction leaders should pressure harder when the region is near a rival.

### Caps

Evolution I should not create a runaway chain. One baseline firing should schedule at most one delayed neighboring country response unless an event cluster explicitly expands it.

## Evolution II: Pressured Neutrality

### Design role

The second evolution makes neutrality feel militarized. Countries at war, countries bordering active faction enemies, and countries with frontier pressure can be drawn into faction choices. Joining a faction can now create direct strategic danger.

### Unlock direction

Evolution II should become possible when at least one of these conditions is true:

- Evolution I has recorded a regional bloc race
- a region contains at least two factions with nearby members
- a selected or pressured country is at war
- the world has several active wars involving faction members
- chaos has reached a mid-tier escalation state

### Active-event evolution

Evolution II should alter existing pressure regions:

- neutral pressured countries can receive `border pressure` or `bloc polarization` spirits
- faction leaders can demand public commitments
- a country already at war can become eligible if joining a faction is diplomatically valid
- newly aligned countries that border enemies can receive border defense missions
- enemy-border states become important objectives

### Pre-fire evolved opening

The first Event 17 firing under Evolution II can choose a war-adjacent minor instead of only a quiet neutral. The selected country can join a faction even if this increases its war danger, as long as it is not joining a direct enemy faction.

### Player experience

A player selected under Evolution II should see whether the faction option will pull them into wars or put them beside a faction enemy. The event should not hide that public consequence. It should still avoid future hidden mechanics.

A player pressured as a neighbor should receive decisions and timed missions that let them prepare, resist, or lean into one bloc.

### AI behavior

- AI countries already at war should favor factions fighting their enemies.
- AI countries with weak armies should avoid joining factions already losing nearby wars unless they are desperate.
- Fascist and communist AI should be more willing to escalate if ideology matches.
- Democratic and neutral AI should prefer defensive guarantees and neutrality resilience unless encircled.
- Faction leaders should pressure border countries when those countries can open a useful front.

### Caps and safeguards

Evolution II can create sharper conflicts, but it should not bypass direct enemy checks. It should not force tiny countries into impossible overseas wars when they have no route, no convoy access, and no strategic connection to the faction.

## Evolution III: Collapse of Neutrality

### Design role

The final evolution represents a broad crisis in which small countries stop trusting neutrality as a survival policy. The event can now create multiple faction joins through follow-up events, especially in one region or continent. It should not force every country in the world into factions.

### Unlock direction

Evolution III should become possible when several conditions point in the same direction:

- Evolution II has fired or comparable pressure exists
- faction wars are active or faction rivalries are severe
- multiple eligible neutrals remain in a pressured region
- chaos is high
- previous Event 17 firings have created local bloc memory

### Active-event evolution

When a region is already under pressure, Evolution III can:

- select two to five eligible minors in a region for sequential follow-ups
- distribute them among existing factions using pressure, ideology, fear, and rivalry weights
- allow one or two countries to resist and gain a temporary neutrality exhaustion spirit instead of joining immediately
- let faction leaders race through support decisions
- trigger a regional report event if several alignments happen close together

### Pre-fire evolved opening

The first firing under Evolution III can open with a small cascade:

- initial selected minor joins through normal player or AI logic
- one or more nearby minors receive delayed follow-ups
- the system prefers different factions where geography and ideology support it
- the cascade cap prevents more than a small share of eligible minors from joining from one automatic firing

### Faction war interaction

At Evolution III, the event can make large faction wars more dangerous when newly aligned minors border enemy faction members. It should not create arbitrary wars by itself. The danger comes from faction membership, existing wars, guarantees, and border proximity.

If two factions are already at war, a newly aligned border minor can become a new front. If factions are not at war, the event can raise threat, war support, and diplomatic pressure without forcing a war goal unless another event or decision chain does that work.

### Player experience

If the player is a small neutral country during Evolution III, the campaign should feel like the map is closing around them. They may have to choose a faction if selected. If pressured but not selected, they can spend resources and complete missions to remain outside a faction temporarily.

If the player is a faction leader, they should see opportunities to support pressured minors. These opportunities should cost real resources and should risk backlash.

### AI behavior

AI should avoid total uniformity. Not every nearby country should choose the same faction unless the region has overwhelming pressure from one bloc.

- countries surrounded by one faction often join that faction
- countries afraid of encirclement often choose a rival
- isolated countries may choose the strongest naval or ideological patron
- countries with high neutrality resilience may hold out
- faction leaders at war prioritize border countries and supply corridors
- faction leaders at peace prioritize ideology, relations, and containment of rivals

### Caps

Evolution III must use strict caps:

- one automatic firing cannot align every eligible country in a region
- a country cannot be selected again while under recent alignment cooldown
- a faction leader reaction should have a cooldown
- regional cascade should expire after a clear period
- if no valid faction alternatives exist, the cascade should remain small

## AI matrix overview

The detailed matrix is in `matrices/017_random_faction_ai_matrix.md`. The implementation should treat AI as part of the design, not a final flat weight.

Important AI principles:

- AI should not choose a route with invalid targets.
- AI should not accept a faction option only because it is first in the option list.
- AI faction leaders should not spam pressure if the target cannot join or if the faction leader cannot reach the region.
- AI neutral countries should value survival, ideology, local threats, faction strength, and recent pressure.
- AI countries under high chaos can make riskier choices, but those choices still need local logic.

## Balance intent

The event should change the diplomatic map without becoming an instant world blender.

### Baseline balance

- one country joins one faction
- short temporary strain for the selected country
- hidden neighbor memory but no immediate chain
- low chaos impact beyond standard faction-join chaos handling

### Evolution I balance

- one delayed neighbor response at most
- rival factions can react, but with resource costs
- regional pressure is noticeable but contained

### Evolution II balance

- war-adjacent countries can be selected
- border missions and polarization spirits make the choice matter
- direct enemy faction checks remain strict

### Evolution III balance

- several countries can be pulled into bloc politics
- the cascade is capped by region, valid factions, and cooldowns
- some countries should still resist or stay outside factions

## Exploit prevention

The event should avoid:

- farming free faction-entry bonuses
- repeatedly applying temporary spirits to the same country
- letting faction leaders farm cheap support decisions for endless influence
- letting countries join direct enemy factions through invalid scope checks
- using player tag switching to force a preferred country into the option pool too often
- stale event targets after faction leaders die
- visible decisions for countries that no longer meet pressure conditions

Use cooldown flags, route validity triggers, target cleanup, and dynamic costs to prevent abuse.

## Interaction with existing Chaos Redux systems

### Chaos Meter

The standard Chaos Redux chaos change for faction joining should be respected. Event 17 should not double-charge chaos unless the event creates an extra visible crisis beyond normal faction entry.

### Event clusters

Cluster behavior can make Event 17 fire alongside diplomatic panic incidents. Cluster expansion should remain indirect and diplomatic unless a later accepted plan changes the diplomacy cluster.

### World threat framework

Event 17 should not create a new existential threat source. It can react to existing world threats by making minors seek factions faster.

### Chemical, biological, death, and air systems

This event does not directly use those systems. It can be indirectly affected by wars or world chaos that those systems create. Do not add chemical or biological hooks unless another accepted design links diplomacy to those systems.

## Edge cases

### Too few factions

If no valid faction exists, Event 17 should show unavailable in event details and manual selection should display the appropriate unavailable state. If one faction exists, the selected country joins that faction or the player receives the single forced option.

### Faction leader dies before option click

The player option should validate that the faction still exists at click time. If the selected option becomes invalid, the event should route to a safe fallback event that reselects from remaining valid factions for that same country. If none remain, it should cancel cleanly and log a skipped reason only in debug or event log systems that already support skipped availability.

### Selected country becomes invalid before firing

The target should be revalidated in the immediate block or pre-option effect. If invalid, cancel without applying pressure and rebuild selection if the event system supports it.

### Country has no neighbors

Island minors and isolated countries can still be selected if they can join a faction. Their regional pressure should use a sea-region, continent, or faction-reach bucket rather than neighbor-only logic.

### Multiplayer

The player option should only open for the human-controlled selected country. Other human players should learn through normal event notifications, event logs, or world behavior.

# Event 043: Monsters from the Deep

## Part 5: Focus-tree architecture and route plans

## Tree ownership

Every full monster country receives a unique focus tree.

The trees share a readable architecture, timing language, system hooks, and focus-filter taxonomy. They do not share copied focus blocks with renamed titles. Each tree needs creature-specific route order, prerequisites, rewards, decisions, unit access, AI plans, failure states, and capstones.

The terminal Cthulhu country receives a separate terminal tree. Abyssal Remnants receive one generic remnant tree with creature-aware localisation.

## Intended size

| Tree | Target range | Reason |
| --- | ---: | --- |
| Each full monster tree | `36-44` focuses | Enough room for survival, apex, brood, range, pact, solitary, failure, and terminal readiness |
| Cthulhu terminal tree | `45-60` focuses | Global war, integration, surviving apex management, inland conquest, and defeat pressure |
| Abyssal Remnant tree | `18-24` focuses | Survival, dispersal, limited brood growth, surrender, and cleanup |

These ranges guide implementation. A tree may use fewer focuses when several actions belong in decisions. It may not satisfy the route map through one or two generic focuses per branch.

## Duration language

- `7` days for initial setup, immediate emergency handoff, or route-state switch
- `35` days for early strategic forks, focused adaptations, and decision unlocks
- `70` days for major lair projects, deep route commitments, pact formation, and capstones
- longer only for terminal commitments whose power and risk justify it

The first meaningful choice should appear after one opening focus or a very small opening group.

## Shared lane order

At normal zoom, every full monster tree should read from left to right as:

1. opening survival and lair
2. apex development
3. support broods
4. coastal empire and inland adaptation
5. pact route
6. solitary dominion
7. terminal readiness and failure response

The pact and solitary lanes are mutually exclusive after a clear commitment focus. Early survival, apex, brood, and limited range investments remain compatible with either political direction.

The layout should reserve a small lower lane for emergency or failure content. Hidden terminal focuses remain invisible until Evolution II and World Collapse conditions allow them.

## Opening group

Every tree begins with one creature-specific opening focus. It should:

- verify the apex and lair
- remove the temporary landing-disorientation idea
- unlock the main event decision category
- reveal two to four early choices
- set the first AI plan
- create no free duplicate units
- give no large generic political-power reward

The early choices should normally include:

- strengthen the apex
- establish the first support-brood route
- secure a second coastal objective
- prepare one creature-specific special action

## Apex branch

The apex branch strengthens the unique creature without creating another copy.

Useful reward types include:

- staged replacement of the apex idea
- terrain and depth resistance
- one signature action
- recovery or armor stance
- port assault
- pursuit
- ambush
- organization disruption
- lair defense
- lower Hunger growth for a defined action
- new interaction with selected support units
- terminal transfer preparation

The branch must preserve counterplay. No focus may make the apex immune to encirclement, Sea Bond loss, or all ordinary damage.

## Brood branch

The brood branch unlocks support families and changes how reinforcement receipts are earned or used.

The branch should contain:

- one initial primary support family
- one second family
- one creature-specific mixed formation or spawn condition
- lair or port growth
- support-cap changes
- over-cap management
- one secondary family choice
- a late capstone that changes the campaign loop

The branch should not issue a passive endless division every month.

## Coastal empire and inland branch

This branch defines legal expansion.

It should:

- register additional lairs
- improve port connection
- extend operational depth
- unlock creature-specific terrain or corridor rules
- open new war targets
- change core eligibility
- impose Hunger or strategic costs
- include one consolidation focus
- include one later ambition focus

Range expansion is a major strategic commitment. The player should understand the public cost before completing it.

## Pact route

The pact route is optional and creature-specific.

It should unlock:

- proposal targets
- truce
- compact
- faction contribution
- shared objective
- reinforcement support
- betrayal consequences
- terminal pact readiness

Pact branches should differ. Cetus is a broker. Hafgufa prefers a narrow northern pact. Scylla treats pacts as temporary passage. Jormungandr protects a leadership claim. Te Wheke preserves local autonomy.

## Solitary route

The solitary route rejects cooperation.

It should unlock:

- rival apex targeting
- stronger independent reinforcement
- subject or absorption handling
- anti-pact war goals
- a unique dominion score path
- Apex Dominion readiness where appropriate
- increased Hunger or diplomatic pressure

It cannot simply grant larger combat modifiers than the pact route. Its strength comes from control and risk.

## Failure and crisis route

A full monster tree needs visible responses to:

- loss of the original lair
- Severed Sea Bond
- Frenzied Hunger
- loss of most support formations
- encircled apex
- failed pact
- threatened extinction
- imminent remnant conversion

Failure focuses are short emergency choices or unlock emergency decisions. They do not erase the consequences for free.

## Idea lifecycle

Each full monster country should begin with no more than three focus-owned ideas:

1. Apex Sovereignty
2. creature-specific apex identity
3. temporary landing disorientation or first-lair instability

The lifecycle should be:

| Idea | Start | Early change | Route change | Failure form | Terminal disposition |
| --- | --- | --- | --- | --- | --- |
| Apex Sovereignty | Defines nonhuman ruler and one-apex rule | Gains lair and decision hooks | Pact or solitary variant | Remnant replacement after apex death | Reconciled into Cthulhu union |
| Creature apex identity | Expresses combat role | Staged improvement | Route-specific final form | Removed permanently on apex death | Surviving identity remains tied to transferred apex |
| Landing instability | Temporary weakness | Removed after first survival focus | None | Can return as isolation crisis | Removed |

Additional ideas should represent a durable institution or stage. Routine rewards belong in decisions, unit changes, state changes, temporary modifiers, and route access.

## Focus filters

Every visible focus needs accurate search filters.

Recommended taxonomy:

- political or route identity
- army or apex
- special forces or support brood
- industry only when a focus changes captured production or construction
- naval for port, convoy, blockade, and maritime control
- diplomacy for pacts
- expansion for war targets, lairs, and range
- special mechanic for Hunger, Sea Bond, or creature powers
- crisis for failure content
- terminal for revealed World Collapse content

A focus can use more than one filter, but its primary lane must remain clear.

## Focus Navigation

Each full tree should expose navigation shortcuts for:

- Apex
- Broods
- Littoral Empire
- Pact or Solitary Dominion
- Crisis

The terminal branch navigation remains hidden until revealed.

Cthulhu's tree should expose:

- Union
- Surviving Apexes
- Continental Conquest
- Generic Broods
- World Order
- Collapse Risk

## No focus inlay

This specification does not add a focus inlay window.

Hunger and Sea Bond already appear in the decision category and tooltips. Repeating them inside sixteen trees adds implementation and visual risk without changing the player's action. A later accepted UI addendum can revisit this only if ordinary focus requirements remain unclear during implementation.

## Full monster route maps

## 1. Titanus Kraken focus architecture

### Opening survival

**From the Norwegian Deep: secure the first harbor, bind the apex to the coast, and survive the opening counterattack.**

The opening group should resolve the immediate landing problem in norwegian coast and norwegian sea pool. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Crushing Reach: improve port assault, fort breaking, entrenchment disruption, and the apex's ability to attack from a lair.**

This branch expresses crushing tentacle siege, port seizure, convoy strangulation, and coastal fortress breaking. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Tentacles in Every Harbor: unlock Raiders and Reefbreakers, then build a linked northern spawn network.**

Primary family access: Abyssal Raiders, Reefbreakers, Trench Stalkers. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**From Fjord to Hinterland: one cautious inland extension with high dependence on ports.**

Range profile: Lowest ordinary inland ceiling. It gains one extra depth only through a late landward route. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Northern Abyss: compact with Hafgufa and a guarded route toward Jormungandr.**

Relationship basis: Strong affinity with Hafgufa, guarded affinity with Jormungandr, rivalry with Scylla. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**No Other Maw: reject pacts, destroy rival lairs, and claim the northern seas.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**Severed Arms: emergency contraction when Sea Bond collapses, with one chance to save the apex.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A northern port network that lets spawned broods move quickly between controlled coastal hubs.


## 2. Titanus Scylla focus architecture

### Opening survival

**The Strait Runs Red: take a second shore and establish a rapid island front.**

The opening group should resolve the immediate landing problem in sicily or calabria near the strait of messina. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Six Maws: pursuit, repeated attack windows, and retreat punishment without duplicating the apex.**

This branch expresses rapid multi-vector attacks, high pursuit, island warfare, and lethal attacks against retreating units. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Hunting Packs: fast Raiders, Shoals, and Venom Broods built around short assaults.**

Primary family access: Riptide Shoals, Abyssal Raiders, Venom Broods. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Across the Narrow Seas: island and strait control before limited continental depth.**

Range profile: Moderate ceiling with strong performance in narrow coastal corridors and islands. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**A Temporary Passage: narrow compacts with Cetus or another Mediterranean survivor.**

Relationship basis: Weak pact preference, situational compact with Cetus, rivalry with Kraken and Leviathan. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Every Ship a Tribute: assassination of rival apexes and control of Mediterranean chokepoints.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Heads Turn Inward: Hunger crisis that can sacrifice a support pack or risk collapse.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A strait network that gives rapid reinforcement and target access across nearby islands.


## 3. Titanus Leviathan focus architecture

### Opening survival

**The Eastern Shore Breaks: establish one fortified coastal dominion seat.**

The opening group should resolve the immediate landing problem in eastern mediterranean and levantine coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Living Fortress: armor, endurance, controlled infrastructure destruction, and defensive stances.**

This branch expresses extreme armor, endurance, infrastructure crushing, and slow unstoppable coastal advance. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**The Weight Below: Colossi, Reefbreakers, and lair guards.**

Primary family access: Drowned Colossi, Reefbreakers, Trench Stalkers. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**The Land Bears the Sea: trade speed for deeper endurance and integration.**

Range profile: Moderate ceiling. Late routes can trade speed for deeper endurance. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**Covenant of Vast Things: anchor a pact with Cetus and Timingila.**

Relationship basis: Affinity with Cetus and Timingila, rivalry with Jormungandr for terminal leadership. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The First and Greatest: subject defeated monster countries and pursue Apex Dominion.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Fortress Isolated: emergency redeployment or final stand after loss of all ports.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A mobile fortress profile that can anchor one major offensive while broods hold captured shores.


## 4. Titanus Cetus focus architecture

### Opening survival

**The Ketos Comes Ashore: secure a Red Sea or Horn foothold and create a mixed support force.**

The opening group should resolve the immediate landing problem in red sea, horn of africa, or levant-adjacent fallback pool. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Ravager of Coasts: balanced strength, amphibious attack, and anti-capital pressure.**

This branch expresses balanced amphibious conquest, support-swarm coordination, and coastal devastation. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Creatures of the Wake: flexible access to Shoals, Raiders, and one heavy family.**

Primary family access: Riptide Shoals, Abyssal Raiders, Drowned Colossi. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Two Seas, One Hunger: link Red Sea and eastern Mediterranean objectives.**

Range profile: Moderate ceiling with an early route toward dry coastal hinterlands. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Deep Assembly: strongest early pact-broker route in the roster.**

Relationship basis: High pact willingness with Leviathan and Timingila, conditional pact with Scylla. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The Sacrificial Shore: feed from coastal capitals and reject equal partners.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**No Offering Remains: choose contraction, destructive feeding, or remnant survival.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A multi-sea reinforcement web built from captured ports and regional pact access.


## 5. Titanus Hafgufa focus architecture

### Opening survival

**The Island Is a Mouth: establish the first feeding lair and survive without rapid expansion.**

The opening group should resolve the immediate landing problem in iceland or greenland sea coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Waiting Maw: ambush, defensive baiting, and ship-swallowing objectives.**

This branch expresses stationary or slow ambush power, blockade, baiting, ship swallowing, and fortified coastal lairs. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Things Beneath the Bait: Stalkers, Reefbreakers, and defensive Shoals.**

Primary family access: Trench Stalkers, Reefbreakers, Riptide Shoals. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**A Coast Held Still: strengthen shallow range while refusing deep continental adaptation.**

Range profile: Very low ceiling. Inland extension remains costly even late. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**Whales Beneath the North: durable compact with Kraken and limited Jormungandr cooperation.**

Relationship basis: Strong affinity with Kraken, guarded affinity with Jormungandr, little interest in distant pacts. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The Sea Comes to Feed: create a network of prepared kill zones and reject distant pacts.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Bait Goes Cold: relocate one lair or accept permanent remnant state.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

Prepared coastal kill zones that reward holding selected ports instead of constant expansion.


## 6. Titanus Jormungandr focus architecture

### Opening survival

**The Coil Unfurls: establish a long coastal path without breaking Sea Bond.**

The opening group should resolve the immediate landing problem in north atlantic or nordic sea pool. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Venom of the World Serpent: venom pressure, reach, and controlled environmental devastation.**

This branch expresses long coastal reach, venom, environmental devastation, and strong late inland adaptation. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Spawn Along the Coil: Venom Broods, Raiders, and Colossi distributed across linked lairs.**

Primary family access: Venom Broods, Abyssal Raiders, Drowned Colossi. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Beyond the Shoreline: strongest non-terminal inland route with escalating Hunger.**

Range profile: Highest ordinary ceiling after Jiaolong and Cipactli. The terminal route can remove most limits. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Serpent's Ring: guarded northern pact that preserves leadership claims.**

Relationship basis: Guarded ties with Kraken and Hafgufa, strong solitary ambition, rivalry with Leviathan. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Release the Tail: defeat rivals, surround multiple seas, and pursue Apex Dominion.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Broken Coil: cut disconnected territory and retreat toward surviving lairs.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A connected ring of coastal strongholds that extends reach without granting unrestricted continental conquest.


## 7. Titanus Iku-Turso focus architecture

### Opening survival

**Fog on the Baltic: conceal the landing and secure a second Baltic shore.**

The opening group should resolve the immediate landing problem in gulf of finland or baltic coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Unfixed Shape: choose one coherent combat identity from several uncertain public interpretations.**

This branch expresses fog, cold-water attack, sudden raids, baltic control, and organization disruption. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Raiders in the Mist: Stalkers, Raiders, and Venom Broods.**

Primary family access: Abyssal Raiders, Venom Broods, Trench Stalkers. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Cold Roads Inland: limited adaptation around frozen coast and approved lake-adjacent corridors.**

Range profile: Moderate ceiling. Frozen coast and lake-adjacent routes can reduce selected penalties after research. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**A Pact Beneath Ice: rare compact with Kraken under shared regional pressure.**

Relationship basis: Low baseline pact willingness, situational compact with Kraken, rivalry with Umibozu. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The Baltic Without Dawn: fog domination, port raids, and refusal of distant partners.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Fog Scatters: choose hidden withdrawal or an exposed final battle.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A Baltic concealment network that improves raids and defensive movement between threatened coasts.


## 8. Titanus Umibozu focus architecture

### Opening survival

**A Black Shape at Sea: close one port and establish a storm-bound lair.**

The opening group should resolve the immediate landing problem in pacific coast of honshu. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Silent Monk of the Waves: disruption, port silence, organization damage, and night pressure.**

This branch expresses storm creation, naval panic, organization damage, port shutdowns, and sudden night attacks. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Figures Under the Rain: Stalkers, Venom Broods, and Shoals.**

Primary family access: Trench Stalkers, Venom Broods, Riptide Shoals. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Storms Over the Interior: project pressure inland without granting ordinary deep conquest.**

Range profile: Low ceiling. It can project pressure inland through storms without becoming a deep land conqueror. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Northern Pacific Compact: coordinate with Akkorokamui and possibly Jiaolong.**

Relationship basis: Affinity with Akkorokamui, cautious cooperation with Jiaolong, rivalry with Bakunawa. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Every Port Goes Dark: chain bounded port shutdowns and reject daylight diplomacy.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Sea Falls Quiet: preserve the apex through one concealed retreat or collapse.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A moving storm front that closes selected enemy ports for bounded periods after successful coastal objectives.


## 9. Titanus Akkorokamui focus architecture

### Opening survival

**Red Water in Uchiura Bay: secure Hokkaido access and establish regeneration conditions.**

The opening group should resolve the immediate landing problem in southern hokkaido and uchiura bay. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Flesh That Returns: bounded regeneration, scar recovery, and anti-attrition strength.**

This branch expresses regeneration, ink or poison effects, tentacle combat, and northern expansion. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Ink and Claw: Reefbreakers, Venom Broods, and Raiders.**

Primary family access: Reefbreakers, Venom Broods, Abyssal Raiders. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Across the Northern Shores: controlled coastal and river-mouth adaptation.**

Range profile: Moderate ceiling with strong coastal recovery and limited river-mouth adaptation. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Red and Black Sea: compact with Umibozu and selected Jiaolong support.**

Relationship basis: Affinity with Umibozu and Jiaolong, conditional rivalry with Kraken. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The Bay Has No Shore: build a protected northern brood domain.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**Regeneration Denied: spend the last reserve on retreat, support sacrifice, or final stand.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A recovery system that converts secured northern ports into bounded regeneration windows.


## 10. Titanus Jiaolong focus architecture

### Opening survival

**Rain at the River Mouth: secure a southeast coast and the first river corridor.**

The opening group should resolve the immediate landing problem in southeastern chinese coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Flood Dragon Stirs: rain, flood pressure, movement, and controlled transformation.**

This branch expresses flood pressure, river access, storms, and movement from coast into river-connected territory. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Spawn of the Estuary: Raiders, Shoals, and Venom Broods.**

Primary family access: Abyssal Raiders, Riptide Shoals, Venom Broods. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Rivers Carry the Sea: expand the curated river-depth exception in stages.**

Range profile: Special rule treats curated river-connected states as one depth shallower, within a hard cap. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**Rain Across Many Seas: high-cooperation route with northwest Pacific monsters.**

Relationship basis: High pact willingness with Akkorokamui, Umibozu, and Cetus. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**From Jiao to Long: reject pacts and pursue ascendant dominion through river systems.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The River Is Dammed: restore one corridor or withdraw to the coast.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A bounded river corridor registry that extends legal targets while retaining coastal dependence.


## 11. Titanus Bakunawa focus architecture

### Opening survival

**The Moon Is Taken: establish an island lair and open the first eclipse window.**

The opening group should resolve the immediate landing problem in central or southern philippines. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Devourer of Light: timed night and eclipse attack power.**

This branch expresses night and eclipse pressure, island conquest, repeated amphibious waves, and temporary visibility disruption. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Waves Between Islands: Raiders, Shoals, and Stalkers.**

Primary family access: Abyssal Raiders, Riptide Shoals, Trench Stalkers. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**An Archipelago of Nests: island-chain movement with weak continental depth.**

Range profile: Island-first range. Deep continental operation remains weak. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Pacific Under Shadow: opportunistic cooperation with Jiaolong or Te Wheke.**

Relationship basis: Opportunistic pact behavior with Jiaolong or Te Wheke, rivalry with Umibozu. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**No Light Above the Sea: repeated eclipse campaigns and rivalry with Umibozu.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Moon Returns: survive the daylight weakness or abandon exposed islands.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

Timed eclipse offensives that improve amphibious operations and expire into a recovery period.


## 12. Titanus Timingila focus architecture

### Opening survival

**The Eater Enters the Bay: gain one feeding reserve and secure a heavy coastal front.**

The opening group should resolve the immediate landing problem in bay of bengal or indian ocean coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Swallower of Whales: durability, large attacks, and reserve generation.**

This branch expresses devouring, high durability, coastal feeding, and heavy reinforcement waves. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**The Heavy Wake: Colossi, Reefbreakers, and Shoals.**

Primary family access: Drowned Colossi, Reefbreakers, Riptide Shoals. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**A Hunger Beyond the Delta: slow inland adaptation with severe upkeep.**

Range profile: Moderate ceiling with powerful coastal sustainment and slow inland movement. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Northern Indian Deep: strong cooperation with Cetus and Leviathan.**

Relationship basis: Affinity with Cetus and Leviathan, limited interest in Pacific pacts. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Nothing Too Large to Eat: target the largest ports and rival apexes.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Maw Goes Empty: contract the army, feed destructively, or enter remnant state.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A feeding reserve that can finance one major reinforcement wave after large coastal victories.


## 13. Titanus Te Wheke focus architecture

### Opening survival

**The Chase Through Cook Strait: establish pursuit routes and a second island objective.**

The opening group should resolve the immediate landing problem in cook strait and marlborough region. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Arms Around the Horizon: ambush, pursuit, and controlled island movement.**

This branch expresses tentacle pursuit, ambush, island movement, and long pacific chase behavior. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**The Wake of the Hunter: Raiders, Shoals, and Stalkers.**

Primary family access: Abyssal Raiders, Riptide Shoals, Trench Stalkers. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Across the Long White Coast: coastal reach within New Zealand and later Pacific islands.**

Range profile: Moderate island and coastal range with low deep inland strength. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**A Net Across the Pacific: cautious compact that preserves local autonomy.**

Relationship basis: Cautious cooperation with Bakunawa and Lusca, strong local autonomy preference. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**The Chase Never Ends: mark and pursue one coastal enemy at a time.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Net Is Cut: withdraw toward a surviving island lair or lose the hunt.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A Pacific pursuit route that can retarget between island chains after completing named coastal objectives.


## 14. Titanus Lusca focus architecture

### Opening survival

**From the Blue Hole: survive the small island start and seize a usable port.**

The opening group should resolve the immediate landing problem in andros or another suitable bahamian state. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**Shark Teeth, Eight Arms: ambush, grapple, and sudden assault.**

This branch expresses blue-hole ambush, island warfare, convoy predation, and sudden local appearances. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Things in the Caverns: Raiders, Stalkers, and Venom Broods.**

Primary family access: Abyssal Raiders, Trench Stalkers, Venom Broods. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Islands Above the Abyss: Caribbean movement with strict continental limits.**

Range profile: Very low continental ceiling and excellent island operation. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Western Atlantic Deep: cooperate with Cipactli and Ipupiara.**

Relationship basis: Affinity with Cipactli and Ipupiara, low interest in transatlantic northern pacts. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**No Diver Returns: expand hidden ambush sites and reject large pacts.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Hole Is Exposed: relocate one ambush site or fight without concealment.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A network of selected island ambush sites that can spawn bounded raider waves after enemy naval movement.


## 15. Titanus Cipactli focus architecture

### Opening survival

**The First Mouth Opens: secure Yucatán or Gulf lowland territory and begin feeding.**

The opening group should resolve the immediate landing problem in gulf of mexico or yucatán coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**A Mouth at Every Joint: high Hunger interaction, repeated feeding, and brutal close assault.**

This branch expresses crocodilian assault, swamp strength, inland feeding, and relentless consumption. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Children of Mud and Salt: Reefbreakers, Colossi, and Venom Broods.**

Primary family access: Reefbreakers, Drowned Colossi, Venom Broods. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Where Water Becomes Earth: marsh and lowland depth exception.**

Range profile: Special rule treats curated marsh and lowland states as one depth shallower, within a hard cap. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The Western Maw Pact: conditional cooperation with Lusca and Ipupiara.**

Relationship basis: Affinity with Lusca and Ipupiara, strong solitary world-making ambition. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Remake the Land: many-mouth dominion and strong Apex Dominion potential.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Mouths Turn on the Brood: sacrifice, contraction, or uncontrolled Hunger crisis.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A marsh corridor network that permits deeper legal operation while increasing Hunger pressure.


## 16. Titanus Ipupiara focus architecture

### Opening survival

**Footprints on the São Vicente Shore: begin a fast raid before the coast fortifies.**

The opening group should resolve the immediate landing problem in são vicente or southeastern brazilian coast. It must connect the first lair, first war, apex position, and current Sea Bond to the next choices.

### Apex route

**The Water Demon Hunts: terror, urban-coast attacks, and rapid retreat.**

This branch expresses fast coastal terror, population attacks, raiding, and south atlantic expansion. The branch must use the existing one-apex unit. It can improve stats, unlock a power, change terrain interaction, and upgrade the apex idea.

### Brood route

**Raiders of the Estuary: Raiders, Venom Broods, and Shoals.**

Primary family access: Abyssal Raiders, Venom Broods, Riptide Shoals. The branch should change receipt sources, support caps, mixed formation use, and lair defense.

### Coastal empire and range

**Up the Atlantic Rivers: limited estuary access without deep continental freedom.**

Range profile: Moderate ceiling with strong urban-coast predation and limited estuary operation. The branch must expose the cost in Hunger, Sea Bond dependence, or front vulnerability.

### Pact route

**The South Atlantic Compact: cooperate with Lusca and Cipactli.**

Relationship basis: Affinity with Lusca and Cipactli, cautious South Atlantic pact behavior. The route needs target validity, acceptance AI, shared objective, failure, and betrayal handling.

### Solitary route

**Every Shore at Night: repeated terror raids and independent expansion.**

The route should pursue independent coastal control and rival-apex defeat. It may contribute to Apex Dominion readiness after Evolution II and World Collapse.

### Crisis route

**The Coast Is Watching: escape observation, lose speed, or accept remnant survival.**

The crisis group should appear only when the matching condition exists. It gives a hard choice and bounded recovery path. It cannot remove a lost lair, dead apex, or failed pact receipt without cost.

### Capstone result

A rapid terror system that weakens selected coastal states before short assault windows.

## Pact and solitary lock

Every tree should delay the final pact or solitary lock until the player has completed basic survival.

The commitment focus must:

- clearly state the public route direction
- set one stable route flag
- close the incompatible lane
- change decision visibility
- change focus AI
- change pact or rival target logic
- change at least one idea or mechanic
- unlock a route-specific campaign action
- survive save and reload

A human player cannot switch routes through decision spam. A route reversal needs a designed crisis event and should be rare.

## Cross-branch interaction

Trees should use a few meaningful cross-links.

Examples:

- apex improvements can reduce the risk of a brood action
- brood control can make one range focus safer
- lair development can unlock one pact contribution
- a pact can open a shared coastal objective
- a solitary victory can unlock a range capstone
- low Sea Bond can reveal a crisis focus
- high Hunger can block a long-term capstone
- a surviving-apex count can reveal terminal readiness

The graph should not become a web of long prerequisite lines. Most interactions should occur through flags, values, decisions, and compact convergence focuses.

## Cthulhu terminal tree

The terminal tree begins only after successful unification.

### Union branch

This branch reconciles:

- transferred apexes
- old country ideas
- support permissions
- subjects
- wars
- lairs
- pacts
- dead-apex memory
- unused reinforcement receipts
- regional control
- terminal Hunger and Sea Bond

The opening union focuses should be short and idempotent. They cannot create missing apexes.

### Surviving apex branch

Each living transferred apex appears through a terminal roster decision or focus group.

The branch should let the player:

- assign apexes to theatres
- improve cooperation
- unlock pair or group synergies
- protect a wounded apex
- exploit creature-specific range rules
- respond to an apex death
- preserve unique identity after transfer

The tree should not require one full focus branch per creature. A data-driven roster and grouped focuses can manage living apexes while retaining creature-specific decisions.

### Continental conquest branch

This branch removes ordinary inland restrictions in stages.

Early terminal content reduces depth penalties and opens inland war targets. Middle content enables deep integration. Late content treats surviving apexes as a world-conquest force.

The route must remain vulnerable to all-apex destruction and normal capitulation.

### Brood branch

Cthulhu can create generic support formations from all six families.

The terminal support loop still uses objectives, caps, and receipts. An unlimited passive unit generator remains forbidden after world-end activation.

### World-order branch

This branch handles:

- monster subjects
- occupied human regions
- coastal capitals
- defeated major powers
- terminal faction or subject policy
- destruction or use of human infrastructure
- final campaign objectives

It should not create a normal human diplomatic empire.

### Collapse-risk branch

Every transferred apex death weakens the union.

The tree and decisions should react to:

- first terminal apex death
- half of transferred apexes dead
- last three apexes
- last apex
- capital isolation
- normal capitulation pressure

The branch gives strategic choices. It cannot restore a dead apex.

## Abyssal Remnant tree

The shared remnant tree contains:

1. emergency survival
2. support-unit consolidation
3. shallow lair defense
4. dispersal or guerrilla coastal route
5. surrender or pact-subordination route
6. final cleanup or Cthulhu auxiliary transfer

The tree should use creature-aware scripted localisation for names and old identity. Its gameplay remains generic because the unique apex is dead.

A remnant cannot:

- reopen its unique tree
- recreate the apex
- lead a pact
- satisfy living-apex terminal thresholds
- claim a solitary dominion capstone
- gain unrestricted inland reach

## Route AI plans

Each full tree needs explicit AI plans for:

- opening survival
- apex priority
- brood priority
- range ambition
- pact willingness
- solitary willingness
- emergency response
- terminal readiness

AI considers:

- current wars
- apex health and position
- Hunger
- Sea Bond
- lair count
- support cap
- coastal state count
- nearby rival monsters
- compatible pact candidates
- human coalition strength
- current evolution
- World Collapse
- player status
- scenario type

No AI plan may complete a pact focus when no valid partner exists or a range focus when the map registry has no valid next-depth target.

## Focus reward budget

A major focus should usually change one important surface and use supporting modifiers only where needed.

Valid main rewards include:

- unlock a decision family
- unlock or improve one support family
- register a lair
- extend legal depth
- grant a one-use receipt
- unlock a signature apex power
- change pact stage
- open a war target
- change core eligibility
- replace an idea stage
- change leader or country presentation
- reveal crisis or terminal content
- create a bounded state effect
- alter AI behavior

Tiny stability, war support, political power, or production modifiers cannot serve as the whole reward.

## Tree layout acceptance

Before completion, each tree must pass:

- source inspection
- `hoi4.focus_inspect`
- full-tree `hoi4.focus_render`
- normal-zoom first-glance review
- branch naming review
- prerequisite and mutual-exclusion review
- focus-filter review
- Focus Navigation review
- route AI probability review
- post-change comparison
- focus auditor pass
- live user validation later

A clean graph with copied route logic still fails. A deep tree with crossed lines also fails.

## End of Part 5

Part 6 defines the monster decision category, human response category, missions, costs, counterplay, pact actions, AI actions, and clutter limits.

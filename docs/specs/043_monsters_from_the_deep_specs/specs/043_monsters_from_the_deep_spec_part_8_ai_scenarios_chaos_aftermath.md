# Event 043: Monsters from the Deep

## Part 8: AI, manual scenarios, Chaos, reactions, and aftermath

## AI design goal

Monster AI should behave like a maritime predator with one irreplaceable apex. Human AI should recognize that destroying the apex or severing its coast can end the threat.

Generic HOI4 front behavior cannot carry the whole design. Event-owned AI strategies, target scoring, focus plans, and decision weights need to shape the campaign.

Every weighted surface requires a baseline probability audit, an owner-applied tuning pass, and a comparison audit using the same named scenarios.

## Monster strategic states

A full monster country can occupy one primary strategic state.

| State | Main condition | AI priorities |
| --- | --- | --- |
| Landing survival | First lair and one-state start | Protect apex, hold lair, secure second port |
| Coastal expansion | Stable Sea Bond and valid targets | Take adjacent coasts, ports, and capitals |
| Lair consolidation | Several exposed coastal states | Register lairs, repair ports, raise defenders |
| Hunger crisis | Hunger Starving or Frenzied | Feed, contract realm, sacrifice support, avoid long projects |
| Sea Bond crisis | Sea Bond Failing or Severed | Retreat apex, retake port, defend lair, cancel deep plans |
| Rival hunt | Solitary route and reachable monster | Mark rival apex, isolate its lairs, avoid human overextension |
| Pact building | Pact route and compatible target | Propose, complete truce objective, contribute safely |
| Extinction response | Several apexes dead and human pressure high | Seek pact, preserve apex, prepare Last Survivors path |
| Terminal preparation | Evolution II and World Collapse | Complete readiness proof, avoid unnecessary apex risk |
| Terminal conquest | Cthulhu active | Assign apexes by theatre, push inland, protect last apexes |

One country should not run conflicting high-priority plans at once.

## Monster target score

Target scoring begins from valid current reach. It never gives a positive weight to an invalid landlocked target.

Positive factors include:

- adjacent coast
- port or naval base
- coastal capital
- high population with remaining feeding capacity
- supply hub near the coast
- state connecting two lairs
- weak current defender
- shared pact objective
- marked capital
- creature-specific terrain
- route-specific rival
- low inland depth
- current war continuity

Negative factors include:

- illegal inland depth
- mountain or desert with no creature adaptation
- no coastal payoff
- strong fortification without siege support
- active human kill zone
- pact partner claim
- disconnected pocket risk
- apex health crisis
- low Sea Bond
- Frenzied Hunger with no feeding payoff
- high naval crossing risk
- another terminal threat
- human player immediate elimination when another natural target exists

The probability auditor must inspect the complete candidate pool. A score-only audit cannot prove final target probability when external front logic is unknown.

## Apex preservation AI

The apex is the country's life. AI should:

- avoid leaving it alone in a pocket
- keep at least one support formation nearby when available
- retreat toward a lair when Sea Bond collapses
- avoid depth `4+`
- avoid crossing a weakly held corridor into deep territory
- refuse low-value attacks at critical strength
- use signature powers for real objectives
- prefer a final stand only when no valid retreat exists
- stop a rival hunt when its own lair is threatened
- assign the apex to the decisive front, not every small border

Apex preservation must not make AI permanently passive. High Sea Bond and support should produce aggressive coastal action.

## Support-force AI

Support families receive roles.

- Riptide Shoals screen and pursue
- Abyssal Raiders take ports and exploit gaps
- Reefbreakers attack forts and hold lairs
- Trench Stalkers defend ambush sites and night fronts
- Venom Broods disrupt dense human formations
- Drowned Colossi anchor a line

AI templates and strategies should maintain a mixed force suited to the creature. It should not assign every formation to one giant front or send heavy units alone into deep territory.

## Pact AI profiles

Monster identities use five pact profiles.

| Profile | Typical members | Behavior |
| --- | --- | --- |
| Broker | Cetus, Jiaolong | Proposes early, values shared objectives, resists betrayal |
| Regional compact | Kraken, Hafgufa, Akkorokamui, Timingila, Te Wheke | Cooperates in compatible theatres |
| Opportunist | Scylla, Bakunawa, Lusca, Ipupiara | Accepts under pressure, may betray for a clear target |
| Dominant partner | Leviathan, Jormungandr, Cipactli | Accepts when likely to lead or when extinction threatens |
| Isolation leaning | Iku-Turso, selected solitary routes | Rarely proposes and demands strong shared pressure |

Route commitment overrides baseline profile.

## Human AI threat assessment

An ordinary AI country should assign Event 043 threat from:

- distance to its territory
- direct border
- current war
- apex path to capital
- threatened population
- threatened ports
- ally requests
- observed Sea Bond
- creature power active
- terminal state
- available transport and military capacity

The response AI should select one primary threat, one secondary threat if capacity allows, and no more active projects than it can support.

## Human AI action rules

### Evacuation

AI evacuates when:

- a high-population coast is likely to fall
- a valid destination and route exist
- transport cost is affordable
- evacuation does not empty the only defended capital without reason

### Port defense

AI fortifies when:

- the port is strategically important
- supplied divisions can reach it
- the monster is within current range
- the project can finish in time
- another higher-priority capital crisis does not consume resources

### Hunter command

AI establishes Monster-Hunter Command when direct war or sustained threat exists and the country can support the officer and equipment cost.

### Kill zone

AI uses a kill zone when:

- apex location is observed
- the selected state is reachable
- required divisions exist
- Sea Bond can plausibly be lowered
- failure will not expose the capital

### Ocean Watch

AI contributes when:

- several monsters are active
- it has naval or air capacity
- it supports threatened allies
- its own immediate survival does not require every resource

## Major-power response

Distant major powers can receive strategic actions through the same category.

They may:

- fund Ocean Watch
- send equipment
- escort evacuations
- deploy volunteers or expeditionary forces through normal rules when valid
- guarantee a threatened coastline
- exploit a monster war against a rival
- withhold aid for political reasons
- form a temporary anti-monster coalition

The event should allow cynical behavior. It should not force every ordinary country into one universal alliance.

## Foreign reactions

Reactions should consider:

- ideology
- current war
- faction membership
- relation to threatened state
- naval capability
- colonial holdings
- distance
- own coastal exposure
- prior Chaos-event experience
- active world threat
- human or nonhuman status

Possible reaction families:

- emergency port inspections
- naval mobilization
- refugee reception
- press censorship
- religious interpretation
- scientific observation
- opportunistic invasion of a weakened rival
- arms and transport aid
- refusal to commit
- faction emergency conference

These are report and decision directions. They should not create dozens of one-line flavour events with no consequence.

## Manual scenario proposal

### Registry

Provisional scenario identity:

- `SCN-015`
- Monsters from the Deep
- four intensity stops
- two setup types
- dynamic scenario-list row
- confirmation flow
- one tightly scoped bypass
- no normal event timing requirement
- no normal Chaos-level requirement
- no prior Event 043 requirement

Implementation must confirm that scenario ID `15` remains free.

## Scenario type 1: Warring Titans

Warring Titans creates independent full monster countries.

Rules:

- every selected monster is hostile to ordinary reachable countries
- monster countries remain hostile to one another
- no opening compact
- pact routes remain available later
- Cthulhu does not activate at setup
- normal terminal gates apply after setup
- intensity determines roster and support strength

## Scenario type 2: Pact of the Deep

Pact of the Deep creates several opening truces or compacts.

Rules:

- selected compatible monsters enter planned pact groups
- pacts remain separate when one global faction would be too large for the chosen intensity
- ordinary countries remain hostile targets
- Maximum can start one qualifying abyssal faction
- Maximum can prepare the Cthulhu sequence
- the scenario must raise Chaos into World Collapse before setting terminal state
- public terminal toggle behavior must be defined and shown

Preferred terminal-toggle behavior:

- normal scenario launch respects the Cthulhu public toggle
- Force Trigger Mode may bypass it
- a disabled terminal route still allows a nonterminal Pact Maximum invasion

## Scenario intensity

| Intensity | Roster | Starting strength | Geographic rule |
| --- | ---: | --- | --- |
| Low | `2` | Baseline apexes and small support package | Two distant macroregions |
| Medium | `5` | Stronger support and one extra receipt | At least four macroregions |
| High | `10` | Evolution I package and several mature starts | Most major oceans |
| Maximum | `16` | Evolution II package and full global opening | Every valid macroregion |

Exact support counts and route progress require balance evidence.

## Scenario selection options

The scenario can use one of two roster-selection modes if the existing UI can express it without another control:

- curated global spread
- deterministic full roster for Maximum

Low, Medium, and High should use the normal geography selector with scenario intensity targets. Maximum uses every ready identity.

The scenario does not need a third monster-subset control in the shared UI.

## Scenario launch sequence

1. save selected type and intensity
2. confirm no incompatible terminal state
3. set Event 043 scenario setup flag
4. reserve tags and landing states
5. create selected countries
6. apply scenario strength
7. create pacts when selected
8. record Event 043 active state
9. update world threat
10. display opening presentation
11. raise or set Chaos only according to scenario contract
12. clear setup bypass and temporary targets
13. verify created count against requested count
14. enable normal Event 043 lifecycle

A failed launch should leave no partial hidden bypass.

## Scenario relaunch

The same scenario should not launch twice into the same active Event 043 system unless a separately designed reinforcement mode exists.

Preferred rule:

- launch disabled while Event 043 is active
- a debug-only additive wave helper remains outside the player scenario UI
- after complete Event 043 defeat and cleanup, relaunch can be allowed only if tags and permanent dead-apex history are deliberately reset by the scenario contract

A manual sandbox relaunch that restores dead apexes must say that it resets Event 043 history. It should not happen accidentally.

## Chaos impact map

Event 043 should add direct Chaos only for major one-shot event-owned consequences.

### Opening

Recommended formula:

- `+10` opening base
- `+2` per successfully emerged apex
- cap at `+40`
- one opening receipt

Examples:

- two-monster manual Low: `+14`
- four-monster natural baseline: `+18`
- eight-monster evolved opening: `+26`
- sixteen-monster global opening: capped at `+40`

The scenario system may set or add Chaos differently when a manual terminal setup needs World Collapse. The scenario detail text must match the actual behavior.

### Later emergences

- `+2` per new apex
- bounded by one evolution-wave cap
- one receipt per apex identity
- no Chaos when a setup fails

### Pacts

- first meaningful three-apex compact or faction: `+5`
- first large pact threshold: `+10`
- each milestone once
- ordinary truce proposals add zero

### Apex defeat

- each pre-terminal full-monster apex collapse: `-5`
- once per identity
- no duplicate reduction after save and reload
- ordinary battle deaths still enter generic Deaths when relevant

### Global defeat

- base `-25`
- additional bounded reduction based on number of apexes destroyed during terminal or global campaign
- total Event 043 global-defeat reduction capped at `-50`
- separate from generic peace and death changes

### Cthulhu activation

Cthulhu activation adds zero direct Chaos. It already requires World Collapse.

### Generic sources

Do not duplicate:

- war Chaos
- annexation Chaos
- death Chaos
- nuclear Chaos
- contamination Chaos
- peace Chaos
- faction membership Chaos

Event-owned changes need the shared Chaos History path and clear actor or source text.

## World-threat interaction

Event 043 activates its world-threat source when the first full monster emerges.

It remains active while:

- one full monster apex lives
- Cthulhu's Dominion exists
- a meaningful Abyssal Remnant war continues

It clears after final cleanup. A single isolated harmless remnant can be retired without keeping the global threat forever.

## Interaction with Event 013 Natural Disasters

Event 043 replaces the old Massive Flood event.

Event 013 remains the owner of ordinary flood disasters. Event 043 may call the documented Natural Disasters gateway for a creature-specific bounded flood only when:

- the source is Jiaolong or another explicitly mapped route
- the call has valid target and authority proofs
- Event 043 accepts the returned result
- no duplicate population or building damage occurs
- the effect remains local or regional
- the call does not refire Event 013 as a pacing event

Most monster damage should remain Event 043-owned.

## Interaction with Event 020 Black Plague

Rat countries and monster countries are separate nonhuman families.

They should:

- recognize each other as special and nonhuman
- use event-specific war and target compatibility
- avoid human civilian decisions
- preserve separate unit registries
- never absorb or convert each other's apex or king units without an accepted cross-event route

A full monster may attack a Rat Nation when physically reachable. The event needs explicit target rules. Generic human-diplomacy assumptions do not apply.

## Interaction with other special countries

The compatibility audit should cover:

- zombies and weaponized zombies
- Death
- cave countries
- cannibalism Wendigo routes
- Brilliant Scientist nonhuman sovereignty
- Holy Realm where ordinary civilian assumptions differ
- Fury actors
- Fallout wasteland and successor states
- future special Chaos countries

Each result should be:

- valid hostile target
- ignored
- protected
- alliance possible through explicit route
- terminal conflict
- blocked pending design

No broad `is_special_chaos_country = no` exclusion should remove all interesting nonhuman conflicts without review.

## Event 070 legacy caller

The current repository directly calls `chaosx.nr43.1` from Event 070 random lists under the old Massive Flood meaning.

Implementation must inspect every such call and choose one disposition:

- remove the Event 043 entry
- replace it with an Event 013 flood gateway
- replace it with another Event 070-owned consequence
- call an Event 043 emergence helper only when that interaction is deliberately accepted and idempotent

Leaving the call unchanged would allow Event 070 to start a Major global invasion outside Event 043 pacing and Chaos rules.

## Defeat aftermath eligibility

A global defeat aftermath is appropriate only when the campaign was large enough.

Suggested eligibility facts:

- Event 043 active for at least one year
- at least eight apex identities emerged, or Cthulhu activated
- several macroregions fought monsters
- tracked Event 043 deaths and coastal destruction exceed a meaningful threshold
- at least one major power participated
- threat ended through apex destruction or normal terminal capitulation
- aftermath branch enabled
- no incompatible world end

A small two-monster containment should use ordinary reports and reconstruction decisions without a global super-event.

## Global defeat aftermath

Working role: **The Shores Remember**.

The aftermath can create:

- a defeat super-event
- reconstruction of major ports
- refugee return and resettlement
- memorial and missing-person reports
- an Abyssal Watch cooperation system
- limited research sharing on monster behavior
- remaining lair purification
- treatment of surviving remnants
- disputes over captured biological material
- changes to naval doctrine and coastal defense
- achievements

The tone should be reflective and specific. It should not present the war as cost-free triumph.

## Abyssal Watch

A postwar cooperation layer can use existing decisions and diplomatic groups.

It should remain limited:

- share sighting and lair data
- fund coastal observation
- coordinate one annual exercise
- respond to surviving remnants
- assist reconstruction

It should not become a permanent universal faction or a large third event mechanic.

## Reconstruction

Reconstruction actions can target:

- ports
- rail links
- naval bases
- coastal factories
- housing and population return
- purified lairs
- coastal capitals

Costs should use construction capacity, convoys, equipment, and time. Population cannot be restored through a button.

## Remnant settlement

After global defeat, each Abyssal Remnant receives one disposition:

- destroyed during final cleanup
- contained in one isolated lair
- surrendered and dispersed
- continued as a minor hostile coastal threat
- transferred into a postwar research or guard event only when culturally and mechanically appropriate

A living support unit cannot be turned into a normal human division.

## Multiplayer rules

- opening and evolution are global transactions
- each monster tag has one owner
- multiple human monster players can coexist
- pacts between human monsters use explicit events
- a human-controlled monster cannot be merged under Cthulhu without a visible choice unless the manual scenario states forced union
- one human refusal must not corrupt the terminal transfer array
- human response categories use local selected targets
- global Chaos and event-log receipts apply once
- save and reload preserves player ownership and target selections
- tag switching clears stale human-only selections

## Probability evidence plan

Named scenarios should cover:

- baseline roster spread
- Evolution I spread
- Evolution II full roster
- landing fallback
- monster target priorities
- pact acceptance
- pact betrayal
- Hunger crisis decisions
- human evacuation
- human port defense
- kill-zone choice
- terminal readiness path timing
- later emergence pacing
- Cthulhu theatre assignment

The matrix file defines exact evidence expectations.

## End of Part 8

Part 9 defines presentation, text direction, super-events, assets, achievements, documentation, acceptance, and implementation completion.

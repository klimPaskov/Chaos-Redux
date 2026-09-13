# Event 043: Monsters from the Deep

## Part 2: Opening, landing geography, and inland range

## Geographic objective

The natural opening should place several dangerous invasions in separate maritime theatres. Each monster needs a landing region that supports its cultural association, its unit design, and a practical HOI4 campaign. The selector must prefer a valid regional alternative over a famous state that creates a broken start.

The event uses curated state pools. It does not choose from every coastal state with one global random list.

## Macroregion registry

The monster roster is divided across twelve operational macroregions.

| Macroregion | Primary monster identities | Geographic purpose |
| --- | --- | --- |
| Northern Atlantic and Arctic | Kraken, Hafgufa, Jormungandr | Norway, Iceland, Greenland Sea, Nordic North Atlantic |
| Baltic | Iku-Turso | Gulf of Finland and Baltic coast |
| Central and Eastern Mediterranean | Scylla, Leviathan | Messina, Sicily, Calabria, Levant |
| Red Sea and Horn | Cetus | Red Sea and Horn coastal states |
| Northwest Pacific | Umibozu, Akkorokamui | Honshu Pacific coast and southern Hokkaido |
| Chinese coast | Jiaolong | Southeastern Chinese coast and curated river mouths |
| Philippine seas | Bakunawa | Central and southern Philippines |
| Bay of Bengal and Indian Ocean | Timingila | Bay of Bengal and Indian Ocean littoral |
| Southwest Pacific | Te Wheke | Cook Strait and Marlborough region |
| Caribbean | Lusca | Andros and Bahamian island pool |
| Gulf of Mexico and Yucatán | Cipactli | Yucatán and Gulf coast |
| South Atlantic | Ipupiara | São Vicente and southeastern Brazilian coast |

Macroregions are selection controls, not new strategic regions. They prevent the baseline wave from concentrating several apexes around one sea while leaving the rest of the world irrelevant.

## Opening roster size

| Start mode | Normal active roster | Meaning |
| --- | ---: | --- |
| Natural baseline | `4` | Global awareness with large untouched regions |
| Natural opening with Evolution I already active | `8` | Multi-ocean crisis with early pact relevance |
| Natural opening with Evolution II already active | `16` | Full global invasion |
| Manual Low | `2` | Focused challenge |
| Manual Medium | `5` | Broad multi-region invasion |
| Manual High | `10` | Most theatres active |
| Manual Maximum | `16` | Complete roster |

These counts are design anchors. The final implementation must run map-validity and outcome-distribution checks. Natural selection may reduce the count when no safe valid candidate remains. A manual Maximum launch should report a blocked identity and refuse a false success if all sixteen cannot be created.

## Two-stage selection

Opening selection should use two stages.

### Stage 1: identity and macroregion

The event builds a candidate list from dormant, content-ready monster identities whose tag, apex unit, leader, focus tree, flag set, landing pool, and cleanup package pass validation.

The selector then chooses identities while favouring:

- one identity per macroregion before a second identity from the same macroregion
- a wide spread across oceans
- regions with valid ordinary coastal hosts
- regions whose appearance will create an actual war
- a mix of combat roles
- a mix of pact preferences
- a mix of large and small theatres

The selector rejects identities whose only remaining landing states conflict with already selected monsters or protected special countries.

### Stage 2: landing state

For each selected identity, the event evaluates that creature's curated landing states in weighted order. The selector stores the chosen state only after every validity test passes.

Identity selection and state selection should not be combined into one opaque random list. A failed state must allow the same identity to try another regional state before the system discards that identity.

## Landing-state validity

A natural landing state is valid when all of these are true:

- the state exists on the installed map
- the state is coastal under the event's saltwater definition
- the state belongs to the creature's curated pool
- the state has at least one land province suitable for ownership and unit placement
- the state has real civilian population
- the state is not already owned or controlled by a full monster country
- the state is not reserved by another simultaneous emergence
- the state is not owned by Cthulhu's Dominion
- the state is not inside an active world-end state that blocks Event 043
- the receiving monster tag is dormant and ready
- the state can support at least one legal hostile neighbour or immediate coastal objective
- the emergence will not create an invalid isolated unit with no land connection inside the state
- no existing special country has an owner-specific protection that forbids transfer

Natural selection should avoid states where the current owner is already a special Chaos country or actual nonhuman country. A scenario launch may allow a broader override only when the scenario contract names that conflict and resolves it safely.

## Human-player protection

The event is a Major threat. It may destroy countries. Protection rules should prevent arbitrary immediate elimination, not guarantee safety.

During a natural opening, a candidate receives a severe penalty in selection weight when it is:

- the only state of a human-controlled country
- the only coastal state of a human-controlled country
- the human player's capital state
- a state whose loss would instantly encircle every human division
- a state whose owner is already fighting another active terminal threat
- a state selected by another newly emerging monster in the same opening transaction

The selector chooses another valid state when one exists. It may still select a human capital when the creature's regional pool has no better valid state and the event would otherwise lose a major geographic identity. The opening event must make the local threat clear and provide the normal reaction window.

Force Trigger Mode and the manual scenario may relax natural player protection according to the selected setup. The scenario detail text must state that Maximum intensity can create immediate existential starts.

## Spacing rule

A baseline or Evolution I opening should avoid immediate monster-on-monster borders.

After a landing state is tentatively selected, the event checks:

- direct land adjacency to every selected monster landing
- whether the two starts share a small island group that will force immediate contact
- whether the same ordinary host will be split between multiple monster starts
- whether one start cuts off the other's only expansion path
- whether the two capitals fall inside the same compact sea theatre

A candidate that fails spacing returns to the state pool. If no alternative state exists, the system tries another identity. It reduces the final roster before it forces a crowded setup.

Evolution II and manual Maximum still avoid duplicate states and invalid unit placement. They may allow closer starts because global saturation is the intended result.

## Curated landing pools

Each monster needs a primary pool, secondary pool, and emergency regional fallback. Exact state IDs belong in the map-audited implementation matrix. Names below define the intended geography.

| Monster | Primary pool | Secondary pool | Emergency regional fallback |
| --- | --- | --- | --- |
| Titanus Kraken | Norwegian Atlantic coast | Northern Norwegian or Skagerrak coast | Faroe or adjacent Nordic coastal state if represented safely |
| Titanus Scylla | Sicily near Messina | Calabria near Messina | Southern Italian or nearby island state inside the same theatre |
| Titanus Leviathan | Levantine Mediterranean coast | Eastern Mediterranean coast | Cyprus or another connected eastern Mediterranean state |
| Titanus Cetus | Red Sea and Horn coast | Southern Red Sea coast | Joppa or nearby Levantine coast when the African anchor is impossible |
| Titanus Hafgufa | Iceland | Greenland Sea coast | Far North Atlantic island or Arctic coastal state |
| Titanus Jormungandr | North Atlantic Nordic coast | Norwegian Sea or Icelandic approach | Another large North Atlantic coastal state with room to expand |
| Titanus Iku-Turso | Gulf of Finland | Northern or central Baltic coast | A Baltic island or adjacent coastal state |
| Titanus Umibozu | Pacific Honshu | Other eastern Japanese coast | Nearby Japanese coastal state with a valid land front |
| Titanus Akkorokamui | Southern Hokkaido | Other Hokkaido coast | Northern Honshu when Hokkaido cannot support a safe start |
| Titanus Jiaolong | Southeastern Chinese coast | Lower Yangtze or Pearl River mouth coast | Another southern Chinese coastal state connected to its river registry |
| Titanus Bakunawa | Central Philippines | Southern Philippines | Another populated Philippine island state |
| Titanus Timingila | Bay of Bengal | Eastern Indian or Bangladeshi coast | Northern Indian Ocean littoral state |
| Titanus Te Wheke | Cook Strait and Marlborough | Lower North Island or upper South Island | Another New Zealand coastal state with a usable front |
| Titanus Lusca | Andros and Bahamian state | Another populated Bahamian island | Northern Caribbean island state when the Bahamas cannot support a tag |
| Titanus Cipactli | Yucatán coast | Gulf of Mexico coast | Caribbean-facing Mesoamerican lowland state |
| Titanus Ipupiara | São Vicente and southeastern Brazil | Nearby Brazilian Atlantic coast | Another populated South Atlantic Brazilian state |

The implementation map audit can reject a named pool when HOI4 state geometry makes it unplayable. It may not move a creature to a different continent for convenience.

## State transfer and emergence footprint

A natural emergence starts with one state.

The event should not grant a free multi-state country at baseline. One-state starts preserve regional pressure, give defenders a chance to react, and make the first conquest meaningful.

The landing transaction must:

1. save the ordinary host and chosen state
2. verify that the tag is dormant
3. write Event 043 origin and creature identity markers
4. transfer ownership and control of the chosen state
5. set the state as the first lair and capital
6. create the leader and country identity
7. load the creature's focus tree
8. create the apex division in a valid province
9. create the support package for the active evolution and scenario intensity
10. apply the correct nonhuman and special-country markers
11. initialize Hunger and Sea Bond
12. seed the country into the active-monster array
13. establish initial wars
14. send local and global reports
15. record one emergence receipt
16. clear every temporary target and reservation used by the transaction

Each step must be idempotent against a duplicate call. A partial transaction needs explicit failure cleanup. It cannot leave a living tag with no apex, a transferred state with no country setup, or a unit under the former host.

## Capital and lair

The landing state becomes the monster country's capital and first registered lair.

The lair provides:

- a large Sea Bond contribution
- a Hunger recovery source
- one protected spawn location
- the first focus and decision anchor
- a visible state modifier
- a target for human counterplay
- a fallback retreat objective for the apex AI

The modifier should describe the visible monster presence and local effects. It must not expose raw hidden reinforcement weights.

A monster can register additional lairs through focuses and decisions. Lairs require controlled coastal states, valid ports or coastal terrain, and a creature-specific cap. Losing a lair removes its benefits after a short confirmation window.

## Initial support package

The baseline package should be strong enough to prevent the apex from being surrounded on the first day.

Recommended baseline shape:

- one apex division
- two to four support divisions selected from the creature's primary families
- a small bounded reserve receipt that can create one later support unit after the first objective
- no ordinary stockpile
- no free passive monthly reinforcement

Evolution I should increase the package and begin the country farther along its early focus route. Evolution II and manual Maximum should provide a larger landing force, but the apex remains the only formation that can defeat a major army by itself.

Final numbers require combat testing. The planning target is that the baseline apex wins against six to ten contemporary infantry divisions in favorable coastal conditions. It should need support to survive a sustained attack by twelve to sixteen well-supplied divisions. Specialist preparation, air power, encirclement, and a severed Sea Bond should produce a credible kill.

## Initial wars

After emergence, a monster declares war on every valid ordinary country that:

- owns a state directly bordering the monster country
- owns another part of the monster's landing state only when map structure makes that relevant
- owns a nearby coastal state reachable within current operational range
- is not already protected by a terminal conflict rule
- is not a full monster country
- is not a valid pact partner under an already active manual setup

The initial transaction should normally create at least one war. A landing candidate with no reachable ordinary target has very low or zero natural weight.

The war goal is an Event 043 monster-conquest goal. It should support the special surrender and apex-death rules. A normal annexation war goal that creates unsuitable peace conferences can be used only after exact behavior is proven.

## Frontier war refresh

A monster does not scan every country each day.

War targets refresh when one of these events occurs:

- the monster gains or loses a state
- the monster completes an inland-range focus
- an adjacent country is released, annexed, or changes control
- a pact changes monster relations
- a bounded event-owned frontier pulse runs for active monster countries
- a manual scenario completes setup

The refresh builds a short candidate set from current borders and registered near-coastal reach. It rejects landlocked targets outside range.

## Ordinary monster hostility

Full monster countries begin hostile to one another. They do not receive an immediate scripted war when their starting states are far apart.

When two full monsters later become legal neighbours or contest the same coastal objective, an event-owned rivalry check can create war after a short delay. A valid truce, compact, faction, or terminal sequence blocks that war.

The system should avoid war declarations that immediately break an active pact because one country's expansion touched another's border. Pact betrayal requires its own action or crisis.

## Saltwater coast definition

The sea tether depends on salt water, not any state with a generic coastal flag if that flag includes enclosed freshwater shorelines.

Implementation must inspect the installed map and establish a maintained registry of valid saltwater coastal states. The registry can begin from engine coastal data, then exclude false positives and inland-lake cases.

A valid saltwater coast should connect to:

- an ocean
- a sea connected to an ocean
- a strait or gulf that is part of that marine system
- a coastal island state

A freshwater lake coast does not set depth `0`. A route may create a separate creature-specific exception, but that exception cannot silently redefine the shared map.

## Inland-depth registry

Inland depth is calculated from physical state adjacency.

- depth `0`: valid saltwater coastal state
- depth `1`: land-adjacent to depth `0`
- depth `2`: land-adjacent to depth `1`, with no shorter path
- depth `3`: land-adjacent to depth `2`, with no shorter path
- depth `4+`: all deeper states

The full installed map should be processed into an explicit state-depth registry or generated script data. Runtime play should read the result. It should not perform a breadth-first world scan during every battle or every AI pulse.

The generation tool and resulting registry need documentation, checksum evidence, and a test that every land state receives one depth. Map updates require regeneration.

## Islands and disconnected landmasses

An island state with a saltwater coast is depth `0`.

A multi-state island can contain depth `1` or deeper interior states if its state adjacency supports that result. The event should not treat an entire large island as coast when only its outer states touch the sea.

A disconnected overseas state uses its own nearest coast. Depth does not travel through the owning country's capital or supply network.

## River-corridor exception for Jiaolong

Jiaolong can unlock a curated river registry.

A valid river-connected state can count as one depth shallower for Jiaolong only when:

- the state belongs to the approved river corridor
- the corridor remains connected through controlled or contested valid states
- the route focus is complete
- the adjusted depth does not fall below `0`
- the route's maximum operating depth still applies

This rule should cover major southeastern Chinese river access first. Expansion to foreign river systems requires later route content and separate map validation.

The visual and tooltip language should describe flood-dragon access along river corridors. It should not claim that every HOI4 river graphic creates a navigable route.

## Marsh and lowland exception for Cipactli

Cipactli can unlock a curated marsh and lowland adaptation.

An approved state can count as one depth shallower when:

- it belongs to the maintained marsh or lowland registry
- it remains within the route's geographic and operational cap
- the focus route is active
- the adaptation does not permit arbitrary mountain or desert penetration

The registry should begin around Yucatán, Gulf lowlands, and connected terrain. It can expand after conquest through bounded route milestones.

## Creature resistance to inland weakness

Every apex and support family follows the shared depth model. Creature profiles modify penalty strength.

Suggested resistance categories:

| Category | Intended users | Meaning |
| --- | --- | --- |
| Extremely coast-bound | Hafgufa, Kraken, Lusca | Severe weakness begins early and range expands slowly |
| Coast-bound | Umibozu, Bakunawa, Te Wheke | Strong island and coastal play with poor deep inland operation |
| Balanced | Scylla, Leviathan, Cetus, Iku-Turso, Akkorokamui, Timingila, Ipupiara | Standard progression |
| Adaptive | Jormungandr | Better late landward route with high Hunger pressure |
| Corridor adaptive | Jiaolong, Cipactli | Special terrain or river adjustments inside bounded registries |

The categories guide tuning. They are not separate public values.

## Operational-range tiers

Every full monster country has a current operational tier.

| Tier | Ordinary legal depth | Core rule | AI behavior |
| --- | ---: | --- | --- |
| Littoral Predator | `0-1` | Coastal cores and selected depth `1` states | Avoids deeper plans |
| Landward Adaptation | `0-2` | Can integrate permitted depth `2` states | Considers shallow hinterland |
| Continental Hunger | `0-3` | Can integrate permitted depth `3` states | Opens deeper targets at high cost |
| Terminal Unbound | unrestricted or nearly unrestricted | Cthulhu-only deep integration | Treats inland countries as normal targets |

A specific monster can start with a narrower effective band or gain resistance modifiers inside the same tier.

## Combat penalty direction

The final penalty values must be tuned through live combat evidence. The design direction is:

- depth `0`: full profile
- depth `1`: small attack, movement, recovery, and organization pressure
- depth `2`: clear attack, defense, breakthrough, movement, and recovery pressure
- depth `3`: severe combat and movement pressure
- depth `4+`: ordinary monster AI treats offensive operation as invalid

Supply use may rise inland if the modifier can be made reliable for equipment-free nonhuman units. Population and equipment must never be removed as a depth penalty.

Sea Bond modifies the same pressure. A monster with very high Sea Bond can tolerate its legal inland edge. A monster whose ports have been severed suffers more even at the same depth.

## Cores and occupation

A full monster country may core:

- its original lair
- controlled depth `0` states that meet its route rules
- controlled near-coastal states inside current operational range
- creature-specific corridor states when the adaptation applies

Territory beyond current range stays non-core and strategically undesirable. The country should gain no normal compliance or human occupation package that implies civil administration.

If peace or a scripted transfer grants illegal deep territory, the event marks it as out-of-range occupation. AI avoids defending or expanding from it. A later range focus can regularise it. Cleanup can transfer abandoned isolated territory to a valid human successor only through a documented aftermath path.

## Front shape and consolidation

Monster AI should value a connected coastal realm over scattered inland pockets.

The target score favours:

- adjacent coastal states
- ports
- coastal capitals
- naval bases
- supply hubs near the coast
- states connecting two lairs
- islands inside the creature's theatre
- river mouths or marsh corridors for the relevant creatures
- states that close an exposed coastal pocket

It penalises:

- deep interior states
- landlocked states
- mountain corridors with no coastal payoff
- long narrow fronts that sever Sea Bond
- targets requiring passage through an active pact partner
- states already claimed by a stronger allied monster under a pact rule

## Camera and presentation order

The opening camera should not jump sixteen times.

For a normal human player, the event selects one presentation target:

1. the closest emerged monster to the player's territory
2. a monster that seized the player's state
3. the monster with the highest immediate threat score to the player
4. the first registered emergence as fallback

The camera pans to that state for the local report. A global super-event presents the scale without forcing repeated map movement.

A human-controlled monster receives a camera pan to its own lair after setup.

## Emergence delay and simultaneity

The opening is one global incident. Country creation can be staged across a very short bounded setup sequence to avoid scope collisions and allow clean asset presentation.

The player-facing result should feel simultaneous. Setup delays should be measured in hours or one to two days, not weeks. The super-event should occur after the roster is successfully created, so it never announces monsters that failed validation.

Later evolution waves use longer paced delays. They should give existing campaigns time to react between new regions.

## Failure handling

If one selected identity fails during setup:

- clear its temporary state reservation
- roll back any partial tag setup
- remove any partial apex or support units
- restore state ownership only if transfer already happened and a safe receipt exists
- record the failed reason in debug evidence
- try one alternative identity when the opening target count still requires it

The event must not silently reduce a full Maximum scenario to fifteen while presenting sixteen.

## Map implementation evidence

Before implementation is accepted, the map specialist must provide:

- exact state IDs for every primary, secondary, and emergency pool
- saltwater coast registry
- inland-depth registry
- river-corridor registry
- marsh and lowland registry
- adjacency and province-placement checks
- one valid spawn province per landing state
- fallback ordering
- collision results for simultaneous opening sets
- examples at baseline, Evolution I, Evolution II, and every scenario intensity
- a list of rejected famous anchors and the gameplay reason for each rejection

HOI4 MCP map inspection and rewrite are mandatory for any source changes to map registries supported by the installed server.

## End of Part 2

Part 3 defines Hunger, Sea Bond, reinforcement receipts, feeding, lairs, apex death, nonhuman-system integration, and runtime performance.

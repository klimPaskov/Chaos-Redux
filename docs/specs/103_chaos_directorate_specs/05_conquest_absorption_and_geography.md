# 05. Conquest that changes the country

## War follows the frontier

The Directorate declares war on its former controller and every country sharing its new land border as part of arrival. Territory gains trigger a frontier update. Every newly adjacent country becomes an enemy as soon as the game can execute the valid declaration. Strait adjacency and naval proximity are classified separately so neither a sea-zone neighbor nor an arbitrary distance becomes an unexplained land border.

The legal-owner case from Part 02 also prevents a remote dispossessed owner from blocking the first transfer behind a peace condition. Allies, subjects and guarantees follow the game's supported war-participation rules. The implementation must handle a subject whose overlord owns declaration authority by involving the correct sovereign. It must not leave an adjacent subject permanently immune because the wrong tag rejected the declaration.

No independent war is opened against the Directorate itself, its dead historical tags or a country already in the same conflict as an enemy. The target list is built from live state and country identity, then rechecked immediately before declaration. A new country released along the frontier becomes a new target. A country ceasing to exist before dispatch consumes no stale action.

The Directorate cannot enter a lasting negotiated peace, become a puppet, join a protective faction or accept a treaty that ends its conquest purpose. Protect its wars from shared white-peace and peace-making Chaos systems through an explicit hostile-actor contract. If a native forced settlement still occurs, retain the hostility target and resume a valid war through the next bounded owner update. Do not globally disable peace for unrelated wars.

Its diplomacy is visible and consistent. Threatened countries receive the same military enemy the map shows. A diplomatic report never postpones the attack to give an artificial preparation month.

## Growth has two distinct forms

| Kind of gain | What is retained | What can be lost |
| --- | --- | --- |
| Live territorial capacity | Factories, local resources, infrastructure, bases, access to recruits and connected supply | Lost control removes the corresponding current contribution |
| Absorbed knowledge and converted reserves | Proven technology, licensed capability, equipment actually transferred and one-time industrial salvage already delivered | Consumed reserves stay consumed. Captured equipment can be lost in combat, but a recapture cannot recreate the same shipment |

This distinction gives conquest a durable snowball without turning every province exchange into a money printer. The country remembers what it learned. It does not continue operating a factory that the enemy now controls.

### State absorption sequence

On the first committed control gain, remember the state, source authority, episode and before-transfer measurements. Native occupation supplies its ordinary benefits once. Every captured state starts on fast exploitation. Deeper restoration is the paid Reconstruction action in Part 07, the only place this choice is made.

Fast exploitation yields useful output and military access immediately, with heavier repair demand, resistance and strain. Restoration preserves more infrastructure and increases long-run throughput, with an upfront allocation of civilian capacity and equipment. Neither path waits for an ideology branch or excludes the other forever. Starting Reconstruction later works on the remaining physical capacity and never grants the original one-time benefit again. Fast exploitation trades long-run throughput for early output and leaves the state carrying its repair demand, resistance and strain until restored, so a recently taken state that has not been restored is where resistance denial and counterattacks cost the Directorate most.

Use the actual native occupation and compliance systems wherever they support this behavior. New state records hold only owner, version, already-accounted contributions, pending transaction and review date. They do not create a second public compliance meter. A captured state's processing date survives a controller change.

| Asset | Absorption rule | Anti-duplication boundary |
| --- | --- | --- |
| Population | Mobilize access to the real controlled population using the Directorate's laws and logistics | Recruitment is not a new civilian population addition. Deaths and displacement use their shared owners |
| Military and civilian industry | Benefit from actual surviving buildings, then repair and expand them | Native occupation output is not counted again as a second factory grant |
| Infrastructure, rail, hubs, ports and airfields | Preserve, repair and join them to current theaters | A destroyed or disconnected asset cannot remain fully credited |
| Equipment stockpiles | Transfer only measured usable concrete equipment through a proved native or owner transaction | Debit the source and credit the boss once. No guessed percentage multiplied by every captured state |
| Fuel and strategic reserves | Capture the quantity the supported transaction actually transfers | Capacity and stored quantity are different. A storage building is not a fresh full stockpile |
| Research capacity | Retain useful established knowledge and allocate real laboratories and new generic staff | Do not duplicate exclusive named scientists, steal a living character token or fabricate project-source history |
| Special facilities | Capture real facilities on territory under Directorate control and repair them | Existing facilities do not bypass the one-per-state special-facility group limit |
| Existing Chaos installations | Ask the owning system to adopt or operate the specific site | Use the real source identity, pending orders and remaining reserves. Do not replay a parent event's setup |
| Enemy divisions | Defeated formations contribute only native supported capture, salvage or an explicitly proved owner operation | Whole-army annex transfer is not assumed. No damaged formation is silently recreated at full strength |

Countries are absorbed through actual war and supported annexation or control settlement. Seizing a capital does not authorize taking unrelated unoccupied territory through a private shortcut. If a country capitulates under normal game rules, the resulting state control is evaluated as it actually exists. Territory held by another resisting country is not gifted to the Directorate because the old legal owner capitulated.

### Ownable impassable administrative territory

Every ownable fully impassable state has an explicit conquest route. Prefer the ordinary supported military settlement when it already changes that state's real ownership and control. Where physical occupation cannot occur, an event-owned administrative settlement may process that exact state only after a verified military-defeat receipt for its actual wartime legal owner. A lost capital, a guessed victory score, nominal alliance leadership or a private defeat flag is insufficient.

The receipt records the defeated owner instance, the real belligerents, the specific state and its before-settlement controller. All combat-occupiable states of that defeated authority on the same continent must already be directly controlled by the Directorate through war or the supported native defeat outcome. The impassable state must still belong to the defeated authority's actual settlement and must not be controlled by a separate resisting actor. These conditions prevent this rule from transferring a third country's holdings or remotely clearing a continent after one capital falls.

The supported settlement then changes only the verified eligible impassable state's ownership and direct control, runs the same measured absorption and state-owner callbacks once, and checks the actual result. No credit is granted merely because the request was queued. If the native settlement cannot establish that control, the state remains missing and the configuration is an explicit implementation blocker. The objective denominator is never reduced to avoid the problem.

The same narrow conquest rule applies on later continents. A defeated Directorate uses a separate victor branch because several real enemies may hold its former territory. Require verified wartime military defeat of CXT, actual loss of all its combat-occupiable states to its wartime conquerors or lawful recipients recorded by that same native war settlement, and no remaining CXT military control. Each specific impassable state must still belong to that actual settlement and must not be controlled by an unrelated third actor.

The native settlement identifies the legitimate participating victor or its proved settlement recipient for that exact impassable holding. Preserve all other victors' actual holdings. Do not award every residual state to the final attacker, transfer uninvolved land or invent a recipient from proximity alone. Only the supported actual ownership and control result receives credit. This branch does not independently mark the boss destroyed. The final defeat contract below still verifies all territory and the native country-destruction lifecycle before closing the episode.

## Human populations and anomalous armies

The Directorate is an institution commanding many kinds of forces. It is not globally reclassified as a nonhuman population because some divisions are zombies, ghosts or robots. The current CXT documentation specifically avoids the special-Chaos-country classifier that would scrub camp fixtures. Event 103 needs a dedicated boss-role check, while every shared system receives the correct population and institutional classifications.

The Directorate adopts unrestricted in-game chemical and biological use policy and may operate the mod's coercive systems through their real interfaces. The design does not invent a new civilian casualty loop. Actual population removal is measured once by the shared population-loss transaction, and its Deaths registration records that same debit. Migration is not counted as death. Capturing a camp or quarantine site preserves its existing state ledger and does not restart its scheduled cycle.

This design concerns the mod's fictional game systems and strategic outcomes. Operational buttons use abstract equipment, preparation, target legality and game effects.

## The origin continent is an exact objective

The target set is every ownable land state assigned to the arrival continent in the installed map. It includes disconnected islands, colonial territories, unindustrialized land and remote possessions. A fully impassable administrative state still counts if the game treats it as ownable land. Only null, decorative, sea-only or genuinely unownable map objects are excluded, with an explicit map-audit reason.

Use the engine continent assignment as the authoritative membership, then audit mixed or exceptional states. Do not substitute a list of major countries, mainland-only control, a population share, victory points, a historical border or a percentage less than complete control. The mainland test is an arrival restriction. It is not a reduction of the later continental objective.

The origin set is established for the episode from the installed map. A supported map-changing update must migrate the set explicitly and record the membership change. Changing a country's capital, controller or name never removes a state from the objective.

Live completion means the Directorate directly controls all required states. Allied or subject control does not qualify. Direct control avoids achieving the ending through a nominal puppet network while another country still governs the land. The country may retain a historical first-completion receipt for rewards and achievements, but the terminal check always recomputes the live missing-state result.

Show the controlled-state total and the missing states through a compact objective display backed by the same set as the trigger. The map view allows the player to identify a remaining island without hunting through a hidden checklist. A hover can name its actual controller and reveal which established transport route is relevant. It must not imply that a past completion is still current after a counterattack.

## Reaching the last territory before the ending

The continental campaign develops transport capability in parallel with land conquest. It does not wait for the terminal focus or the ending flag.

| Geography problem | Available solution | What still has to be achieved |
| --- | --- | --- |
| A landlocked foothold | Immediate coastal target selection, transport knowledge and reserve equipment | Win a land route to a legal coast |
| A nearby island | Convoys, invasion planning, aircraft and a concentrated escort or coastal combat fleet | Secure basing and the native sea or air conditions |
| A heavily defended island | Sustained fleet and air buildup, alternate landing points, airborne support and disruption operations | Defeat interception and hold a real beachhead |
| A distant possession on the same continent | A chain of captured or legally established staging bases and sufficient convoy range | Protect the route and supply the landing |
| A target beyond ordinary delivery range | A verified existing portal, exceptional transport or other owner-provided Chaos capability | Meet that capability's real physical requirements |
| A technical route unavailable without DLC | The supported base-game operation with comparable strategic effect and cost | Prove target, travel, loss and counterplay behavior in that configuration |

Naval production and deployment scale to the obstructing force, the number of routes and the tonnage needed for the assigned invasion army. Initial planning anchors seek local superiority of roughly 1.5 times the relevant defending fleet or air strength, with a viable minimum even when the current opposing fleet is small. This is an objective for materialized ships and aircraft, not a declaration that every sea zone is automatically safe.

Airborne operations do not become unlimited teleportation. Ports, aircraft, range, air conditions, transport capacity and landing survival still matter. Exceptional transport uses a real registered owner capability with its own interception or disruption mechanics. If a provider cannot deliver the promised route in the installed configuration, that is a capability blocker to repair before release. Annexing the island automatically is not the fallback.

## Outward expansion while the ending is gated

The first continent is the priority, not a peace boundary. The Directorate also attacks new neighbors on another continent as its border reaches them. Once its origin continent is complete, it can pursue further landings and conquest while Chaos is too low or the ending is disabled. It retains the first continent as a defensive priority because losing a state blocks the future ending.

The terminal transition increases worldwide concentration, replacement output, transport reach and strategic aggression. It does not introduce the first working transport system. This makes the same country playable when The Final Boss is launched in a low-Chaos world.

## Defeating the Directorate

Capitulation, a lost capital or a temporary empty state list alone is not enough. The defeat settlement requires every Directorate state to be conquered and its country to be destroyed through the verified engine lifecycle. Resolve occupied ownership, any surviving controlled province and queued country-creation work before marking the episode finished.

The final territory settlement may transfer only territory whose loss is actually established. It must not grant a victor random land, annex an uninvolved country or delete another provider's independent actor. Where several opponents control former Directorate territory, retain their actual control settlement and shared attribution rather than awarding the entire map to the final attacker.

On confirmed destruction, cancel future war dispatch, terminate new deployments, remove the boss's contribution to World Threat, settle or cancel pending operations by their owner contracts, and retain historical achievements and Chaos records. Persistent contamination, physical destruction and civilian aftermath remain governed by their shared systems. Defeat is not a universal clean-up spell.

Before Chaos Always Wins, defeat permanently prevents that branch for this episode. After Chaos Always Wins, defeating the country ends its military conquest but leaves the historical world-end latch and record intact. A queued callback cannot recreate the country or refund it a full army in either case.

# Event 018 Resources Found, Part 2 Decisions, Missions, Diplomacy, and UI

All names in this file are working labels only. They are not final localisation.

## Decision design principle

The decision category should feel like the player is managing a valuable state, not buying abstract bonuses. Actions should use construction capacity, equipment, trains, convoys, manpower, local security, survey confidence, state infrastructure, relations, foreign access, divisions in the state, and time. Political power can appear for diplomacy and bureaucratic measures, but it should not be the main price.

The category should have staged visibility:

| Phase | Visible decision families |
| --- | --- |
| Ordinary field | survey, first extraction, infrastructure, trade office, security patrols, closure |
| Politicized field | concessions, nationalization, smuggling response, border commission, demilitarized talks |
| Deep field | deep drill program, safety rotation, shaft inspection, worker relief, halt lower galleries |
| Sickness field | quarantine, medical crews, compensation, restrict shifts, seal infected gallery |
| Public danger | evacuation, monster hunts, city curfews, anti-tank detachments, collapse lower shafts, close site |
| Breach countdown | emergency sealing, last evacuation, abandon state assets, military cordon |
| Cave Host war | anti-monster coalition, resource denial, hardened lines, evacuation corridors, reclamation missions |
| Aftermath | rebuild, memorial, decontaminate shafts, decide whether to restore ordinary resource production if safe |

The UI should show only the families that match the current phase. Obsolete basic actions should close after the public danger phase.

## Field management values and effects

### Field richness

Field richness measures total event-added resource value in the state. It is visible. It affects trade interest, foreign offers, local dependence, and the reward for keeping the site open.

Field richness rises through:

- baseline deposit
- evolved opening deposits
- expansion decisions
- deep survey success
- foreign technical missions
- unsafe extraction breakthroughs
- Evolution III all-resource surge

Field richness falls through:

- closing the site
- controlled sealing of lower galleries
- state devastation after monster attacks
- Cave Host consuming the origin site in the breach narrative, although the resource value remains as army-capacity history

### Extraction pressure

Extraction pressure measures how hard the owner pushes the site. It should be visible from the beginning because the player is controlling it. It rises through expansion, deep drilling, concession contracts, military survey teams, and export quotas. It falls through safety rotations, controlled pauses, closure, and worker relief.

Extraction pressure should be the main player-controlled risk lever. High pressure increases resource output, investment, and concession value. It also increases worker safety problems, local dependence, smuggling, border tension, and below pressure.

### Worker safety

Worker safety should be visible. It is not only a protective modifier. It changes which events happen, how often sickness ticks, and how expensive it is to keep the site open. A country with high industry and good survey confidence can maintain a safer boom. A desperate country can overwork the field and get more resources quickly, but the event should remember that choice.

Worker safety rises through inspections, medical rotations, shift limits, equipment investment, union or local committee cooperation, and controlled pauses. It falls through deep drilling, concession pressure, military extraction, state damage, public panic, and Cave Host attacks.

### Foreign interest

Foreign interest is visible because it creates decisions and diplomatic events. It should not be a hidden punishment for trade. The player should understand that concessions bring attention. Foreign interest rises from field richness, resource scarcity, concession offers, open trade offices, shared survey missions, smuggling events, and border disputes. It falls through negotiated quotas, owner strength, diplomatic alignment, demilitarized commissions, and closure.

High foreign interest can produce:

- investment offers
- import contracts
- opinion changes
- smuggling
- foreign company events
- military survey demands
- border commissions
- intelligence activity
- resource concession crises
- border war risk

### Local dependence

Local dependence measures how much the state economy has organized around the field. It rises with repeated exploitation, infrastructure projects, foreign company presence, and trade offices. It makes closure more painful. It also affects local support for continuing work despite danger. A high dependence state may resist closure and require compensation.

### Public panic

Public panic appears after public incidents. It should be visible when people can see the danger. Panic rises from monster sightings, worker deaths, city attacks, failed hunts, and evacuation delays. It falls through successful hunts, evacuation, local relief, closing the site, and Cave Host defeat. Panic should reduce local stability or compliance, cause population flight, and drive emergency decisions.

### Below pressure

Below pressure is the hidden danger value. It should remain hidden during the ordinary phase. During the sickness phase, implementation can expose a vague dynamic status rather than the exact number. The player should see that the lower galleries are unsafe and that further extraction increases danger. Below pressure rises from deep extraction, repeated large deposits, low worker safety, high chaos, and ignoring sickness events. It falls from closure, sealing lower galleries, controlled pauses, and successful cave hunts before the breach.

## Decision families

### Survey and confirmation

This family is available after discovery. It raises survey confidence and can reveal better extraction options.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | AI use |
| --- | --- | --- | --- |
| Geological survey | Improve survey confidence and lower surprise risk. | Civilian factory time or construction capacity, small political cost, state access. | High for stable countries and AI owners with industry. |
| Deep core sampling | Raises field richness with higher below pressure. | Civilian factories, support equipment, trains if remote, survey confidence threshold. | AI should avoid unless high resource need or high chaos. |
| Independent assay | Lowers foreign dispute risk by making resource estimates credible. | Political cost, time, possible foreign observer requirement. | Good for democracies and trade-focused AI. |
| Military survey team | Raises security and survey confidence, but increases foreign interest and border tension. | Command power, infantry equipment, support equipment, division in state. | Militarist AI, war AI, threatened owner. |

The survey family should not grant direct flat bonuses as its main point. It changes future risk, decision availability, and the chance of safe resource expansion.

### Extraction and infrastructure

This family grows the field and state economy.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | Risk |
| --- | --- | --- | --- |
| Expand surface works | Adds a smaller resource increase and local construction benefit. | Civilian factory time, infrastructure threshold, manpower. | Low danger, raises local dependence. |
| Reopen old shafts | Adds resource output and raises below pressure. | Infantry equipment, support equipment, worker safety threshold. | Medium danger, sickness chance. |
| Build extraction rail | Builds or improves rail and infrastructure in the state or route to capital. | Trains, civilian factory time, steel, control of state. | Low danger, increases foreign interest because exports become practical. |
| Emergency export quota | Temporary trade or industry benefit, raises extraction pressure. | Stability, political cost, convoy or train access. | Raises smuggling and worker risk. |
| Deep excavation program | Adds large resource output and below pressure. | High survey confidence, support equipment, stability, construction capacity, state not in public danger. | High danger and possible evolution trigger. |

The player should feel a real temptation to use deep excavation. It should be strong enough to matter and dangerous enough to change the event path.

### Trade and concessions

This family turns the discovery into diplomacy.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | Consequence |
| --- | --- | --- | --- |
| Open resource exchange | Improves trade opinion and import relations with resource-deficit countries. | Political cost, survey confidence, not at war with target. | Raises foreign interest. |
| Grant foreign concession | Gains investment or construction benefit from target country. | Relations, target resource need, foreign interest threshold. | Raises foreign influence and local dependence. |
| Nationalize the field | Removes or reduces foreign control, improves domestic benefit. | Stability hit, political cost, possible relation penalty. | Lowers foreign interest slowly, raises border tension if foreign concessions existed. |
| Balance concession blocs | Keeps several foreign partners from dominating the field. | Diplomacy, convoys, survey confidence. | Reduces puppet pressure and border claims, but lowers maximum investment reward. |
| Export cartel talks | Creates a short economic boost if owner has large field richness. | Political cost, trade partners, resource type scarcity. | Major powers may react positively or hostile based on needs. |

Foreign countries should not all receive the same event. Their interest should be targeted. Countries with resource deficit, adjacent claims, major-power status, faction leadership, or local rivalry should be selected first.

### Security, smuggling, and internal order

This family handles state control.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | Risk |
| --- | --- | --- | --- |
| Field security patrols | Reduce smuggling and protect workers. | Infantry equipment, manpower, command power, division or garrison in state. | Can lower local support if overused. |
| Customs crackdown | Reduces foreign interest and smuggling. | Political cost, stability, state control. | Damages relations with suspected states. |
| Local guard contracts | Raises security with low state military footprint. | Infantry equipment, local dependence, money represented by civilian burden. | Can empower local armed groups and reduce worker safety if corrupt. |
| Counterintelligence sweep | Reduces sabotage and foreign influence. | Intelligence exposure or political cost, security threshold. | Foreign backlash if discovered. |
| Worker committees | Raise worker safety and lower panic. | Stability or political cost, local dependence threshold. | Lowers extraction pressure and can annoy concession partners. |

Security decisions should not only spend command power. They should use equipment, manpower, local conditions, and state presence.

### Safety, health, and worker relief

This family is quiet at first and urgent later.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | Consequence |
| --- | --- | --- | --- |
| Rotate crews | Raises worker safety and lowers sickness risk. | Manpower, support equipment, reduced extraction pressure. | Slows output. |
| Medical survey camps | Reduces sickness deaths and reveals the Wasting Cut stage. | Support equipment, civilian factory time, local dependence. | May uncover worse symptoms. |
| Compensation fund | Lowers panic and local resistance to closure. | Civilian factory burden or political cost. | Does not reduce below pressure. |
| Halt lower galleries | Lowers below pressure and extraction pressure. | Loses temporary output, local dependence anger. | Can block Evolution IV if done early enough. |
| Seal infected shaft | Strongly reduces below pressure at cost of resources. | Support equipment, engineers, stability, worker safety. | May destroy part of the deposit. |

Safety decisions should have visible tradeoffs. They should not be tiny modifiers. They are the main tool for a player who wants the resource boom without the cave path.

### Evacuation and public danger

This family appears after public monster incidents.

Decision roles:

| Working label | Gameplay role | Cost and requirement direction | Consequence |
| --- | --- | --- | --- |
| Evacuate mining towns | Reduces population loss and panic. | Trains, convoys if coastal, manpower, civilian factory burden. | Local production drops. |
| City shelter program | Reduces city attack deaths. | Civilian factories, support equipment, control of VP city or urban state. | Slows construction. |
| Cordon the site | Reduces attacks spreading from site. | Divisions in state, infantry equipment, command power. | Raises local dependence anger and slows output. |
| Armed cave hunt | Reduces monster pressure and can delay breach. | Infantry equipment, support equipment, anti-tank or artillery, divisions in state. | Failure causes military casualties and panic. |
| Collapse lower shafts | Major anti-breach action that can close the site or destroy most event-added resources. | High cost in equipment, construction capacity, and stability. | Prevents Cave Host if completed before final breach threshold. |

Evacuation should become more urgent if the field contains a VP, high population, or nearby city. Public panic can push population flight from nearby states if not handled.

### Closure

Closure is always a major decision once the field is open. It is the cleanest way to avoid the final cave branch.

Closure variants:

| Phase | Closure decision role |
| --- | --- |
| Ordinary field | Close the site and lose event-added resources, with local economic anger. |
| Politicized field | Close the site and accept concession penalties, relation damage, and local unemployment pressure. |
| Sickness field | Close lower galleries or close the whole site, with worker relief and compensation. |
| Public danger | Emergency sealing, evacuation, and resource removal. |
| Breach countdown | Last chance closure, extremely expensive, high chance of partial failure if below pressure is already too high. |

The final public danger phase must still allow closure before Evolution IV. This is one of the user's core requirements. The cost can be heavy, but the player must be able to prevent the Cave Host by sacrificing the resource field.

## Timed missions

Timed missions should appear when the state asks the player to do actual work.

Mission examples:

| Mission role | Objective direction | Success | Failure |
| --- | --- | --- | --- |
| Secure the survey zone | Place supplied divisions in the discovery state or adjacent state for a period. | Raises security and survey confidence. | Raises smuggling and foreign interest. |
| Build the extraction route | Complete rail, infrastructure, or supply work before a deadline. | Unlocks safer export decisions. | Raises local dependence without enough safety. |
| Hold the concession line | Keep relations and trade access stable with selected partners. | Investment benefit and lower border tension. | Foreign interest rises and target may fund rivals. |
| Protect the lower works | Keep worker safety above a threshold while extraction pressure stays high. | Adds resource safely. | Triggers sickness incident or worker deaths. |
| Evacuate the settlements | Move population before repeated city attacks. | Reduces deaths and panic. | Public panic rises and deaths tick. |
| Seal before breach | Complete emergency closure before the final threshold. | Prevents Cave Host and removes resources. | Triggers breach event if below pressure is high enough. |

Missions should have varied duration. Ordinary survey missions can be around a few months. Construction and border missions should be longer. Emergency public danger missions can be shorter only because the state is visibly falling apart.

## Foreign country actions

Foreign countries should have actions when they are selected as interested actors.

Foreign action groups:

| Actor type | Actions |
| --- | --- |
| Resource-deficit major | Offer investment, demand export quota, pressure for concession, send survey mission. |
| Adjacent rival | Demand demilitarized access, sponsor smuggling, start border commission, escalate to border war. |
| Faction leader | Offer protection and trade priority, ask for military survey rights, station liaison teams. |
| Ideological rival | Fund local opposition, smear owner as hoarder, prepare border incident. |
| Ally or subject overlord | Request guaranteed supply, fund infrastructure, pressure owner to keep field open. |
| Black market actor | Smuggling events, theft, sabotage, local guard corruption. |

Foreign actions should use AI weights. A democracy with good relations may offer investment. A fascist or militarist rival with claims may escalate. A communist sponsor may push nationalized worker control or aid. Neutral trade powers may avoid war and seek access.

## Demilitarized field mechanic

Evolution I can make the site demilitarized through pressure or negotiation. The demilitarized field is not always a punishment. It can reduce immediate border war risk and improve foreign trade confidence, but it weakens owner security and makes monster or smuggler events harder to contain.

Demilitarized pressure can arise when:

- foreign interest is high
- the state is on a border
- neighbours fear militarization of the resource field
- a concession partner demands protection from state troops
- the owner has stationed many divisions in the state
- world tension is high
- the discovery resource is strategically scarce

Possible outcomes:

| Outcome | Effect direction |
| --- | --- |
| Owner accepts field commission | Reduces border war risk, raises foreign influence, limits local military security decisions. |
| Owner refuses | Reduces foreign influence, raises border tension, may start crisis chain. |
| Owner accepts with guarantees | Requires a stronger diplomatic position, lowers tension, keeps some security options. |
| Owner secretly militarizes | Keeps security actions, risks exposure event and stronger border crisis. |

A demilitarized field should not block monster hunts once public attacks begin. Public danger should override prior commission rules, but foreign countries may react to the owner remilitarizing the state.

## Border war design

A border war can transfer the discovery state if the owner loses. It should be dangerous but not automatic.

Border war conditions should include several of:

- state borders a claimant or rival
- high field richness
- high foreign interest
- poor relations
- target has resource deficit
- target is stronger or desperate
- owner is at war or unstable
- chaos tier is high
- demilitarized agreement fails
- smuggling or sabotage incidents are unresolved

The border war should be framed as a limited conflict over access, survey rights, or security control. If the challenger wins, the state transfers and the field follows the new owner. If the owner wins, foreign interest drops for that challenger, but local militarization and extraction pressure may rise.

If the state transfer creates an impossible map result, the implementation should use a less disruptive result such as concession control, a temporary occupation modifier, or a claim. That deviation must be reported if used because the user asked for possible state transfer.

## Local state effects

The discovery state should receive meaningful modifiers that evolve.

State modifier directions:

| State status | Modifier direction |
| --- | --- |
| Fresh discovery | resource boom, construction activity, migration, trade traffic |
| High extraction | production boom, infrastructure strain, local dependence |
| Foreign concessions | investment, foreign influence, smuggling risk |
| Demilitarized field | reduced border tension, weaker owner security, stronger foreign observation |
| Unsafe excavation | worker safety penalty, population risk, deep-site danger |
| Sickness stage | population loss, medical burden, lower construction, high worker fear |
| Public attacks | population flight, production disruption, security emergency |
| Sealed site | resource removal, local unemployment, lower danger |
| Cave Host origin | occupied by nonhuman country, origin nest, starting army capacity memory |

The owner can get temporary national spirits if the field is economically important. These spirits should have a lifecycle and not stack forever across repeat firings. Examples include resource boom, concession influence, unsafe extraction scandal, public cave panic, and sealed field recovery. These are working role labels, not final localisation.

## Custom UI concept

The decision category can be enhanced with a compact scripted GUI. It is useful because the player needs to manage several values in one state. If implementation chooses normal decisions only, it must still show values in the category text with scripted localisation. A richer GUI is preferred.

Working UI concept: resource field ledger.

The UI should show:

- state name and owner
- dominant discovered resource and mixed resource icons
- field richness meter
- extraction pressure meter
- worker safety meter
- foreign interest meter
- local dependence meter
- public panic meter after public incidents
- a hidden or vague below pressure status after sickness appears
- current stage seal
- active foreign actor card when a concession or border crisis is active
- closure button and warning state

Suggested interactive areas:

| UI element | Function |
| --- | --- |
| Survey card | Opens survey decisions and shows survey confidence. |
| Extraction card | Shows extraction pressure and available expansion. |
| Trade card | Shows foreign interest and concession status. |
| Safety card | Shows worker safety and sickness risk direction. |
| Security card | Shows smuggling, border tension, and demilitarized status. |
| Panic card | Appears after public attacks. |
| Closure seal | Shows whether the site can still be closed cleanly. |
| Emergency alert frame | Animates when breach risk is high or evacuation mission is active. |

Animation planning pass:

| Animated asset | State logic | Motion direction | Static fallback |
| --- | --- | --- | --- |
| Category seal | active field, rich field, unsafe field, public danger | frame-by-frame glow or hairline crack changes | static field seal |
| Extraction pressure meter | high pressure threshold | subtle pulse on warning frame | static red warning frame |
| Public panic card | public danger active | flicker or trembling warning border | static panic border |
| Closure seal | closure still possible, last chance, impossible after breach | slow lock or collapsing ring animation | static closure seal |
| Cave breach warning | final countdown active | frame-by-frame fissure widening, no text | static fissure icon |

Animations must follow the frame-animation skill. No transform-only pulses, no generated GIF as final asset, and every animated element needs a static fallback.

## AI behavior for owner decisions

AI owner behavior should be route-like even though this is not a focus tree.

AI owner profiles:

| Profile | Behavior |
| --- | --- |
| Stable industrial owner | Surveys first, builds infrastructure, expands moderately, invests in safety. |
| Resource-desperate owner | Expands faster, accepts higher extraction pressure, seeks export value. |
| War owner | Militarizes state, uses military survey teams, prioritizes the resource type needed for production. |
| Weak minor | Accepts foreign concessions, avoids border war if possible, may become dependent. |
| Authoritarian owner | Uses security patrols and nationalization, tolerates lower worker safety. |
| Democratic owner | Uses worker safety, independent assay, balanced concessions, and closure sooner if public danger rises. |
| High-chaos owner | More willing to deep drill, ignore symptoms, and risk Evolution III. |
| Player-adjacent AI | Should avoid triggering Cave Host too easily unless high chaos, desperation, or aggressive personality supports it. |

AI should close the site when:

- public panic is high
- worker deaths are severe
- owner is weak or at war on multiple fronts
- Cave Host risk is high and the owner lacks anti-tank or hard attack
- the state is not economically essential
- a hostile neighbour is likely to seize the state anyway

AI should keep the site open when:

- the resource is strategically essential
- the owner is strong and has safety investments
- the owner is desperate in war
- high-chaos behaviour is allowed
- the owner has already committed to militarized extraction
- a human player is the foreign rival and AI logic supports risky play

## Exploit prevention

The system should avoid:

- infinite resource stacking from cheap repeat decisions
- repeated closure and reopening loops
- foreign investment loops with no diplomatic cost
- free units from security decisions
- border war state transfers that create broken ownership
- using demilitarized status to make the state immune to consequences
- making Cave Host spawn impossible because the player can close after breach
- making Cave Host spawn unavoidable before the public stage
- excessive population loss from multiple simultaneous active deep sites
- AI repeatedly selecting suicidal deep drilling in ordinary chaos

Controls should include one-time flags per field action tier, cooldowns, escalating costs, stage locks, active mission caps, and ownership transfer cleanup. Any simplification must be reported.

## Documentation needs for this surface

The event documentation should explain the field management loop, the values shown to the player, the closure route, the diplomacy and border crisis loop, and the stage split between ordinary resource boom and strange cave danger. It should not disclose hidden final mechanics in the ordinary event detail text. The implementation docs can include full hidden mechanics for developers.

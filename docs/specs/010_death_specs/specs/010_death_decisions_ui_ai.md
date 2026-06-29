# Event 010 - Death: Decisions, Containment, UI, AI, and Player Responses

## Decision design overview

Death needs player responses, but those responses should not appear before the world has reason to suspect a crisis. The decision systems are phased:

1. **Pre-reveal local reports**: small, local, low-information decisions for island owners, nearby naval powers, and attentive players.
2. **Reveal containment**: public decisions to declare war, fortify coasts, hold borders, investigate wastelands, and coordinate against Death.
3. **Emergency compact**: shared coalition decisions once Death is a major world threat.
4. **Dark methods**: optional necromancy decisions to fight Death at moral and political cost.
5. **Black Oath**: alternate path to pledge to Zol and join Death's side, with heavy risks.
6. **World-end emergency**: last-stage decisions for continental footholds and global evacuation/containment attempts.
7. **Aftermath**: recaptured wasteland cleanup and memorial/reconstruction work after Death is defeated.

The category should not show every possible decision at once. Visibility must be controlled by reveal state, country proximity, war state, route flags, compact membership, and active stage.

This spec intentionally avoids a separate Death mission layer. The event should use ordinary decisions, targeted decisions, cooldowns, state modifiers, and normal war/occupation gameplay instead of timed missions or objective cards.

## Decision categories

### Local Report: Maritime Errata

Visible only before reveal, usually to:

- the old owner of a consumed island.
- countries with naval bases near the sea zone.
- nearby colonial overlords.
- players with an intelligence/recon hook.
- countries that have already received one delayed marine-office packet.

Purpose: let attentive players discover the crisis without telling everyone.

Decisions:

| Decision | Availability | Cost/requirement | Result direction | AI |
| --- | --- | --- | --- | --- |
| `Send a Survey Boat` | First delayed packet. | Convoys, fuel, small command power, nearby port. | Chance to discover Death origin or reduce report delay. Can fail if Death already spread. | Naval/local owners likely. |
| `Check the Telegraph Office` | Owner or colonial overlord. | Political attention plus civilian factory admin burden for a short duration. | Reveals whether the island's state owner/controller changed and may open quiet investigation. | Bureaucratic powers likely. |
| `Issue Harbor Sanitation Notices` | Owner of nearby island/coast. | Stability or trade opinion cost, convoys, and supply. | Slows Death targeting that country's nearby islands and raises local concern. | Rare before repeated packets. |
| `File It Under Weather` | Always for packet recipient. | None. | No immediate cost. Increases ignored-file memory and slightly raises later spread/reveal shock. | Isolationist or distracted AI. |

These decisions should not use only political power. Survey and quarantine should require concrete naval/logistics capacity.

### The Death Country

Visible after public reveal to countries that:

- border Death.
- are at war with Death.
- are major powers.
- control coastal states on a continent with Death.
- are members of the Living Containment Compact.
- have received a direct Death event.

Header should show a compact status summary:

- Death consumed-population band, not exact hidden formulas.
- active stage: `Remote Reports`, `Public Death`, `Black Continent`, `Last Shores`.
- ghost tier if known.
- number of Death-controlled states.
- whether country is in the containment compact.
- whether coastal jump risk is low, rising, or critical.

Decisions:

| Decision | Availability | Cost/requirement | Result direction | AI |
| --- | --- | --- | --- | --- |
| `Recognize the Death War` | Death revealed, not at war, plausible reach. | War support threshold or war support hit, command power, diplomatic cost. | Declares war or joins containment war. | High for neighbors/majors, low for distant minors. |
| `Request the Living Compact` | Death revealed, enough threatened countries. | Diplomatic credibility, relations, maybe existing faction leader consent. | Creates or joins containment compact without always forcing faction changes. | Majors and threatened states. |
| `Open Coastal Watch Stations` | Coastal country after reveal. | Convoys, trains, support equipment, fuel, naval base or coastal states. | Reduces coastal jump target chance in owned/coast-adjacent states. | High for coastal majors and nearby minors. |
| `Mark Low Islands for Evacuation` | Owns small islands and Death hidden/revealed. | Convoys, stability, temporary consumer goods, refugee capacity. | Reduces future civilian death if those islands are consumed. It can create refugee pressure. | Rare before reveal, high after reveal. |
| `Fortify the Quarantine Line` | Borders Death. | Infantry equipment, support equipment, command power, divisions in target states. | Applies state quarantine line and slows or pauses withering. | High for direct neighbors. |
| `Flood the Shore Roads` | Owns target coastal/border state. | Infrastructure damage, trains, command power. | Slows Death movement/withering but hurts own logistics. | Desperate AI only. |
| `Hold the Census Posts` | At war with Death and high consumed-population band. | Administrative burden, stability, divisions present. | Reduces ghost scaling or delays ghost spawn locally by keeping records/names. | High if fighting Death and stable enough. |
| `Authorize Wasteland Entry Gear` | At war or bordering Death. | Support equipment, trucks, fuel, army XP. | Temporary reduction to attrition/strength loss in Death states. | High before offensives. |
| `Establish a Dead-Zone Outpost` | Controls recaptured wasteland. | Engineers, support equipment, trucks, trains, supply connection, per-state cooldown. | Applies a recaptured outpost modifier with milder penalties and clearer logistics. No timed mission. | Only if state strategically important. |

### Living Containment Compact

This is a coalition/compact layer. It can create a faction if the campaign state allows it, but it should also support countries that remain in existing factions. The system should not break major alliance structures just to force a new faction.

Compact goals:

- coordinate war entry.
- share military access against Death.
- send equipment to border states.
- reduce coastal jump risk through patrol networks.
- fund wasteland-entry gear.
- mark threatened states.
- prevent AI countries from ignoring a revealed Death neighbor.

Compact values:

| Value | Meaning | What changes it |
| --- | --- | --- |
| `compact_cohesion` | Willingness of countries to cooperate against Death. | Success/failure in containment, ideology tension, casualties, Death spread. |
| `watch_network` | Coastal detection and patrol coverage. | Coastal watch decisions, naval bases, convoys, fuel, AI contributions. |
| `front_readiness` | Ability to occupy Death without withering away. | Wasteland gear, divisions, supply lines, engineer projects. |
| `public_panic` | Political pressure from Death reports. | Consumed population, reveal events, failed defenses, evacuation failures. |

Compact decisions:

| Decision | Cost/requirement | Result |
| --- | --- | --- |
| `Call the Living Conference` | Major/threatened country, Death revealed, at least two eligible invitees. | Creates compact framework or strengthens existing compact. |
| `Share Wasteland Entry Gear` | Support equipment, trucks, fuel, and compact membership. | Gives target member temporary attrition/strength-loss reduction. |
| `Open Military Access Corridors` | Relations/compact cohesion. | Members grant access for anti-Death operations where safe. |
| `Joint Coastal Patrol Plan` | Convoys/fuel/naval capacity from members. | Raises watch network, slows coastal jumps. |
| `Compact War Declaration` | Compact cohesion and threat threshold. | Pulls willing members into war against Death. Refuses unwilling members with events. |
| `Emergency Refugee Shipping` | Convoys, stability, consumer goods burden. | Evacuates population from likely coastal or island targets, causing domestic costs. |

Compact failure states:

- low cohesion causes members to refuse war entry.
- high public panic increases stability costs.
- poor watch network increases coastal jump chance.
- failed front readiness makes offensives bleed strength.
- ideological rivals can accuse each other of using Death for propaganda.

### Dark Methods: Necromancy Against Death

This branch should be useful, frightening, and optional. It should never be the clean best answer.

Implementation status: implemented as living-country containment decisions using `death_black_method_exposure`, `death_bound_names`, and `death_mourning_debt`. The route creates weak capped bound-shade hosts, exposes Black Book offices to scandal pressure, and can be closed for free if the country has only opened the book. After a forbidden method has been used, the route is closed through `Burn the Black Book`.

Unlock conditions:

- Death revealed.
- country at war with Death or controls a recaptured wasteland.
- high casualties, high chaos, or completed black-book investigation.
- not already Herald of Zol.

Values:

| Value | Meaning |
| --- | --- |
| `black_method_exposure` | How visible the country’s forbidden work has become. |
| `bound_names` | Resource used to raise or reinforce anti-Death spectral units. |
| `mourning_debt` | Political/spiritual cost that can trigger backlash. |

Decisions:

| Decision | Cost/requirement | Result | Risk |
| --- | --- | --- | --- |
| `Open the Black Book` | Stability, political legitimacy, captured wasteland or high casualties. | Unlocks dark methods category. | Raises exposure and panic. |
| `Bind the Unburied` | Consumed or recaptured wasteland, support equipment, army XP, mourning debt. | Creates weak bound-shade units that resist wasteland attrition better. | Condemnation/public horror, stability loss. |
| `Interrogate the Empty Road` | Intelligence exposure, command power, divisions in wasteland. | Reveals next likely wither/coastal target band. | Can trigger a Zol attention event. |
| `Seal the Names in Iron` | Trains, support equipment, recaptured wasteland or existing outpost, per-state cooldown. | Reduces local ghost spawn scaling from a recaptured state. | If the state is reconsumed, the seal breaks and debt/panic can rise. |
| `Burn the Book` | Only after using dark methods. | Removes branch and reduces exposure. | Loses bound units and may trigger backlash if debt high. |

AI should use dark methods only when desperate, authoritarian, high chaos, or on the edge of collapse. Democracies should generally avoid it unless Death is at world-end and no normal route remains.

### Black Oath: Joining Death

The alternate join-Death path should be playable but dangerous. It is not a normal alliance with Death.

Implementation status: implemented as the Herald route. `Whisper to Zol` prepares the route, `Take the Black Oath` applies the Herald of Zol cosmetic identity and Black Oath idea, Herald service decisions manipulate name debt/black favor/living disgust, and Black Apostolate is a hidden player-only culmination after world-end thresholds.

Unlock conditions:

- Death publicly revealed.
- country borders Death, is losing a war against Death, or controls a recaptured wasteland.
- high chaos or severe instability.
- player choice, or extreme AI desperation.
- country is not a special nonhuman country.

Core rule: a Herald is not safe. It is merely not first.

Black Oath values:

| Value | Meaning |
| --- | --- |
| `name_debt` | What the country owes Zol. If it rises too high or goes unpaid, Death can consume Herald states. |
| `living_disgust` | Diplomatic hostility from non-Herald countries. |
| `black_favor` | Temporary power gained from serving Death. |

Decisions:

| Decision | Cost/requirement | Result | Risk |
| --- | --- | --- | --- |
| `Whisper to Zol` | High chaos or near Death border. | Opens oath event chain. | Relations loss if exposed. |
| `Take the Black Oath` | Player confirmation, stability/war support loss, leaves compact. | Country becomes Herald of Zol. | War with containment members, name debt begins. |
| `Offer a Prison Census` | Manpower/prisoner abstraction, stability, exposure. | Gains black favor, may spawn weak Herald units. | Raises name debt and condemnation. |
| `Open a Dead Port` | Coastal state, convoys, high risk. | Helps Death coastal jump or reduces Death hostility toward Herald. | Death may consume the port later. |
| `Feed the Border` | Sacrifice a low-pop border state or allow withering. | Large black favor. | State becomes wasteland and causes massive domestic backlash. |
| `Break the Oath` | High compact support or successful anti-Death war. | Rejoins living side and removes Herald status. | Death targets the traitor aggressively. |

AI should almost never take the Black Oath. It may do so if:

- chaos is very high.
- country is authoritarian or extremist.
- capital is near Death.
- stability is collapsing.
- no allies are helping.
- Death already controls a large part of the continent.

The path should be disabled for AI countries whose survival is essential to another active event unless a valid alternate exists.

## Fighting decisions and narrow missions

The player response is built primarily from decisions that help countries fight, enter, delay, contain, and recapture Death states. A narrow timed mission is allowed for quarantine-line maintenance because it tests whether the player actually keeps a fortified line bordering Death rather than clicking a permanent defensive buff.

The real map work remains normal HOI4 play: move divisions, hold coasts, occupy Death-controlled tiles, and keep supply open. Decisions should read those facts as availability requirements instead of creating separate objectives. For example, a decision can require supplied divisions in a border state, control of a recaptured wasteland, a nearby port, or a working supply connection. If the requirement is not met, the decision should be blocked with a clear tooltip.

Use decisions with cooldowns, temporary state modifiers, target-state flags, narrow mission checks, and cleanup logic. Do not add broad goal-style mission stacks or auto-completing objective cards for Death unless a later accepted spec explicitly asks for them.

### Border fighting decisions

| Decision | Availability | Cost/requirement | Result direction | AI |
| --- | --- | --- | --- | --- |
| `Strengthen the Quarantine Line` | Owns or controls a state bordering Death. | Infantry equipment, support equipment, command power, supplied divisions in the selected state. | Adds a temporary quarantine-line modifier that slows withering and reduces local attrition pressure. | High for direct neighbors. |
| `Keep the Port Lit` | Coastal state in a Death coastal-jump risk region. | Convoys, fuel, nearby naval base or port, local supply. | Reduces coastal-jump target weight for that state or region for a limited period. | High for coastal countries near Death. |
| `Guard the Dead Road` | Non-Death state neighboring Death. | Supplied divisions present, trucks or trains, command power. | Temporarily blocks or weakens withering into that state while defenses remain plausible. | High if the state protects a capital, port, or supply line. |
| `Burn the Approach Roads` | Border or coastal target state. | Infrastructure damage, trains, command power. | Slows Death movement and withering pressure but damages the owner's logistics. | Desperate AI only. |

### Wasteland entry decisions

| Decision | Availability | Cost/requirement | Result direction | AI |
| --- | --- | --- | --- | --- |
| `Survey the Wasteland` | Controls a recaptured Death state. | Support equipment, trucks, army XP, supplied divisions. | Reveals the local cleanup/outpost path and applies a short attrition-reduction modifier. | Medium, higher for strategic states. |
| `Build the Dead-Zone Outpost` | Controls a recaptured wasteland with supply connection. | Engineers, support equipment, trucks, trains, temporary construction burden. | Applies a recaptured outpost modifier. It does not restore population or industry. | Only for ports, chokepoints, capitals, or supply routes. |
| `Seal the Empty Port` | Controls a recaptured coastal wasteland. | Convoys, trains, support equipment, fuel. | Reduces nearby coastal-jump chance and makes the port safer for anti-Death operations. | High if the coast is still threatened. |
| `Issue Wasteland Entry Orders` | At war with Death or bordering Death. | Support equipment, trucks, fuel, army XP. | Temporary reduction to attrition and ticking strength loss while operating in Death states. | High before offensives. |

### Compact support decisions

| Decision | Availability | Cost/requirement | Result direction | AI |
| --- | --- | --- | --- | --- |
| `Send Wasteland Entry Gear` | Compact member or major supporting a Death-front country. | Support equipment, trucks, fuel, convoys or land route. | Gives a target country a temporary wasteland-entry modifier. | High for majors when an ally borders Death. |
| `Fund the Watch Network` | Coastal compact member. | Convoys, fuel, naval access, civilian factory burden. | Raises watch-network strength and lowers coastal-jump pressure. | High for naval powers. |
| `Authorize Compact Access` | Compact member, target member at war with Death. | Relations, compact cohesion, diplomatic cost. | Grants or requests military access for anti-Death operations where possible. | High if access creates a valid front. |
| `Coordinate Border Relief` | Compact member with equipment and reachable threatened ally. | Infantry equipment, support equipment, trains or convoys. | Helps a threatened country strengthen a border state. | High when the target is losing a front. |

## Custom UI: The Black Atlas

Death uses a compact scripted GUI window after reveal. The Black Atlas summarizes the current stage, consumed population, coastal risk, wither-line pressure, compact posture, and forbidden-route exposure without replacing normal map play. It is a transient decision-category dashboard: it does not include a separate close button or standalone decorative status icons, and consumed population is displayed in `K`, `M`, or `B` bands.

### Entry point

A decision category button: `Open the Black Atlas`.

### UI tabs or panels

| Panel | Player sees |
| --- | --- |
| `The Black Map` | Consumed-state count, Death-controlled states, continent status, current footholds. |
| `The Census` | Consumed-population band, ghost tier, public panic band, death-log link if enabled. |
| `Coasts` | Coastal jump risk by broad region, watch-network strength, active watch decisions. |
| `The Line` | Neighboring wither targets, quarantine status, border decisions. |
| `The Compact` | Compact members, cohesion, war-entry status, shared support actions. |
| `Forbidden Methods` | Only if unlocked. Black-method exposure, bound names, oath risk. |

### Information discipline

The UI should not reveal exact hidden next targets before the player has earned intelligence. It can show target bands and risk levels: `quiet`, `watched`, `thin`, `open`, `critical`.

### Animated presentation pass

The Black Atlas receives an animation pass because it represents a living supernatural map threat.

Planned animated assets:

| Asset | State logic | Direction |
| --- | --- | --- |
| `death_black_atlas_header_animated` | Visible after reveal. | Slow dark fog drift, generated frame-by-frame, static fallback. |
| `death_zol_portrait_world_end_animated` | World-end or Herald oath. | Void-lit Zol portrait frames, static fallback, and registration in `interface/chaosx_characters.gfx`. |

Animation should clarify state. If a surface becomes too busy, keep only the header and critical warning animation.

## DTH Category: The Black Ledger

The Black Ledger is visible only to active Death. It is not a living-country intelligence tool. It shows Death's own counters and available actions: consumed states, island count, mainland count, consumed population, spread pressure, generated soul power, available soul power, spent soul power, host counts, island-spread status, mainland-route status, and ghost-host status.

Black Ledger decisions do not spend political power. They spend soul power, which is generated from consumed states, consumed population, and last-shore footholds after world end begins. Soul power has no storage cap. The category can offer island consumption after Second Shore and an island-spread focus, mainland pressure after Mainland Smell when normal pressure or the living-war bypass allows it, and one host-raising decision for the current ghost stage. Host and spread decisions use the same soul-power budget so manual expansion competes with army growth. Forced island consumption starts at the base island-spread cost, then each successful Black Ledger island consumption raises the next forced island cost by one soul power. Successful Black Ledger mainland consumption raises the next forced mainland cost by two soul power. Each ghost host raised increases later host costs by 0.25 soul power.

The same category must be navigable by AI because Death is usually AI-controlled. AI Death should use island spread while it is still cheap, while it is still building the island pattern and pressure, and while valid empty islands remain. It should prioritize the mainland decision once the route is valid and cheap islands are no longer the better pre-reveal spend, then raise the available host tier when it has a valid spawnable wasteland. It should avoid spending pre-reveal souls on hosts only when those souls are needed for a pending mainland press.

## AI strategy matrix

### Death AI

| Situation | Behavior |
| --- | --- |
| Hidden origin | Do nothing visible. No wars or units. |
| Hidden island spread | Consume low-pop empty islands by scripted pulses and cheap Black Ledger island decisions. Living AI does not choose war decisions while Death has consumed only one island. |
| Reports ignored | Slightly increase spread pressure. |
| Mainland route ready | Spend soul power on the Black Ledger mainland decision before raising hosts unless cheap empty islands are still the better pre-reveal spend. |
| Revealed mainland | Declare war on direct-threat neighbors, wither unguarded states, use Black Ledger mainland or island actions when valid, and remain passive militarily until ghosts. Wider neighbor wars wait for late-stage strength or world-end. |
| 600 ghost tier | Raise weak ghosts through the Black Ledger when a valid wasteland can spawn them and Death is not saving for the mainland route or cheap island spread. Hold lines and avoid offensives. |
| 800 ghost tier | Raise stronger ghosts through the Black Ledger, use pressure-driven coastal jumps after setbacks, and keep normal attacks restrained before world-end. |
| World-end | Aggressive attacks, foothold expansion, intensified withering, and repeated Last-Shore host spending from the Black Ledger. |
| Near defeat | Attempt coastal jump if cooldown and stage allow. No fake capitulation. |

### Neighbor AI

| Country type | Behavior |
| --- | --- |
| Direct neighbor | Join or request compact, guard border states, declare war if not already at war, and prioritize quarantine decisions after Death has more than one consumed island or has reached the mainland. |
| Island owner | Investigate early reports, evacuate low islands if repeated reports or revealed Death. |
| Coastal nearby country | Build watch network, fortify vulnerable ports, join compact if Death on same continent. |
| Major power | Coordinate compact, send equipment, declare if Death reaches mainland or world-end. |
| Minor far away | React only after reveal, world-end, or compact call. |
| Existing faction leader | Prefer compact overlay before dissolving/abandoning existing faction. |
| Democratic AI | High containment participation, low necromancy, almost never Herald. |
| Fascist/communist authoritarian AI | Strong containment if threatened. Dark methods possible under high chaos. |
| Desperate unstable AI | May consider Black Oath only if close to collapse. |

### Herald AI

Herald AI should be rare and unstable. It should:

- feed Death only if black favor is low and name debt manageable.
- avoid sacrificing its capital unless in maximum desperation.
- fight containment countries if already committed.
- consider breaking the oath if Death weakens and living coalition support is nearby.
- never be a reliable normal ally to Death.

### Compact AI

Compact AI should:

- join when Death is revealed and nearby.
- weigh war entry by proximity, strength, ideology, existing war burden, and coastal risk after Death has consumed more than one island.
- prioritize border decisions over generic economy decisions.
- send aid to countries with active Death borders.
- avoid impossible decisions that require absent ports, missing convoys, dead targets, or no route to Death.
- keep some countries from overcommitting if they are already losing a major war.

## Localisation tone

Pre-reveal text: bureaucratic, uncertain, maritime, quiet.

Reveal text: blunt, cold, public recognition.

Containment text: practical and frightened. Governments try to make new categories for something that is not a war.

Necromancy text: grim, euphemistic, self-condemning. Avoid cheap jokes about mass death.

Herald text: cultic but restrained. A government pretends surrender is policy.

World-end text: terminal, spare, no melodramatic filler.

## Exploit and cleanup rules

- No decision should allow infinite free units.
- Bound-shade and Last Watch units need real costs and caps.
- Coastal watch should reduce risk, not permanently block Death everywhere. Strong watch-network coverage can intercept an ordinary low-pressure coastal jump once by spending network strength, while high pressure, No Ferry Returns, and world-end pressure bypass that interception.
- Evacuation should save some future deaths but create refugee/political costs.
- Purification projects should not restore population.
- Heralds should not become immune to Death forever.
- Black Oath should not allow a player to farm Death bonuses without eventual name-debt consequences.
- Compact membership should clean up when Death is defeated, the country capitulates, or the country becomes Herald.
- Temporary wasteland, outpost, watch, and quarantine modifiers should expire or be removed if the state changes controller, is reconsumed, or Death is defeated.
- All temporary variables used for popup outcomes should be cleared by event options, not by an early generic cleanup if options still need them.

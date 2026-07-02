# Event 013 Natural Disasters Spec, Part 1, Core System

## Identity and player promise

Event 013 should become a living disaster season system. It should not feel like a single popup that removes a few buildings. A fired Event 013 creates a sequence of delayed disasters, each with a clear affected area, severe local effects, civilian deaths, and recovery needs. The system should be reusable by other events that want to call one disaster family directly, force a country to suffer a targeted disaster, or launch a broader barrage.

The core fantasy is that the world is becoming less reliable. Railways break under mountainsides, cities lose docks to waves, factories stop under ash, crops fail under hail or drought, and capitals have to choose between fast evacuation, supply repair, public order, and economic recovery. Even the baseline should matter enough that the player remembers where it hit.

Event 013 remains a minor repeatable event, but its internal scale changes by evolution state, chaos level, cluster context, and manual scenario intensity. Repeatable does not mean harmless. It means the world can receive disaster seasons again, with diminishing random-event weight handled by the normal event system and with internal cooldowns preventing the same state from being punished every few days.

## Event firing model

One Event 013 firing creates one disaster sequence. The sequence can contain one disaster, several delayed disasters, or a large global barrage depending on current conditions. The sequence itself is the logged event. The individual disaster pulses inside the sequence are not separate Event Log entries. They may still create report events, news digests, death log rows, recovery missions, state modifiers, super-events, scripted GUI updates, and scenario records.

The firing flow should work like this.

1. The Event 013 entry event initializes a disaster sequence from the selected country or global context.
2. The sequence controller computes intensity, family pool, sequence length, delay range, news policy, and recovery policy.
3. The controller picks the first affected target. That target can be a state, region, country, multi-state area, coastline, river system, volcano group, fault zone, storm corridor, or world-scale abnormal map depending on family.
4. The first disaster pulse fires and applies damage immediately in a hidden effect.
5. A clear report or news event can appear after one to two days if the news policy says the hit is meaningful enough.
6. The controller schedules the next disaster after the computed delay.
7. The sequence ends only after all queued pulses have fired or after cleanup decides that no valid target remains.
8. Affected countries keep recovery decisions and missions until the aftermath is removed, expires, or is resolved by action.

The entry event should use finished in-world text only during implementation. The spec direction is that the first popup should describe the season beginning through concrete reports from the affected area, not through a meta explanation of the event system.

## Delay and pacing rules

Disasters must not all land on the same day. Delays are part of the event identity. The player should experience a season that keeps returning, not a single instant bundle.

Baseline delay should usually be five to ten days between disaster pulses. If the sequence has more disasters, the delay compresses so the season still finishes in a reasonable time. Evolution I should commonly use three to seven days. Evolution II should often use one to four days for global or multi-region sequences, with news throttling so the player is not buried in popups. Evolution III abnormal sequences can use one to three days between normal pulses and special scheduled delays for aftershocks, tsunami waves, ash clouds, meteor afterfalls, and moving storm corridors.

Manual Disaster Barrage can compress delays harder, but it should still schedule disasters over several days unless the chosen intensity explicitly launches a single simultaneous world shock. Even at maximum intensity, the controller should prefer one major abnormal opening pulse followed by delayed secondary waves.

Delay should be dynamic. It should react to sequence length, evolution tier, chaos tier, manual scenario intensity, whether a cluster launched it, whether a disaster is a follow-up from another family, and whether the affected area is already in recovery. It should not be a fixed value copied into every event.

## Sequence size and internal intensity

The system should calculate a sequence size, a family severity, and a news threshold independently. This prevents a global season from creating thirty popups and prevents a small sequence from feeling cosmetic.

Recommended design bands are below. Final implementation should tune through script constants.

| Context | Typical disaster pulses | Delay behavior | News behavior | Expected gameplay impact |
| --- | ---: | --- | --- | --- |
| Baseline ordinary firing | 1 to 3 | Five to ten days | Affected-country report after one to two days for each meaningful pulse | Severe state damage, local deaths, recovery decisions |
| Baseline cluster member | 1 to 2 per member | Four to eight days, then cluster schedules next member | First report per affected country, later reports throttled | Several local crises over a month |
| Evolution I | 3 to 6 | Three to seven days | First few reports, then family digests if repeated | Multi-region disruption with modest severity increase |
| Evolution II | 7 to 14 | One to four days | Only severe or player-relevant news, digest summaries | Global disaster season, chained aftermath, recovery categories matter |
| Evolution III | 3 to 10 normal pulses plus one abnormal family when eligible | One to three days plus family-specific follow-up delays | Super-event for abnormal thresholds, otherwise digest summaries | Abnormal disasters reshape regions and can damage many states |
| Disaster Barrage low | 2 to 4 | Four to seven days | Normal baseline reports | Local season for manual testing |
| Disaster Barrage medium | 5 to 8 | Two to five days | First reports plus digests | Regional stress test |
| Disaster Barrage high | 8 to 14 | One to four days | Severe only | Global or large regional stress test |
| Disaster Barrage maximum | 12 to 20 plus abnormal access | One to three days | Super-event thresholds and digest summaries | Challenge setup using the full catalogue |

The sequence size should never be the only measure of severity. A two-pulse season with a major earthquake and tsunami can be worse than a six-pulse season of storms and hail.

## Target selection principles

Every disaster family needs its own target logic. A flood, a volcanic eruption, a blizzard, and a tsunami should not use the same random-state selector. Targeting should be readable and regionally grounded, but implementation can mix exact scripted state groups with fallback terrain, climate, coastal, continent, and building checks.

The target selection layer should support four caller styles.

1. Random affected state, used by normal Event 013 firing.
2. Random affected country or region, used by cluster and Evolution I behavior.
3. Specific state or country, used by other events such as nature gods or regional divine powers.
4. World or map corridor, used by Evolution II and Evolution III global behavior.

When a family cannot find a valid target in its preferred pool, it should either select a lower-confidence fallback that still makes sense or skip the pulse cleanly. A tsunami should not strike an inland desert state because the preferred target list was empty. A sandstorm can use a wider arid or drylands fallback. A blizzard can prefer cold and mountain zones, then use high-latitude states.

Target repeats should be controlled. A recently hit state should receive lower target weight or be blocked for a temporary cooldown unless the new disaster is a chained follow-up, such as earthquake to tsunami, volcano to lahar, fire to flood, or cyclone to flood.

## Core consequence model

Each disaster pulse should apply a mix of immediate damage and aftermath. It should never be only a national spirit. The state is the center of the event.

Immediate effects should include some of these, depending on family.

- State building damage to infrastructure, factories, airbases, ports, dockyards, supply hubs, railways, forts, coastal forts, anti-air, and radar.
- Local population loss through the Deaths system.
- Temporary supply penalties.
- State modifiers for rubble, floodwater, smoke, ash, famine pressure, heat stress, cold exposure, broken bridges, blocked passes, contaminated water, refugee pressure, or evacuation strain.
- Country stability or war support damage when a capital, major population center, or high-industry region is hit.
- Temporary construction or repair burden.
- Temporary division attrition, movement, or supply penalties for units in the affected state or affected neighboring states.
- Recovery decisions and missions that can shorten the aftermath, reduce future deaths, or prevent chained disasters.

The strongest families should damage multiple neighboring states. The state at the epicenter or landfall should receive heavy damage. Adjacent or downstream states receive reduced damage, supply penalties, and aftermath. Evolution II and Evolution III should use this multi-state model frequently.

Damage should be strong enough to matter. A baseline disaster can remove or damage several buildings in a state and kill enough population to appear in the Deaths tab. A severe or abnormal disaster can cripple ports, factories, supply routes, and regional industry.

## Deaths system integration

Natural disasters must feed the shared deaths system. They should reduce real state population, not only manpower. The deaths log should identify civilian deaths, affected country, family source, and affected area where the Deaths UI supports that. This is not an Event Log entry. It belongs to the deaths system.

Population loss should be dynamic. It should scale with state population, urban density, infrastructure, available recovery response, disaster family, severity, terrain, local supply, building damage, and whether the country invests in rescue decisions before follow-up waves. A state with high population and poor infrastructure should suffer higher mortality from floods, earthquakes, heat waves, cold waves, and tsunamis. A lightly populated desert state can suffer large supply penalties from a sandstorm without massive deaths.

A disaster should also be able to create delayed deaths. Heat waves, cold waves, drought, flood disease, ash inhalation, wildfire smoke, and famine pressure can continue to kill over time unless recovery actions reduce the modifier. Delayed deaths should not fire daily world loops by default. Use targeted missions, timed modifiers, or scheduled follow-up events tied to affected states.

## Building damage and local infrastructure model

Each family should have a damage profile. The implementation should centralize profile values in script constants and reusable helper effects.

A profile should define at least:

- primary buildings damaged
- secondary buildings damaged
- maximum buildings affected by baseline severity
- maximum buildings affected by evolution severity
- population loss band
- supply penalty duration
- recovery modifier duration
- follow-up family chance
- news threshold
- AI recovery priority

The profile should treat buildings differently. An earthquake should be dangerous to infrastructure, civilian factories, military factories, forts, supply hubs, railways, and urban industry. A tsunami should hit naval bases, dockyards, coastal infrastructure, convoys in port if modeled, and population. A heat wave should harm manpower, output, stability, and supply more than it destroys buildings. A wildfire should damage infrastructure, factories, resources, and population, and can make later flood damage worse if rain follows.

## Report and news policy

The event needs reports initially. A country hit by a disaster should get a clear report one to two days after the disaster. The report should identify what happened and where. It should not list all hidden values. It should tell the player enough to understand the affected area, the disaster family, and the recovery pressure.

News should become more selective as evolutions escalate.

Baseline news policy:

- A report can appear for each meaningful disaster that hits the player's country, a major country, or a directly observed affected country.
- The report names the affected state, region, coast, river, country, or area.
- The follow-up opens or highlights the recovery decision category.

Evolution I news policy:

- The first disaster in a season receives a report.
- Later reports appear if they hit the player, a major power, a capital, a very high population state, or a severe family threshold.
- Similar repeated families can be merged into a digest report.

Evolution II news policy:

- Global disaster spam is forbidden.
- Only severe, player-relevant, capital-hit, super-event-threshold, or unusual chain reports appear.
- Other disasters appear in the disaster GUI, state modifiers, deaths log, recovery category, and optional digest summaries.

Evolution III news policy:

- Abnormal disasters get super-event treatment when they cross their trigger threshold.
- Normal smaller disasters inside the same season are mostly quiet unless they directly affect the player or create a rare chain.

The implementation should also keep event log discipline. A large season with twelve disasters is still one Event 013 firing in the Event Log.

## Recovery and aftermath loop

Affected countries receive access to a disaster response category. The category should not be a store that trades political power for cleanup. It should ask the country to commit resources and solve map problems.

The recovery loop should have three layers.

1. Emergency response, used in the first days after impact. It saves population, reduces supply collapse, opens evacuation, and prevents worst follow-ups.
2. Stabilization missions, used across the next one to four months. They require holding or repairing named railways, ports, supply hubs, depots, or affected states.
3. Reconstruction projects, used after the immediate danger. They rebuild industry, infrastructure, ports, airfields, farms, resources, and public order.

Costs should vary by family and country size. Use manpower, infantry equipment, support equipment, trucks, trains, convoys, fuel, command power, army XP, civilian factory burden, construction speed penalties, stability, war support, and local unit presence. Political power is not used as the disaster-response store; response work should spend concrete resources and resolve through decisions or missions.

Recovery should create visible differences. A country that reacts quickly should reduce deaths, shorten state modifiers, prevent famine or refugee pressure, protect factories, and avoid some follow-up disasters. A country that ignores the aftermath can face longer supply penalties, delayed deaths, migration pressure, local unrest, lower stability, and stronger future target weight.

## Reusable system requirement

Event 013 should expose a clean reusable disaster API. Other events must be able to call a specific disaster against a target without copying Event 013 code. Nature gods, African gods, occult powers, high-chaos entities, and manual scenarios can call the same family helpers with their own parameters.

The reusable system should support:

- direct family call
- random family call from a pool
- target state, target country, target region, or world target
- intensity override
- delay override
- news policy override
- caller event id and caller actor for tooltips and cleanup
- follow-up chain permission
- recovery category permission
- death logging permission
- super-event permission for abnormal families

The helpers should be idempotent where practical. They should avoid double-opening the same recovery category, double-registering the same state as active disaster aftermath, or double-logging the same state pulse.

## Interaction with related events

Event 046, Earth Earthquake, should stop owning active gameplay. Its global rupture concept belongs inside Event 013 Evolution III. The old event should be reduced to a placeholder and marked as unknown or reserved in catalog and docs. Do not reuse its old logic, because it is described as broken and outdated.

Event 099, Sandstorm, should stop owning sandstorm gameplay after Event 013 takes over the sand and dust storm family. It should become a placeholder. The Event 013 sandstorm family should be callable by other events and by the Disaster Barrage scenario.

Event 051, Heat Wave, remains a separate event. Event 013 extreme heat wave disasters can be similar, but they must not stack with the separate heat wave event. If the separate heat wave effect is active in a country or state, the Event 013 heat family should either skip that target, convert into a compounding drought or wildfire risk without adding duplicate heat modifiers, or wait until the other heat state expires.

The Sun Moves Away event can interact with cold-wave and blizzard family eligibility if implemented later, but Event 013 should not depend on it.

## Player-facing text direction

Final localisation should describe what happened, where it happened, what people can see, and what the country can do next. It should not list script effects in Event Details. It should not say that the event was reworked, that a hidden system exists, or that a report is a warning. It should avoid generic apocalypse phrasing.

Option tone can vary by context. Minor local disasters can use restrained dark irony or regional public frustration. Severe disasters should stay grounded. The option text can be practical, grim, or exhausted, but it should not cheapen mass death.

Dynamic text should include affected state or region names, affected country, disaster family, and broad aftermath class. In global evolutions, digest text should name only the most meaningful disasters and avoid long lists.

## Design acceptance summary

The reworked event is acceptable only if the implementation satisfies these points.

- One Event 013 firing creates a delayed disaster sequence.
- The sequence can be called randomly, manually, by clusters, and by other events.
- Individual disasters do not create separate Event Log entries.
- Each disaster family has unique target logic, damage logic, aftermath, recovery hooks, AI priority, and news policy.
- Baseline disasters are strong enough to damage buildings and kill population.
- Evolution I increases variety and multi-region frequency.
- Evolution II creates global disaster seasons with news throttling, recovery mechanics, chained aftermath, and larger state groups.
- Evolution III owns meteor showers, global rupture, massive eruptions, and moving storm corridors with super-event and scripted GUI support.
- Event 046 and Event 099 are converted to placeholders or reserved wrappers.
- The Disaster Barrage manual scenario uses the same sequence controller and never copies separate disaster logic.

# Event 013 Natural Disasters, Part 1, core design

## Design promise

Natural Disasters is a repeatable catastrophe system. It is not a single popup. It is a reusable Event 013 disaster engine that can be called by the random event system, a manual scenario, a cluster sequence, another event, or a special actor such as a deity, occult force, nature spirit, or hostile country mechanic.

The player should see specific disasters hitting specific places. The event should never feel like a generic disaster institution sending notices. Event 013 is the container behind the curtain. The visible experience is a damaged state, a named disaster family, a delayed country report, visible aftermath decisions, and concrete losses that enter the shared Deaths system.

One Event 013 firing can schedule several delayed disasters. It still creates one Event 013 history log row. Individual warning, impact, report, and aftermath subevents must not create separate Event 013 log rows. Evolution log rows are only for real evolution milestones, not ordinary disaster impacts.

## Fresh-system rule

This package treats Natural Disasters as a fresh design. It does not preserve old Event 013 logic. It does not reuse old Earth Earthquake logic. Deleted or outdated related event logic should stay deleted. Event 046 Earth Earthquake becomes an inactive unknown placeholder while the whole-world rupture idea moves into Event 013 Evolution III. Event 099 Sandstorm becomes a placeholder or bridge into Event 013 dust and sandstorm calls.

## Player experience loop

The loop has four visible moments.

1. The disaster sequence begins quietly through the random event, cluster, manual scenario, or external caller.
2. A warning may appear before impact, depending on family, target capacity, preparation, severity, and chaos.
3. The impact hits a named place with visible building damage, local population loss, and family-specific state disruption.
4. The affected country receives a report 1 to 2 days later and a reliable aftermath category notification that shows active disaster cards, affected states, recovery needs, cleanup state, and available response work.

The player should not need to notice a hidden flag or manually search the decision list. Serious impacts open or refresh the aftermath category and trigger a visible notification or popup path for the affected country.

## Sequence model

A disaster sequence is a short season of delayed hits. It should not fire every subevent on the same day.

| Stage | Sequence size direction | Delay direction | News direction | Report direction |
| --- | ---: | --- | --- | --- |
| Baseline | 1 to 3 local hits | 5 to 10 days between impacts | Most meaningful early disasters can use news | Every affected country receives a delayed report |
| Evolution I | 3 to 6 local or small regional hits | 4 to 8 days | News for selected meaningful disasters | Every affected country receives a delayed report |
| Evolution II | 8 to 18 world and regional hits | 2 to 5 days | Throttled to serious, strange, cascading, or global hits | Reports and recovery categories for serious hits |
| Evolution III | One or more abnormal chains plus ordinary hits | Family-specific movement or cascade timing | Super-events and rare large news only | Reports, GUI map updates, and recovery ledgers |
| Disaster Barrage scenario | Intensity sets sequence size and abnormal access | Compressed by intensity | Throttled by type and severity | Always reliable for affected countries |

These sizes are design ranges. Implementation can tune exact values in script constants, but it must preserve the feeling of a season and the rule that impacts are delayed.

## Disaster families

Event 013 must support individually triggerable disaster families.

| Family group | Families |
| --- | --- |
| Ground and mass movement | Earthquake, dry mass movement, wet mass movement, sinkhole and subsidence, whole-earth rupture |
| Water and coast | Flood, tsunami, storm surge, glacial lake outburst, coastal erosion |
| Weather and storm | Tropical cyclone, extreme wind, tornado outbreak, thunderstorm, hailstorm, blizzard, cold wave |
| Heat, drought, and dust | Drought, extreme heat wave, sandstorm and dust storm |
| Fire | Wildfire, lightning fire outbreak, urban fire after disaster |
| Volcanic | Volcanic eruption, ashfall, lahar, pyroclastic devastation, massive eruption crisis |
| Extra-terrestrial and abnormal | Meteor impact, meteor shower, skyfire hail, abnormal storm corridor |

Every family needs unique target scoring, warning odds, impact distribution, death math, building damage, state modifiers, recovery tasks, follow-up chain options, news direction, report direction, asset direction, and AI response priorities.

## Reusable caller contract

Other events must be able to call the system without copying disaster logic. The design call contract should support these inputs.

| Input | Purpose |
| --- | --- |
| Caller identity | Records whether the random system, scenario, cluster, god event, hostile actor, or scripted effect started the disaster. |
| Disaster family | A specific family, a family group, a weighted random family, or a full random pool. |
| Target mode | Chosen state, chosen country, chosen region, nearby enemy, coastal pool, volcanic pool, dense-state pool, random valid target, or caller-provided target. |
| Severity | Local, severe, regional, catastrophic, abnormal, or scenario-scaled. |
| Sequence count | Single hit, local season, regional system, global pulse, moving corridor, or scenario barrage. |
| News policy | Always, meaningful only, first time only, major only, none, or caller controlled. |
| Report policy | Affected country report, caller report, global report, silent, or delayed batch. |
| Aftermath policy | None, light cleanup, normal recovery category, full recovery category, emergency recovery category, or caller controlled. |
| Chain policy | No chain, family chain, famine chain, disease chain, refugee chain, infrastructure chain, tsunami chain, aftershock chain, or abnormal path chain. |
| Scaling multipliers | Death, building damage, supply disruption, recovery difficulty, warning success, and follow-up risk. |
| Exclusion flags | Block heat stacking, block global one-offs, block repeated huge disasters, block invalid target categories, and block same-day repeat impacts. |

The system should expose safe default behavior. A caller that only provides a family and target should still get warnings, impact, report, aftermath, cleanup, death logging, building damage, news throttling, and event-log containment.

## Targeting principles

Targeting must feel physical and strategic. It should not pick every state with equal chance.

Target scoring should consider:

- population density and state population
- coastal exposure, river exposure, and lake exposure
- mountain, hill, desert, jungle, forest, plains, urban, and island geography
- ports, dockyards, railways, supply hubs, airfields, forts, infrastructure, factories, and resources
- war state, front pressure, occupation, resistance, and supply disruption
- existing devastation, unresolved aftermath, previous disaster memory, and current recovery capacity
- family-specific eligibility such as volcano regions, coast states, dry regions, hot regions, cold regions, storm paths, and meteor spread

Invalid targets should be skipped cleanly. If a family cannot find a valid target, the caller can either retry another family or record a harmless skipped subimpact inside the same sequence without producing a player-facing fake disaster.

## Significant death design

Disaster deaths must matter. Baseline events should not kill decorative numbers. Population loss should feed the shared Deaths system through visible death records, and the loss should remove real state population.

The death model should combine:

- base family lethality
- severity band
- state population and density
- infrastructure and supply quality
- building damage level
- war state and occupation strain
- stability and recovery capacity
- warning success or warning failure
- preparation decisions completed before impact
- unresolved aftermath and chained famine or disease
- family-specific hazards, such as collapse, drowning, heat exposure, ash inhalation, cold exposure, debris flow, fire spread, and meteor blast

The design expectation is that ordinary baseline disasters can kill thousands to tens of thousands in suitable states. Severe regional disasters can kill hundreds of thousands across dense or vulnerable regions. Evolution III abnormal disasters can create multi-million death spikes when the family fits and the player fails to prepare or recover.

## Building damage design

The event must damage buildings enough to change play. Damage should target what the disaster family plausibly breaks.

| Family | Primary building targets | Secondary targets |
| --- | --- | --- |
| Earthquake | infrastructure, civilian factories, military factories, railways, supply hubs | forts, airfields, dockyards, ports |
| Flood | infrastructure, railways, supply hubs, civilian factories | dockyards, ports, resources, airfields |
| Cyclone and wind | ports, dockyards, airfields, infrastructure | factories, anti-air, radar |
| Wildfire | infrastructure, resources, civilian factories | railways, airfields, supply hubs |
| Blizzard and cold | infrastructure, railways, supply hubs | airfields, factories through frozen logistics |
| Heat and drought | infrastructure, resources, civilian production via disruption | supply hubs and rail through overheat strain |
| Volcanic | infrastructure, factories, resources, airfields | ports, railways, supply hubs, agriculture logic through aftermath |
| Meteor | all buildings in impact state, with blast falloff nearby | railways, ports, airfields, supply hubs |

Damage should use repair time, temporary state modifiers, and recovery tasks rather than only instant building removal. A disaster can leave damaged buildings, blocked transport, refugee pressure, famine risk, disease risk, or lingering local modifiers.

## Text direction

The specification gives writing direction only. It does not provide pasteable event titles, options, news copy, report copy, super-event titles, quotes, button text, slogans, or lyric fragments.

Player-facing text should name the disaster and place clearly. It should use physical details and local fear rather than an official category frame. It should avoid generic lines where only the state name changes. News and reports should have family-specific remark direction, such as cracked rail embankments for earthquakes, waterline marks for floods, ash on airfields for volcanoes, red night skies for wildfire, dust-darkened convoys for sandstorms, and silent harbors after tsunami withdrawal.

## Event-log and event-detail direction

The Event Details entry should explain the premise and player-facing situation without listing mechanical effects. It can say that disasters now arrive as delayed local and regional sequences, affected countries receive reports and recovery categories, and later stages bring larger, chained, and abnormal events. It should not display death percentages, building formulas, or hidden weights.

The History row should show Event 013 once per sequence. If the visible actor is meaningful, use the affected country or the sequence anchor country. If a global abnormal chain has no fair single actor, use the default Event 013 actor display or a neutral global context.

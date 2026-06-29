
# Event 013 recovery decisions, missions, scripted GUI, and animation plan

This file expands the player-facing disaster recovery layer. All labels are working labels and are not final localisation.

## Recovery loop

A disaster sequence should give the player a clear disaster record and a set of current actions. The recovery category and optional scripted GUI should make the state of the disaster readable without forcing the player to open several raw tooltips.

The loop should be this.

1. A warning or impact creates an active disaster ledger for the affected country and state.
2. The ledger chooses a small set of relevant decisions and missions.
3. The player spends physical resources, time, local capacity, or foreign access to reduce the dynamic loss rate before it is multiplied by state population.
4. Success clears aftermaths, lowers percentage-based deaths, and prevents chain events.
5. Failure leaves state modifiers, population pressure, supply penalties, or regional consequences.

## Ledger values

These values should be visible through scripted localisation or a scripted GUI. Exact variable names belong to implementation.

| Value | Meaning | Typical sources | Typical sinks |
| --- | --- | --- | --- |
| Transport damage | Roads, railways, bridges, ports, and supply hubs are blocked or damaged. | Flood, quake, storm, blizzard, mass movement, volcano, meteor. | Rescue engineers, rail missions, port reopening. |
| Population pressure | Casualties, displaced people, exposed settlements, and rescue overload. | High-population impacts, tsunamis, cyclones, heat, cold, meteor. | Evacuation, shelters, foreign relief, field hospitals. |
| Water and food stress | Drought, flood contamination, crop failure, and shortage pressure. | Drought, flood, heat wave, ashfall. | Rationing, relief corridors, water purification. |
| Coastal danger | Ports, dockyards, ships, and coastal districts remain exposed. | Tsunami, cyclone, storm surge, coastal quake. | Coastal evacuation, port closure, barrier work. |
| Ash and air disruption | Ash, smoke, dust, or meteor debris disrupts airbases and transport. | Volcano, wildfire, sandstorm, meteor. | Airfield dispersal, ash cleanup, dust clearance. |
| Fire spread | A fire front can move into nearby states. | Wildfire, heat, drought, meteor. | Firebreaks, fuel logistics, supplied divisions. |
| Aftershock risk | Damaged structures can collapse again. | Earthquake, massive quake-wave, volcanic tremor. | Inspection missions and bridge reinforcement. |
| Refugee pressure | Displaced people strain neighboring states or countries. | Any severe disaster with poor recovery. | Shelter missions, foreign relief, refugee intake decisions. |
| Recovery progress | Overall cleanup and stabilization progress. | Successful decisions and missions. | Used to clear state modifiers and close category. |

## Decision category display

The decision category should not be a store. It should display a compact summary and then relevant actions.

### Header direction

The header should include these elements.

- Active disaster count.
- Worst unresolved family.
- Worst active state or named region.
- Current recovery status.
- Next follow-up risk if visible.
- Foreign relief state if available.

If no disaster is active, the category should hide or show only a compact preparedness office if that office has already been unlocked.

### Action filtering

Only show decisions connected to active ledgers.

- Flood actions show pumps, rail clearing, water purification, and shelter tasks.
- Earthquake actions show inspections, rescue engineers, and bridge work.
- Cyclone and tsunami actions show coastal evacuation, port closure, and relief corridors.
- Drought actions show rationing, food support, and refugee prevention.
- Wildfire actions show firebreaks and smoke management.
- Volcano and sandstorm actions show ash or dust clearance and airfield actions.
- Meteor actions show shelters, crater cleanup, and firebreaks.

## Decision family map

| Family | Availability | Costs | Result | Failure or tradeoff |
| --- | --- | --- | --- | --- |
| Evacuate exposed districts | Warning or immediate aftermath in populated state. | Trains, trucks, fuel, manpower, possible stability. | Reduces the dynamic death-rate multiplier and refugee pressure before state population is multiplied. | Production disruption and possible stability loss. |
| Send rescue engineers | Transport or building damage active. | Support equipment, army XP, command power, manpower. | Repairs infrastructure and reduces transport damage. | Consumes scarce support equipment during war. |
| Open foreign relief corridor | Severe aftermath and valid neighbor, faction, coast, or port route. | Convoys, trains, relations, stability burden. | Adds relief progress and reduces refugee pressure. | Can add foreign dependency or expose intelligence in future systems. |
| Build flood barriers | Flood or storm surge warning. | Support equipment, fuel, civilian factory burden. | Reduces flood damage and wet movement chain chance. | Late use has weaker effect. |
| Start firebreak line | Fire spread active or fire weather warning. | Fuel, infantry equipment, support equipment, supplied units. | Stops spread or protects one neighboring state. | Failure can spread the fire to the state the player tried to protect. |
| Ground and disperse aircraft | Airbase, ash, hail, wind, dust, or cyclone warning. | Air mission disruption, fuel, command attention. | Reduces airbase and plane-equipment damage. | Temporary local air weakness. |
| Close exposed port | Coastal warning or cyclone. | Convoys, dockyard downtime, trade disruption. | Reduces port and dockyard damage. | Temporary supply and trade penalty. |
| Water rationing | Drought, heat, or flood-water aftermath. | Stability, trucks, trains, local supply. | Slows famine and water stress. | Repeated use increases unrest risk. |
| Clear ash and dust | Ash, dust, smoke, or meteor debris. | Trucks, fuel, support equipment, air XP if airbases are affected. | Reduces air and supply penalties. | High cost if multiple states are affected. |
| Inspect aftershocks | Earthquake or quake-wave aftermath. | Support equipment, army XP, engineers, time. | Lowers aftershock chance. | If delayed, aftershock risk remains high. |
| Shelter displaced people | Refugee pressure active. | Manpower, trains, trucks, support equipment, stability. | Reduces refugee pressure and ongoing percentage-based deaths. | Failure can push pressure to neighbors. |
| Survey abnormal corridor | Moving storm, meteor cluster, or tsunami basin warning. | Command power, fuel, air XP or naval XP depending on family. | Improves forecast and can shift one target to lower severity. | Forecast can still be wrong at high chaos. |

## Mission map

| Mission | Family | Player objective | Duration | Success result | Failure result |
| --- | --- | --- | --- | --- | --- |
| Rail recovery mission | Flood, quake, mass movement, blizzard, volcano. | Hold and repair named rail or supply states, with supplied divisions or repair progress. | Medium. | Clears transport damage and improves supply. | Adds longer supply penalty and possible refugee pressure. |
| Coastal reopening mission | Cyclone, tsunami, storm surge, volcano. | Hold and repair port state, spend convoys or dockyard burden. | Medium. | Reopens coastal relief and trade. | Port remains damaged and local supply worsens. |
| Drought belt support mission | Drought, heat, ash crop stress. | Keep supply route open and spend trucks or trains over time. | Long. | Prevents famine follow-up. | Famine and refugee pressure begin. |
| Fire line containment mission | Wildfire, meteor fire, heat. | Keep target states supplied and pay fuel or equipment. | Short to medium. | Stops fire spread. | Fire spreads to a valid neighbor. |
| Shelter surge mission | Any severe population impact. | Spend manpower, support equipment, and transport capacity. | Medium. | Lowers ongoing loss-rate ticks. | Displaced pressure spreads. |
| Ash cleanup mission | Volcano, wildfire smoke, sandstorm, meteor dust. | Clear airbase and rail penalties with trucks and support equipment. | Medium. | Removes ash or dust state modifier. | Air and transport disruption persists. |
| Aftershock watch mission | Earthquake, quake-wave, volcanic tremor. | Inspect structures and bridges before deadline. | Medium. | Reduces follow-up chance. | Aftershock follow-up can fire. |
| Corridor tracking mission | Evolution III moving storm or meteor path. | Maintain observation and update path warnings. | Short. | Lets the country protect one forecast state. | Impact severity rises in an unprotected state. |

Missions must have meaningful success and failure effects. They should not all be passive timers.

Mortality display rule: the GUI should show pressure levels, trend arrows, and broad risk labels rather than exact death formulas. Tooltips may explain that loss is population-scaled and that high-population states can suffer larger absolute losses, but they should not expose raw hidden percentages unless the implementation deliberately adds a debug-only view.

## Scripted GUI concept

Working GUI label, not final localisation: `Disaster Operations Map`.

The scripted GUI is recommended from Evolution II onward and required for Evolution III moving disaster paths. The baseline can use the decision category without the full map if implementation needs staged delivery.

### Entry point

- A decision category button opens the map.
- The map should also open from certain warning popups when the player is affected.
- AI should not rely on the GUI. AI uses decisions and helper effects.

### Tabs or modes

| Mode | Purpose |
| --- | --- |
| Warning map | Shows states or regions with active warnings, forecast confidence, and available preparation. |
| Impact ledger | Shows recently hit states, disaster family, severity band, and active penalties. |
| Recovery board | Shows ledgers by country or state, progress, missions, and remaining chain risk. |
| Regional chain | Evolution II and III, shows cross-border refugee, tsunami, ash, fire, or drought chains. |
| Abnormal tracker | Evolution III, shows moving storm corridors, meteor clusters, volcanic ash plume, and tsunami basin path. |

### Map cards

Each active state or region should have a card with these fields.

- Disaster family icon.
- State or named region.
- Warning state, impact state, or recovery state.
- Worst ledger value.
- Active mission if any.
- Next known follow-up if public.
- Buttons for family-appropriate actions.

### Button rules

Every clickable GUI button that changes gameplay must follow the same cost, requirement, tooltip, AI equivalent, and cleanup rules as a normal decision.

- Use scripted triggers for availability.
- Use scripted effects for outcomes.
- Use dynamic scripted localisation for costs and missing requirements.
- Use static fallback sprites when animation is disabled or not produced.
- Use no hidden free resources.

## Animation plan

Animated assets should clarify changing disaster state. They should not be decorative noise.

| Animated asset | Surface | State logic | Target direction | Static fallback |
| --- | --- | --- | --- | --- |
| Warning pulse overlay | GUI map and category header. | Active warning exists and impact is pending. | Subtle pulsing frame around state card or map marker. | Static warning marker. |
| Impact flash marker | GUI map. | New impact occurred during last update. | Short non-looping flash or severe marker. | Static impact marker. |
| Recovery progress shimmer | Recovery board. | Mission is active and progress changed. | Subtle progress frame animation. | Static progress bar. |
| Flood waterline | Flood and tsunami region card. | Flood or coastal danger active. | Slow moving waterline frame sheet. | Static blue hazard mark. |
| Fire front | Wildfire and meteor fire card. | Fire spread risk active. | Small flame or smoke frame sheet. | Static fire marker. |
| Ash plume | Volcano, wildfire smoke, sandstorm, meteor dust. | Ash or dust active and spreading. | Drifting plume frame sheet. | Static ash marker. |
| Storm corridor | Evolution III moving storm map. | Forecast path, current state, next state. | State-driven path markers with moving storm icon. | Static corridor arrow and current state marker. |
| Meteor shower track | Evolution III skyfall map. | Meteor cluster scheduled or falling. | Falling streak markers over selected state cards. | Static crater or skyfall marker. |
| Tsunami wave band | Tsunami warning map. | Basin wave is scheduled and moving toward coast. | Wave band frame sheet, short loop. | Static wave warning marker. |
| Volcanic eruption spot | Evolution III volcano map. | Active eruption and ashfall. | Plume and glow frame sheet. | Static volcano marker. |

All final animation assets must follow the frame-animation workflow. They need source frames, processed frames, a horizontal frame-sheet PNG, a sheet DDS, a static fallback DDS, a GIF preview for review only, a manifest entry, and a gfx handoff. A transform-only pulse from one image is not acceptable as final art.

## GUI cleanup

The GUI and category must close or hide when a country no longer has an active disaster ledger, when the country is annexed, when the player tag changes, when the sequence ends, or when the world enters a terminal scenario through another event. Global event targets and selected-state variables must be cleared.

## Exploit controls

- Recovery decisions should not be repeatable reward farms.
- Building repair should not give more buildings than were lost.
- Foreign relief should not duplicate equipment or convoys.
- Refugee acceptance should not become free manpower unless a specific later system is designed for it.
- Disaster damage should not repeatedly hit the same state without respecting cooldowns or aftermath logic.
- Preparedness should reduce loss, not create invulnerable states.
- AI should not spend rare resources on low-value recovery when a capital, port, supply hub, or dense state is also damaged.

## Big disaster category correction

The generic Natural Disaster Recovery category is not the full recovery system. It is the overview. Each big disaster family has its own decision category when a country is directly hit. Follow `013_natural_disasters_big_disaster_decision_categories.md` for the category registry, values, decisions, missions, cleanup, AI behaviour, and active category cap.

The Disaster Operations Map should show the active family category for the selected state or country. A flood state should route the player to Flood Relief Authority. A seismic state should route to Seismic Emergency Authority or Great Rupture Command. A meteor impact state should route to Skyfall Emergency Bureau or Meteor Storm Command. A moving corridor state should route to Storm Corridor Command.

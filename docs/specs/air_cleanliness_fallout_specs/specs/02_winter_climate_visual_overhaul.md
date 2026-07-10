
# Winter Climate Visual Overhaul

Working labels in this file are not final localisation.

## Required result

Air Winter phases must visibly make the world colder.

The dedicated winter mapmode remains required, but it is not sufficient. A player who stays in the ordinary political, terrain, supply, air, or strategic view should still see that the climate has changed.

The visual presentation must correspond to actual state winter phase, regional climate identity, global soot forcing, and recovery direction.

## Four visual channels

The implementation should combine four channels after local engine proof.

### Normal-map atmospheric grade

A non-interactive atmospheric layer changes the overall light and color of the normal map.

It should communicate:

- reduced sunlight
- colder color temperature
- lower contrast during heavy soot
- darker noon light at severe phases
- gradual brightening during recovery
- a separate ultraviolet-bright state after soot clears where the accepted climate model calls for it

Candidate implementations include a verified map shader, post-processing state, or non-blocking full-screen GUI tint. The local vanilla and official documentation must prove the selected route.

The atmospheric layer must not block clicks, hide text, make borders unreadable, or tint the normal user interface so strongly that buttons become unclear.

### Regional weather and ground state

Where the engine supports dynamic weather forcing, winter phase should influence:

- temperature
- snow likelihood
- blizzard likelihood
- cold rain
- fog and low cloud
- sea and lake ice presentation
- daylight and visibility
- air-operation weather

The local implementation must verify the exact strategic-region or state-level weather control. No unsupported effect may be assumed.

### State and province visual markers

A normal-map state or province presentation layer should show local severity through verified particles, ambient entities, map icons, or other supported effects.

Possible visual families:

- falling snow
- ash-snow mixture
- ground frost
- frozen industrial vapor
- black snow near direct-strike zones
- cold rain in warm climates
- dead vegetation
- dry frost haze
- ice around ports and rivers
- heavy soot cloud over severe urban states
- thaw mud and flood during recovery

This layer must scale with zoom and avoid hundreds of expensive animated elements.

### Dedicated winter mapmode

The winter mapmode remains the precise diagnostic view.

It shows:

- state phase
- direction of travel
- exposure
- forecast
- active visual state
- climate adaptation
- food and shelter pressure
- category damage
- current response

The mapmode should use high-contrast state fill and tooltips. The ordinary map uses atmosphere and physical cues.

## Hard proof gate

Before implementation chooses a visual route, the local pass must prove:

1. how dynamic weather can be changed
2. whether snow cover can expand outside its normal climate
3. whether a normal-map tint or shader can be triggered and removed
4. whether state or province particles can be added dynamically
5. how the presentation behaves at different zoom levels
6. how it behaves with other mapmodes and open windows
7. how multiplayer clients receive the visual state
8. how save-load restores the active state
9. how recovery removes or changes visual effects
10. what performance cost appears when many states are affected

If the engine cannot support a required channel, the implementation report must identify the blocker. It must not quietly reduce visible climate change to the dedicated mapmode.

## Climate severity values

Global values:

- atmospheric soot forcing
- sunlight reduction
- global cold anomaly
- precipitation disruption
- recovery trend
- ultraviolet risk after soot thinning

State values:

- current winter phase
- effective cold severity
- soot and ash severity
- precipitation form
- snow or frost presentation class
- local visibility
- recovery direction
- recent phase-change visual cooldown

The visual layer reads these values. It does not calculate gameplay effects separately.

## Regional presentation classes

### Boreal and continental

Visible cues:

- expanding snow cover
- frozen rivers and lakes where supported
- darker conifer and soil palette
- rail and road frost
- chimney smoke hanging low
- severe whiteout at high phases

Gameplay emphasis:

- rail failure
- heating fuel
- engine start problems
- frozen ports and lake routes
- roof and line damage from snow

### Temperate maritime

Visible cues:

- cold rain and sleet before heavy snow
- grey sea and low cloud
- wet snow around cities
- ice on ports during severe phases
- mud and flood during thaw

Gameplay emphasis:

- port reliability
- damp shelter disease
- convoy delay
- flood and bridge damage after thaw

### Mediterranean

Visible cues:

- pale winter light
- frost in agricultural valleys
- snow at elevations
- cold rain and damaged orchards
- darkened sea and empty coastal fields

Gameplay emphasis:

- orchard and vineyard loss
- heating shortage in unprepared cities
- mountain pass closure
- port and refugee pressure

### Desert and arid plateau

Visible cues:

- cold dust haze
- frost around wells and pipelines
- rare but striking snow in severe phases
- cracked water systems
- dim sun and long cold shadows

Gameplay emphasis:

- water-convoy failure
- frozen pipes at night
- livestock loss
- fuel used for heating and pumping
- exposed refugee mortality

Snow must not cover every desert state at low or middle phases.

### Tropical coast and monsoon

Visible cues:

- cold rain
- persistent low cloud
- weakened canopy color
- highland frost
- rougher grey seas
- reduced sunlight and delayed monsoon

Gameplay emphasis:

- crop timing failure
- rot and mold in shelters
- fishery movement
- river and port disease
- landslides during disrupted rain

The world should look colder without turning every tropical coast white.

### Equatorial rainforest

Visible cues:

- chilled mist
- canopy dieback
- dark rivers
- reduced flowering and fruit
- frost only at elevation or under extreme forcing
- ash trapped in wet vegetation

Gameplay emphasis:

- altered food gathering
- river transport
- fungal disease
- isolated settlements
- fictional altered ecology under high-chaos gates

### Mountain and highland

Visible cues:

- deep snow
- avalanche scars
- blocked passes
- frost line descending
- bright snow under dark sky
- exposed rock and ice during recovery

Gameplay emphasis:

- tunnel shelters
- pass control
- hydro power
- avalanche damage
- mountain refugee routes

### Island and oceanic

Visible cues:

- darker sea
- cold storms
- rough surf
- frost on high islands
- ash rain
- sea ice only where latitude and severity support it

Gameplay emphasis:

- fisheries
- port survival
- refugee fleets
- convoy loss
- isolation
- cyclone and cold-storm overlap

### Polar and subpolar

Visible cues:

- severe whiteout
- sea-ice expansion
- long dark atmospheric grade
- buried stations
- blue-black cold at high phase
- aurora and radio effects only where justified

Gameplay emphasis:

- station isolation
- fuel
- radio
- ice route
- scientific data
- protocol breakdown

## Phase visual states

### Phase 0

Normal regional climate presentation.

Residual soot or fallout may still appear through separate hazard visuals.

### Phase 1, atmospheric dimming

Normal map:

- subtle desaturation
- colder sunlight
- thin haze
- first regional frost cues

Mapmode:

- pale grey-blue fill

Events:

- first persistent haze
- aviation reports
- heating demand
- unusual dawn or noon light

### Phase 2, failed season

Normal map:

- clear colder grade
- regional snow, frost, or cold rain
- weakened vegetation
- darker agricultural states

Mapmode:

- stronger blue-grey

Events:

- crop failure
- seed and livestock decisions
- rural migration
- fishery shift

### Phase 3, infrastructure winter

Normal map:

- persistent snow or regional cold equivalent
- visible frozen transport cues
- ash accumulation in damaged states
- stronger cloud and visibility loss

Mapmode:

- dark cold blue

Events:

- rail ice
- transformer failure
- port closure
- hospital heating
- roof collapse

### Phase 4, black winter

Normal map:

- deep snow or severe regional cold state
- darkened daylight
- strong ash-snow separation
- abandoned urban lighting
- frozen water cues where supported

Mapmode:

- near-black blue-grey with high-contrast borders

Events:

- black harvest
- city-system failure
- mass evacuation
- food seizure
- shelter conflict

### Phase 5, terminal climate

Normal map:

- persistent severe ground state
- thick ash or snow
- localized black sky around heavy soot and blast zones
- dead vegetation
- damaged ports and rivers

Mapmode:

- bruised violet, cold white, and dark grey warning treatment

Events:

- state abandonment
- sealed districts
- government evacuation
- armed corridors
- underground authority

### Phase 6, Fallout night

Normal map:

- strongest soot grade
- visually distinct blast and fallout zones
- severe cold state by region
- no requirement that every state has identical snow
- persistent dead-city and wasteland cues

Mapmode:

- terminal fill with strong border and hazard overlay

Events:

- terminal population loss
- state-class conversion
- survivor enclaves
- direct Fallout request pressure

## Cold, ash, and radiation must remain distinct

Players need to recognize three different hazards.

| Hazard | Main palette and cue | Gameplay meaning |
| --- | --- | --- |
| Cold | pale blue, white frost, snow, cold rain, ice | climate pressure, food loss, heating, supply |
| Ash and soot | grey, charcoal, dark sky, dirty snow, reduced light | atmospheric forcing, crop failure, visibility |
| Radiation and toxic contamination | cyan, sickly amber, marked zones, local particles | local exposure, deaths, quarantine, mutation-fiction gates |

Mixed states combine cues but preserve one dominant signal.

## Global versus local visibility

Global atmospheric forcing should alter the whole map.

Local phase and exposure should alter particular states or strategic regions.

This prevents two errors:

- a severe global winter that looks normal outside the mapmode
- a light global event that covers every state with identical snow

## Visual transitions

Visual states use hysteresis and transition time.

Required behavior:

- phase escalation triggers a gradual visual change
- recovery requires stable improvement before the visual state recedes
- a one-month fluctuation does not flash the map between states
- direct thermonuclear or terminal events may force an immediate severe visual jump
- normal recovery produces patchy thaw, mud, flood, roof failures, and exposed debris
- final warming does not remove radiation, ruins, dead-city, or wasteland visuals

## Climate recovery presentation

Recovery should be visible and mechanically complicated.

### Soot thinning

- brighter daylight
- reduced ash fall
- improved air visibility
- higher ultraviolet risk may appear later
- old snow remains in severe regions

### First thaw

- patchy snow
- flooded roads
- broken pipes
- corpse and waste exposure
- disease risk
- bridge and rail damage

### Unstable seasons

- false spring
- late frost
- seed loss
- short growing windows
- sudden storms

### New climate normal

- some states recover ordinary seasonal visuals
- high-latitude and badly damaged states remain colder longer
- altered ecology and wasteland cues persist
- successful adaptation creates greenhouse, reclaimed field, or repaired-grid visuals

## Gameplay synchronization

A visible phase must match gameplay.

Examples:

- a frozen port visual means port throughput or convoy penalties are active
- deep snow means supply and movement pressure is active
- a dark agricultural state means food pressure is active
- thaw mud means repair and disease risk is active
- a recovered greenhouse refuge should visibly differ from an untreated severe state

Do not show dramatic climate art that has no gameplay consequence.

## Accessibility and controls

Provide settings where practical:

- reduced atmospheric tint intensity
- reduced particle density
- static climate markers instead of animation
- colorblind-friendly winter mapmode palette
- tooltip-first mode
- hide decorative climate effects while retaining gameplay cues

The default presentation should remain strong.

## Asset families

Required visual asset families:

- global cold-grade overlays
- soot-grade overlays
- ultraviolet recovery grade
- snow and frost particles
- ash and dirty-snow particles
- cold rain and mist
- frozen-port and river cues
- dead vegetation and crop-failure cues
- thaw mud and flood cues
- phase-change border or state markers
- mapmode button frame and tooltip icons
- static fallbacks for animated elements

All assets use dedicated Air Cleanliness or Fallout-owned paths. No zombie asset path is acceptable.

## Acceptance standard

The climate presentation passes only when:

- the ordinary map visibly changes as global forcing rises
- affected states show regional cold cues in normal views
- tropical and desert states use suitable cold cues instead of automatic snow
- the winter mapmode precisely reports phase and forecast
- cold, ash, and radiation remain distinguishable
- phase changes and recovery alter visuals without flicker
- normal-map visuals match active gameplay effects
- save-load restores the correct presentation
- multiplayer clients see the same global phase
- performance remains acceptable at world scale
- no unsupported visual route was silently substituted

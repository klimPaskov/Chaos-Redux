# Event 033 Acid Rain, Part 6, scripted GUI and presentation

## Interface goal

The Acid Rain interface gives one readable global map and one national preparedness summary. It does not replace the strategic map or ask the player to manage hundreds of state buttons.

Use a dedicated scripted GUI opened from the Acid Rain decision category and from the Event 33 Event Details page. The category itself uses a full background and a compact inlay summary so the player can see critical information without opening the larger window.

## Layout target

Inspect the repository's current decision and popup anchors before final dimensions are locked. At 1920 by 1080, target a content area near 900 by 600 pixels with these regions:

- top header, event phase and close control
- left and center, world map near 560 by 300 pixels
- right, up to three front cards or one global-layer card
- below map, coverage bar and region rows
- lower national strip, Preparedness, current warning, exposed-state count, casualties, and contamination
- bottom controls, category return, Event Details, and optional map animation toggle

The window must remain usable at the repository's supported lower resolutions. Text cannot overlap at 100 percent and 125 percent interface scale.

## Compact decision-category inlay

The category inlay shows:

- current event phase
- world coverage percent
- national Preparedness
- national warning or exposure status
- button to open the world map

It uses plain values and one status line. It does not repeat the full front list or casualty ledger.

## World map

### Base layer

Create a neutral dark world map that matches the Chaos Redux interface. Borders should remain readable behind weather overlays. The map is a presentation abstraction and does not need exact province geometry.

### Region overlays

Provide one mask or overlay for each stable region:

- Europe
- Middle East
- Asia
- Africa
- Australia and Pacific
- North America
- South America

Overlay states:

- inactive
- current ordinary front region
- future warning region
- visited but currently inactive
- global-layer active

Coverage color cannot be the same as current danger color.

### Front markers

Each ordinary front receives:

- stable front number
- animated swirl marker
- current region
- qualitative intensity
- movement window
- destination once warning is revealed
- severe-cell alert if active

Marker location can use a reviewed region anchor or one of several anchor points per region. It should not imply exact state-level placement when the map cannot render state geometry.

### State footprint summary

Hovering a current region shows:

- active states in this front
- unique states touched during current visit
- untouched states remaining in the region
- region total eligible states
- current visit quota
- severe-cell state count

The GUI reads stored counters. It does not scan states on hover.

## Coverage display

The coverage bar uses exact touched and eligible counts. Display:

- percent
- touched count
- eligible count
- completion status

Below the bar, seven compact rows show each region's touched and total counts. A completed region receives a clear icon, but completion does not imply the front cannot revisit it.

## National strip

The selected player country sees:

- Preparedness from 0 to 100
- four component tier pips
- exposed state count
- severe-warning state count
- unresolved aftermath state count
- Event 33 national deaths
- estimated deaths prevented

Only Preparedness is an active national value. The other entries are status or history.

## Global counters

Show these read-only values:

- Event 33 global deaths
- Event 33 lifetime Air Contamination added
- remaining Event 33 lifetime Air allowance
- current global Air Contamination

The lifetime addition line is the authoritative answer to how much contamination Event 33 contributed. Current event source pressure can remain in the Air Cleanliness source details instead of crowding this window.

## Front cards

### Ordinary front card

- front ID
- current region
- intensity band
- active-state count
- movement-window countdown
- next region when revealed
- severe-cell status

### Multiple-front phase

Show two cards by default. If the third front exists, reduce card height without hiding any timer. Cards remain ordered by stable front ID.

### Global-layer card

Replace ordinary cards with:

- global layer active status
- days since global transition
- minimum duration remaining
- next dissipation check window when eligible
- active superstorm count
- strongest superstorm band

Superstorms use a small bounded list below the global card.

## Severe-cell presentation

A severe cell must be visually distinct from ordinary rain:

- pulsing alert icon on parent front card
- highlighted affected region
- forecast countdown
- state count and broad area name when available
- stronger sound cue for the player's country if it contains a forecast state

Do not use flashing faster than a comfortable warning cadence. Provide an animation toggle or static fallback for users who disable animated interface elements.

## Frame animation

Use real source frames and the repository frame-animation pipeline.

| Element | Frames | Direction |
| --- | --- | --- |
| Ordinary front swirl | 8 to 12 | Slow rotating cloud and rain texture |
| Warning pulse | 6 to 8 | Expanding ring or hatched light pulse |
| Severe-cell pulse | 8 | Denser cloud core with corrosive rain streaks |
| Global-layer movement | 8 to 12 | Slow atmospheric veil with regional variation |

Do not fake animation by repeatedly transforming one static frame. Frame extraction, naming, DDS conversion, sprite registration, frame count, loop mode, and animation rate must follow the frame-animation skill.

## GUI read model

Create one explicit refresh effect that projects stored gameplay state into GUI variables. It can run when:

- the window opens
- the Acid Rain category becomes selected
- a front moves
- a warning is created or cleared
- an exposure pulse changes displayed counters
- an evolution transition completes
- dissipation begins

Opening or refreshing the GUI never mutates gameplay, advances timers, selects targets, or repairs missing runtime state.

## Tooltip requirements

Every important value answers three questions:

1. What is the current value or status?
2. What changes it?
3. What can the player do about it?

Examples:

- Coverage tooltip explains first-touch tracking and the dissipation gate.
- Preparedness tooltip shows four component contributions.
- Contamination tooltip explains the 1500 bp lifetime cap and 5000 bp event ceiling.
- Front timer tooltip distinguishes estimated movement window from fixed warning destination.
- Severe-cell tooltip explains forecast, active duration, and local evacuation.

## Color and icon rules

- ordinary active rain uses a muted yellow-green or gray-green, not neon
- warning uses amber hatching
- severe cell uses rust red and dense gray
- visited coverage uses desaturated blue-gray
- global layer uses a muted acidic veil
- completed coverage uses a neutral check, not a victory-green wash

Icons must remain readable in grayscale and at the 32 by 32 decision scale.

## Presentation sequence at formation

1. Event runtime and first footprint are committed.
2. Super-event opens for all players through the standard framework.
3. The Acid Rain category becomes visible.
4. The first affected countries receive arrival reports on the next safe report day.
5. The GUI opens automatically only for the player whose selected country has an active or warned state, unless the global settings request major-event windows for all players.

## Multiplayer behavior

- one host-authoritative weather runtime
- each player sees the same front data and coverage
- national strip reads the viewing player's country
- no player click advances the global scheduler
- super-event follows the repository multiplayer presentation rule
- simultaneous category opening by several players has no gameplay side effect

## Resolution and fallback checks

Required test resolutions:

- 1920 by 1080
- 1600 by 900
- 1366 by 768

At each resolution verify:

- all front cards fit
- no tooltip runs outside screen bounds
- region rows remain clickable or readable
- national values do not overlap
- the close control remains available
- static severe and global states remain understandable with animation disabled

## Debug presentation

A debug-only overlay can show:

- stable front IDs
- exact region IDs
- active-state counts
- visit quotas
- untouched counts
- next pulse dates
- schema version

It is hidden from normal players and reads existing state only.

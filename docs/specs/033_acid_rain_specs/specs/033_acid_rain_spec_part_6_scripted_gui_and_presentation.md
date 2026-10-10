# Event 033 Acid Rain, Part 6, scripted GUI and presentation

Status: `implemented` in source as `acid_rain_world_window` and `acid_rain_category_inlay` (`interface/033_acid_rain.gui`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, `common/scripted_localisation/033_acid_rain_scripted_localisation.txt`).
The D37 regional state strips are `accepted and queued`.
The player-facing value budget below is a 2026-10-10 audit proposal made under the user's brief to remove values that do not drive a decision; it needs parent acceptance before the implemented surfaces it trims change.
Layout, hover and animation playback are user live checks.

## Interface goal

The Acid Rain interface gives one readable global map and one national preparedness summary. It does not replace the strategic map or ask the player to manage hundreds of state buttons.

Use a dedicated scripted GUI opened from the Acid Rain decision category and from the Event 33 Event Details page. The category itself uses a full background and a compact inlay summary so the player can see critical information without opening the larger window.

## Player-facing value budget

Disposition: `unresolved` proposal (README open question 3).

Every value on the map, inlay or tooltips must answer one of three player questions: is the rain coming for me and when, what should I buy or repair now, and what has it cost.
Values that only describe the weather engine stay internal and appear in the debug overlay.

| Surface | Keeps | Removes from player view |
| --- | --- | --- |
| Category inlay | Phase, World Coverage, Preparedness, one status line naming exposure, a storm forecast or a warning with the country's state counts | Nothing |
| National strip | Preparedness with four component pips; exposed, warned and forecast state counts; aftermath state count; national deaths; estimated deaths prevented | The national Air Contamination line, which repeats a world value the country cannot change |
| World ledger | Worldwide deaths and the Air Contamination the rain has added | Current global Air Contamination, which belongs to the Air Cleanliness interface, and the rain's remaining Air allowance, which is an internal cap |
| Front card | Front number, region, intensity band, days until it moves, destination once announced, severe-cell alert | The front's active-state count |
| Global card | One line saying when the layer can begin to break up, then "may break up at any time"; the superstorm list with region and days to impact or active | Days since the transition and the separate minimum-period and next-check clocks |
| Region tooltip | States reached out of the states in the rain's path there; the weather over the region (front, intensity, severe cell) or approaching it with days until arrival; the global layer | The visit quota, the states first reached on this visit and the states under rain now |

The removed facts stay in stored state and in the debug overlay, so balance and acceptance checks keep their evidence.

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

### Region summary

Hovering a region shows the facts the value budget keeps for the region tooltip.
The GUI reads stored counters and does not scan states on hover.

## Coverage display

The coverage bar uses exact touched and eligible counts. Display:

- percent
- touched count
- eligible count
- completion status

Below the bar, seven compact rows show each region's touched and total counts. A completed region receives a clear icon, but completion does not imply the front cannot revisit it.

## National strip and world ledger

The selected player country sees the national strip and world ledger values listed in the value budget.
Only Preparedness is a managed national value; the counts are status and the deaths are history.
The estimated deaths prevented stays because it is the feedback that shows whether Preparedness is worth its cost; it is always labelled as an estimate.
The Air Contamination the rain has added is the answer to how much contamination Event 33 contributed.

## Front cards

### Ordinary front card

The card shows the front-card values in the value budget.

### Multiple-front phase

Show two cards by default. If the third front exists, reduce card height without hiding any timer. Cards remain ordered by stable front ID.

### Global-layer card

Replace ordinary cards with one global card that shows the global-card values in the value budget.
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
- Contamination tooltip says in words that the rain adds at most 15 points of Air Contamination and never pushes the world above 50 percent.
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
5. The GUI opens automatically once per generation for each player whose country has an exposed or warned state (D28); the mod has no setting that opens major-event windows for every player.

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
- visit quotas and visit progress
- untouched counts
- next pulse dates
- global minimum-period and next-check clocks
- remaining Air allowance
- generation ID

It is hidden from normal players and reads existing state only.

## Accepted implementation decisions, 2026-10-04

Acceptance basis: agent decisions recorded in `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md`, taken on 2026-10-04 under the full design authority the user granted for Event 033; each item is implemented in source and its live-game confirmation is a separate gate.

- Superstorm markers (D16): the world map shows one severe-storm marker for each of the three listed superstorms at the alpha-weighted centre of its seed region's overlay, from forecast until retirement while the global layer lasts (D22), with a still partner for reduced motion; a marker whose region already holds an earlier listed marker moves 48 pixels right. Front markers and superstorm markers never share the map because fronts are projected only up to the global warning.
- Front markers (D24): each ordinary front's markers sit at the same region anchors, on the region the front covers or is about to reach, and move with the front.
- Global layer and veil (D17): the global layer is an eight-frame sheet of three separated cloud banks that leaves the map readable; the warning veil uses defringed art at the original mean opacity of about 46.
- Footer navigation (D18): HOI4 script cannot open the decisions panel, so category return is a Back button that closes the map and reveals the view that opened it, the decision category or Event Details, with a tooltip naming that view. Details closes the map and opens the Event 33 page in Event Details through the shared Event Log entry points, and is hidden when the map was opened from Event Details.
- Render route history: on 2026-10-04 `hoi4.gui_render` refused 1920x1080 for this window under its aggregate pixel budget, so the D16 to D18 renders used 1366x768; later reviews retain 1920x1080 renders (for example `validation/gui_current_2026_10_07/regional_one_1920_v3/` in the plans folder), so that limit is not a current route claim.
- Region tooltips and status line (D33) and Event Details status (D34) are implemented; the value budget above proposes trimming parts of D33.
- Severe forecast cue (D29): each forecast over a player's territory plays one thunder cue at the super-event audio volume setting.
- Regional state strips (D37, `accepted and queued`): the seven region overlays become four-frame static strips (inactive, visited, approaching, active) at the same sprite names, replacing the broad ordinary, warning and visited veils.

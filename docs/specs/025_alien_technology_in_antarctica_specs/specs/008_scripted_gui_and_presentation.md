# Scripted GUI and presentation

## Why the event needs a dedicated GUI

The Expedition Board is justified because the player must manage:

- three interacting visible values
- a multi-phase race
- selected rivals
- changing search sectors
- outpost and route state
- active missions
- evolution-specific hazards
- hidden and public information

A normal decision category would require too many rows and too much repeated text. The board should remain compact and action-oriented.

The board belongs only to Event 025. It must not modify shared log, details, settings, meter, or super-event framework layouts.

## Entry point

A participant opens the Expedition Board through:

- a button in the Event 025 decision category
- an optional alert while an urgent expedition mission is active
- a link from the participant's Event Details state when the shared framework supports it cleanly

Observers do not receive the board button.

## Window structure

The accepted layout uses five regions.

### Header

Shows:

- event identity
- current phase
- broad race state
- days until the next expedition pulse or current mission deadline
- close button

The header should not contain a paragraph.

### Left status column

Shows the player's three visible values:

1. Expedition Progress
2. Logistics Readiness
3. Exposure Risk

After Evolution V, a technology holder sees Alien Dependence in the third slot.

Each value needs:

- icon
- meter or segmented bar
- current stage label
- next meaningful threshold marker
- concise tooltip explaining cause, consequence, and response

The column also shows compact route and outpost status through icons and short labels. Route burden and outpost integrity remain supporting states, not a fourth and fifth main meter.

### Center Antarctic operations panel

Shows a stylized Antarctic sector map.

The map is an event presentation surface, not a new HOI4 strategic map.

It should show:

- broad search sectors
- known and suspected sectors
- the player's outpost
- confirmed fragment sites
- current final recovery sector when known
- evolution overlays such as signal activity, survivor trace, militarised zone, or fragment field

The sectors must not expose exact hidden rival coordinates.

Sector states:

- unknown
- surveyed
- probable
- confirmed
- blocked by weather
- contested
- recovered
- lost or buried

Every state needs a non-colour cue such as border, hatch, icon, or label.

### Right rival column

Shows a bounded list of active rivals.

Each rival card contains:

- flag and country name
- broad expedition phase
- confidence band for estimated progress
- public stance
- known outpost or route state
- incident marker when relations are tense
- selection control

The exact numeric progress of a rival is hidden unless the player has sufficient intelligence.

The list needs scrolling only when the bounded roster exceeds the visible card count.

### Bottom action tray

Shows the three to five primary actions relevant to the current phase.

Each action has:

- unique icon
- concise label
- current cost string with matching texticons
- enabled, disabled, selected, active, cooldown, and warning states
- short tooltip
- clear confirmation for hostile, irreversible, or expensive actions

The tray must not display obsolete actions from previous phases.

## Suggested reference canvas

The UI worker should begin from a reference canvas around `1024x640` and validate against the supported in-game resolutions.

The exact final size depends on current Chaos Redux window conventions and the installed GUI framework. The implementation must use `hoi4.gui_inspect`, `hoi4.gui_render`, and `hoi4.gui_rewrite` before accepting coordinates.

Required review resolutions should include at least:

- `1920x1080`
- `2560x1440`
- one lower supported resolution used by the project

The board must not cover essential top-bar controls or extend beyond the safe screen area.

## Visual hierarchy

The player should understand these facts within a few seconds:

- current phase
- whether progress is competitive
- whether supplies are healthy
- whether risk is becoming dangerous
- which mission or action matters next

The center panel should attract first attention, followed by the three values and the action tray. Rival data remains secondary.

## Background art

The board uses one full background that covers the entire window.

The background may include:

- dark steel or painted expedition framing
- paper map and instrument surfaces
- frost around the border
- radio and navigation motifs
- period expedition materials

Text must not sit over detailed illustrations, bright glare, map labels, or high-contrast decorations.

Fake controls painted into the background are forbidden.

## Main visible values

### Expedition Progress

Range is displayed as stages or a normalized meter.

Suggested stages:

- Organizing
- Southbound
- Established
- Searching
- Final Approach
- Recovery Ready
- Resolved

Tooltip summarizes the main current contributors and the next phase requirement.

### Logistics Readiness

Represents supply, route capacity, camp stocks, transport condition, and personnel readiness.

Suggested bands:

- Critical
- Strained
- Stable
- Prepared
- Overprovisioned

The tooltip should state the immediate consequence of crossing the next lower threshold.

### Exposure Risk

Represents danger from weather, signal effects, survivor contact, wreck instability, hostile action, and unsafe research.

Suggested bands:

- Controlled
- Elevated
- Dangerous
- Severe
- Critical

The value should rise through observed actions and incidents. It should not feel like random punishment.

### Alien Dependence

Evolution V changes the third value only for technology holders.

Suggested bands:

- Experimental
- Embedded
- Reliant
- Entrenched
- Controlling

The tooltip explains which institutions and actions are increasing or reducing dependence.

## Supporting status icons

Supporting states use icons, not extra meters.

Required statuses:

- route burden
- route open or interrupted
- outpost integrity
- survey confidence
- crew condition
- selected rival
- fragment inventory
- final recovery readiness

Each icon should have a concise tooltip. Avoid a row of unexplained numbers.

## Sector map behavior

The map uses six broad sectors arranged around Antarctica.

The exact visual geography must be based on a verified projection and should read clearly at the board's size. The sectors are gameplay abstractions and do not need to match political state boundaries.

Click behavior:

- clicking a visible sector selects it for survey or recovery actions
- unavailable sectors show the blocked reason
- unknown sectors do not reveal hidden weights
- a confirmed final sector receives a strong but readable state
- decorative overlays must be `alwaystransparent` or equivalent so they do not block sector clicks

The implementation must keep click regions aligned with the visible sector shapes.

## Rival selection

Clicking a rival card changes the selected target.

The action tray then displays relevant cooperative, intelligence, defensive, or hostile actions.

The selected card needs a clear frame and name confirmation near the action tray. A hostile confirmation window repeats the target, costs, public risk, and likely consequence.

The selected target clears when it becomes invalid.

## Phase states

### Entry window

The board is not yet open. The entry event shows participation terms.

### Mobilization

Center panel emphasizes gateway and route planning.

Main actions concern commitment, route, personnel, and weather preparation.

### Crossing and outpost

Center panel shows route status and outpost placement.

Main actions concern resupply, alternate landing, camp construction, and route defense.

### Survey

Center panel becomes the primary search surface.

Main actions concern sector survey, signal study, data theft, false information, and fragment analysis.

### Final recovery

Center panel highlights the confirmed sector and final mission.

Main actions concern recovery commitment, stabilization, escort, emergency resupply, and withdrawal.

### Resolved

The race actions disappear.

The board becomes a compact aftermath panel showing winner status, fragments, technology field, and any active Evolution V policy.

## Evolution visual states

### Active Signal

- animated or staged signal arcs over relevant sectors
- interference indicators around communications
- static fallback showing active signal sectors

### Something Survived

- moving trace, opened compartment marker, or repeated track indicator
- no explicit survivor portrait before confirmation
- static fallback showing last known trace

### Militarised Antarctica

- blockade, patrol, and fortified outpost markers
- clear distinction between defensive escort and active exclusion zone

### Wreck Breaking Apart

- several fragment-site markers
- wreck-integrity indicator as a supporting icon
- sector states for buried, contaminated, recovered, or unstable pieces

### Technology Changes Its Users

- restrained visual corruption or system-integration overlay on the aftermath panel
- Dependence meter replaces Exposure Risk
- no horror distortion that makes values unreadable

## Animation plan

Animation is used only where motion communicates changing state.

Candidate loops:

- radio signal pulse
- sector interference sweep
- survivor trace movement
- fragment instability flicker
- Dependence circuit activity

Each final animation requires real per-frame source art, a horizontal frame sheet, DDS output, a static fallback, and a verified `frameAnimatedSpriteType` consumer.

Transform-only glow, scale, blur, or position animation is not accepted as final art.

## Window states

The UI package must document and render:

- normal
- hover
- selected
- active mission
- disabled
- insufficient cost
- cooldown
- warning
- confirmed sector
- contested sector
- resolved winner
- resolved loser
- observer unavailable
- evolution-specific overlays

## Confirmation windows

Use confirmation for:

- entering the race
- withdrawing
- launching final recovery
- hostile sabotage
- outpost seizure
- transferring alien custody
- destroying or sealing the wreck
- aggressive Evolution V integration

The confirmation repeats no more than the information needed to make the decision.

## Tooltips

Value and action tooltips should usually fit in two to four short lines.

A tooltip can be longer when it shows a dynamic cost breakdown, selected target, or several public consequences. Large lore paragraphs belong in reports, not action tooltips.

Non-obvious blocked states need a direct reason.

## Accessibility

The board cannot depend on colour alone.

Required cues:

- meter labels
- icons
- border patterns
- sector hatching
- selected frames
- warning symbols
- textual stage names

Text contrast must remain readable over the full background.

Click targets need enough area for reliable selection at the lowest supported resolution.

## Multiplayer privacy

The board reads private country data only for the current player.

Rival cards show public or intelligence-derived bands. They must not read hidden exact progress from another human participant without an exposure route.

A human player's private sabotage authorship remains hidden until evidence changes.

## AI equivalence

The GUI contains no human-only gameplay result.

Every button calls a shared action helper that AI can invoke through scheduled logic. The GUI is a presentation and input layer over the same country-scoped expedition state.

## GUI file ownership

Expected event-owned surfaces:

- `interface/025_alien_technology_in_antarctica.gui`
- `interface/025_alien_technology_in_antarctica.gfx`
- `common/scripted_guis/025_alien_technology_in_antarctica_scripted_guis.txt`
- event-owned GUI localisation

The exact filenames should follow live repository conventions discovered before implementation.

## Mandatory MCP evidence

Before implementation:

- inspect relevant Chaos Redux independent windows
- inspect current decision-window entry patterns
- render the accepted board skeleton
- inspect hierarchy and click regions

After implementation:

- render every important state at every supported resolution
- compare pre-change and post-change layouts
- verify sector and action click regions
- verify scrolling and clipping
- verify decorative overlays do not intercept input

A source-only review does not satisfy the GUI acceptance gate.

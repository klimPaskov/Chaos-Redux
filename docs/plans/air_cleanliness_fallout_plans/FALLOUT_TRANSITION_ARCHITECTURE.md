# Fallout Transition Architecture

## Purpose

Create one reusable aftermath framework that can be called by gradual Air collapse, Final Silence, a concentrated nuclear exchange, chemical or biological terminal events, and the manual Fallout scenario. Every caller supplies cause and intensity. Every caller enters the same validated blackout, state grading, world rewrite, player handoff, and post-Fallout campaign state.

## Namespace and ownership

All Fallout events are defined in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

Use `chaosx.fallout.*` only for Fallout events. Use `fallout_world_end_*` for Fallout-owned reusable helpers. Event suffixes are allocated inside the dedicated namespace and have no relationship to the manual scenario registry id.

Remove the old Fallout event block from every non-Fallout event file. Migrate each caller directly to `fallout_request_aftermath` or a dedicated `chaosx.fallout.*` entry event. Do not keep a compatibility shim in another namespace.

All blackout GUI, transition GFX, report images, portraits, icons, flags, and audio follow `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Caller contract

Every caller must provide:

- request source enum
- request intensity
- initiating country when one exists
- initiating state when one exists
- manual-scenario flag when applicable
- whether the request bypasses normal risk
- any cause-specific state memory already applied

Caller examples:

### Gradual Air collapse

- source: gradual Air collapse
- intensity: derived from contamination, severe phase share, and wasteland count
- bypass: no
- behavior: request coordinator validates and may start from monthly pressure

### Final Silence

- source: scripted terminal strike
- intensity: maximum or event-defined
- bypass: yes
- behavior: the event applies its direct strike or silence consequences, then requests Fallout

### Manual scenario

- source: manual Fallout scenario
- intensity: selected scenario intensity plus fixed total-strike floor
- bypass: yes after seven days
- behavior: synthetic strike batch runs first, then countdown, then request

### Other terminal scenarios

- source: chemical, biological, mixed, or unknown
- intensity: event-defined
- bypass: yes when the event explicitly requests the aftermath
- behavior: cause memory changes state grading and successor weighting

## Core helpers

### `fallout_request_aftermath`

Scope: country or host-owned country scope

Inputs:

- source enum
- intensity
- optional actor and state targets
- bypass flag

Behavior:

1. Reject if Fallout is already active.
2. Reject duplicate request if one is already pending.
3. Store source, intensity, date, actor memory, and state memory.
4. Set `fallout_requested`.
5. Schedule the validation event or call the validator from the host.

### `fallout_validate_request`

Checks:

- no completed Fallout state
- no incompatible active world rewrite
- caller conditions still valid
- at least one valid state and one valid country context exist
- player scope can be captured
- no active scenario lock forbids transition

On success:

- capture snapshot
- enter transition lock

On failure:

- clear request state
- record a development error counter
- never leave the screen black

### `fallout_capture_pre_transition_snapshot`

Capture before changing the world:

- player country and original tag
- player capital and controlled state list
- country ownership and controller memory needed for survival scoring
- current wars, factions, subjects, guarantees, access, and exile state
- global Air state and winter phase counts
- state population, category, buildings, supply, resources, and contamination memory
- current active terminal cause
- feature-managed countries that require special cleanup
- global systems that must stop during the rewrite

Use arrays only where scope persistence and size are proven safe. Use state and country variables for durable per-scope memory.

### `fallout_begin_blackout`

Behavior:

1. Set `fallout_transition_active`.
2. Set `world_end` and `world_end_fallout` at the transition lock point.
3. Stop ordinary random-event firing and incompatible crisis systems.
4. Close or hide conflicting Chaos Redux windows where possible.
5. Set transition phase to the first blackout beat.
6. Increment the GUI dirty variable.
7. Schedule the next beat.

No normal super-event flag or audio id is set.

### `fallout_advance_blackout_beat`

A hidden host event advances the transition phase. The GUI does not advance itself.

Each beat:

- checks that transition state is valid
- sets the next phase
- increments the dirty variable
- performs the bounded processing action assigned to that beat
- schedules the next beat or waits for a processing cursor

### `fallout_process_state_grades`

Calculates grade and survival value for every valid state. The state pass can be divided into deterministic batches if a single pass causes a visible freeze.

### `fallout_apply_state_rewrite`

Applies one-time population, building, category, resource, supply, and province memory effects from the stored grade.

### `fallout_reset_old_world_diplomacy`

Ends or remaps incompatible relationships only after snapshot capture and before successor diplomacy begins.

### `fallout_select_successors`

Builds candidate pools from state clusters, old governments, tag availability, matrix rules, and player reservation.

### `fallout_apply_country_packages`

Applies country identity, politics, ideas, units, focus tree, AI, and starting mechanic values.

### `fallout_select_player_continuation`

Keeps the player in a valid surviving government when possible. Otherwise opens a controlled successor selection surface.

### `fallout_finish_transition`

Validates:

- every non-wasteland state has a valid owner and controller
- every active country has a capital or accepted no-capital rule
- the player controls a valid country
- no old-world war or subject reference points to an invalid actor
- transition cursors are finished
- no rewrite error counter is nonzero

Then:

- set `fallout_active`
- clear transition-only flags, arrays, targets, and cursors
- reveal the post-Fallout map
- start delayed regional aftermath content
- keep `world_end` and `world_end_fallout`

### `fallout_abort_transition_cleanup`

Allowed only before destructive state ownership changes begin.

It must:

- clear blackout visibility
- clear transition and request flags
- restore ordinary window access
- release event-system locks that were set during validation
- record a clear development error marker

After destructive rewrite begins, the system must finish or enter a dedicated recovery routine. It cannot restore a partially rewritten world from incomplete memory.

## Blackout GUI

## Window structure

Create one independent full-screen `containerWindowType`.

Required elements:

- opaque black background covering the active screen area
- centered primary text box
- optional secondary processing text box
- subtle static or animated texture only when it improves the presentation
- hidden progress or safety indicator in debug mode
- successor-selection panel that remains hidden until needed

The blackout has no ordinary close button.

A post-processing continue action may appear only after the rewrite is valid and the player has a valid country.

## Drawing order and input

The local vanilla GUI inspection must prove:

- the parent or independent window appears above ordinary map and interface windows
- the blackout covers popups that could expose the changing world
- clicks do not reach the map or underlying controls
- focus, politics, decisions, diplomacy, production, and mapmode windows cannot remain interactive under it
- multiplayer clients see the same transition phase while the host owns effects

Do not anchor to `top_bar` only because it covers the screen. The offline reference notes that top-bar children can draw below popups. Use the verified higher-level pattern.

## GUI update model

Use `dirty = global.fallout_transition_dirty` or a verified equivalent so text and properties update only when the phase changes.

The GUI reads:

- transition phase
- player-choice-required flag
- player candidate array
- selected successor index
- processing status
- final readiness flag

AI has no GUI actions. AI equivalents are direct scripted effects.

## Cinematic beat structure

Exact final wording is researched and written during implementation. The spec defines meaning and pacing only.

Recommended sequence:

1. total blackout and silence interval
2. first statement confirming catastrophic world destruction
3. mass death and infrastructure collapse
4. failure of old governments and communication
5. survival beneath shelters, remote regions, ships, mines, mountains, and hardened sites
6. fragmentation into local authorities, warlords, communes, military districts, enclaves, and fictional mutant regimes
7. a processing hold while the map rewrite completes
8. player continuation or first post-Fallout orientation

Each sentence or beat appears alone. The sequence must not use a normal super-event quote or reaction button.

Pacing constants should allow:

- fade-in delay
- display duration
- fade-out delay
- minimum processing hold
- player-choice timeout where needed

## Sound direction

Fallout does not use the super-event audio system.

A separate transition sound package may use:

- initial abrupt silence or cut
- low environmental sound during blackout
- sparse mechanical or radio failure texture
- restrained post-rewrite ambience

Any final music or sound must follow repository licensing and documentation rules. Do not manufacture placeholder oscillator audio.

## State grading

## Inputs

State grade should be deterministic for the same campaign state and request source.

Damage inputs:

- direct thermonuclear strike count
- ordinary nuclear strike count
- nuclear fallout intensity
- chemical contamination
- winter phase and exposure
- recent strategic bombing and building damage where tracked
- urban density and state category
- factory and infrastructure concentration
- population density
- supply isolation
- active combat
- terminal source intensity

Survival inputs:

- shelter capacity
- adaptation
- food reserve
- remote terrain
- island or maritime access
- underground, mountain, mining, polar, or rural characteristics where supported
- functioning port, rail, and supply access
- old government preparation
- treaty relief and cleanup
- route-specific protected facilities

## Grade calculation order

1. Set base damage from request intensity.
2. Add direct strike and local contamination damage.
3. Add winter and infrastructure collapse damage.
4. Subtract shelter, adaptation, food, and remoteness survival factors.
5. Apply cause-specific floors and caps.
6. Clamp grade from 0 to 6.
7. Calculate a separate survival value from 0 to 100.
8. Set state class and candidate flags.

Do not derive successor viability from grade alone. A badly damaged remote state can still support a small survivor package, while a dense destroyed city can have high symbolic value but low survival value.

## One-time state rewrite

For each grade, define one-time consequences.

### Grades 0 and 1

- moderate population loss
- repairable building damage
- preserved state category or one conditional step
- strong old-government survival chance
- high successor viability

### Grades 2 and 3

- major population loss
- broad infrastructure and industrial damage
- category loss based on sustained damage
- likely fragmentation or local successor
- contested resource and supply systems

### Grade 4

- extreme population and building loss
- sparse state administration
- limited viable capitals
- special survivor or abandonment package

### Grades 5 and 6

- wasteland or terminal exclusion status
- very low ordinary population
- no normal industrial recovery
- salvage, expedition, and sealed-zone content
- special fictional packages only under explicit gates

All state population loss goes through the shared Deaths system with an aggregate transition reason and state-level records.

## Old-world diplomacy reset

The rewrite must explicitly handle:

- wars
- civil wars
- factions
- guarantees
- military access
- docking rights
- non-aggression pacts
- subjects and overlords
- collaboration governments
- governments in exile
- volunteers and expeditionary forces
- lend lease
- intelligence relationships
- trade and embargo state
- peace conference state if a transition can begin during one

Preferred policy:

- freeze new diplomatic actions at transition start
- capture relationships needed for memory content
- end or clear incompatible relationships in a deterministic order
- build post-Fallout diplomacy only after every successor exists

The exact effect order must follow official local documentation and vanilla precedents.

## Country survival and fragmentation

Country survival score inputs:

- share of core population surviving
- surviving capital or fallback capital
- surviving connected territory
- command cohesion
- government preparation
- shelter and food network
- surviving armed forces
- surviving ports or remote territory
- legitimacy and ideology stability
- request cause
- whether the country is player-controlled

Outcomes:

- old government survives with a Fallout identity
- old government survives in a reduced refuge state
- country fragments into several successors
- country disappears and its territory becomes local successors or wasteland
- fictional high-chaos transformation

The player is never silently assigned to a dead or invalid tag.

## Player continuation

Priority order:

1. Continue as the old government when it has a valid surviving package.
2. Continue as the strongest direct successor holding the old capital or largest protected population.
3. Offer a small list of valid successor candidates tied to the former player territory.
4. Use a deterministic fallback only if the player does not choose within the configured time.

Candidate rows should show direction only until final localisation exists:

- identity and region
- government archetype
- capital or main state
- starting survival strengths
- main crisis

The choice must not reveal hidden focus routes or secret mutant outcomes.

## Multiplayer

Host owns all effects and arrays.

Clients receive:

- global transition phase
- black-screen visibility
- relevant player candidate list
- final tag switch result

The plan must test:

- several human countries surviving
- one human country disappearing
- two humans claiming overlapping successors
- a human disconnect during blackout
- save-load with multiple humans during countdown and processing

Player reservations are resolved before general successor assignment.

## Post-transition handoff

The transition ends with a short stabilization period:

- ordinary random events remain stopped
- Fallout survival decisions become visible
- each country receives its opening orientation event or mechanic panel
- mapmodes refresh
- severe state modifiers and wasteland rules remain active
- delayed regional wars and diplomacy begin after a grace period

Do not start every war, focus event, and flavour incident on the reveal day.

## Acceptance checks

- no normal super-event appears
- no super-event audio id is set
- blackout cannot be closed during processing
- text beats advance through scripted events
- save-load resumes the correct beat
- state grading is deterministic
- every state is processed once
- every active country has a valid package
- player continuation is valid
- old wars and subjects do not survive accidentally
- post-Fallout systems start only after validation
- every direct caller reaches the same transition framework

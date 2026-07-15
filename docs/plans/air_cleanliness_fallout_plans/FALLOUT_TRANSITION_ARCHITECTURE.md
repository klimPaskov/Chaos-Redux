# Fallout Transition Architecture

## Purpose

Create one reusable aftermath framework that can be called by gradual Air collapse, Final Silence, a concentrated nuclear exchange, chemical or biological terminal events, and the manual Fallout scenario. Every caller supplies cause and intensity. Every caller enters the same validated blackout, state grading, world rewrite, player handoff, and post-Fallout campaign state.

## Live implementation boundary

This document records both the required architecture and the current implementation boundary. The source specifications under `docs/specs/air_cleanliness_fallout_specs/` remain design authority.

The live foundation includes the request envelope, once-per-date project coordinator, schema-7 migration gate, blackout phase events, row-proven snapshot, grading, population-loss, and physical-collapse barriers, partial old-world diplomacy cleanup, deterministic provisional government classification, player-first source and state reservation, a generation-bound pre-allocation conflict inventory, a separate post-allocation proof contract, two-pass player commit preflight, ready-target commit, exact-signature retry recovery, and persisted commit reconstruction.

The transition is not complete. General successor allocation, country-package producers, focus-package producers, player-successor materialization, and candidate-choice UI are not implemented. A player can be committed only to an already existing target with current-transition packages and an exact valid reservation. Immediate `is_ai` observation after `change_tag_from` remains statically unresolved. The old-world diplomacy proof gate is also unresolved. Map return therefore remains intentionally fail closed.

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

The helper headings below describe the required end-state contracts. They are not a claim that every named helper is present. Live phase work is currently split across `fallout_apply_transition_phase_*` effects. In particular, no active `fallout_select_successors`, `fallout_apply_country_packages`, package-generation producer, or player materialization effect exists.

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

No normal super-event flag or shared global audio id is set. Dedicated Fallout dramatic audio still plays through Fallout-owned wrappers that honor the super-event audio mode and volume settings.

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

### `fallout_classify_country_government`

Classifier schema 2 assigns one deterministic provisional origin archetype before ownership changes. State signals come from the Fallout snapshot and the completed state rewrite, and aggregate into the frozen original owner rather than the mutable live owner. The result is stored separately from the final applied archetype package. The fixed specificity order resolves eleven live archetypes. Machine Protocol stays future-only until its machine-survival inputs have real producers. A partial machine claim or any unmatched surviving country raises error 16 and keeps the blackout active.

This step does not change politics or activate successor content. A future allocator must still choose and apply the final archetype package, regional layer, country-memory layer, focus content, leaders, units, decisions, diplomacy, and AI.

### `fallout_reset_old_world_diplomacy`

Ends or remaps incompatible relationships only after snapshot capture and before successor diplomacy begins.

### `fallout_select_successors`

Builds candidate pools from state clusters, old governments, tag availability, matrix rules, and player reservation.

Live boundary: `fallout_build_successor_conflict_ledger` implements the generation-bound inventory that must precede this helper. It records every live country, every possible country scope, every state, player reservations, known event-package ownership, and exact safe-candidate membership. A separate schema-2 output contract consumes that frozen inventory. Every non-retired source and committed output must link to each other and match result, generation, and cleanup owner. Continued, converted, released, dynamically created, retired, protected-package, and player-reserved outcomes each have a distinct provenance contract. Releasing a possible-country scope requires a current release receipt. Membership in `game:all_possible_countries` is not availability proof. Retired sources must be landless and must not name an output. The contract also validates unique assigned countries, unique capitals, exact live-landholder coverage, current package layers, and origin states. The guarded finalizer is the only setter for `fallout_successor_allocation_complete`.

No allocator calls the transaction initializer or finalizer. No assignment or package producer exists. The transition therefore remains in survivor allocation.

The accepted ordering requires a committed nine-resource survival ledger after final allocation. The live survivor-allocation phase does not yet enforce it. The future proof must cover Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition for every assigned successor and included state. No row contract, numeric initialization, aggregation producer, or transition barrier exists.

### `fallout_apply_country_packages`

Applies country identity, politics, ideas, units, focus tree, AI, and starting mechanic values.

### `fallout_initialize_survival_ledger`

This required future producer runs after successor allocation and package assignment but before player continuation. It stores immutable initial values, raw numerators and denominators, and separate mutable values for all nine resources. The global commit must match the current transition generation and exact finalized successor count. No starting formula or value is approved, so no implementation may write the ready flag yet.

### `fallout_select_player_continuation`

Keeps the player in a valid surviving government when possible. Otherwise opens a controlled successor selection surface.

The live pre-allocation barrier separates reservation from destination materialization. It reserves every snapshot-origin player state before the general inventory, preserves landless human sources, and records one explicit materialization branch when no in-place target is ready. The future allocator must supply the missing target, capital, packages, and reciprocal assignment row, rebuild the player planning ledger, then finalize general allocation. Once allocation initialization consumes the reservation ledger, those inputs become immutable. Any later reservation drift records `player_reservation_changed_after_allocation` and remains fail closed. This removes the earlier circular dependency without pretending the missing allocator exists.

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

## Live save migration boundary

The current schema is version 7 and migration is deliberately fail closed.

- A completed old Fallout save is promoted non-destructively to the completed schema-7 state.
- Only the exact schema-3 map-return-error signature is recovered. It must already be in the map-return phase with map return blocked, transition error set, error code `map_postcondition_failed`, and error count one.
- Every other incomplete schema 1 through 3 state remains under blackout with schema migration blocked.
- An incomplete terminal save with no schema also remains under blackout with schema migration blocked.
- Migration does not treat a missing `fallout_transition_destructive_started` flag as proof that a legacy state is safe to restart.
- No generic pre-destructive restart and no legacy altered-grade replay are active behavior.

Schema 7 makes snapshot and destructive-phase completion proof results. Player and world rows are captured and retried as one epoch. Exact live owner and controller equality is required only while capture is being accepted. Durable grading and rewrite receipts retain the frozen owner and controller scopes after valid allocation changes ownership. Grading cannot begin unless both snapshot ledgers pass their current-row proofs. Grading failures rebuild safe derived rows. Population and building failures reconcile existing destructive receipts without applying loss again. Their phase-local checks require the engine's current population and damaged-building observations to match the new result before the phase advances. Map return uses the generation-bound durable transaction receipts, so later normal demographic change or building repair does not invalidate completed destruction. Category recovery repairs flags only when the live category already matches the required result. Modifier recovery removes and rebuilds Fallout-owned modifiers. Each phase can re-enter only with its matching one-error signature.

This narrow recovery rule prevents the current transition from mixing its snapshot and phase ledgers with an ambiguous legacy rewrite.

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

Fallout does not enter the ordinary super-event queue or claim its shared audio id. Fallout-owned audio wrappers still play the dedicated dramatic sound while honoring the super-event audio preference and volume controls.

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
6. Clamp the monotonic physical-damage grade from 0 to 5.
7. Record altered biosphere as a separate fictional high-Chaos subtype so it cannot reduce or reorder physical severity.
8. Calculate a separate survival value from 0 to 100.
9. Set state class and candidate flags.

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

### Grade 5 and the altered biosphere subtype

- wasteland or terminal exclusion status
- very low ordinary population
- no normal industrial recovery
- salvage, expedition, and sealed-zone content
- special fictional packages only under explicit gates

All state population loss goes through the shared Deaths system with reason `chaos_meter_deaths_reason.fallout_aftermath`, numeric reason `19`, and state-level records.

The three destructive rewrite phases use separate proof ledgers. Grading proves the deterministic score band, grade, subtype, survival range, and generation for every state. Population loss stores the grade-derived percentage, requested Deaths amount, applied Deaths amount, exclusive applied-or-zero result, and generation. Physical collapse proves the building receipt, exact grade modifier, altered-biosphere modifier when applicable, state-category result, supply-collapse flag, and rewrite generation. A stale completion flag is cleared when its ledger is no longer current. Missing idempotent rows can re-enter only through the exact error signature owned by their current phase.

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

Live status: `fallout_reset_old_world_diplomacy` handles a subset of the required relationships, but the full reset postcondition remains unproven. The transition must not advance through government sorting or reveal the map until every required diplomacy surface has a supported reset and validation pair.

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

### Live commit path and blockers

The snapshot records each human country, original identity, optional source anchor, former capital, and owned-state origin memory. Every origin state is reserved before the generation-bound conflict inventory is built. A landless human is retained as an emergency-materialization source rather than rejected. Reserved player states are excluded before any successor allocation is permitted. The inventory also excludes every state with human ownership or control and every state whose owner or controller has known live event-package ownership.

`fallout_player_primary_target_is_commit_ready` allows only an existing same-country or AI target with country and focus packages from the current transition generation. The target must own survivable territory. Its actual capital must be the exact state reserved for that player, remain owned and controlled by the target, remain able to host a government, and retain the matching reservation origin and generation.

`fallout_preflight_player_commit_targets` performs a global two-pass preflight over existing commits and proposed targets before any switch occurs. It proves that every snapshotted player has one ready and unique target. The source's `player_reserved` conflict output must equal that same primary target. `fallout_commit_current_player_primary_target` then writes the final target, commit generation, durable assignment origin, and durable assignment generation before an optional `change_tag_from`. Retry logic permits re-entry only for an exact single recoverable error signature, clears only those errors, and revalidates every commit and cross-player assignment before map return. A cleared reservation may be rebuilt from a durable assignment only before allocation initialization. Consumed reservations are never rebuilt.

This is a real commit path for already materialized, current-generation targets. It is not a materialization or package-production path. No active effect creates a missing player successor, applies the required country and focus packages with their transition generations, fills a candidate list, presents a candidate-choice UI, or completes general successor allocation. The source-reservation ledger can safely reach the allocator when a destination is missing. `fallout_player_materialization_required` remains set until that allocator supplies and proves the destination.

Static inspection cannot prove that `change_tag_from` makes the destination observe `is_ai = no` immediately in the same effect chain. The commit effect checks that condition immediately after the switch and fails closed if it is not yet visible. No Hearts of Iron IV run was authorized, so this timing remains unresolved.

### Required continuation priority

Priority order:

1. Continue as the old government when it has a valid surviving package.
2. Continue as the strongest direct successor holding the old capital or largest protected population.
3. Offer a small list of valid successor candidates tied to the former player territory.
4. Materialize an emergency council from the nearest survivable state or largest refugee cluster when the source spec's no-obvious-successor case applies.

Candidate rows should show direction only until final localisation exists:

- identity and region
- government archetype
- capital or main state
- starting survival strengths
- main crisis

The choice must not reveal hidden focus routes or secret mutant outcomes.

## Multiplayer

The project coordinator owns all effects and arrays. The existing daily host flag is deduplicated, transfer to another human occurs only when the flagged country is AI, and the Fallout reconciler records the current global date before gameplay work. Additional calls on that date cannot repeat manual, migration, phase-scheduling, or request transactions. They may only repair the persistent coordinator target after a valid host-flag transfer.

The documented script surface does not identify the literal multiplayer lobby host. `is_global_host` remains a project simulation coordinator on synchronized state. Literal network-host authority is an open engine blocker.

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

The ordering exists in the live phase skeleton. General successor assignment, package production, player materialization, and candidate-choice UI do not.

## Post-transition handoff

The transition records `global.fallout_event_timeline_generation`, `global.fallout_event_timeline_start_date`, and `global.fallout_event_timeline_start_day` on the successful map-return transaction, then ends with a short stabilization period:

- ordinary random events remain stopped
- Fallout survival decisions become visible
- each country receives its opening orientation event or mechanic panel
- mapmodes refresh
- severe state modifiers and wasteland rules remain active
- delayed regional wars and diplomacy begin after a grace period

Do not start every war, focus event, and flavour incident on the reveal day.

## Acceptance checks

- no normal super-event appears
- no ordinary super-event or shared global audio id is set
- dedicated Fallout dramatic audio plays once per transition audio generation when the configured audio mode permits it
- blackout cannot be closed during processing
- text beats advance through scripted events
- save-load resumes the correct beat
- state grading is deterministic
- every state is processed once
- every active country has a valid package
- every player continuation is materially created, assigned, committed, and collision-free
- old wars and subjects do not survive accidentally
- post-Fallout systems start only after validation
- every direct caller reaches the same transition framework

These are release gates. They are not all satisfied by the current implementation.

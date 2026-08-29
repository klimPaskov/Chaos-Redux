# Acceptance and Implementation Handoff

## Source-of-truth order

Implementation should use this order when two sources differ:

1. User corrections in the current accepted task
2. This revised Event 021 specification package
3. Current repository `AGENTS.md`
4. Current relevant Chaos Redux skills
5. Current live Chaos Redux implementation and shared contracts
6. Installed vanilla documentation and vanilla precedents
7. Offline Paradox wiki snapshot
8. Prior Event 021 planning package where it does not conflict with this revision
9. Catalog CSV exports as read-only snapshots

The authoritative event catalog workbook remains the only editable catalog source.

## Required implementation preflight

Before editing:

- read repository `AGENTS.md`
- read this complete Event 021 package
- read the current Event 021 files if any
- inspect Event 006 specs, registry, carriers, package initializers, focus assignment, forces, reinforcement, formables, AI, assets, and docs
- inspect Event 004 and Event 007 cluster behavior
- inspect Event 019 formation revolt boundaries
- inspect the specialized overlap events listed in Part 7
- read the required offline wiki pages
- read relevant installed vanilla documentation
- inspect vanilla civil-war, decision, mission, country, character, subject, faction, and asset precedents
- inspect existing Chaos Redux civil-war and dynamic-country precedents
- inspect the live HOI4 MCP schemas
- verify the authoritative workbook
- verify a free scenario ID
- run tag and character ownership audits
- spawn project subagents with `fork_context=false`

The implementation must not invent unavailable tool names or treat source review as equivalent to required MCP evidence.

## Recommended implementation tranches

### Tranche 1: Repository and contract map

Output:

- Event 021 current-state map
- Event 006 reusable API map
- overlap event boundaries
- cluster and scenario registry
- expected gameplay files
- asset consumers
- documentation and workbook surfaces
- blocker list

Use `chaosx_repo_explorer`.

### Tranche 2: Shared architecture

Output:

- script constants
- target and viability triggers
- hidden Fracture Pressure
- visible State Authority
- actor and front registry
- territory planner
- force planner
- Event 006 adapter
- cleanup
- recurrence
- generation tracking

Use `chaosx_scripted_system_architect` for reusable helper design and narrow implementation.

### Tranche 3: Baseline event

Output:

- entry dispatcher
- target pool
- six archetypes
- baseline map and force planning
- opening events
- government and opposition category phases
- baseline AI
- baseline outcomes
- event log and Event Details
- docs

Run event MCP inspection and baseline probability tests.

### Tranche 4: Decisions and missions

Output:

- phased category
- State Authority presentation
- government actions
- opposition actions
- selected-front flow
- missions
- costs
- success, failure, partial success
- AI
- cleanup
- localisation

Use `chaosx_decision_mission_auditor` after the owner implements the system.

### Tranche 5: Event 006 integration

Output:

- idempotent Event 021 origin adapter
- candidate validation
- Event 006 package creation
- former-host war
- focus loading
- force and reinforcement
- formation decisions
- recognition and diplomacy
- package cleanup
- nested eligibility

Use `chaosx_country_package_auditor`. Use the focus auditor only if focus files or loading behavior change.

### Tranche 6: Evolution I

Output:

- active and prefire paths
- major targeting
- multi-front plan
- distinct side objectives
- independent front settlement
- prevention actions
- AI and probability tests
- event and evolution logs

### Tranche 7: Evolution II

Output:

- neighbor exposure
- civilian relief
- arms-route control
- sponsorship
- mediation
- active-side adaptation
- strange incidents
- cleanup
- AI and probability tests

### Tranche 8: Evolution III

Output:

- world-threat source
- eligible-country registry
- risk bands
- bounded scheduler
- Critical queue
- theater cap
- nested crises
- generation cap
- high-chaos scaling
- global reactions
- cleanup
- performance tests

### Tranche 9: Wars cluster and manual scenario

Output:

- Event 021 cluster membership
- reservation and collision behavior
- skip reasons
- verified scenario ID
- four types
- four intensities
- confirmation
- immediate setup
- measured batch contingency
- bypass cleanup
- scenario docs and workbook fields

### Tranche 10: Presentation and achievements

Output:

- report and news assets
- static category picture
- category, decision, mission, idea, and achievement icons
- final localisation
- six achievements
- manifests and handoffs
- documentation

Use the proper asset subagents. Do not create unauthorized portraits or animation.

### Tranche 11: Improvement and completion review

After meaningful implementation:

- run `chaosx_improvement_loop_planner`
- resolve the addendum, closure handoff, or rejection
- run probability comparison
- run decision, country, focus where applicable, localisation, and completion audits
- run documentation curation
- update the authoritative workbook through the spreadsheet worker
- export CSV snapshots
- run acceptance scenarios
- report every blocker or simplification
- commit the completed plan as one intentional Git commit

Do not deploy another improvement loop for Event 021 while an earlier Event 021 addendum remains unresolved.

## Expected gameplay surfaces

The final exact file map belongs to repository exploration.

Likely event-owned or shared surfaces include:

- event definitions
- event registration and availability
- script constants
- scripted triggers
- scripted effects
- on-actions or bounded pulse adapters
- decisions and categories
- ideas or dynamic modifiers
- AI strategy and templates
- event logs and Event Details
- evolution logs
- cluster registry and logging
- scenario registry and UI
- country collections and Event 006 adapters
- characters and portrait references only when required
- focus loading only when required
- localisation and scripted localisation
- report and news sprites
- decision and idea sprites
- achievements
- event docs
- system docs
- authoritative workbook

Do not create a new file merely to match this list when an existing subsystem file owns the behavior.

## MCP requirements

### Event chains

Use the event inspection, rendering, and comparison routes for:

- dispatcher
- active-war evolution
- settlements
- scenario launch
- cluster integration
- cleanup
- actor and scope flow

### Probability

Every complex weighted surface requires:

1. baseline `hoi4.probability_inspect`
2. named scenario evaluation
3. sweeps where thresholds can reverse ordering
4. owner-applied patch
5. `hoi4.probability_compare` on the same scenarios
6. rendering when a matrix, timing graph, sensitivity view, or comparison improves review

Use simulation only for declared uncertain inputs.

Use sequence analysis only when the complete pool, cadence, recovery, caps, cooldowns, removals, resets, and terminal states are declared.

### Focus

If focus files or focus loading change:

- inspect the tree
- render the relevant branch
- review filters and navigation
- compare source changes
- run focus audit

### GUI

The accepted design does not require a new dedicated scripted GUI. Do not route the event to `chaosx_event_ui_worker` unless a later accepted addendum proves that normal decisions cannot present the system.

### Map

If the region planner requires map rewriting, inspect map data and use the supported map route. Ordinary state selection and transfer should remain gameplay scripting where possible.

## Probability acceptance scenarios

The full named matrix is in `021_random_civil_war_probability_scenario_matrix.md`.

Minimum required comparisons:

- stable minor versus unstable minor
- unstable minor versus stable major after Evolution I
- unstable major versus stable minor
- recent target versus comparable fresh target
- ordinary ideological actor versus complete Event 006 actor at baseline
- Event 006 actor at Evolution I
- one viable actor versus three viable actors
- negotiated settlement versus harsh settlement recurrence
- neighboring active war versus distant comparable country
- strange-incident chance in an ordinary side versus a long-lived high-chaos side
- Critical queue ordering
- scenario shares by intensity
- cluster overlap by chaos tier

The implementation owner chooses the intended tuning. The probability auditor reports actual behavior.

## Acceptance scenarios

### Baseline stable minor

Expected:

- limited opening
- one opponent
- coherent small region
- low force share
- clear category
- winnable government defense
- no irrelevant major systems

### Baseline unstable minor

Expected:

- serious or severe opening
- stronger opponent
- larger region
- State Authority pressure
- useful decisions and missions

### One-state country

Expected:

- same-tag takeover
- no invalid actor
- leader or government outcome
- real mission and consequences
- complete cleanup

### Subject country

Expected:

- valid overlord choices
- no automatic global subject revolt
- safe faction and war handling

### Evolution I medium country

Expected:

- three total belligerents when viable
- distinct goals
- separate front selection
- independent settlement
- rebel victory preserves unresolved fronts

### Evolution I major

Expected:

- strict viability
- several fronts
- viable government remnant
- safe external-war handling
- acceptable performance

### Event 006 independence front

Expected:

- complete package
- Event 021 origin
- former-host war
- Event 006 tree and decisions
- no Event 006 fire or evolution state change
- no duplicate identity

### Evolution II border region

Expected:

- exposure category
- relief and military aid separated
- sponsor and mediation AI
- no forced war in every neighbor
- cleanup after source war

### Strange incident

Expected:

- one active incident per side
- uncertain text
- visible effect and cost
- countermeasure
- no overlap with another event
- cleanup

### Evolution III stable country

Expected:

- compact band
- no decision wall
- long review interval
- easy containment

### Evolution III Critical country

Expected:

- visible emergency state
- queue entry
- no duplicate launch
- launch when capacity permits
- full Event 021 opening

### Nested human independence country

Expected:

- grace period
- valid actor
- generation tracking
- package identity preserved
- no actual nonhuman immunity

### Actual nonhuman country

Expected:

- excluded from automatic Event 021 and global risk
- no visible prevention category
- no scenario target

### Wars cluster

Expected:

- all members reserve before commitment
- correct collision behavior
- one pacing event
- useful skip reasons
- each member keeps identity

### Scenario Low

Expected:

- about one tenth of eligible countries
- minors
- limited fronts
- no evolution prerequisites

### Scenario Maximum

Expected:

- every eligible normal human country committed
- strongest sustainable plans
- actual nonhuman exclusion
- immediate or measured seven-day batch completion
- no terminal flag
- acceptable save and game-speed behavior

### Settlement and recurrence

Expected:

- every settlement type changes aftermath
- negotiated settlement can remain durable
- harsh settlement can raise recurrence
- no automatic immediate second war
- stale fronts and targets removed

### Save and reload

Expected:

- front registry persists
- selected-front state rebuilds safely
- State Authority persists
- missions persist correctly
- Event 006 origins persist
- scenario and evolution state persists
- cleanup remains complete

## AI acceptance

AI is accepted only when:

- role profiles produce different decisions
- governments defend capitals and supply
- independence actors pursue package goals
- sponsors limit commitments
- mediators do not arm sides
- neighbors separate relief from security
- successors rebuild before expansion
- invalid routes receive zero weight
- AI does not create unit, aid, or recognition loops
- AI responds to external war and equipment
- AI can use every player-facing action through an equivalent route

## Asset acceptance

Asset completion requires:

- final static source art
- processed PNG
- final DDS
- correct path
- correct sprite handoff
- manifest
- contact sheet where required
- correct transparency
- asset-type separation
- achievement triplets
- no animation requirement
- no custom 3D requirement
- Event 006 identity reuse
- no invented grounded portrait

## Documentation and workbook acceptance

Update:

- Event 021 event documentation
- shared civil-war system documentation if helpers become public
- Event 006 integration documentation
- Wars cluster documentation
- triggerable scenario documentation
- asset and achievement crosswalks
- Event Details and evolution wording
- authoritative workbook
- exported CSV snapshots

The workbook worker should mirror final in-game wording. It must not invent implementation facts.

## Completion report

The final implementation report should include:

- files changed
- systems implemented
- route and archetype coverage
- Event 006 package coverage
- AI profiles
- probability evidence
- performance evidence
- cluster and scenario evidence
- assets
- achievements
- documentation
- workbook export
- audit results
- accepted improvement-loop disposition
- remaining blockers
- simplifications and fallbacks

If no simplifications or fallbacks remain, state that explicitly and support it with evidence.

## Planning-environment disclosure

All files supplied in this task, all catalog CSV exports, and every TOML definition inside `subagents.zip` were read fully.

The live Chaos Redux repository, offline wiki snapshot, installed vanilla documentation, vanilla files, Workshop references, HOI4 MCP, and subagent execution interfaces were not available in this planning environment. They remain mandatory implementation gates.

The July 25 Event 021 File Library package was reviewed through its compiled master specification and key supporting records. Its loose package was not mounted for direct byte-level comparison. The revision file records which design decisions this package retains and changes.

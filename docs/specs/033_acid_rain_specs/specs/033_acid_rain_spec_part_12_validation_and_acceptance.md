# Event 033 Acid Rain, Part 12, validation and acceptance

## Acceptance principle

Event 33 is complete only when independent Major firing, cluster firing, all three evolutions, decisions, GUI, audio, assets, save migration, AI, and cleanup pass together. A working formation popup with placeholder movement is not a completed rework.

## Gate 1, registration and availability

Pass when:

- Event 33 appears once in the Major registry
- Event 33 appears zero times in repeatable and fire-once registries
- Chaos level 2 blocks it below 200 Chaos
- ordinary Major selection can choose it only when valid
- settings disable removes ordinary and cluster availability
- Event Details show Major, level 2, Natural Disasters, Severe
- all three evolution thresholds and states display correctly

## Gate 2, formation transaction

Pass when:

- valid registry builds once
- every eligible state maps to one region
- every country receives category state
- first front or global transition is valid
- super-event fires once
- formation Chaos fires once
- event history row exists once
- a failed precommit initialization rolls back without firing the event
- a postcommit failure enters recoverable fail-closed state

## Gate 3, bounded runtime

Static inspection must find no daily or weekly all-country plus all-state nested scan.

Runtime profile must show:

- regional pulse scales with active footprint
- multiple-front pulse scales with union of active footprints
- only global phase intentionally processes all frozen eligible states every three days
- GUI refresh does not mutate gameplay
- front movement and dissipation use scheduled dates
- state-control migration uses a narrow on-action path

## Gate 4, front movement and coverage

Test:

- each starting region
- islands with no land neighbors
- regions with fewer than three eligible states
- second visit with remaining untouched states
- two fronts competing for destinations
- three fronts with only two free regions
- load during warning
- load during drift
- region control changes

Pass when:

- active state belongs to one ordinary front at most
- warning target stays frozen
- no front moves into another active front's region
- untouched count never becomes negative
- touched count never decreases
- every valid state can be reached
- correction activates after two no-new-coverage movements
- full coverage is exact, not rounded

## Gate 5, dissipation

Pass when:

- no dissipation check occurs before complete coverage in regional phases
- final coverage date stores once
- fourteen-day minimum wait holds
- chance ladder uses stored check index
- final baseline check is guaranteed
- global minimum duration is at least forty-five days
- global eighth check is guaranteed
- successful dissipation blocks new cells, fronts, and contamination requests in the same transaction
- recovery tail can remain after acute closure

Run at least 10,000 synthetic movement trials per front count and one long in-engine observer campaign per evolution stage.

## Gate 6, mortality and Deaths

For every exposure type verify:

- opening receipt once per episode
- sustained pulse every three days only while active
- current state civilian population used
- vulnerability and protection clamps
- per-pulse and cumulative caps
- protected population floor
- `apply_exact_state_civilian_population_loss` called for every positive requested loss
- pre-pulse population minus post-pulse population equals `state_civilian_population_loss_applied`
- one Deaths registration using the same applied value
- state, country, and global Event 33 totals match the same applied value
- zero applied loss creates no death report or threshold progress
- replaying the same pulse key creates no second population loss
- changing only `local_manpower`, recruitable population, generic manpower, unit attrition, or counters fails the gate
- no duplicate direct Chaos for deaths

Test a tiny state, a protected-floor state, a very dense state, an occupied state, an active-combat state, full preparation, no preparation, repeated visits, Deaths logging disabled, and a deliberate duplicate scheduler call. Capture before and after state population for every case.

A build that reports civilian deaths without reducing real state population is rejected even if every other Event 33 surface works.

## Gate 7, damage and aftermath

Pass when:

- fractional pressure accumulates deterministically
- whole points target only valid existing buildings
- no negative building level occurs
- supply hubs are not deleted by ordinary pressure
- resource deposits are not permanently removed
- state acute modifier matches strongest current exposure
- severe cell overrides ordinary band without losing parent-front history
- leaving acute exposure calculates one aftermath tier
- recovery lowers tiers and cannot overrepair
- Humanitarian source registration and removal are balanced

## Gate 8, Preparedness and decisions

For every project tier and country band verify:

- exact displayed cost equals actual debit
- at most four spendable resource types
- exact stockpile is sufficient
- one item below requirement blocks action
- manpower reserve returns once
- consumed resources do not refund on cancellation
- project tier applies only on completion
- concurrent slot cap holds
- same target tier cannot start twice
- warning and completion dates display correctly

For urgent and recovery actions verify target validity, duration, cooldown, partial timing, and state-transfer behavior.

## Gate 9, Air Contamination

Pass when:

- formation uses actual applied delta
- weekly requests use stored coverage and intensity
- lifetime counter equals sum of actual Event 33 additions
- lifetime counter never exceeds 1500 bp
- Event 33 never raises global total above 5000 bp
- Event 33 adds zero at or above 5000 bp
- other systems can raise the global total above 5000 bp
- preparation never lowers Event 33 contamination request
- source ledger row persists after event end
- post-event source pressure decays without directly subtracting global contamination
- Air Cleanliness generates its normal Chaos once

Run the randomized 10,000-sequence cap test and save-reload tests at 1499, 1500, 4999, 5000, and above 5000 bp.

## Gate 10, evolutions

### Evolution I

- no severe cell before Rising Chaos
- safe active transition after threshold
- no stage rollback
- no direct Chaos for stage activation
- cell forecast, duration, cooldown, targeting, and impact receipt valid

### Evolution II

- second front guaranteed and distinct
- third-front probability inspected
- stable front records independent
- direct Chaos receipts apply once
- no destination collision

### Evolution III

- three-day transition
- every valid state touched and active
- global opening shock once
- global sustained pulse
- bounded superstorm count
- guaranteed endpoint
- no replay of formation super-event

## Gate 11, cluster integration

Pass ordinary Natural Disasters cluster without Event 33, then with Event 33.

Verify:

- Event 13 retains five logical slots
- Event 33 is sixth Severe member
- participation matches tier constants
- selected Event 33 becomes required
- Event 33 orders after all Event 13 slots
- queue with Event 33 uses Major effective pacing once
- queue without Event 33 uses repeatable pacing
- Event 33 reservation blocks ordinary duplicate firing
- Event 33 member dispatch does not reset Major weights twice
- cluster and ordinary event history remain separate and linked
- cancellation releases reservation and records outcome

## Gate 12, AI and probability

Run the full matrix in `matrices/033_acid_rain_ai_acceptance_matrix.md`.

Pass when:

- each capacity band has a payable route
- AI keeps accepted reserves
- AI prepares more aggressively as threat rises
- AI prioritizes high-population severe targets
- AI uses land and island cost variants correctly
- AI does not start actions that cannot affect the relevant window
- AI performs recovery after acute exposure
- no decision has zero AI chance through accidental weight collapse
- probability inspection shows normalized and reachable outcomes

## Gate 13, scripted GUI

At 1920 by 1080, 1600 by 900, and 1366 by 768 verify:

- map fits
- seven region rows fit
- one, two, and three front cards fit
- global card and superstorm list fit
- timers and counters refresh
- Preparedness component pips match runtime
- tooltips remain on screen
- animation toggle and static fallback work
- opening and refreshing the window do not change gameplay
- multiplayer clients see the host state

## Gate 14, reports and text

Pass when:

- super-event fires once with final verified quote and audio
- arrival, warning, severe, casualty, preparation, departure, split, global, dissipation, and recovery reports use correct scopes
- cooldown classes remain independent
- reports use stored facts
- no report claims unimplemented death or damage
- no routine state drift creates popup spam
- localization has no missing keys or malformed encoding
- final text passes the localisation auditor

## Gate 15, assets and audio

For every asset verify:

- source record
- expected and actual dimensions
- nonblank pixels
- correct alpha
- correct DDS format
- correct sprite ID and path
- no missing frame
- no frame count mismatch
- icon readability at game size
- news grayscale treatment
- super-event image fit

For audio verify:

- real source recording
- license proof
- unique use
- excerpt two minutes or less
- coherent start and end
- WAV and OGG conversion
- sound registration
- audio catalogue entry
- in-game volume and stop behavior

## Gate 16, achievements

For all ten achievements verify:

- baseline stored at correct date
- deadlines persist
- debug bypass disqualifies
- tag and controller changes follow shared ownership rules
- exact thresholds use actual applied values
- hidden achievements reveal correctly
- one completion only
- Event Details status correct
- icon registered and visible

## Gate 17, old-save migration

Test four saves:

- prototype never fired
- prototype active with valid current region and acute states
- prototype completed
- ambiguous prototype state

Pass when:

- new schema writes once
- active migration preserves real acute states
- cloud-only states are not falsely counted as acute coverage
- no historical deaths are invented
- completed old event does not reactivate
- ambiguous state closes safely
- old missions and daily on-action no longer run
- reload after migration is stable

## Gate 18, multiplayer and determinism

Test two-player and four-player games with different countries.

Pass when:

- one weather path exists
- clients show identical front and coverage state
- national Preparedness stays country-specific
- simultaneous decisions debit correct countries
- no client GUI click advances scheduler
- save reload preserves accepted random draws
- cluster sequence and Major pacing remain identical for all players

## Gate 19, documentation and catalog alignment

Pass when:

- workbook source has accepted Event 33 row
- cluster workbook has Event 33 sixth member
- generated CSV exports match workbook
- repository docs no longer call Event 33 repeatable
- event cluster docs describe mixed Major pacing
- Air source docs list Acid Rain
- super-event and audio docs list final source
- asset manifest and achievement docs complete
- old prototype documentation removed or clearly archived

## Required specialist review

Before acceptance, route final work through:

- repository explorer
- scripted-system architect
- decision and mission auditor
- AI probability auditor
- event UI worker
- generated event-art worker
- super-event text researcher
- super-event audio researcher
- localisation auditor
- event completion auditor
- documentation curator
- improvement-loop planner

Each reviewer works from the completed implementation and returns concrete findings. Open critical findings block acceptance.

## Completion definition

Event 33 is accepted when every gate above passes, all required assets and audio exist, no critical validation issue remains, the catalog source is aligned, and the old daily prototype path is absent from active runtime.

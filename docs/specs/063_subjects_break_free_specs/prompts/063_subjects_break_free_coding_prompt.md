# Coding prompt: Event 063 Subjects Break Free

Implement Event 063 in Chaos Redux according to the complete specification package under:

`docs/specs/063_subjects_break_free_specs/`

Read every specification, diagram, research note, quality matrix, catalog handoff, and specialized prompt before editing the repository. Follow `AGENTS.md`, `CHAOS_REDUX_MECHANICS`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaosx_dynamic_triggers`, and `chaosx_dynamic_effects`. Preserve the explicit authorization gate in `chaos-redux-debug-playtest`.

Do not implement from this prompt alone. The spec files are the source of truth.

## Core event

Replace the old Event 063 concept with `Subjects Break Free`, a Chaos level 1 Minor Repeatable event and Medium member of the Liberations cluster.

Each firing must:

- build a frozen valid pool of existing subject countries
- scale the bounded release count with that pool
- select without replacement
- reserve the entire selected batch before any release
- release countries in place without recreating tags
- preserve territory, government, leaders, characters, armed forces, equipment, production, research, laws, ideas, focuses, intelligence state, claims, cores, and current country identity
- resolve negotiated, recognized, contested, or armed separation
- register shared liberation origin without taking ownership from Event 006 or Event 005
- publish one global report and direct human notices
- clean every reservation and temporary record

Event weight is `N/A` when no valid subject exists.

## Shared ownership and collision safety

Implement the neutral liberation-origin contract and Event 063 transaction through the shared system prompt. Event 063 must never write the Independence Wave private release ledger, assign Event 006 anchors, create Event 006 country packages, or alter Soviet Collapse private authority and League systems.

Use the Liberation Release Coordinator before country changes. Resolve collisions with Event 006, Event 005, Allies Backstab, civil-war splits, annexation, and country replacement. Preserve successful releases if a later candidate invalidates.

First origin is permanent. Latest liberation can change. Becoming a subject suspends active network status. A later valid return to independence can reactivate it.

## Settlement and multiplayer

Independence happens before reaction choices and cannot be vetoed.

Implement:

- subject postures for conciliatory, guarded, and defiant settlement
- former-overlord batch policies for recognition, association, contest, and restoration
- pair-specific results from choices and campaign facts
- safe agreement cleanup and conversion
- narrow temporary claims and restore-subject goals
- common-war topology gates
- return or cleanup of expeditionary control before hostility
- safe faction retention or departure
- human-human pending settlement with a bounded deadline
- a pragmatic timeout that never starts restoration war for a silent human player

Player and AI choices must resolve without global synchronization or multiplayer deadlock.

## Evolutions

Implement all three evolutions with shared toggles, dynamic pacing, active-event entry, and pre-fire evolved opening.

### Evolution I at 200+

- select one same-overlord cohort of two to five valid subjects
- increase the batch while keeping a hard cap of eight
- create immediate recognition and cooperation opportunities
- avoid automatic faction creation

### Evolution II at 400+

- allow refused cohorts to enter one compound independence war
- use one breakaway war leader and one former-overlord side
- create no more than two new Event 063 theaters per firing
- leave unsafe cohort members in contested separation
- cap Event 063 direct liberated-state interveners at three per theater
- keep material aid more common than direct intervention
- use restore-subject and independence-recognition objectives, not default annexation
- keep the baseline firing cap at one new war theater and the Evolution II cap at two across compound and individual wars

### Evolution III at 600+

- allow a viable founder to call a Liberation Congress
- require enough compatible full-member candidates
- form the Event 063 Liberation Pact only after sufficient acceptances
- use full members, partners, and observers
- never force countries from unrelated factions
- implement leadership transfer, admission, exit, censure, suspension, expulsion, and dissolution
- preserve the informal network after Pact dissolution

Evolution activation itself gives zero Chaos.

## Liberation Pact mechanic

Liberation Cohesion is the only persistent Event 063 number shown to players. Keep all supporting scores hidden.

Implement the 0 to 100 value, its four bands, the four Pact Charter spirit states, causes, consequences, unlocks, AI behavior, anti-farming guards, and dissolution grace rules from Part 3.

Pact decisions must change cohesion through real commitments, aid, defense, mediation, membership, abandonment, and member conflict. Do not create a passive meter detached from gameplay.

The Event 006 congress and Event 005 Free Republics' League remain owner controlled. They may cooperate or hold partner status without forced merger.

## Decisions and missions

Implement every accepted phase family through `chaos-redux-decisions-missions` and the specialized decision prompt.

Use one ordinary category with a static picture. Keep three to five decisions visible in ordinary play, never more than six, and no more than three active missions.

Use real costs such as equipment, support equipment, artillery, trucks, trains, fuel, convoys, civilian factories, military experience, command attention, stability, war support, division commitment, access, relations, time, and Liberation Cohesion. Do not reduce the system to political power or command power purchases.

Aid must transfer real donor capacity. Support for a remaining subject can change pressure, autonomy, or preparedness, but cannot directly release it.

Implement the temporary idea lifecycle for Contested Sovereignty, Former Authority Disputed, Independence War Mobilization, and the Pact Charter states. Prevent stacking duplicate copies and clean obsolete decisions, missions, promises, targets, and modifiers.

## AI and probability

Implement the actor matrix from Part 5 and every named scenario from the probability file.

Before claiming the weighted behavior complete:

1. spawn `chaosx_ai_probability_auditor`
2. run `hoi4.probability_inspect`
3. evaluate the complete named scenario matrix with `hoi4.probability_evaluate`
4. sweep material factors with `hoi4.probability_sweep`
5. compare before and after corrections with `hoi4.probability_compare`
6. use `hoi4.probability_simulate` only for the declared uncertain mixed pools
7. use `hoi4.probability_sequence` only for a fully declared release sequence
8. render rankings, timing, and matrices when useful

Correct any valid option that is starved, invalid option that remains dominant, unexpected rank reversal, or timing band failure. Do not claim exact universal probabilities for incomplete campaign pools.

## Chaos impact map

Implement the complete Chaos map in Part 4.

- use the shared liberation source once per actual country transition
- use shared war, peace, faction, puppeting, annexation, and death sources
- give zero Chaos for evolution eligibility, activation, logging, and branch unlocks
- do not add a duplicate Event 063 batch grant
- guard release cycles, war openings, origin writes, and cohesion actions against farming
- verify that cluster firing does not duplicate member Chaos

Report evidence that generic sources are not counted twice.

## Cluster integration

Add Event 063 as a Medium member of Liberations, Cluster ID 2. Preserve one cluster pacing event and separate member effects and history. Create the shared release-coordinator generation before any liberation member acts.

The supplied catalog has no Domestic Unrest ID. Do not guess one. Add the requested secondary Medium membership only after a verified cluster row and runtime ID exist. Until then, keep Event 063 primarily mapped to Liberations and document the pending secondary integration.

## Presentation and localisation

Implement one global report per firing, direct events for affected human countries, hidden AI resolution, first-use news for the first cohort, first compound war, and first Pact congress, plus Event Logs and cluster history.

Write final player-facing event, news, decision, mission, idea, achievement, Event Details, GUI, and spreadsheet text from the direction in Part 6. Do not copy working labels as final localisation. Include dynamic countries, former overlords, counts, outcomes, and current phase. Keep hidden weights and future surprises out of visible text.

## Assets

Produce and wire every row in the Part 6 asset matrix through the asset prompt.

- report image at 210x176 with the standard processed card treatment
- three news images at 397x153 in black and white
- decision category icon and static picture
- fourteen decision icons at 32x32
- seven idea and cohesion-state icons at 64x64
- Liberation Pact faction emblem using the verified consumer
- four achievement icon triplets at 64x64

Build the requirement-to-runtime crosswalk from accepted rows. Preserve sources, hashes, processing records, DDS validation, registrations, consumers, and screenshots. Do not claim assets complete while any accepted row is missing or unwired.

## Achievements

Implement all four achievements through the achievement prompt:

- Independence Secured
- Pact Founder
- Independence War Victory
- Peaceful Release

Use stable bounded trackers, save persistence, exact disqualifiers, one-shot completion guards, final localisation, and complete icon triplets. Test positive and negative paths, tag switching, reload, and multiplayer attribution.

## Documentation and catalog

Update the authoritative event workbook, then regenerate CSV exports. Change Event 063's name, details, type, Chaos level, cluster, severity, status, and evolution directions. Add Event 063 to the Liberations member list. Do not edit CSV exports as source files.

Create permanent documentation for the event, shared origin contract, decisions, Pact, AI audit, Chaos map, assets, achievements, and playtest evidence. Update dynamic trigger or effect registries only when a helper is genuinely neutral and reusable.

## Validation

Run the complete acceptance matrix with repository checks, HOI4 MCP evidence, parser validation, event and probability comparisons, asset review, and documented test cases for save and reload, multiplayer human-human settlement, cluster firing, owner collision, war topology, achievements, cleanup, and repeated firings. Invoke the autonomous `chaos-redux-debug-playtest` workflow only after the user explicitly authorizes desktop control. Until then, prepare the live test matrix and leave actual in-game execution to the user.

Before claiming near completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false`. Resolve its expansion addendum or closure handoff. Then run `chaosx_event_completion_auditor`, `chaosx_localisation_auditor`, `chaosx_decision_mission_auditor`, `chaosx_scripted_system_architect`, `chaosx_documentation_curator`, and the relevant asset workers.

Do not use fallbacks, silent simplifications, temporary content, placeholder art, unbounded scans, or good-enough approximations. Report every design point that cannot be implemented cleanly. Do not claim completion until the repository, runtime behavior, assets, localisation, docs, audits, and acceptance evidence satisfy the full package.

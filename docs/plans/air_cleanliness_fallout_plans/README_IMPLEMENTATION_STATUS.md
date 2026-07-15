# Air Cleanliness and Fallout Implementation Status

Status reviewed against the live working tree on 2026-07-15.

Overall status: partial implementation with hard release blockers. This document does not claim that Fallout, the manual scenario, the world rewrite, or the player handoff is complete.

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Design authority

The source specifications under `docs/specs/air_cleanliness_fallout_specs/` remain authoritative. This plans directory records implementation evidence, blockers, accepted decisions, audits, and resume state. It does not narrow the source design.

Fallout remains an unnumbered system package with dedicated ownership of:

- `events/fallout_world_end_events.txt`
- the `chaosx.fallout` event namespace
- Fallout scripted effects, triggers, constants, GUI, GFX, assets, and documentation
- the blackout transition and post-Fallout rewrite
- the dormant exact-province manual scenario substrate

## Environment and proof basis

- Installed Hearts of Iron IV build inspected: 1.19.2.0
- Required offline wiki pages inspected from `paradox_wiki/`
- Official installed documentation and vanilla precedents inspected locally
- Hearts of Iron IV runtime was not launched and must not be launched for this documentation reconciliation
- Static artifacts and source inspection are evidence only, not runtime acceptance
- The optional offline event inspector returned `ARTIFACT_STORAGE_LIMIT`. It scanned no file and produced no artifact, so it is not part of the proof basis.

## Live implemented foundations

### Air Cleanliness

The live Air system includes global contamination basis points, monthly host-owned updates, chemical and nuclear state inputs, natural smoke and ash pressure, threshold behavior, winter pressure, treaty behavior, nuclear fallout state intensity, UI read models, and a request path into the dedicated Fallout coordinator.

### Fallout request and blackout skeleton

The live Fallout package includes:

- `fallout_request_aftermath` and request validation
- one project-coordinator reconciliation path with an at-most-once global-date receipt
- a versioned transition envelope with schema 11
- blackout GUI state and phase events
- player and world snapshots
- deterministic state grading and survival values
- generation-bound grading, post-mutation Deaths, permanent state-building loss, province supply-network collapse, no-upgrade category-conversion, and grade-modifier receipts
- partial old-world diplomacy cleanup with exact truce and market-access readback, exhaustive docking-rights inverse coverage, and exhaustive resource-rights inverse coverage
- deterministic provisional classification for eleven live government archetypes, with Machine Protocol fail closed
- player-first source and state reservation planning, including landless-human materialization rows
- generation-bound successor conflict inventory with country, possible-country, state, reservation, and known package-ownership rows
- schema-2 post-allocation proof contract with reciprocal source-output conflict links, unique country and capital checks, exact landholder coverage, package layers, and cleanup ownership
- two-pass player commit preflight for existing current-generation targets
- durable assignment recording, retry recovery, commit reconstruction, and collision validation
- strict map-return postconditions
- exact event-timeline generation, date, and arithmetic day receipts written only by a successful current-schema map return
- a formula-neutral survival identity transaction with aligned country and state arrays, immutable source provenance, fixed resource indexes, and a pre-player-continuation commit barrier
- a dormant living-world registry with aligned country, generation, stable-index, and committed-survival binding receipts
- schema-2 country runtime rows for five-part orientation, fatigue slots, ordinary cooldown, one fixed ordinary opening, compact arc, delayed-result, reciprocal bilateral, cancellation, cleanup, and routing receipts
- a generation-bound monotonic ticket allocator, three independent compact-ledger reconciliation cursors, an ordinary receipt reconciler, exact dispatch envelopes, and mirrored issuance receipts
- exact token-authenticated issued bilateral response, orphan cancellation, and cleanup terminalizers with no detached acknowledgement path
- a scheduler activation gate with no setter and no defined living-world event blocks

These are foundations. The phase chain cannot yet produce a valid complete post-Fallout world.

### Dormant living-world scheduler substrate

The successful map-return transaction freezes the current transition generation, engine date, and engine day for exact campaign-phase arithmetic. The existing at-most-once project coordinator maintains the timeline and can build the country registry once after final successor allocation proves current. It does not add a recurring world-country pool.

Registry validation proves aligned country, generation, and index arrays. The stored index must equal the real array position, which rejects duplicate country rows without a whole-world duplicate scan. The ready flag is written only after the full payload passes, then the initialization request is cleared. Later annexation retains the frozen identity without rerunning successor allocation. Every member receives current scheduler schemas, twenty nonnegative family-fatigue slots, a hard immediate-family repeat veto, ordinary and quiet-period due days, five independent orientation receipts, one empty fixed ordinary-opening receipt, and empty aligned arc, delayed-result, and bilateral arrays.

Schema 2 supplies idempotent ordinary-opening, arc, delayed-result, and reciprocal bilateral reservation APIs. The fixed ordinary receipt owns at most one crisis opening per country and does not consume a major-arc slot. It stores distinct human and AI event tokens and commits its pending flag last. Mutable liveness and due-day checks apply only to new work, while exact retries authenticate the stored payload. An issued ordinary receipt, delayed row, or bilateral response remains as a blocking tombstone until the exact engine event consumes it or cancels a stale subject through its issued wrapper. Generic reconciliation cannot withdraw those events or admit a replacement beside them. Public ticket-only delayed terminalizers and public bilateral pair terminalizers reject issued rows. Public bilateral cleanup release also rejects an issued local row. Shared cancellation history records its transaction source, which prevents cross-family retry authentication. It derives the three arc-slot flags from compact rows, records typed owner, actor, target, and reciprocal loss, and requires cleanup and dispatch envelopes to match their source ticket. A country that no longer exists cannot receive a new reservation or dispatch envelope. Bilateral status changes write both payloads before either status, authenticate the initiator cleanup owner, prove both reciprocal directions, and restore both snapshots on a failed commit. Exact issued bilateral response wrappers authenticate the event token before resolving or cancelling both reciprocal rows. Orphan reconciliation retains an issued local row, while the exact cancellation wrapper may terminalize that local tombstone after reciprocal proof is lost. Exact issued cleanup removes the local row and consumes the envelope in the same effect chain. No detached acknowledgement API exists. One primary frozen registry country reconciles per date and selects the fixed ordinary receipt plus one primary row from each compact transaction family. A proven bilateral pair may also mutate its exact reciprocal row. The selected country can issue one exact envelope through the documented tokenized `country_event` route only after a mirrored issuance receipt commits. That receipt prevents repeat command emission while the event remains unresolved. Future ordinary content must use the exact consume or issued cancellation wrapper. Issued delayed and bilateral result, cancellation, and cleanup wrappers expose token-authenticated terminalization that consumes the envelope without a second acknowledgement. No event block calls these wrappers in this tranche. Recurring reads are linear in the local ledgers. Production-only full uniqueness gates are quadratic in each local compact ledger. Delayed and bilateral queue caps remain absent. Paired runtime-schema-1 and registry-schema-1 rows can promote only after the current map-return, a fully current committed survival ledger, and every preserved runtime field pass, while every later transaction surface is empty or absent as required. Existing schema-2 rows can separately promote only an exactly absent ordinary receipt while production remains disabled. Promotion walks the numeric frozen-registry index array and commits its global receipt only when every index loads the matching country context and the proven count equals the registry count. It accepts registry schema 1 or 2 only while dormant, which lets the supported current-runtime and schema-1-registry path prove every receipt before binding eligibility. The binding transaction writes schema 2, reruns the idempotent promotion, and requires the complete current payload. The accepted specs do not define fatigue mutation, decay, or score magnitudes, so those producers remain absent.

The transition now stages exact country and state survival identities after final allocation and blocks player continuation until the committed ledger exists. An exact survivor-allocation recovery wrapper can rebuild only a malformed uncommitted identity payload. It requires the sole `survival_ledger_incomplete` error signature when an error exists, current planning and allocation ledgers, no committed survival ledger, and no player-continuation commit. A malformed staged payload without an error is also rebuilt from the current allocation because the caller tests structural proof instead of trusting the staged flag. The row shape reserves raw state values, country aggregation receipts, immutable initial values, and mutable values without writing any of them. Numerical initialization, aggregation rules, validation, row commits, and the global ready setter remain absent. Candidate selection, calls to the ordinary reservation API, living-world event definitions, actual human choice content, hidden AI mechanical resolution, content-owned cleanup execution, bilateral wrapper callers, fatigue mutation and scoring, orientation event content, and debug presentation remain absent. Activation flags have no setter. Typed suffixes `100` through `126` reserve identities only. Defined blocks in that range: `0`. Countable living-world blocks toward the release floor: `0`.

## Dormant manual scenario substrate

The installed-build sweep proof contains 10,154 valid assigned land provinces across 1,081 states.

- 118 assigned non-land provinces are excluded.
- 126 assigned land targets in impassable states are included because no official exclusion was found.
- Batches 0 through 39 contain 250 targets each.
- Batch 40 contains 154 targets.
- The total is 41 batches.
- The ledger CSV `batch_index` uses floor division of the zero-based target position by 250 and matches the generated effects.

The event token layout is identity-bearing:

- `.900` is the bootstrap.
- `.910` through `.950` identify batches 0 through 40.
- `.960` through `.966` identify verifier attempts 0 through 6.
- `.903` is the exact countdown callback.
- The former generic `.901` and `.902` callbacks are absent.

The dormant manual runtime ledger is schema 2. Each scheduled batch, verifier, and countdown callback records the active transaction generation. Both the host validator and the hourly callback preflight reject stale or inconsistent ledgers before another native batch can run. The callback recomputes the exact issued-count-to-cursor and last-completed-batch invariants before opening the launch window. The countdown event and request wrapper independently validate the active token. Successful standard-request handoff clears both the due flag and countdown schedule provenance. Schema 1 active manual transactions fail closed.

Static control flow requires issued calls, observed callbacks, unique struck states, state strike totals, and array size to agree before aggregate consequences run. Aggregate Deaths, fallout, Air Contamination, Chaos history, condemnation, and treaty consequences then run once. The countdown end is stored as the verified start day plus seven. Only the engine-scheduled seven-day callback may submit the request. Daily reconciliation cannot submit or reconstruct it, and lost ownership or an overdue callback fails closed.

The public scenario row and dispatch are absent. The live registry reaches SCN-013 with The Unbidden Muster. Event 20 still reserves raw id 12 for Black Plague without registering a live SCN-012 row. Fallout reserves SCN-014 as exactly one greater than the highest live assignment and does not renumber or reuse any existing id.

## Runtime release boundary

Static inspection does not prove that `launch_nuke` with `use_nuke = no` emits exactly one synchronous `on_nuke_drop` callback for every scripted call. It also does not prove native acceptance for all target classes, bounded batch cost, save integrity, multiplayer synchronization, or presentation quality.

Vanilla `on_nuke_drop` schedules twelve one-day nuclear news events per callback. If all 10,154 scripted calls emit callbacks, vanilla may schedule about 121,848 one-day news event attempts. The Chaos Redux callback cannot suppress that separate vanilla branch. Callback occurrence, callback synchrony, and this news-event load are release blockers.

## Transition and migration boundary

Schema-11 migration is fail closed:

- completed schema-10 and older saves are promoted non-destructively and are marked as lacking both current-schema and supply-network receipts
- active schema-7, schema-8, schema-9, and schema-10 saves rebuild only while still in the snapshot phase, before snapshot application or destruction, and without an unrelated error
- an active schema-10 phase 2 transition can promote before grading mutation
- an active schema-10 phase 3 through 6 transition can promote only before allocation, with current grading, and with exact live-to-frozen supply-network equality for every destructive-grade state
- promoted phase 5 or 6 transitions rewind to physical collapse and discard derived government and conflict rows
- completed legacy saves receive no fabricated receipts and do not replay destruction
- the former schema-3 map-return-error promotion is removed
- every other incomplete legacy state remains under blackout
- an incomplete terminal state with no schema remains under blackout
- migration does not infer that a missing `fallout_transition_destructive_started` marker means an old transition is safe
- no generic pre-destructive restart and no legacy altered-grade replay are active behavior

Completed legacy Fallout saves have no proven reveal date. Migration does not invent an event-timeline start date or request scheduler initialization for them. That policy remains blocked pending approval.

Player source reservation is separate from final destination materialization. Every snapshot-origin human state is reserved before the successor inventory is frozen. A landless human is retained as an explicit emergency-materialization source instead of raising a false missing-anchor error. Derived inventory schema 1 binds every row to the active transition generation. The validator checks every live country, every possible country scope, every state, exact candidate and reservation membership, human ownership and control, known overlapping event-package ownership, and capital consistency. A proposed target is commit-ready only when it already exists, has country and focus packages from the current transition generation, owns survivable territory, and owns and controls the exact capital reserved for that player. A global two-pass preflight validates all existing commits and proposed targets before any player switch. Exact single-error signatures can re-enter snapshot, reservation, inventory, peace-conference, or player-commit paths without taking ownership from another failure. Once allocation initialization consumes the reservation ledger, later drift records its own fail-closed error and cannot rebuild those rows.

World transition schema 11 makes the snapshot, grading, population-loss, and physical-collapse ledgers hard phase barriers. One epoch freezes every player, state, and country input used by grading, survival, population targeting, category conversion, and provisional government classification. Air Winter owns a versioned live producer receipt. Valid states initialize and normalize through that producer before exact live-to-frozen comparison. Invalid states receive an explicit N/A kind and complete Air-owned payload. Every state separately freezes and proves its live category. Air Winter's historical original category remains provenance and classifier memory. Exact live owner, controller, and category equality are checked at capture. Blackout and world-end flags are committed only after both snapshot halves pass. Air Winter state mutation pauses during the active rewrite without adding a world pass. Grading rows recompute score and survival from frozen inputs. Population rows store frozen intent, clamp against live population, issue one mutation, observe the result, and only then register the exact loss through Deaths without applying state population twice. Global Deaths totals, sequence, and state-map ledger movement have stored receipts. Physical rows prove permanent `remove_building` loss for five state-building families, a category target no higher than the frozen live baseline, exact grade and subtype modifiers, and rewrite generation. Dead-city and higher grades also issue `set_building_level` through the documented all-provinces selector for `supply_node` and `rail_way`. Each family retries only the idempotent set-to-zero operation until both its aggregate and direct province query report zero. Current receipts require zero aggregate levels and no selected province above zero before the world receipt commits. Durable receipts protect later transition phases from ordinary construction drift. Exact railway topology mutation and immediate engine visibility remain runtime blockers because Hearts of Iron IV was not launched. Each phase advances only after every state row passes. The diplomacy transaction uses the approved `market_access_rights` cancellation pattern and the official `has_market_access_with` trigger for a global postcondition. Government classifier schema 2 aggregates the frozen rows before ownership changes. Eleven archetypes are live. Machine Protocol requires machine-continuity, command-network, EMP-survival, technical-state, and remote-refuge evidence, and remains unreachable until the missing producers exist. The provisional result is stored separately from the final package archetype. The classifier does not change politics or activate content.

The conflict inventory is not an allocator. It does not choose tags, final package layers, conflict results, or cleanup owners. Its known package-ownership helper must be reviewed again against the live repository before ownership changes begin. Successor allocation schema 2 requires each input row to retain its frozen generation, leave the pending state, and own current resolution and cleanup generations. Each non-retired input row and output assignment must name each other, match resolution and generation, and share the same cleanup owner. Converted, released, and dynamically created outputs require distinct current-generation provenance receipts. Frozen possible-country membership is not release proof. A retired input must be landless and cannot name an output. The proof also cross-links every player-reserved source to the same continuation target, requires unique assigned countries and capitals, exact live-landholder coverage, and current package generations. Its guarded finalizer is the only setter for `fallout_successor_allocation_complete`, but no active allocator calls it or produces the required rows.

The 99 accepted candidate rows have stable `fallout_country_memory` ids in their source-matrix order. This closes the numeric identity gap only. The exact twelve-country proof roster, primary state packages, capital order, tag coexistence, cosmetic ids, and Machine Protocol identity remain unapproved.

The commit path writes a durable assignment origin and generation before an optional `change_tag_from`, commits only after the target appears human controlled, and rebuilds and revalidates persisted commits on retry. This can commit an uncommitted player to an already materialized, current-generation target.

Actual successor materialization, country and focus package producers, candidate-choice UI, and general successor allocation are not implemented. The pre-allocation barrier can retain fragmented, refugee, altered, emergency, and landless player sources without pretending their destination exists. The code can set `fallout_player_materialization_required`, but it cannot resolve it. Package and focus generations remain mandatory for every commit and map-return validation.

Static inspection cannot prove that `change_tag_from` makes the destination report `is_ai = no` immediately in the same effect chain. No Hearts of Iron IV run was authorized, so this immediate observation remains a runtime blocker.

The old-world diplomacy proof gate also remains unresolved. Truces now use the official zero-day inverse after white peace and an exhaustive ordered-pair readback. Docking rights have exhaustive generation-bound inverse application proof. Market access and resource rights are no longer missing surfaces. Resource-rights readback covers observable grants, while the unconditional country-state inverse sweep covers the trigger's resource-free-state blind spot. Lend lease has an official ordered-pair detector and current-generation proof when the surface is empty. Ordinary imports have a documented aggregate positive-flow detector, but no route enumerator or inverse. Intelligence has partial detectors and narrow mutations, but no complete reset for agencies, upgrades, networks, operations, decryption, intel, candidates, and operative-slot locks. Active lend-lease cancellation, ordinary imports, intelligence, and expeditionary return still block map return until their required postconditions are genuinely satisfied. The detailed proof matrix is [FALLOUT_DIPLOMACY_AND_INTELLIGENCE_RESET_MATRIX.md](FALLOUT_DIPLOMACY_AND_INTELLIGENCE_RESET_MATRIX.md).

## Hard release blockers

1. Register the reserved SCN-014 public Fallout row and dispatch only after the exact native sweep release gate passes.
2. Prove native strike acceptance, one callback per call, callback timing, performance, save behavior, and multiplayer behavior in a separately authorized runtime pass.
3. Resolve the possible 121,848 vanilla news-event attempts without reducing the exact 10,154-target requirement.
4. Prove that the all-provinces `set_building_level` route removes every supply node and railway edge and exposes the result to the receipt without issuing a family twice.
5. Implement general successor allocation and the country and focus package producers, including current transition generation ledgers. Re-audit every live event-package producer before the first state transfer or tag materialization.
6. Implement player-successor materialization, candidate selection and choice UI, and collision-safe multiplayer handling where the source spec requires them. Prove the immediate `change_tag_from` handoff observation in an authorized runtime pass.
7. Complete and prove the old-world diplomacy reset surfaces.
8. Close the tracked blackout input, scripted-GUI binding, and all-resolution drawing-order gates. The mapmode frame gate is resolved by `AIR_WINTER_MAPMODE_ICON_PROOF.md`.
9. Finish regional successor content, focus content, AI, localisation, assets, documentation alignment, and the required audits.
10. Resolve literal multiplayer lobby-host authority or retain it as an explicit engine blocker. The live project coordinator is deterministic and date-bounded, but it is not a documented lobby-host predicate.
11. Complete and review survival numerical production, validation, row commits, and the ready setter, then implement five-part orientation content, bounded candidate selection, event definitions, human choices, hidden AI resolution, content-owned cleanup, fatigue behavior, and runtime persistence proof before enabling the living-world scheduler.

## Resume map

- Exact sweep proof: `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`
- Manual scenario contract and release gates: `MANUAL_FALLOUT_SCENARIO_PLAN.md`
- Current hard blockers and accepted decisions: `BLOCKERS_AND_DECISIONS.md`
- Transition ordering and postconditions: `FALLOUT_TRANSITION_ARCHITECTURE.md`
- Trade, force-transfer, and intelligence reset proof: `FALLOUT_DIPLOMACY_AND_INTELLIGENCE_RESET_MATRIX.md`
- Air Winter snapshot provenance and transactional lock: `FALLOUT_AIR_WINTER_SNAPSHOT_PROVENANCE_PROOF.md`
- Province supply-network collapse and migration proof: `FALLOUT_SUPPLY_NETWORK_COLLAPSE_PROOF.md`
- Source-of-truth routing: `SOURCE_OF_TRUTH_RECONCILIATION.md`
- Implementation tranches: `IMPLEMENTATION_TRANCHE_PLAN.md`
- Gameplay status for Air Cleanliness: `docs/systems/air_contamination_mechanic.md`
- Manual runtime constants: `common/script_constants/fallout_manual_scenario_constants.txt`
- Manual sweep effects: `common/scripted_effects/fallout_manual_province_sweep_effects.txt`
- Manual coordinator effects: `common/scripted_effects/fallout_manual_scenario_effects.txt`
- Fallout transition effects: `common/scripted_effects/fallout_world_end_effects.txt`
- Fallout postcondition triggers: `common/scripted_triggers/fallout_world_end_triggers.txt`
- Fallout event tokens and phase events: `events/fallout_world_end_events.txt`
- Dormant scheduler proof: `FALLOUT_EVENT_SCHEDULER_PROOF.md`
- Living-world suffix reservations: `FALLOUT_EVENT_ID_LEDGER.md`

## Simplifications and fallbacks

No fallback is approved. The exact province sweep, seven-day delay, full successor rewrite, player continuation, and postcondition-gated map return remain required. Missing work is reported as blocked rather than presented as complete.

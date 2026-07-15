# Blockers and Parent Decisions

## Current blocking items

## B1: writable repository and local official documentation

Status: resolved

Required evidence:

- writable local Chaos Redux checkout
- local `paradox_wiki/` snapshot
- local Hearts of Iron IV `documentation` folder
- local vanilla game files

Evidence:

The writable checkout, offline wiki snapshot, official documentation, and installed vanilla files were inspected locally. Engine-sensitive results are recorded in `ENGINE_SURFACE_PROOF.md` and `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`.

## B2: exact province-wide thermonuclear strike

Status: dormant substrate implemented, runtime release proof blocked

Accepted requirement:

Every valid province must receive a thermonuclear strike.

Observed evidence:

- official `launch_nuke` accepts a province and explicit thermonuclear type
- vanilla nuclear raids pass a variable-backed province id
- the installed map contains 10,154 valid assigned land provinces across all 1,081 states
- generated batches expand to the exact canonical ledger with no duplicates or omissions
- runtime counters require issued, observed, state-count, and state-sum agreement
- manual runtime schema 2 binds each scheduled callback to the active transaction generation
- the daily validator binds issued calls to the exact completed-batch cursor before later native work
- each hourly callback repeats the cursor, last-completed-batch, observation, and struck-state preflight before opening the native launch window

Resolution gate:

Review native acceptance for all target classes, one callback per call, guarded callback timing, batch cost, save integrity, and multiplayer synchronization. Hearts of Iron IV was not run in this task.

Vanilla `on_nuke_drop` schedules twelve one-day nuclear news events for every callback. If all 10,154 scripted calls emit callbacks, it may schedule about 121,848 news event attempts. A mod callback cannot suppress that separate vanilla branch. This amplification is part of the release gate.

Forbidden resolution:

- one strike per state
- province modifiers only
- setting fallout variables without actual strikes
- reducing the strike set for performance

## B3: manual scenario id allocation

Status: resolved, SCN-014 reserved and public activation remains blocked by B2

Observed live checkout:

- the registered public scenario sequence reaches raw id 13 with The Unbidden Muster
- the unfinished Black Plague package separately reserves raw id 12
- the gap at raw id 12 does not lower the highest live assignment

Allocation rule:

- inspect every assigned scenario id in the live checkout
- set Fallout to one greater than the highest assigned id
- preserve every existing scenario id and stored selection value
- update registry arrays, sorting, localisation, dispatch, and documentation with the allocated id

`fallout_manual_scenario_identity.triggerable_scenario_id` reserves raw id 14, which is exactly one greater than the live maximum of 13. Raw id 12 remains untouched, no existing id was renumbered, and the public Fallout row remains absent until the exact native sweep passes B2.

## B4: mapmode strip frame ownership

Status: resolved by DDS geometry and decoded-frame comparison

Proven state:

- vanilla uses 18 frames across a 360 by 18 strip
- Chaos Redux uses 19 frames across a 380 by 18 strip
- both layouts produce exact 20 by 18 frames
- frames 1 through 17 retain vanilla pixels
- frame 18 replaces vanilla's transparent slot with Deaths
- frame 19 appends contaminated states
- every Air Winter mapmode uses its dedicated named 20 by 18 sprite

No twentieth strip frame is required. `AIR_WINTER_MAPMODE_ICON_PROOF.md` records the hashes, frame comparison, and official per-mapmode sprite naming contract.

## B5: full-screen GUI drawing order

Status: open, static evidence proves limited pointer interception only

Need proof that the blackout:

- covers all ordinary windows and popups
- has complete pointer priority over every required hardcoded popup
- captures keyboard input and suppresses hardcoded shortcuts
- obtains native exclusive input or another proven equivalent
- remains visible through the rewrite
- works at supported resolutions
- remains synchronized in multiplayer

Current static evidence:

- a non-transparent top-layer blocker can intercept pointer hits on controls beneath its own layer
- the official scripted-GUI schema expects an independent `containerWindowType`, while the current `interface/fallout_world_end.gui` root uses `windowType`
- the current fixed `10000` by `10000` blocker does not prove all-resolution coverage
- root parentlessness places a structurally valid scripted GUI over most UI, but not necessarily every hardcoded popup
- the official scripted-GUI schema exposes no modal, exclusive-input, keyboard-capture, shortcut-suppression, or pause surface
- vanilla native-exclusive examples depend on hardcoded `SetExclusive`, which is not exposed to scripted GUI
- synchronized state can re-evaluate visibility only after the container binding is structurally valid, and no exposed exclusive-input state can be restored
- `is_global_host` is a project simulation coordinator rather than a proven literal lobby host, and it cannot suppress client-local keyboard input

Converting the root to a full-screen independent `containerWindowType` with percentage sizing is only a possible fallback for broader pointer coverage. It requires explicit user approval before any GUI change. It would not prove complete pointer priority, keyboard capture, shortcut suppression, native exclusive input, or pause control. Pointer-only behavior is not approved as a substitute for the required blackout.

Do not assume a top-bar parent, root parentlessness, or pointer interception beneath one layer resolves B5.

## B6: old `world_end_fallout` save migration

Status: schema 11 fail-closed policy implemented, full transition still blocked

Potential old save states:

- terminal flag set with no rewrite
- Fallout super-event visible
- event system stopped
- contamination at terminal threshold

Implemented policy:

- completed Fallout saves are promoted to the current schema without restarting destruction
- completed legacy saves are marked as lacking current-schema and supply-network receipts and receive no fabricated receipts
- an active schema-7, schema-8, schema-9, or schema-10 save may rebuild both snapshot halves only while still in the snapshot phase, before snapshot application or destruction, and without an unrelated error
- an active schema-10 phase 2 save may promote before grading mutation
- an active schema-10 phase 3 through 6 save may promote only before allocation, with current grading, and with exact live-to-frozen network equality for every destructive-grade state
- a promoted schema-10 phase 5 or 6 save rewinds to physical collapse and invalidates derived government and conflict rows
- schema-10 phase 7 or 8 saves and saves with initialized allocation remain blocked
- every other incomplete legacy transition fails closed under blackout
- an incomplete terminal save with no schema also fails closed under blackout
- the former schema-3 map-return-error promotion is removed because consumed rows cannot acquire trustworthy Air Winter receipts after the fact
- migration does not infer safety from a missing `fallout_transition_destructive_started` marker
- no generic pre-destructive restart and no legacy altered-grade replay are active migration behavior

The schema-7 through schema-10 rebuild requires phase 1, no applied snapshot, no destructive-start receipt, and either no error or the exact one-error player or world snapshot signature. The rebuilt schema-11 row freezes the live state category separately from the historical Air Winter category and includes the market-access and province supply-network contracts. Any ambiguity remains blocked.

Completed legacy Fallout saves have no proven reveal date. They are not given a fabricated scheduler timeline or initialization request. A migration policy for those saves must be approved before the living-world scheduler can run for them.

## B7: player continuation and successor commit

Status: commit and proof contracts implemented for ready targets, allocation, materialization, and package production blocked

Implemented commit path:

- human countries, optional source anchors, and every snapshot-origin state are snapshotted
- all player origin states are reserved before the successor conflict inventory is built, while landless humans receive an explicit emergency-materialization row
- derived inventory schema 1 records and validates every live country, possible country scope, state, reservation, safe candidate, and known overlapping event-package owner for the active transition generation
- commit readiness requires an existing target with current-transition country and focus packages, survivable territory, and the exact reserved capital under its ownership and control
- a two-pass preflight validates every existing commit and proposed target before any player switch, including cross-player collision checks
- the durable assignment origin and generation ledger is written before an optional `change_tag_from`
- recoverable commit errors can be retried, and persisted assignments can rebuild cleared reservations before allocation initialization
- committed targets are reconstructed and revalidated against package generations, human control, exact capital reservation, durable origin, durable generation, and assignment uniqueness
- provisional government classifier schema 2 deterministically resolves eleven live archetypes from frozen owner rows and fails closed on partial Machine Protocol claims or unmatched survivors
- successor allocation schema 2 separates the frozen input inventory from post-mutation output proof
- output proof requires reciprocal frozen-source and committed-output links, equal conflict results and cleanup owners, current source and cleanup generations, resolved and non-pending source lifecycle, valid landless retirement, unique assigned country scopes, unique capital states, exact live-landholder coverage, and current package layers
- converted, released, and dynamically created outputs require distinct current-generation provenance receipts. Frozen possible-country membership does not prove that a releasable was released
- every player source must point to the same country in its continuation target and `player_reserved` conflict output
- reservations are immutable after allocation initialization. Later drift records `player_reservation_changed_after_allocation` and cannot rebuild consumed rows
- the guarded allocation finalizer is the only effect that can set the completion flag

Missing release work:

- no active effect materializes a required player successor
- no active producer applies the required country and focus packages or their current transition generations
- no candidate-choice UI assigns a materialized successor to a player
- no active allocator begins or finalizes general successor allocation
- no active allocator chooses a Fallout package, regional package, final archetype package, conflict result, or cleanup owner
- no active allocator writes the conversion, releasable-release, or dynamic-materialization provenance receipts
- no producer populates the post-allocation assignment and package rows
- Machine Protocol lacks complete live producers for its command-network and EMP-survival requirements
- the accepted 99 candidates have stable numeric memory ids, but no exact twelve-country proof roster, state package, capital order, cosmetic identity, or Machine Protocol source identity is approved
- the known event-package ownership registry requires another live producer audit before any state or tag mutation

The reservation barrier no longer requires a missing player destination to exist before the general inventory can be built. The commit effect can still finish an uncommitted player only when the selected target exists and satisfies every current-generation readiness check. The code can set `fallout_player_materialization_required`, but it cannot resolve that state.

Static inspection cannot prove whether `change_tag_from` makes the destination report `is_ai = no` immediately in the same effect chain. The commit effect checks that condition immediately after the switch. No Hearts of Iron IV run was authorized, so this timing remains a runtime blocker.

The blackout and map-return postconditions must remain blocked until materialization, package and focus producers, target selection, general successor allocation, and the tag-switch timing proof exist.

## B8: literal multiplayer host authority

Status: one scripted coordinator is bounded to one Fallout reconciliation per global date, literal lobby-host identity remains unproven

The shared daily pulse removes duplicate `is_global_host` flags. A human can take the coordinator flag only when the current flagged country has become AI. The Fallout reconciler writes `global.fallout_coordinator_last_reconcile_date` before any manual, migration, transition, or request work. Later calls on the same date cannot repeat those transactions. They may repair the persistent coordinator target and invalidate a stale scheduled recipient after a host-flag transfer.

Official trigger and effect documentation exposes no `is_host`, `is_multiplayer`, or `is_local_player` surface. The live flag therefore identifies a deterministic project coordinator on synchronized game state. It is not proof of the actual network lobby host. Literal host authority remains an engine blocker and must not be claimed.

## B9: living-world scheduler activation

Status: schema-2 dormant transaction integrity implemented, gameplay activation blocked

Implemented structural proof:

- successful map return records the current transition generation, exact engine date, and arithmetic engine day
- the existing at-most-once project coordinator owns scheduler reconciliation
- initial registry construction requires a current successor-allocation transaction
- aligned country, generation, and stable-index arrays reject missing, extra, stale, and duplicate rows
- country runtime rows have separate schema receipts for orientation, arcs, delayed queue, and bilateral data
- five independent orientation components gate ordinary events
- per-country fatigue slots are initialized, while the last cooldown family provides the hard immediate-repeat veto
- one generation-bound global allocator issues monotonic arc, delayed-result, and bilateral tickets
- compact aligned rows support idempotent reservation, payload-before-status updates, typed owner and subject cancellation, exact cleanup release, and aligned rollback or removal
- bilateral reservation writes one ticket to two opposite-role rows and proves the exact reciprocal country and initiator cleanup owner before commit
- structural human, hidden AI, and hidden-cleanup envelopes must match their source row and token
- the selected-country consumer copies the complete envelope identity, records engine date and day, writes its issued flag last, and emits the tokenized `chaosx.fallout` country event only after that receipt proves current
- a persisted issued receipt prevents a later coordinator pass from emitting the same ready envelope again. Event acknowledgement requires that exact receipt and clears it with the envelope
- one primary frozen registry country reconciles per date and selects one primary row from each family. A proven bilateral pair may also mutate its exact reciprocal row. Recurring structural and selected-identity reads remain linear in those two local ledgers
- production-only full uniqueness gates are quadratic in each uncapped local ledger. Delayed and bilateral queue caps remain absent
- paired runtime-schema-1 and registry-schema-1 rows promote to schema 2 only while dormant, after the map-return, a fully current committed survival ledger, and all preserved runtime fields pass, and only when every later transaction, ticket, history, cleanup, and envelope surface is absent or empty as required
- a current runtime schema can bind a schema-1 registry only while registry-ready and dormant, with no scheduler error, after the map-return and full survival ledger pass, and after every indexed registry, allocation, and survival row agrees
- successful registry commit clears the initialization request, so later annexation does not rerun the frozen successor-allocation barrier. Lost owners cannot receive new reservations or dispatch envelopes
- no daily global candidate pool, candidate selector, event producer, event definition, or activation setter exists
- the formula-neutral identity transaction stages exact successor and state rows with generation, allocation, region, archetype, country-memory, destructive-phase, and resource-index provenance
- survivor-allocation advancement, player continuation, map return, and scheduler initialization require the committed ledger
- the frozen Fallout snapshot distinguishes a current produced Air Winter value from an explicit N/A row through schema and generation receipts

Missing release work:

- numerical state rows, country aggregation, value validation, row commits, and the global ready setter remain absent because the numerical contract is not accepted
- no candidate selection, event definition, actual human choice content, hidden AI mechanical resolution, content-owned cleanup execution, or scheduler debug presentation exists
- family-fatigue mutation, decay, and scoring remain absent because the accepted specs do not set their magnitudes
- the five orientation receipts have no implemented Fallout orientation event content
- reserved suffixes `100` through `122` have no event definitions and count as zero release-floor blocks
- literal lobby-host authority, schema-2 runtime save-load preservation, and multiplayer behavior remain unproven

Both activation flags remain unset. No ordinary Fallout living-world event can pass its eligibility trigger. Full evidence is recorded in `FALLOUT_EVENT_SCHEDULER_PROOF.md`.

## B10: old-world diplomacy reset

Status: docking rights and market access resolved by documented effects and precedents, four required active surfaces remain blocked

The transaction clears wars, civil-war links, factions, subjects, exiles, guarantees, military access, non-aggression pacts, embargoes, volunteers, collaboration, purchase contracts, and resource rights with documented effects and documented postcondition triggers. It waits while a peace conference is active.

Market access uses the official generic `diplomatic_relation` cancellation contract, the vanilla `market_access_rights` relation identity, the approved Kaiserreich `clear_relations_with_PREV` cancellation precedent, and the official `has_market_access_with` trigger. The coordinator first dismantles factions and subjects, then applies the cancellation across every country pair, records current-generation application and validation receipts, and requires a global absence result. No Hearts of Iron IV run was performed, so this is static engine and precedent proof only.

Docking rights use the same official cancellation contract with the officially enumerated `docking_rights` relation token. Vanilla cancels that exact relation with `active = no` in `events/AAT_Finland.txt` and `events/TAOG_Australia.txt`. The coordinator applies the inverse unconditionally to every ordered pair of live countries and records current-generation application and verification receipts after the loop. No documented trigger can read the relation back, so the proof is exhaustive inverse coverage rather than runtime query evidence.

Resource rights use the official country-scoped `remove_resource_rights` effect and `has_resources_rights` trigger. The coordinator unconditionally sweeps every live country-state pair so even resource-free states receive the inverse, then records current-generation application and validation receipts and requires global absence for every observable grant. Ordinary factory-for-resource imports remain outside this proven route.

Map return still fails closed on these unresolved surfaces:

- expeditionary forces have a documented detector, but no exact return effect was found. Template-based deletion and whole-force fractional transfer cannot isolate the received divisions and restore them to each sender
- active lend lease has an exact official ordered-pair detector, but no documented scripted inverse. The transaction verifies and receipts an empty surface, while any active lease remains blocked
- ordinary resource imports have a creation effect, but no complete scripted enumerator and inverse pair. Resource rights are handled separately and are no longer part of this blocker
- intelligence has partial detectors and destructive operative effects, but no complete agency, upgrade, network, decryption, capture, and static-intel reset

No fallback reset is active for any of these surfaces.

## B11: province supply-network runtime acceptance

Status: schema-11 transaction implemented, static engine route supported, runtime topology proof blocked

Dead-city and higher grades use `set_building_level` with the documented all-provinces selector for `supply_node` and `rail_way`. The state row freezes its immediate aggregate baseline and exact target. Each family retries only the idempotent set-to-zero command until both the aggregate variable and `any_province_building_level` report zero. Grades below dead city settle with an explicit no-op row. The global receipt commits only after every state is current, and the phase advances only after the durable global and state receipts pass.

The installed documentation and close precedents establish the selector grammar and building identities. They do not prove that setting every selected `rail_way` level to zero removes every cross-state railway edge. They also do not guarantee immediate script visibility after the mutation. Hearts of Iron IV was not launched. An unsupported or delayed result therefore leaves the state unsettled under blackout and causes only an idempotent retry. It cannot fabricate the world receipt or advance the transition.

Runtime acceptance remains required for railway topology, supply-node removal, immediate read visibility, save interruption, and multiplayer synchronization. `FALLOUT_SUPPLY_NETWORK_COLLAPSE_PROOF.md` records the exact static basis and test boundary.

## Design decisions already resolved

### D1: normal super-event removal

Resolved:

Fallout uses a dedicated blackout scripted GUI. It does not use a super-event slot, quote, reaction button, or shared global super-event audio id. Dedicated Fallout dramatic audio still plays through Fallout-owned wrappers and honors the super-event audio settings.

### D1A: provincial network damage proof

Resolved for the static state rewrite contract:

State-scoped `remove_building` is accepted for exact permanent loss of infrastructure, civilian factory, military factory, air base, and dockyard levels. Each family stores total levels before and after, and the observed decrease must equal the rounded request. Historical receipt identifiers containing `building_damage` are compatibility names only.

Province supply networks use the separate selector-backed `set_building_level` transaction. Dead-city and higher grades require physical zero for every selected supply node and railway before their row becomes current. The state supply-collapse flag and grade modifier remain gameplay effects, but they no longer stand in for physical network destruction. Runtime railway topology behavior remains B11 rather than an approved simplification.

### D2: treaty disposition

Resolved for implementation planning:

Restore and modernize the treaty because it is part of the accepted design. Live code disabling it is not treated as a design rejection.

### D3: three-layer focus architecture

Resolved:

Archetype, region, and memory are design layers. Implementation can use verified shared focuses or compiled full trees. Every final country is manually reviewed.

### D4: candidate pool size

Resolved:

The 99 matrix rows are candidates. The rewrite selects a coherent subset. No requirement exists to spawn all 99 at once.

### D5: population ownership

Resolved:

All winter and Fallout population loss uses the shared Deaths pipeline. Fallout issues the bounded population mutation first, reads the observed state delta, and submits only that amount to Deaths with population application disabled. The enabled path proves global total movement, one log-sequence step, and matching state-map ledger movement. The user-disabled and zero-loss paths have distinct receipts.

The official engine surface still provides no population-only mutation. Recruitable-manpower neutrality depends on immediate `manpower_k` observation and correction in the shared population helper. Immediate population and building-level read timing is also not documented. No Hearts of Iron IV run was authorized, so both remain runtime acceptance blockers and are not reported as proven.

### D6: periodic loop ownership

Resolved:

Extend the existing host monthly Air state scan. Do not add another global monthly country loop.

### D7: mutant science boundary

Resolved:

Mutant countries are fictional high-chaos content and are never described as real radiation science.

## Decisions required during the pilot

## P1: shared focus or compiled tree

Decision timing:

After two prototype countries use the same archetype.

Choose shared focus composition only when:

- both trees load safely
- layout remains readable
- country memory remains distinct
- no hidden branch leaks
- audit finds no brittle dependency

Otherwise use compiled full trees with shared scripted helpers.

## P2: wasteland ownership

Options to test:

- leave wasteland owned by a regional actor with severe state rules
- assign wasteland to a dedicated non-playable exclusion actor
- keep ownership but remove normal economic value

Decision criteria:

- AI pathing
- front creation
- supply behavior
- diplomacy
- performance
- player readability

The source spec should guide the choice, but engine behavior determines the safe representation.

## P3: player successor selection scope

Options:

- automatic strongest direct successor
- limited candidate list tied to former player territory
- broader regional list when the former territory is entirely terminal

Accepted default:

Use automatic continuation when the old government survives. Use a limited candidate list when it does not.

## P4: treaty membership survival after Fallout

Possible uses:

- treaty memory increases successor legitimacy
- treaty relief infrastructure improves state survival
- former treaty members receive a reconstruction diplomacy route
- violators receive distrust and isolation memory

This is expected content, but exact numerical influence is tuned during implementation.

## P5: ordinary world-end documentation

The root event skill and mechanics guide say world ends normally require Chaos above 1000 and use super-events.

Required documentation decision:

Add Fallout as an explicit system exception without weakening the ordinary rule for other world-end scenarios.

## Not accepted as shortcuts

- replacing state phases with global modifiers
- using the existing contamination mapmode instead of adding winter visibility
- applying only attrition and no population or building effects
- firing generic flavour with no effects
- leaving active successors on the generic focus tree
- applying one universal Fallout focus tree with renamed text
- spawning countries without starting units or AI
- using a normal super-event for the blackout
- skipping the seven-day manual scenario delay
- one thermonuclear strike per state
- calling the feature complete before regional and country audits


## Resolved ownership decision: dedicated Fallout package

Status: fixed design rule

Fallout owns `events/fallout_world_end_events.txt`, the `chaosx.fallout` namespace, its scripted system files, its blackout GUI and GFX, its asset folders, and any accepted audio files.

Delete stale Fallout blocks in other event files. Do not retain compatibility events in an older namespace. Do not reuse another feature's visual or audio assets. Generic systems may call the Fallout entry helper, but ownership transfers at that call boundary.

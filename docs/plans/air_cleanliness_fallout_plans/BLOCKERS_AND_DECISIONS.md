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

Status: dormant map-pinned substrate implemented, strict engine-native and runtime release proof blocked

Accepted requirement:

Every valid province must receive a thermonuclear strike.

Observed evidence:

- official `launch_nuke` accepts a province and explicit thermonuclear type
- vanilla nuclear raids pass a variable-backed province id
- the installed map contains 10,154 valid assigned land provinces across all 1,081 states
- generated batches expand to the exact canonical ledger with no duplicates or omissions
- official collections expose all states but no global all-valid-province enumerator, so the province set is derived offline rather than enumerated by the engine
- runtime counters require issued, observed, state-count, and state-sum agreement
- manual runtime schema 4 binds each scheduled callback and the counted prestrike population baseline ledger to the active transaction generation
- the daily validator binds issued calls to the exact completed-batch cursor before later native work
- each hourly callback repeats the cursor, last-completed-batch, observation, and struck-state preflight before opening the native launch window

Resolution gate:

The strict engine-native enumeration requirement cannot be proven from the documented script surface. Separately review native acceptance for all target classes, one callback per call, guarded callback timing, batch cost, save integrity, and multiplayer synchronization. Hearts of Iron IV was not run in this task.

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

Status: open, static container binding is repaired, runtime input and z-order proof remains open

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
- the root now uses the documented independent `containerWindowType` with percentage sizing and `fullScreen = yes`
- the current fixed `10000` by `10000` blocker still does not prove all-resolution coverage
- root parentlessness places a structurally valid scripted GUI over most UI, but not necessarily every hardcoded popup
- the official scripted-GUI schema exposes no modal, exclusive-input, keyboard-capture, shortcut-suppression, or pause surface
- vanilla native-exclusive examples depend on hardcoded `SetExclusive`, which is not exposed to scripted GUI
- synchronized state can re-evaluate visibility only after the container binding is structurally valid, and no exposed exclusive-input state can be restored
- `is_global_host` is a project simulation coordinator rather than a proven literal lobby host, and it cannot suppress client-local keyboard input

The root has been converted to a full-screen independent `containerWindowType` with percentage sizing. That repair does not prove complete pointer priority, keyboard capture, shortcut suppression, native exclusive input, or pause control. Pointer-only behavior is not approved as a substitute for the required blackout.

Do not assume a top-bar parent, root parentlessness, or pointer interception beneath one layer resolves B5.

## B6: old `world_end_fallout` save migration

Status: schema 12 fail-closed policy implemented, full transition still blocked

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

The schema-7 through schema-11 rebuild requires phase 1, no applied snapshot, no destructive-start receipt, and either no error or the exact one-error player or world snapshot signature. The rebuilt schema-12 row freezes the live state category separately from the historical Air Winter category, freezes specialty survival inputs and coal, and includes the market-access and province supply-network contracts. Any ambiguity remains blocked.

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

Status: dormant numerical and transaction-integrity substrate implemented, gameplay activation blocked

Implemented structural proof:

- successful map return records the current transition generation, exact engine date, and arithmetic engine day
- the existing at-most-once project coordinator owns scheduler reconciliation
- initial registry construction requires a current successor-allocation transaction
- aligned country, generation, and stable-index arrays reject missing, extra, stale, and duplicate rows
- country runtime rows have separate schema receipts for orientation, arcs, delayed queue, bilateral data, and one fixed ordinary opening
- five independent orientation components gate ordinary events
- per-country fatigue slots are initialized, index zero remains fixed at zero, and accepted fatigue decay, issue mutation, scoring, and the hard immediate-repeat veto remain behind the activation gates
- one generation-bound global allocator issues monotonic ordinary-opening, arc, delayed-result, and bilateral tickets
- the ordinary receipt owns at most one crisis opening per country, has distinct human and AI tokens, does not consume a major-arc slot, and commits its pending flag last
- an issued ordinary receipt remains as a blocking tombstone after subject loss. Generic reconciliation cannot clear it or admit a second opening. The exact issued event must consume it or cancel it through the token-authenticated issued wrapper
- an issued delayed row follows the same rule. Public ticket-only terminalizers reject it, and reconciliation retains it until its exact token-authenticated result, cancellation, or cleanup wrapper runs
- an issued bilateral response follows the same rule. Public pair terminalizers reject it, orphan reconciliation retains its local row, and only the exact token-authenticated response wrapper may resolve or cancel the reciprocal pair. If reciprocal proof is already lost, the exact cancellation wrapper may terminalize only its authenticated local orphan
- public bilateral cleanup release rejects an issued local row. Exact issued cleanup removes that row and consumes its matching envelope in one effect chain
- shared cancellation history records the transaction source, so an ordinary retry cannot authenticate a cancellation from another transaction family
- old schema-2 rows promote only an exactly absent ordinary receipt while production remains disabled. Promotion accepts registry schema 1 or 2 only while dormant, walks the numeric frozen-registry index array, and commits only when every matching country context loads and the proven count equals the registry count. The schema-1 binding transaction then writes schema 2, reruns promotion, and requires the full current payload
- compact aligned rows support idempotent reservation, payload-before-status updates, typed owner and subject cancellation, exact cleanup release, and aligned rollback or removal
- bilateral reservation writes one ticket to two opposite-role rows and proves the exact reciprocal country and initiator cleanup owner before commit
- structural human, hidden AI, and hidden-cleanup envelopes must match their ordinary, delayed, or bilateral source transaction and exact token
- the selected-country consumer copies the complete envelope identity, records engine date and day, writes its issued flag last, and emits the tokenized `chaosx.fallout` country event only after that receipt proves current
- a persisted issued receipt prevents a later coordinator pass from emitting the same ready envelope again. The ordinary consume and issued cancellation wrappers release the fixed receipt atomically. Issued delayed and bilateral terminalizer wrappers consume their envelope internally, so no second acknowledgement is valid. No detached acknowledgement API exists. No event block calls the content-facing wrappers in this tranche
- one primary frozen registry country reconciles per date and selects one primary row from each family. A proven bilateral pair may also mutate its exact reciprocal row. Recurring structural and selected-identity reads remain linear in those two local ledgers
- production-only full uniqueness gates are quadratic in each uncapped local ledger. Hard caps are three major arcs, eight delayed rows, and six bilateral rows per participant. Recurring reads remain bounded to the selected local ledgers
- paired runtime-schema-1 and registry-schema-1 rows promote to schema 2 only while dormant, after the map-return, a fully current committed survival ledger, and all preserved runtime fields pass, and only when every later transaction, ticket, history, cleanup, and envelope surface is absent or empty as required
- a current runtime schema can bind a schema-1 registry only while registry-ready and dormant, with no scheduler error, after the map-return and full survival ledger pass, and after every indexed registry, allocation, and survival row agrees
- successful registry commit clears the initialization request, so later annexation does not rerun the frozen successor-allocation barrier. Lost owners cannot receive new reservations or dispatch envelopes
- no daily global candidate pool, reviewed candidate producer, gameplay call to the ordinary reservation API, living-world event definition, content caller, or activation setter exists. The deterministic selector and numerical review lanes remain dormant behind the gates
- the identity-first transaction stages exact successor and state rows with generation, allocation, region, archetype, country-memory, destructive-phase, and resource-index provenance
- a malformed uncommitted identity payload can be reset and restaged only during survivor allocation. The error-owned route requires the sole `survival_ledger_incomplete` signature, current planning and allocation proof, and no committed survival or player-continuation receipt
- the numerical transaction calculates and replays every state and country row from frozen receipts, preserves immutable initial values, and writes the sole global ready flag last
- a malformed uncommitted numerical payload can be cleared and retried only through the complementary exact one-error signature while identity remains current
- survivor-allocation advancement, player continuation, map return, and scheduler initialization require the committed ledger
- the frozen Fallout snapshot distinguishes a current produced Air Winter value from an explicit N/A row through schema and generation receipts

Missing release work:

- survival numerical initialization is implemented under the accepted contract. [FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md](FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md) records the exact transaction and static arithmetic cases. Scheduler activation and ordinary living-world event content remain absent. The dormant Ash-week pilot is tracked in B12
- no reviewed candidate producer, living-world event definition, human-choice caller, hidden AI result caller, content-owned cleanup execution, or scheduler debug presentation exists. The numerical selector and human or AI review lanes are implemented but dormant
- bilateral event content and callers remain absent. Human choices, hidden AI resolution, stale-subject cancellation, delayed results, and content-owned cleanup must invoke the exact wrappers and pass review before activation
- the accepted family-fatigue mutation, decay, scoring, pressure, cadence, queue-cap, and deterministic tie values are implemented behind the unset gates, but no reviewed content producer can consume them
- major-arc and relationship candidates remain fail-closed because reviewed rows do not freeze the complete atomic class reservation and reciprocal payload before dispatch
- the accepted 25-point human-owned war or mission relevance case remains fail-closed because no typed relationship receipt exists
- pair-family memory is recorded only behind the dormant bilateral path and is not yet an atomic reciprocal reservation with deterministic expiry compaction
- active-siege recurrence remains fail-closed because Fallout has no typed current-siege producer receipt
- twenty-three dormant Ash-week orientation pilot, result, closure, and cleanup blocks exist without a caller or complete matrix. They remain uncounted
- reserved suffixes `100` through `126` have no event definitions and count as zero release-floor blocks. They remain typed reservations only
- literal lobby-host authority, schema-2 runtime save-load preservation, and multiplayer behavior remain unproven

Both activation flags remain unset. No ordinary Fallout living-world event can pass its eligibility trigger. Full evidence is recorded in `FALLOUT_EVENT_SCHEDULER_PROOF.md`.

## B10: old-world diplomacy reset

Status: truces, docking rights, market access, and resource rights resolved by documented effects and precedents. Trade and intelligence remain unconditional blockers. Active lend lease and expeditionaries are conditional blockers

The transaction clears wars, civil-war links, truces, factions, subjects, exiles, guarantees, military access, non-aggression pacts, embargoes, volunteers, collaboration, purchase contracts, and resource rights with documented effects. Truces use the vanilla zero-day cancellation pattern after white peace and an exhaustive ordered-pair readback. It waits while a peace conference is active.

Market access uses the official generic `diplomatic_relation` cancellation contract, the vanilla `market_access_rights` relation identity, the approved Kaiserreich `clear_relations_with_PREV` cancellation precedent, and the official `has_market_access_with` trigger. The coordinator first dismantles factions and subjects, then applies the cancellation across every country pair, records current-generation application and validation receipts, and requires a global absence result. No Hearts of Iron IV run was performed, so this is static engine and precedent proof only.

Docking rights use the same official cancellation contract with the officially enumerated `docking_rights` relation token. Vanilla cancels that exact relation with `active = no` in `events/AAT_Finland.txt` and `events/TAOG_Australia.txt`. The coordinator applies the inverse unconditionally to every ordered pair of live countries and records current-generation application and static inverse-completion receipts after the loop. No documented trigger can read the relation back, so the proof is exhaustive inverse coverage rather than runtime query evidence.

Resource rights use the official country-scoped `remove_resource_rights` effect and `has_resources_rights` trigger. The coordinator unconditionally sweeps every live country-state pair so even resource-free states receive the inverse, then records current-generation application and validation receipts and requires global absence for every observable grant. The documented trigger returns false on resource-free states, so exact coverage of that blind subset comes from the unconditional inverse sweep rather than readback. Ordinary factory-for-resource imports remain outside this proven route.

Map return still fails closed on these unresolved surfaces:

- expeditionary forces have a documented detector, but no exact return effect was found. Template-based deletion and whole-force fractional transfer cannot isolate the received divisions and restore them to each sender
- active lend lease has an exact official ordered-pair detector, but no documented scripted inverse. The transaction verifies and receipts an empty surface, while any active lease remains blocked
- ordinary resource imports have a documented aggregate positive-flow detector for each installed resource, but no route enumerator and no inverse. A zero aggregate cannot prove that zero-delivery routes are absent. Resource rights are handled separately and are no longer part of this blocker
- intelligence has partial detectors and narrow release and token-removal effects, but no complete agency, upgrade, network, operation, decryption, static-intel, candidate-pool, and operative-slot reset. Killing or turning operatives creates persistent death or slot-lock state and is not an inverse

No fallback reset is active for any of these surfaces.

The complete readback and inverse audit is recorded in [FALLOUT_DIPLOMACY_AND_INTELLIGENCE_RESET_MATRIX.md](FALLOUT_DIPLOMACY_AND_INTELLIGENCE_RESET_MATRIX.md).

## B11: province supply-network runtime acceptance

Status: schema-12 transition implemented, static engine route supported, runtime topology proof blocked

Dead-city and higher grades use `set_building_level` with the documented all-provinces selector for `supply_node` and `rail_way`. The state row freezes its immediate aggregate baseline and exact target. Each family retries only the idempotent set-to-zero command until both the aggregate variable and `any_province_building_level` report zero. Grades below dead city settle with an explicit no-op row. The global receipt commits only after every state is current, and the phase advances only after the durable global and state receipts pass.

The installed documentation and close precedents establish the selector grammar and building identities. They do not prove that setting every selected `rail_way` level to zero removes every cross-state railway edge. They also do not guarantee immediate script visibility after the mutation. Hearts of Iron IV was not launched. An unsupported or delayed result therefore leaves the state unsettled under blackout and causes only an idempotent retry. It cannot fabricate the world receipt or advance the transition.

Runtime acceptance remains required for railway topology, supply-node removal, immediate read visibility, save interruption, and multiplayer synchronization. `FALLOUT_SUPPLY_NETWORK_COLLAPSE_PROOF.md` records the exact static basis and test boundary.

## B12: Ash-week orientation implementation

Status: accepted design with a partial dormant pilot, caller and release remain blocked

The user approved `FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` on 2026-07-18. Suffixes `62` through `84` are reserved with the accepted visible, hidden AI, result, closure, and cleanup roles. The accepted contract fixes the five-component sequence, 2, 3, 4, 3, and 2 day result delays, deterministic success bands, human and hidden-AI parity, save-recovery identity, missing-registry refusal, six dedicated assets, and non-activation rules.

Current implementation evidence defines all twenty-three reserved blocks in `events/fallout_world_end_events.txt`: national orientation `62` through `65`, capital condition `66` through `69`, immediate resource crisis `70` through `73`, government archetype `74` through `77`, character or institution `78` through `81`, and closure and cleanup `82` through `84`. Their shared and pilot-specific localisation is present, and the six dedicated Fallout report sprites are source-reviewed, converted, and registered. History `9110` supplies 45 payloads through the shared Event Log detail route. These blocks remain dormant, have no caller, and earn no release-floor credit. Exact capital repair, complete coverage, and registry-backed character installation remain undefined.

The approved 108-cell orientation matrix has twelve country-memory cells with dormant resource and government rows. The other 96 cells remain source design only. The capital-repair approval surface, resource package receipt producer, government-row approval setter, character or institution registry and install producer, and complete candidate asset package remain unproven. A caller remains forbidden until successor allocation, player continuation, every regional and archetype row, country memory, main-state target, and curated character or institution registry are proven. `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` remain unset. The living-world count remains 0 of 660 until the complete orientation tranche is wired, logged, detailed, manually reviewed, and audited.

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

Implemented first tranche:

- one monthly host-owned coordinator manages bounded membership, violation, invitation, active-donor, active-inspector, and relief-route ledgers
- Global Cleaning Day is an atomic paid cleanup project
- Joint Filter Convoy is an atomic paid state-targeted Air Winter relief project
- Verification Mission preserves Winter and Fallout tuning formulas while giving three government-weighted responses and an exact seven-day result
- refusal uses the accepted treaty expulsion, embargo, opinion, and relief-loss consequences
- founder succession, annex cleanup, sanctions, inspection cancellation, route expiry, and the silent Fallout pause have explicit receipts

Still required:

- pooled treaty decontamination with approved sponsor, recipient, cancellation, and refund rules
- seed archive exchange with an approved greenhouse and post-Fallout memory contract
- evacuation corridors
- Fallout-era treaty memory and successor legitimacy
- broader manually reviewed treaty event families
- relief votes and policy for major atmospheric burners
- forecast precision beyond shared basic sampling
- runtime observation of target scope, delayed results, sanctions, and route pressure

### D3: three-layer focus architecture

Resolved:

Archetype, region, and memory are design layers. Implementation can use verified shared focuses or compiled full trees. Every final country is manually reviewed.

### D4: candidate pool size

Resolved:

The 99 matrix rows are candidates. The rewrite selects a coherent subset. No requirement exists to spawn all 99 at once.

### D5: population ownership

Resolved:

All winter and Fallout population loss uses the shared Deaths pipeline. Fallout requests 90, 91, 92, 93, 94, or 95 percent loss from the frozen state population according to grade. It protects one person in every nonempty state, issues the bounded population mutation first, reads the observed state delta, and submits only that amount to Deaths with population application disabled. The enabled path proves global total movement, one log-sequence step, and matching state-map ledger movement. The user-disabled and zero-loss paths have distinct receipts.

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

The implemented Joint Filter Convoy already changes live Air Winter exposure, adaptation, shelter, recovery, and survival values. The Fallout snapshot later freezes those ordinary Air Winter values, so a completed route can influence the frozen state indirectly. No treaty-specific Fallout coefficient, successor legitimacy value, or post-Fallout diplomacy rule has been approved or added. Those direct numerical and political effects remain pending.

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

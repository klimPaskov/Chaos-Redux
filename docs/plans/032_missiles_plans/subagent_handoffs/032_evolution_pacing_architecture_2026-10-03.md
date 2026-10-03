# Event 032 evolution pacing architecture, 2026-10-03

## Status and ownership

Disposition: `unresolved` implementation recommendation within accepted Event 032 requirements, with MCP evidence `blocked` as described below.
The parent explicitly described `docs\specs\032_missiles_specs\` as fully accepted and requested this read-only architecture tranche.
That delegation is the acceptance basis for the requirements below, including its stronger requirement that Automatic Retaliation prove all hostile-pair, mature-programme, technology, hardened-command, and chain-bound conditions.
The helper layout, clock implementation, and receipt names proposed here are parent implementation recommendations, not additional accepted gameplay design.
The parent owns implementation, tuning, balance, final review, and completion.
This handoff does not promote any new acceptance or claim Event 032 completion.

Only this handoff was written.
No gameplay, GUI, assets, skills, workbook, or Git state was changed.
The concurrent ordinary preparation transaction was excluded from the audit.
Its APIs are treated only as future pressure-publication boundaries after the parent finishes that tranche.
Skills read in full: `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-subagents`.

Event identity stays `32`, namespace `chaosx.nr32`, entry `.1`, Minor Repeatable, Calm World, and no cluster.
Event 16 retains its host and personal reaction receipts.
Event 23 retains arsenal ownership and nuclear consequences, Event 76 retains weapons-test ownership, and the shared Fallout owner retains terminal consequences.

## Immediate source findings

Line citations describe the byte revisions in the evidence inventory below.
They should be reread after concurrent parent work before patching.

| Finding | Source evidence | Consequence |
| --- | --- | --- |
| No independent evolution wakeup exists | `common\scripted_effects\032_missiles_effects.txt:274` is the only repository call to `missiles_evaluate_evolution_unlocks` found by the call-site search | A campaign can pass an evolution date indefinitely without unlocking until Event 032 fires again. |
| Due dates are deterministic stored arithmetic | `common\scripted_effects\032_missiles_operations_effects.txt:456-549` sets `global.date + missiles_evolution_delay_days` and later compares dates | These dates are deadlines, not actual MTTH or stochastic event probabilities. |
| Event 032 has no MTTH-variable entries or reads | Evaluator at operations effects `551-617` reads constants, with limited multiplication by `0.50`. Full `common\mtth\chaosx_mtth_variables.txt:1-272` contains zombie and Independence Wave entries | The MTTH-backed timing contract is missing. The lengthening multiplier is defined at constants `800` but unused in this scheduler. |
| World pressure is frozen per new firing | Firing effects `238-243` reset six counts, recipient `.5` publishes at `314`, operations effects `27-70` increment them | Launches, maintenance, reserve changes, peace, captures, new payload ownership, and command changes between firings cannot change these counts. |
| Rogue eligibility excludes the accepted single vulnerable programme case | Operations effects `563` uses `minimum_operational_programs`, whose value is `2` at constants `785` | Separate the one-vulnerable-programme eligibility floor from the widespread-pressure acceleration band. |
| Unreliable eligibility does not prove strain | Operations effects `573-578` checks Chaos and guided count, then wartime count for shortening | Guided programmes alone do not establish low readiness, backlog, reserve/capacity imbalance, or actual launch pressure. |
| Saturation does not use a current-pool share | Operations effects `584-590` uses fixed guided and war counts | Two guided programmes can satisfy it even when nearly all programmes are early. A meaningful current share is not represented. |
| Special Warheads counts technology proxies | Operations effects `47-50` calls `missiles_country_has_payload_owner_capability`. Operations triggers `591-603` accepts technology or a support flag | Atomic research alone can count as payload ownership. Physical supported stockpile plus technology must be proven before this eligibility contribution is published. |
| Automatic Retaliation is underguarded | Operations effects `65-68` counts command control and an active site. Evaluator `608-609` checks Chaos 900 and two counted countries | No actual hostile pair, mature/technology capability, surviving hardened command, unreserved response reserve, or `world_end` guard is established there. |
| Local adoption runs before a newly matured global unlock | Firing effects `311-314` evaluates local adoption before global evaluator `274` | A global unlock on that firing can leave every recipient waiting for another firing to receive track access. |
| Adoption conflates access and commitment | Operations effects `138-145` automatically sets saturation doctrine. `173-179` automatically activates a retaliation network | Saturation choice and Off/Supervised/Delegated/Automatic adoption must remain local choices under the accepted requirements. A global unlock must not silently select them. |
| Disabled pending state can survive | Evaluator outer eligibility tests precede each call to the scheduler. The scheduler clears disabled pending flags only when reached | Disabling after pressure or Chaos falls can leave pending state and old dates behind. Disabling needs a direct cleanup path independent of world eligibility. |
| Log commit lacks the shared gate in its mutation limit | Operations effects `384-454` checks raw disabled flags and unlocked flags before mutation, then sets log context | Set context before the mutation guard and include `is_current_evolution_enabled` in that same guard, with full current eligibility. Preserve actorless context and exactly one record. |

The temporary `missiles_evolution_unlock_recorded_this_pulse` flag is set at evaluator entry and after log commits, but does not enforce staggered independent deliveries.
Several due tracks can consequently unlock on one later firing date.
There is no short, staggered first-fire high-Chaos path in the audited scheduler.

Raw country adoption flags are also read by reserve-package code in `032_missiles_effects.txt:541-551` and operations effects `735`.
The parent should make gated consumers use the existing enabled-and-active triggers so suspension does not keep disabled-track package bonuses active.
This observation concerns evolution gating only, not the excluded preparation transaction.

## Accepted track contract

Part 4 defines parallel tracks and actorless stage `1` logs.
Part 6 requires dynamic pressure and named probability scenarios.
Part 8 requires enabled, eligibility, pending, timing, unlock, log, adoption, and cleanup components for every track.
The accepted delegation additionally makes all specified Automatic Retaliation guards mandatory.

| Track | Type / disabled flag suffix | Minimum eligibility | Timing anchor | Local result |
| --- | --- | --- | --- | --- |
| Saturation Arsenals | `missiles_evolution.saturation`, `32_1_1` | Event fired, live programme pool, meaningful guided/stage-2-or-higher share, accepted wartime requirement | `90` days | Global package-rule access and a country adoption opportunity. Do not automatically commit saturation doctrine. |
| Unreliable Guidance | `missiles_evolution.unreliable_guidance`, `32_2_1` | Event fired, Rising Chaos, real global strain | `105` days | Expanded failure/maintenance rules gated by enabled state. This does not force all launches to fail. |
| Special Warheads | `missiles_evolution.special_warheads`, `32_3_1` | Event fired, Totalen Chaos, at least one live eligible programme with supported technology and physical payload stock | `120` days | Country-specific integration access, with separate payment, training, readiness, command, and time requirements. No payload grant. |
| Rogue Launch Commands | `missiles_evolution.rogue_commands`, `32_4_1` | Event fired, Gathering Storm, at least one genuinely vulnerable programme | `120` days | Incident access with local conditions, one ordinary crisis per country, global cap, and cooldown. No incident manufactured by the unlock. |
| Automatic Retaliation | `missiles_evolution.automatic_retaliation`, `32_5_1` | Event fired, Chaos at least `900`, no `world_end`, actual qualifying hostile programme pair, mature/technology/hardened-command and response-resource conditions | `150` days | Posture choice and warning access. No automatic posture selection or strike at unlock. |

Keep the existing `missiles_evolution_<track>_unlocked` identities and unlock dates where they match this contract.
Treat the one-shot unlock marker as the canonical historical record guard rather than introducing two independently mutable success booleans.
Document any retained legacy aliases as compatibility outputs, never as a second authority.
Do not reuse the legacy `missiles_event.evolution_*_stage` values `1-5` as log stages or the legacy tier values `3-7` as current Chaos tier IDs.
All five rows here use stage `1`, and eligibility uses the accepted tier/900 thresholds.

The Part 1 table proposes Chaos gains for evolution unlocks, while the mandatory events skill says evolution state gives zero Chaos.
This tranche should preserve the currently zero-Chaos log/unlock behavior and record the conflict for the parent's existing design reconciliation.
Do not wire the unused unlock-Chaos constants as a side effect of scheduler repair.
This handoff does not resolve or promote that conflicting prose.

## Recommended files and APIs

Keep private orchestration in the Event 032 owner rather than a central router, wrapper skill, or generic shared scheduler.
The existing dynamic helper registry and matching Markdown index were inspected.
Their neutral building, population, economy, threat, and owner-gateway APIs do not provide an existing missile evolution scheduler.
The Independence Wave interval precedent supplies MTTH-variable structure only, not the missing stochastic delivery behavior.

| File | Parent implementation recommendation |
| --- | --- |
| `common\scripted_effects\032_missiles_evolution_effects.txt` and matching `.md` | Own the effects below, their scope contracts, caller-owned outputs, defaults, examples, receipt lifecycle, and shutdown behavior. Extract only current evolution code from operations effects. |
| `common\scripted_triggers\032_missiles_evolution_triggers.txt` and matching `.md` | Five eligibility triggers, country support predicates, pair predicates, and live-witness validation. Existing enabled/active triggers remain the consumer API. |
| `common\mtth\032_missiles_evolution_mtth.txt` | Five entries: `missiles_saturation_evolution_mtth`, `missiles_guidance_evolution_mtth`, `missiles_special_evolution_mtth`, `missiles_rogue_evolution_mtth`, `missiles_retaliation_evolution_mtth`. Keep existing zombie/Independence entries untouched. |
| `common\script_constants\032_missiles_constants.txt` | Preserve the five anchors. Add owner-controlled cadence, bounds, pressure/share bands, and factor tables. Do not select new balance numbers in this handoff. |
| `events\032_missile_crisis.txt` | Proposed hidden triggered-only `.190` global pulse receiver, `.191` local access/adoption refresh receiver, and `.192` reserved for a proven bounded local observation callback if required. No such IDs were found in the searched Event 032 source. Recheck collisions before allocating. |
| `common\scripted_effects\032_missiles_effects.txt` | Publish committed programme/reserve/network changes and request evolution work after the completed frozen firing. Preserve the parent-owned firing/history and Event 16 contracts. |
| `common\scripted_effects\032_missiles_operations_effects.txt` | Replace the duplicated date scheduler/evaluator with owner calls, and publish committed pressure changes at existing operation/site/payload boundaries. Do not redesign preparation. |
| `common\on_actions\032_missiles_on_actions.txt` | Extend only exact war, peace, government, site, inheritance, and removal callbacks whose scope contracts are proven. No daily/weekly/monthly world hook. |
| `common\scripted_effects\chaos_meter_effects.txt` | One bounded owner notification after relevant numeric Chaos crossings, including `900` within Totalen Chaos. A tier-change-only notification misses the 899-to-900 transition. |
| `common\scripted_effects\chaosx_events_log_effects.txt` | A narrow Event 032 notification after its evolution toggle changes. Retain shared row/log ownership and layout. GUI source needs no rewrite. |
| `docs\events\032_missiles.md` and Event 032 helper docs | Record implemented timing semantics, cadence, owner callbacks, suspension, and validation limits after implementation. |

| Effect / trigger | Scope and inputs | Outputs and side effects | Direct call sites |
| --- | --- | --- | --- |
| `missiles_publish_evolution_pressure` | Country THIS is the programme owner. Source kind, source receipt, and programme generation are explicit caller-owned inputs | Idempotently replace that country's cached contribution, update global totals by deltas, repair incident edges, and request work. No grants, log, or launch | Completed `.5` setup, reserve mutations, network changes, resolved maintenance/site projects, integration and payload-owner bridges, removal cleanup |
| `missiles_publish_hostile_programme_pair` | Two validated country pointers, relation source/receipt, programme generations | Upsert one canonical pair row and qualification contribution. No world enumeration | Exact `on_war_relation_added`, initial frozen firing relation seeding, and accepted hostile/tension owner callbacks |
| `missiles_retire_hostile_programme_pair` | Exact pair row and causal relation receipt | Remove its contribution once and retain a closed/tombstone receipt against replay | Peace, annexation, faction/subject changes, loss of programme support, and source withdrawal |
| `missiles_prepare_evolution_context` | Country worker host, caller-initialized temporary track selector and log fields | Fill event `32`, type, stage `1`, required tier, actorless flag. No state mutation | Every track eligibility/commit call |
| `missiles_<track>_evolution_eligible` | Prepared context, committed world ledger, and explicit live witnesses | Boolean under enabled, not-recorded, terminal, and full world prerequisites. No RNG | Track arm, pressure change, pulse, and final unlock commit |
| `missiles_settle_evolution_clocks` | Any proven caller scope, previous ledger revision and date, existing five track clocks | Advance only eligible exposure under each track's PREVIOUS computed MTTH, then store date/revision. No roll | Before replacing pressure, changing enable state, numeric Chaos crossing, worker evaluation |
| `missiles_request_evolution_pulse` | Country caller plus validated persistent scheduler host | Mark work pending and enqueue at most one delivery for the current host epoch. No roll, unlock, or history | Firing commit, pressure publication, toggle, Chaos crossing, exact prerequisite bridges |
| `missiles_run_evolution_pulse` | `.190` receiver ROOT is scheduler host, matching host epoch and delivery date | Consume transport ownership before dispatch, settle/revalidate five tracks, roll only eligible unrecorded tracks, commit successes, and rearm if work remains | `.190` only |
| `missiles_commit_evolution_unlock` | Worker, caller-owned track context, live successful roll receipt | Recheck full eligibility and shared gate, set canonical unlock/date once, write one actorless shared log row, enqueue bounded local refresh | Successful track evaluation only |
| `missiles_refresh_country_evolution_access` | `.191` receiver ROOT is local programme country, unlock revision and programme generation | Set feature access where valid, refresh status, expose adoption choices, and keep voluntary doctrine/posture state separate. No world log or free stockpile | Unlock publication and later local capability changes |
| `missiles_suspend_evolution_track` | Prepared track context after disable or terminal/eligibility loss | Clear track pending work/exposure and disallow behavior. Retain historical unlock and local commitments according to the shared toggle precedent | Toggle notification, pulse guard, and exact invalidation |
| `missiles_rehome_evolution_worker` | Exact removal callback, old host pointer/epoch and validated new host | Move transport ownership without changing track exposure or granting content. Old delivery becomes harmless | `on_annex` and other proven host-removal boundaries |

Helpers are invoked with `= yes` and documented variables/tokens, not invented named scripted-effect argument blocks or `$PARAMETER$` APIs.
Each caller preinitializes temporary outputs it consumes after a helper returns.
Use normal persistent fields for asynchronous work and receipts.

## Dynamic timing and sparse delivery

### Three different meanings

`set_temp_variable = { missiles_evolution_mtth_days = mtth:missiles_rogue_evolution_mtth }` computes a value from the current base/modifiers.
It does not roll a chance, create a deadline, or enqueue an event.
Native automatic `mean_time_to_happen` is a separate engine event-firing mechanism.
A hidden triggered-only delayed receiver has no automatic native MTTH merely because its delay came from `mtth:`.

Recommendation: use the five computed MTTH values as parameters of a declared sparse stochastic pulse process, serviced by one coalesced hidden country event.
This implements dynamic timing and independent track rolls without an automatic event eligibility scan across all tags.
It must be audited as its actual custom process, not reported as an engine automatic-MTTH event.
The mathematical conversion below is a recommendation awaiting the installed-version probability adapter and meaningful numeric validation.
No numerical probability is claimed by this source audit.

The offline Event modding section describes native daily survival as `2^(-1/M)`, so its `M` is median timing under constant eligibility.
For each track maintain dimensionless eligible exposure `h = sum(delta_days / previous_M)` between rolls.
At a pulse, proposed success probability is `p = 1 - 2^(-h)`.
Draw `u` with documented `set_temp_variable_to_random`, then test `u < p` using `check_variable`.
For an unsuccessful roll, consume/reset that exposure and continue accruing subsequent eligible time.
This groups survival over an interval under complete piecewise inputs, but actual deliveries occur at pulse boundaries and are quantized by cadence.
It is not proof of equality to native within-interval firing dates, startup polling, or version-specific engine probability behavior.

Installed math expressions support scoped values and `pow`, and installed variable effects accept math expressions.
Keep `h`, `M`, and probability bounds finite and centralize numeric units such as the base `2`.
Negate the exposure through documented multiplication, not unary negation of a variable token.
Do not round a fractional probability to an integer or put a dynamic variable into an undocumented `random.chance` field.
The documented normalized random-variable draw avoids that parser assumption.
The probability adapter must still verify fractional-power precision and the RNG/comparison resolution for the installed version.

Settle clocks under the old `M` BEFORE publishing new pressure and recomputing `M`.
Otherwise a later high-pressure receipt incorrectly applies its shorter interval to all earlier quiet time.
Eligibility loss suspends clock accrual and rejects unlock while false.
Recommendation for disable is to discard unconsumed track exposure, retain historical unlocks, and require a fresh eligible interval on reenable.
This reset policy is an implementation recommendation to be recorded by the parent, not an additional accepted progression reward.
Already recorded tracks never roll again.

### Worker state machine

1. On a committed triggering boundary, settle affected clocks, update the ledger, prepare each fixed track context, and arm only enabled, eligible, unrecorded tracks.
2. Select/retain a validated scheduler host and its epoch.
3. Mark transport scheduled BEFORE enqueueing `.190` in that host's country scope.
4. Set its delivery date from a bounded review interval derived from current MTTH and parent-owned cadence constants, with a positive floor.
5. Additional requests set work pending but preserve the existing delivery flag/date.
6. On receiver delivery, verify host identity/epoch, scheduled ownership, date, and no active global firing transaction.
7. Consume scheduling and pending markers before helper dispatch, settle clocks, validate exact witnesses, and evaluate the five fixed tracks.
8. Commit at most one log per track and queue local refreshes separately.
9. Rearm only while eligible unrecorded tracks or explicitly retained observation work exists.
10. When no such work remains, stop the receiver chain and clear the scheduler's global pointer at its named shutdown point.

The review date is transport cadence, not a promised unlock date.
A pressure change does not enqueue another receiver while one is already scheduled.
The parent must choose a bounded maximum review latency so increased pressure cannot wait an entire old 150-day interval for reconsideration.
No new balance value is selected here.
An early delivery does no RNG or commit and does not consume a newer scheduled date.
A repeated same-date pulse has zero fresh elapsed exposure and cannot create another log.
The first high-Chaos firing may use the accepted short-delayed path, after baseline completion, with per-track staggered earliest review dates.
It must still pass all track prerequisites and enable gates and must not guarantee five unlocks.
Public news remains tied to Part 4's public-evidence milestones rather than broadcasting every secret unlock on the first review.

### Host ROOT, local ROOT, and rollover

The entry `.1` ROOT stays the initiating host while it walks recipient scopes.
Existing immediate `.5` binds ROOT to each recipient and must remain the programme setup boundary.
Do not use the Event 16 scientist host as a new global scheduler authority or replace its host selection.

Store one global `missiles_evolution_scheduler_host` pointer plus host ID/epoch for the single shared worker.
In a queued `.190`, ROOT is the recipient scheduler host and FROM is the originating event chain context.
The worker reads global track state rather than interpreting ROOT as the payload owner, vulnerable actor, victim, or hostile-pair member.
Likewise `.191` binds local programme ROOT before any helper whose site predicates depend on ROOT.
A scope loop inside `.190` preserves host ROOT, so local country helpers must be dispatched through the country receiver rather than called under that loop with host ROOT.

Do not rely on the cleared `global.missiles_frozen_recipients` array for a delayed worker.
Maintain only durable programme registry pointers and exact source/pair receipts required by this system.
Regular event targets carry into an event fired from that chain, but are not frozen concurrent transaction inputs when aliases can be overwritten.
Persistent scheduler and programme receipts remain authoritative.

On host removal, rehome through the exact callback while the old actor is still identifiable.
Use an existing valid callback actor or a bounded selection from already registered living programmes, not `every_country`.
Increment the global host epoch, preserve track clocks and dates, and schedule a replacement only when its recipient has no undrained old transport receipt.
The former host's country receipt retains the former epoch, so stale delivery can clear only its own marker and cannot clear the living host's queue.
Do not overwrite a country receipt while an old event on that same recipient is undrained.
No arbitrary immutable nonce payload field is documented for `country_event`, so do not invent one or claim that a rewritten country variable identifies every historical event copy.
If no safe host exists, preserve the logical work and repair from the next exact authorized request, recording the blocked delivery rather than spawning a world scan.

## Pressure source ledger and actual hostile pairs

`global.missiles_firing_*` fields remain historical firing receipts.
Do not silently relabel them as live world pressure.
Add a separate committed `global.missiles_evolution_pressure_revision` and totals for valid programmes, stage-2 operational programmes, mature programmes, war participants, reserve, usable capacity, low-readiness/backlog programmes, vulnerable programmes, supported payload owners, and retaliation-capable programmes.

Each registered programme owns its generation, last accepted source receipts, previous numeric reserve/capacity contributions, and flags describing counted membership in boolean categories.
Use flags for boolean contribution state rather than persistent numeric 0/1 meters.
On a change, compare prior counted flags with recomputed eligibility and increment/decrement each global count exactly once.
Numeric reserve/capacity sums use old/new contribution deltas.
Close country removal receipts by subtracting only published contributions once, removing registry membership and incident edges, then clearing that country's fields.
Do not subtract another owner's physical custody or modify preparation payments from this publisher.

The firing pass seeds publication from accepted recipients after their local transaction succeeds.
Use the already authorized frozen transaction and its committed receipt, not a second global enumeration.
Later publishers run at `missiles_add_reserve`, `missiles_remove_reserve`, completed maintenance/readiness work, `missiles_recalculate_network`, site custody/damage/repair, programme technology normalization, payload integration/owning-system changes, and exact succession/removal boundaries.
Publish after a transaction commits, not after every internal intermediate reserve or capacity update.
Source kinds and receipts distinguish firing, project, operation, payload, relation, and removal publications so replay cannot double-count.
Any delayed publication freezes actor pointer/ID, programme generation, kind, and receipt on its owner before enqueueing.

Store hostility separately from programme support.
A relation receipt names canonical country pair A/B, both programme generations, its source kind/receipt, current hostility evidence, and current qualification.
Use one row per unordered pair with a stable ID tie-break to avoid A/B and B/A double counting.
Maintain endpoint adjacency rows so programme changes update only that country's incident edges.
Global hostile-support count changes only when a row transitions into or out of full qualification.

Native `on_war_relation_added` gives ROOT attacker and FROM defender, with installed vanilla precedent.
It establishes an exact pair, not merely two `has_war` countries.
For programmes created during an already active war, seed edges through the current actor's documented `every_enemy_country` at the frozen firing or its first exact registration.
At seed time retain a relation row even if the other endpoint has not yet completed its recipient transaction, then qualify it after both endpoints publish support.
This prevents recipient ordering from losing a genuine existing pair.
No recurring global relation scan is introduced.

Peace, faction/subject invalidation, capture, annexation, loss of codes, site destruction, reserve loss, and payload-owner changes withdraw or recompute the exact affected edges.
An actual accepted hostile/severe-tension owner can publish the same pair API with provenance.
Do not invent a relation-score cutoff or substitute arbitrary countries for that source.
Every unlock attempt revalidates its live pair witnesses with native country existence, current hostile relation, exact programme generation, and support predicates.
Counts alone are insufficient.
If a stale witness fails, retire its contribution and continue only through bounded already-known candidates.
Do not drop real candidate edges to achieve a processing cap. Persist a cursor and continuation work where a large endpoint has more edges than one bounded dispatch can process.

### Automatic Retaliation conjunction

The world gate requires ALL of the following before arming, rolling, and committing:

- Event 032 has actually fired and initialized a valid programme.
- Track V is enabled and unrecorded.
- Numeric Chaos meets `minimum_chaos_retaliation = 900`, including within-tier crossings.
- No `world_end` is active.
- At least two living operational programmes form one actual hostile, wartime, or accepted severe-tension pair.
- The specified mature-programme and installed missile technology requirements are proven at their required endpoints.
- The specified surviving hardened-command, secure-site/custody, readiness, and control conditions are proven through exact programme/site records.
- At least the required responding endpoint has enough unreserved physical reserve and surviving usable capacity for its bounded response and reserve floor.
- Existing causal queue and chain APIs are available with generation `3`, country `6`, linked incident `12`, one country response per root, one warning per country per root, and the accepted missile/payload bounds.

`missiles_program_is_mature` currently means normalized stage at least `missiles_stage.complete` in triggers `116-123`.
The parent's stronger maturity requirement must explicitly name whether that exact predicate applies to both endpoints or a specified responding endpoint.
The brief supplies no alternative numerical stage or hardening threshold to invent here.
Reuse exact installed technology mappings and accepted control/site constants after parent verification, and document endpoint responsibility in the trigger API.
An active site and control `75` alone cannot replace these conditions.
The existing `missiles_all_active_sites_hardened_secure` is an absence-of-insecure-site test, so pair it with a positive surviving-site proof to avoid a vacuous zero-site success.

The evolution worker never launches.
Warning, commitment, and response workers retain exact root lineage, processed-country guards, resource receipts, and bounded closure.
Preserve `.82` warning checks, `.83` delayed launch preparation, and `.89` root closure ownership.
No direct recursive launch calls or Event 032 terminal flag are permitted.

### Observation limits that must remain explicit

An event-driven ledger is exact only for mutations whose owner publishes them.
The inspected installed on-action documentation does not list a generic research-complete or payload-stockpile-change callback.
Passive stability drift, native research completion, and native payload acquisition can therefore change a prerequisite without a current Event 032 publication.
Do not invent `on_research_complete`, manufacture permanent eligibility flags for an analyzer, or describe the last receipt as live omniscient state.

The parent must map actual installed owning callbacks where they exist.
If bounded local observation events are needed for relevant pending programme witnesses, document exactly which actors, native fields, receipt, cadence, stopping condition, and maximum observation lag they cover.
Those callbacks may inspect only their own programme and known edges and may not form a blanket periodic sweep over every registered country disguised as batches.
Do not claim complete mutable-pressure coverage until each accepted native input has a real hook or a specifically justified sparse observation contract.
Until then, native mutation detection is a validation/integration blocker, not permission to simplify the eligibility requirements.

## Enable, suspension, logging, and cleanup

The shared toggle at `chaosx_events_log_effects.txt:2907-2933` changes the dynamic disabled flag and retains historical records.
Use that retention precedent.
On disable before unlock, clear track pending-work state, exposure, and obsolete due-date fields directly, regardless of current Chaos or world pressure.
On disable after unlock, retain its historical unlock/date/log and local choices, but gate all track actions, incidents, AI, reserve bonuses, and warnings by the existing enabled/active triggers.
The existing queued transport may drain once because there is no documented event cancellation API here.
Its scheduled marker is transport ownership, not a disabled evolution pending-job flag.
Reenable must not produce a second log, bypass local eligibility, or create duplicate queued transports.
A pending physical delivery remains tracked even if an immediate refresh consumes all current work.

Before mutation, initialize shared event/type/stage/required-tier context and include `is_current_evolution_enabled` plus full track eligibility in the same commit limit.
At record time use current actual tier, `events_log_evolution_has_actor = 0`, and the shared `record_events_log_evolution_entry`.
Do not clear or trust inherited regular actor targets as the actorless test.
Publish one global row per type with stage `1` and enqueue only local access refreshes afterward.
The logger remains shared. No new GUI, row arrays, or asset package is proposed.

Global state owns track clocks, canonical unlock/date markers, world contribution totals, pair registry, ledger revision, scheduler host/epoch, and next transport review date.
Country state owns programme generation, contribution snapshots and counted flags, source replay guards, adjacent pair references, local adoption choices, adoption revision, and its immutable-for-one-delivery transport epoch/date.
State objects retain existing physical launch-site variables and flags under Event 032 site ownership.
Operation, warning, payload, and chain receipts remain with their existing owners.
The evolution system only reads their committed outputs.

Use a single global event target only for the single scheduler host.
Cleanup points are host rehome, final scheduler shutdown, and terminal suspension, with exact ownership checks before clearing.
Other concurrent pair/incident pointers use persistent country/state scope variables and row receipts.
Use country `exists = yes` only in COUNTRY scopes and native state predicates/record identity in STATE scopes.
Never use `scope_exists` on a variable scope as object authentication or clear all shared global event targets.

## Constants and tuning plan

Preserve existing base anchors in `missiles_evolution_timing` and existing Chaos thresholds in `missiles_evolution_pressure`.
Separate eligibility floors from pressure-band multipliers so one eligible programme can coexist with slower timing than widespread pressure.
Provide per-track factor tables for Chaos, active programme coverage, relevant launches, reserve/capacity pressure, vulnerable count/share, payload-owner scarcity, and qualifying hostile pairs.
The parent selects factor values and meaningful-share thresholds through the accepted balance targets and auditor scenarios.
Use global script constants with fixed-point access, not duplicated cross-file `@` tuning.

Add positive minimum/maximum MTTH bounds, minimum/maximum review intervals, cadence scaling, first-high-Chaos delay/stagger bands, pressure sampling bounds, and probability units.
Review cadence is a performance/quantization parameter, not the unlock MTTH itself.
Do not reuse warning response durations as evolution polling cadence.
No values beyond the existing/spec anchors are chosen by this architect.
Dynamic event duration support has a project precedent but is not explicitly enumerated by the installed `country_event` field documentation.
The parent must validate that narrow field against the connected validator or exact installed precedent before relying on it.
If a literal injection is required, use the existing documented meta pattern and record the field limitation. Do not silently hardcode a replacement delay.

## Migration order for the parent

1. Finish and review the ordinary preparation tranche independently.
2. Preserve immutable before-source files and an identical scenario fixture/hash for the probability audit before editing weighted timing.
3. Allocate collision-free worker IDs and document their exact ROOT/receipt contracts.
4. Implement current-pressure publication and actual pair receipts from the existing frozen firing and exact owners.
5. Add five MTTH entries and five eligibility predicates, retaining type IDs and stage `1`.
6. Replace `missiles_schedule_evolution_track` date branches and the constant-only evaluator with clock/request/pulse/commit APIs.
7. Retire obsolete `*_due_date` fields through an explicit owner cleanup path. Do not reinterpret stored old deadlines as accumulated stochastic exposure.
8. Add numeric Chaos crossing and narrow shared toggle notifications, with no GUI rewrite or world-on-action.
9. Queue local access refreshes so asynchronous global unlocks no longer wait for another global firing.
10. Keep voluntary saturation adoption and posture state separate from global access.
11. Validate exact disable, host-removal, native mutation observation, and causal chain boundaries.
12. Update helper docs and Event 032 docs and obtain the mandatory probability compare and event evidence before any completion claim.

No helper without a direct call site is proposed.
No broad system refactor is needed beyond extracting the existing five-track orchestration into one Event 032 owner.

## Meaningful validation contract

| Matrix ID | Required fixture and evidence |
| --- | --- |
| `EVO-01` | Gathering Storm, eligible vulnerable programme(s), widespread instability. Rogue computed timing must be shorter than its base, with declared pressure receipts. |
| `EVO-02` | Stable world, one secure programme. Report hard ineligibility separately from a longer potential MTTH score. A score is not an observed unlock chance when no vulnerability gate is met. |
| `EVO-03` | Real committed launches, low readiness/backlog. Guidance timing shorter, with each pressure source and its lifecycle present. |
| `EVO-04` | Few launches and high readiness. Longer potential timing or ineligible absent strain. Do not bypass the strain gate to satisfy a score comparison. |
| `EVO-05` | Chaos Tier, many mature programmes, complete valid-programme denominator and accepted war requirement. Near the target `90` anchor under declared modifiers. |
| `EVO-06` | Few early programmes. Longer timing or ineligible. Add equal guided count with different denominator to prove the share rule. |
| `EVO-07` | No physical payload owner, including technology-only countries. No eligible special unlock. |
| `EVO-08` | Several qualifying payload owners, supported technology and actual physical stock. Eligible without granting stock or integration. |
| `EVO-09` | Chaos `899` with otherwise complete retaliation support. Ineligible, no pending job/log/adoption. |
| `EVO-10` | Chaos `900`, no terminal state, exact hostile supported pair, all maturity/technology/hardening/readiness/reserve guards declared at specified endpoints. Eligible only under that full conjunction. |
| `EVO-11` | Each of the five tracks disabled before arming, while queued, after unlock, and after pressure falls. Zero new unlock/record and no gated behavior, while baseline conventional play continues. |
| `EVO-12` | Each track already recorded. No roll, second row, first-unlock bonus, or duplicate local adoption transaction. |

Retain all original EVO IDs and add named subcases rather than replacing them.
For `EVO-10`, test two unrelated wartime countries, missing maturity, missing exact technology, no hardened surviving site, no unreserved reserve, poor readiness/control, same faction/subject-invalid relation, peace during the wait, stale programme generation, and active `world_end`.
Every single missing mandatory conjunct must block.
Sweep both sides of Chaos 900 and other actual source thresholds with the auditor.

Timing fixtures must specify dates, eligibility intervals, pressure changes, previous/new MTTH values, pulse cadence and maximum latency, enable changes, host epochs, RNG/seed conventions, horizon, and first-high-Chaos mode.
They must name five independent processes, not assume a normalized selection pool choosing one evolution.
If the probability service can inspect only computed MTTH scores, label that result score-only and keep survival timing unresolved.
Use a declared custom process/manifest only if its live schema supports all cadence, reset, termination, and scheduled-change inputs.

Task-specific source/event checks should cover:

- Eligibility acquired after the last global firing causes a delayed worker without another Event 032 firing.
- Ten repeated requests produce one transport delivery and do not increase accumulated exposure or roll count at the same date.
- Immediate refresh while a transport is pending does not lose queue ownership or create a second delivery.
- Low pressure to high pressure settles the previous interval under previous timing and changes only later eligible exposure.
- Threshold falls, pressure withdrawal, disable, and reenable cannot release a stale matured deadline.
- Worker host A, local adopter B, and Event 16 host C remain distinct through scope nesting and delivery.
- Host annexation, same-recipient undrained delivery, early delivery, duplicate delivery, and save persistence do not overwrite another epoch or create duplicate unlocks.
- A global unlock after the frozen pass queues local access without repeating programme grants, reports, Event 16 reactions, or pressure contributions.
- Exact hostile-pair insertion, reversed duplicate, peace withdrawal, endpoint loss, and hostile-before-programme seeding change pair count once.
- Chain caps and processed-country guards still apply through `.82`, `.83`, and `.89`, with no immediate recursive strike or Event 032 `world_end` write.

Relevant existing tests are `STATIC-01/02/03/07`, `BASE-05`, `SAT-01/05`, `PAYLOAD-07`, `ROGUE-LIVE-09`, `AUTO-08/09/10/11/13`, and the existing save/reload cases.
They are acceptance scenarios to be retained by the parent, not claims that this architecture audit executed them.

## MCP evidence and exact blockers

The architect's `ALL_TOOLS` registry exposes no `mcp__hoi4_agent_tools__hoi4_*` tools and no general tool-search route.
Thus this architect cannot directly call `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, `event_inspect`, `event_render`, `event_compare`, `probability_inspect`, or `script_validate`.
This is a session exposure gap, not proof that the service is absent or unhealthy.
The local primary-reference reads below are documentation evidence permitted by AGENTS.md, not equivalent MCP event or probability evidence.

The required `chaosx_ai_probability_auditor` was spawned read-only with `fork_context=false`, thread `01a10266-4bff-7a91-934b-a78a10d070bf`.
Its separate catalog exposed probability inspect/evaluate/sweep/compare/render.
It reported that its initial inspect targeted `common/mtth/chaosx_mtth_variables.txt` with adapter `event_mean_time_to_happen`, remained pending for roughly `108` seconds, and produced no result/error/artifact/revision/scenario hash/analysis ID during observation.
The file is a computed MTTH-variable source and contains no Event 032 entry, so that attempted adapter/target is not a confirmed Event 032 timing definition.
Stopping observation does not establish server cancellation, server failure, or successful completion.
Do not retry the same pending operation or claim its result from elapsed time alone.
Exact request/handle details and narrow event/reference/source attempts were requested from that auditor, but were not yet returned when this handoff was written.
The parent subsequently requested immediate source findings and reported its own corrected probability compare/narrow retry in flight.
The auditor was instructed to issue no further calls, retries, waits, or cancellations and to return only already observed details.
No pending operation was declared cancelled or failed.

No connected server version, health, or native-task negotiation is confirmed.
No helper-expansion, job-inspection, job-cancellation, native task, direct HTTP, wrapper, renderer, game, or desktop launch was used by this architect.
No MCP artifact URI or numeric result was obtained.
The parent must retain the route blockers and acquire the required narrow event inspection/render/comparison, source lookup, and probability evidence before implementing claims based on this design.

## Primary-reference and source revisions

Paths below use Windows repository paths relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` unless absolute.
Revision means SHA-256 of bytes read, not an MCP revision or a stable committed Git tree.
The ordinary preparation file was inspected only for the named scheduler/pressure/call-site surfaces.

| Reference | Sections read | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `263-314` event target lifetime, `719-752` math, `887-912` computed MTTH | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | `130-149` automatic MTTH/triggered-only, `180-239` delayed delivery and execution guards | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | `260-269` ROOT/PREV/FROM, `375` and `523` enemy iterators | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | `210-217` political/peace source contracts | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | `571-594` scoped variable comparisons | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | `702-707` variable/RNG arguments | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | `531-540` scope namespaces and pointers | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | `184-245` math and supported constant access | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Same installed `documentation\script_math_functions.md` | Full file, especially `256-267` fractional `pow` | `3c7116906f0bc7590cdd014f5a8b3cf8ef9f0685044fc10e29fabd19afaf832b` |
| Same installed `documentation\effects_documentation.md` | `2733-2749` target clearing, `2943-2963` delayed events, `3897-3915` enemy iterator, `5288-5295` random scope, `6496-6512` event targets, `7828-7857` temp math/RNG, `7888-7907` normal math | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Same installed `documentation\triggers_documentation.md` | `2110-2134` comparisons, `3844-3851` target presence | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Same installed `common\script_constants\documentation.md` | Full file `1-84` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Same installed `common\mtth\mtth_variables.txt` | Full native example `1-14` | `0cd46aff2dc43cb167269064f68741fd03090404b6becc398e32344ceb34b6fd` |
| Same installed `common\on_actions\_documentation.md` | `20-69` relevant exact callbacks, search for research/technology callbacks | `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4` |
| Same installed `common\on_actions\00_on_actions.txt` | `4911-4934` native ROOT/FROM relation and delayed country event | `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9` |
| `common\scripted_effects\006_independence_wave_evolution_effects.txt` | `689-741` computed MTTH interval and cleanup | `321d4e4b041e7af2de554ad276f7f6f971a890220960162eb728a34d33daa7eb` |
| `common\scripted_effects\035_great_depression_effects.txt` | `2136-2148` coalesced delayed receiver | `b9e01de3eb2cc97fa31e73188745af77a1eef28f07d86ac51ac0346385aa28a9` |
| `events\035_great_depression.txt` | `155-169` consume queue before review/rearm | `c8cd58cb01b8d4c5b664113a07f07fb8ae4fadc299dbfc85f5fa0b3c809c8b14` |
| `common\scripted_effects\032_missiles_operations_effects.txt` | `27-181`, `384-617`, `4516-4565` | `d41b59edcfd29b015f566914fddcf88d2bd7469224be635d22b5e2b967c8a8f1` |
| `common\scripted_effects\032_missiles_effects.txt` | `212-318` frozen firing and receiver call path, narrow reserve/network definitions | `fa3d682945bf0d038d2890c62e334f3785e01ab7d2295f545274d74e350f3d19` |
| `common\script_constants\032_missiles_constants.txt` | Evolution timing/pressure, programme gates, chain limits | `77beb588e0b8cedf8e45459f4790a58234b6ea67c5286c5037c0c7396a80ddee` |
| `events\032_missile_crisis.txt` | Full event receivers and warning boundaries | `b088e3245e1ce7858037f3a697045286f83a2e41dbddf69102dd18152a6f23ab` |
| `common\on_actions\032_missiles_on_actions.txt` | Full existing exact lifecycle hooks | `cc33737cfeadab5e742e6c66b0c75fc051ac812269b7fc8ad244663d3b51f3cf` |
| `common\mtth\chaosx_mtth_variables.txt` | Full existing MTTH reference | `463d52c5ab535e89a8d1359338a4533a163051c8e0fdfcadef2942a748645c5b` |
| `common\scripted_triggers\032_missiles_triggers.txt` | Enable/active gates, maturity `116-123`, local posture access | `d09f35f7bd6ea7717cbb497a93ee0872d3cf029510112aabca162b732e8788aa` |
| `common\scripted_triggers\032_missiles_operations_triggers.txt` | Secure site and posture/payload-owner predicates `529-603` | `14b9051c930c9a5ab1f07954fe16cf83eb012f7e3515e775bf314a818418363a` |
| `common\scripted_effects\chaos_meter_effects.txt` | Numeric/tier mutation boundary `4422-4482` | `5ee595ccf76650aadd4d589f6fe78c258224464cb192128e079b795155eb133b` |
| `common\scripted_effects\chaosx_events_log_effects.txt` | Logger `998-1033`, toggle `2907-2933`, selected toggle `4507-4527` | `7fde6b681e3bd62a38eb2c01a22ffab8fc262ad2b0e37e7d0fede43c028d9b81` |
| `common\scripted_triggers\chaosx_settings_triggers.txt` | Shared enabled/tier gate `44-90` | `99ba6329fa9dd0efcc06fb2a1a6452bd0c82ca252a379be78d0cfaacfe2f8f20` |
| `common\scripted_effects\chaosx_dynamic_effects.txt` and `.md` | Owner boundary, registry/API headings, neutral helper review | TXT `f9591fe2beab4ac7570813ba76d1b4dbf63fc9ff10dc3315adfffccab2a895c2`, MD `aba7e66bdc5d81acc27d1b335ea3c23cafb8466c909570b23de3471f42492de6` |

The project warning scheduler at operations effects `4516-4543` calculates remaining delay, queues `.82` once, and rearms when the response date moved later.
The Event 35 pair above supplies a separate coalescing/consume-before-rearm precedent.
These establish source structure only, not verified native execution or arbitrary host-epoch rollover safety.
Installed delayed-event documentation differs from the offline wiki about the upper endpoint of `random_days`, so installed documentation takes precedence and this recommendation does not depend on that random-delay field.
The attempted installed `documentation\on_actions.md` path was absent. The pertinent existing native source is `common\on_actions\_documentation.md` above.
No installed dedicated MTTH semantics document was found by the bounded documentation search, so the native common/mtth example and offline MTTH sections are the cited structure evidence.

Accepted-source byte revisions, all under `docs\specs\032_missiles_specs\`:

- Part 1, read full: `43787b9f33a0d61ec4088a25e4b0777595f66cc9466f7f45183b46690490c659`.
- Part 4, read full: `cb6d46f480315d1e7f584ca65012f09a87e4db0682569cc87248b7c771a85704`.
- Part 6, read full: `5a5667a4d84e261bd16ac54cb2f3b6027798df0a30cd39aa1f2864dce85b5304`.
- Part 8, read full: `db56350822f62bb010019e3821057699101a3a77595ae4ec862580bc8b7b5894`.
- Probability scenario matrix, read full: `3e1d754eb5a3c9d4e0c72c2a7f0a253f38adae560ea2134578aaf76511e4e957`.
- Acceptance criteria, read full across bounded reads: `62db29dc7e33a32c95ac25e2c72d0dfa27792502b86b147d3f0f8892a2130f56`.
- Test matrix, read full: `93111c40abe63554f49ac9544dcddbc284a90ab88b1ac7de2c146b87020c09fb`.

## Completed, blocked, and remaining work

Completed here: narrow source scheduler/call-site audit, accepted-contract mapping, concrete API/file/ownership and migration plan, primary-reference section reads with byte hashes, and routing of the read-only probability evidence pass.
Meaningful source findings were returned before the MCP evidence wait concluded.
Four principal source hashes were checked again before writing and matched their audited revisions.
No simplification or gameplay fallback was implemented.

Blocked or unresolved: connected MCP event/source/reference artifacts in the architect session, probability inspect response and timing adapter coverage, final numeric balance, exact maturity/hardening endpoint mapping, native passive-input observation coverage, and engine delivery/rollover/save behavior.
Skipped meaningful validation: event render/compare, actual probability evaluation/sweep/simulation/compare, native script validation, and all live-game scenarios.
No probability compare is due for this documentation-only audit, but it is mandatory for the parent's later weighted patch using immutable before source and the same EVO scenarios.
No live runtime result is inferred from this source review.
The parent receives an implementation plan, with those evidence limits carried forward, rather than reusable implemented logic or an event completion claim.

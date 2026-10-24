# Shared-system integration contract

This file is an implementation handoff supporting the design. It separates supplied documented APIs, fully read selected repository owners, and proposed shared extensions. The continuation fully read 90 distinct supplied text bodies and 98 distinct selected repository text bodies, including 17 engine-reference bodies, before reconciling these contracts. Repository observations refer to commit `a3ef485c5da7e2337122eca04ac65c175050f251`; they do not assert the latest branch or installed-engine behavior. The exact coverage, version differences, source anchors and unavailable paths are in [source_coverage.md](source_coverage.md) and [repository_evidence.md](repository_evidence.md). This is not engine code or evidence of executed gameplay.

## Observed owners to preserve

| Surface | Existing documented or inspected owner | Required boundary |
| --- | --- | --- |
| Exact state civilian loss | `apply_exact_state_civilian_population_loss` in the dynamic effects owner | Pinned output is planned, clamped and rounded, not measured. The newer required contract preserves the protected floor and returns observed actual decrease with supported manpower correction. No protected-group selector exists in this helper. |
| Current resident custody | Modern Camp Administration admission and `camp_admin_detainees_k` | Detainees are living membership already present in state population. Admission adds custody, not people and not a population debit. |
| In-place release | `camp_admin_release_survivors` and `camp_admin_release_detainees` | Remove living custody membership. Add no physical population. A later movement uses Migration separately. |
| Custody deaths | `camp_admin_record_deaths` | Measures before/after state population, reduces custody by actual loss and records without another debit. Its Deaths-disabled gate prevents the whole transaction at the pin. |
| Deaths record | `chaos_meter_register_deaths` | Records the supplied amount, subject to its settings. It does not measure loss. After an already applied physical debit, use explicit record-only STATE inputs. Country totals and culpability remain distinct. |
| Forced movement | `migration_execute_forced_transfer_exact` | Specialized forced-deportation wrapper delegates the shared transaction; it is not the generic authorization interface for every relief, return or evacuation role. |
| Physical movement | `civilian_transfer_execute_transaction` | Owns preflight, one physical debit/credit, paired reception, cohort binding, finalization and rollback. Current settlement requires a complete living row. |
| Custody evidence | `migration_record_current_state_cohort_custody_exact` and `migration_record_cohort_custody_action_exact` | Evidence receipts only. These calls do not release, move or kill people. |
| Attribution and sanctions | Existing camp responsibility, genocide crisis and `condemnation_add_source` owners | Original authority, hidden/public evidence and cause remain shared. The additive Condemnation entry needs durable caller/owner receipts; it does not generally deduplicate operations itself. |
| Resistance | Native state resistance, Camp accumulation and narrower genocide-crisis support/disruption owners | Use the supported native/shared forms. The broader intake in Part 03 requires explicit shared adapters; no general existing Resistance API was established. |
| World threat | Existing source registry and `refresh_world_threat_state` | Add and clear this event's source only. Never clear the aggregate while another crisis or client remains active. |

The inspected legacy camp percentage path is not a protected-cohort implementation. The new adapter must use the modern exact custody path and establish that legacy and modern maintenance cannot process the same people twice. Selecting a state pool or a responsible government is not selecting a religion or ethnicity.

Exact custody evidence and physical admission are also separate. The inspected cohort custody adapter requires the whole living row and records evidence; it does not call Camp admission. Completing an evidence receipt cannot imply that detention, release or a population transfer happened. The shared bridge must coordinate actual admission with the correct identity allocation and compensate only newly accepted work if a later step fails.

## Proposed shared identity owner

The necessary addition is a provenance-bearing shared living-group identity layer used by Camps, Migration and other relevant civilian owners. It must represent non-overlapping living segments with stable IDs and multiple possible group memberships. An A-only segment of 60, B-only segment of 30 and A-and-B segment of 10 produces an A target union of 70 and an A-or-B union of 100, not 110.

Each segment records origin, current host, living amount, membership provenance and uncertainty, custody or civilian disposition, displacement state, source lineage and accepted physical transactions. Splitting a segment preserves the total, membership and history. Removing or compacting a row preserves alignment across every sparse registry column. Index positions are not durable identities. Cohort IDs are monotonic.

The fully read current aggregate owners do not yet establish these protected-group partitions, partial-row splits or an external-loss composition crosswalk. They remain required shared work. A transfer or custody request that needs less than an existing row must first consume a supported split receipt, then operate on complete resulting rows. Do not relabel aggregate rows as exact subgroups or relax the existing whole-row finalizer to make an unsupported request appear complete.

Initial subgroup data must fit the current campaign date and state population, with a documented source or accepted alternate-history dataset. The unclassified remainder remains unclassified. A national estimate cannot be distributed across game states without an explicit validated authorship method. Exact targeting does not proceed from a government's religion, ideology, flag, tag, core or an invented percentage.

The owner must handle outside population changes. Supported physical-loss and movement producers need a documented way to identify affected segments or apply an explicitly accepted composition model before committing a loss. That model is simulation policy, not a claim of historical individual knowledge. It must conserve the measured total, preserve uncertainty and never fabricate demographic evidence for an achievement or terminal proof.

If an external or legacy aggregate mutation arrives without sufficient composition evidence, quarantine affected exact membership and invalidate the dependent quantitative proof. Do not guess which group died after the fact, refill known cohorts from generic civilians, or silently scale them to hide a mismatch. The implementation is incomplete until all supported production paths that can affect eligible Event 115 cohorts have a coherent reconciliation contract. An unrelated unsupported mod mutation may remain an explicitly diagnosed compatibility failure.

## Conceptual responsibilities

The labels below are responsibilities, not invented callable identifiers.

| Responsibility | Inputs and owner | Result and consumer |
| --- | --- | --- |
| Resolve targeted living union | Shared identity owner, exact state, charter version, group definitions, segment IDs and current authority | Pure valid or invalid proof, eligible segments and living amount. Camp and Migration preflight consume it. |
| Admit targeted custody | Camp owner, frozen eligible selection, requested amount, site, operator and operation identity | Fresh admitted amount and exact membership allocation. No physical population change. |
| Apply targeted custody loss | Camp owner, exact living custody, state, current operator, immutable responsibility, cause and bounded request | Measured physical loss, matching living reduction, one Deaths and attribution receipt. |
| Move threatened survivors | Migration owner, exact origin, destination, route, authority, custody disposition and reception | One physical transfer receipt, survivor lineage, route deaths and symmetric reception. |
| Publish evidence | Existing camp and Condemnation owner, accepted action receipt and discoverability | One hidden or public source, with original responsibility. No extra physical loss. |
| Refresh participants | Event owner, current government, native faction, subject relation, charter, compact and viable authority | Current role and capacity, bounded invalidation of readiness and active actions. |
| Refresh region proof | Event owner, affected states, local authority, supply, industry and shared persecution evidence | Current region witness and persistent tenure, invalidated immediately on material loss. |
| Review terminal candidate | Shared world-end selector plus event's complete current proof | Pure eligible or ineligible result with reason. No world-end side effects. |
| Commit terminal | Shared terminal owner, fresh current proof, settings, Chaos and unique reservation | One permanent terminal receipt before presentation and campaign dispatch. |
| Retire active work | Each owner, exact episode, actor, site or segment, operation and receipt status | Clear only matching transient work while preserving people, history, clients and terminal permanence. |

## Physical invariants

Custody intake changes membership only. In-place release changes surviving custody only. A death reduces the actual state population and exactly the relevant living amount. It does not grant recruitable manpower. A movement debits the actual origin once, credits actual survivors once and treats route deaths as part of that debit.

For movement, require actual origin debit minus route deaths minus actual destination credit to equal zero. For reception, the receiving state and receiving country change by the same accepted survivor delta. Preparation, an open border or a pending reception promise is not evidence of actual arrival. Integration and return-status metadata never create the people a second time.

The caller initializes `state_civilian_population_loss_applied` and `state_civilian_population_loss_result` before every call. At the inspected pin, these outputs describe the planned, clamped and rounded loss; the generic helper does not observe population after mutation, and its logging branch requests physical application through Deaths. Its paired older documentation describes a stronger contract than the implementation provides. Preserve the newer supplied requirement: a fractional protected remaining floor must be respected conservatively, including ceiling that floor before an integral removal bound, and success must report the observed positive loss. Do not weaken the requirement to the older implementation's rounding.

Camp Administration supplies an existing measured wrapper: it snapshots state population, calls the physical helper with logging disabled, measures the actual decrease, reduces living custody by that amount, and records the observed amount using `chaos_deaths_apply_state_pop = 0` and `chaos_deaths_record_state_ledger = 1`. Preserve that ordering and STATE scope, and reconcile exact target membership to the same actual result. No surrounding event wrapper may apply a second debit or register a planned amount as an observed casualty.

The inspected Camp death wrapper rejects the whole transaction while Deaths is disabled. Respect that physical-owner gate; do not borrow Fallout overrides, secretly enable settings or substitute an Event 115 ledger. An already applied authorized loss cannot be reversed by a recording toggle, and reenabling logging cannot replay it. Changing the Camp setting to govern only recording would require an explicit shared-owner design change and its own migration and validation.

The Deaths registrar accepts a rounded caller amount, not a population measurement. It resets only its target-country, has-target-country and record-state-ledger inputs. Each invocation must initialize amount, reason, civilian classification, physical-apply mode and all attribution inputs explicitly. An old caller's temporary amount, reason or apply flag cannot leak into a later record-only call. The existing shared conversion can request Chaos without the global meter accepting it; Part 08 requires actual applied political deltas and never treats the Deaths conversion counter as proof of a meter change.

If destination credit or reception accounting cannot complete after a debit, the transaction is not a clean rejection merely because a boolean says false. The owner must prove rollback of this exact invocation or retain an acknowledged recoverable state with its unresolved accounting. No success, achievement, population load or repeat debit is published until the transaction actually settles.

The inspected transfer finalizer requires the full requested origin amount, zero unresolved residual, correct role and cohort binding, and completed paired reception. A primitive's success flag is insufficient. The distinct all-death finalization path records its actual result but cannot establish a successful rescue. A mission may report partial overall progress only from its separately finalized whole tranches; a half-settled row remains unresolved. Route-death registration follows completed physical settlement in record-only mode. The current corridor evacuation path requests zero route deaths, and its cleanup can clear local survivor/proof fields; durable transaction history must support later achievements or audits.

### National loss, responsibility and evidence

`chaos_deaths_target_country` selects the country whose Deaths totals and history receive the amount. It does not identify the offender for Condemnation. Freeze any supported national/victim attribution separately from actual operator, original responsible government, issuing government, payer, current owner and controller. The inspected Camp caller passes its original responsible country into that totals field; implementation must resolve the intended shared national-loss policy explicitly, without silently turning the registrar into a culpability API or inferring personal nationality from residence.

The camp/genocide evidence chain retains responsibility and discoverability. `condemnation_add_source` is additive, so the accepted action and a later discovery each need the appropriate durable shared receipt. A completed physical transfer with pending evidence remains physically completed. Repair the evidence binding and record only the missing accepted evidence; never retry the physical operation to repair attribution.

### Transfer, reception and cost dependencies

The full owner read identifies concrete integration gates. A migration-related death adapter does not initialize the exact-loss helper's required minimum-remaining input itself; each supported caller must supply and verify that contract. Current shelter/medical proof setters compare the proof above the constant one while their producer publishes one accepted token. Reconcile that shared contract; do not manufacture a proof value of two. A forced-transfer Condemnation wrapper does not itself save its required actor target and marks its transaction after the downstream call without checking acceptance. Bind the intended actor at the actual upstream boundary and require an accepted evidence result before consuming the evidence receipt.

The newer named paid-reception and cost adapter paths listed as unavailable in the evidence record remain implementation dependencies. The fully read Universal Cost framework establishes quoting, component payment and receipts, not an atomic transaction for every action. Preflight all components, preserve the actual payer and paid amounts, then settle or compensate that invocation. A refund uses the actual payment receipt, not a newly calculated price. Interface cost text, an approved quote or an expired mission is not proof that resources were charged or returned.

### Famine and Resistance boundaries

The inspected direct Camp-to-Famine callback validates and registers food pressure through the Famine owner. It does not replay Camp deaths, move survivors or immediately execute a second mortality debit. Later scheduled famine mortality is a separate accepted cause, subject to its own physical-loss and identity reconciliation. Do not call a direct-death famine adapter for a Camp loss already applied. A date alone is insufficient deduplication when distinct accepted actions can occur on the same date.

Native `has_resistance`/`add_resistance`, Camp's accumulation and the narrower genocide-crisis support/disruption hooks provide concrete integration points. They do not prove the complete broad intake described in Part 03. Document and implement the required shared adapters and their accepted-action receipts; do not invent an event-private resistance strength, automatically spawn an army or infer a successful aid delivery from a political promise.

## Authority and scope

Freeze actor, payer, actual operator, original responsible authority, target state, optional destination, exact living segments, charter version, episode and operation before nested work. Entering country scope does not change ROOT. A founder event cannot charge the founder for a client's independent action or attribute every client's acts to the original event recipient.

Trace the actual callback conventions from the current sources. The supplied event guide documents the annex winner and annexed country, and the new controller, old controller and changed state scopes. Do not infer those positions from a helper's name. Prove a state pointer is a state, not merely an existing country or variable.

The read engine reference gives `on_state_control_changed` as ROOT=new controller, FROM=old controller and FROM.FROM=changed state. Its puppet/liberation peace hooks do not cover every scripted release, autonomy change, government replacement or civil-war path. Those paths need their own verified lifecycle adapters. Country ownership and actual control are separate, and native diplomatic faction membership may include automatically enrolled subjects without their charter consent.

A queued country event can survive a tag's absence until that country exists again, and a literal country-tag scope may resolve through a dynamic offshoot under the documented engine rules. Validate actor incarnation, episode/operation identity, charter version and present authority when work resumes. The new or restored country cannot inherit stale persecution permission, payment ownership, final assent or completed-operation credit merely because a tag string matches.

Preflight is read-only. It does not mark a row consumed, publish success or settle a refund. Clear the fresh consumption output immediately before mutation. An already used or tombstoned row is not a fresh receipt and cannot be rolled back as the current invocation's work. Caller-owned temporary scalar and array outputs are initialized before each helper boundary. Temporary variables do not receive unsupported scope prefixes.

Use documented parameterless helper calls and supported inputs. Do not invent parameter macros, scope-bearing argument syntax or undocumented field names from a conceptual table. Every new helper needs its real direct call sites and a companion contract covering scope, units, defaults, outputs, side effects, receipt lifetime and cleanup.

The selected native references were fully read, but installed-version behavior still needs validation. Use supported temporary-variable initialization; do not invent a `clear_temp_variable` effect. Selection, completion and cancellation are separate native lifecycle points: a focus completion reward runs before the focus is marked completed, direct mission activation can bypass normal eligibility, and scripted decision removal can omit `remove_effect`. Durable operation receipts must govern payment and cleanup across all of those routes. Parts 04, 05, 06 and 11 define the accompanying force, focus, decision and technology requirements.

## Liberation and continuity

Control loss invalidates the defeated authority's pending local orders immediately. The new authority inherits current physical administration where native control gives it that power, while earlier responsibility remains with the original operator and documented issuing authority.

An open administered site or live custody requires the shared closure or release receipt before cleanup. A closed site with live or malformed custody is an error to resolve, not an empty site. Facility-only work needs its own infrastructure proof. Event flags cannot substitute for actual site and custody conditions.

Founder defeat changes compact leadership and removes invalid founder capacity. It does not clear clients' countries, armies, wars, doctrine, persecution, equipment, live cohorts, history or independent obligations. The active event remains until all sustaining governments meet the defeat or dormancy definitions. A departed adherent without a current compact is excluded from that compact's terminal capacity while remaining an active opponent in the wider crisis.

## Scheduling and saves

Use bounded registered participants, affected states, live sites, living cohorts and pending operations. Existing shared monthly owners keep their cadence. Event lifecycle hooks mark affected records dirty and coalesce reviews. Do not introduce an unscoped daily, weekly or monthly scan of all countries or states.

Native daily, weekly and monthly country hooks fan out per country. Bound event work to its registered actors and dirty records within that fan-out. Iterator ceilings are not proof of complete processing; preserve the unvisited suffix, and avoid mutating the iterated array in a way that skips or repeats entries. Validate a required registry is complete and nonempty before an `all` predicate can prove universal readiness. Date encodings and elapsed-day counters have different units: establish the actual shared time owner, constants and conversion before implementing due dates or tenure; the missing named date-constant path is not permission to invent arithmetic.

A state-owned due date survives a control change. Duplicate callbacks do not create extra elapsed time. Persistent records distinguish pending work from an already queued worker. Processing near the native iteration ceiling preserves the unvisited suffix and all unacknowledged receipts. Unresolved rows must not cause the rest of the queue to be cleared or permanently starved.

Save and load initialization is versioned and idempotent. It can create missing containers or rearm recorded pending work. It cannot reseed living people, reset tenure, refill custody, repeat aid, restore a defeated country, alter a branch toggle or refire the opening. Schema migration preserves accounting and historical identity. Legacy aggregate rows remain aggregate until supported group provenance exists.

## Terminal suppression boundary

Both ordinary automatic event producers and final dispatchers respect the permanent terminal latch. A normal event queued before the commitment rechecks at dispatch and cancels without consuming an unfired fire-once record or creating a false history entry. Inventory ordinary pool, cluster, delayed and repair routes so none restart the timer later.

This is required shared integration. The fully read pinned daily producer already checks `events_activated` and `NOT world_end`, while the delayed cluster queue and its dispatcher lack a generic permanent stop. The settings owner can clear `world_end`, and `world_end_scenario_triggered` is an empty effect. No existing serialized terminal reservation or immutable cessation service is established by those names. Commit a durable shared terminal receipt and make each ordinary automatic producer and dispatch boundary consume it, including the prepared Event 013 route that can bypass the usual no-cluster dispatcher.

Before clearing a pending queue, record cancelled outcomes for its unexecuted history rows, finalize affected batches correctly and release their owned reservations. The inspected cleanup releases Acid Rain reservation state and clears 17 aligned arrays plus queue context, but clearing alone does not perform every cancellation/history obligation. A cancelled row must not become a fired event or silently disappear from batch accounting. Already scheduled callbacks must become harmless on re-entry. Save initialization, settings restoration, event activation toggles and terminal victory or defeat cannot clear the durable cessation receipt or restart ordinary firing.

Continuing war, country politics, independent clients, camp maintenance, physical civilian transactions, Deaths, Migration, Resistance, Condemnation, liberation, protection, successor and ending-specific workers remain authorized. A blanket world-end early return in those owners is incorrect. Manual requests follow the shared framework's rules and cannot use this event to overwrite an already committed ending.

The terminal commit rechecks strict Chaos greater than 1000, both settings, current readiness and no competing owner, then acquires and publishes the monotonic terminal state without an intervening wait. If the shared engine path cannot make that sequence indivisible, use its documented guarded reservation and exact recovery receipt. Presentation and war setup consume the one committed result. Defeat of the order never clears the latch.

The pinned ordinary Chaos owner can overshoot from below 1000, then rejects ordinary increases and reversals at or above 1000. Thus 995+10 can qualify at 1005, while 999+1 reaches an ineligible 1000. Preserve strict `>1000` and the existing global meter policy. Do not add a hidden point, borrow the Scientist exception or promise every campaign can reach this ending. Part 08 governs actual-delta receipts, rejected changes and frozen outstanding reversals.

## Required dependency completion

This continuation fully read the selected Camp, civilian transfer, reception, cost, Condemnation, Famine, terminal, settings, catalog and cross-event owners and the 17 selected offline engine references. The accompanying portable manifests record exact bodies, hashes and complete intervals. Do not repeat the earlier claim that these pinned bodies received only a bounded excerpt review. That coverage is also not a whole-repository audit: unavailable newer adapters, unlocated universal identifier/terminal/time contracts, unselected conditional production references and installed assets remain outside it.

Before any separately authorized implementation, read the current definitions and consumer documentation needed for the exact changed surfaces, using both offline wiki and installed-game references for engine-facing behavior. Use a supported MCP check only when it answers a concrete implementation or review question, and follow the current retry limits. Do not impose a general service-health/version poll, structural render, probability analysis, save/reload, viewer, or live-game gate on unrelated work. When a useful route is unavailable or inconclusive, continue with source review and local checks and state that limitation without claiming MCP or engine proof. The user owns live-game validation; no implementation should be left waiting for it.

The shared identity extension, migration crosswalk, country and map manifests, exact target dataset, additive founder-tree integration, source-verified native transfers and terminal capability model are explicit deliverables. They are not optional stubs. A planning package can specify them honestly while leaving their implementation and engine validation outstanding.

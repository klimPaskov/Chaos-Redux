# Event 101: Implementation contract

This is the imported source-design companion to the seven idea-led specification parts. It defines ownership, proposed file boundaries, measurement contracts and implementation dependencies. Apply [current authority and workflow](README.md#current-authority-and-workflow) before a future implementation task. The names below are working implementation labels. They are not final localisation, existing repository APIs or proof of installed engine support.

## Canonical ownership

Event 101 owns task selection, frozen task terms, task progress, task settlement and task-specific achievement facts. The shared random-event system owns scheduling, repeatable weight recovery, dispatch, event history, settings and evolution registration. Existing military, diplomatic, construction and crisis systems own their actual world changes.

Use the canonical root `chaosx.nr101.1` in the selected human country's event scope. One committed shared firing chooses one eligible human country. In multiplayer, different countries may hold different tasks from separate firings. Each country has at most one active task. Co-op seats are deduplicated into one country entry.

The shared scheduler has player-country timers. An Event 101 preflight must therefore reserve and revalidate the selected recipient before assignment and history commit. Two scheduler callbacks cannot assign two tasks to the same country. The country on whose timer the draw originated is not automatically the selected recipient. Pass the selected actor through the existing dispatcher and logging contract explicitly.

Event 101 remains Minor Repeatable, Chaos level 1, with no cluster. Its direct assignment and outcome Chaos delta is zero. Preserve shared repeatable weight recovery of 20 per month and halving of the recovered weight cap after each committed firing. Do not add an Event 101 MTTH scheduler or recharge loop.

## Proposed source boundaries

These are proposed destinations for a future implementation checkout. Inspect current ownership and naming before creating them.

| Proposed destination | Responsibility |
| --- | --- |
| `events/101_tasks.txt` | Canonical root, informational assignment and result reports, bounded hidden observer events where needed |
| `common/scripted_effects/101_tasks_effects.txt` | Event-owned preparation, commitment, observation, resolution, repair and achievement fact publication |
| `common/scripted_triggers/101_tasks_triggers.txt` | Human eligibility, read-only readiness and cheap committed-record predicates |
| `common/decisions/101_tasks_missions.txt` | One non-selectable mission, automatic completion and guarded terminal callbacks |
| `common/decisions/categories/101_tasks_categories.txt` | One ordinary category and its static picture |
| `common/dynamic_modifiers/101_tasks_modifiers.txt` | Verified task benefit and setback consumers, if the selected native implementation uses dynamic modifiers |
| `interface/101_tasks.gfx` | Parent-owned sprite definitions for the accepted task assets |
| `localisation/english/_chaosx_events_l_english.yml` | Event-owned text in the current source convention, with other shared owner files changed only through their documented contracts |
| `docs/events/101_tasks.md` | Canonical permanent event document, with subordinate subsystem files only when justified by the current owner guidance |
| `docs/plans/101_tasks_plans/` | Bounded implementation plans, specialist handoffs and review disposition |
| `docs/specs/101_tasks_specs/` | Imported source-design baseline with its historical acceptance record |

Shared edits must be narrow. Register Event 101 in the actual repeatable arrays, event-type lookup, readiness and dispatch preflight, accepted reworked enable list, event details, history and evolution tables. The inspected seams include `chaosx_logic_effects.txt`, `chaosx_settings_effects.txt` and `chaosx_settings_triggers.txt`. They are shared owner files, not places to put the task engine.

The catalog workbook is the editable authority. The 10 October import evidence records Event 101 as Tasks, Unavailable, with blank Type, Chaos and cluster fields, and no current `chaosx.nr101.*` definitions. Minor Repeatable and level 1 are planned design values. A future implementation reconciles the workbook under the current event status contract and exports CSV. Importing the specification does not upgrade availability or enablement. Do not edit a CSV export as the source of truth.

## Exact weighted hierarchy

Use the four-stage hierarchy from Part 2. These are mathematical definitions, not native script syntax or measured engine output. After hard eligibility and deterministic history filtering, let each target's base quality be `q` and its qualifying evolution factor be `e`. For each archetype, compute `E_archetype = sum(q × e) / sum(q)`. For each family, compute `E_family = sum(E_archetype) / eligible_archetype_count`.

The final family weight is its country-context base times its history factor times `E_family`. The archetype weight is `100 × E_archetype`. The target weight is `q × e`. This preserves equal base archetype shares and applies pressure or Chaos boosts only to the qualifying target mass. It does not add tickets for raw target count.

Country selection remains uniform and separate. If commitment fails, redraw uniformly from untried prepared countries, without replacement and with one attempt per country. Preserve the exact history-relaxation order and multiplicative target-quality rule from Part 2. The probability specialist must inspect all four levels together and must not analyze the boosted family weight without its matching conditional archetype and target weights.

## Record model

Use a recipient-country record with the following fields or equivalent supported storage. Boolean state should use flags where appropriate. Persistent numbers and pointers belong to the owning record. Temporary arithmetic is not persistent evidence.

| Group | Required information |
| --- | --- |
| Identity | Schema version, exact country object, original tag for display, monotonically advanced task generation |
| Lifecycle | Pending, active, resolving or terminal phase, transaction lock, setup receipt, consumed receipt and outcome-issued receipt |
| Provenance | Natural or forced assignment, responsible shared firing, achievement eligibility and disqualifiers |
| Content | Family, archetype, selected variant, evolution snapshot and quote grade |
| Targets | Exact country and state pointers, separate map state numbers, protected original capital or province where relevant, route anchors |
| Baselines | Physical and usable construction baselines, production counter baseline, qualified force or relation baseline, accepted ownership and authority |
| Work | Required quantity and unit, permitted methods, useful partial threshold, mandatory anchors, contribution requirements |
| Time | Assignment time, original deadline, original duration, hold start, hold duration, earliest verified completion and next review date |
| Owner | Adapter version, exact owner system, owner epoch, stage, role, subscription and outcome identity |
| Outcome | Frozen reward and penalty, confidence floor, expected owner effects, actual applied result and completion time |
| Retention | Recent three signatures, terminal tombstone, rest or reentry date, compact achievement facts and unexpired outcome components |

An original country and a new country reusing its tag are different actors. Cosmetic tag changes preserve the original record. Ordinary country scope entry does not rebind event `ROOT`. Helpers must enter and validate the explicit task actor instead of relying on a convenient ancestral scope.

STATE pointers are not map state numbers. The inspected offline STATE `id` getter is an internal object identifier, so it cannot generate a history-map state ID. Do not test a variable pointer with `scope_exists` as proof that its country or state remains valid. Use the installed scope's actual identity and existence predicates, then validate the expected owner and controller as COUNTRY objects. A shared state needs actor-keyed task mirrors if mirrors are required.

Private record generations and owner epochs must be exact integers. Validate numeric range and precision against the installed scripting representation. Do not invent a universal variable maximum, round a fractional generation into validity or wrap a counter onto a live or retained identity.

## Helper contracts

The following names are semantic APIs to implement. HOI4 scripted-effect callers set documented inputs and invoke a real declared helper. This table is not invented named-argument engine syntax.

| Working helper | Caller scope and inputs | Outputs and authorized writes |
| --- | --- | --- |
| `tasks_country_can_receive` | Explicit COUNTRY actor, current authority, active state and reentry date | Read-only eligibility and reason |
| `tasks_prepare_selection` | Shared firing context, bounded eligible human-country set | Selected country, family, archetype, target and complete candidate quote, no committed history |
| `tasks_build_candidate_quote` | Actor, one archetype, live capability evidence and bounded targets | Validity, exact terms, quantities, duration, methods and outcome quote |
| `tasks_commit_assignment` | Actor, expected idle generation and freshly revalidated quote | Fresh assignment receipt, persistent record, subscription, active registry entry and mission activation |
| `tasks_observe_current_work` | Actor and exact active generation, due sampler or scoped owner evidence | Current evidence, hold state and earliest provable completion, no outcome payment |
| `tasks_objective_ready` | Actor and committed record | Cheap read-only result for the native mission predicate |
| `tasks_sync_native_timeout` | Actor, active native mission and stored deadline | Idempotent signed timer correction or guarded expiry resolution |
| `tasks_resolve_current` | Actor, current generation and validated evidence | Fresh consume receipt, exactly one terminal outcome and its history |
| `tasks_close_external` | Actor, current generation and exact closure cause | Neutral closure, tombstone and reentry date, no ordinary reward or failure |
| `tasks_cleanup_record` | Actor and closing generation | Removal of only matching mission, subscription, pointers, scratch and active membership |
| `tasks_restore_runtime` | Saved actor record and schema version | Presentation, subscription and timer repair without invented work, new deadlines or repeated awards |
| `tasks_refresh_outcome_effects` | Actor and bounded unexpired component records | One positive and one negative native aggregate with each earned expiry preserved |

Every helper declaration needs units, defaults, required inputs, caller-owned outputs, permitted writes, call sites and reentrancy rules. Keep event-specific helpers in the Event 101 owner. Add a helper to a shared registry only when it is genuinely neutral and has cross-system callers.

### Caller-owned scratch

Before every call, the immediate caller preallocates every scalar and array output it will consume after return. This also applies when a wrapper forwards a nested output. Reset validity and fresh receipts to false or zero, and clear output arrays before each independent operation.

Temporary variables are unscoped. Do not address them through `ROOT`, `PREV` or a country prefix. Nested callbacks can overwrite temporary scratch and ordinary event targets. Freeze the transaction actor, generation, selected pointers and outer cursor in private recipient-owned normal fields before dispatching a nested chain.

A per-country lock prevents same-country reentrant assignment or settlement. A stale or rejected call must clear its private transaction inputs without clearing another invocation's live actor. Preserve the documented public outputs long enough for the immediate caller to consume them.

## Assignment and terminal lifecycle

| Transition | Conditions | Result |
| --- | --- | --- |
| Idle to pending | Human actor eligible, one real candidate and expected idle generation | Reserve actor and prepare the exact subscription and terms |
| Pending to active | Final eligibility and setup succeeded | Publish immutable terms, register actor, activate and synchronize mission, then report assignment |
| Pending to invalid setup | Target or owner changed before a complete commitment | Clear setup, no ordinary task penalty, no successful firing history |
| Active to resolving | Fresh valid terminal evidence for the current generation | Consume active authority before any external effect or mission removal |
| Resolving to terminal | Outcome-issued receipt set, exact effect path invoked once | Record actual outcome and rest or reentry rule, then clean matching transient state |
| Active to neutral closure | Exact external invalidity or loss of all human control | No ordinary reward, failure or rest, preserve original-deadline reentry and consumed signature |

Assignment reports only acknowledge the existing record. The mission starts at commitment. Clicking the report is not a payment, acceptance choice, extension, reward claim or prerequisite for progress.

Use one resolver for completion, timeout, strict-loss failure, owner results, human-control loss and repair. Revalidate setup and authority inside the resolver even if the mission's earlier availability check succeeded.

Set resolving and the exact consumed receipt before removing the mission, dispatching an owner callback, applying a reward or penalty, writing achievements, logging or showing a report. Only a fresh consumption result authorizes those actions.

Set an exact-generation outcome-issued receipt before entering the effect path. This prevents duplicate issue, but does not establish database transactions or native rollback. If a native chain partially applies, record a diagnostic failure and reconcile it. Do not replay raw grants because an acknowledgement is missing. Delayed owner effect consumers must be idempotent for the same receipt.

A native mission callback has no proven automatic Event 101 generation payload. Treat it as a signal to inspect the current record. An old timeout cannot fail a new task whose deadline is not due. An old completion callback cannot pay a new task whose predicate is false. Owner callbacks must carry the subscription's frozen actor, task generation, owner epoch, target and result identity.

## Time, holds and native mission synchronization

Use a monotonic elapsed-day clock such as the inspected `global.num_days` after verifying its installed semantics. Encoded `global.date` is not elapsed days. Calendar formatting can use an existing shared display helper, but deadline arithmetic must remain in one documented unit.

Proof timestamped at or before the stored deadline is timely. Later work is late. At a terminal check, validate authority, ingest eligible timely evidence, apply irreversible prior strict-loss disqualifiers, then test full success, declared partial success and the remaining failure or exact external closure.

A fresh sample at the deadline can prove a currently observable condition. A sample after the deadline cannot backdate production, control or construction. If an owner can deliver a success callback after timeout, it must provide a synchronous deadline query or verified closure ordering. A settled failure is not reopened by a late receipt.

Consecutive holds store a start time and reset when the condition stops being true. Strict protection stores an irreversible hostile-loss fact. Callback count is not elapsed time. Daily snapshots cannot prove never losing a state between samples.

The supplied event guidance describes state-control callbacks with the new controller in `ROOT`, prior controller in `FROM` and changed state in `FROM.FROM`. Inspect the current source chain and installed precedent before adding an observer. Notify only affected registered actors. Province-level protection needs province-level proof, otherwise that specific variant stays unavailable.

Use one explicitly activated working mission, `tasks_active_mission`, with a substantive cheap `available` condition. In the inspected decision documentation, omitted mission availability defaults true, which can immediately complete a mission. Mission visibility is not controlled by ordinary decision `visible`. Category lifecycle and actual active receipts must govern presentation.

Immediately after activation, and after a valid load or runtime repair:

1. Enter the exact actor and confirm both an active record and an actual native mission.
2. Compute remaining days as stored deadline minus current elapsed day.
3. If due, call the guarded deadline resolver.
4. Otherwise compute signed delta as remaining days minus native remaining timeout.
5. Apply the supported signed adjustment and verify that another synchronization converges to zero.

The current supplied decision skill documents `days_mission_timeout@tasks_active_mission` and `add_days_mission_timeout = { mission = tasks_active_mission days = var:timeout_delta }`. Verify the installed schema and scope before shipping. This adjustment may shorten or extend a repaired native display to the stored deadline. It does not authorize player-purchased time or a changed task deadline.

Do not remove and recreate the mission for ordinary progress. On closure, inspect and remove an actual leftover native mission even when the private active flag is stale. Guard cleanup against a newer generation using the same mission ID.

## Measurement and attribution

| Task proof | Supported design meaning | Required implementation boundary |
| --- | --- | --- |
| State capture | Own attributable acquisition and current control of frozen targets | Control and contribution callbacks, exact actor and target identity |
| Province or capital protection | No forbidden hostile loss throughout the committed interval | Exact position and loss history, no daily-only approximation |
| Corridor | Required anchors and complete practical connection work together | Verified route and usability adapter, state-center distance is insufficient |
| Newly qualified forces | New appropriately trained and equipped usable strength | Baseline, actual formation provenance or equivalent exact proof, retained readiness |
| Equipment production | Cumulative production delta in one exact category | Verify overlapping counter families, units and production scope, do not substitute stockpile |
| Industrial outcome | New usable capacity in exact original states and building types | Physical baseline and current usable levels, lawful grants explicitly allowed |
| Recipient-funded construction | Every credited level funded and commissioned by the recipient | Dedicated construction receipts, national total plus local delta is insufficient |
| Diplomatic action | Actual lawful action and sustained useful relationship | Post-assignment action proof, native permissions and real partner identity |
| Aid | Useful support actually delivered | Deduplicated actor, partner, type, amount, delivery time and return handling |
| Crisis response | Recipient's accepted contribution in an actual owner episode | Versioned owner receipt, stage, epoch, hard deadline and exact result |

For industrial expansion, credit `max(0, U_now - L0)` in each frozen state and type, with current physical-level validation. `L0` is the physical baseline and `U_now` is currently usable undamaged capacity. Baseline repairs alone cannot count as new work. Where damage exists, include required baseline restoration in the effort estimate or select the separately declared repair variant.

Ordinary industrial completion is an outcome test. An external lawful grant after assignment can satisfy it. The separate construction achievement requires receipts for the recipient's own funding. A national construction counter plus a target-state increase cannot prove that those national builds occurred in the target.

The offline equipment-production categories can overlap. A broad infantry counter must not be labelled as rifles alone without exact support. Production is different from stockpile growth, captured equipment and equipped formations. A preparation subtype that cannot prove its promised unit or origin must remain disabled with a recorded coverage gap.

Use existing verified rate history or a documented conservative estimate. One counter read cannot establish a historical production rate. Do not create a continuous all-country history service for Tasks.

## Crisis adapter boundary

Every admitted owner provides a versioned contract with actor and role validation, exact episode and stage, unmet opportunity, achievable work, permitted routes, timing, contribution proof, terminal query or receipt, cancellation causes and retention policy.

The owner retains physical consequences, payments, population, territory, combat, autonomy, rewards and Chaos. Event 101 applies only the distinct prequoted incremental task result. A side-effect ledger must demonstrate that the two systems do not debit or reward the same result twice.

The shared local crisis limit remains three. A task observing an already-counted episode does not claim a duplicate crisis slot. Task feasibility still accounts for the country's combined active burdens.

Named adapter gaps are implementation work, not removed requirements. Fuel Crisis 114 and IMRO 115 need real owner contracts. Inflation 100 has a namespace mismatch in the inspected repository. Event 006's DM-10 inflation consequence is a separate possible owner. Occupation Revolt 095 needs persistent episode and outcome evidence. Partition work attaches only after a committed settlement. Catalog Warlords 127 concerns subject autonomy, while the armed-warlord subtype owned by Event 014 Cannibalism is a different possible owner. The 10 October parent check finds no `chaosx.nr127.*` definitions and does not alias that subtype to Event 127.

## Neutral closure and identity changes

| Cause | Treatment |
| --- | --- |
| All human seats leave the country | Neutral close, no ordinary penalty, original-deadline reentry, streak disqualifier where specified |
| Another human remains in co-op | Continue same country record |
| Cosmetic country rename or tag appearance | Preserve identity, terms and proof |
| New country object reuses a former tag | Reject inheritance and close stale record |
| External settlement removes every declared route | Check timely earned success, otherwise neutral close |
| Owner episode is replaced | Accept only documented continuity, otherwise neutral close |
| Recipient voluntarily destroys, cancels or transfers a required result | Apply the declared ordinary failure or continue to deadline under that task's rule |
| Ordinary military defeat or loss of the target | Apply strict-loss or ordinary task rule, no free neutral reroll |
| Saved record lacks a provable baseline or authority | Invalid-record closure and explicit repair evidence, never invented successful work |

Native signals do not prove a player's intent. A disconnect and deliberate control switch may be indistinguishable. The neutral human-loss policy therefore uses a country reentry quarantine through at least the original deadline. It does not invent account identity, accuse a player or retain an AI task.

Previously earned rewards and already-applied penalties retain their legitimate expiries when an unrelated active task closes. Human-control loss removes the active contract's mission and subscription. It does not erase the country's earlier settled history.

## Bounded maintenance and migration

Keep a persistent registry of exact active human-country records and generations. Use scoped callbacks and due per-actor observers. A duplicate wakeup cannot advance holds twice, create another scheduled delivery or bypass the next review time. Separate pending work from a scheduled delivery flag when immediate work can consume the pending state.

UI predicates read committed local evidence. They do not enumerate the world, run pathfinding, rebuild candidate pools or write progress. Assignment may inspect bounded relevant targets once. Document explicit scan and candidate caps after measuring actual engine behavior.

When cleanup or recovery exceeds the native 1,000-iteration limit, process a tuned batch and preserve the unvisited suffix and all unacknowledged receipts. Never clear an array and rebuild only visited entries. A large synthetic registry test must show that every retained row eventually receives service.

Outcome effects use a small private collection of earned components, each with its own receipt, statistic, sign, grade, magnitude and expiry. Expose only one principal capability per sign. The most recent live positive award selects the positive capability. The highest-grade live negative award selects the negative capability, with the newest receipt breaking equal-grade ties. Within the selected capability, apply the strongest live same-sign value. Suppressed or weaker components may resume only inside their own original expiry. Combining an old magnitude with a newer expiry is forbidden. Follow Part 6's useful-window quote gate and keep immediate grants separate.

Settled-effect maintenance has its own due receipt, independent of the active-task registry. Schedule the next per-actor refresh at the earliest unexpired component boundary, then recompute and schedule the next boundary only if a component remains. Preserve this due work when the active task closes or human control is lost. It maintains already-earned effects and cannot issue a new task, reward, penalty or achievement. Validate the original country identity on every refresh and retire stale replacement-country records. Load repair restores this small due set without enumerating the world. Duplicate expiry wakeups are idempotent.

The normal minimum 30-day post-result rest and 180-day maximum benefit duration bound unexpired positive result records to at most seven at an inclusive boundary. Use capacity eight for this private list. The 90-day penalty maximum similarly needs at most four records. Purge expired records before insertion. If corrupted or forced data exceed a bound, preserve still-earned records, block another award and report the diagnostic. Never discard an unpaid or live receipt to make space.

Migration preserves original deadlines, generations, terminal receipts, provenance, rest and reentry dates, and achievement facts. Rebuild presentation from trusted saved terms. Do not infer a missing baseline from the current world, renew time after reload, recreate a paid reward or transfer progress to a replacement actor.

## Implementation acceptance boundary

No gameplay file, native mission, localisation, asset, achievement registry entry or catalog workbook has been implemented by this planning task. Repository and offline documentation evidence narrows the contracts, but does not prove engine execution.

The implementation must address the task-specific checks in [the validation companion](101_tasks_validation_and_evidence.md), use the bounded specialist routes in [the usage maps](101_tasks_usage_maps.md), and preserve content accepted for that task. A missing exact proof adapter is an explicit incomplete subtype or family. An unavailable optional check is a verification limit under README's current workflow. Neither case authorizes replacing a requested real action with a looser hidden predicate and claiming full completion.

# Event 096: implementation architecture and native gates

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

This is a behavioral handoff with concrete source touchpoints.
Names for new helpers and files are proposals pending the repository collision and schema checks.
It is not pasteable Clausewitz code and does not claim a working native implementation.

## 1. Existing integration that must survive

The archive's inspected repository revision is `a3ef485c5da7e2337122eca04ac65c175050f251`.
At that historical revision, `events/096_divisions_lock.txt` uses `chaosx.nr96.1`, locks every country, sets `division_template_lock_event_active`, opens `.2`, and schedules `.3` after ninety days.
The `.3` option then clears the country lock unconditionally.
That fixed callback and unconditional release are the principal replacement points.
R01 supplies the historical source.
The current parent source/MCP review confirms the same root and blind ninety-day release at source revision `79a28526ecf259f67d13bbd7b69a90887eae2fa0cee937242d3b8df226d371b7`; see [the current import evidence](../../plans/096_divisions_lock_plans/096_import_evidence_2026-10-08.json).
Current source exists independently of whether the proposed redesign has been accepted or implemented.

Preserve `chaosx.nr96.1` as the canonical entry.
Keep the shared Event 019 compatibility marker exactly while Event 096 holds a country.
A watch is not an Event 096 hold.
Existing Event 019 transaction-start, completion, and mutation-boundary protections continue to use the marker and must not be bypassed to implement random removal.

The parent integration owner retains shared event registration, fired-handler order, cluster registration, Event Details, global logs, evolution registry, shared achievement registry, and catalog alignment.
Feature workers receive bounded files and consumers.
They must not independently rewrite those shared systems.

## 2. Native lock ownership

Use an idempotent shared owner-hold coordinator, rather than an incrementing reference count.
Each owner publishes whether its country-wide hold is active.
The effective native lock is the logical OR of all integrated owner holds.

| Existing owner or dependency | Inspected source | Required integration |
| --- | --- | --- |
| Event 096 | `events/096_divisions_lock.txt` | Acquire and release its own hold, preserve its public marker |
| Standard zombie recruitment | `common/scripted_effects/002_zombie_outbreak_effects.txt` | Publish its independent country hold and preserve its special recruitment settings |
| Rat army profile | `common/scripted_effects/020_black_plague_rat_effects.txt` | Preserve country and individual-template restrictions |
| Weaponized zombie profile | `common/scripted_effects/zombie_special_project_effects.txt` | Publish hold without rerunning destructive template-pruning setup |
| Event 049 Doomsday path | `common/decisions/049_mass_panic_decisions.txt` | Preserve its own hold lifecycle |
| Historical Event 089 Doomsday path | `common/decisions/089_tech_sharing_group.txt`, absent in the current checkout | Retain as archive evidence only. Re-resolve the actual current owner if applicable; this path does not establish Doctor Wu ownership |
| Event 014 Cannibalism, current parent finding | `common/scripted_effects/014_cannibalism_effects.txt`, lines 5367, 13796, 19437 and 21746 | Include every corresponding owner lifecycle in the coordinator audit; this caller was omitted from the historical table |
| Event 019 management | `common/scripted_triggers/019_infantry_spawn_triggers.txt` and `019_infantry_spawn_ledger_triggers.txt` | Preserve Event 096 barriers and provider-owned unit records |

Before changing the native boolean, inventory all actual callers in the supported installed mod and vanilla combination.
The table combines the archive's targeted research with the explicitly labelled current parent Cannibalism finding.
The parent evidence records executing lock writes at zombie effects line 1933, rat effects line 1185, weaponized-zombie effects line 2717, Doomsday decisions line 375 and Event 096 lines 34 and 71.
Event 096 line 53 is inside `effect_tooltip` and displays a preview only; it is not another executing lock write.
The parent reference evidence confirms that distinction through installed effect documentation lines 3644–3652, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline Effects line 355, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
It is not a claim that every possible external mod has been examined.
A deployment containing another owner needs its explicit compatible lifecycle or a proven native ownership mechanism.

No native owner stack or lock-state getter was established by the available reference.
Do not invent a prior-lock snapshot from a guessed getter.
Registering only Event 096 and assuming every other hold is absent is unsafe.
Conversely, preserving an opaque forever-lock for every special country would silently change gameplay.

On compliant release, clear Event 096's hold and marker, then recompute the OR.
Set native no only if no integrated owner remains.
Never clear individual template locks, force-allow recruitment flags, division caps, owner AI strategies, or provider ledgers as part of that release.
Reassert the native boolean directly.
Do not call a complete owner setup effect that can prune units or templates.

## 3. One country refresh and action model

| Proposed helper | Contract |
| --- | --- |
| `division_inspection_calculate_force` | Country-scoped, reads documented aggregate and typed counts, produces caller-initialized temporary quarter-point force, no mutation |
| `division_inspection_calculate_allowance` | Country-scoped, reads controlled-state access, population, infrastructure, verified factory accounting, and regime, produces complete temporary allowance |
| `division_inspection_refresh` | Publishes one complete F/A snapshot and live status, then evaluates the current lifecycle |
| `division_inspection_can_release` | Pure check of the authoritative minimum floor and current quarter-point F/A |
| `division_inspection_release_own_hold` | Requires a fresh release proof, clears own hold, updates coordinator and watch or closure state |
| `division_inspection_open_request` | Freezes actor, authority, context, action, and bound without choosing a unit |
| `division_inspection_commit_request` | Revalidates, consumes receipt, selects and removes exact eligible formations one at a time, refreshes after each |
| `division_inspection_review_watch` | Consumes one current credit before deciding pass or reacquisition |
| `division_template_lock_refresh` | Neutral shared coordinator, writes only effective country-wide native lock from explicit owners |

Event-specific helpers belong in proposed `common/scripted_effects/096_divisions_lock_effects.txt` and `common/scripted_triggers/096_divisions_lock_triggers.txt`.
The reusable lock coordinator belongs in a neutral shared file with every real caller documented.
Central tuning belongs in an event-owned constants file using the actual installed schema and required first-field convention.

Temporary outputs must be initialized by the caller at every helper boundary, including nested helper chains.
Durable inspection history and request receipts use normal country variables or proven equivalent storage.
Do not rely on a temporary variable first created deep inside a helper surviving its return.

Within a global iterator, ROOT remains the original root.
Pass or establish the inspected country explicitly.
Before dereferencing a stored country pointer, prove the actual country exists in the expected context.
`scope_exists` alone is not proof that a variable pointer names a valid actor.

## 4. Time and callback ownership

Use integer `global.num_days` for ordinary due-day bookkeeping, AI scheduling, review intervals, and accounting windows.
The reference documents its units.
The supplied source documentation mentions shared date converters, but those converters were absent from the current fetched helper code and helper registry.
Do not call them as though they already exist.

The minimum must last seven elapsed game days.
Prefer an event-owned timed country flag of seven days as its authoritative active-floor marker, provided the installed schema and native test prove that setting it again renews its expiry correctly.
Keep a corresponding due-day record for display and scheduler hints.
A legacy or duplicate callback cannot mature the floor while the current timed flag remains active.

Test a midday firing and a same-day later repeat.
Counting seven midnight boundaries alone is not proof of seven elapsed days.
If the native timed-flag renewal cannot meet that contract, use an exactly verified elapsed-time representation.
Any encoded `global.date` arithmetic must use the documented conversion, where one day is 0.00024, rather than adding raw day integers.
Implement and document a neutral converter before using it if that route is selected.

Maintain at most one logical country refresh chain.
Its callbacks are wakeups that reevaluate current state, not stored authorization to unlock or disband.
A repeat updates current state and due records instead of creating another chain.
A callback whose due condition is not current performs no state change and cannot clear a newer pending-work marker.

Use a last-processed due receipt to prevent duplicate work on the same logical boundary.
An old callback may harmlessly wake the evaluator, but only the current floor, hold, watch, grant, and consumed-credit state can authorize a transition.
Do not claim a generation variable guards a delayed event unless the event actually carries an immutable reference to that generation.

Retire the old `.3` blind release.
Both queued legacy callbacks and already opened legacy release options must route through current guarded evaluation.
Player acknowledgement is informational, never the release authority.
Save compatibility must test the old popup case explicitly.

## 5. Refresh cadence and bounded work

The global firing pass is authorized by the event's worldwide scope.
Ongoing work is country-local while its hold, watch, or unresolved request needs it.
Do not add a fresh unfiltered global `on_daily` loop.

Use relevant ownership and state-control callbacks to request prompt refreshes, with a country-local reconciliation at least daily for active holds.
The snapshot documents `on_state_control_changed` as ROOT new controller, FROM old controller, and FROM.FROM the state, and `on_annex` as ROOT winner and FROM loser.
Apply the actual verified scopes, not guessed alternatives.

Population and industry can change without a convenient unique hook, so the local reconciliation remains necessary.
Closed countries stop ordinary Event 096 refresh work.
Finite achievement observations and request retirement are separate bounded jobs, not reasons to keep the global evolution director active forever.

Use aggregate battalion reads where their boundaries pass, rather than scanning all units daily.
State aggregation is read-only and publishes only after completion.
If an installed map or country footprint exceeds a safe iteration bound, process bounded chunks with an explicit cursor and preserve the unvisited suffix.
No individual scripted loop exceeds the project limit of one thousand.
A partial state sum must never authorize release or disband.

Frame-driven category predicates read complete published snapshots and cheap current guards.
Do not put state, formation, or world aggregation into ordinary visibility and availability blocks.
Request a bounded refresh and withhold stale availability where needed.
Recalculate fully at request opening and again at commit.
Profile the category held open while local refresh runs, so the UI cannot accidentally multiply background work.

The acceptance target is a fresh complete active-country result within one game day, with immediate recertification after an Event 096 removal.
Large-map profiling must prove that batching meets that target.
Do not hide a performance failure by treating missing states as zero capacity or returning an old partial result as live.

## 6. Persistent records

| Record family | Required information and lifetime |
| --- | --- |
| Local inspection | Active hold, current firing grant, episode identity, regime revision, authoritative floor state, F/A snapshot, next logical refresh |
| Evolved watch | Start and due day, spent and remaining credits, once-only review receipts |
| Shared lock owner | Event 096 hold plus all independent integrated owners, idempotent lifecycle |
| Request | Exact actor and authority, immutable request serial and context, action and bound, terminal or invalidated state |
| AI posture | Retain or pending bounded attempt, F/A baselines, T/G/O and pool-state baselines, legal action day |
| Attribution | Manifestation and relapse receipts, per-country relapse-counted status, family Chaos window and spent budget, repeat retirement |
| Achievement history | Exact qualifying grant and actor, entry snapshots, observations, transaction receipts, review outcomes, repeat retirement, and durable award state required by Part 6 |

Global director records identify the active cohort and registered completion states.
They are not a second copy of every country's entire army.
Repeated firings preserve historical receipts needed for anti-farm and achievements while replacing operational grants under Part 4.

When a country disappears, clear active jobs and invalidate requests without claiming successful compliance.
A successor receives only the deliberately transferred inspection obligation and is freshly measured.
Parts 1 and 4 govern held and watched transfers, original due dates, consumed credits, and maximum-based mergers.
Part 5 carries relapse-counted status through verified split and merge transactions.
Part 6 prevents unfinished achievements crossing grants or actors.
No successor inherits the previous player's pending destructive authorization.

Identify each supported originating political or provider transaction and verify its callback scopes.
Obtain all continuing-branch force snapshots before publishing the transfer.
Store an idempotent transfer receipt, retaining unresolved work without awarding attribution or restoration.
Do not claim a generic native succession callback exists.
An incomplete transfer adapter is a named G3 compatibility gate.

## 7. Legacy saves and settings

An old active Event 096 flag without the new schema needs an explicit migration.
On the project's verified version or load migration route, register its own hold, compute current F and A, start a fresh seven-day floor, and replace the legacy ninety-day behavior with the new evaluator.
Inform the player that the active incident has been reassessed.
No unit is removed by migration.

Do not rely on `on_startup` as a save-load migration hook.
The reference says it does not run on loading a save.
Identify the project's actual version-check route or provide a verified explicit migration entry.

Migrate the other native owners through proven existing markers and exact owner contracts.
If ownership cannot be reconstructed for a supported save, report that compatibility gate rather than guessing an unlock.
New-game support and migrated-save support are separate acceptance rows.

Future-event disable, evolution disable, and explicit clear-active-effects have the distinct behavior defined in Parts 1 and 4.
Cleanup preserves other native owners, does not refund unexecuted actions, and does not grant achievements or restoration Chaos for an administrative clear.

## 8. Three native implementation gates

| Gate | Required proof | Forbidden substitute |
| --- | --- | --- |
| G1: measurement and capacity accounting | Fielded-only structural counters, support inclusion, zero-human coverage, damage invariance, owner attribution, factory and offsite semantics, safe population scaling | Division icons, human manpower alone, Boolean per-division presence, incomplete support coverage, available-factory convenience |
| G2: exact voluntary demobilization | Current eligible owner pool, combat and provider preconditions, one exact administrative removal, actual returns including variants, retained native lock, safe receipt and authority lifecycle | Broad template deletion, empty `delete_unit`, fabricated refund syntax, temporary country unlock, stale popup consent |
| G3: ownership and lifecycle | All integrated lock owners, special recruitment exceptions, Event 019 compatibility, native timed-floor renewal, repeat and legacy callback safety, migration and settings behavior | Blind native no, fake prior-state getter, duplicate callback chains, guessed save-load behavior |

These gates are not resolved by the arithmetic and architecture work in this package.
A complete implementation must attach their evidence before claiming this event satisfies the specification.

## 9. Implementation order and final documentation

First establish G1 and G2 with small controlled fixtures and inspect every current native lock caller.
Implement and verify the coordinator before enabling a release path.
Then implement the core country lifecycle and migration, the two decisions and receipts, evolved watches, AI policy, and bounded Chaos accounting.
Add presentation, achievement tracking, and final assets against the established consumers.

Use the separate prompts for bounded work, then integrate through the parent.
Update event documentation, Event Details, global logs, evolution metadata, and Peace High membership together.
The authoritative catalog is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
CSV files are read-only exports and must be regenerated by the required project exporter after an authorized workbook update.

Apply the current [catalog status contract](../../../.claude/skills/chaos-redux-events/SKILL.md#event-catalog-status-contract).
The current parent workbook read confirms To Be Reworked and no Peace membership for Event 096; Peace High membership remains the target.
Do not mark Playable without explicit user approval.
Preserve the final source revisions, comparison artifacts, named fixture results, and outstanding limitations in the implementation handoff.

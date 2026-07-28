# Event 006 and Soviet Collapse coupling completion re-audit - 2026-07-29

## Scope and snapshot

This is a read-only completion re-audit of Event 006 and its direct Soviet Collapse release-transaction coupling.

Random Events Mod, Fallout, CBB, CBD, and every unrelated dirty-worktree surface are explicitly excluded.

The requested baseline commits are `0fb3b6a35`, `80bc9130e`, and `9199b465b`.

The audit was completed against current HEAD `44888d17c`, which also contains the later scoped Event 006 commits `7b2c39975`, `5716b2818`, `f4b521767`, `1696bb940`, and `44888d17c`.

No gameplay, localisation, workbook, CSV, asset, focus, decision, event, Soviet Collapse, or shared release source was edited by this audit.

## Parent closure addendum (2026-07-29)

After this audit, the parent repaired the two narrow source defects and the catalog mirror identified below. Requester-loss payload `6006` now records the lost requester (`FROM.id`) as the Event Log actor and selects `independence_wave.history.crisis.title` through the shared title resolver. `Events!C7` was updated from the workbook source of truth with the rendered crisis consequences, and `.tools/export_event_catalog_csv.py` regenerated the Events CSV. The doubled-ladder validator and scoped tag-audit documentation are also committed. Live evidence, upper-band capacity, stale canonical-doc reconciliation, and all other HOLD/PARTIAL boundaries in this handoff remain unchanged.

The status table, remaining-source-defect list, accepted-plan table, and recommended actions below are the pre-closure audit snapshot. The parent closure addendum supersedes its requester-loss actor/title, Event Details/workbook, validator, and canonical-document findings. A subsequent parent patch also makes cancellation call the same host/cause history recorder before clearing its origin flags. The remaining current boundary is live mission timing, retry cleanup, requester-loss/non-annex removal, save/load, Event Log rendering, upper-band capacity, IW-012 timing, joint execution, focus geometry, scenario cells, asset/audio admission, and whole-event runtime evidence, which remain HOLD/PARTIAL.

## Current-HEAD five-commit re-audit (2026-07-29)

This addendum is the authoritative scoped disposition after `4f4e760cc`, `e354860a9`, `a0a5cfc45`, `d696f5b72`, and `f510eac06`; it was rechecked in the current shared working tree after later unrelated commits advanced HEAD.

The older status table, source-defect list, accepted-plan table, and recommended actions below remain preserved as the pre-repair snapshot and must not be read as current for requester-loss actor/title attribution, cancellation host/cause history, Event Details workbook mirroring, validator commitment, or the IW-012 project-order and Network Standing findings.

The whole-event status remains **HOLD / PARTIAL**.

### Follow-up disposition by repaired seam

| Surface | Current disposition | Current evidence | Remaining boundary |
| --- | --- | --- | --- |
| Requester-loss actor and title | **PASS static; runtime HOLD** | `common/scripted_effects/006_independence_wave_crisis_effects.txt:172-207` records payload `6006` with `events_log_system_actor = FROM.id`, so the row points at the annexed requester rather than the annexer. `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:8566-8589` includes occupation, stability, combined, and requester-lost payloads in the crisis-title selector. | No live requester-annexation, Event Log actor/title rendering, persistence, or save/load receipt exists. Non-annex country removal remains outside the recovery hook. |
| Queued and cancelled crisis history | **PASS static; runtime HOLD** | `independence_wave_record_crisis_history` persists host, cause, date, and the initiating Event Log row before transient origin flags are cleared. `independence_wave_record_crisis_resolution_history` now writes distinct payload rows for queued, blocked, cancelled, committed, and requester-lost resolutions. `independence_wave_cancel_pre_wave_crisis` calls both recorders before cooldown/runtime cleanup. | No live cancellation, resolution-row rendering, or persistence evidence exists. |
| Event Details workbook mirror | **PASS for the Event 006 cell** | The final static portion of `chaosx.events_log.window.event_details.independence_wave`, after resolving the four displayed constants, is exactly 1,190 characters and exactly matches workbook `Events!C7` and the Event 006 Events CSV field. The workbook remains the editable source and the CSV remains export-only. | The workbook and CSV currently contain concurrent unrelated dirty changes, so this is an exact Event 006 cell comparison rather than a repository-clean or whole-catalog claim. |
| IW-012 project order | **PASS static; runtime HOLD** | The executable serialized order is Shipping Registers, Municipal Charter, Coastwatch Expansion, Former-host Charter, North Atlantic Compact, then Armed Neutrality. Compact Support reaches 45 before the Compact, Coastwatch reaches 55 after the Compact and 70 after Armed Neutrality, Shipping Security reaches 65, and all values remain within the shared clamp. The six projects consume 1,230 of the 1,440 harbour-mission days. | Live project availability, resource payment, AI ordering, cancellation, harbour resolution, and save/load remain unproved. |
| IW-012 pre-Compact Network Standing | **PASS static through the imported carrier overlay; runtime HOLD** | `common/national_focus/iceland.txt:28-40` imports the overlay root, `independence_wave_overlay_integrate_release_forces`, `independence_wave_overlay_open_foreign_desk`, and `independence_wave_overlay_join_network`. The joined focus requires the two imported branch prerequisites and calls `independence_wave_focus_reward_network_cooperation`, which applies the centrally defined `aid_gain = 10` to the initialized standing of 10, producing 20 above the Compact's observed gate of 15. The required focus sequence costs 5+7+7+7 weeks, or 182 days, and can execute alongside decisions well before the Compact becomes project-eligible after the first four serialized projects consume 750 days. | Live focus rendering and completion order, AI focus timing, interruption, and save/load remain unproved. The stronger treaty-backed standing gate of 60 is not closed by this focus and remains a later transaction requirement. |
| Current overview and resume wording | **PASS for the repaired seams** | `docs/events/006_independence_wave.md:126-130` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:16-24` now describe the bounded retry, durable receipts, queued/cancelled host/cause rows, requester-loss attribution, final workbook mirror, corrected former-host-before-Compact order, and imported join-network path without claiming runtime completion. | Their historical sections remain dated traceability and the whole-event authority remains HOLD / PARTIAL. |
| Source-of-truth and accepted-spec authority | **PASS for the repaired seams; whole-event HOLD** | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:188,235` and its supersession rows record the repaired workbook, cancellation, requester-loss facts, and source-level crisis receipts. Commits `7dd33471a` and `e22dba0e0` promote the crisis additions in specification Parts 2 and 3 and reconcile the current crisis row. | Historical sections remain traceability snapshots, and live mission/queue/rendering evidence is still open. |

### Accepted-plan disposition after the five commits

| Accepted item | Disposition |
| --- | --- |
| Requester-loss actor/title repair | **Implemented and statically verified.** |
| Cancellation preserves initiating host/cause history | **Implemented and statically verified.** |
| Event Details consequence wording mirrored through workbook and export | **Implemented and exactly verified for Event 006.** |
| Correct former-host-before-Compact project order | **Documented and statically reachable.** |
| Network Standing prerequisite named through the imported `join_network` focus | **Implemented and statically reachable; live focus proof remains open.** |
| Doubled 6/8/10/14/20 validator | **Committed and passing.** |
| Crisis design promotion into accepted specification | **Implemented and committed in `7dd33471a`.** |
| Whole-event runtime, capacity, package, focus, scenario, formable, asset, super-event, achievement, AI, and balance closure | **Not implemented or not evidenced to the completion standard; remains HOLD / PARTIAL.** |

### Meaningful validation repeated at current HEAD

- Ran `python -B .tools/audit_event6_allocator.py`; it passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, eleven attestations across ten compatible reservation groups, the RHI/AJX capacity-two exception, 6/8/10/14/20 with World Collapse 20, anchor-before-territory order, and Event 005-before-Event 006 joint reservation order.
- Traced requester-loss actor scope, payload dispatch, title selection, cancellation recording order, and transient cleanup directly through the current source.
- Compared the resolved static Event Details text against workbook `Events!C7` and the Event 006 Events CSV field in read-only mode; all three are exactly equal at 1,190 characters.
- Recalculated all five IW-012 ledgers through the corrected six-project order and checked the Compact Support, observed Network Standing, Armed Neutrality, and harbour-stability thresholds.
- Traced the ICE carrier's imported focus prerequisites and reward path; the overlay root plus two branch prerequisites and `join_network` require 182 focus-days and raise Network Standing from 10 to 20.

### Remaining whole-event blockers

- No live six-, eight-, or ten-country ordinary wave proves exact selection, both RHI/AJX orderings, same-host protection, synchronized commit, rollback, or save/load.
- Fourteen- and twenty-country automatic bands have no admitted-capacity route and remain intentionally fail-closed; the twenty-country `6002` predicate therefore lacks a reachable capacity path.
- No Event 005-first and Event 006-first joint runtime matrix proves shared-host collisions, busy presentation, rollback, delivery, or persistence.
- Crisis category visibility, exact affordability boundary, AI selection, 120-day timing, cancellation, retry exhaustion, requester annexation, non-annex removal, Event Log rendering, and save/load remain live-evidence gaps.
- IW-012 still lacks live focus visibility, project/focus AI timing, material payment, harbour resolution, host variation, force materialization, FORM-02, cleanup, treaty-backed standing 60, rollback, and save/load evidence.
- The shared Event 006 focus framework still carries fourteen blocking geometry diagnostics, while generic meaningful-tree insertion remains fail-closed outside reviewed carriers.
- The 32 SCN-008 mode/intensity cells, whole-event AI and balance horizons, achievement persistence, package admissions, formable families, and country-package runtime matrices remain open.
- FORM-48 remains unreachable through a compliant HBX/HAW/FSM admission set, FORM-06 through FORM-47 remain fail-closed where their adapters are incomplete, and `6001` audio remains rights-blocked without an approved fallback.
- The source-of-truth map and accepted crisis specification additions are now reconciled in current HEAD; historical handoff sections retain their dated pre-closure findings.

No gameplay, localisation, workbook, CSV, focus, decision, event, Soviet Collapse, asset, or shared release source was edited by this follow-up audit.

## Post-`7165466b1` crisis resolution-history re-audit (2026-07-29)

This is the authoritative bounded disposition for the resolution-history patch committed in `7165466b1`.

Random Events, Fallout, CBB, CBD, and unrelated shared-worktree changes remain outside scope.

The whole-event status remains **HOLD / PARTIAL**.

### Outcome-row wiring

| Outcome | Static writer and actor | Payload and renderer | Disposition |
| --- | --- | --- | --- |
| Queued | `independence_wave_queue_crisis_release` sets resolution `queued` and records in the requesting host's `THIS` scope. | `6007`; Event 006-gated outcome title/detail selectors and `GetIndependenceWaveCrisisResolution`. | **PASS static; runtime HOLD.** |
| Blocked | `independence_wave_apply_crisis_blocked_consequence` sets resolution `blocked` before recording in the current requesting host scope. It is reached after an invalid standalone attempt, retry exhaustion, or timeout while another global crisis queue already exists; the guarded cause recorder now preserves a second host's initiating pressure without duplicating the queued requester's row. | `6008`; Event 006-gated outcome title/detail selectors and the blocked resolver key. | **PASS static; runtime HOLD.** |
| Cancelled | `independence_wave_cancel_pre_wave_crisis` sets resolution `cancelled`, writes the initiating cause row, then writes the outcome row before cooldown and transient-origin cleanup. | `6009`; Event 006-gated outcome title/detail selectors and the cancelled resolver key. | **PASS static; runtime HOLD.** |
| Committed | `chaosx.nr6.3` records resolution `committed` only after `independence_wave_standalone_incident_committed` is present, in the surviving requesting host scope. | `6010`; Event 006-gated outcome title/detail selectors and the committed resolver key. | **PASS static; runtime HOLD.** |
| Requester lost | `independence_wave_recover_crisis_requester_loss` sets resolution `requester_lost`, scopes to annexed `FROM`, and invokes the shared recorder there, so its internal `THIS.id` remains the lost requester. The existing `6006` loss-cause row also retains `FROM.id`. | `6011`; Event 006-gated outcome title/detail selectors and the requester-lost resolver key. | **PASS static for `on_annex`; runtime and non-annex-removal HOLD.** |

The `unknown = 6012` payload is a fail-safe mapping and is covered by both selectors and the resolver, but no current call site reaches the recorder without first setting one of the five explicit resolution values.

The six payload values are unique within the Event 006 crisis constants, every payload has exactly one English outcome key, and `GetIndependenceWaveCrisisResolution` has one current definition.

The Event 006 history-detail resolver checks all six payloads before the generic Event 006 detail, and the history-title resolver checks all six payloads before the generic Event 006 title.

No new Clausewitz brace, constant-reference, dynamic-localisation ownership, or requester actor-scope defect was found in the committed tranche.

### Historical remaining static defects (superseded by the parent correction below)

1. The outcome localisation is not acceptable player-facing Event Log prose under the repository writing contract.

`independence_wave.history.crisis.outcome.description` and the queued, blocked, committed, and unknown branches expose implementation terms such as “release coordinator,” “frozen synchronized plan,” “existing ownership contract,” “second release path,” “allocator,” “documented pressure,” and “reservations.”

The committed branch is also factually stale at the point it is written: it says the release incident “now owns the planned state and host reservations,” while the finalization pass clears pending package metadata and `liberation_release_commit_plan` clears plan scope marks before `independence_wave_standalone_incident_committed` is observed by `chaosx.nr6.3`.

2. The blocked localisation and accepted-spec wording do not cover every statically reachable blocked path.

Several hosts can open the 120-day mission before any one of them creates the global queue.

After the first host queues, a later host can reach `independence_wave_resolve_pre_wave_crisis`, fail its `NOT = { has_global_flag = independence_wave_crisis_release_queued }` limit, and immediately call the blocked consequence without constructing, rejecting, or exhausting a plan.

The visible blocked text currently says an invalid or exhausted plan was rejected, and specification Parts 2 and 3 say every outcome row is added to an initiating cause row.

That competing-queue blocked path writes the `6008` outcome but does not call `independence_wave_record_crisis_history`, so it has no corresponding initiating cause row and its visible explanation is inaccurate.

### Validation performed

- Traced every outcome writer from mission/callback or annexation entry through resolution value, actor scope, payload selection, Event Log append, view refresh, title resolver, detail resolver, dynamic resolver, and English key.
- Confirmed payloads `6007` through `6012` are unique in the scoped script-constant sources and all six are covered by the renderer and localisation resolver.
- Confirmed the outcome YAML remains UTF-8 with BOM and the resolver name is defined once.
- Re-ran `python -B .tools/audit_event6_allocator.py`; the current 6/8/10/14/20 and Event 005-before-Event 006 reservation-order audit still passes.
- Attempted a narrow `hoi4.event_inspect` lint of `chaosx.nr6.3`; the MCP transport closed before producing an artifact, so no MCP syntax or state-flow evidence is claimed.

### Historical current boundary and next actions

1. Rewrite the outcome title, shared description, and outcome branches as player-facing historical consequences without allocator, contract, plan, or reservation terminology.
2. Make the blocked wording truthful for both plan failure/retry exhaustion and competing-queue rejection, and reconcile the specification's claim that every outcome has a separate initiating cause row.
3. Run live queued, invalid-plan blocked, retry-exhausted blocked, competing-queue blocked, cancelled, committed, requester-annexed, and save/load Event Log scenarios before promoting this surface beyond static wiring.
4. Preserve the existing whole-event blockers for lower-band allocator execution, 14/20 capacity, Event 005/Event 006 joint delivery, IW-012 runtime, focus geometry, SCN-008, packages, formables, assets/audio, achievements, AI, and balance.

No fallback or simplification was introduced by this audit.

No gameplay, localisation, workbook, CSV, focus, decision, event, Soviet Collapse, asset, or shared release source was edited by this re-audit.

### Parent post-audit correction

The parent repair in the current working tree closes both static defects identified by the post-`7165466b1` audit.

`independence_wave_apply_crisis_blocked_consequence` now records the initiating cause only when the host still carries an occupation or stability origin flag. A competing host reaches that guard with its origin flags intact and receives one cause row before payload `6008`; a normal queued requester cleared those flags after its earlier cause row, so later invalid-plan or retry-exhaustion handling does not duplicate history.

The outcome title, shared description, and six branches are now player-facing. The blocked branch covers every admission failure without claiming a plan was built, and the committed branch truthfully reports completed state transfers and the surviving host remnant after reservation cleanup.

The resolution-history surface therefore receives **PASS static; runtime HOLD** for queued, blocked, cancelled, committed, and requester-lost outcome rows.

Live row rendering, competing-host ordering, retry exhaustion, requester annexation, non-annex removal, persistence, and save/load evidence remain open.

The overall Event 006 and Soviet Collapse coupling disposition remains **HOLD / PARTIAL**, with all allocator-capacity, joint-delivery, IW-012, focus, scenario, package, formable, asset/audio, achievement, AI, and balance blockers unchanged.

## Overall disposition

**HOLD / PARTIAL remains the correct whole-event disposition.**

The named commits materially close the earlier mission/category, doubled-ladder, Coastwatch-ledger, focus-carrier, Event Details, and initial catalog findings.

The later commits also add durable crisis resolution receipts, an `on_annex` requester-loss recovery, and explicit failure-consequence wording.

Those improvements do not supply runtime transaction evidence, upper-band capacity, live ICE carrier proof, or the Event 005/Event 006 joint matrix.

The older body below is preserved as historical pre-closure evidence. Its requester-loss, documentation-authority, validator, and Event Details/workbook findings are superseded by the dated parent addenda above.

## Completion status by surface

| Surface | Status | Current evidence | Remaining boundary |
| --- | --- | --- | --- |
| Crisis category and selectable mission | **PASS static; runtime HOLD** | `common/decisions/categories/006_independence_wave_crisis_categories.txt:8-16` keeps the category visible through the active mission. `common/decisions/006_independence_wave_crisis_decisions.txt:10-38` uses a 120-day selectable mission, concrete cost, cancellation, timeout, and centralized AI weights. | No live visibility, exact affordability boundary, AI selection, timer, cancellation, timeout, or save/load evidence exists. |
| Crisis pressure gates | **PASS static** | `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:11-32` includes stability below 35%, an enemy-controlled owned state above 50 resistance, and a controlled foreign-owned state above 50 resistance. | Country/state scope evaluation is not runtime-proven. |
| Crisis queue and ordinary allocator delegation | **PASS static; runtime HOLD** | `common/scripted_effects/006_independence_wave_crisis_effects.txt:119-153` creates one queue and requester receipt. `events/006_independence_wave.txt:71-136` rechecks the release barrier, performs the bounded retry, and calls only the ordinary standalone synchronized planner. | No live busy-coordinator, invalid-plan, exact-count, rollback, queue cleanup, save/load, or world-end transition scenario exists. |
| Crisis receipt and ordinary Event Log row | **PASS for queued host/cause source; PARTIAL outcome coverage** | `common/scripted_effects/006_independence_wave_crisis_effects.txt:83-117` persists host, cause, date, and payloads 6003/6004/6005 before clearing transient cause flags, then appends an Event 006 system-history row with the requester as actor. `events/006_independence_wave.txt:85-94` records committed or blocked resolution receipts. | The queue-time Event Log row records the request, not the later committed/blocked resolution. Cancellation before queueing receives a failure receipt but no host/cause Event Log row. No live row rendering or persistence evidence exists. |
| Requester-loss recovery | **PARTIAL; source defects remain** | Commit `7b2c39975` adds `common/on_actions/006_independence_wave_crisis_on_actions.txt` and `independence_wave_recover_crisis_requester_loss`, which clear the queue when the requester is annexed and append payload 6006. | The history actor and title are wrong or incomplete, non-annex removal remains uncovered, and no live annex/save-load evidence exists. |
| Soviet Collapse presentation barrier | **PASS static; joint runtime HOLD** | `can_independence_wave_crisis_release_barrier` rejects both `independence_wave_joint_presentation_pending` and `SOV.soviet_collapse_joint_opening_presentation_pending`. Event 005 and Event 006 each clear only their own pending presentation receipt in their public entry events. | No live Event 005-first, Event 006-first, busy-presentation, SOV disappearance, save/load, or retry-exhaustion scenario exists. |
| Joint Event 005/Event 006 allocator ordering | **PASS static; runtime HOLD** | The current allocator audit reports Event 005 anchors first, Event 006 anchors second, then optional territory and lock. `common/scripted_effects/005_006_liberations_collision_effects.txt:1382-1394` publishes both presentation receipts only after the shared plan commits. | Joint collision, same-host protection, rollback, save/load, and presentation delivery are not runtime-proven. |
| Doubled automatic ladder | **PASS source; capacity PARTIAL** | The constants and Event Details use 6/8/10/14/20 with World Collapse 20. Exact-count planner and executor gates fail closed. The static audit reports eleven attested packages, ten compatible group IDs, and the narrow RHI/AJX capacity-two exception. | Six, eight, and ten remain conditionally viable only after live gates pass. Fourteen and twenty have no admitted capacity route. |
| High-chaos `6002` wave predicate | **PASS source; unreachable** | `common/script_constants/006_independence_wave_super_event_constants.txt` uses the exact twenty-country threshold. | The admitted pool cannot reach twenty, so this predicate route and playback remain unproved. |
| IW-012 ledger reachability | **PASS for Coastwatch arithmetic; proof-note PARTIAL; runtime HOLD** | Commit `0fb3b6a35` adds minor Coastwatch gains to the four pre-commitment projects. A valid ordering can reach Coastwatch 55 before Armed Neutrality and 70 afterward, while the five ICE values remain clamped. | The dated repair table places the Compact before the former-host charter even though Compact Support is only 35 at that point and the Compact gate is 45. The Compact also requires Network Standing 15 while setup starts at 10, so the complete 1,230-day proof depends on an additional eligible network-standing action that the ledger handoff does not state. Live timing, resources, AI ordering, focus visibility, harbour resolution, and save/load remain open. |
| IW-012 package and former-host AI | **PASS static; runtime HOLD** | `1696bb940` records the current package re-audit. No scoped Event 006 ICE gameplay uses a hard-coded `DEN`; setup and cleanup target `event_target:independence_wave_setup_former_host`. | Live date/DLC release, host variation, AI activation and cleanup, force materialization, FORM-02, host survival, and rollback remain unproved. |
| Focus-carrier fail-closed behavior | **PASS static; design and runtime HOLD** | `can_attach_independence_wave_additive_focus_carrier` requires the registered ICE carrier and `iceland_tree`. Failed additive assignment sets the missing-carrier diagnostic without setting the additive-ready flag. Current package-prepared consumers require the flag. | Generic meaningful-tree insertion remains intentionally unavailable until each carrier is reviewed. Live ICE shared-focus visibility and save/load persistence are absent. The central Event 006 tree retains fourteen blocking geometry diagnostics. |
| Crisis player-facing wording | **PASS current localisation** | `f4b521767` names both resistance routes and dynamically discloses cancellation, blocked/exhausted stability, war support, resistance, cooldown, and ownership-preservation consequences in the mission and Event Details. | The bounded retry count remains summarized rather than numerically displayed, which is not a contradiction. |
| Workbook and export alignment | **PARTIAL / stale after `f4b521767`** | `Scenarios!C9`, the Liberations cluster row, and their CSV exports remain aligned. Event 006 and Liberations remain `In progress`; SCN-008 remains `Needs Testing`. | `Events!C7` and the Events CSV still contain the shorter pre-`f4b521767` crisis paragraph and no longer match the current static Event Details localisation. |
| Documentation authority | **PARTIAL / stale** | The source-of-truth map top addenda record receipt, requester-loss, and IW-012 repairs. | The same source map still routes stale crisis and catalog findings at lines 188, 235, and 463. `docs/events/006_independence_wave.md:126-130` and `006_independence_wave_resume_packet.md:20-24` still say durable receipt/Event Log attribution, requester-loss recovery, consequence disclosure, catalog verification, and retry disposition are unresolved. |
| Targeted assets | **No new crisis/IW-012/Soviet-coupling bitmap blocker** | The crisis reuses registered Event 006 assets and IW-012 uses reviewed vanilla ICE identity plus existing Event 006 icons. | Whole-event Event 006 asset admission and the exact `6001` audio-rights blocker remain outside this narrow repair closure and still prevent whole-event completion. |

## Remaining source defects

### 1. Requester-loss Event Log actor is the annexer

The offline on-action contract and vanilla precedents use `ROOT` as the annexing winner and `FROM` as the annexed country.

`common/scripted_effects/006_independence_wave_crisis_effects.txt:180-187` correctly stores `global.independence_wave_last_crisis_host = THIS.id` while scoped to `FROM`.

The same effect leaves `FROM` and sets `events_log_system_actor = THIS.id` at line 191.

That `THIS` is the annexing `ROOT`, so payload 6006 attributes the requester-loss row to the annexer rather than the lost requesting host.

### 2. Requester-loss Event Log title does not select the crisis title

`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5374-5384` includes payload 6006 in the crisis detail selector.

The history-title selector at lines 8547-8572 includes only occupation, stability, and combined payloads.

Payload 6006 therefore falls through to the generic Event 006 title at lines 8574-8582 instead of `independence_wave.history.crisis.title`.

### 3. Event Details and the workbook diverged after the consequence wording commit

The current static Event Details paragraph is 1,485 characters before the dynamic rival-bloc suffix.

`Events!C7` remains the 1,031-character pre-consequence paragraph, and the Events CSV matches that stale workbook cell.

The post-`9199b465b` localisation handoff now claims workbook alignment after the parent consequence patch, but no workbook or CSV change was included in `f4b521767`.

### 4. The IW-012 reachability handoff overstates its exact project sequence

The repair closes the previously impossible Coastwatch 55 and 60 thresholds.

Its displayed order is not executable because the Compact is listed before enough Compact Support exists.

Moving the former-host charter before the Compact repairs the five-value order, but the Compact still needs Network Standing 15 from a start of 10.

The source has general network actions that can raise Network Standing, but the handoff's claimed six-project path and 210-day margin do not name or validate that prerequisite.

### 5. Scoped validation and accepted-spec edits remain uncommitted

`.tools/audit_event6_allocator.py` is modified in the working tree to expect 6/8/10/14/20, and the modified script passes.

The committed validator baseline still expects the historical 3/4/5/7/10 ladder, so the current doubled-ladder validation receipt depends on an uncommitted tool update.

The current working-tree addenda to Event 006 spec Parts 2 and 3 accept a centralized bounded retry window and the crisis receipt contract, but those spec promotions are also uncommitted.

## Accepted-plan disposition

| Accepted requirement or plan | Current disposition |
| --- | --- |
| Automatic ladder 6/8/10/14/20 and World Collapse 20 | **Implemented at source.** Six/eight/ten are runtime-held; fourteen/twenty are capacity-blocked and correctly fail closed. |
| Twenty-country `6002` predicate | **Implemented but unreachable.** No fallback or lowered threshold is authorized. |
| Host-facing 120-day crisis using the ordinary allocator | **Implemented at source; runtime HOLD.** No second release algorithm or direct ownership mutation exists. |
| Busy coordinator remains pending for a bounded centralized window | **Source and current working-tree spec agree.** The previous indefinite-versus-fourteen-day design conflict is superseded, but the spec promotion is uncommitted and the canonical docs remain stale. |
| Durable crisis receipt and host/cause Event Log entry | **Substantially implemented; PARTIAL.** Queued host/cause and outcome flags exist, but cancellation has no host/cause row, requester-loss title/actor attribution is defective, and no runtime row evidence exists. |
| Requester-loss recovery | **Implemented for `on_annex`; PARTIAL.** Actor/title defects and non-annex removal/runtime coverage remain. |
| Visible crisis failure consequences | **Implemented in current localisation.** The workbook mirror is now stale. |
| IW-012 Coastwatch and harbour threshold reachability | **Numerical source defect closed.** The dated proof order and omitted Network Standing prerequisite need reconciliation, and runtime evidence remains open. |
| Fail-closed additive focus carrier | **Implemented.** ICE is the reviewed carrier; generic meaningful-tree insertion remains an explicit design gap rather than a hidden fallback. |
| Event 005-first joint reservation and presentation exclusion | **Implemented statically.** Runtime both-order/collision/save-load proof remains absent. |
| Event Details/catalog alignment | **Regressed after `f4b521767`.** Scenario and cluster mirrors pass, but Event 006 `Events!C7` and the Events CSV are stale. |

## Meaningful validation performed

- Ran `python -B .tools/audit_event6_allocator.py`; the current modified script reports 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, eleven attestations, ten compatible reservation groups, the RHI/AJX capacity-two exception, 6/8/10/14/20 with World Collapse 20, anchor-before-territory ordering, and Event 005-first joint ordering.
- Traced the complete crisis category, mission, cost, queue, retry, resolution, Event Log, requester-annexation, and public presentation paths.
- Compared `on_annex` scopes against the offline Paradox wiki and vanilla on-action precedents.
- Traced both Soviet Collapse and Independence Wave joint presentation flags and the shared committed-plan producer.
- Recalculated the IW-012 five-value ledger through all six projects and checked Compact Support, Network Standing, Armed Neutrality, and harbour-stability gates.
- Rechecked the focus-carrier trigger, assignment, ICE registration ordering, prepared-package consumers, and cleanup.
- Rechecked the current scoped Event 006/Soviet Collapse tag audit at `44888d17c`; it reports zero protected external collisions while explicitly keeping REV, ZIN, and ZZZ outside the scoped carrier set.
- Read the workbook in read-only mode and compared Event 006, Liberations, and SCN-008 rows with current localisation and CSV exports.
- Rechecked Event 006 localisation keys and `defined_text` ownership; `GetIndependenceWaveCrisisHistoryCause` has one current definition.
- Attempted a narrow `hoi4.event_inspect` state-flow query for `chaosx.nr6.3`; the MCP transport closed before returning an artifact, so no new MCP event evidence is claimed.

## Validation still missing

- Live crisis category visibility, exact resource boundary, AI selection, 120-day timing, cancellation, blocked planning, retry exhaustion, save/load, requester annexation, non-annex removal, and Event Log rendering.
- Live six-, eight-, and ten-country ordinary waves, both RHI/AJX orderings, same-host protection, synchronized commit, rollback, and save/load.
- Any viable fourteen- or twenty-country pool and the twenty-country `6002` route.
- Event 005-first and Event 006-first joint incidents, shared-host collisions, busy presentation, rollback, and persistence.
- Live IW-012 project order, Network Standing prerequisite, harbour timer, route AI, shared-focus visibility, force materialization, host variation, FORM-02, cleanup, and save/load.
- Live generic and ICE focus-tree visibility plus a clean central focus-tree layout.
- The 32-cell SCN-008 mode/intensity matrix, AI/balance horizons, achievement persistence, `6001` clearance, and the remaining whole-event package and asset admissions.

## Recommended next actions

1. Correct payload 6006 actor scoping and add payload 6006 to the crisis history-title selector, then run a focused requester-annexation/Event Log re-audit.
2. Update the workbook source from the final accepted Event Details wording and run `.tools/export_event_catalog_csv.py`; do not edit the CSV directly.
3. Reconcile the Event 006 overview, resume packet, source-of-truth map body, and supersession table with the committed receipt, requester-loss, failure-disclosure, catalog, and IW-012 facts.
4. Commit or explicitly reject the current doubled-ladder validator and crisis-spec addenda so accepted-plan authority does not depend on a dirty working tree.
5. Correct the IW-012 reachability handoff to use an executable order and explicitly prove the required Network Standing step without overstating the 1,230-day/210-day timing receipt.
6. Preserve 14/20, generic unreviewed carriers, and unavailable package routes as fail-closed until real capacity and carrier evidence exists.
7. Run the parent-owned targeted runtime matrices before changing the whole-event status.

## Simplifications, omissions, and blockers

No fallback or new simplification was introduced by this audit.

The implementation intentionally fails closed for the impossible 14/20 bands and for unreviewed meaningful-tree carriers.

The audit does not promote Event 006, Soviet Collapse coupling, IW-012, the crisis, the catalog, or the focus framework to complete while the blockers above remain.

Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_post_9199_event6_soviet_collapse_completion_reaudit_2026_07_29.md`.

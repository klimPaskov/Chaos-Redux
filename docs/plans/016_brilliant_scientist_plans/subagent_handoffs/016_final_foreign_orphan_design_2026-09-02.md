# Event 016 foreign-operation orphan cleanup design

## Review boundary and status

This is a read-only source design review for the remaining P2 foreign-operation orphan lifecycle gap after checkpoint `892996690509da646c3dcfa1a912096327f7b862`.

The review covers `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`, `common/decisions/016_brilliant_scientist_foreign_decisions.txt`, `events/016_brilliant_scientist_foreign_events.txt`, the Event 016 project and raid on-action files, the shared world-terminal cleanup in `common/scripted_effects/016_brilliant_scientist_effects.txt`, the host-reaction helper, the foreign-operation system documentation, and the final completion contract.

No gameplay file, decision, event, on-action, cost, duration, AI weight, probability, model, save, or live game was changed by this review.

No MCP acceptance claim is made because this bounded task is source architecture only and the parent explicitly deferred further expensive inspection.

The required syntax references were read before this design: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` lines 254–310 and 400–424 and 817–858, `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` lines 240–277, `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` lines 112–124, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` lines 2278–2290, 2733–2781, 6016–6029, and 6496–6511, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` lines 3844–3851, 5006–5013, 5672–5683, and 7450–7469.

The vanilla `common/on_actions/00_on_actions.txt` annex comment and `common/on_actions/05_lar_on_actions.txt` and `04_mtg_on_actions.txt` pre-annex comments were also inspected for ROOT/FROM ordering and the documented civil-war pre-annex lifetime.

## Finding

The durable numeric `brilliant_scientist_foreign_operation_host_id` at start is sufficient for delayed callback identity, but it cannot recover a host scope after the timed decision's regular event targets were never created or after an event chain has expired.

The safe repair is an actor-owned persistent scope pointer assigned at the successful start boundary, paired with the existing numeric host id and live operation type.

The pointer must feed private actor-scoped record, finish, and orphan-cancel cores through `var:brilliant_scientist_foreign_operation_host_scope`; orphan cleanup must not recreate `brilliant_scientist_foreign_operation_actor` or `brilliant_scientist_foreign_operation_host` with `save_event_target_as`.

Recreating those canonical regular event targets inside an on-action would overwrite a caller's nested operation context, and the installed effects documentation exposes no `clear_event_target` effect that could restore an absent prior target.

Ordinary event wrappers should retain their current regular-target and fixed-expected-type guards, then scope the actor into the same private cores; this gives one settlement implementation without polluting an unrelated caller.

## Source proof of the orphan paths

`brilliant_scientist_foreign_start_operation` runs in targeted-decision actor scope, stores only the host id at lines 59–79, and appends the actor to the host's persistent `brilliant_scientist_foreign_incoming_operation_actors` array while incrementing `brilliant_scientist_foreign_incoming_operation_count` at lines 80–86.

Timed decisions in `common/decisions/016_brilliant_scientist_foreign_decisions.txt` save regular actor and host targets only in their `cancel_effect` blocks and resolve through the delayed callback, so an annexation before expiry can strand an actor receipt without a reconstructible regular target.

`brilliant_scientist_foreign_record_resolution` at lines 267–322 appends actor and host history, then unconditionally calls `brilliant_scientist_refresh_international_recognition_score` and `brilliant_scientist_try_fire_foreign_reaction` at lines 318–319.

`brilliant_scientist_foreign_cancel_operation` at lines 401–415 currently depends on the regular event receipt and invokes that record path before finish, so it is not an orphan-safe entry point and can reach the host-reaction tail.

`brilliant_scientist_foreign_finish_operation` at lines 326–396 currently decrements the host count whenever it is positive and removes an actor value without first proving membership, which can release the wrong slot after a duplicate, stale, or already-finished callback.

`brilliant_scientist_clear_foreign_relationships` at lines 1334–1365 clears bilateral relationship context but does not settle the operation array or receipt, and it is called during transfer, departure, confirmed death, and split-sovereignty flows.

The relationship helper therefore must remain free of orphan cancellation because a successful defection, extraction, or assassination is still resolving when that helper runs.

`brilliant_scientist_foreign_callback_matches_active_operation` and `brilliant_scientist_foreign_event_receipt_matches_active_operation` in the trigger file prove that fixed operation type, actor live state, host id, and original host identity are the existing stale-callback boundary.

The event receipt trigger requires both regular event targets, which is exactly the context unavailable to a timed-operation orphan after its host is annexed or its popup chain is gone.

`brilliant_scientist_try_fire_foreign_reaction` at `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt` lines 63–85 requires a current host, valid event targets, detected result, and no reaction receipt.

That guard should remain defense in depth, but it is not the orphan contract because an already-recorded detected result can retain a positive detection value and on-annex ordering can temporarily leave a host scope addressable.

The terminal helper at `common/scripted_effects/016_brilliant_scientist_effects.txt` lines 3884–3913 currently clears foreign context at line 3889 after project and portal cleanup, with no foreign receipt settlement.

The project on-action's existing `on_annex` block at lines 80–87 only evaluates the defeat-victor path, and the raid on-action's annex hook handles Portal state rather than foreign-operation receipts.

## Persistent pointer and private-core contract

At the successful start boundary, assign `set_variable = { brilliant_scientist_foreign_operation_host_scope = FROM }` in actor scope before entering `FROM` for incoming-slot mutations.

Keep `brilliant_scientist_foreign_operation_host_id = FROM.id` unchanged because delayed callbacks and stale-entry checks need a numeric identity in addition to the scope pointer.

Clear the pointer only as the last actor settlement mutation, after actor history, host history, resolved-target retention, pending flags, live flags, and the numeric host id have been handled and the host registry has been reconciled.

The pointer is an actor-scoped regular variable, not a global event target, so concurrent actors do not collide and no global-target cleanup is required.

The pointer assignment has direct repository precedent in `common/decisions/025_alien_technology_in_antarctica_evolution_decisions.txt` lines 103–148 and in `common/scripted_effects/017_random_faction_effects.txt` and `common/scripted_effects/018_resources_found_decision_effects.txt`, where a scope is stored in a regular variable and later entered through `var:`.

Use `var:brilliant_scientist_foreign_operation_host_scope = { ... }` from the actor core.

Inside that host block, `PREV` is the actor scope according to the repository's existing `for_each_scope_loop` and variable-scope patterns, so host history and array operations must reference actor data through `PREV` rather than through a canonical event target.

The private map should be one shared implementation with these bounded effects.

| Helper | Scope and inputs | Required behavior | Call sites |
|---|---|---|---|
| `brilliant_scientist_foreign_record_resolution_actor_core` | Actor scope; live receipt fields and pointer already validated; optional private no-presentation boundary | Append one actor row and one host row, update outcome counters, set the recorded flag, and never dispatch a response itself | Existing record wrapper and orphan cancellation core |
| `brilliant_scientist_foreign_finish_operation_actor_core` | Actor scope; recorded or private-cancelled receipt; pointer and numeric id identify the original host | Append the type-specific resolved target when the host scope is enterable, clear the actor's live receipt before registry reconciliation, and clear the pointer last; do not decrement or remove a host array entry directly | Existing finish wrapper and orphan cancellation core |
| `brilliant_scientist_foreign_cancel_owned_operation` | Actor scope; persistent pointer and numeric id are the ownership proof; no regular event targets | If unresolved, set the cancellation result and record once through the actor core; if already recorded, preserve result and history; clear pending state and finish; never present a reaction | Annexed actor path, host registry candidate pass, and terminal candidate pass |
| `brilliant_scientist_foreign_reconcile_incoming_operation_registry` | Host scope; a bounded persistent incoming array | Snapshot and deduplicate the array, retain only unique live entries whose pointer and numeric id still identify this host, rebuild after all candidate settlements, derive count, and recompute assassination marker | Annexed-host on-action, actor-finish caller, and terminal caller |

The ordinary `brilliant_scientist_foreign_record_resolution`, `brilliant_scientist_foreign_finish_operation`, and `brilliant_scientist_foreign_cancel_operation` names should remain public wrappers.

Each ordinary wrapper must first preserve its current event-target and fixed expected-operation guard, then enter the actor core without writing a regular target or changing `brilliant_scientist_foreign_expected_operation`.

Only the ordinary successful record wrapper may run score refresh and host reaction presentation, and it may do so after the actor core reports that a new row was committed.

The orphan core must call the same actor ledger body with presentation suppressed, not call the ordinary wrapper and hope that the host-reaction guard rejects it.

No `$PARAM$` scripted-effect syntax is proposed because no repository or vanilla precedent was found for it.

## Host registry reconciliation algorithm

The host helper must use a unique temporary array such as `brilliant_scientist_foreign_orphan_snapshot_actors` and a second temporary array such as `brilliant_scientist_foreign_orphan_retained_actors`.

The terminal helper must use separate names such as `brilliant_scientist_foreign_terminal_snapshot_actors` and `brilliant_scientist_foreign_terminal_retained_actors`, so terminal cleanup cannot clear a host reconciliation's temporary arrays if the scopes become nested.

Clear both temporary arrays at the helper boundary, then iterate the persistent incoming array only to copy unique `THIS` scopes into the snapshot.

Do not call `remove_from_array` or `clear_array` on `brilliant_scientist_foreign_incoming_operation_actors` while its `for_each_scope_loop` is active.

The offline data-structures page and vanilla effects documentation both support arrays of scopes, `is_in_array`, `add_to_temp_array`, and post-loop reconstruction, while the repository's Event 015 annex hook supplies the duplicate-filtered snapshot precedent.

Save the current host id in a uniquely named temporary value such as `brilliant_scientist_foreign_orphan_host_id` before entering the snapshot loop.

For each snapshot actor, classify the entry in actor scope as follows.

1. If the actor lacks the live-operation flag, host id, or host-scope pointer, classify the array entry as stale and do not touch a newer or unrelated operation.
2. If the actor's numeric host id differs from the saved host id, classify the entry as stale for this host and do not cancel the actor's current operation.
3. If the actor's pointer is not the current host, classify the old array entry as stale and do not cancel the actor's current operation.
4. If the actor's pointer and numeric id both identify the current host, add it to the owned-settlement candidates and call `brilliant_scientist_foreign_cancel_owned_operation`, preserving any recorded result and suppressing host reaction presentation.

The candidate pass must finish all matching actor receipts before rebuilding the persistent host array, and actor finish must clear the live receipt before that rebuild.

After the candidate pass, clear the persistent host array and add back only unique entries that still have a live receipt whose pointer and id identify the current host.

For an irreversible annex or terminal cleanup, every matching live receipt is settled and therefore is not retained; an entry whose actor currently points at a different host is also not retained in this host's array, but the actor's current receipt remains untouched.

For a non-destructive reconciliation, matching live entries are retained exactly once, while missing, settled, or mismatched receipts are pruned.

Set `brilliant_scientist_foreign_incoming_operation_count` from the retained unique-array size without a maximum clamp.
The parent rejected the initial clamp recommendation: the count must describe all retained live entries, while the existing start gate prevents new operations at the configured two-operation limit.

Set `brilliant_scientist_foreign_assassination_attempt_live` from the retained entries' live operation types, or clear it when no retained matching assassination entry remains.

This derives the count and marker from what survived the classified rebuild rather than subtracting from a historically drifted count.

The actor finish core clears the live receipt before reconciliation, so no single-remove or blind decrement can release a second slot and duplicate array values cannot survive the rebuild.

The host reconciler derives the count and assassination marker from the retained unique live entries rather than from the previous count, and it never mutates the persistent array while iterating that array.

## Annexation and terminal hooks

Add a foreign cleanup call to the existing Event 016 `on_annex` surface or to a narrowly owned adjacent Event 016 on-action file, preserving the existing defeat-victor and Portal hooks.

In every `on_annex` hook, use the documented `ROOT` annexer and `FROM` annexed-country roles and never treat `ROOT` as the orphaned host.

Call the actor-owned cleanup in `FROM` scope so an annexed actor settles its own outgoing receipt through its persistent host pointer.

Call the host registry cleanup in `FROM` scope so an annexed host snapshots and settles only actor entries whose persistent pointer and id identify that host.

Both paths must be idempotent because the same actor can be encountered as an outgoing receipt and as an entry in the affected host's incoming registry, and a second on-action can follow the first.

Use `on_civil_war_end_before_annexation` in addition to `on_annex` where the hook is available, because the vanilla and offline on-action documentation explicitly state that `FROM` and its country data still exist immediately before civil-war annexation.

Do not gate cleanup with `exists = yes`.

In this annex context that trigger can be false for the annexed country because it no longer owns territory even while the on-action still supplies its `FROM` scope and data.

Enter the explicit `FROM` scope supplied by `on_annex` or the pre-annex hook, and guard cleanup with the receipt flag, stored host pointer, numeric host id, and incoming-array membership instead.

For an ordinary annex, the on-annex path uses the explicit `FROM` scope and performs the same bounded cleanup without relying on the territory-based `exists` trigger or dispatching a new operation response event.

If a particular post-annex path cannot enter the supplied `FROM` scope at all, the pre-annex hook is the only source-proven way to guarantee host-side history and registry settlement; the implementation must fail closed rather than invent a country or global target.

The terminal caller in `brilliant_scientist_cleanup_transient_targets_after_world_end` must run the private foreign cleanup before `brilliant_scientist_clear_foreign_context` and after the terminal marker has set the all-actions/world-end lock.

Terminal cleanup is caller-owned and bounded to that country's outgoing pointer and incoming registry; it must not scan every country and must not become a daily, weekly, monthly, or generic scheduler.

The existing terminal host-reaction cleanup remains in place, and private orphan settlement must not call `brilliant_scientist_try_fire_foreign_reaction`.

## History, result, and reaction semantics

An unresolved receipt receives exactly one cancellation history row on the actor and, when the host scope supplied by the stored pointer is enterable, one aligned host row.

An already recorded success, partial, or failure is never rewritten to cancellation and never receives a second history row.

The permanent resolved-target array remains the one-shot guard after finish, including for cancellation.

If a recorded covert result has a positive detection value and its host is being annexed, cleanup still preserves the result but suppresses a new reaction event because there is no valid recipient.

The existing host-reaction guard is useful evidence: it requires current-host status, valid regular targets, and a non-terminal host, and the response context independently requires `exists = yes` and no world-end lock.

Those guards are not a substitute for the private no-presentation boundary because they do not encode the orphan cleanup intent and cannot prove safe ordering during annexation.

If the stored host pointer cannot be entered before actor settlement, the actor core may clear its own pending/live receipt only after recording the actor-side cancellation or preserving the recorded result, but it must not fire an event or attempt host history through an unenterable scope.

The host-side missing-scope branch is an engine-ordering limitation that must remain documented unless the before-annex hook proves it is unreachable for every relevant annexation path.

No source-only review can prove that the native thirteen-day event timeout fires after a recipient country is destroyed, so the timeout remains an intact-chain behavior rather than an orphan cleanup mechanism.

## Scenario traces

### Intact timed operation

The targeted decision starts an actor receipt, stores the pointer and id, appends one host entry, and lets the native timed callback use its fixed type and original host guard.

The ordinary wrapper enters the actor core, records one row, presents a normal reaction only when its original context is valid, clears the actor live receipt, and then lets host reconciliation rebuild the entry and count before clearing the pointer last.

Costs, durations, rewards, outcome formulas, and AI decisions remain unchanged.

### Host annexed during a timed operation

The before-annex or on-annex hook snapshots the host array, finds the actor whose pointer and id match the affected host, records cancellation if unresolved, suppresses presentation, finishes the receipt, then rebuilds the array without that now-settled entry and derives count and assassination state.

The stale native callback later fails the live receipt guard and cannot mutate a newer operation.

### Host annexed after a detected result

The cleanup preserves the recorded success, partial, or failure and its history, clears the pending response, releases the incoming slot once, and does not call the reaction helper or dispatch a replacement response.

Any late host popup fails its event receipt guard because the actor receipt has been finished.

### Actor annexed while the host survives

The actor-side `FROM` cleanup enters the stored host pointer, records cancellation or preserves the prior result, clears the actor live receipt, and lets host reconciliation rebuild the surviving unique entries before clearing the actor pointer last.

The surviving host's count is derived from the rebuilt unique live entries, including when duplicate historical entries were present.

### Duplicate entry and count drift

The host snapshot deduplicates actor scopes before settlement, classifies stale entries without touching a different live receipt, rebuilds the retained set, sets count from retained size, and derives the assassination marker from retained live types.

The algorithm never assumes that a positive old count proves a removable member.

### Same actor and operation type stale callback

The old callback must match the current live flag, fixed type, numeric host id, and pointer ownership before it can settle anything.

An old array value with a different pointer host id is pruned as stale while the actor's newer receipt remains untouched.

### Transfer, extraction, defection, or assassination in flight

The result-producing helper records the operation before `brilliant_scientist_clear_foreign_relationships` clears bilateral relationships, so ordinary relationship cleanup does not cancel the operation mid-resolution.

Only the irreversible annex or terminal hook invokes orphan settlement.

### Terminal world end

The terminal marker sets the all-actions/world-end lock, the terminal caller snapshots with terminal-specific temporary names, cancels only matching actor-owned receipts, rebuilds the host registry from unique live entries, suppresses reaction presentation, and only then does transient foreign context clear.

No country-wide sweep or new scheduler is introduced.

## Required files and ownership

The parent implementation owner should touch only these gameplay surfaces for this P2 patch.

| File | Change boundary | Owner |
|---|---|---|
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | Add pointer at start, split wrappers from actor cores, add private no-presentation cancellation, clear actor live state before bounded host-array rebuild, and derive count/marker from retained entries | Foreign receipt owner |
| `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt` | Add only narrowly proven pointer/id ownership predicates if they reduce duplicated guards; do not weaken existing fixed-type callback triggers | Foreign receipt owner |
| `common/on_actions/016_brilliant_scientist_project_on_actions.txt` or a single adjacent Event 016 on-action file | Add `on_annex` and `on_civil_war_end_before_annexation` calls while preserving existing hooks | Foreign receipt owner with on-action reviewer |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | Invoke bounded foreign cleanup before transient foreign context is cleared at world end | Terminal lifecycle owner |
| `docs/events/016_brilliant_scientist/systems/foreign_operations.md` | Document pointer ownership, private no-presentation cleanup, annex/pre-annex ordering, and missing-scope limitation | Documentation owner |

No decision cost, duration, trigger, AI, probability, localisation, event text, or spreadsheet surface belongs in this patch.

## Correction to the earlier draft and accepted narrower algorithm

The earlier recommendation to gate every `FROM` pointer and array operation with `exists = yes` is rejected.

In the annex hook, `FROM` is explicitly the annexed country, and the territory-based `exists` trigger can be false for that country even while the on-action still supplies its scope and data.

The accepted hook contract enters the supplied `FROM` directly and guards only with the operation live/recorded flags, `has_variable` for the stored pointer and numeric host id, pointer-to-host identity, and actual incoming-array membership.

The existing `exists = yes` checks in ordinary response-context triggers remain presentation guards for live event recipients and must not be copied into orphan cleanup.

The accepted settlement order is actor finish first, with live receipt state cleared before host registry reconciliation.

The generic host reconciliation then snapshots and deduplicates its persistent array, retains each unique entry whose actor is still live and whose pointer/id identify that host, rebuilds after the candidate pass, and derives the exact count and assassination marker from the retained set.

Annex and terminal cleanup first cancel only matching actor-owned candidates, preserve recorded outcomes, and then run that rebuild with separate temporary snapshot names.

There is no single-remove/decrement path and no cleanup mode flag.

The persistent host array is never mutated while its source array is being iterated, and an actor whose pointer/id identify another host is pruned from the current host registry without touching its current receipt.

The engine-ordering uncertainty remains only whether every ordinary post-annex path permits entering the supplied `FROM` scope at that point; the pre-annex civil-war hook covers the documented guaranteed-lifetime path.

## Validation and limitations

Source validation should cover all eleven timed/targeted operation types, the immediate diplomacy paths, every actor report, all delayed callback wrappers, both annex hooks, and the terminal caller.

The source review confirms variable-scope storage through `var:`, `PREV` nested-scope conventions, `for_each_scope_loop` snapshot requirements, `is_in_array` membership checks, and `on_annex` ROOT/FROM semantics from the offline wiki and vanilla documentation.

No MCP event-inspection artifact is claimed for this orphan design, and no live game or log validation was run.

The remaining meaningful uncertainty is whether every ordinary annex path exposes `FROM` after the post-annex on-action; the before-annex hook covers documented civil-war ordering, while the implementation must guard and report any other path where the host scope has already disappeared.

The design intentionally does not solve operation costs, probabilities, project balancing, world scans, or generic periodic reconciliation.

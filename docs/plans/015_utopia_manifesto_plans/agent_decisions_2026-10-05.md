# Event 015 release decisions, 5 October 2026

## Authority and disposition

The user authorized a full Event 015 release audit, every visible defect repair, weak-design corrections under G6, and event-owned feedback for Settings launches under G7.
These decisions are parent-accepted within that scope and implemented in the named source, with MCP and live verification limits recorded separately.
No workbook or export CSV is edited; catalog changes belong in `catalog_changes_pending.md`.

## Selection output survives the helper return

`utopia_manifesto_prepare_random_event_fire` publishes `utopia_manifesto_prefire_candidate_class` as a country-owned normal variable, reset on each invocation, rather than creating a helper-local temporary that its caller reads after return.
The Settings dispatcher calls this helper without preinitializing that temporary and rejects a `none` result before dispatch.
Offline Data structures explains that helper-created temporaries may disappear after return; caller-preinitialized storage survives.
The four class writes happen in the dispatching country before entering the selected actor, so the caller reads the correct country's result.
Ticket scores, class priority and the existing minor-country replacement gates remain unchanged.
A source-backed conservative call-frame check verified that all four actual class assignments survive return, including the zero-candidate class.
This models documented storage lifetime; it does not execute HOI4.

## Human Settings feedback and once-only opening

The manifesto is offered to a safe minor through the existing selection pool.
A human who requests it through Settings receives `.97`, naming a different selected recipient; an eligible local recipient receives `.1` without that extra notice.
An empty pool receives `.98` and does not create a successful event history row or consume the event.
The ordinary `.1` immediate effect sets `utopia_manifesto_opening_presented`.
Subsequent selection skips an already-presented opening and gives the Settings requester the `.98` already-presented explanation, because native `fire_only_once` otherwise prevents another effect-driven delivery silently.
The reports use regular `utopia_manifesto_prefire_actor` context carried from the selection chain and reuse `GFX_report_event_utopia_manifesto_found`.
No world broadcast is added.
The Settings helper is read only; all changes stay in Event 015 source and localisation.
The requested country's unique focus tree is preserved when another minor receives the proposal.

## Provision board available at acceptance

The main category's foundation gate is written by the opening focus, so the original code withheld the board until that focus completed.
Part 4 of the source design asks for the main category to be visible after acceptance.
Within G5/G6 authorization, acceptance sets `utopia_manifesto_decision_phase_input` to `foundations` and calls the existing monotonic phase helper immediately after initializing the provision model.
Later evolved openings and focus completions retain their higher phase transitions; the phase helper never lowers an existing phase.
The paid founding survey may begin during the opening focus, while its equipment costs and the focus route remain unchanged.
This gives the player an immediately readable situation and a concrete first action rather than a blank decision surface.

## Visible terminology

The visible board is called Common Provision.
Script identifiers retaining `_ledger` are implementation names and remain stable.
The localisation and event-UI owners apply this wording coherently and report their exact changed key families in their handoffs.

## Concise choices and factual reports

The user authorized direct repairs for weak release copy. Event options `.45.a` through `.47.option_d` used multiline action names that mixed button labels with cost, meter changes, and outcomes; each button now names the action, while a matching `_release_tt` key retains those player-facing consequences for a custom effect tooltip. The event source insertions are parent-owned, and no gameplay effect changes are part of this text split.

The `.47.d` report now describes the labor columns and the civilian loss that has already occurred, using the parent-owned report snapshot `utopia_manifesto_penal_works_report_civilian_loss`. It omits the projected completion loss and modifier recap so the event reports the current scene rather than a future outcome or a mechanics list.

The close-gates and refugee-municipality cost rows now match their decision debit types. The refugee tooltip separates consumed manpower, support equipment, trains, and displayed Political Power from the nonconsumed Common Reserve threshold and state conditions.

Related country, district, decision, and evolution prose now uses concrete actions and outcomes and removes generic bookkeeping terms banned by the user. Script identifiers remain unchanged.

## Validation limits

The pre-edit exact event-inspect call used `mode=trace`, `selector={kind:event,eventId:chaosx.nr15.1}`, depth 3, 25 nodes and 35 edges.
It returned `timed out awaiting tools/call after 600s`; there is no event graph or lifecycle artifact from that call.
The context route succeeded, while later searches and event rendering remained slow; final results are recorded in the release audit.
Source review and the call-frame model do not substitute for MCP probability, focus, GUI, event comparison or live consumer evidence.
No simplification or generic replacement is introduced by these entry fixes.
Release qualification remains open wherever required evidence or assets are unresolved.

## Post-crash integration and lifecycle decisions

The shared Settings failure hook can send a fallback after an owner rejects a manual request.
The Event 015 empty-pool branch marks `chaosx_manual_event_failure_shown` before sending its own `.98`, preserving one response per request.
The Event Log history and detail builders preinitialize both temporary default-actor outputs before their helper call; this keeps the prepared minor recipient visible through the documented helper-return boundary.
Those are narrow source edits, with no shared layout change.

Full repeal and collapse explicitly return a country to `generic_focus` only when acceptance recorded that generic origin and the currently loaded tree still belongs to Event 015.
A tree another package installed is preserved.
The original tree loads through `keep_completed = no`; a pre-adoption snapshot now restores all originally completed generic IDs through `unlock_national_focus`, without replaying their completion rewards.
The manually approved non-generic class had no source producer, original-tree identifier or literal return mapping.
It is rejected until an explicit safe capture/return mapping is authored, instead of replacing unique content and leaving it stranded after teardown.
This is a parent-accepted G6 safety restriction and a declared deviation from the former manual light-tree allowance.
All five playable political interpretations and their focus paths remain in the package.

Identity teardown snapshots whether an Event 015 leader or the saved original leader still rules before retiring Event 015 characters.
Saved party and election state is restored only for that ownership case; a foreign successor retains its politics.
Cosmetic removal likewise requires an Event 015 cosmetic identity.
The two consumed renunciation-recorder inputs are initialized in their callers, and a renunciation is rejected before any domestic-alternative qualification can count it as a peaceful settlement.

The first-survey mission's early completion belongs only to the paid founding survey.
Paid recounts keep their full duration; their first-account and evolved-shores reports were already guarded and remain one-time.
Current resource contracts and the four unit-growth fee reductions are described in the decision release handoff.
The formation manpower, infantry equipment, support equipment, Army XP, unit counts, capacity limits and training durations are retained; redundant paper and neighbor-transport charges are consolidated into that existing commitment.
The neighbor receives the actually paid support-equipment gift, and combined affordability includes both its gift and the formation's support demand.

## Audit disposition of the automatic empty result

The no-candidate result on an automatic dispatcher is a bounded scalar cache, overwritten at every selector call, rather than an accumulating registry or reusable scope pointer.
It remains readable until the shared readiness gate consumes it; clearing it inside the selector would violate that return contract.
Successful and manual-refusal receivers clear it after consumption.
The automatic zero-result cache is retained deliberately, with no player-visible state, repeated grant, growing array or active timer attached to it.
The earlier description of this one scalar as an accumulating leak is rejected on that source evidence.

## Image and asset evidence

The resumed task downscales any screenshot or render before viewing and does not open large sprite sheets directly.
The current country audit rechecked runtime asset paths and hashes; deleted temporary-workspace pointers and the stale advisor-report document hash were reconciled in the asset matrix.
Original row-level lineage and current MCP visual proof remain explicitly unresolved where the required evidence cannot be recovered.

## Manual launch scope and bulk failure feedback

Destination and refusal feedback covers the existing human manual context used by Settings, Event Log and forced clusters.
The current shared Event Log bulk dispatcher keeps one failure acknowledgement for its whole request.
The Event 015 no-candidate branch uses that shared hook while `chaosx_manual_event_batch_dispatch` is active, with a no-target or already-active reason, so an earlier failed member does not produce an extra Utopia refusal.
A single manual request retains the more specific `.98` report and claims the shared failure acknowledgement before the generic fallback.
No batch, Settings or Event Log layout is changed.

## Political ownership before formation

The original leader remaining in office does not by itself make the current politics Event 015-owned.
The founding package changes no politics, so its teardown preserves subsequent party and election changes even when the original leader remains.
The retained-original-leader restoration branch is limited to the formed Practical Commonwealth and its expected election state: paused before its constitutional succession, open after it.
An observable external election change is preserved.
Native scripts cannot attribute an outside write that leaves the same election value; no perfect cross-system write-ownership claim is made.
This is a parent-accepted G6 safety correction within identity teardown.

## Caller-owned dynamic price result

The dynamic cost refresh consumes `black_friday_price_payable` after `black_friday_price_table_quote` returns.
It initializes that temporary result in the consuming refresh effect before invoking the quote helper.
This guarantees the existing cached fees survive the helper return, as required by the shared quote contract and the offline Data structures wiki at line 440 (SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`).
The installed `set_temp_variable` effect documentation and the existing shared quote implementation supply the native syntax and precedent.
No ordinary amount, sale ratio, resource type, AI numeric weight or outcome is changed.
This is an owner-applied lifetime correction, not an observed free-fee runtime claim.
The prior probability artifacts do not prove this corrected quote flow; exact-price live fixtures remain required.

## Generic focus completion restoration, 6 October

Implemented under G4/G6: capture all 56 exact native generic focus completions before accepting the manifesto, and restore only those completed IDs after the guarded return to `generic_focus`.
`unlock_national_focus` bypasses the recorded focus without its completion effect, preventing factory, research-bonus and Army XP rewards from being obtained a second time.
The foreign-tree guard remains in place and all private completion flags clear on teardown, including a preserved foreign replacement.
The explicit native ID inventory and API evidence are in `subagent_handoffs/final_generic_focus_return_reference_2026-10-06.md`.
This supersedes the former limitation that completed generic focuses were not reconstructed; unfinished focus progress still cancels at adoption.
Native focus inspection/render and the live return status remain unverified; no completion is claimed for those engine checks.


## Graphics decisions accepted on 2026-10-06

The current graphics brief expressly authorizes de-fringing the entire goal set, rebuilding nine 52x40 category icons and the Plural Compact roundel, and reframing all sixteen fictional advisor cards.
The selected colour-only edge repair keeps every main silhouette; only three isolated export marks are removed.
The active categories now use the original event-owned sprite names and their corrected images.
The fictional portraits retain visible defining traits, use plain frames and larger faces, and omit all note writing; identity uncertainty from the absent high-resolution originals remains documented.
The unconsumed Plural Compact emblem is corrected as a registered reserve pending the requested disposition.
Evidence is docs/plans/gfx_fix_2026-10/015_report.md, alpha_independent_review.md and 015_portraits_handoff.md.

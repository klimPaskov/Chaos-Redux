# Event 016 foreign-operation receipt checkpoint

Date: 2026-09-02.
Status: owner implementation and source review checkpoint, not whole-foreign-system or Event 016 completion.
The parent baseline is `1ddbd30d1d983cd6046d594026e980cca4914261`; the foreign source bytes also match the probability auditor's retained `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd` before-source.

## Scope and ownership

The owner changed the foreign decisions, effects, triggers, constants, and events, promoted the receipt contract into `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, and updated `docs/events/016_brilliant_scientist/systems/foreign_operations.md`.
The decision/mission auditor owns `016_final_foreign_lifecycle_review_2026-09-02.md`.
The read-only probability auditor owns `016_final_foreign_receipt_probability_2026-09-02.md` and its exact `E016_FOREIGN_RECEIPT_LIFECYCLE_2026_09_02.scenarios.json` fixture.
Model adapter work is separate and is not part of this checkpoint.

## Implemented boundary

All eleven operation starts recheck their existing public route, one-live actor rule, two-incoming host limit, and permanent type-specific resolved-target exclusion before acquiring a receipt.
Unknown operation types cannot start.
Project selection and the three immediate diplomatic event dispatches occur only inside a successful start.
The counter-program's existing support-equipment debit moved into that same successful selection boundary; its amount and native Political Power cost did not change.
There is one support debit and no repeat payment at resolution or response.

All eight timed decisions bind both cancellation and expiry to their fixed operation type.
All twenty-two foreign events bind all thirty-nine response/report options to their fixed type.
Regular original actor/host targets, the live flag, the saved host id, and the saved operation type must agree before a callback can record, cancel, or finish.
The caller supplies a fixed temporary expected type, not an event-local snapshot or a read of the current operation's type.

Every host response consumes a separate actor-owned pending flag before applying effects.
The three immediate diplomatic routes require an unrecorded result; the eight detected covert routes require an already recorded result.
This preserves the actual covert ordering: outcome, consequences, history, detected host response, then actor report.
Immediate diplomacy needs Kruger's current living host.
Detected-operation settlement may use the original former host after transfer or death, but destroyed parties and a world-end context cannot receive new response effects.
Invalid context cancels only a matching receipt; an already recorded result is preserved instead of being overwritten with cancellation.
Reports require the matching recorded result and no pending host response.
Finish removes the original actor from the original host's incoming array without assuming `ROOT` is the actor.
Late failed transfer commits clear route-success flags as well as reporting the partial/race-prevented result.

## Persistent history

The aligned chronological row includes peer, actor/host role, type, result, detection, family, start date, and selected project stage.
The two older peer lists are role-specific; the new peer/role columns avoid ambiguous joins when a country has served as both actor and host.
Non-project operations initialize family and stage to the existing none constants.
Missing metadata on earlier rows is padded with the explicit invalid sentinel (-1), never fabricated dates or stages.
Metadata repair only grows short arrays and does not truncate existing records.
The only constants addition is `brilliant_scientist_foreign_history_role`; existing balance constants are untouched.

## Reviewed invariants and meaningful checks

- Before/after source extraction found all eleven decision AI blocks and all twenty-eight host-option AI blocks unchanged.
- All eleven native Political Power costs, eight durations, eleven one-shot settings, and eleven actor-owned target arrays are unchanged.
- There are sixteen fixed-type timer writes, thirty-nine fixed-type event-option writes, and one counter-program support-equipment debit.
- Repeated host responses fail once pending is consumed; an early actor report fails before result recording or while pending remains.
- A stale callback for another host fails the saved host-id check; a stale callback for another operation fails the fixed-type check.
- A finished or cancelled same-type/same-host operation cannot restart through the shared helper because its permanent resolved-target receipt remains.
- Cancellation of an already-recorded operation preserves the real outcome and history while releasing only that receipt.
- A successful transfer still finishes against the original host; receipt settlement does not require that country to remain Kruger's current host.

These are source-boundary checks and independent source-review subjects, not execution of the game engine.
The named scenario fixture and MCP limits below remain necessary qualifications.

## MCP evidence

The probability auditor retained the exact ten-scenario fixture with scenario hash `5d6c32359c2215900683ace57139969c8dd47bd79e67167105cdf483d109c346`.
The frozen decision category, invitation `.100`, and defection `.160` comparisons all returned zero comparison changes, no regressions, and no scenario changes.
Their analysis ids are `probability-bd3b07b29b6e62856ae9f657`, `probability-c6507938f5a5e0215ecfdc91`, and `probability-6acd0a064ee13e9a2bab8748`.
Decision rows remain unresolved/score-only, while the event rows retain unsupported helper traces.
Nine other required response pools retain their exact prepatch `INTERNAL_ERROR` blocker and have no valid comparison.
Before/after source overlays retain historical decision/event bytes but both sides may expand current workspace helpers and MTTH; they are not an isolated historical-helper comparison.
See the probability handoff for complete artifacts, source hashes, candidate pools, and unresolved rows.

The parent's full `event_inspect` `state_flow` request for `chaosx.nr16.100` returned `INTERNAL_ERROR`, no artifacts, and no diagnostic detail.
The focused options render returned `EVENT_RENDERED_PARTIAL`, revision `be06dbd18a1cbdfd71a4575935079960cc7d7dfd05af41c7bfbc620aaa538fd9`, graph hash `4dc33d125e067b05cedc9a5c6e77da78d012a55c4a75c2d2781970c9fb04a496`, and layout hash `3838ce44ec8e7259bf263a21dfdd18aae2561fc4f12416e726c5132c95936b8f`.
It selected seven nodes, indexed zero helpers, rendered zero branch variants, and deferred helper/lifecycle validation.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d295ac2fe3cc1d7255c1e341930cc13cc50f00b218311e47a5cef2a61364c705/94526cbf12e43f5af3e3ad95424d1226ca3a190f5010f19f4f050cf9b31056fe/event-options-be06dbd18a1c-manifest.json`.
The old/new revision comparison used the auditor's before revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd` and the current render revision.
It returned `EVENT_REVISION_NOT_CACHED` with the blocker `Requested event graph revision is not cached` and no comparison artifact.
No complete event lifecycle comparison or raster visual acceptance is claimed.

## Dispositions, omissions, and remaining work

The independent decision/mission postreview resolved the original P1 receipt-identity finding and found no new P0/P1 source defect in this checkpoint.
It verified fixed type and party identity, response phases, cancellation after recording, former-host settlement, and aligned history metadata; the destroyed-country P2 and MCP evidence limitations remain open.
The proposed universal `NOT resolution_recorded` host-response guard is rejected because it would break detected covert responses; the separate pending phase is implemented instead.
The public challenge retains its own consequence set; the documentation's generic detection surcharge is narrowed to covert operations rather than inventing an extra payment.
The route-success flag cleanup is implemented.

Destroyed/annexed recipient cleanup remains a concrete separate lifecycle requirement.
Intact chains have the documented native thirteen-day event timeout, but this patch does not add an orphan watchdog or prove that native timeout survives a destroyed recipient.
Bounded host-array reconciliation and actor-owned terminal settlement must preserve a currently resolving successful transfer or assassination; they cannot zero live receipts wholesale.
Country pointers alone do not prove popup-generation identity after annexation and re-release.
These requirements are queued because this checkpoint fixes callback ownership without introducing an unreviewed scheduler or changing outcome ordering.

No project family, evolution, country, focus, meter, scripted GUI, super-event, achievement, asset, model, or public action is added.
Player-facing names, costs, results, Event Log, and Event Details text do not change, so this checkpoint does not edit the workbook or its CSV exports.
Final catalog alignment, full mapped audits, all remaining Event 016 mechanics, and model/runtime acceptance remain outstanding.
The agent did not launch Hearts of Iron IV or request logs.

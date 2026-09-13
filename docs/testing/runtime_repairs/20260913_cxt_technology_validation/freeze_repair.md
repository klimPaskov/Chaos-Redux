# CXT synchronization batching and activation diagnostics

Date: 2026-09-13.
Disposition: scheduling and diagnostic implementation complete; reported freeze unresolved.

## User evidence and investigation

The user ran `e chaosx_test` while playing Germany, waited approximately one day, and saw no test units before the game froze.
The delayed activation receiver therefore remains an important candidate: it annexes Germany, restores the original capital, and runs condemnation, technology, facility, occupation, warfare, camp, stockpile, resource, and roster setup in sequence.
No exact blocking stage can be established from the supplied symptom alone.

Country and scripted-system audits found no demonstrated unbounded CXT registry loop or Event 016/CBRN callback cycle.
The reconciled country audit is `freeze_audit.md`.
The parent reviewed condemnation scoring and dispatch; the scheduled condemnation pulse is thirty days, while the deferred activation flush is synchronous.
A direct helper-call graph found guarded camp and Soviet-collapse cycles; a lexical cycle alone does not establish executed recursion, and the reviewed camp paths have cleanup or display guards.
The Germany-origin before-roster investigation remains unresolved rather than being attributed to a speculative source defect.

## Implemented scheduling repair

Additive package daily hooks can request repeated complete bus passes when several carriers require registration.
`chaosx_test_country_sync_registered_content` marks pending work and schedules one `chaosx_test_country.2` receiver behind a separate queued-delivery flag.
All hooks retain their startup registration, daily registration repair, and existing public synchronization calls.
The receiver runs after the registration hooks, clears its delivery and work receipts before dispatch, and applies all registered extension, project, equipment, and unit consumers.
Initial console setup and explicit refresh call the same apply body immediately.
A refresh consumes current pending work without forgetting that delivery is already queued; another registration reuses that delivery rather than creating a second event.
This repairs conditional repeated synchronization but does not prove that it caused the reported Germany-origin freeze.

## Temporary diagnostics

`CXT_SETUP_TRACE` markers cover console-to-receiver scheduling, Germany annexation, capital validation, setup phases, six facility-type boundaries, extension entry/exit, and the first queued daily pass.
The markers retain game date, country or carrier identity, and registry count where relevant; the engine's log timestamp identifies entry/exit timing.
The trace flag clears after a queued application completes and remains enabled if setup has not reached that point.
Every added trace statement is temporary and must be removed after the blocking stage is identified and repaired.
No logs were requested or searched, and no game or computer-control testing was performed.

## Verification and limits

`freeze_source_validation.json` verifies that the original facility logic, setup outputs, extension dispatch, and full consumer body remain unchanged after removing diagnostic statements and accounting for the immediate apply call.
Queue-state scenarios cover one and eighteen daily requests, refresh while delivery is queued, a new registration after refresh, and a subsequent daily request.
Eighteen same-pass requests schedule one receiver and one full application; explicit refresh retains immediate application and later registrations remain covered.
The scripted-system architect approved the final separate-delivery/work-flag implementation at source level.

The specialist's event inspection returned partial direct evidence with helper projections and lifecycle analysis deferred; its receipt is `freeze_event_inspect_receipt.json`.
Parent event inspect, render, and compare calls returned `Transport closed`; exact receipts are in `freeze_mcp_receipt.json`.
Neither source queue models nor partial MCP evidence establish native execution or freeze reproduction.

## Simplifications, omissions, and blockers

No gameplay content was simplified or removed.
All history pre-unlocks, eighty-three core projects, seventy-one stockpile entries, eighty-seven static templates and their 261 divisions, six facility types, zombie profile, and package registries remain in the preserved setup bodies.
The reported freeze is not confirmed fixed; the task remains incomplete until its blocking stage is identified and repaired.
The current implementation supplies focused diagnostics and removes a proven scheduling multiplicity without substituting another mechanic or disabling content.
The CXT testing guide and events skill describe the scheduling contract.
Skills used or updated: `chaos-redux-events`, `chaos-redux-subagents`, and the official `skill-creator` workflow for the small generic synchronization guidance update.
No Astra subagents were used.

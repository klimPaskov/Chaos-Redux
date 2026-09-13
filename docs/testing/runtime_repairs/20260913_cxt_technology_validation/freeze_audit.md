# CXT activation and first-day country audit

Date: 2026-09-13.
Disposition: source review complete; reported Germany activation freeze unresolved.

## User evidence and verdict

The user ran `e chaosx_test` while playing Germany and reported a freeze after approximately one day, with no test units visible beforehand.
The delayed activation receiver and its setup before the static roster therefore remain relevant to the investigation.
The reviewed source contains no confirmed unbounded CXT loop, self-recursion, or mutation of an iterated registry.
Source review alone does not establish the blocking runtime stage or prove that the freeze is repaired.

## Activation path

The public console effect transfers and controls the saved capital, sets the CXT capital, schedules hidden receiver `chaosx_test_country.1`, and then performs the final player-tag transfer.
The receiver executes in CXT country scope after that transfer, annexes the saved origin country without transferring its troops, restores the saved capital, and checks that the capital is owned and controlled before applying initial setup or refresh.
Initial setup performs the deferred condemnation flush, technology and history setup, six facility-provisioning passes, occupation and warfare fixtures, camp setup, stockpile and resource refill, the static roster, and an immediate registered-content application.
The static roster remains 87 templates and 261 divisions.
The 83 core project outputs, 71 stockpile entries, history pre-unlocks, zombie profile, and six facility types are preserved.

## Daily registration and synchronization

The source inventory contains 18 `on_daily_CXT` declarations across the core and package hooks.
The initialized core hook refills resources and requests registered-content synchronization.
Package hooks retain their registration wrappers and request synchronization when a new carrier is added.
Registration deduplicates carrier tokens in the shared extension registry.

The public `chaosx_test_country_sync_registered_content` marks pending work and queues one hidden `.2` receiver using a separate queued-delivery flag.
The receiver clears delivery and pending-work receipts before calling `chaosx_test_country_sync_registered_content_apply`.
That apply body consumes the complete extension, project, equipment, and unit registries.
Initial setup and explicit refresh retain immediate application; refresh consumes pending work while retaining any already-scheduled delivery.
Further registrations before that delivery reuse it rather than scheduling another event.
This removes conditional repeated complete applications when several package hooks request synchronization, but no evidence establishes that this multiplicity caused the reported Germany freeze.

## Registry and lifecycle review

The expected extension bus contains 18 carriers, one registered special project, 17 equipment declarations subject to deduplication, 23 frontline subunits, and one support subunit with its aligned anchor.
Extension, project, and equipment consumers do not append to their iterated source arrays, and extension apply effects do not register new extension carriers.
Roster consumers append only to separate country-local processed arrays and retain idempotence guards.
The reviewed Event 016 reconciliation and receipt loops are finite, with no demonstrated callback cycle.

Germany annex cleanup copies camp arrays before cleanup, traverses humanitarian state registries finitely, and uses guarded state-local control handlers.
CXT does not satisfy `is_special_chaos_country`, so its camp reveal follows the ordinary guarded rebuild path.
The accepted capital fixture assignment `genocide_responsible_country = PREV` preserves the responsible CXT country scope.
No source evidence connects that assignment to the freeze.
Famine and migration fixture consumers are finite, and no nested CXT loop-index collision or confirmed first-day lifecycle cycle was found.

## Facility workload and diagnostics

Each facility search uses a separate rejected-state array and exits when no unrejected eligible candidate remains.
The search is bounded by its candidate pool and the engine iteration cap; rejected candidates can still incur expensive temporary ownership and controller transfer/restoration work.
There is no runtime evidence that a no-host search occurred in the supplied Germany reproduction, and callback counts cannot be established from these source bounds alone.
No facility legality rule, fallback host, or content substitution was introduced.

Temporary `CXT_SETUP_TRACE` coverage spans console scheduling, receiver entry, annexation, capital validation, setup phases, each facility type, each extension, and the first queued daily application.
The diagnostic flag clears after a pending queued application completes and remains active if setup has not reached that point.
Every temporary trace must be removed after the blocking stage is identified and repaired.

## Evidence limits

This audit consulted the required offline Paradox wiki snapshot, installed vanilla documentation, and scoped source precedents.
The separate native technology investigation and MCP receipts are recorded in this directory.
No game was run, no logs were requested or searched, and no live behavior or engine cost is claimed.
No gameplay source was changed by this audit, and no gameplay content was simplified, disabled, or replaced.
The Germany freeze remains unresolved.

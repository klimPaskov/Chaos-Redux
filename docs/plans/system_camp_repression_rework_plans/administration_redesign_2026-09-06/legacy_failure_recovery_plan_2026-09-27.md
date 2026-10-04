# Legacy closure failure and retry plan

Disposition: implemented in package-owned source; native decision/GUI and live timing evidence remain unresolved.
Acceptance basis: the user approved the full package rework and required legacy decision/mission reconciliation, one payment per action, finite survivor release, and no false closure outcome.
The parent accepts this bounded retry design because the current USA and French timed closures can fail after control loss while leaving unusable in-progress state.

## Current failure

`camp_admin_reform_site` closes and releases finite custody at the first paid legacy start.
The current per-site start trigger then rejects that closed site, so merely clearing country and site progress flags cannot allow a safe retry.
USA `usa_security_authority_sunset` can expire with `camp_rework_dismantlement_in_progress` set, and its availability blocks a repeat order.
French `fr_close_camp_legacy_sites` has no cancel callback; a failed expiry adds exposure and refugee pressure but can leave untimed `camp_rework_site_reforming` and country progress flags.
The full-registry completion preflight already prevents false national success after control loss.

## Package-owned implementation sequence

1. Add `camp_rework_legacy_closure_active_states` on the country and an active-attempt country flag, plus a transient active-attempt state flag and a persistent site custody-accepted flag. The active array records only sites started by this package route; cleanup must not sweep unrelated reforming sites.
2. Create one site begin predicate that requires current actor or subject control, original responsibility, an eligible active site and no concurrent site closure. Permit a fresh open site through the existing exact row/authority start trigger. Permit a retry only with the persistent custody receipt, closed state, zero living detainees and reconciled rows.
3. First start calls the existing integration reform once, records the receipt only after release/closure acceptance, then arms the legacy dismantlement timer. A retry skips the integration reform and reform credit, and only rearms the timer and active-attempt marker. Both paths use the same current quote and one payment guard.
4. Add the complete begin predicate to each direct paid decision's `available`, its Ledger action availability, and the final effect before a debit. The current Ledger executor debits Political Power before route dispatch, so move that debit behind a route-specific final guard if source revalidation can fail after availability. Include UK slot 3, USA slot 3, FRA slot 4, ITA slot 1 and BEL slot 2.
5. Block overlapping national closure attempts while the package active marker exists. In France, cross-gate the legacy timer, North Africa closure and post-liberation reckoning; country decision and Ledger gates must agree. A genuinely empty network retains its national sunset path.
6. On each UK, USA, French legacy and post-liberation, Italian and Belgian closure callback, clear the transient attempt and reforming/timed flags only for states in the saved active array; preserve the custody receipt. Clear country dismantlement-in-progress only if no other responsible site or GUI dismantlement attempt remains. Preserve accountability, evidence, released population, and the site's physical infrastructure on failure.
7. Test first start, failed control, return of control, retry payment exactly once per attempt, no repeated survivor release or reform credit, no stale country flag, overlapping route rejection, zero-site sunset, annexation, and accepted completion. Run current-source decision/mission and GUI availability audits and native MCP scenarios if the routes respond.

The known direct decision and GUI route entry points are `camp_repression_colonial_country_decisions.txt`, `camp_repression_colonial_country_effects.txt`, `camp_repression_rework_effects.txt`, `camp_repression_rework_triggers.txt`, and `camp_repression_ledger_scripted_gui.txt`.
The plan introduces no shared-core change or whole-world hook.
The read-only architect's decision inventory was partial and scenario inspection timed out after 180 seconds; source tests cannot replace engine timing evidence.

## Current source evidence

The shared first-start/retry and cleanup helpers are in `common/scripted_effects/camp_repression_colonial_country_effects.txt`; the fresh/receipt predicate and national readiness gates are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.
The five Ledger availability slots now call the same national readiness triggers before their Political Power debit, and the six country closure callbacks invoke package-attempt cleanup.
Country exclusion clears the active attempt before deleting the active-site registry.
The `foundation_source_tests.py` suite passes 33 scenario groups, including a first 10-thousand-person survivor release, a failed-attempt cleanup and a second physical-closure start with the release total unchanged, a reopened site's new cohort receiving its own release, preservation of a separate reforming site, the selected-site closure control's reason partition, and mission isolation plus timer-grace regression checks.
The parsed-source test mocks other engine consumers; it does not establish a native mission expiry, actual Political Power debit, or click receipt.

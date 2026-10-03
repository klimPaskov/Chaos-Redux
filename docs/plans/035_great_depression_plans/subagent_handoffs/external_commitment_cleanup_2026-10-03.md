# Event 35 external civilian commitment cleanup

## Disposition

Implemented source repair under the user's requirement for exact resource commitments, bounded evaluation, and cleanup.
The parent accepted this narrow lifecycle repair within that scope after tracing external payments to missing terminal cleanup.
The existing `great_depression_action.action_lock_days` supplies the minimum response interval, and no new balance constant or public meter is introduced.
Executed engine behavior, event rendering, and before/after event comparison remain unverified.

## Problem and repaired behavior

External-only contagion and worldwide-pressure countries can pay `great_depression_pay_action_cost` without owning a national depression.
Their former cleanup paths removed the external pressure but retained the civilian commitment indefinitely.

The payment path schedules one hidden `chaosx.nr35.7` review for an external country with a captured civilian quote.
`great_depression_civilian_release_queued` is a delivery flag set before scheduling, so overlapping payments and terminal paths share one pending callback.
The callback clears the delivery flag first, then reschedules only if the external country still has an action lock.
After that lock, it invokes the guarded idle-release helper.
The idle helper releases only when national depression, incoming contagion exposure, and worldwide pressure are all absent.
A zero quote still receives cleanup for its inert snapshot.
National cleanup removes its own commitment unconditionally through the common clear helper.
A queued callback can arrive after national cleanup or conversion without restoring capacity, granting resources, changing Severity, or changing the crisis lifecycle.

## Files and identifiers

- `common/scripted_effects/035_great_depression_effects.txt`: `great_depression_schedule_civilian_commitment_review`, `great_depression_release_idle_civilian_commitment`, `great_depression_clear_civilian_commitment`, payment scheduling, global registry close, country pressure close, and final outgoing-source cleanup.
- `common/scripted_effects/035_great_depression_decision_effects.txt`: containment recipients, ring-fencing, domestic-priority closure, and support-source closure.
- `events/035_great_depression.txt`: hidden triggered-only callback `chaosx.nr35.7`, with `chaosx.nr35.1` still first and unchanged.
- `docs/events/035_great_depression.md`: external commitment lifecycle and private callback contract.
- `common/scripted_effects/chaosx_dynamic_effects.md`: owner-API index row for the existing start/deepen gateway, without duplicating gameplay implementation.

No AI weights, weighted target rules, custom affordability predicates, decisions file, assets, workbook rows, Chaos receipts, or random-event pacing were changed by this repair.

## Source-reviewed scenarios

| Scenario | Source expectation | Execution evidence |
| --- | --- | --- |
| Sole contagion exposure closes after the response lock | Remove both commitment variants and the captured quote | Unverified in engine |
| Worldwide pressure closes after the response lock | Remove commitment unless another surface remains active | Unverified in engine |
| Exposure closes while worldwide pressure remains | Retain commitment | Unverified in engine |
| Worldwide pressure closes while exposure remains | Retain commitment | Unverified in engine |
| External target converts to national depression | Callback preserves the national commitment | Unverified in engine |
| Several payments or closures occur before delivery | One delivery flag coalesces review requests | Unverified in engine |
| A newer response lock overlaps an older callback | Callback requeues instead of releasing early | Unverified in engine |
| National cleanup precedes callback delivery | Later delivery clears its flag without recreating content | Unverified in engine |
| Captured quote is zero | Private snapshot can still be cleared | Unverified in engine |

## References and source identities

Installed `documentation/effects_documentation.md`, lines 2943 to 2972, documents country-event scheduling and its country scope.
Its revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed `common/scripted_effects/SOV_scripted_effects.txt`, lines 20 to 29 and 42 to 49, supplies variable-backed delayed country-event precedents.
Its SHA-256 is `CC9E16837AFA1428D11E053DC982446B35587980DAA011A1DF12114C3ACE2BF4`.
Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 25 to 35 and 130 to 147, describes recipient scope, delayed delivery, and triggered-only events.
Its SHA-256 is `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D`.
The relevant sections were read directly because current domain/reference-read requests have not returned final artifacts.

Current main effects SHA-256: `2E27D624B6AF99F0A84B711752E95825336A755E866E00DBE8BD1D2F796F0E3F`.
Current decision effects SHA-256: `725C42FABD30A71D43A7C24F80BC94B99E0653D96C4A685C016E8D840A8F8F17`.
Current events SHA-256: `F37608631760449F1313220D7436261510DF29AF856F63C78A3664C048A2F286`.

## Affordability baseline queued separately

The explicit availability gap covers 74 ordinary paid decisions, rather than only the six doctrine choices.
The 15 missions already repeat their affordability predicate in `available`.
No eligibility patch has been applied before its required baseline audit.
The immutable decisions snapshot is `audit_inputs/affordability_2026_10_03/035_great_depression_decisions_before.txt`, with SHA-256 `2CB7B2538E5329772320A858CE7E3B06B5065E858FD4506C6F96DC75AF77C185`.
The six boundary fixtures are `audit_inputs/affordability_2026_10_03/scenarios.json`, with SHA-256 `4512EB75C67071B120FC439833A6669A10EF3065179B87F7672D79189038EFDD`.
Their declared inputs are audit assumptions, not live campaign state.
The isolated probability auditor is `01a10038-028f-7fc0-b726-24694f3e34c8`.
Its first bounded observation timed out without reporting a terminal status, so it must be observed again rather than restarted solely because of that timeout.

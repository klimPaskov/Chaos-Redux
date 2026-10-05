# Event 042 owner decisions, 5 October 2026

Acceptance basis: the current user assigned all Event 042 surfaces and authorized correction of weak design under quality requirement G6.
These are parent decisions within that scope, not separately quoted user approvals.

| Decision | Reason | Disposition and source |
| --- | --- | --- |
| Keep `chaosx.nr42.1` as a hidden canonical entry and use `.2` for discovery. | Entry can recheck eligibility, select a valid alternative, or explain an empty pool without silently failing a forced firing. | Implemented in `events/042_equipment_from_heavens.txt` and `equipment_from_heavens_enter_delivery`; no new dispatcher framework. |
| Retain the full cargo and three-to-seven recovery visits but show one discovery and one final summary. | Repeated image/report IDs and rapidly mutable targets create interruption and misleading presentation. | Implemented in `equipment_from_heavens_start_recovery`, `dispatch_next_report`, and `fire_visible_report`; .10/.11/.12/.14/.15 remain dormant compatibility definitions. |
| Start recovery after discovery acknowledgment and queue visits sequentially. | Prevent simultaneous queued visits from overwriting the text a player is reading. | Implemented; recovery uses saved arrays and country state. |
| Replace one middle visit with an accident. | The old accident append could exceed seven sites. | Implemented; accident odds and cargo tables are preserved. |
| Cap accident loss to equipment still in the stockpile. | A report must describe the actual loss even if cargo has already been deployed or transferred. | Implemented in `equipment_from_heavens_apply_recovery_accident`; infrastructure damage is separate. |
| Show a halt report if every landing ground is lost. | A country unable to finish recovery must not receive a false success report. | Implemented as .17; successful summaries count only completed visits. |
| Merge landing burdens by strength and retain the later deadline. | A small subsequent consignment must not shorten a larger unfinished burden. | Implemented in `equipment_from_heavens_apply_landing_zone`; stored dates use the shared date converters. |
| Credit Tiny Arsenal State to the actual capitulation winner and check its last growth day. | Allied participation alone is insufficient; monthly sampling otherwise misses growth on day 365. | Implemented in the Event 042 on-action and achievement effects. |
| Preserve Borrowed Nightmare's requested combat-loss condition as unresolved. | Country stock decline during war can come from attrition, lend-lease or destruction. Unit-leader callbacks do not prove the participating division. | Blocked: no exact combat-loss primitive was established. No weaker criterion was substituted. |
| Retain every singular-file localisation key in the plural file. | Complete the event-owned naming transition without losing legacy popup text. | Implemented; Git history credits Klim Pashkov commit 794b31a7b with adding the plural file, but does not identify the original uncommitted rework author. |
| Keep the static seven-family special allowlist and existing quantity/AI tables. | No current allowed family was shown unsafe. Hypothetical conditional-pool fixtures do not justify invented eligibility gates. | Implemented; conditional/excluded families remain outside the registry. |

The user prohibits spreadsheet edits for this task.
Required wording is queued in `catalog_changes_pending.md` for the catalog owner.
No event-specific process rule was added to a reusable skill: date units, helper-output lifetime, and shared-index commits are already covered by the repo skills.

Discovery uses the native scripted-localisation picture selector: sealed special cargo, atomic cargo, aircraft, armor, then ordinary crate fields. Final summaries use the overwhelmed depot. This preserves all six report assets while keeping two popups; high Chaos alone never selects a special-cargo picture.

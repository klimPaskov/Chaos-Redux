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

The final entry audit retains manual provenance when a rejected recipient is replaced. Pending and active manual markers are country flags, and all three achievement snapshots reject the active manual flag. A direct unprepared entry stays manual after rerouting; a prepared ordinary automatic entry remains automatic. This closes an eligibility bypass without changing cargo weights or amounts.

Prefire readiness is set only by a successful draw, so a stale same-chain event target cannot make an empty recipient pool look ready. The pointer is not cleared with an invented regular-target API; the caller uses the documented readiness output.

## Borrowed Nightmare follow-up, 6 October 2026

Acceptance basis: the director explicitly approved replacing the stock-loss proxy with a battle victory by a commander whose army contains the recovered equipment.
Disposition: implemented, superseding the unresolved combat-loss decision above.
The native `on_army_leader_won_combat` callback checks the saved equipment token using leader-scoped `num_equipment`, then awards the owner's achievement.
Normal-delivery and player eligibility, source-event absence, the first-family snapshot and the 1095-day window are retained.
The window and source-event guard are checked at the victory itself, so the gap between cleanup pulses cannot admit a late victory.
Forced deliveries cannot open the route and cannot qualify through the victory callback.
The equipment must be present in the winning commander's army, as approved, rather than proven to be in the particular division participating in that battle.
No stock loss is required and the hidden pulse cannot award completion.
Achievement description, tooltip and Event Details state the victory requirement, deadline and forced-delivery exclusion.
No new report or news popup, asset, AI weight, decision or GUI layout is introduced.
Skills used: `chaos-redux-events`, `chaos-redux-scripted-gui` (Event Details text review), and `chaos-redux-shared-git-commit`.
No skills were changed.
No gameplay simplifications were made.

### Validation and route gaps

The connected tool inventory exposes none of `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.script_validate`, event inspect/render/compare or GUI inspect/render/compare.
MCP and visual validation are unavailable in this session, and source review is not claimed as engine evidence.
Installed documentation has no `on_actions_documentation.md` or `scopes_documentation.md`, so the documented vanilla on-action and offline wiki establish the callback scopes.
The report colour audit and focused source checks are recorded in the follow-up completion note.

### References read directly

- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, lines 494-499, SHA-256 `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 1695-1730, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`, lines 1249-1269, SHA-256 `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, lines 2110-2135, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 4833-4852, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt`, lines 5573-5595, SHA-256 `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9`.

### Focused checks and orchestrator live cases

Source review confirms the victory callback is the only writer of `efh_ach_nightmare_complete`, reads leader-scoped equipment rather than country stock, validates source-event absence and the 1095-day window immediately, and retains the manual-delivery rejection at both snapshot and victory.
The report colour audit returned `total keys with colour: 0`.
The shared Event Details layout is unchanged, but the longer description needs visual acceptance at 1920x1080, UI scale 1.

1. In a fresh player-country war fixture, enable Evolution III and obtain an ordinary automatic special delivery with its source event absent.
Inspect `efh_ach_nightmare_token` and field that equipment in an army under a general.
First win a land battle with a different general whose army has none of that type, then win with the equipped general within 1095 days.
Expect no Borrowed Nightmare award for the first victory and one award for the equipped general's victory, even with no equipment losses.
2. On separate branches of the qualifying fixture, lose a battle, reduce the stockpile through transfers or attrition without victory, trigger the equipment's source event before victory, or win after day 1095.
Expect no award in each branch, including victories between two cleanup pulses.
3. In a fresh branch with no ordinary special delivery, force a special delivery from Settings or `event chaosx.nr42.1 <TAG>`, field its special equipment and win a land battle.
Expect no active Borrowed Nightmare route and no award.
4. Open Event 042 Details and the Borrowed Nightmare achievement description/tooltip at 1920x1080, UI scale 1.
Expect the commander-army victory rule, 1095-day deadline and forced-delivery exclusion, readable text and no clipping or raw keys.

Implementation is committed without gameplay simplifications.
MCP and live checks remain validation limitations, not claimed passes.

# Handoff 5: plan completion audit and second pass on restores

Read `00_common_rules.md` in this folder first. Run this after, or alongside, handoffs 1 to 3.

## Why

Each plan item now has commits beside it, but the jobs graded their own work. The owner's complaint was that changes were made that nobody asked for and that good work was overwritten. This handoff checks every item against the owner's own words and catches what the first pass missed.

## Tasks

1. **Item-by-item check.** For every item in `docs/plans/chaos_redux_restore_plan_2026-10-12.md` (A1 to A13, B1 to B14, C1 to C12, D1 to D5, E2), open the commits listed and confirm the item is truly done as the owner worded it. Mark each `done`, `partly done` or `not done` in a new table `docs/plans/plan_completion_audit_2026-10-13.md`, with evidence. Fix what is partly done or not done.
2. **Text restore, second pass.** The first pass restored 9,218 values from 123 commits. Check its exceptions list in `chaos_redux_text_restore_2026-10-12.md`: every key it chose NOT to restore needs a reason that holds (a new key, a dynamic value). Then sample 300 player-facing keys at random across events, decisions, tooltips and super events and compare each with its value on 1 September 2026; any rewritten survivor means a missed commit, so find it and restore the whole commit's keys. Pay particular attention to decision category texts, report and news event options, raid texts and tooltips, which the owner named.
3. **Icons and portraits, second pass.** Compare every `.dds` under `gfx/` that existed on 1 September 2026 with its current bytes. Any that differ and are not listed as restored or as an owner-approved replacement: restore. Check every `.gfx` sprite that existed then still points at the same texture path.
4. **Audio, second pass.** Same comparison for `sound/` and `music/` and their `.asset` and `.txt` definitions.
5. **Gameplay text and values the owner named.** The Orders from Unknown Hands event: confirm its text is the restored older text and that it no longer hands out a strong idea. The crisis pressure setting: off by default, slight, worded for all events. The Last Fury Standing focus: gone, its purpose merged into a neighbour.
6. **Size and type consistency.** Decisions use decision-size icons, categories category icons, ideas idea-size icons. List every mismatch that remains and fix by wiring an existing correct icon.
7. **Report events:** none has more than 4 options.
8. **Docs.** Bring the system docs and the event catalog workbook in line with what was restored (use the `chaos-redux-xlsx` skill; run `python .tools/export_event_catalog_csv.py` after any workbook change).

## Deliverable

`docs/plans/plan_completion_audit_2026-10-13.md`: the table, what the second pass found and restored, your commits, and a short list of anything that genuinely needs the owner.

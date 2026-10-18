# Handoff 2: interface restores that were left undecided

Read `00_common_rules.md` in this folder first.

## Why

`docs/plans/interface_restore_audit_2026-10-13.md` classified 417 commits touching the interface since 1 August 2026 and restored nothing new: 36 choices were listed as unresolved because the auditor was told not to restore when unsure. The owner has now said: "I want everything now restored, fixed and everything that was included in the plan." and earlier: "A lot of things have to be restored how they were before."

## Tasks

1. Go through all 36 unresolved choices in the audit. For each, restore the earlier layout, labels, art bindings and scripted GUI wiring from the parent commit exactly, UNLESS one of these is true:
   - the change is something the owner explicitly asked for in `chaos_redux_restore_plan_2026-10-12.md` (for example the cluster checkboxes, the removed cluster subheaders, the Miscellaneous placement of auto event logs);
   - the change belongs to a genuinely new mechanic that had no earlier window;
   - it is a bug fix with no visual redesign.
   Record the reason for every choice you keep.
2. Event 014: commit `8ee066f4e` removed controls that could not be put back at their exact positions without overlapping later controls. Restore the earlier window as a whole from `46235fdec6` and re-place only the later, genuinely new controls into free space, rather than leaving the removals in place.
3. Do not undo the restores of 12 and 13 October (commits `cd2f068437`, `63188d7cdc`, `0792029bab`, `9e43b45002`, `30ac00fb03`, `1fca4df6a7`, `360245b7ff`, `13aea99060`, `7ea7d51f5b`, `76c7815224`, `13ac669bcb`, `f5b8f4a61a`).
4. Disease Containment Board: its entry points were unhooked by `3deac2d4d`. Confirm nothing in the interface still opens or references it, and that its localisation and sprites cause no load error.
5. After restoring, check each window with one render through the `hoi4_agent_tools` MCP (`hoi4_gui_render`). If rendering stalls again, check geometry from source and hand the list of windows to handoff 1 for screenshots in the live game.

## Deliverable

Update the audit's table with the action taken per choice and your commits, and move the "needs the owner's decision" section to "resolved" with one line each.

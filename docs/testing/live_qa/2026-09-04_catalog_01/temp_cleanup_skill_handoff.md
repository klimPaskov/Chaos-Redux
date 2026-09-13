# Temporary cleanup skill handoff

Disposition: implemented within the parent-authorized skill-only scope.

Updated `.agents/skills/chaos-redux-debug-playtest/SKILL.md`, section 7, with one four-sentence paragraph after the comparison-syntax note.
No equivalent temporary-cleanup guidance was already present.
Exact addition:

```diff
+For an unsupported `clear_temp_variable`, do not mechanically rename it to `clear_variable` or delete all occurrences: the offline Data structures `clear_variable` entry restricts that command to regular variables.
+Inventory each exact identifier's writes, reads, callers, nested helpers, and caller continuations before choosing a repair.
+Delete a terminal cleanup only when every subsequent invocation initializes before any read and no downstream consumer observes the identifier's absence or retained value.
+Cross-helper inputs or sentinel semantics require an explicit repair that preserves the consumer contract; neither setting zero nor assuming deletion at a helper's closing brace proves equivalence to absence.
```

References read: offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:410` for temporary lifetime and helper caveats, and line 530 for the regular-variable-only restriction; installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:2773` for `clear_variable` and line 7820 for supported temporary assignment.
The parent evidence documents `containment_temp_cleanup_analysis.md` and `event21_temp_cleanup_analysis.md` in this QA folder supply per-identifier write/read inventories, caller continuations, repeated-call reasoning, and acceptance boundaries.
The parent reports the first deletion's diagnostic absent from launch 08 and the three later deletions awaiting launch 09; the containment analysis still says native confirmation is pending, so this handoff records that distinction without editing the other owner's document or claiming an independent retest.

Used the previously read `skill-creator` guidance and the target debug-playtest skill for maintenance only.
The addition contains no event identifiers or run-specific context and preserves concurrent schema/comparison notes, launch limits, authorization, routing, and MCP text.
Validation: checked the repair criteria against the documented distinction between regular and temporary variables and the supplied consumer inventories; the skill validator passed.
No new skills were created, and all other skills were left unchanged.
No gameplay, configuration, AGENTS.md, desktop, process, staging, or commit actions were performed.
No simplifications or blockers for this documentation task; runtime acceptance of the underlying repairs remains the parent's responsibility.

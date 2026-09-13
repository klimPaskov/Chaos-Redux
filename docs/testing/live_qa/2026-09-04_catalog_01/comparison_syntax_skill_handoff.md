# Comparison syntax skill handoff

Disposition: implemented within the parent-authorized skill-only scope.

Updated `.agents/skills/chaos-redux-debug-playtest/SKILL.md`, section 7, with four sentences distinguishing valid `check_variable` shorthand from a mixed `var =` plus shorthand comparison.
The repair guidance removes only the redundant `var =` and preserves the comparator, scoped variable token, right-hand value or constant, and valid long-form blocks.
No event identifiers or run-specific context were added to the skill.

Evidence: installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `check_variable` section beginning at line 2110, explicitly documents separate long-form and shorthand forms.
The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, line 531, independently documents both forms and strict shorthand comparisons.
Existing skill coverage was checked; section 7 had generic parse-error triage but no mixed-comparison guidance.
Used `skill-creator` and read the target debug-playtest skill for maintenance only.

Validation: reviewed the addition against both syntax references and confirmed the pre-existing skill edits were preserved.
Approval, MCP, live-control, and routing instructions were not changed by this addition.
No gameplay, configuration, or AGENTS.md edits; no staging or commit.
Other skills were left unchanged, and no new skill was created.
No simplifications or blockers for this bounded task.
This handoff establishes documentation completion only; it does not verify the parent’s gameplay repairs or a live startup result.

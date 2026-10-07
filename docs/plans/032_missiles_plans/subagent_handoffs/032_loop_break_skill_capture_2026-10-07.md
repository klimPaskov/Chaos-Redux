# Loop break isolation skill capture

Disposition: implemented reference capture, pending parent review and parent-owned commit.
Acceptance basis: the parent explicitly requested this bounded capture from two independent source audits reported in the task brief.
Those audits were supplied as findings, without audit paths, and were not independently rerun by this skill-maintenance task.

## Owned changes

- Created `.agents\skills\chaos-redux-events\references\loop-break-isolation.md`, which was absent before this task.
- Appended one link line at `.agents\skills\chaos-redux-events\SKILL.md:978`, with a separating blank line at 977.
- Created this requested handoff.

Exact owned append hunk, relative to the pre-edit working file:

```diff
@@ -976,1 +976,3 @@
 23. Mapped event-owned Chaos changes are tied to concrete outcomes, guarded against repeat farming, and do not double count shared sources.
+
+For helpers that iterate records or scopes, read [Loop break isolation](references/loop-break-isolation.md).
```

The reference covers both foreach defaults, unscoped temporary state, a distinct private break variable reset before every loop invocation, independent inner and outer protection, receipt retention, a generic nested example, and inherited-break regression cases with two objects.
It distinguishes the documented while/for bound from an unproven foreach ceiling and retains a conservative test above 1,000 objects.
No event-specific identifiers or context were added to the skill or reference.

## Evidence and preservation

Read repository `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, and official `skill-creator`.
Live `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` succeeded for the relevant documentation.
The general context bundle omitted Triggers and Modifiers, which are outside this narrow documentation capture, and coverage is claimed only for the exact loop sections read.

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 4279-4295 and 4296-4311, read through revision-bound MCP calls and checked directly.
  Source revision/SHA-256: `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, foreach rows 1216-1217 read through revision-bound MCP calls, with temporary-variable lines 440-442, foreach examples 1222-1256, and explicit while/for bound rows 1219-1220 read directly.
  Source revision/SHA-256: `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

Before editing, the dirty events skill contained 101,319 bytes with SHA-256 `8899b0cc3648f8f35edfef19d3287312cab77410d85d5f97ab38a9de65e57640`.
After editing, its entire original byte sequence remained an exact prefix, preserving all pre-existing owner edits and their mixed CRLF/LF endings.
The only appended content is the blank separator and link shown above.
The official skill validator accepted the existing skill with the new reference link.
The regression cases are documented test guidance, not executed engine or gameplay evidence.

## Parent review and limits

The pre-existing dirty skill at lines 192 and 195 broadly claims a native loop ceiling for all effect loops and fixtures.
The cited offline documentation explicitly identifies the 1,000 bound for `while_loop_effect` and `for_loop_effect`, while the installed foreach sections provide no ceiling.
That broader wording remains unchanged under the append-only task boundary and needs owner review in a separate hunk.
There is no conflict with AGENTS.md, which names the while/for bound, and no subagent-routing update is required.

Parent should review the new reference and commit only the owned append hunk plus the new reference and this handoff, separately from existing dirty skill edits.
No Git commands, sync generators, other agents, gameplay, assets, localisation, workbooks, game launch, or logs were used or changed.
No simplifications or omissions in the requested capture, and no blocker to the reference delivery.
Foreach engine ceilings and live regression outcomes remain unverified.

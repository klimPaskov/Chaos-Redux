# Targeted response refresh skill handoff

Disposition: `implemented` for the authorized skill guidance only.
Acceptance basis: the requesting parent explicitly specified the bounded urgent-offer pattern and authorized edits to this skill and this handoff.

## Owned changes

Updated `.agents\skills\chaos-redux-decisions-missions\SKILL.md` by inserting one generic paragraph immediately after the existing native cadence paragraph under `### Trigger evaluation cost`, before `## 8. Mission quality`.
At write time, the owned sentence lines are 322-325, followed by one blank separator.
Created this handoff; no other files were edited.
No gameplay, Git operations, or game launch occurred.
The parent owns isolation of the skill addition at commit; the full skill file may contain other agents' changes.

Exact owned addition:

```markdown
When an urgent targeted response must appear promptly after an offer, putting its volatile offer predicate only in the daily `target_trigger` can leave a cache gap.
Keep the existing narrow `targets` or `target_array` and preselect stable candidate eligibility in `target_root_trigger`/`target_trigger`; repeat the full current offer and authority predicate in live `visible`, `available`, and effect preflight, preserving `ROOT`/`FROM` scope semantics and every existing eligibility requirement.
Use this pattern only when the per-frame work stays bounded and cheap; never expand to a world scan, weaken eligibility, or hide a paid deadline.
New or uncached countries still obey the engine's target refresh, so source counts do not prove immediate target admission or native UI appearance.
```

The insertion includes the blank line following the paragraph.
All pre-existing skill bytes, including the preceding cadence paragraph and general cheap-visibility guidance, were preserved.
Removing the exact inserted byte range from the written skill reproduced its pre-edit bytes.
Pre-edit skill SHA256: `ec159cc0f9e76a2f7948d18b22f8ce9776b0b8c7d84eb34fe1b8d94e931bdbfe`.
Post-edit skill SHA256 at write verification: `2cce9d17fa69e19da18e400b7ea156c8328619928f60c020aa0b38c7c96ef83f`.
These whole-file hashes are preservation evidence at that moment, not ownership of other hunks or an expectation that the shared file remains unchanged.

## Sources read directly

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`, lines 1-46, SHA256/revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`: lines 12-20 establish interface-refresh cadence and live target scope; lines 24-36 establish daily target preselection and its performance purpose; lines 38-45 warn against broad state selection.
- Offline `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, lines 531-537, SHA256/revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`: lines 534-536 document the daily gap, narrow targets/arrays, and `ROOT`/`FROM` roles.

Both file hashes matched the supplied revisions.
Also read repository `AGENTS.md`, the existing decision skill's cadence and related guidance, and `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`.
Direct section reads were explicitly requested; no broad MCP workflow was needed or invoked for this documentation-only change.
The conditional pattern captures the parent's reported reusable lesson using the documented cadence; the citations do not establish uncached admission timing or native UI behavior.

## Validation and handoff limits

The official `skill-creator` validator returned `Skill is valid!` via `python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-decisions-missions` with UTF-8 mode enabled.
Reviewed the addition against the requested invariants: stable narrow candidate selection, full live offer and authority checks, effect preflight, preserved scope and eligibility, bounded per-frame cost, visible paid deadlines, and explicit engine refresh limits.
The addition contains no event-specific identifiers or context and does not replace the existing cadence guidance.
No runtime or native UI evidence was produced; source counts cannot prove immediate appearance of new or uncached countries.

Skills used: `skill-creator` and `chaos-redux-decisions-missions`.
Skills updated: `chaos-redux-decisions-missions` only.
Skills created: none; all other skills were left unchanged.
Routing changes, `AGENTS.md` updates, and subagent-skill updates needed: none.
Blocked work: none within the authorized documentation scope.
Simplifications or omissions: none within that scope.
Parent review remains responsible for isolating the exact addition; native consumer behavior remains unverified by this skill-maintenance task.

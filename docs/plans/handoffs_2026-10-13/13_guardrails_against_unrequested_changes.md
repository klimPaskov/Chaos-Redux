# Handoff 13: guardrails so this does not happen again

Read `00_common_rules.md` in this folder first. This handoff can run at the same time as all the others.

## Why

The damage came from agents rewriting text, redesigning windows, replacing art and simplifying systems that nobody asked them to touch. The owner: "im crying of many unasked and changes were made." The repo's own instructions and skills must forbid it plainly.

## Tasks

1. Read `AGENTS.md`/`CLAUDE.md`, every skill under `.claude/skills/` and every agent definition under `.claude/agents/`. Find every instruction that invites the behaviour: rules telling agents to tighten, polish, modernise, rewrite, unify, restyle or "improve" existing text, layouts or art; auditors allowed to patch wording in bulk; asset rules that allow replacing existing files; "cleanup" permissions with no boundary.
2. Change them so that:
   - existing player-facing text, interface layouts, art, audio and working mechanics are changed only when the owner's request names them;
   - auditors report findings on existing content and patch only what the current task created;
   - a restore is always exact, from history;
   - new art never replaces or repoints existing art;
   - report events have at most 4 options; large numbers are shortened with k; migration and famine decisions carry no political power cost;
   - bulk edits across more than a handful of existing keys or files need the owner's explicit request.
   Add one short section to `AGENTS.md` (canonical in `CLAUDE.md`) stating these as hard rules, and adjust the skills and agent definitions that contradict them. Keep each skill within its size ceiling (`python .tools/sync/sync_read_limits.py --check`), and regenerate the mirrors with `python .tools/sync/sync_agents.py` followed by `--verify`.
3. Do not put event-specific content in skills.
4. `docs/plans/guardrails_2026-10-13.md`: each instruction changed, before and after, and why.

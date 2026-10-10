# Event 32 decision and mission prompt

## Role

Audit, and patch within scope, the Event 32 decision category, missions, target selection, emergency actions, and the SCN-015 wrapper.
The category and missions are implemented in source; this prompt is for review rounds and the remaining items, not a fresh build.

Read first:

- part 5 of this package (owning section for every action, phase, cost and mission)
- part 2 Player-facing value budget, part 3 for operation rules, part 4 for evolution actions, part 6 for AI
- `docs/plans/032_missiles_plans/agent_decisions_2026-10-04.md` and `032_site_work_implementation_2026-10-09.md` for accepted implementation decisions
- `CLAUDE.md`, `chaos-redux-decisions-missions` and `chaos-redux-events`

## Review checklist

- Phase budget: three to five primary decisions normally, six at most, one to three active missions (part 5, Decision visibility budget).
- Every spendable action has at most four cost types, real costs, a cooldown or cap that prevents farming, and the same ability and payment checks for human and AI.
- Obsolete and invalid actions hide; stale targets, sites, operations, missions and emergency actions clean up when their country, state, war, evolution or incident becomes invalid (part 5, Decision cleanup).
- Missions auto-complete on a provable objective, never ask for a second payment click, and have distinct failure paths.
- Requirement tooltips state real conditions in plain words; implementation-only checks sit in hidden triggers with a custom tooltip (CLAUDE.md section 2).
- Reserve and payload accounting stays exact across preparation, cancellation, launch, failure, drift, capture, removal and reload.
- No action exposes an internal value that the part 2 value budget keeps hidden.
- Rejected options stay out: changing the participating site or preparation speed of a prepared operation, retargeting a retaliation, and diplomatic transfer of a captured site.

## Open design items

The README open questions on Inspect the Incident and the human-facing special-payload policy are `unresolved`.
Report evidence about them; do not change them without acceptance.

## Output

Patch only local defects inside the surface (wrong cleanup, missing tooltip, broken gate, unsafe AI weight).
Broad gaps go to a plan under `docs/plans/032_missiles_plans/`.
Write one handoff with changed files, identifiers, meaningful checks and remaining risks.
Weighted changes route through `chaosx_ai_probability_auditor` with the named scenarios; MCP probability routes are currently blocked, so give source-derived calculations and label them as such.

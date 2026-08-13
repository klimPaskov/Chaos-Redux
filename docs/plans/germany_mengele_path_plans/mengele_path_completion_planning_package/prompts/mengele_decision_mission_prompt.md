# Mengele decision and mission prompt

Use this after the main coding pass touches Germany Mengele decisions or missions.

Read `chaos-redux-decisions-missions`, `chaos-redux-events`, and the relevant repository files.

Audit and patch small local issues in:

- `germany_final_solution_category`.
- `germany_tibet_expedition_category`.
- Directorate civil-war decisions.
- Clone-network decisions, including hidden host offers and activation ledger decisions.
- Any related reveal, cleanup, review, purge, truce, reclaim, or evidence decisions.

Required checks:

- Categories appear only when meaningful actions exist.
- Hidden decisions have reveal and hide logic.
- Costs fit actions and avoid political-power-only button stores.
- AI avoids impossible targets and invalid routes.
- Tibet decisions cancel safely after ideology change, expedition failure, lost access, invalid Holy Realm state, or path closure.
- Clone-network decisions do not duplicate host markers, select dead countries, select invalid majors, or bypass network requirements.
- Cleanup removes obsolete flags, variables, decisions, and missions after closure, civil-war outcome, Directorate defeat, or world-end launch.
- Tooltips are clear, short, and free of raw trigger walls.

Write a subagent handoff under the discovered plan folder and list every changed decision id, before and after behavior, validation performed, and remaining risks.

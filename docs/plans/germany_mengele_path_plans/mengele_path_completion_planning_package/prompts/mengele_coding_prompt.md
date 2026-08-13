# Mengele coding prompt

Implement the finish pass for the Germany Mengele path using this package as the handoff.

Start by reading:

- `AGENTS.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-super-events/SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.
- `.agents/skills/chaos-redux-focus-trees/SKILL.md` if `mengele_clone_army_focus_tree` is touched.
- Offline Paradox wiki and vanilla documentation required by `AGENTS.md` for events, decisions, ideas, localisation, on actions, scopes, effects, triggers, focus trees, scripted localisation, GUI, and audio surfaces you touch.

Then read this package:

- `specs/current_implementation_map.md`.
- `specs/mengele_path_completion_spec.md`.
- `specs/mengele_super_event_acceptance_criteria.md`.
- `specs/mengele_improvement_loop_addendum.md`.
- `matrices/mengele_event_inventory_matrix.md`.
- `matrices/mengele_test_matrix.md`.

The current source says this is a Germany gameplay chain in `events/germany_mengele.txt`, not a random-event pool entry. Verify that in the repo before editing. If the repository disagrees, document the actual file map and adapt the plan without inventing new surfaces.

Finish all live `germany_mengele.*` events and the connected effects, triggers, constants, decisions, ideas, AI, focus tree, special projects, opinion modifiers, localisation, assets, super-events, docs, and spreadsheet surfaces.

Priority work:

1. Verify every event in the namespace, including `.1`, `.10` through `.14`, `.17`, `.20`, `.22`, `.23`, `.24`, `.37`, `.38`, `.40`, `.120`, `.121`, and any additional repo events.
2. Verify camp and genocide-crisis integration. Hidden deaths and internal pressure can grow before exposure, but external condemnation must come through discovery, survivor evidence, exposed records, or equivalent concrete evidence.
3. Finish decision and mission surfaces with meaningful costs, AI, valid targets, phase visibility, cooldowns, and cleanup.
4. Finish the Angel Directorate super-event. Replace default art or verify final art, research quote and button text, validate audio, wire settings-aware playback, and update docs.
5. Verify the `Angelic World Order` world-end path and the `Aryan Supremacy` variant if live.
6. Run the improvement-loop pass. Resolve the addendum, queue it with a reason, reject it with a reason, or promote it into specs before completion.
7. Run localisation, decision, focus, country package, documentation, spreadsheet, and completion audits as relevant.
8. Test the path through meaningful scenarios and record evidence.

Do not claim completion while placeholders, default super-event art, missing audio docs, missing localisation keys, dead decisions, untested route gates, unverified assets, unresolved improvement addenda, or stale docs remain.

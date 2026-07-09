# Mengele path completion planning package

This package converts the current implemented-source notes into a handoff for finishing the Chaos Redux Germany Mengele path.

The requested goal is to finish the Mengele super-event, inspect and complete every connected event, test the route, improve the path through the improvement-loop process, and keep iterating until the feature is actually complete.

The uploaded files describe the implementation, but they are not the full Chaos Redux repository. This package does not claim that gameplay files compile, that the route was tested in HOI4, or that the super-event is finished. It gives the implementation agent a structured spec, prompts, acceptance criteria, and validation plan.

## Critical source findings

- `germany_mengele.md` says this is a Germany gameplay chain in `events/germany_mengele.txt`, not a Chaos Redux random-event pool entry.
- The path begins from normal HOI4 triggers when fascist Germany controls Auschwitz after 1940.06.13.
- Auschwitz is the shared Kielce-state node, state `88` and province `9412`.
- The path has three connected layers: Auschwitz Experiments authorization, hidden Mengele autonomy and the Angel of Death civil war branch, and the Final Solution decision layer with the Tibet Expedition branch.
- The docs name a registered `Angel Directorate` super-event image and audio package, but they also say the currently registered image contains default super-event art. The implementation agent must replace or verify the final art before completion.
- The docs also name a later `Angelic World Order` world-end scenario, with `Aryan Supremacy` as a title variant when the Aryan branch is active.
- The CSV catalogs do not contain a standalone `Mengele` row. The chain must be documented and tested through the Germany path and the connected Holy Realm or genocide-crisis surfaces instead of being treated as a normal random event row.

## Package contents

- `source_processing_manifest.md`: every uploaded source file read, with hashes, line counts, and source conclusions.
- `specs/current_implementation_map.md`: what the uploaded docs say is currently implemented.
- `specs/mengele_path_completion_spec.md`: implementation-ready completion spec.
- `specs/mengele_super_event_acceptance_criteria.md`: pass or fail criteria for the super-event surface.
- `specs/mengele_improvement_loop_addendum.md`: improvement-loop design pass for finishing the path without adding bloat.
- `prompts/mengele_goal_prompt.md`: compact goal prompt for the implementation agent.
- `prompts/mengele_coding_prompt.md`: detailed implementation prompt.
- `prompts/mengele_super_event_prompt.md`: super-event research and wiring prompt.
- `prompts/mengele_asset_prompt.md`: visual asset prompt.
- `prompts/mengele_decision_mission_prompt.md`: decision and mission prompt.
- `prompts/mengele_improvement_loop_prompt.md`: planner prompt.
- `prompts/mengele_audit_prompt.md`: final audit prompt.
- `prompts/mengele_achievement_prompt.md`: achievement decision prompt.
- `matrices/`: event inventory, completion surface map, subagent route map, and test matrix.
- `research/`: catalog search notes and historical sensitivity notes.
- `handoff/`: implementation order and completion report template.

## Recommended repository destination

Because this chain is not a standalone catalog event, place the extracted package under a plans path after the coding agent verifies the final repository slug. A safe first destination is:

```text
docs/plans/germany_mengele_path_plans/mengele_path_completion_planning_package/
```

If the repo already has a more specific accepted plan folder for this chain, use that folder instead and record the move in the completion report.

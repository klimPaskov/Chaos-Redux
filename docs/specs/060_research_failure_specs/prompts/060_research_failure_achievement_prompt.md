# Event 60 achievement implementation prompt

Implement the two Event 60 achievements described in `specs/060_research_failure_spec_part_6_presentation_assets_achievements.md`.
Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the current Chaos Redux achievement registry, existing achievement tracking precedents, and the full Event 60 pack before editing.
Keep the single root achievement registry and its established unique ID policy.

## Achievement 1

Working ID: `research_failure_from_first_principles`.

Track one human-controlled qualifying incident at Scientific Dark Age or Knowledge Collapse severity.
Record the exact incident sequence, initial lost-node set, deadline, and later node closure.
Unlock only after institutional reconstruction is complete and every technology from that qualifying set has been recovered through ordinary research within the final balanced time limit.

Disqualify the run when a lost node is directly restored by Gift from Scientists, Brilliant Scientist, donor union grants, Kruger direct restoration, console or debug effects, or any Event 60 foreign action that directly grants a lost technology.
Allow general research bonuses, ordinary research sharing, production licences, archive-based speed support, specialist return, and foreign assistance that does not set the technology directly.

The tracking must distinguish ordinary research completion from direct grants through an explicit Event 60 receipt or owner callback.
Do not infer the source from timing alone.

## Achievement 2

Working ID: `research_failure_last_laboratory`.

Track one human-controlled Knowledge Collapse incident.
Require the country to remain at the Event 60 one-slot floor for the final balanced minimum exposure, restore the incident's full pre-failure slot ceiling, reach Scientific Capacity 100, complete an institutional settlement, and recover the final balanced majority of the incident's lost nodes.

Disqualify the run for Emergency Kruger Mandate, capitulation during the unresolved institutional crisis, debug completion, slot duplication, or an effect that bypasses required institute projects.
The one-slot timer, restored-slot receipts, pre-failure ceiling, settlement completion, recovered ratio, and disqualifiers must survive save and reload.

## Shared requirements

- Final names and descriptions must follow the writing direction in the specification and must not expose internal flags, sequence IDs, percentages that are still under tuning, or implementation history.
- Create visible and locked-state localisation according to the current achievement UI precedent.
- Use the two approved achievement art packages and root-only DDS naming convention.
- Achievement source icons must be distinct from decision, idea, and mission art.
- Add one-time unlock guards.
- Do not let repeat firings replace an active qualifying incident with an easier one.
- Define civil-war, annexation, tag-change, and player-control behavior explicitly.
- Console and test-country setup must never unlock either achievement.
- Add acceptance tests for every disqualifier, deadline edge, direct-grant source, save and reload state, and repeated incident.

Report exact achievement IDs, registry entries, localisation keys, tracking flags or variables, call sites, icon paths, test results, and unresolved balance choices.

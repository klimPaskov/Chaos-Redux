# Event 018 Resources Found Repo Explorer Prompt

Spawn `chaosx_repo_explorer` with `fork_context=false`.

Parent task:
Map the implementation surfaces for Event 018 `Resources Found` before any gameplay edit. The current source spec is under `docs/specs/018_resources_found_specs/`. The event creates a repeatable resource discovery, a field management decision system, Evolutions I through IV, the Cave Host nonhuman country, Cave Host resource-based army capacity, a Cave Host focus tree, super-events, achievements, assets, and a world-end branch.

Explicit constraints:

- Preserve baseline discovery. A random valid state gains around 100 of one random resource and the owner gets a popup.
- Preserve closure before Evolution IV. Closing the field sacrifices event-added resources and prevents Cave Host.
- Preserve Cave Host army rule. No manpower, no equipment, automatic divisions from controlled resources, one division per 10 total resources, cap 10 per non-origin state, origin starting army capped around 30.
- Preserve economy positive cluster and medium severity.
- Do not implement code. This is read-only exploration.
- Do not use broad exploration as a ritual. Search targeted ids, systems, and patterns.

Files to read first:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `docs/specs/018_resources_found_specs/`

Search targets:

- Event id 18 and namespace `chaosx.nr18`
- Event registration arrays and default enable allowlist
- Existing random valid state selection helpers
- Existing state resource add and remove syntax
- Existing state memory and event target cleanup patterns
- Existing decision category and scripted GUI patterns
- Existing event-log actor and evolution logging patterns
- Existing world threat source framework
- Existing nonhuman classification triggers
- Existing event-created country packages and focus-tree loading patterns
- Existing super-event slot, image, audio id, music table, and settings-aware playback patterns
- Existing achievement registration patterns
- Existing asset folder and GFX conventions

Required report path:

`docs/plans/018_resources_found_plans/subagent_handoffs/018_resources_found_repo_explorer_handoff.md`

Required output sections:

- Scope read
- Primary findings
- Relevant files table
- Existing Chaos Redux patterns
- Vanilla or approved reference precedents
- Likely edit order for the parent
- Validation checks
- Risks and blockers
- Recommended next action

Special questions to answer:

1. How can a state resource deposit be added and later removed safely for a specific event-added amount.
2. Which existing helper patterns should be reused for random state selection, event targets, and cleanup.
3. Which exact files own Event Details, evolution rows, event history actor mapping, and event enable defaults.
4. Which exact files own super-event image, quote, title, button, audio id, music asset, and music table entries.
5. Which exact patterns should be used for a nonhuman event-created country that does not use manpower or equipment.
6. Which exact focus-tree file pattern should be used for an event-created hostile country.
7. Which task-specific validation checks the implementation agent should run after editing.

## Canonical continuation addendum

The public GitHub exploration handoff already maps likely paths and old Event 018 behavior. Your local repo exploration should verify or correct that map against the actual working tree, offline wiki pages, vanilla docs, and local helper patterns. Do not assume the public GitHub branch exactly matches the user's local repository.

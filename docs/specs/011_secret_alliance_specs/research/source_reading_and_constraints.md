# Source Reading and Constraints

Event ID: 011
Event name: Secret Alliance

## Uploaded project files read

All files uploaded into `/mnt/data` for this task were loaded and inspected for the planning pass:

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `chaos-redux-event-assets.md`
- `chaos-redux-event-planning.md`
- `chaos-redux-events.md`
- `chaos-redux-frame-animation.md`
- `chaos-redux-improvement-loop.md`
- `chaos-redux-subagents.md`
- `chaos-redux-super-events.md`
- `hoi4-decisions-missions.md`
- `hoi4-focus-trees.md`
- all `chaosx_*.toml` subagent files
- `chaos_redux_events_catalog.csv`
- `chaos_redux_clusters_catalog.csv`
- `chaos_redux_scenarios_catalog.csv`

The event catalog row for Event 011 currently lists `Secret Alliance`, `Reserved`, `Minor Fire-Once`, and `To Be Reworked`.

## Constraints that affected this package

The uploaded files were available. A full Chaos Redux repository checkout, the offline Paradox wiki snapshot, and vanilla Hearts of Iron IV documentation were not mounted in this environment. The package therefore avoids claiming repo implementation details that were not visible here. Implementation agents must still perform the required repo, vanilla, and offline wiki inspection before editing gameplay files.

Project subagent instruction files were available and used as role guidance. A live subagent runner was not exposed in this environment, so this package includes explicit subagent routing prompts instead of claiming that those agents executed patches or research.

The event planning skill requires final planning output as a zip package with spec files, prompt files, research notes, matrices, and a goal prompt under 4000 characters. This package follows that shape.

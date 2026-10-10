# Event 31 supplied-source audit and limitations

Disposition: `superseded` for current facts by [the package README](README.md) and [the current completion audit](../../plans/031_random_terror_plans/subagent_handoffs/031_current_completion_audit_20261007.md).

This file records what the original planning pass in August 2026 could read.
Its source list is kept as historical evidence.
Its limitation and blocker lists described a planning environment without the repository, the wiki, the game files or the HOI4 tools.
Those limits no longer hold: the event is implemented in the repository and later work used the local references and tools, so the lists are reduced to the summary below.

## Supplied source coverage

The complete supplied bundle was accessed and processed before the specification was written.

The bundle contained 41 readable source files with 1,073,741 bytes and 14,461 lines.

Every supplied Markdown file, TOML file, CSV export, the Event 31 brief, and every extracted subagent definition was decoded and read.

The original `subagents.zip` was extracted and its 20 TOML definitions were included in the source review.

The following project sources were included:

- `AGENTS(7).md`
- `CHAOS_REDUX_MECHANICS(7).md`
- `Pasted markdown(3).md`
- `chaos-redux-3d-model-pipeline(3).md`
- `chaos-redux-comfyui(2).md`
- `chaos-redux-debug-playtest(2).md`
- `chaos-redux-decisions-missions(3).md`
- `chaos-redux-event-assets(7).md`
- `chaos-redux-event-planning(20260813-152954).md`
- `chaos-redux-events(8).md`
- `chaos-redux-focus-trees(3).md`
- `chaos-redux-frame-animation(8).md`
- `chaos-redux-improvement-loop(8).md`
- `chaos-redux-subagents(8).md`
- `chaos-redux-super-events(7).md`
- `chaos_redux_clusters_catalog(3).csv`
- `chaos_redux_events_catalog(3).csv`
- `chaos_redux_scenarios_catalog(3).csv`
- `chaosx_dynamic_effects.md`
- `chaosx_dynamic_triggers.md`
- `config.toml`
- all 20 extracted subagent TOML definitions

The event catalog export contained 182 event rows.

Event 31 was listed as `Random Terror`, `Minor Repeatable`, with status `Unavailable`, no cluster assignment, and no completed evolution, scenario, or world-end catalog fields.

The scenario export contained IDs through `SCN-013`, with `SCN-004` absent from that export while the mechanics guide still reserves it for Final Silence.

The highest visible scenario ID was `SCN-013`, which supports `SCN-014` as the proposed Event 31 scenario ID.

The cluster export contained active numeric IDs through `8`, which supports `9` as the proposed future Internal Fracture cluster ID.

Those planning-time allocation directions are `superseded` by the parent's 2026-10-07 occupancy-based identity correction.
Global Jihad keeps its existing `SCN-016` identity; `SCN-014` belongs to Fallout.
Internal Fracture reserves raw `event_cluster_id` `22` as a separate optional proposal; raw cluster `9` belongs to National Breakthroughs, and Event 031's current catalog membership remains Domestic Unrest `16`.
See [the shared identifier registry](../shared_identifier_registry.md) and [its JSON ledger](../shared_identifier_registry.json); the reservation does not approve the cluster design or change current membership.

## Project contracts applied

The package applies the event planning, event implementation, decision and mission, focus tree, asset, portrait, frame animation, super-event, improvement loop, subagent, mechanics, dynamic effect, dynamic trigger, and completion standards.

The design preserves the distinction between ordinary baseline stages and evolutions.

The design keeps the response category compact, limits visible values, uses concrete costs, maps AI behavior, defines country forces and reinforcement, avoids generic focus content, includes achievements, and provides separate implementation prompts.

The design treats the CSV files as read-only exports.

No CSV was edited.

## Planning-time limits, resolved

The planning pass had no access to the repository, the offline wiki, the installed game and documentation, the workbook, the HOI4 MCP tools, the live game, or subagent execution.
The improvement loop was therefore run manually.
Every identifier the package proposed was later checked against the repository during implementation, and the identity corrections (`SCN-016`, cluster reservation `22`, playback IDs `114` and `115`) are recorded in the README and the shared identifier registry.

## Simplification statement

The design was not shortened into a popup-only event, a generic modifier package, a one-route country, a political power store, or a scripted GUI mockup.

No requested evolution, territorial state, manual scenario, world-end branch, Cannibalism interaction, AI layer, asset family, achievement surface, or documentation surface was omitted from the design.

The deliberate absence of a custom 3D unit and dedicated mechanic window is an anti-bloat design decision supported by the project skills.

Existing unit types and a compact decision category can deliver the event's mechanics with lower maintenance cost and clearer play.

## Implementation blockers

The original twelve blockers were cleared or carried into the implementation record.
Open work is tracked only in the part status sections, the README and the completion audit.

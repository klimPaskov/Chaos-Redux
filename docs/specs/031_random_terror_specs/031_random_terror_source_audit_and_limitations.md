# Event 31 supplied-source audit and limitations

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

These ID proposals remain subject to the authoritative workbook and live registry.

## Project contracts applied

The package applies the event planning, event implementation, decision and mission, focus tree, asset, portrait, frame animation, super-event, improvement loop, subagent, mechanics, dynamic effect, dynamic trigger, and completion standards.

The design preserves the distinction between ordinary baseline stages and evolutions.

The design keeps the response category compact, limits visible values, uses concrete costs, maps AI behavior, defines country forces and reinforcement, avoids generic focus content, includes achievements, and provides separate implementation prompts.

The design treats the CSV files as read-only exports.

No CSV was edited.

## Sources that were not present in the supplied bundle

The live Chaos Redux repository was not mounted in this environment.

The offline Paradox wiki snapshot was not present.

The installed Hearts of Iron IV game files and vanilla documentation were not present.

The authoritative event catalog XLSX workbook was not present.

The HOI4 MCP server was described in the supplied configuration, but no `hoi4.*` tool surface was available in this chat environment.

The Windows desktop, game executable, debug shortcut, current runtime logs, and live game were not available.

The project subagent execution interface was not available.

The supplied subagent definitions were fully read and converted into bounded routing prompts, but the subagents were not actually spawned.

The improvement loop was therefore performed manually against the same planning contract.

## Consequences of those limits

This package is a complete design specification.

It is not repository implementation evidence.

It does not claim that a tag, sprite, super-event slot, sound ID, country carrier, collection, state trigger, map mode registration, focus navigation token, or scenario registry ID is free in the live project.

The implementation agent must verify every proposed identifier against the repository before use.

The implementation agent must inspect the offline wiki, current vanilla documentation, vanilla precedents, Chaos Redux precedents, and required MCP surfaces before editing code.

The implementation agent must use `hoi4.event_inspect`, event render and compare tools, focus inspect and render tools, probability tools, GUI tools when applicable, and map tools when applicable.

The implementation agent must run the relevant project subagents with `fork_context=false` and context-complete prompts.

The implementation agent must update only the authoritative XLSX workbook, then run the repository CSV exporter.

## Simplification statement

The design was not shortened into a popup-only event, a generic modifier package, a one-route country, a political power store, or a scripted GUI mockup.

No requested evolution, territorial state, manual scenario, world-end branch, Cannibalism interaction, AI layer, asset family, achievement surface, or documentation surface was omitted from the design.

The deliberate absence of a custom 3D unit and dedicated mechanic window is an anti-bloat design decision supported by the project skills.

Existing unit types and a compact decision category can deliver the event's mechanics with lower maintenance cost and clearer play.

## Required implementation blockers to clear

Before code can be called complete, the implementation pass must clear these blockers:

1. Confirm the Event 31 current source, namespace, registration state, and default disabled state.
2. Confirm an available event-owned country carrier collection large enough for maximum scenario coverage.
3. Confirm the proposed `SCN-014` ID and proposed Cluster `9` ID against the authoritative workbook and live registries.
4. Confirm the Event 31 world-threat source flag name and register it in the shared aggregate.
5. Confirm the special chaos country classifier update and keep all Event 31 actors outside the actual nonhuman classifier.
6. Confirm the event-owned state map mode pattern and exact update transaction.
7. Confirm the event log prefire actor preparation pattern for a multi-country global repeatable event.
8. Confirm the shared focus tree loading and Focus Navigation pattern for dynamic carriers.
9. Confirm all asset consumers, sizes, paths, and sprite identifiers against current references.
10. Confirm a unique super-event slot, audio ID, image sprite, and public world-end registry row.
11. Run the probability audit before and after every weighted implementation change.
12. Run the event completion audit after all source, asset, documentation, catalog, and AI surfaces are present.

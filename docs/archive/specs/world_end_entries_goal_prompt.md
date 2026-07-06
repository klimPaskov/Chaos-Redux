/goal Implement clickable world-end scenario entries in the Chaos Redux Event Details window and update the event workflow skill so future agents wire this surface by default.

Before editing, read and process all project source files fully: AGENTS.md, CHAOS_REDUX_MECHANICS.md, every Chaos Redux skill, every subagent TOML, and the event, cluster, and scenario catalog CSVs. Inspect live repo patterns and relevant HOI4 wiki, vanilla GUI, scripted GUI, localisation, trigger, effect, and data-structure references.

Add a World End Scenarios section to the Event Details window below the evolution preview box. This is a public catalog surface for terminal branches attached to the selected event. Show one row per public world-end scenario owned by that event. One terminal branch means one row. Several branches mean several rows. Hidden easter egg world-end scenarios stay omitted from this surface and from its controls.

Each row must be clickable. Clicking a row opens or updates a details view for that scenario, using existing Event Details row behavior. The details must describe the scenario premise and terminal state in player-facing terms. They must not expose raw effects, hidden variables, or easter egg content. Rows should show title, owner event, enabled state, and a short status where useful.

Add an enable or disable checkbox to every public world-end entry. Use the same visual style and behavior as existing event toggles. Disabling a world-end scenario must make automatic world-end selection skip that terminal scenario. It must not disable the parent event or unrelated content. Multiple scenarios owned by one event must be independently toggleable.

Make the feature data-driven. Create or extend a world-end scenario registry with stable scenario id, owner event id, sort order, public or hidden visibility, default enabled state, scenario flag, related super-event id or visibility flag, title key, details key, and availability helper when needed. Use aligned arrays or helpers consistent with the Events, Evolutions, Clusters, and Triggerable Scenarios patterns.

Wire the needed surfaces in one pass: events-log effects for registry and row rebuild, scripted GUI events-log handlers for clicks and toggles, chaosx_events_log_popup.gui for layout, events-log scripted localisation for dynamic text, chaosx_gui_l_english.yml for labels, script constants when ids or sort values need central tuning, and the world-end selection helpers.

Update CHAOS_REDUX_MECHANICS.md and relevant docs/systems or docs/events files. Keep spreadsheet-facing world-end fields aligned when the workbook is in scope. Public docs, catalog rows, and Event Details text must omit hidden easter egg terminal branches.

Update the chaos-redux-events skill so this becomes part of normal event implementation. Add guidance that every event with a public terminal branch must register entries, details text, toggle state, row click behavior, super-event linkage, docs, and spreadsheet alignment in the same pass. Add that easter egg world-end scenarios stay out of public Event Details entries and disabled world-end scenarios are skipped by automatic selection.

Use subagents where useful: repo explorer for uncertain file maps, scripted system architect for registry helpers, localisation auditor for labels and dynamic text, skill maintainer or direct skill editing for the workflow update, and event completion auditor before claiming completion.

Acceptance criteria: public world-end entries appear below evolutions, entries open scenario details, toggles persist, disabled scenarios cannot be selected, multiple scenarios per event work, hidden easter egg scenarios stay hidden, world-end chaos rules and super-event linkage remain intact, layout is readable, docs and skill guidance are updated, and any simplification or blocker is reported clearly.

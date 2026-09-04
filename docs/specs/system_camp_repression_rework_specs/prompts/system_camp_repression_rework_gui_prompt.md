# Scripted GUI Prompt: System Camp Repression Rework

Use this prompt after the shared country-kit decisions are implemented or during the same implementation pass when the required GUI work is in scope.

Read:

- `specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` as the current UI source of truth
- `specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md`
- the existing Chaos Redux scripted GUI patterns
- offline Paradox wiki pages for Interface Modding and Scripted GUI Modding
- vanilla GUI and scripted GUI documentation

Build the decision-category header and the full player-opened `repression_ledger_window` described in Part 6. Retain only the existing window, panel, navigation-mark, and action identifiers that the parent verifies in the runtime source, while the player-facing design uses the new navigation labels.

Use the player-facing title `Repression and Camps` in a 960x600 dark vanilla HOI4 framed window with native tiled panels and buttons. The left navigation labels are Situation, Territories, Sites, Policy, and Accountability. Do not use parchment cards, copied game textures, or a detached global action bar.

Required display values:

- Situation: three compact panels with civilian-loss pressure as the primary consequence, administrative strain as supporting context, and surviving evidence with its warning state; the harm tooltip contains current civilian-loss pressure, the resistance band, and inspection or closure guidance, the strain tooltip contains current strain, labor contribution, and guards or quotas guidance, and no bounded state summaries appear here.
- Territories: a scrollable dynamic list over `camp_gui_pool_states` with up to 24 entries and six viewport rows, selected-row highlight, explicit empty state, and two-line location-name rows only; an empty list hides the right detail pane, a nonempty unselected list shows a neutral selection instruction, and a selected row shows the selected name and site type plus six context button slots with paired cost rows.
- Sites: a scrollable dynamic list over `camp_gui_active_site_states` with up to 24 entries and six viewport rows, selected-row highlight, explicit empty state, and two-line location-name rows only; an empty list hides the right detail pane, a nonempty unselected list shows a neutral selection instruction, and a selected row shows the selected name and site type plus six context button slots with paired cost rows.
- Policy: the active institution, current course, four existing directive panels, guard allocation, quota controls, and route-specific actions.
- Accountability: exposure or evidence, recorded Deaths total, and three closure or reform pressure rows.

Rules:

- Do not add chemical or biological killing-efficiency controls; preserve the evidence and consequence boundary in the accepted specs.
- Do not display deaths as an optimization table.
- Link exact deaths to the Chaos Meter Deaths tab or mention that the Deaths tab records totals.
- Give every button an equivalent decision or scripted effect that AI can use without the GUI.
- Rebuild display arrays only on open, after relevant decisions, and during the existing monthly active-site pulse.
- Clean selected pools, selected states, selected locations, and selected action variables when invalid.
- Reset the selected state after a Territories or Sites display-list rebuild, then restore it only when the player selects a row.
- Keep Territories and Sites actions in the selected-location details pane, keep country directives and guard or quota actions in Policy, and keep exposure or closure actions in Accountability.
- Keep detailed location context in the existing selected-state tooltip, and keep Territories and Sites list rows free of status columns, visible tables, and ledger columns.

Asset handoff:

- use native HOI4 tiled panel and button sprites for the 960x600 window;
- do not request or create custom replacement panel, card, background, copied-texture, status-sprite, or animation art;
- retain only parent-verified window, panel, navigation-mark, and action identifiers.

Report:

- GUI files changed.
- scripted GUI entries.
- scripted localisation keys.
- button ids and their AI equivalents.
- cleanup helpers.
- named MCP inspect/render/compare artifacts and unresolved diagnostics, when available.
- final report path: `docs/plans/system_camp_repression_rework_plans/repression_ui_redesign_2026-09-05.md`.

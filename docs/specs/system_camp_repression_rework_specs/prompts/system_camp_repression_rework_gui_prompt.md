# Scripted GUI Prompt: System Camp Repression Rework

Use this prompt after the shared country-kit decisions are implemented or during the same implementation pass if GUI work is in scope.

Read:

- `specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md`
- `specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md`
- the existing Chaos Redux scripted GUI patterns
- offline Paradox wiki pages for Interface Modding and Scripted GUI Modding
- vanilla GUI and scripted GUI documentation

Build the `Repression Ledger` working UI as a country decision category header first. Add the full scripted GUI window only if the header cannot show the required values clearly.

Required display values:

- country kit
- network phase
- reach
- active pool count
- output band
- population-loss consequence band
- stability strain
- resistance or subject pressure
- evidence band
- reform progress
- discovery state

Rules:

- Add chemical and biological killing-efficiency controls.
- Do not display deaths as an optimization table.
- Link exact deaths to the Chaos Meter Deaths tab or mention that the Deaths tab records totals.
- Give every button an equivalent decision or scripted effect that AI can use without the GUI.
- Rebuild display arrays only on open, after relevant decisions, and during the existing monthly active-site pulse.
- Clean selected pools, selected states, and selected action variables when invalid.

Asset handoff:

- request the GUI panel, pool card, warning frame, evidence seal, action button states, and reform progress bar assets from the asset prompt.
- animated warning or reform sprites are optional, but if implemented they must use real frame sheets and static fallbacks.

Report:

- GUI files changed.
- scripted GUI entries.
- scripted localisation keys.
- button ids and their AI equivalents.
- cleanup helpers.
- validation checks run.

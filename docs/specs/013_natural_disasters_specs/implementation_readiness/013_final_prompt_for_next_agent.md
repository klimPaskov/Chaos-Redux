# Final resume prompt for the next Event 013 implementation agent

Continue from the expanded Event 013 Natural Disasters planning package in `docs/specs/013_natural_disasters_specs/`. Use the third-pass implementation-readiness files before editing.

Current source files to read first:

- `research/004_final_improvement_loop_anti_bloat_closure.md`
- `implementation_readiness/013_closure_resume_packet.md`
- `implementation_readiness/013_acceptance_gate_matrix.md`
- `implementation_readiness/013_dependency_order_and_subagent_sequence.md`
- `implementation_readiness/013_validation_scenario_matrix.md`
- `implementation_readiness/013_simplification_blocklist.md`
- all source spec parts under `specs/`
- all matrices under `matrices/`
- all prompt files under `prompts/`

Do not continue from the old continuation prompt. It is superseded.

Core constraints:

- Implement Event 013 from scratch.
- Do not reuse old Natural Disasters logic.
- Do not reuse old Earth Earthquake logic.
- Event 046 remains an inactive unknown placeholder.
- Event 099 becomes a placeholder or a narrow bridge into Event 013 dust and sandstorm calls.
- Event 051 Heat Wave remains separate and Event 013 heat must not stack with it.
- One Event 013 firing creates one Event 013 history row, even when many delayed subevents fire.
- Disasters must be individually triggerable through a reusable dynamic system.
- Affected countries must reliably receive delayed reports and visible aftermath notifications.
- Baseline deaths and damage must matter.
- Evolution II scales harder with vulnerability and chained aftermaths.
- Evolution III can be massively destructive and uses abnormal map presentation for moving or multi-state systems.
- Localisation direction in specs is not final localisation.
- Super-event titles, quotes, remarks, slogans, lyric fragments, and audio choices require researched handoffs before final wiring.
- Achievements are difficult and non-trivial.
- Custom UI animation uses real frame-sheet assets with static fallbacks.

Recommended implementation order:

1. Map live repository files and precedents.
2. Build reusable scripted architecture and constants.
3. Implement one baseline vertical slice from disaster call to cleanup.
4. Expand ordinary families through the shared system.
5. Implement aftermath decisions, missions, active caps, partial success, and AI equivalents.
6. Add Evolution I and Evolution II.
7. Align Event 046, Event 051, Event 099, Natural Disasters cluster, and Disaster Barrage.
8. Add Evolution III abnormal controller and scripted GUI.
9. Produce assets and researched super-event packages.
10. Finish localisation, docs, spreadsheet alignment, and completion audits.

Completion rule:

Do not claim completion while any acceptance gate is missing. Report every simplification, missing asset, missing AI behavior, skipped meaningful validation, unresolved research package, or placeholder clearly.

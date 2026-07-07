# Event 013 Natural Disasters, closure resume packet

This packet continues from `research/004_final_improvement_loop_anti_bloat_closure.md`. It does not add new disaster concepts, new countries, new focus trees, or new world-end branches. It converts the closure handoff into a practical source-of-truth and implementation-readiness map for the next coding pass.

## Current source of truth

The accepted source design is the expanded package under `docs/specs/013_natural_disasters_specs/`.

| Source area | Use in the next pass | Completion meaning |
| --- | --- | --- |
| `specs/013_natural_disasters_spec_part_1_core.md` | Preserve the fresh Event 013 identity, the one-row log rule, the delayed sequence model, and the player loop. | Event 013 behaves as a repeatable disaster sequence container, not as a generic institution. |
| `specs/013_natural_disasters_spec_part_2_reusable_system.md` | Build the dynamic disaster call model, target resolution, warning model, impact ledger, and callback contract. | Other events can call a specific disaster family, target, severity, and policy package without copying family logic. |
| `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md` | Implement the broad family catalogue and the first-layer family playbooks. | Every family has distinct damage logic, warning behavior, aftermath pressure, and report direction. |
| `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md` | Build the normal aftermath category and notification behavior. | Affected countries receive visible reports and usable recovery actions after serious impacts. |
| `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md` | Wire baseline, Evolution I, Evolution II, Evolution III, cluster behavior, and Disaster Barrage. | Severity and sequence breadth evolve without creating extra Event 013 history rows or a world-end branch. |
| `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md` | Drive report, news, super-event, achievement, and asset handoffs. | Presentation supports disaster identity without writing final unresearched localisation in the spec. |
| `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md` | Use AI, balance, exploit, and acceptance rules as the final readiness gate. | The event is not complete until AI, deaths, damage, reporting, cleanup, and documentation all align. |
| `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md` | Treat family mini-specs as the family-level acceptance criteria. | Every family has warning decisions, card fields, AI priorities, report direction, news direction, modifiers, and chain routes. |
| `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md` | Build the abnormal moving-disaster map and static fallbacks. | Evolution III moving disasters have a readable map, cards, animations, path previews, and cleanup. |
| `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md` | Build staged recovery decisions, missions, active caps, partial success, failure, and foreign relief. | Recovery is a living decision layer rather than a flat button list. |

## Non-negotiable design rules carried forward

- Treat Event 013 as a fresh source design.
- Do not preserve or patch old Natural Disasters logic.
- Do not reuse old Earth Earthquake logic.
- Event 046 remains an inactive unknown placeholder.
- Whole-earth rupture belongs only inside Event 013 Evolution III.
- Event 099 becomes a placeholder or narrow bridge into Event 013 dust and sandstorm calls.
- Event 051 Heat Wave remains separate and must not stack with Event 013 heat calls.
- One Event 013 firing creates one Event 013 history row, even if many delayed subevents fire.
- Every serious affected country receives a delayed report and a visible aftermath notification.
- Disasters are individually triggerable through one reusable dynamic system.
- Deaths and building damage must matter at baseline and scale harder at later evolutions.
- Evolution III can cause massive destruction when the family fits.
- Localisation remains direction-only in planning files.
- Super-event titles, quotes, remarks, slogans, lyric fragments, and audio choices remain blocked until researched.
- Achievements stay difficult and non-trivial.
- Custom UI and animation plans stay frame-sheet based with static fallbacks.

## What not to reopen

The closure pass already rejected broad expansion into new countries, focus trees, separate family GUIs, family-level super-event spam, and a terminal world-end branch. Do not reopen those areas unless the user asks for a specific new design surface.

## What the next agent should do first

1. Inspect the live repository, offline wiki pages, vanilla documentation, and existing Chaos Redux patterns.
2. Map the exact files for event script, random event registration, scripted effects, scripted triggers, script constants, on actions, decisions, categories, ideas or modifiers, GUI, GFX, localisation, scripted localisation, event logs, scenarios, clusters, docs, assets, achievements, and spreadsheets.
3. Spawn or perform a narrow scripted-system architecture pass before duplicating family damage, report, or aftermath logic.
4. Build the reusable disaster engine before implementing large family content.
5. Implement one baseline vertical slice from call to warning to impact to report to aftermath to cleanup to validate the contract.
6. Expand family content only after the baseline vertical slice proves the system can carry one-row logging, delayed reports, affected-country notifications, and Deaths-system integration.
7. Add Evolution II and Evolution III after the ordinary family controller is stable.
8. Build abnormal GUI and super-event packages only after the abnormal controller has real state to display.

## Stop condition for planning

Planning can stop. The next useful work is implementation, asset production, super-event research, and audit. A further planning pass should only happen if implementation discovers a concrete gap that the current specs do not answer.

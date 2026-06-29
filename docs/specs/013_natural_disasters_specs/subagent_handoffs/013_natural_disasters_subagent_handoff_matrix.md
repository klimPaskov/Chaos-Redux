
# Event 013 subagent handoff matrix

This matrix translates the provided subagent roles into concrete Event 13 handoffs. It does not claim that subagents have already implemented anything.

| Subagent | Use for Event 13 | Required output |
| --- | --- | --- |
| chaosx_repo_explorer | Use at implementation start if the exact existing event, cluster, scenario, death-system, GUI, and placeholder event files are unclear. | Repo map, touched files, vanilla precedents, edit order, validation plan. |
| chaosx_scripted_system_architect | Use before implementing target selection, sequence scheduling, damage helpers, death helpers, recovery ledgers, and cluster member slot helpers. | Helper map, constants plan, event target plan, cleanup plan, call sites, validation notes. |
| chaosx_decision_mission_auditor | Use after Natural Disaster Recovery category and missions are implemented. | Audit or local patch covering costs, AI, cleanup, mission quality, duplicate risks, exploit risks, and tooltip clarity. |
| chaosx_localisation_auditor | Use after event, decision, GUI, event detail, cluster detail, scenario, achievement, and super-event text is written. | Missing key list, duplicate key list, dynamic text fixes, wording mismatch fixes. |
| chaosx_icon_artist | Use for decision, category, idea, state modifier, GUI small marker, and achievement icons. | Source PNGs, processed PNGs, DDS files, manifest, gfx handoff, contact sheet. |
| chaosx_generated_event_art | Use for fictional or period-documentary report, news, super-event, and GUI panel art. | Source PNGs, processed previews, DDS files, manifest, gfx handoff. |
| chaosx_asset_source_researcher | Use only if real archival disaster imagery is selected for report, news, or super-event images. | Source files, source URLs, license notes, processed PNGs, DDS files, manifest, handoff. |
| chaosx_super_event_text_researcher | Use if the optional Evolution III super-event is implemented. | Quote candidates, selected quote, source confidence, button remark candidates, selected remark, copyright notes. |
| chaosx_super_event_audio_researcher | Use if the optional Evolution III super-event is implemented. | Licensed or public domain audio candidate, final ogg, source and license documentation, wiring handoff. |
| chaosx_event_completion_auditor | Use before final completion claim. | Spec versus implementation audit, missing surfaces, simplifications, validation gaps, blockers. |
| chaosx_spreadsheet_doc_worker | Use after final in-game wording exists. | Workbook update for Event 13 details, evolutions, cluster, and scenario rows using exact in-game wording. |
| chaosx_documentation_curator | Use after several implementation passes or subagent handoffs. | Source-of-truth map, superseded docs, plan dispositions, resume packet if needed. |
| chaosx_focus_tree_auditor | Not expected. Event 13 creates no focus trees. Use only if implementation unexpectedly adds focus content. | Focus audit if focus content exists. |
| chaosx_country_package_auditor | Not expected. Event 13 creates no countries. Use only if implementation unexpectedly changes country packages. | Country package audit if country content exists. |
| chaosx_improvement_loop_planner | Use only after a major implementation tranche if the recovery or GUI loop still feels shallow. | Expansion addendum or closure handoff. |
| chaosx_skill_maintainer | Use only if implementation reveals a reusable hazard or scheduler workflow missing from skills. | Skill update or blocked report. |

## Handoff path expectation

Subagent patch handoffs for this event should go under:

`docs/plans/013_natural_disasters_plans/subagent_handoffs/`

Spec source files stay under:

`docs/specs/013_natural_disasters_specs/`

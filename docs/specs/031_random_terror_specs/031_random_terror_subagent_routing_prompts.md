# Event 31 Random Terror subagent routing

## Shared rule

Spawning, isolation and role boundaries follow [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).
Each prompt is self-contained: it carries every path, constraint, prior decision, current implementation state and allowed file scope the role needs, and it inherits no parent conversation.

The parent keeps final integration, validation, documentation, workbook alignment, commits and completion claims.
Handoffs go under `docs/plans/031_random_terror_plans/subagent_handoffs/`, and planning addenda under `docs/plans/031_random_terror_plans/`.
Do not let two patch-capable agents edit the same files at once.
Other sessions may be editing Event 31 files, so every prompt names the files it may touch.

## Routing table

| Role | Use for Event 31 | Give it | Not for |
| --- | --- | --- | --- |
| `chaosx_scripted_system_architect` | Chaos impact map guards and rolling cap, Deaths reason routing, famine and migration request helpers, terminal commit recheck | Parts 2, 8 and 10, the event documentation, the owner system docs | gameplay balance choices |
| `chaosx_ai_probability_auditor` | every changed weight, the named scenarios including `P11_chaos_feedback`, the four specialist findings in Part 9 | the AI scenario matrix, before and after sources | choosing balance targets or patching |
| `chaosx_decision_mission_auditor` | terminal access, hostage approach, scaled costs and maintained commitments | Part 3, the decision matrix, the decision prompt | GUI work |
| `chaosx_country_package_auditor` | forces, capitals, mergers, takeover, Supply Collapse rename | Part 5, the country matrix | focus layout |
| `chaosx_focus_tree_auditor` | Forge the Seal staged cores, route review, spirit count | Part 6 | country setup |
| `chaosx_localisation_auditor` | new event options, renamed spirit, Deaths cause lines, in-world wording (D13) | Parts 1, 8 and 11 | workbook edits |
| `chaosx_icon_artist` | a Supply Collapse idea icon if the existing art reads as hunger, any Deaths cause icon | the asset prompt | wiring |
| `chaosx_portrait_creator` | recovering portrait provenance records | the asset prompt | new portraits, since all 45 exist |
| `chaosx_super_event_audio_researcher` | recovering the missing original audio downloads | the super-event prompt | new cues |
| `chaosx_spreadsheet_doc_worker` | applying `catalog_changes_pending.md` and running the exporter | the localisation it must match | CSV edits |
| `chaosx_documentation_curator` | keeping the overview, part status sections and plans folder in step | this package and the plans folder | gameplay files |
| `chaosx_event_completion_auditor` | the final completion audit | the whole package and the latest completion audit | patches |

`chaosx_event_ui_worker` and `chaosx_3d_model_pipeline` are not used: Event 31 has no dedicated GUI and no custom unit or model.
A proposal for either goes back to the user as a design change.

## Parent checklist

Before relying on a subagent output, the parent confirms that the prompt named its files and identifiers, the output stayed inside scope, the handoff lists files and IDs, probability changes have before and after evidence, plans carry a disposition, and open blockers stay visible in the completion report.

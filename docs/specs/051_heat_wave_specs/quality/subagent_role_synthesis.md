# Subagent Role Synthesis

## Execution note

The supplied archive contained twenty project subagent definitions. All were read in full. This environment did not expose the project's custom subagent-spawn runtime, so no subagent was actually invoked. Their role contracts were applied manually while writing this planning package.

The table below records how each role affected the design and which roles should be used during implementation.

| Subagent | Planning use in this package | Implementation disposition |
| --- | --- | --- |
| `chaosx_3d_model_pipeline` | Reviewed 3D ownership and hard gates | Not needed. Event 51 has no authorized custom 3D asset |
| `chaosx_ai_probability_auditor` | Defined fourteen named AI scenarios and inspect, sweep, compare requirements | Mandatory for weighted AI, MTTH, target, and random selection surfaces |
| `chaosx_asset_source_researcher` | Defined archival source families and period constraints | Use for real or archival non-portrait images |
| `chaosx_country_package_auditor` | Checked whether the event creates or transforms countries | Not needed unless implementation unexpectedly creates a country, which would require new design approval |
| `chaosx_decision_mission_auditor` | Applied cost, mission, visibility, cleanup, and exploit rules | Mandatory after decisions and missions exist |
| `chaosx_documentation_curator` | Used to separate source specs, prompts, evidence, and implementation docs | Useful after long implementation tranches to reconcile handoffs and permanent docs |
| `chaosx_event_completion_auditor` | Converted the rough brief into explicit completion and blocker checks | Mandatory before completion claim |
| `chaosx_event_ui_worker` | Reviewed the gate for dedicated event-owned GUI work | Not authorized. The event uses an ordinary decision category and map presentation |
| `chaosx_focus_tree_auditor` | Checked whether event-owned focus content was justified | Not needed. No focus tree is part of the accepted design |
| `chaosx_generated_event_art` | Defined nine generated documentary scene briefs and category art | Use for fictional and composite non-icon art |
| `chaosx_icon_artist` | Defined separate decision, state, idea, and achievement icon families | Use for all authorized icon and achievement work |
| `chaosx_improvement_loop_planner` | Applied playable-promise, pressure, consequence, AI, presentation, and anti-bloat review | Do not run another broad pass until this addendum is implemented, queued, or rejected |
| `chaosx_localisation_auditor` | Applied writing restrictions, dynamic fallback, tooltip, and cross-surface alignment rules | Mandatory after broad visible text exists |
| `chaosx_portrait_creator` | Checked portrait authorization and source-mode rules | Not needed. No character portrait is authorized |
| `chaosx_repo_explorer` | Performed a manual supplied-source map and identified live-repo gaps | Use once in the live repository because exact existing Event 51 files and owner touchpoints remain unknown |
| `chaosx_scripted_system_architect` | Defined event-owned helper families, owner APIs, generation proof, sparse processing, and shared-helper boundaries | Use early for lifecycle and adapter architecture |
| `chaosx_skill_maintainer` | Checked whether the task revealed a reusable workflow gap | No skill update is required from planning alone |
| `chaosx_spreadsheet_doc_worker` | Defined exact workbook alignment and export-only CSV rule | Use after implementation wording and status are final |
| `chaosx_super_event_audio_researcher` | Defined source, licensing, recording, conversion, and unique-track requirements | Mandatory for final Evolution III audio |
| `chaosx_super_event_text_researcher` | Defined quote candidate research and attribution requirements | Mandatory for final quote and button reference research |

## Parent responsibility

The implementation parent remains responsible for:

- accepting or rejecting this design
- live repository inspection
- final code and wiring
- subagent prompt completeness
- audit review
- cross-system integration
- map and probability evidence
- user-facing completion report

A subagent handoff cannot replace parent review or make the event complete by itself.

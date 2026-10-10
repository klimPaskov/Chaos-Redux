<!-- Derived from the .claude/agents frontmatter and .tools/sync/agent_profiles.json by python .tools/sync/sync_agents.py claude-map. -->
# Claude Code Subagent Map

Every file in `.claude/agents/` is a canonical Claude Code project subagent: Markdown with `name`, `description` and `model` YAML frontmatter plus a prompt body. Edit those files directly. Do not put README or other non-agent Markdown in that folder, because Claude Code loads every `*.md` there.

Other runtimes are generated from these definitions with `python .tools/sync/sync_agents.py`. Claude Code subagents run in an isolated context window, so the parent prompt must be fully explicit. Each subagent runs on the fixed model tier in the table and the parent may override it for one spawn.

| Identifier | Claude Code | Model | Authority |
| --- | --- | --- | --- |
| `chaosx_3d_model_pipeline` | `chaosx-3d-model-pipeline` | `sonnet` | asset / research (web) |
| `chaosx_ai_probability_auditor` | `chaosx-ai-probability-auditor` | `haiku` | read-only / plan-only |
| `chaosx_asset_source_researcher` | `chaosx-asset-source-researcher` | `haiku` | asset / research (web) |
| `chaosx_country_package_auditor` | `chaosx-country-package-auditor` | `haiku` | patch-capable |
| `chaosx_decision_mission_auditor` | `chaosx-decision-mission-auditor` | `haiku` | patch-capable |
| `chaosx_documentation_curator` | `chaosx-documentation-curator` | `haiku` | patch-capable |
| `chaosx_event_completion_auditor` | `chaosx-event-completion-auditor` | `sonnet` | read-only / plan-only |
| `chaosx_event_ui_worker` | `chaosx-event-ui-worker` | `haiku` | patch-capable |
| `chaosx_focus_tree_auditor` | `chaosx-focus-tree-auditor` | `haiku` | patch-capable |
| `chaosx_generated_event_art` | `chaosx-generated-event-art` | `haiku` | asset / research (web) |
| `chaosx_icon_artist` | `chaosx-icon-artist` | `haiku` | asset / research (web) |
| `chaosx_improvement_loop_planner` | `chaosx-improvement-loop-planner` | `opus` | read-only / plan-only |
| `chaosx_localisation_auditor` | `chaosx-localisation-auditor` | `sonnet` | patch-capable |
| `chaosx_portrait_creator` | `chaosx-portrait-creator` | `haiku` | asset / research (web) |
| `chaosx_repo_explorer` | `chaosx-repo-explorer` | `haiku` | read-only / plan-only |
| `chaosx_scripted_system_architect` | `chaosx-scripted-system-architect` | `sonnet` | patch-capable |
| `chaosx_skill_maintainer` | `chaosx-skill-maintainer` | `sonnet` | patch-capable |
| `chaosx_spreadsheet_doc_worker` | `chaosx-spreadsheet-doc-worker` | `haiku` | patch-capable |
| `chaosx_super_event_audio_researcher` | `chaosx-super-event-audio-researcher` | `haiku` | asset / research (web) |
| `chaosx_super_event_text_researcher` | `chaosx-super-event-text-researcher` | `haiku` | asset / research (web) |

Authority classes follow the `chaos-redux-subagents` skill. Claude Code has no verified tool allowlist in this setup, so the prompt body is the scope contract.

# Event 006 Independence Wave Subagent Deployment Plan

This is a working plan for implementation. Source specs live under `docs/specs/006_independence_wave_specs/`.

## Universal spawn rule

Spawn every project custom Codex subagent with:

```text
fork_context=false
```

The parent prompt must include all needed paths, constraints, user corrections, accepted plans, queued plans, rejected plans, route rules, and validation requirements.

## Active small-patch agents

Use these agents for bounded improvements inside the current Event 006 surface:

| Agent | Can patch directly | Must write handoff |
| --- | --- | --- |
| `chaosx_decision_mission_auditor` | costs, tooltips, cleanup, AI, visibility, cooldowns, existing formable checks, GUI button text | yes |
| `chaosx_focus_tree_auditor` | route locks, prerequisites, mutual exclusions, small rewards, focus AI, icon references, existing formation hooks | yes |
| `chaosx_country_package_auditor` | tag references, focus loading, party names, simple setup, existing formable checks | yes |
| `chaosx_localisation_auditor` | missing keys, dynamic localisation, cost text, scripted localisation, cross-surface wording | yes |
| `chaosx_scripted_system_architect` | narrow helpers, script constants, formable eligibility helpers, GUI button helpers, cleanup helpers | yes |

Handoff path:

```text
docs/plans/006_independence_wave_plans/subagent_handoffs/
```

## Plan-only agent

Use `chaosx_improvement_loop_planner` after meaningful implementation tranches.

Spawn it only when:

- several new mechanics, countries, formables, GUI surfaces, focus routes, decision systems, asset sets, or super-event candidates have been added
- the previous improvement addendum for Event 006 is implemented, promoted into specs, queued with a reason, or rejected

Do not spawn it as a ritual step after every patch.

The planner can return either:

- expansion addendum
- closure handoff

Closure means broad expansion should stop because additional mechanics would add bloat.

## Read-only agents

`chaosx_repo_explorer` stays optional and read-only. Use it only when file locations, patterns, or touchpoints are unclear.

`chaosx_event_completion_auditor` stays read-only for gameplay files and should run before a completion claim.

## Asset agents

Use asset agents by source type:

- `chaosx_asset_source_researcher` for real flags, real portraits, archival images, historical symbols, and sourced animation bases
- `chaosx_generated_event_art` for fictional panels, impossible-state art, generated portraits, generated animation frames, and high-chaos scenes
- `chaosx_icon_artist` for icons, formation seals, small animated button sprites, decision category icons, and achievement icons

Asset subagents do not wire gameplay or `.gfx` files unless the parent gives a narrow exception.

# Event 062 subagent handoff matrix

## Invocation status

The supplied archive contained twenty project subagent definitions, and every definition was read in full. The current environment did not expose a working project subagent spawn route. A tool registry probe returned HTTP 429.

No item below is presented as completed subagent work. These are required future handoffs and ownership boundaries.

## Required subagent sequence

| Order | Subagent | Mode | Event 62 task | Required output |
| ---: | --- | --- | --- | --- |
| 1 | `chaosx_repo_explorer` | read-only | map existing Event 62 code, cluster hooks, faction and war helpers, wiki and vanilla precedents, likely files, and edit order | repository map and blockers |
| 2 | `chaosx_ai_probability_auditor` | read-only | inspect baseline faction, victim, side, decision, sponsor, and settlement weights using the named scenarios | scenario baseline evidence |
| 3 | `chaosx_scripted_system_architect` | active narrow patch | design and implement event-owned transaction helpers, political units, receipts, sparse active registry, and forced-exit Chaos context | bounded patch and handoff |
| 4 | `chaosx_decision_mission_auditor` | active small patch | review and patch the crisis category, dynamic costs, missions, target selection, role visibility, AI, and cleanup | decision handoff |
| 5 | `chaosx_generated_event_art` | asset production | create report image, category picture, and conditional super-event image from accepted briefs | source, PNG, DDS, manifest, handoff |
| 6 | `chaosx_icon_artist` | asset production | create decision, mission, idea, and achievement icon families | source evidence, PNG, DDS, contact sheets, handoff |
| 7 | `chaosx_super_event_text_researcher` | research | research verified quote, reaction text direction, and attribution for the Evolution III super-event | research note |
| 8 | `chaosx_super_event_audio_researcher` | research and asset | find licensed structured musical audio, verify rights, download, convert, and document it | WAV and audio handoff |
| 9 | `chaosx_localisation_auditor` | active small patch | audit event, decision, mission, idea, achievement, Event Details, cluster, and super-event wording | localisation handoff |
| 10 | `chaosx_ai_probability_auditor` | read-only | compare final weights against the baseline using the same scenarios | probability comparison evidence |
| 11 | `chaosx_spreadsheet_doc_worker` | workbook patch | update Event 62 and Wars cluster fields in the authoritative XLSX and run the exporter | workbook and export handoff |
| 12 | `chaosx_improvement_loop_planner` | plan-only | near-completion depth and anti-bloat pass after implementation and audits | closure handoff or one bounded addendum |
| 13 | `chaosx_event_completion_auditor` | read-only | compare final implementation against the full spec, prompts, assets, audits, and catalog | completion report |

## Conditional and excluded subagents

### Conditional

`chaosx_documentation_curator` is useful if implementation creates several handoffs, reports, or conflicting plans. It should reconcile documentation only.

### Excluded by accepted design

The following subagents should not be spawned unless a later accepted addendum changes the design:

- `chaosx_focus_tree_auditor`
- `chaosx_country_package_auditor`
- `chaosx_portrait_creator`
- `chaosx_3d_model_pipeline`
- `chaosx_event_ui_worker`

Event 62 has no focus tree, country package, portrait, 3D model, or dedicated scripted GUI.

## Context rule

Every project subagent prompt must be self-contained and must not rely on inherited parent-thread context. In the Codex runtime, use `fork_context=false`.

Each prompt should include:

- Event 62 identity and accepted spec paths
- current repository revision and relevant changed files
- exact allowed files
- exact ownership boundary
- user constraints
- prior handoff disposition
- named validation or MCP evidence required
- handoff path under `docs/plans/062_allies_backstab_plans/subagent_handoffs/`

## Probability audit boundary

Any patch to faction selection, victim selection, victim count, side choice, decision weights, sponsor choice, settlement acceptance, random lists, or AI strategy factors requires this cycle:

1. baseline `chaosx_ai_probability_auditor` pass
2. owner or parent patch
3. comparison pass with `hoi4.probability_compare`

The auditor remains read-only and does not choose the target balance.

## Event UI worker boundary

The ordinary decision category and static category picture do not justify `chaosx_event_ui_worker`.

Do not route shared Event Logs, Event Details, settings, clusters, or the super-event framework to that worker. A dedicated Event 62 GUI would require a new accepted spec proving that normal decisions cannot present the mechanic clearly.

## Asset ownership split

`chaosx_generated_event_art` owns full-canvas scene art and the static category picture.

`chaosx_icon_artist` owns decision, mission, idea, and achievement icons.

The parent owns final nonportrait `.gfx` wiring and runtime references. Asset workers produce handoff notes and do not edit gameplay files unless a narrow exception is granted.

## Super-event ownership split

`chaosx_super_event_text_researcher` supplies verified wording research.

`chaosx_super_event_audio_researcher` supplies verified licensed audio and the final WAV.

`chaosx_generated_event_art` supplies the image.

The parent owns slot selection, localisation, sound definitions, settings-aware playback, event trigger, Event Details, documentation, and catalog alignment.

## Completion boundary

A successful subagent handoff is evidence, not completion. The parent must review every patch and asset, integrate cross-system behavior, run final validation, dispose of every plan, and report all blockers or simplifications.

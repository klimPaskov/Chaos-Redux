# Event 32 source review

## Review scope

The following uploaded project files were read in full before the specification was written.

### Core project and system files

- `AGENTS(7).md`
- `CHAOS_REDUX_MECHANICS(7).md`
- `chaos-redux-events(8).md`
- `chaos-redux-event-planning(20260813-152954).md`
- `chaos-redux-decisions-missions(3).md`
- `chaos-redux-event-assets(7).md`
- `chaos-redux-super-events(7).md`
- `chaos-redux-improvement-loop(8).md`
- `chaos-redux-frame-animation(8).md`
- `chaos-redux-focus-trees(3).md`
- `chaos-redux-subagents(8).md`
- `chaos-redux-comfyui(2).md`
- `chaos-redux-3d-model-pipeline(3).md`
- `chaos-redux-debug-playtest(2).md`
- `chaosx_dynamic_effects.md`
- `chaosx_dynamic_triggers.md`
- `config.toml`

### Catalog exports

- `chaos_redux_events_catalog(3).csv`
- `chaos_redux_clusters_catalog(3).csv`
- `chaos_redux_scenarios_catalog(3).csv`

The event export contains 182 data rows. Event 32 is listed as Missiles, Minor Repeatable, To Be Reworked, and unclustered. Its current catalog detail gives every country the next available missile technology, operational missiles, and launch sites.

The cluster export contains eight named clusters. Event 32 is not assigned to any of them.

The scenario export contains the current public scenario rows. Repository inspection also shows that raw scenario ID 14 is reserved by the Fallout-owned manual sandbox even though it is not a public catalog row. The next planned public identity for Event 32 is therefore `SCN-015`, subject to a fresh collision audit during implementation.

### Subagent archive

The `subagents.zip` archive was extracted and all 20 TOML definitions were read in full:

- `chaosx_3d_model_pipeline.toml`
- `chaosx_ai_probability_auditor.toml`
- `chaosx_asset_source_researcher.toml`
- `chaosx_country_package_auditor.toml`
- `chaosx_decision_mission_auditor.toml`
- `chaosx_documentation_curator.toml`
- `chaosx_event_completion_auditor.toml`
- `chaosx_event_ui_worker.toml`
- `chaosx_focus_tree_auditor.toml`
- `chaosx_generated_event_art.toml`
- `chaosx_icon_artist.toml`
- `chaosx_improvement_loop_planner.toml`
- `chaosx_localisation_auditor.toml`
- `chaosx_portrait_creator.toml`
- `chaosx_repo_explorer.toml`
- `chaosx_scripted_system_architect.toml`
- `chaosx_skill_maintainer.toml`
- `chaosx_spreadsheet_doc_worker.toml`
- `chaosx_super_event_audio_researcher.toml`
- `chaosx_super_event_text_researcher.toml`

## Current repository findings

The connected `klimPaskov/Chaos-Redux` repository was inspected on the `master` branch.

The current Event 32 source is `events/032_missile_crisis.txt`. It is a legacy hidden global dispatcher. It currently:

- runs `every_country`
- schedules one country report
- grants `experimental_rockets`
- grants `rocket_engines`
- adds two levels of `rocket_site`
- uses the capital for a first site
- uses a random owned state on later firings
- calls the existing Event 16 missile-crisis reaction helper from the recipient report

The current report localisation describes mysterious missiles found in the capital. The rework keeps the unexplained-origin theme, but moves the event from a one-time gift into a persistent missile-program system.

Event 16 already owns a bounded helper named `brilliant_scientist_record_missile_crisis`. Event 32 must keep calling that helper from the appropriate first-recipient context. Event 32 must not reproduce Event 16 mandate, dependence, exposure, or personal-history logic.

Event 23 currently grants Soviet nuclear technology and 100 nuclear bombs. Event 32 must not absorb that arsenal event. Its special-warhead track supplies missile delivery only when the country already owns the relevant payload technology and stockpile.

Event 76 currently represents American weapons testing as a separate event. Event 32 may accept test-data and reliability bridges from Event 76, but it must not replace that event or turn every missile launch into an American test event.

The repository raid documentation exposes rocket-site starting points, equipment requirements, target-state variables, nuclear and thermonuclear nuke types, success levels, and outcome effects. The exact installed vanilla and DLC behavior still requires implementation-time inspection.

## Planning rules applied

The specification follows these project rules:

- one event identity across entry event, country reports, news, decisions, evolutions, logs, documentation, and catalog
- evolutions are separate from ordinary program progression
- disabled evolutions cannot set unlock flags or create dependent content
- player-facing Event Details text explains the premise without listing raw mechanics
- no recurring all-country daily, weekly, or monthly scan
- all event-time global work is bounded to Event 32 firing or explicit scenario setup
- dynamic costs, risk, target weights, reserve packages, site limits, and AI willingness
- no default political-power store
- no more than four spendable cost types on one action
- a normal decision category before considering a custom window
- weighted logic requires named probability scenarios and an auditor comparison pass
- final assets require proper source evidence, processing, DDS conversion, manifest, and wiring
- the catalog workbook is the only editable spreadsheet source during implementation
- the exported CSV files are regenerated, never edited directly

## Subagent-role review applied

This chat runtime did not expose the project Codex subagent runner. The subagent TOMLs were therefore used as review contracts, not presented as independently executed agent reports.

The following role checks were applied manually:

| Role contract | Result in this package |
| --- | --- |
| Repository explorer | Current Event 32, localisation, Event 16 bridge, Event 23, Event 76, scenario registry notes, raid documentation, and relevant shared systems were mapped |
| Scripted-system architect | Normalized strike API, recipient profile, site records, incident queue, bounded delayed jobs, constants, and cross-system adapters are specified |
| Decision and mission auditor | Presentation layer, action budget, cost diversity, mission quality, target selection, cleanup, and exploit controls are specified |
| AI probability auditor | Named scenarios and expected ordering are provided, but no MCP probability evidence was available in this runtime |
| Asset workers | Required generated images and icon families are bounded. Portrait, flag, animation, and 3D routes are excluded because the event does not need them |
| Localisation auditor | Direction-only text requirements and forbidden wording patterns are specified |
| Spreadsheet worker | Workbook fields are mapped for implementation, but no workbook was edited during planning |
| Event completion auditor | Acceptance criteria and test matrix cover the complete event contract |
| Improvement-loop planner | A closure review is included. It rejects extra GUI, focus-tree, country, 3D, and event-owned terminal content as bloat |

## Tooling limitations

The following implementation-only evidence could not be produced here:

- the `hoi4-agent-tools` MCP server was not available
- the installed Windows vanilla game directory was not mounted
- the installed vanilla documentation folder was not mounted
- project subagents could not be spawned
- autonomous live testing was not invoked and is explicit-invocation-only under the debug-playtest skill

The specification therefore does not claim exact engine support for any named technology, raid field, stockpile token, or DLC adapter beyond what the current repository source demonstrates. The coding prompt treats technology graph inspection, raid precedent inspection, probability analysis, and live validation as hard implementation gates.

# Event 15 Subagent Orchestration

## Status

The custom subagent runtime was unavailable during this planning run. None of the subagents below were executed. The package provides explicit prompts so the implementation parent can spawn them with `fork_context=false` and reproducible inputs.

Repository root for implementation prompts:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

Source spec folder:

`docs/specs/015_utopia_manifesto_specs/`

Working plan and handoff folder:

`docs/plans/015_utopia_manifesto_plans/`

## Required order

### 1. Repository exploration

Spawn `chaosx_repo_explorer` before editing.

Purpose:

- map all current ID 15 files and mappings
- identify replaceable-tree patterns
- identify event log, GUI, focus, decision, country, asset, audio, achievement, doc, and workbook touchpoints
- find vanilla and Chaos Redux precedents
- propose edit and validation order

Output:

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/repo_explorer_handoff.md`

### 2. Scripted-system architecture

Spawn `chaosx_scripted_system_architect` after the repo map and before broad implementation.

Purpose:

- design the four-value helper system
- target eligibility and weak-country scoring
- selected-target lifecycle
- case integrity
- reserve and calling calculations
- cleanup
- constants and tuning tables

Output:

- architecture handoff, followed by bounded helper patches when appropriate

### 3. Main implementation tranche

The parent implements:

- event registration and chain
- safe target selection
- Ledger values and first GUI skeleton
- focus tree opening and route architecture
- initial decisions and ideas
- event log and docs skeleton

Do not run the improvement planner yet. It needs a meaningful implemented tranche.

### 4. Asset and super-event production

Run in bounded parallel work after filenames and sprite names are stable.

- `chaosx_generated_event_art` for fictional report, news, super-event, UI, flags, emblems, and institutional portraits
- `chaosx_icon_artist` for focus, idea, decision, category, achievement, and animated icon assets
- `chaosx_asset_source_researcher` only for a real edition, real portrait, real historical photograph, or attested symbol chosen by implementation
- `chaosx_super_event_text_researcher` for final title, description direction support, quote, and cultural remark
- `chaosx_super_event_audio_researcher` for final licensed music and conversion

Each agent writes its manifest or research handoff. The parent wires GFX, GUI, localisation, audio definitions, and event effects.

### 5. Surface audits and bounded patches

After the relevant surfaces exist, spawn:

- `chaosx_focus_tree_auditor`
- `chaosx_decision_mission_auditor`
- `chaosx_country_package_auditor`
- `chaosx_localisation_auditor`

These agents can patch narrow local issues. Broad gaps become plans for the parent.

### 6. Documentation and catalog alignment

After mechanics and final player-facing text stabilize:

- spawn `chaosx_documentation_curator`
- resolve source-of-truth, plan disposition, stale prompt, and handoff issues
- spawn `chaosx_spreadsheet_doc_worker` to update Event 15 in the workbook from exact in-game text

### 7. Mandatory improvement-loop pass

Spawn `chaosx_improvement_loop_planner` after the major implementation tranche and audits.

Required question:

- Does the implemented event fulfill the source promise without shallow routes, missing AI, weak decisions, disconnected assets, or bloat?

The planner returns either:

- an addendum that must be implemented, promoted, queued with reason, or rejected with reason
- a closure handoff

Do not run a second pass while the first is unresolved.

### 8. Skill maintenance review

Spawn `chaosx_skill_maintainer` only after implementation if Event 15 revealed a reusable workflow not already covered, such as a safe full-tree replacement registry, generic need-case framework, or reusable selected-target integration lifecycle.

Do not create an Event 15-specific skill.

### 9. Completion audit

Spawn `chaosx_event_completion_auditor` last.

It must compare:

- source specs
- accepted or rejected plans
- implementation
- handoffs
- assets
- audio
- localisation
- docs
- catalog
- task-specific validation

The parent can claim completion only after the audit finds no undisclosed simplification, missing surface, unresolved accepted plan, or hidden blocker.

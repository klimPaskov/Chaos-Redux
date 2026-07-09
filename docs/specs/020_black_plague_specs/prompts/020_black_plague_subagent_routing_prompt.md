# 020 Black Plague subagent routing prompt

Use this in the implementation environment after the main agent reads the full spec package. Spawn project subagents with `fork_context=false` and pass this package path plus event id `020` and slug `black_plague`.

## Early routing

- Use `chaosx_repo_explorer` only if the implementation agent cannot locate the shared biological warfare, disease mapmode, Deaths, event log, world-threat, focus-tree, or country-package files.
- Use `chaosx_scripted_system_architect` before duplicating disease status, state spread, death scaling, cure progress, mapmode state arrays, rat unit ticks, rat absorption, or country classification helpers.
- Use `chaosx_decision_mission_auditor` after the shared disease decisions are implemented or heavily changed.
- Use `chaosx_focus_tree_auditor` after base rat and King focus trees are built.
- Use `chaosx_country_package_auditor` after rat nation and King country packages exist.
- Use `chaosx_localisation_auditor` after broad player-facing text and dynamic localisation are written.
- Use `chaosx_event_completion_auditor` before any completion claim.
- Use `chaosx_documentation_curator` after several handoffs or after accepted plans are folded into specs.
- Use `chaosx_spreadsheet_doc_worker` only after implementation wording is final and the event catalog workbook can mirror in-game text.

## Asset and super-event routing

- Use `chaosx_generated_event_art` for fictional rat portraits, flags, report images, news images, super-event images, UI panels, and non-icon fictional art.
- Use `chaosx_icon_artist` for decision, focus, idea, category, achievement, tech, unit, and small animated icon work.
- Use `chaosx_super_event_text_researcher` for King reveal and world-end quotes, button remarks, title research, cultural allusions, and source confidence.
- Use `chaosx_super_event_audio_researcher` for unique licensed or public domain audio for every implemented super-event.

## Patch-capable audit routing

Patch-capable subagents may make small, local fixes inside their owned scope. They must write handoffs under `docs/plans/020_black_plague_plans/subagent_handoffs/` or the event-specific path used by the repository. Broad gaps should become plans, not silent redesigns.

## Mandatory near-completion routing

Before the event-planning or implementation goal is considered near complete, run `chaosx_improvement_loop_planner` with `fork_context=false` for the final depth and anti-bloat pass. The current package records a tooling blocker because the package-building environment could not spawn the subagent. The live repository environment must resolve that blocker by running the planner or by receiving an explicit project-owner waiver.

If the planner writes an addendum, fold it into the spec, queue it with a reason, reject it with a reason, or implement it before completion. If it writes a closure handoff, record it and continue to final audits.

---
name: chaos-redux-subagents
description: Use when coordinating custom Codex subagents for Chaos Redux implementation, asset production, super-event research, audits, or documentation work.
---

# Chaos Redux Subagents

Use this skill when a Chaos Redux task should be split across project custom Codex subagents.

This skill is the detailed source of truth for specialized helper-agent routing.

`AGENTS.md` should stay short enough to remain easy to read. Keep detailed subagent routing, ownership boundaries, recursive expansion rules, and handoff expectations in this skill instead of duplicating them in the root file.

This skill does not replace repository-wide rules in `AGENTS.md`. It expands the subagent section of `AGENTS.md`.

## 1. Core rule

The parent Codex agent remains responsible for final implementation.

Subagents can research, create files, audit, or document. The parent must review their outputs, perform final wiring, update dependent files, run validation, and report blockers honestly.

Do not use subagents to hide uncertainty or pass off responsibility. If a subagent reports blocked or uncertain work, the parent must carry that status into the final report.

## 2. Available project subagents

Use `chaosx_repo_explorer` for read-only repo exploration, touched-file mapping, pattern search, vanilla reference mapping, and edit-order planning.

Use `chaosx_asset_source_researcher` for real or archival image sourcing, real leader portraits, historical flags, historical symbols, user-provided source photos, source-image processing, and report/news/super-event images that must depict real historical material.

Use `chaosx_generated_event_art` for generated non-icon art, including fictional or alternate-history report images, news images, super-event images, fictional portraits, fictional flags, faction emblems, UI panels, dossier art, and progression-state base art.

Use `chaosx_icon_artist` for focus icons, idea icons, national spirit icons, officer corps icons, decision icons, decision category icons, achievement icons, and tech icons.

Use `chaosx_super_event_text_researcher` for super-event main quotes, exact wording checks, attribution confidence, source comparison, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for licensed or public domain audio research, source verification, download, `.ogg` conversion, and audio handoff notes.

Use `chaosx_focus_tree_auditor` for read-only focus tree audits covering branch depth, route coverage, icons, localisation, rewards, prerequisites, AI, and simplification.

Use `chaosx_decision_mission_auditor` for read-only decision and mission audits covering decision category lifecycle, objective quality, costs, tooltips, AI behavior, cleanup, balance, and exploit risk.

Use `chaosx_country_package_auditor` for read-only country package audits covering tags, history, states, leaders, portraits, flags, parties, focus loading, ideas, advisors, units, technologies, claims, cores, localisation, AI, and playable setup.

Use `chaosx_localisation_auditor` for read-only localisation and scripted localisation audits covering missing keys, duplicate keys, encoding, tooltip quality, broken dynamic text, and cross-surface text mismatch.

Use `chaosx_scripted_system_architect` for reusable scripted system design or implementation covering scripted effects, scripted triggers, script constants, event targets, meta effects, variables, and tuning values.

Use `chaosx_event_completion_auditor` for read-only spec-versus-implementation audits covering events, mechanics, assets, docs, super-events, focus trees, decisions, and validation.

Use `chaosx_mechanic_expander` for active recursive depth expansion during implementation. It reads the planning skill and relevant system skills, inspects shallow or duplicated mechanics, and writes concrete expansion spec addenda for the main agent. Use it when a feature needs new design material, not just an audit finding.

Use `chaosx_spreadsheet_doc_worker` for documentation, event catalog rows, manifests, completion reports, and player-facing summaries based on implemented repo state. For event details, evolution details, and cluster details, it must use the same wording as the in-game localisation in the relevant spreadsheet fields.


## 3. Asset routing

Do not use one broad asset worker for mixed visual packages.

Use:

- `chaosx_asset_source_researcher` for real, archival, historical, documentary, or public-source images when the asset must show real historical material
- `chaosx_generated_event_art` for generated non-icon fictional, alternate-history, symbolic, high-chaos, or unique event art, including report/news/super-event images that should look like period documentary material
- `chaosx_icon_artist` for generated gameplay icons

The parent agent must give each asset subagent a bounded prompt with exact asset names, target sizes, source mode, final folders, sprite names when already registered, reference folders, and constraints.

For flag work, the parent prompt must state whether each flag is a base flag, ideology variant, focus/event route variant, cosmetic-tag flag, historical flag, or fictional/generated flag. Base flags for existing countries must be preserved or restored from the approved prior asset unless explicitly in scope. Do not ask an asset subagent to create new no-suffix base flags for vanilla-supported or already-existing countries merely because ideology variants are needed. Ideology variants must be genuinely distinct generated or sourced designs, not recolors, filters, flipped copies, copied emblems, or simple added shapes. Historical flags and historically attested symbols belong with `chaosx_asset_source_researcher`; fictional or alternate-history variants belong with `chaosx_generated_event_art`. Every flag handoff must include normal/medium/small output paths, a contact sheet, orientation confirmation, and any historical uncertainty.

For generated report/news/super-event work, the parent prompt must specify the intended era, documentary or news-photo style, whether final output must be black and white, required post-processing, and any real people or real historical scenes that must not be fabricated. For report-event images, require Photoshop post-processing when Photoshop is available and make any approved non-Photoshop fallback explicit.

Asset subagents must read `chaos-redux-event-assets` and inspect the matching reference folder under `.agents/skills/chaos-redux-event-assets/assets/` before creating, sourcing, processing, or converting assets.

If the main agent already registered `.gfx` sprites or texture paths before requesting art, the asset subagent must follow those filenames, sprite names, target DDS paths, and target sizes. It should only propose names or paths when they were not provided.

Asset subagents may create source files, PNG previews, DDS files, contact sheets, manifests, and `gfx_handoff.md`. They must not edit `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files unless the parent explicitly expands scope.

## 4. Super-event routing

Use separate research agents when the super-event package has enough work to justify it.

Use `chaosx_super_event_text_researcher` for the main quote, exact wording checks, attribution confidence, source comparison, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for audio research, license verification, download, `.ogg` conversion, and audio handoff notes.

Use `chaosx_asset_source_researcher` or `chaosx_generated_event_art` for image work according to the source mode required by `chaos-redux-event-assets`. Generated super-event images are preferred for fictional, alternate-history, symbolic, supernatural, high-chaos, or emotionally specific moments; sourced images remain required for real historical people, real photographed events, and real archival artifacts.

The parent agent owns final super-event slot wiring, localisation, scripted localisation, audio id, settings-aware playback, `.gfx` image wiring, event trigger wiring, docs, and spreadsheet alignment.

## 5. Audit routing

Use `chaosx_focus_tree_auditor` after creating or heavily changing any focus tree.

Use `chaosx_decision_mission_auditor` after creating or heavily changing decision categories, timed missions, objective pools, influence systems, aid or intervention decisions, and focus-unlocked decision families.

Use `chaosx_country_package_auditor` after creating, releasing, transforming, splitting, puppeting, or substantially changing countries. Use it when tags, country history, state ownership, leaders, portraits, flags, parties, focus loading, ideas, starting forces, technologies, claims, cores, localisation, or country AI are touched.

Use `chaosx_localisation_auditor` after broad visible-content changes across events, focuses, ideas, decisions, GUI, scripted localisation, event logs, or super-events.

Use `chaosx_scripted_system_architect` before adding repeated cross-file logic, new dynamic helper patterns, shared constants, event-target flows, or meta-effect based systems. Use it again when implementation becomes copy-pasted or hardcoded.

Use `chaosx_event_completion_auditor` before calling any large event implementation complete, especially when the user is worried about simplification or fallback implementation.

Use `chaosx_repo_explorer` before editing when file locations or existing patterns are unclear.

Use `chaosx_spreadsheet_doc_worker` after implementation facts exist, not before.


## 6. Decision and mission audit routing

Use `chaosx_decision_mission_auditor` when a task touches decisions, missions, timed objectives, decision categories, cost localisation, objective pools, AI decision behavior, focus-unlocked decisions, or balance around decision-driven systems.

The auditor should normally be read-only. It should return:

- decision category lifecycle issues
- mission quality issues
- duplicate or passive objective risks
- cost and requirement clarity issues
- AI validity problems
- cleanup and stale-state risks
- exploit risks
- missing localisation and tooltip surfaces
- file paths and identifiers for every finding

The parent agent owns the fixes unless it explicitly grants patching scope.

## 6.5 Country package audit routing

Use `chaosx_country_package_auditor` when a task creates, releases, transforms, splits, puppets, or substantially changes a country.

This includes work touching:

- country tags and country definition files
- country history and state history
- ownership, controller, cores, claims, and capitals
- leaders, portraits, characters, advisors, commanders, and parties
- flags and cosmetic names
- focus tree loading and route availability
- starting ideas, laws, technologies, production, units, and templates
- country decisions, missions, and route-specific actions
- AI strategy, diplomacy behavior, and survival behavior
- localisation, asset manifests, docs, and spreadsheet rows

The auditor should normally be read-only. It should return:

- country package coverage checklist
- file surface checklist
- missing or stale country package surfaces
- map and state setup issues
- politics, leader, portrait, flag, advisor, and party issues
- focus, decision, idea, and asset issues
- starting military, technology, industry, supply, and production issues
- AI and playability issues
- concrete file paths and identifiers for every finding

The parent agent owns the fixes unless it explicitly grants patching scope.

## 7. Localisation audit routing

Use `chaosx_localisation_auditor` when a task adds, renames, rewires, or audits visible text.

This includes:

- event titles and descriptions
- event log names and detail text
- evolution text
- focus names and descriptions
- decision and mission text
- idea, advisor, trait, and country text
- GUI and scripted GUI text
- scripted localisation
- super-event `.t`, `.d`, `.a`, and `.q` keys
- tooltip and blocked-cost text

The localisation auditor must cross-check script references against localisation files. Searching only localisation files is not enough.

The parent agent owns final text edits unless patching scope is explicitly granted.

## 8. Scripted system architecture routing

Use `chaosx_scripted_system_architect` when a mechanic needs reusable scripted logic.

Good triggers include:

- repeated event option effects
- repeated decision effects or triggers
- repeated focus reward logic
- repeated event-log or evolution logic
- shared tuning thresholds
- dynamic target or value calculations
- meta effects or meta triggers
- event-target flows
- cross-file constants
- duplicated cleanup logic

The architect may be read-only for design or write-capable for implementation depending on the parent prompt.

When implementing, it may edit only the approved helper files, constants, narrow call sites, and helper documentation. The parent agent still owns the wider event, focus, decision, localisation, GUI, docs, spreadsheet, and validation alignment.


## 8.5 Recursive expansion routing

Use `chaosx_mechanic_expander` when the parent agent needs new design material during implementation.

Good triggers include:

- a mechanic works but does not change gameplay enough
- a focus tree has branches but the branches do not matter
- focus rewards repeat factories, equipment, PP, stability, war support, or generic ideas
- a decision system is mostly passive buttons
- a country package has a tag, flag, and leader but no playable identity
- events have text but no follow-up, reactions, evolutions, clusters, or detail depth
- visual assets do not evolve with stages or route identity
- lore is present but unclear, generic, or disconnected from effects
- an audit subagent finds major shallow content and tells the parent to spawn the expander

The expander should use `chaos-redux-event-planning` as the design baseline and write an expansion addendum, usually under:

```text
docs/plans/<event_id>_<event_slug>_plans/<feature_slug>_expansion_addendum.md
```

Do not ask the expander to write new plans under `docs/planning/`, `planning/`, or any other planning folder. Use `docs/plans/` for expansion addenda. If a prompt says "planning folder", treat that as `docs/plans/` unless the parent explicitly provides another path. Expansion addenda should be concise design handoffs, not code blueprints: enough concrete behavior to implement, but no long tables of constants, full scripted-effect recipes, parser-level notes, detailed code wiring, or exhaustive touched-file inventories unless the parent specifically needs that level of detail.

The parent agent must decide which parts to implement immediately, which parts to queue, and which parts to reject.

Audit subagents that inspect actual systems should read `chaos-redux-improvement-loop` and include an improvement handoff. For major depth gaps, the handoff should recommend spawning `chaosx_mechanic_expander`.

## 9. Handoff quality

Every subagent prompt should include:

- task goal
- exact inputs to read
- exact outputs to produce
- files or folders allowed to edit
- files or folders forbidden to edit
- source-of-truth documents
- blocked-work reporting format
- final handoff path

Every subagent output should include:

- completed items
- blocked items
- uncertain items
- files created or changed
- evidence used
- recommended parent-agent next steps

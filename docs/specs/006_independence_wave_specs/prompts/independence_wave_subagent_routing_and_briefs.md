# Independence Wave subagent routing and bounded briefs

Every project subagent must be spawned with `fork_context=false`.

The parent remains responsible for integration, validation, source-of-truth decisions, and completion claims.

The briefs below assume the package has been copied to:

`docs/specs/006_independence_wave_specs/`

Subagent handoffs belong under:

`docs/plans/006_independence_wave_plans/subagent_handoffs/`

## 1. Repository explorer

Use only before implementation if the touched-file map, tag registry, existing release helpers, focus loading, scenario wiring, or Event 5 collision pattern remains unclear.

### Prompt

Read `AGENTS.md`, `chaos-redux-subagents`, the Event 6 source specification folder, the current Event 5 implementation and docs, the Liberations cluster implementation, the tag and cosmetic-tag registries, existing event-created country setup, dynamic release helpers, event log, focus loading, triggerable scenario system, and relevant vanilla references. Do not edit gameplay files. Map exact files and identifiers needed for Event 6, identify reusable helpers, locate tag and state collision risks, identify the nearest existing event-created country and release patterns, and propose a safe edit order. Save the report to `docs/plans/006_independence_wave_plans/subagent_handoffs/repo_explorer_handoff.md`. Include exact paths, identifiers, risks, and task-specific validation checks.

## 2. Scripted system architect

Use before duplicating release, origin, package, value, patron, league, or formable logic.

### Prompt

Read `AGENTS.md`, the Event 6 specs, candidate, formable, decision, AI, and tuning matrices, the Event 5 origin logic, existing dynamic effects and docs, event target patterns, script constants, meta effects, and release helpers. Design and, where narrow and safe, implement reusable helpers for synchronized wave planning, protected host states, candidate eligibility, origin assignment, country package application, dynamic force budgets, value initialization, cleanup, patron channels, league state, and formable family checks. Every helper needs scope, inputs, outputs, defaults, side effects, cleanup, call sites, constants, and documentation. Do not redesign the event. Save the handoff to `docs/plans/006_independence_wave_plans/subagent_handoffs/scripted_system_architect_handoff.md`.

## 3. Improvement-loop planner

Run after the main specification is in the repository and again only after a meaningful implementation tranche, with the previous addendum resolved.

### Initial near-completion planning prompt

Read `AGENTS.md`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, all Event 6 specs, matrices, research notes, diagrams, prompts, and any existing Event 6 plans. Confirm whether an unresolved Event 6 addendum already exists. Inspect the design for shallow routes, generic country packages, disconnected values, missing AI, weak formable or league play, missing sensitive-identity safeguards, asset gaps, and scope bloat. Write either one concrete expansion addendum or a closure handoff under `docs/plans/006_independence_wave_plans/`. State what should be promoted into the source specs. Do not edit gameplay files.

### Post-tranche prompt

Read the same sources plus the implemented files, handoffs, and audit reports named by the parent. Evaluate only gaps created or exposed by the completed tranche. Do not stack a new addendum over an unresolved one. Recommend closure when additional mechanics would add bloat.

## 4. Country package auditor

Run after a batch of candidate countries is implemented.

### Prompt

Read `AGENTS.md`, the Event 6 specs, `matrices/006_candidate_country_registry.csv`, regional overlays, formables, origin separation diagram, the parent-provided list of implemented package IDs, and every file touched for those packages. Audit tags, `X` suffix rules, country definitions, history, states, protected hosts, capitals, cores, claims, leaders, parties, flags, portraits, ideas, focus loading, decisions, units, templates, equipment, manpower, technology, supply, AI, formables, localisation, and cleanup. Verify Event 5 and Event 6 origin separation for overlapping tags. Patch only small local defects. Write a handoff with package-by-package status to `docs/plans/006_independence_wave_plans/subagent_handoffs/country_package_audit_<batch>.md`.

## 5. Focus tree auditor

Run after the common framework, each regional overlay tranche, and the signature modules are implemented.

### Prompt

Read `AGENTS.md`, `hoi4-focus-trees`, all Event 6 focus and country specs, regional overlay matrix, idea lifecycle matrix, formable registry, decision map, parent-provided focus file paths, and relevant implementation handoffs. Compare the required survival, government, economy, military, diplomacy, former-host, expansion, league, formable, and high-chaos lanes against implementation. Verify branch depth, interaction, route locks, prerequisites, failure states, AI, decision hooks, idea lifecycles, formable links, icons, localisation, and existing-tree overlay safety. Patch only small local issues. Write a route coverage table and handoff to `docs/plans/006_independence_wave_plans/subagent_handoffs/focus_tree_audit_<scope>.md`.

## 6. Decision and mission auditor

Run after the value system and each major decision family are implemented.

### Prompt

Read `AGENTS.md`, `hoi4-decisions-missions`, Event 6 spec Part 3, `matrices/006_decision_mission_map.csv`, wave tuning, AI matrix, idea lifecycles, and the implementation files named by the parent. Audit every accepted row for owner, phase, target, visible requirement, cost, duration, success, failure, partial result, AI, cooldown, cleanup, route validity, and exploit risk. Flag political-power stores, passive checklists, reward dust, free-unit loops, stale targets, invalid hosts, dead patrons, and formable core spam. Patch only small local cost, tooltip, AI, visibility, cooldown, or cleanup defects. Write the handoff to `docs/plans/006_independence_wave_plans/subagent_handoffs/decision_mission_audit_<scope>.md`.

## 7. Localisation auditor

Run after broad player-facing text exists and before catalog updates.

### Prompt

Read `AGENTS.md`, the Event 6 specs, implemented events, decisions, focuses, ideas, scripted GUI, scripted localisation, event log, evolutions, cluster details, scenario UI, achievements, super-events, and docs. Audit missing and duplicate keys, UTF-8 BOM, namespaces, raw triggers, dynamic values, integer formatting, route tone, hidden spoilers, working labels, research gates, cost clarity, and cross-surface contradictions. Confirm Event Details describes the premise and does not list effects. Patch small local text and key defects. Write the handoff to `docs/plans/006_independence_wave_plans/subagent_handoffs/localisation_audit.md`.

## 8. Asset source researcher

Use for real leaders, historical flags, historically attested symbols, and any report or super-event scene that must depict real material.

### Prompt

Read only the Event 6 asset prompt, the relevant source-mode sections of the asset skill, the candidate package IDs named by the parent, matching reference folders, and source pages. Source and document male real-leader portraits, historical flags, and attested symbols. Verify date, author or archive, license, era fit, and identity fit. Crop real portraits to head and shoulders, preserve identity through the HOI4 treatment, preserve sources, process PNGs, create final DDS or TGA files, update the Event 6 asset manifest, and write `gfx_handoff.md`. Do not edit gameplay or GFX files. Do not create advisor portrait icons. Mark uncertain or blocked assets rather than substituting generated history.

## 9. Generated event art

Use for fictional report and news scenes, super-event images, fictional portraits, councils, alternate flags, faction emblems, and UI art.

### Prompt

Read only the Event 6 asset prompt, named asset package paths, relevant asset-skill sections, and matching visual reference folders. Use the official image generation workflow. Produce final-source art for the exact assets named by the parent. Event 6 leader, commander, and collective portrait subjects must all be male and must match the canonical vanilla HOI4 portrait family. Follow 1936 to 1945 documentary direction for event scenes. Preserve source PNGs, process to exact dimensions, convert to DDS, update manifest and GFX handoff, and create contact sheets. Do not edit GFX or gameplay files. Do not create advisor portrait icons. Do not generate real leaders or attested historical flags.

## 10. Icon artist

Use for focus, idea, decision, category, achievement, scripted GUI, formable, warning, and animated small-sprite assets.

### Prompt

Read only the Event 6 asset prompt, `matrices/006_asset_family_registry.csv`, the parent-provided icon list, relevant asset and animation skill sections, and matching reference folders. Preserve parent filenames and sprite names. Generate distinct source art for each icon type. Do not resize focus art into idea or decision icons. For animated seals and warnings, create real source frames, static fallback, processed frames, sheet PNG and DDS, preview GIF, contact sheet, manifest, and GFX handoff. Do not edit gameplay or GFX files.

## 11. Super-event text researcher

Run after final trigger roles and slots are known.

### Prompt

Read only the Event 6 super-event prompt and the relevant super-event text rules. Verify the approved league formation and dangerous coordinated bloc text packages in `research/006_super_event_text_research.md`. Confirm wording, attribution, source access, UI fit, and copyright note. Do not reselect text unless a documented blocker exists. Do not invent quotes or convert working labels into final titles. Write the research note to `docs/super_events/006_independence_wave_super_event_research.md`.

## 12. Super-event audio researcher

Run after the super-event roles are fixed.

### Prompt

Read only the Event 6 super-event prompt, relevant audio rules, named existing track lists, and output paths. Use the two approved recordings and segment plans in `research/006_super_event_audio_research.md`. Reverify the source pages and rights, preserve source downloads, edit and convert to 44.1 kHz OGG, place final files under the Event 6 music folder, and document checksums, audio IDs, and wiring. Do not edit sound definitions or gameplay files. Reject uncertain licenses and placeholders.

## 13. Documentation curator

Run after several implementation tranches and subagent handoffs.

### Prompt

Read `AGENTS.md`, `chaos-redux-subagents`, all Event 6 source specs, plans, handoffs, audit reports, asset manifests, super-event notes, implementation docs, and prompt files named by the parent. Build a source-of-truth map. Mark every plan as implemented, promoted, queued with reason, rejected with reason, superseded, or blocked. Reconcile contradictions and stale descriptions. Create `docs/plans/006_independence_wave_plans/source_of_truth_map.md` and `resume_packet.md`. Do not edit gameplay, localisation, assets, or spreadsheets.

## 14. Spreadsheet worker

Run only after final in-game localisation and docs exist.

### Prompt

Read the parent prompt, the spreadsheet skill, the Event 6 workbook row, and only the final Event 6 Event Details, event log, evolution, cluster, and scenario localisation needed for mirroring. Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` in place. Replace the stale 4 to 6, 5 to 7, 6 to 9, 8 to 12, and 10 to 16 wave ranges with final in-game wording based on 3, 4, 5, 7, and 10. Preserve workbook structure and formatting. Report changed cells and any blocked fields. Do not edit gameplay or localisation.

## 15. Completion auditor

Run after implementation, audits, docs, assets, super-event research, and spreadsheet alignment are complete.

### Prompt

Read `AGENTS.md`, all Event 6 specs and matrices, every accepted or queued plan, implementation files, audit handoffs, asset manifests, super-event research, docs, catalog update report, and validation evidence. Compare every accepted requirement against implementation. Report completion by surface, missing or simplified content, plan dispositions, meaningful validation, asset and documentation gaps, remaining blockers, and whether another improvement-loop pass is needed. Do not edit gameplay files. Save the audit to `docs/plans/006_independence_wave_plans/006_independence_wave_completion_audit.md`. Do not mark completion while inputs, assets, AI, localisation, catalog, or accepted plans are missing.

## 16. Skill maintainer

No new Event 6-specific skill is recommended. Use the skill maintainer only if implementation reveals a reusable workflow that is absent from existing release, country-package, formable, origin-separation, or large-candidate-registry guidance. Event-specific rules remain in the source spec and implementation docs.

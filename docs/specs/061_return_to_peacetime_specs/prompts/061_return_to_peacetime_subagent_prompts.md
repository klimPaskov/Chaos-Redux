# Event 061 subagent prompts

## Use rules

Every subagent invocation uses `fork_context=false` and a complete explicit prompt.

The parent agent owns integration, review, validation, and the final completion claim.

Patch-capable subagents write handoffs under:

`docs/plans/061_return_to_peacetime_plans/subagent_handoffs/`

The prompts below are working invocation briefs. Add the active repository path, branch, diff, and exact task state before spawning.

## chaosx_repo_explorer

Read repository `AGENTS.md`, every Event 61 source specification, and the current catalog exports. Locate all current Event 61 files, `chaosx.nr61.1`, random-event registration, name mappings, Event Logs mappings, evolution mappings, Peace cluster registry, decision precedents, law definitions, achievement registry, asset consumers, docs, and authoritative workbook. Return exact paths, identifiers, current behavior, stale references, and safe edit boundaries. Do not modify files. Distinguish authoritative sources from generated CSV exports. Record missing or ambiguous surfaces.

## chaosx_scripted_system_architect

Read repository `AGENTS.md`, Event 61 Parts 1 through 5 and Part 7, `chaosx_dynamic_effects.md`, `chaosx_dynamic_triggers.md`, current shared helper files, and local vanilla documentation. Design or audit the smallest reusable helper contracts for validated adjacent economy and conscription law movement, atomic military-to-civilian conversion with a caller-owned state ledger, reverse restoration, exact positive stockpile debit for unsupported ordinary families, and safe scripted conventional division disband. Keep Event 61 orchestration and Readiness private. Identify which helpers are truly cross-event, exact input and output variables, failure codes, idempotence rules, call-site audits, documentation changes, and engine blockers. Do not patch event orchestration unless the parent explicitly requests it.

## chaosx_decision_mission_auditor

Read repository `AGENTS.md`, Event 61 Parts 2, 3, 5, and 7, the decision prompt, current implementation files, and the decision and mission skill. Audit the complete Return to Rearmament category, Readiness calculation, visible action budget, phased decisions, state targeting, cost framework, missions, repeat-cycle merge, active-war changes, extreme-law recovery, AI access, cancellation, cleanup, and save reload. Test for stale targets, free factory restoration, duplicate law steps, impossible costs, mission spam, soft-lock under No Army, and permanent-conversion ambiguity. Make only bounded in-scope fixes when authorized. Write a handoff with every finding and validation result.

## chaosx_ai_probability_auditor

Read repository `AGENTS.md`, Event 61 Parts 2 through 5, the AI probability scenario file, all Event 61 AI source blocks, and the current probability-tool contract. Inspect every `ai_will_do`, option chance, disposition choice, protection-family choice, voluntary Permanent Peace choice, and weighted state or unit pool. Run the twelve named scenarios and required sensitivity sweeps. Use complete normalized pools. Report exact, bounded, sampled, or unresolved results. Compare pre-fix and post-fix behavior after the parent changes weights. Do not edit source. Save evidence under `docs/plans/061_return_to_peacetime_plans/probability_audit/`.

## chaosx_generated_event_art

Read repository `AGENTS.md`, Event 61 Part 6, the asset prompt, the asset requirements handoff, and the event-asset skill. Produce the four final report images and the static Return to Rearmament category picture. Inspect exact installed vanilla reference canvases first. Use fictional anonymous global 1930s to 1940s scenes. Preserve source evidence, generate final full-resolution art, process to exact consumer dimensions, create PNG and DDS outputs, document prompts and provenance, and write GFX handoff notes. Do not wire gameplay or `.gfx` files.

## chaosx_icon_artist

Read repository `AGENTS.md`, Event 61 Part 6, the asset prompt, the achievement prompt, the asset requirements handoff, and the event-asset skill. Produce the complete distinct icon family for the category, every decision and mission consumer, the five idea concepts, Peacetime Economy, No Army, and the three achievements. Inspect exact vanilla icon families and consumer sizes. Preserve transparency, reject halos and fake checkerboards, validate at in-game size, convert to final DDS, and write sprite handoff notes. Do not use one renamed icon for unrelated concepts.

## chaosx_localisation_auditor

Read repository `AGENTS.md`, Event 61 Part 6, the localisation handoff, all final Event 61 localisation files, Event Logs text, cluster text, law text, idea text, decision and mission text, and achievement text. Remove raw keys, developer wording, planning labels, awkward repetition, false mechanical claims, and text that reveals hidden outcomes. Verify dynamic values, pluralization, country and state names, law names, mission deadlines, blocked reasons, Event Details metadata, and option tone. Preserve uncertainty where specified. Do not rewrite mechanics. Write a handoff listing changed keys and remaining blockers.

## chaosx_documentation_curator

Read repository `AGENTS.md`, every Event 61 source spec, implementation handoffs, final source files, Event Logs integration, cluster registry, achievement implementation, asset manifests, and current documentation. Reconcile the source-of-truth map. Update Event 61 public docs, system docs, law docs, achievement docs, cluster docs, and cross-event notes to describe verified implementation. Do not copy stale tuning values. Identify broken links and temporary asset paths. Write a handoff with authoritative paths and unresolved contradictions.

## chaosx_spreadsheet_doc_worker

Read repository `AGENTS.md`, the catalog alignment handoff, authoritative workbook, final Event 61 implementation facts, cluster registry, and documentation. Update only the authoritative XLSX. Replace the stale Event 61 row, set type Minor Repeatable, Chaos level 1, Cluster ID 4, Member Severity High, status that matches verification, and the three evolution summaries. Correct Peace cluster members to `9, 61` and update its description and status. Run `python .tools/export_event_catalog_csv.py`. Review the generated diff and report exact rows and exports. Do not edit CSV files directly.

## chaosx_improvement_loop_planner

Read repository `AGENTS.md`, the improvement-loop skill, every Event 61 source spec, current implementation, validation evidence, probability evidence, asset and localisation handoffs, and documentation state. Perform one near-completion anti-bloat and missing-depth review. Look for shallow decisions, disconnected Readiness state, weak evolution response, unused laws, excessive meters, duplicated helpers, missing AI behavior, missing country outcomes, repeat-cycle failures, soft-locks, asset gaps, and documentation drift. Return a bounded numbered addendum with priority, reason, affected files, and acceptance test for each item. Do not patch. Do not invent a focus tree, new country, scripted GUI, or unrelated event chain unless a proven design gap requires it.

## chaosx_event_completion_auditor

Read repository `AGENTS.md`, every Event 61 source spec, all implementation files, generated handoffs, validation logs, probability evidence, asset manifests, localisation, docs, workbook diff, catalog exports, Event Logs, cluster integration, and achievements. Build a requirement-by-requirement coverage matrix. Verify baseline math, state ledger, law targets, all decisions and missions, all three evolutions, active-war handling, AI evidence, Chaos accounting, save reload, performance, assets, localisation, docs, workbook, and achievements. Mark each row pass, failed, blocked, or not applicable with evidence. Do not call the event complete while a required final asset, safe-disband proof, local law validation, probability result, or catalog update is missing.

## chaosx_event_ui_worker

Use only when actual Event 61 decision or Event Logs surfaces have a confirmed layout defect. Read repository `AGENTS.md`, the Event 61 presentation rules, exact GUI files, and local vanilla references. Audit category picture crop, decision rows, dynamic text, Event Details, cluster detail, scroll bounds, click regions, and supported resolutions. Make bounded fixes only. Do not create a bespoke Event 61 mechanic window.

## chaosx_country_package_auditor

Use only when Event 61 state is inherited by a newly created, restored, or released country and the implementation adds country-package handling. Audit only the Event 61 inheritance contract, law compatibility, state ledger ownership, Readiness reset, and decision availability. Do not redesign the country package.

## chaosx_focus_tree_auditor

Use only when a separate country focus tree directly integrates Event 61 and the implementation changes that tree. Audit the narrow focus hooks, law and decision unlocks, AI route validity, and layout impact. Do not create an Event 61 focus tree.

## chaosx_asset_source_researcher

Use only if the approved asset direction changes from generated fictional scenes to real archival material. Research defensible sources, rights, attribution, and crop suitability. Do not substitute a real person's identity or copy an unclear copyrighted image.

## chaosx_portrait_creator

Use only if a later approved Event 61 route adds a character. Follow the portrait production skill and keep portrait work separate from the current anonymous global design.

## chaosx_super_event_text_researcher and chaosx_super_event_audio_researcher

Use only if a later accepted design adds a super-event threshold. Research verified text, quote, remark, and licensed audio under the super-event skill. Do not attach a super-event to the current implementation merely to enlarge presentation.

## chaosx_3d_model_pipeline

Use only if a later accepted design adds a custom unit model or map entity. The current event uses ordinary factories, laws, stockpiles, and divisions.

## chaosx_skill_maintainer

Use only when implementation proves that an existing project skill or shared contract is wrong or missing a reusable rule. Update the narrow skill source and preserve its general scope. Do not place Event 61 private design into a global skill.

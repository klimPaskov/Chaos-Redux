# Event 31 Random Terror subagent routing prompts

## Shared rule

Every project subagent must be spawned with `fork_context=false`.

The parent prompt must provide every required path, accepted constraint, current implementation state, prior handoff disposition, and allowed file scope.

The parent remains responsible for final integration, validation, documentation, workbook alignment, commits, and completion claims.

Patch-capable subagents write handoffs under:

`docs/plans/031_random_terror_plans/subagent_handoffs/`

Read-only audit reports and planning addenda belong under:

`docs/plans/031_random_terror_plans/`

Do not let several patch-capable agents edit the same files concurrently.

## Recommended order

1. Repository exploration
2. Scripted-system architecture
3. Baseline probability audit for existing or newly mapped weighted surfaces
4. Core parent implementation
5. Decision and mission audit
6. Country-package audit
7. Focus-tree audit
8. Asset production and portrait production
9. Super-event text and audio research
10. Localisation audit
11. Final probability comparison
12. Spreadsheet update
13. Documentation curation
14. Improvement-loop closure pass
15. Event completion audit

## 1. `chaosx_repo_explorer`

Use before editing because Event 31 spans many live systems and the planning package does not contain the repository file map.

### Ready prompt

```text
You are the read-only repository explorer for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-focus-trees, chaos-redux-event-assets, chaos-redux-super-events, chaos-redux-subagents, CHAOS_REDUX_MECHANICS, and every file under docs/specs/031_random_terror_specs/.

Map the existing Event 31 placeholder and every likely touchpoint for event registration, pre-fire history actor preparation, event log and Event Details selectors, evolution logging, public world-end rows and toggles, triggerable scenario registry, country-carrier collections, protected tag audit, special and nonhuman classifiers, world-threat aggregate, Deaths, Condemnation, decision categories, selected-target helpers, state map modes, focus loading, Focus Navigation, achievements, portraits, flags, icons, report and news art, super-event slots, sound definitions, canonical audio catalog, docs, and authoritative workbook.

Inspect current Chaos Redux precedents and exact vanilla precedents. Use mandatory read-only HOI4 MCP event, focus, probability, technology, GUI, and map routes where the surface is supported. Record exact blockers if a route is missing.

Do not patch files.

Write docs/plans/031_random_terror_plans/031_random_terror_repo_map.md with relevant files, identifiers, precedents, collision risks, edit order, and meaningful validation plan. Include the live status of proposed SCN-014, proposed Cluster 9, available carriers, Event 31 entry identity, super-event slots, and state-map presentation options.
```

## 2. `chaosx_scripted_system_architect`

Use after the file map and before repeated Event 31 logic is duplicated.

Allowed patch scope should be limited to Event 31 helpers, event-owned constants, event-owned triggers, and narrowly required shared call sites.

### Ready prompt

```text
You are the scripted-system architect for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, the Event 31 repo map, and every file under docs/specs/031_random_terror_specs/.

Design and, where the parent explicitly permits, implement narrow reusable contracts for Event 31 values, state stages, selected state and corridor targets, organization identity, affected-country pulses, incident validity, pressure and legitimacy changes, actor values, country carrier transaction inputs, scenario validation and bypass cleanup, world-threat refresh, operation outcomes, Deaths registration, and complete invalid-target cleanup.

Use existing dynamic effects and triggers when their contracts fit. Keep helpers private to Event 31 unless they have demonstrated cross-system callers. Centralize tuning through script constants where supported. Do not add recurring whole-world daily, weekly, or monthly scans. Do not invent a custom GUI.

Allowed files: <EXACT_FILES>

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_scripted_system_architect_handoff.md with files changed, helper names, inputs, outputs, defaults, side effects, call sites, meaningful validation, unresolved engine limits, and parent follow-up.
```

## 3. `chaosx_ai_probability_auditor`

Use for every complex target, incident, evolution, decision, mission, focus, route, strategy, scenario, actor-selection, uprising, and world-end weight.

The auditor is read-only.

Run once before weighted patches and once after the owning patch.

### Baseline prompt

```text
You are the read-only AI and probability auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-focus-trees, chaos-redux-subagents, docs/specs/031_random_terror_specs/031_random_terror_spec_part_9_ai_balance_probability.md, and docs/specs/031_random_terror_specs/031_random_terror_ai_scenario_matrix.md.

Start with hoi4.probability_inspect for every named in-scope surface. Analyze scenarios P01 through P10 and the world-end W01 through W08 cases. Include paired identity-fairness cases proving Muslim-majority status, refugee population, ethnicity, nationality, and ordinary ideology do not raise baseline target or recruitment scores.

State whether every candidate pool and external factor set is complete. Distinguish exact, bounded, sampled, score-only, and unresolved evidence. Use evaluate, sweep, simulate, render, or sequence only under the declared scenario contract. Do not patch source and do not choose balance targets.

Write docs/plans/031_random_terror_plans/031_random_terror_probability_baseline.md with scenario IDs, surface IDs, pool completeness, evidence class, current ordering, dominance or starvation findings, unresolved factors, and comparison inputs for the later pass.
```

### Comparison prompt

```text
Repeat the Event 31 probability audit after the owning patches.

Use the same repository root, source files, surface IDs, scenario IDs, candidate pools, and declared external factors as the baseline report.

Run hoi4.probability_compare for every changed weighted surface. Report whether the final ordering matches the Event 31 specification. Do not patch source.

Write docs/plans/031_random_terror_plans/031_random_terror_probability_comparison.md and identify every unresolved, newly dominant, starved, or invalid route.
```

## 4. `chaosx_decision_mission_auditor`

Use after the full government and actor decision categories exist.

### Ready prompt

```text
You are the active decision and mission auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, docs/specs/031_random_terror_specs/031_random_terror_spec_part_3_government_response_decisions_and_missions.md, docs/specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md, the current Event 31 decision files, scripted helpers, category definitions, localisation, and asset handoffs.

Audit and make only small bounded patches for phase visibility, action count, mission count, four-cost limit, concrete cost variety, texticons, exact state and corridor targets, custom trigger tooltips, goal auto-completion, success and failure direction, AI validity, reserve floors, selected-target cleanup, cooldowns, cancellation, duplicate missions, stale targets, victim-support value, category-picture use, and exploit loops.

Do not create a new mechanic, full GUI, country package, route family, or event chain. Broad gaps become a plan and stop.

Any weighted AI patch requires a prior probability baseline and a later comparison by the probability auditor.

Allowed files: <EXACT_FILES>

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_decision_mission_auditor_handoff.md with changed IDs, files, before and after behavior, meaningful validation, skipped checks, remaining gaps, and parent actions.
```

## 5. `chaosx_country_package_auditor`

Use after territorial creation, takeover, merger, split, scenario actors, and final-state packages are implemented.

### Ready prompt

```text
You are the active country-package auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-focus-trees, chaos-redux-event-assets, chaos-redux-subagents, docs/specs/031_random_terror_specs/031_random_terror_spec_part_5_territorial_insurgency_and_country_packages.md, docs/specs/031_random_terror_specs/031_random_terror_country_package_matrix.md, the carrier audit, and all current Event 31 country, history, character, focus-loading, unit, technology, idea, AI, flag, portrait, localisation, and cleanup files.

Audit and make only small bounded patches for carrier safety, origin markers, territory, capital, parent viability, parties, leader and portrait references, flags, starting ideas, research slots, compatible technologies, formations, equipment, manpower, production, supply, air and navy source validity, focus loading, decisions, AI, merger, split, takeover, defeat, and cleanup.

Verify Event 31 actors are special Chaos countries and remain outside actual nonhuman. Verify no custom Event 19 unit provider was introduced. Verify no serious fighting actor is an empty tag.

Do not invent a new country family, new ideology, new formable suite, or broad focus route. Broad gaps become a plan.

Allowed files: <EXACT_FILES>

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_country_package_auditor_handoff.md with tags or carriers, state groups, characters, forces, tech, flags, changed files, validation, blockers, and parent follow-up.
```

## 6. `chaosx_focus_tree_auditor`

Use after the final shared actor tree and terminal branch are built.

### Ready prompt

```text
You are the active focus-tree auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-focus-trees, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-subagents, docs/specs/031_random_terror_specs/031_random_terror_spec_part_6_focus_tree_and_political_routes.md, the country-package matrix, route coverage requirements, current focus source, localisation, icons, decisions, idea lifecycles, and AI.

Use hoi4.focus_inspect and hoi4.focus_render before changes. Review normal-zoom first-glance clarity, branch ownership, opening pacing, Shadow Council, War Directorate, Ideological Secretariat, economy, military, network and diplomacy, expansion, crisis, Jihadist International, Final Jihad, and False Revelation routes. Check prerequisites, mutual exclusions, hidden-route visibility, focus filters, Focus Navigation, reward diversity, dead ends, idea lifecycle, decision integration, route-specific AI, icons, and actor-specific localisation.

Make only small bounded patches inside the current route architecture. Use bounded hoi4.focus_rewrite when needed and render again. Do not invent a new route family or formable suite. Broad design gaps become a plan.

Any focus AI weight patch requires the probability audit cycle.

Allowed files: <EXACT_FILES>

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_focus_tree_auditor_handoff.md and include the required route coverage table, MCP evidence identifiers, changed focus IDs, before and after behavior, remaining gaps, and parent work.
```

## 7. `chaosx_localisation_auditor`

Use after broad player-facing text exists and again if later asset or route identifiers change.

### Ready prompt

```text
You are the active localisation auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, the complete Event 31 specification, final event, decision, mission, focus, idea, character, country, achievement, Event Details, evolution, scenario, world-end, GUI, scripted-localisation, asset, and workbook-facing identifiers.

Audit and make bounded patches for missing keys, duplicate keys, BOM encoding, namespaces, dynamic state and actor text, cost texticons, blocked tooltips, value stages, Event Details wording, evolution rows, scenario type and intensity text, world-end row, route tone, actor names, Muslim opposition representation, victim-centered wording, and cross-surface consistency.

Do not expose hidden readiness, probability, future surprises, prompt language, process notes, or real extremist propaganda. Follow all project prose rules. Do not rewrite unrelated localisation.

Allowed files: <EXACT_FILES>

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_localisation_auditor_handoff.md with keys changed, files, before and after behavior, dynamic-text checks, remaining blockers, and parent follow-up.
```

## 8. `chaosx_portrait_creator`

Use for every Event 31 leader, council, authorized advisor, commander, and the entity.

### Ready prompt

```text
You own complete Event 31 Random Terror portrait production.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-event-assets, chaos-redux-frame-animation for the authorized entity animation, docs/specs/031_random_terror_specs/031_random_terror_spec_part_5_territorial_insurgency_and_country_packages.md, Part 11, the asset prompt, the carrier and character manifest, and exact portrait consumers.

Every subject is fictional_high_chaos or fictional institutional. Use native ImageGen. Do not source or imitate real extremist figures or any real person. Produce the accepted minimum pool of 45 leader and council masters unless the verified simultaneous actor limit requires a documented adjustment. Preserve varied age, gender, appearance, pose, role, and regional context without stereotype. Use exact 156x210 leader framing and matching metadata.

Produce only the route-critical advisor or commander dossiers explicitly authorized in the final manifest, up to 12 under the accepted plan. A dual-role character needs separate role-specific outputs.

Produce the static False Revelation entity portrait. Produce the animation or overlay only after the parent supplies the verified consumer, exact frame brief, sprite names, paths, and frame plan. Follow real per-frame source rules and create a static fallback.

Own portrait-specific processing, DDS, portrait-specific .gfx and existing character references, durable archive, manifests, contact sheets, and handoff. Review accidental resemblance, duplicate faces, identity drift, framing, period fit, symbols, and metadata.

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_portrait_creator_handoff.md with every basename, character, source classification, files, hashes, wiring, review verdict, blocked item, and parent action.
```

## 9. `chaosx_generated_event_art`

Use for report, news, decision-category, flag, faction-emblem, and super-event art.

### Ready prompt

```text
You are the generated non-icon art worker for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-event-assets, chaos-redux-frame-animation when applicable, chaos-redux-super-events for image roles, the Event 31 asset prompt, research notes, and final asset manifest.

Create only the exact authorized fictional assets. Use period-authentic 1936 to 1945 documentary framing for report and news art. Create flat flags through the strict flat ImageGen workflow. Create faction emblems and category pictures for their own surfaces. Create the two super-event images only after final role and text research is stable.

Do not create character portraits. Do not use real extremist names, symbols, sacred calligraphy, modern equipment, generated text, stereotypes, fabric flags, fake UI controls, or primitive placeholders.

Produce source PNGs, processed previews, DDS files, contact sheets, manifests, and gfx_handoff.md. Do not edit gameplay, localisation, GUI, events, focuses, decisions, or workbook files.

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_generated_event_art_handoff.md with files, hashes, prompts, target surfaces, review state, and blockers.
```

## 10. `chaosx_icon_artist`

Use for focus, idea, decision, mission, state, map-mode, faction-surface, and achievement icons.

### Ready prompt

```text
You are the icon artist for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-event-assets, chaos-redux-frame-animation where applicable, the Event 31 asset prompt, final focus IDs, idea lifecycles, decision and mission matrix, state-stage manifest, faction identities, and achievement prompt.

Inspect the exact vanilla reference family and live consumer for every icon type. Create separate source art for focus, idea, decision, mission, state modifier, map mode, faction, and achievement surfaces. Do not satisfy one family by resizing another. Use ImageGen source evidence, real transparency, clear silhouettes, no white matte, no primitive local drawings, no real extremist symbols, no sacred hostile branding, and no readable text.

Create final DDS files, source and processed PNGs, contact sheets, round-trip evidence, manifest rows, and gfx_handoff.md. Achievement assets require completed, grey, and not-eligible triplets with full IDs.

Do not create custom unit counters because Event 31 has no custom unit.

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_icon_artist_handoff.md with every icon ID, source, path, dimensions, hash, consumer, review state, and blocker.
```

## 11. `chaosx_asset_source_researcher`

This event normally uses generated fictional art.

Spawn this worker only when the final implementation deliberately needs a real historical non-portrait image, period symbol, or documented reference for an ordinary government or civic institution.

### Conditional prompt

```text
You are the non-portrait source researcher for one bounded Event 31 historical visual need.

Use fork_context=false.

Repository root: <MOD_ROOT>

Exact asset: <ASSET_ID>
Exact real material required: <SUBJECT>
Reason generation is not acceptable: <REASON>
Target canvas and runtime use: <DETAILS>

Read AGENTS.md, chaos-redux-event-assets, the Event 31 asset prompt, and the exact source requirement. Find a period-appropriate attributed source with usable rights. Preserve original bytes, source URL, author or archive, date, license, checksum, and processing record. Do not source character portraits, real extremist propaganda, sacred hostile branding, modern reenactment, or an unlicensed image.

Write a bounded source and asset handoff. Do not edit gameplay or localisation.
```

Do not spawn this worker as a ritual step for fictional report art.

## 12. `chaosx_super_event_text_researcher`

Use for both super-event text packages.

### Ready prompt

```text
You are the super-event text researcher for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-super-events, the Event 31 super-event prompt, Part 8, Part 11, and research notes.

Research final title, description direction, button text or cultural remark, and main quote for the False Revelation reveal and defeat aftermath. Compare several candidates. Verify exact wording, attribution, source work, date, URL, translation, public-domain or copyright status, and confidence. Do not invent or misattribute text. Do not use Quranic material or sacred Islamic phrases as hostile branding. Preserve ambiguity about the entity.

Do not edit localisation or event files.

Write docs/super_events/031_random_terror_super_event_research.md and a handoff under docs/plans/031_random_terror_plans/subagent_handoffs/ with selected and rejected candidates, sources, confidence, and blockers.
```

## 13. `chaosx_super_event_audio_researcher`

Use for the reveal and defeat tracks.

### Ready prompt

```text
You are the super-event audio researcher for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-super-events, the Event 31 super-event prompt, final text role, and current Chaos Redux audio catalog and sound definitions.

Research two unique licensed or public-domain musical recordings, one for the False Revelation reveal and one for its defeat aftermath. Verify composition and recording rights separately. Reject unclear licensing, generated audio, test tones, oscillators, drones as the entire cue, sound-effect beds, Quran recitation, the call to prayer, Islamic sacred chant, unlicensed commercial recordings, and undocumented legacy audio.

Preserve each original download, URL, title, composer, performer or recording source, license, usage terms, attribution, duration, checksum, and transformation recipe. Prepare a game-ready WAV only through license-permitted mechanical editing. Keep each final cue normally within one to two minutes.

Do not edit sound definitions, event scripts, localisation, or workbook files.

Write permanent research notes and docs/plans/031_random_terror_plans/subagent_handoffs/031_super_event_audio_handoff.md with final files, hashes, proposed sound IDs, volume-wrapper IDs, runtime paths, rights confidence, and blockers.
```

## 14. `chaosx_spreadsheet_doc_worker`

Use only after final in-game-facing wording and implementation facts are stable.

### Ready prompt

```text
You are the spreadsheet worker for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read the spreadsheet skill, docs/spreadsheets/chaos_redux_events_catalog.xlsx, final Event 31 event-name and Event Details localisation, final evolution wording, final Global Jihad scenario wording, and final False Revelation public wording. Do not read broad wiki or vanilla sources.

Update the authoritative workbook only. Align the Event 31 row, the verified Global Jihad scenario row, and the Internal Fracture cluster row only if that cluster has been formally accepted and implemented. Preserve workbook structure, formatting, formulas, filters, and validation.

After saving, run python .tools/export_event_catalog_csv.py. Never edit the CSV exports directly.

Write docs/plans/031_random_terror_plans/subagent_handoffs/031_spreadsheet_handoff.md with workbook fields changed, verified IDs, export result, and blocker.
```

## 15. `chaosx_documentation_curator`

Use during long implementation after several handoffs or before final audit.

### Ready prompt

```text
You are the documentation curator for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read the accepted specification folder, docs/plans/031_random_terror_plans/, final Event 31 docs, asset and super-event manifests, audit reports, and implementation handoffs.

Reconcile documentation only. Build a source-of-truth map, mark superseded notes, record every plan as implemented, promoted, queued with a reason, rejected with a reason, or unresolved, align stable identifiers, and write a resume packet for final audit. Do not edit gameplay, localisation, assets, audio, GUI, GFX, events, focuses, decisions, country files, AI, or spreadsheets.

Write docs/plans/031_random_terror_plans/031_random_terror_documentation_state.md and a curator handoff.
```

## 16. `chaosx_improvement_loop_planner`

The planning package already contains a closure review.

Use this subagent near implementation completion to check whether implementation created a new broad design gap.

Do not spawn a second pass while a previous Event 31 addendum is unresolved.

### Ready prompt

```text
You are the plan-only improvement-loop planner for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-improvement-loop, chaos-redux-event-planning, the complete Event 31 specification, the manual closure review, current implementation, audit handoffs, assets, docs, and unresolved plans.

Determine whether implementation has introduced a broad shallow, disconnected, duplicated, unreadable, or low-impact surface not covered by the accepted specs. Do not add content merely to increase size. Respect the accepted exclusions of custom units, 3D models, dedicated GUI, per-actor bespoke trees, broad advisor rosters, unrelated formables, and a new ideology family.

If no broad gap remains, write a closure handoff listing only final small tasks. If a material new gap exists, write one concrete bounded addendum under docs/plans/031_random_terror_plans/ and explain how it should be promoted into specs if accepted. Do not patch gameplay, localisation, assets, or spreadsheets.
```

## 17. `chaosx_event_completion_auditor`

Use after every implementation, asset, audio, localisation, workbook, and documentation tranche is reconciled.

### Ready prompt

```text
You are the read-only completion auditor for Event 31 Random Terror.

Use fork_context=false.

Repository root: <MOD_ROOT>

Read AGENTS.md, chaos-redux-events, chaos-redux-event-assets, chaos-redux-super-events, chaos-redux-focus-trees, chaos-redux-decisions-missions, chaos-redux-subagents, every file under docs/specs/031_random_terror_specs/, every Event 31 plan and handoff, final implementation files, assets, audio, docs, workbook, and meaningful MCP and probability evidence.

Compare the final repository against every spec part, matrix, achievement, scenario type, intensity, evolution, country profile, focus route, decision family, asset row, super-event package, interaction, cleanup path, and acceptance case. Identify missing content, fallbacks, simplifications, stale docs, unresolved plans, placeholder assets, missing AI, missing probability comparison, and unvalidated terminal behavior.

Do not patch source.

Write docs/plans/031_random_terror_plans/031_random_terror_completion_audit.md with pass, fail, blocked, and needs-user-review findings. Do not call the event complete unless the evidence supports it.
```

## 18. `chaosx_skill_maintainer`

Use only when implementation discovers a reusable workflow, repeated mistake, validation pattern, or project convention that should benefit future events.

Do not put Event 31-specific design into a skill.

### Conditional prompt

```text
You are the skill maintainer for one reusable workflow discovered during Event 31 implementation.

Use fork_context=false.

Repository root: <MOD_ROOT>

Reusable workflow or repeated issue: <WORKFLOW>
Evidence from Event 31: <EVIDENCE>
Relevant existing skills: <SKILLS>

Update the narrowest existing skill when possible. Create a new skill only when the workflow is distinct and reusable. Record paths, commands, validation, handoff rules, and gotchas. Do not include Event 31-specific names, routes, countries, thresholds, or story content. Do not edit gameplay.

Write a skill-maintenance handoff with the files changed and reason.
```

## 19. `chaosx_event_ui_worker`

Do not spawn for the accepted Event 31 design.

Event 31 uses ordinary decision categories, static category pictures, dynamic text, and an event-owned state map presentation.

It introduces no dedicated scripted GUI or mechanic window.

The shared event log, Event Details, settings, Triggerable Scenarios, and super-event framework are explicitly outside this worker's scope.

If implementation later proposes a dedicated Event 31 window, stop and return it for design approval before invoking this worker.

## 20. `chaosx_3d_model_pipeline`

Do not spawn for the accepted Event 31 design.

Event 31 has no custom combat unit, equipment, vehicle, aircraft, ship, creature, building, or articulated model.

Existing HOI4 unit types express its military package.

Adding a custom unit would activate Event 19 provider, model, skeletal animation, sourced unit audio, and bespoke counter obligations. That is outside the accepted specification and requires a new design decision.

## Parent integration checklist

Before relying on a subagent output, the parent must confirm:

- prompt used `fork_context=false`
- allowed files and identifiers were explicit
- output stayed inside scope
- patch handoff lists files and IDs
- probability patches have baseline and comparison evidence
- plans are implemented, promoted, queued, or rejected
- asset outputs are wired or reported blocked
- documentation and workbook agree with final localisation
- unresolved blockers remain visible in the completion report

No subagent owns the final completion claim.

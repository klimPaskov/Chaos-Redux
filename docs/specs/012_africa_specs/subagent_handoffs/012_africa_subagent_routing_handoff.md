# Event 012 Africa — Subagent Routing Handoff

This file provides explicit bounded prompts for project subagents. Each project subagent must be spawned with `fork_context=false`; do not rely on inherited conversation context. The parent implementation agent remains responsible for final integration, review, validation, and completion claims.

## Shared source context for every subagent

Event: `12`, slug `africa`.

Source spec folder:

```text
docs/specs/012_africa_specs/
```

Core files:

- `specs/012_africa_spec_part_1_core.md`
- `specs/012_africa_focus_tree_plan.md`
- `specs/012_africa_decisions_missions_ui.md`
- `specs/012_africa_country_packages_and_subjects.md`
- `specs/012_africa_evolutions_world_end_and_scenarios.md`
- `research/012_africa_research_notes.md`
- `matrices/012_africa_ai_strategy_matrix.md`
- `matrices/012_africa_decision_map.md`
- `matrices/012_africa_asset_matrix.md`
- `matrices/012_africa_acceptance_criteria.md`
- `prompts/012_africa_asset_prompt.md`
- `prompts/012_africa_super_event_prompt.md`
- `prompts/012_africa_achievement_prompt.md`
- `prompts/012_africa_decision_mission_prompt.md`
- `prompts/012_africa_coding_prompt.md`

Global safety constraints:

- Keep source-language court/ruler display-name flavour in localisation only; do not translate it or use raw phrases as ids/assets.
- High-chaos supernatural/nonhuman actors must be explicitly nonhuman or supernatural and must never imply human African peoples are animals or monsters.
- African states should not be instantly annexed by default; use League, regional authorities, and staged integration.
- RSA in Allies gets a civil-war branch and Allied peace after continental victory.
- Final super-event titles, quotes, cultural remarks, and audio are research blockers until sourced.

## chaosx_scripted_system_architect prompt

Read AGENTS.md, relevant event/focus/decision skills, and the Event 012 spec files. Design or implement reusable helpers for:

- selecting a valid African-capital country;
- assigning Event 012 paper cores/claims and later converting them to stable living cores region by region;
- regional authority tracking and cleanup;
- Charter League membership/integration target selection;
- dynamic union names for Africa + Middle East, Asia, Europe, South America, and final world union;
- RSA-in-Allies civil-war routing and Allied peace cleanup;
- continent-unifier sponsorship hooks;
- high-chaos nonhuman actor classification/cleanup;
- script constants for thresholds, costs, timers, and AI weights.

Return helper map with names, scopes, inputs, outputs, side effects, call sites, constants, cleanup plan, validation notes, and risks. Patch only if the changes are narrow and within current implementation scope; otherwise write architecture plan under `docs/plans/012_africa_plans/`.

## chaosx_focus_tree_auditor prompt

After the Africa focus tree/overlay exists, audit it against `specs/012_africa_focus_tree_plan.md` and `focus_graphs/012_africa_focus_tree_architecture.md`. Check:

- route coverage;
- political, industry, military, diplomacy, expansion, diaspora, League, regional authority, high-chaos, post-unification, and world-end branches;
- route locks/mutual exclusions/prerequisites/bypasses;
- focus-decision integration;
- reward diversity;
- idea lifecycle;
- icons/localisation;
- AI weights;
- layout readability;
- exploit risks.

Patch small local focus issues if safe. Write handoff under `docs/plans/012_africa_plans/subagent_handoffs/` with changed focus ids and remaining route risks.

## chaosx_decision_mission_auditor prompt

After decisions/missions/GUI exist, audit against `specs/012_africa_decisions_missions_ui.md` and `matrices/012_africa_decision_map.md`. Check:

- all required categories/families;
- concrete costs beyond PP/CP;
- map objectives;
- active mission caps;
- target selectors/cleanup;
- AI decision validity;
- custom tooltips/localisation;
- duplicate missions;
- integration/coring exploit risk;
- free unit/war-goal/influence loops;
- RSA branch decisions;
- Green Covenant/nonhuman route safety.

Patch small local issues if safe. Write handoff with decision ids, mission ids, category ids, localisation keys, before/after behaviour, validation, and remaining risks.

## chaosx_country_package_auditor prompt

After the selected unifier package, RSA branch, regional authorities, and high-chaos actors exist, audit against `specs/012_africa_country_packages_and_subjects.md`. Check:

- tag/cosmetic tag references;
- country names and ideology-specific names;
- party names;
- leaders/councils/portrait paths;
- flags;
- focus loading and origin flags;
- starting ideas;
- starting units/templates/equipment/manpower;
- reinforcement routes;
- subject/release/annexation safety;
- AI strategy;
- nonhuman classification;
- localisation coverage.

Patch small local package issues if safe. Write handoff with changed tags, leaders, state groups, focus-tree ids, localisation keys, validation, and remaining risks.

## chaosx_localisation_auditor prompt

After visible gameplay text exists, audit Event 012 localisation and scripted localisation. Check:

- missing keys;
- duplicate keys;
- dynamic values in tooltips;
- event name/debug name/event log/detail/evolution text;
- focus, decision, idea, country, achievement, super-event keys;
- tooltip clarity for costs and map requirements;
- no mechanical effect lists in event detail text;
- source-language court/ruler display-name flavour kept untranslated and out of ids/assets;
- no unsafe human/nonhuman wording;
- no unresearched quote/title/audio text pasted as final localisation.

Patch small local text issues if safe. Write handoff with keys changed and remaining wording decisions.

## chaosx_icon_artist prompt

Use `prompts/012_africa_asset_prompt.md` and `prompts/012_africa_achievement_prompt.md`. Produce generated icon packages for focus icons, idea/national-spirit icons, decision icons, decision-category icons, achievement icons, formable seals, and small animated icon/seal sprites. Follow `chaos-redux-event-assets` and `chaos-redux-frame-animation` for animated assets. Inspect reference folders before generation. Do not edit gameplay/GFX files. Output manifest and `gfx_handoff.md` under `docs/assets/012_africa/`.

## chaosx_generated_event_art prompt

Use `prompts/012_africa_asset_prompt.md`. Produce generated non-icon fictional/alternate-history assets: report images, news images, super-event images, fictional route flags, fictional council portraits, UI panels, regional authority emblems, supernatural/nonhuman portraits, and high-chaos art. Follow source-mode rules and do not generate real leaders or historical flags. Output source PNGs, processed PNGs, DDS/TGA where appropriate, manifest, contact sheets, and `gfx_handoff.md`.

## chaosx_asset_source_researcher prompt

Use `prompts/012_africa_asset_prompt.md`. Source real/archival assets only where the spec calls for real materials: RSA/Smuts branch if real leader imagery is used, historically attested flags/symbols if selected by implementation, and any real historical report/news image. Record URL, archive, author, date, license/public-domain status if available, source path, processed path, final DDS/TGA path, and uncertainty. Do not edit gameplay/GFX files.

## chaosx_super_event_text_researcher prompt

Use `prompts/012_africa_super_event_prompt.md` and `research/012_africa_research_notes.md`. Research final quote candidates, exact wording, attribution, source confidence, and final button/cultural remark recommendations for each Africa super-event role. Do not invent quotes. Keep modern copyrighted references short. Output `docs/super_events/012_africa_super_event_research.md` entries.

## chaosx_super_event_audio_researcher prompt

Use `prompts/012_africa_super_event_prompt.md`. Check existing approved Chaos Redux tracks first, then research licensed/public-domain music where needed. Each completed Africa super-event should have unique final audio unless exact reuse is approved. Download from legitimate source, preserve original, convert to `.ogg`, document title/creator/source/license/duration/usage terms, and output audio handoff. Do not edit sound definitions or event files.

## chaosx_event_completion_auditor prompt

Before final completion, audit implementation against the entire Event 012 spec pack and accepted subagent handoffs. Check every required surface: event script, registration, log/details, evolutions, focus tree, decisions/missions/GUI, country packages, regional authorities, RSA branch, high-chaos/nonhuman actors, assets, super-events, achievements, AI, docs, spreadsheet, validation, and simplification reporting. Read-only. Write audit under `docs/plans/012_africa_plans/subagent_handoffs/` or return report.

## chaosx_spreadsheet_doc_worker prompt

Only after implementation facts and in-game localisation exist, update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` row for Event 12. Use the spreadsheet skill only. Do not edit gameplay/docs. Make Details/Evolution/World-End/Cluster wording match in-game event detail and evolution detail text exactly where fields mirror player-facing UI. Preserve workbook structure.

## chaosx_documentation_curator prompt

After implementation and audits, reconcile docs/specs/plans/handoffs/manifests for Event 012. Mark accepted plans implemented/queued/rejected/superseded. Create source-of-truth/resume packet if needed. Do not edit gameplay/localisation/assets/spreadsheets.

## Consolidated older expansion notes

Older V2 expansion handoffs have been folded into the source spec pack. Implementation agents should treat the niche-polity expansion, Authority Atlas, Archive of Old Seats, high-chaos absurd routes, and nonhuman/supernatural actor rules as accepted source design.

Current source files for that layer are:

- `specs/012_africa_niche_polities_and_subjects.md`
- `specs/012_africa_high_chaos_absurd_paths.md`
- `specs/012_africa_niche_polities_and_absurd_paths.md`
- `specs/012_africa_niche_country_expansion.md`
- `matrices/012_africa_expanded_subject_matrix.md`
- `matrices/012_africa_absurd_high_chaos_routes_matrix.md`
- `research/012_africa_niche_polities_research_notes.md`

Human historical authorities are political and cultural actors, not caricatures. Nonhuman and supernatural actors must use explicit nonhuman/supernatural classification and generated or symbolic assets. Source-language court/ruler joke names are localisation flavour, not historical polity names or internal ids.

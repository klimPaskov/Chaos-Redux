# Coding-Agent Prompt — Implement Event 012 Africa

Implement Event ID `12`, **Africa**, from the full source package under:

```text
docs/specs/012_africa_specs/
```

This is a major rework of a Minor Fire-Once event in the Formables cluster. Do not implement a small fallback, thin focus ladder, instant-core shortcut, or placeholder country package. Do not claim completion until the implemented files satisfy the specs, prompt files, matrices, assets, localisation, docs, and catalog-alignment requirements.

## Required reading

Read and follow `AGENTS.md` plus the Chaos Redux skills for events, event planning, improvement loop, subagents, focus trees, decisions/missions, event assets, frame animation, and super-events. Use the offline Paradox wiki and vanilla HOI4 documentation required by AGENTS for every touched system. Inspect existing Chaos Redux patterns before editing.

## Source files

Implement from the whole folder, with priority on:

- `CURRENT_SOURCE_OF_TRUTH.md`
- `specs/012_africa_spec_part_1_core.md`
- `specs/012_africa_focus_tree_plan.md`
- `specs/012_africa_decisions_missions_ui.md`
- `specs/012_africa_country_packages_and_subjects.md`
- `specs/012_africa_evolutions_world_end_and_scenarios.md`
- `specs/012_africa_niche_country_expansion.md`
- `specs/012_africa_niche_polity_expansion.md`
- `specs/012_africa_niche_polities_and_absurd_paths.md`
- `specs/012_africa_niche_authorities_high_chaos_expansion.md`
- `specs/012_africa_high_chaos_absurd_paths.md`
- `research/012_africa_research_notes.md` and niche-polity research notes
- `matrices/012_africa_ai_strategy_matrix.md`
- `matrices/012_africa_decision_map.md`
- `matrices/012_africa_asset_matrix.md`
- `matrices/012_africa_acceptance_criteria.md`
- `prompts/012_africa_asset_prompt.md`
- `prompts/012_africa_super_event_prompt.md`
- `prompts/012_africa_achievement_prompt.md`
- `prompts/012_africa_decision_mission_prompt.md`

## Non-negotiables

1. Event 12 selects a valid African-capital country and proclaims the “Africa is one” unifier fantasy.
2. The selected country changes cosmetic identity and receives continental paper cores/claims, but stable cores require staged integration work.
3. African countries are not instantly annexed. They can join the Charter League, be defended, receive aid, become regional authorities, resist integration, leave, or fight back.
4. If RSA is selected while in the Allies, run the RSA civil-war branch and make the Allies peace out if the continental side wins.
5. Implement a large non-linear Africa focus tree or overlay with political, industry, military, diplomacy, expansion/integration, diaspora, League, regional authority, Archive/Authority Atlas, high-chaos, post-unification, continent-sponsor, and world-end branches where unlocked.
6. Implement decisions and missions with real costs and objectives: equipment, manpower, XP, trains, convoys, fuel, supply, construction capacity, state control, division placement, legitimacy, local trust, League cohesion, and time pressure where appropriate. Do not turn the system into a PP/CP store.
7. Expose the main values clearly: Legitimacy, Authority, League Cohesion, Liberation Momentum, Regional Trust, Colonial Alarm, Paper-Core Burden, Covenant Pressure, Archive Mandate, Old-Seat Legitimacy, Local Sovereignty, Restoration Debt, Mythic Pressure, Nonhuman Sovereignty, Bestiary Alarm, Habitat Trust, and Mythic Volatility.
8. Implement dynamic starting forces and reinforcement routes for the unifier, RSA continental side, regional authorities, restoration subjects, and nonhuman/high-chaos actors that are meant to fight.
9. Implement the Archive of Old Seats / Authority Atlas with at least 24 historical dossiers and at least 6 high-chaos nonhuman/supernatural packages represented in gameplay.
10. Keep human historical polities human, researched, and institutionally framed. Nonhuman/supernatural actors are explicit fictional/high-chaos entities and must not replace or caricature human African communities.
11. Country/cosmetic names must be direct names from the country-package spec, with ideology variants where useful. Do not name countries after generic offices, compacts, boards, bureaus, missions, or guards. Leader/court display names use the source-language joke pool in `specs/012_africa_country_packages_and_subjects.md`; keep those strings untranslated in player-facing English and out of internal ids/assets.
12. Implement Evolutions I–IV, Scramble for Africa, post-unification continent sponsorship, dynamic Afro-Middle Eastern/Afro-Asian/Afro-Eurasian/etc. identities, and the terminal World Is One branch only after all continent-unifier prerequisites.

## Assets, achievements, and super-events

Use the asset, achievement, decision/mission, and super-event prompt files. Super-event final titles, button remarks, quotes, cultural references, and audio are blockers until researched and documented through the proper workflow. Do not paste role labels or working names as final localisation.

Assets need correct source mode, manifests, final DDS files, static fallbacks for animated assets, and GFX handoff notes. Historical flags/symbols and real leaders require sourced asset work; fictional, symbolic, supernatural, and impossible assets may be generated through the asset workflow.

Achievements must reward difficult route completion, rare branches, high-chaos paths, League management, Archive/Authority Atlas mastery, nonhuman route management, RSA branch victory, post-unification sponsorship, and World Is One. Do not make achievements automatic event-fire rewards.

## Subagents and audits

Use project subagents with `fork_context=false` where appropriate: scripted-system architect for reusable helpers, focus/decision/country/localisation auditors for implementation surfaces, asset and super-event research subagents for real packages, documentation curator when docs drift, completion auditor before final completion, and spreadsheet worker only after implementation facts and in-game wording exist. Patch handoffs belong under `docs/plans/012_africa_plans/subagent_handoffs/`.

## Validation and report

Run meaningful task-specific validation: Event 12 registration/log/detail/evolution wiring; valid target and N/A behaviour; RSA-in-Allies branch; focus route coverage; decision/mission costs, timers, AI, cleanup, and clutter; country package tags, leaders/councils, flags, units, focus loading, AI; asset manifest/GFX handoff completeness; super-event source documentation; achievement tracking; nonhuman classification; exploit checks for free units, instant cores, war-goal spam, and annex/puppet shortcuts; docs and catalog alignment.

The final report must list files changed, systems touched, route coverage, decision families, mechanic values, country packages, Authority Atlas coverage, evolutions, super-events, assets, achievements, AI behaviour, validation results, simplifications, omissions, fallbacks, and blockers. If any spec requirement is not fully implemented, report the goal as incomplete.

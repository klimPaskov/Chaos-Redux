# Event 22 Concentration Camps Specification Pack

## Package identity

- Event ID: `22`
- Event slug: `concentration_camps`
- Intended repository folder: `docs/specs/022_concentration_camps_specs/`
- Event type: Minor Repeatable
- Development status: To Be Reworked
- Intended cluster: Random Chaos

This folder is the source design handoff for the complete Event 22 rework. It replaces the old Spain-specific concept. The event now creates and develops camp networks in randomly selected countries, connects those networks to the shared Camps and Genocide system, and gives every affected country a real crisis to manage.

## Design summary

A normal firing selects one eligible country and brings active concentration-camp coverage to 20 percent of that country’s eligible states. Existing compatible camp buildings count toward the target. The selected country must respond through a compact decision category. It can freeze intake and dismantle the network, place the sites under restrictive review, exploit detainees through forced labour, expand the network, conceal evidence, or, after Evolution I, convert part of the network into extermination sites.

Camp operation removes real state population and registers the exact applied loss in the Deaths system. Forced labour can provide strong short-term local output, construction, logistics, or resource gains, but those gains consume a finite detained workforce and create escalating deaths, resistance, sabotage, guard burdens, disease, evidence, foreign pressure, and postwar liability. Extermination sites focus on killing and terror. They do not become a stable production strategy.

The event reuses the existing `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` buildings, the shared camp attribution rules, the hidden evidence system, the Condemnation system, and the exact civilian-population-loss effects. It must not create a second parallel atrocity framework.

## Locked interpretations

The following points resolve ambiguities in the rough concept.

1. The baseline 20 percent is calculated within one selected country, not across the whole world. Repeated firings spread the crisis to more countries or reactivate a former network.
2. Evolution III means that 50 percent of the selected country’s eligible states contain camps in total. Those camp states are split as evenly as possible between concentration camps and extermination camps. It does not mean 100 percent state coverage.
3. Evolution II and Evolution III population percentages are one-time evolution shocks. They do not replace the continuing dynamic death process.
4. When an active network progresses from Evolution II to Evolution III, its existing camp states can suffer the earlier 1 percent shock and the later additional 2 percent shock. A country whose first firing begins at Evolution III receives only the 2 percent opening shock, because the earlier in-play crisis never occurred.
5. “Genocide” is not used as a generic label for every camp death. The term applies only when the campaign establishes the required destructive intent against a qualifying protected group. Other conduct can still be mass detention, forced labour, persecution, mass killing, or crimes against humanity.
6. HOI4 does not contain a reliable ethnicity-demography model. Generic target selection therefore uses campaign markers such as occupied non-core populations, refugees, resistance detainees, ideological persecution, and country-specific historical registries. It must never invent race percentages from cores, ideology, or state ownership.
7. The rough idea’s “controlled genocide” framing is rejected as a balance principle. A regime can obtain temporary coercive output or hardliner support. The design does not permit a sustainable, clean, or dominant atrocity strategy.
8. Ordinary prisoner-of-war camps and lawful civilian security internment are outside Event 22. The event requires arbitrary political detention, persecution, forced labour, extermination, or comparable abuse.

## Player-facing mechanic

The main decision category exposes three values:

- Network Reach, showing how much of the country is covered by operational sites
- Exposure, showing how close hidden evidence is to public verification
- Resistance Pressure, showing escape networks, sabotage, local opposition, and guard strain

The shared Condemnation value remains in the Chaos Meter and is not duplicated as a fourth Event 22 value. State tooltips show the local site type, assignment, workforce condition, operational status, and discovery state.

## Presentation choice

The event uses an ordinary decision category with one strong static archival category picture. The three values are communicated through concise category text, status bands, icons, state modifiers, and tooltips. This keeps the mechanic readable while decisions, state targets, and shared system links carry the gameplay.

## File map

### Source specifications

- `022_concentration_camps_spec_part_1_core.md`
- `022_concentration_camps_spec_part_2_baseline_and_decisions.md`
- `022_concentration_camps_spec_part_3_evolutions_and_variants.md`
- `022_concentration_camps_spec_part_4_discovery_liberation_aftermath.md`
- `022_concentration_camps_spec_part_5_integrations_balance_presentation.md`

### Supporting matrices and handoffs

- `022_concentration_camps_event_chain_map.md`
- `022_concentration_camps_decision_map.md`
- `022_concentration_camps_ai_probability_matrix.md`
- `022_concentration_camps_achievements.md`
- `022_concentration_camps_asset_manifest.md`
- `022_concentration_camps_research_notes.md`
- `022_concentration_camps_catalog_handoff.md`
- `022_concentration_camps_acceptance_criteria.md`

### Implementation prompts

- `022_concentration_camps_asset_prompt.md`
- `022_concentration_camps_achievement_prompt.md`
- `022_concentration_camps_decision_mission_prompt.md`
- `022_concentration_camps_coding_prompt.md`
- `022_concentration_camps_goal_prompt.md`


## Source and tooling status

All supplied project Markdown files, TOML files, CSV exports, spreadsheet skill files, and every subagent TOML contained in `subagents.zip` were read before this package was completed. The current CSV export still lists Event 22 as “Spain Antisemitism,” Minor Fire-Once, Unavailable, with no cluster. That row is an export snapshot and must be updated through the authoritative workbook during implementation.

The custom Chaos Redux subagent runtime and the HOI4 MCP inspection tools were not available in this planning environment. No subagent execution or live MCP proof is claimed. Their prompts and audit requirements are incorporated into the implementation handoffs. The implementation remains responsible for the required probability, event, decision, asset, localisation, spreadsheet, completion, and improvement-loop passes.

## Reviewed source inventory

### Supplied project files

The planning pass read these supplied sources in full:

- `AGENTS(7).md`
- `CHAOS_REDUX_MECHANICS(7).md`
- `chaos-redux-3d-model-pipeline(3).md`
- `chaos-redux-comfyui(2).md`
- `chaos-redux-debug-playtest(2).md`
- `chaos-redux-decisions-missions(3).md`
- `chaos-redux-event-assets(7).md`
- `chaos-redux-event-planning(20260813-152954).md`
- `chaos-redux-events(8).md`
- `chaos-redux-focus-trees(3).md`
- `chaos-redux-frame-animation(8).md`
- `chaos-redux-improvement-loop(8).md`
- `chaos-redux-subagents(8).md`
- `chaos-redux-super-events(7).md`
- `chaosx_dynamic_effects.md`
- `chaosx_dynamic_triggers.md`
- `config.toml`
- `chaos_redux_events_catalog(3).csv`
- `chaos_redux_clusters_catalog(3).csv`
- `chaos_redux_scenarios_catalog(3).csv`

The spreadsheet skill and its API quick-start reference were also read because the final implementation must update the authoritative XLSX and regenerate its CSV exports.

### Subagent files inside `subagents.zip`

The planning pass extracted and read all 20 supplied subagent definitions:

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

The specifications use the relevant ownership and handoff rules from these definitions. No subagent execution is claimed in this environment.

# Camp and Repression Rework: Repository Explorer File Map

> **Superseded preimplementation snapshot.** This file records the repository state explored on 2026-07-10 before the camp repression implementation tranche. Its absence findings, candidate file map, and proposed edit order are historical evidence only. Use `source_of_truth_and_completion_tracker.md` and `completion_report.md` for current files, identifiers, implementation status, and remaining gates.

Date: 2026-07-10

Mode: read-only repository exploration. This handoff does not alter gameplay, localisation, assets, specifications, or the event catalog.

## 1. Historical executive result

The repository has a functioning but narrow genocide-crisis scaffold. It already owns three camp buildings, state registration, monthly deaths, discovery on control change, hidden/public condemnation, a small foreign-response layer, Germany/Japan/Soviet decisions, and bridges into the Chaos Meter Deaths system, the condemnation system, chemical contamination, the Mengele chain, and Soviet Collapse.

It does not yet implement the accepted rework's shared camp lifecycle, Repression Ledger, staged national consequences, country kits beyond Germany/Japan/Soviet, Ishii/Pingfang system, Soviet paranoia/famine chain, reform/dismantlement path, complete unregister/cleanup semantics, focus hooks for the named majors, or catalog alignment.

Three issues must be resolved before implementation proceeds:

1. The accepted specification package contradicts itself on chemical/biological killing-efficiency mechanics. README, Parts 1, 4, and 7, and the research use rules prohibit efficiency curves and require a consequence/evidence model. Several prompts and the continuation prompt explicitly ask to add chemical and biological killing-efficiency mechanics or controls. The safe core specifications should be treated as authoritative, but the contradictory prompt text must be corrected or explicitly rejected in the source-of-truth tracker before coding.
2. common/scripted_effects/germany_mengele_effects.txt is already modified in the shared worktree. The accepted rework must touch this file. Ownership and merge order must be established before any patch to it.
3. The current monthly host pulse performs an every-country scan every month to discover newly constructed camps. This contradicts the rework's array-only performance requirement and the repository rule against whole-world periodic iteration. The rework should replace that scan with event-driven registration or another bounded mechanism; it must not add another periodic scan.

## 2. References consulted

Required offline wiki pages consulted:

- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md
- paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Effects - Hearts of Iron 4 Wiki.md
- paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md
- paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md
- paradox_wiki/On actions - Hearts of Iron 4 Wiki.md
- paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Interface Modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Scripted GUI Modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/National Focus Modding - Hearts of Iron 4 Wiki.md

Required vanilla documentation consulted:

- documentation/script_concept_documentation.md
- documentation/effects_documentation.md
- documentation/triggers_documentation.md
- common/decisions/_documentation.md
- common/on_actions/_documentation.md
- common/scripted_guis/_documentation.md
- common/script_constants/documentation.md
- common/focus_inlay_windows/documentation.md

Accepted package consulted in full:

- docs/specs/system_camp_repression_rework_specs/README.md
- docs/specs/system_camp_repression_rework_specs/package_index.md
- all files under research, matrices, specs, prompts, source_review, and continuation

Current project documentation consulted:

- docs/systems/genocide_crisis_system.md
- docs/systems/genocide_mechanics_spec.md
- docs/systems/chaos_meter_deaths_mechanic.md
- docs/systems/chaos_meter_deaths_and_events_log_ui.md
- docs/systems/condemnation_sanctions.md
- docs/events/germany_mengele/overview.md
- docs/events/005_soviet_collapse/overview.md
- docs/chemical_warfare/japan_chemical_campaign_decisions.md
- docs/chemical_warfare/chemical_warfare_documentation.md
- docs/biological_warfare/biowarfare_system.md

## 3. Source-of-truth contradiction

The following surfaces prohibit chemical/biological killing-efficiency optimization and instead call for a consequence-heavy contaminated-evidence branch:

- README.md
- system_camp_repression_rework_spec_part_1_core_loop.md
- system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md
- system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md
- research/historical_anchor_notes.md
- research/continuation_historical_sources.md

The following surfaces contain conflicting instructions to add chemical and biological killing-efficiency mechanics or controls:

- prompts/system_camp_repression_rework_coding_prompt.md
- prompts/system_camp_repression_rework_goal_prompt.md
- prompts/system_camp_repression_rework_gui_prompt.md
- prompts/system_camp_repression_rework_validation_prompt.md
- continuation/continuation_prompt.md

Required resolution: record that the safe core specification wins, remove or supersede the conflicting lines, and define the current restricted chemical site decision as either:

- removed/replaced by a contamination, evidence, exposure, and condemnation consequence branch; or
- retained only if the user explicitly approves it as compatible with the safety boundary.

No fallback should be silently selected.

## 4. Current live architecture and exact behavior

### 4.1 Buildings

Primary file: common/buildings/chaosx_buildings.txt

- concentration_camp at line 107 is directly buildable, maximum level 1, and globally available because the building definition has no country or route gate. Its state modifiers reduce local manpower and compliance, slightly reduce resistance target, and increase resources and production.
- extermination_camp at line 143 is not directly buildable, hidden when absent, maximum level 1, and applies much harsher manpower/compliance/production effects.
- gulag_labor_camp_network at line 180 is not directly buildable, maximum level 1, and combines manpower/compliance losses with resource and production gains.

Existing presentation:

- interface/chaosx_buildings.gfx registers the three building icons.
- gfx/interface/buildings/building_concentration_camp.dds
- gfx/interface/buildings/building_extermination_camp.dds
- gfx/interface/buildings/building_gulag_labor_camp_network.dds
- gfx/entities/chaosx_buildings.asset supplies map entities for the established building set, but the gulag network does not have a comparable bespoke entity implementation.
- localisation/english/chaosx_buildings_l_english.yml owns building names and descriptions.

Important gap: the accepted design calls for ideology, route, country-kit, and state-pool gates, but concentration camps are currently available through ordinary construction to any country.

### 4.2 Constants and tunable values

Primary file: common/script_constants/genocide_crisis_constants.txt

It currently centralizes:

- monthly Deaths percentages and caps for concentration, extermination, gulag, deportation, forced labor, terror, evidence destruction, experiments, famine pressure, and restricted chemical sites;
- crisis escalation, visibility, cover-up, and hardliner values;
- discovery/condemnation thresholds;
- AI weights for the generic, German, Japanese, and Soviet decisions;
- the restricted chemical bridge, including cylinder gates/costs and contamination dose/duration;
- Soviet Collapse bridge deltas.

Missing accepted value families include camp_network_reach, labor_output, security_intensity, abuse_intensity, disease_pressure, evidence_exposure, reform_progress, Ishii/Pingfang variables, durable Soviet famine/paranoia/NKVD variables, country-kit thresholds for UK/Raj/USA/France/Vichy/Italy/Belgium/Congo, and GUI display cache values.

Recommended ownership: extend this file only for values tightly coupled to the existing genocide system; use a new subsystem script-constant file if the accepted implementation separates shared lifecycle values from country-package tables. Do not duplicate file-scoped @ constants across gameplay files.

### 4.3 Registration, monthly effects, discovery, and cleanup

Primary file: common/scripted_effects/genocide_crisis_effects.txt

Key live effects:

- country initialization: genocide_initialize_country_variables at line 31.
- condemnation bridges: genocide_register_public_condemnation_source at 56, genocide_register_hidden_condemnation_source at 75, and genocide_register_hidden_coverup at 86.
- state list registration: genocide_track_state_for_monthly_pulse at 160.
- concentration registration: genocide_register_concentration_site_for_root at 349.
- extermination registration: genocide_register_extermination_site_for_root at 386.
- gulag registration: genocide_register_gulag_site_for_root at 444.
- construction wrappers: genocide_build_concentration_camp_in_from, genocide_build_extermination_camp_in_from, and genocide_build_gulag_network_in_from at 479-493.
- per-site monthly handlers at 500-600.
- combined monthly state handler: genocide_apply_monthly_state_effects at 614.
- construction rescan: genocide_register_constructed_concentration_camps at 650.
- global pulse: genocide_monthly_global_pulse at 671.
- discovery calculation/application/event chain at 723-926.
- current Germany/Japan/Soviet and generic decision helpers at 974-1500.
- historical GER/JAP/SOV initialization at 1557-1654.
- system initialization at 1654.

Registration currently stores a country pointer in the state variable genocide_responsible_country, adds genocide_site_has_responsible_country, and places the state into global.genocide_active_camp_states.

The active-state array is append-only. There is no corresponding unregister helper. A dismantled, lost, invalid, or otherwise inactive site can remain in the array indefinitely. Monthly processing generally skips states that no longer satisfy site conditions, but stale entries remain a performance and display risk.

The monthly state handler uses independent if blocks. Effects therefore stack when a state has multiple buildings/flags:

- concentration plus extermination both apply;
- an Auschwitz/SS laboratory can apply a building death pulse plus experiment pulse;
- a Japanese experimental site applies both generic experiment and biowarfare-experiment pulses;
- an active restricted chemical flag adds another pulse.

The accepted pressure model must explicitly decide whether those layers are intended and show the exact combined result in the ledger. Otherwise this is accidental double counting.

The construction rescan performs every_country and then inspects controlled states each month. This is the largest existing performance conflict. The global array does not achieve array-only processing while that rescan remains.

Discovery is event-driven through state control change. It detects a discoverer different from the stored responsible country, exposes hidden condemnation/cover-up into public sources, applies stability and thresholds, and fires first-discovery and global-news events. This is the strongest reusable part of the current system.

### 4.4 On actions

- common/on_actions/genocide_crisis_on_actions.txt
  - on_startup at line 10 initializes once through a random country.
  - on_state_control_changed at line 19 calls genocide_on_state_control_changed.
  - on_capitulation at line 25 handles tribunal follow-up.
- common/on_actions/chaosx_on_actions_chaos_meter.txt
  - on_monthly at line 53 is guarded to the global host/player country and calls genocide_initialize_system_if_needed and genocide_monthly_global_pulse at lines 63-64.

The host guard prevents the top-level on_monthly effect from doing substantive work for every country, but the called construction rescan still performs an explicit every_country traversal. Keep the existing host pulse if useful; remove the rescan rather than adding another world loop.

Potential event-driven registration surfaces:

- the scripted construction wrappers;
- historical initializer;
- country-kit state-targeted build decisions;
- any relevant building-completion hook that is proven by current engine documentation/vanilla;
- state-control change for ownership/responsibility validation.

### 4.5 Decisions and categories

Category file: common/decisions/categories/genocide_crisis_categories.txt

- genocide_crisis_category at line 9.
- imperial_occupation_crisis at line 43.
- gulag_and_mass_repression_system at line 58.
- genocide_foreign_response_category at line 75.

Decision file: common/decisions/genocide_crisis_decisions.txt

Germany:

- germany_wartime_camp_administration at line 69.
- germany_expand_occupied_poland_camp_system at 96.
- germany_expand_extermination_site_network at 134.
- germany_intensify_extermination_policy at 182.
- germany_transfer_prisoners_to_experiment_site at 210.

Shared/current:

- genocide_restricted_chemical_site_escalation at 264.
- genocide_build_extermination_camp at 296.
- operational management at 379-530.
- evidence destruction/dismantlement/cover-up at 551-631.

Japan:

- japan_expand_forced_labor_camps at 652.
- japan_conduct_anti_partisan_reprisals at 697.
- japan_transfer_prisoners_to_experimental_facilities at 737.
- japan_destroy_occupation_records at 783.

Soviet:

- visibility toggles at 820 and 836.
- sov_expand_gulag_network at 852.
- deportation, famine requisition, purge, quotas, and records at 914-1115.

Foreign:

- survivor testimony, resistance support, and tribunal preparation at 1155-1220.

Most generic camp-management responses are visible only to AI. A human player does not currently receive the accepted lifecycle choice set.

Target-pool gaps:

- Germany's transfer decision can target any controlled active site and does not enforce occupied Poland/non-core priority before German cores.
- Japan is gated to Chinese-core/Chinese-war contexts but has no Pingfang hierarchy or Ishii influence.
- the Soviet pool uses a small hard-coded state list or broad non-core/resistance fallback rather than the accepted reusable pool model.
- UK/Raj, USA, France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and generic gated packages are absent.

### 4.6 Triggers

Primary file: common/scripted_triggers/genocide_crisis_triggers.txt

It owns existing crisis visibility, active-site checks, GER/JAP/SOV state eligibility, discovery status, and foreign-response conditions. It should remain the central home for reusable country/state pool gates.

Required additions:

- shared active-site/lifecycle-stage checks;
- reusable state pool triggers with core/non-core/occupied/colonial/resistance and priority rules;
- country-kit route availability;
- reform/dismantlement eligibility;
- site owner/responsibility validity and unregister predicates;
- safe Ishii/Pingfang and Mengele archive/project gates;
- Soviet paranoia system-active checks and Soviet Collapse bridge checks.

Do not scatter identical state-pool logic through each decision.

### 4.7 Ideas and dynamic modifiers

Current ideas: common/ideas/genocide_crisis_ideas.txt

- radical_hardliner_support.
- genocide_rail_deportation_priority.
- genocide_tribunal_preparation.
- genocide_military_objections_suppressed.

Current dynamic modifiers: common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt

- genocide_concentration_camp_network_state at line 26.
- forced-labor, sabotage, evidence-burned, refugee, and foreign-resistance state modifiers at lines 34-64.

The accepted staged national lifecycle consequences, country-specific spirits, reform track, disease/abuse/security/labor pressure layers, and public-exposure consequences do not exist. These files are direct touchpoints. New sprites should be named and registered only after the final idea/modifier IDs are stable.

### 4.8 AI

Current file: common/ai_strategy/genocide_crisis_ai_strategy.txt

It contains:

- active regime runtime;
- limited prewar, wartime, and occupied-territory camp construction strategies;
- exposed-regime behavior;
- Japanese occupation runtime;
- Soviet repression runtime.

Only Germany, Japan, and the Soviet Union receive specialized coverage. The strategies affect broad building priorities and army behavior but do not guarantee accepted state-pool priority. The AI decision weights in the constants/decisions also lack the Part 5 country packages, reform pathways, player-facing pressure logic, and bounded escalation caps.

Required AI work belongs in:

- common/ai_strategy/genocide_crisis_ai_strategy.txt or a new country-kit file;
- ai_will_do blocks in common/decisions/genocide_crisis_decisions.txt;
- shared scripted triggers for route and site caps.

### 4.9 Deaths and Chaos Meter integration

Primary effect: common/scripted_effects/chaos_meter_effects.txt

- chaos_meter_register_deaths owns general death accounting.
- chaos_meter_register_state_civilian_deaths_percent at line 3198 converts state population percentages into civilian Deaths, applies population loss, updates country/global totals, and raises Chaos.

Reason IDs are centralized in common/script_constants/chaos_meter_constants.txt, including camp, extermination, and gulag reason types.

Current UI:

- common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt.
- common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt.
- interface/chaosx_chaos_meter_popup.gui.
- interface/chaosx.gfx and related Chaos Meter sprite files.
- localisation/english/chaosx_chaos_meter_l_english.yml.

The accepted Repression Ledger does not exist. No live identifier named repression_ledger, camp_network_reach, or the Part 6 display cache variables was found outside the accepted specification package.

The least risky UI architecture is a dedicated decision category with a header scripted GUI, using the existing decision-category context precedent. Reusing the Chaos Meter popup is possible but creates a larger coupling surface and should not be assumed.

### 4.10 Condemnation integration

Primary files:

- common/script_constants/condemnation_sanctions_constants.txt.
- common/scripted_effects/condemnation_sanctions_effects.txt.
- common/scripted_triggers/condemnation_sanctions_triggers.txt.
- common/decisions/condemnation_sanctions_decisions.txt.
- common/decisions/categories/condemnation_sanctions_categories.txt.
- common/dynamic_modifiers/condemnation_sanctions_dynamic_modifiers.txt.
- common/ideas/condemnation_sanctions_ideas.txt.
- localisation/english/condemnation_sanctions_l_english.yml.
- docs/systems/condemnation_sanctions.md.

The system already separates hidden and public source buckets and provides contexts for camp discovery, experiments, restricted chemical sites, inspections, observers, operations, restricted operations, and destroyed records. The camp system also has its own 25/50/75/100 threshold events. The rework should preserve the shared condemnation ledger but explicitly reconcile these two threshold systems rather than adding a third.

### 4.11 Chemical and biological warfare integration

Relevant chemical files:

- common/script_constants/chemical_warfare_constants.txt.
- common/scripted_effects/chemical_warfare_effects.txt.
- common/decisions/chemical_warfare_decisions.txt.
- common/decisions/japan_chemical_campaign_decisions.txt.
- common/raids/chemical_nerve_raids.txt.
- common/special_projects/projects/chemical_warfare_nerve_projects.txt.
- common/equipment and technologies files referenced by the chemical documentation.

Current camp bridge:

- genocide_apply_restricted_chemical_site_escalation_in_from at common/scripted_effects/genocide_crisis_effects.txt line 1341.
- it consumes chemical_soman_payload_cylinder_1 or chemical_sarin_payload_cylinder_1, sets persistent evidence plus a timed active flag, calls chem_apply_state_contamination, and applies immediate and monthly Deaths.

This is functionally close to the prohibited efficiency mechanic and is the concrete place where the source-of-truth conflict must be resolved.

Relevant biological files:

- common/script_constants/biowarfare_constants.txt.
- common/scripted_effects/biowarfare_effects.txt.
- common/decisions/biowarfare_disease_containment_decisions.txt.
- common/dynamic_modifiers/biowarfare_state_modifiers.txt.
- common/special_projects/projects/biowarfare_main_projects.txt.
- common/special_projects/prototype_rewards/generic_biowarfare_prototype_rewards.txt.
- interface/special_projects/biowarfare.gfx.
- docs/biological_warfare/biowarfare_system.md.

The Japanese prison-experiment decision already rolls possible anthrax, tularemia, or plague contamination. It has no outbreak-accident risk variable, Pingfang facility progression, Ishii influence, Kwantung autonomy, or containment branch.

### 4.12 Germany/Mengele integration

Primary files:

- common/script_constants/germany_mengele_constants.txt.
- common/scripted_effects/germany_mengele_effects.txt.
- common/scripted_triggers/germany_mengele_triggers.txt.
- common/decisions/germany_mengele_decisions.txt.
- common/decisions/categories/germany_mengele_categories.txt.
- common/ideas/germany_mengele_ideas.txt.
- common/dynamic_modifiers/germany_mengele_dynamic_modifiers.txt.
- common/ai_strategy/germany_mengele_ai_strategy.txt.
- events/germany_mengele.txt.
- common/special_projects/projects/mengele_cloning_projects.txt.
- common/national_focus/germany_mengele_clone_army.txt.
- localisation/english/germany_mengele_l_english.yml.
- docs/events/germany_mengele/overview.md.

Critical live gaps:

- germany_mengele_mark_auschwitz_laboratory_site at line 273 stores responsibility and flags on state 88 but does not call genocide_track_state_for_monthly_pulse. The current documentation says the site participates in the monthly system, but the code does not guarantee that unless another camp registration has already added state 88.
- germany_mengele_add_requested_biowarfare_facility at line 311 can place facilities in states 88, 89, 64, or 60 and marks genocide_ss_laboratory_site, but fallback states receive neither responsible-country data nor active-array registration.
- germany_mengele.23 at events/germany_mengele.txt line 679 unlocks the cloning project through broad program flags. It does not require the accepted archive, experiment network, autonomy, or facility-depth gates.
- coup transfer logic follows facility states and Auschwitz, not every accepted experiment-linked registered site.

This file set is mandatory for Germany, but common/scripted_effects/germany_mengele_effects.txt is currently dirty. Merge it only after the active owner finishes or provides a diff.

### 4.13 Japan/Ishii integration

The only explicit Ishii implementation found is the startup scientist:

- common/scripted_effects/chaosx_startup_history_effects.txt lines 614-633 creates Shiro Ishii and sets chaosx_scientist_jap_shiro_ishii.
- localisation/english/chaosx_characters_l_english.yml supplies his name/description.
- the scientist portrait is registered through the scientist portrait GFX surfaces.

No live Unit 731/Pingfang decision category, event namespace, country variables, facility progression, accident risk, or special-project gate exists. The entire accepted Ishii package is a new subsystem layered over the existing scientist, Japanese genocide decisions, biological warfare projects, contamination, Deaths, and condemnation.

Candidate new files:

- common/script_constants/japan_ishii_repression_constants.txt.
- common/scripted_effects/japan_ishii_repression_effects.txt.
- common/scripted_triggers/japan_ishii_repression_triggers.txt.
- common/decisions/japan_ishii_repression_decisions.txt.
- events/japan_ishii_repression.txt.

Alternatively, keep all shared camp lifecycle effects in the genocide files and create only the country-specific decisions/events/constants. Do not duplicate shared registration or Deaths math.

### 4.14 Soviet repression and Soviet Collapse integration

Current camp decisions/effects are in the genocide files. The bridge into Event 005 is:

- soviet_collapse_apply_genocide_gulag_repression_memory at common/scripted_effects/005_soviet_collapse_effects.txt line 61.

It:

- accumulates soviet_collapse_gulag_repression_memory;
- increases old-movement pressure and foreign appetite;
- below a collapse-threat ceiling, increases Moscow authority and military obedience, reduces republic confidence and progressive release pressure;
- clamps components and recalculates total collapse threat.

The bridge is invoked by gulag registration and current Soviet repression decisions.

Missing accepted systems:

- no integration with the vanilla SOV_paranoia variable/system;
- no durable camp-side paranoia_pressure or nkvd_authority;
- no persistent famine-pressure lifecycle or failed-management consequence chain;
- no full decision interaction between gulag reach, famine, paranoia, reform, exposure, and Union Crisis.

Event 005 files are very large and heavily interconnected. Keep the initial bridge narrow in common/scripted_effects/005_soviet_collapse_effects.txt, and put most new camp-side logic in the genocide subsystem. Do not modify the Event 005 focus trees merely to add pre-collapse Soviet camp hooks; those focus files belong to released successor countries, not the pre-collapse Soviet vanilla tree.

### 4.15 Focus-tree availability

The mod's common/national_focus directory contains only:

- germany_mengele_clone_army.txt.
- four Event 005 successor focus files.
- Event 002, 003, 007, and 010 special-event trees.

There are no custom base-country focus trees for ENG/RAJ, USA, FRA/Vichy, ITA, BEL/Congo, JAP, SOV, or ordinary GER. Part 5 focus hooks therefore cannot be inserted into mod-owned base-country trees as currently written.

Implementation choices must be explicit:

- rely on decisions/events/ideas and document that no base-tree edit exists;
- create additive focus trees/branches with careful selection/compatibility rules;
- or use a supported focus inlay/other route only after proving it from vanilla documentation and precedent.

Do not silently claim focus-hook completion by setting unused flags.

### 4.16 Events and localisation

Current camp events: events/genocide_crisis_events.txt.

It owns discovery/news/threshold/tribunal/history events in namespace chaosx_genocide. There are no events for the missing country packages.

Localisation touchpoints:

- localisation/english/chaosx_buildings_l_english.yml.
- localisation/english/chaosx_decisions_l_english.yml for existing camp categories and decisions.
- localisation/english/_chaosx_events_l_english.yml for existing chaosx_genocide events.
- localisation/english/chaosx_chaos_meter_l_english.yml.
- localisation/english/condemnation_sanctions_l_english.yml.
- localisation/english/germany_mengele_l_english.yml.
- localisation/english/005_soviet_collapse_l_english.yml.
- localisation/english/chaosx_characters_l_english.yml.
- the existing genocide decision/event localisation file(s) located by current key ownership should be extended rather than duplicating keys.

All new player-facing IDs need same-change localisation, UTF-8 BOM, current-world wording, and exact correspondence with scripted-GUI values and spreadsheet detail text.

### 4.17 Spreadsheet

Workbook: docs/spreadsheets/chaos_redux_events_catalog.xlsx

Sheets:

- Events: 1015 rows, 13 columns.
- Clusters.
- Scenarios.
- Info.
- Legend.

Events columns are ID, Event Name, Details, Evo I-V, World-End Scenario, Type, Cluster ID, Member Severity, and Status.

No row contains Mengele, genocide, gulag, repression, concentration camp, Unit 731, or Ishii. Therefore this is not a simple stale-row update. The main agent must decide whether the system becomes:

- a new catalog event/system row with an assigned ID;
- details attached to an existing event row; or
- deliberately outside the event catalog, with that decision documented.

Do not have the spreadsheet worker invent an event ID or wording before implementation facts and in-game localisation are stable.

## 5. Required file-touch map

### 5.1 Mandatory existing files

Core:

- common/script_constants/genocide_crisis_constants.txt
- common/buildings/chaosx_buildings.txt
- common/scripted_effects/genocide_crisis_effects.txt
- common/scripted_triggers/genocide_crisis_triggers.txt
- common/decisions/categories/genocide_crisis_categories.txt
- common/decisions/genocide_crisis_decisions.txt
- common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt
- common/ideas/genocide_crisis_ideas.txt
- common/ai_strategy/genocide_crisis_ai_strategy.txt
- common/on_actions/genocide_crisis_on_actions.txt
- common/on_actions/chaosx_on_actions_chaos_meter.txt
- events/genocide_crisis_events.txt

Shared integrations:

- common/scripted_effects/chaos_meter_effects.txt only if the current Deaths API cannot express a required display/result; prefer using it unchanged.
- common/script_constants/condemnation_sanctions_constants.txt and common/scripted_effects/condemnation_sanctions_effects.txt only for genuinely missing source/context support.
- common/scripted_effects/germany_mengele_effects.txt
- common/scripted_triggers/germany_mengele_triggers.txt
- events/germany_mengele.txt
- common/special_projects/projects/mengele_cloning_projects.txt
- common/scripted_effects/005_soviet_collapse_effects.txt for the narrow bridge.
- common/scripted_effects/chaosx_startup_history_effects.txt only if the Ishii scientist needs new flags/assignment behavior.

Presentation/docs:

- interface/chaosx_buildings.gfx
- localisation/english/chaosx_buildings_l_english.yml
- localisation/english/chaosx_decisions_l_english.yml
- localisation/english/_chaosx_events_l_english.yml
- localisation/english/germany_mengele_l_english.yml
- localisation/english/005_soviet_collapse_l_english.yml when bridge text changes
- docs/systems/genocide_crisis_system.md
- docs/systems/genocide_mechanics_spec.md
- docs/systems/chaos_meter_deaths_mechanic.md if Deaths semantics change
- docs/systems/condemnation_sanctions.md if new contexts/sources are added
- docs/events/germany_mengele/overview.md
- docs/events/005_soviet_collapse/overview.md
- common/scripted_effects/chaosx_dynamic_effects.md only if a new shared dynamic helper is added to chaosx_dynamic_effects.txt.

### 5.2 Likely new files

Prefer subsystem separation for readability:

- common/scripted_guis/camp_repression_ledger_scripted_gui.txt
- common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt
- interface/camp_repression_ledger.gui
- interface/camp_repression_rework.gfx
- localisation/english/camp_repression_rework_l_english.yml
- events/camp_repression_country_events.txt or bounded country-specific event files
- optional country-specific constants/effects/decisions for Ishii if the shared genocide files become unwieldy
- docs/systems/genocide_crisis_system.md as the required mechanic document
- docs/assets/system_camp_repression_rework/manifest.md and prompt/handoff files after IDs stabilize

Avoid creating separate duplicated lifecycle engines for each country. Shared registration, pressure, Deaths, exposure, cleanup, and GUI cache logic should remain centralized.

### 5.3 Assets after stable IDs

Existing camp building DDS files are available and can remain as interim registered assets only if the accepted asset spec allows them. Missing accepted assets include ledger frame/header elements, stage/pressure icons, country-kit decision icons, reform/exposure icons, Ishii/Pingfang art, and any new staged idea icons.

Final asset work should use chaos-redux-event-assets after sprite names, sizes, and code IDs are registered. No asset request should precede stable filenames.

## 6. Dirty-worktree overlap and ownership gates

Current relevant dirty file:

- common/scripted_effects/germany_mengele_effects.txt

It is a mandatory rework touchpoint. Do not overwrite, reformat, or patch it until its owner is identified and its diff reviewed. The safe sequence is:

1. finish or snapshot the current Mengele change;
2. review its diff against lines 273 onward and all cloning/coup helpers;
3. rebase the rework patch conceptually onto that version;
4. validate both the existing change and new camp registration/gating behavior.

The worktree also contains many unrelated Event 017/event-cluster/achievement changes. They must not be staged or committed with the camp rework.

## 7. Recommended implementation order

1. Resolve the chemical/biological safety contradiction in the spec tracker. Resolve the focus-hook strategy and catalog ownership question. Claim ownership of the dirty Mengele file.
2. Freeze final identifiers for shared variables, flags, decisions, ideas, dynamic modifiers, scripted GUI, events, sprites, and country kits.
3. Add constants and shared triggers first: lifecycle stages, pressure values, state pools, caps, reform gates, site-validity checks, and country-kit availability.
4. Rework registration semantics:
   - one canonical register helper;
   - one canonical unregister/cleanup helper;
   - responsibility reassignment rules;
   - duplicate-safe array membership;
   - event-driven registration for every construction path;
   - no monthly every-country rescan.
5. Implement the shared monthly site calculation and exact Deaths/condemnation outputs. Explicitly decide additive versus exclusive site-type pulses.
6. Implement shared decisions and categories, including player-visible management, reform/dismantlement, and trigger/effect tooltips.
7. Add staged ideas/dynamic modifiers and update their values from the same shared pressure model.
8. Implement Germany integration after the dirty-file gate:
   - register Auschwitz and every fallback lab;
   - assign responsibility;
   - gate cloning through accepted archive/network/facility variables;
   - transfer all intended linked sites during coup outcomes;
   - enforce Poland/non-core target priority.
9. Implement Japan/Ishii on top of the shared engine and existing bio-contamination APIs.
10. Implement the Soviet camp-side variables, vanilla paranoia bridge, famine failure chain, and the narrow Event 005 bridge.
11. Implement UK/Raj, USA, France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and generic gated decision kits with explicit state pools and AI caps.
12. Add the Repression Ledger scripted GUI after gameplay variables are stable. Cache display values from the same calculation effects used by gameplay.
13. Add events, localisation, and only then assets with final IDs.
14. Update system/event docs and make the catalog decision. The spreadsheet worker should run after in-game wording and facts are final.
15. Run specialist audits: decision/mission, country-package, localisation, event completion, and focus-tree audit if a real focus tree is added.

Commit boundaries should follow these meaningful tranches rather than one giant commit:

- shared engine and cleanup;
- shared decisions/UI data model;
- Germany;
- Japan;
- Soviet;
- remaining country kits;
- GUI/assets/localisation/docs/catalog;
- audit fixes.

## 8. Vanilla precedents to mirror

State-targeted decisions:

- common/decisions/JAP.txt contains multiple state_target = any_controlled_state decisions, including around lines 1608 and 1686.
- common/decisions/SOV.txt contains state-targeted Soviet decisions around line 11001.
- common/decisions/RAJ.txt and RAJ_GOE.txt provide current owned/controlled-state decision patterns.
- common/decisions/ITA.txt around line 3757 provides another occupied-state example.

On actions:

- common/on_actions/_documentation.md documents on_monthly_TAG and on_state_control_changed.
- common/on_actions/07_nsb_on_actions.txt contains Soviet state-control and on_monthly_SOV precedents.
- common/on_actions/14_sea_on_actions.txt contains on_monthly_JAP and state-control precedents.
- common/on_actions/12_wuw_on_actions.txt contains on_monthly_ENG and Congo-era hooks.

Decision-category scripted GUI:

- common/decisions/categories/SOV_decision_categories.txt uses sov_paranoia_system_ui.
- common/decisions/categories/RAJ_GOE_decision_categories.txt uses RAJ_famine_scripted_ui.
- common/decisions/categories/GER_decision_categories.txt uses ger_rk_ui.
- common/decisions/categories/USA_decision_categories.txt uses usa_congress_decision_ui.

Soviet paranoia:

- common/scripted_effects/SOV_scripted_effects.txt owns SOV_paranoia increase/decrease/clamp/update helpers, beginning around line 149.
- common/decisions/SOV.txt owns paranoia decisions and visibility.
- common/decisions/categories/SOV_decision_categories.txt line 13 wires the paranoia GUI.

State/country dynamic modifiers:

- common/scripted_effects/SOV_scripted_effects.txt contains canonical add_dynamic_modifier and variable-backed modifier update patterns.
- events/GOE_Raj.txt contains current famine country/state dynamic modifier application, useful for the accepted persistent famine-pressure chain.

Occupation/repression structure:

- common/occupation_laws/00_occupation_laws.txt is the main vanilla resistance/compliance precedent. Mirror its use of resistance/compliance concepts, not its content framing.

The mod's own current genocide registration/discovery and condemnation APIs take precedence over vanilla when they already provide the required shape.

## 9. Meaningful validation scenarios

Shared lifecycle:

- build/register one site through each supported path; verify one array entry, one responsible country, correct stage, and exact displayed values;
- repeat registration and prove no duplicate entry/count;
- dismantle, reform, lose control, annex, capitulate, and remove the final active marker; verify unregister/cleanup and no future monthly pulse;
- switch control twice and verify discovery fires once with the correct discovering/responsible scopes;
- give a state overlapping site flags and verify the intended combined or exclusive Deaths calculation exactly.

Performance:

- inspect the completed monthly call graph and prove it contains no every_country/every_state scan for camp discovery;
- prove the only monthly site iteration is over the registered state collection, with stale entries removed.

Germany:

- full/restricted/rejected Mengele routes;
- Auschwitz and all four facility fallback states;
- cloning unavailable before every accepted gate and available once all are met;
- coup transfer includes all intended registered experiment sites and excludes unrelated facilities;
- target selection prefers occupied Poland/non-core states before German cores.

Japan:

- Ishii scientist present/absent handling;
- Pingfang progression and Kwantung autonomy;
- experiment accident/containment/exposure branches;
- no direct killing-efficiency optimization control;
- bio contamination and condemnation use existing APIs once per intended outcome.

Soviet:

- paranoia inactive versus active;
- low/high paranoia;
- gulag expansion, famine pressure, failed management, reform, and records destruction;
- Union Crisis inactive/active/terminal;
- repression can temporarily raise central control while increasing long-run grievances and collapse risk as designed.

Country packages:

- test original tags and successor/puppet edge cases for ENG/RAJ, USA, FRA/Vichy, ITA, BEL/Congo;
- test loss of colonial/occupied target pools;
- test democratic/reform routes and AI caps;
- prove generic countries cannot access the system without the accepted gate.

UI:

- decision-category header appears only when relevant;
- every ledger number matches the gameplay variable used that month;
- no missing GUI sprite/localisation keys;
- hidden evidence is not leaked before discovery;
- tooltips state exact current effects and costs.

Documentation/catalog:

- docs match implemented identifiers and behavior;
- asset manifest names match GFX and DDS paths;
- catalog wording, if a row is adopted, matches final in-game localisation exactly.

## 10. Completion implications

This rework cannot be called complete if any of the following remain:

- monthly whole-world camp rescan;
- missing unregister/cleanup;
- unresolved additive death stacking;
- concentration camps globally buildable without accepted gates;
- missing human-player lifecycle decisions;
- missing country kit or AI behavior;
- missing Ishii/Pingfang system;
- missing Soviet paranoia/famine/Union Crisis integration;
- cloning still gated only by broad Mengele flags;
- absent or inaccurate ledger;
- missing localisation/assets/docs/catalog decision;
- focus hooks claimed without an implemented, documented strategy;
- the chemical/biological contradiction left unresolved.

No simplification or fallback is recommended by this report. The unresolved choices above require explicit source-of-truth decisions rather than silent substitutes.

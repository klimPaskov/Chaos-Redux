# System Camp Repression Rework Spec, Part 7: Implementation Checklist, Touched Files, and Validation Commands

Working feature id: `system_camp_repression_rework`

This checklist is for the implementation agent. It should be used after Parts 1 through 6 are accepted as the source design. It names the likely files, helper families, integration order, validation commands, and scenario checks. It does not claim that the live repository has these exact paths available in the sandbox. The implementer must verify paths in the real Chaos Redux repository before editing.

## Live implementation reconciliation, 2026-07-11

The package has moved beyond the preimplementation checklist below. The current runtime is split across `common/decisions/camp_repression_major_country_decisions.txt`, `common/decisions/camp_repression_colonial_country_decisions.txt`, `common/decisions/camp_repression_generic_decisions.txt`, the matching country effects and ideas, `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`, and the shared camp-rework trigger/effect layer.

The final live inventory is **29 major-country actions + 43 colonial-country actions + 12 generic actions = 84 player actions**. The closing actions are `fr_support_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, and `generic_inspect_active_site`. The same decision files contain **41 missions**, and the four Ledger show, hide, open, and close controls are tracked separately. A final decision-and-mission re-audit passed after the bounded cooldown-parity correction; its evidence is in `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/decision_mission_final_audit_2026-07-11.md`.

The subject-selected action bus is implemented through `camp_rework_action_state_id`, `camp_rework_prepare_selected_action_state`, `camp_rework_dispatch_prepare_colonial_selection`, `camp_rework_dispatch_restore_colonial_selection`, and `camp_rework_route_country_specific_action`. Restricted methods use the fixed-country and explicit-doctrine route gates in `common/scripted_triggers/camp_repression_rework_triggers.txt`; country identity or ideology alone is not sufficient.

The connected monthly runtime processes registered active-country and active-state arrays. Population damage reduces real state population and enters the Chaos Meter Deaths pipeline. Active sites retain their stored responsible country, and evidence-based discovery and condemnation follow that stored authority. Germany, Japan, the Soviet Union, the U.K./Raj, the U.S.A., France/Vichy, Italy, Belgium/Congo, and generic country kits are live.

Restricted methods are implemented as abstract capability and stockpile tiers: chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman for chemical capacity; anthrax, tularemia, plague, and smallpox for biological capacity. They resolve through abstract harm, contamination or outbreak, evidence, discovery, instability, and tribunal consequences without operational instructions or protected-class selectors.

The Repression Ledger is implemented with five exact tabs: Overview, State Pools, Active Sites, Country System, and Discovery & Reform. The header displays `[ROOT.GetName]: [GetCampCountryPanelName]` plus phase and discovery state, and all 32 Ledger country action slots use their native decision cooldown gates. Its maintained presentation uses 24 derived DDS sprites from frozen ImageGen sources in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`; all 24 have live consumers, including scripted visibility for the evidence and reform seals. The recorded prompts are in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`, and `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py` is the deterministic processor. This is the accepted static presentation, not a fallback or simple-shape substitute. Optional authored frame animation remains queued.

The five super events are wired at slots `12`, `74`, `75`, `76`, and `77`, with audio ids `45`, `44`, `46`, `47`, and `48` respectively. Static Ledger UI assets, decision/idea/project/achievement icons, report/news art, super-event art, localisation, and the five audio packages are present and wired. Achievements `60` through `69` are live. Germany's focus reward lifecycle is consolidated to at most three stable lane spirits before convergence and exactly one final capstone spirit. The core final variant preserves exact science-and-force totals; stage-specific variants preserve the exact highest completed optional territorial stage through reclamation, continental dominance, the command spine, or full world dominance, with no new command prerequisite.

The event workbook remains aligned through the existing Soviet Collapse Event Log record; this system rework does not create a standalone ChaosX event identity. The historical rows and checkboxes below remain accepted design and validation-contract evidence; current implementation status lives in `source_of_truth_and_completion_tracker.md`, the completion report, and the linked scenario report.

The final decision-and-mission audit is closed. All 13 Part 7 scenarios plus the two cross-cutting abstract-method and full-Ledger contracts were statically traced with zero failures. No engine-runtime scenario execution occurred in this environment, so the static trace does not prove rendered GUI behavior, AI selection, timed outcomes, or numeric deltas in a running game. `docs/plans/system_camp_repression_rework_plans/scenario_contract_validation_report.md` records the evidence and this explicit validation gap. The remainder of this document stays as the accepted implementation and validation contract rather than being rewritten as implementation history.

The remainder of this document is retained as the accepted implementation-order and validation contract. Its `Likely` file tables and recommended helper names are a preimplementation snapshot where they differ from the live file map above.

## Implementation order

Use this order so the rework remains integrated with the existing `genocide_crisis`, Deaths, Condemnation, and country-specific systems.

1. Promote or copy the accepted planning package into `docs/specs/system_camp_repression_rework_specs/`.
2. Read the required repo guidance before editing: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees` for focus hooks, `chaos-redux-event-assets` for any new assets, and `chaos-redux-super-events` for any super-event implementation.
3. Inspect existing `genocide_crisis` files and confirm current helper names before adding new helper families.
4. Add or update script constants for shared values, country caps, mission durations, display bands, AI weights, and state-pool scoring.
5. Add scripted triggers for shared and country-specific state pools.
6. Add scripted effects for state registration, display rebuild, monthly processing, discovery, dismantlement, reform, and AI target selection.
7. Update decisions and categories using the Part 5 decision kits.
8. Update ideas and dynamic modifiers for staged country and generic idea lifecycles.
9. Update on-actions only through existing host-only monthly and state-control hooks.
10. Update country-specific integration files for Germany, Japan, Soviet Union, U.K., U.S.A., France or Vichy, Italy, Belgium, and generic users.
11. Add AI strategy and AI decision weights with caps and route validity checks.
12. Add decision-category header scripted localisation and optional scripted GUI wiring.
13. Add assets only after sprite names, GUI dimensions, and target files are confirmed.
14. Update docs, package manifests, and event catalog spreadsheet only after implementation facts exist.
15. Run validation and scenario checks before any completion claim.

## Likely touched gameplay files

### Core system files

| File | Required work |
| --- | --- |
| `common/script_constants/genocide_crisis_constants.txt` | Add shared pressure values, display bands, death factors, labor output factors, mission durations, AI caps, and country-kit constants. |
| `common/buildings/chaosx_buildings.txt` | Confirm existing `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` remain unique and unchanged unless a migration is required. |
| `common/decisions/categories/genocide_crisis_categories.txt` | Add or update low-priority category visibility, show or hide toggles, and optional open-ledger decision category icon. |
| `common/decisions/genocide_crisis_decisions.txt` | Implement shared generic decisions and call country-specific helper effects. |
| `common/scripted_effects/genocide_crisis_effects.txt` | Add helper effects for registration, refresh, display values, monthly processing, dismantlement, reform, discovery, state selection, and country-kit routing. |
| `common/scripted_triggers/genocide_crisis_triggers.txt` | Add shared and country-specific state-pool triggers, route gates, AI validity triggers, and cleanup triggers. |
| `common/on_actions/genocide_crisis_on_actions.txt` | Keep state-control discovery hooks and cleanup hooks aligned. Do not add a new daily or monthly world loop. |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | Confirm monthly Deaths integration still calls the camp pulse through the existing host-only path. |
| `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt` | Add or update local state modifiers for active networks, overextension, reform, discovery, and burden stages. |
| `common/ideas/genocide_crisis_ideas.txt` | Add staged ideas for generic, U.K., U.S., France or Vichy, Italy, Belgium, and shared reform states. |
| `common/opinion_modifiers/genocide_crisis_opinion_modifiers.txt` | Confirm discovery and tribunal reactions use responsible-country attribution. |
| `common/ai_strategy/genocide_crisis_ai_strategy.txt` | Add country-specific historical caps, reform behavior, and post-discovery avoidance. |

### Germany, Japan, and Soviet integration files

| File | Required work |
| --- | --- |
| `events/germany_mengele.txt` | Ensure Auschwitz, authorization, cloning, coup, and emergency revolt paths read the updated camp values where required. |
| `common/script_constants/germany_mengele_constants.txt` | Add thresholds for camp-linked autonomy, prisoner-transfer pressure, and cloning unlock if not already present. |
| `common/scripted_effects/germany_mengele_effects.txt` | Add or update effects that link experiment sites, Auschwitz state `88`, and camp network reach to `mengele_autonomy` and `mengele_permission_level`. |
| `common/scripted_triggers/germany_mengele_triggers.txt` | Add gates for camp-linked cloning unlock and emergency revolt state capture. |
| `common/decisions/germany_mengele_decisions.txt` | Update Auschwitz and Final Solution decision layer to call shared state-pool and Deaths helpers. |
| `common/special_projects/projects/mengele_cloning_projects.txt` | Confirm `sp_mengele_cloning` availability reads the new unlock package without completing projects directly. |
| `common/decisions/genocide_crisis_decisions.txt` | Add Japan and Soviet country-specific decision families if they remain in the shared file. Split only if repo pattern supports it. |
| `common/scripted_effects/genocide_crisis_effects.txt` | Add Japan Ishii and Soviet gulag bridge effects if no country-specific file exists. |
| `common/scripted_triggers/genocide_crisis_triggers.txt` | Add Japan China and Manchuria pool triggers, Soviet periphery and famine triggers, and Union Crisis bridge gates. |

### U.K., U.S., France, Italy, Belgium, and generic integration files

Country-specific packages can live inside the shared `genocide_crisis` files or in country-specific decision files if the repository already uses that split. Keep the implementation consistent with current Chaos Redux style.

| Surface | File candidates | Required work |
| --- | --- | --- |
| U.K. and Raj decisions | `common/decisions/genocide_crisis_decisions.txt` or country-specific U.K. decisions file | Add Raj survey, activation, labor works, manpower levy, dominion coordination, reform, and dismantlement. |
| U.K. ideas | `common/ideas/genocide_crisis_ideas.txt` or U.K. idea file | Add U.K. and Raj burden lifecycle ideas. |
| U.K. focus hooks | U.K. focus tree files if present | Add route flags or direct unlocks from Part 5, otherwise leave hook flags for future focus integration. |
| U.S. decisions | shared or U.S. decisions file | Add wartime relocation authority, court review, termination, and redress route. |
| U.S. ideas | shared or U.S. idea file | Add wartime security, civil liberties, redress, and reform credit ideas. |
| U.S. focus hooks | U.S. focus tree files if present | Add route flags for security review, court review, and redress. |
| France and Vichy decisions | shared, France, or Vichy decision file | Add legacy inspection, Vichy expansion, North Africa labor, refugee pressure, and liberation reform. |
| France and Vichy ideas | shared or France idea file | Add camp legacy, Vichy collaboration reach, North Africa burden, and reform credit. |
| Italy decisions | shared or Italy decision file | Add Libya and East Africa colonial route, roads and forts, security battalions, closure, and compensation. |
| Belgium decisions | shared or Belgium decision file | Add Congo quotas, resource routing, transport corridors, strikes, inspection, reform, and local administration. |
| Generic decisions | shared `genocide_crisis` decisions file | Add generic activation, quota, labor routing, guard, radicalized escalation, evidence destruction, and dismantlement. |

### UI, GFX, assets, and localisation files

| File | Required work |
| --- | --- |
| `common/scripted_guis/genocide_crisis_scripted_guis.txt` or existing GUI file | Add optional `repression_ledger_window` bindings only if custom GUI is implemented. |
| `interface/genocide_crisis.gui` or existing Chaos Redux GUI file | Add custom window layout only after exact dimensions are confirmed. |
| `interface/chaosx_buildings.gfx` | Confirm building sprites still resolve after any path changes. |
| `interface/chaosx.gfx` or new system GFX file | Register decision, idea, GUI, and optional animated sprites. |
| `localisation/english/chaosx_decisions_l_english.yml` | Add final decision text after implementation. Direction only from specs. |
| `localisation/english/chaosx_ideas_l_english.yml` | Add idea and modifier text after effects are final. |
| `localisation/english/chaosx_modifiers_l_english.yml` | Add dynamic modifier text. |
| `localisation/english/_chaosx_events_l_english.yml` | Add threshold, discovery, reform, and country-specific event text only if events are implemented. |
| `localisation/english/chaosx_gui_l_english.yml` | Add category header, GUI labels, buttons, and tooltips. |
| `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` | Confirm Deaths and Condemnation summaries still display camp reasons correctly. |
| `common/scripted_localisation/chaosx_scripted_localisation_genocide_crisis.txt` if created | Add compact display localisation from Part 6. |
| `docs/systems/genocide_crisis_system.md` | Update current system documentation after implementation. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Update only after implemented event details and player-facing localisation are final. |

## New or updated helper map

Names are recommendations. The implementation agent should adjust to existing naming style if the repo already has closer helpers.

### Scripted triggers

| Trigger id | Scope | Purpose |
| --- | --- | --- |
| `is_valid_camp_active_site_state` | state | True when state has an active registered site that should process monthly. |
| `is_valid_camp_dormant_marker_state` | state | True for historical markers that do not process monthly. |
| `is_valid_camp_discovery_state` | state | True when evidence can be discovered. |
| `is_valid_camp_dismantlement_state` | state | True when a state can be closed or reformed. |
| `is_valid_camp_enemy_proximity_state` | state | True when retreat evidence decisions can appear. |
| `has_active_camp_network` | country | True when country has at least one active registered site. |
| `has_visible_camp_reform_work` | country | True when reform, redress, tribunal, or dismantlement remains. |
| `has_camp_category_visible_action` | country | Controls category visibility. |
| `is_generic_occupied_camp_pool_state` | state | Shared occupied pool. |
| `is_generic_colonial_camp_pool_state` | state | Shared colonial pool. |
| `is_generic_core_fallback_pool_state` | state | Core fallback with severe penalties. |
| `is_uk_raj_detention_pool_state` | state | U.K. Raj package pool. |
| `is_usa_wartime_security_zone_state` | state | U.S. emergency security pool. |
| `is_france_north_africa_labor_pool_state` | state | France or Vichy North Africa pool. |
| `is_italy_libya_repression_pool_state` | state | Italy Libya pool. |
| `is_bel_congo_concession_pool_state` | state | Belgium Congo pool. |

### Scripted effects

| Effect id | Scope | Purpose |
| --- | --- | --- |
| `camp_rework_register_active_site` | state with country root | Store responsible country, site type, evidence depth, and add to active array. |
| `camp_rework_unregister_inactive_site` | state | Remove active registration when site is gone, dismantled, or invalid. |
| `camp_rework_clean_invalid_active_sites` | country or global host | Bounded cleanup of stale active site entries. |
| `camp_rework_apply_monthly_state_effects` | state | Apply Deaths, state population loss, output, resistance, evidence, and local burden. |
| `camp_rework_apply_country_monthly_pressure` | country | Apply national stability, guard, rail, reform, and overextension pressure. |
| `camp_rework_rebuild_display_values` | country | Build Part 6 display variables. |
| `camp_rework_rebuild_gui_arrays` | country | Build bounded state and country-specific GUI arrays. |
| `camp_rework_select_state_for_display` | country with state target | Store selected state id and rebuild selected-state card. |
| `camp_rework_clear_selected_state` | country | Clear selected state after invalidation. |
| `camp_rework_apply_discovery` | state | Discover evidence and apply condemnation to stored responsible country. |
| `camp_rework_attempt_evidence_destruction` | state | Resolve evidence destruction success or failure. |
| `camp_rework_start_dismantlement` | country or state | Start dismantlement mission and freeze expansion where needed. |
| `camp_rework_complete_dismantlement` | country or state | Remove active sites, unregister states, and apply reform legacy. |
| `camp_rework_apply_core_fallback_penalties` | country and state | Apply lower output and higher domestic damage for core fallback. |
| `camp_rework_apply_ai_cap` | country | Clamp AI active site count and escalation choices. |
| `camp_rework_route_country_specific_action` | country | Dispatch U.K., U.S., France, Italy, Belgium, generic, Germany, Japan, or Soviet action helpers. |

## Constants and tuning groups

Use script constants for every threshold, cap, mission duration, AI weight, and effect factor that may be tuned.

Recommended constant groups:

```text
camp_rework_common = {
    low_band
    medium_band
    high_band
    severe_band
    critical_band
    base_monthly_loss_factor
    concentration_loss_factor
    radicalized_loss_factor
    gulag_loss_factor
    experiment_loss_factor
    contaminated_evidence_loss_factor
    occupied_pool_output_factor
    colonial_pool_output_factor
    core_fallback_output_factor
    core_fallback_stability_factor
    core_fallback_reform_factor
}

camp_rework_costs = {
    base_support_equipment_cost
    base_infantry_equipment_cost
    base_truck_cost
    base_train_cost
    base_convoy_cost
    base_guard_manpower_cost
    base_civilian_factory_burden
    base_stability_cost
    max_command_power_cost
}

camp_rework_ai = {
    generic_activation_weight
    generic_radicalized_weight
    generic_reform_weight
    uk_wartime_weight
    usa_pacific_pressure_weight
    vichy_expansion_weight
    italy_colonial_weight
    belgium_congo_resource_weight
    post_discovery_reform_weight
}

camp_rework_mission_days = {
    emergency_activation
    labor_project
    suppression_response
    reform_standard
    reform_major
    retreat_evidence
}
```

If a duration field rejects `constant:` tokens, use a file-scoped `@` constant in the decision or event file and mirror it with the script constant value. Document the mirror near the file-scoped constant.

## Deaths and population integration checklist

Every active monthly population-loss source must use the Chaos Meter Deaths pipeline.

Required checks:

- concentration, radicalized, gulag, experiment, and contaminated evidence routes call the existing Deaths helper or a new helper that wraps it.
- Deaths reason maps to the existing Deaths tab summary categories.
- state population is reduced with state-linked civilian deaths.
- when the site is in occupied territory, state owner receives population-loss record while responsible country receives evidence and condemnation responsibility.
- no country kit subtracts population only through recruitable-population modifiers.
- no new parallel death counter is created outside Chaos Meter Deaths.

## Discovery and responsibility checklist

- Every active site stores `genocide_responsible_country` at creation or activation.
- Discovery uses the stored responsible country, not the discoverer.
- If state ownership or control changes, stored responsibility remains until reform, tribunal, or cleanup explicitly changes it.
- Destroyed evidence and failed cover-up states still remain discoverable where the design requires it.
- Discovery applies condemnation only after evidence is discovered or a country-specific legal exposure route fires.
- First severe discovery can fire a bounded event or news event.
- Repeated discoveries update variables, Deaths, and condemnation without popup spam.

## Country package checklist

### U.K. and Raj

- Raj and Indian Ocean state pools exist.
- U.K. and Raj ideas are staged and removable.
- U.K. decisions include survey, activation, labor works, manpower levy, dominion coordination, release, reform, and dismantlement.
- India or Raj receives burden and autonomy pressure when the system expands.
- AI uses light wartime activation and postwar reform.
- Discovery route links decolonization and Raj autonomy pressure.

### U.S.A.

- War, homeland threat, Pacific pressure, sabotage fear, or high chaos gates activation.
- State pools are geographic military-security pools, not protected-class selectors.
- Court review, termination, and redress are full routes.
- AI rarely activates and terminates after threat falls.
- Domestic legal exposure exists without recurring leak events.

### France and Vichy

- Democratic or Free France has inspection and reform.
- Vichy or authoritarian France has collaboration and North Africa labor routes.
- Responsibility remains clear when German-linked collaboration decisions exist.
- Refugee pressure and post-liberation reckoning are staged ideas or missions.
- AI route differs by democratic France, Free France, and Vichy.

### Italy and Libya

- Libya and East Africa pools exist.
- Roads, forts, ports, supply, security battalions, closure, and compensation routes exist.
- Italian cores are not used by colonial decisions.
- AI expands only under fascist colonial conditions and reforms after regime change.

### Belgium and Congo

- Congo concession and transport pools exist.
- Quota, resource, transport, strike, inspection, reform, and local administration decisions exist.
- Congo receives local burden and autonomy pressure.
- Belgium can use Congo route while in exile if control and subject logic allow it.
- AI caps active quota and transport cycles.

### Generic users

- Generic activation is gated by ideology, war, occupation, resistance, chaos doctrine, or severe crisis.
- Generic radicalized escalation requires an existing site and strong route gate.
- Core fallback is visibly bad and uses special penalties.
- Generic AI is conservative and capped.
- Reform and dismantlement are always available after regime change or discovery.

## Localisation checklist

Final localisation belongs to implementation, not this planning package. When writing it, follow these rules:

- no final prose from planning files should be pasted directly.
- no hidden formulas, debug values, protected-class selectors, or future surprise routes in player text.
- decision and GUI text should explain visible costs and consequences.
- discovery and tribunal text should be evidence-based.
- super-event quotes, cultural remarks, and audio must be separately researched.
- localisation files must keep repository encoding rules.
- dynamic values should use scripted localisation rather than raw trigger blocks.

## Asset checklist

Do not request final artwork before confirming exact target files and sprites.

Required asset families:

- shared decision category icon.
- shared decision icons for expansion, guard allocation, labor project, evidence destruction, inspection, dismantlement, and reform.
- country-specific decision icons listed in Part 5.
- idea icons for each lifecycle idea family.
- report images for discovery routes.
- news images for first severe discovery or colonial reckoning.
- optional scripted GUI panel and value icons from Part 6.
- optional animated warning, evidence, reform, selected-state, and critical frames.
- super-event images only for accepted super-event candidates.

Asset workers must follow source-mode rules. Real historical material should be sourced and documented. Fictional UI, icons, and alternate-history scene art can be generated through the proper asset workflow.

## Validation commands

These commands are implementation-time checks. Adjust paths only if the live repo uses different file names.

### File presence and primary ids

```bash
rg -n "concentration_camp|extermination_camp|gulag_labor_camp_network" common/buildings common/decisions common/scripted_effects common/scripted_triggers
rg -n "genocide_responsible_country" common events
rg -n "global\.genocide_active_camp_states|genocide_active_camp_states" common events
rg -n "chaos_meter_register_deaths|chaos_meter_register_state_civilian_deaths_percent|bio_register_state_civilian_deaths|chem_register_state_civilian_deaths" common events
```

### Recurring minor-popup removal

```bash
rg -n "leak|leaked|minor report|random report|monthly report|refugee popup|sabotage popup" events common/decisions common/scripted_effects
```

Review results manually. Discovery, threshold, and reform events can remain. Ordinary monthly processing should not call recurring leak or minor report popups.

### Country package hooks

```bash
rg -n "is_uk_raj_detention_pool_state|uk_.*raj|raj_labor_burden" common events localisation docs
rg -n "is_usa_wartime_security_zone_state|usa_.*relocation|civil_liberties_damage|redress" common events localisation docs
rg -n "is_france_north_africa_labor_pool_state|vichy_.*camp|north_africa_labor" common events localisation docs
rg -n "is_italy_libya_repression_pool_state|ita_.*desert|libyan_resistance" common events localisation docs
rg -n "is_bel_congo_concession_pool_state|bel_.*congo|congo_concession" common events localisation docs
rg -n "is_generic_occupied_camp_pool_state|generic_.*detention|generic_.*dismantle" common events localisation docs
```

### Germany, Japan, and Soviet integration

```bash
rg -n "mengele_autonomy|mengele_permission_level|sp_mengele_cloning|germany_mengele_start_coup" common events
rg -n "state = 88|province = 9412|Auschwitz|auschwitz" common events docs localisation
rg -n "ishii|pingfang|kwantung|occupation_test|bio_project_pressure" common events docs localisation
rg -n "gulag_network_reach|paranoia_pressure|famine_pressure|union_crisis" common events docs localisation
```

### On-action and performance guard

```bash
rg -n "on_daily|on_weekly|on_monthly" common/on_actions common/scripted_effects events
rg -n "every_country|all_country|every_state|random_state" common/scripted_effects common/on_actions common/decisions events
```

Review any new whole-world loops. The rework should use the existing registered active-site array and host-only monthly pulse. Do not add new broad daily or weekly loops.

### GUI and scripted localisation

```bash
rg -n "repression_ledger|camp_rework_rebuild_display_values|GetCampNetworkPhaseName|GetCampEvidenceBandName" common interface localisation
rg -n "camp_gui_pool_state_ids|camp_gui_active_site_state_ids|camp_selected_state_id" common interface localisation
```

### Asset references

```bash
rg -n "GFX_decision_category_repression_ledger|GFX_repression_ledger|GFX_decision_uk_raj_detention|GFX_decision_usa_emergency_relocation|GFX_decision_bel_congo_concession_quota" interface common localisation docs
find gfx -iname '*repression*' -o -iname '*raj*detention*' -o -iname '*congo*labor*'
```

### Duplicate or stale active-site registration

Use a targeted script after implementation to scan for repeated push calls and missing unregister calls around the same helper names.

```bash
rg -n "camp_rework_register_active_site|camp_rework_unregister_inactive_site|add_to_array.*genocide_active_camp_states|remove_from_array.*genocide_active_camp_states" common events
```

Manual review required:

- every registration path should store responsibility.
- every dismantlement, closure, cleanup, and invalid-site path should unregister.
- active monthly processing should skip dormant markers.
- destroyed evidence should not process as an active labor site unless a specific monthly evidence state is intended.

## Scenario validation matrix

Run or document these scenario checks in a new save after implementation.

Implementation reconciliation: all 13 rows below and the two cross-cutting `SCN-ABSTRACT-CHEM-BIO` and `SCN-FULL-LEDGER` contracts passed static trace with `ScenarioContracts=15 Failed=0`. This was not a new-save or engine-runtime run. The exact evidence and remaining runtime gap are recorded in `docs/plans/system_camp_repression_rework_plans/scenario_contract_validation_report.md`.

| Scenario | Setup | Expected result |
| --- | --- | --- |
| Germany Auschwitz integration | Fascist Germany controls state `88` after 1940 and authorizes experiments | Auschwitz becomes shared node, Deaths route works, `mengele_autonomy` and `mengele_permission_level` affect relevant pressure, cloning unlock is gated. |
| Germany core fallback | Germany has no occupied or non-core pool but still has active route | Core fallback gives lower output, higher stability damage, and stronger internal backlash. |
| Japan occupied China | Japan at war with China controls Chinese or Manchurian states | Ishii route uses occupied pools, China state owner receives population loss, Japan remains responsible. |
| Soviet high paranoia | Soviet Union has high paranoia and gulag route active | Gulag expansion, famine pressure, and Union Crisis bridge interact, relief cap stops at high crisis. |
| U.K. Raj | U.K. at war with Raj or India pool active | Raj decisions appear, U.K. gains limited control or construction, Raj or India receives burden and autonomy pressure. |
| U.S. Pacific war | U.S. at war with valid threat conditions | Relocation authority can appear, court review and redress routes work, AI rarely expands. |
| Vichy North Africa | Vichy controls North Africa and is aligned with authoritarian route | Vichy expansion and North Africa labor decisions appear, Free France or democratic route can reform later. |
| Italy Libya | Fascist Italy controls Libya with resistance or war pressure | Colonial roads, forts, security, closure, and compensation routes work. |
| Belgium Congo | Belgium controls Congo during war or exile economy pressure | Congo quotas and transport projects give resources or infrastructure while burden and accountability rise. |
| Generic authoritarian occupation | Authoritarian country controls occupied high-resistance non-core states | Generic activation and labor route work with capped AI and no protected-class selector. |
| Discovery by enemy control | Enemy captures active site with stored responsibility | Discoverer event or bounded discovery logic fires, condemnation targets responsible country, Deaths history remains state-linked. |
| Dismantlement cleanup | Regime changes and player dismantles active network | Sites unregister, ideas convert, decisions hide, category hides when no work remains. |
| No monthly flavor spam | Let monthly pulse run with several active sites | Deaths, variables, and modifiers update without recurring leak or minor report popups. |

## Completion proof requirements

Do not mark implementation complete until the report includes:

- files changed by surface.
- route coverage table for the country kits.
- helper map with final names if changed from this spec.
- confirmation that all active deaths use Chaos Meter Deaths.
- confirmation that state population is reduced through state-linked civilian deaths.
- confirmation that responsibility is stored and discovery blames the stored responsible country.
- confirmation that recurring minor camp flavor events were removed or remain disconnected from monthly processing.
- AI coverage by country and generic route.
- UI coverage, including category header and optional GUI status.
- asset status for every new visible icon, picture, or GUI sprite.
- documentation and spreadsheet status.
- validation commands run, with only task-specific results reported.
- any simplification, missing asset, deferred GUI surface, or blocked focus hook stated directly.

## Implementation staging recommendation

The safest staging is:

1. Shared helpers, constants, and Deaths integration.
2. Generic route and category visibility cleanup.
3. Germany, Japan, and Soviet integration refresh.
4. U.K., U.S., France or Vichy, Italy, and Belgium country kits.
5. AI caps and validity checks.
6. Decision category header and scripted localisation.
7. Optional scripted GUI.
8. Assets and super-events only after gameplay surfaces are stable.
9. Docs, manifest, and spreadsheet updates.
10. Completion audit.

A partially staged implementation must not claim the full rework is complete. If the custom GUI is deferred, the category header must still show the required values from Part 6. If focus hooks are deferred because no relevant custom focus tree exists, route flags and decision gates should be implemented and the report should say which focus hooks remain future integration points.

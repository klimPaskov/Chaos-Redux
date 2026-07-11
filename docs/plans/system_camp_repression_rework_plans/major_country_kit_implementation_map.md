# Germany, Japan, and Soviet Major-Country Kit Implementation Map

Date: 2026-07-11
Status: **implemented-map reconciliation**. The final decision-and-mission audit passed; the package inventory is 84 actions, 41 missions, and four Ledger controls.

## Current live disposition

The implementation uses consolidated shared triggers in `common/scripted_triggers/camp_repression_rework_triggers.txt`. The proposed `camp_repression_major_country_triggers.txt` file was not created. Major decisions, missions, effects, ideas, dynamic modifiers, Japan projects, and event support live in the files named below.

| Surface | Live file |
| --- | --- |
| Major player actions and missions | `common/decisions/camp_repression_major_country_decisions.txt` |
| Major effects and country bridges | `common/scripted_effects/camp_repression_major_country_effects.txt` |
| Major ideas | `common/ideas/camp_repression_major_country_ideas.txt` |
| Soviet famine state modifier | `common/dynamic_modifiers/camp_repression_major_country_dynamic_modifiers.txt` |
| Japan projects | `common/special_projects/projects/japan_ishii_projects.txt` |
| Events | `events/japan_ishii.txt` and `events/soviet_gulag.txt` |
| Shared GFX and localisation | `interface/camp_repression_rework.gfx`, `interface/special_projects/biowarfare.gfx`, `localisation/english/camp_repression_rework_l_english.yml`, and `localisation/english/camp_repression_country_kits_l_english.yml` |

The live major-country file contains **29 player actions** and 17 missions. The action split is Germany 7, Japan 13, and Soviet Union 9. The exact action IDs are recorded in `source_of_truth_and_completion_tracker.md` and the completion-report scaffold. Mission blocks are not included in the action count.

Every action routes through `camp_rework_route_country_specific_action`. State actions use `camp_rework_action_state_id`, which survives subject-selected and delayed decision routing without relying on `FROM`. Germany, Japan, and Soviet restricted-method access uses the strict fixed-country gates in `camp_rework_country_can_use_restricted_method_route` rather than the generic ideology shortcut.

The detailed sections below preserve the implementation design and validation rationale. Any `Add`, proposed-file, or future-tense wording is historical handoff language. The live file table and identifiers in this section control when the older wording differs.

## 1. Contract and source precedence

This map turns the accepted Part 2/Part 3 country designs and the completion tracker into exact implementation identifiers. It is deliberately additive: existing identifiers remain stable unless this report explicitly marks a one-time alias migration.

Required implementation constraints:

- Use the existing registered monthly country pulse and the empty `camp_rework_update_country_specific_monthly_bridges` dispatcher. Do not add `on_daily`, `on_weekly`, `on_monthly`, or another all-country loop.
- A country action may register a site, mutate a country value, or start a mission immediately. Recurring harm must pass through the shared camp monthly site processor and the Deaths adapter exactly once.
- Keep the existing country categories: Germany uses `genocide_crisis_category` for camp management and `germany_final_solution_category` / `germany_mengele_response_category` for the existing Mengele spine; Japan uses `imperial_occupation_crisis`; the Soviet Union uses `gulag_and_mass_repression_system`.
- Keep a layered state as one registered site. Multiple flags/buildings may coexist, while `camp_state_site_type` remains the single primary display type selected by the shared profile precedence.
- The existing shared constants are binding at equality boundaries: cloning autonomy `55`, archive control `8`, hidden project progress `6`; Soviet paranoia `20/40/65/85`; famine critical `60`; Union Crisis relief cap `8`; Union Crisis relief stop `86`.
- State `88` remains the accepted Auschwitz gameplay anchor even though vanilla calls it Kielce (`history/states/88-Kielce.txt:10,27,32` shows Polish ownership/core and province `9412`). Do not silently move the chain to state `762`.
- State `328` is the exact Pingfang/Harbin gameplay anchor: vanilla state `328` contains Harbin province `10433`. Existing states `716` and `611` remain dormant Japanese labor-site precedents; they are not substitutes for Pingfang.

Authoritative precedents consulted for this handoff include the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, and AI; the official vanilla effect/trigger/script-concept/script-constant/decision/on-action documentation; vanilla Soviet paranoia effects and focuses; and the live Chaos Redux country chains listed below.

## 2. Shared integration surface

### 2.1 Exact new country-package files

| File | Ownership |
| --- | --- |
| `common/scripted_triggers/camp_repression_major_country_triggers.txt` | Strict Germany/Japan/Soviet pool, route, threshold, cloning, project, and reform triggers. |
| `common/scripted_effects/camp_repression_major_country_effects.txt` | Country initializers, value refresh, decisions, missions, site registration, idea refresh, Japan projects/events, Soviet famine, and display projection helpers. |
| `common/decisions/camp_repression_major_country_decisions.txt` | New decisions and missions only; reused decisions stay in their current files. |
| `common/ideas/camp_repression_major_country_ideas.txt` | New staged country ideas. |
| `common/dynamic_modifiers/camp_repression_major_country_dynamic_modifiers.txt` | `sov_famine_pressure_state` and any country-local burden modifiers named in this map. |
| `common/special_projects/projects/japan_ishii_projects.txt` | The five Japan-specific research/risk projects. |
| `events/japan_ishii.txt` | Japan threshold, outbreak, discovery, records, and exposure events. |
| `events/soviet_gulag.txt` | Soviet famine, breakdown, relief, and collapse-record events. |
| `interface/camp_repression_major_country_assets.gfx` | Stable decision/idea/report/project sprite registration. |
| `localisation/english/camp_repression_major_country_l_english.yml` | All new primary, tooltip, event, project, and country-panel strings; UTF-8 with BOM. |

Every new script file needs the repository-standard overview header. These files do not replace the current genocide or Mengele files; the exact bridge edits are listed in section 2.3.

### 2.2 Required helper identifiers

| Country | Scripted triggers | Scripted effects |
| --- | --- | --- |
| Germany | `is_germany_occupied_poland_prisoner_source`, `is_germany_other_occupied_europe_prisoner_source`, `is_germany_core_prisoner_source_fallback`, `germany_mengele_cloning_unlock_ready` | `camp_rework_germany_initialize_country_values`, `camp_rework_germany_refresh_values`, `camp_rework_germany_refresh_ideas`, `camp_rework_germany_monthly_bridge`, `camp_rework_germany_register_auschwitz_layers`, `camp_rework_germany_register_requested_laboratory_state`, `camp_rework_germany_apply_prisoner_transfer`, `germany_mengele_add_cloning_project_progress` |
| Japan | `is_japan_or_subject_controlled_state`, `is_japan_china_manchuria_pool_state`, `is_japan_colonial_occupation_pool_state`, `is_japan_home_island_fallback_state`, `japan_ishii_project_branch_available` | `camp_rework_japan_initialize_country_values`, `camp_rework_japan_refresh_values`, `camp_rework_japan_refresh_ideas`, `camp_rework_japan_monthly_bridge`, `camp_rework_japan_register_pingfang`, `camp_rework_japan_apply_prisoner_experiment`, `camp_rework_japan_apply_outbreak`, `camp_rework_japan_refresh_project_unlocks` |
| Soviet Union | `is_soviet_remote_gulag_pool_state`, `is_soviet_gulag_periphery_pool_state`, `is_soviet_extreme_repression_pool_state`, `sov_camp_is_stalinist_repression_route`, `sov_camp_is_reform_route`, `sov_camp_extreme_escalation_available` | `camp_rework_soviet_initialize_country_values`, `camp_rework_soviet_refresh_values`, `camp_rework_soviet_refresh_ideas`, `camp_rework_soviet_monthly_bridge`, `camp_rework_soviet_refresh_paranoia_projection`, `camp_rework_soviet_update_famine`, `camp_rework_soviet_apply_union_crisis_repression_bridge` |

### 2.3 Exact live integration points and evidence

| Surface | Current evidence | Required edit |
| --- | --- | --- |
| Shared state pools | `common/scripted_triggers/camp_repression_rework_triggers.txt:216-258` defines the generic pools; `:329-396` defines the three major-country gates; `:563-582` dispatches them. | Keep the generic gates. Replace the major-country dispatch with the strict ordered triggers in sections 3-5. |
| Pool arrays and AI selection | `common/scripted_effects/camp_repression_rework_effects.txt:1298-1322` builds country/subject arrays; `:1494-1531` selects the first non-empty generic pool. | Preserve shared arrays for the ledger. Add country-specific selectors where sub-order matters (Poland before other occupied Europe; China/Manchuria before colonial Japan). |
| Country initialization | `common/scripted_effects/camp_repression_rework_effects.txt:12-54` initializes only shared values. | Dispatch the three exact country initializers without creating a second initialization loop. |
| Ideas and monthly bridges | `common/scripted_effects/camp_repression_rework_effects.txt:1804-1883` contains the generic idea dispatcher and an empty country-monthly dispatcher. | Call the three country idea/monthly helpers here. No new periodic on-action. |
| Country displays | `common/scripted_effects/camp_repression_rework_effects.txt:1150-1199` copies shared values and only two Mengele fields. | Copy every `display_*` identifier defined below; do not make GUI variables authoritative gameplay state. |
| AI caps | `common/script_constants/camp_repression_rework_constants.txt:451-455` has GER active/radicalized, JAP active/experiment, and SOV active caps; `common/scripted_triggers/camp_repression_rework_triggers.txt:735-807` only enforces active caps plus Germany/generic radicalized caps. | Preserve GER active `12`/radicalized `5`, JAP active `8`/experiment `3`, and SOV active `14`. Add exact keys `germany_experiment_sites`, `germany_restricted_sites`, `japan_radicalized_sites`, `japan_restricted_sites`, `soviet_radicalized_sites`, `soviet_restricted_sites` plus resolved variables `camp_ai_active_site_cap`, `camp_ai_radicalized_site_cap`, `camp_ai_experiment_site_cap`, `camp_ai_restricted_site_cap`, `camp_ai_active_project_cap`, `camp_ai_can_expand`. Their initial missing values require the tranche's balance pass; the architecture explicitly did not freeze untested numbers. |
| Existing country decisions | `common/decisions/genocide_crisis_decisions.txt:69-264`, `:657-818`, and `:825-1150`; `common/decisions/germany_mengele_decisions.txt:8-325`. | Preserve every reused decision ID in the country registries below and route effects into the shared lifecycle. |
| Historical seeds | `common/scripted_effects/genocide_crisis_effects.txt:1323-1414` seeds Germany `53/64/60`, Japan `716/611`, and Soviet `644/874/881`. | Retain those sites, add state `328` as dormant Pingfang anchor, and seed the Soviet remote-pool flags. Dormant sites do not enter monthly harm until escalation. |
| Deaths ownership | Existing country effects in `common/scripted_effects/genocide_crisis_effects.txt:1012-1266` set a responsible country and then call Deaths. | State owner takes the population loss; responsible country takes evidence/condemnation. Immediate action deaths and recurring monthly deaths must not both represent the same tick. |

## 3. Germany: SS camp administration, Auschwitz, Mengele, and the Directorate

### 3.1 Exact state-pool gates

The prisoner source and the Auschwitz destination are separate scopes. State `88` is always the destination for Auschwitz transfers; the selected `FROM` state is the prisoner source.

1. `is_germany_occupied_poland_prisoner_source`
   - `is_controlled_by = ROOT`
   - `NOT = { is_core_of = ROOT }`
   - `is_on_continent = europe`
   - one of state `88`, `89`, `90`, `92`, `97`, `762`, `is_core_of = POL`, or `is_core_of = SIL`
2. `is_germany_other_occupied_europe_prisoner_source`
   - `is_controlled_by = ROOT`
   - `NOT = { is_core_of = ROOT }`
   - `is_on_continent = europe`
   - `NOT = { is_germany_occupied_poland_prisoner_source = yes }`
3. `is_germany_core_prisoner_source_fallback`
   - `is_owned_and_controlled_by = ROOT`
   - `is_core_of = ROOT`
   - ROOT has no valid state from either higher pool

Both manual targeted decisions and AI selection must enforce this order. A player cannot click an other-occupied or core source while a Polish source exists. Core fallback applies `camp_rework_germany.core_fallback_autonomy = 6`, stability `-0.060`, war support `-0.050`, lower research/project progress, and the shared core-fallback evidence/legitimacy penalty.

Do not reuse `genocide_state_is_german_occupied_poland_target` as the strict first pool. Its current definition at `common/scripted_triggers/genocide_crisis_triggers.txt:402-417` also accepts every `UKR` core. Preserve that legacy identifier for existing callers, but the new strict pool excludes the broad `is_core_of = UKR` branch. The current `is_germany_occupied_transfer_pool_state` at `camp_repression_rework_triggers.txt:329-336` also mixes Poland with every other occupied/non-core state, so generic random array selection cannot satisfy Poland-first behavior.

### 3.2 Auschwitz state 88 and facility registration

Preserve these exact live identifiers:

- `germany_controls_auschwitz_area`, `genocide_auschwitz_experiment_site`, `genocide_ss_laboratory_site`, `germany_mengele_mark_auschwitz_laboratory_site`.
- `germany_mengele.17` facility demand, `germany_mengele.20` monitor, `germany_mengele.22` emergency revolt, `germany_mengele.23` cloning proposal, `germany_mengele.24` completion response.
- Facility candidates `88`, `89`, `64`, `60`; province `9412` remains the existing state-88 construction anchor.

`camp_rework_germany_register_auschwitz_layers` must set responsibility, `camp_rework_experiment_site`, the existing Auschwitz/SS flags as appropriate, and call `camp_rework_register_active_site` once. `germany_mengele_add_requested_biowarfare_facility` must call `camp_rework_germany_register_requested_laboratory_state` inside the actual chosen state branch, so a facility built in `89`, `64`, or `60` does not merely mark state `88`.

Do not edit the `germany_mengele.17` event block. Its accepted option already calls `germany_mengele_add_requested_biowarfare_facility` (`events/germany_mengele.txt:483-536`); registration belongs in that called effect. This also avoids duplicating the event contract.

### 3.3 Decisions and missions

| Status | Exact ID | Role |
| --- | --- | --- |
| Preserve | `germany_wartime_camp_administration` | Centralize SS camp administration. |
| Preserve | `germany_expand_occupied_poland_camp_system` | Occupied Poland expansion. |
| Preserve | `germany_expand_extermination_site_network` | Radicalized network escalation. |
| Preserve | `germany_intensify_extermination_policy` | Harsh policy escalation. |
| Preserve | `germany_transfer_prisoners_to_experiment_site` | Rewire as source-state selection feeding state `88`; do not mark the source as Auschwitz. |
| Preserve | `centralize_race_offices`, `expand_ss_archive`, `classify_eastern_records` | Existing archive/autonomy spine. |
| Preserve | `military_review_of_auschwitz`, `close_auschwitz_program`, `purge_ss_medical_offices` | Existing review/closure/reform spine. |
| Add | `germany_route_prisoner_labor_to_war_construction` | Labor-output project. |
| Add | `germany_redirect_prisoner_labor_to_eastern_fortifications` | Eastern construction project. |
| Add | `germany_tighten_deportation_logistics` | Rail/trains pressure action. |
| Add | `germany_increase_guard_allocation_to_ss_sites` | Guard burden/control action. |
| Add | `germany_build_ss_laboratory_annex_at_auschwitz` | Starts the state-88 annex mission; does not duplicate Event 17. |
| Add | `germany_destroy_auschwitz_evidence_before_retreat` | State-88 retreat crisis wrapper. |
| Add | `germany_dismantle_auschwitz_complex` | Non-fascist/post-defeat dismantlement. |

Required mission IDs and durations:

- `germany_occupied_poland_camp_expansion_mission` — `180` days.
- `germany_eastern_fortifications_labor_mission` — `180` days.
- `germany_ss_laboratory_annex_mission` — `180` days.
- `germany_auschwitz_military_review_mission` — `120` days; started by `military_review_of_auschwitz` rather than replacing that decision ID.
- `germany_auschwitz_evidence_destruction_mission` — `45` days.
- `germany_auschwitz_dismantlement_mission` — `270` days.

Directorate warning/revolt timing remains the existing `germany_mengele.20` threshold chain. Emergency response decisions remain `crush_the_laboratory_state`, `reclaim_laboratory_results`, and `temporary_truce_against_soviets`.

### 3.4 Variables, flags, ideas, and focus hooks

Canonical country variables:

`racial_policy_radicalization`, `ss_archive_control`, `occupied_deportation_pressure`, `poland_transfer_pressure`, `mengele_autonomy`, `mengele_permission_level`, `auschwitz_evidence_depth`, `foreign_atrocity_awareness`, `hardliner_pressure`, `mengele_cloning_project_progress`, `clone_manpower_output`, `laboratory_state_reach`, `numbered_army_growth`, `foreign_clone_network_strength`, `internal_overwrite_pressure`.

`world_threat_source_mengele` is already a global flag (`germany_mengele_refresh_world_threat`, `common/scripted_effects/germany_mengele_effects.txt:245-257`). Preserve it as a Boolean flag; do not also create a numeric country variable with the same name. Project it to `display_world_threat_source_mengele` as `0/1` if the GUI needs a value.

Required display variables are `display_racial_policy_radicalization`, `display_ss_archive_control`, `display_occupied_deportation_pressure`, `display_poland_transfer_pressure`, `display_mengele_autonomy`, `display_mengele_permission_level`, `display_auschwitz_evidence_depth`, `display_foreign_atrocity_awareness`, and `display_hardliner_pressure`.

`mengele_permission_level` preserves the existing enum in `germany_mengele_constants.txt:62-85`: rejected `0`, restricted `1`, limited `2`, full `3`, bypass `4`. Rejected blocks experiment actions; restricted uses the restricted idea/harm branch; limited permits only explicitly limited/foreign-subject operations; full is the minimum cloning permission; bypass receives the highest evidence, harm, and coup-pressure factors. `mengele_autonomy` remains clamped `0..120`, with cloning at `55`, warning at `60`, and coup threshold `85`. Every mutation must call existing `germany_mengele_add_autonomy`; country-kit code must not write autonomy directly.

Preserve country flags `germany_mengele_program_authorized`, `germany_mengele_program_restricted`, `germany_mengele_program_rejected`, `germany_mengele_program_closed`, `germany_mengele_military_review_active`, `germany_mengele_coup_blocked`, `germany_mengele_coup_fired`, `germany_mengele_cloning_project_available`, `germany_mengele_cloning_project_completed`, `directorate_special_project_cloning_available`, `directorate_special_projects_all_available`, `germany_mengele_facility_built_from_demand`, `germany_mengele_facility_demand_cooldown`, `germany_mengele_faction`, `germany_mengele_victorious`, and `germany_mengele_defeated`. Add only `germany_mengele_cloning_unlock_pending` and `germany_auschwitz_complex_dismantled`; use the shared evidence/site flags for all other lifecycle state.

New idea IDs:

- `germany_dormant_ss_camp_legacy`
- `germany_ss_camp_administration`
- `germany_occupied_labor_network`
- `germany_ss_camp_overextension`
- `germany_auschwitz_evidence_pressure`
- `germany_camp_reform_pressure`
- `germany_post_regime_camp_reckoning`

Preserve and integrate existing ideas `germany_auschwitz_experiments`, `germany_auschwitz_experiments_restricted`, `germany_mengele_laboratory_state`, `germany_mengele_cloning_manpower`, `germany_mengele_emergency_crackdown`, `germany_mengele_reclaimed_results`, `germany_mengele_temporary_truce`, `germany_mengele_victory_state`, and `germany_mengele_perfect_aryan_formations`.

No new Germany focus tree is required. Patch the rewards of these exact existing hooks: `MCL_directorate_of_replication`, `MCL_war_laboratory_state`, `MCL_silesian_biological_axis`, `MCL_auschwitz_lab_grid`, `MCL_black_archive_release`, `MCL_occupation_experiment_zones`, `MCL_the_numbered_future`, `MCL_eastern_laboratory_march`, and `MCL_the_numbered_world`. Preserve their existing `mengele_clone_focus_*` completion flags.

### 3.5 Cloning unlock and retry contract

`germany_mengele_cloning_unlock_ready` is true only when all are true:

1. `mengele_permission_level` is at least `constant:germany_mengele_permission.full` (`3`; bypass `4` also passes).
2. `mengele_autonomy` is greater than or equal to `constant:camp_rework_germany.cloning_autonomy_gate` (`55`).
3. At least one controlled state has `biowarfare_facility > 0` and either state `88`, `camp_rework_experiment_site`, `genocide_auschwitz_experiment_site`, or `genocide_ss_laboratory_site`.
4. At least one registered active state has `camp_rework_experiment_site` or `genocide_auschwitz_experiment_site`.
5. `ss_archive_control >= 8` or `NOT = { has_country_flag = germany_mengele_military_review_active }`.
6. `mengele_cloning_project_progress >= 6`.
7. Neither `germany_mengele_cloning_project_available` nor `germany_mengele_cloning_project_completed` is set.

Use explicit `greater_than_or_equals` comparisons at the `55/8/6` boundaries. `germany_mengele_add_cloning_project_progress` is the sole mutation helper and receives progress from completed abnormal reports, classified records, accepted laboratory construction, and valid experiment transfers. Clamp the value; do not use special-project completion as hidden progress.

The initial authorization currently schedules `.23` once (`germany_mengele_effects.txt:1453-1483`), while `.23` currently checks only the active program (`events/germany_mengele.txt:678-700`). Replace `.23`'s trigger with the exact gate. If the first scheduled proposal fails, set `germany_mengele_cloning_unlock_pending`; the already-recurring `.20` monitor evaluates the gate before its coup branches and reschedules `.23` once when ready. Clear the pending flag on unlock, closure, purge, coup, or project completion. This is the required retry path.

In `sp_mengele_cloning`, ordinary Germany must require both `germany_mengele_cloning_project_available` and `germany_mengele_cloning_unlock_ready`; the existing Directorate flags remain explicit bypass routes. Project output remains `germany_mengele_complete_cloning_project`; never directly mark the project complete from a focus, decision, or event.

### 3.6 Assets and localisation

Required sprite IDs:

- Decisions: `GFX_decision_germany_ss_camp_administration`, `GFX_decision_germany_auschwitz_transfer`, `GFX_decision_germany_ss_laboratory_annex`, `GFX_decision_germany_military_review`, plus shared `GFX_decision_camp_guard_allocation`, `GFX_decision_camp_evidence_destruction`, and `GFX_decision_camp_dismantlement`.
- Ideas: `GFX_idea_germany_dormant_ss_camp_legacy`, `GFX_idea_germany_ss_camp_administration`, `GFX_idea_germany_mengele_laboratory_autonomy`, `GFX_idea_germany_auschwitz_evidence_pressure`, plus shared `GFX_idea_camp_network_overreach` and `GFX_idea_camp_dismantlement_reform`.
- Reports/projects: `GFX_report_event_auschwitz_discovery`; preserve `GFX_sp_mengele_cloning`.

Localisation rule: every new decision, mission, and idea ID in section 3 creates exactly `<id>` and `<id>_desc`. Every new mission also creates `<id>_success` and `<id>_failure`. Mixed-cost decisions create `<id>_cost` and `<id>_cost_blocked`. Additional exact keys are:

Every preserved decision/mission/idea keeps its existing same-stem localisation keys; do not rename the live `chaosx_decisions_l_english.yml` or `germany_mengele_l_english.yml` keys while rewiring effects.

`germany_occupied_poland_pool_required_tt`, `germany_occupied_poland_priority_tt`, `germany_core_transfer_fallback_penalty_tt`, `germany_auschwitz_state_88_required_tt`, `germany_mengele_cloning_unlock_requirements_tt`, `germany_mengele_cloning_unlock_pending_tt`, `germany_auschwitz_dismantlement_effect_tt`, `camp_ledger_country_panel_germany`, `camp_ledger_mengele_autonomy`, `camp_ledger_mengele_permission`, `camp_ledger_ss_archive_control`, `camp_ledger_poland_transfer_pressure`, `camp_ledger_auschwitz_evidence_depth` and a matching `_tt` key for each `camp_ledger_*` value label.

### 3.7 Germany validation scenarios

1. Before Poland is occupied, dormant German sites remain out of monthly harm and no core-transfer option bypasses the pool order.
2. With any strict Polish source present, 100 repeated AI selections and all manual targets choose only pool 1.
3. With no Polish source but another occupied/non-core European state, the other occupied pool is used; with neither, only the punitive core fallback is enabled.
4. State `88` simultaneously retains detention/labor, radicalized, experiment, facility, evidence, and cloning flags without duplicate array membership.
5. Accepting Event `.17` for `88`, `89`, `64`, and `60` registers the actually built facility state and assigns Germany as responsible without editing `.17` itself.
6. Restricted/full/bypass permission produces distinct experiment harm/research/evidence/coup effects; the current direct state-88 Deaths routine does not double the shared monthly site death.
7. Cloning fails at `54.99/7.99/5.99`, passes at exactly `55/8/6`, and still requires permission `3` or `4`, facility, and active experiment site.
8. A failed first `.23` attempt later unlocks exactly once through `.20`; closure/purge/coup cancels the retry.
9. Directorate availability flags still expose the project without the ordinary-Germany gate, and completion still goes through `.24`/the existing coup logic.
10. Regime change and dismantlement clear active experiment processing, reduce autonomy, retain discoverable evidence, and satisfy the post-Directorate cleanup path.

## 4. Japan: Shiro Ishii, Pingfang, occupied China, and Manchuria

### 4.1 Exact state-pool gates

`is_japan_or_subject_controlled_state` is `OR = { is_controlled_by = ROOT; CONTROLLER = { is_subject_of = ROOT } }`. This is required because the shared subject loop keeps Japan as ROOT; the current `is_controlled_by = ROOT` test at `camp_repression_rework_triggers.txt:347-359` rejects Manchukuo-controlled states.

Ordered pools:

1. `is_japan_china_manchuria_pool_state`: Japan/subject-controlled, not a JAP core, and core of one of `CHI`, `PRC`, `GXC`, `MEN`, `MAN`, `YUN`, `SHX`, `XSM`.
2. `is_japan_colonial_occupation_pool_state`: Japan/subject-controlled, not a JAP core, not pool 1, and either `camp_rework_japan_colonial_pool` or core of `KOR`, `FSM`, `PLU`, `PHI`, `INS`, or `MAL`.
3. `is_japan_home_island_fallback_state`: owned and controlled by Japan, JAP core, no state in pools 1-2, `camp_rework_country_is_desperate_in_war = yes`, and chaos tier `4` or `5`.

Manual and AI selection must enforce China/Manchuria before colonial, and both before home fallback. The home fallback applies lower `bio_research_gain`, lower `ishii_influence`, major stability loss, military-obedience/review pressure, evidence, and the shared core-fallback penalty.

State `328` receives `camp_rework_pingfang_anchor`. It contains Harbin province `10433` in vanilla (`history/states/328-Manchukuo.txt:22-32`). The existing historical initializer at `genocide_crisis_effects.txt:1358-1382` keeps `716` Liaotung and `611` North China as quiet labor sites and adds `328` as the dormant Pingfang experiment candidate.

### 4.2 Decisions, missions, projects, and events

| Status | Exact ID | Role |
| --- | --- | --- |
| Preserve | `japan_expand_forced_labor_camps` | Occupied labor expansion. |
| Preserve | `japan_conduct_anti_partisan_reprisals` | Occupation reprisals. |
| Preserve | `japan_transfer_prisoners_to_experimental_facilities` | Rewire through canonical Ishii values and owner/responsibility attribution. |
| Preserve | `japan_destroy_occupation_records` | General retreat-record action. |
| Add | `japan_establish_pingfang_research_bureau` | Fixed state-328 bureau/facility start. |
| Add | `japan_expand_occupation_test_records` | Records/project pressure. |
| Add | `japan_shield_ishii_from_army_review` | Influence/autonomy escalation. |
| Add | `japan_redirect_records_to_army_medical_control` | Evidence/authority branch. |
| Add | `japan_invite_kwantung_army_medical_officers` | Kwantung authority branch. |
| Add | `japan_suppress_chinese_resistance_cells` | Pool-1 repression action. |
| Add | `japan_route_supplies_to_epidemic_prevention` | Supply/containment preparation. |
| Add | `japan_open_epidemic_containment_office` | Post-outbreak containment. |
| Add | `japan_destroy_pingfang_records` | State-328 records choice, distinct from the general state-target action. |
| Add | `japan_evacuate_pingfang_research_staff` | Soviet/Allied approach branch. |
| Add | `japan_submit_to_army_review` | Review/reform branch. |
| Add | `japan_remove_ishii_from_program_control` | Removes authority and closes project escalation. |
| Add | `japan_shut_down_prisoner_experiments` | Long reform/dismantlement action. |

Mission IDs and durations:

- `japan_pingfang_research_bureau_mission` — `180` days.
- `japan_army_medical_review_mission` — `120` days.
- `japan_epidemic_containment_mission` — `150` days.
- `japan_pingfang_evacuation_mission` — `45` days.
- `japan_prisoner_experiment_shutdown_mission` — `270` days.

Special-project IDs, in branch order:

1. `sp_japan_pingfang_records_office`
2. `sp_japan_kwantung_medical_intelligence`
3. `sp_japan_occupation_test_ledger`
4. `sp_japan_epidemic_mapping_bureau`
5. `sp_japan_cherry_blossom_dossier`

Availability flags use the same stem plus `_available` without the `sp_` prefix: `japan_pingfang_records_office_available`, `japan_kwantung_medical_intelligence_available`, `japan_occupation_test_ledger_available`, `japan_epidemic_mapping_bureau_available`, `japan_cherry_blossom_dossier_available`. Completion is checked with `is_special_project_completed`; do not duplicate completion into five country flags.

Project gates:

- Records Office: Ishii character exists, state `328` bureau complete, active experiment-linked site, war with China or an active China/Manchuria occupation pool.
- Kwantung Intelligence: Records Office complete, `ishii_influence >= 20`, `kwantung_autonomy >= 20`.
- Occupation Test Ledger: Records Office complete, `occupation_test_records >= 20`, active experiment site.
- Epidemic Mapping Bureau: at least one earlier project complete and either outbreak risk/evidence is non-zero or an outbreak has occurred; ethical use reduces risk but never erases evidence.
- Cherry Blossom Dossier: `ishii_influence >= 55`, high `bio_project_pressure`, desperate war, chaos tier `4/5`, existing biowarfare capacity, and no shutdown/reform flag. It alters existing doomsday biowarfare availability/risk only; it does not add an operational attack recipe.

Event namespace and exact IDs:

- `japan_ishii.1` — Ishii gains independent authority (`.a`).
- `japan_ishii.2` — Kwantung officers bypass Tokyo (`.a`, `.b`).
- `japan_ishii.3` — uncontrolled occupied-territory outbreak (`.a`, `.b`, `.c`).
- `japan_ishii.4` — Soviet/Allied discovery of Pingfang evidence (`.a`).
- `japan_ishii.5` — evacuate, destroy, or surrender records (`.a`, `.b`, `.c`).
- `japan_ishii.6` — postwar tribunal exposure (`.a`).

### 4.3 Variables, flags, ideas, and route hooks

Canonical variables:

`imperial_occupation_reach`, `kwantung_autonomy`, `ishii_influence`, `occupation_test_records`, `bio_research_gain`, `bio_project_pressure`, `outbreak_accident_risk`, `chinese_resistance_pressure`, `occupation_evidence_depth`, `evidence_depth_china`, `tribunal_biowarfare_severity`, `pingfang_facility_level`, `imperial_army_review_pressure`.

Required display variables are the same stems prefixed with `display_`.

The live prisoner-experiment effect currently writes `japan_ishii_influence` and `japan_biological_outbreak_risk` (`genocide_crisis_effects.txt:1035-1061`). Those conflict with the accepted canonical identifiers. One-time migration copies either alias into `ishii_influence` / `outbreak_accident_risk` only when the canonical value is absent, then clears the aliases. No new code may continue writing the aliases.

Preserve Ishii's existing character identifiers `JAP_shiro_ishii`, `chaosx_scientist_jap_shiro_ishii`, and `GFX_portrait_JAP_shiro_ishii` (`chaosx_startup_history_effects.txt:613-633`).

Country flags:

`japan_ishii_program_active`, `japan_ishii_independent_authority`, `japan_kwantung_medical_bypass`, `japan_army_medical_review_active`, `japan_prisoner_experiments_shutdown`, `japan_pingfang_records_destroyed`, `japan_pingfang_staff_evacuated`, `japan_pingfang_records_surrendered`, `japan_pingfang_evidence_exposed`, `japan_biowarfare_outbreak_active`, `japan_biowarfare_outbreak_contained`, plus the five project availability flags above.

State flags:

`camp_rework_pingfang_anchor`, `camp_rework_japan_colonial_pool`, `camp_rework_japan_outbreak_site`, `camp_rework_japan_records_site`, `camp_rework_japan_home_fallback_used`; preserve shared `camp_rework_experiment_site` and `genocide_japanese_biowarfare_atrocity_site`.

No live Japan-specific focus tree exists. The accepted focus-hook surface is therefore these exact route flags, set by decisions/projects and available to a future additive tree without changing IDs: `japan_pingfang_route_unlocked`, `japan_ishii_authority_route`, `japan_biowarfare_containment_route`, `japan_biowarfare_reform_route`.

New idea IDs:

`japan_dormant_occupation_apparatus`, `japan_imperial_occupation_repression`, `japan_forced_labor_experiment_network`, `japan_ishii_program_authority`, `japan_kwantung_medical_autonomy`, `japan_biowarfare_outbreak_pressure`, `japan_imperial_army_review`, `japan_pingfang_exposure_pressure`, `japan_biowarfare_program_overextension`, `japan_reformed_biowarfare_legacy`.

### 4.4 Assets and localisation

Required sprite IDs:

- Decisions: `GFX_decision_japan_pingfang_bureau`, `GFX_decision_japan_prisoner_experiment`, `GFX_decision_japan_army_medical_review`, `GFX_decision_japan_pingfang_records`, `GFX_decision_japan_epidemic_containment`.
- Ideas: `GFX_idea_japan_occupation_apparatus`, `GFX_idea_japan_ishii_influence`, `GFX_idea_japan_kwantung_autonomy`, `GFX_idea_japan_outbreak_pressure`, `GFX_idea_japan_program_review`.
- Projects: `GFX_sp_japan_pingfang_records_office`, `GFX_sp_japan_kwantung_medical_intelligence`, `GFX_sp_japan_occupation_test_ledger`, `GFX_sp_japan_epidemic_mapping_bureau`, `GFX_sp_japan_cherry_blossom_dossier`.
- Reports: `GFX_report_event_pingfang_exposure`; reserve `GFX_news_event_pingfang_exposure` only if the conditional super-event is separately accepted.
- Preserve `GFX_portrait_JAP_shiro_ishii`.

Localisation rule: every new decision, mission, idea, and project ID in section 4 creates exactly `<id>` and `<id>_desc`; missions also create `<id>_success` and `<id>_failure`; projects create `<id>_completed_tt`; mixed-cost decisions create `<id>_cost` and `<id>_cost_blocked`.

Every preserved Japan decision and Ishii character keeps its existing same-stem localisation keys.

Additional exact keys:

`japan_china_manchuria_pool_required_tt`, `japan_colonial_pool_required_tt`, `japan_home_island_fallback_penalty_tt`, `japan_pingfang_anchor_required_tt`, `japan_ishii_project_gate_tt`, `japan_outbreak_risk_effect_tt`, `japan_pingfang_records_choice_tt`, `camp_ledger_country_panel_japan`, `camp_ledger_ishii_influence`, `camp_ledger_kwantung_autonomy`, `camp_ledger_pingfang_facility_level`, `camp_ledger_occupation_test_records`, `camp_ledger_outbreak_accident_risk`, `camp_ledger_imperial_army_review_pressure` and a matching `_tt` for each country-panel value.

Event localisation keys are exactly each event ID with `.t`, `.d`, and the option suffixes listed in section 4.2; for example `japan_ishii.3.t`, `japan_ishii.3.d`, `japan_ishii.3.a`, `japan_ishii.3.b`, `japan_ishii.3.c`.

### 4.5 Japan validation scenarios

1. Japan controls state `328` directly and through a Manchukuo subject in separate tests; both expose Pingfang setup and preserve the state owner as the Deaths population-loss scope.
2. With China/Manchuria and colonial states present, all manual/AI selections use pool 1; with pool 1 absent, pool 2; home islands remain blocked until both are empty plus desperate war and chaos `4/5`.
3. State `328` becomes the Pingfang anchor; states `716` and `611` remain dormant labor precedents and do not impersonate Pingfang.
4. Alias migration runs once, clears `japan_ishii_influence` / `japan_biological_outbreak_risk`, and preserves their values in canonical fields.
5. Each project unlocks only after its predecessor/gates, never auto-completes, and does not expose an operational biological-attack recipe.
6. Japan caps at `8` active and `3` experiment sites under AI; a fourth experiment expansion receives zero AI weight.
7. Outbreak threshold fires once, applies owner-linked Deaths and Japan-linked evidence, and containment lowers risk without deleting records.
8. Soviet/Allied approach enables the `45`-day evacuation/records branch; destroy, evacuate, and surrender produce distinct evidence/tribunal outcomes.
9. Army review, Ishii removal, and experiment shutdown stop new escalation and recurring experiment harm while preserving discovery evidence.
10. Post-defeat exposure reads `evidence_depth_china` and `tribunal_biowarfare_severity`, not the obsolete aliases.

## 5. Soviet Union: paranoia, gulags, famine, and Union Crisis

### 5.1 Exact state pools

`is_soviet_remote_gulag_pool_state` requires Soviet control and one of:

- fixed remote/northern/Far Eastern/Siberian/steppe states `213`, `214`, `407`, `408`, `409`, `516`, `574`, `575`, `576`, `577`, `578`, `579`, `580`, `581`, `582`, `583`, `584`, `585`, `586`, `587`, `588`, `589`, `590`, `644`, `655`, `822`, `825`, `874`, `875`, `881`, `882`;
- core of `KAZ`, `KYR`, `TAJ`, `TMS`, or `UZB`;
- `camp_rework_soviet_remote_pool`, `camp_rework_soviet_industrial_pool`, or `camp_rework_prison_labor_pool`.

`is_soviet_gulag_periphery_pool_state` is the remote pool or a controlled state that is core of `UKR`, `BLR`, `GEO`, `ARM`, `AZR`, has `camp_rework_soviet_borderland_pool` / `camp_rework_political_opposition_pool`, or is non-core with resistance.

`is_soviet_extreme_repression_pool_state` is narrower: controlled, periphery/borderland/opposition or non-core resistance, and `sov_camp_extreme_escalation_available = yes`. It never offers a protected-class target menu.

`sov_camp_extreme_escalation_available` additionally requires `NOT = { sov_camp_is_reform_route = yes }` and at least one exact escalation gate: `paranoia_pressure >= 85`; completed focus `SOV_the_workers_dictatorship`, `SOV_left_purges`, or `SOV_the_enemies_of_the_people`; chaos tier `4/5`; or active Union Crisis with `soviet_collapse_total_collapse_threat >= 86`. This trigger controls visibility, availability, and AI weight so the player cannot bypass it through a highlighted state.

The current legacy trigger at `genocide_crisis_triggers.txt:448-457` contains only `644/874/881/516/581/582`; preserve that ID for existing callers but dispatch the rework through the expanded pool. The current new trigger at `camp_repression_rework_triggers.txt:376-396` adds republic cores but still omits most remote/northern/Far Eastern seeds and industrial flags.

### 5.2 Paranoia is a projection, not a second system

Preserve vanilla `SOV_paranoia`, `SOV_paranoia_system_active_flag`, `SOV_paranoia_low_increase_effect`, `SOV_paranoia_medium_increase_effect`, `SOV_paranoia_high_increase_effect`, all matching decrease effects, and `SOV_paranoia_clamp_and_update_ui_effect` (vanilla `common/scripted_effects/SOV_scripted_effects.txt:149-285`).

`paranoia_pressure` is refreshed from `SOV_paranoia` only while `SOV_paranoia_system_active_flag` exists; otherwise it is `0`. Country decisions call the appropriate vanilla increase/decrease effect and then refresh the projection. The camp package must never initiate the vanilla paranoia system, directly mutate both variables, or maintain an independent decay curve.

Threshold gates use the existing constants and include equality:

- low: `20 <= paranoia_pressure < 40`
- medium: `40 <= paranoia_pressure < 65`
- high: `65 <= paranoia_pressure < 85`
- critical: `paranoia_pressure >= 85`

Focus-hook triggers use exact vanilla focus IDs:

- Stalinist/repression: `SOV_the_centre`, `SOV_the_collectivization_process`, `SOV_the_workers_dictatorship`, `SOV_nkvd_primacy`.
- Centre reform/de-escalation: `SOV_ban_excessive_hero_worship`, `SOV_freedom_of_debate_unity_of_action`.
- Left/opposition reform: `SOV_system_decentralization`, `SOV_return_democracy_to_the_party`.
- Right/opposition reform: `SOV_reverse_the_collectivization_process`, `SOV_administrative_reforms`, `SOV_socialist_humanism`.

No base-Soviet custom focus tree exists in the mod; these direct `has_completed_focus` hooks are the accepted integration surface. Do not edit the successor-country `005` focus trees as a substitute.

### 5.3 Decisions, missions, and famine chain

Preserve exact decision IDs `sov_show_gulag_decisions`, `sov_hide_gulag_decisions`, `sov_expand_gulag_network`, `sov_deport_suspected_opposition_groups`, `sov_confiscate_food_from_disloyal_regions`, `sov_purge_camp_administrators`, `sov_raise_forced_labor_quotas`, and `sov_destroy_gulag_records`.

Add:

- `sov_transfer_prisoners_to_industrial_camps`
- `sov_reinforce_nkvd_authority`
- `sov_reduce_paranoia_through_party_review`
- `sov_release_prisoners_for_military_service`
- `sov_dismantle_overextended_gulags`
- `sov_emergency_famine_relief`
- `sov_conceal_famine_mortality`
- `sov_admit_local_administrative_collapse`

Mission IDs and durations:

- `sov_gulag_quota_cycle` — `180` days.
- `sov_famine_pressure_cycle` — `180` days.
- `sov_emergency_famine_relief_mission` — `180` days.
- `sov_camp_administrator_review_mission` — `150` days.
- `sov_overextended_gulag_dismantlement_mission` — `270` days.
- `sov_retreat_records_crisis_mission` — `45` days.

Famine is persistent, not the current single confiscation burst at `genocide_crisis_effects.txt:1196-1217`. Grain confiscation and quota overreach add country `grain_extraction_burden` / `famine_pressure` and state `sov_famine_state_pressure`. Medium paranoia plus positive grain burden may start the pressure cycle; high paranoia permits crisis events; country `famine_pressure >= 60` permits the critical branch. Monthly state harm uses the shared Deaths processor once, then applies state modifier `sov_famine_pressure_state`; relief lowers pressure, output, and quota burden but does not erase evidence.

Event namespace and exact IDs:

- `soviet_gulag.1` — famine warning (`.a`, `.b`).
- `soviet_gulag.2` — famine crisis (`.a`, `.b`, `.c`).
- `soviet_gulag.3` — local administrative breakdown (`.a`, `.b`).
- `soviet_gulag.4` — relief outcome (`.a`).
- `soviet_gulag.5` — post-collapse/invasion records discovered (`.a`).

### 5.4 Union Crisis suppression cap

Preserve `soviet_collapse_apply_genocide_gulag_repression_memory`, `soviet_collapse_gulag_repression_memory`, `soviet_collapse_total_collapse_threat`, `soviet_collapse_moscow_authority`, `soviet_collapse_military_obedience`, `soviet_collapse_republic_confidence`, `soviet_collapse_old_movement_pressure`, `soviet_collapse_foreign_appetite`, `soviet_collapse_progressive_release_pressure`, `soviet_collapse_active`, and `soviet_collapse_terminal_collapse`.

The current bridge at `common/scripted_effects/005_soviet_collapse_effects.txt:61-103` grants authority/obedience/republic relief on every call below threat `86`; the current action effects call it repeatedly (`genocide_crisis_effects.txt:1173-1266`). Refactor it through `camp_rework_soviet_apply_union_crisis_repression_bridge`:

1. Every material repression action always increases `soviet_collapse_gulag_repression_memory`, `old_movement_grievance`, `republic_fear`, old-movement pressure, and foreign appetite when the relevant variables exist.
2. Beneficial relief is allowed only while `is_soviet_collapse_active = yes`, no terminal flag exists, total threat is strictly below `86`, and `union_crisis_suppression_relief < 8`.
3. Requested minor/major relief is `1/2`. Grant `min(requested, 8 - union_crisis_suppression_relief)` and add exactly the granted amount to the accumulator. A country at `7` receiving a major action gains only `1` benefit.
4. At threat exactly `86`, above `86`, after the accumulator reaches `8`, or after terminal collapse, no authority/obedience/release benefit occurs; harmful grievance/memory still occurs.
5. Clamp/recalculate the Union Crisis once after the complete action, not once per state and not from the monthly country pulse.

`union_crisis_terminal_severity` is a projection of `soviet_collapse_total_collapse_threat` while the crisis is active, not a competing crisis meter.

### 5.5 Variables, flags, and ideas

Canonical country variables:

`gulag_network_reach`, `nkvd_authority`, `paranoia_pressure`, `forced_labor_quota`, `grain_extraction_burden`, `famine_pressure`, `republic_fear`, `old_movement_grievance`, `camp_administrator_corruption`, `union_crisis_suppression_relief`, `union_crisis_terminal_severity`.

State variable: `sov_famine_state_pressure`. Required display variables are each country-variable stem prefixed with `display_`.

Country flags: `sov_famine_warning_fired`, `sov_famine_crisis_active`, `sov_famine_critical_fired`, `sov_famine_relief_active`, `sov_gulag_dismantlement_active`.

State flags: `camp_rework_soviet_gulag_dormant`, `camp_rework_soviet_remote_pool`, `camp_rework_soviet_industrial_pool`, `camp_rework_soviet_borderland_pool`, `camp_rework_soviet_famine_pressure`, `camp_rework_soviet_famine_crisis`, `camp_rework_soviet_mass_deportation_site`, `camp_rework_soviet_records_concealed`.

New idea IDs:

`sov_dormant_gulag_legacy`, `sov_gulag_network_administration`, `sov_nkvd_repression_authority`, `sov_forced_labor_output`, `sov_gulag_corruption_and_overextension`, `sov_famine_pressure`, `sov_republic_fear_and_grievance`, `sov_gulag_reform_pressure`, `sov_post_collapse_repression_legacy`.

Dynamic state modifier: `sov_famine_pressure_state`.

### 5.6 Assets and localisation

Required sprite IDs:

- Decisions: `GFX_decision_sov_gulag_expansion`, `GFX_decision_sov_prisoner_transfer`, `GFX_decision_sov_grain_confiscation`, `GFX_decision_sov_nkvd_review`, `GFX_decision_sov_famine_relief`, `GFX_decision_sov_gulag_dismantlement`, `GFX_decision_sov_records_retreat`.
- Ideas: `GFX_idea_sov_gulag_legacy`, `GFX_idea_sov_gulag_authority`, `GFX_idea_sov_famine_pressure`, `GFX_idea_sov_republic_fear`, `GFX_idea_sov_gulag_reform`.
- Reports: `GFX_report_event_soviet_famine_crisis`; reserve `GFX_news_event_soviet_famine_catastrophe` only if the conditional super-event is separately accepted.

Localisation rule: every new decision, mission, idea, and dynamic modifier ID in section 5 creates exactly `<id>` and `<id>_desc`; missions also create `<id>_success` and `<id>_failure`; mixed-cost decisions create `<id>_cost` and `<id>_cost_blocked`.

Every preserved Soviet decision keeps its existing same-stem localisation keys and existing `_effect_tt` where present.

Additional exact keys:

`sov_paranoia_medium_required_tt`, `sov_paranoia_high_required_tt`, `sov_paranoia_critical_required_tt`, `sov_gulag_periphery_pool_required_tt`, `sov_union_crisis_suppression_cap_tt`, `sov_union_crisis_relief_stopped_tt`, `sov_famine_pressure_effect_tt`, `sov_famine_relief_effect_tt`, `sov_gulag_dismantlement_effect_tt`, `camp_ledger_country_panel_soviet`, `camp_ledger_paranoia_pressure`, `camp_ledger_nkvd_authority`, `camp_ledger_gulag_network_reach`, `camp_ledger_grain_extraction_burden`, `camp_ledger_famine_pressure`, `camp_ledger_old_movement_grievance`, `camp_ledger_union_crisis_suppression_relief` and a matching `_tt` for each country-panel value.

Event localisation keys are exactly each event ID with `.t`, `.d`, and the option suffixes listed in section 5.3.

### 5.7 Soviet validation scenarios

1. With vanilla paranoia active, boundaries `19.99/20`, `39.99/40`, `64.99/65`, and `84.99/85` select the expected bands; after every action `paranoia_pressure == SOV_paranoia`.
2. With vanilla paranoia inactive, the package does not initialize it, `paranoia_pressure` remains `0`, dormant gulags stay quiet, and only non-paranoia background/reform actions appear.
3. Each fixed remote state, Central Asian/republic core, and flagged industrial/periphery state enters the intended pool; no state is selected because of a protected-class identity.
4. Medium paranoia plus grain burden starts pressure; high paranoia permits crisis events; critical famine begins at exactly `60`; monthly Deaths and the state modifier represent one harm tick.
5. Eight minor or four major Union Crisis actions below threat `86` exhaust relief. A mixed action at accumulator `7` grants only `1`; further actions add grievance but no benefit.
6. Threat `85.99` may grant remaining relief; exactly `86`, terminal collapse, or inactive crisis grants none and does not touch absent crisis variables.
7. Stalinist/NKVD hooks raise escalation weights; centre/left/right reform hooks block extreme escalation and expose review/dismantlement.
8. Critical escalation requires the exact route/chaos/collapse gate, uses only the extreme periphery pool, and stops when the resolved Soviet radicalized or restricted cap is reached.
9. Relief, reduced quota, improved supply, party review, and dismantlement lower famine pressure; concealment lowers visibility while increasing evidence/tribunal risk.
10. Collapse/invasion records carry famine, deportation, old-movement grievance, and foreign evidence into successor hostility and the existing Union Crisis aftermath.

## 6. Collision and missing-precedent register

The proposed `Add` IDs and new sprite IDs were searched against live `common/`, `events/`, `interface/`, `localisation/`, and `gfx/` content; none already exist. The collisions below are semantic or legacy-identifier conflicts that must be handled deliberately.

| Risk | Evidence | Binding resolution |
| --- | --- | --- |
| Poland is not actually first | `is_germany_occupied_transfer_pool_state` mixes Poland with all occupied/non-core states; shared selection randomizes within the first generic array. | Add strict Germany sub-pools and enforce them for manual and AI targets. |
| Legacy "Poland" includes Ukraine | `genocide_state_is_german_occupied_poland_target` includes `is_core_of = UKR`. | Preserve the legacy trigger, but use a new strict Poland trigger for the camp rework. |
| Auschwitz source/destination conflation | Current transfer marks `FROM` as an Auschwitz experiment site. | `FROM` is the source; state `88` is the experiment destination and only destination receives Auschwitz layers. |
| Germany transfer ignores permission tier | `genocide_germany_transfer_prisoners_to_experiment_site_in_from` grants the full autonomy delta whenever the permission variable merely exists (`genocide_crisis_effects.txt:1155-1162`). | Branch on rejected/restricted/limited/full/bypass and call `germany_mengele_add_autonomy` with the resolved tier; rejected blocks the action. |
| Facility registration mismatch | `germany_mengele_add_requested_biowarfare_facility` can build in `89/64/60` but later marks only state `88`. | Register the state inside the selected facility branch; do not edit Event `.17`. |
| Duplicate Deaths risk | `germany_mengele_register_experiment_deaths` directly reports state-88 deaths while the shared monthly site processor can report the same experiment harm. | Immediate action burst and recurring monthly harm must use distinct reasons/ticks; only the shared processor handles recurring harm. |
| Cloning unlock can be missed forever | Authorization schedules `.23` once; `.23` has a weak active-program trigger. | Exact gate plus `germany_mengele_cloning_unlock_pending` retried by recurring `.20`. |
| `world_threat_source_mengele` type collision | Accepted value list names it as a value, live code uses a global flag. | Preserve it as the existing Boolean global flag; do not create a same-name numeric variable. |
| Pingfang anchor absent | Current Japan history seeds only `716/611`; vanilla Harbin is province `10433` in state `328`. | Add dormant state `328` anchor; keep `716/611` as labor sites. |
| Manchukuo subject states fail pool gate | Current Japanese trigger requires `is_controlled_by = ROOT` even in the subject-country loop. | Accept controllers that are subjects of Japan and preserve owner-linked Deaths attribution. |
| Japan canonical value collision | Live effect writes `japan_ishii_influence` and `japan_biological_outbreak_risk`; accepted names omit those prefixes. | One-time migrate to `ishii_influence` and `outbreak_accident_risk`, clear aliases, and prohibit new alias writes. |
| Japan package has no live deep precedent | Ishii exists only as generated scientist/portrait; no Pingfang projects/events/ideas exist. | Implement the exact additive files/IDs in section 4; do not copy Germany's route. |
| Soviet pool is too narrow | Legacy whitelist has six states; new gate adds republic cores but omits much of the accepted remote/northern/Far East/industrial coverage. | Use the exact remote whitelist and pool flags in section 5.1. |
| Duplicate Soviet paranoia meter | Accepted `paranoia_pressure` can drift from vanilla `SOV_paranoia`. | Make it a read-only projection and mutate only through vanilla effects. |
| Famine is only an immediate burst | Current confiscation effect sets a flag and immediate Deaths but has no persistent management chain. | Country/state pressure, missions, monthly processor, relief, evidence, and breakdown events as mapped. |
| Union Crisis relief is uncapped | Existing bridge grants benefit on every action below `86`. | Accumulator cap `8`, partial final grant, strict stop at `86`, harmful memory always retained. |
| Country dispatcher is empty | `camp_rework_update_country_specific_monthly_bridges = {}`. | Fill the stable dispatcher; do not add an on-action. |
| Country GUI is incomplete | Core display copy has only two Germany fields, no Japan/Soviet projections. | Add every exact `display_*` and `camp_ledger_*` key in this map. |
| AI cap surface is incomplete | Constants exist for only some required dimensions, and current triggers do not resolve all active/radicalized/experiment/restricted caps. | Add the exact missing constant keys/resolved variables in section 2.3, assign untested numbers during the balance pass, and hard-zero AI weights at or above the resolved cap. |

## 7. Implementation order and completion proof

1. Add strict triggers, canonical variables/flags, alias migration, and country initializers.
2. Wire existing country decisions/effects into registration, value refresh, and the single Deaths lifecycle.
3. Add the exact new decisions, missions, ideas, Japan projects/events, and Soviet famine events.
4. Patch Germany's facility helper, cloning gate/retry, project availability, and existing focus rewards; do not edit `germany_mengele.17`.
5. Refactor the Soviet Union Crisis bridge with the `8/86` cap contract.
6. Wire the country idea/monthly/display dispatchers and AI caps without a new periodic loop.
7. Register the stable sprite IDs before asset production; add all deterministic and explicit localisation keys in the same implementation tranche.
8. Run the scenario suites in sections 3.7, 4.5, and 5.7, then use the country-package, decision/mission, focus, localisation, and event-completion audit routes before a completion claim.

The tranche is incomplete if any listed decision/mission/idea/project/event/value/flag/display/asset/localisation identifier is omitted, if Poland/China-Manchuria/remote-Soviet ordering is not enforced for both player and AI, if recurring harm can be counted twice, if Japan uses the obsolete value aliases, if Soviet paranoia becomes independent, or if Union Crisis relief can exceed `8` or apply at threat `86`.

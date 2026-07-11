# Colonial Country Kit Implementation Map

## Purpose and status

This file now records the live U.K./Raj, U.S.A., France/Vichy/North Africa, Italy, and Belgium/Congo implementation. The original read-only audit is retained below as preimplementation evidence. Statements in that snapshot that call files, values, decisions, missions, assets, or action routing absent are superseded by this section.

The colonial decision file contains **43 verified player actions** and 19 missions. The final split is U.K./Raj 10, U.S.A. 8, France/Vichy 9, Italy 8, and Belgium/Congo 8. The closing actions are live as `fr_support_refugee_and_rescue_networks` and `bel_negotiate_colonial_strike_settlement`. The exact implemented action IDs are controlled by `common/decisions/camp_repression_colonial_country_decisions.txt` and the source-of-truth tracker. The final decision-and-mission re-audit passed; any lower counts or absent-surface statements retained below are preimplementation history only.

Current implementation files are:

- `common/decisions/camp_repression_colonial_country_decisions.txt`
- `common/scripted_effects/camp_repression_colonial_country_effects.txt`
- `common/ideas/camp_repression_colonial_country_ideas.txt`
- `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`
- `localisation/english/camp_repression_country_kits_l_english.yml`
- `interface/camp_repression_rework.gfx`

Subject-controlled state actions are live. Decisions and Ledger buttons use `camp_rework_action_state_id`, and the colonial prepare and restore helpers temporarily adapt `camp_selected_state_id` for existing country payloads. This avoids a world-state targeted decision and preserves a human player's Ledger selection.

The current France pool API is `is_france_camp_legacy_pool_state`, `is_france_north_africa_labor_pool_state`, `is_france_vichy_internment_pool_state`, `is_france_other_colonial_labor_pool_state`, and `is_france_core_fallback_pool_state`.

The current Italy pool API is `is_italy_libya_repression_pool_state`, `is_italy_east_africa_repression_pool_state`, `is_italy_balkan_occupation_pool_state`, `is_italy_colonial_project_pool_state`, and `is_italy_core_fallback_pool_state`. The project pool accepts Libya or East Africa. Italy also has the explicit `ita_authorize_homeland_emergency_detention` and `ita_expand_desert_transport_guard` actions.

The fixed colonial kits cannot inherit the generic restricted-method gate. They require `camp_rework_country_has_explicit_extreme_doctrine_route`, a matching capable stockpile, and a valid responsible country-kit target.

## Required references consulted

- Offline wiki core: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Offline wiki task pages: National focus modding, Country creation, State modding, and Autonomy state modding.
- Official vanilla documentation: `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `common/script_constants/documentation.md`, `common/decisions/_documentation.md`, and `common/ai_strategy/_documentation.md`.
- Accepted package: `README.md`, `package_index.md`, Parts 2, 4, 5, 6, and 7, plus `country_ai_matrix.md`, `country_decision_kits_matrix.md`, `decision_mission_matrix.md`, and `values_and_pressure_model.md`.
- Vanilla country, state, decision, focus, tag, tag-alias, autonomy, building, idea, and scripted-effect precedents.

Two engine constraints govern this tranche:

1. A targeted decision using `state_target = any` evaluates every world state and is explicitly documented as expensive. `any_controlled_state` is the bounded direct-control form, but it does **not** include states controlled by a subject. Subject-administered Raj, Burma, Malaya, and Congo targets therefore need the existing bounded country/subject arrays plus selected-state scripted-GUI dispatch; they must not be exposed by a world-scanning `state_target = any` workaround.
2. `add_autonomy_ratio` and `add_autonomy_score` execute in the subject country scope. `set_autonomy` executes in the overlord country scope. Every use must first prove the subject relationship. Vanilla precedents are `ENG_viceroy_reduce_autonomy_effect` in `common/scripted_effects/ENG_scripted_effects.txt` and `BEL_requisition_congolese_funds_decision` in `common/decisions/BEL.txt`. Ordinary camp pressure should use guarded `add_autonomy_ratio`; no ordinary decision should silently change a subject's autonomy tier with `set_autonomy`.

## Superseded preimplementation shared integration map

| Surface | Live evidence | Meaning for this tranche |
| --- | --- | --- |
| Country-route gate | `common/scripted_triggers/camp_repression_rework_triggers.txt` — `has_camp_country_specific_route`, `camp_rework_country_uses_generic_kit` | `ENG`, `USA`, `FRA`/`VIC`, `ITA`, and `BEL` are reserved for country-specific kits and excluded from the generic package. |
| Country pool dispatch | `common/scripted_triggers/camp_repression_rework_triggers.txt` — `camp_rework_state_matches_country_kit_pool` | All five countries reach their country pool helpers through one dispatcher. |
| Pool array builder | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_build_pool_arrays` | Builds bounded arrays from the responsible country's controlled states and then every subject's controlled states. This is the correct source for subject-administered GUI and AI selection. |
| AI state selector | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_select_ai_state` | Selects randomly from the first nonempty accepted pool tier. It is independent from player GUI selection. |
| Shared site registration | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_register_active_site` | Stores `genocide_responsible_country`, registers the state once, classifies its pool, and preserves responsibility across control changes. |
| Shared dismantlement | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_start_dismantlement`, `camp_rework_complete_dismantlement` | Freezes expansion, removes active buildings/modifiers/flags, unregisters the active state, retains evidence responsibility, and leaves a reformed legacy. Country kits must wrap this rather than duplicate it. |
| Enemy-control discovery | `common/on_actions/genocide_crisis_on_actions.txt` — `on_state_control_changed`; `common/scripted_effects/genocide_crisis_effects.txt` — `genocide_on_state_control_changed`, `genocide_try_discover_state_atrocity` | State control change can discover stored evidence and condemn the stored responsible country. Court, inspection, decolonisation, and postwar discoveries still need explicit bounded country-kit entry points. |
| Monthly host | `common/scripted_effects/genocide_crisis_effects.txt` — `genocide_register_constructed_concentration_camps`, `genocide_monthly_global_pulse` | Migration and the shared monthly camp pulse already run from the existing host; no country kit may add a new all-country daily/weekly/monthly iteration. |
| Country values | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_initialize_country_variables` | Only shared and other-major country values are initialised; none of the Part 2 colonial values is present. |
| Country display cache | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_copy_display_values` | Only shared display values and current other-major values are copied; all Part 6 colonial display bands are absent. |
| Idea dispatcher | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_refresh_country_specific_ideas` | Generic and other-major idea lifecycles may be present; the five colonial lifecycles are absent. |
| Monthly country bridge | `common/scripted_effects/camp_repression_rework_effects.txt` — `camp_rework_update_country_specific_monthly_bridges` | No colonial pressure/autonomy/accountability bridge is present. |
| Common caps and weights | `common/script_constants/camp_repression_rework_constants.txt` — `camp_rework_ai_cap`, `camp_rework_ai_weight` | Numeric country site caps and baseline AI weights exist, but no colonial country decisions consume the country weights. |
| Colonial tuning | `common/script_constants/camp_repression_rework_constants.txt` — `camp_rework_colonial` | Autonomy, burden, accountability, reform, and redress constants exist but are unused by the colonial kits. |
| State threshold | `common/script_constants/camp_repression_rework_constants.txt` — `camp_rework_state_threshold.low_infrastructure`; vanilla `common/buildings/00_buildings.txt` — `infrastructure.level_cap.state_max` | `low_infrastructure = 3`; project triggers use strict `<`, so levels 0-2 qualify against the vanilla maximum of 5. |
| Decisions | `common/decisions/camp_repression_generic_decisions.txt` — `generic_activate_detention_network` through `generic_reform_and_dismantlement` | Only generic decisions and missions exist. Country-specific powers are intentionally excluded by their route gate. |
| Ideas | `common/ideas/camp_repression_rework_ideas.txt` — `generic_detention_network_administration` through `generic_reformed_legacy` | Only generic lifecycle ideas exist in this file. |
| Localisation | `localisation/english/camp_repression_rework_l_english.yml` — generic decision/mission/idea keys | Only shared/generic decision, mission, and idea text exists. |
| Country assets | no listed ID resolves under `interface/`, `gfx/`, `common/`, or localisation | All 32 country-kit sprite IDs require registration and final assets. |

### Shared flags and fields every kit must use

These already exist and should remain the common lifecycle contract:

- Country flags: `camp_rework_dormant_route_available`, `camp_rework_inherited_network`, `camp_rework_democratic_emergency_authorized`, `camp_rework_inspection_active`, `camp_rework_reform_route_open`, `camp_rework_expansion_frozen`, `camp_rework_dismantlement_in_progress`, `camp_rework_redress_pending`, `camp_rework_reformed_legacy`, and `camp_rework_crisis_exposed`.
- State flags: `camp_rework_site_active`, `camp_rework_expanded_labor_site`, `camp_rework_site_reforming`, `camp_rework_site_dismantlement_in_progress`, `camp_rework_site_dismantled`, `genocide_site_discovered`, `camp_rework_liberated_evidence`, `genocide_evidence_destroyed`, `genocide_evidence_destroy_failed`, `camp_rework_security_pool`, `camp_rework_colonial_pool`, `camp_rework_france_camp_legacy`, `camp_rework_france_colonial_labor_pool`, `camp_rework_congo_concession_pool`, and `camp_rework_congo_transport_pool`.
- State responsibility/evidence fields: `genocide_responsible_country`, `camp_state_evidence_depth`, `camp_state_evidence_site_type`, `camp_state_resistance_accumulation`, `camp_state_observer_exposure`, and `camp_state_pool_type`.
- Shared policy values used by country bridges: `camp_policy_labor_output`, `camp_policy_coercive_control`, `camp_policy_population_loss`, `camp_policy_resistance_pressure`, `camp_policy_stability_damage`, `camp_policy_evidence`, `camp_policy_overstretch`, `camp_policy_visibility`, `camp_policy_tribunal`, `camp_policy_legitimacy`, `camp_policy_reform`, `camp_guard_burden`, `camp_rail_burden`, `camp_supply_burden`, and `camp_convoy_burden`.

The France/Vichy collaboration decision additionally requires the architecture-approved scope-valued field `camp_site_secondary_responsible_country`. It is specified in the field, cleanup, and collaborator-share sections of `core_script_architecture_handoff.md` but is not live. It must never overwrite primary `genocide_responsible_country`.

### Minimal new country lifecycle flags

The accepted specs fix focus-hook names but do not fix internal lifecycle flag names. To prevent five implementations from inventing incompatible names, use this minimal contract or update the tracker before implementation:

| Kit | Required lifecycle flags beyond the shared contract |
| --- | --- |
| U.K./Raj | `camp_rework_uk_raj_survey_complete`, `camp_rework_uk_raj_review_complete`, `camp_rework_uk_indian_release_terms_complete` |
| U.S.A. | `camp_rework_usa_authority_active`, `camp_rework_usa_court_review_complete`, `camp_rework_usa_authority_terminated`, `camp_rework_usa_redress_complete` |
| France/Vichy | `camp_rework_france_legacy_inspected`, `camp_rework_france_legacy_closed`, `camp_rework_france_colonial_review_open`, `camp_rework_france_post_liberation_reckoning_complete` |
| Italy | `camp_rework_italy_desert_administration_active`, `camp_rework_italy_security_battalions_active`, `camp_rework_italy_desert_camps_closed`, `camp_rework_italy_colonial_compensation_complete` |
| Belgium/Congo | `camp_rework_belgium_inspection_open`, `camp_rework_belgium_concessions_reformed`, `camp_rework_belgium_local_administration_recognized` |

Do not add flags that duplicate `has_active_camp_network`, an active mission check, a site registration state, or an idea stage. Clear the country-specific active/inspection flags on regime replacement, completed dismantlement, or loss of the subject relationship as applicable; retain completion/reform memory flags.

## Focus-hook result: flags only

There is no bespoke U.K., Raj, U.S., France, Vichy, Italy, Belgium, or Congo focus tree under the mod's `common/national_focus/`; the directory contains only the Chaos-specific zombie, Holy Realm, Soviet-collapse, Fury, Death, and Germany/Mengele trees. The vanilla focus definitions are `british_focus` in `uk.txt`, `indian_focus` in `india.txt`, `indian_focus_goe` in `india_goe.txt`, `usa_focus` in `usa.txt`, `french_focus` in `france.txt`, `vichy_french_focus` in `vichy_france.txt`, `italian_focus` in `italy.txt`, `belgium_focus` in `belgium.txt`, and `congo_focus` in `congo.txt`. This mod must not patch those vanilla files for this tranche.

Every Part 5 focus hook is therefore a **country flag interface**, not a focus definition:

- U.K.: `uk_focus_imperial_security_board`, `uk_focus_wartime_raj_logistics`, `uk_focus_indian_manpower_question`, `uk_focus_dominion_coordination`, `uk_focus_colonial_reform_committee`, `uk_focus_indian_self_government_settlement`.
- U.S.A.: `usa_focus_wartime_security_authority`, `usa_focus_home_front_security_review`, `usa_focus_supreme_court_review`, `usa_focus_civil_liberties_restoration`, `usa_focus_redress_commission`.
- France/Vichy: `fr_focus_legacy_review_commission`, `fr_focus_refugee_aid_networks`, `vichy_focus_national_revolution_security`, `vichy_focus_north_africa_labor_projects`, `vichy_focus_collaboration_records`, `free_france_focus_republican_reckoning`.
- Italy: `ita_focus_fourth_shore_security`, `ita_focus_libyan_road_works`, `ita_focus_colonial_security_corps`, `ita_focus_east_africa_emergency_labor`, `ita_focus_postwar_colonial_reform`, `ita_focus_abandon_colonial_camps`.
- Belgium: `bel_focus_congo_resource_office`, `bel_focus_exile_economy_congo`, `bel_focus_congo_transport_corridors`, `bel_focus_colonial_inspection_mandate`, `bel_focus_reform_concession_system`, `bel_focus_local_administration_recognition`.

Base decisions must remain usable through their accepted war/regime/threat/reform gates when these future-facing flags are unset. A flag may reveal early access, improve an outcome, or lower a cost; no base package may be permanently hidden behind a flag that no live focus sets. These flags need no focus localisation or focus icons in this tranche because no player-visible focus is being defined.

## Localisation contract

All visible keys belong in a reviewed UTF-8-with-BOM English file, preferably the existing `localisation/english/camp_repression_rework_l_english.yml`. For every decision listed below, the mandatory keys are the exact decision ID, `<id>_desc`, and `<id>_effect_tt`. For every mission, the mandatory keys are the exact mission ID, `<id>_desc`, `<id>_success_tt`, and `<id>_failure_tt`. For every idea, the mandatory keys are the exact idea ID and `<id>_desc`. This notation is exhaustive: it expands mechanically for every ID in the per-kit inventories and does not authorize omitting any pair or mission outcome.

Additional cross-surface keys required by the subject and GUI contract are:

- Autonomy sources: `camp_rework_uk_raj_autonomy_pressure`, `camp_rework_uk_raj_autonomy_concession`, `camp_rework_france_colonial_autonomy_pressure`, `camp_rework_france_colonial_autonomy_concession`, `camp_rework_italy_colonial_autonomy_pressure`, `camp_rework_italy_colonial_autonomy_concession`, `camp_rework_bel_congo_autonomy_pressure`, `camp_rework_bel_congo_autonomy_concession`.
- Country panel names: `camp_rework_country_panel_uk_raj`, `camp_rework_country_panel_usa`, `camp_rework_country_panel_france`, `camp_rework_country_panel_vichy`, `camp_rework_country_panel_italy`, `camp_rework_country_panel_belgium_congo`.
- Every country value listed below requires `camp_rework_value_<value>` and `camp_rework_value_<value>_tt`.
- Every Part 6 display variable listed below requires `camp_rework_display_<display-variable-without-display_>` and the corresponding `_tt` key.
- Every country discovery image requires a one-shot report/news event with its own event title, description, and option localisation before the image can be considered wired. The accepted specs do not fix those event IDs; they must be registered in the tracker before implementation rather than silently invented in gameplay.

Player text must describe the world state and consequence, not implementation history, formulas, hidden AI weights, or protected-class selectors.

## U.K. and British Raj kit

### Required identifier inventory

Country values, all absent from the live initialiser and monthly bridge:

- `imperial_detention_reach`
- `raj_labor_burden`
- `dominion_control_pressure`
- `indian_autonomy_resistance`
- `colonial_legitimacy_damage`
- `imperial_manpower_pressure`

Part 6 display values:

- `display_raj_labor_burden_band`
- `display_indian_autonomy_resistance_band`

| Decision ID | Mandatory localisation keys | Required role |
| --- | --- | --- |
| `uk_survey_raj_emergency_detention` | ID, `_desc`, `_effect_tt` | Dormant survey; war plus a Raj/Indian Ocean pool; sets `camp_rework_uk_raj_survey_complete`. |
| `uk_activate_raj_emergency_detention` | ID, `_desc`, `_effect_tt` | First registered Raj detention site; Britain remains responsible; subject/local owner receives burden. |
| `uk_route_colonial_labor_to_military_construction` | ID, `_desc`, `_effect_tt` | Selected-state works route using trains, trucks, support equipment, and a civilian-factory burden. |
| `uk_expand_raj_detention_districts` | ID, `_desc`, `_effect_tt` | Expands an existing site and increases evidence, local burden, and future discovery severity. |
| `uk_demand_indian_manpower_levy` | ID, `_desc`, `_effect_tt` | Wartime manpower pressure with major Raj burden/autonomy backlash. |
| `uk_tighten_dominion_security_coordination` | ID, `_desc`, `_effect_tt` | Timed dominion-control/coordination effect; it must not silently alter autonomy tier. |
| `uk_allocate_additional_colonial_guards` | ID, `_desc`, `_effect_tt` | Shared guard relief wrapped with colonial burden and manpower costs. |
| `uk_release_political_prisoners_for_negotiations` | ID, `_desc`, `_effect_tt` | Reduces burden/reach and opens the negotiated reform path. |
| `uk_reform_colonial_labor_administration` | ID, `_desc`, `_effect_tt` | Freezes expansion and begins the accepted 270-day reform chain. |
| `uk_dismantle_raj_detention_network` | ID, `_desc`, `_effect_tt` | Completes shared site dismantlement and swaps U.K./Raj ideas. |

| Mission ID | Days | Mandatory localisation keys | Success/failure contract |
| --- | ---: | --- | --- |
| `uk_hold_raj_security_line` | 150 | ID, `_desc`, `_success_tt`, `_failure_tt` | Supplied/garrisoned Raj line lowers immediate unrest; failure raises autonomy resistance and overextension. |
| `uk_complete_raj_military_works` | 180 | ID, `_desc`, `_success_tt`, `_failure_tt` | Maintained equipment/construction burden completes a bounded state improvement; failure still records rail, deaths, and evidence pressure. |
| `uk_postwar_raj_review` | 365 | ID, `_desc`, `_success_tt`, `_failure_tt` | Peace/falling war pressure plus reform authority produces reformed legacy; failure opens colonial reckoning. |
| `uk_negotiate_indian_release_terms` | 270 | ID, `_desc`, `_success_tt`, `_failure_tt` | No expansion plus controlled autonomy pressure reduces burden and sets `camp_rework_uk_indian_release_terms_complete`; failure raises India unrest. |

| Idea ID | Owner | Mandatory localisation keys | Lifecycle |
| --- | --- | --- | --- |
| `uk_imperial_detention_legacy` | U.K. | ID, `_desc` | Dormant discoverable marker; replaced on activation or successful reform. |
| `uk_imperial_detention_administration` | U.K. | ID, `_desc` | Active modest control/construction administration. |
| `uk_overextended_imperial_detention` | U.K. | ID, `_desc` | High reach/unrest/transport strain; removed only by reduction or dismantlement. |
| `raj_colonial_labor_burden` | Raj/India subject or distinct local owner | ID, `_desc` | Local population, resistance, compliance, and autonomy burden. Do not apply it to Britain merely because Britain directly owns a state; use state burden there. |
| `uk_imperial_reform_credit` | U.K. | ID, `_desc` | Successful pre-severe-discovery dismantlement memory. |
| `uk_colonial_reckoning_pressure` | U.K. | ID, `_desc` | Discovery, failed review, or decolonisation exposure; removed by completed settlement. |

Required assets:

- `GFX_decision_uk_raj_detention`
- `GFX_decision_uk_colonial_labor_works`
- `GFX_idea_uk_imperial_detention_administration`
- `GFX_idea_raj_colonial_labor_burden`
- `GFX_report_event_raj_detention_discovery`
- `GFX_news_event_colonial_reckoning`

### Exact state-pool logic

The live U.K. pool symbols are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.

1. `is_uk_raj_detention_pool_state` requires both:
   - Raj identity: core of `RAJ`, `PAK`, or `BAN`, **or** owner/controller with `original_tag = RAJ`; and
   - British legal control: controlled by Britain, or controlled by a subject of Britain.
2. `is_uk_indian_ocean_security_pool_state` requires a core of `BRM`, `SRL`, or `MAL` plus British direct control or controller-subject-of-Britain.
3. `is_uk_colonial_emergency_pool_state` requires a non-British-core state under British direct or subject control and at least one of resistance, coastal status, or `camp_rework_security_pool`.
4. `is_uk_core_fallback_pool_state` requires an owned-and-controlled British core, `original_tag = ENG`, war, `surrender_progress > 0.45`, and no Raj, Indian Ocean, or colonial emergency candidate in either British-controlled states or any subject's controlled states.

Vanilla state coverage relevant to the first two pools:

- `RAJ`-owned 1936 states: `423-445`, `787`, `982-992`, and `1012`. The `OWNER/CONTROLLER original_tag = RAJ` branch now includes the princely/central states that the earlier core-only implementation missed.
- `RAJ` cores: `320`, `321`, `429`, `430`, `431`, `434`, `439`, `443`, `733`, `985`, `986`, `988`; `PAK` cores: `430`, `440`, `442-445`, `787`, `987`, `988`, `1012`; `BAN` core: `430`.
- `BRM` cores: `288`, `640`, `993-999`; `SRL` core: `422`; `MAL` cores: `333`, `336`, `1021`, `1023`, `1024`, `1059-1065`.

The control gate prevents French India (`320`) and Goa (`321`) from qualifying until Britain or a British subject actually controls them. The owner/controller-original-Raj clause is still broader than the geographical description: if the Raj conquers and controls a non-Indian state, that state qualifies. The implementation owner must choose whether this subject-administration behavior is intentional or replace it with a reviewed geographic state set; it cannot be silently treated as an exact India-only pool.

Vanilla subject setup is DLC-sensitive. Britain makes `MAL` an integrated puppet, `RAJ` and `BRM` colonies when Together for Victory or Man the Guns is active, but the no-DLC branch puppets `MAL` and `RAJ` and does not puppet `BRM` (the diplomacy `set_autonomy`/`puppet` block in `history/countries/ENG - Britain.txt`). Burma therefore disappears from the subject-administered pool in that configuration unless Britain directly controls it. This is a real compatibility assumption, not a reason to world-scan.

### Subject, population, and autonomy effects

- The target state owner records population loss through the shared Deaths adapter. Britain remains `genocide_responsible_country` for every British-created site.
- If the target controller or owner is a British subject, apply `raj_colonial_labor_burden` to that subject and update `raj_labor_burden`/`indian_autonomy_resistance` in Britain for display and decision gates.
- Use `constant:camp_rework_colonial.local_burden_minor` (`3`) for activation, one works cycle, or guard allocation; use `.local_burden_major` (`8`) for expanded districts or the manpower levy.
- In the subject scope, activation/works backlash uses `add_autonomy_ratio = +0.015` with `camp_rework_uk_raj_autonomy_pressure`; expanded districts/manpower levy uses `+0.035`. This raises freedom pressure, matching the accepted autonomy-resistance consequence.
- Prisoner release/reform may use `+0.015`, and negotiated release/dismantlement may use `+0.035`, with `camp_rework_uk_raj_autonomy_concession`, while subtracting the corresponding burden values. The identical engine direction has different political meaning and therefore needs a distinct localisation source.
- `uk_tighten_dominion_security_coordination` may alter `dominion_control_pressure` and a timed idea. The accepted package does not specify whether it should raise or lower engine autonomy, so it must not apply an unreviewed autonomy delta.
- Never call `set_autonomy` for the levy, coordination, release, or reform decisions. A future self-government tier change requires a separately accepted effect executed in Britain scope.

### Lifecycle and discovery

1. Dormant: a valid Raj/Indian Ocean pool adds `uk_imperial_detention_legacy`; survey does not register a death-producing site.
2. Active: activation registers a selected detention site, records Britain as responsible, adds the U.K. administration idea, and adds subject/local burden.
3. Expanded/project: works and district decisions use the selected-state dispatcher, existing state labor/sabotage modifiers, and shared Deaths/evidence fields. Subject states are selected from bounded arrays, not `state_target = any`.
4. Reform: release or `uk_reform_colonial_labor_administration` sets `camp_rework_expansion_frozen`, `camp_rework_reform_route_open`, and `camp_rework_inspection_active`; active expansion decisions hide.
5. Dismantlement: the review/release chain calls the shared start/complete effects for every registered British site. It removes active output and burden, retains evidence, and awards `uk_imperial_reform_credit` only before severe discovery.
6. Discovery: shared enemy-control discovery covers captured states. Separate one-shot triggers are required for high India autonomy pressure, refused postwar review, and Raj/India separation while British-responsible sites remain. They add `uk_colonial_reckoning_pressure` and unlock inquiry/compensation instead of recurring leak events.

The accepted cap is one security mission plus one reform-or-construction mission. The live global `max_concurrent_projects = 1` cannot express that two-lane cap; use independent `has_decision`/mission-family checks. Do not make the global cap block the allowed second lane.

### AI contract

Accepted conditional weights:

| Condition | Expansion | Reform |
| --- | ---: | ---: |
| Peace, stable empire | 0 | 20 |
| World war, Raj exists, low India pressure | 25 | 5 |
| World war, high India unrest or Burma threat | 45 | 10 |
| Democratic postwar U.K. | 0 | 80 |
| Discovery, condemnation, or decolonisation pressure | 0 | 100 |
| Non-democratic high-chaos empire | 55 | 5 |

The live baseline constants are activation `25`, expansion `18`, reform `80`, with a hard active-site cap of `4`. The `4` is the exact current numeric cap, but Part 5 separately requires a "small" pre-1939 network and does not assign that phrase a number. A date-sensitive pre-1939 cap still needs an explicit owner decision; do not claim that the unconditional cap of four proves that requirement. Normal U.K. AI must never use radicalized escalation or core fallback, and it must stop expansion on discovery/postwar reform.

### Part 7 scenario expectation

With Britain at war and a Raj/India pool active, the Raj decisions appear; a selected direct or subject-administered state registers correctly; Britain gains only limited control/construction benefit; the target state's owner records Deaths; Raj/India receives burden and autonomy pressure; Britain remains responsible; AI uses the route lightly; postwar review, release, and dismantlement remove the active network without deleting evidence. The scenario fails if a British core is chosen while a higher pool exists, a subject state cannot be selected, Britain receives the Raj burden idea instead of the subject/local state burden, or an unset focus-hook flag permanently hides the base route.

## U.S.A. kit

### Required identifier inventory

Country values:

- `wartime_security_reach`
- `civil_liberties_damage`
- `court_challenge_pressure`
- `democratic_legitimacy_damage`
- `relocation_population_disruption`
- `redress_pressure`

Part 6 display values:

- `display_civil_liberties_damage_band`
- `display_court_challenge_pressure_band`

| Decision ID | Mandatory localisation keys | Required role |
| --- | --- | --- |
| `usa_authorize_emergency_relocation_zones` | ID, `_desc`, `_effect_tt` | War/threat emergency authority; sets `camp_rework_usa_authority_active` and `camp_rework_democratic_emergency_authorized`. |
| `usa_expand_interior_security_camps` | ID, `_desc`, `_effect_tt` | Adds limited site capacity in a valid interior/security pool with strong legitimacy cost. |
| `usa_assign_detainee_labor_to_local_works` | ID, `_desc`, `_effect_tt` | Small selected-state repair/infrastructure support; not an economic loop. |
| `usa_strengthen_wartime_review_boards` | ID, `_desc`, `_effect_tt` | Temporary breakdown/court relief that leaves the authority active. |
| `usa_allow_court_review` | ID, `_desc`, `_effect_tt` | Opens the 180-day legal review and freezes expansion while active. |
| `usa_release_detainees_under_supervision` | ID, `_desc`, `_effect_tt` | Reduces disruption and reach at the cost of the security benefit. |
| `usa_terminate_relocation_authority` | ID, `_desc`, `_effect_tt` | Starts closure, unregisters active states on completion, sets `camp_rework_usa_authority_terminated`, and opens redress. |
| `usa_establish_redress_commission` | ID, `_desc`, `_effect_tt` | Starts the long redress route after termination or exposure. |

| Mission ID | Days | Mandatory localisation keys | Success/failure contract |
| --- | ---: | --- | --- |
| `usa_court_review_period` | 180 | ID, `_desc`, `_success_tt`, `_failure_tt` | No expansion plus sufficient democratic stability enables cheaper termination; failure intensifies civil-liberties damage. |
| `usa_security_authority_sunset` | 270 | ID, `_desc`, `_success_tt`, `_failure_tt` | Falling threat without expansion reveals/presses termination; ignored sunset raises court and legitimacy damage. |
| `usa_redress_commission_work` | 365 | ID, `_desc`, `_success_tt`, `_failure_tt` | Paid redress without reactivation grants reform credit; failure retains redress and exposure pressure. |

| Idea ID | Owner | Mandatory localisation keys | Lifecycle |
| --- | --- | --- | --- |
| `usa_wartime_security_authority` | U.S.A. | ID, `_desc` | Active emergency authority; replaced by contested stage or termination. |
| `usa_contested_relocation_authority` | U.S.A. | ID, `_desc` | Court challenge/overextension stage. |
| `usa_civil_liberties_damage` | U.S.A. | ID, `_desc` | Sustained expansion and democratic legitimacy cost. |
| `usa_relocation_population_disruption` | U.S.A. plus state burden representation | ID, `_desc` | National memory/display counterpart; local damage remains on selected states through state values/modifiers. |
| `usa_redress_pressure` | U.S.A. | ID, `_desc` | Termination/exposure budget and political burden. |
| `usa_reform_credit` | U.S.A. | ID, `_desc` | Successful termination and redress memory. |

Required assets:

- `GFX_decision_usa_emergency_relocation`
- `GFX_decision_usa_court_review`
- `GFX_decision_usa_redress_commission`
- `GFX_idea_usa_wartime_security_authority`
- `GFX_idea_usa_civil_liberties_damage`
- `GFX_report_event_usa_relocation_review`

### Exact state-pool logic

The live U.S. pool symbols are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.

1. `is_usa_wartime_security_zone_state` requires U.S. ownership and control and one exact state ID: `377` Arizona, `378` California, `379` Nevada, `380` Utah, `385` Oregon, `386` Washington, `387` Idaho, `463` Alaska, `629` Hawaii, or `685` Panamá Canal.
2. `is_usa_overseas_security_pool_state` requires U.S. control, non-U.S. core status, and either U.S. ownership or occupied-noncore classification.
3. `is_usa_interior_relocation_site_state` requires U.S. ownership and control, a U.S. core, non-coastal status, and exclusion from the exact security-zone list.
4. `is_usa_core_emergency_fallback_state` requires an owned-and-controlled U.S. core, `original_tag = USA`, war, either `surrender_progress > 0.45` or Chaos tier 4/5, and no security-zone, overseas-security, or interior-relocation state still controlled by the U.S.

The accepted description says interior states should have low combat risk and available infrastructure. The live interior trigger checks neither front/enemy proximity nor infrastructure. This is an unresolved semantic gap: add a reviewed low-combat/supply condition or explicitly accept the broader non-coastal-core pool. Do not describe the current trigger as already enforcing those constraints.

Alaska, Hawaii, and Panamá Canal can satisfy both the named security-zone trigger and the non-core overseas trigger. The array builder visits a state once and classifies it once, so this logical overlap does not currently duplicate a row, but action-specific scoring must prefer the named security-zone role. The pool remains geographic/military; no decision or localisation may ask the player to select ethnicity, religion, nationality, or another protected class.

Direct U.S. state actions can use `state_target = any_controlled_state` plus `target_root_trigger`/`target_trigger`. The ledger selected-state path should still be the canonical action dispatcher so AI and GUI use the same trigger. No subject-autonomy bridge is required for this kit.

### Population, lifecycle, and legal discovery

- The selected state's owner records population loss; U.S.A. remains `genocide_responsible_country`.
- Activation adds small `wartime_security_reach`, `civil_liberties_damage`, `court_challenge_pressure`, `democratic_legitimacy_damage`, and disruption. Expansion and labor works use the major shared country-value/burden bands while keeping labor output deliberately small.
- `usa_strengthen_wartime_review_boards` may temporarily reduce `court_challenge_pressure`; it must not erase accumulated evidence or civil-liberties memory.
- Court review sets `camp_rework_inspection_active`, `camp_rework_reform_route_open`, and `camp_rework_expansion_frozen`. A successful review sets `camp_rework_usa_court_review_complete` and enables lower-cost termination.
- Termination calls shared dismantlement for every U.S.-responsible active state, removes state disruption, clears the active-authority flag, sets `camp_rework_usa_authority_terminated`, and adds `camp_rework_redress_pending`/`usa_redress_pressure`.
- Redress completion removes redress pressure, sets `camp_rework_usa_redress_complete`, and adds `usa_reform_credit`; it does not delete evidence history.
- Shared enemy-control discovery covers overseas/occupied sites. Explicit one-shot discovery is still required for failed court review, postwar inquiry, and authority remaining active after threat falls. Domestic legal exposure should intensify national ideas and unlock reform, not emit recurring leak popups or automatically use the severe battlefield-news route.

Activation must require at least one of war plus accepted homeland/Pacific/sabotage pressure, or extreme high chaos. Peacetime with no high chaos hides the category route. `usa_focus_wartime_security_authority` may reveal it earlier under war pressure but must not bypass the threat contract.

### AI contract

| Condition | Activation | Expansion | Reform |
| --- | ---: | ---: | ---: |
| Peacetime, no high chaos | 0 | 0 | 0 |
| War without homeland/Pacific pressure | 5 | 0 | 10 |
| Pacific pressure or homeland raids | 25 | 10 | 5 |
| Homeland invasion or extreme high chaos | 40 | 20 | 5 |
| Court review active | 0 | 0 | 65 |
| Postwar or threat below threshold | 0 | 0 | 100 |

The live baselines are activation `6`, expansion `2`, reform `90`, and the active-site cap is `3`. Those baselines must be modified to the table above rather than used as unconditional behavior. Democratic U.S. AI has no radicalized route, no economy-optimization loop, no core fallback outside the accepted emergency, and must terminate after legal pressure or threat decline.

### Part 7 scenario expectation

With U.S.A. at war and a valid Pacific/homeland threat, authorization can appear, bounded geographic states can be selected, the authority provides only limited security/local works, civil-liberties and court pressure visibly rise, court review can freeze expansion, termination unregisters sites, and redress converts the remaining pressure into reform credit. AI should rarely activate and should stop when the threat falls. The scenario fails if peacetime authorization appears without high chaos, the player selects a protected class, labor becomes a profitable repeat loop, court review does not block expansion, termination deletes evidence, or AI remains active postwar.

## France, Vichy, and North Africa kit

### Required identifier inventory

Country values:

- `french_camp_legacy`
- `vichy_collaboration_reach`
- `north_africa_labor_burden`
- `refugee_pressure`
- `free_french_reform_credit`

Part 6 display values:

- `display_vichy_collaboration_reach_band`
- `display_north_africa_labor_burden_band`

| Decision ID | Mandatory localisation keys | Required role |
| --- | --- | --- |
| `fr_inspect_camp_legacy` | ID, `_desc`, `_effect_tt` | Democratic/Free France inspection of dormant legacy; no forced activation prerequisite. |
| `fr_close_camp_legacy_sites` | ID, `_desc`, `_effect_tt` | Begins the 270-day closure path for dormant or active legacy states. |
| `fr_expand_vichy_internment_administration` | ID, `_desc`, `_effect_tt` | Vichy/authoritarian mainland collaboration activation. |
| `fr_route_north_africa_labor_to_rail_projects` | ID, `_desc`, `_effect_tt` | Bounded North Africa rail/infrastructure/fort/supply project. |
| `fr_collaboration_transfer_records` | ID, `_desc`, `_effect_tt` | Explicit Vichy/German linked record route using secondary responsibility without replacing Vichy responsibility. |
| `fr_suppress_refugee_and_rescue_networks` | ID, `_desc`, `_effect_tt` | Short visibility/resistance relief with later evidence/refugee cost. |
| `fr_open_colonial_labor_review` | ID, `_desc`, `_effect_tt` | Democratic, Free, regime-change, or discovery reform opener for colonial sites. |
| `fr_dismantle_north_africa_labor_network` | ID, `_desc`, `_effect_tt` | Review-complete closure, burden removal, and reform credit. |

| Mission ID | Days | Mandatory localisation keys | Success/failure contract |
| --- | ---: | --- | --- |
| `fr_gurs_legacy_review` | 180 | ID, `_desc`, `_success_tt`, `_failure_tt` | No Vichy expansion plus maintained reform converts dormant to inspected legacy; failure leaves discoverable evidence. |
| `fr_north_africa_rail_labor_project` | 180 | ID, `_desc`, `_success_tt`, `_failure_tt` | Maintained train/convoy capacity and control completes a selected-state project; failure adds deaths/resistance/evidence without full output. |
| `fr_refugee_pressure_response` | 150 | ID, `_desc`, `_success_tt`, `_failure_tt` | Aid/reform lowers refugee pressure; suppression/inaction raises visibility and resistance. |
| `fr_post_liberation_reckoning` | 365 | ID, `_desc`, `_success_tt`, `_failure_tt` | Democratic/Free control plus reform cost removes collaboration burden; failure retains Vichy legacy and discovery risk. |

| Idea ID | Owner | Mandatory localisation keys | Lifecycle |
| --- | --- | --- | --- |
| `fr_camp_legacy` | France/Vichy | ID, `_desc` | Dormant inheritance; replaced by inspected legacy, Vichy administration, or reform credit. |
| `vichy_collaboration_repression` | Vichy/authoritarian France | ID, `_desc` | Active collaboration route; removed after liberation/reform. |
| `fr_north_africa_labor_burden` | Responsible France plus distinct local subject/owner where applicable | ID, `_desc` | Colonial construction burden with state damage/unrest. |
| `fr_refugee_pressure` | France, Vichy, or Free France | ID, `_desc` | Suppression/discovery/failed-review pressure. |
| `free_france_reform_credit` | Free/democratic France | ID, `_desc` | Successful inspection and closure memory. |
| `fr_post_liberation_reckoning` | France | ID, `_desc` | Legal/political cleanup after liberation or discovery. |

Required assets:

- `GFX_decision_fr_camp_legacy_review`
- `GFX_decision_vichy_internment_admin`
- `GFX_decision_fr_north_africa_labor`
- `GFX_idea_fr_camp_legacy`
- `GFX_idea_vichy_collaboration_repression`
- `GFX_report_event_fr_liberated_camp_records`
- `GFX_news_event_vichy_reckoning`

### Exact state-pool logic and identifier mismatch

The live France/Vichy pool symbols are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.

1. Live `is_france_camp_legacy_pool_state` requires French direct control plus `camp_rework_france_camp_legacy` or exact state `21` Bouches-du-Rhône, `31` Midi Pyrenees, or `32` Alpes.
2. `is_france_north_africa_labor_pool_state` requires a core of `ALG`, `MOR`, or `TUN` plus French direct control or a controller subject of France. The vanilla core set is Algeria `459`, `460`, `513`, `514`; Morocco `290`, `461`, `462`, `783`; Tunisia `458`, `665`.
3. Live `is_france_vichy_internment_pool_state` requires French/Vichy direct control and either the legacy pool or the North Africa pool.
4. Live `is_france_other_colonial_labor_pool_state` requires a non-French-core, non-North-Africa state under direct or subject control, plus resistance or `camp_rework_france_colonial_labor_pool`.
5. `is_france_core_fallback_pool_state` requires a French owned-and-controlled core, France/Vichy identity, desperate-war context (`surrender_progress > 0.65`, stability below `0.35`, or Chaos tier 5), and no directly controlled legacy, North Africa, or other-colonial candidate.

The accepted identifiers are `is_france_camp_legacy_state`, `is_vichy_collaboration_pool_state`, and `is_france_colonial_labor_pool_state`; the live names add or change words. Decisions, GUI, audits, and the tracker must converge on one exact API. Prefer the accepted names or provide documented aliases; do not leave two parallel implementations.

The earlier hardcoded state `34` has been removed from the live trigger. That correction is required: the `id = 34`, `owner = BEL`, and `add_core_of = BEL` entries in `history/states/34-Wallonie.txt` identify Wallonia, not a French camp-legacy state.

Two live gaps remain:

- The core-fallback absence checks only France's directly controlled states. A subject-administered North Africa or other-colonial pool does not block a French core fallback. Mirror the U.K. subject-pool exclusion before exposing this trigger to decisions or AI.
- The pool trigger itself does not impose the accepted authoritarian/collaboration restriction on core fallback. That restriction must exist in the decision/action route gate; democratic or Free France must not receive expansion through this fallback.

`VIC` is a valid vanilla country-tag alias, not a static tag. The `VIC` block in `common/country_tag_aliases/tag_aliases.txt` maps it to `original_tag = FRA` with `vichy_french_focus`. `original_tag = FRA` correctly keeps successor French scopes in the package, while Vichy-only expansion must additionally test `tag = VIC`, the Vichy focus tree, or another explicit accepted authoritarian route. A mere original-tag test is not a Vichy discriminator.

### Responsibility, subject, and lifecycle effects

- Vichy-created sites store Vichy as primary `genocide_responsible_country`. `fr_collaboration_transfer_records` may store Germany in `camp_site_secondary_responsible_country` and apply a constant-defined collaborator share. It must not rewrite the primary pointer or make Germany responsible for unrelated Vichy sites.
- Democratic/Free France can inherit and reform evidence without becoming the historical responsible country. Cleanup authority and responsibility are separate scopes.
- Directly administered North African states use state burden, Deaths, resistance, and refugee values. If a North African/colonial controller or owner is a French subject, give it the local burden representation and apply autonomy pressure in that subject scope: `+0.015` for a standard project and `+0.035` for suppression/major expansion, using `camp_rework_france_colonial_autonomy_pressure`.
- Review/dismantlement lowers burden by `3`/`8`; a subject-facing reform concession can add `+0.015`/`+0.035` autonomy freedom with `camp_rework_france_colonial_autonomy_concession`. No ordinary action changes the subject tier.
- Inspection of dormant legacy adds `fr_camp_legacy`/`french_camp_legacy` and `camp_rework_france_legacy_inspected` but must not register a death-producing site.
- Vichy activation registers the selected state and updates collaboration reach, evidence, resistance, and tribunal pressure. North Africa projects use shared state modifiers and Deaths rather than direct population manipulation.
- Democratic/Free inspection or regime change sets the shared freeze/reform/inspection flags and `camp_rework_france_colonial_review_open`. Successful closure calls shared dismantlement, sets the legacy-closed/reckoning-complete flags, removes collaboration/burden ideas, and awards `free_france_reform_credit` when timing permits.
- Shared enemy-control discovery covers liberation/capture. Explicit one-shot entry points are still required for Free France post-liberation review and postwar tribunal threshold. They create refugee/reckoning pressure and reform decisions, not repeated leaks.

### AI contract

| Condition | Expansion | Reform |
| --- | ---: | ---: |
| Democratic France before collapse | 0 | 30 |
| Free France controls legacy/colonial states | 0 | 70 |
| Vichy, German aligned, at war | 45 | 5 |
| Vichy, high resistance or German pressure | 60 | 0 |
| Regime changed away from Vichy | 0 | 90 |
| High condemnation or enemy near sites | 0 | 60 |

The live baselines are Vichy expansion `42`, reform `75`, and active-site cap `5`. Democratic and Free France must have an absolute expansion block; Vichy remains below Germany scale; no extermination route exists without a separately gated extreme generic doctrine. Evidence destruction is limited to an authoritarian collapse route near enemies and undiscovered evidence.

### Part 7 scenario expectation

With Vichy controlling North Africa on an authoritarian route, Vichy expansion and North Africa labor decisions appear, projects stay in valid territorial pools, local owners record Deaths, and Vichy remains primarily responsible even when a reviewed German link exists. After liberation or regime change, democratic/Free France can inspect and dismantle without first activating dormant sites, remove Vichy/colonial burdens, and complete post-liberation reckoning. The scenario fails if democratic France can expand, Wallonia appears as French legacy, German responsibility overwrites Vichy, subject North Africa permits French core fallback, or Free France must create an active camp before it can close inherited legacy.

## Italy and Libya kit

### Required identifier inventory

Country values:

- `colonial_repression_reach`
- `desert_camp_burden`
- `libyan_resistance_pressure`
- `colonial_logistics_output`
- `postwar_colonial_claim_damage`

Part 6 display value:

- `display_desert_camp_burden_band`

| Decision ID | Mandatory localisation keys | Required role |
| --- | --- | --- |
| `ita_reopen_desert_camp_administration` | ID, `_desc`, `_effect_tt` | Fascist/authoritarian activation in Libya or East Africa. |
| `ita_redirect_colonial_labor_to_roads_and_forts` | ID, `_desc`, `_effect_tt` | Selected colonial roads, forts, port, infrastructure, or supply project. |
| `ita_force_settlement_of_rebel_districts` | ID, `_desc`, `_effect_tt` | High-resistance short-term control with major population/evidence/revolt cost. |
| `ita_raise_colonial_security_battalions` | ID, `_desc`, `_effect_tt` | Accepted local-security/garrison-modifier route; sets `camp_rework_italy_security_battalions_active`. |
| `ita_expand_desert_transport_guard` | ID, `_desc`, `_effect_tt` | Truck/fuel/command-power overextension relief with fuel/manpower burden. |
| `ita_close_desert_camps` | ID, `_desc`, `_effect_tt` | Regime-change, reform, discovery, or defeat closure opener. |
| `ita_compensate_local_communities` | ID, `_desc`, `_effect_tt` | Closure/discovery aftermath that lowers colonial-claim damage. |

| Mission ID | Days | Mandatory localisation keys | Success/failure contract |
| --- | ---: | --- | --- |
| `ita_desert_road_labor_project` | 180 | ID, `_desc`, `_success_tt`, `_failure_tt` | Control plus truck/convoy/supply capacity produces bounded infrastructure/supply work; failure adds local damage/evidence without output. |
| `ita_colonial_security_sweep` | 150 | ID, `_desc`, `_success_tt`, `_failure_tt` | Supplied local security lowers immediate resistance; failure or completion still adds long-run resentment/evidence as specified. |
| `ita_desert_camp_closure` | 270 | ID, `_desc`, `_success_tt`, `_failure_tt` | No expansion, site control, and reform payment closes sites; failure retains burden and revolt pressure. |
| `ita_postwar_colonial_compensation` | 365 | ID, `_desc`, `_success_tt`, `_failure_tt` | Peace/regime change without repression lowers claim damage; failure retains foreign/local pressure. |

| Idea ID | Owner | Mandatory localisation keys | Lifecycle |
| --- | --- | --- | --- |
| `ita_colonial_repression_legacy` | Italy | ID, `_desc` | Dormant/first-route marker. |
| `ita_desert_camp_administration` | Italy | ID, `_desc` | Active colonial logistics/control with manpower/stability burden. |
| `ita_libyan_resistance_pressure` | Italy or distinct local owner, plus state pressure | ID, `_desc` | Forced settlement/security resentment and discovery pressure. |
| `ita_colonial_logistics_output` | Italy | ID, `_desc` | Timed road/fort/logistics output; ends on closure. |
| `ita_postwar_colonial_claim_damage` | Italy | ID, `_desc` | Discovery, defeat, or failed-closure liability. |
| `ita_colonial_reform_credit` | Italy | ID, `_desc` | Successful pre-severe-discovery closure memory. |

Required assets:

- `GFX_decision_ita_desert_camp_admin`
- `GFX_decision_ita_colonial_road_labor`
- `GFX_decision_ita_camp_closure`
- `GFX_idea_ita_desert_camp_administration`
- `GFX_idea_ita_libyan_resistance_pressure`
- `GFX_report_event_libyan_camp_discovery`

### Exact state-pool logic and project gap

The live Italy pool symbols are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.

1. `is_italy_libya_repression_pool_state` requires Italian direct control and a `LBA` core. Vanilla Libya cores are `273`, `448-451`, `661-663`.
2. `is_italy_east_africa_repression_pool_state` requires Italian direct control and a core of `ETH`, `ERI`, or `SOM`. This includes Ethiopia `271`, `835-843`, `908`; Eritrea `550`; and Somali cores `268`, `269`, `559`, `835`, `836`, `844`, `903`, subject to actual Italian control.
3. `is_italy_balkan_occupation_pool_state` requires Italian direct control, non-Italian-core status, a core of `YUG`, `GRE`, or `ALB`, Italian war, and Chaos tier 3, 4, or 5.
4. `is_italy_core_fallback_pool_state` requires an Italian owned-and-controlled core, `original_tag = ITA`, desperate-war context, and no directly controlled Libya, East Africa, or Balkan candidate.
5. Live `is_italy_colonial_project_pool_state` requires the **Libya pool only**, plus resistance, coastal status, or infrastructure below `3`.

The accepted project API is `is_italy_colonial_logistics_project_state`; the live helper uses `is_italy_colonial_project_pool_state`. As with France, converge on the accepted name or a documented alias.

More importantly, the project trigger currently excludes every East Africa state unless it is also a Libya core, and therefore cannot satisfy the Part 5 East Africa roads/supply route or `ita_focus_east_africa_emergency_labor`. The reviewed project base must include Libya and East Africa; Balkan targets may join only through the already accepted war/chaos gate. Italian cores must never be exposed through colonial roads, settlement, security-battalion, or project decisions. The separate punitive core-fallback helper may only be used by a visibly distinct desperate-emergency action.

All colonial pool helpers currently require Italian **direct** control. If Libya/East Africa is released as an Italian subject, expansion hides. That is internally consistent with the present trigger but must be paired with cleanup/accountability remaining visible for existing Italian-responsible evidence. Do not broaden to subject control without also adding a subject/local burden and autonomy contract.

### Population, subject, lifecycle, and discovery effects

- Target-state owners record Deaths; Italy remains `genocide_responsible_country`.
- Activation adds minor (`3`) local burden; forced settlement and expanded repression add major (`8`) burden/accountability. Roads/forts add rail, convoy, supply, and local resistance pressure even when their output succeeds.
- Under the current direct-control pool no subject autonomy effect fires. If the reviewed pool is expanded to an Italian subject, apply `+0.015` for ordinary projects and `+0.035` for forced settlement/suppression in the subject scope with `camp_rework_italy_colonial_autonomy_pressure`; closure/compensation concessions use the separate concession key. Do not add subject support implicitly.
- Security battalions may use the explicitly accepted timed garrison/security modifier path rather than inventing an unsupported division template. Closure clears `camp_rework_italy_security_battalions_active` and removes the modifier or converts it to an ordinary non-camp garrison state as the decision tooltip states.
- Closure sets the shared expansion freeze/reform flags and runs `ita_desert_camp_closure`; completion calls shared dismantlement, clears active administration/security flags, sets `camp_rework_italy_desert_camps_closed`, and retains evidence.
- Compensation subtracts accountability/claim damage using `constant:camp_rework_colonial.reform_credit` (`8`) or the accepted major settlement result, sets `camp_rework_italy_colonial_compensation_complete`, and may add `ita_colonial_reform_credit` only before severe discovery.
- Shared enemy-control discovery covers Allied capture/local uprising. Explicit bounded triggers are required for Italian capitulation with active evidence and postwar colonial review. Discovery applies claim damage/condemnation and opens closure after regime change; it does not loop minor reports.

### AI contract

| Condition | Expansion | Reform |
| --- | ---: | ---: |
| Fascist Italy controls Libya, peace/low war pressure | 20 | 0 |
| Fascist Italy at war, high Libya/East Africa resistance | 55 | 0 |
| Italy losing North Africa | 25 | 10 |
| Regime changed away from fascism | 0 | 85 |
| Discovery or high condemnation | 0 | 70 |
| No colonial states controlled | 0 | 0 |

The live baselines are expansion `42`, reform `70`, and active-site cap `5`. "Limited active project count" is qualitative in Part 5; the live common project cap is one and is a defensible exact implementation value, but it does not replace route and state caps. AI cannot use Italian cores through colonial actions, cannot build a Germany-scale European network, and can destroy evidence only near an enemy while evidence remains undiscovered.

### Part 7 scenario expectation

With fascist Italy controlling Libya under war/resistance pressure, Libya roads, forts, security, closure, and compensation routes work; East Africa also becomes eligible when controlled; every project uses a valid logistics target; local states record Deaths/resistance; Italy remains responsible; and non-fascist regime change strongly prefers closure. The scenario fails if the East Africa focus flag unlocks no target, colonial actions select an Italian core, a released colony leaves cleanup invisible, security battalions survive dismantlement as a camp benefit, or AI continues expansion after regime change.

## Belgium and Congo kit

### Required identifier inventory

Country values:

- `congo_extraction_pressure`
- `concession_labor_burden`
- `colonial_resource_output`
- `congo_population_damage`
- `colonial_unrest_pressure`
- `postwar_accountability_pressure`

Part 6 display values:

- `display_congo_extraction_pressure_band`
- `display_congo_accountability_pressure_band`

| Decision ID | Mandatory localisation keys | Required role |
| --- | --- | --- |
| `bel_expand_concession_labor_quotas` | ID, `_desc`, `_effect_tt` | Congo quota activation/expansion with resource and evidence pressure. |
| `bel_route_labor_to_rubber_and_minerals` | ID, `_desc`, `_effect_tt` | Resource-state route for existing rubber/mineral output; no resource creation on an invalid state. |
| `bel_build_congo_transport_corridors` | ID, `_desc`, `_effect_tt` | Selected rail/river/port/infrastructure/supply project. |
| `bel_suppress_colonial_strikes` | ID, `_desc`, `_effect_tt` | Short output restoration with major unrest/autonomy/evidence cost. |
| `bel_open_international_inspection` | ID, `_desc`, `_effect_tt` | Democratic/discovery/foreign-pressure reform opener; sets `camp_rework_belgium_inspection_open`. |
| `bel_reform_concession_system` | ID, `_desc`, `_effect_tt` | Starts the 365-day reform mandate and freezes quota/suppression loops. |
| `bel_recognize_local_administration` | ID, `_desc`, `_effect_tt` | Subject/local-autonomy concession and closure aftermath. |

| Mission ID | Days | Mandatory localisation keys | Success/failure contract |
| --- | ---: | --- | --- |
| `bel_congo_resource_quota_cycle` | 120 | ID, `_desc`, `_success_tt`, `_failure_tt` | Maintained resource-state control/transport grants timed output; failure raises strike/evidence pressure without full output. |
| `bel_congo_transport_corridor_project` | 210 | ID, `_desc`, `_success_tt`, `_failure_tt` | Maintained convoy/truck/train/factory burden completes a bounded corridor; failure adds local/transport burden. |
| `bel_colonial_strike_response` | 150 | ID, `_desc`, `_success_tt`, `_failure_tt` | Negotiation/reform lowers unrest and output; suppression restores output with evidence; inaction drops output and raises discovery risk. |
| `bel_concession_reform_mandate` | 365 | ID, `_desc`, `_success_tt`, `_failure_tt` | No quota expansion plus reform cost and valid Congo relation closes the active network; failure retains accountability/decolonisation crisis. |

| Idea ID | Owner | Mandatory localisation keys | Lifecycle |
| --- | --- | --- | --- |
| `bel_congo_concession_labor_system` | Belgium | ID, `_desc` | Dormant/first-quota administration. |
| `bel_congo_extraction_pressure` | Belgium | ID, `_desc` | Active extraction/transport output and evidence burden. |
| `congo_concession_labor_burden` | Congo subject/distinct local owner | ID, `_desc` | Population, unrest, and autonomy burden; use state burden if Belgium directly owns Congo. |
| `bel_colonial_resource_output` | Belgium | ID, `_desc` | Timed quota/corridor output, removed on closure or loss of Congo. |
| `bel_postwar_accountability_pressure` | Belgium | ID, `_desc` | Discovery, blocked inspection, or decolonisation liability. |
| `bel_congo_reform_credit` | Belgium | ID, `_desc` | Successful pre-severe-discovery reform memory. |

Required assets:

- `GFX_decision_bel_congo_concession_quota`
- `GFX_decision_bel_congo_transport_corridor`
- `GFX_decision_bel_colonial_inspection`
- `GFX_idea_bel_congo_extraction_pressure`
- `GFX_idea_congo_concession_labor_burden`
- `GFX_report_event_congo_labor_discovery`
- `GFX_news_event_congo_colonial_reckoning`

### Exact state-pool logic and overbreadth

The live Belgium pool symbols are in `common/scripted_triggers/camp_repression_rework_triggers.txt`.

1. `is_bel_congo_concession_pool_state` requires a `COG` core or `camp_rework_congo_concession_pool`, plus Belgian direct control or a controller subject of Belgium. Vanilla Congo cores are `295` Léopoldville, `538` Coquilhatville, `718` Stanleyville, `888` Lusambo, `889` Elisabethville, and `890` Costermansville.
2. `is_bel_congo_transport_project_state` requires the concession pool plus coastal status, infrastructure below `3`, or `camp_rework_congo_transport_pool`. In the 1936 vanilla setup, all six Congo states have low infrastructure; `295` also has the relevant port/coastal role.
3. `is_bel_colonial_emergency_pool_state` currently requires only non-Belgian-core status plus Belgian direct or subject control.
4. The accepted `is_bel_core_fallback_pool_state` helper is absent. The Congo package must never use Belgian cores.

The emergency trigger is materially broader than "other Belgian-controlled colonial territory": it admits any non-Belgian-core military occupation and any state controlled by any Belgian subject, including a European occupation. Before country decisions use it, require a reviewed colonial marker/geographic/legal condition. Do not reuse the generic occupied-state rule under a Congo-labelled decision.

Provide the accepted `is_bel_core_fallback_pool_state` API as an explicit negative guard (`always = no`) or another reviewed helper that can never return a Belgian core for the Congo route. Do not add it to the Congo action dispatcher as an eligible pool.

Current resource-bearing Congo states are rubber `538`, `718`, `890`; coal `888`; and tungsten/coal `889`. State `295` is primarily a transport/port target. Resource routing must test the resource that actually exists and keep its output timed; transport projects can target the wider corridor pool.

### DLC, subject, autonomy, and lifecycle effects

With Gotterdammerung, Belgium transfers Congo states to `COG` and the Gotterdammerung `set_autonomy` block in `history/countries/BEL - Belgium.txt` makes it `autonomy_colony` with freedom `0.2`; the Congo state-history DLC blocks perform the transfers. Without it, the same states remain directly Belgian-owned. The kit must support both forms:

- In the subject form, COG receives `congo_concession_labor_burden`; quota/corridor pressure uses `add_autonomy_ratio = +0.015`, strike suppression uses `+0.035`, and the source key is `camp_rework_bel_congo_autonomy_pressure`.
- Inspection/reform subtracts burden by `3`/`8`. Recognition uses `+0.035` freedom pressure with `camp_rework_bel_congo_autonomy_concession`, sets `camp_rework_belgium_local_administration_recognized`, and does not silently change autonomy tier.
- In the direct-ownership form, do not apply `congo_concession_labor_burden` to Belgium as though Belgium were the local victim. Keep the burden in the six Congo states through state variables/dynamic modifiers while Belgium receives extraction and accountability ideas.
- Every selected state's owner records Deaths; Belgium remains `genocide_responsible_country` regardless of direct/subject administration.

Quota activation adds the concession/extraction ideas and minor local burden. Resource/corridor cycles use bounded state selection and timed output; strike suppression adds major burden/evidence and cannot loop without rising cost. Inspection sets the shared inspection/reform/freeze flags and the Belgium inspection flag. Reform completion calls shared dismantlement for every Belgian-responsible site, removes extraction/output and local burden, sets `camp_rework_belgium_concessions_reformed`, and adds reform credit or lingering accountability according to discovery timing.

If COG becomes independent or ceases to be Belgium's subject, all expansion, quota, transport, and suppression actions hide immediately. Inspection, accountability, evidence, and reform remain visible to Belgium while it is still the stored responsible country. This is required even when Belgium has lost its European homeland and operates in exile; Congo control/subject validity, not Belgian core control, gates expansion.

Shared enemy/rebel control discovery covers captured sites. Explicit one-shot discovery remains necessary for blocked international inspection, decolonisation while active, and postwar accountability threshold. Discovery drops resource output sharply, adds Belgian accountability, raises Congo autonomy/unrest, and opens reform/local administration; it must not produce recurring leak popups.

The accepted mission cap is one quota cycle **and** one transport project at the same time. The live global `max_concurrent_projects = 1` cannot express that two-lane rule. Use separate mission-family active checks, as for the U.K. security/reform lanes.

### AI contract

| Condition | Expansion | Reform |
| --- | ---: | ---: |
| Belgium controls Congo, peace/stable economy | 15 | 10 |
| Belgium at war or in exile, resource shortage | 50 | 0 |
| Democratic Belgium with foreign pressure | 10 | 55 |
| Discovery or high accountability | 0 | 90 |
| Congo released/independent | 0 | 80 |
| Non-democratic high-chaos Belgium | 65 | 0 |

The live baselines are expansion `38`, reform `75`, and active-site cap `4`. AI may run one quota and one transport cycle but cannot use Belgian cores, radicalized escalation, or repeated zero-growth strike suppression. Independence forces expansion to zero while cleanup remains weighted.

### Part 7 scenario expectation

With Belgium at war or in exile while directly controlling Congo or retaining COG as a subject, quota/resource/transport decisions appear; only valid Congo resource/corridor states are used; Belgium receives timed output; Congo states and/or COG receive population, unrest, and autonomy burden; Belgium remains responsible; inspection/reform/local administration remove the active system; and AI respects the two-lane mission cap. The scenario fails if a Belgian/European core appears in a Congo action, the no-DLC setup applies the local burden idea to Belgium, COG independence leaves expansion visible, exile hides a still-valid Congo route, or accountability disappears when territorial control is lost.

## Constant and variable wiring contract

### Mission-duration constants

Do not place literal day counts in country decisions. Add these exact keys to `camp_rework_timing` or an equivalently documented `camp_rework_mission_days` script-constant category and use `constant:` access:

- U.K.: `uk_hold_raj_security_line_days = 150`, `uk_complete_raj_military_works_days = 180`, `uk_postwar_raj_review_days = 365`, `uk_negotiate_indian_release_terms_days = 270`.
- U.S.A.: `usa_court_review_period_days = 180`, `usa_security_authority_sunset_days = 270`, `usa_redress_commission_work_days = 365`.
- France: `fr_gurs_legacy_review_days = 180`, `fr_north_africa_rail_labor_project_days = 180`, `fr_refugee_pressure_response_days = 150`, `fr_post_liberation_reckoning_days = 365`.
- Italy: `ita_desert_road_labor_project_days = 180`, `ita_colonial_security_sweep_days = 150`, `ita_desert_camp_closure_days = 270`, `ita_postwar_colonial_compensation_days = 365`.
- Belgium: `bel_congo_resource_quota_cycle_days = 120`, `bel_congo_transport_corridor_project_days = 210`, `bel_colonial_strike_response_days = 150`, `bel_concession_reform_mandate_days = 365`.

The existing broad keys (`short_action_days`, `standard_action_days`, `construction_days`, `reform_days`, `dismantle_days`) do not cover Belgium's 210-day corridor and do not make per-mission tuning explicit. The file-scoped `@` form is not appropriate because the durations cross decisions/effects/localisation/tooltips.

### Country-value bridge rules

Country values are player-facing country-route state, while shared `camp_*` values remain the common Deaths/evidence/registry model. Avoid double-counting:

| Country value family | Bridge into the shared model |
| --- | --- |
| `imperial_detention_reach`, `wartime_security_reach`, `vichy_collaboration_reach`, `colonial_repression_reach`, `congo_extraction_pressure` | Rebuild from registered country-kit sites and route flags; do not add a second copy to `camp_network_reach`, which is already rebuilt from active sites. |
| `raj_labor_burden`, `relocation_population_disruption`, `north_africa_labor_burden`, `desert_camp_burden`, `concession_labor_burden`, `congo_population_damage` | Feed state Deaths/resistance/burden effects and the appropriate subject/local idea; responsible-country display remains separate from local owner impact. |
| `colonial_legitimacy_damage`, `democratic_legitimacy_damage` | Feed `camp_policy_legitimacy`/`camp_democratic_legitimacy_damage`; the U.S. value lacks the `camp_` prefix and must not drift from the shared display value. |
| `indian_autonomy_resistance`, `court_challenge_pressure`, `refugee_pressure`, `libyan_resistance_pressure`, `colonial_unrest_pressure` | Gate country missions/discovery and add to shared resistance/reform/visibility pressure only through the country bridge. |
| `dominion_control_pressure`, `imperial_manpower_pressure`, `colonial_logistics_output`, `colonial_resource_output` | Benefits remain bounded/timed and must carry the accepted manpower, rail, convoy, supply, stability, legitimacy, and evidence costs. |
| `redress_pressure`, `free_french_reform_credit`, `postwar_colonial_claim_damage`, `postwar_accountability_pressure` | Drive cleanup/aftermath ideas and category visibility even after territorial control or active-site count reaches zero. |

Initialise every Part 2 value in `camp_rework_initialize_country_variables`, clamp or rebuild it in the country monthly bridge, copy the Part 6 bands in `camp_rework_copy_display_values`, and clear only transient values during completed reform. Reform credit, accountability, and responsibility/evidence memory survive active-site cleanup as specified.

### Exact live cap/weight constants

| Kit | Active-site cap | Live baseline weights |
| --- | ---: | --- |
| U.K. | `camp_rework_ai_cap.uk_active_sites = 4` | activation `25`, expansion `18`, reform `80` |
| U.S.A. | `camp_rework_ai_cap.usa_active_sites = 3` | activation `6`, expansion `2`, reform `90` |
| France/Vichy | `camp_rework_ai_cap.france_active_sites = 5` | Vichy expansion `42`, reform `75` |
| Italy | `camp_rework_ai_cap.italy_active_sites = 5` | expansion `42`, reform `70` |
| Belgium | `camp_rework_ai_cap.belgium_active_sites = 4` | expansion `38`, reform `75` |

`camp_rework_country_under_ai_site_cap` in `common/scripted_triggers/camp_repression_rework_triggers.txt` consumes these caps. The colonial baseline weights currently have no consumers. Each `ai_will_do` must combine its baseline with the exact Part 5 condition table and use the same pool/action trigger as the player. AI state choice must remain in `camp_rework_select_ai_state`; do not drive AI through the player-selected GUI state.

## Exact implementation surface and ownership map

| File/surface | Required country-tranche work | Collision/ownership rule |
| --- | --- | --- |
| `common/decisions/camp_repression_colonial_country_decisions.txt` (new, recommended) | Define all 40 decisions and 19 missions under the existing `camp_repression_network_category`; bounded state actions call the country action dispatcher. | Do not put these in the generic file and do not duplicate the category metadata. |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | Resolve pool API names, France subject fallback, Italy project scope, Belgium emergency/core guard, country route/activation/reform/mission-cap triggers. | Keep all territorial selectors geographic/legal and bounded. |
| `common/scripted_effects/camp_repression_rework_effects.txt` | Initialise/copy country values; implement `camp_rework_route_country_specific_action`; country idea refresh; country monthly bridge; subject/local burden; one-shot legal/decolonisation discovery; country cleanup wrappers. | Reuse shared registration, Deaths, evidence, selection, and dismantlement. The required route dispatcher does not exist in the live file. |
| `common/script_constants/camp_repression_rework_constants.txt` | Add per-mission day keys, any reviewed country deltas/conditional cap constants, and secondary-responsibility share. | Reuse existing costs/colonial `3/8`, autonomy `.015/.035`, reform `8`, and redress `12`; no hardcoded tuning in decisions. |
| `common/ideas/camp_repression_rework_ideas.txt` | Add all 30 country lifecycle ideas. | Country burden ideas must not substitute for state damage or be applied to the responsible country when it is also direct colonial owner. |
| `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt` | Reuse or narrowly extend state labor, sabotage, refugee, disruption, and local-burden modifiers for country routes. | Do not create five copied state modifiers when the existing state variables can supply the distinction. |
| `common/ai_strategy/genocide_crisis_ai_strategy.txt` and decision `ai_will_do` | Add only useful country strategic context; implement exact condition weights and caps in the decisions/actions. | AI strategy cannot replace valid action/pool checks. |
| `common/decisions/categories/genocide_crisis_categories.txt` | Existing category metadata/highlighting already points at shared valid sites/pools. Update only if country cleanup visibility proves missing. | Category visibility must persist for responsibility, evidence, redress, or reform after pool loss. |
| `common/on_actions/genocide_crisis_on_actions.txt` / existing monthly host | No new global iteration. Reuse state-control and capitulation hooks plus the existing registered-country monthly pulse. | Country legal/postwar checks operate on registered responsible countries, not all countries. |
| `localisation/english/camp_repression_rework_l_english.yml` | Add the exhaustive key families in this report and final in-world text. | UTF-8 BOM; no `:0`; no formula/debug/update-history language. |
| `common/scripted_localisation/` and required GUI files | Add country panel labels, display bands, block/cost/action text, and selected-state subject/local owner output. | Subject-administered targets must be actionable through bounded arrays; no world-state target list. |
| `interface/camp_repression_rework.gfx` (new/reviewed) and final asset folders | Register all 32 listed country IDs before final art handoff; wire decision/idea/report/news sprites. | No placeholder or unregistered sprite counts as complete. Focus flags need no focus icons. |
| Country discovery/report events | Add bounded, one-shot court, inspection, liberation, decolonisation, compensation, and reckoning entry points where justified. | No recurring monthly minor-report spam; final event IDs must be recorded in the tracker before code. |
| `common/national_focus/` | No edit for this tranche. | All 29 Part 5 hooks are country flags only because no bespoke tree exists. |

## Superseded preimplementation collisions, assumptions, and blockers

### Must be resolved before country implementation can be called complete

1. **Subject state actions have no bounded player action surface yet.** Pool arrays include subject-controlled states, but `state_target = any_controlled_state` does not. Implement the selected-state scripted-GUI/action dispatcher; do not use `state_target = any`.
2. **The required country action dispatcher is absent.** `camp_rework_route_country_specific_action` is in the accepted tracker/architecture but has no live definition.
3. **Country values, display bands, ideas, monthly bridges, decisions, missions, localisation, and assets are all absent.** Existing pool triggers and constants are not a country kit.
4. **France and Italy pool APIs do not exactly match accepted names.** Resolve the aliases/names before multiple call sites are added.
5. **France core fallback ignores subject-administered higher pools and lacks its authoritarian gate at trigger level.** A democratic/Free decision must never expose it.
6. **Italy's project pool is Libya-only.** It cannot deliver the accepted East Africa project route.
7. **Belgium's colonial emergency pool is any non-Belgian-core direct/subject-controlled state.** It admits ordinary European occupations and needs a colonial/legal restriction.
8. **Belgium's accepted core-fallback helper is missing.** The Congo package requires an explicit never-core guard.
9. **The U.K. and Belgium two-lane mission caps conflict with the single global project cap.** Independent family checks are required.
10. **Vichy/German secondary responsibility is specified but unimplemented.** Germany cannot be linked safely until `camp_site_secondary_responsible_country` and a constant-defined share exist.
11. **Country discovery is incomplete.** Shared discovery covers qualifying control changes, but court review, international inspection, postwar review, decolonisation, and regime-change reckoning require explicit bounded one-shot entry points.
12. **Some accepted qualitative caps remain numerically undefined.** In particular, "small Raj active network before 1939" and Italy's "limited active count" are not assigned source-spec numbers. The live caps are documented above; any date-sensitive override requires owner acceptance, not an invented value.

### State and tag assumptions

- The previous French `state = 34` collision is resolved in the live trigger. State `34` is Wallonia and must stay out of the French pool.
- The previous `infrastructure < 6` always-true condition is resolved. The live constant is `3`, so the strict test admits levels 0-2 against vanilla's level-5 maximum.
- The U.S. interior pool still assumes non-coastal means low combat risk/usable infrastructure; that is not enforced.
- The Raj owner/controller-original-tag clause supports tag changes and princely states but also admits later Raj conquests outside India.
- Burma's subject status is DLC-dependent in vanilla history; the no-DLC setup does not puppet `BRM`.
- Congo's direct-owner versus subject form is DLC-dependent; both must work without applying the victim burden to Belgium.
- `ENG`, `FRA`, `BEL`, `ITA`, `USA`, `RAJ`, `LBA`, `MAL`, `COG`, `PAK`, `BAN`, `BRM`, `SRL`, `ALG`, `MOR`, `TUN`, `ERI`, and `SOM` all have definitions in vanilla `common/country_tags/00_countries.txt`. `VIC` is the valid alias described above. No live country-pool tag is unsupported.
- Morocco cores `290` and `783` begin Spanish-owned. They only qualify after the French/Vichy control gate is true, so this is a controlled future claim rather than a startup collision.
- East Africa's `ETH`/`SOM` core unions deliberately include French/British Somali and Ethiopian states, but only actual Italian direct control qualifies them.

### Autonomy and ownership blockers

- Direct colonial ownership and subject administration are different. A country idea on the subject cannot represent direct-owned local harm; use state burden in the latter case.
- Positive `add_autonomy_ratio` represents both backlash and negotiated concession. Use distinct localisation source keys so the tooltip explains why freedom pressure rises.
- The U.K. coordination decision's engine-autonomy direction is not fixed by the accepted package. Keep it as a pressure/timed-idea effect until that choice is accepted.
- No ordinary kit action may use `set_autonomy`. A tier change for Indian self-government or Congo recognition is a separate design decision and must execute from the overlord scope if later approved.

## Implementation and validation order

1. Resolve the six pool/API issues: U.S. interior semantics, France API/subject fallback, Italy project scope/API, Belgium emergency restriction, and Belgium no-core helper.
2. Add per-mission constants, country values, initialisation, display copies, and the secondary-responsibility field/share.
3. Implement the bounded selected-state country action dispatcher and country-specific player/AI target validation.
4. Implement one country kit at a time in the order U.K./Raj, U.S.A., France/Vichy, Italy, Belgium; after each, add its ideas, monthly bridge, autonomy/local burden, AI, cleanup, and legal discovery before moving on.
5. Add final localisation and stable GFX registrations in the same country tranche; assets follow the registered IDs.
6. Run the five Part 7 scenarios plus direct-control/subject-control and loss-of-subject variants. Confirm state owner Deaths, stored responsibility, evidence retention, route caps, AI reform, and category visibility after territorial loss.
7. Run the decision/mission, country-package, localisation, and event-completion audit routes before any completion claim. The absence of a bespoke focus tree is not an omission if all listed focus interfaces are implemented and reported as flags.

## Historical completion boundary for the original map

This report contains the full accepted ID inventories, the live pool behavior, exact vanilla state/tag/autonomy evidence, required subject and responsibility handling, conditional AI tables and current numeric caps, lifecycle/discovery expectations, focus-hook disposition, localisation key contract, asset IDs, implementation surfaces, and Part 7 scenario outcomes for all five kits. It makes no gameplay simplification and does not treat any missing country content as implemented. The blockers above remain implementation work or explicit design choices for the parent owner.

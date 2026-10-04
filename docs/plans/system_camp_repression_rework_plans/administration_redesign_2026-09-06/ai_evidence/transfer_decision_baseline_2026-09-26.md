# German exact-cohort prisoner-transfer AI baseline and post-edit audit

Date: 2026-09-26.

## Scope and accepted behavior

Audited surface: `decision_ai_will_do` for `germany_transfer_prisoners_to_experiment_site` in `common/decisions/genocide_crisis_decisions.txt`, plus the 29-decision candidate pool in that source file.

The parent confirmed that the user chose to retire the pre-administration whole-state transfer behavior and repurpose this same explicit decision id as a post-administration paid exact-cohort transfer. This audit therefore evaluates that accepted transition; it does not treat the preserved id as preserving the old behavior.

This is a read-only probability audit. I changed no gameplay, trigger, effect, localisation, or AI source. I created the exact pre-edit source snapshot and this handoff only.

## Source identity

- Pre-edit source: `common/decisions/genocide_crisis_decisions.txt`, local raw SHA256 `4E3E377165AC949B8D54CD9547C6CB6D903046B59915AF4FF2DCCA3A211EDFD5`.
- Exact frozen pre-edit copy: `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/genocide_crisis_decisions_pre_edit_2026-09-26.txt`, raw SHA256 `4E3E377165AC949B8D54CD9547C6CB6D903046B59915AF4FF2DCCA3A211EDFD5`.
- Superseded interim decision source before the compact-order revision: raw SHA256 `FC30D0CA1CFAB4CC8B359AACF901F68DA0FAB5BE7F0ADFD32FA9BCCF434A182A`; its MCP source hash was `e66e2e4907970ec6a1d18386906f49f7b371bd14bb65835a905c7bb6c52e72f6`.
- Current final decision source: `common/decisions/genocide_crisis_decisions.txt`, local raw SHA256 `53687EFA480D162B27C89895269984B74F7D474CABB76F5E022225630C41B237`.
- Supporting source raw SHA256 values at current review: `common/script_constants/genocide_crisis_constants.txt` `A401F28D80B6ACCE73E25ECBE5360CE2BC31CBEF92140833AAE3D4B346AD67B0`; `common/script_constants/camp_repression_rework_constants.txt` `644CCC2FE2F16653AEF3417B321EE78BC56A7059E06EFDFDE99180611938102F`; `common/scripted_triggers/camp_administration_occupation_triggers.txt` `7A24065D8F8A590CAA782F2CA496F3627FCE963A926C3DA4EF9D79336AD7C247`; `common/scripted_effects/camp_repression_major_country_effects.txt` `0BCCCCDDB1D6BFE04CF040076B504AEAA694FE3EF76318D7CDD029E6A0FF3C6E`; `common/scripted_effects/camp_administration_occupation_effects.txt` `137E345405C07512D389B0E61C8D6ACB8800A705B50ED442900C911D73D4218C`; `common/scripted_effects/camp_administration_occupation_effects.md` `7898EF4F5F489A41391940C93EECFDF9C4D86E450E4F12353A5547FFC44F8C16`; `common/scripted_localisation/camp_administration_country_localisation.txt` `722935E6229D3B185D2ED502E60DE2AB3DD382F96AA26C8219CD291F3C1D40CF`; `common/ai_strategy/genocide_crisis_ai_strategy.txt` `C7B09C1598762206CD3D1FCA0055631960E573D759B1C54AC8F147FA9F6A3433`.
- MCP reports its own source hashes, which differ from the local raw SHA256 values; its hash algorithm and normalization are not exposed, so both identities are retained separately.
- Baseline MCP source hash: `5e92b824727e37dabcc4cdb69382deba0e4afd879c2b77bc1c8bf30e5a34d590`; full-pool inspect revision: `ff30a6bb95b9289bd859c84a25de7a00505551f2005209a810f4f9d8c9f8e52f`.
- Current final MCP source hash: `bb8a5c42c6c0a95f78d67d10eb074958fab35c2d5a347af5413878c3e04cc8db`; full-pool inspect revision: `3efb3b80aa0bdceab80fbc9a0ffa6af2d1607163e6624493f66086b9023946f8`.

## Weighted surface and source trace

`common/script_constants/genocide_crisis_constants.txt` defines `genocide_ai_weight.germany_direct_holocaust = 55.00` and `genocide_timing.decision_cooldown = 60` days.

The pre-edit decision used base `55.00` and a factor of `0` when either `camp_rework_country_under_ai_site_cap` or `camp_rework_country_under_ai_experiment_cap` failed.

The final compact national order uses `ai_will_do = { base = constant:genocide_ai_weight.germany_direct_holocaust }` with no decision-local AI modifier. It has no `state_target` or `target_trigger`; availability instead checks the country-level `camp_occ_manual_source_state_id` variable and scopes that selected state through `camp_occ_manual_transfer_source_ready`.

The final decision is visible only after `camp_admin_initialized`, for original GER with the active or restricted Mengele program. Availability checks `camp_occ_manual_transfer_country_ready`, the selected variable-scoped source helper `camp_occ_manual_transfer_source_ready`, and `camp_occ_manual_transfer_can_pay`; the effect calls `camp_rework_germany_apply_exact_cohort_transfer`.

`camp_occ_manual_transfer_country_ready` also requires the live campaign, war, date after 1943-05-29, no expansion freeze, permission above the rejected threshold, and an operational state 88 destination with capacity and GER responsibility. The source helper requires a current native authority row, remaining cohort above its minimum, a permitted GER source state, no rollback failure, and GER responsibility.

`camp_occ_manual_transfer_can_pay` checks 35 political power, 5 army experience, 180 support equipment, and 18 trains. The scripted effect debits the same resources only after a valid transfer receipt; the UI AI hint is 35 political power.

The source has no cohort-specific AI modifier, so the single national order uses the same 55 willingness score regardless of the selected source. The score is not a click probability and is not normalized into one.

`camp_occ_refresh_manual_transfer_source` scans `camp_occ_states` in registration order, preflights the first currently eligible native row for one person, and stores that state as the national order's source. After a successful transfer, the effect refreshes the selection, so newer eligible sources wait until older registered sources stop qualifying. This oldest-first progression is deterministic source selection rather than a target-level AI weight race, and it matches the parent-confirmed user choice.

Relevant source files reviewed: `common/decisions/genocide_crisis_decisions.txt`, `common/script_constants/genocide_crisis_constants.txt`, `common/script_constants/camp_repression_rework_constants.txt`, `common/scripted_triggers/camp_administration_occupation_triggers.txt`, `common/scripted_effects/camp_administration_occupation_effects.txt`, `common/scripted_effects/camp_repression_major_country_effects.txt`, `common/scripted_effects/camp_administration_occupation_effects.md`, and `common/ai_strategy/genocide_crisis_ai_strategy.txt`.

The related `common/ai_strategy/genocide_crisis_ai_strategy.txt` was inspected with the `ai_strategy_factor` adapter. MCP returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and zero required inputs; its current strategy blocks adjust build-army, avoid-war, and equipment-production behavior and did not expose a decision `ai_strategy_factor` surface. This does not prove the absence of every external AI multiplier elsewhere in the game.

## MCP baseline and final results

The baseline full-pool `hoi4.probability_inspect` returned `poolComplete=true` for the 29 candidate ids supplied from this source file, `candidates=29`, and `requiredInputs=33`. This establishes completeness of the declared source-file pool only; it does not prove the full game-wide set of decisions available to every actor.

Baseline scenario set `genocide_transfer_decision_baseline_2026-09-26` has scenario hash `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`. `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED_PARTIAL`, 6 scenarios, 174 candidate-scenario rows, and 541 unresolved items. It reported the old transfer candidate never eligible across those supplied scenarios; because compound helpers, variables, and target scopes were unresolved, this is not proof that a live GER campaign could never make it eligible.

The current compact-order evaluation reused the identical scenario hash and complete 29-id pool. It returned `PROBABILITY_ANALYZED_PARTIAL`, 6 scenarios, 174 candidate-scenario rows, and 494 unresolved items. There was no target-specific never-eligible diagnostic, but the analyzer did not return per-scenario eligibility or an inline score vector, so valid-versus-invalid eligibility remains unresolved. The fixture declares a `from` state but has no typed `camp_occ_manual_source_state_id` or `camp_occ_states` registry; this source version selects the source through that variable rather than `FROM`.

The scenario id `GER_post_administration_invalid` includes the `camp_admin_initialized` flag. The `invalid` suffix describes the baseline pre-administration candidate; this same fixture now has the administration flag required by the post-administration order. The id was kept unchanged for comparison, but source-pointer, country-ready, oldest-source registry, destination, and payment state remain unresolved.

The current numeric sweep used MCP source hash `bb8a5c42c6c0a95f78d67d10eb074958fab35c2d5a347af5413878c3e04cc8db`, the complete 29-id pool, five declared values `0, 25, 55, 100, 150` on `genocide_ai_weight.germany_direct_holocaust`, and `findRankReversals=true`. Scenario set id `genocide_transfer_weight_sensitivity_2026-09-26` has hash `ed0b83aa53585a10d655480b49e8384738739dd67cdc1b3c88d94c450f0746e`. It returned `PROBABILITY_ANALYZED_PARTIAL`, five sweep points, 145 candidate-scenario rows, and 406 unresolved items.

The five-point sensitivity sweep is a bounded sensitivity grid, not a simulation. The tool returned ranking, sensitivity, threshold, and unresolved artifacts, but no inline rank-reversal summary; a rank reversal or stable ordering is therefore unresolved. No exact candidate selection probability is supported.

`hoi4.probability_compare` was attempted against the current `53687E...` source with the exact frozen pre-edit copy, same scenario hash, and same pool. It returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request` for the pre-edit path under `docs/plans/.../ai_evidence/`; it returned no comparison id or numeric delta. The probability adapter indexes weighted decision sources under its decision-source paths and did not recognize the saved documentation-path copy. I did not compare the current file to itself or substitute source arithmetic for MCP evidence.

## Scenario and candidate-pool contract

The six exact scenario ids are `GER_pre_administration_valid`, `GER_post_administration_invalid`, `JAP_pre_administration_weight_check`, `SOV_pre_administration_weight_check`, `ENG_foreign_response_wartime`, and `RAJ_foreign_response_wartime`.

The scenario states are declared synthetic fixtures, not a live save. Their `state` maps are flat primitives. They do not provide typed Clausewitz variable bindings or reliable expansion of compound helper triggers, arrays, native cohort rows, the registered-source array and selection pointer, state-88 custody state, resource payment, or all external AI modifiers. Their old `from` scopes are not consumed by the compact national order. No seeds, random distributions, scheduled state changes, or cadence were declared.

Candidate pool supplied on every completed evaluation and sweep:

```text
germany_wartime_camp_administration
germany_expand_occupied_poland_camp_system
germany_expand_extermination_site_network
germany_intensify_extermination_policy
germany_transfer_prisoners_to_experiment_site
genocide_restricted_chemical_site_escalation
genocide_build_extermination_camp
genocide_intensify_deportations
genocide_hide_evidence_from_foreign_observers
genocide_suppress_internal_reports
genocide_redirect_trains_and_supplies
genocide_deal_with_resistance_sabotage
genocide_handle_refugee_waves
genocide_manage_military_objections
genocide_destroy_camp_evidence
genocide_cover_up_liberated_camps
japan_expand_forced_labor_camps
japan_conduct_anti_partisan_reprisals
japan_transfer_prisoners_to_experimental_facilities
japan_destroy_occupation_records
sov_expand_gulag_network
sov_deport_suspected_opposition_groups
sov_confiscate_food_from_disloyal_regions
sov_purge_camp_administrators
sov_raise_forced_labor_quotas
sov_destroy_gulag_records
genocide_publicize_survivor_testimony
genocide_support_resistance_networks
genocide_prepare_tribunal_records
```

Exact scenario fixture and candidate pool used for the baseline and final evaluation:

```json
{
  "scenarioSet": {
    "id": "genocide_transfer_decision_baseline_2026-09-26",
    "scenarios": [
      {
        "id": "GER_pre_administration_valid",
        "actor": "GER",
        "state": {
          "original_tag": "GER",
          "is_ai": true,
          "is_major": true,
          "date": "1944.6.1",
          "has_government": "fascism",
          "has_war": true,
          "camp_admin_country_mengele_historical_gate": true,
          "germany_mengele_is_germany_scope": true,
          "germany_controls_auschwitz_area": true,
          "germany_mengele_program_active": true,
          "mengele_permission_level": 2,
          "camp_ai_active_site_cap": 4,
          "camp_active_site_count": 1,
          "camp_ai_experiment_site_cap": 3,
          "camp_experiment_site_count": 1,
          "camp_rework_country_under_ai_site_cap": true,
          "camp_rework_country_under_ai_experiment_cap": true,
          "genocide_state_has_active_camps": true,
          "army_experience": 20,
          "manpower": 100000,
          "support_equipment_1": 100,
          "train_equipment_1": 30
        },
        "flags": [
          "germany_mengele_program_authorized",
          "camp_ai_can_expand"
        ],
        "scopes": {
          "root": {
            "id": "GER",
            "state": {
              "original_tag": "GER",
              "is_ai": true,
              "is_major": true,
              "date": "1944.6.1",
              "has_government": "fascism",
              "has_war": true,
              "camp_admin_country_mengele_historical_gate": true,
              "germany_mengele_is_germany_scope": true,
              "germany_controls_auschwitz_area": true,
              "germany_mengele_program_active": true,
              "mengele_permission_level": 2,
              "camp_ai_active_site_cap": 4,
              "camp_active_site_count": 1,
              "camp_ai_experiment_site_cap": 3,
              "camp_experiment_site_count": 1,
              "camp_rework_country_under_ai_site_cap": true,
              "camp_rework_country_under_ai_experiment_cap": true,
              "genocide_state_has_active_camps": true,
              "army_experience": 20,
              "manpower": 100000,
              "support_equipment_1": 100,
              "train_equipment_1": 30,
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "camp_admin_site_is_operational": true
            }
          },
          "from": {
            "id": "89",
            "state": {
              "is_controlled_by": "GER",
              "state_id": 89,
              "is_core_of_ROOT": false,
              "is_on_continent": "europe",
              "is_core_of_POL": true,
              "concentration_camp": 1,
              "extermination_camp": 0,
              "genocide_responsible_country": "GER",
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "is_germany_occupied_poland_prisoner_source": true
            }
          },
          "state_88": {
            "id": "88",
            "state": {
              "is_controlled_by": "GER",
              "camp_admin_site_is_operational": true,
              "camp_rework_state_can_accept_responsibility_from_root": true
            }
          }
        }
      },
      {
        "id": "GER_post_administration_invalid",
        "actor": "GER",
        "state": {
          "original_tag": "GER",
          "is_ai": true,
          "is_major": true,
          "date": "1944.6.1",
          "has_government": "fascism",
          "has_war": true,
          "camp_admin_country_mengele_historical_gate": true,
          "germany_mengele_is_germany_scope": true,
          "germany_controls_auschwitz_area": true,
          "germany_mengele_program_active": true,
          "mengele_permission_level": 2,
          "camp_ai_active_site_cap": 4,
          "camp_active_site_count": 1,
          "camp_ai_experiment_site_cap": 3,
          "camp_experiment_site_count": 1,
          "camp_rework_country_under_ai_site_cap": true,
          "camp_rework_country_under_ai_experiment_cap": true,
          "genocide_state_has_active_camps": true,
          "army_experience": 20,
          "manpower": 100000,
          "support_equipment_1": 100,
          "train_equipment_1": 30
        },
        "flags": [
          "camp_admin_initialized",
          "germany_mengele_program_authorized",
          "camp_ai_can_expand"
        ],
        "scopes": {
          "root": {
            "id": "GER",
            "state": {
              "original_tag": "GER",
              "is_ai": true,
              "is_major": true,
              "date": "1944.6.1",
              "has_government": "fascism",
              "has_war": true,
              "camp_admin_country_mengele_historical_gate": true,
              "germany_mengele_is_germany_scope": true,
              "germany_controls_auschwitz_area": true,
              "germany_mengele_program_active": true,
              "mengele_permission_level": 2,
              "camp_ai_active_site_cap": 4,
              "camp_active_site_count": 1,
              "camp_ai_experiment_site_cap": 3,
              "camp_experiment_site_count": 1,
              "camp_rework_country_under_ai_site_cap": true,
              "camp_rework_country_under_ai_experiment_cap": true,
              "genocide_state_has_active_camps": true,
              "army_experience": 20,
              "manpower": 100000,
              "support_equipment_1": 100,
              "train_equipment_1": 30,
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "camp_admin_site_is_operational": true
            }
          },
          "from": {
            "id": "89",
            "state": {
              "is_controlled_by": "GER",
              "state_id": 89,
              "is_core_of_ROOT": false,
              "is_on_continent": "europe",
              "is_core_of_POL": true,
              "concentration_camp": 1,
              "extermination_camp": 0,
              "genocide_responsible_country": "GER",
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "is_germany_occupied_poland_prisoner_source": true
            }
          },
          "state_88": {
            "id": "88",
            "state": {
              "is_controlled_by": "GER",
              "camp_admin_site_is_operational": true,
              "camp_rework_state_can_accept_responsibility_from_root": true
            }
          }
        }
      },
      {
        "id": "JAP_pre_administration_weight_check",
        "actor": "JAP",
        "state": {
          "original_tag": "JAP",
          "is_ai": true,
          "is_major": true,
          "date": "1941.6.1",
          "has_government": "fascism",
          "has_war_with_chinese_country": true,
          "camp_admin_initialized": false,
          "camp_rework_expansion_frozen": false,
          "camp_rework_country_under_ai_site_cap": true,
          "camp_rework_country_under_ai_experiment_cap": true,
          "camp_ai_active_site_cap": 4,
          "camp_active_site_count": 1,
          "camp_ai_experiment_site_cap": 3,
          "camp_experiment_site_count": 1,
          "genocide_country_has_biowarfare_atrocity_capacity": true,
          "army_experience": 20,
          "manpower": 100000,
          "support_equipment_1": 100,
          "train_equipment_1": 30
        },
        "flags": [
          "camp_ai_can_expand"
        ],
        "scopes": {
          "root": {
            "id": "JAP",
            "state": {
              "original_tag": "JAP",
              "is_ai": true,
              "has_government": "fascism"
            }
          },
          "from": {
            "id": "193",
            "state": {
              "is_controlled_by": "JAP",
              "is_core_of_JAP": false,
              "is_core_of_CHI": true,
              "concentration_camp": 1,
              "extermination_camp": 0,
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "is_japan_china_manchuria_pool_state": true
            }
          }
        }
      },
      {
        "id": "SOV_pre_administration_weight_check",
        "actor": "SOV",
        "state": {
          "original_tag": "SOV",
          "is_ai": true,
          "is_major": true,
          "date": "1941.6.1",
          "has_government": "communism",
          "sov_camp_is_stalinist_repression_route": true,
          "sov_camp_is_reform_route": false,
          "camp_rework_country_under_ai_site_cap": true,
          "camp_ai_active_site_cap": 4,
          "camp_active_site_count": 1,
          "has_stability": 0.6,
          "command_power": 50,
          "political_power": 100
        },
        "flags": [
          "SOV_paranoia_system_active_flag",
          "camp_ai_can_expand"
        ],
        "scopes": {
          "root": {
            "id": "SOV",
            "state": {
              "original_tag": "SOV",
              "is_ai": true,
              "has_government": "communism"
            }
          },
          "from": {
            "id": "193",
            "state": {
              "is_controlled_by": "SOV",
              "is_core_of_SOV": false,
              "gulag_labor_camp_network": 0,
              "camp_rework_state_can_accept_responsibility_from_root": true,
              "is_soviet_gulag_periphery_pool_state": true
            }
          }
        }
      },
      {
        "id": "ENG_foreign_response_wartime",
        "actor": "ENG",
        "state": {
          "original_tag": "ENG",
          "is_ai": true,
          "is_major": true,
          "has_government": "democratic",
          "has_war": true,
          "genocide_country_has_discovered_sites": true,
          "genocide_country_condemnation_50": true,
          "genocide_country_condemnation_100": true,
          "genocide_discovered_sites": 1,
          "condemnation_atrocity": 100,
          "condemnation_coverup": 0
        },
        "flags": [],
        "scopes": {
          "root": {
            "id": "ENG",
            "state": {
              "original_tag": "ENG",
              "is_major": true,
              "has_government": "democratic",
              "has_war": true
            }
          },
          "from": {
            "id": "GER",
            "state": {
              "genocide_country_has_discovered_sites": true,
              "genocide_discovered_sites": 1,
              "genocide_country_condemnation_50": true,
              "genocide_country_condemnation_100": true,
              "genocide_country_condemnation_50_level": true,
              "genocide_country_condemnation_100_level": true
            }
          }
        }
      },
      {
        "id": "RAJ_foreign_response_wartime",
        "actor": "RAJ",
        "state": {
          "original_tag": "RAJ",
          "is_ai": true,
          "is_major": false,
          "has_government": "democratic",
          "has_war": true,
          "genocide_country_has_discovered_sites": true,
          "genocide_country_condemnation_50": true,
          "genocide_country_condemnation_100": true,
          "genocide_discovered_sites": 1,
          "condemnation_atrocity": 100,
          "condemnation_coverup": 0
        },
        "flags": [],
        "scopes": {
          "root": {
            "id": "RAJ",
            "state": {
              "original_tag": "RAJ",
              "is_major": false,
              "has_government": "democratic",
              "has_war": true
            }
          },
          "from": {
            "id": "GER",
            "state": {
              "genocide_country_has_discovered_sites": true,
              "genocide_discovered_sites": 1,
              "genocide_country_condemnation_50": true,
              "genocide_country_condemnation_100": true
            }
          }
        }
      }
    ]
  },
  "candidatePool": [
    "germany_wartime_camp_administration",
    "germany_expand_occupied_poland_camp_system",
    "germany_expand_extermination_site_network",
    "germany_intensify_extermination_policy",
    "germany_transfer_prisoners_to_experiment_site",
    "genocide_restricted_chemical_site_escalation",
    "genocide_build_extermination_camp",
    "genocide_intensify_deportations",
    "genocide_hide_evidence_from_foreign_observers",
    "genocide_suppress_internal_reports",
    "genocide_redirect_trains_and_supplies",
    "genocide_deal_with_resistance_sabotage",
    "genocide_handle_refugee_waves",
    "genocide_manage_military_objections",
    "genocide_destroy_camp_evidence",
    "genocide_cover_up_liberated_camps",
    "japan_expand_forced_labor_camps",
    "japan_conduct_anti_partisan_reprisals",
    "japan_transfer_prisoners_to_experimental_facilities",
    "japan_destroy_occupation_records",
    "sov_expand_gulag_network",
    "sov_deport_suspected_opposition_groups",
    "sov_confiscate_food_from_disloyal_regions",
    "sov_purge_camp_administrators",
    "sov_raise_forced_labor_quotas",
    "sov_destroy_gulag_records",
    "genocide_publicize_survivor_testimony",
    "genocide_support_resistance_networks",
    "genocide_prepare_tribunal_records"
  ]
}
```

## Findings and classification

- **Exact, score-only:** the final source gives this decision a 55.00 base willingness score with no decision-local modifiers; its shared constant and 60-day re-enable value are source-backed.
- **Unresolved:** MCP could not bind the compound country-ready, exact source-row, destination, and payment helpers to the flat scenario state, so candidate eligibility for each scenario is not proven.
- **Exact, source-ordered selection:** `camp_occ_refresh_manual_transfer_source` scans `camp_occ_states` in registration order and selects the first source that passes one-person preflight. After success, the selection is refreshed, so newer eligible rows wait until older registered sources stop qualifying. This deterministic oldest-first priority is parent-confirmed user intent, not a probabilistic target race.
- **Unresolved:** per-scenario decision eligibility, ranking against other available national decisions, dominance, and rank reversal remain unresolved under 494 final-evaluation items and 406 sweep items; rendered artifacts are retained below.
- **Source-backed repetition:** the order re-enables after 60 days, refreshes its selected source after each valid receipt, and each success raises escalation and hidden-atrocity values. The 60-day cumulative pacing and snowball magnitude were not analyzed as a dynamic sequence.
- **Unresolved external factor:** no complete game-wide decision universe or live AI-strategy multiplier set was declared. The 29-id candidate pool is complete for this inspected source file only.
- **Not analyzed:** `probability_simulate` was not used because no uncertain distributions or random inputs were declared. `probability_sequence` was not used because this is a native national decision rather than a declared custom weighted pool. Event MTTH, event `ai_chance`, random-list, focus, mission, research, and technology weights are outside this task.

## Recommended follow-up

Keep the centralized 55.00 base if the compact national order should have uniform AI willingness; no balance target was selected by this audit.

If AI willingness should vary with campaign state, add explicit decision-level modifiers only with a typed scenario fixture that lets MCP evaluate those inputs and rank reversals without changing the oldest-source, payment, or source-validity contract.

The accepted oldest-first selector and 60-day repeat cadence should be included in any cumulative escalation review. If the intended system should stop after a fixed number of successful orders, that limit needs an explicit receipt or completion gate; this audit does not choose or apply one.

## MCP evidence

Baseline artifacts below remain authoritative for the pre-edit source. The `FC30/e66` final-cycle artifacts are preserved as an intermediate revision and are superseded by the current `53687/bb8a` compact national-order cycle in the final subsection.

- Baseline full-pool inspect revision `ff30a6bb95b9289bd859c84a25de7a00505551f2005209a810f4f9d8c9f8e52f`, source hash `5e92b824727e37dabcc4cdb69382deba0e4afd879c2b77bc1c8bf30e5a34d590`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3ffc3ceb8431e5bbb42387e3a9e6eaa85dff0d407c625eda731e525b121a488/50181d7fa071af44bb640715a70ee47f5b91866b17a7c769609517b9c24fbdbe/probability-inspect-5e92b824727e.json`.
- Baseline evaluate analysis `probability-cd8277b50802c4f69d7942fd`, source revision `ba981b4f91583158af584768034aa30455f233d8bd199adf885ed01d98830427`, scenario hash `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0118d7f733ac72e43848d01b34d15553d43e248cd611681661c678c191ffd80/a15263dcc01c4ce82bf68a08edc37e9e04b2782c4d84530d828dd53a49d19410/probability-cd8277b50802c4f69d7942fd.json`.
- Baseline ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25b880b8ed035c3aaa4ca1282759a71119faca392dd1338afc66dfcbb9e85348/a11c9b4bb49740756471bc10092a97ff565b10706010478574c69696288ca443/probability-probability-cd8277b50802c4f69d7942fd-ranking.svg`; matrix SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bf2d4cbf2aa71dd7884e57b4463b554885f1a9deac7aad5c96a05a737baa3ab/88c0a9441558e29ce8c3d079e20461a95d18489dc869a34cbc493360a69e623a/probability-probability-cd8277b50802c4f69d7942fd-matrix.svg`; unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42bf9f36e8392c1f1be2da9a3edd5c8389569094835698251c534b1df8e288e2/7712fba1acb5727fa5ebc691c5ab4cf79b23e4a7f34f78670f23f22b2d1f459f/probability-probability-cd8277b50802c4f69d7942fd-unresolved.svg`.
- Final full-pool inspect revision `0e9374e2be75ba50ae12855d141a149762f3c977ed53e8a820c9e1add3f6e69b`, source hash `e66e2e4907970ec6a1d18386906f49f7b371bd14bb65835a905c7bb6c52e72f6`, pool complete for all 29 supplied ids, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1614e2bdd32761641875824b83e4cae1fc467f5b4f023ec0c8d945d5d6492bc/e21d2546dc7629193f5d50740988ace3c5d662a258c4f4d2ff3c3de3e54ca9b0/probability-inspect-e66e2e490797.json`.
- Final evaluate analysis `probability-8c49b08b88dcfd5e01b9c09a`, source revision `333af6a6af5acff98596e2e5ecc54de704dba9dbd974d621b27c356b50d07d34`, source hash `e66e2e4907970ec6a1d18386906f49f7b371bd14bb65835a905c7bb6c52e72f6`, scenario hash `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59820141cab9c6c5a3d52dc826aa87ff6d9b90850753c153a6fd690df1a5fd2f/a1c9b024dd1a6097c58e592996fa593674158da600eeda5c013876c92085e801/probability-8c49b08b88dcfd5e01b9c09a.json`.
- Final ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e46c2a282eae40a6996c3beba6009ae2128f84f8c97c7e1beae8a094c4ec4d19/b9c6a753d50899cb6a1fd18f5302026fdae84e6b1f487b317037a51debf17766/probability-probability-8c49b08b88dcfd5e01b9c09a-ranking.svg`; matrix SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee4a5e03a546bf424f296ea30b01ec3fb21b7bbfb34afa9dd8b7223927eb3066/d2a9de57f225f41daf06047d0720b21ab7d4437804732820d05d1e672dc7cd43/probability-probability-8c49b08b88dcfd5e01b9c09a-matrix.svg`; waterfall SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62eeb63150710d9df5b7dc3133dae4ad6701827c0f0c5182e91359455e3dd317/723a45d88121d8264879a3a24465c68b4de41adccdb61ec85dda59eef431f671/probability-probability-8c49b08b88dcfd5e01b9c09a-waterfall.svg`; unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7562b0aa3b2dc272c5941d7f29b6577fbea323894c49d968449802dbff783a43/54ce3b26c6743470b666fa15a1f8e01fdefa07f6f3333c2951861e5a2b44a751/probability-probability-8c49b08b88dcfd5e01b9c09a-unresolved.svg`.
- Final sweep analysis `probability-31ed15fa3afcf10fb504ae1b`, source revision `0faf7b51f40caef24e71e9f1c98d16c767c63f8c1e527681f74f7576543ab468`, source hash `e66e2e4907970ec6a1d18386906f49f7b371bd14bb65835a905c7bb6c52e72f6`, scenario hash `ed0b83aa53585a10d655480b49e8384738739dd67cdc1b3c88d94c450f0746e2`, 5 sweep points and 406 unresolved, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cda57cbfb5ef05a1edc147f8ce7e04ade5b96dd882a950c2f2b6572ea7a0ca64/2a8fddde8324586202a6e51ea2f21031d3228eb8acdd74f5bda98f555d144147/probability-31ed15fa3afcf10fb504ae1b.json`.
- Final sweep ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c993584795fd0a3c51a6be105cb6167f843ea5f26dde57700712de77cd1a1bb/679dfba36e4c442bcc4179dba0de64f0ff61d8286ea5ae16619610f9d03f6c0f/probability-probability-31ed15fa3afcf10fb504ae1b-ranking.svg`; sensitivity SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c392e84a1544dfe39bf0940afbc676352634343495221cff08f51da682fbd00/4bb872ca2bbac08a27863bc167fc77a608b3fce84d8fd82e3bb5aaa5c464bfff/probability-probability-31ed15fa3afcf10fb504ae1b-sensitivity.svg`; threshold SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/ecc6adadeffffdd9c60248f8ef6ec862964c48eb553715ef6bf6ce774dc3aa86/probability-probability-31ed15fa3afcf10fb504ae1b-threshold.svg`; unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d1ef8fb1ae582be31894f1b2ef5a83214792914f59d11bab100616925fd2180/331fadfea9c4d0c3fcacbc5f54778b83786fc8a46d8e211d2f0d6143d6452399/probability-probability-31ed15fa3afcf10fb504ae1b-unresolved.svg`.
- Related strategy inspect revision `727bc3a4766d821681c505659655ff2cb303c1e0fba3b5122f8c1712d6e6a7b5`, source hash `6a23f1d4d2e8ecfb212c50f7d555733ed070e9e910cdde6d38d9aa112cd2aafd`, zero candidates, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46698fddad7637afa5c9d88ec603130bf3230f9eb01e58e42f30f369cc68bb25/717fc96f7180ac9d398e3537c6cf0660daf1bcc4e14a1d88ae65c96852fda8aa/probability-inspect-6a23f1d4d2e8.json`.
- The prior FC30 matched-compare attempt returned no artifact and no comparison id: `PROBABILITY_SURFACE_EMPTY`, `No weighted blocks matched this request`, with `before.path` set to the frozen `docs/plans/.../ai_evidence/genocide_crisis_decisions_pre_edit_2026-09-26.txt`.

### Current compact national-order source: raw SHA256 `53687EFA480D162B27C89895269984B74F7D474CABB76F5E022225630C41B237`, MCP source hash `bb8a5c42c6c0a95f78d67d10eb074958fab35c2d5a347af5413878c3e04cc8db`

- Full-pool inspect revision `3efb3b80aa0bdceab80fbc9a0ffa6af2d1607163e6624493f66086b9023946f8`, `poolComplete=true`, 29 supplied candidates, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19717c79a892750544637f4d97bca349f21c74422fa4116085747a6c743df5ee/cde95eed833b117899b6e39b3b808e6b13a981d54e6aa4e02be2b7c261078b2b/probability-inspect-bb8a5c42c6c0.json`.
- Evaluate analysis `probability-d7f3e4430944cddd23357120`, source revision `833f95d41754ab0a4e3198dfbed2607ab653f8e9bd8818e4337e77410a0933c5`, scenario hash `41e48088659f4bbaf7fbd84b1974491d9d9004e028b1fe399fa081df13516c94`, 6 scenarios, 174 candidate-scenario rows, 494 unresolved, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bafba2ad030d53235041b3ce9140f84248bad0ff1da7651da78b8cb580c76c7f/6913e5cb3dc878825e71c9453451f0923bf2e0ff2de78ecf99bc80aa2e01c8ac/probability-d7f3e4430944cddd23357120.json`.
- Rendered evaluation views: ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/074c319f4b31b2448fef1b070563f16eb194bb4c7df4624804b5259e5d9c611e/8c81cf294615dc39cd176fea783112f6e9c5dd1b9f83f743e4b06a28687af39f/probability-probability-d7f3e4430944cddd23357120-ranking.svg`; matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee4a5e03a546bf424f296ea30b01ec3fb21b7bbfb34afa9dd8b7223927eb3066/20268a92e42dfa8dcedb841a23af9deda414b5c0f4a137fb627a9508f695bb7c/probability-probability-d7f3e4430944cddd23357120-matrix.svg`; waterfall `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62eeb63150710d9df5b7dc3133dae4ad6701827c0f0c5182e91359455e3dd317/39ffa0e202cd02a7487be26fe52e49fe0d4df81e087c14610fc6ddda89d91ee4/probability-probability-d7f3e4430944cddd23357120-waterfall.svg`; unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7562b0aa3b2dc272c5941d7f29b6577fbea323894c49d968449802dbff783a43/7cb8776f6323a9278b9381d6bb927759c494a389fca14868de2fbc11bf9ec61e/probability-probability-d7f3e4430944cddd23357120-unresolved.svg`.
- Sweep analysis `probability-6514c0ad7a01208c6a48af30`, source revision `833f95d41754ab0a4e3198dfbed2607ab653f8e9bd8818e4337e77410a0933c5`, scenario hash `ed0b83aa53585a10d655480b49e8384738739dd67cdc1b3c88d94c450f0746e2`, 5 sweep points, 145 candidate-scenario rows, 406 unresolved, JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a223c13c43027b8983ed91806b39d46763f69426546c02427f5cc2ec0505c9a/66f4cbad76b3d365ae9b6c4dcf60b173b7c4352fd1550bc713faac16dddb5e38/probability-6514c0ad7a01208c6a48af30.json`.
- Rendered sweep views: ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f3742a97483aef89439a888696fa98a78cadb1abe3d6bc7ee08c433f935c579/9319273b6d87184ab214b022224e90c231df89e1692b19e90fe85991ca2d8f3e/probability-probability-6514c0ad7a01208c6a48af30-ranking.svg`; sensitivity `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c392e84a1544dfe39bf0940afbc676352634343495221cff08f51da682fbd00/c09c08d4ec57d96cfac71099fa2ecc278d02aa64ad1c7cfaec744ac64b0088a1/probability-probability-6514c0ad7a01208c6a48af30-sensitivity.svg`; threshold `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/12f9d99f778336e4e05fc983423b3d7a04cbad35df441a4221c4d80259b9510d/probability-probability-6514c0ad7a01208c6a48af30-threshold.svg`; unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d1ef8fb1ae582be31894f1b2ef5a83214792914f59d11bab100616925fd2180/cfb6dc71166456e6d4bcf7cda8943ed7fe732db3cee0f6a51460e578764215b1/probability-probability-6514c0ad7a01208c6a48af30-unresolved.svg`.
- Matched compare attempted against the exact frozen pre-edit snapshot and this source with the same six-scenario hash and 29-id pool; MCP returned `PROBABILITY_SURFACE_EMPTY`, `No weighted blocks matched this request`, no comparison id, and no numeric delta.

## References and skills

Offline wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding; the decision AI and MTTH block sections were used to distinguish willingness weights from probability-proportional `ai_chance`.

Vanilla documentation consulted: `documentation/effects_documentation.md` (`activate_decision`), `documentation/triggers_documentation.md` (`has_decision`), and the relevant modifier/trigger/effect references used while tracing the decision contract.

Skills applied: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth`.

## Simplifications, omissions, and blockers

Exact click probability, per-scenario final eligibility, numeric before/after delta, rank reversal, starvation, dominance, and repeated-decision sequence remain unresolved because the adapter cannot bind typed variables and helper scopes from the flat fixture and cannot read the frozen baseline at its documentation path.

No gameplay files were changed by this auditor. No tests or live-game validation were run.

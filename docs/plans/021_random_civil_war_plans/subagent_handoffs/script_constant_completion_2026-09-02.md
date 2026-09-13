# Event 021 script constant completion handoff

Date: 2026-09-02.

Owner: `chaosx_scripted_system_architect` replacement work after the prior worker was authoritatively `not_found`.

## Scope and completion

The exclusive write set for this handoff was `common/script_constants/021_random_civil_war_constants.txt` and this handoff file.

The constants table now declares every filtered `constant:event021_*` and `constant:random_civil_war_*` key referenced by `common/` and the pre-existing `docs/` surfaces.

The missing-key result is zero missing occurrences and zero missing unique keys in the post-patch audit.

The post-patch audit also found zero duplicate declarations for the Event 021 and Random Civil War categories.

`event021_action_tuning` was corrected from `data = int` to `data = fixed_point` because its existing stability gains and the new organization and supply-consumption modifiers contain fractional values.

The pre-existing `random_civil_war_target_weight.major_target_factor = 0.35` and the full `random_civil_war_evolution_mtth` additions were preserved unchanged.

No gameplay, decision, effect, trigger, localisation, spreadsheet, or other non-exclusive file was edited, and no commit was made.

## Audit snapshots

The audit parses all script-constant declarations under `common/script_constants/` and matches them to filtered constant tokens under `common/` and `docs/`.

| Snapshot | Filtered occurrences | Unique tokens | Missing occurrences | Missing unique tokens |
| --- | ---: | ---: | ---: | ---: |
| Before this constants patch, after the parent-owned caller, host-predicate, achievement, and opening-receipt edits visible at that time | 1,462 | 487 | 500 | 231 |
| After the constants patch, using the then-current source tree | 1,531 | 487 | 0 | 0 |
| Latest observed full audit after the provenance update, including the current source tree and documentation references | 1,842 | 487 | 0 | 0 |

The occurrence total increased by 69 while the parent-owned source was changing concurrently; the unique inventory stayed at 487 and the final missing result is based on the current tree, not on a stale pre-parent snapshot.

The latest observed total is 1,553 matches under `common/` and 289 matches under `docs/`; the additional 311 matches relative to the earlier post-patch snapshot reflect continued parallel source and handoff changes, while the unique inventory and zero-missing result remain unchanged.

The 231 newly declared keys are distributed as follows: `event021_action_cost` 52, `event021_action_tuning` 28, `event021_ai` 1, `event021_anchor_weight` 15, `event021_evidence_tuning` 7, `event021_mission_tuning` 1, `event021_parent_tuning` 58, `event021_same_tag_tuning` 19, `event021_scheduler` 5, `event021_settlement_obligation` 6, `random_civil_war_cluster_skip_reason` 10, `random_civil_war_evidence_source` 11, `random_civil_war_evidence_strength` 2, `random_civil_war_force` 3, `random_civil_war_front_goal` 5, `random_civil_war_front_status` 1, and `random_civil_war_log` 7.

## Numeric provenance boundary

The specifications provide several constraints and reference bands, but they do not provide a complete literal numeric table for the missing declarations.

The directly prescribed contracts in this patch are the engine/data contracts and consumer invariants: `event021_action_tuning` must be `fixed_point` because fractional values are consumed; scheduler and array cursors start at zero under the zero-based array contract; `none = 0` is retained where an empty enum state is stored; enum codes are unique because consumers compare them for equality; and resource gate/spend pairs have matching positive-check and negative-spend signs.

The specifications constrain, but do not uniquely prescribe, the selected balance values: settlement and receipt durations use the documented 90/180-day windows; cluster batches use the documented seven-day upper bound; actor size remains below one-half; and force shares follow the documented limited/serious/severe/critical progression and approximate low/medium/high share anchors.

The remaining numeric values are inferred owner choices from current consumers, existing Event 021 ladders, vanilla or Chaos Redux precedents, and unit conversions. This includes action costs, viability thresholds, anchor weights, same-tag weights, secondary-front allocations, `target_pool_weight_scale = 100`, `target_pool_weight_cap = 10`, and the sponsor/incident tuning. They are not being presented as literal prose-spec numbers.

The pre-existing `major_target_factor = 0.35` and the source-level strange-incident pair `.08/.92` with `-3/+4` effects were preserved, not re-derived here. The `.08` probability is therefore an inherited owner choice rather than a spec-prescribed probability, and it remains subject to the required weighted comparison.

## Exact enum contracts

The consumers use equality comparisons for these categories rather than arithmetic ranges.

The assigned codes are therefore stable, distinct internal codes with `none = 0` wherever the consumer records an explicit empty state.

There is no unresolved enum contract after the audit.

| Category | Declared codes |
| --- | --- |
| `event021_settlement_obligation` | `none = 0`, `recognition = 1`, `disarmament = 2`, `rail_security = 3`, `sponsor_repayment = 4`, `coalition_governance = 5` |
| `random_civil_war_cluster_skip_reason` | `none = 0`, `no_eligible_actor = 1`, `no_eligible_target = 2`, `role_collision = 3`, `tag_occupied = 4`, `state_reservation_failed = 5`, `cap_reached = 6`, `generation_blocked = 7`, `stale_delayed_reservation = 8`, `package_incomplete = 9` |
| `random_civil_war_evidence_source` | `political = 1`, `legal = 2`, `regional = 3`, `command = 4`, `event006 = 5`, `same_tag = 6`, `external_war = 7`, `fury = 8`, `neighbor = 9`, `sponsor = 10`, `settlement = 11` |
| `random_civil_war_evidence_strength` | `credible = 1`, `acute = 2` |
| `random_civil_war_front_goal` | `ideological_change = 1`, `constitutional_restoration = 2`, `regional_recognition = 3`, `command_seizure = 4`, `independence = 5` |
| `random_civil_war_front_status` | `active = 1` |
| `random_civil_war_log` | `opening = 1`, `multi_front = 2`, `exposure = 3`, `settlement = 4`, `reconstruction = 5`, `evolution_iii = 6`, `failed_opening = 7` |

## Added declarations and values

### Action costs

All gate and spend pairs use the existing Event 021 sign contract: a positive gate checks availability and the matching negative spend is applied on completion.

`event021_action_cost` additions are `border_command_power_gate = 10`, `border_command_power_spend = -10`, `border_trucks_gate = 10`, `border_trucks_spend = -10`, `border_convoys_gate = 5`, `border_convoys_spend = -5`; `integration_army_xp_gate = 10`, `integration_army_xp_spend = -10`, `integration_infantry_gate = 150`, `integration_infantry_spend = -150`, `integration_manpower_gate = 1000`, `integration_manpower_spend = -1000`; `government_support_political_power_gate = 20`, `government_support_political_power_spend = -20`, `government_support_infantry_gate = 150`, `government_support_infantry_spend = -150`, `government_support_infantry_transfer = 100`, `government_support_convoys_gate = 5`, `government_support_convoys_spend = -5`; `opposition_support_political_power_gate = 20`, `opposition_support_political_power_spend = -20`, `opposition_support_infantry_gate = 150`, `opposition_support_infantry_spend = -150`, `opposition_support_infantry_transfer = 100`, `opposition_support_convoys_gate = 5`, `opposition_support_convoys_spend = -5`; `mediation_political_power_gate = 20`, `mediation_political_power_spend = -20`, `mediation_command_power_gate = 10`, `mediation_command_power_spend = -10`, `mediation_convoys_gate = 5`, `mediation_convoys_spend = -5`; `disengage_political_power_gate = 15`, `disengage_political_power_spend = -15`, `disengage_command_power_gate = 10`, `disengage_command_power_spend = -10`; `disarmament_army_xp_gate = 10`, `disarmament_army_xp_spend = -10`, `disarmament_infantry_gate = 100`, `disarmament_infantry_spend = -100`, `disarmament_manpower_gate = 500`, `disarmament_manpower_spend = -500`; `prevention_political_power_gate = 15`, `prevention_political_power_spend = -15`, `prevention_manpower_gate = 500`, `prevention_manpower_spend = -500`, `prevention_command_power_gate = 10`, `prevention_command_power_spend = -10`, `prevention_trains_gate = 1`, `prevention_trains_spend = -1`; and `priority_command_power_gate = 10`, `priority_command_power_spend = -10`.

These values reuse the already established Event 021 low, medium, and high political-power hint bands, the existing command-power, infantry, manpower, truck, train, and convoy tiers, and the corresponding material/action families in `012_africa_action_constants.txt` and `039_murder_mystery_constants.txt`.

### Action and mission tuning

`event021_action_tuning` additions are `arsenal_authority_gain = 5`, `arsenal_pressure_relief = -8`, `border_authority_gain = 4`, `border_pressure_relief = -6`, `depot_army_organization = 0.10`, `depot_effect_days = 45`, `depot_supply_consumption = -0.10`, `disarmament_authority_gain = 6`, `disarmament_pressure_relief = -10`, `disengage_authority_gain = 3`, `disengage_pressure_relief = -6`, `hardliner_authority_cost = -4`, `loyalty_authority_gain = 5`, `loyalty_pressure_relief = -6`, `maximum_infrastructure = 5`, `mediation_authority_gain = 5`, `mediation_days = 90`, `mediation_pressure_relief = -8`, `opposition_support_authority_cost = -4`, `prevention_authority_gain = 4`, `prevention_pressure_relief = -5`, `priority_authority_gain = 3`, `priority_pressure_relief = -4`, `rail_train_recovery = 1`, `relief_authority_gain = 5`, `relief_pressure_relief = -8`, `sponsor_commitment_days = 90`, and `sponsor_support_amount = 100`.

`event021_mission_tuning.settlement_terms_days = 180` completes the settlement mission timeout.

`event021_ai.exposure_mediator_stability = 0.65` preserves the stability boundary recorded by the prior probability handoff and matches the existing `strong_neighbor_stability_threshold` scale.

The action gains and relief values use the existing Event 021 authority/pressure magnitudes as the ladder: major capital and reconstruction actions remain stronger, logistics and prevention actions remain moderate, and disengagement and priority selection remain lighter.

The duration values follow the Part 3 settlement window, Part 5 bounded exposure window, and the existing 30/45/60/90/120/180-day Event 021 cadence families.

### Anchor and evidence tuning

`event021_anchor_weight` uses `data = int` and declares `base = 10`, `population_medium_k = 1000`, `population_medium = 8`, `population_dense_k = 10000`, `population_dense = 12`, `civilian_factory = 8`, `military_factory = 10`, `infrastructure_good = 3`, `infrastructure = 6`, `supply_node = 12`, `naval_base = 8`, `coastal = 4`, `core = 8`, `capital = 20`, and `maximum = 100`.

The values follow the source scoring order and keep capital, supply, industry, and population meaningful without allowing one feature to exceed the existing 100-point clamp.

`event021_evidence_tuning` uses `data = int` and declares `route_receipt_days = 180`, `external_war_receipt_days = 180`, `fury_receipt_days = 180`, `neighbor_receipt_days = 90`, `sponsor_receipt_days = 90`, `minimum_live_strength = 1`, and `receipt_cleanup_owner = 21`.

The receipt durations follow the existing 180-day event memory and the shorter 90-day relationship/exposure windows; `credible = 1` and `acute = 2` make the minimum live strength gate monotonic.

The cleanup owner marker is the Event 021 id because the current consumer only checks that the marker exists; no current cleanup consumer compares it to another registry.

### Parent, same-tag, scheduler, and force tuning

`event021_parent_tuning` uses `data = fixed_point` and declares `front_id_seed = 1`, `event6_generation_seed = 0`, `minimum_state_population_k = 5`, `minimum_context_population_k = 500`, `minimum_political_authority = 25`, `weak_manpower_gate = 5000`, `minimum_administration_factories = 2`, `nested_generation_minimum = 1`, `minimum_belligerents = 2`, `maximum_major_belligerents = 5`, `maximum_minor_belligerents = 3`, `minimum_actor_size = 0.05`, `maximum_actor_size = 0.45`, `minimum_air_navy_share = 0.05`, `limited_army_share = 0.15`, `limited_stockpile_share = 0.10`, `limited_navy_share = 0.05`, `limited_air_share = 0.05`, `serious_army_share = 0.25`, `serious_stockpile_share = 0.20`, `serious_navy_share = 0.10`, `serious_air_share = 0.10`, `severe_army_share = 0.35`, `severe_stockpile_share = 0.30`, `severe_navy_share = 0.15`, `severe_air_share = 0.15`, `critical_army_share = 0.45`, `critical_stockpile_share = 0.45`, `critical_navy_share = 0.25`, `critical_air_share = 0.25`, `local_units_army_bonus = 0.10`, `command_army_bonus = 0.10`, `command_navy_bonus = 0.05`, `command_air_bonus = 0.05`, `ideological_affinity_army_bonus = 0.05`, `regional_support_army_bonus = 0.05`, `depot_army_bonus = 0.05`, `depot_stockpile_bonus = 0.10`, `arsenal_stockpile_bonus = 0.10`, `local_support_stockpile_bonus = 0.05`, `external_war_army_penalty = -0.05`, `external_war_stockpile_penalty = -0.10`, `poor_equipment_army_penalty = -0.10`, `secondary_front_size = 1`, `secondary_front_minimum_states = 1`, `secondary_front_army_share = 0.15`, `secondary_front_navy_share = 0.05`, `secondary_front_air_share = 0.05`, `settlement_terms_hold_days = 180`, `same_tag_deadline_days = 30`, `cluster_reservation_valid_days = 7`, `scheduler_registration_samples = 4`, `target_pool_weight_scale = 100`, `target_pool_weight_cap = 10`, `strange_incident_probability = 0.08`, `strange_incident_no_probability = 0.92`, `strange_incident_authority_loss = -3`, and `strange_incident_pressure_gain = 4`.

The force ladder follows the specification's limited/serious/severe/critical progression, the existing 0.25/0.30/0.20 actor ratios, the requirement that a split stay below half-country size, and the bounded regional secondary-front direction.

The scheduler values reuse the existing capacity batches: four registration samples, six review entries, and three critical entries; the zero cursors match the documented zero-based array contract.

The target weight scale of 100 maps the 0-1000 score range to a bounded one-to-ten ticket range, matching the existing individual-crisis ticket curve and the bounded ticket caps used by other Chaos Redux pools. This is an inferred owner choice, not a literal balance number from the specification.

With source score `S`, the pre-adjustment ticket counts are `max(1, min(10, round(S / 100)))` for a normal target and `max(1, min(10, round(0.35 * S / 100)))` for a major target. For example, a normal score of 100 and a reduced major score of 35 both resolve to one ticket after the lower clamp, and the lower score bands overlap more broadly at that floor. This is a known quantization risk; `major_target_factor = 0.35`, scale 100, and cap 10 were not silently retuned, and no balance success is claimed from the constants-existence patch.

`event021_same_tag_tuning` uses `data = fixed_point` and declares `minimum = 0`, `maximum = 100`, `government_base = 50`, `claimant_base = 50`, `authority_share = 0.50`, `pressure_share = 0.50`, `arsenal_gain = 5`, `capital_gain = 10`, `loyalty_gain = 5`, `integration_gain = 8`, `priority_gain = 3`, `settlement_claimant_gain = 10`, `mission_government_gain = 8`, `mission_claimant_gain = 8`, `capital_node = 20`, `supply_node = 12`, `rail_node = 10`, `naval_node = 8`, and `depot_node = 8`.

The same-tag values create a symmetric 0-100 leverage contest, give the capital and settlement meaningful leverage, and reuse the anchor's supply/rail/naval/industry hierarchy.

`event021_scheduler` declares `first_array_index = 0`, `initial_review_cursor = 0`, `initial_critical_cursor = 0`, `maximum_review_scan = 6`, and `maximum_critical_scan = 3`.

`random_civil_war_force` adds `infantry_equipment_per_division = 100`, `support_equipment_per_division = 25`, and `artillery_equipment_per_division = 10`, matching the existing minimum package checks.

## Unresolved tuning ambiguity and risk register

The missing-key problem is resolved, but several numeric choices are implementation-complete tuning decisions rather than literal values stated in the prose specifications.

There are 9 unresolved tuning groups for parent-owner confirmation; none leaves a missing token or an undefined default.

| Group | Selected values | Basis | Risk if the intended design differs |
| --- | --- | --- | --- |
| Action economy and leverage | The 52 cost keys above; the 28 action gains/reliefs; same-tag gains | Existing Event 021 costs, AI hint bands, Africa action tiers, Murder Mystery action patterns, and the current authority/pressure ladder | A too-cheap support, mediation, or prevention action can be farmed; a too-expensive action can make a route invisible to the AI or player |
| Viability thresholds | `minimum_state_population_k = 5`, `minimum_context_population_k = 500`, `minimum_political_authority = 25`, `weak_manpower_gate = 5000`, `minimum_administration_factories = 2` | Existing Event 006-style five-thousand-person state floor, Event 021 political-power tiers, the existing one-thousand-manpower minimum, and small administration viability | Population and manpower units are source-derived but not all literal thresholds are specified, so country eligibility may be too broad or too narrow |
| Actor size and severity ladder | `minimum_actor_size = 0.05`, `maximum_actor_size = 0.45`; limited `.15`, serious `.25`, severe `.35`, critical `.45` army shares; matching stockpile and arm shares | Part 4/8 limited-war and below-half-country requirements plus the existing force-ratio family | Critical plans may be capped at 45% and a large country may receive a weaker or stronger opening than intended |
| Secondary front allocation | `secondary_front_size = 1`, army `.15`, navy `.05`, air `.05`, minimum states `1` | Source requires a bounded regional actor and checks more than one controlled state; the one-state size is the smallest valid split | Secondary fronts may be too small to matter or may consume too much of the host's force/territory |
| Anchor score ladder | Population thresholds 1000/10000; base 10; feature weights 3-20; maximum 100 | The source scoring order, the existing population-in-thousands representation, and a bounded weighted-state precedent | Capitals, hubs, or dense states may dominate anchor selection more or less than intended |
| Target ticket conversion | `target_pool_weight_scale = 100`, `target_pool_weight_cap = 10` | Existing 0-1000 target score, individual-crisis load/ticket curve, and bounded ticket caps in other pools | The live global candidate pool is incomplete, so exact target-selection shares remain uncertified and the scale/cap may need comparison tuning |
| Receipt duration and ownership marker | Route/external/Fury 180 days; neighbor/sponsor 90 days; cleanup owner 21 | Existing event memory and cadence windows; current cleanup trigger only requires presence | A stale receipt could persist too long, or a future cleanup registry could require an owner identity other than the Event 021 id |
| Same-tag contest | Symmetric bases 50/50, half authority/pressure shares, 0-100 clamp, node weights and gains above | Same-tag route requires a meaningful contest without a duplicate tag; values reuse anchor/action ordering | The government or claimant can become too dominant before objective resolution |
| Sponsor and incident tuning | `sponsor_support_amount = 100`, `sponsor_commitment_days = 90`, incident `.08/.92`, authority `-3`, pressure `+4` | Sponsor amount matches the 100-unit transfer tier and a bounded exposure commitment; the incident values are inherited from the prior handoff, not literal prose-spec balance targets | Sponsor aid may be too weak/strong or too short/long; the inherited incident probability still needs the required live probability comparison |

The enum choices do not have a corresponding unresolved numeric risk because every current consumer compares an enum value for equality and the codes are unique.

## Validation and evidence

The required offline Paradox wiki pages were consulted before source work, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The installed vanilla documentation consulted included `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md`.

The Event 021 specifications read for this pass were Parts 3, 4, 5, 6, 7, 8, and 10, together with the master and coding/spec handoff files.

The read-only Event MCP lint was refreshed against `chaosx.nr21.1` after the constants patch.

The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e82c9473892df0b9abeb55a1880b07868803580937880a8b885e7571288f6b6/2b141ded07009c8e262ef41f03b11a2380aae9b429ec5f22d41a8b5fe1916287/event-lint-23d07f38466b.json`.

The lint report returned no blocking diagnostics but marked workspace-wide analysis partial because large helper projections were deferred; it is supporting engine evidence, not a substitute for the source token audit.

The required probability discovery began with `hoi4.probability_inspect` on `common/scripted_effects/021_random_civil_war_parent_effects.txt` and discovered the `random_list` adapter with eight source candidates and no unresolved inputs.

The baseline artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/834199001f6e4f5e8a2719deacf7faa4a0bf8242c5dc2f80e1cc9d4d7be96c91/2c5f6123a88116cc1e0cf2c4fd23cd3c19d2783378d010dbee845d852c6e5d22/probability-inspect-a6cad28c99d0.json`.

The post-patch probability auditor completed five read-only `hoi4.probability_compare` attempts, but no valid comparison artifact or comparison ID was produced. Two artifact-backed surfaces returned `PROBABILITY_SURFACE_EMPTY`; the decision and archetype source-backed attempts returned `PROBABILITY_SOURCE_STALE` because the expected pre-patch hashes (`e21827…` and `7233eb…`) did not match the current hashes (`3851afb4…` and `62db0021…`); and a direct artifact-field attempt was rejected with `MCP error -32602: Unrecognized key: "artifactUri" at before`.

The auditor's comparison baseline artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/650ca21460e2ecf576c7ab5c3ee213fa8b2a6a21da993ff7b379443097ea1bb7/2c4245dc435a13d412bf72089607095e62a9e2b84127851c9d8baadd196903d8/probability-52128419efbbfa9b1ca77dcf.json`, using scenario set `event021_sponsor_ai_matrix_2026_09_02` with `SPN-01` through `SPN-05` and all 18 Event 021 decisions as the candidate pool. Refreshed inspections found complete pools with zero unresolved inputs for 18 decisions, 3 missions, 6 archetype outcomes, and 2 strange-incident outcomes, but the MTTH adapter discovered no candidate.

No exact live target-pool probability, scale/cap comparison, incident-rate result, or balance-success claim is made here. The baseline discovery and the constants existence/type audit do not resolve the one-ticket quantization risk above; the valid compare remains pending a stable readable before/after source pair and supported input schema.

The full missing-token audit is the completion proof for this constants-only task; the game was not launched, and no live save or runtime fixture was claimed.

## Follow-up boundary

The parent should confirm the nine tuning groups above during the existing probability, engine-matrix, and runtime-sequence review.

The shared `individual_crisis_candidate` adjustment helper remains outside this exclusive write set; its absence is a separate parent-owned helper issue and was not hidden by adding a duplicate Event 021 fallback.

No gameplay simplification or fallback was introduced by this constants completion.

# Event 021 scenario ticket-count ordering repair

Status: implemented.

Date: 2026-09-06.

Owner: parent implementation pass.

The manual low, medium, and high scenario builder now increments `global.random_civil_war_scenario_eligible_count` only after `adjust_individual_crisis_candidate_ticket_weight` produces a positive adjusted ticket weight.

This keeps the unique eligible-country budget aligned with the actual bounded scenario target pool when the shared individual-crisis load cap removes a candidate.

The maximum-intensity branch remains intentionally separate and continues to freeze `event021_parent_scenario_target_pool` from `event021_parent_scenario_country_eligible` before committing every eligible normal human country.

Changed source: `common/scripted_effects/021_random_civil_war_parent_effects.txt`, `event021_parent_add_scenario_target_to_weighted_pool`.

The source change was reviewed against the shared candidate-ticket contract in `common/scripted_effects/individual_crisis_targeting_effects.txt` and `common/scripted_triggers/individual_crisis_targeting_triggers.txt`.

The fixed-target companion `apply_individual_crisis_fixed_target_event_pressure` remains unresolved because the shared documentation does not define its inputs, output variable, or caller transaction, so this repair does not alias or invent that adapter.

Validation scope: source inspection and targeted syntax hygiene are required after this patch; MCP event and probability evidence remains partial and does not certify live scenario execution.

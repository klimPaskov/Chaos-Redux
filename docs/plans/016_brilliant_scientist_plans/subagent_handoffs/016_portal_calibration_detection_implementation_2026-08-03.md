# Event 016 portal calibration and detection implementation

Date: 2026-08-03

Status: bounded gameplay tranche implemented; no models, CBRN callbacks, new event IDs, or spreadsheet rows added.

## Scope

The accepted Electronics plus Teleportation synergy is now a one-time Directorate decision in `brilliant_scientist_directorate_category`:

- Decision: `brilliant_scientist_establish_portal_calibration_network`
- Readiness: `brilliant_scientist_portal_calibration_network_is_ready`
- Cost gate: `brilliant_scientist_can_pay_portal_calibration_network`
- Completion effect: `brilliant_scientist_complete_portal_calibration_network`
- Resolution validation: `brilliant_scientist_portal_calibration_network_resolution_is_valid`
- Active consumer reader: `brilliant_scientist_portal_calibration_network_is_active`
- Persistent country receipt: `brilliant_scientist_portal_calibration_network_established`
- Kruger character history: `brilliant_scientist_personal_portal_calibration_network_established`

The decision requires Electronics and Teleportation at Prototype in the canonical stage array, valid primary and secondary facilities, an idle project board, healthy and non-stolen ledgers, no containment action, and no terminal or world-end lock. It commits 85 Political Power, 250 Support Equipment, 125 Motorized Equipment, 2,000 fuel, 2,500 manpower, and two civilian factories for 150 days. The transaction grants no stage, capacity, equipment, terminal, division, event-log entry, or new project family.

## Consumers

`brilliant_scientist_refresh_project_accident_pressure` subtracts the fixed calibration reduction only for a healthy Teleportation family on a current host with both physical facilities. `brilliant_scientist_foreign_calculate_operation_outcome` applies the success penalty and detection increase only when the host's active receipt exists and the actor selected Teleportation; existing probability clamps and operation ledgers remain authoritative.

## Transfer and cleanup

An unfinished decision is cleared by transfer, containment, facility loss, project incident, terminal commitment, or world end without refund. The former host loses its live receipt during `brilliant_scientist_reconcile_old_host_after_transfer`. A completed receipt is retained on Kruger, restored on an ordinary recipient from character history, and copied through the fixed-tag formation snapshot. The Kruger State preserves the history but receives no free terminal and cannot activate the current-host countermeasure without the normal facility and project-health checks. The completed history is not removed by terminal cleanup; only unfinished transaction flags are cleared.

## Files changed

- `common/decisions/016_brilliant_scientist_directorate_synthesis.txt`
- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/script_constants/016_brilliant_scientist_foreign_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/projects.md`

## Validation and limits

Targeted identifier scans confirm every decision, trigger, effect, receipt, character-history, transfer, formation, accident, foreign-score, and localisation reference has a source definition or consumer. The touched Clausewitz files were checked for balanced braces and unsupported `<=` or `>=` operators, and the Event 016 localisation file retains UTF-8 BOM encoding with no duplicate keys. No Hearts of Iron IV process was launched; live decision timing, AI selection, transfer scenarios, and probability normalization remain user-owned acceptance work.

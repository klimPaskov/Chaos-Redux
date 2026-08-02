# Event 016 high-speed materials trial implementation handoff

Date: 2026-08-03

## Scope

Implemented the accepted `016_high_speed_materials_trial_addendum_2026-08-03.md` as one bounded Advanced Materials plus Rocketry project-portfolio tranche. No 3D model, CBRN callback, new country route, focus, Event Log row, or catalog row was added.

## Runtime identifiers

- Decision: `brilliant_scientist_prepare_high_speed_materials_trial`
- Completion event: `chaosx.nr16.195`
- Transaction flags: `brilliant_scientist_high_speed_materials_trial_pending`, `brilliant_scientist_high_speed_materials_trial_in_progress`, and `brilliant_scientist_high_speed_materials_trial_failed_ever`
- State flags: `brilliant_scientist_high_speed_test_corridor_active` and `brilliant_scientist_high_speed_test_corridor_certified`
- Persistent outcomes: `brilliant_scientist_high_speed_materials_national_board` and `brilliant_scientist_high_speed_materials_kruger_tables`
- Character history: `brilliant_scientist_personal_high_speed_materials_trial_completed` and `brilliant_scientist_personal_high_speed_materials_kruger_tables`
- Dynamic modifiers: `brilliant_scientist_high_speed_qualification_board` and `brilliant_scientist_high_speed_kruger_envelope`

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/decisions/016_brilliant_scientist_directorate_synthesis.txt`
- `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`
- `events/016_brilliant_scientist_synthesis_events.txt`
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/projects.md`
- `docs/events/016_brilliant_scientist/systems/directorate.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_3_project_portfolio.md`
- `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`

## Cost and ownership contract

The decision requires 100 Political Power, 25 Air Experience, 150 Support Equipment, 200 Motorized Equipment, 5,000 fuel, 3,000 manpower, three civilian factories, Materials Deployment, Rocketry Prototype, expanded prototype works, two valid facilities, healthy ledgers, and one owned, controlled, core, non-impassable state. It runs for 180 days. Invalidated work consumes the payment and clears the active state/global target without a refund or outcome.

The national-board option applies the documented host-only ledger vector and air-safety modifier and certifies the selected state. The proprietary option applies the documented Kruger-dependent ledger vector, range and mission-efficiency modifier, and Rocketry accident-pressure increase. Ordinary transfer clears the proprietary country receipt and restores it only from Kruger's personal history on the recipient; the national receipt remains with the former host. Fixed-tag Kruger State formation carries only the proprietary receipt and never replays costs, event effects, ledger deltas, or state selection.

## AI and presentation

The decision AI requires a reserve above payment gates and goes to zero under severe surrender pressure. War, Rocketry Deployment, and high Project Capacity increase start priority. The `.195` options use only the existing ten settlement receipts plus current Directorate meters and security/safety flags for bounded presentation choice. The event reuses `GFX_report_event_016_brilliant_scientist_breakthrough_materials_rocketry`; the decision reuses `GFX_decision_brilliant_scientist_project_rocketry_propulsion_deployment`.

## Validation and remaining risk

The parent must run targeted static syntax, brace, unsupported-operator, duplicate-localisation, BOM, and read-only Event 016 inspection for the new decision and `.195` event. The handoff does not claim live game acceptance, quantitative campaign balance, or transfer/formation scenario completion. The native CBRN lifecycle remains blocked by the missing reservation/cancel callback, and the seven generic Event 016 model packages remain deferred by user instruction.

## Parent validation record, 2026-08-03

- The eight touched gameplay files have balanced Clausewitz braces and contain no unsupported `<=` or `>=` operators.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` is UTF-8 with BOM, contains 292 unique keys, and covers the decision, delayed event, option, tooltip, and outcome identifiers listed above.
- The decision icon and `.195` report texture are registered in `interface/016_brilliant_scientist_project_icons.gfx` and `interface/016_brilliant_scientist.gfx`; both referenced DDS files exist.
- Read-only `hoi4_event_inspect` lint for `chaosx.nr16.195` returned `status = ok`, no blockers, and no blocking diagnostics. The analyzer reported only its workspace-wide helper-projection deferral (`MCP_INLINE_FILES_TRUNCATED`), so this is source-level evidence rather than live campaign acceptance.
- No HOI4 executable was launched. Quantitative balance, transfer/formation scenarios, and live user acceptance remain open by design.

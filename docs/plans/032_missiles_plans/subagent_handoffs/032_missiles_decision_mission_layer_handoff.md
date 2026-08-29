# Event 32 decision and mission layer handoff

## Scope

This handoff covers only the ordinary Event 32 decision category, its decisions, its timed missions, and their English localization.

The layer uses one ordinary category named `missiles_program_management_category`, the requested static picture `GFX_decision_cat_picture_032_missiles`, and the requested category icon `GFX_decision_category_032_missiles`.

No scripted GUI, event, scenario, achievement, spreadsheet, generated CSV, shared setting, or core Event 32 file was edited by this worker.

## Changed files

- `common/decisions/categories/032_missiles_categories.txt` defines the ordinary category and gates it through `missiles_country_can_manage_program`.
- `common/decisions/032_missiles_decisions.txt` defines the phase-gated state and country decisions, real equipment/fuel/manpower/command/experience costs, cooldowns, blocked-cost tooltips, target selection, and AI willingness.
- `common/decisions/032_missiles_missions.txt` defines survey, secondary-site construction, strike preparation, site repair, site recovery, warning verification, and retaliation-network restoration missions.
- `localisation/english/032_missiles_decisions_l_english.yml` contains only Event 32 decision, mission, cost, requirement, and effect localization and is UTF-8 with BOM.
- `docs/plans/032_missiles_plans/subagent_handoffs/032_missiles_decision_mission_layer_handoff.md` records ownership, validation, dependencies, and blockers.

## Decision surface

The implementation phase-gates the visible actions through the Event 32 phase flags.

- Establishment exposes survey and command authority.
- Maintenance exposes reserve replenishment, readiness restoration, guidance maintenance, and launch authority security.
- Expansion exposes site hardening, capacity expansion, and secondary-site construction.
- War operations expose one target selector, four strike-preparation choices, and special-payload integration, with the saturation and special-payload choices gated by their evolution flags.
- Prepared operation exposes launch and abort.
- Incident response exposes inspection, neutral compensation, and damaged-site suspension.
- Rogue command exposes emergency-code rotation, site isolation, loyal-force recovery, negotiation, and scuttling.
- Retaliation exposes warning verification, delay, network severance, site isolation, response acceptance, and network restoration.

The largest phase surfaces are six visible primary actions in war operations and six in retaliation, matching the specification maximum.

## Mission behavior

All missions are activated explicitly by ordinary decisions and use the repository’s separate mission-file convention.

Mission completion is driven by the core-owned completion flag in `available`, while cancellation and timeout both call `missiles_abort_operation` followed by `missiles_cleanup_operation`.

Strike-preparation cancellation validates the persisted selected target through `event_target:missiles_selected_target` and also cancels when that target pointer is absent.

## API contract status

The existing Event 32 trigger definitions for `missiles_country_can_manage_program`, `missiles_state_is_valid_site_target`, `missiles_country_can_prepare_operation`, `missiles_target_is_valid`, and `missiles_site_can_launch` are present in `common/scripted_triggers/032_missiles_triggers.txt`.

The following effect APIs are referenced cleanly by the layer but have no exact definitions under `common/scripted_effects` at handoff time: `missiles_replenish_reserve`, `missiles_restore_readiness`, `missiles_improve_guidance`, `missiles_secure_launch_codes`, `missiles_harden_site`, `missiles_expand_capacity`, `missiles_establish_secondary_site`, `missiles_select_target`, `missiles_prepare_precision_strike`, `missiles_prepare_strategic_barrage`, `missiles_prepare_saturation_barrage`, `missiles_prepare_counterforce_strike`, `missiles_integrate_special_payload`, `missiles_inspect_incident`, `missiles_compensate_neutral_victim`, `missiles_suspend_damaged_site`, `missiles_rotate_emergency_codes`, `missiles_isolate_site`, `missiles_send_loyal_forces`, `missiles_negotiate_with_command`, `missiles_scuttle_site`, `missiles_verify_warning`, `missiles_delay_retaliation`, `missiles_sever_network`, `missiles_restore_retaliation_network`, `missiles_abort_operation`, and `missiles_cleanup_operation`.

The layer also references `missiles_commit_operation` for launch and accepted retaliation because it is named by the Event 32 implementation contract, but that API is absent and is not in the user-supplied API list.

The core must set and clear the phase, operation, target, incident, warning, rogue-command, site, and mission-completion flags consumed by this layer, including `missiles_target_selected`, `missiles_operation_ready`, `missiles_command_control_secure`, `missiles_rogue_command_active`, `missiles_warning_active`, and `missiles_retaliation_network_severed`.

## Known integration simplifications and blockers

- Survey completion calls the supplied `missiles_establish_secondary_site` API because no dedicated primary-site or survey-resolution effect was exposed; the core owner should replace or parameterize this call if survey completion has a distinct receipt.
- Site-repair completion calls `missiles_restore_readiness` because no dedicated site-repair completion API was exposed; the core owner should add or route a site-specific repair resolution if readiness and site condition are separate records.
- The specification’s clear-target, inspect-operation, participating-site change, and warning target-change actions are not exposed as exact APIs in the requested contract, so no invented references were added.
- The requested category GFX names are referenced exactly, but no matching definitions or Event 32 art were present in the inspected repository; this worker did not edit interface or asset files.
- Cost values are file-local decision tuning because the core constants file was outside this worker’s ownership; every action remains at or below four spendable cost types and uses real game resources.
- No GUI was created, by design.

## Validation evidence

- Native decision structure was cross-checked against `029_riches_found` and targeted state-decision patterns.
- Native mission structure was cross-checked against `007_fury` and the offline Decision Modding wiki mission rules.
- The three Clausewitz source files have balanced braces and no unsupported `<=` or `>=` operators.
- Decision and mission block IDs have no duplicates, and all referenced Event 32 localization keys are present without duplicate localization keys.
- The localization file begins with UTF-8 BOM bytes `EF BB BF` and uses icon-first cost presentation with separate blocked variants.
- No GUI references or prohibited out-of-scope file edits were introduced by this worker.
- Hearts of Iron IV was not launched.

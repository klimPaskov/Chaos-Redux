# Event 016 private Mengele Robotics stage decisions handoff

Disposition: implemented source wrappers for parent integration. Engine acceptance and AI probability comparison remain open.

## Files and identifiers

- `common/decisions/016_mengele_robotics_stage_decisions.txt` adds `mengele_event016_robotics_theory`, `_prototype`, `_deployment`, and `_weaponization` under the existing `mengele_clone_army_category`.
- `common/scripted_triggers/016_mengele_robotics_stage_decision_triggers.txt` adds country-scope visibility, inclusive payment, exact private receipt, cancellation, and provider factory-margin AI gates for those decisions.
- `localisation/english/016_mengele_robotics_stage_l_english.yml` supplies titles, descriptions, stage costs, requirements, and lifecycle text with UTF-8 BOM.
- This handoff is the fourth owned file. No shared source, category, Teleportation, spreadsheet, or stage documentation file was edited.

## Contract and implementation

The accepted portfolio plan `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` and completion contract `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` identify Robotics as family 9. The corresponding private active receipt is `mengele_event016_active_project_stage_entries^8`. Every begin, cancel, and finish callback supplies literal family `constant:brilliant_scientist_project_family.robotics` and its own stage selector. The shared private core owns direct political-power, support-equipment, and fuel debits, refunds, history, and output; these wrappers never call the Kruger board core or its receipts.

The shared duration constants specify 180/300/450/600 days. Stage-cost constants provide factory reservations 1/3/6/8 and political-power quotes 55/83/110/165, with Prototype values from `brilliant_scientist_project_fallback_prototype`. File-local numbers occur only where `civilian_factory_use` and `ai_hint_pp_cost` require them. Payment and player-facing cost displays use shared constants. The existing `GFX_decision_brilliant_scientist_project_robotics_ai_*` sprites cover all four rows.

Theory, Deployment, and Weaponization are provider decisions in either DLC state. Prototype is a paid decision only without Götterdämmerung; with that DLC, `sp_brilliant_scientist_autonomous_cognition` owns the native Prototype clock and payment. The shared native bridge grants the neutral robot operational API after an authenticated native Prototype. The private stage core's paid Prototype branch records the Robotics Prototype flag and modifier but does not grant the neutral robot operational API. Therefore the no-DLC decision grants `chaosx_custom_technology_family.robot` after `brilliant_scientist_mengele_finish_project_stage` only if the finish reports both `mengele_event016_stage_finished = one` and `mengele_event016_project_output_applied = one` and the Robotics Prototype completion flag exists. A failed or invalid private finish cannot grant this package. Deployment and Weaponization use the existing private stage core and its idempotent robot API and `robot_weaponization` upgrade.

Each decision uses the same affordability predicate in `available` and `custom_cost_trigger`. The timed decision's `civilian_factory_use` modifier reserves factories and releases them on completion or cancellation. Cancellation is triggered by loss of provider authority or its exact stage receipt, not by resource changes after payment. The private core refunds only the stored direct payment axes. The AI baseline and preferred factor match the accepted Kruger Robotics rows: `brilliant_scientist_project_board.ai_high` and `brilliant_scientist_project_ai.preferred_factor` at war. The same cautious factor is applied through a provider factory-margin trigger because Kruger's `brilliant_scientist_has_low_project_capacity` reads the Kruger capacity variable and cannot represent this private path.

## Source review and outstanding evidence

Consulted all eleven required offline core wiki pages, including Decision Modding and Idea Modding, installed vanilla decision documentation, script-constant documentation, and `common/decisions/GER.txt`. Consulted the `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` skills. Compared the four Teleportation decision rows, the shared Event 016 private stage core, the native bridge, stage constants, sprites, and the existing neutral custom technology API.

Source validation checked four unique decision IDs, four existing icon definitions, all stage quote and duration constant keys, literal selectors and family index 8, callback placement, localisation references, balanced blocks, and the BOM. This is source evidence only. The parent owns the mandatory read-only HOI4 MCP probability baseline and comparison using the same scenarios, final integration review, native factory reservation and callback-order evidence, native Prototype consumer verification, and live-game acceptance. No HOI4 process was launched. No files were staged or committed.

Known engine limits: source review cannot establish native decision timer and factory-reservation order, or whether a shared cleanup removes a family receipt before a timer callback on the same tick. The parent should keep these as acceptance scenarios. No fallback, extra asset, or changed project price was introduced.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. No skill was created or updated.

## Parent review

The parent confirmed the four literal stage wrappers, family array index eight, exact native Prototype split, existing Robotics sprite definitions, shared quote values, and post-finish guard before the no-DLC Robot operational grant.
The parent added `docs/events/016_brilliant_scientist/systems/mengele_robotics_stages.md` for lifecycle, runtime consumers, assets, and acceptance limits.
Parent review used the baseline audit in `016_mengele_robotics_ai_audit_2026-09-25.md` to replace the single Weaponization-based cautious cutoff with four stage-specific no-spare-factory tests at the exact shared reservation quotes, including equality.
This preserves the existing high base, wartime preferred factor, and cautious factor. The final-source auditor reused the six baseline scenarios and found matching source thresholds at 1/3/6/8, but the adapter left eight outcomes unresolved and rejected historical source-hash fields in the `hoi4.probability_compare` request; the wider decision pool remains open.

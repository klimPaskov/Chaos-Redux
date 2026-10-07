# Implementation Prompt: System Camp Repression Rework

Read [package index](../package_index.md) and the current accepted contract and continuation before assigning this template.
Original inventories and candidate labels below require reconciliation with that scope; they do not authorize redoing delivered work.

Read the full package before editing:

- `../specs/system_camp_repression_rework_spec_part_1_core_loop.md`
- `../specs/system_camp_repression_rework_spec_part_2_country_systems_major_powers.md`
- `../specs/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md`
- `../specs/system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md`
- `../specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md`
- `../specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md`
- `../specs/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md`
- all matrices under `matrices/`
- `../research/historical_anchor_notes.md`

Use the existing Chaos Redux implementation as the base. Do not create a parallel camp system.

## Original implementation surface map

Verify the current assigned paths and source revisions before selecting from this original map:

- `common/script_constants/genocide_crisis_constants.txt`
- `common/buildings/chaosx_buildings.txt`
- `common/decisions/genocide_crisis_decisions.txt`
- `common/decisions/categories/genocide_crisis_categories.txt`
- `common/scripted_effects/genocide_crisis_effects.txt`
- `common/scripted_triggers/genocide_crisis_triggers.txt`
- `common/on_actions/genocide_crisis_on_actions.txt`
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `events/genocide_crisis_events.txt`
- `common/ai_strategy/genocide_crisis_ai_strategy.txt`
- `events/germany_mengele.txt`
- `common/script_constants/germany_mengele_constants.txt`
- `common/scripted_effects/germany_mengele_effects.txt`
- `common/scripted_triggers/germany_mengele_triggers.txt`
- `common/decisions/germany_mengele_decisions.txt`
- country-specific decision, idea, AI, focus-hook, localisation, and docs files for Japan, Soviet Union, U.K., U.S.A., France, Italy, Belgium, and generic users.
- existing repression GUI and interface files only within the current accepted national-administration scope.

## Core rules

- Keep population loss routed through Chaos Meter Deaths helpers.
- Keep discovery evidence-based and tied to `genocide_responsible_country`.
- Keep routine monthly processing quiet. No recurring leak/report popup spam.
- Add dynamic values for network reach, labor output, population loss, evidence, stability damage, resistance pressure, guard/rail burden, hardliner pressure, democratic legitimacy damage, and tribunal severity.
- Add dismantlement and reform routes.
- Add AI caps and country-specific weights.
- Update documentation and localisation in the same implementation pass.
- Implement the Part 5 country kits with state-pool logic, costs, mission timing, AI weights, idea lifecycle, focus hooks, dismantlement, discovery, and asset ids.
- Follow the current accepted administration presentation and its reference/MCP evidence; Part 6 preserves the superseded September design.
- Use Part 7 as the touched-file and validation checklist.

## Boundaries

Use state pools by occupation, core status, colonial status, periphery/borderland scripts, and political repression context.

Preserve the abstract restricted-method consequence boundary in the package README and accepted contract.
Do not introduce a killing-efficiency optimization objective or controls.

## Validation to report

Report only meaningful task-specific validation:

- active sites register exactly once;
- monthly pulse changes Deaths and real state population;
- discovery blames responsible country;
- Germany draws from occupied/non-core pools before German cores;
- Japan uses China/Manchuria pools before home fallback;
- Soviet paranoia and famine change Union Crisis values;
- AI does not use invalid targets;
- decision categories hide when no action exists;
- no recurring minor camp leak events fire from monthly processing.
- The accepted administration interface and decisions use the same current contracts, with mandatory matching MCP evidence.

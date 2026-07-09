# Decision and Mission Prompt

Use this prompt for a decision or mission implementation subagent.

Audit and implement the decision layer for the accepted `system_camp_repression_rework` package.


Primary design sources for this pass:

- `specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md` for country decisions, mission timing, costs, AI weights, reform routes, and discovery routes.
- `specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` for category header values and GUI button equivalence.
- `specs/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md` for touched files and validation commands.

Focus on:

- category visibility and clutter control;
- show/hide management decisions;
- expansion decisions;
- guard allocation;
- forced-labor construction and extraction decisions;
- experiment-transfer decisions for Germany and Japan;
- Soviet paranoia, gulag, famine, and Union Crisis decisions;
- colonial packages for U.K./Raj, U.S.A., France/Vichy, Italy/Libya, Belgium/Congo;
- generic authoritarian, communist, fascist, democratic emergency, and chaos-doctrine users;
- evidence destruction near enemy approach;
- inspection, dismantlement, reform, redress, and tribunal-preparation decisions.

Decision requirements must use concrete costs: trains, support equipment, infantry equipment, trucks, manpower, command power, army XP, civilian-factory burden, stability, war support, supply, local control, and valid state pools. Political power can appear but must not be the default-only cost.

Do not expose raw triggers. Use custom trigger tooltips and scripted localisation for pool requirements, costs, current network values, and missing resources.

Do not create recurring minor flavor events from decision cooldowns or monthly processing.

Add chemical and biological killing-efficiency decisions.


Use Part 5 as the detailed source for U.K./Raj, U.S.A., France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and generic decision families, costs, timing, AI weights, dismantlement routes, discovery routes, and asset ids. Use Part 6 for GUI-button equivalence and display-helper requirements.

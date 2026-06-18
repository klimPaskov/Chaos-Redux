# Event 012 Continental Congress GUI Cost Parity Parent Handoff

## Scope

Parent-owned follow-up for the Event 012 Continental Congress scripted GUI button cost gap identified in `2026-06-18_012_africa_decision_followup_handoff.md`.

## Subagent status

- Spawned `chaosx_decision_mission_auditor` with `fork_context=false`.
- Agent id: `019edb7a-6d62-7482-b921-8b586cd46d5e`.
- The subagent did not return during the audit window and was closed before editing files. The parent inspected, patched, reviewed, and validated the final change.

## Files changed

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_gui_cost_parity_parent_handoff.md`

## Gameplay behavior

Before this patch, `africa_gui_authority_seats_button_click` and `africa_gui_bestiary_terms_button_click` validated and spent only political power even though the decision system expects meaningful non-PP costs for regional authority staffing and Bestiary habitat work.

After this patch:

- `can_africa_use_gui_authority_seats` requires political power, support equipment, manpower, and a controlled regional authority seat state.
- `africa_gui_authority_seats_button_click` spends the same political power plus `africa_pay_authority_seat_cost`.
- `can_africa_use_gui_bestiary_terms` requires political power, support equipment, and command power.
- `africa_gui_bestiary_terms_button_click` spends the same political power plus `africa_pay_bestiary_habitat_terms_cost`.
- `africa_negotiate_bestiary_habitat_terms` uses the same support-equipment and command-power helper, preventing the normal decision path from remaining cheaper than the scripted GUI path.

New helper ids:

- `africa_pay_authority_seat_cost`
- `africa_pay_bestiary_habitat_terms_cost`

New tuning constants:

- `africa_force.authority_seat_support_equipment`
- `africa_force.authority_seat_manpower_gate`
- `africa_force.authority_seat_manpower_spend`
- `africa_force.bestiary_terms_support_equipment`
- `africa_decision.bestiary_terms_command_power_gate`
- `africa_decision.bestiary_terms_command_power_spend`

Changed localisation keys:

- `africa_gui_authority_seats_button_tt`
- `africa_gui_bestiary_terms_button_tt`
- `africa_negotiate_bestiary_habitat_terms_cost_tt`
- `africa_negotiate_bestiary_habitat_terms_cost_tt_blocked`
- `africa_negotiate_bestiary_habitat_terms_cost_tt_tooltip`

## Validation

The parent validation checked helper references, cost-key references, touched script brace counts, localisation BOM preservation, and focused diff cleanliness. No live HOI4 run or scripted GUI screenshot validation was performed in this tranche.

## Remaining risks

This closes only the known PP-only gap for the Authority Seats and Bestiary Terms GUI buttons. It does not close the broader Continental Congress GUI prompt-depth gaps around regional-card lists, selected-target card families, warning-state panel variants, or full targeted scenario validation.

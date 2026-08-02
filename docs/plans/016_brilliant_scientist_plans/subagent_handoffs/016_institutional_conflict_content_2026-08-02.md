# Event 016 institutional conflict content handoff

## Scope

This tranche fills the Phase F university and institutional-conflict surface without producing or wiring any 3D model. It adds the mutually exclusive “Protect Dissenting Scientists” and “Dismiss the Ethics Chair” Directorate decisions.

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`: centralized the 60-day timing, resource costs, hidden-state deltas, and persistent modifier values.
- `common/script_constants/016_brilliant_scientist_containment_constants.txt`: centralized the government and Kruger containment-score factors.
- `common/decisions/016_brilliant_scientist_directorate_institutions.txt`: added one-time host-only decisions with concrete political-power, support-equipment, manpower, timed production burden, AI weights, cancellation, and state-delta effects.
- `common/dynamic_modifiers/016_brilliant_scientist_directorate_modifiers.txt`: added host-only protected-dissent and dismissed-ethics-chair modifiers.
- `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`: feeds both policy flags into the sovereignty score calculation.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`: carries the policy history through verified Kruger State formation and restores the corresponding modifiers on the carrier.
- `localisation/english/016_brilliant_scientist_directorate_l_english.yml`: added decision, tooltip, and modifier text.
- `docs/events/016_brilliant_scientist/systems/directorate.md`: documented costs, lifecycle, hidden-state consequences, containment interaction, and host-only modifier behavior.

## Runtime contract

Both decisions require an established Directorate institution and a current host. They share `brilliant_scientist_institutional_conflict_in_progress`, are one-shot, and cannot be selected after the other policy is recorded. The protection route spends 150 support equipment and 500 manpower; the dismissal route spends 100 support equipment. Their 60-day active modifiers impose a light consumer-goods and factory-efficiency burden. Losing host control cancels the action without applying its policy.

## Validation and remaining risk

Static syntax, reference, constant, localisation, and BOM checks remain to be run with the rest of this tranche. No model was created. Live game acceptance remains user-owned and is not claimed here.

# Event 016 university appointment-method handoff

## Scope

This tranche fills the remaining Phase F public-university governance choices without producing or wiring any 3D model. It adds the mutually exclusive “Award the National Science Chair,” “Rotate Grants Among Institutions,” and “Let Kruger Select the Institutions” decisions.

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`: centralized timing, political-power, support-equipment, manpower, hidden-state, and modifier values.
- `common/decisions/016_brilliant_scientist_directorate_institutions.txt`: added three one-time, university-network-gated decisions with concrete logistics, timed production burden, cancellation, AI policy preference, and persistent method lock.
- `common/dynamic_modifiers/016_brilliant_scientist_directorate_modifiers.txt`: added distinct host-only modifiers for the three methods.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`: carried the method flags through the verified Kruger State history and restored their host modifier receipts.
- `localisation/english/016_brilliant_scientist_directorate_l_english.yml`: added decision, effect-tooltip, and modifier strings.
- `docs/events/016_brilliant_scientist/systems/directorate.md`: documented the route lock and causal trade-offs.

## Runtime contract

All three decisions require `brilliant_scientist_university_research_network_chartered`, share `brilliant_scientist_institutional_appointment_in_progress`, and set `brilliant_scientist_institutional_appointment_method_selected` on completion. The national-chair route consumes 200 support equipment and 1,000 manpower over 90 days; grant rotation consumes 100 support equipment and 500 manpower over 60 days; Kruger selection consumes the same logistics over 45 days. The timed actions impose consumer-goods and factory-efficiency burdens and cancel cleanly if the country stops being the current host or loses control.

## Validation and remaining risk

Static syntax, constant-reference, localisation, and BOM checks remain to be run with the combined tranche. No model was created. Live game acceptance remains user-owned.

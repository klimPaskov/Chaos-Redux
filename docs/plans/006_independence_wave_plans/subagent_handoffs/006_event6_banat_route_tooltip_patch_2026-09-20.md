# Event 006 Banat route tooltip patch

Status: implemented.

## Scope

This bounded patch clarifies the five Banat government-route decision outcomes without changing gameplay effects, costs, availability, cancellation, AI weights, package admission, or probability-bearing logic.

Changed source files:

- `common/decisions/006_independence_wave_balkan_decisions.txt`
- `localisation/english/006_independence_wave_balkan_l_english.yml`

The affected decisions are `independence_wave_axx_ratify_municipal_charter`, `independence_wave_axx_convene_mountain_workers`, `independence_wave_axx_restore_village_autonomy`, `independence_wave_axx_establish_mountain_commission`, and `independence_wave_axx_accept_rail_patron_compact`.

## Implementation

The generic `independence_wave_axx_route_effect_tt` reference was replaced with five route-specific `custom_effect_tooltip` keys.

The new localization keys are `independence_wave_axx_constitutional_route_effect_tt`, `independence_wave_axx_workers_route_effect_tt`, `independence_wave_axx_traditional_route_effect_tt`, `independence_wave_axx_emergency_route_effect_tt`, and `independence_wave_axx_patron_route_effect_tt`.

The wording follows the existing scripted effects in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`: the constitutional route gives a major civic-ledger gain and minor defence-ledger gain, the workers route gives a minor civic-ledger gain and standard defence-ledger gain, the traditional route gives major civic-ledger and standard defence-ledger gains, the emergency route gives a minor civic-ledger loss and decisive defence-ledger gain, and the patron route gives a standard civic-ledger gain and minor defence-ledger gain.

The tooltip wording also names the relevant administrative, diplomatic, or security progression where the route's decision effect supplies it, while avoiding numeric tuning values.

## Validation and limits

The old generic key has no remaining references in the decision or localization trees after the patch.

The localization static audit was rerun after editing and is the primary validation for key coverage, duplicate definitions, parse status, BOM/header encoding, and Event 006 bindings.

No native decision inspector or decision renderer is exposed by the installed HOI4 MCP service, so a decision-window production render was not available for this text-only patch.

No AI weights, costs, effects, package admission, allocator reservations, portraits, audio, GUI layout, or spreadsheet fields were changed.

The wider Event 006 goal remains HOLD/PARTIAL because FSM source and rights clearance, slot-23 audio approval, typed probability evidence, package breadth, GUI/formable evidence, and live user validation remain unresolved elsewhere in the event.

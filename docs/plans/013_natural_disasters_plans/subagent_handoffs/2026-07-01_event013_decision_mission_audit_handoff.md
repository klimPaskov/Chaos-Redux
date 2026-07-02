# Event 013 Natural Disasters Decision/Mission Audit Handoff

## Files changed

- `common/decisions/013_natural_disasters_decisions.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`

The workspace already had parent edits in these files before this audit. This handoff covers only the narrow changes below.

## Changed ids

- `natural_disaster_deploy_rescue_columns`
- `natural_disaster_clear_blocked_routes`
- `natural_disaster_state_is_low_priority_while_critical_exists`

## Before and after behavior

- Before: the rescue-column and blocked-route hover highlights used broad state triggers and could outline disaster states not controlled by the decision owner. After: both highlight triggers require `is_controlled_by = ROOT`, matching the state-targeted decision target pool and availability checks.
- Before: low-priority suppression checked `OWNER = { natural_disaster_country_has_critical_response_state = yes }`. In occupied or controller-managed disaster states, this could compare against the wrong country. After: it checks `CONTROLLER`, matching the `any_controlled_state` recovery queue used by the decisions.

## Audit notes

- Response decisions use concrete custom costs and call matching `natural_disasters_pay_*_cost` effects that spend command power, manpower, fuel, trains, convoys, infantry equipment, motorized equipment, and support equipment. I did not find a political-power store pattern in this decision surface.
- Stabilization and reconstruction missions have activation flags, auto-success when no controlled recovery states remain, timeout failure effects, and flag cleanup in success, failure, and cancel paths.
- AI weights use the new state priority triggers and suppress low-priority targets while a critical controller-owned recovery state exists after this patch.
- Decision target conditions are state-scoped and require current control by ROOT in the target/available checks.

## Validation performed

- Checked the decision file against the offline Decision modding page for state-targeted decisions, custom cost behavior, and mission activation/available behavior.
- Checked vanilla documentation for `has_equipment`, script constants, effects, and triggers relevant to the cost gates and scripted effect calls.
- Searched the Event 013 effects to confirm every custom cost gate has a corresponding resource-spending `natural_disasters_pay_*_cost` effect.
- Searched the patched files to confirm the low-priority suppression trigger now uses `CONTROLLER` and no old `OWNER` branch remains for that helper.

## Skipped validation

- Did not run the game or inspect runtime logs. This audit used static file inspection only.
- Did not edit localisation because no broken decision key was found.

## Remaining risks

- Mission entries still include `visible` blocks. The wiki notes `visible` does nothing for missions, but the active behavior is carried by `activation`, so I left this as harmless existing noise rather than broad cleanup.
- Custom cost gates use strict `>` comparisons, so exact-resource edge cases remain stricter than the displayed cost. This matches common local repo and vanilla patterns, but it is worth a later balance decision if exact-cost availability is desired.

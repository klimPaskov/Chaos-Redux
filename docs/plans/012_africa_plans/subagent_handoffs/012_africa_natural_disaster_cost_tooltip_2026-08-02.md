# Event 012 natural-disaster caller cost tooltip

## Scope

The two priority-member natural-disaster decisions now show the actual caller reserve they already enforce, including a blocked-state variant. No gameplay cost or action ledger changed.

## Change

`africa_priority_member_natural_disaster_dynamic_cost` now displays 35 political power and 10 command power with the standard icons. `africa_priority_member_natural_disaster_dynamic_cost_blocked` provides the red unavailable form. Both Rain and Drought already use the shared custom-cost key and `africa_natural_disaster_member_cost_is_available` trigger.

## Validation

The constants remain authoritative at `common/script_constants/012_africa_action_constants.txt` (`caller_pp_cost = 35`, `caller_cp_cost = 10`), and the decision selectors remain unchanged. Event 012 localisation duplicate/missing-key audits previously reported clean; the modified file retains its UTF-8 BOM. Live UI rendering remains user-owned.

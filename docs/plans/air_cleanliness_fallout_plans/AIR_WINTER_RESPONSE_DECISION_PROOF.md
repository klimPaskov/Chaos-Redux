# Air Winter Response Decision Proof

## Status

The Air Winter response layer has static engine proof for targeted decision scope, timers, custom costs, cancellation, state modifier categories, state population mutation, arrays, and terminal event handoff. Runtime observations are still required for the population transfer side effect and the complete decision flow. This document does not claim live-game proof.

## Required references consulted

- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
  - Lines 302 through 330 define custom cost triggers, the base, blocked, and tooltip localisation keys, and the requirement to deduct the cost in `complete_effect`.
  - Lines 334 through 352 define `days_remove`, `remove_effect`, `cancel_trigger`, and `cancel_effect`.
  - Lines 515 through 592 define targeted decisions, ROOT as the acting country, FROM as the target, `state_target = any_controlled_state`, and `on_map_mode`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt`
  - The state integration decisions near lines 1844 through 1884 use `state_target = any_controlled_state`, a FROM state target, a timed `remove_effect`, and cancellation cleanup.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/SIA.txt`
  - The propaganda decisions near lines 406 through 681 use `constant:` values directly in `days_remove` and `days_re_enable`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`
  - Lines 4567 through 4573 classify `repair_speed_<Building>_factor` as country-only.
  - Lines 4879 through 4885 classify `state_repair_speed_<Building>_factor` as state scope and list infrastructure, railway, and air base types.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
  - Lines 1468 through 1475 support `add_manpower` in STATE and COUNTRY scope and describe state-local population mutation.
  - Lines 2278 through 2290 support scope values in arrays.
  - Lines 2713 through 2720 support `clear_array`.
  - Lines 4296 through 4309 support `for_each_scope_loop` and its scope change to each array member.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
  - The state effect entry near lines 9321 through 9332 confirms that state-scope `add_manpower` changes total state population and notes a recruitable manpower interaction for negative values.

## Implementation mapping

| Engine surface | Implementation | Static proof |
| --- | --- | --- |
| Acting country and selected state | `common/decisions/air_cleanliness_winter_decisions.txt` | Every target gate enters FROM before state triggers. Country affordability and AI checks remain in ROOT. |
| Timed work | `days_remove`, `remove_effect`, `cancel_trigger`, and `cancel_effect` in the decision file | Matches the wiki contract and the vanilla AFG pattern. Vanilla SIA proves direct `constant:` duration access for these decision fields. |
| Exact custom costs | `air_winter_response_can_pay_*` triggers and `air_winter_response_pay_*` effects | All 17 custom costs have base, blocked, and tooltip keys. Each timed project deducts its listed resources in `complete_effect`. Civilian factories are reserved by the active decision modifier. |
| One active project per state | `air_winter_response_project_active` | Set on selection, cleared on completion, cleared on cancellation, and cleared by full state reset. |
| Reception target | `air_winter_reception_states` | Designation clears the country array before adding the selected state. Full global reset clears the array. |
| Population transfer | `air_winter_response_complete_controlled_evacuation` and `air_winter_response_complete_final_evacuation` | The source amount is rounded once, negated in a temporary variable, removed from the source state, and added unchanged to the one reception state. |
| Terminal decisions | `air_winter_response_complete_abandonment_vote` and `air_winter_response_complete_decontamination` | Each saves FROM as regular `air_winter_response_state`, clears the active project, applies the state cooldown, and immediately fires `.201` or `.202` in the same chain. |
| Repair modifiers | `common/dynamic_modifiers/air_cleanliness_winter_dynamic_modifiers.txt` | Phase, rail, and air base modifiers use `state_repair_speed_*` tokens. No country-only repair token remains in a state modifier. |

## Runtime proof still required

1. Start one timed action and confirm its visible timer, exact resource deduction, state lock, expiry effect, and cooldown.
2. Cancel one timed action by losing control of the selected state and confirm that the project flag clears without the expiry effect.
3. Designate a reception state, complete both evacuation decisions, and record source population, receiver population, and country available manpower before and after. The two state population deltas must be equal and opposite. The available manpower observation is required because the offline wiki documents a recruitable manpower interaction for negative state population changes.
4. Complete the abandonment vote and confirm `.201` resolves against the selected state.
5. Complete mass decontamination once above and once below its disclosed Survival, Adaptation, and Water Security gate. Confirm `.202` exposes only the matching deterministic result.
6. Confirm the category and all 17 decision icons after their dedicated sprites are registered.

## Current conclusion

The selected implementation is supported by documented engine surfaces and vanilla structure. Population conservation is proven arithmetically in script, but its country manpower side effect remains a live-game proof item. No fallback implementation is in use.

# Missile scenario transaction inputs

`032_missiles_scenario_effects.txt` owns the synchronous SCN-015 country-package transaction.

`missiles_scenario_apply_country_package` runs in each frozen recipient's country scope.
It snapshots nine inputs from globals into country variables: `missiles_scenario_package_profile`, `missiles_scenario_package_intensity`, `missiles_scenario_package_share`, `missiles_scenario_package_stage`, `missiles_scenario_package_reserve`, `missiles_scenario_package_site_capacity`, `missiles_scenario_package_readiness`, `missiles_scenario_package_control`, and `missiles_scenario_package_incident_cap`.
All nine inputs are assigned before nested package calls.
The initializer consumes the stage, reserve, site-capacity, readiness and control values; the remaining four retain their existing transaction input contract even though current source has no reader.
Country storage is required by the initializer's presence tests and parent-country site-capacity reads.
Cleanup uses `clear_variable` at country completion and again for each selected recipient in `missiles_scenario_finish_transaction`.
This preserves absence after completion, including failed site setup, without substituting zero for a missing value.
These effects do not nest another package application before cleanup.

`missiles_scenario_requested_count` remains a temporary calculation whose result is copied into `global.missiles_scenario_requested_count` before selection.
Selection reads the explicit global result, and subsequent calculation calls initialize the scratch count before arithmetic.
`missiles_evolution_selection` remains a temporary input initialized directly before each recorder call.
Its recorder and unlock consumers inspect that selected value; every later entry into those consumers has its own preceding selection assignment.
Both temporary names expire naturally with the enclosing evaluation.

`missiles_scenario_warning_recipient` remains a regular event target.
Warning seeding overwrites it for each recipient before adding that recipient to the root participant array.
That array and the warning's country/id variables hold the durable receipt; no subsequent continuation reads the regular recipient target without first assigning it again.
The regular target expires naturally with the chain, including any engine-carried event context.
The separate global warning root intentionally persists until incident closure; it is not converted to a regular target or unconditionally cleared at successful setup.

No new constants, scheduling hooks, helper declarations, or weighted decisions are introduced.
See the startup repair handoff and exact-token reference evidence for validation limits.

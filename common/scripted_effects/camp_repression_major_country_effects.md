# Major-country repression helper contracts

This document covers the Soviet famine relief APIs in `camp_repression_major_country_effects.txt`.
Other country modules retain their package specifications and existing administration references.

## Funded Soviet famine relief

`camp_rework_soviet_emergency_famine_relief` runs in the acting Soviet country scope.
It needs positive famine pressure, every quoted equipment type, and no existing relief flag or mission.
`camp_rework_soviet_relief_order_ready` is its read-only final preflight.
The equipment quote comes from `camp_rework_equipment_cost` in `camp_repression_rework_constants.txt`.

The helper clears `camp_rework_soviet_relief_order_accepted` on entry.
On success it removes motorized, trains and support stores once, sets the active relief and accepted-order flags, reduces grain extraction and forced-labor burdens, applies the existing stability consequence, and activates one relief mission.
The receipt is a request result, not a permanent policy flag.
On rejection it spends nothing and grants no relief.
No population, death-record or research primitive belongs to this transaction.

Political power belongs to the caller.
The native decision declares the 30-PP `camp_rework_cost.labor_project_pp` quote.
The Soviet action dispatcher refunds that quote if the final helper rejects.
The shared package router records the scripted cooldown only with an accepted receipt and then clears it.
The event choices declare no additional political-power payment and call the funded helper directly, so they cannot enter the decision refund branch.
They clear the request receipt after selecting their result.
Native decision payment ordering, combined native/custom cost presentation and native re-enable timing remain engine evidence requirements.

Usage from a funded event choice:

```text
if = {
	limit = { camp_rework_soviet_relief_resources_ready = yes }
	camp_rework_soviet_emergency_famine_relief = yes
}
else = { camp_rework_soviet_relief_mobilization_failed = yes }
clr_country_flag = camp_rework_soviet_relief_order_accepted
```

## Explicit material shortfall

`camp_rework_soviet_relief_mobilization_failed` handles the warning response.
It raises famine pressure by the existing minor amount and administrator corruption by its minor amount.
`camp_rework_soviet_relief_crisis_mobilization_failed` handles the crisis response through the existing major famine, corruption and evidence outcome.
Both run in Soviet country scope and require positive famine with no active relief flag or mission.
This protects relief started through another order while an earlier popup remained open.
They consume no equipment, activate no mission and apply no immediate population loss or research reward.
The country monthly processor remains responsible for subsequent measured losses.

The same responses handle a funded event option whose material stock changed after the event appeared.
The independent shortfall options remain selectable when their event has no valid site-specific concealment or admission target.
Their stable keys are `soviet_gulag.1.c` and `soviet_gulag.2.shortfall`.
`soviet_gulag.2.d` belongs only to the crisis description.

## Evidence and remaining work

The parsed production-source suite and its results are in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_famine_shortfall_source_tests.py` and the paired results JSON.
The suite uses mocked native equipment, PP and mission primitives and does not certify engine execution.
The task handoff tracks MCP, localisation, decision, AI and live-evidence gaps.

The relief choices reuse the installed Soviet famine report sprites and existing decision icon.
No new image, text icon or GFX asset is required by these transaction helpers.
Future source-labelled loss receipts must preserve the occupation and custody provenance contract without making deaths advance an institutional program.

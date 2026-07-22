# New Zealand Lifeboat State achievement handoff

Status: accepted pilot achievement set. Working labels are not final localisation.

## `chaosx_fallout_nzl_open_harbors`

- Eligible country: the current `NZL` Fallout package carrier with the humanitarian identity.
- Required route: complete `fallout_nzl_pacific_relief_republic` and `fallout_nzl_pacific_rescue_mandate`.
- Required campaign state: reach the Year 10 closure with at least two living, independent, current-generation relief partners.
- Required mechanic state: harbor capacity, food security, parliament trust, and sea-lane security are each at least 70.
- Disqualifiers: ever complete Last Berth Closure, lose either assigned capital port, become a subject, or fabricate a relief partner receipt.
- Visibility: visible.
- Difficulty: very hard.
- Icon direction: two open harbor lights, two small rescue craft, and the New Zealand four-star navigation mark.

## `chaosx_fallout_nzl_closed_seas`

- Eligible country: the current `NZL` Fallout package carrier with the isolation identity.
- Required route: complete `fallout_nzl_southern_refuge` and `fallout_nzl_southern_sea_exclusion_zone`.
- Required campaign state: defeat or force a settlement with every exact pirate aggressor recorded by the package, retain ownership and control of all five package states, and complete the Year 10 closure. If no current-generation aggressor was ever proven, the explicit no-aggressor route satisfies this condition without creating a substitute target.
- Required mechanic state: sea-lane security at least 85 and food security at least 65.
- Disqualifiers: ever grant foreign basing rights through the bilateral result, lose the package capital, become a subject, or receive the aggressor receipt from an invalid target.
- Visibility: visible.
- Difficulty: very hard.
- Icon direction: closed harbor gate, hard patrol wake, compact silver four-star cross.

## `chaosx_fallout_nzl_two_islands_one_lifeboat`

- Eligible country: any current `NZL` Fallout route.
- Required route: complete `fallout_nzl_two_island_supply_ring` and `fallout_nzl_lifeboat_navy`.
- Required campaign state: complete every shared major mission without a failure receipt, keep Wellington and Auckland naval bases operational, keep all five package states owned and controlled, and complete the Year 10 closure.
- Force limit: create no more than one additional escort formation after the three package-start formations.
- Disqualifiers: any failed major repair, food, refugee, or patrol mission, any free-unit duplication receipt, or loss of a package state at Year 10.
- Visibility: visible.
- Difficulty: hard.
- Icon direction: two linked islands, a milk rail, and a working harbor crane under four stars.

## Implementation requirements

Register all three in `common/achievements/chaos_redux_achievements.txt`. The `possible` block must remain available at campaign start, because the Fallout identity is created later. The `happened` block uses dedicated scripted triggers that fail closed unless the current package, transition generation, route, partner, mission, force, and state-control receipts all pass.

Localisation needs final title, description, and exact condition tooltip keys for each achievement. Asset output requires completed, grey, and not-eligible `64x64` DDS files.

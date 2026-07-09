# Infantry Spawn achievement prompt

Use this file with the coding and asset prompts. Achievement titles here are working labels and title directions, not final localisation.

Event id: 019. Event slug: infantry_spawn.

## Achievement list

| Working key | Title direction | Eligible player | Unlock conditions | Disqualifiers | Visibility | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infantry_spawn_small_state_order | small country mastering sudden musters | any country with limited state count at event start | survive three Infantry Spawn firings, keep command coherence high, no possessed revolt, no chaos splinter | lost capital, used chaos unit authorization | visible | hard | tiny country seal holding many regiments |
| infantry_spawn_no_free_lunch | integrated army without exploitation | any | win a defensive war after receiving Evolution II units while clearing supply strain and roster backlog | disband farming abuse flag, lost capital | visible | medium hard | ledger with balanced scales and rifles |
| infantry_spawn_general_caged | defeated possessed general | any Evolution III country | defeat or arrest a possessed general revolt before it controls the capital | negotiated full autonomy or annexed by third party | visible | hard | officer cap behind bars |
| infantry_spawn_barracks_state_tamed | pacified human breakaway | any parent country | defeat, puppet, or peacefully reintegrate a Barracks State and clear officer appetite | used console scenario bypass in normal run | hidden | hard | broken epaulettes over restored flag |
| infantry_spawn_horde_without_outbreak | contained ragged horde | any | create or face Ragged horde, defeat it, and never trigger parent Zombie Outbreak escalation from this chain | advanced zombie variant unlocked by this chain | hidden | very hard | base zombie hand sealed by army stamp |
| infantry_spawn_pale_recovery | recovered ghost harm | any | defeat Grey host and recover every state it slowly harmed | any harmed state becomes unrecovered by run end | hidden | very hard | pale town returning to color |
| infantry_spawn_stone_broken | defeated stone host | any | defeat Stone host after it controls a fortified or mountain state | parent loses all core territory | hidden | hard | cracked stone helmet |
| infantry_spawn_arsenal_order | mastered Evolution II arsenal wave | major or regional power | receive heavy units, keep supply strain below danger band, and win a war within a set period | disbanded majority of heavy spawned units | visible | hard | tank, train, and orderly ledger |
| infantry_spawn_maximum_scenario_survivor | scenario mastery | selected scenario player | win or survive the triggerable scenario at High or Maximum intensity and eliminate active splinters | lowered intensity after launch | hidden | extreme | world of barracks fires contained by one seal |
| infantry_spawn_close_the_ledger | shut down chaos access | any Evolution IV country | use chaos units, then close the chaos ledger, remove training access, and prevent splinter formation for a long period | any chaos splinter forms | visible | hard | cracked supernatural ledger chained shut |
| infantry_spawn_reckless_and_redeemed | intentionally created and reconquered splinter | any | trigger a chaos splinter from own mismanagement, reconquer it, recover affected states, and keep country alive | parent event world-end flag set by another system | hidden | extreme | black-red roster burned clean |
| infantry_spawn_roster_of_all_things | broad random unit collection | any | field at least one infantry, cavalry, armor, mechanized, specialist, and absurd random formation from the event in one campaign | exploited duplicate spawn bug | hidden | hard | mismatched unit silhouettes in one frame |

## Tracking notes

Implementation should create tracking flags and variables that distinguish normal event play from triggerable scenario play when an achievement requires it. Achievements must not unlock merely because the event fires. They should require sustained management, containment, survival, victory, or rare route completion.

## Asset notes

Each achievement needs a 64x64 completed icon direction. The asset package should create completed, grey, and not-eligible variants when the achievement system requires them. Do not derive achievement icons from focus icons.

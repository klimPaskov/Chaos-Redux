# Infantry Spawn decision and mission map

This file expands the decision map from the main spec. It is not final localisation.

## Decision staging

| Stage | Visible families | Hidden or queued families | Clutter control |
| --- | --- | --- | --- |
| Baseline | inspect, sort, disband if large wave | follow-up flavor events | category hides after backlog clears |
| Evolution I | inspect, sort, standardize, absorb officers | better template rolls | only if strain or backlog exists |
| Evolution II | request unit, target front, depot lottery, ban musters | panic events, supply missions | cooldowns and active caps |
| Evolution III | general demands, illegal regiments, rotate staff, arrest | revolt countdowns | selected general and selected state flow |
| Evolution IV | quarantine, authorize base zombies, bind golems, exorcise ghosts, contain splinter | chaos splinter seeds | unit-family filters and leakage thresholds |

## Major decision families

| Family | Visible purpose | Non-political costs | Dynamic scaling | Failure or risk |
| --- | --- | --- | --- | --- |
| Inspection | learn what the army received | army XP, command power, time | backlog and country size | missed inspection raises uncertainty |
| Depot sorting | lower logistics strain | trains, trucks, support equipment, fuel | spawned unit count and rail quality | supply penalty and worse future fill |
| Standardization | make templates sane | army XP, infantry equipment, support equipment | absurdity and template class | removes some strong weird units |
| Disbanding | remove fragments | stability, manpower loss, command cost | number and quality of divisions | political backlash, limited recovery only |
| On-demand spawn | gamble for another unit | army XP, manpower, equipment, supply strain | prior uses, war state, chaos | terrible unit, general demand, splinter seed |
| Front muster | targeted defensive spawn | war state, units at front, equipment, fuel | enemy threat and controlled fronts | high strain and stronger appetite |
| General concession | buy short-term control | command power, army XP, laws, stability | appetite and war pressure | future revolt strength |
| Staff rotation | reduce general grip | command power, stability, officer corps risk | appetite and number of linked units | immediate demand or sabotage |
| Quarantine | contain chaos units | support equipment, manpower, local divisions | leakage and chaos unit count | unit losses and local panic |
| Binding or exorcism | profile-specific containment | support equipment, stability, army XP, construction | unit profile and state harm | failed action triggers splinter |

## Mission table

| Mission | Owner | Objective | Success direction | Failure direction | Duplicate risk guard |
| --- | --- | --- | --- | --- | --- |
| Guard the depots | parent country | place supplied divisions in named depot states | lower supply strain and depot disorder | depot disorder, poorer equipment fill | target states should rotate or be selected once |
| Register the regiments | parent country | pause requests and hold command coherence | lower backlog and absurdity | demand chain seed | one active mission per country |
| Hold the capital rails | parent country | keep capital controlled and supplied | safer capital defense | capital panic, supply strain | only when capital supply is threatened |
| Break the rogue drill field | parent country | hold selected rebel seed state with loyal units | remove revolt pool | uprising or stronger general | one selected state at a time |
| Seal the strange barracks | parent country | contain chaos state with units and support equipment | lower leakage | chaos unit or splinter seed | only Evolution IV |
| Prove the new command | breakaway | hold capital and depots after revolt | unlock focus route and units | fragmentation or surrender event | one per breakaway |
| Recover the pale zone | parent or victor | hold harmed ghost state and pay resources | remove harm modifier gradually | renewed ghost pressure | one state target per decision family |

## Cleanup obligations

- clear selected target country and selected state when mission ends
- clear general demand flags when character dies, country dies, or revolt resolves
- hide request decisions while ban cooldown is active
- remove chaos training access when the chaos ledger is closed
- cancel containment missions if splinter no longer exists
- remove obsolete target decisions after tag switch or annexation

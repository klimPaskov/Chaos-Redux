# Event 064 Decision and Mission Matrix

All labels are working labels, not final localisation.

## Posture matrix

| Posture | Who can select it | Public purpose | Temporary effect direction | Main project | Main costs encouraged | Main tradeoff | AI preference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Integrate the Line | country with local line or redoubt | organize, man, repair, and use the defenses | fort defense, entrenchment, fort repair, or prepared-ground support through valid modifiers | Reinforce a Priority Sector | civilian factories, infantry equipment, support equipment, manpower | weak offensive counterplay and tied defensive resources | defensive war, weaker than enemy, capital threat, adequate supply |
| Keep the Roads Open | country with affected state and useful network target | connect positions to transport, supply, and repair systems | supply use, infrastructure or railway repair, transport reliability, or lower fortified-sector attrition | Connect the New Line | civilian factories, trains, trucks, support equipment | smaller direct combat effect and transport stockpile commitment | long frontier, poor network, supply strain, several sectors |
| Study the Breach | country with a meaningful fortified foreign target | prepare engineers and staffs to cross the world's new lines | fort attack, planning speed, engineer effectiveness, or target-bound offensive preparation | Conduct Breach Exercises | Army Experience, support equipment, fuel, Command Power | weaker local defense and up-front offensive cost | planned offensive, high enemy forts, available XP and fuel, little local frontier |
| Observation only | country with no local result and no useful target | close the report without opening a false system | none | none | none | no local benefit | forced only when every active posture is invalid |

## Project matrix

| Project | Access | Target | Public commitment | Duration anchor | Completion result | Failure or cancellation | Repeat limit | Icon direction |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| Reinforce a Priority Sector | Integrate posture, open window, no active project | one controlled affected border state below strategic cap | civilian industry, infantry equipment, support equipment, manpower | 45 to 75 days | one bounded extra fort package in valid direct frontier or anchor positions | state lost, frontier removed, country annexed, all positions invalid | one package per target state per wave | reinforced bunker sector |
| Connect the New Line | Logistics posture, open window, no active project | one affected border or redoubt state with a real network gap | civilian industry, trains, trucks, support equipment | 60 to 100 days | repair or improve existing infrastructure or railway support, or bounded local supply alternative | state lost, route invalid, country annexed, no physical result remains | one package per target state per wave | rail or road linking fort |
| Conduct Breach Exercises | Breach posture, open window, no active project | one valid fortified foreign target and objective sector | Army Experience, support equipment, fuel, Command Power | 45 to 75 days | 90 to 150 day target-bound fort attack and planning package | target invalid, target becomes incompatible ally, country annexed | one active target preparation, new completion replaces old Event 064 breach plan | cracked fort and engineer wedge |
| Harden the Air and Coastal Flank | Evolution II local materialization, valid state, open window | one selected Fortress State with air or coastal role | civilian industry, relevant equipment or convoys, relevant experience, support equipment | 60 to 100 days | up to two role-based physical improvements under caps and optional temporary coordination | state lost, all roles capped, country annexed | one package per target state per wave | compact AA, radar, coastal flank symbol |
| Prepare a National Redoubt | Evolution III local materialization, valid redoubt, open window | capital, capital approach, major VP, supply hub, industry, port, or strategic site | civilian industry, trains or infantry equipment, support equipment, manpower | 90 to 140 days | one fort level at bounded redoubt plus at most one justified support improvement | target lost, capital changed through shortcut, country annexed, all roles capped | one National Redoubt project per country per wave | capital citadel in inner ring |

## Visibility matrix

| State | Integrate option | Logistics option | Breach option | Category visible | Projects visible |
| --- | --- | --- | --- | --- | --- |
| Local direct frontier changed | yes | yes when network target exists | yes when foreign target exists | yes after selection | selected posture project plus valid evolved general projects |
| Direct frontier exists but already capped | yes | yes when network target exists | yes when foreign target exists | only with useful action or active challenge | actions that can still change support or preparation |
| Only depth positions changed | yes | yes | yes when target exists | yes | selected posture project if valid and evolved actions |
| Only Fortress State support changed | yes | yes | yes when target exists | yes | support, logistics, and evolved projects under posture rules |
| Only internal redoubt changed | yes | yes when network target exists | yes when target exists | yes | redoubt and selected posture actions |
| No local construction, fortified foreign target exists | no | no | yes | yes after breach selection | breach exercises only |
| No local construction and no fortified foreign target | no | no | no | no after report | none |
| Unsupported special actor | only if owner contract supports it | only if owner contract supports it | only if owner contract supports it | only for supported content | supported subset only |
| Response window expired, project active | posture remains only as project support if designed | same | same | yes | active mission only |
| Response window expired, no project | no new selection | no new selection | no new selection | no | none |

## Dynamic cost factors

| Factor | Reinforce sector | Connect line | Breach exercises | Air or coastal flank | National redoubt |
| --- | --- | --- | --- | --- | --- |
| Target size | more valid frontier positions raises equipment and industry | larger network gap raises transport and industry | higher fort density raises XP, support equipment, and duration | more complex state role raises industry and support cost | more important or exposed redoubt raises duration and industry |
| Country industry | larger countries pay higher capped bundle | larger countries pay higher capped bundle | limited effect, preparation scale tied to target | larger countries pay higher capped bundle | larger countries pay higher capped bundle |
| Country reserves | low stockpile can reduce scope or invalidate | reserve floors can invalidate | reserve floors can invalidate | reserve floors can invalidate | reserve floors can alter train versus equipment bundle |
| State infrastructure | low infrastructure lengthens work | low infrastructure increases work and payoff | no direct cost change unless target access is poor | low infrastructure lengthens work | low infrastructure lengthens work |
| War state | urgent defense can shorten duration at higher material cost | active supply crisis can raise priority | active planned offensive can shorten preparation at higher fuel cost | enemy air or invasion threat raises priority | capital emergency raises priority and can shorten duration at cost |
| Evolution tier | higher caps permit a larger valid result | higher tier can expose redoubt targets | higher foreign fort levels raise preparation need | required from Evolution II | required from Evolution III |
| Prior project in state | invalid when already used this wave | invalid when already used this wave | old target plan replaced, not stacked | invalid when state already used for same package | one per country per wave |
| Cluster benefit | exact relevant abundance can reduce one equipment element | transport abundance can reduce one element | doctrine or equipment abundance can reduce one element | exact air, naval, or equipment gain can reduce one element | exact transport or support abundance can reduce one element |

## Mission state matrix

| Mission state | Player display | Allowed transition | Forbidden transition | Required cleanup |
| --- | --- | --- | --- | --- |
| Available | target rules, costs, duration, public result | start when valid and affordable | start while another Event 064 project active | none |
| Active | target, time remaining, committed costs, failure reasons | complete, fail, cancel under allowed rule, survive save-load | start duplicate, reroll result, change stored target silently | persistent timer and saved target |
| Completed | concise result and history entry | close and allow next valid project while window remains | apply reward twice | clear active flag, keep wave-use guard |
| Failed by target loss | failure explanation | close mission and allow another project if window and posture permit | transfer mission to new controller | clear target and active flag, bounded refund if accepted |
| Failed by annexation | normally no player display after country death | none | retain dead-country mission | full country cleanup |
| Cancelled by player | show lost effort and accepted refund | allow later project if window remains | full refund after meaningful elapsed time | clear target, active flag, and stored temporary state |
| Window expired before start | category hides when no other reason remains | none | start a new project | remove unused target markers and posture at expiry |
| Window expired during active project | mission remains visible until resolution | complete or fail | start another project | remove posture access after project, then hide category |
| New Event 064 wave during active project | new report can replace posture, active mission remains if valid | complete or fail under stored rules | duplicate old reward through new wave | maintain one active-project cap and separate wave ids |

## Targeted-decision map behavior

| Project | Map target style | Visible target cap | Invalid target explanation | Distribution need |
| --- | --- | ---: | --- | --- |
| Reinforce sector | state target on current affected border states | show all valid map targets, avoid list duplication | at cap, no current foreign frontier, state not controlled, used this wave | player chooses strategic sector |
| Connect line | state target on affected border or redoubt states with network gap | show top valid target family through map interface | no network gap, state lost, insufficient transport reserve, used this wave | prioritize poor supply and important line |
| Breach exercises | target country first, then objective state when supported | bounded top target set, suggested cap eight | no meaningful forts, no plausible war route, target ally, target invalid | prioritize current enemies and planned targets |
| Air or coastal flank | state target on selected Fortress States | show valid selected states only | no air or coastal role, all relevant buildings capped, state lost, used this wave | spread across high-value sectors |
| National redoubt | state or province target on bounded internal candidates | suggested cap six | no strategic role, at cap, state lost, redoubt already used this wave | capital first, then supply and VP spread |

## AI decision matrix

| AI condition | Preferred posture | Preferred first project | Secondary project interest | Skip reason |
| --- | --- | --- | --- | --- |
| capital under direct land threat | Integrate | Reinforce capital-front sector | National Redoubt at Evolution III | no valid target or immediate state loss certain |
| weaker country in defensive war | Integrate | Reinforce weakest core border sector | Air defense when enemy air threat is high | equipment or manpower reserve failure |
| long stable frontier with supply strain | Keep Roads Open | Connect worst strategic route | Harden air or coastal flank | train or truck reserve failure |
| large army in poor infrastructure | Keep Roads Open | Connect supply-hub or rail state | National Redoubt if capital route weak | no material network change available |
| planned offensive against level five forts | Study the Breach | Conduct Breach Exercises | Harden forward air flank | low Army Experience, support equipment, or fuel |
| winning offensive with unfortified targets | valid local defense or logistics posture | local useful project | low | no meaningful fortified target for breach |
| island country planning continental war | Study the Breach | Conduct Breach Exercises | National Redoubt at Evolution III | no plausible target route |
| island country under naval threat | Integrate or Keep Roads Open after Fortress World redoubt | National Redoubt | Air or coastal project only when accepted target rules allow it | no local redoubt and no valid project |
| tiny one-state country | Integrate when threatened | scaled Reinforce or Redoubt | normally none | cannot preserve reserve floors |
| selected Fortress State with industry under bombing | Integrate or Keep Roads Open | Harden air flank | Connect line | AA and radar already capped |
| key border port threatened by invasion | Integrate or Keep Roads Open | Harden coastal flank | Connect line | no valid coast or port role |
| special Chaos actor with normal building map but no civilian economy | owner-defined or none | none unless owner contract maps an equivalent cost | none | unsupported ordinary decision systems |

## Refund principles

| Failure timing | Suggested refund direction |
| --- | --- |
| project invalidates immediately before any daily progress | high partial refund, never above paid amount |
| project invalidates during first quarter | moderate partial refund of unconsumed material only |
| project invalidates during middle half | small partial refund or no refund depending on material type |
| project invalidates near completion | no refund |
| player cancellation | lower refund than involuntary invalidation at the same progress |
| annexation | no refund to dead country |
| target transfer caused by player exploit | no refund and challenge disqualification where relevant |

The final refund model must be simple enough to explain. Do not expose a long hidden component ledger.

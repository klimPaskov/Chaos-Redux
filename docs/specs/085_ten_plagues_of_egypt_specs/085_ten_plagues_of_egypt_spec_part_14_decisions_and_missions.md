# 14. Decisions, Costs, and Urgent Objectives

## One readable category

The Ten Plagues category header shows Divine Wrath, the current plague, the next deadline and, during Darkness, the Passover line (Part 7).
Divine Wrath is the only event-specific value.

- Three to five actions are visible at a time, never more than six.
- At most three Event 085 urgent missions run at once; Famine, Migration and Natural Disasters missions stay in their own categories.
- During Darkness, Passover takes priority over any new optional objective.
- Completed actions leave a one-line result and retire; past plagues do not leave permanent rows.
- No custom command GUI is needed; a phase picture (Part 16) is enough.

Unavailable actions name the exact missing target, resource, route or time.

## Cost model

Every action has one cost check, one payment, one objective, one result and one cleanup path.
An action shows at most three cost values with texticons; requirements such as a route are shown separately.

Material actions scale with the target state's population in **relief units** of 250,000 people, rounded up, minimum one.
The action offers only the variants that are physically valid for the state, and never combines them.

| Variant | Cost per relief unit | Notes |
| --- | --- | --- |
| Road | 10 trucks, 10 support equipment, 500 fuel | Needs a land route from a controlled supply source |
| Sea | 2 convoys, 500 fuel | Needs a port; island and coastal states |
| Rail | 2 trains, 10 support equipment | Needs working railway |
| Local organization | A timed −50% factory output penalty in the target state for the service window, plus 10 Political Power + 5 per relief unit | Always available where the state has people; no factory minimum |

Equipment is consumed: it wears out or is lost in relief work, so there is no reservation or return.
Holding exactly the shown amount is enough; nothing is debited if the action cannot start.
The local route gives a smaller country a real way to act through its own people's labor; it never kills or removes population and never creates manpower.
These amounts are tuning anchors in script constants.

## Action families

| # | Action | Phase and window | Target and objective | Variants | Result |
| ---: | --- | --- | --- | --- | --- |
| 1 | Harden Our Hearts | Any phase, once per phase | National policy | — | Part 2 policy effects, +15 Wrath |
| 2 | Heed: Safe Water | Blood, 10 days | Keep one affected state supplied with safe water | Road, sea, rail, local; industry shutdown variant (deeper local penalty, no equipment) | Removes most of the state's direct deaths and Famine shock; halves Frogs cleanup cost there |
| 3 | Heed: Frog Clearance | Frogs, 10 days, before the die-off | Clear one affected state's civilian services | Road, local; strategic-site variant (partial credit) | Prevents the state's sanitation aftermath |
| 4 | Heed: Infestation Control | Lice and Gnats, 10 days | Restore one affected state's services and shelters | Road, local | Cuts the state's disease exposure |
| 5 | Military Stand-Down | Lice and Gnats or Boils, 10 days | Pull exposed divisions back for treatment | National: −25% division attack for 10 days | Halves the phase's recovery and training penalty for the rest of the phase; partial credit only |
| 6 | Heed: Food and Sanitation | Flies, 10 days | Protect one affected state's food storage and sanitation | Road, sea, rail, local; half cost after completed water or frog work in the state | Cancels the state's Flies food shock and most disease exposure |
| 7 | Protect Rural Continuity | Livestock, 15 days | Protect one agricultural state | Road, local | Halves the state's Livestock shock; marks a surviving agricultural base |
| 8 | Heed: Civilian Care | Boils, 15 days | Sustain care in one affected state | Road, rail, local; half cost after completed infestation work in the state | Cuts the state's outbreak exposure; Doctor Wu care can join (Part 5) |
| 9 | Shelter Before the Storm | Hail warning, until impact | Shelter a warned state's population | Road, local; half cost in a state with completed care; site variant protects equipment or an air base (partial credit) | Shelter result passed to Natural Disasters |
| 10 | Preserve the Remaining Harvest | Locusts, until the front arrives | Move or protect food in the next threatened state | Road, sea, rail, local | Cancels most of the state's locust shock |
| 11 | Maintain Essential Service | Darkness, 72 hours | Keep one state's hospital, water and shelter network running | Road, local | Cancels most of the state's Darkness deaths |
| 12 | Observe the Passover | Darkness | National program or local preparation (Part 7) | National: 50 Political Power, 10 support equipment per relief unit of controlled population, +10% consumer goods for 7 days; local: local organization for one state | Passover status |
| 13 | Foreign Relief Pledge | Any phase | Pay the material cost of another country's active objective (Part 10) | Donor's stockpile pays the recipient's road, sea or rail variant | −5 donor Wrath on the recipient's completion, two per phase |
| 14 | Reconstruction Coordination | After the tenth plague | Restore one damaged state (Part 11) | Civilian factories for 90 to 180 days scaled by damage, plus Political Power | Completes on actual repair and food recovery |

Migration's **Evacuate Civilians** covers storm evacuation; Famine's **Release Food Stores** and **Import Food** cover reserves and imports.
Event 085 links to them and never copies them.

## Outcomes and credit

- **Full success**: the objective's state is still controlled and the full window elapsed (or the work finished before the impact or front).
It applies the protection and the full Wrath credit (−10), once per country per phase.
- **Partial success**: a site variant, Military Stand-Down, or work interrupted after at least half its window by capture or a destroyed route.
It applies half the protection and −5 Wrath; a later full completion in the same phase grants only the remaining −5.
- **Failure**: no protection and no credit; spent equipment stays spent.
Failure from capture, a destroyed route or lost access carries no blame; abandoning an achievable objective or diverting its equipment raises Wrath (Part 2).

A full credit requires the target to be a footprint state of the current plague, so small fragments cannot farm Wrath.
More objectives in the same phase still protect their states; they earn no further Wrath credit.
A renewed cycle has new phase credits and reuses nothing from the previous cycle except surviving physical work.

A late completion can still help an ongoing owner crisis but cannot protect people who already died.

## Transfer and cleanup

When a target state changes controller, its objective closes as a partial or failed result for the old controller, without false completion.
At phase end, unfinished objectives close with a result.
At episode end only Event 085's own actions, spirits and records close; Famine, Migration, outbreak and disaster aftermath remain.
The AI uses the same costs, windows and requirements as the player (Part 15).

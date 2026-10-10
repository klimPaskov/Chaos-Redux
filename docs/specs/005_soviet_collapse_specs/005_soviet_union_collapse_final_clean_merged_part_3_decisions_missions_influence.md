# Soviet Union Collapse Final Clean Merged Specification, Part 3
# Decisions, Missions, Influence, Mechanics, and Balance

## Special mechanics

Soviet Collapse must have special mechanics. They should not exist only as hidden variables. The player should see them through decision category headers, scripted localisation, event detail windows, national spirits, event logs, or scripted GUI when appropriate.

The crisis values, their source variables and the visible-value budget are defined once in Part 2.
Use those names and that budget here; do not introduce a parallel list or a new global meter for a decision family.
Per-republic influence work uses the existing sponsor influence, patronage risk and independence resilience values.

If a mechanic uses a scripted GUI, consider progress meters, fill variants, status icons, selected or locked variants, warning frames, and frame animation where useful. Visual motion should clarify the mechanic, not clutter it.

## Focuses and decisions must affect mechanics

Mechanic values must be changed by focuses, decisions, missions, events, wars, state control, foreign influence, AI actions, and prior outcomes. A focus tree must not sit beside the mechanic without changing it. A decision system must not sit beside the mechanic without changing it.

Mechanic values should unlock or block content:

- focuses
- decisions
- missions
- events
- leaders
- advisors
- laws
- factions
- war goals
- reforms
- crises
- achievements
- super-events
- endings

## Mission type rules

Use the right mission type.

Clickable decisions are for chosen actions, such as sending officers, opening an aid corridor, authorizing construction, recognizing a republic, issuing an ultimatum, or starting a crackdown.

Timed missions are for deadlines, such as holding capitals, guarding depots, controlling rail hubs, placing supplied divisions in named states, or keeping foreign liaison offices out.

Goal-style objectives are for conditions that should auto-complete when met. The player should not need a second click after already satisfying the condition.

Union Crisis objectives are goal-style missions, not normal store purchases.

## Mission quality

Remove duplicate and boring passive missions.

Forbidden mission patterns:

- have 20,000 manpower
- have 500 rifles
- have stability above 35 percent
- have war support above 35 percent
- own a tiny generic stockpile
- wait for a passive condition
- pay political power to reduce a meter
- repeat the same threshold under another name

Good missions require action:

- place supplied divisions in named states
- hold named capitals
- secure named rail hubs
- guard named depot belts
- keep a capital connected to supply
- block a foreign liaison chain
- escort a rail repair mission
- open or close a named aid corridor
- improve relations with a specific republic
- send equipment through a decision
- win an influence threshold contest
- prevent a regional release by completing local support work
- rebuild railways or supply hubs in named regions

Even easy missions must require real action. Easy means lower risk or smaller scope, not passive.

## Mission duration

Use varied mission durations.

- easy missions: at least 90 days, often 90, 95, 100, 105, or 110 days
- medium missions: 120 to 180 days
- hard missions: half a year or a full year

Emergency missions can be shorter only if the event story clearly requires immediate danger.

Do not give every mission the same deadline.

## Mission clarity

Every mission must explain what it requires.

If the mission requires capitals, name the capitals:

- `Hold Kyiv and Minsk for 120 days`
- `Hold Tbilisi and Baku until the Caucasus Congress meets`
- `Hold Tashkent, Dushanbe, and Ashgabat during the Southern Cascade`
- `Hold Tallinn, Riga, and Kaunas for the Baltic League vote`

If the mission requires borders or regions, name the region and define it in tooltip or scripted localisation:

- Western Rail Belt
- Dnieper Defense Line
- Baltic Coastal Belt
- Caucasus Pass Line
- Central Asian Pass Line
- Volga-Ural Interior Line
- Siberian Rail Corridor
- Far Eastern Port Line
- Black Sea Littoral
- Dniester Line

If the mission requires depots or rail hubs, name them:

- Kyiv Depot Belt
- Minsk Switchyards
- Baku Oil Rail
- Tashkent Rail Offices
- Trans-Siberian Corridor

Do not show vague requirements like required states, border states, nearby states, key states, sufficient troops, or enough equipment unless scripted localisation names the actual target list.

## Cost localisation

Cost localisation should be short, readable, and icon-first.

Do not prefix every blocked line with `Requires` or `Needed`. In most cases, show only the value and icon.

Examples:

- `2,000 <infantry_equipment_texticon>`
- `20 <army_xp_texticon> 20 <command_power_texticon>`
- `200 <support_equipment_texticon>`
- `Depot control`

Do not add filler words such as `and` between costs.

If the country does not meet a requirement, show the missing or unmet cost in red. If the country meets it, show it normally.

If more than three or four costs or requirements appear at once, show a scripted localisation summary:

- met: `Requirements met`
- not met: `§RRequirements not met§!`

The full tooltip should still use icon-first entries, red for missing requirements and normal colour for satisfied requirements.

## Influence war

Major powers must be able to compete for influence over republics.

Track influence per sponsor and republic. Categories should include:

- recognition
- arms
- volunteers
- industrial investment
- intelligence
- ideology
- logistics
- patronage risk

Sponsors can include Germany, United Kingdom, Japan, France, United States, Turkey, Iran, Poland, Romania, Finland, Sweden, Italy, the Free Republics' League, and Moscow.

Influence decisions include:

- Recognize De Facto Authority
- Fund Civilian Construction Mission
- Fund Military Construction Mission
- Send Equipment Convoy
- Transfer Volunteer Formation
- Send Officer Cadres
- Open Intelligence Liaison Office
- Sponsor Press and Radio Network
- Secure Aid Corridor
- Build a League Conference
- Expose Foreign Patronage
- Counter-Sponsor Radio Campaign
- Offer Better Guarantees
- Demand Anti-Puppet Clause

The volunteer formation transfer should remove or consume sponsor military capacity and spawn a corresponding force for the republic. If exact division transfer is not clean in HOI4 script, remove manpower, equipment, and template-linked force capacity from the sponsor and spawn an equivalent force in the target. Document the substitute.

## Stackable intervention ideas

Intervention ideas should mature through action.

Required stackable families:

| Family | Weak form | Strong form | Risk form |
| --- | --- | --- | --- |
| Recognition | Unrecognized Authority | Treaty-Backed Republic | Sponsor-Defined Legitimacy |
| Reconstruction | Foreign Relief Credits | Sovereign Reconstruction Board | Dependent Construction Network |
| Volunteers | Medical Volunteers | International Defense Corps | Sponsor-Directed Command |
| Advisers | Observer Mission | Joint Staff Mission | Foreign-Run Staff |
| Arms | One Shipment | Arms Pipeline | Sponsor Arsenal Dependence |

Balanced sponsorship strengthens independence. One dominant sponsor raises puppet risk.

## Peaceful reintegration and puppeting

Moscow can use low-threat influence to reintegrate, federate, or peacefully dominate a weak republic.

Moscow decisions include:

- Offer New Union Treaty
- Restore Rail Board Partnership
- Recognize Republican Emergency Authority
- Shared Security Amnesty
- Joint Depot Accounting
- Economic Reconstruction Credits
- Party Reconciliation Mission
- Invite Local Officers into Union Command
- Autonomy Statute Guarantee
- Federal Court Mediation

Foreign puppet attempts require dominant influence, low republic resilience, weak or isolated target, no strong league protection, and a valid diplomatic path. Puppeting should be a chain, not a single button.

## Decision category clutter control

Do not show every possible decision at once. Use phases, caps, priorities, route locks, regional pools, mechanic thresholds, and crisis-state filters. Categories should feel curated by current state, not like a debug menu.

Use:

- early, middle, and late tiers
- active mission caps
- regional mission pools
- route-specific decision families
- replacement of basic decisions by stronger later versions
- cleanup after war, settlement, collapse, or route change

The Soviet Union Crisis category must never show more than ten active Soviet objectives at once.

## Balance and exploit review

Balance review must check:

- initial values
- daily, weekly, and monthly changes
- success effects
- failure effects
- auto-completion effects
- MTTH release effects
- local league formation effects
- influence effects
- focus rewards
- AI use
- active mission counts
- cleanup behavior

Also check exploits:

- free unit loops
- repeated factory rewards
- cheap construction loops
- equipment farming
- influence farming
- puppet abuse
- war-goal spam
- claim or core spam
- advisor discount stacking
- focus bypass abuse
- repeated mission success farming
- decisions with no meaningful cost or risk

Fix exploits with flags, cooldowns, dynamic costs, escalating costs, target limits, route locks, AI limits, cleanup effects, one-time completion flags, or scripted triggers.

## Shared Chaos Redux system connections

The crisis runs inside the mod's shared systems, so it must use them instead of restating their work.

Already connected in current source:

- Camps and repression read the crisis directly.
  `is_soviet_collapse_active`, `soviet_collapse_total_collapse_threat` and `soviet_collapse_terminal_collapse` drive the Soviet gulag and repression surface, and `soviet_collapse_apply_genocide_gulag_repression_memory` calls `camp_rework_soviet_apply_union_crisis_repression_bridge` in the other direction.
  UWR blacksite intake registers real camp sites through the camp system rather than a private ledger.
- Front movement feeds the humanitarian systems automatically.
  `on_state_control_changed` calls the hostile-capture adapter, which adds bounded war flight pressure and queues one famine food assessment for the captured state, so every reclamation offensive, league war and terminal rupture already produces refugees and food strain.
  Event 005 must not add a second famine or migration request for the same fighting.
- Combat casualties and civilian deaths reach the Chaos Meter deaths ledger through the daily casualty update, so the crisis needs no private casualty accounting.
- CBRN use by UWR or any other successor is owned by the CBRN and condemnation systems, which apply their own condemnation sources and sanctions.

Proposed (spec audit 2026-10-10):

- The crisis contributes nothing to the Chaos Meter value itself, although it is one of the mod's largest political ruptures.
  Add one bounded `add_chaos_meter_value` contribution at the terminal moment, sized from the realized rupture rather than from a timer, matching how other world-end branches report themselves.
  Ordinary stage progress should stay silent so a contained crisis cannot farm chaos.
- Gulag geography should push back on the crisis it already reads.
  A republic whose states carry live camp sites should start with higher Armed Breakaway Momentum, and an accepted dismantlement route should reduce it, using the existing camp site count and dismantlement markers instead of a new value.
- A republic released into a state already under famine stage pressure should inherit that pressure as a visible opening problem rather than a clean slate, using the famine system's existing state values.

## Implemented Command and Corridors addendum (2026-07-11)

The 118 numbered Soviet missions remain the only crisis objective pool. They are classified once into 37 Chain of Command missions, 21 Corridors and Depots missions, and 60 Republic Settlement missions. At the existing refill, Moscow computes family pressure from Authority, Obedience, Republic Confidence, Depot Vulnerability, Foreign Appetite, League Cohesion, and Old Movement pressure. It then attempts at most one mission from each family in priority order before running the unchanged 118-mission remainder. The existing active-objective cap, monthly refill cap, mission identifiers, completion flags, and refill event remain authoritative.

The priority bands use Authority 50, Obedience 48, Republic Confidence 42, and Depot Vulnerability 30 as the crisis posture baseline. The opening choice then changes those safe bands before the first board is filled: an Indivisible Union raises the Authority and Obedience floors by 5; an Autonomy Settlement lowers the Republic Confidence ceiling by 5; Isolating the Separatists lowers the Republic Confidence ceiling by 2 and the Depot Vulnerability ceiling by 5; restoring discipline raises the Authority floor by 2 and the Obedience floor by 5. The first objective fill occurs after the opening option has set its posture and applied its component changes.

Each family has one shared compromise decision. A command compromise costs 15 command power and shifts Authority +1, Obedience +1, and Republic Confidence +2. A corridor compromise costs 35 political power and shifts Depot Vulnerability -2, Authority -2, Foreign Appetite +1, and League Cohesion +2. A settlement compromise costs 50 political power and shifts Republic Confidence -2, Authority -2, Foreign Appetite +1, and League Cohesion +2. The resolver concludes exactly one live family mission, marks its existing done flag, removes the mission without firing completion or timeout, queues the existing refill, and increments neither monthly successes nor failures.

Corridor-family activation requires a live state pointer selected from original Union territory that Moscow still owns and controls. Candidates must be passable and contain or connect a supply node, naval base, railway route to the capital, or contested border. Every one of the 21 corridor missions requires its selected state's matching rail, depot, logistics, or border condition before explicit activation, repeats that condition in availability, and uses it to cancel an invalidated project. If the state stops qualifying, the mission cancels into the existing refill path without recording success or failure; if no candidate exists, the family is suppressed. No substitute state is hardcoded.

The Moscow and foreign-patron desks use target arrays plus a selected-target flag for human display. Action-specific permission remains in `available`; selection alone is never authorization. Normal hide/show does not remove or reactivate cooldown-bearing rows. Actual target resolution performs symmetric owner/target cleanup. Post-Union-Unmade use is a converted wartime surface rather than a continuation of obsolete treaty and recognition actions.

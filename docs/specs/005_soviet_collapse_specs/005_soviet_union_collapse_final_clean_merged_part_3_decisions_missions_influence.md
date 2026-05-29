# Soviet Union Collapse Final Clean Merged Specification, Part 3
# Decisions, Missions, Influence, Mechanics, and Balance

## Special mechanics

Soviet Collapse must have special mechanics. They should not exist only as hidden variables. The player should see them through decision category headers, scripted localisation, event detail windows, national spirits, event logs, or scripted GUI when appropriate.

Important values must be dynamic and coloured consistently. Values can include:

- Moscow Authority
- Union Collapse Threat
- Command Obedience
- Armed Breakaway Momentum
- Foreign Penetration
- Old Movement Resurgence
- League Cohesion
- Local Support
- Sponsor Influence
- Patronage Risk
- Independence Resilience
- Balance of Power values for internal struggles

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

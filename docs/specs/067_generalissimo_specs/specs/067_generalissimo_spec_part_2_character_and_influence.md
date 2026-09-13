# Event 067 Character and Influence System

## The canonical character

The Generalissimo is one event-owned fictional male character. His public identity is the title Generalissimo. The event does not need a grounded personal biography, a claimed real nationality, or a connection to a historical commander.

The character should look plausible within the 1936 to 1945 visual language while remaining difficult to place. His uniform may combine period officer tailoring with event-owned insignia, but it must not copy the insignia, face, or personal identity of a real military leader.

### Character ownership rules

- Event 067 creates the character once.
- The character belongs to one country at a time.
- Commander promotion does not create another token.
- Transfer to the junta removes him from the original government before adding him to the junta.
- Peaceful submission keeps the same token in the same country and adds the country-leader role.
- Government victory, successful removal, or successful assassination permanently disables the character.
- Ordinary age, retirement, random death, sickness, wounding, or generic commander events must not remove or weaken him.
- Scripted Event 067 removal outcomes remain valid.
- Event 065 may grant Generalissimo ruler traits to other leaders, but it never creates another Event 067 character.

## Commander implementation contract

The implementation must inspect the current engine limits and installed traits before building the package. The words maximum and every mean the highest safe values supported by the current game version, not remembered numbers from an older version.

### Required commander attributes

The Generalissimo must receive:

- the highest supported army leader skill
- the highest supported Attack value
- the highest supported Defense value
- the highest supported Planning value
- the highest supported Logistics value
- the maximum useful command capacity
- the maximum useful army-group capacity where a commander modifier can affect it
- all safe positive general traits
- all safe positive field marshal traits
- all safe positive terrain traits
- all safe positive logistics, planning, organization, recovery, entrenchment, breakthrough, armor, infantry, special-forces, and combined-arms traits
- all safe positive naval-invasion or amphibious army traits when those are commander-applicable
- all positive Chaos Redux army-leader traits that do not require an incompatible actor type

The package may include contradictory positive specializations. A commander can be an armor expert, infantry expert, defensive planner, offensive planner, logistics master, organizer, and terrain specialist at the same time when the engine accepts the combination.

### Exclusions from the trait package

The implementation must exclude:

- negative traits
- illness and wound traits
- traits that exist only as internal markers
- traits that break the commander role when applied outside their owner system
- mutually exclusive traits that the engine cannot safely hold together
- traits whose effects require a nonhuman unit family or unrelated event actor
- hidden traits that would start another event or mutate the character
- country-leader traits that belong to another living character

Every exclusion must appear in a generated commander-trait audit. The audit should list the candidate trait, whether it was included, and the reason for any exclusion.

### Direct command after political takeover

The Generalissimo must remain available as an active army leader after becoming head of state. He should appear in the command interface and retain his full statistics and traits.

The implementation must test:

- peaceful submission
- civil-war creation
- junta victory
- save and reload
- tag or cosmetic identity changes
- focus-tree loading

A ruler-only clone and a commander-only clone are prohibited. If the engine cannot keep one token in both roles, the implementation is blocked until the conflict is resolved explicitly.

## Dedicated country-leader trait family

When the Generalissimo becomes ruler, he receives the complete Event 067 ruler trait family. The family is intentionally far stronger than ordinary country-leader traits.

The working trait identifiers and roles are:

| Working identifier | Mechanical role | Required effect direction |
| --- | --- | --- |
| `generalissimo_supreme_command` | National command authority | Very large organization, planning, reinforcement, command power, army experience, and army-leader capacity effects |
| `generalissimo_master_of_operations` | Battlefield direction | Very large division attack, defense, breakthrough, planning speed, coordination, and operational tempo effects |
| `generalissimo_logistical_dominion` | Supply and movement | Very large supply, attrition, fuel, transport, recovery, and logistics effects |
| `generalissimo_arsenal_state` | Military mobilization | Very large training, mobilization, military production, conversion, repair, and doctrine-development effects |

The exact modifiers must be inspected against current vanilla and Chaos Redux support. Unsupported modifier keys are not to be invented.

### Power standard

The complete four-trait package should make the Generalissimo-led state visibly stronger in land warfare than an ordinary country with similar industry and divisions. The package should be capable of changing the outcome of a major war.

It should not provide unlimited equipment, free factories, automatic annexation, instant doctrine completion, or immunity from supply. The state still needs an army, equipment, territory, and a functioning economy.

### Event 065 integration

Each of the four traits enters the Event 065 Random Trait pool as an individual trait.

Rules:

- Event 065 can grant one trait from the family through an ordinary random roll.
- Later Random Trait evolutions may increase the weighting of these extreme traits.
- Repeated Event 065 firings can place more than one family trait on another leader if independent rolls select them.
- Another leader who receives one or more traits does not gain the Event 067 commander, Influence system, decision category, focus tree, or world-end ownership.
- Only the original Event 067 Generalissimo receives the complete package automatically.
- The trait family must use a marker that lets Event 065 classify it as extremely powerful without hardcoding four separate special cases in unrelated files.

## Formal command authority

The event uses four qualitative command states. The current state is visible, but it is not a second numerical meter.

| State | Public meaning | Military use | Influence behavior |
| --- | --- | --- | --- |
| Advisory Reserve | The Generalissimo advises without a national field command | Personal commander remains available, but no additional national command package applies | Influence decays slowly during peace and rises little from victories |
| Theater Command | The government gives him one major theater | Strong campaign tools and normal battlefield credit | Moderate influence growth from relevant victories |
| National Field Command | He directs most land operations | Strong national planning and coordination support | High influence growth from victories and authority |
| Supreme Command | He controls the armed forces in practice | Maximum national command support before takeover | Very high influence growth and stronger demands |

The initial state is Theater Command.

### Changing authority

The government changes authority through decisions, demands, and crisis outcomes.

- Expanding authority gives immediate military value and raises the rate at which success becomes political influence.
- Restricting authority weakens the military for a meaningful period and reduces future influence growth.
- The Generalissimo can demand National Field Command or Supreme Command.
- A government that publicly grants a demanded command level takes a larger influence increase than a government that quietly expands his operational responsibility.
- A government cannot repeatedly lower and raise command authority to farm temporary bonuses. Cooldowns, one-time authority milestones, and lost-prestige memory prevent cycling abuse.

## Generalissimo Influence

Generalissimo Influence is a country-scoped value from 0 to 100. It represents how many military and political actors believe that resisting him is dangerous, futile, or illegitimate.

It combines public prestige, command authority, officer loyalty, access to force, institutional concessions, and the belief that the armed forces will follow him.

### Public bands

The labels below are working design labels. Final player-facing wording belongs to implementation.

| Influence | Working state | Public consequence |
| --- | --- | --- |
| 0 to 24 | Decorated Asset | Retirement and dismissal remain practical. The officer network is limited. |
| 25 to 44 | Indispensable Commander | Demands gain weight. Safe removal becomes costly. |
| 45 to 64 | Supreme Command | A large part of the officer corps expects him to lead. Coercive removal is risky. |
| 65 to 84 | State Within the State | He controls important commands and institutions. A revolt can claim a large military share. |
| 85 to 99 | Personal Regime Imminent | The government is close to losing effective authority. Final countermeasures are severe. |
| 100 | Ultimatum Ready | Evolution III can produce the final demand after its pacing gate. |

Influence is clamped at 0 and 100.

### Hidden components

The event may track these hidden components:

- public prestige
- officer loyalty
- operational mandate
- internal-security reach
- military-industry reach
- regional-command support
- loyal formation support
- government counterweight strength
- personal-security exposure

These values exist for calculation, AI, revolt setup, and removal chances. They must not appear as persistent public numbers.

The category can explain the strongest current causes through short qualitative statements, such as broad officer support, control of armament boards, weakened civilian command, or isolated loyal formations. It should not show the complete component ledger.

## Influence gain model

Influence should change through discrete outcomes and one bounded event-owned pulse. The pulse runs only for the active host and does not scan every country.

### Command authority gains

Suggested one-time influence targets:

| Action | Influence direction |
| --- | --- |
| Grant Theater Command at initial appointment | No additional gain because it is the starting state |
| Expand to National Field Command | Moderate immediate gain |
| Grant Supreme Command voluntarily | Large immediate gain |
| Accept a public demand for command authority | Larger gain than a quiet voluntary grant |
| Restore authority after previously restricting it | Large gain and a memory penalty against future restriction |

The exact values are script constants. They should produce a meaningful difference between gradual use and immediate surrender of command.

### Military outcome gains

The event should credit only major outcomes. Routine battles, small state changes, and ordinary casualty ticks must not farm Influence.

Eligible outcomes include:

- capitulation of a hostile major while National Field Command or Supreme Command is active
- capitulation of a meaningful hostile minor when the host was losing or outmatched
- capture of an enemy capital
- recapture of the host capital
- defense of the host capital through a defined high-risk period
- capture or defense of a dynamically selected major command state
- completion of the campaign mission tied to his command
- a major reversal in the host's war situation
- defeat of a substantially stronger enemy offensive

Each outcome uses a one-time state, enemy, war, or mission guard. The same capital cannot generate repeated influence through occupation cycling.

### Political and institutional gains

Influence can rise when the government:

- publicly promotes him
- gives him appointment authority
- removes a rival commander at his request
- expands the military budget under his control
- transfers armament boards or strategic industries
- places internal security under military command
- grants emergency powers
- gives him a foreign-policy veto
- protects loyal officers from investigation
- accepts propaganda centered on his personal leadership

Each concession must give a real benefit or avoid a real penalty. The player should understand why granting it is tempting.

### Passive pulse

The recurring pulse should use a base interval near 30 days. The exact interval and gains are centralized.

Potential positive factors:

- National Field Command
- Supreme Command
- active war
- recent victory
- low stability
- high war support centered on military leadership
- accepted demands
- strong officer network
- Generalissimo control of armament or security institutions

Potential negative factors:

- Advisory Reserve
- peace
- high civilian oversight
- strong loyal reserve command
- dispersed arsenals
- removed loyal officers
- recent defeat under his mandate
- public scandal or failed demand

The monthly change should remain small compared with major decisions and military outcomes. The system should reward action and consequences, not waiting.

## Influence reduction model

Influence reduction must cost something the player can feel.

### Command restrictions

Reducing command authority can lower ongoing influence growth and remove part of his national command bonus. It should also apply temporary penalties to planning, organization, command power, or coordination because units must adjust to a new chain of command.

### Civilian oversight

A civilian oversight program uses political authority and civilian capacity. It lowers hidden institutional reach over time. It may temporarily reduce planning speed, army experience gain, or military factory efficiency because procurement and appointments are being reviewed.

### Counterweight commands

The government can create parallel or loyal command structures. These actions reduce coup coordination and removal risk while imposing military costs.

Possible costs include:

- command power
- army experience
- support equipment
- infantry equipment
- tied-down divisions
- duplicated headquarters
- reduced planning coordination
- reduced army experience gain
- civilian factory burden

The research basis for this tradeoff is that coup-proofing can strengthen regime security while reducing military effectiveness. The implementation should express that relationship in play instead of giving a free influence-reduction button.

### Officer rotation and removal

Rotating regional commanders, retiring loyal officers, and splitting elite formations reduce the hidden network. These actions can lower Influence directly when the Generalissimo lacks enough power to block them.

At high influence, an aggressive purge can raise short-term coup risk. The player should be able to prepare by strengthening civilian command and securing key states before removing officers.

### Defeat and public failure

A serious defeat while the Generalissimo holds National Field Command or Supreme Command can lower public prestige and Influence. This reduction should not reward the player for deliberately losing small battles.

Eligible failures include:

- loss of the host capital
- loss of a major command state
- failure of the campaign mission
- capitulation of an allied major that he publicly promised to defend
- a large war-situation reversal during his command mandate

A failure can also weaken the country. Influence reduction is not a free reward for poor play.

## Stable coexistence

The event must support a long-lived managed state.

A player should be able to:

- keep the Generalissimo at Theater or National Field Command
- use him in selected wars
- accept some demands and reject others
- maintain Influence in a middle band
- periodically rotate commands or strengthen oversight
- avoid the final ultimatum without dismissing him

The cost is lower maximum military output, repeated command disruption, and resources spent on oversight or counterweights.

Influence should not drift inevitably upward during peace when he has limited authority. A country that keeps him in Advisory Reserve and maintains strong institutions should see gradual decline.

## Demand generation

Demands begin after Evolution I. They use a bounded pool and a cooldown. The system shows no more than one active demand at a time.

Demand selection considers:

- current command authority
- current Influence band
- accepted and rejected prior demands
- war state
- army size
- military factory count
- available commanders
- current internal-security and industry ownership
- active focus route after takeover, if any
- whether a requested institution exists

A demand that is already satisfied, impossible, or irrelevant receives zero weight.

### Evolution I demand families

- formal Supreme Command
- appointment authority
- removal of a rival commander
- military budget expansion
- operational-planning authority
- protection for loyal officers
- public promotion

### Evolution II demand families

- control of military production
- emergency powers
- loyal officers in government
- authority over internal security
- foreign-policy veto
- removal of political opponents
- control of strategic industries
- creation of a permanent military council

### Accepting and rejecting demands

Accepting a demand gives the requested benefit, avoids its immediate penalty, and raises Influence.

Rejecting a demand should normally:

- lower his public standing when the government is strong
- raise officer anger when the government is weak
- create a timed mission or temporary military penalty
- increase the weight of a stronger future demand
- expose whether the government still controls the chain of command

Rejecting an ordinary demand does not automatically start a revolt. The final ultimatum is the only direct submit-or-revolt demand outside a failed coercive removal.

## Contextual overlays

These overlays add replay value without creating separate public meters or full alternate event trees.

### War Hero opening

A host that is losing a major war can receive a faster service-record start. Military outcomes have greater Influence impact because the government visibly depends on him.

### Peacetime idol

A stable peaceful host has lower early military gain but stronger public-promotion opportunities. Influence grows through prestige and officer politics instead of battle.

### Dual marshal rivalry

If the host leader is already a military ruler or active field marshal, the crisis begins as a hierarchy conflict. The existing ruler may co-opt him, restrict him, or attempt removal earlier. The Generalissimo remains the unique Event 067 character.

### Claimant rival

If Event 019 has created a valid claimant commander in the host, the officer corps begins divided. Unified coup coordination is weaker, but a revolt can split into more than two military camps when Event 019 ownership rules permit it.

### Maritime command

A host with a major navy and several naval bases can develop a fleet-centered network during Evolution II. Government countermeasures must secure ports and admirals, while revolt strength can include a meaningful naval split.

## Influence display requirements

The crisis category should show:

- Generalissimo portrait
- Influence meter from 0 to 100
- current qualitative Influence band
- current command authority state
- rising, stable, or falling trend
- next public threshold
- one or two strongest current causes
- the active demand or mission

It should not show:

- raw hidden component values
- a full probability formula
- internal variable names
- tuning caps
- debug labels
- a list of every past influence change

A short tooltip may show the latest meaningful gains and losses. The event history and crisis events can provide the longer narrative record.

## Post-takeover value replacement

When the Generalissimo becomes ruler, Influence closes and is no longer displayed.

The military state uses Command Cohesion from 0 to 100 as its only persistent custom government value. Command Cohesion represents agreement among the Generalissimo, senior officers, regional commands, and state administrators.

The replacement prevents the player from managing two overlapping military-politics meters.

Command Cohesion is covered in the country and focus-tree specifications.

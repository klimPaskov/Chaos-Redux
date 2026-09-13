# Event 067 Decisions, Missions, and Removal

## Presentation choice

The pre-coup crisis uses an ordinary decision category with a compact attached display. A separate full-screen mechanic window is not justified because the player manages one public value, one qualitative command state, one active demand, and a small set of current actions.

The category uses phase-based visibility:

- three to five primary decisions visible at one time
- one or two active missions visible at one time
- no more than six primary actions in any state
- obsolete actions removed when a phase, demand, war, or removal attempt ends
- emergency removal actions grouped under one revealed response family

The category picture changes by Influence band. The art is presentation only and contains no painted buttons, meters, numbers, or fake controls.

## Cost model

Every action uses at most four spendable cost types. Costs should be scaled from central constants and the host's army, industry, and war situation.

Useful cost families include:

- command power
- army experience
- political power for genuine constitutional or administrative actions
- infantry equipment
- support equipment
- motorized equipment
- trains
- fuel
- manpower
- stability
- war support
- temporary civilian factory burden
- temporary military factory burden
- tied-down divisions represented through missions or temporary modifiers

Command power costs may never exceed 60.

Player-facing cost strings must use matching texticons and compact amount-first formatting. Requirements such as holding a capital or placing supplied divisions in a state remain separate from costs.

## Command-use decisions

### Expand to National Field Command

**Availability**

- Generalissimo present
- current authority below National Field Command
- no active removal operation
- country has a meaningful army

**Player action**

The government gives him authority over national land operations for a defined period.

**Costs**

- moderate command power
- moderate army experience
- optional war-support or civilian-authority consequence when used during peace

**Effects**

- authority becomes National Field Command
- strong temporary national planning and coordination support
- Influence rises once
- military victories can grant greater Influence
- a command mission may begin

**Tradeoff**

The decision gives immediate wartime value and makes later restriction more disruptive.

**AI direction**

Losing or threatened AI countries should favor it. Stable peaceful countries should be cautious.

### Grant Supreme Command

**Availability**

- Evolution I active
- authority at National Field Command
- no active removal operation
- demand state or voluntary grant route permits it

**Costs**

- high command power within the hard cap
- army experience
- political authority
- temporary civilian oversight loss

**Effects**

- authority becomes Supreme Command
- strongest pre-takeover national military support
- large one-time Influence increase
- officer-network growth accelerates
- stronger demands become eligible

**Tradeoff**

This is the most powerful way to use him before takeover and the fastest way to make removal dangerous.

**AI direction**

AI should favor it only when the military benefit can plausibly decide an important war or when a military regime is already willing to yield authority.

### Return Him to Advisory Reserve

**Availability**

- no active final ultimatum
- no active forced-removal operation
- government retains enough command authority

**Costs**

- command power
- army experience
- temporary planning and organization disruption

**Effects**

- authority falls by one or more steps depending on preparation
- national command bonuses weaken or end
- future passive Influence growth falls
- Influence may decline after a delay
- a high-Influence Generalissimo can refuse the order

**Failure behavior**

A refusal raises Influence, exposes weak civilian control, and locks safe command restriction for a period. It does not automatically cause revolt unless it occurs as the final Evolution III removal attempt.

## Concession decisions

Concessions should be attractive because they grant military or political help, resolve an active demand, or avoid immediate disruption.

### Public Promotion

**Meaning**

The government turns battlefield prestige into an official national campaign.

**Costs**

- political power
- temporary propaganda or civilian-factory burden

**Effects**

- war support or army morale improves
- public prestige and Influence rise
- future retirement becomes harder

**Limits**

One main promotion per campaign, with smaller follow-up recognition handled through events. It cannot be repeated for free war support.

### Give Authority Over Appointments

**Meaning**

The Generalissimo chooses important army commands.

**Costs**

- army experience
- political authority

**Effects**

- officer effectiveness rises
- loyal-officer network grows
- Influence rises
- future government commander rotations become more expensive

### Expand the Military Budget

**Meaning**

The armed forces receive priority access to production and construction.

**Costs**

- temporary civilian factory burden
- fuel or equipment commitment where appropriate

**Effects**

- military production or training improves for a bounded period
- military-industry reach grows
- Influence rises

**Limits**

The benefit uses a timed package and cannot become a permanent free production multiplier through repeated acceptance.

### Protect Loyal Officers

**Meaning**

The government blocks investigations or dismissals of his supporters.

**Costs**

- political power
- stability or government legitimacy consequence

**Effects**

- immediate officer-cohesion benefit
- hidden officer loyalty rises
- Influence rises
- future purges become more dangerous

### Transfer Operational Planning

**Meaning**

The Generalissimo receives exclusive authority over major offensives and defenses.

**Costs**

- command power
- army experience

**Effects**

- planning speed and coordination improve strongly
- Influence rises
- war missions credit him more heavily

## Evolution II concessions

### Transfer the Armament Boards

**Meaning**

Military production decisions move under his direct staff.

**Costs**

- political authority
- temporary production reorganization

**Effects**

- military production, conversion, or repair improves
- military-industry reach rises sharply
- the junta receives a larger stockpile and factory share if revolt occurs

### Put Internal Security Under Army Command

**Meaning**

Military officers take responsibility for internal order and counterintelligence.

**Costs**

- political power
- command power
- stability or civil-liberty consequence

**Effects**

- resistance and subversion control improve
- internal-security reach rises
- arrest and assassination chances against him fall
- Influence rises

### Grant Emergency Powers

**Meaning**

The government gives him temporary authority to bypass ordinary institutions.

**Costs**

- stability
- political authority
- civilian-factory burden

**Effects**

- mobilization, command, and crisis response improve
- emergency powers create a major Influence increase
- Evolution III pacing accelerates

**Limit**

Emergency powers expire unless renewed. Renewal is more costly and gives greater Influence.

### Give a Foreign-Policy Veto

**Meaning**

The Generalissimo can block peace, guarantees, interventions, and alliance changes that affect military planning.

**Costs**

- political authority
- diplomatic flexibility

**Effects**

- selected military diplomacy actions improve
- the government loses access to some contradictory choices
- Influence rises
- aggressive foreign-policy demands become eligible

### Place Loyal Officers in Government

**Meaning**

Senior officers receive cabinet, security, or administrative posts.

**Costs**

- political authority
- stability risk

**Effects**

- administration and military coordination improve
- officer network and regional support rise
- peaceful submission becomes more likely for AI
- future purges become more disruptive

## Counterweight decisions

### Rotate Regional Commands

**Meaning**

The government moves senior officers between commands before local loyalty networks become permanent.

**Costs**

- command power
- army experience
- temporary planning disruption

**Effects**

- officer loyalty and regional-command support fall
- Influence falls modestly
- local organization or planning suffers for a bounded period

**Limits**

A cooldown and diminishing effect prevent repeated farming. At high Influence, the Generalissimo can block the rotation and create an officer confrontation.

### Establish Civilian Military Oversight

**Meaning**

A cabinet, parliamentary, party, royal, or state commission reviews appointments, budgets, and operations according to the host's government form.

**Costs**

- political power
- civilian factory burden
- temporary military production or planning penalty

**Effects**

- institutional reach falls over time
- removal chances improve
- passive Influence growth slows
- military efficiency falls while the review remains active

**DLC behavior**

The no-DLC route uses ordinary government institutions. A relevant intelligence or political DLC can add extra investigation outcomes without changing the core action.

### Remove Loyal Appointees

**Meaning**

The government retires, transfers, or prosecutes officers personally tied to him.

**Costs**

- command power
- army experience
- stability

**Effects**

- officer loyalty falls strongly
- Influence falls if the government is still credible
- the junta receives fewer commanders and divisions if revolt occurs
- army experience gain or command efficiency falls temporarily

**High-risk state**

At very high Influence, a broad purge can provoke a preemptive response. The risk must be shown before the player confirms the action.

### Create a Loyal Reserve Command

**Meaning**

The government builds a separate reserve force whose officers owe promotion and supply to civilian authority.

**Costs**

- infantry equipment
- support equipment
- manpower
- army experience

**Effects**

- creates or designates government-loyal reserve formations
- improves government force share in a revolt
- improves arrest and capture chances
- reduces active frontline efficiency while reserves are held back

**Unit rule**

The reserve uses valid host equipment and templates. It does not create a custom unit family.

### Disperse the Guard Formations

**Meaning**

Elite units associated with the Generalissimo are split across commands and moved away from the capital.

**Costs**

- command power
- fuel or trains
- temporary organization and planning penalties

**Effects**

- loyal-formation support falls
- revolt territory becomes less concentrated
- the government's capital-defense chance improves
- the Generalissimo's personal command bonus applies to fewer protected formations for a period

### Move the Arsenals

**Meaning**

Weapons and transport are moved from commands likely to support him.

**Costs**

- trains
- motorized equipment
- fuel
- civilian factory burden

**Effects**

- military-industry reach and rebel stockpile share fall
- supply strain rises temporarily
- selected loyal government states gain stockpile protection

**Map requirement**

The action uses dynamically selected arsenal and reserve states. The tooltip names them.

### Separate Military Intelligence

**Meaning**

The government moves intelligence files and communications outside the Generalissimo's staff.

**Costs**

- political power
- command power
- temporary intelligence penalty

**Effects**

- internal-security reach falls
- arrest, capture, and assassination chances improve
- foreign intelligence exposure can rise while systems are reorganized

**DLC behavior**

With a relevant intelligence DLC, the action can use agency strength and operatives. Without it, the action remains fully functional through the general staff and police apparatus.

## Active missions

### Hold the Command Centers

**Purpose**

The government gives the Generalissimo responsibility for defending the capital and a small set of dynamically selected command states.

**Duration target**

120 to 180 days depending on front distance and threat.

**Objectives**

- retain control of the capital
- retain control of one or two selected high-value command states
- maintain a minimum number of supplied divisions in the named area
- keep National Field Command or Supreme Command active

**Success**

- strong temporary military reward
- Influence and public prestige rise
- future command demands gain weight

**Failure**

- public prestige and Influence fall
- stability or war support falls
- the host suffers command disruption

The mission must not auto-complete from a condition the player already satisfies at launch. It should select states that are threatened, strategically exposed, or connected to the current front.

### Win the Campaign

**Purpose**

The government gives him a public deadline to reverse a war.

**Duration target**

180 to 270 days depending on enemy strength and distance.

**Objectives**

At least one of these must be selected at mission creation:

- capitulate a named enemy
- recapture a named capital or strategic region
- remove a defined war-danger state
- achieve a meaningful war-score or surrender-progress reversal supported by available script

**Success**

- large Influence gain
- strong temporary military confidence package
- one demand can be accepted at reduced immediate cost

**Failure**

- Influence and public prestige fall
- the country suffers military confidence and planning penalties
- the Generalissimo can blame restricted authority when his command state was below Supreme Command

### Secure the Civilian Chain of Command

**Purpose**

The government proves that critical institutions will still obey civilian orders.

**Duration target**

150 to 210 days.

**Objectives**

- hold the capital
- place supplied loyal divisions in the capital region and one arsenal region
- complete at least one counterweight decision
- avoid granting a new major demand during the mission

**Success**

- strong counterweight increase
- Influence falls
- safe dismissal and arrest chances improve
- government force share rises if revolt begins later

**Failure**

- officer-network strength rises
- Influence rises
- one regional command can openly declare for him

### Build the Loyal Reserve

**Purpose**

The government creates a usable force outside his personal network.

**Duration target**

180 to 240 days.

**Objectives**

- provide the required equipment and manpower
- keep selected training states under government control
- maintain a temporary factory or training commitment

**Success**

- loyal reserve formations become available
- removal chances improve
- government civil-war share increases

**Failure**

- part of the committed equipment is lost
- military confidence falls
- the Generalissimo gains evidence of government plotting

## Removal framework

Permanent removal is a strategic family, not one generic percentage button.

The player can prepare removal by:

- lowering command authority
- rotating loyal officers
- creating a loyal reserve
- moving arsenals
- separating military intelligence
- securing the capital and command states
- reducing public prestige
- waiting for a military failure
- using an existing intelligence network when available

The category must show:

- the method
- broad public consequence
- exact or bounded success chance where the value can be calculated reliably
- the strongest positive and negative factors
- whether failure causes immediate revolt
- the expected aftermath of success

The implementation should prefer an exact displayed chance when all factors are internal and stable. A qualitative band is acceptable only when engine timing or hidden external state makes an exact number misleading.

## Removal methods

### Negotiate Retirement

**Role**

The safest path while Influence is low.

**Availability**

- Influence below the retirement threshold
- no active final ultimatum
- no prior failed retirement negotiation
- Generalissimo lacks entrenched state-wide control

**Costs**

- political authority
- military pension or civilian-factory burden
- loss of his commander services

**Outcome**

Success is normally deterministic when requirements are met. The character retires permanently, the crisis closes, and the country receives a limited officer-reorganization aftermath.

At the upper edge of eligibility, he can demand guarantees for loyal officers. Accepting those terms avoids revolt but leaves a longer military oversight penalty.

### Dismiss from Command

**Role**

A formal government order that tests whether the army still obeys.

**Availability**

- no active final ultimatum except as the final removal choice
- the government retains a minimum counterweight position

**Success factors**

- low Influence
- Advisory Reserve or Theater Command
- strong civilian chain of command
- loyal reserve
- weak officer network
- recent public failure

**Failure outcome before Evolution III**

The Generalissimo refuses, Influence rises, safe dismissal locks, and a stronger confrontation follows. Failure does not automatically cause revolt before the final ultimatum.

**Failure outcome during the final ultimatum**

Immediate revolt.

### Arrest at Headquarters

**Role**

A direct coercive operation against his command staff.

**Availability**

- Evolution I active
- no prior coercive-removal attempt
- government controls the capital or selected headquarters state

**Costs**

- command power
- political authority
- loyal units committed through a mission or requirement

**Success factors**

- loyal reserve
- separated military intelligence
- secured headquarters
- low officer loyalty
- low internal-security reach
- lower command authority

**Success aftermath**

The Generalissimo is imprisoned or permanently removed from public life. The crisis ends. The army suffers a major but temporary command purge.

**Failure aftermath**

Immediate revolt with a bonus to junta coordination because the operation proves that compromise is over.

### Capture During Inspection or Transit

**Role**

A military operation that isolates him away from the center of his network.

**Availability**

- he holds an active command
- a valid inspection, front, or transit state exists
- government retains control of the route or local loyal units

**Costs**

- command power
- fuel or trains
- loyal unit commitment

**Success factors**

- dispersed guard formations
- secure transit route
- low regional-command support in the target state
- active intelligence preparation

**Success aftermath**

He is captured and removed permanently. The country suffers operational confusion because the active commander disappears during a campaign.

**Failure aftermath**

Immediate revolt. The junta receives a stronger initial field army in or near the attempted capture region.

### Assassination

**Role**

The most direct lethal option and the method with the strongest political aftermath.

**Availability**

- no prior coercive-removal attempt
- an event-owned intelligence or security preparation exists

**Costs**

- political authority
- intelligence exposure or stability
- optional equipment or operative commitment through the owner system

**Success factors**

- separated military intelligence
- low personal-security reach
- active Event 039 or intelligence support where valid
- reduced loyal guard support
- a controlled venue or travel route

**Success aftermath**

The Generalissimo dies, the crisis ends, and the government faces an officer purge, public uncertainty, and military morale loss. His loyal network cannot continue the Event 067 coup without him.

**Failure aftermath**

Immediate revolt with a large martyrdom and coordination bonus.

### Final removal attempt

At Evolution III, the government receives one final removal choice. It uses the best still-valid prepared method or a combined arrest operation.

- Success ends the crisis.
- Failure starts the revolt immediately.
- The player sees the chance and the strongest factors before choosing.
- The method cannot be repeated after reloading through an unguarded event chain.

## Removal chance model

The exact formula belongs in script constants and owner helpers. The design target is:

```text
method base chance
+ civilian chain of command
+ loyal reserve strength
+ secured headquarters and capital
+ dispersed loyal formations
+ separated intelligence
+ recent Generalissimo failure
- Generalissimo Influence
- officer loyalty
- internal-security reach
- military-industry reach
- Supreme Command authority
- active wartime emergency
- accepted protection for loyal officers
```

Target result bands:

| Crisis state | Prepared government | Unprepared government |
| --- | --- | --- |
| Influence below 25 | Usually safe | Favorable but not certain for coercive methods |
| Influence 25 to 44 | Favorable with preparation | Contested |
| Influence 45 to 64 | Contested | Poor |
| Influence 65 to 84 | Risky | Very poor |
| Influence 85 to 100 | Possible only after serious preparation | Near-desperate |

The method base values should differ. Negotiated retirement is strongest at low Influence. Arrest is more reliable than assassination when the government controls headquarters. Capture is strongest when transit and guard conditions are favorable. Assassination can gain more from intelligence support but has the harshest success aftermath.

Every weighted or random result must be audited with the named probability scenarios.

## Immediate revolt contract

The following failures cause revolt in the same effect chain:

- failed arrest
- failed capture
- failed assassination
- failed final removal attempt

There is no warning mission, grace period, or second confirmation after failure. The failure event may explain what happened, then the civil-war setup begins immediately.

A failed ordinary dismissal before Evolution III does not automatically cause revolt. It causes a sharper crisis and removes the safe dismissal route.

## Successful removal cleanup

Every successful removal must:

- disable or retire the canonical character
- clear the host event target or persistent character ownership safely
- clear active demands and missions
- clear Generalissimo Influence and hidden network values after aftermath values are copied
- remove temporary command authority bonuses
- remove Event 067 command decisions
- end recurring event-owned pulses
- record the resolution in Event Details and event history
- apply the correct Chaos reversal once
- block the normal Event 067 world-end readiness
- preserve Event 065 trait-pool integration
- preserve unrelated host commanders, focuses, laws, and equipment

The method-specific aftermath can remain for a bounded period.

## Government aftermath by method

| Method | Military aftermath | Political aftermath |
| --- | --- | --- |
| Retirement | Mild officer reorganization | Small authority cost and loss of popular commander |
| Dismissal | Moderate planning and command disruption | Public dispute and divided officer opinion |
| Arrest | Strong officer purge and readiness loss | Emergency legal or security burden |
| Capture | Strong operational confusion during active command | Public uncertainty and investigation |
| Assassination | Severe morale and command disruption | Stability loss, scandal risk, and long investigation |
| Defeat in civil war | Deep military reconstruction | Reconstruction, reconciliation, trials, or purge choices |

The aftermath should be meaningful enough that removal is not a free conversion of a powerful asset into permanent safety.

## AI removal rules

AI must not choose a coercive method because it is available.

AI should consider:

- displayed success chance
- its relative strength in a possible civil war
- current external war
- capital security
- loyal reserve strength
- army equipment
- faction support
- regime type
- Generalissimo command benefit
- proximity to the final ultimatum

A stable civilian government should prepare before acting. A personalist ruler may attempt assassination earlier. A losing wartime government may tolerate high Influence because losing the commander would be worse. A military regime may accept the final transfer of power.

An AI should rarely choose a method below its configured minimum success threshold unless refusal or imminent overthrow makes the alternative worse.

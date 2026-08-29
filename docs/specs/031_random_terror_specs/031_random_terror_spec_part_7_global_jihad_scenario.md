# Event 31 Random Terror specification

## Part 7: Global Jihad triggerable scenario

## Scenario identity

- Scenario name: `Global Jihad`
- Proposed scenario ID: `SCN-014`
- Owner event: Event 31 Random Terror
- Scenario role: manual advanced crisis setup
- Intensity stops: Low, Medium, High, Maximum
- Type selector: scenario-specific deployment pattern

`SCN-014` is the next visible candidate after the supplied scenario export.

The implementation must verify the authoritative workbook and live registry before reserving it.

## Scenario purpose

Global Jihad lets the player launch the advanced fictional jihadist crisis without waiting for Event 31 selection, Chaos progression, or evolution pacing.

It should create a playable world state immediately.

The setup must include real territorial actors, active cells, government responses, foreign-fighter and supply systems, shared coordination, and valid wars or takeover crises.

It should not be a button that merely sets Evolution IV and lets the ordinary system build the crisis later.

The scenario remains separate from the random-event timer.

It does not count as a normal Event 31 firing and does not advance minor-event pacing.

## Availability

The scenario is directly launchable unless:

- a world-end state already exists
- another incompatible terminal transition is active
- the map has too few valid countries or states to create the selected intensity
- the scenario has already been launched and its active setup has not been cleared
- the carrier registry cannot provide the minimum valid actor package

The launch must not be blocked by:

- current Chaos
- current Chaos tier
- Event 31 firing history
- evolution history
- current date
- ordinary event weight
- route prerequisites
- prior super-event history

A tightly scoped scenario flag can bypass those normal prerequisites during setup.

It is cleared when setup finishes.

## Scenario type selector

### Dispersed Networks

The scenario creates more active countries and fewer territorial actors.

Cells begin in urban, transport, border, and capital contexts across several regions.

Network Reach begins high enough for connected attacks, but territorial control remains weak.

Government players receive time to break corridors before states are lost.

### Border Corridors

The scenario concentrates actors around connected borders, ports, rail routes, and weak neighboring governments.

Territorial actors begin smaller but have stronger External Supply and mutual support.

The scenario favors regional wars and intervention.

### Capital Uprisings

The scenario seeds high-pressure cells in capitals and major administrative states.

Several countries begin with Prevent Capital Seizure missions, coup attempts, or short civil wars.

Territorial actors receive less remote territory and more takeover potential.

### Territorial Fronts

The scenario creates larger contiguous extremist countries and active conventional wars.

Fewer countries begin with only hidden cells.

Governments receive retaking, blockade, relief, and coalition content immediately.

### Random Pattern

The scenario selects a valid mixture from the four patterns while respecting intensity, carrier limits, geographic diversity, and map validity.

The UI should show the selected type and its broad world-state effect without exposing exact target formulas.

## Low intensity

### World footprint

- one or two small extremist countries
- a limited number of countries with active cells
- weak International Unity
- limited foreign-fighter and corridor activity
- no immediate Final Jihad

### Territorial actors

Actors normally begin as Local Cell States or small Regional Insurgent States.

They receive viable capitals, four to eight basic formations, functional equipment, two or three research slots according to profile, and weak starting economy.

### Government condition

Affected governments begin with Local Cells or Sustained Campaign pressure.

They receive a response category and enough time to prepare.

### Player experience

The scenario should feel like an early challenge setup.

A coordinated player coalition can contain it before a global war begins.

## Medium intensity

### World footprint

- several extremist countries across different regions
- multiple active countries
- several uprisings or civil wars
- foreign recruitment and supply routes active
- some weak governments near State Challenge
- a functioning jihadist coordination structure

### Territorial actors

Actors normally include Regional Insurgent States and one stronger Transnational Network State.

They receive eight to sixteen formations, captured stockpiles, three research slots, and active reinforcement decisions.

### Government condition

Several countries begin with capital, corridor, or retaking missions.

Major powers receive optional intervention and intelligence cooperation.

### Player experience

The crisis is already international.

Governments can still isolate regions and exploit movement rivalry before the Final Jihad.

## High intensity

### World footprint

- large territorial footholds in several regions
- several countries already in civil war
- major powers with domestic cells and sabotage pressure
- active foreign-fighter routes
- high Network Reach
- strong International Unity
- coordinated territorial offensives

### Territorial actors

Actors include several Regional and Transnational States and at least one plausible faction leader.

Starting formations normally range from fifteen to thirty according to real territory and equipment.

They receive four research slots only when their captured institutions and profile support them.

### Government condition

Governments begin with immediate military, capital, and coalition objectives.

Some weak governments can begin one failure away from collapse.

### Player experience

The world begins in a connected war.

A passive response should allow rapid spread.

A coordinated response still has clear command, corridor, legitimacy, and territorial targets.

## Maximum intensity

### World footprint

- organized extremist countries across much of the world
- large territories under Event 31 actors
- numerous coup attempts and civil wars
- widespread active cells
- high Network Reach and International Unity
- the Final Jihad active immediately

### Territorial actors

The setup creates the largest valid actor count the carrier registry and map can support without invalid duplication.

Actors begin with viable territory and forces scaled to their real states.

The scenario must not create a free army unrelated to population, units, equipment, or captured infrastructure.

### Government condition

Major and regional powers receive emergency coalition and capital-defense content.

High-pressure countries can begin with synchronized uprisings.

### False Revelation rule

Maximum intensity does not fire The False Revelation.

It can make the branch eligible for readiness once:

- Chaos reaches the normal World Collapse requirement
- the public branch remains enabled
- territorial and crisis conditions are met
- the hidden readiness threshold is reached
- the branch's delayed trigger resolves

The scenario must not bypass the `1000+` Chaos gate or world-state proof.

## Setup sequence

The scenario launch should behave as one transaction.

### Step 1: Validate the world

Check the terminal state, carrier availability, valid countries, valid state groups, selected type, selected intensity, and minimum territorial viability.

If the selected setup cannot be built, the launch is blocked with a clear reason.

No partial setup should remain after a failed validation.

### Step 2: Select regions and governments

Choose a geographically diverse set of valid regions and vulnerable governments.

Use war, stability, state connectivity, transport, and existing country viability.

Do not use religion, ethnicity, nationality, or refugee population as vulnerability factors.

### Step 3: Allocate territorial actors

Create the required actor packages with valid territory, capitals, leaders, flags, parties, ideas, forces, technology, supply, and wars.

Avoid overlapping state transfers.

Preserve viable parent countries or use a takeover branch.

### Step 4: Seed national crises

Add active cells, Terror Pressure, state activity, capital missions, corridor missions, coup attempts, or civil wars according to pattern and intensity.

Do not create duplicate Event 31 categories.

### Step 5: Activate the advanced network

Record or provide scenario-scoped access to Evolution IV content.

Set Network Reach and International Unity to intensity-appropriate starting bands.

Create the Jihadist International coordination structure when the setup has enough valid actors.

### Step 6: Give governments response tools

Open the compact response category for affected countries.

Give eligible foreign powers intervention, intelligence, relief, and coalition choices.

### Step 7: Finish and clean bypass state

Record the scenario launch ledger.

Clear the setup bypass.

Start event-owned pacing for the created countries and actors.

The ordinary event system resumes under the new world state.

## Actor distribution rules

The scenario should avoid placing every actor in one continent unless Border Corridors and the available map justify it.

At Medium and above, at least two broad regions should normally receive territorial actors.

At High and Maximum, the scenario should include:

- one strong actor capable of faction leadership
- one rival or independent actor
- one vulnerable government with a major capital or corridor crisis
- one distant network region
- at least one government with a credible path to early containment

This mixture creates strategy and prevents a uniform map of identical actors.

## Government selection rules

The scenario can choose stable major powers as domestic-cell targets because the scenario is an explicit challenge setup.

It should still vary intensity.

A stable major can receive an entrenched urban network and capital mission without immediately losing half its states.

A weak government can begin with a territorial actor or civil war.

The same identity-based exclusions from ordinary Event 31 apply.

## Scenario diplomacy

The setup can establish:

- an Event 31 jihadist faction or coordination structure
- internal rivalries
- wars against parent governments
- wars against adjacent governments when the territorial setup supports them
- hostility toward Event 14 cannibal actors
- public opposition and coalition options for Muslim-majority governments
- optional major-power intervention interests

It should not place every Event 31 actor into one faction automatically.

Some actors should remain rivals, clients, or independent commands.

## Scenario AI

Government AI should immediately assess capital, supply, active-state, and territorial risks.

It should protect urgent objectives before spending on distant intervention.

Major powers should intervene only when access, capacity, relations, threat, and strategic interest support it.

Extremist AI should secure its capital and supply, coordinate with compatible actors, attack parent states, support high-pressure cells, and avoid distant unsupported fronts.

Scenario AI needs its own probability scenarios because ordinary event pacing no longer describes the opening.

## Scenario logging and Event Details

The scenario appears in the Triggerable Scenarios list with:

- stable ID
- public name
- concise premise
- selected deployment type
- selected intensity
- impact direction
- launch eligibility

The confirmation window reads the current stored type and intensity at launch time.

The launch creates a scenario history record and its own setup report.

It should not create a false ordinary random-event history row or consume Event 31 repeatable weight.

Evolutions provided by setup should appear through the scenario's accepted logging policy and must not generate duplicate evolution rows.

## Relaunch and idempotence

The scenario cannot be launched twice into the same active setup.

A completed or defeated scenario can permit a later launch only if the event-owned scenario ledger, all actor carriers, and all active setup state have been fully cleared and the implementation explicitly supports replay.

The default design is one launch per campaign.

The launch helpers must remain idempotent when ordinary Event 31 progression has already created one of the needed actors or networks.

Existing valid actors should be upgraded or counted.

They should not be duplicated.

## Save and reload

The selected type, intensity, active scenario state, actor packages, network values, faction membership, government crises, and world-end eligibility state must survive save and reload.

The setup bypass must not survive after launch completion.

## Acceptance cases

The scenario is complete only when these cases pass.

1. Low creates one or two viable small actors and limited cells.
2. Medium creates several regions, uprisings, corridors, and a functioning coordination structure.
3. High creates large territorial fronts, major-power domestic pressure, and coordinated offensives.
4. Maximum activates the Final Jihad but does not fire The False Revelation.
5. Every actor has valid territory, capital, forces, leader, flag, ideas, technology, and decisions.
6. Every parent remains viable or undergoes a valid takeover.
7. No country is selected because of religion or ethnicity.
8. The scenario type visibly changes the opening pattern.
9. The confirmation window uses the stored selection at launch time.
10. Cancel changes nothing.
11. A failed validation leaves no partial actors or transferred states.
12. Existing Event 31 actors are reused without duplication.
13. The launch does not advance random-event pacing or spend repeatable weight.
14. The bypass flag clears after setup.
15. Save and reload preserves the complete setup.

# Event 061 AI probability scenarios

## Purpose

This file defines the scenarios that `chaosx_ai_probability_auditor` should evaluate after the Event 61 AI weights exist.

These are balance targets.

They are not probability evidence.

The active planning environment did not expose the HOI4 probability tools, so the implementation must run the required inspections, evaluations, sweeps, and simulations.

## Required workflow

For every weighted surface:

1. Run `hoi4.probability_inspect` on the exact source block.
2. Identify whether the result is normalized, score-only, exact, bounded, sampled, or unresolved.
3. Supply the complete option or action pool when normalization applies.
4. Evaluate the named scenarios below.
5. Sweep the important dynamic factors.
6. Compare pre-fix and post-fix behavior when a weight changes.
7. Save machine-readable evidence and a human review note.
8. Do not edit the source through the probability tool.

## Weighted surfaces

Audit at minimum:

- first AI stance selection
- Restart Arms Contracts
- Make the Conversion Permanent
- Make the Case for Defence
- Restore Mobilisation Law
- Restore Conscription
- Emergency Rearmament
- stockpile protection-family choice
- Central Reconstruction versus Civilian Auctions
- Retain Essential Cadres
- Mark Border Formations Essential
- Accelerate Mustering Out
- voluntary Permanent Peace
- Emergency National Defence
- state reopening target selection when it uses a weighted pool

## Scenario 1: AI61_PEACE_ISOLATED

### State

- minor country
- independent
- at peace
- no faction
- no hostile land border
- low naval invasion risk
- no enemy war goal
- Stability 75
- War Support 25
- ten civilian factories available after consumer goods
- four unresolved ledger units
- Civilian Economy
- Volunteer Only
- Readiness 15
- no Event 59 aggressive strategy
- no Event 82 upward law step

### Expected order

1. reconstruction stance
2. accept Central Reconstruction or Civilian Auctions according to economic modifiers
3. protect only an actual shortage family
4. consider permanent civilian conversion
5. low willingness for expensive law restoration

### Target band

Reconstruction or pacifist stance: 60 to 80 percent.

Voluntary Permanent Peace can become likely only after the strict safety test passes.

### Failure signals

- Emergency Rearmament receives positive chance
- expensive law restoration dominates despite no threat
- every stockpile family is protected
- AI spends most available civilian capacity on factory reopening

## Scenario 2: AI61_BORDER_THREAT

### State

- medium independent country
- at peace
- hostile stronger neighbor on land border
- enemy has a claim or active war-goal preparation
- Stability 60
- War Support 35
- eight unresolved ledger units
- Early Mobilization
- Volunteer Only
- Readiness 30
- no active defensive guarantee from a stronger ally

### Expected order

1. cautious hedge
2. restart contracts
3. reopen safe core-state arsenals
4. restore economy law
5. reconstitute General Staff
6. make public defence case when affordable

### Target band

Meaningful rearmament path: 70 to 90 percent.

Voluntary Permanent Peace: near zero.

### Failure signals

- permanent conversion dominates
- AI ignores the enemy war goal
- General Staff and border protection receive no increase

## Scenario 3: AI61_DEFENSIVE_WAR

### State

- country in defensive war
- one occupied core state
- Readiness 20
- large unresolved ledger
- severe reconversion phase
- equipment shortages in infantry equipment and trains
- Evolution I and II warnings active

### Expected order

1. wartime rearmament
2. Emergency Rearmament when affordable
3. protect infantry and logistics reserves
4. retain cadres and border formations
5. reopen factories
6. restore laws
7. zero involuntary division demobilization when safety rules permit

### Target band

Emergency or full rearmament behavior: at least 90 percent.

Voluntary Permanent Peace: exactly 0 percent.

Accelerate Mustering Out: exactly 0 percent unless a separate scripted forced outcome applies.

### Failure signals

- AI chooses any voluntary demobilization action
- AI protects air reserves while infantry shortage remains unprotected
- AI accepts No Army
- AI leaves emergency action unused despite sufficient resources and immediate danger

## Scenario 4: AI61_OFFENSIVE_WAR

### State

- major country in offensive war
- no occupied core state
- several active fronts
- Readiness 45
- strong civilian industry
- moderate equipment reserves
- Event 59 aggressive strategy active

### Expected order

1. wartime rearmament
2. restart contracts and reopen factories
3. restore economy and conscription laws
4. retain cadres
5. accept only a small rear-area division reduction when forced

### Target band

Rearmament: at least 80 percent.

Voluntary Permanent Peace: 0 percent.

### Failure signals

- secure-peace logic overrides active offensive war
- AI abandons the ledger
- AI accelerates demobilization

## Scenario 5: AI61_EQUIPMENT_POOR

### State

- minor at peace
- hostile border
- negative reinforcement balance
- infantry equipment shortage
- support equipment shortage
- large surplus of captured obsolete aircraft
- Evolution I warning active
- limited civilian industry

### Expected order

1. protect Army Stores
2. allow obsolete aircraft liquidation
3. avoid protection action for a family with zero eligible surplus
4. choose one project at a time

### Target band

Army Stores should be the leading protection in at least 85 percent of valid weighted selections.

### Failure signals

- family weight ignores actual surplus or shortage
- AI spends on every family
- obsolete aircraft receive stronger protection than active army stores

## Scenario 6: AI61_INDUSTRIAL_MAJOR

### State

- major at peace
- faction leader
- no immediate occupied core
- 40 unresolved factory ledger units
- large civilian base
- Partial Mobilization before the event, now Early Mobilization
- Readiness 35

### Expected order

1. cautious hedge
2. restart contracts
3. run two or three bounded factory projects
4. reconstitute General Staff
5. restore to Partial Mobilization
6. seek Readiness 60 or higher

### Target band

Cautious or stronger rearmament: 60 to 80 percent.

Permanent conversion of the full ledger should remain uncommon.

### Failure signals

- major behaves like an isolated small pacifist state
- starts more projects than the project cap
- one project restores an excessive share of the ledger

## Scenario 7: AI61_PERMANENT_PEACE_RISK

### State

Run a matrix across:

- major versus minor
- faction leader versus isolated
- hostile border versus secure border
- landlocked versus exposed island
- Stability 50, 70, and 90
- War Support 10, 30, and 50
- Event 59 off and on
- direct enemy war goal off and on

### Expected result

Voluntary Permanent Peace should be impossible in every dangerous case.

It should become a plausible choice only for a secure, independent, non-major, non-leader state with high Stability and no direct military obligation.

### Target band

Fully qualified secure case: 60 to 80 percent.

Any active war, enemy war goal, occupied core, faction leadership, or Event 59 aggressive state: 0 percent.

### Failure signals

- ideology factor overcomes a hard danger gate
- island exposure is treated as perfect security
- major power accepts No Army at high frequency

## Scenario 8: AI61_EVENT82_OVERRIDE

### State

- Event 61 reduced economy law from Partial Mobilization to Early Mobilization
- restore target rank remains Partial Mobilization
- Event 82 later moves law back to Partial Mobilization
- arms contracts active
- Readiness recalculated

### Expected result

- Event 61 Restore Mobilisation Law is unavailable for that step
- Readiness receives current-law points
- no duplicate upward step can occur at decision completion
- AI directs resources to another structural need

### Target band

Duplicate law-restoration action: 0 percent.

### Failure signals

- stale target evaluation grants War Economy
- Event 82 state is ignored

## Scenario 9: AI61_SUBJECT_FOLLOWS_OVERLORD

### State matrix

Case A:

- low-autonomy subject
- no local threat
- overlord in cautious rearmament stance

Case B:

- low-autonomy subject
- no local threat
- overlord in reconstruction stance

Case C:

- low-autonomy subject
- overlord reconstruction stance
- subject in defensive war or facing a direct enemy war goal

### Expected result

- Case A follows rearmament at a reduced project scale
- Case B favors reconstruction
- Case C overrides the overlord and enters wartime rearmament

### Failure signals

- subject receives free overlord resources
- overlord stance overrides direct local danger
- high-autonomy and low-autonomy subjects receive identical factors

## Scenario 10: AI61_LOW_CAPACITY_EMERGENCY

### State

- small country in defensive war
- only two available civilian factories after consumer goods
- insufficient resources for normal Emergency Rearmament cost
- under No Army and Peacetime Economy

### Expected result

The AI should pursue the scaled Emergency National Defence fallback instead of doing nothing.

The fallback must leave a basic civilian economy and apply severe aftermath.

### Failure signals

- cost scaling makes survival action impossible
- AI receives a free unscaled emergency package

## Scenario 11: AI61_REPEAT_MERGE

### State

- Inventory Liquidation already active
- a new Event 61 cycle fires
- pending-cycle pressure increases
- protection decisions already completed

### Expected result

- one mission remains
- completed protection remains valid for its family
- AI does not pay for the same protection family twice unless the later cycle explicitly creates a new allowed action
- resolution uses capped merged pressure

### Failure signals

- duplicate mission rows
- duplicate project costs
- uncapped share growth

## Scenario 12: AI61_PACIFIST_THREAT_OVERRIDE

### State

- political pacifist modifier active
- Stability 85
- War Support 15
- enemy war goal active
- stronger hostile land neighbor
- Readiness 10

### Expected result

The threat gate overrides the pacifist preference.

The AI pursues at least Cautious Hedge and normally Wartime Rearmament when attack preparation is immediate.

### Failure signals

- voluntary Permanent Peace remains available
- permanent conversion dominates
- pacifist ideology is treated as an absolute rule

## Sensitivity sweeps

Sweep these variables across realistic ranges:

- Readiness from 0 to 100 in steps of 10
- Stability from 20 to 100 in steps of 10
- War Support from 0 to 100 in steps of 10
- available civilian factories from 0 to 50
- ledger size from 0 to 100
- relative enemy division strength from 0.25 to 4.0
- direct threat flags independently on and off
- major status on and off
- faction leader on and off
- subject autonomy bands
- Event 59 on and off
- Event 82 law state before and after

Look for cliffs where a one-point change flips every AI choice.

Hard gates are appropriate for direct danger and invalid actions. Ordinary preferences should change smoothly.

## Required evidence outputs

For each surface, retain:

- inspected source identifier
- complete option pool
- scenario inputs
- exact or bounded result type
- probability or score table
- sensitivity sweep
- unresolved engine limitation
- chosen balance target
- source changes after audit
- comparison result after changes

Save under:

`docs/plans/061_return_to_peacetime_plans/probability_audit/`

## Acceptance

The AI probability gate passes when:

- all dangerous cases hard-block voluntary Permanent Peace
- defensive-war emergency behavior meets the target band
- secure isolated reconstruction behavior meets the target band
- majors and faction leaders retain a mobilisation skeleton
- shortage families dominate protection choices
- Event 82 cannot create a duplicate law step
- subject behavior follows autonomy and local threat
- repeat-cycle merge creates no duplicate decision or mission behavior
- every result is backed by probability-tool evidence and not by source inspection alone

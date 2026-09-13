# Event 061: Return to Peacetime

## Part 2: Return to Rearmament

## Mechanic purpose

Return to Rearmament gives each affected country a difficult route back to military preparedness.

The system should force a real choice about civilian capacity, public support, military institutions, and time.

It should not work as a row of political power purchases that instantly undo the event.

A country can rebuild quickly only by diverting substantial civilian capacity and accepting temporary disruption. A country that accepts the transition can keep the civilian factories and let the military penalties expire.

## Presentation layer

Use one ordinary decision category with:

- one decision category icon
- one static category picture
- concise category text
- one public numeric value
- qualitative status for the main readiness pillars
- phased decision visibility
- no separate mechanic window

The system does not need a scripted GUI. The decisions already carry the actions, targets, costs, and deadlines.

The category should normally show three to five primary decisions and no more than one active mission.

A confirmation popup is required for irreversible actions and emergency policies with severe costs.

## Public value: Rearmament Readiness

### Range

Rearmament Readiness ranges from `0` to `100`.

It is the only persistent Event 61 number the player must actively monitor.

Working variable:

`return_to_peacetime_readiness`

### Meaning

Readiness summarizes whether the country has rebuilt enough military industry, law, institutions, public support, and reserve capacity to resist later demobilization.

It is a derived value.

The player does not purchase raw Readiness directly.

Every point comes from an observable structural condition or completed action.

### Readiness bands

| Range | Working state label | Meaning |
| ---: | --- | --- |
| 0 to 19 | Demobilized | Civilian transition dominates and no credible rearmament program exists |
| 20 to 39 | Watching the Borders | Some defensive preparation exists, but the state remains vulnerable to deeper demobilization |
| 40 to 59 | Rearmament Underway | Several military institutions are returning and evolved losses are reduced |
| 60 to 79 | Mobilisation Program | The country has a coherent recovery plan and can resist most forced demobilization |
| 80 to 100 | War Footing | The state has restored a strong military posture and can protect divisions and stockpiles |

These are working state labels. Final localisation should follow the tone rules in Part 6.

### Five hidden point pillars

The total is built from five pillars worth up to 20 points each.

The category may show each pillar as a qualitative state such as dormant, partial, established, or ready. It should not expose five additional raw meters.

#### Pillar 1: Industrial capacity

This pillar measures restored war-production capacity.

Suggested point model:

- 0 points when no arms contracts have restarted and unresolved converted capacity exists
- 5 points after arms contracts restart
- up to 15 additional points from the share of Event 61 converted capacity that has been reopened
- when the country had no convertible military factory at the latest baseline, the contract action can satisfy the unavailable restoration share so small countries are not permanently capped

The restored share should use Event 61 ledger capacity, not total current military factories. Annexation and unrelated construction must not increase this pillar.

#### Pillar 2: Economy law

Suggested point model:

| Current economy law | Points |
| --- | ---: |
| Peacetime Economy | 0 |
| Civilian Economy | 5 |
| Early Mobilization | 10 |
| Partial Mobilization | 15 |
| War Economy or Total Mobilization | 20 |

A country can reach full points through Event 82 or normal law changes. The result reflects actual posture.

#### Pillar 3: Conscription law

Suggested point model:

| Current conscription law | Points |
| --- | ---: |
| No Army | 0 |
| Disarmed Nation | 5 |
| Volunteer Only | 10 |
| Limited Conscription | 15 |
| Extensive Conscription or a higher obligation | 20 |

#### Pillar 4: Defence institutions

Suggested point model:

- 0 points with no Event 61 institutional response
- 10 points after arms contracts restart
- 20 points after the general staff or equivalent national defence planning institution is reconstituted

Restarting contracts can contribute to both industry and institutions because it proves two distinct conditions. The total remains capped by the five-pillar formula.

If the implementation finds this double role too generous in live balance, move the first institutional 10 points to a separate Defence Ministry action. Do not add another public value.

#### Pillar 5: Public and material preparation

This pillar combines public willingness and protected reserves.

Suggested hidden components:

- up to 15 points from War Support thresholds
- 5 points from at least one completed reserve-protection, cadre-retention, or defence-settlement action

Suggested War Support thresholds:

| War Support | Points |
| ---: | ---: |
| below 20% | 0 |
| 20% to 34% | 5 |
| 35% to 49% | 10 |
| 50% or higher | 15 |

The implementation can adjust the thresholds after probability and balance testing. The total pillar remains capped at 20.

### Structural proof

Readiness alone does not always prove that the country has acted.

A country has **meaningful rearmament** when:

- Readiness is at least 50
- at least one structural proof exists

Valid structural proof:

- one or more Event 61 factory ledger units have been reopened
- the economy law has been restored upward after an Event 61 reduction
- the conscription law has been restored upward after an Event 61 reduction

Restarting contracts without restoring a physical or legal structure is preparation, but it is not enough by itself for the normal exemption.

Evolution III uses a stricter last-chance requirement for countries that had not reached meaningful rearmament before its settlement begins.

### Recalculation

Readiness should recalculate:

- after the baseline transaction
- after every Event 61 decision or mission outcome
- after every Event 61 evolution outcome
- after a known cross-event law change such as Event 82
- during the bounded 30-day active-country pulse
- when a converted state changes owner or control through a supported hook
- when the category is opened or refreshed through an existing safe project pattern

The value should not drift through a permanent global daily tick.

## Category phases

The category changes its visible action set according to current state.

### Phase A: Immediate transition

Visible after baseline:

- summary of converted factory capacity
- summary of current Readiness band
- Restart Arms Contracts
- Make the Case for Defence when public support conditions permit
- Make the Conversion Permanent when unresolved factory capacity exists
- active evolution response when one has begun

The category should not show every later law and plant action before the country has restarted contracts.

### Phase B: Industrial revival

Visible after arms contracts restart:

- up to three targeted Reopen State Arms Plants decisions
- Reconstitute the General Staff
- Make the Case for Defence
- Restore Mobilisation Law when valid
- active evolution response

### Phase C: Mobilisation restoration

Visible after Readiness reaches the lower middle band or an institutional action completes:

- Restore Mobilisation Law
- Restore Conscription
- additional state reopening decisions
- emergency response when valid
- category exit when all remaining factory claims can be abandoned

### Phase D: Evolved response

During an evolution mission, replace weak or irrelevant ordinary actions with the most useful response decisions.

Do not increase the visible count beyond five primary actions.

### Phase E: Extreme-law recovery

While Peacetime Economy or No Army is active, prioritize:

- Re-establish a Defence Ministry
- Reopen the National Arsenal
- Restore the Service Registry
- Emergency National Defence when valid
- one active recovery mission

Ordinary restoration actions appear as later phases of this route. They should not compete with the first escape steps.

## Decision family

All names below are working labels.

Final decision names and descriptions should be written during implementation from the localisation direction in Part 6.

## Restart Arms Contracts

### Role

This is the normal first commitment to rearmament.

It represents reopening procurement offices, negotiating supply contracts, preserving technical drawings, and ordering tooling for military production.

### Availability

Available when:

- Return to Rearmament is active
- arms contracts have not restarted for the current unresolved transition
- the country is not already completing the same project
- the country has a valid ordinary government and enough civilian capacity to commit

### Duration

Base target: 90 days.

Dynamic range: 60 to 150 days.

Relevant factors:

- current civilian factory base
- unresolved converted factory count
- war status
- major status
- Industrial Reconversion Shock phase
- embargo or severe depression state
- existing defence institutions

### Cost

Use no more than two spendable cost types:

- political power
- temporary civilian factory commitment

Starting target:

- 50 to 100 political power
- 3 to 8 civilian factories committed for the project duration

The civilian commitment scales with country size but remains a meaningful share for a small country.

### Result

On completion:

- set the arms-contract structural flag
- add the contract contribution to Readiness
- unlock targeted factory reopening
- reduce part of the later reconversion output penalty after the first severe phase
- unlock institutional recovery
- change AI stance from passive reconstruction to at least cautious preparation

### Failure and cancellation

If the country loses the required civilian base, becomes invalid, or cancels the project:

- retain no permanent readiness gain
- refund no completed political cost
- release any ongoing factory commitment through the shared cost framework
- allow a later restart after a cooldown

A cancelled contract project should not permanently block the system.

## Reopen State Arms Plants

### Role

This is a targeted state decision that converts ledgered civilian capacity back into military factories.

### Target selection

The main category shows no more than three state targets at once.

Candidate states must:

- be owned and controlled by the acting country
- have at least one Event 61 ledger unit
- have at least one civilian factory level available for conversion
- pass the local stability and building checks used by the implementation

Candidate priority:

1. largest available ledger count
2. core state
3. undamaged industry
4. connected to the capital or a valid supply network
5. lower immediate occupation risk
6. seeded random tie break

The player can complete a target and receive another candidate on the next refresh.

### Batch size

A decision can restore one to five factory levels.

Suggested batch logic:

- small industry or ledger of one: restore one
- medium industry: restore two or three
- large major with a large state ledger: restore up to five

The exact number is shown before commitment.

### Duration

Base target: 120 days.

Dynamic range: 90 to 180 days.

A damaged state, embargo, depression, or weak infrastructure increases duration.

War, high Readiness, and established contracts can reduce duration within the floor.

### Cost

Use:

- political power
- temporary civilian factory commitment

The project should cost more civilian factory days than Restart Arms Contracts per restored building level.

Starting target:

- 25 to 50 political power
- 2 to 4 committed civilian factories per restored factory level, capped by the category cost framework

### Completion transaction

For each restored level:

- confirm the ledger is still positive
- confirm one civilian factory is still available
- remove one civilian factory
- add one military factory
- subtract one state ledger unit
- update country unresolved and restored totals

The project stops at the number of successful atomic conversions.

If fewer levels remain than the planned batch, it restores only the valid remainder and reports the result.

### Occupation or ownership change during project

If the state becomes invalid before completion:

- cancel the state transaction
- do not consume the ledger
- release remaining factory commitment
- retain a partial administrative cost only if the shared cost framework supports safe cancellation penalties
- refresh the candidate pool

## Reconstitute the General Staff

### Role

This decision restores planning institutions, reserve records, mobilization schedules, and cadre continuity.

It is a national project and a major proof against later division demobilization.

### Duration

Base target: 150 days.

Dynamic range: 90 to 210 days.

### Cost

Use:

- army experience
- political power
- optional temporary civilian factory commitment when the country is large

Starting target:

- 25 to 50 army experience
- 50 to 100 political power
- zero to four committed civilian factories

Command power should not be the default cost.

### Result

- complete the defence-institution pillar
- raise Readiness
- improve AI willingness to retain cadres and border formations
- reduce Evolution II division target
- unlock the strongest normal law restoration actions
- provide one structural action for the Evolution III last-chance test

This action is institutional proof but does not satisfy the normal factory or law structural-proof requirement by itself.

## Make the Case for Defence

### Role

This action reverses part of the public mood shift by campaigning for defence preparedness.

### Availability

Available when:

- War Support is below a tuned upper threshold
- Stability is above a safe floor
- the action is not on cooldown
- the country has a public reason to argue for defence, such as a hostile border, faction obligation, active war, enemy war goal, high global threat, or a rearmament program

A secure pacifist country may still use it at greater cost and lower AI weight.

### Duration

Base target: 60 days.

Dynamic range: 45 to 100 days.

### Cost and result

Use:

- political power
- Stability as a spendable political cost

The action transfers public confidence into military willingness at a deliberately inefficient rate.

Starting target:

- remove 5 to 10 Stability
- add 4 to 8 War Support
- spend 25 to 75 political power

The action must respect a Stability floor and a War Support ceiling.

### Cooldown

Base target: 180 days.

A repeat firing can refresh the need, but it does not clear the cooldown automatically.

This prevents cycling Event 61 into a Stability and War Support farm.

## Restore Mobilisation Law

### Role

This project restores one economy-law step toward the highest unresolved Event 61 restoration target.

### Availability

Available when:

- current economy law rank is below the recorded target rank
- arms contracts have restarted
- Readiness meets the threshold for the requested step
- the country is not already changing the same law through Event 61
- the current law is not blocked by a higher-priority extreme-law exit sequence

Suggested Readiness requirements:

| Requested result | Minimum Readiness |
| --- | ---: |
| Civilian Economy to Early Mobilization | 30 |
| Early Mobilization to Partial Mobilization | 45 |
| Partial Mobilization to War Economy | 60 |
| War Economy to Total Mobilization | 80 |

Event 61 normally restores only ranks that it previously removed. The final row matters only when repeated firings or another event created a valid target at Total Mobilization.

### Duration

Base target: 120 days.

Dynamic range: 75 to 180 days.

### Cost

Use:

- political power
- temporary civilian factory commitment

Higher ranks require more of each.

### Result

- move one valid economy law step upward
- recalculate Readiness
- reconcile the restoration target
- update the category phase

The decision must verify the current law again at completion so an external change cannot produce an extra step.

## Restore Conscription

### Role

This action restores one conscription step toward the highest unresolved Event 61 target.

### Availability

Available when:

- current conscription rank is below the recorded target
- the country has sufficient Readiness and War Support
- the general staff or a defence ministry exists for stronger steps
- the country is not blocked by the initial No Army exit route

Suggested Readiness requirements:

| Requested result | Minimum Readiness |
| --- | ---: |
| Disarmed Nation to Volunteer Only | 30 |
| Volunteer Only to Limited Conscription | 45 |
| Limited Conscription to Extensive Conscription | 65 |
| Extensive Conscription and above | 80 |

### Duration

Base target: 90 days.

Dynamic range: 60 to 150 days.

### Cost

Use:

- political power
- army experience for higher obligations
- temporary civilian factory commitment only when an administrative rebuild is needed

War Support is normally a requirement, not another hidden spendable cost.

### Result

- move one valid conscription step upward
- recalculate Readiness
- restore recruitable population through the ordinary law model
- update the category phase

The decision must not add a separate manpower grant.

## Emergency Rearmament

### Role

Emergency Rearmament is the fast, damaging route for a country that faces an immediate war or is already fighting.

It is not a normal optimization button.

### Availability

Require a concrete emergency:

- the country is in a defensive war
- an enemy has a war goal or active preparation against it
- hostile forces control one of its core states
- a nearby hostile country has overwhelming force under a verified threat test
- an event-owned crisis explicitly marks imminent attack

Offensive war can qualify only when the country is already fighting and would otherwise be crippled by the baseline. Its AI weight remains below the defensive case.

### Frequency

Once per Event 61 cycle.

A repeat firing creates a new cycle only after the previous emergency action has resolved.

### Duration

Base target: 30 days.

### Cost

Use no more than three spendable cost types:

- political power
- Stability
- temporary civilian factory commitment

Starting target:

- 75 to 150 political power
- 10 Stability
- 6 to 12 civilian factories committed for 90 days, scaled to country size

### Result

- restart arms contracts if needed
- restore a bounded share of the factory ledger, never more than the available civilian buildings
- restore one valid economy-law step
- restore one valid conscription step when the current law and public support allow it
- set a strong rearmament intent
- recalculate Readiness
- apply Improvised Rearmament

### Improvised Rearmament

This timed spirit represents rushed procurement, weak training, and poor production organization.

It should impose meaningful temporary penalties to:

- production efficiency retention or growth
- training time
- equipment reliability or attrition where valid
- civilian construction capacity

The emergency route creates survival capacity at a high medium-term cost.

### Achievement treatment

Emergency Rearmament disqualifies challenge achievements that test deliberate reconstruction or pacifist survival.

## Make the Conversion Permanent

### Role

This is the irreversible civilian route.

It accepts ledgered civilian factories as ordinary permanent civilian capacity and abandons the right to restore them through Event 61.

### Availability

Available when:

- the country owns and controls at least one state with a valid ledger
- no reopening project is active in the affected states
- the country is not under an active forced settlement that requires a different response

### Cost

The main cost is the irreversible loss of restoration rights.

A small political power cost is allowed if the implementation needs a confirmation action, but it should not be the design focus.

### Confirmation

The confirmation must show:

- number of ledger units being cleared
- number of states affected
- current Readiness effect
- that civilian factory levels remain
- that later rearmament must use ordinary construction or another event

### Result

- clear valid state ledger units under the current owner
- reduce unresolved converted count
- recalculate Readiness
- remove state reopening decisions that no longer have targets
- allow category cleanup when no other Event 61 surface remains

## Begin a National Rearmament Program

### Role

This is an optional goal-style mission used when the country makes a serious commitment.

It should not be visible before arms contracts restart.

### Duration

Base target: 180 days.

Dynamic range: 150 to 270 days.

### Auto-completion requirements

The mission completes when the country:

- reaches Readiness 60
- completes at least two structural actions
- maintains at least one reopened factory or a restored economy law
- is not under a cancelled emergency program

### Success

- mark the country as having a coherent mobilisation program
- grant no raw free factories or divisions
- improve the strongest Event 61 evolution protection band
- reduce the remaining reconversion penalty within its floor
- unlock the final normal restoration steps

### Failure

- retain completed factories and laws
- remove the program marker
- apply a cooldown before another program can begin
- apply a temporary administrative delay to later rearmament projects

Failure should matter, but it must not delete completed structural work.

## Extreme-law recovery sequence

When Peacetime Economy or No Army is active, ordinary rearmament begins through three staged national projects.

These projects are designed to avoid a resource soft-lock.

They do not require army experience, command power, or a recruitable manpower pool during their first steps.

## Re-establish a Defence Ministry

### Purpose

Restore a legal institution capable of planning national defence.

### Requirements

- stable ordinary government
- no active capitulation cleanup blocker
- enough civilian industry to maintain the project

### Duration

Base target: 180 days.

### Cost

- political power
- temporary civilian factory commitment

### Result

- create the first defence institution
- raise the institutional pillar
- unlock the National Arsenal and Service Registry projects
- permit the first normal law exit when its other requirements are met

## Reopen the National Arsenal

### Purpose

Restore a minimum arms-production base from Event 61 ledgered capacity or ordinary civilian capacity.

### Requirements

- Defence Ministry complete
- at least one valid factory ledger unit, or enough ordinary civilian industry to build a replacement through a costly fallback project

### Duration

Base target: 180 days.

### Cost

- political power
- substantial civilian factory commitment

### Result

- restore a minimum bounded batch of military factories
- restart arms contracts
- move the industrial pillar out of its zero state
- unlock the economy-law exit from Peacetime Economy

### Ledger-free fallback

A country can reach this stage after permanently accepting every conversion, losing its ledger states, or starting with no convertible military factory.

The fallback must be difficult but possible.

It should construct or convert one minimum arsenal through a longer civilian project. It must not require an Event 61 ledger unit that no longer exists.

## Restore the Service Registry

### Purpose

Rebuild the administrative basis for voluntary and limited service.

### Requirements

- Defence Ministry complete
- minimum Stability
- no active incompatible country system

### Duration

Base target: 150 days.

### Cost

- political power
- temporary civilian factory commitment

### Result

- allow the law to move from No Army to Disarmed Nation or Volunteer Only according to the accepted exit sequence
- restore access to ordinary recruitable population through the law
- unlock later conscription restoration

The project must not require army experience or current recruitable manpower.

## Emergency National Defence

### Role

This is the extreme-law emergency exit for a country under attack.

### Availability

Require an active defensive war, occupied core territory, or a verified imminent attack.

### Result

- rapidly establish the Defence Ministry
- reopen a minimal arsenal
- move the two extreme laws one step upward when engine-valid
- create temporary emergency formations only if the implementation can supply them without free-unit abuse
- apply a severe disorganization and civilian strain package

The emergency route should leave the country weaker than one that prepared before the crisis.

## Dynamic cost principles

Every decision uses the universal cost framework where applicable.

Cost scaling can use:

- civilian factory count
- unresolved converted capacity
- major status
- war state
- Readiness band
- reconversion phase
- embargo or depression state
- subject status
- recent emergency use

At most four spendable cost types may appear on one decision.

Most Event 61 decisions should use two or three.

Time and non-consumed conditions are requirements, not spendable cost types.

Every visible resource cost needs its matching texticon.

## Decision clutter rules

The category should never expose every possible state reopening target or every evolution protection family at once.

Use these hard limits:

- three targeted state reopening decisions visible at once
- five primary decisions visible in one phase
- one active mission visible at once
- one confirmation dialog at a time

When a mission or evolution response begins, hide low-priority ordinary actions until space is available.

Completed and invalid decisions must disappear cleanly.

## AI use of the category

AI countries use the same underlying decisions and costs.

AI can bypass the player-facing three-state selector limit while evaluating valid targets, but it still starts only one state reopening project per configured capacity band.

The AI must not:

- restart contracts without a target stance or threat reason
- reopen a state whose ledger has vanished
- spend civilian capacity that would collapse its basic economy
- restore a law that already changed externally
- take Emergency Rearmament without a valid emergency
- permanently abandon the ledger while its chosen stance requires rearmament
- accept an extreme-law pacifist route during active war

Detailed AI policy appears in Part 4.

## Rearmament acceptance conditions

The rearmament system is complete only when:

- Readiness is derived from real conditions and cannot be bought directly
- the player sees only one persistent number
- structural proof is checked separately from the score
- factory reopening consumes the physical state ledger one for one
- state decisions cannot restore more factories than available ledger and civilian capacity
- external law changes cannot produce duplicate Event 61 law gains
- normal recovery has a meaningful civilian and time cost
- Emergency Rearmament has a concrete threat gate and a serious aftermath
- permanent conversion is irreversible and confirmed
- the category remains escapable under Peacetime Economy and No Army
- early extreme-law exit steps do not require army experience or recruitable manpower
- visible decisions stay within the category action budget
- AI uses the same structural rules and cannot access hidden free outcomes

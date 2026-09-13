# Event 061: Return to Peacetime

## Part 3: Evolutions

## Evolution model

Event 61 has three global evolutions.

| Evolution | Chaos requirement | Core escalation |
| --- | ---: | --- |
| Swords into Ploughshares | 200+ | Dismantle eligible military stockpiles for civilian reconstruction |
| The Great Demobilization | 400+ | Muster out eligible standing divisions and return their manpower and equipment |
| Permanent Peace | 600+ | Introduce Peacetime Economy and No Army, with forced adoption for countries that have not credibly rearmed |

Evolution activation follows the shared Chaos Redux evolution system.

Reaching the Chaos threshold makes the evolution eligible. The shared evolution pacing then determines when it activates.

Activation itself adds zero Chaos.

Each activated evolution receives the normal Event Logs evolution record.

## Staggered application

A high-Chaos firing must not execute every evolved loss on the baseline tick.

The event uses visible warning missions and scheduled country reports.

Recommended sequence when all three evolutions are enabled and active:

| Relative time | Event layer |
| ---: | --- |
| Day 0 | Baseline transaction and national report |
| Day 7 | Swords into Ploughshares warning opens |
| Day 45 | Stockpile liquidation resolves |
| Day 46 | Great Demobilization warning opens |
| Day 106 | Division demobilization resolves |
| Day 107 | Permanent Peace settlement opens |
| Day 197 | Extreme-law settlement resolves |

The exact day count may be tuned, but the player must have a useful response window before every destructive evolved effect.

### Disabled evolution handling

Each evolution must remain independently disableable.

A disabled earlier evolution does not block a later enabled one.

If Swords into Ploughshares is disabled and The Great Demobilization is enabled, the division warning can begin after the baseline delay.

If both earlier evolutions are disabled and Permanent Peace is enabled, the settlement can begin after the baseline delay.

The implementation should schedule the next enabled unresolved layer instead of requiring a flag from a disabled layer.

### Active transition unlock

An evolution can activate while countries are still managing an earlier Event 61 firing.

When this happens:

- affected countries receive the new evolution warning without waiting for another baseline firing
- the new layer records its own activation and national handling
- earlier completed baseline effects do not repeat
- later Event 61 cycles use the evolution from their opening sequence

### Pre-activated evolution

When an evolution has already activated before a new Event 61 firing, that firing schedules the evolved layer once for the new cycle.

Each country records the last cycle ID handled for each evolution.

This prevents duplicate execution from save reload, repeated hidden events, or parallel calls.

## Evolution I: Swords into Ploughshares

### Purpose

A share of usable military stockpiles is dismantled, sold, or redirected into civilian reconstruction.

The evolution should target real surplus while preserving enough equipment to avoid arbitrary destruction of the army already in the field.

The player can protect a limited number of important reserve families by spending civilian capacity before the liquidation date.

### Warning mission

Working mission label:

`Inventory Liquidation`

Default duration: 38 days after the seven-day baseline delay, producing a day 45 resolution.

Acceptable balance range: 35 to 60 days.

The mission is a deadline, not a passive checklist.

During the mission the country can:

- protect selected stockpile families
- choose how civilian authorities use the recovered material
- restart arms contracts
- raise Readiness
- accept full liquidation

The mission resolves automatically at its deadline.

### Eligible stockpile principle

Only positive, removable, non-deployed conventional stockpile quantities are eligible.

The calculation should begin from equipment in national stockpile after deployed and training needs are excluded by the engine's stockpile model.

The implementation should then apply an additional reserve floor.

### Eligible equipment families

Target families, subject to local engine support:

- infantry equipment
- support equipment
- artillery
- anti-tank equipment
- anti-air equipment
- motorized equipment
- mechanized equipment
- armoured cars
- tanks and self-propelled variants
- conventional aircraft
- trains
- convoys
- other ordinary conventional equipment with safe stockpile removal semantics

Captured foreign variants are eligible.

Obsolete domestic variants are eligible.

Current-generation domestic variants are eligible only after the higher-priority categories cannot satisfy the calculated amount.

### Hard exclusions

Do not dismantle:

- equipment already issued to deployed units
- equipment reserved by an active lend-lease transaction when the engine exposes that commitment
- ships or naval task forces
- nuclear bombs
- ballistic or cruise missiles
- special project outputs
- unique event-owned equipment
- chemical, biological, supernatural, nonhuman, or other special equipment unless its owner explicitly marks it safe for ordinary stockpile removal
- equipment whose removal helper cannot prove an exact positive debit
- equipment categories that would be recreated through a free refund path

A missing safe removal route is a blocker for that family, not permission to delete an approximate value.

### Reserve floor

The evolution should preserve a defensive reserve before calculating surplus.

Preferred model:

- retain current reinforcement and training need
- retain approximately 90 days of fielded demand
- retain a minimum emergency reserve for equipment families used by active divisions
- retain a higher floor when the country is in a defensive war or faces an immediate threat
- retain a lower floor for obsolete and captured equipment

If the installed engine does not expose demand in a safe form, derive the floor from active battalions, support companies, air wings, and fielded equipment archetypes through an event-owned helper.

Do not use one flat reserve number for every country.

### Base liquidation share

The starting target is 25 percent of eligible surplus after reserve floors.

Dynamic range: 10 to 35 percent.

Suggested factors:

| Factor | Direction |
| --- | --- |
| Readiness below 20 | increase liquidation |
| Readiness 20 to 39 | small reduction |
| Readiness 40 to 59 | moderate reduction |
| Readiness 60 to 79 | strong reduction |
| Readiness 80 or higher | minimum normal share |
| defensive war | strong reduction |
| offensive war | modest reduction |
| secure peace and no hostile border | increase liquidation |
| Reconstruction Priority disposition | increase liquidation yield, not necessarily share |
| protected family | reduce that family's share to a very low band |
| merged repeat-cycle pressure | add a bounded amount |
| equipment shortage | reduce or eliminate the affected family share |

Recommended Readiness mitigation:

| Readiness | Share multiplier |
| ---: | ---: |
| 0 to 19 | 1.00 |
| 20 to 39 | 0.90 |
| 40 to 59 | 0.75 |
| 60 to 79 | 0.50 |
| 80 to 100 | 0.25 |

A defensive war can apply an additional multiplier that brings a protected shortage family to zero.

### Priority order

Within each eligible family, remove equipment in this order when the engine supports variant selection:

1. captured foreign equipment
2. obsolete variants
3. surplus older domestic variants
4. current standard variants

Do not remove current equipment while a sufficient quantity of obsolete or captured equipment remains.

If exact variant targeting is not possible for one archetype, the player-facing result should describe the family total without claiming a variant order that the engine did not enforce.

### Protection decisions

The category should show no more than three protection decisions at a time.

It selects the families with the largest eligible liquidation value and highest strategic relevance.

Working protection families:

- Protect Army Stores
- Protect Mobile and Armoured Reserves
- Protect Air Reserves
- Protect Logistics Reserves

#### Protect Army Stores

Covers infantry equipment, support equipment, artillery, anti-tank equipment, and anti-air equipment.

#### Protect Mobile and Armoured Reserves

Covers motorized, mechanized, armoured cars, tanks, and supported self-propelled variants.

#### Protect Air Reserves

Covers ordinary aircraft stockpiles with safe removal support.

#### Protect Logistics Reserves

Covers trains and convoys.

### Protection cost

Use:

- political power
- temporary civilian factory commitment

Optional third cost only when justified:

- a small Stability cost from public resistance to preserving military stockpiles

Protection should not consume the equipment it protects.

A protected family receives a very low liquidation share, such as 0 to 5 percent of eligible surplus, based on threat and Readiness.

Protection cannot preserve every family in one cycle unless a very large country has enough time and civilian capacity to complete several actions.

### Civilian disposition

The country can choose one of two public dispositions during the warning.

These are strategic uses of the recovered value, not separate equipment-removal quantities.

#### Central Reconstruction

Direct recovered material through public rebuilding programs.

Result direction:

- stronger construction and repair benefit
- more predictable national return
- higher civilian factory administration burden during the mission

This is the default when the player makes no selection.

#### Civilian Auctions

Sell equipment, vehicles, machine tools, and surplus property into civilian use.

DLC-safe result direction:

- lower construction benefit
- temporary consumer-goods or market benefit
- small Stability benefit when the public is secure
- corruption or loss risk only if a connected event later introduces it

When the relevant DLC is present, the implementation may add an International Market interaction. The base result must remain complete without it.

### Reconstruction value

The evolution converts equipment quantities into one hidden reconstruction-value total.

Use per-family value weights so one convoy, one aircraft, one tank, and one rifle do not count equally.

Centralize every value weight.

The total maps to a small number of capped benefit tiers.

Working timed spirit:

`Reconstruction Materials`

Suggested tiers:

| Tier | Relative recovered value | Construction and repair role |
| --- | --- | --- |
| I | modest | useful local rebuilding boost |
| II | substantial | strong national rebuilding boost |
| III | major | major but bounded rebuilding boost |
| IV | exceptional | strongest capped benefit for a very large liquidation |

Starting modifier targets:

| Tier | Construction speed | Repair speed | Duration |
| --- | ---: | ---: | ---: |
| I | `+5%` | `+10%` | 120 days |
| II | `+10%` | `+20%` | 150 days |
| III | `+15%` | `+30%` | 180 days |
| IV | `+20%` | `+40%` | 210 days |

The exact modifiers must be checked against local vanilla syntax.

The benefit does not create permanent factories.

The benefit does not refund equipment.

The benefit cannot stack with another copy from a merged pending cycle. A stronger new result replaces the weaker or extends it within a cap.

### Resolution report

The national result should summarize:

- total equipment units removed by broad family
- protected families
- reconstruction-value tier
- chosen disposition
- any family skipped because no safe or positive surplus existed

Do not create one popup per equipment type.

AI countries resolve silently and record a compact result.

### Interaction with Event 94

Event 94 calculates its own stockpile loss from the remaining stockpile at its resolution time.

If Event 94 fires before Inventory Liquidation resolves, Event 61 recalculates eligible surplus at the deadline.

Event 61 does not preserve an outdated equipment quantity from mission start.

### Repeat-cycle pressure

When another Event 61 cycle merges into an active Inventory Liquidation mission:

- retain one visible mission
- add 5 percentage points to the unmitigated base share per merged cycle
- cap the total base share at 40 percent before Readiness, threat, and protection reductions
- extend the deadline only enough to give the player at least the minimum response window after the later firing

### Evolution record

Record one global activation entry when the evolution activates.

Each country resolution can record a country-specific stage only when the shared evolution log supports meaningful actor rows without flooding the history.

A preferred compromise is one activation row plus the Event 61 history totals for each later cycle.

## Evolution II: The Great Demobilization

### Purpose

A share of standing conventional divisions is mustered out.

Their manpower and equipment return through a safe disband transaction.

Countries that rebuilt military institutions can protect cadres and important border formations.

### Warning mission

Working mission label:

`Mustering Out`

Default duration: 60 days.

Acceptable range: 45 to 90 days.

The mission begins after the previous enabled evolution resolves or after the baseline delay when earlier evolutions are disabled.

During the mission the country can:

- retain essential cadres
- mark bounded border formations as essential
- raise Readiness
- accelerate mustering out for a stronger civilian benefit
- use an emergency path when a war begins

### Eligible division contract

A division can be considered only when it is an ordinary land formation that the engine can safely disband with manpower and equipment returned.

Exclude:

- expeditionary forces controlled for another country
- foreign volunteers abroad
- divisions currently in combat
- divisions in active naval transport or invasion
- encircled divisions when the engine cannot guarantee safe return
- divisions marked locked, undeletable, or event-owned
- temporary civil-war formations whose owner package handles cleanup
- mutiny, zombie, alien, supernatural, chemical, biological, clone, or other special formations unless their owner explicitly marks them safe
- units whose deletion effect would destroy manpower or equipment instead of returning them
- units in a scope state that the local engine documentation marks unsafe for scripted disband

The event should fail closed for uncertain unit families.

### Candidate priority

Eligible divisions receive a demobilization score.

Prefer to muster out:

1. reserve or rear-area formations
2. formations far from a hostile front
3. low-experience formations
4. understrength formations
5. formations with low equipment percentage
6. duplicate small templates when the country retains stronger formations of the same role
7. formations not guarding the capital, a hostile border, a port, or a critical supply route

Prefer to retain:

- veteran formations
- formations in or near an active defensive front
- formations guarding occupied core states
- armoured or specialized formations that would be hard to recreate
- the country's minimum coherent army structure
- formations protected by a completed cadre or border decision

The score should use a seeded tie break.

### Base demobilization share

Starting target: 25 percent of eligible divisions for a secure peacetime country with low Readiness.

Dynamic range: 5 to 25 percent before merged-cycle pressure.

Suggested factors:

| Factor | Direction |
| --- | --- |
| Readiness below 20 | full share |
| Readiness 20 to 39 | small reduction |
| Readiness 40 to 59 | moderate reduction |
| Readiness 60 to 79 | strong reduction |
| Readiness 80 or higher | zero or minimum share |
| defensive war | near-zero share |
| offensive war | reduced share |
| occupied core territory | strong reduction |
| no hostile border and high Stability | increase toward full share |
| general staff restored | reduce share |
| cadre decision complete | reduce count and protect priority units |
| voluntary accelerated demobilization | increase share |
| merged repeat-cycle pressure | bounded increase |

Suggested readiness result:

| Readiness | Maximum normal share |
| ---: | ---: |
| 0 to 19 | 25% |
| 20 to 39 | 20% |
| 40 to 59 | 15% |
| 60 to 79 | 5% to 10% |
| 80 to 100 | 0% |

A country in a defensive war should resolve at zero unless it voluntarily accelerates demobilization.

### Tiny-army protection

Use the eligible division count after exclusions.

| Eligible divisions | Maximum involuntary demobilization |
| ---: | ---: |
| 0 to 3 | 0 |
| 4 to 7 | 1 |
| 8 to 15 | floor of calculated share, minimum 1 only when share is positive |
| 16 or more | calculated share with national minimum-force guard |

The implementation should preserve a minimum coherent force for ordinary countries.

A large army can lose many divisions. A four-division minor cannot lose half its army from percentage rounding.

### Retain Essential Cadres

#### Role

Preserve officers, training staff, specialist teams, and selected formations.

#### Cost

Use:

- army experience
- political power
- temporary civilian factory commitment when needed

#### Result

- reduce the calculated division target
- protect the highest-value eligible formations
- complete a material-preparation action for Readiness
- provide one structural action for the Evolution III last-chance test

The decision does not generate new divisions or equipment.

### Mark Border Formations Essential

#### Availability

Available only when the country has:

- a hostile land border
- an enemy war goal
- occupied core territory
- an active defensive war
- another verified immediate territorial threat

#### Result

Protect a bounded number of eligible formations assigned to or physically present in named threatened states.

The tooltip must identify the relevant states or named border region.

Do not protect arbitrary formations anywhere in the country.

### Accelerate Mustering Out

#### Role

A voluntary pacifist and reconstruction option.

#### Result

- increase the eligible demobilization target by a bounded amount
- improve the Veteran Reintegration benefit
- reduce Readiness
- mark voluntary demobilization for route and achievement checks

The player must see the approximate number of additional divisions at risk before confirming.

### Safe disband transaction

Every selected division must use a verified native or project-supported disband effect that returns manpower and equipment.

The implementation must validate this against the installed vanilla documentation and a local precedent.

A unit-deletion effect that silently destroys its contents is not acceptable.

For each successful disband:

- record the unit selection
- disband through the verified safe route
- record returned manpower when measurable
- record returned equipment by broad family when measurable
- increment the country demobilized-division count

If the safe route fails for one unit, skip that unit and continue only when the transaction remains deterministic.

### Veteran Reintegration

The civilian benefit represents trained workers, technicians, drivers, engineers, and administrators returning from service.

Working timed spirit:

`Veteran Reintegration`

It should provide a meaningful civilian construction, repair, or production-efficiency recovery benefit.

It should also impose a modest temporary consumer or housing burden so mass demobilization is not a free economic gain.

The benefit scales through capped tiers based on returned manpower and number of divisions.

It must not grant recruitable manpower directly.

### Resolution report

Summarize:

- divisions disbanded
- approximate manpower returned when measurable
- broad equipment families returned when measurable
- protected formations or regions
- Readiness protection applied
- Veteran Reintegration tier

Do not show internal selection scores.

### War beginning during mission

If the country enters a defensive war before the deadline:

- recalculate target immediately
- normally reduce involuntary target to zero
- keep voluntary accelerated demobilization only if the player confirms again
- retain completed cadre protection
- allow Emergency Rearmament

If the country begins an offensive war:

- reduce the involuntary target but do not automatically cancel it
- increase AI rearmament priority
- preserve the rule that units currently in combat are excluded

### Repeat-cycle pressure

A merged cycle adds a bounded amount to the base share, such as 5 percentage points per cycle, capped at 35 percent before Readiness and war reductions.

Tiny-army and safety guards remain absolute.

## Evolution III: Permanent Peace

### Purpose

Governments that fail to rebuild a credible defence structure can be pushed below the ordinary law floors.

Two extreme laws become available:

- Peacetime Economy
- No Army

The evolution creates a national settlement period before those laws are forced.

Countries that had clearly begun remilitarizing can avoid the forced transition.

Countries at war receive a provisional deferral so the system does not abolish an army during active national survival.

### New law: Peacetime Economy

Peacetime Economy sits below Civilian Economy.

It represents a government that has dismantled most military production institutions and directs economic planning toward civilian recovery.

Modifier direction:

- severe military factory output penalty
- strong dockyard output penalty
- severe military factory construction penalty
- strong civilian-to-military conversion penalty
- reduced production efficiency cap for military production
- cheaper or faster military-to-civilian conversion
- modest civilian construction and repair benefit
- higher consumer or administrative burden when needed for balance

Starting balance targets:

| Modifier role | Target |
| --- | ---: |
| Military factory output | `-50%` |
| Dockyard output | `-35%` |
| Military factory construction speed | `-75%` |
| Civilian-to-military conversion speed or cost | severe penalty |
| Military-to-civilian conversion speed or cost | strong bonus |
| Production efficiency cap | `-20%` |
| Civilian construction speed | `+10%` |
| Repair speed | `+25%` |

Exact law syntax and modifier availability must be verified locally.

### First transition factory effect

The first forced or voluntary transition into Peacetime Economy during an unresolved Event 61 state converts an additional share of remaining eligible military factories.

Amount:

`floor(remaining eligible military factories / 3)`

A minimum of one applies only when at least three eligible military factories remain.

Every conversion uses the same one-for-one state ledger transaction as the baseline.

The first-transition effect is guarded.

Changing out of the law and returning later does not repeat the extra conversion for the same Event 61 cycle.

A later Event 61 cycle can create a new guarded first transition.

### New law: No Army

No Army sits below Disarmed Nation.

It represents the legal abolition of the conventional standing army.

Modifier direction:

- zero or near-zero ordinary recruitable population
- conventional division training effectively unavailable
- severe army training-time penalty
- severe army experience gain penalty
- very low mobilization speed
- reduced command capacity where the law system supports it

The law should not invalidate event-owned nonhuman or special formations whose owners cannot use normal conscription.

### First transition division effect

The first forced or voluntary transition into No Army during an unresolved Event 61 state schedules a final warning and then disbands every remaining eligible conventional standing division through the verified safe route.

Use the same hard exclusions as The Great Demobilization.

Do not disband:

- divisions currently in combat
- foreign expeditionary or volunteer formations
- locked or undeletable event-owned formations
- units whose owner package forbids generic disband
- units without a verified safe return route

Temporarily unsafe ordinary units remain marked for a bounded follow-up pass after they leave combat.

The system must not run an endless daily search. Use scheduled bounded checks with a maximum duration and a clear unresolved report.

### National Defence Settlement

Working mission label:

`National Defence Settlement`

Default duration: 90 days.

Acceptable range: 75 to 120 days.

### Immediate exemption

A country is exempt at settlement start when:

- Readiness is at least 50
- meaningful rearmament structural proof exists

This recognizes countries that acted before the final warning.

The exempt country still keeps all baseline and earlier evolution effects.

It does not enter Peacetime Economy or No Army through this settlement.

### Last-chance exemption

A country that was not immediately exempt can avoid forced adoption by the deadline when it:

- reaches Readiness 60
- completes at least two structural actions during or before the settlement
- has at least one of the two actions be factory reopening, economy-law restoration, or conscription-law restoration
- is not relying only on a temporary emergency bonus that will expire at the deadline

This higher requirement prevents a country from waiting until the final days and purchasing one superficial action.

### Valid settlement actions

Actions that can count:

- reopen Event 61 factory capacity
- restore an Event 61 economy-law step
- restore an Event 61 conscription step
- complete the General Staff project
- retain essential cadres
- complete a major stockpile-protection action
- establish a Defence Ministry
- complete a National Rearmament Program

Only the first qualifying completion of an action family counts toward the two-action requirement.

Repeated public campaigns do not count twice.

### Active-war deferral

A country at war when the settlement would resolve receives a provisional defence deferral.

The laws are not forced during active war.

The deferral distinguishes war context:

- defensive war grants the strongest protection and immediate emergency access
- offensive war still defers abolition, but does not excuse later failure to rearm
- civil war uses owner-specific compatibility and should not disband one side through a generic global transaction

When the country returns to peace, start a postwar settlement with the same 90-day target unless the country already meets the immediate exemption.

A country cannot keep the deferral forever by joining irrelevant wars after the postwar mission begins. New wars can pause forced abolition only when the country faces direct military danger under a verified test.

### Forced resolution

A non-exempt country at the deadline:

1. moves to Peacetime Economy
2. applies the guarded additional factory conversion
3. moves to No Army
4. begins the guarded final conventional division demobilization
5. applies the Peace Dividend benefit
6. keeps the Return to Rearmament category open in its extreme-law recovery phase
7. records the country outcome for Event 61 history totals

The law changes and first-entry effects must be idempotent.

### Voluntary Permanent Peace

A country that would otherwise be exempt can voluntarily accept both extreme laws.

The confirmation should show:

- expected additional factory conversion
- status of remaining conventional divisions
- loss of Readiness
- Peace Dividend direction
- difficulty of returning to normal defence laws

The decision should appeal to a secure pacifist or reconstruction-focused player through a real civilian benefit.

It should not be the dominant economic choice for a threatened country.

### Peace Dividend

Working staged spirit:

`Peace Dividend`

Role:

- reward the civilian route with higher Stability and useful reconstruction capacity
- offset part of the cost of permanent demilitarization
- never restore the military capacity being dismantled

Possible modifier direction:

- Stability gain or maintenance
- civilian construction speed
- repair speed
- infrastructure and housing construction support when valid
- reduced military spending represented through a limited consumer-goods benefit

The benefit should be bounded and should weaken or disappear as the country exits the extreme laws.

A country that uses Emergency National Defence loses the strongest Peace Dividend tier immediately.

### Extreme-law exit

The Return to Rearmament category remains available.

The normal route is:

1. Re-establish a Defence Ministry
2. Reopen the National Arsenal
3. Restore the Service Registry
4. move from Peacetime Economy to Civilian Economy
5. move from No Army to Disarmed Nation or Volunteer Only
6. continue ordinary Event 61 law restoration where targets remain
7. rebuild divisions through normal production and recruitment

The initial projects use political power, civilian factory commitment, and time.

They do not require army experience or recruitable manpower that the laws made inaccessible.

### Emergency extreme-law exit

A country under attack can use Emergency National Defence.

It moves the country out of the two extreme law floors through a fast path and opens minimal defence production.

It also applies severe temporary disorganization and civilian strain.

The emergency route must not give a larger permanent army, more factories, or better laws than the normal route would eventually allow.

### New country and released country handling

A country created after Evolution III activates does not automatically receive the extreme laws merely because the evolution exists.

It enters Event 61 only through:

- a later normal Event 61 firing
- an inherited state or country transition that explicitly carries unresolved Event 61 state
- a future event connection that calls the Event 61 setup contract

A country inheriting ledgered states can reopen their physical capacity. It does not inherit another country's law restoration target or Readiness score.

### Repeat firing under extreme laws

A later baseline firing still converts half of currently eligible military factories and applies the War Support, Stability, reconversion, and valid law components.

A country already under Peacetime Economy or No Army remains at those floors.

The Evolution III first-entry additional factory conversion and final division demobilization do not repeat merely because the law is already active.

The new cycle can create a fresh first-entry guard only if the country had left the law and the later cycle's settlement forces or voluntarily restores it again.

## Evolution AI summary

### Swords into Ploughshares

AI priority:

1. preserve shortage families needed by fielded units
2. protect logistics in active wars
3. protect air or armoured reserves when doctrine and industry depend on them
4. accept broader liquidation when secure and reconstruction-focused

### The Great Demobilization

AI priority:

1. cancel involuntary demobilization during defensive war
2. preserve cadres and threatened-border units
3. retain a coherent minimum force
4. accept normal peacetime reductions when secure
5. accelerate only for strongly pacifist, isolated, stable countries

### Permanent Peace

AI priority:

1. avoid forced laws during direct military danger
2. pursue exemption when a major, faction leader, hostile-border state, or likely target
3. accept the civilian route only when secure, isolated, politically compatible, and economically able to benefit
4. use emergency exit immediately when attacked under extreme laws

Detailed scoring appears in Part 4.

## Evolution acceptance conditions

The three-evolution package is complete only when:

- each evolution respects its Chaos threshold and enable state
- activation uses shared evolution pacing and logging
- activation itself changes no Chaos
- active countries receive newly activated evolutions without a fresh baseline firing
- high-Chaos opening effects are staggered
- disabled earlier evolutions do not block later ones
- stockpile liquidation uses positive surplus, reserve floors, safe exact debits, and hard family exclusions
- protection decisions reduce the correct family and do not protect the entire stockpile
- reconstruction benefits are capped and cannot create permanent factory rewards
- division demobilization uses a verified safe disband that returns manpower and equipment
- tiny armies and special units are protected
- active defensive wars cancel or nearly eliminate involuntary division cuts
- Permanent Peace uses an immediate exemption and a stricter last-chance exemption
- active war causes a bounded deferral and postwar review
- first-entry factory and division effects are idempotent
- the extreme-law exit cannot soft-lock a country through unavailable military resources
- repeat cycles merge visible warnings instead of creating mission spam

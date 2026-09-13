# Event 061: Return to Peacetime

## Part 5: Balance targets, anti-exploit rules, and edge cases

## Balance purpose

Return to Peacetime should materially change a campaign.

The baseline removes war-production capacity and public willingness immediately. Rearmament remains possible, but it consumes the civilian economy that the event created.

The event should create different recovery times for different countries without turning a small state into an unrecoverable spectator.

The values in this part are starting targets. Final values require script validation, probability analysis, controlled save tests, and live playtesting.

## Core balance targets

| Surface | Starting target |
| --- | --- |
| Baseline factory conversion | `floor(eligible military factories / 2)` |
| War Support transfer | 50% of current War Support |
| Economy law movement | one valid step toward Civilian Economy |
| Conscription movement | one valid step toward Disarmed Nation |
| Reconversion shock | 270 days across three phases |
| Repeat shock maximum | 540 days remaining |
| Meaningful rearmament | Readiness 50 plus structural proof |
| Last-chance exemption | Readiness 60 plus two structural actions |
| Strong protection band | Readiness 80+ |
| Evolution I base surplus share | 25% |
| Evolution I dynamic range | 10% to 35%, with merged-cycle cap at 40% |
| Evolution II secure-peace share | up to 25% of eligible divisions |
| Evolution II merged-cycle cap | 35% before safety and war reductions |
| Evolution III added factory conversion | one third of remaining eligible military factories |
| Standard category size | at most five primary actions and one mission |

## Recovery time bands

The system should produce these approximate recovery horizons for a country that actively pursues rearmament:

| Country profile | Expected recovery |
| --- | --- |
| Small threatened minor restoring a basic defence | 6 to 12 months |
| Medium country restoring most lost capacity | 12 to 24 months |
| Major rebuilding the full ledger and both law targets | 24 to 48 months |
| Country forced into both extreme laws | longer than the corresponding normal recovery unless emergency action is used |

These horizons include parallel projects where the project-cap rule permits them.

A major should not restore fifty military factories through one 90-day click.

A one-factory minor should not wait four years to regain a usable army law.

## Factory conversion progression

Repeated baseline firings shrink the remaining eligible military base by approximately one half each time, subject to floor rounding and any factories built or restored between cycles.

Example without restoration or new construction:

| Starting eligible military factories | After first firing | After second firing | After third firing | Ledger total after third firing |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 | 0 |
| 2 | 1 | 1 | 1 | 1 |
| 5 | 3 | 2 | 1 | 4 |
| 10 | 5 | 3 | 2 | 8 |
| 25 | 13 | 7 | 4 | 21 |
| 100 | 50 | 25 | 13 | 87 |

This exponential pressure is strong enough for a repeatable event. The repeatable weight cap and recovery pacing are balance requirements.

## Small-country protection

Small countries receive the same global policy shock, but integer floors and project scaling protect them from total removal.

Rules:

- one eligible military factory is never converted by the baseline
- Evolution III additional conversion requires at least three remaining eligible military factories before its minimum one applies
- a country with no ledger can use a longer minimum-arsenal recovery project under the extreme laws
- tiny armies use the absolute division cap in Part 3
- first extreme-law exit steps cannot require army experience or recruitable manpower
- dynamic factory commitments must never require more available civilian factories than the country can legally assign

A small country can still suffer severe law and production penalties. The protection prevents arithmetic elimination, not consequence.

## Major-country scaling

Large industrial countries should face large physical losses and long restoration programs.

Recommended scaling:

- factory reopening batch size rises to five
- several state projects can run in parallel within a maximum of three ordinary projects
- political power cost rises more slowly than factory-day cost
- large ledger restoration uses many repeated state projects
- Evolution I value tiers cap civilian benefits so a huge stockpile does not create unlimited construction power
- Evolution II division selection can remove many formations while preserving the minimum coherent-force ratio

Majors should retain the option to rebuild faster through Emergency Rearmament, but the civilian strain and production disorganization must be large enough to matter.

## Law target balance

Event 61 records ranks it removed.

This avoids two opposite failures:

- a decision that cannot restore the actual event damage
- a decision that grants a law higher than the country had before the event

Repeated firings can deepen the law loss while preserving the highest unresolved restore target.

External upward changes count toward restoration.

External downward changes do not increase the Event 61 restore target unless Event 61 caused them.

## War Support and Stability balance

The transfer can create very high Stability for a country with strong War Support.

That is intended as the civilian political benefit of demobilization.

Balance controls:

- the Stability ceiling destroys overflow
- rearmament transfers back inefficiently
- public defence actions have cooldowns
- high Stability can increase AI willingness to accept reconstruction
- voluntary extreme-law routes can require high Stability
- no direct Chaos reduction is awarded

The event should not apply a separate arbitrary Stability bonus beyond the transfer.

## Reconstruction benefit caps

Swords into Ploughshares converts equipment value into a timed benefit.

Cap rules:

- a country receives one Reconstruction Materials spirit
- stronger new tiers replace weaker ones
- equal tiers extend duration within a maximum
- recovered value above the highest threshold gives no larger modifier
- no permanent civilian factory is granted from equipment dismantling
- no political power is generated per equipment unit
- captured equipment cannot be cycled through lend-lease and recovery for repeated benefit

Suggested maximum duration after merging or repeat cycles: 360 days.

## Veteran Reintegration caps

The Great Demobilization can create one timed Veteran Reintegration spirit.

Cap rules:

- benefit tier uses returned manpower and division count, not template name
- repeated small division templates cannot produce a larger result than their actual manpower and equipment value
- selected divisions must exist before the mission begins or pass a minimum-age check to block last-minute template spam
- the spirit does not add recruitable manpower
- the consumer or housing burden scales with the same tier
- stronger new tiers replace weaker ones

Suggested maximum duration: 360 days.

## Readiness anti-farming rules

Readiness is recalculated from current state.

It should not preserve points from structures that no longer exist.

Examples:

- reopened factory lost through state occupation no longer contributes until the country again owns and controls the ledger state
- law points fall when another event moves the law downward
- War Support points fall when War Support falls
- protection or cadre proof remains as a completed institutional action for the current transition, but does not count across unrelated future cycles unless the institution still exists
- emergency temporary bonuses do not satisfy the final settlement at their expiry tick

Readiness is clamped to 0 through 100 after every update.

## Structural-action counting

Evolution III counts action families, not clicks.

A country cannot complete the last-chance exemption by:

- taking the public defence campaign twice
- reopening one factory in two one-level clicks from the same completed project
- toggling a law up and down
- cancelling and restarting contracts
- taking two protection decisions from the same family

Valid two-action combinations include:

- reopen factories plus restore economy law
- reopen factories plus reconstitute general staff
- restore economy law plus restore conscription
- retain cadres plus reopen factories
- establish Defence Ministry plus reopen National Arsenal

At least one action must be a factory or law structural action.

## Factory ledger exploit table

| Exploit risk | Required prevention |
| --- | --- |
| Free military factories from reopening | Every restored level consumes one civilian factory and one positive state ledger unit atomically |
| New civilian construction counted as converted capacity | Only Event 61 conversion increments the ledger |
| Annexed civilian factories used as free Event 61 restoration | Annexation does not create ledger units |
| State ledger restored by former owner after state loss | Ledger belongs to the state and only the current valid owner can act |
| Two countries reopen the same state | Ownership and control rechecked at decision completion |
| Project completes after ledger was spent elsewhere | Ledger and civilian level rechecked for every atomic conversion |
| Save reload repeats completion | Project completion and cycle guards are persistent and idempotent |
| Permanent conversion clears another owner's claim | Only owned and controlled states are cleared |
| Destroyed civilian building recreated for free | Restoration is capped by available civilian factory levels |
| Repeated first-entry Peacetime Economy conversion | Guard first entry per Event 61 cycle |
| Parallel projects exceed ledger | Reserve planned batch or recheck in deterministic completion order, then refund unused commitment through the cost framework |
| State slot limit produces an extra building | One-for-one conversion checks building ceiling before both changes |

## Law exploit table

| Exploit risk | Required prevention |
| --- | --- |
| Event 82 restores a step, then Event 61 restores it again | Compare current rank to stored target at completion |
| Player changes law manually during project | Recheck current and target ranks at completion |
| Player cycles law down to farm Readiness actions | Structural action family counts once and Readiness reflects current law |
| Repeat firing overwrites a higher restore target with a lower one | Store the maximum unresolved target rank |
| Extreme law first-entry reward repeats through toggling | Guard by cycle and transition state |
| Incompatible law group receives invalid token | Validate law group and token before movement |
| Event 61 restores above the pre-event law | Normal decision availability stops at the target rank |
| No Army prevents its own exit | First exit steps use civilian resources and political power |

## Stockpile exploit table

| Exploit risk | Required prevention |
| --- | --- |
| Negative or zero debit becomes equipment gain | Shared debit helper requires a positive amount and fails closed |
| Equipment moved into deployed units after warning avoids every loss | Recalculate positive stockpile and reserve floors at resolution, accept that genuinely deployed equipment is outside stockpile |
| Equipment purchased immediately after liquidation creates extra reconstruction tier | Value uses the actual amount removed, not pre-mission stockpile |
| Lend-lease equipment counted twice | Exclude committed amounts when engine support exists and record the compatibility result |
| Unsupported special equipment is deleted | Unknown families are excluded by default |
| Obsolete equipment gives same value as advanced aircraft | Use centralized per-family and generation-aware value weights where engine data permits |
| Captured equipment is sent out and returned for repeated benefit | Track actual debit and apply spirit cap, with no per-unit political reward |
| Event 94 leaves stale Event 61 amount | Recalculate at Event 61 resolution |
| Convoy removal breaks active overseas supply completely | Apply reserve floor and threat modifier |
| Current-generation shortages are removed before obsolete surplus | Use variant priority when supported, otherwise keep a larger family reserve floor |

## Division exploit table

| Exploit risk | Required prevention |
| --- | --- |
| Player creates many one-battalion divisions to inflate reintegration | Minimum unit age and benefit based on returned manpower and equipment |
| Script deletion destroys manpower and equipment | Use verified safe disband only |
| Special event units vanish | Owner-safe classification and default exclusion |
| Units in combat disappear | Hard exclusion and completion recheck |
| Expeditionary units are treated as national units | Hard exclusion |
| Tiny minor loses its whole army | Absolute tiny-army cap and minimum coherent force |
| Player moves every unit to combat to evade the event | Defensive war can legitimately protect units, but offensive manipulation retains a bounded rear-area target and can defer unresolved units |
| Save reload selects a second set | Persist selected or completed transaction guards |
| Duplicate template spam changes priority | Selection uses manpower, equipment, experience, age, and template count together |
| Units created after warning receive protection or become targets unexpectedly | Use a minimum age for ordinary target eligibility and recalculate only under documented emergency rules |

## Emergency action exploit table

| Exploit risk | Required prevention |
| --- | --- |
| Emergency Rearmament used in safe peace | Concrete threat gate |
| Country starts a trivial offensive war to qualify | Offensive war has stricter gate, higher cost, and no defensive override |
| Emergency action repeated in one cycle | One persistent cycle guard |
| Emergency action gives more permanent capacity than normal route | Bounded restoration and normal target ceilings |
| Emergency action avoids all aftermath | Improvised Rearmament and civilian commitment persist after war |
| Emergency National Defence becomes free army generation | Any temporary formations need full equipment, manpower, cleanup, and anti-duplication rules |
| Emergency bonus passes Evolution III after it expires | Settlement checks current structural state at deadline |
| Achievement route uses emergency shortcut | Explicit disqualifier flags |

## Ownership and annexation edge cases

### State changes owner before baseline completes

The baseline transaction should process a state in the current country scope only while ownership and control remain valid.

If a state changes during iteration, skip it and continue with other candidates.

Do not chase the original quota into another owner's territory.

Record any shortfall from the calculated quota as a transaction shortfall for debugging.

### State changes owner after conversion

The state ledger follows the state.

The new owner can reopen capacity when it is a valid ordinary country and controls the state.

The former owner loses that state from its industrial pillar and unresolved owned-state total.

### Annexation of a country with active Event 61 state

The annexed country state cleans up country-scoped missions, project commitments, and law targets.

State ledgers remain on annexed states.

The annexer receives access through ownership reconciliation.

The annexer does not inherit the annexed country's Readiness or completed structural-action count.

### Country released from annexed territory

The released country sees ledgered capacity in states it owns.

It begins with its own Readiness calculation and no inherited law restoration target unless the release package explicitly carries an Event 61 transition.

### Civil war

A civil-war splinter receives no automatic copy of the parent country's law target or Readiness unless the civil-war system explicitly divides state.

State ledger follows state ownership.

The parent and splinter each calculate their own current law posture.

The Great Demobilization should normally defer generic division selection while a new civil war is active, then resolve through a postwar review.

## Control edge cases

A country can own a state without controlling it.

Rules:

- baseline factory conversion uses owned and controlled states
- reopening uses owned and controlled states
- occupied ledger remains dormant
- an occupying foreign controller cannot reopen the owner's ledger unless it becomes owner
- control restoration triggers or schedules reconciliation

This avoids rewriting an occupied state's permanent building mix for a temporary controller.

## Factory damage edge cases

Building damage can make visible counts differ from total building levels.

The implementation should use physical building levels for conversion and restoration, then respect damage through project duration and availability.

The event should not heal damaged factories.

A reopening action can convert a damaged civilian factory into a damaged military factory only when the verified engine transaction preserves damage safely. Otherwise require the civilian level to be repaired first.

This exact behavior is an engine-validation gate.

## Building slot edge cases

A one-for-one conversion should not change used building slots.

Still verify the target building can exist in that state.

If the engine requires separate removal and addition and the addition would fail, perform a precheck or use an atomic helper.

Never remove the military factory before proving that the civilian addition is valid.

## Law floor and ceiling edge cases

### Already at Civilian Economy

The baseline economy law component resolves at zero.

The event still records the current law and can later force Peacetime Economy through Evolution III.

### Already at Disarmed Nation

The baseline conscription component resolves at zero.

The event can later force No Army through Evolution III.

### Already at Peacetime Economy or No Army

The baseline leaves the law at its floor.

It does not repeat the Evolution III first-entry effect unless a new cycle has a valid new first transition after the country previously left the law.

### Higher custom law

A custom ordinary law can join the ordered mapping only after its owner defines the adjacent step.

Unknown custom laws are skipped with an internal compatibility result.

## War-state edge cases

### Defensive war at baseline

The baseline still applies because the event is global.

The player receives immediate access to Emergency Rearmament.

Later Evolution I and II effects receive strong protection.

Evolution III forced laws are deferred.

### Offensive war at baseline

The baseline still applies.

The country receives a strong rearmament AI stance and a narrower emergency path.

Evolution II can still demobilize a small rear-area share after safety exclusions.

### War begins during an active project

Normal rearmament projects continue unless their civilian commitment becomes impossible.

The category refreshes emergency actions and evolution protection.

### War ends during an Evolution III deferral

Start or resume the postwar settlement.

Give the country the full tuned response window unless it already used most of a prior postwar window and deliberately re-entered a trivial war.

### Permanent low-intensity war exploit

A country cannot use a distant irrelevant war to defer extreme-law settlement forever.

The deferral requires direct military danger, occupied core territory, an active front, enemy war goal, or another strong connection.

## Government and controller edge cases

### Player joins an AI country

Keep all state and timers.

Show the category in its current phase.

Do not replay the baseline report unless the implementation has a standard recent-event catch-up surface.

### Player leaves a country

AI policy begins on the next active-country pulse.

### Government changes ideology

Recalculate AI policy.

Do not reset Readiness, law targets, or ledger.

### Government-in-exile

Process every compatible country-level baseline component.

Physical factory and division components resolve from actual valid assets.

Avoid creating a factory project when the country owns no valid state and has no ledger.

## Repeat-cycle edge cases

### Repeat during baseline report

The event system should serialize global firings. A second Event 61 entry must not interleave state transactions with the first.

### Repeat during Inventory Liquidation

Merge into one mission and increase pressure within the cap.

### Repeat during Mustering Out

Merge into one mission and increase pressure within the cap.

### Repeat during National Defence Settlement

Do not create another settlement row.

Refresh baseline damage and update the settlement calculation.

The original deadline can extend enough to give the minimum response window after the new baseline, subject to a maximum total extension.

### Repeat after permanent conversion

The country can suffer new baseline conversions from military factories that exist at the later firing.

New ledger capacity is created only for those new conversions.

### Repeat after full restoration

The new cycle begins normally.

Completed flags from an earlier cycle should not block new valid actions, but permanent one-time achievement progress and emergency disqualifiers remain recorded as designed.

## Save and reload requirements

Persistent data:

- global cycle identifier
- country last-applied cycle by baseline and evolution
- state ledger count
- law restoration targets
- Readiness and pillar-state inputs
- active projects and missions
- merged-cycle pressure
- evolution first-entry guards
- emergency use and achievement disqualifiers
- voluntary permanent-conversion choices
- active staged spirits and remaining stage

On reload:

- no baseline component repeats
- no project pays twice
- no state conversion repeats
- no evolution resolution repeats
- active mission deadlines remain correct
- category target list rebuilds from current valid state
- stale target decisions disappear

## Performance budget

Event 61 is allowed to perform a large one-time global transaction when it fires.

It should avoid permanent broad iteration.

### Allowed bounded work

- one all-country pass on global firing
- one owned-state pass per affected country for factory conversion
- one stockpile-family pass at Evolution I resolution
- one division selection pass at Evolution II or No Army resolution
- one scheduled country pulse every 30 days only for countries with active Event 61 state
- immediate recalculation after Event 61 actions

### Avoid

- daily all-country checks
- weekly all-state checks
- repeated full stockpile scans while a warning is active
- per-division daily monitoring
- parallel duplicate missions from repeat firings
- one event popup per equipment family or disbanded unit

### Cleanup

The country pulse stops when:

- no state ledger is owned
- no law restoration target remains unresolved
- no Event 61 spirit is active
- no Event 61 project or mission is active
- neither extreme law is active
- no deferred settlement remains

State ledger variables can remain on states because they are physical restoration rights. Clear the accompanying marker when the count reaches zero.

## Failure handling

A partial component failure must not corrupt the rest of the country transaction.

Examples:

- factory conversion shortfall does not block law movement
- incompatible law does not block War Support transfer
- unsupported equipment family is skipped while supported families resolve
- one unsafe division is skipped while other safe candidates resolve

Every failure should produce a debug or validation record with:

- event cycle
- country
- component
- requested amount
- completed amount
- reason

Player-facing text should mention only material visible shortfalls.

## Validation scenarios

The implementation should include scripted or manual tests for at least these cases:

1. country with zero military factories
2. country with one military factory
3. country with two military factories
4. major with military factories across many states
5. country with occupied industrial core states
6. subject with low autonomy
7. faction leader at peace
8. defensive war participant
9. offensive war participant
10. country already at Civilian Economy and Disarmed Nation
11. country under both Evolution III laws
12. repeat firing before earlier warning resolves
13. Event 82 firing during recovery
14. Event 94 firing during Inventory Liquidation
15. state ownership change with positive ledger
16. annexation of a country with active projects
17. release of a country into ledgered states
18. save and reload during each mission
19. save and reload at factory-project completion
20. civil war during The Great Demobilization
21. special event units mixed with ordinary divisions
22. stockpile containing ordinary and special equipment
23. permanent conversion followed by a later Event 61 cycle
24. AI isolated secure minor
25. AI threatened major

## Balance acceptance conditions

The event is balanced enough for testing only when:

- the baseline exact-half conversion passes every integer case
- small countries remain able to recover
- major restoration requires repeated meaningful investment
- the War Support transfer cannot be reversed for profit
- Readiness cannot be farmed through repeated clicks or temporary state
- reconstruction and reintegration benefits are capped
- factory ledger, law, stockpile, division, and emergency exploit tests pass
- active war receives sensible protection without becoming a permanent deferral exploit
- repeat cycles merge safely
- save and reload produces no duplicate transaction
- performance testing shows no persistent whole-world scan
- probability evidence places AI behavior inside the target bands
- exact law and disband effects are proven against local game documentation

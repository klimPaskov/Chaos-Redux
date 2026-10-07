# 8. Death of the Firstborn

## X. One night across the world

The tenth plague resolves once at the end of Darkness.
It affects firstborn people of all ages.
It is not framed as a plague that kills only children.

For an unprepared world in its first cycle, this is the sequence's largest single direct mortality spike.
An exceptionally well-protected country can suffer fewer tenth-plague deaths than it suffered in an earlier storm.
That local success is legitimate and must not be overridden merely to force the tenth plague to rank first everywhere.

The result removes real living civilian population from affected states.
It leaves permanent demographic loss, shared Deaths records, mourning, and possible vacancies among named characters.
An organization penalty, manpower reduction, or event description cannot substitute for the population transaction.

## The firstborn cohort

The proposed initial demographic abstraction places 25% of each eligible state's living civilian population in a hidden firstborn cohort.
This is a game-balance assumption.
It is not a researched estimate of historical birth order or family structure.

The cohort is established once when a population first enters this event's accounting.
It is not rebuilt from 25% of the remaining population before every tenth plague.
Existing people already counted elsewhere must not be initialized again following migration, release, annexation, or a change of tag.
The living firstborn metadata persists after an episode closes so a later legitimate Event 085 episode cannot reclassify surviving non-firstborn people.
A new campaign can initialize its own population; an administrative reset of this metadata is a debug operation that invalidates relevant survival achievements.

The event also distinguishes full Passover protection, partial protection, no preparation, and actual coverage by a working civilian response network within this cohort.
These distinctions describe living people and their current protection.
They are not additional national resources or public progression meters.

Other civilian deaths reduce the represented living firstborn cohort consistently with the population actually removed.
When another source has no birth-order information, a documented proportional allocation is an accounting approximation, not a second mortality event.
Migration carries the surviving cohort with the people moved.
New births or genuinely new population can add new eligible people only through a proven population-source transaction.

A younger sibling does not become a firstborn person because an older sibling has died.
The system does not regenerate vulnerable people between cycles merely to maintain an enormous tenth-plague toll.

## Severity and protection

For a country with Divine Wrath `W`, the initial unprotected firstborn hazard is:

`h(W) = 0.10 + 0.85 × (W / 100)²`

The proposed tenth-plague intensity multiplier is 1.00 at baseline, 1.10 under Evolution I, and 1.25 under Evolutions II and III.
The scenario and recurrence adjustments in Parts 9 and 12 apply before the hazard ceiling.
The resulting unprotected hazard is capped at 0.95.

For each living firstborn protection cohort:

`requested deaths = living firstborn people × min(0.95, h(W) × intensity × recurrence) × preparation multiplier × network multiplier`

The preparation multiplier is 0.05 for fully reached people, 0.50 for partly reached people, and 1.00 for unreached people.
The network multiplier is 0.90 only for people actually served by the functioning earlier response network; otherwise it is 1.00.
The same person cannot enter several coverage classes.

This intentionally makes low Wrath valuable even without full preparation, while preserving the much larger protection from completing Passover.
Extreme Wrath and rejected preparation can kill a devastating share of the living population.

These are proposed tuning anchors, not engine-tested outcomes.
Population floors, actual live population, rounding, and valid source transactions determine the final applied amount.

### Illustrative arithmetic

Consider a state with 1,000,000 civilians and 250,000 living firstborn people at Wrath 50 in a baseline first cycle.
Its unprotected firstborn hazard is 0.3125.
With no preparation or network, the requested loss is 78,125 people.

With all those firstborn people fully reached by Passover, the request becomes 3,906.25 before integer settlement.
With the functioning response network also reaching all of them, it becomes 3,515.625.
An integer transaction must use a consistent rounding rule and carry or discard fractions without ever creating extra people.

These figures exclude earlier plague deaths and assume the stated live cohort still exists.
They are examples of the formula, not a campaign forecast.

## One population transaction

At the common deadline, freeze the episode, cycle, country responsibility, state, live population generation, firstborn cohort, and protection facts needed for resolution.
The actual operation may process bounded batches internally, but the result must be as if the same world deadline governed every state.
Later player choices cannot change an already frozen outcome.

The actual civilian loss is capped by the living eligible cohort and the shared protected population floor.
The public exact population-loss helper settles the population debit and Deaths entry once.
The firstborn cohort is reduced by the actual applied loss, not the larger requested loss.

For example, if a request is 20,000 but the protected floor allows only 4,000 actual deaths, population and the Deaths system change by 4,000.
The firstborn cohort also loses 4,000.
No pending remainder may later be applied without a new valid cause.

A state cannot receive the same cycle's tenth plague twice after save/load, controller transfer, late event delivery, or a repeated coordinator call.
An already settled receipt remains settled.
A queued state that ceases to exist must be reconciled to its actual surviving population responsibility, not silently discarded or applied to an unrelated replacement state.

Reports show the shared owner's applied deaths.
Requested deaths, rejected transactions, and fractional arithmetic are not public casualties.
The event may display a filtered view of its Deaths receipts, but it does not establish a competing public casualty ledger.

## Named characters

Named political leaders, heirs, generals, admirals, ministers, and other supported prominent characters can die.
Eligibility requires that the character is alive, currently valid for the relevant role or country, and actually established as firstborn.

A real person's birth order requires a reliable biographical source.
A fictional character requires explicit character metadata or approved narrative evidence.
Unknown birth order is not filled with a random guess.
No historical character eligibility has been established by this package.

A character's protection follows the verified personal or resident protection context.
The whole government is not exempt because its leader chose a national option.
Conversely, a deceased, retired, absent, duplicated, or invalid character cannot be killed again.

The character owner handles removal, role vacancies, succession, and supported replacement.
Killing a general does not delete every division they command.
Killing a leader does not automatically annex the country or invent a civil war.

Named-character deaths are represented within the demographic catastrophe rather than added as arbitrary extra civilian debits.
Any separately represented military person remains under the appropriate existing military accounting.
The implementation must prove the intended representation before counting them.

## Repeated cycles

Each cycle encounters fewer living firstborn people if earlier cycles killed them.
Higher Wrath, wider coverage, and stronger intensity can increase the hazard faced by survivors.
They cannot justify killing people who already died.

Later tenth-plague death totals can therefore decline even while the world-end becomes harder to survive.
Storms, disease, hunger, destroyed services, and lost reconstruction capacity threaten the wider surviving population between final nights.
The world-end does not need a fabricated eleventh plague or a replenished firstborn cohort to remain catastrophic.

New protected households and later genuine births matter in subsequent cycles.
Earlier Passover observance is not a permanent ritual completion for every future cycle.
Its physical networks persist where intact, while the new final warning requires a new episode-specific observance and current coverage.

## A demographic footprint that remains

After settlement, the world retains the actual smaller populations, surviving cohort records, succession changes, disrupted civilian capacity, and shared casualty history.
No mourning decision restores dead population.
No end-of-event cleanup restores a state to its pre-plague census.

The next chapter concerns whether the world is allowed to rebuild, whether one renewed sequence begins, or whether the full world-end branch takes hold.

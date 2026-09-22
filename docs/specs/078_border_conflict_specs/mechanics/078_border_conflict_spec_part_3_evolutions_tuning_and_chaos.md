# Evolution, tuning, and Chaos

## What the evolutions change

The opening configuration is established from the current Chaos value, enabled evolution settings, and current frontier availability.
A high-Chaos opening can use qualifying evolved behavior immediately.
An ongoing wave uses the shared active-evolution pacing, so crossing a threshold alone does not open a second worldwide wave.
The opening profile and subsequent applied mutations belong to that wave.

| Evolution | Chaos eligibility | New behavior |
| --- | --- | --- |
| Multiple Frontiers | 200 or more | Additional simultaneous roots against the same neighbor on independent usable fronts |
| Border Momentum | 400 or more | A victorious root can seed a capture-driven chain |
| Borders in Motion | 600 or more | All available independent fronts become eligible and enabled momentum seeds become more common |

All three evolutions are persistent capabilities of a wave once applied, subject to their individual settings remaining enabled.
The setting check happens again before any new battle starts.
An evolution does not change the declared stake or combat conditions of an existing battle.
An evolution cannot create land transfers without combat.

## Multiple Frontiers allowance

Let F be the number of independent, usable state fronts in the wave's allocation set for a particular country pair.
A front consumes both native endpoints when those endpoints cannot safely be shared.
Construct a valid disjoint set using the seeded allocation order described in the frontier specification.
Do not describe this practical selection as a mathematically maximum matching.

At baseline the pair receives one root when F is positive.
With Multiple Frontiers, the root allowance is the smaller of F and `1 + floor(F / 5)`.
This gives one root across one to four independent fronts, two across five to nine, and three across ten to fourteen.
With both Multiple Frontiers and Borders in Motion enabled, the allowance becomes F.
Zero available fronts always means zero starts.

The allowance concerns the total roots admitted for that pair in this wave.
Completing a root does not replenish its allowance.
Momentum continuations belong to their existing root and do not consume another root allowance.
They still require free native endpoints.

Existing compatible disputes from older waves consume current frontier capacity.
A new firing does not duplicate them or lower an old wave's accepted allowance retroactively.
When an active evolution raises the current wave's allowance, allocate only the additional roots that have not yet been admitted.
Previously represented pairs are reconsidered, but an evolution does not recruit a new worldwide set of neighboring pairs.
The next repeat handles new neighbor relationships.

## Momentum seed and continuation

Border Momentum gives each eligible, unseeded root's attacking victory one 25 percent seed opportunity.
The opportunity exists only when at least one valid newly opened target is available after the capture.
Borders in Motion raises this seed opportunity to 75 percent when Border Momentum is enabled.
A disabled Border Momentum setting means no seed opportunity at any Chaos value.

Once a root seeds a chain, each subsequent attacking victory continues to another valid target without another probability roll.
The chain stops on an advancing defeat, a draw or cancellation, loss of eligibility, a disabled setting, or exhaustion of valid continuation targets.
There is no arbitrary maximum number of captures.
The finite map, one-use target history, troop losses, and changing frontier provide the limits.

A newly opened target must become adjacent to the advancing country because of the latest capture.
A state that already bordered the advancing country before that capture is not a valid continuation target for that step.
The next battle uses the latest captured state as the staging endpoint.
The original opposing country must still own and control the new target.
No continuation branches into a different opponent's territory.

Do not roll the seed repeatedly while waiting for an endpoint to become available.
A successful seed that cannot complete an immediately valid start closes without a substitute reward.
No persistent retry queue keeps a chain alive until a convenient later opening appears.
The resolution may wait for the first safe engine update needed to recognize a completed transfer, but it cannot wait for a different military situation.

## Active evolution pacing

Use 90 days as the initial MTTH timing target for a newly eligible mutation in an active wave.
This is a planning parameter, not a verified mean in the installed game version.
The implementation must use the shared evolution framework and obtain its actual timing behavior through the required probability adapter.
Do not convert the value into a daily percentage by assumption.

Eligibility requires a live wave and an enabled mutation that can make an actual change.
If several mutations qualify together, apply one at a time in the order Multiple Frontiers, Border Momentum, Borders in Motion, skipping disabled or inapplicable entries.
A later tier may proceed when an earlier tier is disabled if the later tier has independent enabled behavior to change.
For example, Borders in Motion can raise Border Momentum's seed chance while Multiple Frontiers is disabled.
It cannot create simultaneous roots in that configuration.

The history record follows the successful mutation.
A failed allocation or an entirely disabled amplification is not an applied evolution.
A closed wave cannot reopen for a delayed evolution callback.
Achievement hold periods and Chaos containment checks do not keep the wave open for mutation purposes.

## Evolution settings matrix

| Multiple Frontiers | Border Momentum | Borders in Motion | Result once Chaos requirements are met |
| --- | --- | --- | --- |
| Off | Off | Off | One root per eligible pair, no chain |
| On | Off | Off | Moderate additional roots, no chain |
| Off | On | Off | One root, 25 percent seed opportunity |
| On | On | Off | Moderate additional roots, 25 percent seed opportunity |
| Off | Off | On | Baseline behavior, no applied amplification |
| On | Off | On | All independent roots, no chain |
| Off | On | On | One root, 75 percent seed opportunity |
| On | On | On | All independent roots, 75 percent seed opportunity |

The matrix describes available behavior after the relevant evolution has actually applied.
It does not override the separate Chaos thresholds or active-evolution pacing.

## Event-owned Chaos sources

Event 078 represents limited interstate fighting without a normal-war declaration.
Its custom Chaos sources therefore recognize the outbreak, broad simultaneous spread, and sustained territorial advance.
The shared systems continue to own their ordinary death, occupation, annexation, and other general consequences.
A single occurrence must not be charged twice through an event-specific adapter and a generic adapter representing the same source.

| Source | Qualifying occurrence | Change | Shared rolling guard |
| --- | --- | --- | --- |
| Outbreak | First confirmed native battle start in a wave | +5 | 30 days between Event 078 outbreak grants |
| Broad spread | At least five distinct pairs involving at least five distinct countries are actively fighting in this wave at the same time | +5 | 90 days between Event 078 broad-spread grants |
| Sustained advance | One chain in the wave records five valid captures | +5 | 90 days between Event 078 sustained-advance grants |
| Containment | A qualifying defender stops an established chain and meets the hold condition | −5 | Once per wave, against that wave's prior event-owned grant |

Each positive source pays at most once per wave even when the rolling guard would expire during that wave.
The combined positive ceiling is 15 per wave.
The three positive rolling guards are shared across countries and waves so simultaneous repeat firings cannot multiply the same packet through different country roots.
A qualifying occurrence during a closed guard produces no grant and is not stored as a payment waiting for the guard to expire.
It can still appear in the factual history of the wave.

Count successfully started, unresolved conflicts for broad spread.
Five records that ran one after another do not qualify.
Five pairs between fewer than five countries do not qualify.
Starting and immediately invalidating a failed battle does not create a qualifying active pair.

For sustained advance, count a chain's starting capture and subsequent valid captures.
A defensive retention does not count as captured land.
A state awarded twice by duplicate callbacks never contributes twice.
The fifth capture must be a current, valid Event 078 settlement against the original opponent.

## Containment reduction

The defender must win an actual defensive battle that ends an opposing chain with at least five recorded captures.
The defender must then continuously own and control that battle's disputed state for 30 days.
At confirmation the original opponent must have no active advancing Event 078 chain against that defender.
A draw, technical cancellation, normal-war cancellation, or settings shutdown does not establish containment.

The reduction belongs to the stopped chain's wave, even if that wave has already closed.
That wave must have a remaining positive Event 078 grant of at least 5.
The reduction cannot exceed what this wave actually added through its event-specific sources.
It cannot compensate for unrelated global Chaos or for a positive packet that was suppressed by a rolling guard.
The first valid containment confirmation spends the wave's one reduction allowance.

This recognizes stopping the local advance without pretending the event has undone all of its worldwide fighting.
No peace treaty, ownership reset, or diplomatic immunity accompanies the reduction.
The normal global Chaos lower bound still applies.

## Tuning intent and balance checks

The initial tuning favors broad baseline coverage over additional same-pair roots.
The mild first evolution preserves attention for countries with many neighbors.
The third evolution deliberately makes long, state-rich borders demanding.
The seed chance controls how often a captured frontier becomes a campaign, while the strict newly opened adjacency rule controls where that campaign can go.

Balance should be assessed through actual stakes, territorial loss, native army commitment, supply, and attention cost.
Do not add small combat modifiers or political-power payments simply to fill a decision menu.
Do not protect major countries through hidden weighting.
If small countries lose too easily in tests, inspect native troop selection, notice, and frontier validity before changing the declared world scope.

A change to the allowance or seed chance is a design change that must be reflected in the core specification, player tooltips, scenario matrix, and probability comparison.
The values above are starting design choices and are not claimed to have passed gameplay balance tests.

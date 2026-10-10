# 02. The year after collapse

## Continuous eligibility

The automatic route begins when the shared world state is World Collapse and Chaos becomes strictly greater than 1000. The distinction matters because the documented World Collapse tier begins at 1000, while this event's user-defined threshold excludes exactly 1000.

Record the first qualifying date and its one-year anniversary in the game's supported calendar. A full year means the same calendar date in the following year. If the installed calendar allows February 29 and the next year does not, use February 28 at the same time. The implementation must prove this date calculation instead of subtracting encoded date numbers as if they were days.

Any observed change to 1000 or less before arrival resets both the grace and the accumulated time beyond it. The next rise begins a fresh year. Pausing the game does not advance time. Saving and loading preserve the recorded dates. Disabling automatic Event 103 removes it from selection but does not rewrite how long the world has remained above the threshold.

Every shared Chaos mutation that can cross the threshold must notify this owner. A single dated owner callback supplies a recovery check. Daily sampling alone is insufficient if Chaos can fall and recover between samples, because that would falsely count an uninterrupted year.

An existing world-end latch closes the automatic route permanently for this campaign. The global Disable World End setting does not itself reset the grace. It prevents endings while enabled, so a surviving world may still produce the Directorate if Event 103 is allowed. The branch's eventual terminal request separately respects that setting.

## Availability and probability are different

At the anniversary, Event 103 becomes eligible for the ordinary major pool. It receives no free event dispatch and no replacement countdown. Disabled random events, disabled Event 103, occupied CXT carrier, invalid geography and completed episodes continue to prevent selection through normal availability handling.

The same resolver must feed pool counting, the event list, weight calculation and dispatch preflight. Before eligibility, the event list shows the framework's unavailable state and a concise reason. It must not show a positive usable weight or count the unavailable event as an active major.

### Proposed growing weight

Let `y` be uninterrupted qualifying years after the grace anniversary. Freeze `A` as the current normal event-weight anchor when grace completes. Use the existing configured baseline if one exists, with the documented normal weight of 1000 as the initial tuning reference.

The proposed relative weight is:

`W103 = A × (0.05 + 0.10y + 0.05y²)`

| Excess qualifying time | Relative weight with A = 1000 |
| --- | ---: |
| None | 50 |
| Half a year | 112.5 |
| One year | 200 |
| Two years | 450 |
| Three years | 800 |
| Five years | 1800 |

These values are relative weights, not percentages. The actual chance depends on the complete live candidate pool and all shared selection stages. The curve creates a low opening presence and increasingly serious pressure without specifying a guaranteed draw.

This owner weight replaces the generic per-minor buildup for Event 103. The event still counts as one active major once available, and a successful arrival performs the ordinary major pacing reset for the rest of the pool. Another major firing must not reset the Directorate's private excess age or lower its age-derived priority. Adding normal buildup on top would make the starting promise dependent on unrelated historical gains and would create a second competing accumulator.

Calculate the weight from elapsed time at each relevant pool evaluation. A dated recovery callback can refresh the display, but callback count never acts as time. Preserve fractional or fixed-point precision until the final engine-supported weight conversion. For extreme ages, use a numerically safe ratio representation or common pool rescaling that preserves relative weights and every other positive candidate. A hard deadline, an overflow to an exclusive candidate, and rounding all competitors to zero each violate the design.

The formula cannot create a random opportunity when the global scheduler has no opportunity. A campaign with automatic random events paused simply preserves eligibility. No private dispatcher may force Event 103 to compensate.

## Valid origin states

Selection is uniform over the complete valid state set, not uniform over countries followed by a second state draw. Large countries may therefore supply more candidate states. Validity does not favor a convenient industrial region or a weak opponent.

| Requirement | Meaning |
| --- | --- |
| Mainland location | A real, passable land state on its continent's mainland landmass |
| Native island check | The installed `is_island_state` contract must be verified and reject island states |
| Topology check | A chain of adjacent states on a multi-state offshore island must not accidentally qualify it as mainland |
| Continental identity | The state has an unambiguous installed continent classification |
| Deployment | At least one owned-and-controlled-after-transfer land province can receive the planned army legally |
| Current administration | A live non-CXT controller exists and can participate in the immediate war |
| Transfer legality | The state is not a sea zone, impassable pseudo-state or an invalid internal fixture |
| Carrier availability | CXT is dormant, unoccupied by a human, and not an active test session or existing Directorate |

Determine mainland components from the installed map, not a hand-maintained country list. Australia is the mainland anchor for Oceania. An offshore island does not become valid because it contains several states or a strait connection. An archipelagic state requires special map review if its native state classification and mainland deployment province disagree. Ambiguous candidates are excluded with a recorded geography reason until the installed-map audit resolves them.

Capital states, occupied mainland states and powerful countries remain valid. A capital seizure follows native capital relocation for the former holder. In an occupied state, remember both legal owner and actual controller. The actual controller must become an enemy. A surviving legal owner also enters the war when required to settle the ownership transfer, so the country cannot keep a peace treaty that blocks recovery of the seized state.

The chosen state fixes the origin continent for the whole episode. Moving the capital, losing the spawn state or expanding onto another continent never changes the target continent.

## One visible arrival transaction

1. Reserve one global launch request and freeze its source, candidate state, previous owner, previous controller, origin continent, intensity and world-strength snapshot.
2. Prove carrier availability, current candidate validity, setup adapters, required identities and a deployable opening package. Recheck automatic prerequisites for a natural request.
3. Prepare the clean CXT Directorate context and transfer exactly the selected state. Do not invoke the console test command, player-switch receiver, whole-country annex or foreign facility allocator.
4. Establish country identity, legal capital, opening army, stockpiles, fuel, supply support, command, active operational capacities and initial production. The visible arrival cannot precede a functioning military state.
5. Confirm the one-state result, commit this immutable episode, enroll the boss in World Threat, and declare the initial wars. Then release the arrival news and applicable major-event log and pacing effects. Preserve the automatic route's fire-once history independently of the current episode generation.

Setup is allowed to prepare data before commit. It is not allowed to display a helpless placeholder country while its promised army is still waiting for a delayed research or registry pass. Where the engine requires staged work, the implementation must demonstrate a safe provisional context and complete rollback before enabling this event in the pool.

If preflight fails, do not fire the event, consume major buildup, emit success news, add Chaos, reserve achievements or switch players. Return automatic selection to its normal failure path. A manual requester receives one plain reason. If a state becomes invalid during provisional work, restore exact ownership, control and native stockpiles affected by that work. Failed rollback remains a blocking implementation defect, not a successful partial arrival.

## Lifecycle boundaries

| Situation | Required behavior |
| --- | --- |
| Chaos equals 1000 during grace | Reset the grace |
| Chaos drops after eligibility but before arrival | Reset grace, excess age and usable weight |
| Another major fires | Preserve Directorate age and increasing owner weight |
| Event 103 is disabled | Exclude from the pool, retain environmental dates |
| No valid state exists | Stay unavailable, preserve the qualifying dates |
| CXT is being used for a test session | Stay unavailable, never overwrite the session |
| Another world end starts | Close natural arrival and this terminal branch |
| Manual request and natural draw coincide | One reservation can commit, the other has no effect |
| A committed boss later dies | Mark the episode defeated, do not restart the grace |
| Force-trigger is requested again while a boss is active or provisionally committing | Reject the collision, offer no refill or resurrection |
| The Final Boss is requested after confirmed destruction and completed cleanup | Part 09 permits a fresh manual episode with a clean available carrier and no incompatible terminal state. Automatic grace and fire-once history are not restarted |

The current catalog status follows the events skill's actual-root rule, separately from the original brief's requested planning label. Planning does not remove any existing default-disabled rework gate from a user's campaign.

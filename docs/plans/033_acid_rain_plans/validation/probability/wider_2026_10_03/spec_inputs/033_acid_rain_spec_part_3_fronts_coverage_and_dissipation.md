# Event 033 Acid Rain, Part 3, fronts, coverage, and dissipation

## Front meaning

An ordinary front has two scales:

- a current region, used for travel, warning, and broad presentation
- a moving state footprint, used for actual exposure, deaths, damage, and coverage

Selecting Europe does not apply acute rain to every European state at once. It creates one connected or island-aware footprint that drifts through European states until its visit quota and departure conditions are satisfied.

## Starting region

The first region is selected from regions with at least one frozen eligible state. Each valid region starts with equal base weight, then receives a small state-count weight so a region with many valid states is not consistently ignored. No region can be selected if its eligible count is zero.

At a higher-stage opening:

- Multiple Weather Fronts chooses two distinct starting regions, then can add a third according to the third-front roll.
- Global Acid Rain does not choose an ordinary starting region. It starts with the formation presentation, then enters the global-layer transition.

## Region visit quota

When a front enters a region, draw a quota between 60 and 85 percent of that region's frozen eligible-state count. Round up and clamp to at least three states and no more than the region total.

Quota correction rules:

- If the remaining untouched state count in the region is below the drawn quota, the quota includes every remaining untouched state.
- On the second visit to the same region, the front must include every state still untouched there before leaving.
- On later visits, any remaining untouched state is compulsory.
- A region with fewer than three eligible states uses all of them.

These rules make complete coverage achievable without removing revisits or random paths.

## Initial footprint

At region entry:

1. Select an anchor state from eligible states in the region, strongly preferring untouched states.
2. Set an active footprint target between 12 and 20 percent of the region's eligible states.
3. Clamp the target to at least two states and at most forty states per ordinary front.
4. Add the anchor and valid neighboring states until the target is reached.
5. If the connected expansion stalls, select another untouched island or disconnected anchor in the same region and continue.

The forty-state cap is a performance limit for ordinary regional fronts. A large region is covered over several drift pulses, not by an oversized first footprint.

## Drift pulse

Every six days, each front performs one drift step.

### Retire states

A state can retire when it has spent at least twelve days under the current footprint and is not required as the only bridge to a connected growth edge. Retire 20 to 40 percent of the active set, rounded down but at least one when the set is above two states.

### Add states

Fill the footprint back to its target size and add a small growth allowance when the front is intensifying. Candidate order:

1. untouched eligible neighbors of active states
2. untouched eligible states in the same region that border recently retired states
3. other untouched eligible states in the same region
4. touched neighbors needed to preserve a coherent route
5. other touched states only when no untouched state is available

Each newly active state is marked touched immediately. Mortality and damage begin on the next scheduled exposure pulse, not in the drift helper.

### Island and disconnected fallback

If no valid neighbor exists and the visit quota has not been met, create a bounded jump to one untouched state in the same region. The GUI presents this as the weather front reforming over a detached island or distant atmospheric pocket. The jump does not count as a cross-region movement.

## Region dwell window

A front receives a minimum and maximum departure date when it enters a region.

- minimum dwell: 18 to 30 days
- maximum normal dwell: 36 to 50 days
- add up to 12 days for very large regions
- subtract up to 8 days for a high-intensity front
- add up to 10 days when a forced coverage pass has many untouched states left

A front cannot leave before the minimum date. It should leave after the visit quota is satisfied and the current movement window opens. It cannot remain past the corrected maximum unless it is completing compulsory untouched states under the second-visit rule.

## Next-region warning

Seven days before a planned cross-region movement:

1. select and freeze the next region
2. mark the current front card as moving
3. show the warning overlay over the destination
4. notify countries that own or control eligible states there
5. expose the destination and arrival window in their category

The next region stays unknown before the warning date. The warning target can change only if it becomes invalid through a critical map or terminal-state change. A reroute sends one corrected warning and preserves at least three days of notice when possible.

## Region target weighting

Use integer weights that are inspectable in the probability tool. Start with weight 10 for each valid distinct candidate, then apply:

| Condition | Weight change |
| --- | --- |
| Candidate has never been visited | `+25` |
| Candidate has the highest untouched-state count | `+20` |
| More than half of candidate states remain untouched | `+15` |
| Candidate has 10 to 49 untouched states | `+10` |
| Candidate has 50 or more untouched states | `+20` |
| Candidate is the front's current region | multiply by `0.15` |
| Candidate is the front's previous region | multiply by `0.40` |
| Candidate currently hosts another ordinary front | weight `0` |
| Coverage correction has activated | only highest untouched-count candidates remain valid |

When all regions are fully touched, use the normal revisit weights only if the event has not yet dissipated.

## Coverage correction

Each cross-region move records the number of newly touched states since the previous move. If two consecutive moves produce no new state coverage, activate correction for that front. The next target must be a region with the highest remaining untouched count. Within that region, untouched candidates are compulsory until at least one new state is added.

If a front has made twelve movements and world coverage remains below 80 percent, increase its untouched-state preference and reduce immediate-repeat weights further. This is a safety correction, not a visible difficulty change.

## Multiple-front coordination

Evolution II permits two ordinary fronts and sometimes three.

Rules:

- ordinary fronts cannot occupy the same region
- destination selection excludes regions currently occupied by another ordinary front
- warning reservations prevent two fronts from selecting the same next region
- front processing order is stable by front ID
- each front owns its own state arrays, intensity, movement dates, warning, visit quota, severe-cell cooldown, and history
- a state can belong to only one ordinary front at a time
- severe cells can exist independently in separate front footprints

If only one distinct valid region remains available during a planned movement, one front waits in its current region and receives a short corrected movement window. It does not invade another front's region.

## Severe-cell location

A severe cell selects a contiguous group of three to twelve current active states. It prefers high population, low preparedness, damaged transport, and states that have not already hosted a severe cell in the current visit. It cannot select a state outside the parent front's current footprint.

The severe footprint can use the disconnected fallback only when the parent active set itself has disconnected island groups. One severe cell never spans two separate ordinary fronts.

## Global-layer transition

Evolution III closes ordinary front slots and warnings, then begins a short transition:

- transition warning: three days
- every country receives the global warning
- the GUI changes from front cards to one global-layer card
- existing severe cells end as ordinary cells
- on transition day, every frozen eligible state becomes active and touched
- the global opening-shock receipt is set only when the next exposure pulse resolves
- two initial superstorm regions are selected after the transition shock

The global phase uses the frozen eligible registry directly. It does not duplicate every state into three front arrays.

## World coverage calculation

After each new touched receipt:

`coverage = touched_state_count / eligible_state_count`

The displayed percent is rounded to one decimal place when supported, otherwise to the nearest whole percent. Completion uses exact counts, never the rounded display.

A state remains touched after:

- a front leaves
- ownership or control changes
- a civil war changes the responsible country
- local population reaches the protected Deaths-system floor
- the state becomes temporarily inaccessible to decisions

## Baseline and multiple-front dissipation

When `touched_state_count == eligible_state_count`:

1. store the final coverage date once
2. prevent the event from requiring further untouched-state targeting
3. wait at least 14 days
4. run a dissipation roll only at later movement checks

Use this chance ladder by check index:

| Check | Chance |
| --- | --- |
| 1 | 20 percent |
| 2 | 35 percent |
| 3 | 50 percent |
| 4 | 65 percent |
| 5 | 80 percent |
| 6 | 95 percent |
| 7 | guaranteed |

Failed checks schedule another check 10 to 20 days later. A check can also coincide with a normal movement, so fully covered fronts can keep moving and revisiting while the atmosphere remains active.

## Global-phase dissipation

The global phase has a minimum duration of 45 days after its transition shock. It then checks every 14 days:

| Check | Chance |
| --- | --- |
| 1 | 15 percent |
| 2 | 25 percent |
| 3 | 40 percent |
| 4 | 55 percent |
| 5 | 70 percent |
| 6 | 85 percent |
| 7 | 95 percent |
| 8 | guaranteed |

The chance can receive a small negative modifier from high current event source pressure or several active superstorms, but the guaranteed check cannot be removed.

## Dissipation transaction

A successful check:

1. sets the dissipating lock
2. blocks all new severe cells, front movements, and contamination requests
3. ends active severe cells and superstorms
4. removes acute state modifiers from tracked states
5. converts exposed states to their correct aftermath tier
6. clears front and warning arrays
7. sends the global dissipation report and national departure reports under cooldown rules
8. applies the direct Chaos reduction once
9. changes the category to recovery-tail mode
10. clears the active weather flag after all acute state cleanup receipts are valid

A load during this transaction resumes from the stored step. It never starts the event again.

## Synthetic duration check

A 10,000-run abstract movement test used seven region sizes totaling 1,050 valid states, the 60 to 85 percent quota, second-visit completion, 18 to 50 day dwell, and the accepted dissipation ladder.

| Active ordinary fronts | Median duration | 95th percentile | Maximum observed |
| --- | --- | --- | --- |
| 1 | 514 days | 581 days | 661 days |
| 2 | 315 days | 361 days | 424 days |
| 3 | 248 days | 288 days | 342 days |

No run retained an untouched state after the movement safety limit. These results are planning evidence, not an engine benchmark. Runtime testing must repeat the check against the real map registry and scripted selection weights.

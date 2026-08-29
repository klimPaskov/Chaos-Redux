# Event 033 Acid Rain, Part 7, evolutions and cluster integration

## Evolution thresholds

| Stage | Player-facing name | Earliest Chaos tier | Minimum Chaos value |
| --- | --- | --- | --- |
| Baseline | Acid Rain | Gathering Storm | 200 |
| Evolution I | Severe Storm Cells | Rising Chaos | 400 |
| Evolution II | Multiple Weather Fronts | Chaos Tier | 600 |
| Evolution III | Global Acid Rain | Totalen Chaos | 800 |

The three evolutions are cumulative. Later stages keep all lower-stage mechanics that still make sense.

## Evolution activation rules

At event formation, determine the highest stage available from current Chaos and enable every lower stage once.

If Chaos rises while the event is active:

- evaluate evolution transitions at the next safe front or phase check
- schedule a short warning and transition report
- persist the new stage once activated
- do not revert if Chaos later falls
- log the evolution once
- do not add Chaos merely because the stage became available or active

A manually changed Chaos value should follow the same safe transition rule. It must not mutate front arrays in the middle of an exposure pulse.

## Baseline behavior

Baseline uses one front. It moves through region footprints, can revisit regions, exposes states, creates aftermath, adds bounded Air Contamination, and waits for complete world coverage before dissipation checks.

Baseline can produce weak, standard, strong, or rare extreme ordinary intensity. It cannot create Severe Storm Cells before Evolution I.

## Evolution I, Severe Storm Cells

### Availability

Enable at Rising Chaos. If active-event Chaos reaches the threshold, begin severe-cell evaluation after a three-day escalation notice. If the event starts at this tier, the severe-cell system is available from the first region visit, but the first cell cannot start until at least six days after formation.

### Evaluation cadence

A front evaluates cell formation only on a six-day drift pulse when:

- no cell is active for that front
- the cell cooldown has expired
- at least three active states exist
- the front is not inside its final two days before movement
- the event is not dissipating

Suggested base chance per eligible drift pulse:

| Condition | Chance change |
| --- | --- |
| Rising Chaos baseline | 6 percent |
| Chaos is 500 or higher | `+3` percentage points |
| Front is Strong | `+4` percentage points |
| Front is Extreme | `+8` percentage points |
| More than 30 days in current region | `+3` percentage points |
| More than 45 days in current region | another `+3` percentage points |
| Previous cell in same visit | `-6` percentage points |
| First 12 event days | chance `0` |
| Final chance cap | 25 percent |

National preparation does not change atmospheric formation chance. It changes severe target weighting and consequences. This avoids the implausible result where shelters alter weather.

### Forecast and duration

- forecast lead: 3 days
- active duration: 10 to 21 days
- front cooldown after cell ends: 18 to 45 days
- ordinary maximum: one active cell per front
- global phase uses the separate superstorm capacity

### Targeting

After formation succeeds, select three to twelve active states. Weight toward:

- high population
- transport and supply importance
- weak local protection
- prior ordinary exposure
- low previous severe-cell count

A prepared country can still be targeted. Its protection lowers losses.

### Impact threshold for direct Chaos

The first severe cell creates the direct `+5` Chaos outcome only if it causes at least one accepted threshold:

- 100,000 applied civilian deaths across the cell
- 20 building damage points across the cell
- one million people exposed in countries below 30 Preparedness and a major supply disruption

Use one permanent receipt.

## Evolution II, Multiple Weather Fronts

### Availability

Enable at Chaos Tier. An active one-front event announces atmospheric splitting and performs the split seven days later. A pre-fire stage-II event forms two fronts at launch after the super-event.

### Second front

The second front is guaranteed. It chooses a region distinct from the current front and receives its own footprint, timer, intensity, warning state, severe-cell cooldown, and visit ledger.

Forming a stable second front applies the one-time direct `+10` Chaos outcome after both fronts have valid active footprints.

### Third-front roll

Roll once at stage-II activation, then again at most every sixty days while only two fronts exist.

Suggested chance:

- base 20 percent
- `+10` percentage points at Chaos 700 or higher
- `+10` when both existing fronts are Strong or Extreme
- `+10` when event age exceeds 180 days
- cap 50 percent

A third front needs a distinct valid region. A successful roll with no third region is deferred without consuming the sixty-day retry.

The first stable third front applies direct `+5` Chaos once.

### Independent records

Every front owns:

- current and previous region
- active footprint
- visit quota
- movement window
- warning target
- intensity
- severe-cell state
- movement and correction counters

A front cannot borrow another front's warning, severe cooldown, or state array.

## Evolution III, Global Acid Rain

### Availability

Enable at Totalen Chaos. An active regional event starts a three-day global warning after the current exposure pulse completes. A pre-fire stage-III event uses the formation super-event, gives every country the category, and enters the same three-day transition.

### Transition

On transition day:

- close all ordinary front and severe-cell arrays
- preserve their history and cumulative counters
- mark every frozen eligible state touched and active
- satisfy the world coverage requirement
- apply one global opening-shock receipt on the next exposure pulse
- create two initial superstorm forecasts
- switch the GUI to the global-layer model
- apply direct `+15` Chaos once

### Sustained global layer

Every valid state takes the global acute modifier and an immediate global-transition population-loss transaction. Later three-day global pulses continue to remove real state population through the same exact helper. The global operational modifier is weaker than a severe cell because it affects the entire world, but its mortality remains direct and cumulative.

### Superstorms

- minimum active capacity 1
- ordinary capacity 2
- capacity 3 after 60 global days or Chaos 900
- capacity 4 at World Collapse if the event is still active
- absolute cap 5
- forecast lead 3 days
- duration 10 to 21 days
- region or bounded state-group target

Several superstorms can exist at once, but one state cannot belong to two superstorms. Target weighting prefers regions without an active superstorm.

### Endpoint

The global phase has a 45-day minimum duration, then uses its rising fourteen-day dissipation ladder and guaranteed eighth check. Air Contamination, prior storm duration, and active superstorms can lower early chances but cannot remove the guarantee.

## Evolution history

Event Details records:

- stage name
- unlock tier
- activation date
- whether active at formation or activated later
- actor or global scope as required by the shared evolution schema

Do not create ordinary event-history rows for each severe cell, front split, or movement. These are subevents of one Event 33 firing.

## Natural Disasters cluster role

The accepted cluster currently has five logical Event 13 season slots. Event 33 becomes a sixth member. It does not replace an Event 13 slot.

### Member ordering

Accepted order:

1. Event 13 opening local season, Low
2. Event 13 additional early season, Low
3. Event 13 Wider Disaster Seasons slot, Medium
4. Event 13 Regional Cascades slot, High
5. Event 13 Abnormal Paths slot, Severe
6. Event 33 Acid Rain, Severe with later-order bias

The later-order bias ensures Acid Rain resolves after every queued Event 13 season, including the other Severe slot.

### Event 33 cluster validity

Event 33 is available to the cluster only when:

- Event 33 has not fired
- Event 33 is not active
- Event 33 is enabled in settings
- current Chaos is at least 200
- no world-end or incompatible atmospheric terminal transition blocks it
- the event can build at least one valid-state registry
- no other cluster queue has reserved Event 33

### Participation chance

| Chaos state | Optional Event 33 participation |
| --- | --- |
| Calm World | 0 percent |
| Gathering Storm | 20 percent |
| Rising Chaos | 35 percent |
| Chaos Tier | 55 percent |
| Totalen Chaos | 70 percent |
| World Collapse | 85 percent |

If Event 33 was the normal event that caused the cluster roll, it becomes required after validity passes. Other optional members keep their own rolls.

### Cluster danger and current danger

Event 33 remains Severe. Cluster danger can add a small participation modifier only through a documented constant. Suggested maximum is `+10` percentage points. Final chance remains capped at 95 percent for an optional member.

## Mixed Major pacing

The Natural Disasters cluster is normally repeatable, while Event 33 is Major. The cluster system therefore needs an effective pacing type for each prepared queue.

Rules:

1. Build and validate the complete queue before applying pacing.
2. If Event 33 is absent, keep existing Natural Disasters repeatable pacing.
3. If Event 33 is present, set the prepared queue's effective pacing type to Major.
4. Apply Major pacing once at cluster launch through the cluster path.
5. Reserve Event 33 so ordinary selection cannot fire it while queued.
6. Reset Major weights and the Major timer behavior once.
7. Event 33's later member dispatch records its own fired state and history but does not apply a second timer or Major reset.
8. Event 13 member rows remain genuine Event 13 firings with their own history and effects, but they do not add extra global pacing.

Prevalidation must prove Event 33 can initialize before the Major pacing commitment. If a terminal world change later cancels the reserved member, record a cancelled cluster result and release the reservation. Do not attempt to rewind already committed global timer history.

## Independent firing

Outside a cluster, Event 33 uses the normal Major lifecycle:

- starts at Major weight 0
- gains weight through the shared Major system
- becomes selectable only at Chaos level 2 and when valid
- fires once
- resets Major weights and Major timer state through the standard dispatcher
- removes itself from future availability

Manual debug triggering should use the repository's no-cluster path and still establish correct Major fired state unless a clearly marked test bypass is used.

## Event 13 overlap

Event 13 and Event 33 can coexist. Use these conflict rules:

- Event 13 cannot place an ordinary weather-family impact in a state currently under an Acid Rain severe cell or superstorm unless a specific compatibility test accepts it.
- Geological Event 13 families can still occur under Acid Rain.
- Event 13 aftermath and Acid Rain aftermath remain separate records, then feed shared Humanitarian pressure through deduplicated source IDs.
- Event 13 natural aerosol additions and Event 33 contamination use separate Air source accounting.
- A Natural Disasters cluster history row lists both members and their separate outcomes.

## Settings and disable behavior

Disabling Event 33 before firing removes it from ordinary and cluster availability. Disabling it while active stops future evolution transitions and new severe cells only if the shared settings contract allows active-event shutdown. It must not delete active state records or skip cleanup.

The preferred active disable behavior is a controlled early dissipation request that still clears acute state safely, records the administrative end, and preserves deaths and contamination. Implementation must match the repository's accepted settings behavior for active Major events.

# Event 033 Acid Rain, Part 8, AI, balance, and probability

## AI objective

The AI should prepare before exposure, respond to warnings, protect high-value and high-population states, preserve enough resources for war, and finish recovery. It should not spend every train or support-equipment item because a front exists on another continent.

Use native decision AI evaluation where possible. Do not create an all-country custom AI pulse.

## Threat states

Each country derives one bounded threat state from stored Event 33 data:

| Threat | Condition |
| --- | --- |
| 0, distant | No active or warned state and no active front in the country's region |
| 1, regional | A front is in the country's region or the region is a revealed destination |
| 2, exposed | At least one controlled state is actively exposed |
| 3, severe | A severe cell or superstorm warning targets a controlled state, or global layer is active |

Threat state changes refresh decision AI weights. It does not change project costs.

## Capacity behavior

| Industrial capacity | Concurrent permanent projects | Recovery operations | Evacuation cap |
| --- | --- | --- | --- |
| Fragile | 1 | 1 | 2 states |
| Limited | 1 | 1 | 2 states |
| Established | 2 | 2 | 4 states |
| Great-power | 3 | 3 | 8 states |

The global-layer extra project slot follows the player rule and must pass the same available-factory check.

## Reserve rules

Before any AI action, keep these minimum reserves unless Threat 3 allows the emergency floor:

| Resource | Normal reserve | Threat 3 emergency floor |
| --- | --- | --- |
| Civilian factories | 2 free, or 20 percent of available, whichever is higher | 1 free |
| Support equipment | 15 percent of current stockpile | 5 percent |
| Trains | 20 percent of current stockpile and at least 2 | at least 1 |
| Convoys | 15 percent of current stockpile and at least 5 | at least 3 |
| Motorized equipment | 15 percent of current stockpile | 5 percent |
| Fuel | 14 days of current estimated use when available | 5 days |
| Manpower | Do not reserve below the shared deployment safety floor | Same floor |

If the engine cannot estimate days of fuel use safely in decision AI, use stockpile bands defined in constants.

## Permanent project priorities

The AI scores the next tier of each component. Suggested base scores:

| Project | Base score |
| --- | --- |
| Shelter network | 120 |
| Protected water and food | 115 |
| Medical and protective capacity | 105 |
| Transport and infrastructure resilience | 90 |

Modifiers:

- lower current component tier, higher score
- Threat 1, `+30`
- Threat 2, `+60`
- Threat 3, `+90`
- front arrival before project completion, `-35` unless the project still helps sustained or later exposure
- country at war with severe equipment shortage, `-30`
- current component already two tiers above the lowest component, `-40`
- relevant CBRN civilian protection already strong, modest reduction to overlapping medical tier, never zero
- island-heavy country, increase water and food convoy route and evacuation planning
- several damaged railways, increase transport resilience

The AI chooses the highest payable score and respects concurrent slots.

## Urgent-action priorities

### Shelter protocols

Highest when an ordinary arrival is within seven days, active exposure exists, or a severe forecast is present. Do not activate if the modifier is already active for the full remaining exposure window.

### Emergency water and food

Highest for long expected exposure, low water and food tier, island or encircled states, and aftermath tier 2 or 3 risk.

### Medical surge

Highest after a casualty threshold, during severe forecast, or when active states have low medical tier and high population.

### Reroute transport

Highest when active states contain supply hubs, high-level rail, capital connections, or several damaged railway levels.

### Evacuation

State score uses:

- severe or superstorm forecast
- state population
- capital status
- low shelter tier
- low infrastructure
- current combat
- available transport
- expected action completion before impact

The AI should not evacuate a low-population rear state while leaving a dense capital forecast state unprotected unless the capital action is unaffordable or already active.

## Recovery priorities

AI state ordering follows aftermath tier, population, capital, supply importance, factory damage, and age. Action choice follows the state's main burden:

- rail and infrastructure damage, restore transport
- high environmental tier, decontaminate water and soil
- factory damage, repair exposed industry
- no acute or aftermath state, demobilize emergency apparatus

The AI stops new recovery spending when another front warning creates Threat 2 or 3 and essential reserves would be violated.

## Front and severe-cell AI

Weather target selection is global system logic, not country AI. Do not make a country's military strength alter whether a front arrives.

Preparation can affect severe-cell target weighting only after the atmospheric cell has formed. Suggested unpreparedness weight is modest, no more than 25 percent of total target weight. Population and current front geometry remain stronger factors.

## AI event options

Reports should use deterministic acknowledgment options unless a meaningful policy choice exists. Do not add fake choices that all lead to the same state.

Where an event asks whether to fund an emergency action, AI choice weight must call the same affordability and threat helpers as the decision category.

## Probability inspection requirements

Use the repository probability inspection tool and `chaosx_ai_probability_auditor` for:

- first-region selection
- next-region selection at each coverage state
- severe-cell formation chance
- severe-cell state targeting
- third-front roll
- global superstorm targeting
- cluster participation by Chaos tier
- AI project selection by threat and capacity
- AI evacuation target selection
- dissipation chance ladders

For each inspection, record normalized outcomes and unreachable branches. A weighted list that relies on negative or zero accidental weights fails review.

## Synthetic coverage test

Run at least 10,000 abstract campaigns for each active-front count using the real constants and map region counts.

Acceptance:

- zero coverage softlocks
- every valid state touched before the safety movement limit
- one-front median between 400 and 650 days
- two-front median between 240 and 420 days
- three-front median between 180 and 340 days
- guaranteed dissipation boundary always reached

The planning prototype produced medians of 514, 315, and 248 days for one, two, and three fronts.

## Synthetic mortality and population-mutation test

For every test case, record pre-pulse state population, requested deaths, applied deaths, post-pulse state population, protected floor, Deaths entry, and Event 33 totals. The case passes only when post-pulse population equals pre-pulse population minus applied deaths and every total uses that same applied amount. A modifier-only result is a failure.

Test these state populations:

- 10,000
- 100,000
- 1,000,000
- 10,000,000
- 50,000,000

For each, cross:

- Preparedness 0, 25, 50, 75, 100
- Weak, Standard, Strong, Extreme intensity
- ordinary, severe, global, superstorm exposure
- peace, war, occupation, supply isolation
- short, median, and maximum ordinary durations

Acceptance:

- no negative or fractional applied population
- protected population floor always respected
- opening receipt never repeats in one episode
- full preparation materially lowers losses
- severe exposure remains dangerous at full preparation
- ordinary baseline does not remove extreme portions of a state in days
- episode safety caps cannot be bypassed by load or front drift

## Synthetic Air Contamination test

For at least 10,000 randomized sequences:

1. randomize global contamination from 0 to 6000 bp
2. apply formation and weekly Event 33 requests
3. add and remove other-system contamination between requests
4. verify actual Event 33 additions

Acceptance:

- Event 33 lifetime added never exceeds 1500 bp
- Event 33 never applies a positive delta that would take global contamination above 5000 bp
- when global contamination is already 5000 bp or higher, Event 33 adds zero
- other systems can later take the total above 5000 bp
- the sum of actual Event 33 deltas equals the lifetime counter
- reload does not reset the allowance

The planning prototype produced no cap violation in 10,000 randomized sequences.

## Synthetic AI affordability test

The planning prototype used four capacity bands, tiered project costs, stockpile variation from 60 to 140 percent of representative values, and arrival deadlines from 30 to 360 days.

Representative median Preparedness by arrival:

| Time before exposure | Fragile | Limited | Established | Great-power |
| --- | --- | --- | --- | --- |
| 30 days | 13.75 | 13.75 | 25 | 25 |
| 90 days | 18.75 | 25 | 50 | 63.75 |
| 180 days | 18.75 | 45 | 82.5 | 100 |
| 360 days | 18.75 | 45 | 88.75 | 100 |

This spread is intentional. Small countries need emergency actions and cannot match a fully mobilized great power. Runtime tests must verify that fragile countries still have at least one payable project and one payable urgent route.

## Balance levers

Centralize these values:

- region visit quota range
- footprint target range and cap
- dwell windows
- warning lead
- severe-cell chance, duration, and cooldown
- third-front chance
- global minimum duration and dissipation ladder
- all mortality base rates and caps
- vulnerability and protection caps
- damage pressure bands
- aftermath thresholds
- project base costs, tier multipliers, and durations
- urgent and recovery costs
- direct Chaos outcomes
- cluster participation by tier
- Air Contamination request buckets and hard caps

Do not hide balance numbers in event options or GUI scripts.

## AI acceptance cases

At minimum, prove:

- fragile peaceful minor before distant front
- fragile minor under active invasion
- island country with convoy shortage
- landlocked country with no convoys
- established country with two simultaneous warnings
- major at war with low support equipment
- major in global layer with several severe forecasts
- occupied state whose controller changes during evacuation
- country with strong CBRN civilian protection
- country with no aftermath but unfinished preparation project at dissipation

The full case matrix is in `matrices/033_acid_rain_ai_acceptance_matrix.md`.

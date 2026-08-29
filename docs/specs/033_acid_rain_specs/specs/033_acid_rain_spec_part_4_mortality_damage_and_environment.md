# Event 033 Acid Rain, Part 4, mortality, damage, and environment

## Fictional hazard premise

Event 33 is an anomalous and potentially supernatural weather system. Its rain and aerosol are directly lethal. The event does not need a real-world chemical explanation or a measured pH. Research on acid deposition and corrosive exposure informs water damage, soil damage, respiratory harm, corrosion, shelters, protective equipment, and visual presentation. It does not limit how dangerous the anomaly can become.

The four linked hazards are:

- lethal corrosive liquid exposure
- concentrated acid aerosol and respiratory injury
- poisoned food, reservoirs, and water distribution
- repeated corrosion and collapse of transport, power, medical, and industrial systems

Final text should show deaths, burns, respiratory injury, poisoned water, sheltering, and infrastructure failure while keeping the origin uncertain.

## Hard population-loss requirement

Mortality is not a display-only statistic. Each positive Event 33 mortality result must remove the same number of civilians from the affected state's real population. The implementation must use `apply_exact_state_civilian_population_loss`. A `local_manpower` penalty, recruitable-population factor, generic manpower debit, unit attrition, casualty variable, or Event 33 counter by itself does not kill state population and fails this specification.

The authoritative value is `state_civilian_population_loss_applied`, returned by the shared helper after the protected floor and all caps. State, country, global, report, achievement, and Deaths totals must use that returned value and no other estimate.

## Mortality timing

Mortality resolves on the three-day exposure pulse. Each exposure episode has two stages:

1. one opening shock when the episode first resolves
2. one sustained amount on each later pulse while exposure continues

Ordinary, severe-cell, global-transition, global-sustained, and superstorm exposure use separate receipts. A state cannot receive the same opening shock twice for one episode.

## Base rates

Rates are requested civilian population losses per one million current state civilian population before multipliers. After the helper runs, only the applied loss counts as deaths.

| Exposure | Opening deaths per million | Sustained deaths per million every 3 days |
| --- | --- | --- |
| Ordinary front | 400 | 65 |
| Severe storm cell | 1,500 | 350 |
| Global transition | 700 | Uses global sustained after opening |
| Global layer | None after transition | 110 |
| Global superstorm | 1,500 | 350 |

These are starting balance values in script constants.

## Exact calculation

For each applicable stage:

`raw deaths = population in millions × base rate × intensity × local vulnerability × wartime exposure × protection`

Round only after all factors and caps are applied. Call `apply_exact_state_civilian_population_loss` with the shared protected population floor. Read the returned applied loss, then verify that the state's real civilian population fell by that amount before committing Event 33 totals and reports.

### Intensity multiplier

| Qualitative intensity | Multiplier |
| --- | --- |
| Weak | 0.80 to 0.95 |
| Standard | 0.96 to 1.15 |
| Strong | 1.16 to 1.35 |
| Extreme | 1.36 to 1.55 |

The exact value is stored with the front or severe cell. The GUI shows only the qualitative band.

### Local vulnerability

Build one bounded multiplier from observable state conditions:

- low infrastructure
- damaged infrastructure or rail
- supply isolation
- high devastation
- active occupation or contested control
- exposed dense population
- unresolved environmental aftermath
- prior severe exposure during the same event

Clamp the combined local vulnerability between `0.85` and `1.60`. No individual condition should multiply the total without this cap.

### Wartime exposure

| Condition | Multiplier direction |
| --- | --- |
| Country at peace and state supplied | 1.00 |
| Country at war | up to 1.10 |
| State under occupation | up to 1.15 |
| Active combat or severe supply isolation | up to 1.20 |
| Combined wartime multiplier cap | 1.35 |

Wartime exposure is separate from local vulnerability only so the AI and reports can explain why a state performed poorly. The combined formula still receives the final mortality caps below.

## Protection multiplier

National Preparedness gives a linear mortality multiplier:

`1.00 - 0.0068 × Preparedness`

This gives `1.00` at 0 Preparedness and `0.32` at 100 Preparedness.

Then apply component-specific and local adjustments:

- shelter tier has the strongest effect on opening shocks
- medical and protective tier has the strongest effect on sustained mortality
- protected water and food lowers sustained mortality after twelve days of exposure
- transport resilience improves evacuation and severe-cell response
- active local evacuation lowers severe-cell and superstorm mortality
- compatible CBRN civilian protection can lower both stages through the shared protection interface

Final protection floors:

| Exposure | Lowest allowed protection multiplier |
| --- | --- |
| Ordinary front | 0.25 |
| Global ordinary layer | 0.25 |
| Severe cell | 0.35 |
| Global superstorm | 0.40 |

Even complete preparation cannot make a severe cell harmless.

## Pulse caps

Use current state population at the moment of the pulse.

| Exposure | Per-state cap |
| --- | --- |
| Ordinary opening | 0.15 percent |
| Ordinary sustained pulse | 0.02 percent |
| Severe opening | 0.50 percent |
| Severe sustained pulse | 0.08 percent |
| Global transition opening | 0.25 percent |
| Global sustained pulse | 0.03 percent |
| Superstorm opening | 0.50 percent |
| Superstorm sustained pulse | 0.08 percent |

Episode cumulative safety caps:

- ordinary visit episode, 1.5 percent
- severe-cell episode, 4 percent
- complete global phase, 8 percent

The cumulative cap is a safety boundary. Normal balance should remain well below it.

## Prevented-death estimate

For reports and achievements, calculate the same pulse once with protection fixed at `1.00`, without applying population loss. The difference between that unprotected estimate and actual applied deaths becomes the prevented-death estimate. Clamp it to zero or higher and add it to country and global counters.

This estimate is a gameplay statistic. It must be labeled as an estimate and never alter the Deaths system.

## Deaths-system integration

Every actual civilian loss:

1. records the exact requested loss after caps
2. records the state's pre-pulse civilian population
3. calls `apply_exact_state_civilian_population_loss`
4. uses `state_civilian_population_loss_applied` returned by that helper
5. verifies that post-pulse civilian population equals pre-pulse population minus the applied value, subject to the protected floor
6. registers the applied value once under the accepted natural-disaster or dedicated Acid Rain cause
7. increments Event 33 state, country, and global counters with the same applied value
8. stores responsible country, pulse key, and date for history
9. emits no death report or threshold progress when the applied value is zero

Do not add separate Chaos for the same casualties. The shared Deaths system handles its normal one-Chaos-per-million progression.

A dedicated Acid Rain cause is preferable if the Deaths UI can accept one more cause without breaking its fixed layout. Otherwise use the existing natural-disaster cause and add Event 33 attribution in the event history. This choice must be made during implementation inspection, not guessed in localization.

## Casualty report thresholds

Each country can receive report events at these cumulative Event 33 thresholds:

- first 10,000 deaths
- first 100,000 deaths
- first 1,000,000 deaths
- each later full 5,000,000 deaths

Use a minimum thirty-day cooldown between threshold reports. A severe-cell forecast and impact report can still occur during the cooldown because it serves a different purpose.

## Building damage pressure

Avoid an independent random damage roll against every building on every pulse. Each state stores a fractional damage-pressure value.

Per three-day pulse, add:

| Exposure | Pressure points |
| --- | --- |
| Weak ordinary | 0.4 to 0.9 |
| Standard ordinary | 0.8 to 1.5 |
| Strong ordinary | 1.3 to 2.2 |
| Extreme ordinary | 1.8 to 3.0 |
| Severe cell | 4.0 to 8.0 |
| Global layer | 0.8 to 2.0 |
| Global superstorm | 6.0 to 12.0 |

National infrastructure resilience, local evacuation, and CBRN civil protection reduce pressure. The final damage protection floor is `0.35`.

Whenever the accumulator reaches one whole point, spend whole points through the building target table and keep the remainder. Cap points spent in one state on one pulse at the upper end of its exposure band.

## Building target table

| Target | Ordinary weight | Severe or superstorm weight | Rule |
| --- | --- | --- | --- |
| Infrastructure | High | High | Main corrosion target |
| Railway | High | Very high | Damage only existing levels |
| Civilian factory | Medium | High | Prefer exposed industrial states |
| Military factory | Medium | High | Prefer exposed industrial states |
| Air base | Medium | High | Represents runway and equipment exposure |
| Naval base | Low | Medium | Coastal states only |
| Dockyard | Low | Medium | Coastal industrial states only |
| Anti-air or radar | Low | Medium | Secondary exposed installations |

Do not directly delete supply hubs through ordinary pressure. Use acute supply penalties, rail damage, and infrastructure damage. A later engine-tested severe-only supply-hub damage route requires an explicit repair and softlock proof before acceptance.

Permanent resource deposits are not deleted. Environmental aftermath can reduce local resource extraction temporarily.

## Acute state modifiers

Use mutually exclusive modifier bands selected from current exposure:

### Ordinary rain

- lower local supply throughput
- slower movement
- lower construction and repair speed
- lower organization regain
- small attrition increase
- weaker air operations and sortie efficiency
- local resource extraction penalty

### Strong ordinary rain

The same families at larger values, with meaningful railway and factory pressure.

### Severe cell

- large supply and movement penalties
- stronger attrition and organization penalties
- stronger construction and repair penalties
- substantial air operation penalty
- higher building-pressure rate
- severe local casualty multiplier

### Global layer

A moderate worldwide band. It must be lower than severe-cell values because every valid state is active.

### Global superstorm

The strongest temporary band, limited to selected regions or state groups.

All values live in constants. The modifier descriptions should show broad effects and current intensity without exposing every hidden multiplier.

## Military treatment

Event 33 is a civilian and infrastructure disaster. It should affect military operations through attrition, movement, organization regain, supply, air operations, and repair. It should not directly delete divisions through an opaque event effect.

Units in severe or superstorm states can take higher attrition. Protective equipment or CBRN-trained formations can reduce that penalty if the existing system exposes a safe division-level modifier. Implementation must use a documented shared interface and avoid per-unit scripted loops.

## Environmental aftermath

When acute rain leaves, calculate one aftermath tier from:

- cumulative exposure days
- highest intensity
- severe-cell or superstorm history
- building damage points
- local water and food protection
- existing disaster aftermath
- unresolved infrastructure damage

| Tier | Direction |
| --- | --- |
| 0 | No persistent aftermath |
| 1 | Local cleanup, small supply, repair, construction, and resource penalties |
| 2 | Serious water, soil, transport, and industrial cleanup burden |
| 3 | Severe corrosion and contamination, strong recovery penalties and humanitarian pressure |

Aftermath never causes the acute opening shock again. It can create a much smaller delayed mortality burden only through a clearly documented water, food, disease, or humanitarian integration. Any such death still uses the shared Deaths path and carries its own deduplication receipt.

## Humanitarian pressure

A state at aftermath tier 2 or 3 registers disaster and infrastructure pressure through the existing Humanitarian system interface. Tier 3 can also register contaminated-water or displacement pressure when its actual local conditions qualify. Event 33 does not copy the Humanitarian system's refugee, famine, or aid logic.

## Recovery effects

National recovery decisions lower aftermath one tier at a time, repair or speed repair of the relevant building class, and reduce the state's Humanitarian pressure. Vanilla repair continues normally. Event decisions accelerate recovery and prevent secondary consequences. They do not recreate buildings above pre-event maximum levels.

## Synthetic mortality check

Using intensity `1.20`, local and wartime vulnerability combined at `1.15`, and representative durations produced these approximate state-population losses:

| Preparedness | 35-day ordinary visit | 15-day severe cell | 90-day global layer |
| --- | --- | --- | --- |
| 0 | 0.163 percent | 0.448 percent | 0.552 percent |
| 50 | 0.107 percent | 0.296 percent | 0.364 percent |
| 100 | 0.052 percent | 0.179 percent | 0.177 percent |

A high-intensity, high-vulnerability 50-day ordinary visit remained near 0.37 percent at zero Preparedness in the abstract test. A 120-day global phase remained near 1.27 percent before cumulative safety caps. These results show material protection without removing danger. Real map tests must verify total deaths, small-state behavior, repeated visits, and the protected population floor.

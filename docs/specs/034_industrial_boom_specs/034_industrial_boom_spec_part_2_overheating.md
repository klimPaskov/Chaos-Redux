# Industrial Boom specification, part 2: Overheating

## The public value

`Overheating` is the only persistent numeric value the player must manage during Industrial Boom. It compresses many pressures into one readable risk state:

- Material shortage.
- Transport and supply congestion.
- Fuel pressure.
- Credit expansion and speculative investment.
- Price instability.
- Labor shortage and exhaustion.
- Maintenance debt.
- Construction congestion.
- Dependence on vulnerable industrial regions.
- The inability to convert emergency output into sustainable capacity.

The value uses a 0 to 100 range. Zero means the boom is operating with substantial spare capacity. One hundred means the extraordinary system has failed and the Event 35 handoff begins.

The value should never be presented as a moral judgment or a generic economic score. It answers one gameplay question: how close is the boom to losing control?

## Player-facing presentation

The decision category header should show:

- Current Overheating as an integer.
- Current threshold band.
- Current trend.
- The next threshold and its visible consequence.
- Up to three strongest actionable causes.
- Current landing forecast when landing preparation is available.

The player should not see a long component ledger. Cause display should use short, qualitative lines such as strained rail network, secure material access, or speculative projects active. A tooltip may explain the main drivers in more detail, but it should not expose every internal weight.

### Trend states

The trend uses five states:

| Trend | Meaning | Player expectation |
| --- | --- | --- |
| Falling quickly | Recent relief and structural control exceed current pressure | A landing window may be forming |
| Falling | Pressure is declining | Current policies are working |
| Stable | Gains and losses are close | A shock can change direction quickly |
| Rising | Current expansion exceeds sustainable capacity | Stabilization is becoming important |
| Rising quickly | Several strong pressures or one severe shock are active | Immediate action is needed |

The trend is based on recent evaluated change, not on a prediction that ignores future incidents. A stable label should not imply immunity from a blockade, state loss, disaster, or player action.

## Threshold bands

The tuning anchors below use a 0 to 100 scale. Final values may move modestly after probability and balance testing, but the band structure should remain.

| Range | Working status | Mechanical identity | Main player response |
| ---: | --- | --- | --- |
| 0 to 24 | Sustainable surge | Full ordinary boom benefit, low incident severity, best project conversion | Build structure or exploit output |
| 25 to 44 | Stretched capacity | Full benefit with mild pressure, more visible shortages, projects remain efficient | Add reserves and supply support |
| 45 to 64 | Visible strain | Part of the bonus begins to erode, incidents become material, landing preparation becomes urgent | Stabilize and stop avoidable shocks |
| 65 to 79 | Dangerous imbalance | Stronger bonus erosion, project fragility, emergency actions unlock, aggressive decisions become inefficient | Cool the economy or accept major risk |
| 80 to 94 | Pre-crash | Severe volatility, forced-landing tools, high chance of project loss and state disruption | End the boom or take a deliberate gamble |
| 95 to 99 | Terminal instability | Ordinary expansion actions close, only emergency management and landing remain | Prevent the final threshold |
| 100 | Collapse | Event 34 ends and Event 35 inherits the frozen crisis snapshot | Manage the depression |

### Threshold entry behavior

Crossing a threshold should change play, not merely recolor a number.

- Entering Stretched Capacity increases the frequency of light shortage and labor reports.
- Entering Visible Strain reduces part of the temporary bonus and unlocks stronger stabilization options.
- Entering Dangerous Imbalance blocks ordinary project designation, increases state fragility, and enables emergency liquidation or shutdown actions.
- Entering Pre-crash begins a bounded emergency objective and narrows the visible action set.
- Entering Terminal Instability closes every action that can add voluntary pressure.
- Reaching Collapse performs the Event 35 handoff immediately after the current transaction resolves.

Dropping below a threshold removes the associated pressure effects after a short confirmation period. This prevents repeated one-day crossings from causing modifier churn and incident farming.

## Starting range

A normal baseline firing should usually begin between 10 and 20. A robust country may start lower. A fragile country may start near 25. Evolved openings begin higher but should still provide a short benefit window.

Suggested opening bands:

| Opening | Normal start | Fragile start | Purpose |
| --- | ---: | ---: | --- |
| Baseline | 10 to 20 | 20 to 30 | Substantial time before danger |
| Evolution I | 20 to 30 | 30 to 40 | Stronger gain with immediate speculative pressure |
| Evolution II | 25 to 35 | 35 to 45 | Miracle projects begin before full stability exists |
| Evolution III | 35 to 45 | 45 to 55 | Runaway expansion demands active management from the opening |

The implementation should derive the exact start from country condition. These ranges are outcome goals, not a random roll independent of the economy.

## Hidden pressure model

Overheating changes through a periodic event-owned evaluation and through immediate actions or shocks. The event should process only active Event 34 countries. It does not justify a recurring scan of every country in the world.

The hidden model can use many contributors because the player sees only the total and strongest causes.

### Base expansion pressure

Every active boom creates pressure over time. The rate rises with evolution level and aggressive temporary modifiers. It falls when the economy enters a controlled landing.

The monthly equivalent should produce these broad outcomes before player action:

- Baseline target with sound logistics reaches Visible Strain after several months, not several weeks.
- Baseline target with severe supply problems can reach danger within one season.
- Evolution I requires active management within a few months.
- Evolution II can become dangerous quickly when Miracle Regions are expanded without support.
- Evolution III can reach terminal pressure within one major production campaign when ignored.

### Industrial utilization

Utilization pressure reflects how much of the extraordinary capacity is being forced into immediate output.

It rises through:

- Run the Economy Hot.
- Large active construction programs.
- Rapid addition of production lines.
- Wartime emergency production.
- Evolution-specific maximum-output choices.

It falls through:

- Cooling.
- Project suspension.
- Controlled landing.
- Voluntary output sacrifice.

The game does not need to inspect every production-line slider. A country-level approximation based on factories, modifiers, decisions, and strategic state is adequate when it produces readable behavior.

### Supply and transport pressure

Supply pressure can use:

- Train and truck availability.
- Fuel ratio.
- Convoy availability for maritime economies.
- Port and rail damage in Industrial Regions.
- Infrastructure quality.
- Access from Industrial Regions to the capital or supply network.
- Trade access and import dependence.
- Blockade or convoy losses.

Supply pressure should distinguish a self-sufficient land economy from an import-dependent maritime economy. Both can overheat, but their stabilization costs and vulnerabilities differ.

### Material pressure

Material pressure reflects the ability to feed the expanding factories.

It can rise with:

- Resource deficits.
- Lost resource states.
- Embargo or trade isolation.
- Convoy shortage.
- Rapid factory growth without matching extraction or imports.
- Evolution II and III projects that consume abnormal quantities.

It can fall with:

- Resource access.
- Stable trade.
- Recycling and synthetic production.
- Event-owned resource relief from compatible systems.
- Project choices that improve efficiency instead of raw scale.

### Infrastructure pressure

Infrastructure pressure rises when industrial capacity grows faster than railways, ports, power, housing, and local transport.

It should consider:

- Concentration of industry.
- Average infrastructure in Industrial Regions.
- Railway and supply connections.
- State damage.
- Number of active regional projects.
- Industrial spread into low-capacity neighboring states under Evolution III.

High infrastructure can slow drift. It should not make the boom risk-free because labor, materials, credit, and maintenance can still fail.

### Labor and social pressure

Labor pressure remains hidden and should not become a separate unemployment or exhaustion meter.

It rises with:

- Low available manpower relative to industry.
- Mobilization that removes workers from the civilian economy.
- Multiple shifts and aggressive output decisions.
- Rapid population movement into Industrial Regions.
- Low stability.
- Industrial accidents.

It falls with:

- Cooling.
- Better production practices.
- Stable domestic conditions.
- Completed regional support projects.
- A controlled transition away from emergency shifts.

Labor pressure can create local incidents and stability effects. It should not remove military manpower directly merely because civilian labor is scarce.

### Financial and speculative pressure

Financial pressure exists at baseline in a mild form and becomes central under Evolution I.

It rises with:

- Repeated aggressive pushes.
- Speculative incidents.
- Expansion of projects that lack material support.
- Low stability.
- A recent failed project.
- An earlier Event 34 crash.

It falls with:

- Project liquidation.
- Credit restraint represented by cooling.
- Reserves.
- A controlled landing.

The player should understand speculative pressure through reports and the main Overheating cause list. A separate debt value would exceed the mechanic's needs.

### Maintenance pressure

Maintenance debt is a delayed cost of continuous operation.

It rises with:

- Long time at high Overheating.
- Run the Economy Hot.
- Damaged or converted factories.
- Inexperienced rapid expansion.
- Repeated state incidents.
- Evolution III spread.

It falls with:

- Cooling.
- Reserve construction.
- Protected-region projects.
- Repair capacity.
- A successful landing.

Maintenance pressure should create delayed failures. Avoid an immediate penalty every time the player gains output.

## Immediate actions and shocks

Periodic drift creates the baseline arc. Important actions and world events also change Overheating immediately.

### Voluntary pressure increases

- Running the economy hot.
- Accepting an aggressive speculative project.
- Expanding a Miracle Region before its logistics are ready.
- Spreading industry into a neighboring state under Evolution III.
- Refusing a necessary shutdown after a major accident.

### Voluntary relief

- Stabilizing supply chains.
- Building reserves.
- Cooling the expansion.
- Liquidating speculative projects.
- Suspending a fragile state project.
- Beginning controlled landing.

### External shocks

- Loss of an Industrial Region.
- Heavy bombing or infrastructure damage in a key region.
- A natural disaster in an active project state.
- Blockade or severe convoy disruption.
- Fuel collapse.
- Sudden trade loss.
- A major state control change.
- A compatible event-owned economic shock.

External shocks should scale with actual exposure. A destroyed port matters more to an import-dependent country. Loss of a state matters more when it contains a Miracle Region and a large share of national industry.

## Shock absorption

Industrial Reserves and protected regions reduce the effect of shocks.

Reserve status is qualitative and bounded:

| Status | Meaning | Effect |
| --- | --- | --- |
| None | No deliberate spare capacity | Full shock applies |
| Limited | One reserve program completed | Absorbs part of the next moderate shock or improves landing |
| Strong | Several compatible reserve investments completed within the cap | Absorbs a severe shock, improves landing, and lowers inherited depression severity |
| Depleted | A reserve was consumed recently | Cannot absorb another shock until rebuilt |

Reserve status does not become a freely accumulating currency. It is consumed by major shocks or by the landing transition. The player sees the status and broad purpose, not a large numeric stock.

Protected Industrial Regions reduce local shock contribution. Protection should cover infrastructure redundancy, fire control, repair stores, transport alternatives, dispersal, civil defense, and priority access to materials. It does not make the state immune to conquest, bombing, disaster, or supply loss.

## Incidents

Incidents make the value feel connected to the world. They should be sparse, state-linked when possible, and sensitive to current causes.

### Light incidents

Likely in Stretched Capacity and above:

- Rail congestion delays deliveries.
- A factory complex reports tool and spare-part shortages.
- Housing and local services fall behind worker arrivals.
- A ministry must choose between military and civilian orders.
- A resource shipment is diverted to a priority region.

Light incidents mostly adjust trend, project progress, or temporary state modifiers. They should not become repetitive popup spam.

### Serious incidents

Likely in Visible Strain and above:

- A major plant accident interrupts production.
- A rail junction or port reaches operational saturation.
- A speculative development fails and leaves unfinished construction.
- A labor dispute threatens an important region.
- Maintenance failures damage production efficiency.
- Emergency imports consume convoys and fuel.

Serious incidents should offer a small set of clear responses with different costs. They can appear as reports, timed missions, or temporary decisions according to the action needed.

### Critical incidents

Likely in Dangerous Imbalance and above:

- A major Industrial Region partially shuts down.
- Several projects compete for the same materials and one must be cancelled.
- A credit panic causes firms to halt work.
- A transport breakdown isolates a region.
- A severe accident damages factories or infrastructure.
- Uncontrolled expansion pushes a state project toward collapse.

Critical incidents should materially change Overheating and landing quality. They remain bounded so a single random incident cannot erase a well-managed campaign without prior vulnerability.

### Incident selection rules

Incident chance and severity should consider:

- Current threshold band.
- Trend.
- Dominant hidden causes.
- Active evolution.
- Region protection.
- Reserve status.
- Recent incidents.
- War state.
- State validity.

The same incident should not repeat in the same state while its previous consequence is active. A recent-incident memory should reduce repetition and keep the event from feeling scripted.

## Feedback and readability

Every player action that changes Overheating should state:

- Immediate expected direction.
- Main cost.
- Duration or cooldown.
- The visible tradeoff in output, construction, stability, or project progress.
- Any important state target.

The player does not need a precise promise when an outcome depends on changing conditions. A decision can say that relief scales with logistics and current disruption. The tooltip should identify the factors that improve or weaken it.

Every threshold entry report should explain what physically changed. It should not merely announce that the meter crossed a number.

## Pacing goals

The event should support several viable durations:

- A short wartime exploitation can last one production season and end in a rough or forced landing.
- A balanced baseline boom can last roughly half a year to a year depending on management and shocks.
- A carefully stabilized boom can last longer while converting projects into legacy.
- Evolution III should be shorter and more volatile unless the player invests heavily in control.

These are campaign-feel targets. The event remains dynamic and should not end on a fixed calendar date.

## Overheating success and failure tests

The mechanic passes when:

- The value rises for understandable reasons.
- Strong logistics slow pressure without eliminating it.
- Aggressive output decisions are worthwhile in some wars.
- Cooling has a real opportunity cost.
- External shocks matter in proportion to exposure.
- The value can recover from danger through timely action.
- A country can still fail after poor preparation.
- The player never needs to track a second numeric crisis value.

The mechanic fails when:

- Overheating is only a timer in disguise.
- One cheap decision can reset it repeatedly.
- The strongest output route is always correct.
- The safest route preserves the same reward as the risky route.
- Random incidents determine the result regardless of preparation.
- A large major and a small player country pay the same costs.
- High pressure leaves the full positive modifier untouched indefinitely.

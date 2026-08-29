# Great Depression 2.0 specification, part 2: Depression Severity

## Public mechanic

`Depression Severity` is the only persistent event-specific number the player must manage. It uses a `0` to `100` scale. The category shows the current value, a named band, a qualitative trend, the next threshold, and up to three material causes. It does not expose the hidden component ledger or require the player to track separate unemployment, banking, demand, trade, confidence, and fiscal meters.

The value measures the country's ability to keep production, construction, employment, credit, trade, transport, and public confidence working at the same time. A low value means the economy has regained ordinary coordination. A high value means firms cannot obtain orders or finance, workers cannot find employment, public authorities cannot support every failing sector, and industrial regions are becoming disconnected from national recovery.

## Initial tuning scale

| Severity | Working band label | Player-facing meaning | Main gameplay change |
| ---: | --- | --- | --- |
| `0-14` | Recovery Floor | Ordinary coordination has returned, but the recovery still needs proof | Final recovery mission becomes possible |
| `15-29` | Stabilizing Economy | Output and confidence are returning while the country remains vulnerable | Harshest penalties continue to weaken |
| `30-49` | Fragile Economy | Growth is possible, yet closures and unemployment can return after a shock | Stabilization progress can be lost |
| `50-69` | Depression | Persistent contraction defines national planning | Full baseline decision loop is active |
| `70-84` | Deep Depression | Credit, demand, freight, and employment failures reinforce each other | Stronger national and state penalties apply |
| `85-99` | Systemic Breakdown | The state cannot protect every region or institution | Emergency actions and severe incidents become eligible |
| `100` | Economic Paralysis | National economic coordination has reached its worst supported state | A guarded maximum-Severity emergency begins |

These bands are initial design targets. The implementation should centralize them in Event 35 script constants and tune them through scenario comparison. Their ordering and gameplay meaning are fixed. Small numeric adjustments are allowed when testing proves that phase transitions occur too quickly or that a crippled country lacks a viable recovery path.

## Severity is distinct from phase

The four baseline phases and the seven Severity bands serve different purposes.

- The phase records where the country is in the event lifecycle.
- The Severity band records how damaged the economy is now.
- Panic and Contraction can begin at several high bands.
- The Depression phase can continue after Severity first falls below `50` because stabilization must be sustained.
- Stabilization can relapse into Depression.
- Recovery requires a low Severity band plus state and mission proof.

A phase change therefore cannot be inferred from one value check. The country must satisfy duration, mission, and state conditions as well.

## Hidden component model

The simulation may track the following internal components. They are hidden inputs and must not become additional player-facing counters.

### Credit and banking stress

Represents bank closures, frozen lending, capital flight, deposit fear, failed refinancing, distressed public debt, and the inability of firms to finance payroll or working capital.

It rises through:

- Banking or credit incidents.
- Repeated policy reversals.
- High instability.
- Evolution I exposure to another failing economy.
- A failed finance mission.
- Loss of a major commercial center.
- Unfunded rescue commitments.

It falls through:

- A successful banking audit or temporary bank holiday.
- Deposit or credit guarantees that the country can sustain.
- Recapitalization of viable institutions.
- A credible debt standstill or restructuring path.
- Foreign credit support.
- Sustained low Severity without a new panic.

### Demand and employment stress

Represents cancelled orders, falling household purchases, unemployment, inventory liquidation, falling wages, and idle plants.

It rises through:

- Shuttered Depression Centers.
- Austerity or liquidation without a compensating recovery source.
- Postwar demobilization when the economy relied on military orders.
- Failed public works or employment missions.
- Severe trade contraction.
- Long exposure to high Severity.

It falls through:

- Public works.
- Reopened industrial states.
- Stable military demand when supply is secure.
- Foreign reconstruction orders.
- Social relief that preserves purchasing power.
- Successful local employment projects.

### Trade and external-finance stress

Represents lost export markets, collapsed trade credit, foreign-exchange pressure, blocked imports, convoy losses, failed clearing arrangements, and dependence on a distressed partner.

It rises through:

- Port or convoy disruption.
- Blockade.
- Loss of trade access.
- Evolution I contagion.
- Evolution III world contraction.
- Dependence on one supplier or market that becomes unavailable.
- Sanctions or embargoes that have an exact registered source.

It falls through:

- Restored ports and convoys.
- Clearing agreements.
- Diversified imports.
- A foreign aid corridor.
- A stable supplier relationship.
- Recovery of exposed partners.

### Industrial and logistics disruption

Represents lost industrial states, broken railways, damaged infrastructure, bombing, natural disasters, fuel shortages, train shortages, and supply-chain interruption.

It rises through:

- Loss or occupation of a Depression Center.
- Damage to factories, railways, ports, infrastructure, or supply hubs.
- Low trains, trucks, fuel, or convoys relative to the country's burden.
- Failed center protection.
- An Event 34 inherited network collapse.
- Registered natural-disaster or strategic-attack shocks.

It falls through:

- Restored state control.
- Railway and infrastructure repair.
- Protected industrial regions.
- Adequate logistics reserves.
- Successful strategic-industry rescue.
- Completed public works that solve an identified bottleneck.

### Fiscal and policy stress

Represents the cost of relief, debt service, emergency subsidies, administrative overload, expensive economic laws, policy contradiction, and the inability to finance every intervention.

It rises through:

- Several expensive programs at once.
- Emergency economic laws unsupported by production.
- Frequent changes in recovery doctrine.
- Failed public commitments.
- Prolonged high-cost rescue policy.
- Large subject or ally support burdens.

It falls through:

- A credible budget settlement.
- Prioritization of a smaller set of programs.
- Debt restructuring.
- Recovered tax and production capacity.
- Austerity that does not trigger a larger demand collapse.
- External grants or aid that have a real provider.

### Social confidence and institutional stress

Represents confidence in the government, willingness to keep deposits and contracts in normal channels, labor peace, public patience, and the ability of institutions to carry out policy.

It rises through:

- Falling stability.
- Repeated failed missions.
- Long unemployment in the same regions.
- Repression, riots, and unresolved strikes.
- Corruption or exposed favoritism.
- A failed government or cabinet crisis.

It falls through:

- Clear and sustained recovery policy.
- Reopened centers.
- Negotiated labor settlements.
- Visible employment gains.
- High stability.
- Successful relief and confidence actions.
- Recovery without unexplained policy reversals.

### War-demand relief and war burden

War is evaluated as a mixed internal factor instead of a flat modifier.

War demand can lower demand and employment stress when:

- Military factories have secure inputs.
- The country controls its industrial regions.
- Supply and fuel are adequate.
- Foreign or domestic orders are rising.
- The state can protect civilian consumption from total collapse.

War burden raises Severity when:

- Ports, convoys, fuel, trains, or imported resources are failing.
- Core industrial states are bombed or occupied.
- The country has severe equipment and manpower shortages.
- Civilian construction is fully displaced by emergency demand.
- The government maintains expensive laws that the depressed economy cannot support.

## Severity evaluation pulse

Event 35 uses a sparse active-country schedule. Only countries with an active national crisis, a registered contagion condition, or Evolution III pressure are evaluated. The event must not introduce an unauthorized recurring scan across every country.

The normal national evaluation cadence is dynamic but bounded. Panic and Contraction or Economic Paralysis normally schedule the next pulse in `3` to `5` days. Sustained Depression normally uses about `7` days. Stabilization normally uses `10` to `14` days, while final recovery proof uses `7` to `10` days. A new major shock or highly volatile trend can shorten the next interval. Immediate decisions, state loss, registered attacks, inherited Event 34 collapse, and other exact shocks may update Severity between scheduled evaluations.

Only one next-pulse receipt may exist for one country and episode. Cadence changes reschedule that country instead of stacking parallel timers. The drift calculation normalizes pressure by elapsed days so a shorter emergency cadence does not multiply the seven-day-equivalent pressure.

Each normal pulse follows this logic:

1. Read the current phase and Severity band.
2. Rebuild the hidden material contributors from current country and registered state conditions.
3. Add active policy pressure and relief.
4. Apply external-shock memories that have not expired.
5. Apply evolution-specific pressure.
6. Calculate a bounded Severity change.
7. Clamp the value between `0` and `100`.
8. Update the short trend history.
9. Check one-shot thresholds, phase progress, missions, state progression, and incidents.
10. Schedule the next active-country pulse.

Normal drift should usually be small enough that decisions and external shocks remain meaningful. One scheduled pulse should not move the country from Deep Depression to the Recovery Floor without a major mission result. Large changes belong to opening shock conversion, a serious state loss, Event 34 collapse, a bank panic, a coordinated rescue, or another visible incident.

## Drift structure

The implementation should calculate a net pressure score from hidden contributors, then convert it into one bounded Severity change.

A useful initial structure is:

```text
base phase pressure
+ credit and banking pressure
+ demand and employment pressure
+ trade and external pressure
+ industrial and logistics pressure
+ fiscal and policy pressure
+ social and institutional pressure
+ evolution pressure
+ recent shock memory
- active relief
- completed project relief
- stable war demand relief
- foreign support
= net pressure
```

The net score should map to a limited seven-day equivalent movement band, then scale by the actual bounded interval. The exact mapping belongs in script constants. As a starting balance target:

- Very strong recovery conditions can lower Severity by roughly `2` to `4` in a week.
- Normal successful policy lowers it by roughly `1` to `2`.
- A broadly balanced week moves it by `0` or `1`.
- Material deterioration raises it by roughly `1` to `3`.
- A severe registered shock may raise it by `4` to `10` immediately.

These are tuning targets, not player-facing promises. They prevent one ordinary pulse from deciding the whole event.

## Public trend

The trend is derived from recent Severity movement and material shock state. It is qualitative.

| Working trend | Meaning | Suggested evidence window |
| --- | --- | --- |
| Rapidly Improving | Several recent pulses and missions produced strong net relief | Last three normal pulses plus current mission result |
| Improving | Recent net movement is clearly downward | Last three normal pulses |
| Stable | Movement is small or alternating | Last three normal pulses |
| Worsening | Recent net movement is clearly upward | Last three normal pulses |
| Accelerating | Worsening pressure is increasing or a major unresolved shock is active | Last three pulses plus shock memory |

The category should pair the label with an icon or arrow. Color is supporting information. The player must not need color vision to understand the direction.

The public cause list shows no more than three current reasons. It should prefer causes the player can act on. Examples include frozen credit, shuttered industrial regions, broken freight, blockade, war orders, public works, stable banking, or foreign support. It should not show raw formulas or every minor contributor.

## Independent starting Severity

An independent firing begins in a severe but recoverable range. The initial target is usually between `58` and `74`.

Starting Severity rises with:

- Falling or very low stability.
- A major industrial state recently lost or damaged.
- Severe blockade or trade disruption.
- Low trains, convoys, or fuel relative to need.
- Existing famine, migration, or humanitarian pressure with a valid shared context.
- A recent failed economic recovery.
- A prior hollow Event 35 outcome.
- An expensive war that has lost its supply base.

Starting Severity falls with:

- Strong reserves and infrastructure.
- Secure trade and ports.
- Stable government.
- Earlier durable recovery reforms.
- A recent successful Event 34 controlled landing without collapse.
- A small industrial base that cannot support the normal upper opening range.

The independent path should not start below the normal Depression band. Event 35 must change production and construction planning from its first day.

## Inherited starting Severity

An Event 34 collapse begins from the frozen boom snapshot. The initial target can range from the upper Depression band to near Economic Paralysis.

The calculation must use:

- Final Overheating.
- Peak Overheating.
- Time spent in dangerous Overheating bands.
- Final Overheating trend.
- Boom evolution floor.
- Reserve condition.
- Controlled-landing preparation and failure state.
- Number and condition of Industrial Regions.
- Completed, protected, speculative, unfinished, fragile, or abandoned projects.
- Event 34 external shocks.
- Earlier boom crashes and depression episodes.
- Current stability, trade, logistics, and state control.

A high Overheating number alone must not determine the result. A country that built reserves, protected regions, and attempted a landing should begin below an equally overheated country that ran without reserves and lost its core industrial network.

Suggested inherited entry bands:

| Snapshot result | Starting Severity direction |
| --- | --- |
| Baseline crash with reserves and partial landing preparation | Severe but recoverable |
| Baseline or Evolution I crash with weak reserves and speculative exposure | Deep Depression |
| Evolution II crash with fragile Miracle Regions | Systemic Breakdown |
| Evolution III network collapse with failed emergency halt | Very high Systemic Breakdown or Economic Paralysis |

## Contagion and worldwide conversion starts

A country that converts from Economic Contagion usually starts lower than the origin country. Its initial range should reflect local vulnerability and the strength of the connection. A stable country with one exposed market can begin around the Fragile Economy or lower Depression bands. A dependent subject, lender, or trade hub with several failed links can begin in Deep Depression.

Evolution III conversion uses the worldwide pressure state plus local vulnerability. It must not give every country the same starting value. Self-sufficient, stable, and lightly connected countries should remain under the lighter global condition for longer. Highly connected or already unstable countries may enter the full crisis quickly.

## Immediate shocks

An immediate shock is a one-time or short-memory change tied to a visible event. It must have an exact source and a repeat guard.

### Supported shock families

- Loss of a Depression Center.
- Destruction or heavy damage in a registered industrial state.
- Port, convoy, rail, supply-hub, or infrastructure collapse.
- Bank panic or credit freeze.
- Trade or clearing agreement failure.
- Major policy reversal.
- Failed recovery mission.
- Event 34 collapse.
- Contagion from a registered source country.
- Evolution III world-market contraction.
- Postwar cancellation of military orders.
- A registered embargo or sanction with a material economic effect.

### Shock memory

A severe shock can affect several following pulses without reapplying its full immediate value. The event records a decaying shock memory. It is cleared after its defined duration or after a direct recovery action resolves it.

The same state loss, bank failure, or mission failure cannot create a new full shock every pulse. A new shock requires a new receipt, new source, or new threshold.

## Threshold behavior

Thresholds change available content and modifiers. Crossing a threshold is recorded once in each direction where useful.

### Crossing into Deep Depression

- Stronger national penalties apply.
- A second Depression Center may be selected for a large economy if the normal cap allows it.
- Emergency finance, employment, or freight actions become more important.
- Evolution I spread receives more source pressure when active.

### Crossing into Systemic Breakdown

- Ordinary aggressive or low-urgency actions are hidden.
- Emergency recovery missions replace them.
- Depression Centers can progress toward shuttering after sustained exposure.
- Baseline strikes, radicalization, cabinet crises, and National Breakdown warnings become eligible through their own strict conditions.
- Social incidents receive stronger valid weights and use the organized movement ladder when Evolution II is active.
- The country can no longer change doctrine freely.

### Reaching Economic Paralysis

- Apply the deepest national dynamic modifier once.
- Start one maximum-Severity emergency objective.
- Freeze repeated destructive threshold effects behind receipts and cooldowns.
- Allow limited emergency aid and forced stabilization actions even for a country with little remaining civilian capacity.
- Keep the country playable.

### Falling below the Stabilization threshold

- Start or advance the sustained stabilization timer.
- Weaken the harshest penalties gradually.
- Unlock center reopening and policy consolidation.
- Do not close the crisis yet.

### Reaching the Recovery Floor

- Start the final recovery proof only when required centers and emergencies are resolved.
- A single shock can pause or reset the proof.
- The active event closes only after the proof duration is complete.

## Phase timers and proof periods

Initial tuning targets:

- Panic and Contraction minimum duration: about `35` days.
- Stabilization qualification: Severity below `40` for about `42` consecutive days.
- Recovery Floor proof: Severity at or below `14` for about `60` consecutive days.
- Post-recovery safeguard against independent refiring: at least `180` days, increasing modestly after repeated episodes.

The implementation may tune these values through constants. It must preserve the need for sustained improvement.

## Relapse

A relapse is a return from Stabilization to Depression after the economy appeared to be recovering.

Relapse can occur when:

- Severity returns to `50` or higher.
- Severity remains above the stabilizing range for a sustained period.
- A required center closes again.
- A major bank, trade, or war shock occurs.
- The player withdraws support before completing the recovery proof.
- Evolution I or III creates a new external contraction.

The player receives a visible fragile-recovery status before normal drift alone can cause relapse. A sudden major shock may trigger it immediately. The relapse removes accumulated proof progress and restores the appropriate sustained penalties. It does not repeat the full opening shock unless a new crisis source justifies one.

## Maximum-Severity emergency

The maximum-Severity objective should last long enough to permit response, normally between `90` and `150` days depending on country capacity and active evolutions.

Success requires a combination of:

- A material Severity reduction.
- At least one operating or protected Depression Center.
- No unresolved bank panic or freight collapse.
- Payment of the selected emergency policy's real costs.

Success returns the country to Systemic Breakdown or Deep Depression with a temporary no-relapse breathing period. It does not end Event 35.

Failure may:

- Shutter one eligible Depression Center.
- Apply a bounded factory or infrastructure loss in an already distressed state.
- Trigger a baseline government crisis or advance the visible National Breakdown warning.
- Call the rare baseline civil-conflict validator after the full gate and failed prevention objective.
- Activate or advance the organized Social Collapse ladder when Evolution II conditions are met.
- Increase international pressure when Evolution I or III is active.

Failure does not repeat automatically while Severity remains at `100`. A new maximum-Severity emergency requires a cooldown and a new failure condition. The baseline civil-conflict validator can return a nonwar political outcome when the actor, territory, force, or recent-war requirements are not met.

## Baseline National Breakdown gate

The baseline political failure route uses a separate guarded state, not a hidden automatic threshold effect.

Initial tuning direction:

- Severity near `95` or higher for about `90` to `120` consecutive days.
- Very low stability or a proved government-legitimacy failure.
- At least two failed major recovery, emergency, or political responses.
- One coherent opposing political or military base.
- At least one valid territorial and force package.
- No recent civil war or protected aftermath.

The warning state starts Prevent National Breakdown. Success clears the immediate breakdown risk and applies a cooldown. Failure makes civil conflict eligible, but does not guarantee it. The final outcome can be a government replacement, emergency rule, policy reversal, prolonged unrest, or civil conflict according to the validated country state.

When Evolution II is active, Social Collapse owns the movement, coup, separatist, and civil-conflict outcome selection. The baseline gate is suspended so the same economic failure cannot create two political chains.

## National penalty model

Use one event-owned dynamic modifier or a small staged family that reads Severity and phase. Do not stack one separate national spirit for every threshold.

The model should affect:

- Factory output.
- Production-efficiency growth.
- Usable production-efficiency ceiling where appropriate.
- Construction speed.
- Civilian economic capacity.
- Trade and logistics resilience.
- Stability pressure.
- Political or law-maintenance pressure where supported.

The opening shock is a separate short modifier because it is intentionally harsher than the sustained state. Recovery legacies and scars are separate because they persist after the active crisis.

At severe levels, the player should need to change production and construction plans. At maximum Severity, ordinary output may approach paralysis. The event must preserve enough residual capacity, emergency aid access, or scaled-down action costs to avoid a scripted soft lock.

## Severity reduction cannot be purchased directly

No decision should be a simple political-power purchase that removes a large fixed amount of Severity. Every large reduction must come from a policy action, state project, foreign agreement, emergency mission, or accepted sacrifice with real requirements and time.

Small immediate changes are acceptable when they represent the first effect of a larger action. The main result should be delivered through sustained relief, project completion, or mission success.

## Scaling and fairness

Costs and relief scale from the target country's usable economy, not raw total factories alone. A depressed country with many locked factories must not receive costs calculated as if every factory were available.

The implementation should consider:

- Total and usable civilian factories.
- Total and usable military factories.
- Number of Depression Centers.
- Severity band.
- Current war state.
- Stockpile floors.
- Country size.
- Player or AI control.
- Prior failed actions.

A small player country must have a viable one-center recovery loop. A large major must pay more and manage more regional exposure. The event should remain serious in both cases.

## Save continuity and reconciliation

On load or runtime rebuild, Event 35 must reconcile:

- Active crisis flag and episode ID.
- Current Severity and phase.
- Recent trend history.
- Active shock memories.
- Doctrine and policy history.
- Depression Center registry.
- Evolution floor and active evolution modules.
- Contagion source and exposure links.
- Stabilization and recovery proof progress.
- Maximum-Severity receipt and cooldown.

Missing or malformed history should fail closed into a safe active crisis state. It must not reset Severity to zero, duplicate the opening shock, repeat threshold damage, or create a second category.

## Tuning ownership

All thresholds, duration bands, maximum changes, scaling steps, caps, AI weights, and evolution multipliers belong in Event 35 script constants or another documented tuning surface. The design should avoid scattered literals across events, decisions, effects, triggers, and localisation.

The implementation report must list the final constants and the scenario evidence used to tune them.
